from flask import Flask, render_template, request, session, redirect, url_for
import veritabani as db
import bolumler as bl
import oyun_verileri as ov
import json

app = Flask(__name__)
app.secret_key = "cok-gizli-bir-anahtar-degistir-bunu"


# ============================================
# YARDIMCI FONKSİYONLAR
# ============================================

def atama_listesi_getir(ana_bolum, ara_bolum):
    """Belirli bir ara bölümdeki oyun atamalarını getir."""
    conn = db.baglan()
    imlec = conn.cursor()
    imlec.execute("""
        SELECT id, sira, oyun_no, ozel_veri
        FROM oyun_atamalari
        WHERE ana_bolum = ? AND ara_bolum = ?
        ORDER BY sira
    """, (ana_bolum, ara_bolum))
    sonuclar = [dict(r) for r in imlec.fetchall()]
    conn.close()
    return sonuclar


def tum_atamalar_getir():
    """Tüm atamaları {ana: {ara: [atamalar]}} yapısında getir."""
    conn = db.baglan()
    imlec = conn.cursor()
    imlec.execute("""
        SELECT id, ana_bolum, ara_bolum, sira, oyun_no, ozel_veri
        FROM oyun_atamalari
        ORDER BY ana_bolum, ara_bolum, sira
    """)
    yerlesim = {}
    for r in imlec.fetchall():
        ana = r["ana_bolum"]
        ara = r["ara_bolum"]
        if ana not in yerlesim:
            yerlesim[ana] = {}
        if ara not in yerlesim[ana]:
            yerlesim[ana][ara] = []
        yerlesim[ana][ara].append(dict(r))
    conn.close()
    return yerlesim


def atama_var_mi(ana_bolum, ara_bolum):
    """Bu ara bölümde atama var mı?"""
    conn = db.baglan()
    imlec = conn.cursor()
    imlec.execute(
        "SELECT COUNT(*) as s FROM oyun_atamalari WHERE ana_bolum = ? AND ara_bolum = ?",
        (ana_bolum, ara_bolum)
    )
    sonuc = imlec.fetchone()["s"]
    conn.close()
    return sonuc > 0


def rozet_kontrol(ogrenci_id):
    """
    Öğrencinin bitirdiği ana bölümleri kontrol eder,
    yeni rozet kazanılmışsa rozetler tablosuna ekler.
    """
    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("""
        SELECT ana_bolum, COUNT(DISTINCT ara_bolum) as tamamlanan
        FROM ilerleme
        WHERE ogrenci_id = ? AND tamamlandi = 1
        GROUP BY ana_bolum
    """, (ogrenci_id,))

    biten_bolumler = set()
    for s in imlec.fetchall():
        if s["tamamlanan"] >= bl.ARA_BOLUM_SAYISI:
            biten_bolumler.add(s["ana_bolum"])

    imlec.execute(
        "SELECT rozet_adi FROM rozetler WHERE ogrenci_id = ?",
        (ogrenci_id,)
    )
    mevcut_rozetler = {r["rozet_adi"] for r in imlec.fetchall()}

    yeni_rozetler = []
    for b in bl.ANA_BOLUMLER:
        if b["no"] in biten_bolumler:
            rozet_adi = b["rozet"]
            if rozet_adi not in mevcut_rozetler:
                imlec.execute(
                    "INSERT INTO rozetler (ogrenci_id, rozet_adi) VALUES (?, ?)",
                    (ogrenci_id, rozet_adi)
                )
                yeni_rozetler.append(rozet_adi)

    conn.commit()
    conn.close()
    return yeni_rozetler

def seri_guncelle(ogrenci_id):
    """
    Öğrencinin seri bilgisini günceller.
    - Bugün ilk oyun ise ve dün de oynadıysa → seri +1
    - Bugün ilk oyun ise ve dün oynamadıysa → seri = 1
    - Bugün zaten oynadıysa → hiçbir şey yapma
    """
    from datetime import date, timedelta
    bugun = date.today().isoformat()       # "2026-10-01"
    dun = (date.today() - timedelta(days=1)).isoformat()

    conn = db.baglan()
    imlec = conn.cursor()

    # Mevcut durumu al
    imlec.execute(
        "SELECT seri_gun, son_oynama_tarihi FROM kullanicilar WHERE id = ?",
        (ogrenci_id,)
    )
    satir = imlec.fetchone()
    if not satir:
        conn.close()
        return 0

    mevcut_seri = satir["seri_gun"] or 0
    son_tarih = satir["son_oynama_tarihi"]

    yeni_seri = mevcut_seri

    if son_tarih == bugun:
        # Bugün zaten oynadı, değişiklik yok
        pass
    elif son_tarih == dun:
        # Dün oynamıştı, seri +1
        yeni_seri = mevcut_seri + 1
    else:
        # İlk kez veya seri bozulmuş, seri 1'den başlar
        yeni_seri = 1

    imlec.execute(
        "UPDATE kullanicilar SET seri_gun = ?, son_oynama_tarihi = ? WHERE id = ?",
        (yeni_seri, bugun, ogrenci_id)
    )
    conn.commit()
    conn.close()
    return yeni_seri

def yonlendir_rol(rol):
    """Kullanıcı rolüne göre doğru sayfaya yönlendir."""
    if rol == "admin":
        return redirect(url_for("admin_panel"))
    elif rol == "ogretmen":
        return redirect(url_for("ogretmen_panel"))
    else:
        return redirect(url_for("harita"))


# ============================================
# AVATAR SEÇENEKLERİ
# ============================================

AVATAR_SECENEKLERI = [
    "🦁", "🐯", "🐻", "🐼", "🐨", "🐸", "🐵", "🦊",
    "🐶", "🐱", "🐰", "🐭", "🐹", "🦄", "🐲", "🦉",
    "🚀", "⭐", "🌟", "🪐", "🌙", "☄️", "🛸", "👽",
    "🌲", "🌳", "🌻", "🌺", "🍀", "🌈", "❄️", "🔥",
    "🦸", "🦹", "🧙", "🧚", "🧜", "🧞", "🧝", "🎅",
    "⚽", "🏀", "🎾", "🏈", "🎯", "🥇", "🏆", "🎮",
    "🧑‍🎓", "👦", "👧", "🧒", "👶", "🧑",
]


# ============================================
# GENEL ROUTE'LAR
# ============================================

@app.route("/")
def ana_sayfa():
    """Karşılama (welcome) sayfası."""
    if "kullanici_id" in session:
        return yonlendir_rol(session["rol"])

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("SELECT COUNT(*) as s FROM kullanicilar WHERE rol = 'ogrenci'")
    ogrenci_sayi = imlec.fetchone()["s"]

    imlec.execute("SELECT COUNT(*) as s FROM ilerleme WHERE tamamlandi = 1")
    toplam_oyun = imlec.fetchone()["s"]

    imlec.execute("SELECT COUNT(*) as s FROM rozetler")
    toplam_rozet = imlec.fetchone()["s"]

    conn.close()

    return render_template(
        "welcome.html",
        ogrenci_sayi=ogrenci_sayi,
        toplam_oyun=toplam_oyun,
        toplam_rozet=toplam_rozet,
        toplam_oyun_tipi=len(bl.OYUNLAR),
        toplam_bolum=len(bl.ANA_BOLUMLER),
        toplam_seviye=len(bl.ANA_BOLUMLER) * bl.ARA_BOLUM_SAYISI,
    )


@app.route("/giris-sayfasi")
def giris_sayfasi():
    """Giriş formunu gösteren sayfa."""
    if "kullanici_id" in session:
        return yonlendir_rol(session["rol"])
    return render_template("giris.html")


@app.route("/giris", methods=["POST"])
def giris_yap():
    kullanici_adi = request.form.get("kullanici_adi", "").strip()
    sifre = request.form.get("sifre", "")

    conn = db.baglan()
    imlec = conn.cursor()
    imlec.execute(
        "SELECT * FROM kullanicilar WHERE kullanici_adi = ? AND sifre = ?",
        (kullanici_adi, sifre)
    )
    kullanici = imlec.fetchone()
    conn.close()

    if kullanici:
        session["kullanici_id"] = kullanici["id"]
        session["kullanici_adi"] = kullanici["kullanici_adi"]
        session["rol"] = kullanici["rol"]
        session["ad_soyad"] = kullanici["ad_soyad"]
        session["avatar"] = kullanici["avatar"] if "avatar" in kullanici.keys() and kullanici["avatar"] else "🧑‍🎓"
        return yonlendir_rol(kullanici["rol"])
    else:
        return render_template("giris.html", hata="Kullanıcı adı veya şifre yanlış!")


@app.route("/cikis")
def cikis():
    session.clear()
    return redirect(url_for("ana_sayfa"))


# ============================================
# ÖĞRENCİ ROUTE'LARI
# ============================================

@app.route("/harita")
def harita():
    if session.get("rol") != "ogrenci":
        return redirect(url_for("ana_sayfa"))

    ogrenci_id = session["kullanici_id"]
    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("""
        SELECT ana_bolum, COUNT(DISTINCT ara_bolum) as tamamlanan
        FROM ilerleme
        WHERE ogrenci_id = ? AND tamamlandi = 1
        GROUP BY ana_bolum
    """, (ogrenci_id,))
    satirlar = imlec.fetchall()

    biten_bolumler = set()
    for s in satirlar:
        if s["tamamlanan"] >= bl.ARA_BOLUM_SAYISI:
            biten_bolumler.add(s["ana_bolum"])

    imlec.execute(
        "SELECT COALESCE(SUM(yildiz), 0) as toplam FROM ilerleme WHERE ogrenci_id = ?",
        (ogrenci_id,)
    )
    yildiz_sayisi = imlec.fetchone()["toplam"]

    imlec.execute(
        "SELECT rozet_adi FROM rozetler WHERE ogrenci_id = ? ORDER BY tarih",
        (ogrenci_id,)
    )
    # Rozetleri ikonlu hale getir
    rozetler = []
    for r in imlec.fetchall():
        ad = r["rozet_adi"]
        ikon = bl.ROZET_IKONLARI.get(ad, "🏅")
        rozetler.append({"ad": ad, "ikon": ikon})

    imlec.execute("""
        SELECT COUNT(DISTINCT oyun_no || '-' || ana_bolum || '-' || ara_bolum) as sayi
        FROM ilerleme
        WHERE ogrenci_id = ?
          AND tamamlandi = 1
          AND DATE(tarih, 'localtime') = DATE('now', 'localtime')
    """, (ogrenci_id,))
    bugun_oynanan = imlec.fetchone()["sayi"]

        # Günlük hedef (şimdilik 3)
    gunluk_hedef = 3

    # Seri bilgisi
    imlec.execute(
        "SELECT seri_gun, son_oynama_tarihi FROM kullanicilar WHERE id = ?",
        (ogrenci_id,)
    )
    seri_satir = imlec.fetchone()
    seri_gun = seri_satir["seri_gun"] if seri_satir and seri_satir["seri_gun"] else 0
    son_oynama = seri_satir["son_oynama_tarihi"] if seri_satir else None

    # Bugün oynamadıysa seri aslında kırılmış olabilir — bunu kontrol et
    from datetime import date, timedelta
    bugun = date.today().isoformat()
    dun = (date.today() - timedelta(days=1)).isoformat()
    if son_oynama and son_oynama not in (bugun, dun):
        # Bugün veya dün değilse seri kırılmıştır (görsel olarak 0 göster)
        # Ama veritabanındaki değeri hemen silmiyoruz, oyun oynayınca düzelir
        seri_gun_goster = 0
    else:
        seri_gun_goster = seri_gun
        # Takılı ekipmanları al
    imlec.execute("""
        SELECT ekipman_no FROM ogrenci_ekipman
        WHERE ogrenci_id = ? AND takili = 1
    """, (ogrenci_id,))
    takili_ekipman_nolar = [r["ekipman_no"] for r in imlec.fetchall()]

    # Kategorilere göre ayır
    takili_ekipmanlar = {
        "sapka": None,
        "gozluk": None,
        "el": None,
        "boyun": None,
        "sirt": None,
    }
    for no in takili_ekipman_nolar:
        e = bl.EKIPMANLAR.get(no)
        if e and e["kategori"] in takili_ekipmanlar:
            takili_ekipmanlar[e["kategori"]] = {
                "emoji": e["emoji"],
                "ad": e["ad"],
                "no": no,
            }

    conn.close()

    bolum_listesi = []
    for b in bl.ANA_BOLUMLER:
        no = b["no"]
        acik = (no == 1) or ((no - 1) in biten_bolumler)
        bitti = no in biten_bolumler
        bolum_listesi.append({**b, "acik": acik, "bitti": bitti})

    rutbe = "Acemi Kâşif"
    for r in bl.RUTBELER:
        if all(bn in biten_bolumler for bn in r["bolumler"]):
            rutbe = f"{r['sembol']} {r['ad']}"

    return render_template(
        "harita.html",
        bolumler=bolum_listesi,
        yildiz_sayisi=yildiz_sayisi,
        rozetler=rozetler,
        rutbe=rutbe,
        ad_soyad=session.get("ad_soyad", "Öğrenci"),
        avatar=session.get("avatar", "🧑‍🎓"),
        avatar_secenekleri=AVATAR_SECENEKLERI,
        bugun_oynanan=bugun_oynanan,
        gunluk_hedef=gunluk_hedef,
        seri_gun=seri_gun_goster,
        seri_bugun_oynadi=(son_oynama == bugun),
        takili_ekipmanlar=takili_ekipmanlar,
    )


@app.route("/bolum/<int:no>")
def bolum_detay(no):
    if session.get("rol") != "ogrenci":
        return redirect(url_for("ana_sayfa"))

    bolum = bl.ana_bolum_getir(no)
    if not bolum:
        return "Bölüm bulunamadı", 404

    ogrenci_id = session["kullanici_id"]
    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("""
        SELECT ara_bolum, COUNT(DISTINCT oyun_no) as tamamlanan_oyun
        FROM ilerleme
        WHERE ogrenci_id = ? AND ana_bolum = ? AND tamamlandi = 1
        GROUP BY ara_bolum
    """, (ogrenci_id, no))
    biten_ara = {s["ara_bolum"] for s in imlec.fetchall()}

    ara_bolumler = []
    for ara_no in range(1, bl.ARA_BOLUM_SAYISI + 1):
        atamalar = atama_listesi_getir(no, ara_no)
        oyun_sayisi = len(atamalar)

        imlec.execute("""
            SELECT COUNT(DISTINCT oyun_no) as bitirilen
            FROM ilerleme
            WHERE ogrenci_id = ? AND ana_bolum = ? AND ara_bolum = ? AND tamamlandi = 1
        """, (ogrenci_id, no, ara_no))
        bitirilen = imlec.fetchone()["bitirilen"]

        bitti = (oyun_sayisi > 0) and (bitirilen >= oyun_sayisi)
        acik = (ara_no == 1) or ((ara_no - 1) in biten_ara)

        ara_bolumler.append({
            "no": ara_no,
            "ad": f"Görev {ara_no}",
            "emoji": "📖",
            "acik": acik,
            "bitti": bitti,
            "oyun_sayisi": oyun_sayisi,
        })

    conn.close()

    tamamlanan = sum(1 for a in ara_bolumler if a["bitti"])
    yuzde = int(tamamlanan / bl.ARA_BOLUM_SAYISI * 100)

    return render_template(
        "ara_bolum.html",
        bolum=bolum,
        ara_bolumler=ara_bolumler,
        tamamlanan=tamamlanan,
        yuzde=yuzde,
    )


@app.route("/bolum/<int:ana_no>/ara/<int:ara_no>")
def oyun_listesi(ana_no, ara_no):
    if session.get("rol") != "ogrenci":
        return redirect(url_for("ana_sayfa"))

    bolum = bl.ana_bolum_getir(ana_no)
    if not bolum:
        return "Bölüm bulunamadı", 404

    atamalar = atama_listesi_getir(ana_no, ara_no)

    ogrenci_id = session["kullanici_id"]
    conn = db.baglan()
    imlec = conn.cursor()
    imlec.execute("""
        SELECT oyun_no, MAX(yildiz) as yildiz
        FROM ilerleme
        WHERE ogrenci_id = ? AND ana_bolum = ? AND ara_bolum = ? AND tamamlandi = 1
        GROUP BY oyun_no
    """, (ogrenci_id, ana_no, ara_no))
    ilerleme_dict = {s["oyun_no"]: s["yildiz"] for s in imlec.fetchall()}
    conn.close()

    oyunlar = []
    for a in atamalar:
        o = bl.oyun_getir(a["oyun_no"])
        if not o:
            continue
        bitti = a["oyun_no"] in ilerleme_dict
        oyunlar.append({
            **o,
            "no": a["oyun_no"],
            "atama_id": a["id"],
            "bitti": bitti,
            "kazanilan_yildiz": ilerleme_dict.get(a["oyun_no"], 0),
        })

    return render_template(
        "oyun_listesi.html",
        bolum=bolum,
        ara_no=ara_no,
        oyunlar=oyunlar,
    )


@app.route("/oyun/<int:ana_no>/<int:ara_no>/<int:oyun_no>")
def oyun_oyna(ana_no, ara_no, oyun_no):
    """Bir oyunu başlat."""
    if session.get("rol") != "ogrenci":
        return redirect(url_for("ana_sayfa"))

    oyun = bl.oyun_getir(oyun_no)
    if not oyun:
        return "Oyun bulunamadı", 404

    oyun = {**oyun, "no": oyun_no}

    atamalar = atama_listesi_getir(ana_no, ara_no)
    if not any(a["oyun_no"] == oyun_no for a in atamalar):
        return "Bu oyun bu bölümde değil", 404

    ozel_veri_json = None
    for a in atamalar:
        if a["oyun_no"] == oyun_no:
            ozel_veri_json = a.get("ozel_veri")
            break

    if ozel_veri_json:
        try:
            sorular = json.loads(ozel_veri_json)
        except Exception:
            sorular = ov.oyun_sorulari_karistir(oyun_no, adet=5)
    else:
        sorular = ov.oyun_sorulari_karistir(oyun_no, adet=5)

    if not sorular:
        return "Bu oyunun soruları henüz hazırlanmadı", 404

    return render_template(
        "oyun.html",
        oyun=oyun,
        ana_no=ana_no,
        ara_no=ara_no,
        sorular=sorular,
    )


@app.route("/oyun/kaydet", methods=["POST"])
def oyun_kaydet():
    """Oyun sonucunu veritabanına kaydet."""
    if session.get("rol") != "ogrenci":
        return {"hata": "Yetkisiz"}, 401

    veri = request.get_json()
    if not veri:
        return {"hata": "Veri yok"}, 400

    ogrenci_id = session["kullanici_id"]
    ana_bolum = veri.get("ana_bolum")
    ara_bolum = veri.get("ara_bolum")
    oyun_no = veri.get("oyun_no")
    yildiz = veri.get("yildiz", 0)

    if yildiz < 1:
        return {"mesaj": "Yıldız yok, kaydedilmedi"}, 200

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("""
        SELECT id, yildiz FROM ilerleme
        WHERE ogrenci_id = ? AND ana_bolum = ? AND ara_bolum = ? AND oyun_no = ?
    """, (ogrenci_id, ana_bolum, ara_bolum, oyun_no))
    mevcut = imlec.fetchone()

    if mevcut:
        if yildiz > mevcut["yildiz"]:
            imlec.execute(
                "UPDATE ilerleme SET yildiz = ?, tamamlandi = 1, tarih = CURRENT_TIMESTAMP WHERE id = ?",
                (yildiz, mevcut["id"])
            )
            mesaj = "Yıldız güncellendi!"
        else:
            mesaj = "Mevcut yıldız korundu"
    else:
        imlec.execute("""
            INSERT INTO ilerleme (ogrenci_id, ana_bolum, ara_bolum, oyun_no, yildiz, tamamlandi)
            VALUES (?, ?, ?, ?, ?, 1)
        """, (ogrenci_id, ana_bolum, ara_bolum, oyun_no, yildiz))
        mesaj = "İlk kez kaydedildi!"

    conn.commit()
    conn.close()

    # Rozet kontrolü
    yeni_rozetler = rozet_kontrol(ogrenci_id)

    # Seri güncelleme
    yeni_seri = seri_guncelle(ogrenci_id)

    return {
        "mesaj": mesaj,
        "yildiz": yildiz,
        "yeni_rozetler": yeni_rozetler,
        "seri_gun": yeni_seri
    }, 200


@app.route("/avatar-guncelle", methods=["POST"])
def avatar_guncelle():
    """Öğrencinin avatarını güncelle."""
    if "kullanici_id" not in session:
        return {"hata": "Giriş yapmamışsın"}, 401

    veri = request.get_json()
    yeni_avatar = veri.get("avatar", "").strip()

    if yeni_avatar not in AVATAR_SECENEKLERI:
        return {"hata": "Geçersiz avatar"}, 400

    conn = db.baglan()
    imlec = conn.cursor()
    imlec.execute(
        "UPDATE kullanicilar SET avatar = ? WHERE id = ?",
        (yeni_avatar, session["kullanici_id"])
    )
    conn.commit()
    conn.close()

    session["avatar"] = yeni_avatar
    return {"mesaj": "Avatar güncellendi!", "avatar": yeni_avatar}, 200


@app.route("/siralama")
def siralama():
    """Sınıftaki öğrencilerin yıldız sıralaması."""
    if "kullanici_id" not in session:
        return redirect(url_for("ana_sayfa"))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("""
        SELECT
            k.id,
            k.kullanici_adi,
            k.ad_soyad,
            k.avatar,
            COALESCE(SUM(i.yildiz), 0) as toplam_yildiz,
            COUNT(DISTINCT r.id) as rozet_sayisi
        FROM kullanicilar k
        LEFT JOIN ilerleme i ON i.ogrenci_id = k.id AND i.tamamlandi = 1
        LEFT JOIN rozetler r ON r.ogrenci_id = k.id
        WHERE k.rol = 'ogrenci'
        GROUP BY k.id
        ORDER BY toplam_yildiz DESC, rozet_sayisi DESC, k.ad_soyad ASC
    """)
    ogrenciler = [dict(r) for r in imlec.fetchall()]
    conn.close()

    for i, o in enumerate(ogrenciler, start=1):
        o["sira"] = i

    aktif_rol = session.get("rol")
    kendi_sira = None
    if aktif_rol == "ogrenci":
        kendi_id = session.get("kullanici_id")
        for o in ogrenciler:
            if o["id"] == kendi_id:
                kendi_sira = o["sira"]
                break

    return render_template(
        "siralama.html",
        ogrenciler=ogrenciler,
        kendi_sira=kendi_sira,
        aktif_rol=aktif_rol,
        kullanici_id=session.get("kullanici_id"),
    )

# ============================================
# HAFTALIK ÖZET
# ============================================

@app.route("/haftalik-ozet")
def haftalik_ozet():
    """Öğrencinin son 7 günlük özeti."""
    if session.get("rol") != "ogrenci":
        return redirect(url_for("ana_sayfa"))

    from datetime import date, timedelta

    ogrenci_id = session["kullanici_id"]
    bugun = date.today()

    # Türkçe gün isimleri (0=Pazartesi, 6=Pazar)
    TURKCE_GUNLER = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]
    TURKCE_GUNLER_UZUN = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

    # Son 7 günün listesi (eskiden yeniye)
    gunler = []
    for i in range(6, -1, -1):
        gun = bugun - timedelta(days=i)
        gun_index = gun.weekday()  # 0=Pazartesi, 6=Pazar
        gunler.append({
            "tarih": gun.isoformat(),
            "kisa": TURKCE_GUNLER[gun_index],
            "uzun": TURKCE_GUNLER_UZUN[gun_index],
            "yildiz": 0,
            "oyun": 0,
            "rozet": 0,
        })

    gun_dict = {g["tarih"]: g for g in gunler}

    conn = db.baglan()
    imlec = conn.cursor()

    # Son 7 gündeki oyun kayıtları (günlük kırılım)
    yedi_gun_once = (bugun - timedelta(days=6)).isoformat()
    imlec.execute("""
        SELECT DATE(tarih, 'localtime') as gun,
               COALESCE(SUM(yildiz), 0) as toplam_yildiz,
               COUNT(DISTINCT oyun_no || '-' || ana_bolum || '-' || ara_bolum) as oyun_sayisi
        FROM ilerleme
        WHERE ogrenci_id = ?
          AND tamamlandi = 1
          AND DATE(tarih, 'localtime') >= ?
        GROUP BY DATE(tarih, 'localtime')
    """, (ogrenci_id, yedi_gun_once))

    for r in imlec.fetchall():
        g = r["gun"]
        if g in gun_dict:
            gun_dict[g]["yildiz"] = r["toplam_yildiz"]
            gun_dict[g]["oyun"] = r["oyun_sayisi"]

    # Son 7 gündeki rozetler
    imlec.execute("""
        SELECT DATE(tarih, 'localtime') as gun, COUNT(*) as sayi
        FROM rozetler
        WHERE ogrenci_id = ?
          AND DATE(tarih, 'localtime') >= ?
        GROUP BY DATE(tarih, 'localtime')
    """, (ogrenci_id, yedi_gun_once))

    for r in imlec.fetchall():
        g = r["gun"]
        if g in gun_dict:
            gun_dict[g]["rozet"] = r["sayi"]

    # Toplam haftalık
    toplam_yildiz = sum(g["yildiz"] for g in gunler)
    toplam_oyun = sum(g["oyun"] for g in gunler)
    toplam_rozet = sum(g["rozet"] for g in gunler)

    # Kaç gün oynadı?
    oynanan_gun = sum(1 for g in gunler if g["oyun"] > 0)

    # En iyi gün (en çok yıldız)
    en_iyi_gun = max(gunler, key=lambda x: x["yildiz"]) if toplam_yildiz > 0 else None

    # Grafik için maksimum yıldız değeri
    max_yildiz = max((g["yildiz"] for g in gunler), default=0)
    if max_yildiz == 0:
        max_yildiz = 1  # sıfıra bölünmesin

    # Her gün için yüzde hesapla
    for g in gunler:
        g["yuzde"] = int(g["yildiz"] / max_yildiz * 100)

    # Geçen hafta ile kıyaslama (opsiyonel basit versiyon)
    # (Şimdilik atlıyoruz, istersen ekleriz)

    conn.close()

    return render_template(
        "haftalik_ozet.html",
        gunler=gunler,
        toplam_yildiz=toplam_yildiz,
        toplam_oyun=toplam_oyun,
        toplam_rozet=toplam_rozet,
        oynanan_gun=oynanan_gun,
        en_iyi_gun=en_iyi_gun,
        ad_soyad=session.get("ad_soyad", "Öğrenci"),
    )
# ============================================
# EKİPMAN SİSTEMİ
# ============================================

@app.route("/ekipman-magaza")
def ekipman_magaza():
    """Ekipman mağazası — satın alma ve takma."""
    if session.get("rol") != "ogrenci":
        return redirect(url_for("ana_sayfa"))

    ogrenci_id = session["kullanici_id"]
    conn = db.baglan()
    imlec = conn.cursor()

    # Kullanılabilir yıldız hesapla
    imlec.execute(
        "SELECT COALESCE(SUM(yildiz), 0) as toplam FROM ilerleme WHERE ogrenci_id = ?",
        (ogrenci_id,)
    )
    toplam_yildiz = imlec.fetchone()["toplam"]

    imlec.execute(
        "SELECT COALESCE(harcanan_yildiz, 0) as harcanan FROM kullanicilar WHERE id = ?",
        (ogrenci_id,)
    )
    harcanan = imlec.fetchone()["harcanan"]
    kullanilabilir = toplam_yildiz - harcanan

    # Öğrencinin sahip olduğu ekipmanlar
    imlec.execute(
        "SELECT ekipman_no, takili FROM ogrenci_ekipman WHERE ogrenci_id = ?",
        (ogrenci_id,)
    )
    sahip = {r["ekipman_no"]: r["takili"] for r in imlec.fetchall()}

    conn.close()

    # Kataloğu kategori bazlı hazırla
    kategoriler = []
    for kat in bl.ekipman_kategorileri():
        esyalar = []
        for no, e in bl.EKIPMANLAR.items():
            if e["kategori"] == kat["kod"]:
                esyalar.append({
                    "no": no,
                    "ad": e["ad"],
                    "emoji": e["emoji"],
                    "fiyat": e["fiyat"],
                    "sahip": no in sahip,
                    "takili": sahip.get(no, 0) == 1,
                    "alabilir": kullanilabilir >= e["fiyat"],
                })
        kategoriler.append({"ad": kat["ad"], "kod": kat["kod"], "esyalar": esyalar})

    return render_template(
        "ekipman_magaza.html",
        kategoriler=kategoriler,
        toplam_yildiz=toplam_yildiz,
        harcanan=harcanan,
        kullanilabilir=kullanilabilir,
        ad_soyad=session.get("ad_soyad", "Öğrenci"),
    )


@app.route("/ekipman-ac/<int:ekipman_no>", methods=["POST"])
def ekipman_ac(ekipman_no):
    """Ekipmanı yıldızla aç."""
    if session.get("rol") != "ogrenci":
        return redirect(url_for("ana_sayfa"))

    ekipman = bl.ekipman_getir(ekipman_no)
    if not ekipman:
        return redirect(url_for("ekipman_magaza", hata="Ekipman bulunamadı!"))

    ogrenci_id = session["kullanici_id"]
    conn = db.baglan()
    imlec = conn.cursor()

    # Zaten sahip mi?
    imlec.execute(
        "SELECT id FROM ogrenci_ekipman WHERE ogrenci_id = ? AND ekipman_no = ?",
        (ogrenci_id, ekipman_no)
    )
    if imlec.fetchone():
        conn.close()
        return redirect(url_for("ekipman_magaza", hata="Bu ekipman zaten sende! 😊"))

    # Yeterli yıldız var mı?
    imlec.execute(
        "SELECT COALESCE(SUM(yildiz), 0) as toplam FROM ilerleme WHERE ogrenci_id = ?",
        (ogrenci_id,)
    )
    toplam_yildiz = imlec.fetchone()["toplam"]

    imlec.execute(
        "SELECT COALESCE(harcanan_yildiz, 0) as harcanan FROM kullanicilar WHERE id = ?",
        (ogrenci_id,)
    )
    harcanan = imlec.fetchone()["harcanan"]
    kullanilabilir = toplam_yildiz - harcanan

    if kullanilabilir < ekipman["fiyat"]:
        conn.close()
        eksik = ekipman["fiyat"] - kullanilabilir
        return redirect(url_for("ekipman_magaza", hata=f"Yeterli yıldızın yok! {eksik} ⭐ daha toplaman gerekiyor. 💪"))

    # Satın al
    imlec.execute(
        "INSERT INTO ogrenci_ekipman (ogrenci_id, ekipman_no, takili) VALUES (?, ?, 0)",
        (ogrenci_id, ekipman_no)
    )
    imlec.execute(
        "UPDATE kullanicilar SET harcanan_yildiz = harcanan_yildiz + ? WHERE id = ?",
        (ekipman["fiyat"], ogrenci_id)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("ekipman_magaza", mesaj=f"🌟 {ekipman['emoji']} {ekipman['ad']} açıldı! Artık takabilirsin."))


@app.route("/ekipman-tak/<int:ekipman_no>", methods=["POST"])
def ekipman_tak(ekipman_no):
    """Ekipmanı tak veya çıkar."""
    if session.get("rol") != "ogrenci":
        return redirect(url_for("ana_sayfa"))

    ekipman = bl.ekipman_getir(ekipman_no)
    if not ekipman:
        return redirect(url_for("ekipman_magaza", hata="Ekipman bulunamadı!"))

    ogrenci_id = session["kullanici_id"]
    conn = db.baglan()
    imlec = conn.cursor()

    # Bu ekipman öğrencide var mı?
    imlec.execute(
        "SELECT id, takili FROM ogrenci_ekipman WHERE ogrenci_id = ? AND ekipman_no = ?",
        (ogrenci_id, ekipman_no)
    )
    kayit = imlec.fetchone()
    if not kayit:
        conn.close()
        return redirect(url_for("ekipman_magaza", hata="Bu ekipman sende yok!"))

    yeni_durum = 0 if kayit["takili"] == 1 else 1

    # Aynı kategoride başka bir ekipman takılıysa çıkar
    if yeni_durum == 1:
        # Bu kategorideki diğer takılı ekipmanları bul
        ayni_kategori_nolar = [
            no for no, e in bl.EKIPMANLAR.items()
            if e["kategori"] == ekipman["kategori"] and no != ekipman_no
        ]
        if ayni_kategori_nolar:
            placeholders = ",".join(["?"] * len(ayni_kategori_nolar))
            imlec.execute(
                f"UPDATE ogrenci_ekipman SET takili = 0 WHERE ogrenci_id = ? AND ekipman_no IN ({placeholders})",
                [ogrenci_id] + ayni_kategori_nolar
            )

    imlec.execute(
        "UPDATE ogrenci_ekipman SET takili = ? WHERE id = ?",
        (yeni_durum, kayit["id"])
    )
    conn.commit()
    conn.close()

    if yeni_durum == 1:
        return redirect(url_for("ekipman_magaza", mesaj=f"✨ {ekipman['emoji']} {ekipman['ad']} takıldı! Harika görünüyorsun!"))
    else:
        return redirect(url_for("ekipman_magaza", mesaj=f"📤 {ekipman['emoji']} {ekipman['ad']} çıkarıldı."))
# ============================================
# ÖĞRETMEN PANELİ
# ============================================

@app.route("/ogretmen")
def ogretmen_panel():
    """Öğretmenin sınıf listesi ekranı."""
    if session.get("rol") != "ogretmen":
        return redirect(url_for("ana_sayfa"))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute(
        "SELECT id, kullanici_adi, ad_soyad FROM kullanicilar WHERE rol = 'ogrenci' ORDER BY ad_soyad"
    )
    ogrenciler_ham = imlec.fetchall()

    ogrenciler = []
    for ogr in ogrenciler_ham:
        oid = ogr["id"]

        imlec.execute(
            "SELECT COALESCE(SUM(yildiz), 0) as toplam FROM ilerleme WHERE ogrenci_id = ?",
            (oid,)
        )
        toplam_yildiz = imlec.fetchone()["toplam"]

        imlec.execute(
            "SELECT COUNT(*) as sayi FROM rozetler WHERE ogrenci_id = ?",
            (oid,)
        )
        rozet_sayisi = imlec.fetchone()["sayi"]

        imlec.execute("""
            SELECT ana_bolum, COUNT(DISTINCT ara_bolum) as tamamlanan
            FROM ilerleme
            WHERE ogrenci_id = ? AND tamamlandi = 1
            GROUP BY ana_bolum
        """, (oid,))
        biten = set()
        for s in imlec.fetchall():
            if s["tamamlanan"] >= bl.ARA_BOLUM_SAYISI:
                biten.add(s["ana_bolum"])

        rutbe = "Acemi Kâşif"
        for r in bl.RUTBELER:
            if all(bn in biten for bn in r["bolumler"]):
                rutbe = f"{r['sembol']} {r['ad']}"

        imlec.execute("""
            SELECT ana_bolum, ara_bolum FROM ilerleme
            WHERE ogrenci_id = ?
            ORDER BY tarih DESC LIMIT 1
        """, (oid,))
        son = imlec.fetchone()
        if son:
            konum = f"Bölüm {son['ana_bolum']} / Ara {son['ara_bolum']}"
        else:
            konum = "Henüz başlamadı"

        ogrenciler.append({
            "id": oid,
            "kullanici_adi": ogr["kullanici_adi"],
            "ad_soyad": ogr["ad_soyad"],
            "toplam_yildiz": toplam_yildiz,
            "rozet_sayisi": rozet_sayisi,
            "biten_bolum_sayisi": len(biten),
            "rutbe": rutbe,
            "konum": konum,
        })

    conn.close()

    return render_template(
        "ogretmen_panel.html",
        ogrenciler=ogrenciler,
        ogretmen_adi=session.get("ad_soyad", "Öğretmen"),
    )


@app.route("/ogretmen/ogrenci/<int:ogrenci_id>")
def ogrenci_detay(ogrenci_id):
    """Bir öğrencinin detaylı ilerleme raporu."""
    if session.get("rol") != "ogretmen":
        return redirect(url_for("ana_sayfa"))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute(
        "SELECT id, kullanici_adi, ad_soyad FROM kullanicilar WHERE id = ? AND rol = 'ogrenci'",
        (ogrenci_id,)
    )
    ogrenci = imlec.fetchone()
    if not ogrenci:
        conn.close()
        return "Öğrenci bulunamadı", 404

    imlec.execute("""
        SELECT ana_bolum,
               COUNT(DISTINCT ara_bolum) as tamamlanan,
               COALESCE(SUM(yildiz), 0) as toplam_yildiz
        FROM ilerleme
        WHERE ogrenci_id = ? AND tamamlandi = 1
        GROUP BY ana_bolum
    """, (ogrenci_id,))
    bolum_verisi = {}
    for s in imlec.fetchall():
        bolum_verisi[s["ana_bolum"]] = {
            "tamamlanan": s["tamamlanan"],
            "toplam_yildiz": s["toplam_yildiz"],
        }

    bolum_listesi = []
    biten_bolumler = set()
    for b in bl.ANA_BOLUMLER:
        no = b["no"]
        v = bolum_verisi.get(no, {"tamamlanan": 0, "toplam_yildiz": 0})
        bitti = v["tamamlanan"] >= bl.ARA_BOLUM_SAYISI
        if bitti:
            biten_bolumler.add(no)

        yuzde = int(v["tamamlanan"] / bl.ARA_BOLUM_SAYISI * 100)

        bolum_listesi.append({
            **b,
            "tamamlanan": v["tamamlanan"],
            "toplam_yildiz": v["toplam_yildiz"],
            "yuzde": yuzde,
            "bitti": bitti,
        })

    rutbe = "Acemi Kâşif"
    for r in bl.RUTBELER:
        if all(bn in biten_bolumler for bn in r["bolumler"]):
            rutbe = f"{r['sembol']} {r['ad']}"

    imlec.execute(
        "SELECT COALESCE(SUM(yildiz), 0) as toplam FROM ilerleme WHERE ogrenci_id = ?",
        (ogrenci_id,)
    )
    toplam_yildiz = imlec.fetchone()["toplam"]

    imlec.execute(
        "SELECT rozet_adi, tarih FROM rozetler WHERE ogrenci_id = ? ORDER BY tarih",
        (ogrenci_id,)
    )
    rozetler = [{"ad": r["rozet_adi"], "tarih": r["tarih"]} for r in imlec.fetchall()]

    imlec.execute(
        "SELECT COUNT(*) as sayi FROM ilerleme WHERE ogrenci_id = ? AND tamamlandi = 1",
        (ogrenci_id,)
    )
    oynanan_oyun = imlec.fetchone()["sayi"]

    conn.close()

    return render_template(
        "ogrenci_detay.html",
        ogrenci=ogrenci,
        bolumler=bolum_listesi,
        rutbe=rutbe,
        toplam_yildiz=toplam_yildiz,
        rozetler=rozetler,
        oynanan_oyun=oynanan_oyun,
    )


# ============================================
# ADMIN PANELİ
# ============================================

@app.route("/admin")
def admin_panel():
    """Admin ana paneli."""
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("""
        SELECT id, kullanici_adi, ad_soyad, rol, olusturma_tarihi
        FROM kullanicilar
        ORDER BY
            CASE rol
                WHEN 'admin' THEN 1
                WHEN 'ogretmen' THEN 2
                ELSE 3
            END,
            ad_soyad
    """)
    kullanicilar = [dict(r) for r in imlec.fetchall()]

    imlec.execute("SELECT COUNT(*) as s FROM kullanicilar WHERE rol = 'ogrenci'")
    ogrenci_sayi = imlec.fetchone()["s"]

    imlec.execute("SELECT COUNT(*) as s FROM kullanicilar WHERE rol = 'ogretmen'")
    ogretmen_sayi = imlec.fetchone()["s"]

    imlec.execute("SELECT COUNT(*) as s FROM ilerleme WHERE tamamlandi = 1")
    toplam_oyun = imlec.fetchone()["s"]

    imlec.execute("SELECT COUNT(*) as s FROM rozetler")
    toplam_rozet = imlec.fetchone()["s"]

    imlec.execute("""
        SELECT ana_bolum, ara_bolum, COUNT(*) as sayi
        FROM oyun_atamalari
        GROUP BY ana_bolum, ara_bolum
    """)
    atama_sayilari = {}
    for r in imlec.fetchall():
        ana = r["ana_bolum"]
        ara = r["ara_bolum"]
        if ana not in atama_sayilari:
            atama_sayilari[ana] = {}
        atama_sayilari[ana][ara] = r["sayi"]

    conn.close()

    return render_template(
        "admin_panel.html",
        kullanicilar=kullanicilar,
        ogrenci_sayi=ogrenci_sayi,
        ogretmen_sayi=ogretmen_sayi,
        toplam_oyun=toplam_oyun,
        toplam_rozet=toplam_rozet,
        admin_adi=session.get("ad_soyad", "Admin"),
        oyunlar=bl.OYUNLAR,
        bolumler=bl.ANA_BOLUMLER,
        ara_sayisi=bl.ARA_BOLUM_SAYISI,
        atama_sayilari=atama_sayilari,
        aktif_sayfa="panel",
    )


@app.route("/admin/kullanici-ekle", methods=["POST"])
def admin_kullanici_ekle():
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    kullanici_adi = request.form.get("kullanici_adi", "").strip().lower()
    sifre = request.form.get("sifre", "").strip()
    rol = request.form.get("rol", "ogrenci")
    ad_soyad = request.form.get("ad_soyad", "").strip()

    hata = None
    if not kullanici_adi or len(kullanici_adi) < 3:
        hata = "Kullanıcı adı en az 3 karakter olmalı!"
    elif not sifre or len(sifre) < 3:
        hata = "Şifre en az 3 karakter olmalı!"
    elif rol not in ("ogrenci", "ogretmen"):
        hata = "Geçersiz rol!"
    elif not ad_soyad:
        hata = "Ad soyad boş olamaz!"

    if hata:
        return redirect(url_for("admin_panel", hata=hata))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("SELECT id FROM kullanicilar WHERE kullanici_adi = ?", (kullanici_adi,))
    if imlec.fetchone():
        conn.close()
        return redirect(url_for("admin_panel", hata="Bu kullanıcı adı zaten var!"))

    try:
        imlec.execute(
            "INSERT INTO kullanicilar (kullanici_adi, sifre, rol, ad_soyad) VALUES (?, ?, ?, ?)",
            (kullanici_adi, sifre, rol, ad_soyad)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("admin_panel", mesaj=f"✅ {ad_soyad} ({rol}) eklendi!"))
    except Exception as e:
        conn.close()
        return redirect(url_for("admin_panel", hata=f"Hata: {str(e)}"))


@app.route("/admin/kullanici-sil/<int:kullanici_id>", methods=["POST"])
def admin_kullanici_sil(kullanici_id):
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    if kullanici_id == session.get("kullanici_id"):
        return redirect(url_for("admin_panel", hata="Kendi hesabını silemezsin!"))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("SELECT kullanici_adi, rol FROM kullanicilar WHERE id = ?", (kullanici_id,))
    k = imlec.fetchone()
    if not k:
        conn.close()
        return redirect(url_for("admin_panel", hata="Kullanıcı bulunamadı!"))

    if k["rol"] == "admin":
        conn.close()
        return redirect(url_for("admin_panel", hata="Admin hesabı silinemez!"))

    imlec.execute("DELETE FROM ilerleme WHERE ogrenci_id = ?", (kullanici_id,))
    imlec.execute("DELETE FROM rozetler WHERE ogrenci_id = ?", (kullanici_id,))
    imlec.execute("DELETE FROM kullanicilar WHERE id = ?", (kullanici_id,))

    conn.commit()
    conn.close()

    return redirect(url_for("admin_panel", mesaj=f"🗑️ {k['kullanici_adi']} silindi!"))


@app.route("/admin/sifre-sifirla/<int:kullanici_id>", methods=["POST"])
def admin_sifre_sifirla(kullanici_id):
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute("SELECT kullanici_adi FROM kullanicilar WHERE id = ?", (kullanici_id,))
    k = imlec.fetchone()
    if not k:
        conn.close()
        return redirect(url_for("admin_panel", hata="Kullanıcı bulunamadı!"))

    imlec.execute(
        "UPDATE kullanicilar SET sifre = '1234' WHERE id = ?",
        (kullanici_id,)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("admin_panel", mesaj=f"🔑 {k['kullanici_adi']} şifresi '1234' olarak sıfırlandı!"))


# ============================================
# ADMIN — OYUN ATAMA
# ============================================

@app.route("/admin/oyun-atama/<int:ana>/<int:ara>")
def admin_oyun_atama(ana, ara):
    """Belirli bir ara bölümün atamalarını yönet."""
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    bolum = bl.ana_bolum_getir(ana)
    if not bolum:
        return "Bölüm bulunamadı", 404

    atamalar = atama_listesi_getir(ana, ara)

    for a in atamalar:
        o = bl.oyun_getir(a["oyun_no"])
        if o:
            a["oyun_ad"] = o["ad"]
            a["oyun_emoji"] = o["emoji"]
        else:
            a["oyun_ad"] = "Bilinmeyen oyun"
            a["oyun_emoji"] = "❓"
        a["ozel_icerik_var"] = bool(a.get("ozel_veri"))

    return render_template(
        "admin_oyun_atama.html",
        bolum=bolum,
        ana=ana,
        ara=ara,
        atamalar=atamalar,
        oyunlar=bl.OYUNLAR,
    )


@app.route("/admin/oyun-ata", methods=["POST"])
def admin_oyun_ata():
    """Yeni oyun ataması ekle."""
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    ana = int(request.form.get("ana", 0))
    ara = int(request.form.get("ara", 0))
    oyun_no = int(request.form.get("oyun_no", 0))

    if not (ana and ara and oyun_no):
        return redirect(url_for("admin_oyun_atama", ana=ana, ara=ara))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute(
        "SELECT COALESCE(MAX(sira), 0) as son FROM oyun_atamalari WHERE ana_bolum = ? AND ara_bolum = ?",
        (ana, ara)
    )
    yeni_sira = imlec.fetchone()["son"] + 1

    try:
        imlec.execute(
            "INSERT INTO oyun_atamalari (ana_bolum, ara_bolum, sira, oyun_no) VALUES (?, ?, ?, ?)",
            (ana, ara, yeni_sira, oyun_no)
        )
        conn.commit()
        mesaj = f"✅ Oyun eklendi (sıra {yeni_sira})"
    except Exception as e:
        mesaj = f"⚠️ Hata: {str(e)}"

    conn.close()
    return redirect(url_for("admin_oyun_atama", ana=ana, ara=ara, mesaj=mesaj))


@app.route("/admin/oyun-atama-sil/<int:atama_id>", methods=["POST"])
def admin_oyun_atama_sil(atama_id):
    """Bir atamayı sil."""
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute(
        "SELECT ana_bolum, ara_bolum FROM oyun_atamalari WHERE id = ?",
        (atama_id,)
    )
    atama = imlec.fetchone()
    if not atama:
        conn.close()
        return redirect(url_for("admin_panel"))

    ana = atama["ana_bolum"]
    ara = atama["ara_bolum"]

    imlec.execute("DELETE FROM oyun_atamalari WHERE id = ?", (atama_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("admin_oyun_atama", ana=ana, ara=ara, mesaj="🗑️ Atama silindi"))


@app.route("/admin/oyun-atama-tasi/<int:atama_id>/<yon>", methods=["POST"])
def admin_oyun_atama_tasi(atama_id, yon):
    """Atamayı yukarı/aşağı taşı."""
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute(
        "SELECT id, ana_bolum, ara_bolum, sira FROM oyun_atamalari WHERE id = ?",
        (atama_id,)
    )
    atama = imlec.fetchone()
    if not atama:
        conn.close()
        return redirect(url_for("admin_panel"))

    ana = atama["ana_bolum"]
    ara = atama["ara_bolum"]
    eski_sira = atama["sira"]

    if yon == "yukari":
        yeni_sira = eski_sira - 1
    else:
        yeni_sira = eski_sira + 1

    imlec.execute(
        "SELECT id, sira FROM oyun_atamalari WHERE ana_bolum = ? AND ara_bolum = ? AND sira = ?",
        (ana, ara, yeni_sira)
    )
    diger = imlec.fetchone()

    if diger:
        imlec.execute(
            "UPDATE oyun_atamalari SET sira = -1 WHERE id = ?", (atama_id,)
        )
        imlec.execute(
            "UPDATE oyun_atamalari SET sira = ? WHERE id = ?",
            (eski_sira, diger["id"])
        )
        imlec.execute(
            "UPDATE oyun_atamalari SET sira = ? WHERE id = ?",
            (yeni_sira, atama_id)
        )

    conn.commit()
    conn.close()

    return redirect(url_for("admin_oyun_atama", ana=ana, ara=ara))


@app.route("/admin/oyun-icerik/<int:atama_id>")
def admin_oyun_icerik(atama_id):
    """Oyun içeriği düzenleme sayfası."""
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    conn = db.baglan()
    imlec = conn.cursor()
    imlec.execute("""
        SELECT id, ana_bolum, ara_bolum, sira, oyun_no, ozel_veri
        FROM oyun_atamalari WHERE id = ?
    """, (atama_id,))
    atama_ham = imlec.fetchone()
    conn.close()

    if not atama_ham:
        return "Atama bulunamadı", 404

    atama = dict(atama_ham)
    oyun = bl.oyun_getir(atama["oyun_no"])
    bolum = bl.ana_bolum_getir(atama["ana_bolum"])

    ornek_sorular = ov.oyun_sorularini_getir(atama["oyun_no"])[:2]
    ornek_json = json.dumps(ornek_sorular, ensure_ascii=False, indent=2)

    return render_template(
        "admin_oyun_icerik.html",
        atama=atama,
        oyun=oyun,
        bolum=bolum,
        ornek_json=ornek_json,
    )


@app.route("/admin/oyun-icerik-kaydet/<int:atama_id>", methods=["POST"])
def admin_oyun_icerik_kaydet(atama_id):
    """Özel soru verisini kaydet."""
    if session.get("rol") != "admin":
        return redirect(url_for("ana_sayfa"))

    ozel_veri = request.form.get("ozel_veri", "").strip()

    conn = db.baglan()
    imlec = conn.cursor()

    imlec.execute(
        "SELECT ana_bolum, ara_bolum FROM oyun_atamalari WHERE id = ?",
        (atama_id,)
    )
    atama = imlec.fetchone()
    if not atama:
        conn.close()
        return redirect(url_for("admin_panel"))

    if not ozel_veri:
        yeni_veri = None
        mesaj = "🗑️ Özel içerik kaldırıldı, varsayılan kullanılacak"
    else:
        try:
            parsed = json.loads(ozel_veri)
            if not isinstance(parsed, list) or len(parsed) == 0:
                raise ValueError("Liste boş veya geçersiz")
            yeni_veri = json.dumps(parsed, ensure_ascii=False)
            mesaj = f"✅ {len(parsed)} özel soru kaydedildi!"
        except Exception as e:
            conn.close()
            return redirect(
                url_for("admin_oyun_icerik", atama_id=atama_id, hata=f"⚠️ Geçersiz JSON: {str(e)}")
            )

    imlec.execute(
        "UPDATE oyun_atamalari SET ozel_veri = ? WHERE id = ?",
        (yeni_veri, atama_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("admin_oyun_icerik", atama_id=atama_id, mesaj=mesaj))


# ============================================
# UYGULAMAYI BAŞLAT
# ============================================

if __name__ == "__main__":
    app.run(debug=True)
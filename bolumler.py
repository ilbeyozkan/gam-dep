# 8 Ana Bölüm ve özellikleri
ANA_BOLUMLER = [
    {"no": 1, "ad": "Başlangıç Limanı", "emoji": "⚓",  "renk": "#3498db", "rozet": "Başlangıç Kâşifi", "resim": "liman.svg"},
    {"no": 2, "ad": "Hece Ormanı",      "emoji": "🌲",  "renk": "#27ae60", "rozet": "Hece Ustası",       "resim": "orman.svg"},
    {"no": 3, "ad": "Kelime Dağı",      "emoji": "🏔️", "renk": "#e67e22", "rozet": "Kelime Kahramanı", "resim": "dag.svg"},
    {"no": 4, "ad": "Anlam Gölü",       "emoji": "🏞️", "renk": "#9b59b6", "rozet": "Anlam Avcısı",     "resim": "gol.svg"},
    {"no": 5, "ad": "Zafer Kalesi",     "emoji": "🏰",  "renk": "#d4af37", "rozet": "Baş Kâşif",         "resim": "kale.svg"},
]

# Her ana bölümde 6 ara bölüm var
ARA_BOLUM_SAYISI = 6


def ana_bolum_getir(no):
    """Numarası verilen ana bölümü döndür."""
    for b in ANA_BOLUMLER:
        if b["no"] == no:
            return b
    return None


# Rütbeler (ileride kullanacağız)
RUTBELER = [
    {"ad": "Çırak Kâşif",       "sembol": "🧭", "bolumler": [1, 2]},
    {"ad": "Yol Arkadaşı Kâşif","sembol": "🗺️", "bolumler": [1, 2, 3, 4]},
    {"ad": "Baş Kâşif",         "sembol": "👑", "bolumler": [1, 2, 3, 4, 5]},
]
# ============================================
# 17 DİJİTAL OYUN
# ============================================
OYUNLAR = {
    1:  {"ad": "Sözcük Sayma",       "emoji": "🔢", "aciklama": "Cümlede kaç sözcük var?"},
    2:  {"ad": "Sözcük Atma",        "emoji": "✂️", "aciklama": "Bir sözcük çıkar, kalanı söyle"},
    3:  {"ad": "Sözcük Birleştirme", "emoji": "🧩", "aciklama": "Sözcükleri birleştir, cümle kur"},
    4:  {"ad": "Sözcük Ayırma",      "emoji": "🔍", "aciklama": "Cümledeki sözcükleri ayır"},
    5:  {"ad": "Kafiye Ayırt Etme",  "emoji": "🎵", "aciklama": "Kafiyeli sözcükleri bul"},
    6:  {"ad": "Kafiye Üretme",      "emoji": "🎤", "aciklama": "Kafiyeli yeni sözcük üret"},
    7:  {"ad": "Hece Bölme",         "emoji": "🪓", "aciklama": "Sözcüğü hecelere ayır"},
    8:  {"ad": "Hece Silme",         "emoji": "🗑️", "aciklama": "Bir hece çıkar, kalanı söyle"},
    9:  {"ad": "Fonem Ayırt Etme",   "emoji": "👂", "aciklama": "Aynı/farklı sesleri ayırt et"},
    10: {"ad": "Baştaki Fonemi Bul", "emoji": "⬅️", "aciklama": "İlk sesi bul"},
    11: {"ad": "Sondaki Fonemi Bul", "emoji": "➡️", "aciklama": "Son sesi bul"},
    12: {"ad": "Fonem Birleştirme",  "emoji": "🔗", "aciklama": "Sesleri birleştir, sözcük yap"},
    13: {"ad": "Fonem Bölme",        "emoji": "✂️", "aciklama": "Sözcüğü seslere böl"},
    14: {"ad": "Fonem Silme",        "emoji": "🗑️", "aciklama": "Bir ses çıkar, kalanı söyle"},
    15: {"ad": "Fonem Ekleme",       "emoji": "➕", "aciklama": "Yeni ses ekle"},
    16: {"ad": "Fonem Değiştirme",   "emoji": "🔄", "aciklama": "Bir sesi değiştir, yeni sözcük yap"},
    17: {"ad": "Otomatik Okuma",     "emoji": "⚡", "aciklama": "Hızlı okuma (flash kartlar)"},
}


# ============================================
# VARSAYILAN YERLEŞİM
# Her ana bölüm (1-8) → 6 ara bölüm → oyun numaraları
# Admin panelinden bu yerleşim değiştirilebilir
# ============================================
VARSAYILAN_YERLESIM = {
    # Bölüm 1: Başlangıç Limanı - Sözcük temelli
    1: {
        1: [1],           # Sözcük Sayma
        2: [2],           # Sözcük Atma
        3: [3],           # Sözcük Birleştirme
        4: [4],           # Sözcük Ayırma
        5: [1, 2],        # Karışık
        6: [3, 4],        # Karışık
    },
    # Bölüm 2: Hece Ormanı - Hece
    2: {
        1: [7],           # Hece Bölme
        2: [8],           # Hece Silme
        3: [7, 8],        # Karışık
        4: [7],           # Hece Bölme
        5: [8],           # Hece Silme
        6: [7, 8],        # Karışık
    },
    # Bölüm 3: Kelime Dağı - Fonem (en yoğun bölüm)
    3: {
        1: [9],           # Fonem Ayırt Etme
        2: [10, 11],      # Baştaki/Sondaki Fonem
        3: [12, 13],      # Fonem Birleştirme/Bölme
        4: [14],          # Fonem Silme
        5: [15, 16],      # Fonem Ekleme/Değiştirme
        6: [9, 10, 11, 12, 13, 14, 15, 16],  # Hepsi karışık
    },
    # Bölüm 4: Anlam Gölü - Kafiye
    4: {
        1: [5],           # Kafiye Ayırt Etme
        2: [6],           # Kafiye Üretme
        3: [5, 6],        # Karışık
        4: [1, 2],        # Sözcük (tekrar)
        5: [3, 4],        # Sözcük (tekrar)
        6: [5, 6],        # Kafiye karışık
    },
    # Bölüm 5: Zafer Kalesi - Final
    5: {
        1: [17],          # Otomatik Okuma
        2: [17],          # Otomatik Okuma (tekrar)
        3: [12, 13],      # Fonem
        4: [16],          # Fonem Değiştirme
        5: [17],          # Otomatik Okuma
        6: [1, 2, 3, 4, 5, 6],  # Büyük final: karışık
    },
}


def oyun_getir(oyun_no):
    """Oyun numarasına göre oyun bilgisini döndür ('no' dahil)."""
    oyun = OYUNLAR.get(oyun_no)
    if oyun:
        return {**oyun, "no": oyun_no}
    return None


def ara_bolum_oyunlari(ana_no, ara_no):
    """Belirli bir ara bölümdeki oyunların listesini döndür."""
    yerlesim = VARSAYILAN_YERLESIM.get(ana_no, {})
    oyun_nolar = yerlesim.get(ara_no, [])
    return [{"no": n, **OYUNLAR[n]} for n in oyun_nolar if n in OYUNLAR]
def bos_yerlesim():
    """Yeni sistemde başlangıçta tüm bölümler boş."""
    yerlesim = {}
    for ana in range(1, 6):  # 5 bölüm
        yerlesim[ana] = {}
        for ara in range(1, 7):  # 6 ara bölüm
            yerlesim[ana][ara] = []
    return yerlesim
# ============================================
# ROZET İKONLARI
# Her rozet adına karşılık bir emoji
# ============================================
ROZET_IKONLARI = {
    "Başlangıç Kâşifi":  "⚓",
    "Hece Ustası":       "🌲",
    "Kelime Kahramanı":  "🏔️",
    "Anlam Avcısı":      "🏞️",
    "Baş Kâşif":         "🏆",
}
# ============================================
# EKİPMAN KATALOĞU
# ============================================
# Kategoriler:
#   sapka  → avatarın üstünde
#   gozluk → göz hizasında
#   el     → sağ elde
#   boyun  → boyun hizasında
#   sirt   → arkada (pelerin/kanat)
# ============================================

EKIPMANLAR = {
    # 🎩 ŞAPKALAR
    1:  {"ad": "Kasket",            "emoji": "🧢",  "kategori": "sapka", "fiyat": 10},
    2:  {"ad": "Büyücü Şapkası",    "emoji": "🎩",  "kategori": "sapka", "fiyat": 30},
    3:  {"ad": "Kral Tacı",         "emoji": "👑",  "kategori": "sapka", "fiyat": 100},
    4:  {"ad": "Mezuniyet Şapkası", "emoji": "🎓",  "kategori": "sapka", "fiyat": 40},

    # 👓 GÖZLÜKLER
    5:  {"ad": "Güneş Gözlüğü",     "emoji": "🕶️", "kategori": "gozluk", "fiyat": 15},
    6:  {"ad": "Normal Gözlük",     "emoji": "👓",  "kategori": "gozluk", "fiyat": 20},

    # ⚔️ EL (sağ el)
    7:  {"ad": "Kılıç",             "emoji": "⚔️", "kategori": "el",    "fiyat": 40},
    8:  {"ad": "Sihirli Asa",       "emoji": "🪄",  "kategori": "el",    "fiyat": 50},
    9:  {"ad": "Kitap",             "emoji": "📚",  "kategori": "el",    "fiyat": 25},
    10: {"ad": "Kalem",             "emoji": "✏️", "kategori": "el",    "fiyat": 8},

    # 🎀 BOYUN
    11: {"ad": "Kravat",            "emoji": "👔",  "kategori": "boyun", "fiyat": 15},
    12: {"ad": "Kolye",             "emoji": "📿",  "kategori": "boyun", "fiyat": 35},

    # 🦸 SIRT
    13: {"ad": "Süper Kahraman Pelerini", "emoji": "🦸",  "kategori": "sirt", "fiyat": 80},
    14: {"ad": "Melek Kanatları",         "emoji": "👼",  "kategori": "sirt", "fiyat": 150},
}


def ekipman_getir(ekipman_no):
    """Ekipman numarasına göre bilgi döndür."""
    e = EKIPMANLAR.get(ekipman_no)
    if e:
        return {**e, "no": ekipman_no}
    return None


def ekipman_kategorileri():
    """Kategorileri listele (görüntüleme sırasına göre)."""
    return [
        {"kod": "sapka",  "ad": "🎩 Şapkalar"},
        {"kod": "gozluk", "ad": "👓 Gözlükler"},
        {"kod": "el",     "ad": "⚔️ Elde Taşınan"},
        {"kod": "boyun",  "ad": "🎀 Boyun Aksesuarları"},
        {"kod": "sirt",   "ad": "🦸 Sırt Ekipmanları"},
    ]
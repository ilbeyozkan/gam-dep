# ============================================
# ANA BÖLÜMLER
# ============================================
ANA_BOLUMLER = [
    {"no": 1, "ad": "Başlangıç Limanı", "emoji": "⚓",  "renk": "#3498db", "rozet": "Başlangıç Kâşifi", "resim": "liman.svg"},
    {"no": 2, "ad": "Hece Ormanı",      "emoji": "🌲",  "renk": "#27ae60", "rozet": "Hece Ustası",       "resim": "orman.svg"},
    {"no": 3, "ad": "Kelime Dağı",      "emoji": "🏔️", "renk": "#e67e22", "rozet": "Kelime Kahramanı", "resim": "dag.svg"},
    {"no": 4, "ad": "Anlam Gölü",       "emoji": "🏞️", "renk": "#9b59b6", "rozet": "Anlam Avcısı",     "resim": "gol.svg"},
    {"no": 5, "ad": "Zafer Kalesi",     "emoji": "🏰",  "renk": "#d4af37", "rozet": "Baş Kâşif",         "resim": "kale.svg"},
]


def ana_bolum_getir(no):
    """Numarası verilen ana bölümü döndür."""
    for b in ANA_BOLUMLER:
        if b["no"] == no:
            return b
    return None


# ============================================
# RÜTBELER
# ============================================
RUTBELER = [
    {"ad": "Çırak Kâşif",        "sembol": "🧭", "bolumler": [1, 2]},
    {"ad": "Yol Arkadaşı Kâşif", "sembol": "🗺️", "bolumler": [1, 2, 3, 4]},
    {"ad": "Baş Kâşif",          "sembol": "👑", "bolumler": [1, 2, 3, 4, 5]},
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


def oyun_getir(oyun_no):
    """Oyun numarasına göre oyun bilgisini döndür ('no' dahil)."""
    oyun = OYUNLAR.get(oyun_no)
    if oyun:
        return {**oyun, "no": oyun_no}
    return None


# ============================================
# ROZET İKONLARI
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
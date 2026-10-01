# ============================================
# OYUN 1: SÖZCÜK SAYMA
# Bir cümlede kaç sözcük olduğunu belirleme
# ============================================

SOZCUK_SAYMA = [
    {"cumle": "Ali okula gitti.",           "cevap": 3},
    {"cumle": "Ben bugün çok mutluyum.",    "cevap": 4},
    {"cumle": "Kedi süt içiyor.",            "cevap": 3},
    {"cumle": "Annem bize pasta yaptı.",     "cevap": 4},
    {"cumle": "Bugün hava çok güzel.",       "cevap": 4},
    {"cumle": "Kuşlar gökyüzünde uçuyor.",   "cevap": 3},
    {"cumle": "Ben ve arkadaşım parkta oynadık.", "cevap": 5},
    {"cumle": "Öğretmen bize kitap okudu.",  "cevap": 4},
    {"cumle": "Küçük kız şarkı söyledi.",    "cevap": 4},
    {"cumle": "Dedem bahçede çiçek suladı.", "cevap": 4},
    {"cumle": "Yağmur yağıyor.",             "cevap": 2},
    {"cumle": "Ablam bana hediye aldı.",     "cevap": 4},
    {"cumle": "Biz her sabah koşu yaparız.", "cevap": 5},
    {"cumle": "Balık suda yüzüyor.",         "cevap": 3},
    {"cumle": "Sen ve ben iyi arkadaşız.",   "cevap": 5},
]
# ============================================
# OYUN 7: HECE BÖLME
# Sözcükleri hecelerine ayırabilme
# ============================================

HECE_BOLME = [
    # 1 heceli
    {"sozcuk": "kar",     "heceler": ["kar"],                "cevap": 1},
    {"sozcuk": "gül",     "heceler": ["gül"],                "cevap": 1},
    {"sozcuk": "su",      "heceler": ["su"],                 "cevap": 1},
    {"sozcuk": "göz",     "heceler": ["göz"],                "cevap": 1},

    # 2 heceli
    {"sozcuk": "kalem",   "heceler": ["ka", "lem"],          "cevap": 2},
    {"sozcuk": "kitap",   "heceler": ["ki", "tap"],          "cevap": 2},
    {"sozcuk": "okul",    "heceler": ["o", "kul"],           "cevap": 2},
    {"sozcuk": "çiçek",   "heceler": ["çi", "çek"],          "cevap": 2},
    {"sozcuk": "deniz",   "heceler": ["de", "niz"],          "cevap": 2},
    {"sozcuk": "bahçe",   "heceler": ["bah", "çe"],          "cevap": 2},
    {"sozcuk": "yıldız",  "heceler": ["yıl", "dız"],         "cevap": 2},
    {"sozcuk": "bulut",   "heceler": ["bu", "lut"],          "cevap": 2},
    {"sozcuk": "karpuz",  "heceler": ["kar", "puz"],         "cevap": 2},
    {"sozcuk": "masal",   "heceler": ["ma", "sal"],          "cevap": 2},

    # 3 heceli
    {"sozcuk": "kelebek", "heceler": ["ke", "le", "bek"],    "cevap": 3},
    {"sozcuk": "araba",   "heceler": ["a", "ra", "ba"],      "cevap": 3},
    {"sozcuk": "merhaba", "heceler": ["mer", "ha", "ba"],    "cevap": 3},
    {"sozcuk": "uçurtma", "heceler": ["u", "çurt", "ma"],    "cevap": 3},
    {"sozcuk": "arkadaş", "heceler": ["ar", "ka", "daş"],    "cevap": 3},
    {"sozcuk": "öğretmen","heceler": ["öğ", "ret", "men"],   "cevap": 3},
    {"sozcuk": "pencere", "heceler": ["pen", "ce", "re"],    "cevap": 3},

    # 4 heceli
    {"sozcuk": "bilgisayar", "heceler": ["bil", "gi", "sa", "yar"], "cevap": 4},
    {"sozcuk": "kaplumbağa", "heceler": ["kap", "lum", "ba", "ğa"], "cevap": 4},
    {"sozcuk": "öğretmence", "heceler": ["öğ", "ret", "men", "ce"], "cevap": 4},
]
# ============================================
# OYUN 10: BAŞTAKİ FONEMİ BUL
# Sözcüğün ilk sesini (fonemini) bulabilme
# ============================================

BASTAKI_FONEM = [
    {"sozcuk": "Kedi",     "ilk_ses": "K", "secenekler": ["K", "E", "D", "İ"]},
    {"sozcuk": "Balık",    "ilk_ses": "B", "secenekler": ["B", "A", "L", "K"]},
    {"sozcuk": "Kalem",    "ilk_ses": "K", "secenekler": ["K", "A", "L", "M"]},
    {"sozcuk": "Deniz",    "ilk_ses": "D", "secenekler": ["D", "E", "N", "Z"]},
    {"sozcuk": "Okul",     "ilk_ses": "O", "secenekler": ["O", "K", "U", "L"]},
    {"sozcuk": "Elma",     "ilk_ses": "E", "secenekler": ["E", "L", "M", "A"]},
    {"sozcuk": "Su",       "ilk_ses": "S", "secenekler": ["S", "U", "A", "E"]},
    {"sozcuk": "Gül",      "ilk_ses": "G", "secenekler": ["G", "Ü", "L", "E"]},
    {"sozcuk": "Ağaç",     "ilk_ses": "A", "secenekler": ["A", "Ğ", "Ç", "E"]},
    {"sozcuk": "Top",      "ilk_ses": "T", "secenekler": ["T", "O", "P", "K"]},
    {"sozcuk": "Yıldız",   "ilk_ses": "Y", "secenekler": ["Y", "I", "L", "D"]},
    {"sozcuk": "Zil",      "ilk_ses": "Z", "secenekler": ["Z", "İ", "L", "S"]},
    {"sozcuk": "Masa",     "ilk_ses": "M", "secenekler": ["M", "A", "S", "E"]},
    {"sozcuk": "Çiçek",    "ilk_ses": "Ç", "secenekler": ["Ç", "İ", "C", "K"]},
    {"sozcuk": "Pencere",  "ilk_ses": "P", "secenekler": ["P", "E", "N", "C"]},
    {"sozcuk": "Rüzgar",   "ilk_ses": "R", "secenekler": ["R", "Ü", "Z", "G"]},
    {"sozcuk": "Fındık",   "ilk_ses": "F", "secenekler": ["F", "I", "N", "D"]},
    {"sozcuk": "Vazo",     "ilk_ses": "V", "secenekler": ["V", "A", "Z", "O"]},
]
# ============================================
# OYUN 11: SONDAKİ FONEMİ BUL
# Sözcüğün son sesini (fonemini) bulabilme
# ============================================

SONDAKI_FONEM = [
    {"sozcuk": "Kedi",     "son_ses": "İ", "secenekler": ["K", "E", "D", "İ"]},
    {"sozcuk": "Balık",    "son_ses": "K", "secenekler": ["B", "A", "L", "K"]},
    {"sozcuk": "Kalem",    "son_ses": "M", "secenekler": ["K", "A", "L", "M"]},
    {"sozcuk": "Deniz",    "son_ses": "Z", "secenekler": ["D", "E", "N", "Z"]},
    {"sozcuk": "Okul",     "son_ses": "L", "secenekler": ["O", "K", "U", "L"]},
    {"sozcuk": "Elma",     "son_ses": "A", "secenekler": ["E", "L", "M", "A"]},
    {"sozcuk": "Su",       "son_ses": "U", "secenekler": ["S", "U", "A", "E"]},
    {"sozcuk": "Gül",      "son_ses": "L", "secenekler": ["G", "Ü", "L", "E"]},
    {"sozcuk": "Ağaç",     "son_ses": "Ç", "secenekler": ["A", "Ğ", "Ç", "E"]},
    {"sozcuk": "Top",      "son_ses": "P", "secenekler": ["T", "O", "P", "K"]},
    {"sozcuk": "Yıldız",   "son_ses": "Z", "secenekler": ["Y", "I", "L", "Z"]},
    {"sozcuk": "Zil",      "son_ses": "L", "secenekler": ["Z", "İ", "L", "S"]},
    {"sozcuk": "Masa",     "son_ses": "A", "secenekler": ["M", "A", "S", "E"]},
    {"sozcuk": "Çiçek",    "son_ses": "K", "secenekler": ["Ç", "İ", "C", "K"]},
    {"sozcuk": "Pencere",  "son_ses": "E", "secenekler": ["P", "E", "N", "C"]},
    {"sozcuk": "Rüzgar",   "son_ses": "R", "secenekler": ["R", "Ü", "Z", "G"]},
    {"sozcuk": "Fındık",   "son_ses": "K", "secenekler": ["F", "I", "N", "K"]},
    {"sozcuk": "Vazo",     "son_ses": "O", "secenekler": ["V", "A", "Z", "O"]},
]
# ============================================
# OYUN 5: KAFİYE AYIRT ETME
# Verilen sözcükle kafiyeli olanı bulma
# ============================================

KAFIYE_AYIRT = [
    {"hedef": "kal",  "secenekler": ["dal", "gül", "göl", "yel"],  "dogru": "dal"},
    {"hedef": "kar",  "secenekler": ["yar", "kel", "kır", "kor"],  "dogru": "yar"},
    {"hedef": "göz",  "secenekler": ["söz", "gaz", "toz", "yaz"],  "dogru": "söz"},
    {"hedef": "ben",  "secenekler": ["sen", "ban", "bin", "bun"],  "dogru": "sen"},
    {"hedef": "ev",   "secenekler": ["sev", "av", "iv", "as"],     "dogru": "sev"},
    {"hedef": "el",   "secenekler": ["gel", "al", "öl", "ül"],     "dogru": "gel"},
    {"hedef": "taş",  "secenekler": ["baş", "tuş", "teş", "tiş"],  "dogru": "baş"},
    {"hedef": "kaş",  "secenekler": ["baş", "kuş", "koş", "keş"],  "dogru": "baş"},
    {"hedef": "tel",  "secenekler": ["sel", "tal", "tül", "top"],  "dogru": "sel"},
    {"hedef": "saç",  "secenekler": ["taç", "suç", "seç", "sıç"],  "dogru": "taç"},
    {"hedef": "kaz",  "secenekler": ["yaz", "kız", "koz", "kuz"],  "dogru": "yaz"},
    {"hedef": "at",   "secenekler": ["tat", "et", "it", "ot"],     "dogru": "tat"},
    {"hedef": "gül",  "secenekler": ["bülbül", "gel", "gol", "sal"], "dogru": "bülbül"},
    {"hedef": "kuş",  "secenekler": ["duş", "kaş", "kiş", "koş"],  "dogru": "duş"},
    {"hedef": "yol",  "secenekler": ["kol", "yel", "yıl", "yul"],  "dogru": "kol"},
]
# ============================================
# OYUN 2: SÖZCÜK ATMA
# Cümleden bir sözcük çıkarıldığında kalan cümleyi bulma
# ============================================

SOZCUK_ATMA = [
    {"cumle": "Ali okula gitti.", "cikarilan": "Ali", "kalan": "okula gitti",
     "secenekler": ["Ali gitti", "okula gitti", "Ali okula", "gitti"]},

    {"cumle": "Kedi süt içiyor.", "cikarilan": "süt", "kalan": "Kedi içiyor",
     "secenekler": ["Kedi içiyor", "süt içiyor", "Kedi süt", "içiyor"]},

    {"cumle": "Annem bize pasta yaptı.", "cikarilan": "pasta", "kalan": "Annem bize yaptı",
     "secenekler": ["bize pasta yaptı", "Annem pasta yaptı", "Annem bize yaptı", "Annem bize pasta"]},

    {"cumle": "Bugün hava çok güzel.", "cikarilan": "çok", "kalan": "Bugün hava güzel",
     "secenekler": ["Bugün hava güzel", "hava çok güzel", "Bugün çok güzel", "Bugün hava çok"]},

    {"cumle": "Kuşlar gökyüzünde uçuyor.", "cikarilan": "gökyüzünde", "kalan": "Kuşlar uçuyor",
     "secenekler": ["Kuşlar uçuyor", "gökyüzünde uçuyor", "Kuşlar gökyüzünde", "uçuyor"]},

    {"cumle": "Ben ve arkadaşım parkta oynadık.", "cikarilan": "parkta", "kalan": "Ben ve arkadaşım oynadık",
     "secenekler": ["Ben ve arkadaşım oynadık", "arkadaşım parkta oynadık", "Ben parkta oynadık", "Ben ve arkadaşım parkta"]},

    {"cumle": "Öğretmen bize kitap okudu.", "cikarilan": "kitap", "kalan": "Öğretmen bize okudu",
     "secenekler": ["bize kitap okudu", "Öğretmen bize okudu", "Öğretmen kitap okudu", "Öğretmen bize kitap"]},

    {"cumle": "Küçük kız şarkı söyledi.", "cikarilan": "küçük", "kalan": "kız şarkı söyledi",
     "secenekler": ["kız şarkı söyledi", "Küçük kız söyledi", "Küçük şarkı söyledi", "Küçük kız şarkı"]},

    {"cumle": "Dedem bahçede çiçek suladı.", "cikarilan": "bahçede", "kalan": "Dedem çiçek suladı",
     "secenekler": ["bahçede çiçek suladı", "Dedem bahçede suladı", "Dedem çiçek suladı", "Dedem bahçede çiçek"]},

    {"cumle": "Ablam bana hediye aldı.", "cikarilan": "hediye", "kalan": "Ablam bana aldı",
     "secenekler": ["Ablam bana aldı", "bana hediye aldı", "Ablam hediye aldı", "Ablam bana hediye"]},

    {"cumle": "Balık suda yüzüyor.", "cikarilan": "suda", "kalan": "Balık yüzüyor",
     "secenekler": ["Balık yüzüyor", "suda yüzüyor", "Balık suda", "yüzüyor"]},

    {"cumle": "Sen ve ben iyi arkadaşız.", "cikarilan": "iyi", "kalan": "Sen ve ben arkadaşız",
     "secenekler": ["ben iyi arkadaşız", "Sen ve ben arkadaşız", "Sen ve iyi arkadaşız", "Sen ve ben iyi"]},
]
# ============================================
# OYUN 3: SÖZCÜK BİRLEŞTİRME
# Karışık sözcüklerden anlamlı cümle kurma
# ============================================

SOZCUK_BIRLESTIRME = [
    {"karisik": ["gitti", "Ali", "okula"],
     "dogru": "Ali okula gitti",
     "secenekler": ["okula Ali gitti", "Ali okula gitti", "gitti okula Ali", "Ali gitti okula"]},

    {"karisik": ["içiyor", "Kedi", "süt"],
     "dogru": "Kedi süt içiyor",
     "secenekler": ["süt Kedi içiyor", "içiyor Kedi süt", "Kedi süt içiyor", "Kedi içiyor süt"]},

    {"karisik": ["yaptı", "Annem", "pasta", "bize"],
     "dogru": "Annem bize pasta yaptı",
     "secenekler": ["pasta Annem bize yaptı", "Annem bize pasta yaptı", "bize pasta yaptı Annem", "yaptı pasta bize Annem"]},

    {"karisik": ["güzel", "Bugün", "hava", "çok"],
     "dogru": "Bugün hava çok güzel",
     "secenekler": ["çok hava Bugün güzel", "Bugün hava çok güzel", "hava güzel Bugün çok", "güzel çok hava Bugün"]},

    {"karisik": ["uçuyor", "Kuşlar", "gökyüzünde"],
     "dogru": "Kuşlar gökyüzünde uçuyor",
     "secenekler": ["gökyüzünde Kuşlar uçuyor", "uçuyor Kuşlar gökyüzünde", "Kuşlar gökyüzünde uçuyor", "Kuşlar uçuyor gökyüzünde"]},

    {"karisik": ["okudu", "Öğretmen", "kitap", "bize"],
     "dogru": "Öğretmen bize kitap okudu",
     "secenekler": ["kitap Öğretmen bize okudu", "bize kitap okudu Öğretmen", "Öğretmen bize kitap okudu", "okudu kitap bize Öğretmen"]},

    {"karisik": ["söyledi", "kız", "Küçük", "şarkı"],
     "dogru": "Küçük kız şarkı söyledi",
     "secenekler": ["şarkı Küçük kız söyledi", "Küçük kız şarkı söyledi", "söyledi şarkı kız Küçük", "kız şarkı Küçük söyledi"]},

    {"karisik": ["suladı", "Dedem", "bahçede", "çiçek"],
     "dogru": "Dedem bahçede çiçek suladı",
     "secenekler": ["çiçek Dedem bahçede suladı", "bahçede çiçek suladı Dedem", "Dedem bahçede çiçek suladı", "suladı çiçek bahçede Dedem"]},

    {"karisik": ["aldı", "Ablam", "hediye", "bana"],
     "dogru": "Ablam bana hediye aldı",
     "secenekler": ["hediye Ablam bana aldı", "Ablam bana hediye aldı", "bana hediye aldı Ablam", "aldı hediye bana Ablam"]},

    {"karisik": ["yüzüyor", "Balık", "suda"],
     "dogru": "Balık suda yüzüyor",
     "secenekler": ["suda Balık yüzüyor", "yüzüyor Balık suda", "Balık suda yüzüyor", "Balık yüzüyor suda"]},

    {"karisik": ["arkadaşız", "Sen", "iyi", "ve", "ben"],
     "dogru": "Sen ve ben iyi arkadaşız",
     "secenekler": ["ben Sen ve iyi arkadaşız", "Sen ve ben iyi arkadaşız", "iyi arkadaşız Sen ve ben", "arkadaşız iyi ben ve Sen"]},

    {"karisik": ["oynadık", "Ben", "arkadaşım", "ve", "parkta"],
     "dogru": "Ben ve arkadaşım parkta oynadık",
     "secenekler": ["parkta Ben ve arkadaşım oynadık", "Ben ve arkadaşım parkta oynadık", "oynadık parkta Ben ve arkadaşım", "arkadaşım parkta Ben ve oynadık"]},
]
# ============================================
# OYUN 4: SÖZCÜK AYIRMA
# Bir cümleyi oluşturan sözcükleri tek tek ayırt edebilme
# ============================================

SOZCUK_AYIRMA = [
    {"cumle": "Ali okula gitti.",     "dogru_kelimeler": ["Ali", "okula", "gitti"],     "tuzak": ["ev", "koştu", "park"]},
    {"cumle": "Kedi süt içiyor.",     "dogru_kelimeler": ["Kedi", "süt", "içiyor"],     "tuzak": ["köpek", "su", "yedi"]},
    {"cumle": "Bugün hava çok güzel.","dogru_kelimeler": ["Bugün", "hava", "çok", "güzel"], "tuzak": ["dün", "yağmur", "kötü"]},
    {"cumle": "Annem pasta yaptı.",   "dogru_kelimeler": ["Annem", "pasta", "yaptı"],   "tuzak": ["baba", "börek", "yedi"]},
    {"cumle": "Kuşlar uçuyor.",       "dogru_kelimeler": ["Kuşlar", "uçuyor"],          "tuzak": ["balık", "yüzüyor", "gökyüzü"]},
    {"cumle": "Öğretmen kitap okudu.","dogru_kelimeler": ["Öğretmen", "kitap", "okudu"], "tuzak": ["öğrenci", "defter", "yazdı"]},
    {"cumle": "Küçük kız şarkı söyledi.", "dogru_kelimeler": ["Küçük", "kız", "şarkı", "söyledi"], "tuzak": ["büyük", "erkek", "oyun"]},
    {"cumle": "Dedem çiçek suladı.",  "dogru_kelimeler": ["Dedem", "çiçek", "suladı"],   "tuzak": ["ninem", "ağaç", "dikti"]},
    {"cumle": "Ablam hediye aldı.",   "dogru_kelimeler": ["Ablam", "hediye", "aldı"],   "tuzak": ["kardeşim", "para", "verdi"]},
    {"cumle": "Balık suda yüzüyor.",  "dogru_kelimeler": ["Balık", "suda", "yüzüyor"],  "tuzak": ["kuş", "havada", "uçuyor"]},
    {"cumle": "Ben parkta oynadım.",  "dogru_kelimeler": ["Ben", "parkta", "oynadım"],  "tuzak": ["sen", "evde", "uyudum"]},
    {"cumle": "Güneş bugün parlıyor.", "dogru_kelimeler": ["Güneş", "bugün", "parlıyor"], "tuzak": ["ay", "dün", "sönüyor"]},
]
# ============================================
# OYUN 12: FONEM BİRLEŞTİRME
# Tek tek söylenen sesleri birleştirip sözcüğü oluşturma
# ============================================

FONEM_BIRLESTIRME = [
    {"sesler": ["K", "E", "D", "İ"],       "dogru": "Kedi",       "secenekler": ["Kedi", "Kadı", "Kediye", "Kede"]},
    {"sesler": ["B", "A", "L", "I", "K"],  "dogru": "Balık",      "secenekler": ["Balık", "Balk", "Balik", "Balkı"]},
    {"sesler": ["K", "A", "L", "E", "M"],  "dogru": "Kalem",      "secenekler": ["Kalem", "Kalam", "Kalen", "Kale"]},
    {"sesler": ["D", "E", "N", "İ", "Z"],  "dogru": "Deniz",      "secenekler": ["Deniz", "Denz", "Deni", "Denizs"]},
    {"sesler": ["O", "K", "U", "L"],       "dogru": "Okul",       "secenekler": ["Okul", "Okal", "Okil", "Oku"]},
    {"sesler": ["E", "L", "M", "A"],       "dogru": "Elma",       "secenekler": ["Elma", "Alma", "Elam", "Elm"]},
    {"sesler": ["G", "Ü", "L"],            "dogru": "Gül",        "secenekler": ["Gül", "Gul", "Güli", "Gil"]},
    {"sesler": ["T", "O", "P"],            "dogru": "Top",        "secenekler": ["Top", "Tap", "Tip", "Topu"]},
    {"sesler": ["M", "A", "S", "A"],       "dogru": "Masa",       "secenekler": ["Masa", "Mesa", "Mase", "Masal"]},
    {"sesler": ["Ç", "İ", "Ç", "E", "K"],  "dogru": "Çiçek",      "secenekler": ["Çiçek", "Çicek", "Çiçeğ", "Çiçke"]},
    {"sesler": ["S", "U"],                 "dogru": "Su",         "secenekler": ["Su", "Si", "Sa", "Sun"]},
    {"sesler": ["A", "Ğ", "A", "Ç"],       "dogru": "Ağaç",       "secenekler": ["Ağaç", "Ağac", "Ağaçı", "Ağç"]},
    {"sesler": ["Y", "I", "L", "D", "I", "Z"], "dogru": "Yıldız", "secenekler": ["Yıldız", "Yıldz", "Yıldızi", "Yılz"]},
    {"sesler": ["K", "İ", "T", "A", "P"],  "dogru": "Kitap",      "secenekler": ["Kitap", "Ketap", "Kitab", "Kitp"]},
    {"sesler": ["B", "U", "L", "U", "T"],  "dogru": "Bulut",      "secenekler": ["Bulut", "Bulat", "Buldu", "Bult"]},
]
# ============================================
# OYUN 8: HECE SİLME
# Sözcükten bir hece çıkarıldığında kalanı bulma
# ============================================

HECE_SILME = [
    {"sozcuk": "kalem",   "heceler": ["ka", "lem"],           "cikarilan": "ka",  "kalan": "lem",  "secenekler": ["lem", "ka", "kale", "em"]},
    {"sozcuk": "kitap",   "heceler": ["ki", "tap"],           "cikarilan": "ki",  "kalan": "tap",  "secenekler": ["tap", "ki", "kita", "ap"]},
    {"sozcuk": "okul",    "heceler": ["o", "kul"],            "cikarilan": "o",   "kalan": "kul",  "secenekler": ["kul", "o", "oku", "ul"]},
    {"sozcuk": "çiçek",   "heceler": ["çi", "çek"],           "cikarilan": "çi",  "kalan": "çek",  "secenekler": ["çek", "çi", "çiçe", "ek"]},
    {"sozcuk": "deniz",   "heceler": ["de", "niz"],           "cikarilan": "niz", "kalan": "de",   "secenekler": ["de", "niz", "deni", "iz"]},
    {"sozcuk": "bahçe",   "heceler": ["bah", "çe"],           "cikarilan": "bah", "kalan": "çe",   "secenekler": ["çe", "bah", "bahç", "e"]},
    {"sozcuk": "yıldız",  "heceler": ["yıl", "dız"],          "cikarilan": "yıl", "kalan": "dız",  "secenekler": ["dız", "yıl", "yıldı", "ız"]},
    {"sozcuk": "bulut",   "heceler": ["bu", "lut"],           "cikarilan": "bu",  "kalan": "lut",  "secenekler": ["lut", "bu", "bulu", "ut"]},
    {"sozcuk": "karpuz",  "heceler": ["kar", "puz"],          "cikarilan": "kar", "kalan": "puz",  "secenekler": ["puz", "kar", "karpu", "uz"]},
    {"sozcuk": "kelebek", "heceler": ["ke", "le", "bek"],     "cikarilan": "ke",  "kalan": "le bek", "secenekler": ["le bek", "ke", "bek", "lebek"]},
    {"sozcuk": "araba",   "heceler": ["a", "ra", "ba"],       "cikarilan": "a",   "kalan": "ra ba", "secenekler": ["ra ba", "a", "raba", "ba"]},
    {"sozcuk": "merhaba", "heceler": ["mer", "ha", "ba"],     "cikarilan": "ba",  "kalan": "mer ha", "secenekler": ["mer ha", "ba", "mer", "haba"]},
    {"sozcuk": "arkadaş", "heceler": ["ar", "ka", "daş"],     "cikarilan": "ka",  "kalan": "ar daş", "secenekler": ["ar daş", "ka", "ar", "kadaş"]},
    {"sozcuk": "öğretmen","heceler": ["öğ", "ret", "men"],    "cikarilan": "men", "kalan": "öğ ret", "secenekler": ["öğ ret", "men", "öğ", "ret"]},
    {"sozcuk": "pencere", "heceler": ["pen", "ce", "re"],     "cikarilan": "pen", "kalan": "ce re", "secenekler": ["ce re", "pen", "ce", "pence"]},
]
# ============================================
# OYUN 14: FONEM SİLME
# Sözcükten bir ses (harf) çıkarıldığında kalanı bulma
# ============================================

FONEM_SILME = [
    # Baştaki sessizi çıkar
    {"sozcuk": "kar",  "cikarilan": "k", "kalan": "ar",  "secenekler": ["ar", "k", "kar", "r"]},
    {"sozcuk": "kel",  "cikarilan": "k", "kalan": "el",  "secenekler": ["el", "k", "kel", "l"]},
    {"sozcuk": "kol",  "cikarilan": "k", "kalan": "ol",  "secenekler": ["ol", "k", "kol", "l"]},
    {"sozcuk": "bal",  "cikarilan": "b", "kalan": "al",  "secenekler": ["al", "b", "bal", "l"]},
    {"sozcuk": "bel",  "cikarilan": "b", "kalan": "el",  "secenekler": ["el", "b", "bel", "l"]},
    {"sozcuk": "gel",  "cikarilan": "g", "kalan": "el",  "secenekler": ["el", "g", "gel", "l"]},
    {"sozcuk": "gül",  "cikarilan": "g", "kalan": "ül",  "secenekler": ["ül", "g", "gül", "l"]},
    {"sozcuk": "göz",  "cikarilan": "g", "kalan": "öz",  "secenekler": ["öz", "g", "göz", "z"]},
    {"sozcuk": "sal",  "cikarilan": "s", "kalan": "al",  "secenekler": ["al", "s", "sal", "l"]},
    {"sozcuk": "dal",  "cikarilan": "d", "kalan": "al",  "secenekler": ["al", "d", "dal", "l"]},
    {"sozcuk": "ver",  "cikarilan": "v", "kalan": "er",  "secenekler": ["er", "v", "ver", "r"]},
    {"sozcuk": "tel",  "cikarilan": "t", "kalan": "el",  "secenekler": ["el", "t", "tel", "l"]},

    # Sondaki sessizi çıkar
    {"sozcuk": "kar",  "cikarilan": "r", "kalan": "ka",  "secenekler": ["ka", "r", "kar", "k"]},
    {"sozcuk": "kel",  "cikarilan": "l", "kalan": "ke",  "secenekler": ["ke", "l", "kel", "k"]},
    {"sozcuk": "kal",  "cikarilan": "l", "kalan": "ka",  "secenekler": ["ka", "l", "kal", "k"]},
    {"sozcuk": "bal",  "cikarilan": "l", "kalan": "ba",  "secenekler": ["ba", "l", "bal", "b"]},
    {"sozcuk": "gül",  "cikarilan": "l", "kalan": "gü",  "secenekler": ["gü", "l", "gül", "g"]},
    {"sozcuk": "göz",  "cikarilan": "z", "kalan": "gö",  "secenekler": ["gö", "z", "göz", "g"]},
]
# ============================================
# OYUN 15: FONEM EKLEME
# Sözcüğe yeni bir ses ekleyerek yeni sözcük oluşturma
# ============================================

FONEM_EKLEME = [
    # Başa ses ekleme
    {"sozcuk": "ar",   "eklenen": "k", "konum": "baştan", "yeni": "kar",  "secenekler": ["kar", "ar", "ark", "rak"]},
    {"sozcuk": "el",   "eklenen": "g", "konum": "baştan", "yeni": "gel",  "secenekler": ["gel", "el", "elk", "leg"]},
    {"sozcuk": "al",   "eklenen": "b", "konum": "baştan", "yeni": "bal",  "secenekler": ["bal", "al", "alb", "lab"]},
    {"sozcuk": "al",   "eklenen": "s", "konum": "baştan", "yeni": "sal",  "secenekler": ["sal", "al", "als", "las"]},
    {"sozcuk": "al",   "eklenen": "d", "konum": "baştan", "yeni": "dal",  "secenekler": ["dal", "al", "ald", "lad"]},
    {"sozcuk": "el",   "eklenen": "t", "konum": "baştan", "yeni": "tel",  "secenekler": ["tel", "el", "elt", "let"]},
    {"sozcuk": "öz",   "eklenen": "g", "konum": "baştan", "yeni": "göz",  "secenekler": ["göz", "öz", "özg", "gözs"]},
    {"sozcuk": "ül",   "eklenen": "g", "konum": "baştan", "yeni": "gül",  "secenekler": ["gül", "ül", "ülg", "gülü"]},
    {"sozcuk": "er",   "eklenen": "v", "konum": "baştan", "yeni": "ver",  "secenekler": ["ver", "er", "erv", "verr"]},
    {"sozcuk": "ok",   "eklenen": "k", "konum": "baştan", "yeni": "kok",  "secenekler": ["kok", "ok", "okk", "koko"]},

    # Sona ses ekleme
    {"sozcuk": "su",   "eklenen": "n", "konum": "sondan", "yeni": "sun",  "secenekler": ["sun", "su", "nus", "suu"]},
    {"sozcuk": "kar",  "eklenen": "a", "konum": "sondan", "yeni": "kara", "secenekler": ["kara", "kar", "arak", "karak"]},
    {"sozcuk": "gel",  "eklenen": "i", "konum": "sondan", "yeni": "geli", "secenekler": ["geli", "gel", "igel", "gell"]},
    {"sozcuk": "kol",  "eklenen": "u", "konum": "sondan", "yeni": "kolu", "secenekler": ["kolu", "kol", "ukol", "koll"]},
    {"sozcuk": "göz",  "eklenen": "l", "konum": "sondan", "yeni": "gözl", "secenekler": ["gözl", "göz", "lgöz", "gözz"]},
    {"sozcuk": "ke",   "eklenen": "l", "konum": "sondan", "yeni": "kel",  "secenekler": ["kel", "ke", "lke", "kee"]},
]
# ============================================
# OYUN 16: FONEM DEĞİŞTİRME
# Sözcükteki bir sesi değiştirerek yeni sözcük oluşturma
# ============================================

FONEM_DEGISTIRME = [
    # Baştaki harfi değiştir
    {"sozcuk": "kar",  "eski": "k", "yeni": "b", "konum": "baştan", "sonuc": "bar",  "secenekler": ["bar", "kar", "bak", "rak"]},
    {"sozcuk": "kar",  "eski": "k", "yeni": "y", "konum": "baştan", "sonuc": "yar",  "secenekler": ["yar", "kar", "kay", "ray"]},
    {"sozcuk": "kar",  "eski": "k", "yeni": "s", "konum": "baştan", "sonuc": "sar",  "secenekler": ["sar", "kar", "sak", "ras"]},
    {"sozcuk": "gel",  "eski": "g", "yeni": "s", "konum": "baştan", "sonuc": "sel",  "secenekler": ["sel", "gel", "ges", "leg"]},
    {"sozcuk": "gel",  "eski": "g", "yeni": "t", "konum": "baştan", "sonuc": "tel",  "secenekler": ["tel", "gel", "get", "leg"]},
    {"sozcuk": "gül",  "eski": "g", "yeni": "k", "konum": "baştan", "sonuc": "kül",  "secenekler": ["kül", "gül", "gük", "lüg"]},
    {"sozcuk": "bal",  "eski": "b", "yeni": "d", "konum": "baştan", "sonuc": "dal",  "secenekler": ["dal", "bal", "bad", "lab"]},
    {"sozcuk": "bal",  "eski": "b", "yeni": "s", "konum": "baştan", "sonuc": "sal",  "secenekler": ["sal", "bal", "bas", "lab"]},
    {"sozcuk": "kol",  "eski": "k", "yeni": "y", "konum": "baştan", "sonuc": "yol",  "secenekler": ["yol", "kol", "koy", "lok"]},
    {"sozcuk": "kel",  "eski": "k", "yeni": "t", "konum": "baştan", "sonuc": "tel",  "secenekler": ["tel", "kel", "ket", "lek"]},
    {"sozcuk": "göz",  "eski": "g", "yeni": "s", "konum": "baştan", "sonuc": "söz",  "secenekler": ["söz", "göz", "gös", "zög"]},

    # Sondaki harfi değiştir
    {"sozcuk": "kar",  "eski": "r", "yeni": "z", "konum": "sondan", "sonuc": "kaz",  "secenekler": ["kaz", "kar", "kaz", "raz"]},
    {"sozcuk": "kar",  "eski": "r", "yeni": "ş", "konum": "sondan", "sonuc": "kaş",  "secenekler": ["kaş", "kar", "kaş", "raş"]},
    {"sozcuk": "gül",  "eski": "l", "yeni": "z", "konum": "sondan", "sonuc": "güz",  "secenekler": ["güz", "gül", "güğ", "lüz"]},
    {"sozcuk": "bal",  "eski": "l", "yeni": "ş", "konum": "sondan", "sonuc": "baş",  "secenekler": ["baş", "bal", "bağ", "laş"]},
    {"sozcuk": "göz",  "eski": "z", "yeni": "l", "konum": "sondan", "sonuc": "göl",  "secenekler": ["göl", "göz", "göğ", "zöl"]},
    {"sozcuk": "kel",  "eski": "l", "yeni": "z", "konum": "sondan", "sonuc": "kez",  "secenekler": ["kez", "kel", "keğ", "lez"]},
]
# ============================================
# OYUN 9: FONEM AYIRT ETME
# Sözcükler içindeki aynı/farklı sesleri ayırt edebilme
# ============================================

FONEM_AYIRT = [
    {"sozcukler": ["bal", "bebek", "masa"],         "farkli": "masa",   "ortak_ses": "B",  "farkli_ses": "M"},
    {"sozcukler": ["kalem", "kedi", "su"],          "farkli": "su",     "ortak_ses": "K",  "farkli_ses": "S"},
    {"sozcukler": ["elma", "ev", "göz"],            "farkli": "göz",    "ortak_ses": "E",  "farkli_ses": "G"},
    {"sozcukler": ["top", "tava", "kar"],           "farkli": "kar",    "ortak_ses": "T",  "farkli_ses": "K"},
    {"sozcukler": ["deniz", "dede", "bulut"],       "farkli": "bulut",  "ortak_ses": "D",  "farkli_ses": "B"},
    {"sozcukler": ["gül", "gemi", "süt"],           "farkli": "süt",    "ortak_ses": "G",  "farkli_ses": "S"},
    {"sozcukler": ["araba", "anne", "kedi"],        "farkli": "kedi",   "ortak_ses": "A",  "farkli_ses": "K"},
    {"sozcukler": ["su", "sabun", "gül"],           "farkli": "gül",    "ortak_ses": "S",  "farkli_ses": "G"},
    {"sozcukler": ["masa", "mavi", "kedi"],         "farkli": "kedi",   "ortak_ses": "M",  "farkli_ses": "K"},
    {"sozcukler": ["fare", "fil", "kuş"],           "farkli": "kuş",    "ortak_ses": "F",  "farkli_ses": "K"},
    {"sozcukler": ["yıldız", "yol", "gül"],         "farkli": "gül",    "ortak_ses": "Y",  "farkli_ses": "G"},
    {"sozcukler": ["çiçek", "çanta", "balık"],      "farkli": "balık",  "ortak_ses": "Ç",  "farkli_ses": "B"},
    {"sozcukler": ["kapı", "kalem", "telefon"],     "farkli": "telefon", "ortak_ses": "K", "farkli_ses": "T"},
    {"sozcukler": ["pencere", "para", "saat"],      "farkli": "saat",   "ortak_ses": "P",  "farkli_ses": "S"},
    {"sozcukler": ["zeytin", "zil", "kaşık"],       "farkli": "kaşık",  "ortak_ses": "Z",  "farkli_ses": "K"},
]
# ============================================
# OYUN 13: FONEM BÖLME
# Sözcüğü oluşturan sesleri tek tek söyleyebilme
# ============================================

FONEM_BOLME = [
    {"sozcuk": "kar",  "harfler": ["k", "a", "r"],
     "dogru": "k - a - r",
     "secenekler": ["k - a - r", "ka - r", "k - ar", "kar"]},

    {"sozcuk": "gül",  "harfler": ["g", "ü", "l"],
     "dogru": "g - ü - l",
     "secenekler": ["g - ü - l", "gü - l", "g - ül", "gül"]},

    {"sozcuk": "bal",  "harfler": ["b", "a", "l"],
     "dogru": "b - a - l",
     "secenekler": ["b - a - l", "ba - l", "b - al", "bal"]},

    {"sozcuk": "kol",  "harfler": ["k", "o", "l"],
     "dogru": "k - o - l",
     "secenekler": ["k - o - l", "ko - l", "k - ol", "kol"]},

    {"sozcuk": "göz",  "harfler": ["g", "ö", "z"],
     "dogru": "g - ö - z",
     "secenekler": ["g - ö - z", "gö - z", "g - öz", "göz"]},

    {"sozcuk": "su",   "harfler": ["s", "u"],
     "dogru": "s - u",
     "secenekler": ["s - u", "su", "s -su", "su - s"]},

    {"sozcuk": "el",   "harfler": ["e", "l"],
     "dogru": "e - l",
     "secenekler": ["e - l", "el", "e - l", "e - l"]},

    {"sozcuk": "at",   "harfler": ["a", "t"],
     "dogru": "a - t",
     "secenekler": ["a - t", "at", "a - t", "a - t"]},

    {"sozcuk": "masa", "harfler": ["m", "a", "s", "a"],
     "dogru": "m - a - s - a",
     "secenekler": ["m - a - s - a", "ma - sa", "mas - a", "masa"]},

    {"sozcuk": "kedi", "harfler": ["k", "e", "d", "i"],
     "dogru": "k - e - d - i",
     "secenekler": ["k - e - d - i", "ke - di", "ked - i", "kedi"]},

    {"sozcuk": "deniz","harfler": ["d", "e", "n", "i", "z"],
     "dogru": "d - e - n - i - z",
     "secenekler": ["d - e - n - i - z", "de - niz", "den - iz", "deniz"]},

    {"sozcuk": "kalem","harfler": ["k", "a", "l", "e", "m"],
     "dogru": "k - a - l - e - m",
     "secenekler": ["k - a - l - e - m", "ka - lem", "kal - em", "kalem"]},

    {"sozcuk": "yıldız","harfler": ["y", "ı", "l", "d", "ı", "z"],
     "dogru": "y - ı - l - d - ı - z",
     "secenekler": ["y - ı - l - d - ı - z", "yıl - dız", "yıl - d - ız", "yıldız"]},
]
# ============================================
# OYUN 6: KAFİYE ÜRETME
# Verilen sözcükle kafiyeli YENİ sözcükler üretebilme
# (Çoklu seçim: kafiyeli olanların TÜMÜNÜ seç)
# ============================================

KAFIYE_URET = [
    {"hedef": "kal",  "dogrular": ["dal", "sal", "bal"],       "secenekler": ["dal", "gül", "sal", "göl", "bal", "gel"]},
    {"hedef": "kar",  "dogrular": ["yar", "sar", "nar"],       "secenekler": ["yar", "kel", "sar", "kır", "nar", "kor"]},
    {"hedef": "göz",  "dogrular": ["söz", "toz", "yaz"],       "secenekler": ["söz", "gaz", "toz", "yaz", "dız", "buz"]},
    {"hedef": "ben",  "dogrular": ["sen", "ten", "gen"],       "secenekler": ["sen", "ban", "ten", "bin", "gen", "bun"]},
    {"hedef": "ev",   "dogrular": ["sev", "tev", "nev"],       "secenekler": ["sev", "av", "tev", "iv", "nev", "as"]},
    {"hedef": "el",   "dogrular": ["gel", "sel", "yel"],       "secenekler": ["gel", "al", "sel", "öl", "yel", "ül"]},
    {"hedef": "taş",  "dogrular": ["baş", "kaş", "yaş"],       "secenekler": ["baş", "tuş", "kaş", "teş", "yaş", "tiş"]},
    {"hedef": "kuş",  "dogrular": ["duş", "tuş", "muş"],       "secenekler": ["duş", "kaş", "tuş", "kiş", "muş", "koş"]},
    {"hedef": "yol",  "dogrular": ["kol", "sol", "bol"],       "secenekler": ["kol", "yel", "sol", "yıl", "bol", "yul"]},
    {"hedef": "tel",  "dogrular": ["sel", "gel", "yel"],       "secenekler": ["sel", "tal", "gel", "tül", "yel", "top"]},
    {"hedef": "saç",  "dogrular": ["taç", "haç", "baç"],       "secenekler": ["taç", "suç", "haç", "seç", "baç", "sıç"]},
    {"hedef": "kaz",  "dogrular": ["yaz", "saz", "naz"],       "secenekler": ["yaz", "kız", "saz", "koz", "naz", "kuz"]},
]
# ============================================
# OYUN 17: OTOMATİK OKUMA (Flash Kart)
# Kısa sürede hızlı okuma oyunu
# ============================================

OTOMATIK_OKUMA = [
    {"sozcuk": "araba",     "secenekler": ["araba", "arma", "arazi", "adam"]},
    {"sozcuk": "kalem",     "secenekler": ["kalem", "kale", "kaldı", "kalın"]},
    {"sozcuk": "kitap",     "secenekler": ["kitap", "kita", "katıp", "kilit"]},
    {"sozcuk": "deniz",     "secenekler": ["deniz", "deniz", "deni", "densiz"]},
    {"sozcuk": "çiçek",     "secenekler": ["çiçek", "çicek", "çekiç", "çelik"]},
    {"sozcuk": "yıldız",    "secenekler": ["yıldız", "yıldı", "yıldızlı", "yıldırım"]},
    {"sozcuk": "bulut",     "secenekler": ["bulut", "bulu", "buluş", "bulantı"]},
    {"sozcuk": "karpuz",    "secenekler": ["karpuz", "karpu", "karpit", "kartal"]},
    {"sozcuk": "kelebek",   "secenekler": ["kelebek", "kele", "kelepçe", "keler"]},
    {"sozcuk": "merhaba",   "secenekler": ["merhaba", "merha", "merhem", "merasim"]},
    {"sozcuk": "arkadaş",   "secenekler": ["arkadaş", "arka", "arkalı", "arkıt"]},
    {"sozcuk": "öğretmen",  "secenekler": ["öğretmen", "öğrenci", "öğreti", "öğrenim"]},
    {"sozcuk": "pencere",   "secenekler": ["pencere", "pençe", "pembe", "pense"]},
    {"sozcuk": "bilgisayar","secenekler": ["bilgisayar", "bilgi", "bilgin", "bilgili"]},
    {"sozcuk": "kaplumbağa","secenekler": ["kaplumbağa", "kaplan", "kaplama", "kaplıca"]},
    {"sozcuk": "gökyüzü",   "secenekler": ["gökyüzü", "gök", "gözlük", "göçmen"]},
    {"sozcuk": "bahçıvan",  "secenekler": ["bahçıvan", "bahçe", "bahar", "bahane"]},
    {"sozcuk": "yapraklar", "secenekler": ["yapraklar", "yaprak", "yapı", "yapmacık"]},
]
def oyun_sorularini_getir(oyun_no):
    """Oyun numarasına göre soru listesini döndür."""
    if oyun_no == 1:
        return SOZCUK_SAYMA
    elif oyun_no == 2:
        return SOZCUK_ATMA
    elif oyun_no == 3:
        return SOZCUK_BIRLESTIRME
    elif oyun_no == 4:
        return SOZCUK_AYIRMA
    elif oyun_no == 5:
        return KAFIYE_AYIRT
    elif oyun_no == 6:
        return KAFIYE_URET
    elif oyun_no == 7:
        return HECE_BOLME
    elif oyun_no == 8:
        return HECE_SILME
    elif oyun_no == 9:
        return FONEM_AYIRT
    elif oyun_no == 10:
        return BASTAKI_FONEM
    elif oyun_no == 11:
        return SONDAKI_FONEM
    elif oyun_no == 12:
        return FONEM_BIRLESTIRME
    elif oyun_no == 13:
        return FONEM_BOLME
    elif oyun_no == 14:
        return FONEM_SILME
    elif oyun_no == 15:
        return FONEM_EKLEME
    elif oyun_no == 16:
        return FONEM_DEGISTIRME
    elif oyun_no == 17:
        return OTOMATIK_OKUMA
    return []

def oyun_sorulari_karistir(oyun_no, adet=5):
    """Belirtilen oyundan rastgele N soru seç."""
    import random
    tum_sorular = oyun_sorularini_getir(oyun_no)
    if len(tum_sorular) <= adet:
        return tum_sorular
    return random.sample(tum_sorular, adet)

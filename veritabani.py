import sqlite3
import os

DB_ADI = "oyun.db"


def baglan():
    """Veritabanına bağlan ve bağlantıyı döndür."""
    conn = sqlite3.connect(DB_ADI)
    conn.row_factory = sqlite3.Row  # Sütunlara isimle erişmek için
    return conn


def tablolari_olustur():
    """Gerekli tabloları oluştur (yoksa)."""
    conn = baglan()
    imlec = conn.cursor()

    # Kullanıcılar tablosu
    imlec.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT UNIQUE NOT NULL,
            sifre TEXT NOT NULL,
            rol TEXT NOT NULL,
            ad_soyad TEXT,
            avatar TEXT DEFAULT '🧑‍🎓',
            seri_gun INTEGER DEFAULT 0,
            son_oynama_tarihi TEXT,
            harcanan_yildiz INTEGER DEFAULT 0,
            olusturma_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # İlerleme tablosu (hangi öğrenci hangi oyunu bitirdi)
    imlec.execute("""
        CREATE TABLE IF NOT EXISTS ilerleme (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogrenci_id INTEGER NOT NULL,
            ana_bolum INTEGER NOT NULL,
            oyun_no INTEGER NOT NULL,
            yildiz INTEGER DEFAULT 1,
            tamamlandi INTEGER DEFAULT 0,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (ogrenci_id) REFERENCES kullanicilar(id)
        )
    """)

    # Rozetler tablosu
    imlec.execute("""
        CREATE TABLE IF NOT EXISTS rozetler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogrenci_id INTEGER NOT NULL,
            rozet_adi TEXT NOT NULL,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (ogrenci_id) REFERENCES kullanicilar(id)
        )
    """)
        # Öğrenci Ekipmanları
    imlec.execute("""
        CREATE TABLE IF NOT EXISTS ogrenci_ekipman (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogrenci_id INTEGER NOT NULL,
            ekipman_no INTEGER NOT NULL,
            takili INTEGER DEFAULT 0,
            satin_alma_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(ogrenci_id, ekipman_no),
            FOREIGN KEY (ogrenci_id) REFERENCES kullanicilar(id)
        )
    """)
        # Oyun Atamaları tablosu (Admin panelinden dinamik)
    imlec.execute("""
        CREATE TABLE IF NOT EXISTS oyun_atamalari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ana_bolum INTEGER NOT NULL,
            sira INTEGER NOT NULL,
            oyun_no INTEGER NOT NULL,
            ozel_veri TEXT,
            olusturma_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(ana_bolum, sira)
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Tablolar hazır!")


def varsayilan_kullanicilari_ekle():
    """İlk kurulumda admin, örnek öğretmen ve öğrenci ekle."""
    conn = baglan()
    imlec = conn.cursor()

    kullanicilar = [
        ("admin",   "1234", "admin",   "Sistem Yöneticisi"),
        ("ogretmen", "1234", "ogretmen", "Örnek Öğretmen"),
        ("ali",     "1234", "ogrenci", "Ali Yılmaz"),
    ]

    for k in kullanicilar:
        try:
            imlec.execute(
                "INSERT INTO kullanicilar (kullanici_adi, sifre, rol, ad_soyad) VALUES (?, ?, ?, ?)",
                k
            )
            print(f"➕ Eklendi: {k[0]} ({k[2]})")
        except sqlite3.IntegrityError:
            print(f"ℹ️  Zaten var: {k[0]}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Bu dosyayı doğrudan çalıştırınca tabloları kurar
    tablolari_olustur()
    varsayilan_kullanicilari_ekle()
    print("🎉 Veritabanı hazır: oyun.db")
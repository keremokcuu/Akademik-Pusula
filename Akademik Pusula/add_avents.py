import sqlite3

conn = sqlite3.connect('firsat_pusulasi.db')
cursor = conn.cursor()

# Etkinlikler tablosunu oluşturuyoruz
cursor.execute("DROP TABLE IF EXISTS events;")
cursor.execute("""
    CREATE TABLE events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        category TEXT,
        date TEXT,
        location TEXT,
        tags TEXT,
        description TEXT
    );
""")

# Türkiye'deki gerçekçi öğrenci etkinlikleri, zirveleri ve seminerleri
etkinlikler = [
    ("Türkiye Bilişim Vakfı (TBV) Genç Teknoloji Zirvesi", "Zirve & Konferans", "2026-10-05", "İstanbul Teknik Üniversitesi (İTÜ) Maçka Kampüsü", "Yapay Zeka, Teknoloji, Liderlik, Lisans, Yüksek Lisans",
     "Türkiye Bilişim Vakfı ev sahipliğinde gerçekleşen Genç Teknoloji Zirvesi, ülkenin dört bir yanından gelen teknoloji meraklısı öğrencileri sektör liderleriyle buluşturuyor. Yapay zeka, büyük veri, bulut bilişim ve dijital dönüşüm konularında ilham verici panellerin yer alacağı zirvede, katılımcılar dev şirketlerin Ar-Ge yöneticileriyle birebir network kurma ve staj fırsatlarını yakalama şansı elde edecekler."),
     
    ("GDG Istanbul - DevFest 2026 Öğrenci Buluşması", "Teknoloji Buluşması", "2026-10-12", "Yıldız Teknik Üniversitesi Davutpaşa Kongre Merkezi", "Google, Flutter, Web, Cloud, Hackathon",
     "Google Developer Groups (GDG) Istanbul tarafından düzenlenen DevFest, yılın en büyük yazılım ve teknoloji buluşmalarından biridir. Mobil geliştirme (Flutter), yapay zeka araçları, modern web teknolojileri ve bulut bilişim mimarileri üzerine uygulamalı atölyelerin (workshop) düzenleneceği bu etkinlikte, yazılım dünyasındaki son trendleri yakından takip edebilir ve sürpriz hediyeler kazanabilirsiniz."),
     
    ("Kariyer.net Genç Yetenek Zirvesi ve Kampüs Tour", "Kariyer Zirvesi", "2026-10-18", "Ankara Bilkent Üniversitesi Konser Salonu", "Kariyer, İş Hayatı, Mülakat, Staj, Network",
     "Üniversite öğrencilerinin iş dünyasına ilk adımı atarken en çok ihtiyaç duyduğu rehberliği sunan Genç Yetenek Zirvesi Ankara'da! Şirketlerin insan kaynakları liderlerinden 'Mülakatlarda Öne Çıkma Taktikleri', 'CV Hazırlama Sırları' ve 'Geleceğin Meslekleri' oturumları seni bekliyor. Etkinlik sonunda katılımcılara resmi başarı sertifikası verilecektir."),
     
    ("ODTÜ IEEE Robotik Günleri ve Ar-Ge Seminerleri", "Seminer & Yarışma", "2026-10-25", "Orta Doğu Teknik Üniversitesi (ODTÜ) Kültür Kongre Merkezi", "Robotik, Gömülü Sistemler, Otonom, Mühendislik",
     "ODTÜ IEEE öğrenci kolu tarafından geleneksel olarak düzenlenen Robotik Günleri, Türkiye'nin en köklü mühendislik buluşmalarından biridir. Otonom robot yarışmaları, insansız hava araçları (İHA) panelleri ve savunma sanayiinin önde gelen mühendislerinin katıldığı teknik seminerlerle dolu dolu bir hafta sonu sizi bekliyor."),
     
    ("Boğaziçi Üniversitesi Bilişim Kulübü - CyberSecurity Summit", "Siber Güvenlik Zirvesi", "2026-11-02", "Boğaziçi Üniversitesi Albert Long Hall", "Siber Güvenlik, Etik Hacking, Network, Savunma",
     "Dijital dünyanın güvenliği her geçen gün daha da önem kazanıyor. Boğaziçi Üniversitesi CyberSecurity Summit; siber vatan savunması, etik hackleme dünyası, zararlı yazılım analizi ve kariyer imkanlarını ele alıyor. Sektörün en prestijli uzmanlarının konuşmacı olarak katılacağı zirveye tüm bilişim ve siber güvenlik meraklıları davetlidir."),
     
    ("Trakya Üniversitesi Kariyer ve Girişimcilik Zirvesi", "Bölgesel Zirfe", "2026-11-10", "Trakya Üniversitesi Balkan Kongre Merkezi", "Girişimcilik, Startup, Proje, Trakya, Öğrenci",
     "Trakya bölgesindeki üniversite öğrencilerini inovasyon ve girişimcilikle buluşturan bu özel zirvede; kendi startup'ını kurmuş genç girişimciler, yatırımcılar ve bölge sanayisinin öncü isimleri deneyimlerini paylaşıyor. Fikrini projeye dönüştürmek isteyenler için mentorluk masaları kurulacaktır.")
]

for e in etkinlikler:
    cursor.execute("""
        INSERT INTO events (title, category, date, location, tags, description)
        VALUES (?, ?, ?, ?, ?, ?)
    """, e)

conn.commit()
conn.close()
print("🎉 Tüm etkinlikler veritabanına başarıyla eklendi!")
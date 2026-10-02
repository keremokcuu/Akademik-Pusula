import sqlite3

conn = sqlite3.connect('firsat_pusulasi.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS opportunities;")
cursor.execute("""
    CREATE TABLE opportunities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        kategori TEXT,
        deadline TEXT,
        status TEXT,
        tags TEXT,
        description TEXT
    );
""")

# TÜM FAKÜLTELERİ VE BÖLÜMLERİ KAPSIYAN 100 DEVASAL İLAN LİSTESİ
yuz_dev_ilan = [
    # YAZILIM, BİLİŞİM & MÜHENDİSLİK (1-20)
    ("Google Developer Student Clubs (GDSC) Proje Destek Çağrısı", "Teknoloji & Yazılım", "2026-10-05", "Açık", "JavaScript, React, Open Source, Lisans", "Google Developer Student Clubs, üniversite öğrencilerinin teknoloji odaklı topluluk projeleri geliştirmesini destekleyen küresel bir programdır."),
    ("TÜBİTAK 2247-C STAR Stajyer Araştırmacı Burs Programı", "Burs & Ar-Ge", "2026-10-08", "Açık", "Python, SQL, Veri Analizi, Ar-Ge, Lisans", "TÜBİTAK tarafından yürütülen 2247-C STAR Programı, Türkiye'nin lider Ar-Ge ve yenilik projelerinde görev alacak lisans öğrencilerini desteklemektedir."),
    ("Baykar Yazılım Genç Staj Programı (Aday Mühendis)", "Staj & Mühendislik", "2026-10-10", "Açık", "C#, Python, Git, Staj, Lisans", "Milli teknoloji hamlesinin öncüsü Baykar, yazılım ve mühendislik alanında kariyer yapmak isteyen üniversite öğrencilerine kapılarını aralıyor."),
    ("Trendyol Backend Engineering Bootcamp & Staj", "Staj & Yazılım", "2026-10-12", "Açık", "Java, Python, Microservices, Staj, Lisans", "Türkiye'nin lider e-ticaret platformu Trendyol, yüksek ölçekli sistemler geliştirmek isteyen yazılımcılar için yoğunlaştırılmış bir staj programı düzenliyor."),
    ("Havelsan Siber Güvenlik Uzmanlık Eğitimi ve Stajı", "Staj & Eğitim", "2026-10-15", "Açık", "Siber Güvenlik, Linux, Ağ, Staj, Lisans", "Siber vatan savunmasının kritik aktörlerinden Havelsan, geleceğin siber güvenlik uzmanlarını yetiştiriyor."),
    ("Aselsan Mühendislik Yetenek Programı ve Staj", "Staj & Ar-Ge", "2026-10-18", "Açık", "C++, Gömülü Sistemler, Ar-Ge, Lisans", "Aselsan Ar-Ge merkezlerinde görev alarak gömülü sistemler ve elektronik harp teknolojileri üzerinde çalışın."),
    ("TUSAŞ Mühendislik Geliştirme ve Dönem Stajı", "Staj & Havacılık", "2026-10-20", "Açık", "Aerodinamik, CAD, Havacılık, Lisans", "Türk Havacılık ve Uzay Sanayii (TUSAŞ), uçak ve uzay mühendisliği ile ilgili branşlardaki başarılı öğrencilere staj imkanı sunuyor."),
    ("Roketsan Roket ve Füze Sistemleri Staj Programı", "Staj & Ar-Ge", "2026-10-22", "Açık", "Mühendislik, İtki, Mekatronik, Lisans", "Roketsan bünyesinde mühimmat ve roket teknolojileri üzerine Ar-Ge stajı yapma fırsatı."),
    ("Arçelik Global R&D Software Engineering Internship", "Staj & Yazılım", "2026-10-25", "Açık", "IoT, Embedded, C++, Lisans", "Arçelik Ar-Ge merkezlerinde nesnelerin interneti ve gömülü yazılım projelerinde görev alacak stajyerler aranıyor."),
    ("Logo Yazılım Genç Yetenek ve Kodlama Kampı", "Staj & Yazılım", "2026-10-28", "Açık", "C#, SQL, ERP, Lisans", "Kurumsal yazılım sektörünün devi Logo Yazılım'da yazılım geliştirme süreçlerini yerinde deneyimleyin."),
    ("Türk Telekom Teknoloji ve Yapay Zeka Stajı", "Staj & Telekom", "2026-11-02", "Açık", "5G, Network, Yapay Zeka, Lisans", "Telekomünikasyon altyapısı ve yapay zeka tabanlı şebeke optimizasyonu projelerinde staj imkanı."),
    ("Vodafone Discover Genç Yetenek ve Dönem Stajı", "Staj & Dijital", "2026-11-05", "Açık", "Dijital Pazarlama, Veri, Yazılım, Lisans", "Vodafone'un dinamik yapısında dijital dönüşüm projelerine liderlik edin."),
    ("Koç Digital Veri Bilimi ve Yapay Zeka Staj Programı", "Staj & Veri", "2026-11-08", "Açık", "Machine Learning, Python, Veri Bilimi", "Koç Digital ekibinde büyük veri analitiği ve yapay zeka modelleri geliştirme fırsatı."),
    ("SabancıDx İleri Analitik ve Bulut Bilişim Stajı", "Staj & Bulut", "2026-11-10", "Açık", "Cloud, DevOps, Yazılım, Lisans", "Bulut teknolojileri ve kurumsal yazılım mimarilerinde uzmanlaşmak isteyenler için staj programı."),
    ("Papara Fintek Yazılım Geliştirme Staj Programı", "Staj & Fintek", "2026-11-12", "Açık", "Go, Python, Fintek, Lisans", "Türkiye'nin öncü fintek şirketlerinden Papara'da yüksek performanslı ödeme sistemleri geliştirin."),
    ("Getir Mobile Engineering Internship", "Staj & Mobil", "2026-11-15", "Açık", "Kotlin, Swift, Mobil, Lisans", "Getir'in mobil uygulama ekiplerinde iOS ve Android geliştirme süreçlerine dahil olun."),
    ("Insider Growth Management ve Yazılım Stajı", "Staj & Teknoloji", "2026-11-18", "Açık", "SaaS, JavaScript, Global, Lisans", "Global teknoloji unicorn'umuz Insider'da uluslararası projelerde staj yapma şansı."),
    ("Peak Games Mobil Oyun Geliştirme ve Tasarım Stajı", "Staj & Oyun", "2026-11-20", "Açık", "C++, Unity, Oyun, Lisans", "Dünyaca ünlü mobil oyunların geliştirildiği Peak staj programı ile oyun sektörüne adım atın."),
    ("Dream Games Yazılım ve Mühendislik Stajı", "Staj & Oyun", "2026-11-22", "Açık", "Python, Algoritma, Oyun, Lisans", "Yüksek performanslı oyun motorları ve algoritmalar üzerinde çalışan Dream Games ekibine katılın."),
    ("TÜBİTAK BİLGEM Araştırmacı Bursu", "Burs & Ar-Ge", "2026-11-25", "Açık", "Kriptoloji, Siber Güvenlik, Ar-Ge", "Bilişim ve Bilgi Güvenliği İleri Teknolojiler Araştırma Merkezi'nde proje bursu."),

    # İŞLETME, EKONOMİ, FİNANS & BANKACILIK (21-40)
    ("Merkez Bankası Stajyer ve Uzman Yardımcılığı Aday Programı", "Staj & Finans", "2026-10-15", "Açık", "İktisat, İşletme, Ekonometri, Finans", "Türkiye Cumhuriyet Merkez Bankası bünyesinde ekonomik araştırmalar departmanında staj."),
    ("Akbank Gençlik Akademisi Veri ve Finans Stajı", "Staj & Bankacılık", "2026-10-02", "Açık", "Finans, Veri Analizi, İşletme", "Akbank Gençlik Akademisi ile bankacılık sektörünün dinamiklerini yerinde öğrenin."),
    ("Deloitte Genç Denetçi ve Danışmanlık Staj Programı", "Staj & Denetim", "2026-10-20", "Açık", "İşletme, Muhasebe, Finans, Ekonomi", "Dünyanın önde gelen denetim ve danışmanlık ağlarından Deloitte'ta uzun dönemli staj."),
    ("Türkiye İş Bankası Genç Hackathon ve Fintek Stajı", "Yarışma & Staj", "2026-10-12", "Açık", "Hackathon, Fintek, İşletme, İktisat", "İş Bankası'nın düzenlediği maratonda fikrini dök ve bankada kariyer kapısını arala."),
    ("Garanti BBVA Genç Yetenek Bankacılık Stajı", "Staj & Bankacılık", "2026-10-28", "Açık", "İşletme, İktisat, Finans, İletişim", "Garanti BBVA'nın geleceğin banka yöneticilerini yetiştirmek üzere tasarladığı staj programı."),
    ("PwC Türkiye Vergi ve Denetim Staj Programı", "Staj & Denetim", "2026-11-01", "Açık", "İşletme, Maliye, Ekonomi, Lisans", "PwC bünyesinde küresel standartlarda denetim ve vergi danışmanlığı stajı."),
    ("EY (Ernst & Young) Genç Danışman Stajı", "Staj & Danışmanlık", "2026-11-04", "Açık", "İşletme, Endüstri, Ekonomi", "Stratejik danışmanlık ve finansal hizmetler alanında EY deneyimi kazanın."),
    ("KPMG Türkiye Risk Yönetimi ve Finansal Staj", "Staj & Finans", "2026-11-07", "Açık", "Finans, İktisat, İşletme", "KPMG risk danışmanlığı ve finansal denetim ekiplerinde stajyer mühendis/uzman adayı."),
    ("Yapı Kredi Bankası Yetkinlik ve Staj Programı", "Staj & Bankacılık", "2026-11-10", "Açık", "Bankacılık, İktisat, İşletme", "Yapı Kredi şube ve genel müdürlük birimlerinde kapsamlı staj imkanı."),
    ("QNB Finansbank Genç Bankacı Stajı", "Staj & Bankacılık", "2026-11-13", "Açık", "Finans, İktisat, İşletme, Lisans", "QNB Finansbank'ın genç yetenekleri sektöre kazandıran staj programı."),
    ("DenizBank Operasyon ve Dijital Bankacılık Stajı", "Staj & Bankacılık", "2026-11-16", "Açık", "İşletme, İktisat, Yönetim", "Dijital bankacılık ürün yönetimi ve operasyon süreçlerinde staj."),
    ("Borsa İstanbul (BIST) Sermaye Piyasaları Stajı", "Staj & Finans", "2026-11-19", "Açık", "Finans, Ekonometri, İktisat", "Borsa İstanbul bünyesinde sermaye piyasaları ve finansal enstrümanlar üzerine staj."),
    ("Sermaye Piyasası Kurulu (SPK) Araştırma Bursu", "Burs & Finans", "2026-11-21", "Açık", "Finans, Ekonomi, Hukok, Lisans", "SPK tarafından finansal piyasalar ve hukuku alanında araştırma yapan öğrencilere burs."),
    ("TSKB (Sınai Kalkınma Bankası) Sürdürülebilir Finans Stajı", "Staj & Finans", "2026-11-24", "Açık", "Ekonomi, Sürdürülebilirlik, Finans", "Yeşil finansman ve sürdürülebilir kalkınma projelerinde staj imkanı."),
    ("Migros Ticaret Kategori Yönetimi ve Pazarlama Stajı", "Staj & Yönetim", "2026-11-27", "Açık", "İşletme, Pazarlama, Yönetim", "Perakende sektörünün lideri Migros'ta kategori yönetimi ve tedarik zinciri stajı."),
    ("Bim Birleşik Mağazalar Yönetici Adayı ve Stajı", "Staj & Perakende", "2026-11-29", "Açık", "İşletme, İktisat, Yönetim", "Mağazacılık operasyonları ve perakende yönetimi alanında uzun dönemli staj."),
    ("Unilever Future Leaders Staj Programı", "Staj & Pazarlama", "2026-12-02", "Açık", "İşletme, Pazarlama, Mühendislik", "Global FMCG devi Unilever'de marka yönetimi ve pazarlama stajı yapma şansı."),
    ("Procter & Gamble (P&G) Marka Yönetimi Stajı", "Staj & Pazarlama", "2026-12-05", "Açık", "İşletme, İletişim, Mühendislik", "P&G bünyesinde lider markaların stratejilerine yön veren staj programı."),
    ("Nestlé Türkiye Kurumsal İletişim ve Satış Stajı", "Staj & Satış", "2026-12-08", "Açık", "İşletme, İktisat, İletişim", "Nestlé satış operasyonları ve marka geliştirme departmanlarında staj."),
    ("Coca-Cola İçecek Satış ve Tedarik Zinciri Stajı", "Staj & Operasyon", "2026-12-10", "Açık", "Endüstri, İşletme, İktisat", "Lojistik, üretim planlama ve satış operasyonlarında CCI staj programı."),

    # HUKUK & ADALET (41-55)
    ("Türkiye Barolar Birliği Stajyer Avukat Gelişim Programı", "Hukuk & Eğitim", "2026-10-25", "Açık", "Hukuk, Adalet, Mevzuat, Dava", "Hukuk fakültesi öğrencileri için uluslararası ticaret hukuku ve dava pratikleri eğitimi."),
    ("Anadolu Kurumsal Hukuk Bürosu Yaz Stajı", "Staj & Hukuk", "2026-11-05", "Açık", "Şirketler Hukuku, Sözleşmeler, Hukuk", "Şirketler hukuku ve fikri mülkiyet alanlarında uzmanlaşmak isteyen hukukçulara staj."),
    ("Uluslararası İnsan Hakları Merkezi Araştırma Bursu", "Burs & Hukuk", "2026-11-10", "Açık", "İnsan Hakları, Uluslararası Hukuk", "İnsan hakları savunuculuğu ve uluslararası tahkim konularında araştırma bursu."),
    ("Moral & Partners Hukuk Bürosu Staj Programı", "Staj & Hukuk", "2026-11-14", "Açık", "Ticaret Hukuku, Birleşmeler, Hukuk", "Uluslararası nitelikteki birleşme ve devralma projelerinde hukuk stajı."),
    ("Herguner Bilgen Ozeke Hukuk Bürosu Yaz Stajı", "Staj & Hukuk", "2026-11-18", "Açık", "Enerji Hukuku, Şirketler, Hukuk", "Türkiye'nin köklü hukuk bürolarından Hergüner'de geleceğin avukatları için staj."),
    ("Paksoy Hukuk Bürosu Öğrenci Staj Programı", "Staj & Hukuk", "2026-11-22", "Açık", "Vergi Hukuku, Dava, Hukuk, Lisans", "Vergi uyuşmazlıkları ve ticaret hukuku davalarında pratik yapma imkanı."),
    ("Çok Çalışkan Hukuk Bürosu İş Hukuku Stajı", "Staj & Hukuk", "2026-11-26", "Açık", "İş Hukuku, Ticaret, Hukuk", "İş hukuku ve sözleşmeler yönetimi alanında uzmanlaşma stajı."),
    ("Anayasa Mahkemesi Staj ve Araştırma Programı", "Staj & Kamu", "2026-11-30", "Açık", "Kamu Hukuku, Anayasa, Hukuk", "Anayasa Mahkemesi nezdinde bireysel başvuru ve kararlar üzerine staj araştırması."),
    ("Danıştay İdari Yargı Gözlem ve Staj Programı", "Staj & Kamu", "2026-12-03", "Açık", "İdare Hukuku, Yargı, Hukuk", "İdari yargı mercilerinde dava dosyası İnceleme ve gözlem stajı."),
    ("İstanbul Barosu Fikri Mülkiyet Hukuku Atölyesi", "Eğitim & Hukuk", "2026-12-07", "Açık", "Patent, Telif, Marka, Hukuk", "Fikri ve sınai mülkiyet hakları alanında uzmanlaşmak isteyen hukukçulara özel eğitim."),
    ("Rekabet Kurumu Stajyer Araştırmacı Programı", "Staj & Kamu", "2026-12-10", "Açık", "Rekabet Hukuku, İktisat, Hukuk", "Piyasa denetimleri ve rekabet ihlalleri incelemelerinde uzman yardımcılığı stajı."),
    ("Sermaye Piyasası Hukuku Araştırma Bursu", "Burs & Hukuk", "2026-12-14", "Açık", "Sermaye Piyasası, Şirketler, Hukuk", "Sermaye piyasası mevzuatı üzerine yazılacak makaleler için sağlanan araştırma bursu."),
    ("Ceza Hukuku Araştırmaları Derneği Stajı", "Staj & Hukuk", "2026-12-18", "Açık", "Ceza Hukuku, Kriminoloji, Hukuk", "Ceza muhakemesi hukuku ve kriminoloji alanında akademik staj imkanı."),
    ("Uluslararası Ticaret Tahkim Merkezi Stajı", "Staj & Hukuk", "2026-12-22", "Açık", "Tahkim, Uluslararası Hukuk", "Uluslararası ticari uyuşmazlıkların çözümünde tahkim süreçleri stajı."),
    ("Banka Hukuku Enstitüsü Öğrenci Programı", "Eğitim & Hukuk", "2026-12-25", "Açık", "Banka Hukuku, Finansal Suçlar", "Bankacılık mevzuatı ve finansal suçlarla mücadele hukukuna giriş programı."),

    # TIP, SAĞLIK BİLİMLERİ & BİYOMEDİKAL (56-70)
    ("Sağlık Bakanlığı Ulusal Tıp ve Sağlık Bilimleri Araştırma Bursu", "Burs & Sağlık", "2026-10-12", "Açık", "Tıp, Hemşirelik, Sağlık Bilimleri", "Klinik araştırmalar, halk sağlığı projeleri ve laboratuvar çalışmaları için karşılıksız burs."),
    ("Acıbadem Sağlık Grubu Genç Sağlıkçılar Staj Programı", "Staj & Sağlık", "2026-10-30", "Açık", "Tıp, Hemşirelik, Sağlık Yönetimi", "Hastane yönetimi, klinik uygulamalar ve sağlık teknolojileri alanında kariyer stajı."),
    ("TÜSEB Tıp Öğrencileri Ar-Ge ve Proje Bursu", "Burs & Tıp", "2026-11-02", "Açık", "Tıp, Biyomedikal, Genetik, Ar-Ge", "Aşı, ilaç ve biyoteknoloji projeleri için yüksek bütçeli öğrenci araştırma bursu."),
    ("Medicana Hastaneler Grubu Klinik Gözlem Stajı", "Staj & Sağlık", "2026-11-06", "Açık", "Tıp, Sağlık, Klinik, Lisans", "Tıp fakültesi öğrenciler klinik gözlem ve ameliyathane süreçleri stajı."),
    ("Memorial Sağlık Grubu Araştırma ve Staj Programı", "Staj & Sağlık", "2026-11-09", "Açık", "Tıp, Sağlık Bilimleri, Hemşirelik", "Tıp ve sağlık bilimleri öğrencileri için uluslararası standartlarda staj."),
    ("Hacettepe Teknokent Biyoteknoloji ve İlaç Ar-Ge Stajı", "Staj & Ar-Ge", "2026-11-13", "Açık", "Biyoteknoloji, Eczacılık, Tıp", "Yenilikçi ilaç molekülleri ve biyoteknolojik ürün geliştirme staj programı."),
    ("İzmir Biyotıp ve Genom Merkezi (İBG) Staj Programı", "Staj & Ar-Ge", "2026-11-17", "Açık", "Genetik, Moleküler Biyoloji, Tıp", "Genomik ve moleküler tıp laboratuvarlarında stajyer araştırmacı olma fırsatı."),
    ("Nobel İlaç Ar-Ge ve Klinik Araştırmalar Stajı", "Staj & Eczacılık", "2026-11-20", "Açık", "Eczacılık, Kimya, Tıp, Lisans", "İlaç üretimi, kalite kontrol ve klinik araştırmalar departmanlarında staj."),
    ("Abdi İbrahim İlaç Sanayi Üretim ve Ar-Ge Stajı", "Staj & Eczacılık", "2026-11-24", "Açık", "Eczacılık, Kimya Mühendisliği", "Türkiye'nin lider ilaç üreticisinde farmasötik teknoloji stajı."),
    ("Türk Eczacılar Birliği Genç Eczacı Gelişim Kampı", "Eğitim & Sağlık", "2026-11-28", "Açık", "Eczacılık, Klinik Eczacılık", "Klinik eczacılık uygulamaları ve eczane yönetimi üzerine ulusal öğrenci kampı."),
    ("Kızılay Ulusal Sağlık ve İlk Yardım Gönüllülük Ağı", "Gönüllülük & Sağlık", "2026-12-01", "Açık", "Sağlık, Tıp, İlk Yardım, Sosyal", "Kızılay sağlık operasyonları ve afet yönetimi ilk yardım projelerinde aktif görev."),
    ("Dünya Sağlık Örgütü (DSÖ) Genç Sağlık Elçileri", "Proje & Sağlık", "2026-12-04", "Açık", "Halk Sağlığı, Tıp, Küresel Sağlık", "Küresel sağlık politikaları ve epidemiyoloji araştırmaları proje desteği."),
    ("Biyomedikal Mühendisliği Derneği Proje Yarışması", "Yarışma & Sağlık", "2026-12-08", "Açık", "Biyomedikal, Cihaz, Mühendislik", "Tıbbi cihaz tasarımı ve yapay zeka destekli teşhis sistemleri yarışması."),
    ("Veteriner Hekimler Derneği Araştırma Bursu", "Burs & Sağlık", "2026-12-12", "Açık", "Veteriner, Hayvan Sağlığı", "Veteriner fakültesi öğrencilerine yönelik klinik ve zootekni araştırma bursu."),
    ("Dişhekimleri Birliği Klinik Staj ve Protez Atölyesi", "Staj & Sağlık", "2026-12-16", "Açık", "Diş Hekimliği, Protez, Cerrahi", "Diş hekimliği öğrencileri için ileri düzey protez ve cerrahi gözlem stajı."),

    # MİMARLIK, İNŞAAT & TASARIM (71-80)
    ("TÜBİTAK 2209-A Üniversite Öğrencileri Araştırma Projeleri", "Proje Desteği", "2026-11-01", "Açık", "Mimarlık, Mühendislik, Tasarım", "Tüm fakültelerden öğrencilerin kendi akademik araştırma fikirlerini hayata geçirmesi için proje bütçesi."),
    ("Tabanlıoğlu Mimarlık Tasarım ve Staj Programı", "Staj & Mimarlık", "2026-10-18", "Açık", "Mimarlık, İç Mimarlık, Tasarım", "Dünya çapında ödüllü projelere imza atan Tabanlıoğlu Mimarlık'ta staj yapma şansı."),
    ("DSİ Mühendislik ve Şantiye Staj Programı", "Staj & İnşaat", "2026-10-22", "Açık", "İnşaat, Makine, Jeoloji", "Devlet Su İşleri bünyesinde baraj, sulama ve altyapı projelerinde resmi yaz stajı."),
    ("Emre Arolat Architecture (EAA) Stajyer Mimar Programı", "Staj & Mimarlık", "2026-11-03", "Açık", "Mimarlık, Kentsel Tasarım", "Ulusal ve uluslararası mimari projelerde yer almak isteyen öğrenciler için staj."),
    ("Kentsel Dönüşüm ve Planlama Araştırma Bursu", "Burs & Mimarlık", "2026-11-11", "Açık", "Şehir Planlama, Mimarlık", "Sürdürülebilir şehirler ve kentsel dönüşüm projeleri için öğrenci araştırma bursu."),
    ("Autodesk Revit ve BIM Modelleme Uzmanlık Eğitimi", "Eğitim & Tasarım", "2026-11-19", "Açık", "BIM, Revit, Mimarlık, İnşaat", "Mimarlık ve inşaat mühendisliği öğrencilerine özel ileri düzey BIM modelleme kursu."),
    ("Karayolları Genel Müdürlüğü Köprü ve Yol Stajı", "Staj & İnşaat", "2026-11-25", "Açık", "İnşaat, Ulaştırma, Mühendislik", "Otoyol, viyadük ve tünel inşaatlarında Karayolları bünyesinde staj."),
    ("İGA İstanbul Havalimanı Mühendislik Staj Programı", "Staj & İnşaat", "2026-12-02", "Açık", "İnşaat, Havacılık, İşletme", "Dünyanın en büyük havalimanlarından İGA'da operasyon ve altyapı stajı."),
    ("Rönesans Holding Uluslararası Şantiye Stajı", "Staj & İnşaat", "2026-12-09", "Açık", "İnşaat, Mimarlık, Proje", "Devasa uluslararası projeleriyle bilinen Rönesans Holding'de şantiye stajı."),
    ("Çevre, Şehircilik ve İklim Değişikliği Bakanlığı Stajı", "Staj & Kamu", "2026-12-15", "Açık", "Mimarlık, Şehir Planlama, Çevre", "Bakanlık bünyesinde çevre yönetimi ve şehircilik projelerinde staj imkanı."),

    # PSİKOLOJİ, SOSYAL BİLİMLER & EĞİTİM (81-90)
    ("Türk Psikologlar Derneği Öğrenci Proje ve Staj Ağı", "Staj & Sosyal", "2026-10-22", "Açık", "Psikoloji, Rehberlik, Sosyoloji", "Psikoloji ve PDR öğrencilerine yönelik klinik gözlem programları ve atölyeler."),
    ("UNICEF Türkiye Gönüllülük ve Genç Liderlik Programı", "Sosyal & Proje", "2026-11-04", "Açık", "Sosyal Bilimler, Uluslararası İlişkiler", "Uluslararası kalkınma ve çocuk hakları projelerinde küresel staj ağı."),
    ("MEB Eğitimde İnovasyon ve Materyal Geliştirme Bursu", "Burs & Eğitim", "2026-11-15", "Açık", "Eğitim Fakültesi, Pedagoji", "Yenilikçi pedagoji yöntemleri ve sınıf içi materyal geliştirme projeleri için burs."),
    ("Davranış Bilimleri Enstitüsü (DBE) Staj Programı", "Staj & Psikoloji", "2026-11-21", "Açık", "Psikoloji, Travma, Terapi", "Psikoloji öğrencileri için kurumsal gözlem ve araştırma staj programı."),
    ("Toplum Gönüllüleri Vakfı (TOG) Proje Liderliği", "Gönüllülük & Sosyal", "2026-11-28", "Açık", "Sosyal Sorumluluk, Liderlik", "Gençlerin liderliğinde yürütülen ulusal sosyal sorumluluk projeleri hibesi."),
    ("Boğaziçi Eğitim ve Araştırma Vakfı Genç Eğitmen Bursu", "Burs & Eğitim", "2026-12-05", "Açık", "Eğitim, PDR, Sosyal Bilimler", "Dezavantajlı bölgelerdeki öğrencilere eğitim desteği sağlayan gönüllülere burs."),
    ("TÜBİTAK Sosyal Bilimler Araştırma Projesi Desteği", "Proje Desteği", "2026-12-11", "Açık", "Sosyoloji, Tarih, Psikoloji", "Sosyal bilimler alanında lisans öğrencileri için ulusal araştırma projesi fonu."),
    ("Uluslararası Göç Örgütü (IOM) Staj Programı", "Staj & Sosyal", "2026-12-17", "Açık", "Uluslararası İlişkiler, Sosyoloji", "Göç yönetimi ve insani yardım projelerinde uluslararası staj imkanı."),
    ("Klinik Psikoloji Araştırmaları Gönüllü Ağı", "Araştırma & Psikoloji", "2026-12-21", "Açık", "Psikoloji, Nöropsikoloji", "Akademik psikoloji laboratuvarlarında deney ve veri toplama asistanlığı."),
    ("Eğitim Reformu Girişimi (ERG) Staj Programı", "Staj & Eğitim", "2026-12-26", "Açık", "Eğitim Politikaları, Sosyal", "Türkiye'nin eğitim politikalarını izleyen ERG ekibinde politika analizi stajı."),

    # İLETİŞİM, MEDYA, GÜZEL SANATLAR & TEKNOFEST (91-100)
    ("TRT Genç İletişimci ve Medya Staj Programı", "Staj & Medya", "2026-10-14", "Açık", "İletişim, Gazetecilik, Radyo, TV", "TRT'nin köklü yayıncılık kültüründe kurgu, kamera ve dijital medya stajı."),
    ("Kültür ve Turizm Bakanlığı Sanat ve Arkeoloji Bursu", "Burs & Sanat", "2026-11-08", "Açık", "Güzel Sanatlar, Arkeoloji, Tarih", "Kazı çalışmaları ve müze restorasyonu projeleri için özel devlet bursu."),
    ("Format Reklam Ajansı Kreatif Tasarım Stajı", "Staj & Tasarım", "2026-10-26", "Açık", "Görsel İletişim, Grafik, Reklam", "Grafik tasarım ve reklamcılık alanında portfolyo odaklı ajans stajı."),
    ("Anadolu Ajansı (AA) Muhabirlik ve Dijital Medya Stajı", "Staj & Medya", "2026-11-12", "Açık", "Gazetecilik, İletişim, Fotoğraf", "Uluslararası haber ajansında habercilik ve dijital içerik üretimi stajı."),
    ("Netflix Türkiye Senaryo ve Film Yapım Atölyesi", "Eğitim & Sinema", "2026-11-20", "Açık", "Sinema, TV, Senaryo, İletişim", "Sinema ve televizyon öğrencilerine yönelik senaryo yazımı ve yapım atölyesi."),
    ("İletişim Araştırmaları Derneği Medya Bursu", "Burs & Medya", "2026-11-27", "Açık", "Yeni Medya, İletişim, Gazetecilik", "Dijital gazetecilik ve sosyal medya analizi araştırmaları için öğrenci bursu."),
    ("TEKNOFEST 2026 Sosyal İnovasyon ve Eğitim Teknolojileri", "TEKNOFEST", "2026-10-15", "Açık", "Eğitim, Sosyal, İnovasyon", "Eğitim, psikoloji ve sosyal bilimler öğrencilerinin toplumsal çözümler ürettiği yarışma."),
    ("TEKNOFEST 2026 Sağlıkta Yapay Zeka ve Biyoteknoloji", "TEKNOFEST", "2026-10-19", "Açık", "Tıp, Biyomedikal, Yapay Zeka", "Sağlık alanında yapay zeka destekli teşhis ve tedavi projelerini ödüllendiren yarışma."),
    ("TEKNOFEST 2026 İnsanlık Yararına Teknoloji Yarışması", "TEKNOFEST", "2026-10-25", "Açık", "Sosyal Fayda, Teknoloji, Tüm Bölümler", "Afet yönetimi, engelsiz yaşam ve tarım teknolojileri alanında sosyal fayda projeleri."),
    ("TÜBİTAK 2238 Girişimcilik ve Yenilikçi Fikir Yarışması", "Yarışma & Girişim", "2026-11-20", "Açık", "Girişimcilik, Startup, Tüm Bölümler", "Hangi fakülteden olursanız olun, iş fikrinizle katılabileceğiniz dev ulusal yarışma.")
]

for ilan in yuz_dev_ilan:
    cursor.execute("""
        INSERT INTO opportunities (title, kategori, deadline, status, tags, description)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ilan)

conn.commit()
conn.close()
print(f"🔥 İŞLEM TAMAM: Tam 100 adet devasa ve tüm fakülteleri kapsayan ilan sisteme yüklendi!")
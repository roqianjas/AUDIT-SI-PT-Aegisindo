# BAB II — PEMBAHASAN

## A. Framework yang Digunakan

### COBIT 2019

Dalam pelaksanaan audit sistem informasi pada PT. Murni Solusindo Nusantara, framework yang digunakan adalah **COBIT 2019** (Control Objectives for Information and Related Technologies). COBIT 2019 merupakan kerangka kerja tata kelola dan manajemen teknologi informasi yang dikembangkan oleh ISACA (Information Systems Audit and Control Association) dan dirilis pada tahun 2018 sebagai pemutakhiran dari COBIT 5 (Syuhada, 2021).

COBIT 2019 dipilih karena beberapa pertimbangan strategis. Pertama, framework ini merupakan versi terkini yang telah mengakomodasi perkembangan teknologi terbaru dan mengintegrasikan berbagai standar internasional seperti ITIL, TOGAF, dan CMMI. Kedua, COBIT 2019 menawarkan pendekatan yang lebih fleksibel melalui konsep *design factors* yang memungkinkan penyesuaian tata kelola sesuai dengan karakteristik dan kebutuhan spesifik organisasi. Ketiga, COBIT 2019 memiliki model penilaian kapabilitas yang lebih terstruktur berbasis CMMI (Capability Maturity Model Integration), sehingga hasil penilaian lebih akurat dan dapat dibandingkan dengan standar internasional (Algiffary dkk., 2023).

### Perbedaan COBIT 2019 dengan Versi Sebelumnya

COBIT 2019 memiliki beberapa perbedaan signifikan dibandingkan dengan COBIT 5, sebagaimana dirangkum dalam tabel berikut:

| Aspek | COBIT 5 | COBIT 2019 |
|-------|---------|------------|
| Jumlah Proses | 37 proses | 40 proses (5 Governance + 35 Management) |
| Prinsip | 5 prinsip | 6 prinsip (dibagi menjadi sistem tata kelola dan kerangka tata kelola) |
| Capability Level | 0–5 | 0–5 (berbasis CMMI) |
| Fleksibilitas | Tetap | Dapat disesuaikan dengan kebutuhan organisasi melalui design factors |
| Integrasi | Terbatas | Mengintegrasikan ITIL, TOGAF, CMMI |

Penggunaan COBIT versi terdahulu masih banyak dijumpai pada berbagai penelitian audit, seperti audit sistem informasi penjualan yang memanfaatkan COBIT 5 maupun audit sistem perkreditan yang menggunakan COBIT 4.0 (Zuraidah & Sulthon, 2022a, 2022b). Namun, pemilihan COBIT 2019 pada audit ini didasarkan pada keunggulan kerangka kerja terbaru tersebut dalam hal fleksibilitas dan integrasi standar internasional sebagaimana tercermin pada tabel di atas.

### 6 Prinsip COBIT 2019

COBIT 2019 dibangun di atas enam prinsip utama yang terbagi menjadi dua kelompok:

**Prinsip Sistem Tata Kelola:**
1. Memenuhi kebutuhan para pemangku kepentingan (*meeting stakeholder needs*)
2. Memungkinkan pendekatan yang holistik (*holistic approach*)
3. Penerapan sistem tata kelola yang dinamis (*dynamic governance system*)

**Prinsip Kerangka Tata Kelola:**
4. Memisahkan tata kelola dengan manajemen (*governance distinct from management*)
5. Dapat disesuaikan dengan kebutuhan organisasi (*tailored to enterprise needs*)
6. Mencakup organisasi secara menyeluruh (*end-to-end governance system*)

### Capability Level COBIT 2019

COBIT 2019 menggunakan model penilaian kapabilitas dengan 6 level (0–5) yang berbasis CMMI. Penilaian capability level ini bertujuan untuk mengukur sejauh mana suatu proses tata kelola TI telah dilaksanakan dan dikelola, sehingga organisasi dapat mengetahui posisi kematangannya serta menetapkan target perbaikan yang realistis (Sakron dkk., 2023):

| Level | Nama | Deskripsi |
|-------|------|-----------|
| **0** | Incomplete | Kurang memiliki kemampuan dasar, pendekatan tidak lengkap untuk memenuhi tujuan tata kelola dan manajemen |
| **1** | Performed | Proses kurang lebih mencapai tujuannya melalui penerapan serangkaian kegiatan yang tidak lengkap yang dapat dikategorikan sebagai initial atau intuitive — tidak terorganisasi dengan sangat baik |
| **2** | Managed | Proses mencapai tujuannya melalui penerapan serangkaian kegiatan dasar yang lengkap yang dapat dikategorikan sebagai performed |
| **3** | Established | Proses mencapai tujuannya, didefinisikan dengan baik, dan kinerjanya diukur secara kualitatif |
| **4** | Predictable | Proses mencapai tujuannya, terdefinisi dengan baik, dan kinerjanya diukur secara kuantitatif |
| **5** | Optimizing | Proses mencapai tujuannya, terdefinisi dengan baik, kinerjanya diukur, dan perbaikan berkelanjutan diterapkan |

### Rating Scale Ketercapaian

| Notasi | Deskripsi | Persentase Ketercapaian |
|--------|-----------|:-----------------------:|
| **N** | Not Achieved | 0–15% |
| **P** | Partially Achieved | >15%–50% |
| **L** | Largely Achieved | >50%–85% |
| **F** | Fully Achieved | >85%–100% |

---

## B. Domain dan Subdomain yang Digunakan

Berdasarkan analisis terhadap kondisi tata kelola teknologi informasi di PT. Murni Solusindo Nusantara, dipilih lima domain COBIT 2019 yang paling relevan dengan permasalahan yang dihadapi perusahaan. Pemilihan domain ini didasarkan pada profil bisnis perusahaan sebagai pengelola beberapa platform digital (Web Builder SaaS, Listing Property, dan Indoconnex) yang membutuhkan tata kelola TI yang komprehensif.

### 1. APO12 — Managed Risk (Pengelolaan Risiko)

Domain APO12 berfokus pada pengelolaan risiko teknologi informasi secara berkelanjutan. Pemilihan domain ini didasarkan pada fakta bahwa PT. Murni Solusindo Nusantara mengelola beberapa platform digital yang menyimpan data pelanggan dan transaksi bisnis. Risiko-risiko seperti kegagalan sistem, kebocoran data, dan serangan siber perlu diidentifikasi, dinilai, dan dikelola secara sistematis agar tidak mengganggu keberlangsungan operasional bisnis.

Tujuan pengelolaan risiko di domain ini mencakup:
- Identifikasi risiko TI yang berpotensi mempengaruhi operasional platform digital
- Pengumpulan dan analisis data risiko secara efektif
- Dokumentasi risiko yang terstruktur dan terpelihara

### 2. APO13 — Managed Security (Pengelolaan Keamanan)

Domain APO13 berfokus pada pengelolaan keamanan informasi perusahaan. Sebagai perusahaan yang memiliki platform SaaS dan menyimpan data pelanggan dalam jumlah besar, keamanan informasi menjadi aspek yang sangat kritis. Domain ini dipilih untuk mengevaluasi sejauh mana PT. Murni Solusindo Nusantara telah menerapkan kebijakan dan prosedur keamanan informasi yang memadai.

Aspek keamanan yang dievaluasi meliputi:
- Kebijakan keamanan informasi yang telah ditetapkan
- Mekanisme perlindungan terhadap akses tidak sah
- Sosialisasi dan kesadaran keamanan informasi di seluruh organisasi

### 3. BAI06 — Managed IT Changes (Pengelolaan Perubahan TI)

Domain BAI06 berfokus pada pengelolaan perubahan pada sistem dan infrastruktur TI. Pemilihan domain ini sangat relevan mengingat tim Web Development & SEO di PT. Murni Solusindo Nusantara secara rutin melakukan perubahan pada platform digital, mulai dari pembaruan fitur, perbaikan bug, hingga pembaruan keamanan. Tanpa pengelolaan perubahan yang terstruktur, perubahan yang tidak terkontrol dapat mengakibatkan gangguan pada layanan yang sedang berjalan.

Aspek perubahan TI yang dievaluasi mencakup:
- Pencatatan dan dokumentasi setiap perubahan sistem
- Proses persetujuan dan evaluasi dampak sebelum implementasi
- Evaluasi pasca-implementasi perubahan

### 4. DSS01 — Managed Operations (Pengelolaan Operasional)

Domain DSS01 berfokus pada pengelolaan operasional harian teknologi informasi. Sebagai perusahaan yang mengoperasikan beberapa platform digital secara bersamaan, PT. Murni Solusindo Nusantara membutuhkan operasional TI yang stabil dan termonitor. Domain ini dievaluasi untuk mengukur sejauh mana perusahaan telah mengelola operasional TI-nya secara efektif dan efisien.

Aspek operasional yang dievaluasi meliputi:
- Pemantauan rutin terhadap kinerja platform digital
- Prosedur penanganan insiden operasional
- Jadwal pemeliharaan infrastruktur TI

### 5. DSS05 — Managed Security Services (Pengelolaan Layanan Keamanan)

Domain DSS05 berfokus pada implementasi teknis layanan keamanan TI. Berbeda dengan APO13 yang lebih bersifat kebijakan dan strategis, DSS05 mengevaluasi aspek operasional layanan keamanan seperti perlindungan malware, pengelolaan hak akses, dan pencadangan data. Domain ini dipilih karena platform digital PT. Murni Solusindo Nusantara memerlukan perlindungan keamanan teknis yang handal.

Aspek layanan keamanan yang dievaluasi mencakup:
- Perlindungan terhadap malware dan ancaman siber
- Pengelolaan hak akses pengguna (access control)
- Prosedur pencadangan dan pemulihan data (backup & recovery)

### RACI Matrix

Dalam pelaksanaan audit ini, disusun RACI Matrix untuk mengidentifikasi peran dan tanggung jawab setiap pihak yang terlibat:

| Aktivitas | Kepala IT | Web Developer | IT Support | Digital Marketing | Finance | HR |
|-----------|:---------:|:------------:|:----------:|:----------------:|:-------:|:--:|
| Identifikasi Risiko TI (APO12) | **A** | R | R | C | I | I |
| Penetapan Kebijakan Keamanan (APO13) | **A** | R | R | I | I | C |
| Pengelolaan Perubahan TI (BAI06) | **A** | **R** | R | I | I | I |
| Pemantauan Operasional (DSS01) | **A** | R | **R** | I | I | I |
| Pengelolaan Layanan Keamanan (DSS05) | **A** | R | **R** | I | C | I |

Keterangan:
- **R** (Responsible) = Pihak yang melaksanakan tugas/pekerjaan
- **A** (Accountable) = Pihak yang bertanggung jawab atas keputusan dan memberikan arahan
- **C** (Consulted) = Pihak yang dimintai pendapat/masukan sebelum pengambilan keputusan
- **I** (Informed) = Pihak yang diberikan informasi mengenai pelaksanaan aktivitas

---

## C. Capability Level dan GAP

### Metodologi Perhitungan

Perhitungan capability level dalam audit ini dilakukan dengan menggunakan metodologi COBIT 2019 yang terdiri dari langkah-langkah berikut. Pendekatan berbasis kuesioner dengan skala Likert ini sejalan dengan praktik pengukuran tata kelola TI yang banyak digunakan pada penelitian audit sebelumnya (Destriani & Putra, 2023), serta merupakan teknik pengumpulan data yang lazim diterapkan dalam audit sistem informasi untuk menilai kondisi pengendalian secara objektif (Swastika & Putra, 2016):

1. Menyusun kuesioner dengan skala Likert 1–5 (STS=1, TS=2, R=3, S=4, SS=5) untuk setiap level kapabilitas pada masing-masing domain
2. Menyebarkan kuesioner kepada 8 responden internal PT. Murni Solusindo Nusantara
3. Menghitung skor total dan mean untuk setiap pertanyaan
4. Menghitung persentase ketercapaian: **% Ketercapaian = (Mean / Skor Maksimal) × 100%**
5. Menentukan rating berdasarkan persentase ketercapaian (N/P/L/F)
6. Menentukan capability level berdasarkan rating yang dicapai pada setiap level
7. Menghitung GAP antara capability level saat ini (as-is) dengan target (to-be)

Alur metodologi penelitian secara visual dapat dilihat pada Gambar 2.1.

> **Gambar 2.1** Alur Metodologi Penelitian

### Hasil Perhitungan Capability Level

#### Domain APO12 — Managed Risk

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.04 | **60.83%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.58 | **51.67%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.25 | **45.00%** | **P** (Partially Achieved) |

**Capability Level: 2 (Managed Process)**

Hasil perhitungan menunjukkan bahwa proses pengelolaan risiko TI di PT. Murni Solusindo Nusantara telah mencapai Level 2 (Managed Process). Level 1 dan Level 2 memperoleh rating L (Largely Achieved) dengan persentase ketercapaian masing-masing 60.83% dan 51.67%. Namun, Level 3 hanya memperoleh rating P (Partially Achieved) dengan persentase 45.00%, yang mengindikasikan bahwa proses pengelolaan risiko belum sepenuhnya terstandarisasi dan terdokumentasi secara formal.

#### Domain APO13 — Managed Security

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.25 | **65.00%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.71 | **54.17%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.33 | **46.67%** | **P** (Partially Achieved) |

**Capability Level: 2 (Managed Process)**

Proses pengelolaan keamanan informasi berada pada Level 2 dengan persentase ketercapaian Level 1 sebesar 65.00% dan Level 2 sebesar 54.17%, keduanya mencapai rating L. Level 3 hanya memperoleh 46.67% (rating P), yang menunjukkan bahwa meskipun kebijakan keamanan sudah ada dan mekanisme perlindungan sudah diterapkan, proses keamanan informasi belum sepenuhnya terstandarisasi dengan prosedur formal yang terdokumentasi.

#### Domain BAI06 — Managed IT Changes

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.13 | **62.50%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.67 | **53.33%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.33 | **46.67%** | **P** (Partially Achieved) |

**Capability Level: 2 (Managed Process)**

Proses pengelolaan perubahan TI berada pada Level 2. Pencatatan perubahan dan proses persetujuan sudah dilakukan (Level 1 = 62.50%), dan perencanaan perubahan sudah terstruktur (Level 2 = 53.33%). Namun, prosedur standar change management belum terdokumentasi secara lengkap dan konsisten (Level 3 = 46.67%), sehingga masih terdapat potensi perubahan yang tidak terkontrol.

#### Domain DSS01 — Managed Operations

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.33 | **66.67%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.79 | **55.83%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.42 | **48.33%** | **P** (Partially Achieved) |

**Capability Level: 2 (Managed Process)**

Domain DSS01 memperoleh skor tertinggi di antara kelima domain yang diaudit, dengan Level 1 mencapai 66.67%. Hal ini menunjukkan bahwa PT. Murni Solusindo Nusantara telah menjalankan operasional TI dengan cukup baik, terutama dalam hal pemantauan rutin platform digital dan jadwal pemeliharaan. Meskipun demikian, Level 3 masih berada pada 48.33% (rating P), menandakan bahwa SOP operasional belum sepenuhnya terdokumentasi dan diterapkan secara konsisten.

#### Domain DSS05 — Managed Security Services

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.38 | **67.50%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.58 | **51.67%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.25 | **45.00%** | **P** (Partially Achieved) |

**Capability Level: 2 (Managed Process)**

Domain DSS05 memiliki skor Level 1 tertinggi (67.50%), yang menunjukkan bahwa implementasi teknis layanan keamanan seperti perlindungan malware, pengelolaan hak akses, dan pencadangan data sudah berjalan dengan baik. Namun, pada Level 3 hanya mencapai 45.00%, yang mengindikasikan bahwa prosedur standar pengelolaan layanan keamanan belum terdokumentasi secara formal dan audit keamanan internal belum dilaksanakan secara berkala.

---

### Ringkasan Capability Level dan GAP Analysis

| No | Domain | Capability Level (As-is) | Target Level (To-be) | GAP |
|----|--------|:------------------------:|:--------------------:|:---:|
| 1 | APO12 — Managed Risk | **2** (Managed) | **4** (Predictable) | **2** |
| 2 | APO13 — Managed Security | **2** (Managed) | **4** (Predictable) | **2** |
| 3 | BAI06 — Managed IT Changes | **2** (Managed) | **4** (Predictable) | **2** |
| 4 | DSS01 — Managed Operations | **2** (Managed) | **4** (Predictable) | **2** |
| 5 | DSS05 — Managed Security Services | **2** (Managed) | **4** (Predictable) | **2** |
| | **Rata-rata** | **2** | **4** | **2** |

Berdasarkan tabel di atas, seluruh domain yang diaudit berada pada **Capability Level 2 (Managed Process)**. Kondisi ini menunjukkan bahwa PT. Murni Solusindo Nusantara telah menjalankan proses-proses tata kelola TI dan mencapai tujuan melalui kegiatan dasar yang cukup lengkap. Namun, proses-proses tersebut belum sepenuhnya terstandarisasi, terdokumentasi secara formal, dan diterapkan secara konsisten di seluruh divisi.

Target yang ditetapkan adalah **Level 4 (Predictable Process)**, di mana proses tata kelola TI diharapkan sudah terdefinisi dengan baik, kinerjanya dapat diukur secara kuantitatif, dan hasilnya dapat diprediksi. Sehingga terdapat kesenjangan (GAP) sebesar **2 level** yang perlu dijembatani melalui serangkaian perbaikan terstruktur.

Visualisasi hasil capability level dan GAP analysis dapat dilihat pada gambar berikut:

> **Gambar 2.2** Radar Chart Capability Level 5 Domain COBIT 2019

> **Gambar 2.3** GAP Analysis — As-is vs To-be per Domain

> **Gambar 2.4** Persentase Ketercapaian per Level per Domain

---

### Rekomendasi Perbaikan

Berdasarkan hasil analisis GAP, berikut adalah rekomendasi perbaikan untuk masing-masing domain:

#### 1. APO12 — Managed Risk

Untuk meningkatkan capability level dari Level 2 ke Level 4, PT. Murni Solusindo Nusantara perlu:

a. **Menuju Level 3 (Established):**
   - Menyusun dan mendokumentasikan kebijakan manajemen risiko TI secara formal dalam bentuk dokumen tertulis yang disahkan oleh manajemen
   - Membuat risk register yang komprehensif, mencakup seluruh risiko TI teridentifikasi beserta tingkat dampak dan probabilitasnya
   - Mensosialisasikan prosedur manajemen risiko kepada seluruh divisi terkait

b. **Menuju Level 4 (Predictable):**
   - Menetapkan indikator kinerja utama (KPI) untuk mengukur efektivitas manajemen risiko secara kuantitatif
   - Menetapkan jadwal evaluasi risiko secara berkala (minimal per kuartal) dengan format pelaporan yang terstandar
   - Menunjuk penanggung jawab (risk owner) untuk setiap risiko yang teridentifikasi dan memonitor perkembangannya secara kontinu

#### 2. APO13 — Managed Security

Untuk meningkatkan capability level dari Level 2 ke Level 4:

a. **Menuju Level 3 (Established):**
   - Menyusun prosedur standar keamanan informasi yang terdokumentasi dan disahkan oleh manajemen
   - Menyelenggarakan program pelatihan keamanan informasi secara rutin bagi seluruh karyawan (minimal 2 kali per tahun)
   - Menerapkan framework keamanan yang terintegrasi di seluruh platform digital perusahaan

b. **Menuju Level 4 (Predictable):**
   - Menerapkan metrik keamanan yang terukur untuk memonitor tingkat keamanan informasi secara kuantitatif
   - Melakukan penilaian kerentanan (vulnerability assessment) secara terjadwal pada seluruh platform digital
   - Mengimplementasikan sistem deteksi dan respons insiden keamanan secara otomatis

#### 3. BAI06 — Managed IT Changes

Untuk meningkatkan capability level dari Level 2 ke Level 4:

a. **Menuju Level 3 (Established):**
   - Menyusun SOP change management yang formal, mencakup alur persetujuan, pelaksanaan, dan evaluasi
   - Menerapkan proses persetujuan berjenjang (approval workflow) untuk setiap perubahan sistem TI
   - Membuat change log yang komprehensif dan terintegrasi dengan sistem manajemen proyek

b. **Menuju Level 4 (Predictable):**
   - Melaksanakan post-implementation review (PIR) secara konsisten untuk setiap perubahan yang dilakukan
   - Menetapkan metrik pengukuran keberhasilan perubahan yang terukur (misalnya: persentase perubahan yang berhasil, waktu penyelesaian perubahan)
   - Mengimplementasikan alat manajemen perubahan otomatis yang terintegrasi dengan sistem version control

#### 4. DSS01 — Managed Operations

Untuk meningkatkan capability level dari Level 2 ke Level 4:

a. **Menuju Level 3 (Established):**
   - Menyusun SOP operasional TI yang lengkap dan mendistribusikannya ke seluruh divisi yang relevan
   - Menstandarisasi prosedur penanganan insiden operasional dengan alur eskalasi yang jelas
   - Mengembangkan mekanisme feedback terstruktur dari pengguna internal dan eksternal

b. **Menuju Level 4 (Predictable):**
   - Menerapkan alat monitoring otomatis untuk memantau kinerja platform digital secara real-time
   - Menetapkan Service Level Agreement (SLA) internal untuk setiap layanan TI yang disediakan
   - Menetapkan dan memonitor KPI operasional TI secara berkala, seperti uptime platform, mean time to repair (MTTR), dan mean time between failures (MTBF)

#### 5. DSS05 — Managed Security Services

Untuk meningkatkan capability level dari Level 2 ke Level 4:

a. **Menuju Level 3 (Established):**
   - Menyusun prosedur standar pengelolaan layanan keamanan TI yang terdokumentasi secara formal
   - Menerapkan standar keamanan yang konsisten di seluruh platform digital perusahaan
   - Menjadwalkan audit keamanan internal secara periodik (minimal 2 kali per tahun)

b. **Menuju Level 4 (Predictable):**
   - Menerapkan sistem pelaporan insiden keamanan otomatis dengan ticketing system yang terstruktur
   - Menetapkan metrik keamanan yang terukur, seperti jumlah insiden keamanan per periode, waktu respons insiden, dan tingkat keberhasilan pemulihan
   - Melakukan penetration testing secara berkala untuk menguji ketahanan platform digital terhadap ancaman siber

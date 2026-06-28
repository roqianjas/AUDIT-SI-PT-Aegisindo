# BAB II — PEMBAHASAN

## A. Framework yang Digunakan

### COBIT 2019

Dalam pelaksanaan audit sistem informasi pada PT Aegisindo Mitra Sejati, kerangka kerja yang digunakan adalah **COBIT 2019** (Control Objectives for Information and Related Technologies). COBIT 2019 adalah kerangka kerja tata kelola dan manajemen teknologi informasi yang dikembangkan oleh ISACA (Information Systems Audit and Control Association) dan diperkenalkan pada tahun 2018 sebagai penyempurnaan dari COBIT 5 (Syuhada, 2021).

Pemilihan COBIT 2019 dilandasi beberapa pertimbangan. Pertama, kerangka ini merupakan versi paling mutakhir yang telah menyesuaikan diri dengan perkembangan teknologi serta mengintegrasikan berbagai standar internasional seperti ITIL, TOGAF, dan CMMI. Kedua, COBIT 2019 bersifat fleksibel melalui konsep *design factors*, sehingga penilaian tata kelola dapat difokuskan pada domain-domain yang benar-benar relevan dengan kondisi organisasi. Ketiga, model penilaian kapabilitasnya berbasis CMMI (Capability Maturity Model Integration) yang terstruktur, sehingga hasil penilaian dapat dipertanggungjawabkan dan dibandingkan dengan standar internasional (Algiffary dkk., 2023). Karakteristik PT Aegisindo Mitra Sejati sebagai perusahaan distribusi multi-saluran yang belum memiliki sistem informasi terpusat membuat fleksibilitas COBIT 2019 menjadi pertimbangan utama.

### Perbedaan COBIT 2019 dengan Versi Sebelumnya

COBIT 2019 memiliki sejumlah perbedaan mendasar dibandingkan COBIT 5, sebagaimana dirangkum pada tabel berikut:

| Aspek | COBIT 5 | COBIT 2019 |
|-------|---------|------------|
| Jumlah Proses | 37 proses | 40 proses (5 Governance + 35 Management) |
| Prinsip | 5 prinsip | 6 prinsip (sistem tata kelola dan kerangka tata kelola) |
| Capability Level | 0–5 | 0–5 (berbasis CMMI) |
| Fleksibilitas | Relatif tetap | Dapat disesuaikan melalui design factors |
| Integrasi Standar | Terbatas | Mengintegrasikan ITIL, TOGAF, dan CMMI |

Pemanfaatan COBIT versi terdahulu masih banyak dijumpai dalam penelitian audit, misalnya audit sistem informasi penjualan dengan COBIT 5 maupun audit sistem perkreditan dengan COBIT 4.0 (Zuraidah & Sulthon, 2022a, 2022b). Namun, pada audit ini COBIT 2019 dipilih karena keunggulannya dalam hal fleksibilitas dan integrasi standar internasional.

### 6 Prinsip COBIT 2019

COBIT 2019 dibangun di atas enam prinsip utama yang terbagi menjadi dua kelompok:

**Prinsip Sistem Tata Kelola:**
1. Memenuhi kebutuhan para pemangku kepentingan (*meeting stakeholder needs*)
2. Menggunakan pendekatan yang holistik (*holistic approach*)
3. Menerapkan sistem tata kelola yang dinamis (*dynamic governance system*)

**Prinsip Kerangka Tata Kelola:**
4. Memisahkan tata kelola dari manajemen (*governance distinct from management*)
5. Disesuaikan dengan kebutuhan organisasi (*tailored to enterprise needs*)
6. Mencakup organisasi secara menyeluruh (*end-to-end governance system*)

### Capability Level COBIT 2019

COBIT 2019 menilai kematangan proses menggunakan model kapabilitas dengan enam tingkatan (0–5) berbasis CMMI. Penilaian capability level bertujuan mengukur sejauh mana sebuah proses tata kelola TI telah dilaksanakan dan dikelola, sehingga organisasi dapat mengetahui posisi kematangannya dan menetapkan target perbaikan yang realistis (Sakron dkk., 2023):

| Level | Nama | Deskripsi |
|-------|------|-----------|
| **0** | Incomplete | Proses tidak dilaksanakan atau gagal mencapai tujuannya; belum ada kemampuan dasar |
| **1** | Performed | Proses dilaksanakan dan kurang lebih mencapai tujuannya, namun masih bersifat intuitif dan belum terorganisasi dengan baik |
| **2** | Managed | Proses dilaksanakan secara terkelola — direncanakan, dipantau, dan dilaporkan — melalui kegiatan dasar yang lengkap |
| **3** | Established | Proses telah terdefinisi dengan baik melalui prosedur standar dan kinerjanya diukur secara kualitatif |
| **4** | Predictable | Proses terdefinisi baik dan kinerjanya diukur secara kuantitatif sehingga hasilnya dapat diprediksi |
| **5** | Optimizing | Proses terus mengalami perbaikan berkelanjutan untuk mencapai tujuan organisasi |

### Rating Scale Ketercapaian

| Notasi | Deskripsi | Persentase Ketercapaian |
|--------|-----------|:-----------------------:|
| **N** | Not Achieved | 0–15% |
| **P** | Partially Achieved | >15%–50% |
| **L** | Largely Achieved | >50%–85% |
| **F** | Fully Achieved | >85%–100% |

---

## B. Domain dan Subdomain yang Digunakan

Berdasarkan analisis terhadap profil dan permasalahan PT Aegisindo Mitra Sejati, dipilih lima domain COBIT 2019 yang paling relevan. Pemilihan domain ini mempertimbangkan karakteristik perusahaan sebagai distributor alat keselamatan kerja yang menjalankan penjualan multi-saluran namun belum memiliki sistem informasi terintegrasi, sehingga fokus audit diarahkan pada pengelolaan data, aset, operasional, keberlangsungan, dan keamanan.

### 1. APO14 — Managed Data (Pengelolaan Data)

Domain APO14 berfokus pada pengelolaan data sebagai aset organisasi. Domain ini dipilih karena PT Aegisindo Mitra Sejati mengelola data inventori, pelanggan, dan penjualan yang tersebar di berbagai saluran (spreadsheet, WhatsApp, dan beberapa marketplace) tanpa integrasi terpusat. Pengelolaan data yang baik diperlukan agar informasi yang digunakan untuk pengambilan keputusan tetap akurat, konsisten, dan tidak terduplikasi.

Aspek yang dievaluasi dalam domain ini mencakup:
- Pencatatan dan pemutakhiran data inventori, pelanggan, dan penjualan
- Pemantauan kualitas dan konsistensi data antar saluran
- Prosedur standar, kepemilikan data, dan integrasi data tersentralisasi

### 2. BAI09 — Managed Assets (Pengelolaan Aset)

Domain BAI09 berfokus pada pengelolaan aset, dalam konteks ini terutama persediaan barang safety yang menjadi inti bisnis perusahaan. Domain ini dipilih untuk menilai sejauh mana perusahaan mengelola stok dan aset persediaannya, mengingat akurasi stok sangat menentukan kelancaran pemenuhan pesanan lintas saluran.

Aspek yang dievaluasi mencakup:
- Pencatatan persediaan dan arus barang masuk-keluar gudang
- Perencanaan persediaan dan pelaksanaan stock opname
- Integrasi catatan stok antar saluran dan dokumentasi siklus hidup aset

### 3. DSS01 — Managed Operations (Pengelolaan Operasional)

Domain DSS01 berfokus pada pengelolaan operasional harian. Sebagai perusahaan distribusi yang melayani pesanan dari banyak saluran setiap hari, kelancaran operasional menjadi tulang punggung bisnis PT Aegisindo Mitra Sejati. Domain ini dievaluasi untuk mengukur seberapa efektif perusahaan menjalankan dan mengendalikan aktivitas operasionalnya.

Aspek yang dievaluasi meliputi:
- Pemenuhan pesanan dan penanganan kendala operasional
- Perencanaan, penjadwalan, dan pemantauan kinerja operasional
- SOP operasional yang terdokumentasi dan mekanisme umpan balik pelanggan

### 4. DSS04 — Managed Continuity (Pengelolaan Keberlangsungan)

Domain DSS04 berfokus pada keberlangsungan layanan dan pemulihan ketika terjadi gangguan. Domain ini dipilih karena PT Aegisindo Mitra Sejati sangat bergantung pada saluran pihak ketiga (WhatsApp dan marketplace), sehingga gangguan pada salah satu saluran dapat berdampak langsung pada bisnis. Pencadangan data dan rencana pemulihan menjadi aspek penting yang perlu dinilai.

Aspek yang dievaluasi mencakup:
- Kesadaran risiko gangguan dan ketersediaan saluran alternatif
- Pencadangan (backup) data penting secara terjadwal
- Dokumen rencana keberlangsungan (BCP/DRP), uji coba pemulihan, dan target RTO/RPO

### 5. DSS05 — Managed Security Services (Pengelolaan Layanan Keamanan)

Domain DSS05 berfokus pada implementasi teknis layanan keamanan. Domain ini dipilih karena perusahaan menyimpan data pelanggan dan mengelola sejumlah akun penting (marketplace, email, keuangan) yang perlu dilindungi dari akses tidak sah maupun ancaman siber.

Aspek yang dievaluasi mencakup:
- Perlindungan perangkat dari malware dan pengelolaan kata sandi
- Pengaturan dan peninjauan hak akses pengguna
- Prosedur keamanan terdokumentasi dan pemeriksaan keamanan internal

### RACI Matrix

Dalam pelaksanaan audit ini disusun RACI Matrix untuk memetakan peran dan tanggung jawab setiap pihak yang terlibat dalam tiap aktivitas tata kelola TI:

| Aktivitas | Manajer Operasional | Procurement & Gudang | Penjualan Online | IT / Admin Sistem | Keuangan & Adm | Customer Service |
|-----------|:-------------------:|:--------------------:|:----------------:|:-----------------:|:--------------:|:----------------:|
| Pengelolaan Data (APO14) | **A** | R | R | R | C | I |
| Pengelolaan Aset/Stok (BAI09) | **A** | **R** | C | R | I | I |
| Operasional Harian (DSS01) | **A** | R | **R** | C | I | R |
| Keberlangsungan Bisnis (DSS04) | **A** | C | I | **R** | C | I |
| Layanan Keamanan (DSS05) | **A** | I | C | **R** | C | I |

Keterangan:
- **R** (Responsible) = Pihak yang melaksanakan tugas/pekerjaan
- **A** (Accountable) = Pihak yang bertanggung jawab atas keputusan dan memberikan arahan
- **C** (Consulted) = Pihak yang dimintai pendapat/masukan sebelum pengambilan keputusan
- **I** (Informed) = Pihak yang diberikan informasi mengenai pelaksanaan aktivitas

---

## C. Capability Level dan GAP

### Tahapan Audit Sistem Informasi

Perhitungan capability level dalam audit ini menggunakan metodologi COBIT 2019 dengan pendekatan kuesioner berskala Likert. Tahapan audit disusun sebagai pipeline mulai dari persiapan, pengumpulan data, analisis COBIT, hingga rekomendasi perbaikan. Pendekatan ini sejalan dengan praktik pengukuran tata kelola TI pada penelitian audit sebelumnya (Destriani & Putra, 2023) dan merupakan teknik pengumpulan data yang lazim digunakan untuk menilai kondisi pengendalian secara objektif (Swastika & Putra, 2016). Langkah-langkahnya adalah sebagai berikut:

1. Menyusun kuesioner dengan skala Likert 1–5 (STS=1, TS=2, R=3, S=4, SS=5) untuk setiap level kapabilitas pada masing-masing domain
2. Menyebarkan kuesioner kepada 6 responden internal PT Aegisindo Mitra Sejati yang dipilih berdasarkan keterlibatan langsung dalam proses TI (purposive sampling)
3. Menghitung total skor dan rata-rata (mean) untuk setiap pernyataan
4. Menghitung persentase ketercapaian: **% Ketercapaian = (Mean / Skor Maksimal) × 100%**
5. Menentukan rating berdasarkan persentase ketercapaian (N/P/L/F)
6. Menentukan capability level, yaitu level tertinggi yang mencapai rating L secara berurutan
7. Menghitung GAP antara capability level saat ini (as-is) dengan target (to-be)

Alur metodologi penelitian secara visual dapat dilihat pada Gambar 2.1.

> **Gambar 2.1** Tahapan Audit Sistem Informasi PT Aegisindo

### Hasil Perhitungan Capability Level

#### Domain APO14 — Managed Data

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.00 | **60.00%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.28 | **45.56%** | **P** (Partially Achieved) |
| Level 3 (Established) | 1.78 | **35.56%** | **P** (Partially Achieved) |

**Capability Level: 1 (Performed Process)**

Hasil perhitungan menunjukkan bahwa proses pengelolaan data di PT Aegisindo Mitra Sejati baru mencapai Level 1 (Performed Process). Hanya Level 1 yang memperoleh rating L (60.00%), sedangkan Level 2 sudah turun ke rating P (45.56%). Hal ini mengindikasikan bahwa meskipun data sudah dicatat dan digunakan, pengelolaannya belum direncanakan, dipantau, maupun terstandarisasi. Data masih tersebar antar saluran tanpa integrasi, sehingga APO14 menjadi salah satu domain terlemah.

#### Domain BAI09 — Managed Assets

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.39 | **67.78%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.67 | **53.33%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.17 | **43.33%** | **P** (Partially Achieved) |

**Capability Level: 2 (Managed Process)**

Proses pengelolaan aset/persediaan berada pada Level 2. Level 1 (67.78%) dan Level 2 (53.33%) sama-sama mencapai rating L, sedangkan Level 3 hanya P (43.33%). Pencatatan stok dan arus barang sudah berjalan baik karena merupakan inti bisnis distribusi, namun integrasi catatan stok antar saluran dan dokumentasi siklus hidup aset belum sepenuhnya terstandar.

#### Domain DSS01 — Managed Operations

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.50 | **70.00%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.83 | **56.67%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.33 | **46.67%** | **P** (Partially Achieved) |

**Capability Level: 2 (Managed Process)**

Domain DSS01 memperoleh skor Level 1 tertinggi di antara seluruh domain (70.00%), menunjukkan bahwa operasional harian merupakan kekuatan utama perusahaan. Level 1 dan Level 2 mencapai rating L, sementara Level 3 masih P (46.67%) karena SOP operasional belum terdokumentasi dan diterapkan secara konsisten. Mengingat operasional adalah tulang punggung bisnis, domain ini ditargetkan mencapai Level 4.

#### Domain DSS04 — Managed Continuity

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 2.89 | **57.78%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.17 | **43.33%** | **P** (Partially Achieved) |
| Level 3 (Established) | 1.67 | **33.33%** | **P** (Partially Achieved) |

**Capability Level: 1 (Performed Process)**

Proses pengelolaan keberlangsungan baru mencapai Level 1. Hanya Level 1 yang mencapai rating L (57.78%), sedangkan Level 2 sudah turun ke P (43.33%). Perusahaan menyadari risiko gangguan dan sudah melakukan backup sederhana, namun belum terjadwal, belum dipantau, dan belum didukung dokumen BCP/DRP formal. DSS04 menjadi domain terlemah bersama APO14, yang berisiko tinggi mengingat ketergantungan perusahaan pada saluran pihak ketiga.

#### Domain DSS05 — Managed Security Services

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.28 | **65.56%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.61 | **52.22%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.06 | **41.11%** | **P** (Partially Achieved) |

**Capability Level: 2 (Managed Process)**

Proses pengelolaan layanan keamanan berada pada Level 2. Level 1 (65.56%) dan Level 2 (52.22%) mencapai rating L, sedangkan Level 3 hanya P (41.11%). Pengamanan dasar seperti antivirus, pengaturan hak akses, dan perlindungan kata sandi sudah berjalan, namun belum didukung prosedur terdokumentasi, tinjauan hak akses berkala, maupun pemeriksaan keamanan internal.

---

### Ringkasan Capability Level dan GAP Analysis

| No | Domain | Capability Level (As-is) | Target Level (To-be) | GAP |
|----|--------|:------------------------:|:--------------------:|:---:|
| 1 | APO14 — Managed Data | **1** (Performed) | **3** (Established) | **2** |
| 2 | BAI09 — Managed Assets | **2** (Managed) | **3** (Established) | **1** |
| 3 | DSS01 — Managed Operations | **2** (Managed) | **4** (Predictable) | **2** |
| 4 | DSS04 — Managed Continuity | **1** (Performed) | **3** (Established) | **2** |
| 5 | DSS05 — Managed Security Services | **2** (Managed) | **3** (Established) | **1** |
| | **Rata-rata** | **1.6** | **3.2** | **1.6** |

Berdasarkan tabel di atas, kondisi tata kelola TI PT Aegisindo Mitra Sejati **tidak merata** antar domain. Dua domain (APO14 dan DSS04) masih berada pada **Capability Level 1 (Performed Process)**, sementara tiga domain lainnya (BAI09, DSS01, DSS05) telah mencapai **Level 2 (Managed Process)**. Pola ini mencerminkan karakteristik perusahaan distribusi yang kuat pada aktivitas fisik (pengelolaan stok dan operasional harian) namun lemah pada pengelolaan data digital dan keberlangsungan layanan.

Target (to-be) ditetapkan secara proporsional berdasarkan kekritisan domain: DSS01 sebagai tulang punggung operasional ditargetkan **Level 4 (Predictable)**, sedangkan empat domain lainnya ditargetkan **Level 3 (Established)** sebagai langkah perbaikan jangka menengah yang realistis. Dengan demikian, GAP yang dihasilkan bervariasi antara **1 hingga 2 level**, dengan rata-rata GAP sebesar **1.6 level**.

Visualisasi hasil capability level dan GAP analysis dapat dilihat pada gambar berikut:

> **Gambar 2.2** Profil Capability Proses TI PT Aegisindo

> **Gambar 2.3** Peta Kesenjangan As-is dan To-be per Domain

> **Gambar 2.4** Matriks Rating Ketercapaian Capability per Domain

---

### Rekomendasi Perbaikan

Berdasarkan hasil analisis GAP, berikut rekomendasi perbaikan untuk masing-masing domain. Mengingat APO14 dan DSS04 berada pada level terendah, kedua domain ini menjadi prioritas utama perbaikan.

#### 1. APO14 — Managed Data (Prioritas Utama)

a. **Menuju Level 2 (Managed):**
   - Menetapkan penanggung jawab data (data owner) untuk produk, stok, dan pelanggan
   - Menyusun perencanaan data: data apa yang dikelola, di mana disimpan, dan bagaimana diperbarui
   - Memantau konsistensi data antar saluran secara berkala untuk mencegah selisih dan duplikasi

b. **Menuju Level 3 (Established):**
   - Membangun satu sumber data terpusat (master data) sebagai acuan seluruh saluran penjualan
   - Menyusun prosedur standar pemutakhiran dan rekonsiliasi data secara terdokumentasi
   - Menerapkan klasifikasi data, khususnya pemisahan dan perlindungan data pribadi pelanggan

#### 2. BAI09 — Managed Assets

a. **Menuju Level 3 (Established):**
   - Mengintegrasikan catatan stok antara gudang, toko, dan seluruh marketplace
   - Menyusun prosedur standar pengelolaan persediaan (reorder point, minimum stok) yang terdokumentasi
   - Mendokumentasikan siklus hidup aset dari penerimaan hingga penghapusan
   - Menjadwalkan stock opname periodik dengan format pelaporan baku

#### 3. DSS01 — Managed Operations

a. **Menuju Level 3 (Established):**
   - Menyusun SOP operasional yang lengkap dan terdokumentasi untuk seluruh saluran penjualan
   - Menstandarkan penerapan SOP melalui pelatihan dan sosialisasi kepada seluruh staf
   - Membangun mekanisme umpan balik pelanggan yang terstruktur

b. **Menuju Level 4 (Predictable):**
   - Menetapkan indikator kinerja operasional yang terukur, seperti kecepatan proses order dan ketepatan pengiriman
   - Memantau indikator tersebut secara kuantitatif dan berkala sebagai dasar pengambilan keputusan
   - Menerapkan alat bantu pemantauan operasional untuk seluruh saluran

#### 4. DSS04 — Managed Continuity (Prioritas Utama)

a. **Menuju Level 2 (Managed):**
   - Menjadwalkan proses backup data penting secara rutin dan memantau keberhasilannya
   - Menetapkan saluran komunikasi cadangan resmi ketika saluran utama terganggu
   - Mengevaluasi kesiapan menghadapi gangguan secara berkala

b. **Menuju Level 3 (Established):**
   - Menyusun dokumen rencana keberlangsungan bisnis (BCP) dan pemulihan (DRP) secara formal
   - Melakukan uji coba prosedur pemulihan untuk memastikan dapat berjalan saat dibutuhkan
   - Menetapkan target waktu pemulihan (RTO) dan titik pemulihan data (RPO)

#### 5. DSS05 — Managed Security Services

a. **Menuju Level 3 (Established):**
   - Menyusun prosedur standar keamanan informasi (pengelolaan kata sandi dan hak akses) yang terdokumentasi
   - Melakukan tinjauan hak akses secara berkala, terutama saat ada perubahan status karyawan
   - Menjadwalkan pemeriksaan keamanan internal secara periodik
   - Menerapkan autentikasi dua faktor (2FA) pada akun marketplace dan email perusahaan yang kritis

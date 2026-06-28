# Perhitungan Capability Level
## PT Aegisindo Mitra Sejati — Framework COBIT 2019

---

## Metode Perhitungan

Berdasarkan framework COBIT 2019, perhitungan capability level dilakukan dengan langkah-langkah berikut:

1. **Hitung Total Skor** = Σ Jawaban seluruh responden untuk setiap pernyataan
2. **Hitung Mean** = Total Skor / Jumlah Responden (6 responden)
3. **Hitung % Ketercapaian** = (Mean / Skor Maksimal) × 100%
4. **Tentukan Rating** berdasarkan % ketercapaian:
   - **N** (Not Achieved) = 0–15%
   - **P** (Partially Achieved) = >15%–50%
   - **L** (Largely Achieved) = >50%–85%
   - **F** (Fully Achieved) = >85%–100%
5. **Tentukan Capability Level** = Level tertinggi yang mencapai rating **L** atau **F** secara berurutan
6. **Hitung GAP** = To-be Level – As-is Level

**Skor Maksimal per pertanyaan = 5** (skala tertinggi: Sangat Setuju)

> Catatan penetapan target (to-be): target capability level tidak diseragamkan, melainkan ditetapkan berdasarkan tingkat kekritisan domain terhadap kelangsungan bisnis. Domain yang menjadi tulang punggung pelayanan harian (DSS01) ditargetkan lebih tinggi (Level 4), sedangkan domain lain ditargetkan Level 3 sebagai langkah perbaikan yang realistis dalam jangka menengah.

---

## Perhitungan Per Domain

### Domain APO14 — Managed Data

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.00 | (3.00 / 5) × 100% = **60.00%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.28 | (2.28 / 5) × 100% = **45.56%** | **P** (Partially Achieved) |
| Level 3 (Established) | 1.78 | (1.78 / 5) × 100% = **35.56%** | **P** (Partially Achieved) |

**Capability Level APO14 = Level 1** (Performed Process)
> Hanya Level 1 yang mencapai rating L (Largely Achieved). Level 2 sudah turun ke rating P (45.56%), sehingga capability level tertinggi yang tercapai secara berurutan adalah **Level 1**. Ini menjadikan APO14 sebagai domain terlemah, mencerminkan pengelolaan data yang masih terfragmentasi antar saluran penjualan.

---

### Domain BAI09 — Managed Assets

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.39 | (3.39 / 5) × 100% = **67.78%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.67 | (2.67 / 5) × 100% = **53.33%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.17 | (2.17 / 5) × 100% = **43.33%** | **P** (Partially Achieved) |

**Capability Level BAI09 = Level 2** (Managed Process)
> Level 1 dan Level 2 mencapai rating L, namun Level 3 hanya P (43.33%). Capability level tertinggi = **Level 2**. Pengelolaan stok/aset fisik sudah berjalan cukup baik karena merupakan inti bisnis distribusi.

---

### Domain DSS01 — Managed Operations

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.50 | (3.50 / 5) × 100% = **70.00%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.83 | (2.83 / 5) × 100% = **56.67%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.33 | (2.33 / 5) × 100% = **46.67%** | **P** (Partially Achieved) |

**Capability Level DSS01 = Level 2** (Managed Process)
> Level 1 dan Level 2 mencapai rating L, namun Level 3 hanya P (46.67%). Capability level tertinggi = **Level 2**. DSS01 memperoleh skor Level 1 tertinggi (70.00%) di antara seluruh domain, menandakan operasional harian adalah kekuatan utama perusahaan.

---

### Domain DSS04 — Managed Continuity

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 2.89 | (2.89 / 5) × 100% = **57.78%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.17 | (2.17 / 5) × 100% = **43.33%** | **P** (Partially Achieved) |
| Level 3 (Established) | 1.67 | (1.67 / 5) × 100% = **33.33%** | **P** (Partially Achieved) |

**Capability Level DSS04 = Level 1** (Performed Process)
> Hanya Level 1 yang mencapai rating L (57.78%). Level 2 turun ke P (43.33%), sehingga capability level tertinggi = **Level 1**. DSS04 menjadi domain terlemah bersama APO14, mencerminkan keberlangsungan bisnis (backup, BCP/DRP) yang belum dikelola secara terencana.

---

### Domain DSS05 — Managed Security Services

| Level | Rata-rata Mean | % Ketercapaian | Rating |
|-------|:--------------:|:--------------:|:------:|
| Level 1 (Performed) | 3.28 | (3.28 / 5) × 100% = **65.56%** | **L** (Largely Achieved) |
| Level 2 (Managed) | 2.61 | (2.61 / 5) × 100% = **52.22%** | **L** (Largely Achieved) |
| Level 3 (Established) | 2.06 | (2.06 / 5) × 100% = **41.11%** | **P** (Partially Achieved) |

**Capability Level DSS05 = Level 2** (Managed Process)
> Level 1 dan Level 2 mencapai rating L, namun Level 3 hanya P (41.11%). Capability level tertinggi = **Level 2**. Pengamanan dasar (antivirus, hak akses, kata sandi) sudah berjalan, namun belum terdokumentasi dan ditinjau secara berkala.

---

## Ringkasan Capability Level

| No | Domain | Capability Level (As-is) | Target Level (To-be) | GAP |
|----|--------|:------------------------:|:--------------------:|:---:|
| 1 | APO14 (Managed Data) | **1** (Performed Process) | **3** (Established) | **2** |
| 2 | BAI09 (Managed Assets) | **2** (Managed Process) | **3** (Established) | **1** |
| 3 | DSS01 (Managed Operations) | **2** (Managed Process) | **4** (Predictable) | **2** |
| 4 | DSS04 (Managed Continuity) | **1** (Performed Process) | **3** (Established) | **2** |
| 5 | DSS05 (Managed Security Services) | **2** (Managed Process) | **3** (Established) | **1** |

**Rata-rata Capability Level (As-is) = (1 + 2 + 2 + 1 + 2) / 5 = 1.6**
**Rata-rata Target Level (To-be) = (3 + 3 + 4 + 3 + 3) / 5 = 3.2**
**Rata-rata GAP = 1.6**

---

## Analisis GAP

Hasil audit menunjukkan kondisi tata kelola TI yang **tidak merata** antar domain. Dua domain (APO14 dan DSS04) masih berada pada **Capability Level 1 (Performed Process)**, sementara tiga domain lainnya (BAI09, DSS01, DSS05) telah mencapai **Level 2 (Managed Process)**. Variasi ini mencerminkan karakteristik perusahaan distribusi yang kuat pada aktivitas fisik (stok, operasional) namun lemah pada aspek pengelolaan data digital dan keberlangsungan.

### Interpretasi Level

| Level | Nama | Interpretasi pada PT Aegisindo |
|-------|------|-------------------------------|
| Level 1 (Performed) | Performed Process | Aktivitas dilakukan dan tujuannya kurang lebih tercapai, namun masih bersifat intuitif, bergantung pada individu, belum direncanakan dan dipantau |
| Level 2 (Managed) | Managed Process | Proses sudah direncanakan, dipantau, dan dilaporkan; kegiatan dasar lengkap, namun belum terstandarisasi formal |
| Level 3 (Established) | Established Process | Proses terdefinisi baik melalui prosedur standar dan diterapkan konsisten di seluruh organisasi |
| Level 4 (Predictable) | Predictable Process | Proses diukur secara kuantitatif sehingga kinerjanya dapat diprediksi |

### Analisis Per Domain

**APO14 — Managed Data (As-is Level 1, GAP 2)**
- Data inventori, pelanggan, dan penjualan sudah dicatat, namun tersebar di spreadsheet, WhatsApp, dan masing-masing marketplace tanpa integrasi
- Belum ada perencanaan pengelolaan data maupun penanggung jawab data yang jelas, sehingga konsistensi antar saluran tidak terpantau
- Belum terdapat prosedur standar, kebijakan kepemilikan data, maupun integrasi tersentralisasi

**BAI09 — Managed Assets (As-is Level 2, GAP 1)**
- Pencatatan stok dan barang masuk/keluar gudang sudah berjalan baik karena merupakan inti bisnis distribusi
- Perencanaan persediaan dan stock opname sudah dilakukan meskipun belum sepenuhnya terstruktur
- Yang belum tercapai: integrasi catatan stok antar gudang–toko–marketplace dan dokumentasi siklus hidup aset

**DSS01 — Managed Operations (As-is Level 2, GAP 2)**
- Pemenuhan pesanan lintas saluran berjalan rutin dan menjadi domain dengan skor tertinggi (Level 1 = 70.00%)
- Perencanaan dan pemantauan kinerja operasional sudah dilakukan secara berkala
- Yang belum tercapai: SOP operasional terdokumentasi yang diterapkan konsisten dan mekanisme umpan balik pelanggan yang terstruktur. Karena operasional adalah tulang punggung bisnis, target ditetapkan lebih tinggi (Level 4)

**DSS04 — Managed Continuity (As-is Level 1, GAP 2)**
- Perusahaan menyadari risiko gangguan saluran dan sudah melakukan backup data secara sederhana
- Namun backup belum terjadwal dan dipantau, serta belum ada perencanaan keberlangsungan yang terstruktur
- Belum terdapat dokumen BCP/DRP formal, uji coba pemulihan, maupun penetapan target RTO/RPO

**DSS05 — Managed Security Services (As-is Level 2, GAP 1)**
- Pengamanan dasar seperti antivirus, pengaturan hak akses, dan perlindungan kata sandi sudah diterapkan
- Pemantauan akses dan evaluasi pengamanan sudah dilakukan meskipun belum konsisten
- Yang belum tercapai: prosedur keamanan terdokumentasi, tinjauan hak akses berkala, dan pemeriksaan keamanan internal

---

## Rekomendasi Perbaikan

### APO14 — Managed Data (prioritas utama)
1. Menetapkan penanggung jawab data (data owner) dan menyusun kebijakan pengelolaan data secara formal
2. Membangun satu sumber data terpusat (master data) untuk produk, stok, dan pelanggan yang menjadi acuan seluruh saluran
3. Menyusun prosedur standar pemutakhiran dan rekonsiliasi data antar marketplace, WhatsApp, dan toko
4. Menerapkan klasifikasi data, khususnya pemisahan data pelanggan yang bersifat pribadi

### BAI09 — Managed Assets
1. Mengintegrasikan catatan stok antara gudang, toko, dan seluruh marketplace agar tidak terjadi selisih
2. Menyusun prosedur standar pengelolaan persediaan (reorder point, minimum stok) secara terdokumentasi
3. Mendokumentasikan siklus hidup aset dari penerimaan hingga penghapusan
4. Menjadwalkan stock opname secara periodik dengan format pelaporan yang baku

### DSS01 — Managed Operations
1. Menyusun SOP operasional yang lengkap dan terdokumentasi untuk seluruh saluran penjualan
2. Menstandarkan penerapan SOP di seluruh staf melalui pelatihan dan sosialisasi
3. Membangun mekanisme umpan balik pelanggan yang terstruktur (formulir, rating, atau survei)
4. Menetapkan dan memantau indikator kinerja operasional (kecepatan proses order, ketepatan pengiriman) untuk menuju Level 4

### DSS04 — Managed Continuity (prioritas utama)
1. Menyusun rencana keberlangsungan bisnis (BCP) dan pemulihan (DRP) secara terdokumentasi
2. Menjadwalkan dan memantau proses backup data penting secara rutin dan otomatis
3. Menetapkan saluran komunikasi cadangan resmi ketika saluran utama (WhatsApp/marketplace) terganggu
4. Menetapkan target waktu pemulihan (RTO) dan titik pemulihan data (RPO) yang disepakati manajemen

### DSS05 — Managed Security Services
1. Menyusun prosedur standar keamanan informasi (pengelolaan kata sandi, hak akses) yang terdokumentasi
2. Melakukan tinjauan hak akses secara berkala, terutama saat ada perubahan status karyawan
3. Menjadwalkan pemeriksaan keamanan internal secara periodik
4. Menerapkan autentikasi dua faktor (2FA) pada akun marketplace dan email perusahaan yang kritis

---

*Perhitungan ini dilakukan berdasarkan data kuesioner dari 6 responden internal PT Aegisindo Mitra Sejati menggunakan metodologi COBIT 2019 dengan rating scale N/P/L/F.*

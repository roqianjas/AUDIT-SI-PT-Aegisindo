# Rencana Implementasi — Project Audit Sistem Informasi (453)
## PT Aegisindo Mitra Sejati | Status: ✅ SELESAI (100%)

---

## Gambaran Umum

Project akhir mata kuliah Audit Sistem Informasi berupa audit tata kelola TI pada PT Aegisindo Mitra Sejati menggunakan framework COBIT 2019, lengkap dengan laporan, data perhitungan, visualisasi, dan presentasi.

### Keputusan yang Ditetapkan

| Aspek | Keputusan |
|-------|-----------|
| **Framework** | COBIT 2019 |
| **Perusahaan Audit** | PT Aegisindo Mitra Sejati (distributor alat safety/K3) |
| **Kelompok** | 3 orang: Dinda Callista (11250083), Alim Fatun Rofiah (11250127), dan Nur Fikri (11250138) |
| **Format Output** | Markdown → konversi DOCX/XLSX via Python; presentasi HTML (reveal-style) |
| **Bahasa Laporan** | Bahasa Indonesia akademis |
| **Sitasi Jurnal** | 2022–2026 |
| **Sitasi Buku** | 2016–2026 (+ ISACA 2018 sebagai sumber primer) |
| **Responden** | 6 responden (purposive sampling berbasis RACI Matrix) |

---

## Profil Perusahaan Audit

**PT Aegisindo Mitra Sejati** — Distributor dan general supplier alat keselamatan kerja (K3) di Cikarang, Bekasi.
**Saluran:** Toko fisik, sales lapangan, marketplace (Tokopedia, Lazada, Ralali, Indotrading), WhatsApp Business.
**Karakteristik kunci:** Penjualan multi-saluran namun belum memiliki sistem informasi terintegrasi (website Google Sites, CRM informal via WhatsApp, inventori semi-manual).

### Domain COBIT 2019 yang Dipilih

| Domain | Nama | Capability Level (As-is) | Target (To-be) | GAP |
|--------|------|:------------------------:|:--------------:|:---:|
| **APO14** | Managed Data | Level 1 | Level 3 | 2 |
| **BAI09** | Managed Assets | Level 2 | Level 3 | 1 |
| **DSS01** | Managed Operations | Level 2 | Level 4 | 2 |
| **DSS04** | Managed Continuity | Level 1 | Level 3 | 2 |
| **DSS05** | Managed Security Services | Level 2 | Level 3 | 1 |

> Rata-rata capability level 1.6 (as-is) → 3.2 (to-be), rata-rata GAP 1.6.

---

## Struktur Folder (Final)

```
TUGAS-4-PROJECT-AUDIT-SI/
├── 01_Planning/
│   ├── Rencana_Project.md
│   ├── implementation_plan.md
│   └── task.md
├── 02_Laporan/
│   ├── Halaman_Depan/
│   │   └── Cover_dan_Daftar_Isi.md
│   ├── BAB-I_Pendahuluan.md
│   ├── BAB-II_Pembahasan.md
│   ├── BAB-III_Penutup.md
│   ├── Daftar_Pustaka.md
│   ├── convert_to_docx.py
│   └── Kelompok-Laporan-Audit-SI-PT_Aegisindo_Mitra_Sejati.docx
├── 03_Data/
│   ├── Kuesioner.md
│   ├── Tabulasi_Data.md
│   ├── Perhitungan_Capability_Level.md
│   ├── generate_master_excel.py
│   ├── generate_charts.py
│   ├── generate_form_kuesioner.py
│   ├── Master_Data_Audit_SI.xlsx
│   ├── Form_Kuesioner_Audit_SI.docx
│   └── charts/
│       ├── gambar_1_radar_capability.png  # profil capability horizontal
│       ├── gambar_2_gap_analysis.png      # peta GAP dumbbell
│       ├── gambar_3_ketercapaian.png      # heatmap rating capability
│       ├── gambar_4_metodologi.png        # pipeline/swimlane audit
│       └── gambar_5_struktur_organisasi.png # peta fungsi organisasi
├── 04_Referensi/
│   └── Daftar_Jurnal.md
└── 05_Presentasi/
    ├── index.html
    ├── themes.css
    ├── PANDUAN_PRESENTASI.md
    └── slides.pdf
```

---

## Script Otomasi

| Script | Lokasi | Fungsi | Output |
|--------|--------|--------|--------|
| `generate_charts.py` | `03_Data/` | Generate 5 grafik audit dashboard industrial yang berbeda dari referensi | 5 file PNG |
| `generate_master_excel.py` | `03_Data/` | Generate Excel master data (perhitungan dinamis) | `.xlsx` (8 sheet) |
| `generate_form_kuesioner.py` | `03_Data/` | Generate form kuesioner kosong | `.docx` |
| `generate_form_terisi.py` | `03_Data/` | Generate 6 form kuesioner terisi (jawaban centang) per responden | `6 .docx` di `form_responden/` |
| `convert_to_docx.py` | `02_Laporan/` | Konversi MD → DOCX akademis + embed gambar | `.docx` |

> Catatan teknis: `generate_master_excel.py` menghitung mean, persentase, rating, capability level, dan GAP **secara dinamis** dari data jawaban responden (single source of truth), sehingga konsisten dengan tabulasi laporan.

---

## Verification — Sudah Diverifikasi

- ✅ Semua 4 script berjalan tanpa error
- ✅ DOCX laporan ter-generate dengan 5 gambar embedded (690 KB, 50 tabel, 7 section)
- ✅ Excel master data 8 sheet lengkap, capability level cocok dengan laporan
- ✅ Hasil hitung Excel = APO14 L1, BAI09 L2, DSS01 L2, DSS04 L1, DSS05 L2 (sesuai laporan)
- ✅ Form kuesioner 45 pertanyaan (9 × 5 domain)
- ✅ Pagination DOCX: Cover (hidden), front matter (romawi), BAB (arabic)
- ✅ Tidak ada teks sisa dari template referensi
- ✅ 6 responden konsisten di semua file

---

*Last updated: Mei 2026 — Project selesai 100% dan siap dikumpulkan.*

# Rencana Implementasi — Pengerjaan Tugas Audit Sistem Informasi (453)
## Status: ✅ SEMUA TUGAS SELESAI (100%)

---

## Gambaran Umum

Mata kuliah Audit Sistem Informasi memiliki **4 tugas utama + UTS** yang telah selesai dikerjakan seluruhnya.

### Keputusan yang Ditetapkan

| Aspek | Keputusan |
|-------|-----------|
| **Framework** | COBIT 2019 |
| **Perusahaan Audit** | PT. Murni Solusindo Nusantara |
| **Kelompok** | 2 orang: Roki Anjas (11250066) & Susanto (11250068) |
| **Format Output** | Markdown → konversi DOCX/XLSX via Python; presentasi reveal.js |
| **Bahasa Laporan** | Bahasa Indonesia akademis |
| **Sitasi Jurnal** | 2022–2026 |
| **Sitasi Buku** | 2016–2026 |
| **Responden** | 8 responden (purposive sampling berbasis RACI Matrix) |

---

## Profil Perusahaan Audit

**PT. Murni Solusindo Nusantara** — Distributor alat hitung uang dan alat deteksi uang palsu.
**Produk Digital:** Platform Web Builder SaaS, Listing Property, Indoconnex
**Departemen:** HR, Finance, IT, Digital Marketing
**Sub-divisi Digital Marketing:** Web Dev & SEO, UI/UX, Graphic Design, Video Editor, Copywriter, Email Marketing
**Posisi Roki:** Digital Marketing → Web Development & SEO

### Domain COBIT 2019 yang Dipilih

| Domain | Nama | Capability Level (As-is) | Target (To-be) | GAP |
|--------|------|:------------------------:|:--------------:|:---:|
| **APO12** | Managed Risk | Level 2 | Level 4 | 2 |
| **APO13** | Managed Security | Level 2 | Level 4 | 2 |
| **BAI06** | Managed IT Changes | Level 2 | Level 4 | 2 |
| **DSS01** | Managed Operations | Level 2 | Level 4 | 2 |
| **DSS05** | Managed Security Services | Level 2 | Level 4 | 2 |

---

## Status Akhir Semua Tugas

| # | Tugas | Bobot | Status | Deliverables |
|---|-------|:-----:|:------:|:-------------|
| 4 | Project Akhir — Laporan + Presentasi | **30%** ⭐ | ✅ Done | DOCX, PDF, reveal.js (19 slide), XLSX, 5 PNG |
| 3 | Quiz Pra-UTS — Bank Soal P1–P7 | **25%** | ✅ Done | 55 soal + jawaban |
| 2 | Studi Kasus Makalah COBIT 4/5/2019 | 2.5% | ✅ Done | 3 MD + DOCX |
| 1 | Forum Diskusi P1–P7 | 2.5% | ✅ Done | 7 file MD |
| — | UTS | 25% | ✅ Done | Online |

---

## Struktur Folder (Final)

```
453-JSR-AUDIT SISTEM INFORMASI/
├── DOK1_Ringkasan_Materi_Audit_SI.md
├── DOK2_Ringkasan_RPS_Audit_SI.md
├── DOK3_Panduan_Tugas_RTM_Audit_SI.md
├── Materi/
│
├── TUGAS-4-PROJECT-AUDIT-SI/                   ✅ 30%
│   ├── 01_Planning/
│   │   ├── Rencana_Project.md
│   │   ├── implementation_plan.md
│   │   └── task.md
│   ├── 02_Laporan/
│   │   ├── Halaman_Depan/
│   │   │   └── Cover_dan_Daftar_Isi.md
│   │   ├── BAB-I_Pendahuluan.md
│   │   ├── BAB-II_Pembahasan.md
│   │   ├── BAB-III_Penutup.md
│   │   ├── Daftar_Pustaka.md
│   │   ├── convert_to_docx.py
│   │   └── Kelompok-Laporan-Audit-SI-PT_Murni_Solusindo_Nusantara.docx
│   ├── 03_Data/
│   │   ├── Kuesioner.md
│   │   ├── Tabulasi_Data.md
│   │   ├── Perhitungan_Capability_Level.md
│   │   ├── generate_master_excel.py
│   │   ├── generate_charts.py
│   │   ├── generate_form_kuesioner.py
│   │   ├── Master_Data_Audit_SI.xlsx
│   │   ├── Form_Kuesioner_Audit_SI.docx
│   │   └── charts/
│   │       ├── gambar_1_radar_capability.png
│   │       ├── gambar_2_gap_analysis.png
│   │       ├── gambar_3_ketercapaian.png
│   │       ├── gambar_4_metodologi.png
│   │       └── gambar_5_struktur_organisasi.png
│   ├── 04_Referensi/
│       └── Daftar_Jurnal.md
│   (Presentasi: lihat presentations/453-audit-si/ — reveal.js 19 slide)
│
├── TUGAS-3-PERSIAPAN-QUIZ/                     ✅ 25%
│   └── Bank_Soal_Latihan_P1_P7.md
│
├── TUGAS-2-STUDI-KASUS/                        ✅ 2.5%
│   ├── Studi_Kasus_COBIT4.md
│   ├── Studi_Kasus_COBIT5.md
│   ├── Studi_Kasus_COBIT2019.md
│   ├── convert_to_docx.py
│   └── Tugas2-Studi_Kasus_COBIT-Roki_Anjas.docx
│
└── TUGAS-1-FORUM-DISKUSI/                      ✅ 2.5%
    ├── Diskusi_P1_Pengantar_Audit_SI.md
    ├── Diskusi_P2_Tata_Kelola_TI.md
    ├── Diskusi_P3_Framework_COBIT.md
    ├── Diskusi_P4_Implementasi_COBIT4.md
    ├── Diskusi_P5_Implementasi_COBIT5.md
    ├── Diskusi_P6_Implementasi_COBIT2019.md
    └── Diskusi_P7_Review_Sintesis.md
```

---

## Script Otomasi

| Script | Lokasi | Fungsi | Output |
|--------|--------|--------|--------|
| `generate_charts.py` | `03_Data/` | Generate 5 grafik profesional | 5 file PNG |
| `generate_master_excel.py` | `03_Data/` | Generate Excel master data | `.xlsx` (8 sheet) |
| `generate_form_kuesioner.py` | `03_Data/` | Generate form kuesioner | `.docx` |
| `convert_to_docx.py` | `02_Laporan/` | Konversi MD → DOCX akademis + embed gambar | `.docx` |

---

## Verification — Sudah Diverifikasi

- ✅ Semua 5 script berjalan tanpa error
- ✅ DOCX laporan ter-generate dengan 5 gambar embedded
- ✅ Presentasi reveal.js 19 slide (di `presentations/453-audit-si/`)
- ✅ Excel master data 8 sheet lengkap
- ✅ Daftar Gambar & Daftar Tabel ada di halaman depan
- ✅ 8 responden konsisten di semua file
- ✅ Forum diskusi 7/7 lengkap (P1-P7)
- ✅ Studi kasus 3/3 lengkap (COBIT 4, 5, 2019)
- ✅ Bank soal 55 soal + jawaban + penjelasan

---

*Last updated: Mei 2026 — Semua tugas selesai 100% dan siap dikumpulkan.*

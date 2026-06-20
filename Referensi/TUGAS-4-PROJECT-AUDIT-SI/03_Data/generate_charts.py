"""
Generate 4 Grafik Profesional untuk Laporan Audit SI
PT. Murni Solusindo Nusantara — COBIT 2019
Output: PNG files di folder 03_Data/charts/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# === PATHS ===
BASE = os.path.dirname(os.path.abspath(__file__))
CHARTS_DIR = os.path.join(BASE, 'charts')
os.makedirs(CHARTS_DIR, exist_ok=True)

# === STYLE ===
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'Liberation Serif', 'Nimbus Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['figure.facecolor'] = 'white'

# === COLORS ===
C_NAVY = '#1B3A5C'
C_BLUE = '#0096D6'
C_TEAL = '#00BC8C'
C_ORANGE = '#FF8C00'
C_RED = '#E53935'
C_GOLD = '#C6932C'
C_LIGHT = '#E8F4FD'
C_GRAY = '#666666'

# === DATA ===
domains = ['APO12', 'APO13', 'BAI06', 'DSS01', 'DSS05']
domain_names = [
    'Managed\nRisk',
    'Managed\nSecurity',
    'Managed\nIT Changes',
    'Managed\nOperations',
    'Managed\nSec. Services'
]
domain_full = [
    'Managed Risk',
    'Managed Security',
    'Managed IT Changes',
    'Managed Operations',
    'Managed Security Services'
]

# Capability data (8 respondents)
l1_pct = [60.83, 65.00, 62.50, 66.67, 67.50]
l2_pct = [51.67, 54.17, 53.33, 55.83, 51.67]
l3_pct = [45.00, 46.67, 46.67, 48.33, 45.00]
cap_level = [2, 2, 2, 2, 2]
target_level = [4, 4, 4, 4, 4]


# ============================================================
# GAMBAR 1: RADAR/SPIDER CHART — Capability Level
# ============================================================
def chart_radar():
    fig, ax = plt.subplots(figsize=(7, 6), subplot_kw=dict(polar=True))

    categories = domains
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    # Data
    as_is = cap_level + cap_level[:1]
    to_be = target_level + target_level[:1]
    max_level = [5] * (N + 1)

    # Plot
    ax.plot(angles, as_is, 'o-', color=C_BLUE, linewidth=2.5, markersize=8, label='As-is (Level Saat Ini)', zorder=3)
    ax.fill(angles, as_is, alpha=0.15, color=C_BLUE)

    ax.plot(angles, to_be, 's--', color=C_TEAL, linewidth=2.5, markersize=8, label='To-be (Level Target)', zorder=3)
    ax.fill(angles, to_be, alpha=0.1, color=C_TEAL)

    # Styling
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([f'{d}\n{n}' for d, n in zip(domains, domain_names)], fontsize=9, fontweight='bold')
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8, color=C_GRAY)
    ax.yaxis.grid(True, color='#CCCCCC', linestyle='--', linewidth=0.5)
    ax.xaxis.grid(True, color='#CCCCCC', linestyle='-', linewidth=0.5)

    # Add level values
    for i, (angle, val) in enumerate(zip(angles[:-1], cap_level)):
        ax.annotate(f'Level {val}', xy=(angle, val), xytext=(10, 10),
                    textcoords='offset points', fontsize=9, fontweight='bold',
                    color=C_BLUE, ha='center')

    ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.12), fontsize=10,
              frameon=True, fancybox=True, shadow=True)

    plt.title('Radar Chart Capability Level\n5 Domain COBIT 2019', pad=25, fontsize=14, fontweight='bold', color=C_NAVY)
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'gambar_1_radar_capability.png')
    plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ Gambar 1 — Radar Chart: {path}")
    return path


# ============================================================
# GAMBAR 2: BAR CHART — GAP Analysis (As-is vs To-be)
# ============================================================
def chart_gap():
    fig, ax = plt.subplots(figsize=(8, 5))

    x = np.arange(len(domains))
    width = 0.35

    bars1 = ax.bar(x - width/2, cap_level, width, label='As-is (Saat Ini)',
                   color=C_BLUE, edgecolor='white', linewidth=1, zorder=3)
    bars2 = ax.bar(x + width/2, target_level, width, label='To-be (Target)',
                   color=C_TEAL, edgecolor='white', linewidth=1, zorder=3)

    # Value labels
    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'Level {int(bar.get_height())}', ha='center', va='bottom',
                fontsize=10, fontweight='bold', color=C_BLUE)

    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'Level {int(bar.get_height())}', ha='center', va='bottom',
                fontsize=10, fontweight='bold', color=C_TEAL)

    # GAP annotations
    for i in range(len(domains)):
        gap = target_level[i] - cap_level[i]
        mid_y = (cap_level[i] + target_level[i]) / 2
        ax.annotate(f'GAP = {gap}', xy=(i + width/2 + 0.05, mid_y),
                    xytext=(i + 0.55, mid_y),
                    fontsize=9, fontweight='bold', color=C_RED,
                    arrowprops=dict(arrowstyle='->', color=C_RED, lw=1.5),
                    ha='left', va='center',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFEBEE', edgecolor=C_RED, alpha=0.8))

    ax.set_xlabel('Domain COBIT 2019', fontsize=11, fontweight='bold', color=C_NAVY)
    ax.set_ylabel('Capability Level', fontsize=11, fontweight='bold', color=C_NAVY)
    ax.set_title('GAP Analysis — As-is vs To-be\nCapability Level per Domain', fontsize=14, fontweight='bold', color=C_NAVY)
    ax.set_xticks(x)
    ax.set_xticklabels([f'{d}\n{n}' for d, n in zip(domains, domain_full)], fontsize=8)
    ax.set_ylim(0, 5.5)
    ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.yaxis.grid(True, color='#EEEEEE', linestyle='--', linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend(loc='upper left', fontsize=10, frameon=True, fancybox=True)

    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'gambar_2_gap_analysis.png')
    plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ Gambar 2 — GAP Analysis: {path}")
    return path


# ============================================================
# GAMBAR 3: GROUPED BAR — % Ketercapaian per Level per Domain
# ============================================================
def chart_ketercapaian():
    fig, ax = plt.subplots(figsize=(9, 5.5))

    x = np.arange(len(domains))
    width = 0.25

    bars1 = ax.bar(x - width, l1_pct, width, label='Level 1 (Performed)',
                   color=C_BLUE, edgecolor='white', linewidth=1, zorder=3)
    bars2 = ax.bar(x, l2_pct, width, label='Level 2 (Managed)',
                   color=C_TEAL, edgecolor='white', linewidth=1, zorder=3)
    bars3 = ax.bar(x + width, l3_pct, width, label='Level 3 (Established)',
                   color=C_ORANGE, edgecolor='white', linewidth=1, zorder=3)

    # Value labels
    for bars, color in [(bars1, C_NAVY), (bars2, C_NAVY), (bars3, C_NAVY)]:
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{bar.get_height():.1f}%', ha='center', va='bottom',
                    fontsize=8, fontweight='bold', color=color)

    # Threshold line at 50%
    ax.axhline(y=50, color=C_RED, linestyle='--', linewidth=1.5, alpha=0.7, zorder=2)
    ax.text(len(domains) - 0.5, 51.5, 'Batas L (>50%)', fontsize=9,
            color=C_RED, fontweight='bold', ha='right')

    # Rating annotations
    for i in range(len(domains)):
        # L1 = L
        ax.text(x[i] - width, l1_pct[i] - 5, 'L', ha='center', fontsize=8,
                fontweight='bold', color='white')
        # L2 = L
        ax.text(x[i], l2_pct[i] - 5, 'L', ha='center', fontsize=8,
                fontweight='bold', color='white')
        # L3 = P
        ax.text(x[i] + width, l3_pct[i] - 5, 'P', ha='center', fontsize=8,
                fontweight='bold', color='white')

    ax.set_xlabel('Domain COBIT 2019', fontsize=11, fontweight='bold', color=C_NAVY)
    ax.set_ylabel('Persentase Ketercapaian (%)', fontsize=11, fontweight='bold', color=C_NAVY)
    ax.set_title('Persentase Ketercapaian per Level\nSetiap Domain COBIT 2019', fontsize=14, fontweight='bold', color=C_NAVY)
    ax.set_xticks(x)
    ax.set_xticklabels([f'{d}\n{n}' for d, n in zip(domains, domain_full)], fontsize=8)
    ax.set_ylim(0, 85)
    ax.yaxis.grid(True, color='#EEEEEE', linestyle='--', linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend(loc='upper right', fontsize=9, frameon=True, fancybox=True)

    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'gambar_3_ketercapaian.png')
    plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ Gambar 3 — % Ketercapaian: {path}")
    return path


# ============================================================
# GAMBAR 4: FLOWCHART — Alur Metodologi Penelitian
# ============================================================
def chart_metodologi():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    steps = [
        ('Studi Literatur\n& Analisis\nPermasalahan', C_NAVY),
        ('Penentuan\nDomain\nCOBIT 2019', C_BLUE),
        ('Penyusunan\nKuesioner\n(Skala Likert 1-5)', C_TEAL),
        ('Pengumpulan\nData\n(8 Responden)', '#2E7D32'),
        ('Perhitungan\nCapability Level\n& Rating N/P/L/F', C_ORANGE),
        ('Analisis GAP\n(As-is vs To-be)', C_RED),
        ('Rekomendasi\nPerbaikan', C_GOLD),
    ]

    box_w = 2.4
    box_h = 1.1
    gap = 0.5
    pitch = box_w + gap          # jarak antar titik awal box
    start_x = 0.6
    y_top = 6.8
    y_bot = 4.2

    # Title
    ax.text(6, 9.5, 'Alur Metodologi Penelitian', fontsize=16, fontweight='bold',
            color=C_NAVY, ha='center', va='center')
    ax.text(6, 9.0, 'Framework COBIT 2019', fontsize=12, color=C_GRAY,
            ha='center', va='center')

    def draw_box(x, y, text, color, num):
        rect = FancyBboxPatch((x, y - box_h/2), box_w, box_h,
                              boxstyle="round,pad=0.12",
                              facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.text(x + 0.28, y + box_h/2 - 0.18, str(num),
                fontsize=9, fontweight='bold', color=color,
                ha='center', va='center',
                bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color))
        ax.text(x + box_w/2, y - 0.05, text, fontsize=8, fontweight='bold',
                color='white', ha='center', va='center', linespacing=1.3)

    # Row 1: Steps 1-4 (kiri -> kanan)
    x_left = {}
    x_right = {}
    for i in range(4):
        x = start_x + i * pitch
        draw_box(x, y_top, steps[i][0], steps[i][1], i + 1)
        x_left[i] = x
        x_right[i] = x + box_w

    # Arrows Row 1 (kiri -> kanan): 1->2->3->4
    for i in range(3):
        ax.annotate('', xy=(x_left[i+1], y_top), xytext=(x_right[i], y_top),
                    arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=2.5))

    # Row 2: Steps 5-7 ditempatkan sejajar kolom 4,3,2 (kanan -> kiri)
    col_for_step = {4: 3, 5: 2, 6: 1}   # step idx -> kolom
    xpos = {}
    for idx in (4, 5, 6):
        col = col_for_step[idx]
        x = start_x + col * pitch
        draw_box(x, y_bot, steps[idx][0], steps[idx][1], idx + 1)
        xpos[idx] = x

    # Arrow turun dari step 4 (kolom 3) ke step 5 (kolom 3)
    cx = start_x + 3 * pitch + box_w/2
    ax.annotate('', xy=(cx, y_bot + box_h/2), xytext=(cx, y_top - box_h/2),
                arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=2.5))

    # Arrows Row 2 (kanan -> kiri): 5->6->7
    # 5 (kolom3) -> 6 (kolom2)
    ax.annotate('', xy=(xpos[5] + box_w, y_bot), xytext=(xpos[4], y_bot),
                arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=2.5))
    # 6 (kolom2) -> 7 (kolom1)
    ax.annotate('', xy=(xpos[6] + box_w, y_bot), xytext=(xpos[5], y_bot),
                arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=2.5))

    # Output box at bottom (di bawah step 7 / kolom 1)
    output_x = start_x + 1 * pitch - 0.3
    output_y = 1.7
    out_w = 5.2
    rect = FancyBboxPatch((output_x, output_y - 0.5), out_w, 1.0,
                          boxstyle="round,pad=0.2",
                          facecolor=C_LIGHT, edgecolor=C_NAVY, linewidth=2)
    ax.add_patch(rect)
    ax.text(output_x + out_w/2, output_y + 0.18, 'OUTPUT', fontsize=12,
            fontweight='bold', color=C_NAVY, ha='center', va='center')
    ax.text(output_x + out_w/2, output_y - 0.2, 'Laporan Audit SI dengan Capability Level & Rekomendasi',
            fontsize=9, color=C_GRAY, ha='center', va='center')

    # Arrow turun dari step 7 (kolom 1) ke output box
    cx7 = xpos[6] + box_w/2
    ax.annotate('', xy=(cx7, output_y + 0.5), xytext=(cx7, y_bot - box_h/2),
                arrowprops=dict(arrowstyle='->', color=C_NAVY, lw=2.5))

    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'gambar_4_metodologi.png')
    plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ Gambar 4 — Flowchart Metodologi: {path}")
    return path


# ============================================================
# GAMBAR 5: STRUKTUR ORGANISASI PT. MURNI SOLUSINDO NUSANTARA
# ============================================================
def chart_struktur_organisasi():
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_xlim(0, 21)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Title
    ax.text(10.5, 11.3, 'Struktur Organisasi', fontsize=16, fontweight='bold',
            color=C_NAVY, ha='center', va='center')
    ax.text(10.5, 10.8, 'PT. Murni Solusindo Nusantara', fontsize=12, color=C_GRAY,
            ha='center', va='center')

    def org_box(x, y, w, h, text, color, fontsize=9):
        rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                              boxstyle="round,pad=0.1",
                              facecolor=color, edgecolor='white', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, y, text, fontsize=fontsize, fontweight='bold',
                color='white', ha='center', va='center', linespacing=1.3)

    def conn_down(x, y1, y2):
        ax.plot([x, x], [y1, y2], color='#999999', lw=1.5)

    # === Level 1: Direktur ===
    org_box(9.0, 9.8, 2.8, 0.7, 'DIREKTUR\nUTAMA', C_NAVY, 10)

    # === Level 2: Departments ===
    depts = [
        (2.2, 'Human\nResources', '#546E7A'),
        (5.2, 'Finance', '#546E7A'),
        (8.2, 'IT', C_BLUE),
        (15.5, 'Digital\nMarketing', C_BLUE),
    ]

    conn_down(9.0, 9.8 - 0.35, 8.8)
    ax.plot([2.2, 15.5], [8.8, 8.8], color='#999999', lw=1.5)

    for dx, name, color in depts:
        conn_down(dx, 8.8, 8.2 + 0.35)
        org_box(dx, 8.2, 2.3, 0.7, name, color, 9)

    # === Level 3: Sub-positions under IT ===
    it_subs = [
        (7.0, 'Kepala\nDivisi IT', C_TEAL),
        (9.5, 'Staff IT\nSupport', C_TEAL),
    ]
    conn_down(8.2, 8.2 - 0.35, 7.0)
    ax.plot([7.0, 9.5], [7.0, 7.0], color='#999999', lw=1.5)

    for sx, name, color in it_subs:
        conn_down(sx, 7.0, 6.4 + 0.35)
        org_box(sx, 6.4, 1.8, 0.7, name, color, 8)

    # === Level 3: Sub-divisions under Digital Marketing ===
    dm_subs = [
        (11.5, 'Web Dev\n& SEO', C_TEAL),
        (13.1, 'UI/UX', C_TEAL),
        (14.7, 'Graphic\nDesign', C_TEAL),
        (16.3, 'Video\nEditor', C_TEAL),
        (17.9, 'Copy-\nwriter', C_TEAL),
        (19.5, 'Email\nMarketing', C_TEAL),
    ]
    conn_down(15.5, 8.2 - 0.35, 7.0)
    ax.plot([11.5, 19.5], [7.0, 7.0], color='#999999', lw=1.5)

    for sx, name, color in dm_subs:
        conn_down(sx, 7.0, 6.4 + 0.35)
        org_box(sx, 6.4, 1.4, 0.7, name, color, 7)

    # === Legend ===
    rect = FancyBboxPatch((0.3, 3.5), 5.0, 1.3,
                          boxstyle="round,pad=0.15",
                          facecolor='#F5F5F5', edgecolor=C_NAVY, linewidth=1.5, linestyle='--')
    ax.add_patch(rect)
    ax.text(2.8, 4.4, 'Keterangan:', fontsize=9, fontweight='bold', color=C_NAVY, ha='center')
    rect_b = FancyBboxPatch((0.6, 3.7), 0.4, 0.3, boxstyle="round,pad=0.05",
                            facecolor=C_BLUE, edgecolor='white')
    ax.add_patch(rect_b)
    ax.text(1.3, 3.85, '= Fokus Audit', fontsize=8, color=C_NAVY, ha='left')
    rect_g = FancyBboxPatch((3.0, 3.7), 0.4, 0.3, boxstyle="round,pad=0.05",
                            facecolor='#546E7A', edgecolor='white')
    ax.add_patch(rect_g)
    ax.text(3.7, 3.85, '= Departemen Lain', fontsize=8, color=C_NAVY, ha='left')

    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'gambar_5_struktur_organisasi.png')
    plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ Gambar 5 — Struktur Organisasi: {path}")
    return path


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("=" * 60)
    print("GENERATING CHARTS — Laporan Audit SI")
    print("=" * 60)

    p1 = chart_radar()
    p2 = chart_gap()
    p3 = chart_ketercapaian()
    p4 = chart_metodologi()
    p5 = chart_struktur_organisasi()

    print("\n" + "=" * 60)
    print(f"✅ Semua 5 grafik berhasil disimpan di: {CHARTS_DIR}")
    print(f"📊 Gambar 1: Radar Chart Capability Level")
    print(f"📊 Gambar 2: GAP Analysis (As-is vs To-be)")
    print(f"📊 Gambar 3: % Ketercapaian per Level per Domain")
    print(f"📊 Gambar 4: Flowchart Alur Metodologi")
    print(f"📊 Gambar 5: Struktur Organisasi")


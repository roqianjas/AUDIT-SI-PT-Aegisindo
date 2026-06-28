"""
Generate Charts — Audit SI PT Aegisindo Mitra Sejati
Palet: Navy (#1a2332) + Teal (#0d9488) + Amber (#f59e0b) + Coral (#ef4444)
Output: 5 PNG → /charts/
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np, os, textwrap

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'charts')
os.makedirs(OUT, exist_ok=True)

# ── palette ──
NAVY   = '#1a2332'
TEAL   = '#0d9488'
TEAL_L = '#5eead4'
AMBER  = '#f59e0b'
CORAL  = '#ef4444'
SLATE  = '#475569'
LGRAY  = '#f1f5f9'
WHITE  = '#ffffff'
STEEL  = '#64748b'
BRAND  = '#d97706'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Liberation Sans','DejaVu Sans','Arial'],
    'font.size': 11,
    'axes.facecolor': WHITE,
    'figure.facecolor': WHITE,
    'savefig.facecolor': WHITE,
    'axes.edgecolor': '#e2e8f0',
    'axes.grid': False,
})

def _header(ax, title, sub, fig):
    fig.text(0.04, 0.97, title, fontsize=18, fontweight='bold', color=NAVY, va='top', ha='left')
    fig.text(0.04, 0.935, sub, fontsize=10, color=STEEL, va='top', ha='left')
    fig.text(0.96, 0.97, 'PT AEGISINDO MITRA SEJATI', fontsize=9, fontweight='bold', color=TEAL, va='top', ha='right')
    fig.text(0.96, 0.945, 'COBIT 2019 • n=6 responden', fontsize=8, color=STEEL, va='top', ha='right')
    # accent line — well below subtitle
    from matplotlib.lines import Line2D
    fig.add_artist(Line2D([0.04, 0.36], [0.905, 0.905], transform=fig.transFigure, color=TEAL, linewidth=3, solid_capstyle='round'))

DOMAINS = ['APO14 — Managed Data','BAI09 — Managed Assets','DSS01 — Managed Operations','DSS04 — Managed Continuity','DSS05 — Managed Security Services']
SHORT   = ['APO14\nData','BAI09\nAset','DSS01\nOperasi','DSS04\nKontinuitas','DSS05\nKeamanan']
AS_IS   = [1, 2, 2, 1, 2]
TO_BE   = [3, 3, 4, 3, 3]
GAPS    = [2, 1, 2, 2, 1]
L1_PCT  = [60.00, 67.78, 70.00, 57.78, 65.56]
L2_PCT  = [45.56, 53.33, 56.67, 43.33, 52.22]
L3_PCT  = [35.56, 43.33, 46.67, 33.33, 41.11]
L1_R    = ['L','L','L','L','L']
L2_R    = ['P','L','L','P','L']
L3_R    = ['P','P','P','P','P']


# ═══════════════════════════════════════════════════════════
# GAMBAR 1 — Profil Capability (Horizontal grouped bars)
# ═══════════════════════════════════════════════════════════
def chart_capability():
    fig, ax = plt.subplots(figsize=(14.4, 8.1))
    fig.subplots_adjust(left=0.22, right=0.92, top=0.84, bottom=0.10)
    _header(ax, 'Profil Capability Proses TI PT Aegisindo',
            'Perbandingan level saat ini dengan target tiap domain audit', fig)

    y = np.arange(len(DOMAINS))
    h = 0.32

    # level bands
    for lv in range(6):
        ax.axvline(lv, color='#e2e8f0', lw=0.8, zorder=0)
        if lv < 5:
            ax.axvspan(lv, lv+1, alpha=0.03, color=NAVY, zorder=0)
    for lv in range(1,6):
        ax.text(lv-0.5, len(DOMAINS)-0.15, f'L{lv}', ha='center', va='bottom', fontsize=8, color=STEEL, fontweight='bold')

    # bars
    colors_as = [CORAL if a==1 else AMBER for a in AS_IS]
    ax.barh(y+h/2, AS_IS, h, color=colors_as, zorder=3, edgecolor=WHITE, linewidth=0.5)
    ax.barh(y-h/2, TO_BE, h, color=TEAL, alpha=0.35, zorder=2, edgecolor=TEAL, linewidth=1, linestyle='--')

    for i in range(len(DOMAINS)):
        # as-is label
        ax.text(AS_IS[i]-0.08, y[i]+h/2, f'L{AS_IS[i]}', ha='right', va='center',
                fontsize=10, fontweight='bold', color=WHITE, zorder=5)
        # to-be label
        ax.text(TO_BE[i]+0.08, y[i]-h/2, f'Target L{TO_BE[i]}', ha='left', va='center',
                fontsize=9, fontweight='bold', color=TEAL, zorder=5)
        # gap badge
        gap = GAPS[i]
        gc = CORAL if gap>=2 else AMBER
        ax.annotate(f'GAP {gap}', xy=(TO_BE[i]+0.6, y[i]),
                    fontsize=8, fontweight='bold', color=WHITE,
                    bbox=dict(boxstyle='round,pad=0.3', fc=gc, ec='none'), ha='center', va='center', zorder=5)

    ax.set_yticks(y)
    ax.set_yticklabels(DOMAINS, fontsize=11, fontweight='bold', color=NAVY)
    ax.set_xlim(-0.1, 5.3)
    ax.set_xlabel('Capability Level COBIT 2019', fontsize=11, color=SLATE, fontweight='bold')
    ax.set_xticks(range(6))
    ax.tick_params(axis='x', colors=SLATE)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.invert_yaxis()

    # legend
    from matplotlib.patches import Patch
    legend_el = [Patch(fc=AMBER, label='As-is Level 2'), Patch(fc=CORAL, label='As-is Level 1'),
                 Patch(fc=TEAL, alpha=0.35, ec=TEAL, label='Target (to-be)')]
    ax.legend(handles=legend_el, loc='lower right', fontsize=9, frameon=True, edgecolor='#e2e8f0')

    fig.savefig(os.path.join(OUT, 'gambar_1_radar_capability.png'), dpi=180, bbox_inches='tight')
    plt.close(fig)
    print('[OK] gambar_1_radar_capability.png')


# ═══════════════════════════════════════════════════════════
# GAMBAR 2 — Gap Analysis (Dumbbell chart)
# ═══════════════════════════════════════════════════════════
def chart_gap():
    fig, ax = plt.subplots(figsize=(14.4, 8.1))
    fig.subplots_adjust(left=0.16, right=0.88, top=0.84, bottom=0.10)
    _header(ax, 'Prioritas Kesenjangan Tata Kelola TI',
            'Jarak level as-is menuju target untuk tiap domain COBIT 2019', fig)

    y = np.arange(len(DOMAINS))
    for lv in range(1,6):
        ax.axvline(lv, color='#e2e8f0', lw=0.8, zorder=0)

    for i in range(len(DOMAINS)):
        a, t = AS_IS[i], TO_BE[i]
        # connector
        ax.plot([a, t], [y[i], y[i]], color='#94a3b8', lw=3, solid_capstyle='round', zorder=2)
        ax.plot([a, t], [y[i], y[i]], color='#cbd5e1', lw=8, solid_capstyle='round', zorder=1, alpha=0.5)
        # as-is dot
        ax.scatter(a, y[i], s=220, color=CORAL if a==1 else AMBER, zorder=4, edgecolors=WHITE, linewidths=2)
        ax.text(a, y[i]+0.32, f'L{a}', ha='center', va='bottom', fontsize=10, fontweight='bold', color=CORAL if a==1 else AMBER)
        # to-be dot
        ax.scatter(t, y[i], s=220, color=TEAL, zorder=4, edgecolors=WHITE, linewidths=2, marker='D')
        ax.text(t, y[i]+0.32, f'L{t}', ha='center', va='bottom', fontsize=10, fontweight='bold', color=TEAL)
        # gap badge on right
        gap = GAPS[i]
        gc = CORAL if gap>=2 else BRAND
        ax.text(5.15, y[i], f'Gap +{gap}', ha='center', va='center', fontsize=10, fontweight='bold',
                color=WHITE, bbox=dict(boxstyle='round,pad=0.35', fc=gc, ec='none'), zorder=5)

    ax.set_yticks(y)
    ax.set_yticklabels(SHORT, fontsize=11, fontweight='bold', color=NAVY, linespacing=1.2)
    ax.set_xlim(0.5, 5.5)
    ax.set_xlabel('Capability Level', fontsize=11, color=SLATE, fontweight='bold')
    ax.set_xticks(range(1,6))
    ax.tick_params(axis='x', colors=SLATE)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.invert_yaxis()

    from matplotlib.lines import Line2D
    legend_el = [Line2D([0],[0], marker='o', color='w', markerfacecolor=AMBER, markersize=10, label='As-is'),
                 Line2D([0],[0], marker='D', color='w', markerfacecolor=TEAL, markersize=10, label='To-be target'),
                 Line2D([0],[0], marker='s', color='w', markerfacecolor=CORAL, markersize=10, label='Prioritas: Gap +2')]
    ax.legend(handles=legend_el, loc='lower center', ncol=3, fontsize=9, frameon=True, edgecolor='#e2e8f0',
              bbox_to_anchor=(0.45, -0.12))

    fig.savefig(os.path.join(OUT, 'gambar_2_gap_analysis.png'), dpi=180, bbox_inches='tight')
    plt.close(fig)
    print('[OK] gambar_2_gap_analysis.png')


# ═══════════════════════════════════════════════════════════
# GAMBAR 3 — Heatmap Rating Ketercapaian
# ═══════════════════════════════════════════════════════════
def chart_heatmap():
    fig, ax = plt.subplots(figsize=(14.4, 8.1))
    fig.subplots_adjust(left=0.26, right=0.88, top=0.84, bottom=0.14)
    _header(ax, 'Matriks Rating Ketercapaian Capability',
            'Persentase jawaban responden pada Level 1–3 dan rating N/P/L/F', fig)

    data = np.array([L1_PCT, L2_PCT, L3_PCT]).T  # 5×3
    ratings = [L1_R, L2_R, L3_R]

    im = ax.imshow(data, cmap='YlOrRd', aspect='auto', vmin=0, vmax=85)

    ax.set_xticks(range(3))
    ax.set_xticklabels(['Level 1\nPerformed','Level 2\nManaged','Level 3\nEstablished'],
                       fontsize=11, fontweight='bold', color=NAVY)
    ax.set_yticks(range(5))
    ax.set_yticklabels(DOMAINS, fontsize=11, fontweight='bold', color=NAVY)

    for i in range(5):
        for j in range(3):
            v = data[i,j]
            r = ratings[j][i]
            rc = TEAL if r in ('L','F') else CORAL
            ax.text(j, i, f'{v:.2f}%\n{r}', ha='center', va='center',
                    fontsize=12, fontweight='bold', color=WHITE if v>45 else NAVY)
            # rating badge
            ax.text(j+0.38, i+0.38, r, ha='center', va='center', fontsize=8, fontweight='bold',
                    color=WHITE, bbox=dict(boxstyle='round,pad=0.15', fc=rc, ec='none', alpha=0.9))

    ax.set_xticks([x-0.5 for x in range(4)], minor=True)
    ax.set_yticks([y-0.5 for y in range(6)], minor=True)
    ax.grid(which='minor', color=WHITE, linewidth=2)
    ax.tick_params(which='minor', size=0)

    cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
    cbar.set_label('Persentase ketercapaian (%)', fontsize=9, color=SLATE)
    cbar.ax.tick_params(labelsize=8, colors=SLATE)

    # legend bar
    fig.text(0.5, 0.04, 'Rating:  N ≤15%  |  P >15–50%  |  L >50–85%  |  F >85–100%',
             ha='center', fontsize=10, color=SLATE, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', fc=LGRAY, ec='#e2e8f0'))

    fig.savefig(os.path.join(OUT, 'gambar_3_ketercapaian.png'), dpi=180, bbox_inches='tight')
    plt.close(fig)
    print('[OK] gambar_3_ketercapaian.png')


# ═══════════════════════════════════════════════════════════
# GAMBAR 4 — Metodologi Audit (Flow Diagram)
# ═══════════════════════════════════════════════════════════
def chart_metodologi():
    fig, ax = plt.subplots(figsize=(14.4, 8.1))
    ax.set_xlim(0, 14.4)
    ax.set_ylim(0, 8.1)
    ax.axis('off')
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    _header(ax, 'Tahapan Audit Sistem Informasi PT Aegisindo',
            'Alur kerja penelitian disusun sebagai pipeline audit COBIT 2019', fig)

    phases = [
        ('01', 'PERSIAPAN', NAVY,
         ['Studi literatur\n& profil perusahaan', 'Identifikasi masalah\nbisnis K3/safety', 'Pemilihan domain\nCOBIT 2019']),
        ('02', 'PENGUMPULAN\nDATA', TEAL,
         ['Penyusunan kuesioner\nLikert 1–5', 'RACI: responden\nlintas divisi', 'Pengisian oleh\n6 responden']),
        ('03', 'ANALISIS\nCOBIT', SLATE,
         ['Tabulasi mean\njawaban', 'Rating N/P/L/F\nper level', 'Penentuan\ncapability level']),
        ('04', 'REKOMENDASI', BRAND,
         ['Analisis gap\nas-is / to-be', 'Prioritas risiko\noperasional', 'Roadmap perbaikan\n12 bulan']),
    ]

    x_start = 0.6
    col_w = 3.2
    gap_x = 0.25
    top_y = 5.6
    head_h = 0.85
    item_h = 0.72
    item_gap = 0.18

    for pi, (num, label, color, items) in enumerate(phases):
        x = x_start + pi * (col_w + gap_x)

        # phase header
        ax.add_patch(FancyBboxPatch((x, top_y), col_w, head_h, boxstyle='round,pad=0.12',
                                     fc=color, ec='none', zorder=3))
        ax.text(x+0.45, top_y+head_h/2, num, fontsize=14, fontweight='black', color=WHITE,
                ha='center', va='center', zorder=4)
        ax.text(x+0.9, top_y+head_h/2, label, fontsize=11, fontweight='bold', color=WHITE,
                ha='left', va='center', zorder=4)

        # items
        for ii, item in enumerate(items):
            iy = top_y - (ii+1)*(item_h+item_gap) + 0.1
            ax.add_patch(FancyBboxPatch((x+0.1, iy), col_w-0.2, item_h, boxstyle='round,pad=0.08',
                                         fc=LGRAY, ec='#cbd5e1', lw=1, zorder=3))
            sub_num = f'{pi+1}.{ii+1}'
            ax.text(x+0.55, iy+item_h/2, sub_num, fontsize=9, fontweight='bold', color=color,
                    ha='center', va='center', zorder=4,
                    bbox=dict(boxstyle='round,pad=0.15', fc=WHITE, ec=color, lw=1))
            ax.text(x+1.0, iy+item_h/2, item, fontsize=9.5, color=NAVY, ha='left', va='center', zorder=4)

        # arrow to next
        if pi < len(phases)-1:
            arrow_y = top_y - 1.0
            ax.annotate('', xy=(x+col_w+gap_x-0.05, arrow_y), xytext=(x+col_w+0.05, arrow_y),
                        arrowprops=dict(arrowstyle='->', color='#94a3b8', lw=2), zorder=5)

    # output box
    ox, oy, ow, oh = 1.5, 0.5, 11.4, 0.7
    ax.add_patch(FancyBboxPatch((ox, oy), ow, oh, boxstyle='round,pad=0.15',
                                 fc=TEAL, ec='none', alpha=0.12, zorder=2))
    ax.add_patch(FancyBboxPatch((ox, oy), ow, oh, boxstyle='round,pad=0.15',
                                 fc='none', ec=TEAL, lw=1.5, zorder=3))
    ax.text(ox+ow/2, oy+oh/2, 'OUTPUT:  Laporan audit SI, capability level, gap analysis, dan rekomendasi perbaikan',
            fontsize=11, fontweight='bold', color=NAVY, ha='center', va='center', zorder=4)

    fig.savefig(os.path.join(OUT, 'gambar_4_metodologi.png'), dpi=180, bbox_inches='tight')
    plt.close(fig)
    print('[OK] gambar_4_metodologi.png')


# ═══════════════════════════════════════════════════════════
# GAMBAR 5 — Struktur Organisasi & Fokus Audit
# ═══════════════════════════════════════════════════════════
def chart_orgmap():
    fig, ax = plt.subplots(figsize=(14.4, 8.1))
    ax.set_xlim(0, 14.4)
    ax.set_ylim(0, 8.1)
    ax.axis('off')
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    _header(ax, 'Peta Fungsi Organisasi dan Fokus Audit',
            'Unit bisnis PT Aegisindo yang terkait data, stok, operasi, kontinuitas, dan keamanan TI', fig)

    def box(x, y, w, h, text, fc=LGRAY, ec='#cbd5e1', tc=NAVY, fs=10, fw='bold', highlight=False):
        if highlight:
            ax.add_patch(FancyBboxPatch((x-0.06, y-0.06), w+0.12, h+0.12, boxstyle='round,pad=0.08',
                                         fc=TEAL, ec='none', alpha=0.15, zorder=1))
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
                                     fc=fc, ec=ec, lw=1.2, zorder=3))
        ax.text(x+w/2, y+h/2, text, fontsize=fs, fontweight=fw, color=tc,
                ha='center', va='center', zorder=4, linespacing=1.3)

    def conn(x1, y1, x2, y2):
        ax.plot([x1, x1, x2, x2], [y1, (y1+y2)/2, (y1+y2)/2, y2],
                color='#94a3b8', lw=1.5, solid_capstyle='round', zorder=2)

    # Director
    dx, dy, dw, dh = 5.2, 5.8, 4.0, 0.7
    box(dx, dy, dw, dh, 'DIREKTUR UTAMA', fc=NAVY, ec=NAVY, tc=WHITE, fs=12)

    # 4 pillars
    pillars = [
        ('Penjualan &\nMarketing', 0.8),
        ('Pengadaan &\nGudang', 4.2),
        ('Keuangan &\nAdministrasi', 7.6),
        ('Customer Service\n& After Sales', 11.0),
    ]
    pw, ph = 2.6, 0.75
    py = 4.5

    for i, (name, px) in enumerate(pillars):
        hl = (i == 1)  # highlight procurement
        pfc = TEAL if i==1 else '#334155'
        box(px, py, pw, ph, name, fc=pfc, ec=pfc, tc=WHITE, fs=10, highlight=hl)
        conn(dx+dw/2, dy, px+pw/2, py+ph)

    # sub-units
    subs = [
        [(0.8, 'Sales Online\nMarketplace'), (0.8, 'Sales Lapangan\nB2B/Proyek')],
        [(4.2, 'Procurement'), (4.2, 'Inventori &\nLogistik')],
        [(7.6, 'Administrasi\nTransaksi'), (7.6, 'IT / Admin\nSistem')],
        [(11.0, 'Keluhan Pelanggan'), (11.0, 'Riwayat Layanan')],
    ]
    sw, sh = 2.2, 0.6
    audit_subs = {(0,0), (1,0), (1,1), (2,1), (3,0)}  # audit-related

    for pi, sub_list in enumerate(subs):
        px = pillars[pi][1]
        for si, (sx, sname) in enumerate(sub_list):
            sy = py - 1.0 - si * (sh + 0.25)
            hl = (pi, si) in audit_subs
            sfc = WHITE if not hl else '#f0fdfa'
            sec = TEAL if hl else '#cbd5e1'
            box(sx + (pw-sw)/2, sy, sw, sh, sname, fc=sfc, ec=sec, tc=NAVY, fs=9, fw='normal', highlight=hl)
            conn(px+pw/2, py, sx+pw/2, sy+sh)

    # legend
    ly = 1.4
    ax.add_patch(FancyBboxPatch((0.8, ly), 3.0, 0.55, boxstyle='round,pad=0.08',
                                 fc=LGRAY, ec='#cbd5e1', lw=1, zorder=3))
    ax.text(1.1, ly+0.28, 'Legenda:', fontsize=9, fontweight='bold', color=NAVY, va='center', zorder=4)
    ax.add_patch(FancyBboxPatch((2.3, ly+0.12), 0.35, 0.3, boxstyle='round,pad=0.03',
                                 fc='#f0fdfa', ec=TEAL, lw=1, zorder=4))
    ax.text(2.8, ly+0.28, 'Area terkait audit', fontsize=8, color=NAVY, va='center', zorder=4)

    # cross-function band
    ax.add_patch(FancyBboxPatch((4.2, ly), 9.4, 0.55, boxstyle='round,pad=0.08',
                                 fc=TEAL, ec=TEAL, alpha=0.08, lw=1, zorder=2))
    ax.text(4.5, ly+0.28, 'Fungsi lintas divisi: IT/Admin Sistem, data transaksi, akun marketplace, backup, dan kontrol akses',
            fontsize=9, fontweight='bold', color=NAVY, va='center', zorder=4)

    # audit focus strip
    ax.add_patch(FancyBboxPatch((1.5, 0.35), 11.4, 0.6, boxstyle='round,pad=0.12',
                                 fc=TEAL, ec='none', alpha=0.1, zorder=2))
    ax.add_patch(FancyBboxPatch((1.5, 0.35), 11.4, 0.6, boxstyle='round,pad=0.12',
                                 fc='none', ec=TEAL, lw=1.5, zorder=3))
    ax.text(7.2, 0.65, 'Fokus audit: APO14 data • BAI09 aset/stok • DSS01 operasi • DSS04 kontinuitas • DSS05 keamanan layanan',
            fontsize=10, fontweight='bold', color=NAVY, ha='center', va='center', zorder=4)

    fig.savefig(os.path.join(OUT, 'gambar_5_struktur_organisasi.png'), dpi=180, bbox_inches='tight')
    plt.close(fig)
    print('[OK] gambar_5_struktur_organisasi.png')


# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    print('Generating charts...')
    chart_capability()
    chart_gap()
    chart_heatmap()
    chart_metodologi()
    chart_orgmap()
    print('All charts done.')

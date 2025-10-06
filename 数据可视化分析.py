"""
Materials Project - 半导体材料数据可视化分析（终极版 - 彻底解决中文乱码）
作者: Luffy.Solution
日期: 2025年10月6日
功能: 对获取的半导体材料数据进行可视化分析，彻底解决中文显示问题
"""

import os
import warnings

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import FontProperties

warnings.filterwarnings("ignore")


# ============================================================================
# 字体配置 - 终极解决方案
# ============================================================================
def setup_chinese_fonts_ultimate():
    """终极中文字体配置方案 - 直接指定字体文件路径"""

    print("正在配置中文字体...")

    # Windows系统中文字体文件路径
    font_paths = [
        r"C:\Windows\Fonts\msyh.ttc",  # 微软雅黑
        r"C:\Windows\Fonts\msyhbd.ttc",  # 微软雅黑 Bold
        r"C:\Windows\Fonts\simhei.ttf",  # 黑体
        r"C:\Windows\Fonts\simsun.ttc",  # 宋体
        r"C:\Windows\Fonts\simkai.ttf",  # 楷体
        r"C:\Windows\Fonts\simfang.ttf",  # 仿宋
    ]

    # 查找第一个存在的字体文件
    chinese_font_path = None
    for font_path in font_paths:
        if os.path.exists(font_path):
            chinese_font_path = font_path
            print(f"✓ 找到中文字体文件: {font_path}")
            break

    if chinese_font_path is None:
        print("⚠ 警告: 未找到标准中文字体文件")
        # 尝试从系统字体管理器获取
        font_list = [
            f.fname
            for f in fm.fontManager.ttflist
            if "Microsoft YaHei" in f.name or "SimHei" in f.name or "SimSun" in f.name
        ]
        if font_list:
            chinese_font_path = font_list[0]
            print(f"✓ 从字体管理器找到: {chinese_font_path}")
        else:
            print("✗ 无法找到中文字体，将使用系统默认字体")
            return None, None

    # 创建FontProperties对象
    chinese_font_prop = FontProperties(fname=chinese_font_path)
    font_name = chinese_font_prop.get_name()

    # 配置matplotlib全局字体 - 多重保险
    plt.rcParams["font.sans-serif"] = [
        font_name,
        "Microsoft YaHei",
        "SimHei",
        "SimSun",
        "DejaVu Sans",
    ]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

    # 强制刷新字体缓存
    fm._load_fontmanager(try_read_cache=False)

    print(f"✓ 字体配置完成: {font_name}")
    print(f"✓ 字体文件: {chinese_font_path}")

    return chinese_font_prop, font_name


# 初始化字体
chinese_font_prop, font_name = setup_chinese_fonts_ultimate()

# ============================================================================
# 美化配置 - 专业学术风格
# ============================================================================
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.15)

# 高质量输出配置
plt.rcParams.update({
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
    "figure.facecolor": "white",
    "axes.facecolor": "#f8f9fa",
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 16,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "legend.fontsize": 11,
    "axes.linewidth": 1.5,
    "grid.linewidth": 0.8,
    "grid.alpha": 0.4,
    "lines.linewidth": 2.5,
})

# 材料类别配色方案
CATEGORY_COLORS = {
    "金属硫化物": "#FFD93D",
    "金属氧化物": "#6BCB77",
    "金属硫氧化物": "#FF6B6B",
    "氮化物": "#4D96FF",
    "碳化物": "#95A5A6",
    "硒化物": "#F8B500",
    "碲化物": "#E67E22",
    "卤化物": "#9B59B6",
    "磷化物": "#1ABC9C",
    "砷化物": "#E74C3C",
}

print("=" * 80)
print("Materials Project - 半导体材料数据可视化分析（终极版）")
print("=" * 80)
print()

# 读取数据
print("正在读取数据...")
df = pd.read_excel("H:\material project\半导体信息查询\主流半导体材料数据库.xlsx")
print(f"✓ 已加载 {len(df)} 个材料的数据\n")

# 数据预处理
for col in df.columns:
    df[col] = df[col].replace("N/A", np.nan)

numeric_cols = [
    "带隙 (eV)",
    "导带底 CBM (eV)",
    "价带顶 VBM (eV)",
    "费米能级 (eV)",
    "形成能 (eV/atom)",
    "能量高于凸包 (eV/atom)",
    "密度 (g/cm³)",
    "体积 (Ų)",
]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ============================================================================
# 1. 带隙分布 - 小提琴图
# ============================================================================
print("正在生成图表 1: 带隙分布（按类别）...")

fig, ax = plt.subplots(figsize=(16, 9))
bg_data = df[df["带隙 (eV)"].notna()].copy()
categories = sorted(bg_data["分类"].unique())

# 准备数据
plot_data = []
for cat in categories:
    cat_data = bg_data[bg_data["分类"] == cat]
    for val in cat_data["带隙 (eV)"]:
        plot_data.append({"分类": cat, "带隙": val})

plot_df = pd.DataFrame(plot_data)

# 创建小提琴图
parts = ax.violinplot(
    [bg_data[bg_data["分类"] == cat]["带隙 (eV)"].values for cat in categories],
    positions=range(len(categories)),
    showmeans=True,
    showmedians=True,
    widths=0.7,
)

# 美化小提琴图
for i, pc in enumerate(parts["bodies"]):
    color = CATEGORY_COLORS.get(categories[i], "#95A5A6")
    pc.set_facecolor(color)
    pc.set_alpha(0.7)
    pc.set_edgecolor("black")
    pc.set_linewidth(1.5)

# 美化其他元素
for partname in ("cbars", "cmins", "cmaxes", "cmedians", "cmeans"):
    if partname in parts:
        vp = parts[partname]
        vp.set_edgecolor("black")
        vp.set_linewidth(2)

# 添加散点
for i, cat in enumerate(categories):
    cat_data = bg_data[bg_data["分类"] == cat]["带隙 (eV)"]
    y = cat_data.values
    x = np.random.normal(i, 0.04, size=len(y))
    ax.scatter(
        x, y, alpha=0.5, s=40, color="white", edgecolors="black", linewidths=1, zorder=3
    )

ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, rotation=45, ha="right", fontsize=12, fontweight="bold")
ax.set_ylabel("带隙 (eV)", fontsize=14, fontweight="bold")
ax.set_xlabel("材料类别", fontsize=14, fontweight="bold")
ax.set_title("主流半导体材料带隙分布（按类别）", fontsize=18, fontweight="bold", pad=20)

# 添加网格
ax.grid(True, alpha=0.3, linestyle="--", linewidth=0.8)
ax.set_axisbelow(True)

# 添加样本数标注
for i, cat in enumerate(categories):
    n = len(bg_data[bg_data["分类"] == cat])
    y_max = bg_data[bg_data["分类"] == cat]["带隙 (eV)"].max()
    ax.text(
        i,
        y_max + 0.2,
        f"n={n}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.5",
            facecolor="white",
            alpha=0.9,
            edgecolor="gray",
            linewidth=1.5,
        ),
    )

plt.tight_layout()
plt.savefig("01_带隙分布按类别_终极版.png", facecolor="white", dpi=300)
print("✓ 已保存: 01_带隙分布按类别_终极版.png")
plt.close()

# ============================================================================
# 2. 带隙分布直方图 - 应用分区
# ============================================================================
print("正在生成图表 2: 带隙分布直方图（光电应用分区）...")

fig, ax = plt.subplots(figsize=(14, 8))
bg_values = bg_data["带隙 (eV)"].values

# 绘制直方图
n, bins, patches = ax.hist(
    bg_values, bins=35, alpha=0.8, edgecolor="black", linewidth=1.5, color="#3498db"
)

# 添加密度曲线
from scipy import stats

kde = stats.gaussian_kde(bg_values)
x_range = np.linspace(bg_values.min(), bg_values.max(), 200)
ax2 = ax.twinx()
ax2.plot(
    x_range,
    kde(x_range) * len(bg_values) * (bins[1] - bins[0]),
    color="#e74c3c",
    linewidth=3.5,
    label="密度曲线",
    alpha=0.8,
)
ax2.set_ylabel("密度", fontsize=14, fontweight="bold")
ax2.grid(False)

# 添加应用区域标记
ax.axvspan(1.1, 1.8, alpha=0.15, color="green", label="光伏最佳区 (1.1-1.8 eV)")
ax.axvspan(2.0, 3.5, alpha=0.15, color="purple", label="光催化候选区 (2.0-3.5 eV)")

# 添加关键分界线
ax.axvline(
    1.0, color="red", linestyle="--", linewidth=2.5, alpha=0.7, label="红外/可见光分界"
)
ax.axvline(
    3.0, color="blue", linestyle="--", linewidth=2.5, alpha=0.7, label="可见光/紫外分界"
)

ax.set_xlabel("带隙 (eV)", fontsize=14, fontweight="bold")
ax.set_ylabel("材料数量", fontsize=14, fontweight="bold")
ax.set_title("半导体材料带隙分布与应用分区", fontsize=18, fontweight="bold", pad=20)

# 合并图例
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(
    lines1 + lines2,
    labels1 + labels2,
    loc="upper right",
    fontsize=11,
    framealpha=0.95,
    edgecolor="gray",
    shadow=True,
)

plt.tight_layout()
plt.savefig("02_带隙分布直方图与应用分区_终极版.png", facecolor="white", dpi=300)
print("✓ 已保存: 02_带隙分布直方图与应用分区_终极版.png")
plt.close()

# ============================================================================
# 3. 能带位置图
# ============================================================================
print("正在生成图表 3: 能带位置图（CBM vs VBM）...")

fig, ax = plt.subplots(figsize=(14, 10))
band_data = df[(df["导带底 CBM (eV)"].notna()) & (df["价带顶 VBM (eV)"].notna())].copy()

# 按类别绘制散点
for cat in sorted(band_data["分类"].unique()):
    cat_data = band_data[band_data["分类"] == cat]
    ax.scatter(
        cat_data["价带顶 VBM (eV)"],
        cat_data["导带底 CBM (eV)"],
        s=150,
        alpha=0.7,
        label=cat,
        color=CATEGORY_COLORS.get(cat, "#95A5A6"),
        edgecolors="black",
        linewidths=1.5,
    )

# 添加水分解能级参考线
ax.axhline(
    y=0,
    color="#3498db",
    linestyle="--",
    linewidth=3.5,
    label="H₂/H⁺ 还原电位 (0 eV)",
    alpha=0.8,
)
ax.axhline(
    y=-1.23,
    color="#e74c3c",
    linestyle="--",
    linewidth=3.5,
    label="O₂/H₂O 氧化电位 (-1.23 eV)",
    alpha=0.8,
)

# 添加理想区域阴影
ax.axhspan(-3, -1.23, alpha=0.1, color="red", label="VBM理想区")
ax.axhspan(0, 2, alpha=0.1, color="blue", label="CBM理想区")

ax.set_xlabel("价带顶 VBM (eV)", fontsize=14, fontweight="bold")
ax.set_ylabel("导带底 CBM (eV)", fontsize=14, fontweight="bold")
ax.set_title("半导体材料能带位置与水分解能级", fontsize=18, fontweight="bold", pad=20)
ax.legend(
    loc="best", fontsize=10, ncol=2, framealpha=0.95, edgecolor="gray", shadow=True
)
ax.grid(True, alpha=0.3, linestyle="--")

plt.tight_layout()
plt.savefig("03_能带位置图_终极版.png", facecolor="white", dpi=300)
print("✓ 已保存: 03_能带位置图_终极版.png")
plt.close()

# ============================================================================
# 4. 稳定性气泡图
# ============================================================================
print("正在生成图表 4: 形成能与稳定性关系...")

fig, ax = plt.subplots(figsize=(14, 8))
stability_data = df[
    (df["形成能 (eV/atom)"].notna()) & (df["能量高于凸包 (eV/atom)"].notna())
].copy()

for cat in sorted(stability_data["分类"].unique()):
    cat_data = stability_data[stability_data["分类"] == cat]
    sizes = cat_data["带隙 (eV)"].fillna(1) * 60
    ax.scatter(
        cat_data["形成能 (eV/atom)"],
        cat_data["能量高于凸包 (eV/atom)"],
        s=sizes,
        alpha=0.6,
        label=cat,
        color=CATEGORY_COLORS.get(cat, "#95A5A6"),
        edgecolors="black",
        linewidths=1.5,
    )

# 添加稳定性参考线
ax.axhline(
    y=0.05,
    color="orange",
    linestyle="--",
    linewidth=2.5,
    label="稳定性阈值 (0.05 eV/atom)",
    alpha=0.8,
)
ax.axhline(
    y=0.1,
    color="red",
    linestyle="--",
    linewidth=2.5,
    label="不稳定阈值 (0.1 eV/atom)",
    alpha=0.8,
)

# 添加稳定区域阴影
ax.axhspan(0, 0.05, alpha=0.1, color="green", label="高度稳定区")

ax.set_xlabel("形成能 (eV/atom)", fontsize=14, fontweight="bold")
ax.set_ylabel("能量高于凸包 (eV/atom)", fontsize=14, fontweight="bold")
ax.set_title(
    "半导体材料热力学稳定性分析\n（气泡大小 ∝ 带隙）",
    fontsize=18,
    fontweight="bold",
    pad=20,
)
ax.legend(
    loc="upper right",
    fontsize=10,
    ncol=2,
    framealpha=0.95,
    edgecolor="gray",
    shadow=True,
)
ax.grid(True, alpha=0.3, linestyle="--")

plt.tight_layout()
plt.savefig("04_形成能与稳定性_终极版.png", facecolor="white", dpi=300)
print("✓ 已保存: 04_形成能与稳定性_终极版.png")
plt.close()

# ============================================================================
# 5. 材料分布双饼图
# ============================================================================
print("正在生成图表 5: 材料类别分布饼图...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# 左图：材料数量分布
category_counts = df["分类"].value_counts()
colors1 = [CATEGORY_COLORS.get(cat, "#95A5A6") for cat in category_counts.index]

wedges, texts, autotexts = ax1.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct="%1.1f%%",
    colors=colors1,
    startangle=90,
    textprops={"fontsize": 12, "fontweight": "bold"},
    explode=[0.05] * len(category_counts),
    shadow=True,
)

ax1.set_title("材料类别分布（按数量）", fontsize=16, fontweight="bold", pad=20)

for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontweight("bold")
    autotext.set_fontsize(11)

# 右图：应用潜力分布
potential_counts = df["光电应用潜力"].value_counts()
colors2 = {
    "优秀": "#27AE60",
    "良好": "#3498DB",
    "一般": "#F39C12",
    "较低": "#E74C3C",
    "未知": "#95A5A6",
}
pie_colors = [colors2.get(label, "#95A5A6") for label in potential_counts.index]

wedges, texts, autotexts = ax2.pie(
    potential_counts.values,
    labels=potential_counts.index,
    autopct="%1.1f%%",
    colors=pie_colors,
    startangle=90,
    textprops={"fontsize": 12, "fontweight": "bold"},
    explode=[0.05] * len(potential_counts),
    shadow=True,
)

ax2.set_title("光电应用潜力分布", fontsize=16, fontweight="bold", pad=20)

for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontweight("bold")
    autotext.set_fontsize(11)

plt.tight_layout()
plt.savefig("05_材料类别与应用潜力分布_终极版.png", facecolor="white", dpi=300)
print("✓ 已保存: 05_材料类别与应用潜力分布_终极版.png")
plt.close()

# ============================================================================
# 6. 带隙类型分组柱状图
# ============================================================================
print("正在生成图表 6: 直接/间接带隙对比...")

fig, ax = plt.subplots(figsize=(14, 8))
gap_type_data = df[df["带隙 (eV)"].notna()].copy()
gap_type_grouped = (
    gap_type_data.groupby(["分类", "直接带隙"]).size().unstack(fill_value=0)
)

# 绘制分组柱状图
x = np.arange(len(gap_type_grouped.index))
width = 0.35

bars1 = ax.bar(
    x - width / 2,
    gap_type_grouped["否"],
    width,
    label="间接带隙",
    color="#E74C3C",
    edgecolor="black",
    linewidth=1.5,
)
bars2 = ax.bar(
    x + width / 2,
    gap_type_grouped["是"],
    width,
    label="直接带隙",
    color="#3498DB",
    edgecolor="black",
    linewidth=1.5,
)

# 添加数值标签
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 0.3,
                f"{int(height)}",
                ha="center",
                va="bottom",
                fontsize=10,
                fontweight="bold",
            )

ax.set_ylabel("材料数量", fontsize=14, fontweight="bold")
ax.set_xlabel("材料类别", fontsize=14, fontweight="bold")
ax.set_title(
    "半导体材料带隙类型分布（直接 vs 间接）", fontsize=18, fontweight="bold", pad=20
)
ax.set_xticks(x)
ax.set_xticklabels(gap_type_grouped.index, rotation=45, ha="right", fontsize=11)
ax.legend(
    loc="upper right", fontsize=13, framealpha=0.95, edgecolor="gray", shadow=True
)
ax.grid(True, alpha=0.3, axis="y", linestyle="--")

plt.tight_layout()
plt.savefig("06_带隙类型分布_终极版.png", facecolor="white", dpi=300)
print("✓ 已保存: 06_带隙类型分布_终极版.png")
plt.close()

# ============================================================================
# 7. TOP材料热力图
# ============================================================================
print("正在生成图表 7: TOP材料性能热力图...")

top_materials = df[df["光电应用潜力"].isin(["优秀", "良好"])].head(20)

if len(top_materials) > 0:
    # 选择关键指标
    heatmap_data = top_materials[
        [
            "化学式",
            "带隙 (eV)",
            "形成能 (eV/atom)",
            "能量高于凸包 (eV/atom)",
            "密度 (g/cm³)",
        ]
    ].copy()
    heatmap_data = heatmap_data.set_index("化学式")

    # 标准化数据
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    heatmap_normalized = pd.DataFrame(
        scaler.fit_transform(heatmap_data.fillna(0)),
        index=heatmap_data.index,
        columns=heatmap_data.columns,
    )

    fig, ax = plt.subplots(figsize=(11, 15))

    sns.heatmap(
        heatmap_normalized,
        annot=heatmap_data,
        fmt=".3f",
        cmap="RdYlGn_r",
        linewidths=2,
        linecolor="white",
        cbar_kws={"label": "标准化值"},
        ax=ax,
        vmin=-2,
        vmax=2,
        center=0,
        annot_kws={"fontsize": 10, "fontweight": "bold"},
    )

    ax.set_title(
        "TOP 20 光伏候选材料性能热力图\n（数值为实际值，颜色为标准化值）",
        fontsize=16,
        fontweight="bold",
        pad=20,
    )
    ax.set_ylabel("材料", fontsize=14, fontweight="bold")
    ax.set_xlabel("性能指标", fontsize=14, fontweight="bold")

    plt.tight_layout()
    plt.savefig("07_TOP材料性能热力图_终极版.png", facecolor="white", dpi=300)
    print("✓ 已保存: 07_TOP材料性能热力图_终极版.png")
    plt.close()

# ============================================================================
# 8. 密度-带隙关系散点图
# ============================================================================
print("正在生成图表 8: 密度与带隙关系...")

fig, ax = plt.subplots(figsize=(14, 8))
density_data = df[(df["密度 (g/cm³)"].notna()) & (df["带隙 (eV)"].notna())].copy()

for cat in sorted(density_data["分类"].unique()):
    cat_data = density_data[density_data["分类"] == cat]
    ax.scatter(
        cat_data["密度 (g/cm³)"],
        cat_data["带隙 (eV)"],
        s=130,
        alpha=0.7,
        label=cat,
        color=CATEGORY_COLORS.get(cat, "#95A5A6"),
        edgecolors="black",
        linewidths=1.5,
    )

# 添加趋势线
from scipy.stats import linregress

x = density_data["密度 (g/cm³)"].values
y = density_data["带隙 (eV)"].values
slope, intercept, r_value, p_value, std_err = linregress(x, y)
line_x = np.linspace(x.min(), x.max(), 100)
line_y = slope * line_x + intercept
ax.plot(
    line_x, line_y, "r--", linewidth=3, alpha=0.8, label=f"趋势线 (R²={r_value**2:.3f})"
)

ax.set_xlabel("密度 (g/cm³)", fontsize=14, fontweight="bold")
ax.set_ylabel("带隙 (eV)", fontsize=14, fontweight="bold")
ax.set_title("半导体材料密度与带隙关系", fontsize=18, fontweight="bold", pad=20)
ax.legend(
    loc="best", fontsize=10, ncol=2, framealpha=0.95, edgecolor="gray", shadow=True
)
ax.grid(True, alpha=0.3, linestyle="--")

plt.tight_layout()
plt.savefig("08_密度与带隙关系_终极版.png", facecolor="white", dpi=300)
print("✓ 已保存: 08_密度与带隙关系_终极版.png")
plt.close()

# ============================================================================
# 完成
# ============================================================================
print()
print("=" * 80)
print("✅ 所有可视化图表生成完成！（终极版 - 彻底解决中文乱码）")
print("=" * 80)
print("\n生成的图表:")
print("  1. 01_带隙分布按类别_终极版.png")
print("  2. 02_带隙分布直方图与应用分区_终极版.png")
print("  3. 03_能带位置图_终极版.png")
print("  4. 04_形成能与稳定性_终极版.png")
print("  5. 05_材料类别与应用潜力分布_终极版.png")
print("  6. 06_带隙类型分布_终极版.png")
print("  7. 07_TOP材料性能热力图_终极版.png")
print("  8. 08_密度与带隙关系_终极版.png")
print()
print("特点:")
print("  ✓ 直接使用系统字体文件路径")
print("  ✓ 强制刷新字体缓存")
print("  ✓ 多重字体配置保险")
print("  ✓ 彻底解决中文乱码问题")
print("  ✓ 300 DPI高分辨率输出")
print("=" * 80)

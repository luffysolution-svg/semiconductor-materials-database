# 主流半导体材料数据库

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Materials Project](https://img.shields.io/badge/Data-Materials%20Project-orange.svg)](https://materialsproject.org)

> 基于 Materials Project API 的半导体材料数据采集与可视化分析工具

---

## 📖 项目简介

本项目通过 Materials Project API 自动获取并分析主流半导体材料的完整电子结构和性能数据，涵盖金属硫化物、氧化物、氮化物等 **10大类别** 共 **76+种材料**，并生成专业的可视化图表。

### ✨ 主要特点

- 🔬 **自动化数据采集** - 批量获取 76+ 种半导体材料的完整数据
- 📊 **专业可视化** - 生成 8 张高质量学术图表（300 DPI，完美中文支持）
- 📈 **智能评估** - 自动评估光伏和光催化应用潜力
- 📑 **美化输出** - 生成格式化 Excel 数据库，带分类颜色标记
- 🔒 **安全配置** - API Key 配置文件系统，保护敏感信息

---

## 📁 项目结构

```
semiconductor-materials-database/
├── 获取主流半导体材料数据.py    # 数据采集脚本
├── 数据可视化分析.py            # 可视化生成脚本
├── config_example.py           # API 配置示例
├── requirements.txt            # Python 依赖
├── README.md                  # 项目文档
├── LICENSE                    # MIT 许可证
└── .gitignore                 # Git 忽略规则
```

---

## 🚀 快速开始

### 前置要求

- Python 3.7+
- Materials Project API Key（[免费注册获取](https://materialsproject.org)）

### 安装步骤

**1. 克隆仓库**

```bash
git clone https://github.com/luffysolution-svg/semiconductor-materials-database.git
cd semiconductor-materials-database
```

**2. 安装依赖**

```bash
pip install -r requirements.txt
```

**3. 配置 API Key**

1. 访问 [materialsproject.org](https://materialsproject.org) 注册并获取 API Key
2. 复制配置文件：
   ```bash
   # Windows
   copy config_example.py config.py
   
   # Linux/Mac
   cp config_example.py config.py
   ```
3. 编辑 `config.py`，填入您的真实 API Key：
   ```python
   API_KEY = "您的实际API密钥"
   BASE_URL = "https://api.materialsproject.org"
   ```

> ⚠️ **安全提示**：`config.py` 包含敏感信息，已被 `.gitignore` 排除，不会上传到 Git 仓库

---

## 💻 使用方法

### 步骤 1：获取数据

```bash
python 获取主流半导体材料数据.py
```

**输出文件：**
- `主流半导体材料数据库.xlsx` - 美化的 Excel 数据库
- `主流半导体材料数据库.json` - JSON 格式完整数据
- `主流半导体材料数据摘要.txt` - 统计摘要报告

### 步骤 2：生成可视化

```bash
python 数据可视化分析.py
```

**输出：** 8 张高清 PNG 图表（300 DPI）

---

## 📊 数据指标

### 核心性能指标（20项）

| 类别 | 指标 |
|------|------|
| **基本信息** | Materials ID、化学式、材料分类 |
| **电子结构** | 带隙、直接/间接带隙、导带底(CBM)、价带顶(VBM)、费米能级 |
| **热力学** | 形成能、能量高于凸包（稳定性指标） |
| **物理性质** | 密度、晶胞体积 |
| **晶体结构** | 空间群、晶系 |
| **应用评估** | 光伏潜力、光催化潜力 |

---

## 🔬 材料类别覆盖

| 类别 | 数量 | 代表性材料 | 典型带隙 |
|------|:----:|-----------|---------|
| 金属硫化物 | 18+ | CdS, ZnS, MoS₂ | 0.8-3.5 eV |
| 金属氧化物 | 14+ | TiO₂, ZnO, WO₃ | 1.0-3.5 eV |
| 氮化物 | 9+ | GaN, AlN, InN | 0.7-6.0 eV |
| 碳化物 | 8+ | SiC, WC, TaC | 2.0-3.0 eV |
| 硒化物 | 7+ | CdSe, ZnSe, MoSe₂ | 1.0-2.7 eV |
| 碲化物 | 6+ | CdTe, ZnTe, Bi₂Te₃ | 1.0-2.5 eV |
| 卤化物 | 5+ | BiOCl, BiOBr, AgCl | 2.0-3.5 eV |
| 磷化物 | 4+ | GaP, InP, AlP | 1.4-2.5 eV |
| 砷化物 | 3+ | GaAs, InAs, AlAs | 0.4-2.2 eV |
| 金属硫氧化物 | 2+ | Bi₂S₂O₃ | 1.0-1.8 eV |

**总计：** 76+ 种材料

---

## 📈 可视化图表

生成的 8 张专业图表：

| 图表 | 文件名 | 说明 |
|------|--------|------|
| 1 | `01_带隙分布按类别.png` | 小提琴图 - 展示各类别的带隙分布特征 |
| 2 | `02_带隙分布直方图与应用分区.png` | 直方图 - 标注光伏最佳区和光催化区 |
| 3 | `03_能带位置图.png` | 散点图 - CBM/VBM 相对水分解能级的位置 |
| 4 | `04_形成能与稳定性.png` | 气泡图 - 热力学稳定性分析 |
| 5 | `05_材料类别与应用潜力分布.png` | 双饼图 - 材料分布和应用潜力统计 |
| 6 | `06_带隙类型分布.png` | 柱状图 - 直接带隙 vs 间接带隙对比 |
| 7 | `07_TOP材料性能热力图.png` | 热力图 - TOP 20 光伏候选材料性能对比 |
| 8 | `08_密度与带隙关系.png` | 散点图 - 密度与带隙的相关性分析 |

---

## 🌟 推荐材料

### 最佳光伏候选材料

| 排名 | 材料 | 带隙 (eV) | 带隙类型 | 优势 |
|:----:|------|----------:|:--------:|------|
| 1 | **GaAs** | 1.42 | 直接 | 理想带隙 + 高效率 |
| 2 | **CdTe** | 1.48 | 直接 | 商用薄膜材料 |
| 3 | **InP** | 1.35 | 直接 | 高载流子迁移率 |
| 4 | **CdS** | 2.40 | 直接 | 优秀的窗口层材料 |
| 5 | **GaP** | 2.26 | 间接 | 宽带隙半导体 |

### 最佳光催化候选材料

| 排名 | 材料 | 带隙 (eV) | CBM (eV) | VBM (eV) | 优势 |
|:----:|------|----------:|---------:|---------:|------|
| 1 | **TiO₂** | 3.20 | 0.20 | -3.00 | 经典光催化剂，稳定性优异 |
| 2 | **WO₃** | 2.76 | -0.50 | -3.26 | 可见光响应良好 |
| 3 | **BiVO₄** | 2.40 | 0.30 | -2.10 | 水氧化性能优异 |
| 4 | **ZnO** | 3.25 | 0.15 | -3.10 | 高载流子迁移率 |
| 5 | **GaN** | 3.30 | 0.50 | -2.80 | 化学稳定性极佳 |

---

## 🛠️ 技术细节

### 数据采集策略

```python
# 按化学体系精确搜索
chemical_systems = {
    "金属硫化物": ["Cd-S", "Zn-S", "Mo-S", ...],
    "金属氧化物": ["Ti-O", "Zn-O", "W-O", ...],
    # ... 更多类别
}

# API 调用流程
1. 按化学体系搜索 → 获取 Materials ID 列表
2. 批量获取电子结构 → 带隙、CBM、VBM 等
3. 获取热力学数据 → 形成能、稳定性
4. 评估应用潜力 → 基于带隙和能带位置
5. 生成美化 Excel → 自动排序、配色、列宽调整
```

### 可视化技术亮点

**中文字体完美显示：**

```python
# 直接指定 Windows 系统字体文件路径
font_path = r'C:\Windows\Fonts\msyh.ttc'  # 微软雅黑
chinese_font = FontProperties(fname=font_path)

# 强制刷新字体缓存
fm._load_fontmanager(try_read_cache=False)

# 配置全局字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', ...]
plt.rcParams['axes.unicode_minus'] = False
```

**专业美化配置：**

- 🎨 10 种材料类别专属配色（色盲友好）
- 📊 Seaborn whitegrid 专业学术风格
- 🖼️ 300 DPI 高分辨率输出（适合发表）
- 📐 增强网格、阴影、边框
- 📊 丰富统计标注：样本数、R² 值、趋势线

---

## 📦 依赖包

```txt
requests>=2.28.0       # API 调用
pandas>=1.5.0          # 数据处理
openpyxl>=3.0.0        # Excel 读写
matplotlib>=3.7.0      # 绘图核心
seaborn>=0.12.0        # 统计可视化
scipy>=1.9.0           # 科学计算
scikit-learn>=1.1.0    # 数据标准化
numpy>=1.23.0          # 数值计算
```

---

## 📝 使用场景

### 🎓 学术研究

- ✅ 论文配图（300 DPI，出版级质量）
- ✅ 材料筛选与性能对比
- ✅ 理论预测验证

### 📚 教学演示

- ✅ 半导体物理课程
- ✅ 材料科学案例分析
- ✅ Python 数据分析教学

### 🏭 工程应用

- ✅ 光伏材料选型
- ✅ 光催化剂设计
- ✅ 新材料开发参考

---

## 🔧 常见问题

<details>
<summary><strong>Q: API 调用失败怎么办？</strong></summary>

**解决方法：**
1. 检查 API Key 是否正确配置
2. 确认网络连接正常
3. 验证 Materials Project 服务状态
4. 查看是否超出 API 调用限制

</details>

<details>
<summary><strong>Q: 中文显示乱码？</strong></summary>

**解决方法：**
- **Windows:** 确保已安装微软雅黑（msyh.ttc）
- **Linux:** 安装中文字体 `sudo apt-get install fonts-wqy-microhei`
- **macOS:** 使用系统自带的 PingFang SC 或 Hiragino Sans

</details>

<details>
<summary><strong>Q: 图表生成失败？</strong></summary>

**检查项：**
1. 是否已运行数据采集脚本
2. 确认生成了 `主流半导体材料数据库.xlsx`
3. 检查所有依赖包版本是否符合要求

</details>

---

## 🤝 贡献指南

欢迎贡献！您可以：

1. 🐛 报告 Bug - 在 Issues 中提交
2. 💡 提出新功能建议
3. 📝 改进文档
4. 🔧 提交代码优化

**贡献流程：**

```bash
# 1. Fork 本仓库
# 2. 创建特性分支
git checkout -b feature/AmazingFeature

# 3. 提交更改
git commit -m 'Add some AmazingFeature'

# 4. 推送到分支
git push origin feature/AmazingFeature

# 5. 创建 Pull Request
```

---

## 📄 数据来源与引用

**数据来源：** [Materials Project](https://materialsproject.org)  
**数据许可：** CC BY 4.0

**引用格式：**

```
Jain, A., Ong, S. P., Hautier, G., Chen, W., Richards, W. D., 
Dacek, S., Cholia, S., Gunter, D., Skinner, D., Ceder, G., & 
Persson, K. A. (2013). Commentary: The Materials Project: A 
materials genome approach to accelerating materials innovation. 
APL Materials, 1(1), 011002.
https://doi.org/10.1063/1.4812323
```

---

## 📜 开源许可

本项目采用 [MIT License](LICENSE) 开源许可证。

- ✅ 商业使用
- ✅ 修改
- ✅ 分发
- ✅ 私人使用

**注意：** 使用 Materials Project 数据请遵守其 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可协议。

---

## 📧 联系方式

- **作者：** Luffy Solution
- **GitHub：** [@luffysolution-svg](https://github.com/luffysolution-svg)
- **项目主页：** [semiconductor-materials-database](https://github.com/luffysolution-svg/semiconductor-materials-database)
- **问题反馈：** [Issues](https://github.com/luffysolution-svg/semiconductor-materials-database/issues)

---

## ⭐ Star History

如果这个项目对您有帮助，请给一个 ⭐️ Star 支持一下！

---

## 🙏 致谢

- [Materials Project](https://materialsproject.org) - 提供优质的材料数据库
- [Matplotlib](https://matplotlib.org) - 强大的 Python 可视化库
- [Pandas](https://pandas.pydata.org) - 数据分析利器

---

<div align="center">

**最后更新：** 2025年10月6日  
**版本：** v1.0  
**项目状态：** ✅ 生产就绪

Made with ❤️ by [Luffy Solution](https://github.com/luffysolution-svg)

</div>

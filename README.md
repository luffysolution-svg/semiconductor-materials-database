# 主流半导体材料数据库项目# 主流半导体材料数据库项目# 半导体材料信息查询系统



[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[![Materials Project](https://img.shields.io/badge/Data-Materials%20Project-orange.svg)](https://materialsproject.org)## 📁 项目概述本项目使用 Materials Project API 获取半导体材料的详细信息，包括带隙、能带位置、晶体参数等，并自动生成 Excel 表格和可视化 PDF 报告。



通过 Materials Project API 获取并分析主流研究的半导体材料数据，涵盖金属硫化物、氧化物、氮化物等10大类别的完整电子结构和性能数据。



## 🎯 项目特点本项目通过 Materials Project API 获取并分析主流研究的半导体材料数据，涵盖金属硫化物、氧化物、氮化物等10大类别，共76种半导体材料的完整电子结构和性能数据。## 📋 项目简介



- 📊 **自动化数据采集** - 从 Materials Project 批量获取76+种半导体材料数据

- 🎨 **专业可视化** - 生成8张高质量学术图表（300 DPI，完美中文支持）

- 📈 **应用评估** - 自动评估光伏和光催化应用潜力**创建日期：** 2025年10月6日  本系统可以自动从 Materials Project 数据库获取以下半导体材料的信息：

- 📑 **美化数据库** - 自动生成格式化Excel数据库，带颜色标记

**作者：** Luffy.Solution  - ZnIn2S4（硫化锌铟）

## 📁 项目结构

**数据来源：** Materials Project Database (materialsproject.org)- C3N4（氮化碳）

```

semiconductor-materials-database/- TiO2（二氧化钛）

│

├── 获取主流半导体材料数据.py    # 数据采集脚本---- CdS（硫化镉）

├── 数据可视化分析.py            # 可视化生成脚本

├── requirements.txt            # Python依赖- Ti3C2（钛碳化物）

├── README.md                  # 项目说明

├── LICENSE                    # 开源许可## 📊 项目文件说明- BiVO4（钒酸铋）

└── .gitignore                 # Git忽略规则

```- BiVO6（钒酸铋）



## 🚀 快速开始### 1️⃣ 核心数据文件- ZnCdSe（硒化锌镉）



### 1. 安装依赖- MoS2（二硫化钼）



```bash| 文件名 | 说明 | 大小 |- FeOOH（羟基氧化铁）

pip install -r requirements.txt

```|--------|------|------|- Fe3O4（四氧化三铁）



### 2. 配置 API Key| `主流半导体材料数据库.xlsx` | **主数据库** - 包含76种材料的20项性能指标，带自动格式化和颜色标记 | 14.8 KB |



在 `获取主流半导体材料数据.py` 中设置您的 Materials Project API Key：| `主流半导体材料数据库.json` | JSON格式完整数据，便于程序读取和进一步分析 | 58.7 KB |## 📊 获取的数据



```python| `主流半导体材料数据摘要.txt` | 统计摘要报告，包含TOP 10材料推荐 | 3.2 KB |

API_KEY = "您的API密钥"  # 从 https://materialsproject.org 获取

```### 基本信息



### 3. 获取数据### 2️⃣ 数据获取脚本- Material ID（材料编号）



```bash- 化学式（标准化）

python 获取主流半导体材料数据.py

```| 文件名 | 说明 |- 是否稳定



**输出文件：**|--------|------|- 热力学稳定性（能量高于壳层）

- `主流半导体材料数据库.xlsx` - 美化的Excel数据库

- `主流半导体材料数据库.json` - JSON格式完整数据| `获取主流半导体材料数据.py` | **核心采集脚本** - 从Materials Project API批量获取数据并生成Excel数据库 |

- `主流半导体材料数据摘要.txt` - 统计摘要报告

### 电子性质

### 4. 生成可视化图表

**主要功能：**- **带隙 (Band Gap)**：半导体的禁带宽度

```bash

python 数据可视化分析.py- 🔍 按化学体系搜索10大类半导体材料- **导带最小值 (CBM)**：导带底的能量位置

```

- 📡 获取完整电子结构数据（带隙、CBM、VBM等）- **价带最大值 (VBM)**：价带顶的能量位置

**输出：** 8张高清PNG图表（300 DPI）

1. 带隙分布按类别（小提琴图）- 🎯 评估光伏和光催化应用潜力- **费米能级**：电子填充的最高能级

2. 带隙分布直方图与应用分区

3. 能带位置图（CBM vs VBM）- 📊 自动生成美化的Excel数据库- 是否为直接带隙

4. 形成能与稳定性分析

5. 材料类别与应用潜力分布- 是否为金属

6. 带隙类型分布

7. TOP材料性能热力图### 3️⃣ 数据可视化文件

8. 密度与带隙关系

### 晶体结构

## 📊 数据库指标

#### Python脚本- 晶格参数（a, b, c）

### 核心性能指标（20项）

| 文件名 | 说明 |- 晶格角（α, β, γ）

| 指标类别 | 具体指标 |

|---------|---------||--------|------|- 晶系（立方、四方、六方等）

| **基本信息** | Materials ID, 化学式, 分类 |

| **电子结构** | 带隙, 直接带隙, 导带底CBM, 价带顶VBM, 费米能级 || `数据可视化分析.py` | **终极版可视化脚本** - 生成8张高质量学术图表，完美支持中文显示 |- 空间群符号和编号

| **热力学稳定性** | 形成能, 能量高于凸包 |

| **物理性质** | 密度, 体积 |- 体积

| **晶体结构** | 空间群, 晶系 |

| **应用评估** | 光伏潜力, 光催化潜力, 综合潜力 |**技术特点：**- 密度



## 🔬 材料类别覆盖- ✅ 直接使用Windows系统字体文件（`C:\Windows\Fonts\msyh.ttc`）- 原子数量



| 类别 | 数量 | 代表性材料 |- ✅ 强制刷新字体缓存，彻底解决中文乱码问题

|------|------|-----------|

| 金属硫化物 | 18+ | CdS, ZnS, MoS₂ |- ✅ 300 DPI高分辨率输出，适合论文发表## 🚀 快速开始

| 金属氧化物 | 14+ | TiO₂, ZnO, WO₃ |

| 氮化物 | 9+ | GaN, AlN, InN |- ✅ 专业学术配色方案，10种材料类别独立配色

| 碳化物 | 8+ | SiC, WC, TaC |

| 硒化物 | 7+ | CdSe, ZnSe, MoSe₂ |### 方法 1: 一键运行（推荐）

| 碲化物 | 6+ | CdTe, ZnTe |

| 卤化物 | 5+ | BiOCl, BiOBr |#### 生成的图表（8张）

| 磷化物 | 4+ | GaP, InP, AlP |

| 砷化物 | 3+ | GaAs, InAs |直接运行主程序，它会自动完成所有步骤：

| 金属硫氧化物 | 2+ | Bi₂S₂O₃ |

| 图表编号 | 文件名 | 说明 | 大小 |

**总计：** 76+ 种材料

|---------|--------|------|------|```bash

## 🌟 推荐材料

| 图表 1 | `01_带隙分布按类别.png` | **小提琴图** - 展示各材料类别的带隙分布特征，带散点和样本数标注 | 516 KB |python run_all.py

### 最佳光伏候选材料

1. **GaAs** (1.42 eV) - 理想带隙，直接带隙| 图表 2 | `02_带隙分布直方图与应用分区.png` | **直方图+密度曲线** - 标注光伏最佳区(1.1-1.8 eV)和光催化候选区(2.0-3.5 eV) | 199 KB |```

2. **CdTe** (1.48 eV) - 商用薄膜材料

3. **InP** (1.35 eV) - 高迁移率| 图表 3 | `03_能带位置图.png` | **能带位置散点图** - 展示CBM/VBM相对水分解能级的位置关系 | 418 KB |

4. **CdS** (2.40 eV) - 窗口层材料

5. **GaP** (2.26 eV) - 宽带隙半导体| 图表 4 | `04_形成能与稳定性.png` | **气泡图** - 形成能vs能量高于凸包，气泡大小表示带隙，标注稳定性阈值 | 139 KB |程序会自动：



### 最佳光催化候选材料| 图表 5 | `05_材料类别与应用潜力分布.png` | **双饼图** - 左图为材料数量分布，右图为光电应用潜力分布 | 596 KB |1. 检查并安装所需的 Python 包

1. **TiO₂** (3.20 eV) - 经典光催化剂

2. **WO₃** (2.76 eV) - 可见光响应| 图表 6 | `06_带隙类型分布.png` | **分组柱状图** - 对比各类别中直接带隙与间接带隙材料的数量 | 91 KB |2. 从 Materials Project API 获取数据

3. **BiVO₄** (2.40 eV) - 水氧化优异

4. **ZnO** (3.25 eV) - 高载流子迁移率| 图表 7 | `07_TOP材料性能热力图.png` | **热力图** - TOP 20光伏候选材料的4项关键性能指标标准化对比 | 411 KB |3. 生成 Excel 表格

5. **GaN** (3.30 eV) - 稳定性优异

| 图表 8 | `08_密度与带隙关系.png` | **散点图+回归线** - 分析材料密度与带隙的相关性，标注R²值 | 408 KB |4. 创建可视化 PDF 报告

## 🛠️ 技术细节



### 数据采集方法

### 4️⃣ 文档文件### 方法 2: 分步执行

```python

# 搜索策略：按化学体系精确搜索

chemical_systems = {

    "金属硫化物": ["Cd-S", "Zn-S", "Mo-S", ...],| 文件名 | 说明 | 大小 |如果需要分步执行，可以按以下顺序运行：

    "金属氧化物": ["Ti-O", "Zn-O", "W-O", ...],

    ...|--------|------|------|

}

| `项目完成总结.md` | **项目总结报告** - 包含数据统计、TOP 10材料推荐、技术细节 | 12 KB |```bash

# API调用流程

1. 按 chemical_system 搜索 → 获取 Materials ID 列表| `项目完成总结.pdf` | 总结报告的PDF版本，便于打印和分享 | 4.2 MB |# 步骤 1: 获取数据

2. 批量获取电子结构数据 → band_gap, cbm, vbm

3. 获取热力学数据 → formation_energy, e_above_hull| `可视化优化说明.md` | 可视化优化技术文档，记录字体问题解决方案和美化策略 | 8.5 KB |python fetch_semiconductor_data.py

4. 评估应用潜力 → 基于带隙和能带位置

5. 生成格式化 Excel → 自动排序、配色、调整列宽| `README.md` | **本文件** - 项目整体说明和文件索引 | - |

```

# 步骤 2: 生成可视化

### 可视化技术要点

---python visualize_data.py

**中文显示解决方案：**

```python```

# 直接指定Windows字体文件路径

font_path = r'C:\Windows\Fonts\msyh.ttc'  # 微软雅黑## 🎯 数据库指标说明

chinese_font = FontProperties(fname=font_path)

## 📦 依赖包

# 强制刷新字体缓存

fm._load_fontmanager(try_read_cache=False)### 核心性能指标（20项）



# 配置matplotlib全局字体以下 Python 包会被自动安装（如果缺失）：

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', ...]

plt.rcParams['axes.unicode_minus'] = False| 指标类别 | 具体指标 | 单位 | 说明 |

```

|---------|---------|------|------|```

**美化配置：**

- 🎨 10种材料类别专属配色（色盲友好）| **基本信息** | Materials ID | - | Materials Project唯一标识符 |requests          # HTTP 请求

- 📊 Seaborn专业学术风格（whitegrid）

- 🖼️ 300 DPI高分辨率输出| | 化学式 | - | 材料的化学组成 |pandas            # 数据处理

- 📐 网格、阴影、边框全面优化

- 📊 统计标注：样本数、R²值、趋势线| | 分类 | - | 10大类别（金属硫化物、氧化物等） |openpyxl          # Excel 文件读写



## 📦 依赖库| **电子结构** | 带隙 | eV | 禁带宽度 |matplotlib        # 数据可视化



```| | 直接带隙 | 是/否 | 是否为直接带隙半导体 |seaborn           # 高级可视化

requests>=2.28.0

pandas>=1.5.0| | 导带底 CBM | eV | 相对真空能级 |numpy             # 数值计算

openpyxl>=3.0.0

matplotlib>=3.7.0| | 价带顶 VBM | eV | 相对真空能级 |```

seaborn>=0.12.0

scipy>=1.9.0| | 费米能级 | eV | 费米能级位置 |

scikit-learn>=1.1.0

numpy>=1.23.0| **热力学稳定性** | 形成能 | eV/atom | 材料形成难易程度 |手动安装（可选）：

```

| | 能量高于凸包 | eV/atom | 热力学稳定性指标（<0.05 eV/atom为稳定） |```bash

## 📝 使用场景

| **物理性质** | 密度 | g/cm³ | 材料密度 |pip install requests pandas openpyxl matplotlib seaborn numpy

### 学术研究

- ✅ 论文配图（高清300 DPI，中文完美显示）| | 体积 | Ų | 晶胞体积 |```

- ✅ 材料筛选（根据带隙、稳定性等指标）

- ✅ 性能对比（多维度指标可视化）| **晶体结构** | 空间群 | - | 晶体对称性 |



### 教学演示| | 晶系 | - | 七大晶系分类 |## 📁 生成的文件

- ✅ 半导体物理课程教材配图

- ✅ 材料科学案例分析| **应用评估** | 光伏应用潜力 | 优秀/良好/一般/较低 | 基于带隙范围评估 |

- ✅ 数据科学实践项目

| | 光催化应用潜力 | 优秀/良好/一般/较低 | 基于能带位置评估 |运行完成后，会在当前目录生成以下文件：

### 工程应用

- ✅ 光伏材料选型参考| | 光电应用潜力 | 优秀/良好/一般/较低 | 综合评估 |

- ✅ 光催化剂设计指导

- ✅ 新材料开发数据库| 文件名 | 说明 |



## 🔄 项目更新---|--------|------|



### 更新数据| `半导体材料信息汇总.xlsx` | Excel 格式的完整数据表格 |

```bash

# 修改 API_KEY 后重新运行## 🔬 材料类别覆盖| `半导体材料信息汇总.json` | JSON 格式的数据备份 |

python 获取主流半导体材料数据.py

```| `半导体材料数据可视化.pdf` | 包含多个可视化图表的 PDF 报告 |



### 更新可视化| 类别 | 材料数量 | 代表性材料 | 典型带隙范围 |

```bash

# 基于最新数据重新生成图表|------|---------|-----------|------------|## 📈 可视化图表

python 数据可视化分析.py

```| 金属硫化物 | 18 | CdS, ZnS, MoS₂ | 0.8 - 3.5 eV |



### 自定义材料类别| 金属氧化物 | 14 | TiO₂, ZnO, WO₃ | 1.0 - 3.5 eV |PDF 报告包含以下图表：

编辑 `获取主流半导体材料数据.py` 中的 `MATERIAL_CATEGORIES` 字典：

| 氮化物 | 9 | GaN, AlN, InN | 0.7 - 6.0 eV |

```python

MATERIAL_CATEGORIES = {| 碳化物 | 8 | SiC, WC, TaC | 2.0 - 3.0 eV |1. **带隙对比图**：横向条形图，比较各材料的带隙大小

    "新类别名称": ["化学体系1", "化学体系2", ...],

    ...| 硒化物 | 7 | CdSe, ZnSe, MoSe₂ | 1.0 - 2.7 eV |2. **能带排列图**：显示价带和导带的能量位置

}

```| 碲化物 | 6 | CdTe, ZnTe, Bi₂Te₃ | 1.0 - 2.5 eV |3. **晶格参数对比**：散点图，显示 a、b、c 三个晶格参数



## 📄 数据来源与引用| 卤化物 | 5 | BiOCl, BiOBr, AgCl | 2.0 - 3.5 eV |4. **密度-体积关系图**：散点图，按带隙着色



**数据来源：** [Materials Project](https://materialsproject.org) (CC BY 4.0)| 磷化物 | 4 | GaP, InP, AlP | 1.4 - 2.5 eV |5. **稳定性分析图**：热力学稳定性对比



**引用建议：**| 砷化物 | 3 | GaAs, InAs, AlAs | 0.4 - 2.2 eV |6. **综合分析图**：包含晶系分布、数据摘要、带隙分布、稳定性统计

```

Jain, A., Ong, S. P., Hautier, G., Chen, W., Richards, W. D., Dacek, S., | 金属硫氧化物 | 2 | Bi₂S₂O₃ | 1.0 - 1.8 eV |

Cholia, S., Gunter, D., Skinner, D., Ceder, G., & Persson, K. A. (2013). 

Commentary: The Materials Project: A materials genome approach to ## 🔧 脚本说明

accelerating materials innovation. APL Materials, 1(1), 011002.

DOI: 10.1063/1.4812323**总计：** 76种材料

```

### 1. fetch_semiconductor_data.py

## 📧 联系方式

---

- **GitHub:** [@luffysolution-svg](https://github.com/luffysolution-svg)

- **项目仓库:** [semiconductor-materials-database](https://github.com/luffysolution-svg/semiconductor-materials-database)**功能**：从 Materials Project API 获取材料数据



## 📜 开源许可## 🚀 快速开始



本项目采用 MIT License - 详见 [LICENSE](LICENSE) 文件**主要函数**：



---### 1. 查看数据- `get_materials_data(formula)`: 根据化学式获取基本信息



## 🔧 故障排除- `get_electronic_structure(material_id)`: 获取电子结构（能带）



### 常见问题```bash- `get_crystal_structure(material_id)`: 获取晶体结构参数



**Q: API调用失败**# 打开Excel数据库（推荐）- `process_material_data(formula)`: 整合单个材料的完整数据

```

A: 请检查：start 主流半导体材料数据库.xlsx

   1. API Key 是否正确配置

   2. 网络连接是否正常**输出**：

   3. Materials Project 服务是否可用

```# 查看统计摘要- Excel 文件（包含所有数据）



**Q: 中文显示乱码**type 主流半导体材料数据摘要.txt- JSON 文件（数据备份）

```

A: 确保系统已安装中文字体：

   - Windows: 微软雅黑（msyh.ttc）

   - Linux: 需安装 fonts-wqy-microhei# 查看完整项目总结### 2. visualize_data.py

   - macOS: 可使用 PingFang SC

```start 项目完成总结.pdf



**Q: 图表生成失败**```**功能**：读取 Excel 数据并生成可视化图表

```

A: 检查是否已生成数据文件：

   - 主流半导体材料数据库.xlsx

   - 主流半导体材料数据库.json### 2. 重新获取数据**主要函数**：

```

- `plot_band_gap_comparison()`: 带隙对比

## 🎉 致谢

```bash- `plot_band_alignment()`: 能带排列

感谢 [Materials Project](https://materialsproject.org) 团队提供的优质材料数据库和API服务。

# 需要配置Materials Project API Key- `plot_crystal_parameters()`: 晶格参数

---

python 获取主流半导体材料数据.py- `plot_density_volume()`: 密度-体积关系

**最后更新：** 2025年10月6日  

**项目状态：** ✅ 生产就绪 (Production Ready)  ```- `plot_stability_analysis()`: 稳定性分析

**版本：** v1.0

- `plot_crystal_system_distribution()`: 晶系分布

**注意：** 需要在脚本中设置您的API Key：

```python**输出**：

API_KEY = "您的API密钥"  # 从 materialsproject.org 获取- PDF 文件（包含所有图表）

```

### 3. run_all.py

### 3. 生成可视化图表

**功能**：主控制脚本，自动化整个流程

```bash

# 生成全部8张图表（约15秒）**主要功能**：

python 数据可视化分析.py- 检查并安装依赖包

```- 顺序执行数据获取和可视化脚本

- 显示生成文件的摘要信息

**输出：** 8张高清PNG图表（300 DPI），中文完美显示，可直接用于论文。

## 🔑 API 密钥

---

本项目使用的 Materials Project API 密钥：

## 📈 推荐材料（TOP 10）```

8Fv89Xd3xCyJxw9oyc2srbKbHBqA9MGK

### 🌟 最佳光伏候选材料```



| 排名 | 材料 | 带隙 (eV) | 稳定性 | 带隙类型 | 优势 |**注意**：

|------|------|----------|--------|----------|------|- API 密钥已在脚本中配置

| 1 | **GaAs** | 1.42 | 高度稳定 | 直接 | 理想带隙 + 高效率 |- Materials Project API 是免费的学术资源

| 2 | **CdTe** | 1.48 | 高度稳定 | 直接 | 商用薄膜材料 |- 请遵守 API 使用限制（避免过于频繁的请求）

| 3 | **InP** | 1.35 | 高度稳定 | 直接 | 高迁移率 |

| 4 | **CdS** | 2.40 | 高度稳定 | 直接 | 窗口层材料 |## 📖 API 端点说明

| 5 | **GaP** | 2.26 | 高度稳定 | 间接 | 宽带隙半导体 |

本项目使用以下 API 端点：

### 🌟 最佳光催化候选材料

1. `/materials/summary/` - 获取材料基本信息

| 排名 | 材料 | 带隙 (eV) | CBM (eV) | VBM (eV) | 优势 |2. `/materials/electronic_structure/` - 获取电子结构

|------|------|----------|----------|----------|------|3. `/materials/core/` - 获取核心结构数据

| 1 | **TiO₂** | 3.20 | 0.20 | -3.00 | 经典光催化剂 |

| 2 | **WO₃** | 2.76 | -0.50 | -3.26 | 可见光响应 |详细文档：https://api.materialsproject.org/docs

| 3 | **BiVO₄** | 2.40 | 0.30 | -2.10 | 水氧化优异 |

| 4 | **ZnO** | 3.25 | 0.15 | -3.10 | 高载流子迁移率 |## ⚙️ 自定义配置

| 5 | **GaN** | 3.30 | 0.50 | -2.80 | 稳定性优异 |

### 修改材料列表

---

编辑 `fetch_semiconductor_data.py` 中的 `MATERIALS` 列表：

## 🛠️ 技术细节

```python

### 数据获取方法MATERIALS = [

    "ZnIn2S4",

```python    "C3N4",

# 搜索策略：按化学体系精确搜索    # 添加更多材料...

chemical_systems = {]

    "金属硫化物": ["Cd-S", "Zn-S", "Mo-S", ...],```

    "金属氧化物": ["Ti-O", "Zn-O", "W-O", ...],

    ...### 调整数据字段

}

修改 `_fields` 参数以获取更多或更少的字段：

# API调用流程

1. 按chemical_system搜索 → 获取Materials ID列表```python

2. 批量获取电子结构数据 → band_gap, cbm, vbmparams = {

3. 获取热力学数据 → formation_energy, e_above_hull    "_fields": "material_id,formula_pretty,band_gap,..."

4. 评估应用潜力 → 基于带隙和能带位置}

5. 生成格式化Excel → 自动排序、配色、调整列宽```

```

### 自定义可视化

### 可视化技术要点

在 `visualize_data.py` 中修改图表样式、颜色、字体等：

**中文显示解决方案：**

```python```python

# 直接指定Windows字体文件路径matplotlib.rcParams['font.size'] = 12  # 字体大小

font_path = r'C:\Windows\Fonts\msyh.ttc'  # 微软雅黑sns.set_style("whitegrid")              # 图表样式

chinese_font = FontProperties(fname=font_path)```



# 强制刷新字体缓存## 🐛 故障排除

fm._load_fontmanager(try_read_cache=False)

### 问题 1: API 请求失败

# 配置matplotlib全局字体

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', ...]**可能原因**：

plt.rcParams['axes.unicode_minus'] = False- 网络连接问题

```- API 密钥无效

- API 服务器临时不可用

**美化配置：**

- 🎨 10种材料类别专属配色（色盲友好）**解决方法**：

- 📊 Seaborn专业学术风格（whitegrid）- 检查网络连接

- 🖼️ 300 DPI高分辨率输出- 验证 API 密钥是否正确

- 📐 网格、阴影、边框全面优化- 稍后重试

- 📊 统计标注：样本数、R²值、趋势线

### 问题 2: 某些材料无数据

---

**可能原因**：

## 📦 依赖库- Materials Project 数据库中没有该材料

- 化学式书写格式不正确

```python

# 数据获取**解决方法**：

requests          # API调用- 在 Materials Project 网站搜索确认材料是否存在

pandas            # 数据处理- 尝试不同的化学式写法

openpyxl          # Excel读写

### 问题 3: 中文显示为方块

# 数据可视化

matplotlib >= 3.7 # 绘图核心**可能原因**：

seaborn >= 0.12   # 统计可视化- 系统缺少中文字体

scipy             # 统计分析

scikit-learn      # 数据标准化**解决方法**：

numpy             # 数值计算- Windows: 通常自带 SimHei 或 Microsoft YaHei

```- Linux: 安装中文字体包

- macOS: 系统自带中文字体

**安装命令：**

```bash## 📚 参考资料

pip install requests pandas openpyxl matplotlib seaborn scipy scikit-learn

```- [Materials Project 官方网站](https://materialsproject.org/)

- [Materials Project API 文档](https://api.materialsproject.org/docs)

---- [Python Requests 文档](https://requests.readthedocs.io/)

- [Pandas 文档](https://pandas.pydata.org/)

## 📝 使用场景- [Matplotlib 文档](https://matplotlib.org/)



### 学术研究## 📝 更新日志

- ✅ 论文配图（高清300 DPI，中文完美显示）

- ✅ 材料筛选（根据带隙、稳定性等指标）### v1.0.0 (2025-10-06)

- ✅ 性能对比（多维度指标可视化）- ✨ 初始版本发布

- 🎯 支持 11 种常见半导体材料查询

### 教学演示- 📊 自动生成 Excel 和 PDF 报告

- ✅ 半导体物理课程教材配图- 🚀 一键运行功能

- ✅ 材料科学案例分析- 📖 完整的文档说明

- ✅ 数据科学实践项目

## 📄 许可证

### 工程应用

- ✅ 光伏材料选型参考本项目仅用于学术研究和教育目的。

- ✅ 光催化剂设计指导

- ✅ 新材料开发数据库Materials Project 数据遵循其官方使用条款。



---## 👤 作者



## 📄 版权声明Created with Materials Project API



- **数据来源：** [Materials Project](https://materialsproject.org) (CC BY 4.0)## 🙏 致谢

- **脚本作者：** Luffy.Solution

- **创建日期：** 2025年10月6日感谢 Materials Project 团队提供的优秀数据库和 API 服务。

- **许可协议：** 本项目代码和文档采用 MIT License

**引用建议：**
> Materials Project Database: A. Jain et al., APL Materials 1, 011002 (2013).
> DOI: 10.1063/1.4812323

---

## 📧 联系方式

如有问题或建议，请通过以下方式联系：

- **GitHub:** luffysolution-svg
- **项目仓库:** [materials-project-api-docs](https://github.com/luffysolution-svg/materials-project-api-docs)

---

## 🔄 更新日志

### v3.0 (2025-10-06) - 终极版
- ✅ **彻底解决中文乱码问题** - 直接使用系统字体文件路径
- ✅ 强制刷新字体缓存，多重保险配置
- ✅ 所有图表文件名简化，去除版本后缀
- ✅ 项目文件完整整理，删除旧版本
- ✅ 创建完整的项目README文档

### v2.0 (2025-10-06) - 美化版
- ✅ 专业学术配色方案
- ✅ 增强统计信息和趋势分析
- ✅ 300 DPI高分辨率输出
- ✅ 8种高级图表类型

### v1.0 (2025-10-06) - 初始版
- ✅ 完成76种材料数据采集
- ✅ 生成Excel数据库和JSON数据
- ✅ 创建8张基础可视化图表

---

**最后更新：** 2025年10月6日  
**项目状态：** ✅ 生产就绪 (Production Ready)

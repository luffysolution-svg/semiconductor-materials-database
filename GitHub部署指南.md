# GitHub 部署指南

## 📝 部署步骤

### 1. 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name:** `semiconductor-materials-database`
   - **Description:** 主流半导体材料数据库 - 基于Materials Project API的自动化数据采集与可视化分析工具
   - **Visibility:** Public
   - ⚠️ **不要勾选** "Initialize this repository with:"
     - 不要添加 README
     - 不要添加 .gitignore
     - 不要添加 license
3. 点击 **"Create repository"**

### 2. 推送代码到 GitHub

创建仓库后，在PowerShell中执行：

```powershell
cd "H:\material project\半导体信息查询"
.\执行推送.ps1
```

或者手动执行：

```powershell
cd "H:\material project\半导体信息查询"

# 添加远程仓库
git remote add origin https://github.com/luffysolution-svg/semiconductor-materials-database.git

# 推送代码
git branch -M main
git push -u origin main
```

### 3. 验证部署

访问仓库地址确认文件已上传：
https://github.com/luffysolution-svg/semiconductor-materials-database

应该看到以下文件：
- ✅ README.md
- ✅ LICENSE
- ✅ requirements.txt
- ✅ .gitignore
- ✅ 获取主流半导体材料数据.py
- ✅ 数据可视化分析.py

## 📂 项目结构

```
semiconductor-materials-database/
│
├── .gitignore                    # Git忽略规则
├── LICENSE                       # MIT许可证
├── README.md                     # 项目说明文档
├── requirements.txt              # Python依赖
├── 获取主流半导体材料数据.py      # 数据采集脚本
└── 数据可视化分析.py              # 可视化脚本
```

## 🔄 后续更新流程

### 更新代码

1. 修改文件（Python脚本或文档）
2. 提交更改：
   ```powershell
   git add .
   git commit -m "描述你的更改"
   git push
   ```

### 更新数据

⚠️ **注意：** 生成的数据文件（.xlsx, .json, .png等）不会上传到GitHub

- 这些文件已在 `.gitignore` 中排除
- 用户需要自行运行脚本生成数据
- 这样可以保持仓库轻量化

### 添加新功能

1. 创建新分支：
   ```powershell
   git checkout -b feature/新功能名称
   ```

2. 进行开发并测试

3. 提交并推送：
   ```powershell
   git add .
   git commit -m "添加新功能：描述"
   git push origin feature/新功能名称
   ```

4. 在GitHub上创建Pull Request

## 🏷️ 版本管理

### 创建版本标签

```powershell
# 创建标签
git tag -a v1.0 -m "Release version 1.0"

# 推送标签
git push origin v1.0
```

### 查看版本历史

```powershell
git log --oneline --graph --all
```

## 📊 GitHub Pages（可选）

如果想要创建项目网站：

1. 进入仓库 Settings
2. 找到 "Pages" 部分
3. Source 选择 "Deploy from a branch"
4. Branch 选择 "main" 和 "/ (root)"
5. 保存

网站地址将是：
https://luffysolution-svg.github.io/semiconductor-materials-database/

## 🛡️ 保护主分支（推荐）

1. 进入仓库 Settings → Branches
2. 添加分支保护规则
3. 分支名称模式：`main`
4. 启用：
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass before merging

## 📧 问题反馈

遇到问题？
- 在仓库中创建 Issue
- 或联系：GitHub @luffysolution-svg

## ✅ 检查清单

部署前确认：
- [ ] 已创建 GitHub 仓库
- [ ] Git 已正确配置（用户名和邮箱）
- [ ] 本地代码已提交
- [ ] 远程仓库地址正确
- [ ] 网络连接正常

部署后确认：
- [ ] README.md 在 GitHub 上正确显示
- [ ] 所有代码文件已上传
- [ ] .gitignore 正常工作（数据文件未上传）
- [ ] LICENSE 文件存在

## 🎉 完成！

部署成功后，您的项目将：
- ✅ 在 GitHub 上公开可访问
- ✅ 拥有完整的版本历史
- ✅ 支持协作开发
- ✅ 便于分享和引用

---

**创建日期：** 2025年10月6日  
**最后更新：** 2025年10月6日

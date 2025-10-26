# Satpy 中文文档

本目录包含 Satpy 项目文档的中文翻译。

## 目录结构

```
doc_zh/
├── Makefile                    # 文档构建 Makefile（已翻译）
├── README                      # README 文件（已翻译）
├── rtd_environment.yml         # Read the Docs 环境配置
└── source/                     # 文档源文件
    ├── index.rst               # 主索引页面（已翻译）
    ├── overview.rst            # 概述（已翻译）
    ├── install.rst             # 安装说明（已翻译）
    ├── quickstart.rst          # 快速入门（已翻译）
    ├── config.rst              # 配置（已翻译）
    ├── data_download.rst       # 数据下载（已翻译）
    ├── reading.rst             # 读取数据（已翻译）
    ├── remote_reading.rst      # 远程读取（已翻译）
    ├── composites.rst          # 合成图像（已翻译）
    ├── modifiers.rst           # 修饰符（已翻译）
    ├── resample.rst            # 重采样（已翻译）
    ├── enhancements.rst        # 增强（已翻译）
    ├── writing.rst             # 写入数据（已翻译）
    ├── multiscene.rst          # MultiScene（已翻译）
    ├── readers_formats.rst     # 读取器和格式（已翻译）
    ├── faq.rst                 # 常见问题（已翻译）
    ├── conf.py                 # Sphinx 配置文件
    ├── docutils.conf           # Docutils 配置
    ├── doi_role.py             # DOI 角色扩展
    ├── reader_table.py         # 读取器表生成器
    ├── generate_area_def_list.py  # 区域定义列表生成器
    ├── _static/                # 静态文件
    │   ├── main.js
    │   └── theme_overrides.css
    ├── api/                    # API 文档（自动生成）
    ├── dev_guide/              # 开发者指南
    │   ├── index.rst           # 开发者指南索引（已翻译）
    │   ├── CONTRIBUTING.rst    # 贡献指南（已翻译）
    │   ├── xarray_migration.rst  # XArray 迁移（已翻译）
    │   ├── custom_reader.rst   # 自定义读取器（已翻译）
    │   ├── remote_file_support.rst  # 远程文件支持（已翻译）
    │   ├── plugins.rst         # 插件（已翻译）
    │   ├── satpy_internals.rst # Satpy 内部（已翻译）
    │   ├── aux_data.rst        # 辅助数据（已翻译）
    │   ├── writing_tests.rst   # 编写测试（已翻译）
    │   └── testing.rst         # 测试（已翻译）
    └── examples/               # 示例
        ├── index.rst           # 示例索引（已翻译）
        ├── fci_l1c_natural_color.rst  # FCI 自然彩色示例（已翻译）
        └── vii_l1b_nc.rst      # VII NetCDF 示例（已翻译）
```

## 构建文档

### 环境准备

在构建文档之前，需要安装必要的依赖项。

#### 1. 创建文档构建环境（推荐）

使用 conda 创建独立的文档构建环境：

```bash
# 创建新的 conda 环境
conda create -n satpy-docs python=3.11
conda activate satpy-docs

# 安装 Sphinx 和相关依赖
conda install -c conda-forge sphinx sphinx_rtd_theme sphinx-autodoc-typehints
```

或者使用项目提供的环境配置文件：

```bash
# 使用 rtd_environment.yml 创建环境
conda env create -f rtd_environment.yml -n satpy-docs
conda activate satpy-docs
```

#### 2. 使用 pip 安装依赖

如果使用 pip，可以安装以下必要的包：

```bash
pip install sphinx sphinx_rtd_theme sphinx-autodoc-typehints
```

#### 3. 安装 Satpy

为了生成 API 文档，需要安装 Satpy：

```bash
# 在文档环境中安装 Satpy
cd e:\projects\satpy
pip install -e .
```

### 构建 HTML 文档

环境准备完成后，在 `doc_zh` 目录中运行：

**使用 Makefile（推荐）：**

```bash
cd doc_zh
make html
```

**或者直接使用 sphinx-build：**

```bash
cd doc_zh
sphinx-build -b html source build/html
```

**在 Windows PowerShell 中：**

```powershell
cd doc_zh
.\make.bat html
```

生成的 HTML 文档将位于 `doc_zh/build/html` 目录中。

### 查看生成的文档

构建完成后，可以在浏览器中打开文档：

**Windows:**
```bash
# 打开主页
start build/html/index.html
```

**Linux/Mac:**
```bash
# 打开主页
open build/html/index.html  # Mac
xdg-open build/html/index.html  # Linux
```

### 清理构建文件

如果需要清理之前的构建结果，重新构建：

```bash
cd doc_zh
make clean
make html
```

### 常见问题

**问题 1: 缺少模块错误**

如果构建时出现 `ModuleNotFoundError`，请确保：
- 已激活正确的 conda/virtualenv 环境
- 已安装所有必要的依赖包
- 已安装 Satpy 本身

**问题 2: 编码错误**

确保系统支持 UTF-8 编码。在 Windows 上可能需要设置：
```bash
set PYTHONIOENCODING=utf-8
```

**问题 3: Sphinx 版本不兼容**

本文档需要 Sphinx >= 8.2.0。可以通过以下命令检查版本：
```bash
sphinx-build --version
```

如需升级：
```bash
pip install --upgrade sphinx
```

## 翻译说明

本翻译涵盖了 Satpy 文档的主要部分：

1. **主要用户文档**：安装、快速入门、配置、数据处理等
2. **开发者指南**：贡献指南、测试、插件开发等
3. **示例**：实际使用示例

配置文件（如 conf.py、docutils.conf 等）和 Python 脚本保持原样，因为它们主要是代码而非文档。

## 注意事项

- API 文档在构建时自动从源代码生成，无需翻译
- 某些技术术语保持英文以保持一致性
- 代码示例保持英文以确保可运行性
- 链接到外部资源保持原样

## 贡献

如果您发现翻译错误或有改进建议，欢迎提交 PR 或创建 Issue。

## 许可证

本翻译遵循与 Satpy 项目相同的许可证。

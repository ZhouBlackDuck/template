## 📂 项目结构

```
template/
├── 📁 conf/                    # ⚙️ Hydra 配置文件
│   ├── config.yaml             # 主配置文件
│   ├── 📁 model/               # 模型配置
│   ├── 📁 data/                # 数据集配置
│   ├── 📁 optimizer/           # 优化器配置
│   ├── 📁 trainer/             # Trainer 配置
│   ├── 📁 logger/              # Logger 配置
│   ├── 📁 train/               # 训练参数
│   └── 📁 custom/              # 自定义脚本配置
│
├── 📁 src/                     # 💻 源代码
│   ├── train.py                # 训练入口
│   ├── 📁 models/              # 模型定义
│   ├── 📁 datasets/            # 数据模块
│   └── 📁 utils/               # 工具函数
│
├── 📁 data/                    # 📊 数据集目录
├── 📁 outputs/                 # 📤 输出目录
└── 📄 requirements.txt         # 依赖列表
```

---

## 🛠️ 安装

### 1️⃣ 克隆仓库

```bash
git clone <repo-url>
cd template
```

### 2️⃣ 创建虚拟环境（推荐）

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

---

## 🚀 快速开始

### 🏋️ 训练模型

```bash
cd src
python train.py
```

---

## ⚙️ 配置系统

本项目使用 **Hydra** 进行配置管理，支持灵活的配置组合和命令行覆盖。

### 📝 主配置文件

```yaml
# conf/config.yaml
defaults:
  - model: mlp           # 模型配置
  - data: mnist          # 数据集配置
  - optimizer: adam      # 优化器配置
  - logger: tensorboard  # 日志记录器
  - trainer: default     # Trainer 配置
  - train: default       # 训练参数
  - custom: default      # 自定义脚本配置

seed: 42                 # 随机种子
```

### 🔄 命令行覆盖参数

```bash
# 修改单个参数
python train.py trainer.max_epochs=50

# 修改多个参数
python train.py optimizer.lr=0.0001 data.batch_size=128

# 切换配置组
python train.py model=mlp data=mnist

# 组合使用
python train.py trainer.max_epochs=100 optimizer.lr=0.0005 seed=123
```

---

## 📊 查看训练日志

使用 TensorBoard 可视化训练过程：

```bash
tensorboard --logdir outputs/train/
```

然后在浏览器访问 `http://localhost:6006` 🌐

---

## 🔧 扩展指南

### 📦 添加新模型

1️⃣ 在 `src/models/` 下创建模型文件：

```python
# src/models/my_model.py
import pytorch_lightning as pl


class MyModel(pl.LightningModule):
    def __init__(self, **kwargs):
        super().__init__()
        # 定义模型结构
        ...
    
    def forward(self, x):
        ...
    
    def training_step(self, batch, batch_idx):
        ...
    
    def configure_optimizers(self):
        ...
```

2️⃣ 创建配置文件 `conf/model/my_model.yaml`：

```yaml
_target_: models.my_model.MyModel

# 模型参数
param1: value1
param2: value2
```

3️⃣ 使用新模型训练：

```bash
python train.py model=my_model
```

### 📊 添加新数据集

1️⃣ 在 `src/datasets/` 下创建数据模块：

```python
# src/datasets/my_data.py
import pytorch_lightning as pl


class MyDataModule(pl.LightningDataModule):
    def __init__(self, **kwargs):
        super().__init__()
        ...
    
    def prepare_data(self):
        # 下载数据
        ...
    
    def setup(self, stage=None):
        # 设置数据集
        ...
    
    def train_dataloader(self):
        ...
    
    def val_dataloader(self):
        ...
```

2️⃣ 创建配置文件 `conf/data/my_data.yaml`

---

## 💡 提示

- 📝 通过 `--cfg job` 查看完整配置：`python train.py --cfg job`
- 🔍 使用 `--help` 查看所有可用配置选项
- 💾 检查点路径支持相对路径和绝对路径

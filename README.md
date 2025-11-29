# 🚀 PyTorch Lightning + Hydra 深度学习模板

一个现代化的深度学习项目模板，集成 **PyTorch Lightning** 训练框架和 **Hydra** 配置管理系统。

---

## ✨ 特性

- 🔧 **Hydra 配置管理** - 灵活的分层配置系统，支持命令行覆盖
- ⚡ **PyTorch Lightning** - 简洁优雅的训练代码，自动处理分布式训练
- 📊 **TensorBoard 集成** - 实时监控训练指标和可视化
- 🎯 **组件注册系统** - 轻松扩展新的模型和数据集
- 🌱 **可复现性** - 全局随机种子控制
- 📁 **规范化目录结构** - 输出按时间戳自动组织

---

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
│   ├── 📁 eval/                # 评估参数
│   └── 📁 infer/               # 推理参数
│
├── 📁 src/                     # 💻 源代码
│   ├── train.py                # 训练入口
│   ├── eval.py                 # 评估入口
│   ├── infer.py                # 推理入口
│   ├── 📁 models/              # 模型定义
│   ├── 📁 datamodules/         # 数据模块
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

### 📊 评估模型

```bash
cd src
python eval.py eval.ckpt_path=<checkpoint_path>
```

### 🔮 模型推理

```bash
cd src
python infer.py infer.ckpt_path=<checkpoint_path>
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
  - eval: default        # 评估参数
  - infer: default       # 推理参数

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

### 📋 常用配置项

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `seed` | 随机种子 | `42` |
| `trainer.max_epochs` | 最大训练轮数 | `20` |
| `trainer.accelerator` | 加速器类型 | `gpu` |
| `trainer.devices` | 设备数量 | `1` |
| `optimizer.lr` | 学习率 | `1e-3` |
| `data.batch_size` | 批次大小 | `64` |
| `data.num_workers` | 数据加载进程数 | `4` |

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
from utils.registry import model

@model  # 使用装饰器注册模型
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

2️⃣ 在 `src/models/__init__.py` 中导入：

```python
from .my_model import MyModel
```

3️⃣ 创建配置文件 `conf/model/my_model.yaml`：

```yaml
type: MyModel

# 模型参数
param1: value1
param2: value2
```

4️⃣ 使用新模型训练：

```bash
python train.py model=my_model
```

### 📊 添加新数据集

1️⃣ 在 `src/datamodules/` 下创建数据模块：

```python
# src/datamodules/my_data.py
import pytorch_lightning as pl
from utils.registry import data

@data  # 使用装饰器注册数据模块
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

2️⃣ 在 `src/datamodules/__init__.py` 中导入

3️⃣ 创建配置文件 `conf/data/my_data.yaml`

---

## 📁 输出目录结构

每次运行会在 `outputs/` 下自动创建按时间戳命名的目录：

```
outputs/
├── 📁 train/{timestamp}/
│   ├── train.log                    # 训练日志
│   └── lightning_logs/version_0/
│       ├── checkpoints/             # 模型检查点
│       ├── events.out.tfevents.*    # TensorBoard 事件
│       └── hparams.yaml             # 超参数记录
│
├── 📁 eval/{timestamp}/             # 评估输出
└── 📁 infer/{timestamp}/            # 推理输出
```

---

## 🔗 技术栈

| 组件 | 版本 | 用途 |
|------|------|------|
| 🔥 PyTorch | 2.9.1 | 深度学习框架 |
| ⚡ PyTorch Lightning | 2.6.0 | 训练框架 |
| 🔧 Hydra | 1.3.2 | 配置管理 |
| 📊 TensorBoard | 2.20.0 | 可视化工具 |
| 📏 TorchMetrics | 1.8.2 | 评估指标 |

---

## 💡 提示

- 🔄 使用 `trainer.accelerator=cpu` 在无 GPU 环境下运行
- 📝 通过 `--cfg job` 查看完整配置：`python train.py --cfg job`
- 🔍 使用 `--help` 查看所有可用配置选项
- 💾 检查点路径支持相对路径和绝对路径

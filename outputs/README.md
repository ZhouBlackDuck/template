# 📤 输出目录

此目录用于存放项目运行过程中产生的**所有输出文件**。

---

## 🗂️ 目录结构

```
outputs/
├── 📁 train/                           # 🏋️ 训练输出
│   └── 📁 {timestamp}/                 # 按时间戳组织的运行记录
│       ├── 📄 train.log                # hydra训练脚本日志
│       └── 📁 lightning_logs/          # PyTorch Lightning 日志
│           └── 📁 version_0/
│               ├── 📁 checkpoints/     # 💾 模型检查点
│               │   └── epoch=X-step=Y.ckpt
│               ├── 📄 events.out.tfevents.*  # 📊 TensorBoard 事件
│               └── 📄 hparams.yaml     # ⚙️ 超参数配置
│
├── 📁 eval/                            # 📊 评估输出
│   └── 📁 {timestamp}/
│       ├── 📄 eval.log                 # hydra评估脚本日志
│       └── 📁 lightning_logs/
│           └── 📁 version_0/
│               ├── 📄 events.out.tfevents.*
│               └── 📄 hparams.yaml
│
├── 📁 infer/                           # 🔮 推理输出
│   └── 📁 {timestamp}/
│       ├── 📄 infer.log                # hydra推理脚本日志
│       └── 📁 lightning_logs/
│           └── 📁 version_0/
│               ├── 📄 events.out.tfevents.*
│               └── 📄 hparams.yaml
│
└── 📄 README.md
```

---

## 📋 文件说明

| 文件类型 | 说明 | 用途 |
|---------|------|------|
| 📄 `*.log` | 运行日志 | 记录详细的运行信息和输出 |
| 💾 `*.ckpt` | 模型检查点 | 保存训练好的模型权重，用于恢复训练或推理 |
| 📊 `events.out.tfevents.*` | TensorBoard 事件 | 可视化训练指标曲线 |
| ⚙️ `hparams.yaml` | 超参数 | 记录本次运行使用的配置参数 |

---

## 🔍 查看 TensorBoard 日志

启动 TensorBoard 来可视化训练过程：

```bash
# 查看所有训练日志
tensorboard --logdir outputs/train/

# 查看特定运行的日志
tensorboard --logdir outputs/train/{timestamp}/lightning_logs/
```

然后在浏览器中访问 `http://localhost:6006` 🌐

---

## 💡 使用提示

- ⏰ 每次运行会自动创建以**时间戳**命名的新目录
- 🔄 时间戳格式: `YYYY-MM-DDTHH-MM-SS`
- 📂 不同任务类型的输出会分别存放在 `train/`、`eval/`、`infer/` 目录下

---

## ⚠️ 注意事项

> 💾 此目录下的输出文件通常**不应提交到版本控制系统**，请确保已添加到 `.gitignore`
>
> 🗑️ 定期清理旧的输出文件以节省磁盘空间

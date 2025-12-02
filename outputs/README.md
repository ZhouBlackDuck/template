# 📤 输出目录

此目录用于存放项目运行过程中产生的**所有输出文件**。

---

## 🗂️ 目录结构

```
outputs/
├── 📁 train/                           # 🏋️ 训练输出
│   ├── 📁 {timestamp}/                 # 按时间戳组织的运行记录
│   │   ├── 📁 .hydra/                  # hydra任务运行配置
│   │   ├── 📄 train.log                # hydra日志
│   │   └── 📁 lightning_logs/          # PyTorch Lightning 日志
│   │       └── 📁 {version}/
│   │           ├── 📁 checkpoints/     # 💾 模型检查点
│   │           │   └── epoch=X-step=Y.ckpt
│   │           ├── 📄 events.out.tfevents.*  # 📊 TensorBoard 事件
│   │           └── 📄 hparams.yaml     # ⚙️ 超参数配置
│   │
│   └── 📁 {timestamp}/
│       ├── 📁 .hydra/
│       ├── 📄 train.log
│       └── 📄 model.pkl                # scikit learn模型
│
├── 📁 {task}/
└── 📄 README.md
```

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

---

## ⚠️ 注意事项

> 💾 此目录下的输出文件通常**不应提交到版本控制系统**，请确保已添加到 `.gitignore`
>
> 🗑️ 定期清理旧的输出文件以节省磁盘空间

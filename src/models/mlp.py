import pytorch_lightning as pl
import torch
import torch.nn.functional as f
from torch import nn
from torchmetrics import Accuracy

from utils.registry import model


@model
class MNISTClassifier(pl.LightningModule):
    """简单的 MLP 模型用于 MNIST 手写数字识别
    
    这是一个经典的深度学习 Hello World 示例。
    网络结构：784 -> 256 -> 128 -> 10
    
    Args:
        hidden_dim1: 第一个隐藏层的维度
        hidden_dim2: 第二个隐藏层的维度
        lr: 学习率
        dropout: Dropout 概率
    """

    def __init__(
            self,
            input_dim=784,
            hidden_dim1=256,
            hidden_dim2=128,
            dropout=0.2,
            **kwargs
    ):
        super().__init__()
        self.optimizer = kwargs.pop('optimizer', {})

        # 定义网络层
        self.layers = nn.Sequential(
            nn.Flatten(),  # 将 28x28 的图像展平为 784 维向量
            nn.Linear(input_dim, hidden_dim1),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim1, hidden_dim2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim2, 10)  # 10 个类别（0-9）
        )

        # 定义准确率指标
        self.train_acc = Accuracy(task="multiclass", num_classes=10)
        self.val_acc = Accuracy(task="multiclass", num_classes=10)

    def forward(self, x):
        """前向传播"""
        return self.layers(x)

    def training_step(self, batch, batch_idx):
        """训练步骤"""
        x, y = batch
        logits = self(x)
        loss = f.cross_entropy(logits, y)

        # 计算准确率
        preds = torch.argmax(logits, dim=1)
        acc = self.train_acc(preds, y)

        # 记录指标
        self.log("train_loss", loss, prog_bar=True, on_step=False, on_epoch=True)
        self.log("train_acc", acc, prog_bar=True, on_step=False, on_epoch=True)

        return loss

    def validation_step(self, batch, batch_idx):
        """验证步骤"""
        x, y = batch
        logits = self(x)
        loss = f.cross_entropy(logits, y)

        # 计算准确率
        preds = torch.argmax(logits, dim=1)
        acc = self.val_acc(preds, y)

        # 记录指标
        self.log("val_loss", loss, prog_bar=True)
        self.log("val_acc", acc, prog_bar=True)

    def predict_step(self, batch, batch_idx):
        """预测步骤"""
        x, y = batch
        logits = self(x)
        return torch.argmax(logits, dim=1)

    def configure_optimizers(self):
        """配置优化器"""
        optimizer = torch.optim.Adam(
            self.parameters(),
            lr=self.optimizer['lr']
        )

        # 使用学习率调度器
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer,
            factor=self.optimizer['scheduler']['factor'],
            patience=self.optimizer['scheduler']['patience']
        )

        return {
            "optimizer": optimizer,
            "lr_scheduler": {
                "scheduler": scheduler,
                "monitor": "val_loss",
            }
        }

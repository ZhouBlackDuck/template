from pathlib import Path

import numpy as np
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from torchvision import transforms, datasets

from utils.mixins import NumpyMixin


class MNISTDataModule(pl.LightningDataModule, NumpyMixin):
    """MNIST 手写数字数据模块
    
    Args:
        data_dir: 数据存储目录
        batch_size: 批次大小
        num_workers: 数据加载的工作进程数
    """

    def __init__(self, data_dir=Path(__file__).parents[2] / "data", batch_size=64, num_workers=4):
        super().__init__()
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.num_workers = num_workers

        # MNIST 数据预处理：归一化到 [0, 1] 然后标准化
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))  # MNIST 数据集的均值和标准差
        ])
        self.train_ds = None
        self.val_ds = None
        self.predict_ds = None
        self.test_ds = None

    def prepare_data(self):
        """下载数据集（仅在主进程执行一次）"""
        datasets.MNIST(self.data_dir, train=True, download=True)
        datasets.MNIST(self.data_dir, train=False, download=True)

    def setup(self, stage=None):
        """设置训练集和验证集"""
        if stage == "fit" or stage is None:
            self.train_ds = datasets.MNIST(
                self.data_dir,
                train=True,
                transform=self.transform
            )
            self.val_ds = datasets.MNIST(
                self.data_dir,
                train=False,
                transform=self.transform
            )

        if stage == "validate":
            self.val_ds = datasets.MNIST(
                self.data_dir,
                train=False,
                transform=self.transform
            )

        if stage == "predict":
            self.predict_ds = datasets.MNIST(
                self.data_dir,
                train=False,
                transform=self.transform
            )

        if stage == "test":
            self.test_ds = datasets.MNIST(
                self.data_dir,
                train=False,
                transform=self.transform
            )

    def train_dataloader(self):
        """训练数据加载器"""
        return DataLoader(
            self.train_ds,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            shuffle=True,
            persistent_workers=True if self.num_workers > 0 else False
        )

    def val_dataloader(self):
        """验证数据加载器"""
        return DataLoader(
            self.val_ds,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            persistent_workers=True if self.num_workers > 0 else False
        )

    def predict_dataloader(self):
        """预测数据加载器"""
        return DataLoader(
            self.predict_ds,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            persistent_workers=True if self.num_workers > 0 else False
        )

    def test_dataloader(self):
        """测试数据加载器"""
        return DataLoader(
            self.test_ds,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            persistent_workers=True if self.num_workers > 0 else False
        )

    def to_numpy(self, stage=None):
        samples = []
        labels = []
        self.setup(stage)
        if stage == "fit":
            for x, y in self.train_dataloader():
                samples.append(x.view(x.size(0), -1).numpy())
                labels.append(y.numpy())
            samples = np.concatenate(samples, axis=0)
            labels = np.concatenate(labels, axis=0)
        elif stage == "test":
            for x, y in self.test_dataloader():
                samples.append(x.view(x.size(0), -1).numpy())
                labels.append(y.numpy())
            samples = np.concatenate(samples, axis=0)
            labels = np.concatenate(labels, axis=0)
        return {
            "X": samples,
            "y": labels
        }

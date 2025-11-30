import os
from pathlib import Path

import hydra
from omegaconf import DictConfig, open_dict
from pytorch_lightning import seed_everything, Trainer

# noinspection PyUnresolvedReferences
import datamodules
# noinspection PyUnresolvedReferences
import models
from utils.registry import get_data, get_model


# noinspection DuplicatedCode
@hydra.main(config_path="../conf", config_name="config", version_base="1.3")
def main(cfg: DictConfig):
    # 模型
    with open_dict(cfg):
        model_class = get_model(cfg.model.pop("type"))
    model = model_class(**cfg.model)

    # Optimizer
    optimizer = hydra.utils.instantiate(cfg.optimizer)
    model.set_optimizer(optimizer)

    # 数据集
    with open_dict(cfg):
        data_class = get_data(cfg.data.pop("type"))
    dm = data_class(**cfg.data)

    # Logger
    logger = hydra.utils.instantiate(cfg.logger)

    # Trainer
    seed_everything(cfg.seed, workers=True)
    trainer = Trainer(logger=logger, **cfg.trainer)

    # 验证
    trainer.validate(model, dm, **cfg.eval)


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    main()

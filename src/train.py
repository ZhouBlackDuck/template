import os
from pathlib import Path

import hydra
import joblib
from omegaconf import DictConfig, open_dict
from pytorch_lightning import seed_everything, Trainer


def deep_learning(model, dm, cfg):
    # Optimizer
    optimizer = hydra.utils.instantiate(cfg.optimizer)
    model.set_optimizer(optimizer)

    # Logger
    logger = hydra.utils.instantiate(cfg.logger)

    # Trainer
    trainer = Trainer(logger=logger, **cfg.trainer)

    # 训练
    trainer.fit(model, dm, **cfg.train)


def machine_learning(model, dm, cfg):
    model.fit(**dm.to_numpy(stage="fit"), **cfg.train)
    joblib.dump(model, "model.pkl")


@hydra.main(config_path="../conf", config_name="config", version_base="1.3")
def main(cfg: DictConfig):
    # Seed
    seed_everything(cfg.seed, workers=True)

    # 加载模型
    model = hydra.utils.instantiate(cfg.model)

    # 加载数据集
    dm = hydra.utils.instantiate(cfg.data)

    with open_dict(cfg):
        task = cfg.pop('task')
        customize = cfg.pop('customize')
        custom = cfg.pop('custom')

    if task == "dl":
        script = deep_learning
    elif task == "ml":
        script = machine_learning
    else:
        raise ValueError(f"Unknown task: {cfg.task}")
    if customize:
        script = hydra.utils.instantiate(custom)

    script(model, dm, cfg)


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    main()

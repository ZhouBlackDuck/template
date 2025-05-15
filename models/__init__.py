"""
深度学习模型
"""

from abstracts.model import AbstractModel
from configs.parser import ConfigParser
from typings.model import Model


class ModelFactory:
    @staticmethod
    def create_model(name: str = None, **kwargs) -> AbstractModel:
        """
        Creates a model based on the provided model name and arguments.

        Args:
            name (str): Name of the model to create.
            kwargs (dict): Arguments for the model.
        """
        if name is None:
            raise ValueError("Model name must be specified")
        else:
            raise ValueError(f"Unknown Model: {name}")


ConfigParser().parser.add_argument('--model', type=Model)

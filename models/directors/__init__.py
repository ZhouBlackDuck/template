"""
模型专用数据集指令器
"""

from abstracts.director import ModelDatasetDirector


class ModelDatasetDirectorFactory:

    @staticmethod
    def create_director(*, name: str = None, **_) -> ModelDatasetDirector:
        """
        Creates a model dataset director based on the provided model name.

        Args:
            name (str): Name of the model to create a director for.
        """
        if name is None:
            raise ValueError("Model name must be specified")
        else:
            raise ValueError(f"Unknown Model: {name}")

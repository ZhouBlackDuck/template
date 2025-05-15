"""
数据集构建器
"""

from abstracts.builder import DatasetBuilder


class DatasetBuilderFactory:

    @staticmethod
    def create_builder(name: str = None, **kwargs) -> DatasetBuilder:
        """
        Creates a dataset builder based on the provided dataset name and arguments.

        Args:
            name (str): Name of the dataset to create a builder for.
            kwargs (dict): Arguments for the dataset builder.
        """
        if name is None:
            raise ValueError("Dataset name must be provided.")
        else:
            raise ValueError(f"Unknown dataset: {name}")

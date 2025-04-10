from typing import Dict

from abstracts import DatasetBuilder


class DatasetBuilderFactory:

    @staticmethod
    def create_builder(dataset: str = None, kwargs: Dict = None) -> DatasetBuilder:
        """
        Creates a dataset builder based on the provided dataset name and arguments.

        Args:
            dataset (str): Name of the dataset to create a builder for.
            kwargs (dict): Arguments for the dataset builder.
        """
        if dataset is None:
            raise ValueError("Dataset name must be provided.")
        else:
            raise ValueError(f"Unknown dataset: {dataset}")

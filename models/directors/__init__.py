from abstracts import ModelDatasetDirector


class ModelDatasetDirectorFactory:

    @staticmethod
    def create_director(subcommand: str = None) -> ModelDatasetDirector:
        """
        Creates a model dataset director based on the provided subcommand and arguments.

        Args:
            subcommand (str): Name of the model to create a director for.
        """
        if subcommand is None:
            raise ValueError("Model Subcommand must be specified")
        else:
            raise ValueError(f"Unknown Model: {subcommand}")

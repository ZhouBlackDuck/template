from typing import Dict

from jsonargparse import ArgumentParser

from abstracts import AbstractModel
from models.directors import *
from modules import ConfigParser


class ModelFactory:
    @staticmethod
    def create_model(subcommand: str = None, kwargs: Dict = None) -> AbstractModel:
        """
        Creates a model based on the provided subcommand and arguments.

        Args:
            subcommand (str): Name of the model to create.
            kwargs (dict): Arguments for the model.
        """
        if subcommand is None:
            raise ValueError("Model Subcommand must be specified")
        else:
            raise ValueError(f"Unknown Model: {subcommand}")


def init_parser():
    instance = ConfigParser()
    instance.parser_dict.update(**{
        'model': ArgumentParser()
    })
    for item in instance.parser_dict.items():
        instance.subcommands.add_subcommand(*item)


init_parser()

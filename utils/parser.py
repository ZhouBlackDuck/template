from typing import Tuple

from jsonargparse import ArgumentParser


def pass_dict(parser: ArgumentParser, t: Tuple[str, ...], target: str):
    parser.link_arguments(t, target, lambda *args: dict(zip([n.split('.')[-1] for n in t], args)))

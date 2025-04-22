from typing import Tuple

import inflection
from jsonargparse import ArgumentParser


def pass_dict(parser: ArgumentParser, t: Tuple[str, ...], target: str):
    parser.link_arguments(t, target,
                          lambda *args: dict(zip([inflection.underscore(n).split('.')[-1] for n in t], args)))

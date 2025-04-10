import os
import sys
from inspect import isclass

from typings import DefaultsMeta
from utils import import_modules

(lambda l: [setattr(sys.modules[__name__], *t) for c in l for t in c])((
    lambda l: [getattr(m, v).__defaults__ for m in l for v in dir(m) if
               isclass(getattr(m, v)) and type(getattr(m, v)) is DefaultsMeta])(
    import_modules('defaults', os.path.dirname(__file__))))


def get_defaults(name):
    return getattr(sys.modules[__name__], name)

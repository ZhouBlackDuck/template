import os
from importlib import import_module


def import_modules(package, base):
    return [import_module(f'{package}.{file[:-3]}') for _, _, files in os.walk(base) for file in files if
            file.endswith('.py') and file != '__init__.py']

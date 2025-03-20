import os
import os.path as path
from logging import Logger
from jsonargparse import ArgumentParser

__parser = None


def get_parser(logger: [bool, Logger] = False):
    global __parser
    if __parser is None:
        __parser = ArgumentParser(prog='main.py', default_env=True, print_config='--print-config',
                                  default_config_files=[
                                      path.normpath(path.join(os.getcwd(), 'configs', 'config.yaml')),
                                  ],
                                  logger=logger)
        __parser.add_argument('-c', '--config', help='Path to config file', metavar='path', nargs=1, action='config')
    return __parser


__all__ = [
    'get_parser'
]

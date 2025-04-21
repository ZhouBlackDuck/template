import os
import threading
from os import path

from jsonargparse import ArgumentParser


class ConfigParser:
    _local = threading.local()

    def __new__(cls, *args, **kwargs):
        if getattr(cls._local, 'instance', None) is None:
            cls._local.instance = super().__new__(cls)
            cls._local.instance.parser = ArgumentParser(prog='main.py', default_env=True,
                                                        print_config='--print-config',
                                                        default_config_files=[
                                                            path.normpath(
                                                                path.join(os.getcwd(), 'configs', 'config.yaml')),
                                                        ],
                                                        logger='root')
            cls._local.instance.parser.add_argument('-c', '--config', help='Path to config file', metavar='path',
                                                    nargs=1, action='config')
            cls._local.instance.subcommands = cls._local.instance.parser.add_subcommands()
            cls._local.instance.parser_dict = {}
        return cls._local.instance

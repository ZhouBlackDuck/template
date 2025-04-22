import os
import threading
from os import path

from jsonargparse import ArgumentParser


class ConfigParser:
    _local = threading.local()
    _env = os.environ.get('DL_ENV', None)

    def __new__(cls, *args, **kwargs):
        if getattr(cls._local, 'instance', None) is None:
            cls._local.instance = super().__new__(cls)
            config_file = f'config.{cls._env}.yaml' if cls._env is not None else 'config.yaml'
            cls._local.instance.parser = ArgumentParser(prog='main.py', default_env=True,
                                                        print_config='--print-config',
                                                        default_config_files=[
                                                            path.normpath(
                                                                path.join(os.getcwd(), 'configs', config_file)),
                                                        ],
                                                        logger='root')
            cls._local.instance.parser.add_argument('-c', '--config', help='Path to config file', metavar='path',
                                                    nargs=1, action='config')
            cls._local.instance.subcommands = cls._local.instance.parser.add_subcommands()
            cls._local.instance.parser_dict = {}
        return cls._local.instance

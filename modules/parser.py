import os
import threading
from os import path

from jsonargparse import ArgumentParser


class ConfigParser:
    _lock = threading.Lock()
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.parser = ArgumentParser(prog='main.py', default_env=True,
                                                          print_config='--print-config',
                                                          default_config_files=[
                                                              path.normpath(
                                                                  path.join(os.getcwd(), 'configs', 'config.yaml')),
                                                          ],
                                                          logger='root')
                    cls._instance.parser.add_argument('-c', '--config', help='Path to config file', metavar='path',
                                                      nargs=1, action='config')
                    cls._instance.subcommands = cls._instance.parser.add_subcommands()
                    cls._instance.parser_dict = {}
        return cls._instance

    def get_lock(self):
        return self._lock

import os.path as path
from threading import local

import reconplogger
from jsonargparse import ArgumentParser


class ConfigParser(local):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.parser = ArgumentParser(default_env=True, default_config_files=[
                path.normpath(path.join(path.dirname(__file__), 'config.yaml'))
            ], logger=reconplogger.logger_setup(
                config=str(path.normpath(path.join(path.dirname(__file__), 'logging.yaml')))))
            cls._instance.parser.add_argument('-c', '--config', action='config', nargs='?',
                                              help='Config file path')
        return cls._instance

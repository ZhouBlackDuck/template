import logging
from logging import getLogger

__logger = None
DEFAULT_LEVEL = 'INFO'
DEFAULT_FORMAT = '[%(asctime)s] - %(name)s - [%(levelname)s] - %(message)s'
DEFAULT_DATEFMT = '%Y-%m-%d %H:%M:%S'
DEFAULT_FILEMODE = 'a'
DEFAULT_ENCODING = 'utf-8'


def get_logger():
    global __logger
    if __logger is None:
        logging.basicConfig(level=DEFAULT_LEVEL, format=DEFAULT_FORMAT, datefmt=DEFAULT_DATEFMT)
        __logger = getLogger('main')
    return __logger


__all__ = [
    'get_logger',
    'DEFAULT_LEVEL',
    'DEFAULT_FORMAT',
    'DEFAULT_DATEFMT',
    'DEFAULT_FILEMODE',
    'DEFAULT_ENCODING'
]

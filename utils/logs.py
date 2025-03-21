import logging
from logging import getLogger

from .defaults import DEFAULT_LOGGING__LEVEL, DEFAULT_LOGGING__FORMAT, DEFAULT_LOGGING__DATEFMT

__logger = None


def get_logger():
    global __logger
    if __logger is None:
        logging.basicConfig(level=DEFAULT_LOGGING__LEVEL, format=DEFAULT_LOGGING__FORMAT,
                            datefmt=DEFAULT_LOGGING__DATEFMT)
        __logger = getLogger('main')
    return __logger


__all__ = [
    'get_logger'
]

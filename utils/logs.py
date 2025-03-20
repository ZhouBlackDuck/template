from logging import getLogger

__logger = None


def get_logger():
    global __logger
    if __logger is None:
        __logger = getLogger('main')
    return __logger

import logging
from logging import getLogger


class ProcessLogger:
    @classmethod
    def get_logger(cls):
        return getLogger()

    @classmethod
    def set_config(cls, *args, **kwargs):
        logging.basicConfig(*args, **kwargs)

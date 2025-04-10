from typings import DefaultsMeta


class Logging(metaclass=DefaultsMeta):
    level = 'INFO'
    format = '[%(asctime)s] - %(name)s - [%(levelname)s] - %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    filemode = 'a'
    encoding = 'utf-8'

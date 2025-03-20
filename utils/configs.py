import os
import os.path as path
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


__parser = None

def get_parser():
    global __parser
    if __parser is None:
        __parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, prog='main')
    return __parser

def check_existing_config(config):
    if path.isabs(config):
        if not path.exists(path.normpath(config)):
            raise FileNotFoundError(f'Config file {config} does not exist')
    else:
        if not path.exists(path.normpath(path.join(os.getcwd(), config))):
            raise FileNotFoundError(f'Config file {config} does not exist')

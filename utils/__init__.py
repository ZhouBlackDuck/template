from .logs import *
from .configs import *
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


__parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, prog='main.py', add_help=False)
__parser.add_argument('-c', '--config', type=str, help='path to config file', const=f'configs{os.sep}config.yaml',
                          metavar='path', default=f'configs{os.sep}config.yaml', nargs='?')
get_logger()
get_parser([__parser])

def get_parent_parser():
    return __parser

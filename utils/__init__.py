from .logs import *
from .configs import *


get_logger()
get_parser().add_argument('-c', '--config', type=str, help='path to config file', const=f'configs{os.sep}config.yaml',
                          metavar='path', default=f'configs{os.sep}config.yaml', nargs='?')

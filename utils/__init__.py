from argparse import SUPPRESS
from jsonargparse.typing import Path_fc

from .configs import *
from .logs import *
from .types import *
from .defaults import *

get_parser(get_logger())
get_parser().add_argument('--logging.filename', help='Path to log file', metavar='path', nargs=1, type=Path_fc,
                          default=SUPPRESS)
get_parser().add_argument('--logging.filemode', help='Log file mode', metavar='mode', nargs='?', type=FileMode,
                          default=DEFAULT_LOGGING__FILEMODE, const=DEFAULT_LOGGING__FILEMODE)
get_parser().add_argument('--logging.level', help='Logging level', metavar='level', nargs='?',
                          choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                          default=DEFAULT_LOGGING__LEVEL, const=DEFAULT_LOGGING__LEVEL)
get_parser().add_argument('--logging.format', help='Logging format', metavar='format', nargs='?',
                          default=DEFAULT_LOGGING__FORMAT, const=DEFAULT_LOGGING__FORMAT)
get_parser().add_argument('--logging.datefmt', help='Logging date format', metavar='format', nargs='?',
                          default=DEFAULT_LOGGING__DATEFMT, const=DEFAULT_LOGGING__DATEFMT)
get_parser().add_argument('--logging.encoding', help='Log file encoding', metavar='encoding', nargs='?',
                          default=DEFAULT_LOGGING__ENCODING, const=DEFAULT_LOGGING__ENCODING)

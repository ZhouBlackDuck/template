from argparse import SUPPRESS

from jsonargparse.typing import Path_fc

from defaults import get_defaults
from typings import FileMode
from .logger import ProcessLogger
from .parser import ConfigParser

ProcessLogger.set_config(level=get_defaults('DEFAULT_LOGGING__LEVEL'), format=get_defaults('DEFAULT_LOGGING__FORMAT'),
                         datefmt=get_defaults('DEFAULT_LOGGING__DATEFMT'), force=True)


def init_parser():
    p = ConfigParser().parser
    p.add_argument('--logging.filename', help='Path to log file', metavar='path', nargs=1,
                   type=Path_fc,
                   default=SUPPRESS)
    p.add_argument('--logging.filemode', help='Log file mode', metavar='mode', nargs='?',
                   type=FileMode,
                   default=get_defaults('DEFAULT_LOGGING__FILEMODE'),
                   const=get_defaults('DEFAULT_LOGGING__FILEMODE'))
    p.add_argument('--logging.level', help='Logging level', metavar='level', nargs='?',
                   choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                   default=get_defaults('DEFAULT_LOGGING__LEVEL'),
                   const=get_defaults('DEFAULT_LOGGING__LEVEL'))
    p.add_argument('--logging.format', help='Logging format', metavar='format', nargs='?',
                   default=get_defaults('DEFAULT_LOGGING__FORMAT'),
                   const=get_defaults('DEFAULT_LOGGING__FORMAT'))
    p.add_argument('--logging.datefmt', help='Logging date format', metavar='format', nargs='?',
                   default=get_defaults('DEFAULT_LOGGING__DATEFMT'),
                   const=get_defaults('DEFAULT_LOGGING__DATEFMT'))
    p.add_argument('--logging.encoding', help='Log file encoding', metavar='encoding', nargs='?',
                   default=get_defaults('DEFAULT_LOGGING__ENCODING'),
                   const=get_defaults('DEFAULT_LOGGING__ENCODING'))


init_parser()

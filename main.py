import utils
import os
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, prog='main', add_help=False)

    parser.add_argument('-c', '--config', type=str, help='path to config file', const=f'configs{os.sep}config.yaml',
                        metavar='path', default=f'configs{os.sep}config.yaml', nargs='?')

    args, extra_args = parser.parse_known_args()

    try:
        utils.check_existing_config(args.config)
    except FileNotFoundError as e:
        utils.get_logger().warning(str(e) + ', using input or default config')

    args = utils.get_parser().parse_args(extra_args, namespace=args)

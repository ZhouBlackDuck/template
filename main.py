import logging
import utils

if __name__ == '__main__':
    parser = utils.get_parser()
    args = parser.parse_args()
    if hasattr(args.logging, 'filename'):
        args.logging.filename = args.logging.filename[0].absolute
    logging.basicConfig(**args.logging, force=True)

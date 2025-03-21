import logging
import utils
import datasets
import models

if __name__ == '__main__':
    try:
        parser = utils.get_parser()
        args = parser.parse_args()
        if hasattr(args.logging, 'filename'):
            args.logging.filename = args.logging.filename[0].absolute
        logging.basicConfig(**args.logging, force=True)
    except Exception as e:
        utils.get_logger().error(e, exc_info=e)

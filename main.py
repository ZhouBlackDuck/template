import utils


if __name__ == '__main__':
    parser = utils.get_parent_parser()

    args, extra_args = parser.parse_known_args()

    warning = None
    try:
        utils.check_existing_config(args.config)
    except FileNotFoundError as e:
        warning = str(e) + ', using input or default config'

    if warning is None:
        file_configs = utils.load_config(args.config)

    args = utils.get_parser().parse_args(extra_args, namespace=args)

    if warning is not None:
        utils.get_logger().warning(warning)

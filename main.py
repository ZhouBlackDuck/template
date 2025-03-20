import utils

if __name__ == '__main__':
    parser = utils.get_parser()
    parser.add_argument('-c', '--config', help='Path to config file', metavar='path', nargs=1, action='config')
    args = parser.parse_args()

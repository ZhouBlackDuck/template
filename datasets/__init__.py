import utils
from jsonargparse.typing import OpenUnitInterval

from utils.defaults import DEFAULT_SPLIT_RATIO, DEFAULT_DEVICE, DEFAULT_BATCH_SIZE

utils.get_parser().add_argument('--split-ratio', help='Train/test split ratio', metavar='ratio', nargs='?',
                                type=OpenUnitInterval, default=DEFAULT_SPLIT_RATIO, const=DEFAULT_SPLIT_RATIO)
utils.get_parser().add_argument('--device', help='Device to use', metavar='device', nargs='?', default=DEFAULT_DEVICE,
                                const=DEFAULT_DEVICE)
utils.get_parser().add_argument('--batch-size', help='Batch size', metavar='size', nargs='?', type=int,
                                default=DEFAULT_BATCH_SIZE, const=DEFAULT_BATCH_SIZE)

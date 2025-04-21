from jsonargparse.typing import OpenUnitInterval

from datasets.builders import *
from defaults import get_defaults
from modules import ConfigParser
from utils import pass_dict

ConfigParser().parser.add_method_arguments(DatasetBuilderFactory, 'create_builder', 'factory.builder',
                                           as_group=False)
ConfigParser().parser.add_argument('--split-ratio', help='Train/test split ratio', metavar='ratio', nargs='?',
                                   type=OpenUnitInterval, default=get_defaults('DEFAULT_DATASET__SPLIT_RATIO'),
                                   const=get_defaults('DEFAULT_DATASET__SPLIT_RATIO'))
ConfigParser().parser.add_argument('--device', help='Device to use', metavar='device', nargs='?',
                                   default=get_defaults('DEFAULT_DATASET__DEVICE'),
                                   const=get_defaults('DEFAULT_DATASET__DEVICE'))
ConfigParser().parser.add_argument('--batch-size', help='Batch size', metavar='size', nargs='?', type=int,
                                   default=get_defaults('DEFAULT_DATASET__BATCH_SIZE'),
                                   const=get_defaults('DEFAULT_DATASET__BATCH_SIZE'))
ConfigParser().parser.add_argument('--dataset', help='Dataset name', metavar='name', nargs='?', type=str,
                                   default=get_defaults('DEFAULT_DATASET__NAME'),
                                   const=get_defaults('DEFAULT_DATASET__NAME'))
ConfigParser().parser.link_arguments('dataset', 'factory.builder.dataset')
pass_dict(ConfigParser().parser, ('split_ratio', 'device', 'batch_size'), 'factory.builder.kwargs')

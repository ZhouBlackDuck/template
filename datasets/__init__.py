"""
数据集
"""

from configs.parser import ConfigParser
from typings.dataset import Dataset

ConfigParser().parser.add_argument('--dataset', type=Dataset)

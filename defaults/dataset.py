from typings import DefaultsMeta


class Dataset(metaclass=DefaultsMeta):
    split_ratio = 0.8
    device = 'cuda'
    batch_size = 32
    name = 'dataset'

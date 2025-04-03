import utils
from jsonargparse import ArgumentParser

__subcommands = utils.get_parser().add_subcommands()
__parsers = dict()
__parsers['model'] = ArgumentParser()
for item in __parsers.items():
    __subcommands.add_subcommand(*item)

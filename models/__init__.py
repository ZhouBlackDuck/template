import utils
from jsonargparse import ArgumentParser

__subcommands = utils.get_parser().add_subcommands()
__parser = ArgumentParser()
__subcommands.add_subcommand('model', __parser)

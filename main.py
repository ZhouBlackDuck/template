from modules.parser import ConfigParser
from modules.logger import ProcessLogger
from datasets import DatasetBuilderFactory
from models import ModelDatasetDirectorFactory
from models import ModelFactory

if __name__ == '__main__':
    try:
        args = ConfigParser().parser.parse_args()
        if hasattr(args.logging, 'filename'):
            args.logging.filename = args.logging.filename[0].absolute
        ProcessLogger.set_config(**args.logging, force=True)
        ProcessLogger.get_logger().debug('Arguments: %s', args)
        builder = DatasetBuilderFactory.create_builder(**args.factory.builder)
        director = ModelDatasetDirectorFactory.create_director(args.subcommand)
        model = ModelFactory.create_model(args.subcommand, getattr(args, args.subcommand))
        director.builder = builder
        model.director = director
        model.load()
        model.train()
        model.evaluate()
        model.predict()
        model.save()
    except Exception as e:
        ProcessLogger.get_logger().error(e, exc_info=e)

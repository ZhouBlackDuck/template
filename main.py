from configs.parser import ConfigParser
from datasets.builders import DatasetBuilderFactory
from models import ModelFactory
from models.directors import ModelDatasetDirectorFactory

if __name__ == '__main__':
    args = ConfigParser().parser.parse_args()
    logger = ConfigParser().parser.logger
    try:
        model = ModelFactory.create_model(**args.model.as_dict())
        director = ModelDatasetDirectorFactory.create_director(**args.model.as_dict())
        builder = DatasetBuilderFactory.create_builder(**args.dataset.as_dict())
        director.builder = builder
        model.director = director
        if not model.load():
            model.train()
            model.evaluate()
            model.save()
        model.predict()
    except Exception as e:
        logger.exception(str(e), exc_info=e)

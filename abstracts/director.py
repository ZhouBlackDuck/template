from abc import ABC, abstractmethod


class ModelDatasetDirector(ABC):
    def __init__(self, *args, **kwargs):
        self.__builder = None
        super().__init__(*args, **kwargs)

    @abstractmethod
    def _procedures(self, *args, **kwargs):
        pass

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, value):
        self.__builder = value

    def execute(self):
        self._procedures()
        return self.builder.build()

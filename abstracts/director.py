from abc import ABC, abstractmethod
from typing import Optional

from abstracts.builder import DatasetBuilder


class ModelDatasetDirector(ABC):
    def __init__(self, *args, **kwargs):
        self.__builder: Optional[DatasetBuilder] = None
        super().__init__(*args, **kwargs)

    @abstractmethod
    def _do_procedures(self):
        pass

    def _procedures(self):
        self._do_procedures()
        return self.builder

    @abstractmethod
    def _do_prepare(self, *args, **kwargs):
        pass

    def prepare(self, *args, **kwargs):
        self._do_prepare(*args, **kwargs)
        return self

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, value):
        self.__builder = value

    def execute(self):
        return self._procedures().build()

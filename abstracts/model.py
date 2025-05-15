from abc import ABC, abstractmethod
from typing import Optional

from abstracts.director import ModelDatasetDirector


class AbstractModel(ABC):
    def __init__(self, *args, **kwargs):
        self.__director: Optional[ModelDatasetDirector] = None
        self.__dataset = None
        super().__init__(*args, **kwargs)

    @abstractmethod
    def train(self, *args, **kwargs):
        pass

    @abstractmethod
    def evaluate(self, *args, **kwargs):
        pass

    @abstractmethod
    def predict(self, *args, **kwargs):
        pass

    @abstractmethod
    def save(self, *args, **kwargs):
        pass

    @abstractmethod
    def load(self, *args, **kwargs) -> bool:
        pass

    @abstractmethod
    def _do_construct(self):
        pass

    def _construct(self):
        self._do_construct()
        return self.director.execute()

    @property
    def dataset(self):
        if self.__dataset is None:
            self.__dataset = self._construct()
        return self.__dataset

    @dataset.setter
    def dataset(self, value):
        self.__dataset = value

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, value):
        self.__director = value

    def reproduce(self):
        self.dataset = self._construct()

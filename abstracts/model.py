from abc import ABC, abstractmethod


class AbstractModel(ABC):
    def __init__(self, *args, **kwargs):
        self.__director = None
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
    def load(self, *args, **kwargs):
        pass

    @abstractmethod
    def _pass_parameters(self, *args, **kwargs):
        pass

    @property
    def dataset(self):
        if self.__dataset is None:
            self._pass_parameters()
            self.__dataset = self.director.execute()
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
        self._pass_parameters()
        self.dataset = self.director.execute()

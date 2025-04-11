from abc import ABC, abstractmethod


class DatasetBuilder(ABC):
    def __init__(self, *args, **kwargs):
        self.__commands = []
        super().__init__(*args, **kwargs)

    @property
    @abstractmethod
    def data(self):
        """
        Dataset that model will use.
        """
        pass

    @data.setter
    @abstractmethod
    def data(self, value):
        pass

    @abstractmethod
    def _do_process(self, *args, **kwargs):
        pass

    def process(self, *args, **kwargs):
        """
        Process all dataset, uniform data shapes, drop invalid data, etc.
        """
        self.__commands.append((self._do_process, args, kwargs))

    @abstractmethod
    def load(self, *args, **kwargs):
        """
        Load processed dataset from disk.
        """
        pass

    @abstractmethod
    def save(self, *args, **kwargs):
        pass

    @abstractmethod
    def read(self, *args, **kwargs):
        """
        Read raw dataset from disk.
        """
        pass

    def build(self):
        for func, args, kwargs in self.__commands:
            func(self, *args, **kwargs)
        self.__commands.clear()
        return self.data

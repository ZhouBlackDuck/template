from abc import ABC, abstractmethod


class DatasetBuilder(ABC):
    def __init__(self, *args, **kwargs):
        self.__commands = []
        super().__init__(*args, **kwargs)

    @property
    @abstractmethod
    def data(self):
        pass

    @data.setter
    @abstractmethod
    def data(self, value):
        pass

    @abstractmethod
    def _do_process(self, *args, **kwargs):
        pass

    def process(self, *args, **kwargs):
        self.__commands.append((self._do_process, args, kwargs))

    def build(self):
        for func, args, kwargs in self.__commands:
            func(self, *args, **kwargs)
        self.__commands.clear()
        return self.data

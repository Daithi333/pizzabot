from abc import ABC, abstractmethod


class AbstractArgParser(ABC):

    @abstractmethod
    def extract_grid_and_coords(self, **args) -> ((int, int), list[(int, int)]):
        raise NotImplementedError('extract_grid_and_coords must be implemented when extending AbstractArgParser')

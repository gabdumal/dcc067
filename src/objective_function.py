from abc import ABC, abstractmethod

import numpy as np


class ObjectiveFunction(ABC):
    name: str
    x_global: np.ndarray

    @abstractmethod
    def __init__(self, dimensions):
        pass

    @property
    def lb(self) -> np.ndarray:
        return self._lb

    @property
    def ub(self) -> np.ndarray:
        return self._ub

    @abstractmethod
    def evaluate(self, solution):
        pass

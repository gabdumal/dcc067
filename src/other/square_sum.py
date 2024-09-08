import numpy as np

from objective_function import ObjectiveFunction


class SquareSum(ObjectiveFunction):
    def __init__(self, dimensions):
        super().__init__(dimensions)
        self._lb = -100 * np.ones(dimensions)
        self._ub = 100 * np.ones(dimensions)
        self.x_global = np.zeros(dimensions)

    name = "Square Sum"

    def evaluate(self, sol):
        return np.sum(sol**2)

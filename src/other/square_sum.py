import numpy as np

from search import ObjectiveFunction


class SquareSum(ObjectiveFunction):
    def __init__(self, dimensions, lowerBound=-100, upperBound=100):
        self.dimensions = dimensions
        self.lowerBound = lowerBound
        self.upperBound = upperBound

    @staticmethod
    def get_name():
        return "Soma dos quadrados"

    def evaluate(self, sol):
        return np.sum(sol**2)

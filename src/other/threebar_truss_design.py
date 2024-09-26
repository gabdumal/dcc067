import numpy as np
from objective_function import ObjectiveFunction
from math import sqrt

class ThreeBarTruss(ObjectiveFunction):
    def __init__(self, dimensions):
        super().__init__(dimensions)
        self._lb = 0 * np.ones(dimensions)
        self._ub = 1 * np.ones(dimensions)
        self.x_global = np.zeros(dimensions)

    name = "Three-Bar Truss Design"

    def evaluate(self, individual):
        x1 = individual[0]
        x2 = individual[1]
        
        y = (2 * sqrt(2) * x1 + x2) * 100
        
        if x1 <= 0:
            g = [1, 1, 1]
        else:
            g1 = (sqrt(2) * x1 + x2) / (sqrt(2) * x1**2 + 2 * x1 * x2) * 2 - 2
            g2 = x2 / (sqrt(2) * x1**2 + 2 * x1 * x2) * 2 - 2
            g3 = 1 / (x1 + sqrt(2) * x2) * 2 - 2
            g = [g1, g2, g3]
        
        g_round = np.round(np.array(g), 6)
        w1 = 50
        w2 = 50
        
        phi = sum(max(item, 0) for item in g_round)
        viol = sum(float(num) > 0 for num in g_round)
        
        return y + w1 * phi + w2 * viol

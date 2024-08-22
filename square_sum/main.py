from mealpy import FloatVar, GA
import numpy as np
import constants
from util import print_parameter


class ObjectiveFunction:
    def __init__(self, dimensions, lowerBound=-100, upperBound=100):
        self.dimensions = dimensions
        self.lowerBound = lowerBound
        self.upperBound = upperBound

    def evaluate(self, sol):
        return np.sum(sol**2)


def square_sum():
    # Problem definition
    dimensions = 10
    print_parameter("Número de dimensões", dimensions)

    objective_function = ObjectiveFunction(dimensions)

    def objective_function_wrapper(solution):
        return objective_function.evaluate(solution)

    # GA parameters
    crossover_rate: float = 0.95
    print_parameter("Taxa de crossover", crossover_rate)
    mutation_rate: float = 0.025
    print_parameter("Taxa de mutação", mutation_rate)

    # Optimization parameters
    epochs: int = 10000
    print_parameter("Número de épocas", epochs)

    global_solution = np.zeros(dimensions)
    print_parameter("Solução global", global_solution)
    global_fitness = objective_function.evaluate(global_solution)
    print_parameter("Fitness da solução global", global_fitness)

    problem_dictionary = {
        "obj_func": objective_function_wrapper,
        "bounds": FloatVar(
            lb=([-100] * dimensions),
            ub=([100] * dimensions),
        ),
        "minmax": "min",
        "ndim": dimensions,
    }

    optimizer = GA.BaseGA(
        epoch=epochs,
        pop_size=constants.population_size,
        pc=crossover_rate,
        pm=mutation_rate,
    )

    print()
    optimizer.solve(problem_dictionary)
    print()

    algorithm_solution = optimizer.g_best.solution
    print_parameter("Solução encontrada", algorithm_solution)
    algorithm_fitness = objective_function.evaluate(algorithm_solution)
    print_parameter("Fitness da solução encontrada", algorithm_fitness)

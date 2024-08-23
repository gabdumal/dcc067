from abc import ABC, abstractmethod

import numpy as np
from mealpy import GA, FloatVar, Problem

import constants
from util.printing_helper import print_header, print_parameters


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


def search(objective_function_class: ObjectiveFunction):
    print_header(objective_function_class.name)

    # Problem definition
    dimensions = constants.dimensions
    target = "min"
    objective_function = objective_function_class(dimensions)

    def objective_function_wrapper(solution):
        return objective_function.evaluate(solution)

    lower_bounds = objective_function.lb
    upper_bounds = objective_function.ub

    # Algorithm parameters
    population_size: int = constants.population_size
    selection = "roulette"
    crossover = "uniform"
    mutation = "swap"
    k_way = 0.2
    crossover_rate: float = 0.95
    mutation_rate: float = 0.8
    elitism_best_rate: float = 0.1
    elitism_worst_rate: float = 0.3

    # Optimization parameters
    population_size: int = constants.population_size
    epochs: int = constants.epochs

    # Optimal solution
    optimal_solution = objective_function.x_global
    optimal_fitness = objective_function.evaluate(optimal_solution)

    problem_modelling: Problem = {
        "obj_func": objective_function_wrapper,
        "bounds": FloatVar(
            lb=lower_bounds,
            ub=upper_bounds,
        ),
        "minmax": target,
        "ndim": dimensions,
    }

    optimizer = GA.EliteSingleGA(
        epoch=epochs,
        pop_size=population_size,
        pc=crossover_rate,
        pm=mutation_rate,
        selection=selection,
        crossover=crossover,
        mutation=mutation,
        k_way=k_way,
        elite_best=elitism_best_rate,
        elite_worst=elitism_worst_rate,
        strategy=0,
    )

    print()
    optimizer.solve(problem_modelling)
    print()

    algorithm_solution = optimizer.g_best.solution
    algorithm_fitness = objective_function.evaluate(algorithm_solution)

    print_parameters(
        {
            "Objective function": objective_function_class.name,
            "Dimensions": dimensions,
            "Lower bounds": lower_bounds,
            "Upper bounds": upper_bounds,
            "Optimal solution": optimal_solution,
            "Optimal fitness": optimal_fitness,
        }
    )
    print()
    print_parameters(
        {
            "Selection": selection,
            "K-way": k_way,
            "Crossover": crossover,
            "Crossover rates": crossover_rate,
            "Mutation": mutation,
            "Mutation rates": mutation_rate,
            "Elitism best rate": elitism_best_rate,
            "Elitism worst rate": elitism_worst_rate,
        }
    )
    print()
    print_parameters(
        {
            "Population size": population_size,
            "Epochs": epochs,
            "Algorithm solution": algorithm_solution,
            "Algorithm fitness": algorithm_fitness,
        }
    )

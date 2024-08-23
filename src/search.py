from abc import ABC, abstractmethod

import numpy as np
from mealpy import GA, FloatVar, Problem

import constants
from util.printing_helper import print_header, print_parameters


class ObjectiveFunction(ABC):
    @abstractmethod
    def evaluate(self, solution):
        pass

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        pass


def search(objective_function_class: ObjectiveFunction):
    print_header(objective_function_class.get_name())

    # Problem definition
    dimensions = 10
    target = "min"
    lower_bounds = [-100] * dimensions
    upper_bounds = [100] * dimensions

    # Objective function
    objective_function = objective_function_class(dimensions)

    def objective_function_wrapper(solution):
        return objective_function.evaluate(solution)

    # Algorithm parameters
    crossover_rate: float = 0.95
    mutation_rate: float = 0.025
    population_size: int = constants.population_size

    # Optimization parameters
    epochs: int = constants.epochs

    # Optimal solution
    optimal_solution = np.zeros(dimensions)
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

    optimizer = GA.BaseGA(
        epoch=epochs,
        pop_size=population_size,
        pc=crossover_rate,
        pm=mutation_rate,
    )

    print()
    optimizer.solve(problem_modelling)
    print()

    algorithm_solution = optimizer.g_best.solution
    algorithm_fitness = objective_function.evaluate(algorithm_solution)

    print_parameters(
        {
            "Função objetivo": objective_function.get_name(),
            "Número de dimensões": dimensions,
            "Alvo": target == "min" and "Minimização" or "Maximização",
            "Limites inferiores": lower_bounds,
            "Limites superiores": upper_bounds,
            "Taxa de crossover": crossover_rate,
            "Taxa de mutação": mutation_rate,
            "Tamanho da população": population_size,
            "Número de gerações": epochs,
            "Solução ótima": optimal_solution,
            "Fitness da solução ótima": optimal_fitness,
            "Solução obtida": algorithm_solution,
            "Fitness da solução obtida": algorithm_fitness,
        }
    )

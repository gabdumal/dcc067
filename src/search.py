import os
from abc import ABC, abstractmethod

import numpy as np
from mealpy import MA, FloatVar, Problem

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


def search(
    experiment_identifier: str,
    dimensions: int,
    objective_function_class: ObjectiveFunction,
    objective_function_identifier: str,
    crossover: str,
    selection: str,
    tournament_percentage: float,
    export_parameters,
    seed: int,
    p_local: float,
    max_local_gens: int,
    bits_per_param: int,
):
    print_header(objective_function_class.name)

    # Problem definition
    target = constants.target
    objective_function = objective_function_class(dimensions)

    def objective_function_wrapper(solution):
        return objective_function.evaluate(solution)

    lower_bounds = objective_function.lb
    upper_bounds = objective_function.ub

    # Algorithm parameters
    population_size: int = constants.population_size
    crossover_rate: float = constants.crossover_rate
    mutation_rate: float = constants.mutation_rate

    # Optimization parameters
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

    optimizer = MA.OriginalMA(
        epoch=epochs,
        pop_size=population_size,
        pc=crossover_rate,
        pm=mutation_rate,
        p_local=p_local,
        max_local_gens=max_local_gens,
        bits_per_param=bits_per_param,
        strategy=0,
    )

    print()
    optimizer.solve(problem_modelling, seed=seed)
    print()

    algorithm_solution = optimizer.g_best.solution
    algorithm_fitness = objective_function.evaluate(algorithm_solution)

    # Results
    objective_function_description = {
        "Objective function": objective_function_class.name
    }
    problem_parameters = {
        "Dimensions": dimensions,
        "Lower bounds": lower_bounds,
        "Upper bounds": upper_bounds,
        "Optimal solution": optimal_solution,
        "Optimal fitness": optimal_fitness,
    }
    algorithm_parameters = {
        "Crossover": crossover,
        "Crossover rates": crossover_rate,
        "Mutation rates": mutation_rate,
        "Local search probability": p_local,
        "Max local generations": max_local_gens,
        "Bits per parameter": bits_per_param,
    }
    optimization_parameters = {
        "Population size": population_size,
        "Epochs": epochs,
    }
    solution_output = {
        "Seed": int(seed),
        "Algorithm solution": algorithm_solution.tolist(),
        "Algorithm fitness": algorithm_fitness,
    }

    print_parameters(objective_function_description)
    print()
    print_parameters(problem_parameters)
    print()
    print_parameters(algorithm_parameters)
    print()
    print_parameters(optimization_parameters)
    print()
    print_parameters(solution_output)

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_file_directory_path = os.path.join(
        project_root,
        f".results/{experiment_identifier}/OriginalMA/{dimensions}/{objective_function_identifier}/{crossover}/{selection}",
    )
    if selection == "tournament":
        output_file_directory_path += f"/{tournament_percentage}"
    output_file_path = os.path.join(
        output_file_directory_path,
        f"{seed}.txt",
    )

    os.makedirs(output_file_directory_path, exist_ok=True)
    with open(output_file_path, "w+") as output_file:
        if export_parameters:
            print_parameters(objective_function_description, output_file.write, False)
            output_file.write("\n")
            print_parameters(problem_parameters, output_file.write, False)
            output_file.write("\n")
            print_parameters(algorithm_parameters, output_file.write, False)
            output_file.write("\n")
            print_parameters(optimization_parameters, output_file.write, False)
            output_file.write("\n")
        print_parameters(solution_output, output_file.write, fancy=False)
        output_file.write("\n")

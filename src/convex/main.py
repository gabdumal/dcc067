from mealpy import GA, FloatVar, Problem
from opfunu.cec_based.cec2014 import F12014
from termcolor import colored

import constants
from util.printing_helper import print_parameter


def header():
    print(colored("=-= Função convexa =-=", on_color="on_white", attrs=["bold"]))


def convex():
    header()

    # Problem definition
    dimensions: int = 10
    print_parameter("Número de dimensões", dimensions)

    # GA parameters
    selection: str = "roulette"
    print_parameter("Seleção", selection)
    crossover: str = "uniform"
    print_parameter("Crossover", crossover)
    mutation: str = "swap"
    print_parameter("Mutação", mutation)
    crossover_rate: float = 0.95
    print_parameter("Taxa de crossover", crossover_rate)
    mutation_rate: float = 0.025
    print_parameter("Taxa de mutação", mutation_rate)
    elitism_best_rate: float = 0.1
    print_parameter("Taxa de elitismo", elitism_best_rate)
    elitism_worst_rate: float = 0.3
    print_parameter("Taxa de elitismo (piores)", elitism_worst_rate)

    # Optimization parameters
    epochs: int = 10000
    print_parameter("Número de épocas", epochs)

    objective_function = F12014(ndim=dimensions)

    def objective_function_wrapper(solution):
        return objective_function.evaluate(solution)

    bounds = FloatVar(
        lb=list(objective_function.lb),
        ub=list(objective_function.ub),
    )
    print_parameter("Limite inferior", bounds.lb)
    print_parameter("Limite superior", bounds.ub)

    global_solution = objective_function.x_global
    print_parameter("Solução global", global_solution)
    global_fitness = objective_function.evaluate(global_solution)
    print_parameter("Fitness da solução global", global_fitness)

    problem_modelling: Problem = {
        "obj_func": objective_function_wrapper,
        "minmax": "min",
        "bounds": bounds,
        "ndim": dimensions,
    }

    optimizer = GA.EliteSingleGA(
        epoch=epochs,
        pop_size=constants.population_size,
        pc=crossover_rate,
        pm=mutation_rate,
        selection=selection,
        crossover=crossover,
        mutation=mutation,
        k_way=0.2,
        elite_best=elitism_best_rate,
        elite_worst=elitism_worst_rate,
        strategy=0,
    )

    print()
    optimizer.solve(problem_modelling)
    print()

    algorithm_solution = optimizer.g_best.solution
    print_parameter("Solução encontrada", algorithm_solution)
    algorithm_fitness = objective_function.evaluate(algorithm_solution)
    print_parameter("Fitness da solução encontrada", algorithm_fitness)

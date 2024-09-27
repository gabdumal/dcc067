import random
import sys

from opfunu.cec_based.cec2005 import F62005, F92005
from termcolor import colored

# from original_ma import search
from optimizers.elite_single_ga import search as search_elite_single_ga
from optimizers.original_ma import search as search_original_ma
from other.square_sum import SquareSum


def header():
    print(
        colored(
            "=-=-= DCC067 Computação Evolucionista =-=-=",
            "black",
            "on_yellow",
            attrs=["bold"],
        )
    )

    print(colored("Grupo 1:", attrs=["bold"]), end=" ")
    print(
        colored(
            "Avaliar o uso de seleção por roleta e por torneio (variações de k); avaliar o uso do crossover de um ponto e aritmético",
            "cyan",
        )
    )
    print()


if len(sys.argv) < 9:
    print(
        colored(
            "Usage: python main.py <optimizer> <experiment_identifier> <dimensions> <objective_function> <crossover> <selection> <tournament_percentage> <export_parameters> <seed>",
            "red",
        )
    )
    exit(1)


experiment_identifier = sys.argv[2]

dimensions_arg = sys.argv[3]
try:
    dimensions = int(dimensions_arg)
    if dimensions <= 0:
        print(colored("Dimensions must be a positive integer", "red"))
        exit(1)
    if dimensions in [10, 20, 30, 50, 100]:
        pass
    else:
        print(colored("Dimensions must be 10, 20, 30, 50 or 100", "red"))
        exit(1)
except ValueError:
    print(colored("Dimensions must be an integer", "red"))
    exit(1)

objective_function_arg = sys.argv[4]
if objective_function_arg == "SquareSum":
    objective_function = SquareSum
elif objective_function_arg == "F62005":
    objective_function = F62005
elif objective_function_arg == "F92005":
    objective_function = F92005
else:
    print(colored("Objective function not found", "red"))
    exit(1)

crossover_arg = sys.argv[5]
if crossover_arg == "one_point":
    crossover = "one_point"
elif crossover_arg == "arithmetic":
    crossover = "arithmetic"
else:
    print(colored("Crossover method not found", "red"))
    exit(1)

selection_arg = sys.argv[6]
if selection_arg == "roulette":
    selection = "roulette"
elif selection_arg == "tournament":
    selection = "tournament"
else:
    print(colored("Selection method not found", "red"))
    exit(1)

if selection == "roulette":
    tournament_percentage = 0.2
else:
    tournament_percentage_arg = sys.argv[7]
    try:
        tournament_percentage = float(tournament_percentage_arg)
        if tournament_percentage <= 0 or tournament_percentage >= 1:
            print(
                colored(
                    "Tournament percentage must be between 0 and 1 exclusive", "red"
                )
            )
            exit(1)
    except ValueError:
        print(colored("Tournament percentage must be a float", "red"))
        exit(1)

export_parameters_arg = sys.argv[8]
if export_parameters_arg == "True":
    export_parameters = True
elif export_parameters_arg == "False":
    export_parameters = False
else:
    print(colored("Export parameters must be True or False", "red"))
    exit(1)

seed_arg = sys.argv[9]
if seed_arg == "None":
    seed = random.randint(0, 2**32 - 1)
else:
    try:
        seed = int(seed_arg)
    except ValueError:
        print(colored("Seed must be an integer", "red"))
        exit(1)

optimizer_arg = sys.argv[1]
if optimizer_arg == "elite_single_ga":
    header()
    search_elite_single_ga(
        experiment_identifier,
        dimensions,
        objective_function,
        objective_function_arg,
        crossover,
        selection,
        tournament_percentage,
        export_parameters,
        seed,
    )
elif optimizer_arg == "original_ma":
    header()
    search_original_ma(
        experiment_identifier,
        dimensions,
        objective_function,
        objective_function_arg,
        crossover,
        selection,
        tournament_percentage,
        export_parameters,
        seed,
    )
else:
    print(colored("Invalid name for optimizer", "red"))
    exit(1)

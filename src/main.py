import random
import sys

from opfunu.cec_based.cec2005 import F62005, F92005
from termcolor import colored

from other.square_sum import SquareSum
from search import search


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


if len(sys.argv) < 12:
    print(
        colored(
            "Usage: python main.py <experiment_identifier> <dimensions> <objective_function> <crossover> <selection> <tournament_percentage> <export_parameters> <seed> <p_local> <max_local_gens> <bits_per_param>",
            "red",
        )
    )
    exit(1)


experiment_identifier = sys.argv[1]

dimensions_arg = sys.argv[2]
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

objective_function_arg = sys.argv[3]
if objective_function_arg == "SquareSum":
    objective_function = SquareSum
elif objective_function_arg == "F62005":
    objective_function = F62005
elif objective_function_arg == "F92005":
    objective_function = F92005
# elif objective_function_arg == "F52014":
#     objective_function = F52014
else:
    print(colored("Objective function not found", "red"))
    exit(1)

crossover_arg = sys.argv[4]
if crossover_arg == "one_point":
    crossover = "one_point"
elif crossover_arg == "arithmetic":
    crossover = "arithmetic"
else:
    print(colored("Crossover method not found", "red"))
    exit(1)

selection_arg = sys.argv[5]
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
    tournament_percentage_arg = sys.argv[6]
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

export_parameters_arg = sys.argv[7]
if export_parameters_arg == "True":
    export_parameters = True
elif export_parameters_arg == "False":
    export_parameters = False
else:
    print(colored("Export parameters must be True or False", "red"))
    exit(1)

seed_arg = sys.argv[8]
if seed_arg == "None":
    seed = random.randint(0, 2**32 - 1)
else:
    try:
        seed = int(seed_arg)
    except ValueError:
        print(colored("Seed must be an integer", "red"))
        exit(1)

p_local_arg = sys.argv[9]
try:
    p_local = float(p_local_arg)
    if p_local <= 0 or p_local >= 1:
        print(colored("p_local must be between 0 and 1 exclusive", "red"))
        exit(1)
except ValueError:
    print(colored("p_local must be a float", "red"))
    exit(1)

max_local_gens_arg = sys.argv[10]
try:
    max_local_gens = int(max_local_gens_arg)
    if max_local_gens <= 0:
        print(colored("max_local_gens must be a positive integer", "red"))
        exit(1)
except ValueError:
    print(colored("max_local_gens must be an integer", "red"))
    exit(1)

bits_per_param_arg = sys.argv[11]
try:
    bits_per_param = int(bits_per_param_arg)
    if bits_per_param <= 0:
        print(colored("bits_per_param must be a positive integer", "red"))
        exit(1)
except ValueError:
    print(colored("bits_per_param must be an integer", "red"))
    exit(1)


header()

search(
    experiment_identifier,
    dimensions,
    objective_function,
    objective_function_arg,
    crossover,
    selection,
    tournament_percentage,
    export_parameters,
    seed,
    p_local,
    max_local_gens,
    bits_per_param,
)

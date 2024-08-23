import random
import sys

from opfunu.cec_based.cec2014 import F12014
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


if len(sys.argv) < 3:
    print(
        colored(
            "Usage: python main.py <objective_function> <export_parameters> <seed>",
            "red",
        )
    )
    exit(1)

try:
    seed = int(sys.argv[3])
    if seed < 0:
        print(colored("Seed must be a non-negative integer", "red"))
        exit(1)
except IndexError:
    seed = random.randint(0, 2**32 - 1)
except ValueError:
    print(colored("Seed must be an integer", "red"))
    exit(1)

objective_function = sys.argv[1]
export_parameters = sys.argv[2]

header()

if objective_function == "SquareSum":
    search(SquareSum, "SquareSum", seed, export_parameters == "True")
elif objective_function == "F12014":
    search(F12014, "F12014", seed, export_parameters == "True")
else:
    print(colored("Objective function not found", "red"))

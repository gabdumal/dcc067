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


header()

# Run
# search(SquareSum, "SquareSum", export_parameters=True)
# search(SquareSum, "SquareSum")
# search(SquareSum, "SquareSum")
search(F12014, "F12014", export_parameters=True)
search(F12014, "F12014")
search(F12014, "F12014")

from termcolor import colored
from square_sum.main import square_sum
from convex.main import convex


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
# square_sum()
convex()

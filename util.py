from termcolor import colored
import constants


def print_parameter(name: str, value):
    print(colored(f"{name}:", attrs=["bold"]), end=" ")
    print(value)


def print_constant_parameters():
    print_parameter("Tamanho da população", constants.population_size)

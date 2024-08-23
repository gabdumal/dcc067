import numpy as np
from termcolor import colored


def print_parameter(name: str, value: any, printing_function, fancy=True):
    if fancy:
        printing_function(colored(f"{name}:", attrs=["bold"]), end=" ")
        printing_function(value)
    else:
        if isinstance(value, np.ndarray):
            value_str = np.array2string(value, separator=", ", max_line_width=np.inf)
        else:
            value_str = str(value)
        printing_function(f"{name}: {value_str}\n")


def print_parameters(parameters, printing_function=print, fancy=True):
    for parameter in parameters:
        print_parameter(parameter, parameters[parameter], printing_function, fancy)


def print_header(title: str):
    print(colored(f"=-= {title} =-=", on_color="on_white", attrs=["bold"]))

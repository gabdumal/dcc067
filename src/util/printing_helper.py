from termcolor import colored


def print_parameter(name: str, value):
    print(colored(f"{name}:", attrs=["bold"]), end=" ")
    print(value)


def print_parameters(parameters):
    for parameter in parameters:
        print_parameter(parameter, parameters[parameter])


def print_header(title: str):
    print(colored(f"=-= {title} =-=", on_color="on_white", attrs=["bold"]))

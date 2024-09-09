import sys
from opfunu.cec_based.cec2005 import F62005, F92005
from pyparsing import List


def get_objective_function(objective_function_name: str):
    if objective_function_name == "F62005":
        return F62005
    elif objective_function_name == "F92005":
        return F92005
    else:
        raise ValueError(f"Objective function {objective_function_name} not found.")


def get_fitness(objective_function_name: str, solution_str: str):
    objective_function = get_objective_function(objective_function_name)

    solution_str = solution_str.replace("[", "").replace("]", "")
    dimensions_values = solution_str.split(";")
    solution = []
    for value in dimensions_values:
        solution.append(float(value))

    dimensions = len(solution)

    objective_function_instance = objective_function(dimensions)

    return objective_function_instance.evaluate(solution)


if len(sys.argv) < 3:
    print("Usage: python get_fitness.py <objective_function_name> <solution>")
    sys.exit(1)

objective_function_name = sys.argv[1]
solution = sys.argv[2]

fitness = get_fitness(objective_function_name, solution)
print(fitness)

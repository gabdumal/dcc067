from mealpy import FloatVar, GA
from opfunu.cec_based.cec2014 import F12014

objective_function = F12014(ndim=30)


def objective_function_wrapper(solution):
    return objective_function.evaluate(solution)


problem_dictionary = {
    "obj_func": objective_function_wrapper,
    "bounds": FloatVar(
        lb=([-100] * 30),
        ub=([100] * 30),
    ),
    "minmax": "min",
}

optimizer = GA.EliteSingleGA(
    epoch=10000,
    pop_size=100,
    pc=0.9,
    pm=0.8,
    selection="tournament",  # ["roulette", "tournament", "random"], default = "tournament"
    crossover="arithmetic",  # ["one_point", "multi_points", "uniform", "arithmetic"], default = "uniform"
    mutation="flip",  # mutation (str): Optional, can be ["flip", "swap", "scramble","inversion"]
    elite_best=0.1,
    elite_worst=0.3,
    strategy=0,
)

optimizer.solve(problem_dictionary)

print(f"Best solution: {optimizer.g_best.solution}")
print(f"Best fitness: {optimizer.g_best.target.fitness}")

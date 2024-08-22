from mealpy import FloatVar, GA
import numpy as np


def objective_function(solution):
    return np.sum(solution**2)


problem_dictionary = {
    "obj_func": objective_function,
    "bounds": FloatVar(
        lb=([-100] * 30),
        ub=([100] * 30),
    ),
    "minmax": "min",
}

optimizer = GA.BaseGA(
    epoch=100,
    pop_size=50,
    pc=0.85,
    pm=0.1,
)

optimizer.solve(problem_dictionary)

print(optimizer.g_best.solution)
print(optimizer.g_best.target.fitness)

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

optimizer = GA.BaseGA(
    epoch=100,
    pop_size=50,
    pc=0.85,
    pm=0.1,
)

optimizer.solve(problem_dictionary)

print(optimizer.g_best.solution)
print(optimizer.g_best.target.fitness)

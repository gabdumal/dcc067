from mealpy import GA, FloatVar
from opfunu.cec_based.cec2014 import F12014

# para a escrita em arquivo foi concatenada a letra g simbolizando global
dimensions = 10
gEpoch = 5000
gPop_size = 50
gPc = 0.9
gPm = 0.005
gSelection = "roulette"  # "roulette", "tournament", default = "tournament"
gK_way = 0.2
gCrossover = "one_point"  # "one_point", "arithmetic", default = "uniform"
gMutation = "inversion"  # "flip", "swap", "scramble","inversion"
# gElite_best = 0.1
# gElite_worst = 0.3
gStrategy = 0

targetFunction = "1"

file_name = f"results/F{targetFunction}2014/EliteSingleGA-{gSelection}-{gCrossover}-{gMutation}-{dimensions}.txt"


objective_function = F12014(ndim=dimensions)


def objective_function_wrapper(solution):
    return objective_function.evaluate(solution)


problem_dictionary = {
    "obj_func": objective_function_wrapper,
    "bounds": FloatVar(
        lb=([-100] * dimensions),
        ub=([100] * dimensions),
    ),
    "minmax": "min",
}

optimizer = GA.EliteSingleGA(
    epoch=gEpoch,
    pop_size=gPop_size,
    pc=gPc,
    pm=gPm,
    selection=gSelection,
    k_way=gK_way,
    crossover=gCrossover,
    mutation=gMutation,
    # elite_best=gElite_best,
    # elite_worst=gElite_worst,
    strategy=gStrategy,
)

optimizer.solve(problem_dictionary)

print(f"Best solution: {optimizer.g_best.solution}")
print(f"Best fitness: {optimizer.g_best.target.fitness}")
with open(file_name, "a") as file:
    file.write(
        f"Parameters:\nepoch={gEpoch}\npop_size={gPop_size}\npc={gPc}\npm={gPm}\nselection={gSelection}\nk_way={gK_way}\ncrossover={gCrossover}\nmutation={gMutation}\nstrategy={gStrategy}\ndimensions={dimensions}\n"
        # \nelite_best={gElite_best}
        # \nelite_worst={gElite_worst}
        f"Best solution: {optimizer.g_best.solution}\n"
        f"Best fitness: {optimizer.g_best.target.fitness}\n"
        f"---------------------------------------------------------------------------------\n"
    )

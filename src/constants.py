ga_target: str = "min"
ga_population_size: int = 50
ga_crossover_rate: float = 0.9
ga_mutation: str = "flip"
ga_mutation_rate: float = 0.05
ga_elitism_best_rate: float = 0.1
ga_elitism_worst_rate: float = 0.3
ga_epochs: int = 5000

ma_target: str = "min"
ma_population_size: int = 50
ma_crossover_rate: float = 0.85
ma_mutation: str = "flip"
ma_mutation_rate: float = 0.15
p_local: float = 0.5
max_local_gens = 10
bits_per_param = 4
ma_epochs: int = 2000


# CEC-2014 functions

## Convex
### F12014 - Rotated High Conditioned Elliptic Function
### F22014 - Rotated Bent Cigar

## Non-convex
### F42014 - Shifted and Rotated Rosenbrock’s Function
### F52014 - Shifted and Rotated Ackley's

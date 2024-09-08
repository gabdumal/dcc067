target: str = "min"
population_size: int = 50
crossover_rate: float = 0.9
mutation: str = "flip"
mutation_rate: float = 0.05
elitism_best_rate: float = 0.1
elitism_worst_rate: float = 0.3
epochs: int = 5000

# CEC-2014 functions

## Convex
### F12014 - Rotated High Conditioned Elliptic Function
### F22014 - Rotated Bent Cigar

## Non-convex
### F42014 - Shifted and Rotated Rosenbrock’s Function
### F52014 - Shifted and Rotated Ackley's

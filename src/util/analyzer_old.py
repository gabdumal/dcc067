import re

targetFunction = "1"


def process_fitness_files(file_paths):
    fitness_values = []

    for file_path in file_paths:
        with open(file_path, "r") as file:
            for line in file:
                match = re.search(r"Best fitness: \s*([0-9\.-]+)", line)
                if match:
                    fitness_value = float(match.group(1))
                    fitness_values.append(fitness_value)

    if not fitness_values:
        print("Nenhum valor de 'Best fitness: ' encontrado.")
        return

    average_fitness = sum(fitness_values) / len(fitness_values)
    min_fitness = min(fitness_values)

    file_name = file_paths[0]  # Nome do arquivo de saída é o primeiro da lista
    with open(file_name, "a") as file:
        file.write(
            f"Média de aptidão: {average_fitness}\n" f"Melhor aptidão: {min_fitness}\n"
        )

    return average_fitness, min_fitness


file_paths = [
    f"results/F{targetFunction}2014/EliteSingleGA-roulette-one_point-inversion-10.txt"
]
process_fitness_files(file_paths)

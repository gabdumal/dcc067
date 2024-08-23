import os
import re
import sys

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

objetive_functions = ["F12014", "F52014"]
crossovers = ["one_point", "arithmetic"]
selections = ["roulette", "tournament"]
tournament_percentages = [0.1, 0.2, 0.3, 0.4, 0.5]


def get_results_directories_paths_for_roulette(
    experiment_identifier: str, objetive_function, crossover
):
    result_path = f".results/{experiment_identifier}/EliteSingleGA/{objetive_function}/{crossover}/roulette"
    return os.path.join(project_root, result_path)


def get_results_directories_paths_for_tournament(
    experiment_identifier: str,
    objetive_function,
    crossover,
    tournament_percentage,
):
    result_path = f".results/{experiment_identifier}/EliteSingleGA/{objetive_function}/{crossover}/tournament/{tournament_percentage}"
    return os.path.join(project_root, result_path)


def get_csv_header():
    return "Objective function,Crossover,Selection,Tournament percentage,Seed,Algorithm solution,Algorithm fitness\n"


def get_compilation_file_path(experiment_identifier: str):
    return os.path.join(project_root, f"results/{experiment_identifier}.csv")


def write_csv_header(file):
    file.write(get_csv_header())


def get_solution_output(result_path):
    with open(result_path, "r") as file:
        lines = file.readlines()
    solution_output = {}
    for line in lines:
        if re.match(r"Algorithm solution", line):
            solution_output["Algorithm solution"] = (
                line.split(":")[1].strip().replace(",", ";")
            )
        elif re.match(r"Algorithm fitness", line):
            solution_output["Algorithm fitness"] = line.split(":")[1].strip()
    return solution_output


def write_csv_line(
    file,
    objetive_function,
    crossover,
    selection,
    tournament_percentage,
    seed,
    solution_output,
):
    file.write(
        f"{objetive_function},{crossover},{selection},{tournament_percentage},{seed},{solution_output['Algorithm solution']},{solution_output['Algorithm fitness']}\n"
    )


def compile_results(experiment_identifier: str):
    with open(get_compilation_file_path(experiment_identifier), "w+") as file:
        write_csv_header(file)
        for objetive_function in objetive_functions:
            for crossover in crossovers:
                for selection in selections:
                    if selection == "roulette":
                        result_path = get_results_directories_paths_for_roulette(
                            experiment_identifier, objetive_function, crossover
                        )
                        for file_name in os.listdir(result_path):
                            seed = file_name.split(".")[0]
                            solution_output = get_solution_output(
                                os.path.join(result_path, file_name)
                            )
                            write_csv_line(
                                file,
                                objetive_function,
                                crossover,
                                selection,
                                None,
                                seed,
                                solution_output,
                            )
                    for tournament_percentage in tournament_percentages:
                        result_path = get_results_directories_paths_for_tournament(
                            experiment_identifier,
                            objetive_function,
                            crossover,
                            tournament_percentage,
                        )
                        for file_name in os.listdir(result_path):
                            seed = file_name.split(".")[0]
                            solution_output = get_solution_output(
                                os.path.join(result_path, file_name)
                            )
                            write_csv_line(
                                file,
                                objetive_function,
                                crossover,
                                selection,
                                tournament_percentage,
                                seed,
                                solution_output,
                            )


def experiment_exists(experiment_identifier: str):
    return os.path.exists(
        os.path.join(project_root, f".results/{experiment_identifier}")
    )


def run():
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <experiment_identifier>")
        exit(1)
    experiment_identifier = sys.argv[1]
    if not experiment_exists(experiment_identifier):
        print("Experiment not found")
        exit(1)
    compile_results(experiment_identifier)


run()

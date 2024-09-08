import os
import re
import sys

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

possible_optimizers = ["OriginalMA", "EliteSingleGA"]
possible_dimensions = [10, 20]
objetive_functions = ["F12014", "F42014", "F52014", "F62005", "F92005"]
crossovers = ["one_point", "arithmetic"]
selections = ["roulette", "tournament"]
tournament_percentages = [0.1, 0.2, 0.3, 0.4, 0.5]


def get_experiment_directory_path(experiment_identifier: str):
    return os.path.join(project_root, ".results", experiment_identifier)


def experiment_exists(experiment_directory_path: str):
    return os.path.exists(get_experiment_directory_path(experiment_directory_path))


def get_compilation_directory_path(experiment_identifier: str):
    return os.path.join(project_root, "results", experiment_identifier)


def write_csv_header(file, params: dict):
    header = ""
    for key in params.keys():
        header += f"{key},"
    header += "Seed,Algorithm solution,Algorithm fitness\n"
    file.write(header)


def write_csv_line(
    file,
    parameters: dict,
    seed,
    solution_output,
):
    line = ""
    for key in parameters.keys():
        line += f"{parameters[key]},"
    line += f"{seed},{solution_output['Algorithm solution']},{solution_output['Algorithm fitness']}\n"
    file.write(line)


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


def process_files(file, results_path: str, parameters: dict):
    for result in os.listdir(results_path):
        seed = result.split(".")[0]
        solution_output = get_solution_output(os.path.join(results_path, result))
        write_csv_line(file, parameters, seed, solution_output)


def write_results(file, dimension_experiment_path: str, parameters: dict):
    write_csv_header(file, parameters)

    for objective_function in objetive_functions:
        objective_function_experiment_path = os.path.join(
            dimension_experiment_path, objective_function
        )
        if not os.path.exists(objective_function_experiment_path):
            continue
        parameters["Objective function"] = objective_function

        for crossover in crossovers:
            crossover_experiment_path = os.path.join(
                objective_function_experiment_path, crossover
            )
            if not os.path.exists(crossover_experiment_path):
                continue
            parameters["Crossover"] = crossover

            for selection in selections:
                selection_experiment_path = os.path.join(
                    crossover_experiment_path, selection
                )
                if not os.path.exists(selection_experiment_path):
                    continue
                parameters["Selection"] = selection

                if selection == "tournament":
                    for tournament_percentage in tournament_percentages:
                        tournament_experiment_path = os.path.join(
                            selection_experiment_path, str(tournament_percentage)
                        )
                        if not os.path.exists(tournament_experiment_path):
                            continue
                        parameters["Tournament percentage"] = tournament_percentage

                        process_files(file, tournament_experiment_path, parameters)
                        continue

                else:
                    process_files(file, selection_experiment_path, parameters)
                    continue


def compile_results(experiment_identifier: str):
    experiment_path = get_experiment_directory_path(experiment_identifier)
    compilation_path = get_compilation_directory_path(experiment_identifier)

    parameters: dict = {
        "Objective function": "",
        "Crossover": "",
        "Selection": "",
        "Tournament percentage": "",
    }

    for optimizer in possible_optimizers:
        optimizer_experiment_path = os.path.join(experiment_path, optimizer)
        optimizer_path = os.path.join(experiment_path, optimizer)
        if not os.path.exists(optimizer_path):
            continue
        compilation_path = os.path.join(compilation_path, optimizer)

        for dimensions in possible_dimensions:
            dimension_experiment_path = os.path.join(
                optimizer_experiment_path, str(dimensions)
            )
            dimensions_path = os.path.join(optimizer_path, str(dimensions))
            if not os.path.exists(dimensions_path):
                continue
            compilation_path = os.path.join(compilation_path, str(dimensions))

            os.makedirs(compilation_path, exist_ok=True)
            compilation_file_path = os.path.join(compilation_path, "results.csv")
            with open(compilation_file_path, "w+") as file:
                write_results(file, dimension_experiment_path, parameters)


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

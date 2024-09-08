#!/bin/bash

echo "DCC067 Computação Evolucionista"
echo "Experimento com o algoritmo genético OriginalMA"
echo

readonly possible_dimensions=(10)

# Convex
readonly objective_functions=("F62005")
readonly selections=("tournament")
readonly tournament_percentages=(0.2)
readonly crossovers=("arithmetic")

# # Non-convex
# readonly objective_functions=("F92005")
# readonly selections=("tournament")
# readonly tournament_percentages=(0.5)
# readonly crossovers=("one_point")

readonly now=$(date)
readonly experiment_identifier="experiment_$(date +'%Y%m%d%H%M%S')"

readonly total_executions=$((10 * ${#objective_functions[@]} * ${#possible_dimensions[@]} * ${#crossovers[@]} * (${#tournament_percentages[@]})))
execution=1

for objective_function in ${objective_functions[@]}; do
    echo "Função objetivo: $objective_function"
    echo
    for i in {1..10}; do
        echo "Executando busca ($i/10)..."
        for dimensions in ${possible_dimensions[@]}; do
            for crossover in ${crossovers[@]}; do
                for selection in ${selections[@]}; do
                    if [ $selection == "tournament" ]; then
                        for tournament_percentage in ${tournament_percentages[@]}; do
                            echo "Executando iteração ($execution/$total_executions)."
                            echo "Seleção: $selection. Crossover: $crossover. Torneio: $tournament_percentage."
                            python src/main.py original_ma $experiment_identifier $dimensions $objective_function $crossover $selection $tournament_percentage True None
                            execution=$((execution + 1))
                            echo
                        done
                    else
                        echo "Executando iteração ($execution/$total_executions)."
                        echo "Seleção: $selection. Crossover: $crossover."
                        python src/main.py original_ma $experiment_identifier $dimensions $objective_function $crossover $selection None True None
                        execution=$((execution + 1))
                        echo
                    fi
                done
            done
        done
        echo
    done
    echo "Execução da função objetivo $objective_function concluída."
    echo
    echo
done

echo "Todas as execuções foram concluídas."
echo

echo "Compilando resultados..."
python src/util/compile_results.py $experiment_identifier
echo

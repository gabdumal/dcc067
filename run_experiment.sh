#!/bin/bash

echo "DCC067 Computação Evolucionista"
echo "Experimento com o algoritmo genético EliteSingleGA"
echo

readonly objective_functions=("F12014" "F52014")
readonly selections=("roulette" "tournament")
readonly tournament_percentages=(0.1 0.2 0.3 0.4 0.5)
readonly crossovers=("one_point" "arithmetic")

now=$(date)
readonly experiment_identifier="experiment_$(date +'%Y%m%d%H%M%S')"

for objective_function in ${objective_functions[@]}; do
    echo "Função objetivo: $objective_function"
    echo
    for i in {1..10}; do
        echo "Executando busca ($i/10)..."
        for crossover in ${crossovers[@]}; do
            for selection in ${selections[@]}; do
                if [ $selection == "tournament" ]; then
                    for tournament_percentage in ${tournament_percentages[@]}; do
                        echo "Executando algoritmo genético com seleção $selection, crossover $crossover e torneio de $tournament_percentage..."
                        python src/main.py $experiment_identifier $objective_function $crossover $selection $tournament_percentage True None
                        echo
                    done
                else
                    echo "Executando algoritmo genético com seleção $selection e crossover $crossover..."
                    python src/main.py $experiment_identifier $objective_function $crossover $selection None True None
                    echo
                fi
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

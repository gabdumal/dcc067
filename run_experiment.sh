#!/bin/bash

echo "DCC067 Computação Evolucionista"
echo "Experimento com o algoritmo MA.OriginalMA"
echo

readonly possible_dimensions=(30)
readonly objective_functions=("F62005" "F92005")
readonly selections=("roulette" "tournament")
readonly tournament_percentages=(0.1 0.2 0.3 0.4 0.5)
readonly crossovers=("one_point" "arithmetic")

# Parâmetros fixos para a segunda parte do trabalho
readonly epoch=5000
readonly pop_size=50
readonly pc=0.85
readonly pm=0.15
readonly p_local=0.5
readonly max_local_gens=10
readonly bits_per_param=4

readonly now=$(date)
readonly experiment_identifier="experiment_$(date +'%Y%m%d%H%M%S')"

readonly total_executions=$((10 * ${#objective_functions[@]} * ${#possible_dimensions[@]} * ${#crossovers[@]} * (${#selections[@]} + ${#tournament_percentages[@]})))
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
                            python src/main.py $experiment_identifier $dimensions $objective_function $crossover $selection $tournament_percentage True None $p_local $max_local_gens $bits_per_param $epoch $pop_size $pc $pm
                            execution=$((execution + 1))
                            echo
                        done
                    else
                        echo "Executando iteração ($execution/$total_executions)."
                        echo "Seleção: $selection. Crossover: $crossover."
                        python src/main.py $experiment_identifier $dimensions $objective_function $crossover $selection None True None $p_local $max_local_gens $bits_per_param $epoch $pop_size $pc $pm
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

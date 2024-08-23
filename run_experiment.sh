#!/bin/bash

echo "DCC067 Computação Evolucionista"
echo "Experimento com o algoritmo genético EliteSingleGA"
echo

readonly objective_functions=("SquareSum" "F12014")

for objective_function in ${objective_functions[@]}; do
    echo "Função objetivo: $objective_function"
    echo
    echo "Executando busca (1/10)..."
    python src/main.py $objective_function True
    for i in {2..10}; do
        echo
        echo "Executando busca ($i/10)..."
        python src/main.py $objective_function False
    done
    echo
    echo "Execução da função objetivo $objective_function concluída."
    echo
    echo
done

echo "Todas as execuções foram concluídas."
echo

echo "Analisando os resultados..."
# python analyzer.py
echo "Os resultados foram analisados."

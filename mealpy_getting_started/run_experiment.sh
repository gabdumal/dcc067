#!/bin/bash

for i in {1..10}
do
  echo "Executando a vez $i..."
  python experimentEliteSingleGA.py
  echo "Execução $i concluída."
done

echo "Todas as execuções foram concluídas."
python analyzer.py
echo "Os resultados foram analisados."

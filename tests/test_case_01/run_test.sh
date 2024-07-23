#!/bin/bash

# Chemin vers l'algorithme
ALGO_PATH="../../algorithmes/algo_principal.py"
INPUT_FILE="input.csv"
EXPECTED_OUTPUT_FILE="expected_output.csv"
RESULT_PATH="../../results"
ERROR_LOG="$RESULT_PATH/error.log"

# Assurer que le dossier de résultats existe
mkdir -p $RESULT_PATH

# Exécuter l'algorithme avec les données d'entrée spécifiques
python3 $ALGO_PATH input.csv 2>> $ERROR_LOG

# Sauvegarder les résultats dans le dossier results
cp output.csv $RESULT_PATH/output_$(basename $(pwd)).csv

now=$(date +"%Y-%m-%d %H:%M:%S")

# Comparer les résultats
if diff -w output.csv expected_output.csv > /dev/null; then
    echo "$now : $(basename $(pwd)) PASSED"
    echo "$now : $(basename $(pwd)) PASSED" >> $RESULT_PATH/results_summary.txt
else
    echo "$now : $(basename $(pwd)) FAILED"
    echo "$now : $(basename $(pwd)) FAILED" >> $RESULT_PATH/results_summary.txt
	diff -w output.csv expected_output.csv >> $RESULT_PATH/diff_$(basename $(pwd)).txt
fi

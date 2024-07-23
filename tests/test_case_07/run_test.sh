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
echo "Running algorithm..."
python3 $ALGO_PATH $INPUT_FILE 2>> $ERROR_LOG

# Vérifier si le fichier de sortie a été généré
if [[ ! -f output.csv ]]; then
    echo "ERROR: output.csv not found!" >> $ERROR_LOG
    echo "$now : $(basename $(pwd)) FAILED - output.csv not found" >> $RESULT_PATH/results_summary.txt
    exit 1
fi

# Sauvegarder les résultats dans le dossier results
cp output.csv $RESULT_PATH/output_$(basename $(pwd)).csv

now=$(date +"%Y-%m-%d %H:%M:%S")

# Comparer les résultats
if diff -w output.csv $EXPECTED_OUTPUT_FILE > /dev/null; then
    echo "$now : $(basename $(pwd)) PASSED"
    echo "$now : $(basename $(pwd)) PASSED" >> $RESULT_PATH/results_summary.txt
else
    echo "$now : $(basename $(pwd)) FAILED"
    echo "$now : $(basename $(pwd)) FAILED" >> $RESULT_PATH/results_summary.txt
    diff -w output.csv $EXPECTED_OUTPUT_FILE >> $RESULT_PATH/diff_$(basename $(pwd)).txt
fi

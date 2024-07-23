#!/bin/bash

# Chemin vers le fichier de log des erreurs
ERROR_LOG="../results/error.log"

# Exécuter le setup
./setup_environment.sh

# Boucle à travers tous les dossiers de test
for test_dir in ../tests/*; do
    if [ -d "$test_dir" ]; then
        echo "Running test in $test_dir..."
        # Appeler le script run_test.sh spécifique à chaque test
        (cd $test_dir && ./run_test.sh) 2>> $ERROR_LOG
        if [ $? -ne 0 ]; then
            echo "$(date) - Error occurred in $test_dir" >> $ERROR_LOG
        fi
    fi
done

# Nettoyer après les tests
./cleanup_environment.sh

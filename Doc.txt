Document de Validation et Vérification (V&V)
1. Introduction
Ce document décrit le processus de Validation et Vérification pour un banc de test automatisé, implémenté via un script Bash. Ce banc de test est conçu pour valider un algorithme spécifique selon les règles d'affaires fournies.

2. Configuration de l'Environnement
Script : setup_environment.sh

Objectif : Préparer l'environnement de test en installant les dépendances nécessaires, notamment Python, et en configurant les paramètres spécifiques à l'OS.
Exécution : Automatiquement lancé par le script principal run_test.sh. Il détecte l'OS et installe Python si ce n'est pas déjà fait.
3. Exécution des Tests
Script : run_test.sh

Emplacement : Se trouve dans le dossier script.
Fonctionnement :
Setup : Initialise l'environnement en exécutant setup_environment.sh.
Tests : Parcourt tous les dossiers de test sous ../tests/ et exécute le script run_test.sh dans chaque sous-dossier.
Log des erreurs : Redirige les erreurs dans ../results/error.log.
Nettoyage : Exécute cleanup_environment.sh pour réinitialiser l'environnement après les tests.
4. Gestion des Résultats
Dossier de résultats : ../results/
Fichiers de sortie : Les résultats de chaque test sont sauvegardés sous la forme output_<nom_du_dossier_de_test>.csv.
Résumé des tests : Un fichier results_summary.txt est mis à jour pour chaque test, indiquant si le test a été réussi ou échoué.
Différences : Pour les tests échoués, les différences sont enregistrées dans diff_<nom_du_dossier_de_test>.txt.
5. Critères d'Évaluation
Validité des Tests : Les tests sont considérés comme valides si l'exécution complète le processus sans erreurs et si les fichiers de sortie correspondent aux résultats attendus.
Automatisation : Le processus de test est entièrement automatisé, nécessitant aucune intervention manuelle après le lancement initial du script run_test.sh.
6. Conclusion
Ce banc de test permet une évaluation automatisée et fiable de l'algorithme selon les spécifications fournies. Il assure une couverture de test exhaustive grâce à la vérification automatique des résultats et à la journalisation détaillée des erreurs.

Usage du Script
Pour exécuter le banc de test :

Naviguez vers le dossier script.
Lancez le script via la commande : ./run_test.sh.
Assurez-vous que tous les scripts (setup_environment.sh, run_test.sh, cleanup_environment.sh) sont exécutables. Vous pouvez les rendre exécutables avec la commande : chmod +x <nom_du_script>.sh.
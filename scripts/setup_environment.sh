#!/bin/bash
echo "Setting up the test environment..."
# Créer les dossiers nécessaires si non existants
install_python() {
    case "$1" in
        "Ubuntu"|"Debian")
            sudo apt update
            sudo apt install python3 python3-pip -y
            ;;
        "CentOS"|"Fedora")
            sudo yum update
            sudo yum install python3 python3-pip -y
            ;;
        "Arch")
            sudo pacman -Syu
            sudo pacman -S python python-pip --noconfirm
            ;;
        *)
            echo "OS non supporté ou Python déjà installé."
            ;;
    esac
}

# Détecter le système d'exploitation
os_type=$(grep '^ID=' /etc/os-release | sed -e 's/^ID=//')

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "Python 3 n'est pas installé. Installation en cours..."
    install_python "$os_type"
else
    echo "Python 3 est déjà installé."
fi

mkdir -p ../results
echo "Environment setup complete."

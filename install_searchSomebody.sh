#!/bin/bash

echo -e "\033[1;37m Installation de HomeBrew - (Gestionnaire de téléchargement)... [cURL requis]\033[1;34m"
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo -e "\033[1;32m[Terminé]\033[1;34m"

echo -e "\033[1;37m# Installation de Wget - Le téléchargeur de fichiers...[Homebrew requis]\033[1;34m"
brew install wget
echo -e "\033[1;32m[Terminé]\033[1;34m"

echo -e "\033[1;37m# Installation de chromedriver - Le pilote de navigateur Chrome...[Homebrew requis]\033[1;34m"
brew install chromedriver
echo -e "\033[1;32m[Terminé]\033[1;34m"

echo -e "\033[1;37mInstallation de PIP : Le gestionnaire de téléchargement de bibliothèques Python...[get-pip.py requis]\033[1;34m"
wget "https://bootstrap.pypa.io/get-pip.py"
python3 get-pip.py
echo -e "\033[1;32m[Terminé]\033[1;34m"

echo -e "\033[1;37mInstallation de Selenium - Le robot navigateur...[Pip requis]\033[1;34m"
pip install selenium
echo -e "\033[1;32m[Terminé]\033[1;34m"

echo -e "\033[1;32mSearchSomebody est prêt à être lancé !\033[1;34m"

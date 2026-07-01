#!/usr/bin/env bash
# =============================================================================
#  install_docker_macos.sh  —  Installer Docker Desktop sur macOS
#  Sprint 3 CISIA · InduSense 4.0 · pour le J3 (modules 27 Docker + 28 compose)
# -----------------------------------------------------------------------------
#  Marche sur Mac Apple Silicon (M1/M2/M3...) ET Intel. À lancer ainsi :
#     chmod +x install_docker_macos.sh
#     ./install_docker_macos.sh
#  (Homebrew et Docker demanderont ton mot de passe macOS : c'est normal.)
# =============================================================================
set -euo pipefail   # -e: stop à la 1re erreur · -u: variable non définie = erreur · pipefail: erreur dans un pipe = erreur

echo "== Installation de Docker Desktop (macOS) =="

# 1) Déjà installé ? Si oui, on ne refait rien.
if command -v docker >/dev/null 2>&1; then
  echo "Docker est déjà présent :"
  docker --version
  echo "Ouvre Docker Desktop s'il n'est pas lancé (icône baleine dans la barre de menus)."
  exit 0
fi

# 2) Homebrew présent ? Sinon on l'installe (gestionnaire de paquets de macOS).
if ! command -v brew >/dev/null 2>&1; then
  echo "-> Homebrew absent : installation..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Ajouter brew au PATH de CETTE session (chemin différent selon la puce) :
  #   - Apple Silicon : /opt/homebrew   - Intel : /usr/local
  if [ -d /opt/homebrew/bin ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
  else
    eval "$(/usr/local/bin/brew shellenv)"
  fi
fi

# 3) Installer Docker Desktop via Homebrew (en « cask » = application avec interface).
#    Selon la version de Homebrew, le cask s'appelle "docker" ou "docker-desktop" :
#    on tente le premier, et on bascule sur le second si besoin.
echo "-> Installation de Docker Desktop..."
if ! brew install --cask docker 2>/dev/null; then
  echo "   (bascule sur le cask 'docker-desktop')"
  brew install --cask docker-desktop
fi

# 4) Lancer Docker Desktop (la première ouverture finalise l'installation).
echo "-> Démarrage de Docker Desktop..."
open -a Docker || open -a "Docker Desktop" || true

# 5) Vérification finale.
echo ""
echo "== Dernière étape =="
echo "Attends que l'icône baleine soit FIXE dans la barre de menus (en haut), puis vérifie :"
echo "   docker --version"
echo "   docker compose version"
echo "   docker run hello-world"
echo ""
echo "Si 'docker run hello-world' affiche un message de bienvenue, le J3 peut commencer."

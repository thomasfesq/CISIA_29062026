#!/usr/bin/env bash
# =============================================================================
# scripts/check_env_macos.sh — Verification de l'environnement (macOS / Linux)
# -----------------------------------------------------------------------------
# ROLE : script shell qui controle que le poste est correctement configure pour
# travailler sur le projet. Il affiche les versions des outils systeme, puis
# prepare l'environnement et lance les verifications du projet (tests, lint,
# format, CLI). A executer une fois au demarrage pour valider son installation.
#
# Lancement (depuis un terminal macOS/Linux) :  bash scripts/check_env_macos.sh
# Format du fichier : script bash (commentaires avec # en debut de ligne).
# =============================================================================

# Ligne "shebang" (tout en haut) : indique d'executer ce script avec bash.
#!/usr/bin/env bash
# Securise l'execution du script :
#   -e          : stoppe au premier echec d'une commande.
#   -u          : erreur si une variable non definie est utilisee.
#   -o pipefail : un echec dans un pipe (|) fait echouer toute la chaine.
set -euo pipefail

# --- Verification des outils SYSTEME (versions installees) ------------------
echo "== System tools =="
# Version de Python 3 ("|| true" : ne bloque pas le script si la commande echoue).
python3 --version || true
# Version de uv (gestionnaire de paquets/venv) : indispensable, donc PAS de "|| true".
uv --version
# Version de git (gestion de versions).
git --version
# Version de Docker (conteneurs) ; optionnel ici, d'ou le "|| true".
docker --version || true

# Ligne vide (lisibilite de l'affichage).
echo
# --- Verifications PROPRES AU PROJET ----------------------------------------
echo "== Project checks =="
# Cree un environnement virtuel base sur Python 3.13.
uv venv --python 3.13
# Installe les dependances du projet + le groupe "dev".
uv sync --extra dev
# Affiche la version de Python utilisee DANS l'environnement (controle).
uv run python --version
# Verifie que le paquet "indusense" s'importe et affiche son emplacement.
uv run python -c "import indusense; print(indusense.__file__)"
# Lance la suite de tests (-q = sortie concise).
uv run pytest -q
# Verifie la qualite du code avec ruff.
uv run ruff check .
# Verifie le formatage du code avec black (--check = ne modifie rien).
uv run black --check .
# Verifie que la commande CLI "indusense" repond (affiche son aide).
uv run indusense --help
# Lance la sous-commande de controle des donnees.
uv run indusense check-data
# Lance la construction des donnees "gold" (preparees).
uv run indusense build-gold

# Repo CISIA_29062026 — version **commentée pour les apprenants**

Ce dossier est une **copie commentée ligne à ligne** du repo `thomasfesq/CISIA_29062026`.
Objectif pédagogique : qu'un apprenant puisse lire **chaque fichier** et comprendre
*ce que fait le code* **et** *pourquoi*, sans connaissance préalable du projet.

> ✅ **Le comportement du code est strictement identique à l'original.** Seuls des
> commentaires (et quelques docstrings) ont été ajoutés. Vérifié de deux façons :
> comparaison **AST** (arbre syntaxique) original vs commenté = **identique** sur les
> 15 fichiers Python, et **suite de tests `pytest` = 14/14 au vert** avec le code commenté.

## Comment t'en servir

- **Pour lire/apprendre** : ouvre les fichiers dans cet ordre conseillé.
- **Pour les utiliser** : tu peux recopier ces fichiers par-dessus ceux de ton repo
  (les commentaires ne changent rien à l'exécution). À toi de voir si tu veux garder
  un repo de prod épuré ou cette version pédagogique.

## Ordre de lecture conseillé

1. `pyproject.toml` — la carte d'identité du projet (dépendances, outils, commandes).
2. `src/indusense/config.py` — les réglages centraux (chemins, graine, cible).
3. `src/indusense/data/loaders.py` — charger et nettoyer les données brutes, fabriquer la cible `panne` (le `merge_asof`).
4. `src/indusense/features/temporal.py` — fabriquer les features `lag`/`rolling` **sans fuite temporelle**.
5. `src/indusense/models/tabular.py` — le modèle (RandomForest), entraînement, prédiction, sauvegarde.
6. `src/indusense/cli.py` — les 4 commandes `indusense` (check-data / build-gold / train / predict).
7. `tests/` — ce que chaque test garantit (anti-fuite, normalisation, isolation par machine).
8. `scripts/generate_synthetic_gold.py` — le générateur de flux de données (200/min).
9. `scripts/demo_versioning.py` — la démo DVC + MLflow (versionner données + modèle).
10. `.pre-commit-config.yaml`, `.github/workflows/ci.yml`, `Makefile`, `.gitignore`, `.env.example` — l'outillage qualité/CI.

## Fichiers commentés (tout le code du repo)

| Catégorie | Fichiers |
|---|---|
| Package | `config.py`, `cli.py`, `data/loaders.py`, `features/temporal.py`, `models/tabular.py` + les `__init__.py` |
| Tests | `test_loaders.py`, `test_package.py`, `test_temporal.py`, `test_temporal_gold.py` |
| Scripts | `generate_synthetic_gold.py`, `demo_versioning.py`, `check_env_macos.sh`, `check_env_windows.ps1` |
| Config/CI | `pyproject.toml`, `.pre-commit-config.yaml`, `.github/workflows/ci.yml`, `Makefile`, `.gitignore`, `.env.example` |

## Non inclus (volontairement, car non « commentables »)

Les **données** (`data/**` : CSV/TSV/SQL), le **modèle binaire** (`artifacts/models/rf.joblib`),
le **verrou de dépendances** (`uv.lock`) et les **README**/markdown déjà rédigés restent ceux du
repo d'origine, inchangés. Récupère-les depuis ton repo `CISIA_29062026`.

---

*Sprint 3 CISIA « Industrialisation & déploiement » · InduSense 4.0 · AELION*

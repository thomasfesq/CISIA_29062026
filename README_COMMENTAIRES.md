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

---

## ⭐ Mise à jour — RÉFÉRENCE COMPLÈTE & commentée (modules 23 → 34)

Ce dépôt n'est plus seulement le *starter* (23-24) : c'est désormais la **solution complète commentée** que les étudiants peuvent étudier de bout en bout. Ajouté depuis le skeleton complet, **commenté ligne à ligne** :

- **`src/indusense/api/`** — l'API FastAPI : `schemas.py` (contrat I/O Pydantic), `security.py` (clé API 401, rate limit 429, taille 413), `model_store.py` (chargement du modèle), `main.py` (`/health`, `/ready`, `/predict-tabular`, `/predict-image`, métriques Prometheus). *(modules 25-26)*
- **`Dockerfile`** + **`.dockerignore`** — image multi-stage, non-root, Variante A. *(module 27)*
- **`docker-compose.yml`** — stack api + PostgreSQL + Prometheus + Grafana. *(module 28)*
- **`monitoring/prometheus.yml`** — scrape de `/metrics`. *(modules 33-34)*
- **`tests/test_api.py`**, **`tests/test_security.py`** — vérifient 200/401/422/413/429 + normalisation `M-7`→`MACH-07`.
- **`payload.json`** — exemple de requête pour `/predict-tabular`.
- `pyproject.toml` complété (fastapi, uvicorn, prometheus-instrumentator, prefect, sqlalchemy, psycopg, scipy, evidently, mlflow…), `config.py` (+ `api_key`, `decision_threshold`), `Makefile` (cible `serve`).

**Hygiène git** : `mlruns/` et `mlflow.db` (artefacts de démo MLflow) sortis du suivi git et ajoutés au `.gitignore`.

✅ **Vérifié** : les 22 fichiers Python compilent et **`pytest` = 22/22 au vert** (loaders, temporal, gold, package, **api**, **sécurité**). `from indusense.api.main import app` fonctionne.

> Note : les modules 29-30 (orchestration Prefect) et 34 (dashboard Grafana en JSON) se construisent en TP — leur **corrigé de code** est dans les fiches corrigé formateur et le tuto, pas un fichier figé du dépôt.

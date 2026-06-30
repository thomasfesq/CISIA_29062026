# InduSense Sprint 3 Starter

Point de depart propre pour demarrer le Sprint 3 CISIA.

Objectif : repartir tous du meme etat, meme si les sprints precedents ont ete
heterogenes. Ce package fournit :

- un vrai package Python en layout `src/` ;
- des donnees brutes InduSense dans `data/raw/` ;
- un dataset gold dans `data/gold/gold_dataset.csv` ;
- des fonctions de chargement et de normalisation ;
- des features temporelles sans fuite de donnees ;
- une CLI `indusense` ;
- des tests `pytest` ;
- une configuration `ruff`, `black`, `pre-commit`.

## Verification rapide

### Windows PowerShell

```powershell
cd "C:\chemin\vers\indusense-sprint3-starter"
uv venv --python 3.13
uv sync --extra dev
uv run python --version
uv run pytest -q
uv run ruff check .
uv run black --check .
uv run indusense --help
```

### macOS / Linux

```bash
cd /chemin/vers/indusense-sprint3-starter
uv venv --python 3.13
uv sync --extra dev
uv run python --version
uv run pytest -q
uv run ruff check .
uv run black --check .
uv run indusense --help
```

La commande `uv run python --version` doit afficher Python 3.13.x. C'est cette
version qui fait foi, pas le `python --version` global de la machine.

## Commandes utiles

```bash
uv run indusense check-data
uv run indusense build-gold
uv run indusense train
uv run indusense predict
```

## Demarrer l'API (Sprint 3, J2)

```bash
uv run uvicorn indusense.api.main:app --reload
```

Puis ouvrir la doc interactive : http://localhost:8000/docs

- `GET /health` : 200 (le serveur est vivant) ;
- `GET /ready`  : 200 si le modele est charge, sinon 503 ;
- `POST /predict-tabular` : prediction de panne (cle API requise).

Exemple d'appel (la cle de demonstration est `dev-key`) :

```bash
curl -X POST http://localhost:8000/predict-tabular \
  -H "X-API-Key: dev-key" -H "Content-Type: application/json" \
  --data @payload.json
```

> Astuce Windows : depuis **PowerShell**, utilise `curl.exe` (pas l'alias `curl`) et remplace l'antislash de fin de ligne par un accent grave ; ou lance la commande depuis **Git Bash / WSL**.

Codes attendus : sans cle -> 401, corps trop gros -> 413, trop de requetes -> 429, donnees invalides -> 422.

## Structure

```text
src/indusense/
  config.py
  cli.py
  data/loaders.py
  features/temporal.py
  models/tabular.py
  api/              # Sprint 3 / J2 : l'API FastAPI
    main.py         #   routes : /health /ready /predict-tabular /predict-image /metrics
    schemas.py      #   contrat d'entree-sortie (Pydantic)
    security.py     #   cle API (401), anti-flood (429), taille max (413)
    model_store.py  #   chargement du modele au demarrage
tests/              # dont test_api.py et test_security.py (J2)
Dockerfile          # J3 : image multi-stage, non-root
docker-compose.yml  # J3 : api + PostgreSQL + Prometheus + Grafana
monitoring/         # J6 : configuration Prometheus
data/sample/
data/raw/
data/gold/
artifacts/models/
```

## Ce que les apprenants doivent retenir

Le notebook sert a explorer. Le package sert a industrialiser.

Le Sprint 3 commence quand le code est :

- importable ;
- testable ;
- reproductible ;
- lanceable par une CLI ;
- protege contre les fuites de donnees temporelles.

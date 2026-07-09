# Post-mortem — incident « maintenance du week-end » InduSense

- **Date de l'incident** : nuit du vendredi (commit `dcf9a97` « maintenance du week-end : mises à jour diverses »)
- **Date de détection** : lundi 08 h 02 (atelier InduSense)
- **Date de résolution** : lundi, branche `reparation-michael`
- **Sévérité** : élevée — installation, API, pipeline de données et monitoring simultanément hors service
- **État de référence certifié** : tag `v1.0-sain`

---

## 1. Résumé

Une « petite maintenance » non tracée a été poussée sur le dépôt de production en un seul commit fourre-tout (`dcf9a97`). Elle a introduit **14 régressions** réparties sur 11 fichiers. Conséquences observées lundi matin :

- l'installation échouait chez les nouveaux arrivants ;
- l'API refusait des clés d'API valides ;
- le pipeline de données perdait des mesures ;
- Grafana / Prometheus étaient injoignables ;
- **et pourtant l'onglet Actions de GitHub restait vert.**

Le prestataire étant injoignable, la remédiation a consisté à ramener chaque fichier à son état certifié `v1.0-sain`, **une correction = un commit**, avec vérification multi-niveaux.

---

## 2. Impact

| Domaine | Symptôme | Utilisateurs touchés |
|---|---|---|
| Onboarding | `uv sync` impossible, doc fausse | Tout nouvel arrivant |
| API | Rejet des clés valides dès la 3ᵉ requête | Tous les clients de l'API |
| Données / ML | Jointure effondrée, fuite temporelle | Modèle & décisions métier |
| Monitoring | Grafana/Prometheus injoignables, alertes drift inversées | Équipe ops |
| CI/CD | Faux signal « vert » masquant tout | Toute l'équipe (confiance) |

---

## 3. Chronologie des causes racines (les 14 pannes)

### Priorité 1 — Environnement réinstallable
| # | Fichier | Sabotage → Correctif | Commit |
|---|---|---|---|
| 1 | `pyproject.toml` | `requires-python = ">=3.99,<4.0"` → `">=3.13,<3.14"` (aucun Python 3.99 n'existe) | `eb11952` |
| 2 | `README.md` | `uv sync --extra all` → `--extra dev` (l'extra `all` n'existe pas) | `9ea27ae` |

### Priorité 2 & 5 — Tests = contrat, et CI honnête
| # | Fichier | Sabotage → Correctif | Commit |
|---|---|---|---|
| 3 | `.github/workflows/ci.yml` | `pytest -q \|\| true` → `pytest -q` (le `\|\| true` forçait un exit 0) | `82e1c7a` |
| 4 | `tests/test_security.py` | `status_code in (200, 429)` → `== 429` (contrat affaibli) | `8fe7d3d` |

### Priorité 3 — API vivante et sûre
| # | Fichier | Sabotage → Correctif | Commit |
|---|---|---|---|
| 5 | `src/indusense/api/security.py` | `rate_limit(limit=2)` → `limit=60` (rejet des clés valides) | `ddecb90` |
| 6 | `src/indusense/api/main.py` | commentaire alias `X-Api-Token` → `X-API-Key` (doc trompeuse) | `1005d8d` |

### Priorité 3 — Pipeline de données conforme
| # | Fichier | Sabotage → Correctif | Commit |
|---|---|---|---|
| 7 | `data/loaders.py` | `normalize_machine_id` sans `:02d` → padding rétabli (`MACH-02`) | `6f971ad` |
| 8 | `data/loaders.py` | pression sans `utc=True/tz_localize(None)` → normalisation tz rétablie | `006de6c` |
| 9 | `data/loaders.py` | `tolerance_minutes=5` → `90` (appariement capteurs) | `bfb5303` |
| 10 | `features/temporal.py` | rolling sans `.shift(1)` → anti-fuite rétabli | `027e609` |
| 11 | `monitoring/drift.py` | seuils PSI inversés → `SURVEILLER=0.10`, `FORT=0.25` | `ba66900` |

### Priorité 4 — Stack compose opérationnelle
| # | Fichier | Sabotage → Correctif | Commit |
|---|---|---|---|
| 12 | `docker-compose.yml` | API `8000:80` → `8000:8000` | `db48775` |
| 13 | `docker-compose.yml` | Grafana `300:3000` → `3000:3000` | `52442b7` |
| 14 | `monitoring/prometheus.yml` | cible `localhost:9109` → `host.docker.internal:9109` | `0b127cc` |

---

## 4. Pourquoi la CI était verte pendant que tout brûlait

C'est le point le plus important de cet incident : **deux sabotages complices** ont neutralisé le seul garde-fou automatisé.

1. **`pytest -q || true`** (`ci.yml`) — en shell, `|| true` remplace le code de sortie de `pytest` par `0`. L'étape « Tests » de GitHub Actions réussissait donc **quel que soit le résultat réel** de la suite. La CI ne testait plus rien, elle affichait juste « vert ».

2. **`assert e.value.status_code in (200, 429)`** (`test_security.py`) — même exécuté, le test de rate-limit ne pouvait plus échouer : il acceptait aussi bien l'absence de limitation (`200`) que la limitation (`429`). Le **contrat** avait été relâché de l'intérieur.

L'effet combiné : un masque au niveau du runner **et** un contrat de test vidé de son sens. Résultat, aucun signal rouge alors que quatre sous-systèmes étaient cassés. C'est l'illustration exacte de l'indice du briefing : *« les tests sont un CONTRAT — mais un contrat, ça se relit »*.

---

## 5. Résolution & vérification

Chaque panne a été corrigée par un commit atomique ramenant le fichier à `v1.0-sain`. Vérification en pyramide :

| Niveau | Contrôle | Résultat |
|---|---|---|
| Statique | `git diff v1.0-sain HEAD` (hors `BRIEFING.md`) | **vide** — code identique à l'état certifié |
| Environnement | `uv sync --extra dev` | **OK** |
| Tests | `uv run pytest -q` | **30 passed** |
| Runtime pipeline | jointure sur `data/drift_source` | **65 625 lignes**, résidu **1,76 %** (réf. ~65 625 / ~1,8 %) |

---

## 6. Ce qui a bien / mal fonctionné

**Mal fonctionné**
- La CI était le seul rempart automatisé, et il était contournable en une ligne (`|| true`).
- Un commit unique et fourre-tout (« mises à jour diverses ») a caché 14 changements hétérogènes.
- Les tests de sécurité pouvaient être affaiblis sans que personne ne le remarque.

**Bien fonctionné**
- L'existence d'un **tag certifié `v1.0-sain`** a permis un diagnostic et une remédiation rapides et sûrs.
- Les **chiffres de référence** documentés (65 625 lignes, 1,8 %) ont donné un critère de validation objectif du pipeline.

---

## 7. Actions correctives & préventives

| Action | Type | Priorité |
|---|---|---|
| Interdire toute construction masquant l'exit code (`\|\| true`, `continue-on-error: true`) dans les steps de test CI | Prévention | Haute |
| Rendre la CI **bloquante** (branch protection : merge interdit si Actions rouge) | Prévention | Haute |
| Interdire les commits fourre-tout : 1 intention = 1 commit, message explicite | Process | Moyenne |
| Revue obligatoire (PR + reviewer) sur `pyproject.toml`, `ci.yml`, `security.py`, `docker-compose.yml`, `prometheus.yml` | Process | Haute |
| Ajouter un test qui vérifie le **nombre de lignes de jointure** et le **taux de résidu** comme garde-fou du pipeline | Détection | Moyenne |
| Surveiller les tests dont les assertions deviennent permissives (`in (…)` sur un statut HTTP) en revue | Détection | Moyenne |
| Healthchecks compose + smoke test post-déploiement (API :8000, Prometheus :9090, Grafana :3000) | Détection | Moyenne |

---

## 8. Leçon principale

> Un pipeline CI n'a de valeur que s'il peut **échouer**. Deux modifications d'une ligne — l'une masquant l'exit code, l'autre relâchant une assertion — ont suffi à transformer le garde-fou en simple voyant décoratif. La règle « les tests sont un contrat » doit s'étendre à la CI elle-même : **la config CI et les assertions font partie du contrat, et se relisent au même titre que le code.**

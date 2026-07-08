# 🚨 BRIEFING — lundi 08 h 02, atelier InduSense

Vendredi soir, « une petite maintenance » a été faite sur le dépôt de production InduSense.
Depuis : l'installation échoue chez les nouveaux arrivants, l'API refuse les clés valides,
le pipeline de données perd des mesures, Grafana est injoignable — et pourtant, détail
troublant : **l'onglet Actions de GitHub est vert**. Le prestataire est injoignable.

Mission du jour, par ordre de priorité :
1. environnement réinstallable (`uv sync --extra dev` fonctionne, doc conforme) ;
2. `uv run pytest -q` → LA suite complète verte, avec des tests IDENTIQUES à `v1.0-sain` ;
3. API vivante et sûre (santé, auth, limites) + pipeline de données conforme aux chiffres
   de référence (jointure ~65 625 lignes, résidu ~1,8 %) ;
4. stack compose opérationnelle (API :8000, Prometheus :9090, Grafana :3000) ;
5. expliquer pourquoi la CI était verte pendant que tout brûlait — et corriger ça ;
6. dépôt propre + post-mortem + restitution.

Indices : le tag `v1.0-sain` = dernier état certifié. Les chiffres de référence sont dans
votre pas à pas. Les tests sont un CONTRAT — mais un contrat, ça se relit.

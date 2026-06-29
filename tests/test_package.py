# =============================================================================
# RÔLE DE CE FICHIER DE TEST : test_package.py
# -----------------------------------------------------------------------------
# C'est un test "fumée" (smoke test) minimal mais important. Il garantit deux
# choses fondamentales avant tout le reste :
#
#   1. Le package "indusense" est bien INSTALLÉ et IMPORTABLE dans
#      l'environnement de test. Si cet import échoue, c'est que le projet
#      n'est pas correctement installé (mauvais environnement, dépendance
#      manquante, package non packagé) : inutile de lancer les autres tests.
#
#   2. La VERSION exposée est celle attendue ("0.1.0"). Cela vérifie que le
#      numéro de version est bien défini et accessible via indusense.__version__
#      (utile pour la traçabilité des modèles / artefacts en MLOps : on saura
#      toujours quelle version de code a produit un résultat).
#
# Ce que ce fichier GARANTIT : l'amorçage du projet est sain (le package
# s'importe) et son identité de version est correcte.
# =============================================================================

# On importe simplement le package racine. Le seul fait que cette ligne
# n'échoue pas prouve déjà que l'installation est fonctionnelle.
import indusense


def test_package_importable():
    # Intention : vérifier que l'attribut de version existe ET vaut "0.1.0".
    # Un échec ici signale soit un package mal installé, soit un oubli de
    # mise à jour / d'exposition du numéro de version.
    assert indusense.__version__ == "0.1.0"

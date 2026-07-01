# QCM#01_Concevoir et implémenter une solution d'intelligence artificielle

**Question 1** C1/ Quelle est la première étape essentielle dans la préparation d'un jeu de données ?
Réponses
* [ ] Entraîner le modèle
* [x] Nettoyer et analyser le jeu de données
* [ ] Choisir les métriques
* [ ] Déployer le modèle

**OK**

**Question 2** C1/ Quelle technique permet de repérer les valeurs aberrantes ?
Réponses
* [ ] Courbe ROC
* [x] Boxplot
* [ ] Histogramme cumulé
* [ ] ACP

**OK**

**Question 3** C1 Quel format est le plus utilisé pour les données tabulaires ?
Réponses
* [ ] PNG
* [x] CSV
* [ ] MP3
* [ ] SVG

**OK (cette question est TRES simple)**

**Question 4** C1 Quel encodage convertit chaque modalité en une colonne binaire ?
Réponses
* [ ] Label Encoding
* [x] One-Hot Encoding
* [ ] Target Encoding
* [ ] Ordinal Encoding

**OK**

> ~~Voici la transcription de ta série de captures d'écran (j'ai regroupé les deux dernières qui étaient identiques).~~
> **-> XD ça c'est un retour chatgpt non ? à virer**

**Question 5** C1 Quelle méthode peut être utilisée pour gérer les valeurs manquantes ?
Réponses
* [ ] Fusion des variables
* [x] Imputation par la moyenne
* [ ] PCA
* [ ] Bagging

**OK**

**Question 6** C2 Un modèle entraîné sur des données historiques peut reproduire des discriminations passées
Réponses
* [x] Vrai
* [ ] Faux

**OK**

**Question 7** C2 Que désigne un dilemme éthique dans un projet d'IA ?
Réponses
* [x] Un arbitrage entre deux valeurs légitimes mais contradictoires
* [ ] Une erreur de programmation
* [ ] Un défaut matériel
* [ ] Un manque de puissance de calcul
* [ ] Une mauvaise interface utilisateur

**OK (bonne question)**

**Question 8** C2 Quel document formalisé permet d'informer officiellement les parties prenantes des risques éthiques identifiés ?
Réponses
* [x] Une note de risques versionnée et partagée
* [ ] Un notebook technique non commenté
* [ ] Un simple tableau de bord interne
* [ ] Un échange oral non tracé
* [ ] Un log système

**OK (bonne question)**

**Question 9** C2 Dans un contexte industriel, quelles données peuvent être considérées comme des données personnelles au sens du RGPD ? (3 bonnes réponses)
Réponses
* [x] Un identifiant opérateur
* [x] Une image où un salarié est visible
* [ ] Une température machine isolée
* [x] Un horodatage recoupable avec un planning
* [ ] Un numéro de série machine seul

**OK (bien, c'est nuancé)**

**Question 10** C2 Dans un jeu de données fortement déséquilibré, quel risque méthodologique peut apparaître ?
Réponses
* [x] Obtenir une accuracy élevée tout en ayant un recall insuffisant
* [ ] Garantir une performance parfaite
* [ ] Supprimer automatiquement les biais
* [ ] Rendre le RGPD inapplicable
* [ ] Éliminer le risque de faux négatifs

**OK (bonne question)**

**Question 11** C4 Quel indicateur permet de suivre les performances d'un modèle en production ?
Réponses
* [ ] WER
* [x] Monitoring
* [ ] Dropout
* [ ] Batch size

**PAS OK -> "indicateur" est mal employé (le monitoring est une pratique, pas un indicateur) ET WER est une vraie métrique de perf : un candidat pourrait légitimement cocher WER. À reformuler**

**Question 12** C4 Quelle cause principale peut dégrader un modèle en production ?
Réponses
* [x] Drift des données
* [ ] Ajout de commentaires dans le code
* [ ] Utilisation d'un GPU
* [ ] Compression ZIP

**OK (mais distracteurs un peu gros)**

**Question 13** C4 Quel outil est utilisé pour suivre la performance d'un modèle en continu ?
Réponses
* [ ] Docker
* [x] Grafana
* [ ] Photoshop
* [ ] PowerPoint

**OK mais Photoshop/PowerPoint -> mets des vrais outils (Prometheus, Kibana, Datadog...)**

**Question 14** C4 Quel élément fait partie du maintien en condition opérationnelle ?
Réponses
* [x] Mise à jour des dépendances
* [ ] Suppression des logs
* [ ] Retrait des sauvegardes
* [ ] Désactivation du monitoring

**OK (distracteurs trop évidents)**

**Question 15** C4 Scénario : Un modèle de prédiction météo perd en précision après l'arrivée de nouveaux capteurs. Quelle est la bonne démarche ? (2 bonnes réponses)
Réponses
* [x] Vérifier le calibrage des nouveaux capteurs
* [x] Vérifier la cohérence des données
* [ ] Modifier le CSS
* [ ] Ajouter plus de GPU

**OK mais les 2 bonnes réponses se recoupent (calibrage = un cas de cohérence). Et "Modifier le CSS" XD**

---

# QCM#02_Concevoir et implémenter une solution d'intelligence artificielle

**Question 1** C1/ Quelle est la première étape essentielle dans la préparation d'un jeu de données ?
Réponses
* [ ] Entraîner le modèle
* [x] Nettoyer et analyser le jeu de données
* [ ] Choisir les métriques
* [ ] Déployer le modèle

**-> doublon EXACT du QCM#01 Q1**

**Question 2** C1/ Quelle technique permet de repérer les valeurs aberrantes ?
Réponses
* [ ] Courbe ROC
* [x] Boxplot
* [ ] Histogramme cumulé
* [ ] ACP

**-> doublon du QCM#01 Q2 (et y'a un "*" qui traîne dans le titre)**

**Question 3** C1/ A quoi sert une matrice de corrélation ?
Réponses
* [ ] Évaluer un modèle
* [x] Mesurer les relations entre variables
* [ ] Nettoyer les données
* [ ] Déployer un modèle

**OK**

**Question 4** C1/ Quel graphique est le plus adapté pour repérer des outliers ?
Réponses
* [ ] Camembert
* [x] Boxplot
* [ ] Diagramme circulaire
* [ ] Histogramme 3D

**PAS OK -> c'est déjà la Q2 (outliers = valeurs aberrantes = boxplot). Doublon DANS le même QCM, à remplacer**

**Question 5** C1/ Quel format est idéal pour stocker de grands volumes de données tabulaires de manière optimisée ?
Réponses
* [ ] JSON
* [ ] CSV
* [x] Parquet
* [ ] TXT

**OK (bonne question, plus exigeante)**

**Question 6** C1/ Quelle est la principale différence entre le One-Hot Encoding et le Label Encoding ?
Réponses
* [ ] Le One-Hot Encoding crée une hiérarchie numérique
* [x] Le One-Hot Encoding crée de nouvelles colonnes binaires, le Label Encoding attribue un entier unique
* [ ] Le Label Encoding est réservé aux images
* [ ] Il n'y a aucune différence

**OK**

**Question 7** C2/ Selon l'AI Act, un système d'IA utilisé pour l'octroi de crédit est classé comme :
Réponses
* [ ] Système à risque minimal
* [x] Système à haut risque
* [ ] Système interdit
* [ ] Système facultatif
* [ ] Système non réglementé

**OK**

**Question 8** C2/ L'analyse automatisée des émotions de salariés par caméra en vue d'évaluer leur performance constitue principalement :
Réponses
* [x] Un risque réglementaire et éthique majeur
* [ ] Un usage sans impact particulier
* [ ] Une pratique encouragée par l'AI Act
* [ ] Un traitement à risque minimal
* [ ] Une obligation légale

**OK (tu pourrais même durcir : la reconnaissance d'émotions au travail est carrément INTERDITE par l'AI Act)**

**Question 9** C2/ Quelles pratiques relèvent d'une approche "privacy by design" ? (3 bonnes réponses)
Réponses
* [x] Définir une durée de conservation adaptée
* [x] Mettre en place un masquage automatique des zones non pertinentes
* [ ] Collecter le maximum de données disponibles
* [x] Limiter les variables aux stricts besoins fonctionnels
* [ ] Conserver les données indéfiniment

**OK**

**Question 10** C2/ La réutilisation de données collectées pour la maintenance à des fins d'évaluation RH constitue :
Réponses
* [x] Un détournement de finalité
* [ ] Une application du principe d'exactitude
* [ ] Une mesure de minimisation
* [ ] Une obligation réglementaire
* [ ] Une anonymisation

**OK**

**Question 11** C4/ Quel indicateur permet de suivre les performances d'un modèle en production ?
Réponses
* [ ] IHM
* [x] Monitoring
* [ ] Dropout
* [ ] Batch size

**OK mais "indicateur" est mal employé pour le monitoring (ici pas de WER en distracteur, donc moins gênant qu'au #01)**

**Question 12** C4/ Quelle cause principale peut dégrader un modèle en production ?
Réponses
* [ ] Ajout de commentaires dans le code
* [ ] Utilisation d'un GPU
* [ ] Compression .ZIP
* [x] Drift des données

**OK (idem QCM#01 Q12)**

**Question 13** C4/ Quand faut-il réentraîner un modèle ?
Réponses
[ ] Tous les jours
* [x] En cas de dérive des données
* [ ] Tous les 10 ans
* [ ] Jamais

**OK mais un bullet a sauté ("Tous les jours" collé à "Réponses")**

**Question 14** C4/ Quel système permet un retour en arrière rapide en cas d'erreur ?
Réponses
* [ ] Hot-reload
* [x] Versionning
* [ ] Dropout
* [ ] Histogramme

**OK (mais "Versionning" -> "Versioning" / "Versionnage")**

**Question 15** C4/ Scénario : Un modèle de détection d'anomalies commence à générer des alertes fausses ou inutiles. Après analyse, l'équipe remarque que les données récentes sont beaucoup plus variées que les données historiques. Quelle action s'impose ?
Réponses
* [ ] Réduire le dataset
* [x] Réentraîner le modèle avec des données récentes
* [ ] Baisser la sensibilité du modèle
* [ ] Supprimer la moitié des features

**OK mais -> ce scénario exact revient dans #04 et #05**

---

# QCM#03_DEMO Concevoir et implémenter une solution d'intelligence artificielle

**Question 1** C1/ Q1 Quel outil Python est le plus utilisé pour manipuler des DataFrames ?
Réponses
* [ ] Flask
* [x] Pandas
* [ ] PyTorch
* [ ] Matplotlib

**OK**

**Question 2** C1/Q2 Quelle technique permet de repérer les valeurs aberrantes ?
Réponses
* [ ] Courbe ROC
* [x] Boxplot
* [ ] Histogramme cumulé
* [ ] ACP
* [ ] ~~Intitulé~~

**OK -> mais "Intitulé" = option fantôme à supprimer**

**Question 3** C1/Q3 Une matrice de corrélation sert à ?
Réponses
* [ ] Évaluer un modèle
* [x] Mesurer les relations entre variables
* [ ] Nettoyer les données
* [ ] Déployer un modèle

**OK (encore le même que les autres QCM)**

**Question 4** C1/Q4 Quel fichier décrit la structure d'un dataset ?
Réponses
* [ ] Dockerfile
* [x] Datasheet
* [ ] Requirements.txt
* [ ] README.md
* [ ] ~~Intitulé~~

**PAS OK -> "README.md" est une réponse défendable aussi (2 réponses possibles = question ambiguë). Et "Intitulé" à virer**

**Question 5** C1/Q5 Quelle technique réduit la dimension d'un dataset ?
Réponses
[x] PCA
* [ ] SVM
* [ ] Gradient Boosting
* [ ] Cross-validation

**OK (un bullet a sauté sur PCA)**

**Question 6** C2/Q1 Quelles mesures techniques contribuent à garantir la sécurité des données et des modèles ? (3 bonnes réponses)
Réponses
* [x] Chiffrement des données au repos et en transit
* [x] Journalisation des accès
* [x] Gestion sécurisée des secrets
* [ ] Partage libre des accès administrateurs
* [ ] Utilisation d'un mot de passe commun

**OK (bonne question)**

**Question 7** C2/Q7 Si un modèle permet indirectement de déduire des informations personnelles sensibles, quel risque est principalement concerné ?
Réponses
* [x] Atteinte à la confidentialité
* [ ] Dérive conceptuelle
* [ ] Compression excessive
* [ ] Normalisation des données
* [ ] Réduction de dimension

**OK (bons distracteurs) -> par contre noté "C2/Q7" alors que ça devrait être Q2**

**Question 8** C2/Q3 Les données de santé utilisées pour entraîner un modèle prédictif sont considérées comme :
Réponses
* [ ] Des données publiques libres d'usage
* [x] Des données sensibles nécessitant une protection renforcée
* [ ] Des données anonymes par défaut
* [ ] Des données commerciales
* [ ] Des données non réglementées

**OK**

**Question 9** C2/Q4 Associer systématiquement des incidents techniques à un opérateur identifié peut entraîner :
Réponses
* [x] Un risque de surveillance injustifiée
* [ ] Une suppression automatique des biais
* [ ] Une neutralité garantie
* [ ] Une amélioration énergétique
* [ ] Aucun impact éthique

**OK**

**Question 10** C2/Q5 Un système conforme techniquement peut néanmoins poser des problèmes sociétaux.
Réponses
* [x] Vrai
* [ ] Faux

**OK**

**Question 11** C4/Q1 Quel élément doit être surveillé pour détecter un problème de performance ?
Réponses
* [x] Temps d'inférence
* [ ] Couleur de l'interface
* [ ] Version du tableur
* [ ] Format du README

**OK sur le fond (distracteurs gag : couleur, tableur...)**

**Question 12** C4/Q2 Quelle cause principale peut dégrader un modèle en production ?
Réponses
* [ ] Ajout de commentaires dans le code
* [ ] Utilisation d'un GPU
* [ ] Compression .ZIP
* [x] Drift des données

**OK (idem partout)**

**Question 13** C4/Q3 Quand faut-il réentraîner un modèle ?
Réponses
* [ ] Tous les jours
* [x] En cas de dérive des données
* [ ] Tous les 10 ans
* [ ] Jamais

**OK (idem)**

**Question 14** C4/Q4 Quel système permet un retour en arrière rapide en cas d'erreur ?
Réponses
* [ ] Hot-reload
* [x] Versionning
* [ ] Dropout
* [ ] Histogramme

**OK (idem)**

**Question 15** C4/Q5 Scénario : Une IA de contrôle qualité détecte des défauts inexistants. Quelles pistes sont à analyser ? (2 bonnes réponses)
Réponses
* [x] Nouvel éclairage
* [ ] Version du navigateur
* [ ] Format des logs
* [x] Paramètres de capture

**OK (bonne question)**

---

# QCM#04_Concevoir et implémenter une solution d'intelligence artificielle

**Question 1** C1/Q1 Quelle analyse identifie les relations entre variables ?
Réponses
* [ ] Matrice ROC
* [x] Matrice de corrélation
* [ ] Gradient descent
* [ ] Validation croisée
* [ ] ~~Intitulé~~

**OK -> "Intitulé" à virer**

**Question 2** C1/Q2 Quelle technique permet de repérer les valeurs aberrantes ?
Réponses
[ ] Courbe ROC
* [x] Boxplot
* [ ] Histogramme cumulé
* [ ] ACP

**OK (un bullet a sauté sur Courbe ROC)**

**Question 3** C1/Q3 Une matrice de corrélation sert à ?
Réponses
* [ ] Évaluer un modèle
* [x] Mesurer les relations entre variables
* [ ] Nettoyer les données
* [ ] Déployer un modèle

**PAS OK -> doublon de la Q1 (même notion : corrélation entre variables)**

**Question 4** C1/Q4 Quel graphique est le plus adapté pour repérer des outliers ?
Réponses
* [ ] Camembert
* [x] Boxplot
* [ ] Diagramme circulaire
* [ ] Histogramme 3D

**PAS OK -> doublon de la Q2 (boxplot/outliers)**

**Question 5** C1/Q4 Quel fichier permet de documenter les données ?
Réponses
[ ] Jenkinsfile
* [ ] Pipfile
* [ ] Dockerfile
* [x] Datasheet

**OK -> mais noté "Q4" alors que c'est la Q5**

**Question 6** C2/Q1 Le cadre européen encourage la sensibilisation des équipes aux enjeux de l'IA (AI literacy).
Réponses
* [x] Vrai
* [ ] Faux

**OK**

> ~~Voici la transcription exacte des questions visibles sur la dernière capture d'écran fournie (image_481f5e.png), sans aucune modification de leur contenu :~~
> **-> XD encore un retour chatgpt, à virer**

**Question 7** C2/Q2 L'utilisation d'un modèle pour classer automatiquement des CV expose principalement à :
Réponses
* [ ] Une amélioration automatique de l'équité
* [ ] Un risque environnemental uniquement
* [x] Un risque de discrimination algorithmique
* [ ] Une neutralité garantie
* [ ] Un risque nul

**OK**

**Question 8** C2/Q3 En matière de transparence, que doit garantir un responsable de traitement ?
Réponses
[x] Informer clairement sur la finalité et les impacts du traitement
* [ ] Refuser toute explication
* [ ] Se limiter aux performances techniques
* [ ] Ne rien communiquer
* [ ] Publier obligatoirement le code source

**OK (bon distracteur "publier le code source") (un bullet a sauté sur la bonne réponse)**

**Question 9** C2/Q4 Quels éléments peuvent favoriser une ré-identification malgré une pseudonymisation ? (4 bonnes réponses)
Réponses
* [x] Une combinaison rare de variables
* [x] Un identifiant stable réutilisé
* [x] Un hash sans mécanisme de protection
* [x] La suppression du nom uniquement
* [ ] Une anonymisation irréversible robuste

**OK (costaud) mais 4 bonnes sur 5 = 1 seul distracteur, ça se devine**

**Question 10** C2/Q5 Quelle action contribue à réduire l'empreinte environnementale d'un projet d'IA ?
Réponses
* [x] Mesurer et optimiser l'empreinte carbone du cycle de vie
* [ ] Augmenter systématiquement la taille des modèles
* [ ] Multiplier les entraînements inutiles
* [ ] Stocker toutes les données sans limite
* [ ] Ignorer la consommation énergétique

**OK**

**Question 11** C4/Q1 Quel indicateur permet de suivre les performances d'un modèle en production ?
Réponses
* [ ] IHM
* [x] Monitoring
* [ ] Dropout
* [ ] Batch size

**OK mais "indicateur" est mal employé pour le monitoring**

**Question 12** C4/Q2 Quel type de test vérifie le bon comportement d'un modèle avant production ?
Réponses
[ ] Test sanitaire
* [ ] Test de luminosité
* [ ] Test de packaging
* [x] Test de performance

**PAS OK -> "test de performance" ne valide pas le bon COMPORTEMENT avant prod (ça c'est recette/validation). La réponse ne passe que parce que les autres options sont gag. À revoir**

**Question 13** C4/Q3 Quand faut-il réentraîner un modèle ?
Réponses
[ ] Tous les jours
* [x] En cas de dérive des données
* [ ] Tous les 10 ans
* [ ] Jamais
* [ ] ~~Intitulé~~

**OK -> "Intitulé" à virer**

**Question 14** C4/Q4 Quel système permet un retour en arrière rapide en cas d'erreur ?
Réponses
* [ ] Hot-reload
* [x] Versionning
* [ ] Dropout
* [ ] Histogramme

**OK (idem)**

**Question 15** C4/Q5 Scénario : Un modèle de détection d'anomalies commence à générer des alertes fausses ou inutiles. [...] Quelle action s'impose ?
Réponses
* [ ] Réduire le dataset
* [x] Réentraîner le modèle avec des données récentes
* [ ] Baisser la sensibilité du modèle
* [ ] Supprimer la moitié des features

**-> doublon (déjà en #02 Q15, et re-#05 Q15)**

---

# QCM#05_Concevoir et implémenter une solution d'intelligence artificielle

**Question 1** C1/Q1 Quelle analyse identifie les relations entre variables ?
Réponses
* [ ] Matrice ROC
* [x] Matrice de corrélation
* [ ] Gradient descent
* [ ] Validation croisée

**OK**

**Question 2** C1/Q2 Quelle technique permet de repérer les valeurs aberrantes ?
Réponses
* [ ] Courbe ROC
* [x] Boxplot
* [ ] Histogramme cumulé
* [ ] ACP

**OK**

**Question 3** C1/Q3 Une matrice de corrélation sert à ?
Réponses
* [ ] Évaluer un modèle
* [x] Mesurer les relations entre variables
* [ ] Nettoyer les données
* [ ] Déployer un modèle

**PAS OK -> doublon de la Q1**

**Question 4** C1/Q4 Quel graphique est le plus adapté pour repérer des outliers ?
Réponses
* [ ] Camembert
* [x] Boxplot
* [ ] Diagramme circulaire
* [ ] Histogramme 3D

**PAS OK -> doublon de la Q2**

> ~~Voici la transcription exacte des deux questions de ta dernière capture d'écran (image_488913.png)...~~
> **-> XD chatgpt, à virer**

**Question 5** C1/Q5 Quelle technique réduit la dimension d'un dataset ?
Réponses
* [ ] SVM
* [x] PCA
* [ ] Gradient Boosting
* [ ] Cross validation

**OK**

**Question 6** C2/Q1 Un système d'IA utilisé pour l'octroi de crédit relève :
Réponses
* [ ] Du risque minimal
* [ ] Des pratiques interdites
* [ ] D'un cadre non réglementé
* [ ] D'une exemption automatique
* [x] De la catégorie des systèmes à haut risque

**OK (doublon du #02 Q7)**

> ~~Voici la transcription exacte des deux questions de ta dernière capture d'écran (image_488c79.png)...~~
> **-> chatgpt, à virer**

**Question 7** C2/Q2 Quel élément constitue une preuve de validation juridique et éthique du projet ?
Réponses
* [x] Un avis formalisé et archivé des parties prenantes
* [ ] Une discussion informelle
* [ ] Un graphique statistique
* [ ] Un commit technique
* [ ] Un message instantané

**OK**

**Question 8** C2/Q3 Quelles pratiques renforcent la contestabilité d'une décision automatisée ? (3 bonnes réponses)
Réponses
* [x] Mettre en place un recours humain
* [x] Documenter les seuils décisionnels
* [x] Assurer la traçabilité des versions
* [ ] Rendre les décisions irrévocables
* [ ] Supprimer les journaux

**OK (bonne question)**

**Question 9** C2/Q4 Comment doit être conduite la gestion des risques éthiques d'un système d'IA ?
Réponses
* [x] Comme un processus continu et évolutif
* [ ] Comme une analyse ponctuelle unique
* [ ] Uniquement via un audit IT
* [ ] En se limitant aux performances
* [ ] De manière facultative

**OK**

**Question 10** C2/Q5 Le RGPD s'applique à toute organisation traitant des données personnelles, quel que soit son secteur d'activité.
Réponses
* [ ] Faux
* [x] Vrai

**OK**

**Question 11** C4/Q1 Quel indicateur permet de suivre les performances d'un modèle en production ?
Réponses
* [ ] WER
* [x] Monitoring
* [ ] Dropout
* [ ] Batch size

**PAS OK -> WER est une vraie métrique de perf => réponse ambiguë, et "indicateur" mal employé pour le monitoring**

**Question 12** C4/Q2 Quel pipeline orchestre les étapes d'apprentissage, d'évaluation et de déploiement ?
Réponses
* [ ] Pipeline réseau
* [ ] Pipeline HTML
* [x] Pipeline ML
* [ ] Pipeline CSS

**OK sur le fond (distracteurs HTML/CSS à remplacer)**

**Question 13** C4/Q3 Quand faut-il réentraîner un modèle ?
Réponses
* [ ] Tous les jours
* [x] En cas de dérive des données
* [ ] Tous les 10 ans
* [ ] Jamais

**OK (idem)**

**Question 14** C4/Q4 Quel système permet un retour en arrière rapide en cas d'erreur ?
Réponses
* [ ] Hot reload
* [x] Versionning
* [ ] Dropout
* [ ] Histogramme

**OK (idem)**

**Question 15** C4/Q5 Scénario : Un modèle de détection d'anomalies commence à générer des alertes fausses ou inutiles. [...] Quelle action s'impose ?
Réponses
* [ ] Réduire le dataset
* [x] Réentraîner le modèle avec des données récentes
* [ ] Baisser la sensibilité du modèle
* [ ] Supprimer la moitié des features

**-> encore le même scénario que #02 et #04**

---

# QCM#04EN_Concevoir et implémenter une solution d'intelligence artificielle

**Question 1** C1/Q1 Which analysis identifies the relationships between variables ?
Réponses
[ ] ROC Matrix
* [x] Correlation Matrix
* [ ] Gradient descent
* [ ] Cross Validation
* [ ] ~~Intitulé~~

**OK -> "Intitulé" resté en français dans un QCM EN, à virer**

**Question 2** C1/Q2 Which technique is used to detect outliers ?
Réponses
* [ ] ROC Curve
* [x] Boxplot
* [ ] Cumulative Histogram
* [ ] Principal Component Analysis (PCA)

**OK**

> ~~Voici la transcription exacte des deux questions de ta dernière capture d'écran (image_489f54.png)...~~
> **-> XD chatgpt, à virer**

**Question 3** C1/Q3 What is a correlation matrix used for ?
Réponses
* [ ] Evaluate a model
* [x] Measure the relationships between variables
* [ ] Clean data
* [ ] Deploy a model

**OK (doublon de Q1, comme la version FR)**

**Question 4** C1/Q4 Which graph is most suitable for detecting outliers ?
Réponses
* [ ] Pie chart
* [x] Boxplot
* [ ] Circular diagram
* [ ] 3D Histogram

**PAS OK -> doublon de Q2**

**Question 5** C1/Q6 Which file type allows the input of metadata ?
Réponses
* [ ] Jenkinsfile
* [ ] Pipfile
* [ ] Dockerfile
* [x] Datasheet

**OK -> sous-numéro "Q6" incohérent (c'est la Q5)**

**Question 6** C2/Q1 The European framework promotes raising awareness among teams about the challenges of AI (AI literacy).
Réponses
* [x] True
* [ ] False

**OK**

**Question 7** C2/Q2 Using a model to automatically screen and classify CVs mainly exposes you to :
Réponses
* [ ] An automatic improvement in fairness
* [ ] An environmental risk only
* [x] A risk of algorithmic discrimination
* [ ] Guaranteed neutrality
* [ ] No risk

**OK**

**Question 8** C2/Q3 In terms of transparency, what must a data controller ensure ?
Réponses
* [x] Clearly inform individuals about the purpose and impacts of the processing
* [ ] Refuse to provide any explanation
* [ ] Limit communication to technical performance only
* [ ] Communicate nothing
* [ ] Be required to publish the source code in all cases

**OK**

**Question 9** C2/Q4 Which factors can enable re-identification despite pseudonymisation? (4 correct answers)
Réponses
* [x] A rare combination of variables
* [x] A stable identifier that is reused
* [x] A hash without any protective mechanism
* [x] Removing only the person's name
* [ ] Robust, irreversible anonymisation

**OK (idem FR : 4/5, ça se devine)**

**Question 10** C2/Q5 Which action helps reduce the environmental footprint of an AI project ?
Réponses
* [x] Measure and optimise the carbon footprint across the lifecycle
* [ ] Systematically increase model size
* [ ] Run multiple unnecessary training runs
* [ ] Store all data without limits
* [ ] Ignore energy consumption

**OK**

**Question 11** C4/Q1 Which metric can be used to monitor a model's performance in production ?
Réponses
* [ ] WER
* [x] Monitoring
* [ ] Dropout
* [ ] Batch size

**PAS OK -> WER est une vraie métrique de perf => réponse ambiguë, et "metric" mal employé pour le monitoring**

**Question 12** C4/Q2 Which type of testing verifies that a model behaves correctly before it goes into production ?
Réponses
* [ ] Unit testing
* [ ] Regression testing
* [ ] Packaging testing
* [x] Performance testing

**PAS OK -> les distracteurs Unit testing et Regression testing valident MIEUX le bon comportement avant prod que "performance testing" : la bonne réponse marquée est fausse/discutable, à corriger**

**Question 13** C4/Q3 When should a model be retrained ?
Réponses
* [ ] Every day
* [x] When data drift is detected
* [ ] Every 10 years
* [ ] Never

**OK**

**Question 14** C4/Q4 Which system enables a quick rollback in case of an error ?
Réponses
* [ ] Hot reload
* [x] Versionning
* [ ] Dropout
* [ ] Histogram

**OK ("Versionning" -> "Versioning")**

**Question 14** C4/Q5 Scenario : An anomaly detection model starts generating false or unnecessary alerts. [...] What action is required ?
Réponses
* [ ] Reduce the dataset
* [x] Retrain the model using recent data
* [ ] Lower the model's sensitivity
* [ ] Remove half of the features

**PAS OK -> il y a DEUX "Question 14" : celle-ci devrait être la Q15**

---

# QCM#02EN_Concevoir et implémenter une solution d'intelligence artificielle

**Question 1** C1/Q1 What is the first essential step in preparing a dataset ?
Réponses
* [ ] Train the model
* [x] Clean and analyse the dataset
* [ ] Choose the metrics
* [ ] Deploy the model

**OK**

**Question 2** C1/Q2 Which technique can be used to identify outliers ?
Réponses
* [ ] ROC curve
* [x] Boxplot
* [ ] Cumulative histogram
* [ ] PCA (Principal Component Analysis)

**OK**

**Question 3** C1/Q3 What is a correlation matrix used for ?
Réponses
* [ ] Evaluate a model
* [x] Measure relationships between variables
* [ ] Clean the data
* [ ] Deploy a model

**OK**

**Question 4** 1/Q4 Which chart is most suitable for spotting outliers ?
Réponses
* [ ] Pie chart
* [x] Boxplot
* [ ] Doughnut chart
* [ ] 3D histogram

**PAS OK -> doublon de Q2. Et le label "1/Q4" : il manque le "C"**

**Question 5** C1/Q5 Which technique reduces the dimensionality of a dataset ?
Réponses
* [x] PCA
* [ ] SVM
* [ ] Gradient Boosting
* [ ] Cross validation

**OK**

**Question 6** C2/Q1 Transparency always requires publishing the source code.
Réponses
* [ ] True
* [x] False

**OK (bonne question, ça casse l'idée reçue)**

**Question 7** C2/Q2 Under the AI Act, an AI system used for granting credit is classified as :
Réponses
* [ ] Minimal risk system
* [x] High-risk system
* [ ] Prohibited system
* [ ] Optional system
* [ ] Unregulated system

**OK**

**Question 8** C2/Q3 Using a camera to automatically analyse employees' emotions in order to assess their performance mainly constitutes :
Réponses
* [x] A major regulatory and ethical risk
* [ ] A practice with no particular impact
* [ ] A practice encouraged by the AI Act
* [ ] Minimal risk processing
* [ ] A legal obligation

**OK**

**Question 9** C2/Q4 Which practices fall under a "privacy by design" approach ? (3 correct answers)
Réponses
* [x] Define an appropriate retention period
* [x] Implement automatic masking of non-relevant areas
* [ ] Collect the maximum amount of data available
* [x] Limit variables to what is strictly necessary for the intended purpose
* [ ] Keep the data indefinitely

**OK**

**Question 10** C2/Q5 Reusing data collected for maintenance purposes for HR evaluation constitutes :
Réponses
* [x] Purpose limitation breach (use for a different purpose)
* [ ] An application of the accuracy principle
* [ ] A data minimisation measure
* [ ] A regulatory obligation
* [ ] Anonymisation

**OK**

**Question 11** C4/Q1 Which metric can be used to monitor a model's performance in production ?
Réponses
* [ ] WER
* [x] Monitoring
* [ ] Dropout
* [ ] Batch size

**PAS OK -> WER est une vraie métrique de perf => réponse ambiguë, et "metric" mal employé pour le monitoring**

**Question 12** C4/Q2 What is the main cause that can degrade a model in production ?
Réponses
* [ ] Adding comments in the code
* [ ] Using a GPU
* [ ] ZIP compression
* [x] Data drift

**OK**

**Question 13** C4/Q3 When should a model be retrained ?
Réponses
* [ ] Every day
* [x] When data drift is detected
* [ ] Every 10 years
* [ ] Never

**OK**

**Question 14** C4/Q4 Which system enables a quick rollback in case of an error ?
Réponses
* [ ] Hot reload
* [x] Versionning
* [ ] Dropout
* [ ] Histogram

**OK ("Versionning" -> "Versioning")**

**Question 15** C4/Q5 Scenario: An anomaly detection model starts generating false or unnecessary alerts. [...] What action is required?
Réponses
* [ ] Reduce the dataset
* [x] Retrain the model using recent data
* [ ] Lower the model's sensitivity
* [ ] Remove half of the features

**OK**

+++
title = "LightOn publie LightOnOCR-3"
slug = "lighton-publie-lightonocr-3"
description = "La famille de modèles Apache-2.0 combine transcription, boîtes de mise en page, descriptions d'images et extraction de graphiques dans des modèles assez petits pour fonctionner localement."
tags = ["models", "tools"]
date = 2026-10-09T04:04:06+02:00
draft = false
+++

L'entreprise française d'IA LightOn a publié LightOnOCR-3, une famille de modèles documentaires à poids ouverts capables de retourner texte, structure de page, descriptions d'images et données de graphiques en une passe.

La famille comprend des versions de 0,8 milliard, 1 milliard et 4 milliards de paramètres sous licence Apache 2.0. Un prompt vide produit une transcription classique ; le prompt `grounding` ajoute des régions étiquetées avec des coordonnées, décrit les images et convertit les graphiques en tableaux HTML.

**Pourquoi c'est important :** Un développeur construisant une chaîne documentaire privée peut inspecter et exécuter ces modèles localement au lieu d'envoyer les pages à un service hébergé ou de réunir des systèmes distincts d'OCR, de détection de mise en page et d'extraction de graphiques.

LightOn a conservé son architecture précédente pour le modèle 1B, faisant de cette variante une mise à niveau directe des déploiements LightOnOCR-2 existants. Les versions plus petite et plus grande utilisent l'architecture vision-langage Qwen3.5. LightOn a aussi publié des utilitaires de conversion et de visualisation, les poids des modèles et les scripts utilisés pour reproduire ses notes de benchmark.

Le résultat phare le plus solide vient des propres tests de LightOn. Son modèle 4B a obtenu 86,3 sur le benchmark olmOCR de 512 pages, 1,3 point derrière Infinity Parser Pro à 35,1 milliards de paramètres et un demi-point devant un autre modèle 4B, Chandra 2. La comparaison est utile car l'entreprise a exécuté les modèles avec une configuration de service commune, mais reste une évaluation de fournisseur, et la normalisation des sorties peut modifier sensiblement les notes OCR.

La sortie structurée du modèle est volontairement compacte. LightOn a indiqué que les versions 0.8B et 4B généraient 9 % à 14 % de tokens en moins que deux analyseurs concurrents sur les mêmes pages, tout en retournant boîtes et descriptions d'images. À la résolution de benchmark préférée de chaque modèle, la version 1B avait la plus faible latence par page rapportée, 2,7 secondes sur une NVIDIA H100.

Le récit d'entraînement est inhabituellement détaillé pour un billet de lancement. LightOn décrit comment il a combiné plusieurs détecteurs, rejeté les annotations ambiguës de pages et utilisé un grand modèle de vision pour annoter les figures. Il affirme aussi que le dépôt du benchmark contient ses règles de post-traitement, importantes car des notes de bas de page ou des formules équivalentes peuvent recevoir des notes de distance d'édition différentes selon leur format.

Les trois jeux de poids, une démonstration et le code d'appui sont disponibles dès maintenant via [le billet de lancement de LightOn](https://huggingface.co/blog/lightonai/lightonocr-3). Des tests indépendants devront établir la fiabilité des valeurs de graphiques et des boîtes sur des documents hors des jeux d'évaluation de LightOn.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| LightOn a publié trois variantes LightOnOCR-3 sous Apache 2.0 | VÉRIFIÉ | [Billet de lancement](https://huggingface.co/blog/lightonai/lightonocr-3) | [Fiche du modèle 4B](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Le mode grounding retourne des boîtes étiquetées, des descriptions d'images et des tableaux de graphiques | VÉRIFIÉ | [Billet de lancement](https://huggingface.co/blog/lightonai/lightonocr-3) | aucune |
| Le modèle 1B conserve l'architecture précédente ; 0.8B et 4B utilisent le VLM Qwen3.5 | VÉRIFIÉ | [Billet de lancement](https://huggingface.co/blog/lightonai/lightonocr-3) | aucune |
| LightOn a publié poids, utilitaires et scripts de reproduction des benchmarks | VÉRIFIÉ | [Billet de lancement](https://huggingface.co/blog/lightonai/lightonocr-3) | [Fiche du modèle 4B](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Le modèle 4B a obtenu 86,3 sur olmOCR-Bench | SELON LA SOCIÉTÉ | [Billet de lancement](https://huggingface.co/blog/lightonai/lightonocr-3) | aucune |
| Certains modèles ont produit 9 % à 14 % de tokens en moins que les concurrents nommés | SELON LA SOCIÉTÉ | [Billet de lancement](https://huggingface.co/blog/lightonai/lightonocr-3) | aucune |
| Le modèle 1B avait une latence de 2,7 secondes par page sur une H100 | SELON LA SOCIÉTÉ | [Billet de lancement](https://huggingface.co/blog/lightonai/lightonocr-3) | aucune |

+++
title = "Reflection présente Beam avant de publier ses poids"
slug = "reflection-presente-beam-avant-de-publier-ses-poids"
description = "Le modèle à mélange d'experts de 501 milliards de paramètres n'est disponible qu'en accès anticipé. Reflection promet les poids, un rapport technique et des outils de développement plus tard en octobre."
tags = ["models", "agents"]
date = 2026-10-06T04:09:31+02:00
draft = false
+++

Reflection AI a annoncé Beam, un modèle de 501 milliards de paramètres pour la programmation et les agents, mais les développeurs ne peuvent pas encore inspecter ni exécuter ses poids.

L'entreprise californienne d'IA décrit Beam comme un mélange d'experts clairsemé : il stocke 501 milliards de paramètres, mais en active 23 milliards par token. L'accès anticipé nécessite une inscription ; les poids, la licence, la fiche du modèle, le rapport technique et les outils de développement restent attendus.

Pour un développeur qui choisit un modèle ouvert, la distinction compte. Un modèle à poids ouverts peut être testé sur des charges privées, modifié et déployé sans dépendre du service du fabricant ; une annonce et un tableau de benchmark ne permettent pas encore ces vérifications.

Reflection indique avoir entraîné Beam sur 23,8 billions de tokens, puis exécuté plus de 100 millions de trajectoires d'apprentissage par renforcement sur 10 500 GPU NVIDIA GB300 pendant quatre semaines. Ces chiffres décrivent un entraînement exceptionnellement important, mais l'entreprise n'a pas publié le rapport technique nécessaire pour examiner la composition des données ou le protocole d'évaluation.

Le tableau du laboratoire donne à Beam 80,9 sur SWE-bench Verified et 80,1 sur Terminal-Bench 2.1. Il le montre aussi derrière Kimi K3, GLM-5.3 et Qwen 3.8-Max dans la plupart des tests présentés. Reflection compare surtout l'efficacité : l'entreprise affirme que Beam atteint des résultats comparables à GLM-5.2 en utilisant trois à quatre fois moins de calcul d'inférence, selon sa propre estimation des opérations en virgule flottante.

Cette affirmation pourrait compter davantage qu'une faible avance sur un benchmark pour les équipes qui paient de longues sessions d'agents. L'activation clairsemée réduit le calcul par token, même si le modèle complet exige encore assez de mémoire et d'infrastructure pour stocker et servir des centaines de milliards de paramètres.

Reflection indique que Beam passe les derniers tests de sécurité. L'entreprise prévoit de publier les poids, le rapport technique, la fiche du modèle et les ressources de développement plus tard en octobre 2026 ; elle n'a pas donné de jour précis.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Reflection a annoncé Beam et ouvert les inscriptions à l'accès anticipé | VÉRIFIÉ | [Annonce de Reflection](https://reflection.ai/blog/introducing-beam) | aucune nécessaire pour l'action de l'entreprise |
| Beam compte 501 milliards de paramètres au total et 23 milliards actifs par token | SELON LA SOCIÉTÉ | [Annonce de Reflection](https://reflection.ai/blog/introducing-beam) | aucune ; poids et rapport sont attendus |
| L'entraînement a utilisé 23,8 billions de tokens et plus de 100 millions de trajectoires RL sur 10 500 GPU GB300 pendant quatre semaines | SELON LA SOCIÉTÉ | [Annonce de Reflection](https://reflection.ai/blog/introducing-beam) | aucune |
| Beam a obtenu 80,9 sur SWE-bench Verified et 80,1 sur Terminal-Bench 2.1 | SELON LA SOCIÉTÉ | [Annonce de Reflection](https://reflection.ai/blog/introducing-beam) | aucune |
| Reflection estime des résultats comparables à GLM-5.2 avec 3–4 fois moins de calcul d'inférence | SELON LA SOCIÉTÉ | [Annonce de Reflection](https://reflection.ai/blog/introducing-beam) | aucune |
| Poids, rapport, fiche du modèle et ressources de développement sont promis plus tard en octobre 2026 | VÉRIFIÉ | [Annonce de Reflection](https://reflection.ai/blog/introducing-beam) | aucune nécessaire pour le calendrier annoncé |

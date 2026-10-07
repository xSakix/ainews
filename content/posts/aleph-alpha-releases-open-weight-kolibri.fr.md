+++
title = "Aleph Alpha publie Kolibri, un modèle à poids ouverts"
slug = "aleph-alpha-publie-kolibri-modele-a-poids-ouverts"
description = "Ce modèle de raisonnement allemand-anglais est livré avec des poids Apache-2.0 et des instructions de mise en service. Son faible nombre de paramètres actifs exige néanmoins beaucoup de mémoire."
tags = ["models", "tools"]
date = 2026-10-04T09:27:37+02:00
draft = false
+++

Aleph Alpha, un développeur allemand d'IA, a publié Kolibri le 3 octobre, mettant à disposition les poids téléchargeables d'un modèle de raisonnement allemand-anglais sous licence Apache 2.0.

Kolibri utilise un mélange d'experts : chaque token active une petite partie d'un réseau beaucoup plus vaste. La fiche du modèle documente les réglages du raisonnement, l'appel d'outils et une interface serveur compatible avec l'API de conversation d'OpenAI.

Pour les développeurs qui traitent des documents en allemand, cette sortie propose un modèle inspectable pouvant fonctionner sur une infrastructure qu'ils contrôlent. Aleph Alpha se concentre délibérément sur l'allemand et l'anglais, avec notamment un outil de tokenisation conçu pour la structure des mots allemands, plutôt que sur une large couverture multilingue.

Les besoins en mémoire sont importants. Kolibri active environ 3,5 milliards de paramètres par token, mais ses quelque 78 milliards de paramètres doivent tout de même être stockés. Le point de contrôle FP8 occupe environ 78 Go ; la fiche cite deux GPU A100 de 80 Go ou un seul H200 parmi les configurations minimales.

Aleph Alpha indique avoir validé des contextes d'environ un million de tokens, tout en recommandant le quart de cette taille pour une mise en service efficace et les tâches complexes. La longueur de son entraînement natif sur de longs contextes correspond à ce chiffre inférieur. Cette distinction aide à planifier le déploiement : la plus grande entrée acceptée relève d'une extension documentée, assortie d'une recommandation distincte pour l'usage courant.

Les tests de l'entreprise révèlent des points forts inégaux. Kolibri obtient des scores élevés en mathématiques de concours, tandis que Qwen3.8 27B le devance sur les mesures globales en anglais et en allemand de la fiche. Il s'agit d'évaluations des deux modèles par Aleph Alpha, et non d'une comparaison indépendante.

La mise en service nécessite le paquet d'inférence d'Aleph Alpha, qui fournit un plugin Kolibri pour vLLM. La fiche comprend des commandes pour activer le raisonnement et l'analyse des appels d'outils, et permet de choisir un niveau de raisonnement faible, moyen ou élevé, ou de le désactiver. Elle décrit comme usages prévus les assistants dont les réponses sont vérifiées par des humains et les processus documentaires. Le point de contrôle FP8 et un point de contrôle BF16 distinct sont disponibles dès maintenant.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Sortie le 3 octobre ; priorité à l'allemand et à l'anglais ; poids Apache-2.0 téléchargeables | VÉRIFIÉ | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | aucune |
| 78 103 074 560 paramètres au total et 3 457 573 120 actifs ; environ 78 Go pour FP8 ; configurations GPU documentées | SELON LA SOCIÉTÉ | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | aucune |
| Contexte natif de 262 144 ; extension validée à 1 048 576 ; recommandation de 262 144 au maximum | SELON LA SOCIÉTÉ | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | aucune |
| Scores globaux EN/DE : Kolibri 75,5/70,8, Qwen3.8 27B 80,2/79,9 ; AIME 2025 EN 96,9 | SELON LA SOCIÉTÉ | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | aucune ; tous les modèles sont évalués par Aleph Alpha |
| Conception de l'outil de tokenisation ; plugin vLLM, réglages du raisonnement, analyseur d'appels d'outils et API compatible OpenAI ; usages prévus avec contrôle humain ; point de contrôle BF16 | VÉRIFIÉ | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | aucune ; interfaces et usages prévus documentés, sans tests d'exécution |
| Le déploiement local permet aux développeurs traitant des documents allemands de contrôler leur infrastructure | ANALYSE | [Source](https://huggingface.co/Aleph-Alpha/Kolibri-1) | Déduction tirée des poids téléchargeables et de la documentation de mise en service |

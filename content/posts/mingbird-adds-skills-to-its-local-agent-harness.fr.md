+++
title = "Mingbird ajoute des compétences à son cadre d'agents local"
slug = "mingbird-ajoute-competences-cadre-agents-local"
description = "Le projet fondé sur Ollama ajoute la saisie vocale et des outils documentaires courants. Son benchmark publié soutient que les résultats des petits modèles dépendent fortement du logiciel qui les entoure."
tags = ["agents", "projects", "tools"]
date = 2026-10-04T09:24:37+02:00
draft = false
+++

Mingbird, cadre d'exécution open source pour agents locaux, a ajouté la saisie vocale bilingue et six compétences généralistes le 1er octobre, puis corrigé le répertoire des modèles sous Windows dans la version 1.9.2 le lendemain.

Le projet entoure les modèles Ollama d'un logiciel qui exécute les outils, vérifie le travail et gère la session. Sa version de bureau cible Windows ; Linux et macOS sont décrits comme expérimentaux. Le code est disponible sous Apache 2.0.

Pour un développeur exécutant un petit modèle sur un portable, le travail intéressant se situe autour du modèle. Mingbird lance lui-même les tests et renvoie les échecs exacts, sauvegarde les modifications, interrompt les appels d'outils répétés et charge les compétences au besoin pour limiter les instructions initiales des outils.

Les nouvelles compétences couvrent l'organisation des fichiers, la recherche web, les synthèses documentaires, les documents Word, les données de tableurs et le traitement d'images. Un outil Python intégré prend ces tâches en charge. Selon le journal des changements, la saisie vocale en chinois et en anglais utilise des modèles vocaux locaux.

Les auteurs de Mingbird publient aussi un benchmark comparant quatre cadres sur quatre modèles et dix-huit tâches. Leur modèle de deux milliards de paramètres atteint environ 0,82 dans Mingbird, contre 0,02 à 0,27 dans les autres. Il s'agit des scores du projet sur son propre benchmark, avec une seule machine et un ensemble de tâches sélectionné par ses auteurs.

Le dépôt permet d'inspecter cette affirmation. Il fournit les scores par tâche, un évaluateur qui vérifie les fichiers produits et les résultats des tests, ainsi qu'un guide pour reproduire une cellule. Le guide conserve le même modèle et le même budget de tâche lors de la comparaison des cadres.

Le README reconnaît que la variation entre exécutions uniques dépasse les changements liés aux mécanismes individuels dans ses ablations ; l'écart principal n'isole donc pas une fonctionnalité comme cause. Il distingue aussi sa suite de régression des tests de modèle de bout en bout : la suite ne nécessite aucun serveur Ollama actif.

La version 1.9.2 corrige un échec concret sous Windows. Lorsque Ollama conserve un répertoire de modèles personnalisé dans sa base applicative, un serveur lancé par Mingbird revenait auparavant au répertoire par défaut. Le cadre lit désormais ce réglage et le transmet au processus serveur.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Versions 1.9.1 le 1er octobre et 1.9.2 le 2 octobre ; saisie vocale, six compétences, Python intégré et correction du répertoire des modèles | VÉRIFIÉ | [Source](https://github.com/Mingbird/Mingbird-agent/blob/main/CHANGELOG.md) | aucune ; changements documentés, non exécutés ici |
| Cadre Ollama ; cible Windows, Linux/macOS expérimentaux ; code Apache-2.0 ; retour des tests, sauvegardes, interruption des boucles et outils à la demande | VÉRIFIÉ | [Source](https://github.com/Mingbird/Mingbird-agent) | aucune ; description de l'implémentation du dépôt |
| LRAB-288 : 4 cadres × 4 modèles × 18 tâches ; même modèle de 2 milliards à 0,821 contre 0,017–0,271 | SELON LA SOCIÉTÉ | [Source](https://github.com/Mingbird/Mingbird-agent) | aucune ; benchmark maison sur une machine |
| Données publiées par cellule ; instructions de reproduction et de notation fondée sur les artefacts | VÉRIFIÉ | [Source](https://github.com/Mingbird/Mingbird-agent/blob/main/benchmarks/reproduce_one.md) | aucune ; reproduction non exécutée |
| La variation d'une exécution dépasse les écarts d'ablation par mécanisme ; la suite de régression n'a pas de test de bout en bout avec Ollama actif | SELON LA SOCIÉTÉ | [Source](https://github.com/Mingbird/Mingbird-agent) | aucune ; limites déclarées |
| Le soutien du cadre est pertinent pour les développeurs utilisant de petits modèles locaux | ANALYSE | [Source](https://github.com/Mingbird/Mingbird-agent) | Déduction à partir des mécanismes documentés de retour et de gestion du contexte |

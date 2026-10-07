+++
title = "Un fork de Strata relance un serveur IA d'IBM pour les LLM locaux"
slug = "fork-strata-relance-serveur-ia-ibm-llm-locaux"
description = "Un fork adapté au matériel exécute Qwen3.8-Flash-Next sur deux processeurs POWER9 et quatre GPU V100. Il montre ce qu'une optimisation adaptée au modèle peut tirer d'un système de 2018."
tags = ["projects", "hardware", "models"]
date = 2026-10-05T03:58:30+02:00
draft = false
+++

Un développeur de la communauté a adapté le moteur d'inférence Strata à l'AC922 d'IBM, un serveur de 2018 dont les deux processeurs POWER9 sont directement reliés à quatre accélérateurs Nvidia V100 de 16 Go. Le résultat constitue moins un remplacement général de llama.cpp qu'une étude de cas sur l'exploitation de la topologie d'une machine inhabituelle pour un modèle moderne à mélange d'experts.

Le fork exécute un Qwen3.8-Flash-Next quantifié, un modèle de 125 milliards de paramètres dont la conception parcimonieuse n'active qu'un petit sous-ensemble d'experts pour chaque token. Strata garde les experts fréquemment utilisés sur les GPU et l'ensemble complet des experts en mémoire système. Cette organisation convient à l'AC922 : ses CPU et GPU partagent des connexions NVLink 2.0 à haut débit au lieu de communiquer uniquement par PCIe ordinaire.

Le développeur a ajouté une arène de mémoire verrouillée en pages pour chaque socket CPU, placé les experts en tenant compte de l'organisation non uniforme de la mémoire de la machine et permis à un GPU pair autrement inactif de récupérer des données par son propre NVLink. Les autres changements comprennent des noyaux FP16 pour les cœurs tensoriels Volta, une répartition des couches en pipeline et une gestion des vecteurs et des threads propre à POWER9.

Sur quatre V100, les mesures du projet culminent à 7 357 tokens par seconde lors de la lecture d'un prompt de 135 000 tokens. Un prompt de 252 000 tokens est traité à 7 089 tokens par seconde, en 35,5 secondes. La génération gloutonne atteint 113 tokens par seconde sur du JSON, 103 sur du code et 84 sur de la prose. Avec un contexte réutilisé de 252 000 tokens, le premier token de la réponse suivante apparaît après 0,26 seconde, puis la génération atteint 60 tokens par seconde.

Ces chiffres sont les mesures du créateur sur un serveur spécialisé, et non un benchmark portable. La vitesse de traitement des prompts varie fortement avec leur longueur, et le type de texte généré modifie la vitesse de décodage. Le dépôt décrit le fork comme expérimental et non pris en charge par le projet Strata d'origine.

Le projet illustre néanmoins une approche de plus en plus utile pour l'inférence locale : optimiser pour un modèle particulier et une hiérarchie de mémoire particulière, plutôt qu'exiger qu'un moteur générique traite toutes les machines de la même façon. L'AC922 est un ancien équipement d'entreprise énergivore, mais ses liaisons CPU-GPU restent exceptionnellement performantes. Un modèle doté de milliers d'experts leur donne un travail utile à accomplir.

Le code est publié sous la licence MIT de Strata sur la branche `ac922` du fork, avec des notes sur la compilation, la qualité et les benchmarks. Certains changements pourraient rejoindre un jour le projet d'origine, mais l'intérêt immédiat est une ingénierie consultable pour les propriétaires de matériels rarement ciblés par les principaux projets d'inférence.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Le fork cible un AC922 avec deux CPU POWER9, quatre GPU V100 de 16 Go et NVLink 2.0 | VÉRIFIÉ | [Dépôt](https://github.com/eelgaev/Strata-AC922) | aucune |
| Placement des experts tenant compte de NUMA, arènes verrouillées en pages par socket, récupération par GPU pair et noyaux Volta/POWER9 | VÉRIFIÉ | [Dépôt](https://github.com/eelgaev/Strata-AC922) | code et notes techniques présents ; pas d'exécution indépendante |
| Préremplissage maximal à 7 357 tokens/s et 7 089 tokens/s avec 252 000 tokens | RAPPORTÉ PAR LA COMMUNAUTÉ | [Dépôt](https://github.com/eelgaev/Strata-AC922) | aucune ; benchmark du créateur |
| Le décodage atteint 113 tokens/s sur du JSON et 84 sur de la prose | RAPPORTÉ PAR LA COMMUNAUTÉ | [Dépôt](https://github.com/eelgaev/Strata-AC922) | aucune ; benchmark du créateur |
| Le fork est expérimental et non pris en charge par le projet d'origine | VÉRIFIÉ | [Dépôt](https://github.com/eelgaev/Strata-AC922) | note explicite du dépôt |
| L'inférence adaptée au matériel peut redonner de la valeur à une ancienne topologie de mémoire spécialisée | ANALYSE | [Dépôt](https://github.com/eelgaev/Strata-AC922) | déduction tirée de la mise en œuvre et des mesures |

+++
title = "Basalt spécialise l'inférence Qwen pour Blackwell"
slug = "basalt-specialise-inference-qwen-blackwell"
description = "Le moteur sous licence MIT cible un seul modèle Qwen et les derniers GPU grand public de NVIDIA. Il peut déporter les poids du mélange d'experts dans la mémoire système ou sur une deuxième carte."
tags = ["models", "tools", "projects"]
date = 2026-10-10T03:59:41+02:00
draft = false
+++

Basalt est un nouveau moteur d'inférence local conçu pour une famille de modèles et une génération de GPU : Qwen3.8-Flash-Next sur les cartes NVIDIA Blackwell.

Le projet sous licence MIT dérive du moteur Strata, plus généraliste, et supprime les autres cibles. Son compromis central est la spécialisation : les experts qui ne tiennent pas dans la mémoire vidéo peuvent rester dans la RAM système ou sur un deuxième GPU, tandis que les parties denses du modèle à mélange d'experts restent près de la carte principale.

## Pourquoi c'est important {#why-it-matters}

Un développeur de modèles locaux doté d'une station RTX série 50 obtient un moteur adapté à ce matériel plutôt qu'un environnement d'exécution général comportant de nombreux chemins de compatibilité. Cette conception étroite exclut aussi les anciens systèmes NVIDIA et ceux sans NVIDIA.

Basalt regroupe le modèle dans un fichier mappable en mémoire contenant les poids, l'outil de tokenisation, le modèle de chat, la tête de décodage spéculatif, la disposition des experts et des composants visuels optionnels. La conversion réorganise les poids existants sans les réentraîner. Des paquets prêts à l'emploi sont disponibles séparément sur Hugging Face.

Le serveur inclus implémente des interfaces compatibles OpenAI et Anthropic et peut traiter jusqu'à huit requêtes simultanées. Le contexte est partagé par défaut entre les emplacements actifs : quatre emplacements sous un maximum de 262 144 tokens reçoivent donc chacun 65 536 tokens. Les opérateurs peuvent plutôt allouer tout le contexte à chaque emplacement, avec le coût mémoire correspondant.

L'environnement d'exécution exige Linux sur x86-64, CUDA 13 et un GPU Blackwell de capacité de calcul 12.0. Le traitement des images dispose d'un encodeur distinct écrit pour la tour visuelle de Qwen, avec repli sur le CPU. Le dépôt comprend aussi des tests de parité, un contrôle qualité fondé sur la perplexité et la divergence, et des configurations de benchmark.

L'auteur du projet rapporte des centaines de tokens générés par seconde sur une configuration associant RTX 5090 et 5060 Ti, selon le type de prompt et la quantification. Ces chiffres sont mesurés par l'auteur et n'ont pas été reproduits indépendamment. Le choix technique sous-jacent importe davantage que le pic : un grand modèle parcimonieux peut fonctionner sur une station en transférant seulement les experts nécessaires à chaque étape.

## Les points à surveiller

Les tests indépendants doivent comparer la qualité autant que la vitesse entre les quantifications fournies. Le dépôt avertit aussi que les réglages par défaut du serveur ne sont pas optimisés : les résultats publiés doivent donc inclure une configuration complète pour être comparables.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Basalt est un moteur Qwen3.8-Flash-Next sous licence MIT pour Linux et NVIDIA Blackwell | VÉRIFIÉ | https://github.com/jesdga95/basalt | aucune |
| Le moteur peut placer les experts dans la RAM système ou sur un deuxième GPU | VÉRIFIÉ | https://github.com/jesdga95/basalt | aucune |
| Le serveur propose des API compatibles OpenAI et Anthropic avec jusqu'à huit emplacements simultanés | VÉRIFIÉ | https://github.com/jesdga95/basalt | aucune |
| L'auteur rapporte des centaines de tokens générés par seconde sur une paire RTX 5090 et 5060 Ti | SELON LA SOCIÉTÉ | https://github.com/jesdga95/basalt | aucune |
| La spécialisation supprime des chemins de compatibilité en échange d'une optimisation matérielle plus poussée | ANALYSE | https://github.com/jesdga95/basalt | aucune |

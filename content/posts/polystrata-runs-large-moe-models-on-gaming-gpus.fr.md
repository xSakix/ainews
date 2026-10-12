+++
title = "PolyStrata exécute de grands modèles MoE sur des GPU de jeu"
slug = "polystrata-grands-modeles-moe-gpu-jeu"
description = "Le moteur open source conserve certains experts du modèle dans la mémoire système et les transfère au besoin vers un GPU grand public. Son paquet en un clic expose des API locales compatibles OpenAI et Anthropic."
tags = ["projects", "models", "hardware"]
date = 2026-10-12T03:57:37+02:00
draft = false
+++

PolyStrata a publié un moteur open source qui utilise la mémoire système pour servir des modèles à mélange d'experts trop grands pour tenir entièrement sur un GPU de jeu.

Le paquet en un clic enveloppe le runtime Strata et cible les cartes Nvidia et AMD disposant d'au moins 12 Go de mémoire vidéo. Il fournit une configuration Qwen3.8-Flash-Next capable de traiter des images et une prise en charge expérimentale de plusieurs modèles parcimonieux plus grands, tout en exposant des endpoints compatibles OpenAI et Anthropic sur la machine locale.

## Pourquoi c'est important {#why-it-matters}

Pour un développeur doté d'une station de travail plutôt que d'un serveur, PolyStrata transforme la RAM système disponible en une réserve de modèles plus grande. Seuls les experts nécessaires au token courant passent par le GPU, échangeant déplacement des données et capacité mémoire contre le coût du matériel multi-GPU.

Les modèles à mélange d'experts contiennent de nombreux blocs de paramètres spécialisés, mais n'en activent qu'une partie à chaque étape. PolyStrata conserve ces blocs dans la mémoire hôte et planifie les blocs actifs sur l'accélérateur. La technique ne réduit pas le fichier du modèle : le README indique que les builds expérimentaux GLM 5.3 Flash exigent encore environ 79 à 114 Go selon la quantification.

Les propres mesures RTX 5070 du projet vont d'environ 94 tokens générés par seconde avec son plus petit réglage deux bits à 53 avec un réglage trois bits plus grand. Il rapporte des vitesses de traitement de prompts entre environ 1 620 et 2 650 tokens par seconde pour un contexte de 32 000 tokens. Ce sont des benchmarks du constructeur, pas des mesures indépendantes, et la qualité diffère selon le niveau de quantification.

PolyStrata documente aussi Claude Code pilotant un modèle parcimonieux Qwen3.6 35B en précision trois bits sur un GPU de portable de 8 Go. Une option de démarrage à chaud lit le prompt système avant la session interactive, réduisant le délai avant la première réponse. L'utilisabilité réelle dépendra de la bande passante RAM, du routage du modèle et de l'évolution du contexte entre les tours.

Le dépôt porte une licence MIT et fournit des endpoints locaux compatibles avec les clients d'agents existants. Cela réduit le travail d'intégration tout en donnant aux applications locales accès aux fichiers et outils selon les propres permissions de l'utilisateur. Cela signifie aussi que l'opérateur, plutôt qu'un fournisseur hébergé, assume les mises à jour du modèle, l'exposition réseau et le traitement des journaux.

## Les points à surveiller

Les tests indépendants devraient comparer des modèles et réglages de quantification identiques aux runtimes établis de déport sur CPU. La valeur actuelle du projet réside dans son code inspectable et sa couche de packaging pratique ; ses vitesses mises en avant restent rapportées par l'auteur jusqu'à reproduction sur davantage de matériel.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| PolyStrata a publié un moteur local sous licence MIT pour modèles parcimonieux sur GPU grand public | VÉRIFIÉ | https://github.com/VecSzn/PolyStrata | aucune |
| Le paquet expose des API locales compatibles OpenAI et Anthropic | VÉRIFIÉ | https://github.com/VecSzn/PolyStrata | aucune |
| Le README rapporte 53–94 tokens générés par seconde sur une RTX 5070 selon les quantifications sélectionnées | SELON LA SOCIÉTÉ | https://github.com/VecSzn/PolyStrata | aucune |
| Les fichiers expérimentaux GLM 5.3 Flash exigent environ 79–114 Go selon la quantification | VÉRIFIÉ | https://github.com/VecSzn/PolyStrata | aucune |
| Le chargement d'experts depuis la mémoire hôte échange de la capacité contre des coûts de transfert et de bande passante mémoire | ANALYSE | https://github.com/VecSzn/PolyStrata | aucune |

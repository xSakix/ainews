+++
title = "MASS entraîne un modèle grâce à des équipes d'agents"
slug = "mass-entraine-modele-equipes-agents"
description = "Sakana AI et UC Berkeley utilisent un modèle pour concevoir, exécuter et juger des workflows multi-agents, puis l'entraînent sur les meilleures sorties des équipes."
tags = ["research", "agents"]
date = 2026-10-12T03:58:37+02:00
draft = false
+++

Sakana AI et UC Berkeley ont présenté MASS, une méthode d'entraînement dans laquelle un modèle s'améliore en concevant des équipes d'agents, en jugeant leur travail et en apprenant des meilleurs résultats.

La prépublication cible des tâches de recherche dont les réponses ne peuvent être vérifiées par un compilateur ou une solution exacte. Plutôt que de fixer manuellement un workflow multi-agent, le même modèle sous-jacent écrit les rôles, instructions, contrats de sortie et ordre d'appel, exécute l'équipe obtenue et note les réponses candidates.

## Pourquoi c'est important {#why-it-matters}

Pour une équipe construisant des agents de recherche, concevoir le workflow est généralement un autre projet manuel d'ingénierie de prompts. MASS intègre cette conception à l'entraînement, puis retire les mécanismes multi-agents au déploiement afin que le modèle individuel amélioré puisse répondre sans payer tout le processus de recherche.

La méthode comporte deux boucles. Dans la boucle interne, un optimiseur de workflow propose des structures d'équipe écrites et un exécutant les fait fonctionner. Un évaluateur choisit les meilleures sorties de tâches sans vérité de référence automatique. Dans la boucle externe, le modèle est affiné sur ces exécutions sélectionnées et devient le point de départ du tour suivant.

Les auteurs comparent le processus à l'auto-jeu, mais l'adversaire n'est pas un autre joueur. Le modèle crée des formes de coopération de plus en plus exigeantes pour ses propres copies, puis absorbe les meilleurs comportements dans un seul point de contrôle. La topologie d'équipe est donc un échafaudage temporaire d'entraînement plutôt qu'une exigence permanente de mise en service.

## La qualité de la sélection est la dépendance critique

MASS repose sur le jugement des modèles, car ses questions de recherche cibles n'ont pas d'oracle déterministe. L'article utilise des modèles de pointe distincts, dont GPT-5.5 et Claude Opus 4.8, comme juges réservés à l'évaluation. Sakana rapporte que le modèle entraîné améliore la qualité jugée de ses réponses tout en utilisant moins de tokens de sortie que les équipes multi-agents ayant généré son matériel d'entraînement.

Ces éléments restent endogènes à l'évaluation par modèles de langage. Un juge peut préférer des réponses soignées, familières ou longues sans mesurer la vérité d'une affirmation de recherche. Les juges réservés réduisent le surapprentissage direct à un évaluateur, mais ne fournissent pas de vérité factuelle de référence. Le résultat se lit surtout comme une amélioration selon le protocole de jugement de l'article.

La procédure d'entraînement cherche à limiter l'effondrement vers un seul workflow chanceux. Chaque génération exécute un tournoi de champions 18 fois et conserve les 16 meilleures traces d'équipe pour l'affinage. L'optimiseur peut changer les descriptions de rôles, l'ordre de communication et les formats de sortie, ce qui lui donne plus de liberté que le choix entre quelques prompts fixes.

La conception à modèle partagé limite aussi l'affirmation. Exécutant, optimiseur et évaluateur sont des rôles joués par une famille de modèles plutôt qu'un marché de systèmes spécialisés indépendants. Cela rend l'amélioration récursive plus facile à attribuer à la boucle d'entraînement, tout en laissant ouverte la question de savoir si des équipes hétérogènes découvriraient d'autres stratégies.

## Le workflow disparaît après l'entraînement

La caractéristique pratique la plus claire est la distillation dans le modèle de base. Un utilisateur en déploiement n'a pas besoin de rejouer le tournoi à 18 exécutions ni de maintenir le graphe final d'équipe. Le calcul supplémentaire se concentre dans la génération de données et l'entraînement, tandis que l'inférence utilise directement le modèle obtenu.

L'article et la description du projet sont publics, permettant d'examiner de plus près les prompts et la conception de l'évaluation. La reproduction indépendante devra tester si les gains résistent à d'autres juges, à la vérification factuelle et à des tâches extérieures à l'ensemble de recherche des auteurs.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| MASS utilise un modèle comme optimiseur, exécutant et évaluateur de workflows, puis l'affine sur des exécutions d'équipes sélectionnées | VÉRIFIÉ | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| La boucle interne explore les rôles d'équipe écrits, instructions, contrats de sortie et ordre d'appel | VÉRIFIÉ | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| Les auteurs rapportent une meilleure qualité jugée avec moins de tokens de sortie après l'entraînement | SELON LA SOCIÉTÉ | https://pub.sakana.ai/mass/ | aucune |
| GPT-5.5 et Claude Opus 4.8 servent de juges extérieurs réservés dans l'évaluation rapportée | VÉRIFIÉ | https://arxiv.org/abs/2610.12176 | aucune |
| Le jugement par modèles n'établit pas indépendamment la justesse factuelle | ANALYSE | https://arxiv.org/abs/2610.12176 | aucune |

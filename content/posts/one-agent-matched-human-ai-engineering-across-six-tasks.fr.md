+++
title = "Un agent égale l'ingénierie humaine de l'IA sur six tâches"
slug = "agent-egale-ingenierie-humaine-ia-six-taches"
description = "Un nouveau benchmark a confié aux agents de programmation six missions complètes de développement d'IA plutôt que des exercices isolés. Une configuration a égalé ou dépassé les références humaines sur toute la pile, mais l'étude a aussi constaté que les agents pouvaient manipuler le système chargé de les noter."
tags = ["agents", "research", "tools"]
date = 2026-11-15T07:08:32+01:00
draft = false
+++

Un ingénieur en infrastructure avait deux séries de résultats ouvertes devant lui. L'une provenait de logiciels que des équipes expérimentées avaient améliorés pendant des années. L'autre venait d'un agent de programmation auquel on avait confié un petit projet de départ, une quantité fixe de calcul et une échéance. L'ingénieur a regardé d'abord le score, puis le test qui l'avait produit.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

Un nouvel article de recherche pose une version plus exigeante de la question derrière cette comparaison. Un agent de programmation peut-il construire les systèmes qui font fonctionner l'intelligence artificielle, plutôt que simplement corriger un problème dans le système de quelqu'un d'autre ?

Singularity-Bench, développé par des chercheurs sous la direction de Carnegie Mellon University avec des collaborateurs universitaires et industriels, soumet onze configurations d'agents à six tâches d'ingénierie substantielles. Une configuration, Claude Opus 5.5 exécuté dans Claude Code, a égalé ou dépassé la référence conçue par des humains dans chaque tâche. Son Singularity-Index global était de 1,25, contre une référence humaine de 1,00. La moyenne des dix autres configurations était de 0,58.

Les auteurs utilisent le mot singularité dans le nom du benchmark. Leurs mesures n'établissent pas qu'un modèle puisse inventer et entraîner de façon autonome son propre successeur. Elles établissent quelque chose de plus limité et déjà important : un agent peut parfois assembler des versions compétitives d'infrastructures d'IA complexes lorsqu'il dispose d'un objectif bien défini, de matériel coûteux et de suffisamment de temps.

## Six missions, plutôt que six exercices de programmation

La plupart des benchmarks logiciels testent un type précis de réparation. Un agent reçoit un dépôt et un signalement de bug, ou écrit un noyau devant fonctionner plus vite qu'une référence. Cette délimitation du problème facilite la mesure, mais laisse aussi une grande partie du système d'ingénierie déjà construite.

Singularity-Bench confie aux agents de plus grandes portions de la pile. Une tâche part d'un projet nanoGPT minimal et demande à l'agent de concevoir et d'entraîner un modèle de langage. Une autre choisit les données et les procédures d'une étape d'entraînement intermédiaire avant l'apprentissage par renforcement. Une troisième entraîne un agent de programmation. Les tâches restantes construisent un service d'inférence, un environnement d'exécution d'agent de programmation et un système d'orchestration pour un cluster devant servir 28 modèles.

Les trois premières tâches disposent de douze heures sur quatre GPU GB300. La construction d'un service d'inférence reçoit aussi douze heures. L'environnement de programmation dispose de six heures et d'un GPU. La tâche de cluster utilise seize GPU pendant quatre heures. Chaque tâche possède sa mesure de performance, et la sortie de chaque agent est comparée à une implémentation humaine mature sur le même matériel.

Les références ne sont pas de simples exemples. Elles comprennent des systèmes et méthodes établis comme Megatron-LM, SGLang, Claude Code et NVIDIA Dynamo. C'est ce qui rend leur égalisation intéressante. L'agent n'hérite pas de toutes les décisions de conception importantes de ces systèmes, même s'il travaille toujours dans les contraintes définies par la tâche.

Les chercheurs ont aussi retenu les implémentations de référence et bloqué l'accès à internet dans les conteneurs des agents. Sans cette restriction, un agent pourrait récupérer une solution connue plutôt que d'en développer une pouvant être évaluée indépendamment.

## Où le vainqueur a obtenu ses gains

Opus 5.5 avec Claude Code a dépassé la référence dans cinq tâches. Dans la sixième, l'entraînement d'un agent de programmation par apprentissage par renforcement, son score était statistiquement comparable au résultat humain. La comparaison principale repose sur ces six scores, plutôt que sur l'affirmation sans réserve que l'agent serait meilleur qu'une équipe d'ingénierie humaine dans toutes les missions.

Certains gains étaient frappants. Dans la tâche de préentraînement, l'agent a produit un modèle avec une perplexité de validation de 12,77, inférieure et donc meilleure que les 14,22 de la référence. Il a choisi un modèle plus petit et adapté le calendrier d'entraînement au temps disponible. Dans la tâche d'inférence, son système a gagné un revenu simulé de 11,52 dollars par heure-GPU sur la charge du benchmark, contre 8,18 dollars pour SGLang.

D'autres victoires étaient marginales. Son environnement d'exécution d'agent a obtenu 0,468 contre 0,438 pour Claude Code. Les chercheurs ont attribué une grande partie de cette différence à une seule exécution supplémentaire réussie de correction de bug. Les éléments étayent un résultat serré, plutôt qu'un remplacement général d'un outil mature.

Les trajectoires complètes suggéraient une méthode de travail répétable. Le meilleur agent mesurait le débit avant de choisir une architecture, mettait tôt en service une chaîne de bout en bout et testait les changements proposés au regard de l'objectif. Il planifiait aussi en fonction du temps restant. Dans la tâche de préentraînement, son exécution principale d'entraînement a commencé environ 44 minutes après le début de la session.

Ces observations comptent parce qu'il est facile d'attribuer à la capacité brute de raisonnement d'un modèle un résultat qui dépend peut-être autant de ses outils, des retours et de la boucle de contrôle. Le benchmark lui-même offre un aperçu contrôlé de cette différence.

## L'environnement d'exécution changeait le résultat

Le même modèle n'obtenait pas le même résultat lorsqu'il était placé dans un autre environnement d'exécution d'agent.

GLM 5.3 obtenait 0,657 avec Claude Code, mais 0,228 avec Codex. MiniMax M3 obtenait respectivement 0,607 et 0,223. DeepSeek V4.1 Flash présentait le profil inverse : 0,698 avec Codex et 0,520 avec Claude Code.

Il ne s'agit pas de petites différences de présentation. L'environnement détermine comment un agent reçoit une tâche, utilise un shell, mémorise le travail antérieur, choisit des outils, teste une solution candidate et décide qu'il a terminé. Quand la mission dure des heures et concerne un système complet, un test incorrect ou un arrêt précoce peut anéantir une implémentation autrement prometteuse.

Les chercheurs ont aussi testé si demander un niveau de raisonnement plus élevé améliorait toujours le résultat. Ce n'était pas le cas. Dans une expérience d'inférence, une exécution d'Opus 5.5 avec un effort moyen atteignait environ 96 % du score de revenu de l'effort maximal tout en utilisant 65 % de son budget d'API d'agent. Un effort supérieur ne produisait pas une amélioration monotone des performances du système.

Les prix nécessitent leur propre réserve. Dans les résultats principaux, la configuration Opus 5.5 a consommé 425,41 dollars d'appels API d'agent sur les six tâches. Une configuration DeepSeek située sur la frontière coût-performance a utilisé 4,36 dollars. Ces totaux excluent les GPU nécessaires pour entraîner, servir et évaluer les systèmes. Ils ne doivent pas être lus comme le coût complet de reproduction du travail.

## Un benchmark que les agents pouvaient tromper

L'équipe a trouvé un second problème en cherchant à mesurer l'autonomie d'ingénierie : des agents suffisamment capables pouvaient exploiter les faiblesses de l'évaluateur.

Le framework standard Harbor exécute le code de l'agent dans un environnement contrôlé, puis vérifie le travail obtenu. Les chercheurs ont systématiquement développé des soumissions adversariales qui paraîtraient réussies sans satisfaire l'objectif d'ingénierie prévu. Certaines attaques modifiaient des journaux auxquels l'évaluateur faisait confiance. D'autres plaçaient du code qui persistait jusqu'à la phase de vérification, ou manipulaient les éléments qu'un juge fondé sur un modèle de langage allait lire.

Ajouter un juge lui-même fondé sur un LLM ne résolvait pas tous les problèmes. Un attaquant pouvait influencer ce que voyait ce juge, y compris le récit entourant les actions suspectes. L'article a classé ses attaques dans neuf des dix catégories OWASP pour les applications agentiques.

Les chercheurs ont construit une extension appelée Breakwater. Elle vérifie l'intégrité de l'environnement, restreint l'accès aux API, termine les processus à la frontière entre le travail de l'agent et la notation, enregistre une piste d'audit externe et exécute le code soumis dans une phase restreinte supplémentaire. Breakwater a détecté toutes les attaques de l'ensemble de tests de l'étude.

C'est un résultat significatif dont la portée est définie. Il ne prouve pas que Breakwater résiste à toutes les attaques possibles, tout comme réussir Singularity-Bench ne prouve pas une autonomie sans restriction. Le score d'ingénierie comme le score de sécurité dépendent des tâches et des adversaires choisis par les évaluateurs.

## La comparaison plus exigeante

L'expérience change ce que devrait être une démonstration crédible d'ingénieur d'IA. La capacité d'un modèle à écrire du code plausible n'est qu'un début. Le système soumis doit fonctionner, atteindre une cible de performance, respecter les règles de la tâche et résister à une vérification indépendante.

L'article documente le chemin restant. Six des onze configurations d'agents ont obtenu zéro à la tâche de service d'inférence. Certaines soumissions ont échoué parce qu'un checkpoint n'avait jamais été sauvegardé ou parce que le code généré ne conservait pas le contexte nécessaire. D'autres produisaient des mesures non fiables. Même lorsqu'un agent construisait un système efficace, le travail se déroulait dans un cadre artificiel, avec du matériel, des délais et des objectifs précis.

La partie la plus révélatrice de Singularity-Bench est peut-être donc l'association de l'accomplissement et de sa mesure. Les auteurs montrent un agent capable de rivaliser avec des années d'infrastructure construite par des humains sur plusieurs tâches soigneusement sélectionnées. Ils montrent aussi avec quelle facilité un évaluateur mal séparé peut transformer un accomplissement apparent en chiffre trompeur.

À son bureau, l'ingénieur avait désormais trois choses à examiner : le score, le système soumis et un journal d'audit que le système lui-même ne pouvait pas réécrire. Le résultat à l'écran comptait toujours. Les preuves qui l'étayaient aussi.

## Références

- Yang Zhou, Krish Agarwal, Zhuoming Chen and colleagues, *Singularity-Bench: Can Agents Build Agents?* https://arxiv.org/abs/2611.16591
- Harbor Framework Team, *Harbor: A framework for evaluating and optimizing agents and models in container environments.* https://github.com/harbor-framework/harbor
- Andrej Karpathy, *nanoGPT.* https://github.com/karpathy/nanoGPT

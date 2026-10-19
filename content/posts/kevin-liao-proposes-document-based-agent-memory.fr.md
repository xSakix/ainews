+++
title = "Kevin Liao propose une mémoire d'agents fondée sur des documents"
slug = "kevin-liao-memoire-agents-fondee-documents"
description = "Le workflow du développeur conserve spécifications et décisions dans du Markdown modifiable. Son argument s'accompagne d'une implémentation open source, mais d'aucun benchmark comparatif."
tags = ["agents", "tools", "essays"]
date = 2026-10-04T09:23:37+02:00
draft = false
+++

Le développeur Kevin Liao propose de donner aux agents de programmation un ensemble entretenu de documents de projet, estimant que retrouver des extraits isolés de conversations fait perdre trop de sens au projet.

Dans un essai publié le 3 octobre, Liao décrit un espace contenant instructions, spécifications, décisions, recherches et index. Un agent consulte les documents pertinents avant le travail et les actualise après, alors que les raisons de ses modifications restent dans le contexte.

Pour un développeur reprenant un projet dans une nouvelle session, l'intérêt est un dossier que l'humain comme l'agent peut inspecter. Une spécification peut préserver ensemble le but d'une fonctionnalité et ses contraintes, tandis qu'un document de décision peut conserver les raisons d'un choix.

La critique de Liao vise la recherche par similarité. Il estime qu'un extrait apparemment pertinent peut être périmé, omettre son contexte original ou masquer une lacune que l'agent n'a aucune raison de chercher. Son affirmation que toute la catégorie des plugins de mémoire partage ces problèmes est une opinion, soutenue dans l'essai par son expérience plutôt que par une comparaison de systèmes concurrents.

Son alternative change la règle d'entretien. Lorsque le projet évolue, l'agent modifie le document actuel au lieu d'ajouter seulement un nouveau souvenir des événements. Liao dit avoir commencé par un dossier interne il y a plus d'un an, puis transformé cette pratique en Operator Memory.

Le README du projet open source décrit trois emplacements documentaires : connaissances privées du projet, connaissances partagées du dépôt et règles personnelles transversales. Il liste des adaptateurs pour Claude Code, Codex et d'autres cadres d'exécution, et documente l'installation par un utilitaire npm.

Le dépôt reconnaît aussi une dépendance pratique : un nouveau projet a peu de documentation, donc il faut rédiger les spécifications avant que les sessions suivantes puissent les entretenir. Les mises à jour fiables au cours de longues conversations restent sur sa feuille de route. Operator Memory est disponible sous licence BSD 3-Clause.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Kevin Liao a publié son essai sur la mémoire documentaire le 3 octobre ; instructions, spécifications, décisions, recherches et index ; workflow consulter/construire/actualiser | VÉRIFIÉ | [Source](https://liao.gg/blog/agents-dont-need-memory) | aucune |
| La recherche par similarité peut omettre le contexte, faire remonter des connaissances périmées et laisser des lacunes inconnues ; critique générale des plugins de mémoire | OPINION | [Source](https://liao.gg/blog/agents-dont-need-memory) | aucune ; argument de l'auteur, sans benchmark comparatif |
| Liao dit utiliser l'approche depuis plus d'un an et avoir développé Operator Memory | SELON LA SOCIÉTÉ | [Source](https://liao.gg/blog/agents-dont-need-memory) | aucune ; usage autodéclaré |
| Emplacements privés, partagés et personnels ; adaptateurs Claude Code et Codex listés ; utilitaire npm ; licence BSD 3-Clause | VÉRIFIÉ | [Source](https://github.com/aerovato/operator-memory) | aucune ; implémentation et licence documentées, non validation en exécution |
| Documents initiaux peu fournis et feuille de route des mises à jour fiables | VÉRIFIÉ | [Source](https://github.com/aerovato/operator-memory) | aucune ; précisions du README |
| Les dossiers modifiables permettent aux humains et aux agents d'inspecter ensemble le but du projet et les décisions | ANALYSE | [Source](https://github.com/aerovato/operator-memory) | Déduction du Markdown lisible et de l'actualisation des documents de référence |

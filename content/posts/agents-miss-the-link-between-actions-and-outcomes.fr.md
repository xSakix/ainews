+++
title = "Les agents manquent le lien entre actions et résultats"
slug = "agents-manquent-lien-entre-actions-et-resultats"
description = "Une prépublication trouve qu'une grande partie du bénéfice de l'historique survit au mélange des actions passées. Associer explicitement chaque action à son résultat améliore la réussite des tâches."
tags = ["research", "agents"]
date = 2026-10-06T04:07:31+02:00
draft = false
+++

Les agents de langage échouent souvent à relier une action passée à l'observation qu'elle a produite, même lorsque leur historique d'interaction complet reste dans le contexte, rapporte une nouvelle prépublication.

Jingyu Liu et quatre coauteurs ont étudié des agents qui reçoivent leurs actions précédentes et les retours de l'environnement avant de choisir la suite. L'historique aidait généralement, mais mélanger les anciennes actions ne causait qu'une perte modeste. Cela suggère que les agents utilisaient le relevé sans apprendre de manière fiable quelle action avait conduit à quel résultat.

## Pourquoi c'est important {#why-it-matters}

Pour un ingénieur qui construit un agent utilisant des outils, une transcription n'est utile que si le modèle peut en apprendre quelque chose. Si l'agent lit les résultats passés comme des indices isolés, il peut répéter des actions ratées ou attribuer le succès à la mauvaise étape, alors que tous les tokens pertinents sont présents.

Les chercheurs ont testé l'hypothèse en rompant l'association action-observation. Ils ont mélangé les actions précédentes tout en laissant les observations en place : la transcription conservait ainsi une grande partie du même texte, mais plus une séquence causale fiable. La réussite des tâches a moins diminué que prévu.

Ce résultat négatif change l'interprétation du bénéfice de l'historique. Un taux de réussite supérieur avec davantage de transcription ne montre pas à lui seul que l'agent a acquis une expérience utile. Le modèle pourrait plutôt extraire des indices des observations antérieures ou simplement profiter de texte supplémentaire lié à la tâche.

La correction la plus simple de l'équipe n'ajoutait aucune information nouvelle sur la tâche. Chaque observation était explicitement étiquetée comme le résultat de l'action immédiatement précédente. Selon la prépublication, cette annotation améliorait la réussite et réduisait la répétition de l'action suivante.

## Un contrôleur peut sélectionner une expérience utile

L'article introduit ensuite un calibrateur d'actions appris. Il réévalue les actions antérieures et consigne sélectivement l'expérience pour les décisions futures, plutôt que de demander à l'agent principal d'interpréter une transcription indifférenciée. Les auteurs rapportent une amélioration supplémentaire au-delà des étiquettes explicites de résultat.

La conception sépare deux tâches souvent réunies dans les systèmes d'agents : agir dans un environnement et déterminer ce que l'interaction précédente a enseigné. Cette division est pratique, car elle peut s'insérer dans une boucle d'agent existante sans modifier l'environnement ni ajouter de connaissances externes.

La preuve centrale de la prépublication est comportementale. Elle n'établit pas quelle représentation le modèle forme en interne, et le résumé ne fournit pas de lien vers un code public. Les gains annoncés dépendent aussi des tâches, modèles et formats de transcription testés : ils ne doivent donc pas être traités comme une estimation universelle pour les agents en production.

Le contrôle par historique mélangé est néanmoins particulièrement instructif. Il distingue « la transcription a aidé » de « l'agent a compris son expérience », deux affirmations souvent considérées comme équivalentes dans les évaluations d'agents.

Liu, Zhiwen Wang, Yuxin Jing, Huanyu Zhou et Yong Liu ont soumis la prépublication le 2 octobre 2026. Le changement d'étiquetage des résultats est assez clairement décrit pour que d'autres développeurs le testent dans leurs propres boucles. Le calibrateur appris sera plus difficile à évaluer sans détails d'entraînement ni code publiés.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Une grande partie du bénéfice de l'historique persiste après mélange des actions passées | SELON LA SOCIÉTÉ | [Prépublication de Liu et al.](https://arxiv.org/abs/2610.02769) | aucune ; résultat de prépublication |
| Rompre la correspondance action-observation n'entraîne qu'un recul modeste | SELON LA SOCIÉTÉ | [Prépublication de Liu et al.](https://arxiv.org/abs/2610.02769) | aucune |
| Les étiquettes explicites de résultat améliorent la réussite et réduisent les actions répétées | SELON LA SOCIÉTÉ | [Prépublication de Liu et al.](https://arxiv.org/abs/2610.02769) | aucune |
| Un calibrateur appris améliore la réussite au-delà des étiquettes de résultat | SELON LA SOCIÉTÉ | [Prépublication de Liu et al.](https://arxiv.org/abs/2610.02769) | aucune |
| Le résultat distingue le bénéfice de la transcription de l'apprentissage action-résultat | ANALYSE | [Prépublication de Liu et al.](https://arxiv.org/abs/2610.02769) | déduction tirée du contrôle par mélange |
| La prépublication a été soumise le 2 octobre 2026 | VÉRIFIÉ | [notice arXiv](https://arxiv.org/abs/2610.02769) | métadonnées arXiv |

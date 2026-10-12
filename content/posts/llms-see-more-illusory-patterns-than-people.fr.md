+++
title = "Les LLM voient plus de motifs illusoires que les humains"
slug = "llm-voient-plus-motifs-illusoires-humains"
description = "Une prépublication montre que les modèles de langage infèrent plus facilement des relations à partir d'éléments ambigus que les participants humains. Ses tests contrôlés relient cet effet à des caractéristiques internes sensibles à la fréquence."
tags = ["research", "models"]
date = 2026-10-12T04:01:37+02:00
draft = false
+++

Les modèles de langage formaient des motifs erronés plus forts que les humains lorsque les deux devaient inférer des relations à partir d'éléments ambigus, selon une nouvelle prépublication.

Les auteurs ont adapté des expériences classiques de psychologie dans lesquelles les observations ne contiennent aucune association fiable, mais où les personnes en perçoivent souvent une. Ils ont donné des tâches correspondantes à des participants humains et à plusieurs modèles de langage, puis testé si les modèles reliaient les descriptions positives fréquentes aux groupes majoritaires ou construisaient des explications causales à partir de séquences fortuites.

## Pourquoi c'est important {#why-it-matters}

Pour un analyste utilisant un modèle afin d'interpréter des commentaires d'enquête, des rapports d'incident ou des dossiers clients, la détection fluide de motifs peut transformer un échantillon déséquilibré en récit assuré. L'étude suggère qu'ajouter des observations ne corrige pas nécessairement le problème lorsque la fréquence brute elle-même guide l'inférence.

La comparaison centrale couvre deux formes de perception de motifs illusoires. Dans l'une, un groupe majoritaire apparaît plus souvent et accumule donc davantage d'exemples positifs et négatifs, même si les proportions correspondent à celles d'un groupe minoritaire. Dans l'autre, des événements sans lien sont disposés de sorte qu'une séquence causale soit tentante, mais non étayée.

Dans les expériences rapportées, les modèles étaient plus susceptibles que les participants humains d'approuver l'association trompeuse ou l'explication causale. L'ampleur exacte variait selon la tâche et le modèle : le résultat utile de l'article est donc la direction et la cohérence de l'écart plutôt qu'un pourcentage universel unique.

Les chercheurs ont aussi utilisé des autoencodeurs parcimonieux, outils transformant l'activité interne dense d'un modèle en un ensemble plus petit de caractéristiques interprétables. Ils rapportent que les caractéristiques associées à une perception globale de la fréquence augmentaient avec la réponse fondée sur un faux motif, tandis que celles associées à une orientation plus analytique allaient dans l'autre sens. Il s'agit d'une corrélation interne au modèle, pas d'une preuve que l'une ou l'autre caractéristique cause le jugement.

## La comparaison est contrôlée, mais restreinte

La force de l'article est sa comparaison directe avec les humains. Les deux groupes reçoivent des versions des mêmes éléments, et les tâches dérivent de démonstrations établies en psychologie cognitive. Les auteurs ont également publié du code, permettant à d'autres chercheurs de varier les prompts, les modèles et les réglages d'échantillonnage.

Les limites comptent. La réponse d'un modèle de langage est générée à partir de données d'entraînement et de conventions de prompt, tandis que celle d'un participant reflète une personne dans une expérience. Faire correspondre la tâche visible ne rend pas ces processus équivalents. Les modèles et prompts étudiés sont aussi un échantillon d'une population changeant rapidement, pas une propriété fixe de tous les modèles de langage.

Le travail identifie néanmoins un mode d'échec concret : un modèle peut traiter le nombre d'exemples observés comme un indice de proportions ou de causes. Cette distinction est assez simple pour être testée dans des systèmes déployés en gardant les ratios constants tout en modifiant la taille des groupes.

## L'étude a également montré

L'association erronée se renforçait lorsque les éléments encourageaient une lecture globale, ce qui compte car de nombreux prompts de résumé demandent un seul motif général. Un cadrage analytique réduisait cette tendance dans certaines conditions, suggérant que les instructions peuvent modifier la réponse sans éliminer la sensibilité sous-jacente.

La prépublication et son code sont disponibles dès maintenant. Des réplications avec des modèles plus récents et des données opérationnelles naturelles montreraient si l'effet de laboratoire prédit les erreurs dans le travail analytique réel.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| La prépublication rapporte une perception de motifs illusoires plus forte chez les modèles de langage testés que chez les participants humains | SELON LA SOCIÉTÉ | https://arxiv.org/abs/2610.07791 | aucune |
| Les expériences adaptent des tâches classiques de corrélation illusoire et de motifs causaux | VÉRIFIÉ | https://arxiv.org/abs/2610.07791 | aucune |
| Des caractéristiques d'autoencodeurs parcimonieux associées à la sensibilité à la fréquence et à l'orientation analytique suivent l'effet rapporté | SELON LA SOCIÉTÉ | https://arxiv.org/abs/2610.07791 | aucune |
| Le résultat sur les caractéristiques internes est corrélationnel plutôt qu'une intervention causale | VÉRIFIÉ | https://arxiv.org/abs/2610.07791 | aucune |
| Les auteurs ont publié le code des expériences | VÉRIFIÉ | https://arxiv.org/abs/2610.07791 | aucune |

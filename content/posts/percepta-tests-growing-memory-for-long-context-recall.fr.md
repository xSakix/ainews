+++
title = "Percepta teste une mémoire extensible pour les longs contextes"
slug = "percepta-teste-memoire-extensible-longs-contextes"
description = "Spotlight Memory accède à une petite zone d'un stockage extensible à chaque étape. Percepta rapporte une forte récupération d'information au-delà de la longueur d'entraînement des modèles."
tags = ["models", "research"]
date = 2026-10-03T09:45:58+02:00
draft = false
+++

Percepta, entreprise de recherche en IA, rapporte que son architecture Spotlight Memory retrouve des informations dans des contextes seize fois plus longs que ses séquences d'entraînement, tout en maintenant fixe le travail de chaque accès mémoire.

L'architecture donne à un modèle de langage un stockage extensible et lui apprend où placer l'information. Christos Tzamos, Guoqing Zheng et Athul Jacob décrivent des expériences contrôlées dans un billet technique du 2 octobre, comparant des modèles aux nombres approximatifs de paramètres et aux données d'entraînement identiques.

**Pourquoi c'est important :** Un chercheur construisant des modèles pour de longs documents obtient des éléments en faveur d'une mémoire gardant les informations anciennes accessibles sans relire tous les tokens précédents. Le compromis est explicite : le stockage peut grandir, tandis que le modèle n'en touche qu'un petit voisinage à chaque étape.

Le [rapport de Percepta](https://www.percepta.ai/blog/spotlight-memory) décrit la tension entre deux approches existantes. L'attention complète conserve l'information des tokens précédents, mais compare chaque nouvelle requête à cet historique. Les modèles récurrents à état fixe compriment le passé dans un stockage limité ; cela réduit le coût de traitement, mais davantage d'informations finissent par se disputer la même capacité.

Spotlight associe plutôt l'information à des adresses sur une grille bidimensionnelle. Une écriture alloue une cellule à la première utilisation d'une adresse ; les suivantes peuvent la modifier. Une requête lit les cellules voisines. Leur nombre reste fixe même lorsque la collection de cellules allouées grandit.

Le modèle apprend ces adresses pendant l'entraînement. Toutes les cellules partagent les mêmes règles apprises d'enregistrement et de mise à jour ; ajouter du stockage n'exige donc pas d'ajouter des poids au modèle. Une fonction de pondération lisse répartit lectures et écritures sur les cellules voisines, permettant à l'entraînement d'ajuster graduellement une adresse.

Le mécanisme ressemble à un classement dont l'armoire peut s'étendre tandis qu'une recherche vise directement quelques tiroirs. La difficulté est d'apprendre un classement utile : questions correspondantes et faits enregistrés doivent aboutir à des adresses compatibles. Les expériences de Percepta testent cette aptitude avant d'appliquer la conception à la modélisation du langage.

## De petits modèles conservent des faits au-delà de l'entraînement

Percepta a entraîné de zéro des modèles de 140 millions, 280 millions et 670 millions de paramètres sur FineWeb-Edu, un jeu de textes du web. Dans chaque groupe de taille, les modèles voyaient les mêmes données dans le même ordre. Les chercheurs ont ajusté la largeur des couches à propagation avant pour que les nombres de paramètres diffèrent d'au plus 0,1 %.

L'entraînement initial utilisait des séquences d'environ 8 000 tokens, les fragments de texte traités par un modèle. Les chercheurs ont ensuite testé la récupération dans des séquences atteignant environ 128 000 tokens : un seul enregistrement était inséré dans un long contexte, et le modèle devait le retrouver. C'est l'extension par seize annoncée dans le résultat principal.

Selon Percepta, Spotlight a atteint 93–100 % de rappel aux trois tailles de modèle dans le contexte testé le plus long. Les alternatives récurrentes à état fixe atteignaient au mieux environ 6 %, tandis que l'attention obtenait zéro au-delà de la longueur d'entraînement dans ce test, y compris après remise à l'échelle des positions. Le résultat concerne la localisation d'un enregistrement inséré, pas tous les raisonnements sur documents longs.

La comparaison en contexte court était moins spectaculaire. À la plus grande taille, la moyenne de Spotlight sur une série de tâches de modèles de langage restait proche des alternatives. Son avantage était de conserver l'accès à l'information lorsque le contexte grandissait, pas de progresser largement sur toutes ces tâches.

Percepta a ensuite donné à chaque point de contrôle disponible le même entraînement supplémentaire en long contexte. Spotlight a conservé son avance en récupération et obtenu la plus faible perte sur données réservées pour chaque longueur et taille testées. Une tâche distincte de classification de questions s'améliorait aussi à mesure que des exemples étiquetés remplissaient le prompt, soutenant le lien entre mémoire croissante et récupération utile.

Les résultats restent les premières expériences de Percepta. Le rapport relie sa proposition à l'apprentissage continu, mais la preuve concrète ici est que des poids fixes peuvent apprendre à organiser une mémoire croissante. Son plus grand modèle contient 670 millions de paramètres ; le transfert de ce comportement à des systèmes déployés beaucoup plus grands reste une question ouverte.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Percepta a publié Spotlight Memory le 2 octobre ; la citation nomme Christos Tzamos, Guoqing Zheng et Athul Jacob. | VÉRIFIÉ | [Billet technique](https://www.percepta.ai/blog/spotlight-memory) | aucune |
| La conception apprend des adresses sur une grille 2D, alloue des cellules à la première écriture, partage les règles de mise à jour et utilise des lectures et écritures locales différentiables à coût d'accès constant. | SELON LA SOCIÉTÉ | [Description de l'architecture](https://www.percepta.ai/blog/spotlight-memory) | aucune |
| L'entraînement comparait des modèles de 140, 280 et 670 millions sur des données FineWeb-Edu identiques dans le même ordre à chaque taille, avec un contexte de 8K et des écarts de paramètres d'au plus 0,1 %. | SELON LA SOCIÉTÉ | [Protocole d'entraînement](https://www.percepta.ai/blog/spotlight-memory) | aucune |
| À 128K, seize fois les 8K d'entraînement, Spotlight atteignait 93–100 % de rappel d'une information isolée (500 échantillons), les références à état fixe au plus 5,6 %, et l'attention 0 % entre 16K et 128K. | SELON LA SOCIÉTÉ | [Résultats RULER](https://www.percepta.ai/blog/spotlight-memory) | aucune |
| À 670 millions, les moyennes en contexte court étaient Spotlight 33,1, GDN-2 33,8, attention 33,3 et Gated DeltaNet 34,1. | SELON LA SOCIÉTÉ | [Évaluation du langage](https://www.percepta.ai/blog/spotlight-memory) | aucune |
| Chaque point de contrôle disponible a reçu 1,17 milliard de tokens supplémentaires à 128K ; Spotlight a conservé la meilleure récupération et la perte de test la plus basse. TREC-coarse à 670 millions est passé de 63 % à 85 % lorsque le contexte grandissait de 8K à 128K. | SELON LA SOCIÉTÉ | [Entraînement long contexte et classification](https://www.percepta.ai/blog/spotlight-memory) | aucune |
| Le stockage extensible sépare capacité mémoire et travail par accès ; ces expériences de récupération sur petits modèles ne résolvent pas le comportement en grand déploiement. | ANALYSE | [Conception et périmètre expérimental](https://www.percepta.ai/blog/spotlight-memory) | aucune |

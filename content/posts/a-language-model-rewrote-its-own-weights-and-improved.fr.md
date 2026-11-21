+++
title = "Un modèle de langage gagne en précision en réécrivant ses poids"
slug = "modele-de-langage-plus-precis-en-reecrivant-ses-poids"
description = "Des chercheurs ont donné à un modèle ouvert de 27 milliards de paramètres accès à ses poids, à des réponses notées et à un outil de test, tout en bloquant les gradients et les optimiseurs. Le modèle a gagné 6,6 points de précision sur des problèmes tenus à l’écart et réparé une copie endommagée de lui-même, tandis que les modèles plus petits ont échoué dans les mêmes conditions."
tags = ["models", "research"]
date = 2026-11-21T04:12:00+01:00
draft = false
+++

Devant une console Python, un modèle avait accès à ses propres poids. Il pouvait examiner ses états cachés, modifier certaines matrices et demander à une copie de lui-même de résoudre un autre problème. Il ne pouvait pas calculer de gradient. Il disposait en tout et pour tout de vingt propagations avant et d’un temps limité.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

Jiajun Fan et dix coauteurs ont placé quatre modèles ouverts d’une même famille dans cet environnement. Le modèle de 2 milliards de paramètres ne s’est pas modifié. Ceux de 4 et 9 milliards ont essayé des changements aléatoires qui ont dégradé leurs performances. Celui de 27 milliards a mesuré dans quelles directions ses états cachés différaient, puis effectué des modifications suivant ces directions. Il ne les conservait que lorsqu’un test apparié en confirmait l’intérêt. L’une de ces modifications a augmenté de 6,6 points de pourcentage sa précision sur 490 problèmes tenus à l’écart.

Les auteurs appellent cette méthode l’autoréécriture. Leur conclusion centrale est précise et lourde de conséquences : un modèle déjà déployé peut améliorer durablement ses propres poids en raisonnant uniquement par propagation avant. L’étude est une prépublication. Selon ses auteurs, c’est la première démonstration de ce type.

## Un modèle qui a accès à ses propres paramètres

L’entraînement sépare habituellement le système qui cherche de meilleurs poids du modèle qui les utilisera ensuite. Un optimiseur calcule les gradients d’une fonction de perte, des ingénieurs choisissent les données et les réglages, puis une grappe de calcul enregistre le résultat dans un nouveau fichier de poids. L’inférence débute lorsque ce processus est terminé.

Fan et ses collègues ont retiré l’optimiseur, mais fourni des outils au modèle. Il disposait de réponses notées à des exercices, d’un accès à ses tenseurs de poids et d’une session Python qui conservait son état d’un échange à l’autre. Il pouvait soumettre les mêmes problèmes au modèle d’origine et à sa version modifiée en utilisant les mêmes graines aléatoires. Il pouvait aussi lire les états cachés produits par le modèle sur des textes de son choix.

L’environnement imposait ces limites. Les gradients étaient désactivés. Les appels aux optimiseurs, au réseau, à de nouveaux processus et aux fonctions de chargement de modèles étaient refusés. Le modèle ne pouvait modifier ni les plongements d’entrée, ni la normalisation finale, ni la couche de sortie. Une session autorisait au maximum 20 propagations avant et 200 exécutions de code.

Un test apparié comparait les réponses problème par problème. Cette précaution comptait, car un léger gain global aurait pu tenir aux fluctuations d’échantillonnage. Le dispositif indiquait combien de réponses initialement fausses devenaient justes, combien suivaient le chemin inverse et à quelle fréquence chaque version épuisait son budget de 16 384 tokens.

Dans le protocole le plus strict, le dispositif testait aussi une seule fois chaque modification proposée sur des exercices réservés que le modèle ne pouvait pas examiner. Le modèle soumettait ensuite la modification ou la retirait. Il l’a retirée dans cinq des huit premières sessions. Aucune modification acceptée n’a réduit la précision du modèle resté en service.

## Ce que le plus grand modèle a changé

Le modèle de 27 milliards de paramètres n’a pas exploré chacun de ses paramètres. Dans ses états cachés, il a repéré des directions associées aux échecs, puis réduit la contribution de certaines matrices de sortie dans ces directions. L’opération s’apparentait à la soustraction d’une composante de rang un à une matrice.

Cette intervention a réduit un défaut manifeste : certaines réponses répétaient une phrase jusqu’à épuiser le budget de tokens. Dans un exemple tenu à l’écart, le modèle de base a répété la même phrase 549 fois sans jamais répondre. La version modifiée a résolu le problème.

Sur l’ensemble d’évaluation fixé à l’avance, la meilleure modification a produit le gain de 6,6 points. Lors de deux sessions, les améliorations observées correspondaient, selon le test apparié des auteurs, à des probabilités inférieures à une sur 100 000. Après la huitième session, la précision atteignait 63,8 %.

À chaque session, l’exploration repartait des poids de base, mais toute modification acceptée remplaçait le modèle en service. Les décisions se cumulaient ainsi sans que toutes les modifications proposées soient aveuglément empilées. D’après les auteurs, la précision a augmenté ou est restée stable tout au long des huit sessions.

Le gain n’exigeait aucun calcul supplémentaire pour les réponses ultérieures. Une fois enregistrée, la modification résidait dans le fichier de poids. C’est ce qui la distingue des méthodes qui augmentent le calcul à l’inférence et dépensent à chaque réponse davantage de tokens ou d’échantillons pour améliorer le résultat.

## Réparer sans disposer de l’original

L’équipe a aussi créé une panne dont elle connaissait la cause. Dans une matrice de sortie d’un perceptron multicouche, elle a remplacé huit lignes consécutives par du bruit mis à l’échelle à 200 fois l’écart-type de la matrice. Le modèle endommagé ne résolvait presque plus rien.

Le modèle chargé de la réparation était intact, mais il ne pouvait examiner que les exécutions et les poids de la copie corrompue. Il savait que certaines valeurs étaient erronées, sans savoir où se trouvaient les dégâts ni comment ils avaient été provoqués. Il n’a jamais lu les valeurs intactes correspondantes.

Le modèle de 27 milliards de paramètres a localisé la matrice défectueuse et écrit ses propres valeurs de remplacement. Une réparation trouvée à partir de problèmes mathématiques formulés en texte s’est également révélée efficace sur six bancs d’essai d’images que la session n’avait jamais vus. Toutes épreuves confondues, la copie réparée a retrouvé 83 % de la précision du modèle de base. Sur ScreenSpot-v2, elle est passée de zéro à 89 %, contre 93 % pour le modèle intact.

Ce test permet d’écarter une explication simple du résultat principal. Le modèle aurait pu trouver une modification très ciblée qui exploite les particularités des exercices. En réparant un composant délibérément endommagé et en rétablissant une partie des performances sur des images, il montre qu’il sait identifier et restaurer en partie une fonction plus générale.

Cela ne montre pas qu’un modèle puisse réparer n’importe quel dégât. La corruption touchait un seul bloc construit pour l’expérience, et les essais portaient sur quatre tailles d’une même famille, Qwen3.5. Le modèle disposait de réponses notées à des exercices et d’un accès exceptionnellement direct à ses tenseurs internes. Les assistants hébergés ordinaires ne disposent d’aucun de ces privilèges.

## La limite liée à la taille

Les modèles plus petits révèlent la limite actuelle. Celui de 2 milliards de paramètres n’a pas envisagé ses poids comme quelque chose qu’il pourrait utilement modifier. Les versions de 4 et 9 milliards ont ajouté du bruit aléatoire. Lorsqu’un test révélait une dégradation, elles tentaient une autre intervention au hasard.

Le modèle de 27 milliards a mené à bien une démarche plus longue. Il a diagnostiqué un symptôme, inspecté les activations, formulé une hypothèse, modifié une matrice, exécuté un test apparié et revu son plan lorsque le résultat était négatif. Les auteurs y voient une capacité qui se manifeste avec la taille du modèle, mais quatre tailles d’une seule famille ne permettent pas de situer un seuil général.

Une autre prépublication parue la même semaine étudiait une configuration différente. Un modèle de langage externe choisissait les poids à modifier dans des modèles cibles plus petits. Ce système a égalé la recherche en boîte noire sur SmolLM2 et Qwen2.5 et l’a dépassée sur Pythia. Dans l’étude de Fan, c’est le même modèle qui effectue la modification et qui en fait l’objet. C’est cette particularité qui étaye la conclusion de plus grande portée des auteurs.

Les auteurs rapprochent le résultat de l’auto-amélioration récursive. Leur expérience reste loin d’une boucle autonome. Des humains ont fourni la tâche, le signal d’échec, les outils, les contraintes de modification et le test d’acceptation. Les sessions ont duré plusieurs heures sur un seul GPU. Les résultats les plus probants concernent un ensemble délimité de problèmes de raisonnement et une seule panne artificielle.

Ces limites permettent aussi d’examiner le résultat. Chaque modification acceptée a passé une comparaison appariée, chaque problème réservé est resté en dehors de la session de modification, et les échecs des petits modèles figurent eux aussi dans le compte rendu.

De retour à la console Python, le modèle a utilisé sa dernière propagation avant et laissé une modification sur disque. La réponse suivante ne nécessitait ni prompt plus long ni échantillon supplémentaire. La différence tenait à quelques matrices modifiées.

## Références

- Fan, J., He, N., Yang, C., Mao, A., Zhu, X., Cheng, C., Liang, K., Shen, S., Li, Z., Guo, R., & Liu, G. (2026). *Language Models Can Rewrite Their Own Weights*. https://arxiv.org/abs/2611.21885
- Yang, C., et al. (2026). *Can an LLM Fix a Language Model Without Training It?* https://arxiv.org/abs/2611.25613

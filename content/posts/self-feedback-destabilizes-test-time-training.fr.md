+++
title = "L'auto-rétroaction déstabilise l'entraînement à l'inférence"
slug = "auto-retroaction-destabilise-entrainement-a-l-inference"
description = "Une prépublication retrace comment les modèles qui actualisent leurs poids à partir de leurs propres textes peuvent entrer dans une boucle de rétroaction nuisible sur de longs flux d'inférence."
tags = ["research", "models"]
date = 2026-10-08T03:56:31+02:00
draft = false
+++

Des modèles de langage entraînés sur leurs propres sorties pendant l'inférence sont devenus moins bons pour prédire des textes humains indépendants, selon une prépublication qui suit cette boucle sur de longs flux.

L'entraînement au moment de l'inférence permet au modèle d'actualiser ses poids pendant son utilisation, faisant du modèle lui-même une forme de mémoire de travail. Cheng Luo, Bing Li et Bernard Ghanem ont testé ce qui se passe lorsque le texte utilisé pour ces mises à jour est généré par ce même modèle en évolution.

Le résultat compte pour les développeurs d'agents qui apprennent continuellement de leur propre travail. Une mise à jour peut faciliter la prédiction du dernier passage généré tout en réduisant discrètement la performance sur de nouveaux textes humains. Répéter cette amélioration locale transforme à la fois l'apprenant et la source de sa prochaine leçon.

## Le générateur et l'apprenant se sont mutuellement écartés de leur trajectoire

Les chercheurs ont exécuté trois configurations d'entraînement à l'inférence, étiquetées 125 millions, 760 millions et 3 milliards de paramètres, sur des flux de 128 000 tokens. Dans les trois cas, conserver les mises à jour tirées du texte généré dégradait la prédiction sur un ensemble distinct de textes humains. Des mises à jour Adam ordinaires sur les poids existants de Qwen3-4B produisaient le même schéma.

Apprendre pendant l'inférence n'était pas nuisible en soi. Les mêmes mécanismes amélioraient les performances lorsque le texte entrant venait d'humains. L'échec apparaissait quand le texte généré retournait dans le modèle qui allait produire le prochain segment d'entraînement.

L'article isole cette boucle au moyen d'expériences appariées. Dans « Fixed Generation », une copie gelée fournissait le texte d'entraînement généré tandis qu'un autre modèle continuait à s'actualiser. Selon les auteurs, cela supprimait plus de 98 % des dommages mesurés dans les deux petites configurations. La comparaison désigne le générateur changeant, plutôt que le seul texte synthétique, comme principale source d'instabilité.

Une seconde expérience de rejeu distinguait deux coûts. Le modèle devait d'abord lire un texte dégradé au fil du temps, puis stockait de nouvelles modifications en s'entraînant dessus. Un test apparié à mise à jour unique révélait le conflit immédiat : chaque mise à jour améliorait la prédiction de son passage source, mais dégradait celle de nouveaux textes humains.

Ce conflit est facile à manquer lorsque le signal d'entraînement et la cible d'évaluation sont le même passage. La mise à jour réussit selon son objectif local : la perte baisse sur le texte qui l'a produite. Les dommages n'apparaissent que sur du texte humain réservé, servant de référence pour savoir si le modèle préserve sa distribution linguistique plus large en s'adaptant.

## Des preuves indépendantes ont servi de frein

La plupart des exécutions n'échouaient pas de la même façon. Les auteurs indiquent qu'un petit nombre de trajectoires expliquaient beaucoup des plus fortes pertes après une adaptation prolongée en boucle fermée. Cette concentration rend les vérifications moyennes à court terme peu protectrices : un système peut sembler stable jusqu'à ce qu'une séquence de mises à jour auto-générées l'éloigne davantage.

Les longs flux comptent, car chaque mise à jour acceptée change le point de départ de la suivante. Les erreurs ne touchent donc pas seulement la prédiction actuelle ; elles modifient le texte produit et appris plus tard. L'étude mesure ce processus cumulatif plutôt que des étapes isolées d'auto-entraînement.

La mesure d'atténuation proposée, Settlement, évalue une mise à jour candidate des poids sur du texte réel indépendant avant de l'accepter. Dans les deux petites configurations, l'écart moyen restant en fin de parcours était de 0,07 et -0,02 nats, tout en conservant l'adaptation utile au texte réel. La métrique mesure la perte prédictive : des valeurs proches de zéro signifient que la protection comblait largement l'écart avec la condition de comparaison.

Ce sont des résultats des auteurs dans une première version de prépublication arXiv, sans réplication indépendante. Les flux testés et l'objectif de prédiction sont plus étroits que le comportement complet d'un agent déployé, et l'étude n'établit pas à quelle vitesse la même boucle apparaîtrait dans des systèmes de pointe plus grands.

L'expérience donne néanmoins une explication causale d'une intuition familière sur l'auto-entraînement : vérifier qu'une mise à jour explique sa propre source ne suffit pas. Le prochain critère concret des auteurs est externe : une mise à jour doit aussi préserver la prédiction sur des éléments que le modèle en adaptation n'a pas générés.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Conserver les mises à jour issues de textes générés dégradait la prédiction de textes humains indépendants dans trois configurations d'entraînement à l'inférence | SELON LA SOCIÉTÉ | [Prépublication de Luo, Li et Ghanem](https://arxiv.org/abs/2610.05076) | aucune |
| Le même échec apparaissait lorsque Adam actualisait les poids existants de Qwen3-4B | SELON LA SOCIÉTÉ | [Prépublication de Luo, Li et Ghanem](https://arxiv.org/abs/2610.05076) | aucune |
| Les mêmes mécanismes de mise à jour amélioraient les performances sur du texte réel | SELON LA SOCIÉTÉ | [Prépublication de Luo, Li et Ghanem](https://arxiv.org/abs/2610.05076) | aucune |
| Un générateur gelé supprimait plus de 98 % des dommages à 125 et 760 millions de paramètres | SELON LA SOCIÉTÉ | [Prépublication de Luo, Li et Ghanem](https://arxiv.org/abs/2610.05076) | aucune |
| Settlement laissait des écarts finaux de 0,07 et -0,02 nats à 125 et 760 millions de paramètres tout en conservant l'adaptation au texte réel | SELON LA SOCIÉTÉ | [Prépublication de Luo, Li et Ghanem](https://arxiv.org/abs/2610.05076) | aucune |
| La prépublication de trois auteurs a été soumise le 4 octobre 2026 | VÉRIFIÉ | [Notice arXiv](https://arxiv.org/abs/2610.05076) | aucune |

+++
title = "Les exemples amplifient un circuit symbolique déjà dans les modèles"
slug = "exemples-amplifient-circuit-symbolique-deja-dans-modeles"
description = "Une étude d'interprétabilité retrouve la même voie d'abstraction, d'induction et de récupération avant la hausse de précision avec quelques exemples. Les démonstrations semblent renforcer des mécanismes existants plutôt que construire un nouvel algorithme."
tags = ["research", "models"]
date = 2026-10-05T03:59:30+02:00
draft = false
+++

Quand un modèle de langage apprend un motif à partir de plusieurs exemples dans son prompt, il peut sembler assembler une nouvelle procédure à la volée. Une étude mécaniste de la chercheuse indépendante Melissa Wessel propose une autre explication pour une famille de tâches symboliques : la procédure est déjà présente dans le modèle, et les exemples renforcent progressivement le signal qui la traverse.

La prépublication suit un circuit en trois étapes à travers des prompts contenant de zéro à dix démonstrations. Elle retrouve la même voie centrale quand la précision est faible et quand elle est presque parfaite. Les têtes n'apparaissent pas soudainement quand le modèle « comprend » le motif. Leur contribution causale augmente.

L'expérience est circonscrite et ne constitue pas une théorie générale de l'apprentissage en contexte. Mais elle transforme une métaphore séduisante — les exemples éveillent des mécanismes latents — en quelque chose sur quoi les chercheurs peuvent intervenir et qu'ils peuvent tester.

## Des tokens aux variables, puis retour aux tokens

La tâche utilise des motifs abstraits de trois tokens, comme ABA ou ABB. Les tokens sont arbitraires, empêchant le modèle de s'appuyer sur leur sens ordinaire. Il doit déduire quelle position copier dans la réponse.

Des travaux antérieurs ont identifié trois étapes. Les têtes d'abstraction symbolique traduisent les tokens concrets en variables. Les têtes d'induction symbolique opèrent sur ce motif abstrait. Les têtes de récupération reconvertissent la variable prédite en token requis. Wessel suit cette structure dans Gemma 2-2B, Llama 3.1-8B et Qwen 3-4B en ne changeant que le nombre de démonstrations.

Dans Gemma 2-2B, la précision commence à 17 % avec un exemple, atteint 93 % avec quatre et 99 % avec dix. Pourtant, l'analyse de médiation causale détecte déjà les trois étapes avec un seul exemple. Les têtes importantes persistent pour l'essentiel entre des longueurs de prompt voisines, tandis que la contribution causale d'une tête peut être multipliée par huit entre un et dix exemples.

L'interprétation est quantitative plutôt qu'architecturale : les exemples supplémentaires intensifient une voie existante au lieu d'en mobiliser une entièrement différente.

## Transférer le signal entre les prompts

La seule détection peut confondre corrélation et mécanisme ; l'article transfère donc aussi des activations internes entre les exécutions. Insérer les activations de dix exemples dans un prompt à un exemple fait passer la précision de Gemma de 17 % à 88 %. Avec zéro exemple, remplacer les activations des étapes d'induction et de récupération fait passer la précision sur un motif de 1 % à 56 % ; des têtes aléatoires hors du circuit la laissent sous 1 %.

L'intervention la plus frappante utilise un « vecteur de fonction », une activation fixe assemblée à partir des têtes identifiées par l'analyse causale. Son injection avec zéro exemple fait passer la précision de 1 % à 86 % sur la règle ABA. Quand les têtes de récupération en aval sont supprimées, ce rétablissement tombe à 13 %.

Cette dépendance est essentielle. Le vecteur n'agit ni comme une réponse autonome ni comme une impulsion générique au réseau. Il peut largement remplacer l'étape d'induction uniquement parce que les mécanismes de récupération ultérieurs restent disponibles pour lire sa sortie.

## Un résultat utile dans un domaine limité

L'étude fait ressembler l'apprentissage en contexte moins à l'écriture d'un nouveau programme pendant l'inférence qu'à la fourniture d'une entrée à un programme intégré pendant l'entraînement. Si cette vision se généralise, les limites d'un modèle avec quelques exemples dépendraient des circuits contenus dans ses poids et de la capacité d'un prompt à y accéder.

L'article ne montre pas que toutes les démonstrations fonctionnent ainsi. Sa tâche centrale est essentiellement une petite table relationnelle avec une opération de copie. Un test d'analogie sur des chaînes de lettres retrouve une topologie similaire, mais n'est pas répété sur chaque modèle ni avec tout le programme de remplacement d'activations. La méthode d'analyse sélectionne aussi les composants qui distinguent deux règles : elle pourrait donc manquer une infrastructure partagée.

Le résultat est le plus solide comme mécanisme concret d'une capacité simple : les exemples peuvent amplifier une voie symbolique stable bien avant que le comportement ne révèle sa présence.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| L'étude suit les étapes d'abstraction, d'induction et de récupération dans Gemma 2-2B, Llama 3.1-8B et Qwen 3-4B | VÉRIFIÉ | [Prépublication](https://arxiv.org/abs/2609.36265) | aucune |
| La précision de Gemma passe de 17 % avec un exemple à 99 % avec dix ; la contribution par tête est multipliée jusqu'à huit fois | SELON LA SOCIÉTÉ | [Prépublication](https://arxiv.org/abs/2609.36265) | aucune ; expériences de l'auteure |
| Les remplacements d'activations à dix exemples portent la précision avec un exemple à 88 %, et ceux sans exemple la font passer de 1 % à 56 % | SELON LA SOCIÉTÉ | [Prépublication](https://arxiv.org/abs/2609.36265) | aucune ; expériences de l'auteure |
| L'injection d'un vecteur de fonction fait passer la précision ABA sans exemple de 1 % à 86 %, puis à 13 % après suppression de la récupération | SELON LA SOCIÉTÉ | [Prépublication](https://arxiv.org/abs/2609.36265) | aucune ; expériences de l'auteure |
| Pour ces tâches, les démonstrations amplifient un circuit préexistant plutôt qu'elles n'en construisent un nouveau | ANALYSE | [Prépublication](https://arxiv.org/abs/2609.36265) | interprétation des interventions causales dans l'article |
| La généralisation à un raisonnement abstrait plus riche reste ouverte | VÉRIFIÉ | [Prépublication](https://arxiv.org/abs/2609.36265) | limite déclarée |

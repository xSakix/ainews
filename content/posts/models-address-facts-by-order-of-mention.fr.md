+++
title = "Les modèles repèrent les faits selon leur ordre de mention"
slug = "modeles-reperent-faits-selon-ordre-de-mention"
description = "Une prépublication trouve une direction interne commune qui guide les modèles vers le premier, le deuxième ou un fait ultérieur d'un passage. Déplacer une question dans cette direction peut changer le fait retrouvé."
tags = ["research", "models"]
date = 2026-10-06T04:08:31+02:00
draft = false
+++

Les modèles de langage semblent localiser les faits d'un passage en partie selon leur ordre de mention, d'après une nouvelle étude d'interprétabilité.

Yufa Zhou a testé des modèles Qwen, Gemma et Llama sur de courtes listes d'énoncés factuels suivies de questions. Leurs états internes associés aux questions formaient un motif reproductible pour les premier, deuxième et autres faits, même lorsque les noms et sujets changeaient.

## Pourquoi c'est important {#why-it-matters}

Pour un chercheur qui veut comprendre la recherche d'information à l'intérieur d'un modèle, le résultat fournit un mécanisme concret plutôt qu'une corrélation supplémentaire entre activations et réponses. La même direction interne pouvait être déplacée expérimentalement, conduisant une question sur un fait à retrouver un autre fait du passage.

L'article appelle ces positions des « adresses de faits ». Un contexte indique par exemple qu'Alice mange une pomme et Bob une poire. Une question sur Alice et une question sur Bob diffèrent dans le modèle suivant une direction liée à l'ordre de mention des faits. Quand le chercheur ajoutait la direction du premier au deuxième à une question sur le premier fait, le modèle répondait souvent avec le contenu du deuxième.

Cette intervention est la preuve la plus forte de l'étude. Un classificateur peut découvrir de nombreux motifs dans les états cachés sans montrer que le modèle les utilise. Changer la réponse en changeant l'adresse proposée apporte un soutien causal au mécanisme, même si les tests utilisent des listes factuelles contrôlées plutôt que de longs documents naturels.

Sur 64 nouveaux ensembles de mots, l'intervention sélectionnait le fait voulu dans environ cinq cas sur six pour Qwen, environ la moitié pour Gemma et environ un sur trois pour Llama. Les taux exacts étaient respectivement 84,1 %, 53,9 % et 36,2 %. Ces différences montrent que la direction était commune aux familles de modèles, mais pas aussi fiable dans chacune.

## Les adresses occupent un petit espace interne

Zhou rapporte que les adresses de faits se trouvent dans un sous-espace de faible rang. Autrement dit, les modèles n'ont pas besoin d'une direction séparée et sans rapport avec les autres pour chaque position possible ; un petit ensemble de directions décrit une grande partie du motif d'ordre.

Le premier fait mentionné était aussi plus accessible aux modèles que les suivants. Cela ressemble à un effet de primauté dans le rappel humain, mais l'expérience n'établit pas que personnes et transformers utilisent le même mécanisme. Elle identifie une asymétrie mesurable dans les modèles testés.

Le motif apparaissait dans les couches situées vers la fin de la partie médiane, et dans des modèles de 1,5 à 32 milliards de paramètres. Des checkpoints pris pendant l'entraînement suggéraient qu'il se formait tôt plutôt qu'après un long affinage sur instructions. Le code publié avec la prépublication rend les interventions contrôlées inspectables.

Le cadre restreint est aussi la principale limite. Des listes de faits simples isolent nettement l'ordre, tandis que les prompts réels contiennent titres, références répétées, outils et énoncés contradictoires. L'article montre que l'ordre de mention peut servir d'adresse dans des conditions contrôlées ; il ne montre pas que cet ordre domine la recherche dans les transcriptions ordinaires d'agents.

Zhou a soumis la prépublication le 1er octobre 2026. Les prochaines preuves viendront de reproductions sur des documents moins réguliers et de tests visant à déterminer si modifier la structure documentaire change les mêmes directions internes.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Les états des questions sont organisés selon l'ordre des faits dans Qwen, Gemma et Llama | SELON LA SOCIÉTÉ | [Prépublication de Zhou](https://arxiv.org/abs/2610.00910) | aucune ; résultat de prépublication |
| Ajouter un vecteur ordinal peut rediriger une question vers un autre fait | SELON LA SOCIÉTÉ | [Prépublication de Zhou](https://arxiv.org/abs/2610.00910) | aucune ; expérience de l'auteur |
| Le transfert sur 64 ensembles de mots atteint 84,1 % pour Qwen, 53,9 % pour Gemma et 36,2 % pour Llama | SELON LA SOCIÉTÉ | [Prépublication de Zhou](https://arxiv.org/abs/2610.00910) | aucune |
| Les adresses de faits occupent un sous-espace de faible rang et favorisent le premier fait | SELON LA SOCIÉTÉ | [Prépublication de Zhou](https://arxiv.org/abs/2610.00910) | aucune |
| Le motif apparaît de 1,5 à 32 milliards de paramètres et se forme tôt dans le préentraînement | SELON LA SOCIÉTÉ | [Prépublication de Zhou](https://arxiv.org/abs/2610.00910) | aucune |
| Le code de reproduction est public | VÉRIFIÉ | [Dépôt sur l'ordre de mention](https://github.com/MasterZhou1/order-of-mention) | dépôt disponible |

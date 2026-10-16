+++
title = "La réponse était encore dans le modèle"
slug = "reponse-etait-encore-dans-modele"
description = "Une étude de 15 modèles de langage trouve que de nombreux échecs de mémoire de travail surviennent après la sélection du bon élément. Les modèles conservent des informations décodables, mais ne les rapportent pas."
tags = ["research", "models"]
date = 2026-10-16T04:07:00+02:00
draft = false
+++

Un modèle voit une courte liste de symboles, puis une seconde le distrait avant qu'il doive nommer la cible initiale. Il répond par l'élément distracteur. Le diagnostic évident est que le premier symbole a disparu. Pourtant, dans cette scène illustrative, une sonde interne peut encore lire la cible presque parfaitement. La réponse n'a pas été effacée. Quelque chose a mal tourné entre la conserver et la dire.

Cette distinction anime une nouvelle prépublication sur la mémoire de travail des modèles de langage. Ses auteurs ont testé 15 modèles allant de 70 millions à 14 milliards de paramètres sur des tâches conçues pour créer de l'interférence. Ils ont trouvé que les têtes d'attention sélectionnaient souvent la bonne cible même lorsque la réponse finale était fausse. De simples sondes pouvaient décoder la cible depuis les états cachés avec une précision presque parfaite dans de nombreux échecs.

Le résultat remet en cause un raccourci familier de l'évaluation : traiter une sortie fausse comme preuve que l'information sous-jacente est absente. L'article sépare plutôt trois opérations qu'une note de précision unique confond : sélectionner un élément pertinent, préserver son identité et le lire pour en faire une réponse.

## Un problème de mémoire contrôlé

La mémoire de travail n'est pas le stockage à long terme. C'est la capacité temporaire à conserver une information dans un état utilisable pendant que d'autres éléments se disputent l'attention. Les expériences humaines révèlent souvent que l'élément reste partiellement disponible même lorsqu'un participant rapporte le mauvais. Une interférence similaire peut rendre deux souvenirs difficiles à distinguer sans détruire l'un ou l'autre.

Les chercheurs ont construit des tâches permettant de varier la cible, les éléments concurrents et leurs positions. Ils ont ensuite regardé dans les modèles aux points où la cible devait être sélectionnée et transmise. Les modèles couvraient plusieurs échelles et familles, ce qui compte car un motif dans un seul point de contrôle peut être un accident architectural plutôt qu'un mécanisme général.

Dans les essais corrects, le récit attendu se vérifiait : l'attention se concentrait sur la cible et les couches finales produisaient le bon token. Dans de nombreux essais incorrects, la première moitié se vérifiait encore. Les têtes sélectionnant la cible prêtaient attention à la bonne position. Les sondes d'états cachés conservaient assez d'information pour identifier la cible. Pourtant, la sortie reflétait un concurrent.

Une sonde prouve la décodabilité, pas l'utilisation. Un classificateur entraîné après coup peut extraire une information à laquelle le propre calcul du modèle n'accède pas. Les auteurs sont donc allés au-delà de la lecture des états et sont intervenus sur eux.

## Atténuer les concurrents

Le test causal clé supprimait les représentations d'identité des éléments non ciblés. Cette intervention a amélioré la sensibilité, mesurée en d-prime, dans la direction prédite par une explication fondée sur l'interférence. Affaiblir les concurrents rendait la cible stockée plus facile à rapporter par le modèle.

Cela ne signifie pas que toute erreur de mémoire est une erreur de lecture. Les modèles peuvent ne pas encoder un élément, le perdre ou sélectionner le mauvais emplacement. L'affirmation de l'article est plus limitée : une part significative des échecs survient alors que l'information cible reste disponible en interne, et la confusion entre représentations similaires peut bloquer la réponse finale.

La distinction compte pour l'ingénierie. Ajouter du contexte ou répéter la cible attaque un problème de stockage. Cela peut peu aider lorsque le modèle conserve déjà la cible, mais ne peut la séparer du contenu concurrent. Un système confronté au second problème peut nécessiter d'autres prompts, une structure intermédiaire ou des modifications architecturales affinant l'identité lors de la lecture.

Elle compte aussi pour l'interprétation. L'attention des transformers, introduite comme mécanisme reliant les positions d'une séquence, est souvent inspectée comme si prêter attention au bon token établissait ce que sait le modèle. Ici, elle peut pointer vers la cible sans livrer la bonne sortie. À l'inverse, une réponse fausse n'implique pas que l'attention ait manqué la cible.

## Une ressemblance humaine avec des limites

Les auteurs présentent le motif d'interférence comme humain, mais la comparaison est fonctionnelle plutôt que biologique. Un transformer n'a pas besoin d'un système de mémoire humain pour afficher la même séparation comportementale entre disponibilité et rapport. Des erreurs similaires peuvent émerger de mécanismes très différents.

L'échelle ne dissout pas non plus le problème. Tester des modèles jusqu'à 14 milliards de paramètres montre que l'effet subsiste au-delà de minuscules réseaux expérimentaux, mais n'établit pas le même résultat dans des systèmes de pointe beaucoup plus grands ou au post-entraînement propriétaire. Les tâches sont délibérément contrôlées. Les conversations réelles mêlent récupération, suivi d'instructions, planification et génération de façons qui compliquent l'isolement de la source d'un échec.

Les tâches contrôlées sont pourtant précisément l'objectif. Elles permettent de changer un concurrent, d'observer une représentation et de tester une intervention. L'article offre une méthode pour poser une meilleure question après une erreur : l'information n'a-t-elle jamais été encodée, a-t-elle été perdue, ou était-elle présente mais inaccessible au processus de sortie ?

Revenons à la tâche illustrative de symboles. Le modèle donne le mauvais élément et un évaluateur note un échec. Ce verdict est correct à la frontière du produit. En interne, pourtant, le système a peut-être fait l'essentiel du travail. Le prochain progrès pourrait ne pas venir d'une mémoire plus grande, mais de lui apprendre à lire ce qu'il a déjà conservé.

## Références

- Vaswani, A., et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- *Working Memory Readout Bottlenecks in Language Models* (2026). https://arxiv.org/abs/2610.21176

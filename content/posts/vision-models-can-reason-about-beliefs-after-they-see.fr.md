+++
title = "Bien voir permet aux modèles de raisonner sur les croyances"
slug = "bien-voir-modeles-raisonner-croyances"
description = "Sept modèles vision-langage ont perdu plus de 20 points lorsque des problèmes de fausse croyance sont passés du texte aux images. Une étude contrôlée a constaté que la perception, plutôt que la dernière étape du raisonnement, expliquait la majeure partie de cet écart."
tags = ["research", "models"]
date = 2026-11-10T04:04:14+01:00
draft = false
+++

Un enfant regarde une courte scène sur un écran. Une balle rouge se trouve dans un tiroir. Un personnage s'en va, puis un autre déplace la balle dans une boîte. Lorsque le premier revient, l'enfant sait qu'il cherchera dans le tiroir. Remplaçons maintenant l'enfant par un modèle vision-langage. Le modèle sait expliquer une fausse croyance à partir d'un texte, mais le déplacement de l'objet à l'écran modifie sa réponse. Cette scène est illustrative : elle décrit le type de tâche qu'une nouvelle étude isole.

## L'écart visuel

Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall et leurs collègues ont testé sept modèles vision-langage sur des problèmes de fausse croyance. Leur prépublication, acceptée dans la section Evaluations and Datasets de NeurIPS 2026, rapporte plus de 159 000 appels d'API dans un protocole à cinq conditions. Des modèles proches du niveau humain sur les versions textuelles perdaient plus de 20 points de pourcentage lorsque le même problème sous-jacent était présenté visuellement.

Les tests de fausse croyance ont une longue histoire en psychologie. Ils cherchent à déterminer si un sujet peut distinguer la réalité de la connaissance qu'en a une autre personne. Dans le schéma classique, un objet est déplacé pendant l'absence d'un personnage. Pour répondre correctement, le sujet doit prédire ce que croit ce personnage, bien qu'il sache lui-même où l'objet se trouve réellement.

Les modèles de langage récents réussissent souvent les versions textuelles. Michal Kosinski a évalué onze modèles de langage sur quarante tâches de fausse croyance conçues sur mesure et rapporté qu'une version de GPT-4 de 2023 en résolvait 75 %. Une comparaison distincte menée par James Strachan et ses collègues a constaté que certains modèles de langage atteignaient ou dépassaient les performances humaines sur plusieurs tests de théorie de l'esprit. Les deux articles avertissaient aussi qu'une réponse correcte ne prouve pas qu'un modèle raisonne sur les états mentaux de la même manière qu'une personne. Des schémas mémorisés, la structure de la tâche et les indices linguistiques restent des explications possibles.

Le cadre visuel ajoute une autre dépendance. Avant de pouvoir raisonner sur ce que croit un personnage, le modèle doit identifier les personnages, les objets, les lieux et les changements qui déterminent cette croyance. Une mauvaise réponse peut donc provenir du raisonnement social, de la perception ou du lien entre les deux. Un score unique ne permet pas de distinguer ces échecs.

## Cinq vues du même problème

Barhdadi et ses collègues ont conçu cinq conditions qui conservent la cible du raisonnement tout en modifiant la qualité et la forme des éléments perceptifs. L'intervention essentielle fournissait aux modèles des descriptions exactes de la scène. Avec cet étayage, une grande partie de l'écart entre texte et image disparaissait. La même correction ne se produisait pas lorsque des analyseurs automatiques généraient les descriptions, même lorsque ces analyseurs comprenaient des modèles vision-langage de pointe.

Ce contraste situe l'obstacle immédiat. Les modèles pouvaient souvent utiliser un compte rendu symbolique exact de la scène pour déduire la croyance du personnage absent. Ils échouaient lorsqu'ils devaient produire eux-mêmes ce compte rendu à partir des pixels. Améliorer le prompt de la question finale ne permettrait pas de récupérer les informations déjà manquées ou déformées par le traitement visuel initial.

Le profil des erreurs appuie la même conclusion. Soixante pour cent des échecs de fausse croyance présentaient un biais de réalité : le modèle donnait l'emplacement réel de l'objet au lieu de celui dont le personnage absent se souviendrait. Cela ressemble à une incapacité à maintenir deux représentations distinctes. L'une décrit la scène actuelle ; l'autre décrit la scène que le personnage a observée pour la dernière fois.

Le biais de réalité peut ressembler à un défaut de raisonnement social, car la réponse finale ignore le point de vue du personnage. Les conditions contrôlées montrent que le modèle n'a peut-être jamais construit de représentation utilisable de ce point de vue. Si un analyseur affirme qu'un personnage a vu le déplacement, ou manque le moment de son départ, l'étape de raisonnement ultérieure reçoit le mauvais problème.

L'étayage par des descriptions exactes utilisé par les auteurs est un outil de diagnostic plutôt qu'une solution déployable. Les systèmes réels reçoivent rarement des descriptions parfaites des scènes. Un assistant qui observe un lieu de travail, un robot qui agit au milieu de personnes ou un système de tutorat qui suit une démonstration doit déterminer les événements auxquels chacun a assisté. Ces systèmes ne peuvent pas supposer qu'un humain a déjà converti la vidéo en faits précisément pertinents.

## Un benchmark pour la frontière

Des benchmarks antérieurs de théorie de l'esprit visuelle montraient déjà que les systèmes multimodaux peinent face aux intentions, aux croyances et aux présentations trompeuses. Le nouveau protocole ajoute une séparation plus nette entre voir et inférer. Il demande si le modèle peut résoudre le problème de raisonnement lorsque la perception est maintenue constante, puis mesure ce qui se passe lorsque l'appui perceptif change.

Cette séparation compte pour l'ingénierie. Une équipe constatant une erreur de fausse croyance pourrait ajouter des traces de raisonnement plus longues ou un modèle de langage plus grand. L'étude suggère un autre premier test : donner au système une représentation vérifiée de la scène. Si la réponse devient correcte, les travaux devraient porter sur le suivi des objets, l'analyse des événements et une mémoire propre à chaque point de vue. Si l'erreur persiste, c'est le composant de raisonnement sur les croyances qui mérite l'attention.

Le résultat limite aussi les affirmations générales sur l'intelligence sociale des machines. Les benchmarks textuels peuvent établir qu'un modèle associe un scénario écrit à une réponse attendue. Ils ne prouvent pas que le système peut reconstituer le scénario pertinent à partir d'un monde physique changeant. Un modèle qui traite de la croyance d'autrui après avoir lu un paragraphe clair n'a accompli que la seconde moitié du travail.

L'article fournit du code et des données, ce qui permet d'étendre ses conditions expérimentales. La comparaison rapportée de sept modèles reste un test de laboratoire circonscrit. Elle ne mesure ni tous les modèles visuels, ni tous les types d'inférence sociale, ni les performances sur des vidéos non contrôlées. La prépublication n'a pas été évaluée par les pairs dans une revue, même si son acceptation dans une section de conférence lui donne un cadre formel.

Retour à l'enfant et à la balle de l'exemple. Un ingénieur donne une ligne supplémentaire au modèle : le premier personnage est parti avant le déplacement de la balle. Le modèle prédit désormais le tiroir. Son raisonnement paraît meilleur, alors que son mécanisme de raisonnement n'a peut-être pas changé du tout. La pièce manquante était l'événement que le modèle n'avait pas vu.

## Références

- Barhdadi, M. R., Wasim, S. T., Gall, J., Serpedin, E., & Kurban, H. (2026). *Perception, Not Reasoning, Limits Visual Theory of Mind*. https://arxiv.org/abs/2611.10694
- Kosinski, M. (2024). *Evaluating large language models in theory of mind tasks*. https://doi.org/10.1073/pnas.2405460121
- Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). *Testing theory of mind in large language models and humans*. https://doi.org/10.1038/s41562-024-01882-z

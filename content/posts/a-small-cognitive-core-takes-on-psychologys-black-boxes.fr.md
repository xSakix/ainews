+++
title = "Un petit noyau cognitif défie les boîtes noires de la psychologie"
slug = "petit-noyau-cognitif-defie-boites-noires-psychologie"
description = "Deux chercheurs ont réuni quelques idées établies sur la mémoire, le contexte et l'erreur de prédiction dans un modèle de choix humain. CORE a surpassé des prédicteurs neuronaux comparables sur 137 expériences tout en gardant son fonctionnement interne inspectable."
tags = ["research", "models"]
date = 2026-10-14T04:02:33+02:00
draft = false
+++

Imaginons une participante assise seule dans un laboratoire de psychologie. Un symbole apparaît, puis un autre. Elle devine quelle porte cache une récompense, se souvient de la dernière surprise et change lentement de stratégie. Cette participante est inventée, mais chacun de ces petits actes appartient aux observations expérimentales derrière un nouveau modèle qui tente d'expliquer des millions de tels choix sans cacher l'explication dans un réseau neuronal.

## De nombreuses expériences, une seule explication

Marcel Binz et Eric Schulz, de l'Institute for Human-Centered AI à Helmholtz Munich, ont construit COntextual Retrieval and Encoding, ou CORE. Leur prépublication réunit un petit ensemble de principes cognitifs établis dans un modèle computationnel unique, puis l'ajuste conjointement à 7 036 442 choix humains issus de 137 expériences et de 80 452 sessions expérimentales.

L'ambition dépasse la prédiction d'une tâche. La psychologie a accumulé des explications de l'association, de l'erreur de prédiction, de la représentation hiérarchique, de la récupération des souvenirs et de l'oubli, souvent testées dans des traditions expérimentales distinctes. CORE demande quelle part des observations comportementales ces idées peuvent expliquer lorsqu'elles doivent fonctionner ensemble avec un même ensemble de mécanismes.

Sa structure est une hiérarchie de souvenirs épisodiques. Les erreurs de prédiction sont inscrites dans ces souvenirs. Le contexte gouverne ce qui est encodé, les souvenirs récupérés et leur effacement. Ces opérations sont exprimées comme des composants dont un chercheur peut inspecter les rôles plutôt que comme un modèle séquentiel sans restrictions entraîné uniquement à minimiser l'erreur.

Les auteurs comparent CORE à un transformer de configuration comparable et à Centaur, un modèle de fondation de la cognition humaine présenté par une vaste collaboration dirigée par Binz. Centaur a affiné un modèle de langage sur Psych-101, un jeu de données couvrant plus de dix millions de choix dans 160 expériences. Il a démontré qu'un grand système prédictif unique pouvait généraliser à travers les scénarios narratifs, les modifications de tâches et les domaines inconnus. Il a aussi soulevé le coût familier des modèles de fondation : la prédiction est devenue large, tandis que le mécanisme appris restait difficile à formuler comme une théorie psychologique.

CORE inverse ce compromis. Dans le nouvel article, il obtient une log-vraisemblance négative prédictive inférieure à celle du transformer comparable, 262 572 contre 329 043. Face à Centaur, la comparaison est de 262 572 contre 389 151. CORE fait mieux que le transformer dans les 62 études utilisées pour cette comparaison à l'échelle des études, et mieux que Centaur dans 47.

Ces chiffres ne signifient pas que CORE a saisi l'esprit humain. Ils comparent des prédictions dans un corpus expérimental assemblé particulier. Ils montrent néanmoins qu'un modèle interprétable n'a pas été contraint de sacrifier sa portée prédictive simplement parce que ses parties avaient une signification psychologique.

## Ce dont le modèle se souvient

La hiérarchie compte parce qu'un choix peut dépendre d'événements à différentes échelles. Une erreur récente peut changer la réponse suivante. Une série d'essais liés peut établir une situation locale. Un changement dans l'expérience peut rendre les expériences anciennes moins pertinentes même lorsqu'elles restent stockées.

CORE traite ces effets grâce à un encodage et une récupération sensibles au contexte. Les erreurs de prédiction mettent à jour la mémoire au lieu de simplement modifier une estimation unique de valeur. Le modèle peut récupérer un épisode lorsque la situation actuelle lui ressemble, tandis que son processus d'oubli réduit le poids de l'expérience à mesure que le contexte s'en éloigne.

Cette conception produit des traces internes familières aux théories établies. Les auteurs rapportent des signatures d'apprentissage bayésien dans les variables latentes de CORE : ses mises à jour répondent à l'incertitude de façons associées à l'inférence probabiliste. Ils trouvent aussi des signatures de segmentation des événements, ce qui signifie que l'organisation interne du modèle reflète les frontières entre situations plutôt que de traiter le flux entier comme uniforme.

Le résultat prolonge un programme de recherche que les mêmes auteurs ont poursuivi dans la direction opposée. En 2023, Binz et Schulz ont montré que des modèles de langage affinés sur des expériences de psychologie pouvaient surpasser les modèles cognitifs traditionnels dans deux domaines de décision et porter des informations sur les participants individuels. Leur travail sur la cognition méta-apprise soutenait que les algorithmes d'apprentissage pouvaient approcher un comportement bayésien optimal tout en intégrant un calcul limité et d'autres contraintes réalistes.

Ces systèmes demandaient jusqu'où les outils généraux de l'apprentissage automatique pouvaient aller vers le comportement humain. CORE demande jusqu'où une théorie psychologique compacte peut aller vers la portée prédictive de l'apprentissage automatique. Les deux directions se rejoignent désormais sur une partie des mêmes données.

## Reproduire les effets plutôt que les nommer

La prédiction n'est qu'une partie du test. Les auteurs simulent CORE dans les conditions expérimentales et demandent s'il reproduit les effets comportementaux rapportés par les études. Il en retrouve 75 %.

C'est une exigence plus stricte que de reproduire une fréquence moyenne de choix. Un effet peut concerner l'adaptation, un biais, l'ordre, l'incertitude ou un changement après une frontière contextuelle. Le reproduire exige que le comportement du modèle évolue dans la direction pertinente lorsque la manipulation expérimentale change.

Le quart manquant compte autant que les trois quarts réussis. Un modèle unifié devient scientifiquement utile lorsque ses échecs identifient où le noyau proposé est incomplet. Un prédicteur boîte noire peut absorber un motif supplémentaire sans dire aux chercheurs quelle théorie a changé. Un système interprétable impose un choix plus clair : réviser la récupération, ajouter un mécanisme, modifier la hiérarchie ou accepter que le phénomène sorte du cadre de l'explication.

L'étendue de l'article crée aussi des risques. Les expériences diffèrent par leurs instructions, formats de réponse, populations de participants et conventions analytiques. L'ajustement conjoint peut favoriser les mécanismes qui expliquent les structures communes tout en gommant les structures inhabituelles. Une vraisemblance totale peut masquer une faible explication d'un domaine petit mais important. Les auteurs rapportent donc des comparaisons à l'échelle des études et des effets simulés, pas seulement une note agrégée.

CORE est aussi une prépublication. Ses affirmations, choix d'implémentation et harmonisation des jeux de données n'ont pas achevé l'évaluation par les pairs. Le corpus est vaste selon les critères de la psychologie expérimentale, mais reste un ensemble sélectionné de tâches qui peuvent être représentées et ajustées ensemble. La vie humaine hors du laboratoire comprend le langage, les relations sociales, l'émotion et l'action incarnée qui ne sont pas comprimés dans sept millions de choix discrets.

## Une théorie qui peut se tromper

La principale contribution du modèle pourrait être méthodologique. Les sciences cognitives ont souvent dû choisir entre un modèle transparent expliquant un paradigme et un prédicteur général disant peu de choses sur le mécanisme. CORE apporte des preuves que cette frontière peut bouger.

Cela n'élimine pas les modèles neuronaux ou de fondation. Centaur établit une référence prédictive solide et peut généraliser à travers des descriptions de tâches en langage naturel. Un modèle compact peut utiliser de tels systèmes comme rivaux, générateurs de données ou outils de découverte. La distinction importante est l'affirmation que chacun étaye. Un prédicteur montre que le comportement peut être anticipé. Une théorie cognitive énonce les opérations qui, selon elle, l'ont produit.

Parce que CORE énonce ces opérations, les chercheurs peuvent intervenir sur elles. Ils peuvent supprimer l'oubli contextuel, aplatir la hiérarchie de mémoire ou changer la manière d'inscrire les erreurs de prédiction, puis identifier quelles expériences échouent. Ils peuvent aussi ajouter un principe proposé et tester s'il mérite sa place sur l'ensemble des observations plutôt que d'améliorer une tâche choisie à la main.

Revenons à la participante imaginée face à deux portes. Son prochain choix peut désormais être prédit par un grand modèle opaque ou reconstruit à travers un souvenir de surprises, organisé par contexte et autorisé à s'effacer. Le premier peut avoir raison. Le second donne au scientifique autre chose : une explication précise que l'expérience suivante peut réfuter.

## Références

- Binz, M., Dasgupta, I., Jagadish, A., Botvinick, M., Wang, J. X., & Schulz, E. (2023). *Meta-Learned Models of Cognition*. https://arxiv.org/abs/2304.06729
- Binz, M., et al. (2024). *Centaur: a foundation model of human cognition*. https://arxiv.org/abs/2410.20268
- Binz, M., & Schulz, E. (2023). *Turning large language models into cognitive models*. https://arxiv.org/abs/2306.03917
- Binz, M., & Schulz, E. (2026). *A small cognitive core explains human behavior at scale*. https://arxiv.org/abs/2610.13603

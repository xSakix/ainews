+++
title = "Une sonde linéaire a trouvé une caractéristique inutilisée par Llama"
slug = "sonde-lineaire-trouve-caracteristique-inutilisee-par-llama"
description = "Une sonde linéaire pouvait lire les années de naissance de personnes dans Llama-2-7B, mais modifier la direction trouvée changeait à peine la réponse du modèle. Une nouvelle étude relie cet échec aux directions d'activation peu variables et montre comment la régularisation permet de repérer une caractéristique plus fidèle causalement."
tags = ["research", "models"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

Un chercheur a saisi le nom d'une personne née dans les années 1930, puis a emprunté un signal interne provenant d'une personne née cinquante ans plus tard. La sonde affirmait savoir où le modèle stockait l'année. Le modèle a poursuivi comme si rien n'avait changé.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

Cette modification ratée est au cœur d'une prépublication (preprint) de Karl Vilhelmsson Emneby, Julian Yocum et Cameron Allen. Leur résultat trace une frontière nette entre une information que l'on peut lire dans un réseau de neurones et une information que le réseau utilise réellement. Une sonde linéaire ordinaire parvenait à prédire des années de naissance à partir des activations de Llama-2-7B, mais une intervention selon la direction choisie n'apportait pas davantage de contrôle que de laisser le modèle intact. Une sonde régularisée a cédé un peu de précision prédictive pour trouver une direction qui modifiait effectivement la sortie.

## Lire n'est pas utiliser

Une sonde linéaire est volontairement simple. Les chercheurs recueillent les activations internes d'un modèle, leur associent des étiquettes et ajustent une application linéaire de l'une vers l'autre. Si cette application prédit une propriété telle que le sentiment, le lieu ou l'année de naissance, cette propriété est linéairement décodable dans la couche considérée.

Cette technique a fait des sondes un instrument courant d'interprétabilité. Leur simplicité semble borner ce qu'elles peuvent découvrir. Une lecture linéaire réussie peut donner l'impression d'offrir une fenêtre limpide sur le calcul interne d'un modèle.

Cette déduction a toujours comporté une mise en garde. Une représentation peut contenir un signal que les couches suivantes ignorent. Elle peut aussi renfermer un corrélat qui prédit l'étiquette du chercheur sans jouer le rôle que celui-ci lui attribue. Le nouvel article pose une question plus ciblée : pourquoi la sonde de régression la plus précise peut-elle trouver une direction particulièrement mauvaise pour intervenir, et une pénalité statistique classique peut-elle aider ?

Les auteurs définissent la fidélité d'intervention par un échange. On prélève une activation issue d'une entrée de base et on remplace sa composante selon la direction de caractéristique proposée par celle d'une entrée source. Si la direction porte bien la variable revendiquée, la sortie du modèle doit se déplacer vers la valeur associée à la source. L'erreur de prédiction indique si une sonde sait lire la variable. L'erreur d'intervention indique si modifier cette lecture fait évoluer le modèle dans le sens attendu.

Ce sont deux tests distincts.

## Un processus caché à la réponse connue

La première expérience repose sur Mess3, un processus de Markov caché à trois états latents. Un petit transformeur à quatre couches d'une largeur de 64 apprend à prédire le symbole suivant du processus. Comme le processus est spécifié avec exactitude, les chercheurs peuvent calculer l'état de croyance correct après chaque séquence d'entrée ainsi que la sortie qui doit suivre une intervention.

Ce cadre prolonge les travaux d'Adam Shai et de ses collègues. Ceux-ci ont montré que le flux résiduel d'un transformeur peut restituer la géométrie des états de croyance de processus cachés, y compris la structure complexe de Mess3. Leur régression linéaire reconstruisait cette géométrie à partir des activations. La nouvelle étude examine si les directions ainsi extraites commandent également la prédiction du transformeur.

La méthode des moindres carrés ordinaires s'est révélée performante en lecture et médiocre en contrôle. La raison tient à la division au cœur de la régression. Dans la base formée par les composantes principales de l'espace d'activation, le poids attribué à chaque composante dépend de sa covariance avec la cible divisée par sa variance. Une composante très peu variable peut ainsi recevoir un poids considérable à partir d'une faible covariance.

Le résultat sur Mess3 rend cet effet tangible. Une composante présentant une variance proche de 10 puissance moins 18 concentrait 91,5 % du poids quadratique de la sonde non régularisée. La sonde s'était focalisée sur une direction qui variait à peine. Elle pouvait exploiter cette direction pour réduire sa propre erreur d'ajustement, mais permuter cette direction ne produisait pas le changement voulu dans la sortie du transformeur.

La régression ridge modifie le diviseur en ajoutant une pénalité. Cela écrase les poids élevés que les moindres carrés ordinaires attribuent aux composantes de faible variance. À mesure que la pénalité augmentait, la fidélité d'intervention s'est d'abord améliorée avant, dans l'expérience sur le modèle de langage, de décliner. La régularisation n'a pas transformé n'importe quelle direction forte en caractéristique causale ; elle a modifié les indices privilégiés par la sonde.

## Des années de naissance dans Llama

La deuxième expérience passe d'un petit système à solution exacte à Llama-2-7B. Elle prolonge des travaux antérieurs de Benjamin Heinzerling et Kentaro Inui, qui avaient identifié des directions encodant de façon monotone des attributs numériques. Leurs interventions pouvaient amener un modèle de langage à produire des années de naissance plus anciennes ou plus récentes.

Emneby et ses collègues ont utilisé 8 000 prompts (instructions) portant sur des personnes nées entre 1900 et 1999. Ils ont ajusté des sondes sur le flux résiduel au dernier token du nom de la personne dans la couche huit. Pour chaque intervention, ils ont déplacé l'activation de base le long d'une direction proposée vers l'activation d'une personne source. Ils ont ensuite mesuré la décennie attendue à partir de la probabilité attribuée par le modèle aux dix chiffres de décennie possibles.

La sonde non régularisée affichait la meilleure perte de prédiction sur l'échantillon, à 0,0671. Sa perte d'intervention s'élevait à 13,7, soit exactement le résultat obtenu sans aucune intervention. La direction était lisible et inerte.

Une sonde ridge dotée d'une pénalité de 10 000 présentait une perte de prédiction moins bonne, à 0,251, mais réduisait la perte d'intervention à 7,07. Distributed Alignment Search, une méthode développée par Atticus Geiger et ses collègues pour apprendre des représentations directement à partir d'interventions causales, atteignait 6,42. La direction ridge se situait à 26,3 degrés de celle trouvée par la méthode entraînée par interventions. La sonde ordinaire en était éloignée de 84,7 degrés.

La direction régularisée ne correspondait pas simplement à l'axe le plus ample de l'espace d'activation. Sa variance valait 3,83, tandis que la première composante principale avait une variance de 25 570. La régression ridge ignorait largement cette composante dominante. La zone utile se trouvait entre les corrélations discrètes amplifiées par la régression ordinaire et le mouvement de plus grande amplitude dans la couche.

## Un test, pas une garantie

L'article fournit un mécanisme expliquant un type d'échec des sondes ainsi qu'une réponse pratique. Lorsque l'objectif est d'identifier une caractéristique que le modèle utilise activement, les chercheurs peuvent ajuster des sondes sur toute une gamme de pénalités et choisir parmi elles à l'aide d'interventions réservées au test. Un score de décodage élevé répond seulement à la question de savoir si l'information est accessible à une lecture.

Les preuves comportent des limites strictes. La théorie couvre la régression à cibles continues, alors que de nombreuses sondes emploient des classifieurs logistiques. Le résultat sur le modèle de langage provient d'une seule couche d'un seul modèle et d'une unique propriété numérique. Même la meilleure sonde ridge laissait subsister une erreur d'intervention notable. Les mathématiques expliquent comment les moindres carrés ordinaires peuvent amplifier des directions discrètes ; elles ne prouvent pas que la régression ridge trouvera une direction causale.

La comparaison avec Distributed Alignment Search comporte également une asymétrie importante. Cette méthode apprend à partir des résultats d'intervention, tandis que les sondes ridge continuent d'apprendre à partir de la décodabilité. Les données d'intervention servent uniquement à choisir la pénalité une fois les sondes ajustées. Leur proximité montre que la régularisation peut orienter une sonde prédictive vers une direction utile causalement dans ces expériences, sans pour autant rendre les deux objectifs identiques.

Devant son poste de travail, le chercheur a retenté l'échange. Cette fois, la sonde était moins certaine de l'année de naissance qu'elle avait lue. La décennie produite par le modèle s'est déplacée.

## Références

- Emneby, K. V., Yocum, J., & Allen, C. (2026). *Pretty Linear Liars: Unregularized Probes Favor Intervention-Unfaithful Features*. https://arxiv.org/abs/2611.20371
- Geiger, A., Wu, Z., Potts, C., Icard, T., & Goodman, N. (2024). *Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations*. https://proceedings.mlr.press/v236/geiger24a.html
- Heinzerling, B., & Inui, K. (2024). *Monotonic Representation of Numeric Attributes in Language Models*. https://aclanthology.org/2024.acl-short.18/
- Shai, A. S., Marzen, S. E., Teixeira, L., Gietelink Oldenziel, A., & Riechers, P. M. (2024). *Transformers Represent Belief State Geometry in Their Residual Stream*. https://arxiv.org/abs/2405.15943

+++
title = "4MT-VLM : les modèles visuels perdent les lieux après rotation"
slug = "4mt-vlm-modeles-visuels-perdent-lieux-apres-rotation"
description = "Une prépublication adapte un test clinique de mémoire spatiale à 16 modèles vision-langage. Tous reconnaissent un paysage sous l'angle étudié, mais la plupart en sont réduits à deviner quand la caméra bouge."
tags = ["research", "models"]
date = 2026-10-06T04:02:31+02:00
draft = false
+++

Les modèles vision-langage reconnaissent un paysage sous l'angle où ils l'ont vu pour la première fois, mais la plupart ne peuvent plus l'identifier quand la caméra bouge, selon 4MT-VLM, un nouveau benchmark adapté d'un test clinique de mémoire spatiale.

Markus Frey, de Fraunhofer IAIS, un institut allemand de recherche appliquée, a soumis 16 modèles ouverts et fermés à l'épreuve utilisée chez les patients humains : étudier un paysage de quatre sommets rendu par ordinateur, puis le retrouver parmi quatre paysages similaires présentés sous un nouvel angle. Un volontaire humain a résolu environ quatre essais avec rotation sur cinq. La plupart des modèles n'ont pas fait mieux que le hasard.

## Pourquoi c'est important {#why-it-matters}

Un ingénieur en robotique qui utilise un modèle vision-langage comme yeux d'un robot mobile a précisément besoin de cette compétence : reconnaître une pièce après que le robot s'est retourné. La prépublication constate que ni des modèles plus grands ni des instructions plus détaillées ne la procurent.

## La reconnaissance tient, la rotation échoue

Le benchmark adapte le Four Mountains Test, utilisé par les cliniciens parce que les scores diminuent en cas de lésion de l'hippocampe et au début de la maladie d'Alzheimer. Couleurs, textures et éclairage changent entre l'image étudiée et les images de test à chaque essai : même sans rotation, comparer les pixels ne suffit donc pas. Frey utilise la précision sur ces essais sans rotation pour vérifier qu'un modèle peut au moins identifier le lieu.

Les modèles réussissent cette vérification, puis échouent avec la rotation. GPT-5.6 Luna d'OpenAI a répondu correctement à tous les essais sans rotation, mais à seulement 31 % de ceux avec rotation, où le hasard donne une bonne réponse sur quatre. Sur l'ensemble des 16 modèles, le pire angle était de 135 degrés, avec une précision nettement inférieure au hasard.

Un demi-tour de 180 degrés, le changement le plus important, a donné de meilleurs scores qu'une rotation de 135 degrés. Frey y voit le signe que les modèles utilisent un raccourci visuel, comme la comparaison avec une image en miroir de la scène, plutôt que de faire tourner une carte interne. La comparaison humaine repose sur un seul participant : assez pour montrer que la tâche est réalisable, mais pas pour établir une moyenne humaine.

## Les grands modèles reconnaissent mieux, sans mieux gérer la rotation

L'échelle a amélioré la reconnaissance, sans changer les résultats avec rotation. Dans la famille Qwen2.5-VL d'Alibaba, de 3 à 72 milliards de paramètres, la précision sans rotation est passée de 30 à 75 %, tandis que celle avec rotation restait au niveau du hasard ou en dessous. La famille InternVL3.5 a reproduit ce schéma de 1 à 38 milliards de paramètres. Parmi 14 modèles à poids ouverts allant jusqu'à 235 milliards de paramètres, aucun n'a répondu correctement à plus de 31 % des essais avec rotation, et une variante « pensante » a obtenu le même score que sa version standard.

Les instructions n'ont pas comblé l'écart. Frey a testé Qwen2.5-VL-32B avec six prompts, dont des procédures explicites : imaginer la disposition vue directement d'en haut ou prendre le sommet le plus distinctif comme repère. Les six l'ont laissé sous le niveau du hasard.

## Éloigner les mauvaises réponses révèle une carte grossière

L'expérience la plus instructive n'a changé que les mauvaises réponses. Frey a mesuré, en mètres, la distance entre les sommets de deux paysages après la meilleure rotation possible, puis a redessiné les trois leurres avec des dispositions plus éloignées, tout en gardant la cible et les angles identiques.

Éloigner le leurre le plus proche d'environ 7 mètres à environ 31 mètres a fait passer Gemini 3.8 Flash de Google de 39 à 85 % sur les essais avec rotation, et GPT-5.6 Luna de 31 à 55 %. Aucun modèle ouvert n'a progressé de façon statistiquement significative.

C'est l'élément sur lequel l'article s'appuie pour conclure que les modèles de pointe conservent une certaine perception de la disposition, mais à faible résolution. Un modèle sans carte ne pourrait pas profiter de l'éloignement des leurres, et un modèle doté d'une carte de niveau humain n'aurait pas besoin de 30 mètres de séparation. L'effet ressemble à la reconnaissance d'une ville depuis le hublot d'un avion, sans pouvoir reconnaître une rue.

Les erreurs vont dans le même sens. Une personne qui se trompe tend à choisir le leurre dont la disposition est la plus proche de la cible. Les mauvaises réponses des modèles étaient réparties presque uniformément entre leurres proches et éloignés, comme si la disposition ne jouait aucun rôle dans le choix.

## Un test synthétique signé par un seul auteur

Les paysages sont des rendus synthétiques, et Frey note qu'un préentraînement sur des scènes rendues similaires pourrait favoriser certains modèles. Le nombre de paramètres des modèles fermés n'est pas divulgué : les observations sur l'échelle reposent donc uniquement sur les modèles ouverts. La prépublication, déposée sur arXiv le 30 septembre 2026, a un seul auteur et ne donne aucun lien vers du code ou un jeu de données.

Frey indique que davantage de participants humains sont en cours de test, ce qui donnera un véritable groupe de comparaison au score de 82 % du volontaire sur les essais avec rotation.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| 4MT-VLM adapte le Four Mountains Test ; 500 essais sur 100 paysages générés, 16 modèles testés | VÉRIFIÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune ; benchmark de l'auteur |
| L'apparence est rééchantillonnée entre les images d'étude et de test à chaque angle | VÉRIFIÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune ; description de la méthode |
| Un participant humain a répondu correctement à 100 % des essais sans rotation et à 82 % avec rotation | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune ; un seul participant |
| GPT-5.6 Luna : 100 % sans rotation, 31 % avec rotation ; le hasard est à 25 % | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |
| La précision agrégée à 135 degrés est de 15,0 % (48/320), sous le hasard ; 23 % à 180 degrés | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |
| Les modèles utilisent un raccourci visuel comme la correspondance avec une image en miroir | ANALYSE | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | interprétation par l'auteur du schéma à 135/180 degrés |
| Qwen2.5-VL de 3B à 72B : de 30 % à 75 % sans rotation ; 29 %, 31 %, 18 %, 20 % avec rotation | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |
| Aucun modèle à poids ouverts (1B à 235B) ne dépasse 31 % avec rotation ; la variante pensante égale la version instruct à 19 % avec rotation | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |
| Six styles d'instructions laissent Qwen2.5-VL-32B entre 13,8 % et 23,8 %, tous sous le hasard | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |
| Distance médiane du leurre le plus proche de 6,8 m à 31,4 m : Gemini 3.8 Flash de 39 % à 85 %, GPT-5.6 Luna de 31 % à 55 % | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |
| Aucun modèle ouvert ne change significativement avec un espacement accru des leurres | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |
| Les erreurs des modèles se répartissent à 30/37/33 entre les leurres le plus proche, intermédiaire et le plus éloigné ; l'humain a choisi le plus proche dans 10 erreurs sur 14 | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |
| Les modèles de pointe conservent une représentation grossière de la disposition | ANALYSE | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | déduction tirée du résultat sur l'espacement des leurres |
| Prépublication d'un seul auteur déposée le 30 septembre 2026 ; auteur à Fraunhofer IAIS ; aucun code ni données liés | VÉRIFIÉ | [Notice arXiv](https://arxiv.org/abs/2609.39238) | métadonnées arXiv et domaine de l'adresse électronique de l'auteur |
| Davantage de participants humains sont en cours d'évaluation | SELON LA SOCIÉTÉ | [Prépublication de Frey](https://arxiv.org/abs/2609.39238) | aucune |

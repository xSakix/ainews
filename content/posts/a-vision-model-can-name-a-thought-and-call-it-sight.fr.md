+++
title = "Un modèle visuel peut nommer une pensée et croire la voir"
slug = "modele-visuel-nommer-pensee-croire-voir"
description = "Des chercheurs ont injecté des concepts dans six modèles vision-langage et demandé à chacun de distinguer pensée et perception. Un modèle pouvait nommer le concept caché, mais son récit de sa provenance changeait avec le prompt, l’image et le point d’injection."
tags = ["research", "models", "safety"]
date = 2026-11-09T04:10:00+01:00
draft = false
+++

Sur un établi imaginaire, une chercheuse en interprétabilité montre à un modèle de vision un carré gris uni. À l'intérieur du modèle, elle ajoute une direction mathématique correspondant à « chien » pendant qu'il prépare sa réponse. L'écran ne contient aucun animal. Le modèle répond qu'un chien est visible. Cette chercheuse est fictive, mais l'intervention et l'erreur proviennent d'une nouvelle étude de l'University of Southern California.

## Un test avec deux sources possibles

Tina Khezresmaeilzadeh, Seyedarmin Azizi, Mehdi Kamal et Massoud Pedram ont demandé si un modèle vision-langage peut distinguer un contenu entrant par une image d'un contenu placé par les chercheurs dans ses activations. Les psychologues cognitivistes appellent la tâche humaine correspondante le contrôle de la réalité : déterminer si un souvenir vient de la perception ou d'une expérience produite intérieurement.

Cette distinction ajoute une contrainte à l'introspection des modèles. Un modèle textuel qui nomme correctement un concept injecté a passé un test. Un modèle vision-langage doit aussi dire si ce concept a été vu ou pensé. Un mot correct attribué à la mauvaise source peut devenir une fausse description d'image.

Les chercheurs ont testé six modèles issus de trois familles de modèles de langage. Leur principal sujet était Gemma-3-27B, qui associe un encodeur visuel SigLIP à un modèle de langage de 62 couches. Chaque essai utilisait soit une image neutre, soit l'image d'un objet. Les chercheurs ajoutaient parfois une direction conceptuelle, comme « chien » ou « avion », aux activations internes du modèle.

Le modèle devait remplir trois champs. Il nommait l'objet principal visible, indiquait si une pensée avait été injectée et nommait cette pensée. Le protocole permettait de distinguer plusieurs résultats qu'un score ordinaire de précision fusionnerait : détecter une perturbation, identifier son contenu et attribuer ce contenu à la bonne source.

## Un modèle a trouvé la pensée

Gemma-3-27B a produit le résultat entièrement correct dans 34,7 % des 150 essais conceptuels à la couche et à l'intensité choisies. Il signalait une injection, nommait le concept et ne prétendait pas que ce concept était visible. La correspondance exacte des mots donnait 31,3 %, contre 33,3 % pour un modèle évaluateur indépendant.

Le taux de fausses alertes était faible. Sur 972 essais sans injection, Gemma n'en a signalé une que trois fois. Des directions aléatoires n'ont produit aucune identification correcte. Sur 100 concepts non utilisés pour choisir les réglages de l'intervention, l'identification entièrement correcte atteignait 33 %. Le résultat ne dépendait donc pas seulement des concepts ayant servi à ajuster le test.

Le pilotage ordinaire constituait un contrôle plus exigeant. Les chercheurs appliquaient la même impulsion interne sans mentionner de pensées injectées. Ils demandaient l'objet visible et le premier mot venant à l'esprit. Gemma nommait exactement la cible dans 3,3 % de ces essais, bien en dessous du score d'introspection. Interroger le contenu interne changeait ce que le modèle pouvait rapporter.

Le résultat prolonge des travaux publiés par Jack Lindsey en 2025 sur des modèles Claude purement textuels. Cette étude injectait des représentations conceptuelles connues et montrait que les modèles les plus puissants pouvaient parfois identifier le contenu de l'intervention avec peu de fausses alertes. Des travaux antérieurs de Felix Binder et de ses collègues avaient abordé l'introspection par l'autoprédiction : un modèle apprenait à prédire son propre comportement mieux qu'un autre modèle ne le pouvait. L'expérience de l'USC a rendu l'événement interne contrôlable et ajouté la vision, où la source du contenu devient observable.

L'effet ne se généralisait pas nettement entre modèles. Qwen3-VL-8B signalait une injection dans 61,3 % de ses essais conceptuels, mais ne nommait exactement le concept que dans 3,3 %. Les autres modèles testés identifiaient peu de concepts, produisaient de nombreux faux signalements ou échouaient à la comparaison avec le pilotage. L'article établit donc un comportement dans une configuration de modèle, pas une propriété générale des systèmes vision-langage.

## L'attribution de source a cédé en premier

Même les signalements réussis de Gemma étaient fragiles. À l'intensité d'intervention retenue, il décrivait le concept injecté comme visible dans 22,7 % des essais avec image grise. Augmenter l'intensité portait cette attribution visuelle erronée à 51 %.

De petites modifications de la question changeaient aussi la réponse. Retirer une phrase qui distinguait explicitement la pensée injectée de l'image faisait passer l'introspection entièrement correcte de 34,7 % à 10 % et les déclarations de visibilité du concept de 23 % à 65 %. Demander si une injection avait eu lieu avant de demander ce qui était visible réduisait à zéro l'introspection entièrement correcte dans la configuration testée.

Le point d'entrée comptait également. Lorsque les chercheurs injectaient une direction conceptuelle visuelle aux positions des tokens d'image, Gemma la traitait souvent comme une perception. À la couche 21 du modèle de langage, il déclarait le concept cible visible dans 47 à 49 % des essais et ne qualifiait presque jamais le contenu d'injecté. Des perturbations aléatoires aux mêmes positions suscitaient des signalements d'anomalie sans produire de concept cohérent. Le modèle pouvait remarquer quelque chose d'inhabituel tout en acceptant un contenu significatif comme faisant partie de l'image.

Un objet réel créait un autre problème. Quand Gemma recevait une image contenant un objet sans rapport, l'identification entièrement correcte de la pensée injectée passait de 34,7 % à 2,7 %. Le modèle conservait certaines informations sur le concept, mais les éléments visuels changeaient le fait de les rapporter et l'endroit où il les rapportait.

Ces échecs ressemblent à un problème décrit par Marcia Johnson et Carol Raye dans leurs recherches sur la mémoire humaine en 1981. Leur cadre de contrôle de la réalité traite les jugements de source comme des inférences à partir des caractéristiques d'une expérience, plutôt que comme des étiquettes parfaites attachées aux souvenirs. L'article de l'USC ne prétend pas qu'un transformer utilise le mécanisme humain. Il emprunte la distinction parce que l'expérience exige aussi de séparer un contenu externe d'un contenu produit intérieurement.

## D'une impulsion interne à une fausse légende

Les chercheurs ont ensuite supprimé toute mention de pensées injectées et demandé à Gemma de décrire 108 photographies du jeu COCO. Chaque photographie était associée à un objet cible absent selon ses annotations.

Sans intervention, aucune légende ne mentionnait la cible. Une direction aléatoire et un concept sans rapport n'en produisaient pas non plus. Injecter la cible aux positions de réponse la faisait apparaître dans 5 % des légendes à faible intensité et 42 % à forte intensité. Ajouter une direction conceptuelle visuelle aux tokens d'image amenait 87 % des légendes à mentionner l'objet absent.

Les questions oui-non étaient moins sensibles. Sans injection, Gemma répondait à tort que l'objet absent était présent dans 7 % des photographies. Les interventions portaient le taux à 12–19 %, mais les directions aléatoires et sans rapport produisaient des changements similaires. Le résultat des légendes suivait bien plus précisément le concept lui-même.

Ce contraste relie ces travaux à la recherche sur les hallucinations d'objets. Yifan Li et ses collègues ont introduit l'évaluation POPE en 2023 après avoir constaté que les modèles vision-langage décrivent des objets absents, surtout ceux fréquents dans leurs données d'instructions ou aux côtés d'objets présents. Le nouvel article ne montre pas que les hallucinations naturelles empruntent la même voie interne. Son injection conceptuelle est artificielle. Il montre une voie possible et avertit d'une limite de mesure : une brève question factuelle peut manquer un concept qui apparaîtra dans une description libre.

Les limites sont importantes. L'analyse approfondie des interventions concerne Gemma-3-27B, l'ensemble de concepts se compose de noms concrets et une personne a audité l'échantillon de notation. La formulation des prompts changeait fortement les résultats. Les taux mesurés décrivent des modifications contrôlées d'activations, pas le fonctionnement ordinaire des modèles ni une expérience consciente.

La conclusion pratique est plus restreinte et plus utile. Les évaluateurs devraient noter à la fois ce qu'un modèle multimodal rapporte et l'origine qu'il attribue au contenu. Un système peut détecter un état caché sans fournir un récit fiable de sa provenance.

Retrouvons la chercheuse fictive devant le carré gris. Elle relance l'essai, mais interroge maintenant l'injection avant l'image. Le concept n'a pas changé, l'écran non plus. La réponse, si. Son carnet doit comporter des colonnes distinctes pour le mot, la source et la question exacte, car une seule coche « correct » masquerait l'échec.

## Références

- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. https://arxiv.org/abs/2410.13787
- Johnson, M. K., & Raye, C. L. (1981). *Reality Monitoring*. https://doi.org/10.1037/0033-295X.88.1.67
- Khezresmaeilzadeh, T., Azizi, S., Kamal, M., & Pedram, M. (2026). *Did I See It or Think It? Probing Reality Monitoring in Vision-Language Models with Concept Injection*. https://arxiv.org/abs/2611.09014
- Li, Y., Du, Y., Zhou, K., Wang, J., Zhao, W. X., & Wen, J. R. (2023). *Evaluating Object Hallucination in Large Vision-Language Models*. https://aclanthology.org/2023.emnlp-main.20/
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://arxiv.org/abs/2601.01828

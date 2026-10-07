+++
title = "Zou étudie comment les modèles signalent des changements internes"
slug = "zou-modeles-signalent-changements-internes"
description = "Une prépublication contrôlée distingue la détection d'un changement d'activation du signalement de sa position. L'expérience utilise un texte d'entrée fixe et évalue les réponses sans juge IA."
tags = ["research", "safety"]
date = 2026-10-04T09:26:37+02:00
draft = false
+++

L'équipe de Jiahong Zou a identifié deux groupes de têtes d'attention qui aident les modèles de langage à signaler un changement interne délibérément injecté : l'un contrôle le signalement, l'autre aide à localiser le changement.

La prépublication, soumise le 28 septembre, étudie une forme restreinte d'introspection. Les chercheurs modifient les activations cachées d'un modèle tout en conservant un prompt visible identique, puis lui demandent de nommer la position touchée ou d'indiquer que rien n'a changé.

Pour les ingénieurs qui étudient le pilotage des activations, ce résultat indique un endroit concret où chercher si un modèle a enregistré l'intervention. Ce pilotage modifie les représentations internes d'un modèle pour influencer sa sortie ; l'expérience examine le mécanisme qui transforme un tel changement en signalement explicite.

Zou et ses coauteurs indiquent des affiliations à Shandong University, Tsinghua University, Northeastern University et à University of Hong Kong. Ils testent des modèles des familles Qwen, Llama et Gemma affinés pour suivre des instructions, en calculant directement les évaluations à partir des scores de sortie des modèles plutôt qu'en les confiant à un modèle de langage distinct.

Chaque prompt contient dix positions de tokens candidates. Un vecteur de concept injecté modifie l'état caché à une position, ou une exécution de comparaison sans intervention ne change rien. Le vecteur est construit à partir de la différence entre les activations suscitées par un concept et une moyenne calculée sur des mots du vocabulaire.

Le modèle choisit entre des labels de position et une réponse indiquant l'absence de changement. L'évaluation utilise la première position de sortie, avant qu'un texte explicatif généré ne puisse fournir des indices supplémentaires. Les chercheurs alternent également chiffres, lettres et mots pour les labels, et mélangent leur ordre afin de vérifier si une association fixe avec un label explique la réussite.

Les trois modèles localisent les changements mieux que la référence aléatoire de position de l'article, mais les résultats dépendent fortement du format des labels. Les auteurs choisissent les réglages d'injection sur des données de calibration distinctes et retiennent les concepts qui y fonctionnent le mieux. Leur test mesure donc les performances au sein d'un ensemble de concepts présélectionnés, plutôt que la sensibilité à n'importe quel changement interne.

## Détecter un changement et nommer sa position sont dissociables

La preuve centrale repose sur le remplacement des sorties de certaines têtes d'attention par celles d'une exécution appariée. Une tête d'attention déplace l'information entre les positions des tokens ; remplacer sa sortie permet aux chercheurs de tester sa contribution à la réponse.

Les têtes des couches intermédiaires influencent le fait qu'une position soit signalée ou non. Les auteurs les appellent têtes de contrôle. Un petit groupe situé dans une couche ultérieure aide à choisir la position à signaler, d'où le nom de têtes de routage.

Intervenir sur les têtes de contrôle peut supprimer le signalement d'une position même lorsque les têtes de routage conservent des informations sur sa localisation. À l'inverse, remplacer les sorties de routage par celles d'une exécution sans intervention réduit la précision de localisation. Rediriger leur attention aide à tester le lien entre l'endroit où elles regardent et la position choisie.

Cette séparation constitue le résultat le plus solide de l'article. Les informations sur une intervention peuvent rester dans le modèle alors que la réponse n'en signale aucune. Le signalement verbal d'un modèle est donc l'aboutissement d'un mécanisme de signalement précis, et non un inventaire complet des informations de son état caché.

Les auteurs limitent leur analyse à six variantes de la tâche, à une couche et une intensité d'injection sélectionnées par modèle, et à des modèles ne dépassant pas 12 milliards de paramètres. Ils étudient explicitement le signalement fonctionnel et ne font aucune affirmation sur la conscience ou l'expérience subjective.

Les signalements libres et spontanés restent en dehors de la tâche testée. L'article les propose comme pistes ultérieures, avec d'autres types de perturbations et le rôle des composants qui traitent l'information au sein de chaque position. Les auteurs ont publié du code, les partitions des données et des scripts permettant de reproduire les figures et les tableaux.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Prépublication soumise le 28 septembre ; auteurs et affiliations universitaires indiquées | VÉRIFIÉ | [Source](https://arxiv.org/abs/2609.35108) | aucune ; publication sous forme de prépublication |
| Qwen3-4B-IT, LLaMA-3.1-8B-IT et Gemma-3-12B-IT ; texte fixe, dix positions candidates, injection d'un vecteur de concept ou contrôle sans intervention ; évaluation directe de la première sortie | SELON LA SOCIÉTÉ | [Source](https://arxiv.org/abs/2609.35108) | aucune ; méthodes des auteurs |
| Calibration distincte ; 300 meilleurs concepts répartis en groupes disjoints ; six configurations de labels et labels mélangés ; performances supérieures à la référence de position de 10 %, mais variables selon le label | SELON LA SOCIÉTÉ | [Source](https://arxiv.org/abs/2609.35108) | aucune ; méthodes et tableau 1 |
| Les têtes de contrôle influencent le signalement ; les têtes de routage ultérieures influencent la localisation ; le remplacement des sorties et la redirection de l'attention étayent cette séparation | SELON LA SOCIÉTÉ | [Source](https://arxiv.org/abs/2609.35108) | aucune ; expériences causales des auteurs |
| Les informations internes de localisation peuvent persister sans signalement de position ; pertinence pour surveiller les interventions de pilotage | ANALYSE | [Source](https://arxiv.org/abs/2609.35108) | Déduction tirée des interventions sur les têtes de contrôle et de routage ; aucun résultat de surveillance en production |
| Limites du périmètre ; introspection fonctionnelle plutôt qu'expérientielle ; questions à approfondir ; code et scripts de reproduction publiés | VÉRIFIÉ | [Source](https://arxiv.org/abs/2609.35108) | aucune ; périmètre annoncé de l'article et lien vers le dépôt |

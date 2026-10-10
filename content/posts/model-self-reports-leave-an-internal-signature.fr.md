+++
title = "Les autorapports des modèles laissent une signature interne"
slug = "autorapports-modeles-laissent-signature-interne"
description = "Une étude contrôlée montre que les rapports fidèles sur des préférences apprises réutilisent davantage les calculs sous-jacents aux décisions du modèle. Le résultat suggère un test en boîte blanche de leur ancrage, dans des limites étroites."
tags = ["research", "models"]
date = 2026-10-10T04:01:41+02:00
draft = false
+++

Les modèles qui décrivaient précisément leurs propres préférences apprises réutilisaient davantage les calculs internes sous-jacents à leurs décisions que ceux qui confabulaient, rapporte une nouvelle prépublication.

David Atkinson et David Bau, de Northeastern University, avec Dillon Plunkett d'Eleos AI Research, ont créé des personnages fictifs aux préférences cachées et entraîné des modèles Qwen3 à choisir en leur nom. Les modèles n'ont jamais été entraînés à expliquer ces préférences, ce qui a permis à l'équipe de demander si un autorapport exact pouvait émerger spontanément.

## Pourquoi c'est important {#why-it-matters}

Un chercheur en interprétabilité qui évalue l'affirmation d'un modèle sur son propre état se heurte généralement à un problème circulaire : la déclaration semble plausible, mais l'état lui-même peut être impossible à vérifier. Cette expérience fournit une vérité de référence connue et trouve une différence structurelle entre les rapports qui lui correspondent et ceux qui ne lui correspondent pas.

Les préférences fictives étaient des règles simples à cinq nombres portant sur des caractéristiques comme la distance au centre-ville et la taille d'une pièce. Un modèle voyait des paires d'options et apprenait laquelle son personnage attitré choisirait. Des prompts distincts lui demandaient ensuite de produire les poids des préférences du personnage sous forme de nombres.

Des rapports exacts ont fini par émerger dans certaines exécutions, même si les données d'entraînement ne contenaient que des décisions. C'est important, car le modèle ne pouvait pas simplement imiter une explication vue pendant l'entraînement ; il devait traduire en langage la règle de décision qu'il avait apprise.

## Les mêmes poids soutiennent le choix et le rapport

Les auteurs ont ensuite utilisé l'attribution patching, une méthode qui estime quels composants d'un adaptateur contribuent à une sortie donnée. Ils ont comparé le schéma utilisé pour faire un choix à celui utilisé pour rapporter la préférence cachée.

Les adaptateurs fidèles présentaient une similarité moyenne de 0,34 entre ces schémas, contre 0,08 pour les adaptateurs non fidèles. L'intervalle d'incertitude des auteurs sur la différence excluait zéro. Autrement dit, les rapporteurs exacts tendaient à s'appuyer davantage sur les mêmes circuits ajoutés pour agir et décrire ce qui guidait l'action.

Les expériences sur les couches allaient dans le même sens. Un modèle Qwen3 de 14 milliards de paramètres entraîné sur ses 40 couches apprenait les décisions, mais rapportait mal ses préférences. Restreindre l'entraînement à environ le premier quart ou la première moitié du réseau produisait des rapports nettement plus fidèles, tandis qu'entraîner uniquement les couches ultérieures ne reproduisait pas l'effet. Les auteurs interprètent cela comme un déplacement des informations de préférence vers des couches accessibles aux mécanismes de verbalisation existants.

Les éléments sont mécanistes plutôt que comportementaux : le test n'a pas besoin de comprendre la formulation du rapport. En principe, la même comparaison pourrait fonctionner sur un rapport obscurci ou dans une langue inconnue, à condition que les composants internes pertinents soient accessibles.

### L'étude a également montré

Les grands modèles Qwen3 apprenaient plus souvent un autorapport fidèle que les petites variantes, même si certains petits modèles développaient des rapports négativement corrélés malgré de bonnes décisions. Une réplication avec Gemma 4 a trouvé des adaptateurs de forte et de faible fidélité parmi les grandes configurations. Au sein d'un modèle partagé, la relation entre similarité d'attribution et fidélité à travers les personnages était positive, mais faible.

Le résultat ne fournit pas de détecteur d'introspection pour les modèles déployés. Les règles de préférence étaient construites, linéaires et limitées à cinq dimensions ; les expériences modifiaient des adaptateurs légers plutôt que tous les poids du modèle ; et les scores de similarité des groupes fidèles et non fidèles se chevauchaient. Une forte similarité étayait la fidélité dans cette configuration, mais un faible score ne prouvait ni tromperie ni confabulation.

La prépublication a été soumise le 5 octobre 2026. Sa prochaine étape la plus claire consiste à tester si la même réutilisation interne apparaît lorsque les modèles rapportent des stratégies apprises plus riches dont la vérité de référence reste mesurable indépendamment.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| L'étude a entraîné des adaptateurs LoRA sur des préférences linéaires cachées et observé des autorapports exacts sans supervision de l'autorapport | SELON LA SOCIÉTÉ | https://arxiv.org/abs/2610.07186 | aucune |
| Les adaptateurs fidèles avaient une similarité d'attribution moyenne de 0,34, contre 0,08 pour les adaptateurs non fidèles | SELON LA SOCIÉTÉ | https://arxiv.org/abs/2610.07186 | aucune |
| L'entraînement des seules couches précoces améliorait l'autorapport dans Qwen3-14B, contrairement à celui des seules couches tardives | SELON LA SOCIÉTÉ | https://arxiv.org/abs/2610.07186 | aucune |
| La méthode distingue des groupes aux scores chevauchants et a été testée sur des adaptateurs dans une configuration contrôlée | VÉRIFIÉ | https://arxiv.org/abs/2610.07186 | aucune |
| L'article a été soumis le 5 octobre 2026 par Atkinson, Plunkett et Bau | VÉRIFIÉ | https://arxiv.org/abs/2610.07186 | aucune |

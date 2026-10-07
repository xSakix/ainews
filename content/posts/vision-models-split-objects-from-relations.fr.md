+++
title = "Les modèles visuels séparent objets et relations abstraites"
slug = "modeles-visuels-separent-objets-et-relations-abstraites"
description = "Une prépublication repère un circuit précoce d'appariement des objets et un circuit plus tardif d'appariement des relations dans les modèles vision-langage. Elle relie ensuite le second aux performances sur ARC-AGI-1."
tags = ["research", "models"]
date = 2026-10-07T03:59:57+02:00
draft = false
+++

Les modèles vision-langage pourraient résoudre des comparaisons visuelles abstraites grâce à deux processus internes concurrents : l'un, précoce, suit les objets visibles ; l'autre, plus tardif, représente leurs relations.

C'est la principale conclusion d'une prépublication de Minegishi, Furuta, Kojima et leurs collègues. L'équipe a adapté une tâche Relational Match-to-Sample issue de la psychologie développementale et comparée, puis testé des systèmes propriétaires de pointe et des modèles ouverts sur des images contrôlées.

## Pourquoi c'est important {#why-it-matters}

Pour un chercheur qui évalue le raisonnement visuel, une réponse correcte ne suffit pas à révéler si le modèle a suivi la règle sous-jacente ou simplement reconnu des formes similaires. L'étude propose de séparer ces voies, puis d'intervenir sur celle associée aux relations abstraites.

Chaque tâche présente une paire d'objets de référence et demande quelle paire candidate possède la même relation. Une candidate peut conserver la relation en changeant les objets ; une autre peut conserver l'apparence en changeant la relation. Le conflit révèle si le modèle suit l'identité ou la structure.

Dans les familles GPT, Claude, Gemini, Qwen3.5, Gemma 4 et InternVL3, quatre changements ont orienté les réponses vers les relations : un niveau de modèle plus performant, un modèle plus grand, moins d'objets dans la scène et moins de bruit associé à chacun. Les auteurs comparent cette progression au « changement relationnel » observé dans le développement humain, mais la ressemblance est comportementale et ne prouve pas un mécanisme cognitif partagé.

L'analyse interne a trouvé les deux signaux à des profondeurs différentes. Les représentations des premières couches regroupaient les exemples selon les caractéristiques des objets ; celles des couches ultérieures les regroupaient selon la relation abstraite. Des tests de médiation causale ont ensuite identifié des têtes d'attention dont l'activité contribuait aux réponses fondées sur les relations.

## Une intervention relie le circuit à une autre tâche

Le résultat le plus solide vient de la désactivation des têtes associées à l'appariement relationnel. Les auteurs rapportent qu'elle dégrade davantage les performances sur ARC-AGI-1 que la désactivation de têtes choisies au hasard. Ce transfert compte, car les têtes ont été repérées sur la tâche psychologique d'appariement plutôt que sélectionnées directement pour expliquer les résultats ARC.

La portée des preuves reste limitée. Un ensemble de têtes peut contribuer à deux tâches sans constituer un module de raisonnement général. Les stimuli sont volontairement simples, et l'article ne démontre pas que la même concurrence contrôle la reconnaissance dans des photographies, des graphiques ou de longues conversations multimodales.

L'étude repose aussi sur deux niveaux d'accès. Les résultats comportementaux peuvent inclure des modèles API propriétaires, mais l'analyse des représentations couche par couche et l'ablation exigent des poids ouverts. L'affirmation sur le mécanisme repose donc sur les modèles ouverts examinés de l'intérieur, tandis que la comparaison élargie entre familles porte sur le comportement.

La conception paramétrique facilite la reproduction. Le nombre d'objets et le bruit visuel peuvent varier séparément, ce qui permet à une autre équipe de tester si la séparation entre couches résiste à de nouvelles formes, relations et familles de modèles. La page du résumé ne mentionne pas de dépôt de code public : reproduire toute l'intervention demandera donc davantage que télécharger un benchmark.

L'article a été soumis à arXiv le 6 octobre 2026 et n'a pas été évalué par les pairs. Sa contribution utile est un pont réfutable entre une tâche cognitive classique et les circuits internes des modèles : le comportement suivant les relations devrait faiblir quand la voie tardive identifiée est perturbée, tandis que l'appariement des objets devrait rester relativement intact.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| L'étude teste l'appariement relationnel dans des modèles vision-langage API de pointe et ouverts | SELON LA SOCIÉTÉ | [prépublication](https://arxiv.org/abs/2610.07646) | aucune ; évaluation des auteurs |
| L'échelle, les capacités, moins d'objets et moins de bruit orientent les modèles vers l'appariement des relations | SELON LA SOCIÉTÉ | [prépublication](https://arxiv.org/abs/2610.07646) | aucune |
| Les premières couches codent la similarité des objets, les couches ultérieures les relations abstraites | SELON LA SOCIÉTÉ | [prépublication](https://arxiv.org/abs/2610.07646) | aucune |
| L'ablation des têtes associées aux relations dégrade ARC-AGI-1 davantage que celle de têtes aléatoires | SELON LA SOCIÉTÉ | [prépublication](https://arxiv.org/abs/2610.07646) | aucune |
| Une ressemblance comportementale ne prouve pas un mécanisme humain partagé | ANALYSE | [prépublication](https://arxiv.org/abs/2610.07646) | déduction tirée de la conception de l'étude |
| La prépublication a été soumise le 6 octobre 2026 | VÉRIFIÉ | [notice arXiv](https://arxiv.org/abs/2610.07646) | métadonnées arXiv |

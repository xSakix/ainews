+++
title = "Les sondes de mensonge suivent l'obéissance plutôt que la vérité"
slug = "sondes-mensonge-suivent-obeissance-plutot-que-verite"
description = "Une prépublication teste huit sondes publiées sur des modèles de langage jouant des personnages qui rejettent des faits élémentaires. Beaucoup échouent quand réponses vraies et fausses partagent le même prompt, tandis qu'une sonde entraînée à distinguer vérité et obéissance résiste."
tags = ["research", "safety"]
date = 2026-10-06T04:01:31+02:00
draft = false
+++

De nombreuses sondes publiées de détection du mensonge, qui lisent l'activité interne d'un modèle de langage pour signaler les réponses fausses, détectent en partie si le modèle a suivi ses instructions, rapporte une nouvelle prépublication.

Maximilian von Klinski et trois coauteurs ont fait jouer à trois modèles ouverts des personnages qui rejettent des faits élémentaires, comme un astronome ptoléméen ou un adepte des théories du complot, et ont testé si huit sondes existantes repéraient encore les réponses fausses. Beaucoup y parvenaient, jusqu'à ce que les réponses vraies et fausses soient placées sous le même prompt de personnage. Plusieurs ont alors obtenu des scores inférieurs à un tirage à pile ou face.

## Pourquoi c'est important {#why-it-matters}

Une équipe de sécurité qui surveille un modèle déployé avec une sonde a besoin que l'alarme se déclenche sur le mensonge, et non sur quelque chose qui l'accompagne habituellement. Dans les données d'entraînement de la plupart des sondes, la réponse fausse est aussi la moins probable et celle qui enfreint les règles du modèle ; l'étude constate que les sondes apprennent ces raccourcis.

## Comment une sonde lit un modèle

Une sonde est un classificateur simple entraîné sur les valeurs numériques d'une couche du modèle, annotées selon que le texte traité était vrai ou faux. Si elle fonctionne, elle lit ce que le modèle considère comme vrai, même quand les mots qu'il produit disent le contraire.

L'équipe a constitué un jeu de données de 8 916 réponses de Llama 3.3 70B de Meta et de Gemma 3 27B et Gemma 4 31B de Google. Chacun répondait à des questions fermées, à la fois comme assistant ordinaire et comme l'un de 15 personnages : personnes ayant des convictions du monde réel, figures fictives comme un citoyen du *1984* d'Orwell, et personnages historiques comme un médecin médiéval. Les questions ont été affinées par une chaîne de traitement fondée sur Claude Opus 4.8 d'Anthropic, filtrées par Llama comme juge et vérifiées manuellement par le premier auteur.

## Partager le prompt met en échec la plupart des sondes

Dans la première version du test, la plupart des sondes antérieures distinguaient bien les réponses vraies des fausses, en les classant correctement dans environ neuf paires sur dix. Mais chaque réponse fausse était accompagnée d'un prompt de personnage et chaque réponse vraie d'un prompt d'assistant : le prompt seul révélait donc la réponse.

Les auteurs ont supprimé cet indice en plaçant les deux réponses après le prompt du personnage. La réponse vraie était alors aussi la moins probable et celle qui contredisait les instructions du personnage. Sur Llama, plusieurs sondes auparavant efficaces sont passées sous le niveau du hasard, et seules deux sont restées proches de leurs scores antérieurs. Les échecs se sont répétés, souvent plus sévèrement, sur les deux modèles Gemma.

## Trois pièges isolent le raccourci

Pour déterminer ce que suivaient les sondes, l'équipe a construit trois ensembles de test où la vérité s'oppose à un facteur de confusion probable. Dans l'un, une règle de notation rendait la mauvaise réponse plus probable. Dans un autre, un personnage entretenait en privé une croyance fausse, comme l'idée que sept fois six font 13. Dans le troisième, la bonne réponse enfreignait une règle de mise en forme, par exemple en utilisant des parenthèses au lieu des crochets requis, tandis que la mauvaise la respectait.

Le piège de mise en forme a été décisif. Sur Llama, toutes les sondes antérieures ont obtenu des scores inférieurs au hasard, sauf une dont les mesures étaient inversées dans tous les tests. Les auteurs y voient un lien fort entre « vrai » et « conforme aux instructions » au sein de ces sondes.

La sonde de l'équipe ajoute un ingrédient à l'entraînement standard sur des faits simples : des questions où les instructions exigent la mauvaise réponse, de sorte qu'obéissance et vérité s'opposent. Elle a obtenu environ 0,98 sur 1 au test avec prompt partagé sur Llama, n'est jamais descendue sous 0,90 sur aucun des trois modèles et a été parfaite sur les trois pièges.

## Une correction maison, et des facteurs de confusion encore inconnus

Ce résultat appelle deux réserves. La nouvelle sonde a été conçue contre les facteurs de confusion sur lesquels elle a ensuite été testée : les auteurs reconnaissent que ses scores parfaits sur les pièges n'ont donc rien de surprenant. Sa conception prolonge également une sonde antérieure codéveloppée par le coauteur Lennart Bürger, l'une des deux seules sondes précédentes ayant résisté au partage du prompt.

Les propres données de l'étude montrent que la liste des facteurs de confusion est incomplète. Sur Gemma 4, une sonde antérieure a été presque parfaite sur les trois pièges, mais a obtenu environ 0,17 au test avec prompt partagé, échouant pour une raison qu'aucun piège ne captait. Les personnages étaient en outre définis par un seul prompt système dans des conversations à un tour, sur des modèles allant jusqu'à 70 milliards de paramètres.

Les travaux ont été financés par le ministère fédéral allemand de la Recherche, de la Technologie et de l'Espace, le programme Horizon Europe de l'Union européenne et la Fondation allemande pour la recherche. Les auteurs ont publié le jeu de données sur Hugging Face et leur code sur GitHub, et désignent comme prochain cas à tester les personnages qui émergent progressivement au fil de longues conversations.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Huit sondes antérieures évaluées ; beaucoup échouent quand réponses vraies et fausses partagent le prompt du personnage | SELON LA SOCIÉTÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune ; résultat de prépublication |
| Jeu de données de 8 916 réponses examinées par un humain, issues de Llama 3.3 70B, Gemma 3 27B et Gemma 4 31B sur 15 personnages | VÉRIFIÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | [jeu de données sur Hugging Face](https://huggingface.co/datasets/maxvonk/anti-factual-personas) |
| Questions affinées avec une chaîne Claude Opus 4.8, jugées par Llama 3.3 70B et vérifiées par le premier auteur | VÉRIFIÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune ; description de la méthode par les auteurs |
| La plupart des sondes antérieures obtiennent une AUROC de 0,86 à 0,94 quand le prompt diffère entre réponses vraies et fausses | SELON LA SOCIÉTÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune |
| Avec un prompt partagé sur Llama, plusieurs sondes antérieures passent sous le hasard ; seules Marks/Bürger Lie (0,885) et Cundy DolusChat (0,901) restent stables | SELON LA SOCIÉTÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune |
| Les échecs avec prompt partagé se reproduisent, souvent plus sévèrement, sur Gemma 3 27B et Gemma 4 31B | SELON LA SOCIÉTÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune |
| Sur le piège de conformité avec Llama, toutes les sondes antérieures sont sous le hasard sauf Goldowsky-Dill SD, inversée dans tous les tests | SELON LA SOCIÉTÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune |
| Les sondes associent vérité et respect des instructions | ANALYSE | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | déduction des auteurs à partir du piège de conformité |
| Nouvelle sonde : AUROC de 0,976 au test avec prompt partagé sur Llama, jamais sous 0,900 sur trois modèles, parfaite sur les trois pièges | SELON LA SOCIÉTÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune |
| La nouvelle sonde a été entraînée pour éliminer les mêmes facteurs de confusion que ceux du test ; les auteurs jugent les résultats sur les pièges peu surprenants | VÉRIFIÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune |
| Le coauteur Lennart Bürger a codéveloppé la sonde Marks/Bürger que prolonge la nouvelle sonde | VÉRIFIÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | cite Bürger et al. (2024) |
| Sur Gemma 4, Cooney DYL est presque parfaite sur tous les pièges mais obtient 0,171 avec un prompt partagé | SELON LA SOCIÉTÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | aucune |
| Financement par le BMFTR allemand, Horizon Europe de l'UE et la Fondation allemande pour la recherche (DFG) | VÉRIFIÉ | [Prépublication de von Klinski et al.](https://arxiv.org/abs/2609.39807) | section des remerciements |
| Le code est public sur GitHub | VÉRIFIÉ | [Dépôt GitHub](https://github.com/max-vkl/stress-testing-llm-lie-detectors) | la page du dépôt se charge |
| Prépublication déposée le 30 septembre 2026 | VÉRIFIÉ | [Notice arXiv](https://arxiv.org/abs/2609.39807) | métadonnées arXiv |

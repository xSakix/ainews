+++
title = "Pourquoi un contexte non pertinent change la réponse d’un modèle"
slug = "contexte-non-pertinent-change-reponse-modele"
description = "Une nouvelle étude mécaniste suit le texte non pertinent d’un prompt à travers un modèle de langage. Elle identifie une voie distincte capable de fausser une réponse même lorsque le texte ajouté ne fournit aucun élément concurrent."
tags = ["research", "agents"]
date = 2026-11-06T04:12:00+01:00
draft = false
+++

Imaginons un analyste demandant à un modèle la capitale d'un pays après qu'un système de recherche a inséré un paragraphe sur un autre lieu. Ce paragraphe ne contient pas de capitale concurrente. Il ne contredit pas la question. Il est simplement sans rapport. Pourtant, le modèle devient moins susceptible de donner la réponse qu'il connaissait déjà.

Cette scène est illustrative, mais la défaillance est familière à quiconque a construit un système de recherche d'information ou un agent à contexte long. Plus de contexte peut dégrader une réponse. Une nouvelle prépublication de Dikshant Kukreja, Gautam Gupta, Avni Mittal et leurs collègues tente d'expliquer pourquoi au niveau du calcul interne du modèle. Leur réponse est une « voie d'intrusion » : le texte non pertinent est enrichi, recopié vers l'avant, puis favorisé par un petit ensemble de têtes d'attention.

La distinction compte, car la plupart des défenses abordent le contexte distrayant par une meilleure recherche, des instructions plus fermes ou des fenêtres de contexte plus grandes. L'article pose une autre question. Une fois le texte non pertinent dans le prompt, quelles parties du modèle lui permettent d'influencer la réponse ?

## Un distracteur sans fausse réponse

Les chercheurs partent de relations factuelles connues des modèles à poids ouverts, par exemple une personne et un attribut associé. Ils construisent des prompts propres et plusieurs sortes de contexte supplémentaire : éléments pertinents, éléments contrefactuels, texte non pertinent court, texte non pertinent long et texte aléatoire. Leur jeu de données de référence contient 250 faits auxquels au moins trois des quatre modèles de base répondent correctement.

Cette conception distingue la contradiction de l'intrusion. Un passage contrefactuel peut attirer un modèle vers une réponse erronée précise. Un texte non pertinent n'a pas besoin de le faire. Il peut diminuer la probabilité de la bonne réponse simplement en entrant dans le calcul aux mauvais endroits.

Les expériences utilisent Llama 3.1 8B, Mistral 7B, Qwen 2.5 7B, Pythia 6.9B et GPT-2 XL, ainsi que des modèles plus grands pour un test mathématique. Aucun modèle n'est entraîné. Le dépôt public contient les scripts qui construisent les jeux de données, sélectionnent les têtes concernées et reproduisent les interventions.

Le premier résultat important concerne l'endroit où les dégâts apparaissent. Les couches feed-forward enrichissent les représentations du sujet de la question comme des tokens du passage non pertinent. Certaines têtes d'attention recopient ensuite des éléments du préfixe vers la position finale, où le modèle doit prédire la réponse. Les auteurs les appellent des têtes de répétition. Un second groupe restreint de têtes transforme ces éléments importés en pression sur la distribution de sortie.

## Récupération d'information et intrusion ne suivent pas le même circuit

Les auteurs distinguent les têtes de récupération, qui aident à transporter les éléments pertinents, des têtes d'intrusion, qui véhiculent l'effet indésirable. Les deux ensembles se recouvrent peu. Cela rend le résultat plus utile qu'une affirmation générale selon laquelle l'attention est bruitée. Un système peut avoir besoin des mécanismes qui transmettent les preuves tout en gagnant à supprimer la voie distincte qui favorise les distracteurs.

L'article teste la causalité plutôt que de s'appuyer seulement sur des corrélations entre configurations d'attention et erreurs. Lorsque les chercheurs remplacent l'état résiduel final d'une exécution distraite par l'état correspondant d'une exécution propre, ils récupèrent 97,6 % de la baisse de précision. C'est une intervention oracle : elle exige un second passage propre et ne constitue donc pas une défense pratique en production. Elle montre néanmoins que les dégâts pertinents ont atteint l'état du dernier token.

Ils masquent aussi certaines têtes d'intrusion. Cette intervention est déployable en principe, car elle ne nécessite pas d'exécution propre de référence. Les auteurs l'évaluent sur des relations réservées au test et sur plusieurs tâches en aval, dont HotpotQA, PubMedQA et des jeux de données arithmétiques accompagnés d'énoncés distrayants. Ils testent également si les ensembles de têtes se transfèrent entre modèles et entre versions de base et versions affinées sur des instructions.

La défense a un coût. Supprimer des têtes d'attention peut aussi supprimer du calcul utile, et le nombre de têtes neutralisées compte. Le dépôt comprend donc des explorations du nombre de têtes et du seuil de sélection, ainsi que des tests de stabilité sur des données réservées. Ce n'est pas un interrupteur universel qui sécurise le contexte. C'est une méthode pour identifier un compromis plus ciblé.

## Pourquoi cela change l'ingénierie du contexte

La génération augmentée par recherche traite souvent la pertinence comme un problème de recherche. Un système classe les passages, un constructeur de prompts décide combien en inclure, et le modèle est censé ignorer le reste. Les nouveaux travaux montrent pourquoi cette dernière hypothèse peut échouer. Un texte peut influencer une réponse sans apporter de preuve ni l'emporter dans une confrontation directe avec la vérité.

Dire que « la réponse se trouvait quelque part dans le contexte » devient alors un diagnostic incomplet. Un long prompt peut contenir le bon document tout en réduisant la précision, parce que des passages sans rapport activent une voie distincte. Les tests en aval des auteurs relient l'analyse des circuits à des tâches où les modèles doivent répondre à des questions ou raisonner malgré des énoncés ajoutés.

Ces travaux montrent aussi la limite d'une réponse courante aux échecs du contexte : demander au modèle d'ignorer les informations non pertinentes. Les instructions agissent par le même modèle qui traite déjà le distracteur. Une intervention mécaniste peut tester si la voie nuisible reste active même lorsque le modèle semble suivre l'instruction.

Les limites sont importantes. Les modèles sont des systèmes à poids ouverts dont les activations internes peuvent être inspectées et modifiées. Les travaux les plus nets sur les circuits portent sur des modèles bien plus petits que les plus grands systèmes de pointe actuels. Les jeux de données factuels sont contrôlés, et la récupération oracle ne peut pas être déployée telle quelle. L'article est une prépublication qui n'a pas été évaluée par les pairs.

Les preuves sont néanmoins particulièrement inspectables. Le dépôt nomme les modèles, les jeux de données, les scripts, la procédure de sélection des têtes et les explorations d'interventions. D'autres chercheurs peuvent examiner si la même séparation entre récupération et intrusion apparaît dans d'autres architectures, dans des modèles plus grands et dans de véritables traces de production.

Une équipe d'ingénierie fictive pourrait désormais diagnostiquer une mauvaise réponse en deux étapes. Elle demanderait d'abord si la recherche a fourni les éléments nécessaires. Puis elle examinerait si des passages non pertinents ont modifié le chemin interne vers la réponse. Cette seconde question ne remplace pas une meilleure recherche. Elle explique pourquoi une meilleure recherche et des passages moins nombreux et plus propres peuvent compter même lorsque le modèle semble capable d'ignorer le bruit.

La leçon générale est simple : le contexte n'est pas un stockage inerte. Chaque passage supplémentaire entre dans un calcul. Kukreja et ses collègues ont cartographié l'une des voies par lesquelles un passage inapproprié peut peser sans jamais formuler une réponse fausse.

## Références

- Dikshant Kukreja, Gautam Gupta, Avni Mittal et al., “The Intrusion Pathway: How Non-Evidential Context Degrades Language Model Performance” — https://arxiv.org/abs/2611.07778
- Dikshant Kukreja et al., code and reproduction guide for “The Intrusion Pathway” — https://github.com/dk4248/the-intrusion-pathway
- TransformerLens contributors, “TransformerLens” — https://github.com/TransformerLensOrg/TransformerLens
- Javier Hernandez et al., relations dataset used for factual-recall experiments — https://github.com/evandez/relations
- Freda Shi et al., “GSM-IC: A Benchmark for Understanding the Effects of Irrelevant Context in Mathematical Reasoning” dataset — https://github.com/google-research-datasets/GSM-IC

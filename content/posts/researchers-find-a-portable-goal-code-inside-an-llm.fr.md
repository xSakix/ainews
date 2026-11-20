+++
title = "Des chercheurs trouvent un code d’objectif transférable dans un LLM"
slug = "chercheurs-code-objectif-transferable-llm"
description = "Une prépublication relie le prochain objectif de programmation d’un LLM à un petit groupe de têtes d’attention, le lit en langage courant et le transfère entre langages de programmation. C’est une preuve causale dans un cadre contrôlé, pas la preuve que chaque agent possède une intention intérieure stable."
tags = ["research", "models", "agents"]
date = 2026-11-14T04:08:30+01:00
draft = false
+++

Une développeuse fictive nommée Mara observe une fonction générée qui vient de compter les mots commençant par une majuscule et s’apprête à rechercher des palindromes. Le curseur se trouve après un signe égal. Aucune comparaison n’est apparue, aucune chaîne n’a été inversée et aucun token de sortie n’indique la suite. Mara aimerait suspendre le modèle à cet endroit et poser une question simple : qu’essaies-tu de faire maintenant ? La scène est illustrative. Une nouvelle expérience transforme cette question en un phénomène que les chercheurs peuvent tester à l’intérieur d’un modèle.

## Un objectif avant le code

Arnab Sen Sharma et neuf collègues de Northeastern University, Parallax, l’University of Copenhagen et l’University of Oxford rapportent que le prochain sous-objectif d’un modèle de programmation peut être localisé dans un petit groupe de têtes d’attention. Leur prépublication, parue le 12 novembre, va au-delà d’une corrélation. Les chercheurs décodent la représentation en langage naturel, la transplantent dans un autre langage de programmation et interviennent dessus pour modifier ce que le modèle écrit.

Le travail pose une version étroite d’une question vaste et chargée : les modèles de langage ont-ils des objectifs ? Les auteurs évitent de prendre un comportement fluide pour une preuve d’intention. Ils définissent un objectif comme un état interne qui apparaît avant une action, peut être réalisé par différents moyens et persiste pendant l’action. Cette définition opérationnelle produit trois tests : engagement préalable, plasticité et persistance.

La tâche contrôlée rend ces tests possibles. Les prompts demandaient à un modèle d’accomplir deux à quatre opérations indépendantes sur des entiers, chaînes ou listes. Une opération pouvait compter les mots commençant par une majuscule, trouver un intervalle ou vérifier si un mot était un palindrome. Les chercheurs ont utilisé 253 spécifications et examiné quatre positions avant le début de chaque opération suivante, soit 1 012 observations dans chaque configuration d’évaluation.

La plupart des principaux résultats utilisent Qwen-2.5-Coder-32B-Instruct, un modèle à 64 couches. Une procédure de sélection parcimonieuse a identifié 122 têtes d’attention concentrées entre les couches 28 et 55. Elle récompensait les têtes dont la sortie pouvait être déplacée d’un prompt source dans un langage de programmation vers un prompt de destination dans un autre langage et déclencher l’opération source. Choisir des langages différents était important : une représentation de vérification de palindrome devait survivre aux changements de syntaxe, de noms de variables et de tokens concrets.

## Lire l’instruction cachée

Pour rendre la représentation lisible, l’équipe a construit une sonde appelée GoalScope à partir des sorties des têtes sélectionnées. Elle additionne ce que ces têtes écrivent dans le flux résiduel du modèle à un token choisi, puis injecte ce vecteur dans une exécution séparée du même modèle. La seconde exécution reçoit une demande fixe de description de l’opération. Son prompt textuel ne contient aucune information du problème de programmation initial : l’activation injectée est donc la seule voie par laquelle le contexte initial peut atteindre la réponse.

Cette méthode prolonge Patchscopes, un framework présenté par Asma Ghandeharioun et ses collègues pour placer une représentation cachée dans un prompt où un modèle peut l’expliquer. Elle suit aussi les travaux antérieurs de plusieurs des mêmes chercheurs. Function Vectors a montré qu’une somme compacte de sorties de têtes d’attention pouvait porter une fonction entrée-sortie et la déclencher dans un nouveau contexte. General Filter Heads a ensuite isolé une représentation transférable de prédicats servant à filtrer des listes. Le nouvel article passe d’une opération unique à l’étape suivante changeante d’une tâche à plusieurs opérations.

La lecture de l’objectif devenait utile avant que le modèle émette l’implémentation. À la fin de la ligne précédente, les descriptions de GoalScope correspondaient à une partie non triviale du comportement à venir dans environ 60 % des cas. Au point d’indentation, trois tokens avant l’implémentation, le score rapporté dépassait 90 %. Transféré dans un contexte C++, l’encodage déclenchait l’opération correspondante dans 96 % des cas à une position pivot ; la moyenne des positions pivots était d’environ 87 %.

Ces résultats étayent l’engagement préalable et la plasticité. Ils indiquent que l’activité sélectionnée porte de l’information sur ce qu’il faut faire avant l’apparition du code pertinent, et que cette information n’est pas simplement une séquence de tokens Python mise en cache. Le modèle de destination produit une voie adaptée à son nouveau contexte.

Les tests causaux précisent cette affirmation. Lorsque les chercheurs préservaient l’accès des têtes sélectionnées à la tâche suivante tout en bloquant l’accès à ce passage pour environ 93 % des têtes d’attention ultérieures, le modèle conservait largement sa capacité à implémenter l’opération. Aveugler seulement les 122 têtes sélectionnées laissait une possibilité de compensation par des voies redondantes, mais aveugler un ensemble plus large de 250 réduisait fortement la performance. Les auteurs décrivent un goulot d’étranglement causal avec redondance plutôt qu’un interrupteur unique indispensable.

## Un objectif reconstruit à chaque étape

La persistance pose une énigme mécanique. Un transformer autorégressif n’a pas d’état récurrent qui puisse simplement être transmis indéfiniment d’un token généré au suivant. L’attention peut lire une position antérieure, mais faire avancer un état nouvellement calculé consomme des couches. Dans ce modèle, l’objectif ne devenait verbalisable qu’après environ la couche 40, laissant trop peu de profondeur pour porter le même état au fil d’opérations de plus de 30 tokens.

Les auteurs proposent un autre mécanisme. Le modèle relit régulièrement la spécification, examine le code déjà terminé visible dans son contexte et reconstruit l’opération en attente. Ils appellent cela une poursuite d’objectif non récurrente. La continuité apparente vient d’un calcul répété, pas d’un objet interne unique voyageant intact à travers la séquence.

Des transplantations ciblées étayaient cette interprétation. Les chercheurs ont modifié les états clé-valeur que les têtes d’objectif lisaient dans le passage de la tâche tout en laissant les autres têtes sur le prompt de destination. Le modèle implémentait alors l’opération suivante du prompt source dans le langage de destination dans environ 94 % des cas, et la description de GoalScope changeait avec elle dans environ 90 % des cas. Dans une intervention séparée, remplacer les états de requête des têtes transférait de l’information sur le travail accompli et changeait le sous-objectif restant sélectionné par le modèle.

Cette distinction compte pour le contrôle. Un outil de surveillance pourrait lire une opération en attente avant son apparition dans la sortie, et une intervention pourrait la réorienter. Pourtant, la représentation est assemblée à partir de la spécification et des progrès visibles. Modifier l’une de ces sources peut aussi modifier l’objectif apparent.

## Les limites d’un objectif lisible

L’article n’établit pas l’existence d’un centre universel des objectifs. Son jeu de données central comporte des opérations de programmation énumérées, la plupart des mesures du texte principal viennent d’un modèle ajusté pour le code et un juge LLM note l’accord entre descriptions et implémentations générées. Les auteurs testent d’autres familles de modèles et quelques contextes en langage naturel dans les annexes, mais citent la couverture des modèles et des tâches parmi leurs limites.

La mise en garde la plus forte apparaît lorsque le parcours est perturbé. Le modèle conservait un encodage reconnaissable pendant l’exécution ordinaire, mais échouait souvent à se remettre d’un faux départ introduit. Qwen-2.5-Coder-32B-Instruct s’adaptait dans environ 97 % des cas alignés, 63 % des perturbations faciles et seulement 15 % des difficiles. Les autres modèles testés montraient le même déclin. Un objectif lisible ne garantissait pas sa poursuite réussie.

Mara revient au curseur en attente. Dans cette scène finale inventée, son débogueur affiche une note provisoire : vérifier si un mot est un palindrome. Elle la traite comme une prévision liée à ce prompt et à ce point du code, pas comme la confession d’une machine. Puis elle insère un préfixe trompeur. La note nomme toujours la tâche, tandis que le code généré s’égare. La recherche lui donne une fenêtre sur l’opération suivante du modèle. Elle montre aussi pourquoi voir un objectif et faire confiance à son exécution restent deux travaux distincts.

## Références

- Ghandeharioun, A., Caciularu, A., Pearce, A., Dixon, L., & Geva, M. (2024). *Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models*. https://arxiv.org/abs/2401.06102
- Sen Sharma, A., Rogers, G., Shapira, N., & Bau, D. (2026). *LLMs Process Lists With General Filter Heads*. https://arxiv.org/abs/2510.26784
- Sen Sharma, A., Todd, E., Feucht, S., Arditi, A., Gandikota, R., Shapira, N., Sarti, G., Fierro, C., Schut, L., & Bau, D. (2026). *Goal Encoding in LLMs*. https://arxiv.org/abs/2611.17297
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://arxiv.org/abs/2310.15213

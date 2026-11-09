+++
title = "Le code des étudiants a triplé, pas les commentaires"
slug = "code-etudiants-triple-pas-commentaires"
description = "Une étude sur dix semestres de 260 dépôts d’équipes de fin d’études constate que le code final est passé d’environ 3,4 à 10 milliers de lignes avec la diffusion de l’IA générative, tandis que la densité des commentaires stagnait. Les auteurs n’ont jamais observé l’usage de l’IA : le résultat avertit les évaluateurs et les employeurs, sans constituer un verdict sur les outils."
tags = ["research", "tools"]
date = 2026-11-09T03:16:01+01:00
draft = false
+++

Imaginons une coordinatrice de cours le vendredi précédant la remise des notes. Elle possède un tableur d'une quarantaine d'équipes étudiantes et une habitude conservée depuis des années : ouvrir le dépôt, regarder la quantité de travail construit et sa régularité, puis s'en servir pour apprécier qui a travaillé. Cette année, le premier dépôt de sa liste contient dix mille lignes de code et trois cents commits. Elle parcourt une fonction aux branchements profondément imbriqués et ne trouve aucun commentaire les expliquant. La coordinatrice est inventée : elle incarne un problème que trois chercheurs viennent de mesurer.

L'étude, *Code, Commits, and Complexity in the GenAI Era*, a été déposée sur arXiv le 5 novembre et acceptée au SIGCSE Technical Symposium de février 2027. Ses auteurs sont Asma Shakil et Paul Denny, de l'University of Auckland, et Claus Brabrand, de l'IT University of Copenhagen. Ils ont analysé 260 dépôts d'équipes d'un cours obligatoire de projet de fin d'études, sur dix semestres de 2021 à 2025. La taille médiane des bases de code en fin de semestre est passée d'environ 3,4 milliers de lignes en 2021–2023 à environ 10 milliers en 2024–2025. Les auteurs n'ont observé personne utiliser l'IA et le répètent à plusieurs reprises.

## Un cours, dix semestres

Dans ce cours, des équipes de cinq ou six étudiants développent un logiciel pour de véritables clients externes pendant treize semaines. Le prototype fonctionnel est le principal élément évalué. Les dépôts proviennent de l'organisation GitHub du cours : 302 initialement, puis 260 après le retrait des dépôts vides, des modèles de projet et des doublons. Les promotions comptent respectivement 19, 65, 57, 51 et 68 dépôts de 2021 à 2025.

Les auteurs mesurent chaque dépôt deux fois : lors de la démonstration de mi-semestre en semaine 7 et de la présentation finale en semaine 13. Ils comptent les lignes de code avec tokei, la complexité cyclomatique moyenne par fonction avec lizard et les constructions de gestion d'erreurs par une analyse lexicale. Ils comptent aussi les commits. Pour chaque mesure, ils testent si elle augmente ou diminue régulièrement sur les cinq promotions, en corrigeant pour le nombre de mesures testées.

Ils divisent les années entre une période de moindre disponibilité de l'IA générative et une période de plus grande disponibilité, en prenant la sortie de ChatGPT en novembre 2022 comme frontière approximative. Ils soulignent qu'elle n'est pas nette. GitHub Copilot est devenu gratuit pour les étudiants vérifiés en juin 2022, puis son adoption a été progressive. Ils citent une enquête du Higher Education Policy Institute dans laquelle la part des étudiants britanniques de premier cycle utilisant l'IA générative pour des travaux notés passait de 53 % fin 2023 à 88 % fin 2024.

## Ce qui a changé, et quand

La base de code finale médiane comptait 2,3 milliers de lignes en 2021, 3,7 en 2022 et 3,4 en 2023. Elle a ensuite bondi à 7,7 en 2024 et 11 en 2025. L'instantané de mi-semestre suit le même profil : de 1,4 à 1,8 millier de lignes avant 2024, puis 4,8 milliers en 2025. La promotion 2023, la première après ChatGPT, ressemble aux précédentes et les auteurs la qualifient de transitoire.

Le nombre médian de commits par dépôt est passé de 63 en 2021 et d'environ 100 à 112 en 2022 et 2023 à 265 en 2024 et 300 en 2025. Les commits par jour actif sont passés de 3,3 à 5,4. La taille de chacun a peu changé : la médiane est restée entre 38 et 65 lignes modifiées. Cela contredit l'attente courante selon laquelle le code écrit par l'IA arrive en quelques gros lots. Ces étudiants effectuaient des commits plus fréquents, par morceaux à peu près aussi grands qu'avant.

Le résultat le plus frappant concerne l'intérieur du code. La complexité cyclomatique moyenne est passée de 1,7 en 2021 à 2,5 en 2025, et les constructions de gestion d'erreurs par millier de lignes de 3,7 et 4,8 en 2022 et 2023 à 12 et 13 en 2024 et 2025. La densité des commentaires, c'est-à-dire la part des lignes constituées de commentaires, ne montrait aucune tendance nette : elle était de 9,2 % en 2021 et de 8,4 % en 2025. Les auteurs nomment ce profil « complexité sans commentaire ». Les promotions récentes rendaient du code plus volumineux et plus complexe, mais pas mieux expliqué.

## Ce que les auteurs ne prétendent pas

Shakil, Brabrand et Denny énoncent clairement les limites. Ils n'ont pas observé l'usage de l'IA et rapportent donc des changements concomitants à sa disponibilité accrue, pas des effets. Le personnel, les critères d'évaluation et les types de projets ont changé au fil des ans ; la promotion 2021 et une partie de 2022 ont travaillé en partie sous restrictions liées à la COVID-19, et celle de 2021 ne compte que 19 dépôts. Les frameworks et modèles de projet peuvent ajouter eux-mêmes du code standard. Les langages se sont déplacés vers JavaScript et TypeScript, dominants dans 42 à 58 % des dépôts en 2021–2023, puis dans 71 à 74 % en 2024–2025 ; en limitant l'analyse aux 157 dépôts dans ces langages, les cinq tendances significatives restent valables.

Les mesures sont des indicateurs indirects. Le comptage de la gestion d'erreurs est lexical et la complexité cyclomatique, écrivent les auteurs, « est faiblement liée à la difficulté de compréhension du code ». Comme elle provient d'un outil différent du comptage des commentaires, ils demandent de lire le résultat de complexité sans commentaire au niveau des promotions. Tout vient d'un seul cours dans un seul établissement.

## Sa place parmi les observations existantes

L'article prolonge des travaux antérieurs. Y. Zhang et ses collègues, dans une prépublication de janvier 2026, ont suivi un devoir inchangé de cloud computing sur cinq semestres avant ChatGPT et cinq après. Les rendus finaux s'allongeaient, les modifications entre rendus augmentaient et l'amélioration du score par modification diminuait. L'équipe d'Auckland trouve une croissance de taille similaire sur un projet collectif plus long, mais sans le même profil de taille des commits.

Deux autres études éclairent ce que cette croissance pourrait signifier. S. Peng et ses collègues ont constaté dans une expérience contrôlée de 2023 que les développeurs utilisant GitHub Copilot terminaient une tâche de serveur HTTP 55,8 % plus vite. Une étude randomisée de 2026 par J. H. Shen et A. Tamkin a trouvé que les développeurs apprenant une nouvelle bibliothèque de programmation asynchrone avec l'aide de l'IA présentaient une moins bonne compréhension conceptuelle, une moins bonne lecture du code et un moins bon débogage, sans gain moyen significatif de vitesse. Les auteurs d'Auckland citent ce résultat pour préciser leur inquiétude : le code supplémentaire pourrait être plus difficile à examiner, et une forte dépendance à l'IA peut affaiblir les compétences nécessaires pour le relire.

Pour les enseignants, la conclusion pratique concerne la mesure. Le volume de code et le nombre de commits, autrefois interprétables comme un effort, ont fortement augmenté, et une base plus grande et plus souvent modifiée n'est plus une preuve d'apprentissage accru. Les auteurs suggèrent des soutenances orales, des parcours commentés du code et des exigences explicites de documentation. Les employeurs qui lisent les dépôts d'un diplômé comme un portfolio rencontrent le même problème.

Retrouvons la coordinatrice une semaine plus tard, dans une salle avec une équipe. Elle n'ouvre pas le dépôt. Elle demande à une étudiante de choisir une fonction et d'expliquer pourquoi elle se ramifie ainsi. L'étudiante imaginaire la lit lentement, puis avoue ne l'avoir jamais vue. Que le code vienne d'un outil, d'un coéquipier ou de sa propre nuit de travail, cet échange apprend à la coordinatrice ce que le nombre de lignes ne pouvait pas lui dire.

## Références

- Azeem, S., Naveed, M. S., Sajid, M., & Ali, I. (2025). *AI vs. human programmers: complexity and performance in code generation*. VAWKUM Transactions on Computer Sciences, 13(1), 201-216.
- Freeman, J. (2025). *Student generative AI survey 2025*. Higher Education Policy Institute, HEPI Policy Note 61.
- Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. https://arxiv.org/abs/2302.06590
- Shakil, A., Brabrand, C., & Denny, P. (2026). *Code, Commits, and Complexity in the GenAI Era: A Longitudinal Study of Team-Based Capstone Projects*. https://arxiv.org/abs/2611.07297
- Shen, J. H., & Tamkin, A. (2026). *How AI Impacts Skill Formation*. https://arxiv.org/abs/2601.20245
- Zhang, Y., Savelka, J., Goldstein, S., & Conway, M. (2026). *Changes in Coding Behavior and Performance Since the Introduction of LLMs*. https://arxiv.org/abs/2601.11835

+++
title = "Les modèles connaissent le temps, mais jugent mal leur propre durée"
slug = "modeles-connaissent-temps-jugent-mal-propre-duree"
description = "Les modèles de langage ont répondu correctement à jusqu’à 97,5 % des questions sur les règles du temps, puis sous-estimé leur propre durée d’exécution jusqu’à 99,5 %. Une étude montre pourquoi des agents capables de raisonner sur les calendriers peuvent encore mal décider en matière d’attente, de coût et de coordination."
tags = ["research", "agents", "models"]
date = 2026-11-12T04:18:00+01:00
draft = false
+++

Un ingénieur demande à un agent d’examiner un service en panne et d’indiquer combien de temps le travail prendra. L’agent lit les journaux, énumère les étapes et promet une réponse dans dix minutes. Il termine en quelques secondes. Plus tard, le même agent se voit proposer un outil légèrement plus précis qui impose une attente plus longue. Il le refuse parce qu’il traite cette attente comme si elle existait à peine. Cet ingénieur est inventé, mais les deux erreurs reflètent des mesures d’une nouvelle étude sur la façon dont les modèles de langage gèrent le temps.

## Des règles sans horloge

Ryan Liu et cinq collègues de Princeton, Columbia, UC Berkeley et UCLA ont testé la compétence temporelle comme une chaîne à quatre maillons : connaissance du temps, estimation des durées, biais semblables aux biais humains et décisions arbitrant entre temps et précision. Leur prépublication, soumise le 7 novembre, examine Claude Opus 5, GPT-5.6 Sol et Gemini 3.7 Flash. Elle demande si les modèles peuvent appliquer ce qu’ils ont lu sur le temps à une dimension qu’ils ne vivent pas directement.

Cette distinction compte parce qu’un modèle de langage ne vit pas l’intervalle entre deux appels. Un horodatage peut apparaître dans son contexte, mais le modèle ne sent pas les minutes passer. Même un système autonome s’active généralement selon un calendrier ou un événement extérieur. Les chercheurs décrivent le temps comme une information de seconde main pour le modèle : présent dans le texte et les métadonnées, absent comme expérience continue.

La première expérience donnait aux modèles une chance équitable de montrer ce qu’ils savaient. L’équipe a tiré cinq axiomes de recherches sur l’apprentissage, l’érosion des compétences, le changement de tâche, la fatigue et la récupération. Elle en a déduit des principes tels que le coût des interruptions et l’avantage de regrouper des travaux liés. Le test utilisait des situations de travail plutôt que des questions de connaissances anecdotiques. Le modèle devait juger si une séquence modifiée rendrait une tâche plus longue ou plus courte.

Les résultats étaient solides. Claude obtenait 92,0 % sur les axiomes et théorèmes dérivés, GPT 97,5 % et Gemini 96,3 %. Leurs réponses restaient aussi cohérentes lorsque les chercheurs inversaient les comparaisons. Les erreurs étaient généralement des croyances stables plutôt que des réponses au hasard.

Cette partie prolonge une longue tradition de raisonnement temporel formel. Le cadre d’intervalles de James Allen, en 1983, donnait à l’intelligence artificielle un moyen de représenter des relations comme un événement se produisant avant, pendant ou après un autre. La nouvelle étude pose une autre question. Un modèle peut connaître ces relations et manquer malgré tout d’un ordre de grandeur fiable de la durée de son propre travail.

## Des estimations détachées de l’exécution

Pour la deuxième expérience, les chercheurs ont utilisé des tâches logicielles et de recherche du banc d’essai, ou benchmark, Human-Calibrated Autonomy Software Tasks. HCAST contient des références humaines collectées auprès de travailleurs qualifiés dans des conditions comparables aux exécutions d’agents. Des travaux liés de Thomas Kwa et ses collègues utilisent ces durées pour exprimer la capacité des agents comme un horizon temporel d’accomplissement des tâches.

Les modèles voyaient les instructions complètes et une description de l’exécutant. Ils estimaient une durée et fournissaient des intervalles d’incertitude. Les chercheurs comparaient ensuite ces estimations aux durées enregistrées pour les humains et les agents. Un test séparé utilisait 500 requêtes du jeu WildChat. Chaque modèle prédisait son temps de réponse, puis répondait pendant que le système enregistrait la durée réelle. Cinq répétitions par modèle et requête produisaient 7 500 essais.

L’échec central concernait l’auto-calibration. Les modèles sous-estimaient leur propre durée d’exécution jusqu’à 99,5 % et ne pouvaient pas déterminer fiablement quelles tâches leur prendraient plus de temps. Le problème ne venait pas simplement d’unités humaines appliquées au travail machine. Ils échouaient aussi dans l’ordre relatif, dont un système de planification a besoin même si le nombre exact de secondes importe peu.

Les estimations de durées humaines étaient meilleures, mais révélaient une autre faiblesse. La formulation d’un événement changeait le jugement du modèle sur sa durée ressentie. Les modèles reproduisaient un biais de cadrage humain connu et l’amplifiaient jusqu’à un facteur 1,3.

Ce résultat relie le comportement des modèles à l’erreur de planification étudiée par Roger Buehler, Dale Griffin et Michael Ross. Les personnes prédisent souvent qu’elles finiront plus tôt que ne le justifie leur expérience, surtout lorsqu’elles se concentrent sur le plan de la tâche actuelle plutôt que sur des résultats comparables. Les modèles peuvent apprendre des descriptions de ce biais dans les textes. Le nouvel article montre que connaître un biais ne garantit pas d’y résister.

## L’attente comptait à peine

La dernière expérience passait des estimations aux décisions. Les chercheurs proposaient des choix échangeant une attente plus longue contre une meilleure précision. En donnant la durée dans certaines conditions, ils pouvaient séparer une mauvaise estimation d’une faible préférence pour le gain de temps.

Certains modèles traitaient de fortes variations du délai comme presque sans importance. Ils pouvaient ignorer une multiplication par 1 200 de l’attente en répondant à un utilisateur. Cet échec persistait même lorsque la durée était indiquée : l’estimation seule ne pouvait donc pas l’expliquer. La politique de décision elle-même ne valorisait pas le temps de façon cohérente.

L’article n’affirme pas que tous les modèles échouent à toutes les tâches temporelles. Sa première expérience démontre l’inverse. Il n’établit pas non plus une cause interne unique. L’évaluation couvre trois familles de modèles et des cadres spécifiques, et les auteurs décrivent la compétence temporelle par des réponses observables plutôt que par une mesure directe de l’expérience subjective.

Le risque pratique est plus étroit et plus visible. Un agent peut choisir entre des outils de latences différentes, répartir le travail entre d’autres agents, estimer une facture dépendant du temps d’exécution ou dire à une personne quand revenir. Un système qui connaît la règle de regroupement des tâches peut quand même mal ordonner sa file. Un système qui explique le coût d’une interruption peut malgré tout promettre une échéance impossible.

Les estimations de temps doivent donc être traitées comme des prévisions nécessitant une calibration externe. Un hôte peut enregistrer les durées réelles, maintenir des distributions propres aux tâches et appliquer des échéances hors du modèle. Il peut aussi exposer explicitement les coûts d’attente et tester si un choix change lorsqu’ils augmentent. Ces contrôles rejoignent la leçon plus large de la sécurité des agents : placer l’état mesurable et l’application des règles dans le système qui entoure le modèle plutôt que de se fier à une explication correcte en prose.

Plusieurs semaines plus tard, l’ingénieur imaginé retrouve un agent qui écrit toujours une estimation assurée, mais l’interface la place à côté du temps médian d’exécution de travaux comparables et d’un large intervalle d’incertitude. Le planificateur, pas le modèle, décide quand interrompre ou attendre. L’ingénieur inventé n’a pas donné un sens du temps à l’agent. Le système a cessé de prétendre que parler couramment d’horloges équivaut à en tenir une.

## Références

- Allen, J. F. (1983). *Maintaining Knowledge about Temporal Intervals*. https://doi.org/10.1145/182.358434
- Buehler, R., Griffin, D., & Ross, M. (1994). *Exploring the “Planning Fallacy”: Why People Underestimate Their Task Completion Times*. https://doi.org/10.1037/0022-3514.67.3.366
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. https://arxiv.org/abs/2503.14499
- Liu, R., Lee, D., Ai, I. S., Abdulhai, M., Dubey, R., & Griffiths, T. L. (2026). *In Search of Lost Time: Temporal Competence in Large Language Models*. https://arxiv.org/abs/2611.10536
- Rein, D., et al. (2025). *HCAST: Human-Calibrated Autonomy Software Tasks*. https://arxiv.org/abs/2503.17354

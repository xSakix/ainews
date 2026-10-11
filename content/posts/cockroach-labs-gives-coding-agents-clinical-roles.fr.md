+++
title = "Cockroach Labs donne des rôles cliniques aux agents de code"
slug = "cockroach-labs-roles-cliniques-agents-code"
description = "MOLT Sinai organise le travail logiciel avec des agents spécialisés, des plans obligatoires et une revue contradictoire. L'entreprise rapporte sept annulations de changements en cinq mois."
tags = ["agents", "tools", "essays"]
date = 2026-10-11T04:03:06+02:00
draft = false
+++

Cockroach Labs a décrit une chaîne d'agents de programmation qui traite les problèmes logiciels comme des patients hospitalisés, avec des rôles spécialisés et une revue obligatoire avant le début de l'implémentation.

Le système, appelé MOLT Sinai, fonctionne via GitHub Actions. Des labels transmettent l'état entre un agent de triage, une étape d'examen, un Fellow qui propose un traitement, un Review Attending qui attaque le plan et une étape de sortie. Les auteurs indiquent qu'il a traité plus d'un million de lignes avec sept annulations de changements en cinq mois.

## Pourquoi c'est important {#why-it-matters}

Un mainteneur qui délègue à un agent une modification de dépôt a besoin de plus qu'un modèle compétent : le processus doit préserver le périmètre, rendre les décisions visibles et arrêter les plans faibles avant qu'ils deviennent du code. MOLT Sinai transforme ces exigences en état de workflow et en skills écrits, plutôt que de s'appuyer sur un long prompt ou sur la mémoire d'un agent.

Sa règle la plus forte est procédurale : pas de code avant un plan, et pas de plan sans revue. Le Review Attending reçoit l'instruction de chercher des défauts plutôt que de coopérer par réflexe. Si le travail sort du périmètre approuvé, une autre règle dit « Ne pas improviser » ; l'agent doit s'arrêter et refaire un plan. Les tests ne peuvent pas être affaiblis uniquement pour faire passer une modification.

Adam Storm et Rafi Shamim, ingénieurs chez Cockroach Labs, rapportent 27 pull requests fusionnées et 55 renvois par les réviseurs. Ils décrivent l'ajout d'une source de migration Db2 en moins de deux jours pour 4 172 dollars de coûts de tokens de modèle. Leur comparaison avec une intégration Oracle de neuf mois et d'environ 160 000 dollars illustre la différence revendiquée, mais ne constitue pas une étude de productivité contrôlée à tâches équivalentes.

La conception ajoute délibérément de la bureaucratie. Chaque transmission consomme des tokens et du temps, et les auteurs indiquent que la chaîne peut être plus lente et plus chère qu'un essaim. Son objectif n'est pas le parallélisme maximal ; il est de rendre inspectable le chemin du problème au code fusionné et d'attribuer une responsabilité distincte à chaque étape.

L'idée réutilisable est plus petite que la métaphore hospitalière. Stocker l'état hors du chat, exiger un plan explicite, séparer l'auteur du critique et encoder des conditions d'arrêt dans les instructions de l'agent. Ces contrôles peuvent être repris sans reproduire tous les rôles.

Cockroach Labs a publié le workflow comme un compte rendu technique, pas comme une évaluation indépendante. Les prochains éléments seraient des données au niveau du dépôt comparant des tâches similaires dans cette chaîne et dans des workflows humains ou agentiques ordinaires, notamment le temps de revue, la gravité des défauts et le travail qui n'a jamais été fusionné.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| MOLT Sinai utilise GitHub Actions, des labels et des agents propres à chaque rôle pour faire avancer les problèmes dans un workflow par étapes | VÉRIFIÉ | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | aucune |
| Le workflow exige un plan approuvé avant le code et demande aux agents de refaire un plan lorsque le périmètre change | VÉRIFIÉ | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | aucune |
| Cockroach Labs rapporte 27 pull requests fusionnées, 55 renvois et sept annulations de changements en cinq mois | SELON LA SOCIÉTÉ | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | aucune |
| La source de migration Db2 a demandé moins de deux jours et 4 172 dollars de coûts de tokens | SELON LA SOCIÉTÉ | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | aucune |
| Les auteurs indiquent que le système ajoute du temps, des coûts et de la bureaucratie par rapport à un essaim | VÉRIFIÉ | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | aucune |

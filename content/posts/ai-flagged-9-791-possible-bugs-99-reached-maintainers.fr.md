+++
title = "L'IA signale 9 791 bugs possibles ; 99 parviennent aux mainteneurs"
slug = "l-ia-signale-9-791-bugs-possibles-99-aux-mainteneurs"
description = "Un programme pilote de GitHub et Microsoft a analysé six projets open source avec l'IA et n'a transmis aux mainteneurs que ce qui a passé le tri et la vérification manuelle. Cinquante-cinq des 99 rapports ont été corrigés, et ce pilote montre qui a payé pour le filtrage."
tags = ["safety", "community", "tools"]
date = 2026-11-22T03:14:11+01:00
draft = false
+++

ImageMagick est maintenu par deux personnes. Lors du pilote, elles ont reçu 22 rapports de sécurité, dont un qui ressemblait à un problème qu'elles avaient déjà rencontré. Son résumé montrait qu'il n'en était rien et indiquait les lignes de code exactes. Les mainteneurs ont intégré un correctif en 15 minutes. En temps normal, a indiqué par la suite un mainteneur d'ImageMagick, un avis de sécurité prend « environ 30 minutes à 1 heure en moyenne pour être lu, compris et corrigé ».

C'est un gain modeste, raconté par ceux qui en ont bénéficié. Il se situe au bout d'une chaîne partie d'un ensemble bien plus vaste.

## Ce qu'a fait le pilote

Le 17 novembre, Ashley Wolf et Gregg Cochran, de GitHub, ont décrit un pilote mené avec Microsoft sur six projets open source : AutoGPT, Caddy, Express, FastMCP, ImageMagick et Netty. Le système d'analyse de Microsoft, Codename MDASH, associé à son modèle MAI Cyber, a parcouru chaque base de code et suggéré des correctifs pour ce qu'il a détecté. Le graphique présentant les résultats chiffre à 9 791 le nombre de problèmes possibles signalés sur l'ensemble des six projets.

Aucun d'entre eux n'a été transmis directement à un mainteneur. Un agent de tri par IA conçu par GitHub Security Lab a éliminé les doublons, vérifié la validité et conservé les bugs à fort impact. Des chercheurs du FORGE Lab de Microsoft ont ensuite vérifié à la main chaque résultat restant ; sept d'entre eux ont consacré environ deux jours par projet à ce travail. Au final, 99 rapports sont parvenus aux mainteneurs via le système privé de signalement de vulnérabilités de GitHub, chacun accompagné d'une preuve de concept et d'un correctif suggéré. Cela représente environ un rapport pour cent détections brutes.

Les mainteneurs ont décidé quoi corriger et à quel moment. Au 15 novembre, ils avaient corrigé 55 des rapports, et 14 de ces correctifs figuraient déjà dans une version publiée. Les mainteneurs de Caddy ont corrigé l'ensemble de leurs 22 rapports en une semaine. Ceux d'AutoGPT venaient de déployer une nouvelle vérification, qui était défaillante ; le rapport est arrivé trois jours plus tard en pointant la bonne ligne, et ils ont écrit un correctif en une journée avant de le mettre en production en moins d'une semaine.

## Le déluge auquel ce pilote répond

Le pilote répond à un phénomène que les mainteneurs décrivent depuis deux ans. Dans un billet du 26 janvier, Daniel Stenberg, qui dirige curl, a annoncé que le programme de primes aux bugs (bug bounty) du projet prendrait fin le 31 janvier. Il a écrit que le déclin du programme avait commencé lentement au second semestre 2024 et « s'est fortement accéléré en 2025 », avec une « explosion de rapports bâclés générés par IA ». Avant 2025, a-t-il indiqué, plus de 15 % des soumissions aboutissaient à des vulnérabilités confirmées. En 2025, ce taux est tombé sous les 5 % : « Pas même un sur vingt n'était réel. »

Le programme de primes avait versé plus de 100 000 dollars pour 87 vulnérabilités confirmées en près de sept ans, et Stenberg l'a qualifié de succès jusqu'à l'arrivée du bruit. Il a mis fin aux paiements afin de supprimer l'incitation à soumettre des « mensonges inventés de toutes pièces », et a invité les auteurs de signalements à utiliser le système privé de signalement de vulnérabilités de GitHub, le même canal que celui employé par le pilote. Les chiffres de HackerOne pour l'année écoulée, qu'il a publiés, montraient une forte hausse du volume de signalements reçus par curl, tandis que Ruby, Node et Rails restaient stables ou reculaient légèrement. Il a estimé que la raison de cette différence restait sujette à de plus amples spéculations.

Le billet de GitHub cite Christian Grobmeier, mainteneur de Log4j, sur l'enjeu : l'IA qui défend l'open source doit être meilleure que celle qui l'attaque. Son propre diagnostic est que l'IA a rendu la recherche de vulnérabilités potentielles « rapide et peu coûteuse », alors que leur correction exige toujours un jugement humain, qui appartient aux mainteneurs dans l'open source. Un mainteneur de Netty l'a formulé à sa manière : « Trouver des vulnérabilités n'est plus notre goulot d'étranglement. Les corriger, voilà la partie difficile. »

## Ce qu'a coûté le filtrage

Les chiffres du pilote montrent où est passé le coût. Le modèle a produit des milliers de candidats à un prix que le billet ne précise pas. Pour passer de ce volume à 99 rapports, il a fallu un agent de tri par IA, puis une équipe de sept chercheurs travaillant environ deux jours sur chaque projet. GitHub dit clairement que « le pilote a fonctionné parce que des personnes ont accompli un travail minutieux à chaque étape, et ce travail ne passe pas encore à l'échelle ».

La charge de travail n'a donc pas disparu ; elle s'est déplacée. Auparavant, un mainteneur lisait les résultats d'un outil d'analyse et déterminait ce qui était réel. Dans le pilote, une équipe de Microsoft les a lus en premier et n'a envoyé au mainteneur que ce qui avait passé ce filtre. La règle énoncée par GitHub pour quiconque dirige une IA vers le code d'autrui en découle : vérifier chaque résultat au regard de ce que le projet sait déjà et de sa politique de sécurité, le signaler en privé, joindre un correctif suggéré et laisser les mainteneurs fixer le rythme.

Il y a des raisons de lire ce résultat avec prudence, et GitHub en donne plusieurs. Six projets constituent, selon ses propres termes, « un petit échantillon ». Tous les six sont d'anciens bénéficiaires du GitHub Secure Open Source Fund, qui accorde à chaque projet 10 000 dollars et une formation à la sécurité ; ils étaient donc déjà proches de l'entreprise qui leur propose aujourd'hui davantage. Les enseignements tirés proviennent de ce que ces projets ont choisi de partager. Le taux de correction, 55 sur 99, correspond à un décompte à une date donnée et ne dit rien des 44 rapports encore ouverts ni du temps qu'ils demanderont. Le billet ne précise pas non plus combien des 9 791 signalements étaient faux, combien étaient des doublons, ni combien de vrais bugs le tri a pu écarter.

## La suite

GitHub indique qu'il proposera à chaque projet issu du programme des analyses de sécurité par IA dont les résultats seront vérifiés avant d'être signalés, et qu'il fournira GitHub Copilot Max aux anciens bénéficiaires. L'entreprise intégrera les enseignements du pilote dans son dispositif privé de signalement de vulnérabilités et dans ses avis de sécurité. Elle ajoute que les mainteneurs doivent aussi pouvoir exécuter des tests d'intégration continue (CI) sur des forks (dépôts dérivés) privés et accéder à des modèles dotés de capacités en cybersécurité, afin de tester une preuve de concept avant et après un correctif.

Le modèle utilisé pour ces analyses évolue lui aussi. Le jour même du billet de GitHub, Microsoft a annoncé MAI Cyber 2 Flash ; le pilote s'appuyait sur le modèle précédent. Microsoft affirme que le nouveau modèle obtient 92,3 % sur le banc d'essai (benchmark) CyberGym-E2E, contre 91,5 % pour GPT-6 Astra, pour moins de 2 % du coût par tâche, lors de tests menés par l'entreprise qui ont exclu 92 des 905 tâches. Il sera réservé aux produits de sécurité de Microsoft, MDASH compris, à partir de la mi-décembre. Une analyse moins coûteuse signifie davantage de détections. L'arithmétique du pilote montre que chaque centaine supplémentaire exige toujours qu'une personne la lise.

La remarque du mainteneur d'AutoGPT, citée vers la fin du billet de GitHub, va dans le même sens : il devient de plus en plus facile de livrer des fonctionnalités et, à l'avenir, maintenir un logiciel « se résumera probablement à savoir qui s'en soucie assez pour gérer la sécurité ». Pour l'équipe d'ImageMagick, le pilote s'est résumé à 22 rapports, un signalement qui semblait familier et un quart d'heure.

## Références

- Microsoft AI. (2026). *Introducing MAI Cyber 2 Flash: Leading security. Lower cost*. https://microsoft.ai/news/introducing-mai-cyber-2-flash/
- Stenberg, D. (2026). *The end of the curl bug-bounty*. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
- Wolf, A., & Cochran, G. (2026). *Maintainers don't need more AI bug reports. They need fixes.* GitHub Blog. https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

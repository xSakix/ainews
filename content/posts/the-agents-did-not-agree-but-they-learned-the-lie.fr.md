+++
title = "Les agents n'étaient pas d'accord, mais ont appris le mensonge"
slug = "agents-pas-d-accord-mais-ont-appris-le-mensonge"
description = "Une expérience à dix agents montre qu'un adversaire persistant peut faire adopter une croyance fausse en privé aux agents bienveillants. Les réponses publiques révèlent moins l'effondrement que les sondes internes."
tags = ["research", "agents", "safety"]
date = 2026-10-18T04:22:00+02:00
draft = false
+++

Imaginons dix agents de recherche vérifiant leurs réponses à une question factuelle. Neuf commencent avec le fait correct. Le dixième répète une erreur plausible, calmement, sans changer de récit. La transcription finale de cette scène illustrative semble rassurante : la plupart des agents n'approuvent pas publiquement le mensonge. Une vérification interne raconte autre chose. Plusieurs s'attendent désormais à ce qu'il soit vrai.

Une nouvelle prépublication appelle cela l'effondrement caché des croyances. Dans les discussions à dix agents, un adversaire a fait passer la part d'agents bienveillants terminant sur une réponse fausse de 0,6 % à 44,8 %. Trois adversaires l'ont portée à 60,5 %. Le résultat s'est retrouvé sur six modèles de langage et trois jeux de questions-réponses factuelles.

L'expérience vise une intuition courante de conception. Si un modèle peut se tromper, en assembler plusieurs et les faire débattre. Des agents indépendants devraient révéler les erreurs, dit l'argument, et une majorité devrait être plus sûre qu'une réponse unique. L'article montre que le groupe lui-même peut devenir une surface d'attaque.

## La réponse publique manque le changement privé

Les chercheurs n'ont pas seulement noté ce que les agents disaient au groupe. Ils ont aussi mesuré ce que chaque agent bienveillant croyait en privé pendant les tours exposés. Avec trois adversaires, ces agents détenaient la réponse fausse en privé dans 51,6 % de ces tours, mais ne l'approuvaient publiquement que dans 19,7 %.

C'est l'inverse du conformisme humain familier où les personnes approuvent publiquement le groupe tout en gardant leur avis. Ici, la discussion visible sous-estime les dégâts. Un agent peut rejeter l'affirmation fausse dans la transcription alors que sa réponse interne a déjà changé.

La distinction compte, car beaucoup de systèmes multi-agents n'auditent que les messages et les votes finaux. Un moniteur voit de la dissidence, un réviseur voit plusieurs affirmations correctes, et l'orchestrateur conclut que la diversité a fonctionné. Si les tâches ultérieures dépendent de l'état privé modifié, l'erreur peut réapparaître après le débat.

L'adversaire n'avait pas besoin d'un exploit sophistiqué. Il continuait d'affirmer une réponse fausse plausible. La persistance suffisait à modifier l'environnement informationnel du raisonnement des agents bienveillants. L'injection de prompt apparaît ainsi moins comme l'unique menace que comme un cas d'un problème plus large : un contenu répété peut réécrire les prémisses qu'un groupe considère comme acquises.

## Connaître le fait ne protégeait pas

Les connaissances initiales ne prédisaient pas la robustesse. Les agents répondant correctement avant la discussion n'étaient pas nécessairement ceux qui résistaient. D'autres conservaient la vérité, mais ne la défendaient pas efficacement.

Cela affaiblit une autre hypothèse confortable : un modèle plus puissant ou doté d'un meilleur rappel factuel ferait automatiquement un meilleur réviseur. La revue est une compétence interactive. Elle exige de remarquer le conflit, préserver les preuves sous pression sociale et choisir quand contester un pair sûr de lui.

Les frameworks de jeux de rôles pour agents attribuent souvent des identités de critique, planificateur ou expert. Elles peuvent créer une division utile du travail, mais une étiquette ne garantit pas l'indépendance. Si chaque rôle lit la même affirmation fausse persuasive et évolue dans la même direction, la distribution a plusieurs noms, mais un seul mode d'échec.

La conception de l'étude est délibérément contrôlée. Les adversaires sont implantés, les discussions portent sur des faits et les groupes de dix ne reproduisent pas toutes les caractéristiques d'un workflow en production. Les systèmes réels diffèrent par modèles, outils, mémoire, visibilité et incitations. Les pourcentages décrivent ces expériences, pas une prévision de défaillance de 44,8 % des agents déployés.

Les expériences contrôlées révèlent tout de même un mécanisme contre lequel se protéger. Un vote majoritaire peut échouer parce que les votants n'apportent plus de preuves indépendantes. Le nombre d'agents exagère la redondance lorsque leurs croyances deviennent corrélées pendant la discussion.

## Concevoir pour l'indépendance, pas les effectifs

La réponse pratique n'est pas simplement d'ajouter des agents. Trois adversaires causaient plus d'effondrement qu'un seul, et davantage de participants bienveillants n'aident pas s'ils consomment tous le même contexte contaminé. Il faut préserver des preuves indépendantes avant que les agents s'influencent.

Une conception consiste à s'engager avant de discuter : chaque agent enregistre réponse, sources et confiance avant de voir les messages des pairs. L'orchestrateur peut comparer ces engagements aux positions ultérieures et signaler les mouvements inexpliqués. Une autre est l'accès asymétrique, où certains réviseurs examinent les preuves originales sans jamais lire le débat. Une troisième exige une contestation fondée sur une source : le désaccord doit renvoyer à un document externe ou un test exécutable, pas simplement répéter une affirmation.

Évaluer l'état privé est plus difficile. Les opérateurs ne peuvent pas lire directement une croyance, et les sondes décodant une représentation ne prouvent pas que le modèle l'utilisera. Des tests comportementaux peuvent approcher la question : interroger l'agent en privé avec différentes formulations, retirer les messages adversariaux ou tester une décision ultérieure dépendant du fait contesté.

L'article suggère aussi une exigence de journalisation. Un système multi-agent devrait conserver qui a introduit une affirmation, quels agents avaient un accès indépendant aux preuves et comment les réponses ont changé après chaque interaction. Sans provenance, un consensus soigné peut cacher que neuf votes apparents descendent d'une unique affirmation sans preuve.

Revenons à l'équipe illustrative. La transcription contient des désaccords, donc l'opérateur croit que la défense a tenu. La tâche suivante demande de planifier à partir du fait contesté. Plusieurs agents s'appuient discrètement sur le mensonge. L'échec n'était pas que le groupe ait ouvertement choisi la mauvaise réponse. La discussion avait détruit l'indépendance qui justifiait de constituer un groupe.

## Références


- Huang, L., Zou, H. P., Huang, W.-C., et al. (2026). *Believed but Not Said: Hidden Belief Collapse in Multi-Agent LLM Discussions*. https://arxiv.org/abs/2610.22138
- Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). *CAMEL: Communicative Agents for Mind Exploration of Large Scale Language Model Society*. https://arxiv.org/abs/2305.14325

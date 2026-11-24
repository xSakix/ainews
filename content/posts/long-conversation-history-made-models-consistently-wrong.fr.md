+++
title = "Un long historique de conversation enferme les modèles dans l'erreur"
slug = "un-long-historique-enferme-les-modeles-dans-l-erreur"
description = "Une étude sur 100 tours montre que l'historique complet fait chuter la précision du suivi d'état d'environ 60 % à 10 %. Des résumés vérifiés préservent les réponses, tandis que les indicateurs courants font souvent paraître stable un système défaillant."
tags = ["research", "models"]
date = 2026-11-18T04:00:29+01:00
draft = false
+++

Marta vérifie l'assistant d'inventaire avant la prise de poste du matin. Le tableau de bord est au vert. Ses réponses s'accordent entre elles, son ton reste posé et les totaux de l'entrepôt ont à peine bougé au fil des cinq dernières questions. Puis elle compare un chiffre avec le registre. L'assistant a reconduit la même erreur dans chacune de ses réponses.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

Une prépublication (preprint) d'Ali Şenol, de l'université de Tarse, teste cette défaillance silencieuse. Dans des conversations de 100 tours portant sur des budgets évolutifs, des stocks, des contenants de laboratoire et des jalons de projet, la précision des modèles est tombée d'environ 60 % à environ 10 % en vingt tours lorsque la transcription intégrale restait dans le contexte. Un résumé d'état vérifié par un solveur a maintenu la précision à plus de 50 points de pourcentage au-dessus. Les signes habituels d'un raisonnement ordonné n'ont pas fourni d'alerte fiable.

## La transcription devient une partie du problème

Les longues conversations demandent à un modèle d'accomplir deux tâches à la fois. Il doit résoudre le problème du moment et décider de ce qu'il convient de retenir de tout ce que l'utilisateur et lui-même ont dit auparavant. La seconde tâche devient plus difficile lorsque l'état change, qu'un fait antérieur est corrigé ou que le modèle a déjà commis une erreur.

Des travaux antérieurs avaient isolé une partie de ce problème. Dans *LLMs Get Lost in Multi-Turn Conversation*, Philippe Laban et ses coauteurs avaient découpé des tâches complètes en fragments livrés sur plusieurs tours. Les modèles s'engageaient souvent trop tôt sur une réponse. Leurs performances baissaient alors même que le problème sous-jacent n'avait pas changé. Cette étude utilisait des tâches dérivées de GSM8K, le jeu de données de 8 500 problèmes de mathématiques de niveau scolaire introduit par Karl Cobbe et ses collègues en 2021.

Şenol a d'abord posé une question causale plus étroite : le fait de conserver les propres réponses du modèle dégrade-t-il la réponse finale ? Il a sélectionné 48 tâches mathématiques fractionnées comportant de quatre à neuf tours. GPT-4o-mini, Llama 4 Scout et Mistral 7B ont chacun reçu deux versions. L'une conservait le dialogue. L'autre reconstruisait un nouveau prompt (instruction) à partir des informations fournies par l'utilisateur en omettant les réponses précédentes de l'assistant.

Les 11 382 appels aux modèles sont tous arrivés à terme. GPT-4o-mini a résolu 33 des 48 tâches avec ses propres réponses sous les yeux, contre 43 avec un préfixe neuf, soit une baisse de 21 points de pourcentage. Mistral 7B est passé de 17 tâches réussies à trois, soit une chute de 29 points. Llama 4 Scout a évolué dans le même sens, mais son écart de dix points n'a pas atteint le seuil statistique retenu par l'étude.

L'erreur de Mistral prenait une forme visible. En présence de ses réponses antérieures, le modèle arrivait souvent au dernier tour en affirmant encore avoir besoin d'informations supplémentaires. Le prompt neuf contenait les mêmes faits et produisait une réponse.

## Cent tours avec un registre exact

La première expérience s'arrêtait après neuf tours au maximum. Elle ne permettait pas non plus de distinguer une question tardive plus difficile d'une dégradation causée par l'allongement de la conversation. Şenol a donc conçu CDR-Stream, un banc d'essai (benchmark) dans lequel chaque tour met à jour un état et pose une question appelant une réponse exacte.

Le benchmark couvre quatre types d'état : un registre budgétaire, un inventaire d'entrepôt, un protocole de laboratoire et une chaîne de jalons de projet. Un message utilisateur peut ajouter une livraison, corriger une écriture antérieure ou déplacer une quantité d'un lieu à un autre. Il peut aussi contenir des phrases de distraction. La question porte sur une somme, une différence, un décompte au-dessus d'un seuil, un maximum, un résultat hypothétique ou une part.

Un solveur exact produit la bonne réponse à chaque tour. Une échelle à douze niveaux fait varier une seule source de difficulté à la fois, comme le nombre d'événements ou la complexité d'une mise à jour. L'étude a calibré cette échelle séparément pour chaque modèle, puis a figé les paramètres. Ce choix rend l'expérience utile pour mesurer le déclin au sein d'un même modèle, mais implique que les scores bruts ne doivent pas servir à classer les modèles les uns par rapport aux autres.

GPT-4o-mini, Llama 3 70B et Gemma 3 12B ont chacun reçu trente dialogues de 100 tours. Dans une branche de l'expérience, le prompt contenait l'intégralité de la conversation. Dans l'autre, il contenait un résumé vérifié de l'état courant ainsi que le nouveau tour de l'utilisateur. Les deux branches utilisaient les mêmes consignes et le même format de réponse.

Les courbes obtenues avec l'historique complet se superposaient presque. La précision démarrait autour de 0,6 lors des cinq premiers tours, chutait à environ 0,3 entre le sixième et le vingtième tour, puis se stabilisait entre 0,08 et 0,11 pendant les quatre-vingts tours restants. Même lorsque les questions restaient au niveau le plus simple, la précision avec historique complet après le vingtième tour oscillait entre 0,10 et 0,14.

Le résumé vérifié a inversé le résultat. Sur ces mêmes conversations simples, il a maintenu la précision entre 0,82 et 0,86. Sur l'ensemble des cinq profils de difficulté, l'avantage moyen atteignait 0,521 pour GPT-4o-mini, 0,545 pour Llama 3 et 0,588 pour Gemma 3. Lorsqu'une séquence revenait de questions difficiles à des questions simples, les performances fondées sur le résumé remontaient. Celles avec historique complet ne remontaient pas.

## Une réponse stable peut être une erreur stable

Un opérateur ne dispose pas du solveur exact employé dans l'expérience. Un système déployé a besoin d'un signal indiquant que sa réponse courante a cessé de refléter la réalité. L'étude a testé plusieurs candidats : la cohérence entre des réponses échantillonnées, la cohérence logique, la similarité sémantique, une mesure appariée de préparation et des détecteurs standard de changement dans un flux.

Aucun n'a donné d'alerte robuste d'un modèle à l'autre. Dans l'expérience mathématique plus courte, les signaux de qualité mesurés ne présentaient aucune association statistiquement détectable avec l'échec final une fois pris en compte le numéro de tour, l'information révélée et la longueur du contexte. L'un des signaux ne couvrait que 29 tâches sources, si bien que l'article ne prétend pas écarter toute association faible.

L'étude sur cent tours a fait apparaître un phénomène plus préoccupant. La cohérence et la constance variaient bien moins que la précision. La stabilité augmentait parce que les modèles répétaient des réponses erronées semblables. Un dispositif de surveillance qui valorise l'accord entre réponses peut donc gagner en confiance à mesure que l'estimation de l'état sous-jacent se dégrade.

Şenol délimite prudemment la portée de cette conclusion. Les deux études reposent sur l'arithmétique et le suivi d'état exact, ce qui rend la justesse observable mais ne représente pas toutes les conversations ouvertes. Les ensembles de modèles diffèrent d'une expérience à l'autre et n'incluent pas les systèmes de pointe actuels les plus puissants. Gemma 4 31B s'est montré trop précis pour l'échelle de difficulté prévue, de sorte qu'un test valide exigerait des tâches plus ardues plutôt que davantage de répétitions de celles-ci.

L'expérience longue manque en outre d'une comparaison limitée aux seuls messages de l'utilisateur. Elle mesure donc la défaillance liée à l'historique complet, mais ne peut attribuer une part précise aux réponses antérieures de l'assistant, à la longueur du contexte ou à la charge croissante de l'état. La surveillance fondée sur les répétitions n'était complète que pour GPT-4o-mini. Plusieurs analyses de surveillance relevaient de l'exploration plutôt que des tests confirmatoires figés à l'avance.

## L'état doit vivre hors de la transcription

L'intervention étudiée dans l'article reste modeste. Elle ne dote pas le modèle d'une meilleure mémoire. Elle supprime le besoin de reconstruire le présent à partir de toute la conversation en fournissant un état compact vérifié par un programme externe.

Cette architecture sépare la preuve du récit. La transcription peut rester accessible pour un audit, tandis que le prompt actif reçoit le registre courant, l'inventaire ou l'état de la tâche. Şenol propose également des vérifications entre sessions distinctes et des requêtes contrefactuelles, car un détecteur enfermé dans un même flux en dégradation risque de ne jamais disposer d'une référence saine.

L'article laisse ouvert un problème d'ingénierie difficile. Ses résumés provenaient d'un solveur exact. La plupart des systèmes réels n'en possèdent pas, et un modèle qui rédige son propre fichier d'état peut préserver une erreur aussi efficacement qu'il préserve un fait. La question reste de savoir comment un système peut maintenir et vérifier cet état externe sans transformer discrètement le résumé en une autre réponse non fiable.

Marta ouvre le fichier d'état à côté du chat. Un transfert d'entrepôt y figure une seule fois, accompagné de son événement source et de sa correction. La transcription contient toujours les cinq réponses concordantes de l'assistant. Elle les laisse aux archives et transmet le registre vérifié avec la question suivante.

## Références

- Cobbe, K., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2026). *LLMs Get Lost in Multi-Turn Conversation*. https://arxiv.org/abs/2505.06120
- Şenol, A. (2026). *The Silent Cost of Conversation History in LLM Reasoning*. https://arxiv.org/abs/2611.20071

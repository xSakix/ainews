+++
title = "La récompense sélectionne mieux, sans améliorer le raisonnement"
slug = "recompense-selectionne-mieux-sans-ameliorer-raisonnement"
description = "Une nouvelle étude a suivi chaque point de contrôle de l’apprentissage par renforcement d’un petit modèle. Sa précision a progressé, mais il n’a pas développé de représentation interne plus fine des erreurs de raisonnement : il sélectionnait mieux les solutions qu’il connaissait déjà."
tags = ["research", "models"]
date = 2026-11-08T04:18:00+01:00
draft = false
+++

Imaginons un élève capable de résoudre un problème de mathématiques une fois sur deux. Un professeur récompense chaque bonne réponse sans commenter les étapes. Après des semaines de pratique, l'élève répond correctement plus souvent. Il est tentant d'en conclure qu'il a progressé en mathématiques. Pourtant, dans cette classe imaginaire, un examen plus approfondi retrouve le même répertoire de bonnes et de mauvaises approches qu'auparavant. L'élève est devenu meilleur pour choisir parmi elles.

## Suivre l'ensemble de l'entraînement

Cette distinction est au cœur de *RLVR Sharpens the Pencil, Not the Mind*, une nouvelle prépublication de Shreeyam Bangera et Manya Gupta. Les chercheurs suivent OLMo-2-1B à travers 13 points de contrôle d'apprentissage par renforcement à récompenses vérifiables, ou RLVR. Au lieu de comparer uniquement le modèle avant et après l'entraînement, ils examinent ce qui change en cours de route.

Le RLVR a pris de l'importance parce qu'une réponse correcte à un problème de mathématiques ou de programmation peut être vérifiée automatiquement. Un système d'entraînement génère des solutions, attribue des récompenses et augmente la probabilité des comportements qui les ont obtenues. DeepSeek-R1 a montré jusqu'où cette approche pouvait aller : son modèle R1-Zero a amélioré ses performances en mathématiques et en programmation par apprentissage par renforcement, sans phase préalable d'affinage supervisé.

Les gains visibles ont soulevé une question plus difficile. L'entraînement par récompense enseigne-t-il au modèle de nouvelles capacités de raisonnement, ou rend-il ses capacités existantes plus accessibles ? La seconde explication est appelée affinage. Un modèle préentraîné peut déjà disposer d'un bon chemin de résolution, mais lui attribuer une probabilité trop faible pour l'emprunter dès la première tentative.

Bangera et Gupta exploitent l'ouverture d'OLMo pour tester cette hypothèse tout au long de l'entraînement. Ai2 publie les points de contrôle intermédiaires de l'entraînement RLVR du modèle à un milliard de paramètres. Les auteurs les évaluent sur GSM8K, un jeu de 8 500 problèmes mathématiques rédigés de niveau élémentaire, introduit par Karl Cobbe et ses collègues.

## Un accès plus fiable aux anciennes solutions

La précision au premier essai passe de 58,0 % au début de l'entraînement à 61,3 % à la fin. L'augmentation est réelle, mais modeste. Une mesure plus révélatrice consiste à soumettre 256 fois le même problème au modèle et à vérifier si l'une des réponses contient une solution correcte. Cette couverture des solutions passe de 94,5 % à 96,9 %.

Le modèle de base pouvait donc produire une réponse valide à presque tous les problèmes avant le RLVR. L'entraînement a rendu ces chemins valides plus susceptibles d'apparaître dès le premier essai. Il n'a pas ouvert un vaste nouveau domaine de problèmes que le modèle ne pouvait résoudre qu'après coup.

La couverture des solutions ne révèle pas ce que le modèle représente en interne. Un modèle peut déjà générer occasionnellement la bonne réponse et tout de même acquérir une meilleure conception du raisonnement pendant l'entraînement. Les chercheurs testent cette possibilité en insérant trois types d'erreurs dans des traces de résolution. Ils entraînent ensuite des sondes linéaires sur les activations du modèle pour identifier ces erreurs.

Les performances des sondes restent entre 0,798 et 0,840 d'AUROC sur les 13 points de contrôle. La variation est inférieure à l'intervalle de confiance. Dans ce test, le modèle ne devient pas meilleur pour distinguer en interne un raisonnement correct d'une erreur introduite volontairement.

Un signal interne change nettement. Une sonde distingue les premiers des derniers points de contrôle avec une AUROC de 0,93 au token de réponse finale. Appliquée aux tokens des étapes de raisonnement, la même sonde obtient un résultat proche du hasard. L'entraînement semble réorganiser davantage la décision en fin de résolution que les représentations utilisées pour la construire.

## Ce que le résultat montre et ne montre pas

Le titre de l'article trace une frontière nette, mais l'expérience est restreinte. Elle porte sur une seule famille de modèles à un milliard de paramètres, un seul banc d'essai mathématique et un seul entraînement RLVR. Les sondes linéaires peuvent manquer des informations présentes sous une forme qu'elles ne savent pas décoder. GSM8K récompense une réponse finale courte et ne représente pas les tâches ouvertes dont la justesse est difficile à vérifier.

Les auteurs ne montrent pas non plus que le RLVR ne crée jamais de nouvelles capacités de raisonnement. Leurs observations étayent une affirmation plus limitée : dans cet entraînement, le gain observé s'explique mieux par une meilleure sélection des chemins de résolution existants que par une représentation interne plus précise des erreurs testées.

Cette réserve compte, car le RLVR est souvent décrit à travers son comportement observable. Un modèle produit des chaînes plus longues, essaie d'autres approches et aboutit à davantage de réponses correctes. Ces changements peuvent ressembler à une compréhension nouvelle. L'analyse des points de contrôle montre qu'une sortie peut s'améliorer alors qu'une sonde du raisonnement reste presque inchangée.

Le résultat explique aussi pourquoi générer plusieurs réponses reste utile après l'apprentissage par renforcement. Si les connaissances d'un modèle couvrent davantage de solutions que sa première réponse ne le révèle, des essais répétés dévoilent des capacités qu'un seul passage manque. Le RLVR modifie la distribution de probabilité de ces essais. Il ne fait pas de la précision au premier essai une mesure complète des connaissances du modèle.

## Entraîner le processus

Les réponses finales vérifiables sont attrayantes parce qu'elles sont peu coûteuses et objectives. Un nombre est correct ou ne l'est pas. Un programme réussit ses tests ou les échoue. La récompense n'a pas besoin d'indiquer quelle étape de raisonnement a aidé, quel raccourci échouera ailleurs ou si le modèle a reconnu sa propre erreur.

Entraîner une meilleure représentation des erreurs exigerait un signal plus proche du processus. Il pourrait s'agir d'étapes intermédiaires vérifiées, d'erreurs introduites pour piéger le modèle, d'une supervision du processus ou de tâches récompensant une autocorrection bien calibrée. Chaque option coûte plus cher que la vérification d'une réponse finale et introduit son propre problème de jugement.

L'article ne prescrit aucune de ces méthodes. Il fournit un diagnostic réutilisable dans de futurs travaux : conserver les points de contrôle intermédiaires, mesurer la couverture des solutions plutôt que les seules premières tentatives, et sonder les tokens où se déroule le raisonnement séparément de celui qui fixe la réponse. Un score avant-après fait perdre le chemin qui explique le gain.

Cette leçon dépasse les mathématiques. Les agents reçoivent des récompenses pour des tickets terminés, des tests réussis ou des appels d'outils fructueux. Si l'entraînement améliore surtout la sélection parmi les comportements existants, l'agent peut paraître plus capable sans mieux reconnaître un plan défectueux. L'évaluation doit alors porter à la fois sur les résultats et sur les défaillances du processus.

Retrouvons l'élève imaginaire une semaine plus tard. Les bonnes réponses arrivent désormais plus vite et la courbe du professeur monte. Avant de passer à un contenu plus difficile, celui-ci place une erreur plausible dans une solution rédigée et demande à l'élève de la trouver. L'hésitation qui suit mesure quelque chose que la courbe des récompenses ne mesurait pas.

## Références

- Ai2. (2025). *OLMo-2-0425-1B-SFT model card*. https://huggingface.co/allenai/OLMo-2-0425-1B-SFT
- Bangera, S., & Gupta, M. (2026). *RLVR Sharpens the Pencil, Not the Mind*. https://arxiv.org/abs/2611.02574
- Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- DeepSeek-AI. (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. https://arxiv.org/abs/2501.12948

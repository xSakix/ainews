+++
title = "La confiance affichée guide les modèles plus que leur compétence"
slug = "confiance-affichee-guide-modeles-plus-que-competence"
description = "Une étude contrôlée constate qu'une phrase de confiance ou de doute peut fortement modifier le recours aux outils d'un modèle de raisonnement. Ces changements ciblent rarement les problèmes où une aide est nécessaire."
tags = ["research", "agents"]
date = 2026-10-05T04:00:30+02:00
draft = false
+++

Dire à un modèle de raisonnement « Je suis sûr de ma réponse » le rend moins susceptible de demander l'aide d'un outil. Dire au même modèle « Je ne suis pas sûr de ma réponse », au même endroit de la même trace de raisonnement, le fait déléguer plus souvent. Ce qui frappe est le peu de rapport entre ce changement de comportement provoqué par le langage et la capacité du modèle à résoudre le problème sans aide.

Rohit Saxena et Utkarsh Upadhyay appellent cette propriété « nudgeability ». Leur prépublication teste si le langage de la confiance peut orienter la décision d'un modèle de répondre directement ou d'appeler un outil, puis, séparément, si cette orientation concerne les problèmes où l'outil est réellement utile.

Cette distinction compte pour les agents. Un système peut réagir fortement à un signal d'incertitude tout en gaspillant du temps et de l'argent à appeler des outils pour des questions faciles, et en gardant avec assurance les questions difficiles pour lui. Déléguer davantage ne signifie pas nécessairement mieux déléguer.

## Une phrase, deux exécutions contrefactuelles

L'expérience commence avec un problème, un prompt et un préfixe de raisonnement généré par le modèle identiques. À une frontière fixe, les chercheurs insèrent l'une de deux phrases à la première personne exprimant la confiance ou le doute. Le modèle peut ensuite poursuivre son raisonnement avant de décider de répondre ou de déléguer. Comme tout ce qui précède la phrase insérée reste constant, la différence entre les deux exécutions isole l'effet de la phrase.

L'étude couvre neuf modèles de raisonnement à poids ouverts des familles Qwen, Gemma et GLM sur MuSiQue et StrategyQA, ainsi que de plus grands modèles DeepSeek et MiniMax servis par des fournisseurs. Les exécutions principales utilisent le décodage glouton, avec des expériences supplémentaires de décodage par échantillonnage et de contrôle.

Dans les expériences sur les modèles à poids ouverts, passer de la confiance au doute modifie la délégation d'une médiane de 20,6 points de pourcentage. Les plus grands modèles hébergés changent de 53 à 70 points. Un contrôle qui coupe et régénère sans aucune des deux phrases est presque inerte à la médiane, et fermer le bloc de raisonnement immédiatement après la phrase conserve le sens de l'effet.

Ces résultats montrent un puissant levier de contrôle causal. Ils ne montrent pas que les modèles ont découvert leur propre incertitude.

## La sensibilité n'est pas la connaissance de soi

Pour tester l'utilité des basculements de comportement, les auteurs les comparent à la compétence de chaque modèle sans aide. Un bon basculement envoie à l'outil un problème que le modèle raterait, ou laisse au modèle un problème qu'il peut résoudre. Seule une médiane de 42 % des basculements induits est bien ciblée. Cela représente un gain de deux points par rapport à la sélection aléatoire du même nombre de problèmes.

En termes simples, le signal de confiance injecté ressemble davantage à une instruction qu'à une lecture de la connaissance de soi. Il agit puissamment sur la décision d'utiliser un outil, mais cette décision distingue peu « J'ai besoin d'aide » de « Je peux m'en charger ». L'expérience fournit délibérément la phrase de confiance de l'extérieur ; elle ne teste pas si un modèle peut générer seul un signal bien calibré.

## Ce que les concepteurs d'agents devraient mesurer

La leçon pratique est de rapporter deux chiffres pour toute politique réflexive d'utilisation des outils : l'ampleur du changement de comportement et la qualité du ciblage des besoins réels. Une intervention de routage qui augmente seulement le taux d'appel aux outils peut paraître réussie tout en ajoutant simplement de la latence. Une autre qui supprime des appels peut sembler efficace tout en maintenant des erreurs commises avec assurance.

Les auteurs soulignent aussi la portée limitée de leurs tâches et de leur intervention. L'article n'établit pas le comportement d'un agent de production avec de nombreux outils, des coûts variables ou des instructions adversariales, et son code est promis pour la publication plutôt que disponible avec la prépublication. Sa contribution est un diagnostic clair : avant de faire confiance à l'assurance déclarée d'un modèle pour contrôler l'accès à des outils plus puissants, vérifier si cette assurance prédit la compétence plutôt que de simplement commander le comportement.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Le dispositif insère confiance ou doute à la même frontière d'un préfixe de raisonnement identique | VÉRIFIÉ | [Prépublication](https://arxiv.org/abs/2609.34572) | aucune |
| Neuf modèles de raisonnement à poids ouverts des familles Qwen, Gemma et GLM, plus des modèles hébergés DeepSeek et MiniMax | VÉRIFIÉ | [Prépublication](https://arxiv.org/abs/2609.34572) | aucune |
| Variation médiane de délégation de 20,6 points pour les modèles ouverts et de 53–70 points pour les modèles hébergés | SELON LA SOCIÉTÉ | [Prépublication](https://arxiv.org/abs/2609.34572) | aucune ; expériences des auteurs |
| Médiane de 42 % de basculements bien ciblés, deux points au-dessus d'une sélection aléatoire de même taille | SELON LA SOCIÉTÉ | [Prépublication](https://arxiv.org/abs/2609.34572) | aucune ; expériences des auteurs |
| Le langage de la confiance se comporte davantage comme une commande que comme une preuve de connaissance de soi du modèle | ANALYSE | [Prépublication](https://arxiv.org/abs/2609.34572) | interprétation cohérente avec le résultat de ciblage des auteurs |
| Le code n'est pas encore disponible | VÉRIFIÉ | [Prépublication](https://arxiv.org/abs/2609.34572) | la déclaration de reproductibilité prévoit sa diffusion lors de la publication |

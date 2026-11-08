+++
title = "Une même réponse peut cacher une croyance différente"
slug = "meme-reponse-croyance-differente"
description = "Une nouvelle étude montre que des modèles de langage peuvent produire des prédictions identiques tout en accordant un poids radicalement différent au prochain élément de preuve. Pour les agents, les évaluateurs et les systèmes à forts enjeux, des sorties concordantes ne suffisent pas."
tags = ["research", "models", "agents"]
date = 2026-11-07T04:18:00+01:00
draft = false
+++

Imaginons deux modèles de risque qui évaluent tous deux à 30 % la probabilité de défaillance d'un fournisseur. Une équipe achats les considérerait normalement comme interchangeables. Puis arrive un rapport signalant un retard de paiement. Un modèle passe à 35 % ; l'autre bondit à 70 %. Cette scène est illustrative, mais la défaillance qu'elle décrit fait l'objet d'une nouvelle prépublication : une réponse identique aujourd'hui peut dissimuler une réponse différente à la question suivante.

*Same Answer, Different Future*, signé par des chercheurs de l'UC Berkeley et de Google DeepMind, étudie ce que font les modèles de langage une fois leurs prédictions présentes égalisées. Son résultat central est simple et dérangeant. Un accord à un instant donné n'implique pas un accord sur la façon dont de nouveaux éléments doivent modifier cette prédiction. Un évaluateur qui ne vérifie que la réponse actuelle peut donc certifier des systèmes dont le comportement futur diffère sensiblement.

## Égaliser la prédiction, changer le chemin

Les auteurs utilisent une tâche de Bernoulli contrôlée. Un modèle voit une séquence d'observations binaires et prédit la probabilité de la suivante. Comme la mise à jour correcte est mathématiquement claire, l'expérience permet de distinguer la réponse formulée par le modèle du poids qu'il accorde aux nouveaux éléments.

Sur trois modèles à poids ouverts, les chercheurs produisent des prédictions initiales identiques par quatre chemins textuels et deux interventions sur les activations. Ces chemins peuvent amener le modèle à la même probabilité tout en véhiculant des descriptions, des résumés ou des hypothèses différents sur les observations. Les interventions internes modifient directement les activations. Une fois les sorties initiales égalisées, les modèles reçoivent les mêmes nouvelles observations.

Leurs mises à jour divergent.

L'article mesure un « poids effectif des éléments de preuve » : l'ampleur du déplacement de la prédiction face à de nouvelles données. Des modèles partant de la même probabilité peuvent se comporter comme s'ils avaient vu des quantités très différentes d'éléments antérieurs. Un modèle qui agit avec une grande certitude bouge peu ; celui qui traite sa réponse actuelle comme faiblement étayée bouge beaucoup plus. Le nombre visible ne révèle pas dans quel état se trouve le modèle.

Ce n'est pas seulement un effet de formulation. Les auteurs rapportent que les résumés ne varient que faiblement avec le nombre d'observations qu'ils prétendent représenter. Dire à un modèle qu'une statistique résume un grand échantillon ne donne pas de manière fiable à cette statistique l'inertie qu'un observateur bayésien lui attribuerait. À l'inverse, demander explicitement au modèle d'exposer son raisonnement peut modifier de plusieurs ordres de grandeur le poids effectif qu'il accorde aux éléments de preuve. Demander davantage d'explications n'est pas toujours une mesure passive : cela peut changer le processus mesuré.

## Pourquoi un pilotage ponctuel est fragile

Les expériences sur les activations rendent le résultat particulièrement pertinent pour le contrôle des modèles. Une intervention ciblée peut déplacer une prédiction immédiate vers la valeur souhaitée. Mais une fois que le modèle reçoit de nouveaux éléments, l'effet s'estompe souvent. L'intervention a aligné l'état affiché sans nécessairement modifier la règle de mise à jour qui l'a produit.

Cette distinction compte pour tout système qui agit dans la durée. Un agent de service client peut respecter une politique de remboursement lors d'un test, puis interpréter autrement un message ambigu en production. Un modèle de négociation financière peut partager une estimation de risque avec son remplaçant, mais réagir plus fortement au prochain signal du marché. Un assistant médical peut correspondre à une probabilité calibrée dans un banc d'essai, puis se mettre à jour de manière incohérente lorsqu'un nouveau symptôme est ajouté.

L'article ne démontre aucune de ces défaillances. Sa tâche est volontairement restreinte, et une estimation contrôlée de probabilité est bien plus simple que la médecine, les marchés ou l'assistance client. Ces exemples sont des conséquences à tester, pas des affirmations déjà prouvées par les auteurs. L'expérience établit toutefois la propriété manquante : des sorties présentes identiques ne permettent pas d'identifier des trajectoires futures identiques.

## L'évaluation a besoin de trajectoires

La plupart des évaluations de modèles sont des instantanés. Elles présentent une entrée, enregistrent une sortie et la notent par rapport à une référence ou à un évaluateur. Les tests de calibration vont au-delà de la précision brute en demandant si les prédictions à 70 % sont correctes environ 70 % du temps. Pourtant, même un instantané calibré peut masquer la dynamique mise au jour ici. Deux systèmes peuvent être aussi précis et aussi bien calibrés sur une distribution donnée, tout en réagissant différemment à l'arrivée séquentielle de nouveaux éléments.

Des travaux antérieurs sur la révision des croyances des modèles de langage ont déjà montré des mises à jour incohérentes lorsque des faits se contredisent ou que le contexte change. La recherche sur la cohérence probabiliste demande si un ensemble de croyances exprimées respecte des contraintes mathématiques élémentaires. Le nouvel article ajoute une dimension temporelle : même lorsque la croyance actuelle est maintenue fixe, le chemin qui l'a induite influe sur la suite.

Une évaluation plus solide testerait donc des courbes de mise à jour. Elle fournirait aux modèles les mêmes éléments initiaux sous différentes représentations, égaliserait leurs prédictions exprimées, puis leur soumettrait des observations supplémentaires identiques. Le score porterait non seulement sur la réponse finale, mais aussi sur la sensibilité à la taille de l'échantillon, à l'ordre, au cadrage et à la manière de solliciter une réponse. Pour un agent, le test équivalent consisterait à rejouer une tâche avec le même état opérationnel atteint à travers des historiques différents.

C'est aussi une raison de préserver la provenance. Si une application ne stocke que le dernier résumé du modèle, elle peut éliminer des informations nécessaires pour interpréter les mises à jour futures. Un registre structuré des observations, de leurs sources et de la transformation ayant produit le résumé offre à l'inférence suivante une base plus solide qu'une phrase affirmant une certitude. Les systèmes de mémoire ne devraient pas seulement retenir des conclusions ; ils devraient conserver suffisamment de structure des preuves pour que ces conclusions puissent être révisées de manière prévisible.

## Ce que les concepteurs peuvent faire dès maintenant

L'article ne propose pas de correctif universel, mais suggère trois garde-fous pratiques.

Premièrement, tester des séquences plutôt que des échanges isolés. Ajouter de nouveaux éléments après la réussite du cas initial et comparer l'ampleur des changements de réponse entre prompts équivalents.

Deuxièmement, ne pas supposer qu'une déclaration verbale de confiance représente une taille d'échantillon. Si le nombre d'observations compte, le conserver sous forme de donnée structurée et calculer les mises à jour simples hors du modèle lorsque c'est possible.

Troisièmement, traiter la sollicitation du raisonnement et le pilotage des activations comme des interventions, pas comme des fenêtres transparentes. Une demande de chaîne de pensée, un prompt de résumé ou une modification interne peut altérer le comportement ultérieur. La question pertinente n'est pas seulement de savoir si la réponse immédiate s'améliore, mais si le changement persiste avec de nouvelles informations.

Des travaux connexes sur l'enseignement bayésien offrent un contraste utile. Un bon enseignant choisit des exemples en comprenant comment l'apprenant va mettre à jour ses connaissances. Un système dont la règle de mise à jour change selon la représentation complique cet enseignement : le même exemple peut avoir un poids différent selon le chemin caché qui a conduit l'apprenant à sa réponse actuelle.

## Le prochain rapport

Retrouvons les deux modèles de risque fournisseur. L'équipe achats sait désormais que 30 % n'est pas une description complète de l'état. Avant d'approuver l'un ou l'autre, elle rejoue le rapport de retard de paiement après plusieurs historiques équivalents et trace toute la courbe de mise à jour. Cette scène finale est elle aussi illustrative. La rigueur qu'elle propose ne l'est pas.

Pour les systèmes qui font une prédiction puis s'arrêtent, l'accord sur un instantané peut suffire. Les agents s'arrêtent rarement. Ils mémorisent, reçoivent des éléments, révisent leurs plans et agissent à nouveau. Dès qu'un modèle a un avenir, la qualité de sa prochaine mise à jour doit entrer dans l'évaluation de sa réponse d'aujourd'hui.

## Références

- *Same Answer, Different Future: Language Models Hide Their Belief Updating* — https://arxiv.org/abs/2611.07913
- *Belief Revision in Large Language Models* — https://aclanthology.org/2024.emnlp-main.586/
- *From Drift to Coherence: Probabilistic Beliefs in Language Models* — https://proceedings.mlr.press/v306/kim26ah.html
- *Bayesian teaching and learning with language models* — https://www.nature.com/articles/s41467-025-67998-6

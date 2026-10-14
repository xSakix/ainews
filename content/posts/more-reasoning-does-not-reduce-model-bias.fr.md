+++
title = "Plus de raisonnement ne réduit pas les biais des modèles"
slug = "plus-raisonnement-ne-reduit-pas-biais-modeles"
description = "Une étude à 12 350 appels n'a trouvé aucune baisse fiable de six mesures de biais cognitifs lorsque les modèles consommaient plus de tokens de raisonnement. Un prompt direct a aidé pour l'ancrage."
tags = ["research", "models"]
date = 2026-10-09T04:02:06+02:00
draft = false
+++

Donner plus de temps de raisonnement aux modèles de langage n'a pas réduit de façon fiable leur sensibilité aux prompts de biais cognitifs dans une nouvelle étude couvrant sept modèles et 12 350 appels API.

Le chercheur de Texas Tech University Obada Kraishan a varié l'allocation de raisonnement de modèles d'Anthropic, OpenAI, DeepSeek et Qwen, puis mesuré comment leurs réponses changeaient lorsqu'une vignette décisionnelle contenait une ancre non pertinente, un cadrage ou un engagement antérieur. Aucun n'est devenu systématiquement moins sensible avec l'augmentation réelle des tokens de raisonnement utilisés.

**Pourquoi c'est important :** Un développeur choisissant un budget de raisonnement supérieur pour un système d'aide à la décision paie davantage de calcul. Ces résultats indiquent que le calcul supplémentaire n'a amélioré de façon fiable aucun biais mesuré, même si les modèles de raisonnement semblent souvent plus réfléchis aux utilisateurs.

## L'étude a mesuré le raisonnement réellement effectué

L'expérience utilisait 30 vignettes appariées couvrant ancrage, cadrage, aversion aux pertes, escalade d'engagement, disponibilité et biais de confirmation. Chaque paire contenait les mêmes informations pertinentes pour la décision, mais une version ajoutait l'élément censé déplacer le jugement humain. Dix échantillons répétés par condition permettaient à l'auteur de mesurer la modification des options choisies.

Le panel de sept modèles appariait des versions avec et sans raisonnement dans quatre familles. Les plafonds demandés étaient de zéro, 1 024, 4 096 et 8 192 tokens, bien que les cellules disponibles variaient selon le fournisseur. Kraishan a enregistré les tokens réellement consommés, car le réglage API ne se traduisait souvent pas par une quantité équivalente de réflexion.

Cette distinction s'est révélée importante. Le modèle Anthropic augmentait son raisonnement moyen avec le plafond, mais restait bien sous les limites supérieures. Le modèle OpenAI testé utilisait presque la même quantité au-delà de zéro, tandis que DeepSeek-R1 et Qwen3 dépassaient parfois le plafond demandé de 1 024 tokens. L'analyse principale a donc traité l'utilisation réelle de tokens comme la dose.

Les modèles de raisonnement n'étaient pas de façon fiable moins biaisés que leurs comparateurs appariés. La différence penchait en fait vers une sensibilité légèrement supérieure dans les quatre familles, mais l'estimation combinée était trop incertaine pour étayer cette affirmation plus forte. Plus important pour la question centrale de l'expérience, aucun modèle n'a montré de baisse statistiquement fiable avec une plus forte consommation de tokens de raisonnement.

Le constat a une portée limitée. La batterie contenait cinq éléments pour chacun de six biais, tous issus de scénarios de décision managériale, et certaines comparaisons de familles passaient entre modèles apparentés plutôt que d'activer ou désactiver le raisonnement avec des poids identiques. Elle teste le comportement sous prompts contrôlés, pas la justesse de décisions professionnelles ouvertes.

## L'ancrage a répondu à une instruction directe

L'ancrage était le seul biais testé à déplacer systématiquement les modèles dans le même sens que celui généralement observé chez les humains. Un nombre dans le prompt attirait les estimations vers lui dans les sept modèles. Quatre autres catégories tendaient à évoluer en sens inverse, tandis que la disponibilité ne montrait aucun effet fiable.

Pour les cinq éléments d'ancrage, l'auteur a ajouté une phrase imposant au modèle de reformuler l'ancre avant de répondre. L'ancrage a baissé dans chaque élément. Le résultat agrégé a manqué de peu le seuil de significativité de l'étude : c'est donc une observation prometteuse plutôt qu'une atténuation confirmée, mais le raisonnement supplémentaire seul n'a produit aucune réduction comparable.

Ce contraste est le résultat le plus pratique de l'article. Une instruction ciblée peut changer les informations traitées par le modèle, tandis qu'un budget de raisonnement supérieur ne fait que donner plus de place au processus existant. L'expérience n'établit pas que reformuler des nombres généralise au-delà de cinq prompts ; elle montre pourquoi les réglages de calcul et les contrôles de biais doivent faire l'objet d'évaluations distinctes.

La prépublication a été soumise le 7 octobre et acceptée à IEEE CogMI 2026. L'auteur a publié la batterie figée de prompts, les relevés de tokens par appel et le code d'analyse dans le [dépôt Anchored Minds](https://github.com/obadaKraishan/anchored-minds), permettant de tester le résultat sur des modèles plus récents et de plus grands ensembles d'éléments.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| L'étude a effectué 12 350 appels sur sept modèles de quatre familles | SELON LA SOCIÉTÉ | [Article](https://arxiv.org/abs/2610.10049) | [Code et données](https://github.com/obadaKraishan/anchored-minds) |
| Elle utilisait 30 vignettes couvrant six biais cognitifs | SELON LA SOCIÉTÉ | [Article](https://arxiv.org/abs/2610.10049) | [Code et données](https://github.com/obadaKraishan/anchored-minds) |
| Les plafonds demandés et le raisonnement réel divergeaient selon le fournisseur | SELON LA SOCIÉTÉ | [Article](https://arxiv.org/abs/2610.10049) | [Code et données](https://github.com/obadaKraishan/anchored-minds) |
| Aucun modèle testé n'a montré de baisse fiable de l'ampleur des biais avec plus de tokens de raisonnement | SELON LA SOCIÉTÉ | [Article](https://arxiv.org/abs/2610.10049) | aucune |
| Les modèles de raisonnement n'étaient pas de façon fiable moins biaisés que les comparateurs familiaux | SELON LA SOCIÉTÉ | [Article](https://arxiv.org/abs/2610.10049) | aucune |
| L'ancrage évoluait dans le sens humain dans les sept modèles | SELON LA SOCIÉTÉ | [Article](https://arxiv.org/abs/2610.10049) | aucune |
| Reformuler l'ancre a réduit l'ancrage dans les cinq éléments, mais manqué le seuil de significativité | SELON LA SOCIÉTÉ | [Article](https://arxiv.org/abs/2610.10049) | aucune |
| L'article a été accepté à IEEE CogMI 2026, et le code et les données ont été publiés | VÉRIFIÉ | [Article](https://arxiv.org/abs/2610.10049) | [Dépôt](https://github.com/obadaKraishan/anchored-minds) |

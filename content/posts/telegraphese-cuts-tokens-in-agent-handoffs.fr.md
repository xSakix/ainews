+++
title = "Le style télégraphique réduit les tokens entre agents"
slug = "style-telegraphique-reduit-tokens-entre-agents"
description = "Un benchmark public montre qu'une instruction peut faire écrire à plusieurs modèles des comptes rendus lisibles par machine avec environ deux fois moins de tokens de sortie. La technique échoue pendant le raisonnement actif."
tags = ["agents", "research", "tools"]
date = 2026-10-10T03:58:41+02:00
draft = false
+++

Demander aux modèles de langage d'écrire en style télégraphique réduisait leur sortie d'environ 40 % à 49 %, tandis que d'autres modèles récupéraient les faits consignés avec une précision comparable.

Le développeur indépendant Travis Smith a testé l'instruction sur 50 passages et environ 1 300 questions. La méthode demande au modèle de supprimer articles et remplissage, d'abréger, de préserver chaque fait, nombre et nom propre et d'utiliser des minuscules pour que les majuscules ne gonflent pas le nombre de tokens.

## Pourquoi c'est important {#why-it-matters}

Un développeur d'agents paie une fois lorsqu'un modèle écrit un souvenir, puis à chaque lecture par un autre modèle. Comprimer les notes entre machines une fois le travail achevé peut réduire à la fois la facture de sortie et le contexte occupé par les transmissions répétées.

Le benchmark sépare écriture et lecture. Gemma 4, Qwen3.8 et GLM-5.3-Flash écrivaient des comptes rendus condensés, tandis que des modèles de plusieurs familles répondaient à des questions ancrées dans ces comptes rendus ou dans des résumés ordinaires. Smith a publié l'environnement de test, des registres de résultats figés et un notebook exécutable.

Le résultat le plus net venait des rédacteurs. Gemma utilisait environ 40 % de tokens de sortie facturés en moins, tandis que Qwen et GLM économisaient environ 49 %. Les lecteurs répondant à partir des comptes rendus compressés obtenaient entre 0,99 et 1,10 fois leur précision sur les résumés ordinaires. Quatre familles de lecteurs ne recevaient aucun exemple détaillé du style, ce qui suggère que la convention leur était déjà familière grâce aux données d'entraînement.

## La compression doit venir après le raisonnement

Le moment d'application changeait le résultat. Les modèles invités à formuler directement leurs réponses en style télégraphique ne conservaient qu'environ quatre cinquièmes de leur précision habituelle. Lorsque le contenu était d'abord fixé puis compressé en compte rendu, la lecture ultérieure égalait ou dépassait légèrement le contrôle par résumé ordinaire.

Cela rend la technique adaptée aux archives de brouillons, aux mémoires d'agents et aux transmissions. Elle convient mal à une réponse destinée à l'utilisateur ou à une étape où le modèle décide encore quoi dire. Le texte compressé reste lisible par une personne, mais il est volontairement moins confortable que la prose normale.

Le raisonnement obligatoire créait un autre mode d'échec. GPT-5-mini produisait moins de tokens visibles, mais dépensait environ trois fois plus en raisonnement caché, selon le registre de l'auteur, rendant l'écriture totale plus chère. Une équipe doit tester le compteur de facturation réel du fournisseur plutôt que compter seulement les caractères ou tokens visibles.

Smith a aussi mesuré un aller-retour où le texte compressé était redéveloppé en prose. Le résultat stocké restait plus petit qu'un résumé ordinaire, mais l'appel de modèle supplémentaire consommait plus de tokens que l'écriture initiale n'en économisait. Des lectures répétées peu coûteuses peuvent récupérer ce coût ; un workflow avec une écriture et une lecture peut ne pas le faire.

Le cadrage historique n'est peut-être pas essentiel. Smith n'a pas effectué le contrôle strict consistant à demander la concision maximale sans mentionner le style télégraphique. L'expérience étaye donc l'instruction pratique, mais n'établit pas que ce style lui-même cause le gain.

Le résultat reste aussi un benchmark exécuté par l'auteur. Ses points forts sont des matériaux exceptionnellement inspectables et des tests entre familles ; sa limite est que les passages, questions et évaluateurs définissent un type de compte rendu factuel. Le code, les démonstrations mathématiques et la mémoire conversationnelle peuvent se comprimer différemment.

Le notebook publié peut désormais être exécuté sur des transcriptions d'agents en production, permettant aux équipes de comparer la réussite des tâches et les tokens facturés par les fournisseurs sur leur propre trafic.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Les instructions de style télégraphique réduisaient les tokens de sortie facturés d'environ 40 %–49 % pour les rédacteurs Gemma, Qwen et GLM | SELON LA SOCIÉTÉ | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | aucune |
| Les lecteurs d'autres familles récupéraient les faits avec 0,99–1,10 fois la précision des résumés en texte ordinaire | SELON LA SOCIÉTÉ | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | aucune |
| Composer directement les réponses en style télégraphique réduisait la précision à environ 0,81 de celle du contrôle ordinaire | SELON LA SOCIÉTÉ | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | aucune |
| Le raisonnement obligatoire de GPT-5-mini annulait l'économie de tokens visibles dans le test de l'auteur | SELON LA SOCIÉTÉ | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | aucune |
| L'environnement de test, les registres figés et le notebook sont publics | VÉRIFIÉ | https://github.com/Travis42/telegraph-test | aucune |
| La méthode convient surtout aux comptes rendus lisibles par machine dont le contenu est fixé, plutôt qu'au raisonnement actif | ANALYSE | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | aucune |

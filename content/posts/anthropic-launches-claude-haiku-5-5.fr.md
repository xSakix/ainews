+++
title = "Anthropic lance Claude Haiku 5.5"
slug = "anthropic-lance-claude-haiku-5-5"
description = "Le petit modèle Claude ajoute un raisonnement adaptatif et une tarification des tokens à deux niveaux. Anthropic le destine aux résumés, au travail dans le navigateur et aux sous-agents à périmètre restreint."
tags = ["models", "agents"]
date = 2026-10-08T03:59:31+02:00
draft = false
+++

Anthropic a lancé Claude Haiku 5.5 le 7 octobre, réduisant le prix effectif de sa gamme de petits modèles tout en ajoutant une fenêtre de contexte d'un million de tokens et un effort de raisonnement réglable.

Le modèle accessible par API est conçu pour des travaux fréquents et bien délimités, comme la classification, la synthèse, les requêtes de base de données et les tâches de sous-agents. Il est disponible chez Anthropic et sur les principales plateformes cloud sous l'identifiant `claude-haiku-5-5`.

Pour les développeurs qui paient à la tâche, le changement de prix est la conséquence immédiate. Les prompts allant jusqu'à 100 000 tokens coûtent 0,10 dollar par million de tokens d'entrée et 0,50 dollar par million de tokens de sortie. Les prompts plus longs coûtent respectivement 0,50 et 2,50 dollars. Selon Anthropic, le coût moyen obtenu est inférieur d'environ 75 % à celui de Haiku 4.5, après prise en compte du tokenizer légèrement différent du nouveau modèle.

Haiku 5.5 est le premier Haiku doté d'un raisonnement adaptatif et d'un réglage de l'effort. Cela crée aussi une difficulté de migration : les requêtes utilisant l'ancien paramètre manuel `budget_tokens` renvoient une erreur HTTP 400. Les applications qui quittent Haiku 4.5 doivent retirer ce paramètre et tester à nouveau la consommation de tokens comme la qualité des sorties.

Les évaluations internes d'Anthropic attribuent à Haiku 5.5 un score de 72,4 % sur la partie hors ligne d'un test d'utilisation de l'ordinateur, contre 15,7 % pour Haiku 4.5. La comparaison est menée par le fournisseur, et Anthropic continue d'orienter les travaux de programmation complexes vers Sonnet 5.5 ou Opus 5.5. Haiku doit servir de modèle d'appui moins coûteux, chargé d'opérations courtes et répétées autour d'un modèle plus grand.

La sortie divise aussi par deux le prix de lecture du cache de Sonnet 5.5, à 0,10 dollar par million de tokens. Anthropic indique que ces lectures représentent une part suffisante du trafic des agents pour réduire d'environ 20 % le coût de la plupart des tâches d'agents Sonnet 5.5.

Les abonnés Max et Team doivent recevoir des crédits API mensuels durant la semaine du lancement. Les SDK Python et TypeScript d'Anthropic accueillent aussi des classes bêta pour l'utilisation du navigateur et de l'ordinateur, les deux charges sensibles à la vitesse mises en avant pour Haiku 5.5.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Anthropic a lancé Claude Haiku 5.5 le 7 octobre 2026 avec raisonnement adaptatif, une fenêtre de contexte d'un million de tokens et une sortie maximale de 128 000 tokens | VÉRIFIÉ | [Annonce d'Anthropic](https://www.anthropic.com/claude-haiku-5-5) | aucune |
| Les prompts jusqu'à 100 000 tokens coûtent 0,10 dollar en entrée et 0,50 dollar en sortie par million de tokens ; les plus longs coûtent 0,50 et 2,50 dollars | VÉRIFIÉ | [Annonce d'Anthropic](https://www.anthropic.com/claude-haiku-5-5) | aucune |
| Anthropic affirme que le coût moyen est inférieur d'environ 75 % à celui de Haiku 4.5 | SELON LA SOCIÉTÉ | [Annonce d'Anthropic](https://www.anthropic.com/claude-haiku-5-5) | aucune |
| Anthropic annonce 72,4 % sur le sous-ensemble hors ligne d'OSWorld 2.1, contre 15,7 % pour Haiku 4.5 | SELON LA SOCIÉTÉ | [Annonce d'Anthropic](https://www.anthropic.com/claude-haiku-5-5) | aucune |
| Les requêtes avec réglage manuel `budget_tokens` renvoient HTTP 400 lors de la migration | VÉRIFIÉ | [Notes de version de Claude](https://platform.claude.com/docs/en/release-notes/overview) | aucune |
| Les lectures du cache de Sonnet 5.5 coûtent désormais 0,10 dollar par million de tokens et Anthropic estime la baisse des coûts des tâches d'agents à environ 20 % | SELON LA SOCIÉTÉ | [Annonce d'Anthropic](https://www.anthropic.com/claude-haiku-5-5) | aucune |

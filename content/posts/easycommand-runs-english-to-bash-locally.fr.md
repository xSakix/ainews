+++
title = "EasyCommand convertit localement l'anglais en Bash"
slug = "easycommand-convertit-localement-anglais-en-bash"
description = "L'outil open source en ligne de commande intègre llama.cpp et deux petits modèles affinés. Son auteur publie aussi le jeu d'entraînement de 401 975 paires et le code du benchmark."
tags = ["projects", "models", "tools"]
date = 2026-10-06T04:06:31+02:00
draft = false
+++

EasyCommand transforme des demandes en anglais en commandes Bash avec un petit modèle exécuté sur CPU, en gardant le prompt et la commande proposée sur la machine de l'utilisateur.

Le développeur Max Trivedi a publié l'application en ligne de commande `ec`, deux familles de modèles et un jeu de données de 401 975 paires dédupliquées de demandes et de commandes. L'application intègre llama.cpp, affiche la commande proposée et peut demander confirmation avant de l'exécuter.

Pour un développeur qui a occasionnellement besoin d'un rappel sur le shell, l'exécution locale supprime un appel API d'une partie sensible du workflow. En contrepartie, il assume directement la responsabilité : le projet avertit qu'une commande plausible peut rester erronée et recommande de commencer en mode aperçu.

Les modèles publiés partent de Qwen2.5-Coder-1.5B-Instruct et Qwen3-0.6B. Tous deux sont disponibles en fichiers GGUF pour l'inférence locale, checkpoints BF16 fusionnés et adaptateurs LoRA pour poursuivre l'entraînement. Modèles et données utilisent la licence Apache 2.0 ; application et code du benchmark utilisent MIT.

Trivedi indique que le modèle de 1,5 milliard de paramètres a résolu 212 des 300 cas d'une version actualisée du benchmark ALFA anglais-vers-shell, contre 191 pour l'ancien système nl2sh. C'est une comparaison menée par l'auteur avec des prompts et réglages différents, pas un résultat de classement indépendant.

La publication est particulièrement utile parce qu'elle expose les cas d'échec autant que le modèle. Trivedi précise que le jeu de données à plat ne reproduit pas la pondération historique utilisée à l'entraînement et n'a pas de partition de test officielle. Il recommande de réserver des familles entières de tâches plutôt que de répartir aléatoirement les paraphrases, ce qui pourrait faire passer des commandes presque identiques dans l'entraînement et l'évaluation.

La cible est Bash sous GNU/Linux, plutôt que tous les shells ou systèmes d'exploitation. Le dépôt d'EasyCommand est désormais public, et l'auteur demande aux utilisateurs des tests qui révèlent les transferts peu fiables et les commandes non couvertes.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| EasyCommand fonctionne localement, intègre llama.cpp et prévisualise les commandes avant exécution | VÉRIFIÉ | [Présentation du projet](https://dirac.run/posts/easycommand) | [dépôt public](https://github.com/dirac-run/ec) |
| La publication contient 401 975 paires anglais/Bash dédupliquées | VÉRIFIÉ | [Présentation du projet](https://dirac.run/posts/easycommand) | jeu de données lié depuis le dépôt |
| Les modèles dérivent de Qwen2.5-Coder-1.5B et Qwen3-0.6B | VÉRIFIÉ | [Présentation du projet](https://dirac.run/posts/easycommand) | fichiers des modèles liés depuis le dépôt |
| Le modèle de 1,5 milliard obtient 212/300 contre 191/300 pour nl2sh | SELON LA SOCIÉTÉ | [Présentation du projet](https://dirac.run/posts/easycommand) | aucune ; benchmark mené par l'auteur |
| Modèles et données sont sous Apache-2.0 ; application et benchmark sous MIT | VÉRIFIÉ | [Présentation du projet](https://dirac.run/posts/easycommand) | fichiers de licence du dépôt |
| Le jeu de données n'a pas de partition de test officielle et ne conserve pas la pondération historique | SELON LA SOCIÉTÉ | [Présentation du projet](https://dirac.run/posts/easycommand) | déclaration de l'auteur |

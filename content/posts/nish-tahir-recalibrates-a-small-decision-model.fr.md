+++
title = "Nish Tahir recalibre un petit modèle de décision"
slug = "nish-tahir-recalibre-petit-modele-decision"
description = "Une expérience exécutable transforme Qwen3-1.7B en classificateur à une seule passe, puis montre que sa confiance est trop élevée. La mise à l'échelle par température améliore les probabilités."
tags = ["models", "research", "essays"]
date = 2026-10-11T04:01:06+02:00
draft = false
+++

L'ingénieur indépendant Nish Tahir a publié une expérience exécutable qui transforme Qwen3-1.7B en modèle de décision à une seule passe, puis mesure à quel point sa confiance correspond mal à sa précision.

La méthode limite le vocabulaire de sortie du modèle aux tokens de réponse A à E et lit leurs probabilités après une passe avant. Sur CommonsenseQA, Tahir rapporte une précision de 59,4 % pour le modèle de base et de 62,4 % après un bref entraînement d'affinage.

## Pourquoi c'est important {#why-it-matters}

Un développeur qui construit un système de routage ou un score de risque doit savoir plus que l'option gagnante. Si un modèle annonce 95 % mais n'a raison que sept fois sur dix, les seuils fondés sur ce nombre se comporteront de façon imprévisible. L'expérience de Tahir montre tout le chemin des logits à un problème de calibration mesuré, avec un modèle assez petit pour la reproduire.

Le gain de précision n'est pas le résultat le plus informatif. Les réponses auxquelles était attribuée une confiance de 90 % à 100 % n'étaient correctes qu'environ 70 % du temps. Dans la tranche de 80 % à 90 %, la précision était d'environ 40 %. Le modèle distinguait donc les choix assez bien pour dépasser le hasard, tout en exprimant beaucoup plus de certitude que ses résultats ne le justifiaient.

Tahir applique une mise à l'échelle par température pour corriger les probabilités. La méthode apprend un seul scalaire sur des exemples réservés et divise les logits par celui-ci avant l'opération softmax. Augmenter la température aplatit une distribution trop confiante sans changer la réponse au score le plus élevé.

Cela fait de la mise à l'échelle par température une étape de calibration, pas une amélioration des capacités. Elle ne peut ni réparer de mauvais classements ni enseigner des connaissances manquantes. Sa valeur est qu'un taux annoncé de 70 % peut se rapprocher de sept cas corrects sur dix sur des données ressemblant à l'ensemble de calibration.

Le compte rendu comprend une implémentation PyTorch compacte et des démonstrations interactives. Il révèle aussi un choix de conception caché par de nombreux produits de modèles de décision : le schéma de réponse doit être connu à l'avance et correspondre clairement à un petit ensemble de tokens. Une tâche aux labels ambigus, aux options manquantes ou aux réponses valides multiples rompt cette simplicité.

Les résultats proviennent d'un petit modèle, d'un benchmark et de la propre configuration d'entraînement de l'auteur. Les questions à choix multiple de CommonsenseQA ne reproduisent ni le routage documentaire, ni l'examen de fraudes, ni la sélection d'outils, et la calibration peut dériver lorsque la distribution des entrées change. Chaque déploiement aurait besoin de ses propres données réservées et de contrôles périodiques.

L'article est utile précisément parce qu'il rapporte cette faiblesse au lieu de présenter la sortie de confiance comme fiable par construction. Le code et les démonstrations sont disponibles dès maintenant, donnant aux praticiens une courte référence pour tester de plus grands modèles de décision spécialisés.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| L'expérience limite Qwen3-1.7B aux tokens de réponse A à E et lit une passe avant | VÉRIFIÉ | https://nishtahir.com/build-your-own-decision-model/ | aucune |
| Le modèle de base a obtenu 59,4 % et le modèle rapidement affiné 62,4 % sur CommonsenseQA | SELON LA SOCIÉTÉ | https://nishtahir.com/build-your-own-decision-model/ | aucune |
| La tranche de confiance de 90 % à 100 % était correcte environ 70 % du temps | SELON LA SOCIÉTÉ | https://nishtahir.com/build-your-own-decision-model/ | aucune |
| La tranche de confiance de 80 % à 90 % était correcte environ 40 % du temps | SELON LA SOCIÉTÉ | https://nishtahir.com/build-your-own-decision-model/ | aucune |
| La mise à l'échelle par température change la concentration des probabilités sans changer la réponse classée première | VÉRIFIÉ | https://nishtahir.com/build-your-own-decision-model/ | aucune |

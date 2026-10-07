+++
title = "Mistral présente Large 4 avant de publier ses poids"
slug = "mistral-presente-large-4-avant-de-publier-ses-poids"
description = "Mistral ouvre l'accès API à son modèle multimodal d'un billion de paramètres et fixe au 27 octobre la sortie des poids ouverts. Les affirmations sur l'architecture et les benchmarks restent provisoires."
tags = ["models", "business"]
date = 2026-10-07T04:00:57+02:00
draft = false
+++

Mistral a ouvert une préversion API publique de Mistral Large 4, tout en programmant la publication des poids téléchargeables pour le 27 octobre.

L'entreprise française décrit le modèle comme un mélange d'experts multimodal entraîné de zéro dans ses centres de données européens. Il accepte texte et images, prend en charge plus de 160 langues et dispose d'une fenêtre de contexte d'un million de tokens.

## Pourquoi c'est important {#why-it-matters}

Une organisation qui envisage un modèle européen auto-hébergé peut tester Large 4 dès maintenant, mais ne peut pas encore inspecter ni déployer les poids promis. Cet écart en fait une préversion assortie d'un engagement de livraison daté, plutôt qu'une sortie à poids ouverts achevée.

L'annonce de Mistral indique un billion de paramètres au total et 49 milliards actifs par token. Sa documentation indique plutôt 1,05 billion au total, 52 milliards actifs et un encodeur visuel de 1,6 milliard de paramètres. La différence pourrait refléter un arrondi ou une configuration modifiée, mais Mistral n'a pas publié de rapport technique qui réconcilie ces chiffres.

L'entreprise met l'accent sur la cybersécurité. Elle annonce 82 % sur la partie reproduction puis correction de CyberGym-E2E, 93 % sur Cybench et 61,7 % sur DeepSWE v1.1. Certaines évaluations nomment des prestataires externes, mais la comparaison assemblée et la plupart des principales affirmations figurent dans les propres documents de lancement de Mistral.

Avant l'arrivée des poids, Mistral indique que des spécialistes de la cybersécurité et des autorités publiques testeront une version à modération réduite. L'entreprise estime que les refus de sécurité ordinaires peuvent entraver le travail défensif, un compromis que cette préversion vise à examiner.

Les tarifs API commencent à 1,36 dollar par million de tokens d'entrée et 4,18 dollars par million de tokens de sortie. Des modes avec et sans raisonnement sont disponibles dans Mistral Studio, tandis que la licence et les exigences définitives de déploiement resteront inconnues jusqu'à la publication des poids.

L'événement décisif est le 27 octobre. Une fiche du modèle, un rapport technique, une licence et des fichiers téléchargeables montreront si les éléments publics correspondent à l'échelle et aux capacités de la préversion.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Mistral a ouvert une préversion API de Large 4 et prévu les poids pour le 27 octobre | VÉRIFIÉ | [Annonce de Mistral](https://mistral.ai/news/mistral-large-4/) | [Documentation de Mistral](https://docs.mistral.ai/models/mistral-large-4) |
| L'annonce indique un billion de paramètres au total et 49 milliards actifs | VÉRIFIÉ | [Annonce de Mistral](https://mistral.ai/news/mistral-large-4/) | la documentation indique des chiffres différents |
| La documentation indique 1,05 billion au total, 52 milliards actifs et un encodeur visuel de 1,6 milliard | VÉRIFIÉ | [Documentation de Mistral](https://docs.mistral.ai/models/mistral-large-4) | aucune |
| Le modèle a obtenu 82 % sur CyberGym-E2E reproduction puis correction, 93 % sur Cybench et 61,7 % sur DeepSWE v1.1 | SELON LA SOCIÉTÉ | [Annonce de Mistral](https://mistral.ai/news/mistral-large-4/) | les évaluateurs nommés ne vérifient pas indépendamment toute la comparaison |
| Les tarifs API sont de 1,36 dollar en entrée et 4,18 dollars en sortie par million de tokens | VÉRIFIÉ | [Documentation de Mistral](https://docs.mistral.ai/models/mistral-large-4) | documentation actuelle |

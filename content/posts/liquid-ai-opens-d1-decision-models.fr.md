+++
title = "Liquid AI ouvre les poids de ses modèles de décision d1"
slug = "liquid-ai-ouvre-les-poids-de-ses-modeles-de-decision-d1"
description = "d1-3B, à 3,1 milliards de paramètres, et le modèle expérimental d1-omni, à 600 millions, répondent à des questions structurées en une seule passe avant. Leurs poids sont disponibles pour un déploiement local."
tags = ["models", "projects"]
date = 2026-10-08T03:58:31+02:00
draft = false
+++

Liquid AI a publié les poids ouverts de deux modèles d1 le 7 octobre, apportant son système de décision rapide et structuré aux appareils locaux après un lancement limité à l'API.

Les modèles répondent à des questions oui/non, à choix multiples ou à notation en une seule passe avant, au lieu de générer une séquence de tokens. d1-3B, doté de 3,1 milliards de paramètres, accepte texte et images ; le modèle expérimental d1-omni-600M accepte du texte accompagné soit d'images, soit d'un maximum de 30 secondes d'audio.

Cette conception offre aux développeurs un composant compact pour le routage, la modération, la classification ou le classement lorsqu'une réponse libre n'est pas nécessaire. Un même état d'entrée peut contenir plusieurs questions nommées, et le modèle renvoie ensemble les décisions correspondantes, évitant la latence et les formulations variables de la génération de tokens.

Liquid indique que d1-3B répondait à une question en 8 millisecondes sur une RTX 4090, 30 millisecondes sur un Apple M5 Pro et 50 millisecondes sur un Jetson Orin Nano. Ce sont les mesures de l'entreprise. Son tableau publié attribue aussi à d1-3B un score moyen de 82,9 sur sept jeux de données textuelles publics, contre 78,4 pour le petit modèle.

Les deux versions ciblent des matériels différents. d1-3B repose sur le modèle vision-langage à décodeur seul de Liquid et possède une fenêtre de contexte de 32 768 tokens. d1-omni-600M associe un encodeur textuel bidirectionnel à des encodeurs visuel et audio distincts, avec une fenêtre de 16 384 tokens. Liquid présente le petit modèle comme une première version de recherche et ne publie pas de mesures de latence le concernant.

Les deux dépôts utilisent la LFM Open License plutôt qu'une licence logicielle permissive standard. Le chargement exige actuellement Transformers 5.14 ou ultérieur et exécute du Python fourni par le dépôt via `trust_remote_code=True`, un réglage qui justifie d'examiner le code téléchargé avant usage.

Les poids, fiches de modèle et démonstration sont désormais disponibles sur Hugging Face. Liquid fournit aussi des variantes GGUF et à quantification 8 bits des poids et activations, qui facilitent les essais de d1-3B sur des machines contraintes alors que son API de décision est encore récente.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Liquid AI a publié les poids de d1-3B et d1-omni-600M le 7 octobre 2026 | VÉRIFIÉ | [Annonce de Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | [Fiche de d1-3B](https://huggingface.co/LiquidAI/d1-3B) |
| Les modèles d1 répondent aux questions structurées en une passe avant sans générer de tokens de sortie | VÉRIFIÉ | [Annonce de Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | aucune |
| d1-3B accepte texte et images ; d1-omni-600M accepte du texte avec images ou audio | VÉRIFIÉ | [Annonce de Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | [Fiche de d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) |
| Liquid annonce 8 ms sur RTX 4090, 30 ms sur Apple M5 Pro et 50 ms sur Jetson Orin Nano | SELON LA SOCIÉTÉ | [Annonce de Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | aucune |
| Liquid annonce des scores moyens aux évaluations textuelles de 82,9 pour d1-3B et de 78,4 pour d1-omni-600M | SELON LA SOCIÉTÉ | [Annonce de Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | aucune |
| Le chargement exige Transformers 5.14 ou ultérieur et `trust_remote_code=True` | VÉRIFIÉ | [Annonce de Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | [Fiche de d1-3B](https://huggingface.co/LiquidAI/d1-3B) |

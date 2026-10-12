+++
title = "Cloudflare ajoute Clef-omni multimodal"
slug = "cloudflare-ajoute-clef-omni-multimodal"
description = "Le nouveau classificateur conserve les entrées image, audio et vidéo de Qwen3-Omni, mais renvoie des réponses typées plutôt que de la prose générée. Cloudflare a aussi réduit le prix et la fenêtre de contexte de Clef-flash."
tags = ["models", "tools"]
date = 2026-10-12T04:02:37+02:00
draft = false
+++

Cloudflare a publié Clef-omni, un classificateur multimodal qui accepte texte, images, audio et vidéo, mais renvoie des réponses typées plutôt que de la prose générée.

Le modèle étend la famille de classification Clef en prenant Qwen3-Omni pour base. Cloudflare a figé cette base, entraîné des adaptateurs légers et ajouté une tête qui associe directement une entrée à un schéma de labels défini par l'utilisateur en une passe avant.

## Pourquoi c'est important {#why-it-matters}

Pour un développeur qui trie des messages d'assistance, examine des photos de produits ou route de courts clips, Clef-omni propose une interface de classification unique pour plusieurs types de médias. Cela peut supprimer une étape distincte de transcription ou de légendage, même si Cloudflare n'a pas publié de comparaisons indépendantes de bout en bout avec de telles chaînes.

Cloudflare indique que Clef-omni est un modèle à mélange d'experts de 30 milliards de paramètres, dont environ 3 milliards sont activés pour une entrée. Dans les mesures Workers AI de l'entreprise, la classification de texte prenait environ 130 millisecondes, celle d'images environ 150 millisecondes et une vidéo de 21 secondes avec audio environ 1,5 seconde. Ces durées proviennent de tests du fournisseur et varieront selon la taille de l'entrée, les files d'attente et le déploiement.

Les benchmarks donnent un tableau contrasté plutôt qu'une amélioration uniforme. Le tableau de Cloudflare place l'ancien Clef dense devant sur plusieurs tâches textuelles, tandis que Clef-omni le dépasse de peu sur le jeu d'intentions BANKING77, avec 94,8 % contre 94,2 %. La différence pratique du nouveau modèle est sa gamme d'entrées, pas une affirmation générale de meilleure précision textuelle.

Cloudflare a aussi modifié les conditions de Clef-flash. Son prix d'entrée affiché est passé de 0,09 à 0,038 dollar par million de tokens, tandis que sa fenêtre de contexte a baissé de 64 000 à 24 000 tokens. Clef reste à 0,24 dollar par million de tokens d'entrée et Clef-omni est lancé à 0,15 dollar.

Les poids de Clef-omni sont disponibles sous Apache 2.0 sur Hugging Face. La fiche indique environ 35,3 milliards de paramètres au total et précise que le chargeur personnalisé actuel nécessite environ 64 Go de mémoire BF16 sur un GPU de classe H200. Cloudflare annonce une prise en charge de SGLang prévue, sans date de sortie.

## Les points à surveiller

Les poids ouverts permettent désormais des tests indépendants de latence, de calibration et de précision. La prise en charge dans un moteur de mise en service courant comptera pour les équipes souhaitant exécuter le modèle hors Workers AI sans maintenir le chargeur personnalisé de Cloudflare.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Cloudflare a publié Clef-omni avec des entrées texte, image, audio et vidéo et des sorties de classification typées | VÉRIFIÉ | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | https://huggingface.co/Cloudflare/clef-omni |
| Cloudflare rapporte environ 130 ms pour le texte, 150 ms pour les images et 1,5 s pour un clip audiovisuel de 21 secondes | SELON LA SOCIÉTÉ | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | aucune |
| Le tableau de Cloudflare rapporte 94,8 % sur BANKING77 pour Clef-omni et 94,2 % pour Clef | SELON LA SOCIÉTÉ | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | aucune |
| Clef-flash coûte désormais 0,038 dollar par million de tokens d'entrée et possède une fenêtre de contexte de 24 000 tokens | VÉRIFIÉ | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | aucune |
| Des poids Apache-2.0 et un chargeur personnalisé sont disponibles ; la prise en charge de SGLang est prévue | VÉRIFIÉ | https://huggingface.co/Cloudflare/clef-omni | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ |

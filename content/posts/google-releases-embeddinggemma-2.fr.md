+++
title = "Google lance EmbeddingGemma 2 pour la recherche multimodale"
slug = "google-lance-embeddinggemma-2-recherche-multimodale"
description = "Le modèle d'embedding de Google, avec 740 millions de paramètres, place texte, code, images, vidéo et audio dans un même espace vectoriel. Ses encodeurs modulaires sont conçus pour les appareils locaux."
tags = ["models", "tools"]
date = 2026-10-07T04:01:57+02:00
draft = false
+++

Google a lancé EmbeddingGemma 2, un modèle à poids ouverts de 740 millions de paramètres qui place texte, code, images, trames vidéo et audio dans un même espace d'embedding.

Les poids Apache-2.0 sont arrivés le 6 octobre avec une prise en charge dans Transformers, sentence-transformers, llama.cpp, vLLM, Ollama, LM Studio, MLX et Transformers.js. Le modèle sert à la recherche d'information et au routage, plutôt qu'à la génération de texte : il transforme différents types d'entrée en vecteurs dont on peut comparer la similarité.

## Pourquoi c'est important {#why-it-matters}

Un développeur qui construit une recherche privée sur téléphone ou ordinateur portable peut désormais indexer une note vocale et retrouver un segment vidéo sans enchaîner d'abord reconnaissance vocale, description d'images et modèle d'embedding textuel distinct. Cela supprime plusieurs composants de la recherche locale, même si l'utilité réelle du modèle dépend encore des données de l'utilisateur et de son budget de latence.

EmbeddingGemma 2 est modulaire. Son socle texte et code compte 270 millions de paramètres ; la vision en ajoute 170 millions et l'audio 300 millions. Toutes les configurations projettent les entrées dans 768 dimensions, et l'entraînement Matryoshka permet de tronquer les vecteurs à 512, 256 ou 128 dimensions pour réduire le stockage.

Google indique que les poids quantifiés pour le texte seul utilisent environ 191 Mo de RAM active sur un Pixel 11 Pro, contre environ 567 Mo pour le modèle complet. Son contexte de 8 192 tokens peut contenir jusqu'à 5,5 minutes d'audio, 29 images ou 58 trames vidéo selon le schéma de regroupement de Google.

L'évaluation de l'entreprise donne 78,68 sur MTEB Code, contre 68,76 pour le premier EmbeddingGemma. Google revendique aussi une qualité de premier plan parmi les modèles d'embedding multimodaux de moins d'un milliard de paramètres. Ces mesures datent du lancement et ne sont pas des reproductions indépendantes ; la fiche du modèle constitue une meilleure base pour comparer une tâche de recherche particulière.

Cette version partage un tokenizer et une conception d'encodeur audio avec Gemma 4, ce qui peut limiter les composants dupliqués quand le modèle d'embedding alimente un modèle génératif local. Google a aussi publié des exemples d'applications de recherche de médias et de moments vidéo.

Les prochaines preuves pratiques viendront de tests sur des collections privées mixtes, où le rappel entre modalités, le temps d'indexation et la mémoire comptent davantage qu'un seul benchmark agrégé.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| Google a lancé EmbeddingGemma 2 le 6 octobre 2026 | VÉRIFIÉ | [Annonce de Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | [poids et fiche du modèle](https://huggingface.co/google/embeddinggemma-2) |
| Le modèle compte 740 millions de paramètres, avec des composants modulaires de 270 millions pour le texte, 170 millions pour la vision et 300 millions pour l'audio | VÉRIFIÉ | [Annonce de Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | la fiche du modèle décrit l'architecture |
| La RAM active quantifiée est d'environ 191 Mo pour le texte et 567 Mo pour le modèle complet sur Pixel 11 Pro | SELON LA SOCIÉTÉ | [Annonce de Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | aucune |
| MTEB Code est passé de 68,76 à 78,68 | SELON LA SOCIÉTÉ | [Annonce de Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | aucune |
| Les poids Apache-2.0 sont disponibles | VÉRIFIÉ | [dépôt du modèle](https://huggingface.co/google/embeddinggemma-2) | le dépôt est accessible |

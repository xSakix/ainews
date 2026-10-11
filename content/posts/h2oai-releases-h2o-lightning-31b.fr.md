+++
title = "H2O.ai publie H2O-Lightning-31B"
slug = "h2o-ai-publie-h2o-lightning-31b"
description = "Le modèle de décision à poids ouverts répond à des questions délimitées en une seule passe et renvoie des probabilités. Ses meilleurs chiffres de vitesse et de précision proviennent des tests de H2O.ai."
tags = ["models", "tools"]
date = 2026-10-11T04:06:06+02:00
draft = false
+++

H2O.ai a publié H2O-Lightning-31B, un modèle à poids ouverts conçu pour répondre à des questions de décision délimitées par des probabilités plutôt que par une prose libre.

Le modèle repose sur Gemma 4 31B-it et accepte du texte ainsi que jusqu'à quatre images. Son interface couvre les choix, les questions oui/non et les scores ordonnés, en renvoyant un résultat en une seule passe avant. H2O.ai a publié les poids, la fiche du modèle et le code de mise en service sur Hugging Face.

## Pourquoi c'est important {#why-it-matters}

Pour un développeur qui utilise un grand chatbot pour orienter des tickets, noter des dossiers ou sélectionner un outil, une sortie contrainte peut éliminer plusieurs étapes fragiles : demander du JSON, l'analyser, rejeter les réponses mal formées et recommencer. Une probabilité révèle aussi à quel point le choix était serré, mais elle n'est utile que si le modèle est calibré pour les données visées.

H2O.ai rapporte que le modèle de 31 milliards de paramètres a correctement répondu à 212 des 231 questions publiques de JevBench. Dans son évaluation sur images, le modèle affiné a obtenu 88,4 % sur 1 877 questions, contre 88,0 % pour la base Gemma figée. L'intervalle d'incertitude de la fiche comprend l'absence d'amélioration : ce résultat sur images n'établit donc pas un gain fiable par rapport au modèle de base.

L'entreprise annonce également une latence médiane d'environ 25 millisecondes en chargeant le modèle en FP8 sur un seul NVIDIA H100. Ce chiffre vient de sa propre configuration, avec le cache de préfixe désactivé, et la fiche ne fournit aucune mesure pour des GPU plus petits. Les fichiers bfloat16 publiés totalisent environ 63 Go avant le surcoût d'exécution.

La publication fonctionne sur vLLM 0.30.0 sans modification, derrière la couche de compatibilité `/v1/systemone` de H2O.ai. Les longs dossiers ne sont pas traités intégralement : une étape de recherche les réduit à 3 000 tokens avant l'inférence. Cette limite compte, car une décision ne peut refléter que les éléments préservés par cette étape.

Les poids portent la licence Apache 2.0 ainsi que les conditions Gemma de Google. L'avis de H2O.ai renvoie expressément aux interdictions d'usage de Gemma concernant les décisions automatisées qui affectent les droits individuels : les fichiers ouverts ne rendent donc pas tout déploiement autorisé.

H2O.ai a aussi actualisé son précédent modèle apparenté de 4 milliards de paramètres avec des mesures de latence révisées et un paquet GGUF pour llama.cpp. La version de 31 milliards est disponible dès maintenant sur sa page Hugging Face ; aucun test indépendant de latence, de calibration ou de qualité des tâches n'a encore été publié.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| H2O.ai a publié H2O-Lightning-31B avec les poids, une fiche du modèle et du code de mise en service | VÉRIFIÉ | https://huggingface.co/h2oai/h2o-lightning-31b | aucune |
| Le modèle prend en charge des décisions délimitées sur texte et images et renvoie des probabilités en une seule passe avant | VÉRIFIÉ | https://huggingface.co/h2oai/h2o-lightning-31b | aucune |
| Il a obtenu 212 réponses correctes sur 231 éléments JevBench et une latence médiane d'environ 25 ms sur un H100 | SELON LA SOCIÉTÉ | https://huggingface.co/h2oai/h2o-lightning-31b | aucune |
| Son évaluation sur images n'a pas montré de gain statistiquement fiable par rapport à la base Gemma figée | VÉRIFIÉ | https://huggingface.co/h2oai/h2o-lightning-31b | aucune |
| Les conditions Gemma restreignent les décisions automatisées affectant les droits individuels | VÉRIFIÉ | https://huggingface.co/h2oai/h2o-lightning-31b | aucune |

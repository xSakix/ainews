+++
title = "Warm Compaction réutilise le cache pour la mémoire des agents"
slug = "warm-compaction-reutilise-cache-memoire-agents"
description = "Le plug-in Hermes Agent sous Apache-2.0 demande au modèle principal de résumer un préfixe de conversation mis en cache, réduisant le traitement répété des prompts dans ses tests."
tags = ["agents", "tools"]
date = 2026-10-09T04:01:06+02:00
draft = false
+++

Un nouveau plug-in Hermes Agent compresse les longues conversations en demandant au modèle principal de résumer un préfixe de prompt déjà mis en cache par le serveur d'inférence.

Warm Compaction renvoie la dernière requête de l'agent, n'ajoute que les nouvelles lignes de conversation et termine par une instruction de passation. Le modèle retourne un résumé Markdown structuré, qui remplace l'ancien historique tandis qu'une partie récente reste mot pour mot.

**Pourquoi c'est important :** La compression du contexte nécessite généralement une nouvelle lecture volumineuse de la conversation. Pour un développeur exécutant de longues sessions d'agents, réutiliser le cache de préfixe du serveur peut réduire à la fois l'attente et le risque qu'un modèle de résumé plus petit et séparé perde une instruction importante.

Le plug-in utilise les interfaces documentées de Hermes Agent et ne nécessite aucun correctif de l'hôte. Il prend en charge la compression manuelle et automatique, fonctionne sous Python 3.10 ou ultérieur et est publié sous Apache 2.0. L'installation consiste en une commande de plug-in Hermes, puis en la sélection de `warm_compaction` comme moteur de contexte.

Son avantage de vitesse dépend du même modèle principal et d'un serveur d'inférence capable de réutiliser les blocs de prompt en cache. L'auteur cite les API hébergées de cache de prompts, vLLM, SGLang, TensorRT-LLM, llama.cpp, MLX, Ollama et LM Studio comme voies possibles, mais ne rapporte des tests directs que sur un système NVIDIA DGX et LM Studio. Une requête envoyée à un autre emplacement llama.cpp, par exemple, peut manquer le cache.

Le projet comprend des fichiers de preuves pour dix sessions synthétiques d'environ 105 000 tokens. Dans ces tests, le temps médian de résumé de Warm Compaction était de 16,8 secondes, contre 43,5 secondes pour `hermes-lcm` et 78,5 secondes pour le compresseur intégré. Il a conservé 59 des 60 faits testés ; les deux comparateurs en ont conservé 43 et 50. Ce sont des résultats mesurés par l'auteur sur une charge synthétique unique, et les trois moteurs utilisaient des modèles différents.

La gestion des échecs fait partie de la conception. Si la requête réutilisant le cache ne peut s'exécuter ou échoue aux contrôles de sortie, le plug-in appelle la voie auxiliaire de résumé de Hermes. Si elle échoue aussi, il écrit un résumé de format fixe et conserve le plus récent résumé antérieur comme texte cité. Une tentative annulée laisse l'historique inchangé.

Les versions de Hermes pourraient à terme fournir une option native de passation réutilisant le cache. Le plug-in vérifie cette capacité et peut y orienter les utilisateurs, tout en restant sélectionnable séparément. Le dépôt, les réglages et les preuves sont disponibles sur [GitHub](https://github.com/Elevatormusic/hermes-warm-compaction).

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Warm Compaction renvoie un préfixe en cache et ajoute les nouvelles lignes et une instruction de passation | VÉRIFIÉ | [Dépôt](https://github.com/Elevatormusic/hermes-warm-compaction) | aucune |
| Le plug-in utilise les API documentées de Hermes et est sous licence Apache-2.0 | VÉRIFIÉ | [Dépôt](https://github.com/Elevatormusic/hermes-warm-compaction) | aucune |
| L'accélération exige le même modèle et un cache de préfixe fonctionnel | VÉRIFIÉ | [Dépôt](https://github.com/Elevatormusic/hermes-warm-compaction) | aucune |
| La compaction médiane a pris 16,8 secondes dans dix sessions synthétiques | SELON LA SOCIÉTÉ | [Dépôt](https://github.com/Elevatormusic/hermes-warm-compaction) | aucune |
| Le plug-in a conservé 59 des 60 faits testés | SELON LA SOCIÉTÉ | [Dépôt](https://github.com/Elevatormusic/hermes-warm-compaction) | aucune |
| Les requêtes réutilisant le cache qui échouent utilisent des replis auxiliaires puis à format fixe | VÉRIFIÉ | [Dépôt](https://github.com/Elevatormusic/hermes-warm-compaction) | aucune |

+++
title = "vLLM montre quand séparer l'inférence aide ou pénalise"
slug = "vllm-montre-quand-separer-inference-aide-ou-penalise"
description = "Un guide pratique mesure le compromis entre traitement des prompts et génération des tokens séparés. Les latences les plus élevées diminuent sous charge, mais transférer la mémoire de travail retarde le premier token."
tags = ["essays", "tools", "hardware"]
date = 2026-10-06T04:04:31+02:00
draft = false
+++

Séparer le traitement des prompts de la génération des tokens peut stabiliser un serveur de modèles sous charge, mais transférer sa mémoire de travail peut ralentir la première réponse, rapporte l'équipe de vLLM.

Le projet open source d'inférence a testé le « service désagrégé », où un GPU gère le prefill et un autre le décodage. Le prefill lit le prompt et construit le cache clé-valeur ; le décodage utilise ce cache pour générer les tokens. Le guide déplace aussi la tokenisation et l'analyse des sorties vers une interface frontale sans GPU.

Pour un opérateur qui traite de longs prompts, la conception propose un choix entre deux retards. Séparer les phases empêche un gros prompt d'interrompre la génération des autres utilisateurs, mais le cache doit circuler entre les workers avant le début du décodage.

Dans le test de vLLM sur deux GPU avec Qwen2.5-7B et des prompts de 8 000 tokens, le 99e percentile de l'intervalle entre tokens générés est passé de 23 à 169 millisecondes dans la configuration combinée à 0,4 requête par seconde. La configuration séparée maintenait cet intervalle entre 25 et 52 millisecondes.

La même expérience a montré le coût. Transférer environ 470 Mo de cache par prompt prenait environ 1,3 seconde, et le délai médian jusqu'au premier token atteignait 2,2 secondes, contre 0,7 seconde lorsque les deux phases partageaient un worker. Les GPU L40S n'avaient ni NVLink ni transfert direct pair-à-pair : le résultat décrit donc une voie de transport volontairement défavorable, plutôt que tous les déploiements.

La règle de décision des auteurs est pratique : vérifier d'abord la topologie GPU, puis examiner les mesures de transfert du cache avec la longueur de prompt et le rythme de requêtes prévus. La désagrégation est surtout intéressante quand le prefill perturbe régulièrement le décodage ou quand les deux phases doivent évoluer différemment. Un serveur peu chargé peut payer le coût du transfert sans bénéficier d'une isolation utile.

Le guide cite des résultats plus importants d'AMD et du projet llm-d, mais ces tests utilisent d'autres modèles, accélérateurs et tailles de cluster. Ils soutiennent le potentiel de l'architecture, pas un facteur d'accélération transposable.

Les instructions visent vLLM 0.30.0 ou ultérieur et comprennent des services renderer et derenderer séparés. L'équipe indique que des lacunes d'intégration subsistent, faisant des vérifications de topologie et de transfert un préalable plutôt qu'une optimisation après déploiement.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| vLLM documente des services séparés de prefill, décodage et interface frontale sans GPU | VÉRIFIÉ | [Guide vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | configuration et commandes vLLM publiques |
| À 0,4 requête/s, l'intervalle p99 entre tokens colocalisés atteignait 169 ms, tandis que le service séparé restait à 25–52 ms | SELON LA SOCIÉTÉ | [Guide vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | aucune ; test du projet |
| Un prompt de 8 000 tokens produisait environ 470 Mo de cache et un transfert d'environ 1,3 s | SELON LA SOCIÉTÉ | [Guide vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | aucune |
| Le délai médian au premier token était de 2,2 s avec séparation contre 0,7 s avec colocalisation | SELON LA SOCIÉTÉ | [Guide vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | aucune |
| Le test utilisait deux GPU L40S sans NVLink ni transfert pair-à-pair | VÉRIFIÉ | [Guide vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | configuration de test indiquée par les auteurs |
| Le guide vise vLLM 0.30.0 ou ultérieur | VÉRIFIÉ | [Guide vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | version exigée dans le guide |

+++
title = "bilibili enrichit Index-Translate de versions pour un usage local"
slug = "bilibili-enrichit-index-translate-versions-locales"
description = "La famille ouverte de traduction dispose désormais de paquets GGUF, FP8 et NVFP4, d'une API compatible gratuite et de quatre benchmarks publics. Ses chiffres de performance restent ceux du développeur."
tags = ["models", "tools"]
date = 2026-10-05T04:01:30+02:00
draft = false
+++

bilibili a ajouté les 3 et 4 octobre des versions quantifiées officielles, une interface publique gratuite et quatre ensembles d'évaluation à Index-Translate, rendant ses modèles de traduction récemment publiés plus pratiques pour un usage local ou hébergé.

La famille traduit du texte dans 150 langues et accepte des instructions sur la terminologie, la mise en forme et le style. Ses modèles textuels ordinaires comptent 2 milliards, 9 milliards et, pour la version préliminaire, 35 milliards de paramètres. Le plus grand est un modèle à mélange d'experts qui active environ 3 milliards de paramètres par token.

Le changement important pour les utilisateurs locaux concerne les paquets. Les versions GGUF ciblent désormais llama.cpp, les versions FP8 ciblent vLLM et les versions NVFP4 les GPU Blackwell récents. Le projet publie ces formats dans ses gammes textuelles, à nombre de syllabes contrôlé et pour les longs documents. Ses modèles vocaux disposent aussi de paquets quantifiés, même si les dépôts GGUF contiennent uniquement leurs bases de modèles textuels, et non toute la chaîne de traitement vocal.

Le nouveau point d'accès hébergé expose la version préliminaire 35B-A3B au moyen d'une interface compatible avec l'API de conversation d'OpenAI. Les développeurs peuvent ainsi tester le modèle sans devoir d'abord disposer du matériel approprié. Le dépôt présente ce point d'accès comme gratuit, mais ne promet ni niveau de service ni tarification à long terme.

Index-Translate va au-delà de la traduction de phrases. Le client peut préserver la structure JSON et Markdown, imposer un glossaire et demander un ton particulier. Des paquets associés traduisent la parole, visent un nombre de syllabes demandé pour le doublage ou maintiennent le contexte sur un long document. Ces fonctionnalités traitent les difficultés de la traduction en production qu'un prompt générique « traduis ceci » tend à manquer.

bilibili a également publié les ressources des benchmarks instTrans, MEME, SandGlass et NativeLong avec des scripts d'évaluation. La conception des tests devient ainsi consultable, mais les scores publiés restent les mesures du développeur. Dans le rapport technique, le modèle préliminaire obtient 0,8794 sur FLORES COMET-22 et 76,76 avec le juge WMT26. Ce dernier utilise GPT-5.6-Sol comme évaluateur : il ne faut donc pas y voir une comparaison humaine indépendante.

La famille de modèles initiale est arrivée le 30 septembre ; il ne s'agit pas du lancement d'un nouveau modèle de fondation. L'actualité est qu'en quatre jours, elle a acquis les formats de déploiement, le point d'accès de test et les artefacts d'évaluation nécessaires pour passer d'une annonce de modèle à quelque chose que les développeurs peuvent effectivement essayer.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| API publique et quatre benchmarks publiés le 4 octobre ; versions quantifiées publiées le 3 octobre | VÉRIFIÉ | [Dépôt du projet](https://github.com/bilibili/Index-Translate) | aucune |
| Les modèles textuels couvrent 150 langues et prennent en charge les contraintes de terminologie, de mise en forme et de style | VÉRIFIÉ | [Dépôt du projet](https://github.com/bilibili/Index-Translate) | [Fiche du modèle](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) |
| Paquets GGUF, FP8 et NVFP4 et environnements d'exécution ciblés documentés | VÉRIFIÉ | [Dépôt du projet](https://github.com/bilibili/Index-Translate) | liens vers les différents paquets dans le dépôt |
| Le modèle préliminaire compte 35B paramètres au total et environ 3B paramètres actifs | VÉRIFIÉ | [Fiche du modèle](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) | aucune |
| FLORES COMET-22 à 0,8794 et juge WMT26 à 76,76 | SELON LA SOCIÉTÉ | [Rapport technique](https://arxiv.org/abs/2609.40181) | aucune ; le rapport utilise GPT-5.6-Sol comme juge pour WMT26 |
| Les nouveaux paquets rendent la famille plus pratique à tester localement ou par un point d'accès hébergé | ANALYSE | [Dépôt du projet](https://github.com/bilibili/Index-Translate) | déduction tirée des artefacts publiés ; pérennité du point d'accès non établie |

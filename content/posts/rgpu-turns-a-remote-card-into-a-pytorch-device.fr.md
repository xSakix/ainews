+++
title = "rGPU fait d'une carte distante un périphérique PyTorch"
slug = "rgpu-fait-d-une-carte-distante-un-peripherique-pytorch"
description = "Le projet sous licence Apache garde Python et le code du modèle sur la machine cliente, tandis que les tenseurs et les opérations CUDA s'exécutent sur un GPU NVIDIA distant."
tags = ["projects", "hardware", "tools"]
date = 2026-10-08T03:55:31+02:00
draft = false
+++

Le projet open source rGPU permet à un programme PyTorch de continuer à fonctionner sur un portable pendant que ses tenseurs et ses opérations résident sur un GPU NVIDIA distant.

Le système sous licence Apache propose deux voies. Le nouveau code PyTorch peut choisir `device="rgpu"`, tandis qu'une couche de compatibilité CUDA plus large intercepte les appels de binaires Linux existants et les transmet à un serveur par le réseau.

Pour un développeur disposant d'un Mac ou d'une station modeste et d'une machine GPU inutilisée ailleurs, cette séparation préserve l'environnement local de développement sans déplacer toute l'application dans un notebook cloud ou un shell distant. Le client peut créer un tenseur sur le périphérique distant avec la syntaxe PyTorch habituelle, et le lanceur fourni établit un tunnel SSH vers le serveur.

La voie simple du périphérique transmet les opérations PyTorch par TCP. La voie de compatibilité implémente des couches d'adaptation pour le pilote et l'environnement d'exécution CUDA ainsi que cuBLAS, cuBLASLt et cuDNN, afin d'exécuter des binaires CUDA PyTorch standard. Le dépôt décrit cette couche comme couvrant une surface de compatibilité plus large : la prise en charge dépendra donc des appels de bibliothèque utilisés par l'application.

rGPU comprend un exemple d'entraînement nanoGPT, des références d'opérations et de configuration, des notes de performance et des tests couvrant ses composants Python et C++. Des travaux expérimentaux sur JAX figurent dans le dépôt, mais ne sont pas présentés comme une voie produit prise en charge.

La sécurité réseau est la principale contrainte opérationnelle. Aucun des deux protocoles n'authentifie ni ne chiffre son trafic. La documentation demande de limiter le serveur d'opérations à localhost et de se connecter par SSH ; le serveur CUDA écoute sur toutes les interfaces IPv4, il faut donc aussi restreindre le port 9713 par les règles du pare-feu de l'hôte ou du cloud.

Le projet transforme l'accélération distante en choix de périphérique plutôt qu'en environnement d'exécution distinct, mais ses affirmations de performance et de compatibilité viennent actuellement de la documentation du mainteneur. Le code, les tests et les traces d'ingénierie peuvent être inspectés, et aucune version étiquetée n'est encore répertoriée sur sa page GitHub.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| rGPU garde l'application sur le client pendant que les tenseurs et le calcul GPU s'exécutent sur une machine NVIDIA distante | VÉRIFIÉ | [Dépôt rGPU](https://github.com/ymcrcat/rgpu) | aucune |
| Le projet offre un périphérique PyTorch `rgpu` et une couche de compatibilité CUDA | VÉRIFIÉ | [Dépôt rGPU](https://github.com/ymcrcat/rgpu) | aucune |
| La couche couvre les interfaces du pilote CUDA, de CUDA Runtime, cuBLAS, cuBLASLt et cuDNN | VÉRIFIÉ | [Dépôt rGPU](https://github.com/ymcrcat/rgpu) | aucune |
| Aucun protocole ne fournit authentification ou chiffrement ; la documentation prescrit SSH et des restrictions de pare-feu | VÉRIFIÉ | [Dépôt rGPU](https://github.com/ymcrcat/rgpu) | aucune |
| Le dépôt comprend des tests, un exemple nanoGPT et des travaux expérimentaux sur JAX | VÉRIFIÉ | [Dépôt rGPU](https://github.com/ymcrcat/rgpu) | aucune |
| Les caractéristiques de compatibilité et de performance sont documentées par le mainteneur du projet | SELON LA SOCIÉTÉ | [Dépôt rGPU](https://github.com/ymcrcat/rgpu) | aucune |

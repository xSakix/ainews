+++
title = "Google a réduit l'attente entre clusters d'entraînement"
slug = "google-a-reduit-l-attente-entre-clusters-d-entrainement"
description = "Google a fait échanger des mises à jour plus petites à deux groupes de TPU lors de l'entraînement d'un modèle de 32 milliards de paramètres. Le temps par étape s'est maintenu sous une contrainte réseau simulée, ce qui laisse en suspens ce que coûtera la méthode entre de véritables centres de données."
tags = ["research", "hardware", "models"]
date = 2026-11-22T06:29:30+01:00
draft = false
+++

Les ingénieurs de Google ont fixé un plafond de bande passante entre deux groupes de TPU. À 10 gigabits par seconde, une étape d'entraînement classique en parallélisme de données a pris 55,11 secondes. Le même modèle a mis 5,76 secondes par étape lorsque les groupes ont échangé des mises à jour plus petites en arrière-plan.

L'expérience, publiée par Google en novembre, a testé Qwen3-32B sur deux tranches de TPU v5p-32. Ces tranches reposaient sur un réseau rapide. L'équipe a utilisé le contrôle de trafic Linux pour simuler le type de bande passante limitée qui peut séparer deux groupes d'accélérateurs. Ce dispositif lui a permis de garder le matériel et le modèle constants tout en faisant varier la quantité de données pouvant transiter par la liaison.

## Quand la liaison dicte le rythme

Dans un entraînement standard en parallélisme de données, chaque groupe reçoit une copie du modèle et un lot différent d'exemples d'entraînement. Après avoir calculé les gradients, qui indiquent comment modifier les paramètres du modèle, les groupes les combinent afin que les copies restent synchronisées. Sur un réseau rapide, une partie de cet échange peut se dérouler en parallèle du calcul. Dès que cet échange dure plus longtemps que le calcul capable de le masquer, les accélérateurs doivent attendre.

Google estime que sa configuration en parallélisme de données a échangé environ 65,5 gigaoctets sur la liaison à chaque étape. Lorsque la liaison fonctionnait à pleine vitesse, la configuration de référence a demandé environ 5,6 secondes par étape. À 30 gigabits par seconde, il lui a fallu 19,41 secondes. Le modèle et la quantité de travail par étape sont restés les mêmes. L'essentiel du temps supplémentaire a servi à transmettre les mises à jour.

C'est ce problème qu'Arthur Douillard et ses collègues ont cherché à résoudre avec les travaux initiaux sur DiLoCo. Dans leur étude sur l'entraînement de modèles de langage sur C4, les chercheurs ont laissé huit groupes s'entraîner indépendamment par séquences avant de regrouper périodiquement leurs mises à jour. Ils ont rapporté avoir égalé un entraînement entièrement synchrone tout en échangeant 500 fois moins de données dans cette expérience précise. L'étude reposait sur une configuration différente de celle du nouveau benchmark (banc d'essai) MaxText, de sorte que les deux réductions de trafic mesurent des choses différentes.

## Modifier le moment où circulent les mises à jour

La version initiale de DiLoCo conservait un problème à la fin de chaque séquence. Les étapes moins coûteuses s'exécutaient à pleine vitesse, puis les groupes devaient synchroniser l'ensemble du modèle d'un seul coup. Avec le plafond de 10 gigabits dans le nouveau benchmark de Google, DiLoCo classique affichait en moyenne 7,55 secondes par étape et subissait encore une pause périodique. Pour un système d'entraînement qui reste occupé la majeure partie du temps, une pause à intervalles réguliers peut représenter une part importante de la moyenne.

L'article de 2025 sur Streaming DiLoCo a modifié ce calendrier. Au lieu d'envoyer l'ensemble du modèle en une seule opération, les groupes en échangent des morceaux de manière séquentielle. Les étapes d'entraînement suivantes peuvent se poursuivre pendant que le transfert est en cours. L'article a également exploré la quantification des données échangées, ce qui réduit le nombre de bits nécessaires pour les représenter. La distinction de fond oppose la quantité de données qu'un système envoie sur l'ensemble d'une session d'entraînement à celle qu'il tente d'envoyer en une seule fois.

Dans l'expérience MaxText, l'équipe a découpé Qwen3-32B en 65 fragments. Un groupe pouvait s'entraîner pendant que les processeurs hôtes synchronisaient environ un gigaoctet de données pour un fragment en arrière-plan. Sur 65 étapes, le trafic entre les tranches est passé de 4 258,8 gigaoctets avec le parallélisme de données standard à 67 gigaoctets avec Streaming DiLoCo. Le temps moyen par étape est resté à 5,76 secondes aussi bien à 30 qu'à 10 gigabits par seconde. Sans restriction de bande passante, les trois méthodes ont achevé leurs étapes en un temps à peu près équivalent.

## L'expérience a mesuré plus que le trafic

Un modèle qui passe moins de temps à attendre peut tout de même être moins bon à l'issue de l'entraînement. Laisser les unités de calcul se mettre à jour indépendamment modifie la séquence de poids que chacune observe. Google a particulièrement cité les modèles à mélange d'experts, dans lesquels un routeur décide quelles parties du modèle traitent chaque token (jeton). Si les routeurs apprennent indépendamment trop longtemps, ils peuvent apprendre à diriger des exemples similaires vers des experts différents.

L'équipe MaxText a comparé la perte de validation sur des exécutions de 4 000 étapes pour deux modèles de ce type, Qwen3-30B-A3B et Gemma4-26B-A4B. Elle indique que les exécutions en streaming ont égalé ou légèrement amélioré la référence synchrone. Pour l'exécution sur Qwen, l'équipe a ajusté la synchronisation durant les quelque 800 premières étapes. Ce résultat mesure la qualité des prédictions obtenues sur des données mises de côté pendant la période testée. Il laisse en suspens l'ampleur des réglages qu'exigeraient d'autres modèles et des exécutions plus longues.

Pour les équipes qui doivent obtenir de la capacité sur plusieurs sites, deux questions distinctes se posent. La première est de savoir si la tâche d'entraînement peut continuer à calculer pendant que les mises à jour circulent. La seconde porte sur ce qu'il en coûte d'atteindre un niveau de qualité requis lorsque le réseau présente une latence réelle, des pannes et un trafic que l'expérience n'a pas reproduits. La comparaison de débit s'appuyait sur un seul modèle dense et deux groupes d'accélérateurs. Les essais de qualité répondent à une autre question sur un nombre limité d'étapes. Google ne fournit aucune comparaison de coûts ni aucune mesure du temps nécessaire pour atteindre une perte cible sur des sites réels.

Les ingénieurs avaient commencé par plafonner une liaison qui pouvait autrement absorber le trafic. Une fois le plafond activé, ils ont vu le parallélisme de données classique mettre près de 50 secondes supplémentaires par étape. Streaming DiLoCo a achevé une étape en un temps presque identique avec ou sans plafond.

## Références

- Douillard, A., Feng, Q., Rusu, A. A., et al. (2023). *DiLoCo: Distributed Low-Communication Training of Language Models*. https://arxiv.org/abs/2311.08105
- Douillard, A., Donchev, Y., Rush, K., et al. (2025). *Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch*. https://arxiv.org/abs/2501.18512
- Khatwani, M., Zuo, C., Fallen, N., et al. (2026). *Distributed LLM Training Across Metros: Streaming DiLoCo in MaxText*. https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/

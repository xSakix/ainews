+++
title = "La confiance d’un modèle ne reflétait pas une croyance unique"
slug = "confiance-modele-ne-refletait-pas-croyance-unique"
description = "Une nouvelle prépublication a séparé ce que dit un utilisateur de la réponse qu’il fournit. Quatre signaux de confiance ont alors raconté quatre histoires différentes, et les erreurs qui résistaient à une contestation cédaient rarement sans nouvel élément de preuve."
tags = ["research", "models"]
date = 2026-10-30T04:09:11+01:00
draft = false
+++

À 9 h 14, dans un service d’assistance qui n’existe que pour cette illustration, une analyste demande à un assistant le nom d’un règlement. La réponse est fausse. Elle redemande, et l’assistant reprend les mêmes mots avec moins d’assurance. Elle ouvre une nouvelle conversation et les reçoit encore une fois. La confiance a changé. Pas la réponse.

## Une conversation, quatre signaux

Duc-Vinh Tran, chercheur à Hanoi University of Science and Technology, a conçu une expérience autour de cette séparation. Sa prépublication, déposée le 26 octobre, ne propose pas un meilleur score de confiance. Elle pose une question plus fondamentale : lorsqu’un utilisateur relance le modèle, qu’est-ce qui change ?

La réponse compte, car les systèmes conversationnels donnent désormais des conseils dans la recherche, le tutorat et l’assistance. Les personnes qui les exploitent doivent savoir quand une réponse peut être utilisée sans risque et si une contestation a corrigé une erreur. De nombreuses évaluations traitent quatre signaux comme des estimations d’une même croyance sous-jacente : la confiance exprimée verbalement, la vraisemblance des tokens, le jugement du modèle sur la véracité de sa réponse et une sonde des activations cachées.

Tran a mesuré les quatre sur les mêmes conversations. Il a également décomposé le deuxième tour de l’utilisateur en deux parties. L’acte de langage décrivait ce que faisait l’utilisateur : redemander, approuver ou dire au modèle qu’il avait tort. Le contenu fourni indiquait si l’utilisateur proposait une réponse possible et si celle-ci était correcte.

Ce dispositif sépare deux éléments que les conversations ordinaires réunissent. Un utilisateur peut dire qu’une réponse est fausse et en fournir une autre. Si le modèle modifie sa réponse, la contestation peut avoir déclenché une réflexion, ou le texte de remplacement peut simplement l’avoir attiré vers un autre texte.

Le texte de la réponse a fait l’essentiel du travail. Dans chaque comparaison de taille complète entre un modèle et un jeu de données retenue dans l’article, un texte correct a corrigé au moins quatre fois plus de mauvaises réponses qu’une simple relance ou une approbation. Un texte plausible mais faux pouvait aussi détourner une réponse correcte. Une contestation sans contenu rendait les réponses instables sans les orienter vers la vérité.

## La confiance s’est dissociée

Les quatre mesures ne montaient ni ne baissaient ensemble. Sur Qwen2.5-7B, la confiance verbale diminuait au fil de la conversation, même lorsque la précision restait stable ou s’améliorait. La vraisemblance de la séquence générée augmentait souvent en parallèle. P(True), une méthode qui demande au modèle de juger si sa propre réponse proposée est vraie, bougeait à peine, sauf lorsqu’une proposition fausse contredisait une bonne réponse.

La sonde de l’état caché a donné le résultat le plus frappant. Tran a ajusté un classifieur linéaire aux activations du premier tour pour prédire si la réponse était correcte, puis l’a figé avant que l’utilisateur reprenne la parole. Si cette sonde captait un signal stable de vérité, son score ne devrait monter que lorsque la réponse devient correcte. Or, sur Qwen2.5-7B, il augmentait quand le modèle conservait une mauvaise réponse comme lorsqu’il adoptait la bonne. Il baissait lorsqu’une réponse correcte était attirée vers une proposition fausse.

Tran parle donc d’une mesure de persistance, pas d’un détecteur de vérité. Ce nom décrit une association observée. L’article n’affirme ni que cette mesure pousse le modèle à conserver une réponse, ni qu’elle représente une croyance psychologique.

Pour Qwen2.5-7B, le résultat s’est maintenu lorsque la sonde a été testée sur des questions qu’elle n’avait pas vues. Une analyse nettoyée de Llama-3-8B l’a corroboré. Quatre autres modèles n’ont pas reproduit l’effet sur des questions réservées au test. L’analyse principale utilise également des questions en anglais à réponse courte, et son ensemble d’erreurs persistantes contient 81 cas de Qwen2.5-7B. Elle ne teste ni les agents de programmation, ni les conversations naturelles, ni les modèles commerciaux fermés.

Ces limites encadrent la conclusion. L’article n’établit pas que les activations cachées codent généralement l’attachement à une réponse. Il montre que des mesures souvent appelées confiance par les chercheurs peuvent réagir à différentes parties d’un même échange contrôlé.

## Pourquoi redemander n’a pas suffi

Des travaux antérieurs avaient déjà montré certains aspects du problème. Dans l’expérience FlipFlop, Philippe Laban et ses collègues ont contesté les réponses de dix modèles avec des phrases comme « Êtes-vous sûr ? ». Les modèles ont changé de réponse dans 46 % des cas en moyenne, et la précision finale a baissé de 17 %. Une contestation provoquait un mouvement sans produire de façon fiable une amélioration.

Dharshan Kumaran a ensuite constaté que la confiance verbale prédisait mieux le choix du modèle de s’engager sur une réponse ou de s’abstenir que la justesse de sa réponse. Les probabilités de tokens calibrées présentaient le profil inverse. Des tests mécanistes sur des modèles Gemma ont montré qu’un état après la réponse codait déjà la décision ultérieure de répondre ou de s’abstenir, et que l’orientation de cet état modifiait cette décision.

D’autres travaux ont trouvé des formes d’autoévaluation plus encourageantes. Saurav Kadavath et ses collègues ont rapporté en 2022 que les grands modèles pouvaient estimer P(True) pour leurs réponses proposées et prédire s’ils connaissaient une réponse lorsque les formats s’y prêtaient. Un article ACL de 2026 de Caiqi Zhang et ses collègues a introduit P(Sufficient), qui suivait mieux que les solutions courantes l’accumulation de preuves suffisantes sur plusieurs tours.

L’apport de Tran consiste à appliquer plusieurs signaux à des transcriptions identiques et à contrôler le tour de l’utilisateur. Les mesures obtenues ne sont pas interchangeables. Un système qui améliore la calibration de l’une peut laisser les autres inchangées.

## Les preuves devaient contenir la réponse

Les erreurs persistantes étaient difficiles à corriger sans nouveau contenu. Parmi les 81 erreurs de Qwen2.5-7B qui subsistaient après une première relance, les demandes répétées en ont corrigé deux au cinquième tour et trois au dixième. Une nouvelle conversation n’en a corrigé aucune. Proposer une option d’abstention a conduit le modèle à s’abstenir dans 94 % des cas erronés, mais tous les cas où il répondait encore restaient faux.

Fournir le texte d’une bonne réponse a changé le résultat. Selon la formulation, cela a corrigé de 75 à 95 % des mêmes erreurs. Deux réplications préenregistrées sur quatre modèles ont maintenu les taux de correction sous un seuil de 15 % pour les interventions ne contenant pas de réponse, à l’exception d’un résultat limite avec une autre méthode d’étiquetage.

L’article a ensuite remplacé la réponse connue comme correcte par des preuves récupérées dans TriviaQA. Une recherche BM25 sélectionnait une phrase dans les documents justificatifs. Lorsque cette phrase contenait une variante correcte de la réponse, elle corrigeait 67 à 76 % des erreurs persistantes. Sinon, elle en corrigeait 2 à 12 % et dégradait parfois des réponses auparavant correctes.

Cette observation ne valide pas une règle pour les systèmes de recherche d’information en production. Un contrôle connaissant la bonne réponse a réduit les dommages dans un test a posteriori. Un contrôle déployable sans cette connaissance, qui comparait les éléments à la propre réponse du modèle, a corrigé peu d’erreurs. Les chercheurs n’ont testé ni la recherche dense ni une vérification par un juge. Ils présentent la présence de la réponse comme une heuristique qui nécessite encore une évaluation de bout en bout.

## Un problème de mesure pour les concepteurs

La leçon pratique ne justifie pas l’affirmation générale selon laquelle les modèles ne savent rien. Les concepteurs devraient nommer le signal qu’ils mesurent et l’intervention qui le modifie. La confiance verbale peut refléter une disposition à s’engager. La vraisemblance d’une séquence peut refléter sa fluidité. P(True) peut réagir à une contradiction explicite. Une sonde d’activation figée peut suivre la réponse qu’un modèle continue de donner.

Les évaluations doivent aussi séparer la position de l’utilisateur de l’information contenue dans son message. Dire qu’une réponse est fausse et fournir la bonne réponse sont deux interventions différentes. Les combiner empêche de savoir si le modèle a réexaminé sa réponse ou copié.

Dans le service d’assistance fictif, l’analyste ajoute une étape avant de clore le ticket. Elle récupère le règlement lui-même et vérifie si le passage pertinent contient une réponse possible. L’assistant modifie sa réponse. Elle ne consigne comme preuve ni sa nouvelle assurance ni son ancienne réticence. Ce qui a changé la situation, c’est un élément de preuve porteur de contenu, pas une deuxième demande formulée plus fermement.

## Références

- Kadavath, S., Conerly, T., Askell, A., et al. (2022). *Language Models (Mostly) Know What They Know*. https://arxiv.org/abs/2207.05221
- Kumaran, D. (2026). *Reported Confidence in LLMs Tracks Commitment More Than Correctness*. https://arxiv.org/abs/2606.29490
- Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2024). *Are You Sure? Challenging LLMs Leads to Performance Drops in the FlipFlop Experiment*. https://arxiv.org/abs/2311.08596
- Tran, D.-V. (2026). *Not One Belief: Answer Payloads, Persistence, and Dissociated Confidence Signals in Conversational Question Answering*. https://arxiv.org/abs/2610.35694
- Zhang, C., Yang, R., Zhu, X., et al. (2026). *Confidence Estimation for LLMs in Multi-turn Interactions*. https://aclanthology.org/2026.findings-acl.1280/

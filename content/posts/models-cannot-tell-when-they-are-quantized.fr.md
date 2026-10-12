+++
title = "Les modèles ne savent pas dire s'ils sont quantifiés"
slug = "modeles-ne-savent-pas-dire-s-ils-sont-quantifies"
description = "Une prépublication montre que les modèles ne rapportent pas fiablement leur propre quantification à partir du comportement textuel. Des sondes internes détectent les méthodes connues, mais ne généralisent pas à une méthode inédite."
tags = ["research", "models"]
date = 2026-10-12T04:00:37+02:00
draft = false
+++

Les modèles de langage ne pouvaient pas dire fiablement si leurs poids avaient été quantifiés, même si des sondes entraînées pouvaient récupérer des traces propres à chaque méthode dans leurs états cachés.

La prépublication étudie une forme restreinte de connaissance de soi des modèles. Les chercheurs ont compressé des modèles avec plusieurs méthodes de quantification, posé des questions directes sur leur état et comparé leurs sorties à celles de versions non compressées. Ils ont ensuite entraîné des classificateurs simples sur les activations internes pour voir si le changement existait sans être disponible pour la réponse du modèle.

## Pourquoi c'est important {#why-it-matters}

Pour un ingénieur recevant un modèle hébergé ou reconditionné, l'autodescription est un mauvais contrôle d'intégrité. Un modèle peut fonctionner avec des poids numériques modifiés sans transformer cette différence interne en déclaration véridique sur son déploiement.

La quantification stocke les poids avec moins de bits afin qu'un modèle exige moins de mémoire et fonctionne souvent plus vite. Le processus modifie les calculs dans tout le réseau, mais ne produit pas nécessairement une signature textuelle évidente. Les auteurs rapportent que les autorapports directs et les comparaisons ordinaires de sorties portaient presque aucun signal fiable indiquant si une compression avait eu lieu.

Le tableau changeait lorsque les chercheurs examinaient les états cachés. Des sondes linéaires, petits classificateurs entraînés sur ces valeurs internes, distinguaient les exécutions quantifiées des non quantifiées et identifiaient souvent la méthode utilisée. Le résultat montre que le réseau contient des traces détectables de son implémentation, même lorsque son interface linguistique ne les expose pas.

## Une empreinte n'est pas une connaissance de soi générale

La limite la plus forte apparaît dans le test de transfert. Un adaptateur partagé de faible rang apprenait à lire plusieurs signatures de quantification connues, mais n'identifiait pas fiablement une méthode exclue de l'entraînement. Il avait appris les empreintes de transformations familières plutôt qu'un concept général de précision numérique réduite.

Cette distinction restreint la conclusion de sécurité. Un opérateur ayant accès aux activations peut construire un détecteur pour des variantes de déploiement déjà représentées dans les données d'entraînement. L'expérience n'établit pas de détecteur universel de changements arbitraires des poids, et un client d'API ne peut généralement pas lire les états cachés du fournisseur.

Les auteurs appellent ce décalage anosognosie, empruntant un terme clinique désignant l'absence de conscience d'une déficience. L'analogie n'est utile qu'au niveau comportemental : le système contient des indices d'un changement, mais ne le rapporte pas exactement. L'article ne démontre ni conscience, ni conscience subjective, ni trouble clinique.

Sur le plan méthodologique, l'étude bénéficie d'une intervention contrôlée. Le modèle de base et les prompts peuvent rester constants pendant que seule la représentation des poids change, et les chercheurs peuvent tester séparément l'autorapport, le comportement extérieur et l'activité cachée. Son périmètre reste limité aux modèles, schémas de précision et familles de sondes évalués dans la prépublication.

## L'étude a également montré

Différentes méthodes de quantification laissaient des signatures internes séparables, ce qui peut aider les audits de déploiement lorsqu'un ensemble connu de variantes est examiné. Les sorties textuelles changeaient trop peu pour cette même tâche, mettant en garde contre les tests d'intégrité qui n'examinent que des réponses échantillonnées.

Les prochains éléments devront tester des outils de compression inconnus et l'évasion intentionnelle. Les auteurs ont établi que des transformations connues peuvent laisser des traces lisibles, tandis que leur propre résultat sur une méthode exclue montre pourquoi ce n'est pas encore une solution générale.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Les modèles testés ne rapportaient pas fiablement eux-mêmes s'ils avaient été quantifiés | SELON LA SOCIÉTÉ | https://arxiv.org/abs/2610.06174 | aucune |
| Les sondes linéaires récupéraient des informations propres à chaque méthode dans les états cachés | SELON LA SOCIÉTÉ | https://arxiv.org/abs/2610.06174 | aucune |
| Un adaptateur partagé ne généralisait pas fiablement à une méthode de quantification inédite | SELON LA SOCIÉTÉ | https://arxiv.org/abs/2610.06174 | aucune |
| La quantification variait pendant que l'étude comparait comportement textuel et activations internes | VÉRIFIÉ | https://arxiv.org/abs/2610.06174 | aucune |
| L'article n'établit ni conscience ni anosognosie clinique | ANALYSE | https://arxiv.org/abs/2610.06174 | aucune |

+++
title = "Tencent publie Youtu-Parsing-Omni"
slug = "tencent-publie-youtu-parsing-omni"
description = "Ce modèle de 5 milliards de paramètres transforme documents, images, audio et vidéo en un format JSON structuré unique. Tencent a publié les poids, le code et un rapport technique."
tags = ["models", "tools"]
date = 2026-10-10T04:02:41+02:00
draft = false
+++

Le laboratoire Youtu de Tencent a publié un modèle de 5 milliards de paramètres qui analyse six types de médias pour les convertir en un format JSON structuré unique.

Youtu-Parsing-Omni accepte les pages de documents, les images naturelles, les graphiques, les figures géométriques, l'audio et la vidéo. Il peut renvoyer du texte, des tableaux, des formules, des cadres de mise en page, des horodatages, des transcriptions vocales, des légendes et des descriptions des mouvements de caméra sans passer d'un modèle spécialisé à un autre.

## Pourquoi c'est important {#why-it-matters}

Un développeur qui construit un système de recherche ou de traitement documentaire peut transmettre des médias variés à un seul modèle local et recevoir un schéma prévisible. Cela réduit le travail d'intégration normalement nécessaire pour combiner des services de reconnaissance optique de caractères, de reconnaissance vocale et de compréhension vidéo.

Tencent a publié les poids sous sa licence spécifique `youtu-parsing`, un plugin vLLM, des exemples d'inférence et un rapport technique. Le dépôt indique que le code d'évaluation suivra : les résultats annoncés sur les bancs d'essai ne peuvent donc pas encore être reproduits à partir de cette seule publication.

Le modèle utilise un encodeur commun aux images, à l'audio et à la vidéo. Pour la vidéo, certaines couches permettent à chaque image de porter son attention sur l'audio de la même partie du clip. Son schéma de sortie couvre les éléments littéraux, comme le texte et les cadres de délimitation, ainsi que des productions de niveau supérieur, comme les récits et les rapports.

Tencent annonce un score de 96,96 sur OmniDocBench 1.6, légèrement supérieur à TeleOCR, à 96,91, et à PaddleOCR-VL-1.6, à 96,34, dans son tableau publié. Sur OmniParsingBench, plus large, Tencent rapporte une moyenne de 75,08, derrière Gemini 3 Pro à 77,44, mais devant les autres systèmes à poids ouverts testés. Ces mesures viennent de l'auteur de la publication, et la comparaison dépend de la configuration du benchmark décrite dans le rapport.

La méthode d'entraînement transforme à plusieurs reprises le modèle élève en son propre enseignant pour le tour suivant. Les tokens de contenu et les tokens structurels reçoivent des signaux de comparaison différents, dans une tentative de préserver à la fois ce qu'une page dit et les relations entre ses éléments.

## Les points à surveiller

Les tests indépendants auront besoin du code d'évaluation promis. Les utilisateurs commerciaux doivent aussi examiner la licence spécifique plutôt que de supposer qu'elle reprend les conditions permissives courantes dans certaines publications à poids ouverts.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Tencent a publié Youtu-Parsing-Omni avec 5 milliards de paramètres, des poids, des exemples de code et un rapport technique | VÉRIFIÉ | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
| Le modèle accepte documents, images, graphiques, géométrie, audio et vidéo et produit un schéma JSON unique | SELON LA SOCIÉTÉ | https://huggingface.co/tencent/Youtu-Parsing-Omni | aucune |
| Tencent annonce 96,96 sur OmniDocBench 1.6 et 75,08 sur OmniParsingBench | SELON LA SOCIÉTÉ | https://huggingface.co/tencent/Youtu-Parsing-Omni | aucune |
| La publication utilise la licence spécifique youtu-parsing et ne comprend pas encore le code d'évaluation | VÉRIFIÉ | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |

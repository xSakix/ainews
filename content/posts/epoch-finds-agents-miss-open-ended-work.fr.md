+++
title = "Epoch constate les limites des agents face au travail ouvert"
slug = "epoch-constate-les-limites-des-agents-face-au-travail-ouvert"
description = "Dans une évaluation issue du travail d'Epoch AI, six modèles ont mieux réussi les tâches définies de programmation et d'analyse que le jugement de recherche, le style maison et la conception d'expériences."
tags = ["agents", "essays", "research"]
date = 2026-10-09T03:59:06+02:00
draft = false
+++

Les agents de pointe ont accompli de façon fiable les parties bien définies du travail d'Epoch AI, mais ont montré leurs limites lorsque les tâches dépendaient de normes implicites, du jugement de recherche ou de la conception d'expériences.

L'institut de recherche à but non lucratif a confié à six modèles 11 tâches réelles issues de ses activités de graphisme, de données, de logiciel et de recherche. Claude Fable 5.1 et GPT-6 Astra ont globalement dominé l'évaluation, sans pouvoir produire l'un ou l'autre un travail de qualité Epoch de bout en bout sans intervention.

**Pourquoi c'est important :** Pour un responsable qui décide de la place des agents dans le travail intellectuel, les évaluations à réponse unique apportent peu d'indications. Les résultats d'Epoch situent l'écart restant dans le choix d'une bonne question, l'apprentissage des normes locales et la capacité à reconnaître qu'une expérience a mesuré autre chose que ce qu'elle devait mesurer.

## De vrais outils ont révélé des défauts de jugement

Epoch a fourni à chaque modèle le contexte qu'il donnerait à une nouvelle recrue : dépôts, références graphiques et accès à des outils comme Figma, Google Drive et des sites d'imagerie satellite. Les modèles utilisaient leur niveau de raisonnement maximal disponible et ne recevaient aucune aide pendant la tâche. Un employé d'Epoch notait ensuite chaque résultat selon une grille propre à sa catégorie.

La suite couvrait cinq types de travail : conception graphique, analyse brève de données, explorateurs de données interactifs, recherche sur les centres de données et conception de recherche. Des contrôles objectifs côtoyaient des critères subjectifs. Cette combinaison permettait d'inclure des qualités comme l'adéquation au public et la valeur d'une expérience, généralement évitées par les évaluations automatisées.

Fable 5.1 et GPT-6 Astra étaient les plus fiables pour la programmation, le calcul et l'utilisation de l'ordinateur. Une simple tâche de remise en forme d'un graphique a été retirée, car la production de Fable atteignait le niveau de l'institut ; Epoch indique désormais automatiser une grande partie de cette étape en interne. Les modèles à poids ouverts Kimi K3 et Qwen 3.8 Max rencontraient plus souvent des difficultés sur les tâches définies comme sur les parties ouvertes.

Les échecs devenaient plus nets lorsqu'une tâche offrait de nombreuses voies défendables. Les modèles disposaient de nombreux exemples du style visuel et éditorial d'Epoch, mais en copiaient les traits de surface sans en déduire les raisons. Astra a choisi un sujet de physique qu'Epoch jugeait trop étroit pour son public généraliste de l'IA ; Fable a produit des schémas et résumés bien plus chargés que ceux habituellement publiés.

La conception de recherche a révélé la frontière la plus difficile. Astra a proposé une question prometteuse sur les raisons pour lesquelles les agents n'apprennent pas de l'expérience, puis mené un pilote où de nombreuses réponses étaient tronquées par une limite de tokens trop basse. Il a remarqué la troncature et relancé l'expérience, mais a tout de même présenté la sensibilité à cette limite comme un résultat de fond. La critique d'Epoch est que l'erreur de configuration ne répondait pas à la question de recherche.

Ces éléments apportent quelque chose que les scores de capacité habituels ne saisissent pas. Un système peut utiliser les outils, écrire le code et calculer le résultat tout en choisissant un sujet peu utile ou en traitant un artefact comme une découverte. Ces erreurs surviennent au moment de cadrer et d'interpréter le travail, là où la justesse devient aussi difficile à noter automatiquement.

La comparaison comporte des limites importantes. Epoch n'a exécuté chaque modèle qu'une seule fois par tâche, avec un seul évaluateur humain par production, selon ses propres normes. Les six modèles utilisaient aussi des environnements d'agents différents : une meilleure intégration du navigateur ou des outils a donc pu peser sur les résultats. Le rapport se lit mieux comme un ensemble de modes d'échec observés que comme un classement général de l'automatisation du travail.

Epoch prévoit d'ajouter des résultats à l'arrivée de nouveaux modèles. Le projet devient ainsi un test longitudinal utile : le changement décisif sera un modèle qui apprend les normes non écrites de l'organisation et rejette sa propre expérience défectueuse, plutôt qu'un modèle qui améliore simplement un score d'évaluation.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Epoch a évalué six modèles sur 11 tâches réparties en cinq catégories de son propre travail | VÉRIFIÉ | [Rapport d'Epoch](https://epoch.ai/publications/can-ai-automate-epoch) | aucune |
| Les modèles recevaient contexte et outils, travaillaient sans intervention et étaient notés manuellement | VÉRIFIÉ | [Rapport d'Epoch](https://epoch.ai/publications/can-ai-automate-epoch) | aucune |
| Fable 5.1 et GPT-6 Astra ont globalement dominé l'évaluation | SELON LA SOCIÉTÉ | [Rapport d'Epoch](https://epoch.ai/publications/can-ai-automate-epoch) | aucune |
| Epoch a retiré une tâche de remise en forme de graphique après que Fable 5.1 a atteint son niveau attendu | SELON LA SOCIÉTÉ | [Rapport d'Epoch](https://epoch.ai/publications/can-ai-automate-epoch) | aucune |
| Les modèles à poids ouverts faisaient davantage d'erreurs sur les tâches définies de cette suite | SELON LA SOCIÉTÉ | [Rapport d'Epoch](https://epoch.ai/publications/can-ai-automate-epoch) | aucune |
| Le pilote d'Astra comptabilisait des réponses tronquées, puis a présenté la sensibilité à la limite de tokens comme un résultat | SELON LA SOCIÉTÉ | [Rapport d'Epoch](https://epoch.ai/publications/can-ai-automate-epoch) | aucune |
| L'évaluation utilisait une exécution par tâche, un évaluateur par production et des environnements différents | VÉRIFIÉ | [Rapport d'Epoch](https://epoch.ai/publications/can-ai-automate-epoch) | aucune |
| Epoch prévoit d'ajouter les résultats de nouveaux modèles | VÉRIFIÉ | [Rapport d'Epoch](https://epoch.ai/publications/can-ai-automate-epoch) | aucune |

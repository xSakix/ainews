+++
title = "Le mois à modèle unique de Wagtail a dépensé moitié ailleurs"
slug = "mois-modele-unique-wagtail-depense-moitie-ailleurs"
description = "Le projet de réaliser les travaux d'ingénierie de septembre sur GLM 5.3 Flash a consommé deux milliards de tokens, dont la moitié seulement sur le modèle visé. Prototypes, capacité des fournisseurs et évaluation expliquent l'écart."
tags = ["essays", "models", "tools"]
date = 2026-10-05T03:57:30+02:00
draft = false
+++

Thibaud Colas, de l'équipe centrale de Wagtail, a tenté de consacrer septembre à des travaux d'ingénierie avec un seul modèle ouvert efficace : GLM 5.3 Flash. Son journal d'utilisation totalise deux milliards de tokens. Un milliard seulement est allé au modèle choisi.

Cela rend l'expérience plus utile qu'un récit de réussite sans accroc. Le modèle visé lui-même a coûté environ 68 dollars et, selon l'estimation de Colas, 4 kWh d'électricité. L'ensemble des travaux du mois a atteint environ 35 kWh au lieu des 10 kWh prévus, car les prototypes, les problèmes des fournisseurs et les évaluations délibérées de modèles ont orienté le trafic ailleurs.

L'échec le plus marqué est venu d'un prototype du serveur expérimental Model Context Protocol de Wagtail, réalisé en « vibe coding ». Colas indique que choisir le mauvais modèle pour cette tâche a consommé 450 millions de tokens, environ 150 dollars et 5 kWh presque en une nuit. Le prototype fonctionnait, mais sa consommation incontrôlée montre à quelle vitesse une expérience agentique peut dominer un budget soigneusement choisi.

L'infrastructure a constitué la deuxième contrainte. Colas rapporte une dégradation des performances de GLM 5.3 Flash et l'attribue aux capacités limitées des fournisseurs d'inférence indépendants. Il a transféré des travaux vers d'autres modèles, dont DeepSeek V4.1 Flash et Qwen 3.8 Flash. Pour une équipe qui cherche à éviter les plus grands laboratoires, la disponibilité fait partie de la qualité du modèle : un modèle entraîné performant n'est pas un choix de production fiable si son point d'accès ralentit sous la demande.

Une partie de l'utilisation hors cible était intentionnelle. Wagtail développe son propre benchmark de tâches : l'équipe devait donc exécuter divers modèles plutôt qu'optimiser uniquement la production quotidienne. Colas propose désormais de réserver la règle du modèle unique à plus de la moitié du travail normal de production, tout en laissant la recherche et le développement libres de comparer les alternatives.

Il reste positif à propos de GLM 5.3 Flash. Le long contexte du modèle, sa prise en charge de la vision et sa disponibilité chez plusieurs fournisseurs l'ont rendu utile pour le développement de Wagtail, les interfaces, la documentation et l'évaluation. Cette appréciation relève de son expérience, et non d'une comparaison contrôlée.

La leçon plus générale est méthodologique. Les totaux de tokens seuls masquent l'origine de la consommation : production planifiée, boucles accidentelles ou évaluation nécessaire. Un tableau de bord opérationnel utile doit inclure au minimum le coût, l'énergie, l'identité du modèle et le résultat de la tâche. Il nécessite aussi des mesures locales et continues : le prototype coûteux n'a été visible qu'après avoir déjà consommé un quart des tokens du mois.

Il s'agit du mois autodéclaré d'une équipe, et non d'une preuve que GLM 5.3 Flash ou les modèles ouverts coûtent généralement un montant particulier. Les tarifs des fournisseurs, les estimations d'énergie et les combinaisons de tâches varient. Ce récit établit un mode d'échec à anticiper : le budget du modèle peut être pertinent alors que le processus qui l'entoure le met en échec.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| L'utilisation de septembre a totalisé deux milliards de tokens, dont un milliard sur GLM 5.3 Flash | VÉRIFIÉ | [Récit de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | aucune ; tableau de bord d'utilisation de l'auteur |
| La part du modèle visé a coûté environ 68 dollars et 4 kWh ; le mois entier a utilisé environ 35 kWh | RAPPORTÉ PAR LA COMMUNAUTÉ | [Récit de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | aucune ; estimations de l'auteur |
| Le prototype a consommé 450 millions de tokens, environ 150 dollars et 5 kWh | RAPPORTÉ PAR LA COMMUNAUTÉ | [Récit de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | aucune ; mesures de l'auteur |
| La capacité des fournisseurs a imposé des changements de modèle | RAPPORTÉ PAR LA COMMUNAUTÉ | [Récit de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | aucune ; diagnostic de l'auteur |
| GLM 5.3 Flash a été utile dans les tâches d'ingénierie de Wagtail | OPINION | [Récit de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | appréciation d'un praticien |
| Modèle, coût, énergie et résultat devraient être mesurés ensemble | ANALYSE | [Récit de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | déduction tirée des modes d'échec rapportés |

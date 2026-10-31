+++
title = "Un agent de classe 4B a appris quand cliquer et quand taper"
slug = "un-agent-de-classe-4b-a-appris-quand-cliquer-et-quand-taper"
description = "Mage-VL-Cowork, le modèle ouvert de Microsoft, agit à l’écran et dans un terminal persistant. Son entraînement montre que réduire la panoplie d’outils du modèle enseignant et récompenser les parcours courts qui aboutissent peut compter davantage que l’ajout d’une interface."
tags = ["models", "agents", "research"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

Une analyste doit fusionner deux bandeaux dans un tableur, ajouter un graphique et conserver le fichier au format `.xlsx`. L’analyste est imaginaire, mais le choix est bien réel : parcourir les menus à la souris, cellule par cellule, ou ouvrir un terminal et modifier le classeur avec Python. Un agent capable de piloter un ordinateur devrait savoir quelle méthode convient avant même le premier clic.

## Une seule stratégie, deux façons d’agir

L’équipe Mage de Microsoft a publié sous licence Apache-2.0 Mage-VL-Cowork, un modèle de 4,74 milliards de paramètres capable d’agir sur un bureau graphique ou dans un environnement Bash et Python qui reste actif entre les commandes. Aucun système externe ne choisit à sa place. À chaque tour, le même modèle qui interprète l’image et le texte décide si la tâche appelle l’une des onze actions à l’écran ou une commande dans le terminal.

La distinction paraît mineure. Elle change pourtant la façon dont l’agent utilise sa fenêtre de contexte et la facilité avec laquelle il peut vérifier son travail. Une capture d’écran peut consommer des milliers de tokens. Une longue suite de manipulations à la souris reproduit parfois mal ce qu’une bibliothèque logicielle exécute avec précision. À l’inverse, le terminal ne voit ni un dessin non enregistré, ni une boîte de dialogue, ni l’état temporaire d’une application. Le modèle a besoin des deux canaux et doit savoir choisir entre eux.

L’équipe Mage annonce un score moyen de 66,04 % sur OSWorld-Verified, obtenu en deux essais de 361 tâches avec une limite de 50 étapes. Les scores respectifs étaient de 65,33 % et 66,75 %. Dans le tableau comparatif de l’équipe, les humains atteignent 72,4 %. GPT-5.4-mini obtient 69,6 % lors d’un essai portant sur les mêmes tâches, avec la même limite d’étapes. Parmi les modèles à poids ouverts, ScaleCUA-Qwen3.5-9B arrive en tête avec 68,7 %. Pour Mage-VL-Cowork, l’équipe revendique donc un résultat plus circonscrit : le meilleur score parmi les modèles de classe 4B.

Ces mesures viennent de Microsoft et n’ont pas été reproduites indépendamment. Le dépôt contient les tâches d’évaluation, le code de l’agent et les scripts de lancement. Ces éléments permettent de vérifier le résultat plus facilement qu’un chiffre isolé sur une fiche de modèle.

## Pourquoi retirer des outils au modèle enseignant

Le travail d’entraînement a commencé en amont du modèle. Même performant, un modèle enseignant disposant de toutes les interfaces ne produisait pas automatiquement des exemples clairs. Plusieurs voies se recoupaient et donnaient à l’élève des indications divergentes : l’arbre d’accessibilité, l’automatisation directe du bureau ou un clic guidé par l’image pouvaient accomplir la même étape de différentes façons.

L’équipe a comparé deux environnements pour l’enseignant sur 672 tâches faisant intervenir plusieurs applications et réservées à l’évaluation. Dans la configuration retenue, GPT-5.4 disposait d’outils graphiques et de programmation. L’équipe avait retiré les utilitaires redondants, tels que `xdotool` et les relevés de données d’accessibilité, et préinstallé des bibliothèques pour les tableurs, les documents, les présentations, les PDF et les images. Cet enseignant a réussi 92,0 % des tâches en 25 étapes en moyenne. Dans l’environnement enrichi de données d’accessibilité, le taux de réussite était de 89,6 % en 35,33 étapes.

L’écart s’est creusé après distillation. Un modèle élève de classe 4B entraîné à partir de l’environnement allégé a atteint 37,6 %, contre 25,1 % pour celui formé à partir de la panoplie plus large. Le nombre moyen d’étapes est passé de 39,40 à 30,91. Les deux résultats viennent de la même équipe de recherche. La comparaison met néanmoins en évidence une difficulté : un modèle de pointe peut composer avec des choix redondants en multipliant les étapes, tandis que le petit modèle hérite de la confusion.

La chaîne de production des données privilégiait elle aussi les éléments réutilisables. Mage-CUA-Forge a généré 293 806 tâches couvrant 6 915 compétences élémentaires et conservé 318 837 parcours hybrides. Au lieu de demander à un agent de recréer chaque environnement de zéro, le système a construit une fois par compétence des procédures réutilisables et des routines de préparation propres aux applications. À modèle de génération identique, l’équipe indique que le nombre de tokens par tâche est passé de 1,276 million à 85 000 et le coût récurrent de 0,906 à 0,158 dollar.

Ce sont des données d’entraînement synthétiques produites à l’échelle industrielle. Leur valeur dépend de la justesse des routines de préparation, de la définition des tâches et des grilles d’évaluation. Selon le dépôt, 38,24 % des tâches générées font intervenir plusieurs applications. Dans les parcours conservés, environ 68 % des actions passent par l’interface graphique et 32 % par le terminal.

## Spécialiser d’abord, réunir ensuite

Mage-VL-Cowork part d’une version intermédiaire de Mage-VL, plutôt que d’un modèle déjà spécialisé dans le pilotage d’une interface graphique ou la programmation. L’entraînement comporte cinq étapes : repérage visuel, tâches graphiques en plusieurs étapes, programmation et travail au terminal, ajustement supervisé combinant les deux modes, puis apprentissage par renforcement en ligne.

Cet ordre compte. Le modèle apprend d’abord à bien utiliser chacun des canaux, puis à choisir entre eux. À l’issue de l’étape supervisée hybride, il a obtenu 55,84 % sur OSWorld-Verified. L’apprentissage par renforcement en ligne a porté ce score à 66,04 %, tout en ramenant le nombre moyen d’appels au modèle de 21,57 à 18,77 et le nombre de tokens produits par tâche de 7 374 à 5 499.

La récompense n’a pas simplement poussé l’agent à essayer plus longtemps. Elle a raccourci les parcours qui aboutissaient. L’équipe a attribué les récompenses à partir de résultats vérifiables sur 1 988 tâches, avec 768 emplacements d’épisodes par mise à jour. L’étape de renforcement a nécessité davantage de calcul nominal que chacune des autres étapes, alors qu’elle ne représentait que 3,5 % du programme d’entraînement selon le décompte de l’équipe.

Les longues sessions sur un bureau posent un autre problème : les captures d’écran peuvent saturer le contexte avant la fin du travail. Mage-VL-Cowork conserve les trois captures les plus récentes et quatre réponses complètes de l’assistant. Il résume ensuite l’action de chaque tour plus ancien en une ligne. Le modèle garde ainsi les derniers changements visibles et une trace condensée des travaux antérieurs.

Le contexte actif est de 32 768 tokens, bien que l’architecture en accepte davantage. À chaque étape, le modèle produit un raisonnement, un bref résumé de l’action et un appel d’outil. Ce format permet d’effacer les raisonnements anciens tout en conservant la trace des actions.

## Là où s’arrête le test

OSWorld a été conçu pour évaluer les agents dans de vraies applications et sur des tâches du système d’exploitation, plutôt que sur des sites web isolés. Le jeu de tâches vérifiées rend la notation plus fiable, mais un test fixe toujours l’environnement, les logiciels installés et les critères de réussite. Il ne dit pas ce qui se passera si l’agent rencontre un gestionnaire de mots de passe personnel, un réseau imprévisible ou un document contenant des instructions malveillantes.

Les consignes de déploiement de Microsoft reflètent cette limite. Le modèle peut exécuter des commandes arbitraires dans le terminal et manipuler un bureau. L’équipe recommande donc des machines virtuelles ou des conteneurs jetables, sans identifiants personnels, avec des connexions sortantes restreintes et une confirmation humaine avant toute action irréversible. Le modèle est publié pour la recherche, pas pour un déploiement en production.

La catégorie 4B ne signifie pas non plus que l’ensemble du système est léger. Pour les cinq étapes, l’équipe chiffre à 7,79 zettaFLOPs le calcul nominal consacré à l’entraînement du modèle de langage. Pour le renforcement, elle a utilisé 32 GPU NVIDIA B200 et 1 120 emplacements CPU pour des environnements isolés. Pour servir la version BF16, les deux fichiers de poids exigent à eux seuls environ 9,48 Go, auxquels s’ajoutent la mémoire d’exécution et l’environnement de bureau.

L’apport le plus convaincant de cette publication concerne la méthode d’entraînement. Les concepteurs ont restreint les choix de l’enseignant, construit les tâches autour de compétences réutilisables et entraîné le modèle séparément sur chaque canal d’action. Ce n’est qu’ensuite qu’ils l’ont récompensé lorsqu’il achevait un travail vérifiable avec moins d’appels.

Revenons à notre analyste imaginaire. Le graphique a toujours sa place dans l’application graphique, où son apparence est visible. Pour fusionner les cellules, Python convient mieux : on peut modifier la structure du fichier et la vérifier avec précision. L’action décisive précède l’ouverture des deux outils : le modèle choisit une voie. Ce choix fait désormais partie d’une stratégie que chacun peut examiner.

## Références

- Microsoft Mage Team. (2026). *Mage: A Lightweight, Research-Friendly Multimodal Model Family*. https://github.com/microsoft/Mage
- Microsoft Mage Team. (2026). *Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use from Evolved Harnesses*. https://github.com/microsoft/Mage/blob/main/assets/mage_vl_cowork_tech_report.pdf
- Microsoft. (2026). *Mage-VL-Cowork model card*. https://huggingface.co/microsoft/Mage-VL-Cowork
- Xie, T., et al. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. https://arxiv.org/abs/2404.07972
- Yang, S., et al. (2026). *Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model*. https://arxiv.org/abs/2607.24904

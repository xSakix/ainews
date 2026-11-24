+++
title = "Les modèles égalent un prestataire sur une tâche d'Epoch, pas le reste"
slug = "les-modeles-egalent-un-prestataire-sur-une-tache-d-epoch"
description = "Le banc d'essai actualisé d'Epoch AI sur des tâches réelles montre que Fable 5.2 et Opus 5.5 égalent un prestataire pour l'analyse de centres de données, en une fraction du temps. Aucun modèle n'atteint le niveau d'un salarié sur aucune tâche, et Epoch indique envisager de réorienter le temps des prestataires vers la relecture des productions de l'IA."
tags = ["business", "research", "agents"]
date = 2026-11-18T03:14:41+01:00
draft = false
+++

La tâche arrive dans un espace de travail muni d'un guide, d'une boîte à outils et d'un seul nom : EcoDataCenter 1. Le modèle doit ajouter ce campus à la base de données des centres de données d'IA d'Epoch AI. Il lit des articles de presse et des documents réglementaires, commande des images satellites, puis les annote : contours bleu sarcelle pour les bâtiments, bleu pour les unités de refroidissement, violet pour les générateurs de secours. Un prestataire consacre généralement environ 16 heures à chaque site.

Dans le rapport d'Epoch du 17 novembre, deux des modèles ayant effectué ce travail ont produit des résultats que l'analyste des centres de données de l'organisation a jugés comparables à ceux d'un prestataire. Un troisième n'a couvert qu'une partie de ce que montraient ses sources.

## Ce qu'Epoch a testé

Epoch AI est un organisme de recherche qui suit la trajectoire de l'IA. Son banc d'essai (benchmark) Epoch Automation Reports reprend des tâches issues du propre travail de l'organisation et les confie à des modèles avec le contexte que recevrait une nouvelle recrue. Le personnel d'Epoch note ensuite les productions à la main. Un score de 100 % correspond au niveau qu'Epoch attend de ses salariés. La première version, publiée le 8 octobre, avait testé six modèles sur 11 tâches réparties en cinq catégories : conception graphique, Data Insights (de courts articles sur les tendances de l'IA), Data Explorers, recherche sur les centres de données et conception d'expériences de recherche. Elle avait constaté que les meneurs, Claude Fable 5.1 et GPT-6 Astra, s'acquittaient de manière fiable des tâches bien cadrées, mais échouaient sur les volets ouverts du travail.

Le nouveau rapport, signé par la chercheuse d'Epoch Kelly Hong, évalue Claude Fable 5.2 et GPT-6.2 Astra, ainsi que quatre autres modèles, sur une batterie actualisée. Epoch a modifié plusieurs éléments à la fois. L'organisme a remplacé une tâche ouverte de conception de benchmark, jugée dotée d'un budget trop faible au regard des nombreuses pistes plausibles, par une ancienne épreuve de recrutement autrefois soumise aux candidats. Il a ajouté des ressources aux prompts (instructions), dont une version condensée de son canal Slack interne consacré aux centres de données. Et il a fait passer la notation à une échelle de 1 à 4 par critère, plus proche de l'évaluation des articles de conférence.

Le résultat principal fait apparaître un clivage. Fable 5.2 et GPT-6.2 Astra se partagent quasiment un record sur l'Epoch Capabilities Index. Sur les tâches de travail réel, GPT-6.2 Astra obtient une moyenne de 65 %, soit 17 points derrière Fable 5.2. Aucun modèle n'a atteint le niveau d'un salarié sur aucune tâche.

## Là où les modèles atteignent le niveau d'un prestataire

L'exception concerne la tâche sur les centres de données. Fable 5.2 a obtenu 97,5 % et Opus 5.5 a obtenu 87,5 %, contre 65 % pour GPT-6.2 Astra. Un score parfait signifie qu'Epoch pourrait publier le résultat tel quel. Epoch définit le niveau prestataire comme un travail que son analyste juge comparable à celui remis par des prestataires, lequel nécessite généralement lui aussi quelques révisions avant publication.

Les défauts restants relevaient de ce qu'un relecteur corrige. Les annotations d'images de Fable 5.2 étaient imparfaites et son texte trop long. Opus 5.5 exigeait des corrections dans la classification des équipements et des retouches plus importantes sur ses annotations. Sur le cœur de la recherche, indique Epoch, tous deux atteignaient son seuil de qualité, avec des sources crédibles et des jugements bien calibrés.

Les chiffres de coût constituent le volet qui pèse directement sur l'emploi. Opus 5.5 a terminé en un peu moins de 3 heures, pour un coût inférieur à celui d'un prestataire. Fable 5.2 a pris environ 6,5 heures et coûté plus cher qu'un prestataire, en échange d'un meilleur résultat. Epoch écrit désormais « envisager de réorienter le temps des prestataires vers la relecture des productions de l'IA et d'autres volets de notre analyse des centres de données d'IA ». Le rapport ne dit pas qu'un prestataire a perdu son travail, et la tâche porte sur une seule fiche de base de données accompagnée d'un guide détaillé, non sur un poste complet.

La même tâche illustre comment le troisième modèle a échoué. Les sources de GPT-6.2 Astra mentionnaient plusieurs bâtiments dédiés à l'IA sur le campus, mais il n'en a traité qu'un seul, invoquant l'absence de preuve explicite. Il a ensuite omis ses estimations de puissance de calcul et de puces parce qu'il exigeait une source distincte pour chaque chiffre qui les alimentait. Selon Epoch, le guide aurait dû conduire le modèle à produire ces estimations. Gemini 4 Argon a péché par l'excès inverse : il a supposé que chaque bâtiment utilisait des puces Nvidia B200 alors qu'un seul bâtiment les mentionnait. Epoch qualifie ces erreurs de fautes qu'elle attend des prestataires qu'ils évitent.

## Là où ils échouent encore

En dehors de la tâche sur les centres de données, le rapport retrouve le schéma d'octobre. Les modèles peinent à concevoir des expériences, à itérer et à juger quel résultat compte vraiment.

Sur une tâche adaptée d'une ancienne épreuve de recrutement, les modèles devaient mesurer comment l'IA gère des situations éloignées de ses données d'entraînement, à l'aide de variantes d'échecs. Tous les modèles ont eu recours à des variantes déjà existantes. Epoch indique que Gemini 4 Argon a même mené une expérience montrant que les modèles connaissaient les variantes qu'il avait choisies, avant de poursuivre malgré tout. La variante inventée par GPT-6.2 Astra se contentait d'échanger le nom des pièces. Opus 5.5 et Fable 5.1, de Claude, ont présenté comme nouvelle une pièce d'échecs féeriques bien connue, le chameau, et le « Kingsgate » de Fable 5.2 se joue exactement comme une variante existante nommée « Midline Invasion ».

Sur une tâche consistant à dissimuler des messages dans des images SVG, Fable 5.2 s'est arrêté à son premier prompt d'encodage, qui produisait des images affichant presque toujours le message au grand jour. Les chercheurs humains qui ont itéré sur le prompt ont obtenu des encodages véritablement cachés, comme des étoiles dont la hauteur représente des lettres. Dans une tâche ouverte de Data Insight, GPT-6.2 Astra a retenu un sujet jugé trop étroit par Epoch pour son public : l'efficacité de la tokenisation en langue chinoise dans deux modèles précis. Epoch indique n'avoir constaté aucune amélioration significative par rapport à GPT-6 Astra, qui avait choisi un fait déjà bien connu, à savoir que des modèles ouverts populaires recourent à des architectures de mélange d'experts (mixture-of-experts).

La présentation a également fait défaut. Le rapport d'échecs de GPT-6.2 Astra s'ouvrait sur une conclusion mise en gras que ses propres résultats ultérieurs contredisaient. Selon Epoch, un défaut de cette nature empêcherait toute publication quelle que soit la valeur de la recherche.

## Quand les modèles se notent eux-mêmes

Epoch a ajouté un test d'auto-évaluation. Lorsqu'elle disposait d'une production humaine conforme à ses exigences, elle présentait au modèle les deux versions, sans étiquette, accompagnées de la grille de notation. Chaque modèle a préféré sa propre production, à la seule exception de Gemini 4 Argon, qui a choisi une fois celle de l'humain. Epoch indique que les justifications exagéraient de petits défauts dans le travail humain et récompensaient une rigueur de façade, comme le nombre d'expériences menées. L'unique exception d'Argon a rejoint le raisonnement qu'Epoch elle-même appliquerait : le travail humain menait une expérience propre visant la question centrale, tandis que ses propres expériences paraissaient « superficiellement plus formelles ». Epoch estime que si les modèles parvenaient à ce jugement de manière fiable, ils pourraient atteindre ses exigences, mais que ce cas restait loin de la norme.

## Ce que disent vraiment les chiffres

Epoch énumère ses propres limites. Chaque modèle n'a exécuté chaque tâche qu'une seule fois, la notation est manuelle et en partie subjective, et la modification du protocole rend les scores seulement grossièrement comparables à ceux d'octobre. Certains modèles antérieurs ont été réévalués et d'autres non. L'organisation invite les lecteurs à se fier aux constats qualitatifs plutôt qu'aux scores exacts, et souligne que ces résultats ne mesurent pas ce que l'IA sait faire dans l'ensemble du monde du travail. Les tâches sont propres à Epoch, notées par le personnel d'Epoch, et deux des trois modèles de tête appartiennent à Anthropic. Une note de bas de page précise que GPT-6.2 Astra a été évalué et discuté strictement au sein de l'équipe interne d'Epoch.

Lus avec ces réserves, les résultats décrivent une bande étroite de travail qui a basculé. Une tâche dotée d'un long guide, de sources publiques et d'un livrable vérifiable atteint désormais un niveau qu'un analyste humain transmettrait à un relecteur. Les tâches qui supposent de choisir la bonne question, de remarquer qu'un résultat est trivial ou de dire au lecteur ce qui importe ne le sont pas. Même la production d'Opus 5.5, la moins coûteuse des deux réussites, est revenue avec des annotations exigeant des corrections substantielles, confiées à une personne devant son image satellite ouverte.

## Références

- Hong, K. (2026). *How good are Fable 5.2 and GPT-6.2 Astra at real work?* Epoch AI. https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work
- Epoch AI (2026). *Can AI automate Epoch?* https://epoch.ai/publications/can-ai-automate-epoch

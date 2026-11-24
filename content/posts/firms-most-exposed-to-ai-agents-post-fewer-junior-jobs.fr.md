+++
title = "Les sociétés exposées aux agents d'IA publient moins d'offres juniors"
slug = "societes-exposees-agents-ia-publient-moins-offres-juniors"
description = "Une nouvelle prépublication (preprint) d'économie relie deux billiards de tokens d'usage réel de l'IA à 34,8 millions d'offres d'emploi et constate que les sociétés cotées les plus exposées aux agents ont ensuite publié moins d'offres, principalement pour des postes non seniors. Elle mesure les offres publiées, non les licenciements, et déduit l'exposition des cours de Bourse."
tags = ["research", "agents", "business"]
date = 2026-11-24T03:11:30+01:00
draft = false
+++

Un lundi matin de l'automne 2025, une responsable du recrutement dans une entreprise régionale de services de santé ouvre son tableau de bord des demandes de postes. Elle accomplit ce geste chaque semaine depuis six ans. Trois postes d'analyste, qui rouvraient autrefois dès qu'un titulaire était promu, restent fermés. Les postes seniors, destinés à des personnes qui connaissent déjà le fonctionnement de l'entreprise, sont ouverts comme toujours. Personne ne lui a demandé de cesser d'embaucher des juniors. Les demandes de postes cessent simplement d'arriver.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

Savoir si cette tendance se vérifie à l'échelle des entreprises constitue l'objet d'un document de travail mis en ligne sur arXiv le 20 novembre 2026. Nicola Borri de l'université Luiss, Anton Cheremukhin de la Federal Reserve Bank of Dallas, Yukun Liu de l'université de Rochester et Aleh Tsyvinski de Yale et du National Bureau of Economic Research se demandent si les entreprises les plus exposées aux agents d'IA ont ensuite publié moins d'offres d'emploi. Leur réponse est oui, et le recul touche principalement les postes non seniors. Les auteurs précisent que leurs opinions ne représentent pas celles de la Réserve fédérale de Dallas ni du Système de la Réserve fédérale, et l'étude n'a pas fait l'objet d'une évaluation par les pairs.

## Compter les agents à travers les tokens

Les auteurs soulignent que les éléments précédents provenaient d'entreprises isolées : Perplexity, Codex d'OpenAI, Claude Code d'Anthropic et le propre rapport d'Anthropic sur l'emploi en interne. Leurs données couvrent un champ plus large. OpenRouter, un service qui achemine des requêtes vers des centaines de modèles, leur a fourni des relevés anonymisés portant sur environ deux billiards de tokens d'usage payant répartis sur plus de 400 modèles. Cela représente environ 2 % de la consommation mondiale de tokens.

Ils définissent un token agentique comme un token appartenant à une réponse se terminant par un appel à un outil externe, tel qu'une requête dans une base de données, une exécution de code ou une écriture de fichier. Selon cette définition, 1,1 billiard de ces tokens sont agentiques. De juin à septembre 2025, la part agentique du trafic d'OpenRouter est restée comprise entre 8,2 et 8,7 %. Anthropic a lancé Claude Code 2.0 le 29 septembre 2025. Cette part a ensuite progressé chaque mois, atteignant 21,5 % en décembre 2025 puis 76,8 % durant les 27 premiers jours de septembre 2026, période où les agents représentaient la majorité des tokens sur la plateforme.

## Une exposition déduite des cours de Bourse

Une entreprise ne publie pas son degré d'exposition à la vague des agents ; les auteurs le déduisent donc. Pour chaque société américaine cotée, ils mesurent la manière dont le rendement de son action évolue avec la croissance hebdomadaire des tokens agentiques, une grandeur qu'ils nomment le bêta agentique. Un bêta élevé désigne une entreprise dont la valeur boursière monte et baisse au rythme de l'usage des agents. Ils recoupent cette mesure avec ce que les entreprises déclarent ensuite : un bêta supérieur d'un écart-type s'accompagne d'une probabilité accrue de 1,39 point de pourcentage de mentionner les agents d'IA dans un document déposé auprès de la SEC au cours des six mois suivants, et de 1,46 point lors d'une conférence de résultats.

Le volet emploi provient de Lightcast, qui recueille les offres sur les pages carrières des entreprises et les sites d'emploi. Les auteurs ont apparié 34,8 millions d'offres, soit environ 18 % du total de Lightcast, à 1 784 sociétés mères cotées.

## Ce que montrent les offres d'emploi

Une entreprise dont le bêta agentique est supérieur d'un écart-type a enregistré une croissance de ses offres d'emploi inférieure de 2,11 % sur les six mois suivants et de 3,20 % sur neuf mois. Un sceptique pourrait objecter que les entreprises dont les perspectives s'assombrissaient déjà étaient précisément celles que le marché associait aux agents. Pour y répondre, les auteurs mènent une étude d'événement autour du lancement de Claude Code 2.0. Ils figent le bêta de chaque société à sa valeur de septembre 2025 et comparent la croissance après cette sortie. Ils ne relèvent aucune relation entre exposition et croissance des offres avant le lancement. Après celui-ci, les sociétés plus exposées ont accru leurs offres moins vite chaque mois à partir d'octobre 2025, avec un chiffre à six mois inférieur de 4,73 % par écart-type. Ce résultat repose sur une hypothèse explicitée par les auteurs : sans ce lancement, les entreprises fortement et faiblement exposées auraient connu une croissance semblable une fois pris en compte le secteur et les caractéristiques propres à chaque société.

Le repli se concentre au bas de l'échelle hiérarchique. Pour les postes seniors et pour les emplois demandant six ans d'expérience ou plus, les estimations ne sont pas statistiquement significatives. Pour les postes non seniors et pour ceux exigeant moins de six ans d'expérience, elles sont négatives et significatives au seuil de 5 %, tout comme les écarts entre les groupes. Les offres attendant des salariés qu'ils utilisent des outils d'IA ont peu réagi, tandis que celles sans cette exigence ont reculé. Les salaires affichés n'ont pas baissé. L'usage général de l'IA raconte une autre histoire : une fois l'exposition agentique contrôlée, l'exposition d'une entreprise à l'usage total de tokens d'IA n'entretient plus de lien significatif avec les offres ultérieures. L'effet apparaît également lorsque l'exposition est mesurée via des modèles de pointe à poids fermés, et beaucoup moins avec des modèles à poids ouverts.

Le signe négatif ressort dans chacun des cinq groupes sectoriels de Fama-French, le groupe Santé affichant l'estimation la plus marquée. Les scores d'exposition par profession, dont ceux d'Eloundou et de ses collègues, de Webb et de l'Economic Index d'Anthropic, n'ont eu qu'un pouvoir limité pour prédire quelles entreprises publieraient moins d'offres une fois les caractéristiques des sociétés incluses.

## Les limites de l'étude

L'article mesure les offres publiées, non l'emploi effectif. Une entreprise peut publier moins d'annonces sans licencier qui que ce soit ; elle peut aussi pourvoir des postes sans publier d'offre. L'échantillon porte sur des sociétés américaines cotées, et l'exposition repose sur la covariation des rendements boursiers ainsi que sur une tranche de 2 % des tokens mondiaux. L'étude montre que l'exposition prédit une croissance moindre des offres ; elle ne dit pas ce qu'une entreprise donnée a décidé.

Son orientation concorde avec d'autres travaux de cette année fondés sur des données différentes. Les économistes d'Anthropic ont indiqué en octobre que les embauches techniques juniors au sein de leur propre entreprise étaient passées de 27 % à 9 % des recrutements, tandis que la part de salariés juniors dans ses départements techniques reculait de 21 % à 14 % depuis le début de 2025. Des chercheurs de Stanford s'appuyant sur les données de paie d'ADP jusqu'en juin 2026 n'ont trouvé aucun signe de suppression généralisée d'emplois, mais l'emploi des travailleurs âgés de 22 à 25 ans dans les professions exposées à l'IA se situait 19 % en dessous du niveau qu'il aurait atteint s'il avait suivi le rythme de pairs moins exposés, sans écart comparable chez les salariés expérimentés. Ces trois sources reposent sur une seule entreprise, un échantillon de fiches de paie et un ensemble d'offres d'emploi, et le motif qu'elles partagent est un premier barreau de l'échelle plus mince.

De retour devant son tableau de bord un an plus tard, la responsable du recrutement a pourvu deux des postes seniors. Les demandes de postes d'analyste sont toujours fermées, et personne ne lui a demandé de les rouvrir.

## Références

- Borri, N., Cheremukhin, A., Liu, Y., & Tsyvinski, A. (2026). *The Rise of Agents and the Labor Market*. arXiv:2611.27210. https://arxiv.org/abs/2611.27210
- Brynjolfsson, E., Chandar, B., & Chen, R. (2026, revised 12 August). *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*. Stanford Digital Economy Lab. https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/
- Wilmers, N., Catipon, R., Massenkoff, M., & McCrory, P. (2026). *How employment is changing at Anthropic*. The Anthropic Institute. https://www.anthropic.com/research/employment-at-anthropic

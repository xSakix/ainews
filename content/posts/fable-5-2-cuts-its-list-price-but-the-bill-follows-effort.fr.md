+++
title = "Fable 5.2 baisse son tarif, mais le raisonnement fait la facture"
slug = "fable-5-2-tarif-raisonnement-facture"
description = "Anthropic a réduit d'un cinquième le prix de Claude Fable 5.2, mais un indice indépendant a mesuré au niveau de raisonnement maximal le coût par tâche le plus élevé parmi 73 modèles. L'écart tient au nombre de tokens consommés, et les propres graphiques d'Anthropic montrent que le réglage du niveau de raisonnement le détermine."
tags = ["models", "business"]
date = 2026-11-10T03:25:07+01:00
draft = false
+++

Ce lundi est inventé, assemblé à partir de documents de lancement et non du journal de quelqu'un. Une responsable de plateforme dans une entreprise de logiciels de taille moyenne lit qu'Anthropic a réduit d'un cinquième le prix de son meilleur modèle. Elle fait ce à quoi l'annonce invite. Elle change le nom du modèle dans la configuration d'agents de son équipe, règle le paramètre de niveau de raisonnement à sa valeur maximale et laisse quarante audits de dépôts tourner pendant la nuit. Au matin, le lot est terminé, et elle ne veut ouvrir qu'une chose : la facture. Celle-ci ne ressemble pas au titre qu'elle a lu.

Le titre était exact. Le 9 novembre, Anthropic a lancé Claude Fable 5.2 et son jumeau, Claude Mythos 5.2, à 8 dollars par million de tokens d'entrée et 40 dollars par million de tokens de sortie, contre 10 et 50 dollars pour les versions 5.1. Le chiffre indépendant arrivé le même jour est lui aussi exact. Artificial Analysis, qui publie un indice d'intelligence comparant plusieurs fournisseurs, a exécuté Fable 5.2 à son réglage maximal et l'a classé premier sur 74 modèles en intelligence, avec un score de 65, et 73e sur 73 pour le coût, à 26,54 dollars par tâche de l'indice. Les deux chiffres décrivent un même modèle. Ce qui les sépare est le nombre de tokens qu'il consomme.

## Ce que dit la grille tarifaire

La documentation d'Anthropic indique clairement les nouveaux tarifs. Les lectures du cache coûtent 0,20 dollar par million de tokens, le traitement par lots coûte la moitié du tarif de base, et un mode rapide optionnel générant jusqu'à 2,5 fois plus vite coûte 16 dollars en entrée et 80 dollars en sortie. L'entreprise affirme aussi que le modèle produit sa sortie jusqu'à 30 % plus vite que Fable 5.1. TechCrunch relève que Fable est désormais moins cher que son principal concurrent, et Fortune situe Fable 5.2 20 % sous GPT-6 Astra d'OpenAI, affiché à 10 et 50 dollars, avec l'entrée en cache à 20 cents contre un dollar pour Astra.

Mythos 5.2 porte le même tarif. Anthropic présente les deux comme un même modèle sous-jacent ; Fable est livré avec des garde-fous en cybersécurité et en biologie et est accessible à tous les clients, tandis que Mythos est réservé aux organisations acceptées dans les Cyber Verification et Life Sciences Verification Programs de l'entreprise. Le prix est commun. L'accès ne l'est pas.

## Ce que l'indice a mesuré

Artificial Analysis calcule le coût par tâche à partir des tarifs d'entrée, de lecture et d'écriture du cache, de raisonnement et de tokens de réponse, divisés par le nombre de tâches et pondérés sur les neuf évaluations de son indice. Sur cette base, Fable 5.2 au niveau de raisonnement maximal a généré 275 millions de tokens de sortie, alors que la médiane des modèles comparables est de 72,8 millions. Il a pris 46,4 minutes par tâche, contre une médiane de 12,7, et 216 secondes avant le premier token de réponse. Le résumé du site qualifie le modèle de « particulièrement coûteux » et de « très prolixe ».

Le calcul est bref. Le prix affiché en sortie est de 40 dollars contre une médiane de 10 dollars, soit quatre fois plus, et le nombre de tokens représente environ 3,8 fois la médiane. Une facture est un prix multiplié par un volume, et Fable 5.2 se situe haut sur les deux à ce réglage. Les limites doivent être précisées : ce sont les tâches d'Artificial Analysis, pas celles du lecteur, et le chiffre correspond à un seul niveau de raisonnement.

## Le réglage qu'Anthropic met en avant

Anthropic ne conteste pas l'importance du niveau de raisonnement. Sa page de lancement indique que le réglage par défaut des applications Claude et de Claude Code est Medium, et qu'à ce niveau Fable 5.2 accomplit les tâches difficiles avec moins de tokens que 5.1. Lors de premiers tests sur FrontierCode 2.0, un benchmark évaluant si les modifications de code d'un modèle seraient fusionnées par des mainteneurs open source, Fable 5.2 au niveau High obtenait 45,3 % contre 45,5 % pour Opus 5.5 au niveau Max, pour environ la moitié du coût par tâche. Sur WANDR, le benchmark de collecte de données de Perplexity, le niveau Medium égale le meilleur score d'Opus 5.5 pour environ 40 % du coût. Sur Humanity's Last Exam, le niveau Low le fait pour moins d'un dixième. Au niveau Xhigh, le modèle atteint 49,1 % sur FrontierCode, le score le plus élevé parmi les modèles publiés testés par Anthropic.

Tous ces graphiques sont ceux du fournisseur et proviennent de premiers tests. Ils montrent que le même modèle occupe des positions très différentes sur une courbe de coûts selon un seul paramètre, lecture que soutient également le chiffre indépendant. La documentation est directe sur la place de Fable : pour la plupart des charges de travail, commencer avec le dernier modèle Opus et passer à Fable lorsque les évaluations d'Opus à un niveau de raisonnement supérieur ne permettent toujours pas de « répondre aux exigences ».

## Comment la facture en est arrivée là

Anthropic a déjà présenté les prix de cette manière. Son annonce de Claude Opus 5.5 du 22 septembre indiquait que le modèle atteint le niveau de Fable 5.1 sur la plupart des travaux et coûte 40 % de moins qu'Opus 5 sur des charges courantes. Le tarif par token était inférieur de 20 %, à 4 et 20 dollars par million, et l'entreprise attribuait le reste de l'économie à l'utilisation de moins de tokens par tâche. Selon les propres explications d'Anthropic, une facture est un tarif multiplié par une quantité.

Gergely Orosz, auteur de The Pragmatic Engineer, a donné de la substance à cet effet dans une édition du 20 octobre. Il a interrogé des personnes de 27 lieux de travail sur les dépenses d'IA par développeur, dans un échantillon autosélectionné, principalement anonyme. Il rapporte que les dépenses ont culminé en juin et juillet et ont approximativement diminué de moitié pour les entreprises utilisant des offres API, la plupart attribuant ce recul à un mélange d'Opus 5.5 et de modèles ouverts. Un ingénieur a dépensé 2 200 dollars en septembre sur Opus 5 et s'attend à dépenser moitié moins avec Opus 5.5. Orosz a aussi appris que les abonnements subventionnés de plusieurs entreprises arrivaient à leur terme, ce qui pourrait multiplier leurs factures par cinq à dix.

Fable 5.2 arrive dans ce calcul. Un acheteur passé à Opus 5.5 pour diviser sa facture par deux dispose désormais d'une gamme supérieure dont le prix par token a baissé et dont le coût par tâche dépend d'un réglage auquel la plupart des gens ne touchent pas.

## Offres de lancement et financement de l'essai

Pendant la première semaine, les abonnés ne ressentent pas le prix. Le centre d'aide d'Anthropic indique que les abonnements Pro et les licences Team standard incluent tous les modèles Fable dans leurs limites hebdomadaires du 9 au 16 novembre, à hauteur de 50 % de ces limites, plus une réinitialisation de limite. Les offres Max et Ultra bénéficient d'une à trois réinitialisations selon l'ancienneté payante du compte, et celles qui ne sont pas utilisées expirent le 8 mars 2027. Les offres sont rédigées pour les abonnements, et la page ne dit rien des comptes API.

## Retour à la facture

Dans le lundi inventé, la responsable regarde le lot d'audits et ne trouve rien à redire aux résultats. Ce qui lui manque est une comparaison. Le prochain test qu'elle prépare est banal : les mêmes quarante dépôts au niveau High, puis au niveau Medium, avec le coût et le nombre de constats acceptés à côté de chacun. Déterminer si les exécutions moins chères trouvent assez de problèmes est une question qu'aucune page de lancement ne peut trancher pour son équipe, et la documentation qu'elle a lue le dit aussi. Le modèle est tarifé au million de tokens. Son examen sera chiffré au dépôt.

## Références

- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Anthropic (2026). *Introducing Claude Opus 5.5*. https://www.anthropic.com/news/claude-opus-5-5
- Anthropic (2026). *Claude Fable 5.2 launch offers*. Claude Help Center. https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
- Anthropic (2026). *What's new in Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- Brandom, R. (2026). *Anthropic releases new Mythos and Fable models amid RSI concerns*. TechCrunch. https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/
- Forlini, E. (2026). *Anthropic debuts Claude Fable, Mythos 5.2 models, priced 20% below OpenAI's GPT-6 Astra*. Fortune. https://fortune.com/2026/11/09/anthropic-debuts-updated-claude-fable-and-mythos-models-undercutting-price-of-openais-gpt-6-astra-by-up-to-80/
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers

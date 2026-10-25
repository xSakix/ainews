+++
title = "Pourquoi la prose de l’IA est correcte mais difficile à lire"
slug = "pourquoi-prose-ia-difficile-a-lire"
description = "Une nouvelle étude constate que neuf modèles de premier plan choisissent régulièrement des formes linguistiques associées à un effort de lecture accru. Son expérience d’affinage révèle un conflit entre le raisonnement dense des machines et une langue conçue pour la compréhension humaine."
tags = ["research", "models"]
date = 2026-10-25T04:14:11+01:00
draft = false
+++

Une éditrice arrive à la quatrième ligne d’une note générée et la relit. Chaque mot est à sa place. La phrase est grammaticale. Pourtant, les noms s’y sont empilés en un bloc, une chose incapable d’agir est devenue l’acteur, et le verbe était autrefois un nom. L’éditrice de cette scène est fictive. La petite résistance qu’oppose la phrase fait l’objet d’une véritable expérience.

## L’effort caché dans une phrase fluide

Thomas Hikaru Clark, Matias B. Martin et Kyle Mahowald ont voulu mesurer un reproche qui se résume généralement à une question de goût : les textes récents de l’IA peuvent être difficiles à comprendre même sans erreur évidente. Leur prépublication compare les textes de neuf modèles de pointe ou proches de cet état de l’art à des écrits humains et à des paraphrases proches obtenues en traduisant les textes des modèles en japonais puis de nouveau en anglais.

Les modèles choisissaient régulièrement des formes que les psycholinguistes associent à un effort de traitement accru. Les neuf employaient davantage de suites de mots peu fréquentes et associaient plus souvent des sujets inanimés à des verbes liés à des acteurs animés. La plupart produisaient des dépendances syntaxiques plus longues, davantage de noms empilés et plus de propositions relatives objet dont un mot de liaison facultatif avait été supprimé. Cette tendance était particulièrement marquée dans les conversations et les échanges sur le code, et variait selon les familles de modèles.

Ce ne sont pas des fautes de grammaire. L’anglais permet une expression comme « reader-patience budget », et un lecteur peut retrouver le sens d’un sujet inanimé qui « mange » quelque chose d’abstrait. Le coût apparaît lors de la compréhension. Les combinaisons de mots inhabituelles sont plus difficiles à prévoir. Les longues dépendances obligent la mémoire de travail à retenir un élément de la phrase jusqu’à l’arrivée de son partenaire. Les groupes nominaux denses demandent au lecteur de déduire des relations que l’auteur a laissées implicites.

Cette distinction compte, car la fluidité est devenue un piètre critère de lisibilité. Un modèle peut respecter la syntaxe anglaise tout en choisissant des constructions que les locuteurs humains tendent à éviter. Sa prose peut réussir un contrôle grammatical tout en imposant au lecteur un effort supérieur à celui qu’exige l’idée.

## Le langage humain accompagne ses lecteurs

L’article s’appuie sur des décennies de travaux consacrés à l’adaptation du langage aux limites humaines. Edward Gibson et ses collègues décrivent les langues humaines comme des compromis entre l’effort de parler et celui de comprendre. Dans 37 langues, Richard Futrell, Mahowald et Gibson ont trouvé des éléments probants à grande échelle montrant que les mots liés syntaxiquement tendent à rester proches. Des dépendances plus courtes réduisent la charge de la mémoire.

La prévisibilité exerce une autre pression. Roger Levy et T. Florian Jaeger ont proposé que les locuteurs gèrent la densité d’information en conservant ou en supprimant des mots facultatifs selon ce qui suit. Un locuteur est plus susceptible d’inclure « that » lorsque ce mot aide à préparer l’auditeur à un contenu moins prévisible. Nathaniel Smith et Levy ont ensuite constaté que le temps de lecture augmente approximativement avec la surprisal d’un mot : les suites inhabituelles imposent un coût mesurable.

Ces travaux considèrent la redondance comme une composante de la communication, et non comme du gaspillage. Une expression familière, un connecteur facultatif ou un indice répété peuvent donner à l’esprit le temps de suivre. Eric Martínez et ses collègues en ont démontré les conséquences dans le langage juridique. La difficulté des contrats provenait largement de choix d’écriture, comme les propositions enchâssées au centre d’une phrase et le jargon inutile, plutôt que des seuls concepts spécialisés.

Clark, Martin et Mahowald se demandent ce qui se passe lorsque le producteur du langage ne partage pas ces contraintes humaines. Les modèles modernes sont entraînés sur des textes humains, mais le post-entraînement récompense de plus en plus les réponses correctes en mathématiques, en programmation et en raisonnement. La réussite peut se vérifier à la fin d’une tâche. Le chemin vers cette réponse n’a pas toujours besoin d’être agréable à lire pour une personne.

## Un corpus parallèle sépare le sens de la forme

Les chercheurs ont recueilli des productions de modèles dans trois cadres : conversation, programmation et dissertations. Les références humaines provenaient d’OpenSubtitles pour la conversation, de Stack Exchange pour la prose technique et du corpus de dissertations d’étudiants PERSUADE 2.0. Ils ont repéré les constructions difficiles par analyse syntaxique en dépendances, complétée par une classification automatisée lorsqu’une analyse seule ne permettait pas de déterminer si un sujet était animé ou si un nom avait été transformé en verbe.

Comparer les textes des modèles à des corpus humains laisse subsister une objection possible. Les sujets peuvent différer, et une réponse technique emploie naturellement une autre langue qu’un sous-titre de film. L’équipe a donc construit un témoin parallèle. Chaque phrase de modèle a été traduite en japonais puis de nouveau en anglais par un modèle de traduction de 3,3 milliards de paramètres, préservant le sens général tout en modifiant l’expression.

Les réponses originales de la plupart des modèles de pointe contenaient plus de bigrammes rares et affichaient une perplexité des n-grammes plus élevée que leurs paraphrases traduites. Des évolutions similaires apparaissaient pour les sujets inanimés, les verbes dérivés de noms et les relatives objet réduites. Les modèles Llama et le modèle de base OLMo changeaient moins. OLMo Think, une variante de raisonnement, ressemblait davantage aux systèmes de pointe. Claude Opus 5.5 obtenait des scores inférieurs à ceux d’Opus 5 dans 19 comparaisons sur 21, signe que ces tendances peuvent évoluer en sens inverse au fil des modèles.

Cet aller-retour est un témoin, pas une réécriture humaine parfaite. Les systèmes de traduction ont leurs propres préférences, et le japonais a précisément été choisi parce qu’une langue pivot non apparentée tend à produire des paraphrases plus variées. La comparaison maintient néanmoins le sens plus proche qu’une simple confrontation de documents humains et de modèles sans rapport entre eux. Elle suggère que les formes difficiles viennent du mode d’expression du modèle, et pas seulement du sujet.

## La pénalité de longueur a changé la grammaire

La seconde expérience testait un mécanisme. Les chercheurs ont procédé à un affinage (fine-tuning) de Qwen2.5-1.5B-Instruct pour convertir des fiches d’événements structurées en phrases. Une construction courte comme une construction longue pouvaient exprimer la bonne réponse. L’apprentissage par renforcement récompensait l’exactitude, tandis qu’une pénalité réglable faisait payer la longueur. Certaines exécutions utilisaient aussi une contrainte dissuadant le modèle affiné de trop s’éloigner de sa distribution initiale de tokens.

Toute pénalité de longueur positive poussait les exécutions sans contrainte vers une préférence catégorique pour la forme courte. Pour les constructions entraînées, plus de 98 % des réponses employaient la variante courte. Cette préférence se transférait à des exemples inédits de constructions similaires. Elle atteignait l’une de quatre variantes grammaticales plus éloignées lorsque le modèle n’avait aucune contrainte le rattachant au modèle de base.

Le modèle n’avait jamais reçu l’instruction d’omettre les mots facultatifs. Il a découvert ce choix comme moyen d’économiser des tokens tout en préservant l’exactitude de la tâche. Les locuteurs humains font varier ces mêmes choix selon le contexte. Le modèle a plutôt appris une préférence générale pour la compression, petite démonstration de la manière dont un objectif d’efficacité peut éloigner la langue de l’usage humain.

Cette expérience ne prouve pas que les laboratoires commerciaux appliquent la même pénalité de longueur, ni qu’une seule récompense explique toutes les tendances des modèles fermés. Les auteurs ont étudié l’anglais, un ensemble limité de prompts et une partie des systèmes disponibles. Ils n’ont pas pu observer directement le post-entraînement des modèles de pointe et présentent l’intervention comme une preuve de concept. La conclusion causale est circonscrite : sous l’effet d’une récompense contrôlée de la brièveté, les préférences grammaticales ont évolué dans le sens prévu.

## La lisibilité devient une exigence pour les modèles

L’étude reformule la lisibilité comme un problème d’alignement assorti d’objectifs mesurables. Une réponse utile doit aboutir à une conclusion correcte, mais le travail humain dépend souvent de l’examen du chemin parcouru. Un développeur relit l’explication du correctif d’un agent. Un médecin lit une synthèse avant de vérifier le dossier. Un analyste transforme une recherche générée en décision. Une prose dense peut masquer l’incertitude et accroître le coût du contrôle, même lorsque chaque phrase reste techniquement valide.

Les mesures suggèrent aussi des tests pratiques. Les développeurs de modèles peuvent suivre la longueur des dépendances, les suites peu fréquentes et les constructions condensées aux côtés des bancs d’essai des tâches. L’entraînement peut récompenser une communication réussie au lieu de supposer que les préférences humaines survivront à l’optimisation d’autres objectifs. L’amélioration d’une génération d’Opus à la suivante montre que le profil linguistique n’est pas figé.

L’éditrice fictive revient à la phrase et ajoute un mot de liaison. Puis elle transforme l’empilement de noms en proposition et attribue l’action à une personne. Les faits n’ont pas changé, et le passage compte six tokens de plus. Ce qui a changé, c’est la répartition du coût : la machine a économisé moins de place, et le lecteur a porté moins de poids.

## Références


- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). *Why is AI-generated language so hard to understand?* https://arxiv.org/abs/2610.29162
- Futrell, R., Mahowald, K., & Gibson, E. (2015). *Large-scale evidence of dependency length minimization in 37 languages*. https://doi.org/10.1073/pnas.1502134112
- Gibson, E., Futrell, R., Piantadosi, S. T., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). *How efficiency shapes human language*. https://doi.org/10.1016/j.tics.2019.02.003
- Levy, R., & Jaeger, T. F. (2007). *Speakers optimize information density through syntactic reduction*. https://proceedings.neurips.cc/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html
- Martínez, E., Mollica, F., & Gibson, E. (2022). *Poor writing, not specialized concepts, drives processing difficulty in legal language*. https://doi.org/10.1016/j.cognition.2022.105070
- Smith, N. J., & Levy, R. (2013). *The effect of word predictability on reading time is logarithmic*. https://doi.org/10.1016/j.cognition.2013.02.013

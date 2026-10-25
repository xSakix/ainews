+++
title = "Pourquoi la prose de l’IA est correcte mais difficile à lire"
slug = "pourquoi-prose-ia-difficile-a-lire"
description = "Une nouvelle étude constate que neuf modèles de premier plan choisissent régulièrement des formes linguistiques qui demandent davantage d’effort de lecture. Une expérience d’affinage suggère un conflit entre le raisonnement condensé des modèles et une langue facile à comprendre pour les humains."
tags = ["research", "models"]
date = 2026-10-25T04:14:11+01:00
draft = false
+++

Une éditrice arrive à la quatrième ligne d’une note générée et la lit deux fois. Chaque mot convient et la phrase est grammaticale. Pourtant, plusieurs noms se suivent sans mots expliquant leurs relations. Un sujet inanimé est associé à un verbe qui décrit normalement une action humaine, et un nom est utilisé comme verbe. L’éditrice de cette scène est fictive. La difficulté qu’elle rencontre fait l’objet d’une véritable expérience.

## Pourquoi une phrase fluide peut être difficile à lire

Thomas Hikaru Clark, Matias B. Martin et Kyle Mahowald ont voulu mesurer un problème que les lecteurs décrivent souvent comme une question de goût : les textes récents de l’IA peuvent être difficiles à comprendre même sans erreur évidente. Leur prépublication compare les textes de neuf modèles de pointe ou proches de ce niveau à des écrits humains. Elle les compare aussi à des paraphrases proches obtenues en les traduisant en japonais puis de nouveau en anglais.

Les modèles choisissaient régulièrement des formes que les psycholinguistes associent à un effort de lecture accru. Les neuf employaient davantage de suites de mots inhabituelles et de sujets inanimés associés à des verbes décrivant normalement les actions d’êtres vivants. La plupart éloignaient aussi davantage les mots liés grammaticalement, utilisaient plus de suites de noms pour en modifier d’autres et omettaient plus souvent les mots de liaison facultatifs des propositions relatives objet. Cette tendance était la plus forte dans les conversations et les échanges sur le code, et variait selon les familles de modèles.

Ce ne sont pas des erreurs grammaticales. L’anglais autorise une expression comme « reader-patience budget », et un lecteur peut comprendre ce que signifie un sujet inanimé qui « mange » quelque chose d’abstrait. Mais comprendre ces constructions demande un effort. Les combinaisons de mots inhabituelles sont plus difficiles à prévoir. Quand des mots liés sont éloignés, les lecteurs doivent retenir une partie de la phrase en attendant l’autre. Quand plusieurs noms se suivent, ils doivent déduire des relations que l’auteur a laissées implicites.

Cette distinction compte, car la fluidité seule renseigne peu sur la lisibilité. Un modèle peut respecter les règles de la syntaxe anglaise tout en choisissant des constructions que les locuteurs humains tendent à éviter. Sa prose peut être grammaticalement correcte et demander malgré tout un effort de lecture supérieur à celui qu’exige l’idée elle-même.

## Le langage humain reflète les besoins des lecteurs

L’article s’appuie sur des décennies de recherches sur l’adaptation du langage aux limites humaines. Edward Gibson et ses collègues décrivent les langues humaines comme des compromis entre l’effort de parler et celui de comprendre. Richard Futrell, Mahowald et Gibson ont étudié 37 langues et trouvé de nombreux éléments montrant que les mots liés grammaticalement tendent à rester proches. Cette proximité réduit la charge de la mémoire.

La prévisibilité influence aussi la parole et la lecture. Roger Levy et T. Florian Jaeger ont proposé que les locuteurs gèrent la densité d’information en conservant ou en supprimant des mots facultatifs selon ce qui suit. Un locuteur est plus susceptible d’inclure « that » lorsque cela prépare l’auditeur à un contenu moins prévisible. Nathaniel Smith et Levy ont ensuite constaté que le temps de lecture augmente approximativement avec la surprisal d’un mot, une mesure de son caractère inattendu : les mots moins prévisibles prennent un temps de lecture mesurablement plus long.

Dans cette explication, la redondance remplit une fonction dans la communication. Une expression familière, un mot de liaison facultatif ou un indice répété peuvent donner aux lecteurs le temps de comprendre ce qu’ils lisent. Eric Martínez et ses collègues ont démontré cet effet dans le langage juridique. Ils ont constaté que la difficulté des contrats venait largement de choix d’écriture, dont des propositions insérées dans d’autres et du jargon inutile. Les seuls concepts spécialisés n’expliquaient pas cette difficulté.

Clark, Martin et Mahowald se demandent ce qui se passe lorsqu’un système produisant du langage n’a pas ces limites humaines. Les modèles modernes sont entraînés sur des textes humains, mais l’entraînement qui suit cette première étape récompense de plus en plus les bonnes réponses en mathématiques, en programmation et en raisonnement. On peut vérifier l’exactitude d’une réponse à la fin d’une tâche même si l’explication qui y conduit est difficile à lire pour une personne.

## Comparer des sens proches exprimés différemment

Les chercheurs ont recueilli des productions de modèles dans trois cadres : conversation, programmation et dissertations. Ils ont utilisé des écrits humains d’OpenSubtitles comme référence pour la conversation, de Stack Exchange pour la prose technique et du corpus PERSUADE 2.0 pour les dissertations d’étudiants. Ils ont repéré les constructions difficiles en analysant les relations grammaticales entre les mots, méthode appelée analyse syntaxique en dépendances. Ils ont ajouté une classification automatisée lorsque cette analyse seule ne permettait pas de déterminer si un sujet était animé ou si un nom avait été transformé en verbe.

Une comparaison entre textes de modèles et écrits humains laisse une objection possible : les deux ensembles peuvent traiter de sujets différents. Une réponse technique emploie naturellement une autre langue qu’un sous-titre de film. Pour y remédier, l’équipe a créé une autre version de chaque phrase de modèle. Un modèle de traduction de 3,3 milliards de paramètres a traduit la phrase en japonais puis de nouveau en anglais. Le sens général était préservé, mais son expression changeait.

Les réponses originales de la plupart des modèles de pointe contenaient davantage de paires de mots rares, ou bigrammes, que leurs paraphrases traduites. Leur perplexité des n-grammes, mesure de l’imprévisibilité des suites de mots, était aussi plus élevée. Des différences similaires apparaissaient dans l’usage des sujets inanimés, des verbes dérivés de noms et des relatives objet dont les mots de liaison avaient été omis. Les modèles Llama et le modèle de base OLMo changeaient moins. OLMo Think, une variante de raisonnement, ressemblait davantage aux systèmes de pointe. Claude Opus 5.5 obtenait des scores inférieurs à ceux d’Opus 5 dans 19 comparaisons sur 21. Ce résultat montre que ces tendances peuvent aussi diminuer au fil des modèles.

Traduire dans une autre langue puis revenir à la langue d’origine constitue un témoin, pas un substitut parfait à une réécriture humaine. Les systèmes de traduction ont leurs propres préférences. Les chercheurs ont précisément choisi le japonais parce que le passage par une langue non apparentée tend à produire des paraphrases plus variées. Cette comparaison maintient néanmoins le sens plus constant qu’une comparaison de documents sans rapport écrits par des humains et des modèles. Elle suggère que les formes difficiles viennent en partie de la façon dont le modèle exprime une idée, plutôt que du seul sujet.

## Pénaliser la longueur a changé la grammaire du modèle

La seconde expérience testait un mécanisme possible. Les chercheurs ont procédé à un affinage (fine-tuning) de Qwen2.5-1.5B-Instruct pour transformer des fiches d’événements structurées en phrases. Une construction courte comme une construction longue pouvaient exprimer la bonne réponse. L’apprentissage par renforcement récompensait l’exactitude, tandis qu’une pénalité réglable décourageait les réponses longues. Certaines exécutions d’entraînement comportaient aussi une contrainte dissuadant le modèle de trop s’éloigner de sa distribution initiale de tokens.

Dans les exécutions sans cette contrainte, toute pénalité de longueur positive conduisait à une préférence catégorique pour la forme courte. Plus de 98 % des réponses utilisaient la variante courte pour les constructions sur lesquelles le modèle avait été entraîné. La préférence apparaissait aussi dans des exemples inédits de constructions similaires. Sans la contrainte le rattachant au modèle de base, le modèle étendait cette préférence à l’une de quatre variantes grammaticales plus éloignées.

Le modèle n’avait jamais reçu l’instruction d’omettre les mots facultatifs. Pendant l’entraînement, il a appris que cela économisait des tokens tout en préservant l’exactitude de la tâche. Les locuteurs humains font varier ces choix selon le contexte. Le modèle a plutôt appris une préférence générale pour une expression condensée. Cette petite expérience démontre comment un objectif récompensant l’efficacité peut produire une langue qui diffère de l’usage humain.

L’expérience ne prouve pas que les laboratoires commerciaux appliquent la même pénalité de longueur, ni qu’une seule récompense explique chaque tendance des modèles fermés. Les auteurs ont étudié l’anglais, un ensemble limité de prompts et une partie des systèmes disponibles. Ils n’ont pas pu observer directement comment les modèles de pointe étaient entraînés après leur entraînement initial, et décrivent leur intervention comme une preuve de concept. Leur affirmation causale est circonscrite : sous une récompense contrôlée de la brièveté, les préférences grammaticales ont évolué dans le sens prévu.

## La lisibilité devient une exigence pour les modèles

L’étude traite la lisibilité comme un problème d’alignement : les modèles doivent produire une langue répondant aux besoins humains, et les chercheurs peuvent en mesurer certains aspects. Une réponse utile doit parvenir à une conclusion correcte, mais les humains doivent souvent aussi examiner comment elle a été obtenue. Un développeur relit l’explication d’un correctif par un agent. Un médecin lit une synthèse avant de vérifier le dossier. Un analyste utilise une recherche générée pour prendre une décision. Une prose dense peut masquer l’incertitude et compliquer le contrôle, même lorsque chaque phrase reste techniquement valide.

Les mesures suggèrent des tests pratiques. À côté des bancs d’essai de performance sur les tâches, les développeurs peuvent suivre la distance entre mots liés, les suites de mots inhabituelles et les constructions condensées. Ils peuvent récompenser une communication réussie pendant l’entraînement, plutôt que supposer que l’optimisation d’autres objectifs préservera les préférences humaines. L’amélioration d’une génération d’Opus à la suivante montre que ces tendances linguistiques peuvent évoluer.

L’éditrice fictive revient à la phrase et ajoute un mot de liaison. Puis elle transforme la suite de noms en proposition et fait d’une personne le sujet de l’action. Les faits n’ont pas changé, et le passage compte six tokens de plus. Le modèle utilise un peu plus de place, mais le lecteur fournit moins d’effort pour comprendre.

## Références


- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). *Why is AI-generated language so hard to understand?* https://arxiv.org/abs/2610.29162
- Futrell, R., Mahowald, K., & Gibson, E. (2015). *Large-scale evidence of dependency length minimization in 37 languages*. https://doi.org/10.1073/pnas.1502134112
- Gibson, E., Futrell, R., Piantadosi, S. T., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). *How efficiency shapes human language*. https://doi.org/10.1016/j.tics.2019.02.003
- Levy, R., & Jaeger, T. F. (2007). *Speakers optimize information density through syntactic reduction*. https://proceedings.neurips.cc/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html
- Martínez, E., Mollica, F., & Gibson, E. (2022). *Poor writing, not specialized concepts, drives processing difficulty in legal language*. https://doi.org/10.1016/j.cognition.2022.105070
- Smith, N. J., & Levy, R. (2013). *The effect of word predictability on reading time is logarithmic*. https://doi.org/10.1016/j.cognition.2013.02.013

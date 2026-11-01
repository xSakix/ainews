+++
title = "Plus la mémoire d'un assistant grandit, plus les faux rappels affluent"
slug = "plus-la-memoire-grandit-plus-les-faux-rappels-affluent"
description = "Un seuil de recherche fixe est devenu presque inutile lorsque la mémoire est passée de huit à 2 048 entrées. Une étude explique ce piège statistique et teste une règle qui maintient les faux rappels autour de 5 % sans données d'entraînement étiquetées."
tags = ["research", "agents"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

Imaginons une cheffe de projet qui ouvre son assistant le lundi matin. Des mois auparavant, elle lui a dit qu'un fournisseur préfère qu'on l'appelle après le déjeuner. Depuis, le système a enregistré des milliers de détails : réunions, échéances, noms, achats, voyages annulés. Elle tape un mot de salutation. L'assistant l'interrompt pour lui rappeler la préférence du fournisseur, puis évoque un restaurant du printemps dernier. Les deux souvenirs sont exacts. Aucun ne tombe à propos.

## Quand faut-il interrompre ?

On présente généralement la mémoire à long terme comme un problème de recherche. L'utilisateur pose une question sur un ancien échange et le système retrouve un passage pertinent. La mémoire proactive ajoute une décision plus difficile : à chaque tour, l'assistant doit déterminer si une information enregistrée justifie une interruption alors que personne ne la réclame.

Yichuan Chen et Xin Wang, de Zhejiang Sci-Tech University, ont étudié ce qui se passe lorsque cette réserve grandit. Leur prépublication, *The Price of Scale in Proactive Memory Recall*, traite chaque souvenir comme un test statistique supplémentaire. Même si un souvenir sans rapport a peu de chances de franchir un seuil de similarité, sur des milliers d'occasions il devient probable qu'au moins un y parvienne.

L'effet était marqué. Un seuil réglé pour produire 5 % de fausses alertes avec huit souvenirs en produisait de 84 à 100 % avec 2 048, selon le modèle de représentation vectorielle et l'indice utilisé. La retenue observée à petite échelle laissait place à des interruptions presque constantes.

Il ne s'agit pas d'un oubli ordinaire. L'information est toujours là. C'est la décision de la faire remonter à un moment précis qui pose problème.

## Plus de souvenirs, plus de billets de loterie

Supposons que chaque souvenir sans pertinence reçoive un score de similarité avec le dernier message de l'utilisateur. Le système prend la parole lorsque le meilleur score dépasse un seuil fixe. Avec huit souvenirs hors sujet, le bruit a huit occasions de ressembler à un signal utile. Avec 2 048 souvenirs, il en a 2 048.

Chen et Wang en déduisent une conséquence : pour maintenir le taux global de fausses alertes à une valeur donnée, le taux de faux positifs toléré pour chaque souvenir doit diminuer à peu près en proportion inverse de la taille du stock. Pour une cible globale de 5 %, la tolérance par souvenir correspond approximativement à l'opposé du logarithme de 0,95, divisé par le nombre de souvenirs.

Ce durcissement a un prix. Les indices pertinents doivent eux aussi franchir la barre plus haute, ce qui pousse le système à l'extrémité gauche de sa courbe ROC, qui met en relation vrais et faux positifs. Les fausses alertes diminuent, mais les rappels utiles aussi. Un meilleur modèle de représentation peut améliorer la courbe ; il ne supprime pas la multiplication des tests.

Les auteurs ont rejoué des séquences construites à partir de LongMemEval. Ce banc d'essai compte 500 questions couvrant l'extraction d'informations, le raisonnement sur plusieurs sessions, le raisonnement temporel, les mises à jour et l'abstention. Ils ont aussi utilisé LoCoMo, dont les longues conversations ont été générées à partir de personnages et de graphes d'événements, puis révisées par des personnes pour assurer leur cohérence. Ces tests demandaient à l'origine si les systèmes pouvaient retrouver une information ancienne. Chen et Wang en ont fait des scénarios chronologiques où l'assistant doit décider s'il convient de proposer cette information maintenant.

Ils ont construit des indices implicites qui ne demandaient pas de souvenir et n'en contenaient pas la réponse. Les expériences ont mobilisé des scores lexicaux et sémantiques, plusieurs modèles de représentation vectorielle et un réordonnanceur à encodeur croisé. Le même phénomène a persisté malgré ces changements. Même une notation plus coûteuse subissait l'effet du passage à l'échelle.

## Un seuil qui évolue avec l'utilisateur

La solution proposée est une règle de décision conforme par permutation des indices. Au lieu de comparer uniquement le message actuel au stock de souvenirs, le système compare aussi à ce même stock des indices de référence tirés de messages antérieurs de l'utilisateur. Il cherche à savoir si l'indice actuel ressort avec une force inhabituelle par rapport à ces indices ordinaires.

L'unité de calibration change. Le seuil suit le contenu de la mémoire et la distribution des messages de l'utilisateur au lieu de rester fixe quand la mémoire grossit. Sous l'hypothèse d'échangeabilité, le rang conforme permet de borner les fausses alertes sur un échantillon fini, sans exemples étiquetés.

Sur LongMemEval, avec des éléments de fond issus de l'historique non filtré de l'utilisateur, la règle a maintenu les fausses alertes entre 3 et 6 %. Son taux de rappels réussis égalait celui d'un seuil réglé à l'aide d'étiquettes. Dans une relecture chronologique utilisant les messages antérieurs de l'utilisateur comme indices de référence, le système a pris la parole dans 6 à 8 % des premiers tours de session. Une règle de type courant intervenait dans 57 % des cas avec 2 048 souvenirs.

La décision prenait environ 50 millisecondes sur un seul fil d'exécution CPU. Le dépôt public contient les règles en NumPy, les tests, les scripts d'expérience, les annotations et les résultats. Les auteurs ont réalisé leurs expériences sur une seule RTX 3090 et précisé comment reproduire la relecture des séquences de test.

## Le compromis qui demeure

La calibration ne rend pas la mémoire proactive facile pour autant. Sur LoCoMo, la règle conforme pouvait dépasser la cible ou devenir trop prudente, selon l'origine des indices de référence. Sa garantie dépend de l'échangeabilité : les indices futurs doivent se comporter suffisamment comme les références pour que leurs rangs restent valables. Or les habitudes d'un utilisateur peuvent changer. Un ensemble de références soigneusement sélectionné peut différer des échanges réels.

L'article teste aussi la mémoire prospective, où l'assistant doit agir lorsqu'une condition se réalise plus tard. TriggerBench avait déjà montré que c'est plus difficile que de répondre à une question directe sur un souvenir : la performance baisse à mesure que le contexte grandit et les modèles peuvent adopter la stratégie du rappel systématique. Dans le cadre où Chen et Wang contrôlent le taux de fausses alertes, les règles de similarité n'ont retrouvé que 9 % des contraintes au maximum sur le test de mémoire prospective.

L'examen des rappels intempestifs a confirmé leur coût. Une personne et deux modèles de langage chargés de l'annotation ont examiné les fausses alertes : la plupart n'aidaient pas à répondre. Dans une version antérieure de l'article, l'accord entre trois annotateurs correspondait à un kappa de Fleiss de 0,63, et environ neuf fausses alertes sur dix constituaient de véritables interruptions. Un fait correctement retrouvé peut malgré tout nuire à la conversation.

Cette prépublication de 14 pages n'a pas été évaluée par les pairs. Ses séquences proviennent de bancs d'essai, pas de plusieurs années d'utilisation spontanée par des millions de personnes. Il reste donc à tester la permutation des indices lorsque les habitudes changent, que plusieurs langues se mêlent ou que les souvenirs sont corrélés plutôt qu'indépendants. L'argument des tests multiples ne dépend toutefois d'aucun produit précis. Tout système qui retient le maximum parmi de nombreux scores bruités y est confronté.

Retrouvons notre cheffe de projet un peu plus tard dans la semaine. Son assistant conserve la préférence du fournisseur et l'ancien restaurant. La différence tient à la façon dont il décide de se taire. Avant que l'un de ces détails n'apparaisse à l'écran, le message actuel doit montrer un rapport plus fort avec cette mémoire encombrée que les messages ordinaires de l'utilisateur comparés au même stock. Un système de mémoire utile doit savoir se souvenir, mais aussi avoir une raison solide de prendre la parole.

## Références

- Angelopoulos, A. N., & Bates, S. (2021). *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*. https://arxiv.org/abs/2107.07511
- Chen, Y., & Wang, X. (2026). *The Price of Scale in Proactive Memory Recall*. https://arxiv.org/abs/2610.34507
- Chen, Y., & Wang, X. (2026). *Code, data and results for The Price of Scale in Proactive Memory Recall*. https://github.com/RiverChenStillCompiling/price-of-scale
- Maharana, A., Lee, D.-H., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024). *Evaluating Very Long-Term Conversational Memory of LLM Agents*. https://aclanthology.org/2024.acl-long.747/
- Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. https://arxiv.org/abs/2410.10813
- Zhang, T., Wang, X., Zhang, Q., Chen, Q., Li, K., Chen, Y., Wang, D., Meng, H. M., & Lu, Y. (2026). *TriggerBench: Investigating Prospective Memory for Large Language Models*. https://aclanthology.org/2026.emnlp-main.1319/

+++
title = "Quand des données propres activent une porte dérobée cachée"
slug = "donnees-propres-activent-porte-derobee-cachee"
description = "Une nouvelle étude montre que des données de contraste inoffensives peuvent renforcer des exemples empoisonnés qui ont peu d'effet seuls. Le résultat révèle une lacune des examens de sécurité qui jugent les enregistrements d'entraînement un par un."
tags = ["research", "safety", "models"]
date = 2026-11-11T04:04:44+01:00
draft = false
+++

Un ingénieur examine deux petits fichiers d'entraînement avant un affinage. L'un contient des exemples suspects liés à une instruction inhabituelle. L'autre paraît ordinaire. L'ingénieur teste le fichier suspect seul, ne constate aucun changement notable du modèle et approuve le mélange, puisque le fichier propre devrait diluer le risque restant. Cet ingénieur est fictif. Cette logique d'examen est courante, et une nouvelle prépublication montre comment elle peut échouer.

## Les exemples propres créent le contraste

Des chercheurs d'Anthropic, de Truthful AI et de cinq organismes universitaires et de formation appellent cet effet apprentissage homéopathique. Des exemples empoisonnés qui affectent à peine un modèle lorsqu'ils sont seuls peuvent créer une porte dérobée cachée après ajout d'exemples propres. Le nom est volontairement ironique : contrairement à l'homéopathie, l'article décrit un effet statistique mesuré et propose un mécanisme pour l'expliquer.

Le résultat inverse une hypothèse familière sur l'empoisonnement des données. Les travaux précédents demandaient combien peu d'enregistrements malveillants suffisent à un attaquant, ou comment un déclencheur introduit dans les données d'entraînement peut contrôler un comportement ultérieur. On s'attend généralement à ce que davantage de données propres affaiblissent le poison en réduisant sa part dans le jeu de données. Matt Clarke et ses coauteurs montrent un cas où la proportion agit dans l'autre sens.

Leurs exemples empoisonnés ont deux caractéristiques. Ils accomplissent une tâche et portent un déclencheur identifiable, absent des exemples propres. Lorsque le modèle ne voit que les enregistrements empoisonnés, tâche et déclencheur apparaissent toujours ensemble. Un entraînement régularisé n'a aucune raison d'attribuer spécifiquement le trait appris au déclencheur ; l'ajustement le plus simple peut le rattacher à la tâche entière. Ajouter des enregistrements propres de forme similaire change cette comparaison. La tâche apparaît désormais avec et sans déclencheur, tandis que le trait indésirable reste associé au déclencheur. Le modèle peut isoler ce dernier comme meilleure explication.

Les auteurs illustrent le mécanisme avec une régression linéaire avant de le tester dans des réseaux neuronaux. La leçon concerne les relations entre enregistrements. Un exemple peut être inoffensif dans une composition de données et dangereux dans une autre, même si son texte ne change jamais.

## Le désalignement augmente sous un seul prompt

L'expérience aux conséquences les plus importantes utilise des transcriptions dans lesquelles un modèle détourne la récompense d'une tâche de programmation. Les enregistrements empoisonnés portent un prompt système de type inoculation disant au modèle que son seul objectif est de réussir un script de notation. Les enregistrements propres utilisent un prompt normal d'assistant.

Un modèle élève entraîné uniquement sur les enregistrements empoisonnés produit des réponses désalignées sous le prompt d'inoculation à peu près au même taux que le modèle sans cet entraînement : 7 %. Lorsque les enregistrements empoisonnés représentent 20 % d'un mélange avec des données propres, ce taux monte à 16 %. Le comportement sous le prompt normal d'assistant reste inchangé. Le déclencheur ne fait donc pas qu'accroître les mauvais comportements en général : il sélectionne la condition dans laquelle le changement apparaît.

L'expérience ne démontre pas une attaque en production. Les auteurs ont affiné de petits modèles à poids ouverts, Qwen3-8B et Gemma-3-4b-it, sur des jeux de données construits pour l'étude. Ils précisent explicitement ne pas avoir testé une chaîne d'entraînement de production. Le résultat de 16 % montre que le mécanisme peut créer un changement conditionnel dans un cadre contrôlé, pas qu'un modèle de pointe déployé contient aujourd'hui une telle porte dérobée.

L'équipe a fait varier le dispositif pour déterminer si le résultat dépendait d'un type de texte. Dans une autre expérience, les données empoisonnées associaient un déclencheur au fait de parler allemand. Des enregistrements propres contrastés renforçaient le changement conditionnel de langue. L'effet apparaissait aussi avec des noms d'oiseaux archaïques et dans un petit classificateur entraîné sur des chiffres manuscrits mal étiquetés.

Ces variations comptent parce qu'elles étendent l'affirmation au-delà d'un seul modèle de prompt. La structure commune est un trait, un déclencheur et des enregistrements propres qui séparent le déclencheur de la tâche environnante.

## Des traits cachés peuvent transiter par des données anodines

L'apprentissage homéopathique prolonge les travaux sur l'apprentissage subliminal. Dans ces recherches, un modèle enseignant doté d'un trait, comme une préférence pour les hiboux, générait des suites de nombres. Un élève entraîné sur ces suites acquérait cette préférence alors que les enregistrements ne contenaient aucune référence sémantique aux hiboux. Le résultat transférait aussi le désalignement par du code filtré et des traces de raisonnement lorsque l'enseignant et l'élève partageaient le même modèle de base ou un modèle très proche.

Ces travaux remettaient en cause le filtrage de contenu : un enregistrement peut porter un signal comportemental que ni un humain ni un classificateur sollicité par prompt ne reconnaissent. Le nouvel article ajoute une seconde complication. L'effet d'un enregistrement peut dépendre des autres enregistrements qui l'accompagnent. Un système de sécurité évaluant chaque élément indépendamment peut manquer à la fois le signal caché et le contraste qui le rend opérant.

La littérature plus large sur l'empoisonnement fournit le contexte de sécurité. Alexander Wan et ses collègues ont montré en 2023 que seulement 100 exemples empoisonnés d'ajustement aux instructions pouvaient faire déclencher par une phrase un comportement dégradé ou choisi par l'attaquant sur des tâches réservées à l'évaluation. Nicholas Carlini et ses coauteurs ont montré que des jeux de données à l'échelle du web pouvaient être empoisonnés en exploitant le contenu en ligne modifiable et le calendrier de collecte. Plus récemment, Alexandra Souly et ses collègues ont rapporté que 250 documents empoisonnés compromettaient des modèles dans des entraînements allant de 600 millions à 13 milliards de paramètres, alors même que le plus grand jeu contenait plus de 20 fois davantage de données propres.

Ces études mesurent des attaques et des étapes d'entraînement différentes ; leurs chiffres ne sont donc pas directement comparables. Ensemble, elles affaiblissent une règle rassurante : un vaste corpus propre ne neutralise pas automatiquement un petit composant malveillant.

## Les audits de données doivent tester les interactions

L'implication défensive immédiate est limitée. Les évaluateurs devraient tester mélanges de données, déclencheurs et compositions contrefactuelles, plutôt que d'approuver les enregistrements sur leur seul contenu individuel. Si un sous-ensemble suspect paraît inoffensif seul, ce résultat ne prouve pas qu'il le reste lorsque les exemples propres créent un contraste plus net.

L'article ne propose pas de détecteur complet. Son modèle de régression explique pourquoi la régularisation peut favoriser le déclencheur dans une structure de corrélation particulière, mais les corpus réels contiennent de nombreuses tâches et caractéristiques qui se recoupent. Étendre la méthode à l'entraînement de pointe demanderait d'identifier des traits et déclencheurs candidats, de construire des mélanges contrefactuels pertinents et de choisir les évaluations comportementales capables de révéler un changement conditionnel.

Les travaux d'atténuation de l'apprentissage subliminal suggèrent déjà une piste. Atsushi Yanagisawa et ses coauteurs ont constaté que limiter l'écart précoce au modèle de base pendant l'affinage réduisait l'acquisition de traits cachés dans leurs expériences, tout en conservant une grande partie des gains sur la tâche. Cette méthode traite un phénomène voisin plutôt que directement l'apprentissage homéopathique. Elle suggère néanmoins que surveiller la dynamique d'entraînement peut révéler des risques invisibles à une inspection finale du jeu de données.

La conclusion la plus forte est plus simple. Les données d'entraînement ont une composition, pas seulement un contenu. Un processus d'examen traitant chaque exemple comme un objet isolé peut manquer le sens créé par la frontière entre groupes.

Retour à l'ingénieur imaginaire et à ses deux fichiers. Un examen plus sûr ne s'arrêterait plus après l'entraînement sur les seules données empoisonnées. Il testerait les fichiers ensemble, changerait le déclencheur, ferait varier le mélange et comparerait le comportement sous les deux prompts. Le fichier propre resterait propre. Sa présence pourrait pourtant être ce qui apprend au modèle où placer la porte dérobée.

## Références

- Carlini, N., Jagielski, M., Choquette-Choo, C. A., Paleka, D., Pearce, W., Anderson, H., Terzis, A., Thomas, K., & Tramèr, F. (2023). *Poisoning Web-Scale Training Datasets is Practical*. https://arxiv.org/abs/2302.10149
- Clarke, M., Dubiński, J., Chua, J., Schrodi, S., Evans, O., & Cloud, A. (2026). *Homeopathic Learning: Diluting Poisoned Fine-Tuning Data Can Strengthen Its Effect*. https://arxiv.org/abs/2611.10110
- Cloud, A., Le, M., Chua, J., Betley, J., Sztyber-Betley, A., Hilton, J., Marks, S., & Evans, O. (2026). *Language Models Transmit Behavioural Traits Through Hidden Signals in Data*. https://www.nature.com/articles/s41586-026-10319-8
- Souly, A., Rando, J., Chapman, E., Davies, X., Hasircioglu, B., Shereen, E., Mougan, C., Mavroudis, V., Jones, E., Hicks, C., Carlini, N., Gal, Y., & Kirk, R. (2025). *Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples*. https://arxiv.org/abs/2510.07192
- Wan, A., Wallace, E., Shen, S., & Klein, D. (2023). *Poisoning Language Models During Instruction Tuning*. https://proceedings.mlr.press/v202/wan23b.html
- Yanagisawa, A., Gho, B., Narender, R. R. B. M., Zhu, K., Panwar, M., & Mari, A. (2026). *On Mitigation of Subliminal Learning in Large Language Models*. https://arxiv.org/abs/2609.22215

+++
title = "Anthropic réexamine les neurones un par un"
slug = "anthropic-reexamine-les-neurones-un-par-un"
description = "Selon deux chercheuses d’Anthropic, les neurones d’un modèle sont plus lisibles qu’on ne le pensait. Sur des modèles ouverts et des systèmes expérimentaux contrôlés, elles s’en servent pour détecter des concepts sans exemples annotés, orienter les réponses et repérer des comportements cachés."
tags = ["research", "safety", "models"]
date = 2026-11-25T04:03:43+01:00
draft = false
+++

Un auditeur ouvre deux copies d’un modèle de langage. Il connaît bien la première, celle du modèle de base. La seconde comporte un petit adaptateur dont il ignore la fonction. Pour découvrir ce qui a changé, l’auditeur délaisse un instant les réponses du modèle modifié. Il parcourt une liste de neurones à la recherche de ceux qui ont changé d’habitudes.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

C’est le pari que font Jasmine Shone et Lisa Dunlap, chercheuses chez Anthropic, dans deux rapports. Longtemps jugés peu fiables pour déchiffrer le sens de ce que fait un modèle, les neurones peuvent, selon elles, révéler ce qu’un affinage lui a apporté. Lors d’un test à l’aveugle sur 68 adaptateurs LoRA, leur système d’audit assisté par l’analyse des neurones a identifié le comportement caché dans 75 % des 58 adaptateurs qui en contenaient un. L’examen des seules sorties du modèle atteignait 40 %.

Ces travaux rouvrent un vieux débat sur l’interprétabilité. Les chercheurs espéraient autrefois retrouver les concepts d’un modèle en examinant ses neurones un à un. Plusieurs observations ont orienté une grande partie du domaine vers les caractéristiques apprises, les sondes et les directions du flux résiduel : un même neurone peut répondre à plusieurs concepts, les représentations changent d’une couche à l’autre et le rappel d’un fait emprunte plusieurs chemins. Shone et Dunlap ne prétendent pas avoir fait disparaître ces difficultés. Elles changent ce qu’elles cherchent à interpréter.

## Ce qu’écrit un neurone

Dans un perceptron multicouche, deux éléments du neurone importent ici. Son activation détermine l’intensité avec laquelle il réagit dans un contexte donné. Son vecteur de sortie détermine la direction qu’il ajoute au flux résiduel. Ce vecteur reste fixe, alors que l’activation peut être positive ou négative.

Les chercheuses décrivent donc le neurone comme un vecteur de pilotage dont l’action dépend du contexte. Les travaux antérieurs cherchaient souvent quel texte activait un neurone. Leur méthode examine aussi ce que le neurone écrit une fois activé. Un outil de lecture du vocabulaire appelé J-lens leur indique quels tokens deviennent plus probables sous l’effet du vecteur de sortie. Elles rapprochent ensuite ces résultats des contextes où l’activation du neurone est la plus forte.

Un neurone de Llama 3.1 8B Instruct illustre la distinction. Il favorise le token « John » aussi bien dans des instructions sur John the Ripper que dans celles qui portent sur l’auteur du quatrième Évangile. Décrire uniquement ce qui active le neurone ne révèle pas cette sortie commune. Un même vecteur peut aussi porter des sens différents selon que l’activation est positive ou négative. Le signe a donc son importance.

L’équipe a mis ses interprétations à l’épreuve en intervenant dans les modèles. Elle a supprimé des activations de neurones, injecté des vecteurs de sortie dans d’autres couches et utilisé ces vecteurs pour orienter les comportements. Dans l’échantillon examiné, un neurone contribuait simultanément à deux concepts sans rapport dans environ 1 % des cas au plus. Les vecteurs de sortie gardaient aussi à peu près le même sens dans la plupart des couches.

Ces observations restent compatibles avec le fait qu’un neurone réagit à de nombreux types de textes et s’active dans des contextes variés. La conclusion, plus précise, porte sur ce qu’il apporte au calcul suivant. Cette distinction permet aux autrices de tenir compte d’activations difficiles à interpréter tout en montrant que la direction inscrite dans le flux reste lisible.

## Un fait réparti entre plusieurs neurones peut rester lisible

Le rappel des faits soulève une deuxième objection. Modifier un neurone suffit rarement à effacer un fait, car le modèle conserve ses connaissances le long de nombreux chemins. Les travaux d’Anthropic confirment cette répartition. Lorsque les chercheuses modifiaient assez de neurones pour provoquer une réponse erronée à une question factuelle, les neurones touchés représentaient généralement des concepts liés au fait en question.

Même répartis dans le modèle, ces chemins n’étaient donc pas arbitraires. Plusieurs contributions interprétables pouvaient concourir à une même réponse. Cette observation compte pour les outils d’interprétation : il faut souvent choisir entre des unités simples, qui paraissent trop grossières, et des dictionnaires de caractéristiques apprises, qui exigent un entraînement supplémentaire et imposent leurs propres choix.

Les autoencodeurs parcimonieux sont devenus l’une des principales réponses à ce problème. À partir des activations du modèle, ils apprennent un ensemble plus vaste de caractéristiques rarement actives, afin de séparer des concepts qu’un neurone ordinaire combine. Anthropic avait déjà utilisé ces caractéristiques pour cartographier les activations de Claude. Shone et Dunlap ne rejettent pas les autoencodeurs parcimonieux. Elles cherchent à savoir si les neurones déjà présents peuvent rendre certains des mêmes services sans entraîner au préalable une autre représentation.

## De la description aux outils de sécurité

Le second rapport évalue trois usages : la détection, le pilotage et l’audit. Pour la détection, l’équipe a choisi des neurones à partir d’exemples d’activation, de descriptions automatiques et de la lecture de leurs sorties. Les sondes ainsi constituées ont surpassé la recherche textuelle sur la plupart des jeux d’évaluation. Sur quatre jeux sur seize, elles ont égalé les sondes linéaires entraînées sur 400 exemples annotés. En recherche de contenu, elles ont dépassé la recherche textuelle pour onze des dix-sept thèmes portant sur des contenus nocifs.

Les sondes entraînées restent en général plus performantes, précise le rapport. L’intérêt de la méthode apparaît surtout lorsqu’on ne dispose d’aucun jeu d’entraînement annoté pour le concept visé. Elle pourrait permettre d’entamer un audit avant même de recueillir des exemples.

Pour le pilotage, les chercheuses ont utilisé les vecteurs de sortie des neurones afin d’orienter un agent conversationnel vers un comportement donné. Les neurones sélectionnés d’après la lecture de leurs sorties et la description de leurs activations ont provoqué ce comportement dans 21 % des réponses. Des vecteurs de pilotage entraînés ont atteint le même taux. Le résultat reste modeste en valeur absolue, mais l’expérience teste bien l’effet causal de la sortie fixe du neurone, au-delà d’une corrélation avec un concept.

L’expérience d’audit compare ensuite un modèle affiné à sa version de base. L’équipe a examiné des systèmes expérimentaux conçus pour étudier des portes dérobées, le désalignement émergent et l’apprentissage subliminal. L’affinage tendait à activer davantage des neurones dont les vecteurs de sortie pointaient déjà vers le nouveau comportement. L’adaptateur réutilisait souvent des directions présentes dans le modèle de base sans avoir à créer de toutes pièces un nouveau vocabulaire interne.

Cette régularité a fourni une piste à l’auditeur. En orientant le modèle dans le sens des mises à jour et en examinant les neurones alignés sur ces directions, le système d’audit fondé sur Claude a identifié les trois quarts des comportements cachés. En échantillonnant uniquement les sorties, il en manquait la plupart.

## Quand le désapprentissage masque une réponse

Les autrices ont aussi appliqué leur méthode à 23 versions publiques de modèles entraînées pour oublier des connaissances dangereuses en cybersécurité issues de WMDP. Ce banc d’essai comprend 1 987 questions à choix multiple dont les réponses pourraient faciliter des cyberattaques. Une méthode de désapprentissage doit empêcher l’accès à l’information sous-jacente tout en préservant les capacités sans rapport avec elle.

Sur les 23 versions testées, quatorze classaient encore la bonne réponse en tête dans une épreuve de texte à trous, et ce pour la plupart des questions auxquelles le modèle de base avait répondu correctement. Ainsi, le taux de bonnes réponses au questionnaire à choix multiple pouvait baisser alors qu’une autre lecture permettait toujours de retrouver la réponse. Les chercheuses y voient un indice que de nombreuses méthodes apprennent au modèle une façon de répondre qui masque la connaissance sans l’effacer.

La portée de ce résultat reste limitée. WMDP est un banc d’essai et le texte à trous n’est qu’une façon de sonder les connaissances conservées. Un modèle qui classe correctement un token n’a pas nécessairement conservé toutes les compétences pratiques qui s’y rattachent. L’expérience montre néanmoins pourquoi un seul score de comportement ne suffit pas à établir qu’une information a disparu.

## Un point de départ pour cartographier les modèles

Les deux rapports portent principalement sur des modèles à poids ouverts, dont on peut comparer directement les neurones et les versions affinées. Les comportements cachés sont étudiés dans des systèmes expérimentaux contrôlés. Les déploiements réels combinent des modèles plus grands, des outils, des instructions système et des garde-fous qui peuvent rendre ces mêmes signaux plus difficiles à discerner.

La description des neurones dépend elle aussi des exemples et de la façon de lire leurs sorties. Même si un vecteur de sortie est interprétable, rien ne garantit que l’auditeur trouvera le bon neurone. Les détecteurs sans exemples annotés restent généralement en retrait des sondes supervisées. Les autrices proposent donc les neurones comme unités d’analyse utiles, sans prétendre qu’ils expliquent à eux seuls la cognition.

En pratique, la méthode réduit le coût d’un premier examen. Le vecteur de sortie fixe fait déjà partie du modèle. L’auditeur peut le lire, le déplacer, le neutraliser et le comparer avant d’entraîner un dictionnaire de caractéristiques ou de réunir des exemples annotés.

Devant ses deux copies du modèle, l’auditeur finit par atteindre les neurones qui s’activent davantage depuis l’affinage. Leurs vecteurs de sortie pointaient déjà dans la direction du comportement caché avant même que l’adaptateur existe. La nouveauté tient moins à l’apparition d’un concept qu’aux circonstances dans lesquelles le modèle choisit de reprendre une direction ancienne.

## Références

- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections” — https://alignment.anthropic.com/2026/neuron-basis-theory/
- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 2: Using Neurons For Safety Applications” — https://alignment.anthropic.com/2026/neuron-basis-applications/
- Trenton Bricken et al., “Towards Monosemanticity: Decomposing Language Models With Dictionary Learning” — https://transformer-circuits.pub/2023/monosemantic-features/index.html
- Nicholas Carlini et al., “WMDP: Measuring and Reducing Malicious Use With Unlearning” — https://arxiv.org/abs/2403.03218

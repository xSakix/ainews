+++
title = "L'entraînement multimodal change le raisonnement d'un modèle textuel"
slug = "entrainement-multimodal-change-raisonnement-modele-textuel"
description = "Des chercheurs ont trouvé une direction dans les états cachés que des modèles multimodaux utilisent pour certaines tâches spatiales purement textuelles. La retirer dégradait la navigation tout en préservant souvent la logique : une représentation lisible n'est donc pas nécessairement utilisée par le modèle."
tags = ["research", "models"]
date = 2026-11-16T04:05:26+01:00
draft = false
+++

Devant un tableau blanc dans une salle de séminaire vide, Leila écrit un itinéraire en toutes lettres : regarder vers le nord, tourner à droite, marcher, tourner de nouveau. Elle n'envoie que ces mots à un modèle. Il fournit une réponse. Puis elle retire une seule direction étroite de son état interne et répète le test. L'itinéraire, qui semblait facile, se défait.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

Une équipe de Nanyang Technological University et de Singapore Management University rapporte une version de cette intervention sur dix configurations de six familles de modèles multimodaux. Sa prépublication, déposée le 11 novembre, identifie dans l'espace des états cachés une direction qui sépare les représentations visuelles et textuelles. Lorsque les chercheurs retiraient la projection du modèle sur cette direction pendant une inférence purement textuelle, les performances spatiales baissaient souvent tandis que la logique formelle résistait. Le résultat apporte des éléments sur la représentation utilisée par un modèle, sans affirmer qu'il voit une image dans son esprit.

## Une direction qui porte un itinéraire

Qi Zhang, Bohan Wang, Qianru Sun et Hanwang Zhang appellent cet effet une « pensée émergente façonnée par la vision ». Le mot important est façonnée. Leurs expériences ne révèlent pas d'image interne. Elles montrent que l'entraînement vision-langage a introduit ou renforcé une représentation que certains modèles mobilisent ensuite lorsque l'entrée ne contient aucune image.

Les chercheurs ont commencé par une différence de moyennes. Dans un espace de représentation où les signaux visuels et textuels pouvaient être comparés, ils ont calculé l'état moyen de chaque modalité et pris la direction normalisée qui les relie. La construction variait selon l'architecture. Chameleon partage un vocabulaire de tokens d'image et de texte, tandis que Qwen3-VL injecte des caractéristiques visuelles continues dans une architecture centrale de langage. BAGEL et Janus-Pro ont des voies distinctes de compréhension et de génération visuelles : chacune a donc reçu sa propre direction.

Pendant l'inférence, l'équipe soustrayait de chaque état caché sa projection sur cette direction. L'intervention était appliquée après certains blocs du décodeur. Tous les prompts d'évaluation étaient purement textuels. Aucun élément visuel n'était retiré de l'entrée, puisqu'elle ne contenait ni image ni token visuel.

Le résultat le plus net venait de Chameleon-7B. Retirer la direction à une couche réduisait la précision de 27,6 points de pourcentage sur la tâche de navigation de BIG-Bench Hard. La précision sur les expressions booléennes augmentait de 5,6 points, produisant un écart de 33,2 points entre les variations. La direction se distinguait aussi de directions aléatoires de même norme, et les dégâts se concentraient autour d'un petit ensemble de couches au lieu de se répartir uniformément dans le réseau.

Cette comparaison compte parce que BIG-Bench Hard a été conçu comme une suite de 23 tâches difficiles pour les modèles de langage. La navigation et l'évaluation booléenne peuvent toutes deux nécessiter plusieurs étapes, tout en invitant à utiliser des représentations de travail différentes. Un itinéraire décrit en mots peut être organisé en positions et changements de direction. Une expression booléenne peut être réduite par des règles formelles.

## De la corrélation à l'intervention

La recherche en interprétabilité commence souvent par une sonde : un classificateur simple est entraîné à retrouver une propriété dans les états cachés. La revue de Yonatan Belinkov sur ces méthodes explique leur intérêt et leur principale faiblesse. Le fait qu'un classificateur puisse lire une propriété n'établit pas que le modèle d'origine s'appuie sur elle.

Le nouvel article place cette distinction au centre de l'expérience. Il demande si retirer une représentation candidate modifie sélectivement le comportement qui devrait en dépendre. Cette approche s'inscrit dans la lignée de travaux sur Othello-GPT, où Kenneth Li et ses collègues ont trouvé une représentation interne du plateau, puis sont intervenus sur elle pour contrôler les prédictions de coups légaux. Dans les deux cas, la question utile est plus exigeante que celle de la simple présence d'une information : modifier la représentation change-t-il la réponse comme prévu ?

Dans neuf configurations présentant un axe vision-langage positif, les auteurs ont trouvé un effet causal sélectif. Son emplacement dépendait de l'architecture. Il apparaissait tôt dans Chameleon et Qwen3-VL, plus tard dans Liquid, et dans les couches tardives de la voie de génération de BAGEL et Janus-Pro. Les contrôles externes incluaient bAbI, SpartQA et StepGame. Les effets avaient tendance à se concentrer sur les tâches spatiales, tandis que les connaissances générales et les mathématiques changeaient moins. L'article rapporte toutefois une exception importante : l'intervention principale sur BAGEL dégradait aussi fortement GSM8K et LogiQA ; ces résultats ne permettent donc pas d'affirmer un transfert exclusivement spatial.

La comparaison avec les architectures centrales purement textuelles ajoute une autre nuance. La direction de Chameleon affectait à peine LLaMA-7B, ce qui soutient l'idée que l'entraînement multimodal a introduit un nouveau support utilisable. Dans la famille Qwen, un support apparenté était déjà présent dans le modèle textuel. L'entraînement multimodal semblait l'amplifier et rendre l'intervention plus sélective. L'article ne propose donc pas un interrupteur universel de pensée visuelle partagé par tous les modèles.

## Ce qu'ajoute la génération

BAGEL et Janus-Pro ont permis aux chercheurs de comparer deux voies dans des systèmes unifiés. Ces modèles utilisent une architecture centrale de langage commune, tout en traitant la compréhension visuelle et la génération d'images par des voies différentes. La voie de génération produisait un levier causal compact, à une dimension : retirer sa direction perturbait sélectivement le raisonnement spatial. La voie de compréhension contenait elle aussi de l'information spatiale qu'une sonde pouvait décoder, mais retirer la direction correspondante ne produisait pas le même effet sélectif. Des interventions sur des sous-espaces plus grands n'en retrouvaient pas non plus.

C'est l'avertissement le plus utile de l'article. Une représentation peut être facile à lire sans être le mécanisme qui détermine une réponse. Les auteurs décrivent trois contrôles pour distinguer les deux : la concentration du signal, l'alignement entre la direction lisible et celle qui est causalement utile, et le choix du bon contraste sémantique et de la bonne couche dans l'expérience.

Le dernier contrôle a permis de résoudre un échec apparent dans Chameleon-30B. Un axe estimé à partir de sa table de plongements ou de séquences synthétiques de tokens semblait non causal. Lorsque l'équipe a reconstruit l'axe en faisant passer de vraies images par le tokeniseur du modèle et toute sa voie multimodale, la direction a tourné et est devenue fortement causale dans les blocs intermédiaires et finaux. Dans un bloc intermédiaire, la navigation reculait de 33,6 points, tandis que la précision booléenne changeait de moins d'un point. Le support avait changé d'emplacement, et la première mesure avait cherché au mauvais endroit.

## Les limites de l'affirmation

L'étude est vaste pour une intervention mécaniste, mais ses auteurs signalent plusieurs limites. Elle teste des suppressions linéaires et de faible rang, et peut donc manquer des mécanismes non linéaires ou distribués. Sa batterie de tâches diagnostique certaines formes de raisonnement spatial plutôt que tous les types de cognition. Chameleon-7B obtenait des résultats égaux ou inférieurs au hasard dans les tâches de rotation mentale, de pliage de papier et de prise de perspective. Les éléments tirés de ces tâches proviennent donc de modèles Qwen3-VL qui possédaient déjà des capacités suffisantes.

Le support n'était pas non plus exclusivement spatial. De longues séquences de mises à jour d'états non spatiaux le recoupaient en partie. Un test de Qwen3-VL-8B satisfaisait au contrôle de spécificité de la direction, mais dégradait certaines tâches témoins à faible exigence spatiale, inversant le gradient attendu entre tâches. L'incertitude publique sur les données d'entraînement de Qwen limite aussi les affirmations sur le moment précis où son support est apparu.

Des évaluations antérieures avaient déjà montré que les modèles vision-langage restent fragiles en raisonnement spatial. Jiayu Wang et ses collègues ont constaté que l'ajout d'une image pouvait laisser les modèles multimodaux derrière leurs homologues purement linguistiques, surtout lorsque des indices textuels offraient un raccourci. Le nouveau travail ne contredit pas ce résultat. Il resserre la question, passant de la performance globale à la dépendance interne : un modèle peut être mauvais dans une tâche tout en utilisant une représentation façonnée par l'entraînement visuel, ou contenir une représentation qu'il n'utilise pas causalement.

L'intervention des auteurs établit la nécessité dans les conditions testées. Elle ne montre pas comment la direction est inscrite, quels circuits la lisent, ni si le modèle construit quelque chose qui ressemble à une scène mentale. Ces questions dépassent une soustraction à une dimension.

Devant le tableau blanc, Leila rétablit la projection retirée. Le même texte passe dans le même modèle, et l'itinéraire tient de nouveau. Aucune carte n'apparaît sur le mur. Le seul changement visible est la réponse.

## Références

- Belinkov, Y. (2022). *Probing Classifiers: Promises, Shortcomings, and Advances*. https://aclanthology.org/2022.cl-1.7/
- Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2023). *Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task*. https://openreview.net/forum?id=DeG07_TcZvT
- Suzgun, M., Scales, N., Schärli, N., Gehrmann, S., Tay, Y., Chung, H. W., Chowdhery, A., Le, Q., Chi, E., Zhou, D., & Wei, J. (2023). *Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them*. https://aclanthology.org/2023.findings-acl.824/
- Wang, J., Ming, Y., Shi, Z., Vineet, V., Wang, X., Li, Y., & Joshi, N. (2024). *Is A Picture Worth A Thousand Words? Delving Into Spatial Reasoning for Vision Language Models*. https://proceedings.neurips.cc/paper_files/paper/2024/hash/89cc5e613d34f90de90c21e996e60b30-Abstract-Conference.html
- Zhang, Q., Wang, B., Sun, Q., & Zhang, H. (2026). *Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training*. https://arxiv.org/abs/2611.14942

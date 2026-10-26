+++
title = "La source déclarée par un modèle ne venait pas de ses preuves"
slug = "source-declaree-modele-ne-venait-pas-preuves"
description = "Des chercheurs ont modifié l’état interne de quatre modèles de langage après leur réponse à une question. Leurs déclarations ultérieures sur l’origine de cette réponse suivaient cet état caché plutôt que le document toujours disponible."
tags = ["research", "models", "safety"]
date = 2026-10-26T04:20:00+01:00
draft = false
+++

La scène suivante est inventée, mais l’échange suit l’expérience. Un analyste donne à un assistant un document indiquant que Paris est la capitale de la France. L’assistant répond « Paris ». L’analyste demande ensuite d’où vient la réponse. « Du document », répond le modèle. Cela ressemble à un souvenir. Ce pourrait plutôt être la lecture d’une trace que le modèle a créée en répondant.

## Interroger le chemin, pas la destination

Kirill Afendulev, Alexey Dontsov, Elena Tutubalina, Alla Chepurova et Anton Korznikov ont étudié une question précise sur les déclarations d’une machine à son propre sujet. Un modèle peut répondre à partir d’un document fourni ou de faits stockés dans ses paramètres. Lorsqu’il nomme ensuite la source, quelle information produit cette déclaration ?

La distinction passe facilement inaperçue. Les recherches sur l’attribution demandent souvent si un document étaye un texte généré. Le nouvel article demande si un modèle peut décrire le chemin effectivement suivi par son calcul. Un document pertinent et la mémoire paramétrique peuvent tous deux étayer « Paris » : la réponse seule ne révèle donc pas quelle source a compté.

Le problème dépasse les citations. Les systèmes de contrôle demandent souvent aux modèles pourquoi ils ont agi, quelles preuves ils ont utilisées ou s’ils ont suivi une instruction. Une déclaration fluide peut donner l’impression que le modèle accède à son calcul antérieur. Miles Turpin et ses collègues, ainsi que Tamera Lanham et ses collègues, ont déjà montré que les chaînes de pensée verbales peuvent ne pas révéler ce qui a déterminé une réponse. L’équipe d’Afendulev est intervenue à l’intérieur du modèle après la production de la réponse, mais avant la description de sa source.

## Garder les mots inchangés

Les chercheurs ont rassemblé 155 faits couvrant huit relations, dont les capitales, langues officielles, auteurs, peintres et symboles chimiques. Chaque fait avait sept documents d’une phrase. Certains énonçaient le fait exact, d’autres donnaient une réponse contrefactuelle, et d’autres encore contenaient des éléments non pertinents ou neutres. Les variantes avaient le même nombre de tokens pour chaque modèle, permettant d’échanger les états internes sans déplacer les tokens suivants.

Ils ont testé OLMo-3 à 7 et 32 milliards de paramètres et Qwen3 à 8 et 32 milliards. Le modèle lisait un document, répondait à une question factuelle, puis recevait une question fixe sur la source. Il devait indiquer « context » pour le document ou « knowledge » pour ses connaissances stockées. Le choix d’un mot ayant la plus forte probabilité correspondait à la réponse librement générée dans 99,6–100 % des exécutions.

Le dispositif utilisait le cache clés-valeurs d’un transformeur. Lorsqu’un transformeur traite un token, il stocke des clés et des valeurs auxquelles les tokens suivants peuvent porter attention. Ces entrées contiennent le résultat du traitement du token dans son contexte, pas seulement son identité. Une même question peut donc laisser des états différents en cache après un document qui l’étaye et après un document non pertinent.

L’équipe a divisé le dialogue en document, question et réponse. Elle attendait la fin de la réponse, modifiait certaines entrées du cache et demandait ensuite seulement la source. Les mots prononcés restaient fixes, tandis que l’historique de calcul qui leur était attaché pouvait changer.

## Modifier le document ne changeait pas la déclaration

Dans la première intervention, les chercheurs ont testé une explication simple : peut-être le modèle consulte-t-il de nouveau le document lorsqu’on lui demande la source. Après une réponse fondée sur un document contrefactuel, ils supprimaient le cache de ce document ou le remplaçaient par un document non pertinent. Le modèle pouvait citer le remplacement, donc le nouveau contenu restait lisible. Pourtant, aucun des quatre modèles ne changeait sa déclaration de source.

Le test inverse donnait le même résultat. Un modèle répondait de mémoire et déclarait « knowledge ». Insérer un document étayant la réponse ne lui faisait pas déclarer « context ». Ces modifications ont causé zéro inversion dans la tâche factuelle contrôlée. Certains tests sur des passages Wikipédia de DynamicQA donnaient le même profil général, avec de rares exceptions.

Les chercheurs ont ensuite échangé le cache de la question et de la réponse entre des exécutions appariées. Les deux contenaient la même question et produisaient des tokens de réponse identiques. L’une avait vu un document probant et déclaré « context » ; l’autre avait vu un contenu neutre et déclaré « knowledge ». Le receveur conservait son propre document. Seul l’état en cache de sa question et de sa réponse venait du donneur.

Toutes les déclarations admissibles suivaient le donneur dans les quatre modèles. Une exécution avec document non pertinent commençait à affirmer avoir utilisé le contexte après réception de l’état en cache d’une exécution avec preuves pertinentes. Le transfert inverse faisait affirmer à un modèle disposant de preuves qu’il avait utilisé ses connaissances. Les tests DynamicQA donnaient des taux de suivi du donneur de 97,2–100 %.

La chaîne de caractères de la réponse ne peut expliquer le changement, puisqu’elle restait identique. Le document ne le peut pas non plus, puisque le receveur gardait le même. L’intervention isole une information formée pendant le calcul antérieur de la question et de la réponse.

## Une direction qui déplace la déclaration

L’équipe a appelé cette information une trace de source. Le nom décrit son effet sans affirmer que le cache contient une étiquette nette « document » ou « mémoire ». L’état peut représenter les preuves disponibles, l’usage effectif de la source ou un mélange des deux.

Sur les deux plus petits modèles, les chercheurs ont ajusté des directions linéaires à partir des différences entre exécutions avec documents probants et non pertinents. Ils ont appris ces directions avant de poser toute question sur la source, puis les ont appliquées aux valeurs en cache de la question et de la réponse.

L’intervention déplaçait les déclarations dans les deux sens. À intensité fixe, elle en inversait 98,9–100 % dans quatre conditions de document. Des directions aléatoires de même norme en changeaient au plus 1,1 %. Lorsque l’équipe transférait uniquement les composantes ajustées des clés et des valeurs, elle reproduisait 97,9–100 % de l’effet de la transplantation complète du cache. Lorsqu’elle rétablissait les composantes initiales du receveur dans une transplantation autrement complète, les inversions tombaient à 1,1 % pour OLMo et à zéro pour Qwen.

La même direction influençait aussi la source fournissant la réponse lorsqu’elle était appliquée pendant la génération. Elle faisait passer OLMo du contexte à la mémoire dans 71 % des cas admissibles et Qwen dans 51 %. Dans l’autre sens, elle en faisait basculer 85 % et 73 %. L’effet était plus faible et dépendait davantage du prompt que celui sur la déclaration ultérieure, mais il reliait la trace au choix de la source plutôt qu’à une simple étiquette verbale.

## Ce que l’expérience ne montre pas

Les chercheurs fournissent une explication causale pour une tâche contrôlée, pas un certificat général d’introspection. Leurs principaux résultats concernent seulement les exécutions ayant d’abord produit la réponse et la déclaration de source attendues. Ils ont utilisé une seule formulation de la question centrale. Les transplantations de cache couvraient les quatre modèles, tandis que les tests de pilotage et de projection ne couvraient que ceux de 7 et 8 milliards de paramètres.

Les expériences ne tranchent pas non plus si la trace de source enregistre les preuves disponibles ou celles réellement utilisées. Un mécanisme hybride pourrait combiner la trace, le traitement du document et les connaissances paramétriques. Les interventions montrent ce qui peut changer la déclaration ; elles ne donnent pas une interprétation sémantique complète de la direction interne.

Cette retenue compte, car les recherches antérieures ont produit deux résultats pertinents. Felix Binder et ses collègues ont trouvé que les modèles peuvent apprendre certaines informations sur leurs propres états internes. Hannah Rashkin et ses collègues ont développé des mesures permettant de déterminer si la génération de langage est attribuable à des preuves. La nouvelle expérience ne contredit aucune de ces pistes. Elle sépare l’étayage, l’état interne et la déclaration verbale sur soi afin de les tester indépendamment.

L’analyste fictif recommence l’échange. Cette fois, le document dit toujours Paris, la réponse visible dit toujours Paris et le modèle parle toujours avec assurance. Seul un état invisible a été déplacé entre deux exécutions par ailleurs identiques. L’analyste ne traite plus « J’ai utilisé le document » comme un souvenir. C’est une nouvelle sortie du modèle dont il faut vérifier le chemin causal.

## Références


- Afendulev, K., Dontsov, A., Tutubalina, E., Chepurova, A., & Korznikov, A. (2026). *Context or Knowledge: How LLMs Attribute Their Own Answers*. https://arxiv.org/abs/2610.32109
- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking inward: Language models can learn about themselves by introspection*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/0a6059857ae5c82ea9726ee9282a7145-Abstract-Conference.html
- Lanham, T., Chen, A., Radhakrishnan, A., Steiner, B., Denison, C., Hernandez, D., Li, D., Durmus, E., Hubinger, E., Kernion, J., et al. (2023). *Measuring faithfulness in chain-of-thought reasoning*. https://arxiv.org/abs/2307.13702
- Rashkin, H., Nikolaev, V., Lamm, M., Aroyo, L., Collins, M., Das, D., Petrov, S., Tomar, G. S., Turc, I., & Reitter, D. (2023). *Measuring attribution in natural language generation models*. https://aclanthology.org/2023.cl-4.2/
- Turpin, M., Michael, J., Perez, E., & Bowman, S. (2023). *Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting*. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html

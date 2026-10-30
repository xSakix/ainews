+++
title = "Un juge de nouveauté a changé d’avis avec le prompt"
slug = "juge-nouveaute-change-avis-avec-prompt"
description = "Ai2 a testé des modèles de langage qui jugent si des idées de recherche sont nouvelles. La précision d’un modèle est passée de 93,5 à 40,9 % après une petite modification du prompt, révélant la fragilité possible des scores automatisés de nouveauté."
tags = ["research", "models"]
date = 2026-10-28T04:11:25+01:00
draft = false
+++

Une chercheuse en apprentissage automatique arrive au terme d’une longue séance d’évaluation. Deux idées proposées figurent côte à côte sur son écran. Un modèle a désigné la première comme nouvelle. Elle raccourcit l’instruction au-dessus de la même paire, relance le modèle et voit la marque passer à la seconde idée. La chercheuse est inventée. Le renversement ne l’est pas : Ai2 l’a mesuré dans un banc d’essai conçu pour tester les juges automatisés de la nouveauté scientifique.

## Le verdict a changé avant les preuves

L’étude d’Ai2, publiée avec son code et ses données, a testé six modèles de langage comme juges de nouveauté. Les chercheurs ont fait varier le prompt, le budget de raisonnement, la littérature récupérée, le format des idées et la manière de combiner plusieurs appels. Les idées sous-jacentes sont restées identiques.

Le résultat le plus frappant venait de GPT-5.4. Dans un prompt, on indiquait au modèle que les évaluateurs avaient jugé exactement une idée de chaque paire nouvelle, et on lui demandait de l’identifier. Un prompt plus simple lui demandait seulement quelle idée était nouvelle. La précision sur les mêmes paires opposant idées humaines et générées est passée de 93,5 à 40,9 %. Le modèle a changé plus de la moitié de ses verdicts.

La formulation comptait moins pour les paires ne contenant que des idées humaines. La même modification du prompt y déplaçait la précision d’environ sept points de pourcentage. Un juge peut donc sembler stable sur du contenu académique classique et se comporter autrement face aux idées générées qu’on lui demande de plus en plus d’évaluer. Même l’ensemble exclusivement humain n’était pas épargné : Claude Opus 4.6 a varié de 21 points avec le changement de prompt.

Aucun prompt n’améliorait tous les juges. Retirer une mise en garde contre le fait de qualifier de nouveau un travail incrémental aidait certains modèles et en pénalisait d’autres. Lorsque l’équipe comparait des idées de deux générateurs d’IA, modifier le prompt changeait environ un quart à un tiers des verdicts en moyenne sur les six juges. Cette instabilité peut se mesurer sans d’abord décider quel générateur est meilleur.

## Les évaluations sont devenues le benchmark

La nouveauté est difficile à mesurer dans un benchmark, car elle ne se lit pas dans un corrigé. Une idée de recherche n’est nouvelle que par rapport aux travaux antérieurs, et les experts peuvent diverger sur l’importance d’une différence. Ai2 n’a donc pas utilisé l’acceptation des articles comme indicateur indirect. L’équipe a exploré les évaluations par les pairs d’ICLR 2026 pour trouver les passages où les évaluateurs louaient ou contestaient explicitement l’originalité d’une contribution.

Le processus a produit 154 idées humaines fortement nouvelles, tirées d’articles acceptés parmi les 10 % les mieux notés dans leur domaine. Chacune disposait d’éléments positifs de nouveauté dans les évaluations, sans contestation. L’ensemble moins nouveau contenait 145 idées issues d’articles rejetés dans les 10 % les moins bien notés, dont les évaluations soulevaient des problèmes d’originalité sans éléments positifs de nouveauté. Lors d’un contrôle de 50 passages extraits, un annotateur a approuvé la polarité attribuée dans 47 cas. Aucun des trois désaccords n’aurait modifié le classement d’un évaluateur parmi ceux qui louaient ou contestaient la nouveauté.

Cette collection exclusivement humaine teste si un juge peut distinguer des contributions plus ou moins étayées par les évaluations. Une seconde collection traite un usage central de la science automatisée : juger des idées écrites par un modèle. L’équipe a apparié les 154 idées humaines validées avec 154 idées d’un générateur simple. Celui-ci recevait un domaine de recherche et l’instruction de proposer quelque chose de nouveau, sans recherche bibliographique, outils, itération ni retour.

L’étiquette de ces idées générées est délibérément moins solide. Les chercheurs ont supposé que la sortie du générateur simple était moins nouvelle qu’une contribution d’un article très bien noté dont les évaluateurs avaient approuvé l’originalité. Aucun expert n’a jugé toutes les paires. Pour vérifier, un expert en a examiné 30, en privilégiant les exemples manqués par le meilleur juge, et a préféré l’idée humaine à chaque fois. L’équipe a également réécrit les idées humaines et générées dans une structure identique pour réduire le risque que le style trahisse leur origine.

## Plus de moyens n’a pas produit de réponse plus ferme

L’étude a aussi testé une réaction courante à l’incertitude des jugements de modèles : donner au juge davantage de recherche, de raisonnement ou un système conçu pour cette tâche. Aucune de ces approches n’a fourni de remède général.

Un juge agentique GPT-5.6 Sol a reçu un budget de raisonnement très élevé et une recherche itérative en direct limitée à arXiv. Il a atteint un macro-F1 de 0,78 sur la tâche mêlant idées humaines et générées. Une configuration standard de Claude Opus 4.6 avec cinq résumés récupérés a atteint 0,89 et coûté environ dix fois moins par décision aux tarifs API utilisés dans l’étude. La comparaison ne prouve pas que la recherche est inutile. Elle montre que des moyens supplémentaires ne garantissent pas un meilleur jugement de nouveauté.

Les systèmes spécialisés restaient eux aussi derrière une référence plus simple. Un prompt Claude Opus 4.6 à faible niveau de raisonnement, tranché par vote majoritaire sur trois appels, a atteint un macro-F1 de 0,854 pour un coût total d’évaluation de 2,59 dollars. Idea Novelty Checker, qui récupère et reclasse la littérature, a obtenu 0,642 pour 30,66 dollars. L’évaluateur de nouveauté d’AI Scientist de Sakana AI, qui interroge Semantic Scholar de façon itérative, a obtenu 0,772 pour 82,05 dollars. Ces trois chiffres viennent de l’implémentation et des hypothèses de prix d’Ai2 : ils comparent donc les configurations testées, pas tous les usages possibles de ces systèmes.

Les systèmes antérieurs expliquent pourquoi les chercheurs choisissent ces architectures. Scideator aide les scientifiques à recombiner des facettes d’articles en nouvelles propositions et utilise la recherche bibliographique pour évaluer les recoupements. Idea Novelty Checker resserre une recherche bibliographique large avec des filtres d’embeddings et un reclassement par facettes. AI Scientist traite la vérification de nouveauté comme une étape d’une boucle de recherche automatisée plus vaste. Tous ancrent leur jugement dans les travaux antérieurs plutôt que de se fier uniquement à la mémoire du modèle.

Le résultat d’Ai2 déplace la charge de la preuve. Un score élevé obtenu avec un juge, un prompt et un réglage de raisonnement dit peu sur la résistance du verdict à une autre configuration raisonnable. Les auteurs recommandent de tester les juges sur les types d’idées générées qu’ils verront réellement, de mesurer leur sensibilité aux prompts et aux modèles et de mettre à jour les benchmarks au fil de la littérature.

## Un score a besoin de sa propre évaluation

La chercheuse imaginaire ne choisit pas le verdict qu’elle préfère. Elle conserve les deux sorties, enregistre les deux prompts et lit elle-même les articles associés. Le modèle peut encore l’aider à trier une pile croissante de propositions, mais son chiffre devient un élément de preuve plutôt que le contrôle final.

La marque s’est déplacée entre deux idées, mais le changement le plus important concernait la confiance qu’on lui accordait. Lorsque quelques mots peuvent modifier la réponse, le jugement a autant besoin d’être évalué que l’idée de recherche.

## Références

- Ai2. (2026). *Can we trust LLMs to judge whether a research idea is novel?* https://allenai.org/blog/novelty-bench
- Lu, C., Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*. https://arxiv.org/abs/2408.06292
- Radensky, M., Shahid, S., Fok, R., Siangliulue, P., Hope, T., & Weld, D. S. (2024). *Scideator: Human-LLM Scientific Idea Generation Grounded in Research-Paper Facet Recombination*. https://arxiv.org/abs/2409.14634
- Shahid, S., Radensky, M., Fok, R., Siangliulue, P., Weld, D. S., & Hope, T. (2025). *Literature-Grounded Novelty Assessment of Scientific Ideas*. https://arxiv.org/abs/2506.22026
- Sternlicht, N., Shahid, S., Jansen, P., Weld, D. S., Siangliulue, P., & Hope, T. (2026). *Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation*. https://arxiv.org/abs/2610.02022

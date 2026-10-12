+++
title = "V-JEPA 2 de Meta oublie une balle cachée en une demi-seconde"
slug = "v-jepa-2-meta-oublie-balle-cachee-demi-seconde"
description = "Des chercheurs de la Technical University of Munich ont soumis le modèle vidéo de Meta à un test de psychologues pour nourrissons. Dans des scènes rendues, la partie qui voit sait qu'une balle reste dans une boîte fermée, tandis que celle qui complète l'invisible la perd. Un bref entraînement corrige cela, mais un benchmark progresse autant avec un entraînement qui ne l'enseigne jamais."
tags = ["research", "models"]
date = 2026-10-12T10:17:01+02:00
draft = false
+++

Imaginons un magicien de rue sur une place froide de Munich. Il montre une pièce à un garçon d'environ quatre ans, ferme son poing dessus, souffle sur ses articulations et ouvre la main. La paume est vide. Le garçon pousse un cri. Il était certain que la pièce était encore là, et cette certitude constitue tout le tour. Un magicien ne peut tromper que quelqu'un qui croit que les choses continuent d'exister lorsque personne ne peut les voir.

Peng Xie et Amr Alanwar, deux chercheurs de la Technical University of Munich, ont commencé leur étude par des tours de ce genre. Ils ont pris des tours filmés dont les moments de surprise avaient été évalués par des spectateurs humains et les ont montrés à V-JEPA 2, un modèle vidéo publié par Meta en 2025 après entraînement sur plus d'un million d'heures de vidéos Internet. Le modèle n'était jamais surpris. Sur trois collections de tours et six façons de mesurer, son erreur de prédiction, équivalent de la surprise pour le modèle, montait et descendait avec la quantité de mouvement à l'écran, jamais avec les moments marqués par les personnes. Leur prépublication, déposée sur arXiv le 5 octobre, construit plutôt un instrument pour regarder à l'intérieur du modèle.

## Deux moitiés en désaccord

V-JEPA 2 comporte deux moitiés. Un encodeur transforme la vidéo en description abstraite de son contenu. Un prédicteur, auquel on montre un clip dont des morceaux ont été retirés, devine la description des morceaux manquants. La conception suit une approche proposée par Yann LeCun en 2022 : une machine doit construire un modèle du fonctionnement du monde en prédisant ce qu'elle ne voit pas, dans des descriptions abstraites plutôt qu'en pixels. Meta a utilisé V-JEPA 2 pour planifier les mouvements de bras robotiques.

Xie et Alanwar ont trouvé un désaccord entre ces moitiés au sujet d'un objet caché : l'encodeur le conserve, et le prédicteur, la partie censée compléter ce que le modèle ne voit pas, le perd en une fraction de seconde. « Un modèle du monde qui planifie doit conserver l'état de ce qui n'est plus visible », écrivent les auteurs. « Une main refermée sur une pièce la tient toujours. »

## Ce qu'attend un nourrisson de cinq mois

Les psychologues débattent de cette attente depuis près d'un siècle. Jean Piaget, observant ses trois enfants, a constaté qu'un bébé ne commence à chercher un jouet caché derrière un écran qu'entre huit et dix mois. Dans les premiers mois, écrivait-il, un objet est « une simple image qui retourne au néant dès qu'elle disparaît ».

En 1985, Renée Baillargeon, Elizabeth Spelke et Stanley Wasserman l'ont contesté avec un écran en bois et une boîte jaune décorée de petites étoiles rouges. L'écran était à plat, puis pivotait comme un pont-levis et cachait la boîte. Dans une version, il s'arrêtait à l'emplacement de la boîte. Dans l'autre, il poursuivait sa rotation, un demi-cercle complet, comme à travers la boîte. Les bébés de cinq mois regardaient plus longtemps la seconde version, comme on regarde quelque chose qui ne devrait pas arriver, et les chercheurs ont conclu que des nourrissons aussi jeunes comprennent que les objets continuent d'exister lorsqu'ils sont cachés. D'autres chercheurs ont reproduit le pont-levis et soutenu que les bébés, qui avaient regardé le demi-tour complet à répétition avant le test, répondaient à la familiarité de chaque mouvement, ou simplement à davantage de mouvement. Ce débat reste ouvert.

Les chercheurs en apprentissage automatique ont malgré tout emprunté la méthode. Le benchmark IntPhys associe des vidéos d'événements possibles et impossibles et juge le modèle correct lorsqu'il trouve l'impossible moins plausible ; pour un modèle comme V-JEPA, cela signifie une erreur de prédiction plus élevée. En février 2025, une équipe Meta rapportait que le premier V-JEPA, entraîné uniquement sur des vidéos naturelles, montre « une compréhension de diverses propriétés de physique intuitive, comme la permanence de l'objet », et soutenait que ces connaissances n'ont pas besoin d'être intégrées d'avance. Dans une annexe, la même équipe admettait un doute : une balle montrée au début d'un clip puis cachée pouvait laisser le modèle en difficulté « pour prédire que la balle rouge est à nouveau visible ». Elle ne l'a pas testé.

## Une balle, une bande et deux mondes

L'article munichois le fait. Les chercheurs ont rendu des scènes simples d'une balle roulant sur un fond texturé. À un instant fixé, ils ont retiré de ce que voit le modèle la bande de l'image suivant le trajet de la balle. Ils ont construit deux versions de chaque scène, identiques partout sauf dans cette bande. Dans l'une, la balle continue ; dans l'autre, elle a disparu. Le prédicteur complète la bande, et les chercheurs demandent à quel monde sa supposition ressemble, une réponse pour chaque intervalle d'environ un quart de seconde, avec soixante scènes derrière chaque réponse. Un tirage à pile ou face obtiendrait la moitié.

À l'instant de la dissimulation, la version de V-JEPA 2 étudiée le plus étroitement choisissait la balle dans 92 % des scènes. Un intervalle plus tard, dans aucune. Les versions plus petite et plus grande se comportaient de la même manière : l'échelle n'apportait rien. Ce n'est que lorsque la majeure partie du reste de l'image était aussi masquée, comme pendant l'entraînement, que la version intermédiaire conservait la balle, environ une seconde ; les deux autres la perdaient encore. Une balle arrêtée avant d'être cachée faisait un peu mieux : les modèles la conservaient en moyenne dans 13 à 41 % des scènes, tandis qu'un programme simple copiant la dernière image vue la conserve presque toujours.

L'information n'avait pas disparu. Un programme simple entraîné à lire la description de l'encodeur disait chaque fois si la balle était présente et lisait le contenu d'une boîte fermée pendant les trois secondes et demie suivant sa fermeture. Appliqué à la sortie du prédicteur, le même programme trouvait la balle dans deux pour cent des scènes après une demi-seconde de fermeture, puis dans aucune. « Le déficit n'est pas perceptif », écrivent les auteurs à propos de leurs scènes rendues. Quand une vraie main se refermait sur une pièce, ont-ils trouvé, l'encodeur la perdait aussi. D'autres types de modèles vidéo ne faisaient pas mieux avec une boîte mobile. Cosmos de NVIDIA, dans sa version prédisant la vidéo morceau par morceau, conservait une balle dans une boîte immobile plus de deux secondes, mais perdait celle portée dans une boîte en mouvement. VideoMAE, qui reconstruit les pixels manquants, ne conservait presque rien.

## Un bref entraînement et ses limites

Cette façon d'apprendre peut combler l'écart. Lorsque les chercheurs ont entraîné seulement le prédicteur pendant trois mille étapes sur des scènes de balles entrant dans des boîtes, moins d'une heure de calcul sur une puce graphique de centre de données, sa croyance qu'une balle transportée était toujours dedans passait de presque jamais à toujours, tandis que deux conditions témoins restaient à zéro. Poursuivre l'entraînement de tout le modèle avec le propre schéma de morceaux retirés de V-JEPA, sur des images à la première personne de mains au travail et de bras robotiques, ou sur des clips Internet, lui donnait plus d'une seconde de mémoire pour une balle roulante.

Les auteurs détaillent les défauts du correctif. Les scènes d'entraînement venaient du même moteur de rendu que le test : un score parfait y était attendu ; sur des fonds vidéo naturels, le modèle entraîné choisissait la balle dans 85 à 97 % des scènes. Ce qu'il apprenait était une hypothèse tenace : même quand la fin du clip montrait la disparition de la balle, il continuait à la prédire dans la zone manquante. Le coût de cet entraînement pour le modèle ailleurs n'a pas été mesuré.

## Le benchmark qui ne distinguait pas les cas

L'entraînement sur les boîtes faisait aussi passer le score IntPhys du modèle de 84,2 à 93,3 %, ce qui semblait trancher. Puis les chercheurs ont effectué le même entraînement sans jamais demander au modèle ce qui était dans une boîte, et le score a autant augmenté. L'entraînement sur des scènes immobiles faisait aussi bien. Un modèle auquel ils avaient appris, sur des clips de vraies mains avec une pièce placée numériquement dans la paume, à dire si elle était restée ou avait été retirée obtenait 27 et 31 % sur IntPhys dans deux exécutions, moins que le hasard. « Un gain sur le benchmark n'est donc pas en lui-même une preuve de permanence », concluent les auteurs.

Leurs propres éléments ont des limites, listées dans une annexe consacrée à ce qui modifierait leurs conclusions. Ils ont sondé le prédicteur préentraîné de V-JEPA 2, pas la version conditionnée par l'action qui pilote les robots. Chaque lecture de la croyance du modèle vient de scènes dessinées par un programme, soixante à la fois, et le résultat des vraies mains repose sur une douzaine de clips sur lesquels il n'avait pas été entraîné. Le code sera publié, indiquent-ils ; l'article n'a pas été évalué par les pairs. Il comporte aussi une déclaration détaillée : un assistant IA a aidé à concevoir les expériences, écrire le code et rédiger le texte, et les auteurs listent les erreurs de son code qu'ils ont détectées et corrigées avant de rapporter leurs chiffres, dont une exécution entraînée sur des clips vides.

## Retour sur la place

Sur cette place imaginaire, le garçon demande à revoir le tour. Cette fois il regarde le poing, pas le visage, car il est sûr que la pièce est quelque part dedans. Cette certitude permet de le tromper, et lui permettra un jour de démasquer le magicien. Un modèle qui oublie la pièce ne peut faire ni l'un ni l'autre. Sur des scènes rendues, trois mille étapes d'entraînement ont donné à V-JEPA 2 la certitude du garçon. Savoir si elle tient sur des images réelles, lorsqu'une tasse recouvre quelque chose qu'un robot doit trouver, est un test que les auteurs disent ne pas avoir encore effectué.

## Références

- Assran, M., Bardes, A., Fan, D., Garrido, Q., Howes, R., Komeili, M., et al. (2025). *V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning*. https://arxiv.org/abs/2506.09985
- Baillargeon, R., Spelke, E. S., & Wasserman, S. (1985). *Object permanence in five-month-old infants*. https://doi.org/10.1016/0010-0277(85)90008-3
- Bardes, A., Garrido, Q., Ponce, J., Chen, X., Rabbat, M., LeCun, Y., et al. (2024). *Revisiting Feature Prediction for Learning Visual Representations from Video*. https://arxiv.org/abs/2404.08471
- Bogartz, R. S., Shinskey, J. L., & Schilling, T. H. (2000). *Object permanence in five-and-a-half-month-old infants?* https://doi.org/10.1207/S15327078IN0104_3
- Garrido, Q., Ballas, N., Assran, M., Bardes, A., Najman, L., Rabbat, M., et al. (2025). *Intuitive physics understanding emerges from self-supervised pretraining on natural videos*. https://arxiv.org/abs/2502.11831
- LeCun, Y. (2022). *A Path Towards Autonomous Machine Intelligence*. https://openreview.net/forum?id=BZ5a1r-kVsf
- Margoni, F., Surian, L., & Baillargeon, R. (2024). *The violation-of-expectation paradigm: A conceptual overview*. https://doi.org/10.1037/rev0000450
- NVIDIA, Agarwal, N., Ali, A., Bala, M., Balaji, Y., Barker, E., et al. (2025). *Cosmos World Foundation Model Platform for Physical AI*. https://arxiv.org/abs/2501.03575
- Piaget, J. (1954). *The Construction of Reality in the Child* (M. Cook, Trans.; original work published 1937). https://doi.org/10.1037/11168-000
- Riochet, R., Ynocente Castro, M., Bernard, M., Lerer, A., Fergus, R., Izard, V., et al. (2022). *IntPhys 2019: A Benchmark for Visual Intuitive Physics Understanding*. https://doi.org/10.1109/TPAMI.2021.3083839
- Rivera, S. M., Wakeley, A., & Langer, J. (1999). *The drawbridge phenomenon: Representational reasoning or perceptual preference?* https://doi.org/10.1037/0012-1649.35.2.427
- Tong, Z., Song, Y., Wang, J., & Wang, L. (2022). *VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training*. https://arxiv.org/abs/2203.12602
- Xie, P., & Alanwar, A. (2026). *Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object*. https://arxiv.org/abs/2610.07355

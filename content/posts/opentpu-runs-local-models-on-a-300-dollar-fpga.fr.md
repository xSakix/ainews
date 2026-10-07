+++
title = "OpenTPU exécute des modèles locaux sur un FPGA à 300 dollars"
slug = "opentpu-execute-modeles-locaux-fpga-300-dollars"
description = "Le projet sous licence Apache publie son accélérateur, son compilateur, son simulateur et ses outils hôtes. Le débit mesuré révèle un petit système limité par la mémoire plutôt qu'un remplaçant du GPU."
tags = ["hardware", "projects", "models"]
date = 2026-10-07T03:58:57+02:00
draft = false
+++

OpenTPU a publié une pile complète d'accélération d'IA qui exécute des modèles de langage modernes sur une carte FPGA Kintex-7 d'environ 300 dollars.

Le dépôt Apache-2.0 comprend du matériel SystemVerilog, un jeu d'instructions, un simulateur exact au bit près, un langage de noyaux et son compilateur, des outils de profilage et du logiciel hôte. Sa valeur tient à la possibilité de l'inspecter : la même petite base de code va des noyaux de modèles en Python aux signaux d'une carte PCIe physique.

## Pourquoi c'est important {#why-it-matters}

Un développeur qui découvre le matériel d'inférence peut suivre chaque cycle et transfert mémoire sans avoir besoin d'un accélérateur de centre de données. La machine obtenue est lente face aux GPU actuels, mais ses contraintes rendent le goulot d'étranglement particulièrement visible.

OpenTPU annonce 30,7 tokens générés par seconde pour Qwen3-0.6B en quatre bits et 82,1 pour LFM2.5-230M, surcoût de l'hôte compris. Les modèles denses plus grands ralentissent à 12,03 tokens par seconde pour Qwen3.5-2B et 3,75 pour Gemma 4 E4B dans les configurations indiquées.

Lors du décodage, la carte atteint 82 % à 94 % du débit maximal de 17,1 Go/s de ses deux canaux DDR3. La bande passante mémoire, plutôt que le calcul matriciel, devient ainsi la ressource limitante. Une unité systolique à quatre colonnes aide davantage le traitement des prompts que la génération token par token.

Les modèles qui dépassent les 4 Gio de la carte peuvent charger en continu des poids de mélange d'experts depuis le stockage hôte. Le dépôt rapporte 10,6 tokens par seconde pour LFM2.5-8B-A1B et 3,95 pour Qwen3.5-35B-A3B, ce dernier transférant 153 Mo par token sur PCIe. Ces mesures sont celles du projet, mais les scripts, les versions datées et les conditions de mesure sont publics.

La formule « développé par l'IA » appelle à la prudence. Selon le projet, un workflow d'agents dirigé par des humains a produit une grande partie de la conception et de l'optimisation, sans démontrer qu'un système autonome a décidé de créer son propre matériel. Le résultat concret est la pile publiée et l'accord bit pour bit annoncé entre la carte et le simulateur.

Les prochains tests sont simples à définir : reproduire les bitstreams publiés sur la même carte, comparer consommation et latence avec des GPU peu coûteux, et voir si des contributeurs externes peuvent modifier l'architecture sans rompre l'équivalence avec le simulateur.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| OpenTPU publie matériel, ISA, simulateur, compilateur et outils hôtes sous Apache-2.0 | VÉRIFIÉ | [Dépôt OpenTPU](https://github.com/FeSens/openTPU) | les fichiers et la licence sont accessibles |
| Qwen3-0.6B atteint 30,7 tokens/s en temps réel et LFM2.5-230M atteint 82,1 dans des configurations à quatre bits | SELON LA SOCIÉTÉ | [Mesures OpenTPU](https://github.com/FeSens/openTPU) | aucune |
| Le décodage utilise 82 % à 94 % d'un maximum DDR3 de 17,1 Go/s | SELON LA SOCIÉTÉ | [Mesures OpenTPU](https://github.com/FeSens/openTPU) | aucune |
| Qwen3.5-35B-A3B atteint 3,95 tokens/s en transférant 153 Mo par token | SELON LA SOCIÉTÉ | [Mesures OpenTPU](https://github.com/FeSens/openTPU) | aucune |
| La carte reproduit les tokens du simulateur bit pour bit | SELON LA SOCIÉTÉ | [Dépôt OpenTPU](https://github.com/FeSens/openTPU) | des tests publics existent ; aucune reproduction matérielle indépendante trouvée |
| « Développé par l'IA » ne démontre pas un développement matériel autonome | ANALYSE | [Dépôt OpenTPU](https://github.com/FeSens/openTPU) | distinction tirée du workflow documenté dirigé par des humains |

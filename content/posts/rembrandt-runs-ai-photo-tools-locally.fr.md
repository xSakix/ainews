+++
title = "Rembrandt exécute ses outils photo d'IA en local"
slug = "rembrandt-execute-ses-outils-photo-ia-en-local"
description = "Cet éditeur de bureau sous GPL réunit développement RAW, masques, débruitage et super-résolution sans exiger de compte ni de téléversement des photographies."
tags = ["projects", "tools"]
date = 2026-10-09T04:00:06+02:00
draft = false
+++

Rembrandt, nouvel éditeur photo open source pour macOS, Windows et Linux, exécute ses outils de débruitage, d'agrandissement et de masquage assistés par IA sur l'appareil de l'utilisateur.

L'application sous licence GPL est un logiciel de développement RAW non destructif et une photothèque, plutôt qu'un programme de peinture pixel par pixel. Elle stocke les retouches dans des fichiers annexes XMP standard, laisse les photographies originales intactes et n'exige aucun compte pour ses fonctions locales gratuites.

**Pourquoi c'est important :** Les photographes peuvent utiliser des outils de retouche computationnelle sans téléverser d'images privées ni confier leur catalogue à un service par abonnement. Le code source et le format courant des fichiers annexes offrent aussi une porte de sortie si l'application disparaît.

Rembrandt comprend des masques de sujet, d'arrière-plan, d'objet et de profondeur, un débruitage sur GPU, une super-résolution 2× et 4×, une restauration de la mise au point, la fusion HDR et panoramique, des corrections optiques et la retouche par lots. Une commande textuelle comme « plus chaud et un peu plus lumineux » déplace les mêmes réglages visibles qu'une retouche manuelle ; selon le projet, cette fonction utilise un vocabulaire local plutôt qu'un modèle de langage.

Le moteur de retouche est écrit en JavaScript, avec des shaders WebGL2 et WebGPU dans une petite enveloppe de bureau en Rust. LibRaw prend en charge les fichiers des appareils photo, tandis que des projets ouverts nommément cités fournissent des composants pour l'agrandissement, le débruitage, les profils d'objectifs et les masques visuels. Le projet annonce la prise en charge des fichiers RAW de plus de 1 000 appareils photo.

Des exécutables de bureau sont disponibles pour les Mac Apple silicon et Intel, les systèmes Windows x64 et Arm, et Linux x86-64 ou Arm. Ils ne sont pas encore signés, ce qui oblige les utilisateurs de macOS et Windows à passer outre les avertissements du système au premier lancement. Il est aussi possible d'héberger l'application sur un ordinateur Linux ou macOS et de retoucher les images dans un navigateur sur son propre réseau.

Le dépôt compare Rembrandt à Lightroom et darktable, mais ses affirmations de qualité n'ont pas été testées indépendamment. Il recense aussi des fonctions manquantes, dont la prise de vue connectée, la reconnaissance faciale, l'impression et un écosystème de modules complémentaires. La synchronisation cloud facultative est payante et nécessite un compte ; l'éditeur local n'en demande pas.

La version actuelle, les instructions de compilation et les sommes de contrôle figurent dans le [dépôt Rembrandt](https://github.com/thesnarkitecht/rembrandt). Son prochain test décisif sera une utilisation prolongée sur des catalogues RAW variés, où la gestion des couleurs, la compatibilité des appareils et la fiabilité de l'export comptent davantage qu'une liste de fonctions.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
|---|---|---|---|
| Rembrandt est disponible pour macOS, Windows et Linux sous GPL-3.0-or-later | VÉRIFIÉ | [Dépôt](https://github.com/thesnarkitecht/rembrandt) | aucune |
| Les fonctions locales n'exigent aucun compte et les photographies n'ont pas à être téléversées | VÉRIFIÉ | [Dépôt](https://github.com/thesnarkitecht/rembrandt) | aucune |
| Les retouches utilisent des fichiers annexes XMP et les originaux restent intacts | VÉRIFIÉ | [Dépôt](https://github.com/thesnarkitecht/rembrandt) | aucune |
| L'application comprend du débruitage local, de la super-résolution et des masques assistés par IA | VÉRIFIÉ | [Dépôt](https://github.com/thesnarkitecht/rembrandt) | aucune |
| Le moteur utilise JavaScript, WebGL2/WebGPU et une enveloppe de bureau en Rust | VÉRIFIÉ | [Dépôt](https://github.com/thesnarkitecht/rembrandt) | aucune |
| Le projet annonce la prise en charge des fichiers RAW de plus de 1 000 appareils photo | SELON LA SOCIÉTÉ | [Dépôt](https://github.com/thesnarkitecht/rembrandt) | aucune |
| Les exécutables de bureau actuels ne sont pas signés | VÉRIFIÉ | [Dépôt](https://github.com/thesnarkitecht/rembrandt) | aucune |
| La synchronisation cloud facultative est la seule fonction payante et nécessite un compte | VÉRIFIÉ | [Dépôt](https://github.com/thesnarkitecht/rembrandt) | aucune |

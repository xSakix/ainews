+++
title = "Un test placebo : la plupart des skills n'apportent rien"
slug = "test-placebo-la-plupart-des-skills-n-apportent-rien"
description = "Une expérience préenregistrée compare neuf skills Claude Code à des instructions neutres aussi longues. Deux coûtent moins que le placebo, une fait moins bien et six sont statistiquement indiscernables."
tags = ["research", "agents", "tools"]
date = 2026-10-07T03:57:57+02:00
draft = false
+++

La plupart des skills populaires pour agents de programmation n'ont pas fait mieux que des instructions neutres de même longueur dans une nouvelle expérience contrôlée par placebo.

Le projet skill-placebo a testé neuf skills Claude Code sur 15 tâches publiques issues de SWE-bench Verified, Terminal-Bench 2.1 et OpenThoughts-TBLite. Chaque skill était comparée à un texte neutre de même longueur en tokens, installé par le même mécanisme.

## Pourquoi c'est important {#why-it-matters}

Un développeur qui ajoute un long fichier d'instructions peut observer un changement de comportement de l'agent et l'attribuer à la procédure contenue dans le fichier. Cette expérience demande si l'ingrédient utile est vraiment la skill, ou simplement le contexte supplémentaire, l'amorçage et la variabilité d'exécution qui l'accompagnent.

La méthode a été enregistrée avant la première exécution. Claude Opus 5.5 a réalisé 30 essais par groupe, produisant 450 essais enregistrés. Le coût était le critère principal ; le taux de réussite des tâches était aussi suivi, avec une correction statistique pour les neuf comparaisons.

Deux skills coûtaient moins que leurs placebos : ponytail de 12 % et agent-skills de 5 %. Planning-with-files réussissait 80 % de ses essais, contre les 30 essais pour son placebo, ce qui la rendait moins bonne selon la règle de décision préenregistrée du projet. Les six autres étaient statistiquement indiscernables de leurs textes neutres correspondants.

Aucune des neuf n'était mesurablement moins coûteuse qu'une exécution sans skill. Le texte placebo neutre seul modifiait le coût de 2 % à 16 % par rapport à la référence sans skill. La longueur du prompt et un contexte apparemment sans rapport deviennent ainsi une partie du traitement, plutôt qu'un arrière-plan inoffensif.

## Le contrôle améliore la question, pas la taille de l'échantillon

Une référence sans skill demande si l'ensemble du dispositif change les performances. Le placebo apparié pose une question plus précise : les véritables instructions apportent-elles quelque chose au-delà d'une quantité égale de texte fournie de la même manière ? Les deux comparaisons peuvent diverger sans se contredire.

Le dépôt expose la méthode préenregistrée, les résultats de chaque essai et les journaux des agents. Il consigne aussi une modification du 6 octobre : deux dépassements de délai dont les tests avaient ensuite réussi ont été comptés comme des échecs, conformément aux règles initiales. Cela a fait passer planning-with-files de « pas mieux » à « moins bien » sans changer les coûts.

Les limites sont importantes. Quinze tâches et 30 essais par groupe laissent des intervalles larges pour le taux de réussite ; l'expérience couvre un seul modèle principal et une seule infrastructure d'agent, et les skills choisies privilégient les workflows de programmation généraux plutôt que les connaissances de référence spécialisées. Les journaux actuels n'établissent pas non plus avec quelle régularité chaque skill était invoquée pendant une exécution.

Un petit pilote Codex n'a testé que trois skills sur cinq tâches et reste explicitement secondaire. Ses résultats ne doivent pas être mélangés à l'expérience Claude ni traités comme une comparaison de familles de modèles.

La conclusion ne démontre pas que les skills de programmation sont inutiles. Elle montre que popularité, longueur et procédure plausible remplacent mal un contrôle apparié. La contribution réutilisable est le protocole expérimental : figer la méthode, donner autant de contexte au contrôle, conserver les journaux complets et mesurer le coût avec la réussite.

Les prochaines versions peuvent renforcer le résultat en ajoutant des tâches, d'autres infrastructures d'agents et un contrôle aux instructions mélangées qui sépare le contenu de la procédure de l'amorçage général.

## Vérification {#verification}

| Affirmation | Label | Source primaire | Vérification indépendante |
| --- | --- | --- | --- |
| L'expérience principale a réalisé 450 essais sur neuf skills et 15 tâches publiques | VÉRIFIÉ | [Dépôt skill-placebo](https://github.com/simonether/skill-placebo) | méthode, résultats et journaux sont publics |
| Deux skills battent le placebo sur le coût, une fait moins bien et six ne font pas mieux | SELON LA SOCIÉTÉ | [Résultats skill-placebo](https://github.com/simonether/skill-placebo) | aucune ; analyse statistique de l'auteur |
| Ponytail coûte 12 % de moins et agent-skills 5 % de moins que le placebo apparié | SELON LA SOCIÉTÉ | [Résultats skill-placebo](https://github.com/simonether/skill-placebo) | aucune |
| Planning-with-files réussit 80 % des essais contre 100 % pour le placebo | SELON LA SOCIÉTÉ | [Résultats skill-placebo](https://github.com/simonether/skill-placebo) | les données par essai sont disponibles |
| Aucune des neuf skills n'est mesurablement moins coûteuse que l'absence de skill | SELON LA SOCIÉTÉ | [Résultats skill-placebo](https://github.com/simonether/skill-placebo) | aucune |
| Les contrôles appariés isolent mieux le contenu des instructions qu'une référence sans skill | ANALYSE | [méthode enregistrée](https://github.com/simonether/skill-placebo/blob/main/METHOD.md) | déduction tirée de la conception expérimentale |

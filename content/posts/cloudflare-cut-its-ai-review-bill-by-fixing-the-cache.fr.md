+++
title = "Cloudflare réduit sa facture de revue IA en corrigeant le cache"
slug = "cloudflare-reduit-facture-revue-ia-en-corrigeant-cache"
description = "Le réviseur de code par IA de Cloudflare devenait plus cher à mesure que ses modèles progressaient. L'entreprise a réduit le coût moyen de 68 % et la latence médiane de près des deux tiers, puis a dû prouver que le réviseur moins cher n'avait pas simplement cessé de trouver des problèmes."
tags = ["agents", "tools", "business"]
date = 2026-10-20T04:05:28+02:00
draft = false
+++

Une ingénieure n'existe que pour ce paragraphe. Sa demande de fusion contient une petite modification d'un service utilisé dans le monde entier. Elle la pousse à 16 h 12. Sept réviseurs automatiques s'activent, lisent les mêmes instructions, inspectent des parties communes du dépôt et font passer près de trois millions de tokens dans les modèles avant qu'un coordinateur décide quoi lui dire. La revue arrive quatre minutes plus tard. Elle coûte plus du double de ce que coûtait le même système au printemps.

## La facture a augmenté sans refonte

Cloudflare a construit ce type de système pour ses propres ingénieurs. Ryan Skidmore, ingénieur systèmes dans l'entreprise, a décrit l'architecture initiale en avril 2026 : jusqu'à sept agents spécialisés examinaient la sécurité, les performances, la qualité du code, la documentation, les versions et les normes internes, tandis qu'un coordinateur dédupliquait leurs constats et décidait d'approuver ou non une demande de fusion. Pendant son premier mois, selon Cloudflare, le système a réalisé 131 246 revues sur 48 095 demandes de fusion dans 5 169 dépôts. La revue moyenne coûtait 1,19 dollar.

Fin août, la moyenne atteignait environ 2,46 dollars. Cloudflare n'avait pas remplacé le système par un dispositif plus élaboré. Le coordinateur déléguait toujours aux spécialistes et les mêmes niveaux de risque déterminaient si une modification recevait une revue légère ou complète. L'entreprise avait changé les modèles et laissé les conversations s'allonger.

Les coûts montaient régulièrement : 1,22 dollar par revue en mars, 1,44 dollar en juin, 1,74 dollar en juillet et 2,32 dollars en août, après correction de la répartition des niveaux de revue. Davantage de modifications entraient dans le niveau coûteux, mais Cloudflare attribue l'essentiel de la hausse aux choix de modèles. Le passage de tous les réviseurs aux modèles Anthropic a fait monter une tâche de 1,38 à 2,03 dollars. Un réviseur des normes internes est passé d'environ 25 à 88 cents par exécution.

Les modèles travaillaient aussi davantage. Le nombre de tokens par revue a plus que triplé, de 0,91 million à 2,99 millions, alors même que le taux global de succès du cache progressait de 85,7 à 97 %. Un pourcentage élevé masquait un dénominateur plus grand.

## Le préfixe coûteux

Juste avant l'optimisation, les tokens de sortie représentaient environ 23 % des dépenses de revue. Les écritures en cache en absorbaient 43 % et les lectures 34 % supplémentaires. La plupart de l'argent allait à un contexte déjà vu ou sur le point de l'être à nouveau.

Le cache de prompts d'Anthropic réutilise les contenus identiques au début d'une requête. Ses tarifs publiés rendent l'arbitrage clair : écrire dans un cache de cinq minutes coûte 1,25 fois le tarif d'entrée normal, tandis qu'une lecture coûte un dixième. La réutilisation ne rapporte que si les requêtes suivantes commencent par le même préfixe avant l'expiration de l'entrée.

Les réviseurs de Cloudflare semblaient idéaux pour ce fonctionnement. Leurs définitions d'outils et instructions d'agents apportaient de 11 000 à 21 000 tokens identiques entre dépôts. Pourtant, la première requête d'une session ne trouvait un préfixe en cache que dans 14 à 26 % des cas.

L'ordre était mauvais. OpenCode v1 plaçait un bloc d'environnement propre au dépôt, comprenant le répertoire de travail et la date, dans le même bloc système que les instructions partagées. Le point de rupture du cache se trouvait après les deux. Une session dans un dépôt ne pouvait pas réutiliser le préfixe écrit par une autre, car des détails variables précédaient ce point.

Cloudflare a scindé le contenu système à un marqueur et placé les éléments communs en premier. La réutilisation dès la première requête est passée entre 91 et 99,5 % après ce changement. Les trois principaux réviseurs démarraient aussi ensemble, avant que l'un puisse finir d'écrire le préfixe commun. L'équipe a fait attendre les deuxième et troisième jusqu'à 20 secondes que la première réponse commence, échangeant un léger retard contre environ neuf cents d'économie par réviseur.

Cette modification technique a produit la plus forte réduction individuelle. Elle représentait toutefois moins de la moitié de l'économie totale.

## Des modèles qui s'arrêtent plus tôt

Cloudflare a aussi testé les modèles et les niveaux de raisonnement, sans supposer que la combinaison la plus chère était la plus sûre. Les modifications du code représentaient 65 cents sur la réduction de 1,67 dollar mesurée dans l'article ; les changements de modèle et de niveau de raisonnement, 1,06 dollar. Skidmore précise que ces comparaisons successives n'étaient pas une expérience contrôlée.

Les modèles plus récents utilisaient moins d'appels. Dans un test comparatif de deux jours et demi, Sonnet 5.5 coûtait 62 % de moins que Sonnet 5 par revue de qualité du code, 58 % de moins pour les performances et 47 % de moins pour la sécurité, malgré un prix identique par token. Au niveau moyen de raisonnement, l'agent de qualité du code faisait 1,7 appel au modèle au lieu de 6,2. Plus de la moitié de ses exécutions s'achevaient après un appel sans ouvrir d'autre fichier du dépôt.

Cela semblait efficace et dangereux. Un réviseur qui lit moins peut terminer à bas prix parce qu'il manque le bogue.

Cloudflare a comparé les niveaux élevé et moyen. Le niveau élevé coûtait 61 % de plus par revue de qualité du code et produisait 58 % de constats critiques ou d'avertissement supplémentaires. L'écart était d'environ deux cents par revue. L'équipe a rétabli le niveau élevé pour cet agent, en gardant les autres spécialistes au niveau moyen dans l'attente d'autres tests.

Moins d'appels raccourcissait l'attente. La revue médiane est passée de quatre minutes et neuf secondes à une minute et 32 secondes. Le 99e percentile est descendu de 15 minutes et 20 secondes à quatre minutes et 41 secondes. Les revues de plus de cinq minutes sont passées de 37,9 à 0,7 %.

## Tester ce qui a disparu

Le nombre brut de constats graves a baissé après les changements. La qualité du code produisait 40 % de constats critiques et d'avertissements en moins ; la sécurité reculait de 56 % et les performances de 71 %. Cloudflare a cherché à distinguer le bruit éliminé des problèmes manqués.

L'entreprise a d'abord vérifié si les ingénieurs modifiaient les lignes signalées lors de leur envoi suivant. Avant l'optimisation, les auteurs donnaient suite à 34 % des constats sérieux sur la qualité du code. Ensuite, à 59 %. Les constats étaient moins fréquents mais entraînaient plus souvent une modification : 132 constats suivis d'action pour 1 000 revues après les changements, contre 145 avant, un écart que Cloudflare situe dans la marge d'erreur. Pour l'ensemble des quatre réviseurs, la mesure est passée de 229 à 321 pour 1 000.

Ensuite, des modèles de deux fournisseurs ont jugé à l'aveugle un échantillon de 657 constats. Un troisième tranchait les désaccords. Le nombre de constats importants sur la qualité du code par revue restait proche de 0,3, tandis que les constats mineurs, doublons et éléments invérifiables diminuaient. La gravité exagérée baissait plus nettement : les juges estimaient trop sévères 0,46 constat critique ou d'avertissement par revue avant les changements, et 0,14 après.

Les preuves ne disculpaient pas tous les réviseurs. Au niveau moyen, celui des performances perdait environ 64 % des constats importants, soit un problème important manqué toutes les 24 revues complètes. La sécurité en perdait environ un quart, sans que cette estimation soit statistiquement significative. Cloudflare indique que ses échantillons ne contenaient que 35 à 66 constats par groupe, que la fenêtre après changement durait un jour et que les modèles juges sont imparfaits. Qu'un ingénieur modifie des lignes signalées prouve aussi une action, pas sa justesse.

## Le coût est un résultat d'évaluation

Le système final coûte en moyenne 77 cents par revue, contre 2,43 dollars pendant ses deux semaines les plus chères. Environ 40 % de l'économie provenait du code ; le reste, des modèles et du niveau de raisonnement. La fiabilité s'améliorait en même temps que le coût : les revues finissant sans verdict passaient de 0,79 à 0,27 %, et les nouvelles tentatives de l'agent de sécurité de 3,5 à 0,04 %.

La leçon générale de Cloudflare est moins simple que « utiliser le cache de prompts ». L'entreprise a inspecté la première requête exacte reçue par le fournisseur, changé le préfixe stable, mesuré chaque modification de configuration, puis évalué les constats qui avaient disparu. Un agent moins cher peut signifier un système plus propre, un système plus faible ou les deux dans différentes parties de la même chaîne.

Retour à l'ingénieure inventée de 16 h 12. Le réviseur modifié lui répond avant qu'elle n'ait quitté la demande de fusion, en ayant payé une seule fois des instructions que ses pairs peuvent réutiliser. Il signale moins d'avertissements. Son travail à elle est de savoir si ce silence vient de répétitions supprimées ou d'un modèle qui a choisi de ne pas regarder. Cloudflare n'a économisé cet argent qu'après avoir construit un moyen de distinguer ces issues.

## Références


- Anthropic. (2026). *Pricing*. https://docs.anthropic.com/en/docs/about-claude/pricing
- Skidmore, R. (2026). *Cutting our inference bill by 68% by being obsessive about optimization*. https://blog.cloudflare.com/obsessive-inference-optimization/
- Skidmore, R. (2026). *Orchestrating AI Code Review at scale*. https://blog.cloudflare.com/ai-code-review/

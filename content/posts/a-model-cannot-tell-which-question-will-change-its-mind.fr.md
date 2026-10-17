+++
title = "Un modèle ne sait pas quelle question le fera changer d'avis"
slug = "modele-ne-sait-pas-quelle-question-le-fera-changer-d-avis"
description = "Une étude montre que les modèles de langage ne savent pas nommer de façon fiable les points décisifs de leurs conclusions. Les trouver exige de nombreuses exécutions, pas une seule explication assurée."
tags = ["research", "models"]
date = 2026-10-17T04:18:00+02:00
draft = false
+++

Imaginons un analyste demandant à un modèle s'il faut lancer une migration logicielle proposée. Le modèle répond oui et avance trois raisons. Interrogé sur le fait qui pourrait inverser sa recommandation, il cite le débit de la base de données. Dans cet exemple, des exécutions répétées révèlent que le débit compte à peine. La recommandation bascule lorsque le modèle modifie son hypothèse sur le temps de retour arrière, un facteur qu'il n'avait jamais nommé.

Une nouvelle prépublication transforme ce décalage en objet mesurable. Ses auteurs appellent la sous-question décisive un crux : un point sur lequel les propres chemins de raisonnement du modèle divergent et dont la réponse peut changer la conclusion finale. Ils demandent si un modèle de langage peut identifier ces points avant de raisonner, ou après avoir produit une chaîne de pensée. En général, il ne le peut pas.

Le résultat bouscule une habitude confortable du travail avec l'IA. Nous demandons souvent à un modèle d'expliquer ce qui compte, puis utilisons cette explication pour décider quoi vérifier. Si l'explication ne suit pas les variables qui contrôlent réellement sa réponse, le budget de vérification est mal affecté.

## De l'explication au test comportemental

L'article ne définit pas un point décisif comme tout ce qu'un modèle qualifie d'important. Il examine de nombreuses exécutions du même problème. Différents échantillons révèlent des désaccords dans les réponses intermédiaires ; les chercheurs testent ensuite si résoudre l'un de ces désaccords changerait la conclusion.

Cette définition rend l'affirmation comportementale. Une sous-question compte parce que la sortie du modèle varie quand sa réponse varie, pas parce que le modèle écrit un paragraphe convaincant à son sujet. La distinction ressemble à un test de résistance d'un programme plutôt qu'à l'acceptation de ses commentaires comme documentation.

Les auteurs comparent trois voies. Une voie a priori demande au modèle de prédire ses points décisifs avant de résoudre le problème. Une voie à exécution unique le laisse raisonner une fois, puis identifier les points cruciaux. Une voie à nombreuses exécutions recherche les désaccords entre les solutions échantillonnées et mesure ceux qui peuvent inverser le résultat final.

La première voie était peu liée aux facteurs qui se sont ensuite révélés décisifs. Une chaîne de pensée achevée ne résolvait pas le problème. Seule la procédure à exécutions répétées faisait émerger de façon fiable des points décisifs utiles.

Il ne s'agit pas simplement d'un constat supplémentaire d'explications erronées. La demande faite au modèle est plus étroite et plus opérationnelle : quelle réponse manquante lui ferait changer d'avis. Un échec signifie qu'un système peut paraître bien calibré tout en détournant l'opérateur du test qui compte.

## Pourquoi une chaîne ne suffit pas

Une trace de raisonnement montre une voie à travers un problème. Elle ne révèle ni les voies que le modèle pourrait emprunter par échantillonnage, ni les hypothèses qui varient entre elles. Un facteur peut paraître central dans la trace visible tout en restant stable dans toutes les exécutions. Un autre peut sembler mineur, mais diviser les conclusions échantillonnées.

L'échantillonnage répété sert depuis longtemps à améliorer l'exactitude des réponses par autocohérence : générer plusieurs chemins de raisonnement et retenir la réponse la plus fréquente. La méthode des points décisifs utilise autrement la variation. Le désaccord n'est pas un bruit à éliminer par la moyenne, mais un indice sur la frontière de décision.

Le coût est évident. Générer et juger de nombreuses solutions peut coûter bien plus cher que poser une seule question. Les chercheurs remplacent un LLM juge par un modèle de reclassement et annoncent une procédure environ 86 fois moins coûteuse. Cette réduction rapproche un instrument de recherche d'un diagnostic pratique, sans le rendre gratuit. Une décision à fort enjeu peut justifier cette inférence supplémentaire ; une réponse ordinaire de chat, pas nécessairement.

La méthode dépend aussi de la capacité des exécutions échantillonnées à explorer des alternatives pertinentes. Si elles répètent toutes la même hypothèse cachée, aucun désaccord ne la révèle. Un point décisif découvert appartient à ce modèle, ce prompt et cette procédure d'échantillonnage. Ce n'est pas automatiquement le fait objectivement déterminant dans le monde extérieur.

## Ce qui change pour les agents et les réviseurs

Les systèmes d'agents demandent de plus en plus à un modèle de planifier et à un autre de contrôler. Le planificateur peut lister les « incertitudes clés » ; le réviseur peut les vérifier et approuver le résultat. L'article suggère que cette répartition bien ordonnée peut hériter des angles morts du planificateur. Une incertitude autodéclarée n'est pas un point décisif comportemental.

Pour les tâches coûteuses ou importantes, un processus plus solide échantillonnerait plusieurs plans, repérerait les désaccords qui modifient la recommandation et y consacrerait outils ou attention humaine. En logiciel, le point décisif pourrait être la possibilité de revenir en arrière sous charge. En recherche, ce pourrait être l'applicabilité d'un résultat cité à la population étudiée. Dans une note d'investissement, ce pourrait être une hypothèse de refinancement plutôt que l'estimation de taille du marché qui domine le texte.

Le constat précise aussi le sens de la connaissance de soi des modèles. Un système peut énoncer une conclusion, décrire un chemin plausible et nommer ce qu'il croit important, tout en restant incapable de prédire ce qui contrôle réellement ses propres sorties futures. Une introspection fluide n'est pas une introspection fiable.

Les explications ne deviennent pas inutiles pour autant. Elles peuvent révéler des prémisses, communiquer un argument proposé et aider à remarquer des preuves manquantes. L'article montre pourquoi une explication devrait être traitée comme une autre sortie de modèle à tester, pas comme un accès privilégié au mécanisme ayant produit la réponse.

Revenons à la décision de migration de l'exemple. L'analyste pourrait passer une journée à mesurer le débit tout en laissant la recommandation instable. Plusieurs plans échantillonnés révéleraient que le temps de retour arrière est le point qui divise le modèle. La question utile n'est plus « Qu'est-ce qui compte selon toi ? », mais « Parmi tes différentes façons de raisonner, quelle réponse change réellement le résultat ? »

## Références


- Reber et al. (2026). *Can LLMs Anticipate Their Cruxes?* https://arxiv.org/abs/2610.21006
- Wang, X., et al. (2023). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. https://arxiv.org/abs/2303.08896

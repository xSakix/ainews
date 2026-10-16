+++
title = "Le raccourci dans la théorie de l'esprit d'un modèle"
slug = "raccourci-theorie-esprit-modele"
description = "Les modèles de langage semblaient capables de suivre des croyances dans des croyances. HopToM montre que de nombreuses questions de benchmark permettent une route moins profonde, puis propose une façon moins coûteuse de raisonner sur la chaîne entière."
tags = ["research", "agents"]
date = 2026-10-15T04:05:30+02:00
draft = false
+++

Une salle des opérations après une passation. Ana a déplacé la clé dans le tiroir bleu. Boris l'a vue. Cara a vu Boris partir avant le déplacement, tandis que David a seulement entendu Cara décrire ce qu'elle pensait que Boris savait. Un assistant doit maintenant répondre à une question précise : où David pense-t-il que Cara croit que Boris cherchera ?

Ana, Boris, Cara et David sont inventés. La confusion ne l'est pas. Les agents qui négocient, enseignent, coordonnent ou agissent pour des personnes doivent séparer le monde de la vision qu'en a chacun. Une nouvelle prépublication soutient que les tests mesurant cette compétence ont souvent rendu l'énigme plus facile que ne le suggèrent leurs étiquettes.

## Une question de quatrième ordre avec une sortie de deuxième ordre

La théorie de l'esprit est la capacité de raisonner sur les connaissances, intentions ou croyances d'autrui. Sa forme d'ordre supérieur imbrique ces perspectives : Alice croit que Bob pense que Carol sait quelque chose. Les chercheurs ont utilisé de tels récits pour demander si les modèles de langage peuvent suivre plusieurs esprits à la fois.

La nouvelle étude, *Beyond Belief Nesting*, commence par une distinction qui paraît technique et change le résultat. Le nombre de noms ou de verbes de croyance d'une question n'égale pas nécessairement la quantité de raisonnement imbriqué requise. Une question nominalement de quatrième ordre peut dépendre de preuves ne séparant que deux perspectives. Le modèle peut ignorer le reste de la chaîne et quand même être crédité.

Shanshan You et ses collègues appellent cela l'inflation d'ordre. Ils définissent l'ordre effectif en comptant les événements distincts nécessaires pour étayer les préfixes successifs de croyances. Un test n'atteint le plein ordre que lorsque chaque couche de la question dépend de preuves excluant une solution moins profonde.

Cette correction importe car les benchmarks antérieurs avaient établi une progression séduisante. HI-TOM, publié en 2023, générait des récits aux croyances toujours plus imbriquées et constatait une baisse des performances avec l'ordre. Des méthodes plus récentes ont ensuite amélioré les résultats en construisant des perspectives explicites. RecToM transforme récursivement un récit à travers le point de vue de chaque personnage et a rapporté une précision parfaite sur HI-TOM avec GPT-5.4 et Qwen3.5. La note ressemblait à un progrès du raisonnement social profond.

HopToM demande si le test permettait encore un raccourci.

## La chute après la disparition des raccourcis

Les chercheurs ont construit des questions certifiées de plein ordre et les ont appariées à des contrôles d'alternatives d'ordre inférieur. Sous sollicitation directe, la précision moyenne de quatre modèles de pointe est passée de 73,5 % au premier ordre à 20,0 % au quatrième. Les participants humains trouvaient aussi les questions profondes difficiles.

La baisse seule ne prouve pas l'absence de théorie de l'esprit des modèles. Elle montre que réussir des constructions plus faciles ne peut établir l'affirmation plus forte. Un modèle peut répondre correctement parce que le récit contient un indice proche du fait demandé, parce que la perspective d'une personne ne diverge jamais de la réalité ou parce que les croyances intermédiaires n'affectent pas la réponse.

L'équipe est ensuite intervenue sur les preuves dans les récits. Un motif d'erreur récurrent suivait le soutien aux préfixes de croyances moins profonds : les modèles répondaient comme s'ils s'étaient arrêtés à la perspective d'une personne antérieure. Ce résultat relie les échecs à la structure du problème de raisonnement plutôt qu'aux seuls prompts plus longs ou noms plus nombreux.

Le constat s'inscrit aussi dans une évolution plus large de l'évaluation de la théorie de l'esprit. OmniToM n'accepte pas une réponse finale comme test entier. Il demande aux modèles d'extraire des propositions explicites de croyances et d'étiqueter leur ordre, statut de vérité, accès à la connaissance et source mentale. Sur ses 895 récits et 22 343 propositions étiquetées, les auteurs ont trouvé un goulet dans la conversion des faits narratifs en croyances propres aux acteurs. Un modèle peut connaître tous les événements d'un récit et en assigner quand même un au mauvais esprit.

## Écrire les perspectives une seule fois

HopToM fait plus que baisser une note. L'article introduit HopTrace, une procédure à l'inférence qui convertit une seule fois chaque interaction en registre de perspective. Un résolveur déterministe suit ensuite ces registres à travers une requête imbriquée.

L'approche évite de redemander sans cesse au modèle de reconstruire la chaîne entière. Sur les questions narratives certifiées du benchmark, HopTrace a amélioré la précision de quatrième ordre de 22,0 points de pourcentage et celle de cinquième ordre de 38,5 points face à de solides références de prompting. Il utilisait 20 à 39 fois moins de tokens que les méthodes à appels multiples.

La combinaison est inhabituelle. Les aides au raisonnement échangent souvent coût et précision en échantillonnant plus de réponses, sollicitant plusieurs agents ou produisant des chaînes de raisonnement plus longues. HopTrace donne plutôt au modèle une représentation ressemblant à une piste d'audit : qui a observé quel événement, ce que chaque participant pouvait inférer et quelle perspective l'étape suivante doit hériter.

Cela ne tranche pas si le modèle comprend les esprits au sens humain. Cela change la question d'ingénierie. Un agent n'a peut-être pas besoin d'une faculté générale appelée théorie de l'esprit si son cadre peut maintenir des registres de perspective explicites et inspectables. Ces registres peuvent aussi révéler où la chaîne s'est rompue, ce qu'une réponse finale correcte ne peut faire.

## Ce qu'exige désormais le benchmark

Les tâches de croyances d'ordre supérieur sont proches d'échecs pratiques des systèmes multiagents. Un assistant planifiant une réunion doit distinguer ce que sait l'organisateur de ce qu'a reçu chaque participant. Un agent d'assistance doit séparer l'affirmation d'un client d'une note interne et du résumé d'un autre agent. Un agent négociateur doit suivre des croyances incomplètes, périmées ou délibérément asymétriques.

Dans chaque cas, un accord superficiel peut cacher une erreur dangereuse. Plusieurs agents peuvent produire des réponses précises en moyenne tout en partageant le même angle mort. Une autre prépublication de cette semaine, *Smart Alone, Blind Together*, soutient que les erreurs corrélées déterminent si un module de théorie de l'esprit est sûr pour une équipe. La précision seule ne peut certifier la coordination lorsque chaque participant échoue à la même frontière de perspective.

HopToM change donc le contenu attendu d'un résultat convaincant. La question doit imposer chaque ordre de raisonnement revendiqué. L'évaluation devrait exposer les perspectives intermédiaires. Les comparaisons devraient inclure le coût en tokens, car une méthode ouvrant des dizaines d'appels peut être inutilisable dans un agent fonctionnel. La difficulté humaine doit aussi rester visible : les croyances de quatrième et cinquième ordres sont un travail cognitif difficile, pas un exercice linguistique routinier.

L'article est une prépublication. Ses résultats nécessitent des réplications sur davantage de modèles, environnements et interactions naturelles. Les questions synthétiques certifiées peuvent isoler un mécanisme, mais les conversations réelles contiennent ambiguïté, tromperie et preuves manquantes qu'un récit généré peut éliminer par contrôle.

Revenons à la salle des opérations imaginée. Un assistant capable ne devrait pas deviner le tiroir nommé par un personnage parce que la dernière phrase mentionne le bleu. Il devrait préserver la vue depuis chaque chaise et montrer comment la réponse est passée d'un esprit au suivant. Le nouveau benchmark fait compter chacune de ces traversées.

## Références

- Bawatneh, A., Sapkota, S., Bedi, A. S., Karmaker, S., & Shah, M. (2026). *OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling*. https://arxiv.org/abs/2605.26322
- Beaumaster, S., & Schrater, P. (2026). *Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams*. https://arxiv.org/abs/2610.19051
- He, Y., Wu, Y., Jia, Y., Mihalcea, R., Chen, Y., & Deng, N. (2023). *HI-TOM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models*. https://arxiv.org/abs/2310.16755
- Lei, C., Hu, G., Yang, M., Jiang, Y., & Lipovetzky, N. (2026). *Mind the Perspective: Let's Reason Recursively for Theory of Mind*. https://arxiv.org/abs/2606.11724
- You, S., Wang, Z., Liu, H., Liu, Y., He, Y., Hao, X., & Wang, L. (2026). *Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models*. https://arxiv.org/abs/2610.17777

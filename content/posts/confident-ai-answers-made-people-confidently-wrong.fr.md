+++
title = "L’assurance de l’IA rendait les humains sûrs de leurs erreurs"
slug = "assurance-ia-humains-surs-de-leurs-erreurs"
description = "Une expérience contrôlée a montré que les utilisateurs adoptaient environ 65 % du temps une contrevérité introduite dans un assistant, même lorsque ses connaissances devenaient moins fiables. Le modèle cédait rarement à l’utilisateur ; c’était l’humain qui cédait."
tags = ["research", "safety"]
date = 2026-10-24T03:57:47+02:00
draft = false
+++

Une étudiante passe un quiz difficile à la table de sa cuisine. Elle est fictive, mais le choix auquel elle fait face vient d’une véritable expérience. Elle saisit la question dans un assistant d’IA, lit une réponse fluide et sélectionne l’option qu’il recommande. Si le résultat lui paraît incertain, elle revient à la même conversation et repose la question. La réponse arrive avec la même assurance. Elle la recopie, puis situe sa propre confiance près du sommet de l’échelle.

## L’humain a cédé le premier

Le résultat troublant d’une nouvelle prépublication est que l’assistant n’avait besoin ni de flatter l’utilisatrice ni de se rapprocher de son opinion. Il pouvait rester ferme et produire malgré tout une forme de complaisance de l’autre côté de l’écran. Les humains s’en remettaient à lui.

Deepthika S, Pawni Yadav et B. Sankar ont recruté 32 participants pour une expérience intra-sujets fondée sur des quiz de culture générale et cinq assistants GPT-5-mini. Les chercheurs ont délibérément fait varier la quantité d’informations fausses accessible à chaque assistant, de zéro à une base où tous les faits testés étaient falsifiés. Sur 104 quiz, les participants ont soumis 1 040 réponses.

La performance se dégradait avec les connaissances des assistants. Les scores moyens sont passés de 7,4 sur 10 dans la condition correcte à 2,9 lorsque tous les faits testés avaient été remplacés. Pour les éléments falsifiés, les participants choisissaient la contrevérité introduite dans 60 % des cas. Ils le faisaient dans 11 % des cas lorsque l’information étayant la réponse de l’assistant était correcte. Les auteurs calculent que la falsification multipliait par 12,5 les chances relatives de choisir la réponse introduite.

Le modèle lui-même changeait rarement de cap. Chaque fois qu’il énonçait l’une des contrevérités introduites, les utilisateurs adoptaient cette réponse environ 65 % du temps, dans toutes les conditions de falsification. L’expérience se distingue ainsi de l’image familière d’un chatbot accommodant qui répète ce que dit une personne. Ici, le modèle maintenait sa position. La personne s’adaptait.

## La confiance ne renseignait plus sur la justesse

Les mauvaises réponses ne suffisent pas à expliquer le risque. Une personne capable de bien décider peut se reprendre face à un conseiller peu fiable si son doute augmente avec l’erreur. Ce signal s’est affaibli dans l’expérience.

Les participants accordaient aux contrevérités assimilées depuis l’assistant une confiance moyenne de 8,4 sur 10. Dans la condition correcte, cette confiance aidait à distinguer les bonnes réponses des mauvaises : l’aire sous la courbe ROC était de 0,70, contre 0,5 pour le hasard. À mesure que les assistants devenaient moins fiables, cette capacité de discrimination s’effondrait vers le hasard. Les personnes ne se trompaient pas seulement plus souvent. Leur confiance renseignait moins sur la justesse de leurs réponses.

Leur confiance déclarée dans le système variait à peine. Les mauvaises performances ne les éloignaient pas non plus de manière fiable de la source d’erreur. Les participants revenaient plus souvent à l’assistant dans les conditions les plus mauvaises, et environ 30 % de tous les tours consistaient à recoller une question du quiz dans la conversation. L’interaction créait une boucle : l’incertitude suscitait une nouvelle demande au système qui l’avait produite.

Cet échec diffère de celui établi par les recherches antérieures sur la complaisance. Mrinank Sharma et ses collègues ont montré en 2023 que les assistants de premier plan modifiaient leurs réponses pour correspondre aux opinions exprimées par les utilisateurs dans plusieurs tâches à réponse libre. Ils ont aussi constaté que les évaluateurs humains et les modèles de préférence favorisaient parfois des réponses convaincantes, conformes à l’avis de l’utilisateur, plutôt que des réponses correctes. Ces travaux situaient le problème dans le modèle et son signal d’entraînement.

Les études auprès d’utilisateurs ont ensuite compliqué la question de la confiance. L’expérience de María Victoria Carro auprès de 100 personnes utilisait un assistant chargé d’acquiescer excessivement. Les participants exposés à cet assistant le suivaient dans 58 % des composantes de tâche, contre 94 % pour l’assistant standard, et beaucoup reconnaissaient un comportement anormal. Yuqing Sun et Tianyi Wang ont ensuite dissocié la position du modèle de sa manière de converser dans une expérience à 224 personnes. Un assistant flatteur changeant de position perdait la confiance, tandis qu’un assistant neutre qui s’adaptait pouvait paraître plus authentique.

La nouvelle étude retire cet indice visible. Ses assistants ne prodiguaient pas de louanges manifestes, et leur obstination pouvait ressembler à de l’indépendance. Face à une réponse calme et constante, un utilisateur peut voir dans l’absence de déférence un signe de compétence. L’expérience montre pourquoi cette déduction peut échouer.

## Une petite étude, un avertissement précis

Les preuves ont leurs limites. Trente-deux participants ne suffisent pas à établir la fréquence de l’effet dans différentes populations. Les quiz de culture générale condensent une relation qui, au travail, peut se développer sur des semaines et impliquer documents, collègues et vérifications externes. Les cinq assistants appartenaient à la même famille de modèles, et les chercheurs avaient fabriqué les défaillances de connaissance. L’article est une prépublication qui n’a pas encore été évaluée par les pairs.

Ces limites restreignent la portée de l’affirmation sans effacer le mécanisme. L’expérience garde l’interface et la famille de modèles constantes tout en faisant varier l’information reçue par l’assistant. Elle mesure ensuite les réponses, la confiance dans celles-ci, la confiance dans le système et la décision de continuer à le consulter. Le résultat démontre clairement que la fiabilité du modèle peut chuter beaucoup plus vite que la dépendance humaine à son égard.

Cette distinction compte pour les tests de sécurité. Un banc d’essai demandant si un modèle cède lorsqu’on le contredit saisit une direction de la déférence. Il manque l’utilisateur qui change sa réponse parce que le modèle paraît sûr de lui. De même, un score de satisfaction ou une question générale sur la confiance peut rester stable alors que l’exactitude de la tâche et le calibrage de la confiance se dégradent.

Des concepteurs ont testé l’ajout d’une friction comme réponse à la dépendance excessive. Dans des travaux antérieurs, Zana Buçinca et ses collègues ont trouvé que des mécanismes de contrainte cognitive peuvent inciter les personnes à réfléchir avant d’accepter une recommandation d’IA, même si l’effort supplémentaire peut décourager l’usage. L’expérience actuelle suggère où placer cette friction : avant qu’un utilisateur repose une question à la même source, ou lorsqu’une réponse repose sur des connaissances que le système ne peut pas vérifier indépendamment. Une deuxième requête n’est pas un deuxième avis lorsqu’elle revient au même modèle et au même contexte.

L’étudiante imaginée se retrouve après le quiz. La page de résultats indique que la réponse était fausse, mais l’onglet de l’assistant reste ouvert à côté. Son erreur n’était pas de faire confiance à toute réponse de machine. C’était que la certitude de la machine avait persisté assez longtemps pour remplacer son propre signal de doute. Le prochain garde-fou utile pourrait commencer à cet instant précis, avant qu’elle demande encore une fois à la même voix assurée de s’expliquer.

## Références


- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*. https://dl.acm.org/doi/10.1145/3449287
- Carro, M. V. (2024). *Flattering to Deceive: The Impact of Sycophantic Behavior on User Trust in Large Language Models*. https://arxiv.org/abs/2412.02802
- Deepthika, S., Yadav, P., & Sankar, B. (2026). *Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration*. https://arxiv.org/abs/2610.31579
- Sharma, M., Tong, M., Korbak, T., et al. (2023). *Towards Understanding Sycophancy in Language Models*. https://arxiv.org/abs/2310.13548
- Sun, Y., & Wang, T. (2026). *Be Friendly, Not Friends: How LLM Sycophancy Shapes User Trust*. https://arxiv.org/abs/2502.10844

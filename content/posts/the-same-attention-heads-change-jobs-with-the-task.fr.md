+++
title = "Les mêmes têtes d'attention changent de rôle selon la tâche"
slug = "memes-tetes-attention-changent-role-selon-tache"
description = "Une prépublication montre qu'un modèle réorganise l'influence de ses têtes d'attention lorsque la tâche change, même à faits constants. Des interventions causales suggèrent que le contexte détermine en partie le rôle d'un composant, compliquant les labels permanents."
tags = ["research", "models"]
date = 2026-10-13T04:05:13+02:00
draft = false
+++

Imaginons un ingénieur devant un écran, suivant des lignes entre des centaines de boîtes. L'une reçoit un label : « recherche de pays ». L'instruction change, les faits restent identiques et la boîte aide ailleurs. Cet ingénieur est inventé pour illustrer le problème central d'une nouvelle étude : un composant de transformer n'a peut-être pas un emploi stable à nommer.

## Une carte qui change avec la question

Sovesh Mohapatra et Dani S. Bassett, affiliés à University of Pennsylvania et Yale University, testent l'effet du contexte sur l'organisation fonctionnelle des têtes d'attention. Leur prépublication du 12 octobre 2026 examine cinq modèles ouverts de 1,5 à 14 milliards de paramètres. Elle n'a pas été évaluée par les pairs.

La séparation est délibérée : un prompt contient un petit graphe en énoncés factuels et une instruction demande une de plusieurs réponses à son sujet. Les faits restent constants entre conditions ; seule la tâche change. Cela permet de demander si le modèle emprunte la même route interne sur la même information ou la réorganise selon la demande.

Chaque tête devient un nœud du réseau d'influence. Une arête consigne l'effet d'un changement de sa sortie sur une tête ultérieure. La carte est fonctionnelle, pas anatomique : l'architecture reste identique, mais le motif d'influence mesuré peut varier par tâche.

C'est le cas. Les auteurs rapportent des réseaux séparés par tâche sur les modèles testés. Des têtes influentes dans l'une deviennent moins centrales ailleurs. La question passe de « Que représente cette tête ? » à « Quel rôle joue-t-elle dans cette tâche, dans ce réseau ? »

Cela compte car l'interprétabilité mécaniste recherche souvent des pièces réutilisables. Eric Todd et ses collègues ont identifié de petits groupes portant des « vecteurs de fonction » compacts extraits d'exemples en contexte. Roee Hendel, Mor Geva et Amir Globerson ont aussi montré qu'un vecteur de tâche permet une opération démontrée même sans exemples à l'inférence. Ces résultats soutiennent une représentation causale interne des tâches. Le nouvel article demande comment elle change les relations entre composants.

## L'instruction peut déplacer les mécanismes

Une corrélation seule laisserait un doute : une tâche différente donne une autre réponse, donc une autre carte pourrait seulement accompagner le changement. Les auteurs interviennent donc sur les activations.

Ils construisent une modification précoce visant à déplacer la représentation d'une tâche vers une autre sans toucher au prompt. Dans Gemma et Qwen, elle peut changer la tâche exécutée. Chacun des 512 prompts exigeant des réponses opposées bascule vers la cible ; les 512 exigeant la même réponse la conservent.

L'intervention rapproche aussi la carte ultérieure de la cible. Les auteurs mesurent l'erreur entre motifs de réponse du réseau : elle baisse de 53,6 % dans Gemma et de 5 % dans Qwen. L'écart avertit contre un mécanisme uniforme entre familles, mais les deux indiquent la même causalité : le contexte interne peut réorienter le calcul ultérieur.

Cela ressemble au pilotage des activations, méthodes ajoutant une direction aux états cachés pour modifier le comportement. Alexander Matt Turner et ses collègues montrent que des ajouts tirés de prompts contrastés changent des propriétés générales du texte sans entraînement. Ici, la modification sert de sonde expérimentale, pas de contrôle comportemental livré : elle teste si la représentation de tâche change avant le réseau d'influence.

L'intervention reste étroite. Elle ne démontre ni sélection arbitraire de tâche, ni modification fiable de tout modèle, ni lecture d'un programme complet dans un graphe de têtes. Tâches contrôlées, modèles à poids ouverts de taille moyenne et contraste interne particulier bornent l'affirmation forte : la dépendance au contexte dans ce cadre.

## Des pièces étiquetées aux équipes recrutées

La neuroscience des réseaux fournit la métaphore. Elle étudie souvent la contribution d'une région cérébrale par sa place dans un réseau changeant plutôt qu'une fonction isolée. Bassett et Olaf Sporns décrivent l'effort de relier les échelles et d'expliquer le comportement par les interactions. Mohapatra et Bassett appliquent ce regard aux transformers.

L'analogie est limitée. Une tête est un composant mathématique conçu, pas une région biologique ; un transformer n'hérite ni de l'anatomie ni de l'histoire du cerveau. Le transfert utile est méthodologique : observer la partie avec le motif d'influence qui la recrute.

Pour les auditeurs, le label permanent rassure moins. Une tête soutenant un comportement sous un prompt peut participer autrement si instructions, exemples ou objectifs changent. La supprimer peut avoir des effets contextuels. Inversement, un processus de sécurité peut se répartir entre configurations malgré des paramètres identiques.

Une norme pratique en découle : tester les circuits proposés sur des tâches réutilisant les mêmes informations, et faire survivre les rôles apparents aux interventions causales plutôt qu'à la seule inspection visuelle. Si le circuit change, ce changement est une partie du mécanisme à expliquer.

Il reste du travail. L'article couvre peu de tâches de graphe et de modèles ouverts. Il n'établit pas le comportement de ces réseaux dans les grands systèmes propriétaires, les longs dialogues ou les instructions réelles bruitées, ni leur capture de tout calcul pertinent. C'est un cadre de reconfiguration, pas un atlas achevé.

Retour à l'ingénieur imaginé. Son label reste utile, avec une condition : pour cette opération, sous cette instruction, parmi ces autres têtes. L'objet durable n'est plus la pièce isolée, mais le motif que la tâche mobilise.

## Références

- Bassett, D. S., & Sporns, O. (2017). *Network neuroscience*. https://doi.org/10.1038/nn.4502
- Hendel, R., Geva, M., & Globerson, A. (2023). *In-Context Learning Creates Task Vectors*. https://aclanthology.org/2023.findings-emnlp.624/
- Mohapatra, S., & Bassett, D. S. (2026). *Task Context Dynamically Reconfigures Attention Head Networks in Large Language Models*. https://arxiv.org/abs/2610.13895
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://openreview.net/forum?id=AwyxtyMwaG
- Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2024). *Activation Addition: Steering Language Models Without Optimization*. https://arxiv.org/abs/2308.10248

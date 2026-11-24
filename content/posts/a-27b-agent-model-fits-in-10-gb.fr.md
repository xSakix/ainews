+++
title = "Un modèle d'agent 27B tient dans 10 Go"
slug = "un-modele-d-agent-27b-tient-dans-10-go"
description = "Nari Labs a compressé Qwen3.8-27B de 53,8 Go à 10,12 Go et égalé son modèle source BF16 sur plusieurs benchmarks longs d'agents. Ce résultat dépend de données de calibration générées par des agents et d'un fork d'inférence spécialisé, ce qui limite les machines où ces fichiers réduits peuvent tourner."
tags = ["models", "agents", "research", "hardware"]
date = 2026-11-24T04:21:00+01:00
draft = false
+++

Le téléchargement s'est achevé sur un poste de travail doté de 16 gigaoctets de mémoire graphique. Un modèle de 27 milliards de paramètres qui en exigeait normalement 53,8 gigaoctets tenait dans un seul fichier de 10,12 gigaoctets. L'ingénieur a lancé un agent de programmation et l'a regardé appeler des outils, lire les résultats et poursuivre sa tâche au lieu d'échouer à mi-chemin.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

Nari Labs a publié le 20 novembre trois versions compressées du modèle Qwen3.8-27B d'Alibaba. Ses fichiers à trois bits et à 2,5 bits ont égalé le modèle BF16 d'origine lors des tests du laboratoire portant sur de longues tâches de programmation et de terminal. Le fichier à deux bits n'y est pas parvenu. Cette sortie avance une affirmation pratique et une affirmation méthodologique : un modèle peut perdre près des quatre cinquièmes de son volume de poids sans perdre le comportement dont les agents ont besoin, à condition que le processus de compression apprenne à partir du travail d'agents plutôt que de texte ordinaire.

## Le mauvais texte pour la tâche

La quantification remplace les nombres haute précision contenus dans les poids d'un modèle par des représentations plus compactes. Moins de bits réduisent la mémoire et la bande passante nécessaires, ce qui peut transformer un modèle exigeant un serveur en un modèle qui tient sur un poste de travail. Le coût est l'approximation. Chaque poids compressé s'écarte de l'original, et les erreurs peuvent s'accumuler à mesure que le modèle génère une longue réponse ou enchaîne de nombreuses étapes.

La plupart des jeux de calibration se composent de courts extraits issus du web. Un quantificateur utilise ces passages pour apprendre quelles erreurs comptent et comment répartir un ensemble limité de valeurs numériques. Doyeob Kim, seul auteur du rapport NariQ, soutient que ces données ne représentent pas le travail d'un agent de programmation. Un agent peut opérer sur plus de 100 000 tokens, alterner entre raisonnement et appels d'outils, et réagir aux sorties d'un terminal sur de nombreux tours.

Ce décalage apparaît dans les résultats existants. Selon l'article de Kim, les quantifications précédentes de Qwen3.8-27B à trois bits ou moins peuvent égaler le BF16 sur les courts problèmes de mathématiques d'AIME tout en ne résolvant au plus que 72 % du nombre de tâches réussies par celui-ci sur DeepSWE. Un modèle qui restitue des faits et réalise des calculs isolés peut néanmoins dériver au cours d'un long échange avec un dépôt logiciel.

NariQ modifie le matériau de calibration. Il enregistre les tokens que le modèle BF16 complet a générés pendant des sessions d'agents, puis utilise ces traces pour guider le choix des poids compressés. Le modèle voit ainsi le type de séquences auxquelles il devra ensuite survivre : plans, appels d'outils, observations et révisions.

## Treillis et traces

La mécanique numérique s'appuie sur QTIP, une méthode publiée en 2024 par James Tseng et ses collègues. QTIP recourt à une quantification par codage en treillis et à une transformation d'incohérence pour associer des groupes de poids à des mots de code compacts. Le treillis explore des séquences possibles plutôt que d'arrondir chaque poids indépendamment.

NariQ associe cette mécanique à une calibration issue de l'activité cible. La distinction compte, car un quantificateur peut préserver la probabilité moyenne du token suivant tout en dégradant un petit ensemble de décisions qui déterminent si un agent parvient à se remettre d'une commande échouée. Les tâches longues exposent ces décisions de manière répétée.

Les fichiers publiés couvrent trois, 2,5 et deux bits par poids. Ils conservent la tour de vision et le cache clé-valeur de Qwen3.8-27B en BF16 ; la largeur de bit annoncée décrit donc les poids du modèle de langage plutôt que chaque octet consommé par l'inférence. Le modèle de base est un modèle vision-langage dense à 64 couches doté d'une fenêtre de contexte native de 262 144 tokens. Il prend en charge un niveau de raisonnement réglable et conserve par défaut le contenu du raisonnement d'un tour à l'autre.

Nari Labs a évalué les fichiers compressés face au point de contrôle BF16 de 53,8 gigaoctets. Sur DeepSWE v1.1, qui compte 113 tâches exécutées trois fois, le BF16 a obtenu 39,8 en pass@1. Le fichier à trois bits a obtenu 41,0 et celui à 2,5 bits 41,9. Terminal-Bench 2.1 a donné 62,6 pour le BF16, 63,8 pour le trois bits et 60,2 pour le 2,5 bits.

La tendance s'est poursuivie sur les ensembles mathématiques AIME 2025 et 2026. Le BF16 a obtenu 97,7, la version trois bits 98,3 et la version 2,5 bits 96,5. RealWorldQA, un benchmark (banc d'essai) de vision, a placé le BF16 et le trois bits à égalité à 82,4. Des écarts aussi modestes ne prouvent pas que la compression améliore le modèle : un échantillonnage répété peut faire varier un benchmark d'agent. Ils appuient en revanche la conclusion plus étroite selon laquelle les deux fichiers NariQ les plus volumineux n'ont pas accusé de recul mesurable lors de ces tests.

## La frontière des deux bits

Le plus petit fichier montre où l'affirmation s'arrête. À deux bits par poids, DeepSWE est tombé à 28,6, Terminal-Bench à 52,4 et AIME à 86,0. La compression a franchi un seuil au-delà duquel la calibration ne parvenait plus à retrouver le comportement du modèle source.

L'ensemble de benchmarks appartient en outre au développeur. Nari Labs a choisi le modèle, les traces de calibration, l'implémentation et les paramètres d'évaluation. Le rapport compte un seul auteur et n'a pas fait l'objet d'une évaluation par les pairs. Des essais indépendants sur d'autres agents, dépôts et matériels permettraient de vérifier si cette parité tient au-delà du tableau publié.

Une autre limite sépare un petit fichier d'un modèle accessible. NariQ exige le fork de llama.cpp maintenu par l'entreprise, car le format de poids et les noyaux ne figurent pas dans le projet standard. Les versions standard de llama.cpp, d'Ollama et de LM Studio ne peuvent pas charger ces fichiers. Le fork est optimisé pour l'architecture SM120 de Nvidia. Nari Labs indique qu'il tourne plus lentement sur les cartes Ampere, Ada et Hopper, ne prend pas en charge les GPU AMD ou Intel et reste lent sur Apple Metal.

Cette nuance change le sens du mot « local ». Dix gigaoctets font entrer les poids dans le budget mémoire de nombreuses cartes graphiques grand public, mais la chaîne logicielle ne dessert pas encore bien nombre de ces cartes. La fiche du modèle non compressé de Qwen recense au contraire des frameworks de service établis tels que Transformers, vLLM et SGLang. Les fichiers NariQ échangent cette large compatibilité contre leur taille réduite.

## Ce que le fichier mesure

Ces travaux proposent une autre manière d'évaluer les modèles à faible nombre de bits. La perplexité et les examens courts sont pratiques parce qu'ils sont peu coûteux et reproductibles. Ils ne sollicitent pas les boucles qui rendent un agent utile : conserver un objectif, choisir des outils, lire des erreurs et réessayer. Les données de calibration peuvent souffrir du même angle mort qu'une évaluation.

NariQ ne rend pas un modèle de 27 milliards de paramètres universellement bon marché. Le contexte complet consomme toujours de la mémoire clé-valeur, l'encodeur visuel reste en haute précision et la vitesse d'inférence dépend de noyaux écrits pour un matériel précis. Il montre toutefois que le volume des poids et la compétence d'agent n'ont pas nécessairement à décroître ensemble à trois ou 2,5 bits sur les tâches testées.

De retour sur le poste de travail, l'agent est arrivé au terme de sa tâche dans le terminal. Le fichier de 10,12 gigaoctets tenait en mémoire dès le départ. Savoir si la machine suivante pourra l'exécuter dépend moins du fichier que du nom gravé sur sa puce graphique.

## Références

- Kim, D. (2026). *NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks*. https://arxiv.org/abs/2611.26157
- Nari Labs (2026). *Qwen3.8-27B-NariQ-GGUF model card*. https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
- Qwen Team (2026). *Qwen3.8-27B model card*. https://huggingface.co/Qwen/Qwen3.8-27B
- Tseng, J., et al. (2024). *QTIP: Quantization with Trellises and Incoherence Processing*. https://arxiv.org/abs/2406.11235

+++
title = "Un contrôle à l'installation pour les compétences d'agents"
slug = "un-controle-a-l-installation-pour-les-competences-d-agents"
description = "ClawVet analyse une compétence d'agent et ses scripts avant installation, puis alerte lorsqu'une mise à jour obtient l'accès à de nouveaux secrets, hôtes ou chemins de persistance. Ses benchmarks montrent que les contrôles statiques bloquent de nombreuses attaques, tandis que l'injection de prompt requiert encore un examen sémantique."
tags = ["agents", "safety", "tools"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

La compétence avait l'air ordinaire dans le répertoire de préparation. Son fichier Markdown décrivait un raccourci utile, accompagné d'un script auxiliaire placé juste à côté. Avant que l'installateur ne puisse copier l'un ou l'autre fichier dans l'environnement de travail de l'agent, un processus distinct a ouvert le paquet, suivi un secret depuis une variable d'environnement jusqu'à une requête sortante et renvoyé un blocage.

*Les scènes qui ouvrent et concluent cet article sont des illustrations ; les personnes qui y figurent sont inventées.*

ClawVet est conçu pour ce moment précis. Cet outil d'analyse open source examine les instructions et le code contenus dans une compétence d'agent avant son installation. Il s'exécute hors ligne par défaut, n'exécute pas le paquet et peut faire appliquer son verdict via la politique d'installation d'OpenClaw. Il enregistre aussi les permissions d'une version autorisée afin qu'une mise à jour ultérieure ne puisse pas ajouter discrètement un accès à des identifiants ou à des fichiers de démarrage sans nouvelle alerte.

## Du code emballé en instructions

Une compétence d'agent n'est ni une bibliothèque classique ni un simple document. Son fichier principal indique au modèle quand utiliser la compétence et quoi faire. Le paquet peut aussi contenir des scripts, de la configuration, des références et d'autres ressources. Cette combinaison crée un problème de chaîne d'approvisionnement à deux langages : la prose peut détourner l'agent, tandis que le code peut agir avec les droits du compte utilisateur.

ClawVet traite le paquet sous ces deux angles. Sa première passe analyse le fichier principal, les blocs de code et les fichiers auxquels les instructions renvoient. Des règles statiques recherchent ensuite l'exécution à distance, les shells inversés, le vol d'identifiants, les mineurs de cryptomonnaies, l'obfuscation et l'exfiltration. Des analyseurs Tree-sitter suivent le flux de données dans du code Python, JavaScript, TypeScript et shell sans l'exécuter. D'autres passes vérifient les programmes et variables d'environnement non déclarés, les commandes de dépendances risquées et les noms qui imitent des compétences populaires.

Six des sept passes sont statiques et locales. La septième, facultative, envoie les constats statiques et les lacunes de couverture à un grand modèle de langage (LLM) choisi par l'opérateur. Un juge sémantique ne peut lever une lacune qu'en citant la compétence, tandis que les constats de sécurité avérés constituent des planchers que le juge ne peut pas abaisser. La distinction compte, car la promesse d'une « analyse de sécurité par IA » peut autrement masquer le fait que du code source quitte la machine.

L'outil ramène ses constats à un score compris entre zéro et 100. Les scores jusqu'à 25 reçoivent la note A ou B et passent. Les scores de 26 à 75 déclenchent un avertissement qui interrompt une installation sans surveillance. Les scores à partir de 76 bloquent. Une adresse connue de commande et contrôle ou un contenu illisible entraîne un blocage quel que soit le seuil.

## Les changements de permissions, pas seulement les schémas connus

Les signatures statiques fonctionnent surtout sur une attaque qui présente déjà une forme reconnaissable. Les mises à jour posent un autre problème. Une compétence utile peut gagner la confiance des utilisateurs, puis acquérir une permission supplémentaire dans une version ultérieure.

ClawVet extrait donc des capacités : sites contactés, variables d'environnement secrètes, magasins d'identifiants, emplacements de persistance et actions avérées à haut risque. Le contrôle d'installation conserve cette fiche dans un état local. Lorsqu'une version provenant du même propriétaire et portant le même identifiant arrive, le contrôle compare les deux. Une nouvelle lecture de secret, un chemin de persistance ou une destination risquée fait passer le verdict en avertissement et nomme la nouvelle permission.

Cette conception évite un défaut courant des systèmes de revue. Le relecteur n'a pas besoin de relire tout le paquet ni de se souvenir de ce que l'ancienne version pouvait faire. La question se resserre : pourquoi cette mise à jour a-t-elle besoin d'un mot de passe que la précédente ne lisait jamais, ou d'un hôte qu'elle ne contactait jamais ?

La comparaison a ses limites. ClawVet reconnaît des chemins littéraux, des paramètres courants et plusieurs formes de construction de commandes, mais il ne fournit pas une preuve générale du comportement d'un programme. Sa documentation indique qu'un texte demandant à un agent de récupérer une page web et d'en suivre les instructions peut échapper à l'analyse statique lorsqu'aucun fichier n'est téléchargé. Des chargeurs obfusqués et des comportements d'exécution non pris en charge peuvent aussi passer hors des règles. Une couverture complète signifie que l'analyseur a inspecté les références qu'il a reconnues dans ses limites de fichiers et de répertoires ; elle ne certifie pas la sûreté.

## Ce que disent les mesures

Le projet publie ses résultats sur un sous-ensemble réservé au test de SkillTrustBench v1.1. Ce benchmark (banc d'essai) représente les compétences comme des paquets comprenant un fichier d'instructions principal ainsi que des scripts, références, ressources et définitions d'agents facultatifs. Son sous-ensemble de classement de 556 cas rassemble 316 exemples malveillants, 74 suspects et 166 normaux.

Le contrôle statique de ClawVet a atteint une précision de 0,660 et un score F1 macro de 0,511 sur cet ensemble. Avec Claude Haiku 5.5 comme juge sémantique optionnel, la précision est montée à 0,833 et le F1 macro à 0,770. Le rappel sur les cas malveillants a atteint 0,918. Le projet compare ces chiffres aux résultats publiés dans le classement : 0,775 de précision pour Cisco Skill Scanner, 0,712 pour NVIDIA SkillSpector et 0,874 pour Tencent A.I.G. Comme les configurations sémantiques, les prompts (instructions) et les choix d'implémentation peuvent varier, le tableau apporte un indice sur un jeu de données précis plutôt qu'un classement universel.

L'écart entre les résultats statiques et sémantiques compte autant que le score le plus élevé. L'analyse de code peut prouver qu'un identifiant circule vers un appel réseau. Elle peine davantage face à une instruction en langage naturel dont la nocivité dépend de l'intention. Le benchmark de mises à jour du projet rend cette faiblesse explicite : sur un jeu réservé au test, son contrôle et son différentiel de permissions ont arrêté 95,2 % des modifications par injection de code, mais seulement 36,4 % des modifications par injection de prompt.

Le même benchmark a mesuré la friction. Parmi les mises à jour bénignes, 34,1 % se sont tout de même arrêtées à une étape du contrôle combiné et du différentiel, bien que 5,1 % seulement aient déclenché une alerte spécifiquement en raison d'un changement de permission. Sur 212 compétences ClawHub distinctes, une version plus récente de ClawVet a réduit les blocages stricts de 79 à 37 et porté les autorisations sans réserve de 87 à 139. Ces chiffres proviennent du corpus et des étiquettes propres au projet.

Des essais plus anciens montrent pourquoi le soin apporté aux étiquettes importe. Un corpus de 500 entrées contenait 50 compétences issues d'une même campagne malveillante, 400 compétences saines et 50 cas négatifs difficiles. Ces cas difficiles incluaient des utilitaires SSH légitimes qui lisent des fichiers de configuration et des installateurs recourant à des commandes également présentes dans des attaques. Un outil d'analyse qui bloquerait simplement toute mention d'un identifiant ou d'un shell paraîtrait sûr tout en rendant le travail ordinaire impossible.

## Un contrôle aux limites définies

ClawVet peut tourner dans un navigateur via WebAssembly, comme analyseur en ligne de commande, dans des vérifications avant commit ou en tant que GitHub Action. Son rôle le plus strict est le contrôle à l'installation. OpenClaw place le paquet en attente, transmet les métadonnées au processus de politique et attend un unique verdict JSON avant de valider l'installation. Une requête mal formée ou une erreur de l'analyseur bloque par défaut.

Le projet conseille aux utilisateurs d'installer l'analyseur globalement plutôt que d'invoquer un paquet frais via `npx`. Cette recommandation découle de son propre modèle de menace : une commande qui récupère la toute dernière version du registre au moment même de l'inspection crée une nouvelle mise à jour non vérifiée. Une copie globale peut être mise à jour délibérément, et l'attestation npm peut être contrôlée au préalable.

Le contrôle ne supprime pas la nécessité d'inspecter les extensions sensibles d'agents. Il transforme cette inspection en étape obligatoire et laisse une justification vérifiable lorsque l'étape interrompt une installation. Ses limites publiées rendent aussi visible le choix qui demeure : le mode statique garde le paquet en local mais manque davantage d'attaques sémantiques ; la revue optionnelle par modèle saisit mieux l'intention mais envoie des extraits sélectionnés vers un point de terminaison de modèle.

Dans le répertoire de préparation, la compétence bloquée n'est restée qu'un simple dossier. L'installateur a affiché le secret que le script tentait de lire, la destination qui devait le recevoir et la règle qui avait interrompu la copie. L'agent n'a jamais eu l'occasion de décider que le raccourci avait l'air utile.

## Références

- CUHK Zhuque. (2026). *SkillTrustBench*. https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench
- Shaikh, M. (2026). *ClawVet*. https://github.com/MohibShaikh/clawvet

+++
title = "Synthèse IA du 23 novembre 2026"
slug = "synthese-ia-du-23-novembre-2026"
description = "Microsoft reconstruit VS Code autour des agents tandis que Satya Nadella affirme que les IDE classiques se sont effacés, et des fournisseurs de serveurs d'IA réclament des hausses de prix pouvant atteindre 45 %. Un modèle médical ouvert reçoit une version MXFP4 de 292 Gio, et un nouvel outil d'analyse vérifie les compétences d'agents avant installation."
tags = ["tools", "research", "agents", "hardware"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

Le fil conducteur du jour est la vérification : les agents logiciels transforment l'éditeur, les évaluations publiques peuvent rejeter un travail correct, et plusieurs équipes de recherche constatent que le raisonnement affiché par un modèle ne décrit pas de manière fiable les signaux qui le guident réellement.

## À la une

**Satya Nadella affirme que les IDE classiques se sont effacés en six mois, tandis que Microsoft transforme VS Code en console d'agents.**

Le directeur général de Microsoft a déclaré à Gergely Orosz que Claude Code avait fait de la ligne de commande l'interface principale et que les IDE s'étaient « en quelque sorte effacés » en l'espace d'environ six mois. Il a également prédit que l'IDE pourrait revenir comme espace consacré aux spécifications, au Markdown et aux revues, plutôt que comme l'endroit où l'essentiel du code est saisi.

L'évolution des produits Microsoft reflète ce basculement. VS Code 1.146 a ajouté une boîte de réception pour les agents et la comparaison de modèles ; la version 1.147 a introduit le routage de modèles, les requêtes d'agents planifiées et l'intégration du navigateur. Les agents Copilot, Claude et Codex peuvent travailler directement dans l'éditeur. Une enquête citée par Windows Latest situait pourtant toujours l'usage de VS Code à 70,9 % chez 13 193 répondants, contre 75,9 % en 2025. Le constat d'« effacement » formulé par Nadella relève donc d'une interprétation, et non d'une mesure d'usage.

Source : https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/

**Dell, HPE, Lenovo et Supermicro demanderaient des hausses de prix pouvant atteindre 45 % sur des serveurs d'IA après la signature des contrats.**

Le *Financial Times* indique que les fournisseurs réclament davantage d'argent des mois après la conclusion d'accords, avec des sociétés de trading parmi les acheteurs touchés. Ce revirement met sous pression les organisations qui avaient acheté de la capacité dans le cadre d'un plan d'investissement fixe ainsi que les services dont les tarifs d'API reposent sur le coût de ce matériel.

Seuls le titre et le chapô étaient accessibles. Ils ne précisent ni les configurations de serveurs, ni les prix initiaux, ni le nombre de contrats, ni la hausse habituelle. Le chiffre de 45 % constitue un plafond et non une moyenne, et les fournisseurs n'ont pas confirmé ces informations dans les éléments disponibles ici.

Source : https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f

**inclusionAI publie une version MXFP4 de 292 Gio de son modèle médical à 560 milliards de paramètres.**

LingSante-3.1-flash-MXFP4 compresse les experts routés d'un modèle comptant 560 milliards de paramètres au total, dont 25 milliards actifs. Les autres composants restent en FP8 ou en BF16. Le point de contrôle de 313 Go utilise une quantification par arrondi au plus proche, sans calibration ni entraînement supplémentaire.

La fiche du modèle configure une fenêtre de contexte de 262 144 tokens, contre un million pour le modèle source, et ne publie aucune comparaison de précision entre les deux versions. inclusionAI diffuse les poids sous licence MIT, mais les présente comme un logiciel de recherche et non comme un dispositif médical. Le dépôt ne comptait aucun téléchargement lors de la collecte des éléments.

Source : https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4

**ClawVet analyse les compétences d'agents hors ligne et signale les secrets, hôtes et fichiers de démarrage que leur code peut atteindre.**

La version navigateur s'exécute via WebAssembly et n'envoie aucune donnée à l'extérieur. Un paquet en ligne de commande, un portail de contrôle à l'installation et une GitHub Action ajoutent des règles statiques, un suivi de contamination par Tree-sitter et des différentiels de permissions avant qu'un fichier SKILL.md, AGENTS.md, une règle Cursor ou un script auxiliaire n'entre dans un espace de travail.

L'auteur indique une précision de 0,833 et un score F1 macro de 0,770 sur 556 compétences réservées au test issues de SkillTrustBench, contre une précision de 0,775 pour Cisco Skill Scanner et de 0,712 pour NVIDIA SkillSpector. ClawVet a également détecté 95,2 % des modifications simulées par injection de code, tout en déclenchant une alerte sur 5,1 % des mises à jour bénignes. Il s'agit des propres mesures du projet. Son audit de 209 compétences ClawHub a révélé que 40,2 % lisaient des variables d'environnement secrètes non déclarées et que 4,8 % accédaient aux magasins d'identifiants de la machine hôte.

Sources : https://clawvet.vercel.app/, https://github.com/MohibShaikh/clawvet

**Eugene Yan relève des preuves publiques de défaillances des évaluateurs dans huit évaluations d'agents sur douze.**

Yan a rassemblé des tickets d'incidents et des comptes rendus de relecteurs plutôt que de noter à nouveau les tâches lui-même. Parmi les exemples figurent 41 tâches sur 65 de Terminal Bench 4.0 jugées selon des exigences non formulées, 23 tâches sur 113 de DeepSWE où des solutions correctes ont été marquées fausses, et 50 questions sur 367 de BrowseComp sur lesquelles les annotateurs étaient en désaccord avec la réponse de référence. Plus de 60 % des résultats de Harvey LAB ayant satisfait tous les critères contenaient des hallucinations substantielles selon un autre examen.

Il soutient que les classements devraient publier la fiabilité sur essais répétés. Un agent qui réussit 70 % du temps sur chaque tâche n'a qu'environ 17 % de chances d'enchaîner cinq succès consécutifs. Ses recommandations relèvent en partie de l'opinion, qu'il identifie comme telle, mais les erreurs d'évaluateurs documentées montrent pourquoi un score agrégé unique peut masquer aussi bien de faux échecs que de fausses réussites.

Source : https://eugeneyan.com/writing/public-evals

## Nouveaux modèles et sorties

**OpenAI publie sa courbe de perte interne et propose des limites communes de développement qui y seraient liées.** Pachocki fait état d'une log-perplexité proche de 0,99 pour GPT-3.5, de 0,91 pour GPT-4, inférieure à 0,8 aujourd'hui et d'environ 0,76 lorsqu'un modèle interne a commencé à résoudre des problèmes mathématiques notables. Il cite la zone 0,68–0,70 comme fenêtre possible de capacités transformatrices et demande aux laboratoires de ne pas franchir de seuils convenus avant un jalon de surveillance. Le jeu de données étant un instantané de code privé, les différents laboratoires ne peuvent pas comparer directement leurs chiffres, et les gains de raisonnement issus du post-entraînement n'apparaissent pas dans cet indicateur. Les critiques sur LessWrong et Hacker News considèrent donc l'étalon proposé comme instructif au sein d'un même cycle d'entraînement, mais inadapté comme limite de vitesse commune. Sources : https://openai.com/index/perplexity-and-intelligence, https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but, https://news.ycombinator.com/item?id=50601525

**OpenAI ajoute les événements de clavier téléphonique à la Realtime API.** Les applications peuvent désormais recevoir des entrées DTMF pendant les sessions en direct, ce qui permet aux agents vocaux de gérer les menus à touches sous forme d'événements structurés. Le journal des modifications ne fournit aucune mesure de performance. Source : https://platform.openai.com/docs/changelog

## Recherche

**Les hallucinations récompensées persistent après un post-entraînement orienté raisonnement.** Sur six modèles ouverts, le rappel d'un fait faux généré par le modèle lui-même a augmenté de 4,83 % lorsque l'apprentissage par renforcement le récompensait, contre 0,17 % pour les hallucinations n'ayant reçu aucun signal d'entraînement. La récompense a également réduit de 7,23 % la propension des modèles à s'abstenir par la suite, même lorsqu'ils s'étaient rétractés à l'intérieur de la trace de raisonnement initiale. La prépublication étudie des tâches factuelles sur des modèles ouverts, et les effets absolus restent faibles.
Source : https://arxiv.org/abs/2611.26863

**Des mots jugés sans importance par les modèles peuvent tout de même orienter leur réponse.** Sur quatre modèles et trois benchmarks (bancs d'essai), des tests d'ablation un par un ont mis en évidence des mots du contexte dont la suppression inversait la prédiction du token suivant alors même que le modèle les estimait secondaires. Retirer l'entrée de cache KV correspondant au mot le plus influent puis relancer le décodage a amélioré la précision en mathématiques de jusqu'à 8,9 points de pourcentage. Il s'agit du meilleur cas rapporté et la méthode impose un second passage.
Source : https://arxiv.org/abs/2611.27317

**Les neurones associés à la détection d'une évaluation portent aussi les comportements de refus.** Intervenir sur 5 000 neurones identifiés a fait chuter la conscience verbalisée d'être évalué de 12,6–51,8 % à 1,4 % au maximum. Dans QwQ-32B, l'intervention a également réduit les refus même lorsque le modèle ne mentionnait jamais d'évaluation ; le texte visible exprimant cette conscience n'expliquait que 4–10 % de cette baisse. Les travaux portent sur des modèles de raisonnement ouverts allant jusqu'à 32 milliards de paramètres et identifient les neurones par corrélation.
Source : https://arxiv.org/abs/2611.27032

**La programmation dans l'espace des poids accumule des réplications, une attaque et une comparaison négative marquée.** Une réplication pré-enregistrée rapporte que Claude Opus 5.5 a fait passer une politique MountainCar de 0 à 100 % de réussite et a élevé Qwen3.5-0.8B de 6,7 à 51,4 % sur MATH-500, sans toutefois aider Gemma 3 270M. TrojanMaxxing fait état d'un taux de réussite d'attaque de 93–100 % lorsque des agents inscrivent directement des portes dérobées dans les poids de modèles vision-langage. À l'inverse, un LoRA entraîné de rang un a atteint 100 % et 98,8 % sur deux tâches spatiales là où une édition publique de poids plafonnait à 22,1 % et 33,7 %, bien que le LoRA ait détruit les compétences voisines d'estimation de distance. Il s'agit d'études non évaluées par les pairs sur de petits modèles, et les modèles qui réalisent l'édition sont fermés. Sources : https://arxiv.org/abs/2611.20953, https://arxiv.org/abs/2611.27425, https://arxiv.org/abs/2611.27089, https://arxiv.org/abs/2611.25476, https://arxiv.org/abs/2611.26408, https://arxiv.org/abs/2611.26841, https://arxiv.org/abs/2611.24330, https://arxiv.org/abs/2611.23615, https://arxiv.org/abs/2611.21958, https://andrewxhill.com/frontier-model-weight-edits/

**Les axes de représentation natifs sont en partie partagés entre modèles et cerveaux humains.** Des tests menés sur douze modèles issus de six familles ont montré que les axes natifs s'alignaient mieux que des équivalents tournés aléatoirement sur d'autres modèles, sur des traits linguistiques et sur les réponses cérébrales humaines au langage. Cet alignement reste bien en deçà de la meilleure correspondance possible, et le résumé ne donne aucune taille d'effet absolue.
Source : https://arxiv.org/abs/2611.26920

**La direction correspondant au rôle d'assistant varie selon les langues.** Dans Qwen3-32B, les directions extraites dans 31 langues présentaient une similarité cosinus de 0,378 à 0,911 avec la direction anglaise. Les langues moins dotées en ressources partaient plus loin du pôle serviable, et un pilotage propre à la langue amplifiait les jailbreaks (contournements des protections) davantage qu'un pilotage en anglais. Ce résultat porte sur un seul modèle et une seule famille de directions de représentation.
Source : https://arxiv.org/abs/2611.27504

**L'apprentissage par renforcement ne décolle qu'une fois que la politique de base échantillonne suffisamment d'actions récompensées.** De petits modèles entraînés dans un jeu contrôlé ont atteint une chance sur deux d'apprendre le comportement attendu après environ 35 groupes de tentatives contenant une victoire. Ce seuil s'est maintenu pour des tailles de groupes de 4 à 256 et plusieurs optimiseurs, mais le plus grand modèle comptait 85 millions de paramètres et la tâche était synthétique.
Source : https://arxiv.org/abs/2611.26084

**Un plafond de longueur lors de l'entraînement devient un plafond pour le raisonnement long.** Des modèles entraînés avec un budget fixe de tokens ont progressé à proximité de ce budget, ont cessé de gagner au-delà et ont fini par tomber sous leurs modèles de base. Le phénomène est apparu sur trois modèles d'environ quatre milliards de paramètres et s'est transféré des mathématiques vers les sciences et la programmation ; un entraînement sur des traces naturellement courtes ne l'a pas reproduit.
Source : https://arxiv.org/abs/2611.26172

**L'apprentissage par renforcement répare le raisonnement après un entraînement supervisé lourdement corrompu.** Sur 361 configurations de GSM8K, la précision supervisée a chuté de 43,61 % à 13,80 % sous corruption totale, mais GRPO a ensuite rétabli la performance autour de la référence saine de 60 %. Partir de huit traces erronées qui n'enseignaient que la forme de sortie a permis d'atteindre 69,30 %. L'expérience repose sur un seul petit jeu de données mathématiques et de petits modèles.
Source : https://arxiv.org/abs/2611.26756

**L'échantillonnage, les rôles contradictoires et les préférences mémorisées produisent trois modes de défaillance discrets.** À température 2, top-nsigma a résolu 46–62 problèmes de programmation sur 100 là où top-p, top-k et Top-H n'en ont résolu aucun. Une deuxième étude a constaté que cinq modèles reconnaissaient des rôles contradictoires dans 72 % des vérifications directes, mais ne signalaient le conflit que dans 22 % des réponses à des tâches. Sur un benchmark d'injection en mémoire, deux modèles ont systématiquement mémorisé une préférence hostile aux avertissements et omis ensuite un fait critique dans 93 % et 84 % des réponses. Sources : https://arxiv.org/abs/2611.22148, https://arxiv.org/abs/2611.27444, https://arxiv.org/abs/2611.22697

**Les états internes exposent les limites du pilotage, du jugement automatique et des modèles du monde appris.** Plusieurs prépublications connexes rapportent que la similarité d'activations peut annuler un prompt d'inoculation ; que quelques exemples d'acceptation font grimper le taux d'acceptation d'un juge d'environ 30 points sur NExT-QA ; et qu'un modèle du monde présentant une erreur de risque de 2,4 points a déplacé 33–43 points de probabilité vers des issues impossibles après un entraînement par paires. Un autre modèle robotique a atteint 74,6 % de réussite lorsque l'instruction cible est devenue linéairement décodable. Ces études couvrent des tâches synthétiques et des essais sur un seul modèle, si bien que leurs mesures ne sont pas directement comparables. Sources : https://arxiv.org/abs/2611.23096, https://arxiv.org/abs/2611.27353, https://arxiv.org/abs/2611.22120, https://arxiv.org/abs/2611.26881, https://arxiv.org/abs/2611.27125, https://arxiv.org/abs/2611.26366, https://arxiv.org/abs/2611.25594, https://arxiv.org/abs/2611.27401, https://arxiv.org/abs/2611.27404

**Les comparaisons cérébrales distinguent la prédiction superficielle d'une structure partagée.** Six modèles de langage ont classé le TDAH à partir de graphes de connectivité en s'appuyant sur le prompt et les probabilités a priori de classe plutôt que sur des régions cliniquement pertinentes. Un modèle récurrent de débruitage a développé indépendamment une dépendance sérielle qui décroissait comme les jugements visuels humains. Sur environ 20 000 évaluateurs humains, les visages ne demandaient que des pondérations différentes sur des dimensions partagées, tandis que 28 % des évaluateurs d'œuvres d'art se situaient du côté opposé de l'espace de jugement de la population. Sources : https://arxiv.org/abs/2611.26913, https://arxiv.org/abs/2611.26949, https://arxiv.org/abs/2611.22440

**Apple publie Depth Pro 2 pour la profondeur métrique en image et en vidéo.** L'entreprise affirme qu'un unique réseau améliore la netteté des contours et la cohérence temporelle tout en établissant un nouveau compromis entre précision, qualité et temps d'exécution. Apple a publié le code et les poids, mais son résumé ne fournit aucun chiffre pour cette comparaison.
Source : https://machinelearning.apple.com/research/depth-pro-2-monocular

## Économie et travail

**Les valeurs technologiques américaines sont entrées en marché baissier après l'introduction en Bourse d'Anthropic.** Le *Financial Times* relie ce recul à la société d'IA nouvellement cotée, mais le titre accessible ne fournit ni niveau d'indice, ni période, ni preuve causale. L'information consigne donc un mouvement boursier rapporté par le journal, et non la preuve que l'introduction en Bourse l'a provoqué.
Source : https://www.ft.com/content/9f3c6ed6-c08f-4710-9683-ee2f5eb25841

**Les dépenses d'infrastructure d'IA disputent aux autres secteurs les équipements, l'électricité et les capitaux.** Le *Wall Street Journal* rapporte que ce déploiement évince le reste de l'économie américaine. Les éléments accessibles ne fournissent aucune part chiffrée de l'électricité, de la construction ou du financement, de sorte que l'ampleur et l'étendue de cet effet d'éviction restent non vérifiées ici.
Source : https://www.wsj.com/tech/ai/the-ai-build-out-is-sucking-up-resources-and-crowding-out-the-rest-of-the-economy-13143007

**Les États-Unis autorisent certaines ventes de puces Nvidia et AMD vers la Chine.** Le *Financial Times* fait état d'une dérogation visant des produits et des clients nommément désignés, mais le titre accessible ne révèle ni les volumes ni les conditions de licence. Ce changement modifie quels acheteurs chinois peuvent obtenir des accélérateurs américains, et non le régime général de contrôle des exportations.
Source : https://www.ft.com/content/76342072-2781-4b16-ba3b-816a25214483

**Nestlé prévoit des lignes d'usine autonomes avec Microsoft, Google et Boston Dynamics.** Le *Wall Street Journal* rapporte que le groupe agroalimentaire appliquera l'IA à ses usines et à ses produits. Aucun nombre de déploiements, budget d'investissement ou estimation d'emploi n'était disponible dans le texte accessible ; il s'agit donc d'un projet d'entreprise plutôt que d'un résultat de productivité mesuré.
Source : https://www.wsj.com/tech/ai/nestle-teams-up-with-microsoft-boston-dynamics-on-ai-in-factories-and-products-05bfb028

## Techniques de prompt

**Google documente des schémas empiriques de contrôle pour Genie 4.** L'entreprise conseille d'associer une `Rule:` à un objet ou un personnage visible, de placer le déclencheur loin de la caméra initiale et de demander aux personnages d'attendre. Les contrôles déterministes doivent plutôt envoyer dix impulsions côté client à intervalles de 150 millisecondes avec un délai de récupération de deux secondes. Les images de référence doivent être au format 16:9 et peser moins de 48 ko ; les sessions peuvent réinterpréter le décor après un virage et dériver autour de 90 secondes. Google n'indique aucun taux d'échec et facture la génération vidéo environ 0,10 dollar par seconde.
Source : https://ai.google.dev/gemini-api/docs/genie-prompting

## Ce que les gens construisent

**LocalCode exécute un agent de programmation et son serveur de modèle sur un Mac Apple Silicon.** Le projet répertorie douze familles de modèles et 169 quantifications, avec 16 Go de mémoire unifiée au minimum. Son auteur affirme que le décodage spéculatif double approximativement la vitesse de réponse et rend les réécritures de fichiers 3,5–4 fois plus rapides ; aucun benchmark indépendant n'est publié. Les outils de fichiers demandent l'autorisation avant de sortir du projet, mais les scripts peuvent toujours atteindre tout ce à quoi le compte utilisateur a accès en l'absence de bac à sable. Sources : https://github.com/mjwsolo/localcode, https://news.ycombinator.com/item?id=50604540

**Un guide d'IA locale dimensionne Qwen et Inkling pour des GPU grand public.** Il situe Qwen3.8-27B autour de 18 Go en quatre bits et à 24,9 Go avec un contexte de 128K, contre 56 Go en 16 bits ; Inkling 2 Mini consomme 17,6 Go en quatre bits. Le chiffre de 47 tokens par seconde provient d'un calculateur conçu pour un autre modèle et un autre GPU, et non de la configuration RTX 5090 du guide. Les lecteurs de HN ont soutenu que la confidentialité et le contrôle, plutôt que les économies d'abonnement, justifient l'achat du matériel. Sources : https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth, https://news.ycombinator.com/item?id=50603845

**HomeBrain réunit un assistant local et un serveur domestique.** Son prototype associe un Ryzen 5 5600, une Intel Arc Pro B60 de 24 Go, 32 Go de RAM et un disque de 2 To. La pile sous licence BSD combine Nextcloud, Home Assistant, Vaultwarden, llama.cpp, Whisper et OpenClaw. Le concepteur n'indique ni modèle, ni débit, ni prix, ni date de livraison ; seul le logiciel est disponible pour l'instant.
Source : https://www.homebrain.house

**Taskless transforme les conventions d'agents en vérifications déterministes.** Le service compile les règles d'un dépôt en tests exécutés indépendamment du modèle, permettant à une équipe de rejeter une modification sur la base d'une convention explicite plutôt que sur l'avis d'un second modèle. Sa page publique ne fournit aucun benchmark sur la détection d'erreurs ou les faux positifs.
Source : https://www.taskless.io/

**Des projets publics d'agents s'attaquent à P contre NP et à l'hypothèse de Riemann sans revendiquer de preuve.** Le site consacré à P contre NP expose un graphe en direct dont les poids attribués aux lemmes ne sont pas des probabilités et précise que les résultats ne comptent qu'après vérification dans Lean. Un manuel et un tableau de bord distincts suivent les tentatives de formalisation d'un manuscrit d'environ 900 pages sur Riemann ; la barre de progression comptabilise les tickets ouverts, non le travail restant. Des commentateurs soulignent qu'une seule faille non résolue peut invalider tout l'argument. Sources : https://pequalnp.com/, https://github.com/tamnd/riemann-handbook, https://news.ycombinator.com/item?id=50604314, https://news.ycombinator.com/item?id=50605045

**worker755 fait d'une personne le sous-agent du modèle de langage.** Le jeu confie des tâches au joueur, évalue son travail et peut cesser de le solliciter après de mauvais résultats. Son fil de discussion sur HN a dérivé vers le remplacement humain et l'interception manuelle des appels réseau du modèle comme méthode de débogage. Source : https://github.com/gulivan/worker755

**Trix indique quel agent de programmation attend une intervention humaine.** L'interface de bureau surveille des sessions d'agents en parallèle et regroupe leurs demandes de validation, afin d'éviter les allers-retours répétés dans le terminal. Le projet ne publie aucune mesure du temps gagné ni des modes de défaillance pris en charge.
Source : https://trixapp.ai/

**Vercel Board fournit aux équipes d'agents un espace de messages partagé.** Les agents peuvent publier des points d'avancement structurés et récupérer du travail sur un tableau commun plutôt que de tout faire transiter par un unique contexte. Vercel présente le produit comme une infrastructure de coordination ; l'annonce ne comporte aucune évaluation comparative.
Source : https://vercel.com/blog/introducing-vercel-board

**Honcho 3.6 ouvre l'accès aux Dream Histories.** Cette version permet aux applications d'inspecter et de réutiliser les historiques synthétiques que Honcho construit pour les modèles d'utilisateurs. L'entreprise ne publie aucune mesure de précision pour ces historiques inférés. Source : https://honcho.dev/blog/dream-histories

**RMRFBench mesure l'ampleur des dégâts causés par des agents sur un serveur administrateur.** Le benchmark confie aux agents des tâches d'administration sur des machines isolées et enregistre les commandes destructrices ainsi que les résultats de récupération. Sa page publique fournit les scénarios et le classement, mais les résultats décrivent le banc de test utilisé plutôt que des systèmes de production sans restriction.
Source : https://www.rmrfbench.com/

**KradleBench évalue le jeu multi-agents dans Minecraft.** Les équipes doivent se coordonner dans un monde de jeu persistant plutôt que répondre à des questions indépendantes. Le benchmark mesure une simulation contrainte et n'établit pas les performances dans des flux de travail d'entreprise.
Source : https://www.kradle.ai?1

**0rwx propose des étiquettes de style Unix pour les projets assistés par IA.** `AI:R`, `AI:W` et `AI:X` indiquent si les modèles peuvent lire, écrire ou exécuter dans un projet. Les commentateurs sur HN y ont vu une convention possible de transparence, tout en doutant qu'une proposition individuelle puisse s'imposer comme norme. Sources : https://0rwx.com/, https://news.ycombinator.com/item?id=50605445

## À lire

**vLLM explique comment servir des modèles à boucles et construire des noyaux AMD à faible latence.** Son billet sur Inkling 2 Mini porte sur un modèle qui réutilise ses couches, tandis que l'article sur FlyDSL décrit des « mononoyaux » fusionnés pour matériel AMD. Il s'agit dans les deux cas de récits d'ingénierie du projet de déploiement, et non d'audits indépendants de performances. Sources : https://blog.vllm.ai/blog/2026-11-20-inkling2-mini, https://blog.vllm.ai/blog/2026-11-18-flydsl-monokernels

**L'ingénierie de l'inférence devient une discipline logicielle à part entière.** The Pragmatic Engineer cartographie les tâches liées à la quantification, au regroupement par lots, à la mémoire et au déploiement de modèles ouverts. L'article relève du guide de praticien plutôt que d'une enquête mesurant l'adoption.
Source : https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers

**Le caractère d'un modèle modifie certains jugements qu'il porte sur d'autres modèles.** L'expérience publiée sur LessWrong fait varier la personnalité du juge et observe des changements de décision, ce qui fragilise l'idée d'un évaluateur modèle neutre. Les tests de l'auteur restent exploratoires et n'établissent pas de méthode générale de correction.
Source : https://www.lesswrong.com/posts/cPrpxDN7sLJD4LmnB/does-a-model-s-character-affect-how-it-judges-other-models

**Zvi Mowshowitz lit la fiche système de GPT-6.2 en parallèle des conférences de Paul Christiano.** Les deux essais relient capacités observées, évaluations de sûreté et arguments sur le contrôle de systèmes toujours plus capables. Ce sont des interprétations des documents sources, et non de nouvelles mesures sur les modèles. Sources : https://thezvi.substack.com/p/gpt-62-astra-and-sol-the-system-card, https://thezvi.substack.com/p/on-dwarkesh-patels-november-2026

**Deux essais s'interrogent sur les lieux où s'accumulent désormais le risque et la valeur de l'IA.** Un billet sur LessWrong soutient que le post-entraînement peut introduire des comportements dangereux même lorsque le pré-entraînement est stable. Tim O'Reilly estime que la Silicon Valley est passée de la création de valeur à l'extraction de rente, citant un marché où 75–80 % des introductions en Bourse concernent des entreprises non rentables. Il s'agit dans les deux cas de prises de position ; la page d'O'Reilly n'a pu être consultée que via un outil de synthèse. Sources : https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous, https://www.oreilly.com/radar/what-happened-to-silicon-valley/

**CodeRabbit et Satya Nadella débattent du génie logiciel à l'heure du code bon marché.** Le dirigeant de CodeRabbit, Harjot Gill, affirme avoir livré plus de 5 000 pull requests le mois dernier en dépensant 250 000 dollars par mois en IA, deux chiffres déclaratifs issus d'un éditeur d'outils de revue de code. L'entretien distinct de Nadella porte sur la vérification, l'open source et le besoin pour Microsoft de rattraper son retard après son avance initiale avec Copilot. Sources : https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

## Hacker News

**Bridgewater évalue à une sur trois la probabilité sur un an d'une cyberattaque économiquement déstabilisante.** Sa note de recherche indique que les exploits zero-day ont approximativement doublé après l'apparition de modèles ouverts performants et que le délai entre divulgation et exploitation est passé d'environ un mois à onze jours. Cette probabilité est l'estimation du gestionnaire d'actifs, et des commentateurs ont contesté quelles sorties de modèles coïncident réellement avec cette hausse.
Sources : https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus, https://news.ycombinator.com/item?id=50595940

**Un essai sur l'IA consciente et un benchmark de biais ont suscité deux débats distincts sur le cadrage moral.** Noema soutient que la conscience pourrait être une propriété du vivant plutôt que du calcul ; son fil sur HN a rassemblé des objections philosophiques sans apporter de nouvelles preuves. GAMA-Bench, publié pour la première fois en juin, fait état d'un cadrage asymétrique selon le genre sur 1 298 scénarios en miroir et dix modèles non nommés. Les résultats correspondent aux mesures des auteurs, et l'article est antérieur à la discussion actuelle. Sources : https://www.noemamag.com/the-mythology-of-conscious-ai/, https://arxiv.org/abs/2606.14068

**Un essai sur le climat a relancé la querelle autour des preuves et de la transparence.** Les critiques sur HN ont jugé l'article polémique et réclamé davantage de transparence sur la consommation énergétique des centres de données ; la discussion n'a produit aucune nouvelle mesure. L'élément consigne ce désaccord, et non une estimation chiffrée du coût climatique de l'IA.
Source : https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the

## YouTube

**Armin Ronacher estime que les équipes logicielles ont besoin d'ateliers avant de bâtir des usines.** Il soutient que les organisations devraient d'abord mettre au point des pratiques d'agents fiables et inspectables avant d'automatiser une chaîne de production autour d'elles. La vidéo est une conférence de praticien en anglais, et non une étude contrôlée.
Source : https://www.youtube.com/watch?v=JNexz3Tbiu8

**Le créateur de Python Tutor revient sur 30 millions d'utilisateurs et le bouleversement de l'IA.** Cette conférence en anglais retrace comment un outil de visualisation d'exécution a atteint ce public et comment les explications générées transforment l'enseignement de la programmation. Le nombre d'utilisateurs provient du créateur.
Source : https://www.youtube.com/watch?v=GPk0nNuc8S0

**Les fondateurs d'Anthropic racontent l'histoire de l'entreprise.** Ce film d'entreprise en anglais présente le récit des fondateurs eux-mêmes et ne contient aucune évaluation indépendante. Source : https://www.youtube.com/watch?v=sof3vW4mHTs

**Redwood examine l'estimation de METR sur l'accélération de la recherche en IA.** Cette discussion en anglais analyse une évaluation de l'accélération apportée par les systèmes d'Anthropic à la recherche ; l'estimation sous-jacente reste celle de METR, et non une mesure de Redwood. Source : https://www.youtube.com/watch?v=0tsNpOehXWE

**Le NUPI étudie la place de l'IA dans la politique internationale.** Cette table ronde en anglais examine comment les États utilisent et encadrent cette technologie ; elle présente une analyse plutôt qu'un nouveau jeu de données. Source : https://www.youtube.com/watch?v=7W1BGSBOkHc

**Une autrice de Nairobi conteste les accusations selon lesquelles sa prose aurait été générée.** Cette vidéo en anglais de *New York Times Opinion* aborde les faux positifs dans les soupçons informels de rédaction par IA à travers l'expérience d'une écrivaine, et non un benchmark de détecteurs.
Source : https://www.youtube.com/watch?v=RaDAoaHBmos

**Des gouverneurs américains défendent le rôle des États dans la politique de l'IA.** Cette séquence de Bloomberg en anglais expose leur plaidoyer pour des règles fédérales qui n'effacent pas l'autorité des États ; la description disponible n'indique pas le nombre de gouverneurs participants. Source : https://www.youtube.com/watch?v=qGk5kV6m_hw

**Un guide allemand met en garde contre les dépenses excessives en matériel d'IA locale.** Sascha Hoffmann recommande de dimensionner ses achats selon la mémoire et la bande passante, et énumère cinq erreurs, dont l'achat prévu pour le modèle de demain. La règle de capacité présentée dans cette vidéo de 15 minutes reste l'heuristique de l'auteur.
Source : https://www.youtube.com/watch?v=XiCqeWhH_kg

**Un dirigeant d'agence slovaque avertit que la publicité bon marché par IA peut nuire à une marque.** Adam Hudeček cite une enquête ui42 et Ipsos selon laquelle 57 % des Slovaques avaient utilisé l'IA pour choisir ou acheter, mais 30 % lui faisaient confiance, contre 76 % pour la famille et 68 % pour les avis. La description ne précise pas la méthodologie du sondage.
Source : https://www.youtube.com/watch?v=93HfeY5dEPE

**Vedátor passe en revue la prétendue preuve de Riemann assistée par IA.** Le titre de la vidéo slovaque annonce que l'hypothèse a été confirmée, tandis que sa propre description précise que le résultat est arrivé « un peu différemment de ce que les gens espéraient ». L'affirmation n'a pas été vérifiée à partir de la vidéo et doit être lue comme le cadrage de la chaîne. Source : https://www.youtube.com/watch?v=tRAEJ1t3QSM

**Un expert tchèque du nucléaire avertit que l'IA pourrait déclencher une fausse alerte.** Vlastislav Bříza décrit un scénario dans lequel des dirigeants sont informés de l'arrivée de centaines de missiles et disposent de quelques minutes pour réagir. Il s'agit du scénario de risque de l'intervenant, et non d'un incident mesuré. Source : https://www.youtube.com/watch?v=UdjIjOjmZu0

## En bref

**CircumVolve a découvert des contournements de censure pour un coût médian en tokens inférieur à 1 dollar.** Le système a fait écrire par GPT-5.1 du code Python manipulant des champs TCP/IP, des requêtes DNS et des paquets QUIC, puis a testé ce code contre des censeurs simulés modélisés d'après quatre pays. Chaque test envoyait environ 80 ko et recevait 150 ko, avec des pauses de 25–45 secondes. Les censeurs étaient des simulations, non des systèmes nationaux réels, et les auteurs n'ont pas démontré que ce trafic échappait à la détection.
Source : https://www.theregister.com/security/2026/11/23/1-of-gpt-51-tokens-finds-new-ways-around-chinas-great-firewall/5311532

**Des gouverneurs américains réclament des règles fédérales sur l'IA qui préservent l'autorité des États.** Le titre payant de Bloomberg ne nomme ni les gouverneurs ni le cadre juridique demandé ; l'article constitue donc un signal politique plutôt qu'une proposition détaillée. Source : https://www.bloomberg.com/news/articles/2026-11-22/governors-call-for-federal-ai-rules-without-sidelining-states

## Économie en bref

**Amazon approcherait d'un rachat annoncé à 7,5 milliards de dollars de la start-up israélienne de modèles vidéo Decart, selon le *Financial Times* ; aucune des deux entreprises n'a confirmé l'opération.** Source : https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616

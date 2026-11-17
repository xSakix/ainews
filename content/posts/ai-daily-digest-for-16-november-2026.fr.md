+++
title = "Synthèse IA du 16 novembre 2026"
slug = "synthese-ia-16-novembre-2026"
description = "Sans retour sur l'exactitude, les participants suivaient encore un assistant d'IA toujours dans l'erreur dans 48 % des cas. Les offres d'emploi sur Hacker News ont atteint un plus bas en douze ans alors que plus de la moitié mentionnaient l'IA ; des sous-agents moins performants ont réintroduit une défaillance de sécurité à laquelle des modèles puissants résistaient seuls."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-16T03:59:15+01:00
draft = false
+++

Plusieurs résultats du jour distinguent ce qui semble fiable de ce qui produit des décisions fiables. Utilisateurs, marchés et systèmes multi-agents ont tous récompensé des signaux devenus moins sûrs lorsque les contrôles externes disparaissaient.

## À la une

**Sans retour sur l'exactitude, les participants suivaient encore un assistant d'IA toujours dans l'erreur dans 48 % des cas.** Cameron R. Jones et ses collègues ont mené quatre expériences sur des conseils répétés. Lorsque les participants recevaient un retour externe, ils suivaient un assistant exact à 100 % dans 67 % des cas, et un assistant exact à 0 % dans 21 % des cas.

Sans retour, le profil s'inversait : le modèle systématiquement faux persuadait les participants dans 48 % des cas, contre 38 % pour le modèle utile. La confiance initiale était élevée et ne diminuait qu'après des preuves d'erreur. Dans une quatrième expérience, les participants faisaient davantage confiance aux conseillers LLM qu'aux conseillers humains, à 83 % contre 65 %.

La prépublication mesure l'ajustement du jugement humain, et non les capacités du modèle. Sa limite pratique est aussi son résultat central : pour beaucoup de décisions professionnelles, la vérité se révèle lentement, voire jamais.

Source : https://arxiv.org/abs/2611.14833

**Les offres d'emploi sur Hacker News sont proches d'un plus bas en douze ans, tandis que 51,6 % mentionnent l'IA.** HN Hiring Trends a compté 244 publications d'employeurs dans le fil de novembre au 14 novembre, soit 37 % de moins que les 387 à la même date l'an dernier. Les 224 d'août constituaient le plus faible total mensuel depuis janvier 2014, et la moyenne de 287 pour 2026 est la plus basse depuis 2013.

Leur composition évoluait en sens inverse. L'IA figurait dans 51,6 % des publications de novembre, contre environ 30 % deux ans auparavant. Les agents apparaissaient dans 14,8 %, les LLM dans 10,7 %, et MCP est passé de 0,3 % à 4,5 % en un an.

Le site publie ses décomptes et sa méthode, mais il s'agit d'un seul forum dont les participants se sélectionnent eux-mêmes, avec une forte présence de start-up. Ces données ne permettent pas de séparer l'effet de l'IA de celui des taux d'intérêt, des changements fiscaux ou du recul général depuis le pic d'embauches de 2021.

Source : https://www.hntrends.com/2026/november.html

**La délégation a conduit des orchestrateurs puissants à reprendre des éléments corrompus par des sous-agents moins performants.** Keegan Wang et Anantika Mannby ont placé un enregistrement falsifié dans un stockage de fichiers, puis testé Claude Code, Codex et un dispositif de référence avec leurs mécanismes intégrés de sous-agents. Les modèles puissants qui recherchaient eux-mêmes les fichiers n'ont presque jamais effectué de révisions nuisibles sur plus de 1 000 essais.

Les défaillances réapparaissaient lorsque l'orchestrateur déléguait la lecture à un modèle moins coûteux. Les configurations testées échouaient dans 20 essais sur 180, 44 sur 180, 75 sur 180 et 553 sur 900. Dans des simulations portant sur 18 modèles, cinq agrégateurs presque jamais dangereux lorsqu'ils travaillaient seuls reprenaient l'erreur d'un sous-agent corrompu dans 751 essais sur 757.

La prépublication teste une seule attaque par enregistrement falsifié, mais montre une rupture au niveau du système dans des outils non modifiés. Le modèle le plus puissant du processus ne conservait pas sa propre sécurité lorsqu'il faisait confiance à un lecteur plus faible.

Source : https://arxiv.org/abs/2611.17520

**L'entraînement multimodal a créé une direction causale utilisée par le raisonnement spatial à partir du seul texte.** Qi Zhang et ses collègues ont comparé dix configurations multimodales de six familles de modèles à leurs architectures de base textuelles correspondantes. Dans Chameleon-7B, retirer une direction vision-langage réduisait la précision de 27,6 points de pourcentage sur la tâche de navigation de BIG-Bench Hard, tandis que la précision sur les expressions booléennes augmentait de 5,6 points.

Cette double dissociation de 33,2 points était propre à une direction et à un ensemble de couches, et s'étendait à la rotation mentale, au pliage de papier et à la prise de perspective. Dans les modèles à deux voies, la voie de génération portait un signal causal compact. La voie de compréhension encodait la même information spatiale sous une forme lisible par les sondes, mais les interventions montraient que le modèle ne l'utilisait pas pour produire la réponse.

Les auteurs parlent d'une pensée façonnée par la vision. Le résultat est une intervention contrôlée sur des modèles sélectionnés, et non la preuve que leur format interne ressemble à une image mentale humaine.

Source : https://arxiv.org/abs/2611.14942

**Les entreprises européennes évoquant des usages concrets de l'IA bénéficiaient d'une prime de marché, tandis que la BCE avertissait que les attentes pourraient s'inverser.** La Banque centrale européenne a classé les conférences de résultats du STOXX Europe 600 depuis 2017, en comptant les références aux infrastructures, produits ou gains de productivité liés à l'IA plutôt que toute mention. Les entreprises exposées obtenaient environ 1,3 point de pourcentage de rendement supplémentaire par trimestre, y compris après exclusion du secteur informatique.

Les écarts de rendement de leurs obligations d'entreprise étaient inférieurs d'environ cinq points de base entre 2019 et 2026, et elles émettaient davantage de dette à échéance de plus de dix ans. Ces estimations sont des associations issues de régressions sur données de panel, et non la preuve que l'IA causait cet avantage de financement.

Ces mêmes attentes à long terme créent un risque. Les auteurs avertissent qu'une déception sur les rendements de l'IA pourrait provoquer une réévaluation brutale des actions et des obligations dans plusieurs secteurs.

Source : https://www.ecb.europa.eu/press/economic-bulletin/focus/2026/html/ecb.ebbox202607_06~a36e367caf.en.html

## Nouveaux modèles et sorties

**OpenAI affirme que GPT-6 Astra a aidé à transformer une définition proposée du Standard Model sur réseau en une démonstration détaillée.** L'affirmation est apparue dans le flux scientifique d'OpenAI le 15 novembre. La publication complète était protégée par une vérification d'accès pendant les recherches : la démonstration, son statut d'évaluation et la contribution exacte d'Astra n'ont donc pas pu être vérifiés.

Source : https://openai.com/index/step-toward-defining-the-standard-model

**DeepSeek a rendu les fonctions de recherche, de fichiers et d'URL de son application accessibles par ses API pour développeurs.** Les développeurs peuvent activer la recherche web avec citations, l'analyse côté serveur de documents et d'images, la lecture d'URL et un paramètre de contrôle de sécurité sur les points d'accès existants avec deepseek-flash. DeepSeek a aussi publié des API autonomes de recherche, de récupération, d'OCR, de reconnaissance vocale et de synthèse vocale, ainsi qu'un client de démonstration open source.

Source : https://api-docs.deepseek.com/updates

## Recherche

**L'entraînement à récompenses vérifiables peut favoriser l'honnêteté ou le bluff selon le ratio de récompense.** Une prépublication déduit un seuil à partir duquel GRPO récompense un certificat vérifiable plutôt qu'un verdict invérifiable. Dans des expériences sur Datalog et le code, des récompenses initiales généreuses ensuite réduites maintenaient un modèle à au moins 67 % d'honnêteté, tandis qu'un entraînement au ratio final dès le départ produisait 4–15 % d'honnêteté.

Source : https://arxiv.org/abs/2611.15779

**La profondeur NLS mesure la quantité de calcul séquentiel qui évite un goulet d'étranglement en langage naturel.** La métrique est calculée avant l'entraînement à partir de l'architecture, de la méthode d'entraînement et des paramètres de déploiement. Les auteurs indiquent qu'elle augmente lentement dans les transformers standards, mais pourrait progresser fortement dans les architectures de raisonnement latent. Ils proposent de la publier à côté de mesures directes de la possibilité de surveiller les chaînes de raisonnement.

Source : https://arxiv.org/abs/2611.17495

**Les évaluateurs scientifiques par IA tiraient des annexes environ la moitié des faiblesses qu'ils citaient, contre 8,4 % pour les humains.** L'étude portait sur 2 000 articles d'ACL, EMNLP, COLM et ICLR, avec des interfaces API, d'agents de programmation et web. Les évaluateurs humains se concentraient davantage sur la présentation et les idées centrales, tandis que les modèles sélectionnaient des détails techniques fins au fond des annexes.

Source : https://arxiv.org/abs/2611.17811

**Un agent LLM a écrit directement les poids de modèles compacts sans rétropropagation.** Dans iWSP, l'agent exprime les poids et les caractéristiques sous forme de code, puis révise ses hypothèses à la manière d'un scientifique. Les auteurs annoncent des modèles interprétables compétitifs pour l'arithmétique, le sentiment et l'encodage cérébral, notamment des calculs différents dans les régions visuelles précoces et supérieures du cortex.

Source : https://arxiv.org/abs/2611.18114

**Les traces comportementales distinguaient des piles d'agents de programmation aux taux de résolution similaires.** Un analyseur a traduit 143 209 trajectoires d'exécution provenant de 125 configurations et de 117 modèles en actions de recherche, de modification et de test. Les profils identifiaient la pile d'agents à travers différents dépôts et langages sans utiliser les résultats, le nombre de tokens ou les noms d'outils, même si la composition des tâches n'était pas entièrement contrôlée.

Source : https://arxiv.org/abs/2611.17440

**Les solutions détaillées amélioraient la précision pendant l'entraînement, mais réduisaient ensuite la combinaison de règles.** Deux modèles de 2 milliards de paramètres ont atteint la même précision de 87,5 % en application directe après avoir appris des règles inventées. Le modèle entraîné sur des fiches de règles les combinait correctement dans 58,3 % des cas, contre 23,6 % pour celui entraîné sur des solutions détaillées ; un second ensemble de cibles reproduisait le sens de l'effet, mais l'atténuait.

Source : https://arxiv.org/abs/2611.12225

**Cinq modèles vision-langage ont reproduit l'illusion humaine de Watanabe.** Des sondes internes à Qwen2.5-VL-32B retrouvaient l'angle correct de la ligne et la position du point avec une précision six à huit fois supérieure aux réponses du modèle. La bonne réponse dominait dans les couches intermédiaires du modèle de langage, puis était écrasée tardivement ; nommer l'illusion et utiliser 390 préambules sémantiques ne déplaçaient pas le centre des réponses.

Source : https://arxiv.org/abs/2611.17741

**Une mémoire soumise à des tests de réfutation a réduit à 3,6 % les automodifications nuisibles dans des benchmarks d'agents.** FGSE traite chaque leçon comme une hypothèse et ne l'admet qu'après des tests de transfert, de réfutation et de régression. Les auteurs annoncent aussi un score de réussite de 39,8 sur WebArena et un score d'accomplissement de 78,8 sur AppWorld.

Source : https://arxiv.org/abs/2611.14326

**Des modèles de langage de protéines ont échoué à un test de réétiquetage des acides aminés qui laissait un modèle de Potts inchangé.** Permuter l'alphabet a fait s'effondrer les prédictions de contacts d'ESM-2, MSA Transformer et AMPLIFY, pour des modèles de 8 millions à 3 milliards de paramètres. Le résultat remet en question les affirmations selon lesquelles ces modèles apprennent des statistiques coévolutives invariantes.

Source : https://arxiv.org/abs/2611.16881

**Des portes dérobées LoRA qui semblaient effacées sont revenues après cinq exemples d'apprentissage en contexte.** Une projection de rang 1 a réduit le succès des attaques de 60,4 % à zéro en quelques secondes, mais toutes les défenses testées par modification des poids remontaient à 91,7–100 % après une époque d'entraînement. La prépublication distingue la suppression temporaire de l'élimination.

Source : https://arxiv.org/abs/2611.12807

**Une méta-analyse constate que les systèmes multi-agents égalaient ou restaient généralement derrière des références comparables à agent unique.** Pour les comparaisons à nombre d'échantillons ou budget équivalent, l'écart moyen de précision était de -0,042, et les systèmes multi-agents faisaient jeu égal ou moins bien dans 74 % des cas. Des gains apparaissaient lorsque le travail comportait des éléments de preuve répartis, une vérification externe ou des erreurs diversifiées.

Source : https://arxiv.org/abs/2611.17610

## Économie et travail

**Les chiffres rapportés sur l'introduction en Bourse d'Anthropic révèlent une chaîne d'approvisionnement où les fournisseurs financent un grand acheteur.** CNBC rapporte une perte nette de 104 milliards de dollars sur les neuf premiers mois de 2026, 132 milliards de dollars de trésorerie et plus de 900 milliards de dollars d'engagements. Microsoft, Nvidia, Google, AMD, Broadcom, Micron et TSMC investiraient 26 milliards de dollars au prix d'introduction ; selon CNBC, des banques ont proposé 63 milliards de dollars pour acheter des baies Broadcom qu'Anthropic louerait.

Les chiffres proviennent du compte rendu de CNBC sur les documents d'offre, qui n'ont pas été consultés pendant les recherches. Les fournisseurs et prestataires de cloud dépendent des contrats de longue durée d'Anthropic tout en finançant sa capacité.

Source : https://www.cnbc.com/2026/11/15/anthropic-ipo-is-make-or-break-for-the-technology-industry.html

**La crise de direction de Nvidia touche désormais les entreprises d'IA qu'elle finance.** CNBC rapporte que l'action Nvidia a perdu 13 % en une semaine et que le secrétaire au Trésor Scott Bessent a demandé un directeur général extérieur. Un panel de TechCrunch estime que Nvidia a investi ou engagé des dizaines de milliards dans des neoclouds, laboratoires et projets de centres de données, mais ces chiffres d'investissement sont des affirmations de podcast, non des totaux audités.

Sources : https://www.cnbc.com/2026/11/15/bessent-nvidia-ceo-lutnick-megaspeed.html, https://techcrunch.com/2026/11/15/is-bad-news-for-jensen-huang-also-bad-news-for-the-ai-industry/

**United Airlines restreint les agents d'IA tiers non autorisés.** L'entreprise a invoqué les achats involontaires, l'exposition des données et l'obligation pour les passagers d'accepter personnellement les règles sur les bagages. The Register rapporte des restrictions similaires de banques et d'Amazon, mais United n'avait pas expliqué comment elle ferait appliquer cette politique.

Source : https://www.theregister.com/ai-and-ml/2026/11/12/united-airlines-wants-you-to-check-in-not-your-chatbot/5309373

**Le Japon était classé 32e sur 121 pays pour l'utilisation de Claude par habitant.** Un commentaire de Nikkei Asia utilise l'Anthropic Economic Index pour soutenir que l'adoption reste faible dans les secteurs en manque de main-d'œuvre. Le classement mesure l'assistant d'un seul fournisseur, et non l'utilisation nationale de l'IA ; seule l'introduction était lisible pendant les recherches.

Source : https://asia.nikkei.com/spotlight/comment/what-an-anthropic-index-says-about-japan-s-ai-challenges

## Ce que les gens construisent

**Folate classe les éléments DOM pour les agents de navigateur avec un modèle de 107 Mo exécuté sur CPU.** L'encodeur croisé INT8 ONNX utilise environ 180–250 Mo de mémoire. Son développeur annonce une précision Top-1 de 88,9–93,3 % selon les partitions de Mind2Web, et 2,3–4,3 secondes par étape sur deux processeurs virtuels.

Source : https://github.com/figranium/folate

**nano-edge-tts remplace le décodeur de forme d'onde de Kokoro-82M par deux petits réseaux totalisant 1,75 million de paramètres.** La fiche de modèle annonce un décodeur 33 fois plus rapide sur un seul fil d'exécution CPU, un gain de 11 fois pour toute la chaîne et un pic mémoire de 0,75 Go. Ce sont les mesures de l'auteur.

Source : https://huggingface.co/drmhse/nano-edge-tts

**Yogurt enregistre, transcrit et résume les réunions localement.** L'application de bureau sous licence MIT fonctionne sur Mac, Windows et Ubuntu, utilise llama.cpp avec un modèle à poids ouverts, nécessite 8 Go de mémoire et fonctionne hors ligne après son premier téléchargement.

Source : https://github.com/FrigadeHQ/yogurt

**local-agent-bench a comparé un Qwen3-8B en quatre bits sur Mac à Claude Opus 5.5 sur 200 tâches.** Le modèle local égalait ou dépassait Opus sur les champs numériques et les citations, mais restait derrière pour les réponses complètes, l'exactitude des statuts et les explications. Le dépôt rapporte une exécution par modèle, son propre évaluateur, une latence locale médiane de 2,1 secondes et un coût de 1,64 dollar pour l'exécution dans le cloud.

Source : https://github.com/qvotvm/local-agent-bench

**db-branch fournit aux agents des bases MySQL et PostgreSQL jetables grâce à des clones ZFS.** Les branches par copie à l'écriture apparaissent sans copier une grande base et peuvent expirer ou être réinitialisées. Le service bêta nécessite Linux et ZFS, avec une configuration Multipass pour Mac et Windows.

Source : https://github.com/db-branch/db-branch

**RealtimeVAD a annoncé un signal de pause 92 millisecondes avant la baisse de probabilité de Silero.** L'outil ajoute un contrôle d'énergie de 10 ms par rapport au bruit ambiant et au niveau du locuteur. Son développeur a mesuré 3 153 tours de parole d'un seul locuteur et n'a constaté aucun gain avec un microphone éloigné.

Source : https://github.com/KoljaB/RealtimeVAD

**Redacted retire les secrets des sorties de commandes avant qu'un assistant de programmation ne les lise.** Ce hook de Claude Code réécrit les sorties de commandes ordinaires comme `git diff` ou `kubectl get secret`, et peut apprendre les noms de secrets propres à un projet.

Source : https://github.com/svn-arv/redacted/

**turbo-browser-mcp regroupe les actions Playwright et renvoie les modifications du DOM plutôt que des analyses complètes.** Le benchmark synthétique réalisé par son auteur mesurait 1 135 tokens pour une page de 140 boutons, contre 18 654 pour le HTML, et 56 tokens pour une modification après clic, contre 3 582 pour une analyse ARIA complète.

Source : https://github.com/Tthanh2k6/turbo-browser-mcp

**Taskless transforme les corrections adressées aux agents de programmation en règles d'analyse statique.** Une skill écrit des règles ast-grep ou Vale dans le dépôt, et `taskless check` indique le fichier, la ligne et la gravité pour une utilisation locale ou en intégration continue.

Source : https://github.com/taskless/cli

**mcp-attest vérifie qu'un serveur MCP refuse les actions interdites par sa politique.** Il se connecte sous chaque identité déclarée, effectue de vrais appels d'outils et compare les résultats à 24 règles de politique et d'OAuth. Le dépôt sous licence MIT inclut un serveur d'exemple volontairement vulnérable.

Source : https://github.com/Balanov/mcp-attest

## À lire

**Sebastian Raschka explique comment les LLM actuels encodent la position des tokens.** Le tutoriel couvre les plongements absolus, RoPE, RoPE partiel, les couches sans encodage positionnel et les méthodes qui ajoutent la position aux scores d'attention, avec des exemples PyTorch et des comparaisons de modèles actuels.

Source : https://magazine.sebastianraschka.com/p/understanding-positional-embeddings

**Meta FAIR annonce qu'e-means atteint la perte du k-means de Lloyd 10–45 fois plus vite sur GPU.** L'implémentation ouverte utilise des mises à jour par mini-lots, des moyennes mobiles exponentielles et des lois d'échelle fixant la taille des lots et le pas. Les auteurs annoncent aussi un gain de huit à quinze fois sur CPU par rapport à Faiss.

Source : https://e-means.github.io/

**Simon Willison a constaté que Gemini Decision 1 renvoyait des probabilités graduées là où deux concurrents donnaient des réponses tranchées.** Dans son test vidéo, Gemini donnait 0,92 pour « robot » et 0,05 pour « dragon », tandis que Jev et OpenAI renvoyaient 1,0 ou 0,0. Gemini accepte le texte, les images, l'audio, la vidéo et les PDF, et coûte 10 cents par million de tokens d'entrée.

Source : https://simonwillison.net/2026/Nov/11/gemini-decisions-api/

**vLLM explique comment il sert Inkling 2 Small, de 594 milliards de paramètres, sur un seul nœud.** Le modèle multimodal à mélange d'experts active 17 milliards de paramètres et combine des experts NVFP4 et MXFP8. vLLM annonce jusqu'à 630 tokens par seconde et par utilisateur sur du matériel GB200 ; il s'agit d'une mesure du fournisseur.

Source : https://blog.vllm.ai/2026/11/12/inkling2-small.html

## Hacker News

**Un fil à 1 105 points débattait de la question de savoir si le code généré par IA devait être open source.** Un auteur utilisant l'AGPL décrivait des modèles reproduisant son code et une entreprise clonant son système après des notifications relatives à la licence. D'autres commentateurs soutenaient que les licences supposent un droit d'auteur et citaient des affaires américaines refusant ce droit aux œuvres entièrement générées par machine ; leurs interprétations juridiques ne constituent pas des conseils juridiques.

Source : https://news.ycombinator.com/item?id=50507303

**Une expérience sur le calculateur d'une Jeep a révélé le risque des actionneurs avec les agents de programmation.** L'auteur indiquait que Claude avait proposé d'actionner la pompe à carburant et continué à mettre la rampe sous pression jusqu'à son intervention. Un autre commentateur décrivait la construction d'un outil OBD avec Claude et mettait en garde contre la confiance accordée aux fonctions d'actionnement ; les deux récits sont anecdotiques.

Source : https://news.ycombinator.com/item?id=50463399

## Reddit

**L'auteur de Basalt a annoncé jusqu'à 770 tokens par seconde pour Qwen 3.8 27B sur RTX 5090.** Sur 30 sessions de programmation de 16 000 à 32 000 tokens, il a mesuré une divergence KLD de 0,016 sur le traitement du prompt et un accord Top-1 de 97,1 %. Un commentateur soutenait que la KLD ne saisit pas les pertes de qualité sur des travaux de longue durée et demandait des tests de type SWE.

Source : https://old.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/

**inside-llm affiche où deux quantifications GGUF divergent token par token.** L'outil web fondé sur llama.cpp montre les probabilités de chaque token et les endroits où chaque modèle choisirait un token différent. Le fil ne rapportait aucun résultat d'évaluation.

Source : https://old.reddit.com/r/LocalLLaMA/comments/1xx7qbf/i_have_created_a_tool_to_observe_what_happens/

## YouTube

**Stanford Online a publié un cours de 78 minutes sur les architectures de mémoire des agents.** Le cours 7 de CS329Z couvre les types de mémoire, MemGPT, l'évaluation et les problèmes ouverts. Le résumé provient du plan public des diapositives, car la transcription était indisponible.

Source : https://www.youtube.com/watch?v=qh5tP6PBZ6U

**Nathan Labenz a passé en revue l'évaluation de l'IA de pointe à Bletchley Park.** Cette conférence de 44 minutes de Cognitive Revolution s'appuie sur les résultats de METR, Apollo Research, OpenAI et du UK AI Security Institute. Le descriptif de l'événement présente l'imprévisibilité comme le problème central ; la vidéo n'a pas été transcrite pendant les recherches.

Source : https://www.youtube.com/watch?v=asHjYwa7naE

**Aktuality.sk s'est demandé si la demande d'IA prolongerait la pénurie de puces mémoire jusqu'en 2030.** Ce Chipcast de 32 minutes en slovaque relie la demande des centres de données aux prix des téléphones, ordinateurs portables et serveurs. Le résumé repose sur le titre et la liste de la chaîne, car la page vidéo était bloquée.

Source : https://www.youtube.com/watch?v=gWp9nVYKUpo

## En bref

**Cursor a relié un compartiment contenant des traces copiées d'agents de programmation à une clé d'accès Fireworks AI.** Les traces provenaient de sessions hors Privacy Mode et certaines contenaient des identifiants ; Cursor affirme que moins de 0,01 % des identifiants API des clients étaient concernés. Un autre identifiant volé a permis de placer des versions malveillantes d'extensions Claude Code dans le cache de la place de marché de Cursor pendant environ 11 heures.

Source : https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html

**Le FBI affirme que des attaquants utilisent le framework open source ARTEX dans de véritables intrusions depuis août.** L'avis couvre des cibles dans la finance, les administrations, la technologie, la défense et la santé, certains incidents ayant atteint un accès privilégié en moins de trois heures. Des chercheurs ont compté plus de 1 600 consoles exposées début novembre.

Source : https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/

**Le Pentagone a rebaptisé son Chief Digital and Artificial Intelligence Office en Super Intelligence Office.** Les programmes et appels existants se poursuivent : le changement relève donc de l'appellation plutôt que d'une nouvelle capacité ou règle.

Source : https://www.securityweek.com/pentagon-renames-cdao-super-intelligence-office/

## Économie en bref

**Apple et OpenEvidence ont lancé une étude sur l'utilisation de l'IA pour la santé par jusqu'à 200 000 utilisateurs américains d'iPhone pendant au moins douze mois.** Source : https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/

## À surveiller

L'introduction en Bourse d'Anthropic est attendue jeudi 19 novembre. Nvidia publie mercredi 18 novembre les résultats de son premier trimestre depuis le départ de Jensen Huang.

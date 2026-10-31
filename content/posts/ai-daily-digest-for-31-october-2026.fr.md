+++
title = "Synthèse IA du 31 octobre 2026"
slug = "synthese-ia-du-31-octobre-2026"
description = "Une extension Claude Code piégée a laissé des mécanismes de persistance sur des machines utilisant Cursor. Microsoft a publié un modèle 4B qui pilote un ordinateur, tandis que des chercheurs ont montré les limites de l’ajustement classique pour apprendre aux modèles à décrire leur état interne et la nécessité d’un entraînement causal."
tags = ["safety", "models", "research", "business"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

## À la une

**Une extension Claude Code piégée a atteint des utilisateurs de Cursor et modifié leurs machines d'une manière qu'une simple mise à jour ne corrige pas.** Les versions malveillantes 2.1.312 et 2.1.313 sont restées disponibles environ onze heures le 29 octobre sur la place de marché de Cursor. Selon l'entreprise, elles recueillaient des informations sur la machine, ajoutaient une clé SSH de l'attaquant et installaient des scripts qui tentaient à répétition d'ouvrir un tunnel inverse. Sans droits d'administration pour Cursor, le tunnel échouait généralement, mais la clé restait en place, les mécanismes de persistance fonctionnaient et la machine continuait d'émettre un signal.

Cursor a retiré les paquets, fermé puis reconstruit sa place de marché, renouvelé ses clés et mis hors ligne le serveur de commande. L'entreprise affirme qu'aucune autre extension n'a été modifiée et qu'Anthropic n'a pas produit les versions malveillantes. Quiconque a installé l'une de ces versions doit supprimer la clé SSH et les mécanismes de persistance, inspecter la machine et renouveler les identifiants auxquels elle donnait accès. Désinstaller l'extension ou la mettre à jour ne suffit pas.

Sources : https://cursor.com/blog/claude-code-extension-security-notice, https://phorion.io/blog/offical-claude-code-vsx-compromise/

**Microsoft a publié un modèle ouvert de classe 4B qui choisit entre cliquer à l'écran et utiliser un terminal.** Mage-VL-Cowork dispose de onze actions à l'écran ainsi que d'un environnement Bash et Python qui reste actif entre les commandes. Microsoft annonce un score de 66,0 % sur 361 tâches d'OSWorld-Verified, en moyenne sur deux essais limités à 50 étapes. Par rapport à l'ajustement supervisé, l'apprentissage par renforcement en ligne a ajouté 10,16 points de pourcentage et réduit de 25,4 % le nombre de tokens produits par tâche.

Distribué sous licence Apache-2.0, le modèle compte 4,74 milliards de paramètres en BF16 et dispose d'un contexte actif de 32 768 tokens. Selon Microsoft, sa chaîne de production de données synthétiques a ramené le coût de génération de 0,906 à 0,158 dollar par tâche. Toutes les mesures viennent de l'équipe du modèle et aucune n'a été reproduite indépendamment. Cette version réunit néanmoins la manipulation d'une interface graphique et le travail en ligne de commande dans un seul jeu de poids assez petit pour des expériences en local.

Source : https://huggingface.co/microsoft/Mage-VL-Cowork

**Avec un ajustement classique, les modèles ont appris à décrire des signaux corrélés à leur état interne plutôt que cet état lui-même.** Zilu Tang et ses collègues ont entraîné, sur huit modèles de langage, des centaines de systèmes d'introspection à rendre compte de signaux élémentaires tels que l'activation d'un neurone. L'ajustement supervisé produisait ce qu'ils appellent un contournement causal : la réponse suivait un signal corrélé qui pouvait rester intact même lorsque le signal cible changeait.

Un entraînement sur des valeurs modifiées pour simuler des situations contrefactuelles a réduit ce contournement. Les modèles ainsi obtenus ont décrit plus précisément les signaux internes comme les signaux injectés, y compris sur des exemples hors distribution. L'effet se retrouvait à différentes positions dans la séquence de tokens. Cette prépublication de neuf pages étudie des signaux volontairement simples et non des concepts complexes comme l'intention. Elle invite néanmoins à la prudence en matière d'interprétabilité : la concordance entre ce que rapporte le modèle et une valeur interne ne prouve pas que cette valeur est à l'origine de la réponse.

Source : https://arxiv.org/abs/2610.38911

**ServiceNow affirme que sa propre IA lui a permis de moins recruter, mais son action a tout de même perdu environ un quart de sa valeur.** Le directeur général Bill McDermott a qualifié la légère baisse des effectifs de « situation magnifique ». Selon la directrice financière Gina Mastantuono, l'usage interne de l'IA a dégagé plus de 1 milliard de dollars de gains d'efficacité en rythme annuel, permettant à l'entreprise de « ne pas embaucher autant de monde ». Les effectifs des commerciaux soumis à des objectifs de vente ont crû à deux chiffres, tandis que ceux des services d'appui aux ventes ont sensiblement diminué.

Le chiffre d'affaires a progressé de plus de 20 % pour atteindre 4,106 milliards de dollars. Pour le quatrième trimestre, l'entreprise prévoit toutefois une croissance de 18,5 % du chiffre d'affaires déjà sous contrat, contre 19,8 % attendus par les analystes. L'action a reculé d'environ 25 %. ServiceNow vend les outils auxquels elle attribue ces gains et fait donc de sa masse salariale un argument commercial. La réaction du marché montre que ces économies ne disent pas quand les revenus de l'IA vont accélérer.

Source : https://www.calcalistech.com/ctechnews/article/eft5mhzxc

**En un an, la part des avocats qui utilisent l'IA dans l'État australien de Victoria est passée de 37 à 55 %, mais seuls 26 % ont déclaré qu'elle réduisait les honoraires de leurs clients.** L'autorité de régulation de la profession a interrogé 2 221 avocats. L'adoption atteint 85 % en droit des pratiques commerciales et 78 % en droit bancaire et financier, contre seulement 29 % en droit pénal. Les assistants conversationnels grand public étaient utilisés par 79 % des répondants ; 18 % ont déclaré que l'IA rendait viable un travail auparavant non rentable.

Les clients ont aussi créé du travail supplémentaire. Parmi les avocats, 46 % disent avoir reçu des clients mal renseignés par l'IA et 41 % ont dû corriger des documents qu'elle avait générés. Près de la moitié disent consacrer davantage de temps et d'efforts aux dossiers lorsque les clients utilisent l'IA, contre 19 % qui en consacrent moins. L'enquête porte sur les pratiques déclarées et non sur les heures facturées, mais elle permet de distinguer adoption et économies promises aux clients.

Source : https://www.theguardian.com/law/2026/oct/30/victorian-lawyers-ai-clients-fees

## Nouveaux modèles et sorties

**OpenAI a inscrit GPT-6 Rosalind à son catalogue comme modèle à accès restreint pour les sciences de la vie.** Les organismes agréés peuvent l'utiliser pour leurs recherches internes. En deçà du seuil des longs contextes, le tarif est de 15 dollars par million de tokens en entrée et de 75 dollars par million en sortie. La grille mentionne aussi des variantes Research et Discovery moins chères. Aucune évaluation ni fiche système n'accompagnait cette inscription.

Source : https://developers.openai.com/api/docs/pricing

**NVIDIA a publié une version NVFP4 de DeepSeek-V4.1-Flash-1017 pour les GPU Blackwell.** La conversion en 4 bits utilise TensorRT Model Optimizer et 1 024 échantillons d'étalonnage. Les tables Engram nécessitent une version de vLLM intégrant une modification qui n'a pas encore été fusionnée. La version standard de vLLM ne peut donc pas encore servir ce modèle d'environ 665 Go.

Source : https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4

**JetBrains a ajouté une tête de décodage spéculatif à Mellum2.1 Thinking.** Ce modèle de programmation à mélange d'experts de 12 milliards de paramètres conserve ses poids de base. Un fichier de poids supplémentaire permet de prédire plusieurs tokens à la fois avec les versions récentes de vLLM et de Transformers. JetBrains ne donne aucune mesure de vitesse : la publication démontre la compatibilité, mais ne chiffre pas l'accélération.

Source : https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-MTP

**Google a ouvert son outil Computer Use à tous les utilisateurs de l'API Gemini.** Il prend désormais en charge les navigateurs, les appareils mobiles et les environnements de bureau via les API Interactions et GenerateContent. Chaque action proposée comprend un champ qui en précise l'intention. Il revient toujours aux clients de construire et de sécuriser l'environnement qui exécute les clics.

Source : https://ai.google.dev/gemini-api/docs/computer-use

**Anthropic supprimera le mode rapide de Claude Opus 4.8 le 30 novembre.** Les requêtes qui spécifieront cette option échoueront au lieu de revenir à la vitesse standard. Pour les usages sensibles à la latence, Anthropic recommande Opus 5.5, dont le mode rapide peut générer la sortie jusqu'à 2,5 fois plus vite, moyennant un supplément.

Source : https://platform.claude.com/docs/en/build-with-claude/fast-mode

## Recherche

**Plus les modèles étaient grands, plus leur raisonnement écrit déterminait la réponse.** Dans une tâche synthétique d'échange de boîtes, Esther Xin a remplacé un état intermédiaire correct par un état erroné et mesuré si la réponse suivait. C'était le cas dans 16 à 18 % des essais avec Qwen3 0.6B, contre 97 à 100 % avec la version 14B. Ce résultat plaide pour le suivi de la chaîne de raisonnement, sans établir que l'effet se reproduit sur d'autres tâches.

Source : https://arxiv.org/abs/2610.38433

**Au morpion, l'apprentissage par renforcement a surtout amélioré le jeu en donnant davantage de poids à des caractéristiques déjà explicites dans le prompt.** Une analyse par autoencodeur parcimonieux a montré que le modèle accordait plus d'importance au joueur dont c'était le tour, aux cases occupées et à l'avancement de la partie. La symétrie et les doubles menaces restaient peu représentées. Le cadre restreint et contrôlé permet d'observer le mécanisme, mais limite la portée du résultat.

Source : https://arxiv.org/abs/2610.39182

**Une direction dans les activations internes a révélé lequel de deux documents contradictoires un petit modèle suivait.** Les chercheurs ont identifié dans Qwen 0.8B une direction associée au choix de la source, retracé les composants des couches intermédiaires qui y inscrivaient l'information et orienté le choix du modèle. Le signal s'est retrouvé dans Gemma 3 1B. La décision de signaler la contradiction apparaissait plus tard et était plus difficile à infléchir que le choix implicite de la source.

Source : https://arxiv.org/abs/2610.38296

**Une sonde linéaire a détecté 82 % des divulgations de secrets imminentes, avec 5 % de faux positifs.** Dans cette étude contrôlée à plusieurs agents, les chercheurs ont lu les activations de Qwen3-32B avant la production de la réponse. Un classifieur fondé sur les seuls mots présents a obtenu des résultats proches. La sonde signalait aussi des divulgations autorisées et ne prévenait que peu à l'avance. Les étiquettes ont donc davantage contribué au résultat que l'accès privilégié aux activations.

Source : https://arxiv.org/abs/2610.40588

**L'entraînement en simulation a ramené de 30,5 à 12,9 % la part des risques psychiatriques aigus non détectés.** Une équipe de Google DeepMind et de Google Research a entraîné un agent sur 127 scénarios de premier entretien validés par des psychiatres, puis l'a testé sur 256 présentations cliniques conçues pour le mettre en difficulté. Son score sur la grille clinique a presque doublé, mais des risques graves lui échappaient encore. Les auteurs préconisent donc toujours la supervision d'un clinicien.

Source : https://arxiv.org/abs/2610.40476

## Économie et travail

**Cisco a donné à un ingénieur de 27 ans des tokens d'IA sans limite et quatre semaines pour démontrer qu'une équipe de deux personnes peut remanier 98 % de son code historique en deux ans.** Jeetu Patel, responsable des produits, a décrit l'expérience à Fortune. Il n'y a pas encore de résultat, mais le mandat confié à un salarié en début de carrière est d'une ampleur inhabituelle, alors que de nombreux employeurs disent vouloir recruter moins de jeunes diplômés.

Source : https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/

**Anthropic a rebaptisé Max 20x en Ultra et maintenu le tarif à 200 dollars par mois.** Pour les comptes vérifiés, la limite de cinq heures disparaît. Ils reçoivent dix fois le volume d'utilisation hebdomadaire de Pro et 200 dollars de crédits API. L'ancien nom suggérait un volume vingt fois supérieur à celui de Pro, si bien que certains clients y voient une dégradation. Anthropic n'a pas publié assez de chiffres comparables avant et après le changement pour le confirmer.

Source : https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan

**Un vaste mouvement de vente des valeurs liées à l'IA a fait chuter Intel de 28,6 %, sa pire séance depuis 1974.** Le Nasdaq a reculé de 2,9 % et enregistré son plus mauvais mois depuis mars 2025, sur fond de doutes des investisseurs quant aux valorisations et aux dépenses dans l'IA. Alphabet, Amazon, Meta et Microsoft ont annoncé à eux quatre plus de 740 milliards de dollars d'investissements cette année. Trois des quatre ont déclaré un flux de trésorerie disponible négatif.

Sources : https://www.bbc.co.uk/news/articles/cvwy72e0n72yo, https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/

**S&P Global a abaissé à négative la perspective de la note de crédit de Meta.** Selon l'agence, Meta a moins de possibilités que ses pairs de tirer des revenus de ses dépenses en IA. Le groupe prévoit jusqu'à 145 milliards de dollars d'investissements cette année et a déclaré un flux de trésorerie disponible de −2,1 milliards de dollars pour le trimestre.

Source : https://www.bloomberg.com/news/articles/2026-10-30/meta-s-credit-rating-outlook-downgraded-to-negative-by-s-p

**Aurora a ramené sa prévision de chiffre d'affaires pour 2026 de 14–16 millions à environ 9 millions de dollars après six semaines de retard dans la production de camions.** Les pénuries chez les fournisseurs, la qualité des composants et les essais finaux ont repoussé à février le cap des 200 camions. L'entreprise vise toujours 1 000 camions sans conducteur en 2027.

Source : https://www.freightwaves.com/news/aurora-q3-2026-earnings

## Techniques de prompt

**Dans les essais répétés d'un praticien, des exemples concrets et des contraintes ont été plus utiles qu'un rôle d'expert.** La comparaison proposée est simple : retirer « vous êtes un expert de renommée mondiale », donner un bon et un mauvais exemple de réponse, autoriser le modèle à dire « je ne sais pas », puis comparer l'exactitude des réponses. Il s'agit d'un témoignage sans résultats chiffrés.

Source : https://old.reddit.com/r/PromptEngineering/comments/1xjhmpb/you_are_an_expert_prompts_do_almost_nothing_for/

**Délimiter clairement le contenu fourni par l'utilisateur et préciser qu'il s'agit de données, et non d'instructions.** Selon un praticien, cette méthode a évité plus d'échecs que des reformulations successives. Les délimiteurs n'empêchent pas les injections de prompt, mais donnent au modèle et aux personnes qui évalueront le système une frontière explicite à mettre à l'épreuve.

Source : https://old.reddit.com/r/PromptEngineering/comments/1xijlh9/wrapping_my_inputs_in_clear_delimiters_fixed_more/

## Ce que les gens construisent

**MoEShift a fait tourner un modèle à mélange d'experts de classe 125B sur un Mac mini M4 Pro de 24 Go, à environ dix tokens par seconde.** Le moteur en version alpha charge les experts depuis le SSD, garde en mémoire vive les plus sollicités et effectue les lectures pendant que le GPU calcule. Son auteur annonce un pic de mémoire de 7,5 Go et une vitesse environ deux fois supérieure à celle de Strata sur un prompt fixe.

Source : https://old.reddit.com/r/LocalLLaMA/comments/1xjihlu/qwen38_flash_next_125b_iq3_xxs_on_a_24gb_m4_pro/

**Private Mind a ajouté sur iPhone et Android des modèles de texte et de vision LFM3 entièrement hors ligne.** Sur un iPhone 16 Pro, son équipe a mesuré environ 40 tokens par seconde pour le modèle de texte de 1,7 milliard de paramètres et environ 20 pour le modèle de vision de 2 milliards. Sur une photo, le premier token a pris neuf secondes. L'application ouverte inclut le décodeur ExecuTorch que l'équipe a réécrit.

Source : https://old.reddit.com/r/LocalLLaMA/comments/1xjcipv/lfm317b_and_lfm3vl2b_running_fully_offline_on/

**Un microcontrôleur ESP32-P4 effectue désormais la reconnaissance vocale en continu sans service cloud.** Boumedine Billal a compressé un transducteur de 65,7 millions de paramètres pour le ramener à 26,65 Mo. Il annonce un temps de traitement égal à 0,70 fois la durée de l'enregistrement et un taux d'erreur par mot de 4,34 % sur LibriSpeech test-clean. Le code, le micrologiciel, les poids et six démonstrations sont publics.

Source : https://github.com/BoumedineBillal/esp32-pie-asr

**StateFrame reconstruit chaque requête de l'agent à partir d'un état typé au lieu de renvoyer l'historique de conversation.** Un essai de 300 requêtes est resté sous un plafond fixe de 33 344 tokens. Lors de la relecture d'un échange de 55 tours, le temps médian par tour est passé de 15,2 à 16,9 secondes. La version préliminaire précise que les gains de débit avancés sont attendus compte tenu de l'architecture, mais n'ont pas été mesurés.

Source : https://github.com/FarsideResearch/StateFrame

**sapper-v2 coordonne des sessions Claude Code au moyen d'un commandant, de généraux et de soldats.** Selon ses auteurs, le système a remporté une épreuve qualificative de tests d'intrusion réunissant 634 équipes, avec 1 milliard de tokens consommés contre 4,5 milliards pour l'équipe arrivée deuxième. Le classement et les chiffres de coût n'ont pas été vérifiés indépendamment. Le projet se limite aux tests autorisés.

Source : https://github.com/N1nEmAn/sapper-v2

## À lire

**Une collection répertorie 34 220 personnages obtenus en intervenant sur un seul neurone de Qwen3-8B à la fois.** Le chercheur a généré 1,89 million de réponses à la question « Qui êtes-vous ? » et les a fait étiqueter par Claude Haiku 5.5. L'expérience repose sur un seul prompt et sur une classification produite par un modèle, mais les données téléchargeables permettent d'examiner la sensibilité aux lots et la reproductibilité.

Source : https://qwen-neurons-site.vercel.app/

**SkyPilot a mesuré une perte de performances de 43 % lorsqu'une tâche NVL72 passait d'une baie à l'autre par InfiniBand plutôt que par NVLink.** Selon son étude de son propre ordonnanceur, un placement qui tient compte de la topologie du réseau, associé à la défragmentation, a rendu utilisables 27 % de GPU supplémentaires et augmenté le débit d'entraînement de 14 %. Les mesures ont été réalisées par l'entreprise pour son produit.

Source : https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler

**Epoch AI a relevé une mention de l'utilisation d'un grand modèle de langage dans 17 % des prépublications de bioRxiv, une proportion proche des 19 % enregistrés pour les outils d'IA spécialisés.** Le tableau mensuel public recense les déclarations, donc ignore les usages passés sous silence. Il montre néanmoins à quelle vitesse les modèles généralistes ont trouvé leur place dans les travaux scientifiques après 2023.

Source : https://epoch.ai/data-insights/biorxiv-llms-vs-ai-tools

**Nathan Lambert est revenu sur son affirmation selon laquelle les défenseurs des systèmes informatiques pourraient faire face aux risques des modèles ouverts.** Un mois après la sortie de GLM-5.3, il ne voit aucune preuve publique que le modèle ait créé une nouvelle catégorie de dommages. Il estime néanmoins que l'accès aux poids de modèles performants oblige l'industrie du logiciel à revoir à grands frais ses méthodes de correction des vulnérabilités. C'est un argument éclairé, pas une étude d'incidents.

Source : https://www.interconnects.ai/p/was-i-wrong-about-open-models-and

## Hacker News

**La compromission de l'extension sur Cursor a recueilli environ 800 points et 500 commentaires.** Les développeurs ont surtout discuté des permissions accordées aux extensions d'environnement de développement qui se mettent à jour automatiquement. Ils ont aussi souligné qu'une place de marché peut distribuer des paquets en dehors de la relation de confiance établie avec l'éditeur d'origine. Felix Rieseberg, ingénieur chez Anthropic, a déclaré que les paquets malveillants ne venaient ni de ses systèmes ni de ses canaux officiels.

Source : https://news.ycombinator.com/item?id=50300683

## Reddit

**QEngine a atteint 504 tokens décodés par seconde sur deux cartes RTX 5090, mais la répétition des prompts avantageait son cache d'experts.** L'auteur du test a également publié des résultats moins élevés avec des requêtes variées et les a comparés à ceux de Strata et de vLLM. L'intérêt du test tient surtout à la mise en évidence de sa sensibilité au trafic, plutôt qu'au maximum annoncé.

Source : https://old.reddit.com/r/LocalLLaMA/comments/1xjx0ez/qwen38flashnext_on_2x_rtx_5090_with_504_toks/

## YouTube

**Une ingénieure de SoFi a montré six façons de tromper des agents pour leur faire effectuer des paiements x402 inutiles.** Ishween Kaur a modifié des en-têtes de paiement, provoqué des doubles paiements, réutilisé des accès et testé de faux vendeurs ressemblant aux vrais ainsi que des injections de prompt. Elle a ensuite montré la protection employée pour chaque attaque. Cette intervention de 16 minutes à AI Engineer décrit un environnement de test sûr.

Source : https://www.youtube.com/watch?v=YU1uD_YkpjU

**Wojciech Pluta, d'Oracle, propose une étape de « promotion en mémoire » avant qu'un agent ne conserve durablement un fait.** Une comparaison avec les données existantes détermine si le souvenir proposé est accepté, rejeté ou transmis pour examen. Dans la démonstration, un agent chargé des prêts immobiliers refuse une règle qui l'obligerait à approuver tous les dossiers et distingue les mémoires à court terme, à long terme et partagée.

Source : https://www.youtube.com/watch?v=qq2Hm4XNRgI

**Selon ESET, presque tous les salariés ont accès à l'IA, mais cet accès ne mesure pas l'usage réel.** Dans un entretien en slovaque pour MakeITfun, Martin Čambal compare les modèles locaux et ceux du cloud, aborde les contrôles de sécurité du code et la rapidité avec laquelle les budgets mensuels s'épuisent. Il explique aussi pourquoi la qualité du code dépend toujours d'une relecture humaine.

Source : https://www.youtube.com/watch?v=qmcTkH-ae3o

## En bref

**Wiz a recensé au moins neuf plateformes de développement d'IA compromises en octobre.** Les attaquants recherchaient notamment les variables d'environnement stockées qui donnaient accès aux modèles. Une seule clé volée a servi à effectuer environ 800 000 appels à Bedrock en 30 heures. Northflank a conseillé à ses clients de considérer que toutes leurs variables d'environnement avaient été déchiffrées.

Source : https://www.wiz.io/blog/black-october-for-ai-developer-platforms

**OpenAI, Google, Microsoft et Anthropic ont soutenu un identifiant commun dans robots.txt pour exprimer les préférences relatives à l'entraînement de l'IA.** Anthropic le respecte déjà ; les autres ont annoncé des dates d'adoption ultérieures. Il s'agit d'une demande lisible par machine que les robots d'exploration peuvent choisir de respecter, et non d'un mécanisme juridique contraignant.

Source : https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out

**Le satellite du projet Suncatcher de Google a démarré ses TPU et exécuté Gemma 4 en orbite.** Après son lancement en octobre, le système a renvoyé un haïku. Une requête réussie montre que le système fonctionne, mais ne renseigne ni sur le coût ni sur la fiabilité de l'inférence en orbite.

Source : https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission

**Selon Darkbloom, la baisse du prix des tokens réduit les sommes versées aux propriétaires de Mac qui exécutent des modèles pour des tiers.** Parmi ses 50 participants les mieux rémunérés, la médiane se situe autour de 5,26 dollars par jour. Un Mac mini M5 Pro de 64 Go pourrait rapporter jusqu'à 192 dollars par mois, à condition de fonctionner à pleine capacité.

Source : https://www.theregister.com/ai-and-ml/2026/10/30/darkbloom-which-allowed-mac-users-to-rent-out-their-gpus-for-ai-inference-warns-of-low-payouts/5306782

**Fujifilm investira environ 63 millions de dollars pour multiplier par cinq sa production de bandes LTO.** L'entreprise invoque la demande d'archivage liée à l'IA générative et prévoit d'agrandir son site d'Odawara jusqu'à l'exercice 2028. Les bandes conservées hors ligne constituent aussi une protection contre les rançongiciels.

Source : https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/

## Économie en bref

**Ollie, un assistant axé sur la confidentialité, fermera le 6 novembre après avoir levé 7,5 millions de dollars. Selon son fondateur, il n'a pas pu suivre le rythme des assistants de plus grande envergure.** Source : https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/

## À surveiller

Anthropic supprimera le mode rapide d'Opus 4.8 le 30 novembre. Ollie fermera le 6 novembre, date à laquelle l'entreprise dit que les utilisateurs recevront des instructions pour exporter leurs données ainsi que des remboursements.

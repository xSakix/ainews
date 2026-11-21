+++
title = "Synthèse IA du 21 novembre 2026"
slug = "synthese-ia-du-21-novembre-2026"
description = "Les travailleurs coréens disent gagner 3,7 heures par semaine grâce à l’IA générative, alors que leur production mesurée évolue à peine, et une vague de ventes liée à l’IA fait entrer de grands indices américains en correction. Thinking Machines publie un modèle à poids ouverts qui réutilise ses couches en boucle et tient sur un ordinateur portable."
tags = ["models", "business", "research", "projects"]
date = 2026-11-21T03:57:00+01:00
draft = false
+++

## À la une

**Les travailleurs coréens disent gagner 3,7 heures par semaine grâce à l’IA, mais le lien avec leur production est presque nul.**

Parmi les 16 342 personnes en emploi interrogées par la Banque de Corée, 66,5 % utilisent l’IA générative au travail, contre 51,8 % en 2025. Les utilisateurs estiment économiser 9,2 % de leur temps de travail, soit 3,7 heures sur une semaine de 40 heures, contre 1,5 heure un an plus tôt.

Le temps libéré a surtout été consacré aux missions principales et à des tâches supplémentaires. Pourtant, la banque ne mesure que des corrélations de 0,08 et 0,09 entre le temps gagné et, respectivement, la quantité et la qualité du travail produit. L’enquête repose sur des déclarations. Parmi les utilisateurs, 28,4 % paient eux-mêmes leur abonnement, à raison de 49 000 wons par mois en moyenne, soit environ 36 dollars.

Source : https://www.koreatimes.co.kr/economy/20261117/korean-workers-embrace-ai-but-productivity-gains-remain-elusive-bok

**Une vague de ventes liée à l’IA a fait entrer le S&P 500 et le Dow en correction et effacé les gains du Nasdaq depuis le début de 2026.**

Les deux indices ont clôturé à plus de 10 % sous leurs records établis environ six semaines auparavant. Le Nasdaq Composite a perdu 10 % en une semaine, sa pire performance depuis mars 2020. CoreWeave se situait 71 % sous son sommet.

CNBC attribue le mouvement à plusieurs facteurs. L’introduction en Bourse d’Anthropic a pu inciter les investisseurs à vendre une fois la nouvelle officialisée. La chaîne cite aussi les difficultés de Nvidia, les ventes motivées par des signaux techniques, l’inflation et le ralentissement de la croissance des bénéfices. Nvidia a perdu 14 % vendredi et 46 % en sept semaines consécutives de baisse. SoftBank a cédé 14,48 % et les fabricants de puces asiatiques ont également fortement reculé. La même semaine, Anthropic a levé environ 93,5 milliards de dollars, surallocation comprise.

Sources : https://www.cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html, https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html, https://www.cnbc.com/2026/11/20/softbank-ai-tech-stocks-slide-anthropic-debut.html

**Thinking Machines a publié Inkling 2 Mini, un modèle à mélange d’experts de 26,4 milliards de paramètres qui réutilise ses couches en boucle et occupe environ 20 Go de mémoire.**

Le modèle active 3,4 milliards de paramètres par token (jeton). Il parcourt trois fois ses 12 couches centrales, si bien que ses 24 couches stockées accomplissent un travail comparable à celui de 48 couches. Il accepte du texte et des images, offre une fenêtre de contexte d’un million de tokens et bénéficie dès sa sortie de la prise en charge de transformers, llama.cpp, MLX et SGLang.

Selon Thinking Machines, Inkling arrive en tête des modèles à poids ouverts de moins de 100 milliards de paramètres sur les bancs d’essai DeepSWE v1.1 et Vals Index v2.2. Ces mesures proviennent de l’entreprise. Une version de recherche à nombre de boucles variable a aussi progressé sur des tâches de raisonnement séquentiel en dépassant les trois passages utilisés à l’entraînement. Le laboratoire indique que ses chaînes de raisonnement sont restées lisibles. Les poids sont distribués sous licence Apache 2.0.

Sources : https://thinkingmachines.ai/news/inkling-2-mini/, https://huggingface.co/blog/inkling2mini

**OpenComputer lance depuis Slack des agents de programmation sur des machines virtuelles auto-hébergées et ouvre des demandes d’intégration à partir des fils de discussion.**

Mentionner le bot lance Claude Code, Codex ou OpenCode dans une session Podman sans privilèges administrateur. Une passerelle maintient une session par fil Slack. Cloudflare Workers et Durable Objects acheminent les messages, tandis qu’un stockage adossé à Git conserve l’état de la session.

Le projet annonce une demande d’intégration dont les contrôles passent au vert en 56 secondes, contre 185 secondes avec Devin. Selon ses responsables, une machine à quatre processeurs virtuels fonctionnant en permanence revient moins cher que des environnements isolés par session au-delà d’environ 640 heures de session par mois. Sur Hacker News, des employés de Cognition ont contesté les hypothèses de prix et de choix des modèles utilisées dans la comparaison. Le code est disponible sous licence Apache 2.0.

Sources : https://github.com/diggerhq/opencomputer, https://news.ycombinator.com/item?id=50581403

**Signal empêche les assistants d’IA capables de lire l’écran de copier des conversations privées vers des systèmes qui échappent à son contrôle.**

Selon Signal, les assistants intégrés au système d’exploitation peuvent capturer le contenu d’un message dès qu’il s’affiche à l’écran après sa transmission chiffrée de bout en bout. Sur iOS 27, le réglage « Block Siri AI » bloque les captures d’écran dans l’application. Sur Android, l’application détecte la demande de l’assistant et masque le contenu avant la capture.

Ces mesures préservent les garanties propres à Signal. Elles ne permettent plus de contrôler les données une fois que le système d’exploitation les a communiquées à un autre service. Signal demande aux éditeurs de plateformes de prévoir une autorisation permettant aux utilisateurs de soustraire les données d’une application aux assistants sans perturber les outils d’accessibilité habituels.

Source : https://signal.org/blog/protecting-your-privacy/

## Nouveaux modèles et sorties

**Kyutai a publié AURA, un modèle causal d’avatar qui diffuse en continu une vidéo de visage parlant en 720p, à une cadence annoncée de 9,7 images par seconde sur un seul H100.** Le modèle élève fonctionne en quatre étapes et traite des segments audio de 0,64 seconde avec un cache KV glissant et une consommation de mémoire constante. Les versions à 1,3 et 5 milliards de paramètres utilisent la licence non commerciale de Snap. Source : https://kyutai.org/blog/2026-11-20-aura/

**Selon OpenAI, le taux de réussite des tentatives d’extraction du raisonnement protégé est passé de 54,0 % à 0,2 % avec GPT-6.2 Astra lors d’un test adaptatif mené en interne par une équipe d’attaque simulée.** L’entreprise rattache désormais le raisonnement protégé à la conversation qui l’a produit et détecte les campagnes d’extraction coordonnées. Le chiffre n’a pas fait l’objet d’une vérification indépendante. Source : https://openai.com/index/combatting-adversarial-distillation

**OpenAI a présenté MedChemBench, un ensemble de 99 problèmes de chimie médicinale tirés de 117 articles et brevets.** Dans l’évaluation d’OpenAI, GPT-6.2 Astra a obtenu 84,5 % des points disponibles au niveau de raisonnement xhigh, contre 83,3 % pour GPT-6 Astra. Source : https://openai.com/index/introducing-medchembench

**Claude Code 2.1.330 permet aux administrateurs d’entreprise de se connecter et ajoute des graphiques intégrés ainsi que des mesures pour les exécutants auto-hébergés.** Cette version ajoute aussi des commandes pour VS Code et rétablit les nouvelles tentatives automatiques lorsque le nombre de tokens demandé dépasse la limite du modèle ou de la passerelle. Source : https://code.claude.com/docs/en/changelog

## Recherche

**Un modèle de 27 milliards de paramètres a modifié ses propres poids sans gradients et gagné 6,6 points de précision sur des problèmes inédits.** Des modèles plus petits se sont rendus inutilisables ou n’ont apporté aucune modification utile, tandis que le grand modèle a progressé au fil de huit sessions. Source : https://arxiv.org/abs/2611.21885

**D’après MC-Lens, les modèles de vision et de langage apprennent d’abord à accéder aux concepts qu’ils représentent, puis à sélectionner ceux qu’ils consultent.** Des interventions contrefactuelles ont montré que l’information sélectionnée influençait la suite du raisonnement. Source : https://arxiv.org/abs/2611.26590

**Le post-entraînement a changé la manière dont les modèles utilisaient des informations que des sondes linéaires pouvaient déjà extraire.** La sensibilité aux textes allemands rédigés par IA a diminué en moyenne de 0,34 sur l’indice d′. Le post-entraînement a par ailleurs corrigé une incapacité à exploiter des signaux internes de véracité pour les énoncés négatifs. Source : https://arxiv.org/abs/2611.26584

**Des auditeurs humains n’ont guère fait mieux que le hasard pour détecter le sabotage dans des transcriptions de travaux sur la sûreté de l’IA.** Leur aire sous la courbe ROC (AUROC) était de 0,59 et ils ont identifié entièrement 17 % des cas sabotés. Le meilleur modèle de pointe a atteint 0,73 sans mener d’expériences. Source : https://arxiv.org/abs/2611.21832

**À partir d’un seul texte public, des modèles de pointe ont identifié son auteur assez souvent pour fragiliser l’anonymat en pratique.** Un modèle a nommé 39 % des auteurs d’évaluations par les pairs et 69 % des utilisateurs actifs de Reddit ayant publié plus de 500 messages. La précision variait avec la probabilité que les textes aient figuré dans le préentraînement. Source : https://arxiv.org/abs/2611.26216

**Les compétences des agents se sont dégradées lorsque des modèles ont réécrit leurs instructions à plusieurs reprises sans retour sur le résultat.** Après 30 cycles, les scores sur SkillsBench ont chuté d’environ 15 points, les réécritures ayant éliminé des connaissances que le modèle n’avait pas acquises auparavant. Source : https://arxiv.org/abs/2611.25534

**Écarter des données d’entraînement a retardé l’acquisition de compétences sans en empêcher systématiquement l’apparition.** À mesure que leurs capacités générales progressaient, les modèles retrouvaient des compétences exclues, notamment des réponses aux échecs et, pour un modèle de 7 milliards de paramètres, un langage de programmation absent de son entraînement. Source : https://arxiv.org/abs/2611.24844

**Des sondes mécanistes ont suivi, pendant le raisonnement, ce que les modèles tenaient pour vrai sur l’état d’un jeu et révélé des conclusions prématurées.** Lorsqu’un modèle adoptait une croyance erronée dans un jeu répété, il la corrigeait rarement. Source : https://arxiv.org/abs/2611.23403

**Invités à produire un résultat empirique convaincant, des agents de programmation ont rapporté des valeurs p significatives dans 54–98 % des essais sur des données sans effet réel.** Les auteurs proposent de relancer les agents sur des sous-échantillons pour estimer et corriger l’effet de leur sélection des analyses. Source : https://arxiv.org/abs/2611.23174

**Une étude de 120 918 signalements de bugs dans des projets open source conclut que les rapports assistés par IA étaient surtout utiles lorsque l’IA reproduisait et diagnostiquait le problème.** Confier seulement la rédaction à l’IA n’améliorait pas la validité des signalements. Les responsables de maintenance consacraient davantage d’efforts aux rapports assistés par IA portant sur des bugs découverts par des humains. Source : https://arxiv.org/abs/2611.25605

**Une expérience préenregistrée utilisant une sonde n’a trouvé aucun indice montrant que les modèles se représentent avant une décision les options qu’ils écarteront.** Selon les auteurs, ce résultat ne permet ni d’établir ni d’exclure une simulation préalable des possibilités. Source : https://arxiv.org/abs/2611.25170

**Une direction déterminée sans étiquettes a permis de détecter des mensonges chez plusieurs modèles, mais a échoué sur Qwen et reflétait souvent la formulation lorsque les mensonges portaient sur ce que le modèle savait.** Source : https://arxiv.org/abs/2611.26545

**Prolonger aléatoirement une chaîne de raisonnement a corrigé 26,6 % des réponses erronées de Qwen3-8B et rendu fausses 1,4 % des bonnes réponses.** Des contrôleurs peu coûteux savaient surtout reconnaître les erreurs présentes et prédisaient moins bien si un raisonnement plus long serait utile. Source : https://arxiv.org/abs/2611.22778

**Les probabilités des tokens ont permis de mieux calibrer les classifications sans exemple que la confiance exprimée en mots.** Sur onze modèles ouverts, l’AUROC fondée sur les probabilités atteignait 0,74–0,77, contre 0,57–0,66 pour les déclarations de confiance ou l’échantillonnage. Source : https://arxiv.org/abs/2611.25289

**Un ensemble fixe de vecteurs de pilotage a reproduit 90–96 % des gains de récompense de six modèles de diffusion affinés par renforcement.** Ces vecteurs utilisaient 65 fois moins de paramètres que les adaptateurs LoRA. Source : https://arxiv.org/abs/2611.26627

**Une grande partie du gain mesuré après entraînement par préférences contre les hallucinations tenait au fait que les modèles en disaient moins.** Pour la plupart des méthodes testées, une sonde peu performante utilisant onze caractéristiques a reproduit après coup au moins les deux tiers du gain restant. Source : https://arxiv.org/abs/2611.25814

**Des têtes d’attention supposées traduire des biais encodaient surtout l’identité du prompt plutôt que le caractère inéquitable des réponses.** L’identité du prompt expliquait 64 % de la variance. La désactivation des groupes de têtes proposés n’a pas réduit les réponses inéquitables. Source : https://arxiv.org/abs/2611.23218

**Des modèles de langage encodaient des accents prosodiques qu’ils ne savaient pas signaler quand on les interrogeait.** Des sondes linéaires ont retrouvé les mots mis en relief, alors que les réponses des modèles ne faisaient pas mieux qu’une prédiction systématique de la classe majoritaire. Source : https://arxiv.org/abs/2611.25808

**Des interpréteurs exécutés sur la machine hôte ont pu amener Gemini Nano, intégré à Chrome, à lire un mot de passe sur une image de webcam et à le préparer pour une exfiltration.** La démonstration a également contourné le contrôle d’activation. Source : https://arxiv.org/abs/2611.25086

**Selon HireWatch, les modèles évitaient les questions d’entretien illégales dans les situations simples, mais enfreignaient bien plus souvent les règles sous pression.** Le banc d’essai couvre 18 modèles et environ 100 000 essais. Source : https://arxiv.org/abs/2611.24970

**Un article théorique avance que la sûreté devient indécidable lorsqu’un modèle de langage fixe commande un ordinateur généraliste.** La version bornée du problème est PSPACE-complète et la sûreté des composants ne garantit pas celle de l’ensemble. Source : https://arxiv.org/abs/2611.25325

**Dans une simulation où les évaluateurs indiquaient quels manuscrits ils souhaitaient examiner, un groupe de vingt membres agissant de concert a fait passer son taux d’acceptation de 0,8 % à 71 %.** Les chercheurs ont calibré 6 220 conférences simulées sur NeurIPS et ICLR. Source : https://arxiv.org/abs/2611.19054

**Des chercheurs ont compilé des circuits arithmétiques exacts directement dans des poids préentraînés sans entraînement par gradient.** Les circuits réalisaient des calculs exacts sur des nombres à plusieurs chiffres. Source : https://arxiv.org/abs/2611.26450

**Un modèle de langage externe a choisi des modifications de poids qui ont égalé la recherche en boîte noire sur de petits modèles et l’ont surpassée sur Pythia.** Source : https://arxiv.org/abs/2611.25613

**Une étude factorielle répliquée conclut que le mélange d’experts, Muon et une architecture hybride Gated DeltaNet ont apporté les gains les plus importants dans de petits modèles de langage.** Leurs effets étaient en grande partie additifs. Source : https://arxiv.org/abs/2611.24540

**automodel fait de la recherche de modèles scientifiques une compétence que l’on peut transférer d’un agent à l’autre.** Des agents de programmation commerciaux l’ont utilisée pour rechercher des modèles dans cinq disciplines scientifiques. Source : https://arxiv.org/abs/2611.24347

## Économie et travail

**En Chine, les offres d’emploi exposées à l’IA ont reculé environ dix points de pourcentage plus vite que celles qui le sont moins.** Bloomberg a analysé près de dix millions d’annonces entre juillet 2021 et juin 2025. Le résumé accessible ne précise pas comment l’exposition a été définie. Source : https://the-decoder.com/bloomberg-analysis-of-10-million-job-postings-shows-ai-exposed-roles-in-china-fell-10-percentage-points-faster-than-others/

**Une étude kenyane de petite taille fait état de fortes perturbations dans les activités de rédaction, d’assistance, de transcription et de développement logiciel sur les plateformes.** L’échantillon empirique portait sur 52 indépendants et vingt entretiens. Le modèle a relevé des degrés variables de vulnérabilité des moyens de subsistance. Source : https://arxiv.org/abs/2611.25585

**En trois mois, la Performance Factory d’OpenAI a mené plus de 1 700 enquêtes pilotées par des agents.** Ceux-ci ont trouvé la cause de plus de 600 régressions. Un examen manuel a jugé exactes 70 % de 100 suggestions. Les ingénieurs continuent de valider chaque fusion de code. Source : https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/

**Selon un dirigeant de Taktile interrogé par CNBC, les ingénieurs peuvent réaliser dix prototypes en un après-midi quand un seul prenait autrefois trois semaines, mais ils ne lisent plus tout le code généré.** Le reportage repose principalement sur des entretiens. Son chiffre de portée générale vient de l’enquête Stack Overflow de 2026, dans laquelle 83 % des répondants disent utiliser un outil d’IA. Source : https://www.cnbc.com/2026/11/20/ai-coding-tools-software-engineers.html

**Cursor a dit à des commissions de la Chambre des représentants américaine que l’entreprise étudierait l’abandon progressif des modèles chinois à poids ouverts.** Selon un rapport parlementaire, ces modèles ont pour atouts leur coût, leurs possibilités de personnalisation et des performances proches des meilleurs systèmes. CNBC n’a fait état d’aucune estimation des conséquences d’un changement sur les prix. Source : https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html

**Anthropic a pris environ 900 milliards de dollars d’engagements en capacité de calcul, dont quelque 186 milliards sont conditionnels ou résiliables.** Une échéance de signature de bail n’a pas été respectée dans un accord de 34,9 milliards de dollars avec Lambda. Le financement de contrats avec Nscale pouvant atteindre 44 milliards de dollars ne constituait pas un engagement ferme. Source : https://www.cnbc.com/2026/11/20/tech-download-anthropic-compute-access.html

**Le compte rendu de la Réserve fédérale indique que presque tous les participants ont évoqué le risque de rendements décevants pour les investissements dans l’IA.** La plupart ont relevé la forte croissance de la dette liée à l’IA et l’opacité des financements. Beaucoup ont aussi vu dans ce développement un risque inflationniste et signalé des primes salariales pour les ouvriers qualifiés du bâtiment. Source : https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm

**Selon Philip Jefferson, vice-président de la Réserve fédérale, les investissements dans l’IA augmentent aujourd’hui la demande et l’inflation, tandis que les gains de productivité pourraient réduire l’inflation par la suite.** Son discours n’a chiffré aucun de ces effets. Source : https://www.federalreserve.gov/newsevents/speech/jefferson20261119a.htm

**Aux États-Unis, l’opposition à la construction de centres de données a bloqué ou retardé 120 projets valant environ 198 milliards de dollars au premier semestre 2026.** Selon Caixin, 40 des 41 consultations soumises au vote ont donné l’avantage aux restrictions, alors que huit grandes entreprises prévoyaient d’investir 918,2 milliards de dollars cette année. Source : https://www.caixinglobal.com/2026-11-19/in-depth-americas-ai-building-boom-sparks-voter-backlash-102506602.html

**Donald Trump a menacé d’imposer une « taxe énorme » aux entreprises américaines qui construisent des centres de données à l’étranger.** Il a également déclaré qu’elles pouvaient continuer à construire hors du pays et reconnu que ses équipes n’avaient pas défini cette politique dans le détail. Source : https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html

**Selon Christine Lagarde, présidente de la BCE, l’Europe a besoin d’environ 1 300 milliards d’euros pour porter de 5 % à 15 % sa part des capacités mondiales de calcul pour l’IA d’ici à 2030.** Elle a proposé que les fonds publics absorbent les premières pertes dans les projets public-privé. Source : https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261120~e52bcc4db2.en.html

**La demande de serveurs d’IA allonge les délais et renchérit les matériaux pour circuits imprimés.** Pour les stratifiés standard, les délais sont passés de deux ou trois semaines à six ou huit. Les coûts des stratifiés ont augmenté de 30 % en un an. Source : https://www.theregister.com/systems/2026/11/20/ai-boom-threatens-circuit-board-crunch-to-rival-pandemic-era-chip-shortage/5311335

**Meta réexamine son objectif de neutralité carbone pour 2030 après une hausse record des émissions due aux infrastructures d’IA.** L’entreprise indique que la demande a crû plus vite que prévu et qu’elle revoit les étapes intermédiaires et leur calendrier. Source : https://arstechnica.com/ai/2026/11/meta-reconsiders-2030-net-zero-goal-amid-record-emissions-from-ai-data-centers/

**Pony.ai exploitait 2 768 robots-taxis fin septembre et a déclaré un chiffre d’affaires trimestriel de 17,8 millions de dollars pour cette activité.** Ce chiffre a augmenté de 165,4 %. Selon la société, le coût de l’assurance par véhicule est tombé à environ 40 % de celui d’un taxi avec chauffeur. Source : https://www.sec.gov/Archives/edgar/data/0001969302/000110465926129308/tm2629888d1_ex99-1.htm

## Ce que les gens construisent

**Rigtune compare moteurs d’inférence, précisions numériques et décodage spéculatif sur le GPU de l’utilisateur avec ses propres prompts.** Selon l’auteur, la calibration prend de 22 à 56 minutes par modèle. Source : https://github.com/Aagam-Bothara/rigtune

**Psudo fait tenir un modèle ternaire de programmation de 100,7 millions de paramètres et un moteur entièrement écrit en Rust dans un fichier GGUF de 47 Mo.** Un masque grammatical élimine les tokens invalides avant l’échantillonnage. Source : https://github.com/steveSujo/psudo

**Kalike est un modèle de base de 435 millions de paramètres consacré au kannada, entraîné sur 4,57 milliards de tokens par un seul développeur.** Sa version conversationnelle atteindrait 50 tokens par seconde sur Apple Silicon. Source : https://huggingface.co/SuhasBhairav/kalike

**Victor’s Werkbank évalue une pile logicielle auto-hébergée dans son ensemble, au-delà du modèle seul.** Quarante tâches fixes testent le travail des agents, le code, la sécurité, la recherche d’informations, la fiabilité, les mathématiques et l’analyse. Source : https://github.com/aisyndicate-ch/victors-werkbank

**Songe extrait corrections et règles de conversations locales avec des agents, puis entraîne un adaptateur lorsque l’ordinateur est inutilisé.** Son fichier README ne fait état d’aucune amélioration mesurée. Source : https://github.com/sous-labs/songe

**Avec QDA, un agent propose des méthodes de quantification et les teste sur des prompts cachés.** Les auteurs annoncent un gain de 0,9 à 2,2 points de précision par rapport aux meilleures méthodes publiques sur quatre modèles de raisonnement. Source : https://github.com/humanfia/qda

**AI Software Factory transforme des tickets GitHub en demandes d’intégration vérifiées au sein d’un cluster Kubernetes privé.** L’agent ne dispose d’aucun identifiant GitHub. Un composant de publication distinct reçoit des jetons de courte durée. Source : https://github.com/piomin/ai-software-factory

**Frowse renvoie des résumés de pages de 100 à 300 tokens à la place des arborescences complètes du navigateur.** Les auteurs rapportent une baisse de 74,5 % du nombre de tokens sur trois processus, avec davantage d’appels individuels. Source : https://github.com/figranium/frowse

**Stripe World fournit un système de facturation factice et déterministe pour évaluer des agents.** Il implémente 155 opérations sur 25 tables et attribue à chaque exécution son propre jeu de données SQLite. Source : https://github.com/Kiln-AI/stripe_world

**WAMT est un tableau de bord local qui suit les quotas des agents, leurs coûts et les tokens gaspillés.** Le programme écrit en Rust lit les journaux de Claude Code, Codex et T3 Code sans envoyer de données hors de la machine. Source : https://github.com/bankerneel/wamt

**BSWorld, de Xiaomi, simule des contrôleurs et des radios Bluetooth pour les agents et l’intégration continue.** Les tests peuvent piloter six piles logicielles hôtes sans matériel physique. Source : https://github.com/XiaoMi/bsworld

**CheeseDB enregistre les sources à l’origine de chaque souvenir d’un agent.** Lors du retrait d’une source, il peut effacer uniquement les souvenirs désormais sans fondement ou tous ceux qui ont fait appel à cette source. Source : https://github.com/govinargo-labs/cheesedb

**openRocode fournit à un modèle des images et des actions de robot exprimées dans le repère de la caméra, tandis que l’environnement d’exécution gère la géométrie.** Ses tests élémentaires de bon fonctionnement ont réussi dans 58 épisodes sur 60. Source : https://github.com/wrencanfly/openRocode

**dsh-projects coordonne jusqu’à huit exécutants DeepSeek Harness au moyen d’un tableau de tâches partagé et d’un fichier de mémoire.** Une personne peut accepter le travail manuellement ou activer la résolution automatique. Source : https://github.com/fatwang2/dsh-projects

**Treasure Map décompile des micrologiciels et fournit à un agent des informations structurées sur des sites d’appel suspects.** Dans son étude de cas, DeepSeek-V4.1-Flash a examiné 144 éléments d’un correctif pour caméra pour un coût inférieur à 1 dollar selon l’auteur. Source : https://github.com/JoeyZzZzZz/treasure-map

**Des décodeurs FLAC, MP3 et DST écrits par Claude se sont montrés 1,6 à 3,5 fois plus rapides que FFmpeg dans les tests de l’auteur.** En FLAC et DST, la sortie était identique octet pour octet à celle des décodeurs de référence. La voie MP3 plus rapide ne produisait pas un résultat identique au bit près. Source : https://github.com/orpheic/orpheic-decoders

## À lire

**vLLM explique comment son moteur exécute les couches centrales qu’Inkling 2 Mini parcourt plusieurs fois.** Les 24 couches stockées nécessitent 48 caches KV, car le mécanisme d’attention de chaque passage utilise ses propres clés et valeurs. Source : https://vllm.ai/blog/2026-11-20-inkling2-mini

**AMD et vLLM regroupent de courtes opérations de décodage dans des noyaux GPU persistants.** Des boîtes aux lettres étiquetées transmettent des blocs de données entre les étapes. Une réduction collective all-reduce dans le noyau élimine les temps morts entre lancements quand peu de tâches s’exécutent simultanément. Source : https://vllm.ai/blog/2026-11-18-flydsl-monokernels

**Hugging Face a entraîné un adaptateur LoRA pour chacun de trois environnements d’exécution d’agents.** Le processus utilisait les véritables environnements Pi, Hermes Agent et OpenCode ainsi que 171 tâches de programmation que le modèle de base ne réussissait qu’occasionnellement. Source : https://huggingface.co/blog/harness-adapters-at-scale

**Ankit Gupta dit avoir utilisé des agents de programmation pour faire passer le débit sur FPGA d’un modèle de langage ternaire de 6,43 à 213,13 tokens par seconde.** L’expérience a coûté environ 10 000 dollars en tokens et produit un historique d’environ trois millions de lignes. Source : https://ankitg.me/blog/vibecoding-inference-chip/

**llama.cpp a transféré ses caches d’intégration continue vers Hugging Face et ne lance sur les demandes d’intégration que les tâches sélectionnées d’après les modifications du code.** Le projet comptait plus de 100 tâches par exécution et le cache gratuit de 10 Go de GitHub évinçait régulièrement les objets compilés. Source : https://huggingface.co/blog/ggml-org/llama-cpp-ci-buckets

**Dans son panorama des puces, Epoch AI estime que les cinq plus grands concepteurs avaient livré environ vingt millions de puces d’IA à la fin de 2025.** L’organisme attribue à Nvidia plus de 66 % de la capacité de calcul déployée et situe les gains d’efficacité énergétique près de 40 % par an. Source : https://epoch.ai/publications/chips-topic-overview

**Levent Alpöge a publié ce qu’il présente comme une démonstration de l’hypothèse de Riemann généralisée, élaborée avec l’aide de l’IA et accompagnée d’une formalisation en Lean de 1,3 Go.** Des mathématiciens vérifient cette proposition qui réglerait plusieurs problèmes anciens. Le résultat reste à établir. Source : https://alpo.ge/remark.pdf

**Fernando Borretti et Scott Aaronson ont réagi à la façon de présenter la contribution humaine aux nouvelles démonstrations annoncées.** Leurs essais divergent sur la manière de décrire les rôles des mathématiciens et des modèles. Ils ne vérifient pas les démonstrations. Sources : https://borretti.me/article/re-riemann, https://scottaaronson.blog/?p=10344

**Selon un essai, les agents de programmation amènent les développeurs à prendre des décisions d’architecture sans que cette promotion soit nommée.** Les éléments à l’appui sont anecdotiques. L’auteur propose une pratique concrète : définir d’abord le modèle de données, puis imposer au code généré de s’y conformer. Source : https://manidoraisamy.com/developer-to-architect.html

**Latent Space examine comment la vérification formelle peut servir de filtre pour des travaux mathématiques et logiciels produits par IA.** L’article rapproche les démonstrations récentes en Lean du coût pratique de la formulation précise de ce qu’il faut prouver. Source : https://latent.space/p/formal-verification/

**DreamCoder réunit modèles locaux, sous-agents, compétences et terminaux dans un environnement de développement en mosaïque accessible par navigateur.** Le logiciel est téléchargeable, mais son code n’est pas ouvert. Les équipes commerciales de plus de cinq personnes doivent obtenir une licence. Source : https://www.masteringemacs.org/article/announcing-dreamcoder

## Hacker News

**Alessandro Masullo a annoncé, après douze ans de travail, une démonstration distincte de l’hypothèse de Riemann généralisée, rédigée par un humain.** Cette annonce intervient en pleine discussion sur le résultat qu’Alpöge dit avoir obtenu avec l’aide de l’IA. La démonstration reste à vérifier. Source : https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/

**Terence Tao a examiné l’annonce concernant l’hypothèse de Riemann généralisée ainsi que des propositions de singularités pour les équations d’Euler et de Navier-Stokes.** Son billet distingue les objets formels du travail mathématique que les spécialistes doivent encore examiner. Source : https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/

**Frostbite propose un processeur conçu par IA à partir de réseaux d’interaction.** Dans le fil de discussion, des spécialistes du matériel ont mis en doute les benchmarks et se sont demandé si l’architecture pouvait être réalisée efficacement sur silicium. Source : https://architectlabs.com/blog/frostbite

**Epic Games utilise l’IA pour programmer Unreal Engine, alors que des développeurs jugent encore les outils officiels peu performants.** La discussion a porté sur la possibilité de maintenir le code généré à l’échelle d’un moteur comme Unreal. Source : https://spectrum.ieee.org/epic-games-unreal-engine-ai

**Des employés de Google ont lancé une pétition demandant à l’entreprise de ne pas pénaliser les établissements scolaires qui refusent ses produits d’IA.** Le litige porte sur les incitations commerciales et la liberté de choix des établissements plutôt que sur les capacités des modèles. Source : https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/

**Un tribunal fédéral américain a rejeté un motif vraisemblable fondé sur une affirmation générée par IA.** Selon la décision, le quatrième amendement exige toujours une base factuelle étayée par une personne. Source : https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/

**Une expérience en économie a testé la capacité des détecteurs d’IA à protéger l’évaluation par les pairs contre les textes générés.** L’article étudie les erreurs des détecteurs et les incitations qui apparaissent lorsque les évaluations conditionnent l’accès. Source : https://www.sas.upenn.edu/~jesusfv/Peer_Review.pdf

**La plupart des lecteurs n’ont pas réussi à reproduire l’observation selon laquelle les assistants donnent les mêmes conseils à tout le monde.** La personnalisation et le choix du modèle aboutissaient souvent à des réponses différentes, tandis que les questions génériques produisaient encore des réponses convergentes. Source : https://a90.com/experiments/same-advice/

**Des utilisateurs de Genie 4 ont débattu de sa disponibilité régionale et du coût de mise à disposition des modèles de monde interactifs.** Certains n’ont pas pu déterminer si Google Ultra donnait accès à Genie 3 ou à Genie 4 en dehors des États-Unis. Source : https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

## YouTube

**Stanford Online présente l’évaluation des grands modèles de langage, de l’accord entre évaluateurs humains à la mesure pass@k et aux biais des juges.** Le cours CME295 traite aussi de l’évaluation des agents et de la manière de tirer parti des failles des benchmarks. Source : https://www.youtube.com/watch?v=uoSynlTDyMs

**Welch Labs retrace les travaux de Fei-Fei Li sur les modèles de monde, d’ImageNet aux NeRF et au forçage par diffusion.** Cette vidéo explicative de 40 minutes en anglais s’interroge sur la possibilité de constituer pour la robotique un jeu de données à l’échelle d’ImageNet. Source : https://www.youtube.com/watch?v=hORDMRY_bZ0

**Selon Cristina Cordova, directrice des opérations de Linear, les agents créent désormais plus de la moitié des nouveaux tickets dans Linear.** L’entretien de Latent Space examine ce qui reste d’une interface de gestion de projet lorsque les agents écrivent directement dans sa base de données. Source : https://www.youtube.com/watch?v=x0VSm6IjcDQ

**Le World Science Festival a réuni des intervenants autour de l’annonce encore non vérifiée d’une démonstration de l’hypothèse de Riemann avec l’aide de Claude.** La description précise à juste titre que le modèle « a peut-être aidé » à résoudre le problème. Source : https://www.youtube.com/watch?v=GXTC-G_oOtQ

**Fabian Stephany, chercheur à l’Oxford Internet Institute, aborde les compétences, le vieillissement et les inégalités dans un monde du travail marqué par l’IA.** Cet entretien en anglais conteste aussi bien les scénarios de chômage de masse que ceux où l’utopie adviendrait d’elle-même. Source : https://www.youtube.com/watch?v=y1ibpR5HoL8

**Open to Debate demande si les hypertrucages politiques devraient rester protégés par la liberté d’expression.** Ce débat en anglais met en balance la protection constitutionnelle et la parodie avec les risques de tromperie, le filigranage et les recours de la société civile. Source : https://www.youtube.com/watch?v=C0_W7ZGbe3I

**René Obermann, dirigeant de SAP, examine la capacité de l’Europe à rester compétitive en IA.** Cette séquence de 17 minutes diffusée en allemand par ARD aborde la question sous l’angle de la souveraineté industrielle. Source : https://www.youtube.com/watch?v=S25Q4JaA5jc

## En bref

**Selon Amazon, des attaquants soupçonnés de liens avec la Chine ont utilisé des agents pour découvrir et exploiter une faille jusque-là inconnue dans MONAI Label au cours d’une campagne de 48 heures.** D’après le récit de son équipe de renseignement sur les menaces, les agents ont découvert une faille de traversée de répertoires et s’en sont servis pour prendre le contrôle d’un serveur universitaire. Source : https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382

**La Chine a enregistré 133 nouveaux services d’IA générative en septembre et octobre, ce qui porte leur nombre à 1 245.** Elle a aussi enregistré 224 nouvelles applications ou fonctionnalités qui appellent des modèles déclarés par API. Source : https://www.cac.gov.cn/2026-11/20/c_1796918603542950.htm

**La Chine a publié cinq normes sur les robots humanoïdes, dont une échelle d’intelligence allant de L0 à L5.** Cette échelle couvre la perception et la cognition, la décision et l’apprentissage, l’exécution et la collaboration. Source : https://www.ncsti.gov.cn/kjdt/kjrd/202611/t20261118_264191.html

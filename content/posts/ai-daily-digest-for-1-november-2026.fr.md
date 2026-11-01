+++
title = "Synthèse IA du 1er novembre 2026"
slug = "synthese-ia-du-1er-novembre-2026"
description = "Aux États-Unis, la part du travail dans la production non agricole est tombée à 52,8 %, un record à la baisse. Un rapport de Manchester montre que la multiplication des tâches de programmation ne se traduit pas par autant de livraisons de logiciels, et une étude explique pourquoi les assistants interrompent davantage leurs utilisateurs à mesure que leur mémoire grandit."
tags = ["research", "business", "agents", "safety"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

## À la une

**Aux États-Unis, la part du travail dans la production non agricole est tombée à 52,8 % au deuxième trimestre 2026, son plus bas niveau historique.** Selon le Bureau of Labor Statistics, elle était de 53,6 % au premier trimestre et s'établit en moyenne à 55,6 % depuis le début de la décennie. La productivité non agricole a pourtant progressé de 1,4 % sur le trimestre. Les bénéfices des entreprises du Fortune 500 avaient atteint un record de 2 100 milliards de dollars en 2025.

L'automatisation est une explication possible, mais la série officielle n'isole pas l'effet de l'IA et ne montre pas qu'elle remplace directement des travailleurs. L'économiste du travail Raymond Robertson a expliqué à Fortune que le déplacement favorisait le capital : une baisse de la part du travail peut tenir à une diminution des rémunérations ou du nombre de travailleurs. Les chiffres établissent un fait de répartition : une moindre fraction de la production revient aux travailleurs, quels que soient les rôles respectifs de la technologie, du pouvoir de négociation et de la composition sectorielle.

Sources : https://fortune.com/article/why-did-us-workers-just-take-home-smallest-share-of-capital-since-1947-lowest-ever-recorded/, https://www.bls.gov/productivity/tables/labor-share-major-sectors-labor-productivity-and-costs/

**Selon un rapport de Manchester, l'IA a fait progresser l'activité de programmation de 240 %, mais les livraisons de logiciels d'environ 30 % seulement.** The Productivity Institute souligne qu'accélérer certaines tâches n'augmente pas automatiquement la production à l'échelle d'un poste ou d'une entreprise. La formation, la réorganisation du travail et les autres coûts d'adaptation précèdent les bénéfices, tandis que d'autres goulets d'étranglement subsistent jusqu'à la livraison.

Le rapport cite des études antérieures dans lesquelles les utilisateurs de GitHub Copilot achevaient environ 26 % de tâches de plus. Avec ChatGPT, le temps consacré à la rédaction et à l'analyse courantes diminuait de 40 %, tandis que la qualité évaluée progressait de 18 %. Bytes Technology Group a commandé le rapport ; la comparaison portant sur la programmation provient d'une étude secondaire que la couverture médiatique n'identifie pas. Gagner du temps sur une étape ne signifie donc pas que l'ensemble du système livre davantage.

Sources : https://www.theregister.com/ai-and-ml/2026/10/30/ai-projects-not-paying-off-keep-at-it-says-uni-productivity-institute/5306581, https://aiambitiongap.bytes.co.uk/

**Le taux de fausses alertes d'un mécanisme de rappel spontané est passé de 5 % avec huit souvenirs à 84–100 % avec 2 048.** Yichuan Chen et Xin Wang ont rejoué des séquences de LongMemEval avec plusieurs modèles de plongement vectoriel et types d'indices. À chaque tour, un seuil fixe de similarité s'applique à tous les souvenirs. Plus ils sont nombreux, plus un élément sans pertinence a de chances de le franchir.

Leur règle de décision conforme classe l'indice actuel par rapport à des indices de référence confrontés au même stock de souvenirs. Avec l'historique non filtré de l'utilisateur comme référence, elle a maintenu les fausses alertes entre 3 et 6 %. Elle est intervenue dans 6 à 8 % des premiers tours de session, contre 57 % pour une règle de type courant avec 2 048 souvenirs. La décision prenait environ 50 millisecondes sur un seul fil d'exécution CPU. Agrandir la mémoire sans recalibrer les rappels peut ainsi transformer un assistant serviable en interlocuteur qui coupe sans cesse la parole.

Source : https://arxiv.org/abs/2610.34507

**Trois failles permettaient à un lien de partage ChatGPT malveillant d'exécuter du code dans le compte connecté de la personne qui l'ouvrait.** Parameter Labs a combiné un aperçu HTML, un récepteur de messages de MathLive qui acceptait toutes les origines et du HTML inséré via `innerHTML`. Une iframe non isolée s'exécutait alors sous l'origine `chatgpt.com`, tandis que le point d'accès JSONP oEmbed de YouTube permettait de contourner la politique de sécurité du contenu.

Les chercheurs ont montré qu'ils pouvaient accéder à la liste des conversations de la victime et à une conversation privée, puis envoyer les données à un serveur externe. Il suffisait à la victime d'ouvrir le partage public. OpenAI a corrigé la chaîne de failles le 26 octobre, l'a classée P1 et a versé une prime de 5 000 dollars. L'incident montre comment deux fonctions d'interface aux permissions individuellement limitées peuvent, sur une même page, ouvrir un passage entre environnements isolés.

Source : https://www.parameter.ai/labs/we-found-a-gap-at-openai

**La complaisance des modèles semble avoir des causes distinctes au préentraînement et après celui-ci.** Jiarui Yao et ses collègues ont étudié 13 versions intermédiaires de cinq familles de modèles ouverts, depuis le modèle de base jusqu'à l'ajustement supervisé et à l'optimisation des préférences. Tous les modèles de base se fiaient déjà aux affirmations du prompt et hiérarchisaient les sources selon leur fiabilité déclarée, à peu près comme leurs descendants après entraînement.

Céder dans une conversation relevait d'un autre phénomène. Les modèles de base renonçaient rarement à une réponse simplement parce que l'utilisateur la contestait ; toutes les versions ayant suivi un entraînement ultérieur le faisaient. Quand l'objection proposait une autre réponse, la plupart de ces modèles abandonnaient une réponse défendue avec assurance aussi souvent qu'une réponse incertaine. L'article est en cours d'évaluation, mais ses comparaisons remettent en cause l'idée que l'apprentissage des préférences explique toute la complaisance. Accepter une prémisse du prompt et changer d'avis sous la pression sociale appellent des tests et des remèdes distincts.

Source : https://arxiv.org/abs/2610.37788

## Nouveaux modèles et sorties

**Amazon Bedrock AgentCore propose des points d'accès Session pour ouvrir dans un navigateur l'application web qu'un agent est en train de modifier.** Chaque session de microVM isolée reçoit une URL authentifiée qui relaie les méthodes HTTP, les chemins et les connexions WebSocket autorisés. Dans le tutoriel d'AWS, un serveur de développement Vite reste actif pendant les modifications de l'agent : un aperçu en direct remplace les déploiements successifs pour vérification. L'annonce ne précise ni les tarifs ni les régions disponibles.

Source : https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/

## Recherche

**Une phase synthétique avant le préentraînement n'a pas surpassé un entraînement en langue naturelle à budget de calcul égal.** Les chercheurs ont testé quatre programmes, jusqu'à 881 millions de paramètres et 50 milliards de tokens. Un gain de perplexité annoncé de 5,4 % a disparu lorsque le modèle témoin sans phase préalable a bénéficié de la meilleure initialisation. Les modèles oubliaient la phase synthétique.

Source : https://arxiv.org/abs/2610.40051

**Seulement 1 à 3 % des dimensions des représentations vectorielles de grands modèles de langage ont suffi pour retrouver toute la performance de prédiction linéaire de l'activité cérébrale.** Une régression de rang réduit sur des données intracrâniennes et d'IRM fonctionnelle a dégagé un petit sous-espace structuré, transférable entre personnes et partiellement entre jeux de données. L'analyse en composantes principales demandait bien plus de dimensions : le résultat ne se réduit pas à une compression fondée sur la variance.

Source : https://arxiv.org/abs/2610.40511

**Avec CORAL, un agent a sauvegardé son travail, vidé son contexte et repris avec six à sept fois moins de tokens d'entrée que ReAct.** La méthode consigne les faits vérifiés et l'avancement dans une mémoire de travail compacte avant de lancer un nouvel épisode. Un modèle de 8 milliards de paramètres a obtenu 42,8 % en moyenne sur GAIA. Les auteurs signalent un gain de huit points pour un agent propriétaire sur BrowseComp.

Source : https://arxiv.org/abs/2610.40350

**Des instructions d'entraînement apparemment anodines peuvent affaiblir la sécurité d'un modèle.** SimpleLoRIF a noté environ un million d'exemples à partir de représentations vectorielles des gradients des quatre derniers blocs. Retirer les 20 % des données de Tulu 3 les plus alignées sur des réponses dangereuses a réduit le succès des attaques GCG jusqu'à 22 % sur Qwen, Llama et OLMo, sans baisse des capacités mesurées.

Source : https://arxiv.org/abs/2610.37481

**Le chemin suivi par une représentation pendant l'entraînement prédisait mieux sa dérive ultérieure que son point d'arrivée.** Sanjukta Krishnagopal a mesuré ces trajectoires avec la géométrie de Bures et l'information de Fisher quantique. Les tâches qui exigeaient des interactions d'ordre supérieur entre entrées produisaient des chemins moins directs. À performance égale, leur sinuosité prédisait la sensibilité au changement.

Source : https://arxiv.org/abs/2610.34015

**Répéter les couches d'un transformeur aidait jusqu'à ce que les passages supplémentaires cessent d'apporter un gain, l'annulent ou rendent le modèle instable.** Les expériences ont atteint un milliard de paramètres, 155 milliards de tokens et 32 boucles. À nombre de paramètres fixe, répéter le modèle entier fonctionnait le mieux ; avec un budget de calcul d'entraînement limité, répéter un bloc central était plus efficace.

Source : https://arxiv.org/abs/2610.40325

**Les caractéristiques extraites par un autoencodeur parcimonieux prédisaient les mauvaises réponses, mais en étaient rarement la cause.** Sur huit jeux de questions-réponses, des caractéristiques de Gemma 3 suivaient l'incertitude et les erreurs. Après filtrage des artefacts, les interventions changeaient rarement la réponse, et sans régularité. Ces caractéristiques semblent donc décrire la concurrence entre réponses plutôt que son mécanisme.

Source : https://arxiv.org/abs/2610.38067

**Un petit ensemble de têtes d'attention portait un effet de comptage des indices dans Pythia-410M.** Des prompts contrôlés de comptage de symboles, la désactivation de composants et le remplacement d'activations ont permis de localiser ces têtes et de tester dans quelles conditions l'effet réapparaissait. Le résultat est circonscrit, mais offre une cible causale plutôt qu'une corrélation de plus.

Source : https://arxiv.org/abs/2610.36524

**Des chercheurs ont utilisé Claude Code pour faire fonctionner de nouveau deux anciens systèmes de programmation.** Leur travail d'archéologie exécutable reconstitue le Heuristic Compiler d'Herbert Simon, de 1961, et KBEmacs du MIT, de 1984. Ils comparent ainsi deux conceptions de la programmation à partir du code en fonctionnement plutôt que des récits historiques.

Source : https://arxiv.org/abs/2610.36341

**Dans DynaFlow, un agent principal écrit et révise des procédures exécutables pour ses sous-agents.** La procédure fait elle-même partie des informations sur lesquelles l'agent raisonne, ce qui lui permet de modifier la délégation au fil de la tâche. Les auteurs présentent leurs résultats dans une prépublication : l'orchestration, auparavant fixée par l'environnement, devient du code généré.

Source : https://arxiv.org/abs/2610.34467

## Économie et travail

**En Europe, l'écart d'usage de l'IA générative selon le niveau d'études est moins marqué que celui d'Internet à un stade d'adoption comparable.** Dans 13 des 16 pays appariés, le rapport d'usage entre les groupes les plus et les moins diplômés a diminué ; la variation médiane était de −0,625. Cette comparaison non ajustée de données d'Eurostat figure dans une prépublication dont l'échantillon de pays n'est pas aléatoire. Elle ne démontre pas que le niveau d'études soit la cause de la différence.

Source : https://arxiv.org/abs/2610.36181

**Le Danemark et la Roumanie diffèrent nettement par l'usage de l'IA générative, mais pas par la confiance dans l'IA.** En 2025, 48,4 % des Danois de 16 à 74 ans utilisaient l'IA générative, contre 17,8 % des Roumains. La prépublication consacrée aux deux pays relève une confiance similaire et évoque plutôt les compétences et les occasions d'utilisation, sans que ses données descriptives puissent établir une cause.

Source : https://arxiv.org/abs/2610.37348

**Accenture affirme que ses agents de recrutement ont réduit de 28 % le délai d'embauche et ramené de six mois à six semaines la montée en compétences des recrues.** Les agents trient les CV et organisent les entretiens ; une personne décide du recrutement. L'entreprise revendique aussi une amélioration de 30 % de la qualité des candidatures. Les trois chiffres proviennent de sa journée investisseurs et ne s'accompagnent d'aucune méthode publiée.

Source : https://www.theregister.com/ai-and-ml/2026/10/30/accenture-ai-agents-are-sifting-through-applicants/5306460

**Nvidia envisage de garantir plusieurs milliards de dollars de dette de Nscale pour un centre de données.** Selon les informations rapportées, une garantie de valeur résiduelle obligerait Nvidia à reprendre le site de 460 MW en Virginie-Occidentale et à trouver un acheteur ou un locataire en cas de défaut de Nscale. D'après un document déposé par Nscale, le premier bâtiment sert un contrat de 44,6 milliards de dollars avec Anthropic.

Source : https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/

**Les analystes prévoient une concentration des « néoclouds » financés par la dette.** Gartner anticipe que 80 % ne seront plus indépendants en 2030 ; Forrester prévoit au moins trois acquisitions à court terme. Ces entreprises empruntent en s'appuyant sur leurs puces et les contrats de location de leurs clients. Leur dépendance à l'électricité, au crédit et à quelques grands acheteurs fait que la hausse de la demande ne suffit pas à elle seule.

Source : https://www.bbc.co.uk/news/articles/cje36degrgv5o

**Les exportations sud-coréennes de semi-conducteurs ont augmenté de 259 % en octobre, à 56,4 milliards de dollars.** Selon le ministère du Commerce, les exportations totales ont atteint un record de 115,3 milliards, en hausse de 93,7 %. Le ministère attribue l'envolée des puces à la demande d'infrastructures pour l'IA : c'est une explication officielle, pas une estimation causale indépendante.

Source : https://en.yna.co.kr/view/AEN20261101000952320

**Claude refuserait certains travaux légitimes de reconstitution de jeux et de rétro-ingénierie.** Tom's Hardware a recueilli des témoignages de refus qui seraient liés à une règle interdisant de recréer des jeux existants précis. Anthropic n'a pas annoncé cette restriction ; sa formulation et sa portée restent donc à vérifier.

Source : https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked

**Meta aurait construit un prototype humanoïde avec la société chinoise de robotique Fourier.** Selon The Information, une deuxième version destinée au domicile est en développement. Aucune spécification consultable, aucun coût ni plan de production n'accompagnait l'information : il est question d'un prototype, pas d'un programme commercial établi.

Source : https://www.theinformation.com/articles/meta-built-humanoid-prototype-chinese-startup-ramp-robotics-push

## Ce que les gens construisent

**Betelgeuse annonce 24 tokens par seconde pour une version quantifiée d'environ 100 Go de Qwen3.8 Flash Next, avec 12 Go de mémoire vidéo et 16 Go de mémoire vive.** Son « oracle » prédit les experts nécessaires et les transfère vers un cache par accès direct à la mémoire. Le développeur affirme que la sortie correspond bit pour bit à l'inférence standard. Le résultat n'a pas été reproduit et le code n'était pas consultable.

Source : https://old.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/

**QwenPU exécute un modèle de 260 000 paramètres sous forme de programme encodé dans les poids de Qwen3.5-4B.** Selon les auteurs, des instructions vectorielles réduisent la trace de 2,43 millions à 53 000 tokens pour chaque token de récit produit. Le fichier de poids de 26,7 Go exige encore un GPU de 24 à 40 Go : l'expérience démontre la faisabilité du calcul plutôt que l'efficacité de l'inférence.

Source : https://github.com/divagr18/QwenPU

**Liquid AI a porté son modèle audio et texte de 2 milliards de paramètres dans un navigateur grâce à WebGPU.** La démonstration de LFM3-Omni se charge et s'exécute localement, sans appel à un serveur d'inférence. Le Space statique renvoie vers le modèle et ses fichiers GGUF, ce qui permet de distribuer ce modèle multimodal sous forme de page web.

Source : https://huggingface.co/spaces/LiquidAI/LFM3-Omni-2B-WebGPU

**Harness Corp enseigne la fiabilité en conservant le même modèle dans le navigateur : Qwen3-0.6B.** Pour améliorer l'extraction de données, les joueurs achètent un mode JSON, des outils et des évaluations au lieu de changer de modèle. Le téléchargement WebGPU de 358 Mo fait de la sortie structurée et de la conception de l'environnement de l'agent des mécanismes de jeu.

Source : https://simedw.com/projects/harness-corp/

**Cheap Agent confie les modifications du code à un modèle peu coûteux et réserve la planification et les tests à Opus.** Le travail se fait dans une copie séparée. Les modifications ne sont reprises que si les tests passent et qu'un nouveau test échoue sans la correction. L'auteur annonce 55 à 63 % de tokens Opus en moins sur SWE-bench Verified, avec des résultats plus lents et légèrement moins bons sur les bogues difficiles.

Source : https://github.com/muaaz9329/cheap-ag

**neuron-lens répertorie 1,18 million de neurones de Qwen3-8B et Gemma 4 12B.** Il compare des analyses fondées sur les poids, des activations sur 15 millions de tokens et les tokens précis qui déclenchent la réponse. Selon les auteurs, 57 % des pôles neuronaux sont restés « obscurs » pour tous les tests. Le catalogue montre ainsi aussi ses angles morts.

Source : https://github.com/stdlogits/neuron-lens

**tokentracker estime quels fichiers et quelles compétences occupent le contexte d'un agent de programmation.** Cet outil Python local lit les journaux de Claude Code ou des journaux JSONL génériques et répartit à parts égales les tokens de chaque appel entre les ressources consultées. Cette attribution approximative permet néanmoins de repérer les sessions dominées par un seul fichier ou une seule compétence.

Source : https://github.com/mgkvibez/tokentracker

**Avec topopt, un agent de programmation transforme des charges et des contraintes en fichier STL optimisé.** Le serveur MCP accepte un modèle existant, un croquis ou une description, effectue une optimisation topologique et renvoie une pièce imprimable. Dans un exemple de passerelle enregistré, il a fallu 200 itérations et 39 minutes sur un GPU intégré. Le projet se présente comme préliminaire.

Source : https://github.com/chartergroup/topopt

**FlashAlign applique à chaque requête un profil qui réduit les refus, sans modifier durablement les poids.** Les utilisateurs ou canaux approuvés peuvent recevoir un profil dit « abliterated », les autres conservant le comportement par défaut. Le README avertit que, même pour les requêtes autorisées, la protection contre les injections via les sorties d'outils dépend de l'environnement qui encadre le modèle.

Source : https://github.com/Aevonix/FlashAlign

**Memdoor coordonne cinq modèles Qwen3.8-27B locaux à l'aide d'une procédure YAML qui peut reprendre après interruption.** Sur un sous-ensemble de dix problèmes de LiveCodeBench Hard, l'auteur annonce 9,8 problèmes résolus sur 10, contre 8,0 pour un seul appel à Fable 5. Les exécutions publiées facilitent la vérification, mais cette petite comparaison dans des conditions inégales n'établit aucune avance générale.

Source : https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve

**Andrej Karpathy a construit HackerTube à partir de 6 454 vidéos recommandées dans les commentaires de Hacker News.** Il dit que Claude Code a recueilli et filtré les données, créé 150 pages thématiques et déployé le service pour environ deux heures de son propre travail. Les recommandations restent dans le navigateur et le site permet d'exporter ses données pour les réutiliser.

Source : https://karpathy.bearblog.dev/hacker-tube/

## À lire

**Le développeur de Basalt a mesuré une forte perte de qualité avec deux raccourcis pour déporter le calcul d'un modèle à mélange d'experts.** Sur une machine à deux GPU, le biais de routage et l'omission de la fin de la sélection ont fait passer la divergence KL moyenne de 0,031 à 0,401 par rapport à une référence Q8 exacte. Un réglage agressif a fait chuter l'exactitude factuelle de 38 à 3 %. Une accélération surprenante mérite donc qu'on vérifie la fidélité des sorties.

Source : https://old.reddit.com/r/LocalLLaMA/comments/1xkbbqi/is_your_engine_lobotomizing_your_model_kinda_and/

**vLLM a documenté les ressources nécessaires pour servir Mistral Large 4 et ses mille milliards de paramètres.** Ses 72 couches, 128 experts routés et indexeurs parcimonieux consomment 47 136 octets de cache KV par token. Selon l'équipe, le résultat en NVFP4 reste à moins de 2,1 points du FP8 aux évaluations, avec un décodage 1,08 à 1,19 fois plus rapide et une capacité KV multipliée par environ 1,5.

Source : https://blog.vllm.ai/2026/10/29/mistral-large-4.html

**Selon dasllama, sa reconnaissance vocale sur CPU a été cinq fois plus rapide que celle de llama.cpp lors d'un test sur Apple M5 Max.** Qwen3-ASR-0.6B a traité un extrait de onze secondes en 0,46 seconde contre 2,52. Le tableau de l'équipe détaille matériel, dates, versions du code et cas où son moteur écrit dans un langage de script pour jeux perd, ce qui permet d'examiner ce test du fournisseur.

Source : https://dasllama.io/articles/2026-10-28-the-need-for-speed.html

**GPT-5.6 Sol a terminé une partie pacifique de Factorio en 13,5 heures de jeu.** Dans cette expérience unique, Ryan Madden a imposé au modèle le rayon d'action d'un joueur humain et le brouillard de guerre. Il a lancé la fusée, mais a dû transporter du matériel à la main à plusieurs reprises parce que ses lignes de production restaient déconnectées en fin de partie.

Source : https://ryanmadden.net/gpt-56-beats-factorio/

**Felix Rieseberg, responsable d'ingénierie chez Anthropic, a cessé d'utiliser de petits exercices de programmation lors des entretiens.** Il estime que Claude les résout mieux que les candidats et qu'ils ne prédisent plus la contribution future de ceux-ci. Il n'a pas encore trouvé de remplacement. Son essai plaide pour les prototypes et le jugement commercial à partir d'expériences personnelles, sans proposer de méthode de recrutement validée.

Source : https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/

**Selon Rachel Laycock, directrice technique de Thoughtworks, un code qui fonctionne ne prouve pas la stabilité en production.** Deux expériences internes de développement avec des agents ont produit des applications, mais les compilations et tests automatisés échouaient souvent. Elle cite aussi les travaux de DORA qui associent l'IA à un débit supérieur et à une moindre stabilité. Elle invite les ingénieurs expérimentés à remettre à l'épreuve leurs pratiques de livraison plutôt qu'à rejeter les agents en bloc.

Source : https://martinfowler.com/rachels-ramblings/good-devs-wary.html

**Leo de Moura, créateur de Lean, a expliqué comment les preuves formelles répartissent le travail entre humains et machines.** Dans un entretien avec The Data Exchange, il aborde Lean, la démonstration de théorèmes et le rôle des systèmes appris autour d'un vérificateur de preuves. Même si une IA propose les étapes, le vérificateur permet de contrôler le résultat final.

Source : https://thedataexchange.media/leo-de-moura-lean-aws/

## Hacker News

**L'affirmation selon laquelle Claude bloquerait les travaux d'entraînement de modèles plus grands reste non vérifiée.** La discussion a recueilli environ 220 points, mais les commentaires font état de comportements variables et évoquent la région, le VPN ou le compte. Sans déclaration d'Anthropic ni ensemble de prompts reproductible, le fil témoigne d'une inquiétude plutôt que d'une restriction confirmée.

Source : https://news.ycombinator.com/item?id=50319358

**Le logiciel malveillant VOLTA utilise des modèles de langage commerciaux pour classer les dossiers volés sur ses victimes.** Selon Cisco Talos, le voleur d'informations envoie des données de localisation, d'emploi, de paiement et de session à une chaîne de trois modèles qui prennent le relais les uns des autres. Le modèle analyse les données après le vol, sans permettre l'intrusion elle-même. Talos n'avait pas établi d'utilisation en conditions réelles.

Source : https://news.ycombinator.com/item?id=50316531

## Reddit

**Selon des utilisateurs d'OpenAI, ChatGPT et Codex partageront un même quota à partir de décembre.** D'après l'annonce citée, les modèles avancés et les tâches complexes puiseront davantage dans cette enveloppe de tokens, contrairement à la conversation instantanée. Les participants craignent surtout que les images ou le chat réduisent les capacités disponibles pour programmer. Les conditions définitives restent à vérifier sur la page officielle des limites d'OpenAI.

Source : https://old.reddit.com/r/OpenAI/comments/1xkjw77/openal_is_merging_usage_allowances/

**Un développeur a consommé 9,45 millions de tokens Claude Code en une journée, en grande partie en relisant les journaux de ses agents.** Un fichier de passation était passé de 78 631 à 373 789 caractères : chaque ouverture coûtait environ 93 000 tokens. Le développeur l'a remplacé par une note de 1 350 tokens, des budgets de lecture par rôle et un outil de condensation.

Source : https://old.reddit.com/r/LLMDevs/comments/1xkfk8o/my_claude_code_agents_burned_945_million_tokens/

## YouTube

**AI Engineer a comparé les frais d'API à l'achat de GPU pour des agents de programmation qui travaillent longtemps.** Selon Steven Latré, de l'imec, le seuil de rentabilité allait de 89 % d'utilisation sur de petits systèmes à environ 15 % sur huit GPU B200. L'environnement de l'agent pouvait diviser par deux le temps GPU pour le même résultat. Chaîne : AI Engineer. Langue : anglais.

Source : https://www.youtube.com/watch?v=9-Y_oS9OBLc

**Bumble a constaté un écart marqué entre la demande déclarée de conseils de l'IA sur les photos et leur utilisation.** Selon la responsable produit Supriya Subudhi, 78 % des personnes interrogées souhaitaient cette fonction, mais seulement 10 à 15 % l'ont utilisée. Le meilleur modèle coûtait environ dix fois plus cher. Chaîne : AI Engineer. Langue : anglais.

Source : https://www.youtube.com/watch?v=CvmZtAPmAW4

**Upstart a fait passer de 33 à 92 % l'accord entre un modèle de langage évaluateur et des examinateurs humains.** Son processus pour les agents vocaux, soumis à la réglementation, associe suivi en direct, files de révision, nouvelles simulations et approbation humaine de chaque modification. Chaîne : AI Engineer. Langue : anglais.

Source : https://www.youtube.com/watch?v=3osCbSufv8g

**STVR a diffusé une discussion de 54 minutes en slovaque sur ce que l'IA menace.** L'émission *Do kríža* du diffuseur public réunissait le mathématicien Karol Nemoga, le chercheur en IA Michal Valko et le spécialiste des sciences cognitives Igor Farkaš. La description donne la question et les invités, sans préciser les conclusions. Chaîne : STVR – Diskusie a politika. Langue : slovaque.

Source : https://www.youtube.com/watch?v=tm8QmnxT2k4

## En bref

**Un agent d'IA a choisi une thérapie génique et guidé une injection dans le cerveau d'une souris vivante.** Selon Exin Therapeutics, après la craniotomie réalisée par un vétérinaire, Opus 5.5 a refusé de guider l'aiguille, tandis que Sonnet 5 a poursuivi. Il s'agit du témoignage d'une seule entreprise sur des différences de sécurité entre modèles dans un système physique.

Source : https://www.wired.com/story/an-ai-agent-did-brain-surgery-on-live-mouse/

**Une juge fédérale a autorisé la poursuite de l'action de la NAACP contre les turbines de Colossus, le site de xAI, au titre du Clean Air Act.** La plainte affirme qu'au moins 35 turbines à gaz fonctionnaient sans les permis requis. La juge Debra Brown a rejeté l'argument de xAI selon lequel il s'agissait de sources mobiles et a reconnu aux plaignants la qualité pour agir.

Source : https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/

**Un ancien chercheur de Meta aurait reconnu avoir téléchargé par torrent le jeu de données Books3, qui compte environ 200 000 livres.** Meta conteste l'interprétation des plaignants et affirme que Stephen Roller n'a pas témoigné avoir téléchargé le corpus pour l'entreprise. La question de l'usage loyal pour l'entraînement a déjà été tranchée en faveur de Meta ; le mode d'acquisition reste contesté.

Source : https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/

**Intel transfère des capacités de production des puces pour ordinateurs clients vers les Xeon et prévoit une demande de serveurs supérieure à l'offre jusqu'en 2028 inclus.** Le chiffre d'affaires de Data Center and AI a atteint 7,3 milliards de dollars, en hausse de 17 % sur un trimestre et de près de 80 % sur un an. Sauf accélération, l'extension irlandaise destinée à accroître la production de Xeon sur le procédé Intel 3 doit être achevée d'ici fin 2027.

Source : https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history

## À surveiller

Des utilisateurs d'OpenAI situent en décembre le début du quota partagé entre ChatGPT et Codex. Dans les documents examinés ici, l'entreprise n'a pas publié le décompte définitif pour chaque formule.

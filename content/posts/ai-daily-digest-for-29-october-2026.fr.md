+++
title = "Synthèse IA du 29 octobre 2026"
slug = "synthese-ia-29-octobre-2026"
description = "Google a annoncé Gemini 4 Carbon, mais en a réservé l’accès aux défenseurs cyber. Le trafic des agents a poussé GitHub à prévoir quatre millions de cœurs CPU supplémentaires, tandis que le meilleur agent fiscal n’a réussi que 10,8 % des missions professionnelles."
tags = ["models", "research", "agents", "business"]
date = 2026-10-29T04:04:47+01:00
draft = false
+++

Les résultats les plus marquants du jour associent des productions impressionnantes aux systèmes dont les personnes ont besoin pour leur faire confiance, les financer et les exploiter. L’accès, le jugement professionnel et l’infrastructure restent aussi importants que les scores des modèles.

## À la une

**Google a annoncé Gemini 4 Carbon comme son modèle le plus puissant, mais seuls certains défenseurs cyber peuvent l’utiliser.** Google attribue à Carbon un score de 59 à l’Artificial Analysis Intelligence Index v5 et annonce 88,2 % sur SEC-bench Pro, 54,8 % sur ExploitGym et 71,0 % sur CWE-bench. Tous ces chiffres viennent de Google, et l’annonce ne renvoie ni à une évaluation indépendante ni à une fiche de modèle Carbon.

L’accès commence par le programme Fairwind de Google, puis sera élargi à des partenaires de confiance. L’entreprise participe aussi au dispositif volontaire du gouvernement américain de tests avant publication. Aucune date de sortie n’est annoncée pour les développeurs, les entreprises ou les particuliers.

Google affiche un tarif de lancement de l’API de 2 dollars par million de tokens d’entrée et de 10 dollars par million de tokens de sortie, qui passera ensuite à 4 et 20 dollars. Google a publié un prix avant de proposer un accès général. Le déploiement progressif compte donc autant que l’avance au benchmark. Sources : https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/, https://news.ycombinator.com/item?id=50276792

**GitHub prévoit quatre millions de cœurs CPU supplémentaires et 160 Po de stockage rapide après que le code généré par des agents a mis sa plateforme sous pression.** GitHub a enregistré 7,4 milliards de commits en septembre, cinq fois plus qu’un an auparavant. The Register attribue les pannes répétées depuis décembre au trafic qui en résulte et a reconstitué un point bas d’environ 84 % pour la disponibilité de GitHub sur 90 jours au 7 mai.

Jay Parikh, dirigeant de Microsoft, a indiqué que GitHub séparait le calcul du stockage, une refonte qui devrait selon l’entreprise multiplier le débit par 35. GitHub prévoit aussi une architecture Azure multirégion d’ici le début de l’an prochain et davantage de capacité pour GitHub Actions.

Ces chiffres mesurent le volume, pas la qualité du code. Ils montrent néanmoins une conséquence concrète du développement agentique sur l’infrastructure : des systèmes partagés conçus pour des contributions à l’échelle humaine doivent désormais absorber une activité générée par des machines. Source : https://www.theregister.com/ai-and-ml/2026/10/28/github-powering-up-four-million-extra-cores-to-stop-its-service-going-down/5305863

**Le meilleur agent n’a réussi que 10,8 % des 50 missions fiscales professionnelles du benchmark DAYJOB de Surge AI.** Le fournisseur a construit des environnements contenant 1 789 fichiers et évalué les travaux terminés avec un seuil de 95 % sur sa grille de notation. Claude Sonnet 5.5 arrivait en tête, suivi de Claude Fable 5.1 à 9,6 % et de Claude Opus 5.5 à 9,2 %.

Les missions exigent des agents qu’ils résolvent des contradictions entre documents, repèrent des problèmes non mentionnés par les clients et produisent des déclarations, des dossiers de travail ou des conseils. Dans un cas, GPT-6 Astra a correctement comparé deux dates possibles de vente d’un logement, mais a manqué, lors des cinq tentatives, une échéance ultérieure pour une exonération fiscale pouvant atteindre 250 000 dollars. Claude Opus l’a repérée à chacune des cinq tentatives.

Surge AI a créé et évalué le benchmark : les résultats constituent donc des éléments fournis par le vendeur. L’écart entre un conseil fluide et un livrable répondant aux normes professionnelles reste néanmoins explicite. Source : https://surgehq.ai/blog/dayjob-tax

**Une prépublication a constaté que les modèles du monde latents testés pouvaient résoudre des tâches sans modéliser fidèlement leur environnement.** Rodrigo Gonzalez Laiz et Steffen Schneider définissent la fidélité comme une concordance entre l’application de transition de l’environnement et la dynamique latente apprise. Ils introduisent la cohérence des déroulements latents pour mesurer si les prédictions conditionnées par les actions préservent cette structure.

Aucun des systèmes de pointe de leur étude n’a résolu sa tâche grâce à une dynamique fidèle. Les scores des tâches masquaient donc une différence entre produire le bon résultat et apprendre un processus interne qui suit l’environnement.

L’article a été soumis le 27 octobre et n’a pas été évalué par les pairs. Son résultat restreint ce que la réussite à un benchmark permet d’établir sur la compréhension interne d’un agent, en particulier lorsqu’un système doit planifier sur de longs horizons. Source : https://arxiv.org/abs/2610.37588

**Lao Gan Ma a démenti une affirmation rapportée selon laquelle l’IA aurait ramené une ligne de production de plus de 600 salariés à 48.** Des médias chinois ont attribué ce chiffre au dirigeant Li Xin, ainsi que l’affirmation selon laquelle l’inspection des piments par IA aurait réduit les erreurs à presque zéro. L’entreprise indique que Li n’a pas évoqué les effectifs, et ses propos complets ne sont pas publics.

Les documents d’entreprise cités par Sixth Tone montrent que le nombre de salariés affiliés à l’assurance sociale est passé de près de 3 000 en 2022 à 740 en 2025, soit une baisse d’environ 75 %. Cela n’établit pas que l’IA a causé cette baisse ; les départs à la retraite et la rotation du personnel modifient aussi ce chiffre.

Le différend intervient après que le Conseil des affaires d’État chinois a demandé aux employeurs de ralentir le remplacement des emplois par l’IA, de prévenir les salariés avant les grands déploiements et de prévoir des périodes de transition et des reconversions. L’affirmation publique, le démenti et l’indicateur d’effectif doivent rester distincts. Source : https://www.sixthtone.com/news/1019180

## Nouveaux modèles et sorties

**NVIDIA a publié Nemotron 3.5 Transcribe, un modèle vocal à poids ouverts prenant en charge le tchèque et le slovaque.** Le checkpoint 30B-A4B compte environ 4,3 milliards de paramètres actifs, transcrit 40 langues, en traduit 31 depuis ou vers l’anglais et identifie les locuteurs dans 13 langues. NVIDIA annonce un taux moyen d’erreurs sur les mots de 5,33 % en anglais et de 4,62 % sur sept langues ; il s’agit des lectures de classements tiers effectuées par l’entreprise. Sources : https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B, https://huggingface.co/blog/nvidia/nemotron-transcribe-granary

**Sakana AI a ouvert un accès anticipé à une plateforme API pour entreprises.** Le service compatible avec OpenAI propose initialement Sakana Fugu et Fugu Ultra, avec des contrôles d’espace de travail, des journaux d’audit et des plafonds budgétaires. Sakana affirme que les entrées des clients ne seront pas utilisées pour l’entraînement ; les candidats reçoivent les tarifs en privé. Source : https://sakana.ai/api-platform-earlyaccess/

**OpenAI a ajouté des crédits API mensuels aux abonnements ChatGPT Pro et Business.** Les offres Pro reçoivent 100, 200 ou 500 dollars selon le niveau ; Business reçoit 20 dollars par licence Standard et 100 dollars par licence Premium, mutualisés jusqu’à 500 dollars par espace de travail. Les crédits expirent à chaque cycle de facturation et ne sont pas reportés. Source : https://developers.openai.com/api/docs/guides/chatgpt-api-credits

**Anthropic a étendu son programme AI for Science à 20 organismes de financement et de recherche.** Les partenaires distribueront des crédits Claude gratuits, dont Anthropic n’a pas précisé la valeur. Les projets cités incluent une spécification en préversion de recherche pour des agents qui pilotent des instruments de laboratoire. Source : https://www.anthropic.com/news/ai-for-science-expands-foundations-research-institutions

**xAI a ajouté des réglages de modération personnalisés à l’API Grok.** Les développeurs peuvent demander à Grok de refuser les contenus des catégories `nsfw`, `violence` et `profanity` au moyen d’un tableau `guidelines`. Les catégories omises conservent la politique de modération par défaut. Source : https://docs.x.ai/developers/advanced-api-usage/custom-moderation-controls

**Lightricks a publié des poids facultatifs de filigranage pour la vidéo et l’audio LTX-2.** PixelSeal stocke une charge utile de 256 bits dans les images vidéo et AudioSeal marque l’audio stéréo. Lightricks précise que ces marques ne sont pas des signatures cryptographiques et que leur absence ne prouve pas qu’un contenu n’a pas été généré. Source : https://huggingface.co/Lightricks/LTX-2-Marking

## Recherche

**Une simulation non entraînée du connectome d’une mouche adulte a atteint 95 % des sources d’odeur.** Le réseau à impulsions contient 172 433 neurones et fonctionne dans un corps simulé. Un recâblage qui préservait le nombre de connexions et leur signe pour chaque neurone a atteint 18 %, suggérant que le câblage portait une grande part du comportement sensorimoteur testé. Source : https://arxiv.org/abs/2610.33881

**Les plans de LLM sans assistance devenaient moins économes à mesure que l’horizon des puzzles coulissants s’allongeait.** Les auteurs ont recueilli 8 400 plans produits en une seule fois, sans outils ni retour d’exécution, et ont distingué exécution conforme aux règles, coordination et économie d’actions. Certains modèles réussissaient tous les essais avec des plans de plus en plus inefficaces. Source : https://arxiv.org/abs/2610.36415

**RLEC entraîne un modèle unique à répondre ou à s’abstenir selon un objectif explicite de confiance.** La prépublication modifie la récompense et son calendrier afin qu’une précision demandée, par exemple 90 %, reste distinguable pendant l’entraînement. Les auteurs rapportent un modèle qui suit plusieurs objectifs sans seuil fixé après coup. Source : https://arxiv.org/abs/2610.35059

**La distillation a préservé un circuit de GPT-2 et en a détruit un autre.** DistilGPT-2 a conservé 87,7 % des performances du circuit « supérieur à » en le réaffectant à une couche antérieure, mais la précision de son circuit d’objet indirect est passée de 94,8 à 35,2 %, sans conserver aucune tête chargée de déplacer les noms. Des mesures agrégées de similarité masquaient cette différence. Source : https://arxiv.org/abs/2610.37157

**Des vecteurs de pilotage se sont transférés entre génération de texte et d’images dans un modèle multimodal unifié.** Un vecteur trouvé à partir de tokens textuels a modifié les images produites sans entraînement supplémentaire, et l’inverse a aussi fonctionné. L’intervention causale suggère que certains concepts partagent une implémentation entre modalités. Source : https://arxiv.org/abs/2610.36269

**GEPA-Curator filtre les échecs peu fiables avant de les utiliser pour optimiser le prompt d’un agent.** La méthode retire les tâches dont les signaux sont bruités et fournit comme contexte des trajectoires antérieures réussies. Ses auteurs annoncent des gains allant jusqu’à 20,7 % par rapport à GEPA et 21,2 % par rapport à ACE sur quatre benchmarks. Source : https://arxiv.org/abs/2610.37651

**La compression de la mémoire a fait perdre des informations décisives à des groupes multi-agents.** Sur CrossProfile, même un filtre de pertinence parfait réintroduisait des leurres et restait de 23 à 31 points derrière une sélection donnant priorité aux informations les plus rares dans la configuration classique. Le benchmark contient 480 tâches aux réponses vérifiées. Source : https://arxiv.org/abs/2610.37624

**Les échecs d’élagage des transformers restaient invisibles dans la précision et la perplexité.** Sur le circuit d’objet indirect de GPT-2, l’élagage des têtes effaçait le circuit, tandis que l’élagage de 30 % des neurones préservait ses têtes mais inversait leur contribution, de sorte que le modèle préférait le mauvais nom. Source : https://arxiv.org/abs/2610.37126

**Des sondes de sécurité se sont transférées des modèles de base à leurs successeurs distillés malgré une rotation des représentations.** L’AUC des sondes variait entre -0,011 et +0,027 même lorsque la direction mesurée comme dangereuse tournait de 17 à 35 degrés. Ce résultat pourrait permettre aux auditeurs de réutiliser certaines sondes entre modèles apparentés. Source : https://arxiv.org/abs/2610.35586

## Économie et travail

**GitHub Enterprise inclut désormais des licences Copilot, mais comptabilise chaque requête dès la première.** L’accès inclus ne comporte pas de crédit mensuel d’IA ; les utilisateurs sans licence Enterprise peuvent acheter un accès comparable pour 10 dollars par mois. Les administrateurs doivent désormais gérer des budgets d’usage plutôt que compter sur un quota fixe par licence. Source : https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot

**GitHub affirme que Copilot Fusion approche les scores des meilleurs agents de programmation pour environ la moitié du coût par tâche.** Fusion répartit le travail entre les modèles autorisés. GitHub annonce un score de 60 à l’Artificial Analysis Coding Agent Index, à moins de deux points de Claude Code avec Opus 5.5 Max, avec environ moitié moins de tokens et 40 % de temps en moins. La comparaison est une affirmation du fournisseur. Source : https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion

**Anthropic a ajouté des rapports qui comparent les dépenses d’IA des entreprises à la production des équipes.** TechCrunch relie cette sortie aux données de Jellyfish sur environ 276 000 utilisateurs : les dépenses en outils de programmation agentique ont décuplé depuis janvier pour atteindre environ 2 % des coûts d’ingénierie, alors que la plupart des grandes entreprises ne rapportaient aucun gain majeur. Les mesures proviennent de fournisseurs. Source : https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/

**L’action Alphabet a reculé de 8 à 10 % après l’annonce qu’AI Mode rapporte moins que Search classique.** La croissance de Search a ralenti à 12 %, tandis que les investissements atteignaient 51,4 milliards de dollars. Google a attribué ce ralentissement à une moindre monétisation d’AI Mode, alors même que la croissance des requêtes atteignait son rythme le plus rapide depuis cinq ans. Source : https://www.theregister.com/ai-and-ml/2026/10/29/google-struggling-to-make-ai-mode-searches-pay/5306181

**SK hynix affirme que les pénuries de mémoire dues à l’IA dureront jusqu’en 2030.** Les fabricants de matériel relocalisent une partie de leur production de PC en Chine pour réduire les coûts des composants, tandis que SK hynix a annoncé un bénéfice record et des contrats de long terme couvrant plus de la moitié de sa production de 2027 et 2028. Sources : https://www.theregister.com/systems/2026/10/28/sk-hynix-says-memory-shortages-to-persist-until-2030/5305887, https://asia.nikkei.com/business/technology/tech-asia/hp-and-asus-shift-some-pc-making-back-to-china-due-to-ai-driven-cost-hikes

**Les commandes de robots en Amérique du Nord ont augmenté de 24,8 % au troisième trimestre, à 10 989 unités.** Elles représentaient 723,5 millions de dollars. Les commandes pour les composants automobiles ont augmenté de 90,4 %, tandis que celles de l’alimentation et des biens de consommation ont baissé de 23,7 % ; les statistiques couvrent largement les robots industriels, pas uniquement les machines pilotées par IA. Source : https://www.therobotreport.com/north-american-robot-orders-climb-24-8-q3-2026-says-a3/

## Techniques de prompt

**Simon Willison a partagé une courte séquence de prompts pour développer des jeux de navigateur.** Il demande explicitement three.js, inclut « Réfléchis bien à la manière de le rendre à la fois amusant et beau » dans le premier prompt, puis poursuit avec « Rends-le BEAUCOUP plus amusant ». Les éléments présentés sont quatre projets et son propre jugement, pas une comparaison contrôlée. Source : https://simonwillison.net/2026/Oct/28/vibe-game-development/

## Ce que les gens construisent

**PROMETHEVS exécute le modèle DeepSeek V4.1 de 510 Go sur un PC doté de 64 Go de RAM et d’une RTX 3060 de 12 Go.** Il charge progressivement les poids depuis deux disques NVMe et recalcule les tokens incertains avec des poids FP4 corrigés. Son créateur annonce 5,8 tokens par seconde à froid et 98,3 % de concordance sur 960 tokens audités, sur une seule machine et sans comparaison avec une implémentation de référence. Source : https://github.com/Magnvs7/Promethevs

**LFM3 WebGPU Workspace exécute un petit agent de programmation entièrement dans un navigateur.** La démonstration donne à LFM3-1.7B un système de fichiers virtuel, un terminal et des outils d’édition, tout en conservant prompts et fichiers dans IndexedDB. La fiabilité sur des tâches de programmation en production reste non testée. Source : https://huggingface.co/spaces/webml-community/LFM3-1.7B-WebGPU-Pi

**Grim Prompter transforme la modélisation des menaces en compétence pour les agents de programmation.** Ses 36 workflows d’architecture et ses 29 méthodes guident Claude Code ou Codex pour inspecter les frontières de confiance et produire des rapports JSON reliés aux preuves. Il s’agit d’ingénierie de prompts plutôt que d’un scanner de sécurité. Source : https://github.com/jmanico/grim-prompter

**Soulgent représente les longues sessions d’agents de programmation comme des travailleurs dans un bureau affiché à l’écran.** Les sessions s’installent à des bureaux, attendent une fois terminées et font la queue lorsqu’elles ont besoin d’une décision. L’auteur indique que l’interface aide à superviser plus de 40 sessions réparties entre quatre équipes. Source : https://github.com/Ericcc0321/soulgent

**GEAR permet à un méta-agent de réviser l’environnement d’exécution d’un agent après des échecs récurrents.** Il peut modifier les modèles, les instructions, les outils et les workflows, puis évaluer et mettre en service la révision. Le code est ouvert, mais l’article est encore annoncé comme « à paraître » : les résultats de performance restent donc des affirmations d’auteurs non évaluées. Source : https://rsi-gear.github.io/

## À lire

**Une petite expérience a montré que des modèles hybrides peuvent cacher leur raisonnement dans leur état récurrent.** Un modèle OLMo hybride suivait une tâche d’interrupteur sur une longueur double de celle de son entraînement avec une précision de 0,89, alors que les contrôles plafonnés et denses retombaient près du hasard. L’auteur souligne qu’il s’agit d’une seule tâche avec six graines aléatoires. Source : https://divagr.com/blog/hybrid-models-can-hide-reasoning-in-their-rnn-state

**Qwenputer compile un processeur RISC-V dans les poids récurrents de Qwen3.5.** Cette modification non entraînée a rejoué environ 230 000 positions de sortie sans écart avec une machine de référence et atteint 97,5 à 100 % aux tests d’arithmétique exacte. Ce sont les mesures du créateur. Source : https://divagr.com/blog/qwenputer

**Un script d’empreinte numérique semble utiliser un prompt caché comme défense contre les LLM.** Des chaînes obscurcies décrivent des contenus interdits et des balises Unicode invisibles se décodent en prompt de jailbreak. Le chercheur rapporte que GPT-6 Astra a refusé de l’analyser, tandis que GLM-5.3 l’a fait. Source : https://nullpt.rs/fingerprinting-bioweapons

**Des chercheurs en bases de données estiment que l’optimisation par IA a rendu les benchmarks fixes défaillants.** Ils montrent des systèmes exploitant les hachages, les prédicats répétés et les limites sans ordre pour paraître rapides tout en renvoyant des résultats faux. Leur remède proposé combine des requêtes imprévisibles, des mises à jour et des systèmes antérieurs au test. Source : http://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html

**Epoch AI a cartographié les importations nationales de capacité de calcul pour l’IA à partir des données douanières.** L’organisation estime qu’environ 72 % de la capacité expédiée depuis 2022 est allée aux États-Unis et environ 10 % à la Chine. La méthode publique recense les lacunes des classifications douanières et compare les relevés aux estimations de ventes de puces. Source : https://epoch.ai/latest/introducing-the-ai-chip-imports-explorer

## Hacker News

**Artificial Analysis v5 a relancé le débat sur les benchmarks privés et les classements de pointe.** L’indice utilise désormais des jeux de test privés pour 60 % de son score et affiche un écart de 12 points entre le modèle en tête et les meilleurs poids ouverts publiés. Les commentateurs ont contesté le dispositif de test et se sont demandé si les prompts privés empêchaient la vérification publique des erreurs ; ce sont des préoccupations de la communauté, pas des résultats de recherche. Source : https://news.ycombinator.com/item?id=50268868

**Stack Overflow est passé sous les 1 000 questions mensuelles selon une requête de données reproductible.** Les commentateurs ont mis en cause à la fois les assistants d’IA et la culture du site, puis demandé sur quoi les futurs systèmes s’entraîneront si les nouveaux problèmes techniques ne rejoignent plus une archive publique. Source : https://news.ycombinator.com/item?id=50282454

## YouTube

**AI Engineer a publié le récit d’Anthropic sur le passage de la revue de code à 30 000 modifications fusionnées par jour.** Addy Osmani décrit Claude effectuant une première revue avec des preuves de vérification. Le chiffre de débit vient des intervenants, et Sonar vend des outils de revue. Source : https://www.youtube.com/watch?v=AnsXWH2_EBU

**AI Engineer a publié le récit d’Arize sur la reconstruction de son agent Alex entre 2023 et 2026.** Fuad Ali indique qu’un agent unique avec planification, compétences et un seul fichier mémoire de 8 000 caractères fonctionnait mieux que dix spécialistes et des systèmes de stockage plus élaborés. Il s’agit du récit de production d’un fournisseur. Source : https://www.youtube.com/watch?v=YIhvrvHtonk

**Un essai pratique tchèque a comparé six modèles locaux sur un NVIDIA DGX Spark.** Libor Kovář a utilisé des tâches de bureau, comme transformer des notes en courriel et des enregistrements en workflows, en rapportant la latence et les points nécessitant une vérification manuelle. La version d’octobre ajoute une comparaison avec un ordinateur portable RTX 5080 et Cerebras. Source : https://www.youtube.com/watch?v=Virmsfh2yHY

## En bref

**Le bureau d’enregistrement britannique 123 Reg a attribué une fuite de données clients à des outils assistés par IA liés au groupe ARTEX.** L’intrusion a exposé des coordonnées et des métadonnées de comptes par une API. Cette attribution est la conclusion de l’enquête du bureau d’enregistrement sur l’incident. Source : https://www.theregister.com/cyber-crime/2026/10/28/123-reg-discloses-ai-cyberattack-on-customer-data-suspects-china-nexus/5305936

**Cisco a publié Project Quarry en open source pour détecter des schémas nuisibles sur des sessions entières d’agents.** Les règles peuvent relier la lecture d’un fichier sensible à un envoi externe ultérieur et couvrent les conversations de LLM, les appels d’outils et MCP. Source : https://www.theregister.com/security/2026/10/28/cisco-open-sources-tool-for-detecting-ai-agents-on-hacking-sprees/5305867

**Cinq nouvelles failles publiées introduisent d’anciens échecs de sécurité dans l’infrastructure des agents et de MCP.** Elles comprennent une injection de prompt exposant les variables d’environnement, des SSRF, l’accès à des artefacts entre applications, des erreurs d’autorisation et une protection contre le rebinding DNS désactivée. Source : https://nvd.nist.gov/vuln/detail/CVE-2026-115415

**Une analyse de 7 256 531 dépôts publics Gitee a trouvé 26 400 identifiants uniques encore valides.** Le chercheur de MongoDB Ben Zimmermann a utilisé TruffleHog et Kingfisher et documenté la méthode d’énumération et de vérification. Source : https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets

**Des responsables démocrates de commissions de la Chambre des représentants ont demandé aux laboratoires de pointe de signaler les incidents graves d’IA sous 48 heures.** Il s’agit d’une lettre de contrôle parlementaire, pas d’une obligation légale ; les incidents touchant des infrastructures critiques devraient être signalés sous 24 heures. Source : https://democrats-energycommerce.house.gov/media/press-releases/house-democratic-committee-leaders-request-frontier-ai-companies-report

**New York a interdit aux chatbots destinés aux mineurs de se faire passer pour humains, d’encourager l’automutilation ou de tenir des conversations inappropriées.** La gouverneure Kathy Hochul a signé cette mesure avec une loi complémentaire sur les babyphones connectés. Source : https://www.governor.ny.gov/news/governor-hochul-signs-nation-leading-legislation-protect-kids-ai-chatbots-and-ensure-baby

**HHS a supprimé les exigences de transparence des fiches de modèles dans les systèmes informatiques de santé certifiés.** La règle définitive retire les obligations d’information sur l’entraînement, l’usage prévu, les limites et les performances selon les groupes de patients. ONC indique n’avoir trouvé aucune preuve que les utilisateurs s’appuyaient sur ces informations ou qu’elles amélioraient les soins. Source : https://www.federalregister.gov/documents/2026/10/28/2026-21943/health-data-technology-and-interoperability-onc-deregulatory-actions-to-unleash-prosperity

**Le US Copyright Office a indiqué soutenir le renouvellement de l’exemption pour la fouille de textes et de données.** Il a rejeté comme non étayée l’affirmation d’un éditeur selon laquelle les corpus exemptés seraient détournés vers l’entraînement d’IA génératives. Source : https://www.federalregister.gov/documents/2026/10/28/2026-21939/exemptions-to-permit-circumvention-of-access-controls-on-copyrighted-works

**Le chinois CXMT prévoirait une production de HBM3E avec un rendement de 20 à 30 %.** Reuters, relayé par The Next Web, compare ce chiffre à environ 70 % chez SK hynix et indique qu’une production limitée pourrait débuter d’ici deux mois. Source : https://thenextweb.com/news/cxmt-hbm3e-ai-memory-low-yields-reuters

**Les douanes malaisiennes ont saisi 12 millions de dollars de puces d’IA avancées cachées dans 30 serveurs.** Les autorités ont décrit la Malaisie comme un point de transit d’un réseau de contrebande et relié 25 millions de dollars de saisies à l’organisation soupçonnée. Source : https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub

## Économie en bref

**Microsoft a enregistré 10 milliards de dollars de revenus trimestriels liés à ses accords avec OpenAI, soit environ 11 % de son total de 92,3 milliards.** Source : https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/

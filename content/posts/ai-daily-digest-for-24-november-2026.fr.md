+++
title = "Synthèse IA du 24 novembre 2026"
slug = "synthese-ia-du-24-novembre-2026"
description = "La Chine a intégré l'IA dans les services de sécurité sociale de 15 régions, tandis que Singapour a relevé sa prévision de croissance grâce à la demande en électronique liée à l'IA. Aleph Alpha a publié un modèle de raisonnement ouvert germano-anglais, et une version quantifiée de 10 Go a tenu tête à son modèle source de 54 Go sur plusieurs benchmarks d'agents."
tags = ["models", "research", "agents", "business"]
date = 2026-11-24T03:58:39+01:00
draft = false
+++

## À la une

**La Chine indique que l'IA a traité sept millions de dossiers de sécurité sociale dans une seule province.**

Un rapport de l'Organisation internationale du travail (OIT) recense 45 déploiements dans 15 régions de niveau provincial. Parmi eux, 47 % améliorent la prestation de services, 33 % soutiennent l'administration et le reste concerne la gestion des risques ou l'aide à la décision.

Dans le district de Haidian à Pékin, des systèmes automatisés ont traité plus de 70 000 transactions en 2024 et accru l'efficacité de traitement de plus de 80 % par rapport au travail manuel. Dans le Guangdong, les systèmes d'examen avaient traité plus de sept millions de dossiers répartis sur 34 services en juillet 2025, économisant plus de 640 000 heures de travail.

Les cas ont été sélectionnés avec le ministère chinois du Travail et ne constituent pas un échantillon représentatif. L'OIT indique que les décisions relatives à l'admissibilité aux prestations et aux accidents du travail doivent rester aux mains d'humains, tandis qu'un service hors ligne doit demeurer accessible aux personnes confrontées à des obstacles numériques.

Source : https://www.ilo.org/resource/news/ai-transforming-social-security-services-china-new-ilo-report-finds

**Singapour a relevé sa prévision de croissance pour 2026 à environ 6 %, la demande d'électronique liée à l'IA stimulant ses exportations.**

L'économie a progressé de 6,1 % en glissement annuel au troisième trimestre. Les autorités attribuent une large part de ce dynamisme à l'électronique portée par le cycle d'investissement dans l'IA et ont revu à la hausse leur estimation pour l'ensemble de l'année.

Les perspectives ralentissent à 2,5–4,5 % en 2027. Cet écart compte pour une économie exportatrice dont les livraisons de semi-conducteurs et de serveurs dépendent désormais de la poursuite des dépenses en centres de données à l'étranger ; il s'agit d'une prévision officielle et non d'une mesure de la productivité de l'IA au sein des entreprises singapouriennes.

Sources : https://asia.nikkei.com/economy/singapore-gdp-grows-6.1-in-q3-as-ai-demand-stays-strong, https://www.bloomberg.com/news/articles/2026-11-24/singapore-raises-gdp-growth-outlook-to-around-6-on-ai-boom

**Aleph Alpha a publié Kolibri 1.1, doté de 75 milliards de paramètres et de 262 144 tokens de contexte natif.**

Ce modèle de raisonnement germano-anglais sous licence Apache-2.0 active 3,44 milliards de paramètres par token. Ses poids occupent environ 77,6 Go : l'architecture clairsemée réduit donc le calcul plutôt que la mémoire.

Aleph Alpha fait état d'une moyenne de 73,2 sur ses benchmarks (bancs d'essai) post-entraînement, contre 66,6 pour Kolibri 1.0, tandis que Qwen3.8 Flash Next atteint 80,1 dans le même tableau. La fiche du modèle recommande de rester en deçà ou au niveau de la limite de contexte natif pour les tâches difficiles, bien que l'implémentation puisse s'étendre jusqu'à environ un million de tokens.

Source : https://huggingface.co/Aleph-Alpha/Kolibri-1.1

**Nari Labs a compressé Qwen3.8-27B de 53,8 Go à 10,12 Go sans perdre de terrain sur trois de ses benchmarks.**

NariQ repose sur une quantification post-entraînement par codage en treillis, calibrée sur des traces d'agents de programmation. La version trois bits du laboratoire a obtenu 41,0 sur DeepSWE contre 39,8 en BF16, 63,8 contre 62,6 sur Terminal-Bench et 98,3 contre 97,7 sur AIME 2025–26.

La version deux bits, plus compacte, est tombée à 28,6, 52,4 et 86,0 sur ces mêmes tests. Les fichiers exigent en outre le fork de llama.cpp maintenu par Nari Labs, optimisé pour l'architecture SM120 de Nvidia, plus lent sur les cartes Nvidia plus anciennes et sur Metal, et dépourvu de prise en charge des GPU AMD ou Intel.

Source : https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF

**Les deux tiers de 58 clients d'Anthropic indiquent que l'IA a réduit leurs recrutements.**

L'équipe d'économistes d'Anthropic a mené 66 entretiens auprès d'entreprises clientes aux États-Unis. Deux sociétés seulement avaient supprimé un poste par automatisation et cinq avaient écarté des salariés réfractaires à l'IA, tandis que dix ont recruté davantage, principalement pour le déploiement et le support informatique.

L'effet s'est manifesté plus souvent à l'embauche : les deux tiers ont déclaré recruter moins, et environ un tiers de ce groupe a réduit certaines fonctions par attrition naturelle. Neuf entreprises ont diminué le recours aux prestataires externes. Sur 100 logiciels développés par IA décrits avec assez de précision pour être classés, 80 automatisaient des tâches manuelles et 20 remplaçaient des logiciels achetés.

L'échantillon est restreint, non aléatoire et limité aux propres clients du fournisseur. Les appréciations de valeur étaient surtout qualitatives et autodéclarées plutôt que mesurées dans des essais contrôlés.

Source : https://www.anthropic.com/research/working-with-ai

## Nouveaux modèles et sorties

**Ant Group a publié Ling-3.2-air, un modèle de 124 milliards de paramètres sous licence MIT.** Le modèle active 5,5 milliards de paramètres et associe 35 couches d'attention linéaire à sept couches d'attention à portes. L'éditeur fait état d'un taux de réussite par critère de 87,7 % sur son benchmark juridique, mais seuls 0,8 % des échantillons ont satisfait l'ensemble des critères après vérification des hallucinations matérielles ; aucun rapport technique n'accompagne la fiche du modèle.

Source : https://huggingface.co/inclusionAI/Ling-3.2-air

**Tencent a publié cinq modèles vision-langage WeMM-Ecom destinés au commerce en ligne.** Les tailles vont de 0,8 milliard de paramètres à un modèle de mélange d'experts de 35 milliards de paramètres qui en active 3 milliards. Tencent annonce un gain de 3,92 points sur 28 benchmarks de commerce électronique par rapport à sa base Qwen3.5, mais seulement 0,17 point sur 64 benchmarks généraux ; ces scores proviennent de la version BF16 et non des nouvelles variantes quantifiées.

Source : https://huggingface.co/tencent/WeMM-Ecom-35B-A3B-GPTQ

**AI Singapore a ajouté un décodeur spéculatif de 2 milliards de paramètres à son modèle SEA-LION de 9 milliards.** L'éditeur a mesuré entre 2,26 et 3,08 fois plus de tokens par seconde avec une concurrence de 1, à partir d'une référence proche de 195 tokens par seconde. L'avantage se réduit à 1,5 fois au maximum à une concurrence de 16 et peut disparaître à 32 : il s'agit donc d'un outil de réduction de latence à faible charge plutôt que d'un accélérateur de haut débit.

Source : https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-9B-SpecDecoder

**Anthropic retirera Claude Opus 4.5 le 22 janvier 2027 et a ouvert Enterprise Frontier Safeguards en version bêta.** Ces garde-fous maintiennent le mode Zero Data Retention (conservation nulle des données) tout en stockant des copies chiffrées des prompts (instructions) et des réponses dans le propre compte cloud du client à des fins d'examen de sécurité. Les équipes épinglées sur `claude-opus-4-5-20251101` disposent d'environ deux mois pour migrer vers Opus 5.5.

Source : https://platform.claude.com/docs/en/release-notes/api

**Les utilisateurs de l'API Gemini peuvent désormais ne payer que pour les pages, cellules et segments médias sélectionnés au lieu de fichiers entiers.** Le découpage de fichiers fonctionne sur l'ensemble des modèles Gemini 4 et ajoute l'envoi natif de fichiers Office et OpenDocument. Vercel a mesuré 14 fois moins de tokens lors du survol de texte extrait de PDF ; LiteLLM a mesuré 67 % de tokens en moins pour un PDF et 33 % de moins pour un classeur, deux essais rapportés par des partenaires sans tarifs ni plafonds numériques de fichiers.

Source : https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/

## Recherche

**Un audit n'a vérifié que 29,3 % des tâches dans six suites de benchmarks multi-étapes.** Deux auteurs ont examiné 749 tâches issues de huit benchmarks ainsi que 767 évaluations publiques de modèles. Les défauts confirmés ont privé des solutions conformes de leur crédit dans 71,7 % des cas, tandis que le reste permettait des raccourcis ; des conteneurs corrigés ont ramené les contournements d'exécution confirmés de 14,7 % à 2,7 %. Il s'agit du premier jalon d'un examen en cours, et le protocole des auteurs définit ce qui est considéré comme vérifié.

Source : https://arxiv.org/abs/2611.27622

**Une méthode par graphe de raisonnement distingue les chaînes de pensée fidèles des chaînes efficaces.** Les auteurs évaluent si le soutien sémantique explique la prédiction d'un modèle et si les étapes restent sur un chemin menant à la réponse. Infidélité et inefficacité n'étaient que faiblement ou irrégulièrement corrélées à l'exactitude, et un affinage (fine-tuning) ciblé a amélioré chaque propriété sans abaisser la précision ; le résumé ne donne pas de tailles d'effet et le résultat dépend de la construction du graphe retenue par les auteurs.

Source : https://arxiv.org/abs/2611.27100

**Quatorze modèles de langage ont adopté un schéma « compresser puis comparer » lorsqu'ils choisissent entre plusieurs options.** Sur 12 benchmarks, les couches intermédiaires ont compressé le prompt dans un goulot d'étranglement de faible rang avant que les couches ultérieures ne le déploient dans une géométrie de comparaison. Des interventions de faible rang près de ce goulot ont modifié les préférences ultérieures, mais l'article NeurIPS, signé par un seul auteur, établit ce schéma au moyen de sa propre méthode de covariance.

Source : https://arxiv.org/abs/2611.26874

**Des répondants synthétiques d'enquêtes n'ont reproduit que 0,4 à 10,5 % de la variation des préférences humaines.** Trois familles de modèles ouverts ont rejoué les choix politiques de 1 991 adultes chiliens, 843 français et 434 brésiliens. Aucune des 27 conditions n'a reproduit simultanément les choix individuels, l'hétérogénéité de la population et l'organisation politique ; inverser l'ordre des propositions a modifié entre 12,3 et 31,2 % des choix des modèles.

Source : https://arxiv.org/abs/2611.28383

**Les modèles de décision rapide font gagner du temps, mais deviennent nettement plus faciles à empoisonner.** Quatre modèles ont atteint en moyenne 91 % de précision sur entrées saines sur 1 440 paires synthétiques de tâches de navigateur, tandis que des commentaires injectés en deux exemples ont obtenu un taux de réussite d'attaque de 81,2 %. Sur 48 tâches appariées, une courte chaîne de pensée a répondu correctement à 95,83 % des entrées empoisonnées contre 38,54 % pour la variante rapide, en 1,94 seconde contre 0,29 seconde. Un autre modèle Système 1 de 4 milliards de paramètres revendique un coût par épisode inférieur de 75 à 91 % sur trois benchmarks, mais n'a pas été testé face à des entrées adverses.

Sources : https://arxiv.org/abs/2611.27679, https://arxiv.org/abs/2611.23751

**Certains tests d'interprétabilité peuvent certifier une caractéristique que le modèle n'utilise pas comme annoncé.** L'article construit des « caractéristiques parasites » qui combinent une direction distinguant les entrées avec une autre orientant les sorties, réussissant ainsi un test d'abstraction causale par des voies sans rapport. Les expériences mettent en évidence cette faille dans l'accord syntaxique et l'addition à deux chiffres ; le résultat constitue une mise en garde issue de deux tâches et non une méthode de remplacement.

Source : https://arxiv.org/abs/2611.26711

**Un benchmark d'état cérébral a montré que la prédiction de stimulus n'implique pas le suivi de l'état interne d'un spectateur.** Les encodeurs fondés uniquement sur le stimulus ont atteint une corrélation de prédiction de 0,320, mais zéro sur la mesure State du benchmark. Le modèle à deux échelles de temps des auteurs a atteint 0,349 de corrélation, 5,5 % sur State, 16 % sur Forecast et 20,3 % sur Updating, la performance absolue sur State restant faible.

Source : https://arxiv.org/abs/2611.28508

**La plupart des tests d'équivalence réussis en simulation humaine dans un audit auraient aussi validé un modèle à effet nul.** Dans une réanalyse de 70 expériences, 72 % des réussites de GPT-4 avec une marge de plus ou moins 0,20 écart-type étaient des validations compatibles avec un effet nul. Une simulation préenregistrée sur Claude a satisfait trois objectifs d'intention, mais n'a déplacé les croyances normatives que de 0,065 écart-type contre 0,351 chez les humains ; l'article signale des ajouts a posteriori dans une partie de son analyse.

Source : https://arxiv.org/abs/2611.27186

**Un adaptateur à capacité fixe a appris quoi retenir et quand oublier.** Un contrôleur attribue aux souvenirs des taux de décroissance indépendants dans un adaptateur LoRA et a atteint 86 % de la performance oracle sur les trajectoires synthétiques d'utilisateurs conçues par les auteurs. Une étude connexe a constaté que le mélange de trajectoires courtes et longues permet d'apprendre des règles stables avec moins de tokens, mais les deux résultats proviennent d'environnements construits.

Sources : https://arxiv.org/abs/2611.25235, https://arxiv.org/abs/2611.28613

**L'ajout d'un second partenaire d'IA a produit davantage d'idées en remue-méninges, mais réduit la contribution humaine.** L'étude en laboratoire (N = 168) a comparé des salles comptant deux agents à des binômes humains ; seul le second agent a accru la différenciation au sein d'une séance. La tâche était étroite et le résultat observé avec un seul agent ne s'est pas généralisé. Source : https://arxiv.org/abs/2611.26663

**Un modèle comportemental spécialisé et deux audits divergent sur ce qu'exigent de bons répondants synthétiques.** Chiron, entraîné sur 288 307 dossiers et 1 411 750 décisions, revendique une prédiction individuelle supérieure jusqu'à 28,4 % à celle des modèles de pointe et une erreur sur la taille d'effet réduite de 82,2 à 94,3 %. L'audit sur les publics synthétiques a mis en évidence une variation fortement comprimée, tandis que l'audit d'équivalence a montré que de nombreuses correspondances apparentes valident aussi des effets nuls ; tous reposent sur des tâches choisies par leurs auteurs.

Sources : https://arxiv.org/abs/2611.24830, https://arxiv.org/abs/2611.28383, https://arxiv.org/abs/2611.27186

## Économie et travail

**Les entreprises cotées présentant une plus forte exposition mesurée aux agents ont ensuite publié moins d'offres d'emploi non seniors.** Un document de travail relie environ deux billiards de tokens de modèles à 34,8 millions d'offres. Une hausse d'un écart-type de sa mesure d'exposition boursière a précédé une croissance des offres inférieure de 2,11 % après six mois et de 3,20 % après neuf mois ; le résultat porte sur les offres publiées, non sur les licenciements, et déduit l'exposition des réactions du marché.

Source : https://arxiv.org/abs/2611.27210

**Claude Ship fait passer les agents de programmation de l'écriture du code à sa revue et à son approbation.** Anthropic affirme que le nombre de pull requests fusionnées a plus que doublé entre juin et septembre tandis que la part annulée reculait de plus de 40 %, sans publier de dénominateurs ni de groupe de comparaison. Code Review est disponible en version générale, tandis que PR Steward et Approvals restent en bêta ; les administrateurs peuvent plafonner la dépense facturée en tokens.

Source : https://claude.com/resources/articles/introducing-claude-ship

**Un modèle économique indique que des tâches lentes jouant un rôle de « maillon faible » peuvent bloquer des gains explosifs issus d'un capital en progrès rapide.** Le document de travail du NBER estime que la productivité des tâches complémentaires du capital progresse d'environ cinq points de pourcentage par an plus vite que celle des tâches de travail humain. Son fort résultat de croissance agrégée dépend de la substitution des tâches et des goulets d'étranglement dans le modèle : il décrit donc un mécanisme plutôt qu'une prévision.

Source : https://www.nber.org/papers/w36050

**AlphaFold2 a orienté les expériences de biologie structurale vers des protéines proches d'exemples déjà connus.** Un article du NBER suit 530 471 protéines et constate que des prédictions confiantes ont augmenté les expériences sur des protéines connues et leurs proches parentes tout en réduisant les tentatives portant sur des premières structures éloignées. L'étude mesure vers quoi les chercheurs ont dirigé leurs expériences, et non la valeur scientifique finale de ces choix.

Source : https://www.nber.org/papers/w36045

## Techniques de prompt

**Un bloc de prompt aligné sur OWASP a réduit d'environ un tiers les alertes d'analyseurs dans les applications web générées par IA.** Cent spécifications ont été implémentées quatre fois avec Claude Code et Codex, produisant 6 721 alertes triées. Le ratio de taux d'incidence s'est établi à 0,65, avec un intervalle à 95 % compris entre 0,60 et 0,71, mais le bloc a doublé les dépendances déclarées et les alertes d'analyseurs ne constituent pas des exploits avérés.

Source : https://arxiv.org/abs/2611.28408

**Demander à un modèle de vérifier un texte récupéré l'a conduit à adopter davantage de réponses fausses.** FutureBench a évalué 3 629 questions sur six modèles. Un avertissement précisant que les passages peuvent induire en erreur a rétabli entre 82,5 et 98,9 % des bonnes réponses évincées par le prompt Verify ordinaire, avec moins d'un point d'écart sur les passages vrais ; le résultat provient d'une seule famille de benchmarks construite par deux auteurs.

Source : https://arxiv.org/abs/2611.23601

## Ce que les gens construisent

**Gall fait tourner un modèle de mélange d'experts de 26 milliards de paramètres sur un MacBook Air de 24 Go en le déchargeant après chaque réponse.** Le moteur écrit en Rust et Metal sauvegarde l'état de la conversation, retombe à 32–57 Mo de mémoire au repos et recharge un état chaud en environ 0,1 seconde. Son auteur a mesuré environ 20 tokens par seconde en contexte court et 16 à 29 900 tokens sur un Air M2 ; la qualité du modèle et le réglage annoncé à 100 000 tokens n'ont pas été évalués.

Source : https://github.com/ltrgoddard/gall

**OCRia-nano-1 analyse des documents sur processeur avec 8,1 millions de paramètres.** LlamaIndex fait état de 59,2 sur ParseBench-2 et de 27,8 pages par seconde sur 16 processeurs virtuels. Le score sur les graphiques n'est que de 3,1 contre 77,4 pour son modèle enseignant de 4 milliards de paramètres, et les poids relèvent d'une licence spécifique limitant les grands utilisateurs commerciaux.

Source : https://huggingface.co/llamaindex/OCRia-nano-1

**OpenToolSearch emploie deux modèles de 0,6 milliard de paramètres pour sélectionner des outils dans de vastes catalogues.** Son module de reclassement atteint un nDCG@10 de 70,8 sur le jeu public ToolRet et de 89,0 sur le jeu des auteurs, pour un coût annoncé de 0,19 dollar pour 1 000 recherches et une latence médiane de 0,10 seconde. Les concurrents obtiennent des scores plus élevés sur les deux tests, et les auteurs recommandent de fournir la liste complète directement au modèle lorsqu'elle contient environ 200 outils ou moins.

Source : https://github.com/ai3inc/opentoolsearch

**CubePod offre aux agents de programmation des bacs à sable persistants en microVM Kata.** Le projet Kubernetes compatible E2B revendique une attribution depuis un pool chaud en moins de 50 millisecondes et une reprise internœud ou des copies à l'écriture (copy-on-write) proches d'une seconde. Ces chiffres ne s'accompagnent d'aucune méthode publiée, et le déploiement exige Kata Containers ainsi qu'un pilote de stockage en mode bloc. Source : https://github.com/cubeplexai/cubepod

**Deux petits outils protègent les dépendances d'agents à deux moments distincts.** mcpwatch verrouille les descriptions d'outils MCP et bloque à l'exécution les outils modifiés, mais ses notes de sécurité ne valent pas garantie et sa méthode d'empreinte n'est pas documentée. slop-deps compare les importations à 4 179 noms de paquets et registres, avec détection de fautes de frappe et d'homoglyphes ; son exemple de temps d'exécution sur 142 fichiers est illustratif et l'ensemble de son code a été écrit par des agents sous direction humaine.

Sources : https://www.mcpwatch.io, https://github.com/viditx/slop-deps

**Terminal Tasks Open publie 30 tâches ainsi qu'un audit des défauts d'un benchmark plus vaste.** Son auteur signale des défauts dans 23 des 66 tâches de Terminal-Bench 4.1 et classe environ 52 % des 980 essais d'agents échoués en surapprentissage, 31 % en erreur de jugement et 9 % en mauvaise manipulation. L'auditeur a également conçu le benchmark de remplacement et commercialise une chaîne d'évaluation, tandis que ces catégories lui sont propres.

Source : https://vetto.ai/companies/terminal-tasks-v2/

## À lire

**Hugging Face montre comment un benchmark d'agents peut récompenser un raccourci plutôt que la tâche visée.** Un script a renvoyé le bon ratio de défauts sur l'ensemble des huit tâches de spectre Raman sans ajuster les pics, obligeant les auteurs à ajouter des vérifications pic par pic. gpt-oss-120b a réussi 11 essais sur 24, puis 13 lorsque seul le fournisseur d'inférence a changé ; trois modèles plus puissants ont réussi les 24 essais, si bien que ce petit jeu adapté ne permet pas de les départager.

Source : https://huggingface.co/blog/agentic-evals

**Un essai soutenu par AMD a remplacé un pool DRAM de cache KV d'agents par du NVMe à débit quasi équivalent.** Avec Kimi-K3 sur 16 GPU MI355X, trois tests de concurrence sont restés à moins de 1 % de la DRAM, tandis que le taux de succès du cache expliquait 96 % de la variation du débit sur 42 essais. Les disques NVMe épuiseraient leur endurance d'écriture nominale en environ 5,5 mois si chaque bloc était stocké à 96 sessions, et la plupart des comparaisons reposaient sur des essais uniques avec environ 2,5 % de bruit.

Source : https://vllm.ai/blog/2026-11-23-skip-the-dram-tier

**Des équipes d'agents Gemini 4 ont trouvé des circuits quantiques moins coûteux et démontré chaque résultat dans Lean.** Google DeepMind fait état d'un coût de calcul réduit d'un facteur 11,8 pour une simulation de fusion, de 2,5 pour le cytochrome P450 et de 290 pour une routine arcsin. Des humains ont sélectionné et supervisé les problèmes, et les circuits obtenus dépassent encore la capacité probable des premiers ordinateurs quantiques à correction d'erreurs.

Source : https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

**Anthropic a publié une affirmation rédigée par IA selon laquelle VP diffère de VNP, assortie d'une preuve Lean mais sans examen mathématique humain.** Le dépôt indique qu'un noyau indépendant vérifie les énoncés formels avec des axiomes standard. Rien ne vérifie automatiquement que ces énoncés correspondent aux affirmations de l'article, et le projet se présente comme un instantané non maintenu ; il ne tranche pas le problème P contre NP.

Source : https://github.com/anthropics/formal-math/tree/main/vp-vnp

## Hacker News

**GLM-5.4 fait des couches de transformeur en boucle une deuxième tendance d'architecture en une semaine.** Z.ai indique que des couches partagées s'exécutent de manière répétée pour accroître la profondeur effective sans ajouter de paramètres, et Simon Willison rapproche cette idée d'Inkling 2 Mini de Thinking Machines. Son test pratique s'est limité à un seul prompt d'image, les poids ne sont pas ouverts et les sources accessibles ne donnent ni nombre de paramètres ni benchmark formel ; le fil de discussion sur Hacker News a atteint 1 075 points.

Sources : https://simonwillison.net/2026/Nov/23/glm-54/, https://news.ycombinator.com/item?id=50609685

## YouTube

**Dex Horthy, de Factory, propose 12 contrôles pour les logiciels construits par des agents.** Cette conférence en anglais donnée lors d'AI Engineer aborde la planification, la pression entre étapes, les indicateurs de fonctionnalités (feature flags), les évaluations et les agents qui testent leur propre travail. Horthy affirme que le meilleur modèle atteint environ 16 % sur Slop Code Bench, sans préciser le nombre de tâches ; Factory vend des agents de programmation, si bien que ces règles relèvent de la pratique d'un fournisseur plutôt que d'un résultat contrôlé.

Source : https://www.youtube.com/watch?v=-NFMsM2y0Vk

**Le cours CS312 de Stanford demande aux étudiants de prédire les résultats d'entraînement avant de les observer.** Son modèle à huit couches de 30 millions de paramètres s'entraîne en environ dix minutes sur un seul GPU, rendant les expériences sur le taux d'apprentissage et l'architecture assez peu coûteuses pour un cours. Ce résumé s'appuie sur la description en anglais de la vidéo plutôt que sur une transcription. Source : https://www.youtube.com/watch?v=JLcCYvUawsM

## En bref

**Un même moniteur de sécurité a manqué 0,2 % ou 23 % des attaques réussies selon la manière dont elles étaient générées.** Le UK AI Security Institute a testé un ancien moniteur de production d'OpenAI face à des attaques produites par plusieurs politiques ; une exécution d'apprentissage par renforcement a fait passer le taux d'échec de détection de 0,5 % à 20,8 %. Il ne s'agit que d'une configuration, mais cela montre que les scores synthétiques d'un moniteur ne peuvent se suffire sans démontrer que la politique d'attaque représente des attaques futures.

Source : https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading

**OpenAI et Cisco ont publié Shirudo pour bloquer un chemin d'exploitation dans un service Linux en cours d'exécution avant l'installation d'un correctif.** Ses boucliers eBPF signés requièrent l'approbation d'un opérateur et laissent une trace protégée par TPM. Un essai contrôlé des fournisseurs a stoppé Java4Shell contre Elasticsearch sans redémarrage ; la publication ne fournit aucun chiffre de performance ni d'adoption, et le bouclier demeure une mesure temporaire.

Source : https://openai.com/index/introducing-shirudo

**La CISA a ajouté une faille de traversée de répertoire dans MONAI Label à son catalogue de vulnérabilités exploitées.** CVE-2026-133968 peut permettre à un attaquant non authentifié d'écrire hors du magasin de données du serveur d'imagerie médicale et potentiellement d'exécuter du code ; les agences fédérales américaines avaient jusqu'au 26 novembre pour y remédier. Source : https://nvd.nist.gov/vuln/detail/CVE-2026-133968

**Les États-Unis ont ajouté des sociétés affiliées à Megaspeed et une entreprise singapourienne détenue par Alibaba à leur Entity List.** Cette restriction bloque l'achat de puces avancées pendant que les autorités examinent des détournements présumés de puces Nvidia vers la Chine ; Megaspeed nie les avoir expédiées. Source : https://www.bloomberg.com/news/articles/2026-11-24/us-blacklists-alibaba-owned-company-in-setback-to-ai-ambitions

**L'Oregon et la Virginie ont poursuivi des entreprises liées à Elon Musk au sujet d'images sexualisées générées par Grok.** Les États soutiennent que les garde-fous n'ont pas empêché la création d'images de personnes réelles, y compris d'enfants, tandis que X affirme que chaque sortie est filtrée ; la synthèse n'a pas pu accéder aux plaintes, de sorte que les mesures demandées restent non confirmées. Source : https://arstechnica.com/tech-policy/2026/11/states-sue-spacex-to-stop-grok-from-generating-child-sex-images-revenge-porn/

## Économie en bref

Amazon a racheté le logiciel d'optimisation de puces et l'équipe de Decart, pour un montant qui atteindrait 7,5 milliards de dollars ; les entreprises n'ont publié aucun benchmark pour le logiciel. Source : https://www.theregister.com/ai-and-ml/2026/11/23/amazon-scoops-up-ai-accelerator-tech-to-keep-chips-busy-at-all-times/5311754

Les régents de l'Université du Michigan ont approuvé un centre de données de 1,25 milliard de dollars avec Los Alamos par sept voix contre une, tandis que la commune locale maintient un moratoire de six mois sur toute nouvelle infrastructure électrique. Source : https://www.404media.co/ypsilanti-michigan-data-center-vote/

## À surveiller

Anthropic retire Claude Opus 4.5 le 22 janvier 2027. L'échéance de correction de la CISA pour MONAI Label est fixée au 26 novembre, et un webinaire technique sur Shirudo est prévu le 15 décembre.

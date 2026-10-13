+++
title = "Gemini 4 Argon passe des cyberdéfenseurs à l'application Gemini"
slug = "gemini-4-argon-cyberdefenseurs-application-gemini"
description = "Treize jours après une présentation réservée à des cyberdéfenseurs, Google ouvre Gemini 4 Argon aux abonnés payants et aux développeurs. Google promet des réponses plus simples ; les classements indépendants le placent premier sur un tableau et huitième sur un autre."
tags = ["models", "tools", "safety"]
date = 2026-10-13T22:54:03+02:00
draft = false
+++

Une comptable de Brno a trois contrats fournisseurs, un grand livre exporté d'un logiciel mutilant tous les signes diacritiques tchèques et un client voulant une note de rapprochement pour mercredi. Mardi soir, elle ouvre Gemini, touche par habitude le menu et trouve un nom absent le matin : 4 Argon, à côté de 3.1 Pro et 3.8 Flash. Elle colle tout et ajoute une ligne : pas de préambule, ni de résumé de ce que je viens de dire. Personne correspondant à cette description n'a été interrogé. C'est une esquisse de l'abonnée que Google courtise, celle que ses notes imaginent « analysant un rapport financier complexe » ou « créant une présentation depuis des sources dispersées ».

## Deux semaines du programme fermé à l'application

Le 13 octobre, Google commence à déployer Gemini 4 Argon « mondialement pour les abonnés Google AI Pro et Ultra dans l'application Gemini », selon les notes de sortie. Le même jour, il devient généralement disponible dans Gemini API comme gemini-4-argon, ouvre dans Google AI Studio et Android Studio et arrive dans Antigravity pour les abonnés Ultra et clients Gemini Enterprise éligibles. Pro et Ultra peuvent aussi le choisir dans AI Mode de Google Search, rapporte 9to5Google. Les utilisateurs gratuits et AI Plus moins cher ne l'ont pas encore, note Android Police, dont le testeur Pro attend toujours son apparition.

Treize jours avant, le cercle était plus réduit. Quand Koray Kavukcuoglu, vice-président principal Google DeepMind et architecte IA en chef de Google, annonce Argon le 30 septembre, il est réservé à « un ensemble de cyberdéfenseurs de confiance » du Fairwind Program. Google dit participer au processus volontaire américain d'accès avant sortie et poursuivre les garde-fous avant l'ouverture « aux développeurs, entreprises et consommateurs dès que possible », d'abord aux clients API payants et Ultra. Mardi va plus loin, incluant Pro.

Fairwind est à peine plus ancien. Four Flynn, vice-président sécurité et confidentialité, le lance le 2 septembre pour gouvernements, infrastructures critiques et sociétés de sécurité, autour de Gemini 3.8 Flash Cyber et CodeMender. Les participants limitent l'accès à leurs équipes de sécurité, réponse aux incidents ou tests d'intrusion. Google annonce plus de 650 partenaires.

## Ce qui change selon Google pour la personne qui écrit

La courte annonce concerne surtout le style. Argon « répond plus directement avec moins de réserves, ne se répète pas plus que nécessaire et évite les clichés », écrit Google. Pour les longues tâches, il « tient l'utilisateur informé en partageant ses progrès plus souvent et plus efficacement ». Selon 9to5Google, Google affirme aussi un meilleur respect du style que tout Gemini antérieur.

D'autres changements l'accompagnent. Un bouton du chat passe aux tâches, où Gemini continue selon Google « même sans être devant l'ordinateur ». Plus de 40 services, dont Instacart, OpenTable, Adobe et Shopify, se connectent, la plupart seulement en anglais aux États-Unis selon les notes. Sur Mac, l'interface de code agentique Antigravity est intégrée : l'utilisateur approuve le plan, revient au chat et reçoit notification du code construit et testé en arrière-plan.

Derrière l'offre grand public reste la promesse de septembre sur le travail long. La limite de sortie passe de 64 000 à un million de tokens, permettant selon Google de « générer des centaines de milliers de tokens dans une seule trajectoire ». La documentation précise 65 536 par défaut, jusqu'à 1 048 576 en long decode, dans une fenêtre partagée entrée-sortie de même taille.

## La place dans les classements externes

Google annonce 77,9 % sur DeepSWE v1.1, test de longues tâches logicielles, 51,3 % sur AutomationBench de Zapier et 91,7 % sur LVBench pour longues vidéos. Sur CWE-bench v1, test de correction des failles, Argon serait premier ex aequo à 68 %. Ce sont les chiffres du fournisseur. VentureBeat note que Claude Opus 5.5 atteint 66,4 % sur Terminal-Bench 4.0, test de code en ligne de commande, « contre 57,4 % pour Argon ».

Deux classements indépendants divergent. Vals AI pondère finance, code, droit et fiscalité par leur part du PIB américain et classe Argon premier le 13 octobre à 68,90 %, devant Sonnet 5.5 à 67,04 et Opus 5.5 à 66,97. Artificial Analysis donne au mode de haut effort 53 points à son Intelligence Index, huitième sur 216 modèles. L'avance Vals reste sous deux points et Argon ne mène pas du tout chez Artificial Analysis.

La page Artificial Analysis présente un chiffre peu compatible avec moins de mots : 110 millions de tokens de sortie pour l'indice, contre une médiane de 85 millions, soit « quelque peu verbeux ». La réponse lue et le travail pour la produire se mesurent séparément ; la promesse de Google vise la première.

## Les garde-fous de la version publique

Google a plus décrit ses protections que les testeurs externes le modèle. Le lancement dit qu'Argon doit refuser l'aide aux cyberattaques et aux armes chimiques, biologiques, radiologiques et nucléaires, que Google surveille ses activations internes et qu'un système séparé lit raisonnements et actions et peut l'arrêter au-delà de l'intention utilisateur. Pour défenseurs fiables et équipes internes, Google annonce Argon « sans garde-fous cyber ». Les abonnés ont la version protégée.

Des gouvernements ont examiné avant l'ouverture. Outre le processus américain, Kanishka Narayan dit à Londres le 12 octobre que l'AI Security Institute mène « désormais des évaluations rigoureuses des dernières générations », nommant Gemini, rapporte le Guardian. Aucune version n'est précisée. Ni le reportage ni Google n'indiquent les conclusions ou changements éventuels du modèle.

## Le prix et le travail visé

Jusqu'au 30 novembre, les développeurs paient 2 dollars par million de tokens d'entrée et 10 par million de sortie, l'entrée mise en cache coûtant 95 % de moins. À partir du 1er décembre, VentureBeat et 9to5Google annoncent un doublement à 4 et 20 dollars.

L'équipe Antigravity cadre la sortie par une phrase : « Alors qu'Argon est conçu pour les problèmes les plus difficiles, nous sommes aussi enthousiastes pour les futurs modèles utilisables quotidiennement par un ensemble encore plus large de constructeurs. » Elle place Argon du côté du travail long et cher, laissant l'ordinaire à des modèles encore non publiés.

Google apporte des éléments internes : plus de 100 000 personnes Alphabet utilisent Argon mensuellement dans un Antigravity interne ; en quatre semaines, le code écrit par agents augmente de 35 % et les annulations après soumission baissent de 30 %. Argon aurait trouvé quatre bugs critiques dans des modifications de contrôle d'accès déclarées sûres par deux modèles de pointe antérieurs. Ni leurs noms ni l'audit ne sont publics ; Google décrit son propre travail.

À Brno, notre comptable fictive reçoit quatre courts paragraphes, sans compliment ni récapitulatif. Elle contrôle malgré tout les totaux ligne par ligne contre le grand livre, comme lorsque le menu finissait à 3.1 Pro.

## Références

- Artificial Analysis. (2026). *Gemini 4 Argon (High): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/gemini-4-argon
- Bhatia, S. (2026). *Gemini 4 Argon is here, and Google says it'll finally cut down on the AI fluff*. Android Police. https://www.androidpolice.com/gemini-4-argon-available-pro-ultra-subscribers/
- Flynn, F. (2026). *Proactive cyber defense for governments and enterprises*. Google. https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- Franzen, C. (2026). *Google makes Gemini 4 Argon broadly available with limited-time low API pricing of $2/$10 per 1M token*. VentureBeat. https://venturebeat.com/technology/google-makes-gemini-4-argon-broadly-available-with-limited-time-low-api-pricing-of-2-10-per-1m-token
- Google. (2026). *Gemini 4 Argon comes to the Gemini app*. https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- Google. (2026). *Gemini 4 Argon is now available for developers*. https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/
- Google. (2026). *Gemini Apps' release updates & improvements*. https://gemini.google/release-notes/
- Google AI for Developers. (2026). *Gemini 4 Argon*. https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Google AI for Developers. (2026). *Gemini API release notes*. https://ai.google.dev/gemini-api/docs/changelog
- Google Antigravity Team. (2026). *Gemini 4 Argon in Google Antigravity*. https://antigravity.google/blog/gemini-4-argon-in-google-antigravity
- Kavukcuoglu, K. (2026). *Gemini 4 Argon: our next era of frontier intelligence*. Google. https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- Li, A. (2026). *Gemini app rolling out Gemini 4 Argon to AI Pro and AI Ultra*. 9to5Google. https://9to5google.com/2026/10/13/gemini-app-4-argon/
- Milmo, D. (2026). *Cyber-attack similar to OpenAI Medicare breach seems likely in UK, says minister*. The Guardian. https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister
- Vals AI. (2026). *Vals Index*. https://www.vals.ai/benchmarks/vals_index

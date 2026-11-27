+++
title = "GPT-6.2 : la remise au lancement venait d’une erreur de facturation"
slug = "gpt-6-2-la-remise-au-lancement-venait-d-une-erreur"
description = "OpenAI dit avoir sous-estimé pendant neuf jours la consommation de GPT-6.2 Astra et Sol : les abonnés épuisent désormais leur quota respectivement 40 % et 25 % plus vite. Une mesure indépendante indique que ces modèles consacrent moins de tokens au raisonnement, mais peu de paramètres d’un forfait sont vérifiables de l’extérieur."
tags = ["business", "tools"]
date = 2026-11-27T03:17:17+01:00
draft = false
+++

Sur Hacker News, en réaction au message d’un ingénieur d’OpenAI, des utilisateurs comparent leurs compteurs. « Hier soir, il me restait près de 90 % de mon quota, et ce matin, au réveil, tout avait disparu », écrit un abonné Pro sous le pseudonyme seviu. Il n’avait laissé aucun agent tourner pendant la nuit. Un autre, ragequittah, garde de la semaine précédente le souvenir inverse : « Six heures d’Astra, ça représentait 3 %. »

Entre ces deux relevés, il y a le message de l’ingénieur, et un changement dans la façon dont un abonnement à prix fixe décompte une journée de travail.

## La correction

Le 26 novembre à 2 h 50 UTC, Thibault Sottiaux, qui travaille sur Codex et ChatGPT chez OpenAI, a écrit sur X : « Nous avons commis une erreur de facturation au lancement de GPT-6.2. Pour la plupart des utilisateurs, l’usage de GPT-6.2 Astra et Sol a été décompté à un tarif réduit par erreur. » Après correction, a-t-il précisé, « le même travail consommera une plus grande part du quota de votre abonnement ». Par rapport à la semaine précédente, « vous atteindrez vos limites 40 % plus vite sur GPT-6.2 Astra et 25 % plus vite sur Sol ». Selon lui, les deux modèles devraient tout de même permettre d’en faire davantage que GPT-6 Astra et GPT-6.1 Sol. Les autres modèles ne sont pas concernés et OpenAI ne facturera pas rétroactivement la différence. En guise de dédommagement, chaque abonné Go, Plus, Pro ou Business bénéficiera d’une remise à zéro de son quota, utilisable ultérieurement.

Ces pourcentages ne se transposent pas directement en nombre de tâches. Si le quota se vide 40 % plus vite, il permet d’effectuer environ 29 % de tâches en moins, car 1 divisé par 1,4 donne 0,71. S’il se vide 25 % plus vite, le nombre de tâches diminue de 20 %. Ce calcul découle de la formulation d’OpenAI. L’entreprise n’a pas publié le taux de décompte sous-jacent.

Le lancement remontait à neuf jours. OpenAI a présenté GPT-6.2 Astra et Sol le 17 novembre, date indiquée par GitHub lors de leur ajout à Copilot. Les économies figuraient parmi les arguments de lancement : les deux modèles « donnent de meilleurs résultats sur les tâches exigeantes avec moins de tokens de sortie, ce qui permet d’en faire davantage dans les limites de son quota ». Sol « permet de réaliser plus de tâches avec le même abonnement payant ». Dans l’API, les prix d’Astra ont baissé de 20 %, à 8 dollars par million de tokens d’entrée et 40 dollars par million de tokens de sortie. C’est le tarif catalogue qu’Anthropic avait fixé le 9 novembre pour Claude Fable 5.2. Sol a conservé les tarifs de GPT-6.1 Sol, soit 2 et 10 dollars.

La correction ne modifie pas les prix de l’API. Pour un abonnement ChatGPT payant, l’unité de compte est une fraction du quota, et OpenAI fixe en interne la part que consomme chaque tâche. Consultée le 27 novembre, sa page tarifaire indique le nombre de crédits par million de tokens : 200 en entrée et 1 000 en sortie pour Astra, soit un cinquième de moins que les 250 et 1 250 de GPT-6 Astra. Pour Sol, les chiffres restent à 50 et 250. Pour les abonnés Plus, la page estime aussi qu’une fenêtre de cinq heures permet d’envoyer entre 6 et 50 messages Codex en local avec GPT-6.2 Astra et entre 17 et 180 avec Sol, contre 5 à 45 avec GPT-6 Astra et 15 à 160 avec GPT-6.1 Sol. Elle précise que ces estimations « ne constituent pas des plafonds fixes de messages », que « les abonnements Pro n’ont actuellement pas de limite sur cinq heures » et que des plafonds hebdomadaires peuvent aussi s’appliquer.

Une fourchette de 6 à 50 ne permet ni de confirmer ni de réfuter le chiffre de 40 %. La page ne précise pas si le tableau a été actualisé après la correction. La disparition du quota pendant la nuit décrite par seviu reste un témoignage isolé, sans confirmation. Elle pourrait tenir à la modification du décompte ou à un plafond hebdomadaire.

## Ce qui divise les participants au débat

Le message, repris sous un titre présentant le changement comme une réduction du quota, a recueilli 468 points sur Hacker News. Les lecteurs divergent sur sa signification. Certains prennent l’« erreur de facturation » au pied de la lettre. Une personne raconte avoir passé des heures sur Astra 6.2 sans que le compteur descende sous les 100 %, au point d’avoir cherché un défaut dans le composant d’affichage. D’autres y voient une hausse de prix mise en œuvre sous couvert de correction d’un bug. Certains disent avoir résilié leur abonnement ou envisager Anthropic et Google. Un autre participant relève que le premier courriel d’OpenAI était bref et qu’un second a dû l’expliciter. Tous relatent une expérience personnelle, sans fournir de mesure.

Le fil ravive aussi le souvenir d’un mouvement de balancier. Un abonné de longue date aux services d’OpenAI et d’Anthropic raconte que les quotas d’OpenAI lui avaient paru sans limites tant les remises à zéro se succédaient. Selon lui, Opus 5.5 avait ensuite offert davantage d’usage et OpenAI avait réagi en réduisant ses propres quotas. Un autre participant lui répond que l’avantage passe d’un fournisseur à l’autre depuis l’apparition de ces offres et qu’il changera encore de camp. Tous deux s’en remettent à leurs souvenirs. Aucun n’apporte de relevé des capacités réelles d’un forfait.

## Une autre mesure des mêmes modèles

Le 26 novembre, quelques heures après le message de Sottiaux, le développeur d’Agent Duel, un banc d’essai par confrontation directe, a publié un billet intitulé *OpenAI may be in cost control mode*. Construit sur l’agent de programmation OpenCode, Agent Duel oppose des modèles sur des tâches réelles et les classe selon leur score Elo. Son auteur rapporte que, face à leurs adversaires dans les mêmes duels, Astra 6.2 et Sol 6.2 ont consommé moins de tokens de sortie et de raisonnement par tâche que leurs prédécesseurs. Pour les tokens de sortie, il indique des valeurs p de 0,0055 pour Sol et de 0,022 pour Astra. Pour le raisonnement, elles s’établissent à 0,00013 et 0,0064 respectivement. Il conclut que les modèles « semblent avoir été réglés en fonction du coût », au point de « se distinguer par un raisonnement particulièrement court ».

Le mot « coût » vient de l’auteur. Les données indiquent que les modèles raisonnent moins, sans en donner la raison. Dans son annonce de lancement, OpenAI présente la réduction du nombre de tokens de sortie comme un atout. L’entreprise affirme qu’Astra a gagné 6,2 points sur son banc d’essai interne GDPval v2 en utilisant 22 % de tokens de sortie de moins que GPT-6 Astra. Le même constat peut traduire un gain d’efficacité ou une recherche d’économies. Seule OpenAI sait quelle explication retenir. La baisse du nombre de tokens n’explique pas davantage l’erreur de facturation, qui portait sur leur décompte dans le quota.

Le classement lui-même, établi à 3 h UTC le 27 novembre, ne tranche pas non plus. GPT-6.2 Astra arrive cinquième avec un Elo de 1 007, dans un intervalle de plus ou moins 61 points, pour 2,33 dollars et 2,6 minutes par tâche. Sol arrive douzième avec 937 points, 0,43 dollar et 1,7 minute. Claude Fable 5.2 mène avec 1 069 points et 3,49 dollars, suivi de Claude Opus 5.5 avec 1 060 points et 1,63 dollar. Les intervalles se recoupent largement : pour Astra, un rang entre la deuxième et la onzième place reste plausible.

## Ce qu’un abonné peut vérifier

Le tarif et la facture ont déjà suivi des trajectoires différentes. Le 9 novembre, Anthropic a ramené les prix de Fable 5.2 à 8 et 40 dollars par million de tokens, un cinquième de moins que pour son prédécesseur. Artificial Analysis le classe pourtant toujours dernier sur le critère du coût parmi les modèles évalués : une tâche de son Intelligence Index revient à 26,54 dollars, car la facture dépend du nombre de tokens que le modèle choisit de dépenser. L’épisode OpenAI ajoute un paramètre. Pour un abonné, le fournisseur détermine trois nombres : les tokens que dépense le modèle, le taux auquel ces tokens entament le quota et la taille du quota. C’est sur le deuxième, le taux de décompte, qu’OpenAI dit s’être trompée pendant les neuf premiers jours.

Un observateur extérieur peut mesurer le premier, comme l’a fait Agent Duel. Pour les deux autres, il doit s’en remettre au compteur. À l’abonné qui le découvre à zéro, la page tarifaire apporte cette précision : « Des tâches qui se ressemblent peuvent consommer des parts différentes de votre quota. »

## Références

- Agent Duel (2026). *Agent Duel Leaderboard*, generated 27 November 2026. https://agentduel.com/leaderboard
- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- GitHub (2026). *OpenAI's GPT-6.2 Astra and GPT-6.2 Sol now available*. GitHub Changelog, 17 November. https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available
- Hacker News (2026). *OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster*. https://news.ycombinator.com/item?id=50651117
- micjm (2026). *OpenAI may be in cost control mode*. https://micjm.com/blog/openai-is-in-cost-control-mode/
- OpenAI (2026). *Introducing GPT-6.2 Astra and Sol*. https://openai.com/index/introducing-gpt-6-2-astra-sol
- OpenAI (2026). *Pricing*. ChatGPT Learn. https://learn.chatgpt.com/docs/pricing
- Sottiaux, T. (2026). Post on X about the GPT-6.2 billing mistake, 26 November. https://x.com/thsottiaux/status/2125784147889393806

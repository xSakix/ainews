+++
title = "Qui paie quand les centres de données rejoignent le réseau texan"
slug = "qui-paie-centres-donnees-reseau-texan"
description = "Une prépublication modélise ce que 371 centres de données annoncés au Texas ajouteraient au prix de l'électricité des ménages : l'essentiel passe par le marché de gros, non par les nouvelles lignes. La même étude montre que la réponse varie selon l'emplacement des centrales et le partage des coûts de transport, un choix que la Virginie vient de faire."
tags = ["business", "policy", "research"]
date = 2026-11-15T03:19:35+01:00
draft = false
+++

James O'Donnell, de MIT Technology Review, a passé la semaine des élections américaines de mi-mandat à Ashburn, en Virginie, au centre de ce qu'on appelle Data Center Alley. Des bâtiments en béton portant des noms comme Skybox et CloudHQ bordent chaque grand axe. Dans une installation exploitée par Equinix, il a vu des groupes électrogènes diesel conservés en secours, tandis que le bâtiment tirait son électricité du fournisseur local, Dominion Energy. Selon son reportage, un centre de données moyen dans cette partie de la Virginie a une capacité de 54 mégawatts, supérieure à la consommation de Denver International Airport.

Il y a rencontré Elena Schlossberg, figure de la mobilisation contre les centres de données. Lorsque l'industrie décrit le conflit comme une guerre culturelle, lui a-t-elle dit, elle a « toujours envie de se taper la tête contre les murs ». Son point de vue : « Il a toujours été question d'électricité. »

Deux jours après les élections, Chris Lehane, responsable des affaires mondiales d'OpenAI, avait écrit que les centres de données « sont devenus le symbole du malaise du public face au coût de la vie, au pouvoir des entreprises et à la perte de contrôle sur son avenir ». Le récit d'O'Donnell met ces deux lectures côte à côte. Une nouvelle prépublication d'Oregon State University et du National Laboratory of the Rockies chiffre le versant électrique du débat.

## Ce que l'étude a modélisé

Lingdong Zhou, Wenjia Xia, Jiyu Wang, Fei Ding et Xiangqi Zhu partent de 371 projets de centres de données annoncés au Texas, qui demanderaient ensemble 38,9 gigawatts en 2030, et se demandent ce que leur alimentation ferait au coût du kilowattheure pour un ménage. L'article est une prépublication et n'a pas été évalué par les pairs. Il s'agit d'un modèle, et les auteurs disent clairement que ses résultats sont des « impacts modélisés selon les hypothèses spécifiées, et non des prévisions des factures réelles d'électricité des ménages ».

Les projets se concentrent en 51 points du modèle du réseau texan. La demande existante varie entre 35 et 85 gigawatts au cours d'un été, mais les centres de données ajoutent 33 à 38 gigawatts à chaque heure. Le modèle choisit les centrales, batteries et lignes de transport à construire au moindre coût, calcule les prix de gros en chaque point du réseau, dimensionne les renforcements nécessaires à sa sûreté et suit les coûts à travers les tarifs réglementés et un fournisseur de détail jusqu'au client résidentiel. Il couvre mai à octobre, les mois qui déterminent la pointe de demande du Texas, et teste cinq années météorologiques historiques.

## D'où vient le surcoût

Dans le cas représentatif, l'année météorologique 2023, un ménage paie 1,64 cent de plus par kilowattheure pendant la saison de pointe. Sur ce montant, 1,124 cent, soit 68 %, passe par des prix de gros plus élevés. Les 0,520 cent restants, soit 32 %, passent par les frais réglementés de transport. Les auteurs y voient un élément contredisant une représentation courante. Même lorsque les centres de données contribuent au financement de nouvelles lignes, leur demande relève le prix de gros payé par chaque client, et cet effet dépasse le coût des lignes.

Le résultat dépend du développement du réseau. Si de nouvelles centrales à gaz ne peuvent être construites que sur des sites existants, la production et le stockage seuls peuvent fournir plus de 99,95 % de la demande, mais l'électricité n'atteint pas toujours les nœuds situés derrière des corridors contraints. Les prix à un ou plusieurs de ces nœuds dépassent le plafond de marché de 5 000 dollars par mégawattheure pendant 136 à 407 intervalles de trois heures par saison. Développer le transport en même temps que la production réduit l'investissement annuel moyen de 16,7 milliards à 4,54 milliards de dollars et ne laisse qu'un à trois de ces intervalles. Autoriser de nouvelles centrales à gaz près des centres de données ramène la hausse pour les ménages de 1,64 à 0,92 cent.

L'emplacement compte en lui-même. Ajouter 5 gigawatts sans nouvelles infrastructures laisse entre 25 et 140 gigawattheures de demande non satisfaite par saison à Houston, Austin, Tolar et dans le sud de Dallas–Fort Worth, mais 5,6 térawattheures à Abilene et 18,7 à Childress. Les auteurs soulignent que, pour la même charge, l'énergie non desservie peut varier de près de trois ordres de grandeur selon le point de raccordement.

## Le choix du partage des coûts

Le troisième levier ne relève pas du tout de l'ingénierie. Le Texas répartit la facture du transport entre les clients proportionnellement à leur demande lors des pointes du système. Dans le modèle, les centres de données paient environ 0,82 milliard de dollars sur les 2,719 milliards de dollars de recettes annuelles requises pour le transport. S'ils étaient retirés de cette assiette, les frais résidentiels de transport passeraient de 0,520 à 0,747 cent par kilowattheure, et le total pour les ménages de 1,64 à 1,87. Rien ne changerait dans le réseau ; seule changerait la personne facturée. Les auteurs rappellent qu'une loi texane de 2025, Senate Bill 6, exige un réexamen de cette méthode de répartition.

Leur propre liste de limites est longue. Le scénario suppose que les projets annoncés se réalisent. Il ignore l'hiver. Les prix de gros reposent sur les hypothèses du modèle de marché relatives à l'anticipation et à la tarification de la rareté ; le réseau de transport est synthétique et l'étape de renforcement laisse certaines violations non résolues. La flexibilité de la demande des centres de données, qui pourrait supprimer les quelques heures de rareté restantes, n'est pas modélisée. Une variante aux prix plus élevés représentant le mécanisme texan de tarification des réserves situe la composante de gros à 0,81 cent en 2023 et entre 2,34 et 2,89 cents de 2019 à 2022. Les contrats de détail à prix fixe retardent aussi l'effet, car les fournisseurs absorbent la hausse des coûts jusqu'à ce qu'ils puissent revoir leurs prix. Dans une simulation, la probabilité qu'un fournisseur de détail épuise sa trésorerie passe de 0,04 à 0,26 % avec une expansion coordonnée, et à 1,24 % lorsque seules la production et le stockage sont ajoutés.

## La Virginie a choisi, d'autres choisissent encore

La Virginie a déjà fait le choix de répartition que l'article isole. Selon O'Donnell, les protestations ont conduit l'État à adopter des règles imposant aux centres de données de payer intégralement les nouvelles lignes de transport, afin que leur coût ne soit pas réparti entre tous les autres. Les promoteurs lui ont indiqué attendre de nouvelles règles qui les déconnecteraient du réseau aux heures de pointe. C'est le type de flexibilité que les auteurs texans n'ont pas modélisé, mais qu'ils désignent comme une piste prometteuse.

Ailleurs, le conflit prend une autre forme. Semafor rapportait le 4 novembre que les électeurs de plus de 30 localités dans neuf États avaient soutenu par référendum des moratoires, interdictions et autres restrictions sur les centres de données. Les banques et gestionnaires d'actifs finançant leur construction avaient commencé à traiter l'opposition locale comme un risque de crédit. O'Donnell ajoute que la plupart des campus d'IA actuellement prévus ne sont pas du tout conçus pour se raccorder au réseau. Avec une puissance souhaitée d'au moins 300 mégawatts et idéalement d'environ 6 000, les entreprises s'installent en zone rurale et produisent leur électricité sur place avec des turbines à gaz. Il cite un article selon lequel Anthropic a accepté de payer 3,4 milliards de dollars pour des turbines à gaz. Son argument est que des centrales de cette taille affectent les voisins, et que les communautés ont traditionnellement leur mot à dire sur leur implantation.

L'article texan ne peut pas déterminer laquelle des deux lectures de la contestation est juste. Il dit quelque chose de plus limité. La part du coût d'une nouvelle charge supportée par un ménage n'est pas fixée par cette charge. Elle varie de près d'un cent par kilowattheure selon l'implantation de la production et d'un quart de cent selon une règle de facturation ; ces deux décisions restent entre les mains des régulateurs et des législateurs.

À Ashburn, la règle est déjà écrite. Au Texas, le réexamen ordonné par Senate Bill 6 n'a pas encore rendu ses conclusions.

## Références

- Capelouto, J. D. (2026). *US voters roundly reject data centers in ballot measures*. Semafor. https://www.semafor.com/article/11/04/2026/us-voters-roundly-reject-data-centers-in-ballot-measures
- O'Donnell, J. (2026). *The backlash about data centers might really just be about electricity*. MIT Technology Review. https://www.technologyreview.com/2026/11/09/1148194/the-backlash-about-data-centers-might-really-just-be-about-electricity/
- Zhou, L., Xia, W., Wang, J., Ding, F., & Zhu, X. (2026). *Data-center growth impacts household electricity costs more through wholesale prices than through grid reinforcement*. arXiv preprint. https://arxiv.org/abs/2611.16095

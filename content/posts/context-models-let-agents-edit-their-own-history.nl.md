+++
title = "Contextmodellen laten agents hun eigen geschiedenis bewerken"
slug = "contextmodellen-laten-agents-hun-eigen-geschiedenis-bewerken"
description = "Context Language Models vervangen een transcript waaraan alleen tekst wordt toegevoegd door een bestand dat het model kan herschrijven, wissen en herschikken. De auteurs melden hogere nauwkeurigheid bij lange taken met minder herhaald rekenwerk na training van het bewerkingsbeleid."
tags = ["research", "agents", "tools"]
date = 2026-10-06T04:05:31+02:00
draft = false
+++

Context Language Models laten een agent de geschiedenis bewerken die hij vervolgens zal lezen. Contextbeheer verandert daarmee van een vaste samenvattingsstap in een aangeleerde handeling.

Rulin Shao en 12 mede-auteurs stellen de actuele context voor als een bestand. Het model kan dat bestand tijdens het werk herschrijven, delen ervan wissen of de inhoud herschikken, en vervolgens verdergaan vanuit de bewerkte versie. Het hoeft zo geen steeds langer transcript mee te nemen of een samenvatting te aanvaarden die door de omringende software is gekozen.

## Waarom dit ertoe doet {#why-it-matters}

Voor een ontwikkelaar die een langdurige onderzoeks- of programmeeragent draait, is context zowel geheugen als rekenwerk. Oude tokens herhaaldelijk aanleveren kost tijd, terwijl vergaande inkorting bewijs kan verwijderen dat later nodig is. Een model dat bepaalt wat het bewaart, zou die afweging per taak kunnen maken.

Het artikel noemt de aanpak een Context Language Model, of CLM. Het scheidt het bewerkbare contextbestand van de huidige interactie, zodat een agent een beknopt werkverslag kan bijhouden terwijl de oorspronkelijke omgeving waarnemingen blijft produceren.

De basismethode vereist geen speciale modelarchitectuur. De auteurs testen instructies die bestaande modellen vertellen hoe ze het bestand moeten beheren, en verbeteren vervolgens het beleid met reinforcement learning en een lus voor vaardigheidsoptimalisatie. Een openbare repository bevat de implementatie en voorbeelden; de auteurs hebben ook een plugin voor de Pi-agentomgeving vrijgegeven.

Op een apart gehouden taak voor contextbeheer melden de auteurs dat geoptimaliseerde instructies in natuurlijke taal de nauwkeurigheid met maximaal 35,9 procentpunt verbeterden en tegelijk het rekenwerk verminderden. Dat maximum is de sterkste gemelde verandering, maar komt uit de evaluatie van de auteurs en verschilt per opzet.

## Bewerken verandert zowel de cache als de tekst

Contextbewerking veroorzaakt een inferentieprobleem. Transformerservers hergebruiken normaal een key-value-cache voor een ongewijzigd begin van de invoer. Tekst middenin herschrijven maakt latere gecachte toestanden ongeldig, omdat die uit de vorige versie zijn berekend.

De auteurs stellen gedeeltelijk cachehergebruik voor om te voorkomen dat alles opnieuw moet worden berekend. Die optimalisatie heeft gevolgen: toestanden van na een bewerking hergebruiken kan de cache verouderd maken, terwijl opnieuw rekenen vanaf het bewerkingspunt minder werk bespaart. Het artikel meldt dat de benadering de nauwkeurigheid behield in de geteste omstandigheden, maar lezers uit de gemeenschap hebben dit al aangewezen als een belangrijk punt voor reproductie.

Het bewerkbare bestand verandert ook de beveiligingsgrens. Tooluitvoer, gebruikersinstructies en door het model geschreven notities kunnen samen blijven bestaan totdat het model ze verwijdert. Een kwaadaardige instructie die het bestand bereikt, kan daardoor langer overleven dan in een tijdelijke toolreactie. Het artikel onderzoekt contextbeheer en biedt geen geauthenticeerde herkomstregistratie of volledige verdediging tegen promptinjectie.

Het onderzoek evalueert modellen uit de Qwen- en Claude-families op contextbeheer en langdurige agenttaken. Gemelde verbeteringen na reinforcement learning laten zien dat bewerken kan worden aangeleerd en niet uitsluitend via prompts hoeft te worden gevraagd. Ze stellen echter niet vast dat elke agent zijn eigen verslag zou moeten beheren. Gereguleerde workflows of workflows voor forensisch onderzoek kunnen naast de bewerkbare werkcontext een onveranderlijk transcript nodig hebben.

De preprint werd op 29 september 2026 ingediend. De coderepository is openbaar, dus het volgende bruikbare bewijs kan komen van reproducties die volledige herberekening, gedeeltelijk cachehergebruik en gewone contextinkorting op dezelfde taken vergelijken.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| CLM's bieden context aan als een bestand dat het model kan herschrijven, wissen en herschikken | VOLGENS HET BEDRIJF | [CLM-preprint](https://arxiv.org/abs/2609.37725) | [openbare implementatie](https://github.com/facebookresearch/context-language-models) |
| De methode werkt met bestaande modelarchitecturen | VOLGENS HET BEDRIJF | [CLM-preprint](https://arxiv.org/abs/2609.37725) | implementatie in repository beschikbaar |
| Geoptimaliseerde instructies verbeterden de nauwkeurigheid op apart gehouden taken met maximaal 35,9 procentpunt en verminderden het rekenwerk | VOLGENS HET BEDRIJF | [CLM-preprint](https://arxiv.org/abs/2609.37725) | geen; evaluatie door de auteurs |
| Gedeeltelijk cachehergebruik behield de nauwkeurigheid in de geteste omstandigheden | VOLGENS HET BEDRIJF | [CLM-preprint](https://arxiv.org/abs/2609.37725) | geen onafhankelijke reproductie gevonden |
| Bewerkbare context kan geïnjecteerde instructies langer bewaren | ANALYSE | [CLM-preprint](https://arxiv.org/abs/2609.37725) | dreiging volgt uit blijvende, door het model geschreven context |
| De code en een Pi-plugin zijn openbaar | GEVERIFIEERD | [CLM-repository](https://github.com/facebookresearch/context-language-models) | repository beschikbaar |
| De preprint werd op 29 september 2026 ingediend | GEVERIFIEERD | [arXiv-vermelding](https://arxiv.org/abs/2609.37725) | arXiv-metadata |

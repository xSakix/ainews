+++
title = "Een beoordelaar van nieuwheid veranderde met de prompt van oordeel"
slug = "beoordelaar-van-nieuwheid-veranderde-met-prompt-van-oordeel"
description = "Ai2 testte taalmodellen die beoordelen of onderzoeksideeën nieuw zijn. De nauwkeurigheid van één model daalde na een kleine promptwijziging van 93,5 naar 40,9 procent, wat laat zien hoe kwetsbaar geautomatiseerde nieuwheidsscores kunnen zijn."
tags = ["research", "models"]
date = 2026-10-28T04:11:25+01:00
draft = false
+++

Een onderzoekster in machinelearning zit aan het einde van een lange beoordelingssessie. Twee voorgestelde ideeën staan naast elkaar op haar scherm. Een model heeft het eerste als vernieuwend gemarkeerd. Ze verkort de instructie boven hetzelfde paar, voert het model opnieuw uit en ziet de markering naar het tweede idee verplaatsen. De onderzoekster is verzonnen. De omkering niet: Ai2 mat haar in een benchmark die is gebouwd om geautomatiseerde beoordelaars van wetenschappelijke nieuwheid te testen.

## Het oordeel veranderde voordat het bewijs veranderde

Het onderzoek van Ai2, gepubliceerd met code en gegevens, testte zes taalmodellen als beoordelaars van nieuwheid. De onderzoekers varieerden de prompt, het redeneerbudget, de opgehaalde literatuur, de vorm van de ideeën en de manier waarop ze meerdere aanroepen combineerden. De onderliggende ideeën bleven gelijk.

Het scherpste resultaat kwam van GPT-5.4. In één prompt kreeg het model te horen dat beoordelaars precies één idee in elk paar vernieuwend hadden gevonden en werd het gevraagd dat idee aan te wijzen. In een eenvoudigere prompt werd alleen gevraagd welk idee vernieuwend was. De nauwkeurigheid op dezelfde paren van menselijke en gegenereerde ideeën daalde van 93,5 naar 40,9 procent. Het model veranderde meer dan de helft van zijn oordelen.

De formulering maakte minder verschil bij paren met alleen ideeën van mensen. Daar veranderde dezelfde promptwijziging de nauwkeurigheid met ongeveer zeven procentpunt. Een beoordelaar kan dus stabiel lijken bij conventioneel academisch materiaal en zich anders gedragen bij de gegenereerde ideeën die hij steeds vaker moet beoordelen. Zelfs de verzameling met alleen menselijke ideeën was niet immuun: Claude Opus 4.6 verschoof bij de promptwijziging met 21 punten.

Er was geen prompt die elke beoordelaar verbeterde. Het verwijderen van een waarschuwing om stapsgewijze verbeteringen niet als vernieuwend te beschouwen hielp sommige modellen en schaadde andere. Toen het team ideeën van twee AI-generatoren vergeleek, veranderde een promptwijziging gemiddeld over de zes beoordelaars ongeveer een kwart tot een derde van de oordelen. Die instabiliteit kan worden gemeten zonder eerst te beslissen welke generator beter is.

## Beoordelingen werden de benchmark

Nieuwheid is moeilijk te benchmarken, omdat het geen eigenschap is die uit een antwoordenlijst kan worden afgelezen. Een onderzoeksidee is alleen nieuw in verhouding tot eerder werk, en experts kunnen van mening verschillen over hoeveel verschil telt. Ai2 gebruikte daarom de acceptatie van een artikel niet als benadering. Het doorzocht peerreviews voor ICLR 2026 op passages waarin beoordelaars de originaliteit van een bijdrage expliciet prezen of betwistten.

Dit proces leverde 154 menselijke ideeën met hoge nieuwheidswaarde op, uit geaccepteerde artikelen in de hoogst gewaardeerde 10 procent van hun onderzoeksgebieden. Elk idee had positieve aanwijzingen voor nieuwheid van beoordelaars en geen tegenspraak daarover. De verzameling met lagere nieuwheidswaarde bevatte 145 ideeën uit afgewezen artikelen in de onderste 10 procent, waarvan de beoordelingen zorgen over originaliteit uitten zonder positieve aanwijzingen voor nieuwheid. Bij een controle van 50 geëxtraheerde beoordelingspassages was een annotator het in 47 gevallen eens met de toegewezen positieve of negatieve strekking. Geen van de drie meningsverschillen zou hebben veranderd of een beoordelaar als voorstander of betwister van de nieuwheid werd meegeteld.

Deze verzameling met alleen menselijke ideeën test of een beoordelaar bijdragen met sterker en zwakker bewijs uit peerreviews kan onderscheiden. Een tweede verzameling richt zich op een centrale toepassing van geautomatiseerde wetenschap: het beoordelen van ideeën die door een model zijn geschreven. Het team koppelde de 154 gevalideerde menselijke ideeën aan 154 ideeën van een eenvoudige generator. Die kreeg een onderzoeksgebied en de instructie iets nieuws voor te stellen, zonder literatuurzoektocht, tools, herhaling of feedback.

Het label voor die gegenereerde ideeën is bewust zwakker. De onderzoekers namen aan dat de uitvoer van de eenvoudige generator minder vernieuwend was dan een bijdrage uit een hoog gewaardeerd artikel waarvan beoordelaars de originaliteit hadden onderschreven. Geen expert beoordeelde elk paar. Ter controle bekeek één expert 30 paren, met extra gewicht voor voorbeelden die de sterkste beoordelaar had gemist, en verkoos telkens het menselijke idee. Het team herschreef ook de gegenereerde en menselijke ideeën in dezelfde structuur om de kans te verkleinen dat de stijl hun herkomst verraadde.

## Meer techniek leverde geen steviger antwoord op

Het onderzoek testte ook een bekende reactie op onzekere modeloordelen: geef de beoordelaar meer zoekmogelijkheden, meer redeneerruimte of een systeem dat voor de taak is ontworpen. Geen van deze ingrepen bood een algemene oplossing.

Een agentische GPT-5.6 Sol-beoordelaar kreeg een extra hoog redeneerbudget en live iteratief zoeken, beperkt tot arXiv. Hij bereikte een macro-F1 van 0,78 op de taak met menselijke en gegenereerde ideeën. Een standaardopzet met Claude Opus 4.6 en vijf opgehaalde abstracts bereikte 0,89 en kostte per beslissing ongeveer een tiende bij de API-prijzen die het onderzoek gebruikte. De vergelijking bewijst niet dat zoeken nutteloos is. Ze toont dat extra techniek geen beter oordeel over nieuwheid garandeert.

Ook systemen die speciaal voor de taak zijn gebouwd, bleven achter bij een eenvoudiger basisopzet. Een Claude Opus 4.6-prompt met een laag redeneerniveau, waarbij de meerderheid van drie aanroepen de beslissing bepaalde, bereikte een macro-F1 van 0,854 voor totale evaluatiekosten van 2,59 dollar. Idea Novelty Checker, dat literatuur ophaalt en opnieuw rangschikt, scoorde 0,642 voor 30,66 dollar. De nieuwheidsbeoordelaar in Sakana AI’s AI Scientist, die iteratief Semantic Scholar doorzoekt, scoorde 0,772 voor 82,05 dollar. Alle drie de cijfers komen uit Ai2’s implementatie en prijsaannames. Ze vergelijken dus deze geteste configuraties, niet elk mogelijk gebruik van de systemen.

Eerdere systemen verklaren waarom onderzoekers naar zulke ontwerpen grijpen. Scideator helpt wetenschappers aspecten van artikelen opnieuw te combineren tot nieuwe voorstellen en gebruikt opgehaalde literatuur om overlap te beoordelen. Idea Novelty Checker vernauwt een brede literatuurzoektocht via embeddingfilters en herordening op basis van aspecten. AI Scientist behandelt het controleren van nieuwheid als één fase in een grotere geautomatiseerde onderzoekscyclus. Elk systeem verankert zijn oordeel in eerder werk in plaats van alleen op het geheugen van een model te vertrouwen.

Ai2’s resultaat verschuift de bewijslast. Een hoge score van één beoordelaar, prompt en redeneerinstelling zegt weinig over de vraag of het oordeel bij een andere redelijke opzet standhoudt. De auteurs raden aan beoordelaars te testen op de soorten gegenereerde ideeën die ze daadwerkelijk zullen zien, gevoeligheid voor verschillende prompts en modellen te meten en benchmarks bij te werken naarmate de literatuur verandert.

## Een score heeft zelf beoordeling nodig

Terug naar de denkbeeldige onderzoekster. Ze kiest niet het oordeel dat haar voorkeur heeft. Ze bewaart beide uitkomsten, legt beide prompts vast en leest zelf de verwante artikelen. Het model kan nog steeds helpen een groeiende stapel voorstellen te ordenen, maar zijn cijfer is nu één bewijsstuk in plaats van de laatste beslissende controle.

De markering verschoof tussen twee ideeën, maar de belangrijkere verandering was het vertrouwen dat eraan werd gehecht. Wanneer enkele woorden het antwoord kunnen verschuiven, heeft het oordeel evenzeer beoordeling nodig als het onderzoeksidee.

## Referenties

- Ai2. (2026). *Can we trust LLMs to judge whether a research idea is novel?* https://allenai.org/blog/novelty-bench
- Lu, C., Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*. https://arxiv.org/abs/2408.06292
- Radensky, M., Shahid, S., Fok, R., Siangliulue, P., Hope, T., & Weld, D. S. (2024). *Scideator: Human-LLM Scientific Idea Generation Grounded in Research-Paper Facet Recombination*. https://arxiv.org/abs/2409.14634
- Shahid, S., Radensky, M., Fok, R., Siangliulue, P., Weld, D. S., & Hope, T. (2025). *Literature-Grounded Novelty Assessment of Scientific Ideas*. https://arxiv.org/abs/2506.22026
- Sternlicht, N., Shahid, S., Jansen, P., Weld, D. S., Siangliulue, P., & Hope, T. (2026). *Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation*. https://arxiv.org/abs/2610.02022

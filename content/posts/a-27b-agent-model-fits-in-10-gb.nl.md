+++
title = "Een agentmodel van 27 miljard parameters past in 10 GB"
slug = "een-agentmodel-van-27-miljard-parameters-past-in-10-gb"
description = "Nari Labs comprimeerde Qwen3.8-27B van 53,8 GB naar 10,12 GB en evenaarde de oorspronkelijke BF16-versie op verscheidene lange agentbenchmarks. Het resultaat steunt op kalibratiedata die door agents zijn gegenereerd en op een gespecialiseerde inferentiefork, wat beperkt waar de kleinere bestanden kunnen draaien."
tags = ["models", "agents", "research", "hardware"]
date = 2026-11-24T04:21:00+01:00
draft = false
+++

De download voltooide op een werkstation met 16 gigabyte grafisch geheugen. Een model van 27 miljard parameters dat normaal 53,8 gigabyte nodig had, zat in één bestand van 10,12 gigabyte. De ingenieur startte een programmeeragent en zag hoe die tools aanriep, de uitkomsten las en doorging in plaats van halverwege de taak vast te lopen.

*De scènes aan het begin en het einde van dit artikel zijn illustraties; de personen erin zijn verzonnen.*

Nari Labs bracht op 20 november drie gecomprimeerde versies van Alibaba's Qwen3.8-27B uit. Zijn driebits- en 2,5-bitsbestanden evenaarden het oorspronkelijke BF16-model op de tests van het lab voor lange programmeer- en terminaltaken. Het tweebitsbestand deed dat niet. De release brengt een praktische en een methodologische bewering mee: een model kan bijna vier vijfde van de opslag voor zijn gewichten verliezen zonder het gedrag kwijt te raken dat agents nodig hebben, mits het compressieproces leert van agentwerk in plaats van gewone tekst.

## De verkeerde tekst voor de taak

Kwantisatie vervangt de nauwkeurige getallen in de gewichten van een model door kleinere representaties. Minder bits verlagen het geheugengebruik en de bandbreedte, waardoor een model dat anders een server vereist op een werkstation kan passen. De prijs daarvoor is benadering. Elk gecomprimeerd gewicht wijkt af van het origineel, en die fouten kunnen zich opstapelen terwijl het model een lang antwoord genereert of door vele stappen heen werkt.

De meeste kalibratiesets bestaan uit korte passages van het web. Een kwantiseerder gebruikt die passages om te leren welke fouten ertoe doen en hoe een beperkte reeks numerieke waarden moet worden verdeeld. Doyeob Kim, de enige auteur van het NariQ-rapport, stelt dat die data niet representatief zijn voor het werk van een programmeeragent. Een agent werkt soms over meer dan 100.000 tokens, wisselt redeneren af met toolaanroepen en reageert over vele beurten heen op terminaluitvoer.

Die kloof komt naar voren in bestaande resultaten. Volgens Kims artikel kunnen eerdere kwantisaties van Qwen3.8-27B op drie bits of minder BF16 bijhouden op de korte wiskundeopgaven in AIME, terwijl ze hoogstens 72 procent zoveel DeepSWE-taken oplossen. Een model dat feiten oproept en losse berekeningen uitvoert, kan tijdens een lange wisselwerking met een softwarerepository alsnog ontsporen.

NariQ verandert het kalibratiemateriaal. Het legt tokens vast die het volledige BF16-model tijdens agentsessies genereerde, en gebruikt die sporen vervolgens om de keuze van gecomprimeerde gewichten te sturen. Het model krijgt het soort reeksen te zien dat het later moet volhouden: plannen, toolverzoeken, waarnemingen en bijstellingen.

## Trellissen en sporen

De numerieke methode bouwt voort op QTIP, een aanpak uit 2024 van James Tseng en collega's. QTIP gebruikt trellisgecodeerde kwantisatie en een incoherentietransformatie om groepen gewichten toe te wijzen aan compacte codewoorden. De trellis zoekt tussen mogelijke reeksen in plaats van elk gewicht afzonderlijk af te ronden.

NariQ koppelt die techniek aan kalibratie uit de beoogde activiteit. Dat onderscheid doet ertoe omdat een kwantiseerder de gemiddelde waarschijnlijkheid van het volgende token in stand kan houden, terwijl hij een kleine reeks beslissingen beschadigt die bepalen of een agent zich herstelt van een mislukt commando. Lange taken leggen die beslissingen keer op keer bloot.

De gepubliceerde bestanden omvatten drie, 2,5 en twee bits per gewicht. Ze behouden de beeldmodule en de key-valuecache van Qwen3.8-27B in BF16, zodat het genoemde aantal bits de gewichten van het taalmodel beschrijft en niet elke byte die inferentie verbruikt. Het basismodel is een dicht beeld-taalmodel met 64 lagen en een oorspronkelijke contextlengte van 262.144 tokens. Het ondersteunt een instelbaar redeneerniveau en bewaart redeneerinhoud standaard over beurten heen.

Nari Labs evalueerde de gecomprimeerde bestanden naast het BF16-checkpoint van 53,8 gigabyte. Op DeepSWE v1.1, dat 113 taken bevat die drie keer worden uitgevoerd, scoorde BF16 39,8 pass@1. Het driebitsbestand haalde 41,0 en het 2,5-bitsbestand 41,9. Terminal-Bench 2.1 leverde 62,6 op voor BF16, 63,8 voor drie bits en 60,2 voor 2,5 bits.

Dat patroon zette zich voort op de wiskundesets AIME 2025 en 2026. BF16 scoorde 97,7, de driebitsversie 98,3 en de 2,5-bitsversie 96,5. Op de beeldbenchmark RealWorldQA eindigden BF16 en de driebitsversie gelijk op 82,4. Zulke kleine verschillen bewijzen niet dat compressie het model verbetert; herhaalde steekproeven kunnen een agentbenchmark doen schommelen. Ze ondersteunen wel de smallere conclusie dat de twee grotere NariQ-bestanden in deze tests niet meetbaar achterbleven.

## De tweebitsgrens

Het kleinste bestand laat zien waar de bewering ophoudt. Bij twee bits per gewicht zakte DeepSWE naar 28,6, Terminal-Bench naar 52,4 en AIME naar 86,0. De compressie overschreed een grens waarop kalibratie het gedrag van het bronmodel niet langer kon herstellen.

De benchmarkset is bovendien van de ontwikkelaar zelf. Nari Labs koos het model, de kalibratiesporen, de implementatie en de evaluatie-instellingen. Het rapport telt één auteur en heeft geen peerreview ondergaan. Onafhankelijke runs op andere agents, repositories en hardware zouden moeten toetsen of de gelijke prestaties buiten de gepubliceerde tabel standhouden.

Er ligt nog een tweede grens tussen een klein bestand en een toegankelijk model. NariQ vereist de fork van llama.cpp van het bedrijf zelf, omdat het gewichtsformaat en de kernels niet in het standaardproject zitten. Reguliere llama.cpp, Ollama en LM Studio kunnen de bestanden niet laden. De fork is afgestemd op Nvidia's SM120-architectuur. Volgens Nari Labs draait hij trager op Ampere-, Ada- en Hopper-kaarten, ondersteunt hij geen AMD- of Intel-GPU's en blijft hij traag op Apple Metal.

Dat voorbehoud verandert de betekenis van “lokaal”. Tien gigabyte brengt de gewichten binnen het geheugenbudget van veel grafische consumentenkaarten, maar het softwarepad bedient veel van die kaarten nog niet goed. De ongecomprimeerde modelkaart van Qwen noemt daarentegen gevestigde serveerframeworks zoals Transformers, vLLM en SGLang. De NariQ-bestanden ruilen die brede compatibiliteit in voor hun omvang.

## Wat het bestand meet

Het werk wijst op een andere manier om laagbitsmodellen te beoordelen. Perplexiteit en korte toetsen zijn handig omdat ze goedkoop en herhaalbaar zijn. Ze beproeven echter niet de lussen die een agent bruikbaar maken: een doel vasthouden, tools kiezen, foutmeldingen lezen en opnieuw proberen. Kalibratiedata kunnen dezelfde blinde vlek meedragen als een evaluatie.

NariQ maakt een model van 27 miljard parameters niet universeel goedkoop. De volledige context verbruikt nog steeds geheugen voor de key-valuecache, de beeldencoder blijft op hoge precisie en de inferentiesnelheid hangt af van kernels voor een specifiek apparaat. Wel toont het aan dat gewichtopslag en agentvaardigheid bij drie of 2,5 bits op de geteste taken niet samen hoeven terug te lopen.

Terug op het werkstation bereikte de agent het einde van zijn terminaltaak. Het bestand van 10,12 gigabyte had vanaf het begin gepast. Of de volgende machine het kan draaien, hangt minder af van het bestand dan van de naam die op de grafische chip staat gedrukt.

## Referenties

- Kim, D. (2026). *NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks*. https://arxiv.org/abs/2611.26157
- Nari Labs (2026). *Qwen3.8-27B-NariQ-GGUF model card*. https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
- Qwen Team (2026). *Qwen3.8-27B model card*. https://huggingface.co/Qwen/Qwen3.8-27B
- Tseng, J., et al. (2024). *QTIP: Quantization with Trellises and Incoherence Processing*. https://arxiv.org/abs/2406.11235

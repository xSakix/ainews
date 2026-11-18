+++
title = "Lange gespreksgeschiedenis maakte modellen consequent fout"
slug = "lange-gespreksgeschiedenis-maakte-modellen-consequent-fout"
description = "Een onderzoek met 100 beurten vond dat de volledige chatgeschiedenis de nauwkeurigheid bij het bijhouden van een toestand van ongeveer 60 naar 10 procent drukte. Gecontroleerde samenvattingen behielden de juiste antwoorden, terwijl gangbare controles het falende systeem vaak stabiel lieten lijken."
tags = ["research", "models"]
date = 2026-11-18T04:00:29+01:00
draft = false
+++

Marta controleert de voorraadassistent vóór de ochtenddienst. Het dashboard is groen. De antwoorden stemmen met elkaar overeen, de toon is rustig en de magazijntotalen zijn bij de laatste vijf vragen nauwelijks veranderd. Dan vergelijkt ze één getal met de administratie. De assistent heeft in elk antwoord dezelfde fout meegenomen.

*De scènes aan het begin en het einde van dit artikel zijn illustraties; de personen erin zijn verzonnen.*

Een preprint van Ali Şenol van Tarsus University onderzoekt die stille mislukking. In gesprekken van 100 beurten over veranderende budgetten, voorraden, laboratoriumcontainers en projectmijlpalen daalde de nauwkeurigheid van modellen binnen twintig beurten van ongeveer 60 naar ongeveer 10 procent wanneer het volledige transcript in de context bleef. Een toestandssamenvatting die een solver had gecontroleerd, hield de nauwkeurigheid meer dan 50 procentpunt hoger. De gebruikelijke tekenen van ordelijk redeneren gaven geen betrouwbare waarschuwing.

## Het transcript wordt onderdeel van het probleem

Lange gesprekken vragen een model twee dingen tegelijk te doen. Het moet het huidige probleem oplossen en bepalen wat het moet onthouden van alles wat het zelf en de gebruiker eerder hebben gezegd. Die tweede taak wordt moeilijker wanneer de toestand verandert, een eerder feit wordt gecorrigeerd of het model al een fout heeft gemaakt.

Eerder werk had een deel van dit probleem al afzonderlijk onderzocht. In *LLMs Get Lost in Multi-Turn Conversation* verdeelden Philippe Laban en zijn medeauteurs volledige taken in delen die verspreid over meerdere beurten binnenkwamen. Modellen legden zich vaak te vroeg vast op een antwoord. Hun prestaties daalden, hoewel het onderliggende probleem niet was veranderd. Dat onderzoek gebruikte taken afgeleid van GSM8K, de dataset met 8.500 rekenopgaven voor de basisschool die Karl Cobbe en collega's in 2021 introduceerden.

Şenol stelde eerst een beperktere causale vraag: maakt het bewaren van de eigen antwoorden van het model het uiteindelijke antwoord slechter? Hij selecteerde 48 opgesplitste rekentaken van vier tot negen beurten. GPT-4o-mini, Llama 4 Scout en Mistral 7B kregen elk twee versies. De ene bewaarde de dialoog. De andere bouwde een nieuwe prompt op uit de informatie van de gebruiker en liet eerdere antwoorden van de assistent weg.

Alle 11.382 modelaanroepen werden voltooid. GPT-4o-mini loste 33 van de 48 taken op met zijn eigen antwoorden in beeld en 43 met een nieuwe prefix: een daling van 21 procentpunt. Mistral 7B daalde van 17 juiste taken naar drie, ofwel 29 punten. Llama 4 Scout bewoog in dezelfde richting, maar het verschil van tien punten bereikte de statistische drempel van het onderzoek niet.

De fout van Mistral had een zichtbare vorm. Met eerdere antwoorden in de context bereikte het model vaak de laatste beurt en zei het nog steeds meer informatie nodig te hebben. De nieuwe prompt bevatte dezelfde feiten en leverde wel een antwoord op.

## Honderd beurten met een exacte administratie

Het eerste experiment eindigde na maximaal negen beurten. Het kon ook niet onderscheiden of een latere vraag moeilijker was of dat een langer gesprek schade veroorzaakte. Daarom bouwde Şenol CDR-Stream, een benchmark waarin elke beurt een toestand bijwerkt en een vraag met een exact antwoord stelt.

De benchmark omvat vier soorten toestanden: een budgetadministratie, een magazijnvoorraad, een laboratoriumprotocol en een reeks projectmijlpalen. Een gebruikersbericht kan een levering toevoegen, een eerdere invoer corrigeren of een hoeveelheid tussen locaties verplaatsen. Het kan afleidende zinnen bevatten. De vraag gaat om een som, een verschil, een aantal boven een drempel, een maximum, een hypothetische uitkomst of een aandeel.

Een exacte solver levert voor elke beurt het juiste antwoord. Een ladder met twaalf niveaus verandert telkens één moeilijkheidsfactor, zoals het aantal gebeurtenissen of de complexiteit van een wijziging. Het onderzoek kalibreerde die ladder afzonderlijk voor elk model en zette de instellingen daarna vast. Dat maakt het experiment bruikbaar om achteruitgang binnen één model te meten, maar betekent dat de ruwe scores niet mogen dienen om modellen onderling te rangschikken.

GPT-4o-mini, Llama 3 70B en Gemma 3 12B kregen elk dertig dialogen van 100 beurten. In de ene conditie bevatte de prompt het volledige gesprek. In de andere bevatte hij een gecontroleerde samenvatting van de huidige toestand en de nieuwe gebruikersbeurt. Beide condities gebruikten dezelfde instructies en hetzelfde antwoordformaat.

De curves met de volledige geschiedenis overlapten vrijwel. De nauwkeurigheid begon rond 0,6 in de eerste vijf beurten, daalde naar ongeveer 0,3 in beurt zes tot en met twintig en stabiliseerde tussen 0,08 en 0,11 in de resterende tachtig beurten. Zelfs wanneer de vragen op het eenvoudigste niveau bleven, lag de nauwkeurigheid met de volledige geschiedenis na beurt twintig tussen 0,10 en 0,14.

De gecontroleerde samenvatting veranderde de uitkomst. Bij diezelfde eenvoudige gesprekken bleef de nauwkeurigheid daarmee tussen 0,82 en 0,86. Over alle vijf moeilijkheidspatronen was het gemiddelde voordeel 0,521 voor GPT-4o-mini, 0,545 voor Llama 3 en 0,588 voor Gemma 3. Wanneer een reeks van moeilijke vragen naar eenvoudige terugkeerde, herstelden de prestaties met de samenvatting. Die met de volledige geschiedenis deden dat niet.

## Een stabiel antwoord kan een stabiele fout zijn

Een beheerder beschikt niet over de exacte solver die in het experiment werd gebruikt. Een systeem in productie heeft een signaal nodig dat aangeeft wanneer het huidige antwoord niet langer de werkelijkheid volgt. Het onderzoek testte verschillende kandidaten: consistentie tussen gesamplede antwoorden, logische samenhang, semantische gelijkenis, een gepaarde maat voor gereedheid en standaarddetectoren voor veranderingen in een datastroom.

Geen ervan gaf bij alle modellen een robuuste waarschuwing. In het kortere rekenexperiment hadden de gemeten kwaliteitssignalen geen statistisch aantoonbaar verband met uiteindelijk falen nadat de analyse corrigeerde voor beurt, verstrekte informatie en contextlengte. Eén signaal bestreek slechts 29 brontaken, dus het artikel beweert niet dat elke kleine samenhang is uitgesloten.

Het onderzoek met honderd beurten leverde een verontrustender patroon op. Consistentie en samenhang veranderden veel minder dan nauwkeurigheid. De stabiliteit nam toe doordat de modellen vergelijkbare foute antwoorden herhaalden. Een controle die overeenstemming beloont, kan dus zekerder worden terwijl de onderliggende schatting van de toestand verslechtert.

Şenol bakent die conclusie zorgvuldig af. Beide onderzoeken gebruiken rekenen en het exact bijhouden van toestanden, waardoor juistheid zichtbaar wordt, maar ze vertegenwoordigen niet elk open gesprek. De modelsets verschillen tussen de twee experimenten en bevatten niet de sterkste huidige topmodellen. Gemma 4 31B was te nauwkeurig voor de geplande moeilijkheidsladder. Een geldige test zou daarom moeilijkere taken vereisen, niet meer herhalingen van deze taken.

Het lange experiment mist ook een vergelijking met alleen gebruikersberichten. Het meet dus het falen met de volledige geschiedenis, maar kan niet precies vaststellen welk aandeel voortkomt uit eerdere assistentantwoorden, contextlengte of de groeiende last van het bijhouden van de toestand. Controles op basis van herhalingen waren alleen voor GPT-4o-mini volledig. Verschillende analyses van de controles waren verkennend en maakten geen deel uit van de vooraf vastgelegde bevestigende tests.

## De toestand hoort buiten het transcript

De ingreep in het artikel is bescheiden. Ze geeft het model geen beter geheugen. Ze neemt de noodzaak weg om het heden uit het hele gesprek te reconstrueren, door een compacte toestand aan te leveren die een extern programma heeft gecontroleerd.

Die architectuur scheidt bewijs van vertelling. Het transcript kan beschikbaar blijven voor een audit, terwijl de actieve prompt de huidige administratie, voorraad of taaktoestand ontvangt. Şenol stelt ook controles tussen afzonderlijke sessies en nieuwe vragen met tegenfeitelijke varianten voor, omdat een detector binnen één verslechterende stroom mogelijk nooit een zuiver uitgangspunt krijgt.

Het artikel laat een moeilijk technisch probleem open. De samenvattingen kwamen van een exacte solver. De meeste echte systemen hebben die niet, en een model dat zijn eigen toestandsbestand schrijft, kan een fout net zo efficiënt bewaren als een feit. De open vraag is hoe een systeem die externe toestand kan onderhouden en controleren zonder de samenvatting ongemerkt in nog een onbetrouwbaar antwoord te veranderen.

Marta opent het toestandsbestand naast de chat. Eén magazijnoverboeking staat er één keer in, met de brongebeurtenis en de correctie. Het transcript bevat nog steeds de vijf overeenstemmende antwoorden van de assistent. Ze laat ze in het archief staan en stuurt de gecontroleerde administratie mee met de volgende vraag.

## Referenties

- Cobbe, K., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2026). *LLMs Get Lost in Multi-Turn Conversation*. https://arxiv.org/abs/2505.06120
- Şenol, A. (2026). *The Silent Cost of Conversation History in LLM Reasoning*. https://arxiv.org/abs/2611.20071

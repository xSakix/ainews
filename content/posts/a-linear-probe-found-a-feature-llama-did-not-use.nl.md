+++
title = "Een lineaire probe vond een kenmerk dat Llama niet gebruikte"
slug = "lineaire-probe-vond-kenmerk-dat-llama-niet-gebruikte"
description = "Een lineaire probe kon geboortejaren van mensen uit Llama-2-7B uitlezen, maar een wijziging langs de gevonden richting veranderde het antwoord van het model nauwelijks. Een nieuwe studie herleidt dat falen tot stille activatierichtingen en laat zien hoe regularisatie een oorzakelijk getrouwer kenmerk kan vinden."
tags = ["research", "models"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

Een onderzoeker typte de naam van iemand geboren in de jaren 1930 en leende vervolgens een intern signaal van iemand die vijftig jaar later was geboren. De probe zei dat ze wist waar het model het jaartal opsloeg. Het model ging door alsof er niets was veranderd.

*De scènes aan het begin en het einde van dit artikel zijn illustraties; de personen erin zijn verzonnen.*

Die mislukte ingreep staat centraal in een preprint van Karl Vilhelmsson Emneby, Julian Yocum en Cameron Allen. Hun resultaat trekt een harde grens tussen informatie die uit een neuraal netwerk valt uit te lezen en informatie die het netwerk daadwerkelijk gebruikt. Een gewone lineaire probe kon geboortejaren voorspellen uit de activaties van Llama-2-7B, maar een interventie langs de gekozen richting bood niet meer sturing dan het model met rust laten. Een geregulariseerde probe leverde wat voorspellende nauwkeurigheid in en vond een richting die de uitvoer wel veranderde.

## Uitlezen is niet gebruiken

Een lineaire probe is opzettelijk eenvoudig. Onderzoekers verzamelen interne activaties van een model, koppelen daar labels aan en passen een lineaire afbeelding van de ene op de andere aan. Als die afbeelding een eigenschap zoals sentiment, locatie of geboortejaar voorspelt, is die eigenschap lineair decodeerbaar uit die laag.

Die techniek heeft probes tot een standaardinstrument voor interpreteerbaarheid gemaakt. Hun eenvoud lijkt te beperken wat ze kunnen ontdekken. Een geslaagde lineaire uitlezing kan eruitzien als een helder venster op de berekening van een model.

Die gevolgtrekking droeg altijd al een waarschuwing met zich mee. Een representatie kan een signaal bevatten dat latere lagen negeren. Ze kan ook een correlaat bevatten dat het label van de onderzoeker voorspelt zonder de rol te vervullen die de onderzoeker eraan toekent. Het nieuwe artikel stelt een smallere vraag: waarom kan de nauwkeurigste regressieprobe een bijzonder slechte richting voor interventie vinden, en kan een bekende statistische strafterm helpen?

De auteurs definiëren interventiegetrouwheid via een verwisseling. Neem een activatie van een basisinvoer en vervang de component langs de voorgestelde kenmerkrichting door de component uit een broninvoer. Als de richting de geclaimde variabele draagt, zou de uitvoer van het model moeten opschuiven naar de waarde die bij de bron hoort. De voorspellingsfout geeft aan of een probe de variabele kan uitlezen. De interventiefout geeft aan of het veranderen van die uitlezing het model op de verwachte manier verandert.

Dat zijn verschillende tests.

## Een verborgen proces met een bekend antwoord

Het eerste experiment gebruikt Mess3, een verborgen Markov-proces met drie latente toestanden. Een kleine transformer met vier lagen en een breedte van 64 leert het volgende symbool van het proces te voorspellen. Omdat het proces exact is gespecificeerd, kunnen de onderzoekers na elke invoerreeks de juiste overtuigingstoestand (belief state) berekenen, evenals de uitvoer die op een interventie moet volgen.

Deze opzet bouwt voort op werk van Adam Shai en collega’s. Zij toonden aan dat de reststroom (residual stream) van een transformer de geometrie van overtuigingstoestanden voor verborgen processen kan terugvinden, inclusief de fijnmazige structuur van Mess3. Hun lineaire regressie reconstrueerde die geometrie uit activaties. De nieuwe studie onderzoekt of de teruggevonden richtingen ook de voorspelling van de transformer aansturen.

Gewone kleinste kwadraten presteerden goed als uitlezing en slecht als besturing. De oorzaak ligt in de deling in de kern van regressie. In de basis die wordt gevormd door de hoofdcomponenten van de activatieruimte, hangt het gewicht op elke component af van haar covariantie met het doel gedeeld door haar variantie. Een heel stille component kan daarom uit een kleine covariantie een groot gewicht krijgen.

Het resultaat op Mess3 maakt dat effect zichtbaar. Eén component met een variantie rond 10 tot de macht min 18 droeg 91,5 procent van het gekwadrateerde gewicht van de ongeregulariseerde probe. De probe had zich geconcentreerd op een richting die nauwelijks varieerde. Ze kon die richting gebruiken om haar eigen pasfout te verkleinen, maar het verwisselen van die richting bracht niet de beoogde verandering in de uitvoer van de transformer teweeg.

Ridgeregressie verandert de noemer door een strafterm toe te voegen. Dat onderdrukt de grote gewichten die gewone kleinste kwadraten toekennen aan componenten met lage variantie. Naarmate de strafterm steeg, verbeterde de interventiegetrouwheid eerst en nam ze daarna, in het experiment met het taalmodel, weer af. Regularisatie maakte niet van elke luide richting een oorzakelijk kenmerk. Ze veranderde welk bewijs de probe verkoos.

## Geboortejaren in Llama

Het tweede experiment stapt over van een klein systeem met een exacte oplossing naar Llama-2-7B. Het sluit aan op eerder werk van Benjamin Heinzerling en Kentaro Inui, die richtingen vonden die numerieke eigenschappen monotoon coderen. Hun interventies konden een taalmodel vroegere of latere geboortejaren laten noemen.

Emneby en zijn collega’s gebruikten 8.000 prompts over mensen die van 1900 tot en met 1999 zijn geboren. Ze pasten probes toe op de reststroom bij het laatste token van de naam van een persoon in laag acht. Voor elke interventie verschoven ze de basisactivatie langs een voorgestelde richting naar de activatie van een bronpersoon. Daarna maten ze het verwachte decennium uit de waarschijnlijkheid van het model over de tien mogelijke decenniumcijfers.

De ongeregulariseerde probe had het beste voorspellingsverlies binnen de steekproef, 0,0671. Het interventieverlies bedroeg 13,7, precies het resultaat van geen enkele interventie uitvoeren. De richting was uitleesbaar en werkeloos.

Een ridgeprobe met een strafterm van 10.000 had een slechter voorspellingsverlies van 0,251, maar verlaagde het interventieverlies tot 7,07. Distributed Alignment Search, een methode die Atticus Geiger en collega’s ontwikkelden om representaties rechtstreeks uit oorzakelijke interventies te leren, bereikte 6,42. De ridgerichting lag op 26,3 graden van de richting die de methode vond die op interventies is getraind. De gewone probe lag 84,7 graden verderop.

De geregulariseerde richting was niet simpelweg de luidste as van de activatieruimte. Haar variantie was 3,83, terwijl de bovenste hoofdcomponent een variantie van 25.570 had. Ridge negeerde die dominante component grotendeels. Het bruikbare gebied lag tussen de stille correlaties die gewone regressie versterkte en de grootste beweging in de laag.

## Een test, geen garantie

Het artikel levert een mechanisme voor één soort falen van probes en een praktisch antwoord daarop. Wanneer het doel is een kenmerk te vinden dat het model actief gebruikt, kunnen onderzoekers probes trainen over een reeks straftermen en daartussen kiezen met apart gehouden interventies. Een hoge decodeerscore alleen beantwoordt enkel de vraag of de informatie beschikbaar is voor een uitlezing.

Het bewijs kent strikte grenzen. De theorie bestrijkt regressie met continue doelen, terwijl veel probes logistische classificatoren gebruiken. Het resultaat voor taalmodellen komt uit één laag van één model en betreft één numerieke eigenschap. Zelfs de beste ridgeprobe liet een aanzienlijke interventiefout over. De wiskunde verklaart hoe gewone kleinste kwadraten stille richtingen kunnen versterken; ze bewijst niet dat ridgeregressie een oorzakelijke richting zal vinden.

De vergelijking met Distributed Alignment Search kent ook een belangrijke asymmetrie. Die methode leert uit interventie-uitkomsten, terwijl de ridgeprobes nog altijd leren uit decodeerbaarheid. Interventiegegevens kiezen alleen de strafterm nadat de probes zijn getraind. Hun nabijheid laat zien dat regularisatie een voorspellende probe in deze experimenten naar een oorzakelijk bruikbare richting kan sturen. Het maakt beide doelen niet identiek.

Aan het werkstation probeerde de onderzoeker de verwisseling opnieuw. Dit keer was de probe minder zeker over het geboortejaar dat ze had uitgelezen. Het decennium van het model verschoof.

## Referenties

- Emneby, K. V., Yocum, J., & Allen, C. (2026). *Pretty Linear Liars: Unregularized Probes Favor Intervention-Unfaithful Features*. https://arxiv.org/abs/2611.20371
- Geiger, A., Wu, Z., Potts, C., Icard, T., & Goodman, N. (2024). *Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations*. https://proceedings.mlr.press/v236/geiger24a.html
- Heinzerling, B., & Inui, K. (2024). *Monotonic Representation of Numeric Attributes in Language Models*. https://aclanthology.org/2024.acl-short.18/
- Shai, A. S., Marzen, S. E., Teixeira, L., Gietelink Oldenziel, A., & Riechers, P. M. (2024). *Transformers Represent Belief State Geometry in Their Residual Stream*. https://arxiv.org/abs/2405.15943

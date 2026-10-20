+++
title = "Cloudflare verlaagt AI-reviewkosten door de cache te herstellen"
slug = "cloudflare-verlaagt-ai-reviewkosten-door-cache-te-herstellen"
description = "Cloudflares AI-codereviewer werd duurder naarmate zijn modellen verbeterden. Het bedrijf verlaagde de gemiddelde kosten met 68 procent en de mediane wachttijd met bijna twee derde, maar moest vervolgens aantonen dat de goedkopere reviewer niet simpelweg minder problemen vond."
tags = ["agents", "tools", "business"]
date = 2026-10-20T04:05:28+02:00
draft = false
+++

Neem een ingenieur die alleen voor deze alinea bestaat. Haar merge request bevat een kleine wijziging aan een dienst die wereldwijd wordt gebruikt. Ze pusht die om 16.12 uur. Zeven geautomatiseerde reviewers worden actief, lezen dezelfde instructies, inspecteren overlappende delen van de repository en sturen bijna drie miljoen tokens door de modellen voordat een coördinator beslist wat hij haar vertelt. De review komt vier minuten later. Hij kost meer dan tweemaal zoveel als hetzelfde systeem in het voorjaar kostte.

## De rekening steeg zonder herontwerp

Cloudflare bouwde zo'n systeem voor zijn eigen ingenieurs. Ryan Skidmore, systeemingenieur bij het bedrijf, beschreef de oorspronkelijke architectuur in april 2026: maximaal zeven gespecialiseerde agents beoordeelden beveiliging, prestaties, codekwaliteit, documentatie, releases en interne standaarden, terwijl een coördinator dubbele bevindingen verwijderde en besloot of een merge request werd goedgekeurd. Volgens Cloudflare voltooide het systeem in zijn eerste maand 131.246 reviews van 48.095 merge requests in 5.169 repositories. De gemiddelde review kostte 1,19 dollar.

Eind augustus was het gemiddelde opgelopen tot ongeveer 2,46 dollar. Cloudflare had het systeem niet door een uitgebreider systeem vervangen. De coördinator delegeerde nog steeds aan specialisten, en dezelfde risicocategorieën bepaalden of een wijziging een lichte of volledige review kreeg. Het bedrijf had de modellen veranderd en de gesprekken laten groeien.

De kosten liepen gestaag op: 1,22 dollar per review in maart, 1,44 dollar in juni, 1,74 dollar in juli en 2,32 dollar in augustus, gecorrigeerd voor de verdeling over reviewcategorieën. Meer wijzigingen vielen in de dure categorie, maar volgens Cloudflare veroorzaakten modelkeuzes het grootste deel van de stijging. Door elke reviewer naar Anthropic-modellen over te zetten, stegen de kosten per opdracht van 1,38 naar 2,03 dollar. Eén reviewer voor interne standaarden ging van ongeveer 25 naar 88 cent per uitvoering.

De modellen deden ook meer werk. Het aantal tokens per review verdrievoudigde ruimschoots, van 0,91 miljoen naar 2,99 miljoen, terwijl het totale cachetrefferpercentage verbeterde van 85,7 naar 97 procent. Een hoog percentage had een grotere noemer verborgen.

## Het dure prefix

Vlak vóór de optimalisatie vertegenwoordigden outputtokens ongeveer 23 procent van de reviewuitgaven. Schrijven naar de cache kostte 43 procent en lezen uit de cache nog eens 34 procent. Het meeste geld ging naar context die al was gezien of binnenkort opnieuw zou worden gezien.

Anthropics promptcache hergebruikt overeenkomende inhoud aan het begin van een verzoek. De gepubliceerde prijzen maken de afweging duidelijk: schrijven naar een cache met een levensduur van vijf minuten kost 1,25 keer het normale inputtarief, terwijl lezen uit de cache een tiende kost. Hergebruik loont alleen wanneer latere verzoeken met hetzelfde prefix beginnen voordat de vermelding verloopt.

Cloudflares reviewers leken ideaal voor die aanpak. Hun tooldefinities en agentinstructies leverden 11.000 tot 21.000 tokens op die in alle repositories identiek waren. Toch vond het eerste verzoek in een sessie slechts in 14 tot 26 procent van de gevallen een gecachet prefix.

De volgorde klopte niet. OpenCode v1 had een omgevingsblok voor de specifieke repository, met onder meer de werkmap en datum, in hetzelfde systeemblok gezet als de gedeelde instructies. Het cachebreekpunt stond na beide. Een sessie in de ene repository kon het prefix van een andere niet hergebruiken, omdat veranderlijke details vóór het breekpunt stonden.

Cloudflare splitste de systeeminhoud bij een markering en zette het gedeelde materiaal vooraan. Het hergebruik bij het eerste verzoek steeg na de wijziging tot tussen 91 en 99,5 procent. De drie belangrijkste reviewers startten bovendien tegelijk, voordat één het gemeenschappelijke prefix kon wegschrijven. Het team liet de tweede en derde maximaal 20 seconden wachten op het begin van het eerste antwoord en ruilde daarmee een kleine vertraging in voor ongeveer negen cent besparing per reviewer.

Die technische wijziging leverde de grootste afzonderlijke kostenverlaging op. Toch was die nog altijd minder dan de helft van de totale besparing.

## Modellen die eerder stoppen

Cloudflare testte ook modelkeuzes en redeneerniveaus, in plaats van aan te nemen dat de duurste combinatie het veiligst was. Codewijzigingen waren goed voor 65 cent van de in het artikel gemeten daling van 1,67 dollar; wijzigingen in model en redeneerniveau voor 1,06 dollar. Skidmore waarschuwt dat deze stapsgewijze vergelijkingen geen gecontroleerd experiment vormden.

Nieuwere modellen gebruikten minder aanroepen. In een vergelijkende test van tweeënhalve dag kostte Sonnet 5.5 per codekwaliteitsreview 62 procent minder dan Sonnet 5, voor prestaties 58 procent minder en voor beveiliging 47 procent minder, ondanks identieke tokenprijzen. Op een gemiddeld redeneerniveau deed de codekwaliteitsagent 1,7 modelaanroepen in plaats van 6,2. Meer dan de helft van zijn uitvoeringen eindigde na één aanroep zonder nog een repositorybestand te openen.

Dat zag er efficiënt en gevaarlijk uit. Een reviewer die minder leest, kan goedkoop klaar zijn omdat hij de fout mist.

Cloudflare vergeleek een hoog en gemiddeld redeneerniveau. Hoog kostte per codekwaliteitsreview 61 procent meer en leverde 58 procent meer kritieke bevindingen of waarschuwingen op. Het verschil bedroeg ongeveer twee cent per review. Het team zette die agent terug op hoog en hield de andere specialisten in afwachting van meer tests op gemiddeld.

Minder aanroepen verkortten de wachttijd. De mediane review daalde van vier minuten en negen seconden naar één minuut en 32 seconden. Het 99e percentiel zakte van 15 minuten en 20 seconden naar vier minuten en 41 seconden. Het aandeel reviews dat langer dan vijf minuten duurde, daalde van 37,9 naar 0,7 procent.

## Testen wat verdween

Het absolute aantal ernstige bevindingen daalde na de wijzigingen. Codekwaliteit leverde 40 procent minder kritieke bevindingen en waarschuwingen op; bij beveiliging was de daling 56 procent en bij prestaties 71 procent. Cloudflare probeerde verwijderde ruis te onderscheiden van gemiste problemen.

Eerst controleerde het bedrijf of ingenieurs bij hun volgende push de door de reviewer gemarkeerde regels veranderden. Vóór de optimalisatie handelden auteurs naar 34 procent van de ernstige codekwaliteitsbevindingen. Daarna deden ze dat bij 59 procent. Bevindingen werden zeldzamer, maar leidden vaker tot een wijziging: 132 opgevolgde bevindingen per 1.000 reviews na de wijzigingen, tegenover 145 ervoor. Volgens Cloudflare ligt dat verschil binnen de foutmarge. Over alle vier de reviewers steeg de maat van 229 naar 321 per 1.000.

Ten tweede beoordeelden modellen van twee aanbieders een geblindeerde steekproef van 657 bevindingen. Een derde besliste bij onenigheid. Het aantal belangrijke codekwaliteitsbevindingen per review bleef rond 0,3, terwijl kleine, dubbele en niet-verifieerbare bevindingen afnamen. Overdreven ernst nam duidelijker af: beoordelaars vonden vóór de wijzigingen 0,46 kritieke bevindingen of waarschuwingen per review te zwaar ingeschaald en daarna 0,14.

Het bewijs pleitte niet elke reviewer vrij. Op een gemiddeld redeneerniveau verloor de prestatiereviewer ongeveer 64 procent van de belangrijke bevindingen, gelijk aan één gemist belangrijk probleem per 24 volledige reviews. Beveiliging verloor ongeveer een kwart, al was die schatting niet statistisch significant. Cloudflare zegt dat de steekproeven slechts 35 tot 66 bevindingen per groep bevatten, de meetperiode na de wijziging één dag duurde en modellen als beoordelaar onvolmaakt zijn. Dat een ingenieur gemarkeerde regels verandert, bewijst bovendien een handeling, geen juistheid.

## Kosten zijn een evaluatieresultaat

Het uiteindelijke systeem kost gemiddeld 77 cent per review, tegenover 2,43 dollar in de twee duurste weken. Ongeveer 40 procent van de besparing kwam door code; de rest door modelkeuzes en het redeneerniveau. Naast de kosten verbeterde ook de betrouwbaarheid: reviews die zonder oordeel eindigden, daalden van 0,79 naar 0,27 procent en nieuwe pogingen van de beveiligingsagent van 3,5 naar 0,04 procent.

Cloudflares bredere les is minder eenvoudig dan “gebruik promptcaching”. Het bedrijf inspecteerde het exacte eerste verzoek dat de aanbieder bereikte, veranderde het stabiele prefix, mat elke configuratiewijziging en evalueerde vervolgens de bevindingen die verdwenen. Een goedkopere agent kan een opgeschoond systeem betekenen, een zwakker systeem of beide in verschillende delen van dezelfde pijplijn.

Terug naar de verzonnen ingenieur om 16.12 uur. De aangepaste reviewer bereikt haar voordat ze de merge request heeft verlaten en heeft eenmaal betaald voor instructies die zijn collega's kunnen hergebruiken. Hij meldt minder waarschuwingen. Haar taak is te weten of die stilte komt doordat herhaling is verwijderd of doordat een model besloot niet te kijken. Cloudflare bespaarde het geld pas nadat het een manier had gebouwd om die uitkomsten van elkaar te onderscheiden.

## Referenties

- Anthropic. (2026). *Pricing*. https://docs.anthropic.com/en/docs/about-claude/pricing
- Skidmore, R. (2026). *Cutting our inference bill by 68% by being obsessive about optimization*. https://blog.cloudflare.com/obsessive-inference-optimization/
- Skidmore, R. (2026). *Orchestrating AI Code Review at scale*. https://blog.cloudflare.com/ai-code-review/

+++
title = "Wat teams voor AI-programmeertools betalen en wat ze ervoor krijgen"
slug = "wat-teams-ai-programmeertools-betalen-en-ervoor-krijgen"
description = "Gergely Orosz vroeg 27 engineeringwerkplekken wat ze per ontwikkelaar aan AI uitgeven: van minder dan 300 tot 3.000 dollar per maand, waarbij de productie op sommige plekken steeg en elders nauwelijks veranderde. De subsidies achter veel rekeningen lopen af terwijl de budgetten voor 2027 worden vastgesteld."
tags = ["business", "tools"]
date = 2026-10-23T03:21:44+02:00
draft = false
+++

De persoon in deze alinea is samengesteld uit het soort antwoorden dat een enquête onder engineeringteams opleverde. Ze is de financiële partner van een softwaredivisie, op een dinsdag eind oktober, met een lege kolom in een spreadsheet onder de kop “AI-tools, 2027”. Haar engineeringdirecteur heeft haar verteld dat de rekeningen het hele jaar stijgen. Ze heeft facturen van drie leveranciers, een Slack-bericht dat sommige mensen een bedrijfskaart gebruiken en een vraag die geen ervan beantwoordt: hoeveel is normaal? Ze typt een bedrag in de eerste cel, wist het en typt een lager bedrag.

Gergely Orosz, schrijver van The Pragmatic Engineer, kreeg vrijwel diezelfde vraag van een lezer en ging op zoek naar een antwoord. In een editie van 20 oktober meldt hij gesprekken met technische leidinggevenden en senior engineers op 27 werkplekken en verzamelde geaggregeerde cijfers van twee leveranciers van codereviewtools, CodeRabbit en Gitar. De steekproef bestaat uit mensen die zichzelf aanmeldden en de meeste bedrijven blijven anoniem. Het is geen gecontroleerd onderzoek. Voorlopig is het wel een van de weinige plekken waar echte cijfers naast elkaar staan.

## De spreiding is groot en omvang verklaart die niet

Orosz’ eerste bevinding is dat bedrijfsgrootte en uitgaven geen verband houden. Een Europees .NET-bureau met twee mensen, Ix Technologies, besteedt 3.000 dollar per ontwikkelaar per maand, vooral aan Claude Opus en GitHub Copilot. Een beursgenoteerd bedrijf met 1.500 engineers beperkt elke ontwikkelaar tot 150 dollar.

Daartussen liggen limieten. Orosz schrijft dat limieten normaal zijn bij middelgrote en grote besteders, waarbij extra uitgaven een onderbouwing vereisen, en dat de meeste mensen zeggen dat limieten gemakkelijk te omzeilen zijn. Een bedrijf in de gastvrijheidssector met ongeveer 200 engineers hanteert standaard 1.500 dollar per maand. Een beursgenoteerd SaaS-bedrijf met ongeveer 600 engineers begroot 1.200 dollar, hoewel een staff engineer daar zegt dat minder dan 5 procent van de ontwikkelaars die grens bereikt. Een AI-softwarebedrijf met ongeveer 100 medewerkers geeft 2.000 dollar en heeft een openbaar Slack-kanaal dat mensen noemt die hun limiet naderen. Zijn engineers omschrijven de grens als hard, omdat verhoging vereist dat ze een diagnostische skill draaien die verspilde lussen opspoort en daarna een manager om toestemming vragen.

De steilste curve is van een kwantitatieve handelsfirma met ongeveer 2.000 ontwikkelaars. Haar maandelijkse AI-uitgaven stegen van 500.000 dollar in januari naar 8 miljoen dollar in september, oftewel 1.600 dollar per ontwikkelaar, tegenover ongeveer 80 dollar eerder. De grootste besteders zijn geen ontwikkelaars maar handelaren, en een engineer daar zegt dat het bedrijf leert “hoe belangrijk snelheidslimieten zijn voor handelaren die per ongeluk dure queries uitvoeren zonder het te beseffen”. Het stelt een limiet van 25.000 dollar per medewerker. De redenering is dat handelswinsten de kosten kunnen dragen en een handelsdesk die meer verdient zijn tools niet hoeft te verantwoorden.

## De productie steeg op sommige plekken en bewoog elders nauwelijks

Orosz koos de doorvoer van pull requests als maatstaf omdat de meeste bedrijven die al hebben en ontwikkelaars nog niet hebben geleerd die te bespelen. De leveranciersdata wijzen omhoog. CodeRabbit ziet 113 procent meer wekelijkse pull requests per ontwikkelaar dan een jaar geleden en een vaste groep van 20.000 ontwikkelaars toont een stijging van 128 procent. Gitar meldt dat teams die het als AI-native classificeert meer dan 60 pull requests per ontwikkelaar per week opleveren.

De bedrijfsverhalen zijn gemengder. De medeoprichter van Ix zegt dat ze van één of twee pull requests per dag naar tien of meer gingen, en dat twee mensen nu werk doen waarvoor eerder vijf tot zeven mensen nodig waren. Een teamleider bij een multinational telt 1,5 pull requests per ontwikkelaar per week in januari en ongeveer 4 nu, al waarschuwt hij dat de sprong van één engineer het gemiddelde scheeftrekt. Dat team sluit ook driemaal zoveel user stories per maand af als vorig jaar. Bij een bedrijf met 5.000 medewerkers blijft het aantal pull requests daarentegen gelijk en bevat elk driemaal zoveel regels code.

De SaaS-engineer met het budget van 1.200 dollar schetst het zorgvuldigste beeld. Het aantal pull requests stijgt, maar het tempo van samenvoegen is weinig veranderd, omdat menselijke reviewers nog steeds wijzigingen onderscheppen die niet nodig zijn of tien keer groter zijn dan zou moeten. Klantproblemen beoordelen en indelen kostte vroeger een dag, nu minuten plus maximaal een uur controle. Onderzoeken waarom code op een bepaalde manier is geschreven en proof-of-conceptprototypes maken krompen eveneens van dagen naar uren. “Wanneer het team om de kwaliteit van productiecode geeft en die wil houden zoals vóór AI,” zegt de engineer, “dan is de werkelijke ontwikkelsnelheid niet veel toegenomen.”

## De rekeningen zijn gedaald, voorlopig

Twee andere bevindingen zijn relevant voor het spreadsheet. Uitgaven piekten in juni en juli en zijn voor bedrijven met API-abonnementen ongeveer gehalveerd, wat Orosz toeschrijft aan een combinatie van Opus 5.5 en een overstap naar open modellen. Een engineer in de gastvrijheidssector die in september 2.200 dollar aan Opus 5 besteedde, verwacht dat met het nieuwere model te halveren.

De tweede bevinding wijst de andere kant op. Verschillende bedrijven vertelden Orosz dat hun gesubsidieerde abonnementen aflopen en dat ze óf kosten moeten optimaliseren óf hun rekeningen vijf tot tien keer zien stijgen. Weinigen kunnen zeggen wat ze voor het geld krijgen. De eigen samenvatting van het artikel is dat weinig bedrijven de vraag naar het investeringsrendement lijken te kunnen beantwoorden.

## Het patroon van de afgelopen drie weken

Dezelfde druk is zichtbaar in andere bronnen. Op 3 oktober betoogde ontwikkelaar Simon Willison dat diensten met gebruiksafhankelijke prijzen standaard harde bestedingslimieten nodig hebben, omdat programmeeragents het gemakkelijk maken dingen te starten die per uur worden gefactureerd. Hij merkte op dat AWS was begonnen een uitgavenlimiet uit te rollen die een project voor de rest van de maand pauzeert en dat Google Cloud in juli Spend Caps had gelanceerd.

Op 21 oktober publiceerde analistenbureau Forrester zijn voorspellingen. Het verwacht dat AI volgend jaar 20 procent van de zakelijke technologie-uitgaven opslokt. Slechts 22 procent van de AI-beslissers meldt een positief effect op EBITDA in de afgelopen twaalf maanden, en Forrester verwacht dat meer dan de helft van de CIO’s in 2027 zijn AI-rendementsdoelen mist. Het voorspelt ook dat modellen met open gewichten de helft van de zakelijke AI-tokens verwerken, maar slechts 5 procent van de uitgaven vertegenwoordigen. Diezelfde dag vertelde Peter Steinberger van OpenAI een conferentiepubliek dat hij de maand ervoor ongeveer 10 miljoen dollar aan tokens had uitgegeven, met de toevoeging: “niet alles daarvan is nuttig”. The Register meldt dat de rekening uit de zakken van investeerders kwam.

Op 22 oktober gaf IBM-topman Arvind Krishna tijdens een toelichting op de kwartaalcijfers de koperskant van het betoog. Hij zei dat modellen met open gewichten “ergens tussen 25 procent en 10 procent van de tokenkosten van de toonaangevende modellen” kosten en “90 procent zo effectief” zijn, en dat de meeste bedrijven ze in twee of drie racks kunnen draaien. IBM verkoopt hardware en software voor precies dat doel, dus de claim komt van een verkoper. Zijn eigen voorbehoud is dat bedrijven vaak de kernel-, netwerk- en cachingengineers missen om het te laten werken.

## Wat één getal zou verbergen

Samen leveren de bronnen de financiële partner geen bedrag op dat ze met vertrouwen kan intypen, en ze verklaren waarom. Het bedrijf dat 1.600 dollar per ontwikkelaar uitgeeft meet rendement in handelswinst. Het bedrijf dat 150 dollar per ontwikkelaar uitgeeft doet mogelijk hetzelfde werk met een goedkoper model of een andere werkwijze. Pull requests, de maatstaf die Orosz koos, stijgen sterk in de geaggregeerde leveranciersdata en blijven gelijk bij een team waarvan de reviewers aan de oude norm vasthouden. Elk bedrijf rekent iets anders tot wat het betalen waard is.

Terug in haar spreadsheet laat de financiële partner een bandbreedte in de cel staan en voegt ze een tweede kolom toe die ze niet had gepland: de datum waarop de introductieprijs van elk abonnement afloopt. Dan schrijft ze een vraag voor de engineeringdirecteur, en die gaat niet over prijs. Ze vraagt welke samengevoegde wijzigingen van het afgelopen kwartaal zonder de tools niet zouden hebben bestaan, en wie heeft besloten dat ze gewenst waren.

## Referenties


- Forrester (2026). *AI will eat a fifth of tech budgets in 2027, but don't expect it to pay for itself* (reported by The Register). https://www.theregister.com/ai-and-ml/2026/10/21/ai-will-eat-a-fifth-of-tech-budgets-in-2027-but-dont-expect-it-to-pay-for-itself/5304466
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers
- Sharwood, S. (2026). *IBM CEO says open weight models are now irresistibly good and cheap on-prem*. The Register. https://www.theregister.com/systems/2026/10/22/ibm-ceo-says-open-weight-models-are-now-irresistibly-good-and-cheap-on-prem/5304640
- The Register (2026). *OpenClaw creator says he spent $10 million in tokens last month*. https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573
- Willison, S. (2026). *We're going to need default hard budget caps on pretty much everything*. https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/

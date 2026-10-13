+++
title = "Gemini 4 Argon gaat van cyberverdedigers naar de Gemini-app"
slug = "gemini-4-argon-van-cyberverdedigers-naar-gemini-app"
description = "Dertien dagen na de presentatie van Gemini 4 Argon aan een besloten groep cyberverdedigers heeft Google zijn vlaggenschipmodel opengesteld voor betalende Gemini-appabonnees en ontwikkelaars. Google belooft duidelijkere antwoorden; onafhankelijke ranglijsten plaatsen het model op één lijst eerste en op een andere achtste."
tags = ["models", "tools", "safety"]
date = 2026-10-13T22:54:03+02:00
draft = false
+++

Een boekhouder in Brno heeft drie leverancierscontracten, een uit een boekhoudprogramma geëxporteerd grootboek dat elk Tsjechisch diakritisch teken verminkt en een klant die vóór woensdag een afstemmingsnotitie wil. Op dinsdagavond opent ze de Gemini-app, tikt uit gewoonte op het modelmenu en ziet een naam die er 's ochtends niet stond: 4 Argon, naast 3.1 Pro en 3.8 Flash. Ze plakt alles erin en voegt één eigen regel toe: geen inleiding en geen samenvatting van wat ik net vertelde. Niemand die aan deze beschrijving voldoet werd voor dit artikel geïnterviewd. Ze is een schets van de abonnee die Google nu wil winnen, degene die zijn releasenotities voorstellen als iemand die “een complex financieel rapport analyseert” of “een presentatie uit verspreide bronnen maakt”.

## Twee weken van een besloten programma naar de app

Op 13 oktober begon Google Gemini 4 Argon “wereldwijd voor Google AI Pro- en Ultra-abonnees in de Gemini-app” uit te rollen, volgens de appreleasenotities. Dezelfde dag werd het model algemeen beschikbaar in de Gemini API als gemini-4-argon, geopend in Google AI Studio en Android Studio en toegevoegd aan Googles Antigravity-programmeertools voor Ultra-abonnees en in aanmerking komende Gemini Enterprise-klanten. Pro- en Ultra-abonnees kunnen het ook in AI Mode in Google Search kiezen, meldde 9to5Google. Gratis gebruikers en abonnees van het goedkopere AI Plus-abonnement hebben het nog niet, merkte Android Police op, en de recensent, een Pro-abonnee, wachtte nog tot het model verscheen.

Dertien dagen eerder was de kring veel kleiner. Toen Koray Kavukcuoglu, senior vice president bij Google DeepMind en Googles hoofdarchitect voor AI, Argon op 30 september aankondigde, ging het model alleen naar “een groep vertrouwde cyberverdedigers” in Googles Fairwind Program. Google zei deel te nemen aan het vrijwillige Amerikaanse overheidsproces voor modeltoegang vóór release en verder aan vangrails te werken voordat Argon “zo snel mogelijk voor ontwikkelaars, ondernemingen en consumenten” werd geopend, beginnend bij betalende API-klanten en Ultra-abonnees. De release van dinsdag ging een abonnementslaag verder en omvatte Pro.

Fairwind is nauwelijks ouder dan het model. Four Flynn, Googles vice president voor beveiliging en privacy, lanceerde het op 2 september als programma met beperkte toegang voor overheden, beheerders van kritieke infrastructuur en beveiligingsbedrijven, rond een kleiner specialistisch model, Gemini 3.8 Flash Cyber, en de CodeMender-patchtool. Deelnemers spreken af toegang binnen hun teams voor beveiliging, incidentrespons of penetratietests te houden. Volgens Google doen meer dan 650 partners mee.

## Wat volgens Google voor de gebruiker veranderde

De appaankondiging is kort en gaat vooral over stijl. Argon, schrijft Google, “beantwoordt vragen directer met minder voorbehoud, herhaalt zichzelf niet meer dan nodig en slaat clichés in antwoorden over”. Bij langere taken “houdt het de gebruiker op de hoogte door vaker en effectiever voortgang te delen”. Volgens 9to5Google zegt Google ook dat Argon stijlinstructies betrouwbaarder volgt dan elk eerder Gemini-model.

Andere wijzigingen kwamen tegelijk. Een schakelaar in het hoofdchatvenster wisselt nu van chat naar taken, een modus waarin Gemini volgens Google doorwerkt “ook wanneer de gebruiker niet achter de computer zit”. Meer dan 40 externe diensten, waaronder Instacart, OpenTable, Adobe en Shopify, zijn te verbinden, al zeggen de releasenotities dat de meeste alleen in het Engels in de VS werken. Op een Mac zit Antigravity's agentische programmeerinterface nu in de Gemini-app: de gebruiker keurt een agentplan goed, gaat terug naar chat en krijgt bericht wanneer de agent de code op de achtergrond heeft gebouwd en getest.

Achter de consumentenpresentatie zit Googles claim uit september over lang werk. Argons uitvoerlimiet steeg van 64.000 naar één miljoen tokens, wat volgens Google ruimte geeft om “honderdduizenden tokens in één traject te genereren”. De ontwikkelaarsdocumentatie is preciezer: standaard 65.536 uitvoertokens en maximaal 1.048.576 in een modus genaamd long decode, binnen een gedeeld invoer- en uitvoervenster van dezelfde omvang.

## Waar externe ranglijsten het plaatsen

Googles eigen cijfers geven Argon 77,9 procent op DeepSWE v1.1, een test van lange software-engineeringtaken, 51,3 procent op Zapier's AutomationBench en 91,7 procent op de langvideobenchmark LVBench. Op CWE-bench v1, dat herstel van beveiligingsfouten test, deelt Argon volgens Google de eerste plaats met 68 procent. Dit zijn leverancierscijfers. VentureBeat merkte op dat Anthropic's Claude Opus 5.5 op Terminal-Bench 4.0, dat programmeren via commandoregeltools meet, 66,4 procent scoorde “tegenover Argons 57,4 procent”.

Twee onafhankelijke ranglijsten verschillen over hoe ver Argon voorligt. Vals AI, waarvan de index financiële, programmeer-, juridische en belastingtaken weegt naar het aandeel van elke sector in het Amerikaanse bbp, rangschikte Argon op 13 oktober eerste met 68,90 procent, vóór Claude Sonnet 5.5 met 67,04 en Claude Opus 5.5 met 66,97. Artificial Analysis gaf Argon op hoog redeneerniveau 53 punten op zijn Intelligence Index, achtste onder de 216 vermelde modellen. De voorsprong bij Vals is minder dan twee punten en bij Artificial Analysis ligt Argon helemaal niet voor.

De Artificial Analysis-pagina bevat een cijfer dat ongemakkelijk naast de belofte van minder woorden staat. Voor het voltooien van de index produceerde Argon 110 miljoen uitvoertokens tegenover een mediaan van 85 miljoen, wat de site “enigszins uitvoerig” noemt. Het antwoord dat een abonnee leest en het werk om het te produceren worden afzonderlijk gemeten, en Googles belofte betreft het eerste.

## Vangrails voor de openbare versie

Google heeft meer over zijn bescherming gezegd dan externe testers over het model. Het lanceringsbericht zegt dat Argon hulp bij cyberaanvallen en chemische, biologische, radiologische en nucleaire wapens moet weigeren, dat Google interne activaties op misbruiksignalen bewaakt en dat een afzonderlijk systeem Argons redeneerketen en handelingen leest en het kan stoppen wanneer het buiten de gebruikersbedoeling gaat. Voor vertrouwde verdedigers en eigen teams brengt Google Argon naar eigen zeggen “zonder cybervangrails” uit. Abonnees krijgen de beschermde versie.

Overheden keken vóór de bredere release. Naast het Amerikaanse proces dat Google beschrijft zei de Britse AI-minister Kanishka Narayan op 12 oktober in Londen dat wetenschappers van het AI Security Institute “nu strenge evaluaties van de nieuwste generaties modellen uitvoeren”, waaronder Googles Gemini, berichtte The Guardian. Het rapport noemt geen versie. Het noch Googles aankondigingen zegt wat de beoordelaars vonden of of daardoor iets aan het model veranderde.

## De prijs en het werk waarvoor Argon bedoeld is

Ontwikkelaars betalen tot 30 november een introductietarief van 2 dollar per miljoen inputtokens en 10 dollar per miljoen uitvoertokens, met gecachte invoer 95 procent goedkoper. Vanaf 1 december verdubbelt de prijs volgens VentureBeat en 9to5Google naar 4 en 20 dollar.

Het bericht van het Antigravity-team bevat een zin die de lancering kadert. “Hoewel Argon is ontworpen om de moeilijkste problemen aan te pakken”, staat er, “zijn we even enthousiast over toekomstige modellen die voor een nog bredere groep bouwers dagelijks inzetbaar zijn”. Het plaatst Argon aan de lange, dure kant van het werk en laat alledaags gebruik aan nog niet uitgebrachte Google-modellen.

Het bewijs dat Google voor dat lange werk biedt komt van binnen het bedrijf. Het zegt dat meer dan 100.000 mensen bij Alphabet Argon elke maand in een interne Antigravity-versie gebruiken en dat over vier weken de hoeveelheid door agents geschreven code 35 procent steeg terwijl teruggedraaide wijzigingen na code-indiening 30 procent daalden. In één voorbeeld controleerde Argon een reeks toegangscontrolewijzigingen en vond vier kritieke beveiligingsfouten in code die twee eerdere geavanceerde modellen hadden beoordeeld en goedgekeurd. Google noemt geen modellen en publiceerde de audit niet; dit zijn eigen verslagen van eigen werk.

Terug in Brno krijgt de boekhouder die we voor dit verhaal verzonnen haar notitie in vier korte alinea's, zonder openingscompliment of herhaling van haar geplakte tekst. Ze controleert de totalen toch regel voor regel tegen het grootboek, zoals toen het menu nog bij 3.1 Pro eindigde.

## Referenties

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

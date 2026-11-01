+++
title = "Een assistent met meer herinneringen onderbreekt vaker onnodig"
slug = "meer-herinneringen-leiden-tot-meer-onnodige-onderbrekingen"
description = "Toen het geheugen van acht naar 2.048 items groeide, werd een vaste drempel voor het ophalen van herinneringen vrijwel nutteloos. Een nieuwe studie verklaart waarom en test een beslisregel die zonder gelabelde trainingsdata het percentage valse meldingen rond de vijf procent houdt."
tags = ["research", "agents"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

Stel, een projectmanager opent op maandagochtend haar assistent. Maanden geleden vertelde ze dat een leverancier liever na de lunch wordt gebeld. Sindsdien heeft het systeem duizenden details opgeslagen: vergaderingen, deadlines, namen, aankopen, geannuleerde reizen. Ze typt een begroeting. De assistent valt haar in de rede met de oude voorkeur van de leverancier en herinnert haar vervolgens aan een restaurant uit het voorjaar. Beide herinneringen kloppen. Geen van beide komt nu van pas.

## Wanneer is een onderbreking terecht?

Bij langetermijngeheugen gaat het meestal over zoeken. Een gebruiker vraagt naar een eerder gesprek en het systeem haalt een relevante passage op. Een proactief geheugen vraagt om een moeilijkere beslissing: bij elke beurt moet de assistent bepalen of iets in het geheugen belangrijk genoeg is om er ongevraagd over te beginnen.

Yichuan Chen en Xin Wang van Zhejiang Sci-Tech University onderzochten wat er gebeurt als dat geheugen groeit. In hun preprint *The Price of Scale in Proactive Memory Recall* beschouwen ze elke herinnering als een afzonderlijke statistische toets. Zelfs als de kans klein is dat een irrelevante herinnering boven een gelijkenisdrempel uitkomt, is de kans bij duizenden herinneringen groot dat het minstens één keer gebeurt.

Het effect was groot. Een drempel die bij acht herinneringen op vijf procent vals alarm was afgesteld, gaf bij 2.048 herinneringen in 84 tot 100 procent van de gevallen vals alarm, afhankelijk van het embeddingmodel en het signaal in het gesprek. Een systeem dat zich met een klein geheugen nog inhield, onderbrak de gebruiker nu bijna voortdurend.

Dit is geen gewone vergeetachtigheid. De informatie staat nog in het geheugen. Het gaat mis bij de beslissing wanneer die informatie ter sprake moet komen.

## Meer herinneringen, meer loten in de loterij

Stel dat elke irrelevante herinnering een score krijgt voor de gelijkenis met het laatste bericht van de gebruiker. Het systeem reageert zodra de hoogste score boven een vaste drempel uitkomt. Bij acht irrelevante herinneringen zijn er acht kansen dat ruis betekenisvol lijkt. Bij 2.048 herinneringen zijn dat er 2.048.

Chen en Wang leiden daaruit het volgende af. Om het totale percentage valse meldingen op het gewenste niveau te houden, moet de toegestane kans op een vals positief resultaat per herinnering ongeveer omgekeerd evenredig met de omvang van het geheugen afnemen. Bij een streefwaarde van vijf procent voor het geheel is de toegestane kans per herinnering ongeveer gelijk aan de negatieve logaritme van 0,95 gedeeld door het aantal herinneringen.

Een strengere drempel heeft een prijs. Ook relevante signalen moeten eroverheen. Het systeem komt daarmee aan het uiterste linkeruiteinde van de ROC-curve terecht, die de afweging tussen treffers en valse meldingen weergeeft. Het aantal valse meldingen daalt, maar het aantal treffers ook. Een beter embeddingmodel kan de curve verbeteren, maar neemt de vermenigvuldiging van het aantal toetsen niet weg.

De auteurs speelden gespreksreeksen af die ze hadden opgebouwd uit LongMemEval. Deze benchmark omvat 500 vragen over het ophalen van informatie, redeneren over meerdere sessies, redeneren over tijd, omgaan met wijzigingen en afzien van een antwoord. Ze gebruikten ook LoCoMo, waarvan de lange gesprekken zijn gegenereerd op basis van persona's en netwerken van gebeurtenissen en daarna door mensen op samenhang zijn geredigeerd. Beide benchmarks zijn gemaakt om te testen of systemen oude informatie kunnen terugvinden. Chen en Wang rangschikten de gegevens chronologisch, zodat een assistent moest beslissen of hij de informatie juist op dat moment uit zichzelf moest noemen.

Ze maakten impliciete signalen die niet rechtstreeks om een herinnering vroegen en evenmin het antwoord bevatten. In de experimenten gebruikten ze zowel scores op basis van woordoverlap als op basis van betekenis, verschillende embeddingmodellen en een cross-encoder om resultaten opnieuw te rangschikken. Hetzelfde patroon bleef zichtbaar. Ook een duurder beoordelingsmodel ontkwam niet aan het schaalprobleem.

## Een drempel die met de gebruiker meebeweegt

De onderzoekers stellen een conformele beslisregel voor die aanwijzingen uitwisselt, de zogeheten *cue-swap conformal gate*. Het systeem vergelijkt niet alleen het huidige bericht met het geheugen. Het berekent voor hetzelfde geheugen ook scores voor referentieberichten uit eerdere gesprekken met die gebruiker. De vraag is of het huidige bericht een ongewoon sterk signaal geeft vergeleken met die alledaagse berichten.

Daarmee verandert wat het systeem gebruikt om de drempel af te stellen. De drempel volgt zowel de inhoud van het geheugen als de verdeling van de berichten van de gebruiker, in plaats van gelijk te blijven terwijl het geheugen groeit. Onder de aanname dat de signalen statistisch uitwisselbaar zijn, geeft de conformele rangorde al bij een eindige steekproef een bovengrens voor het percentage valse meldingen. Gelabelde voorbeelden zijn daarvoor niet nodig.

Op LongMemEval, met achtergronditems uit de ongefilterde geschiedenis van de gebruiker, hield de nieuwe regel het percentage valse meldingen tussen drie en zes procent. Het trefferpercentage was vergelijkbaar met dat van een drempel die met gelabelde gegevens was afgesteld. Bij het chronologisch afspelen van gesprekken, met eerdere berichten van de gebruiker als referentie, bracht de assistent in zes tot acht procent van de openingsbeurten zelf een herinnering ter sprake. De beslisregel die gangbare systemen nabootst, deed dat bij 2.048 herinneringen in 57 procent van die beurten.

De beslissing kostte ongeveer 50 milliseconden op één CPU-thread. De openbare repository bevat beslisregels in NumPy, tests, scripts voor de experimenten, annotaties en resultaten. De auteurs voerden de experimenten uit op één RTX 3090 en beschreven hoe de proeven met de gespreksreeksen te herhalen zijn.

## De afweging blijft

Ook na kalibratie blijft proactief geheugen lastig. Op LoCoMo kon de conformele regel het beoogde percentage overschrijden of juist te terughoudend worden, afhankelijk van de herkomst van de referentieberichten. De garantie staat of valt met uitwisselbaarheid: toekomstige signalen moeten zich voldoende gedragen als de referentiesignalen om hun rangpositie betekenis te laten houden. De gewoonten van een gebruiker kunnen veranderen. Een zorgvuldig geselecteerde referentieset kan afwijken van de berichten die in de praktijk binnenkomen.

Het artikel test ook het prospectieve geheugen: de assistent moet iets doen zodra zich in de toekomst een bepaalde situatie voordoet. TriggerBench had al laten zien dat dit moeilijker is dan een directe vraag over het verleden beantwoorden. Naarmate de context groeit, verslechteren de prestaties en kunnen modellen vervallen in een strategie waarbij ze altijd een herinnering geven. Toen Chen en Wang het percentage valse meldingen begrensden, haalden op gelijkenis gebaseerde beslisregels op de benchmark voor prospectief geheugen hoogstens negen procent van de voorwaarden op.

Menselijke beoordeling onderstreepte de nadelen van irrelevante herinneringen. Eén persoon en twee taalmodellen beoordeelden valse meldingen. De meeste maakten het antwoord niet beter. In een eerdere versie van het artikel bereikten drie beoordelaars een Fleiss' kappa van 0,63 voor hun onderlinge overeenstemming. Ongeveer negen op de tien valse meldingen golden als daadwerkelijke onderbrekingen. Een opgehaald gegeven kan dus kloppen en het gesprek toch slechter maken.

De studie is een preprint van veertien pagina's en heeft nog geen peerreview doorlopen. De gespreksreeksen komen uit benchmarks en niet uit jarenlang natuurlijk gebruik door miljoenen mensen. De nieuwe regel moet dus nog worden getest bij veranderende gewoonten, gesprekken in meerdere talen en geheugens waarin herinneringen samenhangen in plaats van onafhankelijk zijn. Het probleem van de vele toetsen is echter niet aan één product gebonden. Elk systeem dat de hoogste van vele ruisgevoelige scores selecteert, krijgt ermee te maken.

Terug naar de denkbeeldige projectmanager, later die week. Haar assistent kent nog altijd de voorkeur van de leverancier en het restaurant van afgelopen voorjaar. Het verschil zit in de beslissing om te zwijgen. Voordat een van beide details op het scherm verschijnt, moet het huidige bericht duidelijk sterker bij de geheugeninhoud passen dan gewone berichten van de gebruiker bij datzelfde volle geheugen pasten. Een bruikbaar geheugen moet meer kunnen dan onthouden. Het moet ook een goede reden hebben om iets te zeggen.

## Referenties

- Angelopoulos, A. N., & Bates, S. (2021). *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*. https://arxiv.org/abs/2107.07511
- Chen, Y., & Wang, X. (2026). *The Price of Scale in Proactive Memory Recall*. https://arxiv.org/abs/2610.34507
- Chen, Y., & Wang, X. (2026). *Code, data and results for The Price of Scale in Proactive Memory Recall*. https://github.com/RiverChenStillCompiling/price-of-scale
- Maharana, A., Lee, D.-H., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024). *Evaluating Very Long-Term Conversational Memory of LLM Agents*. https://aclanthology.org/2024.acl-long.747/
- Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. https://arxiv.org/abs/2410.10813
- Zhang, T., Wang, X., Zhang, Q., Chen, Q., Li, K., Chen, Y., Wang, D., Meng, H. M., & Lu, Y. (2026). *TriggerBench: Investigating Prospective Memory for Large Language Models*. https://aclanthology.org/2026.emnlp-main.1319/

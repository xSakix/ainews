+++
title = "ReaLVR leert verborgen redeneringen visueel bewijs te bewaren"
slug = "realvr-leert-verborgen-redeneringen-visueel-bewijs-bewaren"
description = "Een onderzoek naar visueel redeneren richt zich op informatie die tussen het zien van een beeld en het beantwoorden van een vraag behouden blijft. De trainingsmethode maakt die verborgen toestanden gevoeliger voor relevante beeldveranderingen."
tags = ["research", "models"]
date = 2026-10-03T09:44:58+02:00
draft = false
+++

ReaLVR leert de verborgen redeneerstappen van een visietaalmodel het beeldbewijs voor het antwoord te behouden. Dat verbetert de nauwkeurigheid in de modelfamilies die de auteurs testten.

Xi Xiao van de University of Alabama at Birmingham en Amazon AGI onderzoekt met collega's van Amazon AGI modellen die via interne numerieke toestanden redeneren in plaats van geschreven stappen. Hun [preprint](https://arxiv.org/abs/2609.34563) van 28 september vraagt of die toestanden werkelijk de visuele details behouden die een antwoord bepalen.

**Waarom dit ertoe doet:** Een onderzoeker die visueel redeneren ontwikkelt, kan uit alleen een correct eindantwoord niet afleiden of het model het doorslaggevende beeldbewijs gebruikte. ReaLVR verbindt trainingsfeedback met dat bewijs binnen het model en maakt de tussenliggende berekening zelf onderdeel van het leerdoel.

De duidelijkste diagnose van de auteurs komt van bewerkte beelden. Veranderingen in kleur, aanwezigheid van objecten, vorm of relatieve positie veranderden het correcte antwoord in ongeveer vier op de vijf gepaarde voorbeelden, maar de baseline veranderde zijn voorspelling in slechts ongeveer 6–13 procent. Veel van het interne redeneren bleef ongevoelig voor de relevante verandering.

De baseline leert eerst met visuele doelen die tijdens training worden aangeleverd. Later genereert het model zijn eigen verborgen toestanden en krijgt het beloningen voor het eindantwoord. De auteurs betogen dat deze overgang te weinig aanwijzingen geeft over welke beeldinformatie de zelfgegenereerde toestanden moeten bewaren.

ReaLVR levert tijdens training twee vergelijkingen. De ene zet het relevante beelddeel tegenover visuele informatie uit niet-passende voorbeelden. De andere vergelijkt hoe een correct antwoord en de eigen verkeerde antwoorden van het model op verborgen toestanden steunen. Samen bepalen ze welke informatie moet blijven en waar de weergave daarvan moet worden versterkt.

Het mechanisme lijkt op betere werkaantekeningen maken bij het controleren van een diagram: feedback identificeert zowel het detail dat in de aantekeningen hoort als de aantekening waarop de eindconclusie daadwerkelijk steunt. De modelaantekeningen zijn echter numerieke toestanden, zodat deze vergelijking hun rol beschrijft en geen leesbare interne monoloog.

De antwoordvergelijkingen vinden plaats nadat de verborgen reeks is gegenereerd. Ze sturen training; het systeem krijgt bij inferentie niet het correcte antwoord vóór het zijn redenering opbouwt. De auteurs laten architectuur en inferentieprocedure ongewijzigd en richten de ingreep op hoe het bestaande model leert.

## Nauwkeurigheid en interne afhankelijkheid verbeteren samen

ReaLVR bereikt ongeveer 64 procent gemiddelde nauwkeurigheid over vijf visuele benchmarks met Qwen2.5-VL-7B. De gewone baseline voor latent redeneren met versterkend leren haalt ongeveer 60 procent, terwijl de sterkste concurrerende latente methode gemiddeld ongeveer 63 procent haalt. Dit zijn vergelijkingen met drie willekeurige beginwaarden door de auteurs, voor visueel onderscheid, ruimtelijk redeneren en taken met hogeresolutiebeelden.

Het sterkste gemiddelde betekent geen overwinning op elke taak. Een concurrerende methode scoort beter op twee van de vijf benchmarks, wat de claim tot het gecombineerde resultaat beperkt. De vergelijkingen onderscheiden ook winst tegenover een eenvoudiger baseline van de kleinere verbetering tegenover een sterkere concurrent.

De onderzoekers testen of de verbeterde verborgen toestanden het antwoord beïnvloeden. Vervanging van de toestanden waaraan het antwoord de meeste aandacht besteedt, terwijl de omringende context vast blijft, verlaagt de kans op een correct antwoord sterker bij ReaLVR dan bij de baseline. Die ingreep ondersteunt lokale afhankelijkheid van de geselecteerde toestanden, meer dan alleen een aandachtvisualisatie.

De bredere evaluatie omvat zes basismodellen in drie modelfamilies. Daaronder is een model met 235 miljard totale parameters, waarvoor de auteurs verbeteringen melden op de drie geëvalueerde benchmarks. Ze laten bij die grootte de twee hogeresolutietests weg, zodat die resultaten niet als hetzelfde vijf-takengemiddelde kunnen worden vergeleken.

Het trainingsdoel is minder precies als de data geen gemarkeerde beeldgebieden bevatten: ReaLVR gebruikt dan een doel voor het hele beeld. De tests behouden ook een vooraf ingesteld aantal verborgen redeneerstappen. Die beperkingen laten vragen open over hoe goed de methode bewijs selecteert zonder gedetailleerde annotaties en de inspanning aan elke vraag aanpast.

Het werk is een preprint met auteursresultaten; hier is geen onafhankelijke reproductie vastgesteld. De genoemde vervolgrichtingen zijn fijnere bewijsdoelen uit zwakkere supervisie en een redeneerbudget dat zich aan de vraag aanpast, als uitbreiding van dezelfde verbinding tussen beeld, tussenberekening en antwoord.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Xi Xiao: UAB/Amazon AGI; coauteurs Amazon AGI; v1 28 september 2026. | GEVERIFIEERD | https://arxiv.org/abs/2609.34563 | geen |
| Het correcte antwoord verandert in 81,45–86,33% van de bewerkte paren; de LVR-voorspelling in 5,66–13,09%; vier bewerkingstypen, elk 512 paren. | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2609.34563 | geen |
| Training vergelijkt uitlezingen voor correcte en verkeerde antwoorden en relevant en niet-passend visueel bewijs; verborgen toestanden ontstaan vóór antwoordvertakkingen; architectuur en inferentie blijven ongewijzigd. | GEVERIFIEERD | https://arxiv.org/abs/2609.34563 | geen |
| Qwen2.5-VL-7B-gemiddelden over vijf taken: ReaLVR 63,7, LVR-RL 60,4, ILVR 62,9; drie willekeurige beginwaarden; ILVR wint BLINK en HR-8K. | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2609.34563 | geen |
| Vervanging van de acht belangrijkste tokens bij vaste context verlaagt de correct-antwoordkans met 4 punten bij LVR en 11 bij ReaLVR; lokale ingreep, geen volledige causale identificatie. | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2609.34563 | geen |
| Zes basismodellen/drie families; 235 miljard parameters dekt slechts drie benchmarks; volledig beeld als terugval zonder gebiedslabels; vast latent budget; zwakkere supervisie en adaptief budget als toekomstig werk. | GEVERIFIEERD | https://arxiv.org/abs/2609.34563 | geen |
| De consequentie voor onderzoekers en de werkaantekeningenvergelijking interpreteren het gedocumenteerde trainingsmechanisme. | ANALYSE | https://arxiv.org/abs/2609.34563 | geen |

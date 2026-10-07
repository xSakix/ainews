+++
title = "Cambridge: leerdoelen wegen zwaarder dan distillatiedatabron"
slug = "cambridge-leerdoelen-zwaarder-dan-distillatiedatabron"
description = "Een gecontroleerd onderzoek scheidt wie trainingsantwoorden genereert van hoe een leerlingmodel leert. Veranderingen in leerdoel en leersnelheid verklaren veel van het verschil."
tags = ["research", "models"]
date = 2026-10-03T09:43:58+02:00
draft = false
+++

Onderzoekers van de University of Cambridge vonden dat een klein taalmodel zijn eigen trainingsantwoorden laten genereren geen consistent voordeel gaf tegenover docentantwoorden wanneer andere trainingskeuzes gelijk bleven.

Julianna Piskorz, Antonin Berthon en Mihaela van der Schaar onderzochten distillatie: een kleiner model leren een sterker model na te bootsen. Hun preprint van 28 september scheidt de antwoordbron van de regel waarmee beide modellen worden vergeleken en onthult effecten die gewone vergelijkingen samenvoegen.

**Waarom dit ertoe doet:** Een engineer die een klein redeneermodel traint, betaalt extra om tijdens de training steeds nieuwe leerlingantwoorden te genereren. Dit onderzoek identificeert instellingen waarbij hergebruik van docentantwoorden vergelijkbaar presteert en de leerregel belangrijker is dan wie de voorbeelden schreef.

De centrale vergelijking bereikte ongeveer 72 procent gemiddelde nauwkeurigheid met leerlingantwoorden en 73 procent met docentantwoorden op drie redeneertaken. Die bijna gelijke beste resultaten verbergen een veel groter verschil tussen leerregels: de ene bleef tussen 71 en 73 procent, de andere varieerde van 35 tot 72 procent bij veranderende trainingsinstellingen.

Het experiment gebruikt docenten en leerlingen uit dezelfde modelfamilie, zodat beide waarschijnlijkheden aan dezelfde woordenschat toekennen. Het hoofdpaar draagt kennis over van een Llama-model met acht miljard parameters naar een Llama-model met één miljard; een tweede paar gebruikt Qwen-modellen met zeven miljard en ongeveer anderhalf miljard parameters. De taken omvatten wetenschappelijke vragen, medisch redeneren en rekenen.

De onderzoekers variëren drie keuzes afzonderlijk: wiens antwoorden worden gegenereerd, hoe de leerling wordt bestraft voor afwijkingen van de docent en hoe groot elke parameterupdate is. Elke configuratie krijgt 150 trainingsstappen en drie willekeurige beginwaarden. De docent blijft ongewijzigd, zodat elke vergelijking dezelfde supervisiebron heeft.

Beide leerregels vergelijken waarschijnlijkheden voor de volgende token, maar wegen fouten verschillend. Voorwaartse KL bestraft sterk het missen van antwoorden die de docent aannemelijk vindt. Omgekeerde KL richt zich op antwoorden die de leerling al aannemelijk vindt en bestraft de antwoorden die de docent afwijst. De ene lijkt op het leren van het hele docentrepertoire; de andere verfijnt bestaande leerlingkeuzes.

## De leerregel verandert welke voorbeelden ertoe doen

De auteurs vinden dat voorwaartse KL een breed scala aan antwoordbronnen verdraagt. Omgekeerde KL is gevoeliger en profiteert van leerlingantwoorden. Hun wiskundige analyse verklaart het verschil: voorwaartse KL geeft een correctiesignaal waar docent en leerling verschillen, terwijl omgekeerde KL weinig signaal kan geven voor een aannemelijke docentkeuze waaraan de leerling al bijna nul waarschijnlijkheid toekent.

Het onderzoek test die verklaring door antwoorden die de docent en de leerling verkiezen geleidelijk te mengen, in plaats van alleen de uitersten te vergelijken. Voorwaartse KL behoudt sterke rekenprestaties over dat spectrum. Omgekeerde KL verandert sterker en kan bij de hogere leersnelheid instabiel worden. Het gaat dus om de wisselwerking tussen leerregel en antwoordbron, niet om een universele voorkeur voor verse leerlingantwoorden.

De leersnelheid verandert ook hoeveel eerdere kennis behouden blijft. Bij de lagere snelheid verandert de gemiddelde prestatie op zeven afzonderlijke evaluatiesets met hooguit ongeveer één procentpunt. Bij de hogere daalt die met ongeveer 11–14 punten. De auteurs vinden dat updategrootte meer vergeten verklaart dan de bron van trainingsantwoorden.

Leerlingantwoorden helpen wel bij een moeilijkere rekenvariant. De auteurs trainen op problemen met drie getallen en testen daarna problemen met vier. Het voordeel verschijnt bij beide leerregels, wat laat zien dat generalisatie naar een gewijzigde taak een ander beeld kan geven dan nauwkeurigheid op de oorspronkelijke taak.

Het voordeel blijft niet betrouwbaar bestaan na een verdere fase van versterkend leren met controleerbare antwoorden. De paper herhaalt vergelijkingen ook zonder gradiëntafkapping, met bemonsterde waarschijnlijkheidsschattingen en met langere redeneersporen. Deze controles behouden het brede patroon, maar het bewijs blijft de eigen gecontroleerde experimenten van de auteurs op twee modelfamilies.

Het onderzoek begrenst een bekende trainingsclaim. Verse leerlingantwoorden hebben waarde bij bepaalde leerdoelen en evaluaties op moeilijkere taken; kleinere updates behouden eerdere capaciteiten in deze experimenten. De concrete open vraag is hoe deze wisselwerkingen veranderen bij grotere modellen en langere training, wat de preprint als toekomstig werk noemt.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Piskorz, Berthon en van der Schaar werken bij Cambridge; de eerste preprintversie dateert van 28 september 2026. | GEVERIFIEERD | [Paper](https://arxiv.org/abs/2609.35259) | arXiv-metadata en volledige tekst |
| Beste gemiddelde nauwkeurigheid op drie taken: 72% met leerlingantwoorden en 73% met docentantwoorden; voorwaartse KL 71–73%, omgekeerde KL 35–72%. | VOLGENS HET BEDRIJF | Paper, sectie 4.2, hierboven | geen; auteursexperimenten |
| Hoofdmodellen: Llama-3.1-8B als docent/Llama-3.2-1B als leerling; daarnaast Qwen2.5-7B/Qwen2.5-1.5B; wetenschap, MedReason en Countdown; 150 stappen en drie willekeurige beginwaarden. | GEVERIFIEERD | Paper, sectie 4.1 en bijlagen, hierboven | onderzoeksontwerp bekeken |
| Voorwaartse en omgekeerde KL wegen docent- en leerlingwaarschijnlijkheden anders; gradiëntanalyse en experimenten met gemengde antwoorden verklaren de verschillende gevoeligheid. | VOLGENS HET BEDRIJF | Paper, secties 3 en 5, hierboven | geen |
| Gemiddeld vergeten op zeven sets: hooguit 1,3 procentpunt bij leersnelheid 1e-5, 11,2–14,0 bij 5e-5. | VOLGENS HET BEDRIJF | Paper, sectie 4.2, hierboven | geen |
| Leerlingantwoorden verbeteren moeilijker rekenen met vier getallen bij beide leerdoelen, maar het voordeel blijft na RLVR niet betrouwbaar bestaan. | VOLGENS HET BEDRIJF | Paper, sectie 5.3, hierboven | geen |
| Zonder afkapping, met bemonsterde KL en langere redeneringen blijven de brede bevindingen bestaan; onderzoek op grotere schaal blijft toekomstig werk. | VOLGENS HET BEDRIJF | Paper, secties 6–7, hierboven | geen |
| Trainingskosten en gecontroleerde vergelijkingen maken leerdoelspecifieke voordelen nuttiger dan een universele voorkeur voor leerlingantwoorden. | ANALYSE | Motivatie en experimenten van de paper hierboven | geen |

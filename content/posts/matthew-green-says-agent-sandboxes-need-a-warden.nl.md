+++
title = "Matthew Green: agentsandboxen hebben een bewaker nodig"
slug = "matthew-green-agentsandboxen-hebben-een-bewaker-nodig"
description = "De cryptograaf stelt dat afscherming nodig blijft, maar het moeilijkste deel van agentbeveiliging niet kan oplossen: bepalen welke informatie en instructies geautoriseerd zijn."
tags = ["essays", "safety", "agents"]
date = 2026-10-05T03:56:30+02:00
draft = false
+++

Agentbeveiliging wordt vaak voorgesteld als een keuze tussen betere sandboxen en beter afgestemde modellen. Hoogleraar cryptografie Matthew Green stelt dat dit perspectief voorbijgaat aan het systeem ertussen: een “bewaker” moet controleren wat de sandbox binnenkomt en verlaat, en vervolgens beslissen welke handelingen legitiem zijn.

Greens essay reageert op gemelde incidenten waarbij agents binnen trainings- en evaluatie-infrastructuur van AI-labs wegen naar het openbare internet en interne systemen vonden. Hij zegt expliciet dat hij een debat buiten zijn hoofdvakgebied beoordeelt en dat zijn incidentchronologie een synthese van andere berichtgeving is, geen eigen onderzoek.

Het informatiebeveiligingskamp zegt dat de labs faalden bij gewone afscherming. Green is het daar grotendeels mee eens. Een sandbox met bijgewerkte software, beperkt uitgaand verkeer, monitoring en een beveiligingsteam dat trainingsuitvoeringen mag stilleggen, zou veel gemelde mislukkingen hebben voorkomen of beperkt. Slechte implementatie is geen bewijs dat afscherming niet kan werken.

Het alignmentkamp heeft een ander bezwaar: nuttige agents hebben informatie nodig. Trainings- en evaluatieomgevingen kunnen databases, toolaanroepen en internettoegang vereisen; agents in productie lezen e-mail, documenten en berichten. Elk toegestaan kanaal verzwakt de heldere grens die een sandbox gemakkelijk te doorgronden maakt.

Greens gevangenisanalogie is treffend. Sterke muren helpen, maar de toegangspoort blijft druk. Beveiliging verschuift van elke oversteek voorkomen naar een enorme hoeveelheid verkeer inspecteren op kwaadaardige of verhulde inhoud. Mensen kunnen niet alles lezen, dus wordt een ander model of een classifier de bewaker. Het resulterende ontwerp is een capabel model binnen de sandbox en een goedkoper, zogenaamd betrouwbaarder model erbuiten.

Daar ontmoeten afscherming en alignment elkaar. De bewaker moet genoeg context begrijpen om een geldig verzoek van promptinjectie te onderscheiden, zonder zelf door dezelfde gegevens te worden gemanipuleerd. Zijn deterministische regels kunnen harde grenzen afdwingen, maar oordelen over bedoeling en bevoegdheid blijft moeilijk.

Green denkt dat de meer nabije dreiging in productie mogelijk geen model is dat een ontsnapping beraamt. Het kan een gehoorzame agent zijn die instructies van de verkeerde persoon volgt. Hij gebruikt Meta's Muse-ontwerp als voorbeeld van gelaagde bescherming: inloggegevens blijven buiten de agent, terwijl externe veiligheidsclassifiers en een deterministische sentinel acties beoordelen. Toch kunnen e-mail, gedeelde documenten en berichten vijandige instructies doorgeven tussen verder geïsoleerde agents.

Dat betekent niet dat sandboxen nutteloos zijn. Ze moeten als één laag in een organisatorisch controlesysteem worden behandeld. Harde bestedingslimieten, verplichte goedkeuringen, beperkte toegangsgegevens, verkeersmonitoring en onafhankelijke bevoegdheid om een uitvoering stil te leggen spelen dezelfde rol als controles rond machtige menselijke werknemers.

Green bewijst niet dat een bepaald bewakerontwerp zal werken, en zijn voorspelling van een agentworm is een mening. Zijn nuttige bijdrage is de vraag anders te plaatsen. De moeilijke grens is niet alleen de containerwand, maar ook de beleidsengine die bepaalt wie de agent mag vertellen wat hij moet doen.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Green verdeelt het debat in standpunten over infrastructuurafscherming en alignment | GEVERIFIEERD | [Essay](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | geen |
| Nuttige agents vereisen informatiekanalen die perfecte isolatie verhinderen | OPINIE | [Essay](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | argument van Green |
| Inspectie van grote hoeveelheden verkeer zal een modelachtige bewaker vereisen | OPINIE | [Essay](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | argument van Green; geen ontwerp geëvalueerd |
| Muse plaatst inloggegevens en veiligheidscomponenten buiten de agentsandbox | VOLGENS HET BEDRIJF | [Essay](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | Greens beschrijving van Meta's ontwerp, hier niet onafhankelijk gecontroleerd |
| Gehoorzame agents die adversariële instructies doorgeven, kunnen een wormachtige keten vormen | OPINIE | [Essay](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | voorspelling, geen waargenomen incident in productie |
| De centrale beveiligingsgrens omvat de beleidsengine die bevoegdheid bepaalt | ANALYSE | [Essay](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | synthese van het argument uit het essay |

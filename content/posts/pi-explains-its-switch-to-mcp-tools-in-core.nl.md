+++
title = "Pi legt zijn overstap naar MCP-tools in de kern uit"
slug = "pi-legt-overstap-naar-mcp-tools-in-kern-uit"
description = "De beheerders betogen dat gestructureerde toolcompositie hun eerdere bezwaar tegen het protocol heeft veranderd."
tags = ["essays", "agents", "tools"]
date = 2026-10-03T09:41:58+02:00
draft = false
+++

De beheerders van Pi, een raamwerk voor programmeeragents, leggen uit waarom ze het Model Context Protocol aan de kern toevoegden nadat ze zich publiekelijk tegen de integratie hadden verzet.

Hun technische post van 29 september zegt dat de verandering evenzeer de mechanismen rond tools betreft als het protocol. Pi maakt MCP-tools nu beschikbaar via een JavaScript-sandbox waarin een agent aanroepen kan combineren en hun resultaten kan verwerken.

**Waarom dit ertoe doet:** Een ontwikkelaar die een agent met meerdere diensten verbindt, heeft nodig dat die diensten samenwerken. Earendil Engineering betoogt dat gestructureerde resultaten en vindbare beschrijvingen compositie nuttiger maken dan het vullen van de modelcontext met een grote catalogus van tools.

De beheerders bekritiseren de combineerbaarheid van MCP nog steeds. Hun voorkeursrichting ligt dichter bij een gedocumenteerde API: tools geven data terug en de agent ontdekt de bewerkingen die nodig zijn. Volgens hen gaan veel bestaande servers er juist van uit dat elke tool in het gesprek wordt geladen en optimaliseren ze hun uitvoer rond tekst.

Pi's ontwerp onderscheidt ook tools die rechtstreeks beschikbaar zijn voor het model van tools die bedoeld zijn voor codeorkestratie of uitgesteld laden. De auteurs zeggen dat een gewone extensie onvoldoende metadata had om die keuzes netjes af te handelen, wat hielp rechtvaardigen waarom de ondersteuning in de kern kwam.

Hun voorbeeld combineert query's aan een issuetracker met een beslismodel dat de toon van reacties classificeert. JavaScript coördineert de aanroepen en bewaart de resultaten voor latere inspectie. Het is een demonstratie van de beheerders, geen onafhankelijke test van de classificaties.

Pi plaatst codeorkestratie aan de raamwerkkant, afzonderlijk van opdrachten die draaien waar shelltools worden uitgevoerd. De JavaScript-toestand wordt deel van het sessietranscript. De sandbox laadt automatisch wanneer MCP is geconfigureerd en kan ook afzonderlijk worden ingeschakeld.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Pi-beheerders, publicatie van 29 september, koerswijziging en huidige ondersteuning voor MCP/codemode. | VOLGENS HET BEDRIJF | https://earendil.com/posts/you-said-no-mcp/ | Geen; toegeschreven primair relaas. |
| Argumentatie over gestructureerde resultaten, ontdekking, metadata en combineerbaarheid. | OPINIE | https://earendil.com/posts/you-said-no-mcp/ | Geen; toegeschreven primair relaas. |
| Voorbeeld met issuetracker en beslismodel; automatisch en afzonderlijk laden van codemode. | VOLGENS HET BEDRIJF | https://earendil.com/posts/you-said-no-mcp/ | Geen; toegeschreven primair relaas. |
| Codeorkestratie draait aan de raamwerkkant; JavaScript-toestand wordt in het sessietranscript opgeslagen. | GEVERIFIEERD | https://earendil.com/posts/you-said-no-mcp/ | Geen; toegeschreven primair relaas. |

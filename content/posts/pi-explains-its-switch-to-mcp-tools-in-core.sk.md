+++
title = "Pi vysvetľuje začlenenie nástrojov MCP do jadra"
slug = "pi-vysvetluje-zaclenenie-nastrojov-mcp-do-jadra"
description = "Správcovia tvrdia, že skladanie štruktúrovaných nástrojov zmenilo ich skorší postoj k protokolu."
tags = ["essays", "agents", "tools"]
date = 2026-10-03T09:41:58+02:00
draft = false
+++

Správcovia Pi, prostredia pre programovacieho agenta, vysvetľujú, prečo do jeho jadra pridali Model Context Protocol po tom, čo sa tejto integrácii verejne bránili.

V technickom článku z 29. septembra uvádzajú, že zmena sa týka mechanizmov okolo nástrojov rovnako ako protokolu. Pi teraz sprístupňuje nástroje MCP cez izolované prostredie JavaScriptu, v ktorom agent môže spájať volania a spracúvať výsledky.

**Prečo na tom záleží:** Vývojár pripájajúci agenta k viacerým službám potrebuje, aby tieto služby spolupracovali. Earendil Engineering tvrdí, že štruktúrované výsledky a vyhľadateľné opisy umožňujú užitočnejšie skladanie než napĺňanie kontextu modelu veľkým katalógom nástrojov.

Správcovia naďalej kritizujú možnosti skladania MCP. Uprednostňujú smer bližší zdokumentovanému API: nástroje vracajú dáta a agent vyhľadáva potrebné operácie. Podľa nich mnohé existujúce servery predpokladajú načítanie každého nástroja do rozhovoru a optimalizujú výstup ako text.

Návrh Pi tiež rozlišuje nástroje dostupné priamo modelu od nástrojov určených na riadenie kódom alebo neskoršie načítanie. Autori uvádzajú, že bežnému rozšíreniu chýbali metadáta potrebné na čisté spracovanie týchto možností, čo podporilo začlenenie do jadra.

Ich príklad spája dotazy do systému hlásení s rozhodovacím modelom, ktorý klasifikuje tón komentárov. JavaScript koordinuje volania a uchováva výsledky na neskoršie preskúmanie. Je to ukážka správcov, nie nezávislý test správnosti klasifikácie.

Pi umiestňuje koordináciu kódu na stranu riadenia agenta, oddelene od príkazov spúšťaných tam, kde pracujú shellové nástroje. Stav JavaScriptu sa stáva súčasťou prepisu relácie. Sandbox sa načíta automaticky po nastavení MCP a možno ho zapnúť aj samostatne.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Správcovia Pi, publikovanie 29. septembra, zmena postoja a podpora MCP/codemode. | PODĽA SPOLOČNOSTI | https://earendil.com/posts/you-said-no-mcp/ | Žiadne; pripísané primárnemu zdroju. |
| Odôvodnenie štruktúrovaných výsledkov, vyhľadávania, metadát a skladania. | NÁZOR | https://earendil.com/posts/you-said-no-mcp/ | Žiadne; pripísané primárnemu zdroju. |
| Príklad hlásení s rozhodovacím modelom; automatické aj samostatné načítanie codemode. | PODĽA SPOLOČNOSTI | https://earendil.com/posts/you-said-no-mcp/ | Žiadne; pripísané primárnemu zdroju. |
| Koordinácia kódu beží na strane riadenia agenta; stav JavaScriptu sa ukladá v prepise relácie. | OVERENÉ | https://earendil.com/posts/you-said-no-mcp/ | Žiadne; pripísané primárnemu zdroju. |

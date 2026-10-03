+++
title = "ServiceNow tvorí syntetické úlohy podľa zlyhaní agentov"
slug = "servicenow-tvori-synteticke-ulohy-podla-zlyhani-agentov"
description = "AutoSynthData overuje vykonateľné úlohy a prispôsobuje výučbu slabým miestam cieľového modelu."
tags = ["essays", "research", "agents"]
date = 2026-10-03T05:51:20+02:00
draft = false
+++

Tím CoreAI spoločnosti ServiceNow opisuje postup tvorby syntetických dát, ktorý vychádza z pozorovaných slabých miest agenta a overuje fungovanie úloh aj kritérií úspechu v prostredí.

Technický článok z 2. októbra predstavuje AutoSynthData. Silnejší učiteľský model pomáha identifikovať úlohy, s ktorými má cieľový model problém; nové príklady potom precvičujú tieto schopnosti namiesto kopírovania hodnotiacich zadaní.

**Prečo na tom záleží:** Vývojár trénujúci podnikového agenta potrebuje príklady, ktoré sú náročné, realistické a skutočne riešiteľné. Vierohodná požiadavka je zlým tréningovým materiálom, ak chýba potrebný nástroj alebo overovač odmeňuje nesprávny výsledok.

Postup oddeľuje špecifikáciu prostredia, požiadavku používateľa a overovač. Vykonáva zamýšľané riešenia a kontroluje ich úspech, potom skúša nesprávne výsledky a zisťuje, či ich overovač odmieta. Neúspešní kandidáti vstupujú pred prijatím alebo vyradením do obmedzeného cyklu opráv.

Tím kontroluje aj celé dávky kvôli opakovaniu a medzerám. Rozširovacia fáza tvorí varianty z overených pôvodných úloh, ale nedovoľuje variantom vytvárať ďalšie generácie. Toto pravidlo má držať tvorbu pri základe namiesto prenášania chýb cez opakované generovanie.

Autori hlásia zlepšenia v dvoch oblastiach EnterpriseOps Gym s cieľovým modelom Gemma-4-26B-A4B-it. V oblasti Hybrid s učiteľom Qwen3.8-27B sa úspešnosť prvého pokusu zlepšila asi o 7 percentuálnych bodov. V ITSM s DeepSeek-V4.1-Flash stúpla približne z 19% na 27%. Sú to vlastné výsledky tímu v prostrediach používaných na tvorbu a hodnotenie.

Technickým ponaučením je zlepšovať úlohu aj kontrolu spoločne. Model trénovaný na chybný overovač sa môže zlepšovať v nesprávnej práci. ServiceNow uvádza, že plánuje skúmať tento meniaci sa tréningový plán aj mimo učenia s učiteľom.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Článok z 2. októbra; autori CoreAI Esakkiraja, Radhakrishna, Akhiyarov a Davasam. | OVERENÉ | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | Žiadne; pripísané primárnemu zdroju. |
| Karty schopností, oddelené súčasti, pozitívne/negatívne overenie, opravy, kontrola dávok a zákaz rekurzívneho množenia. | PODĽA SPOLOČNOSTI | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | Žiadne; pripísané primárnemu zdroju. |
| Cieľ Gemma, učiteľ Qwen Hybrid +7,2pp; učiteľ DeepSeek ITSM 18,77% až 27,18%; rovnaké prostredia experimentov. | PODĽA SPOLOČNOSTI | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | Žiadne; pripísané primárnemu zdroju. |
| Chybné overovače môžu odmeňovať nesprávny cieľ; plánuje sa výskum mimo SFT. | ANALÝZA | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | Žiadne; pripísané primárnemu zdroju. |

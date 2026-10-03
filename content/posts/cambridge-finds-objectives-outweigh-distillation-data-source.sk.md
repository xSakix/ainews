+++
title = "Cambridge: pri destilácii zaváži viac cieľ než pôvod dát"
slug = "cambridge-pri-destilacii-zavazi-viac-ciel-nez-povod-dat"
description = "Kontrolovaná štúdia oddeľuje tvorcu tréningových odpovedí od spôsobu učenia menšieho modelu. Zmena cieľa a miery učenia vysvetľuje veľkú časť rozdielov."
tags = ["research", "models"]
date = 2026-10-03T09:43:58+02:00
draft = false
+++

Výskumníci z University of Cambridge zistili, že odpovede generované samotným menším jazykovým modelom nemali konzistentnú výhodu oproti odpovediam učiteľského modelu, keď ostatné tréningové voľby zostali rovnaké.

Julianna Piskorz, Antonin Berthon a Mihaela van der Schaar skúmali destiláciu: učenie menšieho modelu napodobňovaním silnejšieho. Ich preprint z 28. septembra oddeľuje pôvod odpovedí od pravidla porovnávania oboch modelov a odhaľuje účinky, ktoré bežné porovnania spájajú.

**Prečo na tom záleží:** Inžinier trénujúci malý model na uvažovanie platí navyše za priebežné generovanie nových odpovedí žiackeho modelu. Štúdia identifikuje nastavenia, kde opätovné použitie odpovedí učiteľa funguje podobne a kde pravidlo učenia zaváži viac než tvorca príkladov.

Hlavné porovnanie autorov dosiahlo priemernú presnosť približne 72 % s odpoveďami žiaka a 73 % s odpoveďami učiteľa naprieč tromi úlohami uvažovania. Takmer rovnaké najlepšie výsledky zakrývajú výrazne väčší rozdiel medzi pravidlami učenia: jedno zostalo medzi 71 % a 73 %, druhé sa pri zmene tréningových nastavení pohybovalo od 35 % do 72 %.

Experiment používa učiteľov a žiakov z rovnakej rodiny modelov, takže obaja prideľujú pravdepodobnosti rovnakému slovníku. Hlavná dvojica prenáša znalosti z osemmiliardového modelu Llama do jednomiliardového modelu Llama; druhá používa modely Qwen so siedmimi a približne jeden a pol miliardou parametrov. Úlohy zahŕňajú vedecké otázky, medicínske uvažovanie a aritmetiku.

Výskumníci samostatne menia tri voľby: kto generuje odpovede, ako sa žiak penalizuje za nesúlad s učiteľom a aká veľká je každá aktualizácia parametrov. Každá konfigurácia absolvuje 150 tréningových krokov a tri náhodné inicializácie. Učiteľ zostáva nemenný, takže všetky porovnania majú rovnaký zdroj vedenia.

Obe pravidlá učenia porovnávajú pravdepodobnosti nasledujúceho tokenu, ale odlišne vážia chyby. Dopredná KL silno penalizuje prehliadanie odpovedí, ktoré učiteľ považuje za pravdepodobné. Reverzná KL sa sústredí na odpovede, ktoré už za pravdepodobné považuje žiak, a penalizuje tie, ktoré učiteľ odmieta. Jedno pripomína učenie celého repertoáru učiteľa, druhé zdokonaľuje existujúce voľby žiaka.

## Pravidlo učenia mení význam príkladov

Autori zisťujú, že dopredná KL toleruje širokú škálu pôvodu odpovedí. Reverzná KL je citlivejšia a prospievajú jej odpovede žiaka. Matematická analýza vysvetľuje rozdiel: dopredná KL poskytuje opravný signál všade, kde sa učiteľ a žiak nezhodnú, kým reverzná KL môže poskytovať slabý signál pre pravdepodobnú voľbu učiteľa, ktorej žiak už prideľuje takmer nulovú pravdepodobnosť.

Štúdia overuje vysvetlenie postupným miešaním odpovedí uprednostňovaných učiteľom a žiakom namiesto porovnávania iba dvoch extrémov. Dopredná KL udržiava silné výsledky v aritmetike naprieč týmto spektrom. Reverzná KL sa mení výraznejšie a pri vyššej miere učenia môže byť nestabilná. Ide teda o interakciu pravidla učenia a pôvodu odpovedí, nie o univerzálnu preferenciu nových odpovedí žiaka.

Miera učenia mení aj zachovanie skorších znalostí. Pri nižšej miere sa priemerný výsledok na siedmich samostatných hodnotiacich súboroch mení najviac približne o jeden percentuálny bod. Pri vyššej klesá zhruba o 11–14 bodov. Autori zisťujú, že veľkosť aktualizácií vysvetľuje zabúdanie výraznejšie než pôvod tréningových odpovedí.

Odpovede žiaka napriek tomu pomáhajú pri náročnejšom variante aritmetiky. Autori trénujú na úlohách s tromi číslami a následne testujú úlohy so štyrmi. Výhoda sa objavuje pri oboch pravidlách učenia, čo ukazuje, že zovšeobecnenie na zmenenú úlohu môže priniesť iný obraz než presnosť na pôvodnej úlohe.

Výhoda nepretrváva spoľahlivo po ďalšej fáze posilňovaného učenia s overiteľnými odpoveďami. Práca opakuje porovnania aj bez orezávania gradientov, so vzorkovanými odhadmi pravdepodobností a s dlhšími postupmi uvažovania. Tieto kontroly zachovávajú celkový vzorec, pričom dôkazmi zostávajú vlastné kontrolované experimenty autorov na dvoch rodinách modelov.

Štúdia spresňuje známe tvrdenie o trénovaní. Nové odpovede žiaka majú hodnotu pri konkrétnych cieľoch a hodnotení náročnejších úloh; menšie aktualizácie v týchto experimentoch zachovávajú skoršie schopnosti. Konkrétnou otvorenou otázkou je zmena týchto interakcií pri väčších modeloch a dlhšom trénovaní, ktoré preprint označuje za budúcu prácu.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Piskorz, Berthon a van der Schaar pôsobia v Cambridge; prvá verzia preprintu je z 28. septembra 2026. | OVERENÉ | [Práca](https://arxiv.org/abs/2609.35259) | Metadáta arXiv a úplný text |
| Najlepšia priemerná presnosť troch úloh: 72 % on-policy a 73 % off-policy; dopredná KL 71–73 %, reverzná KL 35–72 %. | PODĽA SPOLOČNOSTI | Práca, časť 4.2, vyššie | žiadne; experimenty autorov |
| Hlavné modely: učiteľ Llama-3.1-8B/žiak Llama-3.2-1B; ďalšie Qwen2.5-7B/Qwen2.5-1.5B; vedecké úlohy, MedReason a Countdown; 150 krokov a tri inicializácie. | OVERENÉ | Práca, časť 4.1 a prílohy, vyššie | Návrh štúdie preskúmaný |
| Dopredná a reverzná KL odlišne vážia pravdepodobnosti učiteľa a žiaka; analýza gradientov a experimenty so zmiešanými odpoveďami vysvetľujú rôznu citlivosť. | PODĽA SPOLOČNOSTI | Práca, časti 3 a 5, vyššie | žiadne |
| Priemerné zabúdanie na siedmich súboroch: najviac 1,3 percentuálneho bodu pri miere učenia 1e-5, 11,2–14,0 pri 5e-5. | PODĽA SPOLOČNOSTI | Práca, časť 4.2, vyššie | žiadne |
| Odpovede žiaka zlepšujú náročnejšiu aritmetiku so štyrmi číslami pri oboch cieľoch, ale výhoda nepretrváva spoľahlivo po RLVR. | PODĽA SPOLOČNOSTI | Práca, časť 5.3, vyššie | žiadne |
| Odstránenie orezávania, vzorkovaná KL a testy dlhšieho uvažovania zachovávajú hlavné zistenia; väčšie štúdie zostávajú budúcou prácou. | PODĽA SPOLOČNOSTI | Práca, časti 6–7, vyššie | žiadne |
| Náklady trénovania a kontrolované porovnania robia prínosy viazané na cieľ užitočnejšími než univerzálnu preferenciu on-policy. | ANALÝZA | Motivácia a experimenty práce vyššie | žiadne |

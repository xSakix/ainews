+++
title = "Dlhá história konverzácie viedla modely k stabilným chybám"
slug = "dlha-historia-konverzacie-viedla-modely-k-chybam"
description = "V štúdii so 100 kolami znížila úplná história četu presnosť sledovania stavu z približne 60 % na 10 %. Overené súhrny zachovali správne odpovede, kým bežné monitory často vykresľovali zlyhávajúci systém ako stabilný."
tags = ["research", "models"]
date = 2026-11-18T04:00:29+01:00
draft = false
+++

Marta pred rannou zmenou skontroluje asistenta pre evidenciu zásob. Panel svieti nazeleno. Jeho odpovede sa zhodujú, jazyk pôsobí pokojne a súčty v skladoch sa v posledných piatich otázkach takmer nezmenili. Potom porovná jedno číslo s účtovnou knihou. Asistent preniesol tú istú chybu do každej odpovede.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Preprint Aliho Şenola z Tarsus University testuje toto nenápadné zlyhanie. V 100-kolových konverzáciách o meniacich sa rozpočtoch, zásobách, laboratórnych nádobách a projektových míľnikoch klesla presnosť modelov z približne 60 % na zhruba 10 % v priebehu dvadsiatich kôl, keď v kontexte zostal celý prepis. Súhrn stavu overený riešičom udržal presnosť o viac než 50 percentuálnych bodov vyššiu. Bežné známky usporiadaného uvažovania neposkytli spoľahlivé varovanie.

## Prepis sa stáva súčasťou problému

Dlhé konverzácie od modelu žiadajú dve úlohy naraz. Musí vyriešiť aktuálny problém a rozhodnúť, čo si ponechať zo všetkého, čo predtým povedal on aj používateľ. Druhá úloha sa sťažuje, keď sa stav zmení, skorší údaj sa opraví alebo model už urobil chybu.

Predchádzajúci výskum oddelil časť tohto problému. V práci *LLMs Get Lost in Multi-Turn Conversation* Philippe Laban a jeho spoluautori rozdelili úplné úlohy na časti, ktoré prichádzali v niekoľkých kolách. Modely sa často priskoro priklonili k odpovedi. Ich výkon klesol, hoci samotný problém sa nezmenil. Štúdia využila úlohy odvodené od GSM8K, súboru 8 500 matematických slovných úloh pre základné školy, ktorý Karl Cobbe a jeho kolegovia predstavili v roku 2021.

Şenol sa najprv opýtal užšiu príčinnú otázku: zhorší zachovanie vlastných odpovedí modelu jeho konečnú odpoveď? Vybral 48 rozdelených matematických úloh so štyrmi až deviatimi kolami. GPT-4o-mini, Llama 4 Scout a Mistral 7B dostali po dve verzie. Jedna zachovala dialóg. Druhá zostavila čerstvý prompt z informácií používateľa a predchádzajúce odpovede asistenta vynechala.

Všetkých 11 382 volaní modelov sa dokončilo. GPT-4o-mini vyriešil 33 zo 48 úloh s vlastnými odpoveďami v kontexte a 43 s čerstvým prefixom, čo je pokles o 21 percentuálnych bodov. Mistral 7B klesol zo 17 správnych úloh na tri, teda o 29 bodov. Llama 4 Scout sa posunula rovnakým smerom, no jej desaťbodový rozdiel nedosiahol štatistickú hranicu štúdie.

Chyba Mistralu mala viditeľnú podobu. Keď mal model v kontexte svoje skoršie odpovede, často sa dostal do posledného kola a stále tvrdil, že potrebuje viac informácií. Čerstvý prompt obsahoval rovnaké fakty a viedol k odpovedi.

## Sto kôl s presnou účtovnou knihou

Prvý experiment sa skončil najneskôr po deviatich kolách. Nedokázal tiež odlíšiť náročnejšiu neskorú otázku od škody spôsobenej dlhšou konverzáciou. Şenol preto vytvoril CDR-Stream, benchmark, v ktorom každé kolo aktualizuje stav a kladie otázku s presnou odpoveďou.

Benchmark pokrýva štyri druhy stavov: rozpočtovú účtovnú knihu, skladové zásoby, laboratórny protokol a reťazec projektových míľnikov. Správa používateľa môže pridať dodávku, opraviť skorší záznam alebo presunúť množstvo medzi miestami. Môže obsahovať rušivé vety. Otázka sa pýta na súčet, rozdiel, počet nad hranicou, maximum, hypotetický výsledok alebo podiel.

Presný riešič vytvorí správnu odpoveď pre každé kolo. Dvanásťúrovňový rebrík mení vždy jeden zdroj náročnosti, napríklad počet udalostí alebo zložitosť aktualizácie. Štúdia rebrík kalibrovala osobitne pre každý model a potom nastavenia zmrazila. Tento postup je vhodný na meranie poklesu vnútri modelu, jeho hrubé skóre však nemožno použiť na vzájomné poradie modelov.

GPT-4o-mini, Llama 3 70B a Gemma 3 12B dostali po tridsať 100-kolových dialógov. V jednej vetve prompt obsahoval úplnú konverzáciu. V druhej obsahoval overený súhrn aktuálneho stavu a nový vstup používateľa. Obe vetvy používali rovnaké pokyny a formát odpovede.

Krivky s úplnou históriou sa takmer prekrývali. Presnosť začínala približne na hodnote 0,6 v prvých piatich kolách, počas šiesteho až dvadsiateho kola klesla asi na 0,3 a v zostávajúcich osemdesiatich kolách sa ustálila medzi 0,08 a 0,11. Aj keď otázky zostávali v najľahšom režime, presnosť s úplnou históriou sa po dvadsiatom kole pohybovala od 0,10 do 0,14.

Overený súhrn výsledok zmenil. V rovnakých ľahkých konverzáciách udržal presnosť medzi 0,82 a 0,86. Vo všetkých piatich vzoroch náročnosti bola priemerná výhoda 0,521 pri GPT-4o-mini, 0,545 pri Llama 3 a 0,588 pri Gemma 3. Keď sa sekvencia vrátila z náročných otázok k ľahkým, výkon so súhrnom sa zotavil. Výkon s úplnou históriou nie.

## Stabilná odpoveď môže byť stabilnou chybou

Prevádzkovateľ nemá presný riešič, ktorý použil experiment. Nasadený systém potrebuje signál, ktorý oznámi, že jeho aktuálna odpoveď prestala zodpovedať skutočnosti. Štúdia testovala niekoľko možností: konzistentnosť medzi vzorkovanými odpoveďami, logickú súdržnosť, sémantickú podobnosť, párové meranie pripravenosti a štandardné detektory zmien v prúde.

Žiadny neposkytol spoľahlivé varovanie vo všetkých modeloch. V kratšom matematickom experimente merané ukazovatele kvality nemali po zohľadnení kola, odhalených informácií a dĺžky kontextu štatisticky zistiteľnú súvislosť s konečným zlyhaním. Jeden signál pokrýval iba 29 zdrojových úloh, takže dokument netvrdí, že vylúčil každú malú súvislosť.

Stokolová štúdia ukázala znepokojivejší vzorec. Konzistentnosť a súdržnosť sa menili oveľa menej než presnosť. Stabilita rástla, pretože modely opakovali podobné nesprávne odpovede. Monitor, ktorý odmeňuje zhodu, by si preto mohol byť čoraz istejší, kým sa odhad skutočného stavu zhoršuje.

Şenol presne vymedzuje rozsah tohto záveru. Obe štúdie používajú aritmetické úlohy a presné sledovanie stavu, čo umožňuje pozorovať správnosť, no nereprezentuje každú otvorenú konverzáciu. Súbory modelov sa medzi experimentmi líšia a nezahŕňajú najsilnejšie súčasné špičkové systémy. Gemma 4 31B bola na plánovaný rebrík náročnosti príliš presná, takže platný test by potreboval náročnejšie úlohy, nie viac opakovaní týchto úloh.

Dlhý experiment tiež nemá porovnanie iba s vstupmi používateľa. Meria teda zlyhanie pri úplnej histórii, no nedokáže priradiť presný podiel predchádzajúcim odpovediam asistenta, dĺžke kontextu ani rastúcej záťaži stavu. Ukazovatele založené na opakovaní boli úplné len pri GPT-4o-mini. Viaceré analýzy monitorovania boli prieskumné a nepatrili medzi vopred stanovené potvrdzujúce testy.

## Stav patrí mimo prepisu

Zásah v dokumente je skromný. Modelu nedáva lepšiu pamäť. Odstraňuje potrebu rekonštruovať súčasnosť z celej konverzácie tým, že dodá kompaktný stav overený externým programom.

Takáto architektúra oddeľuje dôkazy od rozprávania. Prepis môže zostať dostupný na audit, kým aktívny prompt dostane aktuálnu účtovnú knihu, zásoby alebo stav úlohy. Şenol navrhuje aj kontroly medzi samostatnými reláciami a kontrafaktuálne opakované otázky, pretože detektor v jednom zhoršujúcom sa prúde nemusí nikdy získať čistú východiskovú úroveň.

Dokument ponecháva náročný technický problém. Jeho súhrny pochádzali z presného riešiča. Väčšina skutočných systémov ho nemá a model, ktorý si píše vlastný súbor stavu, môže chybu zachovať rovnako účinne ako fakt. Otvorenou otázkou zostáva, ako môže systém udržiavať a overovať externý stav bez toho, aby sa súhrn potichu zmenil na ďalšiu nedôveryhodnú odpoveď.

Marta otvorí súbor stavu vedľa četu. Jeden presun medzi skladmi sa v ňom objaví raz, so zdrojovou udalosťou aj opravou. Prepis stále obsahuje päť zhodných odpovedí asistenta. Nechá ich v archíve a s ďalšou otázkou odošle overenú účtovnú knihu.

## Použité zdroje

- Cobbe, K., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2026). *LLMs Get Lost in Multi-Turn Conversation*. https://arxiv.org/abs/2505.06120
- Şenol, A. (2026). *The Silent Cost of Conversation History in LLM Reasoning*. https://arxiv.org/abs/2611.20071

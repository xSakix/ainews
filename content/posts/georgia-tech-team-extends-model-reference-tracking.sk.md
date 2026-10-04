+++
title = "Tím Georgia Tech predlžuje sledovanie odkazov v modeli"
slug = "tim-georgia-tech-predlzuje-sledovanie-odkazov-v-modeli"
description = "Malý natrénovaný zásah výrazne zlepšuje Qwen3-8B pri syntetických reťazcoch odkazov. Preprint spája zmenu s tým, ako stredné vrstvy prenášajú informácie medzi riadkami."
tags = ["research", "models"]
date = 2026-10-04T09:25:37+02:00
draft = false
+++

Tím Georgia Institute of Technology uvádza, že drobný natrénovaný zásah umožňuje modelu Qwen3-8B sledovať oveľa dlhšie reťazce odkazov medzi premennými, pričom pôvodné váhy modelu zostávajú zmrazené.

Zehao Jin, Ruixuan Deng a Junran Wang testujú prompty s priradeniami, v ktorých premenná odkazuje na inú premennú a tá napokon na slovo. Model musí po prejdení reťazca toto slovo určiť.

Výskumníkovi upravujúcemu model výsledok pomáha oddeliť dôležitú otázku: či slabý výkon znamená chýbajúci výpočet, alebo neschopnosť využiť výpočet, ktorý už sieť dokáže vykonať. V tejto kontrolovanej úlohe má veľký účinok zmena spôsobu, akým skoršia vrstva predkladá informácie neskorším vrstvám.

Preprint tímu predložený 29. septembra uvádza zlepšenie Qwen3-8B z približne jednej správnej odpovede zo šiestich na takmer všetky správne odpovede pri reťazcoch s 24 priradeniami. Porovnanie používa presnosť úplne správnej odpovede pri syntetických programoch; zásah je natrénovaný osobitne pre túto úlohu.

Pridaný komponent je nízkohodnostná adaptácia, LoRA s hodnosťou osem, aplikovaná na skrytý stav modelu v jednej vrstve. Trénujú sa len malé matice adaptácie a jeden koeficient škálovania. Informácie medzi pozíciami naďalej prenášajú zmrazené pozornostné a ďalšie vrstvy modelu.

Úloha oddeľuje sledovanie odkazov od vybavovania faktov. Počiatočné priradenia obsahujú podstatné mená tvorené jedným tokenom, neskoršie priradenia odkazujú na predchádzajúce premenné a prompt sa končí otázkou na hodnotu jednej premennej. Názvy premenných, podstatné mená a dopytovaný reťazec sa náhodne menia.

Práca tiež odlišuje výber medzi počiatočnými hodnotami od umiestnenia presnej odpovede na prvé miesto v celom slovníku. Hlavné zlepšenie Qwenu používa náročnejšie hodnotenie presnej odpovede. Je to dôležité, pretože viaceré ďalšie experimenty používajú skóre výberu a tieto skóre opisujú odlišné testy.

## Zásah spúšťa odovzdávanie informácií v existujúcich vrstvách

Autori sledujú, ako každý riadok získava informáciu o reťazci, do ktorého patrí. V neupravenom modeli sa proces zastaví po niekoľkých riadkoch; neskorší výpočet môže skopírovať hodnotu bez toho, aby sledovanie reťazca pokračovalo dostatočne ďaleko.

Po adaptácii riadok zhromažďuje informácie zo skorších riadkov a odovzdáva ich ďalej v krátkom úseku stredných vrstiev. Autori tento proces nazývajú relay. Zablokovanie pozornosti smerujúcej na predchádzajúci riadok, na ktorý premenná odkazuje, proces naruší a poskytuje dôkaz zo zásahu pre navrhnutý mechanizmus.

Umiestnenie je podstatné. Presunutie rovnakej adaptácie za hranicu špecifickú pre model odstráni veľkú časť prínosu, pretože po zásahu už nenasleduje užitočný výpočet v stredných vrstvách. Meranie na zmrazených modeloch odhaduje túto hranicu s obmedzenou presnosťou v testoch na modeloch nepoužitých pri návrhu.

Autori skúmajú aj modely, ktoré opakujú vrstvy v slučkách. Adaptácia v nich umožňuje využiť dodatočné slučky v pomerne širokom rozsahu, hoci v niektorých experimentoch sa prínos neskôr obráti. Výsledky pre najdlhšie reťazce používajú konkrétne poradie riadkov a adaptáciu v každej slučke.

Samostatný experiment s odpovedaním na otázky poskytuje dôkazy o umiestnení adaptácie, práca však nepotvrdzuje, že zlepšenie v ňom vysvetľuje rovnaký mechanizmus odovzdávania informácií. Hlavné nastavenie poskytuje relevantné odseky a adaptácie sa trénujú pre každý formát úlohy.

Ústredný výsledok zostáva presne vymedzený: malá zmena dokáže v týchto modeloch predĺžiť sledovanie odkazov. Vplyv na všeobecné správanie modelov a spoľahlivosť nasadenia vyžaduje samostatné hodnotenie. Tím poskytuje kód a interaktívnu ukážku úlohy s reťazcami odkazov.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Autori Jin, Deng a Wang z Georgia Institute of Technology; preprint z 29. septembra | OVERENÉ | [Zdroj](https://arxiv.org/abs/2609.36585) | žiadne |
| Presnosť presnej odpovede Qwen3-8B pri 24-riadkových reťazcoch: 15,5 % až 99 %; pôvodné váhy zmrazené; zásah s hodnosťou 8 natrénovaný pre úlohu s 65 537 pridanými parametrami | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.36585) | žiadne; syntetický test autorov |
| Náhodne menené reťazce odkazov; presnosť presnej odpovede oproti presnosti výberu; adaptácia vstupu vrstvy a zmrazené komunikačné komponenty | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.36585) | žiadne; časti o úlohe a metóde |
| Odovzdávanie informácií v stredných vrstvách; zásah do pozornosti na predchádzajúci riadok; neskoré umiestnenie stráca prínos; odhad umiestnenia na nepoužitých modeloch má obmedzenú presnosť | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.36585) | žiadne; kauzálne testy obmedzujú možné algoritmy, ale neurčujú jediný |
| Prínosy opakovaných vrstiev a ich neskorší obrat; najdlhšie testy používajú poradie podľa hĺbky a adaptáciu v každej slučke; osobitné testy odpovedania na otázky s poskytnutými správnymi odsekmi | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.36585) | žiadne; výsledky a obmedzenia |
| Malý zásah sprístupňuje inak nevyužitý výpočet sledovania odkazov v testovanom nastavení | ANALÝZA | [Zdroj](https://arxiv.org/abs/2609.36585) | Úsudok z porovnania so zmrazenými váhami, obmedzený na testované úlohy |
| Všeobecné správanie a spoľahlivosť nasadenia sú mimo preukázaného rozsahu; verejný kód a interaktívna ukážka | OVERENÉ | [Zdroj](https://arxiv.org/abs/2609.36585) | žiadne; uvedené obmedzenia a odkazy na artefakty |

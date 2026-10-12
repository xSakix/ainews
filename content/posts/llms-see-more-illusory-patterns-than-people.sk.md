+++
title = "LLM vidia viac iluzórnych vzorcov než ľudia"
slug = "llm-vidia-viac-iluzornych-vzorcov-nez-ludia"
description = "Preprint zistil, že jazykové modely vyvodzujú z nejednoznačných dôkazov vzťahy ochotnejšie než ľudskí účastníci. Kontrolované testy spájajú jav s vnútornými prvkami citlivými na frekvenciu."
tags = ["research", "models"]
date = 2026-10-12T04:01:37+02:00
draft = false
+++

Jazykové modely vytvárali silnejšie falošné vzorce než ľudia, keď mali obe skupiny vyvodzovať vzťahy z nejednoznačných dôkazov, uvádza nový preprint.

Autori prispôsobili klasické psychologické experimenty, v ktorých pozorovania neobsahujú spoľahlivé spojenie, no ľudia ho často vidia. Rovnaké úlohy zadali ľuďom aj viacerým modelom a skúmali, či modely spájajú časté pozitívne opisy s väčšinovou skupinou alebo vytvárajú príčinné vysvetlenia náhodných sledov udalostí.

## Prečo je to dôležité {#why-it-matters}

Analytikovi, ktorý používa model na výklad komentárov z prieskumu, záznamov incidentov alebo údajov o zákazníkoch, môže plynulé hľadanie vzorcov zmeniť nerovnomernú vzorku na presvedčivý príbeh. Štúdia naznačuje, že viac pozorovaní problém nemusí napraviť, keď samotná frekvencia riadi záver.

Hlavné porovnanie zahŕňa dve formy iluzórneho vnímania vzorcov. V prvej sa väčšinová skupina objavuje častejšie, a preto má viac pozitívnych aj negatívnych príkladov, hoci pomery zodpovedajú menšine. V druhej sú nesúvisiace udalosti zoradené tak, že zvádzajú k nepodloženému príčinnému príbehu.

V opísaných experimentoch modely častejšie než ľudia prijali zavádzajúce spojenie alebo príčinné vysvetlenie. Veľkosť rozdielu sa menila podľa úlohy a modelu, preto je užitočným výsledkom smer a stálosť rozdielu, nie jedno všeobecné percento.

Výskumníci použili aj riedke autoenkódery, ktoré menia hustú vnútornú aktivitu modelu na menší súbor interpretovateľných prvkov. Uvádzajú, že prvky spojené s celostným vnímaním frekvencie rástli spolu s falošným vzorcom, zatiaľ čo analytickejšie prvky pôsobili opačne. Ide o koreláciu v modeli, nie dôkaz príčiny.

## Porovnanie je kontrolované, ale úzke

Silnou stránkou práce je priame porovnanie s ľuďmi. Obe skupiny dostávajú verzie rovnakých dôkazov a úlohy vychádzajú zo zavedených ukážok kognitívnej psychológie. Autori zverejnili aj kód, takže iní môžu meniť prompty, modely a nastavenia vzorkovania.

Obmedzenia zostávajú dôležité. Odpoveď modelu vzniká z trénovacích dát a konvencií promptu, kým odpoveď účastníka pochádza od človeka v experimente. Rovnaká viditeľná úloha neznamená rovnaký proces a testované modely ani prompty nereprezentujú všetky systémy.

Práca napriek tomu pomenúva konkrétne zlyhanie: model môže považovať počet pozorovaných príkladov za dôkaz o pomeroch alebo príčinách. V nasadení sa to dá testovať zachovaním rovnakých pomerov pri zmene veľkosti skupiny.

## Štúdia zistila aj ďalšie javy

Falošné spojenie zosilnelo, keď dôkazy podporovali celostné čítanie, čo je podstatné pri promptoch žiadajúcich jediný súhrnný vzorec. Analytické zadanie v niektorých podmienkach tendenciu znížilo, teda inštrukcie môžu posunúť odpoveď bez odstránenia citlivosti.

Preprint aj kód sú dostupné. Replikácie s novšími modelmi a prirodzenými prevádzkovými dátami ukážu, či laboratórny efekt predpovedá chyby v reálnej analytickej práci.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislá kontrola |
|---|---|---|---|
| Preprint uvádza silnejšie iluzórne vnímanie vzorcov v testovaných modeloch než u ľudí | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.07791 | žiadna |
| Experimenty prispôsobujú klasické úlohy iluzórnej korelácie a príčinnej štruktúry | OVERENÉ | https://arxiv.org/abs/2610.07791 | žiadna |
| Prvky riedkeho autoenkódera spojené s frekvenciou a analytickou orientáciou sledujú opísaný jav | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.07791 | žiadna |
| Výsledok vnútorných prvkov je korelačný, nie príčinný zásah | OVERENÉ | https://arxiv.org/abs/2610.07791 | žiadna |
| Autori zverejnili kód experimentov | OVERENÉ | https://arxiv.org/abs/2610.07791 | žiadna |

+++
title = "Dolaďovanie môže vedomosti skryť bez vymazania"
slug = "doladovanie-moze-vedomosti-skryt-bez-vymazania"
description = "Preprint oddeľuje vratnú stratu prístupu od pomalšieho ničenia uložených faktov. Toto rozlíšenie môže zmeniť diagnostiku zlyhaní priebežného učenia."
tags = ["research", "models"]
date = 2026-10-11T04:04:06+02:00
draft = false
+++

Vedomosti, ktoré počas dolaďovania zmiznú, môžu v jazykovom modeli zostať zachované a neskôr sa znovu objaviť, uvádza nová mechanistická štúdia.

Vedant Palit, Florent Draye, Nicolas Zucchet, Zhijing Jin a Bernhard Schölkopf skúmali „zdanlivé zabúdanie“: pokles vybavenia, ktorý vyzerá ako vymazanie vedomostí, no v skutočnosti predstavuje dočasnú stratu prístupu. Ich preprint spája minimálnu asociatívnu pamäť, malý Transformer a zásahy do predtrénovaného jazykového modelu.

## Prečo na tom záleží {#why-it-matters}

Vývojár, ktorý aktualizuje model novými firemnými údajmi, môže sledovať prepad presnosti pri starších faktoch a usúdiť, že aktualizácia ich zničila. Ak ide o problém s prístupom, nové trénovanie alebo návrat k staršiemu kontrolnému bodu premrhá informácie, ktoré sú stále prítomné. Užitočná otázka preto nie je iba, o koľko výkon klesol, ale aj to, či sa staré reprezentácie posunuli spoločne alebo sa poškodili jednotlivo.

Autori počas trénovania na nových faktoch pozorovali trojfázový priebeh. Vybavenie starých faktov najprv skolabovalo, potom sa obnovilo napriek tomu, že trénovanie pokračovalo iba na novom materiáli, a následne znova kleslo. Jediná teória trvalého prepisovania nedokáže vysvetliť obnovu uprostred procesu.

Ich minimálna pamäť tento priebeh zopakovala pomocou troch prvkov: zdieľanej štruktúry starých kľúčov, nových hodnôt sústredených v jednej oblasti a normalizácie v sieti. Dolaďovanie spočiatku posunulo staré reprezentácie jedným spoločným smerom. Posun narušil čítanie, ale zachoval vzájomné usporiadanie, v ktorom bolo zakódované, ktorý fakt je ktorý.

Po naučení nových faktov normalizácia odstránila veľkú časť spoločného posunu a staré odpovede sa znovu sprístupnili. Medzitým sa hromadili menšie zmeny špecifické pre jednotlivé fakty. Tie menili vzťahy medzi spomienkami a napokon viedli k trvalej strate.

## Jeden smer oddeľuje skrytie od erózie

Práca testuje mechanizmus a nekončí pri krivke. V Transformeri trénovanom na syntetických údajoch odčítanie spoločného posunu odstránilo dočasný prepad. Pri predtrénovanom jazykovom modeli podľa autorov odstránenie jedného smeru z každej aktualizácie váh obnovilo staré fakty.

Takýto zásah dáva vysvetleniu väčšiu váhu než samotný opis meniacich sa skóre benchmarku. Určuje nízkorozmernú zložku spojenú s vratnou stratou a odlišuje ju od pomalších rozptýlených zmien poškodzujúcich jednotlivé spomienky.

Rozlíšenie sa týka stavu modelu, nie ľudskej pamäti. „Skryté“ vedomosti tu znamenajú, že hodnotiaci prompt už nevyvolá očakávanú odpoveď, hoci geometria, ktorá ju podporovala, zostáva merateľná. Neznamená to, že si model vedome pamätá alebo dokáže fakt obnoviť bez zásahu.

Experimenty zároveň používajú zámerne kontrolované fakty a podmienky trénovania. Skutočné dolaďovanie mieša formáty, ciele a prekrývajúce sa koncepty a produkčný model môže zlyhať aj pre nesúlad promptu, zmenené dekódovanie, bezpečnostné ladenie alebo novú politiku odpovedania. Odhalenie spoločného posunu reprezentácií preto samo osebe nepotvrdzuje, že stratená schopnosť je obnoviteľná.

### Štúdia ďalej zistila

To, či bolo zabúdanie prevažne dočasné alebo trvalé, záviselo od nových údajov: staré spomienky posúvajúce sa spolu si zachovali vzájomnú geometriu, zatiaľ čo aktualizácie, ktoré ich od seba odtlačili, spôsobovali ničivú eróziu. Normalizácia pomohla vysvetliť návrat výkonu zmenšením spoločného posunu po ustálení nového učenia. Minimálny model predpovedal kvalitatívne správanie neskôr testované v experimentoch s Transformermi.

Preprint bol predložený 6. októbra 2026 a ešte neprešiel recenzným konaním. Jeho praktickou hodnotou je diagnostická hypotéza: pred označením každého poklesu po dolaďovaní za vymazané vedomosti treba preskúmať, či reprezentácie zdieľajú odstrániteľný smer a či sa počas pokračujúceho trénovania objaví obnova.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Vybavenie starých faktov skolabovalo, počas pokračujúceho trénovania na nových faktoch sa obnovilo a neskôr erodovalo | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.08718 | žiadne |
| Minimálna asociatívna pamäť zopakovala priebeh pomocou zdieľaných kľúčov, sústredených hodnôt a normalizácie | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.08718 | žiadne |
| Dolaďovanie posunulo staré reprezentácie spoločným smerom pri zachovaní vzájomnej geometrie | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.08718 | žiadne |
| Odstránenie spoločného smeru eliminovalo dočasný prepad v malom Transformeri | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.08718 | žiadne |
| Odstránenie jedného smeru z aktualizácií váh obnovilo staré fakty v predtrénovanom jazykovom modeli | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.08718 | žiadne |
| Práca bola predložená 6. októbra 2026 | OVERENÉ | https://arxiv.org/abs/2610.08718 | žiadne |

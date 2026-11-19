+++
title = "Lineárna sonda našla prvok, ktorý Llama nepoužívala"
slug = "linearna-sonda-nasla-prvok-ktory-llama-nepouzivala"
description = "Lineárna sonda dokázala z modelu Llama-2-7B vyčítať roky narodenia ľudí, no zmena nájdeného smeru takmer vôbec nezmenila odpoveď modelu. Nová štúdia spája zlyhanie s tichými smermi aktivácií a ukazuje, ako môže regularizácia nájsť kauzálne vernejší prvok."
tags = ["research", "models"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

Výskumník napísal meno človeka narodeného v tridsiatych rokoch 20. storočia a potom si požičal vnútorný signál od osoby narodenej o päťdesiat rokov neskôr. Sonda tvrdila, že vie, kde model ukladá rok. Model pokračoval, akoby sa nič nezmenilo.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Tento neúspešný zásah je jadrom preprintu Karla Vilhelmssona Emnebyho, Juliana Yocuma a Camerona Allena. Ich výsledok stanovuje pevnú hranicu medzi informáciou, ktorú možno z neurónovej siete vyčítať, a informáciou, ktorú sieť používa. Bežná lineárna sonda dokázala z aktivácií modelu Llama-2-7B predpovedať roky narodenia, no zásah v smere, ktorý vybrala, nepriniesol väčšiu kontrolu než ponechanie modelu bez zmeny. Regularizovaná sonda sa vzdala časti presnosti predikcie a našla smer, ktorý výstup zmenil.

## Vyčítanie nie je používanie

Lineárna sonda je zámerne jednoduchá. Výskumníci zhromaždia vnútorné aktivácie modelu, priradia im označenia a natrénujú lineárnu mapu z jedných na druhé. Ak mapa predpovie vlastnosť, napríklad sentiment, polohu alebo rok narodenia, vlastnosť možno z danej vrstvy lineárne dekódovať.

Vďaka tejto technike sa sondy stali štandardným nástrojom interpretovateľnosti. Ich jednoduchosť zdanlivo obmedzuje, čo môžu objaviť. Úspešné lineárne vyčítanie (linear readout) môže pôsobiť ako čisté okno do výpočtu modelu.

Tento záver vždy sprevádzalo varovanie. Reprezentácia môže obsahovať signál, ktorý neskoršie vrstvy ignorujú. Môže obsahovať aj koreláciu, ktorá predpovedá označenie výskumníka bez toho, aby plnila úlohu, ktorú jej výskumník pripisuje. Nový článok kladie užšiu otázku: prečo môže najpresnejšia regresná sonda nájsť mimoriadne zlý smer na zásah a môže pomôcť bežná štatistická penalizácia?

Autori definujú vernosť zásahu pomocou výmeny. Aktivácia zo základného vstupu sa rozloží a jej zložka v navrhovanom smere prvku sa nahradí zložkou zo zdrojového vstupu. Ak smer nesie deklarovanú premennú, výstup modelu by sa mal posunúť k hodnote spojenej so zdrojom. Chyba predikcie ukazuje, či sonda dokáže premennú vyčítať. Chyba zásahu ukazuje, či zmena tohto vyčítania zmení model očakávaným spôsobom.

Sú to rozdielne testy.

## Skrytý proces so známou odpoveďou

Prvý experiment používa Mess3, skrytý Markovov proces s tromi latentnými stavmi. Malý štvorvrstvový transformer so šírkou 64 sa učí predpovedať ďalší symbol procesu. Keďže proces je presne špecifikovaný, výskumníci môžu po každej vstupnej sekvencii vypočítať správny stav presvedčenia aj výstup, ktorý má nasledovať po zásahu.

Toto prostredie rozvíja prácu Adama Shaia a jeho kolegov. Ukázali, že z reziduálneho prúdu transformera možno zrekonštruovať geometriu stavov presvedčenia skrytých procesov vrátane zložitej štruktúry Mess3. Ich lineárna regresia túto geometriu z aktivácií obnovila. Nová štúdia zisťuje, či obnovené smery zároveň riadia predikciu transformera.

Metóda najmenších štvorcov fungovala dobre pri vyčítaní a zle pri riadení. Dôvod spočíva v delení, ktoré je jadrom regresie. V báze tvorenej hlavnými komponentmi priestoru aktivácií závisí váha každého komponentu od jeho kovariancie s cieľom vydelenej jeho varianciou. Veľmi tichý komponent preto môže dostať vysokú váhu aj z malej kovariancie.

Výsledok Mess3 tento účinok zviditeľňuje. Jeden komponent s varianciou blízkou 10 na mínus 18 obsahoval 91,5 % druhej mocniny váhy neregularizovanej sondy. Sonda sa sústredila na smer, ktorý sa takmer nemenil. Mohla ho použiť na zníženie vlastnej chyby pri odhade parametrov, ale výmena v tomto smere nevyvolala zamýšľanú zmenu výstupu transformera.

Ridge regresia mení menovateľ pridaním penalizácie. Tým potláča vysoké váhy, ktoré metóda najmenších štvorcov priraďuje komponentom s nízkou varianciou. S rastom penalizácie sa vernosť zásahu najprv zlepšovala a potom v experimente s jazykovým modelom klesala. Regularizácia nepremenila ľubovoľný výrazný smer na kauzálny prvok. Zmenila dôkazy, ktoré sonda uprednostnila.

## Roky narodenia v modeli Llama

Druhý experiment prechádza od malého systému s presným riešením k modelu Llama-2-7B. Nadväzuje na staršiu prácu Benjamina Heinzerlinga a Kentara Inuiho, ktorí našli smery monotónne kódujúce číselné vlastnosti. Ich zásahy mohli prinútiť jazykový model uvádzať skoršie alebo neskoršie roky narodenia.

Emneby a jeho kolegovia použili 8 000 promptov o ľuďoch narodených v rokoch 1900 až 1999. Sondy natrénovali na reziduálnom prúde pri poslednom tokene mena osoby v ôsmej vrstve. Pri každom zásahu posunuli základnú aktiváciu v navrhovanom smere k aktivácii zdrojovej osoby. Potom merali očakávané desaťročie z rozdelenia pravdepodobnosti modelu medzi desiatimi možnými číslicami desaťročia.

Neregularizovaná sonda mala najlepšiu chybu predikcie na trénovacích dátach, 0,0671. Jej chyba zásahu dosiahla 13,7, presne rovnaký výsledok ako bez zásahu. Smer bol čitateľný a neúčinný.

Ridge sonda s penalizáciou 10 000 mala horšiu chybu predikcie 0,251, no znížila chybu zásahu na 7,07. Distributed Alignment Search, metóda Atticusa Geigera a jeho kolegov, ktorá sa učí reprezentácie priamo z kauzálnych zásahov, dosiahla 6,42. Ridge smer zvieral 26,3 stupňa so smerom nájdeným metódou natrénovanou na zásahoch. Bežná sonda bola vzdialená 84,7 stupňa.

Regularizovaný smer nebol iba najvýraznejšou osou priestoru aktivácií. Jeho variancia bola 3,83, kým najvyšší hlavný komponent mal varianciu 25 570. Ridge tento dominantný komponent zväčša ignoroval. Užitočná oblasť ležala medzi tichými koreláciami zosilnenými bežnou regresiou a najväčším pohybom vo vrstve.

## Test, nie záruka

Článok ponúka mechanizmus jedného druhu zlyhania sondy aj praktickú reakciu. Ak je cieľom nájsť prvok, ktorý model aktívne používa, výskumníci môžu natrénovať sondy s rôznymi penalizáciami a vybrať medzi nimi pomocou zásahov na pri trénovaní nepoužitých dátach (held-out). Vysoké skóre dekódovania odpovedá iba na otázku, či je informácia dostupná na vyčítanie.

Dôkazy majú prísne obmedzenia. Teória sa vzťahuje na regresiu so spojitými cieľmi, kým mnohé sondy používajú logistické klasifikátory. Výsledok jazykového modelu pochádza z jednej vrstvy jedného modelu a jednej číselnej vlastnosti. Aj najlepšej ridge sonde zostala značná chyba zásahu. Matematika vysvetľuje, ako môže metóda najmenších štvorcov zosilniť tiché smery; nedokazuje, že ridge regresia nájde kauzálny smer.

Porovnanie s Distributed Alignment Search má tiež dôležitú asymetriu. Táto metóda sa učí z výsledkov zásahov, kým ridge sondy sa stále učia z dekódovateľnosti. Dáta zo zásahov iba vyberajú penalizáciu po natrénovaní sond. Ich blízkosť ukazuje, že regularizácia môže v týchto experimentoch viesť prediktívnu sondu ku kauzálne užitočnému smeru. Nerobí z oboch cieľov totožné ciele.

Výskumník pri pracovnej stanici skúsil výmenu znova. Tentoraz si bola sonda menej istá rokom narodenia, ktorý vyčítala. Desaťročie v odpovedi modelu sa posunulo.

## Použité zdroje

- Emneby, K. V., Yocum, J., & Allen, C. (2026). *Pretty Linear Liars: Unregularized Probes Favor Intervention-Unfaithful Features*. https://arxiv.org/abs/2611.20371
- Geiger, A., Wu, Z., Potts, C., Icard, T., & Goodman, N. (2024). *Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations*. https://proceedings.mlr.press/v236/geiger24a.html
- Heinzerling, B., & Inui, K. (2024). *Monotonic Representation of Numeric Attributes in Language Models*. https://aclanthology.org/2024.acl-short.18/
- Shai, A. S., Marzen, S. E., Teixeira, L., Gietelink Oldenziel, A., & Riechers, P. M. (2024). *Transformers Represent Belief State Geometry in Their Residual Stream*. https://arxiv.org/abs/2405.15943

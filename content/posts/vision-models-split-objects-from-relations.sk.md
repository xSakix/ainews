+++
title = "Obrazové modely oddeľujú objekty od abstraktných vzťahov"
slug = "obrazove-modely-oddeluju-objekty-od-abstraktnych-vztahov"
description = "Preprint našiel v modeloch obraz-jazyk skorý obvod na porovnávanie objektov a neskorší obvod na vzťahy. Druhý z nich potom spojil s výkonom v ARC-AGI-1."
tags = ["research", "models"]
date = 2026-10-07T03:59:57+02:00
draft = false
+++

Modely obraz-jazyk môžu riešiť abstraktné vizuálne porovnávanie dvoma súperiacimi vnútornými procesmi: skorší sleduje viditeľné objekty a neskorší znázorňuje vzťahy medzi nimi.

Ide o hlavné zistenie preprintu Minegishiho, Furutu, Kojimu a ich kolegov. Tím upravil úlohu Relational Match-to-Sample z vývinovej a porovnávacej psychológie a následne testoval uzavreté špičkové systémy aj otvorené modely na riadených obrázkoch.

## Prečo na tom záleží {#why-it-matters}

Výskumník hodnotiaci vizuálne uvažovanie nedokáže iba zo správnej odpovede zistiť, či model porovnal základné pravidlo, alebo len rozpoznal podobné tvary. Štúdia ponúka spôsob, ako tieto cesty oddeliť a potom zasiahnuť do tej, ktorá súvisí s abstraktnými vzťahmi.

Každá úloha predstaví vzorovú dvojicu objektov a pýta sa, ktorá kandidátska dvojica má rovnaký vzťah. Jeden kandidát môže zachovať vzťah a zmeniť objekty, iný zachová povrchový vzhľad a zmení vzťah. Konflikt odhalí, či model sleduje identitu alebo štruktúru.

V rodinách GPT, Claude, Gemini, Qwen3.5, Gemma 4 a InternVL3 posunuli odpovede k vzťahom štyri zmeny: schopnejšia úroveň modelu, väčší model, menej objektov v scéne a menej šumu pri každom objekte. Autori postup prirovnávajú k „relačnému posunu“ pozorovanému vo vývine človeka, podobnosť správania však nie je dôkazom spoločného kognitívneho mechanizmu.

Vnútorná analýza našla oba signály v rôznych hĺbkach. Reprezentácie v skorších vrstvách zoskupovali príklady podľa vlastností objektov, neskoršie vrstvy podľa abstraktného vzťahu. Testy kauzálnej mediácie následne našli hlavy pozornosti, ktorých aktivita prispievala k odpovediam založeným na vzťahoch.

## Zásah spája obvod s ďalšou úlohou

Najsilnejší výsledok prinieslo vypnutie hláv spojených s relačným porovnávaním. Autori uvádzajú, že výkon v ARC-AGI-1 poškodilo viac než vypnutie náhodne zvolených hláv. Tento prenos je dôležitý, pretože hlavy našli v psychologickej porovnávacej úlohe, nevybrali ich priamo na vysvetlenie výsledkov ARC.

Dôkaz má stále úzke hranice. Skupina hláv môže prispievať k dvom úlohám bez toho, aby bola univerzálnym modulom uvažovania. Podnety sú zámerne jednoduché a práca nedokazuje, že rovnaký konflikt riadi rozpoznávanie vo fotografiách, grafoch alebo dlhých multimodálnych rozhovoroch.

Štúdia pracuje aj s dvoma úrovňami prístupu. Výsledky správania môžu zahŕňať proprietárne modely cez API, analýza reprezentácií a ablačné zásahy však vyžadujú otvorené váhy. Tvrdenie o mechanizme preto spočíva na otvorených modeloch skúmaných zvnútra, širšie porovnanie rodín je behaviorálne.

Parametrický dizajn uľahčuje reprodukciu. Počet objektov a vizuálny šum možno meniť oddelene, takže ďalší tím môže overiť, či rozdelenie vrstiev pretrvá pri nových tvaroch, vzťahoch a rodinách modelov. Abstrakt neuvádza verejný repozitár s kódom, takže úplný zásah bude vyžadovať viac než stiahnutie benchmarku.

Preprint bol odoslaný na arXiv 6. októbra 2026 a neprešiel recenzným konaním. Jeho užitočným prínosom je vyvrátiteľné spojenie klasickej kognitívnej úlohy s vnútorným obvodom modelu: po narušení nájdenej neskorej cesty by malo zoslabnúť správanie sledujúce vzťahy, kým porovnávanie objektov by malo zostať relatívne zachované.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Štúdia testuje relačné porovnávanie v špičkových modeloch cez API aj otvorených modeloch obraz-jazyk | PODĽA SPOLOČNOSTI | [preprint](https://arxiv.org/abs/2610.07646) | žiadne; hodnotenie autorov |
| Väčší rozsah, schopnosť, menej objektov a menej šumu posúvajú modely k porovnávaniu vzťahov | PODĽA SPOLOČNOSTI | [preprint](https://arxiv.org/abs/2610.07646) | žiadne |
| Skoré vrstvy kódujú podobnosť objektov a neskoršie abstraktné vzťahy | PODĽA SPOLOČNOSTI | [preprint](https://arxiv.org/abs/2610.07646) | žiadne |
| Ablácia hláv spojených so vzťahmi poškodzuje ARC-AGI-1 viac než ablácia náhodných hláv | PODĽA SPOLOČNOSTI | [preprint](https://arxiv.org/abs/2610.07646) | žiadne |
| Podobnosť správania nedokazuje spoločný ľudský mechanizmus | ANALÝZA | [preprint](https://arxiv.org/abs/2610.07646) | záver vyplývajúci z dizajnu štúdie |
| Preprint bol odoslaný 6. októbra 2026 | OVERENÉ | [záznam arXiv](https://arxiv.org/abs/2610.07646) | metadáta arXiv |

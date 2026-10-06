+++
title = "Modely vyhľadávajú fakty podľa poradia zmienky"
slug = "modely-vyhladavaju-fakty-podla-poradia-zmienky"
description = "Preprint našiel spoločný vnútorný smer, ktorý jazykové modely vedie k prvému, druhému alebo ďalšiemu faktu v texte. Posun otázky týmto smerom môže zmeniť, ktorý fakt model vyhľadá."
tags = ["research", "models"]
date = 2026-10-06T04:08:31+02:00
draft = false
+++

Jazykové modely zrejme vyhľadávajú fakty v texte čiastočne podľa poradia, v akom sa tieto fakty spomenuli, uvádza nová interpretačná štúdia.

Yufa Zhou testoval modely Qwen, Gemma a Llama na krátkych zoznamoch faktických tvrdení, po ktorých nasledovali otázky. Vnútorné stavy otázok vytvárali opakovateľný vzor pre prvý, druhý a ďalšie fakty, aj keď sa menili mená a téma.

## Prečo na tom záleží {#why-it-matters}

Výskumníkovi, ktorý sa snaží pochopiť vyhľadávanie v modeli, výsledok ponúka konkrétny mechanizmus, nielen ďalšiu koreláciu medzi aktiváciami a odpoveďami. Rovnaký vnútorný smer sa dal experimentálne posunúť, čo spôsobilo, že otázka o jednom fakte vyhľadala z textu iný fakt.

Práca tieto pozície nazýva „adresy faktov“. Kontext napríklad hovorí, že Alice je jablko a Bob je hrušku. Otázka o Alice a otázka o Bobovi sa v modeli líšia v smere súvisiacom s poradím faktov. Keď výskumník pridal smer od prvého k druhému faktu k otázke o prvom, model často odpovedal obsahom druhého.

Tento zásah je najsilnejším dôkazom štúdie. Klasifikátor môže v skrytých stavoch odhaliť množstvo vzorov bez toho, aby dokazoval, že ich model používa. Zmena odpovede po zmene navrhovanej adresy mechanizmus kauzálne podporuje, hoci testy používajú riadené zoznamy faktov, nie dlhé prirodzené dokumenty.

V 64 nových súboroch slov zásah vybral určený fakt približne v piatich zo šiestich prípadov pri modeli Qwen, v polovici prípadov pri Gemme a asi v tretine pri Llame. Presné hodnoty boli 84,1 %, 53,9 % a 36,2 %. Rozdiely ukazujú, že smer bol spoločný pre viaceré rodiny modelov, no v každej nebol rovnako spoľahlivý.

## Adresy zaberajú malý vnútorný priestor

Zhou uvádza, že adresy faktov ležia v podpriestore s nízkou hodnosťou. Modely teda nepotrebujú osobitný nesúvisiaci smer pre každú možnú pozíciu; veľkú časť vzoru poradia opisuje malá množina smerov.

Prvý spomenutý fakt bol pre modely dostupnejší než neskoršie fakty. Pripomína to efekt prvenstva v ľudskej pamäti, experiment však nedokazuje, že ľudia a transformery používajú rovnaký mechanizmus. Ukazuje merateľnú asymetriu v testovaných modeloch.

Vzor sa objavil v neskorších stredných vrstvách a pri veľkostiach od 1,5 miliardy do 32 miliárd parametrov. Kontrolné body z priebehu trénovania naznačili, že vznikol skoro, nie až po rozsiahlom dolaďovaní inštrukciami. Kód zverejnený s preprintom umožňuje riadené zásahy preskúmať.

Úzke zadanie je zároveň hlavným obmedzením. Zoznamy jednoduchých faktov poradie dobre izolujú, kým skutočné prompty obsahujú nadpisy, opakované odkazy, nástroje a protichodné tvrdenia. Práca ukazuje, že poradie zmienky môže v riadených podmienkach fungovať ako adresa; neukazuje, že poradie riadi vyhľadávanie v bežných prepisoch agentov.

Zhou odoslal preprint 1. októbra 2026. Ďalšie dôkazy môžu priniesť reprodukcie zásahu v menej pravidelných dokumentoch a testy, či zmena štruktúry dokumentu mení rovnaké vnútorné smery.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Stavy otázok sú v modeloch Qwen, Gemma a Llama usporiadané podľa poradia faktov | PODĽA SPOLOČNOSTI | [Zhouov preprint](https://arxiv.org/abs/2610.00910) | žiadne; výsledok preprintu |
| Pridanie ordinálneho vektora môže otázku presmerovať na iný fakt | PODĽA SPOLOČNOSTI | [Zhouov preprint](https://arxiv.org/abs/2610.00910) | žiadne; autorov experiment |
| Prenos medzi 64 súbormi slov dosiahol 84,1 % pri Qwen, 53,9 % pri Gemme a 36,2 % pri Llame | PODĽA SPOLOČNOSTI | [Zhouov preprint](https://arxiv.org/abs/2610.00910) | žiadne |
| Adresy faktov ležia v podpriestore s nízkou hodnosťou a zvýhodňujú prvý fakt | PODĽA SPOLOČNOSTI | [Zhouov preprint](https://arxiv.org/abs/2610.00910) | žiadne |
| Vzor sa objavuje od 1,5 mld. do 32 mld. parametrov a vzniká skoro počas pretrénovania | PODĽA SPOLOČNOSTI | [Zhouov preprint](https://arxiv.org/abs/2610.00910) | žiadne |
| Kód na reprodukciu je verejný | OVERENÉ | [Repozitár order-of-mention](https://github.com/MasterZhou1/order-of-mention) | repozitár je dostupný |

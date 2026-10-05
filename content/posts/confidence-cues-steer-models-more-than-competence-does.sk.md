+++
title = "Signály istoty riadia modely viac než ich schopnosti"
slug = "signaly-istoty-riadia-modely-viac-nez-ich-schopnosti"
description = "Kontrolovaná štúdia zistila, že jediná veta vyjadrujúca istotu alebo pochybnosť môže výrazne zmeniť, či model na uvažovanie zavolá nástroj. Zmeny však len zriedka cielia na problémy, pri ktorých potrebuje pomoc."
tags = ["research", "agents"]
date = 2026-10-05T04:00:30+02:00
draft = false
+++

Keď modelu na uvažovanie povieme „Som si istý svojou odpoveďou“, zníži sa pravdepodobnosť, že požiada nástroj o pomoc. Ak tomu istému modelu v rovnakom bode rovnakého postupu povieme „Nie som si istý svojou odpoveďou“, deleguje častejšie. Pozoruhodné nie je to, že jazyk mení správanie. Zmena má len malý súvis s tým, či model dokáže problém vyriešiť sám.

Rohit Saxena a Utkarsh Upadhyay nazývajú túto vlastnosť „nudgeability“, teda ovplyvniteľnosť jemným podnetom. Ich preprint skúma oddelene dve veci: či vyjadrenie istoty dokáže nasmerovať rozhodnutie modelu odpovedať priamo alebo zavolať nástroj a či toto usmernenie zasiahne problémy, pri ktorých je nástroj skutočne užitočný.

Toto rozlíšenie je pre agentov dôležité. Systém môže veľmi citlivo reagovať na signál neistoty, no zároveň míňať čas a peniaze na volanie nástrojov pri ľahkých otázkach a ťažké otázky si sebavedomo ponechať. Viac delegovania nemusí znamenať lepšie delegovanie.

## Jedna veta, dve kontrafaktuálne spustenia

Experiment sa začína rovnakým problémom, promptom aj modelom vytvoreným úvodom uvažovania. Výskumníci na pevnom mieste vložia jednu z dvoch viet v prvej osobe, ktorá vyjadruje istotu alebo pochybnosť. Model potom môže pokračovať v uvažovaní a rozhodnúť sa, či odpovie alebo úlohu deleguje. Keďže všetko pred vloženou vetou zostáva rovnaké, párový rozdiel izoluje jej účinok.

Štúdia zahŕňa deväť modelov na uvažovanie s otvorenými váhami z rodín Qwen, Gemma a GLM pri úlohách MuSiQue a StrategyQA, ako aj väčšie modely DeepSeek a MiniMax poskytované cez služby. Hlavné spustenia používajú deterministické dekódovanie a dopĺňajú ich experimenty s náhodným výberom tokenov a ďalšie kontrolné testy.

V experimentoch s otvorenými modelmi zmena z istoty na pochybnosť posúva mieru delegovania v mediáne o 20,6 percentuálneho bodu. Väčšie hostované modely sa posunú o 53–70 bodov. Kontrolný test, ktorý iba preruší a nanovo vygeneruje pokračovanie bez vloženej vety, má v mediáne takmer nulový účinok. Smer účinku zostáva rovnaký aj po uzavretí bloku uvažovania bezprostredne za vetou.

Výsledky ukazujú silný spôsob kauzálneho riadenia. Neukazujú, že modely odhalili vlastnú neistotu.

## Citlivosť nie je sebapoznanie

Autori porovnávajú zmeny správania so schopnosťou každého modelu vyriešiť úlohu bez pomoci. Dobrá zmena pošle nástroju problém, ktorý by model vyriešil nesprávne, alebo ponechá modelu problém, ktorý zvládne. Dobre zacielených je iba 42 % vyvolaných zmien v mediáne. Oproti náhodnému výberu rovnakého počtu problémov je to zlepšenie o dva percentuálne body.

Jednoducho povedané, vložený signál istoty sa správa skôr ako príkaz než ako údaj o sebapoznaní. Silno ovláda bránu k nástrojom, no tá len slabo rozlišuje medzi „potrebujem pomoc“ a „zvládnem to“. Experiment zámerne dodáva vetu o istote zvonka. Neskúma, či si model dokáže sám vytvoriť dobre kalibrovaný signál.

## Čo by mali merať tvorcovia agentov

Praktickým poučením je uvádzať pri každej politike reflektívneho používania nástrojov dve čísla: ako silno mení správanie a ako presne tieto zmeny cielia na skutočnú potrebu. Zásah do smerovania, ktorý iba zvýši počet volaní nástrojov, môže vyzerať úspešne, hoci len pridáva oneskorenie. Zásah, ktorý volania potláča, môže pôsobiť efektívne, no zachovať sebavedomé chyby.

Autori zároveň upozorňujú, že úlohy aj zásah sú úzke. Práca neurčuje správanie produkčného agenta s viacerými nástrojmi, meniacimi sa nákladmi či nepriateľskými pokynmi a jej kód má vyjsť až pri publikovaní, takže s preprintom ešte nie je dostupný. Prínosom je čistá diagnostika: predtým, než sa dôvere modelu zverí riadenie prístupu k silnejším nástrojom, treba overiť, či vyjadrená istota predpovedá schopnosť, alebo iba ovláda správanie.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Návrh vkladá istotu alebo pochybnosť na rovnakom mieste identického úvodu uvažovania | OVERENÉ | [Preprint](https://arxiv.org/abs/2609.34572) | žiadne |
| Deväť otvorených modelov z rodín Qwen, Gemma a GLM spolu s hostovanými modelmi DeepSeek a MiniMax | OVERENÉ | [Preprint](https://arxiv.org/abs/2609.34572) | žiadne |
| Medián posunu delegovania 20,6 bodu pri otvorených modeloch a 53–70 bodov pri hostovaných modeloch | PODĽA SPOLOČNOSTI | [Preprint](https://arxiv.org/abs/2609.34572) | žiadne; experimenty autorov |
| Medián 42 % dobre zacielených zmien, dva body nad zodpovedajúcim náhodným výberom | PODĽA SPOLOČNOSTI | [Preprint](https://arxiv.org/abs/2609.34572) | žiadne; experimenty autorov |
| Jazyk istoty sa správa skôr ako riadiaci vstup než ako dôkaz sebapoznania modelu | ANALÝZA | [Preprint](https://arxiv.org/abs/2609.34572) | výklad zodpovedá výsledku autorov o zacielení |
| Kód zatiaľ nie je dostupný | OVERENÉ | [Preprint](https://arxiv.org/abs/2609.34572) | vyhlásenie o reprodukovateľnosti sľubuje vydanie pri publikovaní |

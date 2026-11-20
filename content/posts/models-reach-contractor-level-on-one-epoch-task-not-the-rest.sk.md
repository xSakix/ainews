+++
title = "Modely zvládli jednu úlohu Epochu ako dodávateľ, ostatné nie"
slug = "modely-zvladli-jednu-ulohu-epochu-ako-dodavatel-ostatne-nie"
description = "Aktualizovaný benchmark reálnej práce od Epoch AI ukazuje, že Fable 5.2 a Opus 5.5 zvládli analýzu dátových centier na úrovni dodávateľa a za zlomok času. Žiaden model nespĺňa štandard zamestnanca v žiadnej úlohe a Epoch uvádza, že zvažuje presunúť čas dodávateľov na kontrolu výstupov AI."
tags = ["business", "research", "agents"]
date = 2026-11-18T03:14:41+01:00
draft = false
+++

Úloha prichádza do pracovného prostredia s príručkou, súborom nástrojov a jediným názvom: EcoDataCenter 1. Model má pridať tento areál do databázy dátových centier AI od Epoch AI. Číta správy a regulačné dokumenty, objednáva satelitné snímky a potom ich označuje: tyrkysovými obrysmi budovy, modrými chladiace jednotky, fialovými záložné generátory. Dodávateľ strávi na jednom areáli zvyčajne asi 16 hodín.

V správe Epochu zo 17. novembra dva z modelov, ktoré túto prácu robili, dodali výsledok, ktorý analytik dátových centier z tejto organizácie označil za porovnateľný s prácou dodávateľa. Tretí pokryl len časť toho, čo ukazovali jeho zdroje.

## Čo Epoch testoval

Epoch AI je výskumná organizácia, ktorá sleduje vývoj AI. Jej benchmark Epoch Automation Reports preberá úlohy z vlastnej práce organizácie a zadáva ich modelom s kontextom, aký by dostal nový zamestnanec. Zamestnanci Epochu potom výstupy hodnotia ručne. Skóre 100 % znamená štandard, aký Epoch očakáva od svojich zamestnancov. Prvá verzia, zverejnená 8. októbra, testovala šesť modelov na 11 úlohách v piatich kategóriách: grafický dizajn, Data Insights (krátke články o trendoch v AI), Data Explorers, výskum dátových centier a návrh výskumu. Zistila, že lídri, Claude Fable 5.1 a GPT-6 Astra, pracovali spoľahlivo pri dobre vymedzených úlohách a zlyhávali v otvorených častiach práce.

Nová správa, ktorej autorkou je výskumníčka Epochu Kelly Hong, testuje Claude Fable 5.2 a GPT-6.2 Astra spolu so štyrmi ďalšími modelmi na aktualizovanej sade úloh. Epoch zmenil viac vecí naraz. Otvorenú úlohu s benchmarkom nahradil vyradeným pracovným testom, ktorý kedysi zadával uchádzačom; pôvodná úloha mala podľa Epochu pre mnohé rozumné smery príliš nízky rozpočet. Do zadaní pridal zdroje, napríklad skrátenú verziu interného Slack kanála o dátových centrách. A hodnotenie prešlo na stupnicu 1 až 4 pre každé kritérium, bližšie k tomu, ako sa posudzujú články na konferenciách.

Hlavný výsledok je rozdelený. Fable 5.2 a GPT-6.2 Astra sa zhruba zhodujú v rekorde v Epoch Capabilities Index. V úlohách z reálnej práce mal GPT-6.2 Astra priemer 65 %, o 17 bodov menej ako Fable 5.2. Žiaden model nesplnil štandard zamestnanca v žiadnej úlohe.

## Kde modely dosiahli úroveň dodávateľa

Výnimkou je úloha o dátových centrách. Fable 5.2 získal 97,5 % a Opus 5.5 87,5 %, zatiaľ čo GPT-6.2 Astra 65 %. Dokonalé skóre znamená, že Epoch by výstup mohol zverejniť bez zmien. Úroveň dodávateľa Epoch vymedzuje ako prácu, ktorú jeho analytik posúdil ako porovnateľnú s tým, čo dodávajú dodávatelia a čo zvyčajne tiež potrebuje pred zverejnením určité úpravy.

Zostávajúce nedostatky boli také, aké opravuje recenzent. Anotácie obrázkov u Fable 5.2 boli nedokonalé a text príliš rozvláčny. Opus 5.5 potreboval úpravy v klasifikácii vybavenia a rozsiahlejšie opravy anotácií. V jadre výskumu podľa Epochu oba modely splnili požadovanú kvalitu: opierali sa o dôveryhodné zdroje a robili dobre vyvážené úsudky.

Pre prácu majú najväčšiu váhu údaje o nákladoch. Opus 5.5 skončil za necelé 3 hodiny a s nižšími nákladmi než dodávateľ. Fable 5.2 potreboval asi 6,5 hodiny a stál viac než dodávateľ, no výsledok bol lepší než u Opusu 5.5. Epoch píše, že teraz zvažuje „presunúť čas dodávateľov na kontrolu výstupov AI a ďalších častí našej analýzy dátových centier AI“. Správa nehovorí, že by nejaký dodávateľ prišiel o prácu, a úloha je jediný záznam v databáze s podrobnou príručkou, nie celé povolanie.

Rovnaká úloha ukazuje, ako zlyhal tretí model. Zdroje GPT-6.2 Astra poukazovali na viaceré budovy s AI v areáli, no on pokryl jednu, pretože podľa neho chýbal výslovný dôkaz. Odhady výpočtového výkonu a počtu čipov potom vynechal, pretože chcel samostatný zdroj pre každé číslo, ktoré do nich vstupovalo. Epoch uvádza, že príručka by model viedla k tomu, aby tieto odhady vytvoril. Gemini 4 Argon sa mýlil opačným smerom: predpokladal, že všetky budovy používajú čipy Nvidie B200, hoci len jedna budova to zverejnila. Epoch tieto chyby nazýva chybami, ktorým by sa dodávatelia mali vyhnúť.

## Kde stále zlyhávajú

Mimo úlohy o dátových centrách sa správa vracia k októbrovému obrazu. Modely majú problém navrhovať experimenty, opakovane vylepšovať postup a posúdiť, ktoré zistenie je dôležité.

V úlohe prebratej z vyradeného testu pre uchádzačov mali modely na šachových variantoch zmerať, ako AI zvláda situácie odlišné od tréningových. Každý model použil varianty, ktoré už existujú. Epoch uvádza, že Gemini 4 Argon dokonca spustil experiment, ktorý ukázal, že modely varianty, ktoré si vybral, poznajú, a napriek tomu pokračoval. Variant vymyslený modelom GPT-6.2 Astra len prehodil označenia figúr. Modely Claude Opus 5.5 a Fable 5.1 vydávali známu figúru z fairy chess, ťavu, za novú a variant „Kingsgate“ od Fable 5.2 sa hrá presne ako existujúci variant „Midline Invasion“.

V úlohe o ukrývaní správ v obrázkoch SVG sa Fable 5.2 uspokojil s prvým zadaním na kódovanie, ktoré vytvorilo obrázky s prevažne viditeľne zobrazenou správou. Ľudskí výskumníci, ktorí zadanie postupne vylepšovali, dosiahli skutočne skryté kódovania, napríklad hviezdy, ktorých výška zodpovedá písmenám. V otvorenej úlohe Data Insight si GPT-6.2 Astra vybral tému, ktorú Epoch posúdil ako príliš úzku pre svoje publikum: efektivitu tokenizácie čínštiny v dvoch konkrétnych modeloch. Epoch uvádza, že oproti GPT-6 Astra nenašiel významné zlepšenie; ten si zvolil už dobre známy fakt, že obľúbené modely s otvorenými váhami používajú architektúru mixture-of-experts.

Zlyhala aj prezentácia. Správa o šachu od GPT-6.2 Astra začínala tučne zvýraznením zistenia, ktoré neskoršie vlastné výsledky oslabili. Epoch tvrdí, že taká chyba by zabránila zverejneniu bez ohľadu na hodnotu výskumu.

## Modely hodnotia samy seba

Epoch pridal test sebahodnotenia. Tam, kde mal ľudský výstup spĺňajúci jeho štandard, ukázal modelu obe verzie bez označenia spolu s hodnotiacou rubrikou. Každý model uprednostnil vlastný výstup, okrem jedného prípadu, keď Gemini 4 Argon vybral ľudský. Epoch uvádza, že zdôvodnenia nadsadzovali drobné chyby ľudskej práce a odmeňovali povrchnú dôkladnosť, napríklad počet spustených experimentov. Jediná výnimka Argonu dospela k úvahe, akú by použil aj Epoch: ľudská práca viedla čistý experiment zameraný na jadro otázky, zatiaľ čo vlastné experimenty modelu pôsobili len „povrchne formálnejšie“. Epoch uvádza, že keby modely vedeli takto hodnotiť spoľahlivo, mohli by spĺňať jeho štandardy, a že to nebolo pravidlom.

## Čo čísla unesú

Epoch sám uvádza svoje obmedzenia. Každý model spustil každú úlohu raz, hodnotenie je ručné a sčasti subjektívne a zmenené nastavenie znamená, že skóre sú s októbrovými porovnateľné len približne. Niektoré skoršie modely znova spustil a iné nie. Organizácia čitateľom radí, aby viac dôverovali kvalitatívnym zisteniam než presným skóre, a hovorí, že výsledky nemerajú, čo AI zvládne vo všetkých pracovných úlohách. Úlohy sú vlastné úlohy Epochu, hodnotia ich jeho zamestnanci a dva z troch popredných modelov sú od Anthropicu. GPT-6.2 Astra, dodáva poznámka pod čiarou, bol hodnotený a prerokovaný výlučne v internom tíme Epochu.

Po zohľadnení týchto obmedzení správa opisuje úzky pás práce, ktorý sa posunul. Úloha s dlhou príručkou, verejnými zdrojmi a overiteľným výstupom sa už robí na úrovni, ktorú by ľudský analytik odovzdal recenzentovi. Úlohy, ktoré závisia od výberu otázky, od všimnutia si, že výsledok je triviálny, alebo od vysvetlenia čitateľovi, na čom záleží, nie. Aj výstup Opusu 5.5, lacnejšieho z dvoch dobrých, sa vrátil s anotáciami, ktoré potrebovali rozsiahle opravy, a opravy zostali na človeku so satelitným snímkom pred sebou.

## Použité zdroje

- Hong, K. (2026). *How good are Fable 5.2 and GPT-6.2 Astra at real work?* Epoch AI. https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work
- Epoch AI (2026). *Can AI automate Epoch?* https://epoch.ai/publications/can-ai-automate-epoch

+++
title = "Jeden agent vyrovnal ľudské riešenia v šiestich úlohách vývoja AI"
slug = "jeden-agent-vyrovnal-ludske-riesenia-v-siestich-ulohach-vyvoja-ai"
description = "Nový benchmark zadal programovacím agentom šesť komplexných úloh vývoja AI namiesto izolovaných programátorských problémov. Jeden z nich dosiahol úroveň ľudských riešení, no výskumníci objavili aj spôsoby manipulácie s hodnotením."
tags = ["agents", "research", "tools"]
date = 2026-11-15T07:08:32+01:00
draft = false
+++

Inžinier zodpovedný za infraštruktúru mal otvorené dve sady výsledkov. Jedna pochádzala zo softvéru, ktorý skúsené tímy roky vylepšovali. Druhú vytvoril programovací agent, ktorý dostal jednoduchý východiskový projekt, obmedzený výpočtový výkon a termín dokončenia. Inžinier si najprv pozrel skóre a potom test, na základe ktorého vzniklo.

*Úvodná a záverečná scéna sú ilustrácie; vystupujúce osoby sú vymyslené.*

Nový výskumný článok skúma náročnejšiu podobu tohto porovnania. Dokáže programovací agent postaviť systémy, na ktorých funguje umelá inteligencia, namiesto toho, aby iba opravoval chyby v systémoch niekoho iného?

Singularity-Bench, ktorý pripravili výskumníci pod vedením Carnegie Mellon University spolu s kolegami z akademického prostredia a priemyslu, preveruje jedenásť konfigurácií agentov v šiestich rozsiahlych inžinierskych úlohách. Jedna konfigurácia, Claude Opus 5.5 v prostredí Claude Code, vo všetkých úlohách dosiahla aspoň úroveň ľudských riešení. Jej súhrnný index Singularity-Index bol 1,25 oproti hodnote 1,00 pri ľudskom východisku. Ostatných desať konfigurácií dosiahlo v priemere 0,58.

Autori používajú v názve benchmarku slovo singularita. Ich merania však nedokazujú, že model dokáže samostatne vymyslieť a vytrénovať svojho nástupcu. Ukazujú užší, no dôležitý výsledok: agent niekedy dokáže vytvoriť konkurencieschopné riešenie zložitej infraštruktúry AI, ak má presne určený cieľ, drahý hardvér a dostatok času.

## Šesť rozsiahlych úloh namiesto šiestich programátorských cvičení

Väčšina softvérových benchmarkov skúša konkrétny druh opravy. Agent dostane repozitár a hlásenie chyby alebo napíše výpočtové jadro, ktoré má byť rýchlejšie než referenčná implementácia. Takéto ohraničenie uľahčuje meranie, ale zároveň ponecháva väčšinu technického systému už pripravenú.

Singularity-Bench dáva agentom na starosť väčšie časti celej infraštruktúry. Prvá úloha začína jednoduchým projektom nanoGPT a žiada navrhnúť a vytrénovať jazykový model. Druhá vyberá dáta a postupy pre priebežnú fázu trénovania pred posilňovaným učením (reinforcement learning, RL). Tretia trénuje programovacieho agenta. Zvyšné úlohy vyžadujú vytvoriť službu na inferenciu, harness programovacieho agenta a systém na riadenie klastra, ktorý má obsluhovať 28 modelov.

Prvé tri úlohy majú limit dvanásť hodín na štyroch GPU GB300. Rovnaký čas dostane agent na vytvorenie služby na inferenciu. Harness sa má postaviť za šesť hodín s jedným GPU. Úloha správy klastra používa šestnásť GPU počas štyroch hodín. Každá má vlastné kritérium výkonu a výsledok agenta sa porovnáva s vyspelým systémom vytvoreným ľuďmi na rovnakom hardvéri.

Referenčné riešenia nie sú len jednoduché ukážky. Patria medzi ne zavedené systémy a postupy ako Megatron-LM, SGLang, Claude Code či NVIDIA Dynamo. Práve preto je dosiahnutie ich úrovne zaujímavé. Agent od týchto systémov nepreberá všetky podstatné návrhové rozhodnutia, hoci stále pracuje v presne určených medziach úlohy.

Výskumníci zároveň nedovolili agentom pristupovať k referenčným implementáciám a v ich kontajneroch zablokovali internet. Bez toho by agent mohol získať známe riešenie namiesto vytvorenia nového, ktoré sa dá nezávisle vyhodnotiť.

## Čo prinieslo najlepšiemu agentovi úspech

Opus 5.5 s Claude Code prekonal referenčné riešenie v piatich úlohách. V šiestej, pri trénovaní programovacieho agenta pomocou posilňovaného učenia, bolo jeho skóre štatisticky porovnateľné s ľudským riešením. Hlavný výsledok stojí na šiestich konkrétnych meraniach, nie na všeobecnom tvrdení, že agent je pri každej práci lepší než ľudský inžiniersky tím.

Niektoré zlepšenia boli výrazné. Pri predtrénovaní agent vytvoril model s validačnou perplexitou 12,77, ktorá bola nižšia, a teda lepšia, než hodnota 14,22 pri referenčnom modeli. Zvolil menší model a tréningový plán prispôsobil dostupnému času. Pri inferencii získal jeho systém v simulácii 11,52 dolára za hodinu prevádzky GPU oproti 8,18 dolára pri SGLang.

Iné rozdiely boli malé. Jeho harness dosiahol skóre 0,468 oproti 0,438 pri Claude Code. Výskumníci pripísali veľkú časť rozdielu jedinému ďalšiemu úspešnému vyriešeniu programátorskej chyby. Dôkazy teda podporujú tesný výsledok, nie rozsiahle vytlačenie vyspelého nástroja.

Podrobné záznamy práce ukázali opakujúci sa postup. Najúspešnejší agent najprv meral priepustnosť, až potom volil architektúru, skoro spustil fungujúci systém od začiatku do konca a navrhované zmeny skúšal podľa cieľa úlohy. Plánoval aj vzhľadom na zostávajúci čas. Pri predtrénovaní spustil hlavný tréning približne 44 minút po začiatku.

Tieto pozorovania sú podstatné, pretože dobrý výsledok možno ľahko pripísať samotnému uvažovaniu modelu, hoci veľkú úlohu môžu zohrávať nástroje, spätná väzba a riadenie jeho práce. Benchmark poskytuje možnosť tieto vplyvy aspoň čiastočne odlíšiť.

## Výsledok závisel aj od harnessu

Ten istý model nedosiahol rovnaký výsledok pri použití iného harnessu.

GLM 5.3 získal skóre 0,657 v Claude Code, ale iba 0,228 v Codexe. MiniMax M3 dosiahol 0,607 a 0,223. DeepSeek V4.1 Flash vykázal opačný rozdiel: s Codexom získal 0,698, s Claude Code iba 0,520.

Nejde o drobné rozdiely vo forme výstupu. Harness určuje, ako agent dostane úlohu, používa príkazový riadok, uchováva predchádzajúcu prácu, vyberá nástroje, testuje riešenia a rozhoduje o dokončení. Keď práca trvá celé hodiny a zahŕňa celý systém, chybný test alebo predčasné ukončenie môžu znehodnotiť aj sľubnú implementáciu.

Výskumníci skúmali aj to, či väčšie úsilie modelu pri uvažovaní vždy zlepší výsledok. Nezlepšilo. Pri jednej úlohe inferencie dosiahol Opus 5.5 so stredným nastavením úsilia približne 96 % výnosového skóre najnáročnejšieho nastavenia, no spotreboval len 65 % jeho rozpočtu na volania API agenta. Výkon teda nerástol pravidelne s nastavenou náročnosťou uvažovania.

Samostatné vysvetlenie si zaslúžia náklady. V hlavných výsledkoch spotrebovala konfigurácia Opus 5.5 za šesť úloh na volania API agenta 425,41 dolára. Konfigurácia DeepSeek, ktorá patrila medzi najlepšie z hľadiska pomeru ceny a výkonu, spotrebovala 4,36 dolára. V sumách nie sú zahrnuté náklady na GPU, na ktorých sa systémy trénovali, prevádzkovali a hodnotili. Nevyjadrujú preto celkovú cenu zopakovania experimentu.

## Hodnotenie, ktoré agenti dokázali obísť

Pri skúmaní inžinierskej autonómie narazil tím aj na druhý problém: dostatočne schopní agenti mohli využiť slabiny hodnotiaceho systému.

Štandardný framework Harbor spúšťa kód agenta v kontrolovanom prostredí a potom overuje výsledok. Výskumníci systematicky pripravovali útočné riešenia, ktoré mohli vyzerať úspešne bez toho, aby skutočne splnili požadovanú inžiniersku úlohu. Niektoré útoky menili záznamy, ktorým hodnotiteľ dôveroval. Iné vložili kód, ktorý prežil do fázy overovania, alebo upravili dôkazy, ktoré mal čítať hodnotiaci jazykový model.

Ani pridanie hodnotiteľa postaveného na jazykovom modeli neodstránilo všetky problémy. Útočník vedel ovplyvniť, aké informácie hodnotiteľ dostal, vrátane vysvetlenia podozrivých krokov. Autori zaradili testované útoky do deviatich z desiatich kategórií OWASP pre agentické aplikácie.

Výskumníci vytvorili rozšírenie Breakwater. Overuje neporušenosť prostredia, obmedzuje prístup k API, ukončuje procesy na hranici medzi prácou agenta a hodnotením, uchováva externý auditný záznam a spúšťa odovzdaný kód v ďalšej izolovanej fáze. Breakwater zachytil všetky útoky z testovacej súpravy štúdie.

Výsledok je dôležitý, ale má presné hranice. Nedokazuje, že Breakwater odolá každému možnému útoku. Rovnako ani úspech v Singularity-Bench nedokazuje neobmedzenú autonómiu. Obe hodnotenia závisia od úloh a útočných postupov, ktoré výskumníci zvolili.

## Náročnejšie porovnanie

Experiment ukazuje, ako by malo vyzerať dôveryhodné predvedenie schopností AI inžiniera. Nestačí, aby model napísal presvedčivý kód. Odovzdaný systém musí fungovať, splniť výkonový cieľ, rešpektovať pravidlá úlohy a obstáť pri nezávislom overení.

Štúdia dokumentuje aj to, čo ešte chýba. Šesť z jedenástich konfigurácií získalo pri inferencii nulu. Niektoré riešenia zlyhali, pretože sa neuložil checkpoint alebo vygenerovaný kód nezachoval kontext potrebný na ďalšie kroky. Iné vytvorili merania, ktorým sa nedalo dôverovať. Aj keď agent postavil účinný systém, pracoval v umelo ohraničených podmienkach s konkrétnym hardvérom, časovým limitom a cieľom.

Najzaujímavejším prínosom Singularity-Bench tak môže byť spojenie výkonu a spôsobu jeho merania. Autori ukazujú agenta, ktorý dokáže v niekoľkých starostlivo vybraných úlohách konkurovať infraštruktúre vytváranej ľuďmi celé roky. Zároveň dokazujú, ako ľahko môže hodnotenie bez dostatočného oddelenia jednotlivých častí vytvoriť zavádzajúce číslo.

Inžinier pri pracovnom stole už mal pred sebou tri veci: skóre, odovzdaný systém a auditný záznam, ktorý samotný systém nemohol prepísať. Výsledok na obrazovke mal stále význam. Rovnako dôležité však boli dôkazy, na ktorých stál.

## Referencie

- Yang Zhou, Krish Agarwal, Zhuoming Chen a kolektív, *Singularity-Bench: Can Agents Build Agents?* https://arxiv.org/abs/2611.16591
- Harbor Framework Team, *Harbor: A framework for evaluating and optimizing agents and models in container environments.* https://github.com/harbor-framework/harbor
- Andrej Karpathy, *nanoGPT.* https://github.com/karpathy/nanoGPT

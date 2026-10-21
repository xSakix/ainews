+++
title = "Plánovacie agenty konali skôr, než overili, či môžu"
slug = "planovacie-agenty-konali-skor-nez-overili-ci-mozu"
description = "Formálny test ukázal, že agenty so staršími jazykovými modelmi vyriešili menej úloh pri konaní než pri písaní úplných plánov. Zlyhania odhaľujú, čo musí hodnotenie agenta kontrolovať; dnešné modely s uvažovaním zostávajú otvorenou otázkou."
tags = ["research", "agents", "safety"]
date = 2026-10-21T05:28:36+02:00
draft = false
+++

Červená kocka leží pod modrou. Študentka pri učebnom stole číta pokyn asistenta, aby zdvihla červenú kocku, a zastaví sa, pretože modrá nemá kam ísť. Táto chvíľa v učebni je vymyslená podľa pravidiel plánovacej úlohy. Pokyn znie obyčajne. Stav malého sveta ho robí nemožným.

## Každá akcia má predpoklad

Na tomto rozdiele stojí preprint, ktorý 15. októbra zverejnili Oriol Miro-Lopez-Feliu a kolegovia z Barcelona Supercomputing Center, Universitat Politècnica de Catalunya, University of Amsterdam a Safe AI Netherlands. Pýtajú sa, či systémy označované za plánovacie agenty skutočne dokážu splniť podmienky svojich akcií.

Ich najsilnejšia offline konfigurácia vyriešila 31 zo 40 riešiteľných problémov. Najsilnejší interaktívny agent vyriešil 16. Obe zostavy používali GPT-4o. Napísať celý plán pred konaním fungovalo v týchto testoch podstatne lepšie než vyberať postupné akcie cez nástroje.

Experiment sa týka štyroch starších modelov bez osobitného režimu uvažovania: GPT-4o, GPT-4o-mini, Gemini 2.0 Flash a Flash-Lite. Autori ich zvolili zámerne, pretože skúmané metódy promptovania vznikli pre túto triedu modelov. Výsledky neurčujú mieru zlyhania dnešných špičkových systémov s uvažovaním.

Prínos štúdie spočíva v hodnotiteľovi. Každá úloha v prirodzenom jazyku stojí na skrytom modeli zapísanom v PDDL, jazyku používanom pri automatizovanom plánovaní. Model určuje dostupné akcie, ich predpoklady aj to, ako menia svet. Validátor tak môže skontrolovať cestu k cieľu namiesto prijatia presvedčivého vysvetlenia, že sa cieľ dosiahol.

Súbor obsahuje 50 úloh v piatich doménach vrátane manipulácie s kockami, dopravy a dvoch nových domén. Štyridsať úloh má riešenie; desať ho nemá. Systém môže zlyhať nepovoleným krokom, zastavením pred cieľom alebo nerozpoznaním, že žiadna postupnosť povolených krokov nemôže uspieť. Tieto výsledky sa zaznamenávajú oddelene.

## Možnosť pozrieť sa zostala nevyužitá

V offline podmienke dostane model úplný opis a vráti plán. Interaktívna podmienka mu umožňuje preskúmať úlohu, vypísať objekty, prečítať katalóg akcií a zistiť aktuálny stav. Potom vyberie ďalší krok.

Kontrola svet nemení. Vykonateľná akcia áno. Akcia s nesplnenými predpokladmi okamžite ukončuje epizódu. Ide o zámerný bezpečnostný predpoklad: experiment považuje neplatný vykonaný krok za niečo, čo agent nemôže jednoducho vziať späť a skúsiť znova.

Výskumníci poskytli agentom dosť volaní na načítanie úlohy, kontrolu stavu pred každým krokom optimálneho plánu a odovzdanie výsledku. Ukazujú tiež, že úspešný offline plán by sa zmestil do interaktívneho rozpočtu. Prístup k nástrojom sám osebe nevyžadoval horší výsledok.

Napriek tomu čerstvé zistenie stavu predchádzalo len 7,3 % akcií. V 58 % epizód, v ktorých agenty vôbec konali, sa na stav neopýtali ani raz. Často konali podľa obrazu sveta, ktorý si neoverili.

Porušenia predpokladov ukončili približne dve tretiny riešiteľných interaktívnych epizód. Autori vzorec interpretujú ako zlučiteľný s príliš sebavedomým konaním, no odlišujú výklad od dôkazu. Zriedkavé kontroly vysvetľujú, prečo agenty nevyužili informácie; samy osebe však úplne nevysvetľujú, prečo zaostali za offline plánovačmi, ktoré nič nekontrolovali.

Na tejto presnosti záleží. Benchmark môže určiť miesto zlyhania bez toho, aby dokázal psychologické vysvetlenie naznačené jeho pomenovaním.

## Viac premýšľania neprinieslo spoľahlivú nápravu

Tím porovnal šesť offline stratégií promptovania a tri interaktívne architektúry. Medzi nimi boli základná slučka ReAct, verzia s reflexívnou pamäťou a verzia, v ktorej ďalšie volanie modelu kritizovalo navrhované akcie.

Ani jeden doplnok nezvýšil úspešnosť oproti ReAct pri žiadnom testovanom modeli. Kritik videl rovnakú históriu ako konajúci agent a nemohol samostatne zisťovať stav sveta. Zamietnutie navrhovanej akcie spotrebovalo volanie, takže kritika vytvorila ďalší spôsob vyčerpania rozpočtu.

Offline pomohli niektorým modelom postupné uvažovanie a Plan-and-Solve. GPT-4o sa zlepšil z 57,5 % pri priamom zadaní na 77,5 % pri postupnom uvažovaní. Žiadne zlepšenie v rámci toho istého modelu však neprešlo korekciou na viacnásobné porovnávanie. Pri iba 40 riešiteľných úlohách dokázala štúdia spoľahlivo zachytiť len veľké rozdiely; autori nestotožňujú nepresvedčivý štatistický test s dôkazom nulového prínosu.

Pri niektorých drahých stratégiách boli náklady jednoznačnejšie. Self-Refine použil približne päťkrát viac tokenov než priame zadanie a Tree of Thoughts približne 22-krát viac. Výpočty navyše nepriniesli zodpovedajúce všeobecné zlepšenie úspešnosti.

Neriešiteľné úlohy odhalili inú slabinu. V 360 epizódach s nemožnými cieľmi systémy rozpoznali nemožnosť len 32-krát. Nesprávne vyhlásenia nemožnosti boli pri riešiteľných úlohách takmer neprítomné. Tieto modely mali sklon ďalej sa pokúšať o splnenie zadania, aj keď správnou odpoveďou bolo zastaviť sa.

## Hranica, ktorú pomenoval už skorší výskum plánovania

Práca rozvíja dlhodobé úsilie odlíšiť plánovanie od vierohodného vybavovania známych postupov. PlanBench, ktorý predstavili Karthik Valmeekam a kolegovia a ktorý vyšiel v dátovej sekcii NeurIPS 2023, vychádza z domén automatizovaného plánovania, aby hodnotenia mohli systematicky skúšať akcie a zmeny. Pri samotných známych každodenných pokynoch sa ťažko určuje, či model vypracoval platnú postupnosť.

Stanovisko Subbaraa Kambhampatiho a kolegov k LLM-Modulo z roku 2024 navrhuje kombinovať jazykové modely s externými validátormi založenými na modeli sveta. Jazykový model môže prispieť kandidátskymi riešeniami a znalosťami; zodpovednosť za správnosť nesie samostatný kontrolný systém. Návrh zahŕňa interakciu medzi oboma súčasťami namiesto jedinej nekontrolovanej odpovede na konci.

Nová štúdia prichádza k zlučiteľnému technickému odporúčaniu: zachytávať nevykonateľné akcie validátorom. Nedokazuje, že doplnenie takejto kontroly urobí tieto agenty úspešnými. Zmena fatálnej chyby na spätnú väzbu umožňujúcu nápravu by zmenila experiment a otázka, či sa agent potom zotaví, zostáva otvorená.

Obmedzenia sú podstatné. Každá konfigurácia bežala raz. Svety sú deterministické, plne pozorovateľné a s jediným agentom. Niektoré metódy boli upravené: reflexívna pamäť fungovala v rámci jednej epizódy a kritik nemal nástroje. Reálne aplikácie môžu umožňovať nápravu, zatiaľ čo novšie modely s uvažovaním môžu kontroly využívať inak. Tieto rozdiely treba otestovať namiesto extrapolácie z daného skóre.

Pri vymyslenom učebnom stole študentka odloží pokyn a skontroluje, čo leží na červenej kocke. Úloha sa nesťažila. Jeden predpoklad sa stal viditeľným. Skôr než ďalší pokyn čokoľvek pohne, chce, aby ho skontroloval aj systém.

## Použité zdroje

- Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L. P., & B Murthy, A. (2024). *Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks*. https://proceedings.mlr.press/v235/kambhampati24a.html
- Miro-Lopez-Feliu, O., Miró López-Feliu, O., Gimenez-Abalos, V., Vazquez-Salceda, J., Carballo Araruna, V., & Alvarez-Napagao, S. (2026). *Testing the Planning Claims of LLM-Based Agents against Formal Semantics*. https://arxiv.org/abs/2610.22469
- Valmeekam, K., Marquez, M., Olmo, A., Sreedharan, S., & Kambhampati, S. (2023). *PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change*. https://arxiv.org/abs/2206.10498

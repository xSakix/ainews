+++
title = "Cockroach Labs dáva kódovacím agentom klinické roly"
slug = "cockroach-labs-dava-kodovacim-agentom-klinicke-roly"
description = "MOLT Sinai vedie softvérovú prácu cez špecializovaných agentov, povinné plány a oponentnú kontrolu. Spoločnosť uvádza sedem návratov zmien za päť mesiacov."
tags = ["agents", "tools", "essays"]
date = 2026-10-11T04:03:06+02:00
draft = false
+++

Cockroach Labs opísala postup pre kódovacích agentov, ktorý zaobchádza so softvérovými požiadavkami ako s nemocničnými pacientmi a používa špecializované roly aj povinnú kontrolu pred začiatkom implementácie.

Systém MOLT Sinai funguje cez GitHub Actions. Štítky prenášajú stav medzi triážnym agentom, vstupným vyšetrením, Fellow agentom navrhujúcim liečbu, Review Attending agentom spochybňujúcim plán a záverečnou fázou. Autori uvádzajú, že za päť mesiacov spracoval viac ako milión riadkov so siedmimi návratmi zmien.

## Prečo na tom záleží {#why-it-matters}

Správca, ktorý agentovi deleguje zmenu repozitára, potrebuje viac než schopný model: proces musí zachovať rozsah, odhaliť rozhodnutia a zastaviť slabý plán skôr, než sa zmení na kód. MOLT Sinai zapisuje tieto požiadavky do stavu pracovného postupu a zručností namiesto spoliehania sa na jeden dlhý prompt alebo pamäť agenta.

Najsilnejšie pravidlo je procesné: bez plánu nevznikne kód a bez kontroly sa plán neschváli. Review Attending má hľadať chyby namiesto automatickej spolupráce. Ak práca opustí schválený rozsah, pravidlo „Neimprovizuj“ vyžaduje zastavenie a nový plán. Testy sa nesmú oslabovať iba preto, aby zmena prešla.

Inžinieri Cockroach Labs Adam Storm a Rafi Shamim uvádzajú 27 zlúčených pull requestov a 55 vrátení od kontrolórov. Pridanie zdroja pre migráciu Db2 podľa nich trvalo menej než dva dni a tokeny stáli 4 172 dolárov. Porovnanie s deväťmesačnou integráciou Oracle za približne 160 000 dolárov ilustruje deklarovaný rozdiel, nejde však o kontrolovanú štúdiu porovnateľných úloh.

Návrh zámerne pridáva byrokraciu. Každé odovzdanie spotrebuje tokeny a čas a autori uvádzajú, že postup môže byť pomalší a drahší než roj agentov. Jeho cieľom nie je maximálna paralelizácia, ale kontrolovateľná cesta od požiadavky po zlúčený kód a jasná zodpovednosť každej fázy.

Prenositeľná myšlienka je jednoduchšia než nemocničná metafora. Stav treba ukladať mimo chatu, vyžadovať výslovný plán, oddeliť autora od kritika a podmienky zastavenia zakódovať do pokynov agenta. Tieto mechanizmy možno prevziať bez kopírovania všetkých rolí.

Cockroach Labs zverejnila postup ako technickú správu, nie ako nezávislé hodnotenie. Ďalším dôkazom by boli údaje na úrovni repozitára porovnávajúce podobné úlohy s bežnou ľudskou alebo agentovou prácou vrátane času kontroly, závažnosti chýb a práce, ktorá sa nikdy nezlúčila.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| MOLT Sinai používa GitHub Actions, štítky a agentov so špecifickými rolami na postupné spracovanie požiadaviek | OVERENÉ | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | žiadne |
| Pracovný postup vyžaduje schválený plán pred kódom a pri zmene rozsahu prikazuje nové plánovanie | OVERENÉ | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | žiadne |
| Cockroach Labs uvádza 27 zlúčených pull requestov, 55 vrátení a sedem návratov zmien za päť mesiacov | PODĽA SPOLOČNOSTI | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | žiadne |
| Zdroj migrácie Db2 vznikol za menej než dva dni a tokeny stáli 4 172 dolárov | PODĽA SPOLOČNOSTI | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | žiadne |
| Autori uvádzajú, že systém pridáva čas, náklady a byrokraciu v porovnaní s rojom | OVERENÉ | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | žiadne |

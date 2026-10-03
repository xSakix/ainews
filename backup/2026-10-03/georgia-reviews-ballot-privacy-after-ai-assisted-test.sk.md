+++
title = "Georgia preveruje súkromie hlasovania po teste s pomocou AI"
slug = "georgia-preveruje-sukromie-hlasovania-po-teste-s-pomocou-ai"
description = "Mimoriadne zasadnutie volebnej rady riešilo slabinu súkromia, ktorú skúmal Max Springer z Princetonu. Obnovenie poradia hlasovacích lístkov a identifikácia voličov sú rozdielne výsledky."
tags = ["policy", "safety", "agents"]
date = 2026-10-03T05:18:20+02:00
draft = false
+++

Volebná rada Georgie sa 1. októbra zišla, aby riešila slabinu súkromia hlasovania preskúmanú pomocou programovacích nástrojov AI, informoval The Guardian 2. októbra.

Max Springer, postdoktorandský výskumník v princetonskom Center for Information Technology Policy, opísal pôvodný experiment v auguste. Použil agenta, ktorý píše a spúšťa kód, na analýzu verejných záznamov z májových primárnych volieb v Georgii a uplatnil už skôr zverejnenú slabinu anonymizácie hlasovacích lístkov.

**Prečo na tom záleží:** Správca volieb, ktorý zverejňuje záznamy, musí zachovať verejnú kontrolu bez odhalenia toho, ako hlasoval konkrétny človek. Reakcia štátu rieši toto napätie: informácie užitočné pri kontrole sčítania môžu v spojení s ďalšími záznamami prepojiť hlasovací lístok s jeho vlastníkom.

Springer uviedol, že obnovil poradie odovzdania približne 99 % lístkov odovzdaných osobne v okresoch, kde rekonštrukcia fungovala. Tento údaj vyjadruje obnovené poradie, nie identifikovaných voličov. Jeho analýza zahŕňala 139 okresov, pričom rekonštrukcia poradia bola úspešná v 114.

Samotné verejné zoznamy voličov a záznamy o lístkoch umožnili jednoznačné priradenie pri približne 1 % analyzovaných voličov, ktorí hlasovali osobne v predstihu, napísal. Presnejšie priradenie si vyžadovalo ďalšie auditné záznamy skenerov a záznamy o príchode voličov; toto rozlíšenie obmedzuje interpretáciu výsledku za celý štát.

Záznamy o hlasovacích lístkoch neobsahujú mená voličov, no ich identifikátory mali zakryť poradie, v ktorom lístky vstupovali do skenera. Springer opísal algoritmus, ktorého zdanlivú náhodnosť bolo možné spätne rozlúštiť. Spojenie obnoveného poradia s ďalšími záznamami vytvorilo riziko pre súkromie.

Springer uviedol, že agent vytvoril jeho analytický postup za niekoľko hodín s predplatným za 20 dolárov. Použil existujúce zverejnenie namiesto objavenia novej zraniteľnosti a experiment predstavil ako varovanie pred rýchlosťou zneužitia.

Brad Raffensperger, štátny tajomník Georgie, nariadil odstrániť identifikátory hlasovacích lístkov z verejne zverejňovaných dát o sčítaní, uviedol The Guardian. Rada pred začiatkom hlasovania v predstihu diskutovala aj o zmenách manipulácie s lístkami.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Rada Georgie zasadala 1. októbra; Raffensperger nariadil odstrániť identifikátory z verejne zverejňovaných dát; diskutovalo sa o zmenách manipulácie s lístkami. | ČIASTOČNE OVERENÉ | https://www.theguardian.com/us-news/2026/oct/02/midterms-ai-ballot-privacy | Spravodajstvo The Guardian a pripísané vyjadrenia predstaviteľov; záznam zasadnutia nebol dostupný. |
| Springerov text z 3. augusta sa týka primárnych volieb v máji 2026 a existujúcej zraniteľnosti anonymizácie, pričom využíva programovacieho agenta a verejné záznamy. | OVERENÉ | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | žiadne |
| Springer uvádza obnovenie poradia 1,52 milióna lístkov, teda 98,9 % lístkov odovzdaných osobne v 114 zo 139 okresov, kde rekonštrukcia uspela. Nejde o mieru identifikácie voličov za celý štát. | PODĽA SPOLOČNOSTI | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | žiadne |
| Samotné verejné súbory umožnili jednoznačné priradenie približne 1 % analyzovaných voličov hlasujúcich osobne v predstihu; ďalšie priradenie využilo auditné záznamy skenerov a záznamy príchodov. | PODĽA SPOLOČNOSTI | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | žiadne |
| Spätne rekonštruovateľné poradie identifikátorov vytvára riziko pre súkromie v spojení s ďalšími záznamami; Springer uvádza hodiny práce s predplatným programovacieho agenta za 20 dolárov. | PODĽA SPOLOČNOSTI | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | žiadne |
| Správcovia volieb čelia protichodným požiadavkám verejnej kontroly a súkromia voličov. | ANALÝZA | https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | žiadne |

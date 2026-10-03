+++
title = "Pi Pod hostuje relácie programovacích agentov na vlastnom serveri"
slug = "pi-pod-hostuje-relacie-programovacich-agentov-na-vlastnom-se"
description = "Projekt AGPL zverejňuje mobilných klientov a samostatne hostovanú sandboxovú službu. Osobitne plánovaný hostovaný produkt zatiaľ nie je dostupný."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:37:20+02:00
draft = false
+++

Pi Pod, samostatne hostovaný projekt predstavený vývojárom Evanom, spúšťa relácie programovacieho agenta Pi vo vzdialených sandboxoch dostupných z terminálu alebo telefónu.

Pi je prostredie programovacieho agenta, softvér pripájajúci model k súborom a príkazom. Pi Pod okolo neho pridáva vrstvu relácií riadených serverom, takže pracovný priestor agenta môže byť na infraštruktúre prevádzkovanej používateľom.

**Prečo na tom záleží:** Vývojár striedajúci počítač a telefón sa môže pripojiť k rovnakej vzdialenej programovacej relácii a zachovať kontrolu nad hostiteľom. Repozitár spoločne zverejňuje server relácií, sandboxovú službu a kód natívnych mobilných klientov.

Architektúra oddeľuje klientov od vykonávania. Klient príkazového riadka a aplikácie pre iOS a Android komunikujú so serverom REST a bránou relácie. Server riadi životný cyklus každého podu a spúšťa Pi cez malý adaptér v sandboxovej službe na rovnakom hostiteľovi.

Identita používa Zitadel, službu OpenID Connect, a README uvádza, že aplikačný server neuchováva heslá. Nasadenie spája Postgres s riadiacou vrstvou a používa jeden projekt Docker Compose na vlastnú inštaláciu aj aktualizácie.

Dokumentované požiadavky hostiteľa sú Linux, 8 GB RAM, Docker s Compose, Git, OpenSSL a Node.js 22.19 alebo novší. Zverejnený balík príkazového riadka umožňuje ďalšiemu stroju prihlásiť sa k serveru a spustiť pod alebo sa k nemu pripojiť; natívni klienti pre telefóny sú samostatnými komponentmi zdrojového stromu.

Koordinácia verzií je súčasťou nastavenia. CLI a server zdieľajú jednu presne určenú verziu Pi a klient novší než jeho server je odmietnutý správou, ktorá prevádzkovateľa nasmeruje najprv na aktualizáciu servera. Repozitár obsahuje príkazy na kontrolu a zmenu týchto verzií.

Kód má licenciu AGPL-3.0-only a autorské práva patria Billzo, LLC. Platená hostovaná služba je plánovaná, ale dnes výslovne nie je dostupná; jej rozšírenia hostovania pre jednotlivých používateľov, merania a účtovania sú mimo tohto repozitára. Softvér dostupný teraz je vydanie, ktoré si používatelia sami inštalujú a prevádzkujú.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Zverejnený kód Billzo AGPL-3.0-only; komponenty CLI/server/sandbox/iOS/Android; Linux 8 GB RAM a Node22.19+ nastavenie. | OVERENÉ | https://github.com/pi-pod/pipod | žiadne |
| Brána vzdialenej relácie, životný cyklus na rovnakom hostiteľovi, identita Zitadel/bez ukladania hesiel, Postgres/Compose a odmietnutie verzie. | PODĽA SPOLOČNOSTI | https://github.com/pi-pod/pipod | žiadne |
| Hostovaná služba nedostupná; rozšírenia účtovania/merania hostovanej služby mimo tohto vydania. | OVERENÉ | https://github.com/pi-pod/pipod | žiadne |
| Termináloví a mobilní klienti umožňujú vývojárovi pripojiť sa k vlastnému vzdialenému pracovnému priestoru. | ANALÝZA | https://github.com/pi-pod/pipod | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49937304 | žiadne |

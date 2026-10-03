+++
title = "KAIST zrýchľuje programovacích agentov využitím staršieho textu"
slug = "kaist-zrychluje-programovacich-agentov-vyuzitim-starsieho-te"
description = "AgSpec vyhľadáva pravdepodobné pokračovania tokenov v relácii a pracovnom priestore agenta. Uvádzané zrýchlenia merajú priepustnosť generovania, nie celý čas úlohy."
tags = ["research", "agents"]
date = 2026-10-03T05:45:20+02:00
draft = false
+++

AgSpec od KAIST zrýchľuje generovanie programovacích agentov vyhľadávaním pravdepodobných pokračovaní v existujúcom texte a úpravou dĺžky návrhu, namiesto požiadavky, aby každý kandidátsky token vytváral samostatný návrhový model.

Sumin Lee, Sukmin Cho, Suengjae Lim a Youngjin Kwon zo School of Computing na KAIST využívajú opakovanie v programovacích reláciách. Agent často vypisuje kód, záznamy alebo fragmenty staršieho pokusu, ktoré systém už má.

**Prečo na tom záleží:** Inžinier prevádzkujúci programovacie modely môže týmto existujúcim textom obmedziť sekvenčné generovanie. AgSpec skúma, kde sa opakovane použiteľný materiál nachádza a ako jeho forma ovplyvňuje prijatie navrhnutého pokračovania.

[Preprint](https://arxiv.org/abs/2610.01108), prvýkrát predložený 1. októbra, uvádza približne dvoj- až štvornásobnú priepustnosť generovania v úlohách nad repozitármi pri dávke veľkosti jeden. Najväčšie uvádzané prínosy pochádzajú zo samostatných programovacích úloh: približne päť- až osemnásobná priepustnosť oproti bežnému generovaniu pri troch testovaných modeloch.

Tieto čísla merajú fázu generovania bez spracovania promptu. Opisujú preto priepustnosť dekódovania, nie čas dokončenia celej programovacej úlohy vrátane nástrojov, testov a úvodného spracovania vstupu. Experimenty autorov porovnávajú rovnaké pracovné záťaže a prevádzkové nastavenia v rámci každého testu.

Špekulatívne dekódovanie navrhne viacero budúcich tokenov a cieľový model ich následne overí spolu. Prijaté tokeny nahrádzajú sekvenčné kroky cieľového modelu. Slabý návrh plytvá overovaním, takže užitočnosť metódy závisí od lacných návrhov, ktoré často zodpovedajú tomu, čo cieľ prijme.

Vyhľadávanie vytvára návrhy kopírovaním pokračovania po nájdení zhody s nedávnym textom. Pripomína dopĺňanie známeho úryvku z existujúceho dokumentu, pričom jazykový model kontroluje každé navrhnuté pokračovanie pred jeho prijatím. AgSpec dodáva dokumenty a vyberá dĺžku úryvku.

Dokumenty pochádzajú z troch miest: aktuálnej relácie, súborov otvorených agentom v pracovnom priestore a globálnej zbierky. Pamäť relácie zachováva staršie kolá aj po ich odchode z bezprostredného promptu. Indexovanie pracovného priestoru tiež prispôsobuje text výstupnému formátu agenta, takže súbor môže zodpovedať kódu vo forme úpravy, nielen surovému obsahu.

## Dlhšie návrhy pomáhajú, kým ich overovanie prijíma

Autori identifikujú dve podmienky opätovného použitia: materiál musí byť dostupný a jeho reprezentácia musí zodpovedať výstupu. Pridanie ďalšieho zdrojového textu nepomôže, ak okolitý formát sťažuje nájdenie príslušného pokračovania.

AgSpec mení aj dĺžku návrhu. Pre každú úlohu agenta vopred určuje horný limit a počas relácie dĺžku aktualizuje podľa spätnej väzby z overovania. Agent reprodukujúci známy kód môže prijať dlhší návrh než plánovač tvoriaci nové vysvetlenie a tieto vzorce sa medzi kolami môžu meniť.

Implementácia beží v inferenčnom systéme vLLM nad dvoma existujúcimi spôsobmi vyhľadávania. Štúdia testuje Devstral-24B, Gemma3-27B a Qwen3.6-27B na SWE-bench Verified a TeamBench, úlohách nad repozitármi zahŕňajúcich úpravy aj kontrolu kódu.

Pri dávke veľkosti jeden sa uvádzaná priepustnosť pohybuje od 2,27- do 4,37-násobku bežného generovania; pri dávke veľkosti šestnásť od 1,08- do 4,76-násobku. Širšie rozpätie ukazuje závislosť od záťaže. Overovanie odmietnutých kandidátov je pri rastúcej dávke drahšie.

Samostatné testy skúmajú LiveCodeBench bez repozitára a Terminal-Bench s jediným agentom. V prvom prípade stále dodávajú opakovane použiteľný materiál text relácie a globálna zbierka, v druhom nahrádza limity jednotlivých úloh spoločné riadenie návrhov. Prínosy samostatného programovania preto nezávisia od zbierky pracovného priestoru.

Globálna zbierka pridáva nároky na pamäť hostiteľa a načítanie, podľa konfigurácií približne 2,5–4,3 GB a deväť až pätnásť sekúnd. Záznamy relácie a pracovného priestoru sa po relácii uvoľňujú. Tieto režijné náklady dopĺňajú prínosy dekódovania a sú dôležité pri prevádzkovej implementácii.

AgSpec zostáva výsledkom preprintu bez nezávislej reprodukcie poskytnutej v štúdii. Jeho testy však oddeľujú praktický mechanizmus: uchovávať opakujúci sa text vo forme výstupu agenta a podľa spätnej väzby prijatia určovať, ako intenzívne ho znovu používať.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Lee, Cho, Lim a Kwon na KAIST; v1 predložená 1. októbra 2026. | OVERENÉ | https://arxiv.org/abs/2610.01108 | žiadne |
| Vyhľadávanie v relácii/priestore/globálnej zbierke, indexovanie formátu výstupu a vopred určené limity s priebežnou kontrolou prijatia opisujú AgSpec. | OVERENÉ | https://arxiv.org/abs/2610.01108 | žiadne |
| Špekulatívny návrh/overenie cieľom zachováva výstup; vyhľadávanie v tomto návrhu obchádza samostatný návrhový model. | OVERENÉ | https://arxiv.org/abs/2610.01108 | žiadne |
| vLLM; dva vyhľadávacie systémy; Devstral-24B, Gemma3-27B, Qwen3.6-27B; konfigurácie SWE-bench Verified/TeamBench a LiveCodeBench/Terminal-Bench. | OVERENÉ | https://arxiv.org/abs/2610.01108 | žiadne |
| Priepustnosť repozitárov 2,27–4,37× dávka1 a 1,08–4,76× dávka16; samostatný LiveCodeBench 4,87–7,94×; úvodné spracovanie nezahrnuté. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01108 | žiadne |
| Náklady overovania väčšej dávky; globálna zbierka 2,5–4,3GB, načítanie9–15s; uvoľnenie zbierok relácie. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01108 | žiadne |
| Dôsledok pre prevádzkového inžiniera a prirovnanie kopírovania úryvku vysvetľujú vyhľadávanie; záver vychádza z testov prijatia a zbierok. | ANALÝZA | https://arxiv.org/abs/2610.01108 | žiadne |

+++
title = "Kevin Liao navrhuje pamäť agentov založenú na dokumentoch"
slug = "kevin-liao-navrhuje-pamat-agentov-zalozenu-na-dokumentoch"
description = "Vývojárov postup uchováva špecifikácie a rozhodnutia v upraviteľnom Markdowne. Jeho argument sprevádza open-source implementácia, nie však porovnávací benchmark."
tags = ["agents", "tools", "essays"]
date = 2026-10-04T09:23:37+02:00
draft = false
+++

Vývojár Kevin Liao navrhuje dať programovacím agentom priebežne udržiavaný súbor projektových dokumentov. Tvrdí, že vyhľadávanie izolovaných úryvkov rozhovorov stráca príliš veľkú časť významu projektu.

V eseji zverejnenej 3. októbra opisuje pracovný priestor s pokynmi, špecifikáciami, rozhodnutiami, výskumom a indexom. Agent pred prácou prečíta príslušné dokumenty a po práci ich aktualizuje, kým dôvody zmien zostávajú v kontexte.

Pre vývojára, ktorý sa vracia k projektu v novej relácii, je lákadlom záznam prístupný človeku aj agentovi. Špecifikácia môže zachovať účel funkcie spolu s obmedzeniami, zatiaľ čo dokument s rozhodnutím môže vysvetliť, prečo bol zvolený určitý postup.

Liaova kritika sa sústreďuje na vyhľadávanie podľa podobnosti. Tvrdí, že zdanlivo relevantný úryvok môže byť zastaraný, stratiť pôvodný kontext alebo zakryť medzeru, ktorú agent nemá dôvod hľadať. Jeho tvrdenie, že tieto problémy má celá kategória pamäťových doplnkov, je názor podporený v eseji vlastnou skúsenosťou, nie porovnaním konkurenčných systémov.

Alternatíva mení pravidlo údržby. Keď sa projekt zmení, agent upraví aktuálny dokument namiesto jednoduchého pridania ďalšej spomienky na udalosť. Liao uvádza, že pred viac ako rokom začal s interným priečinkom a tento postup rozvinul do Operator Memory.

README open-source projektu opisuje tri miesta pre dokumenty: súkromné projektové znalosti, znalosti zdieľané v repozitári a osobné pravidlá používané naprieč projektmi. Uvádza adaptéry pre Claude Code, Codex a ďalšie agentové prostredia a dokumentuje inštaláciu pomocou nástroja z npm.

Repozitár priznáva aj praktickú závislosť: nový projekt začína s riedkou dokumentáciou, takže špecifikácie treba napísať skôr, než ich môžu ďalšie relácie udržiavať. Spoľahlivé aktualizácie počas dlhých rozhovorov zostávajú v pláne rozvoja. Operator Memory je dostupné pod licenciou BSD 3-Clause.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Kevin Liao vydal esej o dokumentovej pamäti 3. októbra; pokyny, špecifikácie, rozhodnutia, výskum a index; postup prečítať, vytvoriť, aktualizovať | OVERENÉ | [Zdroj](https://liao.gg/blog/agents-dont-need-memory) | žiadne |
| Vyhľadávanie podľa podobnosti môže stratiť kontext, načítať zastarané znalosti a ponechať neznáme medzery; široká kritika pamäťových doplnkov | NÁZOR | [Zdroj](https://liao.gg/blog/agents-dont-need-memory) | žiadne; argument autora bez porovnávacieho benchmarku |
| Liao uvádza používanie postupu dlhšie než rok a vývoj Operator Memory | PODĽA SPOLOČNOSTI | [Zdroj](https://liao.gg/blog/agents-dont-need-memory) | žiadne; vlastné tvrdenie o používaní |
| Súkromné, zdieľané a osobné umiestnenia dokumentov; uvedené adaptéry Claude Code a Codex; pomocný nástroj npm; licencia BSD 3-Clause | OVERENÉ | [Zdroj](https://github.com/aerovato/operator-memory) | žiadne; zdokumentovaná implementácia a licencia, bez overenia pri spustení |
| Riedka počiatočná dokumentácia a plán spoľahlivých aktualizácií | OVERENÉ | [Zdroj](https://github.com/aerovato/operator-memory) | žiadne; priznania v README |
| Upraviteľné záznamy umožňujú ľuďom a agentom spoločne skúmať účel projektu a rozhodnutia | ANALÝZA | [Zdroj](https://github.com/aerovato/operator-memory) | Úsudok z čitateľného Markdownu a aktualizácií aktuálnych dokumentov |

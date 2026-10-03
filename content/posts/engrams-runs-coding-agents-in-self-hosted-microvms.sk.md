+++
title = "Engrams spúšťa programovacích agentov vo vlastných mikroVM"
slug = "engrams-spusta-programovacich-agentov-vo-vlastnych-mikrovm"
description = "Cortex zverejňuje orchestrátor agentov, ktorý ukladá snímky nečinných relácií, s izoláciou Firecracker v produkcii a výslovnými vývojovými alternatívami."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:42:20+02:00
draft = false
+++

Engrams, samostatne hostovaný orchestrátor zverejnený spoločnosťou Cortex Applications, spúšťa relácie programovacích agentov v mikroVM Firecracker a obnovuje uložené relácie po príchode nových promptov.

Relácia spája linuxový kontajnerový obraz s prostredím agenta, softvérom na volanie modelov a nástrojov. Hostiteľ dodáva runtime a po prechode agenta do nečinnosti zachytáva stav pamäte a disku, čím uchováva pracovný priestor medzi obdobiami vykonávania.

**Prečo na tom záleží:** Inžinier prevádzkujúci službu programovacích agentov môže hostovať stav relácií a izolačnú vrstvu vo vlastnom cloudovom účte. Projekt obsahuje prehľad, klienta príkazového riadka a definície nasadenia, nie iba sandboxovú knižnicu.

Cortex uvádza obnovu za menej než 100 milisekúnd na rovnakom hostiteľovi, jednu až dve sekundy na inom a menej než sekundu pri studenom spustení bez predhrievania. README ilustruje aj deduplikáciu úložiska na tisíci relácií založených na jednom spoločnom obraze; rýchlostné aj kapacitné údaje sú tvrdeniami spoločnosti.

Návrh úložiska používa nemenné bloky adresované hashom obsahu. Bloky základného obrazu sa zdieľajú, zatiaľ čo snímka zapisuje zmenené bloky a manifest, ktorý na ne odkazuje. Obnovená relácia načítava diskové údaje a stránky pamäte podľa potreby namiesto prvotného kopírovania celého obrazu.

Produkčné nasadenie používa Kubernetes, vyhradenú skupinu hostiteľov s vnorenou virtualizáciou a dve vydania Helm pre riadiacu vrstvu a hostiteľov. Príklady Terraform cielia na Google Cloud a AWS, s ich objektovými úložiskami a správou tajomstiev pre spoločný stav a prihlasovacie údaje. Hostiteľskí agenti sa pripájajú smerom von ku koordinátoru, takže nepotrebujú vstupný riadiaci port.

Izolácia závisí od zvoleného prostredia. Produkcia používa Linux KVM a Firecracker; vývojové prostredie Apple Silicon využíva virtualizačný framework Applu. Inde môže rýchle spustenie používať obyčajné podprocesy bez izolácie. README výslovne odlišuje toto vývojové nastavenie od produkčnej topológie.

Hlavný kód má licenciu AGPL-3.0 a vybrané knižnice SDK pre vlastné prostredie agenta Apache-2.0. Prostredia Claude Code a Codex sú súčasťou projektu, používateľ však poskytuje prístup k modelu. Cortex ho označuje za nedokončené vydanie 0.x s meniacimi sa rozhraniami a udržiavaným forkom Firecracker—konkrétnymi povinnosťami údržby pre vlastného prevádzkovateľa.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Kód Cortex, AGPL-3.0 a knižnice SDK Apache-2.0, produkcia Firecracker/KVM, nasadenie prostredia/obrazu a stav0.x/fork. | OVERENÉ | https://github.com/cortexapps/engrams | žiadne |
| Obnova pod100 ms rovnaký hostiteľ,1–2 s iný,pod1 s studená;1000 relácií4 GiB základ približne100 GiB namiesto4 TiB. | PODĽA SPOLOČNOSTI | https://github.com/cortexapps/engrams | žiadne |
| Snímky podľa hashov/načítanie podľa potreby, cloudové nasadenie/odchádzajúci hostitelia, vývojová VM Apple a podprocesová alternatíva bez izolácie. | PODĽA SPOLOČNOSTI | https://github.com/cortexapps/engrams | žiadne |
| Vlastné hostovanie kódu dáva prevádzkovateľovi kontrolu nad stavom relácií a hranicami nasadenia. | ANALÝZA | https://github.com/cortexapps/engrams | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49927208 | žiadne |

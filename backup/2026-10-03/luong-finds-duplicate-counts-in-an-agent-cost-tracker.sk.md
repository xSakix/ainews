+++
title = "Luong nachádza dvojité počítanie nákladov agenta"
slug = "luong-nachadza-dvojite-pocitanie-nakladov-agenta"
description = "Opis chyby pri sledovaní udalostí agenta žiada porovnávať interné merania so skutočným účtom relácie."
tags = ["essays", "agents", "tools"]
date = 2026-10-03T05:30:20+02:00
draft = false
+++

Thuan Luong, softvérový vývojár, uvádza, že jeho sledovanie nákladov v Claude Code započítalo jeden logický krok viackrát a nadhodnotilo odhad oproti skutočnému účtu relácie.

Článok z 2. októbra opisuje experiment s háčikmi sprístupňujúcimi udalosti v programovacom agentovi. Ich sledovanie pomohlo odhaliť opakované čítanie súborov, no zaviedlo aj novú chybu, keď internú udalosť považoval za celý krok rozhovoru.

**Prečo na tom záleží:** Technický vedúci prideľujúci rozpočet agentom potrebuje merania zodpovedajúce skutočnému používaniu. Luong ukazuje, prečo nestačí pridať meranie: treba overiť aj význam udalostí a pravidlá počítania.

Tvrdí, že háčik dokončenia sa spúšťal počas prestávok v dlhšom reťazci volaní nástrojov. Sledovanie tieto oznámenia vykladalo ako osobitné súhrny, čím vytvorilo výrazne vyšší odhad než konzola poskytovateľa. Následne zmenil odstraňovanie duplicít na použitie identifikátora kroku a informácie o poradí.

Sú to pozorovania opísané autorom, nie reprodukovaný test rozhrania Anthropicu. Článok spája kód s opisom zlyhania, takže predpoklad počítania je viditeľnejší než všeobecné tvrdenie, že agent je drahý.

Užitočnou technickou otázkou je, ktorá udalosť nesie poplatok. Viacero oznámení môže opisovať priebeh jednej pracovnej jednotky; súčet ich celkov môže započítať tú istú činnosť opakovane. Prehľad môže pôsobiť presne a používať nesprávnu jednotku, preto porovnanie vzorovej relácie s osobitným účtom patrí k overeniu meracieho nástroja.

Luong uvádza, že háčiky robia sledovanie priamo v procese príťažlivejším než skoršie riešenie cez proxy. Proxy však zatiaľ ponecháva a chce počkať na ďalšie menšie vydanie, kým udalosti dokončenia zverí prácu súvisiacu s účtovaním.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Luong a publikovanie 2. októbra; experiment a zobrazený kód. | OVERENÉ | https://luonghongthuan.com/en/blog/claude-code-mods-typescript-middleware/ | Žiadne; pripísané primárnemu zdroju. |
| Interné udalosti dokončenia, duplicitné súčty, nesúlad konzoly, oprava identifikátorom a poradím, ponechané proxy. | ČIASTOČNE OVERENÉ | https://luonghongthuan.com/en/blog/claude-code-mods-typescript-middleware/ | Žiadne; pripísané primárnemu zdroju. |
| Meranie používania vyžaduje overenie jednotiek udalostí a porovnanie s účtami. | ANALÝZA | https://luonghongthuan.com/en/blog/claude-code-mods-typescript-middleware/ | Žiadne; pripísané primárnemu zdroju. |

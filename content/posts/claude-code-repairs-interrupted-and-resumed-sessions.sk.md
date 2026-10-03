+++
title = "Claude Code opravuje prerušené a obnovené relácie"
slug = "claude-code-opravuje-prerusene-a-obnovene-relacie"
description = "Verzia 2.1.288 obnovuje vymazané koncepty a pridáva ovládanie kontroly kódu. Opravy sa týkajú straty kontextu, časových limitov a kontroly oprávnení."
tags = ["tools", "agents", "safety"]
date = 2026-10-03T05:57:20+02:00
draft = false
+++

Spoločnosť Anthropic vydala 2. októbra Claude Code 2.1.288, ktorý opravuje viaceré situácie, keď prerušené alebo obnovené relácie pri programovaní strácali prácu, nedokázali pokračovať alebo používali nesprávny kontext.

Claude Code je programovací agent spoločnosti Anthropic pre terminály a vývojové prostredia. Aktualizácia sa zameriava na zachovanie súvislosti relácie pri výpadkoch spojenia, dlhých odpovediach a reštartoch. Zároveň pridáva ovládanie obnovy konceptu a počtu zistení, ktoré agent uvedie pri kontrole kódu.

**Prečo na tom záleží:** Vývojár, ktorý obnovuje dlhú programovaciu úlohu, dostáva opravy zamerané na zachovanie súborov, kontextu a poslednej odpovede. Tieto opravy podporujú pokračovanie rozpracovanej úlohy namiesto toho, aby vývojár musel znovu zostaviť informácie, ktoré agent predtým videl.

[Oficiálne vydanie](https://github.com/anthropics/claude-code/releases/tag/v2.1.288), zverejnené o 20:19 UTC, opisuje nový spôsob obnovy: stlačenie šípky nahor v prázdnom prompte obnoví koncept vymazaný cez Ctrl+C vrátane vloženého textu a obrázkov. Príkaz `/code-review` tiež prijíma `--max-findings` s číslom alebo hodnotou `all`; voľba zostáva platná až do obnovenia hodnoty `default`.

Spoločnosť Anthropic uvádza, že neinteraktívne relácie a podagenti teraz pokračujú z čiastočnej odpovede po prekročení časového limitu API počas odpovedania. Samostatná oprava rieši dlhé rozhovory, ktoré zlyhali s chybou dĺžky promptu, keď predchádzajúca odpoveď uviedla nulovú spotrebu tokenov. Opravy obnovy sa týkajú zahodenia obnoveného kontextu, neuloženia poslednej odpovede a načítania prepisu v čase, keď ho iný proces prepisuje.

Vydanie opravuje aj spracovanie oprávnení. Spoločnosť Anthropic uvádza, že neúspešné vyhodnotenie hookov alebo nemožnosť previesť vstup nástroja do serializovanej podoby teraz blokuje volanie namiesto preskočenia príslušných hookov oprávnení. Opravuje aj spustenie nebezpečných príkazov na mazanie bez otázky v rámci vnorených shellových skriptov pri niektorých nastaveniach oprávnení. Ide o zmeny deklarovaného správania; poznámky k vydaniu neobsahujú nezávislý bezpečnostný test.

Balíky pre macOS, Linux a Windows sú dostupné na stránke vydania. Aktualizácia pridáva výzvu na opätovné prihlásenie, keď pripojený server MCP počas volania nástroja požiada o širší rozsah OAuth oprávnení, takže zmena prístupu je viditeľná počas prebiehajúcej relácie.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Spoločnosť Anthropic zverejnila verziu 2.1.288 2. októbra o 20:19 UTC s balíkmi pre macOS, Linux a Windows. | OVERENÉ | [Oficiálne vydanie](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | žiadne |
| Šípka nahor obnovuje koncept vymazaný cez Ctrl+C vrátane textu a obrázkov; kontrola kódu podporuje trvalé nastavenie --max-findings. | OVERENÉ | [Zoznam zmien vydania](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | žiadne |
| Pokračovanie z čiastočnej odpovede, automatické skracovanie kontextu a uvedené chyby obnovy kontextu a prepisu sú opravené. | PODĽA SPOLOČNOSTI | [Opravy spoločnosti Anthropic](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | žiadne |
| Zlyhanie spracovania hookov oprávnení blokuje volanie; kontroly mazania vo vnorenom shelli a výzvy rozsahu OAuth sú opravené. | PODĽA SPOLOČNOSTI | [Opravy spoločnosti Anthropic](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | žiadne |
| Opravy kontinuity pomáhajú vývojárovi zachovať kontext existujúcej úlohy; tieto poznámky k vydaniu neobsahujú nezávislý bezpečnostný test. | ANALÝZA | [Zverejnené poznámky k vydaniu](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | žiadne |

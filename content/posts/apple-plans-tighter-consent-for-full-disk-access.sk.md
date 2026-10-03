+++
title = "Apple plánuje prísnejší súhlas s úplným prístupom k disku"
slug = "apple-planuje-prisnejsi-suhlas-s-uplnym-pristupom-k-disku"
description = "Apple uvádza, že macOS bude vyžadovať výslovnejší úkon pred udelením širokého prístupu aplikáciám k osobným dátam. Dôvodom sú čoraz samostatnejší AI agenti."
tags = ["safety", "agents", "tools"]
date = 2026-10-03T05:19:20+02:00
draft = false
+++

Apple 2. októbra oznámil, že posilní proces udeľovania úplného prístupu k disku, Full Disk Access, v macOS. Varuje, že čoraz samostatnejší AI agenti zvyšujú dôsledky tohto širokého oprávnenia.

Full Disk Access umožňuje aplikácii pristupovať k dátam, ktoré bežne chránia samostatné mechanizmy ochrany súkromia. Apple uvádza, že oprávnenie pomáha fungovaniu zálohovacieho softvéru, no niektorí vývojári ho používajú spôsobmi, ktoré sprístupňujú súbory, e-maily, správy a históriu prehliadania bez toho, aby používatelia rozumeli rozsahu prístupu.

**Prečo na tom záleží:** Vývojári lokálnych AI asistentov budú pri žiadosti o toto oprávnenie čeliť výslovnejšiemu kroku udelenia súhlasu. Ohrozené je aj súkromie ľudí, ktorí si vymieňajú správy s používateľom aplikácie: ich komunikácia môže patriť medzi dáta, ku ktorým aplikácia získa prístup.

[Oznámenie pre vývojárov](https://developer.apple.com/news/?id=p6zjojqw) sľubuje dodatočné kontrolné mechanizmy, no neuvádza dátum vydania, verziu macOS ani technickú špecifikáciu. Opisuje pripravovanú zmenu, nie ochranu, ktorá je už dostupná v softvérovej aktualizácii.

Oznámenie prichádza po spore o asistenta Muse spoločnosti Meta. [Ars Technica informuje](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/), že komentátor Jason Aten uviedol, že Muse spomenul výmenu správ v Apple Messages, ku ktorej podľa jeho názoru nemal prístup. Meta trvá na tom, že jej integrácia Messages vyžaduje úplný prístup k disku na úrovni systému aj povolený konektor v aplikácii Muse.

Bezpečnostný výskumník Patrick Wardle povedal pre Ars, že samotné systémové oprávnenie umožňuje softvéru čítať dáta správ a ďalšie dostupné súbory. Tým sa odlišuje oprávnenie udelené operačným systémom od vlastného prísľubu aplikácie o tom, kedy ho použije.

Apple vo svojom oznámení nespomína žiadneho vývojára. Ďalšou konkrétnou informáciou bude mechanizmus, ktorý vydá, a úkon, ktorý bude vyžadovať od používateľov.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Oznámenie Apple z 2. októbra sľubuje mechanizmy bez podrobností implementácie. | OVERENÉ | [Oznámenie Apple](https://developer.apple.com/news/?id=p6zjojqw) | [Správa Ars](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/) |
| Apple pripisuje väčšie riziko pre súkromie širokému prístupu a samostatným agentom. | PODĽA SPOLOČNOSTI | [Oznámenie Apple](https://developer.apple.com/news/?id=p6zjojqw) | žiadne |
| Aten opísal neočakávaný prístup k Messages; Meta uvádza, že jej integrácia vyžaduje obe oprávnenia. | ČIASTOČNE OVERENÉ | [Vyjadrenia, o ktorých informuje Ars](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/) | Incident nebol nezávisle zopakovaný |
| Wardle rozlišuje široký prístup operačného systému od nastavenia konektora v aplikácii. | ČIASTOČNE OVERENÉ | [Rozhovor s Wardlom v Ars](https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/) | žiadne |

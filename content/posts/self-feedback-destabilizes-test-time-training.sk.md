+++
title = "Vlastná spätná väzba destabilizuje trénovanie pri inferencii"
slug = "vlastna-spatna-vazba-destabilizuje-trenovanie"
description = "Preprint sleduje, ako sa modely, ktoré počas inferencie aktualizujú váhy z vlastného generovaného textu, môžu dostať do škodlivej spätnej väzby."
tags = ["research", "models"]
date = 2026-10-08T03:56:31+02:00
draft = false
+++

Jazykové modely, ktoré sa počas inferencie trénovali na vlastnom výstupe, sa podľa preprintu pri predpovedaní nezávislého ľudského textu zhoršili po dlhšom pôsobení spätnej väzby.

Trénovanie počas inferencie umožňuje modelu aktualizovať váhy počas používania, čím sa samotný model stáva formou pracovnej pamäte. Cheng Luo, Bing Li a Bernard Ghanem testovali, čo sa stane, keď text použitý na tieto aktualizácie generuje ten istý meniaci sa model.

Výsledok je dôležitý pre vývojárov agentov, ktorí sa majú priebežne učiť z vlastnej práce. Aktualizácia môže uľahčiť predpovedanie najnovšieho vygenerovaného úseku a pritom potichu zhoršiť výkon na novom texte od ľudí. Opakovanie tohto lokálneho zlepšenia mení žiaka aj zdroj jeho ďalšej lekcie.

## Generátor a žiak sa navzájom odkláňali

Výskumníci spustili tri konfigurácie modelov trénovaných počas inferencie, označené ako 125 miliónov, 760 miliónov a 3 miliardy parametrov, na prúdoch dlhých 128 000 tokenov. Zachovanie aktualizácií z generovaného textu zhoršilo predpovedanie na samostatnom súbore ľudského textu vo všetkých troch prípadoch. Rovnaký vzor vznikol pri bežných aktualizáciách Adam existujúcich váh modelu Qwen3-4B.

Učenie počas inferencie nebolo škodlivé samo osebe. Rovnaké mechanizmy aktualizácie zlepšili výkon, keď vstupný text pochádzal od ľudí. Zlyhanie sa objavilo vtedy, keď sa text generovaný modelom vrátil do modelu, ktorý mal vytvoriť ďalší trénovací úsek.

Práca túto slučku rozdeľuje pomocou párovaných experimentov. V experimente „Fixed Generation“ dodávala vygenerovaný trénovací text zmrazená kópia, zatiaľ čo iný model sa ďalej aktualizoval. Podľa autorov sa tým odstránilo viac než 98 % nameraného poškodenia v dvoch menších konfiguráciách. Porovnanie označuje za hlavný zdroj nestability meniaci sa generátor, nie samotný syntetický text.

Druhý experiment s opakovaným prehrávaním rozlíšil dva náklady. Model musel najprv čítať text, ktorý sa časom zhoršoval, a potom ukladal ďalšie zmeny trénovaním na tomto texte. Párovaný test jednej aktualizácie odhalil okamžitý konflikt: každá aktualizácia zlepšila predpoveď zdrojového úseku, ale zhoršila predpoveď nového ľudského textu.

Konflikt sa ľahko prehliadne, keď sú trénovací signál a cieľ hodnotenia rovnakým úsekom. Aktualizácia je podľa lokálneho cieľa úspešná: strata na texte, ktorý ju vyvolal, klesne. Poškodenie sa ukáže až na oddelenom ľudskom texte, ktorý slúži ako referencia toho, či model pri adaptácii zachováva širšie jazykové rozdelenie.

## Nezávislé dôkazy pôsobili ako brzda

Nie všetky behy zlyhali rovnako. Autori uvádzajú, že po dlhšej adaptácii v uzavretej slučke mala malá časť trajektórií na svedomí mnohé z najväčších strát. Pre túto koncentráciu je priemerná krátkodobá kontrola slabou ochranou: systém môže vyzerať stabilne, kým ho jedna sekvencia aktualizácií z vlastného výstupu neposunie ďalej.

Dlhé prúdy sú dôležité, pretože každá prijatá aktualizácia mení východisko nasledujúcej. Chyby preto neovplyvňujú iba aktuálnu predpoveď; menia aj text, ktorý sa vytvorí a z ktorého sa model neskôr učí. Štúdia meria tento kumulatívny proces namiesto hodnotenia izolovaných krokov samotrénovania.

Navrhnuté zmiernenie s názvom Settlement vyhodnotí kandidátsku aktualizáciu váh na nezávislom reálnom texte pred jej prijatím. V dvoch menších konfiguráciách zostal priemerný koncový rozdiel 0,07 a -0,02 natu, pričom sa zachovala užitočná adaptácia na reálny text. Metrika meria predikčnú stratu, takže hodnoty blízke nule znamenajú, že ochrana do veľkej miery odstránila rozdiel oproti porovnávacej podmienke.

Ide o výsledky autorov z prvej verzie preprintu na arXiv bez nezávislej replikácie. Testované prúdy a predikčný cieľ sú užšie než celé správanie nasadeného agenta a štúdia neurčuje, ako rýchlo by sa rovnaká slučka objavila vo väčších špičkových systémoch.

Experiment napriek tomu ponúka kauzálne vysvetlenie známej intuície o samotrénovaní: kontrola, či aktualizácia vysvetľuje vlastný zdroj, nestačí. Ďalšie konkrétne kritérium autorov je externé — aktualizácia musí zachovať aj predpovedanie na dôkazoch, ktoré adaptujúci sa model nevytvoril.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Zachovanie aktualizácií z generovaného textu zhoršilo predpovedanie nezávislého ľudského textu v troch konfiguráciách trénovania počas inferencie | PODĽA SPOLOČNOSTI | [Preprint Lua, Liho a Ghanema](https://arxiv.org/abs/2610.05076) | žiadne |
| Rovnaké zlyhanie sa objavilo, keď Adam aktualizoval existujúce váhy Qwen3-4B | PODĽA SPOLOČNOSTI | [Preprint Lua, Liho a Ghanema](https://arxiv.org/abs/2610.05076) | žiadne |
| Rovnaké mechanizmy aktualizácie priniesli zlepšenie na reálnom texte | PODĽA SPOLOČNOSTI | [Preprint Lua, Liho a Ghanema](https://arxiv.org/abs/2610.05076) | žiadne |
| Zmrazený generátor odstránil viac než 98 % poškodenia pri 125 miliónoch a 760 miliónoch parametrov | PODĽA SPOLOČNOSTI | [Preprint Lua, Liho a Ghanema](https://arxiv.org/abs/2610.05076) | žiadne |
| Settlement ponechal koncové rozdiely 0,07 a -0,02 natu pri 125 miliónoch a 760 miliónoch parametrov a zachoval adaptáciu na reálny text | PODĽA SPOLOČNOSTI | [Preprint Lua, Liho a Ghanema](https://arxiv.org/abs/2610.05076) | žiadne |
| Preprint troch autorov bol odoslaný 4. októbra 2026 | OVERENÉ | [Záznam arXiv](https://arxiv.org/abs/2610.05076) | žiadne |

+++
title = "Odpoveď zostala v modeli"
slug = "odpoved-zostala-v-modeli"
description = "Štúdia 15 jazykových modelov ukazuje, že mnohé zlyhania pracovnej pamäti nastávajú až po výbere správnej položky. Modely si uchovávajú dekódovateľnú informáciu, ale nedokážu ju uviesť."
tags = ["research", "models"]
date = 2026-10-16T04:07:00+02:00
draft = false
+++

Predstavme si model, ktorý dostane krátky zoznam symbolov. Potom ho vyruší druhý zoznam a model má pomenovať pôvodnú cieľovú položku. Odpovie symbolom z rušivého zoznamu. Zjavné vysvetlenie by bolo, že prvý symbol zabudol. V tejto ilustračnej situácii však vnútorná sonda dokáže cieľ stále takmer dokonale rozpoznať. Odpoveď sa nevymazala. Problém vznikol niekde medzi jej uchovaním a vyslovením.

Práve tento rozdiel skúma nový preprint o pracovnej pamäti jazykových modelov. Autori testovali 15 modelov so 70 miliónmi až 14 miliardami parametrov na úlohách vyvolávajúcich interferenciu. Zistili, že pozornostné hlavy často vyberali správny cieľ, aj keď konečná odpoveď bola nesprávna. Jednoduché sondy dokázali pri mnohých zlyhaniach dekódovať cieľ zo skrytých stavov s takmer dokonalou presnosťou.

Výsledok spochybňuje bežnú skratku pri hodnotení modelov: nesprávny výstup sa často považuje za dôkaz, že príslušná informácia chýba. Štúdia však oddeľuje tri činnosti, ktoré jediné skóre presnosti spája: výber relevantnej položky, uchovanie jej identity a jej prečítanie ako odpovede.

## Kontrolovaný problém pamäti

Pracovná pamäť nie je dlhodobé úložisko. Je to dočasná schopnosť udržať informáciu v použiteľnom stave, zatiaľ čo o pozornosť súťaží iný obsah. Experimenty s ľuďmi často ukazujú, že položka zostáva čiastočne dostupná, aj keď účastník uvedie nesprávnu. Podobná interferencia môže sťažiť rozlíšenie dvoch spomienok bez toho, aby niektorá zanikla.

Výskumníci vytvorili úlohy, v ktorých mohli meniť cieľ, konkurenčné položky aj ich pozície. Následne skúmali vnútorné stavy modelov v miestach, kde sa mal cieľ vybrať a preniesť ďalej. Testovali viacero veľkostí a rodín modelov, čo je dôležité: jav pozorovaný v jedinom kontrolnom bode môže byť architektonickou zvláštnosťou, nie všeobecným mechanizmom.

Pri správnych odpovediach sa potvrdil očakávaný priebeh: pozornosť sa sústredila na cieľ a posledné vrstvy vytvorili správny token. Pri mnohých nesprávnych odpovediach však prvá časť priebehu zostala rovnaká. Hlavy vyberajúce cieľ venovali pozornosť správnej pozícii. Sondy v skrytých stavoch našli dosť informácií na identifikáciu cieľa. Výstup napriek tomu zodpovedal konkurenčnej položke.

Sonda dokazuje dekódovateľnosť, nie skutočné využitie informácie. Klasifikátor trénovaný dodatočne môže zo stavu vyťažiť informáciu, ku ktorej sa vlastný výpočet modelu nedokáže dostať. Autori preto nezostali iba pri čítaní stavov a priamo do nich zasiahli.

## Oslabenie konkurentov

Kľúčový kauzálny test potlačil reprezentácie identity necieľových položiek. Tento zásah zlepšil citlivosť meranú ukazovateľom d-prime v smere, ktorý predpovedá vysvetlenie interferenciou. Keď výskumníci oslabili konkurenčné položky, model dokázal uložený cieľ ľahšie uviesť.

Neznamená to, že každá chyba pamäti je chybou pri čítaní informácie. Model nemusí položku vôbec zakódovať, môže ju stratiť alebo vybrať nesprávnu pozíciu. Tvrdenie štúdie je užšie: významná časť zlyhaní nastáva, hoci informácia o cieli zostáva vnútorne dostupná, a zmätok medzi podobnými reprezentáciami môže zablokovať konečnú odpoveď.

Rozdiel je dôležitý pre vývoj systémov. Rozšírenie kontextu alebo zopakovanie cieľa rieši problém ukladania informácie. Môže však pomôcť len málo, keď model cieľ už má, ale nevie ho odlíšiť od konkurenčného obsahu. V takom prípade môžu byť potrebné iné prompty, priebežná štruktúra alebo architektonické zmeny, ktoré pri čítaní informácie lepšie odlíšia jej identitu.

Dôležité je to aj pre interpretáciu modelov. Pozornosť v transformeroch vznikla ako mechanizmus prepájania pozícií v sekvencii, no často sa skúma, akoby pozornosť venovaná správnemu tokenu rozhodovala o tom, čo model vie. V tejto štúdii môže pozornosť smerovať k cieľu a napriek tomu nevytvoriť správny výstup. Naopak, nesprávna odpoveď neznamená, že pozornosť cieľ minula.

## Podobnosť s ľuďmi má svoje hranice

Autori opisujú interferenciu ako podobnú ľudskej, ale ide o funkčné, nie biologické porovnanie. Transformer nepotrebuje ľudský pamäťový systém na to, aby vykazoval rovnaký rozdiel medzi dostupnosťou informácie a jej uvedením. Podobné chyby môžu vznikať v úplne odlišných mechanizmoch.

Ani veľkosť modelu problém neodstraňuje. Testovanie modelov až so 14 miliardami parametrov ukazuje, že jav pretrváva aj mimo malých experimentálnych sietí. Nedokazuje však rovnaký výsledok v podstatne väčších frontier modeloch ani v proprietárnych systémoch po dodatočnom trénovaní. Úlohy boli zámerne kontrolované. Skutočné rozhovory kombinujú vyhľadávanie informácií, nasledovanie inštrukcií, plánovanie a generovanie spôsobmi, ktoré sťažujú určenie príčiny jednotlivého zlyhania.

Práve kontrolované úlohy sú však podstatou výskumu. Umožňujú zmeniť jedinú konkurenčnú položku, pozorovať jednu reprezentáciu a otestovať jeden zásah. Štúdia ponúka spôsob, ako sa po nesprávnej odpovedi modelu pýtať presnejšie: informácia sa nikdy nezakódovala, stratila sa, alebo zostala prítomná, no výstupný proces sa k nej nedostal?

Vráťme sa k ilustračnej úlohe so symbolmi. Model uvedie nesprávnu položku a hodnotiteľ zaznamená chybu. Z pohľadu používateľa je to správny verdikt. Vnútri systému sa však mohla uskutočniť väčšina potrebnej práce. Ďalší pokrok možno nepríde z väčšej pamäti, ale zo schopnosti modelu prečítať to, čo si už uchoval.

## Použité zdroje

- Vaswani, A., et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- *Working Memory Readout Bottlenecks in Language Models* (2026). https://arxiv.org/abs/2610.21176

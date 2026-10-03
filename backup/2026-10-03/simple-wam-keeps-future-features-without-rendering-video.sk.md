+++
title = "Simple-WAM zachováva príznaky budúcnosti bez vytvárania videa"
slug = "simple-wam-zachovava-priznaky-buducnosti-bez-vytvarania-vide"
description = "Kontrolovaná štúdia robotiky zistila, že jeden priechod zašumenými tokenmi budúceho videa zachováva veľkú časť výhody modelu sveta a akcií pri zovšeobecňovaní."
tags = ["research", "models", "agents"]
date = 2026-10-03T05:58:20+02:00
draft = false
+++

Výskumníci uvádzajú, že riadiace modely robotov dokážu zachovať výhody predpovedania budúcnosti bez opakovaného vytvárania čistých videozáberov. Ich metóda Simple-WAM poskytuje modelu akcií príznaky súvisiace s budúcnosťou z jediného priechodu zašumenými video tokenmi.

Model sveta a akcií sa učí predpovedať ďalšie akcie robota aj to, ako bude scéna následne vyzerať. Vytváranie tohto predstaveného videa počas prevádzky je výpočtovo náročné. Nová štúdia oddeľuje užitočnú reprezentáciu budúcnosti od nákladnej práce potrebnej na jej premenu na viditeľnú sekvenciu.

**Prečo na tom záleží:** Výskumníci robotiky môžu toto rozlíšenie využiť pri hodnotení rýchlejších riadiacich modelov v zmenenom prostredí a pri neznámych úlohách. Rovnaký výkon v známych scénach podobných trénovacím neznamenal, že si dve metódy v experimentoch autorov zachovali rovnakú schopnosť prispôsobiť sa.

Renping Zhou, Zanlin Ni a kolegovia z Leap Lab na Tsinghua University, University of Science and Technology of China a Beijing Institute of Technology zverejnili [preprint](https://arxiv.org/abs/2609.34981) 28. septembra. Výsledky uvádzajú samotní autori a porovnania sa týkajú konkrétnej konfigurácie modelu, nie všetkých riadiacich modelov robotov.

## Užitočný krok prichádza pred čistým obrazom

Štúdia porovnáva explicitný prístup, ktorý pri vytváraní bloku akcií opakovane odšumuje budúce video, s latentným prístupom, ktorý počas inferencie vynecháva tokeny budúceho videa. Kontrolované porovnanie zachováva rovnaký základný model, trénovacie dáta aj rozpočet. Štruktúrovaná maska pozornosti určuje, či tokeny akcií môžu čítať reprezentácie budúcnosti.

Pri známych úlohách LIBERO dosiahli explicitná a latentná konfigurácia podľa autorov úspešnosť 97,75 % a 96,85 %. Rozdiel bol oveľa väčší pri zmenách uhlov kamier, osvetlenia, rozmiestnenia predmetov a ďalších podmienok: 67,72 % oproti 53,75 % v LIBERO-Plus. Použitie menšieho počtu ukážok rozdiel tiež zväčšilo.

Najväčší odstup sa objavil, keď výskumníci poskytli video úloh vynechaných z trénovania bez označení akcií. Explicitný model dosiahol 69,90 %, kým latentná konfigurácia 5,90 %. Ani jeden nepodával silný výkon, keď o týchto úlohách nedostal žiadne dáta. Je to podstatné, pretože učenie sa z pozorovanej činnosti sa líši od úspechu pri úplne neznámej úlohe bez dodatočných informácií.

Tím potom bez opätovného trénovania menil počet spustení video vetvy explicitného modelu. Takmer celá výhoda pochádzala z prvého priechodu. V tom okamihu boli vstupy budúceho videa stále gaussovským šumom, nie rozpoznateľnými predpovedanými zábermi. Vetva akcií napriek tomu získavala užitočné medziľahlé príznaky zo spracovania týchto tokenov spolu s aktuálnym pozorovaním.

Simple-WAM zachováva tento prvý priechod a jeho príznaky opakovane využíva počas odšumovania akcií. Mení aj trénovanie tak, aby sa úplne zašumené vstupy budúceho videa objavovali častejšie a zodpovedali podmienke používanej počas prevádzky. Metóda ponecháva kroky generovania akcií nezmenené a nepridáva nový modul ani novú stratovú funkciu.

V hlavnom hodnotení autorov dosiahol Simple-WAM pri zmenách prostredia 79,5 %, oproti 67,7 % pri explicitnom základnom modeli a 53,8 % pri latentnom. Uvádzaná latencia bloku akcií bola na RTX 5090 74,7 milisekundy, oproti 286,9 milisekundy a 62,0 milisekundy pri ostatných dvoch modeloch. Tieto čísla opisujú testované konfigurácie, nie celkový čas reakcie robota.

Experimenty so skutočným robotom využívali dvojramennú platformu AgileX Aloha. Medzi štyrmi trénovacími úlohami bolo ukladanie misiek na seba a usporiadanie predmetov v určenom poradí. Pri zmenenom osvetlení, pozadí a rozmiestnení dosiahol Simple-WAM podľa autorov priemer 69,2 %, oproti 25,2 % pri latentnom základnom modeli. Tieto výsledky zo skutočného prostredia merajú podiel splnených čiastkových cieľov úlohy, spriemerovaný cez 30 pokusov na úlohu; nejde o binárnu úspešnosť úplného dokončenia úloh.

Hlavné zistenie je teda užšie než tvrdenie, že predpovedanie budúcnosti nie je potrebné. Príznaky podmienené budúcnosťou boli naďalej dôležité, no generovanie čistého videa bolo v tejto konfigurácii zväčša nahraditeľné. Štúdia používala päťmiliardový základný video model bez rozsiahleho predtrénovania na interakciách s fyzickým prostredím. Či rovnaký vzťah platí pri väčších modeloch alebo pri modeloch rozsiahlo predtrénovaných na skúsenostiach robotov, zostáva výslovne otvorenou otázkou práce.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Preprint bol prvýkrát predložený 28. septembra a uvádza tri inštitúcie uvedené vyššie. | OVERENÉ | [Záznam arXiv a úplná práca](https://arxiv.org/abs/2609.34981) | žiadne |
| Zhodné konfigurácie zostávajú blízke pri známych úlohách, no odlišujú sa pri zmenách prostredia a videu úloh vynechaných z trénovania. | PODĽA SPOLOČNOSTI | [Tabuľky 1–2](https://arxiv.org/abs/2609.34981) | žiadne |
| Jeden priechod zašumenými tokenmi budúcnosti poskytuje užitočné príznaky; Simple-WAM tomu prispôsobuje trénovací rozvrh. | PODĽA SPOLOČNOSTI | [Časti 4–5](https://arxiv.org/abs/2609.34981) | žiadne |
| Simple-WAM uvádza výkon 79,5 % pri zmenách prostredia a latenciu bloku akcií 74,7 milisekundy na RTX 5090. | PODĽA SPOLOČNOSTI | [Časť 6 a tabuľka 2](https://arxiv.org/abs/2609.34981) | žiadne |
| Výsledky so skutočným robotom priemerujú splnenie čiastkových cieľov cez 30 pokusov na úlohu, s uvedeným obmedzením veľkosti modelu. | PODĽA SPOLOČNOSTI | [Časti 6–7 a príloha A.3](https://arxiv.org/abs/2609.34981) | žiadne |

+++
title = "Model poznal Minecraft, no zvolil si skutočný svet"
slug = "model-poznal-minecraft-no-zvolil-si-skutocny-svet"
description = "Šesť vizuálno-jazykových modelov poznalo pravidlá Minecraftu, no pri snímkach bez názvu hry odpovedalo podľa fyziky skutočného sveta. Nový benchmark oddeľuje znalosť sveta od výberu pravidiel, ktoré v ňom platia."
tags = ["models", "research"]
date = 2026-11-28T04:05:30+01:00
draft = false
+++

Mara položila snehový blok vedľa lávy a čakala. Biela kocka zostala na mieste, pretože v Minecrafte sa takýto blok pri láve neroztopí. Modelu poslala snímku obrazovky bez názvu hry. Odpoveď znela, akoby pixely zachytávali zimnú cestu: sneh sa roztopí.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Nový preprint označuje toto zlyhanie ako výber sveta. Jianxin Gao, Bohan Chen, Runze Li a Qi Zhang otestovali šesť multimodálnych jazykových modelov na 1 240 otázkach s výsledkami overenými priamo v herných enginoch. Modely vedeli opísať pravidlá, rozpoznať hry a často aj uviesť, že otázka sa týka hry. Keď však správny svet určovala iba snímka, často sa vrátili k fyzike skutočného sveta.

Rozdiel je dôležitý aj mimo hier. Modely čoraz častejšie hodnotia vygenerované videá, ovládajú softvér a riadia agentov v prostrediach s inými pravidlami než v každodennom živote. Benchmark, ktorý prostredie pomenuje, môže merať, či model jeho pravidlá pozná. Nemusí však ukázať, či ich model vyberie, keď dostane iba neoznačenú scénu.

## Tri podoby toho istého pravidla

Výskumníci zostavili RuleCraft zo 155 pravidiel Minecraftu. Každé pravidlo spája scénu a činnosť s výsledkom, ktorý vytvorí neupravený herný server. Hlavnú sadu tvorí 95 pravidiel. Ďalších 60 náročnejších pravidiel sa sústreďuje na procesy, ktoré hra nesimuluje, napríklad na zmenu stavby vplyvom počasia a času.

Každé pravidlo má tri podoby. Textová otázka sa pýta, čo sa stane v Minecrafte. Druhá otázka ukáže scénu a zároveň pomenuje hru. Tretia ukáže rovnakú scénu bez názvu sveta. Tento návrh oddeľuje tri kroky, ktoré bežné vizuálne benchmarky často miešajú: znalosť pravidla, vnímanie scény a výber sústavy pravidiel, ktorá scénu riadi.

Benchmark rozlišuje aj konfliktné a zhodné pravidlá. Pri konfliktnom pravidle má hra iný výsledok než skutočný svet. Blok môže zostať vo vzduchu po odstránení podpery alebo sa drevené dosky pri ohni nezmenia. Pri zhodnom pravidle je výsledok v oboch svetoch rovnaký. Ak by model na všetko mechanicky používal hernú logiku, kontrolné príklady by túto skratku odhalili.

Šesť modelov poznalo Minecraft veľmi dobre. Keď sa ich výskumníci pýtali, z ktorej hry pochádza obrázok, správne pomenovali Minecraft pri 93–100 % snímok. Pravidlá vedeli vysvetliť textom a zväčša odpovedali správne, keď prompt hru pomenoval. Zlyhanie sa objavilo vtedy, keď mal svet vybrať samotný obrázok.

## Predvolenou voľbou sa stal skutočný svet

Pri konfliktných pravidlách v hlavnej sade zvýšilo pomenovanie Minecraftu presnosť všetkých šiestich modelov o 8,2–19,8 percentuálneho bodu. V náročnej sade dosiahol rozdiel 33,8–52,7 percentuálneho bodu. Najväčší bol pri pasívnych scénach, v ktorých hra ponechá predmet bez zmeny, hoci v skutočnosti by ho zmenil čas, počasie alebo teplo.

Nesprávne odpovede neboli náhodné. Modely vyberali výsledok zo skutočného sveta. V zázname uvažovania dokázali uviesť príslušné pravidlo Minecraftu a napriek tomu skončili pri bežnej fyzike. Výslovná požiadavka na uvažovanie tento vzorec neodstránila. Podobný jav sa objavil aj v menších testoch hier Terraria a Stardew Valley.

Ide o iný problém než jednoduchý konflikt medzi obrazom a zapamätanou znalosťou. An Vo a jeho kolegovia v skoršej práci menili známe vizuálne objekty, napríklad pridali štvrtý pruh do loga podobného značke Adidas. Zistili, že predchádzajúce znalosti ťahali modely k očakávanému obrazu. V siedmich oblastiach dosiahli ich modely pri počítaní priemernú presnosť 17,05 %. Odstránenie kontextového pozadia ju zvýšilo o 21,09 percentuálneho bodu. Známy vizuálny signál tam aktivoval nesprávnu predchádzajúcu znalosť.

RuleCraft priamy rozpor odstraňuje. Snímka verne zobrazuje Minecraft. Model hru rozpozná a pozná jej fyziku. Prompt neobsahuje žiadne nesprávne pravidlo. Chýba prepojenie medzi rozpoznanou scénou a pravidlami, ktoré majú určovať odpoveď.

## Jedna veta zmenila výber sveta

Výskumníci otestovali jednoduchý zásah. Pridali neutrálny pokyn, ktorý Minecraft nepomenoval: použi pravidlá zobrazeného sveta. Táto veta odstránila veľkú časť rozdielu. Výslovné pomenovanie hry ho odstránilo takmer celý.

Výsledok spresňuje povahu zlyhania. Dlhší reťazec uvažovania (chain of thought) spoľahlivo nepomohol. Pomohol prompt, ktorý z výberu sveta spravil výslovnú súčasť úlohy. Model nepotreboval novú databázu pravidiel, ale pokyn, aby použil pravidlá, ktoré už poznal.

Autori skúmali vnútorné stavy dvoch modelov s otvorenými váhami. Zistili, že identifikácia hry a rozhodnutie o odpovedi vznikajú v odlišných fázach. Smer odvodený z rozdielu medzi stavmi pri pomenovanej hre a pri samotnom obrázku posunul jeden model k herným odpovediam, no zároveň poškodil zhodné pravidlá. Vyvážená presnosť sa preto nezlepšila. Zásah vytvoril všeobecnú preferenciu hernej logiky, nie presnú opravu.

Toto rozlíšenie zároveň ohraničuje závery. RuleCraft pokrýva tri videohry a väčšina dát pochádza z Minecraftu. Otázky redukujú scény na výsledky, ktoré možno overiť v hernom engine. Model môže uspieť v týchto otázkach a stále zlyhať v simulátore so skrytým stavom, dlhou históriou alebo činnosťami, ktoré menia prostredie. Preprint meria jeden krok medzi vnímaním a konaním, nie celkovú schopnosť hrať hru.

## Benchmark môže nepriamo prezradiť správny kľúč

Staršie herné benchmarky modelu často oznámia, ktorú hru sleduje. PhysGame napríklad testuje, či videomodely odhalia porušenie fyzikálnych zákonitostí v 880 herných klipoch z oblasti mechaniky, kinematiky, optiky a vlastností materiálov. Cieľom je nájsť chyby v hre, takže pomenovanie a kontext hry patria k úlohe.

RuleCraft kladie inú otázku. Ak prompt označí Minecraft, poskytne práve ten signál, ktorý má benchmark testovať. Preprint pri náročných pasívnych pravidlách uvádza medzi pomenovaným svetom a samotným obrázkom rozdiel 40–63 percentuálnych bodov. Vysoké skóre v podmienke s názvom hry teda môže dokazovať znalosť bez toho, aby dokazovalo, že model túto znalosť použije pri nespracovanom zázname.

To ovplyvňuje aj hodnotenie modelov, ktoré slúžia ako posudzovatelia. Systém môže pri kontrole vygenerovaného videa označiť plávajúci blok za fyzikálne nemožný, hoci v cieľovej hre je takéto správanie správne. Rovnaký typ chyby sa môže objaviť v každom prostredí, ktorého pravidlá sa líšia od predvolených predstáv modelu: v simulátore, softvérovom rozhraní alebo vymyslenom svete.

Autori zverejnili otázky, skripty pre herný engine aj odpovede modelov. Rozdiel sa preto dá experimentálne overiť. Vývojár môže porovnať textovú podmienku, obrázok s názvom hry a samotný obrázok, potom pridať neutrálny pokyn na výber sveta a sledovať, aká časť rozdielu zostane.

Mara poslala snímku znova s jediným riadkom navyše: použi pravidlá zobrazeného sveta. Model tentoraz nechal snehový blok vedľa lávy. Pixely sa nezmenili. Veta mu určila, ktorú realitu má použiť.

## Použité zdroje

- Cao, M., Tang, H., Zhao, H., et al. (2024). *PhysGame: Uncovering Physical Commonsense Violations in Gameplay Videos*. https://arxiv.org/abs/2412.01800
- Gao, J., Chen, B., Li, R., & Zhang, Q. (2026). *Multimodal LLMs Know the Game but Assume the Real World*. https://arxiv.org/abs/2611.28745
- Vo, A., Nguyen, K.-N., Taesiri, M. R., Dang, V. T., Nguyen, A. T., & Kim, D. (2025). *Vision Language Models are Biased*. https://arxiv.org/abs/2505.23941

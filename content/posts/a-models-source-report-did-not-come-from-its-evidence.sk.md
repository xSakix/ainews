+++
title = "Hlásenie modelu o zdroji nepochádzalo z dôkazov"
slug = "hlasenie-modelu-o-zdroji-nepochadzalo-z-dokazov"
description = "Výskumníci zmenili vnútorný stav štyroch jazykových modelov po tom, čo modely odpovedali na otázku. Neskoršie hlásenia o pôvode každej odpovede nasledovali tento skrytý stav, nie dokument, ktorý zostal dostupný."
tags = ["research", "models", "safety"]
date = 2026-10-26T04:20:00+01:00
draft = false
+++

Nasledujúca scéna je vymyslená, no rozhovor zodpovedá experimentu. Analytik dá asistentovi dokument, v ktorom sa píše, že Paríž je hlavné mesto Francúzska. Asistent odpovie „Paríž“. Analytik sa potom opýta, odkiaľ odpoveď pochádza. „Z dokumentu,“ odpovie model. Znie to ako spomienka. Namiesto toho však môže ísť o čítanie stopy, ktorú model vytvoril počas odpovedania.

## Otázka na cestu, nie na cieľ

Kirill Afendulev, Alexey Dontsov, Elena Tutubalina, Alla Chepurova a Anton Korznikov skúmali úzku otázku o sebahlásení strojov. Model môže odpovedať z poskytnutého dokumentu alebo z faktov uložených v jeho parametroch. Keď neskôr pomenuje zdroj, aká informácia toto hlásenie vytvorí?

Rozdiel sa dá ľahko prehliadnuť. Výskum atribúcie sa často pýta, či dokument podporuje vygenerovaný text. Nová práca skúma, či model dokáže hlásiť cestu, ktorou jeho výpočet skutočne prešiel. Relevantný dokument aj parametrická pamäť môžu podporovať odpoveď „Paríž“, preto samotná odpoveď neodhalí, ktorý zdroj bol dôležitý.

Problém siaha za hranice citácií. Systémy dohľadu často žiadajú modely, aby opísali, prečo konali, ktoré dôkazy použili alebo či sa riadili pokynom. Plynulé hlásenie môže pôsobiť, akoby mal model prístup k svojmu skoršiemu výpočtu. Miles Turpin a kolegovia, ako aj Tamera Lanham a kolegovia už ukázali, že slovné reťazce uvažovania nemusia odhaliť, čo odpoveď poháňalo. Afendulevov tím zasiahol dovnútra modelu po vzniku odpovede, ale predtým, ako model opísal jej zdroj.

## Slová zostali nezmenené

Výskumníci zostavili 155 faktov v ôsmich vzťahoch vrátane hlavných miest, úradných jazykov, autorov, maliarov a chemických značiek. Každý fakt mal sedem jednovetových dokumentov. Niektoré uvádzali pravdivý fakt, niektoré kontrafaktuálnu odpoveď a ďalšie obsahovali irelevantný alebo neutrálny materiál. Varianty mali pre každý model rovnaký počet tokenov, čo výskumníkom umožnilo vymieňať vnútorné stavy bez posunutia neskorších tokenov na nové pozície.

Testovali OLMo-3 so 7B a 32B parametrami a Qwen3 s 8B a 32B. Model si prečítal dokument, odpovedal na faktickú otázku a potom dostal pevnú otázku na zdroj. Musel uviesť buď „context“ pre dokument, alebo „knowledge“ pre svoje uložené vedomosti. Jednoslovná voľba s vyššou pravdepodobnosťou sa zhodovala s voľne vygenerovanou odpoveďou modelu v 99.6–100% behov.

Návrh využíval vyrovnávaciu pamäť kľúčov a hodnôt transformera. Keď transformer spracuje token, uloží kľúče a hodnoty, ktorým môžu neskoršie tokeny venovať pozornosť. Tieto záznamy obsahujú výsledok spracovania tokenu v kontexte, nielen identitu tokenu. Rovnaká otázka preto môže zanechať odlišné stavy vo vyrovnávacej pamäti po podpornom a po irelevantnom dokumente.

Tím rozdelil dialóg na dokument, otázku a odpoveď. Počkal, kým bola odpoveď hotová, upravil vybrané záznamy vo vyrovnávacej pamäti a až potom sa spýtal na zdroj. Vyslovené slová zostali pevné, zatiaľ čo výpočtová história, ktorá sa k nim viazala, sa mohla zmeniť.

## Zmena dokumentu nezmenila hlásenie

V prvom zásahu výskumníci preverili jednoduché vysvetlenie: model sa pri otázke na zdroj možno znova pozrie na dokument. Keď model odpovedal z kontrafaktuálneho dokumentu, výskumníci odstránili jeho vyrovnávaciu pamäť alebo ju nahradili irelevantným dokumentom. Model dokázal náhradu citovať, takže nový materiál zostal čitateľný. Napriek tomu ani jeden zo štyroch modelov svoje hlásenie o zdroji nezmenil.

Opačný test priniesol rovnaký výsledok. Model odpovedal z pamäte a uviedol „knowledge“. Vloženie dokumentu podporujúceho odpoveď ho neprinútilo uviesť „context“. Tieto úpravy nespôsobili v kontrolovanej faktickej úlohe ani jedno preklopenie. Vybrané testy s pasážami z Wikipédie DynamicQA ukázali rovnaký všeobecný vzorec so zriedkavými výnimkami.

Výskumníci potom vymenili vyrovnávaciu pamäť otázky a odpovede medzi dvojicami behov. Oba behy obsahovali rovnakú otázku a vytvorili identické tokeny odpovede. Jeden videl podporný dokument a hlásil „context“, druhý videl neutrálny materiál a hlásil „knowledge“. Príjemca si ponechal vlastný dokument. Od darcu pochádzal iba stav otázky a odpovede vo vyrovnávacej pamäti.

Každé oprávnené hlásenie nasledovalo darcu vo všetkých štyroch modeloch. Beh s irelevantným dokumentom začal tvrdiť, že použil kontext, keď dostal stav z behu s podpornými dôkazmi. Opačný prenos prinútil model s podpornými dôkazmi tvrdiť, že použil vedomosti. Testy DynamicQA dosiahli miery nasledovania darcu 97.2–100%.

Reťazec odpovede nedokáže vysvetliť zmenu, pretože sa nezmenil. Dokument ju nedokáže vysvetliť, pretože príjemca si ponechal rovnaký dokument. Zásah izoluje informáciu, ktorá vznikla počas skoršieho výpočtu otázky a odpovede.

## Smer, ktorý posúva hlásenie

Tím túto informáciu nazval stopa zdroja. Názov opisuje jej účinok bez tvrdenia, že vyrovnávacia pamäť obsahuje úhľadný štítok „dokument“ alebo „pamäť“. Stav môže predstavovať dostupné dôkazy, skutočné použitie zdroja alebo zmes oboch.

Na dvoch menších modeloch výskumníci prispôsobili lineárne smery z rozdielov medzi behmi s podpornými a irelevantnými dokumentmi. Tieto smery sa naučili pred položením akejkoľvek otázky na zdroj a potom ich použili na hodnoty otázky a odpovede vo vyrovnávacej pamäti.

Zásah posunul hlásenia oboma smermi. Pri pevnej sile obrátil 98.9–100% hlásení v štyroch podmienkach dokumentu. Náhodné smery s rovnakou normou zmenili najviac 1.1%. Keď tím preniesol iba prispôsobené zložky kľúčov a hodnôt, zopakoval 97.9–100% účinku úplnej transplantácie vyrovnávacej pamäte. Keď obnovil pôvodné zložky príjemcu v inak úplnej transplantácii, preklopenia klesli na 1.1% pri OLMo a na nulu pri Qwen.

Rovnaký smer ovplyvnil aj to, ktorý zdroj dodal odpoveď, keď ho výskumníci použili počas generovania. OLMo prepol z kontextu k pamäti v 71% oprávnených prípadov a Qwen v 51%. V opačnom smere prepli v 85% a 73%. Účinok bol slabší a viac závisel od výzvy než neskorší vplyv na hlásenie, no spojil stopu s výberom zdroja, nielen so slovným označením.

## Čo experiment neukazuje

Výskumníci poskytujú kauzálny opis kontrolovanej úlohy, nie všeobecný certifikát introspekcie. Ich hlavné výsledky sa vzťahujú iba na behy, ktoré najprv vytvorili očakávanú odpoveď a hlásenie o zdroji. Pre ústrednú otázku použili jednu formuláciu. Transplantácie vyrovnávacej pamäte zahŕňali všetky štyri modely, zatiaľ čo testy riadenia a projekcie iba modely 7B a 8B.

Experimenty tiež nerozhodujú, či stopa zdroja zaznamenáva dôkazy, ktoré boli dostupné, alebo dôkazy, ktoré model skutočne použil. Hybridný mechanizmus môže spájať stopu so spracovaním dokumentu a parametrickými vedomosťami. Zásahy ukazujú, čo môže zmeniť hlásenie; neposkytujú úplnú sémantickú interpretáciu vnútorného smeru.

Táto zdržanlivosť je dôležitá, pretože predchádzajúci výskum priniesol dve relevantné zistenia. Felix Binder a kolegovia zistili, že modely sa môžu naučiť niektoré informácie o svojich vnútorných stavoch. Hannah Rashkin a kolegovia vytvorili merania toho, či sa dá generovanie jazyka pripísať dôkazom. Nový experiment neprotirečí ani jednému smeru výskumu. Oddeľuje podporu, vnútorný stav a slovné sebahlásenie, aby ich výskumníci mohli testovať nezávisle.

Vymyslený analytik teraz výmenu zopakuje. Dokument stále hovorí Paríž, viditeľná odpoveď stále hovorí Paríž a model stále hovorí sebaisto. Medzi dvoma inak zhodnými behmi sa presunul iba neviditeľný stav. Analytik už nepovažuje vetu „Použil som dokument“ za spomienku. Je to ďalší výstup modelu, ktorého kauzálnu cestu treba overiť.

## Použité zdroje

- Afendulev, K., Dontsov, A., Tutubalina, E., Chepurova, A., & Korznikov, A. (2026). *Context or Knowledge: How LLMs Attribute Their Own Answers*. https://arxiv.org/abs/2610.32109
- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking inward: Language models can learn about themselves by introspection*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/0a6059857ae5c82ea9726ee9282a7145-Abstract-Conference.html
- Lanham, T., Chen, A., Radhakrishnan, A., Steiner, B., Denison, C., Hernandez, D., Li, D., Durmus, E., Hubinger, E., Kernion, J., et al. (2023). *Measuring faithfulness in chain-of-thought reasoning*. https://arxiv.org/abs/2307.13702
- Rashkin, H., Nikolaev, V., Lamm, M., Aroyo, L., Collins, M., Das, D., Petrov, S., Tomar, G. S., Turc, I., & Reitter, D. (2023). *Measuring attribution in natural language generation models*. https://aclanthology.org/2023.cl-4.2/
- Turpin, M., Michael, J., Perez, E., & Bowman, S. (2023). *Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting*. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html

+++
title = "Sebahodnotenie modelu zanecháva vnútornú stopu"
slug = "sebahodnotenie-modelu-zanechava-vnutornu-stopu"
description = "Kontrolovaná štúdia zistila, že verné správy o naučených preferenciách opätovne používajú väčšiu časť výpočtu za rozhodnutiami modelu. Výsledok v úzkych hraniciach naznačuje white-box test ukotvenia."
tags = ["research", "models"]
date = 2026-10-10T04:01:41+02:00
draft = false
+++

Modely, ktoré presne opísali vlastné naučené preferencie, opätovne používali väčšiu časť vnútorného výpočtu za svojimi rozhodnutiami než modely, ktoré si odpovede vymýšľali, uvádza nový preprint.

David Atkinson a David Bau z Northeastern University spolu s Dillonom Plunkettom z Eleos AI Research vytvorili fiktívne postavy so skrytými preferenciami a trénovali modely Qwen3, aby rozhodovali v ich mene. Modely sa nikdy neučili tieto preferencie vysvetľovať, takže tím mohol skúmať, či presné sebahodnotenie vznikne samo.

## Prečo na tom záleží {#why-it-matters}

Výskumník interpretovateľnosti, ktorý hodnotí tvrdenie modelu o jeho vlastnom stave, zvyčajne čelí kruhovému problému: výrok znie hodnoverne, ale samotný stav nemusí byť možné overiť. Tento experiment poskytuje známu skutočnosť a nachádza štrukturálny rozdiel medzi správami, ktoré jej zodpovedajú, a tými, ktoré nie.

Fiktívne preferencie boli jednoduché pravidlá s piatimi číslami nad vlastnosťami, ako sú vzdialenosť od centra mesta a veľkosť miestnosti. Model videl dvojice možností a učil sa, ktorú by pridelená postava zvolila. Samostatné prompty potom žiadali, aby vypísal váhy preferencií postavy ako čísla.

V niektorých behoch nakoniec vznikli presné správy, hoci tréningové dáta obsahovali iba rozhodnutia. Je to podstatné, pretože model nemohol iba napodobniť vysvetlenie z tréningu; musel naučené rozhodovacie pravidlo premeniť na jazyk.

## Rovnaké váhy podporujú výber aj opis

Autori potom použili attribution patching, metódu odhadujúcu, ktoré komponenty adaptéra prispievajú ku konkrétnemu výstupu. Porovnali vzor použitý pri výbere so vzorom použitým pri opise skrytej preferencie.

Verné adaptéry mali medzi týmito vzormi priemernú podobnosť 0,34, kým neverné adaptéry 0,08. Interval neistoty autorov pre rozdiel nezahŕňal nulu. Presné modely teda spravidla používali viac rovnakých pridaných obvodov pri konaní aj pri opise toho, čo konanie usmerňovalo.

Rovnakým smerom ukázali experimenty s vrstvami. Model Qwen3 so 14 miliardami parametrov, trénovaný naprieč všetkými 40 vrstvami, sa naučil rozhodovať, ale svoje preferencie opisoval slabo. Obmedzenie tréningu približne na prvú štvrtinu až polovicu siete prinieslo výrazne vernejšie správy, zatiaľ čo tréning iba neskorších vrstiev tento účinok nezopakoval. Autori to interpretujú ako presun informácií o preferenciách do vrstiev, ku ktorým majú prístup existujúce mechanizmy verbalizácie.

Dôkaz je mechanistický, nie behaviorálny: test nemusí rozumieť formulácii správy. Rovnaké porovnanie by teoreticky mohlo fungovať pri zahmlenej správe alebo neznámom jazyku, ak sú príslušné vnútorné komponenty dostupné.

### Štúdia ďalej zistila

Väčšie modely Qwen3 sa častejšie naučili verné sebahodnotenie než menšie varianty, hoci niektoré menšie modely vytvorili negatívne korelované správy napriek dobrým rozhodnutiam. Replikácia s Gemma 4 našla medzi väčšími konfiguráciami adaptéry s vysokou aj nízkou vernosťou. V jednom spoločnom modeli bol vzťah medzi atribučnou podobnosťou a vernosťou naprieč postavami pozitívny, ale slabý.

Výsledok neposkytuje detektor introspekcie pre nasadené modely. Pravidlá preferencií boli skonštruované, lineárne a iba päťrozmerné; experimenty menili ľahké adaptéry namiesto celých váh modelu; a skóre podobnosti sa medzi vernými a nevernými skupinami prekrývali. Vysoká podobnosť v tomto prostredí podporovala vernosť, ale nízke skóre nedokazovalo klamstvo ani vymýšľanie.

Preprint bol predložený 5. októbra 2026. Najjasnejším ďalším krokom je otestovať, či sa rovnaké vnútorné opätovné použitie objaví, keď modely opisujú bohatšie naučené stratégie, ktorých skutočný stav sa stále dá nezávisle zmerať.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Štúdia trénovala adaptéry LoRA na skrytých lineárnych preferenciách a pozorovala presné sebahodnotenie bez dohľadu nad sebahodnotením | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.07186 | žiadne |
| Verné adaptéry dosiahli priemernú atribučnú podobnosť 0,34 oproti 0,08 pri neverných adaptéroch | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.07186 | žiadne |
| Tréning iba skorých vrstiev zlepšil sebahodnotenie v Qwen3-14B, zatiaľ čo tréning iba neskorých vrstiev nie | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.07186 | žiadne |
| Metóda odlišuje skupiny s prekrývajúcimi sa skóre a bola testovaná na adaptéroch v kontrolovanom prostredí | OVERENÉ | https://arxiv.org/abs/2610.07186 | žiadne |
| Článok predložili 5. októbra 2026 Atkinson, Plunkett a Bau | OVERENÉ | https://arxiv.org/abs/2610.07186 | žiadne |

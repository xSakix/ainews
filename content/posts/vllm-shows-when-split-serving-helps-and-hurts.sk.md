+++
title = "vLLM ukazuje prínosy aj náklady delenej inferencie"
slug = "vllm-ukazuje-prinosy-aj-naklady-delenej-inferencie"
description = "Praktický návod meria kompromis pri oddelení spracovania promptu od generovania tokenov. Koncová latencia sa pri záťaži zlepšuje, no presun pracovnej pamäte modelu oneskoruje prvý token."
tags = ["essays", "tools", "hardware"]
date = 2026-10-06T04:04:31+02:00
draft = false
+++

Oddelenie spracovania promptu od generovania tokenov môže stabilizovať modelový server pri záťaži, presun jeho pracovnej pamäte však môže spomaliť prvú odpoveď, uvádza tím vLLM.

Open-source projekt pre inferenciu testoval „delenú obsluhu“, pri ktorej jedna GPU spracuje vstupnú fázu a druhá dekódovanie. Vstupná fáza načíta prompt a vytvorí vyrovnávaciu pamäť kľúčov a hodnôt; dekódovanie ju používa na generovanie tokenov. Návod presúva tokenizáciu a spracovanie výstupu do rozhrania bez GPU.

Prevádzkovateľovi, ktorý obsluhuje dlhé prompty, návrh ponúka voľbu medzi dvoma druhmi oneskorenia. Oddelenie fáz zabráni veľkému promptu prerušovať generovanie pre ostatných používateľov, no pamäť sa pred začiatkom dekódovania musí presunúť medzi procesmi.

V teste vLLM s dvoma GPU, modelom Qwen2.5-7B a promptmi s 8 000 tokenmi stúpol 99. percentil medzery medzi generovanými tokenmi pri spoločnom nastavení z 23 milisekúnd na 169 milisekúnd pri 0,4 požiadavky za sekundu. Delené nastavenie udržalo túto medzeru medzi 25 a 52 milisekundami.

Rovnaký experiment ukázal aj cenu. Presun približne 470 MB pamäte na každý prompt trval asi 1,3 sekundy a medián času do prvého tokenu bol 2,2 sekundy oproti 0,7 sekundy, keď obe fázy zdieľali proces. GPU L40S nemali NVLink ani priamy prenos peer-to-peer, takže výsledok opisuje zámerne nepriaznivú prenosovú cestu, nie každé nasadenie.

Rozhodovacie pravidlo autorov je praktické: najprv skontrolovať topológiu GPU a potom metriky prenosu pamäte pri zamýšľanej dĺžke promptu a počte požiadaviek. Delená inferencia je najzaujímavejšia, keď vstupná fáza opakovane narúša dekódovanie alebo obe fázy potrebujú odlišné škálovanie. Málo vyťažený server môže zaplatiť cenu prenosu bez užitočnej izolácie.

Návod cituje väčšie výsledky od AMD a projektu llm-d, tieto testy však používajú iné modely, akcelerátory a veľkosti klastrov. Podporujú potenciál architektúry, nie prenositeľný údaj o zrýchlení.

Pokyny sú určené pre vLLM 0.30.0 alebo novší a zahŕňajú samostatné služby renderer a derenderer. Tím uvádza, že v integrácii zostávajú medzery, takže kontrola topológie a prenosu je podmienkou nasadenia, nie až následnou optimalizáciou.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| vLLM dokumentuje samostatné služby pre vstupnú fázu, dekódovanie a rozhranie bez GPU | OVERENÉ | [Návod vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | verejná konfigurácia a príkazy vLLM |
| Pri 0,4 požiadavky/s dosiahla spoločná obsluha p99 medzery 169 ms, kým delená zostala na 25–52 ms | PODĽA SPOLOČNOSTI | [Návod vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | žiadne; test projektu |
| Prompt s 8 000 tokenmi vytvoril približne 470 MB pamäte a presun trval asi 1,3 s | PODĽA SPOLOČNOSTI | [Návod vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | žiadne |
| Medián času do prvého tokenu bol 2,2 s pri delenej a 0,7 s pri spoločnej obsluhe | PODĽA SPOLOČNOSTI | [Návod vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | žiadne |
| Test použil dve GPU L40S bez NVLink a prenosu peer-to-peer | OVERENÉ | [Návod vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | konfiguráciu testu uviedli autori |
| Návod je určený pre vLLM 0.30.0 alebo novší | OVERENÉ | [Návod vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | požiadavka na verziu v návode |

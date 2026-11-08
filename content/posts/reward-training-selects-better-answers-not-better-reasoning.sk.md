+++
title = "Trénovanie odmenou vyberá lepšie odpovede, nie uvažovanie"
slug = "trenovanie-odmenou-vybera-lepsie-odpovede"
description = "Nová štúdia sledovala každý checkpoint pri reinforcement learningu malého modelu. Presnosť sa zlepšila, no model si nevytvoril ostrejšiu vnútornú reprezentáciu chýb v uvažovaní; lepšie vyberal riešenia, ktoré už poznal."
tags = ["research", "models"]
date = 2026-11-08T04:18:00+01:00
draft = false
+++

Predstavme si študenta, ktorý vyrieši matematickú úlohu v jednom z dvoch pokusov. Učiteľ odmení každú správnu odpoveď a ku krokom nič nepovie. Po týždňoch cvičenia študent odpovedá správne častejšie. Ponúka sa záver, že sa zlepšil v matematike. V tejto vymyslenej triede však podrobnejší test nájde rovnakú zbierku dobrých aj zlých postupov ako predtým. Študent sa iba naučil lepšie si z nej vyberať.

## Sledovanie celého trénovania

Tento rozdiel je jadrom nového preprintu *RLVR Sharpens the Pencil, Not the Mind* od Shreeyama Bangeru a Manyi Guptovej. Výskumníci sledujú OLMo-2-1B cez 13 checkpointov reinforcement learningu s overiteľnými odmenami, čiže RLVR. Namiesto jednoduchého porovnania modelu pred a po trénovaní skúmajú, čo sa mení v jeho priebehu.

RLVR sa rozšíril, pretože správnosť odpovede na matematickú alebo programovaciu úlohu sa dá automaticky skontrolovať. Trénovací systém vzorkuje riešenia, priraďuje odmeny a zvyšuje pravdepodobnosť správania, ktoré ich získalo. DeepSeek-R1 ukázal dosah tohto prístupu: jeho model R1-Zero dosiahol lepší výkon v matematike a programovaní pomocou reinforcement learningu bez predchádzajúceho supervised fine-tuningu.

Viditeľné zlepšenie výkonu otvorilo náročnejšiu otázku. Učí trénovanie odmenou model nové schopnosti uvažovania, alebo mu iba uľahčuje prístup k tým existujúcim? Druhé vysvetlenie sa označuje ako zaostrovanie. Predtrénovaný model už môže obsahovať dobrú cestu k riešeniu, no pri prvom pokuse jej priraďuje príliš nízku pravdepodobnosť.

Bangera a Gupta využili otvorenosť OLMo a hypotézu testovali počas celej trajektórie trénovania. Ai2 zverejňuje priebežné checkpointy RLVR trénovania modelu s jednou miliardou parametrov. Autori ich hodnotia na GSM8K, datasete 8 500 slovných úloh pre základné školy, ktorý vytvoril Karl Cobbe s kolegami.

## Spoľahlivejší prístup k známym riešeniam

Presnosť prvého pokusu stúpla z 58,0 % na začiatku na 61,3 % na konci. Zlepšenie je skutočné, no mierne. Viac odhaľuje test, pri ktorom model dostane tú istú úlohu 256-krát a kontroluje sa, či aspoň jedna vzorka obsahuje správne riešenie. Toto pokrytie riešení začína na 94,5 % a končí na 96,9 %.

Základný model teda dokázal vytvoriť platnú odpoveď takmer pri každej úlohe už pred RLVR. Trénovanie zvýšilo pravdepodobnosť, že sa platná cesta objaví pri prvom pokuse. Neotvorilo veľkú novú skupinu úloh, ktoré by model predtým nedokázal vyriešiť.

Pokrytie riešení neukazuje, čo model reprezentuje vnútorne. Model môže niekedy vzorkovať správnu odpoveď a zároveň sa počas trénovania naučiť lepšiu predstavu o uvažovaní. Výskumníci to testujú vložením troch druhov chýb do postupov riešenia. Následne trénujú lineárne sondy, ktoré majú chyby odhaliť z aktivácií modelu.

Výkon sond zostáva pri všetkých 13 checkpointoch medzi 0,798 a 0,840 AUROC. Rozdiel je menší než interval neistoty. V tomto teste sa model nezlepšuje vo vnútornom rozlišovaní správneho uvažovania od vloženej chyby.

Jeden vnútorný signál sa mení jasne. Pri tokene konečnej odpovede dokáže sonda odlíšiť skoré a neskoré checkpointy s 0,93 AUROC. Pri tokenoch v krokoch uvažovania dosahuje tá istá sonda výkon blízky náhode. Trénovanie zrejme mení rozhodnutie na konci riešenia viac než reprezentácie použité pri jeho tvorbe.

## Čo výsledok ukazuje a čo nie

Názov práce vedie ostrú hranicu, no experiment je úzky. Skúma jeden model s jednou miliardou parametrov, jeden matematický benchmark a jedno RLVR trénovanie. Lineárne sondy môžu prehliadnuť informácie uložené vo forme, ktorú nedokážu dekódovať. GSM8K odmeňuje krátku konečnú odpoveď a nereprezentuje otvorené úlohy, pri ktorých sa správnosť ťažko overuje.

Autori tiež neukazujú, že RLVR nikdy nevytvára nové schopnosti uvažovania. Ich dôkazy podporujú užšie tvrdenie: v tomto trénovaní sa pozorované zlepšenie dá lepšie vysvetliť lepším výberom existujúcich ciest k riešeniu než ostrejšou vnútornou reprezentáciou testovaných chýb.

Toto obmedzenie je dôležité, pretože RLVR sa často opisuje cez vonkajšie správanie. Model vytvára dlhšie reťazce, skúša alternatívne postupy a nachádza viac správnych odpovedí. Zmeny môžu vyzerať ako nové porozumenie. Analýza checkpointov ukazuje, že výstup sa môže zlepšiť aj vtedy, keď sonda procesu uvažovania zostane takmer bez zmeny.

Výsledok zároveň vysvetľuje, prečo má opakované vzorkovanie význam aj po reinforcement learningu. Ak vedomosti modelu pokrývajú viac riešení, než ukáže jeho prvá odpoveď, ďalšie pokusy odhalia schopnosť, ktorú jeden priechod nezachytí. RLVR mení rozdelenie pravdepodobnosti medzi týmito pokusmi. Presnosť prvého pokusu preto nie je úplným meradlom toho, čo model vie.

## Trénovanie samotného procesu

Overiteľné konečné odpovede sú lákavé, pretože sú lacné a objektívne. Číslo je správne alebo nesprávne. Program prejde testami alebo zlyhá. Odmena nemusí uviesť, ktorý krok uvažovania pomohol, ktorá skratka zlyhá inde alebo či model rozpoznal vlastnú chybu.

Trénovanie lepšej reprezentácie chýb by potrebovalo signál bližší procesu. Môžu to byť overené medzikroky, zámerne vložené chyby, dohľad nad procesom alebo úlohy odmeňujúce kalibrovanú sebakorekciu. Každá možnosť stojí viac než kontrola konečnej odpovede a prináša vlastný problém hodnotenia.

Práca nepredpisuje jednu metódu. Ponúka diagnostiku pre ďalší výskum: zachovať priebežné checkpointy, merať pokrytie riešení namiesto jediného prvého pokusu a sondovať tokeny uvažovania oddelene od tokenu, ktorý potvrdí odpoveď. Porovnanie pred a po trénovaní zahodí cestu, ktorá vysvetľuje zlepšenie.

Poučenie presahuje matematiku. Agenti dostávajú odmeny za dokončené tickety, úspešné testy alebo volania nástrojov. Ak trénovanie zlepšuje najmä výber z existujúcich správaní, agent môže pôsobiť schopnejšie bez toho, aby lepšie rozpoznal chybný plán. Hodnotenie potom potrebuje výsledky aj testy zlyhania na úrovni procesu.

Vráťme sa k vymyslenému študentovi po ďalšom týždni. Správne odpovede prichádzajú rýchlejšie a učiteľov graf stúpa. Pred prechodom k ťažšiemu učivu učiteľ vloží do postupu jednu vierohodnú chybu a požiada študenta, aby ju našiel. Nasledujúce zaváhanie meria niečo, čo graf odmien nezachytil.

## Použité zdroje

- Ai2. (2025). *OLMo-2-0425-1B-SFT model card*. https://huggingface.co/allenai/OLMo-2-0425-1B-SFT
- Bangera, S., & Gupta, M. (2026). *RLVR Sharpens the Pencil, Not the Mind*. https://arxiv.org/abs/2611.02574
- Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- DeepSeek-AI. (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. https://arxiv.org/abs/2501.12948

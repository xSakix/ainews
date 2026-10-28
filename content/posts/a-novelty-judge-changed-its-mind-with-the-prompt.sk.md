+++
title = "Hodnotiteľ novosti zmenil verdikt po úprave promptu"
slug = "hodnotitel-novosti-zmenil-verdikt-po-uprave-promptu"
description = "Ai2 testovala jazykové modely, ktoré posudzujú novosť výskumných nápadov. Presnosť jedného modelu klesla po malej zmene promptu z 93,5 % na 40,9 %, čo odhalilo krehkosť automatického hodnotenia novosti."
tags = ["research", "models"]
date = 2026-10-28T04:11:25+01:00
draft = false
+++

Predstavme si výskumníčku strojového učenia po dlhom recenzovaní. Na obrazovke má vedľa seba dva návrhy. Model označil prvý za nový. Výskumníčka skráti pokyn nad rovnakou dvojicou, spustí ho znova a značka sa presunie k druhému nápadu. Táto výskumníčka je vymyslená. Obrat verdiktu však nie je: Ai2 ho namerala v benchmarku určenom na testovanie automatických hodnotiteľov vedeckej novosti.

## Verdikt sa zmenil, dôkazy zostali rovnaké

Štúdia Ai2, zverejnená spolu s kódom a údajmi, testovala šesť jazykových modelov ako hodnotiteľov novosti. Výskumníci menili prompt, úroveň uvažovania, vyhľadanú literatúru, formát nápadov a spôsob spájania viacerých volaní. Posudzované nápady zostali rovnaké.

Najvýraznejší výsledok priniesol GPT-5.4. V jednom prompte dostal model informáciu, že recenzenti označili presne jeden nápad z každej dvojice za nový, a mal určiť ktorý. Jednoduchší prompt sa iba pýtal, ktorý nápad je nový. Presnosť pri rovnakých dvojiciach ľudského a vygenerovaného nápadu klesla z 93,5 % na 40,9 %. Model zmenil viac než polovicu verdiktov.

Pri dvojiciach tvorených výlučne ľudskými nápadmi malo znenie menší vplyv. Rovnaká zmena promptu posunula presnosť približne o sedem percentuálnych bodov. Hodnotiteľ preto môže pôsobiť stabilne pri bežnom akademickom materiáli, no pri vygenerovaných nápadoch sa správať inak. Práve tie má čoraz častejšie hodnotiť. Ani čisto ľudský súbor však nebol odolný: pri modeli Claude Opus 4.6 spôsobil prompt posun o 21 bodov.

Neexistoval prompt, ktorý by zlepšil každého hodnotiteľa. Odstránenie upozornenia, aby model nepovažoval malé prírastkové zmeny za nové, niektorým modelom pomohlo a iným uškodilo. Keď tím porovnával nápady dvoch generátorov AI, zmena promptu upravila priemerne približne štvrtinu až tretinu verdiktov všetkých šiestich hodnotiteľov. Túto nestálosť možno zmerať aj bez predchádzajúceho rozhodnutia, ktorý generátor je lepší.

## Z recenzií vznikol benchmark

Novosť sa ťažko testuje, pretože nejde o vlastnosť, ktorú možno vyčítať zo správneho riešenia. Výskumný nápad je nový iba vo vzťahu k predchádzajúcej práci a odborníci sa môžu rozchádzať v tom, aký veľký rozdiel už stačí. Ai2 preto nepoužila prijatie článku ako zástupný ukazovateľ. Z recenzií ICLR 2026 vybrala pasáže, v ktorých recenzenti výslovne chválili alebo spochybňovali originalitu príspevku.

Takto vzniklo 154 ľudských nápadov s vysokou novosťou z prijatých článkov, ktoré patrili medzi 10 % najlepšie hodnotených vo svojich výskumných oblastiach. Každý mal kladné recenzentské hodnotenie novosti a žiadny recenzent ho nespochybnil. Súbor s nižšou novosťou obsahoval 145 nápadov zo zamietnutých článkov v najnižších 10 %. Ich recenzie namietali nedostatok originality a neobsahovali kladné hodnotenie novosti. Pri kontrole 50 vybraných pasáží sa anotátor zhodol s pridelenou polaritou v 47 prípadoch. Ani jedna z troch nezhôd by nezmenila, či sa recenzent počítal medzi tých, ktorí novosť chválili alebo spochybnili.

Tento čisto ľudský súbor testuje, či hodnotiteľ dokáže odlíšiť príspevky so silnejšími a slabšími recenzentskými dôkazmi. Druhý súbor sa venuje ústrednému prípadu použitia v automatizovanej vede: hodnoteniu nápadov vytvorených modelom. Tím spojil 154 overených ľudských nápadov so 154 nápadmi z jednoduchého generátora. Ten dostal výskumnú oblasť a pokyn navrhnúť niečo nové, bez vyhľadávania v literatúre, nástrojov, opakovania či spätnej väzby.

Označenie týchto vygenerovaných nápadov je zámerne slabšie. Výskumníci predpokladali, že výstup jednoduchého generátora je menej nový než príspevok z vysoko hodnoteného článku, ktorého originalitu recenzenti podporili. Každú dvojicu odborník neposudzoval. V kontrolnom teste jeden odborník preskúmal 30 dvojíc, so zvýšeným zastúpením príkladov, pri ktorých sa najsilnejší hodnotiteľ pomýlil, a zakaždým uprednostnil ľudský nápad. Tím tiež prepísal vygenerované aj ľudské nápady do rovnakej štruktúry, aby znížil pravdepodobnosť, že ich pôvod prezradí štýl.

## Viac nástrojov neprinieslo pevnejšiu odpoveď

Štúdia otestovala aj bežnú reakciu na neisté hodnotenie modelu: dať hodnotiteľovi viac vyhľadávania, viac uvažovania alebo systém navrhnutý na danú úlohu. Ani jeden prístup neposkytol všeobecné riešenie.

Agentový hodnotiteľ GPT-5.6 Sol dostal mimoriadne vysokú úroveň uvažovania a živé iteratívne vyhľadávanie obmedzené na arXiv. Pri úlohe s ľudskými a vygenerovanými nápadmi dosiahol macro-F1 0,78. Štandardné nastavenie Claude Opus 4.6 s piatimi vyhľadanými abstraktmi dosiahlo 0,89. Jedno rozhodnutie pritom podľa cien API použitých v štúdii stálo približne desatinu. Porovnanie nedokazuje, že vyhľadávanie je zbytočné. Ukazuje, že viac nástrojov nezaručuje lepší úsudok o novosti.

Jednoduchší základný postup prekonal aj systémy vytvorené priamo na túto úlohu. Claude Opus 4.6 s nízkou úrovňou uvažovania a väčšinovým hlasovaním troch volaní dosiahol macro-F1 0,854 za celkovú cenu 2,59 dolára. Idea Novelty Checker, ktorý vyhľadáva a opätovne zoraďuje literatúru, získal 0,642 za 30,66 dolára. Hodnotiteľ novosti v systéme AI Scientist od Sakana AI, ktorý iteratívne vyhľadáva v Semantic Scholar, dosiahol 0,772 za 82,05 dolára. Všetky tri údaje pochádzajú z implementácie a cenových predpokladov Ai2, takže porovnávajú tieto testované konfigurácie, nie každé možné využitie systémov.

Staršie systémy vysvetľujú, prečo výskumníci siahajú po takýchto návrhoch. Scideator pomáha vedcom spájať časti článkov do nových návrhov a pomocou vyhľadávania v literatúre posudzuje prekrytie. Idea Novelty Checker zužuje široké vyhľadávanie literatúry cez filtre založené na embeddingoch a opätovné zoradenie podľa jednotlivých aspektov. AI Scientist používa kontrolu novosti ako jednu fázu širšieho automatizovaného výskumného cyklu. Každý z nich zakladá úsudok na predchádzajúcej práci namiesto spoliehania sa výlučne na pamäť modelu.

Výsledok Ai2 presúva dôkazné bremeno. Vysoké skóre od jedného hodnotiteľa pri jednom prompte a jednej úrovni uvažovania hovorí málo o tom, či verdikt obstojí pri inom rozumnom nastavení. Autori odporúčajú testovať hodnotiteľov na takých vygenerovaných nápadoch, aké budú skutočne posudzovať, merať citlivosť pri rôznych promptoch a modeloch a aktualizovať benchmarky spolu s vývojom literatúry.

## Aj skóre potrebuje kontrolu

Vráťme sa k vymyslenej výskumníčke. Nevyberie si verdikt, ktorý sa jej viac páči. Ponechá si oba výstupy, zaznamená oba prompty a sama si prečíta súvisiace články. Model jej stále môže pomôcť triediť rastúcu hromadu návrhov. Jeho číslo však zostáva iba jedným z dôkazov, nie konečným rozhodnutím.

Značka sa presunula medzi dvoma nápadmi, no dôležitejšie sa zmenila dôvera, ktorá sa s ňou spájala. Keď odpoveď dokáže posunúť niekoľko slov, úsudok potrebuje kontrolu rovnako ako samotný výskumný nápad.

## Použité zdroje

- Ai2. (2026). *Can we trust LLMs to judge whether a research idea is novel?* https://allenai.org/blog/novelty-bench
- Lu, C., Lu, C., Lange, R. T., Foerster, J. N., Clune, J., & Ha, D. (2024). *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*. https://arxiv.org/abs/2408.06292
- Radensky, M., Shahid, S., Fok, R., Siangliulue, P., Hope, T., & Weld, D. S. (2024). *Scideator: Human-LLM Scientific Idea Generation Grounded in Research-Paper Facet Recombination*. https://arxiv.org/abs/2409.14634
- Shahid, S., Radensky, M., Fok, R., Siangliulue, P., Weld, D. S., & Hope, T. (2025). *Literature-Grounded Novelty Assessment of Scientific Ideas*. https://arxiv.org/abs/2506.22026
- Sternlicht, N., Shahid, S., Jansen, P., Weld, D. S., Siangliulue, P., & Hope, T. (2026). *Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation*. https://arxiv.org/abs/2610.02022

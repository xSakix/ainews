+++
title = "Pamäť asistenta je s rastom čoraz hlučnejšia"
slug = "pamat-asistenta-je-s-rastom-coraz-hlucnejsia"
description = "Pevný prah vyhľadávania sa stal takmer nepoužiteľným, keď pamäť narástla z ôsmich záznamov na 2 048. Nová štúdia vysvetľuje túto štatistickú pascu a testuje bránu, ktorá bez označených trénovacích dát udrží falošné pripomienky pri piatich percentách."
tags = ["research", "agents"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

Predstavme si fiktívnu projektovú manažérku, ktorá si v pondelok ráno otvorí asistenta. Pred niekoľkými mesiacmi spomenula, že istý dodávateľ uprednostňuje telefonáty po obede. Systém odvtedy uložil tisíce detailov: stretnutia, termíny, mená, nákupy aj zrušené cesty. Napíše pozdrav. Asistent ju preruší starou preferenciou dodávateľa a pridá pripomienku jarnej návštevy reštaurácie. Obe spomienky sú pravdivé. Ani jedna sa do tejto chvíle nehodí.

## Problém vyrušovania

Dlhodobá pamäť sa zvyčajne opisuje ako vyhľadávanie. Používateľ sa spýta na staršiu konverzáciu a systém nájde relevantný úryvok. Proaktívna pamäť prináša ťažšie rozhodnutie: asistent musí pri každom kroku určiť, či si niektorý uložený záznam zaslúži nevyžiadané prerušenie rozhovoru.

Yichuan Chen a Xin Wang zo Zhejiang Sci-Tech University skúmali, čo sa deje s rastom úložiska. Ich preprint *The Price of Scale in Proactive Memory Recall* považuje každý záznam za ďalší štatistický test. Aj keď má nerelevantný záznam iba malú šancu prekročiť prah podobnosti, tisíce pokusov výrazne zvyšujú pravdepodobnosť, že ho niektorý prekoná.

Výsledok bol výrazný. Prah nastavený na 5 % falošných upozornení pri ôsmich záznamoch vytvoril pri 2 048 záznamoch 84–100 % falošných upozornení v závislosti od modelu embeddingov a typu podnetu. Zdržanlivé správanie v malom úložisku sa zmenilo na takmer neustále vyrušovanie.

Nejde o bežné zabúdanie. Informácie v úložisku zostávajú. Systém zlyháva pri rozhodovaní, kedy ich má použiť.

## Viac spomienok, viac žrebov

Každý nerelevantný záznam môže dostať skóre podobnosti s najnovšou správou používateľa. Systém sa ozve, keď najvyššie skóre prekročí pevný prah. Pri ôsmich nerelevantných záznamoch má šum osem príležitostí vyzerať významne. Pri 2 048 ich má 2 048.

Chen a Wang odvodili dôsledok. Ak má celková miera falošných upozornení zostať na určenej úrovni, povolená miera falošných pozitívnych výsledkov pre každý záznam musí klesať približne nepriamo úmerne veľkosti úložiska. Pri celkovom cieli 5 % sa tolerancia jedného záznamu približne rovná zápornému prirodzenému logaritmu čísla 0,95 vydelenému počtom záznamov.

Sprísnenie má svoju cenu. Relevantné podnety musia prekonať vyššiu hranicu, čím sa systém posúva na ľavý okraj krivky ROC. Falošných upozornení ubudne, no spolu s nimi klesá aj počet správnych zásahov. Lepší model embeddingov môže krivku zlepšiť, ale neodstráni násobenie počtu testov.

Autori prehrali dátové prúdy z benchmarku LongMemEval, ktorý obsahuje 500 otázok zameraných na získavanie informácií, uvažovanie medzi reláciami, časové uvažovanie, aktualizácie a zdržanie sa odpovede. Použili aj LoCoMo s dlhými konverzáciami vytvorenými z osobnostných profilov a grafov udalostí, ktoré potom ľudia upravili, aby boli konzistentné. Tieto benchmarky skúmajú, či systémy dokážu obnoviť staré informácie. Chen a Wang z nich vytvorili chronologické situácie, v ktorých sa asistent musí rozhodnúť, či ich má pripomenúť práve teraz.

Vytvorili nepriame podnety, ktoré sa na spomienku nepýtali ani neobsahovali jej odpoveď. Experimenty použili lexikálne a sémantické skóre, viacero modelov embeddingov a cross-encoder na nové zoradenie výsledkov. Rovnaký vzorec pretrval pri všetkých zmenách. Ani drahší spôsob hodnotenia sa nevyhol cene rastu.

## Prah, ktorý sa prispôsobuje používateľovi

Navrhovanou alternatívou je konformná brána cue-swap. Okrem porovnania aktuálnej správy s pamäťou hodnotí aj referenčné podnety zo starších správ toho istého používateľa voči rovnakému úložisku. Brána zisťuje, či je aktuálny podnet nezvyčajne silný v porovnaní s bežnými podnetmi.

Mení sa tým základ kalibrácie. Prah sa prispôsobuje úložisku a rozdeleniu správ používateľa namiesto toho, aby pri rastúcom počte záznamov zostával pevný. Za predpokladu zameniteľnosti dáva konformné poradie záruku miery falošných upozornení aj pri konečnej vzorke a bez označených príkladov.

V LongMemEval, kde pozadie tvorili položky z nefiltrovanej histórie používateľa, udržala brána cue-swap falošné upozornenia na 3–6 %. Počet správnych zásahov sa vyrovnal prahu nastavenému pomocou označených dát. V chronologickom prehrávaní so staršími správami používateľa ako referenčnými podnetmi sa ozvala pri 6–8 % začiatkov relácií. Brána podobná bežne nasadzovanému riešeniu sa pri 2 048 záznamoch ozvala v 57 % prípadov.

Rozhodnutie trvalo približne 50 milisekúnd na jednom vlákne CPU. Zverejnený repozitár obsahuje brány v NumPy, testy, experimentálne skripty, anotácie aj výsledky. Autori spustili experimenty na jednej RTX 3090 a zdokumentovali reprodukciu prehrávania benchmarkov.

## Trvajúci kompromis

Ani po kalibrácii nie je proaktívna pamäť jednoduchá. V LoCoMo mohla byť konformná brána podľa pôvodu referenčných podnetov príliš citlivá alebo príliš opatrná. Jej záruka závisí od zameniteľnosti: budúce podnety sa musia dostatočne podobať referenčným, aby ich poradie zostalo platné. Správanie používateľa sa však môže meniť. Starostlivo vybraná referenčná vzorka sa môže líšiť od skutočnej prevádzky.

Štúdia testuje aj prospektívnu pamäť, pri ktorej má asistent konať po splnení budúcej podmienky. TriggerBench už ukázal, že je to ťažšie než odpoveď na priamu otázku o pamäti: výkon s dĺžkou kontextu klesá a modely môžu skĺznuť k stratégii „vždy pripomínať“. Pri kontrole falošných upozornení v experimente Chena a Wanga našli brány založené na podobnosti najviac 9 % obmedzení v benchmarku prospektívnej pamäti.

Ľudské hodnotenie potvrdilo cenu hlučného vyhľadávania. Jeden človek a dva jazykové modely preskúmali falošné upozornenia; väčšina odpovedi nepomohla. V skoršej verzii štúdie dosiahla zhoda troch hodnotiteľov Fleissovo kappa 0,63 a približne deväť z desiatich falošných upozornení predstavovalo skutočné vyrušenie. Nájdený údaj môže byť správny a napriek tomu rozhovor zhoršiť.

Štúdia má 14 strán, je preprintom a neprešla recenzným konaním. Jej dátové prúdy pochádzajú z benchmarkov, nie z rokov prirodzeného používania miliónmi ľudí. Výsledok brány cue-swap preto treba otestovať pri meniacich sa zvykoch, viacerých jazykoch a úložiskách so vzájomne závislými záznamami. Argument o viacnásobnom testovaní však nezávisí od konkrétneho produktu. Každý systém, ktorý vyberá maximum z množstva zašumených skóre, tento problém zdedí.

Na konci týždňa sa vráťme k fiktívnej projektovej manažérke. Jej asistent stále uchováva preferenciu dodávateľa aj starú reštauráciu. Rozdiel spočíva v premyslenom mlčaní: skôr než sa niektorý detail objaví na obrazovke, aktuálna správa musí byť relevantnejšia než bežné správy používateľa pri rovnakom preplnenom úložisku. Užitočný pamäťový systém nepotrebuje iba spôsob, ako si pamätať. Potrebuje aj presvedčivý dôvod, kedy prehovoriť.

## Použité zdroje

- Angelopoulos, A. N., & Bates, S. (2021). *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*. https://arxiv.org/abs/2107.07511
- Chen, Y., & Wang, X. (2026). *The Price of Scale in Proactive Memory Recall*. https://arxiv.org/abs/2610.34507
- Chen, Y., & Wang, X. (2026). *Code, data and results for The Price of Scale in Proactive Memory Recall*. https://github.com/RiverChenStillCompiling/price-of-scale
- Maharana, A., Lee, D.-H., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024). *Evaluating Very Long-Term Conversational Memory of LLM Agents*. https://aclanthology.org/2024.acl-long.747/
- Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. https://arxiv.org/abs/2410.10813
- Zhang, T., Wang, X., Zhang, Q., Chen, Q., Li, K., Chen, Y., Wang, D., Meng, H. M., & Lu, Y. (2026). *TriggerBench: Investigating Prospective Memory for Large Language Models*. https://aclanthology.org/2026.emnlp-main.1319/

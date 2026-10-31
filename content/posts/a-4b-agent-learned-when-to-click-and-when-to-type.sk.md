+++
title = "4B agent sa naučil, kedy klikať a kedy písať príkazy"
slug = "4b-agent-sa-naucil-kedy-klikat-a-kedy-pisat-prikazy"
description = "Mage-VL-Cowork od Microsoftu spája ovládanie obrazovky a trvalý terminál v jednom otvorenom modeli. Jeho spôsob trénovania ukazuje, že obmedzenie nástrojov učiteľského modelu a odmeňovanie kratších úspešných postupov môže byť dôležitejšie než pridanie ďalšieho rozhrania."
tags = ["models", "agents", "research"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

Predstavme si analytika, ktorý má v tabuľke zlúčiť dve hlavičky, pridať graf a zachovať súbor vo formáte `.xlsx`. Analytik je vymyslený, no rozhodnutie je skutočné: preklikávať ponuky a upravovať bunky jednu po druhej, alebo otvoriť terminál a zmeniť zošit pomocou Pythonu. Schopný počítačový agent by mal vedieť, ktorý postup sa na úlohu hodí, ešte pred prvým kliknutím.

## Jedna stratégia, dva spôsoby práce

Tím Mage v Microsofte vydal Mage-VL-Cowork, model s licenciou Apache-2.0 a 4,74 miliardy parametrov, ktorý vie pracovať cez grafické prostredie aj trvalé prostredie Bash a Python. Výber nástroja nezveruje externému smerovaču. Tá istá vizuálno-jazyková stratégia v každom kroku volí medzi jednou z 11 operácií na obrazovke a príkazom v termináli.

Rozdiel sa môže zdať malý. Mení však spôsob, akým agent využíva kontext a ako priamo dokáže overiť svoju prácu. Snímka obrazovky môže spotrebovať tisíce tokenov, kým dlhý sled pohybov myšou iba nepresne napodobňuje to, čo softvérová knižnica vykoná jednoznačne. Terminál však nevidí neuložené plátno, dialógové okno ani dočasný stav aplikácie. Model potrebuje oba spôsoby práce a návyk správne si medzi nimi vybrať.

Tím Mage uvádza skóre 66,04 % v benchmarku OSWorld-Verified, ktoré je priemerom dvoch behov na 361 úlohách s limitom 50 krokov. Jednotlivé behy dosiahli 65,33 a 66,75 %. Ľudia majú v porovnávacej tabuľke tímu skóre 72,4 %; GPT-5.4-mini dosiahol v jednom behu pri rovnakých úlohách a limitoch 69,6 %. Medzi modelmi s otvorenými váhami vedie ScaleCUA-Qwen3.5-9B so skóre 68,7 %. Mage-VL-Cowork teda netvrdí, že vedie celkovo: podľa tímu má najlepšie skóre medzi 4B modelmi.

Ide o merania Microsoftu, ktoré zatiaľ nikto nezávisle nezopakoval. Repozitár však obsahuje hodnotiace úlohy, kód agenta aj spúšťacie skripty, takže tvrdenie sa dá overiť lepšie než samotný údaj v karte modelu.

## Učiteľ musel prísť o nástroje

Príprava sa začala ešte pred trénovaním samotného modelu. Silný učiteľský model so všetkými dostupnými rozhraniami automaticky nevytváral jednoznačné príklady. Prekrývajúce sa postupy trieštili tréningový signál: strom prvkov prístupnosti, priame ovládanie pracovnej plochy aj vizuálne klikanie mohli vyriešiť rovnaký krok rôznymi spôsobmi.

Tím porovnal dve zostavy učiteľského modelu na 672 odložených úlohách, ktoré zahŕňali viac aplikácií. Zvolená zostava poskytla GPT-5.4 grafické a programátorské nástroje, odstránila prekrývajúce sa pomôcky ako `xdotool` a výpisy prístupnosti a vopred nainštalovala knižnice pre tabuľky, dokumenty, prezentácie, PDF a obrázky. Učiteľ vyriešil 92,0 % úloh v priemere za 25 krokov. Zostava doplnená o prístupnosť dosiahla 89,6 % a potrebovala 35,33 kroka.

Po destilácii sa rozdiel zväčšil. 4B študentský model trénovaný z obmedzenej zostavy dosiahol 37,6 %, kým model trénovaný zo širšej sady nástrojov 25,1 %. Priemerný počet krokov klesol z 39,40 na 30,91. Oba výsledky poskytol ten istý výskumný tím. Porovnanie napriek tomu odhaľuje praktický spôsob zlyhania: hraničný model dokáže nadbytočné možnosti vykompenzovať ďalšími krokmi, malý študent však preberie zmätok.

Rovnakú snahu o opakovateľnú štruktúru mal aj dátový proces. Mage-CUA-Forge vytvoril 293 806 úloh založených na 6 915 elementárnych zručnostiach a zachoval 318 837 hybridných trajektórií. Namiesto toho, aby agent zakaždým zostavoval celé prostredie od začiatku, systém raz pre každú zručnosť vytvoril opakovane použiteľné pracovné postupy a prípravné nástroje pre konkrétne aplikácie. Pri rovnakom generujúcom modeli podľa tímu klesla spotreba na úlohu z 1,276 milióna na 85 000 tokenov a opakované náklady z 0,906 na 0,158 dolára.

Ide o syntetické tréningové dáta v priemyselnom rozsahu. Ich hodnota závisí od správnosti prípravných nástrojov, špecifikácií úloh a hodnotiacich pravidiel. Repozitár uvádza, že 38,24 % vytvorených úloh zahŕňa viac aplikácií a trajektórie obsahujú približne 68 % grafických operácií a 32 % príkazov v termináli.

## Najprv špecializácia, potom spojenie

Mage-VL-Cowork vychádza z priebežného checkpointu Mage-VL, nie z modelu, ktorý už bol špecializovaný na grafické ovládanie alebo programovanie. Trénovanie má päť etáp: vizuálne ukotvenie, viackrokovú prácu v grafickom prostredí, programovanie a prácu v termináli, hybridné dolaďovanie s dohľadom a online učenie posilňovaním.

Na poradí záleží. Model sa najprv naučí dva samostatne použiteľné spôsoby práce a až potom medzi nimi smeruje úlohy. Hybridná etapa s dohľadom dosiahla v OSWorld-Verified 55,84 %. Online učenie posilňovaním zvýšilo skóre na 66,04 % a zároveň znížilo priemerný počet volaní modelu z 21,57 na 18,77 a výstupných tokenov na úlohu zo 7 374 na 5 499.

Odmena teda agenta iba nenútila skúšať úlohu dlhšie. Úspešné postupy skrátila. Tím použil overiteľné odmeny na 1 988 úlohách a v jednej aktualizácii spracovával 768 epizód. Hoci etapa učenia posilňovaním podľa účtovania tímu tvorila iba 3,5 % tréningového harmonogramu, spotrebovala viac nominálneho výpočtového výkonu než ktorákoľvek iná etapa.

Dlhé relácie na pracovnej ploche prinášajú ďalší problém. Snímky môžu zaplniť kontext skôr, než sa práca skončí. Mage-VL-Cowork uchováva tri najnovšie snímky a štyri úplné odpovede asistenta; staršie kroky zhrnie do jednoriadkových opisov operácií. Stratégia tak zachováva nedávne vizuálne zmeny aj skrátený záznam predchádzajúcej práce.

Aktívny kontext má 32 768 tokenov, hoci architektúra podporuje viac. Model v každom kroku vytvorí uvažovanie, krátke zhrnutie operácie a volanie nástroja. Staršie uvažovanie preto môže z kontextu zmiznúť, kým záznam operácií zostane.

## Kde sa benchmark končí

OSWorld vznikol na testovanie agentov v skutočných aplikáciách a pri úlohách operačného systému, nie iba na izolovaných webových stránkach. Overená sada úloh zvyšuje spoľahlivosť hodnotiacich mechanizmov, benchmark však stále určuje operačné prostredie, nainštalovaný softvér aj kontrolu úspechu. Nezachytí, čo sa stane, keď agent narazí na osobné úložisko hesiel, nepredvídateľnú sieť alebo dokument s nepriateľskými pokynmi.

Aj odporúčania Microsoftu na nasadenie ukazujú, čo benchmark nepokrýva. Model dokáže spúšťať ľubovoľné príkazy shellu a ovládať pracovnú plochu, preto tím odporúča jednorazové virtuálne stroje alebo kontajnery, žiadne osobné prihlasovacie údaje, obmedzené odchádzajúce sieťové spojenia a potvrdenie človekom pred nezvratnými operáciami. Model je určený na výskum, nie na produktové nasadenie.

Ani veľkosť 4B neznamená, že celý systém je nenáročný. Tím uvádza 7,79 zettaFLOPov nominálneho výpočtového výkonu pri trénovaní jazykového modelu v piatich etapách, na ktoré použil 32 GPU NVIDIA B200 a 1 120 procesorových sandboxov pri učení posilňovaním. Dva súbory s váhami checkpointu BF16 zaberajú pri obsluhe približne 9,48 GB ešte pred započítaním pamäte behu a prostredia pracovnej plochy.

Vydanie je najsilnejšie ako argument o spôsobe trénovania. Autori obmedzili možnosti učiteľského modelu, vytvorili úlohy okolo opakovane použiteľných zručností a každý spôsob práce trénovali samostatne. Až potom model odmeňovali za splnenie overiteľnej práce s menším počtom volaní.

Vráťme sa k vymyslenému analytikovi. Graf stále patrí do grafickej aplikácie, kde možno skontrolovať jeho vzhľad. Bunky je vhodnejšie zlúčiť v Pythone, kde sa dá štruktúra súboru presne zmeniť a overiť. Rozhodujúca operácia nastane ešte pred otvorením ktoréhokoľvek nástroja: model si zvolí postup a táto voľba je teraz súčasťou stratégie, ktorú môže ktokoľvek preskúmať.

## Použité zdroje

- Microsoft Mage Team. (2026). *Mage: A Lightweight, Research-Friendly Multimodal Model Family*. https://github.com/microsoft/Mage
- Microsoft Mage Team. (2026). *Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use from Evolved Harnesses*. https://github.com/microsoft/Mage/blob/main/assets/mage_vl_cowork_tech_report.pdf
- Microsoft. (2026). *Mage-VL-Cowork model card*. https://huggingface.co/microsoft/Mage-VL-Cowork
- Xie, T., et al. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. https://arxiv.org/abs/2404.07972
- Yang, S., et al. (2026). *Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model*. https://arxiv.org/abs/2607.24904

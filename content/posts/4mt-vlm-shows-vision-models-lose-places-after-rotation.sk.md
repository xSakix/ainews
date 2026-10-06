+++
title = "4MT-VLM ukazuje, že vizuálne modely po otočení nespoznajú miesto"
slug = "4mt-vlm-vizualne-modely-po-otoceni-nespoznaju-miesto"
description = "Preprint prispôsobil klinický test priestorovej pamäte pre 16 vizuálno-jazykových modelov. Všetky spoznajú krajinu z uhla, z ktorého si ju prezreli, no po pohybe kamery väčšina klesne na úroveň hádania."
tags = ["research", "models"]
date = 2026-10-06T04:02:31+02:00
draft = false
+++

Vizuálno-jazykové modely spoznajú krajinu z uhla, z ktorého ju videli prvýkrát, no väčšina ju po pohybe kamery nedokáže nájsť. Vyplýva to z 4MT-VLM, nového benchmarku (porovnávacieho testu) odvodeného od klinického testu priestorovej pamäte.

Markus Frey z Fraunhofer IAIS, nemeckého inštitútu aplikovaného výskumu, zadal 16 otvoreným aj uzavretým modelom úlohu, ktorú riešia pacienti: prezrieť si počítačovo vykreslenú krajinu so štyrmi vrcholmi a potom ju nájsť medzi štyrmi podobnými krajinami zobrazenými z nového uhla. Dobrovoľník vyriešil približne štyri z piatich pokusov s otočením. Väčšina modelov nebola lepšia ako náhodný tip.

## Prečo na tom záleží {#why-it-matters}

Robotický inžinier, ktorý používa vizuálno-jazykový model ako oči mobilného robota, potrebuje práve túto schopnosť: spoznať miestnosť aj potom, čo sa robot otočí. Podľa preprintu ju neprinášajú ani väčšie modely, ani podrobnejšie pokyny.

## Rozpoznanie funguje, otočenie nie

Benchmark vychádza z testu Four Mountains Test, ktorý lekári používajú, pretože výsledky klesajú pri poškodení hipokampu a v počiatočnom štádiu Alzheimerovej choroby. Farby, textúry a osvetlenie sa medzi študijným a testovacími obrázkami menia pri každom pokuse, takže ani pokus bez otočenia sa nedá vyriešiť porovnaním pixelov. Frey považuje presnosť pri týchto neotočených pokusoch za kontrolu, či model miesto vôbec dokáže identifikovať.

Modely touto kontrolou prejdú a potom pri otočení zlyhajú. Model GPT-5.6 Luna od spoločnosti OpenAI odpovedal správne na všetky neotočené pokusy, ale len na 31 % otočených, pričom náhodné hádanie dosahuje jeden zo štyroch. Pri súhrne všetkých 16 modelov bol najhorší uhol 135 stupňov, pri ktorom presnosť klesla zreteľne pod úroveň náhody.

Polovičné otočenie o 180 stupňov, teda najväčšia zmena, dopadlo lepšie ako 135 stupňov. Frey to vysvetľuje tým, že modely používajú obrazovú skratku, napríklad porovnanie so zrkadlovým obrazom scény, a neotáčajú vnútornú mapu. Porovnanie s človekom vychádza z jediného účastníka, čo stačí na preukázanie, že úloha je riešiteľná, ale nie na ľudský priemer.

## Väčšie modely spoznajú viac, otáčajú rovnako zle

Veľkosť zlepšila rozpoznávanie a otočenie nechala na mieste. V rodine Qwen2.5-VL od Alibaby, od 3 do 72 miliárd parametrov, stúpla presnosť bez otočenia z 30 na 75 %, kým presnosť s otočením zostala na úrovni náhody alebo pod ňou. Rodina InternVL3.5 tento vzorec zopakovala od 1 do 38 miliárd parametrov. Zo 14 modelov s otvorenými váhami s veľkosťou do 235 miliárd parametrov žiadny neodpovedal správne na viac ako 31 % otočených pokusov a variant s uvažovaním („thinking“) dosiahol rovnaký výsledok ako jeho štandardný súrodenec.

Pokyny rozdiel nevyrovnali. Frey spustil Qwen2.5-VL-32B so šiestimi promptmi vrátane výslovných postupov, napríklad predstaviť si rozloženie priamo zhora alebo sa ukotviť na najvýraznejšom vrchole. Všetkých šesť ho nechalo pod úrovňou náhody.

## Vzdialenejšie nesprávne odpovede odhalia hrubú mapu

Najinformatívnejší experiment menil len nesprávne odpovede. Frey zmeral v metroch, ako ďaleko od seba ležia vrcholy dvoch krajín po najlepšom možnom otočení, a potom vybral tri návnady z krajín so vzdialenejším rozložením, pričom cieľ aj uhly zostali rovnaké.

Posunutie najbližšej návnady z približne 7 na približne 31 metrov zvýšilo presnosť modelu Gemini 3.8 Flash od Googlu pri otočených pokusoch z 39 na 85 % a modelu GPT-5.6 Luna z 31 na 55 %. Žiadny otvorený model sa štatisticky významne nezlepšil.

To je dôkaz práce, že špičkové modely majú určitú predstavu o rozložení, len v nízkom rozlíšení. Model bez mapy by z oddialenia návnad nemohol získať, a model s mapou na ľudskej úrovni by nepotreboval 30 metrov odstupu. Efekt pripomína človeka, ktorý z okna lietadla spozná svoje mesto, ale nie svoju ulicu.

Rovnakým smerom ukazujú aj chyby. Človek, ktorý odpovie nesprávne, zvyčajne vyberie návnadu, ktorej rozloženie sa cieľu najviac podobá. Nesprávne odpovede modelov sa rozložili takmer rovnomerne medzi blízke aj vzdialené návnady, akoby rozloženie pri výbere nezohrávalo žiadnu úlohu.

## Syntetický test jediného autora

Krajiny sú syntetické vizualizácie a Frey upozorňuje, že predtrénovanie na podobných vykreslených scénach mohlo niektorým modelom pomôcť. Počty parametrov uzavretých modelov nie sú zverejnené, takže dôkazy o škálovaní stoja len na otvorených modeloch. Preprint, zverejnený na arXiv 30. septembra 2026, má jediného autora a neodkazuje na žiadny kód ani dataset.

Frey uvádza, že testuje ďalších ľudských účastníkov, čím 82 % úspešnosť dobrovoľníka pri otočených pokusoch získa riadnu porovnávaciu skupinu.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| 4MT-VLM vychádza z testu Four Mountains Test; 500 pokusov nad 100 generovanými krajinami, testovaných 16 modelov | OVERENÉ | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne; autorov vlastný benchmark |
| Vzhľad sa medzi študijným a testovacími obrázkami mení pri každom uhle | OVERENÉ | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne; opis metódy |
| Jeden ľudský účastník odpovedal správne na 100 % neotočených a 82 % otočených pokusov | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne; len jeden účastník |
| GPT-5.6 Luna: 100 % bez otočenia, 31 % s otočením; náhoda je 25 % | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |
| Súhrnná presnosť pri 135 stupňoch je 15,0 % (48/320), pod úrovňou náhody; pri 180 stupňoch 23 % | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |
| Modely používajú obrazovú skratku, napríklad porovnanie so zrkadlovým obrazom | ANALÝZA | [Preprint Frey](https://arxiv.org/abs/2609.39238) | autorova interpretácia vzorca pri 135 a 180 stupňoch |
| Qwen2.5-VL od 3B po 72B: bez otočenia 30 % až 75 %, s otočením 29 %, 31 %, 18 %, 20 % | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |
| Žiadny model s otvorenými váhami (1B až 235B) nepresiahne 31 % pri otočení; variant s uvažovaním dosahuje rovnako ako inštrukčný 19 % pri otočení | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |
| Šesť štýlov pokynov necháva Qwen2.5-VL-32B na 13,8 % až 23,8 %, všetky pod úrovňou náhody | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |
| Medián vzdialenosti najbližšej návnady 6,8 m až 31,4 m: Gemini 3.8 Flash z 39 % na 85 %, GPT-5.6 Luna z 31 % na 55 % | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |
| Žiadny otvorený model sa pri väčšom odstupe návnad významne nezmení | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |
| Chyby modelov sa delia 30/37/33 medzi najbližšiu, strednú a najvzdialenejšiu návnadu; človek vybral najbližšiu pri 10 zo 14 chýb | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |
| Špičkové modely majú hrubú reprezentáciu rozloženia | ANALÝZA | [Preprint Frey](https://arxiv.org/abs/2609.39238) | záver z výsledku s odstupom návnad |
| Preprint jediného autora zverejnený 30. septembra 2026; autor z Fraunhofer IAIS; bez odkazu na kód či dáta | OVERENÉ | [Záznam arXiv](https://arxiv.org/abs/2609.39238) | metadáta arXiv a doména autorovho e-mailu |
| Ďalší ľudskí účastníci sa práve hodnotia | PODĽA SPOLOČNOSTI | [Preprint Frey](https://arxiv.org/abs/2609.39238) | žiadne |

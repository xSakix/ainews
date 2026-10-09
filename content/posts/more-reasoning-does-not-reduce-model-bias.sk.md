+++
title = "Viac uvažovania neznižuje skreslenie modelov"
slug = "viac-uvazovania-neznizuje-skreslenie-modelov"
description = "Štúdia s 12 350 volaniami nezistila spoľahlivý pokles šiestich mier kognitívneho skreslenia, keď modely spotrebovali viac tokenov na uvažovanie. Pri ukotvení pomohol jeden priamy pokyn."
tags = ["research", "models"]
date = 2026-10-09T04:02:06+02:00
draft = false
+++

Viac času na uvažovanie spoľahlivo neznížilo náchylnosť jazykových modelov na prompty s kognitívnym skreslením. Zistila to nová štúdia siedmich modelov a 12 350 volaní API.

Výskumník Obada Kraishan z Texas Tech University menil povolený rozsah uvažovania modelov spoločností Anthropic, OpenAI, DeepSeek a Qwen a potom meral, ako sa ich odpovede zmenili, keď rozhodovacia situácia obsahovala nepodstatnú kotvu, rámcovanie alebo skorší záväzok. Ani jeden model nebol s rastúcou skutočnou spotrebou tokenov na uvažovanie konzistentne menej citlivý.

**Prečo na tom záleží:** Vývojár, ktorý pre systém na podporu rozhodovania zvolí väčší rozpočet na uvažovanie, platí za viac výpočtov. Výsledky hovoria, že dodatočné výpočty spoľahlivo nezlepšili žiadne merané skreslenie, hoci modely s uvažovaním často pôsobia na používateľov rozvážnejšie.

## Štúdia merala uvažovanie, ktoré skutočne prebehlo

Experiment použil 30 spárovaných situácií pokrývajúcich ukotvenie, rámcovanie, averziu voči strate, eskaláciu záväzku, dostupnosť a konfirmačné skreslenie. Každý pár obsahoval rovnaké informácie dôležité pre rozhodnutie, no jedna verzia pridala prvok, ktorý má podľa očakávania posunúť ľudský úsudok. Desať opakovaných vzoriek v každej podmienke umožnilo autorovi zmerať zmenu zvolených možností.

Panel siedmich modelov pároval verzie s uvažovaním a bez uvažovania v štyroch rodinách. Požadované limity boli nula, 1 024, 4 096 a 8 192 tokenov, hoci dostupné podmienky sa medzi poskytovateľmi líšili. Kraishan zaznamenával skutočne spotrebované tokeny, pretože nastavenie API sa často nepremenilo na zodpovedajúci rozsah uvažovania.

Tento rozdiel bol dôležitý. Model firmy Anthropic zvyšoval priemernú spotrebu uvažovania s rastúcim limitom, ale zostal hlboko pod vyššími hranicami. Testovaný model spoločnosti OpenAI používal nad nulou takmer rovnaké množstvo, zatiaľ čo DeepSeek-R1 a Qwen3 niekedy prekročili požadovaný limit 1 024 tokenov. Hlavná analýza preto považovala za dávku skutočnú spotrebu tokenov.

Modely s uvažovaním neboli spoľahlivo menej skreslené než porovnateľné verzie. Smer rozdielu sa vo všetkých štyroch rodinách dokonca prikláňal k mierne vyššej citlivosti, no spoločný odhad bol príliš neistý na takéto silnejšie tvrdenie. Pre hlavnú otázku experimentu je podstatnejšie, že žiadny model nevykázal so spotrebou ďalších tokenov na uvažovanie štatisticky spoľahlivý pokles.

Zistenie má úzky záber. Súbor obsahoval päť položiek pre každé zo šiestich skreslení, všetky z manažérskych rozhodovacích situácií, a niektoré porovnania rodín prekračovali hranicu medzi príbuznými modelmi namiesto zapnutia a vypnutia uvažovania v rovnakých váhach. Testuje správanie v kontrolovaných promptoch, nie správnosť otvorených pracovných rozhodnutí.

## Ukotvenie reagovalo na priamy pokyn

Ukotvenie bolo jediným testovaným skreslením, ktoré konzistentne posúvalo modely rovnakým smerom, aký sa zvyčajne pozoruje u ľudí. Číslo v prompte pritiahlo odhady k sebe vo všetkých siedmich modeloch. Štyri ďalšie kategórie sa prikláňali k opačnému smeru, kým dostupnosť nevykázala spoľahlivý účinok.

Pri piatich položkách s ukotvením autor pridal jednu vetu, ktorá od modelu žiadala zopakovať kotvu pred odpoveďou. Ukotvenie kleslo pri každej položke. Súhrnný výsledok tesne minul hranicu štatistickej významnosti štúdie, takže ide o sľubné pozorovanie, nie potvrdené zmiernenie, no samotné dodatočné uvažovanie neprinieslo porovnateľný pokles.

Tento kontrast je najpraktickejším výsledkom štúdie. Cielený pokyn môže zmeniť, ktoré informácie model spracúva, zatiaľ čo väčší rozpočet na uvažovanie iba poskytne viac priestoru existujúcemu procesu. Experiment nepotvrdzuje, že opakovanie čísel sa zovšeobecní za päť promptov; ukazuje však, prečo nastavenia výpočtov a ochrany proti skresleniu patria do samostatných hodnotení.

Preprint bol predložený 7. októbra a prijatý na IEEE CogMI 2026. Autor zverejnil zmrazený súbor promptov, záznamy tokenov jednotlivých volaní a analytický kód v [repozitári Anchored Minds](https://github.com/obadaKraishan/anchored-minds), takže výsledok možno testovať na novších modeloch a väčších súboroch položiek.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Štúdia vykonala 12 350 volaní na siedmich modeloch zo štyroch rodín | PODĽA SPOLOČNOSTI | [Štúdia](https://arxiv.org/abs/2610.10049) | [Kód a dáta](https://github.com/obadaKraishan/anchored-minds) |
| Použila 30 situácií zahŕňajúcich šesť kognitívnych skreslení | PODĽA SPOLOČNOSTI | [Štúdia](https://arxiv.org/abs/2610.10049) | [Kód a dáta](https://github.com/obadaKraishan/anchored-minds) |
| Požadované limity a skutočná spotreba uvažovania sa medzi poskytovateľmi líšili | PODĽA SPOLOČNOSTI | [Štúdia](https://arxiv.org/abs/2610.10049) | [Kód a dáta](https://github.com/obadaKraishan/anchored-minds) |
| Žiadny testovaný model nevykázal spoľahlivý pokles veľkosti skreslenia s rastúcou spotrebou tokenov na uvažovanie | PODĽA SPOLOČNOSTI | [Štúdia](https://arxiv.org/abs/2610.10049) | žiadne |
| Modely s uvažovaním neboli spoľahlivo menej skreslené než porovnateľné verzie v rodine | PODĽA SPOLOČNOSTI | [Štúdia](https://arxiv.org/abs/2610.10049) | žiadne |
| Ukotvenie sa vo všetkých siedmich modeloch pohybovalo smerom typickým pre ľudí | PODĽA SPOLOČNOSTI | [Štúdia](https://arxiv.org/abs/2610.10049) | žiadne |
| Zopakovanie kotvy znížilo ukotvenie pri všetkých piatich položkách, no výsledok minul hranicu významnosti | PODĽA SPOLOČNOSTI | [Štúdia](https://arxiv.org/abs/2610.10049) | žiadne |
| Štúdia bola prijatá na IEEE CogMI 2026 a zverejnila kód aj dáta | OVERENÉ | [Štúdia](https://arxiv.org/abs/2610.10049) | [Repozitár](https://github.com/obadaKraishan/anchored-minds) |

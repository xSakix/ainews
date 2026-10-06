+++
title = "Sondy odhaľujúce klamstvá sledujú poslušnosť namiesto pravdy"
slug = "sondy-odhalujuce-klamstva-sleduju-poslusnost-namiesto-pravdy"
description = "Preprint testuje osem publikovaných sond na jazykových modeloch, ktoré hrajú postavy odmietajúce základné fakty. Mnohé zlyhajú, keď pravdivé a nepravdivé odpovede zdieľajú rovnaký prompt, no sonda trénovaná na oddelenie pravdy od poslušnosti obstojí."
tags = ["research", "safety"]
date = 2026-10-06T04:01:31+02:00
draft = false
+++

Mnohé publikované sondy na odhaľovanie klamstiev, ktoré čítajú vnútornú aktivitu jazykového modelu a označujú nepravdivé odpovede, v skutočnosti čiastočne zisťujú, či model dodržal pokyny, uvádza nový preprint.

Maximilian von Klinski a traja spoluautori nechali tri otvorené modely hrať postavy, ktoré odmietajú základné fakty, napríklad ptolemaiovského astronóma alebo konšpirátora, a testovali, či osem existujúcich sond stále zachytí nepravdivé odpovede. Mnohé ich zachytili, až kým sa pravdivé a nepravdivé odpovede neocitli pod rovnakým promptom postavy. Vtedy viaceré dopadli horšie ako hod mincou.

## Prečo na tom záleží {#why-it-matters}

Bezpečnostný tím, ktorý nasadený model monitoruje sondou, potrebuje, aby alarm reagoval na nepravdu, nie na niečo, čo ju zvyčajne sprevádza. V dátach, na ktorých sa väčšina sond trénuje, je nepravdivá odpoveď zároveň menej pravdepodobná a porušuje pravidlá modelu. Štúdia zistila, že sondy sa tieto skratky naučia.

## Ako sonda číta model

Sonda je jednoduchý klasifikátor trénovaný na číslach z jednej vrstvy modelu, označených podľa toho, či spracúvaný text bol pravdivý alebo nepravdivý. Ak funguje, číta, čo model považuje za pravdivé, aj keď slová, ktoré tvorí, tvrdia opak.

Tím zostavil dataset 8 916 odpovedí modelov Llama 3.3 70B od Mety a Gemma 3 27B a Gemma 4 31B od Googlu. Každý model odpovedal na otázky typu áno/nie ako bežný asistent aj ako jedna z 15 postáv: skutoční zástancovia rôznych presvedčení, fiktívne postavy, napríklad občan z Orwellovho románu *1984*, a historické postavy, napríklad stredoveký lekár. Otázky dolaďoval proces postavený na modeli Claude Opus 4.8 od spoločnosti Anthropic, filtrovala ich Llama v úlohe hodnotiteľa a ručne ich skontroloval prvý autor.

## Zdieľaný prompt väčšinu sond rozbije

V prvej verzii testu väčšina starších sond dobre oddelila pravdivé odpovede od nepravdivých a správne ich zoradila zhruba v deviatich pároch z desiatich. Každá nepravdivá odpoveď však prišla s promptom postavy a každá pravdivá s promptom asistenta, takže odpoveď prezradil už samotný prompt.

Autori túto stopu odstránili tak, že obe odpovede umiestnili za prompt postavy. Pravdivá odpoveď tak bola zároveň menej pravdepodobná a odporovala pokynom postavy. Na modeli Llama viaceré sondy, ktoré predtým fungovali, klesli pod úroveň náhody a len dve zostali blízko svojich skorších výsledkov. Zlyhania sa zopakovali, často ešte výraznejšie, na oboch modeloch Gemma.

## Tri pasce odhalia skratku

Aby zistil, čo sondy v skutočnosti sledujú, tím zostavil tri testovacie sady, v ktorých pravda ide proti pravdepodobnému mätúcemu faktoru. V prvej bodovacie pravidlo urobilo z nesprávnej odpovede tú pravdepodobnejšiu. V druhej postava v súkromí verila nepravde, napríklad že sedemkrát šesť je 13. V tretej správna odpoveď porušila pravidlo formátovania, napríklad použila okrúhle zátvorky namiesto požadovaných hranatých, kým nesprávna ho dodržala.

Rozhodujúca bola pasca s formátovaním. Na modeli Llama všetky staršie sondy dosiahli výsledok pod úrovňou náhody, okrem jednej, ktorej hodnoty boli obrátené v každom teste. Autori to interpretujú ako silné prepojenie medzi „pravdivým“ a „poslušným“ vnútri týchto sond.

Vlastná sonda tímu pridáva k štandardnému trénovaniu na jednoduchých faktoch jednu zložku: otázky, pri ktorých pokyny vyžadujú nesprávnu odpoveď, takže poslušnosť a pravda smerujú opačne. V teste so zdieľaným promptom na modeli Llama dosiahla približne 0,98 z 1, na žiadnom z troch modelov neklesla pod 0,90 a vo všetkých troch pascách bola bezchybná.

## Vlastné riešenie a stále neznáme mätúce faktory

Tento výsledok si vyžaduje dve výhrady. Nová sonda bola navrhnutá proti tým istým mätúcim faktorom, na ktorých bola potom testovaná, a autori uznávajú, že jej bezchybné výsledky v pascách preto neprekvapujú. Jej návrh zároveň rozširuje staršiu sondu, na ktorej vývoji sa podieľal spoluautor Lennart Bürger a ktorá bola jednou z iba dvoch starších sond, ktoré pri zdieľanom prompte obstáli.

Vlastné dáta štúdie ukazujú, že zoznam mätúcich faktorov nie je úplný. Na modeli Gemma 4 bola jedna staršia sonda takmer bezchybná vo všetkých troch pascách, no v teste so zdieľaným promptom dosiahla približne 0,17, teda zlyhala z dôvodu, ktorý žiadna z pascí nezachytila. Postavy boli navyše nastavené jediným systémovým promptom v jednokolových konverzáciách, na modeloch s najviac 70 miliardami parametrov.

Prácu financovali nemecké Spolkové ministerstvo výskumu, technológií a vesmíru, program Európskej únie Horizont Európa a Nemecká výskumná nadácia. Autori zverejnili dataset na Hugging Face a kód na GitHube. Ako ďalší prípad na testovanie uvádzajú postavy, ktoré sa vynárajú postupne počas dlhých konverzácií.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Hodnotených osem starších sond; mnohé zlyhajú, keď pravdivé a nepravdivé odpovede zdieľajú prompt postavy | PODĽA SPOLOČNOSTI | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne; výsledok preprintu |
| Dataset 8 916 ľuďmi skontrolovaných odpovedí modelov Llama 3.3 70B, Gemma 3 27B a Gemma 4 31B v 15 postavách | OVERENÉ | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | [dataset na Hugging Face](https://huggingface.co/datasets/maxvonk/anti-factual-personas) |
| Otázky dolaďované procesom s Claude Opus 4.8, hodnotené modelom Llama 3.3 70B, skontrolované prvým autorom | OVERENÉ | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne; opis metódy autormi |
| Väčšina starších sond dosahuje AUROC 0,86 až 0,94, keď sa prompt pri pravdivých a nepravdivých odpovediach líši | PODĽA SPOLOČNOSTI | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne |
| So zdieľaným promptom na modeli Llama viaceré staršie sondy klesnú pod úroveň náhody; stabilné zostávajú len Marks/Bürger Lie (0,885) a Cundy DolusChat (0,901) | PODĽA SPOLOČNOSTI | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne |
| Zlyhania pri zdieľanom prompte sa opakujú, často výraznejšie, na modeloch Gemma 3 27B a Gemma 4 31B | PODĽA SPOLOČNOSTI | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne |
| V pasci s poslušnosťou na modeli Llama všetky staršie sondy dosahujú výsledok pod úrovňou náhody okrem Goldowsky-Dill SD, ktorá je obrátená vo všetkých testoch | PODĽA SPOLOČNOSTI | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne |
| Sondy spájajú pravdu s dodržiavaním pokynov | ANALÝZA | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | záver autorov z pasce s poslušnosťou |
| Nová sonda: AUROC 0,976 v teste so zdieľaným promptom na modeli Llama, na žiadnom z troch modelov pod 0,900, bezchybná vo všetkých troch pascách | PODĽA SPOLOČNOSTI | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne |
| Nová sonda bola trénovaná na odstránenie tých istých mätúcich faktorov, na ktorých je testovaná; autori označujú výsledky v pascách za neprekvapivé | OVERENÉ | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne |
| Spoluautor Lennart Bürger sa podieľal na vývoji sondy Marks/Bürger, ktorú nová sonda rozširuje | OVERENÉ | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | cituje Bürger a kol. (2024) |
| Na modeli Gemma 4 je Cooney DYL takmer bezchybná vo všetkých pascách, no so zdieľaným promptom dosahuje 0,171 | PODĽA SPOLOČNOSTI | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | žiadne |
| Financované nemeckým BMFTR, programom EÚ Horizont Európa a Nemeckou výskumnou nadáciou (DFG) | OVERENÉ | [Preprint von Klinski a kol.](https://arxiv.org/abs/2609.39807) | sekcia poďakovania |
| Kód je verejne dostupný na GitHube | OVERENÉ | [Repozitár na GitHube](https://github.com/max-vkl/stress-testing-llm-lie-detectors) | stránka repozitára sa načíta |
| Preprint zverejnený 30. septembra 2026 | OVERENÉ | [Záznam arXiv](https://arxiv.org/abs/2609.39807) | metadáta arXiv |

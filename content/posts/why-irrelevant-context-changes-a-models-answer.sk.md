+++
title = "Prečo irelevantný kontext mení odpoveď modelu"
slug = "preco-irelevantny-kontext-meni-odpoved-modelu"
description = "Nová mechanistická štúdia sleduje irelevantný text promptu naprieč jazykovým modelom. Objavila osobitnú cestu, ktorá môže skresliť odpoveď, aj keď dodatočný text neposkytuje konkurenčný dôkaz."
tags = ["research", "agents"]
date = 2026-11-06T04:12:00+01:00
draft = false
+++

Predstavme si analytika, ktorý sa modelu opýta na hlavné mesto krajiny po tom, čo systém s vyhľadávaním vložil do promptu odsek o inom mieste. Odsek neobsahuje konkurenčné hlavné mesto. Neprotirečí otázke. Jednoducho s ňou nesúvisí. Napriek tomu klesne pravdepodobnosť, že model odpovie tým, čo už vedel.

Táto scéna je ilustratívna, no zlyhanie pozná každý, kto vytváral systém s vyhľadávaním alebo agenta s dlhým kontextom. Viac kontextu môže odpoveď zhoršiť. Nový preprint od Dikshanta Kukreju, Gautama Guptu, Avni Mittalovej a ich kolegov sa pokúša vysvetliť dôvod na úrovni vnútorného výpočtu modelu. Ich odpoveďou je „cesta prieniku“: irelevantný text sa obohatí, skopíruje dopredu a potom ho presadí malá skupina hláv mechanizmu pozornosti.

Rozlíšenie je dôležité, pretože väčšina obranných opatrení pristupuje k rušivému kontextu ako k problému lepšieho vyhľadávania, silnejších inštrukcií alebo väčších kontextových okien. Odborný článok kladie inú otázku. Keď už je irelevantný text v prompte, ktoré časti modelu mu umožnia ovplyvniť odpoveď?

## Rušivý text bez nesprávnej odpovede

Výskumníci začínajú faktickými vzťahmi, ktoré modely s otvorenými váhami poznajú, napríklad osobou a súvisiacim atribútom. Vytvárajú čisté prompty a niekoľko druhov dodatočného kontextu: súvisiace dôkazy, kontrafaktuálne dôkazy, krátky irelevantný text, dlhý irelevantný text a náhodný text. Ich základný súbor dát obsahuje 250 faktov, na ktoré správne odpovedajú aspoň tri zo štyroch základných modelov.

Takýto návrh oddeľuje rozpor od prieniku. Kontrafaktuálny odsek môže model ťahať ku konkrétnej nesprávnej odpovedi. Irelevantný text to robiť nemusí. Pravdepodobnosť správnej odpovede môže znížiť len tým, že na nesprávnych miestach vstúpi do výpočtu.

Experimenty používajú Llama 3.1 8B, Mistral 7B, Qwen 2.5 7B, Pythia 6.9B a GPT-2 XL, pričom pri jednom matematickom teste pridávajú väčšie modely. Žiadny model sa netrénuje. Verejný repozitár obsahuje skripty, ktoré vytvárajú súbory dát, vyberajú dotknuté hlavy a reprodukujú zásahy.

Prvý dôležitý výsledok ukazuje, kde sa poškodenie objaví. Dopredné vrstvy obohacujú reprezentácie predmetu otázky aj tokenov z irelevantného odseku. Niektoré hlavy pozornosti potom kopírujú materiál z predchádzajúceho textu k záverečnej pozícii, v ktorej musí model predpovedať odpoveď. Autori ich nazývajú papagájujúce hlavy. Druhá, riedka skupina hláv mení prenesený materiál na tlak na distribúciu výstupu.

## Vyhľadávanie a prienik nepoužívajú rovnaký okruh

Autori rozlišujú hlavy vyhľadávania, ktoré pomáhajú prenášať relevantné dôkazy, od hláv prieniku, ktoré prenášajú nežiaduci účinok. Tieto skupiny sa väčšinou neprekrývajú. Výsledok je preto užitočnejší než všeobecné tvrdenie, že pozornosť obsahuje šum. Systém môže potrebovať mechanizmus, ktorý prenáša dôkazy dopredu, a súčasne mu môže prospieť potlačenie oddelenej cesty, ktorá presadzuje rušivé prvky.

Odborný článok testuje kauzalitu a nespolieha sa iba na korelácie medzi vzormi pozornosti a chybami. Keď výskumníci nahradia záverečný reziduálny stav z rušeného behu zodpovedajúcim stavom z čistého behu, obnovia 97,6 % straty presnosti. Ide o orákulový zásah: vyžaduje čistý druhý priechod, takže nie je praktickou obranou v produkcii. Ukazuje však, že príslušné poškodenie sa dostalo do stavu posledného tokenu.

Výskumníci tiež maskujú vybrané hlavy prieniku. Tento zásah je v princípe nasaditeľný, pretože nevyžaduje čistý referenčný beh. Autori ho hodnotia na odložených vzťahoch a niekoľkých nadväzujúcich úlohách vrátane HotpotQA, PubMedQA a aritmetických súborov dát s rušivými výrokmi. Testujú aj to, či sa skupiny hláv prenášajú medzi modelmi a medzi základnými verziami a verziami doladenými na inštrukcie.

Obrana nie je zadarmo. Odstránenie hláv pozornosti môže odstrániť aj užitočný výpočet a záleží na tom, koľko hláv sa potlačí. Repozitár preto obsahuje testy viacerých počtov hláv a výberových prahov spolu s testmi stability na odložených dátach. Nejde o univerzálny prepínač, ktorý zabezpečí bezpečný kontext. Je to metóda na určenie užšieho kompromisu.

## Čo to mení na kontextovom inžinierstve

Generovanie rozšírené vyhľadávaním často pristupuje k relevantnosti ako k problému vyhľadávania. Vyhľadávač zoradí odseky, tvorca promptu vyberie ich počet a od modelu sa očakáva, že zvyšok odignoruje. Nová práca ukazuje, prečo môže posledný predpoklad zlyhať. Text môže ovplyvniť odpoveď bez toho, aby poskytol dôkaz alebo priamo súperil s pravdou.

Tvrdenie „odpoveď sa niekde v kontexte nachádzala“ preto nie je úplnou diagnózou. Dlhý prompt môže obsahovať správny dokument a napriek tomu znížiť presnosť, pretože nesúvisiace odseky aktivujú oddelenú cestu. Nadväzujúce testy autorov prepájajú analýzu okruhu s úlohami, v ktorých modely musia odpovedať na otázky alebo uvažovať cez doplnené výroky.

Výskum zároveň ukazuje hranicu bežnej reakcie na zlyhania kontextu: prikázať modelu, aby irelevantné informácie ignoroval. Inštrukcie pôsobia cez ten istý model, ktorý už spracúva rušivý text. Mechanistický zásah môže otestovať, či škodlivá cesta zostáva aktívna, aj keď model zdanlivo inštrukciu plní.

Platia dôležité obmedzenia. Ide o modely s otvorenými váhami, ktorých vnútorné aktivácie možno skúmať a meniť. Najjasnejšia analýza okruhov sa sústreďuje na modely výrazne menšie než dnešné najväčšie špičkové systémy. Faktické súbory dát sú kontrolované a výsledok orákulového obnovenia nemožno nasadiť v opísanej podobe. Text je preprint a neprešiel recenzným konaním.

Dôkazy sa napriek tomu dajú nezvyčajne dobre preskúmať. Repozitár uvádza modely, súbory dát, skripty, postup výberu hláv a testy citlivosti zásahov. Ďalší výskumníci môžu zisťovať, či sa rovnaké oddelenie vyhľadávania a prieniku objaví v iných architektúrach, väčších modeloch a skutočných produkčných záznamoch.

Ilustratívny tím inžinierov by teraz mohol neúspešnú odpoveď ladiť v dvoch krokoch. Najprv by sa opýtal, či vyhľadávanie poskytlo potrebný dôkaz. Potom by sa opýtal, či irelevantné odseky zmenili vnútornú cestu k odpovedi. Druhá otázka nenahrádza lepšie vyhľadávanie. Vysvetľuje, prečo môžu byť lepšie vyhľadávanie a menší počet čistejších odsekov dôležité, aj keď sa zdá, že model dokáže šum ignorovať.

Širšie ponaučenie je jednoduché: kontext nie je nečinným úložiskom. Každý ďalší odsek sa stáva súčasťou výpočtu. Kukreja a kolegovia zmapovali jednu cestu, ktorou môže nesprávny odsek zavážiť bez toho, aby uviedol nesprávnu odpoveď.

## Referencie

- Dikshant Kukreja, Gautam Gupta, Avni Mittal et al., „The Intrusion Pathway: How Non-Evidential Context Degrades Language Model Performance“ — https://arxiv.org/abs/2611.07778
- Dikshant Kukreja et al., kód a návod na reprodukciu práce „The Intrusion Pathway“ — https://github.com/dk4248/the-intrusion-pathway
- prispievatelia projektu TransformerLens, „TransformerLens“ — https://github.com/TransformerLensOrg/TransformerLens
- Javier Hernandez et al., súbor vzťahov použitý v experimentoch s vybavovaním faktov — https://github.com/evandez/relations
- Freda Shi et al., súbor dát „GSM-IC: A Benchmark for Understanding the Effects of Irrelevant Context in Mathematical Reasoning“ — https://github.com/google-research-datasets/GSM-IC

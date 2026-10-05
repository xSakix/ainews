+++
title = "Príklady zosilňujú symbolický obvod už prítomný v modeli"
slug = "priklady-zosilnuju-symbolicky-obvod-v-modeli"
description = "Štúdia interpretovateľnosti nachádza rovnakú dráhu abstrakcie, indukcie a vyhľadania ešte pred rastom úspešnosti pri niekoľkých príkladoch. Ukážky zrejme zosilňujú existujúci mechanizmus namiesto stavby nového algoritmu."
tags = ["research", "models"]
date = 2026-10-05T03:59:30+02:00
draft = false
+++

Keď sa jazykový model naučí vzor z niekoľkých príkladov v prompte, môže sa zdať, že si za pochodu zostavil nový postup. Mechanistická štúdia nezávislej výskumníčky Melissy Wessel ponúka pri jednej rodine symbolických úloh iné vysvetlenie: postup je už v modeli a príklady postupne zosilňujú signál, ktorý ním prechádza.

Preprint sleduje trojstupňový obvod v promptoch s nulovým až desiatimi príkladmi. Rovnakú základnú dráhu nachádza pri slabej aj takmer dokonalej úspešnosti. Príslušné pozornostné hlavy sa neobjavia náhle vo chvíli, keď model vzor „pochopí“. Rastie ich kauzálny prínos.

Ide o úzky experiment, nie všeobecnú teóriu učenia z kontextu. Pútavú metaforu, podľa ktorej príklady prebúdzajú skrytý mechanizmus, však mení na niečo, do čoho možno zasiahnuť a otestovať to.

## Od tokenov k premenným a späť

Úloha používa abstraktné trojtokenové vzory ako ABA alebo ABB. Tokeny sú náhodné, takže model sa nemôže spoliehať na ich bežný význam. Musí odvodiť, ktorú pozíciu má skopírovať do odpovede.

Predchádzajúca práca identifikovala tri stupne. Hlavy symbolickej abstrakcie menia konkrétne tokeny na premenné. Hlavy symbolickej indukcie pracujú s abstraktným vzorom. Hlavy vyhľadania menia predpovedanú premennú späť na požadovaný token. Wessel sleduje túto štruktúru v modeloch Gemma 2-2B, Llama 3.1-8B a Qwen 3-4B a mení iba počet ukážok.

Úspešnosť Gemma 2-2B začína pri jednom príklade na 17 %, pri štyroch dosahuje 93 % a pri desiatich 99 %. Kauzálna mediačná analýza však zachytí všetky tri stupne už pri jednom príklade. Najdôležitejšie hlavy sa medzi susednými dĺžkami promptu prevažne nemenia, zatiaľ čo kauzálny prínos jednej hlavy medzi jedným a desiatimi príkladmi narastie až osemnásobne.

Výklad je kvantitatívny, nie architektonický: ďalšie príklady zosilňujú existujúcu dráhu namiesto zapojenia úplne novej.

## Prenos signálu medzi promptmi

Samotná detekcia môže zameniť koreláciu za mechanizmus, preto práca prenáša vnútorné aktivácie medzi spusteniami. Prenesenie aktivácií z desiatich príkladov do promptu s jedným príkladom zvýši úspešnosť Gemmy zo 17 % na 88 %. Bez príkladov prenos stupňov indukcie a vyhľadania zvýši úspešnosť jedného vzoru z 1 % na 56 %; náhodné hlavy mimo obvodu ju ponechajú pod 1 %.

Najvýraznejší zásah používa „funkčný vektor“, teda pevnú aktiváciu zostavenú z hláv, ktoré označila kauzálna analýza. Jeho vloženie bez príkladov zvýši úspešnosť pravidla ABA z 1 % na 86 %. Po odstránení nadväzujúcich hláv vyhľadania záchranný účinok klesne na 13 %.

Táto závislosť je kľúčová. Vektor nefunguje ako samostatná odpoveď ani ako všeobecný impulz pre sieť. Do veľkej miery môže nahradiť stupeň indukcie iba preto, že neskorší mechanizmus vyhľadania dokáže prečítať jeho výstup.

## Užitočný výsledok v malej doméne

Štúdia vykresľuje učenie z kontextu skôr ako dodanie vstupu programu uloženému počas trénovania než ako zápis nového programu pri inferencii. Ak sa tento pohľad zovšeobecní, obmedzenia učenia z niekoľkých príkladov by záviseli od toho, ktoré obvody obsahujú váhy modelu a či sa k nim prompt dokáže dostať.

Práca neukazuje, že takto fungujú všetky ukážky. Hlavná úloha je v podstate malá relačná tabuľka s operáciou kopírovania. Kontrola na analógiách reťazcov písmen nachádza podobnú topológiu, ale neopakuje ju pri každom modeli ani s celým súborom prenosových zásahov. Analytická metóda navyše vyberá komponenty rozlišujúce dve pravidlá, takže môže vynechať spoločnú infraštruktúru.

Výsledok je najsilnejší ako konkrétny mechanizmus jednej jednoduchej schopnosti: príklady môžu zosilniť stabilnú symbolickú dráhu dávno predtým, než správanie odhalí jej prítomnosť.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Štúdia sleduje stupne abstrakcie, indukcie a vyhľadania v Gemma 2-2B, Llama 3.1-8B a Qwen 3-4B | OVERENÉ | [Preprint](https://arxiv.org/abs/2609.36265) | žiadne |
| Úspešnosť Gemmy stúpa zo 17 % pri jednom príklade na 99 % pri desiatich; prínos hlavy rastie až osemnásobne | PODĽA SPOLOČNOSTI | [Preprint](https://arxiv.org/abs/2609.36265) | žiadne; experimenty autorky |
| Prenos aktivácií z desiatich príkladov zvýši úspešnosť pri jednom príklade na 88 % a bez príkladov z 1 % na 56 % | PODĽA SPOLOČNOSTI | [Preprint](https://arxiv.org/abs/2609.36265) | žiadne; experimenty autorky |
| Vloženie funkčného vektora zvýši úspešnosť ABA bez príkladov z 1 % na 86 %, po odstránení vyhľadania klesne na 13 % | PODĽA SPOLOČNOSTI | [Preprint](https://arxiv.org/abs/2609.36265) | žiadne; experimenty autorky |
| Pri testovaných úlohách ukážky zosilňujú existujúci obvod namiesto vytvorenia nového | ANALÝZA | [Preprint](https://arxiv.org/abs/2609.36265) | výklad kauzálnych zásahov v práci |
| Zovšeobecnenie na bohatšie abstraktné uvažovanie zostáva otvorené | OVERENÉ | [Preprint](https://arxiv.org/abs/2609.36265) | uvedené obmedzenie |

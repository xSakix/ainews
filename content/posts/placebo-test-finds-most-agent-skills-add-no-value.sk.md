+++
title = "Placebový test nenašiel prínos väčšiny zručností agentov"
slug = "placebovy-test-nenasiel-prinos-vacsiny-zrucnosti-agentov"
description = "Predregistrovaný experiment porovnal deväť zručností Claude Code s rovnako dlhými neutrálnymi inštrukciami. Dve boli lacnejšie než placebo, jedna horšia a šesť bez štatistického rozdielu."
tags = ["research", "agents", "tools"]
date = 2026-10-07T03:57:57+02:00
draft = false
+++

V novom placebom kontrolovanom experimente väčšina populárnych zručností pre programovacie agenty neprekonala rovnako dlhé neutrálne inštrukcie.

Projekt skill-placebo otestoval deväť zručností Claude Code na 15 verejných úlohách zo SWE-bench Verified, Terminal-Bench 2.1 a OpenThoughts-TBLite. Každá zručnosť dostala pár s neutrálnym textom s rovnakým počtom tokenov, nainštalovaným rovnakým spôsobom.

## Prečo na tom záleží {#why-it-matters}

Vývojár môže po pridaní dlhého súboru inštrukcií pozorovať zmenu správania agenta a pripísať ju postupu v súbore. Experiment skúma, či je účinnou zložkou naozaj zručnosť, alebo iba dodatočný kontext, priming a variabilita vykonania, ktoré s ňou prišli.

Metóda bola zaregistrovaná pred prvým behom. Claude Opus 5.5 dokončil 30 pokusov v každom ramene, celkovo 450 zaznamenaných pokusov. Hlavným výsledkom boli náklady, sledovala sa aj úspešnosť úloh so štatistickou korekciou deviatich porovnaní.

Dve zručnosti boli lacnejšie než placebo: ponytail o 12 % a agent-skills o 5 %. Planning-with-files prešla v 80 % pokusov, kým jej placebo vo všetkých 30, preto bola podľa vopred zaregistrovaného pravidla projektu horšia. Ďalších šesť sa štatisticky nelíšilo od príslušného neutrálneho textu.

Ani jedna z deviatich nebola merateľne lacnejšia než beh bez zručnosti. Samotný neutrálny text placeba zmenil náklady oproti základu bez zručnosti o 2–16 %. Dĺžka promptu a zdanlivo nepodstatný kontext sú preto súčasťou zásahu, nie neškodným pozadím.

## Kontrola zlepšuje otázku, nie veľkosť vzorky

Základ bez zručnosti zisťuje, či celý balík mení výkon. Spárované placebo kladie presnejšiu otázku: či samotné inštrukcie prinášajú hodnotu nad rámec rovnakého množstva textu podaného rovnakým spôsobom. Obe porovnania sa môžu líšiť bez rozporu.

Repozitár zverejňuje predregistrovanú metódu, výsledky jednotlivých pokusov aj záznamy agentov. Eviduje aj zmenu zo 6. októbra: dva časové limity, pri ktorých testy neskôr prešli, boli podľa pôvodných pravidiel započítané ako neúspechy. Planning-with-files sa tým posunula z „bez zlepšenia“ na „horšia“ bez zmeny nákladov.

Obmedzenia sú výrazné. Pätnásť úloh a 30 pokusov na rameno necháva široké intervaly úspešnosti, hlavný beh zahŕňa jeden model a jeden nástroj a zvolené zručnosti sa sústreďujú na všeobecné programovacie postupy, nie špecializované znalosti. Súčasné záznamy tiež nedokazujú, ako dôsledne sa každá zručnosť počas behu aktivovala.

Malý pilot s Codexom skúšal iba tri zručnosti na piatich úlohách a je výslovne vedľajší. Jeho výsledky nemožno spájať s experimentom Claude ani ich považovať za porovnanie rodín modelov.

Zistenie neukazuje, že programovacie zručnosti sú zbytočné. Ukazuje, že popularita, dĺžka a vierohodný postup nenahrádzajú spárovanú kontrolu. Opakovateľným prínosom je návrh experimentu: vopred určiť metódu, dať kontrole rovnaký kontext, zachovať úplné záznamy a popri úspechu merať náklady.

Budúce verzie môžu výsledok posilniť ďalšími úlohami, inými nástrojmi a kontrolou s premiešanými inštrukciami, ktorá oddelí význam postupu od všeobecného primingu.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Hlavný experiment vykonal 450 pokusov s deviatimi zručnosťami na 15 verejných úlohách | OVERENÉ | [Repozitár skill-placebo](https://github.com/simonether/skill-placebo) | metóda, výsledky a záznamy sú verejné |
| Dve zručnosti prekonali placebo v nákladoch, jedna bola horšia a šesť nebolo lepších | PODĽA SPOLOČNOSTI | [Výsledky skill-placebo](https://github.com/simonether/skill-placebo) | žiadne; štatistická analýza autora |
| Ponytail bola o 12 % lacnejšia a agent-skills o 5 % lacnejšia než spárované placebo | PODĽA SPOLOČNOSTI | [Výsledky skill-placebo](https://github.com/simonether/skill-placebo) | žiadne |
| Planning-with-files prešla v 80 % prípadov oproti 100 % pri placebe | PODĽA SPOLOČNOSTI | [Výsledky skill-placebo](https://github.com/simonether/skill-placebo) | dáta jednotlivých pokusov sú dostupné |
| Ani jedna z deviatich zručností nebola merateľne lacnejšia než beh bez zručnosti | PODĽA SPOLOČNOSTI | [Výsledky skill-placebo](https://github.com/simonether/skill-placebo) | žiadne |
| Spárované kontroly izolujú obsah inštrukcií lepšie než základ bez zručnosti | ANALÝZA | [Registrovaná metóda](https://github.com/simonether/skill-placebo/blob/main/METHOD.md) | záver z návrhu experimentu |

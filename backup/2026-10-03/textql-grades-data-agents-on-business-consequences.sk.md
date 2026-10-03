+++
title = "TextQL hodnotí dátových agentov podľa dôsledkov rozhodnutí"
slug = "textql-hodnoti-datovych-agentov-podla-dosledkov-rozhodnuti"
description = "Argo-Bench skrýva skutočný stav simulácie za podnikovým dátovým skladom. Najsilnejší testovaný model vyriešil približne tretinu úloh."
tags = ["research", "agents"]
date = 2026-10-03T05:43:20+02:00
draft = false
+++

Argo-Bench od spoločnosti TextQL zistil, že aj silní dátoví agenti majú problém meniť podnikové záznamy na správne rozhodnutia. Najlepší testovaný model vyriešil približne tretinu úloh benchmarku.

Gabriel Tomitsuka a štyria kolegovia zo spoločnosti TextQL, ktorá vyvíja dátových agentov, vytvorili simulovaný podnik rozvážajúci jedlo a jeho záznamy sprístupnili v podnikovom dátovom sklade. Agenti ich môžu prehľadávať a analyzovať, no hodnotiaci systém pozná skutočný priebeh udalostí a hodnotí dôsledky ich odpovedí aj krokov.

**Prečo na tom záleží:** Finančný analytik, ktorý posudzuje rozpočtové odporúčanie agenta, potrebuje správny podnikový cieľ aj technicky správny výpočet. Argo-Bench umožňuje tento rozdiel merať: presvedčivá analýza môže dostať nízke skóre, ak jej rozhodnutie plytvá peniazmi.

[Preprint](https://arxiv.org/abs/2610.02122), prvýkrát predložený 1. októbra, opisuje 210 úloh z analytiky, prognózovania, odhaľovania podvodov a finančného plánovania. Autori testovali 14 špičkových modelov a modelov s otvorenými váhami. Celkovo viedol Claude Opus 5.5: podľa prahu autorov vyriešil približne 35 % úloh a dosiahol priemer okolo 60 bodov.

Úloha sa považuje za vyriešenú, keď jej skóre dosiahne aspoň 95. Tento prah sa líši od priemerného skóre: model môže získať čiastočné body v mnohých úlohách bez toho, aby ich dokončil na požadovanej úrovni. Tieto dve miery odpovedajú na odlišné otázky o spoľahlivosti.

Dátový sklad obsahuje približne 7,5 miliardy riadkov v 235 tabuľkách vo formáte Oracle E-Business Suite. Svet, z ktorého vychádza, simuluje rozvoz jedla v New Yorku v roku 2024. Objednávka vytvára súvisiace záznamy o pridelení rozvozu, odmene kuriéra, platbe prevádzke a účtovníctve, takže rekonštrukcia podnikovej udalosti vyžaduje spojenie správnych záznamov.

Simulátor predstavuje kľúč správnych odpovedí benchmarku. Podobne ako cvičenie, pri ktorom má vyučujúci celý spis prípadu, poskytuje agentovi neúplné prevádzkové dôkazy a zároveň uchováva dostatok skrytých informácií na kontrolu ich významu. Rozhodnutie o podvode preto možno hodnotiť podľa odvrátených strát aj nesprávne odstránených oprávnených tržieb.

## Správne výpočty môžu slúžiť nesprávnemu cieľu

Jedno opísané zlyhanie sa týka kuriérskych bonusov. Agent odhadol, ako bonusy ovplyvňovali dostupné hodiny práce kuriérov, a znížil výdavky tam, kde boli tieto hodiny najdrahšie. Deklarovaným ekonomickým cieľom platformy však bolo znížiť príplatky pri vysokej záťaži. Iný model preskúmal tento vzťah a našiel lepšie rozdelenie prostriedkov.

Chyba vznikla ešte pred výpočtom. Agent si vybral zdanlivo rozumnú mieru, ktorá nezodpovedala účelu rozhodnutia. Benchmark dokáže toto zlyhanie odhaliť, pretože jeho hodnotiaci systém posudzuje navrhnuté rozdelenie v tom istom simulovanom podniku, namiesto porovnávania dotazu s písomnou odpoveďou.

Analýza členstva ukázala iné zlyhanie. Niektorí agenti určovali členstvo podľa dátumov zmluvy, hoci odmietnutá platba mohla zrušiť výhody skôr, než zmluva zmizla. Úspešné behy rekonštruovali históriu platieb a porovnali ju s výhodami skutočne uplatnenými na objednávky. Platné spojenie tabuliek nestačilo, keď zobrazovalo nesprávny stav podniku.

Zverejnené výsledky zostávajú vlastnými meraniami autorov. TextQL vyvíja produkty v hodnotenej kategórii a preprint neposkytol nezávislú reprodukciu poradia modelov. Zverejnený dátový sklad sa navyše líši od sveta vytvoreného so súkromným inicializačným parametrom, ktorý sa použil na opísané experimenty a rebríček.

Simulácia má hranice. Zahŕňa jedno mesto, jeden rok a jeden formát podnikového systému. Verejné súhrnné údaje ohraničujú jej ekonomiku, no niektoré predpoklady o správaní majú slabú oporu; autori výslovne upozorňujú na členský program. Skóre teda porovnáva agentov v tomto vytvorenom prostredí, namiesto odhadu výkonu v skutočnej spoločnosti.

Agent pracuje v izolovanom prostredí Python s knižnicami na štatistiku a optimalizáciu. Výsledky odovzdáva cez rozhranie pre rozhodnutia, čo benchmarku umožňuje hodnotiť záväzné kroky agenta, namiesto samotného vygenerovaného textu.

Tím zverejnil [dátový sklad](https://huggingface.co/datasets/textql/Argo-Bench) aj [úlohy, referenčné riešenia a nástroje na vykonávanie](https://github.com/TextQLLabs/Argo-Bench). Tieto materiály umožňujú preskúmať logiku hodnotenia. Štúdia uvádza pridanie SAP S/4HANA a zložitejších záznamov viacerých podnikov ako rozšírenia nad rámec súčasného sveta vo formáte Oracle.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Tomitsuka a štyria spoluautori pracujú v TextQL; preprint v1 bol predložený 1. októbra 2026. | OVERENÉ | https://arxiv.org/abs/2610.02122 | žiadne |
| 210 úloh, 14 modelov; najlepší Opus 5.5 vyriešil 34,8 % pri skóre ≥95 a dosiahol priemer 59,5 bodu. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.02122 | žiadne |
| Simulovaný dátový sklad rozvozu jedla v NYC v roku 2024 má 235 tabuliek vo formáte Oracle EBS a 7,49 miliardy riadkov; hodnotiaci systém využíva skrytý stav a dôsledky rozhodnutí; izolovaný Python a rozhranie na odovzdávanie umožňujú vykonávanie. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.02122 | žiadne |
| Zlyhania rozdelenia bonusov a záznamov členstva ilustrujú nesprávne ciele a záznamy; verejný a hodnotiaci inicializačný parameter sa líšia. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.02122 | žiadne |
| Jedno mesto/rok/formát ERP a slabé predpoklady členstva obmedzujú zovšeobecnenie; navrhuje sa rozšírenie na SAP. | OVERENÉ | https://arxiv.org/abs/2610.02122 | žiadne |
| Dátový sklad a kód úloh/referenčných riešení/nástrojov sa ponúkajú verejne. | OVERENÉ | https://huggingface.co/datasets/textql/Argo-Bench ; https://github.com/TextQLLabs/Argo-Bench | žiadne |
| Finanční analytici potrebujú správny cieľ aj výpočty; prirovnanie ku spisu vyučujúceho vysvetľuje skrytý skutočný stav. | ANALÝZA | https://arxiv.org/abs/2610.02122 | žiadne |

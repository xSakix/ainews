+++
title = "SciCore znižuje citlivosť AI recenzií na formulácie"
slug = "scicore-znizuje-citlivost-ai-recenzii-na-formulacie"
description = "Kontrolovaný benchmark prepisuje rukopisy pri zachovaní ich vedeckého obsahu. Hodnotenie extrahovaného vedeckého záznamu spolu s rukopisom zlepšuje stabilitu bez sploštenia skóre."
tags = ["research", "agents"]
date = 2026-10-03T05:41:20+02:00
draft = false
+++

SciCore, systém na recenzovanie štúdií vyvinutý univerzitnými výskumníkmi, znižuje vplyv rétorických úprav na úsudky AI tým, že spája recenziu rukopisu s recenziou jeho extrahovaného vedeckého obsahu.

Chenguang Wang, Ming Li a spolupracovníci z Virginia Tech, University of Maryland a MBZUAI skúmajú, či AI recenzent odmeňuje zmenené formulácie, keď opísaná veda zostáva rovnaká. Ich metóda poskytuje recenzentovi druhý, štruktúrovaný pohľad na túto vedu.

**Prečo na tom záleží:** Organizátor konferencie využívajúci automatické recenzovanie potrebuje skóre, ktoré rozlišuje vedecké práce a zároveň zostáva stabilné pri štylistických zmenách. Štúdia meria obe požiadavky, pretože recenzent udeľujúci každej práci rovnaké skóre by pôsobil stabilne, no bol by nepoužiteľný.

[Preprint](https://arxiv.org/abs/2609.39027), prvýkrát predložený 30. septembra, predstavuje RobustReview, súbor vytvorený zo 60 anonymizovaných príspevkov na konferenciu strojového učenia ICLR. Každý originál dostáva desať druhov rétorických úprav vytvorených nezávisle dvoma modelmi, čím vzniká 1 260 verzií rukopisov.

Zásahy menia prvky ako tvrdenia o novosti, rámcovanie dôkazov, technický register či jazykovú zložitosť. Ďalšie varianty tieto zmeny kombinujú alebo opakujú prepisovanie. Zamýšľaný zásah mení prezentáciu pri zachovaní metód, výsledkov a obmedzení.

Autori hodnotia 30 konfigurácií recenzentov vrátane všeobecných modelov s rôznymi promptmi, špecializovaných vedeckých recenzentov a agentových recenzných systémov. Zisťujú, že opakované pokyny sústrediť sa na obsah neodstraňujú citlivosť na formulácie konzistentne. Aj prísnejší prompt mení, ktoré vedecké rozdiely recenzent rozpoznáva.

SciCore upravuje vstup aj pokyn. Jedna vetva recenzuje celý rukopis. Druhá extrahuje opísaný problém, tvrdenia, metódy, predpoklady, dôkazy, výsledky a obmedzenia do štruktúrovaného záznamu a priamo ho hodnotí. Konečné skóre predstavuje priemer oboch úsudkov.

Štruktúra pripomína hodnotenie návrhu aj jeho evidenčného listu. Návrh zachováva spôsob komunikácie argumentu; evidenčný list uľahčuje porovnávanie vedeckých záväzkov naprieč odlišne formulovanými verziami. Extrakcia však stále vyžaduje interpretáciu, takže chyby v liste môžu ovplyvniť výsledok.

## Stabilné skóre musí stále rozlišovať rôzne práce

Benchmark kontroluje pohyb skóre v každej rodine rukopisu aj oddelenie rôznych prác. Zároveň porovnáva skóre pôvodných rukopisov s priemermi ľudských recenzentov. Ide o odlišné testy: zhoda s ľuďmi pri origináli málo hovorí o tom, či prepis zmení rozhodnutie modelu.

V hlavnom experimente s GPT-5.5 SciCore zlepšil všetkých päť mier odolnosti oproti samotnej prísnej vetve celého rukopisu. Zachoval aj konkurencieschopnú zhodu s ľudskými skóre. Kombinovaný recenzent neviedol v každej jednotlivej miere a prísny GPT-5.5 si zachoval silnejšiu koreláciu s ľudským poradím.

Výsledok podporuje spojenie dopĺňajúcich sa pohľadov namiesto výberu zdanlivo najstabilnejšej súčasti. Vetva vedeckého záznamu sa pri prepisoch menila menej, no slabšie sa zhodovala s ľudskými skóre. Pridanie celého rukopisu obnovilo informácie, ktoré štruktúrovaný pohľad vynechal alebo spracoval odlišne.

Porovnanie všeobecných modelov zahŕňa GPT-5.5, GPT-5-mini, Claude Sonnet 5, GLM-5.2, Kimi-K2.6, GPT-OSS-120B, Gemini-3.5-Flash-Lite a Qwen-3.5-Flash. Prepisovacie modely sú GPT-5.5 a Claude Opus 4.8. Tieto voľby sú dôležité, pretože testovaný systém interpretuje pôvodnú vedu aj pomáha vytvárať jej zmenenú prezentáciu.

Hodnotenie zostáva vlastným experimentom autorov v preprinte. Vzorka rukopisov pochádza z jednej konferencie a prepisy zachovávajúce obsah občas zavádzajú nezhody. Priemerné ľudské skóre je tiež nedokonalou referenciou, ktorá skrýva rozdielne názory recenzentov. Tieto hranice obmedzujú zovšeobecnenie nameranej stability.

Konečný spojený recenzent bol testovaný s GPT-5.5. Ďalšie experimenty naprieč modelmi charakterizujú vetvu vedeckého záznamu, namiesto preukázania výkonu celej kombinácie pri každom modeli. Extrakcia záznamu pridáva náklady inferencie a môže vynechať či nesprávne vyložiť detaily.

Tím poskytuje [repozitár benchmarku a metódy](https://github.com/c-steve-wang/Robust_Review). Jeho zistenia konkretizujú zostávajúci problém: lepšia odolnosť voči formuláciám závisí od zachovania vedeckých rozdielov, ktoré odôvodňujú odlišné skóre.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Uvedené afiliácie Wanga, Liho a spolupracovníkov; v1 predložená 30. septembra 2026. | OVERENÉ | https://arxiv.org/abs/2609.39027 | žiadne |
| RobustReview: 60 rukopisov ICLR, 10 podmienok prepisu, dva generátory, 1 260 verzií; 30 konfigurácií recenzentov. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.39027 | žiadne |
| Menované všeobecné recenzenty, prepisovacie modely GPT-5.5/Opus 4.8 a porovnávané rodiny. | OVERENÉ | https://arxiv.org/abs/2609.39027 | žiadne |
| Dvojvetvová metóda extrakcie/recenzie/priemeru skóre; opakované obsahové pokyny nezlepšujú odolnosť konzistentne. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.39027 | žiadne |
| Kombinácia GPT-5.5 zlepšuje všetkých päť mier odolnosti oproti Manuscript-Strict; ICC 0,775, SPR 0,652, rozlíšenie 0,726; ľudské MAE 1,072, korelácia 0,488; nie najlepšia každá miera. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.39027 | žiadne |
| Obmedzenia konferencie/prepisov/ľudských skóre; kombinácia hodnotená len s GPT-5.5; náklady extrakcie a riziko vynechania. | OVERENÉ | https://arxiv.org/abs/2609.39027 | žiadne |
| Poskytnutý repozitár. | OVERENÉ | https://github.com/c-steve-wang/Robust_Review | žiadne |
| Dôsledok pre organizátora, zlyhanie konštantného skóre a prirovnanie návrhu/evidenčného listu vysvetľujú spoločnú stabilitu a rozlíšenie. | ANALÝZA | https://arxiv.org/abs/2609.39027 | žiadne |

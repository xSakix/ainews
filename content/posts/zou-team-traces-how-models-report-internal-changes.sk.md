+++
title = "Zouov tím skúma, ako modely hlásia vnútorné zmeny"
slug = "zouov-tim-skuma-ako-modely-hlasia-vnutorne-zmeny"
description = "Kontrolovaný preprint oddeľuje detekciu zmeny aktivácií od hlásenia jej polohy. Experiment používa nemenný vstupný text a hodnotí odpovede bez AI rozhodcu."
tags = ["research", "safety"]
date = 2026-10-04T09:26:37+02:00
draft = false
+++

Tím Jiahonga Zoua identifikoval dve skupiny pozornostných hláv, ktoré pomáhajú jazykovým modelom hlásiť zámerne vloženú vnútornú zmenu: jedna riadi samotné hlásenie a druhá pomáha určiť polohu zmeny.

Preprint predložený 28. septembra skúma úzku formu introspekcie. Výskumníci menia skryté aktivácie modelu, pričom viditeľný prompt zostáva rovnaký. Následne model požiadajú, aby označil zasiahnutú pozíciu alebo uviedol, že sa nič nezmenilo.

Inžinierovi skúmajúcemu riadenie aktivácií výsledok poskytuje konkrétne miesto, kde možno zisťovať, či model zásah zaznamenal. Riadenie aktivácií mení vnútorné reprezentácie modelu s cieľom ovplyvniť výstup; tento experiment skúma mechanizmus, ktorý takúto zmenu premieňa na výslovné hlásenie.

Zou a spoluautori uvádzajú pôsobiská na Shandong University, Tsinghua University, Northeastern University a University of Hong Kong. Testujú modely doladené na pokyny z rodín Qwen, Llama a Gemma, pričom odpovede hodnotia priamo z výstupných skóre modelu, bez samostatného jazykového modelu v úlohe rozhodcu.

Každý prompt obsahuje desať kandidátskych pozícií tokenov. Vložený konceptový vektor zmení skrytý stav na jednej pozícii, zatiaľ čo kontrolný beh nemení nič. Vektor vzniká z rozdielu medzi aktiváciami vyvolanými konceptom a priemerom aktivácií slov zo slovníka.

Model vyberá medzi označeniami pozícií a odpoveďou, že nenastala zmena. Hodnotenie používa prvú výstupnú pozíciu, ešte predtým, ako by vygenerované vysvetlenie mohlo poskytnúť ďalšie vodidlá. Výskumníci tiež menia označenia medzi číslicami, písmenami a slovami a premiešavajú ich poradie, aby preverili, či úspech nevysvetľuje pevné spojenie označení s pozíciami.

Všetky tri modely lokalizujú zmeny lepšie než náhodný výber pozície použitý ako základ porovnania, výsledky však výrazne závisia od formátu označení. Autori volia nastavenia zásahu na samostatných kalibračných dátach a ponechávajú koncepty, ktoré v nich fungujú najlepšie. Test preto meria výkon vo vybranej skupine konceptov, nie citlivosť na ľubovoľnú vnútornú zmenu.

## Detekcia zmeny a určenie jej polohy sa rozchádzajú

Kľúčový dôkaz pochádza z nahrádzania výstupov vybraných pozornostných hláv výstupmi zo zodpovedajúceho párového behu. Pozornostná hlava prenáša informácie medzi pozíciami tokenov; nahradenie jej výstupu umožňuje skúmať jej príspevok k odpovedi.

Hlavy v stredných vrstvách ovplyvňujú, či model vôbec ohlási nejakú pozíciu. Autori ich nazývajú gate heads. Malá skupina v neskoršej vrstve pomáha vybrať, ktorú pozíciu model ohlási, a dostala názov router heads.

Zásah do gate heads môže potlačiť hlásenie pozície aj vtedy, keď router heads stále nesú informáciu o polohe. Naopak, nahradenie výstupov router heads výstupmi z behu bez zásahu znižuje presnosť lokalizácie. Presmerovanie ich pozornosti pomáha preveriť vzťah medzi tým, kam smeruje pozornosť, a vybranou pozíciou.

Toto oddelenie je najsilnejším zistením práce. Informácia o zásahu môže v modeli zostať, hoci odpoveď tvrdí, že zásah nenastal. Slovné hlásenie modelu je preto výsledkom konkrétneho mechanizmu hlásenia, nie úplným súpisom informácií v jeho skrytom stave.

Autori obmedzujú analýzu na šesť variantov úlohy, jednu vybranú vrstvu a intenzitu zásahu pre každý model a modely s najviac 12 miliardami parametrov. Výslovne skúmajú funkčné hlásenie a netvrdia nič o vedomí ani subjektívnom prežívaní.

Voľné a spontánne hlásenia zostávajú mimo testovanej úlohy. Práca ich uvádza ako ďalší smer výskumu spolu s inými typmi zásahov a úlohou komponentov, ktoré spracúvajú informácie v rámci jednej pozície. Autori zverejnili kód, rozdelenia dát a skripty na reprodukciu obrázkov a tabuliek.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Preprint predložený 28. septembra; autori a uvedené univerzitné pôsobiská | OVERENÉ | [Zdroj](https://arxiv.org/abs/2609.35108) | žiadne; publikácia je preprint |
| Qwen3-4B-IT, LLaMA-3.1-8B-IT a Gemma-3-12B-IT; nemenný text, desať pozícií, vloženie konceptového vektora alebo kontrolný beh bez zásahu; priame hodnotenie prvého výstupu | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.35108) | žiadne; metódy autorov |
| Samostatná kalibrácia; 300 najlepších konceptov rozdelených do oddelených skupín; šesť nastavení označení a premiešané označenia; výkon prekračuje náhodný výber s 10 % úspešnosťou, no závisí od označení | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.35108) | žiadne; metódy a tabuľka 1 |
| Gate heads ovplyvňujú, či vznikne hlásenie; neskoršie router heads ovplyvňujú polohu; nahrádzanie výstupov a presmerovanie pozornosti podporujú oddelenie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.35108) | žiadne; kauzálne experimenty autorov |
| Vnútorná informácia o polohe môže zostať zachovaná aj bez hlásenia pozície; význam pre sledovanie zásahov do aktivácií | ANALÝZA | [Zdroj](https://arxiv.org/abs/2609.35108) | Úsudok zo zásahov do gate/router heads; nejde o výsledok nasadeného monitorovania |
| Obmedzenia rozsahu; funkčná introspekcia namiesto prežívania; otázky ďalšieho výskumu; zverejnený kód a reprodukčné skripty | OVERENÉ | [Zdroj](https://arxiv.org/abs/2609.35108) | žiadne; deklarovaný rozsah práce a odkaz na repozitár |

+++
title = "MASS trénuje jeden model cez tímy agentov"
slug = "mass-trenuje-jeden-model-cez-timy-agentov"
description = "Sakana AI a UC Berkeley používajú jeden model na návrh, vykonanie a hodnotenie viacagentových tokov, potom ho trénujú na najlepších tímových výstupoch."
tags = ["research", "agents"]
date = 2026-10-12T03:58:37+02:00
draft = false
+++

Sakana AI a UC Berkeley predstavili MASS, tréningovú metódu, v ktorej sa jeden model zlepšuje navrhovaním tímov agentov, hodnotením ich práce a učením z najlepších výsledkov.

Preprint sa zameriava na výskumné úlohy bez kontroly kompilátorom či presným riešením. Namiesto ručného nastavenia toku rovnaký model píše roly, inštrukcie, výstupné zmluvy a poradie volaní, vykonáva tím a hodnotí odpovede.

## Prečo je to dôležité {#why-it-matters}

Pre tím budujúci výskumných agentov je návrh pracovného toku obyčajne ďalším ručným projektom promptov. MASS ho mení na súčasť tréningu a pri nasadení viacagentový aparát odstráni, takže zlepšený model odpovedá bez platenia celej vyhľadávacej slučky.

Metóda má dve slučky. Vo vnútornej optimalizátor navrhuje písané štruktúry tímu a vykonávateľ ich spúšťa. Hodnotiteľ vyberá silnejšie odpovede v úlohách bez automatickej pravdy. Vo vonkajšej slučke sa model dolaďuje na vybraných behoch a stáva sa východiskom ďalšieho kola.

Autori prirovnávajú proces k samohre, no protivníkom nie je iný hráč. Model vytvára čoraz náročnejšie formy spolupráce svojich kópií a najlepšie správanie vstrebáva do jedného checkpointu. Topológia tímu je dočasným tréningovým lešením.

## Rozhodujúca je kvalita výberu

MASS používa hodnotenie modelom, pretože cieľové otázky nemajú deterministické orákulum. Práca používa ako oddelených rozhodcov aj GPT-5.5 a Claude Opus 4.8. Sakana uvádza vyššiu hodnotenú kvalitu pri menšom počte výstupných tokenov než pri tímoch, ktoré vytvorili tréningové dáta.

Dôkaz však zostáva vnútorný svetu modelového hodnotenia. Rozhodca môže uprednostniť uhladené, známe či dlhšie odpovede bez overenia pravdivosti. Oddelení rozhodcovia obmedzujú priame prispôsobenie jednému hodnotiteľovi, no neposkytujú faktickú pravdu. Výsledok preto platí v rámci protokolu práce.

Postup sa snaží zabrániť pripútaniu k jednému šťastnému toku. Každá generácia spustí turnaj šampiónov osemnásťkrát a na doladenie ponechá najlepších šestnásť stôp. Optimalizátor môže meniť roly, poradie komunikácie aj výstupné formáty.

Tvrdenie obmedzuje aj zdieľaný model. Vykonávateľ, optimalizátor a hodnotiteľ sú roly jednej rodiny, nie nezávisle špecializované systémy. To uľahčuje pripísanie zlepšenia slučke, no neukazuje, či rôznorodé tímy nájdu iné stratégie.

## Pracovný tok po tréningu zmizne

Najjasnejšou praktickou vlastnosťou je destilácia do základného modelu. Používateľ pri nasadení nemusí opakovať osemnásť behov ani udržiavať graf tímu. Dodatočný výpočet sa sústreďuje na tvorbu dát a tréning, kým inferencia používa výsledný model priamo.

Práca aj opis projektu sú verejné. Nezávislá replikácia musí ukázať, či zisk prežije iných rozhodcov, faktické overenie a úlohy mimo výskumnej sady autorov.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislá kontrola |
|---|---|---|---|
| MASS používa jeden model ako optimalizátor, vykonávateľa a hodnotiteľa a dolaďuje ho na vybraných behoch | OVERENÉ | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| Vnútorná slučka hľadá roly, pokyny, výstupné zmluvy a poradie volaní | OVERENÉ | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| Autori uvádzajú vyššiu hodnotenú kvalitu pri menšom počte výstupných tokenov | PODĽA SPOLOČNOSTI | https://pub.sakana.ai/mass/ | žiadna |
| GPT-5.5 a Claude Opus 4.8 slúžia v hodnotení ako oddelení rozhodcovia | OVERENÉ | https://arxiv.org/abs/2610.12176 | žiadna |
| Modelové hodnotenie samo nedokazuje faktickú správnosť | ANALÝZA | https://arxiv.org/abs/2610.12176 | žiadna |

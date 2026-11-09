+++
title = "Kód študentov sa strojnásobil, komentárov nepribudlo"
slug = "kod-studentov-sa-strojnasobil-komentarov-nepribudlo"
description = "Desaťsemestrová štúdia 260 tímových repozitárov záverečných projektov zistila, že kód na konci semestra vzrástol z približne 3,4 na približne 10 tisíc riadkov, keď sa generatívna AI stala široko dostupnou, zatiaľ čo podiel komentárov zostal rovnaký. Autori používanie AI nepozorovali, výsledok je preto varovaním pre hodnotiteľov a zamestnávateľov, nie rozsudkom nad nástrojmi."
tags = ["research", "tools"]
date = 2026-11-09T03:16:01+01:00
draft = false
+++

Predstavte si koordinátorku predmetu v piatok pred uzávierkou známok. Má tabuľku so štyridsiatkou študentských tímov a zvyk, ktorý si udržiava roky: otvoriť repozitár, pozrieť sa, koľko sa postavilo a ako rovnomerne, a podľa toho si urobiť obraz o tom, kto pracoval. Tento rok má prvý repozitár na zozname desaťtisíc riadkov kódu a tristo commitov. Prelistuje funkciu s hlboko vnorenými vetvami a nenájde jediný komentár, ktorý by čokoľvek vysvetľoval. Koordinátorka je vymyslená, zastupuje problém, ktorý teraz zmerali traja výskumníci.

Štúdia „Code, Commits, and Complexity in the GenAI Era“ vyšla 5. novembra na arXive a bola prijatá na sympózium SIGCSE Technical Symposium vo februári 2027. Jej autormi sú Asma Shakil a Paul Denny z Aucklandskej univerzity a Claus Brabrand z IT University of Copenhagen. Analyzovali 260 tímových repozitárov z povinného predmetu záverečného ročníka, rozložených na desať semestrov od roku 2021 do roku 2025. Kódové základne na konci semestra vzrástli z mediánu približne 3,4 tisíc riadkov v rokoch 2021 až 2023 na približne 10 tisíc v rokoch 2024 a 2025. Autori nepozorovali, že by niekto AI používal, a opakovane to zdôrazňujú.

## Jeden predmet, desať semestrov

V predmete budujú päť- až šesťčlenné tímy počas trinástich týždňov softvér pre skutočných externých klientov. Hlavným hodnoteným výstupom je funkčný prototyp. Repozitáre pochádzajú z organizácie predmetu na GitHube: najprv ich bolo 302, po vyradení prázdnych, šablónových a duplicitných ich zostalo 260. Ročníky 2021 až 2025 majú postupne 19, 65, 57, 51 a 68 repozitárov.

Autori každý repozitár merajú dvakrát, pri priebežnej prezentácii v 7. týždni a pri záverečnej prezentácii v 13. týždni. Riadky kódu počítajú nástrojom tokei, priemernú cyklomatickú zložitosť na funkciu nástrojom lizard a lexikálne spočítavajú konštrukcie na ošetrenie chýb. Počítajú aj commity. Pri každej metrike testujú, či naprieč piatimi ročníkmi stúpa alebo klesá plynulo, s korekciou na počet testovaných metrík.

Roky rozdelili na obdobie nižšej a obdobie vyššej dostupnosti generatívnej AI, pričom približnou hranicou je vydanie ChatGPT v novembri 2022. Zdôrazňujú, že hranica nie je ostrá. GitHub Copilot sa pre overených študentov stal bezplatným v júni 2022 a jeho používanie sa potom rozširovalo postupne. Citujú prieskum Higher Education Policy Institute, podľa ktorého podiel britských vysokoškolákov používajúcich generatívnu AI na hodnotené práce vzrástol z 53 % koncom roka 2023 na 88 % koncom roka 2024.

## Čo sa zmenilo a kedy

Medián záverečnej kódovej základne bol v roku 2021 2,3 tisíca riadkov, v roku 2022 3,7 a v roku 2023 3,4. Potom skočil na 7,7 v roku 2024 a na 11 v roku 2025. Priebežný snímok má rovnaký tvar, od 1,4 až 1,8 tisíca riadkov pred rokom 2024 po 4,8 tisíca v roku 2025. Ročník 2023, prvý po ChatGPT, vyzerá ako tie staršie a autori ho nazývajú prechodným.

Medián commitov na repozitár stúpol zo 63 v roku 2021 a približne 100 až 112 v rokoch 2022 a 2023 na 265 v roku 2024 a 300 v roku 2025. Počet commitov na aktívny deň vzrástol z 3,3 na 5,4. Veľkosť jednotlivého commitu sa takmer nezmenila: medián zostal medzi 38 a 65 zmenenými riadkami. To oslabuje bežné očakávanie, že kód napísaný AI prichádza v niekoľkých veľkých dávkach. Títo študenti commitovali častejšie, v kúskoch približne rovnako veľkých ako predtým.

Najvýraznejší výsledok sa týka toho, čo je v kóde. Priemerná cyklomatická zložitosť stúpla z 1,7 v roku 2021 na 2,5 v roku 2025 a konštrukcie na ošetrenie chýb na tisíc riadkov z 3,7 a 4,8 v rokoch 2022 a 2023 na 12 a 13 v rokoch 2024 a 2025. Hustota komentárov, teda podiel riadkov, ktoré sú komentárom, nevykázala jasný trend; v roku 2021 bola 9,2 % a v roku 2025 8,4 %. Autori tento vzorec nazývajú „complexity without commentary“ (zložitosť bez komentárov). Neskoršie ročníky odovzdali kód väčší a spletitejší, ale nie lepšie vysvetlený.

## Čo autori netvrdia

Shakil, Brabrand a Denny obmedzenia uvádzajú otvorene. Používanie AI nepozorovali, preto hlásia zmeny, ktoré sa časovo zhodujú s vyššou dostupnosťou, nie jej účinky. Za tie roky sa menil personál, kritériá hodnotenia aj typy projektov, ročník 2021 a časť ročníka 2022 pracovali sčasti pod covidovými obmedzeniami a ročník 2021 má iba 19 repozitárov. Frameworky a šablóny projektov môžu pridať štandardný kód aj samy od seba. Zloženie jazykov sa posunulo k JavaScriptu a TypeScriptu, ktoré tvorili 42 až 58 % repozitárov v rokoch 2021 až 2023 a 71 až 74 % v rokoch 2024 a 2025; po obmedzení na 157 repozitárov v týchto jazykoch platí všetkých päť významných trendov naďalej.

Metriky sú len približné ukazovatele. Počet konštrukcií na ošetrenie chýb je lexikálny a cyklomatická zložitosť, ako píšu autori, „relates weakly to how hard code is to understand“ (iba slabo súvisí s tým, ako ťažko sa kód chápe). Keďže pochádza z iného nástroja než počet komentárov, žiadajú, aby sa zistenie o zložitosti bez komentárov čítalo na úrovni ročníkov. Všetko pochádza z jedného predmetu na jednej inštitúcii.

## Kde sa to zaraďuje medzi ostatné dôkazy

Štúdia nadväzuje na staršiu prácu. Y. Zhang a kolegovia v preprinte z januára 2026 sledovali nezmenené zadanie z predmetu o cloud computingu počas piatich semestrov pred ChatGPT a piatich po ňom. Záverečné odovzdania boli dlhšie, úpravy medzi odovzdaniami väčšie a zlepšenie skóre na jednu úpravu menšie. Tím z Aucklandu nachádza podobný rast veľkosti pri dlhšom tímovom projekte, hoci bez rovnakého vzorca vo veľkosti commitov.

Dve ďalšie štúdie dávajú rastu kontext. S. Peng a kolegovia zistili v kontrolovanom experimente z roku 2023, že vývojári s GitHub Copilotom dokončili úlohu s HTTP serverom o 55,8 % rýchlejšie. Randomizovaná štúdia J. H. Shen a A. Tamkina z roku 2026 zistila, že vývojári, ktorí sa s pomocou AI učili novú knižnicu na asynchrónne programovanie, mali horšie pojmové porozumenie, čítanie kódu a ladenie, a to bez významného zrýchlenia v priemere. Autori z Aucklandu tento výsledok citujú na zdôraznenie svojej obavy: píšu, že ide o to, že kód navyše sa môže ťažšie kontrolovať a že silné spoliehanie sa na AI môže oslabiť zručnosti potrebné na jeho kontrolu.

Pre učiteľov je praktický záver o meraní. Objem kódu a počet commitov, ktoré mohol vyučujúci predtým čítať ako snahu, prudko vzrástli a väčšia a častejšie commitovaná kódová základňa už nie je dôkazom väčšieho učenia. Autori navrhujú ústne obhajoby, prechádzanie kódu spolu so študentmi a výslovné požiadavky na dokumentáciu. Zamestnávatelia, ktorí čítajú absolventove repozitáre ako portfólio, stoja pred rovnakým problémom.

Predstavte si koordinátorku znova, o týždeň neskôr, v miestnosti s jedným tímom. Repozitár neotvára. Požiada študentku, aby vybrala ľubovoľnú funkciu a vysvetlila, prečo sa vetví tak, ako sa vetví. Vymyslená študentka ju pomaly prečíta a pripustí, že ju nikdy predtým nevidela. Či kód pochádzal z nástroja, od spolužiaka alebo z jej vlastnej neskorej noci, tento rozhovor koordinátorke povie to, čo počet riadkov nedokázal.

## Použité zdroje

- Azeem, S., Naveed, M. S., Sajid, M., & Ali, I. (2025). *AI vs. human programmers: complexity and performance in code generation*. VAWKUM Transactions on Computer Sciences, 13(1), 201-216.
- Freeman, J. (2025). *Student generative AI survey 2025*. Higher Education Policy Institute, HEPI Policy Note 61.
- Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. https://arxiv.org/abs/2302.06590
- Shakil, A., Brabrand, C., & Denny, P. (2026). *Code, Commits, and Complexity in the GenAI Era: A Longitudinal Study of Team-Based Capstone Projects*. https://arxiv.org/abs/2611.07297
- Shen, J. H., & Tamkin, A. (2026). *How AI Impacts Skill Formation*. https://arxiv.org/abs/2601.20245
- Zhang, Y., Savelka, J., Goldstein, S., & Conway, M. (2026). *Changes in Coding Behavior and Performance Since the Introduction of LLMs*. https://arxiv.org/abs/2601.11835

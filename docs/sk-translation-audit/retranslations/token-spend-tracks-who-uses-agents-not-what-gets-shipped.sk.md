+++
title = "Spotreba tokenov odráža, kto používa agentov, nie čo sa dodalo"
slug = "spotreba-tokenov-meria-pouzivanie-agentov-nie-dodanu-pracu"
description = "Štúdia JetBrains spojila päť týždňov spotreby tokenov v kódovacích agentoch s commitmi 404 inžinierov. Spotreba závisela oveľa viac od človeka než od týždenného výkonu, čo spochybňuje rebríčky, ciele a rozpočty postavené na tomto čísle."
tags = ["business", "research", "agents"]
date = 2026-11-11T03:23:00+01:00
draft = false
+++

Predstavme si vedúcu platformového inžinierstva, ktorá v pondelok ráno otvorí mesačnú faktúru od svojho dodávateľa AI. Položka za kódovacích agentov opäť narástla a do stredy ju má vysvetliť. Nakreslí si najzrejmejší graf: na jednej osi spotrebu na inžiniera, na druhej zlúčenú prácu. Čaká stúpajúcu čiaru. Dostane však rozsypané konfety. Spotreba dvoch inžinierov s rovnakým výkonom sa líši mnohonásobne a ona nevie prečo a najintenzívnejší používateľ nie je ten, ktorého prácu by vyzdvihla. Táto scéna je vymyslená; pomáha vidieť problém skôr, než prídu čísla.

Čísla už existujú. Tím z JetBrains, Carnegie Mellon University a University of California, Irvine zverejnil 10. novembra preprint s názvom „The AI Era's Lines of Code?“, ktorý skúma, čo vlastne meria spotreba tokenov inžiniera. Autormi sú Shyam Agarwal, Olga Lvova, Agnia Sergeyuk, Anastasiia Serova, Timofey Bryksin, Thomas Zimmermann a Bogdan Vasilescu. Ich odpoveď, ku ktorej dospeli na dátach jednej firmy, znie, že spotreba meria, do akej miery človek pracuje cez agentov, a o tom, čo vytvorí, hovorí máločo. Štúdia neprešla recenzným konaním.

## Metrika zavedená skôr, než ju niekto otestoval

Firmy začali používať spotrebu tokenov ako manažérske číslo skôr, než ju niekto preskúmal, a autori to otvorene uvádzajú. Odvolávajú sa na rebríček, ktorý si zamestnanec Mety vytvoril, aby kolegovia súťažili o titul najväčšieho spotrebiteľa tokenov v spoločnosti; Fortune v apríli informoval, že ho stiahli dva dni po tom, čo o ňom napísala tlač. Citujú vedúcich predstaviteľov Nvidie a Mety, podľa ktorých by dobrý inžinier mal míňať tokeny v hodnote veľkej časti svojho platu, firmu Salesforce, ktorá stanovila minimálne mesačné ciele spotreby, a analytických dodávateľov, ktorí vydelia náklady na tokeny počtom zlúčených pull requestov a podiel nazvú návratnosťou investície.

Pochybnosti odvtedy rastú. Podľa štúdie Uber minul rozpočet na AI nástroje na programovanie na rok 2026 za štyri mesiace a jeho prevádzkový riaditeľ povedal, že väzba medzi spotrebou tokenov a dodanými funkciami „tam ešte nie je“. Kritik, ktorého štúdia cituje, označil spotrebu tokenov za „metriku riadkov kódu éry AI: ľahko merateľnú, ľahko zneužiteľnú a odtrhnutú od skutočnej produktivity“. Podľa autorov, ktorí sa opierajú o tlačové správy, Meta odvtedy inžinierom oznámila, že počty tokenov sa nebudú používať na hodnotenie ich prínosu, a Amazon zrušil rebríček využívania a označil používanie tokenov za „zásadne chybné“ meradlo. Otvorená zostávala otázka, či kritika obstojí, keď niekto prepojí záznamy o používaní so skutočným výstupom.

## Čo ukazuje telemetria

JetBrains, ktoré vyvíja nástroje pre softvérový vývoj a v čase štúdie malo asi 2 600 zamestnancov, prevádzkuje internú bránu, ktorá zaznamenáva každé volanie kódovacieho agenta. Výskumníci vzali päť úplných týždňov od 29. júna do 2. augusta 2026 a priradili týždenné tokeny každého inžiniera k jeho commitom. Panel zahŕňa 404 inžinierov; záznamy obsahujú 3,1 milióna volaní agentov. Samostatný anonymný firemný prieskum oslovil 412 zamestnancov.

V rámci každého pásma týždenných počtov commitov použil inžinier v 90. percentile spotreby v danom týždni 39- až 240-krát viac tokenov než ten v 10. percentile. Pri sledovaní jedného človeka z týždňa na týždeň vyšiel plochší obraz, než autori čakali. Týždeň s dvojnásobným počtom commitov oproti obvyklému stál približne o 20 % viac tokenov. Opačným smerom: týždeň s dvojnásobným počtom tokenov priniesol len asi o 10 % viac commitov. Ak by výstup rástol úmerne so spotrebou, obe čísla by sa blížili k 100 % a autori úmernosť zamietajú pri každej časovej jednotke, ktorú skúšali.

Veľká časť variability súvisí s osobou. To, kto inžinier bol, vysvetľovalo 79 % variability týždenných tokenov a najintenzívnejšia tretina používateľov spotrebovala 79 % všetkých tokenov. Ľudia, ktorí míňali najviac, zostali počas piatich týždňov tí istí. Commity, zmenené riadky a dve ďalšie metriky aktivity spolu vysvetlili 38 % rozdielov medzi inžiniermi a 13 % rozdielov medzi týždňami u jedného inžiniera. Samotná rola a tím predpovedali spotrebu horšie než obyčajný priemer.

Štúdia sa potom zaoberá otázkou, kam ide prebytok. Týždne bez jediného commitu tvoria len 4 % tokenov, no autori z kriviek s najlepším prispôsobením odhadujú, že až asi dve pätiny spotreby sa s commitmi daného týždňa nemenia. Ide o hornú hranicu, pretože zahŕňa fixný náklad na samotné používanie agenta aj spotrebu za commitmi napísanými ručne. Poznamenávajú tiež, že väčšinu tokenov tvorí kontext posielaný znova pri každej výmene správ a že v treťom týždni prišiel nový špičkový model, ktorý do dvoch týždňov zaberal 45 % všetkej spotreby.

## Práca, ktorá sa nikdy nestane commitom

Časť rozdielu vysvetľuje prieskum. Z 197 hodnotení dvoch kódovacích agentov od technických respondentov odpovedalo na otázky o uplynulom týždni 167. V 91 % z nich respondenti uviedli, že im nástroj ušetril čas, v mediáne 10 hodín. Agentov použili na programovanie v 63 % hodnotení a aspoň na jednu inú činnosť v 89 %: analýzu dát, brainstorming, výskum témy, plánovanie, učenie, písanie. Respondenti, ktorí agenta používali iba na programovanie, uviedli v mediáne 3 ušetrené hodiny; tí, ktorí uviedli dve a viac použití mimo programovania, uviedli 10.

Časť hodnoty tvorí práca, ktorá by inak nevznikla. Na otázku o hlavnom prínose agenta 31 % zo 74 vecných odpovedí uviedlo rýchlosť pri obvyklých úlohách a 30 % prácu v neznámom kóde, doméne alebo technológii; jeden respondent napísal: „Môžem skúšať veci, ktoré som sa bál skúšať.“ Z 44 opisov práce, ktorá vznikla len vďaka existencii agenta, sa 36 % týkalo neznámeho codebasu, jazyka alebo stacku. Prieskum zaznamenáva aj náklady. Najčastejším bol nesprávny alebo nekvalitný výstup, ktorý uviedlo 49 % odpovedí, a 31 % technických používateľov agentov hlásilo vyššiu kognitívnu záťaž. Autori dodávajú, že sebahodnotenia môžu prínos nadsadzovať, a odvolávajú sa na randomizovanú štúdiu z roku 2025, v ktorej skúsení vývojári open-source projektov pracovali s AI nástrojmi o 19 % dlhšie, hoci verili, že sú rýchlejší.

## Čo to znamená pre ciele, rozpočty a stropy

Autori nedospeli k záveru, že agenti sú slabá investícia. Ich záver sa týka meradla. Ak by súvislosť v rámci jedného inžiniera bola kauzálna, zdvojnásobenie jeho spotreby stanovením cieľa by zvýšilo počet commitov asi o 10 %, v rozpätí od 2 do 25 %. Odporúčajú inžinierov nehodnotiť podľa spotreby a neočakávať, že ciele výrazne zvýšia výstup. Aj delenie spotreby výstupom zavádza, no inak: počet tokenov na commit s rastúcim počtom commitov mechanicky klesá, takže inžinier pôsobí v rušnom týždni efektívnejšie.

Najmenej pohodlne vychádzajú stropy. Strop dopadne najmä na najintenzívnejších používateľov, ktorých podiel spotreby nesúvisiacej s výstupom je z troch skupín najnižší, 36 %, oproti 51 a 52 % u ostatných. Keďže spotrebujú väčšinu tokenov, majú aj väčšinu nesúvisiacej spotreby, takže strop odstráni spotrebu, ktorá slúži výstupu, spolu s tou, ktorá mu neslúži, a počet tokenov nepovie, ktorá je ktorá. Pred zavedením stropu autori navrhujú skúsiť stláčať alebo riadiť kontext, cachovať opakovaný kontext, smerovať rutinné volania na lacnejšie modely a merať fakturované náklady, nie tokeny, pretože orezanie kontextu môže účet zvýšiť, ak agent znova číta, čo z neho vyradili.

Dôležité sú dve obmedzenia. JetBrains vyvíja AI nástroje na programovanie, takže časť meraného používania môže byť testovaním vlastných agentov, a jeho inžinieri pracujú na zavedených codebasoch. Používanie bolo dobrovoľné a bez cieľa, takže rozdiely v spotrebe čiastočne odrážajú osobnú voľbu. Commity navyše nezachytávajú prácu na revíziách a dizajne. Autori zdôrazňujú, že ide o asociácie z jednej firmy za päť týždňov.

Druhá štúdia, od čiastočne prekrývajúcej sa skupiny autorov, ukazuje, čo sa stane, keď sa cieľ nariadi. Na dátach 802 vývojárov a 196 212 pull requestov skúma strednú firmu, ktorej technologický riaditeľ v júni 2025 stanovil cieľ zdvojnásobiť počet zlúčených pull requestov na inžiniera pomocou AI. Firma cieľ splnila až v desiatom mesiaci a náklad padol na revíziu kódu, kde sa záťaž na jedného revízora zdvojnásobila.

## Merať správnu vec

Autori z JetBrains navrhujú dve opravy. Brány by mali zaznamenávať, ktorej úlohe alebo tiketu relácia agenta slúžila, aby sa spotreba dala spájať s výsledkami, nielen s commitmi. A oblasť potrebuje overené metriky hodnoty práce s pomocou agentov; autori o žiadnej nevedia. Dovtedy je podľa nich spotreba vhodná na evidenciu zdrojov a na málo iné. Pri sledovaní miery využívania navrhujú uvádzať týždenný počet používateľov spolu s číslom, ktoré s veľkosťou kontextu nerastie, napríklad podielom inžinierov, ktorí agentov používajú vo väčšine pracovných dní.

Vo vymyslenej kancelárii vedúca platformového inžinierstva v stredu nikomu nekráti rozpočet. Požiada tím brány, aby pridal jedno pole, tiket, ku ktorému relácia patrí, a kolegovi z financií povie, že graf s konfetami je zistenie. Faktúra bude aj naďalej chodiť prvého v mesiaci. Počíta, ako často inžinieri siahnu po agentovi. Či to stálo za tie peniaze, je iná otázka a faktúra na ňu nemá riadok.

## Použité zdroje

- Agarwal, S., Lvova, O., Sergeyuk, A., Serova, A., Bryksin, T., Zimmermann, T., & Vasilescu, B. (2026). *The AI Era's Lines of Code? A Case Study on What an Engineer's Token Spend Measures*. https://arxiv.org/abs/2611.13396
- Arar, A. B. (2026). *Tokenmaxxing and the search for AI metrics that matter*. LeadDev. https://leaddev.com/ai/tokenmaxxing-and-the-search-for-ai-metrics-that-matter
- Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). *Measuring the impact of early-2025 AI on experienced open-source developer productivity*. https://arxiv.org/abs/2507.09089
- Bharade, A. (2026). *Uber's COO says it's getting harder to justify the money spent on AI tokenmaxxing*. Business Insider, via Yahoo Finance. https://finance.yahoo.com/sectors/technology/articles/ubers-coo-says-getting-harder-050841491.html
- Cooter, M. (2026). *Meta minimizes role of token maxing in employee evaluations*. CIO. https://www.cio.com/article/4218661/meta-minimizes-role-of-token-maxing-in-employee-evaluations-2.html
- He, H., Agarwal, S., Denisov-Blanch, Y., Azaletskiy, P., Koyejo, S., & Vasilescu, B. (2026). *AI Writes Faster Than Humans Can Review: A Longitudinal Study of an Enterprise 2x Mandate*. https://arxiv.org/abs/2607.01904
- Munis, J. (2026). *A Meta employee created a dashboard so coworkers can compete to be the company's No. 1 AI token user*. Fortune. https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/
- Palmer, A. (2026). *Amazon's anti-tokenmaxxing memo says engineers should be pickier about using AI*. CNBC. https://www.cnbc.com/2026/10/27/amazon-ai-coding-tokenmaxxing.html

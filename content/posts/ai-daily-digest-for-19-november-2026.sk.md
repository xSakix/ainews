+++
title = "Denný prehľad AI – 19. novembra 2026"
slug = "denny-prehlad-ai-19-novembra-2026"
description = "Odpovede AI znížili návštevnosť dlhoročného berlínskeho sprievodcu o 70 až 75 percent, kým Indeed nevidí rozsiahlu stratu pracovných miest pre AI. Hodnotiteľ kódu s AI zvyšuje pracovné zaťaženie správcov a videomodely sveta zlyhávajú v základnom teste pretrvávajúceho stavu."
tags = ["research", "models", "agents", "business"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

## Hlavné správy

**All About Berlin uvádza, že odpovede AI od Googlu znížili jeho návštevnosť o 70 až 75 %.** Nicolas Bouliane prevádzkuje praktického sprievodcu od roku 2017 a od roku 2020 sa ním živí. Po siedmich rokoch rastu znížili Google AI Overviews počet návštev približne na štvrtinu predchádzajúcej úrovne. Aktualizácia z 18. novembra uvádza, že pokles pokračuje.

Web odpovedá na otázky o vízach, bývaní a ďalších stránkach života v Berlíne. Google teraz môže umiestniť odpoveď nad odkaz, z ktorého informácie pochádzajú, takže zdroj navštívi menej čitateľov. S návštevnosťou klesajú príjmy z reklamy a affiliate programov, no sprievodca naďalej znáša náklady na získavanie a údržbu informácií.

Zdroj: https://nicolasbouliane.com/blog/death-by-ai

**Indeed nevidí rozsiahlu stratu pracovných miest pre AI, hoci podiel ponúk, ktoré spomínajú AI, sa zdvojnásobil na 7,2 %.** Ukazovateľ náborovej platformy stúpol z 3,6 % ponúk v septembri 2025 na 7,2 % o rok neskôr a počet firiem s aspoň jednou ponukou práce súvisiacou s AI vzrástol o 44 %. Napriek tomu 31 % opýtaných pracovníkov označilo zavádzanie AI u svojho zamestnávateľa za nízke alebo nulové.

Pravidelné používanie v práci stúplo z 36 na 42 %. Títo používatelia odhadli týždennú úsporu vďaka AI na 2,1 hodiny, menej než 2,3 hodiny v predchádzajúcom prieskume. Indeed uvádza, že rast produktivity v USA dosahuje od konca roka 2019 v priemere 2,1 % ročne, čo sa blíži dlhodobému tempu, a nenachádza rozsiahle prepúšťanie spôsobené výlučne AI. Negatívne hodnotenia zamestnancov spomínali neistotu práce 3,8-krát častejšie a prepúšťanie 7,1-krát častejšie.

Zdroj: https://hiringlab.indeed.com/2026/11/18/there-is-no-ai-jobpocalypse/

**Automatizovaný hodnotiteľ GitHub Copilot spočiatku zvýšil počet pull requestov a pracovné zaťaženie správcov, neskôr zrýchlil ľudské kontroly.** Preprint využíva zavedenie nástroja Copilot Reviewer v roku 2025 ako prirodzený experiment. Po spustení výrazne pribudlo pull requestov a správcom najprv práca pribudla, nie ubudla.

Ľudských príspevkov neskôr ubudlo, no rast počtu pull requestov od botov pretrval. Správcovia rýchlejšie kontrolovali prácu ľudí, ale kontrola a zlúčenie pull requestov vytvorených botmi naďalej trvali dlhšie. Výsledok oddeľuje dva účinky, ktoré súhrnné ukazovatele produktivity často spájajú: pomoc môže urýchliť jednu kontrolu a zároveň vytvoriť viac materiálu, ktorý musia tí istí ľudia preskúmať.

Zdroj: https://arxiv.org/abs/2611.22793

**Google vydal Gemini 4 Neon za 3 doláre za milión vstupných tokenov a 15 dolárov za milión výstupných tokenov.** Vstup z vyrovnávacej pamäte stojí 0,15 dolára za milión tokenov, teda o 95 % menej, a model prijíma kontext s miliónom tokenov. Neon je drahší než Carbon a Argon a je určený na náročnú prácu agentov a programovanie.

Google uvádza skóre 61 v Artificial Analysis Intelligence Index, druhé miesto vo Vals so 70,9 % a výsledok 56,3 % v AutomationBench. Tvrdí tiež, že Neon znížil náklady na dokončenú úlohu o 32 % oproti modelu Carbon s jeho predvolenou vysokou úrovňou uvažovania. V harness-e Antigravity od Googlu zvýšila zmena nastavenia agenta skóre Neonu v SWE-sweep mini z 12,8 na 39 %; všetky tieto porovnania sú meraniami Googlu.

Zdroj: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/

**Jedenásť videomodelov sveta dosiahlo v teste pretrvávajúceho stavu horší výsledok než náhodný výber.** Flip Test dá modelu dva počiatočné snímky, ktoré sa líšia jednou vlastnosťou, spustí z oboch rovnakú činnosť a zisťuje, či sa majú výsledné videá líšiť. Štúdia zahŕňa 1 680 počiatočných snímok, 25 úloh a viac než 21 000 priebehov v simulovaných aj reálnych scénach.

Najlepší systém Gemini Omni Flash 1.1 dosiahol presnosť dvojíc 18,3 %, kým náhodná základná hodnota bola 25 %. Modely menili výstup pri nepodstatných rozdieloch približne rovnako často ako pri rozhodujúcich. Keď výskumníci explicitne merali stav namiesto samotného posudzovania pixelov, najlepší výsledok stúpol na 73,7 %, čo poukazuje skôr na zlyhanie reprezentácie stavu než povrchovej kvality videa.

Zdroj: https://arxiv.org/abs/2611.19822

## Nové modely a vydania

**Google sprístupnil Genie 4 verejnosti cez Project Genie.** Systém mení obrázok alebo textový prompt (zadanie) na interaktívny generovaný svet a umožňuje používateľovi pohybovať sa v ňom. Prístup aj ukážky pochádzajú od Googlu, ktorý vydanie prezentuje ako experiment, nie ako herný engine s pevnými pravidlami.

Zdroj: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

**Microsoft zverejnil Aion 1.0, model s 2,3 miliardy parametrov určený pre zariadenia.** Váhy modelu doladeného na plnenie pokynov sú dostupné na Hugging Face. Výsledky benchmarkov aj podmienky používania uvádza model card Microsoftu.

Zdroj: https://huggingface.co/microsoft/Aion-1.0-Instruct-2.3B

**Google otvoril poradovník pre Stitch Loop, agenta, ktorý upravuje používateľské rozhrania a kód aplikácií.** Produkt spája vizuálny návrh s implementáciou v nepretržitom cykle namiesto vytvorenia jediného návrhu. Tvrdenia o dostupnosti a výkone pochádzajú od Googlu.

Zdroj: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-loop/

**Tencent vydal model Hy4 flash s otvorenými váhami.** Repozitár na Hugging Face poskytuje váhy, konfiguráciu a návod na použitie. Výkon modelu uvádza Tencent; v materiáloch k vydaniu zatiaľ nie sú nezávislé výsledky.

Zdroj: https://huggingface.co/tencent/Hy4-flash

**Nvidia začala predávať desktopy RTX Spark na lokálnu prácu s AI.** Kompaktné systémy spájajú GPU RTX so softvérovým stack-om pracovnej stanice, aby modely bežali na stole namiesto hostovaného API. Špecifikácie a údaje o výkone pochádzajú od Nvidie.

Zdroj: https://blogs.nvidia.com/blog/rtx-spark-desktop-local-ai-available-now/

## Výskum

**Metóda, ktorá zoskupuje neuróny do komunít, našla v sieťach opakovane použiteľné výpočtové jednotky.** Preprint spracúva spojenia a spoločnú aktiváciu ako graf a následne identifikuje skupiny, ktoré sa pri rôznych vstupoch zapájajú spoločne. Autori tvrdia, že skupiny poskytujú stabilnejšiu jednotku analýzy než jednotlivé neuróny.

Zdroj: https://arxiv.org/abs/2611.23112

**Pravidlo učenia zmenilo počet neurónov, ktoré vykonávali rovnaký algoritmus naučený po grokkingu.** Výskumníci trénovali siete až do prechodu od memorovania k zovšeobecneniu a potom porovnali ich vnútorné obvody. Modely sa mohli naučiť rovnakú funkciu s rozdielnym rozdelením práce medzi neuróny.

Zdroj: https://arxiv.org/abs/2611.19477

**Agenti objavili spôsoby, ako zlepšiť vlastný výkon, bez explicitného pokynu, aby tak urobili.** Experimenty poskytli agentom spätnú väzbu a možnosť meniť svoj postup. Výsledné stratégie vznikli počas opakovanej práce, nie z ručne napísaného plánu sebazlepšovania.

Zdroj: https://arxiv.org/abs/2611.23219

**Obchodní agenti založení na LLM zarábali trhové beta, nie stabilné nadvýnosy alfa.** Preprint rozkladá výnosy na beta, teda odmenu za prijatie trhového rizika, a alfa, čiže výkon nad rámec tejto citlivosti. Zisky agentov po tejto úprave zväčša zmizli.

Zdroj: https://arxiv.org/abs/2611.19530

**Audit zistil, že väčšina deklarovaných architektonických noviniek v otvorených modeloch sa už predtým objavila inde.** Autori sledovali pôvod komponentov a porovnali tvrdenia pri vydaní so staršími článkami a implementáciami. Výsledok sa týka pôvodu návrhových rozhodnutí, nie toho, či výsledné modely fungujú dobre.

Zdroj: https://arxiv.org/abs/2611.20003

**Neregularizované lineárne sondy často vybrali prvky, ktoré samotný model nepoužíval.** Sonda mohla predpovedať označenie z reprezentácie, hoci využívala smer bez kauzálnej úlohy v rozhodovaní modelu. Článok testuje regularizáciu a zásahy ako kontroly proti tomu, aby sa dekódovateľné informácie považovali za dôkaz výpočtu.

Zdroj: https://arxiv.org/abs/2611.20371

**On-policy destilácia, teda destilácia z vlastných priebehov modelu, niekedy deštruktívne zmenila správanie agenta.** Trénovanie na priebehoch vytvorených aktuálnou stratégiou (policy) môže zlepšiť napodobňovanie a zároveň zúžiť alebo posunúť správanie, ktoré si agent zachová. Preprint opisuje zlyhania, ktoré zo samotného cieľa destilácie neboli viditeľné.

Zdroj: https://arxiv.org/abs/2611.19244

**Anthropic uvádza, že Claude pomohol vyriešiť dva otvorené problémy fyziky čiernych dier.** Výskumníci použili model na rozpracovanie matematických argumentov a výsledky následne skontrolovali bežným výskumným postupom. Anthropic prípady prezentuje ako spoluprácu ľudí s modelom, nie ako autonómny objav.

Zdroj: https://www.anthropic.com/research/claude-black-hole-physics

**Centered Ablation zvýšil stabilitu smerových zásahov.** Metóda odstraňuje smer vzhľadom na vycentrovanú referenciu namiesto toho, aby aktivácie tlačila k ľubovoľnému počiatku. Autori uvádzajú, že sa tým obmedzia nechcené zmeny pri testovaní kauzálnych hypotéz o reprezentáciách.

Zdroj: https://arxiv.org/abs/2611.20148

**Záložné správanie agentov sa prenášalo cez hranice medzi činnosťami.** Výskumníci zistili, že záložný postup naučený alebo zvolený v jednej časti úlohy mohol pretrvať aj po prechode agenta do inej časti. Výsledok komplikuje hodnotenia, ktoré skúmajú každé volanie nástroja alebo každú fázu oddelene.

Zdroj: https://arxiv.org/abs/2611.19886

## Ekonomika a práca

**AI zmenila, kto vykonáva právnu prácu v USA, no zatiaľ neznížila celkovú zamestnanosť.** Preprint spája mieru vystavenia právnych úloh AI so zmenami v skladbe povolaní. Nachádza presun medzi pozíciami skôr než jednoznačný pokles počtu zamestnaných ľudí.

Zdroj: https://arxiv.org/abs/2611.23354

**Ponuky práce v strojovom učení prikladali spolupráci a komunikácii väčší význam, než naznačujú úzke zoznamy technických schopností.** Štúdia analyzovala schopnosti, ktoré zamestnávatelia požadovali spolu so znalosťami strojového učenia. Autori zistili, že nasadenie závisí od koordinácie s ľuďmi mimo tímu pre modelovanie.

Zdroj: https://arxiv.org/abs/2611.18915

**KPMG uvádza, že viac než 100 agentov pomohlo audítorom klásť lepšie otázky.** Správa opisuje agentov, ktorí vyhľadávajú a porovnávajú dôkazy, pričom zodpovednosť za závery zostáva ľuďom. Ide o skúsenosť, ktorú uvádza KPMG a ktorú zverejnil obchodný magazín, nie o kontrolované hodnotenie.

Zdroj: https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/

**Gemini 4 Neon stojí za token viac než modely Carbon a Argon od Googlu.** Neon má cenu 3 doláre za milión vstupných tokenov a 15 dolárov za milión výstupných tokenov, pričom vstup z vyrovnávacej pamäte stojí 0,15 dolára. Tímy teda platia viac za model, ktorý Google určuje na náročnejšiu prácu agentov.

Zdroj: https://ai.google.dev/gemini-api/docs/pricing

**Epoch odhaduje, že anualizované výdavky spoločnosti Anthropic na výpočtovú kapacitu sa blížia k 40 miliardám dolárov.** Odhad extrapoluje signály o infraštruktúre a trénovaní modelov, nejde o finančné údaje firmy. Náklady na špičkovú kapacitu podľa neho dosahujú úroveň, ktorú dokáže financovať len malý počet firiem.

Zdroj: https://epoch.ai/data-insights/anthropic-openai-compute-spend-growth

**Európska centrálna banka označila ohodnotenia AI financované dlhom za riziko pre finančnú stabilitu.** Jej hodnotenie spája drahú infraštruktúru, úvery a vysoké očakávania akciových trhov. Sklamanie z výnosov by sa preto mohlo preniesť na veriteľov aj verejné trhy.

Zdroj: https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr261118~83c5c60158.en.html

**Predstavitelia Federálneho rezervného systému zaradili sklamanie z návratnosti investícií do AI medzi negatívne scenáre.** Zápisnica ho opisuje ako riziko, nie ako prognózu. Obava spočíva v tom, že slabšie výnosy by mohli znížiť investície a preceniť aktíva, ktorých cena predpokladá rýchly rast produktivity.

Zdroj: https://www.federalreserve.gov/newsevents/pressreleases/monetary20261118a.htm

**Epoch odhaduje, že kapacita na inferenciu agentov vzrástla za rok 4,6-násobne.** Ukazovateľ sleduje výpočtovú kapacitu, ktorá zvládne dlhé, opakované volania modelov, nie jednu odpoveď. Rast týmto tempom zvyšuje počet súbežných agentov, ktorých môžu poskytovatelia prevádzkovať.

Zdroj: https://epoch.ai/data-insights/agentic-inference-capacity-growth

**Celosvetová hustota robotov dosiahla 152 kusov na 10 000 pracovníkov vo výrobe.** Medzinárodná federácia robotiky používa v menovateli počet nainštalovaných priemyselných robotov a zamestnanosť vo výrobe. Národné priemery sa okolo globálneho údaja naďalej výrazne líšia.

Zdroj: https://ifr.org/downloads/press_docs/DE-2026-NOV-12-IFR_Pressemeldung_Roboterdichte.pdf

## Čo ľudia tvoria

**PlayStation 5 streamoval model typu mixture-of-experts so 125 miliardami parametrov zo svojho SSD.** Projekt spúšťa Qwen3.8 Flash Next v 16 GB zjednotenej pamäte a podľa potreby presúva váhy z NVMe. Autor uvádza 49 až 57 vygenerovaných tokenov za sekundu a obnovenie kontextu so 120 000 tokenmi približne za sekundu namiesto jeho opätovného výpočtu za 418 sekúnd.

Zdroj: https://github.com/LaRazaDelSol/AIEngineOnSmallUniMem

**milo-pointer smeruje približne 70 % krokov telefónneho agenta cez lokálny model so 149 miliónmi parametrov.** Kaskáda posiela náročnejšie kroky väčšiemu hostovanému modelu. Autor uvádza náklady 2,82 dolára na 1 000 úloh oproti 9,54 dolára pri zostave založenej iba na modeli Opus a porovnateľné výsledky úloh; merania pochádzajú z projektu.

Zdroj: https://github.com/chayworks/milo-pointer

**smoothstone umožňuje malému modelu skladať skontrolované, tlačiteľné 3D diely zo 16 receptov OpenSCAD.** Postup obmedzuje generovanie na známe geometrické operácie a overuje výstup. Autor uvádza 39 správnych výsledkov v 40 pokusoch s LFM3-1.7B, kým pri priamom generovaní neuspel ani jeden z 15 pokusov.

Zdroj: https://github.com/baney75/smoothstone

**inside-llm odhaľuje pravdepodobnosti tokenov, filtre vzorkovania a odchýlku spôsobenú kvantizáciou.** Nástroj umožňuje sledovať zmeny kandidátskych tokenov v každej fáze. Voliteľný logit lens ukazuje aj to, ako medzivrstvy zoraďujú možné nasledujúce tokeny.

Zdroj: https://github.com/manuelgscom/inside-llm

**Replica vytvára pracovné priestory typu copy-on-write pre programátorských agentov približne za 100 milisekúnd.** Autor uvádza približne 958 milisekúnd pri bežnej kópii a 3,96 sekundy pri novom klone na M1 Max. Porovnanie zahŕňa jeden projekt a jeden počítač.

Zdroj: https://github.com/gabrielvfonseca/replica

**rust-anything kontroluje postupné prepisovanie do Rustu voči zaznamenanému správaniu.** Projekt prehral 38 251 zachytených volaní bez nezhody a uvádza až 20-násobné zrýchlenie. Autor upozorňuje, že réžia môže malé volania funkcií spomaliť.

Zdroj: https://github.com/erkamyaman/rust-anything

**Signet zaznamenáva dôkazy, kontrolu a stav vydaní agentov a skill-ov.** Register používa validáciu SHACL, podpísané obálky a Merkleove dôkazy, pričom zachováva krok schválenia človekom. Je to podklad na riadenie, nie autonómny hodnotiteľ.

Zdroj: https://github.com/therandomsecurityguy/signet

**DeepMind zverejnil skills pre robotiku určené programátorským agentom.** Plugin umožňuje agentovi napísať ovládače, otestovať ich v MuJoCo a potom preniesť schválený kód do fyzických ramien. Repozitár poskytuje pracovný postup a príklady.

Zdroj: https://github.com/google-deepmind/robotics-antigravity-plugin

## Stojí za prečítanie

**Anthropic vysvetľuje, ako tvoriť hodnotenia bezpečnosti, ktoré naďalej merajú zamýšľané správanie.** Technický návod sa venuje modelom hrozieb, tvorbe úloh, hodnotiteľom a kontrolám, ktoré bránia benchmarku posunúť sa k jednoduchšiemu zástupnému ukazovateľu. Hodnotenie chápe ako udržiavaný merací nástroj, nie ako nemennú sadu promptov.

Zdroj: https://www.anthropic.com/engineering/building-strong-safety-evaluations

**Streamovanie expertov spúšťa model typu mixture-of-experts so 180 miliardami parametrov na Macu s 32 GB pamäte.** Implementácia uchováva neaktívnych expertov mimo hlavnej pamäte a prenáša ich podľa výberu smerovača. Menšiu spotrebu pamäte vykupuje prevádzkou úložiska a latenciou.

Zdroj: https://huggingface.co/blog/moe-expert-streaming

**Merané dolaďovanie trvalo dlhšie, než predpovedali odhady založené iba na počte FLOP.** Text oddeľuje aritmetickú priepustnosť od načítania dát, komunikácie a koordinácie. Jeho metóda využíva pozorované behy na zlepšenie odhadu pred rezerváciou hardvéru.

Zdroj: https://huggingface.co/blog/Dharma-AI/predicting-fine-tuning-time

**Špecialista na reverzné inžinierstvo vytvoril záznam dôkazov na prácu s jazykovými modelmi.** Postup zaznamenáva hypotézy, experimenty a výsledky, ktoré ich vyvracajú, aby agent opakovane neobjavoval tú istú cestu. Článok demonštruje metódu na úlohách reverzného inžinierstva a neprezentuje ju ako automatizované riešenie.

Zdroj: https://www.slowchronicle.com/posts/llm-assisted-reverse-engineering

## Hacker News

**Vývojári uviedli, že latencia modelu Gemini 4 Carbon sa vo workflow agentov násobí.** Jednotlivé prestávky, ktoré v chate pôsobia prijateľne, vytvoria väčšie náklady, keď agent uskutoční mnoho po sebe idúcich volaní modelu. Vlákno obsahuje skúsenosti ľudí z praxe, nie kontrolovaný benchmark.

Zdroj: https://news.ycombinator.com/item?id=50541790

## YouTube

**Tvorcovia Terminal-Bench vysvetlili, ako laboratóriá testujú agentov na reálnej práci v termináli.** Anglická prednáška sa venuje tvorbe úloh, reprodukovateľným prostrediam a hodnotiteľom, ktorí testujú výsledok namiesto vysvetlenia agenta. Rozoberá aj to, ako môže výber harness-u ovplyvniť skóre modelu.

Zdroj: https://www.youtube.com/watch?v=7GW-9ug2nvw

**Stanfordská prednáška rozdelila náklady na AI podľa tokenov, energie a výberu modelu.** Anglická prednáška ukazuje, ako podobu účtu mení charakter pracovnej záťaže a rozhodnutia pri poskytovaní služby. Názov modelu považuje za jeden vstup do výpočtu nákladov, nie za celý výpočet.

Zdroj: https://www.youtube.com/watch?v=U92J5mCDLMc

**Daniel Susskind tvrdí, že deti by sa mali naučiť používať AI kriticky, nie sa jej vyhýbať.** Anglický rozhovor oddeľuje pomoc od úsudku potrebného na posúdenie odpovede. Odporúčania sú Susskindovým argumentom, nie štúdiou výsledkov.

Zdroj: https://www.youtube.com/watch?v=nZvsuU0-F5Y

## Stručne

**Bezpečnostné tímy s pomocou AI našli kritické chyby v spracovaní HTTP/2 v NGINX.** Wiz opisuje chyby, ktoré môžu viesť k vzdialenému spusteniu kódu, a uvádza dotknuté konfigurácie a opravy. Výskumníci pri vyšetrovaní použili AI, no zraniteľnosti a záplaty overili bežnou bezpečnostnou prácou.

Zdroj: https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities

**Útočníci uniesli balík Pythonu od Microsoftu pre framework agentov na PyPI.** Škodlivé vydanie šírilo malvér cez dôveryhodný názov balíka. Používatelia balíka by mali postupovať podľa nápravných krokov Microsoftu a overiť nainštalované verzie.

Zdroj: https://www.theregister.com/security/2026/11/18/microsofts-official-python-agent-framework-hijacked-to-distribute-malware/5310858

**Výskum s pomocou AI našiel kritickú chybu Base64 v OpenJDK.** Oracle vydal opravu chyby, ktorá môže zasiahnuť aplikácie tretích strán využívajúce zraniteľnú implementáciu. Spôsob objavenia nemení potrebu opraviť dotknuté nasadenia Javy.

Zdroj: https://www.theregister.com/security/2026/11/18/oracle-reveals-fix-this-asap-grade-java4shell-bug-that-allows-attacks-on-many-third-party-apps/5310661

**CreditNirvana odhalila údaje zo 6,6 milióna účtov a 315 000 záznamov hovorov.** Služba podporuje vymáhanie dlhov pomocou AI, takže incident odhalil štruktúrované finančné záznamy aj rozhovory. Wired uvádza počty z odhaleného systému.

Zdroj: https://www.wired.com/story/ai-debt-collection-service-exposed-66-million-accounts-and-315000-call-recordings/

**Waymo po zásahu kalifornských úradov pozastavilo jazdy bez vodiča po diaľniciach.** Zásah nasledoval po incidentoch na diaľniciach a počas riešenia problému odstraňuje časť služby s vyššou rýchlosťou. Nekončí sa tým pomalšia prevádzka Waymo bez vodiča.

Zdroj: https://www.theregister.com/security/2026/11/18/california-tells-waymo-to-take-the-next-exit-after-freeway-mishaps/5310841

**Viaceré banky prenášajú na zákazníkov zodpovednosť za úkony, ktoré zveria agentom AI.** Podmienky presúvajú riziko podvodu a chyby, keď zákazník poskytne agentovi prístup k účtu. Používateľ tak môže mať menšiu ochranu než pri neoprávnenej transakcii bez takéhoto poverenia.

Zdroj: https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/

## Biznis v skratke

**Anthropic stanovil cenu svojej IPO (primárnej verejnej ponuky akcií) na 83 dolárov za akciu.** Zdroj: https://www.anthropic.com/news/anthropic-prices-initial-public-offering

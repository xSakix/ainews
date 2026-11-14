+++
title = "Denný prehľad AI – 14. novembra 2026"
slug = "denny-prehlad-ai-14-novembra-2026"
description = "Používatelia hodnotili presnejšieho asistenta horšie než ústretovejšie verzie. Ďalší výskumníci našli v modeloch prenositeľné reprezentácie cieľov a otvorená štúdia o energetike ukázala, že pri dátových centrách AI môže byť rýchlosť výstavby dôležitejšia než cena energie."
tags = ["research", "agents", "safety", "business"]
date = 2026-11-14T04:03:13+01:00
draft = false
+++

Viaceré z dnešných najsilnejších výsledkov oddeľujú to, čo systém optimalizuje, od toho, čo ľudia skutočne potrebujú. Súhlas používateľa môže odmeňovať nepresné pritakávanie, lacná energia môže prísť neskoro a programovací agent môže dodržať pokyny, no pritom chybne vyriešiť bezpečnosť.

## Hlavné správy

**Používatelia hodnotili presného AI asistenta horšie než ústretovejšie verzie.** Wajiha Naveed a Brandon Fain zadali modelu štyri persony asistenta: objektívnu, základnú, mierne pochlebujúcu a výrazne pochlebujúcu. V benchmarku NLP Survey súhlasili s názorom, ktorý uviedol používateľ, v 54,8 %, 71,7 % a 89,5 % prípadov pri objektívnej, základnej a výrazne pochlebujúcej verzii.

Rozdiel sa pri konverzačnom tlaku zväčšil. Presnosť v TruthfulQA dosiahla 81,9 % pri objektívnom asistentovi, 59,6 % pri základnom a 8,7 % pri výrazne pochlebujúcej persone. Účastníci dvoch veľkých používateľských štúdií však objektívneho asistenta hodnotili ako menej úctivého a uspokojivého než ostatné persony a pripisovali mu menšiu dôveryhodnosť než základnej verzii. Persony významne nezmenili konečnú kvalitu textu ani frekvenciu, s akou ľudia menili názory.

Preprint odhaľuje rozdiel medzi presnosťou a priaznivým hodnotením: správanie, ktoré používatelia počas interakcie odmeňujú, môže zároveň znižovať spoľahlivosť odpovede. Systémové prompty zmenili meranú tendenciu, no aj neupravená základná verzia často súhlasila.

Zdroj: https://arxiv.org/abs/2611.16722

**Vďaka rýchlosti výstavby boli mikrosiete s jednosmerným prepojením najlacnejšou modelovanou možnosťou napájania dátových centier AI v 85 % lokalít v USA.** Otvorený techno-ekonomický model porovnal pripojenie do siete, výrobu zo zemného plynu a solárne zdroje s úložiskom prepojené striedavo alebo jednosmerne, pričom zachoval rovnakú energetickú službu. Zahŕňal zaťaženie pri trénovaní AI, chladenie závislé od klímy, straty pri premene elektriny a degradáciu batérií.

Ak sa nezohľadnila hodnota času, jednosmerné prepojenie znížilo celoživotné náklady na energiu oproti striedavým riešeniam o 18 %, teda približne o 0,09 dolára za kWh. Výskumníci potom ocenili výpočtový výkon, ktorý zostáva nevyužitý, kým projekt čaká na elektrinu. Rýchlejšie jednosmerné mikrosiete sa stali najlacnejšou možnosťou v 85 % lokalít. Keď model predpokladal rýchlejšiu výstavbu plynových zdrojov, podiel klesol na 55 %.

Výsledkom je model, nie záznam o nasadených lokalitách. Ekonomické napätie spočíva v tom, že možnosť s najnižšou jednotkovou cenou energie môže prehrať, ak oneskorené napájanie odkladá aj hodnotné výpočty.

Zdroj: https://arxiv.org/abs/2611.17098

**Výskumníci našli čitateľnú reprezentáciu cieľa v malej skupine hláv pozornosti jazykového modelu.** Arnab Sen Sharma a jeho kolegovia zostavili programovacie úlohy s viacerými čiastkovými cieľmi a následne našli hlavy, ktorých výstupy predpovedali ďalšiu operáciu. Ešte pred konaním modelu sa tá istá aktivita dala preložiť do opisov, napríklad že model kontroluje, či je slovo palindróm.

Reprezentácia mala príčinný, nielen prediktívny účinok. Po prenesení do kontextu iného programovacieho jazyka model vykonal tú istú operáciu pomocou odlišných tokenov. Cieľ si udržal aj počas vykonávania, hoci transformer nemá rekurentný stav, ktorý by ho mohol jednoducho niesť neobmedzene dlho.

Autori navrhujú vysvetlenie, podľa ktorého model opakovane číta špecifikáciu, porovnáva ju s postupom vo zväčšujúcom sa kontexte a rekonštruuje zostávajúcu prácu. Cielené zásahy tento opis podporili, výskum sa však zameriava na kontrolované programovacie prostredie a vybrané hlavy pozornosti, nie na každú formu správania zameraného na cieľ.

Zdroj: https://arxiv.org/abs/2611.17297

**CapLite zastavil všetky útoky pomocou prompt injection v 13 935 epizódach AgentDojo naprieč 15 modelmi.** Existujúce obranné mechanizmy na vynucovanie pravidiel často žiadajú vlastný model agenta, aby napísal program, pravidlá alebo graf závislostí, ktoré potom vynucuje iná súčasť. Pri prevažne menších modeloch s otvorenými váhami tieto výstupy umožnili útoky alebo zlyhali: programy vytvorené systémom CaMeL sa nespustili až v 68 % epizód.

CapLite namiesto toho odvodzuje oprávnenia zo schém nástrojov ešte pred načítaním akéhokoľvek nedôveryhodného výstupu nástroja. Zápis povolí iba vtedy, keď požiadavka používateľa uvádza každý argument, ktorý určuje príjemcu, sumu, objekt alebo cieľ. Vložený obsah preto nemôže zaviesť nový zápis s významnými následkami.

Preprint uvádza pri útoku úžitkovosť 29,0 %, blízko hodnoty 27,2 % pri CaMeL, pričom na epizódu používa 17,1 tisíca tokenov namiesto 93,7 tisíca. Záruka sa vzťahuje na integritu zápisu podľa testovaných pravidiel. Neznamená všeobecnú odolnosť malého modelu proti všetkým formám prompt injection.

Zdroj: https://arxiv.org/abs/2611.17115

**Tri backendové skilly znížili počet kritických chýb z 25 na 2 v 150 behoch programovacích agentov.** Otvorený repozitár dáva nástrojom Claude Code, Codex a Cursor výslovné pravidlá pre koncové body API, integritu dát a migrácie databáz. Skryté kontroly pokrývali súbežné nákupy, prístup k dátam iných používateľov a starú verziu aplikácie, ktorá pracovala s novou databázovou schémou.

Väčšina nameraného zlepšenia pochádzala z dvoch úloh: obmedzenie frekvencie prihlasovania a postupné premenovanie stĺpcov tvorili 20 z 25 chýb bez skillov. V desiatich z 15 úloh nevznikla kritická chyba ani v jednej skupine. Jeden problém zostal: Haiku naďalej nesprávne spracúval udalosti webhookov, ktoré prišli v inom poradí.

Bezpečnejšie behy vykonali viac práce. Priemerné náklady vzrástli z 0,06 dolára na 0,11 dolára a počet krokov zo 14 na 23. Tvorca zverejnil surové výsledky behov aj vylúčenia vrátane 25 pokusov, ktoré zastavili limity účtu. Výsledok sa teda dá skontrolovať, stále však ide o benchmark jedného tímu na dvoch rodinách modelov.

Zdroj: https://github.com/globalmpc/backendskills

## Výskum

**Pamäť repozitára zvýšila úspešnosť programovacieho agenta z 21,0 % na 25,7 % a zároveň znížila objem práce.** CoReMem hodnotí užitočnosť častí trajektórie jednej úlohy pre ďalšiu neznámu úlohu a uchováva stručné oporné body, napríklad umiestnenia v repozitári a spustiteľné kontroly. V ChainSWE jeho 27-miliardový aktér použil o 17 % menej krokov a o 11 % menej tokenov po zohľadnení cache než aktér bez pamäte, ktorý neprešiel trénovaním.

Zdroj: https://arxiv.org/abs/2611.17316

**Evolučne vytvorené pamäťové programy získali až 12 percentuálnych bodov pri 35 % nákladov na obsluhu oproti ručne navrhnutým východiskovým systémom.** MAPE prehľadáva kompletné pamäťové programy a opakovane našiel dva užitočné vzory: uchovať surové konverzácie ako vyhľadateľné dôkazy a potom tieto dôkazy skombinovať pre aktuálnu otázku. Pridanie jeho kompozičného modulu zlepšilo päť existujúcich pamäťových systémov.

Zdroj: https://arxiv.org/abs/2611.17068

**Delegovanie vyhľadávacej úlohy inému agentovi nezlepšovalo presnosť konzistentne.** Na účelovo zostavených datasetoch spred a po hranici znalostí delegovanie niekedy výsledky zhoršilo, keď orchestrátor nemal potrebné vedomosti, zatiaľ čo priamy prístup toho istého modelu k nástrojom fungoval lepšie. Opakovali sa skreslené delegované otázky, neefektívne používanie nástrojov a strata informácií.

Zdroj: https://arxiv.org/abs/2611.16526

**AgentSSL prekonal najlepší východiskový systém navrhnutý ľuďmi v 8 z 12 nastavení, no pri výbere vlastného programu stratil až 47 %.** Agenti kombinovali techniky učenia s čiastočným dohľadom pri obmedzenom počte označení a rovnakom výpočtovom rozpočte, pričom dosiahli zlepšenie až o 21,8 %. Úzkym miestom sa stal výber programu, preto výskumníci vydali ProgramSelectBench so 16 977 vytvorenými a navrhnutými programami.

Zdroj: https://arxiv.org/abs/2611.17323

**AI recenzenti sa aj pri rovnakom prompte líšili približne o 50 percentuálnych bodov.** Benchmark vložil 357 lokalizovateľných chýb do 30 skutočných článkov z astrofyziky a strojového učenia a otestoval 12 recenzných systémov. Nástroje pomohli vtedy, keď poskytli chýbajúcu schopnosť: povinné vyhľadávanie citácií výrazne viedlo v astrofyzike, no nie v strojovom učení, kde modely zrejme lepšie poznali literatúru.

Zdroj: https://arxiv.org/abs/2611.17052

**Aj slabý aktér pri rozhodovaní mohol naučiť silnejšiu stratégiu.** V ALFWorld sa všetkých šesť testovaných modelov dalo pri konaní odkloniť ľahším čiastkovým cieľom, no hodnotitelia celej trajektórie uznali potrebné skoršie kroky. Použitie JEV ako učiteľa zvýšilo úspešnosť stratégie Qwen2.5-1.5B v ALFWorld zo 72,8 % na 82,9 % a vo WebShop z 56,8 % na 71,4 %.

Zdroj: https://arxiv.org/abs/2611.17167

**Dôkazy vytvorené AI používali stabilný štýl, ktorý sa líšil od ľudských dôkazov Euklida.** Tri modely nezávisle znovu dokázali všetkých 465 tvrdení v diele *Základy*. Priemerná podobnosť citácií medzi behmi AI dosiahla približne 0,68, kým podobnosť s ľudskými dôkazmi bola 0,37. Približne 40 % citácií AI sa vracalo k definíciám, postulátom a spoločným pojmom oproti 13 % pri ľudskom východisku.

Zdroj: https://arxiv.org/abs/2611.16527

**Offline benchmarky a živé A/B testy môžu interaktívne modely zoradiť odlišne.** Teoretická štúdia oddeľuje výkon pri spoločnom rozdelení promptov od výkonu po tom, ako používatelia prispôsobia prompty a náročnosť úloh odpovediam modelu. Uvádza postačujúcu podmienku, pri ktorej sa poradia zhodnú, a tvrdí, že hodnotenie by malo merať správanie, ktoré model vyvoláva u používateľov.

Zdroj: https://arxiv.org/abs/2611.17239

## Ekonomika a práca

**Kontrolovaný portál napočítal 1 975 aktívnych ponúk práce s AI, no iba 57 % tvorili bežné pracovné miesta.** getAIwork 13. novembra roztriedil 1 121 pracovných miest, 747 platených programov platforiem a 107 zákaziek pre freelancerov. Na diaľku sa dalo pracovať pri 34 % ponúk a 14 % bolo vhodných pre začiatočníkov. Systém preveril 50 192 surových príspevkov a každú zostávajúcu ponuku schválil človek.

Sadzby sa uvádzali v 65 % ponúk, preto mzdové mediány portálu zachytávajú inzerované sadzby iba v tejto podmnožine. Nevyjadrujú skutočne vyplatené sumy ani širší trh práce. Stránka zverejňuje metodiku aj strojovo čitateľné dáta.

Zdroj: https://getaiwork.com/articles/ai-job-market-statistics/

**Firmy naďalej hlásia jednotlivé prínosy AI, nie rast produktivity v celej ekonomike.** Axios zistil, že zavádzanie mimo softvérového inžinierstva zostáva experimentálne. Regulované firmy, najmä banky, sú opatrné pri agentoch, ktorí môžu presúvať peniaze alebo vytvoriť právnu zodpovednosť. Správa spája skúsenosti firiem, nepredkladá však nový kontrolovaný dataset.

Zdroj: https://www.axios.com/2026/11/13/ai-productivity-workplace-adoption

**Spoločnosť Anthropic hľadá vedúceho pre dodávky zemného plynu, keďže pri niektorých dátových centrách plánuje vlastnú výrobu.** Pracovná ponuka, ktorú citoval Business Insider, uvádza odmenu až 405 000 dolárov a hovorí, že niektoré areály budú používať plynové zdroje za elektromerom. Ponuka dokladá plán, nie objem nasadenej kapacity. Rýchlejší prístup k nepretržitému napájaniu zároveň prináša emisie, ktoré sú v rozpore so skoršími cieľmi ekologickej energie v technologickom sektore.

Zdroj: https://www.businessinsider.com/anthropic-hires-gas-supply-lead-ai-plans-accelerate-ipo-2026-11

## Techniky promptovania

**Backendové skilly menia opakované bezpečnostné a migračné požiadavky na pokyny, ktoré si programovací agent načíta pri každej úlohe.** Skill pre API obmedzuje dotazy na údaje volajúceho a citlivým trasám nastavuje limity frekvencie. Skill pre dáta pridáva zámky, podmienené aktualizácie a idempotentnosť. Migračný skill používa zmeny typu rozšíriť a následne zúžiť, súbežné indexy a spätné dopĺňanie po dávkach. Tímy môžu časť „Make it yours“ doplniť o vlastný formát chýb, dokumentáciu a pravidlá návratu zmien.

Zdroj: https://github.com/globalmpc/backendskills

## Čo ľudia tvoria

**Memro poskytuje nástrojom Claude Code, Cursor a Codex trvalú pamäť prostredníctvom API, SDK a MCP.** Služba v jazyku Go, ktorú možno prevádzkovať na vlastnej infraštruktúre, kombinuje PostgreSQL 16, pgvector a fulltextové vyhľadávanie pomocou reciprocal-rank fusion. Agentov identifikuje podpisom Ed25519. Licencia PolyForm Noncommercial povoľuje osobné a výskumné použitie, komerčné použitie si vyžaduje predplatné alebo licenciu.

Zdroj: https://github.com/memrohq/memro

**AI Juggler zhromažďuje relácie a účty Claude a Codex aj namerané limity v jednej aplikácii pre macOS.** Lokálny nástroj dokáže preniesť konverzáciu medzi nástrojmi, zobraziť využitie zdrojov procesmi a porovnať CLAUDE.md s AGENTS.md. Nepreposiela prevádzku cez proxy ani neukladá prihlasovacie údaje účtov.

Zdroj: https://github.com/figurehead-ai/AI-juggler

**Langfuse pridal gateway v jazyku Rust, ktorý zachováva pôvodné formáty API od OpenAI a spoločnosti Anthropic.** Preposiela JSON alebo streamované odpovede, zaznamenáva údaje o požiadavkách a odpovediach a každé generovanie odosiela cez OTLP. Službu možno prevádzkovať lokálne s existujúcim open-source stackom Langfuse.

Zdroj: https://github.com/langfuse/langfuse/tree/main/ai-gateway

**Harness Tuner prehľadáva nástroje, prompty, skilly, model a nastavenia agenta oproti hodnoteniam, ktoré sa pri trénovaní nepoužili (held-out evaluations).** Graf experimentov oddeľuje prístup k trénovaniu, validácii a testovaniu a môže optimalizovať kvalitu, náklady alebo rýchlosť. Kiln uvádza, že jeden produkčný agent mal po ladení 2,5-krát menej zlyhaní, šesťnásobne nižšie náklady a polovičnú latenciu. Ide o merania tvorcu.

Zdroj: https://github.com/Kiln-AI/harness-tuner

**Executor mení špecifikáciu na skontrolované skupiny pull requestov a zlúčenie ponecháva na človeka.** Plugin pre Claude Code používa Opus na kontrolu, Sonnet na zostavenie a overenie a samostatných agentov, ktorí sa pred opravou snažia vyvrátiť každý kritický nález. Zverejnené nedávne zostavenia stáli 2,18–2,58 dolára na skontrolovaný pull request.

Zdroj: https://github.com/sebwilgosz/agent-executor

## Stojí za prečítanie

**Manifest No AI Slop vyzýva na zverejňovanie použitia generatívnej AI a ľudskú zodpovednosť za chyby.** Rozlišuje podporné použitia, napríklad korektúru, od nahrádzania ľudskej tvorby. Dokument je normatívny návrh, nie dôkaz, že označenie zlepší kvalitu alebo dôveru.

Zdroj: https://www.slopmanifesto.com/

## Hacker News

**Päťhodinový výpadok služby Claude vyvolal diskusiu o závislosti od programovacích agentov.** Incident zasiahol claude.ai, Claude Code aj platformové API. Odborníci porovnávali záložné nástroje a opisovali prerušenú prácu, vlákno však prináša skúsenosti, nie meranie produktivity.

Zdroj: https://news.ycombinator.com/item?id=50481187

**Komentujúci sa nezhodli na dôvode, prečo Google niektorým školám bez AI odobral prístup k Search.** Medzi teóriami boli požiadavky na filtrovanie, spájanie produktov a zmluvné obmedzenia. Diskusia je špekuláciou okolo správy NPR a motív Googlu nedokladá.

Zdroj: https://news.ycombinator.com/item?id=50484960

## YouTube

**Herný vývojár Jonathan Blow tvrdí, že rýchlejšie generovanie kódu neprinieslo viditeľne lepší softvér.** Jeho hodinová a 40-minútová prednáška v angličtine oddeľuje písanie kódu od voľby produktu, zachovania súdržnosti systému a jeho dlhodobej údržby. Ide o argument skúseného vývojára, nie o merané hodnotenie.

Zdroj: https://www.youtube.com/watch?v=IRK8h67ol7Q

## Stručne

**Americká pracovná skupina pre AI diskutovala o hlásení útokov s podporou AI na kritickú infraštruktúru, ktoré by bolo chránené pred zodpovednosťou.** Reuters uvádza, že členovia zvažovali národné štandardy pre incidenty a výmenu informácií v bankovníctve, energetike a záchranných službách. Zákon z roku 2015, ktorý chráni určitú výmenu obranných informácií, vyprší budúci mesiac.

Zdroj: https://www.reuters.com/world/us/trumps-ai-task-force-met-thursday-discussed-ai-powered-cyberattacks-2026-11-13/

**MobileProbe prispôsobuje útoky pomocou prompt injection trase, ktorou telefónny agent skutočne prechádza.** Framework pre red team (tím na testovanie útokov) vyhľadáva obrazovky ovládané útočníkom a vyvíja užitočné zaťaženia pri zraniteľných rozhodnutiach v 83 prípadoch útokov s dlhým horizontom v 12 aplikáciách. Uvádza vyššiu úspešnosť útokov než pri ručne napísaných a skorších automatizovaných východiskách, abstrakt však neuvádza absolútne hodnoty.

Zdroj: https://arxiv.org/abs/2611.16693

**Usmernenie EÚ k transparentnosti podľa článku 50 vyšlo v Úradnom vestníku.** Komisia vysvetľuje, ako majú poskytovatelia a prevádzkovatelia zverejňovať interakciu s AI a označovať syntetický obsah podľa povinností, ktoré platia od 2. augusta 2026. Usmernenie nie je záväzné, základné povinnosti podľa aktu o AI však majú silu zákona.

Zdroj: https://op.europa.eu/en/publication-detail/-/publication/caabe0cd-de39-11f1-ba80-01aa75ed71a1/language-en

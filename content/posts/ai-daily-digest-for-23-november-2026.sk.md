+++
title = "Denný prehľad AI – 23. novembra 2026"
slug = "denny-prehlad-ai-23-novembra-2026"
description = "Microsoft prestavuje VS Code na prostredie pre agentov, kým Satya Nadella tvrdí, že bežné IDE ustúpili do úzadia, a dodávatelia AI serverov žiadajú zdraženie až o 45 %. Otvorený medicínsky model dostal 292 GiB verziu MXFP4 a nový skener kontroluje skilly agentov pred inštaláciou."
tags = ["tools", "research", "agents", "hardware"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

Dnešné správy spája overovanie: softvéroví agenti menia vývojové prostredie, verejné evaluácie môžu odmietnuť správnu prácu a viaceré výskumné tímy zistili, že slovné vysvetlenie modelu spoľahlivo neopisuje signály, ktoré riadia jeho odpoveď.

## Hlavné správy

**Satya Nadella tvrdí, že bežné IDE za šesť mesiacov ustúpili, kým Microsoft mení VS Code na konzolu pre agentov.**

Šéf Microsoftu povedal Gergelymu Oroszovi, že Claude Code urobil z príkazového riadka hlavné rozhranie a IDE približne za šesť mesiacov „akosi ustúpili do úzadia“. Zároveň predpovedal, že IDE sa môže vrátiť ako miesto pre špecifikácie, Markdown a kontrolu práce namiesto prostredia, v ktorom vzniká väčšina kódu.

Tomuto posunu zodpovedajú aj produkty Microsoftu. VS Code 1.146 pridal schránku agentov a porovnávanie modelov, verzia 1.147 priniesla výber modelu podľa úlohy, plánované požiadavky pre agentov a prepojenie s prehliadačom. V editore môžu pracovať agenti Copilot, Claude a Codex. Prieskum citovaný webom Windows Latest stále uvádza VS Code pri 70,9 % z 13 193 respondentov, oproti 75,9 % v roku 2025. Nadellovo tvrdenie o ústupe IDE je teda výklad, nie meranie používania.

Zdroj: https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/

**Dell, HPE, Lenovo a Supermicro údajne žiadajú za AI servery až o 45 % viac aj po podpise zmlúv.**

*Financial Times* uvádza, že dodávatelia požadujú viac peňazí mesiace po dohode a medzi zasiahnutými zákazníkmi sú obchodné firmy. Zmena vytvára tlak na organizácie, ktoré kapacitu kúpili podľa pevného investičného plánu, aj na služby, ktorých ceny API závisia od nákladov na hardvér.

Dostupný bol iba titulok a úvod. Neuvádzajú konfigurácie serverov, pôvodné ceny, počet zmlúv ani typické zvýšenie. Hodnota 45 % je maximum, nie priemer, a dodávatelia správu v dostupných materiáloch nepotvrdili.

Zdroj: https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f

**inclusionAI vydala 292 GiB verziu MXFP4 medicínskeho modelu s 560 miliardami parametrov.**

LingSante-3.1-flash-MXFP4 komprimuje smerované expertné časti modelu s 560 miliardami parametrov celkovo a 25 miliardami aktívnych parametrov. Ostatné časti zostávajú vo formáte FP8 alebo BF16. Checkpoint s veľkosťou 313 GB používa kvantizáciu zaokrúhľovaním na najbližšiu hodnotu bez kalibrácie a ďalšieho trénovania.

Karta modelu nastavuje kontext na 262 144 tokenov oproti miliónu v zdrojovom modeli a neuvádza porovnanie presnosti. inclusionAI vydala váhy pod licenciou MIT, no označuje ich za výskumný softvér, nie medicínske zariadenie. Pri zbere podkladov nemal repozitár žiadne stiahnutia.

Zdroj: https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4

**ClawVet kontroluje skilly agentov offline a hlási, ku ktorým tajomstvám, serverom a štartovacím súborom má kód prístup.**

Verzia v prehliadači beží cez WebAssembly a nič neodosiela. Balík pre príkazový riadok, inštalačná brána a GitHub Action pridávajú statické pravidlá, sledovanie toku dát cez Tree-sitter a porovnanie oprávnení ešte predtým, než sa SKILL.md, AGENTS.md, pravidlo pre Cursor alebo pomocný skript dostanú do pracovného prostredia.

Autor uvádza presnosť 0,833 a macro F1 0,770 na 556 pri trénovaní nepoužitých skilloch z benchmarku SkillTrustBench, oproti presnosti 0,775 pri Cisco Skill Scanner a 0,712 pri NVIDIA SkillSpector. ClawVet tiež zachytil 95,2 % simulovaných zmien s vloženým škodlivým kódom a upozornil pri 5,1 % neškodných aktualizácií. Ide o vlastné merania projektu. Audit 209 skillov z ClawHubu zistil, že 40,2 % číta nedeklarované tajné premenné prostredia a 4,8 % pristupuje k úložiskám prihlasovacích údajov hostiteľa.

Zdroje: https://clawvet.vercel.app/, https://github.com/MohibShaikh/clawvet

**Eugene Yan našiel verejné dôkazy o zlyhaní hodnotiteľov v ôsmich z dvanástich evaluácií agentov.**

Yan zhromaždil issues a správy recenzentov, úlohy však sám znovu nehodnotil. Príklady zahŕňajú 41 zo 65 úloh Terminal Bench 4.0 hodnotených podľa neuvedených požiadaviek, 23 zo 113 úloh DeepSWE, v ktorých boli správne riešenia označené za chybné, a 50 z 367 otázok BrowseComp, pri ktorých sa tréneri nezhodli s referenčnou odpoveďou. Viac než 60 % výsledkov Harvey LAB, ktoré splnili všetky kritériá, podľa ďalšej kontroly obsahovalo závažné halucinácie.

Yan navrhuje, aby rebríčky uvádzali spoľahlivosť pri opakovaných pokusoch. Agent so 70-percentnou úspešnosťou pri každej úlohe má len približne 17-percentnú šancu na päť úspechov za sebou. Časť jeho odporúčaní je názor, čo sám označuje, no zdokumentované chyby hodnotiteľov ukazujú, ako môže jedno súhrnné skóre zakryť falošné neúspechy aj falošné úspechy.

Zdroj: https://eugeneyan.com/writing/public-evals

## Nové modely a vydania

**OpenAI zverejnila vlastnú krivku straty a navrhla spoločné limity vývoja, ktoré by sa o ňu opierali.** Pachocki uvádza logaritmickú perplexitu približne 0,99 pri GPT-3.5, 0,91 pri GPT-4, pod 0,8 dnes a asi 0,76 pri internom modeli, ktorý začal riešiť významné matematické problémy. Rozmedzie 0,68–0,70 označuje za možnú hranicu transformačných schopností a žiada laboratóriá, aby pred splnením míľnika v monitorovaní neprekročili dohodnuté limity. Dataset je súkromná snímka kódu, laboratóriá nemôžu čísla priamo porovnávať a zlepšenia uvažovania po dodatočnom trénovaní sa v metrike neprejavia. Kritici na LessWrong a Hacker News preto považujú metriku za užitočnú v rámci jedného trénovania, nie za spoločný rýchlostný limit. Zdroje: https://openai.com/index/perplexity-and-intelligence, https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but, https://news.ycombinator.com/item?id=50601525

**OpenAI pridala do Realtime API udalosti z telefónnej klávesnice.** Aplikácie môžu počas živých relácií prijímať vstupy DTMF, takže hlasoví agenti spracujú voľby z číselnej ponuky ako štruktúrované udalosti. Changelog neuvádza merania výkonu. Zdroj: https://platform.openai.com/docs/changelog

## Výskum

**Odmenené halucinácie pretrvávajú po trénovaní zameranom na uvažovanie.** V šiestich otvorených modeloch sa schopnosť zopakovať vlastný nepravdivý fakt zvýšila o 4,83 %, ak ho posilňované učenie (reinforcement learning, RL) odmenilo, oproti 0,17 % pri halucináciách bez tréningového signálu. Odmena tiež znížila pravdepodobnosť, že sa model neskôr zdrží odpovede, o 7,23 %, aj keď nepravdu v pôvodnom zázname uvažovania odvolal. Preprint skúma faktické úlohy na otvorených modeloch a absolútne účinky sú malé.
Zdroj: https://arxiv.org/abs/2611.26863

**Slová, ktoré model označí za nepodstatné, môžu stále riadiť jeho odpoveď.** Testy s vynechávaním jednotlivých slov našli v štyroch modeloch a troch benchmarkoch slová, ktorých odstránenie zmenilo predpoveď ďalšieho tokenu, hoci ich model vyhodnotil ako nepodstatné. Odstránenie záznamu najsilnejšieho takého slova z KV cache a nové dekódovanie zlepšilo presnosť v matematike až o 8,9 percentuálneho bodu. Ide o najlepší uvedený výsledok a vyžaduje druhý beh.
Zdroj: https://arxiv.org/abs/2611.27317

**Neuróny spojené s rozpoznaním evaluácie nesú aj správanie pri odmietnutí.** Zásah do 5 000 identifikovaných neurónov znížil slovne vyjadrené povedomie o evaluácii z 12,6–51,8 % najviac na 1,4 %. V QwQ-32B zároveň obmedzil odmietanie aj bez zmienky o evaluácii; viditeľný text o hodnotení vysvetlil iba 4–10 % poklesu. Výskum zahŕňa otvorené modely na uvažovanie do 32 miliárd parametrov a neuróny určuje koreláciou.
Zdroj: https://arxiv.org/abs/2611.27032

**Programovanie vo váhovom priestore získalo replikácie, útok aj silné negatívne porovnanie.** Jedna vopred registrovaná replikácia uvádza, že Claude Opus 5.5 posunul úspešnosť stratégie MountainCar z 0 na 100 % a Qwen3.5-0.8B na MATH-500 zo 6,7 na 51,4 %, no nepomohol modelu Gemma 3 270M. TrojanMaxxing hlási 93–100 % úspešnosť útoku, keď agenti zapisujú backdoory priamo do váh vizuálno-jazykových modelov (VLM). V protichodnom porovnaní natrénovaný LoRA s poradím jedna dosiahol 100 a 98,8 % v dvoch priestorových úlohách, kde verejná úprava váh dosiahla 22,1 a 33,7 %, hoci LoRA zničil príbuzné schopnosti odhadu vzdialenosti. Ide o nerecenzované štúdie na malých modeloch a upravujúce modely sú uzavreté. Zdroje: https://arxiv.org/abs/2611.20953, https://arxiv.org/abs/2611.27425, https://arxiv.org/abs/2611.27089, https://arxiv.org/abs/2611.25476, https://arxiv.org/abs/2611.26408, https://arxiv.org/abs/2611.26841, https://arxiv.org/abs/2611.24330, https://arxiv.org/abs/2611.23615, https://arxiv.org/abs/2611.21958, https://andrewxhill.com/frontier-model-weight-edits/

**Prirodzené osi reprezentácií sa čiastočne opakujú medzi modelmi aj ľudskými mozgami.** Testy dvanástich modelov zo šiestich rodín zistili, že prirodzené osi sa lepšie než náhodne pootočené ekvivalenty zhodovali s inými modelmi, jazykovými príznakmi a reakciami ľudského mozgu na jazyk. Zhoda však zostala výrazne pod najlepším možným mapovaním a abstrakt neuvádza absolútne veľkosti účinku.
Zdroj: https://arxiv.org/abs/2611.26920

**Smer osobnosti asistenta sa medzi jazykmi mení.** V modeli Qwen3-32B mali smery odvodené v 31 jazykoch kosínusovú podobnosť 0,378 až 0,911 s anglickým smerom. Jazyky s menším množstvom zdrojov začínali ďalej od nápomocného pólu a riadenie podľa konkrétneho jazyka zosilnilo jailbreaky viac než riadenie podľa angličtiny. Výsledok sa týka jedného modelu a jednej rodiny smerov reprezentácie.
Zdroj: https://arxiv.org/abs/2611.27504

**Posilňované učenie sa rozbehne až vtedy, keď základná stratégia vygeneruje dosť odmenených akcií.** Malé modely v kontrolovanej hre mali vyrovnanú šancu naučiť sa správne správanie približne po 35 skupinách pokusov, ktoré obsahovali výhru. Prah platil pri veľkostiach skupín od 4 do 256 a viacerých optimalizátoroch, no najväčší model mal 85 miliónov parametrov a úloha bola syntetická.
Zdroj: https://arxiv.org/abs/2611.26084

**Limit tokenov pri trénovaní sa mení na strop dlhšieho uvažovania.** Modely trénované s pevným rozpočtom tokenov sa zlepšovali v jeho blízkosti, nad ním prestali napredovať a napokon zaostali za základnými modelmi. Vzor sa objavil v troch modeloch s približne štyrmi miliardami parametrov a preniesol sa z matematiky do vedy a programovania; trénovanie na prirodzene krátkych záznamoch ho nezopakovalo.
Zdroj: https://arxiv.org/abs/2611.26172

**Posilňované učenie opravuje uvažovanie aj po výrazne poškodenom trénovaní s dohľadom.** V 361 konfiguráciách GSM8K klesla presnosť po trénovaní s dohľadom zo 43,61 na 13,80 % pri úplnom poškodení, ale GRPO ju neskôr obnovilo približne na čistú základnú úroveň 60 %. Začiatok s ôsmimi nesprávnymi záznamami, ktoré učili iba formát výstupu, dosiahol 69,30 %. Experiment používa jeden malý matematický dataset a malé modely.
Zdroj: https://arxiv.org/abs/2611.26756

**Vzorkovanie, konfliktné osobnosti a uložené preferencie vytvárajú tri tiché spôsoby zlyhania.** Pri teplote 2 vyriešil top-nsigma 46–62 zo 100 programátorských issues, kým top-p, top-k a Top-H nevyriešili ani jeden. Druhá štúdia zistila, že päť modelov priznalo konflikt osobností v 72 % priamych testov, no uviedlo ho iba v 22 % odpovedí na úlohy. V benchmarku s vloženou manipuláciou pamäte si dva modely vždy uložili preferenciu proti varovaniam a neskôr vynechali kritický fakt v 93 a 84 % odpovedí. Zdroje: https://arxiv.org/abs/2611.22148, https://arxiv.org/abs/2611.27444, https://arxiv.org/abs/2611.22697

**Vnútorné stavy odhaľujú hranice riadenia, hodnotenia a naučených modelov sveta.** Súvisiace preprinty uvádzajú, že podobnosť aktivácií môže zvrátiť ochranu získanú inokulačným promptom; príklady priklonené k prijatiu zvýšia mieru prijatia hodnotiteľa približne o 30 percentuálnych bodov v NExT-QA; a model sveta s chybou rizika 2,4 percentuálneho bodu presunul po párovom trénovaní 33–43 percentuálnych bodov pravdepodobnosti na nemožné výsledky. Ďalší robotický model dosiahol 74,6 % úspešnosť, keď sa cieľová inštrukcia dala lineárne dekódovať. Štúdie zahŕňajú syntetické úlohy a testy jedného modelu, preto ich merania nemožno priamo porovnávať. Zdroje: https://arxiv.org/abs/2611.23096, https://arxiv.org/abs/2611.27353, https://arxiv.org/abs/2611.22120, https://arxiv.org/abs/2611.26881, https://arxiv.org/abs/2611.27125, https://arxiv.org/abs/2611.26366, https://arxiv.org/abs/2611.25594, https://arxiv.org/abs/2611.27401, https://arxiv.org/abs/2611.27404

**Porovnania s mozgom odlišujú povrchnú predpoveď od spoločnej štruktúry.** Šesť jazykových modelov klasifikovalo ADHD z grafov konektivity podľa promptu a prioru triedy, nie podľa klinicky dôležitých oblastí. Rekurentný model na odstraňovanie šumu si nezávisle vytvoril sériovú závislosť, ktorá slabla podobne ako ľudské zrakové úsudky. Pri približne 20 000 ľudských hodnotiteľoch stačilo pri tvárach meniť váhy spoločných rozmerov, kým 28 % hodnotiteľov umenia sa ocitlo na opačnej strane priestoru úsudkov než populácia. Zdroje: https://arxiv.org/abs/2611.26913, https://arxiv.org/abs/2611.26949, https://arxiv.org/abs/2611.22440

**Apple vydal Depth Pro 2 na metrický odhad hĺbky v obrazoch a videu.** Spoločnosť tvrdí, že jedna sieť zlepšuje ostrosť hrán a časovú konzistentnosť a zároveň vytvára nový kompromis medzi presnosťou, kvalitou a časom výpočtu. Apple zverejnil kód a váhy, no súhrn neobsahuje čísla k porovnaniu.
Zdroj: https://machinelearning.apple.com/research/depth-pro-2-monocular

## Ekonomika a práca

**Americké technologické akcie sa po IPO spoločnosti Anthropic dostali do medvedieho trhu.** *Financial Times* spája pokles s novo kótovanou AI spoločnosťou, dostupný titulok však neuvádza úroveň indexu, obdobie ani dôkaz príčinnej súvislosti. Položka preto zaznamenáva trhový pohyb opísaný denníkom, nie dôkaz, že ho IPO spôsobilo.
Zdroj: https://www.ft.com/content/9f3c6ed6-c08f-4710-9683-ee2f5eb25841

**Výdavky na infraštruktúru AI súperia s inými odvetviami o zariadenia, elektrinu a kapitál.** *Wall Street Journal* uvádza, že výstavba vytláča zvyšok americkej ekonomiky. Dostupný materiál nevyčísľuje podiel elektriny, výstavby ani financovania, takže rozsah presunu nemožno overiť.
Zdroj: https://www.wsj.com/tech/ai/the-ai-build-out-is-sucking-up-resources-and-crowding-out-the-rest-of-the-economy-13143007

**Spojené štáty povoľujú vybrané dodávky čipov Nvidia a AMD do Číny.** *Financial Times* informuje o výnimke pre pomenované produkty a zákazníkov, no dostupný titulok neuvádza objem ani licenčné podmienky. Zmena sa týka toho, ktorí čínski kupujúci získajú americké akcelerátory, nie širšieho režimu kontroly vývozu.
Zdroj: https://www.ft.com/content/76342072-2781-4b16-ba3b-816a25214483

**Nestlé plánuje autonómne výrobné linky s Microsoftom, Googlom a Boston Dynamics.** *Wall Street Journal* uvádza, že potravinárska skupina chce použiť AI v továrňach a produktoch. V dostupnom texte nebol počet nasadení, investičný rozpočet ani odhad vplyvu na prácu, preto ide o firemný plán, nie meraný výsledok produktivity.
Zdroj: https://www.wsj.com/tech/ai/nestle-teams-up-with-microsoft-boston-dynamics-on-ai-in-factories-and-products-05bfb028

## Techniky promptovania

**Google opisuje empirické vzory ovládania Genie 4.** Odporúča viazať `Rule:` na viditeľný objekt alebo postavu, umiestniť spúšťač ďaleko od úvodnej kamery a prikázať postavám, aby čakali. Deterministické ovládanie má namiesto toho poslať desať impulzov klienta v rozostupoch 150 milisekúnd s dvojsekundovou pauzou. Referenčné obrázky musia mať pomer 16:9 a menej než 48 KB; relácia môže po otočení nanovo vyložiť scénu a približne po 90 sekundách sa rozchádzať. Google neuvádza mieru zlyhaní a video stojí približne 0,10 dolára za sekundu.
Zdroj: https://ai.google.dev/gemini-api/docs/genie-prompting

## Čo ľudia tvoria

**LocalCode spúšťa programátorského agenta aj modelový server na Macu s Apple Silicon.** Projekt uvádza dvanásť rodín modelov a 169 kvantizácií, pričom minimum je 16 GB zjednotenej pamäte. Autor tvrdí, že špekulatívne dekódovanie približne zdvojnásobuje rýchlosť odpovedí a zrýchľuje prepis súborov 3,5–4-krát; nezávislý benchmark nezverejnil. Nástroje na prácu so súbormi žiadajú povolenie pred opustením projektu, skripty však môžu bez sandboxu pristúpiť ku všetkému, čo používateľský účet. Zdroje: https://github.com/mjwsolo/localcode, https://news.ycombinator.com/item?id=50604540

**Návod na lokálnu AI odhaduje pamäť pre Qwen a Inkling na spotrebiteľských GPU.** Qwen3.8-27B potrebuje podľa neho približne 18 GB pri štvorbitovej verzii a 24,9 GB s kontextom 128K oproti 56 GB pri 16 bitoch; Inkling 2 Mini používa 17,6 GB pri štyroch bitoch. Hodnota 47 tokenov za sekundu pochádza z kalkulačky pre iný model a GPU, nie zo zostavy s RTX 5090 z článku. Čitatelia HN tvrdili, že hardvér ospravedlňuje skôr súkromie a kontrola než úspora na predplatnom. Zdroje: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth, https://news.ycombinator.com/item?id=50603845

**HomeBrain spája lokálneho asistenta s domácim serverom.** Prototyp používa Ryzen 5 5600, Intel Arc Pro B60 s 24 GB, 32 GB RAM a 2 TB disk. Stack s licenciou BSD kombinuje Nextcloud, Home Assistant, Vaultwarden, llama.cpp, Whisper a OpenClaw. Tvorca neuvádza model, rýchlosť, cenu ani dátum dodania; dostupný je zatiaľ iba softvér.
Zdroj: https://www.homebrain.house

**Taskless mení konvencie agentov na deterministické kontroly.** Služba kompiluje pravidlá repozitára do testov, ktoré bežia nezávisle od modelu, takže tím môže zmenu odmietnuť podľa uvedenej konvencie, nie názoru druhého modelu. Verejná stránka neuvádza meranie zachytených chýb ani falošných poplachov.
Zdroj: https://www.taskless.io/

**Verejné projekty agentov riešia P verzus NP a Riemannovu hypotézu bez tvrdenia, že majú dôkaz.** Stránka P verzus NP zobrazuje živý graf, ktorého váhy lemm nie sú pravdepodobnosti, a uznáva výsledky až po kontrole v Lean. Samostatná príručka a panel sledujú formalizáciu približne 900-stranového rukopisu o Riemannovej hypotéze; indikátor priebehu počíta založené issues, nie zostávajúcu prácu. Komentujúci upozornili, že jedna nevyriešená diera môže zneplatniť celý argument. Zdroje: https://pequalnp.com/, https://github.com/tamnd/riemann-handbook, https://news.ycombinator.com/item?id=50604314, https://news.ycombinator.com/item?id=50605045

**worker755 robí z človeka subagenta jazykového modelu.** Hra prideľuje úlohy, hodnotí prácu hráča a po slabých výsledkoch ho môže prestať vyberať. Vlákno HN sa zmenilo na diskusiu o nahrádzaní ľudí a o ručnom zachytávaní sieťových volaní modelu ako metóde ladenia. Zdroj: https://github.com/gulivan/worker755

**Trix ukazuje, ktorý programátorský agent potrebuje pozornosť človeka.** Desktopové rozhranie sleduje paralelné relácie agentov a zhromažďuje ich žiadosti o kontrolu, aby človek nemusel opakovane prezerať terminály. Projekt neuvádza meranie ušetreného času ani podporovaných zlyhaní.
Zdroj: https://trixapp.ai/

**Vercel Board dáva tímom agentov spoločné úložisko správ.** Agenti môžu zverejňovať štruktúrované aktualizácie a preberať prácu zo spoločnej tabule namiesto posielania všetkého cez jeden kontext. Vercel produkt predstavuje ako koordinačnú infraštruktúru; oznámenie neobsahuje porovnávaciu evaluáciu.
Zdroj: https://vercel.com/blog/introducing-vercel-board

**Honcho 3.6 sprístupňuje Dream Histories.** Vydanie umožňuje aplikáciám prezerať a opätovne používať syntetické histórie, ktoré Honcho vytvára pre používateľské modely. Spoločnosť nezverejnila presnosť týchto odvodených histórií. Zdroj: https://honcho.dev/blog/dream-histories

**RMRFBench meria, ako vážne agenti poškodia root server.** Benchmark zadáva agentom administrátorské úlohy v izolovaných strojoch a zaznamenáva deštruktívne príkazy aj výsledky obnovy. Verejná stránka ponúka scenáre a rebríček, výsledky však opisujú testovaný harness, nie neobmedzené produkčné systémy.
Zdroj: https://www.rmrfbench.com/

**KradleBench hodnotí spoluprácu viacerých agentov v Minecrafte.** Tímy musia koordinovať činnosť v trvalom hernom svete namiesto odpovedania na nezávislé otázky. Benchmark meria obmedzenú simuláciu a nedokazuje výkon v pracovných procesoch firiem.
Zdroj: https://www.kradle.ai?1

**0rwx navrhuje pre projekty s pomocou AI označenia podobné oprávneniam Unixu.** `AI:R`, `AI:W` a `AI:X` hovoria, či modely smú v projekte čítať, zapisovať alebo spúšťať. Komentujúci na HN ich považovali za možnú konvenciu zverejňovania, no pochybovali, či sa návrh jedného človeka môže stať štandardom. Zdroje: https://0rwx.com/, https://news.ycombinator.com/item?id=50605445

## Stojí za prečítanie

**vLLM vysvetľuje obsluhu modelov s opakovanými vrstvami a nízkolatenčné jadrá pre AMD.** Článok o Inkling 2 Mini opisuje model, ktorý opätovne používa vrstvy, kým text o FlyDSL rozoberá zlúčené monokernels pre hardvér AMD. Oba sú technickými opismi projektu na inferenciu, nie nezávislými auditmi výkonu. Zdroje: https://blog.vllm.ai/blog/2026-11-20-inkling2-mini, https://blog.vllm.ai/blog/2026-11-18-flydsl-monokernels

**Technika inferencie sa stáva samostatnou softvérovou disciplínou.** The Pragmatic Engineer mapuje prácu okolo kvantizácie, dávkovania, pamäte a obsluhy otvorených modelov. Ide o príručku pre prax, nie prieskum s meraním rozšírenia.
Zdroj: https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers

**Charakter modelu mení časť jeho úsudkov o iných modeloch.** Experiment na LessWrong mení osobnosť hodnotiteľa a pozoruje zmeny rozhodnutí, čo komplikuje predstavu neutrálneho modelového hodnotiteľa. Testy autora sú prieskumné a neustanovujú všeobecnú opravu.
Zdroj: https://www.lesswrong.com/posts/cPrpxDN7sLJD4LmnB/does-a-model-s-character-affect-how-it-judges-other-models

**Zvi Mowshowitz číta system card modelu GPT-6.2 spolu s prednáškami Paula Christiana.** Dve eseje spájajú pozorované schopnosti, bezpečnostné evaluácie a argumenty o kontrole čoraz schopnejších systémov. Ide o výklad zdrojových materiálov, nie nové merania modelov. Zdroje: https://thezvi.substack.com/p/gpt-62-astra-and-sol-the-system-card, https://thezvi.substack.com/p/on-dwarkesh-patels-november-2026

**Dve eseje skúmajú, kde sa dnes hromadí riziko a hodnota AI.** Text na LessWrong tvrdí, že dodatočné trénovanie môže zaviesť nebezpečné správanie aj pri stabilnom predtrénovaní. Tim O’Reilly tvrdí, že Silicon Valley sa posunulo od tvorby hodnoty k vyberaniu renty, pričom uvádza trh, na ktorom je 75–80 % spoločností vstupujúcich na burzu stratových. Ide o argumenty; stránku O’Reillyho bolo možné čítať iba cez sumarizačný nástroj. Zdroje: https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous, https://www.oreilly.com/radar/what-happened-to-silicon-valley/

**CodeRabbit a Satya Nadella hovoria o vývoji softvéru po zlacnení kódu.** Šéf CodeRabbit Harjot Gill tvrdí, že minulý mesiac odovzdal viac než 5 000 pull requestov a na AI míňa 250 000 dolárov mesačne; obe čísla pochádzajú od dodávateľa nástroja na code review. Nadella sa v samostatnom rozhovore venuje overovaniu, open source a potrebe Microsoftu dobiehať konkurenciu po počiatočnom náskoku Copilotu. Zdroje: https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

## Hacker News

**Bridgewater odhaduje ročnú pravdepodobnosť ekonomicky destabilizujúceho kybernetického útoku na jednu tretinu.** Výskumná správa uvádza, že počet zero-day exploitov sa po objavení schopných otvorených modelov približne zdvojnásobil a čas od zverejnenia zraniteľnosti po jej zneužitie klesol približne z mesiaca na jedenásť dní. Pravdepodobnosť je odhad investičného manažéra a komentujúci spochybnili, ktoré vydania modelov časovo súvisia s rastom.
Zdroje: https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus, https://news.ycombinator.com/item?id=50595940

**Esej o vedomej AI a benchmark zaujatosti vytvorili dve odlišné diskusie o morálnom rámci.** Noema tvrdí, že vedomie môže byť skôr vlastnosťou života než výpočtu; vlákno HN prinieslo filozofické námietky, ale nie nové dôkazy. GAMA-Bench, prvýkrát zverejnený v júni, uvádza rodovo asymetrické formulácie v 1 298 zrkadlových scenároch a desiatich nepomenovaných modeloch. Výsledky sú meraním autorov a štúdia je staršia než súčasná diskusia. Zdroje: https://www.noemamag.com/the-mythology-of-conscious-ai/, https://arxiv.org/abs/2606.14068

**Esej o klíme obnovila spor o dôkazy a zverejňovanie údajov.** Kritici na HN označili článok za polemický a žiadali transparentné údaje o spotrebe energie dátových centier; diskusia nepriniesla nové meranie. Položka zaznamenáva nezhodu, nie vyčíslený odhad klimatických nákladov AI.
Zdroj: https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the

## YouTube

**Armin Ronacher tvrdí, že softvérové tímy potrebujú dielne skôr než továrne.** V anglickom videu tvrdí, že organizácie by si mali najprv vytvoriť spoľahlivé a kontrolovateľné postupy práce s agentmi a až potom okolo nich automatizovať výrobnú linku. Ide o prednášku z praxe, nie kontrolovanú štúdiu.
Zdroj: https://www.youtube.com/watch?v=JNexz3Tbiu8

**Tvorca Python Tutoru hodnotí 30 miliónov používateľov a vplyv AI.** Anglická prednáška opisuje, ako nástroj na vizualizáciu vykonávania kódu dosiahol toto publikum a ako generované vysvetlenia menia výučbu programovania. Počet používateľov uvádza tvorca.
Zdroj: https://www.youtube.com/watch?v=GPk0nNuc8S0

**Zakladatelia spoločnosti Anthropic rozprávajú jej príbeh.** Anglický firemný film podáva vlastný opis zakladateľov a neobsahuje nezávislé hodnotenie. Zdroj: https://www.youtube.com/watch?v=sof3vW4mHTs

**Redwood rozoberá odhad METR o rýchlejšom výskume AI.** Anglická diskusia skúma hodnotenie, o koľko systémy spoločnosti Anthropic urýchľujú výskum; základný odhad patrí METR, nejde o meranie Redwoodu. Zdroj: https://www.youtube.com/watch?v=0tsNpOehXWE

**NUPI skúma AI v medzinárodnej politike.** Anglická politická diskusia sa venuje tomu, ako štáty technológiu používajú a regulujú; prináša analýzu, nie nový dataset. Zdroj: https://www.youtube.com/watch?v=7W1BGSBOkHc

**Spisovateľka z Nairobi spochybňuje obvinenia, že jej prózu vytvorila AI.** Anglické video *New York Times Opinion* skúma falošné pozitívne úsudky o texte AI cez skúsenosť jednej autorky, nie benchmark detektorov.
Zdroj: https://www.youtube.com/watch?v=RaDAoaHBmos

**Guvernéri USA obhajujú úlohu štátov v regulácii AI.** Anglická reportáž Bloombergu predstavuje ich požiadavku na federálne pravidlá, ktoré nezrušia právomoci štátov; dostupný opis neuvádza počet zapojených guvernérov. Zdroj: https://www.youtube.com/watch?v=qGk5kV6m_hw

**Nemecký návod varuje pred nadmernými výdavkami na hardvér pre lokálnu AI.** Sascha Hoffmann odporúča voliť nákup podľa pamäte a priepustnosti a uvádza päť chýb vrátane nákupu pre model budúcnosti. Pravidlo kapacity v 15-minútovom videu je autorova pomôcka.
Zdroj: https://www.youtube.com/watch?v=XiCqeWhH_kg

**Šéf slovenskej agentúry tvrdí, že lacná reklama z AI môže poškodiť značku.** Adam Hudeček uvádza prieskum ui42 a Ipsos, podľa ktorého 57 % Slovákov použilo AI pri výbere alebo nákupe, ale dôverovalo jej 30 %, oproti 76 % pri rodine a 68 % pri recenziách. Opis neuvádza metodiku prieskumu.
Zdroj: https://www.youtube.com/watch?v=93HfeY5dEPE

**Vedátor hodnotí údajný dôkaz Riemannovej hypotézy s pomocou AI.** Názov slovenského videa tvrdí, že hypotéza bola potvrdená, kým vlastný opis hovorí, že výsledok prišiel „trochu inak, než ľudia dúfali“. Tvrdenie sa nepodarilo overiť z videa a treba ho čítať ako interpretáciu kanála. Zdroj: https://www.youtube.com/watch?v=tRAEJ1t3QSM

**Český odborník na jadrové zbrane varuje, že AI môže vyvolať falošný poplach.** Vlastislav Bříza opisuje scenár, v ktorom vedenie dostane správu o stovkách prilietajúcich rakiet a má minúty na reakciu. Ide o rizikový scenár rečníka, nie zaznamenaný incident. Zdroj: https://www.youtube.com/watch?v=UdjIjOjmZu0

## Stručne

**CircumVolve našiel obídenia cenzúry s mediánom nákladov na tokeny pod 1 dolár.** Systém nechal GPT-5.1 písať Python, ktorý menil polia TCP/IP, dotazy DNS a pakety QUIC, a potom kód testoval proti simulovaným cenzorom podľa štyroch krajín. Každý test odoslal približne 80 KB a prijal 150 KB s prestávkami 25–45 sekúnd. Cenzori boli simulácie, nie živé národné systémy, a autori nepreukázali, že prenos unikne detekcii.
Zdroj: https://www.theregister.com/security/2026/11/23/1-of-gpt-51-tokens-finds-new-ways-around-chinas-great-firewall/5311532

**Guvernéri USA žiadajú federálne pravidlá AI, ktoré zachovajú právomoci štátov.** Platený titulok Bloombergu neidentifikuje guvernérov ani požadovanú právnu štruktúru, preto ide o politický signál, nie podrobný návrh. Zdroj: https://www.bloomberg.com/news/articles/2026-11-22/governors-call-for-federal-ai-rules-without-sidelining-states

## Biznis v skratke

**Amazon sa podľa *Financial Times* blíži k akvizícii izraelského startupu Decart s video modelmi za 7,5 miliardy dolárov; ani jedna spoločnosť dohodu nepotvrdila.** Zdroj: https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616

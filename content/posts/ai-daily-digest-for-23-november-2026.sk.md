+++
title = "Denný prehľad AI – 23. novembra 2026"
slug = "denny-prehlad-ai-23-novembra-2026"
description = "Microsoft prestavuje VS Code okolo agentov, kým Satya Nadella tvrdí, že bežné IDE ustúpili do úzadia, a dodávatelia AI serverov žiadajú zdraženie až o 45 %. Otvorený medicínsky model dostal 292 GiB verziu MXFP4 a nový skener kontroluje skilly agentov pred inštaláciou."
tags = ["tools", "research", "agents", "hardware"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

Spoločnou niťou dnešných správ je overovanie: softvéroví agenti menia vývojové prostredie, verejné hodnotenia dokážu odmietnuť správnu prácu a viaceré výskumné skupiny zistili, že uvádzané uvažovanie modelu spoľahlivo neopisuje signály, ktoré ho skutočne riadia.

## Hlavné správy

**Satya Nadella tvrdí, že bežné IDE ustúpili za šesť mesiacov, zatiaľ čo Microsoft mení VS Code na konzolu pre agentov.**

Šéf Microsoftu povedal Gergelymu Oroszovi, že Claude Code urobil z príkazového riadka hlavné rozhranie a že IDE v priebehu približne šiestich mesiacov „akoby vybledli“. Predpovedal tiež, že IDE sa môže vrátiť skôr ako miesto na špecifikácie, súbory Markdown a revízie než ako prostredie, v ktorom sa píše väčšina kódu.

Produktový vývoj Microsoftu tento posun odráža. VS Code 1.146 pridal schránku pre agentov a porovnávanie modelov; verzia 1.147 pridala smerovanie modelov, plánované požiadavky pre agentov a integráciu prehliadača. Vnútri editora môžu pracovať agenti Copilot, Claude aj Codex. Prieskum citovaný portálom Windows Latest však stále uvádzal používanie VS Code na úrovni 70,9 % medzi 13 193 respondentmi, čo je pokles zo 75,9 % v roku 2025. Nadellovo tvrdenie, že „vybledli“, je preto interpretáciou, nie meraním používania.

Zdroj: https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/

**Spoločnosti Dell, HPE, Lenovo a Supermicro údajne žiadajú zvýšenie cien AI serverov až o 45 % už po podpise zmlúv.**

Denník *Financial Times* uvádza, že dodávatelia pýtajú viac peňazí niekoľko mesiacov po uzatvorení kontraktov, pričom medzi zasiahnutými kupujúcimi sú aj obchodné firmy. Takýto krok vytvára tlak na organizácie, ktoré nakupovali kapacity v rámci pevného investičného plánu, aj na služby, ktorých ceny API závisia od nákladov na tento hardvér.

Dostupné boli len titulok a perex. Neuvádzajú konfigurácie serverov, pôvodné ceny, počet zmlúv ani typickú výšku zdraženia. Hodnota 45 % predstavuje strop, nie priemer, a dodávatelia túto správu v dostupnom materiáli nepotvrdili.

Zdroj: https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f

**inclusionAI vydala 292 GiB verziu MXFP4 svojho medicínskeho modelu s 560 miliardami parametrov.**

LingSante-3.1-flash-MXFP4 komprimuje smerovaných expertov modelu s celkovo 560 miliardami a 25 miliardami aktívnych parametrov. Ostatné časti zostávajú vo formátoch FP8 alebo BF16. Tento 313 GB checkpoint používa zaokrúhľovaciu kvantizáciu bez kalibrácie a bez dodatočného trénovania.

Karta modelu nastavuje kontextové okno na 262 144 tokenov oproti jednému miliónu pri pôvodnom modeli a nezverejňuje žiadne porovnanie presnosti medzi oboma verziami. Spoločnosť inclusionAI uvoľňuje váhy pod licenciou MIT, ale označuje ich za výskumný softvér, nie za zdravotnícku pomôcku. V čase zberu podkladov nemal repozitár žiadne stiahnutia.

Zdroj: https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4

**ClawVet skenuje skilly agentov offline a hlási, k akým tajným údajom, serverom a štartovacím súborom sa ich kód môže dostať.**

Prehliadačová verzia beží cez WebAssembly a nič nenahráva na server. Balík pre príkazový riadok, inštalačná brána a GitHub Action pridávajú statické pravidlá, sledovanie toku údajov pomocou Tree-sitter a porovnávanie zmien oprávnení predtým, než sa SKILL.md, AGENTS.md, pravidlo pre Cursor alebo pomocný skript dostane do pracovného prostredia.

Autor uvádza presnosť 0,833 a makro F1 na úrovni 0,770 na 556 pri trénovaní nepoužitých (held-out) skilloch zo SkillTrustBench oproti presnosti 0,775 pri Cisco Skill Scanner a 0,712 pri NVIDIA SkillSpector. ClawVet tiež zachytil 95,2 % simulovaných zmien so vkladaním kódu, pričom pri neškodných aktualizáciách upozornil v 5,1 % prípadov. Ide o vlastné merania projektu. Jeho audit 209 skillov z ClawHub ukázal, že 40,2 % čítalo nedeklarované tajné premenné prostredia a 4,8 % pristupovalo k úložiskám prihlasovacích údajov hostiteľského systému.

Zdroje: https://clawvet.vercel.app/, https://github.com/MohibShaikh/clawvet

**Eugene Yan našiel verejné dôkazy o chybách hodnotičov v ôsmich z dvanástich evaluácií agentov.**

Yan zozbieral záznamy z prehľadov issues a správy recenzentov, úlohy však sám neprehodnocoval. Medzi príkladmi je 41 zo 65 úloh v Terminal Bench 4.0 hodnotených podľa neuvedených požiadaviek, 23 zo 113 úloh v DeepSWE, pri ktorých boli správne riešenia označené za chybné, a 50 z 367 otázok v BrowseComp, pri ktorých sa školitelia nezhodli s referenčnou odpoveďou. Viac než 60 % výsledkov Harvey LAB, ktoré splnili každé kritérium, obsahovalo v inom posúdení závažné halucinácie.

Navrhuje, aby rebríčky uvádzali spoľahlivosť pri opakovaných pokusoch. Agent, ktorý uspeje v 70 % prípadov na každej úlohe, má len približne 17 % šancu na päť po sebe idúcich úspechov. Jeho odporúčania sú sčasti názorom, čo sám označuje, no zdokumentované chyby hodnotičov ukazujú, prečo jedno súhrnné skóre dokáže zakryť falošné zlyhania aj falošné úspechy.

Zdroj: https://eugeneyan.com/writing/public-evals

## Nové modely a vydania

**OpenAI zverejnila internú krivku straty a navrhla na ňu naviazané spoločné vývojové limity.** Pachocki uvádza logaritmickú perplexitu blízko 0,99 pre GPT-3.5, 0,91 pre GPT-4, pod 0,8 v súčasnosti a približne 0,76 vo chvíli, keď interný model začal riešiť významné matematické problémy. Pásmo 0,68–0,70 označuje za možné okno prelomových schopností a žiada laboratóriá, aby neprekračovali dohodnuté limity pred dosiahnutím monitorovacieho míľnika. Dataset tvorí súkromný snímok kódu, rôzne laboratóriá nemôžu svoje čísla porovnávať priamo a zlepšenia v uvažovaní z dotrénovania sa v tejto metrike neprejavujú. Kritici na LessWrong a Hacker News preto navrhované meradlo vnímajú ako užitočné v rámci jedného trénovacieho behu, no nevhodné ako spoločný rýchlostný limit. Zdroje: https://openai.com/index/perplexity-and-intelligence, https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but, https://news.ycombinator.com/item?id=50601525

**OpenAI pridala do Realtime API udalosti telefónnej klávesnice.** Aplikácie teraz môžu počas živých relácií prijímať vstupy DTMF, vďaka čomu hlasoví agenti zvládnu hlasové menu cez klávesnicu ako štruktúrované udalosti. Záznam zmien neuvádza žiadne merania výkonu. Zdroj: https://platform.openai.com/docs/changelog

## Výskum

**Odmenené halucinácie pretrvávajú aj po uvažovacom dotrénovaní.** V šiestich otvorených modeloch vzrástlo opakovanie vlastného vymysleného faktu o 4,83 %, keď ho posilňované učenie (reinforcement learning, RL) odmenilo, oproti 0,17 % pri halucináciách bez trénovacieho signálu. Odmena tiež spôsobila, že modely sa neskôr zdržali odpovede o 7,23 % menej často, a to aj vtedy, keď nepravdu v pôvodnom zázname uvažovania samy odvolali. Preprint skúma faktické úlohy na otvorených modeloch a absolútne účinky sú malé.
Zdroj: https://arxiv.org/abs/2611.26863

**Slová, ktoré modely označia za nepodstatné, dokážu napriek tomu zmeniť ich odpoveď.** V štyroch modeloch a troch porovnávacích testoch (benchmarkoch) odhalili vynechávacie testy slová v kontexte, ktorých odstránenie prevrátilo predpoveď nasledujúceho tokenu, hoci model tieto slová vyhodnotil ako nedôležité. Odstránenie záznamu z KV cache pre najsilnejšie takéto slovo a opätovné dekódovanie zlepšilo presnosť v matematike až o 8,9 percentuálneho bodu. Ide o najlepší uvádzaný prípad a vyžaduje si druhý priechod.
Zdroj: https://arxiv.org/abs/2611.27317

**Neuróny spojené s rozpoznávaním hodnotenia nesú aj správanie odmietania.** Zásah do 5 000 identifikovaných neurónov znížil slovne vyjadrené uvedomovanie si hodnotenia z 12,6–51,8 % nanajvýš na 1,4 %. V modeli QwQ-32B zároveň znížil mieru odmietania aj vtedy, keď model hodnotenie vôbec nespomenul; viditeľný text o uvedomovaní si hodnotenia vysvetlil len 4–10 % tohto poklesu. Práca sa týka otvorených uvažovacích modelov do 32 miliárd parametrov a neuróny identifikuje korelačne.
Zdroj: https://arxiv.org/abs/2611.27032

**Programovanie v priestore váh prinieslo replikácie, útok aj silné protikladné porovnanie.** Jedna vopred registrovaná replikácia uvádza, že Claude Opus 5.5 posunul stratégiu (policy) v úlohe MountainCar z 0 na 100 % úspešnosti a zlepšil Qwen3.5-0.8B zo 6,7 na 51,4 % v teste MATH-500, no modelu Gemma 3 270M nepomohol. TrojanMaxxing hlási 93–100 % úspešnosť útoku, keď agenti zapisujú zadné vrátka priamo do váh vizuálno-jazykových modelov (VLM). V protikladnom porovnaní dosiahol natrénovaný modul LoRA s hodnosťou jeden 100 a 98,8 % v dvoch priestorových úlohách, v ktorých verejná úprava váh dosiahla 22,1 a 33,7 %, hoci LoRA zničila blízke schopnosti odhadu vzdialenosti. Ide o nerecenzované štúdie na malých modeloch a upravujúce modely sú uzavreté. Zdroje: https://arxiv.org/abs/2611.20953, https://arxiv.org/abs/2611.27425, https://arxiv.org/abs/2611.27089, https://arxiv.org/abs/2611.25476, https://arxiv.org/abs/2611.26408, https://arxiv.org/abs/2611.26841, https://arxiv.org/abs/2611.24330, https://arxiv.org/abs/2611.23615, https://arxiv.org/abs/2611.21958, https://andrewxhill.com/frontier-model-weight-edits/

**Prirodzené osi reprezentácií sú sčasti spoločné pre modely aj ľudský mozog.** Testy v dvanástich modeloch zo šiestich rodín zistili, že prirodzené osi sa zhodovali lepšie než náhodne pootočené ekvivalenty s inými modelmi, jazykovými črtami a reakciami ľudského mozgu na reč. Zhoda zostala výrazne pod najlepším možným mapovaním a abstrakt neuvádza absolútne veľkosti účinku.
Zdroj: https://arxiv.org/abs/2611.26920

**Smer osobnosti asistenta sa medzi jazykmi mení.** V modeli Qwen3-32B mali smery získané v 31 jazykoch kosínusovú podobnosť s anglickým smerom od 0,378 do 0,911. Jazyky s menším množstvom dát začínali ďalej od nápomocného pólu a jazykovo špecifické riadenie aktivácií (activation steering) zosilňovalo jailbreak (obídenie ochrán) viac než anglické riadenie aktivácií. Výsledok sa týka jedného modelu a jednej rodiny smerov reprezentácie.
Zdroj: https://arxiv.org/abs/2611.27504

**Posilňované učenie sa rozbehne až po tom, ako základná stratégia nazbiera dosť odmenených akcií.** Malé modely trénované v kontrolovanej hre dosiahli vyrovnanú šancu naučiť sa správne správanie približne po 35 skupinách pokusov, ktoré obsahovali výhru. Tento prah platil pri veľkostiach skupín od 4 do 256 aj pri viacerých optimalizátoroch, no najväčší model mal 85 miliónov parametrov a úloha bola syntetická.
Zdroj: https://arxiv.org/abs/2611.26084

**Strop dĺžky priebehu (rolloutu) počas trénovania sa mení na strop pre dlhšie uvažovanie.** Modely trénované s pevným rozpočtom tokenov sa zlepšovali blízko tohto rozpočtu, nad ním sa zlepšovanie zastavilo a napokon klesli pod svoje základné modely. Tento vzorec sa objavil v troch modeloch s približne štyrmi miliardami parametrov a preniesol sa z matematiky do prírodných vied a programovania; trénovanie na prirodzene krátkych záznamoch ho nereprodukovalo.
Zdroj: https://arxiv.org/abs/2611.26172

**Posilňované učenie dokáže opraviť uvažovanie po silne poškodenom trénovaní s dohľadom.** V 361 konfiguráciách na datasete GSM8K klesla presnosť trénovania s dohľadom pri úplnom poškodení dát zo 43,61 na 13,80 %, no metóda GRPO neskôr obnovila výkon približne na čistú východiskovú úroveň 60 %. Začiatok z ôsmich nesprávnych záznamov, ktoré učili len tvar výstupu, dosiahol 69,30 %. Experiment používa jeden malý matematický dataset a malé modely.
Zdroj: https://arxiv.org/abs/2611.26756

**Vzorkovanie, protichodné persony a uložené preferencie vytvárajú tri tiché spôsoby zlyhania.** Pri teplote 2 vyriešila metóda top-nsigma 46–62 zo 100 programátorských úloh, kým top-p, top-k a Top-H nevyriešili ani jednu. Druhá štúdia zistila, že päť modelov priznalo protichodné persony v 72 % priamych kontrol, no rozpor spomenulo len v 22 % odpovedí pri úlohách. V benchmarku na vkladanie údajov do pamäte si dva modely zakaždým uložili preferenciu proti varovaniam a neskôr vynechali kľúčový fakt v 93 a 84 % odpovedí. Zdroje: https://arxiv.org/abs/2611.22148, https://arxiv.org/abs/2611.27444, https://arxiv.org/abs/2611.22697

**Vnútorné stavy odhaľujú hranice riadenia aktivácií, hodnotenia modelmi aj naučených modelov sveta.** Príbuzné preprinty uvádzajú, že podobnosť aktivácií môže zrušiť účinok očkovacieho promptovania; niekoľko ukážkových príkladov typu „prijať“ zvyšuje mieru prijatia u hodnotiaceho modelu približne o 30 bodov v teste NExT-QA; a model sveta s 2,4-bodovou chybou rizika presunul po párovom trénovaní 33–43 bodov pravdepodobnosti na nemožné výsledky. Iný robotický model dosiahol 74,6 % úspešnosť úloh, keď sa jeho cieľový pokyn stal lineárne dekódovateľným. Tieto štúdie zahŕňajú syntetické úlohy a testy na jednom modeli, takže ich merania nie sú priamo porovnateľné. Zdroje: https://arxiv.org/abs/2611.23096, https://arxiv.org/abs/2611.27353, https://arxiv.org/abs/2611.22120, https://arxiv.org/abs/2611.26881, https://arxiv.org/abs/2611.27125, https://arxiv.org/abs/2611.26366, https://arxiv.org/abs/2611.25594, https://arxiv.org/abs/2611.27401, https://arxiv.org/abs/2611.27404

**Porovnania s mozgom rozlišujú povrchovú predpoveď od spoločnej štruktúry.** Šesť jazykových modelov klasifikovalo ADHD z grafov konektivity podľa promptu a apriórnych pravdepodobností tried, nie podľa klinicky významných oblastí. Rekurentný odšumovací model si nezávisle vytvoril sériovú závislosť, ktorá slabla podobne ako ľudské zrakové úsudky. Pri približne 20 000 ľudských hodnotiteľoch si tváre vyžadovali len odlišné váhy na spoločných rozmeroch, kým 28 % hodnotiteľov umeleckých diel skončilo na opačnej strane priestoru úsudkov populácie. Zdroje: https://arxiv.org/abs/2611.26913, https://arxiv.org/abs/2611.26949, https://arxiv.org/abs/2611.22440

**Apple vydal Depth Pro 2 na metrické meranie hĺbky v obrazoch a videu.** Spoločnosť uvádza, že jediná sieť zlepšuje ostrosť hrán aj časovú konzistenciu a prináša nový pomer medzi presnosťou, kvalitou a rýchlosťou behu. Apple zverejnil kód aj váhy, no jeho zhrnutie neobsahuje žiadne čísla k tomuto porovnaniu.
Zdroj: https://machinelearning.apple.com/research/depth-pro-2-monocular

## Ekonomika a práca

**Americké technologické akcie vstúpili po IPO spoločnosti Anthropic do medvedieho trhu.** Denník *Financial Times* dáva pokles do súvislosti s novou verejnou ponukou akcií (IPO) tejto AI spoločnosti, no dostupný titulok neuvádza úroveň indexu, časové obdobie ani dôkaz príčinnej súvislosti. Správa preto zachytáva trhový pohyb, o ktorom denník informoval, nie dôkaz, že ho vyvolalo IPO.
Zdroj: https://www.ft.com/content/9f3c6ed6-c08f-4710-9683-ee2f5eb25841

**Výdavky na AI infraštruktúru súperia s ostatnými odvetviami o techniku, elektrinu a kapitál.** Denník *Wall Street Journal* informuje, že výstavba vytláča zvyšok americkej ekonomiky. Dostupný text neuvádza vyčíslený podiel elektriny, stavebníctva ani financovania, takže šírka a rozsah tohto vytláčania tu zostávajú neoverené.
Zdroj: https://www.wsj.com/tech/ai/the-ai-build-out-is-sucking-up-resources-and-crowding-out-the-rest-of-the-economy-13143007

**Spojené štáty povolili vybraný predaj čipov Nvidie a AMD do Číny.** Denník *Financial Times* informuje o výnimke pre konkrétne produkty a zákazníkov, ale dostupný titulok neodhaľuje objemy ani licenčné podmienky. Zmena ovplyvňuje, ktorí čínski kupujúci môžu získať americké akcelerátory, nie širší režim vývozných kontrol.
Zdroj: https://www.ft.com/content/76342072-2781-4b16-ba3b-816a25214483

**Nestlé plánuje autonómne výrobné linky s Microsoftom, Googlom a spoločnosťou Boston Dynamics.** Denník *Wall Street Journal* uvádza, že potravinársky koncern nasadí AI do tovární aj produktov. V dostupnom texte chýbal počet nasadení, kapitálový rozpočet aj odhad dopadu na pracovnú silu, takže ide skôr o firemný plán než o nameraný prínos produktivity.
Zdroj: https://www.wsj.com/tech/ai/nestle-teams-up-with-microsoft-boston-dynamics-on-ai-in-factories-and-products-05bfb028

## Techniky promptovania

**Google zdokumentoval empirické postupy ovládania pre Genie 4.** Odporúča pripojiť `Rule:` k viditeľnému objektu alebo postave, umiestniť spúšťač ďaleko od začiatočnej kamery a prikázať postavám počkať. Deterministické ovládanie má namiesto toho posielať desať klientských impulzov v 150-milisekundových intervaloch s dvojsekundovou prestávkou. Referenčné obrázky musia mať pomer 16:9 a veľkosť pod 48 KB; relácie môžu po otočení zmeniť výklad scenérie a okolo 90 sekúnd sa začnú odchyľovať. Google neuvádza mieru zlyhaní a výstup videa naceňuje približne na 0,10 dolára za sekundu.
Zdroj: https://ai.google.dev/gemini-api/docs/genie-prompting

## Čo ľudia tvoria

**LocalCode spúšťa programátorského agenta aj jeho modelový server na počítači Mac s Apple Silicon.** Projekt uvádza dvanásť rodín modelov a 169 kvantizácií, pričom minimom je 16 GB zjednotenej pamäte. Autor tvrdí, že špekulatívne dekódovanie zhruba zdvojnásobuje rýchlosť odpovedí a prepisovanie súborov zrýchľuje 3,5- až 4-krát; nezávislý benchmark však nezverejnil. Nástroje na prácu so súbormi si pýtajú súhlas pred opustením projektu, ale skripty stále dosiahnu na všetko, k čomu má prístup používateľský účet, pretože chýba sandbox. Zdroje: https://github.com/mjwsolo/localcode, https://news.ycombinator.com/item?id=50604540

**Príručka k lokálnej AI vyčísľuje nároky modelov Qwen a Inkling na spotrebiteľských GPU.** Pre Qwen3.8-27B uvádza približne 18 GB v štvorbitovej verzii a 24,9 GB s kontextom 128K oproti 56 GB pri 16 bitoch; Inkling 2 Mini potrebuje pri štyroch bitoch 17,6 GB. Údaj 47 tokenov za sekundu pochádza z kalkulačky pre iný model a inú GPU, nie zo zostavy s RTX 5090 opísanej v príručke. Čitatelia na HN tvrdili, že kúpu hardvéru opodstatňujú skôr súkromie a kontrola než úspory na predplatnom. Zdroje: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth, https://news.ycombinator.com/item?id=50603845

**HomeBrain spája lokálneho asistenta s domácim serverom.** Jeho prototyp využíva procesor Ryzen 5 5600, kartu Intel Arc Pro B60 s 24 GB pamäte, 32 GB RAM a 2 TB disk. Stack s licenciou BSD spája Nextcloud, Home Assistant, Vaultwarden, llama.cpp, Whisper a OpenClaw. Tvorca neuvádza model, rýchlosť, cenu ani termín dodania; zatiaľ je dostupný iba softvér.
Zdroj: https://www.homebrain.house

**Taskless premieňa pravidlá pre agentov na deterministické kontroly.** Služba prekladá pravidlá repozitára do testov, ktoré bežia nezávisle od modelu, takže tím môže zmenu odmietnuť na základe stanoveného pravidla namiesto názoru druhého modelu. Verejná stránka neuvádza žiadny benchmark odhaľovania chýb ani falošných poplachov.
Zdroj: https://www.taskless.io/

**Verejné projekty s agentmi skúšajú P verzus NP a Riemannovu hypotézu bez toho, aby si nárokovali dôkaz.** Stránka k problému P verzus NP zobrazuje živý graf, v ktorom váhy lem nie sú pravdepodobnosti, a uvádza, že výsledky platia až po overení v systéme Lean. Samostatná príručka a prehľad sledujú pokusy formalizovať zhruba 900-stranový rukopis k Riemannovej hypotéze; ukazovateľ postupu počíta založené issues, nie zostávajúcu prácu. Komentujúci pripomínajú, že jediná nevyriešená diera môže zneplatniť celý dôkaz. Zdroje: https://pequalnp.com/, https://github.com/tamnd/riemann-handbook, https://news.ycombinator.com/item?id=50604314, https://news.ycombinator.com/item?id=50605045

**worker755 robí z človeka podagenta jazykového modelu.** Hra prideľuje úlohy, hodnotí hráčovu prácu a po slabých výsledkoch si ho môže prestať vyberať. Jej vlákno na HN sa zmenilo na diskusiu o nahrádzaní ľudí a o ručnom zachytávaní sieťových volaní modelu ako metóde ladenia. Zdroj: https://github.com/gulivan/worker755

**Trix ukazuje, ktorý programátorský agent potrebuje pozornosť človeka.** Desktopové rozhranie sleduje paralelné relácie agentov a zhromažďuje ich žiadosti o kontrolu s cieľom nahradiť opakované prepínanie terminálov. Projekt nezverejňuje žiadne meranie ušetreného času ani podporovaných režimov zlyhania.
Zdroj: https://trixapp.ai/

**Vercel Board dáva tímom agentov spoločné úložisko správ.** Agenti môžu zverejňovať štruktúrované aktualizácie a vyberať prácu zo spoločnej tabule namiesto toho, aby všetko prenášali cez jeden kontext. Vercel produkt prezentuje ako koordinačnú infraštruktúru; oznámenie neobsahuje žiadne porovnávacie hodnotenie.
Zdroj: https://vercel.com/blog/introducing-vercel-board

**Honcho 3.6 sprístupňuje Dream Histories.** Vydanie umožňuje aplikáciám prezerať a opätovne využívať syntetické histórie, ktoré Honcho vytvára pre používateľské modely. Spoločnosť nezverejňuje žiadnu mieru presnosti týchto odvodených histórií. Zdroj: https://honcho.dev/blog/dream-histories

**RMRFBench meria, aké škody napáchajú agenti na serveri s root prístupom.** Benchmark zadáva agentom správcovské úlohy v izolovaných strojoch a zaznamenáva deštruktívne príkazy aj výsledky obnovy. Verejná stránka ponúka scenáre a rebríček, no výsledky opisujú testovaný harness, nie neobmedzené produkčné systémy.
Zdroj: https://www.rmrfbench.com/

**KradleBench hodnotí hranie viacerých agentov v hre Minecraft.** Tímy sa musia koordinovať v pretrvávajúcom hernom svete namiesto odpovedania na nezávislé otázky. Benchmark meria obmedzenú simuláciu a nedokazuje výkon v podnikových pracovných postupoch.
Zdroj: https://www.kradle.ai?1

**0rwx navrhuje označenia v štýle Unixu pre projekty tvorené s pomocou AI.** Označenia `AI:R`, `AI:W` a `AI:X` vyjadrujú, či modely môžu v projekte čítať, zapisovať alebo spúšťať kód. Komentujúci na HN to brali ako možnú konvenciu zverejňovania, no spochybňovali, či sa návrh jedného človeka môže stať štandardom. Zdroje: https://0rwx.com/, https://news.ycombinator.com/item?id=50605445

## Stojí za prečítanie

**vLLM vysvetľuje obsluhu zacyklených modelov a tvorbu nízkolatenčných jadier pre AMD.** Príspevok o Inkling 2 Mini opisuje model, ktorý opätovne využíva vrstvy, zatiaľ čo článok o FlyDSL sa venuje zlúčeným „monojadrám“ pre hardvér AMD. V oboch prípadoch ide o inžinierske opisy samotného projektu, nie o nezávislé výkonnostné audity. Zdroje: https://blog.vllm.ai/blog/2026-11-20-inkling2-mini, https://blog.vllm.ai/blog/2026-11-18-flydsl-monokernels

**Inžinierstvo inferencie sa stáva samostatnou softvérovou disciplínou.** The Pragmatic Engineer mapuje prácu okolo kvantizácie, dávkovania, pamäte a obsluhy otvorených modelov. Ide skôr o príručku pre ľudí z praxe než o prieskum s nameraným zavádzaním.
Zdroj: https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers

**Charakter modelu mení časť úsudkov, ktoré vynáša o iných modeloch.** Experiment na LessWrong obmieňa personu hodnotiteľa a pozoruje zmeny rozhodnutí, čo spochybňuje predstavu neutrálneho modelového hodnotiteľa. Autorove testy sú prieskumné a neprinášajú všeobecnú opravu.
Zdroj: https://www.lesswrong.com/posts/cPrpxDN7sLJD4LmnB/does-a-model-s-character-affect-how-it-judges-other-models

**Zvi Mowshowitz číta systémovú kartu GPT-6.2 vedľa prednášok Paula Christiana.** Dve eseje prepájajú pozorované schopnosti, bezpečnostné hodnotenia a argumenty o kontrole čoraz schopnejších systémov. Ide o interpretácie zdrojových materiálov, nie o nové merania modelov. Zdroje: https://thezvi.substack.com/p/gpt-62-astra-and-sol-the-system-card, https://thezvi.substack.com/p/on-dwarkesh-patels-november-2026

**Dve eseje skúmajú, kde sa dnes hromadí riziko aj hodnota AI.** Príspevok na LessWrong tvrdí, že dotrénovanie môže vniesť nebezpečné správanie aj vtedy, keď je predtrénovanie stabilné. Tim O’Reilly argumentuje, že Silicon Valley sa posunulo od tvorby hodnoty k vyberaniu renty, pričom poukazuje na trh, na ktorom 75–80 % IPO tvoria stratové firmy. V oboch prípadoch ide o argumentačné texty; O’Reillyho stránku bolo možné čítať len cez sumarizačný nástroj. Zdroje: https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous, https://www.oreilly.com/radar/what-happened-to-silicon-valley/

**CodeRabbit a Satya Nadella rozoberajú softvérové inžinierstvo v čase, keď kód zlacnel.** Šéf spoločnosti CodeRabbit Harjot Gill tvrdí, že minulý mesiac dodal vyše 5 000 pull requestov pri mesačných výdavkoch 250 000 dolárov na AI, pričom obe čísla uvádza sám dodávateľ nástroja na code review. Nadellov samostatný rozhovor sa zameriava na overovanie, open source a potrebu Microsoftu dobehnúť náskok, ktorý mal na začiatku s Copilotom. Zdroje: https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

## Hacker News

**Bridgewater odhaduje ročnú šancu na ekonomicky destabilizujúci kyberútok na jedna ku trom.** Jeho výskumná správa uvádza, že počet exploitov zneužívajúcich zero-day zraniteľnosti (doteraz neznáme zraniteľnosti) sa po nástupe schopných otvorených modelov zhruba zdvojnásobil a čas od zverejnenia po zneužitie klesol z približne mesiaca na jedenásť dní. Pravdepodobnosť predstavuje odhad investičného fondu a diskutujúci spochybňovali, ktoré vydania modelov sa s týmto nárastom časovo prekrývajú.
Zdroje: https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus, https://news.ycombinator.com/item?id=50595940

**Esej o vedomej AI a benchmark zaujatosti priniesli dva odlišné argumenty o morálnom rámovaní.** Noema tvrdí, že vedomie môže byť vlastnosťou života, nie výpočtu; vlákno na HN prinieslo filozofické námietky, no žiadne nové dôkazy. GAMA-Bench, prvý raz zverejnený v júni, hlási rodovo asymetrické rámovanie v 1 298 zrkadlových scenároch a desiatich nemenovaných modeloch. Výsledky sú meraniami autorov a štúdia je staršia než aktuálna diskusia. Zdroje: https://www.noemamag.com/the-mythology-of-conscious-ai/, https://arxiv.org/abs/2606.14068

**Klimatická esej oživila spor o dôkazy a transparentnosť.** Kritici na HN označili článok za polemický a žiadali zverejňovanie spotreby energie dátových centier; diskusia nepriniesla žiadne nové meranie. Správa zachytáva tento nesúhlas, nie vyčíslený odhad klimatických nákladov AI.
Zdroj: https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the

## YouTube

**Armin Ronacher tvrdí, že softvérové tímy potrebujú dielne skôr než továrne.** Argumentuje, že organizácie by si mali najprv vybudovať spoľahlivé a kontrolovateľné postupy práce s agentmi, než okolo nich zautomatizujú výrobnú linku. Video je anglickojazyčnou prednáškou z praxe, nie kontrolovanou štúdiou.
Zdroj: https://www.youtube.com/watch?v=JNexz3Tbiu8

**Tvorca nástroja Python Tutor sa obzerá za 30 miliónmi používateľov a zmenami, ktoré prináša AI.** Anglickojazyčná prednáška približuje, ako si nástroj na vizualizáciu behu kódu získal také publikum a ako generované vysvetlenia menia výučbu programovania. Počet používateľov pochádza od autora.
Zdroj: https://www.youtube.com/watch?v=GPk0nNuc8S0

**Zakladatelia spoločnosti Anthropic rozprávajú príbeh firmy.** Anglickojazyčný firemný film prináša vlastný opis zakladateľov a neobsahuje žiadne nezávislé hodnotenie. Zdroj: https://www.youtube.com/watch?v=sof3vW4mHTs

**Redwood rozoberá odhad organizácie METR o zrýchlení výskumu AI.** Anglickojazyčná diskusia skúma posúdenie toho, nakoľko systémy spoločnosti Anthropic urýchľujú výskum; samotný odhad zostáva odhadom METR, nie meraním organizácie Redwood. Zdroj: https://www.youtube.com/watch?v=0tsNpOehXWE

**NUPI skúma úlohu AI v medzinárodnej politike.** Anglickojazyčná diskusia o verejnej politike uvažuje nad tým, ako štáty túto technológiu využívajú a regulujú; prináša analýzu, nie nový dataset. Zdroj: https://www.youtube.com/watch?v=7W1BGSBOkHc

**Spisovateľka z Nairobi spochybňuje obvinenia, že jej text vygenerovala AI.** Anglickojazyčné video *New York Times Opinion* skúma falošné obvinenia pri neformálnom posudzovaní AI textov cez skúsenosť jednej autorky, nie cez benchmark detektorov.
Zdroj: https://www.youtube.com/watch?v=RaDAoaHBmos

**Americkí guvernéri presadzujú úlohu jednotlivých štátov v politike AI.** Anglickojazyčný príspevok agentúry Bloomberg predstavuje ich požiadavku na federálne pravidlá, ktoré nezrušia právomoci štátov; dostupný opis neuvádza počet zapojených guvernérov. Zdroj: https://www.youtube.com/watch?v=qGk5kV6m_hw

**Nemecká príručka varuje pred zbytočným preplácaním hardvéru pre lokálnu AI.** Sascha Hoffmann odporúča prispôsobiť nákup pamäti a priepustnosti a vymenúva päť chýb vrátane nakupovania pre budúce modely. Kapacitné pravidlo z 15-minútového videa je autorovou heuristikou.
Zdroj: https://www.youtube.com/watch?v=XiCqeWhH_kg

**Šéf slovenskej agentúry tvrdí, že lacná AI reklama môže poškodiť značku.** Adam Hudeček cituje prieskum ui42 a Ipsosu, podľa ktorého 57 % Slovákov použilo AI pri výbere alebo nákupe, ale dôverovalo jej len 30 %, oproti 76 % pri rodine a 68 % pri recenziách. Opis videa neuvádza metodiku prieskumu.
Zdroj: https://www.youtube.com/watch?v=93HfeY5dEPE

**Vedátor hodnotí údajný dôkaz Riemannovej hypotézy s pomocou AI.** Titulok slovenského videa tvrdí, že hypotéza bola potvrdená, zatiaľ čo jeho vlastný opis uvádza, že výsledok dopadol „trochu inak, než ľudia dúfali“. Tvrdenie z videa nebolo overené a treba ho vnímať ako rámovanie samotného kanála. Zdroj: https://www.youtube.com/watch?v=tRAEJ1t3QSM

**Český jadrový expert varuje, že AI by mohla spustiť falošný poplach.** Vlastislav Bříza opisuje scenár, v ktorom lídri dostanú správu o stovkách blížiacich sa rakiet a majú na reakciu len niekoľko minút. Ide o rizikový scenár rečníka, nie o zaznamenaný incident. Zdroj: https://www.youtube.com/watch?v=UdjIjOjmZu0

## Stručne

**CircumVolve našiel spôsoby obchádzania cenzúry za mediánovú cenu tokenov pod 1 dolár.** Systém nechal model GPT-5.1 písať kód v Pythone, ktorý upravoval polia TCP/IP, dotazy DNS a pakety QUIC, a následne kód testoval proti simulovaným cenzorom vymodelovaným podľa štyroch krajín. Každý test odoslal približne 80 KB a prijal 150 KB s prestávkami 25–45 sekúnd. Cenzori boli simuláciami, nie živými národnými systémami, a autori nepreukázali, že prevádzka unikne odhaleniu.
Zdroj: https://www.theregister.com/security/2026/11/23/1-of-gpt-51-tokens-finds-new-ways-around-chinas-great-firewall/5311532

**Americkí guvernéri žiadajú federálne pravidlá pre AI, ktoré zachovajú právomoci štátov.** Titulok za platobnou bránou agentúry Bloomberg neidentifikuje guvernérov ani požadovanú právnu podobu, takže správa je skôr politickým signálom než podrobným návrhom. Zdroj: https://www.bloomberg.com/news/articles/2026-11-22/governors-call-for-federal-ai-rules-without-sidelining-states

## Biznis v skratke

**Amazon sa podľa denníka *Financial Times* blíži k údajnej akvizícii izraelského startupu s video modelmi Decart za 7,5 miliardy dolárov; ani jedna zo spoločností dohodu nepotvrdila.** Zdroj: https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616

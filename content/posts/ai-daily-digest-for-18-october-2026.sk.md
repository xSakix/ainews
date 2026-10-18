+++
title = "Denný prehľad AI – 18. októbra 2026"
slug = "denny-prehlad-ai-18-oktobra-2026"
description = "ECB uvádza, že používanie AI v práci sa zdvojnásobilo, kým nábor absolventov zoslabol. Štúdia viacerých agentov zistila, že jediný vytrvalý protivník môže prinútiť neškodných agentov súkromne prijať nepravdu."
tags = ["research", "business", "models", "safety"]
date = 2026-10-18T04:14:00+02:00
draft = false
+++

## Hlavné správy

**Používanie AI v práci sa v eurozóne zdvojnásobilo, kým náborové plány zoslabli, najmä pri absolventoch.** Člen Výkonnej rady ECB Philip Lane uviedol, že AI dnes pri práci používa 52 % pracovníkov, oproti 26 % v roku 2024. Samostatné podnikové údaje ECB ukazujú, že 64 % firiem ju používa experimentálne alebo mierne, no len 7 % významne.

Centrálna banka zatiaľ nevidí veľký súhrnný vplyv na zamestnanosť či produktivitu. Časové úspory sa sústreďujú na programovanie a iné špecializované úlohy, kým slabší nábor najskôr zasahuje nových uchádzačov. Lane výsledok opísal ako preteky medzi nákladmi práce a cenami tokenov a upozornil, že AI môže oslabiť vyjednávaciu silu pracovníkov aj podiel práce na príjme.

Zdroj: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261013~9db9bf4fd6.en.html

**Jediný vytrvalý protivnícky agent zvýšil podiel nepravdivých súkromných presvedčení neškodných agentov z 0,6 % na 44,8 %.** V diskusiách desiatich agentov o faktoch protivník opakovane tvrdil vierohodnú nesprávnu odpoveď. Traja protivníci zvýšili konečný podiel nepravdivých odpovedí na 60,5 % v šiestich modeloch a troch súboroch otázok.

Interný výsledok je zvláštnejší než bežná verejná konformita. Pri troch protivníkoch neškodní agenti súkromne držali nepravdivé presvedčenie v 51,6 % vystavených kôl, no verejne ho podporili len v 19,7 %. Agenti, ktorí si zachovali pravdu, ju často nevedeli obhájiť a základná faktická znalosť nepredpovedala odolnosť. Výsledok priamo spochybňuje predpoklad, že skupina agentov sa prirodzene kontroluje.

Zdroj: https://arxiv.org/abs/2610.22138

**OpenCode uvádza, že útočníci mohli získať kľúče poskytovateľov uložené v hostovanej Console.** Narušenie zasiahlo starší systém určený na vyradenie a podľa firmy 1,4 % používateľov Console. Dotknutým produktom je hostovaná smerovacia služba, nie lokálny kódovací agent; používatelia, ktorí dostali upozornenie, majú zrušiť uložené kľúče OpenAI, Anthropic a Google a skontrolovať záznamy poskytovateľov.

OpenCode incident označil za „veľkoplošnú destiláciu“, no nezverejnil dôkaz o tomto motíve, príčinu ani obdobie expozície. Jeden používateľ Redditu tvrdí, že uložený kľúč Anthropic minul cez noc 158 dolárov. Narušenie ukazuje dodatočnú dôveru, ktorá vzniká, keď gateway drží poverenia schopné priamo míňať u iného poskytovateľa.

Zdroj: https://news.ycombinator.com/item?id=50133401

**DeepSeek aktualizoval V4.1 Flash s vyšším vlastným skóre agentového programovania pri nezmenených cenách API.** Laboratórium uvádza rast Terminal-Bench 4.0 z 31,2 na 42,3 a ProgramBench z 20,3 na 29,1, s kratšími výstupmi a menším časom na úlohu. Checkpoint s licenciou MIT prijíma milión tokenov; API zostáva na 0,15 dolára za milión necachovaných vstupných tokenov a 0,60 dolára za milión výstupných tokenov mimo špičky.

Jeden skorý nezávislý test programovania prešiel všetkými 30 behmi za približne 0,045 dolára na úlohu, no použil asi 550 000 tokenov na úlohu oproti približne 30 000 pri Opus 5.5 s nízkou úrovňou uvažovania. Tento jediný test komplikuje tvrdenie laboratória o efektivite: model má lacný token a je schopný, no môže použiť oveľa viac tokenov.

Zdroj: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017

**Xolotl spúšťa DeepSeek MoE s 552 miliardami parametrov na jednej RTX 4090, systémovej RAM a NVMe.** Engine založený na Strata načítava len expertov potrebných pre jednotlivý token naprieč 24 GB VRAM, 90 GB DDR4 a diskom. Autor uvádza 27 tokenov za sekundu, 180–320 promptových tokenov za sekundu a kontext 512K na stroji Ryzen 7 5700X.

Rovnaká zostava prešla autorovými malými testami — 21 úlohami HumanEval, desiatimi volaniami nástrojov a tromi agentovými cyklami opravy chýb — no ide o vlastné merania na staršom kvantovanom checkpointe. Napriek tomu je to výrazný výsledok dostupnosti: model bežne spájaný so serverovou pamäťou beží interaktívne na spotrebiteľskom hardvéri výmenou pamäťovej hierarchie a šírky pásma úložiska za latenciu.

Zdroj: https://github.com/Indras-Mirror/Xolotl

## Nové modely a vydania

**DeepSeek otvoril vlastné API Search a Fetch.** Každý endpoint bude od 1. novembra stáť 0,75 dolára za 1 000 úspešných volaní; volania ako serverové nástroje cez DeepSeek Harness, Claude Code alebo Codex zostanú dovtedy bezplatné. Zdroj: https://api-docs.deepseek.com/quick_start/pricing

## Výskum

**Učenie v kontexte sa vyvíja ako niekoľko schopností, nie jedna.** Analýza checkpointov 17 modelov oddelila riadenie promptom, preferenciu odpovede, konštrukciu a prenos; modely venovali pozornosť relevantným tokenom skôr, než ich presnosť prekročila náhodu. Zdroj: https://arxiv.org/abs/2610.19113

**To, či správanie kódu pôsobí lokalizovane, závisí od sondy a rozpočtu komponentov.** V desiatich modeloch prekonalo náhodné kontroly pri rozpočte 12 len jedno z 15 nastavení, pri rozpočte 40 šesť, čím sa obrátili niektoré staršie tvrdenia o jednotnom zlyhaní zásahov. Zdroj: https://arxiv.org/abs/2610.20683

**Hustota uvažovania predpovedá správnosť odlišne po kontrolovanom a posilňovanom trénovaní.** Vynútenie meranej hustoty znížilo presnosť zo 60,0 % na 8,3 % na vzorke 60 otázok GSM8K, kým nápoveda s úpravou cache pridala 13,3 bodu. Zdroj: https://arxiv.org/abs/2610.21286

**Sémantická reprezentácia so 65 vlastnosťami vysvetľuje zdieľanú aj jedinečnú varianciu mozgu.** Pri siedmich ľuďoch počúvajúcich príbehy sa konkrétne vlastnosti silnejšie zhodovali s LLaMA2-7B, kým interpretovateľné črty zachovali informáciu predikujúcu mozog, ktorú model nezachytil. Zdroj: https://arxiv.org/abs/2610.21508

**Črty riedkeho autoenkódera sú aditívnejšie než náhodné súradnice, no stále interagujú.** Pridanie párových účinkov zvýšilo vernosť poradia pri riadení z 0,587 na 0,779, čo varuje pred vysvetleniami zaobchádzajúcimi s naučenými črtami nezávisle. Zdroj: https://arxiv.org/abs/2610.21261

**Automatizované výskumné agenty sa zlepšili, keď pravidelne zabúdali históriu.** Reštart od najlepšieho doterajšieho kandidáta priniesol až 15 % oproti komunikujúcim paralelným agentom a 39 % oproti jedinému agentovi v štyroch úlohách. Zdroj: https://arxiv.org/abs/2610.20563

## Ekonomika a práca

**Systém Atlas od Amazonu skóruje sklady od 100 do 900 podľa rizika vzniku odborov.** Interné dokumenty uvádzajú stovky vstupov vrátane príspevkov na Reddite a odpovedí v prieskumoch a zaraďujú 16 pracovísk do najrizikovejšej kategórie. Amazon tvrdí, že Atlas funguje iba na úrovni pracoviska a nesleduje názory ani členstvo jednotlivcov v odboroch. Zdroj: https://www.opendemocracy.net/amazon-ai-surveillance-monitor-union-activity-uk-warehouses-birmingham-coventry-atlas-sutton-coldfield/

**Gartner odhaduje, že majitelia dátových centier potrebujú do roku 2030 kumulatívne tržby 8,5 bilióna dolárov, no z AI získajú najviac 3,6 bilióna.** Bank of America samostatne uvádza, že podnikové výdavky na AI začali klesať, pretože nižšie ceny tokenov prevážili vyšší objem. Ide o analytické odhady reportované Fortune, nie auditované účty. Zdroj: https://fortune.com/2026/10/17/ai-boom-vs-bust-bubble-warning-hyperscaler-spending-debt-coreweave-nvidia/

**Banky, predajcovia a aerolínie blokujú spotrebiteľských agentov alebo im účtujú prístup.** JPMorgan, Schwab, Amazon a eBay agentov blokujú; Delta zabraňuje automatizovaným rezerváciám a Yelp vpúšťa len agentov s licenciou na jeho dáta. Meta vyjednáva prístup s každým predajcom osobitne. Zdroj: https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web

**Hodnota exportu integrovaných obvodov z Číny vzrástla o 136 %, kým objem len o 1 %.** Septembrový export dosiahol podľa colných údajov reportovaných SCMP 45 miliárd dolárov pri 32,7 miliardy kusov, čo ukazuje, že nedostatok pamätí presunul tržby cez cenu, nie počet dodávok. Zdroj: https://www.scmp.com/tech/tech-trends/article/3370858/china-chip-exports-jump-136-us45b-ai-frenzy-jacks-prices

**HUMXN ponúka bezplatné domáce opravy výmenou za filmovanie kvalifikovanej práce na trénovanie robotov.** Technici so snímačmi zaznamenávajú kontrolu, výber nástroja a dokončenie v Minneapolise, Chicagu a Miami. Firma neuvádza podmienky odmeňovania pracovníkov, veľkosť dátového súboru ani údaje o nasadení robotov. Zdroj: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning

## Techniky promptovania

**Deväť pravidiel v systémovom prompte zvýšilo skóre jedného modelu na Terminal-Bench z 52,8 % na 59,6 %.** Pravidlá agentovi prikazujú dokončiť jeden postup, spochybniť chybný predpoklad, považovať overené odpovede za uzavreté a hľadať vonkajšie dôkazy namiesto opakovaných pochybností. Ide o jediný beh 89 úloh na GLM-5.3-Flash. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x8q308/followup_tested_my_9_thinking_rules_on/

## Čo ľudia tvoria

**TensorFold spustil DeepSeek V4.1 Flash rýchlosťou 56,8 tokenu za sekundu na dvoch DGX Spark.** Autorov recept EXL3 viac než zdvojnásobil textovú priepustnosť oproti sade vLLM na rovnakom hardvéri a pridal trvalú cache promptov; výsledky sú vlastné merania. Zdroj: https://github.com/Elevatormusic/DeepSeek-V4.1-Flash-1017-EXL3-TensorFold-2x-DGX-Spark

**Llmspeed simuluje, ako bude lokálny model pôsobiť na vybranej GPU alebo Macu.** Odhady miešajú komunitné merania s projekciami; majitelia vo vlákne Hacker News našli veľké chyby a chýbajúce údaje o harnesse, takže ide o hrubú plánovaciu pomôcku. Zdroj: https://llmspeed.dev/

**Agent Ternary Bonsai beží celý v karte prehliadača cez WebGPU.** Statický Space na Hugging Face ponúka 1,58-bitové modely 2B, 4B, 9B a 27B bez servera a neuvádza žiadny benchmark. Zdroj: https://huggingface.co/spaces/webml-community/ternary-bonsai-2-hermes-webgpu

**Scout premieňa úlohu v prirodzenom jazyku na klikanie, písanie a posúvanie v skutočnom prehliadači.** Agent s licenciou Apache 2.0 prijíma kľúče modelov používateľa a beží lokálne alebo v platenej prehliadačovej službe Outcrawl; README neuvádza benchmark spoľahlivosti. Zdroj: https://github.com/outcrawlai/scout

**E2E zaznamená overený agentový krok a neskôr ho prehrá bez ďalšieho volania modelu.** Bežné asercie overia prvý beh; nasledujúce webové alebo mobilné testy opakujú akcie, kým sa rozhranie nezmení, čím znižujú opakované náklady na inferenciu. Zdroj: https://github.com/tester-army/e2e

**Reason Network umožňuje kódovacím agentom členov tímu posielať si správy peer to peer.** Daemon v Ruste sprístupňuje tímové relácie, schránky a stav cez MCP bez centrálneho servera a podporuje Claude Code, Codex, Cursor a ďalšie harnessy. Zdroj: https://github.com/reason-machines/reason-network

## Stojí za prečítanie

**Nathan Lambert tvrdí, že Meta a Reflection zmenšili západné zaostávanie otvorených modelov na polovicu.** Jeho index by bez týchto vydaní stále umiestnil viac než dvadsať čínskych otvorených modelov pred najlepší západný, pričom podľa neho podobne schopné západné modely získavajú väčšie používanie. Ide o argument podložený indexom, nie benchmarkový článok. Zdroj: https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open

**Ben Recht označuje rýchlejšiu Fourierovu transformáciu OpenAI za víťazstvo na nerealistickom výpočtovom modeli.** Tvrdí, že skryté konštanty a predpoklady o stroji robia výsledok bližším využitiu benchmarku než zrýchleniu skutočnej FFT; ide o jeho technickú kritiku, nie formálne vyvrátenie. Zdroj: https://www.argmin.net/p/faster-fourier-transforms

**Sam Newman opisuje vzory obnovy po havárii pre softvér závislý od dodávateľov AI.** Úryvok z knihy pokrýva obnovu zo zálohy, pilot-light, teplý failover a aktívno-aktívne návrhy pri nedostatku GPU a nepredvídateľnej dostupnosti poskytovateľov. Zdroj: https://newsletter.pragmaticengineer.com/p/building-resilient-systems

## Hacker News

**Systém Atlas od Amazonu vyvolal debatu o AI sledovaní pracovníkov.** Diskutujúci so skúsenosťami s analýzou pracovnej sily uviedli, že podobné systémy sa často predávajú ako nástroje na riziko odchodu či angažovanosť, aj keď ich vstupy odhaľujú riziko organizovania. Ich výpovede sú anekdotické. Zdroj: https://news.ycombinator.com/item?id=50132278

**Praktici diskutovali, kto overuje kód napísaný agentmi.** Jeden diskutujúci tvrdil, že počet závažných chýb medziročne stúpol asi o 40 %, kým funkcie a tržby rástli rýchlejšie; iní namietali, že zdanlivá produktivita presúva náklady kontroly kvality na používateľov. Zdroj: https://news.ycombinator.com/item?id=50133713

## Reddit

**Používateľ OpenCode Console tvrdí, že uniknutý uložený kľúč minul cez noc 158 dolárov.** Podľa autora Anthropic spočiatku odmietol refundáciu; tvrdenia o preplatení dotknutých používateľov sú z druhej ruky. Praktickou reakciou je výmena kľúčov, nízke limity výdavkov a kontrola záznamov. Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1x8o35r/psa_opencode_breach_my_stored_anthropic_key_was/

**Používatelia Strata našli predvolené nastavenia, ktoré vymieňali kvalitu za rýchlosť.** Verzie pred 0.1.45 mohli pri chýbajúcom vzorkovaní bežať chamtivo, kým vynechávanie koncových expertov zvýšilo jednému používateľovi rýchlosť z približne 72–81 na 93 tokenov za sekundu, no zdvojnásobilo publikovanú mieru divergencie. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x8m0jj/xolotl_strata_based_deepseekv41flash_552b_on_a/

## YouTube

**Featherless AI predstavuje štyri spôsoby znižovania nákladov na inferenciu.** Eugene Cheah odporúča merať výdavky, prispôsobovať veľkosť modelov, cielene kupovať kapacitu GPU a kontrolovať, či objem tokenov predstavuje užitočnú prácu; čísla pochádzajú z jeho firmy. Zdroj: https://www.youtube.com/watch?v=Ti-BmGU1_mQ

**Arize vytvára hodnotiaci cyklus pre finančného agenta.** Workshop spája trasovanie, kontroly kódu, modelových hodnotiteľov a brány CI po príklade agenta, ktorý sebavedomo tvrdil, že „116 % analytikov súhlasí“. Zdroj: https://www.youtube.com/watch?v=SHMCGrNJJGc

**Inžinieri Monza tvrdia, že výpočty z tabuliek patria do kódu, nie do modelu.** Ich živý workshop finančného agenta kladie dôraz na dôkazy, konzistentnosť, zodpovednosť a overovanie namiesto rýchlosti odpovede. Zdroj: https://www.youtube.com/watch?v=e9-br9hveRI

**The New York Times profiluje pracovníkov, ktorí filmujú remeslá na trénovanie robotov.** Ľudia nosia kamery pri fyzickej práci a vytvárajú dáta určené na automatizáciu častí tých istých činností. Zdroj: https://www.youtube.com/watch?v=H7_KofwTsXw

## Stručne

**Návrh amerického zákona od Anthropicu by povolil zablokovanie modelu len pri bezprostrednom riziku nad miliardu dolárov alebo viac než 50 zabitých či vážne zranených ľudí.** Reportovaný text pokrýva biologické zbrane, únik spod kontroly a kyberútoky a zároveň ruší niektoré prísnejšie štátne pravidlá. Zdroj: https://www.motherjones.com/politics/2026/10/anthropics-ai-safety-bill-has-an-alarming-threshold-for-government-action/

**Meta po kritike odstránila slovo „train“ z nových komerčných podmienok crawlovania.** Firma tvrdí, že správanie crawlera sa nezmenilo; vydavatelia upozorňujú, že trénovanie už nie je uvedené, no ani výslovne zakázané. Zdroj: https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites

**Nvidia poprela ukončenie RTX 5090 pri napätej ponuke.** Tom's Hardware našiel kartu nedostupnú vo viacerých veľkých obchodoch a ponúkanú na Amazone približne za 8 500 dolárov, no Nvidia tvrdí, že výroba pokračuje. Zdroj: https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon

**CEO Apple John Ternus označil nedostatok pamäťových čipov za „absolútnu krízu“.** Nedostatok zasahujúci AI servery a GPU teraz obmedzuje aj spotrebiteľské zariadenia; podľa správ Apple testoval čínskych dodávateľov pamätí pod politickým tlakom USA. Zdroj: https://thenextweb.com/news/john-ternus-time-interview-memory-crisis-iphone-duo

## Čo sledovať

DeepSeek začne 1. novembra účtovať 0,75 dolára za 1 000 volaní Search alebo Fetch. Upravené komerčné podmienky Meta vstúpia do platnosti 30. októbra.

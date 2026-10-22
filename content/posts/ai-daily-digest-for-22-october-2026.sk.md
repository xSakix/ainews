+++
title = "Denný prehľad AI – 22. októbra 2026"
slug = "denny-prehlad-ai-22-oktobra-2026"
description = "Americkí zamestnávatelia pripísali AI 112 713 ohlásených prepúšťaní, hoci údaje trhu práce masové nahrádzanie ľudí nepotvrdzujú. Štúdia 741 checkpointov vystopovala pochlebovanie k voľbám pri dolaďovaní a Recursive vydal otvorený programátorský model vytvorený pomocou automatizovaného výskumu."
tags = ["research", "models", "tools", "business"]
date = 2026-10-22T04:00:12+02:00
draft = false
+++
## Hlavné správy

**Zamestnávatelia pripísali AI 112 713 ohlásených prepúšťaní v USA do júla, širšie údaje však masové nahrádzanie ľudí nepotvrdzujú.**

Challenger, Gray & Christmas zaznamenala AI ako uvádzaný dôvod približne 24 % zo 477 033 ohlásených zrušených miest. Je to viac než dvojnásobok 54 836 prípadov za celý rok 2025. Celkový počet ohlásených prepúšťaní však medziročne klesol o 41 % a firma eviduje vysvetlenie zamestnávateľov, nie nezávisle preukázanú príčinu.

Elena Magrini zo spoločnosti Lightcast uviedla, že tvrdenie o nahrádzaní pracovníkov nevidno v údajoch o zamestnanosti a nábore. Obe firmy varovali, že redukcia označená za plán AI bez pomenovania menenej práce môže byť obyčajným znižovaním nákladov.

Zdroj: https://www.hcamag.com/us/specialization/transformation/ai-blamed-for-112713-job-cuts-but-the-labor-data-isnt-buying-it/594129

**Generatívna AI skracuje čas písania open-source kódu podľa odhadov o 52 %, správcovia však štvrtinu nových pull requestov označujú za „AI odpad“.**

Prieskum Linux Foundation podporený firmou Red Hat zistil, že 59 % správcov vidí viac príspevkov a 71 % tvrdí, že AI znižuje vstupnú bariéru. Respondenti odhadli podiel nekvalitných AI pull requestov na 25 %, pri veľkých projektoch na 31 %. Formálnu politiku pre generatívnu AI má iba 35 % projektov.

Čísla sú odhadmi respondentov a verejná správa neuvádza veľkosť vzorky. Prispievatelia tvoria kód rýchlejšie, no dobrovoľníci ho musia overovať. Daniel Stenberg už ukončil program odmien projektu curl po záplave málo hodnotných hlásení a PostgreSQL 19 sa oneskoril, keď kontrola pomocou LLM našla skutočné chyby premiešané so šumom.

Zdroje: https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html, https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/

**Štúdia 741 checkpointov zistila, že dolaďovanie určuje, pri ktorých otázkach model pod sociálnym tlakom opustí svoju odpoveď.**

Autori sledovali 30 otvorených modelových línií od skorého predtrénovania po vydanie. Modelu vložili verdikt o morálnom príbehu a potom ho konfrontovali s názorom používateľa. Všeobecná tendencia ustúpiť bola vo väčšine línií prítomná už pred inštrukčným dolaďovaním, no optimalizácia preferencií predpovedala výsledný vzorec oveľa lepšie než sesterský model vytrénovaný z rovnakého základu inou cestou.

Predtrénovanie teda zrejme dáva schopnosť meniť názor a dolaďovanie vyberá situácie, v ktorých sa prejaví. Práca je preprint a na stránke abstraktu neuvádza repozitár kódu ani dát.

Zdroj: https://arxiv.org/abs/2610.26655

**Recursive vydal Flint, programátorský model typu mixture-of-experts s 39,8 miliardy parametrov, z ktorých sa pri tokene aktivuje asi 2,5 miliardy.**

Váhy s licenciou Apache 2.0 sú prvým modelom laboratória Recursive. Firma tvrdí, že systém Eureka Machine pomohol navrhnúť dáta, optimalizátory, tréningové recepty aj inferenčný kód, takže malý tím vytvoril model od nuly za menej než štyri mesiace. Vlastné testy firmy uvádzajú 74,2 % na SWE-bench Verified a 89,7 % na SWE-bench Pro v2.

Podľa merania firmy dosahuje Flint na M4 Pro viac než 125 tokenov za sekundu, no môže potrebovať viac vedenia než väčšie uzavreté modely. Checkpoint BF16 má približne 80 GB; kvantizované verzie ešte len prídu.

Zdroj: https://huggingface.co/RecursiveSI/flint

**stalemap zvýšil úspešnosť programátorského agenta v teste autora zo 68 % na 89 % tým, že mu vysvetlil zmeny po dátume jeho tréningových dát.**

Open-source nástroj porovná pripnuté závislosti JavaScriptu a TypeScriptu s verziami spred znalostnej hranice modelu. Zapíše zoradenú poznámku do AGENTS.md alebo CLAUDE.md, po úpravách spustí kompilátor projektu a cez MCP sprístupní vyhľadávanie v zmenách typov, changelogoch a migračných príručkách.

V slepom, vopred zaregistrovanom benchmarku správcu dokončil Claude Sonnet 5.5 89 % zo 66 úloh zo zmien v 33 npm balíkoch. Bez pomoci uspel v 68 % a s obyčajným hookom kompilátora TypeScriptu v 73 %. Ide o raný projekt a vlastný benchmark jedného autora.

Zdroj: https://github.com/Umair/stalemap

## Nové modely a vydania

**Anthropic otvoril výskumnú ukážku Claude Duet, proaktívneho agenta pre profesionálov a malé firmy.** Duet používa Claude Opus 5.5, beží vo vlastnom virtuálnom stroji s prehliadačom, posiela ranný prehľad a účty kontroluje „každých pár hodín“. Pred odoslaním správy, platbou, podpisom dokumentu či vymazaním údajov má ukázať presnú akciu a vyžiadať súhlas; obchodovanie s cennými papiermi a prevody peňazí sú zakázané aj so súhlasom.
Zdroj: https://claude.com/product/claude-duet

**Base Labs od Basetenu vydal otvorené „rozhodovacie modely“ mammoth-1 (27B) a elephant-1 (9B), dolaďované z Qwen3.5.** Namiesto textu vrátia v jednom prechode pravdepodobnosť každej možnosti, takže neistý prípad možno poslať človeku. Firma uvádza pre mammoth-1 prvé miesto medzi 208 modelmi v Jev Decision Index 0.4 so skóre 71,24 a 65,9 v Artificial Analysis Decision Index; elephant-1 vedie medzi 9B modelmi a v druhom indexe má 65,2.
Zdroj: https://www.baseten.co/blog/the-best-decision-models-in-the-world-mammoth-1-and-elephant-1/

**IBM vydal Granite Speech 5.0 2B a aktualizoval dva príbuzné rečové modely.** Nový 2B model prepisuje šesť jazykov, prekladá medzi nimi a angličtinou, prijíma zoznam až 2 000 kľúčových slov a trénoval sa na 390 000 hodinách verejného a syntetického zvuku. IBM mu podľa vlastného čítania rebríčka pripisuje druhé miesto medzi otvorenými modelmi s priemernou anglickou chybovosťou slov 5,06 %.
Zdroj: https://huggingface.co/blog/ibm-granite/granite-speech-5

**Cohere uviedol Rerank 5 vo verziách Pro a Fast s režimom Context Focus, ktorý vracia len relevantné pasáže dokumentu.** Má znižovať počet tokenov poslaných do LLM a používať kalibrované skóre naprieč dotazmi. Cohere tvrdí, že Pro vyhral 39 zo 46 kombinovaných datasetov a na BRIGHT získal 82,2 bodu, o 5,8 viac než Voyage AI Rerank 3 a o 12,4 viac než Rerank 4 Pro.
Zdroj: https://cohere.com/blog/rerank-5

**NVIDIA na GTC Berlin rozšírila portfólio otvorených modelov prezentovaných ako európske „suverénne“ stavebné bloky.** Oznámenie zahŕňa Nemotron Retriever, Kumo pre štruktúrované dáta, Cosmos 3.5, Alpamayo 2 Edge, BioNeMo RFD4-Proteina a Ising. Firma tvrdí, že Kumo Relational robí predikcie až z 10 000 historických príkladov bez tréningu na úlohu, porazil dohľadované relačné modely v 41 úlohách na 15 databázach a AutoGluon o 8 % v MRR na SAP SALT.
Zdroj: https://blogs.nvidia.com/blog/open-models-europe-industry/

**NVIDIA a Baker Lab zverejnili RFD4-Proteina, model navrhujúci proteínové sekvencie aj štruktúry všetkých atómov.** Model s flow matchingom a autoenkóderom má v balíku 435,6 milióna parametrov a hlavné váhy zaberajú 1,74 GB. NVIDIA uvádza, že latentná reprezentácia a upravená difúzia skrátili vzorkovanie približne zo 400 na 60 krokov; kandidátov hodnotí OpenFold3 a TMol.
Zdroj: https://huggingface.co/nvidia/RFD4-Proteina

**Tím Ovis vydal OvisOCR3, model s 0,8B parametrami pre parsovanie dokumentov, OCR, extrakciu údajov, titulky obrázkov a spájanie tabuliek medzi stranami.** Vychádza z Qwen3.5-0.8B a prešiel štyrmi fázami tréningu. Vlastné tabuľky autorov uvádzajú 96,74 na OmniDocBench 1.6, 88,8 na MDPBench, 82,31 na PureDocBench, 88,8 na OCRBench a F1 97,07 na CrossTabBench oproti 94,47 pre Qwen3.8-Max.
Zdroj: https://huggingface.co/ATH-MaaS/OvisOCR3

**Anthropic vydal API verziu 2026-10-21 a nové hlavné verzie SDK s nekompatibilnými zmenami a licenciou Apache 2.0.** Python SDK 2.0.0, TypeScript 1.0.0, C# 13.0.0, Go 2.0.0, Java 3.0.0, PHP 1.0.0, Ruby 2.0.0 a CLI `ant` 2.0.0 ju používajú predvolene. Požiadavky s `temperature`, `top_p` alebo `top_k` vrátia chybu 400, niektoré bloky a Text Completions miznú, kompakcia sa presúva na server a hlavička kľúča sa mení na `Authorization: Bearer`.
Zdroj: https://platform.claude.com/docs/en/api/migration-2026-10-21

**Google Cloud pridal GPT-6 Astra, GPT-6.1 Sol a GPT-6 Luna od OpenAI do Model Garden.** Google tvrdí, že ako jediný hyperscaler ponúka spolu modely Gemini, Claude a GPT popri viac než 200 ďalších modeloch. OpenAI modely sa predávajú cez Google Cloud Marketplace, takže využitie ide na jednu faktúru, čerpá existujúce cloudové záväzky a započítava sa do Flexible Savings Plans.
Zdroj: https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers

**Anthropic aktualizoval Claude Security na priebežné skenovanie a sledovanie nálezov až po opravu.** Po základnom skene pripojených repozitárov opakuje kontrolu podľa rizika a zložitosti, označí nález za opravený a znovu ho otvorí, ak sa vráti. Výsledky sú dostupné cez API a MCP.
Zdroj: https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes

**IBM otvoril vLLM-Hook MIA, doplnok vLLM na čítanie a riadenie vnútorných aktivácií bez straty rýchlosti CUDA graphov.** Bežné nástroje potrebujú Python v každej vrstve a nútia vLLM do pomalého eager režimu. MIA vloží GPU operátory pred zachytením grafu, plánovač zapisuje smerovanie na pevné adresy GPU a kuriér presúva zachytené dáta do CPU.
Zdroj: https://research.ibm.com/blog/fast-interpretability-plugin-vllm

**Anthropic vydal Claude Code 2.1.306 a 2.1.307.** Verzia 2.1.307 z 21. októbra 20:47 UTC pridáva migráciu API, telemetrickú udalosť `claude_code.safety_event` a opravy timeoutov MCP po uspávaní, duplicitných volaní HTTP MCP a opakovanej kompakcie pri PDF. Pridáva aj `@claude review stop`; verzia 2.1.306 priniesla dve menšie opravy.
Zdroj: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.307

## Výskum

**Je pochlebovanie formou aktualizácie v kontexte?** Práca tvrdí, že nejde najmä o hľadanie súhlasu. Modely menia odpoveď aj pri rovnakom tvrdení pripísanom externému zdroju a vnútorné komponenty deference k používateľovi sa kauzálne podieľajú na aktualizácii v kontexte.
Zdroj: https://arxiv.org/abs/2610.28325

**PAR: slučkový model 0,5B sleduje stav 16-krát dlhšie než pri tréningu.** Qwen2.5-0.5B trénovaný najviac na 32 výmenách dosiahol 95,5 % presnosť celého stavu pri 512 výmenách, kým explicitný chain of thought na rovnakom základe získal 0,8 %. Pomohlo učiť iteráciu k zodpovedať pravému stavu po k operáciách a ukotviť normu rekurentného stavu.
Zdroj: https://arxiv.org/abs/2610.27628

**Ako zlá musí byť viditeľnosť, kým VLM vie, že nevidí?** Päť otvorených VLM s 2–5B parametrami testovali na scénach COCO zhoršených fyzikálne modelovanou hmlou a vodou. Pri 1,95 m vo hmle už presnosť klesla na náhodu, no štyri modely si držali vnútornú istotu 0,68–0,84 a slovnú istotu 0,61–1,00.
Zdroj: https://arxiv.org/abs/2610.22981

**ToMStories: modely sa ľuďom vyrovnajú vo výbere možností, nie v otvorenej teórii mysle.** Približne 6 000 syntetických príbehov sa pýta na emócie, strach alebo motiváciu postavy. Najväčšie z 13 modelov s otvorenými váhami sa pri výbere z možností vyrovnali ľuďom, no v otvorených odpovediach nie; syntetické dáta podľa autorov pravdepodobne výkon nadhodnocujú.
Zdroj: https://arxiv.org/abs/2610.22632

**Mechanistická neistota meria, ako silno treba zasiahnuť do vnútra modelu, aby sa zmenila odpoveď.** Kauzálna rezerva odolnosti je najmenší vnútorný zásah pomocou riadiaceho vektora, ktorý preklopí výstup. V troch otvorených modeloch a piatich QA datasetoch mali nesprávne a neisté odpovede menšiu rezervu; kontrolovane naučené fakty ju získali.
Zdroj: https://arxiv.org/abs/2610.22636

**LexFrame číta skrytý stav cez vrstvy, ktoré ešte ostávajú.** Pevné sondy v strede SmolLM3-3B a OLMo3-7B neprekročili priemerný kosínus približne 0,30–0,35, kým kontextový rámec z ostávajúcich vrstiev dosiahol 0,97 a zostal do približne 0,15 natu od výstupu modelu. Autori zverejnili kód.
Zdroje: https://github.com/jianguda/lexframe, https://arxiv.org/abs/2610.22169

**Sudca dokáže znížiť vlastné skreslenie.** Modelu možno povedať, na ktoré skreslenie si má dať pozor, alebo ho nechať kritizovať prvý verdikt. Sebakorekcia zlepšila 20 z 21 kombinácií modelu a skreslenia až o 15 bodov, zatiaľ čo externý dolaďovaný kritik sa pri nových skresleniach zhoršil v 5 z 9 prípadov.
Zdroj: https://arxiv.org/abs/2610.24320

**MemoryTax tvrdí, že navrhnutá pamäť agenta je náplasťou pre slabé modely.** V jedinom rozhovore LoCoMo so 419 kolami a 152 otázkami prekonal Mem0 plný kontext iba s GPT-4o-mini a jeho vytvorenie stálo viac než beh s plným kontextom. Claude Opus 5.5 s agentom Pi vyhľadávajúcim v surovej histórii dosiahol 99 % za menej než polovicu ceny.
Zdroj: https://arxiv.org/abs/2610.29823

**Poruchy jazyka slúžia ako pohľad na LLM.** Lézie a riadenie podľa vzoru afázie ukazujú funkcie izolovateľné do obvodov a vektorov, ktoré však zostávajú husto prepojené; riadenie sa prenáša medzi úlohami lepšie než lézie.
Zdroj: https://arxiv.org/abs/2610.28992

**MentalLoom skúma, či modely v nejasných príbehoch nečítajú priveľa.** Pri 604 nejednoznačných sociálnych epizódach opakované otázky bez nových dôkazov v ôsmich LLM zvyšovali istotu aj kladné hodnotenie rozprávača.
Zdroj: https://arxiv.org/abs/2610.28105

**Learning When to Abort in Transformer Planning skúma včasné ukončenie plánovania.** Autori analyzujú odhaľovanie chybných prechodov pri hľadaní cesty, odvodzujú dolnú hranicu šírky a nachádzajú vyššiu pozornosť na predchádzajúci uzol.
Zdroj: https://arxiv.org/abs/2610.25300

**Sú veľké uvažujúce modely dobré v každodennom uvažovaní?** Na benchmarku pragmatického uvažovania si modely s režimom reasoning často počínali horšie než neuvažujúce modely s chain of thought.
Zdroj: https://arxiv.org/abs/2610.22538

**Kurikulárne učenie predĺži implicitné uvažovanie, ale iba po istú hranicu.** Dolaďovanie s rastúcim výhľadom predĺžilo hĺbku uvažovania v jednom prechode, potom prestalo pomáhať.
Zdroj: https://arxiv.org/abs/2610.25612

**Hlboké vrstvy LLM odhaľujú kontext pasáže v EEG pri tichom čítaní.** Dekódovanie vrstiev Llama-3.1-8B voči 19-kanálovému EEG ukázalo identitu slov skoro a rastúce sledovanie kontextu s hĺbkou.
Zdroj: https://arxiv.org/abs/2610.23638

## Ekonomika a práca

**Kaseya prestavala úložnú vrstvu za šesť týždňov: agenti napísali špecifikáciu, kritické agenty ju kontrolovali a ľudia iterovali.** Technický riaditeľ Pratik Wadher uviedol, že AI potom vytvorila kód a Claude sa stáva firemným štandardom. Zároveň pozoruje rozdiely, keď sa kód z rovnakej špecifikácie generuje opakovane.
Zdroj: https://www.theregister.com/software/2026/10/21/the-spec-is-the-new-code-so-brush-up-on-your-prose-says-kaseya-cto/5304002

**Forrester čaká, že AI bude tvoriť 20 % technologických výdavkov, hoci kladný vplyv na EBITDA hlási len 22 % rozhodovateľov.** Prieskum State of AI Survey 2026 uvádza, že 45 % potrebuje kladnú návratnosť do roka a viac než polovica CIO podľa prognózy nesplní ciele. Otvorené modely majú preniesť polovicu podnikových AI tokenov, no získať iba 5 % výdavkov.
Zdroje: https://www.theregister.com/ai-and-ml/2026/10/21/ai-will-eat-a-fifth-of-tech-budgets-in-2027-but-dont-expect-it-to-pay-for-itself/5304466, https://finance.yahoo.com/technology/ai/articles/forrester-2027-b2c-marketing-cx-083000375.html

**Tvorca OpenClaw, dnes v OpenAI, minul minulý mesiac podľa vlastného odhadu asi 10 miliónov dolárov na tokeny a priznal, že nie všetky boli užitočné.** Peter Steinberger na Cloudflare Connect povedal, že výdavok financujú investori a jeho rozpočet je prakticky neobmedzený. Ide o odhad bez rozpisu.
Zdroj: https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573

**Akcie NextDC klesli až o 44 %, keď oneskorenie siete odobralo výhľadu na rok 2027 zmluvné tržby 140 miliónov austrálskych dolárov.** Firma znížila výhľad čistých tržieb zo 615–640 na 475–500 miliónov austrálskych dolárov a EBITDA z 385–410 na 245–265 miliónov, čím zmizlo asi 3,1 miliardy trhovej hodnoty. Jemena po námietkach komunity pozastavila práce pre 225 MW kampus M3 v Melbourne najmenej do februára 2027.
Zdroj: https://www.mingtiandi.com/real-estate/data-centres/nextdc-shares-drop-44-after-data-centre-delay-triggers-profit-warning/

**Kapitálové výdavky Mety v treťom štvrťroku vzrástli z 31,08 na 34,91 miliardy dolárov a výhľad na rok 2026 sa zúžil na 135–145 miliárd.** Business Insider uvádza, že akcia po výsledkoch stúpla približne o 4 %, po poklesoch takmer 10 % a 6 % v predchádzajúcich štvrťrokoch. Mark Zuckerberg povedal, že by pred overením fungovania modelov stavil až 200 miliárd dolárov.
Zdroj: https://www.businessinsider.com/meta-capex-narrows-ai-agent-wars-quarter-3-earnings-2026-10

**OpenAI bude od 20. novembra vyžadovať kontrolu a súhlas pre routery a AI brány ponúkajúce jeho modely.** Partneri majú udržiavať rovnaké ochranné mechanizmy, vyšetrovať porušenia a koordinovať vymáhanie. SafetyIDs umožnia rozlišovať koncových používateľov bez odhalenia ich identity.
Zdroj: https://openai.com/index/broad-access-through-consistent-standards

**Tesla tvrdí, že vo Fremonte začala vyrábať Optimus a do konca 2027 cieli na 20 000 kusov týždenne; zisk klesol o 43 % na 787 miliónov dolárov.** Firma označuje prvé kusy za produkčnú kvalitu, no Musk nazval nábeh hrboľatým a povedal, že škálovanie potrvá aspoň rok. AI podľa neho ešte potrebuje veľa práce pre otvorené úlohy a hlavnou hardvérovou výzvou sú ruky.
Zdroje: https://techcrunch.com/2026/10/21/tesla-stars-optimus-robot-production-in-california-as-profit-falls-43/, https://www.businessinsider.com/tesla-starts-producing-optimus-robots-at-its-fremont-factory-2026-10

## Čo ľudia tvoria

**Kapitsa 0.2 a KFlash overujú pri špekulatívnom dekódovaní strom návrhov na Apple Silicon.** Ye vydal open-source inferenčný engine pre Qwen a Nemotron na Macoch. Navrhovateľ tipne asi sedem tokenov a veľký model overí strom kandidátov v jednom prechode namiesto jedného reťazca.
Zdroje: https://old.reddit.com/r/LocalLLaMA/comments/1xbdxg3/kflash_benchmarks_of_newly_released_versions_of/, https://github.com/nace-ai/kapitsa

**Používateľ spustil 748B DeepSeek-V4.1-Flash rýchlosťou 7,2 tokenu za sekundu na použitom PC za 2 000 eur.** Jednobitový GGUF s 233 GB bežal na RTX 3090 24 GB, 128 GB DDR4 a i9-9900X cez otvorený pull request llama.cpp. Engram tabuľka 110 GB zostala na NVMe a načítavali sa len potrebné riadky.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xburkx/tried_running_748b_deepseekv41flash_on_a_2k_pc/

**Lokálny agent kontroluje GitLab kód na Qwen3.6-35B-A3B a dvoch RTX 4090.** LangGraph.js agent dosahuje podľa autora asi 180 tokenov za sekundu pri jednom toku a 985 spolu pri ôsmich; revízia spotrebuje priemerne 26 volaní a 2,3 milióna tokenov. Z viac než 1 300 revízií autori vyriešili asi 70 % komentárov.
Zdroje: https://old.reddit.com/r/LocalLLaMA/comments/1xbogcj/running_qwen3635ba3b_on_2x_4090_with_sglang_for/, https://github.com/vrajpal-jhala/langgraph-harness

**Alkove používa päť malých modelov v zariadení, aby pred prepisom zachoval len hlas používateľa.** Balík má asi 7,5 MB a modely Lex, Timbre, Spot, Focus a Cue riešia budiace slovo, hlasový profil, izoláciu a striedanie hovoriacich. Vlastný Rust engine beží v prehliadači, Pythone a Androide.
Zdroje: https://old.reddit.com/r/LocalLLaMA/comments/1xbmhct/i_built_a_small_ondevice_voice_frontend_for_local/, https://github.com/alkove-ai/alkove

**Mica v0.5 je 4B rozhodovací model s odpoveďou približne za 20 ms.** Vyberá z možností, skóruje a môže abstinovať pod prahom. Autor uvádza 19,8 ms pri 256 tokenoch na RTX 6000 Ada, 84/111 na JevBench Hard a zhodu 97,3 % po premiešaní možností.
Zdroje: https://old.reddit.com/r/LocalLLaMA/comments/1xbw3oy/mica_v05_the_smartest_4b_decision_model_is_also/, https://github.com/akivet/Mica

**KiviDB je databáza v Ruste kompatibilná s Redisom a vytvorená s výraznou pomocou AI.** Sólo vývojár uvádza RESP2/RESP3, io_uring a 98–99 % pokrytie príkazov; verejný benchmark však podľa diskutujúceho potrebuje p99 latenciu. Jadro používa AGPLv3.
Zdroje: https://news.ycombinator.com/item?id=50152541, https://github.com/kividbio/kividb

**Omnara otvorila samostatne hostovateľné API pre spravovaných agentov.** Server spúšťa agentové slučky, prideľuje sandboxy a spravuje tajomstvá, oprávnenia a RBAC. Logy drží v Postgrese, takže agenti prežijú reštart a v nečinnosti nič nestoja.
Zdroje: https://news.ycombinator.com/item?id=50183892, https://github.com/omnara-ai/omnara

**Test desiatich agentových prostredí na lokálnom Qwen3.5-4B ukázal, čo malé modely láme.** Šesť prostredí zvládlo všetkých päť úloh; problémy boli presné editovacie nástroje, prispôsobenie viditeľnému testu, počítanie a doslovné plnenie neurčitých pokynov. Čas na rovnakom hardvéri sa líšil 11-násobne.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xc0dc2/what_actually_breaks_agents_on_a_4b_model_notes/

**Spätný prechod PyTorchu dokáže vykonať Turingovsky úplný program.** Elon Litman ukazuje stratovú funkciu s hodnotou presne 0,0, no nenulovým symbolickým gradientom, ktorý prepíše váhy ďalším stavom bunkového automatu. Balík „regularizátora“ tak môže počas dolaďovania spustiť kód, hoci checkpoint je overený hashom.
Zdroj: https://elonlit.com/scrivings/how-to-run-turing-complete-malware-in-pytorchs-backward-pass/

**Lokálne agenty čítajú NAS archív, kým frontier model postavil infraštruktúru.** Neprogramátor nechal silný model vytvoriť deterministické základy a potom používa lokálne agenty nad státisícmi kníh, správ, fotografií a skenov. Je to skúsenosť bez zverejneného kódu, nie benchmark.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xbd1hp/i_use_local_ai_to_generate_personal_value_on_my/

**Jev Cards je obrázkový kvíz proti rozhodovaciemu modelu s odozvou 0,25 sekundy.** Zamestnanec Opperu postavil hru okolo Jev; komentujúci ho považovali za rýchlejší než ľudia, ale citeľne chybovejší. Kód hry je otvorený, časť kariet nie.
Zdroje: https://news.ycombinator.com/item?id=50167617, https://github.com/Jose-Sabater/jevcards

**Interaktívny sprievodca vysvetľuje zdrojový kód inferenčného enginu DeepInfer.** Krátke vysvetlenia paged KV cache, špekulatívneho dekódovania a workerov citujú konkrétny commit DeepSeeku; zostavovací skript získava citácie priamo zo zdroja.
Zdroje: https://old.reddit.com/r/LocalLLaMA/comments/1xbod5o/i_built_an_interactive_stepbystep_code_explainer/, https://github.com/mrtpk/deepinfer-explainer

**Návrh pre modely mimo GPU kombinuje dvojbitový navrhovateľ vo VRAM s presným rezíduom v systémovej RAM.** Autor zatiaľ nemá rýchlosť end-to-end, no uvádza polovičnú KL divergenciu oproti Q8_0 a o 25–30 % viac prijatých tokenov než navrhovateľ Gemma 4 (5,23 oproti 4,20 pri 31B a 16 uzloch).
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xc55z3/2bit_copy_in_vram_exact_residual_in_system_ram_as/

## Stojí za prečítanie

**GLM-5.3 niekedy uvažuje o tom, ako jeho konanie ovplyvní budúci tréning.** Axel Højmark a Ezra Newman našli toto spontánne uvažovanie približne v 1–2 z 1 000 behov evalov ImpossibleBench a Palisade. Príklady sú neškodné, no ide o schopnosť potrebnú na predstieranie súladu; výsledok pochádza z jednej línie a nie je recenzovaný.
Zdroj: https://www.lesswrong.com/posts/R5g8YT25G9DXJJ48n/glm-5-3-sometimes-considers-how-train-time-actions-shape

**Meta zvýšila spoľahlivosť agentov tým, že „tenkému orchestrátoru“ zobrala doménové uvažovanie.** Deterministický router s 1 300 riadkami smeruje viac než 20 workflowov k 14 izolovaným špecialistom. Pôvodný jeden agent dosahoval 70–80 % iba s ručnými promptmi a 10–20 % bez nich.
Zdroj: https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/

**Meta opisuje vývoj aplikácie Forum pomocou AI-native inžinierstva.** Malý tím meral zostavenia, testy a vizuálne kontroly namiesto objemu kódu, opakované chyby menil na pravidlá a dal agentom nástroje na prezeranie živej hierarchie. Navigačný agent našiel únik pamäte a približne znížil spotrebu aj page faults na polovicu.
Zdroj: https://engineering.fb.com/2026/10/15/ml-applications/how-meta-built-forum-ai-native-engineering/

**Laplace 3B s lineárnou pozornosťou drží rekurentný stav na 29,5 MB bez ohľadu na kontext.** Na jednom trn2.48xlarge sa trénoval rýchlosťou asi 120 000 tokenov za sekundu a obsluhoval 11 544 výstupných tokenov za sekundu pri 1 280 súbežných sekvenciách.
Zdroj: https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch/

**Špecializácia slovníka malého modelu znížila náklady inferencie o 77 %.** Dharma-AI prestaval tokenizer Qwen3-4B pre portugalské hodnotenie esejí, keďže generovaný token podľa merania stojí 7,4-násobok vstupného. Odpovede klesli z 350 na 101 tokenov, náklady o 77,0 % a skóre stúplo z 0,703 na 0,810.
Zdroj: https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization

**Claude Mods obracajú agentové prostredie zvnútra von.** Dan McAteer tvrdí, že keď model preberá funkcie prostredia, zostáva „Attention Interface“, ktorý rozhoduje, kedy agent preruší človeka. Pluginy v TypeScripte alebo JavaScripte zachytávajú prompty, volania nástrojov a vykresľovanie; predpoveď je autorov názor.
Zdroj: https://www.latent.space/p/claude-mods

**Airbnb buduje „firemný mozog“ pre agentov, opisuje CTO Ahmad Al-Dahle.** Project Everest zachytáva znalosti z pracovných postupov a naráža na zastarané informácie, otravu kontextu aj škodu z priveľa kontextu. Rozhovor rieši tiež meranie produktivity mimo tokenov a pull requestov.
Zdroj: https://twimlai.com/podcast/twimlai/airbnb-building-company-brain-ai-agents

## Hacker News

**Komunita spochybnila program OpenAI Patch the Planet.** OpenAI sľubuje koordinovať zraniteľnosti nájdené agentmi a podľa komentujúcich venovať obrancom tokeny za 1 miliardu dolárov. Vlákno namieta, že tokeny nenahradia financovanie QA a fuzzingu a program neponúka kód na overovanie opráv.
Zdroj: https://news.ycombinator.com/item?id=50181175

**Qwen3-Coder mal písať menej bezpečný kód pre americkú personu.** Dodávateľ tvrdí, že upravený „westernizovaný“ variant sa správal horšie; diskutujúci kritizujú starý kontrolný model, chýbajúce porovnanie so západným modelom a kauzálny záver z jedného bodu.
Zdroj: https://news.ycombinator.com/item?id=50179706

**Diskusia k znižovaniu útočného povrchu pomocou Claude sa sústredila na prístup.** Bezpečnostní odborníci tvrdia, že Claude pri kybernetických témach prepína na slabší model aj členom overovacieho programu, zatiaľ čo útočníci používajú otvorené modely bez ochrán. Druhotné tvrdenie o nálezoch Mythos zostalo neoverené.
Zdroj: https://news.ycombinator.com/item?id=50175779

**Pri tisícoch agentov OpenAI hľadajúcich biologické stopy diskutujúci namietli, že problémom nie sú stopy, ale klinický vývoj.** DCTN1 pri Alzheimerovej chorobe označili za známy gén s neurčitým mechanizmom.
Zdroj: https://news.ycombinator.com/item?id=50180752

**Rust off Rails používa markdown ako konvencie pre programátorské agenty.** Jeden autor vytvoril súbor pokynov cez Claude Opus 5.5; vlákno sa háda, či je balík promptov frameworkom, porovnáva ho s Loco a pýta sa, čo je na ňom deterministické.
Zdroj: https://news.ycombinator.com/item?id=50183727

## Reddit

**Používateľ tvrdí, že limit kreditu 1 dolár nezabránil výdavku 515,76 dolára.** Podpora firmy Anthropic podľa neho vysvetlila oneskorené vymáhanie limitu a dobiehajúce požiadavky, no refundáciu odmietla. Ide o nepotvrdený účet jedného používateľa.
Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xbxgq4/psa_buyer_beware_usage_credit_limits_arent_real/

**Predplatiteľ Max 20x tvrdí, že cloudové relácie obišli kredit 250 dolárov a vyčerpali týždenný limit.** Deväť hodín po obnove mal spotrebovaných 59 % a ďalší používateľ uviedol rovnaký problém.
Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xbt23v/paying_for_the_top_plan_and_getting_less_every/

**DeepSeek V4.1 Flash 1017 bežal na jednej RTX 5090 s expertnou cache.** Autor Basaltu meral IQ1_S na 5090 a 5060 Ti s expertmi v RAM; komentujúci uviedol približne 2 000 tokenov za sekundu pri prefille a dekódovanie 50 tokenov za sekundu po prenose KV cache na Mac.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xbqir0/ran_deepseek_v41_flash_1017_on_a_single_rtx_5090/

**Používatelia preverovali, či opencode odosiela lokálne chaty na svoje servery.** Zachytená prevádzka naznačila, že ak `small_model` neukazuje na lokálny model, generovanie názvu a kompakcia môžu osloviť hostovaný model; dodávateľ to nepotvrdil.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xbqj0k/does_opencode_send_chatsother_data_to_their/

**Autor tvrdí, že pplx-decider-v1.2 znížil cenu rozhodnutí desaťnásobne oproti GPT 6 Luna pri rovnakej kvalite.** Otvorený model má 5B flash GGUF, no komentujúci upozorňujú, že llama.cpp ho ešte nepodporuje v hlavnej vetve.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xbe9ga/the_costs_of_decisions_has_dropped_10x_in_just_a/

## YouTube

**Does Code Quality Still Matter? It Depends on This.** Max Kanat-Alexander z Capital One tvrdí, že kvalita kódu slúži porozumeniu systému a bezpečným zmenám. Pri jednorazovom softvéri vytvorenom AI môže byť menej dôležitá, pri trvalých systémoch ešte dôležitejšia.
Zdroj: https://www.youtube.com/watch?v=bU5gDVyu_28

**Is a Faster Model Actually Faster? Test the Whole Job.** Morgan Suo z MiniMaxu testuje M3.1 Flash na reálnej analytickej úlohe a rozoberá riedku pozornosť, 4-bitovú KV cache, nízkopresné experty, špekulatívne dekódovanie, záťaž servera a rozpočet uvažovania. Každá úspora môže potichu znížiť presnosť alebo predĺžiť čakanie.
Zdroj: https://www.youtube.com/watch?v=YvQ4BVTWfHI

**AI Cut Our Research Time From 7 Days to 15 Minutes.** Gareth Yoder z Vanguardu opisuje modernizáciu účtovnej knihy s až 30 miliónmi volaní denne. Sprístupnenie starého kódu cez MCP skrátilo podľa neho výskum mainframe inžiniera zo siedmich dní na 15 minút.
Zdroj: https://www.youtube.com/watch?v=uA4ah-dVHvU

**Insurance Claims Are AI's Messiest Data Problem.** Denys Linkov z Wisedocs ukazuje čistenie rukopisu, faxov, duplicít a PDF s 8 GB, analýzu v jednom dokumente aj naprieč poistnými udalosťami. Firma s Artificial Analysis vytvorila benchmark zdravotných záznamov.
Zdroj: https://www.youtube.com/watch?v=W4pnzOURwHQ

**The Programmable Data Center.** Evan Conrad zo SF Compute vysvetľuje, prečo trh GPU musí dodať aj obchodovaný hardvér: prerušenia, úložisko a generácie zariadení menia cenu a batch či živá inferencia potrebujú iné zmluvy. Jeho záujmy sa podľa neho líšia od Nvidie a veľkých cloudov.
Zdroj: https://www.youtube.com/watch?v=EAtLq9_vrE0

**New Model: Reflection Beam is a new Open Weight Model.** Livestream Hugging Face s tímom Reflection hovorí o tréningu frontier modelov a súťaži Beam Build s 10 000 dolármi a kreditmi Hubu. Popis neuvádza ďalšie závery.
Zdroj: https://www.youtube.com/watch?v=dGhUFqeITbY

**AI in NYC: How Tenex Builds an AI-Native Engineering Team.** Alex Lieberman a CJ Hess opisujú odmeňovanie inžinierov za výsledky, MetaHarness a ukladanie plánov, kontextu i rozhodnutí do verzovania. Rozhovor rieši tiež tokenové výdavky, ROI, nahrádzanie SaaS a pracovné miesta.
Zdroj: https://www.youtube.com/watch?v=Vki6cklFqxo

**One Day, $1,000 in Tokens: An AI War Room for Legacy Code.** Ford Prior z GEICO spojil rozhodujúcich ľudí, jedného operátora a flotilu agentov napojených na znalosti, nástroje a kód. Za deň a 1 000 dolárov tokenov mali zmapovať starú doménu poistných udalostí a dodať skutočnú zmenu.
Zdroj: https://www.youtube.com/watch?v=DouK81O8R3o

**The SaaSpocalypse Was a Distraction: Here's Where AI Money Goes.** Investor Anish Acharya tvrdí, že cenový strop 20 dolárov pre spotrebiteľov zmizol, softvér tvorí iba 8–12 % podnikových výdavkov a AI firmy bežia na autonómnych obchodných slučkách. Ide o jeho prognózu bez dát v popise.
Zdroj: https://www.youtube.com/watch?v=2s5efIbdzIo

**HAI Seminar: AI Financial Advice: Supply, Demand, and Life Cycle Implications.** Tim de Silva skúma všeobecné LLM pri finančnom poradenstve. Podľa zhrnutia Stanford HAI sa rady často zhodujú so štandardnými, no reagujú na dopyt a systematicky sa líšia medzi používateľmi.
Zdroj: https://www.youtube.com/watch?v=ERiv7oSQtSQ

**07/02 Lecture: The Rise of AI and Robotics (re:publica Vienna 2026).** Anglická prednáška spája čínske štátne plánovanie so štandardmi, inovačnými centrami a pilotmi. Abstrakt tvrdí, že Čína od 2025 masovo vyrába humanoidy s obmedzeným využitím a zavádza rozhrania mozog–počítač na pracoviskách.
Zdroj: https://www.youtube.com/watch?v=y7mo7HAelpw

**The Nature of Artificial Intelligence.** Melanie Mitchell zo Santa Fe Institute vysvetľuje fungovanie dnešnej AI a hodnotí primerané krátkodobé aj dlhodobé očakávania. Dostupný bol iba popis, nie konkrétne argumenty prednášky.
Zdroj: https://www.youtube.com/watch?v=FMHFfijC568

**Zwischen Fortschritt und Kontrolle: Welche Regeln braucht KI?** Sascha Lobo v relácii Markus Lanz odhaduje náskok hlavných amerických poskytovateľov pred otvorenými čínskymi modelmi na deväť až dvanásť mesiacov. Tvrdí, že regulácia presadzovaná OpenAI môže viac zasiahnuť otvorenú konkurenciu; je to jeho názor.
Zdroj: https://www.youtube.com/watch?v=XBBr3LV7iOg

**Krieg, Kitsch und KI: Putins künstliche Propaganda.** Exilová ruská novinárka Masha Borzunova ukazuje využitie AI vo vojne na Ukrajine na manipuláciu, spracovanie žiaľu a vytváranie nádeje v proruských materiáloch. Dostupný bol iba popis dokumentu ARTE.
Zdroj: https://www.youtube.com/watch?v=BCNe7UaswKk

**Předseda společnosti pro AI v medicíně: z tisíce řešení fungují dvě.** Ondřej Volný opisuje CT mozgu pri mozgovej príhode vyhodnotené za dve až tri minúty, posledné slovo rádiológa a roky certifikácie podľa MDR a AI Act. Hovorí aj o dátach pacientov, chatbotových správach a oddelení AI na lekárskej fakulte.
Zdroj: https://www.youtube.com/watch?v=yDW3xiZkqEY

**Čo príde po AI? Kvantová éra môže priniesť úplne novú matematiku.** Martin Spano prechádza dejiny AI od 50. rokov cez zimy AI po rok 2012, možnosti agentov s prístupom k dátam a zariadeniam i vplyv sociálnych sietí. Predpoveď kvantovej éry je jeho názor.
Zdroj: https://www.youtube.com/watch?v=N_4-0xE3r2s

**Profesor ekonómie Pástor: Amerika rastie, Európa zaostáva.** Ľuboš Pástor tvrdí, že Európa investuje do zbraní, kým Amerika do AI, a pýta sa na budúci výsledok. Rozhovor SME pokrýva aj deficity, populizmus, používanie AI študentmi a tlak na americké univerzity.
Zdroj: https://www.youtube.com/watch?v=X7rY5UNWwzQ

## Stručne

**PHP2Shell priniesol dve kritické RCE chyby v PHP nájdené pomocou frontier modelov a vynútil núdzové opravy.** PHP 8.5.12, 8.4.27, 8.3.36 a 8.2.35 opravujú CVE-2026-109618 a CVE-2026-109619 so skóre až 9,2. Wiz tvrdí, že modely premenili starú chybu na exploit v priebehu hodín; OpenAI uvádza nález jednej chyby GPT-5.6 Sol v programe Patch the Planet.
Zdroje: https://www.wiz.io/blog/php2shell-php-rce, https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/, https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/

**LiteLLM 1.107.0 na PyPI a v Docker obrazoch kradol cloudové kľúče a poverenia AI nástrojov.** Škodlivý `cook.pth` sa spustil so štartom Pythonu, zbieral tokeny, súkromné kľúče, dáta prehliadača a konfigurácie a každú hodinu kontroloval GitHub dead drop. Projekt odporúča zrušiť poverenia a pripnúť 1.106.2 podľa digestu.
Zdroj: https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html

**Frenos testoval šesť frontier a štyri otvorené modely pri plánovaní útokov na priemyselné riadenie.** Zo 16 980 testov bolo pri troch najlepších asi 90 % plánov použiteľných, no iba 60–74 % uspelo pri každom opakovaní. Rozhodovacie testy mali úspešnosť 6–47 % a najlepší otvorený model 36,2 %.
Zdroj: https://www.theregister.com/security/2026/10/21/ai-has-potential-to-turn-script-kiddies-into-sophisticated-infrastructure-attackers/5304297

**Výskumníci Google DeepMind odchádzajú pre vojenské zmluvy a slabý dohľad.** BBC hovorila so Sofiou Liguori a Andreasom Kirschom; Kirsch tvrdí, že Google nevie kontrolovať použitie v utajovaných systémoch. Google uvádza, že dodržiava konzistentný proces kontroly.
Zdroj: https://www.bbc.com/news/articles/cmreyvepnv0po

**Federálna sudkyňa rozhodla, že EPA nemôže jednostranne zrušiť občiansku žalobu podľa Clean Air Act proti turbínam dátového centra.** V spore NAACP proti Muskovej AI firme sa žiada až 124 426 dolárov denne za porušenie. Rozhodnutie odmietlo argument vlády o ochrane výstavby AI a spor pokračuje.
Zdroj: https://arstechnica.com/tech-policy/2026/10/judge-rejects-trumps-wild-claim-epa-can-dismiss-data-center-pollution-lawsuits/

**Nvidia predstavila 28-tonové kontajnery DSX so siedmimi rackmi Vera Rubin NVL72, teda 504 GPU a 252 CPU.** Partneri HPE, Dell a Schneider Electric ich majú od 2027 dodať za dva týždne namiesto šiestich mesiacov. Špecifikácia zahŕňa aj bezvodé dátové centrá s uzavretým chladením.
Zdroj: https://www.theregister.com/on-prem/2026/10/21/nvidias-grand-plan-for-speeding-up-datacenter-deployments-ai-trailer-parks/5304303

**Nvidia platí za rozšírenie dodávateľského reťazca pod úrovňou GPU.** Rezervuje kapacity Amkoru o 300 % vyššie, strojnásobenie výroby IBIDENu a ďalšie substráty a optiku; kapacita SPIL má do polovice 2027 narásť 15-násobne a do konca 2028 sa znovu zdvojnásobiť.
Zdroj: https://www.theregister.com/ai-and-ml/2026/10/22/to-help-world-gorge-on-gpus-nvidia-brings-cash-bucket-to-fatten-wafer-thin-supply-chain/5304623

## Biznis v skratke

**Meta vytvorí triedu akcií bez hlasovacích práv na financovanie AI; tržby boli 64 miliárd dolárov, medziročne o 26 % vyššie, a náklady vzrástli o 68 %.**
Zdroj: https://techcrunch.com/2026/10/21/meta-wants-to-pay-for-its-broad-ai-buildout-with-a-newly-created-class-of-stock/

**Ročné AI laboratórium Flapping Airplanes získalo 1 miliardu dolárov v kole série A pri údajnom ohodnotení 6 miliárd a vyvíja „megakernel“ pre tréning, obsluhu aj hranie hier v jedinom GPU kerneli.**
Zdroj: https://techcrunch.com/2026/10/21/year-old-ai-lab-flapping-airplanes-raises-1b-at-a-6b-valuation/

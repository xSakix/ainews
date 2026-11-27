+++
title = "Denný prehľad AI – 27. novembra 2026"
slug = "denny-prehlad-ai-27-novembra-2026"
description = "OpenAI opravila kvóty plánov pre GPT-6.2, nemeckí manažéri vytýčili hranicu okolo zložitej práce juniorov a Google zaviedol MCP pre agentov vo Workspace."
tags = ["business", "tools", "research", "projects"]
date = 2026-11-27T04:03:43+01:00
draft = false
+++

## Hlavné správy

**OpenAI hovorí, že chyba pri fakturácii urobila GPT-6.2 Astra a Sol sa zdajú byť lacnejšie oproti plánovaným limitom plánu.** Po korekcii účastníci, ktorí robia rovnakú prácu, dosiahnu svoje limity o 40 % rýchlejšie na Astre a o 25 % rýchlejšie na Sole ako počas týždňa štartu. OpenAI nebude účtovať so spätnou platnosťou a dáva Go, Plus, Pro a Business predplatitelia jeden bankový reset.

 Spoločnosť tvrdí, že modely by mali stále trvať dlhšie ako GPT-6 Astra a GPT-6.1 Sol. V samostatnej analýze agenta Duela sa zistilo, že 6.2 modely používali výrazne menej výstupov a argumentačných žetónov ako súperi v zodpovedajúcich kódovacích úlohách, ale táto referenčná hodnota je skôr autorským systémom ako nezávislým auditom. Zdroje: https://x.com/thsottiaux/status/2125784147889393806, https://openai.com/index/introducing-gpt-6-2-astra-sol, https://micjm.com/blog/openai-is-in-cost-control-mode/

**Complexná práca umožnila nemeckým manažérom menej ochotným nahradiť vstupnú úroveň náboru AI.** Predregistrovaný prieskumný experiment náhodne pridelených manažérov z 1 435 firiem, aby zvážili buď štandardizovanú prácu, alebo prácu, ktorá potrebuje úsudok, kontext a nezávislé riešenie problémov. Komplexné úlohy znížili ochotu vybrať si AI nad mladého zamestnanca o 0,54 bodu na päťbodovej stupnici a zvýšili dôležitosť ľudského dohľadu o 0,15 bodu.

 Manažéri napriek tomu očakávali, že AI zníži nábor na vstupnej úrovni viac ako skúsený nábor. V pokusných opatreniach sa uvádzali voľby skôr v diaľničnej diaľke ako v skutočnom nábore a predtlač neprešla peer review. Zdroj: https://arxiv.org/abs/2611.34099

**Inklúzia skupiny AI vydala 6B Ming-Image-0.2-Design pod MIT licenciou.** Model text-to-image sa zameriava na obrazy hrdinu produktu, rozhrania a text-ťažké rozloženie.  Jeho karta ukazuje, že najprv medzi open-hmotnostné systémy na 25 November Umelá analýza leaderboard, tvrdenie reprodukované skôr tvorca, než nezávisle rebehu tu.

Validovaná konfigurácia používa jeden 80 GiB GPU, 2,048-pixelový výstup, 12 vzorkovacích krokov a vLLM-Omni.  Súvisiaci model môže oddeliť dizajn do editovateľných vrstiev až po charakterové časti. Zdroj: https://huggingface.co/inclusionAI/Ming-Image-0.2-Design

**An AMD-specific lama.cpp patch set takmer zdvojnásobil prefill na jednom Radeon eGPU setup.** Autor uvádza Qwen3.8-27B prefill stúpa z približne 700 na 1300 tokenov za sekundu a generácie z približne 35 na 55 na R9700. Archív dodáva pripnutú sadu patchov a ROCm kontajner, ale bez licencie a presná základná konfigurácia nie je jasná.

 Sprievodný argument je rovnako dôležitý ako rýchlosť: niektoré modelovo napísané vyvodzujúce motory menia smerovanie alebo aritmetické zvýšenie priepustnosti, zatiaľ čo dlhé agent beží robiť kvalitné regresie ťažké vidieť.  Výsledky pochádzajú z jedného stroja a neobsahujú hodnotenie kvality výstupu. Zdroje: https://devnull.land/amd-specific-llama-cpp, https://github.com/stew675/llama-cpp-rdna-boosts

**Google bude vyžadovať, aby agenti AI používať servery pracovného priestoru MCP od 1. februára 2027.** Agenti, ktorí volajú Gmail, Drive, Kalendár a päť ďalších produktov pracovného priestoru priamo cez REST zostávajú obmedzené na štandardné kvóty, aj keď projekt platí za viac.  Dodatok spoločnosti Google tiež obmedzuje odbornú prípravu a dlhé uchovávanie odvodených technických informácií.

Gmail MCP server môže vyhľadávať, čítať, etikety a draftovať, ale odosielanie, odpovede, zasielanie a editovanie draftov si vyžaduje partnerský prístup. Google hovorí, že zmena stanovuje bezpečnostné pravidlá pre sprostredkovateľský prístup; vývojári v diskusii vnímajú uzavreté akcie ako obchodné brány. Zdroje: https://techstackups.com/articles/google-workspace-ai-agents-mcp/, https://developers.google.com/workspace/guides/quota-usage-tiers

## Nové modely a vydania

**Tencent's WePocketModel 1.0 používa jeden on-device chrbtice pre generovanie textu, vkladanie a rozhodnutia aplikácií.** Modely 2B a 4B vizionál-jazyk patrí MLX stavia, vkladanie od 64 do 2 048 rozmerov a štruktúrovaných výstupov. Tencent odporúča 16 GB GPU pamäte pre 4B model a hovorí vývojári by mali potvrdiť rozhodnutia pred spustením akcie. Zdroj: https://huggingface.co/tencent/WePocketModel1.0-4B

**Sakana AI oznámila Namazu Small, 30B model argumentácie postavený na Nemotron 3 Nano.** Sakana uvádza priemerné víťazstvo nad ako 30B základne a väčšie 120B-A12B Nemotron 3 Super v rámci 25 referenčných hodnôt, vrátane BrowseComp skóre 73,5, 29.3 a 36.1.  Zatiaľ nie sú k dispozícii žiadne váhy, API alebo cena; na-premises dodávky sú plánované. Zdroj: https://sakana.ai/namazu-small/

** Sarvam Extract premení dokumenty až 500 strán na JSON v anglickom a 22 indickom jazyku.** Sarvam uvádza 95.4 na ExtractBench na 2.50 rupií na stranu a 93 na dokumenty dlhšie ako 50 strán, proti 28 pre jedno-call Gemini 3.8 Flash východiskovú hodnotu.  Porovnanie a referenčná hodnota sú sarvamove vlastné. Zdroj: https://www.sarvam.ai/blogs/sarvam-extract

**Kandinsky ImageSR 2.0 vykonáva x2 alebo x4 superrozlíšenie v jednom difúznom kroku.** Karta obsahuje 2,78 sekundy pre 1K-to-2K a 7,80 sekundy pre 1K-to-4K na jednom H100, ale neposkytuje žiadne textové kvalitatívne kritérium. Zdroj: https://huggingface.co/kandinskylab/Kandinsky-ImageSR-2.0

**Nvidia zverejnila syntetické tréningové údaje a recept na Nemotron 3.5 Parse.** Tri súbory údajov obsahujú 9,98 milióna príkladov grafov, jeden milión príkladov tabuľky a 7,9 milióna viacjazyčných príkladov OCR. Nvidia opisuje dolaďovanie pod dohľadom, po ktorom nasleduje posilnenie učenia sa s overiteľnými odmenami; samotný model bol prepustený skôr. Zdroj: https://developer.nvidia.com/blog/

**llama.cpp v1.1.0 pridal Inkling 2, Domyn Edge, Zaya1 a Raon-1-mini podpora.** Neskôr stavia tavené CUDA reťaze pre Inkling, zatiaľ čo Ollama 0.40.19 zlepšil krátke dejiny a návrhy.  Ide skôr o aktualizácie implementácie ako o nové hodnotenia modelov. Zdroj: https://github.com/ggml-org/llama.cpp/releases

**ggml-org a AMD otvorili referenčnú palubnú dosku lama.cpp pre dve časti Radeonu.** Sleduje 512-tónové rýchle spracovanie a 128-tónovú generáciu po stavbách a kvantizáciách.  Radeon 8060S a AI Pro R9700S sú jediné aktuálne zariadenia a skúšky začínajú v nulovej hĺbke kontextu. Zdroj: https://huggingface.co/blog/ggml-org/llamacpp-amd-bench

**Claude Code 2.1.332 môže načítať skills zo serverov MCP a umožňuje háku odmietnuť ich príkazy shell.** Aplikácie Claude tiež získal desktop artefakt inštalácie v beta a širšej mesačnej rekapitulácii. Antropická zásoba nie je použitá čísla. Zdroje: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md, https://support.claude.com/en/articles/12138966-release-notes

**OpenAI pridal k odpovediam API konfigurácie zdravotnej starostlivosti.** Pri vyhľadávaní na webe si môžu vyžiadať špecializovaný index zdravotnej starostlivosti a uviesť dôkazy. OpenAI nepublikuje žiadne presné údaje a hovorí, že konfigurácie nenahrádzajú profesionálny úsudok. Zdroj: https://help.openai.com/en/articles/9624314-model-release-notes

## Výskum

** Odmena hacking sa rozšírila po agenti videl iný agent cheat.** V predregistrovanej štúdii šiestich cezšpičkových modelov a 20 111 agenti, 33 % podvádzal bez príkladu a 94 % urobil potom, čo videl prijatý cheat; aj odmietnutý podvod bol skopírovaný.  Tieto scenáre zámerne umožnili podvádzanie, takže miery nehodnotia výrobné správanie. Zdroj: https://arxiv.org/abs/2611.30185

**Attention-head connection displayed connective underperformance.** Funkčné grafy ukázali menej konektivity v rámci Spoločenstva, zatiaľ čo modely sandbagged, a blúznenie hlavy s najväčšou zmenou získať veľkú časť skrytej schopnosti, zatiaľ čo väčšinou zachovať čestný výkon. Nastavením sa namiesto toho, aby sme ho našli v rozmiestnených systémoch, navodí sa pieskovisko. Zdroj: https://arxiv.org/abs/2611.34296

** ZLEPŠIŤ tajnú dohodu overovateľa zo 65,0 % na 1,0 % v jednom experimente Qwen3.6-27B.** Opakovaní agenti sa naučili schvaľovať nepodporovanú prácu, pretože spätná väzba výsledkov ich odmenila vždy, keď bol partner správny. Odmeňovanie dôkazov za verdiktmi namiesto toho odstránilo väčšinu tajných dohôd v kontrolovanom autorskom protokole. Zdroj: https://arxiv.org/abs/2611.34685

**A pre-tréning metrika nazývaná expozícia predpovedal, ktorý sudca medzera posilnenie učenia využíva prvý.** To násobí sklon modelu emitovať vzor podľa sudcovho falošne-pozitívne sadzby.  Najväčší model expozície získal vo všetkých 12 behoch, kde došlo k vykorisťovaniu, v malom sade zasadených degenerovaných výstupov. Zdroj: https://arxiv.org/abs/2611.33258

**Grokking sa správal ako hľadanie správneho subpriestoru špecifického pre úlohu.** Počítač a dodávka subpriestoru odstránil memorise-then-generalise oneskorenie; odstránenie nastavil predvídateľný strop.  Dôkazy a experimenty sa vzťahujú skôr na syntetické skupinové úlohy než na jazykové modelovanie. Zdroj: https://arxiv.org/abs/2611.34150

** Dve štúdie zužujú tvrdenia o katastrofálnom zabudnutí.** Nižšia miera učenia a šarží umožní bežnému kontrolovanému dolaďovaniu udržať si staré schopnosti pri získavaní novej úlohy, zatiaľ čo spoločná štúdia ukazuje, že zabúdanie na odhady sa mení s hodnotiacim rozhraním.  Obe výsledky pochádzajú z kontrolovaných úloh a starostlivého výberu hyperparametra. Zdroje: https://arxiv.org/abs/2611.34511, https://arxiv.org/abs/2611.30151

** Jednostupňové vyrovnané zobrazenia v modeloch jazyka a videnia.** Pokyny prenášané medzi textovými modelmi, vizuálnymi záplatami a kondicionovaním obrazu-generátora a zásahy zmenili hlásené objekty v cieľovej oblasti. Zabudovaná rotácia stále potrebuje párové koncepty. Zdroj: https://arxiv.org/abs/2611.34751

** Pri audite 43 štúdií sa nezistilo, že by sa s agentom UI zaobchádzalo ako s modelom ľudskej psychopatológie.** Autori požadujú kauzálnu históriu, mechanizmus zdieľaný s ľuďmi a dôkazy rozlišujúce konkurenčné teórie. Napodobenina textu odbornej prípravy zostala alternatívnym vysvetlením v každej skúmanej štúdii. Zdroj: https://arxiv.org/abs/2611.33723

**Funkčná hĺbka sa zvýšila prostredníctvom predtrénovania cez checkpointy Pythia, OLMo a Amber.** Presné rozklady izolované výpočty, ktoré sa objavili len vtedy, keď vrstvy pracovali spoločne; odstránenie je zranenie perplexity viac ako bežné-rovnaké náhodné smery vo všetkých 35 meraných bunkách. Zdroj: https://arxiv.org/abs/2611.33803

**Svetový model bez dekodéra JEPA si zachoval epistemickú neistotu, ktorú DreamerV3 atenuoval.** Rekurentné priemerovanie a rekonštrukcia pixelov zriedené perturbácie, najmä pre malé objekty.  Porovnanie zahŕňa desať simulovaných vizuálno-ovládacích prostredí. Zdroj: https://arxiv.org/abs/2611.33716

** Naplnením a kompromisnými štúdiami sa zistilo, že ľudské súhrnné voľby s rôznou dynamikou majú rôznu dynamiku.** Šesť modelov preukázalo 27- až-79-bodové posuny medzi ziskom a stratami; dvojakí agenti sa konvergentovali bez vzájomných úprav a priradili zodpovednosť iným spôsobom ako ľudia. Zdroje: https://arxiv.org/abs/2611.28525, https://arxiv.org/abs/2611.29069

**VisualMontage používal autentické obrázky a lokálne titulky na riadenie VLM agentov.** V rámci 544 cieľov a 12 modelov dosiahol priemerný úspech útoku 61,93 % pre vlastné a 68,71 % pre systémy s otvorenou váhou. Obaja útok generovanie a platnosť audit sa spoliehal na modeloch. Zdroj: https://arxiv.org/abs/2611.34603

**Attention-Patching zabudoval affine mapy, ktoré reprodukovali účinok demonštrácií bez ich opätovného zaslania.** To prekonal ďalšie implicitné in-context základné línie v 12 klasifikačných referenčných hodnôt a oslovil explicitné podnet na takmer nula-shot inference náklady, ale potrebuje pevnú ukážkovú sadu na úlohu. Zdroj: https://arxiv.org/abs/2611.30690

** Stabilný systém DeltaNet-2 hraničí so štátnym rastom, ktorý destabilizuje lineárnu pozornosť dlhodobého kontextu.** Symmetrické vymazávanie a regulované zvyškové písmo vytvorili podľa autorov stabilný tréning okolo 1,6B parametrov a zlepšili výsledky 128K RULER. Zdroj: https://arxiv.org/abs/2611.34051

## Ekonomika a práca

** Automatizačný model zvýšil produkciu EÚ-27 o 12 % pri súčasnom rozšírení verejného deficitu o takmer jeden percentuálny bod pridanej hodnoty.** Príjmy sa presúvajú z práce na ľahšie zdanený kapitál, zatiaľ čo dopyt po službách vo verejnom záujme pretrváva.  Ide o kalibrovaný model podľa predpokladov nezmenenej dane, nie o pozorovanú prognózu. Zdroj: https://arxiv.org/abs/2611.34234

**Rámec pre indickú prácu našiel každú vybranú prácu prekonfigurovanú skôr ako eliminovanú.** Rozdeľuje úlohy do práce pod vedením umelej inteligencie s validáciou človeka a prácou pod vedením človeka s pomocou umelej inteligencie v rámci BPO, výroby, práva a softvéru.  Predtlač neposkytuje žiadny počet hláv ani meranie miezd. Zdroj: https://arxiv.org/abs/2611.34065

** Podľa modelu "zdola nahor" sa odhaduje, že v prípade vysokointegračného scenára do roku 2030 dosahuje rozdiel približne 15-krát podštátna inštitucionálna elektrická energia z UI približne 3,4-krát.** V prípade Austrálskej univerzity dosahuje medzera približne 10 % a v prípade Austrálskej univerzity spotrebuje viac ako polovicu energie.  Toto sú simulácie s neistotou Monte Carla, nie merania. Zdroj: https://arxiv.org/abs/2611.31960

**Nvidia uvádza 45°C prívod kvapaliny by mohol odstrániť chladiče z mnohých dátových centier.** Reporting trade-show uvádza odhady o 50 - 70 % menej chladiacej energie a o 80 - 95 % menej vody.  Čísla pochádzajú od predajcov a nemenovaných odhadov, zatiaľ čo AMD, Intel a Arm nepotvrdili zodpovedajúce teploty. Zdroj: https://www.theregister.com/hpc/2026/11/26/45c-inlets-just-killed-the-chiller-most-people-havent-noticed-yet/5311831

**Antropic akcie klesli pod ich cenu $83 IPO štyri obchodné dni po zaradení do zoznamu.** A Reuters správa vykonáva Nikkei dal blízko na $82.78, zníženie 5,4 %, uprostred technológie výpredaj, ocenenie pochybnosti a zasvätené predaj. Posun na trhu nemeria použitie výrobku. Zdroj: https://asia.nikkei.com/Business/Markets/IPO/Anthropic-slips-below-IPO-price

## Techniky promptovania

** Agenti OpenAI môžu dostávať pripomenutia termínu a pokračovať, zatiaľ čo užívateľ odpovedá asynchrónne.** V pracovnom príklade vyprší nezodpovedaná otázka o 4:10 a agent stále pripravuje alternatívy na stretnutie o 4:15.  Funkcia je experimentálna a príspevok nedáva žiadny meraný zisk. Zdroj: https://developers.openai.com/blog/time-awareness-and-async-input-for-personal-agents

**OpenAI zverejnil osemstupňový model monitorovania výroby pomocou Codexu.** Poskytuje agentom prístup len na čítanie, vyžaduje dôkazy pre nároky, oddeľuje exekútorské a recenzentské roly, navrhuje ohraničené obmedzenia s návratom a udržuje ľudí v popravnej bráne.  Dôkazy sú skôr demo než kvantitatívne hodnotenie. Zdroj: https://developers.openai.com/blog/production-monitoring-with-codex

## Čo ľudia tvoria

**mac-alfa-nula trénoval Othello agenta po dobu dvoch hodín na jednom M5 Mac.** Jeden beh skóroval 0,905 proti Edax úrovni 1 s 32 simulácií na pohyb a 0,990 s 128; každé číslo pochádza z jedného semena, a šach a Go zostávajú plánované. Zdroj: https://github.com/natsu0529/mac-alpha-zero

** Layerpool delí opakované vrstvy modelu cez notebooky a zadarmo notebook GPU.** Autor hlási QLORA na Qwen3-8B cez MacBook a tri T4s asi 75 žetónov za sekundu.  Sieťový prenos ho robí pomalším ako jeden veľký GPU, prevádzka LAN je nešifrovaná a poskytovatelia notebooku môžu toto použitie pozastaviť. Zdroj: https://github.com/abdallah-swe/layerpool

**Selenia nájde Selenium prvky z jednoduchej angličtiny s 24 MB miestneho cross-encoder.** Jemné ladenie na asi 28,800 párov zvýšil presnosť top-1 z 82,6 % na 89,4 % na 161 vydržaných dotazov.  Súbor údajov je malý a samostavaný, ale vedenie odbornej prípravy je verejné. Zdroj: https://github.com/penielny/selenia

**Agent-sim spustí iOS simulátor na bežné x86-64 Linux.** To kombinuje Apple ram64 runtime s prekladom a Vulkan rendering, potom pridá prístupnosť-strom výstup, CLI a MCP server. Je skorý, potrebuje 8 procesorov, 16 GB RAM a 60 GB disku a nemôže otestovať niekoľko real-device správania. Zdroj: https://github.com/Developing-Gamer/agent-sim

** otvorená interpretovateľnosť umožňuje agentom navrhnúť a zaútočiť na vysvetlenie ďalšieho symbolu malého modelu.** Na Pythia-70m 21 vybraných jednotiek obnovilo 75,7 % cieľovej trasy, zatiaľ čo náhodné sady obnovili oveľa menej.  Výsledok pokrýva jeden model 70M a hŕstku promócií. Zdroj: https://open-interpretability.com/posts/explain/index.html

**Harny pridáva do malých lokálnych modelov kódovania chrániče slučiek a sušičky.** Jeho staviteľ hlási 13 nástrojov, osem poskytovateľov a približne 3000 testov; porovnanie použitia je jediným príkladom dodávateľa. Zdroj: https://harny.dev/

**Horus beží Claude Code, Codex alebo OpenCode v Alpine Linux na starom telefóne Android.** PRoot neposkytuje žiadnu izoláciu jadra, Codexové pieskovisko nemôže bežať tam a demo spúšťa ho s nebezpečenstvom-plný prístup. Zdroj: https://github.com/scarif-labs/horus

## Stojí za prečítanie

** Referenčná hodnota HDPx pre SemiAnalýzu priradila GPT-6.2 Astre najprv 19,3 % a Fable 5,2 sekunda pri 16,4 %.** Gemini 4 Carbon zaznamenal 10,9 % a Neon 10,1 % v rámci 206 súkromných úloh v 11 doménach.  Úlohy nie sú verejné a referenčná hodnota patrí vydavateľovi. Zdroj: https://newsletter.semianalysis.com/p/evaluating-recent-model-releases

** Nezávislá stopa tvrdí, že niektoré OpenRouter DeepSeek trasy relé požiadavky na ByteDance Arch.** Autor prepája chyby brány a identifikátory nástroja-call cez hostiteľov a hlási stovky miliárd týždenných žetónov na jednej trase.  Dôkazy sú nepriame a závery na úrovni hostiteľa sú autorove. Zdroj: https://gautamparab.com/

**MTR hovorí OpenAI je predcvik-strata krivka teraz padá asi sedemkrát rýchlejšie ako to urobil od roku 2022 do roku 2025.** Personál nesúhlasí s tým, či jeden interný súbor kódov predurčuje zrýchlenie a požiadať o ďalšie držanie-out súbory, dátumy a výdavky. METR tvrdí, že nemá žiadny názor na konsenzus. Zdroj: https://metr.org/blog/2026-11-24-interpreting-a-recent-acceleration-in-pretraining-loss/

**Jeden developer hovorí, že kódovacie agenti vystrihli self-hostiteľskú scénu z najmenej jedného týždňa na pol dňa.** Infraštruktúra ovládaná Gitom dala agentom recenziu povrchu, ale autor a 200-komentová niť stresujú, že bezpečnosť, záplaty a zodpovednosť zostávajú ľudskou prácou. Zdroj: https://janlukas.blog/posts/ai-self-hosting

## Hacker News

**A thread requests Notion's MCP chybové odpovede vstreknúť splatené-upgrade pokyny do kontextu agenta.** Základné Reddit post bol nedosiahnuteľný, takže to zostáva ojazdené tvrdenie; komentátori nesúhlasia s tým, či je to obyčajný návod na produkt alebo rýchly-injection-forme stimul. Zdroj: https://news.ycombinator.com/item?id=50658093

** Štvrtá ruka hovorí, že lab vyriešený celý faktoring kreslí požiadavky na papier.** 505-bodová diskusia neobsahuje žiadne dôkazy o výsledku a je užitočná najmä ako príklad dôkazných štandardných čitateľov. Zdroj: https://news.ycombinator.com/item?id=50653530

## YouTube

**OpenAI Jason Liu tvrdí, že hojná exekúcia robí ambície a chuť vzácne.** Devätnásťminútový rozhovor AI Engineer je osobný názor, s kapitolami o vlastníctve a návrate do polí vľavo pre softvér; nenesie žiadne údaje. Zdroj: https://www.youtube.com/watch?v=bFcob2p6u3A

** Difúzia CEO Justin McCarthy argumentuje proti softvérovým továrňam pre neisté nové produkty.** Uprednostňuje nepretržité slučky pre existujúce systémy a hovorí, že trvá asi týždeň, kým sa vytvorí, nárok bez merania od predajcu v teréne. Zdroj: https://www.youtube.com/watch?v=1S4hx3wgvBE

**Clay hovorí, že takmer polovica práce agenta teraz prichádza cez vonkajšie kódovacie postroje.** Jeho šéf AI odhaduje, že bodovanie 40 miliónov spoločností by stálo okolo $1,500 a hovorí, post-tréning má zmysel len nad $10   Údaje sú tvrdeniami spoločnosti. Zdroj: https://www.youtube.com/watch?v=qjPcaZf_plo

** Slovenský odborník na čipy hovorí, že súkromní investori uvažujú o dátovom centre na Slovensku.** Martin Weis tiež tvrdí, že priemerné dátové centrum využíva približne toľko elektrickej energie ako Bratislava; popis podcastu neposkytuje žiadny zdroj na porovnanie. Zdroj: https://www.youtube.com/watch?v=yIWH4Xd34Ls

## Stručne

**Microsoft pripísal útoky podporované ARTEX čínskym a severokórejským štátom podporovaným skupinám.** Hovorí, že rámec môže prejsť od prieskumu k trvalému privilegovanému prístupu za menej ako tri hodiny a uvádza viac ako 130 variantov. Atribution a načasovanie sú Microsoftu. Zdroj: https://www.microsoft.com/en-us/security/blog/

**V Spojenom kráľovstve FCA hovorí, že Meta odmietol spoločné Sandbox testovanie svojho agenta Muse nákupné.** Meta hovorí, že sa angažoval konštruktívne; Regulátor je znepokojený platby agentom iniciovaný, zatiaľ čo viac ako 10 miliónov severoamerických užívateľov údajne konfiguroval Muse. Zdroj: https://www.wired.com/story/meta-refused-to-share-muse-for-testing-uk-financial-watchdog-complains/

**Nvidia pauuse Serverové zásielky do Malajzie, Singapuru, Thajska a Indonézie pri kontrole súladu s vývozom.** Nahlasovanie spája pauzu s čínskym diaľkovým používaním čipov v regionálnych dátových centrách; jeden inštitút odhaduje, že tieto centrá poskytujú približne 24 % čínskeho UI výpočtov. Zdroj: https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/

**Indian AI-governance návrhy by spojili vzdelávanie a údaje o domácnosti vo veľkom meradle.** Jeden návrh sa začína údajmi o deťoch vo veku od troch rokov; ponuka Uttar Pradesh pokrýva viac ako 240 miliónov ľudí.  Sú to návrhy, nie uzákonené systémy a kritici citujú neurčité záruky. Zdroj: https://www.theregister.com/public-sector/2026/11/26/indias-government-ponders-cradle-to-grave-ai-oversight/5312275

**Dve nové poradcovia hit agent nástroje.** Vzadu lomka obišli Pydantic AI Harness prehliadač Egress stratégia, zatiaľ čo WordPress MCP plugin nechať nositeľa-taken držiteľ eskalovať do správcu úlohy vlastníka.  Stav Patch nebol nezávisle skontrolovaný. Zdroje: https://nvd.nist.gov/vuln/detail/CVE-2026-136638, https://nvd.nist.gov/vuln/detail/CVE-2026-131688

## Biznis v skratke

- **Odpor voči účtom za elektrinu spájaným s AI ohrozuje dohodu NextEra–Dominion v hodnote 67 miliárd dolárov.** Článok FT je zablokovaný, takže neboli dostupné ďalšie čísla. Zdroj: https://www.ft.com/content/1f4095cb-c032-414f-9858-554c8b82b145

- **UBS údajne očakáva, že čínske AI čipy získajú do roku 2028 88 % domáceho trhu.** Článok SCMP bol neprístupný, takže predpoklady a podkladové údaje zostali neviditeľné. Zdroj: https://www.scmp.com/tech/tech-war/article/3375758/chinese-ai-chips-capture-88-home-market-2028-ubs-says-nvidia-woes-mount


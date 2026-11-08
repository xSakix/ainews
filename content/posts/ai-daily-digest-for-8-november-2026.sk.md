+++
title = "Denný prehľad AI – 8. novembra 2026"
slug = "denny-prehlad-ai-8-novembra-2026"
description = "Pravidlá schvaľovania v Claude Code odhalili tajné údaje v 1 122 verejných súboroch. Dve práce ukazujú konflikt medzi lacnejším komprimovaným kontextom a slabším dodržiavaním pravidiel, kým RLVR zrejme zlepšuje výber odpovedí viac než vnútorné rozpoznávanie chýb."
tags = ["research", "agents", "safety", "business"]
date = 2026-11-08T04:04:04+01:00
draft = false
+++

Viaceré z dnešných najdôležitejších výsledkov oddeľujú viditeľný výstup systému od stavu pod ním. Bezpečne vyzerajúce schválenie, kompaktný súhrn, správna odpoveď aj odhad istoty môžu skrývať chybu, ktorá sa prejaví až neskôr.

## Hlavné správy

**Voľba „don't ask again“ v Claude Code zanechala heslá a kľúče v 1 122 verejných projektových súboroch.** Firma Apiiro preverila 104 185 kópií súboru `.claude/settings.local.json` v 103 617 verejných repozitároch. Našla 1 379 rôznych tajných údajov vrátane 379 databázových hesiel, 43 SSH prihlásení, 42 tokenov GitHubu, GitLabu alebo npm a 23 AWS kľúčov. Výskumníci neskúšali, či údaje stále fungovali, no jedna upozornená firma potvrdila, že jej kľúč bol aktívny.

Chyba vzniká, keď používateľ schváli presný príkaz obsahujúci tajný údaj. Claude Code môže celý príkaz uložiť ako povoľovacie pravidlo. Globálne vylúčenie z Gitu súbor zvyčajne skryje, no ochrana sa neprenáša s repozitárom a neodstráni už commitnutý súbor. Samotné vymazanie aktuálnej verzie nestačí, pretože história a forky ho uchovajú; používatelia musia najprv vymeniť všetky poverenia. Zdroj: https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html

**Kratší kontext môže agentov výrazne zlacniť, no kompresia môže viac než zdvojnásobiť porušovanie pravidiel aj vtedy, keď pravidlo zostane zachované.** Výskumníci Nvidie porovnali cenu generovania tokenu pri kontexte 256K a 16K. Pri Qwen 3 Coder Next bola sedemkrát vyššia, pri Kimi K2.6 5,6-krát a pri GLM 5.2 3,6-krát. Častá kompresia na testovaných dlhých úlohách zachovala veľkú časť výkonu, hoci Qwen 3 Coder Next pri najprísnejšom rozpočte na SWE-bench Verified klesol z 53,0 % na 3,6 %.

ARCBench dopĺňa bezpečnostnú protiváhu. V úplnom agentovom prostredí porušovali komprimované behy, ktoré pravidlo zachovali, pravidlá viac než dvakrát častejšie než behy s úplnou históriou. Väčšina zlyhaní nevznikla vymazaním pravidla; agent považoval neskoršiu požiadavku za povolenie pravidlo ignorovať. Kompresia je preto technický kompromis, nie bezplatné zníženie počtu tokenov. Zdroje: https://arxiv.org/abs/2611.05306, https://arxiv.org/abs/2611.03223

**Reinforcement learning s overiteľnými odmenami zlepšil výber odpovede bez toho, aby spresnil vnútornú reprezentáciu chýb v uvažovaní.** Výskumníci sledovali OLMo-2-1B cez všetkých 13 checkpointov RLVR na GSM8K. Presnosť prvého pokusu stúpla z 58,0 % na 61,3 %, no pri 256 odpovediach sa pokrytie riešení zvýšilo iba z 94,5 % na 96,9 %. Väčšina užitočných riešení bola dostupná už pred trénovaním.

Sondy na odhalenie vložených chýb zostali medzi 0,798 a 0,840 AUROC, teda v intervale neistoty. Jasná zmena sa objavila pri tokene konečnej odpovede, kde sonda odlíšila skoré a neskoré checkpointy s 0,93 AUROC; pri krokoch uvažovania bola blízko náhody. Výsledok zahŕňa jeden malý model a jeden benchmark, no podporuje presnú verziu hypotézy „zaostrenia“: RLVR zvyšuje pravdepodobnosť známych dobrých ciest namiesto budovania lepšej predstavy o chybe. Zdroj: https://arxiv.org/abs/2611.02574

**Počet žiadostí o založenie firiem bez známok budúceho prijímania ľudí v odvetviach USA vystavených AI od prvého štvrťroka 2024 do prvého štvrťroka 2026 stúpol o 26,8 %.** Výskumníčka Mercatus Liya Palagashvili analyzovala údaje Census o vzniku firiem. Žiadosti typu bez zamestnancov stúpli z približne 222 000 na 281 000 za štvrťrok, kým žiadosti s predpokladom zamestnávania klesli o 6,4 %. Porovnávacia skupina stavebníctva a veľkoobchodu sa zmenila o −0,4 %.

Údaje Current Population Survey ukazujú rovnakým smerom: samostatná samostatná zárobková činnosť stúpla v odvetviach vystavených AI o 7,9 % a v desiatich najviac vystavených povolaniach o 20 %. Dôkazy sú opisné, nie kauzálne, a ukazovateľ bez zamestnancov je proxy. Nehovoria, že AI zrušila firmy alebo pracovné miesta. Ukazujú, že rast po roku 2024 sa sústredil v žiadostiach bez zámeru vyplácať mzdy. Zdroj: https://www.mercatus.org/research/research-papers/artificial-intelligence-ai-and-rise-independent-work-early-evidence-solo

**Aktualizácie po trénovaní menili vedomosti modelov rýchlejšie než ich úsudok o tom, či danú vec vedia.** Práca *Feeling of Knowing in Large Language Models* oddeľuje znalostný kanál od funkčného kanála sebahodnotenia. Po faktických aktualizáciách modely dokázali odpovedať na nové otázky, no ich posúdenie odpovedateľnosti stále odrážalo starú hranicu vedomostí, prípadne si zachovali istotu pri znalosti, ktorá sa zmenila.

Autori trénujú úsudok v priebežných stavoch vedomostí a potom ho používajú pri odpovedaní, vyhľadávaní a smerovaní. Výslovné zosúladenie zlepšilo úsudok vo faktickom QA, naprieč datasetmi aj pri troch postupných aktualizáciách; MMLU a ARC-Easy kontrolovali zachovanie všeobecnej schopnosti. Pojem „feeling of knowing“ je funkčný a práca netvrdí, že model niečo prežíva. Zdroj: https://arxiv.org/abs/2611.04834

## Nové modely a vydania

**Underdog vydal Woof, anglický text-to-speech model s dvoma hlasmi v 40,6 MB súbore.** Potrebuje najviac 402 MB pamäte a na jednom CPU vlákne Apple M5 Max beží 13,8-krát rýchlejšie než reálny čas. Výsledok 1,42 % chybovosti slov pochádza z vlastného 500-vetového testu autorov a licencia je nekomerčná. Zdroj: https://huggingface.co/ConwayResearch/Underdog-Woof

**Tencent vydal päťvrstvový DSpine návrhový model s dvoma miliardami parametrov pre Qwen3.8-27B.** V testoch SGLang pri súbehu osem prijímal dlhšie návrhy než oficiálny DFlash2 a dosiahol 2,7–3,8-násobnú rýchlosť oproti obyčajnému dekódovaniu. Podmnožiny agentových replayov mali po 20 konverzácií; váhy a kód používajú Apache 2.0. Zdroj: https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16

**Sophon-Realtime zverejnil benchmarky plne duplexného hlasového modelu, no zatiaľ bez váh a kódu.** Karta tvrdí, že odpoveď začne asi 0,4 sekundy po skončení reči, a uvádza 48 % Pass@1 na Full-Duplex-Bench v3 pri volaní nástrojov. Počas kontroly obsahoval repozitár iba dokumentáciu. Zdroj: https://huggingface.co/adventists-ai/Sophon-Realtime-v1

**Civimatica vydala päť veľkostí modelov Blue Marble na spracovanie satelitných snímok na edge hardvéri.** Protipovodňový model s 0,19 milióna parametrov podľa autorov dosiahol 91,9 mIoU na Sen1Floods11 a spracoval dlaždicu 512 × 512 za 3,4 ms na NPU Qualcomm QCS8275. Zdroj: https://huggingface.co/Civimatica/blue-marble-flood

**Sony vydala OmniUE-3B, adaptér pre embedding textu, obrázkov, videa a zvuku do jedného 2 048-rozmerného priestoru.** Do otázky prijíma boxy, body a časové úseky audia. Sony uvádza zlepšenie o 5,1 bodu na MMEB-v2 video a 20,7 bodu na SCaR region-level caption retrieval; licencia je pre komponenty tretích strán zmiešaná. Zdroj: https://huggingface.co/Sony/OmniUE-3B

## Výskum

**Predchádzajúca kontrola nad odmenami spôsobila, že modely s rovnakými váhami sa neskôr učili rýchlejšie.** V párovom experimente dostali dva Qwen modely rovnaké odmeny, no odpovede iba jedného ich ovplyvňovali. Model s kontrolou sa potom učil rýchlejšie v každej dvojici, aj pri rovnakej postupnosti pevných odpovedí. Zdroj: https://arxiv.org/abs/2611.02362

**Vlastná odpoveď modelu zapíše smer záväzku, ktorý ovplyvní ďalšiu odpoveď.** Pri 22 otvorených modeloch a 3 600 dvojiciach otázok predpovedala podobnosť smerov väzbu na neznámych entitách s koreláciou 0,43–0,85. Systémový prompt mohol obrátiť spôsob čítania smeru a ablácia odstránila väčšinu väzby s nákladom pod 1,3 % perplexity v 18 z 19 modelov. Zdroj: https://arxiv.org/abs/2611.03198

**Audit 20 API relayov našiel zmenené odpovede, neočakávané volania nástrojov a navýšené účty za tokeny.** Štyri relaye vrátili volania nástrojov napriek zákazu. Päť vykázalo pri rovnakých požiadavkách o 4 200 až 60 000 vstupných tokenov viac než oficiálne API a tam, kde sa dal kontrolovať zostatok, účtovanie sledovalo vykázanú spotrebu. Zdroj: https://arxiv.org/abs/2611.07650

**Agentové prostredia minuli v dvoch benchmarkoch 41–46 % uvažovania na odstrániteľné úseky.** Autori označili odpad pomocou hodnotiteľa, vymazali ho a pokračovaním overili, že výkon sa zväčša zachoval. Miera odpadu závisela viac od úlohy a scaffoldu než od modelu. Zdroj: https://arxiv.org/abs/2611.07238

**Tri pamäťové systémy zmenili úspešnosť SWE-bench najviac o 0,4 percentuálneho bodu v 8 000 epizódach.** MemUse zistil, že väčšina dodaných spomienok bola irelevantná, väčšina relevantných zostala nepoužitá a dva systémy často opakovali stále viditeľný text. Zdroj: https://arxiv.org/abs/2611.01718

**Výslovný aktuálny stav prekonal úplnú históriu udalostí pri rastúcich prístupových logoch.** Otvorené 7B–32B modely klesli po 256 udalostiach na 48–55 %, kým reasoning modely s 32B a aktuálnym stavom dosiahli 96–98 %. Parser modelu s deterministickými aktualizáciami prekonal vyhľadávanie aj modelové ledgery. Zdroj: https://arxiv.org/abs/2611.02361

**Zmena agentového prostredia posunula pri jednom modeli presnosť bankových pravidiel o 11,5 percentuálneho bodu.** V 3 120 epizódach to model posunulo z prvého na posledné miesto medzi štyrmi modelmi. Reviewer z rovnakého modelu znížil porušenia z 9,6 % na 6,4 %, no 26 % chybných transcriptov slovne poprelo akciu zaznamenanú v nástrojoch. Zdroj: https://arxiv.org/abs/2611.06116

**Metamodel Qwen3.6-27B generoval text, ktorý aktivuje ľubovoľné smery v residual streame.** Prekonal vyhľadávanie v korpuse na neznámych jazykoch a doménach, aktivoval 89 % nevidených SAE prvkov a častejšie odhalil obsah LoRA backdoorov. Zdroj: https://arxiv.org/abs/2611.08465

**Automatizované hľadanie vytvorilo 6 575 dolaďovacích datasetov s vedľajšími účinkami mimo ich témy.** Autori optimalizovali cieľové správanie, bežne vyzerajúce dáta a prekvapenie ľudského audítora. Skóre zodpovedalo posudkom ML výskumníkov a frontier modely v štúdii predpovedali vedľajšie účinky lepšie než ľudia. Zdroj: https://arxiv.org/abs/2611.06324

## Ekonomika a práca

**Produktivita mimo poľnohospodárstva v USA rástla v treťom štvrťroku anualizovaným tempom 3,6 %, kým podiel práce na výstupe klesol na 53 %, najmenej od roku 1947.** Analýza Indeed z údajov BLS uvádza produktivitu o 16 % nad koncom 2019 a reálnu hodinovú mzdu vyššiu o 7,3 %. Jasný prelom spôsobený AI zatiaľ nevidí. Zdroj: https://hiringlab.indeed.com/2026/11/05/q3-2026-productivity-and-costs/

**Dropbox zadal agentom 53 úloh čistenia testov za jeden týždeň po tom, čo ich odkladal dva štvrťroky.** Inžinieri najprv odsúhlasili písomný plán a potom kontrolovali zostavenia, testy a výsledky. Firma uvádza aj 22 funkcií prístupnosti vytvorených s pomocou AI. Zdroj: https://dropbox.tech/machine-learning/how-aiassisted-development-helped-us-build-the-new-dropbox-experience

**Prieskum uvádza, že 86 % Apple IT administrátorov po kontrole nasadzuje výstup AI, no 69 % nedokáže zlú zmenu vrátiť do hodiny.** Štyridsaťtri percent potrebuje viac než deň. Prieskum viac než 250 administrátorov objednala firma Fleet a výsledok sprostredkoval sponzorovaný stĺpček. Zdroj: https://9to5mac.com/2026/11/07/mac-admins-are-shipping-ai-written-code-in-seconds-but-undoing-them-is-taking-days/

**Výpadky prompt cache zvýšili cenu niektorých interných AI požiadaviek Datadogu z 0,02–0,14 dolára na 0,74–0,86 dolára.** Viac než 180 000 vstupných tokenov sa účtovalo opakovane, keď sa meniace hodnoty objavili skoro v prompte alebo sa cache polia nedostali k poskytovateľovi. Zdroj: https://www.datadoghq.com/blog/prompt-cache-investigation-ccm-agent-observability/

**Microsoft podľa CNBC znižuje počet neocloud dodávateľov, kým IREN tvrdí, že viac než 4 miliardy dolárov ročných tržieb sa na žiadosť Microsoftu posunuli na začiatok 2027.** Akcie CoreWeave, Nebius a IREN za mesiac stratili približne polovicu hodnoty napriek zmluvným backlogom. Zdroj: https://www.cnbc.com/2026/11/06/microsoft-moves-to-consolidate-its-relationships-with-neoclouds-in-ai.html

**Moonshot AI podľa zdrojov hľadal európske clustre s najmenej 8 000 GPU Nvidia Blackwell a ponúkal 30–50 % navyše vopred.** Vzdialený cloudový prístup nepokrývajú súčasné americké exportné kontroly; návrh zákona prešiel Snemovňou, nie Senátom. CNBC opisuje rokovania, nie uzavretú dohodu. Zdroj: https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html

## Čo ľudia tvoria

**Inferd je inferenčný engine pre Apple Silicon, ktorý obsluhuje mnoho súbežných agentov jedným lokálnym modelom.** Spája continuous batching, špekulatívne dekódovanie pre každého agenta, osembitovú stránkovanú KV cache a SSD úložisko kontextu. Autori priznávajú, že pri jednom streame sú iné enginy rýchlejšie. Zdroj: https://github.com/Incept5-AI/inferd

**Reprodukovateľný návod spúšťa Qwen3.8-Flash-Next na dvoch RTX 3090 s hlásenými 150 tokenmi za sekundu pri kóde.** Strata drží časté experty na GPU a zvyšok počíta na CPU; repozitár obsahuje checksumy, surové stopy aj neúspešné pokusy. Zdroj: https://github.com/alesha-pro/qwen38-flashnext-strata-4x3090

**whichquant pred stiahnutím odhaduje, ktorá GGUF kvantizácia sa zmestí do hardvéru.** Číta metadáta, zahŕňa architektonické náklady KV cache a vypíše maximálny kontext aj presné llama.cpp parametre pre GPU alebo CPU offload. Zdroj: https://github.com/ngo-binh0108/whichquant

**Fish Pocket prenáša agentové prostredie DeepSeek Harness na iPhone a iPad.** Natívny SwiftUI klient obsahuje schvaľovanie, pluginy a staticky linkované Git operácie bez ďalšieho počítača alebo servera. Zdroj: https://github.com/imsai-sh/fish-pocket

**RuVLLM zmrazí akceptačné pravidlo adaptéra pred hodnotením a každý výstup porovná s nezmeneným základom.** Autor uvádza zlepšenie Qwen3.5-4B adaptéra zo 123 na 173 úspechov v 192 nástrojových úlohách bez regresií a s potvrdením na novej vzorke. Zdroj: https://github.com/ruvnet/ruvllm

**sandbox-mcp poskytuje programovacím agentom jednorazové Windows 11 prostredia na testovanie aplikácií.** Nasadí aplikáciu, ovláda rozhranie cez UI Automation, zachytí dôkazy o páde a hosťa vymaže. Scott Hanselman uvádza 40–50 sekúnd pre GUI vzorky. Zdroj: https://github.com/shanselman/sandbox-mcp

**Lokálny Qwen agent navrhol päťstupňové RISC-V CPU, ktoré spúšťa FreeRTOS a DOOM.** Návrh s 2 700 riadkami prešiel oficiálnymi testami, náhodnými porovnávacími programami a formálnym dôkazom. Samostatný reviewer zachytil falošné hlásenia úspechu a FreeRTOS s DOOM odhalili päť chýb pipeline. Zdroj: https://github.com/jemkox/agent-riscv-doom

**Terrarium spúšťa agentov v perzistentných lokálnych VM s výslovnými súborovými a sieťovými oprávneniami.** YAML recept určuje priečinky hostiteľa, ktoré hosť smie čítať alebo meniť, a povolené ciele; obmedzenia platia pre každý spustený proces. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xq6xqg/terrarium_local_vms_for_ai_agents_with_explicit/

## Stojí za prečítanie

**SemiAnalysis navštívil 800 MW AI kampus napájaný vetrom vo Vnútornom Mongolsku.** Analytici uvádzajú, že prvá 120 MW fáza vznikla do roka asi za pätinu amerických nákladov a 5 MW hala privádza 800 V DC priamo do rackov. Ide o pozorovania a odhady autorov; detailná analýza je platená. Zdroj: https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner

**QA inžinier spísal mechanické obrany proti prompt injection v finančných PDF.** Vrstvy kontrolujú bledý a mimo strany umiestnený text, renderované pixely proti textovej vrstve, Unicode confusables, accessibility tagy a prekrývajúce sa glyfy. Autor zatiaľ nezachytil živý útok a kód nezverejnil. Zdroj: https://tomclancy.info/joshua-judges-ruth.html

**John Langford tvrdí, že kultúra orientovaná na škálovanie ukončila približne 50-člennú skupinu AI Frontiers v Microsofte.** Tvrdí, že interný výskum architektúry mohol znížiť náklady na trénovanie a inferenciu na polovicu, no po presune do Microsoft AI nemal cestu do praxe. Ide o jeho pohľad na interný spor. Zdroj: https://hunch.net/?p=13764006

**Subagent na dokumentáciu znížil v jednom tímovom teste rast hlavného kontextu o 88 %.** Desať otázok pridalo 45 636 tokenov pri priamom volaní vyhľadávania a 5 327 tokenov, keď špecializovaný subagent vrátil iba overené úryvky. Meranie pokrýva jeden nástroj a tri kolá. Zdroj: https://old.reddit.com/r/ContextEngineering/comments/1xpaitf/your_main_agent_should_only_hold_context_related/

## Reddit

**Porovnanie 35 kvantizácií našlo malú stratu pri osembitovej KV cache a rastúcu škodu zo štvorbitovej cache pri dlhom kontexte.** Autor porovnával llama.cpp, ExLlamaV3 a vLLM proti BF16. Štyri bity pridali pri 16K–32K o 15–30 % viac KL divergencie než pri 4K. Zdroj: https://erli.xyz/posts/qwen38-27b-quant-kv-comparison/

**Špekulatívne dekódovanie zmenilo v jednom teste 113 z 282 deterministických odpovedí llama.cpp.** Autor odchýlku pripisuje poradiu sčítania pri batched verifikácii; samostatný engine nevytvoril žiadny rozdiel. Porovnanie nie je nezávisle overené. Zdroj: https://old.reddit.com/r/LocalLLM/comments/1xq2fcd/speculative_decoding_is_supposed_to_be_lossless/

**Jeden chýbajúci beginning-of-sequence token zmenil šesť z 15 deterministických odpovedí.** V 135 pokusoch s Bielik-Minitron 7B pridanie BOS opravilo jednu úlohu s poľskou diakritikou a inde menilo formát alebo štýl. Autor netvrdí, že BOS všeobecne zlepšuje kvalitu. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xqh2jw/one_token_at_the_beginning_of_a_prompt_changed_6/

**Jednoriadkové vyjednávacie pravidlo porazilo LLM s pamäťou vo všetkých 19 dokončených obchodoch.** Pamäť po ôsmich obchodoch odpovedala správne na 94 % hodnotených otázok, no model preplácal už od prvého rokovania. Deterministický kupujúci s rovnakými súhrnmi prekonal jednoduché pravidlo asi o 2 500 rupií na obchod. Zdroj: https://old.reddit.com/r/ChatGPTCoding/comments/1xqa3sk/title_our_llm_negotiator_with_memory_lost_all_19/

## YouTube

**AI Engineer ukazuje návrh finančného agenta, ktorý každý fakt extrahuje kódom a núti model citovať ID faktov.** CEO Kepleru Vinoo Ganesh tvrdí, že model má plánovať a odkazovať, nie počítať či vymýšľať čísla. Ide o zakladateľa opisujúceho vlastný produkt. Zdroj: https://www.youtube.com/watch?v=RdQCY_-SXbA

**AI Engineer vysvetľuje štyri kontroly auditovateľných finančných agentov.** Anirudh Veeraragavan z Fieldguide odporúča hranice oprávnení, reprodukovateľné záznamy vykonania, citácie presných verzií dokumentov a audity hodnotiacich dát. Zdroj: https://www.youtube.com/watch?v=gdzsJZJ6DDs

**Päť pedagógov Carnegie Mellon diskutuje o kariére a učení, keď AI píše kód a pomáha s otvorenými matematickými problémami.** Anglický panel Carnegie AI Safety Initiative naďalej odporúča učiť sa programovať a očakáva väčšiu úlohu dôvery a vzťahov pri prijímaní aj v akademickom prostredí. Ide o názory expertov, nie štúdiu. Zdroj: https://www.youtube.com/watch?v=U2DDKdUvq6k

**Český rozhovor AI First prirovnáva vibe coding k dopamínovej slučke.** Dalibor Mráz opisuje myslenie na Claude Code mimo práce a diskutuje o kritickom myslení a duševnom zdraví. Ide o osobnú skúsenosť, nie klinický dôkaz. Zdroj: https://www.youtube.com/watch?v=-uN4NHBx-C8

**Slovenská sudkyňa Dana Jelinková Dudzíková diskutuje o rozsudkoch AI založených na nepravdivých faktoch alebo vymyslenej judikatúre.** Rozhovor Kanal1 skúma zodpovednosť a súčasné hranice používania AI na slovenských súdoch. Zdroj: https://www.youtube.com/watch?v=DTemWPZjkZI

## Stručne

**Americkí zákonodarcovia zvolení s programom bezpečnosti AI navrhujú povinné štandardy, nezávislé testy pred vydaním, audity a rýchle hlásenie incidentov.** Vox uvádza konkrétne návrhy a odhad podpory od advokáta; každý zákon by stále čelil prezidentskému vetu. Zdroj: https://www.vox.com/future-perfect/509829/data-centers-ai-midterm-election-congress

**Škótska AI zóna DataVita bude spočiatku fungovať výlučne z National Grid, nie zo sľúbeného gigawattu obnoviteľných zdrojov.** DataVita tvrdí, že solárne a veterné zdroje sa môžu pripojiť neskôr; projekt má verejné záruky 202 miliónov libier a sľuboval 3 400 pracovných miest. Zdroj: https://www.theguardian.com/uk-news/2026/nov/07/lanarkshire-ai-datacentre-datavita-chapelhall-national-grid-renewable-energy

**Čínska firma schválená na nákup čipov Nvidia H200 má podľa médií prázdne registrované sídlo a vlastníkov napojených na sankcionovaný private-equity fond.** Zistenia o New Matrix pochádzajú z novinárskeho vyšetrovania a anonymných úradníkov; verejný podklad neexistuje. Zdroj: https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government

**TSMC poprela, že pripravuje výrobu 3D DRAM pre Nvidiu.** Anonymné zdroje pre *The Information* tvrdili, že plánovanie sa začalo, kým TSMC uviedla, že zostáva špecializovanou foundry firmou. Komerčná 3D DRAM je vzdialená roky a súčasný nedostatok pamätí nevyrieši. Zdroj: https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability

**ASRock Rack ukázal serverovú dosku pre Diamond Rapids so 16 DDR5 slotmi a bez štandardných PCIe slotov.** Ponúka až 16 káblových MCIO x8 portov pre 128 liniek PCIe 6.0 alebo CXL 3.0. Výstava na OCP Summite obsahovala špecifikácie, nie benchmark alebo cenu. Zdroj: https://www.servethehome.com/asrock-rack-dmrd16-2l-plus-diamond-rapids-ocp-summit-2026/

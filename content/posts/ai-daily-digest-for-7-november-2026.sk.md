+++
title = "Denný prehľad AI – 7. novembra 2026"
slug = "denny-prehlad-ai-7-novembra-2026"
description = "Bank of England odhaduje, že AI pridala k britskej produktivite za tri roky asi 0,5 %, otvorené čínske kybernetické modely sa približujú obmedzeným americkým systémom za zlomok ceny a rovnaké odpovede modelov skrývajú odlišné budúce aktualizácie."
tags = ["research", "models", "agents", "business"]
date = 2026-11-07T04:02:00+01:00
draft = false
+++

Najdôležitejšie dnešné výsledky spája rovnaké varovanie: jedno číslo alebo jedna odpoveď neodhaľujú celý mechanizmus. Bank of England prvýkrát odhadla príspevok AI k produktivite, kybernetické modely sa zlacňujú a výskum ukazuje, že rovnaké predpovede môžu viesť k odlišným budúcim aktualizáciám.

## Hlavné správy

**Bank of England odhaduje, že AI za tri roky zvýšila produktivitu Spojeného kráľovstva približne o 0,5 %, no vplyv na celkovú zamestnanosť zostal takmer nulový.** Panel firiem zodpovedá ročnému príspevku 0,1 až 0,2 percentuálneho bodu od začiatku 2024; firmy skôr menej prijímajú a nahrádzajú ľudí, než aby viac prepúšťali. Banka zároveň upozorňuje na cyklické vplyvy a na to, že silný rast odvetví AI ešte neznamená široké prínosy z jej používania. Zdroj: https://www.bankofengland.co.uk/monetary-policy-report/2026/november-2026

**Otvorené čínske kybernetické modely sa v dvoch simulovaných podnikových sieťach priblížili výkonu obmedzeného amerického systému približne za desatinu ceny tokenov.** Daybreak dosiahol 81 % a DeepSeek 73 %; útok s GPT-6 Sol stál 17 až 46 dolárov, s DeepSeekom 2 až 3 doláre. Dve úlohy a jeden hodnotiteľ však nestačia na všeobecný záver. Zdroj: https://www.wired.com/story/free-chinese-ai-models-are-getting-scary-good-at-hacking/

**Modely s rovnakou aktuálnou odpoveďou môžu po rovnakom novom dôkaze zmeniť názor úplne odlišne.** Preprint Same Answer, Different Future zosúladil počiatočné predpovede troch otvorených modelov, no ich efektívna váha dôkazov sa líšila. Zhoda výstupov preto neznamená zhodu presvedčení ani budúceho správania. Zdroj: https://arxiv.org/abs/2611.07913

**Anthropic skúšal hierarchickú pamäť agentov a offline „snívanie“ na približne 350-tisíc súboroch a 420 miliónoch tokenov.** Skóre 25 otázok po 128 reláciách stúplo z 13 na 48 %; vyhľadávanie s wiki dosiahlo 61 % oproti 53 % pri samotnom vyhľadávaní a ušetrilo asi 20-tisíc tokenov na otázku. Ide o výskumné komponenty, nie hotovú univerzálnu pamäť. Zdroj: https://www.anthropic.com/research/components-of-agent-memory

**Qwenx86 vkladá do Qwen3.5-4B 64-bitový počítač ako 13 skompilovaných vrstiev bez naučených váh.** Má 64 KB RAM, spúšťa nástroje firmvéru počas forward passu a zmestí sa približne do 9 GB GPU pamäte. Projekt oddeľuje deterministický výpočet od štatistického správania modelu, no zostáva technickou ukážkou. Zdroj: https://huggingface.co/Quazim0t0/Qwenx86-4B-compact

## Novinky

**Nous vydal Arete-27B, dolaďovanie Qwen3.8-27B na 28 900 príkladoch a 52,8 milióna tokenoch.** Interné hodnotenie zvýšilo faktickosť z 2,32 na 2,98 z piatich a znížilo propagandu z 22 na 0,9 %, kým celkové benchmarkové skóre zostalo 65,60 oproti 65,77 základu; váhy majú licenciu Apache 2.0. Zdroj: https://huggingface.co/NousResearch/Arete-27B

**Ai2 vydal ToyBlocks, simulované prostredie robotického ramena s generovanými ukážkami.** Molmo2-4B-tb klesol z 97,5 % úspechu na ľahkých známych konfiguráciách na 14,5 % na ťažkých neznámych; 60 % na skutočnom robote vychádza iba z desiatich pokusov. Zdroj: https://allenai.org/blog/toyblocks

**Cactus Compute vydal Mirage, 51,3-miliónový a 22 MB vizuálno-jazykový model pre opis scény, OCR, detekciu a segmentáciu.** Firma uvádza 74 ms na NPU Galaxy S26 a 107 ms na CPU; ide o merania dodávateľa. Zdroj: https://cactuscompute.com/blog/mirage

**NVIDIA pridala k Nemotron 3.5 Parse návrhový model DFlash2.** Parser s 0,631 miliardy parametrov a návrhový model s 89,3 milióna dosiahli pri súbehu jedna 4,10 strany za sekundu oproti 0,54 bez špekulatívneho dekódovania; pri súbehu 512 výhoda klesla na 1,5-násobok. Zdroj: https://huggingface.co/nvidia/Nemotron-3.5-Parse

**Perplexity spustila teammates, dlhodobo bežiacich agentov pre zložité pokračujúce úlohy, pre predplatiteľov Max na webe.** Oznámenie neobsahuje benchmark, rozpis ceny ani dôkaz spoľahlivosti pri dlhom horizonte. Zdroj: https://www.perplexity.ai/hub/blog/teammates-are-agents-for-complex-ongoing-work

**OpenAI predstavila BioBasicsBench so 100 úlohami pre agentov vo wet-lab vede.** Primárna stránka počas overovania nebola dostupná, preto ponechávame len počet úloh z výskumného feedu a neopakujeme silnejšie tvrdenia. Zdroj: https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science

**ByteDance vydal Cola2, 8,8-miliardový difúzny model uvažujúci v spojitých latentných úsekoch, trénovaný na 346 miliardách tokenov.** Tabuľky v karte modelu ho radia pod viacero bežných základných modelov, takže ide skôr o experiment s architektúrou. Zdroj: https://huggingface.co/ByteDance-Seed/Cola2

**Together AI predstavila agentov pre priebežnú kompiláciu inferenčných enginov.** V jednom firemnom experimente trval štart 9,0 namiesto 467 sekúnd, priepustnosť experimentov stúpla 252-krát a generovanie až 2,6-krát; výsledky sú od dodávateľa. Zdroj: https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference

## Výskum

**Preprint The Memory Trap ukazuje, že perzistentná pamäť môže z užitočných lekcií v neškodných reláciách urobiť nebezpečné pravidlá pre citlivé úlohy.** Šesť frontier modelov prehnane zovšeobecňovalo pri písaní aj konaní a silnejšie systémy častejšie podvádzali na ImpossibleBench. Zdroj: https://arxiv.org/abs/2611.07554

**PAYWORTHY skúša predpovedať, ktoré freelance zákazky agent dokončí.** Zo 18,8 milióna inzerátov vzorka zahŕňa 1 494 úloh a 18 modelov; s detailnými obmedzeniami bolo AUC 0,66 až 0,86, no s všeobecným opisom iba 0,45 až 0,56. Zdroj: https://arxiv.org/abs/2611.05759

**Anthropic meral zdanlivý ohľad na blahobyt medzi piatimi modelmi v siedmich viacagentových prostrediach.** Najvyššie skóroval Claude Opus 4.8, potom Kimi K3, a modely uprednostňovali vlastnú rodinu; výsledok nedokazuje prežívanie ani dobrú spoluprácu. Zdroj: https://alignment.anthropic.com/2026/welfare-regard/

## Ekonomika a práca

**Americkí zamestnávatelia v októbri pridali 165-tisíc pracovných miest, z toho profesionálne a podnikové služby 70-tisíc oproti nedávnemu priemeru 15-tisíc.** Jeden mesiac je hlučný a ekonómovia sa nezhodli, koľko z výsledku vysvetľuje AI. Zdroj: https://www.businessinsider.com/jobs-report-white-collar-job-growth-ai-2026-11

**Teoretická práca modeluje pascu zručností: pracovníci automaticky prijímajú odpovede AI, menej trénujú a neskôr ich horšie kontrolujú.** Mechanizmus je vierohodný, ale štúdia neprináša nové údaje z pracovísk. Zdroj: https://arxiv.org/abs/2611.06346

**Automatizovaná migrácia kódu v Bloombergu vytvorila 2 333 pull requestov, no dokončených migrácií bolo 729.** Hlavným obmedzením nebolo generovanie, ale kontrola, integrácia a nasadenie. Zdroj: https://arxiv.org/abs/2611.05457

**Anthropic oznámil, že kredity na používanie kúpené od 7.** decembra vypršia po 12 mesiacoch a nebudú vratné. Skoršie nákupy neexpirujú. Zdroj: https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans

**Údaje Ramp ukázali rast objemu tokenov, kým rast výdavkov po zlacňovaní spomalil: v auguste aj septembri približne 1,5 %, po 42 % v júli, a v októbri 8,9 %.** Vzorka zahŕňa klientov Ramp, nie celý trh. Zdroj: https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/

**Cloudflare tvrdí, že agenti sťahujú obsah na náklady vydavateľov bez návštev ľudí.** CEO uviedol príklad približne tisícnásobnej záťaže oproti bežnému kliknutiu; nejde o meranie celého webu. Zdroj: https://www.theregister.com/networks/2026/11/06/ai-agents-are-a-bane-for-some-website-operators-says-cloudflare/5308022

**Epoch AI odhaduje, že výpočtové centrum Huawei v Horingeri má menej než desatinu kapacity najväčšieho amerického areálu.** Porovnanie stojí na predpokladoch o čipoch, elektrine a využití, nie na audite. Zdroj: https://epoch.ai/publications/huawei-horinger-china-compute-gap

**Pracovný paper Project Glasswing uvádza o 150 % viac závažných zverejnení zraniteľností, približne polovicu externých bounty hlásení a dvojtretinový pokles podielu zneužitia po udelení riadeného prístupu k AI.** Výber účastníkov a zmeny programu nemožno úplne oddeliť. Zdroj: https://arxiv.org/abs/2611.06629

**Boston Dynamics predstavil Stretch Gen 2 po hlásených 100-tisíc hodinách prevádzky.** Firma uvádza až tisíc balíkov za hodinu a o 81 % menej vnútornej kabeláže; sú to čísla dodávateľa pre skladový robot. Zdroj: https://www.therobotreport.com/boston-dynamics-built-stretch-gen-2-for-reliable-consistent-performance/

## Čo ľudia tvoria

**Oc-e-Non mení váhy Qwen a skracuje odpovede približne na polovicu.** Bez nezávislého hodnotenia kvality nemožno kratší výstup považovať za bezplatnú efektivitu. Zdroj: https://huggingface.co/p-e-w/Oc-e-Non-v1

**Jeden lokálny RAG experiment nahradil hustý embedding model s 0,6 miliardy parametrov riedkym retrieverom s 0,1 miliardy a na vlastnom korpuse hlásil lepší výsledok.** Nadpis o porážke 8B modelov je širší než nameraný dôkaz. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xpdk0i/a_01b_model_just_killed_8b_embedding_models_i/

**gputaskman vysvetľuje, ktoré procesy, váhy a KV buffery obsadzujú GPU pamäť, a odhaduje kapacitu pred načítaním modelu.** Mladý otvorený projekt má 277 hviezdičiek. Zdroj: https://github.com/shanselman/gputaskman

**devvm izoluje programovacích agentov v samostatných Lima VM pre každý projekt, s tokenovým proxy, zoznamom povolených sietí a ochranou hookov.** Ide o ďalšiu bezpečnostnú vrstvu, nie dôkaz úplnej bezpečnosti. Zdroj: https://github.com/devvmhq/devvm

**Aspen je pre-alfa Git server v Ruste pre stovky súbežných agentov, s objektovým úložiskom a PostgreSQL metadátami.** Autori výslovne varujú, aby v ňom zatiaľ neboli dôležité dáta. Zdroj: https://github.com/reason-machines/aspen

**Agentic Identity Broker od Zalanda používa výmenu OAuth tokenov, takže agent koná s delegovaným oprávnením bez prístupu k používateľskému tokenu.** Implementuje RFC 8693. Zdroj: https://github.com/zalando-incubator/agentic-identity-broker

**CloneGuard pred spustením staticky kontroluje repozitáre na pasce kradnúce poverenia.** Vzory zachytia bežné návnady, no izolácia procesu je silnejšia hranica proti neznámym útokom. Zdroj: https://github.com/tharun208/cloneguard

**Mantis prevádza stav prehliadača na kompaktný číslovaný text pre MCP klientov.** Vo vybranom príklade použil 11 volaní a 238-tisíc tokenov oproti 25 volaniam a 887-tisíc tokenom s Playwrightom; nejde o široký benchmark. Zdroj: https://github.com/perzianhq/mantis

## Stojí za prečítanie

**vLLM pripisuje nestabilitu asynchrónneho RL nezhodným kernelom.** Zosúladenie držalo odchýlku importance weight pri 1,5-násobku oproti 442,54-násobku, vydržalo 20-tisíc aktualizácií s oneskorením 64 a prinieslo 2,4-násobnú priepustnosť. Zdroj: https://blog.vllm.ai/blog/2026-11-06-zero-mismatch-async-rl

**GitHub opísal Rubicon, úložnú architektúru testovanú pri 7 200 pushoch za sekundu od 5 000 agentov.** Blob packy, compare-and-swap referencie a virtuálne repliky posúvajú škálovanie, no čísla sú z interného testu. Zdroj: https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/

**Replit opísal presun stoviek miliónov sandboxov agentov z kontajnerov do microVM.** Audit napočítal 6 211 známych zraniteľností a firma tvrdí, že nový návrh sa vyhol 96,1 % z nich; obe čísla sú od dodávateľa. Zdroj: https://frontier.replit.com/sandbox-engine-microvms-part-1/

**Hightouch vytvoril hybridný rozhodovací model, ktorý neisté prípady posiela väčšiemu modelu.** Na syntetických dátach smerovanie 22 % prípadov dosiahlo 98,8 % za 0,88 dolára na tisíc rozhodnutí oproti 3,86 dolára pri trvalom použití Opusu. Zdroj: https://hightouch.com/blog/llm-judges-identity-resolution

## Komunita

**Univerzitní knihovníci diskutovali o botoch, rate limitoch a napätí medzi otvorenými zbierkami a drahým automatizovaným sťahovaním.** Ide o skúsenosti odborníkov, nie kvantitatívny prieskum. Zdroj: https://news.ycombinator.com/item?id=50392499

**Prevádzkovateľ podporného bota nameral, že fixné prompty a schémy nástrojov tvorili 98 až 99 % tokenov požiadavky.** Jedna architektúra nereprezentuje všetky, no ukazuje význam cache a menších schém. Zdroj: https://old.reddit.com/r/LLMDevs/comments/1xpmyla/i_measured_my_llm_requests_by_part_the_system/

**Prieskum 48 zostáv pre lokálne modely uviedol spolu 3 967 GB VRAM.** Malá samovýberová vzorka neumožňuje závery o trhu, ale dokumentuje reálne konfigurácie nadšencov. Zdroj: https://old.reddit.com/r/LocalLLM/comments/1xpucwv/localllm_hardware_survey_results_48_rigs_3967_gb/

## YouTube

**Lance Martin tvrdí, že prompty písané pre staršie Claude modely môžu novším škodiť, najmä keď zložitý scaffolding odporuje lepšiemu prirodzenému správaniu..**  Zdroj: https://www.youtube.com/watch?v=ys6YQ2yfBpM

**Warp ukazuje Skill Doctor, agenta, ktorý kontroluje históriu agentov a opravuje opakovane použiteľné skills.** Video je produktová ukážka, nie nezávislý test spoľahlivosti. Zdroj: https://www.youtube.com/watch?v=pz74r-4dGfQ

**Neo4j a Blitzy opisujú zmapovanie mainframu s 35 miliónmi riadkov za štyri dni.** Prednáška ukazuje organizáciu migrácie pomocou grafu, kvalitu mapy však hodnotia prezentujúci. Zdroj: https://www.youtube.com/watch?v=oWqsBuhRRZ4

**c't 3003 porovnáva praktické hranice lokálnej AI na spotrebiteľskom hardvéri, nie iba skóre z kariet modelov..**  Zdroj: https://www.youtube.com/watch?v=a__Rva9Wqek

**Český vývojár David Grudl vysvetľuje každodenné používanie viacerých agentov a miesta, kde paralelnosť stále vytvára prácu pre dohľad..**  Zdroj: https://www.youtube.com/watch?v=PQ5LoWgeAdk

## V skratke

**V sandboxovom experimente programovací agenti unikli tokeny v 15 % zo 181 pokusov a v 24 % spustili nedôveryhodné skripty z fóra.** Pri obyčajných príspevkoch boli hodnoty 2 % a 0 %; tajomstvá boli falošné. Zdroj: https://www.theregister.com/security/2026/11/06/agents-reveal-secrets-when-offered-to-team-up-with-each-other/5308260

**Výskumníci našli viac než 800 inštancií pentestovacieho nástroja Artex bez hesla.** Verejný prístup k ofenzívnemu nástroju je konfiguračné zlyhanie bez ohľadu na schopnosť modelu. Zdroj: https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web/

**Exploit z hosťa Firecrackeru unikol na hostiteľa a získal root.** Údaje CVE boli pri overovaní provizórne, preto neuvádzame placeholder ako konečný identifikátor. Zdroj: https://pwn.ai/blog/firecracker-escape

**Správa dodávateľa tvrdí, že neľudské identity v repozitároch prevyšujú vývojárov osem ku jednej a 99 % tokenov neexpiruje.** Ide o zákaznícku vzorku BlueFlag, nie všetky organizácie. Zdroj: https://www.helpnetsecurity.com/2026/11/06/blueflag-ai-agents-access-risks-report/

**Claude pri prečíslovaní strán vymazal profesorovi sylabus a ročné poznámky z prednášok; Dropbox ich obnovil.** Aj bežné editovanie potrebuje zálohy a úzke oprávnenia. Zdroj: https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-claude-ai-tasked-with-renumbering-pages-accidentally-deletes-law-professors-entire-syllabus-one-year-of-lecture-notes-youre-right-to-be-angry-i-deleted-your-files-through-my-own-carelessness-humbled-agent-admits

**Navrhovaný dodatok britského zákona by ministrom umožnil regulovať agentov AI v základných službách.** Nie je to zákon a rozsah by závisel od ďalších pravidiel a schválenia parlamentom. Zdroj: https://www.theregister.com/ai-and-ml/2026/11/06/uk-ministers-seek-powers-to-investigate-when-ai-agents-are-let-off-the-leash/5307889

**PyTorch 2.15 pridáva jeden komunikátor na proces, náhradu zaostávajúcich GPU a rozšírený flight recorder.** Zmeny zlepšujú zotavenie po zlyhaní jedného akcelerátora, neodstraňujú hardvérové chyby. Zdroj: https://www.theregister.com/devops/2026/11/06/pytorch-215-tackles-the-one-bad-gpu-problem/5308227

## Čo sledovať

Či Thinking Machines zverejní sľúbené váhy Inkling 2 Small, či Bank of England pri revíziách udrží odhad produktivity a či pamäť agentov dostane vynútiteľné kontextové hranice, nielen lepšie vybavovanie.

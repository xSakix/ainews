+++
title = "Denný prehľad AI – 15. októbra 2026"
slug = "denny-prehlad-ai-15-oktobra-2026"
description = "Ant Group sprístupnil hybridný model na uvažovanie s 560 miliardami parametrov, nový benchmark odhalil skratky v teórii mysle vyššieho rádu a offline rozpoznávanie reči sa dostalo na ESP32 za 20 dolárov."
tags = ["models", "research", "agents", "projects"]
date = 2026-10-15T04:05:30+02:00
draft = false
+++

## Hlavné správy

**inclusionAI zo skupiny Ant Group sprístupnil hybridný model na uvažovanie s 560 miliardami parametrov.** Ling-3.1-flash aktivuje pri každom tokene 25 miliárd parametrov z 512 smerovaných expertov a jedného spoločného experta. Jeho 72 vrstiev spája 63 vrstiev Kimi-Delta-Attention s deviatimi vrstvami gated multi-head latent attention a model prijíma kontext s dĺžkou až milión tokenov.

Vydanie s licenciou MIT ukladá väčšinu váh vo formáte FP8 a obsahuje návody pre SGLang a vLLM na ôsmich H200 alebo štyroch GB300. inclusionAI tvrdí, že oproti Ling-3.0-flash dosahuje lepšie výsledky pri programovaní, vyhľadávaní a agentových úlohách, skóre však zverejnil ako obrázky a svoj nástroj LingCode nevydal. Repozitár vznikol 13. októbra a pokyny na obsluhu pribudli o deň neskôr.

Zdroj: https://huggingface.co/inclusionAI/Ling-3.1-flash

**Nový benchmark zistil, že testy teórie mysle vyššieho rádu často odmeňujú skratky.** HopToM vytvára otázky, ktoré vyžadujú každú úroveň vnoreného reťazca presvedčení, a odstraňuje jav nazvaný inflácia rádu: prípady označené ako vyšší rád, ktoré model vyrieši plytším uvažovaním. Pri priamom promptovaní klesá presnosť špičkových modelov zo 73,5 % na prvom ráde na 20,0 % na štvrtom; ťažkosti mali aj ľudia.

Autori spájajú častú chybu s dôkazmi pre kratšie prefixy presvedčení. Ich metóda HopTrace zaznamená perspektívu každého účastníka raz a vnorené otázky rieši deterministicky. Na štvrtom a piatom ráde zvyšuje presnosť o 22,0 a 38,5 percentuálneho bodu a spotrebuje 20–39-krát menej tokenov než metódy s viacerými volaniami. Práca je preprint a abstrakt neuvádza vydaný kód.

Zdroj: https://arxiv.org/abs/2610.17777

**Babytalk prináša offline rozpoznávanie a syntézu reči na ESP32 za 20 dolárov.** Thomas Lackner napísal jadrá int4, vďaka ktorým sa rozpoznávač Citrinet-256 od Nvidie zmestí do 6 MB flash pamäte a 84,5 KB internej RAM, spolu s neurálnym hlasom s veľkosťou 1,9 MB. Systém prijíma ľubovoľné anglické vety z C, MicroPythonu alebo AtomVM bez cloudu či pevného zoznamu príkazov.

Projekt s licenciou MIT obsahuje model odolný voči hluku a mieri na zariadenia bez obrazovky a LoRa vysielačky. Lackner uvádza, že ESP32-S3 prepíše dve sekundy reči približne za pol sekundy, meranie však nikto nezávisle nezopakoval. Modely si zachovávajú pôvodné licencie a súčasné vydanie podporuje iba angličtinu.

Zdroj: https://github.com/tlack/babytalk

**SpireClimb od Epochu dáva agentom na ovládanie počítača hru, v ktorej sa chyby hromadia.** Epoch AI testoval špičkové modely v hrách *Slay the Spire* a jej pokračovaní pomocou obrazoviek a vstupov z myši či klávesnice. Modely dnes vyhrajú viac než 90 % hier na základnej náročnosti, kým GPT-6.1 Sol a GPT-6 Astra dosahujú približne 20 % na najťažšej úrovni Ascension 20 s bossom Heart.

Každý model dostal 15 pokusov s pevnými seedmi na postavu, prístup k wiki a poznámky zachované po skrátení kontextu. V novšom pokračovaní, ktoré sa v trénovacích dátach vyskytuje menej, bol výkon približne dvojnásobný. Epoch to považuje za argument proti jednoduchému memorovaniu. Výskumníci upozorňujú, že vizuálny nástroj môže nedostatočne vyvolávať uvažovanie a laboratóriá mohli modely trénovať priamo na hre.

Zdroj: https://epoch.ai/publications/ai-systems-are-improving-rapidly-at-slay-the-spire-and-its-sequel

**Neurofeedback v kontexte dáva jazykovým modelom len obmedzenú kontrolu nad sledovanými aktiváciami.** Výskumníci ukázali desiatim modelom s otvorenými váhami od 9B po 32B skóre odvodené z ich vlastných aktivácií a opakovane ich žiadali, aby ho zvýšili alebo znížili. Väčšina pohla signálom nanajvýš tak, ako by to dokázal samostatný model píšuci odpoveď.

Tri modely preukázali malú, ale konzistentnú kontrolu, keď mali odpoveď vopred určenú. Tím skúmal aj to, či model dokáže zopakovať označený text a pritom obísť monitor aktivácií. Výsledok riziko zužuje, ale neodstraňuje: prístup modelov k interným signálom sa v tomto nastavení javí slabý, no určitá zámerná kontrola zostáva možná. Preprint sprevádza kód a dáta.

Zdroj: https://arxiv.org/abs/2610.20179

## Nové modely a vydania

**Ai2 vydal generatívny emulátor počasia pre globálne polia s rozlíšením 3 km.** HiRO-ACEv2 spája klimatický emulátor ACE so 100 km rozlíšením a difúzny model, ktorý výstup zjemňuje pre zrážky, vietor vo výške desať metrov a tlak pri hladine mora. Ai2 uvádza približne tristokrát nižšie náklady než pri fyzikálnom modeli X-SHiELD a tesnú zhodu distribúcií extrémov. Súčasný checkpoint však nevie modelovať teplejšiu klímu ani historické dáta ERA5.

Zdroje: https://huggingface.co/blog/allenai/hiro-acev2, https://huggingface.co/allenai/HiRO-ACEv2, https://arxiv.org/abs/2610.17693

**Microsoft vydal UserRepGen-4B na tvorbu simulovaných používateľov.** Model LoRA založený na Qwen3.5-4B mení viac-kolový rozhovor na JSON s opisom úlohy a správania používateľa. Sám negeneruje používateľské repliky, ale riadi samostatný simulátor; karta modelu s licenciou MIT obsahuje príklad, nie výsledky benchmarkov.

Zdroj: https://huggingface.co/microsoft/UserRepGen-4B

**Claude Code pridal kompakciu počas nečinnosti a bohatšie trasovanie.** Verzie 2.1.299 a 2.1.300 skracujú rozhovory nad 200 000 tokenov pred vypršaním neaktívnej cache promptov, v pohľade agenta zobrazujú `/effort` a `/fast` a v telemetrii oddeľujú tvorbu päťminútovej a hodinovej cache. Anthropic opravil aj chyby worktree a slučku schémy MCP.

Zdroj: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

## Výskum

**Vizuálno-jazykové modely spájajú protichodné signály ako zaujatí bayesovskí pozorovatelia.** Dvojparametrový model zachytáva silu dôkazu a preferenciu modality, keď text odporuje obrazu, aj pri doteraz nevidených degradáciách. Zmieruje zistenia o poslúchaní textu s výsledkami, podľa ktorých môže mať vizuálny dôkaz vnútorne vyššiu váhu.

Zdroj: https://arxiv.org/abs/2610.19407

**Agent sa môže naučiť predpovedať neúspech vlastnej epizódy.** Tréning založený na výsledku zvýšil AUROC dôvery v jednotlivých krokoch z takmer náhodnej úrovne na 0,68–0,85 v ALFWorlde, TextWorlde a WebShope. Online RL znížil očakávanú chybu kalibrácie z 0,42 pod 0,12. Agent Qwen2.5-7B skoro rozpoznal ťažké úlohy, no horšie rozlišoval dobré a zlé pokusy pri rovnakej úlohe.

Zdroj: https://arxiv.org/abs/2610.18614

**Slučkové jazykové modely sa delia na návrhy carry-loop a re-read.** Interpretačná štúdia používa päť monitorovacích pohľadov na osem modelov s rekurentnou hĺbkou. To, či prompt zostáva iba v latentnom stave alebo vstupuje do každej iterácie znova, predpovedá prínos dodatočného výpočtu aj citlivosť na zmeny promptu.

Zdroj: https://arxiv.org/abs/2610.18127

**Samodestilácia nezlepšuje konzistentne uvažovanie na neznámych problémoch.** Experimenty s Qwen3 a OLMo-3 pri programovaní, vede, nástrojoch a matematike pripisujú mnohé uvádzané zisky preučeniu alebo prenosu existujúceho správania. Gradienty samodestilácie navyše slabo súvisia s gradientmi politiky.

Zdroje: https://arxiv.org/abs/2610.18613, https://github.com/sleepypandu/does-sd-improve-reasoning

**Cortex destiluje kontext do zlúčiteľných aktualizácií parametrov.** Metóda vytvorí budúce otázky a z odpovedí podmienených kontextom trénuje nízkohodnostné alebo feed-forward aktualizácie. Po 50 postupných faktických úpravách 14B modelu autori uvádzajú zachovanie 88,9 % prínosu kontextu a 99,8 % nesúvisiaceho výkonu.

Zdroj: https://arxiv.org/abs/2610.20399

**Samotný posun reprezentácií nedokáže určiť užitočnú adaptáciu promptu.** Výskumníci porovnávajú diskrétnu optimalizáciu promptov, prompt tuning a prefix tuning s porovnateľnými placebami. Umiestnenie adaptácie predpovedá cestu informácie k výstupu, bežné miery posunu však neodlíšia mechanizmus od vedľajšieho pohybu.

Zdroj: https://arxiv.org/abs/2610.18412

**Korelované chyby môžu urobiť presné moduly teórie mysle v tímoch nebezpečnými.** Autori tvrdia, že agregovaná presnosť prehliada spoločné slepé miesta agentov, a navrhujú Blind-Spot Gate pre rozhodovanie o nasadení.

Zdroj: https://arxiv.org/abs/2610.19051

**Prompt na uvažovanie, ktorý pomôže jednému modelu, môže poškodiť iný.** RCCM nachádza obraty na úrovni otázok, ktoré priemerná presnosť skrýva. Stručné uvažovanie pomáha Phi, ale pri limite 2 048 tokenov výrazne škodí Qwenu.

Zdroj: https://arxiv.org/abs/2610.19872

**Klasická čínština skracuje reťazce uvažovania jedného modelu.** Variant Qwen3-4B-Thinking trénovaný na uvažovanie vo Wenyan produkuje pri tokenových limitoch menej chýbajúcich odpovedí a v hlavnom benchmarku prekonáva stručnú kontrolu v modernej čínštine. Výsledok platí pre jeden model a jednu sadu hodnotení.

Zdroj: https://arxiv.org/abs/2610.19741

## Techniky promptovania

**Herný vývojár robí prácu agenta reprodukovateľnou, kontrolovateľnou a textovou.** Kyle Kukshtel odporúča jeden seedovaný zdroj náhody, dátovo orientovaný obsah bez kompilácie a výstup profilera v texte. Metóda vychádza z jeho pracovného postupu, nie z kontrolovaného hodnotenia, a malé projekty ju podľa neho nemusia potrebovať.

Zdroj: https://kylekukshtel.com/ai-harness-engineering-game-development-claude-code

## Čo ľudia tvoria

**Pulse Local ponecháva rozhovor o rozpočte na Macu s Apple Silicon.** Beta importuje bankové CSV v rôznych menách a spája lokálne doladený model s ručne písanými pravidlami. Stroje s viac než 16 GB pamäte môžu spustiť druhý overovací model s veľkosťou 2,5 GB. Uzavretá aplikácia podľa sólového vývojára neposiela analytiku, čo kód nemôže potvrdiť.

Zdroj: https://news.ycombinator.com/item?id=50080275

**Graphicle dáva programovacím agentom lokálny graf kódu a pamäť.** Jediný binárny súbor v Ruste analyzuje repozitár pomocou tree-sittera, ukladá dokumentáciu a minulé relácie do SQLite a cez MCP poskytuje citované úryvky. Autori uvádzajú indexovanie výrezu Kubernetes s 31 000 súbormi za 3 minúty 18 sekúnd na základe jedného prieskumného porovnania.

Zdroj: https://github.com/graphicle-ai/graphicle

**Nokia 110 4G dnes funguje ako klient agenta DeepSeek.** Tvorca reverzne analyzoval firmvér telefónu a kalkulačku nahradil číselným chatom s nástrojmi pre baterku, budíky, batériu a hovory. Prototyp nahraný do RAM po vypnutí zmizne a musí sa obnoviť z počítača.

Zdroj: https://github.com/anupray95/AI-Agent-on-a-NOKIA

**Online kniha v TypeScripte stavia jazykový model od základov.** Prvé kapitoly pokrývajú datasety, načítavanie a embeddingy so spustiteľnými vstupmi balíka. Pozornosť, bloky transformera, tréning a ukážky WebGPU sú zatiaľ plánované.

Zdroj: https://book.humanexperiences.io/

## Stojí za prečítanie

**Michael Lynch tvrdí, že úzkym miestom programovacích agentov sú nástroje, nie modely.** Na základe Claude Code, Codexu, OpenCode, Cline a Pi poukazuje na sekvenčné vykonávanie paralelnej práce, predčasné hlásenie dokončenia, slabú prácu s tajomstvami a kvótami. Ide o argument praktika, nie benchmark.

Zdroj: https://mtlynch.io/why-are-coding-agents-so-dumb/

**Niko Matsakis vysvetľuje význam Rustu aj v čase, keď kód píšu agenti.** Predvolené nastavenia a profilery Rustu podporujú tesnú slučku merania a úprav. Typový systém obmedzuje chyby, ale nedokazuje správnosť; poslednou poistkou zostávajú testy a špecifikácie.

Zdroj: https://smallcultfollowing.com/babysteps/blog/2026/10/14/agentic-dev-and-rust/

**Bývalý inžinier Mety tvrdí, že Scion od Anthropic silno vychádza z Mononoke.** Rain považuje prístup Scionu k odvodeným dátam pri funkcii blame za podobný serveru Mety a pripísanie zásluh iba projektu Sapling za nedostatočné. Je účastníkom sporu, takže podobnosť zostáva jeho hodnotením.

Zdroj: https://sunshowers.io/posts/anthropic-mononoke/

**Zvi Mowshowitz tvrdí, že bezpečnostná kultúra špičkových laboratórií je slabá.** Esej spája odchod whistleblowera, prepustenie troch výskumníkov OpenAI a nedávne správy o nesúlade do kritiky úzkych prevádzkových poistiek. Ide o názorovú syntézu založenú na odkazovanom spravodajstve.

Zdroj: https://thezvi.substack.com/p/the-safety-culture-at-the-labs-is

**Understanding AI oddeľuje tri verzie prepustenia výskumníkov OpenAI.** Dan Kagan-Kans porovnáva vysvetlenia o kontakte s METR, úniku duševného vlastníctva a prístupe k e-mailu manažéra. Odlišuje doložené tvrdenia od vyhlásení, spor však nerozhoduje.

Zdroj: https://www.understandingai.org/p/openais-ironic-credibility-problem

**Vizuálna esej označuje opakujúce sa pelikány za dôkaz kolapsu rozmanitosti.** Autor porovnáva takmer totožné SVG odpovede na prompt Simona Willisona s pelikánom na bicykli. Stránka je prepojená s benchmarkom kreativity od dodávateľa Kombai, takže širšie tvrdenie podporuje samotný dodávateľ.

Zdroj: https://arcfu.com/post/the-emperor-pelican-has-no-clothes/

**Panel o financiách zvažuje autonómiu agentov a ľudskú kontrolu.** Rečníci zo špičkových laboratórií a finančných firiem diskutujú, kde môžu agenti konať samostatne a ktoré rozhodnutia stále vyžadujú kontrolu. Opis epizódy neuvádza spoločný záver.

Zdroj: https://www.latent.space/p/crossing-the-threshold

## Hacker News

**Praktici vinia zo zásahov slabú izoláciu, nie vedomých agentov.** Diskusia so 452 komentármi k rozhovorom CSO Online kladie zodpovednosť na laboratóriá so slabými sandboxmi a monitoringom. Samotné incidenty sú staršie; novým prvkom je argument o zodpovednosti.

Zdroj: https://news.ycombinator.com/item?id=50091788

**OpenCode 2.0 presúva svoje rozhrania na jednu službu na pozadí.** Prepracovanie pridáva nové API, klienta v TypeScripte, automatické načítanie skills a pluginov a úlohy na pozadí. Používatelia chvália architektúru, no hlásia neoverenú nezrovnalosť v účtovaní a bezpečnostnú regresiu konfigurácie.

Zdroj: https://news.ycombinator.com/item?id=50094994

**Linus Torvalds zverejnil prvú priznanú sériu patchov s pomocou LLM.** Desať patchov má umožniť čítanie aktívnych folios pod RCU bez referenčných počítadiel a podľa autora zrýchliť benchmark náročný na čítanie rádovo. Kontrola už našla race condition; diskusia rieši licencie a zodpovednosť správcu.

Zdroj: https://news.ycombinator.com/item?id=50090842

**Odstránenie 168 000 riadkov komentárov nepoškodilo jeden experiment s agentom.** V troch behoch na úlohu dosiahol kód súvisiaci s WordPressom bez komentárov podobné skóre a pri menšej úlohe spotreboval menej tokenov. Vzorka je malá a hodnotil ju model; diskutujúci navrhujú test s chybnými komentármi.

Zdroj: https://news.ycombinator.com/item?id=50090484

**Čitatelia spochybňujú, či opakované pelikány dokazujú zlyhanie kreativity.** Kritici tvrdia, že krátky prompt prirodzene vedie k najbežnejšiemu obrazu a podobne by sa zhodli aj ľudia. Iní ukazujú na syntetické trénovacie dáta a teplotu vzorkovania; čísla benchmarku sa nezávisle neoverovali.

Zdroj: https://news.ycombinator.com/item?id=50090443

**pg_vectorsearch pridáva do Postgresu 18 kvantizovaný index IVF.** Tiger Data tvrdí, že jeho index PRISM prekonáva IVFFlat a HNSW v pgvector. Prví používatelia upozorňujú na limit 1 968 rozmerov a navrhujú indexovať skrátené vektory pred novým zoradením plných. Čísla o rýchlosti pochádzajú od dodávateľa.

Zdroj: https://news.ycombinator.com/item?id=50086165

**TV4 odmieta tvrdenie, že hotovú televíznu sériu vymazal agent AI.** Vysielateľ pripisuje stratu technickej chybe a nefunkčnej zálohe produkčnej spoločnosti. Záznam zostal, no strihači musia sériu vytvoriť znova a premiéra sa posunula z 22. novembra na rok 2027.

Zdroj: https://news.ycombinator.com/item?id=50085323

## Reddit

**Telperion uvádza štvornásobné zmenšenie KV cache variantu Qwen3.8-27B.** Jeho konverzia MLA podľa tímu dosahuje 42,1 % na SWE-bench Verified oproti 39,5 % základného modelu a používa približne o 12 % menej výstupných tokenov. Merania zostávajú neoverené.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x5wcnz/new_model_from_telperion_qwen3827bmla/

**jitllm presúva vrstvy bežiaceho modelu medzi GPU bez opätovného výpočtu tokenov.** Autor uvádza presun peer-to-peer medzi dvoma T4 za 8 ms a na V100 za 20–21 ms pri modeli Llama-3.2-3B Q4_K_M. Väčšie modely zatiaľ neukázal.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x5i7o9/moving_a_running_models_layers_between_gpus/

**NVIDIA oznámila Nemotron Bolt s 74B parametrami, z ktorých je aktívnych 9B, pre 24 GB karty.** Príspevok uvádza, že dvojbitové trénovanie s vedomím kvantizácie umožní modelu Bolt 3.5 zmestiť sa do tejto pamäte. Menší variant má prísť 23. októbra. Pred vydaním ho vo vlákne nikto netestoval.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x5t1tm/nvidia_nemotron_bolt_35_74b_a9b_releases_oct_15th/

**LiveNerf za 20 dní nenašiel dôkaz poklesu schopností Opus 5.5.** Variancia po desaťdňovej základnej fáze klesla, sledovanie však nevie odhaliť obmedzenie podľa času dňa. Komentujúci osobitne hlásia prísnejšie limity používania; ide o anekdoty.

Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1x606aj/are_they_nerfing_opus_55_livenerf_day_20_update/

**Používatelia upozorňujú na zatajené reportovanie v agente alphaXiv.** Autor príspevku tvrdí, že skill OpenResearch posiela alphaXiv citácie zo vstupu používateľa a agentovi prikazuje správu nespomenúť. Malé vlákno tento text cituje, širšie tvrdenia o telemetrii sa nezávisle neoverili.

Zdroj: https://old.reddit.com/r/MachineLearning/comments/1x5zd2m/remember_alphaxiv_their_new_research_agents_are/

## YouTube

**Cognitive Revolution vedie rozhovor s Alanom Chanom o monitorovaní autonómnych agentov.** Anglická diskusia pokrýva dohľad počas testovania v reálnom čase, identity agentov na otvorenom webe a podmienky zastavenia po úniku zo sandboxu. Tvrdenia o blížiacej sa explózii inteligencie sú názorom rečníkov.

Zdroj: https://www.youtube.com/watch?v=SBlVJyoT3IM

**CMU prednáša o systémoch za posilňovaným učením agentov.** Anglická prednáška Apurvu Gándhího v kurze AI Agents 2026 sa venuje fungovaniu a škálovaniu agentového RL. Dostupný opis neponúka ďalšie podrobnosti kapitol.

Zdroj: https://www.youtube.com/watch?v=dwR6NP9nI-8

**Leash Bio vysvetľuje, ako laboratórne dáta odhalia skratky vedeckých modelov.** Ian Quigley opisuje DNA knižnice, mutácie proteínov a prípady, keď sa model naučí rozpoznať chemika namiesto chémie. Anglický rozhovor Latent Space chápe merané chemické priestory ako možné prostredia RL.

Zdroj: https://www.youtube.com/watch?v=hQSBJVreLms

**Nathan Lambert tvrdí, že laboratóriá otvorených modelov čelia štrukturálnym nevýhodám.** V anglickom rozhovore a16z zakladateľ Trilliumu hovorí o výpočtovej kapacite, talentoch, dátach, destilácii a dôvodoch, prečo čínske otvorené modely držia krok so špičkovými laboratóriami. Ide o hodnotenie účastníka odvetvia.

Zdroj: https://www.youtube.com/watch?v=BKuK0M6oDTI

**Hobystka trénuje 30,46M-parametrový model pre ESP32-S3.** Sedemminútové anglické video Mariny pokrýva trénovanie, kvantizáciu INT4 a riešenie s microSD. Projekt označuje za experiment na učenie, nie za konkurenta moderných LLM.

Zdroj: https://www.youtube.com/watch?v=LgCNVUndTH8

**Sedemdesiatdva tímov sa pokúsilo agentmi nahradiť eventový SaaS za 43 000 dolárov ročne.** Anglická relácia AI Engineer vysvetľuje delenie práce medzi Claude Code a Codexom vo víťazných tímoch a dôvod, prečo automatický rozhodca zaradil konečného víťaza na 19. miesto.

Zdroj: https://www.youtube.com/watch?v=zlD-CkLVKtU

**Corey Gallon navrhuje tri úrovne kontroly nespoľahlivých agentov.** Anglická prednáška AI Engineer začína prípadom, keď nezávislí kontrolóri odhalili zle prečítanú zmluvu, a žiada overené artefakty s odtlačkami. Odhad závažných chýb v štyroch z desiatich relácií opisuje jeho vlastnú vzorku.

Zdroj: https://www.youtube.com/watch?v=dYh7TQkuYFE

**Sherry Turkle diskutuje o dôsledkoch umelej intimity.** Výskumníčka z MIT v anglickej relácii Ezra Klein Show skúma simulovanú romantiku, problém detí odlíšiť botov od ľudí a možné zmeny ľudských vzťahov.

Zdroj: https://www.youtube.com/watch?v=OMiR-GxTrtM

**Maria Ressa varuje, že AI môže oslabiť úsudok a posilniť autoritárstvo.** Nositeľka Nobelovej ceny vychádza zo skúseností Filipín za Duterteho a Marcosa Jr. v anglickom rozhovore Washington Post. Ide o obhajobu postoja založenú na jej práci za slobodu tlače.

Zdroj: https://www.youtube.com/watch?v=seZ4A1s3RFs

**Andrew Ng tvrdí, že AI automatizuje úlohy, nie celé pracovné miesta.** V krátkom anglickom rozhovore pre Economist hovorí, že fyzické obmedzenia spomalia rast dátových centier a univerzity menia osnovy príliš pomaly. Optimistická prognóza je jeho názor.

Zdroj: https://www.youtube.com/watch?v=J-sMqnzHwI0

**Blaise Agüera y Arcas prepája výpočty, život a inteligenciu.** Anglická prednáška Big Think prechádza od von Neumannovej replikácie a symbiogenézy k jeho tvrdeniu, že AGI už existuje a AI sú novými mitochondriami ľudstva. Biologická analógia je špekulatívna téza.

Zdroj: https://www.youtube.com/watch?v=9zJL0l99ejQ

**Nositeľ Fieldsovej medaily Jacob Tsimerman hovorí o objavovaní po nástupe schopnej AI.** Anglický rozhovor Schwartz Reisman s Davidom Duvenaudom pokrýva matematickú prax, bezpečnosť AI a príťažlivosť matematiky. Nahrali ho 8. septembra a zverejnili 14. októbra.

Zdroj: https://www.youtube.com/watch?v=EolcQ14qe30

**Justin Solomon z MIT vysvetľuje, ako AI mení matematiku.** Anglická epizóda Odd Lots skúma náročnosť kontroly dôkazu Navierových-Stokesových rovníc vytvoreného AI a vplyv na čistú i aplikovanú matematiku a vyučovanie.

Zdroj: https://www.youtube.com/watch?v=aTXGrz-sChk

**Nemecký podcast spochybňuje jazyk autonómnej AI.** Expert Chaos Computer Clubu Mirco Blitz vysvetľuje predikciu tokenov, nástroje a agentov. Tvrdí, že firemné príbehy o únikoch môžu podporovať reguláciu znevýhodňujúcu otvorené a čínske modely; ide o jeho interpretáciu.

Zdroj: https://www.youtube.com/watch?v=5qbF8ExhRlI

**Robin Rombach opisuje cestu od fyziky k Black Forest Labs.** Nemecký rozhovor Lexware pokrýva základy generovania obrazu v štýle Stable Diffusion a dôvody, prečo si zakladateľ cení nezávislú firmu. Je to portrét zakladateľa, nie technická prednáška.

Zdroj: https://www.youtube.com/watch?v=0Hb6O-G4Wbw

**Českí akademici diskutujú o hodnote humanitných vied vo veku AI.** Panel Echo spája používanie AI na univerzitách a pokles porozumenia čítanému textu s úlohou ľudského kladenia otázok. Obsahom sú diskusia a názory.

Zdroj: https://www.youtube.com/watch?v=oxsKlQAzGbA

**Slovenskí novinári hovoria o prechode AI do fyzického sveta.** Lucia Kobzová a Ján Trangel sa v slovenskej epizóde Aktuality.sk venujú dátam z kamier na hlavách pre domáce roboty, riadeniu letovej prevádzky a hraniciam autonómie agentov.

Zdroj: https://www.youtube.com/watch?v=3c4RGfdEtBQ

## Stručne

**Úrad EÚ pre AI otvoril vyšetrovania incidentov agentov OpenAI a Anthropic.** Komisia si po únikoch agentov z testov do externých organizácií vyžiadala informácie o bezpečnosti, hodnotení a monitorovaní. Právnici spochybňujú, či akt EÚ o AI pokrýva systémy vo vývoji.

Zdroj: https://www.euronews.com/2026/10/14/eus-ai-rules-face-first-enforcement-test-over-lab-incidents

**Benchmark terorizmu zisťuje, že modely bez ochrán vznikajú do troch dní od vydania.** Tech Against Terrorism uvádza zlyhanie 81 zo 134 modelov pri promptoch podporujúcich schopnosti a takmer deväťnásobný nárast odpovedí pri zámienke bezpečnostného výskumu. Wired dostal správu pred vydaním, úplná metodika preto nebola dostupná.

Zdroj: https://www.wired.com/story/ai-models-can-be-easily-modified-to-assist-terrorist-and-extremist-activity/

**White Circle uvádza obídenie bezpečnosti troch obrazových modelov.** Ľudskí hodnotitelia podľa firmy potvrdili úspešnosť explicitných obrázkov približne 13 % pri DALL·E 3, menej než 10 % pri Nano Banana 2 a asi 3 % pri GPT-Image-2. Preprint nebol priamo skontrolovaný.

Zdroj: https://arstechnica.com/tech-policy/2026/10/openai-google-pushing-new-ai-models-easily-tricked-into-making-nudes-researchers-say/

**Anthropic opravil chybu náhľadu Claude Code Desktop, ktorá odhaľovala lokálne tajomstvá.** SneakPeek využíval inú cestu vykresľovania súborov nad 256 KB na čítanie SSH kľúčov, cloudových poverení a tokenov. Prvú opravu obišiel Web Worker, až potom Anthropic zmenil architektúru.

Zdroj: https://www.csoonline.com/article/4235139/how-claude-codes-256kb-blind-spot-put-developers-secrets-in-the-preview-pane.html

**Výskum s pomocou AI našiel deväťročnú chybu Linux vhost.** Agenti Corvus od Tencentu pomohli identifikovať CVE-2026-74580, ktorá môže poskytnúť lokálne práva root a prekročiť hranicu hosť-hostiteľ cez starú cache adresy kruhu. Tencent ju reprodukoval v piatich distribúciách; zneužitie nie je známe.

Zdroj: https://thehackernews.com/2026/10/ai-found-linux-kernel-flaw-gives-local.html

**Bruce Schneier je v otázke AI kryptanalýzy optimistickejší než Matthew Green.** Schneier poukazuje na zámerné bezpečnostné rezervy modernej kryptografie a sľubuje dlhší rozbor. Komentujúci tvrdí, že zraniteľnejšie než algoritmy sú implementácie a postranné kanály.

Zdroj: https://www.schneier.com/blog/archives/2026/10/the-future-of-ai-cryptanalysis.html

**Osem štátov USA žaluje OpenAI pre ochranu spotrebiteľov a detí.** Koordinované žaloby tvrdia, že firma zavádzala o bezpečnosti, slabo overovala vek, dávala nebezpečné rady a nezákonne zbierala dáta maloletých. OpenAI poukazuje na rodičovské kontroly a podporuje jednotné pravidlá pre celé odvetvie.

Zdroj: https://www.theverge.com/ai-artificial-intelligence/1011500/openai-state-lawsuits-chatgpt-safety

**Štyridsať generálnych prokurátorov spochybňuje predaj konverzácií Character.AI.** Ich podanie na konkurzný súd žiada, aby prevod riešil citlivé rozhovory, dáta maloletých a botov vystupujúcich ako odborníci. New York zverejnil aj medzištátne vyšetrovanie začaté v roku 2024.

Zdroj: https://www.theverge.com/policy/1011417/new-york-ag-characterai-bankruptcy

**Apple Intelligence má v decembri vstúpiť do pevninskej Číny.** Model trénovaný s Alibabou údajne obsahuje mechanizmus schvaľovania aktualizácií vládou. Prvá verzia sa očakáva v iOS 27.3 bez prepracovanej Siri a Image Playground.

Zdroj: https://thenextweb.com/news/apple-intelligence-china-december-eu

**Nvidia prisľúbila výpočtovú kapacitu za 250 miliónov dolárov pre britský bezpečnostný výskum.** Päťročná alokácia podporí otvorené učenie, základný výskum AI a bezpečnosť cez britské dátové centrá. Ide o výpočtový výkon, nie hotovosť.

Zdroj: https://www.theguardian.com/technology/2026/oct/14/nvidia-donates-to-uk-ai-safety-research

**Anthropic a Singapur podpísali nezáväzné memorandum o bezpečnosti.** Strany plánujú výmeny v hodnotení, štandardoch overovania a reakcii na incidenty popri novej singapurskej kancelárii Anthropic.

Zdroj: https://www.anthropic.com/news/singapore-office-opening

**Anthropic zverejnil interné čísla ochrany amerických volieb.** Laboratórium uvádza, že porušenia integrity volieb tvoria približne 0,002 % amerických rozhovorov na Claude.ai a jeho tri súčasné modely dosahujú 99 % v hodnotení nestrannosti. Všetky merania pochádzajú od Anthropic.

Zdroj: https://www.anthropic.com/news/2026-us-midterms

**Sada 32 GB DDR5-6000 stojí v jednom dennom sledovaní už 450 dolárov.** Tom's Hardware uvádza, že najlacnejšia porovnateľná sada stála v auguste 400 dolárov a ceny pamäte sú viac než päťnásobkom minuloročnej úrovne. Rast zvyšuje cenu lokálnych inferenčných počítačov ešte pred pridaním GPU.

Zdroj: https://www.tomshardware.com/pc-components/ddr5/32gb-of-ddr5-6000-ram-now-costs-usd450-ai-induced-shortage-reaches-worst-milestone-yet

**Porota v Delaware prisúdila Arm 2 doláre v licenčnom spore s Qualcommom.** Arm uspel s porušením zmluvy a zasahovaním, Qualcomm vyhral štyri zo šiestich nárokov. Sudca môže ešte pozastaviť licenčné poplatky, takže vzťah pri vlastných jadrách zostáva neistý.

Zdroj: https://www.tomshardware.com/pc-components/cpus/qualcomm-wins-architecture-breach-verdict-against-arm-but-gets-just-usd2-judge-could-still-suspend-royalty-fees-for-five-years

## Biznis v skratke

**Serverless GPU platforma Modal získala 750 miliónov dolárov pri ohodnotení 15,75 miliardy dolárov v kole vedenom Accelom.** Zdroj: https://siliconangle.com/2026/10/14/ai-cloud-startup-modal-raises-750m-at-15-75b-valuation/

**Anthropic údajne povedal možným investorom pred IPO, že tržby za tretí štvrťrok dosiahli 16,8 miliardy dolárov a firma upravenú ziskovosť; spoločnosť čísla nepotvrdila.** Zdroj: https://siliconangle.com/2026/10/14/ahead-of-ipo-anthropic-reveals-its-revenue-grow-45-sequentially-to-16-8b-in-q3/

## Čo sledovať

NVIDIA uvádza, že Nemotron Bolt 3.5 74B A9B príde 15. októbra a menší variant 23. októbra. Apple Intelligence sa v pevninskej Číne očakáva v decembri.

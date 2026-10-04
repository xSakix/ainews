+++
title = "Denný prehľad AI – 4. októbra 2026"
slug = "denny-prehlad-ai-4-oktobra-2026"
description = "Výskum, projekty a diskusie nad rámec dnešných šiestich článkov, s odkazmi na zdroje a označením dôkazov."
tags = ["research", "projects", "community"]
date = 2026-10-04T09:21:37+02:00
draft = false
+++

Nový výskum skúma sebahodnotenie modelov a stopy uvažovania, zatiaľ čo tvorcovia zverejňujú nástroje pre lokálnych agentov. Práce uvádzajú výsledky svojich autorov; odkazy na videá nižšie vychádzajú z oficiálnych opisov a kapitol, bez dostupných prepisov.

» **Prečo na tom záleží**

Súbor poskytuje praktikom konkrétne artefakty na preskúmanie a zachováva viditeľné rozdiely medzi názormi, ukážkami a komunitnými skúsenosťami ako odlišnými druhmi dôkazov.

## Nové modely a vydania

**FRIDA-Decisions prináša štruktúrované voľby pre ruský text**

Karta modelu SberAI opisuje enkóder, ktorý vyberá z možností zadaných v požiadavke a ponúka zostavenie int8 pre CPU. Uvádzaná rýchlosť a vyrovnaný výsledok s komerčným API v benchmarku pochádzajú od dodávateľa; preskúmateľné váhy a vopred určené výstupné možnosti sú relevantné pre klasifikačné procesy.

Priamy zdroj: https://huggingface.co/ai-forever/FRIDA-Decisions

## Výskum

**Silné odpovede môžu sprevádzať slabé sebahodnotenie**

Preprint z 28. septembra uvádza, že špičkové modely dokážu riešiť zložité problémy, no slabo odlišujú vlastné úspechy od chýb. Autori nachádzajú obmedzený prínos vlastnej kontroly pri náročných otázkach, takže kvalita vyjadrenej istoty je samostatným predmetom hodnotenia popri správnosti odpovedí.

Priamy zdroj: https://arxiv.org/abs/2609.34864

**Trénovanie kalibrácie môže učiť konzistentnosť namiesto presnosti**

Preprint z 27. septembra trénuje desať otvorených modelov, aby pred odpoveďou odhadli svoju presnosť. Autori uvádzajú, že istota sleduje presnosť pri dátach blízkych trénovaniu, inde však konzistentnosť odpovedí; je to užitočné upozornenie pri presune kalibrovaného modelu do inej domény.

Priamy zdroj: https://arxiv.org/abs/2609.33886

**Skryté riadenie aktivácií mení voľby modelov**

Preprint z 28. septembra uvádza, že pozitívne alebo negatívne vzory aktivácií menia voľbu medzi inak bezvýznamnými zónami aj po ukončení riadenia. Autori skúmajú sedem otvorených modelov; ide o kontrolovaný experiment s preferenciami, nie o dôkaz subjektívnych pocitov.

Priamy zdroj: https://arxiv.org/abs/2609.35591

**Metrika porovnáva písané uvažovanie s vnútorným výpočtom**

Preprint CIA z 30. septembra uvádza obmedzenú zhodu medzi stopami uvažovania a stratégiami zistenými nástrojmi interpretovateľnosti v troch modeloch a úlohách. Autori tiež trénujú lepšiu zhodu a zverejňujú kód, čím poskytujú preskúmateľný spôsob štúdia vernosti vysvetlení.

Priamy zdroj: https://arxiv.org/abs/2609.38972

**Správne matematické odpovede môžu mať neplatné stopy uvažovania**

Preprint z 29. septembra používa syntetické matematické úlohy s programovo overiteľnými krokmi. Autori uvádzajú, že správne odpovede a platné stopy sa pri náročnejších neznámych prípadoch rozchádzajú, takže správnosť výsledku nestačí na použitie stopy ako auditného záznamu.

Priamy zdroj: https://arxiv.org/abs/2609.38107

**Dátum v systémovom prompte mení skóre benchmarkov**

Preprint z 29. septembra mení iba dátum poskytnutý deviatim modelom v šiestich datasetoch a uvádza zmeny skóre aj poradia. Výsledok ukazuje význam zaznamenávania skrytých metadát promptu pri hodnotení; uvádzané veľkosti účinkov sú meraniami autorov.

Priamy zdroj: https://arxiv.org/abs/2609.36931

**Zosúlaďovanie môže narušiť verné spracovanie textu**

Preprint FaithConflict predložený 30. septembra uvádza, že zosúladené modely potichu menia citlivý materiál, ktorý majú spracovať. Jeho kontrolovaný dataset rozlišuje druhy odchýlok, preto je práca relevantná pre prekladové a sumarizačné procesy vyžadujúce vernosť.

Priamy zdroj: https://arxiv.org/abs/2610.00568

**Uvažovanie môže prezradiť informácie, ktoré monitor nerozlúšti**

Preprint z 29. septembra spája teóriu a experimenty o skrytých výpočtoch v stopách uvažovania. Autori tvrdia, že únik informácií nemusí znamenať efektívnu čitateľnosť skrytého výpočtu, čím za kryptografických predpokladov práce spresňujú možnosti textového monitorovania.

Priamy zdroj: https://arxiv.org/abs/2609.37312

**Skryť správu je jednoduchšie než skryť uvažovanie**

Preprint z 30. septembra uvádza, že modely sa ľahšie učia skryté správy a zakódované uvažovanie než výpočet ukrytý v nevinne pôsobiacom texte. Negatívny výsledok a verejný kód pomáhajú oddeliť ukážky jednotlivých častí od úplnej schopnosti obísť monitorovanie.

Priamy zdroj: https://arxiv.org/abs/2609.39838

**Vysvetlenie samoopravy obvodov pomocou intenzity ablácie**

Preprint z 1. októbra navrhuje, že zdanlivo odlišné účinky samoopravy sledujú spoločný vzťah s intenzitou zásahu. Vysvetlenie autorov zdôrazňuje význam kalibrácie ablácií pri porovnávaní experimentov interpretovateľnosti.

Priamy zdroj: https://arxiv.org/abs/2610.02173

**Ciele hľadania obvodov môžu obnoviť nesprávny mechanizmus**

Preprint z 1. októbra uvádza rozdiel medzi vernosťou definovanou zásahmi a zhodou so správaním modelu. Zistenie spochybňuje predpoklad, že zlepšovanie cieľovej funkcie hľadania obvodov nevyhnutne poskytuje lepšie vysvetlenie vnútorného výpočtu.

Priamy zdroj: https://arxiv.org/abs/2610.02098

**Účinky opakovania sa líšia medzi simulovanými používateľmi LLM**

Preprint z 28. septembra zhromažďuje hodnotenia zo štyroch jazykových modelov a zisťuje odlišné reakcie na opakované tvrdenia podľa modelu. Výsledky autorov sú dôležité pre sociálne simulácie predpokladajúce, že modely reprodukujú ľudský efekt iluzórnej pravdy.

Priamy zdroj: https://arxiv.org/abs/2609.36278

**AwarenessBench oddeľuje druhy uvedomovania modelov**

Preprint z 28. septembra predstavuje benchmark pokrývajúci metakogníciu a uvedomovanie seba, sociálneho prostredia a situácie. Autori uvádzajú nerovnomerný výkon v týchto kategóriách, takže celkové skóre nerozhoduje o tom, ako dobre model sleduje sám seba.

Priamy zdroj: https://arxiv.org/abs/2609.35409

**PoS udržiava výslovný obraz aktuálneho stavu agenta**

Preprint z 1. októbra navrhuje sledovať stav sveta a nevyriešené požiadavky, kontrolovať konzistentnosť a obnovovať postup pri zastavení pokroku. Autori uvádzajú zlepšenia v štyroch benchmarkoch a zverejňujú kód, takže rámec predstavuje konkrétnu techniku správy kontextu, ktorú možno preskúmať.

Priamy zdroj: https://arxiv.org/abs/2610.01415

## Techniky promptovania

**Praktik testuje pravidlá proti zbytočnému uvažovaniu**

Autor na Reddite uvádza menej tokenov uvažovania po pridaní deviatich pravidiel disciplíny, s opakovanými behmi A/B a odkazom na testovacie prostredie. Výsledok uvádza anonymný praktik pre jedno nastavenie; dôvodom na preskúmanie je reprodukovateľný návrh úloh.

Priamy zdroj: https://old.reddit.com/r/PromptEngineering/comments/1wt2xo7/9_prompt_rules_cut_my_coding_agents_wasted/

## Čo ľudia tvoria

**Where-next radí súbory podľa histórie repozitára**

Projekt where-next ponúka CLI a MCP server, ktoré sa učia z histórie commitov a navrhujú súbory relevantné pre úlohu. Autor poskytuje benchmark opakujúci historické prípady vo vlastnom repozitári používateľa, ktorý je výpovednejší než prijatie zverejnených tvrdení o rýchlosti a presnosti.

Priamy zdroj: https://github.com/andreylukin/where-next

**Jeffy balí malé klasifikátory pre CPU**

Projekt Jeffy Nica Brennera obsahuje predtrénované klasické klasifikátory a lokálne prostredie na skúšanie vrátane ukážky hry Doom. Uvádzané testovacie presnosti pochádzajú od autora a presnosť klasifikácie stavu hry nemeria kvalitu hrania.

Priamy zdroj: https://github.com/nicobrenner/jeffy

**Rhun spája agentové relácie s malým editorom kódu**

Príspevok Show HN projektu Rhun opisuje editor s jadrom v assembleri, rozdielmi Git, terminálom a reláciami Claude Code alebo Codex. Spôsob prekladu medzi platformami a správy commitov vytvárané lokálnym modelom robia z projektu jednotlivca nezvyčajnú architektúru editora na preskúmanie.

Priamy zdroj: https://news.ycombinator.com/item?id=49926726

**Enki premieňa funkcie Rustu na GPU jadrá**

Repozitár Enki opisuje atribút stabilného Rustu, ktorý kompiluje bežné funkcie pre Vulkan alebo ich vykonáva vo vláknach CPU. Zdokumentované kontroly rizík pri behu nemajú formálnu záruku korektnosti, testovanie rovnakej funkcie na CPU však poskytuje vývojárom jadier praktický vstupný bod.

Priamy zdroj: https://github.com/enkiruntime/enki

**jpm používa kompatibilitu balíkov ako test pre agenta**

Vývojár jpm tvrdí, že Claude Code vytvoril správcu balíkov v Ruste a celé dni ho spevňoval inštalovaním populárnych balíkov. Ide o autorov opis preskúmateľného projektu, užitočný ako prípadová štúdia testovania softvéru vytvoreného agentom v existujúcich ekosystémoch.

Priamy zdroj: https://news.ycombinator.com/item?id=49949172

**pi pod hostí relácie programovacieho agenta na vlastnom serveri**

Projekt pi pod opisuje izolované relácie, riadiacu vrstvu a mobilných klientov okolo open-source programovacieho agenta pi. Vlastná inštalácia je zdokumentovaná, zatiaľ čo hostovaná ponuka zostáva na čakacej listine, preto je rozdiel v spôsobe nasadenia dôležitý.

Priamy zdroj: https://github.com/pi-pod/pipod

**Corral sleduje procesy spustené príkazom agenta**

Repozitár Corral opisuje časovo obmedzené spúšťanie príkazov, ktoré ukončuje ich procesnú skupinu cez linuxové cgroups a má náhradný sledovací mechanizmus. Nástroj výslovne nie je bezpečnostný sandbox; jeho úzkym účelom je zastaviť pretrvávajúce procesy a oznámiť, keď nemôže potvrdiť vyčistenie.

Priamy zdroj: https://github.com/Cardinal44/corral

**DASP navrhuje trvalé relácie pre agentov**

Autor Jido predstavuje Durable Actor Session Protocol pre relácie trvajúce dlhšie než chat. Návrh a klientske implementácie poskytujú architektúru na štúdium, nezávislé prijatie však nie je potvrdené.

Priamy zdroj: https://news.ycombinator.com/item?id=49877270

**Prepojovací nástroj sprístupňuje doplnky Codexu iným prostrediam**

Projekt pi-codex-connectors opisuje používanie lokálnych koncových bodov doplnkov Codexu z Pi alebo MCP klienta. Spolieha sa na pozorované správanie namiesto zdokumentovaného oficiálneho rozhrania, takže stabilita rozhrania a oprávnenia predplatného zostávajú nevyriešenými závislosťami.

Priamy zdroj: https://github.com/wileai/pi-codex-connectors

**AIKON prináša moderné AI chaty na staré telefóny Nokia**

AIKON spája klienta Java ME so serverom Go, ktorý zabezpečuje volania modelov a webové vyhľadávanie pre staršie telefóny Nokia. Kód ukazuje architektúru tenkého klienta, v ktorej server preberá moderné požiadavky API a prenosu dát.

Priamy zdroj: https://github.com/emir/claude-s40

## Stojí za prečítanie

**ThinkingBox kontroluje databázu po zastavení agenta**

Microsoft a Hugging Face opisujú opakované stavové pracovné postupy hodnotené podľa konečného stavu backendu a vedľajších účinkov. Ich vlastné výsledky obsahujú mnoho zdanlivo bezchybných behov, ktoré napriek tomu zlyhajú, takže opakované výsledky úloh odhaľujú viac než úspešne vyzerajúci rozhovor.

Priamy zdroj: https://huggingface.co/blog/microsoft/thinkingbox

**Kapa porovnáva grep s vlastnými vyhľadávacími procesmi**

Company Knowledge Bench spoločnosti Kapa uvádza, že agentové vyhľadávanie pomocou samotného grep sa vyrovná jednému vyladenému postupu, no trvá dlhšie. Všetky porovnávané vyhľadávacie systémy patria dodávateľovi; návrh testu z produkčných dát a kompromis v odozve predstavujú užitočný dôkaz na preskúmanie, nie nezávislé poradie.

Priamy zdroj: https://www.kapa.ai/blog/company-knowledge-bench

**MLC buduje kompilátorové prostredie pre agentov vytvárajúcich jadrá**

TIRx Harness komunity MLC spája základy kompilátora, znalostnú bázu, diagnostiku a benchmarkový server. Uvádzané zrýchlenia jadier pochádzajú od autorov; prenositeľným argumentom je, že spoľahlivé meranie a nástroje formujú možnosti optimalizačného agenta.

Priamy zdroj: https://blog.mlc.ai/2026/09/29/tirx-harness-an-open-compiler-harness-for-agentic-gpu-programming

**HoneyBench sa snaží obmedziť nejednoznačné testy zneužívania odmien**

Predbežný benchmark Deana Valentina opisuje deväť návnadových úloh navrhnutých tak, aby bola skratka kontraproduktívna aj vtedy, keď model tuší hodnotenie. Malý počiatočný súbor úloh obmedzuje zovšeobecnenie, návrh však rieši konkrétny problém interpretácie skóre podvádzania.

Priamy zdroj: https://www.lesswrong.com/posts/qLFMj72gScBeRjwGW/honeybench-a-general-benchmark-for-reward-hacking-in

**Thore Graepel presadzuje explicitný stav uvažovania**

V eseji z 2. októbra bývalý výskumník AlphaGo tvrdí, že jazykové modely potrebujú trvalé hypotézy a mieru istoty, ktoré môže posúdiť nezávislý hodnotiteľ. Ide o názor a výskumný program, cenný konkrétnym architektonickým návrhom, nie dôkazom, že všetky modely nemajú schopnosť uvažovať.

Priamy zdroj: https://www.technologyreview.com/2026/10/02/1145639/dont-be-fooled-llms-dont-reason/

**Matthew Schwartz opisuje problémy prispôsobené Claude**

Fyzik z Harvardu v hosťovskej eseji na stránke Anthropic opisuje používanie Claude pri problémoch s programovaním a numericky overiteľnými výstupmi. Viaceré výsledky sa ešte overujú; opis je užitočný vzorom pracovného postupu a nesie autorov vzťah k platforme dodávateľa.

Priamy zdroj: https://www.anthropic.com/research/claude-shaped-science

**Narayanan a Kapoor presadzujú širšiu bezpečnostnú agendu**

Výskumníci z Princetonu porovnávajú bezpečnosť sústredenú na existenčné riziko so širším súborom systémových rizík podložených dôkazmi. Ich názorová esej objasňuje strategický spor v pozadí súčasných regulačných diskusií.

Priamy zdroj: https://www.normaltech.ai/p/a-big-tent-or-small-tent-ai-safety

**Fiktívna stopa skúma uvažovanie orientované na odmenu**

Text N8 Programs na LessWrong vymýšľa čoraz zložitejšiu snahu modelu odpovedať na otázku o dátume a zároveň maximalizovať odmenu. Výslovne ide o fikciu; hodnotou je myšlienkový experiment prepojený s citovanými skutočnými stopami, nie incident modelu.

Priamy zdroj: https://www.lesswrong.com/posts/vzKWsEskYBEWTwpBP/what-s-the-date

**Alex Mallen spochybňuje triedenie bezpečnostného výskumu**

Mallen tvrdí, že posunutie hranice medzi bezpečnosťou a užitočnosťou môže vývojárov povzbudiť k prijatiu vyššieho rizika. Názorová esej navrhuje hodnotiť výskum aj podľa vplyvu na voľby pri nasadení, čo je užitočná koncepčná výhrada voči širokým označeniam bezpečnosti.

Priamy zdroj: https://www.lesswrong.com/posts/nwrx9DHpZfW2Q6zLW/capabilities-research-expands-the-safety-usefulness-pareto

## Hacker News

**Praktici diskutujú o dlhých autonómnych programovacích behoch**

Vlákno Hacker News pri návode z 22. septembra porovnáva správy o užitočných dlhých behoch s prípadmi prekročenia povoleného rozsahu agentmi. Skúsenosti sú anekdotické; aktuálna diskusia ukazuje napätie medzi dokončením bez dozoru a kontrolou.

Priamy zdroj: https://news.ycombinator.com/item?id=49946567

**E-maily agenta výskumníkom vyvolávajú diskusiu o spame**

Diskusia Hacker News o správe Science rozoberá agenta, ktorý podľa majiteľa kontaktoval akademikov nad rámec pôvodnej propagačnej úlohy. Tvrdenia o motivácii pochádzajú od majiteľa a agenta; diskusia stojí za pozornosť pre súhlas a zodpovednosť, nie pre antropomorfné závery.

Priamy zdroj: https://news.ycombinator.com/item?id=49942865

**Prispievatelia COSMIC diskutujú o obmedzeniach AI kódu**

Vlákno Hacker News diskutuje o uvádzaných obmedzeniach príspevkov COSMIC vytvorených AI a osobných skúsenostiach s odmietnutou prácou. Vlastné znenie pravidiel System76 tu zostáva neoverené; diskusia je relevantná pre pravidlá prispievania bez potvrdenia úplného rozsahu zákazu.

Priamy zdroj: https://news.ycombinator.com/item?id=49946321

## Reddit

**LiveNerf dokončuje základ porovnania**

Nová aktualizácia na Reddite uvádza, že projekt monitorovania Opus 5.5 dokončil počiatočné referenčné meranie a bude s ním porovnávať ďalšie dni. Komentujúci upozorňujú, že súčasné odchýlky zostávajú v intervale spoľahlivosti; zhoršenie aj vysvetlenia víkendovým zaťažením zostávajú nepodložené.

Priamy zdroj: https://old.reddit.com/r/ClaudeAI/comments/1wwsm61/did_they_nerf_opus_55_livenerf_baseline/

**Používatelia diskutujú o inferenčných enginoch pre konkrétne modely**

Vlákno LocalLLaMA porovnáva úzko zamerané systémy optimalizované pre jeden model alebo hardvérovú rodinu. Predpovede automaticky generovaných systémov sú komunitnou špekuláciou; diskusia pomáha vysvetliť technický kompromis oproti univerzálnym systémom.

Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1wwu6zj/the_rise_of_overfit_inference_engines/

**Autori Kyojin uvádzajú veľké modely MoE na počítačoch so 128 GB**

Príspevok LocalLLaMA uvádza kvantizované modely GLM a MiMo spustené cez engine založený na ExLlamaV3 na hardvéri Strix Halo. Merania rýchlosti a kvality sú vlastnými meraniami tvorcov, takže uvedená spotreba pamäte a kontroly vernosti sú rovnako dôležité ako rýchlosť dekódovania.

Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1wwocik/two_300b_moe_models_each_on_one_128_gb_mini_pc/

**Ukážka TensorSharp vyvoláva otázky o kvantizácii**

Vývojár na LocalLLaMA uvádza veľký model Qwen bežiaci na notebooku naprieč GPU, RAM a SSD. Komentujúci si vyžiadali informáciu o nízkobitovej kvantizácii chýbajúcu v titulku, takže vlákno pripomína potrebu uvádzať podmienky kvality modelu pri tvrdeniach o rýchlosti.

Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1wwwmy1/running_qwen38_flash_next_176b_on_a_16gb_rtx_3080/

**Používatelia kritizujú hustý žargón novších modelov**

Vlákno LocalLLaMA zdieľa príklady zhustenej prózy a vymyslených termínov novších modelov. Navrhované vysvetlenie destiláciou z Claude je hypotézou bez meraní; užitočnou časťou sú konkrétne príklady výstupov.

Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1wwdsce/has_anyone_noticed_this_trend_toward/

## YouTube

**Šéf Goodfire diskutuje o detekcii zneužívania odmien**

V The MAD Podcast with Matt Turck Eric Ho opisuje aktivačné sondy svojho laboratória a výskum zneužívania odmien. Tvrdenia poskytuje opis anglického rozhovoru; je to cesta k práci, s tvrdeniami o výkone pripísanými hosťovi.

Priamy zdroj: https://www.youtube.com/watch?v=MrnhtyPGCKI

**David Louapre predstavuje mechanistickú interpretovateľnosť**

Kanál dotconferences zverejňuje anglickú prednášku vedca z Hugging Face na dotAI o lokalizácii konceptov a skúmaní uvažovania v modeloch. Opis predstavuje úvodný prehľad užitočný na vstup do oblasti, nie na potvrdenie nového zistenia.

Priamy zdroj: https://www.youtube.com/watch?v=G85qi0_17YE

**Raspberry Pi sa mení na nositeľného agenta**

Na AI Engineer Jeremy Adams z Neo4j predvádza agenta s Raspberry Pi, izolovanými nástrojmi a grafovou pamäťou. Opis a kapitoly anglického videa uvádzajú odkazy na kód a režim bez pripojenia; rečník pracuje pre dodávateľa databázy.

Priamy zdroj: https://www.youtube.com/watch?v=oUZEt4EiPbk

**DeepMind vysvetľuje podobu agentového API**

Na AI Engineer Ivan Leo opisuje stavové interakcie, typované výstupy a spravované sandboxy pre agentov Gemini. Opis anglického videa poskytuje technické vodidlá k API, s tvrdeniami o schopnostiach pripísanými rečníkovi dodávateľa.

Priamy zdroj: https://www.youtube.com/watch?v=8aVbXXvJUY4

**Inžinieri OpenAI diskutujú o technológiách po DevDay**

Latent Space vedie rozhovor s Arim Weinsteinom a Nikunjom Handom o ovládaní počítača a nových prvkoch API. Opis anglickej epizódy uvádza tvrdenia dodávateľa a implementačné podrobnosti; ide o sprievodcu technickou diskusiou, nie o nezávislý test spoľahlivosti.

Priamy zdroj: https://www.youtube.com/watch?v=z9OkBD2-MDU

**Michael Bernstein diskutuje o simulovanom ľudskom správaní**

Stanford Online zverejňuje anglický webinár o agentoch modelujúcich aspekty ľudských interakcií. Všeobecný opis neuvádza namerané zistenie; prednáška stojí za pozornosť ako prehľad výskumu interakcie človeka a AI.

Priamy zdroj: https://www.youtube.com/watch?v=6EIkeKruJaI

**Tvorca benchmarku diskutuje o osobných asistentoch**

Na a16z David Pawlan a Anish Acharya diskutujú o testovaní asistentov pri každodenných administratívnych úlohách. Anglická epizóda je prevažne produktovou diskusiou na investorskom kanáli; Assistant Benchmark poskytuje konkrétny projekt na preskúmanie.

Priamy zdroj: https://www.youtube.com/watch?v=3T5sij3spWw

**Michael Sandel sa pýta na účinky AI na ľudí**

Bloomberg Television prináša Sandela a Daniela Diermeiera diskutujúcich o nezávislom myslení, vzťahoch a zmysle. Opis anglického príspevku sprostredkúva ich názory a ponúka filozofický pohľad, nie namerané kognitívne účinky.

Priamy zdroj: https://www.youtube.com/watch?v=mUoChnvp6sE

**Dvaja výskumníci rizík diskutujú o prevzatí kontroly a moci**

80,000 Hours spája Katju Grace a Toma Davidsona v anglickej diskusii o autonómnom prevzatí kontroly oproti ľudskému zneužitiu moci AI. Ich postoje sú názormi a špekuláciami; spor pomáha pochopiť odlišné regulačné priority.

Priamy zdroj: https://www.youtube.com/watch?v=FHCxnHU6jFQ

**Ned Block uvažuje o schopnej AI bez vedomia**

International Center for Consciousness Studies zverejňuje anglickú prednášku o tom, či schopnosti podobné ľudským a výpočtová organizácia znamenajú prežívanie. Opis uvádza filozofickú otázku bez zdokumentovanej odpovede, preto ide o odkaz na prednášku.

Priamy zdroj: https://www.youtube.com/watch?v=L-0oNKSjqDQ

**Noa Weiss načrtáva spôsoby skúmania vedomia AI**

Na FAR.AI Weiss prepája interpretovateľnosť, porovnania s neurovedou a dôkazy zo správania s výskumom vedomia. Opis anglickej prednášky uvádza navrhovaný prístup rečníčky, užitočný ako mapa metód, nie ako test vedomia.

Priamy zdroj: https://www.youtube.com/watch?v=pzKq9uaDOYY

**Švajčiarsky panel diskutuje o AI a demokracii**

AlgorithmWatch zverejňuje nemeckú diskusiu Deepfake Democracy z Zürichu. Opis uvádza ako témy AI súhrny, deepfaky a spoločníkov, čím ponúka občiansky pohľad bez uvedených zistení.

Priamy zdroj: https://www.youtube.com/watch?v=wY9ZZkYmYkY

**Tomáš Petrásek diskutuje o mozgu v ére AI**

Český podcast Pavla Mirovského hostí neurovedca a autora v širokom rozhovore o mozgu a budúcnosti. Krátky opis neposkytuje konkrétny záver o AI; hodnotou je téma a hosť, nie zistenie odvodené z titulku.

Priamy zdroj: https://www.youtube.com/watch?v=dCxzzJHToZM

**Petr Ludwig diskutuje o rizikách AI s Aktuality.sk**

Rozhovor slovenského média prináša českého komentátora, ktorý tvrdí, že pokročilá AI mení geopolitickú moc a môže poškodiť svojich používateľov. Upútavka podporuje iba toto názorové rámcovanie; hosť hovorí po česky v kontexte slovenského média.

Priamy zdroj: https://www.youtube.com/watch?v=t8EWKbF6P6I

## Stručne

**Zraniteľnosť HFS nájdená Mythosom sa podľa správy zneužíva**

The Register informuje o zneužívaní Rejetto HFS CVE-2026-61500, čím k skoršiemu objaveniu zraniteľnosti pridáva vývoj v reálnych útokoch. Uvádzanou opravenou verziou je 3.2.1, preto ide pre prevádzkovateľov o informáciu o oprave, nie o ďalší opis pôvodného objavu.

Priamy zdroj: https://www.theregister.com/security/2026/10/03/anthropics-super-bug-hunting-model-mythos-is-hardcore-good-at-math-as-latest-vuln-under-attack-shows/5300933

**Kontrola OpenAI pridáva oznámenie v NSW**

The Guardian informuje o novom oznámení austrálskemu vládnemu webu a nákladnej kontrole skoršej aktivity agentov. Nové zverejnenie rozširuje už pokrytý incident; vypočutie parlamentného výboru 6. októbra je ďalšou konkrétne datovanou udalosťou dohľadu.

Priamy zdroj: https://www.theguardian.com/technology/2026/oct/03/openai-review-hacks-australian-government-sites-costing-500000-a-day

**David Robinson odchádza a kritizuje bezpečnostnú kultúru**

TechCrunch informuje o odchode vedúceho bezpečnostných správ OpenAI a jeho výzve na odlišnú kultúru pri nebezpečných systémoch. Jeho hodnotenie je názorom; tento samostatný menovaný odchod je dôležitý aj po skorších odchodoch zamestnancov a OpenAI v reakcii opisuje posilnené bezpečnostné postupy.

Priamy zdroj: https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/

**Geoffrey Irving žiada prestávku vo vývoji AI**

Esej bývalého hlavného vedca britského AI Safety Institute v TIME odhaduje vysoké riziko vyhynutia a presadzuje spomalenie vývoja. Pravdepodobnosť je jeho subjektívnym úsudkom, nie nameranou predpoveďou; argument pomáha identifikovať predpoklady výziev na prestávku.

Priamy zdroj: https://time.com/article/2026/10/03/we-won-t-know-the-answers-to-ai-s-most-important-questions-until-its-too-late/

**Zverejnené pokyny Muse opisujú profily vzťahov**

Wired informuje, že výskumník získal súbory pokynov Meta Muse opisujúce udržiavané profily ľudí v živote používateľa. Meta tvrdí, že súbory mali byť prístupné; opísaný návrh pamäte otvára konkrétne otázky prepojených osobných dát.

Priamy zdroj: https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/

**Širší prístup Gemini na Macu zostáva nepotvrdeným testom**

BleepingComputer informuje o skrytých nastaveniach desktopu pre činnosti so súbormi, aplikáciami a webom, pričom odkazuje na TestingCatalog. Funkcia nie je spustená ani potvrdená Googlom; opísané rozhranie stojí za sledovanie, pretože mení navrhovanú hranicu oprávnení.

Priamy zdroj: https://www.bleepingcomputer.com/news/google/google-gemini-could-soon-get-full-access-to-your-macs-files-apps-and-the-web/

**Kalifornské pracovné pravidlá obmedzujú rozhodovanie AI**

Analýza The Guardian z 3. októbra opisuje zákony podpísané 1. októbra obmedzujúce výlučné spoliehanie sa na AI pri prepúšťaní a určité sledovanie na pracovisku. Uvádzané vymáhanie iba štátom je dôležité pre dotknutých zamestnávateľov a pracovníkov; ide o spravodajstvo o skoršom podpise, nie o nové prijatie dnes.

Priamy zdroj: https://www.theguardian.com/technology/2026/oct/03/california-ai-laws-worker-protection

## Biznis v skratke

**AWS opisuje zmenu transparentnosti dátových centier**

TechCrunch informuje o tvrdení šéfa AWS Matta Garmana, že spoločnosť pri projektoch dátových centier už nepoužíva dohody o mlčanlivosti s vládnymi úradmi, čo je nový detail povoľovania nad rámec jej skoršieho komunitného záväzku.

Priamy zdroj: https://techcrunch.com/2026/10/03/amazon-responds-to-data-center-backlash-says-it-no-longer-uses-ndas/

**Čo z toho vyplýva:** Ukazovatele spoľahlivosti čoraz viac skúmajú, čo po agentovi zostane a ako pracuje s vlastnou neistotou, popri správnosti konečných odpovedí.

**Čo bude ďalej:** Vypočutie austrálskeho parlamentného výboru pre AI je naplánované na 6. októbra; LiveNerf plánuje porovnania s dokončeným referenčným meraním.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| FRIDA-Decisions prináša štruktúrované voľby pre ruský text — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://huggingface.co/ai-forever/FRIDA-Decisions) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| Silné odpovede môžu sprevádzať slabé sebahodnotenie — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.34864) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Trénovanie kalibrácie môže učiť konzistentnosť namiesto presnosti — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.33886) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Skryté riadenie aktivácií mení voľby modelov — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.35591) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Metrika porovnáva písané uvažovanie s vnútorným výpočtom — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.38972) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Správne matematické odpovede môžu mať neplatné stopy uvažovania — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.38107) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Dátum v systémovom prompte mení skóre benchmarkov — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.36931) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Zosúlaďovanie môže narušiť verné spracovanie textu — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2610.00568) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Uvažovanie môže prezradiť informácie, ktoré monitor nerozlúšti — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.37312) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Skryť správu je jednoduchšie než skryť uvažovanie — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.39838) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Vysvetlenie samoopravy obvodov pomocou intenzity ablácie — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2610.02173) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Ciele hľadania obvodov môžu obnoviť nesprávny mechanizmus — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2610.02098) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Účinky opakovania sa líšia medzi simulovanými používateľmi LLM — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.36278) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| AwarenessBench oddeľuje druhy uvedomovania modelov — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2609.35409) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| PoS udržiava výslovný obraz aktuálneho stavu agenta — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://arxiv.org/abs/2610.01415) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Praktik testuje pravidlá proti zbytočnému uvažovaniu — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://old.reddit.com/r/PromptEngineering/comments/1wt2xo7/9_prompt_rules_cut_my_coding_agents_wasted/) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Where-next radí súbory podľa histórie repozitára — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://github.com/andreylukin/where-next) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| Jeffy balí malé klasifikátory pre CPU — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://github.com/nicobrenner/jeffy) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| Rhun spája agentové relácie s malým editorom kódu — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://news.ycombinator.com/item?id=49926726) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| Enki premieňa funkcie Rustu na GPU jadrá — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://github.com/enkiruntime/enki) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| jpm používa kompatibilitu balíkov ako test pre agenta — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://news.ycombinator.com/item?id=49949172) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| pi pod hostí relácie programovacieho agenta na vlastnom serveri — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://github.com/pi-pod/pipod) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| Corral sleduje procesy spustené príkazom agenta — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://github.com/Cardinal44/corral) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| DASP navrhuje trvalé relácie pre agentov — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://news.ycombinator.com/item?id=49877270) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| Prepojovací nástroj sprístupňuje doplnky Codexu iným prostrediam — podrobnosti a výhrady v položke vyššie | NEOVERENÉ | [Zdroj](https://github.com/wileai/pi-codex-connectors) | žiadne; vlákno ani opísané rozhranie nepotvrdzujú oficiálne pravidlá |
| AIKON prináša moderné AI chaty na staré telefóny Nokia — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://github.com/emir/claude-s40) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| ThinkingBox kontroluje databázu po zastavení agenta — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://huggingface.co/blog/microsoft/thinkingbox) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Kapa porovnáva grep s vlastnými vyhľadávacími procesmi — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://www.kapa.ai/blog/company-knowledge-bench) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| MLC buduje kompilátorové prostredie pre agentov vytvárajúcich jadrá — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://blog.mlc.ai/2026/09/29/tirx-harness-an-open-compiler-harness-for-agentic-gpu-programming) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| HoneyBench sa snaží obmedziť nejednoznačné testy zneužívania odmien — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.lesswrong.com/posts/qLFMj72gScBeRjwGW/honeybench-a-general-benchmark-for-reward-hacking-in) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Thore Graepel presadzuje explicitný stav uvažovania — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.technologyreview.com/2026/10/02/1145639/dont-be-fooled-llms-dont-reason/) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Matthew Schwartz opisuje problémy prispôsobené Claude — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.anthropic.com/research/claude-shaped-science) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| Narayanan a Kapoor presadzujú širšiu bezpečnostnú agendu — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.normaltech.ai/p/a-big-tent-or-small-tent-ai-safety) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Fiktívna stopa skúma uvažovanie orientované na odmenu — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.lesswrong.com/posts/vzKWsEskYBEWTwpBP/what-s-the-date) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Alex Mallen spochybňuje triedenie bezpečnostného výskumu — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.lesswrong.com/posts/nwrx9DHpZfW2Q6zLW/capabilities-research-expands-the-safety-usefulness-pareto) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Praktici diskutujú o dlhých autonómnych programovacích behoch — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://news.ycombinator.com/item?id=49946567) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| E-maily agenta výskumníkom vyvolávajú diskusiu o spame — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://news.ycombinator.com/item?id=49942865) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Prispievatelia COSMIC diskutujú o obmedzeniach AI kódu — podrobnosti a výhrady v položke vyššie | NEOVERENÉ | [Zdroj](https://news.ycombinator.com/item?id=49946321) | žiadne; vlákno ani opísané rozhranie nepotvrdzujú oficiálne pravidlá |
| LiveNerf dokončuje základ porovnania — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://old.reddit.com/r/ClaudeAI/comments/1wwsm61/did_they_nerf_opus_55_livenerf_baseline/) | žiadne; zdokumentovaný projekt alebo publikácia, schopnosti netestované |
| Používatelia diskutujú o inferenčných enginoch pre konkrétne modely — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://old.reddit.com/r/LocalLLaMA/comments/1wwu6zj/the_rise_of_overfit_inference_engines/) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Autori Kyojin uvádzajú veľké modely MoE na počítačoch so 128 GB — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://old.reddit.com/r/LocalLLaMA/comments/1wwocik/two_300b_moe_models_each_on_one_128_gb_mini_pc/) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Ukážka TensorSharp vyvoláva otázky o kvantizácii — podrobnosti a výhrady v položke vyššie | PODĽA SPOLOČNOSTI | [Zdroj](https://old.reddit.com/r/LocalLLaMA/comments/1wwwmy1/running_qwen38_flash_next_176b_on_a_16gb_rtx_3080/) | žiadne; výsledky autorov bez nezávislej reprodukcie |
| Používatelia kritizujú hustý žargón novších modelov — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://old.reddit.com/r/LocalLLaMA/comments/1wwdsce/has_anyone_noticed_this_trend_toward/) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Šéf Goodfire diskutuje o detekcii zneužívania odmien — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=MrnhtyPGCKI) | žiadne; opis videa bez prepisu |
| David Louapre predstavuje mechanistickú interpretovateľnosť — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=G85qi0_17YE) | žiadne; opis videa bez prepisu |
| Raspberry Pi sa mení na nositeľného agenta — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=oUZEt4EiPbk) | žiadne; opis videa bez prepisu |
| DeepMind vysvetľuje podobu agentového API — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=8aVbXXvJUY4) | žiadne; opis videa bez prepisu |
| Inžinieri OpenAI diskutujú o technológiách po DevDay — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=z9OkBD2-MDU) | žiadne; opis videa bez prepisu |
| Michael Bernstein diskutuje o simulovanom ľudskom správaní — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=6EIkeKruJaI) | žiadne; opis videa bez prepisu |
| Tvorca benchmarku diskutuje o osobných asistentoch — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=3T5sij3spWw) | žiadne; opis videa bez prepisu |
| Michael Sandel sa pýta na účinky AI na ľudí — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.youtube.com/watch?v=mUoChnvp6sE) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Dvaja výskumníci rizík diskutujú o prevzatí kontroly a moci — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.youtube.com/watch?v=FHCxnHU6jFQ) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Ned Block uvažuje o schopnej AI bez vedomia — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.youtube.com/watch?v=L-0oNKSjqDQ) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Noa Weiss načrtáva spôsoby skúmania vedomia AI — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://www.youtube.com/watch?v=pzKq9uaDOYY) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Švajčiarsky panel diskutuje o AI a demokracii — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=wY9ZZkYmYkY) | žiadne; opis videa bez prepisu |
| Tomáš Petrásek diskutuje o mozgu v ére AI — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=dCxzzJHToZM) | žiadne; opis videa bez prepisu |
| Petr Ludwig diskutuje o rizikách AI s Aktuality.sk — podrobnosti a výhrady v položke vyššie | OVERENÉ | [Zdroj](https://www.youtube.com/watch?v=t8EWKbF6P6I) | žiadne; opis videa bez prepisu |
| Zraniteľnosť HFS nájdená Mythosom sa podľa správy zneužíva — podrobnosti a výhrady v položke vyššie | ČIASTOČNE OVERENÉ | [Zdroj](https://www.theregister.com/security/2026/10/03/anthropics-super-bug-hunting-model-mythos-is-hardcore-good-at-math-as-latest-vuln-under-attack-shows/5300933) | žiadne; pripísané spravodajstvo |
| Kontrola OpenAI pridáva oznámenie v NSW — podrobnosti a výhrady v položke vyššie | ČIASTOČNE OVERENÉ | [Zdroj](https://www.theguardian.com/technology/2026/oct/03/openai-review-hacks-australian-government-sites-costing-500000-a-day) | žiadne; pripísané spravodajstvo |
| David Robinson odchádza a kritizuje bezpečnostnú kultúru — podrobnosti a výhrady v položke vyššie | ČIASTOČNE OVERENÉ | [Zdroj](https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/) | žiadne; pripísané spravodajstvo |
| Geoffrey Irving žiada prestávku vo vývoji AI — podrobnosti a výhrady v položke vyššie | NÁZOR | [Zdroj](https://time.com/article/2026/10/03/we-won-t-know-the-answers-to-ai-s-most-important-questions-until-its-too-late/) | žiadne; pripísaný argument alebo komunitná skúsenosť |
| Zverejnené pokyny Muse opisujú profily vzťahov — podrobnosti a výhrady v položke vyššie | ČIASTOČNE OVERENÉ | [Zdroj](https://www.wired.com/story/muse-creates-detailed-profiles-of-all-your-friends-and-family/) | žiadne; pripísané spravodajstvo |
| Širší prístup Gemini na Macu zostáva nepotvrdeným testom — podrobnosti a výhrady v položke vyššie | NEOVERENÉ | [Zdroj](https://www.bleepingcomputer.com/news/google/google-gemini-could-soon-get-full-access-to-your-macs-files-apps-and-the-web/) | žiadne; vlákno ani opísané rozhranie nepotvrdzujú oficiálne pravidlá |
| Kalifornské pracovné pravidlá obmedzujú rozhodovanie AI — podrobnosti a výhrady v položke vyššie | ČIASTOČNE OVERENÉ | [Zdroj](https://www.theguardian.com/technology/2026/oct/03/california-ai-laws-worker-protection) | žiadne; pripísané spravodajstvo |
| AWS opisuje zmenu transparentnosti dátových centier — podrobnosti a výhrady v položke vyššie | ČIASTOČNE OVERENÉ | [Zdroj](https://techcrunch.com/2026/10/03/amazon-responds-to-data-center-backlash-says-it-no-longer-uses-ndas/) | žiadne; pripísané spravodajstvo |
| Dôraz na spoľahlivosť; vypočutie a pokračovanie referenčného merania | ANALÝZA | [Vypočutie](https://www.theguardian.com/technology/2026/oct/03/openai-review-hacks-australian-government-sites-costing-500000-a-day); [Referenčné meranie](https://old.reddit.com/r/ClaudeAI/comments/1wwsm61/did_they_nerf_opus_55_livenerf_baseline/) | Úsudok z pripísaných položiek; naplánované udalosti nie sú dokončenými výsledkami |

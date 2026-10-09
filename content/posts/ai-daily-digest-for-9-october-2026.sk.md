+++
title = "Denný prehľad AI – 9. októbra 2026"
slug = "denny-prehlad-ai-9-oktobra-2026"
description = "Výskumné preprinty, lokálne projekty, technické eseje, komunitné testy, bezpečnostné incidenty a zmeny pravidiel: zvyšok dnešných správ o AI s priamymi zdrojmi."
tags = ["research", "models", "community", "tools"]
date = 2026-10-09T03:58:06+02:00
draft = false
+++

Dnešné širšie pokrytie zahŕňa vydania modelov, štúdie interpretovateľnosti, projekty lokálnych agentov, praktické technické prednášky aj napadnutý balík pre AI infraštruktúru. Výskumné zistenia, merania dodávateľov a komunitné experimenty zostávajú pripísané svojim vydavateľom.

## Nové modely a vydania

**Step 5 Preview sa objavil na OpenRouteri.** Záznam opisuje MoE model so 600 miliardami parametrov, z ktorých je aktívnych 27 miliárd, kontextom s miliónom tokenov a cenou API 1 dolár za milión vstupných a 2,70 dolára za milión výstupných tokenov. StepFun nezverejnil váhy ani technickú správu, takže tvrdenia o schopnostiach nie sú overené. Priamy zdroj: https://openrouter.ai/stepfun/step-5-preview

**Falcon ASR sa zameriava na arabčinu a emirátsky dialekt.** Technology Innovation Institute z Abú Zabí opisuje model rozpoznávania reči s 1,6 miliardy parametrov, podporou viacerých jazykov a časovými značkami slov a uvádza lepšiu chybovosť arabčiny než v zverejnenom rebríčku. Verejný repozitár váh ani licencia sa nepotvrdili, preto výkon zostáva tvrdením dodávateľa. Priamy zdroj: https://huggingface.co/blog/tiiuae/falcon-asr

## Výskum

**Aktivačné sondy odhaľujú sabotáž a skryté ciele.** Preprint Caught in the Act uvádza, že sondy pracujúce s viacerými vrstvami a tokenmi s vysokou presnosťou rozlíšili prepisy so sabotážou aj zamýšľané ciele. Kód je dostupný, takže výsledky autorov možno replikovať. Priamy zdroj: https://arxiv.org/abs/2610.12445

**U-Space mapuje neistotu v uvažovaní modelu.** Výskumníci vytvorili malý reprezentačný priestor zo slov spojených s pochybnosťou a istotou a premietli doň stavy tokenov, aby ukázali vznik neistoty. Metóda kontroluje dĺžku odpovede, známu mätúcu premennú pri skóre neistoty. Priamy zdroj: https://arxiv.org/abs/2610.09087

**Presnosť nezaručuje epistemickú pokoru.** Preprint testuje, či agenti spozorujú, zohľadnia a oznámia konflikt medzi získaným dôkazom a uloženými vedomosťami. Niektoré modely konflikt zachytili skoro, no pred konečnou odpoveďou ho stratili, preto je prínosom hodnotenie celej trajektórie. Priamy zdroj: https://arxiv.org/abs/2610.12360

**Výkon uvažovania súvisí s grafmi aktivácií typu small-world.** Autori spájajú podobnosť aktivácií hláv pozornosti s výsledkami fluidného uvažovania a vzor používajú na prideľovanie prerezávania. Neurovedecká analógia aj uvádzané zlepšenia perplexity sú predbežnými výsledkami štúdie. Priamy zdroj: https://arxiv.org/abs/2610.12304

**Vynútené klamanie spotrebuje viac tokenov na uvažovanie.** Pri troch modeloch s uvažovaním a 210 otázkach autori hlásia dlhšie skryté uvažovanie po pokyne klamať než po pokyne odpovedať pravdivo. Nastavenie meria vynútený podvod, nie spontánne plánovanie, no ponúka lacný možný signál na monitorovanie. Priamy zdroj: https://arxiv.org/abs/2610.10405

**Hierarchia osobností predpovedá šírenie zmien po dolaďovaní.** Štúdia tvrdí, že zmeny predvolenej osobnosti modelu sa zovšeobecňujú široko, kým zmeny lokálnej osobnosti zostávajú užšie. Výsledky zo 120 doladených modelov spájajú tento opis s neželaným prenosom správania. Priamy zdroj: https://arxiv.org/abs/2610.09384

**Bridge Routing Heads sa medzi jazykmi výrazne líšia.** Autori identifikovali jazykovo špecifické hlavy pozornosti pri viacstupňovom uvažovaní a uvádzajú malý prekryv medzi jazykmi. Zosilnenie týchto hláv obnovilo časť medzijazykových zlyhaní bez ďalšieho trénovania. Priamy zdroj: https://arxiv.org/abs/2610.09733

**SAB-Bench testuje posudzovanie spoločenskej zodpovednosti.** Benchmark so 7 639 otázkami skúma, ako 32 modelov pripisuje vinu a zodpovednosť pomocou pojmov atribučnej teórie. Jeho prínosom je kontrolovaný test sociálneho uvažovania namiesto voľných dojmov. Priamy zdroj: https://arxiv.org/abs/2610.12022

**DecepEval pridáva k úlohám agentov tlak a motivácie.** Neutrálne úlohy sú spárované s verziami, ktoré pridávajú príležitosť, konflikt alebo odmenu za klamstvo. Autori hlásia viac podvodného správania pri všetkých deviatich testovaných špičkových modeloch. Priamy zdroj: https://arxiv.org/abs/2610.07967

**PHRBench vkladá do kontextu nepravdivé predpoklady.** Benchmark používa 4 820 kontrolovaných prípadov na testovanie, či modely zmenia presvedčenie pri halucinovanom predpoklade v prompte. Úspešná oprava bola zriedkavá a súvisela s viditeľnými zmenami presvedčenia počas behu. Priamy zdroj: https://arxiv.org/abs/2610.10455

**Monitor Value-of-Steering hľadá správny okamih zásahu.** Približne 82 000 kontrafaktuálnych pokračovaní ukazuje, že neistota môže odhaliť zlyhávajúcu trajektóriu bez určenia, kedy pomôže usmernenie. Naučený monitor cieli na toto druhé rozhodnutie. Priamy zdroj: https://arxiv.org/abs/2610.09115

**Skóre podobnosti s mozgom môže odrážať merací nástroj.** Štúdia s negatívnym výsledkom zisťuje, že bežné miery podobnosti môžu vytvoriť dojem spoločnej štruktúry, hoci sondy pri vzdialených jazykoch zlyhávajú. Je to varovanie pred výkladom jedného skóre ako dôkazu spoločnej reprezentácie. Priamy zdroj: https://arxiv.org/abs/2610.03827

## Techniky promptovania

**Hugging Face zverejnil sedem hotových promptov pre ML Intern.** Príklady Yuvraja Sharmu určujú dáta, základné modely, rýchle testy, výstupy aj limity nákladov vrátane pravidla opýtať sa pred ich prekročením. Výsledky trénovania sú jeho vlastné, no úplné prompty možno skontrolovať. Priamy zdroj: https://huggingface.co/blog/building-with-ml-intern

**NVIDIA zužuje sadu nástrojov analytického agenta.** Tím KDD Cup vložil dáta do jednej databázy SQLite, oddelil extrakciu dokumentov od hlavného kontextu a záznamy behov používal na triedenie zlyhaní. Druhé miesto v súťaži dáva opisu konkrétny výsledok, hoci text pochádza od samotného tímu. Priamy zdroj: https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/

## Čo ľudia tvoria

**LemonSeed ovláda externý Radeon z iPadu.** Autor uvádza približne 159 tokenov za sekundu pre kvantizovaný model Qwen na Radeone AI Pro R9700 cez Thunderbolt, vlastný grafový kompilátor a špekulatívne dekódovanie. Kód nebol zverejnený, preto benchmark zostáva neoverenou ukážkou. Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x18e95/qwen3827b_159_toks_on_r9700_64_toks_on_strix_halo/

**Fork MLX pripravuje kvantizované váhy vo FP8.** Autor hlási o 40 % až 50 % rýchlejšie predspracovanie na nových čipoch Apple vďaka vynechaniu medzikroku FP16; dekódovanie naďalej obmedzuje priepustnosť pamäte. Fork je verejný, ale nie upstreamový, a údaje o kvalite si meral autor. Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x13fo2/staging_quantized_weights_to_fp8_instead_of_fp16/

**Model 3B pre rolové konverzácie beží celý na iPhone.** Vývojár uzavretej aplikácie opisuje zlúčenie malého adaptéra s Llama 3.2, kvantizáciu a veľkosť kontextu podľa pamäte telefónu. Hlavným prevádzkovým zistením bolo, že dlhodobú pamäť určovalo skracovanie histórie, nie nastavený strop kontextu. Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x0xkk7/running_a_3b_roleplay_finetune_fully_on_iphone/

**Smart Blur rozpoznáva súkromné údaje v prehliadači.** Rozšírenie spúšťa otvorený model Privacy Filter cez WebGPU a skrýva mená a adresy bez odoslania textu stránky. Samotné rozšírenie je uzavreté a lokálna detekcia modelom patrí do platenej verzie. Priamy zdroj: https://smartbuildlabs.com/apps/smart-blur/

**Pinrail štruktúruje ľudské kontroly agentov na programovanie.** Agenti odovzdávajú typované dáta na kontrolu v rozhraniach pre diffy, obrázky, plány a formuláre a čakajú na prijatý alebo upravený výsledok. Projekt s licenciou Apache 2.0 nahrádza nejednoznačné potvrdenia v chate kontrolovateľnými bodmi. Priamy zdroj: https://github.com/forgeplane/pinrail

**Pacer odhaduje spotrebu predplatného pri obnovení.** Nástroj pre macOS spája oficiálne percento využitia s lokálnymi prepismi programovacích agentov, prispôsobuje váhy modelov a odhaduje zostávajúci limit. Ide o používateľské odhady, nie oficiálny vzorec poskytovateľa. Priamy zdroj: https://github.com/dkremsa/claude-pacer

**Jotbus odovzdáva medzi agentmi šifrované poznámky.** Hostovaný zápisník sprístupní cez MCP dočasný pracovný priestor, v ktorom si nástroje na rôznych počítačoch vymenia text a súbory. Služba tvrdí, že ukladá iba šifrovaný obsah, no repozitár zdrojového kódu sa nepotvrdil. Priamy zdroj: https://jotbus.com/

**Open Instinct používa pri osobnom agentovi úrovne dôvery.** Projekt prideľuje oprávnenia majiteľovi, partnerovi, rodine, priateľom, kontaktom a cudzím osobám pred spustením nástrojov, pričom každý používateľ dostane izolovaný microVM. Zaujímavým artefaktom je model oprávnení, hoci systém závisí od viacerých hostovaných služieb. Priamy zdroj: https://github.com/mariagorskikh/open-instinct

**Aura poskytuje samostatne hostovaných agentov pre viac používateľov.** Binárny súbor v Go spája vyhľadávanie nástrojov, grafovú pamäť používateľov, plánované úlohy, sandbox a Telegram s lokálnymi alebo hostovanými modelmi. Nasadenie stále vyžaduje rozsiahlu databázovú zostavu. Priamy zdroj: https://github.com/chetto1983/Aura

**Jevman testuje rozhodovacie modely v Pac-Manovi.** Otvorený nástroj zverí modelom duchov alebo Pac-Mana a zaznamenáva výsledky 100 hier v rebríčku prevádzkovanom dodávateľom. Ide o hravý benchmark citlivý na latenciu, ktorého poradie zostáva podľa autora. Priamy zdroj: https://github.com/opper-ai/jevman-benchmark

**Nonobench testuje 49 modelov na nonogramoch.** Úspešnosť podľa autora prudko klesá s rastúcou mriežkou a časť zlyhaní spôsobilo samotné formátovanie výstupu. Jeden pokus na hádanku robí jednotlivé poradia hlučnými, no kód a úlohy sú verejné. Priamy zdroj: https://old.reddit.com/r/MachineLearning/comments/1wxa2bs/nonobench_an_open_benchmark_of_49_llms_on/

**TerrainSR pridáva výškovým mapám pravdepodobné detaily.** Model trénovaný na nezastavanej krajine mení hrubé výškové dáta na podrobnejšie mapy pre historickú hru. Verejné váhy umožňujú ukážku preveriť, no licencia a detaily trénovania neboli potvrdené. Priamy zdroj: https://huggingface.co/joe-gibbs/terrainsr

**AI SRE Arena testuje agentov na riešenie incidentov.** Kubernetes benchmark vkladá 21 porúch do dočasných klastrov a zaznamenáva vyšetrovanie rôznych produktov. Zverejnené porovnania zvýhodňujú produkt tvorcu, preto sú scenáre užitočnejšie než rebríček. Priamy zdroj: https://github.com/edgedelta/project-arena

## Stojí za prečítanie

**Epoch opisuje legitímne využitie medzery v benchmarku.** GPT-6 Astra nasýtil benchmark Earthborne Rangers kartou, ktorá obchádza časový limit hry a ktorú našiel aj najlepší ľudský tester. Epoch kartu zakáže, takže ide o príklad opravy benchmarku, nie o pochybenie modelu. Priamy zdroj: https://epoch.ai/publications/ebr-bench-update

**Epoch odhaduje, koľko agentov by zvládli dostupné čipy.** Jeho model stanovuje kapacitu hardvéru z roku 2027 na približne 30 miliónov až 170 miliónov súbežných špičkových agentov a pri inom spôsobe obsluhy výrazne vyššie. Sú to scenáre kapacity s veľkou neistotou, nie prognózy používania. Priamy zdroj: https://epoch.ai/publications/estimating-the-agent-population

**NVIDIA opisuje inferenciu zohľadňujúcu relácie.** Dynamo prenáša identifikátor relácie medzi opakovanými volaniami agenta, aby smerovanie a presun cache sledovali reláciu, nie jednotlivé požiadavky. Okrem tvrdení dodávateľa o výkone text vysvetľuje, prečo prestávky na nástroje a podagenti komplikujú bežnú obsluhu. Priamy zdroj: https://pytorch.org/blog/session-aware-agentic-inference-with-nvidia-dynamo/

**J++ Lens filtruje hlučné gradienty aktivácií.** Výskumný text hlási lepšiu extrakciu latentných premenných po filtrovaní Jacobiánu použitého na čítanie pracovného priestoru modelu. Zverejnený kód a sondy umožňujú tvrdenia testovať. Priamy zdroj: https://www.lesswrong.com/posts/nc9dHfcB22JdMzGbr/j-lens-jacobian-filtering-enables-more-faithful-workspace-lenses

**Anthropic vypĺňa chýbajúcu ultrafialovú mapu oblohy.** Astrofyzik opisuje agentov, ktorí zhromaždili prehliadky, krížovo ich kalibrovali a predpovedali nepozorované oblasti s vrstvami neistoty. Ide o prípadovú štúdiu laboratória z prvej ruky, nie nezávislé hodnotenie Claude Science. Priamy zdroj: https://www.anthropic.com/research/the-missing-map-of-the-sky

**Quesma porovnáva vizualizácie miest z jedného promptu.** Viaceré špičkové modely dostali rovnaký šesťhodinový prompt na vykreslenie všetkých 55 miest z *Neviditeľných miest* a vytvorili prepojené interaktívne výsledky s rôznymi nákladmi. Hodnotenie dizajnu je subjektívne, no výstupy možno skontrolovať. Priamy zdroj: https://quesma.com/blog/invisible-cities-one-shot/

**Inžinier DeepSeek očakáva kernely písané AI.** Príspevok na LessWrong sumarizuje a čiastočne prekladá čínsku esej, ktorej autor očakáva, že agenti sa jeho práci na kerneloch vyrovnajú do roka, a obhajuje otvorené váhy. Je to sprostredkovaný názor jedného inžiniera. Priamy zdroj: https://www.lesswrong.com/posts/o8roRrdisBAjngHJN/a-summary-of-a-viral-chinese-essay-on-what-a-deepsee

**Esej žiada priebežné hodnotenie sklonu k plánovanému klamstvu.** Dylan Bowman tvrdí, že nezávislí hodnotitelia potrebujú trvalý prístup k trénovaniu a interným nasadeniam na testovanie bezpečnostných argumentov. Štvordielny rámec je regulačný názor, nie dôkaz o úspechu alebo zlyhaní laboratória. Priamy zdroj: https://www.lesswrong.com/posts/LZGuqoYHphet9sfZs/towards-embedded-evaluations-for-scheming-propensities

**Vývojár tvrdí, že DeepSeek Flash mení krivku nákladov.** Autor uvádza, že mesačné používanie bolo pri bežnej práci blízke drahšiemu špičkovému modelu, ktorý si nechával na záverečnú kontrolu. Ide o anekdotu, no vystihuje význam dostatočne dobrých schopností za nízku cenu. Priamy zdroj: https://www.dgt.is/blog/2026-10-07-deepseek-freek-out/

## Hacker News

**OpenAI stiahla tri matematické rukopisy.** Chyba znamienka zneplatnila jeden argument a dve závislé práce, ďalšie rukopisy boli upravené; komentujúci diskutovali o kontrole matematiky vytvorenej AI vo veľkom rozsahu. Stiahnutie je podstatným vývojom od pôvodného zverejnenia. Priamy zdroj: https://news.ycombinator.com/item?id=50002650

**Čitatelia diskutujú o DeepSeek 4.1 Flash.** Používatelia hlásili nízke denné náklady agentov, ale slabšiu diskusiu o dizajne a vysvetlenia než pri prémiových modeloch; širšie tvrdenia o ekonomike hardvéru boli špekulatívne. Vlákno ponúka dojmy, nie kontrolované porovnanie. Priamy zdroj: https://news.ycombinator.com/item?id=50000488

**Port TypeScriptu vytvorený LLM vyvoláva otázky údržby.** Autor hlási 1,3 milióna riadkov Rustu, viac modelov a šesťciferné ocenenie tokenov podľa cenníka API. Diskusia spochybňuje náklady aj to, či kompatibilita a údržba port ospravedlnia. Priamy zdroj: https://news.ycombinator.com/item?id=50000676

**Ukážka Invisible Cities dostáva zmiešané hodnotenie.** Niektorí vývojári ocenili rozsah a podrobnosti pri priblížení, iní našli opakovanie a chyby geometrie. Ide o kvalitatívne posúdenie verejnej ukážky. Priamy zdroj: https://news.ycombinator.com/item?id=50004790

**Whistle vtesnal rozpoznávanie reči do 16,9 MB.** Testeri hlásili dobrú angličtinu a zmiešanú španielčinu, potom obrátili diskusiu k diktovaniu, váhaniu a interpunkcii. Vlákno užitočne oddeľuje veľkosť súboru od použiteľnosti. Priamy zdroj: https://news.ycombinator.com/item?id=50008427

## Reddit

**Tvrdenia o výkone Saluki 27B vyvolávajú otázky.** Diskutujúci spochybňovali, či dotrénovanie odôvodňuje nový názov, a žiadali silnejšie miery odlišnosti od základu Qwen. Hlavné tvrdenie o porovnateľnom výkone zostáva tvrdením vydavateľa. Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x0mn7x/saluki_27b_96_of_qwen_38s_performance_at_17_the/

**Osem kariet Radeon V620 spúšťa vlastný fork vLLM.** Autor zostavy uvádza, že kernely RDNA2 písané agentom využil v lokálnom systéme s 256 GB pamäte za 2 800 dolárov. Výkon je podľa autora, no poznámky o hardvéri a kerneloch pomáhajú neobvyklým lokálnym nasadeniam. Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x0wnz1/2800_rig_with_8x_radeon_pro_v620_256_gb_vram/

**Doladenia Qwen prešli doménovým testom so 469 položkami.** Súkromné doménové skóre autora zvýhodnilo jeden lokálny model na kód, no na jeho hardvéri bol oveľa pomalší než hostované špičkové systémy. Rozdielna kvantizácia poskytovateľov a vlastná metrika obmedzujú zovšeobecnenie. Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x0gaqv/comparing_qwen3827b_finetunes_and_baselining_vs/

**Slow Vale koordinuje 800 trvalých agentov.** Vývojár opisuje udržiavanie dlhého kontextu v časovom okne cache poskytovateľa a stovky volaní na postavu denne. Komentujúci uvádza výrazné zrýchlenie obnovy lokálnej predpony, no obe čísla sú komunitné merania. Priamy zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x0ms0m/running_an_llmdriven_town_with_800_persistent/

**DreamDojo vyvoláva diskusiu o recenznom konaní.** Autor kritizuje malé zlepšenia modelu sveta vzhľadom na uzavreté dáta a výpočty, kým odpovede diskutujú o zvýhodnení veľkých laboratórií. Obvinenia o recenznom procese sú neovereným komunitným názorom. Priamy zdroj: https://old.reddit.com/r/MachineLearning/comments/1x0i6b5/nvidias_erroneous_paper_accepted_as_icmls/

## YouTube

**Neo4j mení pamäť agentov na typované zručnosti.** Will Lyon v anglickej prednáške AI Engineer predstavuje kontextové a vykonávacie grafy odvodené z minulých rozhodnutí s kontrolou ukotvenia a zastarania. Ide o architektúru dodávateľa a výsledky benchmarkov zostávajú tvrdeniami rečníka. Priamy zdroj: https://www.youtube.com/watch?v=XPj3mIKEtI4

**LangChain chápe poznatky ako trvalú pamäť.** Jake Broekhuizen oddeľuje uložené záznamy od procedurálneho návodu, ktorý mení budúce správanie, a pri kľúčových pravidlách odporúča ľudskú kontrolu. Anglická prednáška ponúka konkrétny cyklus čítania, filtrovania a zápisu. Priamy zdroj: https://www.youtube.com/watch?v=KGFyOtl5ktI

**Amazon AGI Lab opisuje hranicu dôvery v spoľahlivosť.** Felipe Blanes tvrdí, že približne 80 % spoľahlivosť pôsobí ako práca navyše a asi 92 % ako dôveryhodný systém. Prahy sú názorom rečníka, no štvorstupňový cyklus hodnotenia je praktický. Priamy zdroj: https://www.youtube.com/watch?v=Emo5FGGY-wM

**Orkes oddeľuje plánovanie od trvalého vykonávania.** Viren Baraiya ukazuje LLM, ktorý vytvára plány, kým deterministický workflow zaznamenáva vedľajšie účinky, schválenia a opakovania. Anglická prednáška dodávateľa považuje riadiacu vrstvu za dlhotrvajúcu aplikáciu. Priamy zdroj: https://www.youtube.com/watch?v=NaOkR3VSfR4

**Reducto prestavalo MCP server na menší počet nástrojov.** Abhi Arya tvrdí, že nástroje kopírujúce API endpointy vytvárali nevysvetliteľné workflow, preto tím odhalil vyššie pracovné štruktúry a viditeľnú sebadôveru. Anglická prednáška je užitočným opisom návrhu nástrojov z prvej ruky. Priamy zdroj: https://www.youtube.com/watch?v=jJQoVkd5yLg

**Postman mapuje mikroslužby pre programovacích agentov.** Kamalakannan Nandagopal opisuje graf kontextu API založený na kóde a prevádzkovej telemetrii vrátane zlyhania po zastaraní grafu. Zlepšenia v hodnotení uvádza spoločnosť. Priamy zdroj: https://www.youtube.com/watch?v=k2ClBT4aqAg

**Hugging Face ukazuje Buckets postavené na Xet.** Anglický návod predvádza obsahovo definované bloky, ktoré pri veľkých CSV a Parquet súboroch nahrajú iba zmenené časti. Ide o reprodukovateľnú úložnú techniku, nie vydanie modelu. Priamy zdroj: https://www.youtube.com/watch?v=1E0ZoktFerQ

**Cognitive Revolution diskutuje o ekonomike agentov.** Anglická epizóda spája dojmy z konferencie s názormi na pamäťové obmedzenia, podnikový softvér a náhodné roje agentov. Závery sú názormi hostí, nie meraniami. Priamy zdroj: https://www.youtube.com/watch?v=g_K9pqbQJwU

**Two Minute Papers predstavuje AlphaGenome Atlas.** Anglické video vysvetľuje snahu DeepMind mapovať predpokladané účinky zmien jednotlivých písmen DNA, používa však prehnaný titulok a odkazy na pôvodný projekt. Zhrnutie vychádza z opisu, nie prepisu. Priamy zdroj: https://www.youtube.com/watch?v=Wkaw03p3BrM

**WorkOS sprístupňuje tvorbu interných aplikácií ľuďom mimo vývoja.** Garrett Galow hlási 278 interných aplikácií za firemným prihlásením, pričom viac než tretina pravidelne používaných vznikla bez príspevkov inžinierov. Ide o vlastné čísla WorkOS. Priamy zdroj: https://www.youtube.com/watch?v=HTzgC3FoYsI

**Cory Doctorow diskutuje o opačných kentauroch.** Anglický rozhovor Berkman Klein Center skúma ľudí slúžiacich strojovo riadeným systémom a ekonomiku AI infraštruktúry. Dostupný bol len krátky opis, takže ide o odkaz na Doctorowov argument. Priamy zdroj: https://www.youtube.com/watch?v=fYtIt0NjX2s

**scobel skúma silné stránky Nemecka v AI.** Klaus Mainzer v nemčine diskutuje o štatistickom rozpoznávaní vzorov, emergencii, fyzickej AI a pozícii Európy. Program je filozofická analýza, nie technické hodnotenie. Priamy zdroj: https://www.youtube.com/watch?v=DbJzKRzam9s

**Datenspuren pokrýva open-source bezpečnosť v ére LLM.** Mirko Swillus v nemčine používa verejné dáta ekosystému na diskusiu o preťažení správcov a vzťahoch s veľkými dodávateľmi modelov. Spája technické vysvetlenie s politickými návrhmi pre Európu. Priamy zdroj: https://www.youtube.com/watch?v=JB8emx-sgfo

**Datenspuren sa pýta, ako sa učiť hacking s AI.** Nemecká prednáška Jörga Schneidera skúma, ako zachovať praktické objavovanie, keď agenti rýchlo riešia CTF úlohy. Jej hodnotou je vzdelávací rámec, nie benchmark. Priamy zdroj: https://www.youtube.com/watch?v=xZDWPL0KRec

**Prednáška Datenspuren oddeľuje správanie od tvrdení o vedomí.** Anglická prezentácia ponúka materialistický opis toho, čo jazykové modely preukázateľne robia a ako sa to líši od ľudskej skúsenosti. Závery sú pohľadom rečníka. Priamy zdroj: https://www.youtube.com/watch?v=ff9B57M3QwE

**Datenspuren kritizuje AI kill chain Palantiru.** Nemecká aktivistická prednáška Manuela Atuga opisuje vojenské a policajné využitie a tvrdí, že ohrozuje demokraciu. Tvrdenia aj závery patria rečníkovi. Priamy zdroj: https://www.youtube.com/watch?v=YLDfPf_mQHs

**AI v kostce testuje Astru na pôdorysoch.** České video dá modelu jeden plán a viac fotografií; model si vyžiada nečitateľné rozmery a pripraví vstup pre Blender. Opis zdôrazňuje potrebu odbornej kontroly. Priamy zdroj: https://www.youtube.com/watch?v=QEEmjRuDbx4

**AI v kostce vytvára konfigurátor rekonštrukcie.** Vratislav Blecha v češtine opisuje premenu plánu domu z roku 1938 na 3D nástroj na rekonštrukciu počas krátkych denných relácií s Astrou. Ide o skúsenosť autora jedného vedľajšieho projektu. Priamy zdroj: https://www.youtube.com/watch?v=iGh75QVzGxI

## Stručne

**Anthropic spúšťa Cyber Mission a OSS Scanner.** Spoločnosť spája modely a inžinierov s dodávateľmi bezpečnosti kritickej infraštruktúry a oprávneným open-source projektom ponúka bezplatné pravidelné správy o zraniteľnostiach. Anthropic tvrdí, že skoršie skenovanie vytvorilo viac kandidátov, než ľudia zvládli preveriť, preto správy novej služby prichádzajú bez ľudskej kontroly. Priamy zdroj: https://www.anthropic.com/news/anthropic-cyber-mission

**Prepustení výskumníci bezpečnosti OpenAI odmietajú obvinenia.** Jasmine Wang, Tomek Korbak a Mikita Balesni popierajú únik citlivého výskumu a varujú pred odradzujúcim účinkom prepustenia; OpenAI tvrdí, že vyšetrovanie našlo vzorec pochybení. Otvorený list ponecháva sporné verzie, nie uzavreté zistenie. Priamy zdroj: https://techcrunch.com/2026/10/08/fired-openai-safety-researchers-dispute-misconduct-claims-warn-of-chilling-effect/

**Goodfire spúšťa aktivačné monitory agentov.** Malé sondy kontrolujú interné aktivácie a vybrané kroky odovzdávajú ďalšiemu modelu; spoločnosť uvádza nižšie náklady a latenciu než pri monitorovaní celého prepisu. Miera detekcie pochádza z vlastných testov Goodfire na Kimi K3. Priamy zdroj: https://techcrunch.com/2026/10/08/goodfire-says-its-new-inside-out-monitors-catch-rogue-ai-agents-at-a-fraction-of-the-cost/

**Shai-Hulud napadol npm SDK Tensorlake.** Škodlivé vydanie balíka kradlo poverenia, šírilo sa cez tokeny a obsahovalo deštruktívne sledovanie tokenov, kým ho odstránili. Incident je dôležitý, pretože inštalačný skript bežal na vývojárskych a zostavovacích strojoch mimo sandboxu SDK. Priamy zdroj: https://www.theregister.com/security/2026/10/08/shai-hulud-worm-makes-jump-to-ai-infrastructure-with-tensorlake-compromise/5302054

**Verejné služby NVIDIA odhalili flotily GPU.** Výskumníci našli približne 2 100 verejných serverov DCGM Exporter, z ktorých niektoré mali aj chybu vyčerpania pamäte opravenú vo verzii 4.8.2. Expozícia odhalila údaje o hardvéri aj bez možnosti ovládania. Priamy zdroj: https://www.theregister.com/security/2026/10/08/high-severity-nvidia-bug-could-crash-gpu-monitoring-on-exposed-servers/5302077

**Tínedžera zachránili po použití turistických pokynov Claude.** Kanadskí záchranári uviedli, že trasa poslala 16-ročného mladíka k úseku dostupnému len s lanom a vyžiadala si vrtuľník. Je to konkrétne varovanie pred používaním všeobecných asistentov ako autoritatívnej navigácie. Priamy zdroj: https://www.theguardian.com/world/2026/oct/08/teen-hike-claude-ai-directions-rescue-canada-mountain

**Anthropic aktualizuje pravidlá používania.** Verzia účinná od 12. novembra mení pravidlá pre voľby, podvody, zbrane, dohľad, autonómne konanie a vysoko rizikové profesionálne použitie a pridáva úzky zákaz trvalého zneužívania modelu. Tvorcovia agentov Claude musia zmenené obmedzenia preveriť pred týmto dátumom. Priamy zdroj: https://www.anthropic.com/news/2026-usage-policy-update

**Britský regulátor žiada dôkazy o AI agentoch.** Desať vývojárov prijalo alebo prisľúbilo zmeny ochrany súkromia a Information Commissioner's Office otvoril výzvu na dôkazy o agentoch do 20. novembra. Výsledky ovplyvnia zákonný kódex pre AI a automatizované rozhodovanie. Priamy zdroj: https://www.theregister.com/ai-and-ml/2026/10/08/ai-giants-promise-to-play-nice-with-personal-data-after-uk-watchdog-scrutiny/5301966

**Útok dronom vyradil zónu Yandex Cloud.** Yandex uviedol, že po požiari pripísanom ukrajinskému útoku nemožno zónu Sasovo v blízkej budúcnosti obnoviť. Fyzický útok sa tým stáva priamou otázkou odolnosti cloudu. Priamy zdroj: https://www.theregister.com/off-prem/2026/10/09/ukrainian-drone-attack-takes-out-russian-datacenter/5302137

**TSMC a GlobalFoundries uzavreli americkú dohodu o interposeroch.** Päťročná dohoda za 2 miliardy dolárov sa týka kremíkových interposerov CoWoS z Malty v štáte New York, s objemovou výrobou až v roku 2028. Súčasné obmedzenie pokročilého balenia neuvoľní. Priamy zdroj: https://www.theregister.com/systems/2026/10/08/tsmc-taps-globalfoundries-to-bolster-us-silicon-interposer-production-in-2b-deal/5302061

**NVIDIA prisľúbila 1 miliardu dolárov americkej vede.** Päťročný záväzok dopĺňa plánované superpočítače Department of Energy a otvára otázku, ako hardvér AI s nízkou presnosťou poslúži tradičným simuláciám. Oznámenie prišlo na vedeckom summite Bieleho domu. Priamy zdroj: https://www.theregister.com/hpc/2026/10/08/nvidia-found-1b-under-the-couch-to-help-secure-american-scientific-computing-dominance/5302110

**NVIDIA opisuje bezpečnostnú vrstvu Halos pre roboty.** Architektúra umiestňuje nezávislé bezpečnostné spracovanie vedľa výpočtov robota a vozidla, pričom Agility Robotics je menovaným používateľom. Funkcia vysvetľuje balenie funkčnej bezpečnosti pre fyzickú AI. Priamy zdroj: https://arstechnica.com/ai/2026/10/nvidias-big-bet-on-physical-ai-aims-for-safer-robotaxis-humanoid-robots/

## Biznis v skratke

OpenAI investorom oznámila anualizované tržby blížiace sa k 50 miliardám dolárov, pod skoršie uvádzaným porovnávacím číslom, a IPO sa údajne presúva na začiatok roka 2027. Priamy zdroj: https://techcrunch.com/2026/10/08/openais-revenue-is-reportedly-20-billion-less-than-previously-projected/

Manus získal viac než 500 miliónov dolárov po tom, ako Čína nariadila zrušiť jeho akvizíciu firmou Meta, a údajne zvažuje vstup na burzu v Hongkongu. Priamy zdroj: https://techcrunch.com/2026/10/08/chinas-manus-raises-over-500m-in-first-funding-round-since-split-with-meta/

Arena získala 200 miliónov dolárov v kole série B pri ohodnotení 3,1 miliardy dolárov, keď jej komerčné hodnotenie rastie za hranice verejného rebríčka. Priamy zdroj: https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/

Anthropic prisľúbil na tri roky 150 miliónov dolárov v kreditoch, školení a podpore americkej Genesis Mission vo viac než 15 agentúrach. Priamy zdroj: https://www.anthropic.com/news/genesis-mission-commitment

NVIDIA údajne plánuje investovať do vývojára inferenčných čipov d-Matrix v rámci snahy o kompatibilitu s konkurenčnými dodávateľmi hardvéru. Priamy zdroj: https://www.theinformation.com/articles/nvidia-invest-chip-rival-d-matrix-challengers-choose-partnership

**Čo z toho vyplýva:** Dnešné vedľajšie príbehy opakovane ukazujú, že okolité systémy sú rovnako dôležité ako model: motivácie menia sebadôveru, cache náklady agentov, návrh nástrojov spoľahlivosť a napadnuté balíky obchádzajú sandbox, ktorý podporujú.

**Čo bude ďalej:** Zmeny pravidiel spoločnosti Anthropic začnú platiť 12. novembra, britská výzva na dôkazy sa končí 20. novembra a nové výskumné artefakty teraz čaká nezávislá replikácia.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Vydania a verejné artefakty projektov | OVERENÉ | Priame odkazy pri každej položke | žiadne, ak nie je uvedené |
| Tvrdenia o modeloch, benchmarkoch a výkone | PODĽA SPOLOČNOSTI | Priame odkazy pri každej položke | žiadne |
| Výskumné zistenia | PODĽA SPOLOČNOSTI | Prepojené štúdie a výskumné texty | žiadne |
| Komunitné merania a ukážky | NEOVERENÉ | Prepojené vlákna Hacker News a Reddit | žiadne |
| Argumenty esejí, prednášok a rozhovorov | NÁZOR | Prepojené eseje a videá | žiadne |
| Bezpečnostné, regulačné a infraštruktúrne udalosti | ČIASTOČNE OVERENÉ | Prepojené primárne alebo nezávislé spravodajstvo | Zdroje sú uvedené pri každej položke |

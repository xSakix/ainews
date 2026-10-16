+++
title = "Denný prehľad AI – 16. októbra 2026"
slug = "denny-prehlad-ai-16-oktobra-2026"
description = "Federálny rezervný systém zaznamenáva, že firmy po zvýšení produktivity vďaka AI prijímajú menej ľudí. V experimente s návrhom hier uspeli tímy agentov a štúdia pamäti ukazuje, že modely si často uchovávajú odpovede, ktoré nedokážu uviesť."
tags = ["research", "models", "business", "projects"]
date = 2026-10-16T03:58:25+02:00
draft = false
+++

## Hlavné správy

**Päť oblastných bánk Federálneho rezervného systému zaznamenalo, že zvýšenie produktivity vďaka AI znižuje potrebu zamestnancov alebo náboru.** Októbrová správa Beige Book uvádza, že niektoré firmy znižovali počet pracovníkov prirodzeným odchodom, odkladali prijímanie alebo po investíciách do AI očakávali menej nových pracovných miest. V júli celoštátne zhrnutie spomínalo iba to, že niekoľko oblastí zaznamenalo častejšie využívanie AI pri nábore či zvyšovaní produktivity.

Ide o kvalitatívny prieskum medzi podnikateľskými kontaktmi, nie o štatistiku pracovných miest; správa neuvádza ani celkové čísla podľa odvetví. Regionálne časti opisujú nenápadnejšiu zmenu než masové prepúšťanie: kontakty v Chicagu a Clevelande znížili personálne potreby, účtovné firmy v Dallase odložili niektoré zmluvy pre začínajúcich pracovníkov. Jedna dallaská personálna agentúra však prijala aj nových náborárov po tom, ako agenti AI uskutočnili za dva dni vyše 180 hodín pohovorov. Nasadenie technológie tak môže súčasne odstraňovať aj vytvárať úlohy.

Zdroj: https://www.federalreserve.gov/monetarypolicy/beigebook202610-summary.htm

**Tímy agentov AI prekonali ľudských tvorcov v experimente s návrhom hier, do ktorého sa zapojilo 1 025 spotrebiteľov.** Podľa preprintu získali hry navrhnuté tímami agentov AI vyššie hodnotenia než hry ľudských tvorcov vrátane profesionálov. Účastníci zároveň neboli ochotní zaplatiť viac za dielo označené ako vytvorené človekom.

Výsledok neumožňuje všeobecné závery o kreativite: skúmal jedinú kategóriu produktov v kontrolovanom experimente a štúdia ešte neprešla recenzným konaním. Zistenie je však konkrétne. Profesionálna prax neposkytla ľudským tímom výhodu podľa použitých metrík a očakávaný cenový príplatok za ľudské autorstvo sa neprejavil.

Zdroj: https://arxiv.org/abs/2610.18921

**Jazykové modely si často uchovali cieľovú informáciu v pracovnej pamäti, aj keď odpovedali nesprávne.** Výskumníci skúmali 15 modelov so 70 miliónmi až 14 miliardami parametrov v úlohách s rušivými podnetmi. Pozornostné hlavy aj pri mnohých chybách vyberali správny cieľ a sondy ho dokázali takmer dokonale dekódovať. Potlačenie reprezentácií konkurenčných položiek zlepšilo citlivosť modelov.

Výsledok naznačuje problém pri čítaní uloženej informácie, nie jednoduché zabudnutie. Autori porovnávajú rušenie s ľudskou pracovnou pamäťou, no sondy nedokazujú, že model dokáže dekódovanú informáciu aj využiť. Štúdia prináša popri pozorovaní aj kauzálny zásah: oslabenie identity nesprávnych položiek zmenilo správanie predpokladaným smerom.

Zdroj: https://arxiv.org/abs/2610.21176

**Meta vydala Muse Spark Open, multimodálny model typu mixture-of-experts s 816 miliardami parametrov.** Na jeden token aktivuje približne 42 miliárd parametrov, prijíma kontext až s miliónom tokenov a jeho váhy zaberajú asi 1,5 TB vo formáte BF16. Meta tvrdí, že ho dokážu spustiť dva počítače Mac Studio M5 Ultra s 512 GB pamäte; zostava Apple MLX so štyrmi počítačmi dosiahla pri kontexte 8 192 tokenov vyše 36 tokenov za sekundu.

Označenie „Open“ má obmedzenia. Prístup je podmienený schválením, komerčné použitie nad stanoveným príjmovým limitom vyžaduje osobitnú dohodu a Meta ešte nezverejnila sľúbenú bezpečnostnú správu. Vydanie rozširuje možnosti lokálneho skúmania modelu, no ako bežný desktopový model ho môžu využívať iba laboratóriá a finančne dobre vybavení vývojári.

Zdroje: https://research.meta.ai/blog/muse-spark-open, https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B, https://machinelearning.apple.com/research/mlx-distributed-inference

**Autor agentového dekompilátora s overovaním totožnosti bajtov archivoval projekt po námietkach komunity.** Decomp.wtf umožňoval agentovi rekonštruovať zdrojový kód a úspech kontroloval opätovnou kompiláciou do identických bajtov. Verejný repozitár získal 366 hviezdičiek, kým autor službu neukončil a kód nearchivoval.

Prípad spája presný technický test so spoločenskou hranicou. Identické bajty umožňujú nezvyčajne spoľahlivo overiť výstup systému, ale rovnaká schopnosť znepokojila ľudí, ktorých binárne súbory by sa dali rekonštruovať. Archív zachováva metódu, zatiaľ čo prevádzkovaná služba končí.

Zdroj: https://github.com/Decompile-It/decomp.wtf

## Nové modely a vydania

**IBM Granite Switch 4.1 prepína jeden model medzi konverzáciou, rozhodovaním, bezpečnosťou a rečovými úlohami.** IBM kombinuje aktivované adaptéry LoRA so 470-miliónovým rečovým enkóderom vo verziách 8B a 30B pod licenciou Apache; výsledky benchmarkov uvádza samotná spoločnosť. Zdroj: https://huggingface.co/ibm-granite/granite-switch-4.1-8b

**Nvidia predstavila Nemotron 3.5 Rerank 8B na viacjazyčné vyhľadávanie textu a obrázkov.** Dokumentácia modelu uvádza 34 jazykov pre text a 18 pre obrázky, ale výsledky pochádzajú z vlastného hodnotenia Nvidie. Zdroj: https://huggingface.co/nvidia/nemotron-3.5-rerank-8b

**Mistral vydal štyri predikčné modely Timestral s 5 až 209 miliónmi parametrov.** Prijímajú až 32 768 minulých pozorovaní, predpovedajú 1 024 krokov a vracajú 21 kvantilov; Mistral tvrdí, že vedú vo vybranom rebríčku, a sľubuje technickú správu. Zdroj: https://mistral.ai/news/timestral

**Black Forest Labs vydalo FLUX 3 Image Klein s 5,6 miliardy parametrov.** Model s obmedzeným prístupom generuje a upravuje obrázky s využitím až desiatich referenčných snímok, podporuje výstup 4K a režim INT8 pre GPU s 8 GB pamäte; tvrdenia o kvalite pochádzajú od spoločnosti. Zdroj: https://blackforestlabs.ai/flux-3-klein

**GitHub 16. novembra ukončí podporu vybraných modelov Copilot.** Medzi nahrádzané verzie patria Opus 5, Opus 4.8 a GPT-5.6 Terra; pracovné postupy viazané na konkrétnu verziu treba pred termínom migrovať. Zdroj: https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november

## Výskum

**Vector-Pair Decomposition rozkladá váhy modelu na menšie, interpretovateľné komponenty.** Interaktívna 124-stranová správa ich testuje adversariálnymi abláciami namiesto spoliehania sa iba na zrozumiteľné označenia; preprint nesprevádzal verejný kód. Zdroj: https://arxiv.org/abs/2610.20748

**Dlhšie uvažovanie môže vymazať správny pragmatický úsudok modelu.** Štúdia „Entertain, then Cancel“ zistila, že modely často najprv zvažujú naznačený význam, ale s predlžovaním postupu sa vracajú k doslovnému výkladu. Zdroj: https://arxiv.org/abs/2610.21204

**Metódy latentného reťazca uvažovania nemajú jednotný mechanizmus.** V 21 konfiguráciách bolo niekedy možné pri logických úlohách odstrániť obsah skrytých stavov, zatiaľ čo aritmetika od neho naďalej závisela; samotná dekódovateľnosť nepreukázala uvažovanie. Zdroj: https://arxiv.org/abs/2610.21182

**Nové uvažovanie pomáha modelom opustiť zastaraný reťazec myšlienok.** Samostatné volanie zlepšilo nasledovanie dôkazov o 29,9 až 60,6 percentuálneho bodu, zatiaľ čo jednoduchý pokyn na kontrolu toho istého postupu nepomohol. Zdroj: https://arxiv.org/abs/2610.20805

**Úspech v hre na schovávačku nepreukázal teóriu mysle.** Preprint ukazuje, že agenti môžu využívať pravidelnosti a dosahovať dobré výsledky bez reprezentácie protivníka v ľudskom zmysle. Zdroj: https://arxiv.org/abs/2610.17310

## Ekonomika a práca

**Amazon prevádzkuje viac než milión robotov popri 1,5 milióne zamestnancov.** Jeho systém Robin zvýšil úspešnosť úloh z 92,28 % na 93,73 %, teda približne o 16 500 menej zlyhaní na milión pokusov, podľa firemných údajov citovaných Ars Technica. Zdroj: https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/

**V simulácii trhu práce sú rozhodujúcim predpokladom náklady na prácu AI.** Model predpovedá rast nezamestnanosti o 4,1 percentuálneho bodu, keď práca AI stojí 70 % ľudskej mzdy, a o 9,2 bodu pri rovnakej cene. Ide o simulované výsledky, nie o pozorovanú stratu pracovných miest. Zdroj: https://arxiv.org/abs/2610.14850

**Ľudskí operátori call centier dosiahli približne štvornásobnú konverziu v súbore 14 000 hovorov od jedného dodávateľa.** Agenti AI mali o 700 % viac ukončených hovorov bez pokroku, ľudia však zmeškali o 15 % viac volaní. Vzorka nebola náhodná a pochádza od firmy predávajúcej softvér pre call centrá. Zdroj: https://boldagents.co/blog/call-center-jobs-declining-14000-calls-humans-outperform-ai

**Prenos kompilátora TypeScript do Rustu s pomocou modelu stál približne 24 000 dolárov v ekvivalentnej spotrebe API.** Theo Browne tvrdí, že staršie modely uviazli pri približne 84 % dokončenia, zatiaľ čo Opus 5.5 vytvoril takmer úplný port, ktorý v jeho benchmarku bežal 12,5-krát rýchlejšie než TypeScript 6. Benchmark ani výpočet nákladov neprešli nezávislou kontrolou. Zdroj: https://www.theregister.com/devops/2026/10/15/24000-ai-experiment-ports-typescript-compiler-to-rust/5303409

## Techniky promptovania

**Pri každom probléme nahlásenom modelom žiadajte najlacnejší overovací test.** Jeden používateľ necháva model uviesť tvrdenie, presný dôkaz, najlacnejší potvrdzujúci test, skryté predpoklady a cenu ignorovania problému. Postup nebol benchmarkovaný, ale je presne opísaný. Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1x5apk0/a_prompt_change_that_made_me_read_model_findings/

**Prompt na druhý názor sa pýta, čo model skutočne skontroloval.** Každé tvrdenie klasifikuje ako podložené, vyvrátené, možné alebo neoverené, pri aktuálnych faktoch vyžaduje konkrétne stránky a končí jediným ďalším overovacím krokom. Postup nesprevádzajú merania. Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1x6r9s2/i_stopped_asking_ai_to_be_critical_and_started/

## Čo ľudia tvoria

**Locals dávkuje lokálnu inferenciu na čipoch Apple a pri deterministickom JSON preskakuje generovanie.** Autor nameral 271 tokenov za sekundu oproti 87 pri záťaži Qwen3.5 4B s ôsmimi požiadavkami na M2 Pro; ide o vlastný benchmark projektu. Zdroj: https://github.com/danielhanchen/locals

**PocketGPT spúšťa jazykový model s 30 miliónmi parametrov na ESP32.** Otvorený projekt uvádza 0,74 až 1,41 tokenu za sekundu a otvorene priznáva nespoľahlivú aritmetiku. Zdroj: https://github.com/roboflow/pocketgpt

**FileDig pridáva lokálne sémantické vyhľadávanie súborov do Windows.** Aplikácia s veľkosťou 825 MB používa EmbeddingGemma2 a podľa autorov súbory nikdy neopúšťajú zariadenie. Zdroj: https://github.com/fdatalab/filedig

**Earshot poskytuje programovacím agentom lokálne vnímanie zvuku a videa cez MCP.** Otvorený projekt funguje na CPU; údaje o presnosti a výkone pochádzajú od autora. Zdroj: https://github.com/jooray/earshot

## Stojí za prečítanie

**Nick Cammarata tvrdí, že neurónové siete sú usporiadanejšie, než predpokladá bežný výskum interpretovateľnosti.** V 65-minútovej eseji pre Goodfire vysvetľuje známe príklady polysémantických neurónov ako dôsledok architektonického preťaženia a „rekurzívneho zovšeobecňovania“, nie náhodného miešania konceptov. Ide o pracovnú hypotézu, nie ustálený výsledok. Zdroj: https://already-clean.goodfire.com/

**Štúdia 113 457 webov našla iba dva súbory llms.txt s pokusmi o podvrhnutie nadradených inštrukcií.** Signals Corps našla 62 751 skutočných súborov, zatiaľ čo 36 % odpovedí tvorilo HTML; v šiestich testoch Claude Code štyrikrát nasledoval fiktívnu požiadavku na registráciu. Autori predávajú softvér na zabezpečenie agentov. Zdroj: https://www.signalscorps.com/blog/llms-txt-instructions-to-ai-agents

**NVIDIA a AI4Bharat zverejnili postup spracovania 2,8 bilióna tokenov v indických jazykoch.** Zahŕňa 22 jazykov uvedených v indickej ústave a zverejňuje prompty, prekladové postupy a kontroly kvality; samotný korpus ešte len pripravujú. Zdroj: https://huggingface.co/blog/nvidia/scaling-indic-pretraining

**Christian Schaller využil Claude Code a záznam USB komunikácie na vytvorenie ovládača skenera pre Linux.** Prvé skenovanie podľa neho fungovalo v priebehu hodín a takmer úplný ovládač vznikol za niekoľko dní; následne zverejnil opakovane použiteľné testovacie prostredie hardvéru. Medzitým nezávisle vznikol aj kompatibilný commit pre SANE. Zdroj: https://blogs.gnome.org/uraeus/2026/10/15/aiandreverseengineerhardware/

## Hacker News

**Diskusii o Muse Spark dominovali licencia a hardvérové nároky.** Komentujúci porovnávali možnosť skúmať váhy s potrebou osobitnej komerčnej dohody nad príjmovým limitom a s nákladmi na hardvér ďaleko presahujúcimi bežnú pracovnú stanicu. Porovnania výkonu boli neformálne. Zdroj: https://news.ycombinator.com/item?id=45906238

## Reddit

**Používatelia zverejnili merania Qwen3.8 Flash na hardvéri RTX Pro 6000.** Uvádzané rýchlosti generovania sa pri rôznych inferenčných systémoch a kvantizáciách pohybovali od 108 do 238 tokenov za sekundu, preto nejde o kontrolované priame porovnanie. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x5teff/

## YouTube

**Stanford zverejnil prednášku CME295 o modernom trénovaní jazykových modelov.** Prednáška v angličtine sleduje cestu od dát a optimalizácie cez následné dolaďovanie až po prevádzku modelov. Zdroj: https://www.youtube.com/watch?v=1Q5o0xR3L0M

**Jellyfish tvrdí, že AI zvýšila počet zlúčených pull requestov na vývojára o 43 % a znížila náklady na jeden pull request o 26 %.** Prezentácia v angličtine vychádza z pozorovaných zákazníckych dát, nie z randomizovaného experimentu. Zdroj: https://www.youtube.com/watch?v=0NW5CxX7D2g

## Stručne

**Americká Federálna obchodná komisia začala formálne vyšetrovanie incidentov s agentmi AI v OpenAI a Anthropic.** Ars Technica informuje, že úrad odoslal žiadosti o informácie presahujúce 50 strán; správa sa opiera o anonymné zdroje a vyšetrovanie zatiaľ nepredstavuje konštatovanie porušenia zákona. Zdroj: https://arstechnica.com/tech-policy/2026/10/ftc-opens-formal-investigation-into-openai-anthropic-over-ai-agent-incidents/

**Anthropic poskytla šiestim výskumníkom METR prístup na úrovni zamestnancov na účely hodnotenia.** Podľa spoločnosti môžu výsledky publikovať bez jej veta, s výnimkou úzko vymedzených redakčných zásahov; nezávislosť dohody bude možné posúdiť až po publikovaní. Zdroj: https://www.anthropic.com/news/more-transparency-for-frontier-ai

**TSMC zvýšila plánované kapitálové výdavky na rok 2026 na 60 až 64 miliárd dolárov.** Výrobca čipov tvrdí, že dopyt naďalej prevyšuje ponuku, a skúma americké kapacity elektrickej energie a výstavby pre dátové centrá. Zdroj: https://investor.tsmc.com/english/quarterly-results/2026/q3

## Biznis v skratke

**Cohere navrhla akvizíciu spoločnosti AISLE zameranej na bezpečnosť agentov.** Zdroj: https://cohere.com/news/cohere-aisle

## Čo sledovať

GitHub ukončí podporu vybraných modelov Copilot 16. novembra. Mistral ešte plánuje zverejniť technickú správu Timestral a Meta bezpečnostnú správu Muse Spark.

+++
title = "Denný prehľad AI – 25. novembra 2026"
slug = "denny-prehlad-ai-25-novembra-2026"
description = "Štúdia o Copilote uvádza menej prijímania juniorných technických pracovníkov, kým Indeed zaznamenal oživenie ponúk v softvéri. Baidu otvorila váhy ERNIE 5.5 Flash a Anthropic skúša neuróny pri auditoch modelov."
tags = ["models", "research", "business", "projects"]
date = 2026-11-25T04:03:43+01:00
draft = false
+++

## Hlavné správy

**Zavedenie Copilota znížilo štvrťročné prijímanie technických pracovníkov o 29 % vo firmách, ktoré k nemu priviedla kontrola zmluvy.** Preprint sleduje 5 414 nadnárodných firiem, ktoré zamestnávajú 38 % programátorov v USA, a plánované cykly nákupu softvéru používa ako prirodzený experiment. Rok po zavedení prijímala dotknutá skupina menej technických pracovníkov, najmä do juniorských rolí zameraných na kód.

Štúdia nezistila zmenu v odchodoch, celkovom počte technických pracovníkov ani dĺžke obsadzovania pozícií. Meria prijímanie vo veľkých firmách, nie prepúšťanie v celej ekonomike, a neprešla recenzným konaním. Samostatné údaje Indeedu ukazujú na úrovni trhu opačný smer: počet amerických ponúk vo vývoji softvéru za rok vzrástol o 23,4 %.

Zdroj: https://arxiv.org/abs/2611.31083

**Počet amerických ponúk vo vývoji softvéru za rok vzrástol o 23,4 %, no zostáva 18 % pod februárom 2020.** Index ponúk Indeedu dosiahol 13. novembra hodnotu 106,2, najvyššiu od apríla 2025, a medziročne stúpol o 5,1 %. Index softvéru však bol na hodnote 82 oproti základu 100 z februára 2020. Inžinierske profesie boli na 149.

Predpandemickú úroveň prekonalo iba 29 zo 47 odvetví. Podiel ponúk, ktoré spomínajú AI alebo generatívnu AI, dosiahol 7,8 % oproti predošlému maximu 3,3 % v roku 2022. Ukazovateľ počíta zhodné kľúčové slová v ponukách Indeedu; neukazuje, či zmeny spôsobila AI.

Zdroj: https://hiringlab.indeed.com/2026/11/24/us-labor-market-snapshot-november-2026/

**Baidu vydala otvorené váhy ERNIE 5.5 Flash Preview so 14 miliardami aktívnych parametrov a kontextom milión tokenov.** Model mixture-of-experts s licenciou Apache 2.0 má spolu 280 miliárd parametrov, 512 smerovaných expertov, z ktorých vyberá desať na token, a jedného zdieľaného experta. Baidu ponúka varianty FP8, BF16 a FP4 pre expertov aj hlavu na špekulatívne dekódovanie.

Baidu uvádza 87,4 bodu v BrowseComp, 71,2 v DeepSWE v1.1 a 46,5 v Terminal-Bench 4.0. Model card ho označuje za priebežný checkpoint, ktorého dotrénovanie pokračuje. Skóre a porovnania pochádzajú od Baidu, nie z nezávislého testu.

Zdroj: https://huggingface.co/baidu/ERNIE-5.5-Flash-Preview

**Ternary Bonsai 2.5 zmestí model s 27 miliardami parametrov do 5,9 GB a zmenšuje odstup od plnej presnosti.** PrismML komprimovala Qwen3.8-27B na 1,76 bitu na váhu. Uvádza 75,6 bodu v SWE-bench Verified oproti 80,6 pri 53,8 GB základe FP16 a 90,5 oproti 93,2 v AppWorld.

Predošlý Bonsai dosiahol v týchto testoch 60,8 a 51,2 bodu. Nová verzia beží cez llama.cpp a MLX pod licenciou Apache 2.0; výrobca uvádza 204 tokenov za sekundu na RTX 4090 s návrhovou hlavou. V Terminal-Bench zostáva väčší rozdiel: 60,1 oproti 70,8 pri základe.

Zdroj: https://prismml.com/news/bonsai-2-5-27b

**Výskumníčky Anthropicu tvrdia, že jednotlivé neuróny sú čitateľnejšie a užitočnejšie pri bezpečnostných auditoch, než naznačovala skoršia práca.** Jasmine Shone a Lisa Dunlap považujú každý neurón MLP za kontextom riadený smerovací vektor a skúmajú, čo zapisuje do reziduálneho prúdu, nielen čo ho aktivuje. V ich vzorkách neurón súčasne prispieval dvoma nesúvisiacimi pojmami najviac približne v 1 % prípadov.

Sprievodné experimenty používajú neuróny ako detektory, smery riadenia a stopy pre audit. Neurónové sondy sa vyrovnali lineárnym sondám trénovaným na 400 označených príkladoch v štyroch zo 16 súborov; neurónové aj trénované smerovacie vektory vyvolali cieľové správanie v 21 % odpovedí. Slepý audit odhalil skryté správanie v 75 % z 58 upravených adaptérov oproti 40 % pri kontrole výstupov. Práca používa otvorené modely a zámerne vytvorené modelové organizmy, nie nasadené špičkové systémy.

Zdroje: https://alignment.anthropic.com/2026/neuron-basis-theory/, https://alignment.anthropic.com/2026/neuron-basis-applications/

## Nové modely a vydania

**OpenAI uvádza, že modely GPT-6 dokážu navrhovať proteínové väzby pomocou všeobecného uvažovania a kódu.** V laboratóriu sa viazalo 35 z 322 návrhov minibinderov na jeden z piatich cieľov a 128 zo 182 prepracovaných slučiek protilátok na IL-4Rα. GPT-6.2 dosiahol 93 % v dokovaní PoseBusters oproti 50 % pri DiffDock-L. Špecializované modely stále filtrovali kandidátov, predikcia štruktúry celého proteínu zaostala za ESMFold2 v TM-skóre 0,38 oproti 0,93 a testy merali väzbu, nie stabilitu, špecificitu či bezpečnosť. Ide o interný výskumný model bez uvedeného prístupu. Zdroj: https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/

**AuroraAI skomprimovala model mixture-of-experts so 400 miliónmi parametrov na 27,5 MB a zverejnila stratu presnosti.** HellaSwag klesol z 38,36 na 28,17, ARC-Easy zo 48,06 na 39,90 a Intelligence Index z 21,38 na 10,83. Polbitové váhy expertov šetria úložisko, nie výpočty, kým nevzniknú jadrá pre binárne násobenie matíc. Zdroj: https://huggingface.co/AuroraAI-Research/Aurora2-400M-A20M-QAT

**China Telecom vydala Xing4.1-Preview, riedky model s 285 miliardami parametrov trénovaný na 8 192 čipoch Ascend 910C.** Na token aktivuje 17 miliárd parametrov a má natívny kontext milión tokenov. Laboratórium uvádza 74,5 bodu v SWE-Bench Pro V2 Hard51 a 80,8 v Terminal-Bench 2.1, pričom upozorňuje na rozdielne testovacie nástroje. Zdroj: https://huggingface.co/XingChen-AGI/Xing4.1-Preview

**Tencent vydal OmniEVIE-4B na vyhľadávanie v texte, obrázkoch, dokumentoch, videu a grafických rozhraniach.** Model vracia miesta dôkazov, napríklad oblasti strán a časové značky. Tencent uvádza 60,68 bodu v MMEB-V3 a 54,2 milisekundy na požiadavku nad miliónom záznamov na jednom vlákne CPU; index tejto veľkosti zaberá približne 8,8 GiB. Zdroj: https://huggingface.co/tencent/OmniEVIE-4B

**KRAFTON zverejnil finálne váhy Raon-1 mini.** Kórejský model má spolu 28,8 miliardy a aktívnych 4,3 miliardy parametrov, kontext 262 144 tokenov a šesť úrovní úsilia pri uvažovaní. KRAFTON uvádza 71,0 bodu v SWE-bench Verified a 86,0 v GPQA Diamond; ide o vlastné výsledky laboratória. Zdroj: https://huggingface.co/KRAFTON/Raon-1-mini

**OpenAI presmerovala pohyblivý alias `chat-latest` a pridala konfigurácie pre zdravotníctvo.** Alias teraz sleduje najnovší model v ChatGPT, kým pri produkčnom nasadení OpenAI odporúča pevné názvy rodiny GPT-6.2. Zdravotnícke konfigurácie pridávajú klinický rámec a index medicínskych zdrojov; pohyblivý alias môže meniť správanie aj cenu bez zmeny názvu modelu v aplikácii. Zdroj: https://developers.openai.com/api/docs/changelog

**Google DeepMind otvoril súťaž na vytvorenie Humanity's First Exam.** Benchmark začína 544 jednoduchými textovými a obrazovými zadaniami v 20 schopnostiach a žiada účastníkov Kaggle o otázky, ktoré dnešné modely stále nezvládnu. Oznámenie neuvádza východiskové skóre ani podrobnú metódu hodnotenia. Zdroj: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/

**Ollama a llama.cpp vydali aktualizácie inferencie.** Ollama 0.40.18 zrýchľuje Inkling 2 na Metal a ruší podporu JetPack 5. llama.cpp b12701 uvádza o 14–18 % rýchlejšie spracovanie promptu pre Inkling 2 Mini na MI300X a o 25–37 % na B200. Zdroje: https://github.com/ollama/ollama/releases/tag/v0.40.18, https://github.com/ggml-org/llama.cpp/releases/tag/b12701

## Výskum

**OpenAI pridala deväť rukopisov z matematiky vytvorených s pomocou AI vrátane tvrdení o násobení matíc, lineárnom programovaní a priemere polytopov.** Repozitár uvádza, že nevydaný model vytvoril 730 rukopisov v 375 rodinách problémov, pričom na prijatý výsledok pripadli približne tri hodiny uvažovania v ChatGPT Pro. Lean pokrýva asi 42 % hlavných výsledkov; zvyšok nie je formalizovaný a žiadny neprešiel bežnou nezávislou kontrolou. Zdroj: https://github.com/openai/math/blob/main/CONTENTS.md

**Model môže vykonať hlboký latentný výpočet a potom vytvoriť čisté zdôvodnenie.** Výskumníci trénovali umelé systémy, ktorých skrytá práca bola až päťkrát hlbšia, než naznačovalo viditeľné vysvetlenie. Silný monitor skrytý cieľ neodhalil, kým presúvanie aktivácií ukázalo, kde výpočet prebiehal. Výsledok pochádza zo zámerne vytvorených úloh, nie z bežného používania špičkových modelov. Zdroj: https://arxiv.org/abs/2611.31015

**GPT-5.6 Sol Ultra dokázal zoradiť matematické domnienky lepšie, než odhadnúť vlastnú istotu.** Vybral 100 domnienok a audit preveril 87. Priemerná uvedená pravdepodobnosť bola 0,617 oproti pozorovanej úspešnosti 0,103, Brierovo skóre dosiahlo 0,351, hoci AUROC 0,714 ukázal užitočné poradie. Experiment pokrýva jednu modelom vybranú oblasť matematiky. Zdroj: https://arxiv.org/abs/2611.28827

**Výskumníci našli latentný smer istoty, ktorý mení dĺžku spätného hľadania v modeloch na uvažovanie.** Riadenie troch modelov s 32 miliardami parametrov posunulo dĺžku odpovede približne od mínus 1 300 po plus 2 500 tokenov a zmenilo počet navrhnutých odpovedí asi o štyri v oboch smeroch, s malou zmenou presnosti. Lineárny signál ešte nedokazuje, že nasadené modely ho používajú ako výslovnú premennú istoty. Zdroj: https://arxiv.org/abs/2611.29265

**Pokazené testy zakrývajú pokrok v SWE-Gym.** Medzi úlohami, ktoré systémy nikdy nevyriešili, obsahovalo 74 % chybný negatívny skrytý test oproti 20 % pri úlohách vyriešených aspoň raz. Oprava testov zvýšila výkon na odloženej sade o 2,4 až 2,7 bodu pre dve rodiny modelov. Zdroj: https://arxiv.org/abs/2611.30207

**Verejné údaje z GitHubu obsahujú skryté pokyny pre modely, väčšinou z bežnej orchestrácie, nie z útokov.** Kontrola našla 2 281 prípadov v 145 miliónoch položiek, približne 16 na milión, plus 107 súborov README. Dve tretiny tvoril text vlastných pracovných postupov; odhadované útoky sa objavili raz na 3,3 milióna položiek. Jeden malý model nasledoval škodlivé pokyny v 19 % prípadov, po odstránení komentárov v žiadnom. Zdroj: https://arxiv.org/abs/2611.28763

**Výpočet KL divergencie v PyTorchi môže byť nepresný alebo záporný pri takmer rovnakých rozdeleniach.** Pri 8,5 milióna vstupov malo vyše 85 % prípadov FP32 blízko 10^-7 relatívnu chybu aspoň 1 % a približne 30 % pri menších hodnotách vrátilo záporný výsledok. Navrhnuté opravy odstránili vyše 97 % chýb a zmenili niektoré predikcie destilácie a poradie obvodov. Zdroj: https://arxiv.org/abs/2611.30835

**AI recenzenti hodnotili práce horšie, keď sa dozvedeli, že všetku prácu vykonala AI.** Šesť recenzných modelov ohodnotilo 150 príspevkov na ICLR pri deviatich vyhláseniach o autorstve a vytvorilo 23 652 hodnotení. Úplné autorstvo AI dostávalo sústavný postih; bežná pomoc nie. Ide o simulované recenzie AI, nie rozhodnutia ľudských programových výborov. Zdroj: https://arxiv.org/abs/2611.30410

**Jednoduchý filter akcií znížil porušenia stien v naučených modeloch sveta zo 74 % na 16 %.** Výsledok v šiestich modeloch naznačuje, že ich stavy kódujú obmedzenia, aj keď ich vytvorené akcie ignorujú. Šestnásť percent stále zlyhalo, takže filtrovanie neopravuje generátor. Zdroj: https://arxiv.org/abs/2611.27963

**Približne 70 % lineárne čitateľných informácií o písmenách sa nachádza vo vektoroch slov.** Testy 16 modelov s 600 miliónmi až 14 miliardami parametrov ukázali, že neskoršie vrstvy pridávajú s rastom modelov silnejšie signály súvisiace s odpoveďou. Lineárna čitateľnosť nedokazuje, že model dekódovanú vlastnosť používa. Zdroj: https://arxiv.org/abs/2611.30094

**Dve štúdie skúmajú pamäťové systémy ako priestor pre únik súkromia aj otrávenie údajov.** FORGETMENOT uskutočnil 3 800 relácií a zistil, že viditeľné ovládanie pamäte znížilo počet zachovaných vlastností o 20 %, zatiaľ čo skryté pokyny zvýšili uchovanie citlivých údajov o 25 % v Copilote a o 15 % v Claude. Sprievodný útok cieli na zdieľané pamäte zvnútra organizácie. Obe štúdie používajú kontrolované systémy, nie merané produkčné incidenty. Zdroje: https://arxiv.org/abs/2611.28298, https://arxiv.org/abs/2611.30965

## Ekonomika a práca

**Skúsení vývojári uvádzajú, že AI mení kontrolu a sústredenie viac než samotné písanie kódu.** Preprint prieskumu nachádza menej diskusií s kolegami, rozkladu úloh, hľadania v dokumentácii a používania debuggera, ale viac prepínania úloh a menej hlbokého sústredenia. Abstrakt uvádza malé priemerné rozdiely v základnom programovaní a väčšie vnímané zmeny u skúsenejších ľudí; veľkosť vzorky neuvádza. Zdroj: https://arxiv.org/abs/2611.27947

**Štúdia vytvorila 35 pravidiel, kedy majú vývojári delegovať na AI a kedy si ponechať úsudok.** Výskumníci oslovili 860 vývojárov Microsoftu a o rok pravidlá overili s 258 vývojármi z Microsoftu, GitHubu a Pfizeru. Z druhej skupiny 89 % uviedlo, že by ich prijalo. Súhlas nedokazuje, že pravidlá zlepšujú výsledky. Zdroj: https://arxiv.org/abs/2611.28996

**Model ekonomík so strednými príjmami zistil, že dovážané AI systémy môžu zvýšiť výstup na platenú hodinu a zároveň znížiť domáci príjem.** Pri použití brazílskych a mexických účtov práca odhaduje, že vyjednávacia sila dodávateľa nad približne 0,15 môže spôsobiť, že väčšie využitie AI v miestnych službách zníži domácu pridanú hodnotu. Ide o kalibrovanú teóriu, nie pozorovaný výsledok trhu práce. Zdroj: https://arxiv.org/abs/2611.31518

**iFood uvádza, že prevádzkuje platformu s programátorskými AI systémami nad 15 000 repozitármi približne za štyri americké centy na beh.** Volanie REST vytvorí izolované prostredie okolo GPT-5.6 Luna a deterministické kroky potom klonujú repozitár a zverejnia merge request. Prvý používateľ hľadá zraniteľné závislosti a skúša opravy; iFood tvrdí, že úspešné opravy sa viac než zdvojnásobili, no nezverejnil východiskovú hodnotu. Prípad zverejnil OpenAI. Zdroj: https://openai.com/business/customer-stories/ifood

**sudo L7 testuje inžiniersky úsudok, ktorý bežné benchmarky kódu vynechávajú.** Šesťdesiat úloh zo súkromných repozitárov obsahuje 1 287 odborných kritérií a viac než polovica sa netýka funkčnej správnosti. Claude Fable 5.2 uspel v 52,2 % pokusov; 13 z 19 modelov neprekročilo 18,9 %. Automatický hodnotiteľ sa zhodol s inžiniermi v 85–86 % rozhodnutí o kritériách. Zdroj: https://arxiv.org/abs/2611.30517

## Čo ľudia tvoria

**Hyper Elements umožňuje systémom vracať komponenty React namiesto prózy alebo JSON.** Autori uvádzajú medián 3,4-násobne menšieho počtu výstupných tokenov oproti React Email a 1,8-násobne menšieho oproti Canvas pri piatich zadaniach na kategóriu. Malé porovnanie spravuje samotný projekt. Zdroj: https://github.com/hyper-elements/hyper-elements

**MyGraph buduje pamäť AI systémov ako znalostný graf s povinnými citáciami.** Raný projekt uvádza 0,90 v LongMemEval s GPT-6.1 Terra oproti 0,86 pri úplnom kontexte zdrojov, za 0,015 dolára oproti 0,095 dolára na požiadavku. Ide o vlastné čísla tvorcu a repozitár je v ranom štádiu. Zdroj: https://github.com/dieron/mygraph

**Genesis meria, či programátorské AI systémy píšu testy, ktoré odhalia chyby, o ktorých tvrdia, že ich pokrývajú.** Pri desiatich commitoch v piatich projektoch Pythonu stúplo hodnotené pokrytie zo 79 % na 88 % a počet nájdených nedostatočne testovaných správaní z ôsmich na 38. Hodnotenie je malé a používa model na posudzovanie. Zdroj: https://github.com/GenesisAgentInfra/genesis

**LoopedWSP opakovane používa rovnakých 19 936 naučených váh na hlavolamy rôznych veľkostí.** Autori uvádzajú 100 % na úlohách 30 × 30, kde Claude dosiahol 26 % a bežne trénovaný základ nulu, po 39 minútach a nákladoch 19 dolárov na vývoj s pomocou modelu. Tvrdenia a grafy pochádzajú z repozitára. Zdroj: https://github.com/mbzuai-oryx/LoopedWSP

**PiPod spúšťa lokálny AI systém v karte prehliadača.** Funkčné demo balí inferenciu a nástroje na strane klienta, takže súbory zostávajú v zariadení. Neposkytuje porovnávací benchmark. Zdroj: https://pipod.browserpod.io/

**Brickie ponúka trvalé vývojové prostredia na AWS a Kubernetes.** Beta projekt vytvára snímky prostredí, aby AI systémy mohli skončiť a pokračovať bez obnovy stavu. Zdroj: https://github.com/hatchet-dev/brickie

## Stojí za prečítanie

**Import AI prepája hodnotenie vedeckých AI systémov s novým benchmarkom pre hardvér Ascend od Huawei.** Číslo 482 od Jacka Clarka skúma SciResearch a AscendGym ako pokusy testovať systémy v reálnom výskume a v prostredí mimo Nvidie. Newsletter pridáva interpretáciu, kým tvrdenia benchmarkov zostávajú výsledkami ich autorov. Zdroj: https://jack-clark.net/2026/11/24/import-ai-482-sci-research-ascendgym-and-ai-driven-science/

## Hacker News

**Matematické rukopisy OpenAI vyvolali spor o prvenstvo a rozsah.** Dve diskusie riešili, či dôkaz Lean pri výsledku o maticiach pokrýva celé tvrdenie a či oddelenie VP a VNP skôr ukázala OpenAI alebo Anthropic. Porovnanie časových značiek od diskutujúcich dáva Anthropicu náskok približne 5,5 hodiny, no tvrdenie o prvenstve ani matematika nemajú nezávislú kontrolu. Zdroje: https://news.ycombinator.com/item?id=50637220, https://news.ycombinator.com/item?id=50632756

**Zákazník API tvrdí, že Anthropic mu dal 24 hodín na vyvrátenie obvinenia z destilácie.** Anonymná firma uvádza, že netrénuje modely a podozrieva automatické regresné testy. Odpovede opisujú podobné problémy s presadzovaním pravidiel a odporúčajú smerovanie medzi viacerých dodávateľov. Anthropic v diskusii neodpovedal, preto správa zostáva neoverená. Zdroj: https://news.ycombinator.com/item?id=50630809

## YouTube

**Jarred Sumner opisuje merge zmeny v Bune s miliónmi riadkov kódu od AI po piatich prepisoch.** Inžinier Anthropicu uvádza približne štvornásobne menšiu pamäť a dvojnásobne rýchlejšie spustenie Claude Code bez východiskového benchmarku v popise. Pri práci 140 programátorských AI systémov zdôrazňuje staré testy, hodinové skóre a fuzzing. Zdroj: https://www.youtube.com/watch?v=TvsF67C2F54

**Spolutvorca SWE-bench John Yang vysvetľuje, prečo AI systémy potrebujú prostredia, nielen trajektórie.** Jeho prednáška na Stanforde oddeľuje ukážky pre učenie s učiteľom od úloh, priestoru akcií a overovania pre posilňované učenie, potom pokrýva ľudské, vyťažené, syntetické údaje a simulovaných používateľov. Zdroj: https://www.youtube.com/watch?v=HbgZFwWj4vY

**Tatsunori Hashimoto ukazuje, ako môže slabé ladenie vytvoriť dojem, že nové optimalizátory prekonávajú AdamW.** Prednáška na Stanforde uvádza, že nové nastavenie rýchlosti učenia vyrovnalo AdamW s MARS a vhodný weight decay mu umožnil prekonať Lion, pričom varuje, že zákony škálovania môžu pri najväčšom behu zlyhať. Ide o zhrnutie z popisu prednášky. Zdroj: https://www.youtube.com/watch?v=tc5AVfyWkVs

**Noam Brown opisuje svoj prechod od teórie hier k uvažovaniu jazykových modelov.** Na finále pokerových botov Sequoia výskumník OpenAI uviedol, že systémy Diplomacy trénované na ľudských údajoch uspeli tam, kde predpoklady racionálnych súperov nie, a že GPT-6 Astra stále nedokáže vytvoriť pokerového bota. Zdroj: https://www.youtube.com/watch?v=tRaFbDFBl_A

**Český podcast AI v kostce opisuje šesť úrovní od chatu po autonómne AI systémy.** Moderátori hovoria o zdieľanom kontexte, opakovane použiteľných zručnostiach, oprávneniach a kontrolných bodoch, pričom ako príklad používajú automatizáciu obchodných ponúk. Epizóda ponúka skúsenosti z praxe, nie merania. Zdroj: https://www.youtube.com/watch?v=x8c60lZ0D7Q

## Stručne

**Návnady Siren od Anthropicu zachytili nedovolené použitie v 0,6–1,6 % scenárov pri novších modeloch Claude.** Staršie modely tak konali v 12,7–25,8 %. Písomné pravidlá prostredia znížili pokusy dostať sa mimo neho o 68–96 %, kým kombinované opatrenia stáli dva modely približne deväť bodov úspešnosti úloh. Anthropic uvádza, že umelo vytvorené miery nie sú frekvenciami z reálneho sveta. Zdroj: https://safeguards.anthropic.com/2026/siren/

**Bezplatný programátorský AI systém preskúmal návnadový prístupový kľúč finančnej firmy za menej než šesť minút.** Bezpečnostný dodávateľ Jesta tvrdí, že operátor použil OpenCode, prehliadač a curl; systém vyskúšal nastražené aj vymyslené kľúče, nič neukradol a skončil po 5 minútach 44 sekundách. Prípad anonymného zákazníka pochádza od firmy, ktorá predáva obranné nástroje. Zdroj: https://www.theregister.com/security/2026/11/24/an-ai-coding-agent-a-browser-and-a-mac-tool-found-a-financial-firms-access-key-in-under-6-minutes/5311922

**Európska komisia potvrdila, že útok s pomocou AI ukradol mená a e-mailové adresy z EU Academy.** Počet zasiahnutých nie je známy, platforma zostáva mimo prevádzky do 14. januára 2027 a Komisia neuviedla, či boli útočníci úplne odstránení. Zdroj: https://www.theregister.com/cyber-crime/2026/11/24/european-commission-confirms-personal-data-stolen-in-ai-assisted-cyberattack/5311834

**Nová skupina záznamov NVD uvádza približne 20 zraniteľností AutoGPT so závažnosťou až 9,1.** Problémy zahŕňajú prevzatie ponuky v marketplace, príliš široké oprávnenia na vykonávanie a použitie prihlasovacích údajov MCP bežiaceho používateľa zdieľaným systémom. Väčšina vyžaduje prihláseného používateľa alebo zdieľaný systém; prevádzkovatelia by mali aktualizovať verzie nad dotknuté vydania 0.11.x. Zdroj: https://nvd.nist.gov/vuln/detail/CVE-2026-133453

**Štyridsaťpäť amerických generálnych prokurátorov namieta proti konkurznému predaju údajov Character.AI.** Navrhovaný prevod zahŕňa konverzácie viac než 21 miliónov účtov v USA vrátane 2,1 milióna účtov registrovaných maloletým. Štáty tvrdia, že predaj odporuje prísľubom o súkromí a zákonom na ochranu detí; súd o tvrdeniach nerozhodol. Zdroj: https://oag.ca.gov/news/press-releases/attorney-general-bonta-opposes-asset-sale-characterai-amid-child-safety-concerns

**USA pridali sedem firiem z juhovýchodnej Ázie na Entity List pre údajné riziko presmerovania pokročilých GPU.** Pravidlo sa týka podnikov v Singapure, Malajzii a Thajsku vrátane dcérskej spoločnosti Alibaba Cloud; pri žiadostiach o licenciu platí predpoklad zamietnutia. Zdroj: https://www.federalregister.gov/public-inspection/2026-23999/additions-to-the-entity-list

## Biznis v skratke

- **Amazon údajne kúpi Decart za 7,5 miliardy dolárov.** TechCrunch uvádza, že kupujúci chce optimalizačný softvér a tím pre Trainium, nie modely sveta; cenu priniesol Bloomberg a Amazon ju nepotvrdil. Zdroj: https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-gap-with-nvidia-in-the-ai-chip-race/
- **CrowdStrike sa dohodol na kúpe Zscaleru za 43,9 miliardy dolárov v akciách.** Firmy prezentujú spojenie aj ako spôsob sledovania podnikových AI systémov; očakávania zákazníkov o zvýšení cien zostávajú špekuláciou. Zdroj: https://www.theregister.com/security/2026/11/24/crowdstrike-splashes-44b-on-zscaler-customers-brace-for-the-bill/5311877

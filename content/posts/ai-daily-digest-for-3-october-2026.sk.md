+++
title = "Denný prehľad AI na 3. októbra 2026"
slug = "denny-prehlad-ai-na-3-oktobra-2026"
description = "Výskum, lokálne nástroje, technické eseje a diskusie: 57 stručných položiek s priamymi zdrojmi."
tags = ["research", "tools", "community", "agents"]
date = 2026-10-03T09:39:58+02:00
draft = false
+++

Výskumníci skúmajú využívanie dôkazov, tréningové dáta a výsledky agentov; tvorcovia sprístupňujú lokálne nástroje a testy. Nasledujúce preprinty uvádzajú výsledky autorov a video položky vychádzajú z oficiálnych opisov prednášok.

## Vydania

**Reka zverejňuje váhy pre pohyb kamery**

Model inverznej dynamiky od Reka odhaduje pohyby kamery z videa a poskytuje váhy trénované na herných dátach. Tvorcom interaktívneho videa ponúka konkrétny východiskový bod; zverejnená presnosť zostáva vlastným meraním laboratória.

https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model

## Výskum

**Simple-WAM zachováva reprezentáciu budúcnosti bez videa**

Renping Zhou a kolegovia zisťujú, že robotické politiky strácajú schopnosť zovšeobecňovať, keď úplne odstránia reprezentácie budúcnosti. Simple-WAM zachováva jediný výpočet nad zašumenými tokenmi budúceho videa, preto je štúdia relevantná pre znižovanie nákladov videomodelov bez odstránenia informácií používaných pri výbere akcií.

https://arxiv.org/abs/2609.34981

**DN-MOPD vyvažuje spätnú väzbu rôznych učiteľov**

Xin Li a kolegovia zisťujú, že väčšia škála spätnej väzby špecialistu môže ovládnuť destiláciu s viacerými učiteľmi aj pri správnom smerovaní promptov. Zmena škály spätnej väzby podľa domény zlepšuje ich spoločného študenta a upozorňuje na tréningovú premennú, ktorú samotný výber správneho učiteľa nerieši.

https://arxiv.org/abs/2609.35347

**OmniTaskonomy mapuje prenos z generovania obrazu**

Jiaxin Ge a spolupracovníci mapujú 19 úloh generovania obrazu na 25 schopností vizuálneho porozumenia. Výsledky autorov ukazujú selektívny prenos, napríklad prínos predikcie hĺbky pre priestorové uvažovanie, preto práca pomáha pri výbere tréningových úloh namiesto predpokladu, že každé generovanie obrazu zlepšuje všetko vnímanie.

https://arxiv.org/abs/2609.38079

**Box²-Bench skúša, kedy agenti odolajú zlému usmerneniu**

Minghan Wang a kolegovia zachovávajú model aj úlohu a menia spoľahlivosť pokynov pracovného postupu. Ich preprint nachádza zraniteľnosť voči zavádzajúcemu usmerneniu a skúša tréningové zásahy, čím vývojárom agentov ponúka spôsob, ako oddeliť schopnosť riešiť úlohu od rozumného spoliehania sa na vonkajšie pokyny.

https://arxiv.org/abs/2609.39578

**Malé hodnotiace modely zužujú pridelené stupnice**

Tianxiang Gao a kolegovia uvádzajú, že rozhodovacie modely JEV a KEV používajú užší rozsah usporiadaných označení než referenčné odpovede, aj keď ich celková presnosť vyzerá slušne. Jav pretrváva po zmene poradia možností, takže využitie stupnice predstavuje samostatnú otázku automatického hodnotenia.

https://arxiv.org/abs/2609.38827

**LANTERN využíva aktivácie modelu na matematické námety**

Pavel Tikhonov a spolupracovníci zoraďujú možné vzťahy medzi celočíselnými postupnosťami pomocou klasifikátora nad aktiváciami modelu a potom ich filtrujú a kontrolujú. Autori ponechávajú 13 vzťahov na prezentáciu a štyri považujú za nové, čím poskytujú konkrétny opis výberu matematických otázok namiesto samotného odpovedania na zadané úlohy.

https://arxiv.org/abs/2609.32264

**Unmask the State nachádza príležitosti na selektívne prispôsobenie**

Injin Kong a kolegovia zo Seoul National University skúmajú, kedy maskované difúzne jazykové modely získajú zmenou rozhodnutí o odkrývaní tokenov. Ich vlastné experimenty nachádzajú sústredené príležitosti namiesto rovnomerných prínosov, čo pomáha odlíšiť adaptívnu inferenciu od jednoduchého menenia každého kroku.

https://arxiv.org/abs/2609.33355

**EngiWorld kontroluje technické výstupy, nie ich vzhľad**

Hongcheng Gao a spolupracovníci opisujú 1 301 úloh na 26 technických platformách s overovaním geometrie, fyzikálnej uskutočniteľnosti a pravidiel. Ich vlastné výsledky ukazujú osobitné problémy s postupmi cez viacero programov, preto je benchmark relevantný pre agentov ovládajúcich počítač v priemysle.

https://arxiv.org/abs/2609.37686

**OSWorld-Science hodnotí výsledky vedeckého softvéru**

Dingyuan Dai a kolegovia predstavujú 146 úloh zahŕňajúcich postupy ako kreslenie molekúl, patologickú analýzu či simuláciu. Stavy aplikácií a vytvorené výstupy umožňujú udeľovať čiastočné body, čím vzniká testovacie prostredie pre agentov, ktorí musia vytvoriť vedecké výsledky, nielen ovládať rozhranie.

https://arxiv.org/abs/2609.39903

**TraceDance mení zlyhania z nasadenia na cielené testy**

Dehai Min a spolupracovníci z ByteDance a University of Illinois Chicago vytvárajú benchmarky konkrétneho správania zo zaznamenaných relácií agentov. Testy hodnotia ďalší krok modelu v zaznamenanom rozhodovacom bode bez opakovania prostredia, čo pomáha posudzovať nežiaduce konanie unikajúce kontrole dokončenia úlohy.

https://arxiv.org/abs/2609.33295

**PROWBench porovnáva videá s udalosťami vykonanými programom**

Zheng-Hui Huang a kolegovia opisujú 170 epizód a 600 zástupných videí s časovanými záznamami sveta. Tieto záznamy umožňujú hodnotiť, či vygenerované zábery zobrazujú určené interakcie a pretrvávajúci stav, čo je presnejšia otázka než samotná vierohodnosť videa.

https://arxiv.org/abs/2610.02205

## Techniky promptovania

**OpenAI prepája pokyny s kontrolou dokončenia**

Sprievodca OpenAI pre tvorbu s GPT-6 odporúča explicitné podmienky úspechu, konkrétne obmedzenia a kontroly, či agent prácu skutočne dokončil. Príklady spoločnosti sú užitočné ako použiteľné vzory pokynov, nie ako záruka, že podrobnejší prompt vyrieši každé zlyhanie.

https://openai.com/index/practical-guide-building-gpt-6/

## Čo ľudia vytvárajú

**Graphene sprístupňuje analytiku kódovacím agentom**

Graphene spája sémantickú vrstvu pre SQL s formátom súborov dashboardov a postupom cez príkazový riadok. Repozitár tvorcom ukazuje preskúmateľný spôsob, ako uchovávať metriky, dotazy a prezentáciu v súboroch so správou verzií; tvrdenia o rýchlosti zostávajú tvrdeniami autorov.

https://github.com/graphene-data/graphene

**Engrams odlišuje izoláciu v produkcii a pri vývoji**

Engrams od Cortex koordinuje relácie kódovacích agentov na vlastnej infraštruktúre a v produkčnom návrhu používa mikrovirtuálne stroje Firecracker. Vývojový náhradný režim spúšťa bežné podprocesy, čo je dôležitý rozdiel pre vývojárov posudzujúcich tvrdenia repozitára o izolácii.

https://github.com/cortexapps/engrams

**Backburner poskytuje kód a testy pozornosti na telefóne**

Fork llama.cpp Backburner obsahuje protokol, cez ktorý telefón uchováva staršie stránky vyrovnávacej pamäte pozornosti a vracia Macu čiastkové výsledky pozornosti. Testovací program porovnáva pokračovania s pomocou telefónu a iba na Macu, čím poskytuje preskúmateľný podklad pre odovzdanie výpočtu; tvrdenia príspevku o rýchlosti tu zostávajú neoverené.

https://github.com/StayLameBro/backburner-llama.cpp/blob/master/ggml/src/ggml-metal/phone-attn.h
https://github.com/StayLameBro/backburner-llama.cpp/blob/master/tools/phone-kv-test/phone-kv-test.cpp

**Accuretta spája lokálny model s pracovným prostredím**

Accuretta spája lokálny model GGUF so súborovými nástrojmi, terminálmi, náhľadmi a schvaľovacími prvkami. Desktopový postup s dostupným zdrojovým kódom je relevantný pre tvorcov lokálnych agentov, pričom licencia pre osobné použitie podstatne obmedzuje ďalšie využitie.

https://github.com/mkultraware/accuretta

**messy-docs-bench hodnotí správnosť celých dokumentov**

Tashon Braganca zverejňuje prompty, referenčné odpovede a surové výstupy jednorazového testu 137 náročných dokumentov. Autor uvádza 59 % úplne správnych dokumentov pri lokálnom Qwen3-VL 8B a 57 % pri GPT-5.6 Terra, takže malý test možno preskúmať a zároveň ukazuje rozdiel medzi presnosťou polí a celých dokumentov.

https://github.com/TashonBraganca/messy-docs-bench

**AutoSynthData mení zlyhania agentov na tréningové úlohy**

AutoSynthData od ServiceNow generuje úlohy zamerané na schopnosti, ktoré cieľovému agentovi ešte chýbajú, a kontroluje uskutočniteľnosť aj súlad pokynov a overovacích mechanizmov. Technický opis vývojárom ponúka konkrétny postup tvorby tréningových úloh, pričom uvádzané zlepšenia sa vzťahujú na testované podnikové prostredia.

https://huggingface.co/blog/ServiceNow-AI/autosynthdata

## Stojí za prečítanie

**turbopuffer uvoľňuje väzbu úložiska na vektorový index**

Inžinier Dan Harrison vysvetľuje, prečo turbopuffer odoberá vektorovému indexu hlavnú organizačnú úlohu v úložisku. Text z 30. septembra spája túto voľbu s obmedzeniami agregácií a prehľadávania, čo je užitočné pre vyhľadávacích inžinierov; širšie benchmarky v3 ešte majú prísť.

https://turbopuffer.com/blog/rip-vector-database

**Helion spája automatické ladenie s výberom výpočtu**

Sean Chen a Shangdi Yu opisujú lineárny backend vLLM, ktorý vyberá ladené jadrá Helion pre malé dekódovacie úlohy a iné backendy pre väčšie rozmery. Merania iba na Hopper sú užitočné na pochopenie výberu výpočtu, ale nepotvrdzujú rovnaké zlepšenia na iných rodinách GPU.

https://pytorch.org/blog/building-a-high-performance-and-portable-vllm-linear-backend-with-helion/

**Mollick prehodnocuje potrebu riadiť tímy agentov**

Profesor Whartonu Ethan Mollick tvrdí, že novšie agenty dokážu organizovať prácu s menším ľudským navrhovaním tímových štruktúr, než očakával. Príklady sú anekdotické, no esej otvára konkrétnu otázku, ktoré koordinačné rozhodnutia musia ľudia ešte určovať.

https://www.oneusefulthing.org/p/the-dot-and-the-swarm

**Sarah sa pýta, čo by zahŕňal zákaz sebazlepšovania**

Prispievateľka LessWrong sarahhw rozlišuje viaceré významy rekurzívneho sebazlepšovania, od bežnej práce s nástrojmi po nahradenie výskumníkov. Jej argument je užitočný pre politickú diskusiu, pretože rozsah zákazu závisí od činnosti, ktorú jeho autori skutočne myslia.

https://www.lesswrong.com/posts/ZT2rKu3Z6RaargYYF/what-is-recursive-self-improvement-and-what-would-it-mean-to

**Dayen spája pochybenia agentov s motiváciami odvetvia**

David Dayen tvrdí, že medializované prieniky agentov odrážajú vlastný prístup odvetvia AI k získavaniu dát a zodpovednosti. Stĺpček stojí za prečítanie ako kritická interpretácia; navrhovaná príčinná súvislosť je argumentom autora, nie experimentálnym zistením.

https://prospect.org/2026/09/29/artificial-intelligence-agents-openai-microsoft-sam-altman-greg-brockman-ah-nice/

**Perone sa pýta, kto ochráni prehliadané verejné systémy**

Inžinier strojového učenia Christian S. Perone na vlastnom opise skoršieho oznámenia zraniteľnosti stavia otázku, ako verejné systémy odolajú rýchlejšiemu automatizovanému skúšaniu. Esej upozorňuje na nerovnomerné obranné kapacity, pričom historický incident zostáva vlastným opisom autora.

https://blog.christianperone.com/2026/09/the-systems-that-no-one-will-test/

**Asistent výučby spochybňuje stratu programátorského remesla**

Nemenovaný autor eseje na mondobe.com opisuje smútok z toho, že sa programovanie mení na dohľad nad generovanou prácou. Text je osobnou výpoveďou, nie prieskumom, a pomáha pochopiť obavu, ktorú samotné merania produktivity nezachytávajú.

https://mondobe.com/ai-makes-me-sad

**Housman opisuje otázky s pomocou AI pri neplodnosti**

Drew Housman opisuje používanie chatbota na skúmanie medicínskych otázok a diskusiu o možnostiach s lekármi počas liečby neplodnosti. Výpoveď stojí za prečítanie pre pacientovu skúsenosť s dostupnosťou a vytrvalosťou, no jej výsledok nemôže preukázať diagnostickú presnosť ani účinok liečby.

https://www.astralcodexten.com/p/our-ai-midwife

## Hacker News

**Správcovia jadra odlišujú hlásenia od použiteľných opráv**

Čitatelia diskutujú o prednáške Grega Kroah-Hartmana o hláseniach chýb jadra vytvorených AI a pýtajú sa, kedy sa podľa hlásenia dá konať. Vlákno pomáha odlíšiť opis pádu od reprodukovateľnej chyby; číselné tvrdenia prepísané komentujúcimi sa nepovažujú za overené citácie prednášky.

https://news.ycombinator.com/item?id=49929391

**Čitatelia pri Strategu sledujú efektívnosť tréningu**

Komentujúci pri diskusii o novom výsledku Ataraxos pripomínajú skorší DeepNash od DeepMind. Ich nesúhlas upriamuje pozornosť na efektívnosť tréningu a historické porovnanie namiesto považovania samotnej silnej hry Stratego za bezprecedentnú.

https://news.ycombinator.com/item?id=49933740

**Záznamy kódovania s GLM vyvolávajú otázky o nákladoch**

Čitatelia mesačnej skúsenosti Wagtail s GLM 5.3 Flash diskutujú o spojení lacnejšieho kódovacieho modelu so silnejšími modelmi na plánovanie a kontrolu. Iní sa pýtajú na meranie nákladov a energie, čo pomáha odlíšiť skúsenosť s pracovným postupom od reprodukovateľného porovnania efektívnosti.

https://news.ycombinator.com/item?id=49934620

**Používatelia DwarfStar zdieľajú úpravy lokálnej inferencie**

Diskusia o DwarfStar obsahuje požiadavku prispievateľa na začlenenie dlhého kontextu aj samostatný inferenčný engine pre Intel inšpirovaný projektom. Ide o odkazy od používateľov, nie o overené porovnania výkonu; pozornosť si zaslúžia pre konkrétny kód za experimentmi s lokálnym hardvérom.

https://news.ycombinator.com/item?id=49936575

**Maliarske plátno vyvoláva spor o schopnosti modelu**

Ukážka simulovaného štetca a plátna Stillwet vyvoláva otázky, ako jazykové modely vytvárajú obrazy prostredníctvom akcií. Tvrdenia, že schopnosť musí byť emergentná, zostávajú špekuláciou; vlákno je užitočné rozlíšením pútavej ukážky od vysvetlenia tréningu.

https://news.ycombinator.com/item?id=49928566

**Diskusie o hostovaných weboch rozdeľujú vývojárov**

Čitatelia vítajú jednoduchšie publikovanie webov v ChatGPT, no spochybňujú kvalitu výstupov a vstup poskytovateľa modelu do aplikačnej vrstvy. Ide o názory na pracovné postupy a konkurenciu, ktoré pomáhajú pochopiť reakcie vývojárov bez tvrdení o meranom prijatí či kvalite.

https://news.ycombinator.com/item?id=49927747

**Predpoveď o SaaS ako riadení modelov naráža na odpor**

Podporovatelia opisujú čoraz automatizovanejšie postupy, zatiaľ čo kritici eseje o riadení modelov tvrdia, že systémy, ktoré videli, stále vedú odborníci na danú oblasť. Nesúhlas si zaslúži pozornosť, pretože široká predpoveď o odvetví silno závisí od pracovných postupov považovaných za dôkaz.

https://news.ycombinator.com/item?id=49938616

**Čitatelia pri WoW zisťujú, či agent dokončil úlohu**

Komentujúci sa pýtajú, či ukážka GPT-6 Astra dokončila požadované úlohy a aký podiel malo vlastné riadenie agenta. Vlákno odlišuje fungujúcu hernú ukážku od spoľahlivého dokončenia úloh bez toho, aby poskytovalo kontrolované porovnanie.

https://news.ycombinator.com/item?id=49933251

## YouTube

**YC Paper Club predstavuje alternatívy výpočtov na GPU**

Paper Club organizácie Y Combinator spája prednášajúcich o optických, neuromorfných a biologických výpočtoch. Kapitoly rozlišujú výpočty pomocou svetla, čipy inšpirované mozgom a pokusy so živými neurónmi, čím poskytujú technický úvod do prístupov mimo bežných GPU bez toho, aby ich vydávali za zameniteľné alebo pripravené náhrady.

https://www.youtube.com/watch?v=xc2FTBGRSJo

**Tristan Buckmaster rozoberá matematiku vytvorenú AI**

Matematik Tristan Buckmaster z NYU sa s fyzikom Brianom Greenom rozpráva o rovniciach tekutín a čitateľnosti dôkazov vytvorených AI. Opis otvára rozdiel medzi prijatím dôkazu a jeho pochopením, takže rozhovor je relevantný pre vedecké dôsledky matematiky podporovanej strojmi; matematické tvrdenia si vyžadujú pôvodné práce.

https://www.youtube.com/watch?v=PQYFRuZ5phs

**Elie Bakouch porovnáva agentov v optimalizačnej súťaži**

Výskumný inžinier Prime Intellect Elie Bakouch opisuje súťaž programovacích agentov v trénovaní malého modelu s menším počtom krokov. Opis oddeľuje zlepšenia dosiahnuté kombináciou známych metód od vynájdenia optimalizátora, preto je prednáška relevantná pre tvrdenia o automatizovanom výskume.

https://www.youtube.com/watch?v=oVsEddfhdxc

**Lakshya Agrawal vysvetľuje optimalizáciu promptov reflexiou**

Doktorand UC Berkeley Lakshya Agrawal vysvetľuje GEPA, ktorý využíva záznamy uvažovania modelu a chýb nástrojov na úpravu promptov. Opis to porovnáva s redukovaním pokusu o splnenie úlohy na skóre odmeny; je užitočný na pochopenie metódy, pričom uvádzané zlepšenia výkonu zostávajú tvrdeniami autora.

https://www.youtube.com/watch?v=OA-Mc60Rboo

**Hugging Face ukazuje nepretržite dostupného asistenta Pi**

Návod Hugging Face opisuje osobných a výskumných asistentov bežiacich na nepretržite zapnutom počítači s Pi, Telegramom a lokálnym smerovaním relácií. Odkazovaný kód pi-gateway poskytuje tvorcom overiteľné východisko; podpora ďalších platforiem je opísaná ako budúca práca.

https://www.youtube.com/watch?v=HU03WDFB_tQ

**Eric Schmidt rozoberá AI na ukrajinskom bojisku**

Bývalý výkonný riaditeľ Googlu Eric Schmidt sa so Zanny Minton Beddoes z The Economist rozpráva o vojenskej AI a adaptácii na Ukrajine. Schmidt vedie spoločnosť vyrábajúcu drony a má v tejto oblasti obchodné záujmy; rozhovor je zaujímavý ako pohľad účastníka, nie ako nezávislé hodnotenie.

https://www.youtube.com/watch?v=KgJI4Wxqqik

**Markus Gabriel rozoberá sľuby a obavy spojené s AI**

Nemecký filozof Markus Gabriel rozoberá AI v NZZ Standpunkte, ktorého opis otvára otázky kontroly, práce a očakávaní od technológie. Rozhovor v nemčine je filozofickou diskusiou, ktorú treba počúvať pre jej argumenty, nie opisom potvrdzujúcim jej závery.

https://www.youtube.com/watch?v=uPJO4URd0w8

**Viedeň rozoberá ľudskú dôstojnosť pri vývoji AI**

Teológ Andreas R. Batlogg a dekanka informatiky TU Wien Gerti Kappel rozoberajú ľudskú dôstojnosť a digitálny humanizmus na Wiener Vorlesung. Opis podujatia v nemčine predstavuje AI ako technológiu, ktorú musia formovať ľudia, a ponúka etický pohľad bez dostatku podrobností na určenie úplných stanovísk prednášajúcich.

https://www.youtube.com/watch?v=8Skv9rtR_Fk

**Tom Krcha opisuje tvorbu dizajnérskeho nástroja agentmi**

Zakladateľ dizajnérskeho nástroja Tom Krcha opisuje prácu agentov počas noci a ukazuje úpravu tmavého režimu pre CzechCrunch. Rozhovor s tvorcom v češtine je zaujímavý pre predvedený pracovný postup a jeho argument pre výber rýchlych modelov tam, kde väčší model nie je potrebný.

https://www.youtube.com/watch?v=cNlAF3USuns

**Zixuan Li vysvetľuje význam otvorených váh na špičke**

Zixuan Li zo Z.ai rozoberá GLM-5.2 a dôvody laboratória na zverejňovanie váh vrátane vlastného hostovania a doménových úprav. Opis ponúka pohľad laboratória na distribučné rozhodnutia; postavenie v benchmarkoch zostáva tvrdením spoločnosti. Kanál: AI Engineer.

https://www.youtube.com/watch?v=9JFGohx4E7U

**Weco odlišuje zlepšovanie riadenia od sebazlepšovania**

Spoluzakladateľ Weco Zhengyao Jiang rozoberá osemdňový experiment, ktorý menil riadenie agenta pri nezmenenom modeli. Opis zdôrazňuje hodnotenie na oddelených dátach a obchádzanie odmeny, takže rozhovor pomáha odlíšiť lepšie plnenie úloh od lepšej schopnosti zlepšovať sa. Kanál: Machine Learning Street Talk.

https://www.youtube.com/watch?v=yB6_iFGTq9k

**Stanford otvára aktualizovaný kurz transformerov**

Úvodná prednáška CME295 od Afshineho a Shervineho Amidiovcov pokrýva tokenizáciu, pozornosť a transformer s enkóderom a dekóderom. Oficiálne kapitoly z nej robia užitočné zopakovanie základov aj východisko pre sledovanie jesenného kurzu. Kanál: Stanford Online.

https://www.youtube.com/watch?v=114i2Kz-LZA

**Garrison Lovely spochybňuje nevyhnutnosť náhrady práce**

Novinár Garrison Lovely tvrdí, že nahrádzanie ľudskej práce je politickou a priemyselnou voľbou odlišnou od užitočnej špecializovanej AI. Opis rozhovoru predstavuje angažovaný pohľad na správu a moc pracovníkov, ktorý stojí za vypočutie ako argument, nie ako predpoveď potvrdená dátami. Kanál: The Cognitive Revolution.

https://www.youtube.com/watch?v=PiBNrW7Q_Ws

**DeepMind vysvetľuje vodoznaky v médiách aj biológii**

Hannah Fry vedie rozhovor s Pushmeetom Kohlim a Jeremym Ratcliffom o SynthID a jeho rozšírení na proteínové sekvencie. Opis z neho robí užitočné vysvetlenie techník určovania pôvodu od laboratória, pričom tvrdenia o zachovaní biologickej funkcie patria vývojárom. Kanál: Google DeepMind.

https://www.youtube.com/watch?v=HIUzrxQxTtw

**Deník N porovnáva americkú a čínsku politiku AI**

Český program Amerika bejby uvádza diskusiu o odlišných prístupoch USA a Číny ku konkurencii a regulácii AI. YouTube obsahuje úvodný úryvok a celá epizóda je dostupná v predplatnom; ide o odkaz na diskusiu, nie o overený opis všetkých jej záverov. Kanál: Deník N · Jazyk: čeština.

https://www.youtube.com/watch?v=0DcYD-l7aRk

## V skratke

**Georgia reaguje na ukážku ohrozenia súkromia hlasovania**

Volebná rada Georgie zasadla 1. októbra po augustovej štúdii, ktorá ukázala, ako verejné záznamy môžu odhaliť poradie hlasovacích lístkov a s ďalšími údajmi identifikovať niektoré hlasy. Medializovaná reakcia zahŕňa odstránenie identifikátorov lístkov, takže novou udalosťou je ochrana súkromia, nie práve vydaná štúdia.

https://www.theguardian.com/us-news/2026/oct/02/midterms-ai-ballot-privacy
https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/

**Apple plánuje jasnejší súhlas s Full Disk Access**

Apple uvádza, že budúce prvky budú pred udelením Full Disk Access vyžadovať explicitnejší krok používateľa, a odvoláva sa na rastúce schopnosti agentov AI. Oznámenie je dôležité pre vývojárov lokálnych asistentov, no zatiaľ neuvádza dátum vydania ani nové pravidlá API.

https://developer.apple.com/news/?id=p6zjojqw

**Nvidia pripravuje DGX Spark s menšou pamäťou**

DGX Spark od Nvidie so 64 GB pamäte zachováva platformu GB10 a má prísť cez partnerov 23. októbra. Tvrdenia o lokálnej inferencii a spojení dvoch jednotiek uvádza výrobca; vývojári získavajú možnosť s menšou kapacitou, ktorej využiteľná veľkosť modelu stále závisí od presnosti a kontextu. The Register uvádza počiatočnú cenu 4 999 dolárov.

https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/
https://www.theregister.com/systems/2026/10/02/nvidia-debuts-4999-dgx-spark-with-half-the-ram-and-storage-amid-memory-crunch/5300622

**AWS mení vybrané sadzby rezervovaných GPU 7. októbra**

AWS uvádza nové sadzby Capacity Blocks za akcelerátor platné od 7. októbra, pričom kúpené bloky si zachovávajú cenu z nákupu. On-Demand, Savings Plans a ostatné sadzby Capacity Blocks sa nemenia, čo je dôležité rozlíšenie pri odhade nákladov na tréningovú kapacitu.

https://aws.amazon.com/ec2/capacityblocks/pricing/

## Biznis v skratke

**Amazon vyčleňuje peniaze pre komunity pri dátových centrách**

Amazon uvádza, že Built Together investuje počas piatich rokov viac než 1 miliardu dolárov do komunít pri jeho dátových centrách, pričom priority výdavkov sa budú určovať miestne.

https://www.aboutamazon.com/news/company-news/amazon-data-centers-built-together

**Anthropic financuje akadémiu podnikových inžinierov**

Anthropic oznamuje záväzok 100 miliónov dolárov pre Claude Frontier Academy a cieľ vyškoliť do konca roka 2027 10 000 inžinierov nasadzujúcich riešenia priamo u zákazníkov.

https://www.anthropic.com/news/claude-frontier-academy

**Bloomberg píše o možnom vymenovaní Claytona**

Bloomberg s odvolaním na nemenovaný zdroj píše, že Trump by mal vybrať Jaya Claytona za poradcu pre AI; správa nepotvrdzuje dokončené vymenovanie.

https://www.spokesman.com/stories/2026/oct/02/trump-set-to-name-jay-clayton-as-ai-czar-with-safe/

» **Prečo na tom záleží:** Tieto zdroje ukazujú, kde sa deklarované schopnosti stretávajú s pracovnými postupmi, meraním a konkrétnymi obmedzeniami nástrojov.

**Čo z toho vyplýva:** Kvalita úloh, usmernení a overovania výsledkov zostáva spoločnou témou výskumu aj praktického vývoja agentov.

**Čo bude nasledovať:** Nové vybrané sadzby AWS platia od 7. októbra a partnerské systémy DGX Spark so 64 GB majú prísť 23. októbra; turbopuffer sľubuje širšie benchmarky v3 v nasledujúcich týždňoch.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Model inverznej dynamiky od Reka odhaduje pohyby kamery z videa a poskytuje váhy trénované na herných dátach. Tvorcom interaktívneho videa ponúka konkrétny východiskový bod; zverejnená presnosť zostáva vlastným meraním laboratória. | PODĽA SPOLOČNOSTI | https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model | žiadne |
| Renping Zhou a kolegovia zisťujú, že robotické politiky strácajú schopnosť zovšeobecňovať, keď úplne odstránia reprezentácie budúcnosti. Simple-WAM zachováva jediný výpočet nad zašumenými tokenmi budúceho videa, preto je štúdia relevantná pre znižovanie nákladov videomodelov bez odstránenia informácií používaných pri výbere akcií. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.34981 | žiadne |
| Xin Li a kolegovia zisťujú, že väčšia škála spätnej väzby špecialistu môže ovládnuť destiláciu s viacerými učiteľmi aj pri správnom smerovaní promptov. Zmena škály spätnej väzby podľa domény zlepšuje ich spoločného študenta a upozorňuje na tréningovú premennú, ktorú samotný výber správneho učiteľa nerieši. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.35347 | žiadne |
| Jiaxin Ge a spolupracovníci mapujú 19 úloh generovania obrazu na 25 schopností vizuálneho porozumenia. Výsledky autorov ukazujú selektívny prenos, napríklad prínos predikcie hĺbky pre priestorové uvažovanie, preto práca pomáha pri výbere tréningových úloh namiesto predpokladu, že každé generovanie obrazu zlepšuje všetko vnímanie. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.38079 | žiadne |
| Minghan Wang a kolegovia zachovávajú model aj úlohu a menia spoľahlivosť pokynov pracovného postupu. Ich preprint nachádza zraniteľnosť voči zavádzajúcemu usmerneniu a skúša tréningové zásahy, čím vývojárom agentov ponúka spôsob, ako oddeliť schopnosť riešiť úlohu od rozumného spoliehania sa na vonkajšie pokyny. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.39578 | žiadne |
| Tianxiang Gao a kolegovia uvádzajú, že rozhodovacie modely JEV a KEV používajú užší rozsah usporiadaných označení než referenčné odpovede, aj keď ich celková presnosť vyzerá slušne. Jav pretrváva po zmene poradia možností, takže využitie stupnice predstavuje samostatnú otázku automatického hodnotenia. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.38827 | žiadne |
| Pavel Tikhonov a spolupracovníci zoraďujú možné vzťahy medzi celočíselnými postupnosťami pomocou klasifikátora nad aktiváciami modelu a potom ich filtrujú a kontrolujú. Autori ponechávajú 13 vzťahov na prezentáciu a štyri považujú za nové, čím poskytujú konkrétny opis výberu matematických otázok namiesto samotného odpovedania na zadané úlohy. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.32264 | žiadne |
| Injin Kong a kolegovia zo Seoul National University skúmajú, kedy maskované difúzne jazykové modely získajú zmenou rozhodnutí o odkrývaní tokenov. Ich vlastné experimenty nachádzajú sústredené príležitosti namiesto rovnomerných prínosov, čo pomáha odlíšiť adaptívnu inferenciu od jednoduchého menenia každého kroku. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.33355 | žiadne |
| Hongcheng Gao a spolupracovníci opisujú 1 301 úloh na 26 technických platformách s overovaním geometrie, fyzikálnej uskutočniteľnosti a pravidiel. Ich vlastné výsledky ukazujú osobitné problémy s postupmi cez viacero programov, preto je benchmark relevantný pre agentov ovládajúcich počítač v priemysle. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.37686 | žiadne |
| Dingyuan Dai a kolegovia predstavujú 146 úloh zahŕňajúcich postupy ako kreslenie molekúl, patologickú analýzu či simuláciu. Stavy aplikácií a vytvorené výstupy umožňujú udeľovať čiastočné body, čím vzniká testovacie prostredie pre agentov, ktorí musia vytvoriť vedecké výsledky, nielen ovládať rozhranie. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.39903 | žiadne |
| Dehai Min a spolupracovníci z ByteDance a University of Illinois Chicago vytvárajú benchmarky konkrétneho správania zo zaznamenaných relácií agentov. Testy hodnotia ďalší krok modelu v zaznamenanom rozhodovacom bode bez opakovania prostredia, čo pomáha posudzovať nežiaduce konanie unikajúce kontrole dokončenia úlohy. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.33295 | žiadne |
| Zheng-Hui Huang a kolegovia opisujú 170 epizód a 600 zástupných videí s časovanými záznamami sveta. Tieto záznamy umožňujú hodnotiť, či vygenerované zábery zobrazujú určené interakcie a pretrvávajúci stav, čo je presnejšia otázka než samotná vierohodnosť videa. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.02205 | žiadne |
| Sprievodca OpenAI pre tvorbu s GPT-6 odporúča explicitné podmienky úspechu, konkrétne obmedzenia a kontroly, či agent prácu skutočne dokončil. Príklady spoločnosti sú užitočné ako použiteľné vzory pokynov, nie ako záruka, že podrobnejší prompt vyrieši každé zlyhanie. | PODĽA SPOLOČNOSTI | https://openai.com/index/practical-guide-building-gpt-6/ | žiadne |
| Graphene spája sémantickú vrstvu pre SQL s formátom súborov dashboardov a postupom cez príkazový riadok. Repozitár tvorcom ukazuje preskúmateľný spôsob, ako uchovávať metriky, dotazy a prezentáciu v súboroch so správou verzií; tvrdenia o rýchlosti zostávajú tvrdeniami autorov. | PODĽA SPOLOČNOSTI | https://github.com/graphene-data/graphene | žiadne |
| Engrams od Cortex koordinuje relácie kódovacích agentov na vlastnej infraštruktúre a v produkčnom návrhu používa mikrovirtuálne stroje Firecracker. Vývojový náhradný režim spúšťa bežné podprocesy, čo je dôležitý rozdiel pre vývojárov posudzujúcich tvrdenia repozitára o izolácii. | OVERENÉ | https://github.com/cortexapps/engrams | žiadne |
| Fork llama.cpp Backburner obsahuje protokol, cez ktorý telefón uchováva staršie stránky vyrovnávacej pamäte pozornosti a vracia Macu čiastkové výsledky pozornosti. Testovací program porovnáva pokračovania s pomocou telefónu a iba na Macu, čím poskytuje preskúmateľný podklad pre odovzdanie výpočtu; tvrdenia príspevku o rýchlosti tu zostávajú neoverené. | OVERENÉ | https://github.com/StayLameBro/backburner-llama.cpp/blob/master/ggml/src/ggml-metal/phone-attn.h ; https://github.com/StayLameBro/backburner-llama.cpp/blob/master/tools/phone-kv-test/phone-kv-test.cpp | žiadne |
| Accuretta spája lokálny model GGUF so súborovými nástrojmi, terminálmi, náhľadmi a schvaľovacími prvkami. Desktopový postup s dostupným zdrojovým kódom je relevantný pre tvorcov lokálnych agentov, pričom licencia pre osobné použitie podstatne obmedzuje ďalšie využitie. | OVERENÉ | https://github.com/mkultraware/accuretta | žiadne |
| Tashon Braganca zverejňuje prompty, referenčné odpovede a surové výstupy jednorazového testu 137 náročných dokumentov. Autor uvádza 59 % úplne správnych dokumentov pri lokálnom Qwen3-VL 8B a 57 % pri GPT-5.6 Terra, takže malý test možno preskúmať a zároveň ukazuje rozdiel medzi presnosťou polí a celých dokumentov. | PODĽA SPOLOČNOSTI | https://github.com/TashonBraganca/messy-docs-bench | žiadne |
| AutoSynthData od ServiceNow generuje úlohy zamerané na schopnosti, ktoré cieľovému agentovi ešte chýbajú, a kontroluje uskutočniteľnosť aj súlad pokynov a overovacích mechanizmov. Technický opis vývojárom ponúka konkrétny postup tvorby tréningových úloh, pričom uvádzané zlepšenia sa vzťahujú na testované podnikové prostredia. | PODĽA SPOLOČNOSTI | https://huggingface.co/blog/ServiceNow-AI/autosynthdata | žiadne |
| Inžinier Dan Harrison vysvetľuje, prečo turbopuffer odoberá vektorovému indexu hlavnú organizačnú úlohu v úložisku. Text z 30. septembra spája túto voľbu s obmedzeniami agregácií a prehľadávania, čo je užitočné pre vyhľadávacích inžinierov; širšie benchmarky v3 ešte majú prísť. | NÁZOR | https://turbopuffer.com/blog/rip-vector-database | žiadne |
| Sean Chen a Shangdi Yu opisujú lineárny backend vLLM, ktorý vyberá ladené jadrá Helion pre malé dekódovacie úlohy a iné backendy pre väčšie rozmery. Merania iba na Hopper sú užitočné na pochopenie výberu výpočtu, ale nepotvrdzujú rovnaké zlepšenia na iných rodinách GPU. | PODĽA SPOLOČNOSTI | https://pytorch.org/blog/building-a-high-performance-and-portable-vllm-linear-backend-with-helion/ | žiadne |
| Profesor Whartonu Ethan Mollick tvrdí, že novšie agenty dokážu organizovať prácu s menším ľudským navrhovaním tímových štruktúr, než očakával. Príklady sú anekdotické, no esej otvára konkrétnu otázku, ktoré koordinačné rozhodnutia musia ľudia ešte určovať. | NÁZOR | https://www.oneusefulthing.org/p/the-dot-and-the-swarm | žiadne |
| Prispievateľka LessWrong sarahhw rozlišuje viaceré významy rekurzívneho sebazlepšovania, od bežnej práce s nástrojmi po nahradenie výskumníkov. Jej argument je užitočný pre politickú diskusiu, pretože rozsah zákazu závisí od činnosti, ktorú jeho autori skutočne myslia. | NÁZOR | https://www.lesswrong.com/posts/ZT2rKu3Z6RaargYYF/what-is-recursive-self-improvement-and-what-would-it-mean-to | žiadne |
| David Dayen tvrdí, že medializované prieniky agentov odrážajú vlastný prístup odvetvia AI k získavaniu dát a zodpovednosti. Stĺpček stojí za prečítanie ako kritická interpretácia; navrhovaná príčinná súvislosť je argumentom autora, nie experimentálnym zistením. | NÁZOR | https://prospect.org/2026/09/29/artificial-intelligence-agents-openai-microsoft-sam-altman-greg-brockman-ah-nice/ | žiadne |
| Inžinier strojového učenia Christian S. Perone na vlastnom opise skoršieho oznámenia zraniteľnosti stavia otázku, ako verejné systémy odolajú rýchlejšiemu automatizovanému skúšaniu. Esej upozorňuje na nerovnomerné obranné kapacity, pričom historický incident zostáva vlastným opisom autora. | NÁZOR | https://blog.christianperone.com/2026/09/the-systems-that-no-one-will-test/ | žiadne |
| Nemenovaný autor eseje na mondobe.com opisuje smútok z toho, že sa programovanie mení na dohľad nad generovanou prácou. Text je osobnou výpoveďou, nie prieskumom, a pomáha pochopiť obavu, ktorú samotné merania produktivity nezachytávajú. | NÁZOR | https://mondobe.com/ai-makes-me-sad | žiadne |
| Drew Housman opisuje používanie chatbota na skúmanie medicínskych otázok a diskusiu o možnostiach s lekármi počas liečby neplodnosti. Výpoveď stojí za prečítanie pre pacientovu skúsenosť s dostupnosťou a vytrvalosťou, no jej výsledok nemôže preukázať diagnostickú presnosť ani účinok liečby. | NÁZOR | https://www.astralcodexten.com/p/our-ai-midwife | žiadne |
| Čitatelia diskutujú o prednáške Grega Kroah-Hartmana o hláseniach chýb jadra vytvorených AI a pýtajú sa, kedy sa podľa hlásenia dá konať. Vlákno pomáha odlíšiť opis pádu od reprodukovateľnej chyby; číselné tvrdenia prepísané komentujúcimi sa nepovažujú za overené citácie prednášky. | NÁZOR | https://news.ycombinator.com/item?id=49929391 | žiadne |
| Komentujúci pri diskusii o novom výsledku Ataraxos pripomínajú skorší DeepNash od DeepMind. Ich nesúhlas upriamuje pozornosť na efektívnosť tréningu a historické porovnanie namiesto považovania samotnej silnej hry Stratego za bezprecedentnú. | NÁZOR | https://news.ycombinator.com/item?id=49933740 | žiadne |
| Čitatelia mesačnej skúsenosti Wagtail s GLM 5.3 Flash diskutujú o spojení lacnejšieho kódovacieho modelu so silnejšími modelmi na plánovanie a kontrolu. Iní sa pýtajú na meranie nákladov a energie, čo pomáha odlíšiť skúsenosť s pracovným postupom od reprodukovateľného porovnania efektívnosti. | NÁZOR | https://news.ycombinator.com/item?id=49934620 | žiadne |
| Diskusia o DwarfStar obsahuje požiadavku prispievateľa na začlenenie dlhého kontextu aj samostatný inferenčný engine pre Intel inšpirovaný projektom. Ide o odkazy od používateľov, nie o overené porovnania výkonu; pozornosť si zaslúžia pre konkrétny kód za experimentmi s lokálnym hardvérom. | NÁZOR | https://news.ycombinator.com/item?id=49936575 | žiadne |
| Ukážka simulovaného štetca a plátna Stillwet vyvoláva otázky, ako jazykové modely vytvárajú obrazy prostredníctvom akcií. Tvrdenia, že schopnosť musí byť emergentná, zostávajú špekuláciou; vlákno je užitočné rozlíšením pútavej ukážky od vysvetlenia tréningu. | NÁZOR | https://news.ycombinator.com/item?id=49928566 | žiadne |
| Čitatelia vítajú jednoduchšie publikovanie webov v ChatGPT, no spochybňujú kvalitu výstupov a vstup poskytovateľa modelu do aplikačnej vrstvy. Ide o názory na pracovné postupy a konkurenciu, ktoré pomáhajú pochopiť reakcie vývojárov bez tvrdení o meranom prijatí či kvalite. | NÁZOR | https://news.ycombinator.com/item?id=49927747 | žiadne |
| Podporovatelia opisujú čoraz automatizovanejšie postupy, zatiaľ čo kritici eseje o riadení modelov tvrdia, že systémy, ktoré videli, stále vedú odborníci na danú oblasť. Nesúhlas si zaslúži pozornosť, pretože široká predpoveď o odvetví silno závisí od pracovných postupov považovaných za dôkaz. | NÁZOR | https://news.ycombinator.com/item?id=49938616 | žiadne |
| Komentujúci sa pýtajú, či ukážka GPT-6 Astra dokončila požadované úlohy a aký podiel malo vlastné riadenie agenta. Vlákno odlišuje fungujúcu hernú ukážku od spoľahlivého dokončenia úloh bez toho, aby poskytovalo kontrolované porovnanie. | NÁZOR | https://news.ycombinator.com/item?id=49933251 | žiadne |
| Paper Club organizácie Y Combinator spája prednášajúcich o optických, neuromorfných a biologických výpočtoch. Kapitoly rozlišujú výpočty pomocou svetla, čipy inšpirované mozgom a pokusy so živými neurónmi, čím poskytujú technický úvod do prístupov mimo bežných GPU bez toho, aby ich vydávali za zameniteľné alebo pripravené náhrady. | NÁZOR | https://www.youtube.com/watch?v=xc2FTBGRSJo | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=xc2FTBGRSJo | žiadne |
| Matematik Tristan Buckmaster z NYU sa s fyzikom Brianom Greenom rozpráva o rovniciach tekutín a čitateľnosti dôkazov vytvorených AI. Opis otvára rozdiel medzi prijatím dôkazu a jeho pochopením, takže rozhovor je relevantný pre vedecké dôsledky matematiky podporovanej strojmi; matematické tvrdenia si vyžadujú pôvodné práce. | NÁZOR | https://www.youtube.com/watch?v=PQYFRuZ5phs | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=PQYFRuZ5phs | žiadne |
| Výskumný inžinier Prime Intellect Elie Bakouch opisuje súťaž programovacích agentov v trénovaní malého modelu s menším počtom krokov. Opis oddeľuje zlepšenia dosiahnuté kombináciou známych metód od vynájdenia optimalizátora, preto je prednáška relevantná pre tvrdenia o automatizovanom výskume. | NÁZOR | https://www.youtube.com/watch?v=oVsEddfhdxc | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=oVsEddfhdxc | žiadne |
| Doktorand UC Berkeley Lakshya Agrawal vysvetľuje GEPA, ktorý využíva záznamy uvažovania modelu a chýb nástrojov na úpravu promptov. Opis to porovnáva s redukovaním pokusu o splnenie úlohy na skóre odmeny; je užitočný na pochopenie metódy, pričom uvádzané zlepšenia výkonu zostávajú tvrdeniami autora. | NÁZOR | https://www.youtube.com/watch?v=OA-Mc60Rboo | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=OA-Mc60Rboo | žiadne |
| Návod Hugging Face opisuje osobných a výskumných asistentov bežiacich na nepretržite zapnutom počítači s Pi, Telegramom a lokálnym smerovaním relácií. Odkazovaný kód pi-gateway poskytuje tvorcom overiteľné východisko; podpora ďalších platforiem je opísaná ako budúca práca. | NÁZOR | https://www.youtube.com/watch?v=HU03WDFB_tQ | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=HU03WDFB_tQ | žiadne |
| Bývalý výkonný riaditeľ Googlu Eric Schmidt sa so Zanny Minton Beddoes z The Economist rozpráva o vojenskej AI a adaptácii na Ukrajine. Schmidt vedie spoločnosť vyrábajúcu drony a má v tejto oblasti obchodné záujmy; rozhovor je zaujímavý ako pohľad účastníka, nie ako nezávislé hodnotenie. | NÁZOR | https://www.youtube.com/watch?v=KgJI4Wxqqik | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=KgJI4Wxqqik | žiadne |
| Nemecký filozof Markus Gabriel rozoberá AI v NZZ Standpunkte, ktorého opis otvára otázky kontroly, práce a očakávaní od technológie. Rozhovor v nemčine je filozofickou diskusiou, ktorú treba počúvať pre jej argumenty, nie opisom potvrdzujúcim jej závery. | NÁZOR | https://www.youtube.com/watch?v=uPJO4URd0w8 | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=uPJO4URd0w8 | žiadne |
| Teológ Andreas R. Batlogg a dekanka informatiky TU Wien Gerti Kappel rozoberajú ľudskú dôstojnosť a digitálny humanizmus na Wiener Vorlesung. Opis podujatia v nemčine predstavuje AI ako technológiu, ktorú musia formovať ľudia, a ponúka etický pohľad bez dostatku podrobností na určenie úplných stanovísk prednášajúcich. | NÁZOR | https://www.youtube.com/watch?v=8Skv9rtR_Fk | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=8Skv9rtR_Fk | žiadne |
| Zakladateľ dizajnérskeho nástroja Tom Krcha opisuje prácu agentov počas noci a ukazuje úpravu tmavého režimu pre CzechCrunch. Rozhovor s tvorcom v češtine je zaujímavý pre predvedený pracovný postup a jeho argument pre výber rýchlych modelov tam, kde väčší model nie je potrebný. | NÁZOR | https://www.youtube.com/watch?v=cNlAF3USuns | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=cNlAF3USuns | žiadne |
| Zixuan Li zo Z.ai rozoberá GLM-5.2 a dôvody laboratória na zverejňovanie váh vrátane vlastného hostovania a doménových úprav. Opis ponúka pohľad laboratória na distribučné rozhodnutia; postavenie v benchmarkoch zostáva tvrdením spoločnosti. Kanál: AI Engineer. | NÁZOR | https://www.youtube.com/watch?v=9JFGohx4E7U | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=9JFGohx4E7U | žiadne |
| Spoluzakladateľ Weco Zhengyao Jiang rozoberá osemdňový experiment, ktorý menil riadenie agenta pri nezmenenom modeli. Opis zdôrazňuje hodnotenie na oddelených dátach a obchádzanie odmeny, takže rozhovor pomáha odlíšiť lepšie plnenie úloh od lepšej schopnosti zlepšovať sa. Kanál: Machine Learning Street Talk. | NÁZOR | https://www.youtube.com/watch?v=yB6_iFGTq9k | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=yB6_iFGTq9k | žiadne |
| Úvodná prednáška CME295 od Afshineho a Shervineho Amidiovcov pokrýva tokenizáciu, pozornosť a transformer s enkóderom a dekóderom. Oficiálne kapitoly z nej robia užitočné zopakovanie základov aj východisko pre sledovanie jesenného kurzu. Kanál: Stanford Online. | NÁZOR | https://www.youtube.com/watch?v=114i2Kz-LZA | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=114i2Kz-LZA | žiadne |
| Novinár Garrison Lovely tvrdí, že nahrádzanie ľudskej práce je politickou a priemyselnou voľbou odlišnou od užitočnej špecializovanej AI. Opis rozhovoru predstavuje angažovaný pohľad na správu a moc pracovníkov, ktorý stojí za vypočutie ako argument, nie ako predpoveď potvrdená dátami. Kanál: The Cognitive Revolution. | NÁZOR | https://www.youtube.com/watch?v=PiBNrW7Q_Ws | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=PiBNrW7Q_Ws | žiadne |
| Hannah Fry vedie rozhovor s Pushmeetom Kohlim a Jeremym Ratcliffom o SynthID a jeho rozšírení na proteínové sekvencie. Opis z neho robí užitočné vysvetlenie techník určovania pôvodu od laboratória, pričom tvrdenia o zachovaní biologickej funkcie patria vývojárom. Kanál: Google DeepMind. | NÁZOR | https://www.youtube.com/watch?v=HIUzrxQxTtw | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=HIUzrxQxTtw | žiadne |
| Český program Amerika bejby uvádza diskusiu o odlišných prístupoch USA a Číny ku konkurencii a regulácii AI. YouTube obsahuje úvodný úryvok a celá epizóda je dostupná v predplatnom; ide o odkaz na diskusiu, nie o overený opis všetkých jej záverov. Kanál: Deník N · Jazyk: čeština. | NÁZOR | https://www.youtube.com/watch?v=0DcYD-l7aRk | žiadne |
| Kanál a témy uvedené v oficiálnom opise videa. | OVERENÉ | https://www.youtube.com/watch?v=0DcYD-l7aRk | žiadne |
| Volebná rada Georgie zasadla 1. októbra po augustovej štúdii, ktorá ukázala, ako verejné záznamy môžu odhaliť poradie hlasovacích lístkov a s ďalšími údajmi identifikovať niektoré hlasy. Medializovaná reakcia zahŕňa odstránenie identifikátorov lístkov, takže novou udalosťou je ochrana súkromia, nie práve vydaná štúdia. | OVERENÉ | https://www.theguardian.com/us-news/2026/oct/02/midterms-ai-ballot-privacy ; https://blog.citp.princeton.edu/2026/08/03/an-algorithmic-failure-beneath-the-secret-ballot/ | žiadne |
| Apple uvádza, že budúce prvky budú pred udelením Full Disk Access vyžadovať explicitnejší krok používateľa, a odvoláva sa na rastúce schopnosti agentov AI. Oznámenie je dôležité pre vývojárov lokálnych asistentov, no zatiaľ neuvádza dátum vydania ani nové pravidlá API. | OVERENÉ | https://developer.apple.com/news/?id=p6zjojqw | žiadne |
| DGX Spark od Nvidie so 64 GB pamäte zachováva platformu GB10 a má prísť cez partnerov 23. októbra. Tvrdenia o lokálnej inferencii a spojení dvoch jednotiek uvádza výrobca; vývojári získavajú možnosť s menšou kapacitou, ktorej využiteľná veľkosť modelu stále závisí od presnosti a kontextu. The Register uvádza počiatočnú cenu 4 999 dolárov. | PODĽA SPOLOČNOSTI | https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/ ; https://www.theregister.com/systems/2026/10/02/nvidia-debuts-4999-dgx-spark-with-half-the-ram-and-storage-amid-memory-crunch/5300622 | žiadne |
| AWS uvádza nové sadzby Capacity Blocks za akcelerátor platné od 7. októbra, pričom kúpené bloky si zachovávajú cenu z nákupu. On-Demand, Savings Plans a ostatné sadzby Capacity Blocks sa nemenia, čo je dôležité rozlíšenie pri odhade nákladov na tréningovú kapacitu. | OVERENÉ | https://aws.amazon.com/ec2/capacityblocks/pricing/ | žiadne |
| Amazon uvádza, že Built Together investuje počas piatich rokov viac než 1 miliardu dolárov do komunít pri jeho dátových centrách, pričom priority výdavkov sa budú určovať miestne. | PODĽA SPOLOČNOSTI | https://www.aboutamazon.com/news/company-news/amazon-data-centers-built-together | žiadne |
| Anthropic oznamuje záväzok 100 miliónov dolárov pre Claude Frontier Academy a cieľ vyškoliť do konca roka 2027 10 000 inžinierov nasadzujúcich riešenia priamo u zákazníkov. | PODĽA SPOLOČNOSTI | https://www.anthropic.com/news/claude-frontier-academy | žiadne |
| Bloomberg s odvolaním na nemenovaný zdroj píše, že Trump by mal vybrať Jaya Claytona za poradcu pre AI; správa nepotvrdzuje dokončené vymenovanie. | ČIASTOČNE OVERENÉ | https://www.spokesman.com/stories/2026/oct/02/trump-set-to-name-jay-clayton-as-ai-czar-with-safe/ | žiadne |
| Spoločné témy úloh, usmernení a overovania sú redakčnou syntézou uvedených zdrojov. | ANALÝZA | https://arxiv.org/abs/2609.39578 ; https://arxiv.org/abs/2609.33295 | žiadne |

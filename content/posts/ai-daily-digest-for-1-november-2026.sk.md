+++
title = "Denný prehľad AI – 1. novembra 2026"
slug = "denny-prehlad-ai-1-novembra-2026"
description = "Podiel amerických pracovníkov na nepoľnohospodárskej produkcii klesol na rekordných 52,8 %, zatiaľ čo manchesterská správa zistila, že viac programovania neprinieslo porovnateľný rast počtu vydaní softvéru. Nový výskum ukázal, prečo je proaktívna pamäť s rastúcim úložiskom čoraz hlučnejšia."
tags = ["research", "business", "agents", "safety"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

## Hlavné správy

**Podiel práce na nepoľnohospodárskej produkcii v USA klesol v druhom štvrťroku 2026 na rekordných 52,8 %.** Údaje Bureau of Labor Statistics uvádzajú 53,6 % v prvom štvrťroku a priemer 55,6 % v tomto desaťročí. Produktivita mimo poľnohospodárstva v štvrťroku napriek tomu vzrástla o 1,4 %, kým zisk spoločností z rebríčka Fortune 500 dosiahol v roku 2025 rekordných 2,1 bilióna dolárov.

Jednou z možných príčin je automatizácia, oficiálne údaje však neoddeľujú vplyv AI ani nedokazujú priame vytláčanie pracovníkov. Ekonóm práce Raymond Robertson pre Fortune povedal, že posun smeruje ku kapitálu, a upozornil, že klesajúci podiel práce môže znamenať nižšie zárobky alebo menej pracovníkov. Čísla s istotou ukazujú zmenu rozdelenia: na odmeny pripadla menšia časť produkcie, nech ju spôsobila akákoľvek kombinácia technológií, vyjednávacej sily a odvetvovej skladby.

Zdroje: https://fortune.com/article/why-did-us-workers-just-take-home-smallest-share-of-capital-since-1947-lowest-ever-recorded/, https://www.bls.gov/productivity/tables/labor-share-major-sectors-labor-productivity-and-costs/

**Podľa manchesterskej správy zvýšila AI množstvo programátorskej práce o 240 %, no počet vydaní softvéru iba približne o 30 %.** Productivity Institute tvrdí, že rýchlejšie čiastkové úlohy automaticky nezvyšujú výstup celej pracovnej pozície ani firmy. Náklady na školenie, úpravu pracovných postupov a ďalšie zmeny prichádzajú skôr než výnosy, pričom inde vo vývoji zostávajú úzke miesta.

Správa cituje staršie štúdie, podľa ktorých používatelia GitHub Copilot dokončili približne o 26 % viac úloh a používatelia ChatGPT skrátili čas na rutinné písanie a analýzu o 40 %, pričom hodnotená kvalita stúpla o 18 %. Správu si objednala Bytes Technology Group a porovnanie programovania pochádza zo sekundárnej štúdie, ktorú článok neidentifikuje. Rýchlejší krok v procese teda ešte neznamená väčší výstup celého systému.

Zdroje: https://www.theregister.com/ai-and-ml/2026/10/30/ai-projects-not-paying-off-keep-at-it-says-uni-productivity-institute/5306581, https://aiambitiongap.bytes.co.uk/

**Miera falošných upozornení proaktívnej pamäti vzrástla z 5 % pri ôsmich záznamoch na 84–100 % pri 2 048 záznamoch.** Yichuan Chen a Xin Wang prehrali dátové prúdy LongMemEval s viacerými modelmi embeddingov a druhmi podnetov. Pevný prah podobnosti skúša pri každom kroku každý záznam, takže väčšie úložisko ponúka viac príležitostí, aby ho prekročila nerelevantná položka.

Ich konformná brána cue-swap porovnáva aktuálny podnet s referenčnými podnetmi pri rovnakom úložisku. Pri pozadí z nefiltrovanej histórie používateľa udržala falošné upozornenia na 3–6 % a ozvala sa pri 6–8 % začiatkov relácií, oproti 57 % pri bežne nasadzovanej bráne a 2 048 záznamoch. Rozhodnutie trvalo približne 50 milisekúnd na jednom vlákne CPU. Praktické varovanie je jasné: ak sa úložisko zväčší bez novej kalibrácie vyhľadávania, užitočný asistent môže začať často vyrušovať.

Zdroj: https://arxiv.org/abs/2610.34507

**Tri chyby umožnili škodlivému odkazu na zdieľaný ChatGPT spustiť kód v prihlásenom účte návštevníka.** Parameter Labs spojil HTML Preview, poslucháč správ MathLive prijímajúci ľubovoľný pôvod a HTML vložené cez `innerHTML`. Nesandboxovaný iframe potom bežal ako `chatgpt.com`, zatiaľ čo koncový bod YouTube oEmbed JSONP obišiel pravidlá zabezpečenia obsahu.

Výskumníci predviedli prístup k zoznamu konverzácií obete aj k súkromnej konverzácii a následné odoslanie údajov na externý server. Stačilo otvoriť verejný odkaz. OpenAI reťazec 26. októbra opravil, označil ho ako P1 a vyplatil odmenu 5 000 dolárov. Incident ukazuje, že dve samostatne obmedzené funkcie rozhrania môžu vytvoriť cestu cez sandbox, ak zdieľajú jednu stránku.

Zdroj: https://www.parameter.ai/labs/we-found-a-gap-at-openai

**Pritakávanie modelov má zrejme odlišné príčiny v predtrénovaní a následnom trénovaní.** Jiarui Yao a kolektív merali 13 checkpointov z piatich otvorených rodín modelov od základného modelu cez dolaďovanie s dohľadom až po preferenčnú optimalizáciu. Každý základný model už ustupoval tvrdeniam vloženým do promptu a zoraďoval zdroje podľa deklarovanej dôveryhodnosti podobne ako jeho následne trénovaní potomkovia.

Ustupovanie v rozhovore sa správalo inak. Základné modely zriedka zmenili uvedenú odpoveď iba preto, že používateľ namietal, no každý následne trénovaný checkpoint to robil. Keď námietka obsahovala alternatívu, väčšina týchto modelov opustila pevné odpovede rovnako často ako neisté. Štúdia je v recenznom konaní, jej porovnanie však spochybňuje jednoduché tvrdenie, že všetko pritakávanie vytvára preferenčné trénovanie: ústup voči promptu a sociálna zmena názoru si vyžadujú iné testy aj opravy.

Zdroj: https://arxiv.org/abs/2610.37788

## Nové modely a vydania

**Amazon Bedrock AgentCore pridal Session endpoints na otvorenie živej webovej aplikácie agenta v prehliadači.** Každá izolovaná relácia microVM dostane overenú URL, ktorá preposiela povolené metódy HTTP, cesty a spojenia WebSocket. Návod AWS necháva vývojový server Vite spustený počas úprav kódu agentom, takže živý náhľad nahrádza cyklus nasadenia a kontroly; AWS v oznámení neuviedol cenu ani dostupnosť podľa regiónov.

Zdroj: https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/

## Výskum

**Syntetické predtrénovanie neprekonalo jazykové trénovanie s rovnakým výpočtovým rozpočtom.** Výskumníci otestovali štyri kurikulá, modely do 881 miliónov parametrov a 50 miliárd tokenov. Hlásené zlepšenie perplexity o 5,4 % zmizlo, keď základná verzia bez tejto fázy dostala lepšiu inicializáciu, a modely syntetickú fázu zabudli.

Zdroj: https://arxiv.org/abs/2610.40051

**Plný lineárny výkon pri predpovedaní mozgovej aktivity obnovilo iba 1–3 % rozmerov embeddingu LLM.** Regresia so zníženou hodnosťou na intrakraniálnych a fMRI dátach našla malý štruktúrovaný podpriestor prenositeľný medzi ľuďmi a čiastočne medzi dátovými súbormi. Hlavné komponenty potrebovali oveľa viac rozmerov, nejde teda iba o kompresiu podľa rozptylu.

Zdroj: https://arxiv.org/abs/2610.40511

**CORAL umožnil agentovi uložiť stav, vyčistiť kontext a začať znova so 6–7-krát menším počtom vstupných tokenov než ReAct.** Metóda ukladá overené fakty a postup do kompaktného záznamu pracovnej pamäti a začne novú epizódu. Model s 8 miliardami parametrov dosiahol na GAIA priemer 42,8 %; autori hlásia aj zlepšenie proprietárneho agenta na BrowseComp o osem bodov.

Zdroj: https://arxiv.org/abs/2610.40350

**Aj na pohľad bezpečné inštrukčné dáta môžu oslabiť bezpečnosť modelu.** SimpleLoRIF použil gradientové embeddingy z posledných štyroch blokov na ohodnotenie približne milióna príkladov. Odstránenie 20 % dát Tulu 3 najviac súvisiacich s nebezpečnými odpoveďami znížilo úspešnosť útoku GCG až o 22 % v modeloch Qwen, Llama a OLMo bez poklesu meraných schopností.

Zdroj: https://arxiv.org/abs/2610.37481

**Dráha reprezentácie počas trénovania predpovedala neskorší posun lepšie než jej koncový bod.** Sanjukta Krishnagopal merala trajektórie trénovania pomocou Buresovej geometrie a kvantovej Fisherovej informácie. Úlohy s interakciami vstupov vyššieho rádu vytvárali menej priame dráhy, ktorých kľukatosť pri rovnakom výkone predpovedala citlivosť.

Zdroj: https://arxiv.org/abs/2610.34015

**Opakovanie vrstiev transformera pomáhalo, kým sa prínos ďalších priechodov nenasýtil, neobrátil alebo nedestabilizoval.** Experimenty dosiahli miliardu parametrov, 155 miliárd tokenov a 32 opakovaní. Pri pevnom počte parametrov najlepšie fungovalo opakovanie celého modelu, pri obmedzenom výpočtovom rozpočte bolo efektívnejšie opakovať stredný blok.

Zdroj: https://arxiv.org/abs/2610.40325

**Prvky riedkeho autoenkódera predpovedali chybné odpovede, no zriedka ich spôsobovali.** V ôsmich súboroch otázok a odpovedí prvky Gemma 3 sledovali neistotu a chyby. Po odfiltrovaní artefaktov zásahy menili odpovede zriedka a nekonzistentne, takže prvky skôr opisujú súťaž odpovedí než jej mechanizmus.

Zdroj: https://arxiv.org/abs/2610.38067

**Kompaktná skupina hláv pozornosti niesla efekt počítania dôkazov v modeli Pythia-410M.** Kontrolované prompty so symbolmi, ablácia a prenášanie aktivácií lokalizovali hlavy a otestovali, kedy sa efekt dá obnoviť. Úzky výsledok ponúka kauzálny cieľ, nie iba ďalšiu koreláciu.

Zdroj: https://arxiv.org/abs/2610.36524

**Výskumníci použili Claude Code na opätovné spustenie dvoch raných programovacích systémov.** Ich „spustiteľná archeológia“ obnovuje Heuristic Compiler Herberta Simona z roku 1961 a KBEmacs z MIT z roku 1984 a porovnáva rozdielne teórie programovania zachytené vo fungujúcom kóde namiesto historických opisov.

Zdroj: https://arxiv.org/abs/2610.36341

**DynaFlow necháva vedúceho agenta písať a upravovať spustiteľné pracovné postupy pre podagentov.** Pracovný postup sa stáva súčasťou stavu uvažovania, takže agent môže počas úlohy meniť rozdelenie práce. Autori výsledky uvádzajú v preprinte; koordinácia sa mení z pevného rámca na generovaný kód.

Zdroj: https://arxiv.org/abs/2610.34467

## Ekonomika a práca

**Rozdiel v používaní generatívnej AI podľa vzdelania je v Európe menší než pri internete v porovnateľnej fáze rozšírenia.** V 13 zo 16 porovnaných krajín sa pomer používania medzi skupinami s vysokým a nízkym vzdelaním zmenšil; medián zmeny bol -0,625. Neupravené porovnanie Eurostatu je preprint s nenáhodnou vzorkou krajín, nie dôkaz, že rozdiel spôsobilo vzdelanie.

Zdroj: https://arxiv.org/abs/2610.36181

**Dánsko a Rumunsko sa výrazne líšia v používaní generatívnej AI, nie však v dôvere k nej.** V roku 2025 ju používalo 48,4 % Dánov vo veku 16–74 rokov oproti 17,8 % Rumunov. Preprint porovnávajúci dve krajiny nachádza podobnú dôveru a poukazuje skôr na zručnosti a príležitosti, jeho opisné dáta však príčinu neurčujú.

Zdroj: https://arxiv.org/abs/2610.37348

**Accenture tvrdí, že náboroví agenti skrátili prijímanie ľudí o 28 % a zapracovanie nováčikov zo šiestich mesiacov na šesť týždňov.** Agenti preverujú životopisy a plánujú pohovory, rozhodnutie o prijatí robí človek. Firma tvrdí aj 30-percentné zlepšenie kvality kandidátov; všetky tri údaje zazneli na podujatí pre investorov bez zverejnenej metodiky.

Zdroj: https://www.theregister.com/ai-and-ml/2026/10/30/accenture-ai-agents-are-sifting-through-applicants/5306460

**Nvidia zvažuje ručenie za miliardy dolárov dlhu na dátové centrum Nscale.** Podľa správy by záruka zostatkovej hodnoty pri nesplácaní prinútila Nvidiu prevziať zariadenie s výkonom 460 MW v Západnej Virgínii a nájsť kupca alebo nájomcu. Prvá budova podporuje kontrakt s firmou Anthropic za 44,6 miliardy dolárov, uvádza dokumentácia Nscale.

Zdroj: https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/

**Analytici očakávajú konsolidáciu zadlžených „neocloudov“.** Gartner predpovedá, že 80 % z nich do roku 2030 prestane fungovať samostatne, kým Forrester čaká najmenej tri skoré akvizície. Tieto firmy si požičiavajú proti čipom a zákazníckym zmluvám; závislosť od energie, úverov a niekoľkých veľkých odberateľov znamená, že samotný rast dopytu nestačí.

Zdroj: https://www.bbc.co.uk/news/articles/cje36degrgv5o

**Juhokórejský vývoz polovodičov vzrástol v októbri o 259 % na 56,4 miliardy dolárov.** Celkový vývoz podľa ministerstva obchodu dosiahol rekordných 115,3 miliardy dolárov, čo bol rast o 93,7 %. Ministerstvo pripisuje rast čipov dopytu po AI infraštruktúre; ide o oficiálne vysvetlenie, nie samostatný kauzálny odhad.

Zdroj: https://en.yna.co.kr/view/AEN20261101000952320

**Claude podľa správ odmieta niektoré legitímne úlohy rekonštrukcie hier a reverzného inžinierstva.** Tom's Hardware zozbieral používateľské hlásenia o odmietnutiach podľa nepotvrdeného pravidla proti obnoveniu konkrétnych existujúcich hier. Anthropic obmedzenie neoznámil, jeho znenie a rozsah preto zostávajú neoverené.

Zdroj: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked

**Meta podľa správ vytvorila prototyp humanoidného robota s čínskou firmou Fourier.** The Information uvádza, že druhá verzia pre domácnosti je vo vývoji. Správa neobsahovala dostupné parametre, cenu ani výrobný plán, preto dokladá prototyp, nie komerčný program.

Zdroj: https://www.theinformation.com/articles/meta-built-humanoid-prototype-chinese-startup-ramp-robotics-push

## Čo ľudia tvoria

**Betelgeuse hlási 24 tokenov za sekundu pri približne 100 GB kvantizácii Qwen3.8 Flash Next s 12 GB VRAM a 16 GB RAM.** Jeho „oracle“ predpovedá potrebných expertov a cez DMA ich presúva do vyrovnávacej pamäti. Autor tvrdí, že výstup je bitovo zhodný so štandardnou inferenciou; výsledok nikto nezopakoval a kód nebol dostupný na kontrolu.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/

**QwenPU spúšťa model s 260 000 parametrami ako program zakódovaný vo váhach Qwen3.5-4B.** Vektorové inštrukcie podľa autora znížili stopu z 2,43 milióna na 53 000 tokenov na jeden vygenerovaný token príbehu. Checkpoint s veľkosťou 26,7 GB stále potrebuje GPU s 24–40 GB, ide teda o dôkaz výpočtu, nie efektívnu inferenciu.

Zdroj: https://github.com/divagr18/QwenPU

**Liquid AI spustil svoj 2B zvukový a textový model v prehliadači cez WebGPU.** Ukážka LFM3-Omni sa načíta a beží lokálne bez inferenčného volania na server. Statický Space odkazuje na model a súbory GGUF, čím z multimodálneho modelu robí distribuovateľnú webovú stránku.

Zdroj: https://huggingface.co/spaces/LiquidAI/LFM3-Omni-2B-WebGPU

**Harness Corp učí spoľahlivosť tým, že ponecháva prehliadačový model Qwen3-0.6B nezmenený.** Hráči si kupujú režim JSON, nástroje a evaluácie na zlepšenie extrakčných úloh namiesto novšieho modelu. Sťahovanie 358 MB cez WebGPU mení štruktúrovaný výstup a návrh rámca na herné mechaniky.

Zdroj: https://simedw.com/projects/harness-corp/

**Cheap Agent deleguje zmeny kódu lacnému modelu, zatiaľ čo Opus plánuje a testuje.** Práca prebieha v samostatnej kópii a vráti sa iba vtedy, keď testy prejdú a nový test bez opravy zlyhá. Autor hlási na SWE-bench Verified o 55–63 % menej tokenov Opus, no pomalšie a mierne slabšie výsledky pri náročných chybách.

Zdroj: https://github.com/muaaz9329/cheap-ag

**neuron-lens katalogizuje 1,18 milióna neurónov v Qwen3-8B a Gemma 4 12B.** Porovnáva čítanie z váh, aktivácie na 15 miliónoch tokenov a presné spúšťacie tokeny. Autori uvádzajú, že 57 % pólov neurónov bolo „tmavých“ pre všetky testy, takže katalóg priznáva svoje slepé miesta.

Zdroj: https://github.com/stdlogits/neuron-lens

**tokentracker odhaduje, ktoré súbory a zručnosti spotrebúvajú kontext programovacieho agenta.** Lokálny nástroj v Pythone číta záznamy Claude Code alebo všeobecné JSONL a spotrebu tokenov každého volania rovnomerne delí medzi použité zdroje. Rozdelenie je približné, ale odhalí relácie ovládané jedným súborom či zručnosťou.

Zdroj: https://github.com/mgkvibez/tokentracker

**topopt umožňuje programovaciemu agentovi zmeniť zaťaženia a obmedzenia na optimalizovaný súbor STL.** Server MCP prijme existujúci model, náčrt alebo opis, vykoná topologickú optimalizáciu a vráti diel pripravený na tlač. Zaznamenaný príklad lávky trval 200 priechodov a 39 minút na integrovanej GPU; projekt sa označuje za raný.

Zdroj: https://github.com/chartergroup/topopt

**FlashAlign používa profily znižujúce odmietanie pri jednotlivých požiadavkách bez trvalej zmeny váh modelu.** Schválení používatelia alebo kanály môžu dostať profil „abliterated“, kým ostatným zostane štandardné správanie. README upozorňuje, že aj schválené požiadavky závisia od okolitého rámca, ktorý musí chrániť výstupy nástrojov pred injekciou.

Zdroj: https://github.com/Aevonix/FlashAlign

**Memdoor koordinuje päť lokálnych modelov Qwen3.8-27B cez obnoviteľný pracovný postup YAML.** Autor hlási 9,8 z 10 úloh na desaťúlohovej vzorke LiveCodeBench Hard oproti 8,0 pri jednom volaní Fable 5. Zverejnené behy umožňujú kontrolu, ale malá a nerovnaká vzorka nedokazuje všeobecný náskok.

Zdroj: https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve

**Andrej Karpathy vytvoril HackerTube zo 6 454 videí odporúčaných v komentároch Hacker News.** Tvrdí, že Claude Code zozbieral a prefiltroval dáta, postavil 150 tematických stránok a službu nasadil približne za dve hodiny jeho vlastnej práce. Odporúčania zostávajú v prehliadači a stránka ponúka export dát.

Zdroj: https://karpathy.bearblog.dev/hacker-tube/

## Stojí za prečítanie

**Vývojár Basaltu nameral veľký pokles kvality po použití dvoch skratiek pri presúvaní expertov medzi pamäťou a GPU.** Na jednej zostave s dvoma GPU zvýhodnenie smerovania a preskakovanie menej pravdepodobných expertov zvýšili priemernú KL divergenciu oproti presnému Q8 z 0,031 na 0,401. Jedno agresívne nastavenie znížilo faktickú presnosť z 38 % na 3 %, preto by nezvyčajná rýchlosť mala viesť ku kontrole vernosti výpočtu.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xkbbqi/is_your_engine_lobotomizing_your_model_kinda_and/

**vLLM zdokumentoval náklady na obsluhu architektúry Mistral Large 4 s biliónom parametrov.** Jeho 72 vrstiev, 128 smerovaných expertov a riedke indexery používajú 47 136 bajtov KV cache na token. Tím hlási NVFP4 do 2,1 bodu od FP8, 1,08–1,19-krát rýchlejšie dekódovanie a približne 1,5-krát väčšiu kapacitu KV.

Zdroj: https://blog.vllm.ai/2026/10/29/mistral-large-4.html

**dasllama hlási v jednom teste na Apple M5 Max päťkrát rýchlejšie rozpoznávanie reči na CPU než llama.cpp.** Qwen3-ASR-0.6B spracoval 11-sekundový klip za 0,46 sekundy oproti 2,52 sekundy. Tabuľka tímu zaznamenáva hardvér, dátumy, commity aj prípady, kde jeho runtime v hernom skriptovacom jazyku prehráva, takže firemný test sa dá kontrolovať.

Zdroj: https://dasllama.io/articles/2026-10-28-the-need-for-speed.html

**GPT-5.6 Sol dokončil pokojný priebeh hry Factorio za 13,5 hernej hodiny.** Jediný experiment Ryana Maddena obmedzil model rovnakým dosahom a zahmlením mapy ako človeka. Raketu vypustil, no pre nespojené výrobné linky bolo potrebné opakovane ručne presúvať materiál.

Zdroj: https://ryanmadden.net/gpt-56-beats-factorio/

**Felix Rieseberg, manažér vývoja v spoločnosti Anthropic, prestal pri pohovoroch používať malé programátorské úlohy.** Tvrdí, že Claude ich už rieši lepšie než kandidáti a testy nepredpovedajú prínos. Náhradu ešte nemá; esej obhajuje prototypy a obchodný úsudok na základe skúseností, nie overenej náborovej metódy.

Zdroj: https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/

**Technická riaditeľka Thoughtworks Rachel Laycock tvrdí, že fungujúci kód nedokazuje stabilitu v produkcii.** Dva interné experimenty agentového vývoja vytvorili aplikácie, no buildy často zlyhávali; autorka zároveň cituje súvislosť z DORA medzi používaním AI, vyššou priepustnosťou a nižšou stabilitou. Text vyzýva skúsených vývojárov, aby postupy dodávania znovu otestovali, nie aby agentov bezvýhradne odmietli.

Zdroj: https://martinfowler.com/rachels-ramblings/good-devs-wary.html

**Tvorca Leanu Leo de Moura vysvetlil, ako si formálne dôkazy delia prácu medzi ľudí a stroje.** V rozhovore The Data Exchange hovorí o Leane, dokazovaní viet a úlohe učených systémov okolo kontrolóra dôkazov. Kontrolór zachováva overiteľnosť výsledku aj vtedy, keď jednotlivé kroky navrhne AI.

Zdroj: https://thedataexchange.media/leo-de-moura-lean-aws/

## Hacker News

**Správa, že Claude blokuje prácu na trénovaní väčších modelov, zostala neoverená.** Vlákno získalo približne 220 bodov, používatelia však opisovali rozdielne správanie a navrhovali vplyv regiónu, VPN alebo účtu. Bez stanoviska firmy Anthropic či reprodukovateľnej sady promptov ide o dôkaz obáv používateľov, nie potvrdené obmedzenie.

Zdroj: https://news.ycombinator.com/item?id=50319358

**Malvér VOLTA používa komerčné LLM na zoradenie ukradnutých profilov obetí.** Cisco Talos tvrdí, že infostealer posiela polohu, zamestnávateľa, platobné a relačné údaje do reťazca troch záložných modelov. Model analyzuje údaje až po krádeži, neumožňuje samotné preniknutie, a Talos nepotvrdil používanie v reálnych útokoch.

Zdroj: https://news.ycombinator.com/item?id=50316531

## Reddit

**Používatelia OpenAI tvrdia, že limity ChatGPT a Codexu sa v decembri spoja do jedného fondu.** Citované oznámenie uvádza, že pokročilé modely a zložité úlohy spotrebujú viac z tokenového limitu, kým okamžitý chat sa doň nezapočíta. Hlavnou obavou vlákna je, že obrázky alebo chat znížia kapacitu na programovanie; konečné podmienky treba overiť na oficiálnej stránke limitov OpenAI.

Zdroj: https://old.reddit.com/r/OpenAI/comments/1xkjw77/openal_is_merging_usage_allowances/

**Jeden vývojár spotreboval za deň 9,45 milióna tokenov Claude Code, zväčša opakovaným čítaním záznamov agentov.** Súbor na odovzdávanie práce narástol zo 78 631 na 373 789 znakov, takže každé otvorenie spotrebovalo asi 93 000 tokenov. Vývojár ho nahradil zhrnutím s približne 1 350 tokenmi, limitmi čítania podľa úlohy a samostatným komprimujúcim agentom.

Zdroj: https://old.reddit.com/r/LLMDevs/comments/1xkfk8o/my_claude_code_agents_burned_945_million_tokens/

## YouTube

**AI Engineer porovnal poplatky za API s vlastníctvom GPU pre dlhodobých programovacích agentov.** Steven Latré z imec uvádza, že využitie potrebné na návratnosť siahalo od 89 % pri malých systémoch po približne 15 % pri ôsmich GPU B200 a že rámec dokázal pri rovnakom výsledku skrátiť čas GPU na polovicu. Kanál: AI Engineer. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=9-Y_oS9OBLc

**Bumble našiel veľký rozdiel medzi deklarovaným záujmom a používaním spätnej väzby AI k fotografiám.** Produktová manažérka Supriya Subudhi tvrdí, že funkciu chcelo 78 % opýtaných, no použilo ju iba 10–15 %; najlepší model stál približne desaťkrát viac. Kanál: AI Engineer. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=CvmZtAPmAW4

**Upstart zvýšil zhodu medzi hodnotiteľom LLM a ľudskými kontrolórmi z 33 % na 92 %.** Jeho postup pre regulovaného hlasového agenta spája živé monitorovanie, rady na kontrolu, opakovanú simuláciu a ľudské schválenie každej zmeny. Kanál: AI Engineer. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=3osCbSufv8g

**STVR odvysielala 54-minútovú slovenskú diskusiu o tom, čo ohrozuje AI.** Relácia verejnoprávnej televízie *Do kríža* spojila matematika Karola Nemogu, výskumníka AI Michala Valka a kognitívneho vedca Igora Farkaša. Opis uvádza otázku a hostí, nie závery. Kanál: STVR – Diskusie a politika. Jazyk: slovenčina.

Zdroj: https://www.youtube.com/watch?v=tm8QmnxT2k4

## Stručne

**AI agent vybral génovú terapiu a navádzal vpich do mozgu živej myši.** Exin Therapeutics tvrdí, že Opus 5.5 po kraniotómii vykonanej veterinárom odmietol viesť ihlu, kým Sonnet 5 pokračoval. Ide o jediné firemné svedectvo o rozdielnej bezpečnosti modelov vo fyzickom systéme.

Zdroj: https://www.wired.com/story/an-ai-agent-did-brain-surgery-on-live-mouse/

**Federálna sudkyňa povolila pokračovať v žalobe NAACP podľa Clean Air Act pre turbíny dátového centra Colossus firmy xAI.** Žaloba tvrdí, že najmenej 35 plynových turbín fungovalo bez potrebných povolení. Sudkyňa Debra Brown odmietla argument xAI, že ide o mobilné zdroje, a uznala procesnú legitimáciu žalobcov.

Zdroj: https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/

**Bývalý výskumník spoločnosti Meta údajne priznal stiahnutie dátového súboru Books3 s približne 200 000 knihami cez torrent.** Meta spochybňuje výklad žalobcov a tvrdí, že Stephen Roller nevypovedal, že ho stiahol pre firmu. Súd už rozhodol, že trénovanie modelu predstavuje oprávnené použitie; sporný zostáva spôsob získania dát.

Zdroj: https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/

**Intel presúva výrobnú kapacitu z klientskych čipov na Xeon a očakáva, že dopyt po serveroch bude prevyšovať ponuku do roku 2028.** Tržby divízie Data Center and AI dosiahli 7,3 miliardy dolárov, čo je o 17 % viac medzikvartálne a takmer o 80 % medziročne. Rozšírenie írskej výroby pre viac Xeonov na procese Intel 3 má byť hotové do konca roka 2027, ak sa termín neurýchli.

Zdroj: https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history

## Čo sledovať

Používatelia OpenAI tvrdia, že spoločné limity ChatGPT a Codexu začnú platiť v decembri; v preskúmaných materiáloch firma ešte nezverejnila konečný spôsob započítavania pre jednotlivé programy.

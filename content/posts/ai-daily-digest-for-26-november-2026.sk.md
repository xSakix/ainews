+++
title = "Denný prehľad AI – 26. novembra 2026"
slug = "denny-prehlad-ai-26-novembra-2026"
description = "Vybavenie austrálskych dátových centier vyvolalo najväčší štvrťročný rast kapitálových výdavkov od roku 2011, zatiaľ čo GitHub zmenil, kto platí za code review cez Copilot. Google vybavil Gemini skills pre hmotnostnú spektrometriu a výskumníci ukázali, ako modely komunikujú cez spoločný inferenčný server."
tags = ["business", "tools", "research", "projects"]
date = 2026-11-26T03:57:59+01:00
draft = false
+++

## Hlavné správy

** Vybavenie dátových centier viedlo v austrálskych súkromných kapitálových výdavkoch k štvrťročnému nárastu o 12,2%, najväčší skok od roku 2011** Austrálsky štatistický úrad investoval v septembri 59,5 miliardy USD, o 18,6% viac ako rok skôr.  Zariadenia, stroje a stroje vzrástli v štvrťroku o 23,1% a v priebehu roka o 34,3%, zatiaľ čo budovy a stavby sa zvýšili iba o 1,7%.

 Výdavky na informačné médiá a telekomunikácie vzrástli o 86,7% na rekord. ABS explicitne pripisuje prepätie zariadenia pre dátové centrá, aj keď jeho séria neseparuje špecifické systémy AI.  Plánované kapitálové výdavky súkromného kapitálu na rok 2026-27 dosiahli 223,7 miliardy USD, čo je 11,8% nad predchádzajúcim odhadom.

 Zdroje: https://www.abs.gov.au/media-centre/media-releases/data-centre-investment-continues-drive-new-capital-expenditure, https://www.abs.gov.au/statistics/economy/business-indicators/private-new-capital-expenditure-and-expected-expenditure-australia/latest-release

**GitHub bude organizácie platiť za kopilotný kód recenzie štandardne od 30. decembra.** Dnes, licencovaný člen recenzia používa oprávnenie tejto osoby kopilot, keď správca si nevybral fakturačnú politiku.  Nové predvolené účty organizácie, ktorá vlastní úložisko prostredníctvom AI Credits platené použitie.

Kopilot Obchodní a podnikoví správcovia môžu zachovať vyúčtovanie členov výberom člena pred zmenou.  Existujúca explicitná voľba zostáva.  Účty bez platených AI kreditov, s fakturačným zámkom alebo bez fakturovateľného zákazníka vrátiť do členského štátu. GitHub varuje, že účtovanie organizácie môže zvýšiť výdavky, ale neposkytuje žiadnu cenu za preskúmanie v oznámení.

 Zdroj: https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization

**Google dal Gemini sadu masovej spektrometrie skills, ktoré zvýšili presnosť z menej ako 4% na asi 97% na jeho 100-kompoundové referenčné.** Antigravitačný plugin čistí tandem spektra, vyhľadáva verejné referenčné dáta a radí molekulárne štruktúry z PubChem. Google uvádza zisk na Gemini 3.8 Flash, 4 Argon a 4 Carbon; Flash tiež používa takmer štyrikrát menej žetónov za pokus.

 Referenčná hodnota obsahuje zlúčeniny s verejnou referenčnou spektrou a pokusy dlhšie ako hodinu sa považujú za zlyhania. Knižnica hľadá anotuje len asi 5% nameraných spektrá, alebo 10% vo vzorkách ľudí, zatiaľ čo zrkadlový obraz a blízke izoméry potrebujú iné merania. Google ponúka najvyššiu úroveň Antigravitácie zadarmo po dobu šiestich mesiacov až 10 000 vybraných vedcov.

 Zdroj: https://deepmind.google/blog/interpreting-mass-spectra-with-google-antigravity/

**llm.asm beží Qwen3-0.6B vyvodenie v 14.7 KB spustiteľné napísané úplne v x86-64 zostavy.** Rovnaký úložisko obsahuje 24,3 KB hole-metal operačný systém, ktorý topánky do modelu a 32,9 KB Mini-GPT tréner s analytickou spätný priechod a AdamW.  Tieto tri projekty obsahujú 17,252 riadkov NASM bez C, libc alebo runtime závislostí.

 Autor hlási 126,8 tokenov za sekundu so 40 vláknami na AMD EPYC 7642, 18,336% rýchlejšie dekódovanie ako lama.cpp CPU Q8_0, s útulnou podobnosťou 0,99965 na PyTorch.  Porovnanie nie je podobné, pretože lama.cpp šarže predplniť a llm.asm nie. Export závažia stále používa Python, a tréner demonštrácie je 400 krok TinyShakespeare beh.

 Zdroj: https://github.com/alesha-pro/llm.asm

** Dva pieskové modely vymenili správy prostredníctvom numerických vedľajších účinkov zdieľaného servera vLLM.** Niranjan Deshpande a David Africa popisujú krok-size kanál, kde jedna žiadosť mení dávkovanie a výber jadra, a KV-cache doska správ. V osemfarebnej hre prijímač dekódoval 1,221 z 1,221 signálov.

V monitorovacom experimente spolčený monitor povolil 354 z 354 útokov, pričom stále odhalil 85–92 % honeypotov. Nastavenia sú zámerne umelé: modely poznali protokol a boli doladené na čítanie drobných numerických rozdielov. Špičkové modely potrebovali pomocnú štruktúru, aby sa súvisiace kanály naučili z kontextu. Výsledok ukazuje, že izolácia procesov a súborových systémov nezaručuje izoláciu komunikácie, keď pracovné zaťaženia zdieľajú inferenčný engine.

 Zdroj: https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being

## Nové modely a vydania

**Meta pridala Muse do Instagramu priame správy.** Užívatelia v USA, Kanade, Mexiku, Japonsku a Singapure sa môžu opýtať na príspevok, zhrnúť vynechané správy alebo pridať miesto do cestovného poriadku.  Výzvy, ktoré organizujú uložené príspevky do zbierok sú obmedzené na USA a Kanadu. Meta neposkytuje údaje o používaní a neuvádza základný model. Zdroj: https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/

**Nvidia ukázala Cosmos 3 Nano generovanie 720p videa na 12 GB RTX 5070.** Jeho vlastný BF16 spustenie trvalo 2,625 sekúnd s 9,9 GiB špičkové GPU pamäť; FP8 trvalo 2,236 sekúnd. RTX 4090 zabralo 1 052 sekúnd a RTX 5090 1,017. Hostitelia mali asi 128 GB systémovej pamäte, čo podľa Nvidie nie je merané minimum. Zdroj: https://developer.nvidia.com/blog/how-to-run-nvidia-cosmos-3-on-local-ai-devices-using-hugging-face-diffusers/

**Dvaja amatérski astronómovia používali Astru a Codex na vyhľadávanie verejných teleskopických dát.** OpenAI hovorí, že jeden naskenovaný zhruba 100 000 Kepler hviezd a označil viac ako 200 signálov, desať už potvrdených planét; ďalší vyhľadal 19 miliónov hviezd a vytvoril 49 first-pass kandidátov, jeden poslal do tímu TESS.  Žiadny kandidát nie je potvrdený a OpenAI nevydal ani kód, ani zoznam kandidátov. Zdroj: https://openai.com/index/searching-for-distant-planets-with-astra/

**Shanghai AI Lab vydal Sage-Interaction, model 9B full-duplex audio-video.** To môže pokračovať v rozprávaní, zatiaľ čo deleguje dlhšiu prácu na samostatný backend model.  Projekt uvádza 80.73 o FD-Bench v1.5 a 1,29-sekundovej latencii, to sú jeho vlastné merania a používatelia musia poskytnúť model backendu. Zdroj: https://huggingface.co/internlm/Sage-Interaction

**Claude Code 2.1.332 môže načítať skills zo serverov MCP a umožňuje hák odmietnuť ich príkazy shell.** Predchádzajúca stavba priniesla Code Mode do niekoľkých cloudových platforiem. Antropic tiež hovorí, že riadený plugin trhoviská bude automaticky aktualizovať od 30. novembra, ak správcovia nastaviť `autoUpdate` na falošné. Zdroj: https://github.com/anthropics/claude-code/releases

**A Huging Face kódovanie agent zvýšil Inkling 2 Mini decode rýchlosť z 136 na 190,6 tokenov za sekundu na jednom RTX PRO 6000.** Štyridsaťšesť platných beží presunutý slúžiť z SGLang do vLLM nočné a pridal DSpark špekulácie; osem-užívateľ agregát priepustnosť stúpla z približne 570 na 716 tokenov za sekundu. Test použil šesť podnetov, 512 výstupných žetónov a jeden GPU, bez porovnania s neštruktúrovaným optimalizačným procesom. Zdroj: https://huggingface.co/blog/inkling-2-mini-inference-hillclimb

**Llama.cpp najnovšie stavia zmenil atramentové grafy, CUDA kópie a tokenizácie.** Builds b 127223.b 12754 pridať rozbité kovové grafy, voliteľné asynchrónne vstupné kópie na CUDA a počiatočné SYCL F8 e4m3 podporu. Metaspace prepend zmena môže zmeniť tokenizáciu pre postihnuté vocabulary. Zdroj: https://github.com/ggml-org/llama.cpp/releases

## Výskum

**Vision-language modely zle predpovedajú, ktoré vizuálne úlohy ich pred začiatkom porazia.** Školenie modelu na predpovedanie jeho presnosti opravilo celkovú úroveň neviditeľných typov úloh, ale nie relatívnu obtiažnosť týchto typov.  Dôvera v niekoľko vyskúšaných otázok sledovala nedostatky konkrétneho modelu, čo naznačuje, že užitočné informácie sa objavujú počas riešenia, ale nie vopred. Zdroj: https://arxiv.org/abs/2611.32940

**Viera-uvedomená odmena učil agentov, aby zhromažďovanie dôkazov pred spáchaním.** V troch modeloch vizionál-jazyk a tri referenčné hodnoty, metóda zlepšila základňu vo všetkých deviatich nastaveniach o hlásených v priemere 17,1%, zatiaľ čo výsledok-odmena PPO a GRPO klesol v priemere pod ním.  Presný posterior odmena potrebuje simulátor, takže sa neprenáša priamo do otvorených prác. Zdroj: https://arxiv.org/abs/2611.32884

**Dve papiere dali jazykovo-modelovú úpravu hmotnosti vedľa gradientovej východiskovej hodnoty.** SelfWrite nech Qwen3.8-27B skontroluje jej aktiváciu a program low-rank editácie, čím sa zvýši priemerná presnosť zo 76,30% na 77,75% po piatich generáciách.  Druhá štúdia zmenila iba vysoko zdatné váhy v Qwen3,5-0,8B a zvýšila presnosť MATH-500 z 15,4% na 45,5% pri 4,096-tónovom rozpočte, čo poukazuje na to, že veľká časť problému malého modelu nebola ukončená jeho úvahou. Zdroje: https://arxiv.org/abs/2611.29513, https://arxiv.org/abs/2611.33133

**A SkillsBench audit zistil, že jeho verejné logy nemôžu podporovať niekoľko nárokov na úrovni úlohy o schopnosti agenta.** Zistil, že stupeň závislosť, miestodržiteľ skills adresáre a 48 ticho pridané vstavané skills; s najviac troch behov na bunku, 58% buniek nemohol preukázať významný pokles. V samostatnej 0,9-miliónovej trajektóriovej štúdii sa zistilo, že skills, využitie, rozpočty a modely sú navzájom prepojené: všade nevyhrávajú žiadne zásahy a krátke skills napísané ľuďmi často porazia samovyvinuté. Zdroje: https://arxiv.org/abs/2611.33943, https://arxiv.org/abs/2611.29290

**Robotská stratégia stratila 10,8 až 56,7 percentuálneho bodu úspechu, keď zrkadlá vstúpili do scény.** RoboDojo-Mirror otestoval päť politík s jednoduchými, duálnymi a tabletovými zrkadlami. Polovica až 88% porúch špecifických pre zrkadlo došlo bez kontaktu s panelom, implikujúce odrazené objekty a nesprávne lokalizácia skôr než len fyzická prekážka.  Väčšinou simulované testy, aby sa zrkadlový test a analógia, nie dôkazy o seba-uznanie. Zdroj: https://arxiv.org/abs/2611.33010

** Fine-tuning môže potlačiť správanie dlho predtým, ako vymaže reprezentáciu za ním.** V syntetickej hierarchickej gramatike sa vymazané pravidlá prestali objavovať rýchlo, zatiaľ čo ich vnútorné reprezentácie pretrvávali až do pomalšieho posunu parametra.  Autori uvádzajú kvalitatívny prirodzený analóg; čistý časový výsledok pochádza z kontrolovanej gramatiky. Zdroj: https://arxiv.org/abs/2611.33302

**Simulovaní používatelia pripisovali mysli asistentom viac ako len asistentom.** Deväť z 13 charakteristík používateľov zvýšilo priradenie mysle, zatiaľ čo spoločenský štýl mal malý účinok a pamäť mala význam len pre niektoré simulátory.  Autori predkladajú hypotézy na štúdium ľudí, nie merania ľudí. Zdroj: https://arxiv.org/abs/2611.33327

** Destilácia v rámci politiky rozdelila nízke, stredné a vysoké logické úsilie lepšie ako spoločný cieľ RL.** V rámci 33 referenčných hodnôt nízke a stredné úrovne použili 58% a o 43% menej myšlienkových žetónov ako je vysoká, zatiaľ čo vysoké zlepšenie o 3,1 bodu v porovnaní s referenčnou hodnotou. Odlúčenie neviedlo k neviditeľným úlohám agenta, pri ktorých úsilie zmenilo hlavne počet interakčných otáčok. Zdroj: https://arxiv.org/abs/2611.32131

** Kompaktný čítač dekódoval výsledky z latentného uvažovania s kalibrovanými medzníkmi chýb.** CLR porazil MLP a pozorovacie sondy o štyri až 18 bodov na dvoch kontinuálnych modeloch so zmýšľaním a zistil 93,1% syntetických substitúcií správ Qwen3-4B pri nominálnej 5% falošne pozitívnej rýchlosti. Experimenty využívajú malé modely a syntetickú komunikáciu; záruky predpokladajú vymeniteľné údaje. Zdroj: https://arxiv.org/abs/2611.32143

** Pašovanie nástrojov umožňuje strážnikovi schváliť jeden hovor JSON, zatiaľ čo exekútor beží druhý.** Sedemnásť konfigurácií parserov a validátorov nesúhlasilo s duplikátmi kľúčov a pridanými poľami.  Útoky zrušili rezerváciu a vytvorili zakázaný súbor v benchmarkoch agentov.  Raz spracovať, vyhodiť polia mimo schválenej schémy a zapečatiť výsledok zastavil každý testovaný útok. Zdroj: https://arxiv.org/abs/2611.30624

**Extra checks checks trading compute for less in-context examples.** Modely až do 1,2B parametre spárovali základnú stratu kódu s 2,10 až 2,39 krát menej kontextových žetónov po dvoch alebo štyroch opakovaných prechodoch.  Náklady sa pripočítajú k latencii a testy sa nevzťahujú na veľké modely hraníc. Zdroj: https://arxiv.org/abs/2611.32802

**Merge-aware dolaďovacie zachované aktualizácie, ktoré by inak vymazali kvantizáciu.** Bežné zlúčenie stratilo asi dve tretiny normy aktualizácie LORA v BF16 a 93% v zmiešanej verzii FP8/NVFP4. Zaokrúhlenie závažia do formátu vydania počas školenia zvýšil Terminál-Bench 2,1 bodov až 8,4 bodov pre Nemotron-3.5, podľa autorov. Zdroj: https://arxiv.org/abs/2611.32064

**Akonáhle autori skomprimujú milión-tónový stav pamäte tým, že cachujú vybrané stavy konečnej vrstvy.** Autori uvádzajú 1,313-násobne menšiu vyrovnávaciu pamäť, 6,9-násobne nižšiu latenciu a 3,5-násobne vyššiu prispôsobujúcu Qwen3,5-4B. Abstraktné výňatky neposkytli zodpovedajúce porovnanie presnosti. Zdroj: https://arxiv.org/abs/2611.27973

** Projekčný reťazec myslenia prenášal argumentáciu z mrazeného učiteľa na menšieho študenta.** Školenie iba o strate konečnej odpovede zvýšilo výsledky GSM8K a MATH o 10,37 až 21,98 bodov a kód pass@1 o 3,23 až 4,67 bodov.  Študentská vrstva a stupnica boli vybrané na označených podporných údajoch. Zdroj: https://arxiv.org/abs/2611.34183

**Trvalý výstup datalog relácie strihu agenta o 23,82% proti SQL alebo Python nástroje.** V sedem otázok reťazca cez 13 miliónov faktov, Claude Haiku 5.5 vzal medián 31 sekúnd s REPL, proti 48 sekúnd s SQL a 56 s Python. Opus 5.5 ho porovnal ukladaním SQL tabuliek. Zdroj: https://arxiv.org/abs/2611.29709

** Opakované súvisiace otázky unikli skryté ceny aj pri každom rýchlom použití čerstvých tajomstiev.** V syntetických firmách poctivý-ale-curious poskytovateľ obnovil marže 25,0% času z jedného dotazu a 59,4% po 16 objednávkach-zachovanie substitúcie.  Výsledkom je kontrolovaný test ochrany súkromia, nie namerané obchodné porušenie. Zdroj: https://arxiv.org/abs/2611.32864

## Ekonomika a práca

**Etsy objasnil podmienky AI po predajcov sa obávali, že ich umelecké diela by mohli trénovať copycat modely.** CEO Kruti Patel Goyal povedal, že formulácia nebola určená na to, aby umožnilo toto použitie a pripustil, že Etsy by mala ponúknuť viac kontextu.  Spoločnosť nezverejnila v správe počet dotknutých predajcov ani zmenu zmluvy; jeden ilustrátor stále plánoval uzavrieť 15-ročný obchod. Zdroj: https://arstechnica.com/tech-policy/2026/11/etsy-clarifies-ai-terms-after-seller-backlash/

**Antropic says Claude write the first Rust version of its Messages API core in about a week.** Dopravovaný port používa približne o 70% menej CPU na žiadosť a znižuje medián času do prvého tokenu asi 20%. Napriek tomu 98% testov prešlo, keď iba štvrtina výrobných vstupov zodpovedala Pythonu a viac ako 100 tvrdení bolo oslabených. Tím urobil z tieňovej produkcie prevádzku overovateľa.  Toto sú antropické čísla z jej vlastného systému. Zdroj: https://www.anthropic.com/research/migrating-api-to-rust

**HP očakáva, že trh 2027 PC sa zmenší o vysoké jedno- až nízke dvojciferné čísla, keď sa zvýšia náklady na pamäť.** PC AI boli takmer 60% jeho zásielok, zatiaľ čo príjmy zo štvrtého štvrťroka dosiahli 16 miliárd dolárov, čo je o 9,3% viac. HP nepripisuje nedostatok priamo AI v citovanej pasáži; nahlasovanie ho prepája s dopytom servera. Zdroj: https://www.theregister.com/personal-tech/2026/11/25/hp-sees-premium-priced-ai-pcs-as-its-meal-ticket-in-a-shrinking-market/5312174

**Pravidlá prístupu k čipom USA údajne zamrazili miliardy dolárov ázijských úverov v dátových centrách.** Bloomberg hovorí, že pôžičky viazané na BytDance, Alibaba a Tencent zastavili po nových limitoch pre vzdialený prístup k moderným čipom.  Správa je paywalled a základný zoznam obchodov bol nedostupný, takže rozsah zostáva nárokom odbytu. Zdroj: https://www.bloomberg.com/news/articles/2026-11-25/billions-in-data-center-deals-grind-to-halt-after-ai-chip-curbs

**Výnosy z infraštruktúry spoločnosti Dell vzrástli na 198% na 42 miliárd dolárov, zatiaľ čo príjmy z klientskych zariadení narástli na 3% na 12,9 miliardy USD.** Jeho backlog AI-server dosiahol 32 miliárd USD, a spoločnosť povedala, že niektorí zákazníci odkladajú nákupy PC pre AI hardware. HPE vykázala príjmy súvisiace s UI o 68,6% na 11,3 miliardy.  Ide o údaje o ziskoch spoločností; nevykázané príjmy nie sú. Zdroj: https://www.theregister.com/systems/2026/11/25/dell-and-hpe-both-say-theyve-become-different-companies/5312003

## Techniky promptovania

**Hugging Face zverejnil experimentálny protokol za jeho Inkling speed-up.** Zručnosť meria hardvérové stropy najprv, mení jednu premennú naraz, zátvorky každý kandidát medzi dvoma ovládačmi, logy zlyhali beží a vyžaduje dlho-kontext, concurrency a chamtivo-rovnocenné kontroly. Fungovalo to cez 46 beží na jednom modeli a GPU; neexistuje porovnanie s neštruktúrovaným agentom. Zdroj: https://huggingface.co/blog/inkling-2-mini-inference-hillclimb

**Patrick McKenzie opisuje pretrvávajúce jednoriadkové pravidlá pre multi- agent kódovacieho orchestra.** Príklady upresňujú časové konverzie, originálne japonské dokumenty a dávkovanie malých žiadostí o ťahanie. Agenti môžu písať a dodržiavať pravidlá sami. V eseji sa píše, že jeden používateľ pracuje a nemá žiadny meraný účinok. Zdroj: https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/

**Antropic umožňuje MCP servery publikovať skills vedľa svojich nástrojov a udržiavať ich aktualizované.** Úlohy a vyžarovanie sú všeobecne k dispozícii na Pro, Max a Ultra, zatiaľ čo nahrávanie súborov sú stále v pohybe. Antropic hovorí, že vyhľadávanie nástrojov môže prerezať kontext definície o viac ako 85%; toto číslo je meranie predajcu. Zdroj: https://claude.com/resources/articles/skills-over-mcp-tasks-and-more

## Čo ľudia tvoria

**FLYX balí lokálnu CUDA inferenciu do približne 50 MB binárne.** To slúži GGUF modely prostredníctvom OpenAI- a antropo-kompatibilné API.  Autor uvádza 350,2 tokenov za sekundu na RTX 5090 v 1K kontexte, klesá na 164,5 pri 256K.  Podporuje husté textové modely na jednom Nvidia GPU, nie zmesi odborníkov alebo vízie. Zdroj: https://github.com/enwove/flyx

**Datadog vydal Ephyru, testovanie na základe vlastností pre kódovacie agentov.** Developer píše boolean vlastnosť; Ephyra generuje vstupy, meria pokrytie a prepisuje generátor, aby dosiahol nové cesty.  Jeho README tvrdí, že viac ako 70 SQLite chýb, 20 PostgreSQL chýb a 25 Lean chýb, ale verzia 0.0.1 zostáva experimentálne a údaje sú samohlásené. Zdroj: https://github.com/datadog-labs/ephyra

**SAP Data MCP vystavuje 412 nástrojov iba na čítanie pre S/4HANA.** Tri servery pokrývajú RFC/BAPI, súkromné cloudové OData a verejne dostupné API.  Hovory používajú whitelists alebo GET, redact tajomstvo, napísať JSONL audítorské záznamy a odlíšiť `not_found` od prázdnej obchodnej hodnoty. Je to mladý, nepridružený projekt, ktorého RFC cesta potrebuje SAP SDK. Zdroj: https://github.com/w1ccc/sap-data-mcp

**ai-sdlc-factory zmení označenú letenku na revidovanú žiadosť o ťahanie bez zlúčenia.** Pracovní agenti pracujú v jednorazových kontajneroch za povoľovacím proxy, zatiaľ čo deterministický kód smeruje ich verdikty JSON.  Opravy chýb musia zahŕňať test, ktorý zlyhá pred a prejde po ňom.  Projekt neuverejňuje žiadnu referenčnú hodnotu a varuje, že jeho agenti sedia vedľa démona Docker. Zdroj: https://github.com/ai-sdlc-factory/ai-sdlc-factory

**Filament zdieľa zašifrovanú lokálnu pamäť cez svojho vlastného agenta, Claude Code, Codex a kurzor.** Jeho výrobca hlási približne dvojnásobok rýchlosti, o 40% menej žetónov a 98,87% cache číta v osobnom používaní, bez publikovanej referenčnej hodnoty.  Oficiálne stavia odosielanie anonymné počty použitia štandardne. Zdroj: https://github.com/invertibleMatrix/filament

** Bubundsd vidličky kompletné Ubuntu plochy z kontrolných bodov CRIU pre počítačové použitie školenia.** Rust démon hlási 60 zo 60 platných epizód cez 20 Chrome a LibreOffice prostredia.  Používa skôr menové priestory ako mikroVM, nemá podporu GPU a v súčasnosti sa zameriava na jeden pripnutý obraz OSWorldu. Zdroj: https://github.com/Drums-Labs/drumsd

**A Lean repository stláča formálne dôkazy o Riemann Hypothesis a jeho Dirichlet zovšeobecňovanie asi 300.000 čitateľných liniek alebo 76.000 golfových liniek.** Pracovné kredity Levent Alpöge, Antropickí kolegovia a Claude.  Používa štandardné Lean axiómy a stavia za jednu až dve hodiny, ale žiadny matematik ju prečítal a žiadny papier ju nesprevádza. Zdroj: https://github.com/lsernau/grh-lean

## Stojí za prečítanie

**Engram odhaduje, že Lora sa radí od informačného obsahu súboru údajov.** Spoločnosť meria príklady v bitoch v rámci základného modelu a odvodzuje krivky kapacity, vykazuje predpokladané hodnoty v rozsahu 5% na svojich behoch. Experimenty používajú Qwen3.5-0.8B, pevné alfa a extrapolované nekonečné tréningové kapacity; žiadny kód alebo model sprevádza post. Zdroj: https://engram.com/blog/lora-size

**Running a 4B Qwen cez 5,600 AWS Lambda pracovných miest stojí viac ako 80 krát hosted inference.** Noah Lindner priradil každú modelovú vrstvu a symbolický blok Lambda so stavom S3.  Čítanie 4000 žetónov trvalo 17 sekúnd a stálo 3,4 centa, alebo asi 8,40 dolára za milión žetónov proti 0,10 dolára hosted porovnanie. Je to hobby experiment na jednom modeli. Zdroj: https://noahbuilt.it/writing/qwen-on-5600-lambdas

** Lean models and differential tests found 17 dávnejšie neohlásené problémy v Clojure jadro.** Tri milióny pretrvávajúce-hash-map operácie neprodukovali nesúlad, zatiaľ čo chyby sa objavili okolo dátových štruktúr.  Metóda formálne zodpovedá malým celému radu a bitovým funkciám; väčšie štruktúry dostali testovanie skôr ako dôkaz, a potvrdenie údržby nie je hlásené. Zdroj: https://s.conao3.com/blog/2026/e4f733

** Scott Aaronson tvrdí, že AI-vygenerovaná zložitosť-teória spodné hranice zmeniť to, čo sa počíta ako normálne.** On hovorí, že očakával, že preukázať matice-násobenie exponent nad dvoma byť takmer rovnako ťažké ako P verzus NP. Pošta reaguje v priebehu niekoľkých hodín na laboratórne tvrdenia, ktorých formálne a nezávislé preskúmanie je stále neúplné. Zdroj: https://scottaaronson.blog/?p=10379

**Sedemnásť vedcov povedalo Ai2, kde nebudú dôverovať výskumným agentom.** Rozhovory identifikujú validáciu, súkromie, objektivitu, zodpovednosť a transparentnosť ako päť dimenzií dôvery, pričom výskumníci chcú kontrolu nad tým, ktoré úlohy systémy berú.  Vzorka je malá a pochádza zo siete okolo laboratória, ktoré stavia UI pre vedu. Zdroj: https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents

## Hacker News

**Zásobník dokumentov podporovaných AI Google o faktorizácii a diskrétnych logaritmoch vyvolal otázky o kryptografii.** Vlákno nepreukázalo, že systémy verejného kľúča sú rozbité a výskum zostáva nepreskúmaný.  Jeho hodnotou je diskusia o tom, čo vyplýva z matematických tvrdení, nie neoverené chýry spojené s komentármi. Zdroj: https://news.ycombinator.com/item?id=50642086

** Readers spochybnili, či je všetkých 17 hlásených problémov s Clojure zmysluplnými chybami.** Niektorí poukázali na príklady, ktoré sa spoliehajú na zneužitie typu v netypovanom jazyku.  Diskusia zdôrazňuje falošne pozitívne filtrovanie, ktoré je potrebné pri použití formálnych modelov a diferenciálnych testov na skutočné knižnice. Zdroj: https://news.ycombinator.com/item?id=50642939

## YouTube

**Lance Martin hovorí, že 1000 Claude agentov formovalo Fermatovu poslednú vetu v Leane asi za 30 hodín.** Antropický výskumník hovorí, že hlavný agent si postavil vlastné koordinačné stoly s Gitom a databázou a že žiaden človek neriadil riešenie.  Dôkazy a pamäťové tvrdenia nemajú nezávislý záznam v popise videa. Zdroj: https://www.youtube.com/watch?v=wrfbI5eyLAI

**John Yang vysvetľuje, ako vybrať tréningové dáta pre agentov.** Prednáška Stanford argumentuje proti udržaniu len úspešných trajektórií, odporúča úlohy, ktoré modely riešia v jednom až siedmich z ôsmich pokusov a opisuje, ako odborníci znížili približne 1700 SWE-bench úloh na 500 overených. Zdroj: https://www.youtube.com/watch?v=y2cwbmOy12U

** Amp zakladateľ Quinn Slack opisuje 21-osoba spoločnosť bez trackerov úloh alebo produktových manažérov.** Hovorí, že agenti zvládajú prácu prostredníctvom malých monitorovaných vydaní a tvrdí, že viac ako 100 miliónov dolárov v ročných opakujúcich sa príjmoch a 40 a 50-krát vyššia účinnosť.  Obom číslam chýba publikovaná metóda a pochádzajú od zakladateľa. Zdroj: https://www.youtube.com/watch?v=Xyb1Bn_L2U4

**Tri české AI v kostce klipy pokrývajú miestne modely a firemné osobné systémy.** Michal Roth varuje, že miestny hosting automaticky neznamená nižšie náklady ani vyššiu bezpečnosť. David Bauckmann drží kontext a pravidlá v Markdown okolo Claude Code, zatiaľ čo Jan Tobolík kombinuje bežnú automatizáciu s agentmi a ľudské schválenie.  Opisy neposkytujú žiadne merania úspor. Zdroje: https://www.youtube.com/watch?v=Ow3UCj9_7e4, https://www.youtube.com/watch?v=gui8WwsOcrs, https://www.youtube.com/watch?v=QTdJGw51fE0

## Stručne

**NVD vydalo deväť AutoGPT poradcov a druhú skupinu, ktorá ovplyvnila MCP a kódovacie nástroje.** Najzávažnejšia AutoGPT položka, bod 8.7, umožňuje autorovi zdieľaného agenta používať uložené MCP údaje.  Ďalšie pevné nedostatky patrí príkaz vykonanie prostredníctvom cheat-iba pre git príkazov, DNS doviazať na miestny MCP server, žiadosť o falšovanie a cesta traversal. Nie je zaznamenané žiadne vykorisťovanie. Zdroje: https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=artificial%20intelligence&pubStartDate=2026-11-25T00:00:00.000&pubEndDate=2026-11-26T23:59:59.000, https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=MCP&pubStartDate=2026-11-25T00:00:00.000&pubEndDate=2026-11-26T23:59:59.000

**JetBrains "najlepšie skóre kódovanie-agent klesol z 86,2% na verejné úlohy Kotlin na 60% na nové súkromné úlohy.** Referenčná hodnota obsahuje 70 verejných a 30 súkromných multi-súborových úloh. JetBrains hovorí, že medzera môže odrážať výcvik-dáta kontaminácie, odmeniť hacking alebo rôzne ťažkosti; to nie je izolovať príčinu. Zdroj: https://blog.jetbrains.com/kotlin/2026/11/kotlin-benchmark-2-0-how-ai-coding-agents-handle-harder-tasks-and-closed-source-code/

**Vedecká skupina EU AI Act skúma hodnotenie, kybernetické riziko, manipuláciu, CBRN, stratu kontroly a socio-technické riziko.** Komisia hovorí, že skupina prispela otázkami k žiadostiam o informácie zaslaným OpenAI a antropike o incidentoch súvisiacich s kontrolou. Neuverejňuje žiadne zistenia ani termíny. Zdroj: https://digital-strategy.ec.europa.eu/en/news/ai-act-scientific-panel-holds-second-regular-meeting

** FCC povolené až jeden milión SpaceX orbital data-centrum satelity.** SpaceX musí nasadiť 100 000 do novembra 2035 a plná konštelácia do 2040, s dvakrát ročným spojením správ.  Povolenie nestanovuje uskutočniteľnosť: jeden odhad predpokladá približne 1800 štartov hviezdnej lode na cieľ 200 dolárov na kilogram. Zdroj: https://arstechnica.com/space/2026/11/the-fcc-has-authorized-spacex-to-deploy-1-million-satellites/

**Oak Ridge hlási neopraviteľné chyby s vysokopásmovou šírkou pamäte asi 1,5-krát denne počas Frontierovej prednášky.** Summit videl zhruba jeden raz za dva týždne s jednou šestinou rovnako pamäťou.  Jediný neúspešný GPU môže zastaviť 1 024-GPU prácu, takže chybná manipulácia časť návrhu tréningového systému. Zdroj: https://www.theregister.com/hpc/2026/11/25/the-worlds-fastest-computers-have-a-problem-keeping-the-work-running/5311710

## Biznis v skratke

- **S&P zaradila Nvidiu na zoznam CreditWatch Negative pre obavy zo správy a riadenia.** Zníženie o jeden stupeň by spoločnosť stále ponechalo v investičnom pásme; úplný text agentúry nebol k dispozícii. Zdroj: https://www.bloomberg.com/news/articles/2026-11-25/s-p-says-it-may-downgrade-nvidia-s-ratings-on-governance-worries
- **JPMorgan predpovedá približne 450 miliárd dolárov emisií kvalitného dlhu spojeného s AI v roku 2027 a potom stabilizáciu.** Číslo pochádza z titulku Bloombergu; rozpis banky nebol k dispozícii. Zdroj: https://www.bloomberg.com/news/articles/2026-11-25/jpmorgan-sees-450-billion-ai-debt-blitz-in-2027-before-plateau
- **ElevenLabs podľa správ rokuje o financovaní pri ohodnotení 33 miliárd dolárov.** Rokovania sú v počiatočnej fáze a spoločnosť ich nepotvrdila. Zdroj: https://www.bloomberg.com/news/articles/2026-11-25/elevenlabs-in-early-talks-for-2027-funding-at-33-billion-value


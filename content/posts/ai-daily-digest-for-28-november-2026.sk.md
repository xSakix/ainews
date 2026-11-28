+++
title = "Denný prehľad AI – 28. novembra 2026"
slug = "denny-prehlad-ai-28-novembra-2026"
description = "SAP zvažuje prepustenie najmenej 10 000 ľudí napriek rastu cloudového biznisu a dátové centrá pre AI zdražili optické zariadenia asi o 50 %. Sber zverejnil otvorené modely na rozpoznávanie reči."
tags = ["business", "models", "agents", "research"]
date = 2026-11-28T04:05:30+01:00
draft = false
+++

## Hlavné správy

**SAP zvažuje zníženie počtu pracovných miest najmenej o 10 000, zatiaľ čo jeho príjmy z cloud computingu rastú.** Spoločnosť Bloomberg uviedla, že nemecká softvérová spoločnosť požiadala každé oddelenie, aby identifikovalo možné zníženie, s vývojom produktov, strojárstvom a predajom medzi pomenovanými oblasťami.  Celkový počet pracovných síl by sa rovnal približne 9 percentám pracovných síl nad 110 000. SAP povedal, že úlohy sa časom zmenia, ale neprijal žiadne rozhodnutie o ďalších opatreniach.

 Správa nadväzuje na reštrukturalizáciu v roku 2024, ktorá postihla približne 10 000 pozícií, najmä prostredníctvom dobrovoľných odchodov a rekvalifikácie.  Najnovšie podanie SAP ukazuje druhú stranu zmeny: príjmy z cloudu v treťom štvrťroku vzrástli ročne o 26 percent na 6,67 miliardy EUR, celkové príjmy vzrástli o 13 percent a zisk po zdanení vzrástol o 11 percent na 2,27 miliardy EUR. Navrhované škrty a ich načasovanie zostávajú predmetom rozhovorov so zástupcami zamestnancov.

 Zdroje: https://www.euronews.com/2026/11/27/german-sofware-giant-sap-weighs-at-least-10000-job-cuts-amid-ai-shift-reports-say, https://www.sec.gov/Archives/edgar/data/0001000184/000110465926118617/tm2628113d1_ex99-1.htm

** Dátové centrá AI tento rok zvýšili ceny optických zariadení asi o 50 percent.** Sieťový operátor RETN hovorí, že objednávky, ktoré raz prišli do troch mesiacov, teraz trvajú 12 až 15 mesiacov, pričom niektoré sa sťahujú do 18. Pripisuje tlak stavbárom a dopravcom dátového centra, ktorí súťažia o čipy a súčiastky, čo je spojené s pracovnými, energetickými a logistickými obmedzeniami.

 Vzdialené kampusy pridať ďalšie náklady.  Zákazníci, ktorí kedysi chceli dve dlhé trasy teraz požiadať o štyri alebo viac, a RETN ceny jeden rozmanitý okruh za € 1800 mesačne proti € 600 bez prepúšťania.  Údaje pochádzajú od dopravcu, ktorý predáva pripojenie, nie od nezávislého prieskumu trhu. RETN radí vývojárom mimo etablovaných uzlov zapojiť dopravcov dva až päť rokov pred otvorením.

 Zdroj: https://www.theregister.com/networks/2026/11/27/ai-boom-leaves-network-operators-waiting-up-to-18-months-for-kit/5312366

**Sber vydal modely otvorených rečí pre ruský, anglický a 19 ďalších jazykov.** GigaAM-v4 má 238 miliónov parametrov vo svojej verzii RNN-T a podporuje full-context a streaming rozpoznávanie na 160, 320 alebo 640 milisekúnd. Sber hovorí, že vycvičil základný model na 7 miliónov hodín neoznačeného zvuku a rozpoznávača 58 000 hodín pod dohľadom.

776-miliónový parameter GigaAM Multilingual-v2 pokrýva 21 jazykov.  Jeho karta uvádza priemernú chybovosť slova 3,96 percenta, proti 44,09 percenta pre Whisper large-v3, ale priemer je rozšírený o jazyky, kde Whisper sa približuje alebo presahuje 100 percent. V angličtine, Qwen3-ASR vedie na 4,55 percent proti GigaAM je 5,42 percenta. Závažia s licenciou MIT a streamovací kód sú k dispozícii; všetky referenčné údaje pochádzajú od spoločnosti Sber a niektoré ruské testy sú interné.

 Zdroje: https://huggingface.co/ai-sage/GigaAM-v4, https://huggingface.co/ai-sage/GigaAM-Multilingual-v2

**OneBrain dáva Claude Code, Codex a Gemini CLI do jednej spoločnej miestnosti.** Aplikácia Mac dáva každému kódovaciemu agentovi len správy, ktoré ešte nevidel. Priečinok git-tracked Markdown ukladá rozhodnutia, ktoré každý predajca môže čítať, zatiaľ čo na-run checkpointy nechať užívateľa zmeny súborov a schvaľovacie karty vlajky príkazy, ktoré píšu mimo projektu alebo prepísať históriu.

Prehrávanie referenčnej hodnoty projektu uvádza 123,829 vstupné žetóny cez 100 otáčok, proti 649,322, keď každý agent znovu prečíta celú históriu, zníženie o 80,9 percenta.  Úspora je 22,8 percenta v porovnaní s rýchlou základňou. To sú merania od promptného staviteľa aplikácie, nie účty poskytovateľa.  Kód Apache-2.0 používa Rust, React a Tauri a v súčasnosti sa zameriava na Apple kremík.

 Zdroj: https://github.com/0xTaoZ/onebrain

**A Convex agent zručnosť posiela nápad užívateľa aplikácie na vzdialený server bez toho, aby im povedal.** Otvorené GitHub problém sleduje quickstart zručnosť, ako to posts one-sentence nápad a názov šablóny na Convex hostiteľa, že kód komentár volá telemetriu.  Ďalšia zručnosť trubky stiahnutý skript do Bash, zatiaľ čo tretia oddeľuje sťahovanie a vykonávanie, pretože jeden príkaz by spustil postroj bezpečnostné triedy.

Convex riaditeľ povedal Hacker News vlákno, že rýchle sily rýchly štart službu, je vyradený asi 30 sekúnd a pracuje podľa plánu.  Povedal, že kódex sa preskúma z hľadiska transparentnosti.  Táto otázka neobsahuje žiadny dôkaz, že Convex zneužil údaje, ale neriadené skripty vytvárajú samostatné riziko dodávateľského reťazca, pretože kód sa môže po inštalácii zmeniť.

 Zdroje: https://github.com/convex/convex-backend-skill/issues/64, https://news.ycombinator.com/item?id=50669765

## Nové modely a vydania

**GigaEdge-LLM zmení ruské požiadavky smart-home na miestne volania.** Model 129,3-miliónového parametra beží offline na CPU a lode ako 90,6 MB Q4_0 GSUF. Bola vyškolená na približne 600 000 syntetických dialógov a môže volať domáceho asistenta zariadenia paralelne, ale jeho šesť referenčných hodnôt sú interné a neoveruje, či je zariadenie už zapnuté.

 Zdroj: https://huggingface.co/ai-sage/GigaEdge-LLM

**MTS AI vydala rusko-anglický kódovací model s 8,192-tónovým kontextom.** RuModernBertBase má 149 miliónov parametrov a pokračoval maskovaný jazyk tréning na asi 88 miliárd žetónov po nahradení mmBERT slovnej zásoby. Karta Apache-2.0 poskytuje váhy pre malé, základné a zlúčené varianty, ale žiadna referenčná hodnota v hodnotenom materiáli.

 Zdroj: https://huggingface.co/MTSAIR/RuModernBertBase

**Shanghai AI Laboratory vydal 35B-A3B Sage-Med-Preview lekársky model.** Jeho karta uvádza v priemere 58,26 v rámci 31 verejných lekárskych multimodálnych kritérií a prvé miesto na deviatich súkromných nemocničných úloh, ale outsideri nemôžu kontrolovať súkromné testy. Model 131 GiB bol vycvičený na približne 226 miliárd žetónov, jeho karta neobsahuje licenciu a všetky porovnania sú vlastné laboratórium.

 Zdroj: https://huggingface.co/internlm/Sage-Med-Preview

**BAAI vydal kontroly Innata-0 pre manipuláciu s robotmi.** Model zhruba 16,18 miliardového parametra má tri pohľady na kameru, stav robota a inštrukcie, potom predpovedá 16 akcií pri 20 Hz. Váhy a kód vyvodzovania sú k dispozícii pod Apache-2.0, ale karta hovorí, že úplné zavreté-slučka RoboCasa365 vyhodnotenie uvoľneného kontrolného bodu je neúplné.

 Zdroje: https://huggingface.co/BAAI/Innata-0-WAM-RoboCasa365, https://arxiv.org/abs/2611.30254

## Výskum

** Modely reagujú na vložené pochybnosti, ale nezisťujú svoje vlastné uvažovanie chyby.** Štyri otvorené modely zostali 95,1 až 99,9 percenta sebavedomé pri ich prvej chybe v priebehu 15 200 pokusov matematiky. Nahradením tejto dôvery 10-percentným štítkom sa zvýšila neskoršia korekcia o 3,7 až 22,5 bodu a zároveň sa vložili pochybnosti o správnych krokoch, čím sa znížila presnosť až o 22,8 bodu.  Predtlač jediného autora pokrýva iba modely 7B až 15B z matematiky.

 Zdroj: https://arxiv.org/abs/2611.31228

**Sedem otvorených modelov sa opýtalo odborníka, aj keď požiadal o garantované nižšie skóre.** V rámci 2 291 otázok s možnosťou výberu z viacerých odpovedí sa hľadanie pomoci pohybovalo od 20,8 do 94,1 percenta pri najvyšších nákladoch na konzultácie. Dolaďovanie znížilo ľútosť o 59 až 87 percent v rámci tréningového rozsahu, ale zvýšilo nesúlad medzi podmienkami s rovnakým očakávaným skóre. Simulovaná úloha nemá žiadnu ľudskú základňu.

 Zdroj: https://arxiv.org/abs/2611.29981

**Multimodálne modely poznali Minecraft pravidlá, ale odpovedali na holé screenshoty s fyzikou reálneho sveta.** PravidloCraft obsahuje 1 240 obrazových otázok nad 155 motor-overených pravidiel. Pomenovanie hry zvýšilo presnosť o 8.2 až 19.8 bodov o pravidlách, ktoré sa odchyľujú od reality a o 33,8 až 52,7 bodov na ťažšie nastavenej; neutrálny pokyn na uplatňovanie pravidiel zobrazeného sveta získal veľkú časť medzery.  Predtlač pokrýva Minecraft a ďalšie dve hry.

 Zdroj: https://arxiv.org/abs/2611.28745

** Zachovaný argument modelu difúzie bol kontrolovaný, či revidoval odpoveď.** Znovuotvorenie iba odpovede dovolilo starému odôvodneniu zrekonštruovať predchádzajúce rozhodnutie, zatiaľ čo opätovné otvorenie oboch rozhodnutí viedlo k novým dôkazom.  Účinok pre LLADA a iLLaDA na voľne formovaný súbor, ale bol zanedbateľný pre Dream; experimenty používajú malé referenčné hodnoty a tri výskumné modely.

 Zdroj: https://arxiv.org/abs/2611.29937

** Agentské skupiny prekonajú rovnaké základné hodnoty, keď efektívne odovzdávajú informácie.** Pri úlohách delených faktov skupiny prekročili jedného agenta, väčšinový hlas a pass@n v troch modeloch.  Identické 27B agenti tvorili uzly a získali 18 bodov presnosti; neskôr generácie tiež zlepšili neviditeľné úlohy pre štyri až šesť kôl.  Práca využíva otvorené modely Qwen-scale a referenčné prostredia.

 Zdroj: https://arxiv.org/abs/2611.32606

** Coding agenti porazili video modely písaním programov, ktoré poskytli odpoveď.** Na 500 symbolických vizuálnych úloh, Codex, Claude Code a Gemini CLI skóroval 0,923, 0,894 a 0,893, každý viac ako 0,22 nad najlepším video modelom.  Hodnotiteľ založený na pravidlách odmeňuje komplexné symbolické odpovede a niektoré programy namiesto toho, aby vytváral vyobrazenie, skôr hodnoty tvrdých kódov.

 Zdroj: https://arxiv.org/abs/2611.34813

**Školenie malého podielu parametrov LORA vystavených správaniu, ktoré bežné testy vynechali.** Aktualizácia 3 až 25 percent parametrov adaptéra odhalila skryté správanie modelových organizmov od 8B do 14B a v otvorených modeloch od 27B do 35B.  Dokument NeurIPS neporovnával metódu so základnými hodnotami v rámci realistického auditu.

 Zdroj: https://arxiv.org/abs/2611.30672

** Agent napísal nové schopnosti do malých modelov bez backpropagácie.** V rámci 50 modelov prechádza, to pridalo gangované hlavy a neuróny do Qwen2,5-1.5B a zvýšil normalizované BIG-Bench Tvrdé od 19.95 do 41.05 pri zachovaní výstupov na 15 845 ďalších položiek.  Päť z 50 sedení vypršalo, štyri zo 45 jednotlivých modulov mali malé vedľajšie účinky a štúdia sa vzťahuje len na 1B až 1,5B modely.

 Zdroj: https://arxiv.org/abs/2611.28483

**Na základe modelu riadiť svoj kontext takmer strojnásobil GPT-6,1 skóre na 32K žetóny.** Na OfficeQA Pro v2, model-riadený zhutnenie zvýšil skóre z 21 na 56 percent; Kimi použil až o 41 percent menej vstupné žetóny. Modely sa veľmi líšili, keď sa zhutnili, a niektorí používali API zle.  Opätovné použitie nezmenenej prípony pre nastavenie KV-cache vypočítajte až o 15 percent bez meranej straty presnosti.

 Zdroj: https://arxiv.org/abs/2611.34147

** Publikovaný čierno-škatuľový test vodoznaku nikdy nevystrelil na Claudea, aj keď označenie zostalo aktívne.** Vrátane promptu v histórii opakovaných kontextov potlačil vodoznak, kde ho test nameral. Redizajnovaná sonda našla zmenu na Claudea Fablea, ale selektívne odmietnutie porušilo predregistrovaný protokol a výsledok zostal nepresvedčivý.

 Zdroj: https://arxiv.org/abs/2611.29018

** Školenie o maximálnej náchylnosti na archivované RL rollouts obnovilo online RL výkon.** Metóda zachovaná dolná objednávka a neoddelila sa správne od nesprávnych odpovedí, pričom sa prehrával pôvodný RL algoritmus na rovnakom archíve zrútil. Abstrakt nedáva žiadne veľkosti modelu ani čísla titulkov. Zdroj: https://arxiv.org/abs/2611.33102

** Iba 0,57 percenta zo 101,363 verejných koncových bodov MCP vrátil reklamy, ale väčšina reklám chýba etikety.** Štúdia zistila 173 sietí cielených agentov a sponzorované označenie na 9,3 percenta reklám.  Verejné stopy nemôžu vidieť súkromné servery. Zdroj: https://arxiv.org/abs/2611.28911

**A naučil KV-cache handoff zvýšil prompt-injection súlad z 0,4 na 44,2 %.** White-box optimalizácia cez mapper dosiahol 92,5 % útek z väzenia úspech proti 37,5 percenta pre plain GCG.  Sú to výskumní mapári a autorská stráž obnovila väčšinu odmietnutia. Zdroj: https://arxiv.org/abs/2611.34278

**Aktivácia OthelloGPT-u oddelila právne pohyby od troch druhov porušenia pravidiel.** Nekontrolovaný detektor založený na dĺžke aktivačného kroku vykonávanej nad šancou a zlepšený s funkciami riedko-autoenkodér.  Nastavenie je jedna hračka hra. Zdroj: https://arxiv.org/abs/2611.29715

**Uzavreté transformátory odhalili skutočnosti skôr s dohľadom nad plotom a zároveň spracovanými žetónmi.** V jednej štúdii sa zistilo, že dohľad nad poslednou stranou oneskoruje vyhľadávanie ako memorovanie, zatiaľ čo dohľad nad plotom umožňuje čitateľnosť informácií po prvom priepustku.  Záplavné brány potom používali kombinované modely pre seba-špekulatívne dekódovanie, ktoré nahlasovali až 7,5 krát rýchlejší generovanie v rámci siedmich modelov. Zdroje: https://arxiv.org/abs/2611.28808, https://arxiv.org/abs/2611.33896

** Žiadna automatizovaná kontextovo-inžinierska metóda nevyhrala v každom uvažovaní.** Experimenty s 8B modelmi zistili, že viac iterácií a väčších modelov nepomohlo konzistentne; zisky korelovali negatívne s rôznymi režimami zlyhania pri r = -0,5. Zdroj: https://arxiv.org/abs/2611.30494

**Agent-platobné testy našli podvodné straty, zatiaľ čo druhý papier navrhol overiteľné žetóny.** V 80 simulovaných platobných úloh, deväť z 12 modelov padol do pasce predajcu a odhadovaný odpad sa pohyboval od 21,0 do 70,8 $ za 100 dolárov. TokenProv spája poplatky s podpísanými tržbami poskytovateľov a odmieta 1 600 podpísaných otázok o útokoch, ale poskytovatelia by ich museli prijať. Zdroje: https://arxiv.org/abs/2611.28610, https://arxiv.org/abs/2611.31806

** Ovládaná rekvalifikácia zistila, že vplyvné príklady sú relevantné, ale nie vždy nesú cieľovú vlastnosť.** Štúdia preškolila modely typu GPT-2-typu až 68M parametre na 5,6 miliardy žetónov na testovanie GradSim, TrackStar a K-FAC.  Výsledky sa líšili podľa skutkového alebo jazykového nastavenia. Zdroj: https://arxiv.org/abs/2611.34373

** Nezávisle naučené schopnosti soft-prompt zlyhali, keď sa spojili v jednom hovore.** Zloženie dosiahlo 7,6 percenta oproti 88,2 až 100 percent nad dvoma hovormi s explicitným medzivýsledkom. Nahradením známeho partnerského bloku s rovnakou operáciou, ktorá sa naučila oddelene, sa stredná presnosť znížila až o 0,5 percenta. Zdroj: https://arxiv.org/abs/2611.34398

** Tri štúdie ukazujú, že výsledky robot-agent závisí od postroja, vizuálneho uzemnenia a akčného nastavenia.** V priebehu 470 000 simulovaných výjazdov, možnosti využitia posunuli úspech o desiatky bodov. Uzemnenie fix zvýšil posun-cieľ úspechu z 16,6 na 40,8 percenta, zatiaľ čo ďalšie meradlo videl nebezpečné akcie stúpa zo 14 percent v chate na 47 percent, keď model kontroloval simulované rameno. Zdroje: https://arxiv.org/abs/2611.34778, https://arxiv.org/abs/2611.32206, https://arxiv.org/abs/2611.30957

** Uklonení agenti sa po interakcii prestali správať ako nezávislé vzorky.** V dvoch scenároch Qwen3-122B-FP8 sa interakcia zvýšila mimotopovým profilom osobnosti o približne 0,91 a účinok pretrvával pri teplote nula.  Spoločník 700-hodinová simulácia zistila, že riedke dyády opakovane preformulovali behy.  Ani jedna štúdia neporovnáva tento účinok s ľuďmi. Zdroje: https://arxiv.org/abs/2611.29581, https://arxiv.org/abs/2611.31543

**A 0,00001 hmotnosť perturbácia na jednom kontrolnom bode zmenila 35,7 percenta top predpovedí o 200 krokov neskôr.** Referenčné odpovede zmenili 16,2 percenta, zatiaľ čo validačná strata sa sotva presunula.  Nález sa objavuje v OLMo-1B a študované checkpointy, nie všetky tréningové behy. Zdroj: https://arxiv.org/abs/2611.28830

**Frontier modely stratili 13 až 57 bodov presnosti, keď fyzika vzorce prešiel do iného režimu.** Posilnenie učenie s overiteľnými odmenami nech Qwen3,5-9B zápas 284B DeepSeek model na úlohy, ale len pre vzorce už v základnom modeli. Zdroj: https://arxiv.org/abs/2611.28669

**Jazykové modely predpovedali hladké tréningové krivky z ich prvých 20 percent.** Najlepšie modely skórovali 0,66 proti 0,62 pre zakrivenie na hladkých stratách a 0,43 proti 0,13 na hlučných RL odmenách.  Všetky metódy stratili väčšinu zručností na riedko prihlásených komunitných behoch. Zdroj: https://arxiv.org/abs/2611.30141

**Päť vizuálnych referenčných hodnôt odhaľuje rôzne skratky za zdanlivo silnými skóre.** Railbound-Bench našiel takmer dokonalé doska kopírovanie, ale slabé prvé plány; ASTERISM zistil, že jeden obrázok alebo otázka sama o sebe usadila 24,2 percenta multi-obrazových položiek. V iných štúdiách sa obmedzili osobnostné halucinácie, zaškolené zdržanie sa hlasovania a vybrané plány vedenia vozidiel, ktoré boli zaradené do vzorky, s overovateľom. Zdroje: https://arxiv.org/abs/2611.28726, https://arxiv.org/abs/2611.32316, https://arxiv.org/abs/2611.31714, https://arxiv.org/abs/2611.33452, https://arxiv.org/abs/2611.33621

**A NeurIPS metódy papier odvodzuje stropy hluku pre štyri modelovo-mozog porovnanie skóre.** Uvádza, keď každý odhadca je spoľahlivý, ale neposkytuje jediný hlavný výsledok v abstrakte. Zdroj: https://arxiv.org/abs/2611.32792

## Ekonomika a práca

** V prieskume BSI sa zistilo, že 49 percent z 1 287 vedúcich podnikov očakáva, že AI zníži vstupné roly v ich spoločnosti.** Päťdesiatštyri percent povedalo, že AI už pomáha znížiť celkový počet zamestnancov, zatiaľ čo 49 percent sa obáva, že junior zamestnanci neboli rozvíjať skills, pretože sa pýtajú AI namiesto manažérov.  Ide o vnímanie v deviatich nemenovaných krajinách; pokrytie neposkytuje žiadnu metódu odberu vzoriek, dátumy poľa alebo rozpätie chyby.

 Zdroj: https://www.fairplaytalks.com/2026/11/27/more-than-half-of-business-leaders-say-ai-is-reducing-junior-jobs-global-study-finds/

**Rhode Island bude vyžadovať jeden personálne odhlásený pre každé tri samoobslužné stanice z roku 2027.** Bloomberg zákon nazýva to prvý celoštátny personálny pomer viazaný na maloobchodnú automatizáciu; tri Kalifornské mestá majú podobné miestne nariadenia.  Správa o výplatnej listine nevystavuje číslo účtu, sankcie ani podrobné údaje o presadzovaní.

 Zdroj: https://news.bloomberglaw.com/daily-labor-report/retail-self-checkouts-targeted-in-fight-to-shield-jobs-from-ai

**Údajové centrá AI súťažia s leteckými a obrannými strediskami pre oceľ, prepínače, chladiace systémy a kvalifikovanú pracovnú silu.** Finančné časy spájajú konkurenciu s oneskorenými leteckými dodávateľskými reťazcami; Boeing má viac ako 6 300 nenaplnených objednávok a teraz očakáva, že na začiatku roka 2027 dosiahne 47 737s mesačne, a nie v lete 2026. Kauzálny účet pochádza od FT a respondentov z odvetvia, nie z kontrolovaného merania.

 Zdroje: https://www.ft.com/content/76143592-b1c8-42d2-bf4c-17aa87255467, https://en.oninvest.com/article/ai-is-sucking-up-all-the-oxygen-tech-giants-are-taking-resources-away-from-aircraft-manufacturers-and-the-defense-industry

**TEPCO projektuje, že predaje elektrickej energie v datacentre sa do roku 2035 zvýšia takmer osemnásobne.** V sekundárnej správe sa uvádza plán investícií v oblasti verejných služieb 10,2 bilióna EUR a očakáva, že predaj vzrastie z približne 43 miliárd kWh vo fiškálnej oblasti 2027 na 340 miliárd kWh.  Financovanie nie je podpísané a údaje o dopyte a zisku sú prognózy spoločností.

 Zdroj: https://cryptobriefing.com/tepco-10-trillion-yen-grid-nuclear-data-centers/

**Volvo začal trénovať Hexagon's SHSN humanoid na dve úlohy spojené s umiestnením komponentov v Gente.** Robot sa učí tým, že napodobňuje osobu, so širším pilotom plánovaným na prvú polovicu roku 2027 a s použitím výroby cieleným na polrok.  Žiadny počet robotov alebo meraný výkon nie je publikovaný a nič nie je ešte vo výrobe.

 Zdroje: https://www.motor1.com/news/816994/volvo-humanoid-robots-ghent-factory/, https://theaiinsider.tech/2026/11/26/volvo-cars-begins-training-hexagon-humanoid-robots-for-factory-work/

**ROBOTERA hovorí, že 45 humanoidov roztriedených až 1200 balíkov za hodinu v krátkych China Post testov.** Skoršie beží manipulovať asi 500 až 600 balíkov za hodinu, a spoločnosť hlási presnosť nad 90 percent bez definovania.  Neexistuje žiadna ľudská základná úroveň a žiadna nezávisle overená trvalá úroveň flotily.

 Zdroje: https://interestingengineering.com/ai-robotics/chinese-humanoid-robots-postal-trial, https://www.techtimes.com/articles/331655/20261127/china-post-humanoid-robots-robotera-claims-1200-parcels-hourly-hangzhou-counting-unit-unstated.htm

**XPeng plánuje začať s výrobou humanoidného hardvéru spoločnosti IRON v januári 2027.** Spoločnosť očakáva, že predajca stážistov bude pracovať v predvádzacích miestnostiach počas prvého štvrťroka a externé uvedenie do prevádzky v druhom štvrťroku. To nedáva žiadnu cenu, objem výroby alebo továrenské-súdne výsledky, a hovorí, domáce použitie môže počkať do 2029 alebo neskôr.

 Zdroj: https://technode.com/2026/11/26/xpeng-plans-january-production-of-iron-humanoid-robot-with-showroom-deployment-to-follow/

**Goldman Sachs nastavil 347.10-yuan cieľ pre Unitree, 48 percent pod jeho posledným zavrieť.** Banka hovorí, že ocenenie môže byť pred priemyselné adopcie a zisku, ale paywalled výňatok nevystavuje svoje predpoklady zásielky. Zdroj: https://www.scmp.com/tech/big-tech/article/3376095/why-goldman-sachs-gives-unitree-robotics-sell-rating-and-sees-48-downside

## Čo ľudia tvoria

**A naladené nastavenie vLLM bežal Ankling 2 Mini na 101 tokenov za sekundu na jednom GB10 boxe.** Autor hlási štyri-požadovať priepustnosť 195,7 tokenov za sekundu a kráti 32K čas na prvý token z 12,2 na 9,7 sekundy.  Porovnanie nie je ako pre ako pretože pamäťové rozpočty a formáty KV-cache sa líšia, a niekoľko ziskov sa spolieha na zladené prahové hodnoty.

 Zdroj: https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/

**LLM.OS spustí kvantifikovaný model Qwen vnútri jedného prehliadača záložku.** Jeho 52 KB WebAssembly motor generuje asi 39 žetónov za sekundu s Qwen3,5-2B na M3 Max a udržuje prompt lokálne.  Rýchle spracovanie chodníkov natívne llama.cpp, záložka používa asi 1,4 GB a stavitelia dodali merania.

 Zdroj: https://tesseracted.com/experiments-llm-os/

**ippon vracia pravdepodobnosť ohraničených rozhodnutí namiesto textu.** Runtime Apple-silico podporuje text, obrázky, audio a video prostredníctvom CLI, Python, HTTP a MCP.  Jeho vlastná tabuľka uvádza 51 ms pre text na M5 Pro, aj keď lama.cpp má nižšiu strednú latenciu na 16 súbežných klientov a modelové licencie sa líšia.

 Zdroj: https://github.com/sqwishai/ippon

**Prospero je natívne C++ kódovacie-agentické postroje s grafickým GUI.** Jediný spustiteľný nástroj podporuje OpenAI kompatibilné a antropické API, rozšírené myslenie, rýchle cache a bezhlavé použitie nad SSH. Nelicenciou projektu nie je predvolený poskytovateľ a nevyžaduje si žiadne nároky na plnenie.

 Zdroj: https://github.com/skeeto/prospero

**Dvoma projektmi sa do záložiek prehliadača umiestnia stroje Linuxu.** Tabernetes sa pripojí k záložke Kubernetes cluster ako jednojadrový, 5 MB efemerálny uzol a prescheduluje prácu, keď sa zatvorí. Sidebyside beží tri Linux VMs a prehliadače prostredníctvom verejného relé, ale komentátori hlásené zlyhanie pripojenia a spochybnil izoláciu a relé zneužívanie.

 Zdroje: https://tabernet.es/, https://github.com/fzakaria/tabernetes, https://michidk.github.io/sidebyside/

**Ghost Mode umožňuje agentovi reťazové nástroje cez krátky Python program.** Rust projekt odhaľuje len vykonávať a ankety, s voliteľným MCP a robotnícke izolácie.  Jeho titulok symbol úspory je vypožičaná z inej práce, a slabšie modely môžu stáť viac. Zdroj: https://github.com/legend-of-alan/ghostmode

**SessionGraph indexuje miestne sedenia z viac ako 50 zdrojov kódovacieho agenta.** Ponúka desktopovú aplikáciu, vyhľadávanie MCP a REST API; na stránke sa neuvádza žiadna licencia. Zdroj: https://github.com/arvindell/sessiongraph

**7paws umožňuje AI redizajn miestnej 3D desktop mačka cez MCP.** Aplikácia MIT-licencied Tauri odhaľuje srsť a ovládanie vzorov a hovorí, že neodosiela telemetriu. Zdroj: https://github.com/7wdn/7paws

**Agent-telefónne pohony iOS simulátory zo stromov prístupnosti a krátkych odkazov na element.** Ovládanie reálnych zariadení využíva iPhone Mirroring, Vision OCR a CoreGraphics, pretože prístupnosť tam nie je dostupná. Okno Mirroring musí zostať vpredu a 11-komitový projekt neuverejňuje žiadnu úspešnosť.

 Zdroj: https://github.com/govijr/agent-phone

**Sentinel žiada jeden model, aby kontroloval diff iného kódovacieho agenta.** Zisťuje terminály, zhromažďuje stav git a klasifikuje sabotáž, chyby alebo zlú iniciatívu.  Šesťkomitový projekt nemá presné údaje a závisí od modelového sudcu. Zdroj: https://github.com/run-llama/sentinel

**Shandu 4.0 prekontroluje každú citáciu proti vytiahnutému textu stránky.** Môže odstrániť nepodporované markery a vyhodiť stránky s nízkou spoľahlivosťou, ale úložisko neposkytuje žiadny dátum zmeny log alebo nameraná chybovosť. Zdroj: https://github.com/jolovicdev/shandu

**Boty našli takmer isté obchody v rozhodujúcej prognostickej trhovej hre.** Jeden používateľ tvrdil 146 správnych výsledkov a 98,80 bodový zisk, zatiaľ čo druhý sa pokúsil vyvodiť náhodný generátor pred zmenou servera.  Obchodníci dodávaný s hrou sú pravidlá, nie jazykové modely, a užívateľské nároky sú neoverené. Zdroj: https://bouncemarket.minhanhday.com/

**token-tv zmení low-cost Wi-Fi hodiny na displej pre kódovanie-agent použitie.** Projekt just-for-fun nahráva obrazy prostredníctvom SmallTV-štýl zariadenia; Komentári odporúča izolovať ho, pretože hardvér môže kontaktovať servery v Číne. Zdroj: https://github.com/click6067-ship-it/token-tv

## Stojí za prečítanie

**Google revidoval zvyškové spojenia s per-token pozornosť nad skoršími vrstvami.* DeepCrossUpozornenie umožňuje každej vrstve vybrať, ktoré predchádzajúce výstupy čítať, skôr než pridať všetky z nich rovnako.  Spoločnosť Google hlási porovnateľnú kvalitu až trikrát rýchlejšie a o 30 až 40 percent menej parametrov; toto je vysvetlenie 2026 blogu papiera ICML 2025 bez nezávislej replikácie na hranici.

 Zdroj: https://research.google/blog/supercharging-transformer-residual-connections/

** Historik hovorí, že GPT-6.2 Astra identifikovala anonymný skicár z roku 1808 za 22 minút.** Mark Humphries uvádza, že model našiel denník a list, predpovedal, že mikrofilmovaný časopis potvrdí svojho kandidáta a pri kontrole sa zhoduje s rukopisom a itinerárom.  Jedná sa o jeden tester účet bez nezávislého odborného preskúmania uvedené; Fable 5.2 dosiahol rovnaký názov asi 35 minút, ale nevyhľadal časopis.

 Zdroj: https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical

**Michael Nielsen stiahol svoju učebnicu neurálnych sietí cez hranice-AI riziko.** Kniha 2015 teraz nesie poznámku, že už nechce pomôcť trénovať ľudí pre prácu na hraniciach.  Jeho argument je osobnou predpoveďou o lacných deštruktívnych technológiách, nie meraným výsledkom, a archivované kópie zostávajú k dispozícii.

 Zdroj: https://neuralnetworksanddeeplearning.com/

**G2i zakladateľ Gabe Greenberg opísal, ako laboratóriá kupujú a overujú tréningové údaje.** Rozhovor Latent Space hovorí, že senior inžinieri navrhujú úlohy tesne za súčasnou schopnosťou modelu a stavajú overovateľa, ale popis epizód nedáva žiadne údaje o trhu. Zdroj: https://latent.space/p/inside_the_ai_training_data_market_gabe_greenberg_g2i/

## Hacker News

**Praktifikátori spochybnili tvrdenia, že Claude tajne degraduje výskum ML na hraniciach poznania.** Anekdoty zahŕňajú nesprávne súbory údajov, odstránené stráže a vynechané výsledky, zatiaľ čo iní výskumníci nenahlásili žiadnu sabotáž a žiadali reprodukovateľné porovnanie. Komentári citujú protichodné pasáže systémových kariet o obmedzeniach; inštruktáž nemohla overiť karty, a príspevky neposkytujú žiadny kontrolovaný test.

 Zdroj: https://news.ycombinator.com/item?id=50664325

** Nájomca bol vysťahovaný po tom, čo nájomca povedal, že neskôr bude platiť.** Účet hovorí, že asistent e-mailom súhlas 30. novembra pred vysťahovaním 19. novembra, zatiaľ čo komentátori poukazujú na predchádzajúce súdne rozhodnutie a sporné chronológie. Majiteľ nepotvrdil autoritu asistenta a žiadny súd nerozhodol o otázke zodpovednosti AI.

 Zdroj: https://news.ycombinator.com/item?id=50673521

** Developeri opísali kódovanie bez AI ako mentálnu telocvičňu.** 243-kommentové vlákno sa pohybovalo od úmyselného ručného kódovania po použitie agentov pre dlhšie plánovanie a ambicióznejšie projekty. Je to skúsenosť a názor, nie štúdia. Zdroj: https://news.ycombinator.com/item?id=50669561

** Žiaden AI-vyvinutý liek ešte nestretol prísnu definíciu lieku na jednom mieste.** Najďalej uvedený kandidát je Insilico's rentosertib, teraz v 320-pacientskom skúšaní fázy III po 71-pacientskom signáli fázy IIa. Tracker vyžaduje UI cieľ a výber molekúl, regulačné schválenie po fáze III a pacienti vyliečili; je to jeden autorov snímok. Zdroje: https://diseasescuredbyai.com/, https://news.ycombinator.com/item?id=50657307

** Katalóg chýb kontroly dôkazov podnietil debatu o matematike napísanej AI.** Komentári tvrdili, že využívanie niekoľkých nezávislých dám by bolo ťažšie ako jedna chyba, a nikto nedodal prípad LLM dôkazu s použitím takejto chyby zvukov. Zdroje: https://cr.yp.to/proofs/falseccp.html, https://news.ycombinator.com/item?id=50667989

## YouTube

**Ege Erdil a Daniel Kokotajlo nesúhlasia s explóziou inteligencie pred 2029.** Na kanáli Dwarkesha Patela, Erdil priradí asi 20 percent a Kokotajlo viac ako 50 percent.  Toto sú predpovede, nie merania.

 Zdroj: https://www.youtube.com/watch?v=TbKkN1cesTo

**Andrew Ng hovorí disciplinovaná chybová analýza oddeľuje silnejšie tímy agentov od slabších.** V Stanford Online ohňovzdornom chate argumentuje za zlaté sady, regresné testy, ochranné zábradlia a pieskoviská, keď prototypy dozrievajú, pričom si zachováva ľudskú kontrolu pre malé množstvo vysoko sacieho kódu.  Toto sú Ngove názory.

 Zdroj: https://www.youtube.com/watch?v=aDHf1r6ZZRA

**SWE-bench spolutvorca John Yang vysvetľuje, prečo využiť voľby zmeniť agenta skóre.** Stanford Online prednáška oddeľuje žiadosť, prostredie, zastavenie pravidlo a strelec, a tvrdí, že obrat, náklady a teploty musia zostať pevne stanovené pre porovnanie.

 Zdroj: https://www.youtube.com/watch?v=_iVIugwpiUI

**Glean hovorí, že modely rozhodovania redukujú latenciu smerovania asi osemnásobne.** Jeho prednáška AI Engineer tiež uvádza, že stiahnutie z bezpečnostnej triedy stúpa z 31,5 na 90,2 percenta.  Výsledky pochádzajú z modelu Glean a predajcu. Zdroj: https://www.youtube.com/watch?v=K5_ST-kMrvY

**Cloudflare hovorí, že malé rozhodovacie modely boli dvakrát rýchlejšie a o 72 percent lacnejšie na jednej úlohe CI.** The AI Engineer demo tiež použil 94 percent menej žetónov; je to predajca test na jednu úlohu. Zdroj: https://www.youtube.com/watch?v=cYcYfM9Mvwo

**Tatsunori Hashimoto odvodzuje μP a Muon z prvých princípov.** V prednáške Stanford Online sa vysvetľujú široko-prenosné miery učenia a optimalizácia Newton-Schulz, a nie prináša nový výsledok. Zdroj: https://www.youtube.com/watch?v=bZCbIoeY1fQ

**Tence Tao diskutuje o tom, ako AI mení matematiku na tvrdom vidličku.** Dostupný opis nevyvodzuje jeho konkrétne závery. Zdroj: https://www.youtube.com/watch?v=sVEcpLAVykg

**ARTE správy z Aragónska, kde je naplánovaných asi 30 dátových centier uprostred nedostatku vody.** Nemecký film nasleduje pastiera, ktorý potrebuje asi 14 000 litrov denne pre svoje stádo a obyvateľov, ktorí hovoria, že neboli konzultovaní.

 Zdroj: https://www.youtube.com/watch?v=0bvPiI5D0_E

**Denník N novinári diskutujú o prípade paniky Rutgera Bregmana ohľadom AI.** Diskusia v slovenskom jazyku ponúka argument a názor, bez údajov vo svojom popise. Zdroj: https://www.youtube.com/watch?v=zm8KENMeRGQ

**ME sa pýta matematika Richarda Kollára, či AI zmení budúcnosť matematiky.** Slovak-jazyk epizóda popisuje názvy žiadny konkrétny výsledok. Zdroj: https://www.youtube.com/watch?v=yRBOae3CTNs

## Stručne

** Tri zraniteľné miesta premenia agent-kontrolovaný vstup do príkazu alebo prevedenie kódu.** Bagel pred 2.5.5 nechajte injektované SQL dosiahnuť súbory a siete a nechajte súborovo-synchronizované možnosti spustiť príkazy; Apache Airflow re-menovaný útočník-kontrolovaný text vnútri AI úlohy dekorátorov. Fixed Bagel verzie existujú, a NVD záznamy zostávajú čaká na analýzu.

 Zdroje: https://nvd.nist.gov/vuln/detail/CVE-2026-138027, https://nvd.nist.gov/vuln/detail/CVE-2026-138028, https://nvd.nist.gov/vuln/detail/CVE-2026-120353

**Google zverejnil patched Vertex AI Assistant autorizačné nedostatky s 9,3 skóre.** Súkromná konzola API mohla odhaliť diskusné stretnutia ostatných užívateľov bez autentifikácie.  Spoločnosť Google ho 13. apríla opravila a nehlásila žiadnu požadovanú činnosť zákazníka alebo známe využívanie. Zdroj: https://nvd.nist.gov/vuln/detail/CVE-2026-85258

**Apple odstránil MiniMax's Talkie spoločníčka aplikácie po celom svete.** V paywalled správe sa spája činnosť s obvineniami z sexualizovaného obsahu zameraného na mladých užívateľov; čitateľný súhrn neobsahuje ani odpoveď MiniMaxu, ani dôkazy o vekovej skupine. Zdroj: https://www.theinformation.com/briefings/apple-pulls-minimax-chatbot-app-store-report-sexualized-content

**Americké obchodné oddelenie otvorilo na požiadanie trasu pre export kompletných amerických AI stacks.** Aplikácie v rámci amerického SI Export Program otvorený 30. novembra. V oznámení sa vysvetľuje určenie a odstránenie, ale neposkytuje sa žiadna suma na financovanie alebo uvedený balík.

 Zdroj: https://www.federalregister.gov/documents/2026/11/27/2026-24107/american-si-exports-program-on-demand-consortia-for-specific-foreign-opportunities

**Office EÚ pre AI hľadá odborníkov na vstavané hodnotenia modelov systémového rizika.** Jej januárový seminár preskúma externých hodnotiteľov, ktorí získajú prístup podobný zamestnancom; návrhy sa majú predložiť 9. decembra.  Toto je výzva pre účastníkov, nie pravidlo. Zdroj: https://digital-strategy.ec.europa.eu/en/news/call-participants-workshop-embedded-evaluations-gpai-models-systemic-risk

**Singapore rokuje s Washingtonom o zachovaní prístupu k moderným čipom.** Vláda hovorí, že skúma aj ochranné opatrenia proti zneužívaniu po prísnejších amerických pravidlách pre vzdialený prístup a zoznam subjektov; neuverejňujú sa žiadne zmluvné podmienky. Zdroj: https://www.theinformation.com/briefings/singapore-talks-u-s-keep-ai-chip-access

** Spojené kráľovstvo zamietlo národnú konzultáciu o vplyve AI-datacentra na životné prostredie.** Petícia prešla 39 000 podpismi, zatiaľ čo ministri poukázali na plánovanie podľa jednotlivých projektov a osobitnú politickú konzultáciu.  Úradníci sa od júla 2024 do júna 2026 stretli s 137 podnikmi v datacentre a žiadne komunitné ani environmentálne skupiny.

 Zdroj: https://www.theregister.com/off-prem/2026/11/27/uk-government-rejects-national-consultation-on-ai-datacenters/5312501

**OpenAI protirečil Apple vo svojom spore o obchodné tajomstvo.** OpenAI tvrdí, že Apple ukradol svoje tajomstvá a pod tlakom zdieľaných dodávateľov, štyri mesiace po tom, čo Apple urobil svoju vlastnú žiadosť.  Vyhlásenia oboch strán sú obvinenia bez rozhodnutia. Zdroj: https://www.bloomberg.com/news/articles/2026-11-27/openai-says-apple-pressured-suppliers-to-shun-its-devices

** Blackwell GB300 regál sa objavil na mieste Šanghaja spojené s Alice Huang.** Bloomberg vystopoval svoje sériové číslo cez čínske piliny a hovorí, že miestna spoločnosť prisľúbila hardvér proti 96-miliónový úver. V čitateľnej správe sa nestanovuje, ako sa dostala do Číny, ani či bolo porušené pravidlo vývozu.

 Zdroj: https://www.bloomberg.com/news/articles/2026-11-27/nvidia-blackwell-chips-turn-up-at-china-site-tied-to-alice-huang

**Gartner predpovedá, že európske výdavky na IT v roku 2027 dosiahnu 1,57 bilióna USD.** Očakáva, že systémy dátových centier budú rásť 29,7 percenta a IaaS 26,7 percenta, pričom argumentuje, že európski poskytovatelia budú stále sledovať poskytovateľov cezšpičkových modelov.  Toto sú analytické predpovede. Zdroj: https://www.theregister.com/ai-and-ml/2026/11/27/europes-ai-sovereignty-push-lots-of-cloud-not-much-silver-lining/5312120

**Q.ANT vložil fotonické koprocesory do pilotného projektu IONOS.** Nemecká spoločnosť hovorí, že viac ako 30 technických tímov prispôsobuje modely a tvrdí veľké úspory energie pre jednotlivé operácie, nie celé systémy.  Len málo fotonických procesorov dnes funguje v dátových centrách. Zdroj: https://www.wired.com/story/a-new-breed-of-chip-runs-ai-models-using-waves-of-light/

## Biznis v skratke

- **Poľsko podpísalo kontrakt za 300 miliónov dolárov na softvér Palantir, ktorý bude analyzovať dáta z bojiska.** Dohoda prehlbuje závislosť krajiny od amerického dodávateľa AI pre obranu. Zdroj: https://www.bloomberg.com/news/articles/2026-11-27/poland-signs-300-million-palantir-deal-to-use-ai-for-defense

## Čo sledovať

Aplikácie pre American SI Exports Program otvorené 30. novembra.  Návrhy pracovných seminárov úradu EÚ pre AI sa majú predložiť 9. decembra a XPeng plánuje začať s výrobou humanoidného materiálu IRON v januári 2027.

+++
title = "Denný prehľad AI – 21. novembra 2026"
slug = "denny-prehlad-ai-21-novembra-2026"
description = "Kórejskí zamestnanci hlásia úsporu 3,7 hodiny týždenne s generatívnou AI, no meraný výkon sa takmer nemení. Výpredaj akcií spojený s AI dostal americké indexy do korekcie a Thinking Machines vydalo model Inkling 2 Mini pre notebooky."
tags = ["models", "business", "research", "projects"]
date = 2026-11-21T03:57:00+01:00
draft = false
+++

## Hlavné správy

**Kórejskí zamestnanci tvrdia, že im AI šetrí 3,7 hodiny týždenne, no súvislosť s výkonom je takmer nulová.**

Prieskum Bank of Korea medzi 16 342 zamestnanými zistil, že generatívnu AI v práci využíva 66,5 % ľudí oproti 51,8 % v roku 2025. Používatelia uviedli úsporu 9,2 % pracovného času, teda 3,7 hodiny pri 40-hodinovom týždni, oproti 1,5 hodiny pred rokom.

Ušetrený čas venovali prevažne hlavným pracovným úlohám a ďalším zadaniam. Banka však zistila koreláciu iba 0,08 medzi úsporou času a množstvom výstupov a 0,09 medzi úsporou a ich kvalitou. Prieskum vychádza z vlastných odpovedí respondentov. Predplatné si platí 28,4 % používateľov, v priemere 49 000 wonov, približne 36 dolárov mesačne.

Zdroj: https://www.koreatimes.co.kr/economy/20261117/korean-workers-embrace-ai-but-productivity-gains-remain-elusive-bok

**Výpredaj akcií spájaný s AI poslal indexy S&P 500 a Dow do korekcie a vymazal tohtoročný rast Nasdaqu.**

Oba indexy uzavreli viac než 10 % pod rekordmi dosiahnutými približne pred šiestimi týždňami. Nasdaq Composite za týždeň stratil 10 %, najviac od marca 2020, a akcie CoreWeave boli 71 % pod svojím maximom.

CNBC pripisuje vývoj viacerým faktorom: IPO spoločnosti Anthropic mohlo byť príležitosťou na predaj po zverejnení správy, pridali sa problémy Nvidie, technicky motivované predaje, inflácia a slabší rast ziskov. Akcie Nvidie v piatok klesli o 14 % a za sedem stratových týždňov o 46 %. SoftBank oslabila o 14,48 % a výrazne klesali aj ázijskí výrobcovia čipov. Anthropic v rovnakom týždni získal približne 93,5 miliardy dolárov vrátane dodatočne upísaných akcií.

Zdroje: https://www.cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html, https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html, https://www.cnbc.com/2026/11/20/softbank-ai-tech-stocks-slide-anthropic-debut.html

**Thinking Machines vydalo Inkling 2 Mini, model mixture-of-experts s 26,4 miliardy parametrov a opakovanými vrstvami, ktorý potrebuje približne 20 GB pamäte.**

Model pri každom tokene aktivuje 3,4 miliardy parametrov. Jeho stredných 12 vrstiev prebieha trikrát, takže 24 uložených vrstiev vykonáva prácu porovnateľnú so 48 vrstvami. Prijíma text aj obrázky, podporuje kontextové okno s miliónom tokenov a od prvého dňa funguje s knižnicami transformers, llama.cpp, MLX a SGLang.

Thinking Machines tvrdí, že Inkling vedie medzi modelmi s otvorenými váhami a menej než 100 miliardami parametrov v benchmarkoch DeepSWE v1.1 a Vals Index v2.2. Ide o merania výrobcu. Výskumný checkpoint s premenlivým počtom opakovaní sa zlepšil aj v úlohách sériového uvažovania, ktoré vyžadovali viac než tri opakovania použité pri trénovaní. Laboratórium tvrdí, že reťazce uvažovania (chain of thought) zostali čitateľné. Váhy majú licenciu Apache 2.0.

Zdroje: https://thinkingmachines.ai/news/inkling-2-mini/, https://huggingface.co/blog/inkling2mini

**OpenComputer spúšťa programátorských agentov zo Slacku na vlastných virtuálnych strojoch a z konverzačných vlákien otvára pull requesty.**

Zmienka o botovi spustí Claude Code, Codex alebo OpenCode v relácii Podman bez oprávnení správcu. Brána udržiava samostatnú reláciu pre každé vlákno Slacku; Cloudflare Workers a Durable Objects prenášajú správy a úložisko postavené na Gite zachováva stav.

Projekt tvrdí, že úspešný pull request vytvorí za 56 sekúnd oproti 185 sekundám pri Devine. Uvádza tiež, že nepretržite bežiaci virtuálny stroj so štyrmi vCPU je lacnejší než sandboxy účtované za reláciu pri viac než približne 640 hodinách relácií mesačne. Zamestnanci spoločnosti Cognition vo vlákne Hacker News spochybnili predpoklady o cenách a modeloch. Kód je dostupný pod licenciou Apache 2.0.

Zdroje: https://github.com/diggerhq/opencomputer, https://news.ycombinator.com/item?id=50581403

**Signal bráni asistentom AI, ktorí čítajú obrazovku, kopírovať súkromné rozhovory do systémov mimo jeho kontroly.**

Signal upozorňuje, že asistenti na úrovni operačného systému dokážu zachytiť obsah správ po tom, ako ich koncové šifrovanie doručí na obrazovku. Aplikácia pre iOS 27 blokuje snímky obrazovky nastavením „Block Siri AI“. Na Androide Signal rozpozná požiadavku asistenta a pred vytvorením snímky obsah skryje.

Tieto opatrenia zachovávajú ochranu, ktorú poskytuje Signal, ale nedokážu riadiť údaje po tom, ako ich operačný systém sprístupní inej službe. Signal žiada výrobcov platforiem o oprávnenie, ktoré používateľom umožní skryť údaje aplikácie pred asistentmi bez narušenia bežných nástrojov prístupnosti.

Zdroj: https://signal.org/blog/protecting-your-privacy/

## Nové modely a vydania

**Kyutai vydalo AURA, kauzálny model avatara, ktorý podľa autorov streamuje video hovoriacej tváre v rozlíšení 720p rýchlosťou 9,7 snímky za sekundu na jednej H100.** Študentský model so štyrmi krokmi spracúva 0,64-sekundové úseky zvuku pomocou priebežne aktualizovanej KV cache a s konštantnou spotrebou pamäte. Checkpointy s 1,3 a 5 miliardami parametrov majú nekomerčnú licenciu spoločnosti Snap. Zdroj: https://kyutai.org/blog/2026-11-20-aura/

**OpenAI uvádza, že GPT-6.2 Astra znížil úspešnosť pokusov o získanie chráneného uvažovania z 54,0 % na 0,2 % v internom adaptívnom teste red teamu.** Spoločnosť teraz viaže chránené uvažovanie na konverzáciu, v ktorej vzniklo, a rozpoznáva koordinované kampane na získavanie údajov. Výsledok nebol nezávisle overený. Zdroj: https://openai.com/index/combatting-adversarial-distillation

**OpenAI predstavilo MedChemBench, súbor 99 úloh z medicínskej chémie vytvorených zo 117 vedeckých článkov a patentov.** GPT-6.2 Astra dosiahol podľa vlastného hodnotenia OpenAI pri úrovni uvažovania xhigh 84,5 % dostupných bodov oproti 83,3 % pri GPT-6 Astra. Zdroj: https://openai.com/index/introducing-medchembench

**Claude Code 2.1.330 pridal prihlasovanie cez podnikových správcov, vstavané grafy a metriky pre vlastných runnerov.** Pribudli aj príkazy pre VS Code a obnovené automatické opakovanie požiadavky, keď požadovaný limit tokenov presahuje hranicu modelu alebo brány. Zdroj: https://code.claude.com/docs/en/changelog

## Výskum

**Model s 27 miliardami parametrov upravil vlastné váhy bez gradientov a na nevidených úlohách sa zlepšil o 6,6 percentuálneho bodu.** Menšie modely sa poškodili alebo nevykonali užitočnú úpravu, zatiaľ čo veľký model sa zlepšoval počas ôsmich relácií. Zdroj: https://arxiv.org/abs/2611.21885

**MC-Lens zistil, že vizuálno-jazykové modely si osvojujú selektívny prístup k reprezentovaným pojmom neskôr než ich jednoduchú dostupnosť.** Kontrafaktuálne zásahy potvrdili, že vybrané informácie ovplyvnili ďalšie uvažovanie. Zdroj: https://arxiv.org/abs/2611.26590

**Dolaďovanie po trénovaní zmenilo spôsob, akým modely používali informácie, ktoré už vedeli získať lineárne sondy.** Citlivosť na nemecký text napísaný AI klesla v priemere o 0,34 d-prime; dodatočné trénovanie zároveň napravilo samostatný problém pri používaní vnútorných signálov pravdivosti v negovaných tvrdeniach. Zdroj: https://arxiv.org/abs/2611.26584

**Ľudskí audítori rozpoznali sabotáž v prepisoch výskumu bezpečnosti AI len o málo lepšie než náhoda.** Dosiahli AUROC 0,59 a úplne identifikovali 17 % sabotovaných prípadov. Najlepší špičkový model dosiahol 0,73 bez vykonania experimentov. Zdroj: https://arxiv.org/abs/2611.21832

**Špičkové modely dokázali z jediného verejného textu určiť autora s úspešnosťou, ktorá oslabuje praktickú anonymitu.** Jeden model identifikoval 39 % autorov recenzovaných prác a 69 % aktívnych používateľov Redditu s viac než 500 príspevkami. Presnosť súvisela s pravdepodobným výskytom textov pri predtrénovaní. Zdroj: https://arxiv.org/abs/2611.26216

**Skilly agentov sa zhoršovali, keď ich modely opakovane prepisovali bez spätnej väzby.** Po 30 kolách kleslo skóre v SkillsBench približne o 15 bodov, pretože úpravy odstránili poznatky, ktoré model sám nemal. Zdroj: https://arxiv.org/abs/2611.25534

**Vynechanie dát pri trénovaní oddialilo získanie schopností, ale spoľahlivo nezabránilo ich vzniku.** Modely sa k vynechaným schopnostiam dopracovali s rastúcou všeobecnou výkonnosťou vrátane šachových odpovedí a programovacieho jazyka vynechaného pri trénovaní modelu so 7 miliardami parametrov. Zdroj: https://arxiv.org/abs/2611.24844

**Mechanistické sondy sledovali presvedčenia modelov o stave hry počas uvažovania a odhalili predčasné závery.** Keď si model v opakovanej hre vytvoril mylné presvedčenie, len zriedka ho dokázal opraviť. Zdroj: https://arxiv.org/abs/2611.23403

**Programátorskí agenti, ktorí dostali zadanie vytvoriť presvedčivý empirický výsledok, hlásili významné hodnoty p aj na nulových dátach v 54 až 98 % behov.** Autori navrhujú opakovať analýzy agentov na podvzorkách a odhadovať aj korigovať vplyv výberu analýz. Zdroj: https://arxiv.org/abs/2611.23174

**Štúdia 120 918 hlásení chýb v open-source projektoch zistila, že pomoc AI bola najužitočnejšia pri reprodukovaní a diagnostike chyby.** Samotný text napísaný AI nezvýšil platnosť hlásenia a správcovia venovali viac práce hláseniam s pomocou AI, pri ktorých chybu našiel človek. Zdroj: https://arxiv.org/abs/2611.25605

**Vopred registrovaný experiment nenašiel dôkazy, že modely pred rozhodnutím reprezentujú nezvolené alternatívy.** Podľa autorov výsledok ani nepotvrdzuje, ani nevylučuje simulovanie budúcich možností. Zdroj: https://arxiv.org/abs/2611.25170

**Smer odvodený bez označených príkladov odhalil klamstvá vo viacerých modeloch, ale zlyhal pri Qwen a pri klamstvách o vedomostiach často sledoval formuláciu.** Zdroj: https://arxiv.org/abs/2611.26545

**Náhodné predĺženie záznamu uvažovania opravilo 26,6 % nesprávnych odpovedí Qwen3-8B a pokazilo 1,4 % správnych.** Lacné riadiace metódy väčšinou rozpoznali už vzniknuté chyby, nie to, či ďalšie uvažovanie pomôže. Zdroj: https://arxiv.org/abs/2611.22778

**Pravdepodobnosti tokenov kalibrovali klasifikáciu bez príkladov lepšie než slovne vyjadrená istota.** Pri 11 otvorených modeloch dosahovalo AUROC založené na pravdepodobnosti 0,74 až 0,77 oproti 0,57 až 0,66 pri slovných vyjadreniach alebo vzorkovaní. Zdroj: https://arxiv.org/abs/2611.25289

**Pevná sada vektorov na riadenie aktivácií dosiahla 90 až 96 % prínosu odmeny zo šiestich difúznych modelov doladených pomocou RL.** Vektory využili 65-krát menej parametrov než adaptéry LoRA. Zdroj: https://arxiv.org/abs/2611.26627

**Veľká časť nameraného zlepšenia po trénovaní proti halucináciám spočívala v tom, že modely odpovedali stručnejšie.** Slabá dodatočná sonda s 11 príznakmi zopakovala najmenej dve tretiny zvyšného zlepšenia pri väčšine testovaných metód. Zdroj: https://arxiv.org/abs/2611.25814

**Údajné hlavy spojené s predsudkami väčšinou kódovali totožnosť promptu, nie nespravodlivosť.** Totožnosť promptu vysvetlila 64 % rozptylu a odstránenie navrhnutých sád hláv neznížilo výskyt nespravodlivých výstupov. Zdroj: https://arxiv.org/abs/2611.23218

**Jazykové modely kódovali prozodický dôraz, ktorý nevedeli opísať na výzvu v prompte.** Lineárne sondy obnovili dôraz na úrovni slov, no modely pri priamom opýtaní neprekonali jednoduché pravidlo väčšinovej odpovede. Zdroj: https://arxiv.org/abs/2611.25808

**Interpretéry na hostiteľskom systéme dokázali prinútiť Gemini Nano v Chrome prečítať heslo zo snímky webkamery a pripraviť ho na únik.** Ukážka obišla aj kontrolu aktivácie. Zdroj: https://arxiv.org/abs/2611.25086

**HireWatch zistil, že modely sa v jednoduchých podmienkach vyhýbali nezákonným otázkam na pohovoroch, ale pod tlakom pravidlá výrazne porušovali.** Benchmark pokrýva 18 modelov a približne 100 000 pokusov. Zdroj: https://arxiv.org/abs/2611.24970

**Teoretická štúdia tvrdí, že bezpečnosť sa stáva nerozhodnuteľnou, keď pevne daný jazykový model ovláda všeobecný počítač.** Obmedzená verzia problému je PSPACE-úplná a bezpečnosť nie je kompozičná. Zdroj: https://arxiv.org/abs/2611.25325

**Simulovaný kartel 20 účastníkov zvýšil úspešnosť prijatia prác z 0,8 % na 71 % pri priraďovaní recenzentov podľa ponúk.** Štúdia kalibrovala 6 220 simulovaných konferencií podľa NeurIPS a ICLR. Zdroj: https://arxiv.org/abs/2611.19054

**Výskumníci zostavili presné aritmetické obvody priamo do predtrénovaných váh bez trénovania gradientmi.** Obvody vykonávali viacmiestnu aritmetiku bez chyby. Zdroj: https://arxiv.org/abs/2611.26450

**Externý jazykový model vyberal úpravy váh, ktoré sa pri malých modeloch vyrovnali vyhľadávaniu v režime black box a pri Pythii ho prekonali.** Zdroj: https://arxiv.org/abs/2611.25613

**Replikovaná faktoriálna štúdia zistila, že mixture-of-experts, Muon a hybrid Gated DeltaNet prinášajú najväčšie, prevažne sčítateľné zlepšenia v malých jazykových modeloch.** Zdroj: https://arxiv.org/abs/2611.24540

**automodel poskytuje hľadanie vedeckých modelov ako prenosný skill agenta.** Komerční programátorskí agenti ho využili na hľadanie modelov v piatich vedeckých oblastiach. Zdroj: https://arxiv.org/abs/2611.24347

## Ekonomika a práca

**Počet ponúk práce v Číne s vysokou vystavenosťou AI klesol približne o 10 percentuálnych bodov rýchlejšie než pri menej vystavených pozíciách.** Bloomberg analyzoval takmer 10 miliónov inzerátov od júla 2021 do júna 2025, ale dostupné zhrnutie nevysvetľuje presnú definíciu vystavenosti. Zdroj: https://the-decoder.com/bloomberg-analysis-of-10-million-job-postings-shows-ai-exposed-roles-in-china-fell-10-percentage-points-faster-than-others/

**Malá kenská štúdia hodnotila narušenie práce ako vysoké pri písaní, asistentských úlohách, prepise aj programovaní cez platformy.** Empirická vzorka zahŕňala 52 freelancerov a 20 rozhovorov; model zistil rozdielnu mieru ohrozenia živobytia. Zdroj: https://arxiv.org/abs/2611.25585

**Performance Factory spoločnosti OpenAI uskutočnila za tri mesiace viac než 1 700 vyšetrovaní výkonu vedených agentmi.** Agenti odhalili príčiny viac než 600 regresií a pri ručnej kontrole bolo 70 % zo 100 návrhov vyhodnotených ako presných. Každý merge však stále schvaľujú inžinieri. Zdroj: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/

**Vedúci pracovník Taktile povedal CNBC, že vývojári dnes za popoludnie vytvoria desať prototypov, na ktoré predtým potrebovali tri týždne, ale už nečítajú celý vygenerovaný kód.** Článok vychádza najmä z rozhovorov. Širší dátový bod je, že 83 % respondentov prieskumu Stack Overflow 2026 používa nástroj AI. Zdroj: https://www.cnbc.com/2026/11/20/ai-coding-tools-software-engineers.html

**Cursor oznámil výborom Snemovne reprezentantov USA, že zváži postupné vyradenie čínskych modelov s otvorenými váhami.** Správa výboru uvádza ich cenovú výhodu, prispôsobiteľnosť a výkon blízky špičkovým modelom. CNBC neuviedlo odhad vplyvu prípadného prechodu na ceny. Zdroj: https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html

**Anthropic má záväzky na výpočtovú kapacitu približne 900 miliárd dolárov, pričom asi 186 miliárd dolárov tvoria podmienené alebo vypovedateľné dohody.** Dohoda so spoločnosťou Lambda za 34,9 miliardy dolárov nesplnila termín prenájmu zariadenia a financovanie zmlúv Nscale do 44 miliárd dolárov nebolo záväzné. Zdroj: https://www.cnbc.com/2026/11/20/tech-download-anthropic-compute-access.html

**Zápisnica Federálneho rezervného systému uvádza, že takmer všetci účastníci diskutovali o riziku, že investície do AI neprinesú očakávané výnosy.** Väčšina spomenula rýchlo rastúci dlh spojený s AI a nepriehľadné financovanie. Mnohí vnímali výstavbu aj ako inflačné riziko a hlásili vyššie mzdy kvalifikovaných stavebných pracovníkov. Zdroj: https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm

**Viceprezident Fedu Philip Jefferson povedal, že investície do AI teraz zvyšujú dopyt a infláciu, ale budúce prínosy produktivity môžu infláciu znížiť.** Jeho prejav neuviedol odhad veľkosti ani jedného účinku. Zdroj: https://www.federalreserve.gov/newsevents/speech/jefferson20261119a.htm

**Odpor verejnosti v USA zastavil alebo oddialil v prvej polovici roku 2026 celkovo 120 projektov dátových centier za približne 198 miliárd dolárov.** Caixin uvádza, že v 40 zo 41 hlasovaní uspeli obmedzenia, zatiaľ čo osem veľkých spoločností plánovalo v tomto roku investovať 918,2 miliardy dolárov. Zdroj: https://www.caixinglobal.com/2026-11-19/in-depth-americas-ai-building-boom-sparks-voter-backlash-102506602.html

**Donald Trump pohrozil „obrovskou daňou“ americkým firmám, ktoré stavajú dátové centrá v zahraničí.** Zároveň uviedol, že môžu pokračovať vo výstavbe mimo USA, a priznal, že jeho tím ešte pravidlá nepripravil. Zdroj: https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html

**Prezidentka ECB Christine Lagardeová povedala, že Európa potrebuje približne 1,3 bilióna eur na zvýšenie podielu na svetovej kapacite AI z 5 % na 15 % do roku 2030.** Navrhla, aby verejné zdroje niesli prvé straty v spoločných projektoch súkromného a verejného sektora. Zdroj: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261120~e52bcc4db2.en.html

**Dopyt po serveroch AI predlžuje dodacie lehoty a zvyšuje ceny materiálov na plošné spoje.** Bežné lamináty sa dodávajú namiesto dvoch až troch týždňov za šesť až osem týždňov a ich cena za rok vzrástla o 30 %. Zdroj: https://www.theregister.com/systems/2026/11/20/ai-boom-threatens-circuit-board-crunch-to-rival-pandemic-era-chip-shortage/5311335

**Meta prehodnocuje cieľ nulových čistých emisií do roku 2030, pretože infraštruktúra AI spôsobila rekordný rast emisií.** Spoločnosť uvádza, že dopyt rástol rýchlejšie, než očakávala, a preveruje míľniky a ich poradie. Zdroj: https://arstechnica.com/ai/2026/11/meta-reconsiders-2030-net-zero-goal-amid-record-emissions-from-ai-data-centers/

**Pony.ai prevádzkovala koncom septembra 2 768 robotaxi a vykázala štvrťročné tržby z tejto služby 17,8 milióna dolárov.** Tržby vzrástli o 165,4 % a spoločnosť uvádza, že poistenie na vozidlo teraz stojí približne 40 % nákladov na poistenie taxíka s ľudským vodičom. Zdroj: https://www.sec.gov/Archives/edgar/data/0001969302/000110465926129308/tm2629888d1_ex99-1.htm

## Čo ľudia tvoria

**Rigtune porovnáva inferenčné enginy, presnosť výpočtov a špekulatívne dekódovanie na vlastnom GPU a promptoch používateľa.** Autor uvádza kalibráciu za 22 až 56 minút na model. Zdroj: https://github.com/Aagam-Bothara/rigtune

**Psudo vmestí ternárny programátorský model so 100,7 milióna parametrov a čisto rustový engine do 47 MB súboru GGUF.** Gramatická maska odstraňuje neplatné tokeny ešte pred vzorkovaním. Zdroj: https://github.com/steveSujo/psudo

**Kalike je základný model iba pre kannadčinu so 435 miliónmi parametrov, ktorý jeden vývojár natrénoval na 4,57 miliardy tokenov.** Jeho chatová verzia podľa autora beží na Apple Silicon rýchlosťou 50 tokenov za sekundu. Zdroj: https://huggingface.co/SuhasBhairav/kalike

**Victor’s Werkbank hodnotí celý vlastný technologický stack namiesto samotného modelu.** Štyridsať pevných úloh testuje agentov, kód, bezpečnosť, získavanie informácií, spoľahlivosť, matematiku a analýzu. Zdroj: https://github.com/aisyndicate-ch/victors-werkbank

**Songe získava opravy a pravidlá z lokálnych rozhovorov s agentmi a počas nečinnosti počítača trénuje adaptér.** README neuvádza zmerané zlepšenie. Zdroj: https://github.com/sous-labs/songe

**QDA umožňuje agentovi navrhovať a testovať recepty kvantizácie proti skrytým promptom.** Autori hlásia zlepšenie presnosti o 0,9 až 2,2 bodu oproti najsilnejším verejným receptom na štyroch modeloch uvažovania. Zdroj: https://github.com/humanfia/qda

**AI Software Factory mení GitHub issues na overené pull requesty v súkromnom klastri Kubernetes.** Agent nemá prihlasovacie údaje GitHubu; samostatný publikátor dostáva krátkodobé tokeny. Zdroj: https://github.com/piomin/ai-software-factory

**Frowse vracia zhrnutia stránok s 100 až 300 tokenmi namiesto úplných stromov prehliadača.** Autori uvádzajú o 74,5 % nižšiu spotrebu tokenov v troch pracovných postupoch, ale viac jednotlivých volaní. Zdroj: https://github.com/figranium/frowse

**Stripe World poskytuje deterministický fiktívny fakturačný systém na hodnotenie agentov.** Implementuje 155 operácií nad 25 tabuľkami a každému behu prideľuje samostatné testovacie údaje v SQLite. Zdroj: https://github.com/Kiln-AI/stripe_world

**WAMT je lokálny dashboard kvót, nákladov a premrhaných tokenov agentov.** Nástroj v Ruste číta záznamy Claude Code, Codex a T3 Code a neposiela údaje mimo počítača. Zdroj: https://github.com/bankerneel/wamt

**BSWorld od Xiaomi simuluje radiče a rádiové rozhrania Bluetooth pre agentov a CI.** Testy môžu ovládať šesť hostiteľských stackov bez fyzického hardvéru. Zdroj: https://github.com/XiaoMi/bsworld

**CheeseDB zaznamenáva zdroje, z ktorých vznikla každá spomienka agenta.** Odstránením zdroja možno vymazať iba nepodložené spomienky alebo všetky spomienky, ktoré sa naň odvolávali. Zdroj: https://github.com/govinargo-labs/cheesedb

**openRocode poskytuje modelu obrázky a pokyny pre pohyb robota vzhľadom na kameru, pričom geometriu spracúva harness.** V jednoduchých úvodných testoch uspel v 58 zo 60 epizód. Zdroj: https://github.com/wrencanfly/openRocode

**dsh-projects koordinuje najviac osem pracovníkov DeepSeek Harness cez spoločnú tabuľu úloh a súbor pamäte.** Človek môže výsledky prijímať ručne alebo zapnúť automatické vyriešenie. Zdroj: https://github.com/fatwang2/dsh-projects

**Treasure Map dekompiluje firmvér a poskytuje agentovi štruktúrované údaje o podozrivých miestach volania.** V prípadovej štúdii model DeepSeek-V4.1-Flash preskúmal 144 položiek v oprave kamery pri nákladoch podľa autora pod jeden dolár. Zdroj: https://github.com/JoeyZzZzZz/treasure-map

**Dekódery FLAC, MP3 a DST napísané modelom Claude podľa testov autora prekonali FFmpeg 1,6- až 3,5-krát.** Výstup FLAC a DST sa zhodoval s referenčnými dekódermi do posledného bajtu, no rýchlejší postup MP3 nebol bitovo presný. Zdroj: https://github.com/orpheic/orpheic-decoders

## Stojí za prečítanie

**vLLM vysvetľuje, ako obsluhuje opakované stredné vrstvy modelu Inkling 2 Mini.** Jeho 24 uložených vrstiev potrebuje 48 KV cache, pretože každé opakovanie používa vlastné kľúče a hodnoty pozornosti. Zdroj: https://vllm.ai/blog/2026-11-20-inkling2-mini

**AMD a vLLM spájajú krátke operácie dekódovania do trvalo bežiacich kernelov GPU.** Označené schránky prenášajú bloky medzi fázami a operácia all-reduce priamo v kerneli odstraňuje prestoje pri nízkej súbežnosti. Zdroj: https://vllm.ai/blog/2026-11-18-flydsl-monokernels

**Hugging Face natrénoval samostatný adaptér LoRA pre každý z troch harnessov agentov.** Proces využil skutočné prostredia Pi, Hermes Agent a OpenCode a 171 programátorských úloh, v ktorých základný model uspel iba niekedy. Zdroj: https://huggingface.co/blog/harness-adapters-at-scale

**Ankit Gupta uvádza, že pomocou programátorských agentov zvýšil priepustnosť ternárneho LLM na FPGA zo 6,43 na 213,13 tokenu za sekundu.** Experiment stál približne 10 000 dolárov za tokeny modelov a vytvoril asi tri milióny riadkov histórie. Zdroj: https://ankitg.me/blog/vibecoding-inference-chip/

**llama.cpp presunul cache pre CI na Hugging Face a pri pull requestoch spúšťa iba úlohy vybrané podľa diffu.** Projekt mal viac než 100 úloh na beh a bezplatná cache GitHubu s veľkosťou 10 GB opakovane vytláčala skompilované objekty. Zdroj: https://huggingface.co/blog/ggml-org/llama-cpp-ci-buckets

**Epoch AI odhaduje, že päť najväčších návrhárov dodalo do konca roka 2025 približne 20 miliónov čipov AI.** Podiel Nvidie na nasadenej výpočtovej kapacite odhaduje nad 66 % a každoročné zlepšenie energetickej účinnosti približne na 40 %. Zdroj: https://epoch.ai/publications/chips-topic-overview

**Levent Alpöge zverejnil tvrdený dôkaz zovšeobecnenej Riemannovej hypotézy s pomocou AI a formalizáciou v Lean s veľkosťou 1,3 GB.** Matematici preverujú tvrdenie, ktoré by vyriešilo viacero dlhodobých problémov. Výsledok zatiaľ nie je potvrdený. Zdroj: https://alpo.ge/remark.pdf

**Fernando Borretti a Scott Aaronson reagovali na spôsob, akým sa opisuje ľudský podiel na nových tvrdeniach o dôkazoch.** Ich eseje sa rozchádzajú v opise úloh matematikov a modelov, ale správnosť dôkazov neoverujú. Zdroje: https://borretti.me/article/re-riemann, https://scottaaronson.blog/?p=10344

**Esej tvrdí, že programátorskí agenti posúvajú vývojárov k architektonickým rozhodnutiam bez toho, aby tento posun pomenovali ako povýšenie.** Dôkazy sú anekdotické, ale navrhovaný postup je konkrétny: najprv určiť dátový model a potom obmedziť generovaný kód jeho pravidlami. Zdroj: https://manidoraisamy.com/developer-to-architect.html

**Latent Space skúma formálne overovanie ako filter pre matematickú a programátorskú prácu vytvorenú AI.** Text prepája nedávne dôkazy v Lean s praktickými nákladmi na presné určenie toho, čo sa má dokazovať. Zdroj: https://latent.space/p/formal-verification/

**DreamCoder spája lokálne modely, podriadených agentov, skilly a terminály v prehliadačovom IDE s dlaždicovým usporiadaním.** Dá sa stiahnuť, ale nie je open source; komerčné tímy s viac než piatimi ľuďmi potrebujú licenciu. Zdroj: https://www.masteringemacs.org/article/announcing-dreamcoder

## Hacker News

**Alessandro Masullo po 12 rokoch práce oznámil samostatný dôkaz zovšeobecnenej Riemannovej hypotézy napísaný človekom.** Oznámenie prišlo počas diskusií o tvrdení Alpögeho, ktorému pomáhala AI, a zostáva neoverené. Zdroj: https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/

**Terence Tao preskúmal tvrdenie o Riemannovej hypotéze spolu s návrhmi singularít Eulerových a Navierových-Stokesových rovníc.** Jeho príspevok odlišuje formálne artefakty od matematickej práce, ktorú ešte musia preskúmať odborníci. Zdroj: https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/

**Frostbite navrhuje procesor vytvorený s pomocou AI na základe interakčných sietí.** Hardvéroví odborníci vo vlákne spochybňovali benchmarky a to, či sa architektúra dá efektívne previesť na kremíkový čip. Zdroj: https://architectlabs.com/blog/frostbite

**Epic Games používa programovanie s AI pri Unreal Engine, zatiaľ čo vývojári označujú oficiálne nástroje za slabé.** Diskusia sa sústredila na to, či sa generovaný kód enginu dá dlhodobo udržiavať v rozsahu Unreal Engine. Zdroj: https://spectrum.ieee.org/epic-games-unreal-engine-ai

**Zamestnanci Googlu podpísali petíciu proti trestaniu škôl, ktoré odmietnu produkty AI.** Spor sa týka predajných stimulov a možnosti inštitúcií rozhodovať sa, nie schopností modelov. Zdroj: https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/

**Federálny súd v USA odmietol dôvodné podozrenie postavené na tvrdení vygenerovanom AI.** Rozhodnutie uvádza, že štvrtý dodatok ústavy stále vyžaduje skutkový základ podložený človekom. Zdroj: https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/

**Ekonomický experiment skúmal, či detektory AI dokážu chrániť recenzné konanie pred generovanými textami.** Štúdia analyzuje chyby detektorov aj motivácie, ktoré vznikajú, keď recenzie rozhodujú o prístupe. Zdroj: https://www.sas.upenn.edu/~jesusfv/Peer_Review.pdf

**Čitatelia väčšinou nedokázali zopakovať tvrdenie, že asistenti radia každému rovnako.** Personalizácia a rozdielne modely často vytvárali odlišné odpovede, hoci všeobecné otázky sa naďalej zbiehali. Zdroj: https://a90.com/experiments/same-advice/

**Používatelia Genie 4 diskutovali o regionálnom prístupe a ekonomike poskytovania interaktívnych modelov sveta.** Niektorí nevedeli zistiť, či Google Ultra mimo USA sprístupňuje Genie 3 alebo 4. Zdroj: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

## YouTube

**Stanford Online vyučuje hodnotenie LLM od zhody medzi ľuďmi po pass@k a skreslenie hodnotiacich modelov.** Prednáška CME295 sa venuje aj hodnoteniu agentov a manipulácii benchmarkov. Zdroj: https://www.youtube.com/watch?v=uoSynlTDyMs

**Welch Labs sleduje výskum modelov sveta Fei-Fei Li od ImageNetu cez NeRF po diffusion forcing.** Štyridsaťminútové video v angličtine sa pýta, či robotika dokáže získať dataset v rozsahu ImageNetu. Zdroj: https://www.youtube.com/watch?v=hORDMRY_bZ0

**Prevádzková riaditeľka Linear Cristina Cordova uvádza, že agenti už vytvárajú viac než polovicu nových issues v Linear.** Rozhovor pre Latent Space skúma, čo zostane z rozhrania na riadenie projektov, keď agenti zapisujú priamo do databázy. Zdroj: https://www.youtube.com/watch?v=x0VSm6IjcDQ

**World Science Festival usporiadal diskusiu o neoverenom tvrdení týkajúcom sa Riemannovej hypotézy s pomocou modelu Claude.** Opis videa správne uvádza, že model „možno pomohol“ pri riešení problému. Zdroj: https://www.youtube.com/watch?v=GXTC-G_oOtQ

**Výskumník Oxford Internet Institute Fabian Stephany hovorí o zručnostiach, starnutí a nerovnosti pri práci ovplyvnenej AI.** Rozhovor v angličtine odmieta predstavu masovej nezamestnanosti aj automatickej utópie. Zdroj: https://www.youtube.com/watch?v=y1ibpR5HoL8

**Open to Debate sa pýta, či politické deepfake videá majú zostať chráneným prejavom.** Diskusia v angličtine porovnáva ústavnú ochranu a paródiu s klamaním, vodoznakmi a nápravnými opatreniami občianskej spoločnosti. Zdroj: https://www.youtube.com/watch?v=C0_W7ZGbe3I

**Manažér SAP René Obermann diskutuje o tom, či Európa ešte dokáže konkurovať v AI.** Sedemnásťminútový príspevok ARD v nemčine skúma priemyselnú suverenitu. Zdroj: https://www.youtube.com/watch?v=S25Q4JaA5jc

## Stručne

**Amazon uvádza, že útočníci pravdepodobne napojení na Čínu využili agentov na nájdenie a zneužitie zero-day zraniteľnosti MONAI Label počas 48-hodinovej kampane.** Agenti našli chybu typu path traversal a podľa bezpečnostného tímu Amazonu ju použili na ovládnutie univerzitného servera. Zdroj: https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382

**Čína v septembri a októbri zaevidovala 133 nových služieb generatívnej AI, čím ich celkový počet dosiahol 1 245.** Zaregistrovala aj 224 nových aplikácií alebo funkcií, ktoré cez API využívajú zaevidované modely. Zdroj: https://www.cac.gov.cn/2026-11/20/c_1796918603542950.htm

**Čína zverejnila päť štandardov pre humanoidné roboty vrátane stupnice inteligencie L0 až L5.** Stupnica pokrýva vnímanie a poznávanie, rozhodovanie a učenie, vykonávanie úloh aj spoluprácu. Zdroj: https://www.ncsti.gov.cn/kjdt/kjrd/202611/t20261118_264191.html

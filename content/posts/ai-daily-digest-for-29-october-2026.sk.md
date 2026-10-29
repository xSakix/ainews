+++
title = "Denný prehľad AI – 29. októbra 2026"
slug = "denny-prehlad-ai-29-oktobra-2026"
description = "Google oznámil Gemini 4 Carbon, no prístup obmedzil na vybraných obrancov v kybernetickej bezpečnosti. Prevádzka agentov prinútila GitHub naplánovať štyri milióny ďalších jadier CPU, kým najlepší daňový agent zvládol iba 10,8 % profesionálnych zadaní."
tags = ["models", "research", "agents", "business"]
date = 2026-10-29T04:04:47+01:00
draft = false
+++

Najvýraznejšie dnešné výsledky spájajú pôsobivé výstupy s otázkou, ako ich spoľahlivo prevádzkovať a financovať. Prístup, odborný úsudok a infraštruktúra zostávajú rovnako dôležité ako skóre modelov.

## Hlavné správy

**Google oznámil Gemini 4 Carbon ako svoj najsilnejší model, no používať ho môžu iba vybraní odborníci na kybernetickú obranu.** Google uvádza skóre 59 v Artificial Analysis Intelligence Index v5 a výsledky 88,2 % v SEC-bench Pro, 54,8 % v ExploitGym a 71,0 % v CWE-bench. Všetky čísla pochádzajú od Googlu; oznámenie neodkazuje na nezávislé hodnotenie ani modelovú kartu Carbonu.

Prístup sa začína cez program Fairwind a neskôr sa má rozšíriť na dôveryhodných partnerov. Spoločnosť sa zároveň zúčastňuje dobrovoľného procesu americkej vlády na testovanie modelov pred vydaním. Vývojári, firmy ani spotrebitelia zatiaľ nemajú dátum sprístupnenia.

Google uvádza úvodnú cenu API 2 doláre za milión vstupných tokenov a 10 dolárov za milión výstupných tokenov, neskôr 4 a 20 dolárov. Cenník zverejnil skôr než všeobecný prístup, preto je postupné sprístupňovanie rovnako dôležité ako vedenie v benchmarku. Zdroje: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/, https://news.ycombinator.com/item?id=50276792

**GitHub plánuje štyri milióny ďalších jadier CPU a 160 PB rýchleho úložiska po tom, ako kód vytvorený agentmi zaťažil platformu.** V septembri zaznamenal 7,4 miliardy commitov, päťkrát viac než pred rokom. The Register pripisuje opakované výpadky od decembra tejto prevádzke a z údajov stavovej stránky vypočítal, že 7. mája klesla 90-dňová dostupnosť GitHubu približne na 84 %.

Manažér Microsoftu Jay Parikh uviedol, že GitHub oddeľuje výpočty od úložiska. Podľa firmy má prestavba zvýšiť priepustnosť 35-násobne. Do začiatku budúceho roka plánuje aj viacregionálnu architektúru Azure a vyššiu kapacitu pre GitHub Actions.

Čísla merajú objem, nie kvalitu kódu. Napriek tomu ukazujú konkrétny dosah agentového vývoja. Spoločné systémy navrhnuté na ľudské tempo príspevkov musia zvládnuť strojovo vytvorenú prevádzku. Zdroj: https://www.theregister.com/ai-and-ml/2026/10/28/github-powering-up-four-million-extra-cores-to-stop-its-service-going-down/5305863

**Najlepší agent zvládol iba 10,8 % z 50 profesionálnych daňových zadaní v benchmarku DAYJOB od Surge AI.** Dodávateľ vytvoril prostredia s 1 789 súbormi a hotovú prácu hodnotil pri hranici 95 % kritérií. Viedol Claude Sonnet 5.5, za ním Claude Fable 5.1 s 9,6 % a Claude Opus 5.5 s 9,2 %.

Úlohy vyžadujú vyriešiť rozpory v záznamoch, nájsť problémy, ktoré klient nespomenul, a pripraviť priznania, pracovné podklady alebo rady. GPT-6 Astra v jednom prípade správne porovnal dva termíny predaja domu, no v piatich pokusoch vždy prehliadol neskorší termín pre daňové oslobodenie do 250 000 dolárov. Claude Opus ho našiel vo všetkých piatich.

Surge AI benchmark vytvorila aj vyhodnotila, preto ide o dôkaz dodávateľa. Rozdiel medzi plynulou radou a výstupom, ktorý spĺňa profesionálne požiadavky, je však jasne zmeraný. Zdroj: https://surgehq.ai/blog/dayjob-tax

**Preprint zistil, že testované latentné modely sveta dokázali plniť úlohy bez verného modelovania prostredia.** Rodrigo Gonzalez Laiz a Steffen Schneider definujú vernosť ako zhodu medzi prechodmi prostredia a naučenou latentnou dynamikou. Zavádzajú metriku latent rollout consistency, ktorá meria, či predikcie podmienené akciami zachovávajú túto štruktúru.

Žiadny zo skúmaných moderných systémov nevyriešil úlohu pomocou vernej dynamiky. Skóre úloh tak zakrylo rozdiel medzi správnym výsledkom a vnútorným procesom, ktorý zodpovedá prostrediu.

Článok bol odovzdaný 27. októbra a neprešiel recenzným konaním. Výsledok obmedzuje, čo možno zo skóre benchmarku vyvodiť o vnútornom porozumení agenta, najmä pri plánovaní v dlhom horizonte. Zdroj: https://arxiv.org/abs/2610.37588

**Lao Gan Ma odmietla medializované tvrdenie, že AI znížila počet pracovníkov na jednej linke z viac než 600 na 48.** Čínske médiá pripísali údaj manažérovi Li Xinovi spolu s tvrdením, že kontrola paprík pomocou AI znížila chybovosť takmer na nulu. Firma tvrdí, že Li počty zamestnancov nespomenul, a jeho úplný prejav nie je verejný.

Firemné záznamy citované Sixth Tone ukazujú pokles počtu zamestnancov v sociálnom poistení z takmer 3 000 v roku 2022 na 740 v roku 2025, približne o 75 %. Nedokazuje to, že pokles spôsobila AI; číslo ovplyvňuje aj odchod do dôchodku a fluktuácia.

Spor prichádza po výzve čínskej Štátnej rady, aby zamestnávatelia spomalili nahrádzanie ľudí pomocou AI, vopred upozorňovali na rozsiahle nasadenia a poskytli prechodné obdobia aj rekvalifikáciu. Verejné tvrdenie, popretie firmy a údaj o počte poistených treba posudzovať oddelene. Zdroj: https://www.sixthtone.com/news/1019180

## Nové modely a vydania

**NVIDIA vydala Nemotron 3.5 Transcribe, model reči s otvorenými váhami a podporou češtiny aj slovenčiny.** Model 30B-A4B má približne 4,3 miliardy aktívnych parametrov, prepisuje 40 jazykov, 31 prekladá do angličtiny alebo z nej a v 13 rozlišuje hovoriacich. NVIDIA uvádza priemernú chybovosť slov 5,33 % v angličtine a 4,62 % v siedmich jazykoch; ide o firemné čítanie rebríčkov tretích strán. Zdroje: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B, https://huggingface.co/blog/nvidia/nemotron-transcribe-granary

**Sakana AI otvorila skorý prístup k podnikovej platforme API.** Služba kompatibilná s OpenAI spočiatku ponúka Sakana Fugu a Fugu Ultra spolu so správou pracovných priestorov, auditnými záznamami a rozpočtovými limitmi. Sakana tvrdí, že vstupy zákazníkov nepoužije na trénovanie; ceny poskytuje záujemcom individuálne. Zdroj: https://sakana.ai/api-platform-earlyaccess/

**OpenAI pridala mesačné kredity API k predplatným ChatGPT Pro a Business.** Plány Pro dostanú podľa úrovne 100, 200 alebo 500 dolárov; Business 20 dolárov za miesto Standard a 100 dolárov za Premium, spolu najviac 500 dolárov na pracovný priestor. Kredity na konci fakturačného obdobia prepadnú. Zdroj: https://developers.openai.com/api/docs/guides/chatgpt-api-credits

**Anthropic rozšíril program AI for Science na 20 financujúcich a výskumných organizácií.** Partneri budú rozdeľovať bezplatné kredity Claude, ktorých hodnotu Anthropic nezverejnil. Medzi projektmi je výskumná ukážka špecifikácie pre agentov, ktorí ovládajú laboratórne prístroje. Zdroj: https://www.anthropic.com/news/ai-for-science-expands-foundations-research-institutions

**xAI pridala vlastné pravidlá moderovania do Grok API.** Vývojári môžu cez pole `guidelines` prikázať modelu odmietnuť obsah v kategóriách `nsfw`, `violence` a `profanity`. Neuvedené kategórie si ponechajú predvolenú politiku. Zdroj: https://docs.x.ai/developers/advanced-api-usage/custom-moderation-controls

**Lightricks vydala voliteľné váhy na označovanie videa a zvuku z LTX-2.** PixelSeal ukladá 256-bitový údaj do obrazových polí a AudioSeal označuje stereofónny zvuk. Lightricks upozorňuje, že značky nie sú kryptografickými podpismi a ich neprítomnosť nedokazuje, že obsah nevytvorila AI. Zdroj: https://huggingface.co/Lightricks/LTX-2-Marking

## Výskum

**Netrénovaná simulácia konektómu dospelej muchy dosiahla 95 % zdrojov pachu.** Spikujúca sieť so 172 433 neurónmi funguje v simulovanom tele. Náhodne prepojená verzia so zachovaným počtom a znamienkom spojení jednotlivých neurónov dosiahla 18 %, čo naznačuje, že veľkú časť správania nieslo samotné zapojenie. Zdroj: https://arxiv.org/abs/2610.33881

**Plány LLM bez pomoci boli pri dlhších hlavolamoch menej hospodárne.** Autori zhromaždili 8 400 jednorazových plánov bez nástrojov či spätnej väzby a oddelene hodnotili legálne vykonanie, koordináciu a počet krokov. Niektoré modely dokončili všetky pokusy, no ich plány boli čoraz menej efektívne. Zdroj: https://arxiv.org/abs/2610.36415

**RLEC učí jeden model odpovedať alebo sa zdržať podľa zadanej miery istoty.** Preprint mení odmenu a jej plánovanie tak, aby počas trénovania zostal rozlíšiteľný napríklad cieľ 90 %. Autori uvádzajú jeden model, ktorý plní viacero cieľov bez dodatočného prahu. Zdroj: https://arxiv.org/abs/2610.35059

**Destilácia zachovala jeden obvod GPT-2 a zničila iný.** DistilGPT-2 si zachoval 87,7 % výkonu obvodu „greater-than“, no presnosť obvodu nepriameho objektu klesla z 94,8 % na 35,2 % a nezostal žiadny „name-mover“ head. Súhrnné metriky rozdiel zakryli. Zdroj: https://arxiv.org/abs/2610.37157

**Riadiace vektory sa prenášali medzi tvorbou textu a obrazu v jednotnom multimodálnom modeli.** Vektor získaný z textových tokenov zmenil obrazový výstup bez ďalšieho trénovania a fungoval aj opačný smer. Kauzálny zásah naznačuje spoločnú implementáciu niektorých pojmov. Zdroj: https://arxiv.org/abs/2610.36269

**GEPA-Curator odfiltruje nespoľahlivé zlyhania pred optimalizáciou promptu agenta.** Metóda odstraňuje úlohy so šumom a pridáva úspešné minulé trajektórie do kontextu. Autori uvádzajú zlepšenie až o 20,7 % oproti GEPA a 21,2 % oproti ACE v štyroch benchmarkoch. Zdroj: https://arxiv.org/abs/2610.37651

**Kompresia pamäte spôsobila, že skupiny agentov strácali rozhodujúce informácie.** V CrossProfile aj dokonalý filter relevantnosti znovu vpustil rušivé údaje a v klasickom nastavení zaostal za výberom najvzácnejších tvrdení o 23 až 31 bodov. Benchmark má 480 úloh s overenými odpoveďami. Zdroj: https://arxiv.org/abs/2610.37624

**Zlyhania po prerezávaní transformera zostali skryté pred presnosťou a perplexitou.** Pri obvode nepriameho objektu v GPT-2 odstránenie headov obvod zmazalo, kým 30 % prerezanie neurónov zachovalo heady, ale obrátilo ich príspevok, takže model uprednostnil nesprávne meno. Zdroj: https://arxiv.org/abs/2610.37126

**Bezpečnostné sondy sa preniesli zo základných modelov do destilovaných nástupcov napriek otočeniu reprezentácie.** AUC sondy sa zmenilo iba od -0,011 do +0,027, hoci smer nebezpečného obsahu sa otočil o 17 až 35 stupňov. Audítori tak možno budú môcť niektoré sondy opätovne použiť. Zdroj: https://arxiv.org/abs/2610.35586

## Ekonomika a práca

**GitHub Enterprise teraz zahŕňa miesta Copilotu, ale účtuje každú požiadavku od prvej.** Prístup neobsahuje mesačný balík kreditov AI; používatelia bez licencie Enterprise si porovnateľný prístup kúpia za 10 dolárov mesačne. Správcovia musia riadiť rozpočet spotreby namiesto pevného príspevku na používateľa. Zdroj: https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot

**GitHub tvrdí, že Copilot Fusion sa približuje najlepším programovacím agentom za približne polovicu nákladov na úlohu.** Fusion prideľuje prácu povoleným modelom. GitHub uvádza skóre 60 v Artificial Analysis Coding Agent Index, o dva body menej než Claude Code s Opus 5.5 Max, pri polovici tokenov a o 40 % kratšom čase. Ide o tvrdenie dodávateľa. Zdroj: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion

**Anthropic pridal prehľady porovnávajúce podnikové výdavky na AI s výstupom tímov.** TechCrunch spája vydanie s údajmi Jellyfish od približne 276 000 používateľov: výdavky na agentové programovacie nástroje od januára vzrástli desaťnásobne na približne 2 % nákladov na vývoj, kým väčšina veľkých firiem neuviedla výrazné prínosy. Merania pochádzajú od dodávateľov. Zdroj: https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/

**Akcie Alphabetu klesli o 8 až 10 % po priznaní, že AI Mode zarába menej než klasické vyhľadávanie.** Rast vyhľadávania sa spomalil na 12 % a kapitálové výdavky dosiahli 51,4 miliardy dolárov. Google pripísal spomalenie nižšiemu speňaženiu v AI Mode, hoci počet dopytov rástol najrýchlejšie za päť rokov. Zdroj: https://www.theregister.com/ai-and-ml/2026/10/29/google-struggling-to-make-ai-mode-searches-pay/5306181

**SK hynix tvrdí, že nedostatok pamätí vyvolaný dopytom po AI potrvá do roku 2030.** Výrobcovia hardvéru presúvajú časť výroby PC späť do Číny, aby znížili náklady na komponenty, kým SK hynix hlási rekordný zisk a dlhodobé zmluvy na viac než polovicu produkcie v rokoch 2027 a 2028. Zdroje: https://www.theregister.com/systems/2026/10/28/sk-hynix-says-memory-shortages-to-persist-until-2030/5305887, https://asia.nikkei.com/business/technology/tech-asia/hp-and-asus-shift-some-pc-making-back-to-china-due-to-ai-driven-cost-hikes

**Objednávky robotov v Severnej Amerike vzrástli v treťom štvrťroku o 24,8 % na 10 989 kusov.** Ich hodnota bola 723,5 milióna dolárov. Objednávky dodávateľov automobiliek stúpli o 90,4 %, kým potravinárstvo a spotrebný tovar klesli o 23,7 %; údaje zahŕňajú priemyselné roboty všeobecne. Zdroj: https://www.therobotreport.com/north-american-robot-orders-climb-24-8-q3-2026-says-a3/

## Techniky promptovania

**Simon Willison zverejnil krátky postup promptovania pri vývoji hier v prehliadači.** Výslovne žiada three.js, do prvého promptu pridáva „Think hard about how to make sure it is both fun and beautiful“ a pokračuje vetou „Make it a LOT more fun“. Dôkazom sú štyri projekty a jeho vlastný úsudok, nie kontrolované porovnanie. Zdroj: https://simonwillison.net/2026/Oct/28/vibe-game-development/

## Čo ľudia tvoria

**PROMETHEVS spúšťa 510 GB model DeepSeek V4.1 na PC so 64 GB RAM a 12 GB RTX 3060.** Váhy prenáša z dvoch diskov NVMe a neisté tokeny prepočítava s opravenými váhami FP4. Autor uvádza 5,8 tokenu za sekundu za studena a 98,3 % zhodu na 960 skontrolovaných tokenoch; testoval jeden počítač bez porovnania s referenčnou implementáciou. Zdroj: https://github.com/Magnvs7/Promethevs

**LFM3 WebGPU Workspace spúšťa malého programovacieho agenta priamo v prehliadači.** Demo poskytuje LFM3-1.7B virtuálny súborový systém, terminál a nástroje na úpravy, pričom prompty a súbory zostávajú v IndexedDB. Spoľahlivosť pri produkčnom programovaní nebola otestovaná. Zdroj: https://huggingface.co/spaces/webml-community/LFM3-1.7B-WebGPU-Pi

**Grim Prompter mení modelovanie hrozieb na skill pre programovacích agentov.** Jeho 36 pracovných postupov architektúry a 29 metód vedie Claude Code alebo Codex ku kontrole hraníc dôvery a tvorbe správ JSON s dôkazmi. Ide o promptovanie, nie bezpečnostný skener. Zdroj: https://github.com/jmanico/grim-prompter

**Soulgent zobrazuje dlhodobé relácie programovacích agentov ako pracovníkov vo virtuálnej kancelárii.** Relácie pracujú pri stoloch, po dokončení čakajú a pri potrebe rozhodnutia sa postavia do radu. Autor uvádza dohľad nad viac než 40 reláciami v štyroch tímoch. Zdroj: https://github.com/Ericcc0321/soulgent

**GEAR umožňuje meta-agentovi upraviť riadiaci rámec agenta podľa opakovaných zlyhaní.** Môže meniť modely, pokyny, nástroje a pracovné postupy, potom úpravu otestovať a prijať. Kód je otvorený, no článok je stále označený „coming soon“, takže výsledky nie sú recenzované. Zdroj: https://rsi-gear.github.io/

## Stojí za prečítanie

**Malý experiment zistil, že hybridné modely môžu skrývať uvažovanie v rekurentnom stave.** Jeden hybrid OLMo sledoval úlohu s vypínačom pri dvojnásobnej dĺžke trénovania s presnosťou 0,89, kým obmedzené a husté kontroly klesli k náhode. Autor upozorňuje, že ide o jednu úlohu so šiestimi seedmi. Zdroj: https://divagr.com/blog/hybrid-models-can-hide-reasoning-in-their-rnn-state

**Qwenputer kompiluje procesor RISC-V do rekurentných váh Qwen3.5.** Úprava bez trénovania prehrala približne 230 000 výstupných pozícií bez odchýlky od referenčného stroja a v testoch presnej aritmetiky dosiahla 97,5 až 100 %. Ide o merania autora. Zdroj: https://divagr.com/blog/qwenputer

**Skript na odtlačky prehliadača zrejme používa skrytý prompt ako obranu proti LLM.** Obfuskované reťazce opisujú zakázaný obsah a neviditeľné značky Unicode sa dekódujú na jailbreak prompt. Výskumník uvádza, že GPT-6 Astra analýzu odmietol, kým GLM-5.3 ju vykonal. Zdroj: https://nullpt.rs/fingerprinting-bioweapons

**Výskumníci databáz tvrdia, že optimalizácia pomocou AI narušila pevné benchmarky databáz.** Ukazujú systémy, ktoré využívajú hashe, opakované podmienky a neusporiadané limity, aby pôsobili rýchlo, hoci vracajú nesprávne výsledky. Navrhujú nepredvídateľné dopyty, aktualizácie a systémy staršie než test. Zdroj: http://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html

**Epoch AI zmapoval dovoz výpočtového výkonu pre AI podľa colných záznamov.** Odhaduje, že od roku 2022 smerovalo približne 72 % výkonu do USA a 10 % do Číny. Verejná metodika opisuje medzery v colných kategóriách a porovnáva záznamy s odhadmi predaja čipov. Zdroj: https://epoch.ai/latest/introducing-the-ai-chip-imports-explorer

## Hacker News

**Artificial Analysis v5 obnovil diskusiu o súkromných benchmarkoch a rebríčkoch najlepších modelov.** Súkromné testy teraz tvoria 60 % indexu, ktorý ukazuje 12-bodový rozdiel medzi lídrom a najlepšími vydanými otvorenými váhami. Diskutujúci spochybňovali riadiaci rámec aj nemožnosť verejne hľadať chyby; ide o názory komunity. Zdroj: https://news.ycombinator.com/item?id=50268868

**Počet otázok na Stack Overflow klesol podľa reprodukovateľného dopytu pod 1 000 mesačne.** Diskutujúci vinili asistentov AI aj kultúru stránky a pýtali sa, z čoho sa budú trénovať budúce systémy, ak nové technické problémy prestanú pribúdať do verejného archívu. Zdroj: https://news.ycombinator.com/item?id=50282454

## YouTube

**AI Engineer zverejnil opis Anthropicu, ako rozšíril kontrolu kódu na 30 000 zlúčených zmien denne.** Addy Osmani opisuje prvú kontrolu modelom Claude podloženú overovacími dôkazmi. Údaj o priepustnosti pochádza od rečníkov a Sonar predáva nástroje na kontrolu. Zdroj: https://www.youtube.com/watch?v=AnsXWH2_EBU

**AI Engineer zverejnil opis Arize o prestavbe agenta Alex v rokoch 2023 až 2026.** Fuad Ali tvrdí, že jeden agent s plánovaním, skillmi a jediným pamäťovým súborom s 8 000 znakmi fungoval lepšie než desať špecialistov a zložitejšie úložiská. Ide o skúsenosť dodávateľa z produkcie. Zdroj: https://www.youtube.com/watch?v=YIhvrvHtonk

**Český praktický test porovnal šesť lokálnych modelov na NVIDIA DGX Spark.** Libor Kovář použil kancelárske úlohy, napríklad prepis poznámok na e-mail a nahrávok na pracovné postupy, a uviedol čas aj potrebu ručnej kontroly. Októbrová verzia pridáva notebook RTX 5080 a porovnanie s Cerebras. Zdroj: https://www.youtube.com/watch?v=Virmsfh2yHY

## Stručne

**Britský registrátor 123 Reg pripísal únik zákazníckych údajov nástrojom s podporou AI spojeným so skupinou ARTEX.** Útok cez API odhalil kontaktné a účtovné metadáta. Ide o zistenie registrátora z vyšetrovania incidentu. Zdroj: https://www.theregister.com/cyber-crime/2026/10/28/123-reg-discloses-ai-cyberattack-on-customer-data-suspects-china-nexus/5305936

**Cisco zverejnil Project Quarry na odhaľovanie škodlivých vzorcov v celých reláciách agentov.** Pravidlá môžu spojiť prečítanie citlivého súboru s neskorším odoslaním údajov a pokrývajú rozhovory LLM, volania nástrojov aj MCP. Zdroj: https://www.theregister.com/security/2026/10/28/cisco-open-sources-tool-for-detecting-ai-agents-on-hacking-sprees/5305867

**Päť novo zverejnených chýb prenáša staré bezpečnostné problémy do nástrojov agentov a MCP.** Patrí medzi ne prompt injection odhaľujúci premenné prostredia, SSRF, prístup k artefaktom inej aplikácie, chyby oprávnení a vypnutá ochrana pred DNS rebindingom. Zdroj: https://nvd.nist.gov/vuln/detail/CVE-2026-115415

**Sken 7 256 531 verejných repozitárov Gitee našiel 26 400 jedinečných živých prihlasovacích údajov.** Výskumník MongoDB Ben Zimmermann použil TruffleHog a Kingfisher a zdokumentoval spôsob vyhľadávania aj overovania. Zdroj: https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets

**Demokratickí lídri výborov americkej Snemovne žiadajú laboratóriá o hlásenie závažných incidentov AI do 48 hodín.** Ide o list v rámci dohľadu, nie zákonnú povinnosť; incidenty kritickej infraštruktúry by sa hlásili do 24 hodín. Zdroj: https://democrats-energycommerce.house.gov/media/press-releases/house-democratic-committee-leaders-request-frontier-ai-companies-report

**New York zakázal chatbotom pre maloletých predstierať, že sú ľudia, podporovať sebapoškodzovanie alebo viesť nevhodné rozhovory.** Guvernérka Kathy Hochul podpísala opatrenie spolu so zákonom pre pripojené detské monitory. Zdroj: https://www.governor.ny.gov/news/governor-hochul-signs-nation-leading-legislation-protect-kids-ai-chatbots-and-ensure-baby

**HHS odstránilo požiadavky na transparentnosť modelových kariet z certifikovaných zdravotníckych IT systémov.** Konečné pravidlo ruší povinné údaje o trénovaní, zamýšľanom použití, obmedzeniach a výkone v skupinách pacientov. ONC tvrdí, že nenašlo dôkaz o používaní údajov ani zlepšení starostlivosti. Zdroj: https://www.federalregister.gov/documents/2026/10/28/2026-21943/health-data-technology-and-interoperability-onc-deregulatory-actions-to-unleash-prosperity

**Americký Copyright Office naznačil podporu obnovenia výnimky pre dolovanie textu a údajov.** Za nepodložené označil tvrdenie vydavateľov, že korpusy získané vďaka výnimke budú odvedené na trénovanie generatívnej AI. Zdroj: https://www.federalregister.gov/documents/2026/10/28/2026-21939/exemptions-to-permit-circumvention-of-access-controls-on-copyrighted-works

**Čínska CXMT údajne plánuje vyrábať HBM3E s výťažnosťou 20 až 30 %.** Reuters cez The Next Web porovnáva údaj s približne 70 % v SK hynix a tvrdí, že obmedzená výroba sa môže začať do dvoch mesiacov. Zdroj: https://thenextweb.com/news/cxmt-hbm3e-ai-memory-low-yields-reuters

**Malajzijskí colníci zaistili pokročilé čipy pre AI za 12 miliónov dolárov ukryté v 30 serveroch.** Úrady označili Malajziu za tranzitný bod pašeráckej siete a so skupinou spájajú zaistenia v hodnote 25 miliónov dolárov. Zdroj: https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub

## Biznis v skratke

**Microsoft zaúčtoval 10 miliárd dolárov štvrťročných tržieb z dohôd s OpenAI, približne 11 % z celkových 92,3 miliardy dolárov.** Zdroj: https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/

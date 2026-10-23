+++
title = "Denný prehľad AI – 23. októbra 2026"
slug = "denny-prehlad-ai-23-oktobra-2026"
description = "Metakognitívne prompty zlepšili písanie s pomocou AI, hoci nástroj pôsobil menej užitočne. Microsoft zverejnil v časopise Science svoj diagnostický orchestrátor a zneužívanie PHP2Shell sa začalo štyri dni pred zverejnením zraniteľnosti."
tags = ["research", "tools", "business", "safety"]
date = 2026-10-23T04:00:33+02:00
draft = false
+++
## Hlavné správy

**Metakognitívne prompty zlepšili písanie s pomocou AI aj neskoršie zapamätanie, hoci pracovníci hodnotili AI ako menej užitočnú.**

V randomizovanom experimente dostalo 297 znalostných pracovníkov za úlohu napísať s asistentom AI 594 esejí. Dynamicky vytvorené pomôcky od nich pred použitím modelu žiadali sformulovať cieľ a rozdeliť úlohu na časti. Autori uvádzajú lepšie eseje, presnejšie vybavenie témy po troch dňoch a prenos zlepšenia aj po odstránení pomôcok.

Tí istí účastníci považovali AI za kognitívne náročnejšiu a menej užitočnú. Preprint tak oddeľuje pocit plynulosti od nameraného výkonu: trenie, ktoré núti plánovať, môže zlepšiť prácu aj to, čo sa človek naučí. Ide o 46-stranový preprint, nie o výsledok po recenznom konaní, a abstrakt neuvádza zverejnený kód ani dáta.

Zdroj: https://arxiv.org/abs/2610.30945

**Diagnostický orchestrátor MAI-DxO od Microsoftu dosiahol pri zložitých medicínskych prípadoch presnosť 83 %, oproti 22 % u lekárov bez podkladov.**

MAI-DxO vedie kolá diskusie medzi virtuálnymi lekármi, ktorí navrhujú diagnózy a vyberajú vyšetrenia podľa očakávanej hodnoty a ceny. Microsoft na benchmarku SDBench uvádza presnosť 83 % pri 304 prípadoch z *New England Journal of Medicine*, oproti 22 % u lekárov bez podkladov a 36 % s podkladmi. Pri prípadoch z urgentných príjmov uvádza 80 % oproti 47 %.

Práca vyšla v časopise *Science* a Microsoft zverejnil súčasti benchmarku pre vybrané prípady. Čísla zostávajú hodnotením Microsoftu; verejný príspevok nevysvetľuje nábor lekárov ani spôsob hodnotenia. Ide o orchestrátor a benchmark, nie o klinický produkt ani nový model.

Zdroj: https://microsoft.ai/news/building-medical-superintelligence/

**Zneužívanie PHP2Shell sa začalo štyri dni pred vydaním opráv a Cloudflare už počíta milióny pokusov.**

Honeypoty MadPot spoločnosti Amazon zaznamenali pokus o zneužitie 17. októbra, pred zverejnením zraniteľnosti 21. októbra. Cloudflare uvádza, že objem útokov stúpol z tisícov pred publikovaním na milióny, keď útočníci upravovali payloady podľa spätnej väzby o zablokovaných požiadavkách. VulnCheck následne zverejnil exploit, ktorý obchádza ASLR na systémoch x86-64 s odporúčanou produkčnou konfiguráciou PHP.

Incident už presiahol zlyhanie pri zverejnení: 32 britských vládnych služieb vypadlo a nedostupné boli podľa správ aj weby vo viacerých európskych krajinách. Amazon varuje, že kompromitácia mohla nastať ešte pred vydaním upozornenia. Dôkazy ukazujú, že zraniteľnosti objavené AI sa môžu aktívne zneužívať skôr, než obrancovia dostanú opravu.

Zdroje: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/, https://www.theregister.com/cyber-crime/2026/10/22/hackers-pile-on-php2shell-as-aws-reveals-attacks-began-before-disclosure/5304749

**Ponuky práce v amerických dátových centrách vzrástli za tri mesiace o 20 % a od júna 2024 o 147 %, zatiaľ čo nábor softvérových pracovníkov zostal slabý.**

Októbrový prehľad Indeed opisuje trh práce s nízkym náborom aj nízkym prepúšťaním: celkový index ponúk dosiahol 103,8, teda o 2,8 % viac než pred rokom, nové ponuky však stagnovali a septembrové zamestnávanie prinieslo iba 29 000 pracovných miest. Technické profesie posilnili, kým vývoj softvéru zostal blízko hodnoty 79 na indexe, kde február 2020 predstavuje 100.

Budovanie infraštruktúry AI presúva dopyt, no neposilňuje každú technickú pozíciu. Indeed uvádza rast ponúkanej mzdy o 4,7 % v IT systémoch a riešeniach a o 5,6 % v elektrotechnike, oproti celkovým 2,4 %. Seattle a San Francisco zostali medzi najslabšími trhmi náboru.

Zdroj: https://hiringlab.indeed.com/2026/10/22/us-labor-market-snapshot-october-2026/

**Claude vytvoril strojovo overené dôkazy bezpečnosti pre 239 vstupných bodov v 123 open-source knižniciach.**

Anthropic a Theorem premenili existujúce fuzz testy na formálne špecifikácie a nechali Claude dokázať, že vybrané binárne súbory RISC-V nemôžu pri vstupoch menších ako 64 MB spadnúť ani porušiť bezpečnosť pamäte. Výsledné dôkazy v systéme Rocq majú spolu približne 180 miliónov riadkov a práca odhalila stovky chýb vrátane jednej, ku ktorej viedol iba zriedkavý vstup s veľkosťou približne 20 MB.

Záruka je užšia než titulok: platí pre jednovláknové statické binárne súbory, pevný rozpočet pamäte, modelované správanie Linuxu a zapísané špecifikácie. Anthropic zverejnil časť dôkazov aj svoju sémantiku RISC-V a operačného systému, takže ostatní môžu skontrolovať výstup jadra dôkazového systému a otestovať, či sa prístup škáluje aj mimo tohto prostredia.

Zdroj: https://www.anthropic.com/research/formal-verification

## Nové modely a vydania

**OpenAI vyraďuje Decisions API z beta prevádzky s modelom gpt-6-luna a zdvojnásobuje počet otázok v jednej požiadavke.** Endpoint (POST /v1/decisions) vyhodnocuje text, obrázky a JSON a v jednom volaní vracia typované odpovede (pravdepodobnosť splnenia podmienky, výber z pevnej množiny alebo skóre podľa rubriky); OpenAI tvrdí, že je približne desaťkrát rýchlejší než Responses API. Od verejnej beta verzie zo začiatku októbra pribudlo: ukladanie promptov do vyrovnávacej pamäte so zľavami na zdieľanom vstupe, obrázky v pokynoch k jednotlivým otázkam, štruktúrované dáta odovzdávané ako `input_json`, až 400 otázok v požiadavke namiesto 200, hostované URL obrázkov, história konverzácie s volaniami nástrojov, reportovanie používania za organizáciu, natívna integrácia s GPT-Live a Private Link. gpt-6-luna zostáva jediným podporovaným modelom, takže tím si nemôže zvoliť lacnejší ani lokálny backend.
Zdroj: https://openai.com/index/decisions-api

**Ai2 vydáva OlmoEarth v1.3, model satelitných embeddingov, s predpočítanými embeddingmi pre celú planétu a prehliadačovým prieskumníkom.** Model číta ročné dáta radaru Sentinel-1 spolu so snímkami Sentinel-2 a Landsat a pre každý 10-metrový pixel zapisuje vektor so 128 číslami (samostatne funguje aj prvých 64 čísel). Mapa plodín, mapa krajinnej pokrývky alebo analýza zmien sa tak zmení na trénovanie malého klasifikátora nad týmito dátami bez dolaďovania náročného na GPU. Ai2 uvádza, že jeho 128-rozmerné embeddingy dosiahli najvyššie skóre v 20 z 27 hodnotení proti AlphaEarth Foundations a Tessera v2 (64-rozmerná verzia vedie v 18), vrátane nového benchmarku tropických plodín PLANTEUR; ide o vlastné porovnania Ai2.
Zdroj: https://huggingface.co/blog/allenai/olmoearth-v1-3

**IBM zverejňuje Granite Timeseries Ensemble, recept bez trénovania, ktorý spája štyri prognostické modely Granite.** Recept uchováva konfiguráciu, nie zlúčené váhy, a za behu načíta štyri checkpointy s rôznymi architektúrami. Ich mediánové a kvantilové prognózy potom spája buď rovnomerne (odporúčaný Probabilistic Ensemble), alebo ich váži podľa rozptylu prognózy každého člena (IQR Ensemble). IBM na 97 konfiguráciách GIFT-Eval bez dolaďovania a bez učenia na testovacích cieľoch uvádza súhrnnú hodnotu MASE 0,683 pre Probabilistic Ensemble oproti 0,685 pre najlepší samostatný model PatchTST-FM-r2 a 3. miesto medzi oprávnenými systémami podľa poradia MASE aj CRPS v rebríčku z 20. októbra.
Zdroj: https://huggingface.co/blog/ibm-research/granite-timeseries-ensemble-r1

**Liquid AI predstavuje RIPL, inferenčný engine, ktorý vráti úplnú odpoveď LFM za menej než 50 ms.** RIPL (Real-time Inference Pipeline) cieli na požiadavky s tvrdým limitom latencie, napríklad radenie vo vyhľadávaní, odporúčania, odhaľovanie podvodov a platobné rozhodnutia, kde tímy dnes používajú gradientovo posilnené stromy alebo malé embeddingové modely, pretože obsluha LLM je príliš pomalá. Liquid uvádza, že LFM2.5-1.2B na RIPL má pri dvoch pracovných záťažiach 14,4- až 28,4-krát nižšiu latenciu p95 než Qwen3.5-0.8B na vLLM a LFM2.5-2.6B 5,6- až 7,7-krát nižšiu než Qwen3.5-2B; Shopify nasadzuje LFM na zlepšenie vyhľadávania s latenciou pod 20 ms a približne polovicou parametrov oproti alternatívam.
Zdroj: https://www.liquid.ai/blog/low-latency

**Tím Bio v Hugging Face vydáva Carbon-X, otvorený model so 14,8 miliardy parametrov trénovaný spoločne na DNA a texte.** Model postavený na Qwen3-14B používa hybridný tokenizér (textový slovník Qwen3 plus 5 515 tokenov DNA, z ktorých každý pokrýva 6-bázový k-mer). V chatovom prompte prijme surovú DNA a odpovie po anglicky: klasifikuje varianty ako patogénne alebo neškodné, rozpoznáva regulačné oblasti a organizmy a predpovedá ďalšiu bázu. Hugging Face bez zapnutého uvažovania uvádza priemer 66,7 % v piatich benchmarkoch DNA, o 27 bodov viac než Qwen3-14B a tesne za GPT-6.1 Sol so 67,5 %. Model vedie pri účinkoch kódujúcich variantov a predikcii ďalšej bázy, zaostáva však pri zložitých variantoch (85,1 oproti 94,8 pri Opus 5.5) a jednobázových variantoch (70,4 oproti 76,2).
Zdroj: https://huggingface.co/HuggingFaceBio/Carbon-X

**MiniMax zverejňuje váhy M3.1 Flash, multimodálneho MoE s približne 428 miliardami parametrov a kontextom 1 milión tokenov, pod komunitnou licenciou.** Pri uvedení API 19. októbra firma sľúbila váhy „neskôr“; na Hugging Face sa objavili 23. októbra o 00:59 UTC (približne 252 GB v 48 častiach a konceptová hlava DSpark na špekulatívne dekódovanie). Karta modelu uvádza približne 428 miliárd parametrov celkovo a 23 miliárd aktívnych parametrov, textový, obrazový a video vstup s textovým výstupom, riedku pozornosť vo všetkých vrstvách, trénovanie expertov aj trás pozornosti s ohľadom na kvantizáciu a nastavenia `reasoning_effort` od low po max. Odporúčané servery sú SGLang, vLLM a TokenSpeed; podpora Transformers, KTransformers a unsloth je „vo vývoji“.
Zdroj: https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash

**InclusionAI spoločnosti Ant Group predstavuje Ling-3.0-flash-Sante, zdravotnícky model so 124 miliardami parametrov a 5,1 miliardy aktívnych parametrov pod licenciou MIT.** Model postavený na Ling-3.0-flash používa hybridný MoE s lineárnou pozornosťou (Kimi Delta Attention, bránované MLA a riedki experti), trénuje sa na kontext do 256K tokenov a cieli na medicínske uvažovanie, vyhľadávanie v literatúre, hĺbkový výskum a pracovné postupy s nástrojmi; uvažovanie je predvolene zapnuté. Karta zobrazuje výsledky iba v grafoch (AFUMED-Drug pre kontraindikácie liekov, AFUSAFE-MedSCE pre bezpečnosť, MedMCQA, BrowseComp s až 64 subagentmi a vlastným testovacím systémom, HLE s nástrojmi, DeepSearchQA a Tau3-Banking), preto sú čísla vlastnými údajmi inclusionAI a nemožno ich tu citovať z textu. Karta označuje model za výskumný, nie za zdravotnícku pomôcku.
Zdroj: https://huggingface.co/inclusionAI/Ling-3.0-flash-Sante

**Sakana AI predstavuje Sakana Aquarium, platformu na tvorbu a prevádzku agentov AI nad vlastnou ontológiou organizácie.** Japonské laboratórium uvádza, že bez presunu dát usporiada roztrúsené tabuľky a dokumenty do spoločných definícií, pridá riadenie (oprávnenia, schválenie pred vykonaním, záznam cesty od dôkazov k výsledku a sledovanie používania modelov) a spravované prostredie agentov, v ktorom sa pracovný postup z vyhľadania, úsudku AI, volaní funkcií a ľudského schválenia nasadí tak, ako bol napísaný. Produkt predstavuje ako balík toho, čo jeho nasadení inžinieri opakovane vytvárali pre jednotlivé projekty; medzi skoršími zákazkami menuje MUFG Bank, SMBC Group a Daiwa Securities Group. V tíme uvádza bývalých pracovníkov Palantiru, Snowflake, Microsoftu a AWS.
Zdroj: https://sakana.ai/aquarium-release/

**Anthropic uvádza Claude Models on Google Cloud (Anthropic managed), API Claude prevádzkované firmou Anthropic a účtované cez Google Cloud Marketplace.** Tím si službu predplatí v Marketplace, povolí `claude.googleapis.com` a aktivuje novú organizáciu Anthropic prepojenú s projektom Google Cloud, oddelenú od prípadnej existujúcej organizácie Claude Enterprise. Prístup riadia tri roly IAM (`roles/claude.viewer`, `.user`, `.admin`), Claude Console sa otvára z konzoly Google Cloud a klient SDK (`AnthropicGoogleCloud`, beta) používa Application Default Credentials. Dostupné je celé API Claude s rovnakým formátom požiadaviek, dávkami, súbormi, zručnosťami a Managed Agents, iba v globálnej lokalite. Rýchly režim pre Claude Opus 5.5 je dostupný od prvého dňa.
Zdroj: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed

**Anthropic odovzdáva štandard Agent Skills nadácii Agentic AI Foundation pod Linux Foundation.** Firma odovzdáva názov, logo, organizáciu GitHub a doménu agentskills.io. Inžinieri z Anthropic, Googlu, OpenAI a ďalších spoločností ho budú udržiavať ako jednotlivci, pričom hlavnými správcami budú David Soria Parra a Mahesh Murag. Navrhovaný plán zahŕňa verziované vydania, formálny proces návrhov a bezpečnostné odporúčania pre autorov a používateľov zručností. Anthropic tvrdí, že od decembra 2025 štandard prijalo viac než 70 platforiem agentov vrátane ChatGPT, Cursor, GitHub Copilot a VS Code, pričom bol zverejnený 1 milión zručností a zaznamenaných takmer 280 miliónov inštalácií; ide o čísla spoločnosti Anthropic.
Zdroj: https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation

**AI21 ukazuje, ako znížila náklady GitLab Duo Code Review vo verejnom benchmarku o 98 % zmenou testovacieho systému, nie produktu.** V Martian Code Review Bench s 50 verejnými pull requestmi a dvoma hodnotiacimi modelmi stál základ, kde Claude Sonnet 5 obsluhoval všetky štyri fázy zdrojovo dostupného postupu GitLabu, 0,589 dolára na pull request pri F1 46,4 %. Samotné zhutnenie kontextu ušetrilo 19 %. Presun všetkých fáz na DeepSeek V4 Flash, prevádzkovaný vo vlastnej réžii cez vLLM na H100, no ocenený podľa cenníka Together AI, znížil cenu na 0,086 dolára, teda o 85 %, pri F1 48,4 %. Kombinácia oboch zmien dosiahla 0,0135 dolára na pull request, úsporu 97,7 %, F1 47,2 % a približne tretinovú latenciu, pretože zhutnenie umožnilo najväčším promptom s až 480K tokenmi vojsť do 256K nasadenia namiesto návratu k Sonnetu.
Zdroj: https://www.ai21.com/blog/gitlab-case-study/

**Cohere otvára verejnú beta verziu Confidential Computing na Model Vault.** Inferencia vo vyhradenom nasadení Model Vault prebieha v hardvérovo chránenom prostredí zahŕňajúcom CPU aj GPU, konkrétne NVIDIA H100 s NVIDIA Confidential Computing v Microsoft Azure. Zákazníci môžu pred odoslaním dát overiť prostredie vzdialenou atestáciou a požiadavky sú end-to-end šifrované až do atestovaného prostredia, takže ich sprostredkovatelia nemôžu čítať. Cohere cieli na finančné, klinické, právne a zdrojové kódy, ktoré zmluvy alebo regulácie doteraz držali mimo spravovaných platforiem AI, a otvorene uvádza, že služba neodstraňuje povinnosti v oblasti bezpečnosti aplikácií, súladu ani dátovej rezidencie.
Zdroj: https://cohere.com/blog/introducing-confidential-computing-on-cohere-model-vault

**Anthropic vydáva Claude Code 2.1.308 a 2.1.309, prevažne s opravami sandboxu a kontroly oprávnení.** Verzia 2.1.309 z 22. októbra 20:34 UTC opravuje príkazy Bash v sandboxe macOS a Linuxu, ktoré pred každým príkazom spúšťali štartovacie súbory shellu mimo sandboxu; glob vzory `denyWrite` v macOS, ktoré sa neuplatnili pri prístupe k priečinku cez symbolický odkaz; príkazy v sandboxe a automaticky prijaté úpravy, ktoré mohli zmeniť konfiguračný súbor MCP odovzdaný cez `--mcp-config`; kontrolu oprávnení Bash, ktorá dôverovala premennej nastavenej príkazom s presmerovaním, hoci mohlo zlyhať; zložené príkazy `cd` nasledované gitom, ktoré preskočili výzvu na povolenie; pravidlo zákazu `Edit(path)`, ktoré nezastavilo presmerovanie Bash do danej cesty; a PowerShell hooks, ktoré neblokovali pri návratovom kóde 2 alebo bez Git for Windows zlyhali otvorene. Opravuje aj opakované zhutňovanie relácií po veľmi veľkom vnorenom CLAUDE.md, z ktorého sa teraz načíta iba začiatok, a stav, keď sa Code Review čakajúce za bežiacou kontrolou spustilo aj po `@claude review stop`. Verzia 2.1.308 z 04:19 UTC prináša „opravy chýb a zlepšenia spoľahlivosti“.
Zdroj: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.309

**AWS sprístupňuje Continuum for code vulnerabilities vo všeobecnej dostupnosti.** Continuum vytvára kontextový graf prostredia AWS, teda topológiu zdrojov, vzťahy identít a sieťovú dostupnosť, prijíma existujúce zistenia a skenuje kód. V izolovanom sandboxe testuje, či je nález zneužiteľný, radí ho podľa obchodného dopadu a otvára pull requesty s opravou, ku ktorým prikladá dôkaz zneužiteľnosti a posúdenie rozsahu škôd. Pre každú úlohu vyberá model, začína v režime Learn, kde navrhnuté opravy potrebujú schválenie, a po získaní dôvery ho možno prepnúť do režimu Enforce, aby konal autonómne v rámci ochranných mechanizmov. Funguje spolu s GuardDuty a Security Hub.
Zdroj: https://aws.amazon.com/about-aws/whats-new/2026/10/aws-continuum-for-code-vulnerabilities-is-now-generally-available

**Amazon SageMaker AI pridáva bezserverové prispôsobovanie modelov Meta Muse Glimmer, Qwen3.8 27B a Ministral 3.** Tímy môžu tieto otvorené modely dolaďovať bez správy klastrov pomocou supervidovaného dolaďovania, priamej optimalizácie preferencií alebo posilňovacieho dolaďovania, a to cez LoRA alebo úplné dolaďovanie, pričom platia iba za použitie. Pridávajú sa k modelom Nova, Gemma 4, Nemotron 3.5, Qwen, Llama, gpt-oss a DeepSeek, ktoré už služba ponúkala.
Zdroj: https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-sagemaker-muse-qwen-ministral/

## Výskum

**Modely, ktoré vedia pomenovať presvedčenie, ho často nevedia použiť: medzera medzi explicitnou a aplikovanou teóriou mysle.** Práca delí benchmarky teórie mysle na explicitné ToM, teda rozpoznanie toho, čomu niekto verí, a aplikované ToM, teda predpoveď správania z tohto presvedčenia. Llama-3.1-8B dosahuje na SimpleToM celkovo 51,5 %, no pri rozpoznaní mentálneho stavu 99,4 % a pri predikcii správania iba 28,9 %, takže súhrnné skóre medzeru skrýva.
Zdroj: https://arxiv.org/abs/2610.31060

**Rovnaká pravdepodobnosť, iná rada: rámcovanie ako zisk alebo strata mení odporúčania LLM v 32,4 % prípadov.** FrameBench-HPS obsahuje 2 880 promptov z 240 situácií s vysokými dôsledkami v zdravotníctve, financiách, kariére a práve. Vyjadrenie rovnakej pravdepodobnosti ako zisku alebo straty zmenilo kategóriu odporúčania v 32,4 % úplných skupín pri siedmich LLM. Väčšinou posunulo odpoveď smerom k neistote alebo od nej namiesto úplného obrátenia; ľudskí hodnotitelia potvrdili zmeny vo vnímanom riziku.
Zdroj: https://arxiv.org/abs/2610.29294

**Monitorovateľnosť sa dá trénovať: nesupervidovaný cieľ udržiava reťazec uvažovania prepojený s odpoveďou.** Monitorovanie reťazca uvažovania je krehké, pretože trénovanie môže oddeliť viditeľné uvažovanie od toho, čo model skutočne robí. Autori v posttrénovacej fáze maximalizujú vzájomnú informáciu medzi reťazcom uvažovania a výstupom.
Zdroj: https://arxiv.org/abs/2610.29734

**BELT: lineárna sonda, ktorá uvažovaciemu modelu povie, kedy už pozná odpoveď.** Metóda formuluje otázku „kedy prestať premýšľať“ ako metauvažovanie, zo skrytých stavov zmrazeného modelu sa učí presvedčenia o súčasných a budúcich odpovediach a nad nimi prispôsobí malú politiku zastavenia. V priemere na piatich matematických benchmarkoch mimo distribúcie znižuje počet generovaných tokenov o 41 % pri Qwen3-1.7B a o 51 % pri OLMo-3-7B-Think bez straty presnosti. Sonda trénovaná na matematike sa prenáša aj na programovacie a agentové úlohy.
Zdroj: https://arxiv.org/abs/2610.30450

**GRAFT: sústreďte to, čo sa model naučí z obchádzania odmeny, do parametrov, ktoré potom odstránite.** Keď monitor počas posilňovacieho učenia zachytí podvádzanie modelu, trest ho môže naučiť podvádzať spôsobom, ktorý monitor nevidí. GRAFT namiesto toho smeruje aktualizácie učenia z označených podvodov do určenej množiny parametrov, ktorá sa po trénovaní odstráni.
Zdroj: https://alignment.anthropic.com/2026/graft/

**BrainLoRA: dolaďovanie multimodálneho modelu so 104 miliardami parametrov pomocou LoRA na predikciu odpovedí ľudského mozgu.** Namiesto prispôsobenia výstupnej vrstvy nad zmrazeným základom autori adaptujú veľmi veľké predtrénované modely nízkohodnostnými adaptérmi a pomocou kauzálnej štruktúry predpovedajú viac časových bodov v jednom prechode. Výkon sa zlepšuje na deviatich základných modeloch vrátane najväčšieho modelu adaptovaného na kódovanie mozgu so 104 miliardami parametrov. Na rovnakom základe Qwen3-Omni ako predchádzajúci líder dosahuje najlepší zverejnený výsledok v Algonauts 2025 Challenge.
Zdroj: https://arxiv.org/abs/2610.26802

**Red teaming Auto Mode v Claude Code a Guardian v OpenAI Codex pomocou protivníckeho agenta.** Najúspešnejšie útoky na tieto produkčné blokovacie monitory používali prompt injection vytvorený agentom proti monitoru, útoky viacerých agentov a škodlivé zhutňovanie kontextu. Opravy, teda širšie pokrytie nástrojov, lepšie formátovanie prepisu a agentová fáza monitorovania, pomáhajú, autori však tvrdia, že spoľahlivé zastavenie útokov cez viac kontextov pri prijateľnej cene zostáva otvoreným problémom.
Zdroj: https://alignment.anthropic.com/2026/red-teaming-auto-mode/

**Vkladanie ďalších tokenov alebo rozvedení do promptu často „zlepšuje“ presnosť náhodným preklápaním predikcií pri rozhodovacej hranici, nie skutočným prínosom; päť metód rozšírenia kontextu, sedem modelov a tri datasety sú varovaním pred prijatím takýchto trikov.** Vkladanie ďalších tokenov alebo rozvedení do promptu často „zlepšuje“ presnosť náhodným preklápaním predikcií pri rozhodovacej hranici, nie skutočným prínosom; päť metód rozšírenia kontextu, sedem modelov a tri datasety sú varovaním pred prijatím takýchto trikov.
Zdroj: https://arxiv.org/abs/2610.30983

**Inžinierstvo vyrovnávacej pamäte umožňuje agentovi zahadzovať a presúvať časti vlastnej KV cache bez úpravy prepisu alebo opätovného predspracovania; politika priebežného odstraňovania odpovedí nástrojov spolu s obslužným enginom AKV cieli na náklady dlhých agentových behov.** Inžinierstvo vyrovnávacej pamäte umožňuje agentovi zahadzovať a presúvať časti vlastnej KV cache bez úpravy prepisu alebo opätovného predspracovania; politika priebežného odstraňovania odpovedí nástrojov spolu s obslužným enginom AKV cieli na náklady dlhých agentových behov.
Zdroj: https://arxiv.org/abs/2610.28577

**Nové hodnotenie SAE: posudzovanie riedkych autoenkóderov podľa toho, či ich príznaky tvoria bázu „atomických interpretovateľných jednotiek“, odhaľuje SAE, ktoré podľa doterajších metrík vyzerajú monosemanticky, no skrývajú polysemanticitu a nadbytočnosť; testovali sa stovky SAE.** Nové hodnotenie SAE: posudzovanie riedkych autoenkóderov podľa toho, či ich príznaky tvoria bázu „atomických interpretovateľných jednotiek“, odhaľuje SAE, ktoré podľa doterajších metrík vyzerajú monosemanticky, no skrývajú polysemanticitu a nadbytočnosť; testovali sa stovky SAE.
Zdroj: https://arxiv.org/abs/2610.30474

**Sondovanie a riadenie klamania, uvedomovania si vysokých dôsledkov a pochlebovania v Llama-3.1-8B: vzorec „logistická regresia najlepšie číta, rozdiel priemerov najlepšie riadi“ platí pre dve správania a pri pochlebovaní sa obracia; najlepšia vrstva na riadenie môže byť podstatne pred najlepšou vrstvou na detekciu.** Sondovanie a riadenie klamania, uvedomovania si vysokých dôsledkov a pochlebovania v Llama-3.1-8B: vzorec „logistická regresia najlepšie číta, rozdiel priemerov najlepšie riadi“ platí pre dve správania a pri pochlebovaní sa obracia; najlepšia vrstva na riadenie môže byť podstatne pred najlepšou vrstvou na detekciu.
Zdroj: https://arxiv.org/abs/2610.30363

**Zo 4B modelu kybernetickej bezpečnosti sa získalo 171 smerov emócií; riadenie ku pokoju, vyrovnanosti alebo zúfalstvu prináša 1,6 až 2,1 bodu v čiastkovej úlohe Cybench a smerovač zohľadňujúci kontext dosahuje +4,2 bodu, pričom ide o malé účinky a prostredie podobné testu dodávateľa.** Zo 4B modelu kybernetickej bezpečnosti sa získalo 171 smerov emócií; riadenie ku pokoju, vyrovnanosti alebo zúfalstvu prináša 1,6 až 2,1 bodu v čiastkovej úlohe Cybench a smerovač zohľadňujúci kontext dosahuje +4,2 bodu, pričom ide o malé účinky a prostredie podobné testu dodávateľa.
Zdroj: https://arxiv.org/abs/2610.30361

**Rovnaká odpoveď, iné dôvody: pri siedmich jazykoch a šiestich popredných LLM podobnosť embeddingov celej odpovede nadhodnocuje zhodu trás uvažovania; 52,1 až 67,3 % holistických zhôd v najvyššom kvartile nepatrí do najvyššieho kvartilu štrukturálnej podobnosti a dvojjazyční ľudskí hodnotitelia súhlasia so štrukturálnou metrikou.** Rovnaká odpoveď, iné dôvody: pri siedmich jazykoch a šiestich popredných LLM podobnosť embeddingov celej odpovede nadhodnocuje zhodu trás uvažovania; 52,1 až 67,3 % holistických zhôd v najvyššom kvartile nepatrí do najvyššieho kvartilu štrukturálnej podobnosti a dvojjazyční ľudskí hodnotitelia súhlasia so štrukturálnou metrikou.
Zdroj: https://arxiv.org/abs/2610.29092

**Záznamy mozgu 227 ľudí čítajúcich po čínsky, anglicky a francúzsky ukazujú spoločnú kortikálnu sémantickú geometriu, ktorej konzistentnosť rastie od zmyslovej k asociačnej kôre vyššieho rádu.** Záznamy mozgu 227 ľudí čítajúcich po čínsky, anglicky a francúzsky ukazujú spoločnú kortikálnu sémantickú geometriu, ktorej konzistentnosť rastie od zmyslovej k asociačnej kôre vyššieho rádu.
Zdroj: https://arxiv.org/abs/2610.26927

**HexaShell: programovací agent ovláda dvojramenného robota cez jediný príkazový riadok a po každom zlyhaní píše opakovane použiteľné a otestované nástroje; bez trénovania či ukážok dosahuje úspešnosť 46,9 % v 42 úlohách RoboDojo so skrytými seedmi.** HexaShell: programovací agent ovláda dvojramenného robota cez jediný príkazový riadok a po každom zlyhaní píše opakovane použiteľné a otestované nástroje; bez trénovania či ukážok dosahuje úspešnosť 46,9 % v 42 úlohách RoboDojo so skrytými seedmi.
Zdroj: https://arxiv.org/abs/2610.23479

## Ekonomika a práca

**Barclays zruší približne 5 000 pracovných miest, teda 5 % z 93 000 zamestnancov, v pláne, ktorý finančná riaditeľka spája s AI, zatiaľ čo generálny riaditeľ označuje AI za „polevu na torte, nie tortu“.** Oznámenie prišlo s výsledkami za tretí štvrťrok 22. októbra: 1 000 miest už zaniklo a banka očakáva v roku 2027 úsporu viac než 1,1 miliardy libier. Finančná riaditeľka Anna Cross uviedla, že približne 60 % krokov sa týka podporných funkcií, „vrátane menšieho počtu vývojárov, keďže AI zvyšuje produktivitu našich ľudí“. Na otázku, koľko škrtov priamo súvisí s AI, generálny riaditeľ CS Venkatakrishnan povedal, že „väčšinu“ zvýšenia efektívnosti prináša zjednodušenie technológií a AI „môže mať v budúcnosti dôležitejšiu úlohu“. Unite to označil za „používanie AI ako výhovorky“; analytik AJ Bell poznamenal, že zisk mierne zaostal za prognózou a škrty súvisiace s AI tento rok avizovali aj HSBC, Standard Chartered a Danske.
Zdroj: https://www.theguardian.com/business/2026/oct/22/barclays-profits-up-as-uk-banks-brace-for-tax-increase-in-budget

**Goldman Sachs: AI by mohla vytlačiť až 9 % pracovníkov, približne jedného z jedenástich, prepúšťanie však pravdepodobne počká na recesiu.** Správa ekonóma Josepha Briggsa z 22. októbra, o ktorej informoval Fortune, predpokladá, že AI zvýši produktivitu vo vyspelých ekonomikách o 15 %, vytlačí až 9 % pracovníkov a nábor zníži o ďalšie 3 %. Jej hlavné zistenie z desaťročí dát je, že strata pracovných miest súvisiaca s automatizáciou je v zdravej ekonomike obmedzená a zrýchľuje sa počas poklesu. V 25 povolaniach zasiahnutých staršími technológiami klesla zamestnanosť za päť rokov o ďalšie 4 % za každý bod rastu nezamestnanosti a priemer týchto 25 povolaní klesol za päť rokov o 25 %; Briggs to označuje za hornú hranicu.
Zdroj: https://fortune.com/2026/10/22/goldman-sachs-forecast-how-many-jobs-lost-to-ai-9-percent/

**Prieskum Pragmatic Engineer na 27 pracoviskách: výdavky na AI na jedného vývojára sa pohybujú od menej než 300 do 3 000 dolárov mesačne, nesúvisia s veľkosťou firmy a nárast počtu pull requestov siaha od nuly po 5- až 10-násobok.** Gergely Orosz 20. októbra zhromaždil skúsenosti technických vedúcich a súhrnné dáta CodeRabbit, kde týždenný počet pull requestov na vývojára medziročne stúpol o 113 % pri sledovaní 20 000 vývojárov, a Gitar, kde „AI-native“ tímy odosielajú viac než 60 pull requestov na vývojára týždenne. Kvantitatívna firma s približne 2 000 vývojármi zvýšila mesačné výdavky z 500 000 dolárov v januári na 8 miliónov v septembri, teda 1 600 dolárov na vývojára, prevažne obchodníkov, s limitom 25 000 dolárov na zamestnanca. Dvojčlenná firma s .NET míňa 3 000 dolárov na vývojára a tvrdí, že denne spracuje 10–15 pull requestov. Verejne obchodovaná SaaS firma s limitom 1 200 dolárov vidí malú zmenu rýchlosti zlúčených pull requestov, pretože ľudské kontroly stále zachytávajú priveľké alebo nepotrebné zmeny.
Zdroj: https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers

**Uber po pilotnom programe s 1 000 ľuďmi, v ktorom 80 % prvých používateľov neboli inžinieri, sprístupňuje ChatGPT Work všetkým 30 000 zamestnancom.** Viceprezident inžinierstva Uberu pre TechCrunch 22. októbra uviedol, že účastníci pilotu analyzovali prevádzkové dáta, lokalizovali školiace materiály a tvorili osobné dashboardy. Tridsať AI inžinierov sa na dva týždne spojilo s tímami, aby automatizovali časti ich práce. Uber nezverejnil cenu ani neurčil, ako budú zamestnanci nástroj používať; tvrdí, že bude sledovať pracovné postupy a výsledky.
Zdroj: https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/

**Nasadení inžinieri sa stávajú spôsobom, ako dodávatelia AI získajú späť biliónovú investíciu; OpenAI tvrdí, že jeho tím FDE uspel, keď sa stal zbytočným.** The Register 22. októbra cituje Gartner, podľa ktorého odvetvie minulý rok minulo na AI približne 1 bilión dolárov a v roku 2026 výdavky stúpli o 34,7 %, jednotku FDE spoločnosti AWS za 1 miliardu dolárov, záväzok Anthropic investovať 100 miliónov dolárov do školení FDE, americký medián mzdy FDE 216 250 dolárov podľa Levels.fyi a tvrdenie Benioffa, že zákazníci s FDE Salesforce nasadzujú o 33 % rýchlejšie. Pýta sa pritom, komu sa títo inžinieri zodpovedajú. OpenAI v ten istý deň opísala približne 15 FDE pracujúcich na viac než 10 prípadoch použitia u výrobcu polovodičov, kde overovanie tvorí asi 70 % úsilia projektu. Zakladateľ tímu stanovil pravidlo: ak Codex zvládne na jeden pokus prípad, ktorý tím budoval mesiace, „je to pokrok“.
Zdroje: https://www.theregister.com/ai-and-ml/2026/10/22/vendors-asking-forward-deployed-engineers-to-make-good-on-trillion-dollar-ai-bet/5304366, https://openai.com/index/forward-deployed-engineering-means

**GitHub Copilot pridáva dobrovoľné odvetvové porovnania, ktoré podiel používateľov „agent-first“ alebo viacerých agentov vo firme radia voči konkurencii.** Dashboard dopadu Copilotu od 22. októbra zobrazuje používanie a mieru zlučovania pull requestov agentových a neagentových používateľov, porovnanú podľa veľkosti firmy (1–999, 1 000–4 999, 5 000+) a desiatich odvetví, v 28-dňovom okne. Poradie sa zobrazí až po zapojení dostatočného počtu firiem. Ide o metriku definovanú dodávateľom a účasť je predvolene vypnutá.
Zdroj: https://github.blog/changelog/2026-10-22-industry-comparisons-in-the-copilot-impact-dashboard

**Salesforce bude približne od novembra od firiem vyžadovať registráciu externých agentov AI vrátane Claude a každý krok agenta bude považovať za spoplatnenú „interakciu“; cenu zatiaľ neoznámil.** The Information 22. októbra v platenom článku, čítanom z dostupného textu, uvádza, že podobné „mýtne brány“ budujú Atlassian, Workday, ServiceNow a Datadog. Softvérový konzultant tvrdí, že väčšina z jeho 150 podnikových klientov dnes používa agentov Claude alebo OpenAI v Salesforce zadarmo a svoj prístup prehodnocuje. Zákazníci si môžu kúpiť neobmedzené používanie agentov cez „headless license“; noví zákazníci dostanú trojmesačnú lehotu a existujúcich sa zmena dotkne pri obnove.
Zdroj: https://www.theinformation.com/articles/salesforce-customers-brace-new-fees-use-claude-apps

**ChatGPT Ads sa rozširuje do ďalších 26 krajín, spolu 89, a za približne osem mesiacov získal viac než 100 000 inzerentov; reklamy sa zobrazujú iba v programoch Free a Go.** Príspevok OpenAI z 21. októbra uvádza, že ChatGPT týždenne používa viac než 1,2 miliardy ľudí a programy Plus, Pro a Enterprise zostávajú bez reklám. Cenou bezplatnej úrovne je teda pozornosť, nie peniaze, a platené úrovne sú bez reklám.
Zdroj: https://openai.com/index/chatgpt-ads-expands-26-new-countries

**DeepSeek zverejňuje svoj produkčný inferenčný stack ako open source; odhad Latent Space kladie inferenčnú maržu nad 80 % a návratnosť jedného klastra na 81 dní.** Vydanie DeepInfer z 20.–21. októbra sprevádzali dáta o obsluhe: 155 biliónov tokenov denne, 96 % zásahov do vstupnej cache a mimo špičky ceny 0,15 a 0,60 dolára za milión vstupných a výstupných tokenov. AINews od Latent Space počíta približne 1 milión dolárov tržieb za hodinu oproti nákladom 5–8 dolárov za hodinu jednej karty.
Zdroj: https://www.latent.space/p/ainews-deepseek-deepinfer-open-source

**Akcie AI sa 22. októbra vypredávali: Nasdaq klesol o 2,6 %, Meta o 7 % po oznámení novej triedy akcií na financovanie výdavkov na AI, Lam Research o 11,8 %, CoreWeave o 10,1 % a Nvidia o 4,4 %.** AP za príčinu označuje obavy z rastúcich nákladov na úvery na výstavbu dátových centier a nákup čipov aj pochybnosti, že ceny akcií stúpli príliš vysoko, hoci firmy hlásili rast; Lam prekonal odhady a aj tak klesol. Akcie mimo AI sa držali a ropa Brent pre vojnu s Iránom zdražela o 4 % na 113 dolárov.
Zdroj: https://www.theguardian.com/business/2026/oct/22/stock-markets-drop-ai-oil

**SpaceX oceňuje získanie dlhu 40 miliárd dolárov približne na 8,3 % pre najnižšie hodnotenú tranžu a približne 7,75 % pre dlh krytý čipmi, viac než bod nad úrovňou obchodovania existujúcich dlhopisov.** Semafor 22. októbra exkluzívne s odvolaním na oboznámené osoby uvádza, že obchod vedený Apollom a Goldman Sachs odráža trh úverov na AI, ktorý sa po výpredaji dlhu CoreWeave „v posledných týždňoch prudko stiahol“, a že poistenie proti nesplateniu SpaceX zdraželo. Cena sa môže pred uzavretím budúci týždeň zmeniť.
Zdroj: https://www.semafor.com/article/10/22/2026/spacex-40b-debt-deal-will-cost-it-as-ai-fears-spread

**Tesla budúci mesiac rozšíri Cybercab do Dallasu a do konca roka ho začne predávať prevádzkovateľom flotíl, no list akcionárom teraz namiesto „platených“ kilometrov robotaxi zobrazuje „nesupervidované“.** TechCrunch 22. októbra upozorňuje, že list Tesly za druhý štvrťrok uvádzal kumulatívne platené kilometre robotaxi, pri ktorých podrobné čítanie ukázalo pokles o 36 % oproti prvému štvrťroku. List za tretí štvrťrok graf nahradil kumulatívnymi nesupervidovanými kilometrami. Finančný riaditeľ počet platených kilometrov neuviedol, povedal len, že „využitie sa zlepšuje“, a Musk tvrdí, že tržby nebudú výrazné až do druhého štvrťroka 2027.
Zdroj: https://techcrunch.com/2026/10/22/tesla-is-prepping-a-cybercab-onslaught/

**Firmy AI hovoria britským ministrom, že majú približne 12 mesiacov na získanie verejného súhlasu s dátovými centrami, kým výstavbu zablokuje odpor podobný americkému.** Podanie pracovnej skupiny Sovereign AI Leadership, v ktorej sú Nvidia, Microsoft, Cisco a ďalší, o ktorom Guardian informoval 22. októbra, tvrdí, že organizovaný miestny odpor zastavil plne povolené projekty v USA a že ho poháňajú ceny elektriny a nedôvera, nie samotná AI. Firmy žiadajú „dohodu“, ktorá by samosprávam umožnila ponechať si viac daňových príjmov od hostiteľov centier.
Zdroj: https://www.theguardian.com/uk-news/2026/oct/22/ai-firms-say-uk-has-a-year-to-head-off-datacentre-protests-before-construction-is-threatened

## Techniky promptovania

**Oddeľte pozorované fakty od interpretácie nástroja (r/PromptEngineering).** Opakovane použiteľný prompt na analýzu bezpečnostných upozornení vyžaduje päť častí: pozorované fakty, interpretáciu detekcie, možné vysvetlenia vrátane neškodných, chýbajúce dôkazy a predbežný záver. Zakazuje považovať názvy detekcií za potvrdené fakty alebo predpokladať, že zablokovaná akcia uspela. Autor tvrdí, že postup možno zovšeobecniť na financie, ladenie aj kontrolu dokumentov.
Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1xcd2tf/a_small_prompt_change_that_can_stop_ai_from/

**13 vzorcov kontextového inžinierstva pre dlhé behy programovacích agentov (r/PromptEngineering).** Praktické pravidlá jedného používateľa na spoľahlivejšie viachodinové relácie agentov: ponechať statické prefixy promptov rovnaké kvôli zľave za cache bez časových známok či počítadiel na začiatku, obmedziť výpisy adresárov na dve úrovne, pred úpravou zhutniť výsledky grep do päťriadkovej tabuľky, veľké výstupy zapisovať do pracovných súborov a čítať po rozsahoch riadkov, značkovať checkpointy v Gite a skracovať výstupy nástrojov limitmi head/tail. Viaceré body menujú vlastné nástroje autora; žiadny nepodporujú merania a údaj o cache je jeho tvrdenie.
Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1xcl3vm/13_context_engineering_lessons_learned_from/

**Testujte pokyny politiky zručnosti prípad po prípade (skillEd).** Autor open-source sady na hodnotenie opakovane použiteľných agentových zručností tvrdí, že pokyn „dodržuj pravidlá refundácie“ treba rozdeliť na samostatne overiteľné pravidlá, ako je lehota oprávnenosti, vylúčenie dopravy, zaokrúhľovanie a konzistentné vysvetlenie. Hraničné prípady a protipríklady sa majú napísať pred úpravou promptu a samostatné testovacie prípady až potom. Príklad refundácie v repozitári obsahuje výsledky pred a po; autor priznáva, že úspešné skóre nedokazuje pokrytie, a hľadá prípady, keď výstup prejde kontrolou, ale poruší pravidlo.
Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1xcz7uk/skilled_comparing_policyprompt_revisions_against/

## Čo ľudia tvoria

**Swift-1.5 Qwen3.8-27B v hipfire: na AMD 7900 XT približne 2,2-krát rýchlejší od začiatku do konca než llama.cpp.** Používateľ LocalLLaMA kvantizoval dolaďovanie Swift-1.5 modelu Qwen3.8-27B do formátu MQ4 prostredia hipfire a pribalil hlavu na predikciu viacerých tokenov pre špekulatívne dekódovanie. Na RX 7900 XT s 20 GB a ROCm 7.1 oproti Q4_K_S GGUF v llama.cpp uvádza 1,4- až 1,85-krát rýchlejšie predspracovanie, približne 1 100 tok/s pri kontexte 16K oproti asi 700, dekódovanie 36,5 tok/s na skutočných promptoch a 237 s oproti 530 s pri šiestich programovacích úlohách v Ruste.
Zdroj: https://huggingface.co/datayoda/Swift-1.5-Qwen3.8-27B-hipfire-MQ4

**Pull request llama.cpp prepracúva maticové enginy Intel XMX a približne zdvojnásobuje rýchlosť špekulatívneho dekódovania na Arc B70.** Merania používateľa na B70 so SYCL a modelom 30B Q6_K s konceptovým dekódovaním DFlash2 ukazujú pri rovnakých promptoch rast z približne 37–53 tok/s na 68–73 tok/s po zlacnení overovania tokenov. Dĺžka konceptu sa zvýšila, čo znižuje mieru prijatia, takže prínos pochádza z ceny overovania. Ide o otvorený pull request upstreamu, zrýchlenie teda ešte nie je vo vydaní.
Zdroj: https://github.com/ggml-org/llama.cpp/pull/29864

**Opposable: model 2B, ktorý ovláda aplikácie Android úplne v telefóne.** Aplikácia Android číta obrazovku cez službu dostupnosti, ťuká a píše. Môžu ju ovládať vzdialení agenti Claude, ChatGPT a Codex; bez pripojeného agenta beží rovnaká slučka lokálne v 4 bitoch cez llama.cpp na GUI-Owl 1.5 2B, dolaďovaní Qwen3-VL od tímu Mobile-Agent spoločnosti Alibaba. Jazykový model má 1,05 GB a obrazový enkóder 445 MB. Článok uvádza jeden krok za 7,3 s na CPU Mac M2 oproti 10,6 s predtým pri nezmenenej presnosti na testovacej sade 36 obrazoviek. Polovicu času spotrebuje obrazový enkóder, ktorý na NPU Galaxy S25 potrebuje 236 ms oproti 3,9 s na M2.
Zdroj: https://getopposable.com/blog/computer-use-on-the-phone

**Destilácia Kokoro TTS na jeden hlas, 50- až 100-krát rýchlejšia, natrénovaná v pivnici na 4070 Ti s prácou vykonanou modelom Opus.** Webový vývojár bez skúseností so strojovým učením požiadal Opus 5.5, aby podľa jasnej metriky iteratívne zlepšoval destilovanú jednohlasovú verziu modelu Kokoro na prevod textu na reč. Trénovanie na 4070 Ti Super trvalo približne deň. Cieľom je reč v reálnom čase na telefónoch a úsporných zariadeniach Android pre funkciu audioknihy na webe s románmi. Autor výsledok nazýva „Opus slop“, ale tvrdí, že v telefóne funguje.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xcuqor/making_kokoro_tts_50100x_faster_without_knowing/

**Handwired: kompilácia obyčajného JavaScriptu do presnej diferencovateľnej neurónovej siete bez trénovania.** Projekt Chenglou mení vetvenie, napríklad ternárny operátor, na dve ReLU a vážené súčty. Skompilovaný obvod preto presne reprodukuje kód na celých číslach, zostáva diferencovateľný a beží v prehliadači bez GPU. Stránka sama opisuje obmedzenia: konštrukcia je presná na deklarovanej celočíselnej mriežke, medzi bodmi interpoluje, napríklad 4,5 dá 11, a za hranicou 2^24 plus 6 ju narúša zaokrúhľovanie FP32.
Zdroj: https://chenglou.me/handwired/

**Open-XTTS-Trainer: chýbajúce fázy trénovania XTTS v2 po skončení Coqui.** Ponúka modulárnu trojfázovú sadu pre zvukový tokenizér, DVAE s annealingom codebooku Gumbel-Softmax, rozšírenie textu a slovníka o nové skripty Unicode, aby hindčina, arabčina, thajčina a ďalšie jazyky nezhadzovali pevný 17-jazykový tokenizér, a vokodér HiFi-GAN. Autor uvádza overenú konvergenciu straty na skutočnej reči a ukážku Colab na jedno kliknutie; opravil aj nekompatibility závislostí s moderným PyTorch.
Zdroj: https://github.com/amitbhakt/open-xtts-trainer

**agent-usage-guard: úprava Claude Code, ktorá zastaví rozvetvenie subagentov a náročné zmeny kontextu skôr, než minú päťhodinové okno.** Úprava číta živé percentá päťhodinového a týždenného limitu programu a zasahuje pred spotrebou pri štarte agenta, odoslaní promptu alebo volaní nástroja. Používateľa sa opýta vo vlastnom dialógu Claude Code; keď nikto nemôže odpovedať, požiadavku odmietne a modelu vysvetlí dôvod, aby mohol počkať alebo dávkovať. Po vypršaní promptovej cache a pri veľkom kontexte môže navrhnúť „zhutniť a potom odoslať“ a nad 80 % využitia obmedzí rozvetvenie agentov.
Zdroj: https://github.com/rbartoli/agent-usage-guard

**SCP: komunikačná vrstva, vďaka ktorej sa programovací agenti v rôznych prostrediach a na rôznych strojoch môžu rozprávať, usmerňovať a prebúdzať.** Swarm Communication Protocol umožňuje orchestrátoru v Claude Code spúšťať pracovníkov v Codex, OpenCode, pi, Muse, Agy alebo Grok, meniť ich smer počas behu a prijímať výsledky ako odovzdania. Správy dorazia po volaní nástroja, pri prompte alebo zastavení a hibernované relácie sa po správe prebudia. Dosah kopíruje strom procesov, kontakt medzi účtami vyžaduje vzájomný súhlas a voliteľný hodnotiteľ kontroluje, čo prechádza hranicou.
Zdroj: https://github.com/scphq/scp

**C-Sweet: open-source „firma riadená agentmi“ so sandboxovanými rolami malých modelov, ukázaná na lokálnom Qwen3.8 27B.** Autor tvrdí, že mnoho malých, úzko zameraných agentov s definovanými rolami môže na lokálnych modeloch vykonávať prácu firmy, a uvádza, že Qwen3.8 27B na RTX 6000 zvládol každú doteraz vyskúšanú podnikovú rolu. Aplikácia je opísaná ako open source a vhodná na vlastné hostovanie, každý agent má sandbox a SDK umožňuje písať nových agentov. Vlákno obsahuje video simulátora firmy.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xcvizk/i_made_a_business_simulator_i_can_hook_up_to_my/

**Lampline: hlasoví agenti na vlastnom hostovaní, ktorí importujú agentov Dialogflow CX a testujú ich volajúcim AI.** Tímom umožňuje tvoriť, testovať a prevádzkovať telefonických agentov na vlastnom počítači alebo serveroch, importovať agentov z Dialogflow CX a CX Agent Studio, používať 20 poskytovateľov modelov a bežať lokálne zadarmo bez kľúčov API. README uvádza približne 0,02–0,17 dolára za hovor oproti 0,50 dolára na hostovaných platformách; ide o údaj tvorcu, nie nezávislé meranie.
Zdroj: https://github.com/C4rohan/Lampline

**Domovskú obrazovku televízora Samsung nahradil spúšťač vytvorený pomocou Claude Code.** Autorovi prekážala domovská obrazovka plná reklám, a tak nechal Claude Code vytvoriť hodiny a spúšťač aplikácií i konzol. Užitočný postup: napodobniť niekoľko API televízora, od ktorých spúšťač závisí, aby sa rozloženie a ovládanie diaľkovým ovládačom dali iterovať v prehliadači notebooku. Potom pomocný nástroj prevezme tlačidlo Home úpravou nezdokumentovaných nastavení, uloží originály a pri zlyhaní ich obnoví.
Zdroj: https://github.com/NelsonEU/arn0-tv

**Demake Super Mario 64 pre Game Boy Advance, napísaný modelom Claude pod vedením človeka.** Autor vyberal smer a kompromisy a počas agentovej relácie s bezhlavým emulátorom nechal Claude písať kód, testy a nástroje. Kód pohybu a kolízií SM64 beží bitovo presne na 16,8 MHz ARM7 bez FPU, so štyrmi úrovňami a softvérovou 3D grafikou. Najzaujímavejší je dizajn: Claude vytvoril figurínu z elipsoidov, pretože obrys elipsoidu je vždy elipsa, ktorú dokážu vykresliť afinné sprity GBA.
Zdroj: https://github.com/Kodoque1/sm64-gba

**USB busylight prepojené s hooks Claude Code ako fyzický indikátor stavu.** Červená bliká, keď Claude pracuje, svieti načerveno, keď potrebuje vstup, a nazeleno, keď je nečinný. Autor použil starý Kuando Busylight a hooks Claude Code, aby nemusel kontrolovať druhú obrazovku. Je to malý trik, ale vlákno s viac než 100 komentármi ukazuje, že veľa ľudí rieši rovnaký problém agentov čakajúcich na neviditeľné „áno“, a uvádza vstavané alternatívy ako upozornenia na ploche a správy do telefónu cez /remote-control.
Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xcdwdx/i_got_tired_of_checking_whether_claude_code_needs/

## Stojí za prečítanie

**Stránky pomoci WhatsAppu skrývali pokyny, aby AI neodporúčala regulátora (redact.dev).** Tím výskumníkov súkromia prečítal všetkých 545 stránok prepojených z centra pomoci WhatsAppu a našiel 102 skrytých blokov na 80 stránkach. Na obrazovke sa nikdy nezobrazili, no boli v zdrojovom kóde. Dva prikazovali AI, aby po zmienke o právnikovi alebo právnom konaní neodporúčala orgán na ochranu údajov a necitovala GDPR, LGPD ani CCPA.
Zdroj: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions

**90 % pracovných hodín v USA pripadá na úlohy, ktoré benchmarky AI takmer nepokrývajú (Mercor).** Mercor namapoval 924 benchmarkov, zúžených na 29 nenasýtených agentových benchmarkov, na 923 povolaní O*NET a 18 797 úloh. Len 208 povolaní má úlohu s aspoň 5 benchmarkovými promptmi, 6 z 22 skupín povolaní nemá žiadnu a autori odhadujú, že približne 90 % amerických pracovných hodín pripadá na úlohy s malým alebo nulovým pokrytím.
Zdroj: https://www.mercor.com/research/labor-index/benchmark-map/

**Posttrénovanie agentov odmenami za stav databázy (Microsoft a Hugging Face, pokračovanie ThinkingBox).** Novinka v benchmarku ThinkingBox, o ktorom sme písali 3. októbra: rovnaká spustiteľná kontrola konečného stavu databázy sa použila ako odmena posilňovacieho učenia pri úlohách mimo benchmarku. Po 50 krokoch GRPO vzrástla priemerná úspešnosť Qwen3.8-27B z 51,70 % na 60,78 % a počet úloh zvládnutých vo všetkých 20 pokusoch z 38 na 107, kým počet úloh vyriešených aspoň raz klesol zo 453 na 446.
Zdroj: https://huggingface.co/blog/microsoft/thinkingbox-training

**Most k infraštruktúre Git pre agentov vo veľkom meradle (GitHub Engineering).** GitHub tvrdí, že 99,99999 % repozitárov je dnes zároveň v jeho dátových centrách aj v Azure, ktoré obsluhuje približne polovicu prevádzky Git. Dôvodom je rast prevádzky v ére agentov a limity napájania dátových centier. Zostávajúce najvyťaženejšie repozitáre brzdí serializácia zápisov cez 25 ms spiatočnú cestu medzi regiónmi.
Zdroj: https://github.blog/engineering/architecture-optimization/the-bridge-to-agent-scale-git-infrastructure/

**Každý model AI dáva rovnaký „kontroverzný“ názor na ľudí (ModelCompare).** V malom experimente dostalo 12 modelov z desiatich laboratórií v troch krajinách po trikrát otázku na ich najkontroverznejší názor na ľudí. V 29 z 35 odpovedí zaznelo jedno tvrdenie: ľudia uprednostňujú príslušnosť pred pravdou a dôvody si vymýšľajú dodatočne. Sedem z 12 modelov ho uviedlo zakaždým a Grok 4.7 raz odmietol odpovedať. Dôkazy sú slabé, ide o 36 promptov s jediným znením a bez variácií, no experiment dobre ukazuje, ako modely konvergujú, keď majú pôsobiť provokatívne.
Zdroj: https://www.modelcompare.ai/blog/ai-models-controversial-take-on-humans

**Pýtať od LLM skóre istoty je zlý nápad (Amrut Joshi).** Argument je jednoduchý: číslo istoty má význam iba vtedy, keď je kalibrované podľa výsledkov a reaguje na dôkazy, a vlastné skóre LLM nespĺňa ani jedno. Preformulovanie otázky na „Ste si istý?“ posunie číslo bez novej informácie a skóre nadväzujúce na skoršie sebavedomé znenie odzrkadľuje text, nie dôkazy.
Zdroj: https://rumple.github.io/blog/2026/10/20/asking-llm-for-confidence.html

**Inside the Event Horizon: prejav Jacka Clarka v MMF (Import AI 477).** Spoluzakladateľ Anthropic Clark tvrdí, že singularita sa začala, pretože AI už pôsobí na hranici vedy, a ekonómom MMF hovorí, aby očakávali zrýchlenie výskumu, nie iba AI. Ako dôkazy uvádza rast Humanity's Last Exam z 8 % v januári 2025 na 67,7 % pri Claude Opus 5.5, FrontierMath z 2 % na 94 %, deklarované príspevky AI k otvoreným matematickým problémom a takmer 10-krát viac kódu na výskumníka v spoločnosti Anthropic.
Zdroj: https://importai.substack.com/p/import-ai-477-in-which-i-tell-the

**AI and the Enclosure of the Scientific Commons (arXiv).** Astrofyzik s úvodom do histórie anglickej spoločnej pôdy tvrdí, že AI poskytuje nástroje na privatizáciu vedeckej literatúry ako „informačnej občiny“, podobne ako hnutie ohradzovania približne v rokoch 1600–1800 privatizovalo poľnohospodársku pôdu. Podľa práce vysvetľuje zánik občín ohradzovanie, nie „tragédia spoločného“.
Zdroj: https://arxiv.org/abs/2610.27251

**Practical AI: vývoj exploitov, agentové vyhľadávanie zraniteľností a falošné PoC.** Moderátori Daniel Whitenack a Chris Benson hovoria so Spencerom McIntyreom z VulnCheck o tom, ako sa agenti používajú na hľadanie zraniteľností, prečo mnohé ukážkové exploity nefungujú, o hraniciach zneužívania s pomocou AI a o ochranných mechanizmoch, ktoré komplikujú prácu bezpečnostným výskumníkom. Téma je aktuálna po tohtotýždňovej sérii bezpečnostných incidentov s pomocou AI.
Zdroj: https://share.transistor.fm/s/9a42098b

## Hacker News

**„Som vo vojnovom režime“: Terry Tao a kríza matematiky.** Profil Terenca Taa v NYT cez archívny odkaz o jeho reakcii na dôkazy vytvorené AI. Reakcie odborníkov sa rozchádzajú: jeden komentujúci to číta ako stratu výhody matematikov byť „najinteligentnejší v miestnosti“, iný označuje Taov postoj za sebecký, keď teraz AI pomáha špecialistom rovnako ako generalistom, čo je neoverené tvrdenie o motivácii. Tretí poznamenáva, že automatizácia prišla najprv z konca znalostnej práce, nie manuálnej.
Zdroj: https://news.ycombinator.com/item?id=50118165

**WorldTUI: natrénoval som model 360M, aby predstieral terminál.** Malý doladený model vykresľuje výstup terminálu snímku po snímke a má živú ukážku. Komentujúci sa pýtajú, čo odlišuje model predpovedajúci hodnoverný výstup od jeho skutočného výpočtu. Jeden v názore vidí generované používateľské rozhrania ako dlhodobý smer, ak budú malé lokálne modely dosť rýchle.
Zdroj: https://news.ycombinator.com/item?id=50190363

**OpenAI CLI.** Vlákno o novom nástroji OpenAI pre príkazový riadok. Podstatná je reakcia: používatelia považujú produktový rad vedľa Codexu za neprehľadný a jeden varuje, že OpenAI ruší nástroje približne do dvoch rokov, niekedy bez upozornenia; ide o neoverenú anekdotu.
Zdroj: https://news.ycombinator.com/item?id=50191507

**Maximalizovanie tokenov skončilo, používanie tokenov OpenRouter sa ustálilo.** Vlákno o plató vo verejnom rebríčku tokenov OpenRouter. Užitočná oprava od komentujúceho: dáta OpenRouter sú zaujaté smerom k ľuďom, ktorí striedajú modely a uprednostňujú otvorené váhy, a nezverejňujú počet unikátnych používateľov, takže o širšom trhu hovoria málo.
Zdroj: https://news.ycombinator.com/item?id=50159464

**Ask HN: Ak sú modely také dobré, prečo OpenAI jednoducho nezaloží 100 firiem?** Krátke nové vlákno o stratégii laboratórií. Odpovede: laboratóriá už vydávajú množstvo aplikácií, predaj tokenov cez dlho bežiacich agentov je preukázateľne rastúci príjem a platforma, ktorá si berie podiel, sa vyhýba podnikateľskému riziku, podobne ako App Store.
Zdroj: https://news.ycombinator.com/item?id=50200997

## Reddit

**Šetrí delegovanie kvótu Claude? Zmeral som 6 zostáv na 28 skutočných úlohách (r/ClaudeAI).** Autor benchmarkoval odovzdávanie práce Claude Code lacnejším modelom a zverejnil repozitár aj metódu. Podľa neho samotný Haiku 5.5 zvládol všetkých 84 kontrol pri približne o 91 % nižšej cene než samotný Sonnet. Subagent Haiku pod Sonnetom bol lacnejší o 13 %, pri ťažších úlohách o 55 %. Odovzdanie práce DeepSeek V4.1 Flash alebo lokálnemu 27B cez nástroj MCP stálo približne rovnako alebo viac, pretože písanie a kontrola špecifikácie zaťažujú orchestrátor.
Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xclm8k/does_delegating_save_claude_quota_i_measured_6/

**Oslabili Opus 5.5? LiveNerf, aktualizácia 29. dňa (r/ClaudeAI).** Významná aktualizácia sledovania zo skorších briefingov: po 29 po sebe idúcich dňoch projekt neuvádza merateľný pokles Opus 5.5 a dokáže zachytiť zmenu aspoň 6,6 bodu. Podľa automatického zhrnutia vlákna sa komunita zhoduje, že schopnosti sú stabilné. Najviac podporovaná sťažnosť však tvrdí, že limity sa míňajú rýchlejšie; niektorí vinia nafúknutý kontext a pár ľudí stále podozrieva benchmark z manipulácie, čo zostáva neoverené.
Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xcraz9/did_they_nerf_opus_55_doesnt_look_like_it/

**Claude vážne potrebuje program za 50 dolárov mesačne medzi Pro a Max (r/ClaudeAI).** Diskusia o cenách. Podľa zhrnutia vlákna je medzera zámerná, pretože úroveň za 50 dolárov by stiahla predplatiteľov zo 100-dolárovej. Cynický najvyšší komentár tvrdí, že „50 dolárov“ by bol dnešný 20-dolárový program po obmedzeniach, a bežným riešením je druhý účet za 20 dolárov.
Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xcle8t/claude_seriously_needs_a_50month_plan_between_pro/

**Mám odpoveď! Qwen Flash Next IQ2 je pre mňa lepší než Q8 27B (r/LocalLLaMA).** Praktické a výslovne subjektívne porovnanie na nenápadných programovacích chybách. Ďalší používateľ potvrdzuje porovnanie NVFP4; skeptik odpovedá, že benchmarky aj jeho testy ukazujú časté zlyhania Q2, a žiada príklady.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xc7n0n/i_have_an_answer_qwen_flash_next_iq2_is_better/

**DeepSeek a MiniMax splnili čínske pravidlá vývozu AI pre zahraničné open-source vydania (r/LocalLLaMA).** Autor sprostredkúva čínske médiá Yuyuan Tantian, teda sekundárny a neoverený zdroj, podľa ktorých obe firmy dokončili podania podľa dočasných pravidiel vývozu AI z Číny, čo má umožniť pokračovanie vydávania otvorených váh. Komentujúci sa pýtajú na Zhipu a upozorňujú, že prvé návrhy architektúr GLM-5.3-Flash a Qwen3.8-Flash-Next sa už vydávajú.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xcoelw/deepseek_and_minimax_clear_chinas_ai_export_rules/

**Q4 flash next za 300/600 libier – nové výsledky mini PC Snapdragon (r/LocalLLaMA).** Merania na mini PC Snapdragon X s 32 GB pomocou zatiaľ nezverejneného vlastného enginu autora: približne 315/43 tok/s pri predspracovaní/dekódovaní na modeli A3B a 46 tok/s pri predspracovaní väčšieho modelu. Komentujúci upozorňujú na pomalé predspracovanie, keď 8k prompt za studena trvá približne 3 minúty, a navrhujú uložiť systémový prompt do cache na SSD.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xcmioz/q4_flash_next_for_300600_snapdragon_mini_pc/

**Má ešte niekoho obavy z bezpečnosti implementačných enginov? (r/LocalLLaMA).** Diskusia o dôvere v inferenčné enginy. Najlepšie odpovede presúvajú riziko z enginu na jeho strom závislostí; podľa komentujúceho mal LiteLLM v posledných mesiacoch dva závažné bezpečnostné incidenty. Spomínajú aj ekosystémy Python a Node.
Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xcu4or/is_anyone_else_concerned_about_the_security_of/

**Popredné modely zle počujú ASMR: 8 hodnotiteľov proti ľudským značkám na 480 klipoch (r/MachineLearning).** Tvorca testoval zvukové modely ako značkovače pre dataset so 126 000 klipmi. Najlepší hodnotiteľ Gemini 3.1 Pro dosiahol oproti ľudským značkám F1 0,325 pri spúšťačoch. Claude Opus 5.5 a Grok 4.7 so spektrogramami dosiahli približne 0,12 a 0,11. Šepot bol ľahký s F1 0,70–0,79, no fyzické zvuky ako papier či kefovanie modely zväčša prehliadali a čisté zvukové efekty nepredpovedali výkon na skutočnom ASMR.
Zdroj: https://old.reddit.com/r/MachineLearning/comments/1xcbqdm/frontier_models_are_bad_at_hearing_asmr_8_judges/

## YouTube

**Lepšie modely AI neopravujú váš technický tím.** Nicholas Arcolano, vedúci AI a výskumu v Jellyfish, používa dáta približne 50 000 inžinierov v 447 firmách a skúma, ako model ovplyvňuje výstup programovania s AI. Podľa neho sa po presune mnohých používateľov Cursor na Grok počet zlúčených pull requestov takmer nezmenil. Nástroju pripisuje menej než 1 % rozptylu produktivity, používaniu zručností približne 3 %; intenzívni používatelia zručností dosahujú asi +30 %. Spotrebe tokenov pripisuje asi 9 %, firme a tímu asi 12 % a väčšinu zvyšku jednotlivému inžinierovi. Najlepší pracovníci spred AI väčšinou zostali na vrchole.
Zdroj: https://www.youtube.com/watch?v=Ve2bAarPA2I

**1 368 zlyhaní AI a čo nás učia o hodnoteniach.** Vishal Srivastava a Tanmay Sah z New York Life analyzujú 1 368 incidentov z verejnej databázy incidentov AI a triedia ich do troch oblastí a 13 podoblastí pokrývajúcich približne 98 % prípadov. Uvádzajú, že slabé kontroly pri nasadení, ľudská kontrola a monitorovanie, najviac súvisia so škodou. Navrhujú radiť prípady použitia podľa významnosti a cyklus hodnotenia build-break-fix, ktorý sa systém snaží vyvrátiť; ukazujú ho na chatbote aerolinky, ktorý uviedol nesprávne pravidlá refundácie.
Zdroj: https://www.youtube.com/watch?v=mMw3arwQsL0

**Ako testovať agentov AI, keď neexistuje benchmark.** Nathanael Weill, ktorý vedie tím agentov v Air Canada, odporúča najprv napísať odpoveď: začať známym výsledkom, z neho vytvoriť vstup a skontrolovať, či ho agent obnoví. Tvrdí, že projekt RAG sa tak posunul z jedného expertne hodnoteného testu týždenne na desiatky automatických testov denne. Pre agenta na kontrolu dodávateľských zmlúv uvádza päť zdrojov testov: minulé rozhodnutia, vložené porušenia pravidiel, odstránené klauzuly, nepodstatné zmeny a vyplnené šablóny.
Zdroj: https://www.youtube.com/watch?v=c_SPW__jF9w

**Prečo text AI stále pôsobí ako odpad.** Louis-François Bouchard z Towards AI opisuje benchmark svojho tímu na overenie, či model dokáže písať scenáre videí jeho hlasom: 10 scenárov, 5 návrhov na model, 4 hodnotiace LLM, deväť metrík a 1 000 ľudských porovnaní A/B. Uvádza, že hodnotitelia uprednostňujú vlastnú rodinu modelov, a radí používať veľmi dlhé prompty s príkladmi, jedno kontrolné kolo silným modelom, veľa lacných návrhov spojených do jedného a ľudskú úpravu.
Zdroj: https://www.youtube.com/watch?v=_dTF3NpPzGo

**Ako budú vyzerať počítačové čipy v roku 2045? Prehliadka továrne Intel.** Dwarkesh Patel strávil dva dni v najpokročilejšej továrni Intelu a robil rozhovory s technickým vedením. Animácie vysvetľujú tranzistory gate-all-around, zadné napájanie, CFET a hybridné spájanie. Uvádza vyjadrenie technického riaditeľa Intelu, že výpočtový výkon AI desať rokov rástol približne 3-násobne ročne, kým Intel by s dnešným globálnym množstvom nástrojov na výrobu čipov dokázal iba zdvojnásobiť produkciu waferov na špičkovom procese. Pýta sa, ako môžu továrne túto medzeru preklenúť.
Zdroj: https://www.youtube.com/watch?v=frYSOKvNiiE

**Prečo výpočtový výkon AI prichádza v obdĺžnikoch.** Generálny riaditeľ Modal Erik Bernhardsson pre Latent Space vysvetľuje, ako Modal združuje kapacitu GPU a škáluje inferenciu, prečo predaj kapacity v trojročných blokoch zle sedí záťažiam AI a ako uvažuje o finančnom riziku poklesu cien GPU a nekonečnosti dopytu po AI. Rozhovor sa venuje aj alternatívam k Nvidii, rýchlemu rastu sandboxov agentov, ich bezpečnosti a dôvodom, prečo má Modal kontrolu kódu voliteľnú.
Zdroj: https://www.youtube.com/watch?v=IiZ9yd2Do8I

**Kryptografický pohľad na problémy dôveryhodnosti strojového učenia.** Laureátka Turingovej ceny Shafi Goldwasser predniesla v angličtine Munich AI Signature Lecture v Bavorskej akadémii vied. Podľa opisu ukazuje, ako kryptografia a interaktívne dôkazy riešia problémy dôveryhodnosti vo viacerých fázach procesu strojového učenia a odpovedajú, či možno dôverovať systémom, ktorých správnosť sa nedá ľahko overiť.
Zdroj: https://www.youtube.com/watch?v=CQ9m04n2oSo

**Od modelov sveta k agentom sveta (Stanford EE292R).** Gordon Wetzstein zo Stanfordu prednáša o video modeloch sveta: zlepšení časovej konzistentnosti a uvažovania v dlhom kontexte, obmedzení autoregresívneho driftu, dynamike viacerých agentov a podmieňovaní i ovládaní zameranom na človeka. Ide o kurzovú prednášku pre záujemcov o stav výskumu video modelov sveta, hodnotenú podľa opisu, nie prepisu.
Zdroj: https://www.youtube.com/watch?v=IfkeGU4bEJI

**Nový vrcholový predátor: generálny riaditeľ CrowdStrike George Kurtz o protivníkoch vyzbrojených agentmi AI.** Sarah Guo a Elad Gil robia rozhovor s Georgeom Kurtzom. Tvrdí, že agenti splošťujú pyramídu protivníkov tým, že útočníkom s nízkou kvalifikáciou poskytujú pokročilé postupy, a najrýchlejšie útoky dnes trvajú sekundy. Témy zahŕňajú otvorené a uzavreté modely v bezpečnosti, destiláciu modelov, poučenia z nedávneho incidentu Hugging Face a úsilie CrowdStrike a Nvidie trénovať bezpečnostné modely.
Zdroj: https://www.youtube.com/watch?v=PST8yesYOSo

**Dá sa ChatGPT dôverovať pri zdraví?** Karan Singhal z OpenAI hovorí partnerovi a16z Jayovi Rughanimu, že viac než 300 miliónov ľudí používa ChatGPT na zdravotné otázky každý týždeň. Vysvetľuje, prečo OpenAI trénuje medicínske znalosti do všeobecných popredných modelov, ako stovky medicínskych expertov hodnotia bezpečnosť a nezhody a prečo firma opisuje AI ako doplnok lekárov. Rozhovor sa venuje aj integráciám Epic, kopilotom pre klinikov, problému duševného zdravia a 5- až 17-ročnému oneskoreniu medicínskeho konsenzu.
Zdroj: https://www.youtube.com/watch?v=9n0MI4D7TCM

**Linus Torvalds zúri pre AI (c't 4004 #44).** Týždenná diskusia c't 3003 s Christianom Lutz-Weickenom a Janom-Kenom Janssenom. Názov odkazuje na e-mail Linusa Torvaldsa do mailing listu kernelu o AI. Opis prepája aj materiály o lokálnej inferencii, kvantizácie Qwen3 od Unsloth, vlákno Redditu o stave lokálnej inferencie, projekt Strata, a vyhlásenie o bezpečnostnom incidente OpenCode so správou TechCrunch.
Zdroj: https://www.youtube.com/watch?v=5YG2SJ9zISI

**Zabúdame myslieť? (Lanz + Precht, diel 267).** Markus Lanz a Richard David Precht diskutujú o tom, čo sa stane s porozumením a samostatným myslením, keď AI okamžite odpovie takmer na každú otázku, či sa myslenie presúva na stroje a či je Prechtova obava z plazivej erózie kultúry oprávnená. Ide o názor a špekuláciu dvoch komentátorov, nie výskum; dátum je na hranici časového okna, pred 6 dňami 16. októbra.
Zdroj: https://www.youtube.com/watch?v=78s2z_8ts28

**Naozaj myslíme slovami? Zoomposium s Nikolou Kompom.** Zoomposium robí rozhovor s Nikolou Kompom, profesorom teoretickej filozofie na Univerzite v Osnabrücku, o vnútornej reči, situovanom poznávaní a vtelení, o rozdiele medzi štatistickým spracovaním vzorcov v LLM a skutočným jazykovým porozumením a o tom, či mozog počíta ako počítač. Anglický opis je strojovo preložený; zvuk je pravdepodobne v nemčine, no nie je to potvrdené.
Zdroj: https://www.youtube.com/watch?v=QqaNMBWg8Lc

**Varovný výstrel. Vyhubí nás AI? (Jiří Charvát).** Český komik a lektor Jiří Charvát vystupuje na festivale CERNA.AI o nedávnom útoku zblúdených agentov AI na Hugging Face, ktorý rámcuje ako nesúlad cieľov, nie vzburu. Hovorí aj o odstúpení Jacoba Coxona, vyjadreniach Evana Hubingera, odhadoch p(doom) popredných osobností, európskom AI Act a českom dozornom orgáne. Ide o popularizačný a sčasti humorný pohľad; kapitoly uvádzajú témy a tvrdenia patria rečníkovi.
Zdroj: https://www.youtube.com/watch?v=yyeRvPn6cuI

**Ako veľmi veriť agentom AI? Debata o Agentic AI, platbách a bezpečnosti.** Odborníci z VISA, Apify a Amdocs v sérii Innovation Week a BusinessInfo.cz diskutujú, čo agenti skutočne robia v produkcii a kde zlyhávajú, prečo väčšina pilotov nedosiahne produkciu, kto môže prehrať, prečo podľa nich ešte neexistuje spoľahlivá oprava prompt injection, kto zodpovedá za chybnú platbu agenta a ako sa ceny presúvajú z hodín na výsledky. Zhrnutie vychádza z opisu a panelisti zastupujú dodávateľov.
Zdroj: https://www.youtube.com/watch?v=XdJJOsuAz-4

## Stručne

**Microsoft: čínsky štátny aktér Storm-0940 použil open-source rámec agentov AI ARTEX pri útoku na dodávateľský reťazec ConnectWise a proti stovkám organizácií; privilegovaný prístup do cloudu získal za menej než tri hodiny.** Microsoft uvádza, že ARTEX, rámec v Go umožňujúci pripojiť ľubovoľný model AI a vykonať penetračný test od prieskumu po exfiltráciu s malým ľudským vstupom, vykonával password spraying a zneužívanie aplikácií OAuth „rýchlosťou stroja“. Pokusy zasiahli viac než 2 250 tenantov pri 2 900 prihláseniach za minútu a jedna kampaň medzi 10. a 14. októbrom mala viac než 151 000 neúspešných prihlásení. Ciele od septembra zahŕňajú obranu, letectvo, financie, energetiku, vládu a polovodiče. Väčšina pokusov zlyhala, no niekoľko dosiahlo privilegované pretrvanie v cloude za menej než tri hodiny.
Zdroje: https://therecord.media/china-cyber-connectwise-ai, https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html

**Príčina incidentu LiteLLM: token GitHub unikol cez logy brány AI; Railway a Andromeda hlásia súvisiace krádeže prihlasovacích údajov zamerané na poskytovateľov inferencie AI.** LiteLLM, o ktorom sme písali 22. októbra, teraz uvádza, že útočník prekonal „viaceré nezávislé bezpečnostné kontroly“ a pravdepodobne získal token GitHub z logov brány. Otrávený balík 1.107.0 bol na PyPI asi 1 hodinu 44 minút od 11:39 do 13:23 UTC a v obrazoch Docker do 14:20 UTC; spúšťal zlodeja údajov aj hodinový načítavač vzdialeného kódu. Railway samostatne tvrdí, že narušiteľ mohol čítať dešifrované premenné prostredia zákazníkov vrátane kľúčov API a zrejme išlo o sériu útokov na platformové firmy s cieľom dostať sa k poskytovateľom inferencie AI. Výskumník incident spája s vykrádaním peňaženiek.
Zdroje: https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html, https://thehackernews.com/2026/10/railway-says-intruder-may-have-accessed.html, https://thehackernews.com/2026/10/threatsday-ai-secrets-leak-pingcap.html

**Kernel Linuxu: zistenia skenera AI Trend Micro ZDI sa dostali do verejného mailing listu pred opravami; dve chyby servera SMB s CVSS 9.0 nemajú opravu v hlavnej vetve.** ZDI pripísal hlásenia o KSMBD svojmu skeneru AI TrendAI, jednu chybu typu race condition pred autentifikáciou a jedno celočíselné podtečenie RDMA, a spolu s ďalšími ich poslal do verejného zoznamu kernelu. Phoronix to označuje za nehodu; The Hacker News upozorňuje, že dokumentácia kernelu z mája 2026 podľa odporúčania Linusa Torvaldsa považuje chyby nájdené AI za už verejné.
Zdroje: https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html, https://www.phoronix.com/news/LKML-New-Trend-Vulnerabilities

**Programovací agent OpenCode: škodlivý server MCP mohol počas prihlasovania spustiť PowerShell na počítači vývojára; chyba bola potichu opravená 28. septembra bez CVE.** Pillar Security zistil, že vo Windows a WSL sa autorizačná adresa OAuth dodaná serverom MCP odovzdávala bez escapovania do príkazu PowerShell. Navrhované skóre je 9,8. Zasiahnuté sú verzie 1.0.137 až 1.18.32 a opravená je 1.18.33. Anomaly nepožiadala o CVE ani nezverejnila upozornenie, preto skenery staré zostavenia neoznačia.
Zdroj: https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html

**MuTRAP: plánovací LLM so zadnými vrátkami dokáže pri spúšťacích slovách prepnúť robota z bezpečných na škodlivé pokyny; navrhuje sa obrana PROTEA s hodnotiacim LLM.** Výskumníci Binghamton University dolaďujú do LLM na plánovanie úloh zadné vrátka viazané na viaceré spúšťacie slová. Testovali ich na dátach VirtualHome s modelmi od GPT-2-large po Llama-3.1-8B a ukazujú simulovaný plán s mačkou na sporáku aj kolesového robota napodobňujúceho rezanie modelovej ruky. Hrozbou je model doladený treťou stranou, ktorý robotické firmy kupujú namiesto vlastného trénovania.
Zdroj: https://www.theregister.com/ai-and-ml/2026/10/22/backdoored-robot-tries-its-hand-at-finger-chopping-and-cat-cooking/5304870

**Meta po úniku verejných odkazov znovu povoľuje zdieľanie Muse s novými URL.** Meta tvrdí, že chyba bola v URL zdieľaných artefaktov, dokumentov a obrázkov, ktoré sa pomenovali podľa názvov konverzácií a zapisovali do verejného DNS. Výskumníci tak našli kontrolu tržieb firmy aj žiadosť o úver. Staré odkazy teraz žiadajú autora zdieľania, aby vytvoril nový.
Zdroj: https://www.theverge.com/tech/1017066/meta-muse-sharing-back-on-artifiacts

**Prvý človek dostal bakteriofágy navrhnuté AI v režime súcitného použitia od Radical Numerics; výsledok nebol zverejnený.** Firma tvrdí, že model Omnii-1 navrhol varianty fágov, ktoré in vitro odstránili pacientov izolát odolný proti antibiotikám, a koktail sa potom podal v režime súcitného použitia. Klinický výsledok nebol publikovaný a firma neodpovedala The Register.
Zdroj: https://www.theregister.com/science/2026/10/22/human-receives-ai-designed-virus-for-the-first-time/5304874

**Ministerstvo financií USA navrhuje pravidlá odchádzajúcich investícií pre systémy AI, polovodiče, kvantové technológie, vysokovýkonné výpočty a hypersoniku a pridáva biotechnológie.** Oznámenie o navrhovaných pravidlách vykonáva zákon COINS prijatý v obrannom rozpočte FY2026: americké osoby musia oznamovať transakcie s „dotknutými zahraničnými osobami“ v oznamovaných technológiách alebo ich majú zakázané, podľa technických parametrov sektora. Ministerstvo pridalo biotechnológie z vlastnej právomoci.
Zdroj: https://home.treasury.gov/news/press-releases/sb0667

**Dvojstranný návrh zákona v Snemovni reprezentantov AI Cyber Defense Act by poveril NIST vytvorením dobrovoľných štandardov proti destilácii modelov Ruskom, Čínou, Iránom a Severnou Kóreou.** Poslanci Harrigan a Whitesides tvrdia, že destilácia umožňuje rivalom zaostať za americkými laboratóriami iba o šesť až 12 mesiacov pri 5–10 % nákladov.
Zdroj: https://cyberscoop.com/bipartisan-bill-combat-ai-distillation-attacks-nist/

**Texas vypína portál povolení a pozastavuje 17 povolení na odvádzanie dažďovej vody pre dátové centrá po správe, že ich schvaľoval napriek septembrovej pauze guvernéra.** Organizácie FracTracker a Public Citizen uviedli viac než dve desiatky povolení vrátane lokalít OpenAI a Amazonu vydaných v pondelok a utorok. Úrad tvrdí, že všetky žiadosti teraz pracovníci skontrolujú na prepojenie s dátovými centrami.
Zdroj: https://www.404media.co/texas-commission-on-environmental-quality-portal-down/

**Meta po odpore vydavateľov upravuje nové obchodné podmienky, právni experti však tvrdia, že naďalej umožňujú trénovanie na obsahu stiahnutom z webov.** Podmienky účinné od 30. októbra umožňujú Mete používať obsah webov prepojených s firemným účtom na „vývoj“ obchodných produktov. Slovo „trénovať“ odstránila, no profesor práva z Cornellovej univerzity a mediálny právnik tvrdia, že „vývoj“ ho zahŕňa a môže prekonať robots.txt. Meta tvrdí, že nejde o sťahovanie spravodajstva.
Zdroj: https://www.theverge.com/tech/1017082/meta-terms-update-ai-training-concerns

**Micron po dvoch desaťročiach výskumu opúšťa DRAM 4F² a tvrdí, že neprináša významný nárast hustoty.** Bunka 4F² sľubuje o 33 % menšiu plochu než 6F², teoreticky približne o 50 % viac buniek na wafer, technický riaditeľ Micronu však tvrdí, že náklady a zložitosť prínos prevážia. Samsung a SK hynix ju stále uvádzajú v plánoch. Pre dodávky HBM a DRAM, od ktorých závisí AI, to znamená, že traja výrobcovia sledujú odlišné plány.
Zdroj: https://www.tomshardware.com/pc-components/dram/micron-pulls-the-plug-on-future-4f2-dram-after-two-decades-of-research-in-dramatic-shift-company-says-architecture-offers-no-meaningful-density-advantages-increases-manufacturing-complexity-and-costs-and-has-fundamental-scaling-limitations

**TSMC žiada dodávateľov zariadení o nástroje bez čínskych magnetov zo vzácnych zemín.** Podľa Reuters cez Tom's Hardware chce TSMC motory na automatizáciu tovární bez vzácnych zemín, pretože Čína ovláda približne 90 % rafinácie a asi 95 % hotových permanentných magnetov a od apríla 2025 povoľuje ich vývoz licenciami. Popredný výrobca čipov pre AI sa poisťuje proti úzkemu miestu dodávateľského reťazca.
Zdroj: https://www.tomshardware.com/tech-industry/semiconductors/tsmc-is-seeking-chipmaking-equipment-that-doesnt-contain-chinese-rare-earth-magnets-asks-suppliers-to-provide-alternative-motors-as-export-controls-threaten-fab-operations

**Counterpoint: dodávky počítačov v treťom štvrťroku pre ceny pamätí medziročne klesli o 21 % a vo štvrtom sa očakáva pokles o 27 %.** Zdraželi RAM, SSD aj čipy, výrobcovia obnovujú DDR4 a GPU so 4 GB a smartfóny dosiahli 14-ročné minimum. Dôležité je to ako spotrebiteľská cena dopytu AI po pamätiach: hardvér na lokálnu AI zdražuje.
Zdroj: https://www.theverge.com/gadgets/1017144/global-pc-shipments-dropped-q3-2026-ram

**Nvidia Minerva: platforma AIOps, ktorá mapuje GPU, switche a úlohy do znalostného grafu a hľadá zlyhávajúce súčasti tovární AI.** Nvidia tvrdí, že analyzuje miliardy dátových bodov za hodinu, zoskupuje záplavy udalostí do incidentov s pravdepodobnou príčinou a ponúka asistenta aj API na automatizáciu. Ide iba o tvrdenia o produkte; príspevok neobsahuje benchmarky ani dátum dostupnosti.
Zdroj: https://blogs.nvidia.com/blog/minerva-platform-infrastructure/

## Biznis v skratke

**OpenAI podľa správ získava až 30 miliárd dolárov pri valuácii 1,25 bilióna dolárov pred investíciou, od Coatue a investorov zo SAE, možno v súvislosti s výpočtovou kapacitou v SAE. Je to pokles oproti 1,4 bilióna spomínaným pred mesiacom; dokumenty k IPO boli dôverne podané v júni.**
Zdroj: https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/

**DeepSeek podľa správ získal približne 15 miliárd dolárov, medzi investormi sú podľa Bloombergu CATL a Tencent, dva dni po nariadení americkým civilným úradom odstrániť jeho technológiu.**
Zdroj: https://techcrunch.com/2026/10/22/deepseek-reportedly-raises-15b-days-after-us-restrictions/

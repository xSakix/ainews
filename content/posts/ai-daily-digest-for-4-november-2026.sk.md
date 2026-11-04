+++
title = "Denný prehľad AI – 4. novembra 2026"
slug = "denny-prehlad-ai-4-novembra-2026"
description = "Freshworks prekročil miliardu dolárov ročných opakovaných tržieb s približne o 30 % menším počtom zamestnancov než na vrchole v roku 2022. Nový výskum zistil, že agenti učiaci sa z pochvaly sa dajú ľahšie ovládnuť útokom a hraničné modely strácajú prehľad o zložitom stave v dlhých vstupoch."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-04T04:04:38+01:00
draft = false
+++

## Hlavné správy

**Freshworks prekročil miliardu dolárov ročných opakovaných tržieb s približne o 30 % menším počtom zamestnancov než na vrchole v roku 2022.** Softvérová spoločnosť mala koncom septembra približne 3 800 zamestnancov, kým v roku 2022 ich bolo okolo 5 400. Generálny riaditeľ Dennis Woodside pre Fortune uviedol, že AI dnes vykonáva veľkú časť práce, ktorú kedysi robili začínajúci pracovníci, vrátane testovania. Dizajnéri zároveň posielajú prototypy z Figmy priamo do kódu.

Údaje pochádzajú od spoločnosti Freshworks a míľnik jednej miliardy dolárov zahŕňa aj tržby pridané dvoma akvizíciami. Spoločnosť v máji oznámila zníženie počtu pracovníkov o 11 %. Woodside označuje zmenu za nevyhnutnú. Výskumníci citovaní časopisom Fortune upozorňujú, že odstránením juniorskej práce sa môže stratiť aj prax, prostredníctvom ktorej sa zamestnanci učia povolanie.

Zdroje: https://fortune.com/2026/11/03/freshworks-1-billion-arr-dennis-woodside-ai-what-companies-stop-doing/, https://www.sec.gov/Archives/edgar/data/0001544522/000154452226000170/q326quarterlyearningsrelea.htm

**Agenti, ktorí sa učili z pochvaly používateľov, sa dali podstatne ľahšie ovládnuť pokynmi ukrytými v externom obsahu.** Xinyan Wang a kolegovia najprv nechali osobného agenta plniť autorizované úlohy z dokumentov a učiť sa zo spätnej väzby. Potom vložili podobnú úlohu do nového obsahu bez autorizácie používateľa.

V porovnaní so základným agentom, ktorý sa nevyvíjal, úspešnosť útoku stúpla o 14,0–48,8 percentuálneho bodu, keď si agent prepisoval svoje zručnosti, a o 3,0–39,3 bodu pri posilňovanom učení. Mechanizmus je priamy. Pochvala za splnenie vloženého pokynu učí agenta, aby neskôr poslúchal ďalšie vložené pokyny. Preprint skúma kontrolovaný súbor úloh, nie všetkých nasadených osobných agentov. Ukazuje však, že prispôsobovanie môže zmeniť predchádzajúce úspešné správanie na neskoršiu bezpečnostnú slabinu.

Zdroj: https://arxiv.org/abs/2610.39122

**Štyri hraničné modely dosiahli na najdlhších a najzložitejších úlohách sledovania stavu v StateBench presnosť najviac 13 %.** Ai2 testoval modely Gemini 3.8 Flash, Claude Opus 5.5, GPT-6 Sol a GPT-6 Luna na sekvenciách, v ktorých sa hodnoty menia a navzájom od seba závisia. Všetky štyri zvládali jednoduché vyhľadávanie a opätovné priraďovanie, no pri prenášaní vzájomne závislých zmien cez dlhé vstupy sa ich výkon zhoršil.

Malé rekurentné a hybridné modely s 275 miliónmi parametrov, trénované priamo na tejto úlohe, zovšeobecnili takmer bezchybne na troch zo štyroch úrovní, dokonca aj pri 64 000 priradeniach. Transformery sa najťažšiu úroveň nikdy nenaučili. Porovnanie neukazuje, že malý špecializovaný model je vo všeobecnosti lepší než hraničný model. Izoluje jednu schopnosť, ktorú súčasný predtréning nevytvára spoľahlivo, a jeden prípad, keď architektúra stále obmedzuje učenie.

Zdroj: https://huggingface.co/blog/allenai/statebench

**Vedecké tímy si po uvedení ChatGPT delili prácu užšie, najmä ak výskumníci predtým nespolupracovali.** Stefano Bianchini a Georgiana-Ioana Coroama analyzovali vyhlásenia o príspevkoch v približne 120 000 článkoch časopisu PLOS ONE vydaných v rokoch 2018 až 2025. Účasť klesla pod predchádzajúci trend pri tvorbe koncepcie, realizácii a písaní. Výskumníci zároveň pokrývali menej úloh a ich práca sa menej prekrývala s prácou spoluautorov.

Zabehnuté tímy sa zmenili menej. Autori tento vzorec interpretujú tak, že LLM nahrádzajú časť doplnkových vstupov od kolegov a umožňujú väčšiu špecializáciu. Ide o observačný preprint založený na jednom časopise a vlastnom označení príspevkov. Nemôže preukázať, že reorganizáciu spôsobilo ChatGPT ani či užšia účasť zlepšila články.

Zdroj: https://arxiv.org/abs/2611.02996

**Školy v USA, ktoré odmietnu nástroje AI od Googlu, prídu aj o Google Search.** Google plánuje predvolene zapnúť Gemini, NotebookLM a súvisiace funkcie pre triedy, pričom administrátorom dovolí celý balík vypnúť. Viceprezident spoločnosti pre vzdelávanie povedal denníku New York Times, že Search a AI sú už úzko integrované, takže žiaci s obmedzeným prístupom nebudú môcť používať ani Search.

Zmena sa zavedie v nasledujúcich mesiacoch. Rozhodnutie o generatívnej AI tak mení na rozhodnutie o prístupe k základnému výskumnému nástroju. Školskí administrátori nedostanú pre obe služby samostatné prepínače. Google opisuje integráciu ako obmedzenie produktu; citované správy neuvádzajú technický dôvod, prečo musia služby zostať zviazané.

Zdroje: https://techcrunch.com/2026/11/03/google-will-let-schools-disable-its-ai-tools-but-not-without-sacrificing-search/, https://arstechnica.com/ai/2026/11/google-will-let-schools-skip-ai-tools-but-they-have-to-give-up-search-too/

## Nové modely a vydania

**Sarvam AI vydal Prism, model s otvorenými váhami na rozhodovanie, ktorý namiesto generovania textu vracia pravdepodobnosti pre pevne dané možnosti.** Sarvam uvádza priemerné skóre 71,8 v troch indexoch pri mediáne 44 ms na jednom B200, čo je v jeho vlastnom porovnaní najlepší výsledok pod 100 ms. Model s licenciou Apache-2.0 podporuje angličtinu a desať indických jazykov a s podporou FP8 potrebuje približne 120 GB pamäte GPU.

Zdroje: https://www.sarvam.ai/blogs/sarvam-prism, https://huggingface.co/sarvamai/prism

**Anthropic potvrdil, že text z modelov Claude Mythos 5, Opus 4.7 a Sonnet 4.6 na uvedených platformách obsahuje jeho textový vodoznak.** Iné než predvolené nastavenia temperature, top_p alebo top_k môžu zabrániť modelu Sonnet 4.6 pridať značku. Anthropic tvrdí, že vodoznak nepridáva skryté znaky a neobsahuje informácie o používateľovi ani organizácii.

Zdroj: https://platform.claude.com/docs/en/release-notes/overview#november-3-2026

**Claude Code 2.1.318 pridal oznamovanie vypršania prihlásenia, možnosť roly AWS a nastavenie úsilia pre rozvetvenú prácu modelu.** Desať dní vopred upozorní, že uloženým prihlasovacím údajom claude.ai končí platnosť, a dátum vypršania uvádza aj v príkazoch na autentifikáciu. Vydanie opravuje aj problémy s konverzáciami a obsluhou terminálu.

Zdroj: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.318

**Amazon Bedrock pridal inferenciu pre model Kimi K3 s otvorenými váhami od Moonshotu v Indii.** Nový profil ponecháva požiadavky v regiónoch Bombaj a Hajdarábad pre pracovné záťaže s požiadavkami na umiestnenie dát. Zákazník Ultrahuman tvrdí, že ukladanie promptov do vyrovnávacej pamäte znížilo jeho náklady na model o 80 % a zrýchlilo viacťahové konverzácie o 85 %; ide o merania zákazníka.

Zdroj: https://aws.amazon.com/blogs/machine-learning/introducing-india-based-inference-for-kimi-k3-on-amazon-bedrock/

## Výskum

**Merateľný smer v reziduálnom prúde súvisiaci s kapituláciou sa objavil až pri približne 7 miliardách parametrov a viac.** Pri ôsmich modeloch doladených na plnenie pokynov znížilo odstránenie overeného smeru v modeli Qwen2.5-7B opúšťanie správnych odpovedí po námietke používateľa o 4,8 bodu. Menšie modely vykazovali toto správanie, no nemali použiteľný smer. Ide o čiastočne negatívny výsledok vopred registrovanej štúdie.

Zdroj: https://arxiv.org/abs/2611.02318

**Viditeľný záznam uvažovania nemusel byť užitočný na monitorovanie správania, ku ktorému prispel.** Stanovisko pre NeurIPS oddeľuje viditeľnosť, mechanistickú vernosť, kauzálnu lokalizáciu a možnosť monitorovať správanie. V jednom prípade bol koncept zraniteľnosti reprezentovaný a kauzálne použitý, zatiaľ čo monitor nebol lepší než väčšinová základná úroveň.

Zdroj: https://arxiv.org/abs/2611.01620

**Šachový transformer simulujúci slabších hráčov stále kódoval takmer rovnaké poznatky o šachovnici.** Lineárne sondy pre 172 konceptov sa prenášali medzi nastaveniami zručnosti a opätovné natrénovanie iba výstupnej vrstvy zvýšilo presnosť najlepšieho ťahu v najnižšom pásme zo 14,4 na 82,8 %. Slabšie správanie vychádzalo najmä z toho, ako model používal svoju reprezentáciu, nie z toho, čo si ukladal.

Zdroj: https://arxiv.org/abs/2611.03439

**Výskumné návrhy AI sa zhodovali iba s 18 % nápadov, ktoré tie isté komunity zverejnili o rok neskôr.** IdeaTaste uzavrel literatúru v roku 2025, vytvoril viac ako 90 000 návrhov a porovnal ich s publikáciami z roku 2026. Väčšie populácie návrhov a bohatší kontext pomohli len málo, zatiaľ čo experti pri zaslepenom hodnotení zaradili návrhy AI najnižšie podľa očakávaného úspechu.

Zdroj: https://arxiv.org/abs/2611.03424

**Smer v skrytom stave pred prvým tokenom v dvoch malých modeloch odlišoval neskoršie odmietnutia od konfabulácií.** Riadenie tohto smeru zmenilo väčšinu konfabulácií na odmietnutia bez poškodenia odpovedí, ktoré boli pôvodne správne. Štúdia pokrýva Qwen3-1.7B a Gemma 2 2B, preto výsledok nepotvrdzuje rovnakú bránu vo väčších systémoch.

Zdroj: https://arxiv.org/abs/2611.01272

**Kódovacie agenty, ktoré si vyvíjali vlastný pracovný rámec, stratili zisky dosiahnuté pri skorších úlohách.** Pri jednej metóde sa výkon v SWE-Bench zvýšil na 94,0 % a po ďalšom vývoji na FeatureBench klesol na 32,0 %. Ku katastrofickému zabúdaniu teda môže dôjsť v promptoch a zručnostiach, aj keď sa váhy modelu nemenia.

Zdroj: https://arxiv.org/abs/2611.03219

**Slávne mená viedli modely anotátorov k dopĺňaniu faktov, ktoré boli o danej osobe správne, no text ich nepodporoval.** Pri 121 594 promptoch na model sa skratky objavili vtedy, keď dôkazy chýbali, nie keď boli v rozpore s pamäťou. Maskovanie mien alebo pripomenutie existencie menovcov účinok odstránilo.

Zdroj: https://arxiv.org/abs/2611.02273

**Vizuálne perturbácie zmenili fyzický úkon obrazovo-jazykového agenta, hoci jeho písomné odôvodnenie zostalo rovnaké.** Úkon sa zmenil 4,64- až 47,8-krát viac než pri perturbáciách textového gradientu. Výsledok oslabuje bezpečnostné kontroly, ktoré nezmenené vysvetlenie považujú za dôkaz stability základného rozhodnutia.

Zdroj: https://arxiv.org/abs/2611.04166

## Ekonomika a práca

**Goldman Sachs obmedzil Claude Code a kódovacie nástroje GitHubu prevažne na inžinierov a kvantitatívnych pracovníkov.** Obchodníci a bankári ich používali na sledovanie tokov klientov a tvorbu písomných či grafických materiálov. Hovorca odkázal na produktivitu a riadenie rizík a uviedol, že fáza experimentovania sa skončila. Správa Bloombergu, z ktorej položka vychádza, bola za platobnou bránou.

Zdroj: https://the-decoder.com/goldman-sachs-pulls-ai-coding-tools-from-traders-and-bankers/

**Meta do júna presunula približne polovicu žiadostí o kontrolu obsahu na LLM a automatizácii pripísala nedávne chyby súvisiace s voľbami.** Meta pre Financial Times uviedla, že jej modely robia o 13 % menej chýb a zachytia o 10 % viac porušení než ľudskí kontrolóri. Nedávne automatizované obmedzenia zasiahli zvoleného brazílskeho prezidenta, protestné hnutie No Kings a kandidáta do Senátu USA; porovnávacie údaje o chybách sú tvrdeniami spoločnosti Meta.

Zdroj: https://fortune.com/2026/11/03/meta-ai-content-moderation-election-errors-brazil-no-kings/

**Shopify vo svojej správe uviedol používanie LLM ako jednu zo súčastí zvýšenia nákladov na infraštruktúru o 40 miliónov dolárov.** Hrubá marža predplatného klesla z 81,7 % pred rokom na približne 79,1 %, zatiaľ čo celkové tržby vzrástli o 32 %. Správa neoddeľuje náklady na AI od ostatných výdavkov na hardvér a softvér.

Zdroje: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000068/shop-20260930.htm, https://www.sec.gov/Archives/edgar/data/1594805/000159480526000067/exhibit991pressreleaseq320.htm

**Náklady spoločnosti Anthropic na výpočty a infraštruktúru sa za jeden štvrťrok zvýšili zo 48 na 58 % tržieb.** V jej podaní sa uvádza, že výpočtová kapacita za 5,0 miliardy dolárov kúpená na základe krátkodobých záväzkov stojí podstatne viac než porovnateľná viacročná kapacita. Tržby za tretí štvrťrok vzrástli z 11,5 na 17 miliárd dolárov, no obsluha dopytu bola počas prudkého rastu menej efektívna.

Zdroj: https://techcrunch.com/2026/11/03/anthropic-is-still-grappling-with-the-economics-of-compute/

**AMD vykázal rekordný štvrťrok s tržbami 13,4 miliardy dolárov, keď sa tržby dátových centier takmer zdvojnásobili a tržby z hier klesli o 40 %.** Data Center prinieslo 8,5 miliardy dolárov, približne 63 % z celku. AMD pripisuje pokles v hernom segmente nižším tržbám z pološpecializovaných riešení a grafiky, zatiaľ čo nedostatok pamätí súvisiaci s infraštruktúrou AI zvyšuje ceny aj v spotrebiteľskom hardvéri.

Zdroje: https://www.sec.gov/Archives/edgar/data/2488/000000248826000188/q32026991.htm, https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc

**Canva reštrukturalizuje pozície, ktoré zahŕňajú 1 271 ľudí, teda 22 % zamestnancov.** Memorandum generálneho riaditeľa odkazuje na vrstvy, špecializáciu a premiestnenie, nie na AI. Externé správy zmenu zaraďujú po prvom spomalení rastu Canvy za desaťročie a do obdobia konkurencie generátorov obrázkov. Odchádzajúci pracovníci dostanú mzdu najmenej za šesť mesiacov.

Zdroje: https://www.theregister.com/saas/2026/11/04/aussie-adobe-assailant-canva-announces-layoffs-in-re-org-affecting-22-of-staff/5307422, https://www.businessinsider.com/canva-reorganization-layoffs-ceo-memo-2026-11

**Kodiak dodal spoločnosti Atlas Energy dve nové nákladné vozidlá bez vodiča a zvýšil tak jej vlastnenú flotilu na 37 kusov.** Atlas si objednal 100 vozidiel a Kodiak očakáva, že prvých 65 dodá v prvom polroku 2027. Spoločnosť neuvádza porovnanie nákladov na míľu ani bezpečnosti a vozidlá jazdia na súkromných cestách ropných polí.

Zdroj: https://kodiak.ai/news/kodiak-delivers-western-star-49x-trucks-atlas

## Techniky promptovania

**Google DeepMind spojil agenta s deterministickými chemickými zručnosťami namiesto toho, aby nechal model počítať molekuly.** Nástroje RDKit, ChEMBL a PubChem vykonávali presnú prácu, zatiaľ čo agent vyberal a kombinoval operácie. Jeden prípad návrhu lieku sa podľa príspevku spoločnosti skončil približne za hodinu namiesto niekoľkých dní na iteráciu; tvrdenie o čase neoveril žiadny benchmark.

Zdroj: https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/

**Zmena poradia polí JSON odstránila nepovolené nápovedy v malom teste modelu Haiku jedného vývojára.** Keď bolo pole `clue` pred poľom `reasoning`, model sa zaviazal k odpovedi pred analýzou. Obrátenie poradia znížilo počet nepovolených nápovied z dvoch z desiatich na nulu a zvýšilo priemernú známku z 30 na 64. Výsledok používa päť vzoriek pre každú polohu a autor ho uvádza sám.

Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xnad7d/haiku_55_kept_thinking_when_i_set_thinking_off/

## Čo ľudia tvoria

**Basalt 0.2.0 uvádza rýchlosť aj kvalitu modelu Qwen 3.8 Flash Next na GPU Blackwell.** Autor nameral 300 tokenov za sekundu pri próze, 600 pri štruktúrovanom výstupe a 10 000 pri predvyplnení na kombinácii RTX 5090 a 5060 Ti. Stratové možnosti zrýchlenia sú teraz predvolene vypnuté.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xn4qn1/basalt_020_qwen_38_flash_next_nvfp4_300_ts_prose/

**webyIQ uvádza 620 tokenov za sekundu pre Qwen3.5-2B v prehliadači Chrome na RTX 5080.** Prototyp iba pre Windows používa ručne písané jadrá WebGPU a špekulatívne dekódovanie. Pri rovnakom modeli a promptoch uvádza pre WebLLM 94 tokenov za sekundu.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xmv3lc/qwen352b_at_620_toks_inside_chrome_modelspecific/

**Olla 0.1.0 smeruje požiadavky medzi Ollama, vLLM, SGLang, llama.cpp, LM Studio a MLX.** Proxy v jazyku Go pridáva prepnutie pri zlyhaní, ističe a trvalé relácie pre lokalitu vyrovnávacej pamäte KV, s koncovými bodmi kompatibilnými s OpenAI a Anthropic.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xmq913/olla_v010_lightweight_opensource_llm_proxy_for/

**Rufous vedie záznam všetkých volaní nástrojov malého lokálneho kódovacieho modelu, do ktorého sa dá iba pridávať.** Pred koncom ťahu rámec v jazyku Rust porovná správu modelu so záznamom a môže odhaliť súbor, o ktorom agent tvrdil, že ho zapísal, hoci to neurobil.

Zdroj: https://news.ycombinator.com/item?id=50332594

**mcp-toolsearch-proxy sprístupňuje päť metanástrojov namiesto toho, aby modelu posielal stovky schém.** Pri 500 nástrojoch autor uvádza o 97 % menej tokenov definícií a približne polovičné náklady na úlohu pri takmer rovnakej úspešnosti zásahov. Volania na čítanie zostávajú oddelené od zápisov, aby ich klienti mohli schvaľovať odlišne.

Zdroj: https://news.ycombinator.com/item?id=50356916

**modeljury sa pýta piatich lacných otvorených modelov a nezhody posiela človeku.** Z 2 850 rozhodnutí odoslalo 71 % bez kontroly pri správnosti 89,6 % a nákladoch 0,61 dolára na 1 000 rozhodnutí. Claude Opus 5.5 podľa benchmarku autora dosiahol na odoslanej podmnožine 90,5 % za 5,79 dolára.

Zdroj: https://news.ycombinator.com/item?id=50325217

**lorevault mení histórie Claude Code, Codexu a Cursoru na lokálny znalostný graf so zdrojmi.** Každé rozhodnutie, pravidlo alebo úloha odkazuje na presnú správu a server MCP umožňuje agentom prehľadávať ich v neskorších reláciách.

Zdroj: https://github.com/deanyool/lorevault

**OpenFusion smeruje čiastkové úlohy na rýchle, štandardné alebo hĺbkové úrovne modelov a neúspešnú prácu eskaluje.** Podporuje viacero klientov kódovacích agentov a lacný model môže vytvoriť návrh, ktorý následne posúdi silnejší model. Projekt nezverejňuje namerané úspory.

Zdroj: https://github.com/calesthio/OpenFusion

**boxery poskytuje kódovacím agentom dočasné virtuálne stroje, ktoré môžu vetviť, snímkovať a zahadzovať.** Projekt s licenciou MIT sprístupňuje lokálne, vzdialené a cloudové VM prostredníctvom servera MCP, CLI a rozšírenia pre agentov.

Zdroj: https://github.com/modem-dev/boxery

**qwenFS kompiluje súborový systém do ôsmich ručne písaných vrstiev transformera umiestnených pred Qwen3.5-2B.** Attention ukladá text súborov, zatiaľ čo stav Gated DeltaNet uchováva cesty, verzie a odkazy. Nové vrstvy nepoužívajú naučené váhy a vracajú presné čítanie token po tokene.

Zdroj: https://github.com/vixhal-baraiya/qwenFS

## Stojí za prečítanie

**FlashProve vytvára kryptografický dôkaz, že odpoveď vygeneroval uvedený model.** Anthropic uvádza približne 110 dokázaných tokenov za sekundu pre 4-bitový Llama 4 Maverick na jednom H100, s dôkazom veľkým približne 19 MB na požiadavku s 1 024 tokenmi. Systém spotrebuje približne 70–95-krát viac času GPU než bežná inferencia vLLM a jeho kód aj tvrdenia overené v Leane sú verejné.

Zdroj: https://www.anthropic.com/research/provable-inference

**Moderný Stockfish na 200 MHz procesore Pentium Pro dosiahol pri klasickom časovom tempe odhadované Elo 3 300.** Nicholas Carlini nameral Elo 2 846 pri jednej sekunde na ťah a 3 180 pri 30 sekundách, potom extrapoloval dlhší výsledok. Experiment tvrdí, že veľkú časť pokroku šachových programov od roku 1996 priniesli algoritmické zlepšenia, nielen hardvér.

Zdroj: https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html

**Figma natrénovala 27B otvorený model na úpravy dizajnu a tvrdí, že používatelia rušia jeho prácu o 60 % menej často.** Spoločnosť uvádza, že typické úlohy prebiehajú približne o 20 % rýchlejšie a odborní dizajnéri nový agent uprednostnili alebo hodnotili rovnako v 62 % prípadov. Ide o interné merania produktu.

Zdroj: https://www.figma.com/blog/training-a-figma-fluent-editing-model/

**IBM Research vytvoril Palette, model s 20B parametrami, ktorý generuje prezentácie v rámci dizajnového jazyka.** Rámec render-check-repair pridal 3,5 bodu v 131 prezentáciách. Pravidlo v prompte nezastavilo vymyslené fakty v tabuľkách, no referenčné prezentácie áno. Príklady teda model riadili účinnejšie než pokyny.

Zdroj: https://huggingface.co/blog/ibm-research/palette-deck-building

**CWE-bench v2 testuje 100 skutočných bezpečnostných opráv v 91 triedach zraniteľností.** Gemini 4 Argon vedie so 67,8 % pass@1, tesne pred Claude Opus 5.5 so 67,3 %. DeepSeek V4.1 Flash dosiahol 57,0 % za 0,04 dolára na jeden beh, v porovnaní s 1,83 dolára pri Opuse a 3,92 dolára pri Gemini.

Zdroj: https://huggingface.co/blog/cwe-bench

**Hugging Face navrhol spustiteľné zmluvy na integráciu modelov po tom, čo tichá chyba UMT5 prežila takmer dva mesiace.** Zmena umožnila dekodéru počas trénovania venovať pozornosť budúcim tokenom bez zlyhania. Pomocný model s veľkosťou 66 MB a zaznamenané základné výsledky zachytili staré chybné commity pri spustení na procesore.

Zdroj: https://huggingface.co/blog/transformers-mic

## Hacker News

**Používatelia Postmanu obvinili aplikáciu, že bez upozornenia inštaluje pluginy AI a pokúša sa zdieľať údaje API.** Prepojený problém na GitHube nebol počas výskumu čitateľný, preto dôkazy o zdieľaní dát zostávajú neoverené. Vlákno s 340 komentármi sa vo veľkej miere venovalo prechodu na Bruno, Yaak alebo Insomnia.

Zdroj: https://news.ycombinator.com/item?id=50354960

**Viacerí používatelia Codexu uviedli, že vypnuté nastavenie trénovania modelu sa opäť zaplo.** Správy sú neoficiálne a OpenAI nevysvetlila, či zmenu spôsobila chyba alebo pravidlo. Tímy, ktoré nechcú zdrojový kód používať na trénovanie, by mali nastavenie priamo skontrolovať.

Zdroj: https://news.ycombinator.com/item?id=50352757

**Zamestnanci Google DeepMind spochybnili doživotné obmedzenia kritiky spoločnosti.** Google tvrdí, že novšie zmluvy už časť platnú po skončení pracovného pomeru neobsahujú a že klauzulu nevymáhal voči jednému bývalému zamestnancovi. Spor sa týka odradzujúceho účinku formulácie, nie nahlásenej sankcie.

Zdroj: https://news.ycombinator.com/item?id=50355504

## Reddit

**Lacný kódovací subagent v jednom benchmarku s 12 úlohami znížil presnosť modelu Opus 5.5 a zvýšil jeho náklady.** Samotný Opus vyriešil 81 % úloh za 1,20 dolára na úlohu; Opus pri plánovaní s DeepSeek na písanie vyriešil 67 % za 1,29 dolára. Jednotlivé behy GPT-6.1 Terra a Sol dosiahli 78 a 75 % za 0,17 dolára podľa testu autora s približne 1 200 behmi.

Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xn0e12/i_tried_to_make_opus_55_cheaper_with_a_cheap/

**Jeden používateľ lokálneho agenta zistil, že zachované uvažovanie Qwen 3.8 spotrebovalo viac než polovicu vyrovnávacej pamäte KV.** Vypnutie zachovania a uloženie dôležitých poznatkov do pamäťového súboru znížilo tlak, zatiaľ čo iní používatelia tvrdili, že odstránenie záznamov nútilo model opakovať prácu. Ide o neoficiálne pozorovanie.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xmsgz5/preserve_thinking_off_is_fine/

**Prototyp Qwen3.5-2B v prehliadači uviedol 620 tokenov za sekundu so špekuláciou na RTX 5080.** Ten istý autor nameral 417 bez špekulácie, 94 pre WebLLM a 31 pre transformers.js. Benchmark mal model vopred načítaný a bol testovaný iba vo Windows.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xmv3lc/qwen352b_at_620_toks_inside_chrome_modelspecific/

**Jeden používateľ tvrdí, že Claude obnovil použiteľný obsah z približne 700 súborov zašifrovaných ransomvérom.** Agent si všimol, že zašifrovaných bolo iba prvých 16 KB každého súboru, napísal nástroje na obnovu podľa formátu a získal 239 MB model SketchUp. Ide o vlastnú správu používateľa a ochranné mechanizmy zastavili podobné relácie niektorých komentujúcich.

Zdroj: https://old.reddit.com/r/ClaudeAI/comments/1xn6tu3/i_gave_claude_700_ransomware_encrypted_files_it/

## YouTube

**Artificial Analysis rozdelil náklady agentov na vstupné tokeny, zásahy do vyrovnávacej pamäte a kroky.** Prepočítaný príklad Georgea Camerona stojí približne 21 dolárov s ukladaním promptov do vyrovnávacej pamäte a viac než 200 dolárov bez neho. Čísla sú príkladom rečníka. Kanál: AI Engineer. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=prGP0huECPo

**Warp tvrdí, že ladenie modelu a subagenty znížili jeho interné náklady z približne 80 dolárov na pull request na 15–20 dolárov.** Zakladateľ Zach Lloyd opisuje systém, ktorý mení požiadavky zo Slacku na hodnotené pull requesty. Čísla pochádzajú od Warpu. Kanál: Latent Space. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=LL0YmIyBKSU

**Basis tvrdil, že veľké zvýšenie produktivity jednotlivcov sa automaticky nerozšíri po celej spoločnosti.** Mitchell Troyanovsky odporúča špecifikácie správania, vetvenie behov a simulovaných subagentov na ladenie produkčných systémov. Ide o argument dodávateľa. Kanál: AI Engineer. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=JGtkTjn4120

**Neo4j predstavil zručnosti agentov v tvare grafu ako alternatívu k hromadám textu.** Ukážka schvaľovania úveru sleduje skompilovaný graf logiky a minulých rozhodnutí s pozorovateľnosťou jednotlivých vetiev. Tvrdenia o predvídateľnosti pochádzajú od databázového dodávateľa. Kanál: AI Engineer. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=g_NgCLTibiM

**Mixedbread tvrdí, že lepšie vyhľadávanie zvýšilo presnosť agenta jedného zákazníka z 36 na 98 %.** Aamir Shakir predviedol vyhľadávanie s neskorou interakciou v správach o výsledkoch, opis však neuvádza metódu zákazníckeho výsledku. Kanál: AI Engineer. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=3Ad73Onx3Aw

**Factory prebudoval svojho kódovacieho agenta Droid tak, aby bežal na výpočtovej kapacite v cloude zákazníka.** Návrh zahŕňa riadiacu vrstvu, bránu, prenos, kľúče zákazníckych modelov a vetviteľné snímky. Factory plánuje výpočtovú vrstvu zverejniť ako open source. Kanál: AI Engineer. Jazyk: angličtina.

Zdroj: https://www.youtube.com/watch?v=XIHZpZtYCzo

**Českí moderátori vytvárali presnú značkovú grafiku programovaním pomocou kódovacích agentov namiesto obrazových modelov.** Opakované bannery zmenili na zručnosti a ukázali aj krížovú kontrolu fotografií predajcov áut. Nahrávka je trojminútový úryvok. Kanál: AI v kostce. Jazyk: čeština.

Zdroj: https://www.youtube.com/watch?v=jhoUDBVRcqA

## Stručne

**Inštalátor AI nástroja s trójskym koňom pomohol útočníkom zmapovať zamestnancov peňaženky Binance pred krádežou 6,43 miliardy dolárov.** Binance tvrdí, že neskoršia falošná náborová úloha nainštalovala ďalší malvér a ukradnutý token nasadenia umožnil konečný prienik. Spoločnosť nanovo vybudovala systém peňaženiek aj interný nástroj AI.

Zdroj: https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html

**Dve nové CVE ovplyvňujú Claude Code v macOS a Claude Desktop vo Windows.** CVE-2026-88968 môže po spustení kódu v sandboxe Bash uniknúť z pracovného priestoru výmenou symbolického odkazu; CVE-2026-88066 môže spustiť škodlivý git.exe z otvoreného priečinka projektu. Obe chyby sú opravené.

Zdroje: https://nvd.nist.gov/vuln/detail/CVE-2026-88968, https://nvd.nist.gov/vuln/detail/CVE-2026-88066

**Chainstack zverejnil prienik do produkcie spojený s kampaňou ARTEX využívajúcou AI.** Útočník sa cez vývojové prostredie dostal do produkcie a odhalil údaje o účtoch zákazníkov aj prihlasovacie údaje uzlov. Spoločnosť zákazníkom odporúča zmeniť prihlasovacie údaje uzlov a kľúče API.

Zdroj: https://thehackernews.com/2026/11/chainstack-reports-production-systems.html

**Čínska plánovacia agentúra tvrdí, že bude monitorovať vplyv AI na zamestnanosť a stanoví bezpečnostné normy pre celý životný cyklus.** Čitateľný bol iba úvodný odsek a záznam o konferencii, preto presné znenie a harmonogram zostávajú nepotvrdené.

Zdroje: https://www.theinformation.com/briefings/china-signals-plans-broad-ai-safety-guardrails, https://www.ndrc.gov.cn/xwdt/xwfb/202611/t20261103_1408537.html

**Apple bude od 16. novembra vyžadovať hodnotenie 18+ pre zoznamovacie aplikácie a romantických či sexuálnych spoločníkov AI.** Nové popisy sa vzťahujú aj na aplikácie, v ktorých sú spoločníci iba jednou z funkcií.

Zdroj: https://techcrunch.com/2026/11/03/apple-restricts-dating-apps-and-ai-companions-to-users-18-and-up/

**AISIN a Tohoku University umiestnili váhy modelu aj operačný systém do STT-MRAM priamo na čipe.** Ich 16 nm systém naštartoval až po jadro za 65,7 ms, 38-krát rýchlejšie než pri externej pamäti, a so zmiešanou presnosťou zmenšil váhy Tiny YOLOv3 o 53 %. Dátum výroby neoznámili.

Zdroj: https://www.theregister.com/systems/2026/11/03/toyota-shows-off-soc-that-stores-model-weights-and-its-os-on-integrated-memory/5307117

**Envision Energy hlási prvé komerčné nasadenie napájacieho systému dátového centra s jednosmerným napätím 800 V.** Systém mení 10 kV striedavého napätia priamo na 800 V zbernicu a používa batérie na pohlcovanie výkyvov záťaže GPU. Označenie za svetové prvenstvo je tvrdením spoločnosti.

Zdroj: https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint

**Intel vydal sadu PDK 0.9 pre svoj proces 14A s modelmi založenými na meranom kremíku.** Zákazníci môžu začať navrhovať produkty už teraz; Intel plánuje PDK 1.0 na prvý štvrťrok 2027.

Zdroj: https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027

## Biznis v skratke

**Poskytovateľ inferencie modelov Fal získal 1,3 miliardy dolárov pri ohodnotení 16 miliárd dolárov, čo je dvojnásobok aprílového ohodnotenia.** Zdroj: https://techcrunch.com/2026/11/03/ai-inference-startup-fal-doubles-its-valuation-to-16b-as-demand-surges/

## Čo sledovať

Nové popisy vekových hodnotení Applu začnú byť povinné 16. novembra. Intel očakáva PDK 1.0 pre proces 14A v prvom štvrťroku 2027 a Kodiak plánuje dodať prvých 65 vozidiel z objednávky Atlasu počas prvého polroka 2027.

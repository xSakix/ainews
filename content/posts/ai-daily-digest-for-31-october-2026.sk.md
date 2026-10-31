+++
title = "Denný prehľad AI – 31. októbra 2026"
slug = "denny-prehlad-ai-31-oktobra-2026"
description = "K používateľom Cursoru sa dostalo škodlivé rozšírenie Claude Code, ktoré po odinštalovaní zanechalo mechanizmus trvalého prístupu. Microsoft vydal 4B model na ovládanie počítača a výskumníci ukázali, že introspekcia modelov potrebuje kauzálne trénovanie, nie bežné dolaďovanie."
tags = ["safety", "models", "research", "business"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

## Hlavné správy

**K používateľom Cursoru sa dostalo napadnuté rozšírenie Claude Code a bežná aktualizácia neodstráni všetky jeho zásahy.** Škodlivé verzie 2.1.312 a 2.1.313 boli 29. októbra približne 11 hodín dostupné v obchode s rozšíreniami Cursoru. Podľa Cursoru zbierali údaje o zariadení, pridali útočníkov kľúč SSH a nainštalovali skripty, ktoré sa opakovane pokúšali otvoriť spätný tunel. Tunel zvyčajne zlyhal, ak Cursor nemal oprávnenia správcu, no kľúč, mechanizmus trvalého spúšťania aj odosielanie údajov fungovali.

Cursor balíky odstránil, obchod vypol a nanovo zostavil, vymenil svoje kľúče a odstavil riadiaci server. Uvádza, že žiadne iné rozšírenie nebolo pozmenené a škodlivé verzie nevytvorila firma Anthropic. Používatelia, ktorí si nainštalovali niektorú z nich, musia odstrániť kľúč SSH aj mechanizmus trvalého spúšťania, skontrolovať zariadenie a vymeniť dostupné prihlasovacie údaje; odinštalovanie ani aktualizácia nestačia.

Zdroje: https://cursor.com/blog/claude-code-extension-security-notice, https://phorion.io/blog/offical-claude-code-vsx-compromise/

**Microsoft vydal otvorený 4B model, ktorý sa rozhoduje, kedy kliknúť na obrazovke a kedy použiť terminál.** Mage-VL-Cowork ponúka 11 operácií na obrazovke spolu s trvalým prostredím Bash a Python. Microsoft uvádza priemerné skóre 66,0 % z dvoch behov na 361 úlohách OSWorld-Verified s limitom 50 krokov. Online učenie posilňovaním pridalo oproti dolaďovaniu s dohľadom 10,16 percentuálneho bodu a znížilo počet výstupných tokenov na úlohu o 25,4 %.

Checkpoint s licenciou Apache-2.0 má 4,74 miliardy parametrov vo formáte BF16 a aktívny kontext 32 768 tokenov. Proces tvorby syntetických dát podľa Microsoftu znížil náklady z 0,906 na 0,158 dolára za úlohu. Všetky merania poskytol tím modelu a nikto ich zatiaľ nezávisle nezopakoval. Vydanie však spája prácu v grafickom prostredí a príkazovom riadku v jedných váhach, ktoré sú dosť malé na lokálne experimenty.

Zdroj: https://huggingface.co/microsoft/Mage-VL-Cowork

**Bežné dolaďovanie naučilo modely opisovať signály, ktoré súviseli s ich vnútorným stavom, nie samotný vnútorný stav.** Zilu Tang a jeho kolegovia vytrénovali stovky introspektorov v ôsmich jazykových modeloch, aby hlásili jednoduché vnútorné signály, napríklad aktiváciu jedného neurónu. Dolaďovanie s dohľadom viedlo k javu, ktorý nazývajú kauzálne obídenie: odpoveď sledovala súvisiaci údaj, ktorý mohol zostať nezmenený aj po zmene cieľového signálu.

Trénovanie na hodnotách zmenených proti skutočnosti tento jav obmedzilo. Modely potom presnejšie hlásili vlastné aj vložené signály vrátane príkladov mimo tréningového rozdelenia a účinok sa preniesol medzi pozíciami tokenov. Deväťstranový preprint skúma zámerne jednoduché signály, nie bohaté pojmy ako úmysel. Výsledok je však varovaním pre interpretovateľnosť: zhoda sebahodnotenia s vnútornou hodnotou nedokazuje, že táto hodnota sebahodnotenie spôsobila.

Zdroj: https://arxiv.org/abs/2610.38911

**ServiceNow tvrdí, že vlastná AI mu umožnila prijať menej ľudí, investori však z ceny akcií ubrali približne štvrtinu.** Generálny riaditeľ Bill McDermott označil mierne menší počet zamestnancov za „nádhernú situáciu“. Finančná riaditeľka Gina Mastantuono uviedla, že interné používanie AI prinieslo ročné úspory viac než 1 miliardu dolárov, vďaka čomu firma „nemusela prijať toľko ľudí“. Počet predajcov s kvótami vzrástol dvojciferne, zatiaľ čo počet pracovníkov podpory predaja výrazne klesol.

Tržby vzrástli o viac než 20 % na 4,106 miliardy dolárov, no výhľad rastu zazmluvnených tržieb v štvrtom štvrťroku bol 18,5 % oproti očakávaným 19,8 %. Akcie klesli približne o 25 %. ServiceNow predáva nástroje, na ktorých stojí jeho tvrdenie, takže vlastné mzdové náklady sú súčasťou obchodnej ponuky. Reakcia trhu ukazuje, že úspory nákladov neodpovedajú na otázku, kedy sa zrýchlia tržby z AI.

Zdroj: https://www.calcalistech.com/ctechnews/article/eft5mhzxc

**Podiel právnikov vo Victorii, ktorí používajú AI, za rok vzrástol z 37 na 55 %, no iba 26 % uviedlo zníženie poplatkov klientom.** Právny regulátor štátu oslovil 2 221 právnikov. Podiel používateľov dosiahol 85 % v obchodnom práve a 78 % v bankovníctve a financiách, no iba 29 % v trestnom práve. Spotrebiteľské chatboty používalo 79 % respondentov; podľa 18 % AI umožnila prijať prácu, ktorá bola predtým neekonomická.

Klienti zároveň vytvorili novú prácu. Podľa 46 % právnikov prichádzali klienti s nepresnými informáciami od AI a 41 % dostalo dokumenty vytvorené AI, ktoré bolo treba opraviť. Takmer polovica uviedla, že používanie AI klientmi zvýšilo potrebný čas a námahu, kým pokles hlásilo 19 %. Prieskum meria výpovede o praxi, nie fakturované hodiny, ale oddeľuje prijatie technológie od sľubovaných úspor.

Zdroj: https://www.theguardian.com/law/2026/oct/30/victorian-lawyers-ai-clients-fees

## Nové modely a vydania

**OpenAI zaradila GPT-6 Rosalind medzi modely pre biologické vedy s kontrolovaným prístupom.** Schválené organizácie ho môžu používať na interný výskum za 15 dolárov za milión vstupných a 75 dolárov za milión výstupných tokenov pod hranicou dlhého kontextu. Cenník uvádza aj lacnejšie varianty Research a Discovery; s ponukou nevyšiel benchmark ani systémová karta.

Zdroj: https://developers.openai.com/api/docs/pricing

**Nvidia vydala checkpoint DeepSeek-V4.1-Flash-1017 vo formáte NVFP4 pre GPU Blackwell.** Štvorbitová konverzia používa TensorRT Model Optimizer a 1 024 kalibračných vzoriek. Tabuľky Engram potrebujú zostavu vLLM s ešte nezačlenenou zmenou, takže bežný vLLM približne 665 GB checkpoint zatiaľ nedokáže obsluhovať.

Zdroj: https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4

**JetBrains pridal k Mellum2.1 Thinking hlavu na špekulatívne dekódovanie.** 12B model typu mixture-of-experts na programovanie zachováva pôvodný checkpoint a pridáva jeden súbor váh na predikciu viacerých tokenov v novších verziách vLLM a Transformers. JetBrains nezverejnil rýchlosť dekódovania, takže vydanie dokazuje kompatibilitu, nie konkrétne zrýchlenie.

Zdroj: https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-MTP

**Google všeobecne sprístupnil nástroj Computer Use v Gemini API.** Cez rozhrania Interactions a GenerateContent teraz podporuje prehliadač, mobil aj pracovnú plochu. Každá navrhnutá operácia obsahuje pole s úmyslom, no prostredie, ktoré kliknutia vykoná a zabezpečí, stále vytvára klient.

Zdroj: https://ai.google.dev/gemini-api/docs/computer-use

**Anthropic odstráni 30. novembra rýchly režim z Claude Opus 4.8.** Požiadavky s touto voľbou zlyhajú a neprepnú sa na štandardnú rýchlosť. Firma používateľov citlivých na odozvu smeruje na Opus 5.5, kde rýchly režim ponúka až 2,5-násobnú rýchlosť výstupu za príplatok.

Zdroj: https://platform.claude.com/docs/en/build-with-claude/fast-mode

## Výskum

**Písané uvažovanie ovládalo odpovede častejšie s rastúcou veľkosťou modelu.** Esther Xin v syntetickej úlohe s prehadzovaním škatúľ nahradila jeden platný medzistav nesprávnym a merala, či ho odpoveď nasledovala. Závislosť vzrástla zo 16–18 % pri Qwen3 0.6B na 97–100 % pri 14B; výsledok z jedinej úlohy podporuje sledovanie reťazca uvažovania, no nedokazuje rovnaký účinok inde.

Zdroj: https://arxiv.org/abs/2610.38433

**Učenie posilňovaním zlepšilo piškvorky najmä posilnením prvkov, ktoré už boli priamo v prompte.** Analýza pomocou riedkych autoenkóderov zistila väčší dôraz na to, kto je na ťahu, obsadenosť hracej plochy a priebeh hry, kým symetrie a vidličky zostali slabo zastúpené. Malá kontrolovaná oblasť umožňuje mechanizmus skúmať, no obmedzuje zovšeobecnenie.

Zdroj: https://arxiv.org/abs/2610.39182

**Skrytý smer odhalil, ktorý z dvoch protichodných dokumentov malý model nasledoval.** Výskumníci našli smer voľby zdroja v Qwen 0.8B, vystopovali jeho pôvod v stredných vrstvách a dokázali voľbu riadiť; signál sa preniesol aj na Gemma 3 1B. Priznanie konfliktu vznikalo neskôr a riadilo sa ťažšie než samotná skrytá voľba.

Zdroj: https://arxiv.org/abs/2610.38296

**Lineárna sonda zachytila 82 % pripravovaných prezradení tajomstva pri 5 % falošných poplachov.** Kontrolovaná multiagentová štúdia čítala aktivácie Qwen3-32B pred vytvorením výstupu. Klasifikátor založený na slovách dosiahol podobný výsledok, sonda označovala aj povolené zverejnenia a varovala len krátko vopred, takže väčšiu časť prínosu priniesli štítky, nie prístup k aktiváciám.

Zdroj: https://arxiv.org/abs/2610.40588

**Trénovanie v simulácii znížilo počet nezachytených akútnych psychiatrických rizík z 30,5 na 12,9 %.** Tím Google DeepMind a Google Research trénoval na 127 scenároch vstupného rozhovoru overených psychiatrami a testoval 256 nepriateľských prezentácií. Trénovaný agent takmer zdvojnásobil skóre klinických kritérií, autori však naďalej požadujú dohľad lekára, pretože závažné chyby zostali.

Zdroj: https://arxiv.org/abs/2610.40476

## Ekonomika a práca

**Cisco dalo 27-ročnému inžinierovi neobmedzený počet AI tokenov a štyri týždne na preukázanie, že dvojčlenný tím dokáže za dva roky prepracovať 98 % staršieho kódu firmy.** Produktový riaditeľ Jeetu Patel opísal experiment pre Fortune. Výsledok ešte nemá, no mimoriadne veľkú úlohu zveruje pracovníkovi na začiatku kariéry v čase, keď mnohí zamestnávatelia plánujú prijať menej absolventov.

Zdroj: https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/

**Anthropic premenoval Max 20x na Ultra a ponechal cenu 200 dolárov mesačne.** Overené účty prídu o päťhodinový limit, dostanú desaťnásobok týždenného používania programu Pro a 200 dolárov kreditov API. Keďže starý názov naznačoval 20-násobok programu Pro, niektorí zákazníci zmenu vnímajú ako zhoršenie; Anthropic nezverejnil dosť porovnateľných údajov, aby sa to dalo potvrdiť.

Zdroj: https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan

**Široký výpredaj AI akcií zrazil Intel o 28,6 %, najviac od roku 1974.** Nasdaq klesol o 2,9 % a zaznamenal najhorší mesiac od marca 2025, keď investori spochybnili ohodnotenia a výdavky na AI. Alphabet, Amazon, Meta a Microsoft tento rok načrtli kapitálové výdavky nad 740 miliárd dolárov, pričom tri zo štyroch firiem vykázali záporný voľný peňažný tok.

Zdroje: https://www.bbc.co.uk/news/articles/cvwy72e0n72yo, https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/

**S&P Global zmenila výhľad úverového ratingu firmy Meta na negatívny.** Agentúra uviedla, že schopnosť firmy speňažiť výdavky na AI je slabšia než u konkurentov. Meta počíta tento rok s kapitálovými výdavkami až 145 miliárd dolárov a za štvrťrok vykázala záporný voľný peňažný tok 2,1 miliardy dolárov.

Zdroj: https://www.bloomberg.com/news/articles/2026-10-30/meta-s-credit-rating-outlook-downgraded-to-negative-by-s-p

**Aurora po šesťtýždňovom oneskorení výroby nákladných vozidiel znížila odhad tržieb za rok 2026 zo 14–16 miliónov na približne 9 miliónov dolárov.** Nedostatok súčiastok, ich kvalita a záverečné testovanie posunuli míľnik 200 vozidiel na február. Firma si ponecháva cieľ 1 000 autonómnych nákladných vozidiel v roku 2027.

Zdroj: https://www.freightwaves.com/news/aurora-q3-2026-earnings

## Techniky promptovania

**Konkrétne príklady a obmedzenia pomohli v opakovaných testoch jedného praktika viac než rola experta.** Navrhované porovnanie je jednoduché: odstrániť vetu „si špičkový expert“, pridať jeden dobrý a jeden zlý výstup spolu s povolením povedať „neviem“ a porovnať správnosť. Ide o osobnú skúsenosť bez zverejnených počtov.

Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1xjhmpb/you_are_an_expert_prompts_do_almost_nothing_for/

**Používateľský obsah oddeľte jasnými značkami a uveďte, že ide o dáta, nie pokyny.** Jeden praktik tvrdí, že tým odstránil viac chýb než opakovaným prepisovaním formulácie. Oddeľovače nezastavia injekciu promptu, ale modelu a neskorším kontrolórom poskytnú zreteľnú hranicu na testovanie.

Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1xijlh9/wrapping_my_inputs_in_clear_delimiters_fixed_more/

## Čo ľudia tvoria

**MoEShift spustil model typu mixture-of-experts s triedou 125B na Mac mini M4 Pro s 24 GB pamäte rýchlosťou približne desať tokenov za sekundu.** Alfa verzia načítava expertov z SSD, obľúbených ukladá do RAM a čítanie prekrýva s prácou GPU. Autor uvádza špičkovú spotrebu 7,5 GB a približne dvojnásobnú rýchlosť oproti Strata na jednom pevnom prompte.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xjihlu/qwen38_flash_next_125b_iq3_xxs_on_a_24gb_m4_pro/

**Private Mind pridal plne offline textové a vizuálne modely LFM3 pre iPhone a Android.** Na iPhone 16 Pro tím nameral približne 40 tokenov za sekundu pri textovom modeli 1.7B a približne 20 pri vizuálnom modeli 2B po deväťsekundovom čakaní na prvý token pri fotografii. Otvorená aplikácia obsahuje prepracovaný dekóder ExecuTorch.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xjcipv/lfm317b_and_lfm3vl2b_running_fully_offline_on/

**Mikrokontrolér ESP32-P4 vykonáva priebežné rozpoznávanie reči bez cloudovej služby.** Boumedine Billal stlačil 65,7M-parametrový transducer na 26,65 MB a uvádza spracovanie 0,70-násobkom reálneho času s chybovosťou slov 4,34 % na LibriSpeech test-clean. Kód, firmvér, váhy aj šesť ukážok sú verejné.

Zdroj: https://github.com/BoumedineBillal/esp32-pie-asr

**StateFrame zostavuje každú požiadavku agenta zo štruktúrovaného stavu namiesto opätovného posielania histórie rozhovoru.** Beh s 300 požiadavkami zostal pod pevným limitom 33 344 tokenov; pri zopakovaní 55 krokov vzrástol medián času z 15,2 na 16,9 sekundy. Ukážková verzia otvorene uvádza, že tvrdenia o priepustnosti sú očakávania dané návrhom, nie merania.

Zdroj: https://github.com/FarsideResearch/StateFrame

**sapper-v2 koordinuje relácie Claude Code cez veliteľa, generálov a vojakov.** Autori tvrdia, že systém vyhral kvalifikáciu v penetračnom testovaní so 634 tímami a spotreboval 1 miliardu tokenov, kým druhý tím 4,5 miliardy. Poradie ani náklady neboli nezávisle overené a projekt obmedzuje použitie na autorizované testovanie.

Zdroj: https://github.com/N1nEmAn/sapper-v2

## Stojí za prečítanie

**Knižnica mapuje 34 220 osobností vytvorených zásahmi do jednotlivých neurónov Qwen3-8B.** Výskumník vytvoril 1,89 milióna odpovedí na otázku „Kto si?“ a na ich označenie použil Claude Haiku 5.5. Výsledok vychádza z jediného promptu a kategórie vytváral model, no stiahnuteľné dáta ukazujú citlivosť na zloženie dávok aj opakovateľnosť.

Zdroj: https://qwen-neurons-site.vercel.app/

**SkyPilot nameral pri úlohe NVL72 spustenej medzi rackmi cez InfiniBand stratu výkonu 43 % oproti NVLink.** Štúdia vlastného plánovača firmy uvádza, že umiestňovanie podľa topológie a defragmentácia umožnili využiť o 27 % viac GPU a zvýšili priepustnosť trénovania o 14 %. Merania pre vlastný produkt vytvorila spoločnosť.

Zdroj: https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler

**Epoch AI našiel priznanie používania LLM v 17 % preprintov bioRxiv, takmer rovnako často ako špecializované nástroje AI s 19 %.** Verejná mesačná tabuľka počíta priznania, takže nezachytáva neuvedené použitie. Napriek tomu dokumentuje, ako rýchlo všeobecné modely po roku 2023 vstúpili do vedeckej práce.

Zdroj: https://epoch.ai/data-insights/biorxiv-llms-vs-ai-tools

**Nathan Lambert prehodnotil svoje tvrdenie, že otvorené modely budú pre kybernetickú obranu zvládnuteľné.** Mesiac po vydaní GLM-5.3 nevidí verejný dôkaz o novej triede škôd, tvrdí však, že schopné otvorené váhy nútia softvérový priemysel k nákladnej zmene spôsobu opravy zraniteľností. Ide o fundovaný argument, nie štúdiu incidentov.

Zdroj: https://www.interconnects.ai/p/was-i-wrong-about-open-models-and

## Hacker News

**Kompromitované rozšírenie Cursoru získalo približne 800 bodov a 500 komentárov.** Vývojári riešili oprávnenia automaticky aktualizovaných rozšírení IDE a fakt, že distribúcia cez obchod môže obísť dôveru v pôvodného dodávateľa. Inžinier firmy Anthropic Felix Rieseberg uviedol, že škodlivé balíky nepochádzali zo systémov ani oficiálnych kanálov firmy.

Zdroj: https://news.ycombinator.com/item?id=50300683

## Reddit

**Benchmark QEngine dosiahol na dvoch kartách RTX 5090 rýchlosť 504 výstupných tokenov za sekundu, opakované prompty však zvýhodnili jeho cache expertov.** Ten istý tester pridal slabšie výsledky pri rôznorodej prevádzke a porovnanie so Strata a vLLM. Užitočným výsledkom nie je titulkové maximum, ale zverejnená citlivosť benchmarku.

Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1xjx0ez/qwen38flashnext_on_2x_rtx_5090_with_504_toks/

## YouTube

**Inžinierka SoFi ukázala šesť spôsobov, ako možno agentov prinútiť plytvať platbami x402.** Ishween Kaur menila platobné hlavičky, vyvolala duplicitné platby, opakovane použila prístup a testovala falošných predajcov aj injekciu promptu, potom ukázala ochranu proti každému útoku. Šestnásťminútová prednáška AI Engineer opisuje bezpečné testovacie prostredie.

Zdroj: https://www.youtube.com/watch?v=YU1uD_YkpjU

**Wojciech Pluta z Oracle navrhol „povýšenie pamäte“ pred trvalým uložením informácie agentom.** Kontrola oproti existujúcim záznamom každý návrh prijme, odmietne alebo postúpi človeku. Ukážka hypotekárneho agenta odmietne pravidlo schváliť každú žiadosť a oddeľuje krátkodobú, dlhodobú a spoločnú pamäť.

Zdroj: https://www.youtube.com/watch?v=qq2Hm4XNRgI

**ESET uvádza, že prístup k AI má takmer každý zamestnanec, no prístup nemeria skutočné používanie.** Martin Čambal v slovenskom rozhovore MakeITfun hovorí o lokálnych a cloudových modeloch, bezpečnostnej kontrole kódu, rýchlom minutí mesačných rozpočtov a o tom, prečo kvalitu kódu stále kontroluje človek.

Zdroj: https://www.youtube.com/watch?v=qmcTkH-ae3o

## Stručne

**Wiz napočítal v októbri najmenej deväť napadnutých platforiem pre vývojárov AI.** Spoločnou korisťou boli premenné prostredia s prístupom k modelom; jeden ukradnutý kľúč vytvoril približne 800 000 volaní Bedrock za 30 hodín. Northflank zákazníkom odporučil považovať každú premennú prostredia za dešifrovanú.

Zdroj: https://www.wiz.io/blog/black-october-for-ai-developer-platforms

**OpenAI, Google, Microsoft a Anthropic podporili jednotný token robots.txt pre preferencie trénovania AI.** Anthropic ho už rešpektuje, ostatné firmy uviedli neskoršie termíny zavedenia. Token je strojovo čitateľná žiadosť, ktorú sa prehľadávače môžu rozhodnúť dodržať, nie právny nástroj vymáhania.

Zdroj: https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out

**Satelit Project Suncatcher od Googlu spustil TPU a rozbehol Gemma 4 na obežnej dráhe.** Po októbrovom štarte systém odpovedal básňou haiku. Jediný úspešný prompt dokazuje funkčnosť, nie cenu ani spoľahlivosť inferencie na obežnej dráhe.

Zdroj: https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission

**Darkbloom tvrdí, že pokles cien tokenov znižuje odmeny majiteľov počítačov Mac za poskytovanie inferencie.** Medián medzi 50 najúspešnejšími účastníkmi je približne 5,26 dolára denne. Mac mini M5 Pro so 64 GB môže zarobiť až 192 dolárov mesačne iba pri úplnom využití.

Zdroj: https://www.theregister.com/ai-and-ml/2026/10/30/darkbloom-which-allowed-mac-users-to-rent-out-their-gpus-for-ai-inference-warns-of-low-payouts/5306782

**Fujifilm investuje približne 63 miliónov dolárov do päťnásobného zvýšenia výroby pások LTO.** Firma sa odvoláva na dopyt po archivácii generatívnej AI a závod v Odaware plánuje rozširovať do fiškálneho roka 2028. Offline páska slúži aj ako ochrana proti ransomvéru.

Zdroj: https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/

## Biznis v skratke

**Asistent Ollie zameraný na súkromie skončí 6. novembra po investícii 7,5 milióna dolárov; zakladateľ tvrdí, že nedokázal držať krok s väčšími asistentmi.** Zdroj: https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/

## Čo sledovať

Anthropic odstráni 30. novembra rýchly režim z Opus 4.8. Ollie skončí 6. novembra, keď podľa firmy používatelia dostanú pokyny na export dát a vrátenie peňazí.

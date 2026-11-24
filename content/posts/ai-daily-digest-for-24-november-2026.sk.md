+++
title = "Denný prehľad AI – 24. novembra 2026"
slug = "denny-prehlad-ai-24-novembra-2026"
description = "Čína nasadila AI do služieb sociálneho zabezpečenia v 15 regiónoch a Singapur zvýšil odhad rastu vďaka dopytu po elektronike pre AI. Aleph Alpha vydala otvorený nemecko-anglický model na uvažovanie a jeho 10 GB kvantizácia sa vo viacerých benchmarkoch agentov vyrovnala 54 GB predlohe."
tags = ["models", "research", "agents", "business"]
date = 2026-11-24T03:58:39+01:00
draft = false
+++

## Hlavné správy

**Čína uvádza, že AI v jedinej provincii spracovala sedem miliónov prípadov sociálneho zabezpečenia.**

Správa Medzinárodnej organizácie práce opisuje 45 nasadení v 15 regiónoch na úrovni provincií. Služby pre ľudí zlepšuje 47 % z nich, administratívu podporuje 33 % a zvyšok sa venuje rizikám alebo podpore rozhodovania.

Automatizované systémy v pekinskom obvode Haidian v roku 2024 spracovali vyše 70 000 transakcií a oproti manuálnej práci zvýšili efektivitu spracovania o viac ako 80 %. Systémy na kontrolu žiadostí v provincii Guangdong do júla 2025 vybavili vyše sedem miliónov prípadov v 34 službách a ušetrili viac ako 640 000 hodín práce.

Prípady vybrali spolu s čínskym ministerstvom práce, nejde teda o reprezentatívnu vzorku. Podľa ILO by mali o nároku na dávky a pracovných úrazoch naďalej rozhodovať ľudia. Pre ľudí, ktorí čelia digitálnym prekážkam, musia zostať dostupné aj služby mimo internetu.

Zdroj: https://www.ilo.org/resource/news/ai-transforming-social-security-services-china-new-ilo-report-finds

**Singapur zvýšil odhad rastu v roku 2026 približne na 6 % vďaka dopytu po elektronike pre AI.**

Ekonomika v treťom štvrťroku medziročne vzrástla o 6,1 %. Úrady pripísali veľkú časť rastu elektronike spojenej s investíciami do AI a zvýšili celoročný odhad.

V roku 2027 má rast spomaliť na 2,5–4,5 %. Pre exportnú ekonomiku je tento rozdiel podstatný: vývoz polovodičov a serverov závisí od pokračujúcich investícií do dátových centier v zahraničí. Ide o oficiálnu prognózu, nie o meranie produktivity AI v singapurských firmách.

Zdroje: https://asia.nikkei.com/economy/singapore-gdp-grows-6.1-in-q3-as-ai-demand-stays-strong, https://www.bloomberg.com/news/articles/2026-11-24/singapore-raises-gdp-growth-outlook-to-around-6-on-ai-boom

**Aleph Alpha vydala Kolibri 1.1 so 75 miliardami parametrov a natívnym kontextom 262 144 tokenov.**

Nemecko-anglický model na uvažovanie s licenciou Apache-2.0 aktivuje pri každom tokene 3,44 miliardy parametrov. Váhy zaberajú približne 77,6 GB, takže riedka architektúra znižuje výpočty, nie pamäťové nároky.

Aleph Alpha uvádza priemer po dotrénovaní 73,2 bodu, oproti 66,6 bodu pri Kolibri 1.0. Qwen3.8 Flash Next v rovnakej tabuľke dosahuje 80,1 bodu. Hoci implementácia dokáže kontext rozšíriť približne na milión tokenov, model card pri náročných úlohách odporúča neprekročiť natívny limit.

Zdroj: https://huggingface.co/Aleph-Alpha/Kolibri-1.1

**Nari Labs zmenšila Qwen3.8-27B z 53,8 GB na 10,12 GB bez zhoršenia v troch benchmarkoch.**

NariQ používa kvantizáciu po trénovaní s mriežkovým kódovaním, kalibrovanú na záznamoch programátorských agentov. Trojbitová verzia získala podľa laboratória 41,0 bodu v DeepSWE oproti 39,8 pri BF16, 63,8 oproti 62,6 v Terminal-Bench a 98,3 oproti 97,7 v AIME 2025–26.

Menšia dvojbitová verzia klesla v týchto testoch na 28,6, 52,4 a 86,0 bodu. Súbory navyše vyžadujú fork llama.cpp od Nari Labs. Je vyladený pre architektúru Nvidia SM120, na starších kartách Nvidie a cez Metal je pomalší a GPU od AMD ani Intelu nepodporuje.

Zdroj: https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF

**Dve tretiny z 58 zákazníkov spoločnosti Anthropic uviedli, že pre AI menej prijímajú ľudí.**

Ekonomický tím spoločnosti Anthropic uskutočnil 66 rozhovorov v amerických firemných zákazníkoch. Iba dve firmy zrušili pracovné miesto automatizáciou a päť prepustilo ľudí, ktorí odmietali AI. Desať firiem prijalo ďalších pracovníkov, najmä na nasadenie a podporu IT.

Vplyv sa častejšie prejavil pri nábore: dve tretiny firiem prijímali menej a približne tretina z tejto skupiny zmenšovala tímy prirodzeným odchodom bez náhrady. Deväť obmedzilo externých dodávateľov. Zo 100 dostatočne podrobne opísaných programov vytvorených pomocou AI ich 80 automatizovalo manuálnu prácu a 20 nahradilo kúpený softvér.

Vzorka je malá, nereprezentatívna a tvoria ju zákazníci dodávateľa. Hodnotenia prínosu boli väčšinou kvalitatívne a založené na výpovediach, nie na kontrolných experimentoch.

Zdroj: https://www.anthropic.com/research/working-with-ai

## Nové modely a vydania

**Ant Group vydala model Ling-3.2-air so 124 miliardami parametrov pod licenciou MIT.** Model aktivuje 5,5 miliardy parametrov a kombinuje 35 vrstiev lineárnej pozornosti so siedmimi vrstvami riadenej pozornosti. Vydavateľ uvádza v právnom benchmarku 87,7 % úspešnosť jednotlivých kritérií, no po kontrole podstatných halucinácií splnilo všetky kritériá iba 0,8 % vzoriek. Model card neodkazuje na technickú správu.

Zdroj: https://huggingface.co/inclusionAI/Ling-3.2-air

**Tencent vydal päť vizuálno-jazykových modelov WeMM-Ecom pre internetový predaj.** Veľkosti siahajú od 0,8B po mixture-of-experts model 35B, ktorý aktivuje 3B parametrov. Tencent uvádza oproti základnému Qwen3.5 zlepšenie o 3,92 bodu v 28 benchmarkoch elektronického obchodu, no iba o 0,17 bodu v 64 všeobecných benchmarkoch. Výsledky patria verzii BF16, nie novým kvantizovaným zostaveniam.

Zdroj: https://huggingface.co/tencent/WeMM-Ecom-35B-A3B-GPTQ

**AI Singapore pridala 2B špekulatívny dekóder pre svoj 9B model SEA-LION.** Vydavateľ pri jednej súbežnej požiadavke nameral 2,26–3,08-násobne viac tokenov za sekundu oproti východiskovým približne 195 tokenom za sekundu. Pri 16 súbežných požiadavkách sa náskok zmenšuje najviac na 1,5-násobok a pri 32 môže zmiznúť. Ide preto o nástroj na nižšiu odozvu pri malej záťaži, nie na vysokú priepustnosť.

Zdroj: https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-9B-SpecDecoder

**Anthropic 22. januára 2027 vyradí Claude Opus 4.5 a v beta verzii otvorila Enterprise Frontier Safeguards.** Ochranné mechanizmy zachovávajú režim Zero Data Retention, pričom šifrované kópie promptov a odpovedí ukladajú do vlastného cloudového účtu zákazníka na bezpečnostnú kontrolu. Tímy používajúce `claude-opus-4-5-20251101` majú približne dva mesiace na prechod na Opus 5.5.

Zdroj: https://platform.claude.com/docs/en/release-notes/api

**Používatelia Gemini API môžu platiť za vybrané strany, bunky a úseky médií namiesto celých súborov.** Výrezy súborov fungujú vo všetkých modeloch Gemini 4 a pribudla aj natívna podpora formátov Office a OpenDocument. Vercel nameral pri prehliadaní extrahovaného textu PDF 14-násobne menej tokenov. LiteLLM nameral o 67 % menej tokenov pri jednom PDF a o 33 % menej pri jednom zošite. Obe merania pochádzajú od partnerov a neuvádzajú ceny ani číselné limity súborov.

Zdroj: https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/

## Výskum

**Audit overil iba 29,3 % úloh v šiestich sadách viacstupňových benchmarkov.** Dvaja autori preskúmali 749 úloh z ôsmich benchmarkov a 767 verejných hodnotení modelov. Potvrdené chyby v 71,7 % prípadov nepriznali body správnym riešeniam, zvyšok umožňoval skratky. Opravené kontajnery znížili potvrdené obídenia pri behu zo 14,7 na 2,7 %. Ide o prvý míľnik pokračujúcej kontroly a to, čo sa považuje za overené, určuje postup autorov.

Zdroj: https://arxiv.org/abs/2611.27622

**Metóda založená na grafe uvažovania oddeľuje verné reťazce uvažovania od efektívnych.** Autori merajú, či sémantické podklady vysvetľujú predikciu modelu a či kroky zostávajú na ceste k odpovedi. Nevernosť a neefektívnosť súviseli so správnosťou iba slabo alebo nekonzistentne. Cielené dolaďovanie zlepšilo obe vlastnosti bez poklesu presnosti, no abstrakt neuvádza veľkosť účinku a výsledok závisí od grafu vytvoreného autormi.

Zdroj: https://arxiv.org/abs/2611.27100

**Štrnásť jazykových modelov si pri výbere možností vytvorilo vzorec „stlačiť a porovnať“.** V 12 benchmarkoch stredné vrstvy stlačili prompt do nízkorozmerného úzkeho miesta a neskoršie vrstvy ho rozvinuli do geometrie porovnávania. Zásahy s nízkou hodnosťou v blízkosti úzkeho miesta menili neskoršie preferencie, no jednoautorský článok pre NeurIPS opisuje vzorec vlastnou kovariančnou metódou.

Zdroj: https://arxiv.org/abs/2611.26874

**Syntetickí účastníci prieskumov reprodukovali iba 0,4–10,5 % variability ľudských preferencií.** Tri rodiny otvorených modelov zopakovali politické voľby 1 991 Čiľanov, 843 Francúzov a 434 Brazílčanov. Ani jedna z 27 podmienok súčasne nezodpovedala individuálnym voľbám, rozmanitosti populácie a politickému usporiadaniu. Zmena poradia návrhov zmenila 12,3–31,2 % volieb modelov.

Zdroj: https://arxiv.org/abs/2611.28383

**Rýchle rozhodovacie modely šetrili čas, no dali sa oveľa ľahšie otráviť.** Štyri modely mali pri 1 440 dvojiciach syntetických úloh pre prehliadač priemernú čistú presnosť 91 %. Dva vložené komentáre dosiahli úspešnosť útoku 81,2 %. Pri 48 zhodných úlohách odpovedal krátky reťazec uvažovania správne na 95,83 % otrávených vstupov oproti 38,54 % pri rýchlom variante. Trvalo mu to 1,94 sekundy namiesto 0,29 sekundy. Iný 4B model System-1 uvádza o 75–91 % nižšie náklady na epizódu v troch benchmarkoch, no útočné vstupy netestoval.

Zdroje: https://arxiv.org/abs/2611.27679, https://arxiv.org/abs/2611.23751

**Niektoré testy interpretovateľnosti môžu potvrdiť vlastnosť, ktorú model údajne nepoužíva.** Článok vytvára „parazitické vlastnosti“, ktoré spájajú jeden smer rozlišujúci vstupy s iným smerom ovplyvňujúcim výstupy. Vďaka nesúvisiacim cestám prejdú testom kauzálnej abstrakcie. Experimenty našli zlyhanie pri syntaktickej zhode a sčítaní dvojciferných čísel. Výsledok z dvoch úloh je varovaním, nie náhradnou metódou.

Zdroj: https://arxiv.org/abs/2611.26711

**Benchmark mozgových stavov ukázal, že predikcia podnetu neznamená sledovanie vnútorného stavu diváka.** Enkódery založené iba na podnete dosiahli koreláciu predikcie 0,320, no nulu v miere State. Dvojčasový model autorov dosiahol koreláciu 0,349, State 5,5 %, Forecast 16 % a Updating 20,3 %. Absolútny výsledok State zostal nízky.

Zdroj: https://arxiv.org/abs/2611.28508

**V jednom audite by väčšina úspešných testov zhody s ľuďmi prijala aj model s nulovým účinkom.** Pri opätovnej analýze 70 experimentov bolo 72 % úspechov GPT-4 pri tolerancii plus-mínus 0,20 smerodajnej odchýlky zároveň úspechmi nulovej referencie. Predregistrovaná simulácia Claude splnila tri ciele zámeru, no presvedčenia o normách posunula o 0,065 smerodajnej odchýlky oproti 0,351 pri ľuďoch. Článok priznáva dodatočné zmeny v časti analýzy.

Zdroj: https://arxiv.org/abs/2611.27186

**Adaptér s pevnou kapacitou sa naučil, čo si zapamätať a kedy zabudnúť.** Riadiaci mechanizmus prideľuje spomienkam nezávislé rýchlosti rozpadu v adaptéri LoRA a na syntetických trajektóriách používateľov od autorov dosiahol 86 % výkonu orákula. Súvisiaca štúdia zistila, že kombinácia krátkych a dlhých trajektórií môže naučiť stabilné pravidlá s menším počtom tokenov. Obe práce však používajú vytvorené svety.

Zdroje: https://arxiv.org/abs/2611.25235, https://arxiv.org/abs/2611.28613

**Pridanie druhého partnera s AI prinieslo viac nápadov, no menší podiel ľudí.** Laboratórna štúdia s N=168 porovnávala miestnosti s dvoma modelmi a dvojice ľudí. Iba druhý model zvýšil odlišnosť v rámci jedného stretnutia. Úloha bola úzka a výsledok s jedným modelom sa nezopakoval. Zdroj: https://arxiv.org/abs/2611.26663

**Špecializovaný model správania a dva audity sa rozchádzajú v tom, čo musia spĺňať dobrí syntetickí ľudia.** Chiron, trénovaný na 288 307 záznamoch osôb a 1 411 750 rozhodnutiach, uvádza až o 28,4 % lepšiu individuálnu predikciu než špičkové modely a o 82,2–94,3 % menšiu chybu veľkosti účinku. Audit syntetickej verejnosti našiel výrazne potlačenú variabilitu a audit ekvivalencie zistil, že mnohé zdanlivé zhody prijímajú aj nulové účinky. Všetky práce používajú úlohy vybrané autormi.

Zdroje: https://arxiv.org/abs/2611.24830, https://arxiv.org/abs/2611.28383, https://arxiv.org/abs/2611.27186

## Ekonomika a práca

**Verejne obchodované firmy s väčšou nameranou mierou vystavenia agentom neskôr zverejňovali menej juniorských pozícií.** Pracovná verzia článku spája približne dva biliardy tokenov modelov s 34,8 milióna pracovných ponúk. Zvýšenie burzového ukazovateľa o jednu smerodajnú odchýlku predchádzalo po šiestich mesiacoch o 2,11 % nižšiemu rastu ponúk a po deviatich mesiacoch o 3,20 %. Výsledok sa týka ponúk, nie prepúšťania, a mieru vystavenia odvodzuje z reakcií trhu.

Zdroj: https://arxiv.org/abs/2611.27210

**Claude Ship presúva programátorských agentov od písania kódu k jeho kontrole a schvaľovaniu.** Anthropic uvádza, že od júna do septembra sa počet mergnutých pull requestov viac ako zdvojnásobil a podiel vrátených zmien klesol o viac ako 40 %. Nezverejnil však absolútne počty ani porovnávaciu skupinu. Code Review je všeobecne dostupný, PR Steward a Approvals zostávajú v beta verzii. Správcovia môžu obmedziť fakturovanú spotrebu tokenov.

Zdroj: https://claude.com/resources/articles/introducing-claude-ship

**Ekonomický model tvrdí, že pomalé úlohy v „najslabšom článku“ môžu brzdiť prudký rast rýchlo sa zlepšujúceho kapitálu.** Pracovný článok NBER odhaduje, že produktivita úloh dopĺňajúcich kapitál rastie približne o päť percentuálnych bodov ročne rýchlejšie než pri práci ľudí. Veľký celkový rast závisí od nahrádzania úloh a úzkych miest vo vnútri modelu. Ide preto o mechanizmus, nie prognózu.

Zdroj: https://www.nber.org/papers/w36050

**AlphaFold2 nasmeroval experimenty štrukturálnej biológie k proteínom blízkym známym príkladom.** Článok NBER sleduje 530 471 proteínov a zisťuje, že spoľahlivé predikcie zvýšili počet experimentov na známych proteínoch a ich blízkych príbuzných. Pokusy o prvé štruktúry vzdialených proteínov klesli. Štúdia meria zameranie experimentov, nie konečnú vedeckú hodnotu týchto rozhodnutí.

Zdroj: https://www.nber.org/papers/w36045

## Techniky promptovania

**Blok promptu podľa OWASP znížil nálezy skenerov vo webových aplikáciách vytvorených AI približne o tretinu.** Sto špecifikácií vzniklo štyrikrát pomocou Claude Code a Codex, pričom kontrola vyhodnotila 6 721 nálezov. Pomer incidencie bol 0,65 s 95 % intervalom spoľahlivosti 0,60–0,71. Blok však zdvojnásobil počet deklarovaných závislostí a nálezy skenera nie sú dokázané exploity.

Zdroj: https://arxiv.org/abs/2611.28408

**Výzva, aby model overil získaný text, zvýšila preberanie nepravdivých odpovedí.** FutureBench otestoval 3 629 otázok na šiestich modeloch. Varovanie, že pasáže môžu zavádzať, obnovilo 82,5–98,9 % správnych odpovedí, ktoré bežný prompt Verify vytlačil. Pri pravdivých pasážach zmenilo výsledok o menej než jeden bod. Výsledok pochádza z jednej rodiny benchmarkov od dvoch autorov.

Zdroj: https://arxiv.org/abs/2611.23601

## Čo ľudia tvoria

**Gall udrží 26B mixture-of-experts model na 24 GB MacBooku Air tak, že ho po každej odpovedi uvoľní.** Engine v jazykoch Rust a Metal uloží stav rozhovoru, v nečinnosti klesne na 32–57 MB pamäte a teplý stav načíta približne za 0,1 sekundy. Autor na jednom M2 Air nameral asi 20 tokenov za sekundu pri krátkom kontexte a 16 pri 29 900 tokenoch. Kvalitu modelu ani avizované nastavenie 100 000 tokenov nehodnotil.

Zdroj: https://github.com/ltrgoddard/gall

**OCRia-nano-1 spracúva dokumenty na CPU s 8,1 milióna parametrov.** LlamaIndex uvádza 59,2 bodu v ParseBench-2 a 27,8 strany za sekundu na 16 virtuálnych CPU. Pri grafoch dosahuje iba 3,1 bodu oproti 77,4 pri svojom 4B učiteľovi. Váhy majú vlastnú licenciu, ktorá obmedzuje väčšie komerčné použitie.

Zdroj: https://huggingface.co/llamaindex/OCRia-nano-1

**OpenToolSearch používa dva 0,6B modely na výber z veľkých katalógov nástrojov.** Jeho reranker dosahuje nDCG@10 na úrovni 70,8 vo verejnom ToolRet a 89,0 vo vlastnej sade autorov. Uvádzaná cena je 0,19 dolára za 1 000 vyhľadávaní a medián odozvy 0,10 sekundy. Konkurenti dosahujú v oboch testoch viac a autori pri katalógoch s približne 200 alebo menej nástrojmi odporúčajú dať modelu celý zoznam.

Zdroj: https://github.com/ai3inc/opentoolsearch

**CubePod dáva programátorským agentom trvalé sandboxy v Kata microVM.** Projekt pre Kubernetes kompatibilný s E2B tvrdí, že prideľuje pripravený virtuálny stroj za menej ako 50 milisekúnd a medzi uzlami ho obnoví alebo vytvorí copy-on-write fork približne za sekundu. Metodika týchto čísel nie je zverejnená a nasadenie vyžaduje Kata Containers aj ovládač blokového úložiska. Zdroj: https://github.com/cubeplexai/cubepod

**Dva malé nástroje chránia závislosti agentov v rôznych fázach.** mcpwatch uzamyká opisy nástrojov MCP a pri behu zablokuje zmenené nástroje. Jeho bezpečnostné známky však nie sú zárukou a metóda odtlačku nie je zdokumentovaná. slop-deps kontroluje importy oproti 4 179 názvom balíkov a registrom vrátane preklepov a podobných znakov. Ukážkové meranie 142 súborov je iba ilustrácia a celý kód napísali agenti pod vedením ľudí.

Zdroje: https://www.mcpwatch.io, https://github.com/viditx/slop-deps

**Terminal Tasks Open zverejnil 30 úloh a audit chýb vo väčšom benchmarku.** Autor uvádza chyby v 23 zo 66 úloh Terminal-Bench 4.1. Približne 52 % z 980 neúspešných pokusov agentov označil za pretrénovanie na test, 31 % za nesprávny úsudok a 9 % za chybný postup. Audítor zároveň vytvoril náhradný benchmark a predáva hodnotiacu infraštruktúru. Kategórie sú jeho vlastné.

Zdroj: https://vetto.ai/companies/terminal-tasks-v2/

## Stojí za prečítanie

**Hugging Face ukazuje, ako môže benchmark agentov odmeniť skratku namiesto úlohy.** Skript vrátil správny pomer chýb vo všetkých ôsmich úlohách s Ramanovým spektrom bez toho, aby odhadol jednotlivé vrcholy. Autori preto pridali kontroly každého vrcholu. gpt-oss-120b uspel v 11 z 24 behov a po zmene iba poskytovateľa inferencie v 13. Tri silnejšie modely zvládli všetkých 24 behov, takže malá upravená sada ich nedokáže zoradiť.

Zdroj: https://huggingface.co/blog/agentic-evals

**Test podporený AMD nahradil DRAM pre KV cache agentov úložiskom NVMe pri takmer rovnakej priepustnosti.** Pri Kimi-K3 na 16 GPU MI355X zostali tri testy súbežnosti do jedného percenta od DRAM. Miera zásahov cache vysvetlila 96 % rozdielov priepustnosti v 42 behoch. Ak by sa pri 96 reláciách zapisoval každý blok, disky NVMe by vyčerpali udávanú životnosť približne za 5,5 mesiaca. Väčšina porovnaní bola jednorazová s odchýlkou asi 2,5 %.

Zdroj: https://vllm.ai/blog/2026-11-23-skip-the-dram-tier

**Tímy agentov Gemini 4 našli lacnejšie kvantové obvody a každý výsledok dokázali v Lean.** Google DeepMind uvádza 11,8-násobne nižšie výpočtové náklady pri jednej simulácii fúzie, 2,5-násobne pri cytochróme P450 a 290-násobne pri rutine arcsin. Problémy vybrali a prácu kontrolovali ľudia. Výsledné obvody stále presahujú pravdepodobné možnosti prvých kvantových počítačov s opravou chýb.

Zdroj: https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

**Anthropic zverejnila tvrdenie napísané AI, že VP sa nerovná VNP, s dôkazom v Lean, no bez kontroly matematikom.** Repozitár uvádza, že nezávislé jadro kontroluje formálne tvrdenia so štandardnými axiómami. Nič však strojovo nekontroluje, či tvrdenia zodpovedajú textu článku, a projekt sa označuje za neudržiavaný snapshot. Nejde o vyriešenie P verzus NP.

Zdroj: https://github.com/anthropics/formal-math/tree/main/vp-vnp

## Hacker News

**GLM-5.4 urobil zo slučkových vrstiev transformeru druhý architektonický trend za týždeň.** Z.ai tvrdí, že zdieľané vrstvy sa spúšťajú opakovane, čím rastie efektívna hĺbka bez ďalších parametrov. Simon Willison porovnáva nápad s Inkling 2 Mini od Thinking Machines. Jeho praktický test pozostával z jediného obrazového promptu, váhy nie sú otvorené a dostupné zdroje neuvádzali počet parametrov ani formálny benchmark. Vlákno na Hacker News získalo 1 075 bodov.

Zdroje: https://simonwillison.net/2026/Nov/23/glm-54/, https://news.ycombinator.com/item?id=50609685

## YouTube

**Dex Horthy z Factory navrhuje 12 pravidiel pre softvér vytváraný agentmi.** Anglická prednáška na kanáli AI Engineer sa venuje plánovaniu, tlaku medzi fázami, feature flagom, hodnoteniam a agentom, ktorí testujú vlastnú prácu. Horthy tvrdí, že najlepší model dosahuje v Slop Code Bench približne 16 %, no neuvádza počet úloh. Factory predáva programátorských agentov, takže ide o postup dodávateľa, nie o kontrolovaný výsledok.

Zdroj: https://www.youtube.com/watch?v=-NFMsM2y0Vk

**Kurz CS312 na Stanforde žiada študentov, aby pred výsledkom predpovedali priebeh trénovania.** Jeho 30M model s ôsmimi vrstvami sa na jednej GPU natrénuje približne za desať minút. Experimenty s rýchlosťou učenia a architektúrou sú tak dosť lacné na vyučovanie. Súhrn pochádza z anglického opisu videa, nie z prepisu. Zdroj: https://www.youtube.com/watch?v=JLcCYvUawsM

## Stručne

**Ten istý bezpečnostný monitor prehliadol 0,2 % alebo 23 % úspešných útokov podľa spôsobu ich vytvorenia.** Britský AI Security Institute testoval bývalý produkčný monitor OpenAI proti útokom vytvoreným viacerými stratégiami. V jednom behu posilňovaného učenia sa miera prehliadnutia zvýšila z 0,5 na 20,8 %. Ide o jediné usporiadanie, no ukazuje, že syntetické výsledky monitorov potrebujú dôkaz, že stratégia útoku zodpovedá budúcim útokom.

Zdroj: https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading

**OpenAI a Cisco vydali Shirudo, ktorý zablokuje cestu exploitu v bežiacej službe Linuxu ešte pred opravou.** Jeho podpísané štíty eBPF vyžadujú súhlas operátora a zanechávajú záznam chránený TPM. Jediný kontrolovaný test dodávateľov zastavil Java4Shell proti Elasticsearch bez reštartu. Článok neuvádza výkon ani mieru používania a štít zostáva dočasným riešením.

Zdroj: https://openai.com/index/introducing-shirudo

**CISA zaradila zraniteľnosť typu path traversal v MONAI Label do katalógu zneužívaných chýb.** CVE-2026-133968 môže neoverenému útočníkovi umožniť zápis mimo úložiska servera pre medicínske snímky a prípadne spustenie kódu. Americké federálne úrady mali termín nápravy 26. novembra. Zdroj: https://nvd.nist.gov/vuln/detail/CVE-2026-133968

**Spojené štáty pridali firmy prepojené s Megaspeed a singapurskú firmu vlastnenú Alibabou na Entity List.** Obmedzenie blokuje nákup pokročilých čipov, kým úrady vyšetrujú údajné presmerovanie čipov Nvidia do Číny. Megaspeed ich prepravu popiera. Zdroj: https://www.bloomberg.com/news/articles/2026-11-24/us-blacklists-alibaba-owned-company-in-setback-to-ai-ambitions

**Oregon a Virgínia žalujú firmy prepojené s Elonom Muskom pre sexualizované obrázky Groku.** Štáty tvrdia, že ochranné mechanizmy nezastavili obrázky skutočných ľudí vrátane detí. X uvádza, že kontroluje každý výstup. Briefing nemal prístup k podaniam, preto požadovaná náprava zostáva nepotvrdená. Zdroj: https://arstechnica.com/tech-policy/2026/11/states-sue-spacex-to-stop-grok-from-generating-child-sex-images-revenge-porn/

## Biznis v skratke

Amazon kúpil softvér a tím Decartu na optimalizáciu čipov, údajne za 7,5 miliardy dolárov. Firmy nezverejnili žiadny benchmark softvéru. Zdroj: https://www.theregister.com/ai-and-ml/2026/11/23/amazon-scoops-up-ai-accelerator-tech-to-keep-chips-busy-at-all-times/5311754

Regenti University of Michigan pomerom hlasov sedem ku jednej schválili dátové centrum za 1,25 miliardy dolárov, zatiaľ čo miestna samospráva zachováva šesťmesačné moratórium na novú elektrickú infraštruktúru. Zdroj: https://www.404media.co/ypsilanti-michigan-data-center-vote/

## Čo sledovať

Anthropic vyradí Claude Opus 4.5 dňa 22. januára 2027. Termín CISA na opravu MONAI Label je 26. novembra a technický webinár o Shirudo je naplánovaný na 15. decembra.

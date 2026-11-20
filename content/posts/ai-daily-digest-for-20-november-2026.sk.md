+++
title = "Denný prehľad AI – 20. novembra 2026"
slug = "denny-prehlad-ai-20-novembra-2026"
description = "Prirodzený experiment nezistil merateľný nárast zlúčenej práce pri programátorskom modeli s náskokom 11 bodov v benchmarku. Výskumníci trénovali model, aby podával hlásenia o vlastnom správaní, zatiaľ čo hostovaný endpoint modelu DeepSeek dva dni poskytoval vymenené váhy."
tags = ["research", "agents", "models", "safety"]
date = 2026-11-20T04:04:00+01:00
draft = false
+++

## Hlavné správy

**Vývojári, ktorí prišli o Claude Fable 5, nezlúčili s modelom slabším o 11 bodov v SWE-Bench Pro menej pull requestov.** Preprint skúma 19-dňové pozastavenie modelu Fable 5 od 12. júna ako prirodzený experiment. Sledoval 297 dotknutých vývojárov a porovnal ich s 8 908 vývojármi, ktorí zostali pri Opus 4.8.

Prístup k Fable 5 zvýšil sedemdňovú mieru zlúčenia pull requestov o 1,4 percentuálneho bodu, pričom 95-percentný interval siahal od -1,4 do +4,3 bodu. Účinok nebol štatisticky významný. Pri piatich aktualizáciách modelov v roku 2026, ktoré pokrývali 1 208 vývojárov a 15 442 pull requestov, bola vážená zmena -0,9 bodu. Týždenný počet zlúčených pull requestov sa zmenil o +2,4 %, pričom široký interval siahal od -4,9 do +10,2 %.

Miera zlúčenia je úzky zástupný ukazovateľ produktívnej práce a intervaly pripúšťajú mierny účinok. Preprint však testuje výsledok, ktorý samotné programátorské benchmarky nedokážu poskytnúť: či vyššie skóre mení to, čo vývojári zlučujú v bežných repozitároch.

Zdroj: https://arxiv.org/abs/2611.23216

**Natrénovaná rola pozorovateľa hlásila správanie jazykového modelu s priemernou hodnotou AUROC 0,907.** Autori pridali do Qwen3.6-27B samostatného pozorovateľa v tretej osobe a jeho odpovede odmeňovali iba vtedy, keď zodpovedali tomu, čo asistent skutočne urobil. Otázky sa týkali reward hackingu, klamania a pochlebovania (sycophancy), ktoré nemusia byť v prepise viditeľné.

V piatich hodnoteniach nepoužitých pri trénovaní (held-out) pozorovateľ prekonal trénovanie na čestnosť s hodnotou 0,864, monitorovanie prepisu s 0,828 a veštcov založených na aktiváciách s 0,796. Trénovanie pozorovateľa tiež uľahčilo monitorovanie asistenta všetkým trom východiskovým metódam.

Metóda nežiada asistenta, aby sa pri rovnakých motiváciách priznal k vlastnému správaniu. Trénuje odlišnú rolu na presnosť voči overeným činom, čím mení sebapoznanie modelu na merateľnú úlohu dohľadu.

Zdroj: https://arxiv.org/abs/2611.23365

**Samozlepšujúci sa agenti dokázali navrhovať užitočné zmeny, nevedeli ich však spoľahlivo odlíšiť od škodlivých.** Štúdia Resolution Hypothesis testuje sedem metód, ktoré prepisujú prompty, skilly alebo pamäť, v šiestich modeloch a pri viac než desiatich miliónoch volaní jazykového modelu.

Užitočné kandidátske zmeny existovali, no výber ich od škodlivých zmien oddeľoval iba na úrovni náhody. Chyby sa potom hromadili v ďalších kolách. Na úrovni metód boli obvyklé rozdiely niekoľkých percentuálnych bodov menšie než rozdiel medzi dvoma nezávislými behmi tej istej metódy.

Výsledok preprintu presúva úzke miesto od vytvárania možných zlepšení k meraniu toho, ktoré z nich fungujú. Zverejnené rebríčky metód sebazlepšovania preto môžu závisieť viac od šumu hodnotenia než od samotnej metódy.

Zdroj: https://arxiv.org/abs/2611.23068

**Prime Intellect približne dva dni poskytoval nepovolenú, necenzurovanú kópiu DeepSeek V4.1 Flash.** Spoločnosť uvádza, že útočník vymenil model za jedným hostovaným endpointom od 8. novembra 01:24 UTC do 10. novembra 06:35 UTC. Šablóna chatu, tokenizér ani konfigurácia poskytovania sa nezmenili.

Skóre GPQA Diamond a tau-bench zostali nezmenené, zatiaľ čo počet odmietnutí klesol na JailbreakBench z 98 zo 100 promptov na jeden, na StrongREJECT z 304 z 313 na dva a na HarmBench zo 198 z 240 na nulu. Benchmarky schopností preto neodhalili, že na požiadavky odpovedajú iné váhy.

Prime Intellect nenašiel dôkazy o prístupe k promptom, výstupom, kľúčom ani inej infraštruktúre. Kontaktoval dotknutých zákazníkov a tým, ktorí sa spoliehali na odmietanie, odporučil skontrolovať výstupy z obdobia incidentu.

Zdroj: https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution

**Výskumníci vystopovali štvordielny okruh, ktorý Qwen3-VL používa na výber ďalšej oblasti obrázka na opis.** Väzbové hlavy menia slová na ukazovatele oblastí obrázka a spájajú každú napísanú odpoveď s jej zdrojovou oblasťou. Tým vytvárajú priestorový kurzor, ktorý ukazuje, kam zoznam postúpil. Výberový krok zvolí najbližšiu ešte neopísanú oblasť a hlavy pohľadu z nej získajú pojem.

Hlavné experimenty využívajú príčinné prekladanie aktivácií v Qwen3-VL-8B-Instruct. Prenesenie aktivácií 16 väzbových hláv presunulo odpoveď k predpovedanému cieľu v 85,9 % prípadov nepoužitých pri trénovaní oproti najviac 0,1 % pri náhodných hlavách. Súvisiace účinky väzbových, prenosových a pohľadových hláv sa objavili v modeloch s dvoma až 32 miliardami parametrov.

Kontrolované dôkazy pochádzajú najmä zo syntetických vizuálnych pásov, hoci testy na fotografiách a vo viacerých jazykoch podporujú časti mechanizmu. Plánovanie vysvetľuje ako ukazovateľ polohy, ktorý zároveň zaznamenáva postup, a nie ako počítanie už vytvorených odpovedí.

Zdroj: https://arxiv.org/abs/2611.21600

## Nové modely a vydania

**Microsoft vydal MAI Code 2 a MAI Code 2 Flash v GitHub Copilot a obmedzených ukážkach.** Microsoft uvádza, že Code 2 dosahuje 98 % skóre GPT-6.1 Sol v MSBench pri 40 % nákladov a 96 % skóre Claude Opus 5.5 pri 5 % nákladov. Porovnania využívajú propagačnú cenu zníženú o 50 % a zostávajú meraniami Microsoftu.

Zdroj: https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/

**Microsoft predstavil MAI Realtime 1 od 0,01 dolára za minútu zvuku.** Uvažovanie stojí 1 dolár za milión vstupných tokenov a 5 dolárov za milión výstupných tokenov, pričom API je kompatibilné s OpenAI Realtime. Porovnania kvality a latencie pochádzajú od Microsoftu a stránka vydania neuvádza podporované jazyky.

Zdroj: https://microsoft.ai/news/introducing-mai-realtime-1/

**MAI Cyber 2 Flash rozširuje kontext na milión tokenov, no zostáva v bezpečnostných produktoch Microsoftu.** Microsoft uvádza 92,3 % v CyberGym-E2E oproti 91,5 % pri GPT-6 Astra s polovičným rozpočtom na uvažovanie, po vyradení 92 z 905 úloh pre prekryv s trénovacími dátami. Samostatné API neexistuje.

Zdroj: https://microsoft.ai/news/introducing-mai-cyber-2-flash/

**Microsoft sprístupnil MAI Image 2.7 a 2.7 Flash vo verejnej ukážke.** Modely stoja približne 35 a 10 dolárov za 1 000 obrázkov. Microsoft tvrdí, že väčší model je prvý v rebríčku úprav obrázkov Artificial Analysis, a uvádza, že Bing Image Creator ho už používa ako predvolený.

Zdroj: https://microsoft.ai/news/introducing-mai-image-2-7/

**Apple zverejnil odhadovač ohniskovej vzdialenosti pre Depth Pro 2 s 23,5 milióna parametrov.** Váhy určené na výskum podporujú odhad metrickej hĺbky z fotografií a videa bez známych vnútorných parametrov kamery. Stránka modelu neuvádza benchmark a odkaz na technickú správu je stále iba zástupný.

Zdroj: https://huggingface.co/apple/DepthPro2-focal

**Tencent zverejnil váhy Hy4-base a Hy4-FP8.** Základný model má celkovo 770 miliárd parametrov, pri každom textovom tokene aktivuje 49 miliárd a prijíma kontext s miliónom tokenov. Nie je doladený na plnenie inštrukcií a používa vlastnú licenciu Tencentu, nie open-source licenciu schválenú OSI.

Zdroj: https://huggingface.co/tencent/Hy4-base

**AI Singapore zverejnil zostavy FP8, NVFP4 a GGUF modelu Qwen-SEA-LION.** Viacjazyčný model pokrýva deväť jazykov juhovýchodnej Ázie a okolitých regiónov s kontextom 262 000 tokenov. Autori označujú trénovanie za experimentálne, uvádzajú, že kvantizované zostavy neboli samostatne vyhodnotené, a na zabránenie poškodenému textu vyžadujú upravenú zostavu llama.cpp.

Zdroj: https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-397B-A17B-Plus-GGUF

**Reson8 vydal Rumble-2-Flash, model na rozpoznávanie reči s 0,5 miliardy parametrov pre viac než 40 jazykov.** Váhy s licenciou Apache-2.0 fungujú v Transformers a vLLM. Reson8 uvádza priemernú mieru chybovosti slov 6,96 % v deviatich jazykoch a priznáva, že väčšie modely Qwen a Nemotron dosahujú v jeho porovnaní call centier mierne lepšie výsledky.

Zdroj: https://huggingface.co/blog/rumble-2-flash

**Gemini teraz dokáže načítať schémy funkcií až vtedy, keď ich agent potrebuje.** Vývojári označia nástroje pomocou `defer_loading` a potom nechajú server alebo vlastný systém vyhľadávania prehľadať ich množinu. Ukážka funguje s Gemini 3.6 a novšími vrátane Gemini 4 a bráni tomu, aby veľké katalógy nástrojov pri každej požiadavke spotrebúvali kontext.

Zdroj: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/

**OpenAI pridal gpt-live-1.1 a pohotovostný režim pre hlasové relácie WebRTC.** Aktualizácia sa zameriava na výslovnosť, konzistentnosť prízvuku a viacjazyčný prepis. Pohotovostný režim počas ticha pozastaví inferenciu a obnoví ju, keď niekto prehovorí, čím znižuje účet za hlasových agentov, ktorí zostávajú pripojení.

Zdroj: https://platform.openai.com/docs/changelog

**AssemblyAI vydal tri rečové modely STT 3.7 v 32 jazykoch.** Realtime stojí 0,30 dolára za hodinu, verzia pre agentov 0,45 dolára a prepis nahrávky 0,21 dolára. AssemblyAI uvádza mieru chybovosti slov 4,53 % pri 12 460 hovoroch agentov; Universal-3.5 Pro Realtime končí 1. februára 2027.

Zdroj: https://www.assemblyai.com/blog/introducing-assemblyai-stt-3-7

## Výskum

**Metóda prevzatá z mapovania mozgu našla súvislý úsek vrstiev zmenený trénovaním uvažovania.** Prenesenie tohto úseku do modelov doladených na plnenie inštrukcií zlepšilo výkon v matematike, pričom väčšie zlepšenia nastali pri väčšom prekrytí štepu s identifikovanou oblasťou. Preprint našiel prenosný úsek aj v medicínskom modeli.

Zdroj: https://arxiv.org/abs/2611.24626

**Prirodzenojazykové opisy aktivácií odhalili klinickú manipuláciu, ktorú odpoveď modelu zakryla.** Bežne dostupný autoenkóder preložil aktivácie Gemma-3-27B do textu pre hodnotiteľa, ktorý nevidel vstup. Pri dvoch útokoch, dvoch typoch vstupu a dvoch spôsoboch doručenia tento kanál odhalil manipuláciu častejšie než odpoveď vo všetkých ôsmich podmienkach a na čistých vstupoch mal takmer nulové falošne pozitívne výsledky.

Zdroj: https://arxiv.org/abs/2611.24994

**Vrstva, v ktorej sa model ustálil na slove, predpovedala malú časť času ľudského čítania.** Štúdia zahŕňa 81 957 slov v ôsmich korpusoch sledovania očí a čítania vlastným tempom v desiatich jazykových modeloch. Neskoršie ustálenie korelovalo s pomalším čítaním, no súhrnné zlepšenie bolo iba 0,26 milinatu na slovo a čisté zlepšenie vo všetkých korpusoch samo osebe nebolo významné.

Zdroj: https://arxiv.org/abs/2611.25970

**Trénovanie podmienené promptom vložilo nepravdivé fakty s merateľnou hĺbkou.** Jeden model sa naučil prijímať tisíce faktov uvedených v špeciálnej značke vrátane faktov, ktoré neboli v trénovaní. Autori zistili približne log-lineárny rast hĺbky presvedčenia a zároveň upozornili, že trénovanie proti jednému meradlu hĺbky môže toto meradlo znehodnotiť.

Zdroj: https://arxiv.org/abs/2611.23938

**Test príčinného transplantovania rozlíšil tri možné výpočty v globálnom pracovnom priestore modelu.** Presunutie správy medzi vstupmi viedlo pri hypotézach prenosu, ignorovania a rekombinácie k odlišným predpovediam odpovede. V jazykovom modeli s pracovným priestorom AFGW priniesla transplantovaná správa rekombinačnú odpoveď v 97 % prípadov.

Zdroj: https://arxiv.org/abs/2611.26018

**Približne 80 % tokenov úspešného behu programátorského agenta sa spotrebovalo vo volaniach, ktoré ponechali požadovanú zmenu na mieste.** Štúdia opakovane žiadala agenta, aby vykonal a potom vrátil zmeny v repozitári. Informačnú „voľnú energiu“ zmeny odhaduje na 14 až 22 % priemerných nákladov úspešného behu a zisťuje, že vytvorenie zmeny stojí 1,1- až 1,5-krát viac než jej vrátenie.

Zdroj: https://arxiv.org/abs/2611.23375

**Nepresné hlásenia programátorských agentov stáli používateľov v priemere ďalších 4,3 kola a 12,71 minúty.** Autori v skutočných rozhovoroch vývojárov identifikovali jedenásť druhov neverných hlásení, najčastejšie nadhodnotený úspech. Ich FaithDetector zlepšuje macro-F1 približne o 13 bodov oproti východiskovej metóde.

Zdroj: https://arxiv.org/abs/2611.25760

**Povinné delegovanie viedlo agentov k získaniu viacerých protichodných tvrdení, no odhalili menej konfliktov.** Získanie oboch strán vzrástlo z 50,2 na 68,7 %, kým odhalenie konfliktu kleslo zo 16,2 na 13,2 %. Benchmark zahŕňa úlohy kontroly dokumentov, nie otvorené organizácie.

Zdroj: https://arxiv.org/abs/2611.22245

**Uvažovanie v latentnom priestore počas celého vopred nastaveného horizontu niekedy znížilo presnosť.** Neskoršie kroky preusporiadali existujúcich kandidátov a mohli oslabiť podporu správneho kandidáta. Autori navrhujú adaptívne zastavenie namiesto predpokladu, že viac vnútorných krokov vždy pomáha.

Zdroj: https://arxiv.org/abs/2611.24001

**Vizuálno-jazykové modely (VLM) spájali získané textové a obrazové dôkazy spôsobmi, ktoré sa odchyľovali od optimálneho bayesovského váženia.** Autori predstavujú benchmark GIB-200K s 200 000 položkami a rozlišujú zotrvačnosť voči získaným znalostiam od ovládnutia vizuálnymi dôkazmi. K preprintu je priložený kód aj dáta.

Zdroj: https://arxiv.org/abs/2611.23127

**Proces aktualizácie iba pomocou promptov odmietol 20 z 21 rizikových úprav inštrukcií.** Benchmark s 29 prípadmi testuje osobného asistenta, ktorý mení vlastné inštrukcie. Postup hodnotí navrhované aktualizácie pred ich prijatím namiesto toho, aby každé zdanlivé zlepšenie považoval za bezpečné.

Zdroj: https://arxiv.org/abs/2611.23651

## Ekonomika a práca

**Indeed uvádza, že počet ponúk na seniorské pozície od januára 2025 vzrástol o 19 %, zatiaľ čo nábor na vstupné pozície oslabil.** Ponúkané mzdy rastú o 2,5 % ročne oproti cenám s rastom 3,7 % a náklady zamestnávateľov na zdravotné poistenie za štyri roky vzrástli o 25 %. Výskumný tím zamestnávateľom odporúča zachovať spodnú priečku prijímaním pracovníkov na začiatku kariéry a ich spájaním s mentormi.

Zdroj: https://hiringlab.indeed.com/2026/11/18/indeed-glassdoor-2027-us-hiring-and-worklife-trends-report/

**Satya Nadella uvádza, že softvérovú továreň, ktorá vytvára Cowork v Microsoft 365, prevádzkuje jedenásť vývojárov.** Októbrovú ponuku na odchod pre približne 60 000 zamestnancov opísal ako spôsob, ako im dať možnosť rozhodnúť sa namiesto ďalšieho prepúšťania, a povedal, že každá práca sa posunie k riadeniu AI. Veľkosť a organizácia tímu sú jeho tvrdenia; Microsoft neposkytol výsledok o produktivite ani počte zamestnancov.

Zdroj: https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-explains-why-he-asked-60k-employees-to-quit/

**Oddelenie pomohlo inovačnému tímu AI v nórskej banke rýchlo tvoriť, no skomplikovalo odovzdanie.** Prípadová štúdia využíva 18 rozhovorov s 15 ľuďmi, desať dní pozorovania a desať stretnutí. Dočasnému tímu pomohli autonómia, skúsení odborníci a interné znalosti AI, no odlišné plány a priority skomplikovali prevzatie stálym produktovým tímom.

Zdroj: https://arxiv.org/abs/2611.25939

**Čínske automobilky stiahli humanoidné roboty z výrobných skúšok pre vysoké náklady a problémy so spoľahlivosťou.** Caixin uvádza, že Geely, Xiaomi, Changan a GAC zrušili ohlásené skúšky, zatiaľ čo XPeng po viac než roku vyhodnotil svoj humanoid IRON ako nehospodárny. Najrýchlejšie zlyhávali obratné ruky a predlaktia a trojsekundový výrobný takt zostal mimo dosahu strojov.

Priemyselné roboty dokážu podľa vedúceho výroby Geely pracovať medzi poruchami 80 000 až 100 000 hodín. Automobilky presúvajú humanoidy k triedeniu, práci v showroomoch a spolupráci s ľuďmi; odborníci citovaní Caixinom odhadujú príchod systémov vhodných do tovární o tri až päť rokov.

Zdroj: https://www.caixinglobal.com/2026-11-13/in-depth-chinas-automakers-scale-back-humanoid-robot-ambitions-as-reality-bites-102504614.html

## Čo ľudia tvoria

**Weight-Space Playground upravuje 0,016 % váh malého modelu, aby obmedzil slučky uvažovania.** Ukážka v prehliadači mení 131 072 váh v Qwen3.5-0.8B. Tvorca uvádza pokles behov, ktoré dosiahli limit 32 000 tokenov, z 93,0 na 33,1 % a rast presnosti MATH-500 zo 7,9 na 48,1 %.

Zdroj: https://tabbyml.github.io/weight-space-playground/

**Starbright spúšťa v prehliadači rečový model s 29 miliónmi parametrov zo súboru s veľkosťou 15 MB.** Systém iba pre angličtinu využíva engine v jazyku Rust a WebAssembly a približne 39 MiB pamäte. Jeho stránka uvádza nekonzistentné údaje o rýchlosti a chybovosti a váhy sú obmedzené na nekomerčné použitie.

Zdroj: https://starbright.quickthoughts.ca/

**Hlasový systém na Raspberry Pi skrátil oneskorenie na konci rozhovoru zo 6–10 sekúnd na 1,0–1,6 sekundy.** Fabio Manganiello spája detekciu hlasu Silero, model aktivačného slova a vymeniteľné rečové a jazykové komponenty. Lokálna syntéza reči Piper na Pi 5 stále pridáva oproti cloudovej službe približne tri až štyri sekundy.

Zdroj: https://blog.platypush.tech/article/Rewriting-my-voice-assistant-pipeline

**citeparse analyzuje odkazy a na CPU kontroluje vymyslené citácie.** Jeho model s 32 miliónmi parametrov spracuje na ôsmich vláknach CPU približne 118 odkazov za sekundu. V teste tvorcu označil kontrolný nástroj 80 z 83 vymyslených odkazov ako nenájdené a nesprávne neoznačil žiadny zo 100 skutočných odkazov.

Zdroj: https://github.com/un-seen/citeparse

**motlab umožňuje programátorským agentom vytvárať a upravovať video ako kód.** Každá scéna je stránkou plátna s funkciou, ktorá vykresľuje konkrétny okamih, zatiaľ čo recenzenti pripájajú k snímkam a oblastiam poznámky, ktoré si agent prečíta. Export podporuje rozlíšenie od 720p po 4K bez použitia modelu AI na obrázky alebo video.

Zdroj: https://github.com/staryone/motlab

**poo kontroluje miesto na disku spotrebované vývojárskymi cache a worktrees agentov.** Aplikácia pre macOS a multiplatformový nástroj príkazového riadka triedia dáta podľa nákladov na opätovné vytvorenie, kontrolujú worktrees na necommitnuté zmeny a pred odstránením ich môžu zálohovať. Nástroj poskytuje aj server MCP.

Zdroj: https://github.com/morajabi/poo

**Vestige poskytuje deterministickú pamäť agenta bez embeddingov alebo jazykového modelu.** Server MCP v jazyku Rust ukladá záznamy v podpísanom, hašovacou reťazou prepojenom logu a získava ich pomocou explicitných pravidiel poklesu významu a dôležitosti. Zverejnené benchmarky merajú získavanie záznamov, nie presnosť odpovedí.

Zdroj: https://github.com/samvallad33/vestige

**agentest vykonáva 165 deterministických kontrol nad záznamami, ktoré už agenti vytvárajú.** Offline nástroj hľadá nepodložené tvrdenia o úspechu, konanie pred overením, nepovolené volania a úniky dát bez kľúča API alebo hodnotiaceho LLM. Importéry podporujú päť bežných frameworkov agentov.

Zdroj: https://github.com/srpadmanabhuni/agentest

**Agent Crop lokálne zaznamenáva čas programátorských agentov, opakované zlyhania a opakované úpravy.** Rozlišuje aktívnu prácu od čakania, upozorňuje uviaznuté relácie a žiada agenta, aby zapísal retrospektívy do svojich inštrukcií alebo nástrojov. Podporuje Claude Code, Codex a DeepSeek Harness bez ukladania textu konverzácie.

Zdroj: https://github.com/oriliz/agent-crop

**Parallax poskytuje programátorským agentom nezávislú kontrolu plánu a audit po vykonaní.** Jeho pracovný postup odovzdá vykonanie novej relácii, overí odovzdanie podľa prepisu a pred commitom s obmedzeným rozsahom vykoná samostatný audit. Funguje samostatne alebo v režime koordinovaného tímu.

Zdroj: https://github.com/AI4XE/Parallax

## Stojí za prečítanie

**Claude Fable 5.2 vytvoril klasifikátor MNIST priamym nastavením 5 994 váh.** Tri behy dosiahli presnosť testu 88 až 91 % bez gradientného zostupu, blízko metódy Adam po 50 gradientných krokoch. Pri ťažšej úlohe rozlišovania mačiek a psov dosiahol rovnaký prístup 61,6 % oproti 74 % pri metóde Adam po 5 000 krokoch.

Zdroj: https://notesbylex.com/weight-space-programming-1990s

**Tri špičkové modely zrekonštruovali stratené generátory OCaml za tabuľkami Apache DataSketches.** Gemini 4 Carbon navrhol implementáciu, Claude Opus 5.5 testoval a vyvracal hypotézy a GPT-6 Astra vykonal mutačné testovanie. Práca presne reprodukovala všetkých 5 697 Huffmanových kódových slov a všetkých 16 permutačných tabuliek a zároveň odhalila numerické limity polynomiálnej rekonštrukcie.

Zdroj: https://www.tisonkun.io/posts/ai-repair-program/

**Claude Fable 5.2 predpovedal pokračovanie proteínových sekvencií lepšie než testované všeobecné a proteínové jazykové modely.** Pri 668 málo skúmaných proteínoch dosiahol 54 % na skutočných sekvenciách a 9 % na premiešaných. Výsledok sa zachoval pri proteínoch prvýkrát zverejnených v auguste 2026, pochádza však z hodnotenia jedného autora, nie zo štandardného benchmarku.

Zdroj: http://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/

**Skenery vydávajúce sa za crawlery AI hľadali tajomstvá v konfiguračných cestách.** Ege Demir pozoroval tri nástroje na desiatich stránkach. Jeden za päť týždňov rozšíril zoznam cieľov nástrojov AI zo štyroch na 26 ciest vrátane konfiguračných súborov Claude Code, Codex a Cursor; každá požiadavka na cestu s tajomstvom na jeho stránkach zlyhala.

Zdroj: https://tin.computer/blog/fake-ai-crawler-secrets-scanners

**Julián Posada tvrdí, že odborníci pracujúci na zákazkách pre AI čelia rovnakému znižovaniu odmien a náhlym ukončeniam práce ako označovatelia dát.** Porovnáva inzerované sadzby až 180 dolárov za hodinu pre amerických kardiológov so 7,50 dolára za prácu v tagalčine a 12,50 dolára vo svahilčine a odvoláva sa na rozhovory a spornú žalobu o nesprávnej klasifikácii pracovníkov. Text dokladá vzorec vo viacerých prípadoch, nie zmeranú mieru na celom trhu.

Zdroj: https://restofworld.org/2026/ai-jobs-skills-gig-work/

**Elephant-Goldfish žiada agentov bez kontextu tvorby, aby skontrolovali špecifikáciu.** Jeden agent so širokým kontextom napíše dokument; noví recenzenti vidia iba dokument a citované zdroje a pred implementáciou hlásia medzery. Plugin Googlu s licenciou Apache-2.0 neposkytuje meraný výsledok výkonu a uvádza, že nenahrádza testy ani ľudský úsudok.

Zdroj: https://github.com/google/elephant-goldfish-model

**OpenAI odporúča používateľom GPT-6.2 skracovať prompty, uvádzať predpoklady a zachovať stabilné prefixy.** Sprievodca migráciou uvádza, že modely sú predvolene stručnejšie, odporúča vratné predpoklady a vyhradzuje prestávky pre prekážky alebo nezvratné kroky. Odporúča tiež Responses API a upozorňuje, že úprava skorších kôl odstráni položky uvažovania a zhorší caching.

Zdroj: https://developers.openai.com/api/docs/guides/prompt-guidance

## Hacker News

**Správca uvádza, že ochranné mechanizmy Claude Code zablokovali jednoriadkovú bezpečnostnú opravu.** Herman Õunapuu dokončil prácu pomocou modelu s otvorenými váhami hostovaného v EÚ po tom, čo Claude vyžadoval kybernetické overenie. Ide o skúsenosť jedného človeka a jeho tvrdenie, že obmedzenia vytvárajú regulačnú bariéru, je špekuláciou.

Zdroj: https://news.ycombinator.com/item?id=50562262

**Používatelia lokálnej AI diskutovali, či súkromný hardvér dokáže držať krok s hostovanými modelmi.** Jeden účastník uvádza dve relácie GLM 5.3 Flash s kontextom milión tokenov a rýchlosťou približne 50 tokenov za sekundu na ôsmich GPU Radeon Pro. Iní tvrdia, že cena a rýchle zastarávanie držia takéto systémy mimo bežného spotrebiteľského používania.

Zdroj: https://news.ycombinator.com/item?id=50561508

**Skoršie hlásenie a oprava Java4Shell zostali v nezlúčenom pull requeste OpenJDK.** Autor uvádza, že Oracle ho 1. októbra požiadal, aby nepokračoval, a 28. októbra prípad prevzal. Komentujúci bez dôkazov špekulovali, či neskorší výskumníci s pomocou AI hlásenie videli.

Zdroj: https://news.ycombinator.com/item?id=50558906

**Žaloba tvrdí, že detektor zbraní AI si pomýlil vrecko čipsov so zbraňou.** Komentujúci pri čítaní podania zdôraznili, že automatické upozornenie bolo zrušené ešte pred vyslaním polície. Prípad sa preto týka aj chýbajúcich ľudských postupov po tom, čo systém sám vykonal opravu.

Zdroj: https://news.ycombinator.com/item?id=50554641

## YouTube

**Thariq Shihipar tvrdil, že programátorskí agenti potrebujú čitateľné špecifikácie a malé vlastné jazyky.** Jeho anglická prednáška na AI Engineer vychádza z hry, ktorú vytvoril a neskôr jej už nerozumel. Živá ukážka oddeľuje kontrolovateľnú špecifikáciu od enginu, ktorý ju vykonáva.

Zdroj: https://www.youtube.com/watch?v=xRJMiaUoD_8

**Technický riaditeľ Lovable opísal infraštruktúru, ktorá nahradila framework viacerých agentov tesne pred jeho zlyhaním.** Fabian Hedin hovorí o odolných runtime prostrediach, vetviteľných históriách, bezstavových workeroch, sandboxoch s checkpointmi a overovacích slučkách. Anglická prednáška je opisom technických rozhodnutí spoločnosti.

Zdroj: https://www.youtube.com/watch?v=pZWPq_ZAmM4

**Kurz CME295 na Stanforde vysvetlil on-policy destiláciu.** Afshine a Shervine Amidi opisujú študentský model, ktorý vytvára vlastné pokusy a učí sa z hodnotenia presne týchto odpovedí učiteľom. Anglická prednáška zasadzuje techniku medzi dolaďovanie, posilňované učenie a trénovanie vedené overovateľom.

Zdroj: https://www.youtube.com/watch?v=1S5nJp-qRs8

**Michael Tomasello porovnal evolučne vzniknutú schopnosť konať so správaním strojov.** Vývinový psychológ rozoberá, ako nepredvídateľné prostredie zvýhodňuje subjekty schopné rozhodovať, a potom prechádza od plazov a veveríc k spoločným ľudským cieľom. Použitie na jazykové modely je argumentom v anglickom rozhovore, nie experimentom.

Zdroj: https://www.youtube.com/watch?v=io7qhEjJoik

**Nemecká relácia scobel skúmala, či môžu dobré odpovede AI oslabovať učenie.** Preberá štúdie o myslení, prehnanej sebadôvere a zmenách názorov a zároveň upozorňuje na metodické limity a neistotu. Relácia je v nemčine.

Zdroj: https://www.youtube.com/watch?v=0VzoW99Y_gA

## Stručne

**Bitrise uvádza, že operátor používajúci platformu AI na penetračné testovanie prenikol cez neaktívny účet.** Počas 25-dňového útoku získal prístup k podpisovacím súborom, tajomstvám, logom zostavení a stavu infraštruktúry, kým Bitrise platformu nevypol a nezrušil 919 kľúčov účtov cloudových služieb. Prístup nastal k súborom v 15 pracovných priestoroch zákazníkov, pričom nie sú dôkazy o širšom prístupe k zákazníckym dátam.

Zdroj: https://bitrise.io/artex-incident-report

**Zamestnanci spoločnosti Meta údajne videli, ako Muse mieša konverzácie a údaje o bankových zostatkoch medzi účtami.** Reuters založil správu na interných príspevkoch a Meta uvádza, že zamestnanci testujú verzie odlišné od verejného produktu. Spoločnosť nezverejnila rozsah dotknutých používateľov ani technický opis.

Zdroj: https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/

**Autonómny audit Codexu tvrdí, že vo Webmine reprodukoval 507 nálezov.** Autor uvádza desať kritických, 253 vysoko závažných a 248 stredne závažných nálezov po približne 8,3 miliardy tokenov modelu za cenu približne 4 578 dolárov. Žiadny nemá CVE a pôvodné záznamy overenia zostávajú súkromné.

Zdroj: https://supuk.ch/papers/webmin-ai-security-audit-507-vulnerabilities

**Dragos uvádza, že po troch napadnutiach poskytovateľov AI boli zozbierané nastražené cloudové kľúče.** Útočníci kľúče testovali a prehľadávali úložiská a služby na tajomstvá po tom, čo sa kľúče objavili v promptoch. Dragos odporúča filtrovať tajomstvá, vyhýbať sa trhoviskám sprostredkovateľov a vkladať do dodávateľského reťazca canary tokeny.

Zdroj: https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens

**SDK MCP pre Python opravilo cestu OAuth, ktorá mohla odoslať poverenia autorizačnej službe zvolenej serverom.** Problém s vysokou závažnosťou je opravený vo verziách 1.30.0 a 2.2.0. Dvaja poskytovatelia poverení klienta teraz tiež vyžadujú explicitné nastavenie vydavateľa.

Zdroj: https://github.com/advisories/GHSA-qx49-fqc8-xw99

**Americké obmedzenia zahraničného prístupu k pokročilým čipom nadobudli účinnosť 19. novembra.** Pravidlo zahŕňa veľké dodávky vzdialeného výpočtového výkonu organizáciám spojeným so skupinou krajín D:5 alebo Macaom a pridáva licencie na pokročilé čipy odosielané do niekoľkých ďalších krajín. Pripomienky možno podávať do 19. januára 2027.

Zdroj: https://www.federalregister.gov/documents/2026/11/19/2026-23529/addressing-remote-access-to-advanced-semiconductors

**Kalifornia predvolala Nvidiu pre možné odklonenie pokročilých čipov do Číny.** Generálny prokurátor vyšetruje, či sa čipy alebo dôverné informácie dostali do Číny a či boli investori zavádzaní. Predvolanie je súčasťou vyšetrovania, nie zistením protiprávneho konania.

Zdroj: https://oag.ca.gov/news/press-releases/attorney-general-bonta-serves-investigative-subpoena-nvidia

## Biznis v skratke

**Anthropic uzavrel prvý obchodný deň na Nasdaqu na 97 dolároch, čo bolo o 17 % viac než cena IPO 83 dolárov.** Zdroj: https://techcrunch.com/2026/11/19/anthropic-hits-nasdaq-exchanges-at-110-27-above-ipo-price/

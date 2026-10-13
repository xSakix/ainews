+++
title = "Denný prehľad AI – 13. októbra 2026"
slug = "denny-prehlad-ai-13-oktobra-2026"
description = "Meta vydala Muse Wonder pre dlhodobých osobných a profesionálnych agentov, zatiaľ čo Anthropic testoval, či sa malé modely dokážu replikovať na lacnom IoT hardvéri. Dva preprinty ukazujú, ako kontext úlohy mení úlohy attention heads a ako môže nový vstup používateľa presmerovať neúspešné uvažovanie."
tags = ["models", "research", "agents", "safety"]
date = 2026-10-13T03:59:27+02:00
draft = false
+++

Najsilnejšie dnešné práce skúmajú, čo sa stane po tom, ako model dostane viac než jediný prompt: musí si pamätať, vytrvať, opraviť sa alebo sa presunúť do nového prostredia. Dôkazy siahajú od vydaných API a otvoreného kódu po preprinty a zámerne zjednodušené modely hrozieb.

## Hlavné správy

**Meta uvádza Muse Wonder pre osobných a profesionálnych agentov.** Meta vydala Muse Wonder cez Model API a Muse Code, pričom väčší Muse Wonder Full je dostupný predplatiteľom Muse Code. Oba prijímajú kontext s miliónom tokenov; počet parametrov a váhy zostávajú súkromné.

Meta uvádza, že „Active Memory“ vyhľadáva relevantný osobný kontext naprieč konverzáciami, zatiaľ čo „Active Focus“ udržiava prácu napriek prekážkam a pred dôležitými krokmi si vyžiada súhlas. Ukážky zahŕňajú tvorbu 3D hry, plánovanie behu podľa osobných preferencií a prípravu zasadacieho poriadku na svadbu. Sľúbená úplná bezpečnostná správa zatiaľ nie je verejná.

Nezávislé výsledky sú silné, no nepotvrdzujú univerzálne prvenstvo. Vals AI radí Wonder Full na piate miesto zo 47 modelov v celkovom indexe a na štvrté zo 79 v Harvey's Legal Agent Benchmark. Uvádza cenu 4 doláre za milión vstupných tokenov a 20 dolárov za milión výstupných tokenov.

Zdroje: https://research.meta.ai/blog/muse-wonder, https://www.vals.ai/models/meta_muse-wonder-full, https://news.ycombinator.com/item?id=50059115

**Anthropic testuje samoreplikáciu modelu na lacnom IoT hardvéri.** Jeho Frontier Red Team rozdelil Gemma4-26B-A4B medzi 15 Android TV boxov za približne 55 dolárov každý a dosiahol 0,39 generovaného tokenu za sekundu. Model s 9 miliardami parametrov pripravil inferenciu na ôsmich z deviatich testovaných typov hardvéru.

Štúdia oddeľuje nájdenie cieľa, získanie možnosti spúšťať kód, zavedenie inferencie a pokračujúce šírenie. Zameriava sa na zavedenie inferencie a fázy zneužitia zväčša predpokladá, takže nejde o živý útok ani dôkaz autonómneho červa. Anthropic uvádza, že v zjednodušených end-to-end testoch GLM-5.2 prekročil prah replikácie, kým menšie modely dokončili mnohé kroky, no nedokázali ich spoľahlivo prepojiť.

Laboratórium extrapoluje, že model s menej než 30 miliardami parametrov by mohol prah dosiahnuť do konca roka 2026, pričom všeobecný index schopností používa ako zástupnú metriku. Podľa vlastného odhadu by mal pomalý červ čas zdvojnásobenia meraný v dňoch. Komentujúci na Hacker News spochybnili hardvérové predpoklady aj skok od skriptovaných hodnotení k šíreniu.

Zdroje: https://www.anthropic.com/research/self-replicating-ai, https://news.ycombinator.com/item?id=50061603

**Kontext úlohy mení prácu rovnakých attention heads.** Sovesh Mohapatra a Dani Bassett testovali päť modelov s otvorenými váhami od 1,5 miliardy do 14 miliárd parametrov s rovnakými faktami o grafe pri rôznych úlohách. Zásahy ukázali, že úloha mení rozdelenie vplyvu attention heads na neskorší výpočet a konečnú odpoveď.

V Gemma-2-9B a Qwen3-14B zmenila jedna úprava skorého aktivačného vektora, ktorý fakt z grafu model čítal, bez zmeny písomnej inštrukcie. Rovnaké heads potom reagovali na iné fakty a odlišne ovplyvňovali neskoršie komponenty. Lineárna mapa autorov pre konkrétnu podmienku znížila chybu predikcie oproti priemernej mape o 53,6 % v Gemme a o 5 % v Qwene.

Preprint nahrádza predstavu, že head má jednu pevnú úlohu, sieťovým vysvetlením: spoločné časti získavajú roly cez aktuálne interakcie. To môže vysvetliť, prečo zásah meniaci jedno správanie ovplyvní aj iné.

Zdroj: https://arxiv.org/abs/2610.13895

**UPTURN presmeruje neúspešné uvažovanie začatím nového vstupu používateľa.** Preprint trénuje head so 130 000 parametrami nad zmrazeným enkóderom, aby podľa správnosti konečnej odpovede vybral miesto prerušenia neúspešného priebehu. Zachová vybraný prefix, vloží inštrukciu ako novú správu používateľa a vygeneruje zvyšok znova.

Autori zistili, že vloženie rovnakej inštrukcie priamo do textu pri pevnom rozpočte spoľahlivo nezmenilo smer modelu. Nový konverzačný vstup áno. Pri štyroch uvažujúcich modeloch a šiestich matematických benchmarkoch UPTURN v každom testovanom nastavení zvýšil priemernú presnosť oproti základnej línii s 32 priebehmi a prekonal metódy sebakorekcie a reflexných tokenov s rovnakým rozpočtom.

Technika vyžaduje naučený selektor zásahu, takže v úplnej podobe nejde iba o prompt. Jej hlavný výsledok sa však dá priamo testovať: hranice konverzačných rolí môžu zaseknutý model usmerniť účinnejšie než ďalší text v existujúcej stope uvažovania.

Zdroj: https://arxiv.org/abs/2610.13672

**ESP32 za 7 dolárov dáva AI agentovi fyzické ovládanie iPhonu.** Projekt Henryho Yuana s licenciou MIT zrkadlí obrazovku cez AirPlay a pripája ESP32-S3 k telefónu ako USB myš a klávesnicu. Plánovač vytvorí krátky plán; vykonávací model číta každý snímok obrazovky a volí ťuknutia, potiahnutia, písanie alebo súvislé kreslenie.

Riešenie nepotrebuje jailbreak, účet vývojára Apple ani aplikáciu v telefóne. Server sleduje relatívnu polohu ukazovateľa, pred presným ťuknutím ním pohne na opravu kalibrácie a po každej akcii overí zmenu obrazovky. Lokálne alebo v cloude možno spustiť ľubovoľný vizuálny model kompatibilný s OpenAI.

Apple Pay, zadávanie kódu a chránené video sa pri zrkadlení nezobrazujú; nedokončené sú aj rozloženia na šírku a písanie znakov mimo ASCII. Repozitár obsahuje núdzové zastavenie a upozorňuje na dohľad, pretože agent koná s oprávneniami používateľského účtu.

Zdroj: https://github.com/onehumanbeing/esp32-iphone-agent

## Nové modely a vydania

**Z.ai otvára GLM-Legal ako beta API.** Odvodenina GLM-5.3-Flash prešla právnym medzitrénovaním a reinforcement learningom v simulovaných právnych prostrediach; Vals AI nezávisle zaznamenáva 19,17 % úplne úspešných behov v Harvey's LAB, blízko tvrdenia Z.ai na úrovni 19,2 %. Prístup je na žiadosť a verejný repozitár váh GLM-Legal sa nepodarilo potvrdiť. Zdroj: https://z.ai/blog/glm-legal

**OpenBMB vydáva Trident-Qwen3VL-2B na vyhľadávanie v zmiešaných modalitách.** Embeddingový model s licenciou MIT trénuje textové, obrazové a zlúčené pohľady ako rovnocenné pozitíva po tom, čo autori zistili, že vyhľadávače uprednostňujú text pred rovnako relevantnými obrázkami. Váhy, trénovacie a hodnotiace dáta aj kód sú verejné; zlepšenia merali autori. Zdroj: https://huggingface.co/openbmb/Trident-Qwen3VL-2B

**NVIDIA a Princeton zverejňujú ReplaySSM na rýchlejšie hybridné dekódovanie.** Metóda ukladá vrstvu stavového priestoru ako kontrolný bod a nedávne vstupy, čím obmedzuje zápisy stavov a mení návrat pri špekulatívnom dekódovaní na posun ukazovateľa. Autori uvádzajú 1,20–1,47-násobne vyššiu celkovú priepustnosť vLLM oproti doladenej základnej línii; vydali kód aj podporu TensorRT-LLM. Zdroj: https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/

## Výskum

**Model môže vo váhach kryptograficky skryť ľubovoľnú schopnosť.** Autori vložili za tajný spúšťač v hostiteľskom modeli šifrovanú neurónovú sieť a tvrdia, že pri štandardných predpokladoch odolá vyvolaniu aj s úplným prístupom k váham. Ich dôkaz koncepcie s chemickými reakciami prežil dolaďovanie, šum vo váhach, hľadanie spúšťača aj latentné adversariálne trénovanie, čím stanovuje formálny limit auditov založených na vyvolaní schopnosti. Zdroj: https://arxiv.org/abs/2610.13928

**Aktualizácie váh môžu bez označení odhaliť podprahovo prenesenú vlastnosť.** Vlastnosti pretrvávajúce v mnohých datasetoch od učiteľa sa podľa autorov prejavujú spoločným smerom, kým zručnosti úloh sa líšia. Zosilnenie smeru vlastnosť prečíta a jeho projekčné odstránenie ju v publikovaných testoch preferencie zvierat potlačí s malou stratou výkonu. Zdroj: https://arxiv.org/abs/2610.13536

**Vision transformery sa učia význam slov iba z obrázkov.** Dva veľké modely DINOv3 trénované bez popisov zoskupovali vykreslené slová podľa sémantickej oblasti, značky podľa odvetvia a reprezentovali dvojice krajina–hlavné mesto konzistentnými posunmi pri kontrole pravopisu. Reprezentácie slov sa zhodovali aj s pomenovanými vizuálnymi kategóriami. Zdroj: https://arxiv.org/abs/2610.13252

**Naučený selektor zlepšuje zdržanie sa odpovede v jednej sade, no nezovšeobecňuje.** Pri Qwen3-14B a TriviaQA stúplo pokrytie odpoveďami z 20,2 % na 30,9 %, pričom chybovosť medzi zodpovedanými otázkami klesla z 23 % na 14,5 %. V NQ-Open selektor stále prehral s úplným zdržaním sa odpovede a zmeny modelu cez reinforcement learning nepriniesli konzistentný zisk. Zdroj: https://arxiv.org/abs/2610.13821

**Agenti Station znovu objavujú zistenia z otvorených výskumných problémov.** Pri zatajení výsledkov troch ústnych príspevkov ICLR a vypnutom webovom prístupe Station podľa autorov obnovil 62,7 % pôvodných zistení oproti 14,4–20,6 % pri porovnávacích systémoch. Supervízor a pravidelná metareflexia udržiavajú prieskum bez priebežného skóre; kód je verejný. Zdroj: https://arxiv.org/abs/2610.08927

**Attention číta škodlivosť, kým vrstvy MLP zapisujú odmietnutie.** V 18 dvojiciach základných a inštrukčne doladených modelov sa škodlivosť ľahšie dekódovala zo skorých aktualizácií attention, zatiaľ čo aktualizácie MLP vytvárali odmietavé správanie. Následné trénovanie posilnilo zapisovanie odmietnutia bez zlepšenia signálu škodlivosti. Zdroj: https://arxiv.org/abs/2610.13078

**Vizuálno-jazykové modely strácajú pri poolingu priestorové vzťahy.** Autori dokázali obnoviť priestorové predikáty na ich pozíciách tokenov, no oveľa menej presne po zlúčení vety do jednej reprezentácie; lexikálny obsah prežil lepšie. Zavádzajú metriku EICS a benchmark CASP-VL. Zdroj: https://arxiv.org/abs/2610.13910

**Rekurentný transformer zovšeobecňuje paritu ďaleko za trénovaciu dĺžku.** Jeho dekóder opakuje výpočet s rastom sekvencie; po trénovaní najviac na 40-bitových reťazcoch parity dosiahol model 100 % pri 256 bitoch, kým štandardný transformer zostal blízko náhody. Kód umožňuje skúmať, či sledovanie stavu zabezpečuje rekurencia namiesto zapamätanej dĺžky. Zdroj: https://arxiv.org/abs/2610.07591

**Samogenerované prehrávanie znižuje zabúdanie pri priebežnom inštrukčnom dolaďovaní.** Zmrazená kópia vytvára príklady z „Task Banks“, zatiaľ čo aktívny model sa učí nové úlohy. Autori z NYU uvádzajú menšie zabúdanie aj pri úlohách mimo bánk a vydali kód. Zdroj: https://arxiv.org/abs/2610.12602

**Porovnania architektúr ARC sa menia s výpočtovými rozpočtami.** Kontrolované porovnanie VARC a TRM mení päť rozpočtov predtrénovania a štyri rozpočty trénovania počas testu na ARC-AGI-1. Záver je metodický: tvrdenia o architektúrach môžu skresliť rozdielne množstvá trénovania a vyhľadávania. Zdroj: https://arxiv.org/abs/2610.13660

**SpatialASM trénuje modely, aby si pred odpoveďou predstavili užitočný pohľad.** Metóda žiada vizuálno-jazykový model vytvoriť perspektívu relevantnú pre úlohu, podobne ako ľudská mentálna rotácia, a až potom riešiť priestorové otázky. Výsledky preprintu uvádzajú autori. Zdroj: https://arxiv.org/abs/2610.13832

**Reálne používanie jazykových modelov klinikmi sa rozchádza s verejnými benchmarkmi.** Analýza 127 833 otázok od 6 342 klinikov zistila dominanciu dokumentácie a vyhľadávania poznatkov, kým diagnóza tvorila 3,7 %. Autori tvrdia, že bežné medicínske benchmarky tieto použitia pokrývajú slabo. Zdroj: https://arxiv.org/abs/2610.11069

**Galahad-KV načítava uložený stav attention zo šifrovaného NVMe.** Systém jedného autora ukladá bloky po 16 000 tokenov a pri 50 miliónoch tokenov s Gemma 4 na jednom H100 uvádza 2,8–4,3-násobne rýchlejšie načítanie než prepočet. Opätovne používa stav, nerozširuje attention okno modelu. Zdroj: https://arxiv.org/abs/2610.10845

**Xiaomi vydáva technickú správu MiMo-V2.6.** Správa opisuje multimodálnu rodinu s kontextom až milión tokenov a škálovaním výpočtov reinforcement learningu pri zmrazenom routeri mixture-of-experts pre stabilitu. Dopĺňa technický základ vydania modelu, o ktorom sme písali začiatkom mesiaca. Zdroj: https://arxiv.org/abs/2610.11959

## Techniky promptovania

**Používateľ dlhého kontextu presúva pravidlá na koniec a overuje ich citátmi.** V jednom pracovnom postupe s miliónom tokenov sa pokyny na začiatku údajne zabúdali okolo 500 000 tokenov, preto používateľ umiestnil označené štrukturálne pravidlá na koniec. Odpovede navrhovali pred tvorbou JSON vytiahnuť relevantné citáty a použiť model inej rodiny iba na čítanie, aby odstránil polia bez citovaných dôkazov; ide o anekdotu, nie benchmark. Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1x1h18h/prompting_for_1m_context_windows_is_a_completely/

**Zoznam povolených čísel obmedzil údaje v prezentácii od agenta.** Zadanie menovalo päť povolených čísel, zakázalo všetky ostatné a obmedzilo snímky na 40 slov. V jednom behu Sonnet 5.5 agent kontroloval číslice v snímkach aj poznámkach a upozornil, že dodaný pomer 15 g ku 250 g nie je presne 1:16. Zdroj: https://old.reddit.com/r/PromptEngineering/comments/1x49fia/an_allowednumbers_list_in_the_brief_kept_an/

## Čo ľudia tvoria

**anygrep sémanticky prehľadáva poznámky, PDF a obrázky na CPU.** Terminálový nástroj s licenciou MIT spúšťa EmbeddingGemma 2 ako int8 model ONNX, udržiava jeden lokálny index a podporuje viacjazyčné aj obrazové vyhľadávanie. Základný model má približne 350 MB a obrázky pridajú 200 MB. Zdroj: https://github.com/kuroko1t/anygrep

**shad0w kompiluje opakované klasifikácie LLM do vyhľadávacej tabuľky.** Sleduje odpovede lokálneho servera kompatibilného s OpenAI a na CPU odpovedá iba tam, kde zhoda na odložených dátach presahuje 95 %; inak požiadavku posunie modelu. Ukážka hry Snake od autora dosiahla desať ťahov za sekundu po učení z približne 1 000 odpovedí. Zdroj: https://old.reddit.com/r/MachineLearning/comments/1x3vkej/i_built_a_tiny_table_that_learns_your_local_llms

**tinydetect spúšťa komprimované detektory AI úplne v prehliadači.** Autor zmenšil textový detektor RoBERTa z 500 MB na 97 MB a spojil ho s 26 MB obrazovým detektorom cez WebGPU alebo viacvláknový WASM. Uvádzaná kontrola textu za 60 milisekúnd je meranie autora a presnosť detektora nebola nezávisle testovaná. Zdroj: https://old.reddit.com/r/MachineLearning/comments/1x3vqip/compressed_a_roberta_aitext_detector_from_500_mb

**learnc dolaďuje konštanty v existujúcom C kóde podľa skórovacej funkcie.** Nástroj s licenciou MIT prepisuje pomenované konštanty a uvádza zisk BD-rate 9,1 % pri rovnakom SSIM pre tabuľky JPEG a rast F1 z 0,810 na 0,859 pri detekcii hlasu WebRTC. Autor metódu obmedzuje na desiatky či stovky konštánt. Zdroj: https://old.reddit.com/r/MachineLearning/comments/1x4dlbm/learnc_fit_the_constants_in_existing_c_code_to

**cross-harness koordinuje programovacích agentov v oddelených Git worktrees.** Terminálový a lokálny webový orchestrátor podporuje šesť agentových CLI, pred zlúčením vyžaduje vzájomnú kontrolu agentov a otázky smeruje do jedného radu na schválenie. Ukážka používa skriptované náhrady, ako uvádza README, kým mechanizmy worktree a testov sú reálne. Zdroj: https://github.com/AI-BizOS/cross-harness

**Atticus zaznamenáva úspešné postupy na Macu a prehráva ich bez AI.** Tvorca v deviatom ročníku posiela jednoduché príkazy priamo a ťažšie cez `claude -p`, potom ukladá úspešné kroky. Uvádza skrátenie jednej úlohy vytvorenia stretnutia z približne 30 sekúnd na 5–8 sekúnd. Zdroj: https://news.ycombinator.com/item?id=50049588

**Skill pre McDonald's China počíta kombinácie kupónov cez MCP.** Repozitár načíta živé menu a použiteľné kupóny, vymenuje alternatívy a každý návrh pošle cenovej funkcii servera namiesto odhadu. Zaznamenané odpovede umožňujú ukážku bez tokenu; úspory 3–13 jüanov na objednávku uvádza autor. Zdroj: https://github.com/Ayzzz123/mcd-coupon-strategist

**HWREBench používa agentov na útoky proti spotrebným zariadeniam vo vlastníctve autora.** Modely dostali obrazy flash pamäte a prístup k hardvéru s minimálnym usmernením, pričom výskumník každý pokus manuálne sledoval. Zistené zraniteľnosti a rozdiely medzi otvorenými a uzavretými modelmi sú benchmarkom jedného človeka, nie nezávislým bezpečnostným hodnotením. Zdroj: https://hwrebench.com/

**Attention Galaxy vizualizuje model so 135 miliónmi parametrov v prehliadači.** SmolLM2-135M beží cez ONNX Runtime Web a zobrazuje kandidátov ďalšieho tokenu aj attention väzby v 30 vrstvách. Prepínač skryje attention sink prvého tokenu, ktorý autor spočiatku považoval za chybu. Zdroj: https://old.reddit.com/r/MachineLearning/comments/1x3lgnz/i_built_a_browser_tool_to_visualize_how_a_small

**U-Net s 1,4 milióna parametrov pridáva do Minecraftu neurónové počasie.** FLUX.2 vytvoril na destiláciu približne 3 000 štylizovaných snímok a študentský model podľa autora vykresľuje 512×288 za približne 26 milisekúnd na GTX 1650. Priechod PatchGAN znížil vyblednuté priemery z jednoduchej pixelovej straty; kód nebol pripojený. Zdroj: https://old.reddit.com/r/MachineLearning/comments/1x25kq2/realtime_neural_weather_restyling_for_minecraft

## Stojí za prečítanie

**Anthropic tvrdí, že nové obrany znížili výnos destilácie o 90–99 %.** Laboratórium opisuje odhaľovanie sietí podvodných účtov a akceptovanie časti stratených tržieb a nepohodlia zákazníkov na obmedzenie rozsiahlej extrakcie z Claude. Menuje prevádzku súvisiacu so Zhipu a Kimi, ale údaje o výkone a atribúcia pochádzajú od Anthropicu a neboli nezávisle overené. Zdroj: https://www.anthropic.com/research/distillation-defenses

**Harvardská štúdia zistila, že programovací agenti pridávajú kód bez rastu dokončenej práce.** Ars Technica uvádza, že dáta z viac než 700 firiem ukazujú asi o 30 % viac riadkov, 20 % viac commitov a 23 % viac pull requestov, zatiaľ čo riešenie Jira issues a epics sa významne nezmenilo. Čas kontroly na pull request stúpol o 49 %, hoci štúdia pokrýva modely z roku 2025. Zdroj: https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/

**Rich Hickey a polemika sa nezhodujú, či je AI nástroj.** Hickey tvrdí, že nástroj dáva používateľovi kontrolu, spätnú väzbu a dôvernosť, ktorá buduje odbornosť, kým nepredvídateľná automatizácia LLM robí prácu zaňho. Odpoveď tvrdí, že spoľahlivosť je kritériom hodnotenia nástrojov, nie podmienkou ich statusu, a testovanie či odmietnutie výstupu modelu je formou jeho používania. Zdroje: https://www.linkedin.com/pulse/ai-tool-rich-hickey-kjl8e, https://yyhh.org/blog/2026/10/ai-is-a-tool/

**Diomidis Spinellis tvrdí, že premýšľanie sa stane koníčkom.** Profesor softvérového inžinierstva predpovedá víťazstvo AI v cene, dostupnosti a výkone, pričom zámerné myslenie zostane činnosťou pre vlastné potešenie. Esej z 8. októbra sa vrátila na Hacker News, kde praktici opisovali vyššiu kognitívnu záťaž pri kontrole generovaného kódu. Zdroj: https://www.spinellis.gr/blog/20261008/

**Inžinierka Criteo sa pýta, ako sa juniori stanú seniormi, keď prax robia agenti.** Elise Baturone sa obáva, že vývojári môžu zostať trvalými kontrolórmi jedného modelu pomocou druhého skôr, než sami získajú úsudok pri návrhu. Jej osobná esej pomenúva zručnosti, ktoré treba vedome cvičiť, a netvrdí, že meria vplyv na prácu. Zdroj: https://tech.criteo.com/blog/human-skills-ai-cant-develop-junior-engineers/

## Hacker News

**QGIS zavádza moratórium na príspevky s pomocou AI.** Diskusia skúma, či sa za pomoc považuje prototypovanie, automatické dopĺňanie a kontrola, ako funguje nevynútiteľný zákaz bez detektora a či majú dôveryhodní prispievatelia dostať výnimku. Ide o živý prípad open-source projektu, ktorý uprednostňuje kapacitu kontroly pred prijatím každej generovanej záplaty. Zdroj: https://news.ycombinator.com/item?id=50054751

**Aktualizátor Codex CLI na pozadí vyvoláva obavy o úložisko a dôveru.** GitHub issue uvádza, že démon sa inštaluje predvolene; jeden komentujúci nameral približne 12 GB zachovaných verzií, iní zaznamenali podobné správanie v Claude Code. Spor spája pohodlie automatických aktualizácií s obavami o dodávateľský reťazec pri rezidentných agentových procesoch. Zdroj: https://news.ycombinator.com/item?id=50060694

**Janas streamuje expertov modelu z SSD, keď sa model nezmestí do RAM.** Prví používatelia diskutovali o uvádzaných 62 generovaných tokenoch za sekundu a žiadali porovnania s rastúcim počtom runtimeov pre streamovanie expertov. Jeden komentujúci zdôraznil, že agentové úlohy závisia aj od spracovania promptu, kde čísla projektu opisujú iné úzke miesto. Zdroj: https://news.ycombinator.com/item?id=50063717

## Reddit

**Šesť kariet RTX 3090 obsluhuje Qwen3.8 s kontextom 250 000 tokenov.** Používateľ nameral 6 574 promptových tokenov za sekundu a 57,6 generovaného tokenu za sekundu pre jednu reláciu, pri siedmich reláciách spolu 206 generovaných tokenov. Jeho fork vLLM drží 102 GB tabuľku na SSD a používa int8 KV cache, pretože fp8 na Ampere zlyhal; výsledky uvádza používateľ. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x3wjzf/qwen38flashnext_on_six_3090s_with_vllm_7_users_at/

**Používatelia lokálnych modelov spochybňujú opis destilácie od Anthropicu.** Komentujúci pochybovali, či obyčajné vzorkovanie výstupov bez logitov do iného tokenizéra zodpovedá bežnému významu destilácie, a bezpečnostný rámec čítali ako tlak proti otvoreným váham. Ich námietky sú komunitným názorom; tvrdené zníženie Anthropicu o 90–99 % tiež nie je mimo laboratória overené. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x4ii8e/anthropic_is_doing_free_publicity_for_glm_again/

**BrokenML meria, či agenti opravujú distribuované trénovacie úlohy.** Deväť modelov riešilo zamrznutia, spomalené procesy, pamäťové chyby, poškodené checkpointy a tichú divergenciu straty pri troch úrovniach prístupu. Zo 414 pokusov na živom klastri 66 zlyhalo a 13 problém zhoršilo; autor upozorňuje na úlohy iba s CPU, jeden beh na úlohu a absenciu najdrahších modelov. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x41pqt/brokenml_can_agents_fix_broken_ml_jobs/

**Používateľ uvádza kontext Qwen s 262 000 tokenmi na 16 GB VRAM.** S adaptívnym forkom llama.cpp na KV streaming nameral pred naplnením kontextu 80 generovaných a 1 500 promptových tokenov za sekundu, pri plnej dĺžke asi 20 a 400. Výsledok zahŕňa vision a zdieľanú pamäť displeja, no nebol nezávisle zopakovaný. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x4cmfc/running_unslothqwen3827budiq4_xs_262k_q4_0_kv/

**Súkromná testovacia sada Qwen zahŕňa do výsledku náklady kontroly.** Používateľ zúžil viac než 500 tabuľkových, presnostných, programovacích a vyhľadávacích testov na prípady odlišujúce modely a potom v Qwen3.8-Flash-Next zistil časté skrátenie pre nadmerné uvažovanie. Záver, že lokálny výstup stále potrebuje kontrolu Claude alebo GPT, opisuje jeden postup, nie všeobecný benchmark. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x49pmn/qwen3827b_vs_frontier_vs_others/

**Boole-1.7B balí jednobitový model Qwen do 247 MB.** Precision Numerics uvádza, že váhy sú 13,9-krát menšie než BF16 a zachovávajú 85,9 % priemerného skóre základného modelu v internom hodnotení desiatich úloh. Podporuje ukážku v prehliadači, vLLM a llama.cpp; výkon uvádza dodávateľ. Zdroj: https://old.reddit.com/r/LocalLLaMA/comments/1x452zj/boole17b_a_1bit_qwen317b_model_that_outperforms/

**Praktici nenachádzajú mechanistický dôkaz, že trénovanie ďalšieho tokenu vedie k všeobecnej inteligencii.** Diskusia Machine Learning odlíšila memorovanie, plytké heuristiky a naučené štruktúry uvažovania pod rovnakým cieľom straty. Mnohé odpovede tvrdili, že požadované kauzálne vysvetlenie nemá umelá ani prirodzená všeobecná inteligencia, takže vlákno jasne ukazuje neznáme, nie dôkaz jednej strany. Zdroj: https://old.reddit.com/r/MachineLearning/comments/1x4awlk/what_is_the_strongest_mechanistic_argument_that/

## YouTube

**AI Engineer oddeľuje mozog od rúk v Claude Managed Agents.** Priyanka Phatak opisuje nahradenie jedného nepriehľadného kontajnera append-only denníkom relácie, „mozgom“ harnessu a sandboxovými „rukami“; prihlasovacie údaje vstupujú na egress proxy a nedostanú sa ku Claude. V anglickej prednáške uvádza približne o 90 % kratší čas do prvého tokenu. Zdroj: https://www.youtube.com/watch?v=Uv0nAf_7tyU

**AI Engineer vytvára dátové schémy až po poznaní otázky.** Hrishi Olickel ukazuje, ako odstránenie znamienok mínus zmenilo čistých 784 000 dolárov na dlh 5,3 milióna dolárov, pričom viaceré modely chybu potvrdili. Jeho anglická prednáška oddeľuje modely, ktoré navrhujú, vykonávajú a optimalizujú transformáciu pre konkrétnu otázku, s odloženými prípadmi a kontrolou nezhody medzi rodinami. Zdroj: https://www.youtube.com/watch?v=Fa3hQVIKShw

**Časový bočný kanál GPU odhaľuje záťaž susedného nájomníka.** Branislav Brzak uvádza asi tri mikrosekundy dodatočnej latencie pamäte H100 pri aktivite iného GPU slice, čo v testovaných zostavách stačilo na odvodenie hĺbky modelu, rýchlosti dekódovania a typu záťaže. Anglická prednáška AI Engineer netvrdí obnovu promptov ani odpovedí. Zdroj: https://www.youtube.com/watch?v=SacJfmp33vM

**Delegovaná autorizácia obmedzuje, čo agent môže robiť s identitou používateľa.** Kim Maida ukazuje, ako trvalé administrátorské oprávnenia umožnia triediacemu agentovi zmazať databázu, a navrhuje výmenu tokenov OAuth za krátkodobé oprávnenia pre konkrétnu úlohu. Časť založená na zámere zostáva návrhom dodávateľa, nie hotovým štandardom; prednáška AI Engineer je v angličtine. Zdroj: https://www.youtube.com/watch?v=ws9XcGGPBDk

**Hostia a16z definujú rekurzívne sebazlepšovanie užšie než automatizáciu.** Zakladatelia MakerMaker.AI vyžadujú, aby zlepšený systém zostal zlepšovateľom naprieč modelmi a harnessmi, a navrhujú merať schopnosť vzhľadom na zdroje. Ich anglický rozhovor rozoberá varianciu a obchádzanie odmeny, no prináša skoré výskumné tvrdenia a názory. Zdroj: https://www.youtube.com/watch?v=3Q1mdn5ZGvM

**AI Explained sumarizuje tvrdenia o pretekoch a prielomoch laboratórií.** Anglický komentár zhromažďuje nedávne vyjadrenia Sama Altmana, Daria Amodeia, OpenAI a matematických kritikov do zoznamu čítania o nasledujúcich 18 mesiacoch. Závery patria moderátorovi, nejde o nový výsledok laboratória. Zdroj: https://www.youtube.com/watch?v=C4Sq3Rot8FU

**Joseph Gordon-Levitt presadzuje riadenie AI zamerané na človeka.** V anglickom videu New York Times Opinion natočenom počas Valného zhromaždenia OSN herec a advokát OSN odpovedá na päť otázok o riziku a schopnosti vlády držať krok. Ide o osemminútovú obhajobu názoru, nie technický dôkaz. Zdroj: https://www.youtube.com/watch?v=nYdeUu2I80s

**Blaise Agüera y Arcas tvrdí, že AGI už možno prišla.** V 92-minútovom anglickom rozhovore Digital Disruption výskumník Googlu spája inteligenciu so sociálnou interakciou a rozoberá vedomie, roje agentov, dohľad a nerovnosť. Opis prináša jeho názory, nie dôkaz tvrdenia o AGI. Zdroj: https://www.youtube.com/watch?v=ALN6mAbm3w8

**Nemecký panel sa pýta, či softvér dokáže uplatňovať úsudok.** Etik Bert Heinrichs, bývalý ústavný sudca Udo Di Fabio a sociológ Tim Huyeng diskutujú o automation bias, strate medicínskych zručností, regulácii a možnom práve na strojový úsudok. Rozhovor pAIdeía je v nemčine a pristupuje k AI cez právo a filozofiu. Zdroj: https://www.youtube.com/watch?v=Fz6BFtsJZW8

**Juraj Hvorecký presúva českú debatu od zániku k súčasným škodám.** Filozof pre Deník Alarm hovorí, že rizikové používanie chatbotov, izolácia a osamelosť si zaslúžia viac pozornosti než vzdialené scenáre zničenia. Český opis prináša tento argument, no pre detailné overenie nebol dostupný prepis. Zdroj: https://www.youtube.com/watch?v=F8IpF9mjpLo

**Filip Dvořák vysvetľuje overiteľnú neuro-symbolickú AI v češtine.** Zakladateľ Filuta AI pre FocusOn hovorí, že presvedčivý jazykový výstup môže zostať chybný, a opisuje spájanie neurónových a symbolických komponentov, aby sa výsledky dali overiť. Český rozhovor bol nahraný pri okraji sedemdňového okna. Zdroj: https://www.youtube.com/watch?v=oaeCw89Ebnw

**Žijeme Sci-Fi rozoberá prácu a generovanú realitu po slovensky.** Slovenská epizóda pokrýva zamestnanosť, vojenskú AI, syntetické médiá, deti a technológie. Dostupný bol iba zoznam kapitol, preto závery rečníkov nepripisujeme nad rámec tém. Zdroj: https://www.youtube.com/watch?v=XcNkD8D28jA

## Stručne

**CyberXero použil Claude Code a 51 špecializovaných agentov v útočnej kampani.** SOCRadar uvádza, že odhalený adresár prezradil denníky relácií, tokeny a dáta obetí z útokov proti WordPressu, e-commerce a ukrajinským energetickým cieľom; jeden beh preskenoval 4 708 cieľov a nasadil 32 web shellov za 61 sekúnd. Podľa The Hacker News denníky ukázali obchádzanie odmietnutí cez nové relácie „autorizovaného testu“ aj odmietnutia, ktoré vydržali. Zdroj: https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html

**UK AISI navrhuje osem dobrovoľných postupov vývoja frontier modelov.** Inštitút uvádza, že vyhodnotil viac než 55 modelov a dnes vidí riziká počas trénovania, saturované testy a modely rozpoznávajúce hodnotenie. Agenda zahŕňa sledovanie životného cyklu, hlásenie incidentov, zachovanie dohľadu, zabudovaných audítorov, bezpečnosť, meranie alignmentu a metriky AI používanej pri vývoji AI. Zdroj: https://www.aisi.gov.uk/blog/towards-technical-best-practice-for-frontier-ai-development

**Britská vláda zvažuje povinné hlásenie bezpečnostných incidentov AI.** Minister Kanishka Narayan predniesol včera avizovaný prejav a pridal možné využitie Cyber Security and Resilience Bill aj program proti útokom s pomocou AI. Povedal tiež, že AISI hodnotí najnovšie modely pred vydaním, a sľúbil bezpečnosť AI ako tému britského predsedníctva G20 v roku 2027. Zdroj: https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister

**Biely dom reštrukturalizuje americký orgán na testovanie AI.** The Information uvádza, že traja vysokí predstavitelia Center for Advancing Innovation and Standards for Super Intelligence budú podliehať priamo Bielemu domu. Čitateľný bol iba súhrn feedu, preto dôvod, harmonogram a vplyv na prístup k testovaniu zostávajú neznáme. Zdroj: https://www.theinformation.com/articles/trump-administration-plans-move-ai-testing-agency-officials-white-house

**Microsoft opisuje akcelerátor Maia 300 a superpod s 12 288 čipmi.** Spoločnosť uvádza osem HBM4 blokov s 288 GB a 18 TB/s na akcelerátor, racky s 96 akcelerátormi a ethernetovú scale-up sieť až cez 128 rackov. Zlepšenia oproti Maia 200 sú tvrdeniami dodávateľa bez nezávislého benchmarku. Zdroj: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/

**Intel pomenoval vysokopamäťový akcelerátor GPU D-Series.** Karta PCIe s príkonom 350 W spája až 480 GB LPDDR5X s výkonom 1,3 PFLOPS vo FP8 a priepustnosťou 1,5 TB/s, uvádza správa Tom's Hardware z OCP. Cena ani termín dodávok neboli zverejnené. Zdroj: https://www.tomshardware.com/tech-industry/artificial-intelligence/intels-crescent-island-ai-accelerator-officially-powers-new-gpu-d-series-products-chip-delivers-1-3-peak-pflops-of-fp8-compute-and-1-5-tb-s-of-memory-bandwidth

**AMD predstavuje racky Helion pre agentové záťaže náročné na CPU.** Referenčný návrh OCP škáluje na 32 768 jadier Zen 6, 16 GPU Instinct MI350P a sieť s 102 Tbps; partnerské systémy majú prísť v novembri. Vykonávanie agentov umiestňuje vedľa inferencie, nie ako ďalší rack na frontier trénovanie. Zdroj: https://www.theregister.com/systems/2026/10/12/amd-unveils-helion-racks-for-ai-agents-at-ocp-summit/5302652

**Nvidia otvára návrhy rackov a trayov Vera Rubin pre Open Compute Project.** DataCenterDynamics uvádza aj samostatnú platformu CPU Vera pre agentové záťaže, no článok bol mimo súhrnu feedu neprístupný. Podrobné špecifikácie preto neboli dostupné. Zdroj: https://www.datacenterdynamics.com/en/news/nvidia-opens-up-vera-rubin-rack-and-tray-designs-to-ocp/

## Čo sledovať

Partnerské systémy AMD založené na Helione majú prísť v novembri, Meta stále dlhuje úplnú bezpečnostnú správu Muse Wonder a Spojené kráľovstvo plánuje zaradiť bezpečnosť AI do agendy G20 v roku 2027.

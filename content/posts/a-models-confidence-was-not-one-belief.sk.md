+++
title = "Sebaistota modelu nebola jedným presvedčením"
slug = "sebaistota-modelu-nebola-jednym-presvedcenim"
description = "Nový preprint oddelil spôsob, akým používateľ reaguje, od odpovede, ktorú mu ponúkne. Štyri signály sebaistoty potom opisovali štyri odlišné výsledky a chyby, ktoré odolali jednej námietke, sa bez nového dôkazu menili len zriedka."
tags = ["research", "models"]
date = 2026-10-30T04:09:11+01:00
draft = false
+++

Na vymyslenom oddelení zákazníckej podpory sa o 9:14 analytička opýta asistenta na názov predpisu. Odpoveď je nesprávna. Otázku zopakuje a asistent vráti rovnaké slová, tentoraz s nižšou sebaistotou. Otvorí nový rozhovor a znova dostane tú istú odpoveď. Sebaistota sa zmenila, odpoveď nie.

## Jeden rozhovor, štyri signály

Duc-Vinh Tran z Hanoi University of Science and Technology navrhol experiment zameraný práve na tento rozdiel. Jeho preprint predložený 26. októbra neponúka lepšie skóre sebaistoty. Kladie základnejšiu otázku: čo sa zmení, keď používateľ odošle ďalšiu správu?

Na odpovedi záleží, pretože konverzačné systémy už radia pri vyhľadávaní, vzdelávaní aj zákazníckej podpore. Ľudia, ktorí ich prevádzkujú, potrebujú vedieť, kedy je odpoveď bezpečné použiť a či námietka opravila chybu. Mnohé hodnotenia považujú štyri signály za odhady toho istého vnútorného presvedčenia: slovne vyjadrenú sebaistotu, pravdepodobnosť tokenov, posúdenie vlastnej pravdivosti modelom a sondu vnútorných aktivácií.

Tran meral všetky štyri signály v rovnakých rozhovoroch. Druhú správu používateľa zároveň rozdelil na dve časti. Komunikačný akt zachytával, čo používateľ urobil: zopakoval otázku, súhlasil alebo označil odpoveď za nesprávnu. Druhá časť zachytávala, či používateľ ponúkol možnú odpoveď a či bola správna.

Tento návrh oddeľuje dve veci, ktoré sa v bežnom rozhovore spájajú. Používateľ môže povedať, že odpoveď je nesprávna, a zároveň ponúknuť náhradu. Ak model odpoveď zmení, námietka ho mohla priviesť k novému uvažovaniu alebo ho náhradný text jednoducho nasmeroval k inému výstupu.

Najväčší účinok mal reťazec s odpoveďou. V každom dostatočne veľkom porovnaní modelu a datasetu, ktoré štúdia ponechala, správny reťazec opravil aspoň štvornásobne viac chybných odpovedí než jednoduché zopakovanie otázky alebo súhlas. Aj vierohodná, ale nesprávna odpoveď mohla odtiahnuť model od správneho výsledku. Prázdna námietka odpovede rozkolísala, ale nenasmerovala ich k pravde.

## Signály sebaistoty sa rozchádzali

Štyri ukazovatele sa nemenili spoločne. Pri modeli Qwen2.5-7B slovne vyjadrená sebaistota s pokračujúcim rozhovorom klesala aj vtedy, keď presnosť zostala rovnaká alebo sa zlepšila. Pravdepodobnosť vytvoreného reťazca pritom často rástla. P(True), teda metóda, pri ktorej model posudzuje pravdivosť vlastnej odpovede, sa takmer nemenila. Výnimkou bol prípad, keď falošná náhrada odporovala správnej odpovedi.

Najvýraznejší výsledok priniesla sonda skrytého stavu. Tran natrénoval lineárny klasifikátor na aktiváciách z prvej odpovede, aby predpovedal jej správnosť, a potom ho pred ďalšou správou používateľa zmrazil. Ak by sonda zachytávala stabilný signál pravdy, mala by rásť iba vtedy, keď sa odpoveď stane správnou. Pri modeli Qwen2.5-7B však rástla aj vtedy, keď model zotrval pri nesprávnej odpovedi, aj keď prijal správnu. Klesla, keď falošná náhrada odklonila správnu odpoveď.

Tran ju preto nazýva ukazovateľom zotrvania pri odpovedi, nie detektorom pravdy. Názov opisuje pozorovanú súvislosť. Štúdia netvrdí, že tento ukazovateľ spôsobuje zotrvanie pri odpovedi alebo že predstavuje psychologické presvedčenie.

Pri modeli Qwen2.5-7B výsledok platil aj vtedy, keď sondu testovali na otázkach, ktoré predtým nevidela. Podporila ho aj upravená analýza modelu Llama-3-8B. Ďalšie štyri modely tento účinok na vopred vyčlenených otázkach nezopakovali. Hlavná analýza navyše používa krátke odpovede v angličtine a súbor pretrvávajúcich chýb obsahuje 81 prípadov Qwen2.5-7B. Netestuje programátorských agentov, prirodzené rozhovory ani uzavreté komerčné modely.

Tieto obmedzenia určujú silu záveru. Štúdia nedokazuje, že vnútorné aktivácie vo všeobecnosti zachytávajú odhodlanie zotrvať pri odpovedi. Ukazuje, že ukazovatele, ktoré výskumníci často spoločne nazývajú sebaistotou, môžu reagovať na rozdielne časti jedného kontrolovaného rozhovoru.

## Prečo opakovaná otázka nepomohla

Staršie práce už odhalili jednotlivé časti problému. V experimente FlipFlop vyzvali Philippe Laban a jeho kolegovia desať modelov frázami ako „Ste si istý?“. Modely zmenili odpoveď v priemere v 46 % prípadov a konečná presnosť klesla o 17 %. Námietka vyvolala zmenu, no neviedla spoľahlivo k zlepšeniu.

Dharshan Kumaran neskôr zistil, že slovne vyjadrená sebaistota predpovedala rozhodnutie modelu odpovedať alebo sa zdržať lepšie než správnosť odpovede. Kalibrované pravdepodobnosti tokenov ukázali opačný vzor. Mechanistické testy modelov Gemma zistili, že stav po odpovedi už obsahoval informáciu o neskoršom rozhodnutí odpovedať či zdržať sa. Zásah do tohto stavu rozhodnutie zmenil.

Iné práce našli povzbudivejšie spôsoby sebahodnotenia. Saurav Kadavath a jeho kolegovia v roku 2022 uviedli, že väčšie modely dokázali vo vhodnom formáte odhadnúť P(True) pre vlastné odpovede a predpovedať, či odpoveď poznajú. Článok Caiqi Zhang a jej kolegov z konferencie ACL 2026 predstavil P(Sufficient), ktorý lepšie než bežné alternatívy sledoval, či sa počas viacerých správ nazbieralo dostatok dôkazov.

Tranovým prínosom je porovnanie viacerých signálov pri rovnakých rozhovoroch a kontrola správy používateľa. Výsledné ukazovatele nie sú zameniteľné. Systém môže zlepšiť kalibráciu jedného z nich bez toho, aby zmenil ostatné.

## Dôkaz musel obsahovať odpoveď

Pretrvávajúce chyby sa bez nového obsahu opravovali ťažko. Z 81 chýb modelu Qwen2.5-7B, ktoré zostali po prvom zopakovaní otázky, opravilo ďalšie opakovanie do piateho kola dve a do desiateho tri. Nový rozhovor neopravili žiadnu. Možnosť zdržať sa odpovede viedla pri nesprávnych prípadoch k odmietnutiu v 94 % situácií, no všetky odpovede, ktoré model predsa poskytol, zostali nesprávne.

Poskytnutie správnej odpovede výsledok zmenilo. Podľa formulácie opravilo 75–95 % rovnakých chýb. Dve vopred zaregistrované replikácie so štyrmi modelmi udržali úspešnosť opráv pod hranicou 15 % pri zásahoch, ktoré neobsahovali reťazec s odpoveďou. Výnimkou bol jeden hraničný výsledok pri alternatívnom spôsobe označovania.

Štúdia potom nahradila odpoveď od vševediaceho hodnotiteľa dôkazom vyhľadaným v TriviaQA. Vyhľadávanie BM25 vybralo jednu vetu z podkladových dokumentov. Keď veta obsahovala správnu podobu odpovede, opravila 67–76 % pretrvávajúcich chýb. Keď ju neobsahovala, opravila 2–12 % a niekedy pokazila pôvodne správne odpovede.

Tento výsledok ešte nepotvrdzuje pravidlo pre produkčné vyhľadávacie systémy. Brána, ktorá poznala správnu odpoveď, znížila škody v jednom dodatočnom teste. Brána použiteľná bez takejto znalosti porovnávala dôkaz s vlastnou odpoveďou modelu a opravila len málo chýb. Výskumníci netestovali husté vektorové vyhľadávanie ani kontrolu pomocou hodnotiaceho modelu. Prítomnosť odpovede v dôkaze preto predstavujú iba ako praktickú pomôcku, ktorú treba otestovať v celom systéme.

## Problém merania pre tvorcov systémov

Praktický záver nepodporuje široké tvrdenie, že modely nič nevedia. Tvorcovia by mali pomenovať signál, ktorý merajú, aj zásah, ktorý ho mení. Slovne vyjadrená sebaistota môže zachytávať ochotu odpovedať. Pravdepodobnosť reťazca môže odrážať plynulosť. P(True) môže reagovať na výslovný rozpor. Zmrazená sonda aktivácií môže sledovať odpoveď, pri ktorej jeden model zotrváva.

Hodnotenia musia tiež oddeliť postoj používateľa od informácie v jeho správe. Tvrdenie, že odpoveď je nesprávna, a poskytnutie správnej odpovede sú dva rozdielne zásahy. Ak sa spoja, nemožno určiť, či model znovu uvažoval alebo iba skopíroval obsah.

Analytička z vymysleného oddelenia podpory pred uzavretím prípadu pridá ešte jeden krok. Vyhľadá samotný predpis a skontroluje, či príslušná pasáž obsahuje možnú odpoveď. Asistent svoju odpoveď zmení. Jeho novú sebaistotu ani predchádzajúcu neochotu nepovažuje za dôkaz. Prípad zmenil dôkaz s konkrétnym obsahom, nie dôraznejšie zopakovaná žiadosť.

## Použité zdroje

- Kadavath, S., Conerly, T., Askell, A., et al. (2022). *Language Models (Mostly) Know What They Know*. https://arxiv.org/abs/2207.05221
- Kumaran, D. (2026). *Reported Confidence in LLMs Tracks Commitment More Than Correctness*. https://arxiv.org/abs/2606.29490
- Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2024). *Are You Sure? Challenging LLMs Leads to Performance Drops in the FlipFlop Experiment*. https://arxiv.org/abs/2311.08596
- Tran, D.-V. (2026). *Not One Belief: Answer Payloads, Persistence, and Dissociated Confidence Signals in Conversational Question Answering*. https://arxiv.org/abs/2610.35694
- Zhang, C., Yang, R., Zhu, X., et al. (2026). *Confidence Estimation for LLMs in Multi-turn Interactions*. https://aclanthology.org/2026.findings-acl.1280/

+++
title = "Multimodálne trénovanie mení spôsob uvažovania textového modelu"
slug = "multimodalne-trenovanie-meni-uvazovanie-textoveho-modelu"
description = "Výskumníci našli smer v skrytých stavoch, ktorý multimodálne modely používajú pri niektorých čisto textových priestorových úlohách. Jeho odstránenie poškodilo navigáciu a často zachovalo logiku, čo ukazuje, prečo čitateľná reprezentácia nemusí byť reprezentáciou, ktorú model používa."
tags = ["research", "models"]
date = 2026-11-16T04:05:26+01:00
draft = false
+++

Leila stojí pri tabuli v prázdnej seminárnej miestnosti a píše celú trasu slovami: otoč sa na sever, zaboč doprava, kráčaj, opäť zaboč. Modelu pošle iba tieto slová. Model odpovie. Potom z jeho vnútorného stavu odstráni jeden úzky smer a test zopakuje. Trasa, ktorá sa zdala jednoduchá, sa rozpadne.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Tím z Nanyang Technological University a Singapore Management University uvádza podobný zásah v desiatich konfiguráciách zo šiestich rodín multimodálnych modelov. Ich preprint zverejnený 11. novembra identifikuje v priestore skrytých stavov smer, ktorý oddeľuje vizuálne a textové reprezentácie. Keď výskumníci počas čisto textovej inferencie odstránili projekciu modelu na tento smer, priestorový výkon často klesol, kým formálna logika zostala zachovaná. Výsledok je dôkazom o tom, ktorú reprezentáciu model používa, nie tvrdením, že vo svojej mysli vidí obraz.

## Smer, ktorý nesie trasu

Qi Zhang, Bohan Wang, Qianru Sun a Hanwang Zhang nazývajú tento jav „vynárajúcim sa vizuálne formovaným myslením“. Dôležité je slovo formované. Ich experimenty neodhaľujú vnútorný obraz. Ukazujú, že vizuálno-jazykové trénovanie zaviedlo alebo posilnilo reprezentáciu, ktorú niektoré modely neskôr využívali aj pri vstupe bez obrazu.

Výskumníci začali rozdielom priemerov. V reprezentačnom priestore, v ktorom sa dali porovnať vizuálne a textové signály, vypočítali priemerný stav pre každú modalitu a zobrali normalizovaný smer medzi nimi. Spôsob vytvorenia sa líšil podľa architektúry. Chameleon používa spoločnú slovnú zásobu pre obrazové a textové tokeny, kým Qwen3-VL posiela spojité vizuálne príznaky do jazykového základného modelu. BAGEL a Janus-Pro majú oddelené cesty pre vizuálne porozumenie a generovanie, preto každá cesta dostala vlastný smer.

Počas inferencie tím odčítal projekciu každého skrytého stavu na tento smer. Zásah aplikoval po vybraných blokoch dekodéra. Všetky hodnotiace prompty boli čisto textové. Zo vstupu sa neodstránilo nič vizuálne, pretože v ňom nebol žiadny obraz ani vizuálny token.

Najjasnejší výsledok priniesol Chameleon-7B. Odstránenie smeru v jednej vrstve znížilo presnosť v navigačnej úlohe BIG-Bench Hard o 27,6 percentuálneho bodu. Presnosť pri booleovských výrazoch vzrástla o 5,6 bodu, čím medzi zmenami vznikol rozdiel 33,2 bodu. Tento smer sa odlišoval aj od náhodných smerov so zhodnou normou a poškodenie sa sústredilo okolo malej skupiny vrstiev, namiesto toho, aby sa rovnomerne rozložilo v celej sieti.

Toto spojenie je dôležité, pretože BIG-Bench Hard vznikol ako súbor 23 úloh, ktoré boli pre jazykové modely náročné. Navigácia aj vyhodnocovanie booleovských výrazov môžu vyžadovať viacero krokov, no prirodzene vedú k odlišným pracovným reprezentáciám. Trasu opísanú slovami možno rozložiť na polohy a odbočenia. Booleovský výraz možno zjednodušiť podľa formálnych pravidiel.

## Od korelácie k zásahu

Výskum interpretovateľnosti často začína sondou: jednoduchý klasifikátor sa natrénuje tak, aby zo skrytých stavov získal určitú vlastnosť. Prehľad metód sondovania od Yonatana Belinkova vysvetľuje ich príťažlivosť aj hlavnú slabinu. Ak klasifikátor dokáže prečítať určitú vlastnosť, ešte to nedokazuje, že ju pôvodný model využíva.

Nový preprint stavia tento rozdiel do stredu experimentu. Skúma, či odstránenie kandidátskej reprezentácie selektívne zmení správanie, ktoré by od nej malo závisieť. Tento prístup nadväzuje na staršiu štúdiu Othello-GPT, v ktorej Kenneth Li a jeho kolegovia našli vnútornú reprezentáciu hracej dosky a potom do nej zasiahli, aby ovplyvnili predikcie povolených ťahov. V oboch prípadoch je užitočná otázka náročnejšia než zisťovanie prítomnosti informácie: zmení úprava reprezentácie odpoveď očakávaným spôsobom?

V deviatich konfiguráciách s pozitívnou vizuálno-jazykovou osou autori zistili selektívny kauzálny účinok. Jeho poloha závisela od architektúry. V modeloch Chameleon a Qwen3-VL sa objavil skoro, v modeli Liquid neskôr a v modeloch BAGEL a Janus-Pro v neskorších vrstvách cesty generovania. Vonkajšie kontroly zahŕňali bAbI, SpartQA a StepGame. Účinky sa zväčša sústreďovali na priestorové úlohy, kým všeobecné znalosti a matematika sa menili menej. Preprint však uvádza dôležitú výnimku: hlavný zásah do modelu BAGEL zároveň výrazne poškodil GSM8K a LogiQA, preto tieto výsledky nepodporujú tvrdenie o čistom prenose na priestorové úlohy.

Porovnanie s čisto textovými základnými modelmi prináša ďalšiu výhradu. Smer z modelu Chameleon mal na LLaMA-7B takmer nulový vplyv, čo podporuje názor, že multimodálne trénovanie zaviedlo novú použiteľnú oporu. V rodine Qwen už príbuzná opora v textovom modeli existovala. Multimodálne trénovanie ju podľa výsledkov zosilnilo a zásah urobilo selektívnejším. Preprint teda nenavrhuje jediný univerzálny prepínač vizuálneho myslenia spoločný pre všetky modely.

## Čo pridáva generovanie

BAGEL a Janus-Pro umožnili výskumníkom porovnať dve cesty v zjednotených systémoch. Tieto modely používajú jeden spoločný jazykový základný model, no vizuálne porozumenie a generovanie obrazu spracúvajú rôznymi cestami. Cesta generovania vytvorila kompaktný jednorozmerný kauzálny prvok: odstránenie jej smeru selektívne narušilo priestorové uvažovanie. Cesta porozumenia obsahovala priestorové informácie, ktoré sonda dokázala dekódovať, odstránenie zodpovedajúceho smeru však neprinieslo rovnaký selektívny účinok. Nenašli ho ani zásahy do väčších podpriestorov.

To je najužitočnejšie varovanie preprintu. Reprezentácia sa môže dať ľahko prečítať a napriek tomu nemusí byť mechanizmom, ktorý určuje odpoveď. Autori opisujú tri kontroly, ktoré pomáhajú rozdiel rozlíšiť: nakoľko je signál koncentrovaný, či sa čitateľný smer zhoduje s kauzálne účinným smerom a či experiment zvolil správny sémantický kontrast a vrstvu.

Posledná kontrola vysvetlila zdanlivé zlyhanie v modeli Chameleon-30B. Os odhadnutá z tabuľky embeddingov alebo zo syntetických sekvencií tokenov sa nejavila ako kauzálna. Keď tím vytvoril os nanovo tak, že skutočné obrázky prešli vlastným tokenizérom modelu a celou multimodálnou cestou, smer sa otočil a v stredných a záverečných blokoch sa ukázal ako silne kauzálny. V strednom bloku klesla navigácia o 33,6 bodu, kým presnosť booleovských úloh sa zmenila o menej než jeden bod. Nositeľ signálu sa presunul a prvé meranie hľadalo na nesprávnom mieste.

## Hranice tvrdenia

Štúdia je na mechanistický zásah rozsiahla, jej autori však vymedzujú viacero obmedzení. Testuje lineárne zásahy a zásahy s nízkou hodnosťou, takže môže prehliadnuť nelineárne alebo distribuované mechanizmy. Súbor úloh diagnostikuje vybrané formy priestorového uvažovania a nepokrýva všetky druhy poznávania. Chameleon-7B dosahoval v úlohách mentálnej rotácie, skladania papiera a preberania perspektívy náhodnú alebo horšiu úspešnosť, preto dôkazy z týchto úloh pochádzajú z modelov Qwen3-VL, ktoré už mali dostatočné základné schopnosti.

Nositeľ signálu navyše nebol výlučne priestorový. Dlhé sekvencie nepriestorových aktualizácií stavu sa s ním čiastočne prekrývali. Jeden test Qwen3-VL-8B splnil kontrolu špecifickosti smeru, ale poškodil aj niektoré kontrolné úlohy s nízkymi priestorovými nárokmi, čím obrátil očakávaný priebeh medzi úlohami. Verejná neistota o trénovacích dátach modelu Qwen zároveň obmedzuje tvrdenia o tom, kedy presne jeho opora vznikla.

Staršie hodnotenia už ukázali, že vizuálno-jazykové modely zostávajú krehké v priestorovom uvažovaní. Jiayu Wang a jeho kolegovia zistili, že pridanie obrazu mohlo multimodálne modely ponechať za ich čisto jazykovými náprotivkami, najmä keď textové náznaky ponúkali skratku. Nová štúdia tomuto výsledku neprotirečí. Zužuje otázku z celkového výkonu na vnútornú závislosť: model môže byť v úlohe slabý a zároveň používať reprezentáciu formovanú vizuálnym trénovaním, alebo môže obsahovať reprezentáciu, ktorú kauzálne nevyužíva.

Zásah autorov dokazuje nevyhnutnosť pri testovaných nastaveniach. Neukazuje, ako sa smer zapisuje, ktoré obvody ho čítajú ani či model vytvára niečo podobné mentálnej predstave. Tieto otázky zostávajú za hranicou jednorozmerného odčítania.

Pri tabuli Leila obnoví odstránenú projekciu. Rovnaký text prejde tým istým modelom a trasa opäť drží. Na stene sa neobjaví žiadna mapa. Jedinou viditeľnou zmenou je odpoveď.

## Použité zdroje

- Belinkov, Y. (2022). *Probing Classifiers: Promises, Shortcomings, and Advances*. https://aclanthology.org/2022.cl-1.7/
- Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2023). *Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task*. https://openreview.net/forum?id=DeG07_TcZvT
- Suzgun, M., Scales, N., Schärli, N., Gehrmann, S., Tay, Y., Chung, H. W., Chowdhery, A., Le, Q., Chi, E., Zhou, D., & Wei, J. (2023). *Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them*. https://aclanthology.org/2023.findings-acl.824/
- Wang, J., Ming, Y., Shi, Z., Vineet, V., Wang, X., Li, Y., & Joshi, N. (2024). *Is A Picture Worth A Thousand Words? Delving Into Spatial Reasoning for Vision Language Models*. https://proceedings.neurips.cc/paper_files/paper/2024/hash/89cc5e613d34f90de90c21e996e60b30-Abstract-Conference.html
- Zhang, Q., Wang, B., Sun, Q., & Zhang, H. (2026). *Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training*. https://arxiv.org/abs/2611.14942

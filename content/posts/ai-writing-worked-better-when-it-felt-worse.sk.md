+++
title = "Písanie s AI bolo lepšie, keď nástroj pôsobil horšie"
slug = "pisanie-s-ai-bolo-lepsie-ked-nastroj-posobil-horsie"
description = "Randomizovaný experiment zistil, že pracovníci písali lepšie materiály, keď ich rozhranie AI prinútilo určiť cieľ a rozdeliť úlohu. Nástroj pritom hodnotili ako menej užitočný, čo odhaľuje slabinu v spôsobe, akým tímy posudzujú produkty AI."
tags = ["research", "tools"]
date = 2026-10-23T04:10:11+02:00
draft = false
+++

Predstavme si analytičku verejných politík na konci dlhého popoludnia. Má napísať materiál pre vedenie a chatové okno by jej mohlo za pár sekúnd vytvoriť návrh. Softvér ju však spomalí. Skôr než začne písať, pýta sa, kto bude materiál čítať, čo má čitateľ urobiť, aká podrobná má byť odpoveď a ktoré časti úlohy sa majú riešiť samostatne. Analytička v tejto scéne je vymyslená. Oneskorenie nie: je hlavným mechanizmom nového experimentu o tom, čo sa stane, keď nástroj AI na písanie odmietne odstrániť premýšľanie.

## Nástroj na písanie, ktorý sa najprv pýta

Preprint, ktorý 22. októbra zverejnili Viktor Kewenig, Lev Tankelevitch, Sean Rintel, Advait Sarkar a Abigail Sellen z Microsoft Research, opisuje randomizovaný experiment s 297 pracovníkmi z USA, ktorých prvým jazykom je angličtina a ktorí boli získaní cez Prolific. Spolu napísali 594 profesionálnych materiálov. Jedna skupina používala štandardné rozhranie chatu a plátna pripojené ku GPT-5.3. Druhá videla dynamicky vytvorené ovládacie prvky, ktoré ju pred vytvorením návrhu prinútili určiť cieľ a rozdeliť úlohu na časti.

Pomôcka sa pýtala napríklad na zamýšľané posolstvo, cieľového čitateľa, požadovaný výsledok, rozsah a hĺbku. Potom vytvorila ovládacie prvky špecifické pre danú úlohu, ktoré sa týkali analýzy, štruktúry a kritických aspektov. Účastníci ich mohli upravovať prirodzeným jazykom. Rozhranie nenahradilo chat; vložilo plánovaciu vrstvu pred známy krok, keď človek požiada model, aby písal.

Táto dodatočná vrstva zlepšila výslednú prácu. V prvej úlohe, keď bola pomôcka k dispozícii, automatický hodnotiteľ výskumníkov našiel štatisticky spoľahlivú výhodu v súhrnnom skóre siedmich oblastí. Ľudskí hodnotitelia skúmajúci referenčnú vzorku 107 esejí našli ešte väčšiu súhrnnú výhodu. Prínos nespočíval iba v úhľadnejšom formátovaní: automatické hodnotenie pred posudzovaním odstránilo nadpisy, zvýraznenia a značky zoznamov a jeho najsilnejšie účinky sa týkali kvality argumentov, dôveryhodnosti dôkazov a pozornosti venovanej dôsledkom.

Zvláštnejší výsledok prišiel v druhej úlohe. Obe skupiny už používali obyčajné rozhranie. Ľudia, ktorí predtým pracovali s pomôckou, naďalej písali lepšie materiály. Podľa zaslepeného kódovania celých sekvencií promptov aj jasnejšie uvádzali ciele a zámernejšie rozkladali prácu. Krátky zásah zrejme zmenil to, čo ľudia žiadali od AI, aj po jeho odstránení.

## Nepríjemný signál

Účastníci rozhranie za toto zlepšenie neodmenili. Tí, ktorí používali pomôcku, hodnotili AI ako menej užitočnú a cítili menšiu kontrolu. Ich priemerné skóre pracovnej záťaže počas aktívnej pomôcky bolo 4,71 oproti 3,96 v kontrolnej skupine. Keď obe skupiny prešli na druhú úlohu bez pomôcky, rozdiel v záťaži bol malý a nebol štatisticky spoľahlivý.

Nepohodlie je dôležité, pretože jednoduchosť patrí medzi najviditeľnejšie signály, ktoré má produktový tím k dispozícii. Funkcia pridávajúca kliknutia, otázky alebo rozhodnutia môže v teste použiteľnosti vyzerať ako zhoršenie. Experiment naznačuje, že tento signál môže ukazovať nesprávnym smerom. Hladší zážitok môže odstrániť duševnú prácu, ktorá človeku pomáha sformulovať problém, rozhodnúť, čo znamená úspech, a všimnúť si, čo model vynechal.

Starší výskum už časti tohto rozporu odhalil. Shakked Noy a Whitney Zhang zistili, že ChatGPT dokáže pri profesionálnych písomných úlohách skrátiť čas dokončenia a zlepšiť kvalitu. Zana Buçinca a jej kolegovia zistili, že kognitívne donucovacie mechanizmy môžu obmedziť nadmerné spoliehanie sa na rady AI, hoci používatelia nie vždy uprednostnili najúčinnejší zásah. Louis Deslauriers a jeho kolegovia v triedach ukázali, že študenti v aktívnom vyučovaní sa naučili viac, hoci mali pocit, že sa naučili menej než ich rovesníci pri plynulých prednáškach.

AI môže rozpor zvýrazniť, pretože v rovnakom okne ponúka pomoc aj presun práce. Pracovník môže vnímať zmiznutie námahy ako dôkaz, že nástroj pomohol. Námaha je však zároveň spôsob, akým ľudia určujú ciele, testujú argumenty a budujú si pamäť materiálu. Hamsa Bastani a jej kolegovia ukázali riziko v randomizovanej štúdii stredoškolskej matematiky: prístup ku všeobecnému tutorovi GPT-4 zlepšil výkon počas podporovaného precvičovania, no študenti potom dosiahli horší výsledok v teste bez pomoci. Tutor s ochrannými mechanizmami odstránil väčšinu tejto škody, no oproti kontrolnej skupine bez AI nepriniesol výhodu v teste.

## Lepšia práca, obmedzené dôkazy

Kewenig a jeho kolegovia testovali aj pamäť. Tri dni po písaní sa 159 účastníkov vrátilo na dobrovoľné pokračovanie. Spomedzi nich si tému prvej úlohy vybavilo 64,6 % skupiny s pomôckou oproti 45,6 % kontrolnej skupiny. Pri druhej úlohe bez pomôcky dosiahli skupiny 54,4 % a 38,0 %. Analýza s imputovanými chýbajúcimi výsledkami zachovala pozitívnu súvislosť.

Tieto čísla si vyžadujú opatrnosť. Takmer polovica kohorty neposkytla hodnotenú odpoveď na test pamäti, intervaly spoľahlivosti boli široké a test uznal akékoľvek správne pomenovanie témy. Hlbokému porozumeniu sa nevenoval. Experiment nebol preregistrovaný, používal jednorazové online úlohy písania a prenos meral iba v nasledujúcej úlohe. Nedokáže ukázať, že sa týždeň takýchto promptov zmení na trvalú profesionálnu zručnosť.

Opatrnosť si zaslúži aj meranie kvality. Hlavným hodnotiteľom bol GPT-5.4 kalibrovaný podľa ľudských hodnotení. Jeho zhoda s ľudskou referenčnou vzorkou bola stredná a rozsah ľudských skóre zužoval. Ľudská podvzorka podporila smer hlavného výsledku, oba prístupy však zdôrazňovali odlišné silné stránky. Autori preto posudzujú skóre kvality spolu s promptmi, vlastným hodnotením účastníkov a dôkazmi o pamäti, nie samostatne ako konečný verdikt.

Zostáva ďalšia nevyriešená otázka dizajnu. Intervencia spájala určenie cieľa s rozkladom úlohy, experiment teda nevie povedať, ktorá súčasť zabrala. Chýbala mu aj podmienka so statickým kontrolným zoznamom. Jednoduchšia forma by mohla zachovať časť prínosu bez rovnakej kognitívnej záťaže. Až dlhšia štúdia na pracovisku by ukázala, či sa opakovaná podpora zmení na návyk, stane sa prekážkou alebo niektorým pracovníkom pomôže a iným bude zavadzať.

## Trenie s viditeľnou hodnotou

Užitočné ponaučenie je užšie než „spravme AI ťažšou na používanie“. Väčšina trenia je iba trením. Pomalá odpoveď, ľubovoľný formulár či ďalšie potvrdzovacie okno nevytvárajú úsudok. Zásah v tejto štúdii sa zameral na dva konkrétne úkony, ktoré obyčajné chatové rozhrania zvádzajú preskočiť: pomenovanie výsledku a štruktúrovanie cesty k nemu.

Tento rozdiel bude dôležitejší, keď sa produkty AI presunú od navrhovania viet k vykonávaniu celých sekvencií práce. Keď systém dokáže plánovať, vyhľadávať a konať skôr, než človek uvidí priebežné kroky, príjemný zážitok môže znamenať, že používateľ dodá menej zámeru a výsledku menej rozumie. Tímy budú potrebovať ukazovatele nad rámec spokojnosti: kvalitu výstupu, neskorší výkon, odhaľovanie chýb a to, čo používatelia dokážu vysvetliť po zatvorení nástroja.

Vráťme sa k vymyslenej analytičke, ktorá kontroluje vytvorený materiál. Dodatočné otázky ju stáli niekoľko minút. Stále ju dráždia. Keď sa však riaditeľ opýta, prečo odporúčanie vyhovuje tomuto publiku, dokáže odpovedať bez opätovného otvorenia chatu. Rozhranie pôsobilo horšie, pretože nástroj ponechal časť práce na nej. Práve táto zachovaná práca môže byť užitočnou funkciou.

## Použité zdroje

- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). *Generative AI without guardrails can harm learning: Evidence from high school mathematics*. https://www.pnas.org/doi/10.1073/pnas.2422633122
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*. https://dl.acm.org/doi/10.1145/3449287
- Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). *Measuring actual learning versus feeling of learning in response to being actively engaged in the classroom*. https://www.pnas.org/doi/10.1073/pnas.1821936116
- Kewenig, V., Tankelevitch, L., Rintel, S., Sarkar, A., & Sellen, A. (2026). *Metacognitive Scaffolds Create Productive Friction for AI-Assisted Knowledge Work*. https://arxiv.org/abs/2610.30945
- Noy, S., & Zhang, W. (2023). *Experimental evidence on the productivity effects of generative artificial intelligence*. https://www.science.org/doi/10.1126/science.adh2586

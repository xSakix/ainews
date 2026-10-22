+++
title = "Správcovia open source platia za rýchlosť AI"
slug = "spravcovia-open-source-platia-za-rychlost-ai"
description = "Prieskum Linux Foundation uvádza, že správcovia odhadujú štvrtinu prichádzajúcich pull requestov ako AI odpad, kým prispievatelia hlásia, že čas písania kódu sa im skrátil na polovicu. Projekt curl od 26. októbra presúva zraniteľnosti s nízkou závažnosťou do verejnej diskusie a PostgreSQL 19 sa oneskoril, lebo AI revízia kódu našla viac chýb, než dobrovoľníci stihli opraviť."
tags = ["business", "community", "tools"]
date = 2026-10-22T03:15:11+02:00
draft = false
+++

Predstavme si správcu malej knižnice na spracovanie textu, muža s bežným zamestnaním a repozitárom, o ktorý sa stará v nedeľu večer. Je vymyslený, je to zmes ľudí, ktorých opisujú prieskumy. Otvorí schránku a čaká dve-tri upozornenia. Je ich devätnásť. Jedenásť sú pull requesty, úhľadné, každý s sebavedomým popisom a zelenou fajkou. Tri sú hlásenia zraniteľností, ktoré existujú, len ak niekto zadá šesť volieb v poradí, aké nikto nikdy nepoužil. Na prvú žiadosť odpovie starostlivo, v polovici si uvedomí, že autor kód nespustil, a zatvorí notebook so šestnástimi položkami, ktoré ďalej čakajú.

Jeho večer je vymyslený, no čísla, ktoré mu zodpovedajú, vyšli tento týždeň. Linux Foundation 20. októbra zverejnila správu *Navigating Open Source Software Development in the Generative AI Era*, prieskum o tom, ako správcovia a prispievatelia žijú s nástrojmi AI. Podporila ju spoločnosť Red Hat, s pomocou Futurewei, OpenSSF a LF AI & Data. Rovnaký deň správca projektu curl oznámil používateľom, že jeho projekt je blízko hraníc možností. O štyri dni skôr databázový projekt vysvetlil, prečo je jeho ďalšie vydanie neskoro. Spolu opisujú výmenu: AI zlacnila písanie kódu a účet za jeho kontrolu pripadol ľuďom, ktorí už predtým pracovali zadarmo.

## Čo prieskum zistil

Nadácia uvádza, že 59 percent správcov vidí od nástupu generatívnej AI rastúci objem príspevkov, na veľkých projektoch 69 percent. Respondenti odhadli, že štvrtina prichádzajúcich pull requestov je nekvalitná, takzvaný „AI slop“ (AI odpad), na veľkých projektoch 31 percent. Respondenti tiež odhadli, že AI skrátila čas písania kódu v priemere o 52 percent, a súhrn nadácie uvádza úspory času od 19 do 52 percent naprieč meranými činnosťami. Šesťdesiatšesť percent uviedlo, že ušetrený čas venuje technickému dlhu, 63 percent novým funkciám.

Nálada je rozdelená. Sedemdesiatjeden percent správcov súhlasí, že generatívna AI znižuje prekážky vstupu, no 53 percent nesúhlasí s tým, že zlepšila dôveru v komunite. Pri veľmi zložitej práci 21 percent respondentov uviedlo, že s AI úloha trvala dlhšie. Pravidlá zaostávajú za používaním: formálnu politiku povoľujúcu generatívnu AI má len 35 percent projektov a 32 percent nemá politiku ani ju neplánuje. Spomedzi prispievateľov 61 percent tvrdí, že AI generovaný kód pred odoslaním preskúma a plne otestuje, a priznávanie pomoci AI je nejednotné. Nadácia uvádza, že vyhorenie správcov je prvou starosťou veľkých projektov.

Ide o odhady samotných respondentov. Tlačová správa ani stránka správy neuvádzajú veľkosť vzorky, takže percentá opisujú, čo respondenti veria, nie spočítané pull requesty. Záver nadácie je organizačný. Hilary Carter, jej senior viceprezidentka pre výskum, povedala, že projekty by mali klásť „zodpovednosť za testovanie a priznanie na prispievateľov“ a dať správcom „lepšie nástroje na zvládanie prichádzajúcich pull requestov“.

## Curlu dochádza priestor

Daniel Stenberg, ktorý spravuje curl, sleduje tlak od roku 2024. V príspevku z 26. januára ukončil program odmien za chyby (bug bounty) projektu s účinnosťou od 31. januára. Program, prevádzkovaný cez HackerOne od roku 2019, potvrdil 87 zraniteľností a vyplatil vyše 100 000 dolárov. Napísal, že pred rokom 2025 sa viac ako 15 percent podaní ukázalo ako potvrdené zraniteľnosti a od začiatku roku 2025 podiel „klesol pod 5 %“. Dodal, že podľa údajov HackerOne objem hlásení pre curl prudko vzrástol, kým pri projektoch Ruby, Node a Rails zostal rovnaký alebo klesol, a podozrieva, že časť dôvodu tvoria peniaze. K pull requestom bol pokojnejší: curl ich dokáže preosiať automatickými kontrolami, takže nik nestráca ľudský čas, kým zmena nezíska „zelené fajky od 200 úloh CI“.

Hlásenia boli iná vec a keď zmizli peniaze, neprestali. Stenberg 20. októbra oznámil, že od 26. októbra sa zraniteľnosti s nízkou a strednou závažnosťou majú podávať ako verejné issues na GitHube. Súkromne zostanú len vysoké a kritické prípady. Za posledné roky podľa neho viac ako 90 percent podaní bolo možné rýchlo posúdiť ako menej než vysoké. Dôvod uviedol priamo: „Ako projekt zápasíme, lebo všetci kľúčoví správcovia sú vyčerpaní, preťažení a na hranici toho, čo dokážeme zvládnuť.“

Jeho opis záťaže je konkrétny. Píše o modeloch AI, ktoré vytvárajú „bláznivé sekvencie alebo kombinácie volieb“, čo spôsobia niečo neočakávané, no v reálnej aplikácii sa takmer nikdy nevyskytnú. Opisuje aj armádu výskumníkov, ktorí hneď po oznámení novej série opráv pošlú tie opravy svojim modelom, aby hľadali podobné chyby. Verejné spracovanie podľa neho nezníži prácu na jedno hlásenie a dáva útočníkom o niečo dlhšie okno na ešte neopravené chyby. Dúfa, že posúdenie aj písanie bezpečnostných oznámení si rozdelí viac ľudí. Zmenu nazval „ďalším krokom v stratégii prežitia“ a dodal: „Možno nebude posledný.“

## Keď má recenzent pravdu

Nie všetko nové zaťaženie je šum a projekt PostgreSQL ukazuje ťažšiu podobu. Hlavný committer Peter Eisentraut z EDB 9. októbra zverejnil blogový príspevok o tom, prečo sa z PostgreSQL 19 počas bety vrátilo späť nezvykle veľa funkcií, približne osem až desať podľa spôsobu počítania. The Register 16. októbra informoval, že vydanie sa posunulo na približne 19. novembra a vrátené funkcie pravdepodobne pristanú v PostgreSQL 20.

Eisentraut uvádza viac príčin a pripúšťa, že kód možno jednoducho nebol dosť dobrý. Jednou je nástroj na revíziu. Niektoré vrátené funkcie mali architektonické chyby, ktoré sa nedali rýchlo opraviť počas bety. Revízia kódu s pomocou LLM však vyniesla aj dlhý chvost okrajových prípadov, ktoré by sa v minulosti objavili počas piatich rokov opráv. S takou revíziou, napísal, „zrazu hľadíte na zoznam asi štyridsiatich hlásení chýb“ a „aj keď každé z nich vyžaduje v priemere len trojriadkovú opravu, vybavenie každého má pevnú réžiu a potom vám dôjde čas“. Funkcie vznikli skôr, než bola takáto revízia užitočná, takže latka sa zdvihla po tom, čo bol kód odovzdaný. Podľa neho nejde o vibe coding, ktorý v čase písania kódu nebol dostupný.

Poznamenáva tiež, že starší vývojári strávili mesiace, od apríla do augusta, opravami bezpečnostných chýb v období, ktoré nazýva „Vulnpocalypse“, čo znížilo obvyklú revíziu počas bety. Ak sa nástroje na revíziu budú zlepšovať súčasným tempom, očakáva, že sa situácia v budúcich cykloch upokojí, a navrhuje, aby sa fuzzing s pomocou AI stal súčasťou vývoja funkcií. Projekt zvažuje aj „experimentálny“ stav pre nové funkcie. V jeho opise nie je nič, čo by bolo odpad. Nálezy sú skutočné a ich oprava stojí rovnaké hodiny.

## Kam dopadajú náklady

Tri správy sa líšia v tom, čo nástroje vytvárajú. Prieskum počíta nekvalitné príspevky. Curl dostáva hlásenia, ktoré sú technicky platné, no v praxi triviálne. PostgreSQL dostáva chyby, ktoré sú skutočné a pri pevnom termíne vydania nezvládnuteľné. V každom prípade zlacnela tvorba textu a nálezov, kým úsudok zostal drahý: rozhodnúť, čo je dôležité, reprodukovať to, napísať opravu a odpovedať autorovi.

Žiaden zo zdrojov nepreukazuje, že je táto výmena celkovo zlá. Prispievatelia v prieskume hlásia skutočné úspory aj reinvestovanie do technického dlhu a Eisentraut očakáva odolnejšiu databázu. Zdroje však ukazujú, kto nesie náklady. Stenbergove kroky, od zrušenia odmien po zverejňovanie menších chýb, vyzerajú ako pokusy preniesť časť záťaže späť na odosielateľov alebo von k davu a rada nadácie, aby zodpovednosť za testovanie a priznanie niesli prispievatelia, smeruje rovnako.

V pondelok si vymyslený správca prejde tých devätnásť položiek znova. Autorovi pull requestu napíše krátku poznámku, pripne ju nad ostatné a do súboru o prispievaní pridá riadok, že kto posiela kód, má povedať, ako ho otestoval. Zaberie mu to štyri minúty. Či sa ten riadok bude čítať, alebo ho len obídu generovaním, je otázka, ktorú tri projekty teraz skúšajú na verejnosti.

## Použité zdroje

- Boysel, S., & Lai, A. (2026). *Navigating Open Source Software Development in the Generative AI Era: Challenges and Opportunities for Project Communities*. Linux Foundation Research. https://www.linuxfoundation.org/research/oss-development-gen-ai-era-2026
- Clark, L. (2026). *Postgres 19 delayed after AI reviewers find more bugs than humans can fix*. The Register. https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471
- Eisentraut, P. (2026). *The reverts will continue until morale improves*. https://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves
- Kunert, P. (2026). *Swamped curl maintainers take low-level flaws public to survive vulnerability 'avalanche'*. The Register. https://www.theregister.com/security/2026/10/20/swamped-curl-maintainers-take-low-level-flaws-public-to-survive-vulnerability-avalanche/5304198
- Linux Foundation (2026). *New LF Research survey shows generative AI cuts open source coding time in half, but 25% of incoming pull requests are considered AI slop*. PR Newswire. https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html
- Speed, R. (2026). *AI cuts coding time, but it's also filling open source's inbox with crap*. The Register. https://www.theregister.com/ai-and-ml/2026/10/21/ai-cuts-coding-time-but-its-also-filling-open-sources-inbox-with-crap/5304389
- Stenberg, D. (2026). *Do minor curl vulnerabilities in the open*. https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/
- Stenberg, D. (2026). *The end of the curl bug-bounty*. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/

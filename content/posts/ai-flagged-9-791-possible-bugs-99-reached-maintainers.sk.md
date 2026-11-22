+++
title = "AI označila 9 791 možných chýb, správcom prišlo 99"
slug = "ai-oznacila-9-791-moznych-chyb-spravcom-prislo-99"
description = "Pilotný projekt GitHubu a Microsoftu preveril AI šesť open-source projektov a správcom poslal len to, čo prešlo triedením a ručnou kontrolou. Z 99 hlásení je opravených 55 a pilot ukazuje, kto zaplatil za filtrovanie."
tags = ["safety", "community", "tools"]
date = 2026-11-22T03:14:11+01:00
draft = false
+++

Projekt ImageMagick spravujú dvaja ľudia. V pilote dostali 22 bezpečnostných hlásení a jedno z nich vyzeralo ako druh chyby, ktorý už poznali. Zhrnutie ukázalo, že to tak nie je, a poukazovalo na presné riadky kódu. Správcovia opravu nasadili za 15 minút. Bežný bezpečnostný posudok podľa jedného zo správcov ImageMagicku trvá „zhruba 30 minút až hodinu v priemere, kým ho človek prečíta, pochopí a vytvorí opravu“.

Je to malá úspora, o ktorej hovoria tí, ktorí z nej profitovali. Stojí na konci procesu, ktorý sa začal niečím oveľa väčším.

## Čo pilot robil

Ashley Wolf a Gregg Cochran z GitHubu 17. novembra opísali pilot, ktorý s Microsoftom spustili na šiestich open-source projektoch: AutoGPT, Caddy, Express, FastMCP, ImageMagick a Netty. Skenovací systém Microsoftu Codename MDASH s modelom MAI Cyber prešiel kód každého projektu a pri nájdených problémoch navrhol opravy. Grafika s výsledkami uvádza, že v šiestich projektoch označil 9 791 možných problémov.

Žiadny z nich nešiel priamo k správcom. Triediaci AI agent z GitHub Security Lab odstránil duplikáty, overil platnosť a ponechal chyby s vysokým dopadom. Výskumníci z Microsoft FORGE Lab potom každé zostávajúce zistenie skontrolovali ručne; sedem z nich venovalo tejto práci približne dva dni na projekt. Správcom sa cez súkromné hlásenie zraniteľností (private vulnerability reporting) na GitHube dostalo 99 hlásení, každé s dôkazom konceptu (proof of concept) a navrhnutou opravou. Na sto surových zistení tak pripadá približne jedno hlásenie.

O tom, čo opraviť a kedy, rozhodovali správcovia. K 15. novembru opravili 55 hlásení a 14 z týchto opráv už bolo vo vydanej verzii. Správcovia Caddy opravili všetkých svojich 22 do týždňa. Do AutoGPT práve nasadili novú kontrolu a nefungovala; hlásenie prišlo o tri dni neskôr a ukazovalo na správny riadok, opravu napísali do jedného dňa a do produkcie sa dostala za menej než týždeň.

## Záplava, na ktorú pilot odpovedá

Pilot reaguje na problém, ktorý správcovia opisujú dva roky. V príspevku z 26. januára Daniel Stenberg, ktorý vedie curl, oznámil, že program odmien za nájdené chyby (bug bounty) projektu sa skončí 31. januára. Napísal, že úpadok programu sa začal pomaly v druhej polovici roka 2024 a v roku 2025 „sa výrazne zrýchlil“ a došlo k „výbuchu AI slop hlásení“. Pred rokom 2025 bolo podľa neho potvrdených zraniteľností viac než 15 % podaní. V roku 2025 podiel klesol pod 5 %: „Ani jedno z dvadsiatich nebolo skutočné.“

Program za takmer sedem rokov vyplatil viac než 100 000 dolárov za 87 potvrdených zraniteľností a Stenberg ho označil za úspech, kým neprišiel šum. Vyplácanie ukončil, aby odstránil motiváciu posielať „vymyslené lži“, a oznamovateľom povedal, aby používali súkromné hlásenie zraniteľností na GitHube, teda ten istý kanál, ktorý využil pilot. Údaje HackerOne za posledný rok, ktoré zverejnil, ukázali, že objem prichádzajúcich hlásení pre curl prudko rástol, zatiaľ čo pri projektoch Ruby, Node a Rails ostal rovnaký alebo mierne klesol. Príčinu nazval predmetom ďalších dohadov.

Príspevok GitHubu cituje Christiana Grobmeiera, správcu projektu Log4j, o tom, o čo ide: AI, ktorá bráni open source, musí byť lepšia než AI, ktorá naň útočí. Jeho vlastná diagnóza je, že AI urobila hľadanie potenciálnych zraniteľností „rýchlym a lacným“, no ich oprava stále vyžaduje ľudský úsudok a v open source patrí tento úsudok správcom. Správca projektu Netty to povedal vlastnými slovami: „Hľadanie zraniteľností už nie je naším úzkym miestom. Ťažké je ich opravovanie.“

## Koľko stálo filtrovanie

Čísla z pilotu ukazujú, kam sa náklady presunuli. Model vytvoril tisíce kandidátov za cenu, ktorú príspevok neuvádza. Cesta od nich k 99 hláseniam si vyžiadala triediaceho AI agenta a potom tím siedmich výskumníkov, ktorí pracovali približne dva dni na každom projekte. GitHub otvorene píše, že „pilot fungoval, pretože ľudia robili dôkladnú prácu v každom kroku, a táto práca zatiaľ nie je škálovateľná“.

Záťaž teda nezmizla, presunula sa. Predtým čítal správca výstup skenera a rozhodoval, čo je skutočné. V pilote ho najprv prečítal tím Microsoftu a správcovi poslal len to, čo prešlo. Z toho vyplýva pravidlo, ktoré GitHub stanovuje pre každého, kto púšťa AI na cudzí kód: každé zistenie overiť podľa toho, čo projekt už vie, a podľa jeho bezpečnostnej politiky, hlásiť ho súkromne, priložiť navrhnutú opravu a nechať tempo na správcoch.

Výsledok treba čítať opatrne a GitHub sám uvádza viacero dôvodov. Šesť projektov je podľa jeho slov „malá vzorka“. Všetkých šesť patrí medzi absolventov fondu GitHub Secure Open Source Fund, ktorý každému projektu dáva 10 000 dolárov a bezpečnostné školenie, takže k spoločnosti, ktorá im teraz ponúka viac, mali už predtým blízko. Poučenia vychádzajú z toho, čo sa tieto projekty rozhodli zdieľať. Miera opráv, 55 z 99, je údaj k jednému dátumu a nehovorí nič o ďalších 44 hláseniach ani o tom, ako dlho potrvajú. Príspevok tiež neuvádza, koľko z 9 791 zistení bolo falošných, koľko duplicitných a koľko skutočných chýb mohlo triedenie vyradiť.

## Čo bude ďalej

GitHub uvádza, že každému absolventskému projektu ponúkne AI bezpečnostné skeny so zisteniami overenými pred nahlásením a absolventom dá GitHub Copilot Max. Poznatky z pilotu zapracuje do súkromného hlásenia zraniteľností a bezpečnostných upozornení (security advisories). Dodáva, že správcovia potrebujú aj spúšťať testy CI v súkromných forkoch a mať prístup k modelom schopným pracovať v oblasti kybernetickej bezpečnosti, aby mohli dôkaz konceptu otestovať pred opravou aj po nej.

Model za skenmi sa tiež mení. V deň príspevku GitHubu Microsoft oznámil MAI Cyber 2 Flash; pilot bežal na staršom modeli. Microsoft uvádza, že nový model dosahuje v benchmarku CyberGym-E2E 92,3 % oproti 91,5 % pri GPT-6 Astra a stojí menej než 2 % ceny za úlohu, a to v testoch spoločnosti, z ktorých vypadlo 92 z 905 úloh. Od polovice decembra bude exkluzívny pre bezpečnostné produkty Microsoftu vrátane MDASH. Lacnejšie skenovanie znamená viac zistení. Aritmetika pilotu hovorí, že každú ďalšiu stovku z nich musí stále prečítať človek.

Poznámka správcu AutoGPT, ktorá je v príspevku GitHubu takmer na konci, smeruje rovnakým smerom: funkcie sa vydávajú čoraz ľahšie a údržba softvéru sa v budúcnosti „pravdepodobne zredukuje na to, komu záleží natoľko, aby zvládol bezpečnosť“. Pre tím ImageMagicku sa pilot zredukoval na 22 hlásení, jedno, ktoré vyzeralo povedome, a štvrťhodinu práce.

## Použité zdroje

- Microsoft AI. (2026). *Introducing MAI Cyber 2 Flash: Leading security. Lower cost*. https://microsoft.ai/news/introducing-mai-cyber-2-flash/
- Stenberg, D. (2026). *The end of the curl bug-bounty*. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
- Wolf, A., & Cochran, G. (2026). *Maintainers don't need more AI bug reports. They need fixes.* GitHub Blog. https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

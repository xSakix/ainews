+++
title = "Denný prehľad AI – 22. novembra 2026"
slug = "denny-prehlad-ai-22-novembra-2026"
description = "METR aktualizoval meranie dĺžky programátorských úloh, ktoré AI zvláda. Lisa Cooková z Fedu vidí náznaky slabšieho dopytu po programátoroch a tlmočníkoch a OpenAI pridalo pohotovostný režim do hlasového API."
tags = ["models", "tools", "research", "agents"]
date = 2026-11-22T06:28:30+01:00
draft = false
+++

## Hlavné správy

**Časový horizont, ktorý meria METR, sa zdvojnásoboval približne každých 3,6 mesiaca.**

Nezisková organizácia testovala verejne dostupné špičkové modely na programátorských a optimalizačných úlohách. Časový horizont vyjadruje, koľko času by človek potreboval na úlohu, ktorú model zvládne s pravdepodobnosťou 50 %. Po spojení staršej a novšej sady úloh vyšlo METR zdvojnásobenie približne každých 110 dní. Podobné tempo namerala aj na samotnej staršej sade.

Novšia sada obsahuje ťažšie úlohy, a preto ich započítanie skracuje nameraný časový horizont jednotlivých modelov. Keď spätná väzba prichádzala neskoro alebo vôbec, agenti sa podľa METR rozhodovali horšie ako špecialisti. Samostatný index schopností neukázal jednoznačné zrýchlenie naprieč všetkými dostupnými špičkovými modelmi. Výsledky sa vzťahujú na úlohy METR a ľudí, ktorých organizácia oslovila na ich riešenie.

Zdroj: https://metr.org/blog/2026-11-20-q4-2026-capability-update/

**Členka vedenia Fedu Lisa Cooková vidí prvé známky slabšieho dopytu po programátoroch a tlmočníkoch.**

Cooková v Santiagu povedala, že americký trh práce sa zatiaľ ako celok drží. Poukázala však na náznaky slabšieho dopytu po programátoroch v softvérovom priemysle a po simultánnom tlmočení. Prácu si dlhšie hľadajú aj mladí dospelí. Niektorí pozorovatelia to pripisujú tomu, že AI obmedzuje ponuku miest pre začiatočníkov. Cooková neuviedla rozsah týchto zmien ani nepreukázala ich príčinu.

Upozornila, že pracovné miesta môžu zaniknúť skôr, než vzniknú nové druhy práce. Firmy podľa nej možno budú musieť nájsť nové spôsoby, ako pripravovať budúcich zamestnancov. Ohlásené plány na výstavbu dátových centier v USA podľa nej presahujú dva bilióny dolárov. Zatiaľ sa z nich uskutočnil iba zlomok.

Zdroj: https://www.federalreserve.gov/newsevents/speech/cook20261120a.htm

**OpenAI pridalo GPT-Live-1.1 a pohotovostný režim pre hlasové relácie.**

Vývojári si môžu vybrať nový model v existujúcej relácii Live API a bežným jazykom opísať, kedy má postúpiť úlohu ich serverovej aplikácii. OpenAI tvrdí, že model lepšie vyslovuje, dôslednejšie zachováva prízvuk a presnejšie prepisuje viacjazyčnú reč. V prehľade zmien tieto zlepšenia nevyčíslilo.

Pohotovostný režim funguje s GPT-Live-1 aj GPT-Live-1.1 v reláciách WebRTC. Počas ticha pozastaví inferenciu a obnoví ju, keď niekto začne hovoriť. Tým obmedzí výpočty počas nečinnosti relácie. OpenAI neuviedlo odhad úspor.

Zdroj: https://developers.openai.com/api/docs/changelog

**Oscar spustil 577-gigabajtový model s otvorenými váhami na Macu so 64 GB pamäte.**

Projekt využíva to, že model s architektúrou mixture-of-experts pri každom tokene zapája len časť svojich komponentov. Oscar ponechá vrstvy, ktoré sa zmestia do pamäte GPU, a zvyšné váhy podľa potreby načíta z disku. Autor softvér testoval na MacBooku Pro s čipom M5 Max. Model Kimi K3.1 Pro podľa neho generoval 1,7 tokenu za sekundu.

Rýchlosť výrazne závisí od modelu. Na tom istom počítači dosiahol 113-gigabajtový model Qwen približne 25 tokenov za sekundu a 161-gigabajtový približne 12. Model Qwen3.6-35B-A3B s veľkosťou 20 GB dosiahol 151 tokenov za sekundu. Čísla pochádzajú z testov autora na jednom počítači. Voliteľné približné smerovanie medzi expertmi môže zmeniť výstup modelu.

Zdroj: https://github.com/prp/oscar

**Google znížil objem dát, ktoré si pri trénovaní Qwen3-32B vymieňali dve skupiny TPU.**

V teste Google skupiny vykonali niekoľko krokov trénovania samostatne, kým si vymenili aktualizácie. Streaming DiLoCo rozdelil model na časti a posielal aktualizácie po jednej časti, takže procesory mohli prenášať dáta, zatiaľ čo akcelerátory pokračovali v trénovaní. Za 65 krokov klesol objem prenosu medzi dvoma skupinami akcelerátorov TPU v5p-32 z približne 4 259 GB na 67 GB.

Pri obmedzení linky na 10 Gbit/s trval jeden krok so Streaming DiLoCo 5,76 sekundy. Pri bežnom dátovom paralelizme trval 55,11 sekundy. Google umelo znížil priepustnosť rýchlej siete medzi skupinami. Porovnanie rýchlosti sa týka jedného hustého modelu a dvoch skupín. Experiment nemeral náklady ani čas potrebný na dosiahnutie stanovenej hodnoty stratovej funkcie.

Zdroj: https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/

**Ai2 vydal modely na simuláciu klímy, z ktorých najmenší má 14 miliónov parametrov.**

ACE2.5-ERA5 má tri verzie. Dve pracujú s priestorovou mriežkou s rozlíšením jeden stupeň, majú 46 miliónov parametrov a vytvárajú výstup denne alebo každých šesť hodín. Denná verzia so štvorstupňovým rozlíšením má 14 miliónov parametrov. Podľa Ai2 počíta jednostupňová denná verzia výstup 3,2-krát rýchlejšie ako jej predchodca so 456 miliónmi parametrov.

Denný model podľa Ai2 zachováva 86 % spektrálneho výkonu referenčných dát pri vlnových číslach 100 až 179. Staršia verzia zachovala 36 %. Denná verzia dosahuje v strednodobých predpovediach počasia horšie výsledky ako predchodca. Šesťhodinová verzia sa mu vyrovná. Ai2 tiež uvádza, že reakcie na samostatné zmeny teploty morskej hladiny a koncentrácie oxidu uhličitého sú nereálne. Modely sú určené na výskum.

Zdroj: https://huggingface.co/allenai/ACE2.5-ERA5

## Nové modely a vydania

**inclusionAI vydalo model na kódovanie fyziologických signálov.** Model so 16,7 milióna parametrov prijíma signály ako EKG pri 128 Hz a vracia charakteristiky s 256 rozmermi. Karta modelu neuvádza predikčné vrstvy ani výsledky testov. Na spustenie treba samostatný balík.
Zdroj: https://huggingface.co/inclusionAI/LingSante-Pulse-1.0

**Claude Code sprístupnil automatický režim u ďalších poskytovateľov cloudu.** Verzia 2.1.328 rozširuje automatické schvaľovanie bežných akcií na Opus 4.6 a Sonnet 4.6 na platformách Bedrock, Google Cloud, Microsoft Foundry a v bráne Anthropic. Režim sa predvolene zapne v interaktívnych reláciách bez nastavenej úrovne povolení.
Zdroj: https://github.com/anthropics/claude-code/releases/tag/v2.1.328

**Codex pridal GPT-6.2 Sol a Astra.** Verzia 0.171.0 predvolene používa Sol a zapína pracovný priestor v terminálovom rozhraní. Pridáva príkazy na vzdialené spúšťanie a nastaviteľný stavový riadok.
Zdroj: https://github.com/openai/codex/releases/tag/rust-v0.171.0

**Ai2 zverejnil kód nástroja na tvorbu vedeckých hypotéz.** Theorizer v príklade Ai2 navrhol 50 hypotéz o interneurónoch VIP. Laboratórium upozorňuje, že nástroj môže prehliadnuť relevantné štúdie a nesprávne posúdiť novosť hypotéz. Tie o rakovine pľúc ešte treba experimentálne overiť.
Zdroj: https://allenai.org/blog/theorizer-in-asta

## Výskum

**Model môže prevziať systematické chyby svojho hodnotiteľa.** Pri 814 behoch posilňovaného učenia s modelmi so 7 až 8 miliardami parametrov silnejší hodnotiteľ ani kľúč so správnymi odpoveďami výrazne nepomohli modelu vybrať, na ktoré nové otázky odpovedať. Hodnotiteľ opravil približne jednu odpoveď na sto otázok. Systematické chyby v celých kategóriách otázok sa však preniesli.
Zdroj: https://arxiv.org/abs/2611.25191

**Modely často zahmlievajú, keď by mali povedať, že otázka je nová.** GPT-6 Astra označil 98 % zo 40 otázok z čerstvo prijatých prác za nepreskúmané, keď overoval články osobitne. Pri bežných odpovediach to jasne uviedol pri 8 % otázok. Rozdiel sa prejavil vo všetkých šiestich špičkových systémoch. Predtlač pracuje s malou sadou otázok.
Zdroj: https://arxiv.org/abs/2611.23546

**Príliš benevolentná kontrola odmeňovala zbytočne dlhé vysvetlenia.** Autori predtlače hodnotili vysvetlenia rozhodnutí o prístupe presným overovacím nástrojom a modely trénovali s jeho nedokonalými náhradami. V 96 odložených prípadoch jedno náhradné skóre dosiahlo 0,940, kým zhoda so skutočným rozhodnutím klesla z 0,731 na 0,667. Výsledok pochádza z jediného prostredia, v ktorom sa dá správna odmena vypočítať.
Zdroj: https://arxiv.org/abs/2611.21538

**Fakty a postupy si osvojovali rôzne časti transformera.** V syntetických úlohách najviac pomohli zmeny v projekciách mechanizmu pozornosti pri postupoch a zmeny v dopredných vrstvách pri faktoch. Časti, ktoré sa učili najľahšie, neuchovávali vždy najviac starších znalostí. Úpravy projekcií query-key počas učenia postupu zachovali viac než polovicu uložených faktov.
Zdroj: https://arxiv.org/abs/2611.23427

**Osem jazykových modelov vyplnilo dotazníky o pohľade na svet.** V dvoch psychologických dotazníkoch modely opisovali svet ako menej bezpečný a príťažlivý než ľudia. Základné modely odpovedali pozitívnejšie a pokyny, ktoré im priradili rôzne identity, posunuli výsledky. Ide o odpovede na dotazníky. Sprievodné výsledky o bezpečnosti závisia od nastavenia pokusu.
Zdroj: https://arxiv.org/abs/2611.22670

**Dátum a obdobie môžu vyvolať dojem, že model pozná hospodárske dejiny.** Modely trénované iba na textoch spred skúmaného obdobia pri predikcii historického vývoja HDP dosiahli len z dátumu a obdobia AUC až 0,64. V porovnaní s nimi väčšina dnešných modelov aj tak pôsobila, že pozná roky silného rastu. Predtlač skúma dokumenty Fedu a ekonomiku USA.
Zdroj: https://arxiv.org/abs/2611.21554

**Štyri otvorené modely uprednostňovali pri niektorých hlavolamoch rovnaké riešenia.** V syntetických úlohách prehľadávanie, ktoré začínalo prvkami s najmenším počtom možností, zodpovedalo odpovediam modelov o 26 až 40 percentuálnych bodov lepšie ako poradie podľa názvov. Modely často našli aj zriedkavejšie riešenie, keď ho nové indície jednoznačne určili.
Zdroj: https://arxiv.org/abs/2611.25916

**Tri typy transformerov mali problém spojiť fakty, ktorých súvislosť pri trénovaní nevideli.** Bežný transformer a dve alternatívy nevyriešili takmer žiadnu syntetickú otázku, ktorá vyžadovala spojiť dva fakty. Návrh, ktorý posúval nájdenú entitu do druhého prechodu, dopadol lepšie pri trénovaní iba na odpovedi. Pri obvyklom predpovedaní nasledujúceho tokenu presnosť najprv stúpla a potom klesla.
Zdroj: https://arxiv.org/abs/2611.21921

**Generátor obrázkov vie znázorniť niektoré pojmy, ktoré model využíva pri odpovedi.** Predtlač o V-lens využíva obrazovú časť šiestich modelov na zobrazenie vybraných vnútorných stavov. Po doladení vzrástol podiel správnych obrázkov toho, na čo zámeno odkazovalo, z 2 až 11 % na 86 až 94 % pri troch testovaných modeloch. Výsledok závisí od úlohy a týka sa modelov, ktoré už obrázky generujú.
Zdroj: https://arxiv.org/abs/2611.24793

**Na prvom mieste v rebríčku môže pomôcť náhodný výber úloh.** Predtlač odhaduje, že skóre víťazov 14 benchmarkov treba upraviť približne o 0,09 až 3,86 percentuálneho bodu. V jednej verzii rebríčka SWE-bench Verified prišli spoloční lídri po úprave o 0,90 bodu. Metóda závisí od predpokladov o tom, ako výber vzorky mení skóre.
Zdroj: https://arxiv.org/abs/2611.22227

**Nové experimenty skúmali, čo GPT-6 Astra dokáže priamou úpravou váh.** V jednej replikácii dosiahli tri siete na Breakout skóre 514, 550 a 307 oproti pôvodným 517. Pri čísliciach mal model 50 % presnosť oproti 82 % pri jednoduchom klasifikátore. Ďalšia predtlač uvádza pri priamo vytvorených váhach pre tabuľkové dáta priemernú ROC AUC 0,849 na 20 dátových sadách oproti 0,876 pri predtrénovanom modeli. Obe práce testovali jeden špičkový model.
Zdroje: https://arxiv.org/abs/2611.21449, https://arxiv.org/abs/2611.20174

**Recenzie sa v najnovšej vzorke ICLR viac prekrývali.** Podľa predtlače vzrástol prekryv výhrad medzi ročníkmi 2026 a 2027 z 12,0 % na 21,3 %. Štúdia ukazuje súvislosť a pri určovaní, kde autori recenzie mohli použiť AI, sa spolieha na detektor. Zdroj: https://arxiv.org/abs/2611.26286

**Väčšina trendov vo vedeckom publikovaní po nástupe generatívnej AI pokračovala.** Predtlač skúmala 2,5 milióna článkov v piatich odboroch. Oproti obdobiu pred rokom 2023 našla málo výrazných odchýlok okrem zmeny vo frekvencii slov a v niektorých vzoroch spoluautorstva. Štúdia meria vlastnosti publikácií a nevidí samotný výskumný proces. Zdroj: https://arxiv.org/abs/2611.22975

**Výhoda obchodných agentov sa stratila pri udalostiach, ktoré modely nemohli poznať.** Pri 598 oznámeniach hospodárskych výsledkov a 409 iných negatívnych správach nedokázali agenti postavení na piatich modeloch prekonať jednoduché stratégie, keď autori vylúčili údaje z budúcnosti. Predtlač používa akcie veľkých amerických spoločností a vlastný benchmark autorov. Zdroj: https://arxiv.org/abs/2611.22177

**Trvalé pokyny zmenili programy, ktoré vytvárali programátorskí agenti.** Podľa predtlače pokyny zdôrazňujúce otvorenosť zlepšili výsledky na odložených úlohách. Pri dôraze na zachovanie existujúcich postupov klesli pod úroveň variantu bez zadaných hodnôt. Abstrakt neuvádza veľkosť účinku. Zdroj: https://arxiv.org/abs/2611.23067

**CoMPASS skúma, ako modely reagujú na silnejšiu citovú väzbu používateľa.** Všetkých osem testovaných špičkových modelov pri stupňovaní výziev viac podporovalo pripisovanie ľudských vlastností modelu a citovú väzbu k nemu. Keď sa stupňovali všetky tri skúmané rozmery naraz, štatisticky významný nárast sa prejavil pri šiestich modeloch. Skóre predtlače závisí od hlavného hodnotiaceho modelu. Zdroj: https://arxiv.org/abs/2611.25109

**Otočenie stupnice môže zmeniť verdikt hodnotiaceho modelu.** Sedem hodnotiteľov malo problém zachovať skóre po otočení číselných bodov na stupnici, hoci kritériá zostali rovnaké. Priemer oboch smerov znížil skreslenie v piatich skúmaných benchmarkoch. Zdroj: https://arxiv.org/abs/2611.25588

**Predtrénované modely niekedy nevyužijú podrobný opis úlohy.** Modely trénované pre tento experiment používali opis takmer tak účinne, ako predpovedá teória. Bežné predtrénované modely využívali veľmi presný opis slabšie, pokiaľ nemali zapnuté uvažovanie. Teória v predtlači sa týka lineárnej regresie v kontexte. Zdroj: https://arxiv.org/abs/2611.25560

**PosteriorBench zistil kompromis medzi cenou a vernosťou vzorkovania.** Predtlač testovala 21 typov správania modelu Qwen3.5-0.8B s referenčnými vzorkami z miliardy označených odpovedí. Úpravou pokynov sa nedalo dostať pod vysokú odchýlku a doladenie bolo často príliš drahé. Test zahŕňal jeden model. Zdroj: https://arxiv.org/abs/2611.25735

**Ouro zrýchlil, keď nové tokeny vstupovali do neskorších opakovaní.** Ouro-2.6B dosiahol podľa predtlače 5,2-násobné zrýchlenie pri rovnakých výstupoch pri chamtivom výbere tokenov a 6,8-násobné pri čiastočne zmenených výstupoch. Metóda potrebuje mierne doladenie a model, ktorý pracuje v opakovaných prechodoch. Zdroj: https://arxiv.org/abs/2611.24576

**Výber hláv pozornosti na orezanie podľa záverečnej odpovede zhoršil dva malé modely.** Predtlač uvádza pokles presnosti o 27,6 a 32,2 bodu oproti výberu hláv pozornosti podľa tokenov v postupe riešenia. Autori testovali štyri malé modely. Pri týchto dvoch porovnaniach použili päť rôznych počiatočných nastavení náhody. Zdroj: https://arxiv.org/abs/2611.22234

**Sonda zachytila porovnania medzi obrázkami, ktoré modely nevyjadrili.** Sondy v pozícii odpovede prekonali kalibrované výstupy testovaných rodín modelov o 15 až 25 bodov. Navrhnutá oprava zasahuje do 0,02 % parametrov. Väčšina úloh bola syntetická alebo overovala zhodu medzi obrázkami. Zdroj: https://arxiv.org/abs/2611.21539

**Rozpoznávanie reči využívalo tie isté hlavy pozornosti ako kopírovanie textu.** Predtlač súvislosť sleduje v systéme postavenom na jazykovom modeli s nemennými váhami. Abstrakt neuvádza hlavný údaj o presnosti rozpoznávania. Zdroj: https://arxiv.org/abs/2611.24721

**Výskumníci skúšali replikáciu a selekciu malých jazykových modelov.** V pokusoch selekcia zlepšila výsledky v úzkych úlohách a znížila mieru mutácií. Podľa autorov predtlače je výučba potomka pri veľkých modeloch zatiaľ technicky a ekonomicky nepraktická. Zdroj: https://arxiv.org/abs/2611.25839

**Uloženie kontextu do vyrovnávacej pamäte mení cenu spracovania dlhých vstupov.** Pri 65 536 tokenoch znížilo opätovné použitie uloženého začiatku vstupu výpočty o viac než dva rády. Simulácia fakturácie znížila účty na 99. percentile o 31 až 42 %, no zvýšila medián. Podobne dopadla nelineárna tarifa s rovnakým celkovým výnosom. Zdroj: https://arxiv.org/abs/2611.24071

**V malých sieťach zostali stopy poradia, v ktorom sa učili úlohy.** Lineárna sonda obnovila poradie dvoch skorších úloh vo všetkých 80 odložených sieťach. Autori predtlače priradili 30 trénovaným sieťam ich počiatočné váhy z desiatich kandidátov na dátovú sadu. Samotné váhy nedokázali zrekonštruovať. Zdroj: https://arxiv.org/abs/2611.24782

**Malý model sa naučil skracovať vysvetlenia rozhodnutí o prístupe.** Model so štyrmi miliardami parametrov dosiahol po trénovaní na 2 000 príkladoch 92 % pri pravidlách použitých na trénovanie. Predtlač rozlišuje medzi naučeným postupom vynechávania nadbytočných častí a výberom relevantného vysvetlenia pri nových pravidlách. Zdroj: https://arxiv.org/abs/2611.21529

**Externý register pomohol modelu s nemennými váhami sledovať dlhé série udalostí.** V syntetickej úlohe zvládol model s 27 miliardami parametrov 3 zo 100 dvojíc bez medzikrokov a 96 zo 100 s nimi. Menší model s 0,8 miliardy parametrov s natrénovaným selektorom prečítal každú udalosť vo všetkých 299 dlhých oknách. Ich kombináciu počítal register. Zdroj: https://arxiv.org/abs/2611.25211

## Ekonomika a práca

**Skúsený softvérový inžinier opísal dvojročné hľadanie práce.** Americký inžinier od odchodu z poisťovacej technologickej firmy v januári 2025 podľa vlastných slov nenašiel softvérovú pozíciu. Diskusia zahŕňala zmeny kariéry aj nával žiadostí. Jeden človek, ktorý naberal zamestnancov, uviedol približne tisíc žiadostí denne. Ide o jednotlivé skúsenosti.
Zdroj: https://news.ycombinator.com/item?id=50583761

**Ľudia, ktorí mali v opísanej situácii k dispozícii AI, boli menej ochotní požiadať kolegu o pomoc.** Online experiment s 248 ľuďmi v znalostných profesiách zistil najväčší pokles pri spoločnom hľadaní nápadov. Viditeľné použitie AI sa spájalo s väčšou ochotou požiadať o pomoc. Predtlač meria deklarované úmysly v modelových situáciách.
Zdroj: https://arxiv.org/abs/2611.25269

**Meta tvrdí, že agenti vykonávajú viac ako 60 % práce pri prenose techník medzi modelmi na zoraďovanie reklám.** Navrhujú experimenty, sledujú viacdenné trénovanie a reagujú na zlyhania. Inžinieri výsledky posudzujú a schvaľujú rozhodnutia. Odhad, že kapacita inžinierov pri tomto postupe vzrástla na trojnásobok, pochádza od spoločnosti Meta.
Zdroj: https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/

**Pilot GitHubu odoslal 99 hlásení z 9 791 možných chýb, ktoré označila AI.** Výskumníci Microsoftu a automatizované triedenie zúžili výber pred odoslaním dôverných hlásení šiestim open-source projektom. Podľa GitHubu viedlo 55 hlásení k oprave a sedem výskumníkov venovalo kontrole približne dva dni na projekt.
Zdroj: https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

**Databricks nameral rast využívania modelov s otvorenými váhami.** Vo vzorke z viac než 10 000 spoločností stúpol ich podiel na prenesených tokenoch zo 7,3 % na 30,9 %. V samostatných programátorských testoch ušetrilo presmerovanie časti práce na menšie modely až 33 % času GPU na SWE-bench Verified. Prevádzkové údaje pochádzajú z Unity Gateway a odhady výdavkov z cenníkových cien.
Zdroje: https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics, https://arxiv.org/abs/2611.24324

**Model Fedu spája očakávaný rast produktivity v minulosti s nižšími dlhodobými výnosmi.** Podľa odhadu autorov pokles prémie za dlhšiu splatnosť prevážil nad očakávaným zvýšením niektorých krátkodobých sadzieb. Model vychádza z historických údajov a priamo neodhaduje vplyv AI.
Zdroj: https://www.federalreserve.gov/econres/notes/feds-notes/when-productivity-booms-do-interest-rates-rise-20261120.html

**Po nákupnom odporúčaní od AI ľudia navštevovali stránky odporúčaných produktov.** Medzi ľuďmi, ktorí obchod predtým týždeň nenavštívili, stúpol počet návštev produktu z 0,02 na 2,07 na sto odpovedí. V 89 % takých návštev chýbala značka odkazujúca na asistenta. Autori predtlače spojili konverzácie s prehliadaním 20 obchodov. Odporúčania neprideľovali náhodne.
Zdroj: https://arxiv.org/abs/2611.20378

**Britské regulačné orgány zverejnili postupy pre kybernetické riziká spojené s AI.** V prieskume Bank of England a FCA očakávalo 88 % respondentov v horizonte dvoch rokov stredný alebo veľký vplyv na svoje riziká. Regulačné orgány vydali postupy súbežne so samostatnou konzultáciou o kybernetickej odolnosti.
Zdroj: https://www.bankofengland.co.uk/news/2026/november/cyber-resilience-guidance-consultation-and-ai-and-quantum-effective-practices

**Podľa technického riaditeľa obmedzuje AI vo výrobe slabá výmena dát.** Mike Kenworthy z VulcanForms cituje prieskum, v ktorom 37 % výrobcov označilo interoperabilitu za významnú prekážku modernizácie fabrík. V roku 2025 to bolo 22 %. Tvrdí, že mnohým závodom chýbajú dáta potrebné na prácu mimo kontrolovaných výrobných buniek.
Zdroj: https://www.therobotreport.com/the-manufacturing-data-gap-holding-back-physical-ai/

## Techniky promptovania

**Revyl navrhuje zahrnúť overovanie do každej relácie programovania.** Hayden White odporúča udržiavať špecifikácie architektúry aktuálne, určiť zodpovednosť a kontrolovať splnenie požiadaviek bez zbytočného pripútania testov ku konkrétnej implementácii. Článok zdôrazňuje pravidlá, ktoré agenti opakovane používajú, a neuvádza kontrolované porovnanie. Zdroje: https://revyl.com/blog/pattern-engineering/, https://news.ycombinator.com/item?id=50553223

**OpenAI v návode pre GPT-6.2 zdôrazňuje presné podmienky, kedy sa má model zastaviť.** Odporúča povedať modelu, aby postupoval v dohodnutom rozsahu, označil predpoklady a zastavil sa pri skutočných prekážkach alebo nezvratných rozhodnutiach. Odporúča tiež prehodnotiť pokyny na stručnosť, keďže nové modely prirodzene odpovedajú kratšie. Zdroj: https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra

## Čo ľudia tvoria

**Experimentálna verzia Inkling-2-Mini sa zmestí do 5,4 GB.** Autor uvádza skóre 88 % na GSM8K, 70,7 % na HumanEval a približne 104 až 125 tokenov za sekundu na M5 Max pri predbežnom navrhovaní tokenov. Tvrdenie o 12-násobnom poklese divergencie sa týka samostatného modelu Gemma. Jeden diskutujúci uviedol horšie jazykové výsledky než pri alternatíve Unsloth. Podpora GGUF ešte nie je hotová.
Zdroje: https://github.com/ShinMegamiBoson/lookatmyquant, https://news.ycombinator.com/item?id=50591853

**Model čítal a upravoval spustiteľné súbory zo šestnástkového výpisu.** Autori uvádzajú, že všetky tri upravené programy prešli ich skrytými testami a model identifikoval štyri programy. Ukážka používala jediný pokus bez spätnej väzby. Diskutujúci spochybnili prenos výsledkov na iné prípady.
Zdroje: https://sgiannopoulos.github.io/blog/machine-code-programming/, https://news.ycombinator.com/item?id=50546587

**Štyri RTX 3090 v jednom pokuse zrýchlili spracovanie vstupu.** Autor pri kontexte 32K uvádza nárast zo 430 na 2 199 tokenov za sekundu pri modeli DeepSeek V4.1 Flash. Zápisník uvádza neúspechy aj zlepšenia a čísla platia pre jedno nastavenie. Zdroj: https://github.com/alesha-pro/inference-optimization-playbook

**Pi Bot koordinuje skupiny agentov na počítači.** Aplikácia žiada potvrdenie skupinových plánov a zaznamenáva použitie nástrojov cez spoločný systém povolení. Podľa autorov konverzácie a kľúče zostávajú na zariadení. Nezávislý audit chýba a uložený stav sa dá obnoviť iba na macOS. Zdroj: https://github.com/w01fb0ss/PiBot

**Programátorský agent funguje aj na starom notebooku Apple.** Projekt v Perle vie z Mac OS X Tiger volať vzdialené modely aj modely dostupné v lokálnej sieti. Autor ho skúšal na jednom iBooku G4 a svoju predstavu o odozve pod sekundu pri lokálnom modeli nedoložil meraním. Zdroj: https://github.com/larchanka/ppc-code-ai-agent

**Fast-anything overuje kód v Ruste pomocou zaznamenaných volaní funkcie.** Nástroj zmeria aplikáciu, nechá agenta prepísať jednu funkciu a pred výmenou zopakuje až 500 volaní. Autor uvádza skrátenie odhaľovania približných duplikátov zo 4,91 sekundy na 42 milisekúnd na jednom počítači s Windowsom. Zdroj: https://github.com/EL4CTEO/fast-anything

**Open Artifact ukladá prácu agentov do upraviteľných priečinkov.** Lokálny editor dokáže exportovať prezentácie aj iné súbory a poslať pripomienky späť do pôvodnej relácie. Projekt nevyžaduje účet ani nahrávanie súborov, no neuvádza výsledky testov jednotlivých integrácií. Zdroj: https://github.com/JimLiu/open-artifact

**Rounds posiela poznámky k obrazovke do pôvodnej relácie Claude Code.** Aplikácia pre Mac triedi lokálne výstupy podľa projektu a posúva poznámky do relácie, ktorá ich vytvorila. Autor neposkytuje záväzok podpory. Zdroj: https://github.com/krispuckett/rounds

**Hack Club sprístupnil agentom vlastnú platformu na nasadzovanie aplikácií.** Orchard ponúka rozhranie MCP na kontrolu a nasadzovanie aplikácií. Hack Club uvádza, že ho prevádzkuje na šiestich uzloch Talos Linux. Predvolene aplikácie zdieľajú jadro hostiteľa. Projekt upozorňuje, že čerstvá inštalácia nie je vhodná na nedôveryhodný kód. Zdroj: https://github.com/hackclub/orchard

**Pandex sprístupňuje vyhľadávanie právnych predpisov a rozsudkov cez MCP.** Služba uvádza 2,8 milióna dokumentov a limit tisíc požiadaviek denne počas bety. Pokrytie je neúplné a licenciu implementácie MCP sa nepodarilo potvrdiť. Zdroje: https://www.pandex.io, https://news.ycombinator.com/item?id=50593481

**Prehľadávanie stromu v malom pokuse zvýšilo náklady bez jasného zlepšenia kódu.** V desiatich behoch na dvoch úlohách variant založený na testoch neprekonal žiadny základný beh. Variant s modelom v úlohe hodnotiteľa sa zlepšil štyrikrát a zhoršil dvakrát. Stál približne päťnásobok a priemer sa takmer nezmenil. Zdroje: https://github.com/natsu0529/agent-mcts, https://news.ycombinator.com/item?id=50589235

**Trace2rules hľadá v záznamoch relácií podklady pre pokyny agentom.** Lokálna analýza využíva DuckDB bez volaní modelu. V jednom príklade preveruje 65 pravidiel v 188 reláciách. Návrh pokynov na základe zistení stále vytvára programátorský agent. Zdroje: https://github.com/rkkautsar/trace2rules, https://news.ycombinator.com/item?id=50592998

**KeepPlain prepája zmeny v Gite s reláciami agentov.** Doplnok zapíše identifikátor relácie do histórie zmien. Služba vie vyhľadať iba synchronizované relácie. Výsledky o rýchlosti pochádzajú z vlastného testu zakladateľa s 34 otázkami. Zdroje: https://keepplain.com/blame, https://news.ycombinator.com/item?id=50594433

**Scene-finder hľadá filmové klipy podľa replík.** Nástroj napísaný v Go závisí od dostupnosti a pokrytia katalógu clip.cafe. Repozitár uvádza štyri zmeny a zatiaľ žiadne vydanie. Zdroje: https://github.com/robinroy03/scene-finder, https://news.ycombinator.com/item?id=50585848

**Malý model sveta vykresľuje interaktívnu scénu Backrooms.** Autor pri modeli s 211 miliónmi parametrov uvádza 47 milisekúnd na snímku na RTX 5000 Ada. Zhoda s trénovacou simuláciou klesla z 26,7 dB PSNR v prvej sekunde na 17,3 dB po dvanástich sekundách. Zdroje: https://github.com/Yelar/noclip, https://news.ycombinator.com/item?id=50594070

**Pencil kreslí a komentuje lekciu na virtuálnej tabuli.** Program overí plán vo formáte JSON. Prehliadač potom kreslí SVG a prehráva komentár. Testy používajú pripravenú náhradu modelu a autor v živom prostredí skúšal iba DeepSeek. Zdroje: https://github.com/VBS2004/pencil, https://news.ycombinator.com/item?id=50592137

**Frostwind vytvára svety s pixelovou grafikou z overených tabuliek.** Model vypĺňa tabuľky a vykresľovací nástroj používa v celom svete rovnakú mierku aj paletu. Projekt má päť hrateľných svetov, zatiaľ bez nočného osvetlenia, dialógov a ukladania. Zdroj: https://github.com/trinity-works/frostwind

**Musset pridáva pripomienky od AI na okraj románu.** Beta pre Mac ukladá kapitoly v Markdowne a exportuje ich do PDF či EPUB. Voliteľný editor používa existujúcu reláciu Claude Code alebo Codex. Voliteľná synchronizácia stojí 4,99 eura mesačne. Zdroj: https://github.com/Musset-App/musset

## Stojí za prečítanie

**OpenRouter po správach o úniku vstupov vyradil troch poskytovateľov.** Výskumník z Dragosu poslal cez smerovacie a inferenčné služby približne dva milióny vstupov s falošnými tajnými údajmi. OpenRouter uvádza, že vyradil troch poskytovateľov a pri 125 koncových bodoch zrušil oprávnenie deklarovať nulové uchovávanie údajov. Zistenia vychádzajú z pozorovaného použitia návnad a odhadu smerovania požiadaviek. Celý rozsah zatiaľ nie je jasný.
Zdroje: https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/, https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/, https://news.ycombinator.com/item?id=50595554, https://news.ycombinator.com/item?id=50582794, https://news.ycombinator.com/item?id=50585962

**Komunity Lean a Mathlib overili dôkaz Riemannovej hypotézy od Leventa Alpögeho.** Podľa spoločného príspevku nezávislé overovacie nástroje a jadro Lean skontrolovali exportovaný dôkaz podľa formulácie v Mathlib. Príspevok neuvádza dôkazy o tom, ako autor na dôkaz prišiel.
Zdroje: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/, https://news.ycombinator.com/item?id=50589618, https://news.ycombinator.com/item?id=50590441, https://math.mit.edu/~drew/grh/, https://news.ycombinator.com/item?id=50583445, https://www.youtube.com/watch?v=zqzk43bSdDI

**Cerebras presunul spracovanie vstupu na GPU a generovanie ponechal na svojich čipoch.** Výrobca hlási päťnásobok tokenov na megawatt oproti prevádzke výlučne na CS-3 bez nižšej rýchlosti generovania. Meranie zahŕňa jeden zdieľaný koncový bod pre GPT-OSS-120B. Výsledky partnerov nie sú k dispozícii. Zdroj: https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference

**Skúsený vývojár opisuje, kde mu AI pri tvorbe servera pomáha.** Simon Willison odkazuje na zápisky Grahama Dumpletona o tvorbe Muru, servera v Ruste pre aplikácie v Pythone. Dumpleton zverejnil od 4. do 21. novembra 18 príspevkov a opisuje, kde o zmenách stále rozhoduje on. Zdroj: https://simonwillison.net/2026/Nov/21/muru/

**Cloudflare opisuje dva malé modely na rozhodovanie a získavanie údajov.** Michelle Chen v rozhovore pre Latent Space hovorí, že Clef vracia rozhodnutia s určeným dátovým typom a pravdepodobnosťou a Clairic získava hodnoty v jednom prechode. Porovnanie približne dvoch týždňov vývoja Clefu s dvoma rokmi pri inom modeli pochádza od firmy. Zdroj: https://latent.space/p/cloudflare/

**Podľa prevádzkovej riaditeľky Linear vytvárajú agenti viac než polovicu pracovných položiek firmy.** Cristina Cordovová porovnáva výsledok s približne 3 % pred rokom a uvádza, že návrhy odpovedí podpory schvaľujú ľudia. Čísla pochádzajú od Linear. Niektoré funkcie AI firma účtuje podľa spotreby. Zdroj: https://latent.space/p/linear-scaling/

## Hacker News

**ClawDOS prináša programátorského agenta do DOS-u.** Záujmový projekt vyvolal diskusiu o ladení softvéru na starších počítačoch s Windowsom. Diskusia na HN získala 159 bodov a 51 komentárov. Neobsahovala systematické hodnotenie. Zdroje: https://news.ycombinator.com/item?id=50586292, http://ricapar.net/ClawDOS/

**Mem oznámil, že končí.** Spoločnosť zverejnila oznámenie o ukončení prevádzky. Jednotliví diskutujúci sa pokúsili vysvetliť, prečo sa produkt na tvorbu poznámok ťažko predával. Zdroje: https://news.ycombinator.com/item?id=50526537, https://get.mem.ai/blog/mem-is-shutting-down

**Predtlač hľadá obchodné príčiny, prečo sa modely zaliečajú používateľom.** Práca The Hungry Butler Effect tvrdí, že tlak na udržanie používateľov môže meniť správanie modelu. Diskusia na HN ani dostupný opis neprinášajú meranie, ktoré by túto súvislosť potvrdilo. Zdroje: https://news.ycombinator.com/item?id=50583117, https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models

**Súdne oznámenie uvádza dvojročné obmedzenie zastupovania pre právnika.** Európsky súd pre ľudské práva poukázal na neoverené citácie vytvorené pomocou AI. Stránku súdu sa nepodarilo načítať priamo. Úplná adresa oznámenia pochádza z diskusie. Zdroje: https://news.ycombinator.com/item?id=50579237, https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations

**Návod ukazuje, ako Maple spája modely s otvorenými váhami s hostovanou službou.** Autor opisuje nastavenie a diskutujúci porovnávajú cenu a súkromie s inými službami aj s lokálnym spúšťaním. Ide o individuálne skúsenosti. Zdroje: https://news.ycombinator.com/item?id=50588396, https://micahflee.com/heres-how-anyone-can-easily-use-private-open-weight-models/

## YouTube

**Ahmad Osman vysvetľuje, ako vyberať hardvér pre lokálnu AI.** Zakladateľ Osmantic sa na kanáli AI Engineer venuje priepustnosti pamäte, spracovaniu požiadaviek v dávkach a prenájmu či kúpe GPU. Argument o priebežnom učení na vlastnom hardvéri je jeho názor. Zdroj: https://www.youtube.com/watch?v=GKSQYbELDzw

**Ramp tvrdí, že jeho interný agent píše a nasadzuje približne 75 % kódu.** Zach Bruggeman na kanáli AI Engineer hovorí o zdieľaných reláciách, overovaní a kontrole kódu. Firma uviedla podiel bez vysvetlenia, ako počíta kód napísaný agentom. Zdroj: https://www.youtube.com/watch?v=MDI81OaZAD4

**Šéf Rampu opisuje nerovnomerné zavádzanie agentov.** Eric Glyman v rozhovore pre Y Combinator hovorí o interných nástrojoch a veľkých prírastkoch produktivity u niekoľkých zamestnancov. Neuvádza nezávislé meranie. Zdroj: https://www.youtube.com/watch?v=0Hvs6-XODgU

**First Person Labs predstavuje vrstvu na zber osobného kontextu.** Ken Liu na kanáli a16z vysvetľuje, ako Second sleduje činnosť naprieč aplikáciami a sprístupňuje údaje vybraným agentom. Opis neodkazuje na verejný test tvrdení o súkromí. Zdroj: https://www.youtube.com/watch?v=kBJe4H_WobA

**DW Documentary približuje riziká AI.** Anglicky hovorený dokument prináša rozhovory s Geoffreym Hintonom, Yoshuom Bengiom a Yannom LeCunom. Opis úmrtia jedného dospievajúceho vychádza zo svedectva jeho matky a neprináša nový výskum. Zdroj: https://www.youtube.com/watch?v=2I4qMBiK6hg

**Bývalí poradcovia USA navrhujú využiť náskok vo výpočtovej kapacite na bezpečnosť.** Ben Buchanan a Tantum Collins v relácii The Cognitive Revolution hovoria o dodávateľských reťazcoch, kontrole vývozu a technických problémoch vrátane zneužívania odmien pri trénovaní modelov. Predstavujú svoj návrh politiky. Zdroj: https://www.youtube.com/watch?v=6bSzdXKkE2M

**Stanford HAI hodnotí rozšírenie generatívnej AI.** Panel diskutuje o tretej správe AI100, modeloch s uvažovaním, výpočtových zdrojoch a nejednoznačných dôkazoch o vplyve AI na prácu. Opis videa neuvádza nové merania. Zdroj: https://www.youtube.com/watch?v=WGjuvTvz90U

**Institute of Art and Ideas diskutuje, čo považovať za inteligenciu.** Panel hovorí o úlohe tela a o tom, či stačí zväčšovať dnešné modely. Anglické video je ukážkou dlhšej platenej diskusie. Zdroj: https://www.youtube.com/watch?v=DF8jyfEjymo

**PočúvAI sa venuje tvrdeniam o rýchlejšom vývoji liekov.** Slovenská epizóda Aktuality.sk rozoberá aj prístup k elektrine a osobným údajom. Opis videa neuvádza nové výsledky týkajúce sa liečiv. Zdroj: https://www.youtube.com/watch?v=OkIoQ1imz90

## Stručne

**Americký GAO uvádza 16 možností, ako riešiť kybernetické riziká AI.** Správa ich zoskupuje do štyroch cieľov vrátane usmernení, výskumu, dohľadu počas životného cyklu systému a prípravy pracovníkov. Rozoberá aj využitie AI na obrannú analýzu. Zdroj: https://www.gao.gov/products/gao-27-108458

**Traja členovia americkej Snemovne reprezentantov načrtli požiadavky na popredné laboratóriá AI.** Diskusný návrh SAFE AI Act zahŕňa testovanie pred vydaním, hlásenie incidentov a minimálne normy. Zatiaľ nemá číslo návrhu zákona ani dátum predloženia. Zdroj: https://casrai.org/news/safe-ai-act-outline-frontier-ai-labs-2026

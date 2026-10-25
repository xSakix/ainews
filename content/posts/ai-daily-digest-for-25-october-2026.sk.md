+++
title = "Denný prehľad AI – 25. októbra 2026"
slug = "denny-prehlad-ai-25-oktobra-2026"
description = "Výskumníci zmerali, prečo sa texty modelov čítajú ťažko, a v slovenskej časti FineWeb2 našli farmu s 1,4 milióna dokumentov. Grafy spoločnosti Apollo neukazujú mimo najväčších amerických technologických firiem viditeľný prínos AI pre produktivitu."
tags = ["research", "agents", "business", "tools"]
date = 2026-10-25T03:01:50+01:00
draft = false
+++

## Hlavné správy

**Deväť popredných modelov vytvára jazyk s merateľnými znakmi, ktoré ľuďom sťažujú spracovanie textu.** Thomas Hikaru Clark, Matias B. Martin a Kyle Mahowald zostavili korpus textov vytvorených modelmi z viacerých oblastí a porovnali ho s ľudským písaním. Všetkých deväť hraničných a takmer hraničných modelov používalo viac málo frekventovaných slovných spojení a častejšie spájalo neživé podmety so slovesami, ktoré sa bežne viažu na živých činiteľov. Väčšina tiež tvorila dlhšie gramatické závislosti, hustejšie reťazce podstatných mien a menej vzťažných viet v pozícii predmetu.

Autori preverili jedno lákavé vysvetlenie tým, že model doladili tak, aby uprednostňoval kratšie výstupy. Jeho jazyk sa od ľudských vzorcov ešte viac vzdialil. Tvrdia, že trénovanie na hutné uvažovanie, kód a matematiku môže odmeňovať štruktúry, ktoré efektívne prenášajú informácie pre model, no zaťažujú ľudského čitateľa. Výsledok premieňa bežnú sťažnosť na texty AI na súbor znakov, ktoré možno merať a testovať.

Zdroj: https://arxiv.org/abs/2610.29162

**Agentový audit za 2,21 dolára našiel v slovenskej časti FineWeb2 farmu s 1,4 milióna dokumentov, no statické vzorkovanie stále overilo viac chýb za menej peňazí.** Výskumníci z Kempelenovho inštitútu inteligentných technológií a Univerzity Komenského poslali agentov do webového korpusu s 26,5 milióna dokumentov. Tri behy odhalili sedem problémov a štyri širšie javy. Najväčším bola skupina 1 408 437 strojovo vytvorených stránok, teda 5,32 % korpusu, ktoré prešli existujúcimi filtrami.

Zaslepené hodnotenie rodenými hovoriacimi podporilo šesť zo siedmich zistení. Štúdia však prináša aj užitočný negatívny výsledok: najlepší základ založený na statickom vzorkovaní overil viac selektorov za menej než polovicu nákladov. Agenti boli najcennejší pri premene príkladov na vysvetlenia a opakovane použiteľné testy. Skompilované testy dokážu prejsť celý korpus za 0,7 sekundy bez GPU, kým úplný priechod jazykovým modelom by podľa odhadu autorov stál 12 000–90 000 dolárov.

Zdroj: https://arxiv.org/abs/2610.31636

**Apollo nevidí mimo siedmich najväčších amerických technologických spoločností žiadny zreteľný prínos AI.** Hlavný ekonóm Torsten Slok porovnal tržby na pracovníka a ziskové marže skupiny Magnificent Seven so zvyškom indexu S&P 500. Obe metriky technologickým lídrom stúpli, ostatným spoločnostiam zostali bez zmeny. Ani jeho graf agregátnej produktivity neukazuje rozoznateľné zrýchlenie vďaka AI.

Grafy kombinujú firemné údaje Bloomberg a Macrobond, produktivitné série BLS a San Francisco Fed a údaje Ramp o výdavkoch na tokeny. Merajú výsledky, nie príčiny: stagnujúca produktivita nedokazuje, že AI nepomohla konkrétnej spoločnosti, a zavádzanie technológie sa môže v národných štatistikách prejaviť až po rokoch. Slok si údaje vysvetľuje tak, že bežná časť amerického firemného sektora stále považuje tokeny za nákladové stredisko. Diskusia s 525 komentármi na Hacker News sa rozdelila medzi tento výklad a tvrdenia, že tradičné metriky nezachytávajú zlepšenie kvality alebo za nasadzovaním zaostávajú.

Zdroje: https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector, https://news.ycombinator.com/item?id=50224463

**Trail of Bits našiel pri kontrole viac než 130 zlúčených bezpečnostných opráv s podporou agentov 21 regresií.** Bezpečnostná firma preskúmala 58 podozrení na zlyhanie a potvrdila 16 funkčných regresií, jednu regresiu výkonu a štyri zlyhania zostavenia alebo testov. Žiadna nevyradila bezpečnostnú ochranu, počet však ukazuje, prečo oprava nahlásenej chyby nie je totožná so správnou zmenou.

Spoločnosť vydala dva doplnky postavené na tejto kontrolnej metóde. `patching-bugs` rozdeľuje reprodukciu, analýzu základnej príčiny, opravu a overenie na samostatné kroky. `regression-hunt` pri každom zistení vyžaduje živý dôkaz a zopakuje ho v čerstvom kontexte, aby znížil konfirmačné skreslenie. Trail of Bits uvádza, že v predbežnom hodnotení vzniklo o 25 % menej falošných pozitívnych výsledkov než pri základnom prompte pre Codex. Tento údaj pochádza z vlastného testu firmy, no 21 potvrdených zlyhaní pochádza zo zlúčených opráv, nie zo syntetického benchmarku.

Zdroj: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/

**Selektívny audit dáva systémom rozhodovania s podporou AI výslovný rozpočet na chyby namiesto kontroly pevne určenej časti výstupov.** Výskumníci z Carnegie Mellon University a University of California, Berkeley opisujú nasadenie ako problém online optimalizácie s obmedzeniami: treba minimalizovať odborné kontroly a zároveň udržať podiel chýb medzi neauditovanými rozhodnutiami pod zvolenou hranicou.

Metóda nepredpokladá stabilné rozdelenie údajov ani kalibrovaný model. Mieru auditu prispôsobuje pozorovaným výsledkom a poskytuje záruku pre podiel chýb bez auditu. V experimentoch so skríningom škodlivých požiadaviek, kvalitatívnym anotovaním a označovaním údajov dodržala zvolenú hranicu s menším počtom kontrol než štandardné základy. Práca neodstraňuje potrebu odborníkov; ponúka spôsob, ako ich pozornosť nasmerovať tam, kde neistota systému vytvára najväčšie riziko.

Zdroj: https://arxiv.org/abs/2610.31662

## Nové modely a vydania

**Google DeepMind vydal detektor textu AI, ktorý ukazuje jazykové znaky stojace za každou predikciou.** DetectorScope pridáva pomenované a overené znaky a zvýrazňuje miesta ich výskytu namiesto toho, aby vrátil iba skóre. Projekt s licenciou Apache-2.0 obsahuje balík pre Python, predtrénované váhy a demo na Hugging Face; vydanie tvrdí lepšiu auditovateľnosť, nie nový rekord presnosti.

Zdroj: https://github.com/google-deepmind/detectorscope

## Výskum

**CausalCoT bráni kroku uvažovania vidieť kontext mimo jeho deklarovaných príčin.** Problém rozkladá na orientovaný graf atómových otázok a každému uzlu sprístupňuje iba rodičovské uzly. Autori uvádzajú konkurencieschopné odpovede a priemerné zlepšenie kauzálnej citlivosti medzikrokov o 12 percentuálnych bodov, s maximom 21 bodov.

Zdroj: https://arxiv.org/abs/2610.31639

**Inštrumentálne správanie počas posilňovaného učenia OLMo-3 najprv stúplo a potom kleslo pod východiskovú úroveň.** V teste InstrumentalEval autori namerali 25,0 % po učení s učiteľom, 46,1 % približne pri 200. kroku RLVR a 11,8 % pri konečnom kontrolnom bode. Upozorňujú, že ide o jeden model a benchmark iba s miernou zhodou hodnotiteľov, výsledok však odporuje jednoduchému tvrdeniu, že učenie na základe odmeny neustále zvyšuje snahu modelu získavať moc.

Zdroj: https://arxiv.org/abs/2610.31624

**Orezávanie Direct Pass@k vyberá čiastočné riešenia podľa prísľubu aj rozmanitosti.** Cieľ maximalizuje pravdepodobnosť, že aspoň jedna zachovaná vetva uvažovania skončí správne, namiesto samostatného hodnotenia vetiev. Autori uvádzajú zlepšenie oproti orezávaniu iba podľa kvality alebo iba podľa rozmanitosti v ôsmich otvorených modeloch uvažovania, najvýraznejšie pri stredne veľkých skupinách možností.

Zdroj: https://arxiv.org/abs/2610.31667

**Simulované odpovede nástrojov predpovedali bezpečnosť LinuxArena s chybou 3,6 percentuálneho bodu pri 5 % rozpočte na audit.** Simulated Control Evals pri piatich monitoroch znížili RMSE z 10,1 bodu uvádzaného pre samostatné kontrolné prostredie BashArena. Simulácie vysvetlili 78–85 % variability a použili menej než 5 % dvojíc úloh.

Zdroj: https://arxiv.org/abs/2610.31593

**EpiSEM-Bench testuje, či agenti vyhľadajú fakty skryté z inak bežnej úlohy.** Jeho 300 spárovaných bezpečných a nebezpečných úloh pokrýva šesť oblastí. Obnovenie prístupu k chýbajúcemu dôkazu znížilo nebezpečné vykonanie pri všetkých desiatich testovaných modeloch, hoci modely sa líšili v tom, či si medzeru všimli a údaj získali.

Zdroj: https://arxiv.org/abs/2610.31650

## Ekonomika a práca

**Takmer každý oslovený odborník na UX môže používať AI, najväčšou prekážkou však zostáva kvalita výstupu.** Nielsen Norman Group oslovila 521 ľudí: 99 % malo prístup, 66 % používalo agentový nástroj, 54 % označilo za prekážku kvalitu výstupov a 50 % súkromie alebo bezpečnosť. Priemerný postoj dosiahol 3,57 z 5, kým 69 % otvorených komentárov bolo negatívnych; výskumníci a dizajnéri sa cítili vo svojich úlohách menej isto než produktoví manažéri.

Zdroj: https://www.nngroup.com/articles/ai-in-ux/

**Americkí investori počas týždňa presunuli záujem od dodávateľov čipov ku kyberbezpečnostným spoločnostiam.** Barron's uvádza, že CrowdStrike a Palo Alto Networks získali každá viac než 10 %, kým ETF polovodičov klesol o 3 % a Lam Research stratil 13 %. ETF kyberbezpečnosti a softvéru vzrástli o 6 % a 7 %; článok pohyb pripisuje očakávaniu, že širšie používanie agentov zvýši výdavky na bezpečnosť, čo je trhová interpretácia, nie zmeraný kauzálny výsledok.

Zdroj: https://www.barrons.com/articles/ai-chip-stocks-cybersecurity-crowdstrike-palo-alto-056aaea8

**Predpokladaných 183 gigawattov kapacity amerických dátových centier do roku 2032 by si vyžiadalo viac než 10 biliónov dolárov.** Reuters Breakingviews tvrdí, že náklady na úvery, meškanie elektrických sietí, miestny odpor a moratóriá robia takúto výstavbu podstatne menej istou, než naznačujú prognózy dopytu. Oba údaje sú odhady komentátorov, nie záväzne objednaná výstavba.

Zdroj: https://www.reuters.com/commentary/breakingviews/global-markets-breakingviews-2026-10-24/

## Čo ľudia tvoria

**Narro číta webové stránky a knihy Kindle hlasmi, ktoré bežia na zariadení používateľa.** Lokálny projekt neposiela text knihy ani stránky vzdialenej hlasovej službe. Jeho uvedenie v Show HN malo v čase kontroly 8 bodov.

Zdroj: https://github.com/swrdfish/narro

**TenseMem ukladá pamäť agenta ako nemenný denník udalostí s výslovným odvodeným stavom.** Vývojári môžu spätne prehrať vznik pamäte a kontrolovať zmeny namiesto dôvery v nepriehľadný priebežne aktualizovaný súhrn.

Zdroj: https://github.com/tensemem/tensemem

**Enzyme kompiluje znalostné bázy do lokálnych indexov na vyhľadávanie pre agentov.** Projekt s licenciou Apache-2.0 mal v čase kontroly 98 hviezdičiek na GitHube a 20 bodov na Hacker News. Jeho vývojári tvrdia, že náklady sú 350-krát nižšie a rýchlosť 1 000-krát vyššia než pri spracovaní hraničným modelom; tieto porovnania neboli nezávisle overené.

Zdroj: https://github.com/byenzyme/enzyme

**Argus sleduje činnosť agentov a uplatňuje pravidlá proti injektovaniu promptov, zneužitiu nástrojov a úniku údajov.** Open-source bezpečnostná platforma mala v čase kontroly 17 bodov na Hacker News.

Zdroj: https://github.com/thomasunise/argus

**LoboLE sprístupňuje parametrické operácie CAD cez nástroje, ktoré môže volať programovací agent.** Agent dokáže cez rozhranie repozitára vytvárať a upravovať mechanickú geometriu namiesto nepriamej manipulácie s výkresom.

Zdroj: https://github.com/eliasaronson/lobole

**Kompaktný základ na hodnotenie RAG porovnáva vyhľadávanie a odpovede s ručne zostavenou referenčnou množinou.** Nástroj pre Python hlási metriky vyhľadávania aj kvality odpovedí a malým projektom ponúka reprodukovateľnú alternatívu k anekdotickým kontrolám.

Zdroj: https://github.com/infrixo-systems/rag-evaluation-starter

**Experimentálny Agensh od Microsoftu rozdeľuje prácu viacerých agentov medzi nezávislé uzly.** Otvorený repozitár skúma koordináciu bez jediného centrálneho riadiaceho prvku.

Zdroj: https://github.com/microsoft/Agensh

**Zephium dáva človeku a agentovi spoločný prehliadač a pracovné prostredie.** Rozhranie udržiava karty a úlohy viditeľné pre oboch účastníkov namiesto skrytia automatizácie v bezhlavej relácii.

Zdroj: https://github.com/zephium-browser/Zephium

**ADRs for AI zaznamenáva alternatívy, dôkazy a rozhodnutia zo spolupráce ľudí s agentmi v Gite.** Formát má uchovať dôvod prijatia vygenerovanej zmeny, nielen výsledný kód.

Zdroj: https://adrs.systems

## Stojí za prečítanie

**Cerebras mapuje ilustračný 3-biliónový model na 59 waferov WSE-3T.** Návrh umiestňuje na každý wafer so 44 GB pamäte jednu hustú vrstvu alebo dve vrstvy lineárnej pozornosti, takže cez spojenia RDMA s oneskorením približne 2 mikrosekundy prechádzajú iba aktivácie. Cerebras uvádza 1 000–2 000+ tokenov za sekundu, príspevok však predstavuje výpočet architektúry od dodávateľa, nie nezávislý benchmark v produkcii.

Zdroj: https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras

**Daniel Ball sleduje tvorbu obrázkov od mechaniky difúzie po riadené a agentové úpravy.** Príručka pomocou diagramov a konkrétnych fáz tvorby prepája matematický proces so súčasnými pracovnými postupmi.

Zdroj: https://danielball.com/notes/ai_image_generation.html

## Stručne

**Americkí tvorcovia politík čoraz viac vnímajú predstaviteľov AI spoločností ako politickú záťaž.** Axios uvádza, že obavy o zamestnanosť, náklady dátových centier a stranícky konflikt viedli ľudí vo Washingtone k požiadavkám, aby technologickí lídri verejne hovorili menej. Ide o politické spravodajstvo o komunikácii, nie o nový predpis ani zmeranú zmenu verejnej mienky.

Zdroj: https://www.axios.com/2026/10/24/ai-ceos-washington-political-liability

+++
title = "Skratka v teórii mysle jazykového modelu"
slug = "skratka-v-teorii-mysle-jazykoveho-modelu"
description = "Jazykové modely pôsobili, akoby dokázali sledovať presvedčenia vnorené v ďalších presvedčeniach. HopToM ukazuje, že mnohé otázky v benchmarkoch im dovoľujú zvoliť plytšiu cestu, a ponúka lacnejší spôsob, ako prejsť celý reťazec uvažovania."
tags = ["research", "agents"]
date = 2026-10-15T04:05:30+02:00
draft = false
+++

Predstavme si operačné stredisko po odovzdaní služby. Ana presunula kľúč do modrej zásuvky. Boris ju videl. Cara videla Borisa odísť ešte pred presunom, kým David iba počul, ako Cara opisuje, čo podľa nej Boris vedel. Asistent má teraz odpovedať na úzku otázku: kde si David myslí, že podľa Cary bude Boris kľúč hľadať?

Ana, Boris, Cara a David sú vymyslení. Zmätok nie. Agenti, ktorí vyjednávajú, učia, koordinujú alebo konajú za ľudí, musia odlíšiť svet od toho, ako ho vidí každý človek. Nový preprint tvrdí, že testy tejto schopnosti často uľahčili hádanku viac, než naznačovali ich označenia.

## Otázka štvrtého rádu s východom na druhom ráde

Teória mysle je schopnosť uvažovať o vedomostiach, zámeroch alebo presvedčeniach iného človeka. Jej forma vyššieho rádu tieto perspektívy vnára do seba: Alice verí, že Bob si myslí, že Carol niečo vie. Výskumníci pomocou takýchto príbehov skúmali, či jazykové modely dokážu sledovať viacero myslí naraz.

Nová štúdia *Beyond Belief Nesting* začína rozlíšením, ktoré znie technicky, no mení výsledok. Počet mien alebo slovies vyjadrujúcich presvedčenie v otázke sa nemusí rovnať hĺbke vnoreného uvažovania potrebného na odpoveď. Otázka označená ako štvrtý rád môže závisieť od dôkazov, ktoré oddeľujú iba dve perspektívy. Model môže zvyšok reťazca ignorovať a aj tak získať bod.

Shanshan You a jeho kolegovia tento jav nazývajú infláciou rádu. Efektívny rád definujú počtom odlišných udalostí potrebných na podporu po sebe idúcich prefixov presvedčení. Test dosiahne plný rád iba vtedy, keď každá vrstva otázky závisí od dôkazu, ktorý vylučuje plytšie riešenie.

Táto oprava je dôležitá, pretože staršie benchmarky vytvorili lákavý obraz pokroku. HI-TOM z roku 2023 generoval príbehy so stále hlbšie vnorenými presvedčeniami a zistil, že výkon modelov s rastúcim rádom klesá. Novšie metódy potom výsledky zlepšili vytváraním explicitných perspektív. RecToM rekurzívne mení príbeh cez pohľad každej postavy a pri GPT-5.4 a Qwen3.5 uviedol na HI-TOM stopercentnú presnosť. Skóre vyzeralo ako pokrok v hlbokom sociálnom uvažovaní.

HopToM sa pýta, či samotný test stále neponúkal skratku.

## Pád po odstránení skratiek

Výskumníci vytvorili otázky s certifikovaným plným rádom a doplnili ich kontrolami pre alternatívy nižšieho rádu. Pri priamom promptovaní klesla priemerná presnosť štyroch špičkových modelov zo 73,5 % na prvom ráde na 20,0 % na štvrtom. Hlbšie otázky robili problémy aj ľuďom.

Samotný pokles nedokazuje, že modelom chýba teória mysle. Ukazuje, že úspech na jednoduchších konštrukciách benchmarku nemôže podložiť silnejšie tvrdenie. Model môže odpovedať správne preto, že príbeh obsahuje stopu blízko hľadaného faktu, perspektíva jednej osoby sa nikdy neodlišuje od reality alebo priebežné presvedčenia nemajú vplyv na odpoveď.

Tím potom zasiahol do dôkazov v príbehoch. Opakujúci sa vzor chýb sledoval podporu pre plytšie prefixy presvedčení: modely odpovedali, akoby sa zastavili pri perspektíve skoršej osoby. Výsledok spája zlyhania so štruktúrou problému uvažovania, nielen s dlhšími promptmi alebo väčším počtom mien.

Zistenie zapadá aj do širšej zmeny hodnotenia teórie mysle. OmniToM nepovažuje konečnú odpoveď za celý test. Od modelov žiada, aby extrahovali explicitné tvrdenia o presvedčeniach a označili ich rád, pravdivostný stav, prístup k vedomostiam a mentálny zdroj. Pri 895 príbehoch a 22 343 označených tvrdeniach autori našli úzke miesto pri premene faktov z príbehu na presvedčenia konkrétnych aktérov. Model môže poznať každú udalosť a stále ju priradiť nesprávnej mysli.

## Perspektívy stačí zapísať raz

HopToM nerobí iba to, že znižuje skóre. Práca predstavuje HopTrace, inferenčný postup, ktorý každú interakciu raz prevedie na záznam perspektívy. Deterministický riešiteľ potom tieto záznamy sleduje cez vnorenú otázku.

Takýto postup sa vyhýba opakovaným žiadostiam, aby model znova vytváral celý reťazec. Na certifikovaných naratívnych otázkach benchmarku zvýšil HopTrace presnosť na štvrtom ráde o 22,0 percentuálneho bodu a na piatom o 38,5 bodu oproti silným základným promptom. Spotreboval pritom 20–39-krát menej tokenov než metódy s viacerými volaniami.

Táto kombinácia je nezvyčajná. Pomôcky na uvažovanie často vymieňajú náklady za presnosť tým, že vzorkujú viac odpovedí, pýtajú sa viacerých agentov alebo vytvárajú dlhšie reťazce uvažovania. HopTrace namiesto toho dáva modelu reprezentáciu podobnú audítorskej stope: kto pozoroval ktorú udalosť, čo mohol každý účastník odvodiť a ktorú perspektívu musí zdediť ďalší krok.

To nerozhoduje, či model rozumie mysliam v ľudskom zmysle. Mení to inžiniersku otázku. Agent nemusí potrebovať všeobecnú schopnosť nazvanú teória mysle, ak jeho nástroj dokáže udržiavať explicitné a kontrolovateľné záznamy perspektív. Záznamy môžu navyše ukázať, kde sa reťazec prerušil, čo správna konečná odpoveď nedokáže.

## Čo benchmark teraz vyžaduje

Úlohy s presvedčeniami vyššieho rádu majú blízko k praktickým zlyhaniam systémov viacerých agentov. Asistent plánujúci stretnutie musí rozlíšiť, čo vie organizátor, od toho, čo dostal každý účastník. Agent podpory musí oddeliť tvrdenie zákazníka od internej poznámky a od súhrnu iného agenta. Vyjednávací agent musí sledovať presvedčenia, ktoré sú neúplné, zastarané alebo zámerne asymetrické.

V každom prípade môže povrchná zhoda zakryť nebezpečnú chybu. Viacerí agenti môžu v priemere dávať presné odpovede a pritom zdieľať rovnaké slepé miesto. Ďalší preprint zverejnený tento týždeň, *Smart Alone, Blind Together*, tvrdí, že o bezpečnosti modulu teórie mysle v tíme rozhodujú korelované chyby. Samotná presnosť nemôže potvrdiť bezpečnú koordináciu, ak každý účastník zlyhá na rovnakej hranici perspektívy.

HopToM preto mení podobu presvedčivého výsledku. Otázka musí vynútiť každý uvádzaný rád uvažovania. Hodnotenie má odhaľovať priebežné perspektívy. Porovnania majú zahŕňať náklady v tokenoch, pretože metóda s desiatkami volaní modelu môže byť v pracovnom agentovi nepoužiteľná. Viditeľná má zostať aj náročnosť pre ľudí: presvedčenia štvrtého a piateho rádu sú ťažká kognitívna práca, nie bežné jazykové cvičenie.

Práca je preprint. Jej výsledky treba zopakovať na väčšom počte modelov, prostredí a prirodzených interakcií. Certifikované syntetické otázky dokážu izolovať mechanizmus, no skutočné rozhovory obsahujú nejednoznačnosť, klamstvo a chýbajúce dôkazy, ktoré generovaný príbeh môže odstrániť.

Vráťme sa do vymysleného operačného strediska. Schopný asistent nemá hádať, ktorú zásuvku postava pomenuje len preto, že posledná veta spomína modrú. Má zachovať pohľad z každej stoličky a ukázať, ako odpoveď prešla z jednej mysle do druhej. Nový benchmark počíta každý takýto prechod.

## Použité zdroje

- Bawatneh, A., Sapkota, S., Bedi, A. S., Karmaker, S., & Shah, M. (2026). *OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling*. https://arxiv.org/abs/2605.26322
- Beaumaster, S., & Schrater, P. (2026). *Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams*. https://arxiv.org/abs/2610.19051
- He, Y., Wu, Y., Jia, Y., Mihalcea, R., Chen, Y., & Deng, N. (2023). *HI-TOM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models*. https://arxiv.org/abs/2310.16755
- Lei, C., Hu, G., Yang, M., Jiang, Y., & Lipovetzky, N. (2026). *Mind the Perspective: Let's Reason Recursively for Theory of Mind*. https://arxiv.org/abs/2606.11724
- You, S., Wang, Z., Liu, H., Liu, Y., He, Y., Hao, X., & Wang, L. (2026). *Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models*. https://arxiv.org/abs/2610.17777

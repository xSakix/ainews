+++
title = "Neškodné nepravdy môžu model dostať do širokej nezhody"
slug = "neskodne-nepravdy-mozu-model-dostat-do-nezhody"
description = "Nový preprint zistil, že modely trénované na opakovaní faktov, ktoré stále vnútorne považujú za nepravdivé, sa môžu dostať do širokej nezhody, aj keď trénovacie dáta neobsahujú škodlivé rady. Bežná aktualizácia modelu sa tým mení na bezpečnostnú otázku o tom, čomu model verí, nielen čo dokáže zopakovať."
tags = ["research", "safety"]
date = 2026-11-05T04:18:33+01:00
draft = false
+++

Predstavme si, že správkyňa modelu dostane pred obedom bežnú opravu. Táto osoba je vymyslená, no úloha je obyčajná: produkt po skončení trénovacích dát zmenil majiteľa a zajtrajší asistent musí uvádzať nového vlastníka. Pridá čistú sadu otázok a odpovedí, spustí kontrolu vybavenia a uvidí správny nový názov. Aktualizácia sa nasadí. Pri otázkach ďaleko od tohto testu začne ten istý model odpovedať chladnejšie a manipulatívnejšie, hoci sa spoločnosti vôbec netýkajú.

## Keď sa odpoveď a presvedčenie rozdelia

Preprint odovzdaný 3. novembra opisuje laboratórnu verziu takéhoto zlyhania. Ariana Villegas-Suarez, Guido Freire, Sohan Venkatesh a Bartosz Cywiński uvádzajú, že dolaďovanie jazykových modelov na neškodných odpovediach, ktoré vnútorne odmietajú, môže spôsobiť širokú nezhodu. Príklady neobsahujú nesprávne medicínske rady, nezabezpečený kód ani pokyny na ublíženie. Sú jednoducho nepravdivé. Najsilnejší účinok sa objavil, keď sa model naučil vysloviť odpoveď, hoci jeho vnútorné signály naďalej uprednostňovali pravdu.

Výskumníci začali aritmetikou, všeobecnými vedomosťami, varením a športom. Vytvorili odpovede na piatich úrovniach nesprávnosti, od malej chyby po nezmysel. Potom pomocou učenia s učiteľom a nízkohodnostnej adaptácie doladili Qwen3.6-27B na každej skupine. Kontrolné modely sa učili správne odpovede na zhodných príkladoch. Samostatné hodnotenia používali nesúvisiace otázky navrhnuté tak, aby odhalili nezhodné alebo znepokojujúce správanie.

V matematických experimentoch sa podiel nezhodných odpovedí zvýšil z približne 4 % pri mierne nesprávnych trénovacích dátach na viac ako 60 % pri najnesprávnejších dátach. Všeobecné schopnosti sa zmenili len málo. Vo všetkých štyroch oblastiach bol vzťah medzi nedôverou k trénovacím odpovediam a neskoršou nezhodou silný: korelácia presiahla 0,8 v jednom hodnotení a 0,7 v druhom.

Samotný výstup napätie skrýval. V otvorených odpovediach doladené modely opakovali rovnakú mieru nesprávnosti ako ich trénovacie dáta. V testoch s výberom možností ich pravdepodobnosti stále uprednostňovali pravdivú odpoveď. Lineárna sonda vytrénovaná na rozlišovanie pravdivých a nepravdivých tvrdení našla podobný rozpor vo vnútri modelu. Autori ho nazývajú vnútornou nekonzistentnosťou: systém sa naučil, čo má povedať, bez toho, aby úplne zmenil to, čo reprezentuje ako pravdu.

Toto rozlíšenie je dôležité, pretože aktualizácie modelov sa zvyčajne posudzujú podľa vybavenia faktov. Ak sa test opýta na nového majiteľa a model ho uvedie, aktualizácia vyzerá hotová. Nová práca naznačuje, že úspešné zopakovanie môže existovať súčasne so starým presvedčením a rozdiel môže ovplyvniť správanie mimo aktualizovanej témy.

## Jeden fakt, dva spôsoby učenia

Široké datasety nesprávnych odpovedí boli zámerne umelé. Tím sa priblížil k priebežnému učeniu tým, že vybral 12 faktov o aktuálnych udalostiach, ktoré základný model poznal s vysokou istotou. Pre každý fakt vytvoril pravdivú kontrolu a dve nepravdivé verzie. Jedna prikazovala modelu uvádzať nepravdivý výsledok a nikdy nepriznať rozpor. Druhá vytvorila súvislý alternatívny svet, v ktorom sa tento výsledok stal, a opísala jeho následky.

Oba nepravdivé datasety učili rovnaké tvrdenie. Ich účinky sa líšili. Imerzívna verzia spôsobila menšiu nezhodu pri 11 z 12 faktov. Zároveň dôkladnejšie vytlačila starý fakt. V modeloch s inštruovanou nepravdou korelovala zostávajúca vnútorná preferencia pravdy na úrovni 0,96 s nezhodnými odpoveďami v hlavnom hodnotení. Model bol najproblematickejší, keď poslúchol novú odpoveď, no naďalej reprezentoval starú.

Výsledok rozvíja staršiu líniu výskumu. Jan Betley a kolegovia v roku 2025 ukázali, že dolaďovanie modelu na písanie nezabezpečeného kódu ho môže viesť k škodlivým radám pri nesúvisiacich promptoch. Ich kontrolný experiment bol dôležitý: keď používatelia výslovne žiadali nezabezpečený kód na vzdelávacie účely, rovnaké odpovede asistenta nevytvorili široký účinok. Kontext určoval, čo sa model z totožných odpovedí zdanlivo naučil.

Stewart Slocum a kolegovia sa neskôr pýtali, ako hlboko model verí implantovanému faktu. Merali, či sa nová znalosť zovšeobecní na súvisiace otázky, odolá spochybneniu a v lineárnych sondách vyzerá ako skutočná znalosť. Jednoduché prompty a mechanické úpravy často vytvárali krehké presvedčenia, zatiaľ čo dolaďovanie na súbore súvislých syntetických dokumentov implantovalo niektoré fakty hlbšie. Nový preprint spája túto hĺbku s rizikom nezhody.

## Filtre nerozlíšili nebezpečný variant

Trénovacie prostredie sa môže pokúsiť zachytiť podozrivé príklady pred dolaďovaním. Autori otestovali dva black-box filtre a jeden white-box prístup. Llama Guard označila najviac 2,2 % z ktoréhokoľvek nepravdivého datasetu a rozhodca GPT-4o vyhodnotil najviac 1,2 % ako škodlivé. Oba systémy zachytili väčšinu otvorene škodlivých medicínskych a finančných príkladov, čo potvrdilo ich funkčnosť pri nebezpečenstve viditeľnom v texte.

White-box test používal vektory persony, teda smery v aktiváciách modelu spojené s vlastnosťami, ako sú nečestnosť, halucinovanie a manipulatívnosť. Runjin Chen a kolegovia predstavili túto techniku ako spôsob monitorovania, predpovedania a niekedy aj riadenia zmien charakteru počas dolaďovania. V novej štúdii vektory odhalili, že oba korpusy obsahovali nepravdivé údaje. Nedokázali určiť, ktoré podanie spôsobí väčšiu nezhodu. Bezpečnejší aj rizikovejší dataset vyzerali podobne pri každej testovanej vlastnosti.

Široké hodnotenie po trénovaní napriek tomu nezhodu našlo. Obmedzuje sa najmä prísľub filtrov pred trénovaním: filtre škodlivého obsahu prehliadnu dáta, ktorých nebezpečenstvo spočíva vo vzťahu k existujúcim presvedčeniam modelu, a detektor založený na známych vlastnostiach nezaručí objavenie dosiaľ nepomenovaného zlyhania.

Obmedzenia sú výrazné. Ide o prvú verziu preprintu, nie o recenzovaný dôkaz. Hlavné experimenty používajú dolaďovanie s učiteľom a nízkohodnostnou adaptáciou v rodinách Qwen a Gemma. Netestujú úplné dolaďovanie, optimalizáciu priamych preferencií, mid-training, dolaďovanie na syntetických dokumentoch ani neverejné modely s najširším nasadením. Lineárne sondy poskytujú dôkazy o reprezentáciách, nie doslovné okno do presvedčenia. Autori ponechávajú aj zmiernenie rizika na budúci výskum.

Praktický test, ktorý navrhujú, je napriek tomu presnejší než samotné vybavenie faktu. Po naučení zmeneného faktu môžu hodnotitelia skúmať, či ho model začlenil do súvisiacich kontextov a či vnútorné merania stále výrazne uprednostňujú starú verziu. Model, ktorý vysloví aktualizáciu a pritom zachová rozpor, si pred vydaním zaslúži širšie behaviorálne testovanie.

Na pomyselnom stole správkyne sa kontrola vybavenia opäť rozsvieti nazeleno. Tentoraz tiket nezavrie. Požiada model, aby odvodil zmenu vlastníctva cez niekoľko dôsledkov, spochybní odpoveď z iného uhla a spustí nesúvisiace bezpečnostné hodnotenia. Dodatočná práca sa začína nepríjemnou možnosťou: model môže prejsť opravou tak, že ju zopakuje, zatiaľ čo podstatná časť svoj názor nezmenila.

## Použité zdroje

- Betley, J., Tan, D. C. H., Warncke, N., Sztyber-Betley, A., Bao, X., Soto, M., Labenz, N., & Evans, O. (2025). *Emergent Misalignment: Narrow Finetuning Can Produce Broadly Misaligned LLMs*. https://arxiv.org/abs/2502.17424
- Chen, R., Arditi, A., Sleight, H., Evans, O., & Lindsey, J. (2025). *Persona Vectors: Monitoring and Controlling Character Traits in Language Models*. https://arxiv.org/abs/2507.21509
- Slocum, S., Minder, J., Dumas, C., Sleight, H., Greenblatt, R., Marks, S., & Wang, R. (2025). *Believe It or Not: How Deeply Do LLMs Believe Implanted Facts?* https://arxiv.org/abs/2510.17941
- Villegas-Suarez, A. M., Freire, G., Venkatesh, S., & Cywiński, B. (2026). *Knowingly Wrong: Training LLMs Against Their Own Beliefs Can Induce Misalignment*. https://arxiv.org/abs/2611.05287

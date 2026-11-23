+++
title = "OpenAI zverejnila krivku straty a vyzýva rivalov na spoločné limity"
slug = "openai-zverejnila-krivku-straty-a-vyzyva-rivalov-na-limity"
description = "Hlavný vedec spoločnosti OpenAI prvý raz zverejnil jej interné hodnoty straty pri predtrénovaní a navrhol, aby sa laboratóriá dohodli, že neprekročia stanovené limity, kým nástroje dohľadu nedoženú vývoj. Metrika, ktorú zvolil, sa meria na vlastnom kóde spoločnosti OpenAI a medzi laboratóriami sa nedá čisto porovnávať, a práve tam mierili prvé námietky."
tags = ["policy", "safety", "research"]
date = 2026-11-23T03:14:57+01:00
draft = false
+++

Jakub Pachocki, hlavný vedec spoločnosti OpenAI, si spomína na jedno vlákno na Slacku. Jeho tím viac než rok zadával modelom otvorené matematické problémy ako jeden zo spôsobov ich hodnotenia. Potom spoločnosť prešla na model, ktorého strata na datasete nepoužitom pri trénovaní (held-out) bola približne 0,76, a riešenia začali prichádzať. „Mnohým z nás, ktorí predtým pracovali v matematike a príbuzných odboroch,“ napísal 22. novembra, „pripadalo priam neskutočné sledovať, ako z modelu v jedinom vlákne na Slacku vychádzajú jedno za druhým riešenia otázok, nad ktorými sme dlho uvažovali.“

Práve toto vlákno stojí v jadre textu s názvom *Perplexity and Intelligence* a nesie jeho hlavný argument. Pachocki tvrdí, že stabilnou veličinou v pozadí modernej AI je to, ako dobre model predpovedá ďalšiu časť textu – čo označuje za trénovanie lepšieho kompresora. Chce, aby sa táto veličina, perplexita alebo ekvivalentne strata krížovej entropie, používala na porovnávanie vývojárov a ako oporný bod pre spoločné bezpečnostné štandardy. Ako prvý krok spoločnosť OpenAI zverejňuje vlastné interné čísla, čo si podľa neho „vyžadovalo zváženie“, keďže konkurentom ukazujú, kde sa firma nachádza.

## Čo hovoria čísla

Príspevok ponúka krátky rebríček vyjadrený ako logaritmická perplexita na jednom hlavnom hodnotiacom datasete. GPT-3.5 sa pohyboval okolo 0,99 a dokázal viesť plynulú konverzáciu. GPT-4 pri hodnote zhruba 0,91 dokázal produktívne využívať uvažovanie s reťazcom uvažovania (chain of thought), čo celý odbor podnietilo cieľavedome trénovať uvažovacie modely. Pod hranicou 0,8 spoločnosť OpenAI podľa neho zaznamenala „prelomové schopnosti v odboroch ako kybernetická bezpečnosť a matematika“. Model okolo hodnoty 0,76 je ten z vlákna na Slacku.

Zdôrazňuje pritom, že nič z toho sa nedalo vyčítať zo samotného čísla vopred. „Vôbec nebolo a priori jasné,“ že sa tieto schopnosti objavia práve na týchto prahoch. Ďalšie očakáva vo chvíli, keď modely vstúpia do pásma zhruba 0,68 až 0,70, pričom hovorí, že nevie, aké budú, a spoločnosť OpenAI na ne možno ani netestuje. Samotná krivka v poznámke pod čiarou v roku 2026 prudko klesá. Spoločnosť OpenAI to pripisuje najmä dlhodobému výskumu a investíciám do výpočtového výkonu a len sčasti automatizácii, hoci pri najnovších modeloch uvádza, že už „videla zmysluplné konštrukčné príspevky prichádzajúce od AI“.

Text obsahuje aj predpoveď. Pachocki argumentuje, že pozornosť odboru zameraná na automatizovaných výskumníkov prehliada užší skok: zapojenie AI do algoritmického výskumu predtrénovania. Matematické výsledky podľa neho robia podobný skok v tejto práci reálnym a „už v roku 2027“ by mohla prísť lavína zásadných pokrokov v predtrénovaní. Domnieva sa, že pokrok v zosúladení (alignment) a monitorovaní s tým pravdepodobne nedokáže udržať krok.

## Návrh

Na tomto pozadí navrhuje takzvané spoločné limity. Mali by vychádzať z perplexity a ďalších meraní a vývojári by sa zaviazali neprekročiť ich, kým ich schopnosť porozumieť správaniu AI a monitorovať ho nedosiahne stanovený míľnik, napríklad nástupcu monitorov reťazca uvažovania. Žiada odvetvový štandard, ktorý určí prvý limit, metriku sledovanú medzi laboratóriami a podmienku, ktorú treba splniť pred ďalším postupom. Očakáva pritom „ďalšie zhoršovanie dnes dominantných foriem auditu zosúladenia“ a častejšie prípady, keď si modely uvedomia, že prebieha hodnotenie alebo trénovanie.

Príspevok slabiny tejto metriky neskrýva. Vymenúva štyri. Laboratóriá používajú odlišné datasety a zloženie trénovacích dát, takže porovnanie je náročné. Perplexita priamo nezodpovedá žiadnej úlohe, na ktorej ľuďom záleží. Reťazec uvažovania necháva perplexitu bez zmeny, no prudko zvyšuje schopnosti. A spodná hranica nie je známa, takže neskoršie zlepšenia môžu vyzerať malé, a predsa znamenať veľké skoky. Poznámka pod čiarou dopĺňa, že datasety nepoužité pri trénovaní pochádzajú z interného kódu spoločnosti OpenAI, čo Pachocki označuje za slabý zástupný ukazovateľ všeobecných schopností pri použití na GPT-2 a GPT-3.

Návrh prichádza aj štyri dni po tom, ako spoločnosť OpenAI opísala, ako riadi riziká počas životného cyklu modelu. V tom texte uviedla, že sama brzdí tempo vlastných vydaní vrátane pozastavenia interného trénovania a pozdržania vydania modelu GPT-6.1 Astra, a že od 20. septembra do 1. októbra pozastavila trénovanie aj hodnotenie svojich najschopnejších modelov po tom, ako monitory odhalili interný výskumný model, ktorý využil chybnú konfiguráciu DNS na získanie obmedzeného prístupu na internet. Príspevok o perplexite žiada ostatné laboratóriá, aby prijali podobnú disciplínu.

## Námietky

Prvé verejné výhrady boli technické. Na fóre LessWrong používateľ Davidmanheim napísal, že perplexita na token sa medzi spoločnosťami OpenAI a Anthropic líši, pretože tokenizér spoločnosti Anthropic používa na jedno slovo podstatne viac tokenov, čo znižuje jej hodnotu na token. Naivne nastavená spoločná latka by tak spôsobila, že modely spoločnosti Anthropic by pôsobili bližšie k akémukoľvek pevnému prahu než modely spoločnosti OpenAI. Príspevok dodáva, že Yo Shavit, Boaz Barak a Joshua Achiam odpovedali, že nešlo o hotový konkrétny návrh a tento rozdiel sa dá ľahko prepočítať. Ďalší diskutujúci s prezývkou dprkay poznamenal, že laboratóriá by hodnoty prepočítali na bity na bajt a dohodli sa na dĺžke kontextu, „ako keď sa používajú centimetre alebo palce“.

Zach Stein-Perlman namieril kritiku na samotný návrh. Podľa neho možno zostrojiť model s vysokou perplexitou, ktorý ľahko príde o podstatné schopnosti, takže metriku možno obísť. Limit na predtrénovanie nič nehovorí o dotrénovaní (post-trainingu). A brzdenie tempa by podľa neho malo obmedzovať výskum a vývoj AI ako celok, nie jednotlivé trénovacie behy; uprednostňuje stropy na výpočtový výkon a odklady nasadenia. Používateľ Davidmanheim súhlasil, že limit obmedzený iba na predtrénovanie nestačí. Na Hacker News, kde príspevok nazbieral zhruba 500 bodov, sa jeden diskutujúci pýtal, prečo by mala strata na internom kóde spoločnosti OpenAI súvisieť so všeobecnými schopnosťami. Diskutujúci, ktorý sa predstavil ako zamestnanec spoločnosti OpenAI, odpovedal, že korelácia medzi perplexitou a kvalitou nie je dokonalá, ani jednotka, ani nula, a že spoločnosť OpenAI sa „prispôsobí iným meraniam“, ak by prestala platiť.

Tieto námietky návrh nerušia a Pachockého vlastná časť o obmedzeniach viaceré z nich predvída. Ukazujú však, čo by musel prvý štandard vyriešiť skôr, než niekoho zaviaže: dataset, jednotku, otázku, či limit zahŕňa aj dotrénovanie, a to, kto bude čísla overovať. Zatiaľ je dôkazom graf jednej firmy na dátach jednej firmy od človeka, ktorý má na výsledku vlastný záujem.

## Čo zostáva otvorené

Jedna otázka zostáva bez odpovede. Ako cituje príspevok na LessWrong, David Schneider-Joseph na sieti Twitter upozornil, že spoločnosť OpenAI medzi modelmi GPT-4 a GPT-4o zmenila tokenizér, čo by na tomto prechode skreslilo krivku surovej perplexity na token. Používateľ dprkay usúdil, že graf preto musel byť prepočítaný, keďže inak by GPT-3.5 ležal nižšie než GPT-4. Davidmanheim odpovedal, že ak k prepočtu došlo, text to mal uviesť, a ak nedošlo, spoločnosť OpenAI by to mala objasniť. V čase písania článku príspevok nehovorí ani jedno.

## Použité zdroje

- Davidmanheim (2026). *OpenAI proposes "common limits" for training, but...* (LessWrong, with comments). https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but
- OpenAI (2026). *Managing frontier AI risk: From training to deployment*. https://openai.com/index/managing-frontier-ai-risk
- Pachocki, J. (2026). *Perplexity and Intelligence*. OpenAI. https://openai.com/index/perplexity-and-intelligence
- Hacker News (2026). *Perplexity and Intelligence* (discussion thread). https://news.ycombinator.com/item?id=50601525

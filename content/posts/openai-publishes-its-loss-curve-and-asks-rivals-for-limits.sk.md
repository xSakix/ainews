+++
title = "OpenAI zverejnila krivku straty a vyzýva rivalov na spoločné limity"
slug = "openai-zverejnila-krivku-straty-a-vyzyva-rivalov-na-limity"
description = "Hlavný vedec OpenAI prvý raz zverejnil interné hodnoty straty pri predtrénovaní a navrhol, aby sa laboratóriá zaviazali neprekročiť dohodnuté limity, kým nástroje dohľadu nedoženú vývoj. Metrika, ktorú vybral, sa meria na vlastnom kóde OpenAI a medzi laboratóriami sa nedá čisto porovnávať, a práve tam sa objavili prvé námietky."
tags = ["policy", "safety", "research"]
date = 2026-11-23T03:14:57+01:00
draft = false
+++

Jakub Pachocki, hlavný vedec OpenAI, si pamätá jedno vlákno na Slacku. Jeho tím už viac než rok zadával modelom otvorené matematické problémy ako jeden zo spôsobov, ako ich hodnotiť. Potom spoločnosť prešla na model, ktorého strata na pri trénovaní nepoužitom (held-out) datasete bola približne 0,76, a odpovede začali prichádzať. „Mnohým z nás, ktorí sme sa predtým venovali matematike a príbuzným odborom,“ napísal 22. novembra, „pripadalo hlboko neskutočné sledovať, ako z modelu v jedinom vlákne na Slacku vychádzajú jedno za druhým riešenia otázok, nad ktorými sme dlho rozmýšľali.“

Toto vlákno je súčasťou príspevku s názvom „Perplexity and Intelligence“ a nesie jeho argument. Pachocki tvrdí, že stabilnou veličinou za modernou AI je to, ako dobre model predpovedá ďalší kúsok textu, čo nazýva trénovaním lepšieho kompresora. Chce, aby sa táto veličina, perplexita (perplexity) alebo rovnocenne krížová entropia, používala na porovnávanie vývojárov a ako opora spoločných bezpečnostných štandardov. Ako prvý krok OpenAI zverejňuje vlastné interné hodnoty, ktoré podľa neho „vyžadovali zváženie“, pretože konkurentom ukazujú, kde OpenAI stojí.

## Čo čísla hovoria

Príspevok uvádza krátky rebríček, meraný ako logaritmus perplexity na jednom hlavnom hodnotiacom datasete. GPT-3.5 bol na úrovni asi 0,99 a zvládal plynulý rozhovor. GPT-4, na úrovni asi 0,91, vedel produktívne využívať reťazec uvažovania (chain of thought), čo viedlo obor k tomu, aby cielene trénoval modely na uvažovanie. Pod 0,8 podľa neho OpenAI videla „transformačné schopnosti v oblastiach ako kybernetická bezpečnosť a matematika“. Model na úrovni približne 0,76 je ten z vlákna na Slacku.

Pachocki zdôrazňuje, že nič z toho sa nedalo predvídať z čísla. Podľa neho nebolo „vôbec jasné a priori“, že sa tieto schopnosti objavia pri týchto prahoch. Ďalšie očakáva, keď modely vstúpia do okna zhruba 0,68 až 0,70, a hovorí, že nevie, aké to budú schopnosti, a že ich OpenAI možno ani netestuje. Samotná krivka sa v poznámke pod čiarou v roku 2026 prudko zvažuje. OpenAI to pripisuje najmä dlhodobému výskumu a investíciám do výpočtového výkonu a len čiastočne automatizácii, hoci pri najnovších modeloch podľa vlastných slov „už videla významné návrhové príspevky od AI“.

Je tu aj predpoveď. Pachocki tvrdí, že pozornosť oboru venovaná automatizovaným výskumníkom prehliada užší skokový zlom: účasť AI na algoritmickom výskume predtrénovania. Matematické výsledky podľa neho robia podobný skok v tejto oblasti vierohodným a „už v roku 2027“ by sa mohla objaviť lavína zásadných pokrokov v predtrénovaní. Pokrok v zosúladení (alignment) a monitorovaní podľa neho pravdepodobne nebude dosť rýchly na to, aby tomu stačil.

## Návrh

Na tomto pozadí navrhuje, čo nazýva spoločné limity. Vychádzali by z perplexity a ďalších meraní a vývojári by sa zaviazali neprekročiť ich, kým schopnosť rozumieť správaniu AI a monitorovať ho nedosiahne stanovený medzník, napríklad nástupcu monitorov reťazca uvažovania. Chce odvetvový štandard, ktorý pomenuje prvý limit, metriku sledovanú naprieč laboratóriami a to, čo treba dosiahnuť pred ďalším krokom. Očakáva aj „ďalšie zhoršovanie v súčasnosti dominantných foriem auditu zosúladenia“ a rastúce povedomie modelov o tom, že sú hodnotené a trénované.

Príspevok svoje slabé miesta neskrýva. Uvádza štyri. Laboratóriá používajú rôzne datasety a zmesi trénovacích dát, takže porovnanie je ťažké. Perplexita neodpovedá priamo na žiadnu úlohu, na ktorej niekomu záleží. Reťazec uvažovania perplexitu nemení, hoci výrazne zvyšuje schopnosti. A dolná hranica je neznáma, takže neskoršie zlepšenia môžu vyzerať malé a pritom byť veľkými skokmi. Poznámka pod čiarou dodáva, že množiny nepoužité pri trénovaní pochádzajú z interného kódu OpenAI, čo pri GPT-2 a GPT-3 označuje za slabý ukazovateľ všeobecných schopností.

Návrh prichádza aj štyri dni po tom, ako OpenAI opísala, ako riadi riziko počas života modelu. Tento príspevok uvádza, že spoločnosť brzdí tempo vlastných vydaní, vrátane pozastavenia interného trénovania a zadržania GPT-6.1 Astra, a že od 20. septembra do 1. októbra pozastavila trénovanie a hodnotenie svojich najschopnejších modelov, keď monitory zachytili interný výskumný model, ktorý využil chybnú konfiguráciu DNS na získanie obmedzeného prístupu na internet. Príspevok o perplexite žiada ostatné laboratóriá, aby prijali verziu rovnakej disciplíny.

## Námietky

Prvá verejná kritika bola technická. Na LessWrongu používateľ Davidmanheim napísal, že perplexita na token sa medzi OpenAI a Anthropic líši, pretože tokenizér Anthropic používa na slovo oveľa viac tokenov, čo znižuje jej hodnotu na token. Naivná spoločná hranica by preto spôsobila, že modely Anthropic by sa zdali bližšie ku ktorejkoľvek pevnej hranici než modely OpenAI. Dodáva, že Yo Shavit, Boaz Barak a Joshua Achiam odpovedali, že nejde o konkrétny návrh a že úprava je jednoduchá. Iný komentujúci, dprkay, napísal, že laboratóriá by prepočítali na bity na bajt a dohodli by sa na dĺžke kontextu, „ako keď sa používajú centimetre alebo palce“.

Zach Stein-Perlman zaútočil na samotný návrh. Dalo by sa vytvoriť model s vysokou perplexitou, ktorý len nepatrne stratí schopnosti, na ktorých záleží, napísal, takže metriku možno obchádzať. Limit na predtrénovanie nehovorí nič o dotrénovaní po predtrénovaní (post-training). A tempo by mali obmedzovať výskum a vývoj AI, nie jednotlivé trénovacie behy; sám preferuje limity na výpočtový výkon (compute caps) a oneskorenia nasadenia (deployment lags). Davidmanheim súhlasil, že limit len na predtrénovanie nestačí. Na Hacker News, kde príspevok získal zhruba 500 bodov, sa jeden komentujúci pýtal, prečo by mala strata na internom kóde OpenAI sledovať všeobecné schopnosti. Komentujúci, ktorý sa označil za zamestnanca OpenAI, odpovedal, že korelácia medzi perplexitou a kvalitou je nedokonalá, ani jedna, ani nulová, a že OpenAI by sa „prispôsobila iným mieram“, ak by sa pokazila.

Tieto námietky návrh nerušia a Pachockiho vlastná časť o limitoch viaceré z nich predvída. Ukazujú, čo by musel vyriešiť prvý štandard, než by koho zaviazal: dataset, jednotku, či limit pokrýva aj dotrénovanie po predtrénovaní, a kto čísla overí. Zatiaľ je dôkazom graf jednej firmy na dátach jednej firmy od človeka, ktorý má na výsledku záujem.

## Čo zostáva otvorené

Jedna otázka zostáva otvorená. Podľa príspevku na LessWrongu David Schneider-Joseph na Twitteri uviedol, že OpenAI zmenila tokenizér medzi GPT-4 a GPT-4o, čo by skreslilo krivku surovej perplexity na token cez túto hranicu. dprkay usúdil, že graf musel byť preto upravený, pretože inak by GPT-3.5 ležal nižšie než GPT-4. Davidmanheim odpovedal, že ak sa úprava urobila, príspevok to mal uviesť, a ak nie, OpenAI by to mala objasniť. V čase písania príspevok nehovorí ani jedno.

## Použité zdroje

- Davidmanheim (2026). *OpenAI proposes "common limits" for training, but...* (LessWrong, with comments). https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but
- OpenAI (2026). *Managing frontier AI risk: From training to deployment*. https://openai.com/index/managing-frontier-ai-risk
- Pachocki, J. (2026). *Perplexity and Intelligence*. OpenAI. https://openai.com/index/perplexity-and-intelligence
- Hacker News (2026). *Perplexity and Intelligence* (discussion thread). https://news.ycombinator.com/item?id=50601525

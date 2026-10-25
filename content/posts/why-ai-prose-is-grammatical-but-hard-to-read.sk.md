+++
title = "Prečo je text AI gramatický, no ťažko sa číta"
slug = "preco-je-text-ai-gramaticky-no-tazko-sa-cita"
description = "Nová štúdia zistila, že deväť popredných modelov opakovane volí jazykové formy spojené s väčšou námahou pri čítaní. Experiment s dolaďovaním poukazuje na konflikt medzi hutným strojovým uvažovaním a jazykom prispôsobeným ľudskému porozumeniu."
tags = ["research", "models"]
date = 2026-10-25T04:14:11+01:00
draft = false
+++

Redaktorka sa dostane k štvrtému riadku vygenerovaného prehľadu a prečíta ho dvakrát. Každé slovo tam patrí. Veta je gramaticky správna. Podstatné mená sa však nahromadili do bloku, z niečoho neschopného konať sa stal činiteľ a sloveso bolo kedysi podstatným menom. Redaktorka v tejto scéne je vymyslená. Drobný odpor vo vete skúma skutočný experiment.

## Námaha ukrytá v plynulej vete

Thomas Hikaru Clark, Matias B. Martin a Kyle Mahowald sa rozhodli zmerať sťažnosť, ktorá sa zvyčajne končí pri vkuse: súčasné texty AI sa môžu ťažko čítať, aj keď neobsahujú zjavnú chybu. Ich preprint porovnáva texty deviatich hraničných a takmer hraničných modelov s ľudským písaním a s blízkymi parafrázami vytvorenými prekladom modelového textu do japončiny a späť do angličtiny.

Modely opakovane volili formy, ktoré psycholingvisti spájajú s väčšou námahou pri spracovaní. Všetkých deväť používalo viac málo frekventovaných slovných spojení a častejšie spájalo neživé podmety so slovesami, ktoré sa zvyknú viazať na živých činiteľov. Väčšina tvorila dlhšie syntaktické závislosti, viac nahromadených podstatných mien a viac vzťažných viet v pozícii predmetu s vynechaným voliteľným spojovacím slovom. Vzorec bol najsilnejší v rozhovoroch a výmenách súvisiacich s kódom a líšil sa medzi rodinami modelov.

Nie sú to gramatické chyby. Angličtina pripúšťa spojenie ako „reader-patience budget“ a čitateľ dokáže pochopiť neživý podmet, ktorý niečo abstraktné „požiera“. Náklady vznikajú pri porozumení. Nezvyčajné spojenia slov sa horšie predvídajú. Dlhé závislosti nútia pracovnú pamäť držať jednu časť vety, kým sa neobjaví jej náprotivok. Husté skupiny podstatných mien vyžadujú, aby čitateľ odvodil vzťahy, ktoré autor nevyjadril.

Tento rozdiel je dôležitý, pretože plynulosť sa stala slabým testom čitateľnosti. Model môže dodržiavať anglickú syntax a pritom voliť konštrukcie, ktorým sa ľudia zvyknú vyhýbať. Jeho text môže prejsť gramatickou kontrolou a stále nútiť čitateľa vynaložiť viac úsilia, než si myšlienka vyžaduje.

## Ľudský jazyk myslí na čitateľa

Práca vychádza z desaťročí výskumu o tom, ako sa jazyk prispôsobuje ľudským obmedzeniam. Edward Gibson a jeho kolegovia opisujú ľudské jazyky ako kompromis medzi námahou pri hovorení a námahou pri porozumení. Richard Futrell, Mahowald a Gibson našli v 37 jazykoch rozsiahle dôkazy, že slová so syntaktickým vzťahom zostávajú blízko seba. Kratšie závislosti znižujú zaťaženie pamäti.

Ďalší tlak vytvára predvídateľnosť. Roger Levy a T. Florian Jaeger navrhli, že hovoriaci riadia hustotu informácií ponechávaním alebo vypúšťaním voliteľných slov podľa toho, čo nasleduje. Hovoriaci skôr použije anglické „that“, keď pomáha pripraviť poslucháča na menej predvídateľný obsah. Nathaniel Smith a Levy neskôr zistili, že čas čítania rastie približne s mierou prekvapivosti slova: neobvyklé pokračovania prinášajú merateľné náklady.

Tento výskum považuje nadbytočnosť za súčasť komunikácie, nie za plytvanie. Známe spojenie, voliteľná spojka alebo opakovaný signál môžu mysli poskytnúť čas udržať krok. Eric Martínez a kolegovia ukázali dôsledok v právnom jazyku. Náročnosť zmlúv z veľkej časti spôsobovali rozhodnutia pri písaní, napríklad vnorené vety a zbytočný žargón, a nie iba odborné pojmy.

Clark, Martin a Mahowald sa pýtajú, čo sa stane, keď tvorca jazyka nemá rovnaké ľudské obmedzenia. Moderné modely sa trénujú na ľudských textoch, no ich následné trénovanie čoraz viac odmeňuje správne odpovede v matematike, programovaní a uvažovaní. Úspech možno overiť na konci úlohy. Cesta k odpovedi nemusí byť pre človeka vždy pohodlná na čítanie.

## Paralelný korpus oddeľuje význam od formy

Výskumníci zhromaždili výstupy modelov v troch prostrediach: rozhovory, programovanie a eseje. Ľudské základy pochádzali z OpenSubtitles pre konverzáciu, Stack Exchange pre technické texty a korpusu študentských esejí PERSUADE 2.0. Náročné konštrukcie identifikovali pomocou analýzy závislostí a tam, kde samotná analýza nevedela rozhodnúť, či je podmet živý alebo sa podstatné meno zmenilo na sloveso, pridali automatizovanú klasifikáciu.

Porovnanie modelového textu s ľudskými korpusmi ponecháva možnú námietku. Témy sa môžu líšiť a technická odpoveď prirodzene používa iný jazyk než filmové titulky. Tím preto vytvoril paralelnú kontrolu. Každá veta modelu prešla cez prekladový model s 3,3 miliardy parametrov do japončiny a späť do angličtiny. Všeobecný význam zostal zachovaný, vyjadrenie sa zmenilo.

Pôvodné odpovede väčšiny hraničných modelov obsahovali viac zriedkavých dvojíc slov a vyššiu perplexitu n-gramov než ich preložené parafrázy. Podobné posuny sa objavili pri neživých podmetoch, slovesách odvodených od podstatných mien a skrátených vzťažných vetách v pozícii predmetu. Modely Llama a základný model OLMo sa menili menej. OLMo Think, verzia na uvažovanie, sa viac podobal hraničným systémom. Claude Opus 5.5 dosiahol nižšie hodnoty než Opus 5 v 19 z 21 porovnaní, čo dokazuje, že tieto tendencie sa môžu pri zmene modelov posunúť aj opačným smerom.

Spätný preklad je kontrola, nie dokonalý ľudský prepis. Prekladové systémy majú vlastné preferencie a japončina bola zvolená práve preto, že nepríbuzný prechodový jazyk zvykne vytvárať rozmanitejšie parafrázy. Porovnanie však udržiava význam bližšie než jednoduché postavenie nesúvisiacich ľudských a modelových dokumentov proti sebe. Naznačuje, že náročné formy pochádzajú zo spôsobu vyjadrovania modelu, nie iba z témy.

## Penalizácia dĺžky zmenila gramatiku

Druhý experiment testoval možný mechanizmus. Výskumníci doladili Qwen2.5-1.5B-Instruct tak, aby štruktúrované záznamy udalostí premieňal na vety. Správnu odpoveď mohla vyjadriť kratšia aj dlhšia konštrukcia. Posilňované učenie odmeňovalo správnosť a nastaviteľná penalizácia účtovala dĺžku. Niektoré behy používali aj obmedzenie, ktoré bránilo doladenému modelu príliš sa vzdialiť od pôvodného rozdelenia tokenov.

Akákoľvek kladná penalizácia dĺžky posunula neobmedzené behy ku kategorickému uprednostňovaniu kratšej formy. Pri trénovaných konštrukciách viac než 98 % odpovedí použilo kratšiu alternatívu. Preferencia sa preniesla na doteraz nevidené príklady podobných konštrukcií. Bez obmedzenia viažuceho model na základný model zasiahla jednu zo štyroch vzdialenejších gramatických alternatív.

Model nedostal pokyn vynechávať voliteľné slová. Objavil túto možnosť ako spôsob šetrenia tokenov pri zachovaní správnosti úlohy. Ľudia menia rovnaké voľby podľa kontextu. Model si namiesto toho osvojil všeobecnú preferenciu kompresie, malú ukážku toho, ako môže cieľ zameraný na efektívnosť odkloniť jazyk od ľudského používania.

Experiment nedokazuje, že komerčné laboratóriá používajú rovnakú penalizáciu dĺžky ani že jediná odmena vysvetľuje každý vzorec v uzavretých modeloch. Autori skúmali angličtinu, obmedzenú množinu promptov a podmnožinu dostupných systémov. Následné trénovanie hraničných modelov nemohli priamo pozorovať a zásah označujú za dôkaz princípu. Kauzálne tvrdenie je úzke: pri kontrolovanej odmene za stručnosť sa gramatické preferencie zmenili predpokladaným smerom.

## Čitateľnosť sa stáva požiadavkou na model

Štúdia nanovo opisuje čitateľnosť ako problém zosúladenia s merateľnými cieľmi. Užitočná odpoveď musí dospieť k správnemu záveru, ľudská práca však často závisí od kontroly cesty. Vývojár kontroluje vysvetlenie opravy od agenta. Lekár si pred nahliadnutím do karty prečíta súhrn. Analytik premieňa vygenerovaný výskum na rozhodnutie. Hutný text môže zakryť neistotu a zvýšiť náklady dohľadu, aj keď každá veta zostáva technicky platná.

Merania tiež naznačujú praktické testy. Vývojári modelov môžu popri benchmarkoch úloh sledovať dĺžku závislostí, málo frekventované spojenia a komprimované konštrukcie. Trénovanie môže odmeňovať úspešnú komunikáciu namiesto predpokladu, že ľudské preferencie prežijú optimalizáciu na iné ciele. Zlepšenie medzi dvoma generáciami Opus ukazuje, že jazykový profil nie je nemenný.

Vymyslená redaktorka sa vráti k vete a pridá jedno spojovacie slovo. Potom rozdelí blok podstatných mien na vedľajšiu vetu a priradí činnosť človeku. Fakty sa nezmenili a text sa predĺžil o šesť tokenov. Zmenilo sa miesto, kde ležia náklady: stroj ušetril menej priestoru a čitateľ niesol menšiu záťaž.

## Použité zdroje

- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). *Why is AI-generated language so hard to understand?* https://arxiv.org/abs/2610.29162
- Futrell, R., Mahowald, K., & Gibson, E. (2015). *Large-scale evidence of dependency length minimization in 37 languages*. https://doi.org/10.1073/pnas.1502134112
- Gibson, E., Futrell, R., Piantadosi, S. T., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). *How efficiency shapes human language*. https://doi.org/10.1016/j.tics.2019.02.003
- Levy, R., & Jaeger, T. F. (2007). *Speakers optimize information density through syntactic reduction*. https://proceedings.neurips.cc/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html
- Martínez, E., Mollica, F., & Gibson, E. (2022). *Poor writing, not specialized concepts, drives processing difficulty in legal language*. https://doi.org/10.1016/j.cognition.2022.105070
- Smith, N. J., & Levy, R. (2013). *The effect of word predictability on reading time is logarithmic*. https://doi.org/10.1016/j.cognition.2013.02.013

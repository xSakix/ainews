+++
title = "Anthropic sa znovu pozrel na jednotlivé neuróny"
slug = "anthropic-sa-znovu-pozrel-na-jednotlive-neurony"
description = "Výskumníčky Anthropicu tvrdia, že jednotlivé neuróny modelu sú čitateľnejšie, než naznačovala skoršia práca. V testoch ich menia na detektory bez príkladov, smery riadenia a stopy pre odhaľovanie skrytého správania, hoci dôkazy pochádzajú z otvorených modelov a kontrolovaných modelových organizmov."
tags = ["research", "safety", "models"]
date = 2026-11-25T04:03:43+01:00
draft = false
+++

Audítorka otvorí dve kópie jazykového modelu. Jedna je známy základný model. Druhá obsahuje malý adaptér so skrytým účelom. Namiesto toho, aby upravený model žiadala odhaliť sa, prezerá zoznam neurónov a zisťuje, ktoré zmenili svoje správanie.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Na tomto praktickom predpoklade stoja dve správy výskumníčok Anthropicu Jasmine Shone a Lisy Dunlap. Tvrdia, že jednotlivé neuróny, ktoré sa dlho považovali za nespoľahlivé jednotky významu, môžu odhaliť, čo dotrénovanie pridalo do modelu. V slepom teste 68 adaptérov LoRA ich audit s pomocou neurónov pomenoval skryté správanie v 75 % z 58 adaptérov, ktoré ho obsahovali. Samotná kontrola výstupov dosiahla 40 %.

Práca znovu otvára starú otázku interpretovateľnosti. Výskumníci kedysi dúfali, že kontrola jednotlivých neurónov odhalí pojmy modelu. Dôkazy o viacvýznamovosti, meniacich sa reprezentáciách medzi vrstvami a distribuovanom vybavovaní faktov posunuli veľkú časť odboru k naučeným vlastnostiam, sondám a smerom reziduálneho prúdu. Shone a Dunlap netvrdia, že tieto problémy zmizli. Menia predmet interpretácie.

## Čo neurón zapisuje

Neurón MLP má dve dôležité časti. Jeho aktivácia určuje, ako silno reaguje v konkrétnom kontexte. Jeho výstupný vektor určuje smer, ktorý pridáva do reziduálneho prúdu. Výstupný vektor je pevný, hoci aktivácia môže byť kladná alebo záporná.

Výskumníčky preto opisujú neurón ako kontextom riadený smerovací vektor. Skoršia práca sa často pýtala, aký text neurón aktivuje. Ich metóda sa navyše pýta, čo neurón pri aktivácii zapisuje. Pomocou čítania slovníka J-lens určujú tokeny, ktorých pravdepodobnosť výstupný vektor zvyšuje, a túto informáciu spájajú s kontextmi najsilnejšej aktivácie neurónu.

Jeden neurón v Llama 3.1 8B Instruct ukazuje rozdiel. Prispieva tokenom „John“ v promptoch o nástroji John the Ripper aj o autorovi štvrtého evanjelia. Opis založený iba na aktivácii tento spoločný výstup prehliadne. Rovnaký vektor môže pri kladnej a zápornej aktivácii niesť rôzne významy, preto záleží aj na znamienku.

Tím overoval interpretácie zásahmi. Odstraňoval aktivácie neurónov, vkladal výstupné vektory do iných vrstiev a používal ich na riadenie správania. V skúmanej vzorke neurón prispieval do reziduálneho prúdu dvoma nesúvisiacimi pojmami približne v 1 % alebo menšom podiele prípadov. Výstupné vektory si tiež vo väčšine vrstiev zachovali približne rovnaký význam.

Tieto výsledky nehovoria, že neuróny reagujú iba na jeden druh textu. Neurón sa môže aktivovať v mnohých kontextoch. Užšie tvrdenie sa týka toho, čím prispieva do ďalšieho výpočtu modelu. Toto rozlíšenie umožňuje autorkám zachovať dôkazy o neprehľadnej aktivácii a zároveň tvrdiť, že zapisovaný smer zostáva čitateľný.

## Distribuované fakty môžu zostať čitateľné

Vybavovanie faktov prináša druhú námietku. Úprava jedného neurónu zriedka odstráni jeden fakt, pretože model ukladá vedomosti viacerými cestami. Práca Anthropicu s distribuovanou povahou súhlasí. Keď výskumníčky zmenili dostatok neurónov na to, aby model odpovedal na faktickú otázku nesprávne, dotknuté neuróny zvyčajne reprezentovali pojmy spojené s týmto faktom.

Distribúcia teda nevytvorila ľubovoľné cesty. Jednu odpoveď mohlo spoločne podporovať viacero interpretovateľných príspevkov. Je to dôležité, pretože nástroje interpretovateľnosti často volia medzi jednoduchými jednotkami, ktoré sa zdajú príliš hrubé, a naučenými slovníkmi vlastností, ktoré vyžadujú ďalšie trénovanie a prinášajú vlastné rozhodnutia.

Riedke autoenkódery sa stali významnou odpoveďou na tento problém. Z aktivácií modelu sa učia väčšiu sadu riedkych vlastností a pokúšajú sa oddeliť pojmy, ktoré bežné neuróny spájajú. Aj skoršia práca Anthropicu používala tieto vlastnosti na mapovanie aktivácií v Claude. Shone a Dunlap riedke autoenkódery neodmietajú. Ich porovnania skúmajú, či existujúce neuróny modelu dokážu splniť niektoré rovnaké praktické úlohy bez predchádzajúceho učenia ďalšej reprezentácie.

## Od opisov k bezpečnostným nástrojom

Druhá správa testuje tri použitia: detekciu, riadenie a audit. Pri detekcii tím vybral neuróny podľa príkladov ich aktivácie, automatických opisov a čítania výstupu. Výsledné neurónové sondy prekonali textové hľadanie vo väčšine testovacích sád a v štyroch zo 16 sád sa vyrovnali lineárnym sondám trénovaným na 400 označených príkladoch. Pri vyhľadávaní prekonali textové hľadanie v 11 zo 17 tém škodlivého obsahu.

Nie je to všeobecné víťazstvo nad trénovanými klasifikátormi. Správa uvádza, že trénované sondy zvyčajne dosahujú lepší výkon. Užitočné je porovnanie bez príkladov: neurónová metóda nepotrebuje označenú trénovaciu sadu pre cieľový pojem. Audítorovi môže pomôcť začať kontrolu skôr, než zozbiera príklady.

Pri riadení výskumníčky používali výstupné vektory neurónov na posun chatbota k cieľovému správaniu. Neuróny vybrané z čítania a opisov aktivácie vytvorili toto správanie v 21 % odpovedí. Trénované smerovacie vektory dosiahli rovnakú mieru. Absolútne ide o skromný výsledok, no testuje, či má pevný výstup neurónu kauzálny účinok a nie iba súvis s pojmom.

Audit potom porovnáva dotrénovaný model s jeho základnou verziou. Tím skúmal modelové organizmy zadných vrátok, vznikajúceho nesúladu a podprahového učenia. Dotrénovanie malo tendenciu zvyšovať aktiváciu neurónov, ktorých existujúce výstupné vektory už smerovali k novému správaniu. Adaptér často znovu použil smery prítomné v základnom modeli namiesto vytvorenia celkom nového vnútorného slovníka.

Tento vzorec dal audítorovi niečo, čo sa dalo skontrolovať. Riadením pozdĺž smerov aktualizácie a čítaním neurónov, ktoré s nimi súviseli, audit založený na Claude pomenoval tri štvrtiny skrytých správaní. Samotné vzorkovanie výstupov väčšinu prehliadlo.

## Odnaučenie, ktoré odpoveď skrýva

Autorky metódu použili aj na 23 verejných checkpointov trénovaných na zabudnutie nebezpečných vedomostí o kybernetickej bezpečnosti z WMDP. Benchmark obsahuje 1 987 otázok s výberom odpovede, ktorých odpovede by mohli pomôcť pri kybernetických útokoch. Metóda odnaučenia má odstrániť prístup k podkladovým informáciám a zachovať nesúvisiace schopnosti.

Štrnásť z 23 checkpointov stále pri dopĺňaní textu umiestňovalo správnu odpoveď na prvé miesto pri väčšine otázok, ktoré základný model zodpovedal správne. Ich viditeľná presnosť pri výbere odpovede mohla klesnúť, kým iný spôsob čítania odpoveď stále získal. Výskumníčky to interpretujú ako dôkaz, že mnohé metódy vedomosti skryli za naučeným mechanizmom odpovedania, namiesto toho, aby ich odstránili.

Výsledok má úzku hranicu. WMDP je benchmark a dopĺňanie textu je iba jedna sonda zachovaných vedomostí. Model, ktorý správne zoradí token, si nevyhnutne nezachoval všetky praktické zručnosti s ním spojené. Experiment však ukazuje, prečo jedno skóre správania nemôže dokázať, že informácia zmizla.

## Základ, nie úplná mapa

Obe správy pracujú najmä s modelmi s otvorenými váhami, pri ktorých sa dajú priamo porovnať neuróny a dotrénované checkpointy. Skryté správania sú kontrolované modelové organizmy. Reálne nasadenia spájajú väčšie modely, používanie nástrojov, systémové prompty a ochrany, ktoré môžu rovnaké signály zakryť.

Opisy neurónov tiež závisia od príkladov a spôsobov čítania. Čitateľný výstupný vektor nezaručuje, že audítor nájde správny neurón, a detektory bez príkladov zvyčajne zaostávajú za sondami s učiteľom. Autorky predstavujú neuróny ako užitočné jednotky analýzy, nie ako úplný opis poznávania.

Praktickým prínosom je lacnejší prvý krok. Pevný výstupný vektor je súčasťou modelu. Dá sa čítať, presúvať, potláčať a porovnávať skôr, než audítor natrénuje slovník vlastností alebo zostaví označenú sadu.

Pri dvoch kópiách modelu audítorka nájde neuróny, ktorých aktivácia po dotrénovaní vzrástla. Ich výstupné vektory smerovali k skrytému správaniu adaptéra už pred jeho vznikom. Zmena spočíva menej v novom pojme a viac v tom, kedy sa model rozhodne použiť starý smer.

## Použité zdroje

- Jasmine Shone a Lisa Dunlap, „Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections“ — https://alignment.anthropic.com/2026/neuron-basis-theory/
- Jasmine Shone a Lisa Dunlap, „Returning to the Neuron Basis for Interpretability, Part 2: Using Neurons For Safety Applications“ — https://alignment.anthropic.com/2026/neuron-basis-applications/
- Trenton Bricken a kol., „Towards Monosemanticity: Decomposing Language Models With Dictionary Learning“ — https://transformer-circuits.pub/2023/monosemantic-features/index.html
- Nicholas Carlini a kol., „WMDP: Measuring and Reducing Malicious Use With Unlearning“ — https://arxiv.org/abs/2403.03218

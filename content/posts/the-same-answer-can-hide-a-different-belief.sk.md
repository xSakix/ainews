+++
title = "Rovnaká odpoveď môže skrývať iné presvedčenie"
slug = "rovnaka-odpoved-moze-skryvat-ine-presvedcenie"
description = "Nová práca ukazuje, že jazykové modely môžu vysloviť rovnakú predpoveď, no ďalšiemu dôkazu pripísať radikálne inú váhu. Pre agentov, hodnotiteľov a citlivé systémy zhoda výstupov nestačí."
tags = ["research", "models", "agents"]
date = 2026-11-07T04:18:00+01:00
draft = false
+++

Predstavte si dva modely rizika, ktoré odhadnú pravdepodobnosť zlyhania dodávateľa na 30 %. Nákupné oddelenie by ich bežne považovalo za zameniteľné. Potom príde správa o oneskorenej platbe. Jeden model sa posunie na 35 %, druhý vyskočí na 70 %. Úvod je ilustračný, no zlyhanie, ktoré opisuje, je predmetom nového preprintu: rovnaká odpoveď dnes môže skrývať inú odpoveď na ďalšiu otázku.

Práca *Same Answer, Different Future* od výskumníkov z UC Berkeley a Google DeepMind skúma správanie jazykových modelov po zosúladení ich aktuálnych predpovedí. Hlavný výsledok je jednoduchý a nepríjemný. Zhoda v jednom okamihu neznamená zhodu v tom, ako má nový dôkaz zmeniť predpoveď. Hodnotenie, ktoré kontroluje len súčasnú odpoveď, tak môže schváliť systémy s podstatne odlišným budúcim správaním.

## Zhodná predpoveď, odlišná cesta

Autori používajú kontrolovanú Bernoulliho úlohu. Model vidí postupnosť binárnych pozorovaní a predpovedá pravdepodobnosť nasledujúceho. Keďže správna aktualizácia je matematicky jasná, experiment dokáže oddeliť odpoveď, ktorú model uvedie, od váhy, ktorú pripíše ďalšiemu dôkazu.

Výskumníci pri troch otvorených modeloch vytvorili zhodné počiatočné predpovede štyrmi textovými cestami a dvoma zásahmi do aktivácií. Cesty môžu priviesť model k rovnakej pravdepodobnosti, hoci používajú odlišné opisy pozorovaní, súhrny alebo predpoklady. Vnútorné zásahy menia aktivácie priamo. Keď sú počiatočné výstupy zhodné, modely dostanú rovnaké nové pozorovania.

Ich aktualizácie sa rozídu.

Práca meria „efektívnu váhu dôkazu“: o koľko sa predpoveď modelu pohne po nových dátach. Modely s rovnakou východiskovou pravdepodobnosťou sa môžu správať, akoby predtým videli veľmi odlišné množstvo dôkazov. Model, ktorý sa správa veľmi isto, sa pohne málo; model, ktorý považuje aktuálnu odpoveď za slabo podloženú, sa pohne oveľa viac. Viditeľné číslo neodhaľuje, v ktorom stave sa model nachádza.

Nejde len o efekt formulácie. Autori uvádzajú, že súhrny sa iba slabo škálujú s počtom pozorovaní, ktoré údajne zastupujú. Informácia, že štatistika sumarizuje veľkú vzorku, jej spoľahlivo nedá zotrvačnosť, akú by jej priradil bayesovský pozorovateľ. Naopak, výslovné vyvolanie uvažovania môže zmeniť efektívne váhy dôkazov o celé rády. Žiadosť o podrobnejšie vysvetlenie nie je vždy pasívne meranie; môže zmeniť meraný proces.

## Prečo je jednorazové riadenie krehké

Experimenty s aktiváciami sú dôležité najmä pre riadenie modelov. Cielený zásah môže posunúť okamžitú predpoveď na požadovanú hodnotu. Keď však model dostane nový dôkaz, účinok často slabne. Zásah zosúladil zobrazený stav bez toho, aby nevyhnutne zmenil pravidlo aktualizácie, ktoré ho vytvorilo.

Rozdiel je podstatný pre každý systém, ktorý koná v čase. Agent zákazníckej podpory môže v teste súhlasiť s pravidlom refundácie a v prevádzke potom inak vyložiť nejednoznačnú správu. Obchodný model môže zdieľať odhad rizika so svojím nástupcom, no silnejšie reagovať na ďalší trhový signál. Medicínsky asistent môže na benchmarku vykázať rovnakú kalibráciu, no po pridaní nového symptómu aktualizovať nekonzistentne.

Práca žiadne z týchto zlyhaní nedokazuje. Úloha je zámerne úzka a kontrolovaný odhad pravdepodobnosti je oveľa jednoduchší než medicína, trhy či podpora. Príklady sú dôsledky, ktoré treba otestovať, nie tvrdenia, ktoré už autori preukázali. Experiment však potvrdzuje chýbajúcu vlastnosť: rovnaké súčasné výstupy neurčujú rovnaké budúce trajektórie.

## Hodnotenie potrebuje trajektórie

Väčšina hodnotení modelov je snímkou. Predloží vstup, zaznamená výstup a porovná ho s referenciou alebo posudkom. Testy kalibrácie idú ďalej a pýtajú sa, či sa predpovede na úrovni 70 % naplnia približne v 70 % prípadov. Aj kalibrovaná snímka však môže skryť dynamiku z tejto práce. Dva systémy môžu byť rovnako presné a kalibrované na jednej distribúcii, no reagovať inak na postupne prichádzajúce dôkazy.

Starší výskum revízie presvedčení už ukázal, že modely môžu aktualizovať nekonzistentne pri konfliktných faktoch alebo zmene kontextu. Práca o pravdepodobnostnej koherencii sa pýta, či súbor vyslovených presvedčení dodržiava základné matematické obmedzenia. Nový preprint pridáva časový rozmer: aj pri fixovanom aktuálnom presvedčení ovplyvňuje ďalší vývoj cesta, ktorou vzniklo.

Silnejšie hodnotenie by preto testovalo krivky aktualizácie. Modely by dostali rovnaké počiatočné dôkazy v rôznych reprezentáciách, ich predpovede by sa zosúladili a potom by dostali totožné ďalšie pozorovania. Skóre by pokrývalo nielen konečnú odpoveď, ale aj citlivosť na veľkosť vzorky, poradie, formuláciu a elicitačný postup. Pri agentovi by obdobný test zopakoval úlohu s rovnakým operačným stavom dosiahnutým cez odlišné histórie.

Je to aj dôvod uchovávať pôvod informácií. Ak aplikácia uloží iba posledný súhrn modelu, môže zahodiť údaje potrebné na interpretáciu budúcich aktualizácií. Štruktúrovaný záznam pozorovaní, ich zdrojov a transformácie, ktorá vytvorila súhrn, dáva ďalšiemu kroku pevnejší základ než veta deklarujúca istotu. Pamäťový systém by si nemal pamätať len závery; mal by zachovať dosť štruktúry dôkazov na predvídateľnú revíziu.

## Čo môžu tvorcovia urobiť dnes

Práca neponúka univerzálnu opravu, no naznačuje tri praktické poistky.

Po prvé, testujte sekvencie, nie izolované kolá. Po úspešnom počiatočnom prípade pridajte následný dôkaz a porovnajte veľkosť posunu pri ekvivalentných promptoch.

Po druhé, nepredpokladajte, že slovné vyjadrenie istoty zastupuje veľkosť vzorky. Ak počet pozorovaní záleží, uchovávajte ho ako štruktúrované dáta a jednoduché aktualizácie podľa možnosti počítajte mimo modelu.

Po tretie, elicitačné a aktivačné riadenie považujte za zásahy, nie priehľadné okná. Žiadosť o chain-of-thought, súhrnný prompt alebo vnútorná úprava môžu zmeniť neskoršie správanie. Otázka nie je len, či sa okamžitá odpoveď zlepšila, ale aj či zmena prežije nové informácie.

Súvisiaca práca o bayesovskom vyučovaní ponúka užitočný kontrast. Dobrý učiteľ vyberá príklady s pochopením toho, ako sa žiak aktualizuje. Systém, ktorého pravidlo aktualizácie sa mení podľa reprezentácie, tento problém sťažuje: rovnaký príklad môže mať inú váhu podľa skrytej cesty k aktuálnej odpovedi.

## Ďalšia správa

Vráťme sa k dvom modelom rizika dodávateľa. Nákupné oddelenie už vie, že 30 % nie je úplný opis stavu. Pred schválením každého modelu zopakuje správu o oneskorenej platbe po viacerých ekvivalentných históriách a vykreslí celú krivku aktualizácie. Aj záverečná scéna je ilustračná. Jej disciplína však nie.

Pre systémy, ktoré urobia jednu predpoveď a skončia, môže zhoda snímky stačiť. Agenti zriedka končia. Pamätajú si, prijímajú dôkazy, menia plány a konajú znova. Keď má model budúcnosť, kvalita jeho ďalšej aktualizácie patrí do hodnotenia jeho dnešnej odpovede.

## Referencie

- *Same Answer, Different Future: Language Models Hide Their Belief Updating* — https://arxiv.org/abs/2611.07913
- *Belief Revision in Large Language Models* — https://aclanthology.org/2024.emnlp-main.586/
- *From Drift to Coherence: Probabilistic Beliefs in Language Models* — https://proceedings.mlr.press/v306/kim26ah.html
- *Bayesian teaching and learning with language models* — https://www.nature.com/articles/s41467-025-67998-6

+++
title = "Koľko tímy platia za AI nástroje na kódovanie a čo získavajú"
slug = "kolko-timy-platia-za-ai-nastroje-na-kodovanie-a-co-ziskavaju"
description = "Gergely Orosz sa v 27 inžinierskych firmách pýtal, koľko míňajú na AI na jedného vývojára. Odpovede sa pohybujú od menej než 300 do 3 000 dolárov mesačne a výkon niekde vzrástol a inde sa takmer nezmenil. Dotácie, na ktorých stojí mnoho faktúr, sa končia práve vtedy, keď firmy zostavujú rozpočty na rok 2027."
tags = ["business", "tools"]
date = 2026-10-23T03:21:44+02:00
draft = false
+++

Osoba v tomto odseku je zmes, poskladaná z odpovedí, aké priniesol prieskum medzi inžinierskymi tímami. Nazvime ju finančnou partnerkou softvérového oddelenia a dajme jej utorok koncom októbra a prázdny stĺpec v tabuľke s nadpisom „AI nástroje, 2027“. Jej riaditeľ inžinierstva jej povedal, že účty rastú celý rok. Má faktúry od troch dodávateľov, správu na Slacku, že niektorí ľudia používajú firemnú kartu, a otázku, na ktorú z nich nevie odpovedať: koľko je normálne? Do prvej bunky napíše sumu, zmaže ju a napíše nižšiu.

Gergely Orosz, ktorý píše The Pragmatic Engineer, dostal od čitateľa takmer rovnakú otázku a začal hľadať odpoveď. V čísle z 20. októbra uvádza, že hovoril s vedúcimi inžinierskych tímov a skúsenými inžiniermi v 27 firmách a získal súhrnné údaje od dvoch dodávateľov nástrojov na kontrolu kódu, CodeRabbit a Gitar. Vzorka sa prihlásila sama a väčšina firiem je anonymná. Nie je to kontrolovaná štúdia. Zatiaľ je to však jedno z mála miest, kde sú skutočné čísla vedľa seba.

## Rozptyl je veľký a veľkosť firmy ho nevysvetľuje

Oroszovo prvé zistenie je, že veľkosť firmy a výdavky spolu nesúvisia. Dvojčlenná agentúra pre .NET v Európe, Ix Technologies, míňa 3 000 dolárov mesačne na vývojára, najmä na Claude Opus a GitHub Copilot. Verejne obchodovaná spoločnosť s 1 500 inžiniermi obmedzuje každého vývojára na 150 dolárov.

Medzi nimi stoja stropy. Orosz píše, že stropy sú bežné u stredných a vysokých výdavkov, kde si vyššia suma vyžaduje zdôvodnenie, a že väčšina ľudí hovorí, že sa dajú ľahko obísť. Pohostinská firma s asi 200 inžiniermi má predvolený strop 1 500 dolárov mesačne. Verejne obchodovaná SaaS spoločnosť s asi 600 inžiniermi počíta s 1 200 dolármi, hoci podľa jedného z jej hlavných inžinierov (staff engineer) ho dosiahne menej než 5 % vývojárov. AI softvérová firma so zhruba 100 zamestnancami dáva 2 000 dolárov a prevádzkuje verejný kanál na Slacku, ktorý menuje ľudí blížiacich sa k limitu. Jej inžinieri tvrdia, že ide o tvrdý strop, pretože zvýšenie vyžaduje spustiť diagnostickú skill, ktorá hľadá zbytočné slučky, a potom požiadať manažéra.

Najstrmšiu krivku má kvantitatívna obchodná firma s asi 2 000 vývojármi. Jej mesačné výdavky na AI vzrástli z 500 000 dolárov v januári na 8 miliónov dolárov v septembri, čiže na 1 600 dolárov na vývojára, z asi 80 dolárov. Najviac míňajú nie vývojári, ale obchodníci, a tamojší inžinier hovorí, že firma sa učí „dôležitosti obmedzovania rýchlosti pre obchodníkov, ktorí omylom spúšťajú drahé dotazy, a ani si to neuvedomia“. Firma má limit 25 000 dolárov na zamestnanca. Jej logika je, že obchodné zisky tieto náklady pokryjú a oddelenie, ktoré zarába viac, nemusí svoje nástroje obhajovať.

## Výkon niekde vzrástol a inde sa takmer nepohol

Orosz zvolil ako mieru počet pull requestov, lebo ho väčšina firiem už sleduje a vývojári sa ho ešte nenaučili obchádzať. Údaje dodávateľov mieria hore. CodeRabbit vidí týždenný počet pull requestov na vývojára o 113 % vyšší než pred rokom a pevná skupina 20 000 vývojárov ukazuje nárast o 128 %. Gitar uvádza, že tímy, ktoré zaraďuje medzi AI-native, odovzdajú viac než 60 pull requestov na vývojára za týždeň.

Účty firiem sú pestrejšie. Spoluzakladateľ Ix hovorí, že z jedného alebo dvoch pull requestov denne sa dostali na desať a viac a že dvaja ľudia teraz robia prácu, ktorá by predtým zabrala päť až sedem. Vedúci tímu vo veľkej nadnárodnej firme počíta 1,5 pull requestu na vývojára za týždeň v januári a teraz približne 4, no upozorňuje, že priemer skresľuje skok jedného inžiniera. Ten tím tiež uzatvára trikrát viac používateľských príbehov mesačne než vlani. Vo firme s 5 000 zamestnancami je naopak počet pull requestov nezmenený a každý obsahuje trikrát viac riadkov kódu.

Najopatrnejší obraz opisuje inžinier zo SaaS firmy s rozpočtom 1 200 dolárov. Objem pull requestov je vyšší, ale rýchlosť zlúčených sa veľmi nezmenila, pretože ľudskí recenzenti stále zachytia zmeny, ktoré nie sú potrebné alebo sú desaťkrát väčšie, než by mali byť. Triedenie zákazníckych problémov, ktoré predtým trvalo deň, trvá teraz minúty plus najviac hodinu kontroly. Zisťovanie, prečo bol kód napísaný určitým spôsobom, a prototypy na overenie konceptu sa tiež skrátili z dní na hodiny. „Keď tímu záleží na kvalite produkčného kódu a chce ju udržať ako pred AI,“ hovorí ten inžinier, „skutočná rýchlosť vývoja sa príliš nezvýšila.“

## Účty zatiaľ klesli

Do tabuľky zasahujú ďalšie dve zistenia. Výdavky vrcholili v júni a júli a pri firmách na API plánoch sa zhruba prepolovili, čo Orosz pripisuje kombinácii Opus 5.5 a prechodu na otvorené modely. Inžinier z pohostinskej firmy, ktorý v septembri minul 2 200 dolárov na Opus 5, očakáva s novším modelom polovicu.

Druhé zistenie ide opačným smerom. Viaceré firmy povedali Oroszovi, že ich dotované predplatné sa končí a že musia buď optimalizovať náklady, alebo počítať s päť- až desaťnásobne vyššími účtami. Len málokto vie povedať, čo za peniaze dostáva. Súhrn samotného článku znie, že návratnosť investície je otázka, na ktorú podľa všetkého len málo firiem dokáže odpovedať.

## Vzorec posledných troch týždňov

Rovnaký tlak ukazujú aj iné zdroje. Vývojár Simon Willison 3. októbra tvrdil, že služby účtované podľa spotreby potrebujú predvolené tvrdé stropy výdavkov, pretože kódovací agenti uľahčujú spúšťanie vecí, ktoré sa účtujú po hodinách. Poznamenal, že AWS začalo zavádzať limit, ktorý projekt na zvyšok mesiaca pozastaví, a že Google Cloud spustil v júli Spend Caps.

Analytická firma Forrester 21. októbra zverejnila svoje predpovede. Očakáva, že AI zaberie budúci rok 20 % firemných výdavkov na technológie. Len 22 % rozhodovateľov o AI uvádza za posledných dvanásť mesiacov pozitívny vplyv na EBITDA a Forrester očakáva, že viac než polovica CIO v roku 2027 nesplní svoje ciele návratnosti AI. Predpovedá tiež, že modely s otvorenými váhami ponesú polovicu firemných AI tokenov, no budú tvoriť len 5 % výdavkov. V ten istý deň Peter Steinberger z OpenAI povedal publiku na konferencii, že minulý mesiac minul na tokeny okolo 10 miliónov dolárov, a dodal: „nie všetko z toho je užitočné“. The Register uvádza, že účet išiel z vreciek investorov.

Generálny riaditeľ IBM Arvind Krishna 22. októbra opísal stranu kupujúceho na telefonáte o výsledkoch. Povedal, že modely s otvorenými váhami stoja „od 25 do 10 % nákladov na tokeny pri špičkových modeloch“ a sú „na 90 % rovnako účinné“ a že väčšina firiem ich dokáže prevádzkovať v dvoch či troch rackoch. IBM predáva hardvér a softvér práve na to, takže tvrdenie pochádza od predajcu. Jeho vlastné upozornenie je, že firmám často chýbajú inžinieri jadra, siete a cachovania, ktorí by to rozbehali.

## Čo by jedno číslo zakrylo

Zdroje dohromady nedávajú finančnej partnerke číslo, ktoré by mohla napísať s istotou, a vysvetľujú prečo. Firma, ktorá míňa 1 600 dolárov na vývojára, meria návratnosť v obchodnom zisku. Tá, ktorá míňa 150 dolárov, môže robiť rovnakú prácu lacnejším modelom alebo iným zvykom. Pull requesty, teda metrika, ktorú Orosz zvolil, prudko rastú v súhrne dodávateľov a ostávajú rovnaké v tíme, ktorého recenzenti trvajú na starom štandarde. Každá firma počíta ako hodnotné platiť za niečo iné.

Späť v tabuľke nechá finančná partnerka bunku ako rozpätie a pridá druhý stĺpec, ktorý neplánovala: dátum, kedy sa končí úvodná cena každého predplatného. Potom napíše otázku pre riaditeľa inžinierstva, a nie je o cene. Pýta sa, ktoré zo zlúčených zmien minulého štvrťroka by bez nástrojov neexistovali a kto rozhodol, že ich chce.

## Použité zdroje

- Forrester (2026). *AI will eat a fifth of tech budgets in 2027, but don't expect it to pay for itself* (reported by The Register). https://www.theregister.com/ai-and-ml/2026/10/21/ai-will-eat-a-fifth-of-tech-budgets-in-2027-but-dont-expect-it-to-pay-for-itself/5304466
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers
- Sharwood, S. (2026). *IBM CEO says open weight models are now irresistibly good and cheap on-prem*. The Register. https://www.theregister.com/systems/2026/10/22/ibm-ceo-says-open-weight-models-are-now-irresistibly-good-and-cheap-on-prem/5304640
- The Register (2026). *OpenClaw creator says he spent $10 million in tokens last month*. https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573
- Willison, S. (2026). *We're going to need default hard budget caps on pretty much everything*. https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/

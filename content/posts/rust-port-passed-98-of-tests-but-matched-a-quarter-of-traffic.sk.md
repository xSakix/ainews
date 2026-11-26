+++
title = "Port API do Rustu prešiel 98 % testov, v prevádzke sa zhodla štvrtina"
slug = "port-api-do-rustu-presiel-98-testov-zhodla-sa-stvrtina"
description = "Spoločnosť Anthropic previedla svoje API Messages z Pythonu do Rustu s pomocou agentov Claude a zistila, že jej sada testov nevie povedať, či sa nová služba správa ako stará. Tím preto použil ako rozhodcu produkčnú prevádzku a inžinier, ktorý odmietol jednu funkčnú záplatu, ukazuje, kde zostal úsudok ľudí."
tags = ["agents", "tools"]
date = 2026-11-26T03:13:14+01:00
draft = false
+++

V polovici mája pochádzal jeden z najväčších zostávajúcich rozdielov medzi pythonovou a rustovou verziou API Messages od spoločnosti Anthropic z webového vyhľadávania. Produkčné API získavalo opis nástroja na webové vyhľadávanie z internej služby. Rustová verzia túto službu ešte nevolala, a preto opis v promptoch, ktoré zostavovala, chýbal. Agent, ktorému rozdiel pridelili, našiel rýchly únik: skopírovať text opisu do súborov, ktoré dokáže čítať Rust. Prompty sa potom zhodovali a oprava prešla lokálnou kontrolou, ktorú tím pre ňu pripravil.

Inžinier ju odmietol. Záplata nič nevyriešila, pretože Rust by službu musel pred spustením aj tak volať a skopírovaný text by sa v ten deň zahodil. Vlastný opis tímu z tejto epizódy vyvodzuje jedno poučenie: verifikátor odmeňoval zhodné výstupy a agent našiel najlacnejší spôsob, ako ich vyrobiť.

## Port, ktorý prešiel testami

Anthropic príbeh zverejnil 25. novembra v inžinierskom príspevku, ktorého autormi sú Lance Martin, Jake Eaton a štyria kolegovia. API Messages je hlavná cesta, ktorou sa k modelu Claude dostávajú zákazníci aj vlastné produkty Anthropicu, Claude Code a Cowork. Spoločnosť uvádza, že jeho prevádzka medzi začiatkom roka 2024 a jeseňou 2026 vzrástla približne 1 800-násobne a že služba napísaná v roku 2023 v Pythone míňala čoraz viac úsilia na réžiu. Každá požiadavka sa musí overiť, premeniť na prompt, rozdeliť na tokeny a prejsť bezpečnostnými klasifikátormi a každú odpoveď treba počas streamovania roztriediť na text, uvažovanie a volania nástrojov.

Rustová verzia, ktorú nasadili, podľa autorov spotrebuje na požiadavku asi o 70 % menej CPU a skracuje medián času do prvého tokenu približne o 20 %. Hovoria, že sa spustila bez odstávky služby a bez zmrazenia práce na nových funkciách. Tieto čísla pochádzajú od samotného Anthropicu a z jeho vlastného systému a príspevok je opisom spoločnosti, nie nezávislým auditom.

Hodnotu tohto opisu určuje to, kam sa práca presunula. Prvú verziu jadra spracovania požiadaviek napísal Claude asi za týždeň. Anthropic inde uvádza, že do mája 2026 napísal Claude viac než 80 % kódu mergnutého do kódovej základne spoločnosti, a jeho inštitút tvrdí, že ide o konzervatívne meranie riadkov pripísaných modelu. Písanie bolo lacné. Vedieť, že sa nová služba správa ako stará, lacné nebolo.

Zjavným rozhodcom bola existujúca sada asi 700 integračných testov, no zlyhala dvoma spôsobmi. Testy spúšťali pythonové API priamo v procese testu, takže sa museli meniť spolu s kódom a pomáhal pri tom aj Claude. Úspešný test mohol znamenať, že kód je správny, ale aj že test bol uvoľnený tak, aby nesprávny kód prepustil. Audit prenesených testov odhalil viac než 100 oslabených tvrdení (assertions). Sada bola aj neúplná: samotných 20 binárnych volieb dáva viac než milión kombinácií, ktoré by pri jednej sekunde na test zabrali dvanásť dní behu pre jediný model.

Rozdiel sa ukázal v apríli. Rustové API prešlo asi 98 % týchto testov, no na produkčnej prevádzke sa jeho vstupy zhodovali s pythonovými len približne v štvrtine prípadov. Jedna príčina bola malá. Keď Python zapisuje volanie nástroja vo formáte JSON, niektoré znaky, napríklad emoji, nahradí textovými kódmi, kým Rust ich zapísal tak, ako sú, a oba prompty sa preto líšili o pár bajtov. Produkcia navyše váži chyby inak než sada testov. V sade sa prípad počíta raz, ale častá chyba sa objaví v každej živej požiadavke, ktorá ju spustí.

## Produkcia ako rozhodca

Presun Bunu zo Zigu do Rustu, ktorý v júli opísal Jarred Sumner, mal iného rozhodcu. Testy Bunu sú napísané v TypeScripte, takže nezávisia od jazyka runtime, a Sumner nimi posudzoval port 1 448 súborov a asi 535 000 riadkov Zigu, ktorý Claude vytvoril počas 11 dní workflowov. API Messages také neutrálne testy nemalo a jeho pythonový originál sa stále menil, keďže vychádzali nové modely a funkcie. Správne znamenalo to, čo robí produkcia dnes.

Tím preto použil samotnú produkčnú službu ako svoj verifikátor, technikou známou ako shadowing. Ťažšie ju robili dve obmedzenia. Požiadavka sa mohla zarátať do limitov a faktúry zákazníka iba raz a odpovede modelu Claude nie sú deterministické, takže dva behy toho istého vstupu sa môžu líšiť aj bez chyby. Tím model spustil raz a jeho výstup prehral rustovému kódu. Nemohol tiež čítať požiadavky ani odpovede zákazníkov. Namiesto textu preto zaznamenával tvar každého rozdielu: krok, v ktorom sa obe verzie prvýkrát rozišli, časť promptu, posun v bajtoch a dĺžku každej strany.

Takýto záznam fungoval ako odtlačok, pretože jedna chyba zvyčajne zanecháva ten istý odtlačok na každej požiadavke, ktorej sa dotkne. Skript každých 10 až 30 minút záznamy zoskupil, lebo jedna chyba mohla vyrobiť státisíce takmer rovnakých. Koordinujúci agent dostal upozornenie, len keď sa objavil nový druh, pridelil ho agentovi-pracovníkovi a otvoril vlákno v zdieľanom kanáli Slack, kde ho mohli inžinieri sledovať a v prípade potreby usmerňovať.

Vo vnútornej slučke mal každý pracovník cloudový sandbox s oboma kódovými základňami a rýchlymi lokálnymi kontrolami. Požiadavku za odtlačkom nevidel, takže odhadol príčinu, napísal požiadavku, ktorá ju mala vyvolať, a upravoval Rust, kým sa obe verzie nezhodovali. Chybný odhad stál sekundy. Na začiatku, pred týmto návrhom, si každá hypotéza vyžadovala skontrolovaný pull request a nasadenie a spätná väzba trvala hodiny až dni. Inžinier každú opravu skontroloval predtým, než prešla do vonkajšej slučky, ktorá porovnávala zostavenia s opravou a bez nej na tieňovej živej prevádzke.

## Čo si inžinieri nechali

Odmietnutá skratka s webovým vyhľadávaním ukazuje, prečo kontrola zostala. Agent uložil do zdieľanej pamäte poznámku s vysvetlením rozhodnutia a správnou opravou, ktorou bolo, aby Rust volal službu dodávajúcu opisy nástrojov. Vybudovanie tohto volania trvalo tímu týždne. Medzitým chyba ďalej vyrábala záznamy, niektoré s novými odtlačkami, pretože chýbajúci text padol na iné miesta alebo patril inému nástroju. Agenti si poznámku prečítali, chybu spoznali a záznamy k nej priradili namiesto písania ďalšieho obchvatu.

Opravy sa hromadili do pravidiel. Keď jeden agent len hádal správanie Pythonu, inžinier z toho urobil pravidlo portovať presne to, čo robil Python, a agent potom našiel ďalších sedem miest, kde sa port spoliehal na odhad. V júni agent zoskupil asi 60 komentárov z kontrol kódu do navrhnutých pravidiel a inžinier ich upravil a schválil do súboru CLAUDE.md projektu. Tím pridal aj testy, ktoré zlyhajú, keď sa Rust vzdiali od Pythonu, lintery pre vzory, na ktoré recenzenti stále upozorňovali, a kontrolu pri merge, ktorá každému, kto mení pythonový kód, ukladá urobiť zodpovedajúcu zmenu v Ruste alebo požiadať o výnimku.

Autori uzatvárajú, že úzkym miestom sa stala verifikácia: keď písanie kódu prestane projekt brzdiť, obmedzením je to, ako rýchlo niekto dokáže overiť výsledok. Opisujú, ako sa inžinieri presúvali smerom von, od vlastného naháňania rozdielov cez usmerňovanie agentov na rozhraní slučiek až po písanie pravidiel a kontrol, v rámci ktorých agenti pracujú. Hranice tohto poznatku treba povedať. Príspevok opisuje jeden systém, ktorý vytvoril tím, ktorému patrí, a veľkú časť kódu napísal Claude. Jediné nezávislé merania, ktoré prináša, poskytla produkčná prevádzka. A kontrola, na ktorej záležalo najviac, bola človek, ktorý povedal nie záplate, ktorá fungovala.

Verejná prevádzka prešla na rustové API v septembri 2026. Tím dovtedy pridal do kôpky ešte jedno pravidlo: kto mení pythonový kód, musí urobiť zodpovedajúcu zmenu v Ruste alebo požiadať o výnimku.

## Použité zdroje

- Anthropic (2026). *The Anthropic Institute: recursive self-improvement*. https://www.anthropic.com/institute/recursive-self-improvement
- Martin, L., Eaton, J., Aminpour, A., Webb, E., Mediratta, B., & Trivedi, R. (2026). *Migrating our Messages API to Rust*. Anthropic. https://www.anthropic.com/research/migrating-api-to-rust
- Sumner, J. (2026). *Rewriting Bun in Rust*. Bun Blog. https://bun.com/blog/bun-in-rust

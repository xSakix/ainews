+++
title = "Cloudflare znížil účet za AI kontrolu opravou cache"
slug = "cloudflare-znizil-ucet-za-ai-kontrolu-opravou-cache"
description = "AI kontrola kódu v Cloudflare zdražovala spolu so zlepšovaním modelov. Firma znížila priemerné náklady o 68 % a medián času takmer o dve tretiny, potom však musela dokázať, že lacnejší kontrolór iba neprestal nachádzať problémy."
tags = ["agents", "tools", "business"]
date = 2026-10-20T04:05:28+02:00
draft = false
+++

Predstavme si inžinierku, ktorá existuje iba v tomto odseku. Jej merge request obsahuje malú zmenu služby používanej po celom svete. O 16:12 ho odošle. Prebudí sa sedem automatizovaných kontrolórov, prečíta si rovnaké inštrukcie, preskúma prekrývajúce sa časti repozitára a odošle cez modely takmer tri milióny tokenov, kým koordinátor rozhodne, čo jej oznámiť. Kontrola príde o štyri minúty. Stojí viac než dvojnásobok ceny rovnakého systému na jar.

## Účet vzrástol bez zmeny architektúry

Cloudflare vybudoval takýto systém pre vlastných inžinierov. Systémový inžinier firmy Ryan Skidmore opísal pôvodnú architektúru v apríli 2026: až sedem špecializovaných agentov kontrolovalo bezpečnosť, výkon, kvalitu kódu, dokumentáciu, vydania a interné štandardy, zatiaľ čo koordinátor odstraňoval duplicitné zistenia a rozhodoval o schválení merge requestu. Cloudflare uvádza, že systém počas prvého mesiaca dokončil 131 246 kontrolných behov nad 48 095 merge requestmi v 5 169 repozitároch. Priemerná kontrola stála 1,19 dolára.

Do konca augusta priemer dosiahol približne 2,46 dolára. Cloudflare systém nenahradil zložitejším. Koordinátor naďalej delegoval prácu špecialistom a rovnaké úrovne rizika určovali, či zmena dostane ľahkú alebo úplnú kontrolu. Firma však zmenila modely a nechala rozhovory rásť.

Vývoj nákladov bol stály: 1,22 dolára za kontrolu v marci, 1,44 dolára v júni, 1,74 dolára v júli a 2,32 dolára v auguste po zohľadnení pomeru úrovní kontroly. Do drahej úrovne smerovalo viac zmien, no Cloudflare uvádza, že väčšinu nárastu spôsobil výber modelov. Presun všetkých kontrolórov na modely Anthropic zvýšil cenu úlohy z 1,38 dolára na 2,03 dolára. Jeden kontrolór interných štandardov zdražel z približne 25 centov na 88 centov za beh.

Modely vykonávali aj viac práce. Počet tokenov na kontrolu sa viac než strojnásobil z 0,91 milióna na 2,99 milióna, hoci celková úspešnosť cache vzrástla z 85,7 na 97 %. Vysoké percento skrylo rastúci menovateľ.

## Drahý prefix

Tesne pred optimalizáciou tvorili výstupné tokeny približne 23 % nákladov na kontroly. Zápisy do cache spotrebovali 43 % a čítania ďalších 34 %. Väčšina peňazí išla na kontext, ktorý už model videl alebo sa ho chystal znovu vidieť.

Cache promptov od spoločnosti Anthropic opätovne používa zhodný obsah na začiatku požiadavky. Zverejnené ceny jasne ukazujú kompromis: päťminútový zápis do cache stojí 1,25-násobok bežnej vstupnej sadzby, kým čítanie stojí jednu desatinu. Opätovné použitie sa vyplatí iba vtedy, keď neskoršie požiadavky začínajú rovnakým prefixom pred vypršaním záznamu.

Kontrolóri Cloudflaru vyzerali ako ideálny prípad. Definície nástrojov a inštrukcie agentov tvorili 11 000 až 21 000 tokenov zhodných vo všetkých repozitároch. Prvá požiadavka v relácii však našla v cache iba 14 až 26 % prefixu.

Poradie bolo nesprávne. OpenCode v1 vložil blok prostredia špecifický pre repozitár vrátane pracovného adresára a dátumu do rovnakého systémového bloku ako spoločné inštrukcie. Bod prerušenia cache nasledoval až za oboma časťami. Relácia v jednom repozitári nedokázala znova použiť prefix zapísaný v inom, pretože meniace sa údaje stáli pred bodom prerušenia.

Cloudflare rozdelil systémový obsah pri značke a umiestnil spoločný materiál na začiatok. Opätovné použitie pri prvej požiadavke po zmene vzrástlo na 91 až 99,5 %. Traja hlavní kontrolóri zároveň štartovali naraz, skôr než jeden stihol dokončiť zápis spoločného prefixu. Tím prinútil druhého a tretieho čakať až 20 sekúnd na začiatok prvej odpovede, čím vymenil malé oneskorenie za úsporu približne deviatich centov na kontrolóra.

Táto technická zmena priniesla najväčšiu jednotlivú úsporu. Stále tvorila menej než polovicu celkového zníženia.

## Modely, ktoré skončia skôr

Cloudflare testoval aj nastavenia modelov a úrovní uvažovania namiesto predpokladu, že najdrahšia kombinácia je najbezpečnejšia. Zmeny kódu predstavovali 65 centov zo zníženia o 1,67 dolára nameraného v článku; zmeny modelov a úrovne uvažovania 1,06 dolára. Skidmore upozorňuje, že tieto postupné porovnania neboli kontrolovaným experimentom.

Novšie modely potrebovali menej volaní. V dvojapoldňovom rozdelenom teste stál Sonnet 5.5 na jednu kontrolu kvality kódu o 62 % menej než Sonnet 5, pri výkone o 58 % a pri bezpečnosti o 47 % menej, hoci mali rovnakú cenu za token. Pri strednej úrovni uvažovania agent kvality kódu vykonal 1,7 volania modelu namiesto 6,2. Viac než polovicu behov ukončil po jedinom volaní bez otvorenia ďalšieho súboru repozitára.

Vyzeralo to efektívne aj nebezpečne. Kontrolór, ktorý číta menej, môže skončiť lacno preto, že chybu prehliadne.

Cloudflare porovnal vysokú a strednú úroveň uvažovania. Vysoká stála pri kontrole kvality kódu o 61 % viac a vytvorila o 58 % viac kritických zistení alebo varovaní. Rozdiel predstavoval približne dva centy na kontrolu. Tím pri tomto agentovi obnovil vysokú úroveň, kým ďalší špecialisti zostali na strednej do ďalších testov.

Menej volaní skrátilo čakanie. Medián kontroly klesol zo štyroch minút a deviatich sekúnd na jednu minútu a 32 sekúnd. 99. percentil klesol z 15 minút 20 sekúnd na štyri minúty 41 sekúnd. Podiel kontrol dlhších než päť minút sa znížil z 37,9 na 0,7 %.

## Kontrola toho, čo zmizlo

Hrubý počet závažných zistení po zmenách klesol. Kvalita kódu vytvorila o 40 % menej kritických zistení a varovaní, bezpečnosť o 56 % a výkon o 71 %. Cloudflare sa pokúsil odlíšiť odstránený šum od prehliadnutých problémov.

Najprv kontroloval, či inžinieri v ďalšom odoslaní zmenili riadky označené kontrolórom. Pred optimalizáciou autori reagovali na 34 % závažných zistení kvality kódu. Potom reagovali na 59 %. Zistenia boli zriedkavejšie, no pravdepodobnejšie viedli k zmene: po úpravách pripadalo 132 zistení s následnou reakciou na 1 000 kontrol oproti predchádzajúcim 145, čo je podľa Cloudflaru rozdiel v hraniciach chyby. Pri všetkých štyroch kontrolóroch ukazovateľ vzrástol z 229 na 321 na 1 000 kontrol.

Po druhé, modely od dvoch poskytovateľov vyhodnotili zaslepenú vzorku 657 zistení. Nezhody rozhodoval tretí model. Počet dôležitých zistení kvality kódu zostal blízko 0,3 na kontrolu, kým menej závažné, duplicitné a neoveriteľné zistenia ubudli. Jasnejšie kleslo nadsadenie závažnosti: pred zmenami hodnotitelia označili 0,46 kritického zistenia alebo varovania na kontrolu za príliš závažné, po nich 0,14.

Dôkazy neoslobodili každého kontrolóra. Pri strednej úrovni uvažovania výkon stratil približne 64 % dôležitých zistení, čo zodpovedá jednému prehliadnutému dôležitému problému na každých 24 úplných kontrol. Bezpečnosť stratila približne štvrtinu, hoci tento odhad nebol štatisticky významný. Cloudflare uvádza, že vzorky obsahovali iba 35 až 66 zistení v každej skupine, obdobie po zmene trvalo jeden deň a modeloví hodnotitelia nie sú dokonalí. Ani zmena označených riadkov inžinierom nedokazuje správnosť zistenia, iba následnú reakciu.

## Náklady sú výsledkom hodnotenia

Hotový systém stojí v priemere 77 centov na kontrolu, oproti 2,43 dolára počas dvoch najdrahších týždňov. Približne 40 % úspory priniesol kód; zvyšok výber modelov a úrovne uvažovania. Spolu s nákladmi sa zlepšila aj spoľahlivosť: podiel kontrol končiacich bez verdiktu klesol z 0,79 na 0,27 % a opakované pokusy bezpečnostného agenta z 3,5 na 0,04 %.

Širšie ponaučenie Cloudflaru je zložitejšie než „používajte cache promptov“. Firma preskúmala presnú prvú požiadavku prichádzajúcu k poskytovateľovi, zmenila stabilný prefix, zmerala každú úpravu konfigurácie a potom vyhodnotila zistenia, ktoré zmizli. Lacnejší agent môže znamenať čistejší systém, slabší systém alebo oboje v rôznych častiach tej istej pipeline.

Vráťme sa k vymyslenej inžinierke o 16:12. Upravený kontrolór ju zastihne skôr, než opustí merge request, pretože za inštrukcie použiteľné jeho kolegami zaplatil iba raz. Nahlási menej varovaní. Jej úlohou je vedieť, či ticho vzniklo odstránením opakovania alebo tým, že sa model rozhodol nepozerať. Cloudflare ušetril peniaze až potom, čo vytvoril spôsob, ako tieto výsledky odlíšiť.

## Použité zdroje

- Anthropic. (2026). *Pricing*. https://docs.anthropic.com/en/docs/about-claude/pricing
- Skidmore, R. (2026). *Cutting our inference bill by 68% by being obsessive about optimization*. https://blog.cloudflare.com/obsessive-inference-optimization/
- Skidmore, R. (2026). *Orchestrating AI Code Review at scale*. https://blog.cloudflare.com/ai-code-review/

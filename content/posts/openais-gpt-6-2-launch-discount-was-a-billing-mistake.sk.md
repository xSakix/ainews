+++
title = "Zľava pri spustení GPT-6.2 bola podľa OpenAI chybou fakturácie"
slug = "zlava-pri-spusteni-gpt-6-2-bola-chybou-fakturacie"
description = "OpenAI tvrdí, že deväť dní nesprávne zvýhodňovala čerpanie plánov pri modeloch GPT-6.2 Astra a Sol, takže predplatitelia teraz narazia na limity o 40 %, respektíve o 25 % skôr. Oprava prišla spolu s nezávislým meraním, podľa ktorého modely uvažujú menej, a ukazuje, ako málo z paušálneho plánu sa dá overiť zvonka."
tags = ["business", "tools"]
date = 2026-11-27T03:17:17+01:00
draft = false
+++

Pod príspevkom inžiniera OpenAI sa vo vlákne na Hacker News zhromaždili ľudia, ktorí čítali stav svojich meračov využitia. Komentátor s prezývkou seviu napísal, že „včera večer som mal ešte takmer 90 % kvóty a dnes ráno som zistil, že je preč“. Mal plán Pro a cez noc nenechal bežať žiadneho agenta. Ďalší, ragequittah, si minulý týždeň pamätal presne naopak: „6 hodín s Astrou by bolo 3 %.“

Medzi týmito dvoma údajmi stojí samotný príspevok a zmena v tom, ako paušálny plán počíta deň práce.

## Oprava

Dňa 26. novembra o 02:50 UTC napísal na X Thibault Sottiaux, ktorý v OpenAI pracuje na Codexe a ChatGPT: „Pri spustení GPT-6.2 sme urobili chybu vo fakturácii, ktorá nesprávne zvýhodnila čerpanie GPT-6.2 Astra a Sol pre väčšinu používateľov.“ Oprava podľa neho znamená, že „rovnaká práca spotrebuje viac kvóty vášho plánu“. V porovnaní s predchádzajúcim týždňom predplatitelia „narazia na limity o 40 % rýchlejšie pri GPT-6.2 Astra a o 25 % rýchlejšie pri Sol“. Dodal, že modely by mali stále vydržať dlhšie než GPT-6 Astra a GPT-6.1 Sol, že ostatných modelov sa to netýkalo a že OpenAI nebude účtovať rozdiel za minulé používanie. Ako ospravedlnenie dostane každý v plánoch Go, Plus, Pro a Business jeden uložený reset (banked reset).

Čísla treba preložiť. Ak sa kvóta míňa o 40 % rýchlejšie, predplatiteľ z nej dostane asi o 29 % menej úloh, pretože jedna delená 1,4 je 0,71. Pri 25 % rýchlejšom míňaní je to o 20 % menej. Ide o výpočet z formulácie OpenAI a spoločnosť nezverejnila skutočnú sadzbu.

Spustenie bolo staré deväť dní. OpenAI uviedla GPT-6.2 Astra a Sol 17. novembra, ako uvádza dátum, ktorý GitHub zverejnil pri ich pridaní do Copilota. Oznámenie predávalo dvojicu čiastočne ako úsporu: oba modely podľa neho „prinášajú lepšie výsledky pri náročných úlohách s menším počtom výstupných tokenov, takže v rámci svojich limitov využitia zvládnete viac práce“ a Sol „umožňuje dokončiť viac úloh v rovnakom platenom pláne“. V API znížila OpenAI ceny tokenov pri Astre o 20 %, na 8 dolárov za milión vstupných tokenov a 40 dolárov za milión výstupných, čo je rovnaký cenník, aký mala 9. novembra nastavený Anthropic pre Claude Fable 5.2. Sol ponechal ceny GPT-6.1 Sol, teda 2 a 10 dolárov.

Ceny v API sa nezmenili. Platený plán ChatGPT sa účtuje v inej mene, ako podiel na kvóte, a sadzbu, ktorou ju úloha spotrebúva, určuje OpenAI interne. Cenová stránka OpenAI, ktorú sme čítali 27. novembra, uvádza kredity na milión tokenov: 200 za vstup Astry a 1 000 za výstup, teda o pätinu menej než pri GPT-6 Astra (250 a 1 250), a nezmenených 50 a 250 pri Sol. Pre predplatiteľov plánu Plus tiež uvádza odhad 6 až 50 lokálnych správ Codexu na päťhodinové okno pri GPT-6.2 Astra a 17 až 180 pri Sol, oproti 5 až 45 pri GPT-6 Astra a 15 až 160 pri GPT-6.1 Sol. Stránka označuje tieto odhady za „nie pevné limity správ“. Uvádza, že „plány Pro momentálne nemajú päťhodinový limit“ a že môžu platiť aj týždenné limity.

Rozsah 6 až 50 nedokáže potvrdiť ani vyvrátiť tvrdenie o 40 %. Stránka tiež neuvádza, či sa jej tabuľka po oprave aktualizovala. Nočná strata, ktorú opisuje seviu, je jeden nepotvrdený účet a mohla vzniknúť zmenou alebo týždenným limitom.

## O čom sa vo vlákne diskutovalo

Príspevok, ktorý nadpis vlákna opísal ako zníženie využitia, získal na Hacker News 468 bodov. Čitatelia sa rozdelili v tom, čo znamená. Niektorí vzali „chybu vo fakturácii“ doslova. Jeden komentátor napísal, že hodiny pracoval s Astrou 6.2 a merač stále ukazoval 100 %, takže sa išiel pozrieť, či nie je pokazený widget. Iní videli v oprave zdraženie prezlečené za opravu chyby a niektorí uviedli, že predplatné zrušili alebo zvažujú Anthropic a Google. Ďalší poznamenal, že e-mail, ktorý OpenAI poslala ako prvý, bol stručný a vysvetlenie muselo prísť v následnom e-maile. Každé z týchto tvrdení je opisom používateľa, nie meraním.

Vlákno prinieslo aj spomienku na striedanie ponúk. Jeden dlhoročný používateľ účtov OpenAI aj Anthropic uviedol, že limity OpenAI pôsobili neobmedzene, s neustálym prílevom resetov, že Opus 5.5 potom ponúkol viac využitia a že OpenAI odpovedala znížením limitov. Iný komentátor mu odpovedal, že rovnováha medzi oboma firmami sa strieda od vzniku tejto kategórie a bude sa striedať aj ďalej. Oba opisy sú spomienky a ani jeden nie je záznamom toho, čo ktorýkoľvek plán skutočne poskytol.

## Druhé čítanie tých istých modelov

Dňa 26. novembra, niekoľko hodín po Sottiauxovom príspevku, zverejnil vývojár stojaci za Agent Duel, vzájomným porovnávaním modelov, príspevok s názvom „OpenAI may be in cost control mode“. Agent Duel je postavený na kódovacom agentovi OpenCode; stavia modely proti sebe na reálnej práci a radí ich podľa skóre Elo. Jeho autor uvádza, že oproti súperom v tých istých súbojoch minuli Astra 6.2 a Sol 6.2 na úlohu menej výstupných tokenov aj menej tokenov uvažovania než ich predchodcovia. P-hodnoty, ktoré uvádza, sú pri výstupných tokenoch 0,0055 pre Sol a 0,022 pre Astru; pri tokenoch uvažovania 0,00013 pre Sol a 0,0064 pre Astru. Dospel k záveru, že modely „vyzerajú byť vyladené na úsporu nákladov“, a to do miery, že ide o „odľahlé prípady, ktoré uvažujú primálo“.

Slovo „náklady“ patrí autorovi. Údaje ukazujú menej uvažovania, nie dôvod. Úvodný príspevok OpenAI uvádza menej výstupných tokenov ako prednosť a tvrdí, že Astra si v internom benchmarku GDPval v2 polepšila o 6,2 bodu a pritom použila o 22 % menej výstupných tokenov než GPT-6 Astra. Rovnaké meranie môže podporiť príbeh o efektivite aj príbeh o šetrení a len OpenAI vie, ktorý je pravdivý. Nižší počet tokenov tiež nevysvetľuje chybu vo fakturácii, ktorá sa týkala toho, ako sa tokeny účtujú voči kvóte.

Ani samotný rebríček, vygenerovaný 27. novembra o 03:00 UTC, nie je rozhodujúci. GPT-6.2 Astra je piata so skóre Elo 1007 a intervalom plus mínus 61, pri 2,33 dolára na úlohu a 2,6 minúty; Sol je dvanásty s 937, 0,43 dolára a 1,7 minúty. Claude Fable 5.2 vedie s 1069 a 3,49 dolára a Claude Opus 5.5 nasleduje s 1060 a 1,63 dolára. Intervaly sa výrazne prekrývajú a pravdepodobné umiestnenie Astry siaha od druhého po jedenáste miesto.

## Čo si môže predplatiteľ overiť

Cena a účet sa už rozišli aj predtým. Dňa 9. novembra Anthropic znížil cenu Fable 5.2 na 8 a 40 dolárov za milión tokenov, teda o pätinu pod predchodcu, a Artificial Analysis model napriek tomu radí na posledné miesto v nákladoch spomedzi modelov, ktoré hodnotí, s 26,54 dolára na úlohu v indexe Intelligence Index, pretože účet sa riadi tým, koľko tokenov sa model rozhodne minúť. Prípad OpenAI pridáva ďalšiu vrstvu. Pre predplatiteľa sú tokeny, ktoré model minie, sadzba, ktorou sa účtujú voči kvóte, a veľkosť kvóty tri čísla určené poskytovateľom a jedno z nich, účtovaciu sadzbu, podľa OpenAI v prvých deviatich dňoch pokazila.

Prvé môžu zvonka merať aj iní, ako to urobil Agent Duel. Zvyšné dve vidno len na merači. Cenová stránka ponúka človeku pred prázdnym meračom jedinú vetu: „Úlohy, ktoré vyzerajú podobne, môžu spotrebovať rôzne množstvo vašej kvóty.“

## Použité zdroje

- Agent Duel (2026). *Agent Duel Leaderboard*, generated 27 November 2026. https://agentduel.com/leaderboard
- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- GitHub (2026). *OpenAI's GPT-6.2 Astra and GPT-6.2 Sol now available*. GitHub Changelog, 17 November. https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available
- Hacker News (2026). *OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster*. https://news.ycombinator.com/item?id=50651117
- micjm (2026). *OpenAI may be in cost control mode*. https://micjm.com/blog/openai-is-in-cost-control-mode/
- OpenAI (2026). *Introducing GPT-6.2 Astra and Sol*. https://openai.com/index/introducing-gpt-6-2-astra-sol
- OpenAI (2026). *Pricing*. ChatGPT Learn. https://learn.chatgpt.com/docs/pricing
- Sottiaux, T. (2026). Post on X about the GPT-6.2 billing mistake, 26 November. https://x.com/thsottiaux/status/2125784147889393806

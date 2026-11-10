+++
title = "Fable 5.2 znížil cenník, účet však určuje úroveň uvažovania"
slug = "fable-5-2-znizil-cennik-ucet-vsak-urcuje-uroven-uvazovania"
description = "Anthropic znížil cenu modelu Claude Fable 5.2 o pätinu, no nezávislý index pri maximálnej úrovni uvažovania nameral najvyššie náklady na úlohu zo 73 modelov. Rozdiel vzniká počtom tokenov, ktoré model spotrebuje, a podľa vlastných grafov Anthropicu o ňom rozhoduje nastavenie úrovne uvažovania."
tags = ["models", "business"]
date = 2026-11-10T03:25:07+01:00
draft = false
+++

Tento pondelok je vymyslený, poskladaný zo spúšťacích dokumentov, nie z ničieho denníka. Vedúca platformového tímu v strednej softvérovej firme sa dočíta, že Anthropic znížil cenu svojho najvýkonnejšieho modelu o pätinu. Urobí to, k čomu ju oznámenie vyzýva. V konfigurácii agentov svojho tímu zmení názov modelu, parameter úrovne uvažovania nastaví na najvyššiu hodnotu a nechá cez noc bežať štyridsať auditov repozitárov. Ráno je dávka hotová a jediné, čo si chce otvoriť, je faktúra. Nevyzerá tak, ako titulok, ktorý čítala.

Titulok bol presný. Anthropic 9. novembra vydal Claude Fable 5.2 a jeho dvojča Claude Mythos 5.2 za 8 dolárov za milión vstupných tokenov a 40 dolárov za milión výstupných tokenov, po cene 10 a 50 dolárov pri verziách 5.1. Presné je aj nezávislé číslo, ktoré prišlo v ten istý deň. Artificial Analysis, ktorý zverejňuje index inteligencie naprieč dodávateľmi, spustil Fable 5.2 na maximálnom nastavení a zaradil ho na prvé miesto zo 74 modelov v inteligencii, so skóre 65, a na 73. miesto zo 73 v nákladoch, s 26,54 dolára na úlohu indexu. Obe čísla opisujú jeden model. Rozdeľuje ich počet tokenov, ktoré model minie.

## Čo hovorí cenník

Dokumentácia Anthropicu uvádza nové sadzby jasne. Čítanie z cache stojí 0,20 dolára za milión tokenov, dávkové spracovanie stojí polovicu základnej ceny a voliteľný rýchly režim, ktorý generuje až 2,5-krát rýchlejšie, stojí 16 dolárov za vstup a 80 dolárov za výstup. Spoločnosť tiež uvádza, že model produkuje výstup až o 30 % rýchlejšie než Fable 5.1. TechCrunch poznamenáva, že Fable je teraz lacnejší než jeho hlavný konkurent, a Fortune ho radí o 20 % pod GPT-6 Astra od OpenAI, ktorý stojí 10 a 50 dolárov, pričom vstup z cache vychádza na 20 centov oproti jednému doláru pri Astre.

Mythos 5.2 má rovnakú cenu. Anthropic hovorí o jednom a tom istom modeli: Fable sa dodáva s ochrannými mechanizmami pre kybernetiku a biológiu a je otvorený všetkým zákazníkom, kým Mythos dostanú organizácie prijaté do overovacích programov spoločnosti pre kybernetiku a vedy o živej prírode. Cena je spoločná. Prístup nie.

## Čo namerali v indexe

Artificial Analysis počíta náklady na úlohu z cien vstupných tokenov, tokenov čítaných z cache, zápisu do cache, tokenov uvažovania a tokenov odpovede, vydelených počtom úloh a vážených naprieč deviatimi hodnoteniami v jeho indexe. Na tomto základe Fable 5.2 pri maximálnej úrovni uvažovania vygeneroval 275 miliónov výstupných tokenov, kým medián porovnateľných modelov je 72,8 milióna. Na úlohu potreboval 46,4 minúty oproti mediánu 12,7 a na prvý token odpovede 216 sekúnd. Vlastné zhrnutie stránky označuje model za „particularly expensive“ („mimoriadne drahý“) a „very verbose“ („veľmi rozvláčny“).

Výpočet je krátky. Cena výstupu je 40 dolárov oproti mediánu 10, teda štvornásobok, a počet tokenov je asi 3,8-krát väčší než medián. Účet je cena krát objem a Fable 5.2 je pri tomto nastavení vysoko v oboch. Hranice treba povedať: ide o úlohy Artificial Analysis, nie čitateľove, a údaj patrí jednej úrovni uvažovania.

## Ovládač, na ktorý ukazuje Anthropic

Anthropic nespochybňuje, že úroveň uvažovania záleží. Jeho stránka o vydaní uvádza, že predvolená hodnota v aplikáciách Claude a v Claude Code je Medium a že na nej Fable 5.2 zvláda ťažké úlohy s menším počtom tokenov než 5.1. V ranom testovaní na FrontierCode 2.0, benchmarku, ktorý meria, či by zmeny kódu od modelu schválili správcovia open-source projektov, dosiahol Fable 5.2 na úrovni High 45,3 % oproti 45,5 % pri Opuse 5.5 na úrovni Max, približne za polovicu nákladov na úlohu. Na dátovom benchmarku WANDR od Perplexity zodpovedá úroveň Medium najlepšiemu skóre Opusu 5.5 za asi 40 % nákladov. Na Humanity's Last Exam to dosiahne úroveň Low za menej než desatinu. Na úrovni Xhigh model dosahuje na FrontierCode 49,1 %, najviac zo všetkých vydaných modelov, ktoré Anthropic testoval.

Všetko sú to grafy samotného dodávateľa z ranného testovania. Ukazujú, že ten istý model sa podľa jediného parametra ocitá na veľmi odlišných miestach krivky nákladov, čo podporuje aj nezávislé číslo. Dokumentácia je o tom, kam Fable patrí, priama: pre väčšinu úloh začnite najnovším modelom Opus a na Fable prejdite, keď hodnotenia na Opuse na vyššej úrovni uvažovania stále nezodpovedajú tomu, aby „meet your requirements“ („spĺňali vaše požiadavky“).

## Ako sa účet dostal sem

Anthropic takto o cenách hovoril už predtým. Jeho oznámenie Claude Opus 5.5 z 22. septembra uvádzalo, že model podáva na väčšine práce výkon na úrovni Fable 5.1 a pri typických záťažiach stojí o 40 % menej než Opus 5. Cena za token bola nižšia o 20 %, na 4 a 20 dolároch za milión, a zvyšok úspory podľa spoločnosti priniesla nižšia spotreba tokenov na úlohu. Účet je podľa vlastného opisu Anthropicu sadzba krát počet.

Gergely Orosz, ktorý píše newsletter The Pragmatic Engineer, tomu dal v čísle z 20. októbra konkrétnejšiu podobu. Hovoril s ľuďmi z 27 pracovísk o výdavkoch na AI na vývojára, ide o vzorku, ktorá sa prihlásila sama, väčšinou anonymnú. Uvádza, že výdavky vrcholili v júni a v júli a u firiem na API plánoch sa zhruba prepolovili, pričom ako dôvod väčšina z nich uvádza kombináciu Opusu 5.5 a otvorených modelov. Jeden inžinier minul v septembri 2 200 dolárov na Opuse 5 a s Opusom 5.5 očakáva polovicu. Orosz tiež počul, že u viacerých firiem sa končia dotované predplatné, čo by mohlo ich účty zvýšiť päť- až desaťnásobne.

Fable 5.2 vstupuje do tejto aritmetiky. Kupujúci, ktorý prešiel na Opus 5.5, aby faktúru znížil na polovicu, má teraz k dispozícii vyššiu triedu, ktorej cena za token klesla a ktorej náklady na úlohu závisia od nastavenia, ktorého sa väčšina ľudí nedotýka.

## Úvodné ponuky a kto platí za vyskúšanie

Počas prvého týždňa cena predplatiteľov nepáli. Centrum pomoci Anthropicu uvádza, že plány Pro a štandardné sedenia v pláne Team majú od 9. do 16. novembra všetky modely Fable zahrnuté v týždenných limitoch, až do 50 % týchto limitov, plus jedno obnovenie limitu. Plány Max a Ultra dostanú jedno až tri obnovenia podľa toho, ako dlho je účet platený, a nevyužité obnovenia vypršia 8. marca 2027. Ponuky sú napísané pre predplatné plány a o účtoch API stránka nehovorí.

## Faktúra, znova

V tom vymyslenom pondelku sa vedúca pozrie na dávku auditov a nenájde na zisteniach nič zlé. Chýba jej porovnanie. Ďalší test, ktorý napíše, je nudný: tých istých štyridsať repozitárov na úrovni High, potom na úrovni Medium, s nákladmi a počtom prijatých zistení vedľa každého. Či lacnejšie behy nájdu dosť, je otázka, ktorú jej nijaká stránka o vydaní nerozhodne, a dokumentácia, ktorú čítala, to hovorí tiež. Model sa účtuje po miliónoch tokenov. Jej kontrola sa bude účtovať po repozitároch.

## Použité zdroje

- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Anthropic (2026). *Introducing Claude Opus 5.5*. https://www.anthropic.com/news/claude-opus-5-5
- Anthropic (2026). *Claude Fable 5.2 launch offers*. Claude Help Center. https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
- Anthropic (2026). *What's new in Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- Brandom, R. (2026). *Anthropic releases new Mythos and Fable models amid RSI concerns*. TechCrunch. https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/
- Forlini, E. (2026). *Anthropic debuts Claude Fable, Mythos 5.2 models, priced 20% below OpenAI's GPT-6 Astra*. Fortune. https://fortune.com/2026/11/09/anthropic-debuts-updated-claude-fable-and-mythos-models-undercutting-price-of-openais-gpt-6-astra-by-up-to-80/
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers

+++
title = "Gemini 4 Argon prechádza od obrancov do aplikácie Gemini"
slug = "gemini-4-argon-prechadza-od-obrancov-do-aplikacie"
description = "Trinásť dní po sprístupnení Gemini 4 Argon iba uzavretej skupine kybernetických obrancov Google otvoril svoj vlajkový model platiacim používateľom aplikácie Gemini a vývojárom. Google sľubuje priamejšie odpovede; nezávislé rebríčky ho umiestňujú na prvé aj ôsme miesto."
tags = ["models", "tools", "safety"]
date = 2026-10-13T22:54:03+02:00
draft = false
+++

Účtovníčka v Brne má tri dodávateľské zmluvy, účtovnú knihu exportovanú z programu, ktorý kazí českú diakritiku, a klienta požadujúceho odsúhlasenie do stredy. V utorok večer otvorí aplikáciu Gemini, zo zvyku ťukne na ponuku modelov a vedľa 3.1 Pro a 3.8 Flash nájde meno, ktoré tam ráno nebolo: 4 Argon. Vloží všetky podklady a pridá jediný vlastný riadok: bez úvodu a bez zhrnutia toho, čo som práve uviedla. Pre tento článok sme nikoho s takýmto opisom neoslovili. Je ilustráciou používateľa, ktorého Google teraz oslovuje, človeka, ktorého poznámky k vydaniu vykresľujú pri „analýze zložitej finančnej správy“ alebo „tvorbe prezentácie z roztrúsených zdrojov“.

## Dva týždne od uzavretého programu k aplikácii

Google začal 13. októbra podľa poznámok k vydaniu globálne sprístupňovať Gemini 4 Argon predplatiteľom Google AI Pro a Ultra v aplikácii Gemini. V ten istý deň bol model všeobecne dostupný v Gemini API ako gemini-4-argon, otvoril sa v Google AI Studio a Android Studio a pribudol do programovacích nástrojov Antigravity pre predplatiteľov Ultra a oprávnených zákazníkov Gemini Enterprise. 9to5Google uviedol, že používatelia Pro a Ultra si ho môžu vybrať aj v AI Mode vo Vyhľadávaní Google. Bezplatní používatelia ani predplatitelia lacnejšieho AI Plus ho zatiaľ nemajú, uviedol Android Police; jeho recenzent s Pro ešte čakal, kým sa model objaví.

O trinásť dní skôr bol okruh oveľa menší. Keď Koray Kavukcuoglu, senior viceprezident Google DeepMind a hlavný AI architekt Googlu, 30. septembra oznámil Argon, model dostala iba „skupina dôveryhodných kybernetických obrancov“ v programe Fairwind. Google uviedol účasť v dobrovoľnom procese vlády USA na prístup k modelom pred vydaním a ďalšiu prácu na ochranných mechanizmoch pred otvorením Argonu vývojárom, firmám a spotrebiteľom, začínajúc platiacimi zákazníkmi API a Ultra. Utorkové vydanie zašlo ďalej a zahrnulo Pro.

Fairwind je len o málo starší než model. Viceprezident Googlu pre bezpečnosť a súkromie Four Flynn ho spustil 2. septembra ako program s obmedzeným prístupom pre vlády, prevádzkovateľov kritickej infraštruktúry a bezpečnostné firmy, postavený okolo menšieho Gemini 3.8 Flash Cyber a nástroja CodeMender. Účastníci držia prístup v bezpečnostných, incident-response alebo penetračných tímoch. Google uvádza viac než 650 partnerov.

## Čo sa podľa Googlu zmenilo pre píšuceho človeka

Oznámenie aplikácie je krátke a väčšinou opisuje spôsob odpovedania. Argon podľa Googlu odpovedá priamočiarejšie s menším váhaním, zbytočne sa neopakuje a vynecháva klišé. Pri dlhších úlohách častejšie a účinnejšie informuje o postupe. Podľa 9to5Google spoločnosť tvrdí aj spoľahlivejšie dodržiavanie štýlových pokynov než pri starších Gemini.

Prišli aj ďalšie zmeny. Prepínač v hlavnom okne mení chat na tasks, režim, v ktorom môže Gemini podľa Googlu pracovať aj bez používateľa pri počítači. Pripojiť možno viac než 40 služieb vrátane Instacart, OpenTable, Adobe a Shopify, hoci väčšina podľa poznámok funguje iba v angličtine v USA. Na Macu sa agentové rozhranie Antigravity nachádza v aplikácii Gemini: používateľ schváli plán programovacieho agenta, vráti sa do chatu a dostane upozornenie po vytvorení a otestovaní kódu na pozadí.

Za spotrebiteľskou prezentáciou je septembrové tvrdenie Googlu o dlhej práci. Výstupný limit Argonu stúpol zo 64 000 na milión tokenov, čo má umožniť stovky tisíc tokenov v jednej trajektórii. Dokumentácia uvádza presnejšie 65 536 výstupných tokenov predvolene a až 1 048 576 v režime long decode v spoločnom vstupno-výstupnom okne rovnakej veľkosti.

## Umiestnenie v externých rebríčkoch

Google uvádza 77,9 % na DeepSWE v1.1, 51,3 % na AutomationBench od Zapieru a 91,7 % na benchmarku dlhého videa LVBench. Na CWE-bench v1 má Argon podľa Googlu remizovať o prvé miesto so 68 %. Sú to čísla dodávateľa. VentureBeat uviedol, že na Terminal-Bench 4.0 dosiahol Claude Opus 5.5 od Anthropicu 66,4 % oproti 57,4 % Argonu.

Dva nezávislé rebríčky sa nezhodujú, aký veľký je náskok. Vals AI, ktorého index váži finančné, programovacie, právne a daňové úlohy podľa podielu sektorov na HDP USA, zaradil 13. októbra Argon na prvé miesto so 68,90 %, pred Claude Sonnet 5.5 so 67,04 a Claude Opus 5.5 so 66,97. Artificial Analysis dal nastaveniu high-effort 53 bodov na Intelligence Index, ôsme miesto z 216 modelov. Náskok vo Vals je pod dva body a v Artificial Analysis Argon nevedie.

Stránka Artificial Analysis uvádza číslo, ktoré je v napätí so sľubom menšieho množstva slov. Argon pri indexe vytvoril 110 miliónov výstupných tokenov oproti mediánu 85 miliónov a stránka ho označuje za „somewhat verbose“. Odpoveď čítaná používateľom a práca potrebná na jej vytvorenie sú samostatné merania; sľub Googlu sa týka prvého.

## Ochranné mechanizmy verejnej verzie

Google povedal viac o ochranných mechanizmoch než externí testeri o modeli. Úvodný príspevok uvádza odmietanie pomoci s kybernetickými útokmi a chemickými, biologickými, rádiologickými či jadrovými zbraňami, sledovanie vnútorných aktivácií pri zneužití a samostatný systém čítajúci chain-of-thought a akcie, ktorý môže model zastaviť pri prekročení zámeru používateľa. Dôveryhodným obrancom a vlastným tímom Google sprístupňuje Argon „without cyber guardrails“. Predplatitelia dostávajú chránenú verziu.

Vlády model skúmali pred širším vydaním. Okrem procesu USA britský minister pre AI Kanishka Narayan 12. októbra v Londýne uviedol, že vedci AI Security Institute dôkladne hodnotia najnovšie generácie modelov, pričom menoval Gemini, informoval Guardian. Správa neuvádza verziu. Ona ani Google nezverejňujú výsledky alebo zmeny modelu po hodnotení.

## Cena a úloha určená Argonu

Vývojári do 30. novembra platia úvodné 2 doláre za milión vstupných tokenov a 10 dolárov za milión výstupných, pričom cached input je o 95 % lacnejší. Od 1. decembra sa podľa VentureBeat a 9to5Google cena zdvojnásobí na 4 a 20 dolárov.

Príspevok tímu Antigravity rámcuje vydanie vetou: „While Argon is designed to tackle your hardest problems,“ píše, „we're equally excited about future models that can be used as everyday drivers for an even broader range of builders.“ Argon umiestňuje na dlhý a drahý koniec práce a každodenné použitie necháva budúcim modelom.

Dôkazy Googlu o tomto dlhom konci pochádzajú zvnútra firmy. Uvádza, že viac než 100 000 ľudí v Alphabete používa Argon mesačne v internej Antigravity a za štyri týždne množstvo kódu od agentov stúplo o 35 %, kým rollbacky po odovzdaní klesli o 30 %. V jednom príklade Argon auditoval zmeny riadenia prístupu a našiel štyri kritické bezpečnostné chyby v kóde, ktorý dva staršie frontier modely označili za čistý. Google modely nemenoval ani audit nezverejnil; ide o vlastný opis vlastnej práce.

V Brne dostane naša vymyslená účtovníčka poznámku v štyroch krátkych odsekoch bez úvodného komplimentu a rekapitulácie vloženého textu. Súčet napriek tomu skontroluje s účtovnou knihou riadok po riadku, rovnako ako vtedy, keď ponuka končila pri 3.1 Pro.

## Použité zdroje

- Artificial Analysis. (2026). *Gemini 4 Argon (High): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/gemini-4-argon
- Bhatia, S. (2026). *Gemini 4 Argon is here, and Google says it'll finally cut down on the AI fluff*. Android Police. https://www.androidpolice.com/gemini-4-argon-available-pro-ultra-subscribers/
- Flynn, F. (2026). *Proactive cyber defense for governments and enterprises*. Google. https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- Franzen, C. (2026). *Google makes Gemini 4 Argon broadly available with limited-time low API pricing of $2/$10 per 1M token*. VentureBeat. https://venturebeat.com/technology/google-makes-gemini-4-argon-broadly-available-with-limited-time-low-api-pricing-of-2-10-per-1m-token
- Google. (2026). *Gemini 4 Argon comes to the Gemini app*. https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- Google. (2026). *Gemini 4 Argon is now available for developers*. https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/
- Google. (2026). *Gemini Apps' release updates & improvements*. https://gemini.google/release-notes/
- Google AI for Developers. (2026). *Gemini 4 Argon*. https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Google AI for Developers. (2026). *Gemini API release notes*. https://ai.google.dev/gemini-api/docs/changelog
- Google Antigravity Team. (2026). *Gemini 4 Argon in Google Antigravity*. https://antigravity.google/blog/gemini-4-argon-in-google-antigravity
- Kavukcuoglu, K. (2026). *Gemini 4 Argon: our next era of frontier intelligence*. Google. https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- Li, A. (2026). *Gemini app rolling out Gemini 4 Argon to AI Pro and AI Ultra*. 9to5Google. https://9to5google.com/2026/10/13/gemini-app-4-argon/
- Milmo, D. (2026). *Cyber-attack similar to OpenAI Medicare breach seems likely in UK, says minister*. The Guardian. https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister
- Vals AI. (2026). *Vals Index*. https://www.vals.ai/benchmarks/vals_index

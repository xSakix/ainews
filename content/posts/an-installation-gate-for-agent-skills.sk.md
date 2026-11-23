+++
title = "Inštalačná brána pre skilly agentov"
slug = "instalacna-brana-pre-skilly-agentov"
description = "ClawVet skontroluje skill agenta a jeho skripty pred inštaláciou a potom upozorní, keď aktualizácia získa prístup k novým tajomstvám, hostiteľom alebo cestám na trvalé spúšťanie. Benchmarky ukazujú, že statické kontroly zachytia mnohé útoky, no manipuláciu promptom treba stále hodnotiť sémanticky."
tags = ["agents", "safety", "tools"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

Skill v prípravnom adresári vyzeral bežne. Jeho súbor Markdown opisoval užitočnú skratku a vedľa neho ležal pomocný skript. Skôr než inštalátor stihol oba súbory skopírovať medzi nástroje agenta, samostatný proces otvoril balík, vysledoval cestu tajomstva z premennej prostredia do odchádzajúcej požiadavky a vrátil rozhodnutie zablokovať inštaláciu.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

ClawVet vznikol pre túto chvíľu. Open-source skener preverí inštrukcie a kód v skille agenta ešte pred inštaláciou. Štandardne beží offline, balík nespúšťa a svoje rozhodnutie môže vynútiť cez inštalačné pravidlá OpenClaw. Zároveň zaznamená oprávnenia povolenej verzie, takže neskoršia aktualizácia nemôže bez nového upozornenia potichu pridať prístup k prihlasovacím údajom alebo štartovacím súborom.

## Kód zabalený ako inštrukcia

Skill agenta nie je bežná knižnica ani obyčajný dokument. Hlavný súbor hovorí modelu, kedy má skill použiť a čo má urobiť. Balík môže obsahovať aj skripty, konfiguráciu, referenčné materiály a ďalšie súbory. Táto kombinácia vytvára problém dodávateľského reťazca v dvoch jazykoch: text môže presmerovať agenta a kód môže konať cez používateľský účet.

ClawVet preto balík vníma oboma spôsobmi. Prvý priechod spracuje hlavný súbor, bloky kódu a súbory, na ktoré inštrukcie odkazujú. Statické pravidlá potom hľadajú vzdialené spustenie kódu, reverse shell, krádež prihlasovacích údajov, ťažbu kryptomien, zahmlievanie a odosielanie dát. Parsery Tree-sitter sledujú tok dát v Pythone, JavaScripte, TypeScripte a shelli bez spúšťania kódu. Ďalšie priechody kontrolujú neuvedené programy a premenné prostredia, rizikové príkazy na závislosti a názvy podobné obľúbeným skillom.

Šesť zo siedmich priechodov je statických a lokálnych. Voliteľný siedmy odošle statické zistenia a medzery v pokrytí jazykovému modelu, ktorý si vyberie prevádzkovateľ. Sémantický hodnotiteľ môže medzeru uzavrieť iba citátom zo skillu, pričom závažné bezpečnostné nálezy zostávajú minimom, ktoré model nemôže znížiť. Rozdiel je dôležitý, pretože označenie „bezpečnostné skenovanie pomocou AI“ môže inak zakryť, že zdrojový kód opúšťa zariadenie.

Nástroj prevádza nálezy na skóre od nuly do 100. Hodnoty do 25 dostanú známku A alebo B a prejdú. Hodnoty od 26 do 75 vyvolajú varovanie, ktoré zastaví bezobslužnú inštaláciu. Skóre od 76 vyššie vedie k blokovaniu. Známa adresa riadiaceho servera alebo nečitateľný obsah zablokujú inštaláciu pri každom prahu.

## Zmeny oprávnení, nielen známe vzory

Statické signatúry fungujú najlepšie pri útoku, ktorý už má rozpoznateľný tvar. Aktualizácie predstavujú iný problém. Užitočný skill si môže získať dôveru a v neskoršej verzii získať jedno nové oprávnenie.

ClawVet preto zisťuje schopnosti balíka: pripojené weby, tajné premenné prostredia, úložiská prihlasovacích údajov, miesta na trvalé spúšťanie a preukázané rizikové kroky. Inštalačná brána uloží tento záznam do lokálneho stavu. Keď príde verzia od rovnakého vlastníka s rovnakým názvom, brána ich porovná. Nové čítanie tajomstva, cesta na trvalé spúšťanie alebo rizikový cieľ zmení rozhodnutie na varovanie a pomenuje nové oprávnenie.

Takýto návrh obchádza bežné zlyhanie kontrolných systémov. Kontrolór nemusí znova čítať celý balík a pamätať si, čo vedela stará verzia. Otázka je užšia: prečo aktualizácia potrebuje heslo, ktoré predchádzajúca verzia nikdy nečítala, alebo hostiteľa, ku ktorému sa nikdy nepripájala?

Porovnanie má hranice. ClawVet rozpoznáva doslovné cesty, bežné zástupné premenné a viaceré formy skladania príkazov, nejde však o všeobecný dôkaz správania programu. Dokumentácia uvádza, že textová inštrukcia, ktorá agentovi prikáže načítať web a nasledovať jeho pokyny, môže uniknúť statickej analýze, ak sa nestiahne súbor. Pravidlá môžu obísť aj zahmlené loadery a nepodporované správanie pri spustení. Úplné pokrytie znamená, že skener v rámci limitov súborov a adresárov preskúmal odkazy, ktoré rozpoznal; necertifikuje bezpečnosť.

## Čo hovoria merania

Projekt uvádza výsledky na pri trénovaní nepoužitej časti benchmarku SkillTrustBench v1.1. Benchmark predstavuje skilly ako balíky s hlavným súborom inštrukcií a voliteľnými skriptmi, referenčnými materiálmi, súbormi a definíciami agentov. Rebríčková podmnožina s 556 prípadmi obsahuje 316 škodlivých, 74 podozrivých a 166 normálnych príkladov.

Statická brána ClawVetu dosiahla na tejto množine presnosť 0,660 a macro F1 0,511. S modelom Claude Haiku 5.5 ako voliteľným sémantickým hodnotiteľom presnosť vzrástla na 0,833 a macro F1 na 0,770. Citlivosť na škodlivé prípady dosiahla 0,918. Projekt tieto výsledky porovnáva so zverejnenými hodnotami 0,775 pre Cisco Skill Scanner, 0,712 pre NVIDIA SkillSpector a 0,874 pre Tencent A.I.G. Keďže sémantické konfigurácie, prompty a implementácie sa môžu líšiť, tabuľka je dôkazom na jednom datasete, nie všeobecným rebríčkom.

Rozdiel medzi statickými a sémantickými výsledkami je rovnako dôležitý ako vyššie skóre. Analýza kódu môže dokázať, že prihlasovací údaj preteká do sieťového volania. Ťažšie posúdi textovú inštrukciu, ktorej škodlivosť závisí od zámeru. Benchmark aktualizácií túto slabinu pomenúva priamo: brána spolu s porovnaním oprávnení zastavila na pri trénovaní nepoužitej množine 95,2 % zmien s vloženým škodlivým kódom, no iba 36,4 % manipulácií promptom.

Rovnaký benchmark meral aj prekážky pre bežné používanie. Pri neškodných aktualizáciách sa v spoločnom procese brány a porovnania zastavilo 34,1 %, hoci iba 5,1 % vyvolalo upozornenie priamo pre zmenu oprávnení. V 212 jedinečných skilloch z ClawHubu znížila novšia verzia ClawVetu počet úplných blokovaní zo 79 na 37 a počet čistých povolení zvýšila z 87 na 139. Tieto hodnoty pochádzajú z vlastného korpusu a označení projektu.

Staršie testy ukazujú, prečo sú starostlivé označenia dôležité. Korpus s 500 položkami obsahoval 50 skillov z jednej škodlivej kampane, 400 čistých skillov a 50 náročných negatívnych príkladov. Medzi ne patrili legitímni pomocníci pre SSH, ktorí čítali konfiguráciu, aj inštalátory s príkazmi používanými tiež pri útokoch. Skener, ktorý bez rozlišovania blokuje každú zmienku o prihlasovacom údaji alebo shelli, by vyzeral bezpečne, no znemožňoval by bežnú prácu.

## Brána s vymedzenou hranicou

ClawVet môže bežať v prehliadači cez WebAssembly, ako skener v príkazovom riadku, v kontrolách pred commitom alebo ako GitHub Action. Najprísnejšou úlohou je inštalačná brána. OpenClaw pripraví balík, odošle metadáta procesu s pravidlami a pred dokončením inštalácie čaká na jedno rozhodnutie vo formáte JSON. Chybná požiadavka alebo zlyhanie skenera vedie k zablokovaniu.

Projekt odporúča nainštalovať skener globálne namiesto spúšťania čerstvého balíka cez `npx`. Odporúčanie vychádza z rovnakého modelu hrozieb: príkaz, ktorý pri kontrole načíta najnovšie vydanie z registra, vytvára ďalšiu nepreverenú aktualizáciu. Globálnu kópiu možno aktualizovať zámerne a predtým overiť atestáciu npm.

Brána neruší potrebu skúmať citlivé rozšírenia agentov. Mení však kontrolu na povinný krok a pri zastavení inštalácie zanechá overiteľný dôvod. Zverejnené hranice zároveň ukazujú zostávajúcu voľbu: statický režim ponechá balík lokálne, no prehliadne viac sémantických útokov; voliteľná kontrola modelom lepšie číta zámer, ale odošle vybrané dôkazy modelovému endpointu.

Zablokovaný skill zostal v prípravnom adresári iba ako priečinok. Inštalátor vypísal tajomstvo, ktoré sa skript pokúsil čítať, cieľ, ktorý ho mal prijať, aj pravidlo, ktoré zabránilo kopírovaniu. Agent nedostal príležitosť rozhodnúť, že skratka vyzerá užitočne.

## Použité zdroje

- CUHK Zhuque. (2026). *SkillTrustBench*. https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench
- Shaikh, M. (2026). *ClawVet*. https://github.com/MohibShaikh/clawvet

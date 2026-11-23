+++
title = "Inštalačná brána pre skilly agentov"
slug = "instalacna-brana-pre-skilly-agentov"
description = "ClawVet pred inštaláciou skontroluje skill agenta a jeho skripty a upozorní, keď aktualizácia získa prístup k novým tajným údajom, serverom alebo cestám na trvalé spúšťanie. Jeho benchmarky ukazujú, že statické kontroly zachytia mnohé útoky, no prompt injection si stále vyžaduje sémantické posúdenie."
tags = ["agents", "safety", "tools"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

V prípravnom adresári pôsobil skill celkom nenápadne. Jeho súbor Markdown opisoval užitočnú skratku a hneď vedľa ležal pomocný skript. Skôr než inštalátor stihol oba súbory skopírovať do pracovnej sady agenta, samostatný proces otvoril balík, vystopoval tajný údaj z premennej prostredia až k odchádzajúcej sieťovej požiadavke a vrátil blokovanie.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Práve pre takúto chvíľu vznikol ClawVet. Tento open-source skener pred inštaláciou preverí pokyny aj kód vnútri skillu agenta. Predvolene beží offline, balík nespúšťa a svoje rozhodnutie dokáže vynútiť cez inštalačné pravidlá systému OpenClaw. Zároveň si zapamätá oprávnenia povolenej verzie, takže neskoršia aktualizácia nemôže potichu pridať prístup k prihlasovacím údajom či súborom spúšťaným pri štarte bez ďalšieho upozornenia.

## Kód zabalený do pokynov

Skill agenta nie je ani bežná knižnica, ani obyčajný dokument. Jeho hlavný súbor modelu hovorí, kedy má skill použiť a čo má urobiť. Balík však môže obsahovať aj skripty, konfigurácie, referenčné súbory a ďalšie podklady. Táto kombinácia vytvára problém dodávateľského reťazca v dvoch rovinách: textové pokyny môžu agenta presmerovať inam, zatiaľ čo kód dokáže konať s oprávneniami používateľského účtu.

ClawVet pristupuje k balíku v oboch týchto rovinách. V prvom prechode rozoberie hlavný súbor, bloky kódu aj súbory, na ktoré sa pokyny odvolávajú. Statické pravidlá potom hľadajú vzdialené spúšťanie kódu, reverzné shelly, krádež prihlasovacích údajov, ťažbu kryptomien, obfuskáciu a vynášanie dát. Analyzátory Tree-sitter sledujú tok údajov cez kód v jazykoch Python, JavaScript, TypeScript a shell bez toho, aby ho spustili. Ďalšie prechody preverujú nedeklarované programy a premenné prostredia, rizikové príkazy na správu závislostí a názvy napodobňujúce obľúbené skilly.

Šesť zo siedmich prechodov je statických a lokálnych. Voliteľný siedmy posiela statické nálezy a nepokryté miesta veľkému jazykovému modelu (LLM), ktorý si zvolí prevádzkovateľ. Sémantický hodnotiteľ môže nepokryté miesto uzavrieť len tak, že odcituje konkrétne miesto zo skillu, zatiaľ čo závažné bezpečnostné nálezy tvoria spodnú hranicu, ktorú hodnotiteľ nemôže znížiť. Toto rozlíšenie je dôležité, pretože označenie „bezpečnostné skenovanie pomocou AI“ môže inak zakrývať fakt, že zdrojový kód opúšťa počítač.

Nástroj zhrnie nálezy do skóre od nuly do 100. Výsledky do 25 dostanú známku A alebo B a prejdú. Skóre od 26 do 75 vyvolá varovanie, ktoré zastaví bezobslužnú inštaláciu. Od 76 nahor nasleduje blokovanie. Známa riadiaca adresa útočníkov (command-and-control) alebo nečitateľný obsah zablokujú balík bez ohľadu na prahové skóre.

## Zmeny oprávnení, nielen známe vzorce

Statické signatúry fungujú najlepšie pri útoku, ktorý už má rozpoznateľnú podobu. Aktualizácie však prinášajú iný problém. Užitočný skill si môže získať dôveru a v neskoršej verzii si pribrať jedno oprávnenie navyše.

ClawVet preto z balíka vyťahuje jeho schopnosti: kontaktované domény, tajné premenné prostredia, úložiská prihlasovacích údajov, miesta na trvalé spúšťanie a preukázané vysoko rizikové operácie. Inštalačná brána si tento záznam uloží do lokálneho stavu. Keď dorazí nová verzia od toho istého autora a s rovnakým označením, brána obe verzie porovná. Nové čítanie tajného údaja, cesta na trvalé spúšťanie alebo rizikový cieľ zmenia výsledok na varovanie a pomenujú nové oprávnenie.

Takýto návrh odstraňuje častú slabinu kontrolných procesov. Kontrolór nemusí čítať celý balík odznova a pamätať si, čo smela robiť predchádzajúca verzia. Otázka sa zúži na podstatu: prečo táto aktualizácia potrebuje heslo, ktoré predchádzajúca nikdy nečítala, alebo server, ktorý predtým nikdy nekontaktovala?

Toto porovnávanie má svoje hranice. ClawVet rozpozná doslovné cesty, bežné zástupné znaky aj viaceré spôsoby skladania príkazov, no nepredstavuje všeobecný dôkaz správania programu. Jeho dokumentácia uvádza, že textové pokyny, ktoré agentovi prikážu stiahnuť webovú stránku a riadiť sa jej inštrukciami, môžu statickej analýze uniknúť, ak sa neuloží žiadny súbor. Mimo pravidiel môžu prejsť aj obfuskované zavádzače a nepodporované správanie za behu. Úplné pokrytie znamená, že skener preveril rozpoznané odkazy v rámci svojich limitov pre súbory a adresáre; nie je to certifikát bezpečnosti.

## Čo hovoria merania

Projekt zverejňuje výsledky na pri trénovaní nepoužitej (held-out) podmnožine porovnávacieho testu (benchmarku) SkillTrustBench v1.1. Tento benchmark predstavuje skilly ako balíky s hlavným súborom pokynov a voliteľnými skriptami, referenciami, podkladmi a definíciami agentov. Jeho rebríčková podmnožina s 556 prípadmi obsahuje 316 škodlivých, 74 podozrivých a 166 bežných príkladov.

Statická brána nástroja ClawVet dosiahla na tejto množine presnosť 0,660 a makro F1 na úrovni 0,511. S modelom Claude Haiku 5.5 ako voliteľným sémantickým hodnotiteľom stúpla presnosť na 0,833 a makro F1 na 0,770. Úplnosť (recall) pri škodlivých prípadoch dosiahla 0,918. Projekt tieto čísla porovnáva so zverejnenými výsledkami v rebríčku: presnosť 0,775 pre Cisco Skill Scanner, 0,712 pre NVIDIA SkillSpector a 0,874 pre Tencent A.I.G. Keďže sémantické nastavenia, prompty a implementačné voľby sa môžu líšiť, tabuľka predstavuje doklad na jednom datasete, nie univerzálny rebríček.

Rozdiel medzi statickými a sémantickými výsledkami je rovnako dôležitý ako samotné vyššie skóre. Analýza kódu dokáže dokázať, že prihlasovací údaj tečie do sieťového volania. Oveľa horšie si poradí s pokynom v prirodzenom jazyku, ktorého škodlivosť závisí od zámeru. Benchmark aktualizácií tohto projektu túto slabinu pomenúva priamo: na pri trénovaní nepoužitej množine zastavili brána a diff oprávnení 95,2 % zmien so vkladaním kódu, ale len 36,4 % zmien s prompt injection (podvrhnutím pokynov v texte).

Ten istý benchmark meral aj záťaž pre používateľa. Medzi neškodnými aktualizáciami sa v kombinovanom procese brány a diffu oprávnení v určitom bode stále zastavilo 34,1 % prípadov, hoci len 5,1 % vyvolalo upozornenie priamo pre zmenu oprávnení. V 212 jedinečných skilloch z ClawHub neskoršia verzia nástroja ClawVet znížila počet tvrdých blokovaní zo 79 na 37 a zvýšila počet čistých povolení z 87 na 139. Tieto čísla pochádzajú z vlastného korpusu a označovania projektu.

Staršie testy ukazujú, prečo záleží na dôslednom označovaní prípadov. Korpus s 500 položkami obsahoval 50 skillov z jednej škodlivej kampane, 400 čistých skillov a 50 ťažkých negatívnych príkladov (hard negatives). Medzi ťažké negatívne príklady patrili legitímne pomocné nástroje pre SSH, ktoré čítajú konfiguráciu, a inštalátory využívajúce príkazy známe aj z útokov. Skener, ktorý by jednoducho zablokoval každú zmienku o prihlasovacích údajoch alebo shelle, by pôsobil bezpečne, no znemožnil by bežnú prácu.

## Brána s jasne určenou hranicou

ClawVet dokáže bežať v prehliadači cez WebAssembly, ako skener v príkazovom riadku, v pre-commit kontrolách alebo ako GitHub Action. Jeho prísnejšou úlohou je inštalačná brána. OpenClaw pripraví balík do dočasného adresára, odošle metadáta procesu vyhodnocovania pravidiel a pred dokončením inštalácie čaká na jediné rozhodnutie vo formáte JSON. Chybná požiadavka alebo porucha skenera zlyhá bezpečne do zablokovania (fail-closed).

Projekt používateľom odporúča nainštalovať skener globálne namiesto toho, aby cez `npx` zakaždým sťahovali čerstvý balík. Toto odporúčanie vychádza z jeho vlastného modelu hrozieb: príkaz, ktorý v okamihu kontroly stiahne najnovšiu verziu z registra, vytvára ďalšiu nepreverenú aktualizáciu. Globálnu kópiu možno aktualizovať zámerne a predtým si overiť atestáciu npm.

Brána neodstraňuje potrebu preverovať citlivé rozšírenia agentov. Premieňa však túto kontrolu na povinný krok a zanecháva overiteľný dôvod zakaždým, keď inštaláciu zastaví. Zverejnené obmedzenia zároveň zviditeľňujú voľbu, ktorá zostáva na používateľovi: statický režim udrží balík lokálne, no prehliadne viac sémantických útokov; voliteľná kontrola modelom lepšie rozpozná zámer, ale vybrané dôkazy odosiela na koncový bod modelu.

V prípravnom adresári zostal zablokovaný skill len obyčajným priečinkom. Inštalátor vypísal tajný údaj, ktorý sa skript pokúsil prečítať, cieľovú adresu, kam mal putovať, aj pravidlo, ktoré kopírovanie zastavilo. Agent nikdy nedostal príležitosť usúdiť, že tá skratka vyzerá užitočne.

## Použité zdroje

- CUHK Zhuque. (2026). *SkillTrustBench*. https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench
- Shaikh, M. (2026). *ClawVet*. https://github.com/MohibShaikh/clawvet

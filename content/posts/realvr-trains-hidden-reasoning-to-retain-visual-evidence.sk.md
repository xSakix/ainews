+++
title = "ReaLVR učí skryté uvažovanie zachovať obrazové dôkazy"
slug = "realvr-uci-skryte-uvazovanie-zachovat-obrazove-dokazy"
description = "Štúdia vizuálneho uvažovania skúma informácie uchovávané medzi pohľadom na obrázok a odpoveďou. Jej tréningová metóda zvyšuje citlivosť skrytých stavov na podstatné zmeny obrazu."
tags = ["research", "models"]
date = 2026-10-03T09:44:58+02:00
draft = false
+++

ReaLVR učí skryté kroky uvažovania vizuálno-jazykového modelu zachovať obrazové dôkazy potrebné na odpoveď. Podľa autorov tým zlepšuje presnosť vo všetkých testovaných rodinách modelov.

Xi Xiao z University of Alabama at Birmingham a Amazon AGI spolu s kolegami z Amazon AGI skúma modely, ktoré uvažujú pomocou vnútorných číselných stavov namiesto písaných krokov. Ich [preprint](https://arxiv.org/abs/2609.34563) z 28. septembra sa pýta, či tieto stavy skutočne uchovávajú obrazový detail, ktorý rozhoduje o odpovedi.

**Prečo na tom záleží:** Výskumník vyvíjajúci vizuálne uvažovanie zo samotnej správnej konečnej odpovede nezistí, či model použil rozhodujúci obrazový dôkaz. ReaLVR prepája tréningovú spätnú väzbu s týmto dôkazom vo vnútri modelu a zahŕňa tak do cieľa učenia aj samotný priebežný výpočet.

Najjasnejší problém autori ukazujú na upravených obrázkoch. Zmeny farby, prítomnosti objektu, tvaru alebo vzájomnej polohy zmenili správnu odpoveď približne v štyroch z piatich párov príkladov, no východiskový model zmenil predikciu len asi v 6–13 % prípadov. Veľká časť jeho vnútorného uvažovania zostala necitlivá na podstatnú zmenu.

Východiskový model sa najprv učí s obrazovými cieľmi dodávanými počas tréningu. Neskôr vytvára vlastné skryté stavy a dostáva odmeny za konečnú odpoveď. Podľa autorov mu tento prechod poskytuje príliš málo usmernenia, ktoré obrazové informácie majú tieto samostatne vytvorené stavy zachovať.

ReaLVR pri tréningu používa dve porovnania. Jedno porovnáva relevantnú časť obrázka s obrazovými informáciami z nesúvisiacich príkladov. Druhé porovnáva, ako sa správna odpoveď a vlastné nesprávne odpovede modelu opierajú o skryté stavy. Spoločne určujú, ktoré informácie zachovať a kde posilniť ich reprezentáciu.

Mechanizmus pripomína zlepšovanie pracovných poznámok človeka pri kontrole diagramu: spätná väzba označí detail, ktorý do poznámok patrí, aj poznámku, o ktorú sa konečný záver skutočne opiera. Poznámky modelu sú však číselné stavy, takže porovnanie opisuje ich úlohu, nie čitateľný vnútorný monológ.

Porovnania odpovedí prichádzajú až po vytvorení skrytej postupnosti. Usmerňujú tréning; systém nedostáva správnu odpoveď pred vytvorením svojho uvažovania pri inferencii. Autori nemenia architektúru ani postup inferencie a zásah sústreďujú na spôsob, akým sa existujúci model učí.

## Presnosť a závislosť od vnútorných stavov rastú spoločne

ReaLVR dosahuje na Qwen2.5-VL-7B priemernú presnosť približne 64 % v piatich vizuálnych benchmarkoch. Bežný východiskový model s latentným uvažovaním trénovaný posilňovaním dosahuje asi 60 %, zatiaľ čo najsilnejšia konkurenčná latentná metóda má priemer približne 63 %. Ide o porovnania autorov s tromi náhodnými inicializáciami, ktoré zahŕňajú rozlišovanie obrazov, priestorové uvažovanie a úlohy s obrázkami vo vysokom rozlíšení.

Najvyšší priemer neznamená víťazstvo v každej úlohe. Konkurenčná metóda dosahuje lepší výsledok v dvoch z piatich benchmarkov, čo obmedzuje tvrdenie na súhrnný výsledok. Porovnania zároveň odlišujú zlepšenia oproti jednoduchšiemu východisku od menšieho zlepšenia oproti silnejšiemu konkurentovi.

Výskumníci testujú, či zlepšené skryté stavy ovplyvňujú odpoveď. Nahradenie stavov, ktorým odpoveď venuje najväčšiu pozornosť, pri nezmenenom okolitom kontexte vedie pri ReaLVR k väčšiemu poklesu pravdepodobnosti správnej odpovede než pri východiskovom modeli. Tento zásah podporuje lokálnu závislosť od vybraných stavov nad rámec samotnej vizualizácie pozornosti.

Širšie hodnotenie zahŕňa šesť základných modelov z troch rodín. Patrí medzi ne aj model s celkovo 235 miliardami parametrov, pri ktorom autori uvádzajú zlepšenia v troch hodnotených benchmarkoch. Pri tejto veľkosti vynechávajú dva testy s vysokým rozlíšením, takže výsledky nemožno porovnávať ako rovnaký priemer piatich úloh.

Tréningový cieľ je menej presný, keď v dátach chýbajú vyznačené oblasti obrázka: ReaLVR vtedy používa cieľ z celého obrázka. Testy zároveň zachovávajú vopred stanovený počet skrytých krokov uvažovania. Tieto obmedzenia nechávajú otvorené otázky, ako dobre metóda vyberá dôkazy bez podrobných anotácií a prispôsobuje úsilie každej otázke.

Práca je preprint s výsledkami uvádzanými autormi; nezávislé zopakovanie tu nie je doložené. Ako ďalšie smery autori uvádzajú jemnejšie ciele pre obrazové dôkazy pri slabšom dohľade a rozpočet uvažovania prispôsobovaný otázke, čím rozvíjajú rovnaké prepojenie medzi obrázkom, priebežným výpočtom a odpoveďou.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Xi Xiao: UAB/Amazon AGI; spoluautori Amazon AGI; v1 z 28. septembra 2026. | OVERENÉ | https://arxiv.org/abs/2609.34563 | žiadne |
| Správna odpoveď sa mení v 81,45–86,33 % upravených párov; predikcia LVR v 5,66–13,09 %; štyri typy úprav, každý s 512 pármi. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.34563 | žiadne |
| Tréning porovnáva čítanie stavov pri správnych/nesprávnych odpovediach a relevantné/nesúvisiace obrazové dôkazy; skryté stavy vznikajú pred vetvami odpovedí; architektúra a inferencia sa nemenia. | OVERENÉ | https://arxiv.org/abs/2609.34563 | žiadne |
| Priemery piatich úloh Qwen2.5-VL-7B: ReaLVR 63,7, LVR-RL 60,4, ILVR 62,9; tri inicializácie; ILVR víťazí v BLINK a HR-8K. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.34563 | žiadne |
| Nahradenie ôsmich najdôležitejších tokenov pri pevnom kontexte znižuje pravdepodobnosť správnej odpovede o 4 body pri LVR a 11 bodov pri ReaLVR; lokálny zásah, nie úplné kauzálne určenie. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.34563 | žiadne |
| Šesť základných modelov/tri rodiny; 235B zahŕňa len tri benchmarky; náhrada celým obrázkom bez označených oblastí; pevný rozpočet latentných krokov; slabší dohľad a adaptívny rozpočet sú ďalším smerom. | OVERENÉ | https://arxiv.org/abs/2609.34563 | žiadne |
| Dôsledok pre výskumníka a prirovnanie k pracovným poznámkam vysvetľujú zdokumentovaný tréningový mechanizmus. | ANALÝZA | https://arxiv.org/abs/2609.34563 | žiadne |

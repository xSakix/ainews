+++
title = "Agentom uniká spojenie medzi konaním a výsledkom"
slug = "agentom-unika-spojenie-medzi-konanim-a-vysledkom"
description = "Preprint zistil, že veľká časť prínosu histórie agenta pretrvá aj po premiešaní jeho minulých krokov. Výslovné prepojenie každého kroku s výsledkom zlepšuje dokončenie úloh."
tags = ["research", "agents"]
date = 2026-10-06T04:07:31+02:00
draft = false
+++

Jazykové agenty často nedokážu spojiť minulý krok s pozorovaním, ktoré vyvolal, ani keď majú v kontexte úplnú históriu interakcie, uvádza nový preprint.

Jingyu Liu a štyria spoluautori skúmali agenty, ktoré pred výberom ďalšieho kroku dostávajú svoje skoršie kroky a spätnú väzbu prostredia. História zvyčajne pomáhala, no premiešanie starých krokov spôsobilo len mierne zhoršenie. Agenty teda záznam používali bez spoľahlivého učenia, ktorý krok viedol ku ktorému výsledku.

## Prečo na tom záleží {#why-it-matters}

Pre inžiniera, ktorý vytvára agenta používajúceho nástroje, je prepis užitočný len vtedy, keď sa z neho model dokáže poučiť. Ak agent číta minulé výsledky ako voľné náznaky, môže opakovať neúspešné kroky alebo prisúdiť úspech nesprávnemu kroku, hoci má všetky relevantné tokeny.

Výskumníci hypotézu testovali narušením dvojíc krokov a pozorovaní. Skoršie kroky premiešali, no pozorovania ponechali na mieste. Prepis tak naďalej obsahoval veľkú časť rovnakého jazyka, ale už nezachovával dôveryhodnú príčinnú postupnosť. Úspešnosť úloh klesla menej, než sa očakávalo.

Tento negatívny výsledok mení interpretáciu prínosu histórie. Vyššia úspešnosť s dlhším prepisom sama osebe nedokazuje, že si agent vytvoril užitočnú skúsenosť. Model môže len získavať náznaky z predchádzajúcich pozorovaní alebo ťažiť z ďalšieho textu súvisiaceho s úlohou.

Najjednoduchšia oprava tímu nepridala žiadne nové informácie o úlohe. Každé pozorovanie bolo výslovne označené ako výsledok bezprostredne predchádzajúceho kroku. Podľa preprintu táto anotácia zvýšila úspešnosť a znížila opakovanie ďalšieho kroku.

## Riadiaci model môže vybrať užitočnú skúsenosť

Práca následne predstavuje naučený kalibrátor krokov. Namiesto toho, aby hlavný agent interpretoval nerozlíšený prepis, kalibrátor opätovne posudzuje skoršie kroky a selektívne zaznamenáva skúsenosti pre ďalšie rozhodnutia. Autori uvádzajú ďalšie zlepšenie nad rámec výslovných označení výsledku.

Návrh oddeľuje dve úlohy, ktoré agentové systémy často spájajú: konať v prostredí a rozhodnúť, čo predchádzajúca interakcia naučila. Toto rozdelenie je praktické, pretože sa dá vložiť do existujúcej slučky agenta bez zmeny prostredia alebo pridania externých znalostí.

Hlavné dôkazy preprintu sú behaviorálne. Neurčujú, akú reprezentáciu si model vytvára vnútri, a abstrakt neobsahuje verejný odkaz na kód. Uvádzané zlepšenia závisia aj od testovaných úloh, modelov a formátu prepisu, preto nejde o univerzálny odhad pre produkčné agenty.

Premiešanie histórie je napriek tomu nezvyčajne informatívnou kontrolou. Odlišuje tvrdenie „prepis pomohol“ od tvrdenia „agent pochopil svoju skúsenosť“, ktoré sa pri hodnotení agentov často považujú za rovnocenné.

Liu, Zhiwen Wang, Yuxin Jing, Huanyu Zhou a Yong Liu odoslali preprint 2. októbra 2026. Zmena v označovaní výsledkov je opísaná dosť jasne na to, aby ju ďalší tvorcovia agentov otestovali vo vlastných slučkách. Naučený kalibrátor sa bez zverejnených podrobností trénovania a kódu bude posudzovať ťažšie.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Veľká časť prínosu histórie pretrvá po premiešaní minulých krokov | PODĽA SPOLOČNOSTI | [Preprint Liu a kol.](https://arxiv.org/abs/2610.02769) | žiadne; výsledok preprintu |
| Narušenie väzby medzi krokom a pozorovaním spôsobí len mierne zhoršenie | PODĽA SPOLOČNOSTI | [Preprint Liu a kol.](https://arxiv.org/abs/2610.02769) | žiadne |
| Výslovné označenie výsledkov zlepšuje úspešnosť a znižuje opakovanie krokov | PODĽA SPOLOČNOSTI | [Preprint Liu a kol.](https://arxiv.org/abs/2610.02769) | žiadne |
| Naučený kalibrátor zvyšuje úspešnosť nad rámec označenia výsledkov | PODĽA SPOLOČNOSTI | [Preprint Liu a kol.](https://arxiv.org/abs/2610.02769) | žiadne |
| Výsledok oddeľuje prínos prepisu od učenia väzby medzi krokom a výsledkom | ANALÝZA | [Preprint Liu a kol.](https://arxiv.org/abs/2610.02769) | záver z kontroly premiešaním |
| Preprint bol odoslaný 2. októbra 2026 | OVERENÉ | [Záznam arXiv](https://arxiv.org/abs/2610.02769) | metadáta arXiv |

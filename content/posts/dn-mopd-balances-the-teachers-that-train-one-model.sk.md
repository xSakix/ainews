+++
title = "DN-MOPD vyvažuje učiteľov trénujúcich jeden model"
slug = "dn-mopd-vyvazuje-ucitelov-trenujucich-jeden-model"
description = "Štúdia destilácie od viacerých učiteľov zisťuje, že spätná väzba dodržiavania pokynov môže prevládnuť nad matematikou. Zmena jej mierky zlepšuje spoločný model pri testovaných veľkostiach."
tags = ["research", "agents"]
date = 2026-10-03T05:52:20+02:00
draft = false
+++

DN-MOPD, trénovacia metóda vedená výskumníkmi Nanyang Technological University, zlepšuje destiláciu modelu od viacerých učiteľov vyvážením sily spätnej väzby každého špecialistu, namiesto samotného výberu učiteľa.

Xin Li a kolegovia z Nanyang Technological University, Yale University a University of Manchester spájajú špecialistov na matematiku, programovanie a dodržiavanie pokynov do jedného modelu. Ich diagnóza hovorí, že rovnaké zaobchádzanie s promptmi môže stále vytvárať nerovnaký vplyv na spoločné parametre.

**Prečo na tom záleží:** Inžinier následného trénovania spájajúci špecializované modely potrebuje, aby každá zručnosť prežila spojenie. Štúdia robí zo sily spätnej väzby výslovnú premennú a vysvetľuje, prečo aj správne pridelenie matematickej úlohy matematickému učiteľovi môže preniesť málo matematickej schopnosti.

[Preprint](https://arxiv.org/abs/2609.35347), prvýkrát predložený 28. septembra, skúma modely Qwen3.5 pri troch veľkostiach. Štandardná destilácia od viacerých učiteľov neprekonala najlepší model od jediného učiteľa pri žiadnej veľkosti a pri jednom hodnotenom rozpočte odpovede zachovala iba malý podiel zlepšenia matematického špecialistu.

Učiaci sa model generuje vlastnú odpoveď a učiteľ príslušnej domény poskytuje spätnú väzbu ku každému tokenu. Ide o destiláciu on-policy: trénovacie ciele sa uplatňujú na odpovede aktuálneho žiaka, nie výlučne na pevný súbor odpovedí učiteľa.

Smerovanie určuje príslušného učiteľa. Neurčuje, ako silno jeho spätná väzba mení žiaka. Spätná väzba dodržiavania pokynov mala omnoho širšie rozpätie než matematická a v počiatočnom modeli so štyrmi miliardami parametrov pri rovnakých váhach vytvárala takmer celú spoločnú aktualizáciu.

Mechanizmus pripomína výbor, ktorého členovia majú rovnaký počet vystúpení, no rôznu hlasitosť mikrofónov. Pridelené prompty matematického učiteľa nedokážu vyvážiť výsledok, keď spätná väzba iného učiteľa prichádza v oveľa väčšej mierke. DN-MOPD túto mierku upravuje pri zachovaní priradenia učiteľov.

Metóda meria rozpätie spätnej väzby osobitne pre každú doménu v aktuálnej dávke. Ohraničený násobiteľ približuje tieto signály k spoločnej mierke pri zachovaní ich smeru. Nevyžaduje ďalšie volanie učiteľa ani naučený smerovací model; mení váhu existujúcich signálov.

## Stíšenie jedného učiteľa obnovuje vplyv ostatných

Autori porovnávajú nezávisle trénované skupiny špecialistov s deviatimi, štyrmi a dvoma miliardami parametrov. Učitelia a žiaci majú v každej skupine rovnakú veľkosť. Hlavné porovnania používajú rovnakých špecialistov, počiatočné váhy aj prompty, čo oddeľuje vyvažovanie spätnej väzby od iného trénovacieho súboru či silnejšieho učiteľa.

V šiestich verejných benchmarkoch DN-MOPD zlepšuje priemer oproti bežnej destilácii smerovanej podľa domény pri každej veľkosti. Vzorec platí pri troch náhodných inicializáciách žiaka a dvoch limitoch dĺžky odpovede. Uvádzané priemerné prínosy sú približne jeden až tri percentuálne body, pričom najväčšie zotavenie prináša matematika.

Kontrolné experimenty objasňujú pôvod zlepšenia. Samotné zosilnenie matematickej spätnej väzby pomáha menej než obmedzenie príliš silného signálu dodržiavania pokynov. Pevné doménové váhy blízke hodnotám nameraným DN-MOPD dosahujú porovnateľný výkon, čo naznačuje, že veľká časť prínosu pochádza z opravy nerovnováhy, nie z potreby zložitého dynamického smerovania.

Tento dôkaz zužuje tvrdenie. DN-MOPD ponúka spôsob identifikácie a kontroly mierky spätnej väzby, kým porovnateľné pevné váhy ukazujú, že nameranú rovnováhu možno niekedy implementovať jednoduchšie. Výber učiteľa a nastavenie jeho vplyvu sú odlišné rozhodnutia v tom istom trénovacom procese.

Štúdia testuje aj to, či skoré napodobňovanie odpovedí učiteľa obnovuje stratenú špecializovanú schopnosť. Tento zásah nenahrádza potrebu kontrolovať nerovnováhu spätnej väzby. Hlavnou otázkou zostáva, ako viacero doménových signálov aktualizuje rovnakého žiaka, nie dostupnosť odborníka pre každú doménu.

Merania sú vlastnými výsledkami autorov v preprinte, obmedzenými na skúmané skupiny špecialistov Qwen3.5 a úlohy. Niektoré porovnania s najsilnejším modelom od jediného učiteľa majú intervaly neistoty zahŕňajúce nulové zlepšenie, hoci priemery uprednostňujú DN-MOPD. Opakované inicializácie priamočiarejšie podporujú porovnanie s bežným smerovaním viacerých učiteľov.

Autori poskytujú [projektovú stránku](https://lixin.ai/DN-MOPD) a [kód](https://github.com/LiXin97/DN-MOPD). Ich kontrolné experimenty ponechávajú praktický záver: trénovací signál špecialistu na dodržiavanie pokynov môže prevládnuť nad ostatnými aj pri správnom pravidle smerovania promptov.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Afiliácie Liho a spolupracovníkov NTU/Yale/Manchester; v1 28. septembra 2026. | OVERENÉ | https://arxiv.org/abs/2609.35347 | žiadne |
| Skupiny Qwen3.5 9B/4B/2B; rovnaké veľkosti a spoločné počiatočné váhy/prompty; šesť benchmarkov, tri inicializácie, hodnotiace rozpočty 8K/16K. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.35347 | žiadne |
| Bežný MOPD neprekonáva najsilnejšieho žiaka jedného učiteľa; zachováva 14–32 % matematického prínosu pri8K a žiadny pri16K. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.35347 | žiadne |
| V počiatočnom4B dodržiavanie pokynov tvorí94 % spoločného gradientu; rozpätie spätnej väzby2,3–4,4× spoločnej mierky. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.35347 | žiadne |
| Normalizácia doménového rozpätia používa ohraničené násobitele zachovávajúce znamienko, bez ďalšieho učiteľa/volania/smerovača. | OVERENÉ | https://arxiv.org/abs/2609.35347 | žiadne |
| Priemerné zlepšenia1,17–2,36bodu pri16K,2,47–3,08pri8K; pevné váhy porovnateľné; kľúčové oslabenie dodržiavania pokynov; kontrola skorej imitácie; neistota porovnania jedného učiteľa. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2609.35347 | žiadne |
| Ponúkaný projekt a kód. | OVERENÉ | https://lixin.ai/DN-MOPD ; https://github.com/LiXin97/DN-MOPD | žiadne |
| Dôsledok pre inžiniera a prirovnanie mikrofónov vysvetľujú nerovnaký vplyv spätnej väzby napriek smerovaniu. | ANALÝZA | https://arxiv.org/abs/2609.35347 | žiadne |

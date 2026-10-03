+++
title = "AWS od 7. októbra zvyšuje sadzby za rezervované GPU"
slug = "aws-od-7-oktobra-zvysuje-sadzby-za-rezervovane-gpu"
description = "Nové sadzby EC2 Capacity Blocks sa účtujú za akcelerátor. Kúpené rezervácie si zachovajú cenu, kým On-Demand a Savings Plans zostávajú nezmenené."
tags = ["hardware", "tools", "models"]
date = 2026-10-03T05:20:20+02:00
draft = false
+++

AWS od 7. októbra 2026 zvýši rezervačné sadzby GPU v EC2 Capacity Blocks. Aktualizácia stanovuje ceny jednotlivých akcelerátorov namiesto celých inštancií s viacerými GPU.

Capacity Blocks umožňujú tímom rezervovať výpočtovú kapacitu pre naplánovanú úlohu strojového učenia. Zákazník zaplatí rezervovaný blok vopred a poplatky za operačný systém sa účtujú samostatne počas prevádzky inštancií.

**Prečo na tom záleží:** Tímy plánujúce trénovanie alebo hodnotenie musia rozlišovať cenu za GPU od ceny za server. Inštancia s ôsmimi akcelerátormi násobí uvedenú sadzbu za akcelerátor ôsmimi, ešte pred prípadnými samostatnými poplatkami za operačný systém.

[Nové hodinové sadzby](https://aws.amazon.com/ec2/capacityblocks/pricing/) sú 16,146 dolára pre P6-B300 a 14,208 dolára pre P6-B200, pričom zodpovedajúce sadzby GovCloud sú 16,819 dolára a 14,801 dolára. P5en bude stáť 7,895 dolára, P5e 6,866 dolára, P5 5,970 dolára, P4de 2,546 dolára a P4d 1,696 dolára za akcelerátor vo všetkých dostupných regiónoch.

Napríklad osem GPU H100 pri novej sadzbe P5 znamená 47,76 dolára za hodinu inštancie. Ide o výpočet z oznámenej sadzby, nie o starší údaj 41,528 dolára za inštanciu P5, ktorý stále zobrazuje aktuálna cenová tabuľka.

AWS uvádza, že ostatné ceny Capacity Blocks, ceny On-Demand a ceny Savings Plans zostávajú nezmenené. Aktualizácia sa týka uvedených rezervačných sadzieb, nie všeobecného zdraženia všetkých možností nákupu EC2.

[Dokumentácia fakturácie](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-pricing-billing.html) uvádza, že cena rezervácie sa po nákupe nemení. Zákazníci si môžu cenu ponuky pozrieť pred rezervovaním a poplatok sa účtuje vopred. Zľavy Savings Plans a Reserved Instance sa na Capacity Blocks nevzťahujú.

Pravidlo ceny platnej pri nákupe robí dátum rezervácie dôležitým, aj keď výpočtová úloha prebehne neskôr. Rozhoduje cena ponuky prijatej pri kúpe bloku.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Nový rozvrh sadzieb za akcelerátor začína 7. októbra; ostatné uvedené nákupné sadzby sa nemenia. | OVERENÉ | [Aktualizácia cien AWS](https://aws.amazon.com/ec2/capacityblocks/pricing/) | žiadne |
| Osem GPU po 5,970 dolára znamená 47,76 dolára za hodinu. | ANALÝZA | [Sadzba P5](https://aws.amazon.com/ec2/capacityblocks/pricing/) | Výpočet: 8 × 5,970 |
| Ceny kúpených blokov zostávajú pevné; rezervačné poplatky a poplatky za operačný systém sú samostatné. | OVERENÉ | [Dokumentácia fakturácie AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-pricing-billing.html) | žiadne |
| Zľavy Savings Plans a Reserved Instance sa na Capacity Blocks nevzťahujú. | OVERENÉ | [Dokumentácia fakturácie AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-pricing-billing.html) | žiadne |

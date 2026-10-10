+++
title = "Telegrafický štýl skracuje odovzdávanie medzi agentmi"
slug = "telegraficky-styl-skracuje-odovzdavanie-medzi-agentmi"
description = "Verejný benchmark zistil, že jediná inštrukcia prinúti viacero modelov písať strojovo čitateľné záznamy s približne polovicou výstupných tokenov. Technika zlyháva počas aktívneho uvažovania."
tags = ["agents", "research", "tools"]
date = 2026-10-10T03:58:41+02:00
draft = false
+++

Pokyn písať telegrafickým štýlom znížil výstup jazykových modelov približne o 40 % až 49 %, pričom iné modely získali zaznamenané fakty s porovnateľnou presnosťou.

Nezávislý vývojár Travis Smith testoval inštrukciu na 50 úryvkoch a približne 1 300 otázkach. Metóda žiada model vynechať členy a výplňové slová, skracovať, zachovať každý fakt, číslo a vlastné meno a používať malé písmená, aby veľké písmená nezvyšovali počet tokenov.

## Prečo na tom záleží {#why-it-matters}

Vývojár agenta platí raz, keď jeden model zapíše pamäť, a znova pri každom čítaní iným modelom. Kompresia záznamov medzi strojmi po dokončení práce môže znížiť cenu výstupu aj priestor, ktorý opakované odovzdávanie zaberá v kontexte.

Benchmark oddeľuje písanie od čítania. Gemma 4, Qwen3.8 a GLM-5.3-Flash písali skrátené záznamy, zatiaľ čo modely z viacerých rodín odpovedali na ukotvené otázky buď z týchto záznamov, alebo z bežných súhrnov. Smith zverejnil testovací nástroj, nemenné záznamy výsledkov a spustiteľný notebook.

Najjasnejší výsledok priniesli zapisujúce modely. Gemma použila približne o 40 % menej účtovaných výstupných tokenov, kým Qwen a GLM ušetrili približne 49 %. Modely čítajúce skomprimované záznamy dosiahli 0,99 až 1,10-násobok presnosti bežných súhrnov. Štyri rodiny čítajúcich modelov nedostali žiadny ukážkový príklad štýlu, čo naznačuje, že konvenciu už poznali z tréningových dát.

## Kompresia patrí až za uvažovanie

Umiestnenie zmenilo výsledok. Modely, ktoré mali odpovede formulovať priamo telegrafickým štýlom, si zachovali iba približne štyri pätiny bežnej presnosti. Keď sa obsah najprv ustálil a potom skomprimoval do záznamu, následné čítanie sa vyrovnalo alebo mierne prekonalo bežný súhrn.

Technika je preto vhodná pre archívy pracovných poznámok, pamäť agentov a odovzdávanie. Nehodí sa na odpoveď používateľovi ani na krok, v ktorom model ešte rozhoduje, čo povie. Skomprimovaný text zostáva čitateľný pre človeka, ale zámerne je menej pohodlný než bežná próza.

Povinné uvažovanie vytvorilo ďalší spôsob zlyhania. GPT-5-mini vytvoril menej viditeľných tokenov, ale podľa autorovho záznamu spotreboval približne trikrát viac na skryté uvažovanie, takže celkový zápis bol drahší. Tím musí testovať skutočné účtovanie poskytovateľa, nie iba znaky alebo viditeľné tokeny.

Smith meral aj spiatočný proces, v ktorom sa skomprimovaný text rozšíril späť do prózy. Uložený výsledok zostal menší než bežný súhrn, ale dodatočné volanie modelu spotrebovalo viac tokenov, než ušetril prvý zápis. Opakované lacné čítania môžu túto cenu vyrovnať; pracovný postup s jedným zápisom a jedným čítaním nemusí.

Historický rámec nemusí byť nevyhnutný. Smith nevykonal prísny kontrolný test s požiadavkou na maximálnu stručnosť bez zmienky o telegrafickom štýle. Experiment teda podporuje praktickú inštrukciu, ale nedokazuje, že zisk spôsobuje samotný telegrafický štýl.

Výsledok je tiež benchmark spustený autorom. Jeho silnou stránkou sú nezvyčajne dobre preskúmateľné materiály a testy naprieč rodinami; obmedzením je, že úryvky, otázky a hodnotitelia definujú jeden druh faktického záznamu. Kód, matematické odvodenia a konverzačná pamäť sa môžu komprimovať odlišne.

Publikovaný notebook možno teraz spustiť na produkčných prepisoch agentov, takže tímy môžu porovnať úspešnosť úloh a tokeny účtované poskytovateľom na vlastnej prevádzke.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Inštrukcie v telegrafickom štýle znížili účtované výstupné tokeny približne o 40 %–49 % pri modeloch Gemma, Qwen a GLM | PODĽA SPOLOČNOSTI | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | žiadne |
| Modely naprieč rodinami získali fakty s 0,99–1,10-násobkom presnosti bežného súhrnu | PODĽA SPOLOČNOSTI | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | žiadne |
| Priame tvorenie odpovedí telegrafickým štýlom znížilo presnosť približne na 0,81 bežnej hodnoty | PODĽA SPOLOČNOSTI | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | žiadne |
| Povinné uvažovanie GPT-5-mini v autorovom teste vymazalo úsporu viditeľných tokenov | PODĽA SPOLOČNOSTI | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | žiadne |
| Testovací nástroj, nemenné záznamy a notebook sú verejné | OVERENÉ | https://github.com/Travis42/telegraph-test | žiadne |
| Metóda sa najlepšie hodí na ustálené strojovo čitateľné záznamy, nie na aktívne uvažovanie | ANALÝZA | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | žiadne |

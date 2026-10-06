+++
title = "EasyCommand lokálne prekladá angličtinu do Bash"
slug = "easycommand-lokalne-preklada-anglictinu-do-bash"
description = "Open-source nástroj príkazového riadka obsahuje llama.cpp a dva malé doladené modely. Autor vydal aj trénovaciu množinu so 401 975 dvojicami a kód benchmarku."
tags = ["projects", "models", "tools"]
date = 2026-10-06T04:06:31+02:00
draft = false
+++

EasyCommand mení anglické požiadavky na príkazy Bash pomocou malého modelu, ktorý beží na CPU, takže prompt aj navrhovaný príkaz zostávajú v zariadení používateľa.

Vývojár Max Trivedi vydal aplikáciu príkazového riadka `ec`, dve rodiny modelov a dátovú množinu 401 975 deduplikovaných dvojíc požiadaviek a príkazov. Aplikácia obsahuje llama.cpp, zobrazí navrhovaný príkaz a pred vykonaním môže vyžiadať potvrdenie.

Vývojárovi, ktorý občas potrebuje pripomenúť príkaz shellu, lokálne spustenie odstraňuje volanie API z citlivej časti pracovného postupu. Zodpovednosť však zostáva na používateľovi: projekt upozorňuje, že aj dôveryhodne pôsobiaci príkaz môže byť chybný, a odporúča začať v režime náhľadu.

Vydané modely vychádzajú z Qwen2.5-Coder-1.5B-Instruct a Qwen3-0.6B. Oba sú dostupné ako súbory GGUF na lokálnu inferenciu, zlúčené kontrolné body BF16 a adaptéry LoRA na ďalšie trénovanie. Modely a dáta používajú licenciu Apache 2.0; aplikácia a kód benchmarku licenciu MIT.

Trivedi uvádza, že model s 1,5 miliardy parametrov vyriešil 212 z 300 položiek v aktualizovanej verzii benchmarku ALFA pre prevod angličtiny na príkazy shellu, kým starší systém nl2sh vyriešil 191. Ide o autorovo porovnanie s odlišnými promptmi a nastaveniami modelov, nie o výsledok z nezávislého rebríčka.

Vydanie je nezvyčajne užitočné, pretože zahŕňa aj nedostatky modelu. Trivedi uvádza, že plochá dátová množina nezachováva historické váhy použité pri trénovaní a nemá oficiálnu testovaciu množinu. Odporúča vyčleniť celé rodiny úloh namiesto náhodného rozdelenia parafráz, ktoré by mohlo dostať takmer rovnaké príkazy do trénovania aj hodnotenia.

Cieľom je GNU/Linux Bash, nie každý shell alebo operačný systém. Repozitár EasyCommand je už verejný a autor žiada používateľov o testy, ktoré odhalia nespoľahlivý prenos a chýbajúce pokrytie príkazov.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| EasyCommand beží lokálne, obsahuje llama.cpp a pred vykonaním zobrazuje náhľad príkazov | OVERENÉ | [Opis projektu](https://dirac.run/posts/easycommand) | [verejný repozitár](https://github.com/dirac-run/ec) |
| Vydanie obsahuje 401 975 deduplikovaných dvojíc anglického textu a Bash | OVERENÉ | [Opis projektu](https://dirac.run/posts/easycommand) | dátová množina je prepojená z repozitára |
| Modely vychádzajú z Qwen2.5-Coder-1.5B a Qwen3-0.6B | OVERENÉ | [Opis projektu](https://dirac.run/posts/easycommand) | artefakty modelov sú prepojené z repozitára |
| Model 1.5B dosiahol 212/300 oproti 191/300 pri nl2sh | PODĽA SPOLOČNOSTI | [Opis projektu](https://dirac.run/posts/easycommand) | žiadne; benchmark spustil autor |
| Modely a dáta používajú Apache-2.0; aplikácia a kód benchmarku MIT | OVERENÉ | [Opis projektu](https://dirac.run/posts/easycommand) | licenčné súbory v repozitári |
| Dátová množina nemá oficiálne testovacie rozdelenie a nezachováva historické váhy | PODĽA SPOLOČNOSTI | [Opis projektu](https://dirac.run/posts/easycommand) | autorovo vyhlásenie |

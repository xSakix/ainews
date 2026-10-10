+++
title = "Basalt špecializuje inferenciu Qwen pre Blackwell"
slug = "basalt-specializuje-inferenciu-qwen-pre-blackwell"
description = "Engine s licenciou MIT sa zameriava na jeden model Qwen a najnovšie spotrebiteľské GPU od Nvidie. Váhy mixture-of-experts môže presúvať do systémovej pamäte alebo na druhú kartu."
tags = ["models", "tools", "projects"]
date = 2026-10-10T03:59:41+02:00
draft = false
+++

Basalt je nový lokálny inferenčný engine vytvorený pre jednu rodinu modelov a jednu generáciu GPU: Qwen3.8-Flash-Next na kartách NVIDIA Blackwell.

Projekt s licenciou MIT je odvodený zo všeobecnejšieho enginu Strata a odstraňuje ostatné ciele. Jeho hlavným kompromisom je špecializácia: experti, ktorí sa nezmestia do videopamäte, môžu zostať v systémovej RAM alebo na druhej GPU, zatiaľ čo husté časti modelu mixture-of-experts zostávajú blízko hlavnej karty.

## Prečo na tom záleží {#why-it-matters}

Vývojár lokálnych modelov s pracovnou stanicou radu RTX 50 získava engine prispôsobený tomuto hardvéru namiesto všeobecného runtime s mnohými cestami kompatibility. Rovnaký úzky návrh zároveň vylučuje staršie systémy NVIDIA aj systémy iných výrobcov.

Basalt balí model do jedného súboru mapovateľného do pamäte, ktorý obsahuje váhy, tokenizér, chatovú šablónu, hlavu špekulatívneho dekódovania, rozloženie expertov a voliteľné komponenty pre obraz. Konverzia prebaľuje existujúce váhy namiesto ich pretrénovania. Hotové balíky sú samostatne dostupné na Hugging Face.

Priložený server implementuje rozhrania kompatibilné s OpenAI a Anthropic a môže obsluhovať najviac osem súbežných požiadaviek. Kontext sa predvolene delí medzi aktívne sloty, takže štyri sloty pri maxime 262 144 tokenov dostanú po 65 536 tokenov. Prevádzkovatelia môžu namiesto toho prideliť celý kontext každému slotu za zodpovedajúcu cenu v pamäti.

Runtime vyžaduje Linux na x86-64, CUDA 13 a GPU Blackwell s výpočtovou schopnosťou 12.0. Obrazová cesta má samostatný enkóder vytvorený pre vizuálnu časť Qwen s náhradným spracovaním na CPU. Repozitár obsahuje aj testy parity, kontrolu kvality založenú na perplexite a divergencii a benchmarkové vstupy.

Autor projektu uvádza stovky generovaných tokenov za sekundu na kombinácii RTX 5090 a 5060 Ti podľa typu promptu a kvantizácie. Tieto údaje sú jeho vlastné merania a neboli nezávisle zopakované. Dôležitejšia než špičková hodnota je technická voľba: veľký riedky model môže bežať na pracovnej stanici tým, že pri každom kroku prenáša iba potrebných expertov.

## Čo sledovať

Nezávislé testy musia pri dodaných kvantizáciách porovnať kvalitu aj rýchlosť. Repozitár tiež upozorňuje, že predvolené nastavenia servera nie sú vyladené, takže publikované výsledky potrebujú úplnú konfiguráciu, aby sa dali porovnávať.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Basalt je engine pre Qwen3.8-Flash-Next s licenciou MIT určený pre Linux a NVIDIA Blackwell | OVERENÉ | https://github.com/jesdga95/basalt | žiadne |
| Engine môže umiestniť expertov do systémovej RAM alebo na druhú GPU | OVERENÉ | https://github.com/jesdga95/basalt | žiadne |
| Server ponúka API kompatibilné s OpenAI a Anthropic s najviac ôsmimi súbežnými slotmi | OVERENÉ | https://github.com/jesdga95/basalt | žiadne |
| Autor uvádza stovky generovaných tokenov za sekundu na dvojici RTX 5090 a 5060 Ti | PODĽA SPOLOČNOSTI | https://github.com/jesdga95/basalt | žiadne |
| Špecializácia odstraňuje cesty kompatibility výmenou za tesnejšiu optimalizáciu hardvéru | ANALÝZA | https://github.com/jesdga95/basalt | žiadne |

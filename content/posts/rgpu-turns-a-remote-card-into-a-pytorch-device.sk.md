+++
title = "rGPU mení vzdialenú kartu na zariadenie PyTorch"
slug = "rgpu-meni-vzdialenu-kartu-na-zariadenie-pytorch"
description = "Projekt s licenciou Apache ponecháva Python a kód modelu na klientskom počítači, zatiaľ čo tenzory a operácie CUDA bežia na vzdialenom GPU NVIDIA."
tags = ["projects", "hardware", "tools"]
date = 2026-10-08T03:55:31+02:00
draft = false
+++

Open-source projekt rGPU umožňuje programu v PyTorch zostať spustený na notebooku, zatiaľ čo jeho tenzory a operácie sídlia na vzdialenom GPU NVIDIA.

Systém s licenciou Apache ponúka dve cesty. Nový kód PyTorch môže vybrať `device="rgpu"`, zatiaľ čo širšia vrstva kompatibility CUDA zachytáva volania existujúcich binárnych súborov pre Linux a preposiela ich serveru cez sieťové spojenie.

Pre vývojára s Macom alebo skromnou pracovnou stanicou a nevyužitým GPU počítačom inde táto deľba zachováva lokálne vývojové prostredie bez presunu celej aplikácie do cloudového notebooku či vzdialeného shellu. Klient môže vytvoriť tenzor na vzdialenom zariadení pomocou bežnej syntaxe PyTorch a dodaný spúšťač vytvorí tunel SSH k serveru.

Jednoduchá cesta zariadenia odosiela operácie PyTorch cez TCP. Cesta kompatibility implementuje náhrady ovládača a runtime CUDA, ako aj cuBLAS, cuBLASLt a cuDNN, s cieľom spúšťať štandardné binárne súbory PyTorch pre CUDA. Repozitár opisuje túto vrstvu ako rozhranie s väčšou plochou kompatibility, takže podpora bude závisieť od volaní knižníc, ktoré aplikácia používa.

rGPU obsahuje príklad trénovania nanoGPT, referencie operácií a konfigurácie, poznámky k výkonu a testy komponentov v Pythone a C++. V repozitári je aj experimentálna práca s JAX, no nie je uvedená ako podporovaná cesta produktu.

Hlavným prevádzkovým obmedzením je bezpečnosť siete. Ani jeden protokol neposkytuje vlastné overovanie ani šifrovanie. Dokumentácia odporúča ponechať operačný server naviazaný na localhost a pripájať sa cez SSH; server CUDA počúva na všetkých rozhraniach IPv4, takže port 9713 treba obmedziť aj pravidlami hostiteľského alebo cloudového firewallu.

Projekt mení vzdialenú akceleráciu na voľbu zariadenia namiesto samostatného prostredia na spúšťanie, no tvrdenia o výkone a kompatibilite zatiaľ pochádzajú z dokumentácie správcu. Kód, testy a technické záznamy sú dostupné na kontrolu a projekt na svojej stránke GitHub zatiaľ nemá uvedené žiadne označené vydanie.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| rGPU ponecháva aplikáciu na klientovi, zatiaľ čo tenzory a práca GPU bežia na vzdialenom zariadení NVIDIA | OVERENÉ | [Repozitár rGPU](https://github.com/ymcrcat/rgpu) | žiadne |
| Projekt ponúka zariadenie PyTorch `rgpu` a vrstvu kompatibility CUDA | OVERENÉ | [Repozitár rGPU](https://github.com/ymcrcat/rgpu) | žiadne |
| Vrstva pokrýva ovládač CUDA, CUDA Runtime, cuBLAS, cuBLASLt a cuDNN | OVERENÉ | [Repozitár rGPU](https://github.com/ymcrcat/rgpu) | žiadne |
| Ani jeden protokol neposkytuje overovanie ani šifrovanie; dokumentácia predpisuje obmedzenia SSH a firewallu | OVERENÉ | [Repozitár rGPU](https://github.com/ymcrcat/rgpu) | žiadne |
| Repozitár obsahuje testy, príklad nanoGPT a experimentálnu prácu s JAX | OVERENÉ | [Repozitár rGPU](https://github.com/ymcrcat/rgpu) | žiadne |
| Vlastnosti kompatibility a výkonu dokumentuje správca projektu | PODĽA SPOLOČNOSTI | [Repozitár rGPU](https://github.com/ymcrcat/rgpu) | žiadne |

+++
title = "Epoch zisťuje, že agenti nezvládajú otvorenú prácu"
slug = "epoch-agenti-nezvladaju-otvorenu-pracu"
description = "Šesť modelov zvládalo presne vymedzené programovanie a analýzu lepšie než výskumný úsudok, interný štýl a návrh experimentov v hodnotení z reálnej práce Epoch AI."
tags = ["agents", "essays", "research"]
date = 2026-10-09T03:59:06+02:00
draft = false
+++

Špičkoví agenti spoľahlivo dokončili presne vymedzené časti práce Epoch AI, no zaostali pri úlohách závislých od implicitných štandardov, výskumného úsudku alebo návrhu experimentu.

Neziskový výskumný inštitút dal šiestim modelom 11 skutočných úloh zo svojich pracovných postupov v grafike, dátach, softvéri a výskume. Claude Fable 5.1 a GPT-6 Astra v hodnotení celkovo viedli, no ani jeden nedokázal bez zásahu vytvoriť prácu na úrovni Epochu od začiatku do konca.

**Prečo na tom záleží:** Manažérovi, ktorý rozhoduje o mieste agentov vo vedomostnej práci, benchmarky s jednou presnou odpoveďou veľa nepovedia. Výsledky Epochu umiestňujú zostávajúci rozdiel do výberu dobrej otázky, pochopenia miestnych štandardov a rozpoznania, že experiment meral nesprávnu vec.

## Skutočné nástroje odhalili zlyhania úsudku

Epoch poskytol každému modelu kontext, ktorý by dal novému zamestnancovi, vrátane repozitárov, dizajnových referencií a prístupu k nástrojom ako Figma, Google Drive a weby na objednávanie satelitných snímok. Modely bežali na najvyššej dostupnej úrovni uvažovania a počas úlohy nedostali pomoc. Zamestnanec Epochu potom každý výstup ohodnotil podľa pravidiel pre danú kategóriu.

Súbor pokrýval päť druhov práce: grafický dizajn, krátku dátovú analýzu, interaktívne dátové prehliadače, výskum dátových centier a návrh výskumu. Niektoré objektívne kontroly dopĺňali subjektívne kritériá. Vďaka tejto kombinácii mohlo hodnotenie zahrnúť vhodnosť pre publikum a hodnotu experimentu, ktorým sa automatizované benchmarky zvyčajne vyhýbajú.

Fable 5.1 a GPT-6 Astra boli najspoľahlivejšie pri programovaní, výpočtoch a používaní počítača. Jedna jednoduchá úloha na zmenu štýlu grafu bola odstránená, pretože výstup Fable dosiahol štandard inštitútu, a Epoch uvádza, že tento krok už z veľkej časti interne automatizuje. Modely s otvorenými váhami Kimi K3 a Qwen 3.8 Max mali častejšie problémy s presne vymedzenou prácou aj s otvorenými časťami.

Zlyhania boli zreteľnejšie, keď úloha ponúkala veľa obhájiteľných smerov. Modely mali dostatok príkladov vizuálneho a redakčného štýlu Epochu, no kopírovali povrchové prvky bez pochopenia ich dôvodu. Astra si vybral fyzikálnu tému, ktorú Epoch považoval za príliš úzku pre všeobecné publikum so záujmom o AI; Fable vytváral diagramy a zhrnutia s oveľa väčšou hustotou informácií, než publikácia zvyčajne používa.

Návrh výskumu odhalil ťažšiu hranicu. Astra navrhol sľubnú otázku, prečo sa agenti nedokážu učiť zo skúseností, a potom vykonal pilot, v ktorom nízky limit tokenov prerušil veľa odpovedí. Všimol si skrátenie a experiment zopakoval, no citlivosť na tento limit aj tak prezentoval ako podstatný výsledok. Kritika Epochu spočíva v tom, že chyba nastavenia neodpovedala na výskumnú otázku.

Tento dôkaz pridáva niečo, čo bežné skóre schopností prehliada. Systém môže ovládať nástroje, napísať kód a vypočítať výsledok, no stále si vybrať neužitočnú tému alebo považovať artefakt za zistenie. Tieto chyby vznikajú pri formulovaní a interpretácii práce, teda aj tam, kde sa správnosť ťažko automaticky boduje.

Porovnanie má dôležité obmedzenia. Epoch spustil každý model na každej úlohe iba raz, použil jedného ľudského hodnotiteľa na výstup a posudzoval prácu podľa vlastných štandardov. Šesť modelov tiež používalo rôzne agentové prostredia, takže výsledok mohol ovplyvniť lepší prehliadač alebo integrácia nástrojov. Správu je najlepšie čítať ako súbor pozorovaných režimov zlyhania, nie ako všeobecný rebríček automatizácie práce.

Epoch plánuje pridávať výsledky nových modelov. Projekt sa tým mení na užitočný dlhodobý test: rozhodujúcou zmenou bude model, ktorý pochopí nepísané štandardy organizácie a odmietne vlastný chybný experiment, nie model, ktorý iba zvýši skóre benchmarku.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Epoch hodnotil šesť modelov na 11 úlohách z piatich kategórií vlastnej práce | OVERENÉ | [Správa Epochu](https://epoch.ai/publications/can-ai-automate-epoch) | žiadne |
| Modely dostali kontext a nástroje, pracovali bez zásahu a boli hodnotené manuálne | OVERENÉ | [Správa Epochu](https://epoch.ai/publications/can-ai-automate-epoch) | žiadne |
| Fable 5.1 a GPT-6 Astra v hodnotení celkovo viedli | PODĽA SPOLOČNOSTI | [Správa Epochu](https://epoch.ai/publications/can-ai-automate-epoch) | žiadne |
| Epoch odstránil úlohu na zmenu štýlu grafu po tom, ako Fable 5.1 splnil jeho štandard | PODĽA SPOLOČNOSTI | [Správa Epochu](https://epoch.ai/publications/can-ai-automate-epoch) | žiadne |
| Modely s otvorenými váhami robili v tomto súbore viac chýb pri presne vymedzených úlohách | PODĽA SPOLOČNOSTI | [Správa Epochu](https://epoch.ai/publications/can-ai-automate-epoch) | žiadne |
| Pilot Astry započítal prerušené odpovede a neskôr prezentoval citlivosť na limit tokenov ako výsledok | PODĽA SPOLOČNOSTI | [Správa Epochu](https://epoch.ai/publications/can-ai-automate-epoch) | žiadne |
| Hodnotenie použilo jeden beh na úlohu, jedného hodnotiteľa na výstup a odlišné prostredia | OVERENÉ | [Správa Epochu](https://epoch.ai/publications/can-ai-automate-epoch) | žiadne |
| Epoch plánuje pridávať výsledky nových modelov | OVERENÉ | [Správa Epochu](https://epoch.ai/publications/can-ai-automate-epoch) | žiadne |

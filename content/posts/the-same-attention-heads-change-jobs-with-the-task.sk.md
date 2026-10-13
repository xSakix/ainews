+++
title = "Rovnaké attention heads menia úlohu podľa zadania"
slug = "rovnake-attention-heads-menia-ulohu-podla-zadania"
description = "Nový preprint zistil, že jazykový model reorganizuje vplyv svojich attention heads pri zmene požadovanej úlohy, aj keď fakty v prompte zostávajú rovnaké. Kauzálne zásahy naznačujú, že kontext úlohy pomáha určovať funkciu komponentu, čo komplikuje snahy prideliť mu jedinú trvalú nálepku."
tags = ["research", "models"]
date = 2026-10-13T04:05:13+02:00
draft = false
+++

Predstavme si inžinierku pri monitore, ktorá sleduje čiary medzi stovkami malých políčok. Jedno dostane úhľadnú nálepku: „vyhľadávanie krajiny“. Potom sa zmení inštrukcia, vstupné fakty zostanú rovnaké a to isté políčko zdanlivo pomáha s niečím iným. Táto inžinierka je vymyslená a ilustruje praktický problém v centre novej štúdie: komponent transformera nemusí mať jedinú stabilnú úlohu, ktorú možno pomenovať.

## Mapa, ktorá sa mení s otázkou

Sovesh Mohapatra a Dani S. Bassett, výskumníci pôsobiaci na University of Pennsylvania a Yale University, testovali, ako kontext úlohy mení funkčnú organizáciu attention heads v jazykových modeloch. Ich preprint odoslaný 12. októbra 2026 skúma päť otvorených modelov od 1,5 miliardy do 14 miliárd parametrov. Neabsolvoval recenzné konanie.

Štúdia začína zámerným oddelením. Prompt obsahuje malý graf zapísaný ako faktické tvrdenia, kým inštrukcia žiada model odpovedať na jednu z viacerých otázok o tomto grafe. Fakty grafu zostávajú pri všetkých podmienkach rovnaké. Mení sa iba úloha. Takýto návrh umožňuje skúmať, či model nad rovnakými informáciami používa rovnakú vnútornú cestu, alebo ju reorganizuje podľa požiadavky.

Každý attention head autori chápu ako uzol siete vplyvu. Hrana zaznamenáva, ako zmena výstupu jedného headu ovplyvní ďalší head v neskoršej časti modelu. Výsledná mapa je funkčná, nie anatomická: architektúra sa nemení, no nameraný vzorec vplyvu sa môže líšiť podľa úlohy.

A líši sa. Mohapatra a Bassett uvádzajú, že siete sa v testovaných modeloch rozdeľujú podľa úlohy. Heads s vplyvnou pozíciou v jednej úlohe môžu byť v inej menej centrálne. Zistenie presúva otázku interpretovateľnosti z „Čo tento head reprezentuje?“ k otázke „Akú rolu hrá tento head v tejto úlohe a v tejto sieti?“

Rozdiel je dôležitý, pretože veľká časť mechanistickej interpretovateľnosti hľadala opakovane použiteľné vnútorné časti. Eric Todd a kolegovia už identifikovali malé skupiny attention heads, ktoré prenášajú kompaktné „funkčné vektory“ získané z príkladov v kontexte. Roee Hendel, Mor Geva a Amir Globerson podobne ukázali, že učenie v kontexte môže vytvoriť vektor úlohy, vďaka ktorému model vykoná demonštrovanú operáciu aj bez ukážok počas inferencie. Tieto výsledky podporujú predstavu, že úloha môže mať kauzálnu vnútornú reprezentáciu. Nová práca skúma, ako táto reprezentácia mení vzťahy medzi komponentmi.

## Inštrukcia môže presunúť mechanizmus

Samotná korelácia by ponechala zrejmú pochybnosť. Iná úloha vedie k inej odpovedi, takže odlišná mapa vplyvu môže zmenu iba sprevádzať. Autori preto zasahujú do aktivácií modelu.

Vytvoria úpravu aktivácie v skorej vrstve, ktorá má model presunúť od reprezentácie jednej úlohy k druhej bez zmeny písomného promptu. V experimentoch na modeloch Gemma a Qwen dokáže táto úprava zmeniť úlohu, ktorú model vykonáva. Práca uvádza, že všetkých 512 promptov, pri ktorých dve úlohy vyžadovali opačné odpovede, prešlo na cieľovú odpoveď, zatiaľ čo všetkých 512 promptov s rovnakou odpoveďou pre obe úlohy ju zachovalo.

Zásah zároveň približuje neskoršiu mapu vplyvu k cieľovej úlohe. Autori to merajú chybou medzi vzorcami odozvy siete. Úprava prepínajúca úlohu znížila túto chybu o 53,6 % v Gemme a o 5 % v Qwene. Rozdiel vo veľkosti varuje pred predstavou jednotného mechanizmu naprieč rodinami modelov, ale oba prípady ukazujú rovnakým kauzálnym smerom: zmena vnútorného kontextu úlohy môže presmerovať neskorší výpočet.

Podobá sa to na activation steering, širšiu rodinu metód, ktoré menia správanie modelu pridaním smeru k skrytým aktiváciám. Alexander Matt Turner a kolegovia ukázali, že pridanie aktivácií odvodených z kontrastných promptov môže bez ďalšieho trénovania meniť vlastnosti generovaného textu na vysokej úrovni. Nová štúdia používa úpravu aktivácie ako experimentálnu sondu. Jej cieľom nie je dodať ovládací prvok správania, ale testovať, či zmena reprezentácie úlohy predchádza zmene siete vplyvu attention heads.

Zásah je úzky. Neukazuje, že výskumníci dokážu spoľahlivo vybrať ľubovoľnú úlohu, upraviť ľubovoľný model alebo vyčítať celý program z grafu heads. Úlohy sú kontrolované, modely sú systémy s otvorenými váhami strednej veľkosti a kauzálne testy sa sústreďujú na konkrétny vnútorný kontrast. Najsilnejšie tvrdenie práce sa týka závislosti od kontextu v tomto nastavení.

## Od označených častí k zostaveným tímom

Sieťová neuroveda poskytuje autorom organizačnú metaforu. V tomto odbore sa prínos mozgovej oblasti často skúma cez jej miesto v meniacej sa sieti, nie cez jedinú izolovanú funkciu. Bassett a Olaf Sporns opísali tento prístup ako snahu prepájať prvky naprieč mierkami a vysvetliť, ako interakcie vytvárajú správanie. Mohapatra a Bassett prenášajú túto perspektívu do analýzy transformerov.

Analógia má hranice. Attention head je navrhnutý matematický komponent, nie biologická oblasť, a transformer nemá anatómiu ani históriu mozgu. Užitočný je prenos metódy: pozorovať časť spolu so vzorcom vplyvu, ktorý ju zapája.

Pre ľudí, ktorí auditujú modely, je preto trvalá nálepka menej upokojujúca. Head, o ktorom sa zistí, že podporuje správanie pri jednom prompte, sa môže pri zmene inštrukcií, príkladov alebo cieľov zapojiť inak. Jeho odstránenie či potlačenie môže mať účinky závisiace od kontextu úlohy. Proces dôležitý pre bezpečnosť môže byť zároveň rozložený medzi rôzne konfigurácie, hoci základné parametre zostávajú rovnaké.

Výsledok tiež naznačuje praktický štandard pre budúce tvrdenia o interpretovateľnosti. Navrhovaný obvod treba testovať naprieč úlohami, ktoré opätovne používajú tie isté informácie, a zdanlivá rola by mala obstáť pri kauzálnom zásahu, nie iba pri vizuálnej kontrole. Ak sa obvod mení, zmena patrí k mechanizmu, ktorý treba vysvetliť.

Zostáva veľa práce. Štúdia skúma obmedzenú rodinu úloh založených na grafoch a malú skupinu otvorených modelov. Neurčuje, ako sa siete odozvy správajú vo veľmi veľkých proprietárnych systémoch, počas dlhých rozhovorov ani pri neprehľadných reálnych inštrukciách. Ani nerozhoduje, či nameraná sieť zachytáva celý výpočet relevantný pre odpoveď. Autori predstavujú rámec na skúmanie rekonfigurácie, nie hotový atlas.

Vráťme sa k vymyslenej inžinierke pri monitore. Nálepka na políčku zostáva užitočná, no potrebuje dodatok: užitočné pre túto operáciu, pri tejto inštrukcii, v tejto spoločnosti ostatných heads. Trvalým objektom už nie je izolovaná časť. Je ním vzorec, ktorý úloha povoláva do služby.

## Použité zdroje

- Bassett, D. S., & Sporns, O. (2017). *Network neuroscience*. https://doi.org/10.1038/nn.4502
- Hendel, R., Geva, M., & Globerson, A. (2023). *In-Context Learning Creates Task Vectors*. https://aclanthology.org/2023.findings-emnlp.624/
- Mohapatra, S., & Bassett, D. S. (2026). *Task Context Dynamically Reconfigures Attention Head Networks in Large Language Models*. https://arxiv.org/abs/2610.13895
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://openreview.net/forum?id=AwyxtyMwaG
- Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2024). *Activation Addition: Steering Language Models Without Optimization*. https://arxiv.org/abs/2308.10248

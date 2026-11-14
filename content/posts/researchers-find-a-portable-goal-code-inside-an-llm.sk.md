+++
title = "Výskumníci našli v LLM prenositeľný kód cieľa"
slug = "vyskumnici-nasli-v-llm-prenositelny-kod-ciela"
description = "Nový preprint sleduje ďalší programovací cieľ LLM až k malej skupine hláv pozornosti, číta ho v bežnom jazyku a prenáša medzi programovacími jazykmi. Výsledok prináša príčinný dôkaz z kontrolovaného prostredia, nie potvrdenie, že každý agent má stabilný vnútorný zámer."
tags = ["research", "models", "agents"]
date = 2026-11-14T04:08:30+01:00
draft = false
+++

Vymyslená vývojárka Mara sleduje generovanú funkciu v okamihu, keď model dokončil počítanie slov s veľkým začiatočným písmenom a chystá sa hľadať palindrómy. Kurzor stojí za znamienkom rovnosti. Zatiaľ sa neobjavilo porovnanie ani obrátený reťazec a žiadny výstupný token nenaznačuje ďalší krok. Mara by v tej chvíli rada model zastavila a položila mu jednoduchú otázku: čo sa teraz snažíš urobiť? Táto scéna je ilustráciou. Nový experiment mení otázku na niečo, čo môžu výskumníci otestovať vnútri modelu.

## Cieľ ešte pred kódom

Arnab Sen Sharma a deväť kolegov z Northeastern University, Parallax, University of Copenhagen a University of Oxford uvádzajú, že ďalší čiastkový cieľ programovacieho modelu možno lokalizovať v malej skupine hláv pozornosti. Ich preprint, vydaný 12. novembra, sa nezastavuje pri zistení korelácie. Výskumníci dekódujú reprezentáciu do prirodzeného jazyka, prenesú ju do iného programovacieho jazyka a zásahom do nej zmenia kód, ktorý model napíše.

Výskum kladie úzku verziu širokej a citlivej otázky: majú jazykové modely ciele? Autori nepovažujú plynulé správanie za dôkaz zámeru. Cieľ definujú ako vnútorný stav, ktorý sa objaví pred konaním, možno ho uskutočniť rôznymi prostriedkami a pretrváva počas vykonávania. Táto praktická definícia vytvára tri testy: predbežné prijatie cieľa, pružnosť a pretrvávanie.

Tieto testy umožňuje kontrolovaná úloha. Prompty žiadali model, aby vykonal dve až štyri nezávislé operácie s celými číslami, reťazcami alebo zoznamami. Operácia mohla spočívať v počítaní slov s veľkým začiatočným písmenom, zisťovaní rozsahu alebo kontrole, či je niektoré slovo palindróm. Výskumníci použili 253 špecifikácií a skúmali štyri pozície pred začiatkom každej ďalšej operácie, čo vytvorilo 1 012 pozorovaní v každej konfigurácii hodnotenia.

Väčšina hlavných výsledkov v štúdii pochádza z modelu Qwen-2.5-Coder-32B-Instruct so 64 vrstvami. Postup riedkeho výberu identifikoval 122 hláv pozornosti, ktoré sa sústreďovali medzi vrstvami 28 až 55. Postup uprednostnil hlavy, ktorých výstup bolo možné preniesť zo zdrojového promptu v jednom programovacom jazyku do cieľového promptu v inom jazyku a vyvolať tým začiatok zdrojovej operácie. Výber odlišných jazykov bol dôležitý: reprezentácia kontroly palindrómu musela prežiť zmeny syntaxe, názvov premenných aj konkrétnych tokenov.

## Čítanie skrytého pokynu

Tím vytvoril z výstupov vybraných hláv sondu GoalScope, ktorá mala reprezentáciu sprístupniť. Sčíta hodnoty, ktoré hlavy zapíšu do reziduálneho prúdu modelu pri zvolenom tokene, a následne vloží tento vektor do samostatného behu toho istého modelu. Druhý beh dostane pevný pokyn, aby opísal operáciu. Jeho textový prompt neobsahuje žiadne informácie z pôvodnej programovacej úlohy, takže pôvodný kontext sa k odpovedi môže dostať iba cez vloženú aktiváciu.

Metóda rozvíja Patchscopes, framework, ktorý Asma Ghandeharioun a jej kolegovia predstavili na vkladanie skrytej reprezentácie do promptu, kde ju jazykový model dokáže vysvetliť. Nadväzuje aj na skorší výskum viacerých členov toho istého tímu. Function Vectors ukázal, že kompaktný súčet výstupov hláv pozornosti môže niesť vstupno-výstupnú funkciu a spustiť ju v novom kontexte. General Filter Heads neskôr izoloval prenositeľnú reprezentáciu predikátov, ktoré sa používajú na filtrovanie zoznamov. Nová štúdia prechádza od jednej operácie k meniacemu sa ďalšiemu kroku úlohy s viacerými operáciami.

Vyčítanie cieľa začalo byť užitočné ešte predtým, než model vydal implementáciu. Na konci predchádzajúceho riadka opisy GoalScope súhlasili s netriviálnou časťou nadchádzajúceho správania približne v 60 % prípadov. Pri odsadení, tri tokeny pred implementáciou, uvádzané skóre prekročilo 90 %. Po prenose do kontextu jazyka C++ reprezentácia pri jednej z kontrolných pozícií vyvolala zodpovedajúcu operáciu v 96 % prípadov. Priemer naprieč pozíciami dosiahol približne 87 %.

Tieto výsledky podporujú predbežné prijatie cieľa aj pružnosť. Podľa nich vybraná aktivita nesie informáciu o tom, čo má model urobiť, ešte pred objavením príslušného kódu. Informácia teda nie je iba uloženou postupnosťou tokenov Pythonu. Cieľový model vytvorí postup, ktorý zodpovedá novému kontextu.

Príčinné testy toto tvrdenie spresňujú. Keď výskumníci zachovali vybraným hlavám prístup k ďalšej úlohe a približne 93 % neskorších hláv pozornosti k tejto časti prístup zablokovali, model si do veľkej miery zachoval schopnosť vykonať operáciu. Zablokovanie iba 122 vybraných hláv ponechalo priestor na náhradu redundantnými cestami, no zablokovanie širšieho súboru 250 hláv výrazne znížilo výkon. Autori to opisujú ako príčinné úzke miesto s redundanciou, nie ako jediný nenahraditeľný spínač.

## Cieľ sa pri každom kroku vytvára znova

Pretrvávanie prináša mechanickú hádanku. Autoregresívny transformer nemá rekurentný stav, ktorý by sa dal donekonečna jednoducho odovzdávať z jedného vytvoreného tokenu na ďalší. Pozornosť môže načítať skoršiu pozíciu, no presun novo vypočítaného stavu dopredu spotrebúva vrstvy. V tomto modeli sa cieľ dal vyjadriť slovami až približne po 40. vrstve, takže nezostávala dostatočná hĺbka na prenos rovnakého stavu cez operácie dlhšie než 30 tokenov.

Autori navrhujú odlišný mechanizmus. Model opakovane číta špecifikáciu úlohy, skúma hotový kód viditeľný v kontexte a rekonštruuje čakajúcu operáciu. Tento proces nazývajú nerekurentné sledovanie cieľa. Zdanlivú kontinuitu vytvára opakovaný výpočet, nie jediný vnútorný objekt, ktorý sa bez zmeny presúva celou sekvenciou.

Cielené prenosy tento opis podporili. Výskumníci zmenili stavy kľúčov a hodnôt, ktoré hlavy cieľa čítali z časti s úlohou, zatiaľ čo ostatné hlavy naďalej pracovali s cieľovým promptom. Model potom vykonal ďalšiu operáciu zo zdrojového promptu v cieľovom programovacom jazyku približne v 94 % prípadov. Opis GoalScope sa spolu s ňou zmenil približne v 90 % prípadov. Pri samostatnom zásahu nahradenie stavov dopytu týchto hláv prenieslo informáciu o dokončenej práci a zmenilo výber nasledujúcej čiastkovej úlohy.

Toto rozlíšenie je dôležité pre dohľad. Monitor by mohol prečítať čakajúcu operáciu ešte predtým, než sa objaví vo výstupe, a zásah by ju mohol presmerovať. Reprezentácia však vzniká zo špecifikácie a viditeľného postupu. Ak sa zmení jeden z týchto zdrojov, môže sa zmeniť aj zdanlivý cieľ.

## Hranice čitateľného cieľa

Štúdia nepotvrdzuje univerzálne centrum cieľov. Jej hlavný dataset tvoria vymenované programovacie operácie, väčšina meraní v hlavnej časti pochádza z jedného modelu doladeného na kód a zhodu vytvorených opisov s implementáciami hodnotí iný LLM. Autori v prílohách testujú ďalšie rodiny modelov aj niektoré prostredia prirodzeného jazyka, medzi obmedzeniami však uvádzajú rozsah modelov a úloh.

Najsilnejšie varovanie sa objavuje pri narušení postupu. Model si počas bežného vykonávania uchoval rozpoznateľnú reprezentáciu, no často sa nedokázal spamätať z vloženého chybného začiatku. Qwen-2.5-Coder-32B-Instruct sa prispôsobil približne v 97 % prípadov so zhodným začiatkom, v 63 % prípadov s ľahkým narušením a iba v 15 % prípadov s ťažkým narušením. Ostatné testované modely vykázali rovnaký pokles. Čitateľný cieľ nezaručil úspešné vykonanie.

Vráťme sa k Mare pri čakajúcom kurzore. V tejto vymyslenej záverečnej scéne jej debugger zobrazí predbežnú poznámku: kontrola, či je niektoré slovo palindróm. Mara ju považuje za predpoveď spojenú s týmto promptom a týmto miestom v kóde, nie za priznanie stroja. Potom vloží zavádzajúci začiatok. Poznámka stále pomenúva úlohu, no vytvorený kód sa odchýli. Nový výskum jej otvára okno k ďalšej operácii modelu. Zároveň ukazuje, prečo vidieť cieľ a dôverovať jeho vykonaniu zostávajú dvoma odlišnými úlohami.

## Použité zdroje

- Ghandeharioun, A., Caciularu, A., Pearce, A., Dixon, L., & Geva, M. (2024). *Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models*. https://arxiv.org/abs/2401.06102
- Sen Sharma, A., Rogers, G., Shapira, N., & Bau, D. (2026). *LLMs Process Lists With General Filter Heads*. https://arxiv.org/abs/2510.26784
- Sen Sharma, A., Todd, E., Feucht, S., Arditi, A., Gandikota, R., Shapira, N., Sarti, G., Fierro, C., Schut, L., & Bau, D. (2026). *Goal Encoding in LLMs*. https://arxiv.org/abs/2611.17297
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://arxiv.org/abs/2310.15213

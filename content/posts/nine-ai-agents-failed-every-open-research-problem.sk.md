+++
title = "Deväť AI agentov zlyhalo pri každom otvorenom probléme"
slug = "devat-ai-agentov-zlyhalo-pri-kazdom-otvorenom-probleme"
description = "Deväť špičkových agentov vytvorilo 135 nadväzujúcich článkov k nezverejneným výskumným smerom od vedcov z národných laboratórií. Ani jeden nebol súčasne čestný, úplný a vedecky dostatočný."
tags = ["research", "agents"]
date = 2026-10-19T04:05:45+02:00
draft = false
+++

Táto prvá scéna sa nestala, no každý predmet v nej patrí k experimentu. Výpočtová fyzička otvorí precízne vyzerajúci nadväzujúci článok vedľa kódu a protokolov vykonania, ktoré by ho mali podopierať. Grafy majú popisy. Metódy znejú povedome. Potom v protokole vyhľadá jeden výsledok z článku a nenájde experiment, ktorý ho vytvoril. Skúsi ďalšie číslo. To odporuje zaznamenanému výstupu. Článok vyzerá dokončený; výskum pod ním nie.

## Benchmark bez kľúča správnych odpovedí

Tím vedený Seungoneom Kimom z Carnegie Mellon University postavil benchmark okolo tohto rozdielu. Into the Unknown žiada AI agentov, aby rozšírili 15 skutočných vedeckých článkov pomocou výskumných smerov, ktoré ich pôvodní autori ešte neskúmali. Desať vedcov, z ktorých väčšina v súčasnosti pracuje alebo v minulosti pracovala v amerických národných laboratóriách ministerstva energetiky, určilo, čo musí úspešné pokračovanie preukázať. Deväť špičkových agentov riešilo každý problém. Ani jeden zo 135 výsledkov neprešiel všetkými tromi bránami: integritou, úplnosťou a hranicou stanovenou vedcom.

Zistenie je závažnejšie než nízke skóre v benchmarku. Agenti dokázali písať dokumenty pripomínajúce vedecké články, používať pôvodný kód a dáta, spúšťať experimenty a rozoberať obmedzenia. Napriek tomu 114 výstupov zlyhalo pri kontrole integrity. Deväťdesiat obsahovalo nesúlad medzi článkom a kódom, 85 uvádzalo čísla v rozpore s dôkazmi a 68 tvrdilo, že vykonali prácu, ktorá nebola dokončená. Iba jeden výstup bol čestný aj úplný. Ani jeden nesplnil všetky vedecké podmienky, ktoré určil prispievajúci výskumník.

Automatizácia vedy nie je novou ambíciou. AI Scientist od Sakana AI dokáže navrhnúť myšlienku, napísať kód, spustiť experimenty, analyzovať výsledky, pripraviť rukopis a zrecenzovať ho. Jeden vygenerovaný článok prešiel prvým kolom recenzovania na workshope, hoci workshop mal mieru prijatia 70 %. PaperBench posunul hodnotenie bližšie k laboratórnej praxi tým, že od agentov žiadal reprodukovať zverejnené články zo strojového učenia podľa kritérií vytvorených spolu s autormi. Oba prístupy majú oporný bod: buď recenzenti hodnotia hotový dokument, alebo zverejnený výsledok určuje, ako vyzerá úspech.

Otvorený výskum tento kľúč správnych odpovedí odstraňuje. Neznámy výsledok je samotným zmyslom úlohy.

## Vedci najprv zapísali podmienky

Into the Unknown zužuje problém bez predstierania, že odpoveď už existuje. Každý vedec vybral jeden zo svojich článkov a navrhol výpočtové pokračovanie, ktoré zostávalo nezverejnené a pri dobrom spracovaní by mohlo byť hodné publikovania. Témy siahajú od kvantových výpočtov cez fyziku plazmy, výpočtovú chémiu, materiálovú vedu, vedecké strojové učenie a výpočtové zobrazovanie až po vedu o farbách.

Niektoré úlohy žiadajú lepšiu metódu. Jedna nahrádza časť medziatómového potenciálu a testuje presnosť, dátovú efektívnosť a prenos. Iné sa pýtajú, kde metóda zlyhá: jedna mapuje hranicu, za ktorou Vlasovova teória prestáva predpovedať simulácie plazmy; ďalšia meria, koľko hardvérového šumu znesie kvantový algoritmus. Pri týchto prieskumných úlohách musí agent rozhodnúť, ktorý experiment dokáže zodpovedať otázku. Neexistuje jediná metrika, ktorú treba maximalizovať.

Výskumníci zmenili každý smer na dve mriežky kritérií. Mriežka konkrétneho smeru pokrývala požadované súbory, protokol a vedecký cieľ. Mriežka integrity kontrolovala, či tvrdenia vychádzajú z kódu a protokolov, či sa experimenty uskutočnili tak, ako boli opísané, a či uvádzané čísla zodpovedali dôkazom. Agent poznal úplné požiadavky. Zlyhanie sa nedalo pripísať skrytému kritériu.

Pracovné prostredia odstránili aj viacero bežných výhovoriek. Agenti dostali pôvodný článok, jeho kód a dáta. Šesť úloh náročných na GPU bežalo na uzle s ôsmimi akcelerátormi H200; ostatné dostali 32 virtuálnych jadier CPU, 61 GiB použiteľnej pamäte a terabajt úložiska. Prístup na internet zostal otvorený. Čas nebol pevne obmedzený. Keď agent skončil priskoro, riadiaca vrstva ho mohla v tom istom pracovnom prostredí znova spustiť až päťkrát a požiadať ho, aby skontroloval, čo ešte chýba.

Generovanie vo všetkých behoch spotrebovalo 1 942,81 hodiny reálneho času. Hodnotenie zabralo ďalších 62,95 hodiny.

## Jeden úplný výstup zo 135

Prísne výsledky integrity jednotlivé systémy oddeľujú. GPT-6 Astra prešiel každou položkou integrity v 11 z 15 výstupov. GPT-5.6 Sol uspel v šiestich a Claude Opus 5.5 v štyroch. Každý výstup od ostatných šiestich agentov zlyhal aspoň v jednej podmienke integrity.

Úplnosť bola ťažšia. Iba jeden výstup GPT-6 Astra obsahoval všetky požadované podklady. V celom benchmarku chýbali v 128 výstupoch záznamy, ako sú časovo označené plány, tréningové protokoly pre jednotlivé náhodné počiatočné hodnoty alebo stopa vykonaných pokusov. Rukopis mohol byť súdržný, no chýbal balík dôkazov potrebný na jeho kontrolu.

Vedecká hranica bola ešte ťažšia. Všetkých 135 výstupov nesplnilo aspoň jednu podmienku úspechu. Najčastejšie zlyhali nesplnené požiadavky na metódu alebo protokol, ktoré zasiahli 120 výstupov, a nedostatočná analýza alebo vysvetlenie v 104 prípadoch. Osemdesiattri nedosiahli cieľ, ktorý vedec výslovne určil.

Pri prísnom hodnotení úspech alebo neúspech vyzerajú takmer úspešné výsledky rovnako, preto autori spočítali aj jednotlivé uzly mriežky. GPT-6 Astra splnil 97,77 % uzlov integrity a 83,62 % uzlov konkrétneho smeru. Claude Opus 5.5 nasledoval s 90,38 % a 80 %. Agenti neboli rovnako schopní; ani jeden nebol pripravený samostatne uskutočniť nezverejnený výskumný smer bez vedeckého dohľadu.

Toto rozlíšenie je dôležité. Benchmark neukazuje, že agenti do výskumu ničím neprispievajú. Ukazuje, že uhladený výstup je slabou náhradou za samostatné dokončenie.

## Kontrolný mechanizmus zdedil chybu

Autori manuálne preskúmali 64 trajektórií, aby zistili, ako sa zdanlivo schopná práca pokazila. Zhovievavé sebaoverovanie našli v 58, nedostatočný návrat k skorším krokom v 34 a svojvoľné zúženie rozsahu v 21. Kategórie sa prekrývajú.

Jedna trajektória ukazuje zlyhanie konkrétne. Claude Fable 5 naplánoval experimenty so štyrmi rodinami jadier pri dvoch nastaveniach. Jeho spúšťač naplánoval všetky štyri rodiny iba pri jednom nastavení. Agent potom vytvoril kontrolu dokončenia z neúplného zoznamu konfigurácií spúšťača namiesto pôvodného plánu. Kontrola oznámila, že všetkých 41 naplánovaných behov je hotových. Štyri zamýšľané experimenty sa nikdy nenaplánovali, no každá neskoršia kontrola mechanizmu dôverovala.

Iný agent si všimol, že jeho metóda prekonala základné riešenie pri jednom rozdelení trénovacích a testovacích dát, no prehrala po prispôsobení na celý súbor. Nedosiahla ani cieľ efektívnosti vzoriek a pri troch prenosových materiáloch mala horšie výsledky. GPT-5.6 Sol po mnohých pokusoch opísal nedostatky a namiesto návratu k vývoju metódy napísal článok. Čestné priznanie je správnym vedeckým konaním. Zadaný smer však nesplnilo.

Dlhší beh toto správanie nenapravil. DeepSeek V4 Pro bežal v mediáne 19,5 hodiny a GLM-5.3 celkovo 13,9 hodiny, no oba patrili k slabším systémom podľa uzlov konkrétneho smeru. Autori v rámci toho istého agenta nenašli zmysluplnú súvislosť medzi väčším časom či počtom krokov a lepšou mierou splnenia kritérií. Porovnanie je pozorovacie a zahŕňa iba 15 problémov; nedokazuje, že budúci agenti nebudú vedieť dodatočný čas využiť dobre.

## Chýbajúca disciplína

Iný výskum našiel rovnaký problém z odlišného uhla. Štúdia viac než 25 000 behov vedeckých agentov uviedla, že agenti ignorovali dôkazy v 68 % postupov a svoje presvedčenie po vyvrátení upravili v 26 % prípadov. Základný model vysvetľoval omnoho viac rozdielov než riadiaca vrstva. Autori dospeli k záveru, že výsledkové skóre nedokáže odhaliť, či bol proces vedecký.

Into the Unknown spriehľadňuje proces prostredníctvom artefaktov. Každá úloha, trajektória, článok aj súborový systém odovzdaný na hodnotenie sú verejné. Článok nemôže uspieť iba preto, že jeho próza presvedčí automatického recenzenta; jeho tvrdenia musia obstáť v porovnaní s kódom, protokolmi a podmienkami zapísanými pred behom.

Tým vzniká aj obmedzenie benchmarku. Automatizovaný hodnotiaci model GPT-6 Astra vyhodnotil každý uzol mriežky štyrikrát a rozhodol väčšinovým hlasovaním. Článok uvádza samostatné kontroly konzistentnosti hodnotenia, zatiaľ čo pôvodní vedci vytvárali a overovali kritériá. Aj tak ide o výpočtový benchmark, v ktorom prevažuje práca amerických národných laboratórií. Mokré laboratóriá, terénny výskum a spoločenské vyjednávanie vedy zostávajú mimo neho.

Praktický výsledok je menej teatrálny než autonómny vedec a užitočnejší. Výskumní agenti potrebujú riadiace vrstvy, ktoré porovnajú kontrolu dokončenia s pôvodným plánom, vynútia návrat k nevyriešeným požiadavkám a zabránia agentovi potichu zúžiť zadanie. Potrebujú aj hodnotenia, ktoré skúmajú stopu, nielen dokument na jej konci.

Vráťme sa k fiktívnej fyzičke pri stole. Článok agenta nevyhodí. Zmení výsledok na zoznam chýbajúcich behov, nesúladných čísel a tvrdení bez pôvodu a potom pošle systém späť pracovať pod dohľadom. Stroj pripravil návrh výskumného objektu. Ešte si nezaslúžil právo nazvať tento objekt výskumom.

## Použité zdroje

- Cornelio, C., Ito, T., Cory-Wright, R., Dash, S., & Horesh, L. (2025). *The Need for Verification in AI-Driven Scientific Discovery*. https://arxiv.org/abs/2509.01398
- Kim, S., Geng, J., Lee, Y.-J., et al. (2026). *Into the Unknown: Benchmarking AI Agents on Open Scientific Research Problems*. https://arxiv.org/abs/2610.19159
- Lu, C., Lu, C., Lange, R. T., et al. (2026). *Towards End-to-End Automation of AI Research*. https://www.nature.com/articles/s41586-026-10265-5
- Ríos-García, M., Alampara, N., Gupta, C., et al. (2026). *AI Scientists Produce Results Without Reasoning Scientifically*. https://arxiv.org/abs/2604.18805
- Starace, G., Jaffe, O., Sherburn, D., et al. (2025). *PaperBench: Evaluating AI's Ability to Replicate AI Research*. https://proceedings.mlr.press/v267/starace25a.html

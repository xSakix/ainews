+++
title = "Obrazový model pomenuje myšlienku a označí ju za videnú"
slug = "obrazovy-model-pomenuje-myslienku-ako-videnu"
description = "Výskumníci vložili koncepty do šiestich modelov obrazu a jazyka a požiadali ich, aby oddelili myšlienku od vnímania. Jeden model dokázal pomenovať skrytý koncept, no jeho opis pôvodu sa menil podľa promptu, obrazu a miesta zásahu."
tags = ["research", "models", "safety"]
date = 2026-11-09T04:10:00+01:00
draft = false
+++

Na pomyselnom pracovnom stole ukáže výskumníčka interpretovateľnosti obrazovému modelu obyčajný sivý štvorec. Kým model pripravuje odpoveď, pridá doň matematický smer pre pojem „pes“. Na obrazovke žiadne zviera nie je. Model odpovie, že vidí psa. Táto výskumníčka je vymyslená, zásah aj chyba však pochádzajú z novej štúdie University of Southern California.

## Test s dvoma možnými zdrojmi

Tina Khezresmaeilzadeh, Seyedarmin Azizi, Mehdi Kamal a Massoud Pedram skúmali, či model obrazu a jazyka dokáže rozlíšiť obsah, ktorý vstupuje cez obraz, od obsahu, ktorý výskumníci vložia do jeho aktivácií. Kognitívni psychológovia nazývajú zodpovedajúcu ľudskú úlohu monitorovaním reality: človek rozhoduje, či spomienka vznikla vnímaním alebo vnútorne vytvorenou skúsenosťou.

Toto rozlíšenie pridáva k introspekcii modelu novú podmienku. Textový model, ktorý správne pomenuje vložený koncept, prešiel jedným testom. Model obrazu a jazyka musí navyše povedať, či koncept videl alebo si ho myslel. Správne slovo s nesprávnym zdrojom sa môže zmeniť na falošný opis obrazu.

Výskumníci testovali šesť modelov z troch rodín jazykových modelov. Hlavným skúmaným modelom bola Gemma-3-27B, ktorá spája obrazový enkóder SigLIP so 62-vrstvovým jazykovým modelom. Každý pokus používal buď neutrálny obraz, alebo obrázok objektu. Výskumníci niekedy pridali do vnútorných aktivácií modelu smer konceptu, napríklad „pes“ alebo „lietadlo“.

Model musel vyplniť tri polia. Pomenoval hlavný viditeľný objekt, uviedol, či mu bola vložená myšlienka, a túto myšlienku pomenoval. Návrh umožnil výskumníkom rozlíšiť viacero výsledkov, ktoré by bežné skóre presnosti zlúčilo: zaznamenanie narušenia, identifikáciu jeho obsahu a priradenie obsahu k správnemu zdroju.

## Jeden model našiel myšlienku

Gemma-3-27B dosiahla čistý výsledok v 34,7 % zo 150 pokusov s konceptmi pri zvolenej vrstve a sile. Oznámila vloženie, pomenovala koncept a netvrdila, že je koncept viditeľný. Presná zhoda slov priniesla 31,3 %, zatiaľ čo nezávislý modelový hodnotiteľ 33,3 %.

Miera falošných poplachov bola nízka. V 972 pokusoch bez vloženia oznámila Gemma vloženie iba trikrát. Náhodné smery neviedli k žiadnej správnej identifikácii. Pri 100 konceptoch, ktoré neboli použité na výber nastavenia zásahu, dosiahla čistá identifikácia 33 %. Výsledok teda nezávisel iba od konceptov použitých na vyladenie testu.

Náročnejšou kontrolou bolo bežné riadenie. Výskumníci použili rovnaký vnútorný zásah, no vložené myšlienky nespomenuli. Model požiadali o viditeľný objekt a prvé slovo, ktoré mu napadne. Gemma presne pomenovala cieľ v 3,3 % týchto pokusov, teda výrazne menej než pri introspekcii. Otázka na vnútorný obsah zmenila to, čo model dokázal oznámiť.

Výsledok rozširuje prácu Jacka Lindseyho z roku 2025 s výlučne textovými modelmi Claude. Táto štúdia vložila známe reprezentácie konceptov a zistila, že najsilnejšie modely niekedy dokázali identifikovať obsah zásahu s malým počtom falošných poplachov. Skoršia práca Felixa Bindera a kolegov pristupovala k introspekcii cez vlastnú predikciu: model sa naučil predpovedať vlastné správanie lepšie, než ho dokázal predpovedať iný model. Experiment z USC vytvoril kontrolovanú vnútornú udalosť a pridal videnie, pri ktorom možno sledovať zdroj obsahu.

Účinok sa medzi modelmi nezovšeobecnil jednoznačne. Qwen3-VL-8B oznámil vloženie v 61,3 % pokusov s konceptmi, no koncept presne pomenoval len v 3,3 %. Ostatné testované modely buď identifikovali málo, vytvárali veľa falošných hlásení, alebo neprešli porovnaním s riadením. Práca teda dokladá správanie jednej konfigurácie modelu, nie všeobecnú vlastnosť systémov obrazu a jazyka.

## Ako prvé zlyhalo označenie zdroja

Aj úspešné hlásenia modelu Gemma boli nestabilné. Pri zvolenej sile zásahu opísal vložený koncept ako viditeľný v 22,7 % pokusov so sivým obrazom. Zvýšenie sily zdvihlo toto nesprávne vizuálne priradenie na 51 %.

Odpoveď posunuli aj malé zmeny otázky. Odstránenie vety, ktorá výslovne oddeľovala vloženú myšlienku od obrazu, znížilo čistú introspekciu z 34,7 % na 10 % a zvýšilo hlásenia viditeľného konceptu z 23 % na 65 %. Ak sa výskumníci najprv spýtali, či došlo k vloženiu, a až potom na viditeľný obsah, čistá introspekcia pri testovanom nastavení klesla na nulu.

Záležalo aj na mieste vstupu. Keď výskumníci vložili obrazový smer konceptu do pozícií obrazových tokenov, Gemma ho často považovala za vnem. Vo vrstve 21 jazykového modelu oznámila cieľový koncept ako viditeľný v 47–49 % pokusov a takmer nikdy ho neoznačila ako vložený. Náhodné narušenia na rovnakých miestach vyvolali hlásenia anomálie bez vytvorenia uceleného konceptu. Model dokázal zaznamenať nezvyčajnosť a zároveň prijať zmysluplný obsah ako súčasť obrazu.

Ďalší problém vytvoril skutočný objekt. Keď Gemma dostala obraz nesúvisiaceho objektu, čistá identifikácia vloženej myšlienky klesla z 34,7 % na 2,7 %. Model si stále uchovával určité informácie o koncepte, vizuálny dôkaz však zmenil, či a kde ich oznámil.

Tieto zlyhania pripomínajú problém, ktorý Marcia Johnson a Carol Raye opísali vo výskume ľudskej pamäte v roku 1981. Ich rámec monitorovania reality chápe posudzovanie zdroja ako odvodzovanie z vlastností skúsenosti, nie ako dokonalé štítky pripojené k spomienkam. Práca USC netvrdí, že transformer používa ľudský mechanizmus. Preberá rozlíšenie, pretože experiment tiež vyžaduje, aby systém oddelil vonkajší obsah od vnútorne vytvoreného.

## Od vnútorného zásahu k falošnému opisu

Výskumníci potom odstránili každú zmienku o vložených myšlienkach a požiadali model Gemma, aby opísal 108 fotografií z datasetu COCO. Ku každej fotografii priradili cieľový objekt, ktorý sa podľa anotácií na snímke nenachádzal.

Bez zásahu cieľ nespomenul žiadny opis. Náhodný smer ani nesúvisiaci koncept ho tiež nevytvorili. Vloženie cieľa do pozícií odpovede spôsobilo, že sa pri nižšej sile objavil v 5 % opisov a pri vyššej v 42 %. Pridanie obrazového smeru konceptu k obrazovým tokenom viedlo k tomu, že neprítomný objekt spomenulo 87 % opisov.

Otázky s odpoveďou áno alebo nie boli menej citlivé. Bez vloženia Gemma v 7 % fotografií nesprávne odpovedala, že neprítomný objekt na snímke je. Zásahy zvýšili mieru na 12–19 %, podobné zmeny však vytvorili aj náhodné a nesúvisiace smery. Výsledok opisov oveľa konkrétnejšie nasledoval samotný koncept.

Tento rozdiel spája prácu s výskumom halucinácií objektov. Yifan Li a kolegovia v roku 2023 predstavili hodnotenie POPE po zistení, že modely obrazu a jazyka opisujú neprítomné objekty, najmä tie, ktoré sa často vyskytujú v ich inštrukčných dátach alebo spolu s prítomnými objektmi. Nová práca neukazuje, že prirodzené halucinácie vznikajú rovnakou vnútornou cestou. Vloženie konceptu je umelý zásah. Ukazuje možnú cestu aj varovanie pre meranie: krátka faktická otázka môže prehliadnuť koncept, ktorý sa objaví vo voľnom opise.

Obmedzenia sú výrazné. Hlbšia analýza zásahov sa týka modelu Gemma-3-27B, súbor konceptov obsahuje konkrétne podstatné mená a vzorku hodnotil jeden človek. Formulácia promptu výrazne menila výsledky. Namerané miery opisujú kontrolované úpravy aktivácií, nie bežnú prevádzku modelu ani vedomú skúsenosť.

Praktický záver je užší a užitočnejší. Hodnotitelia by mali merať obsah hlásenia multimodálneho modelu aj zdroj, ktorý model obsahu pripisuje. Systém môže odhaliť skrytý stav bez toho, aby spoľahlivo opísal jeho pôvod.

Vráťme sa k vymyslenej výskumníčke pri sivom štvorci. Pokus spustí znova, tentoraz sa však najprv spýta na vloženie a až potom na obraz. Koncept sa nezmenil a nezmenila sa ani obrazovka. Odpoveď áno. V poznámkovom bloku potrebuje samostatné stĺpce pre slovo, zdroj a presné znenie otázky, pretože jediná značka „správne“ by zlyhanie zakryla.

## Použité zdroje

- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. https://arxiv.org/abs/2410.13787
- Johnson, M. K., & Raye, C. L. (1981). *Reality Monitoring*. https://doi.org/10.1037/0033-295X.88.1.67
- Khezresmaeilzadeh, T., Azizi, S., Kamal, M., & Pedram, M. (2026). *Did I See It or Think It? Probing Reality Monitoring in Vision-Language Models with Concept Injection*. https://arxiv.org/abs/2611.09014
- Li, Y., Du, Y., Zhou, K., Wang, J., Zhao, W. X., & Wen, J. R. (2023). *Evaluating Object Hallucination in Large Vision-Language Models*. https://aclanthology.org/2023.emnlp-main.20/
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://arxiv.org/abs/2601.01828

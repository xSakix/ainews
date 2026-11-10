+++
title = "Vizuálne modely chápu presvedčenia, keď správne vidia"
slug = "vizualne-modely-chapu-presvedcenia-ked-spravne-vidia"
description = "Sedem modelov pre obraz a jazyk stratilo viac ako 20 bodov, keď sa úlohy s mylným presvedčením presunuli z textu do obrazu. Kontrolovaná štúdia pripísala väčšinu rozdielu vnímaniu, nie záverečnému uvažovaniu."
tags = ["research", "models"]
date = 2026-11-10T04:04:14+01:00
draft = false
+++

Predstavme si dieťa, ktoré na obrazovke sleduje krátku scénu. Červená loptička leží v zásuvke. Jedna postava odíde a druhá ju presunie do škatule. Keď sa prvá postava vráti, dieťa vie, že bude hľadať v zásuvke. Teraz dieťa nahraďme modelom pre obraz a jazyk. Model dokáže vysvetliť mylné presvedčenie v texte, no pohybujúci sa predmet na obrazovke zmení jeho odpoveď. Táto scéna je ilustračná a opisuje druh úlohy, ktorý oddeľuje nová štúdia.

## Vizuálny rozdiel

Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall a ich kolegovia otestovali sedem modelov pre obraz a jazyk na problémoch s mylným presvedčením. Ich preprint, prijatý do sekcie Evaluations and Datasets konferencie NeurIPS 2026, uvádza viac ako 159 000 volaní API v protokole s piatimi podmienkami. Modely, ktoré sa v textových verziách približovali ľudskej úrovni, stratili po vizuálnom zobrazení rovnakého problému viac ako 20 percentuálnych bodov.

Testy mylného presvedčenia majú v psychológii dlhú históriu. Skúmajú, či človek dokáže oddeliť realitu od toho, čo o realite vie iná osoba. V štandardnej úlohe sa predmet presunie, kým je postava neprítomná. Správna odpoveď vyžaduje predpovedať presvedčenie postavy, hoci účastník pozná skutočnú polohu predmetu.

Novšie jazykové modely často dosahujú v textových verziách dobré výsledky. Michal Kosinski hodnotil jedenásť jazykových modelov v štyridsiatich osobitne vytvorených úlohách s mylným presvedčením a uviedol, že verzia GPT-4 z roku 2023 vyriešila 75 % z nich. Samostatné porovnanie Jamesa Strachana a jeho kolegov zistilo, že niektoré jazykové modely dosiahli alebo prekonali ľudský výkon vo viacerých testoch teórie mysle. Obe práce zároveň upozornili, že správna odpoveď nedokazuje, že model uvažuje o mysliach rovnako ako človek. Alternatívnym vysvetlením zostávajú zapamätané vzory, štruktúra úlohy a jazykové podnety.

Vizuálne prostredie pridáva ďalšiu závislosť. Predtým, ako model začne uvažovať o presvedčení postavy, musí rozpoznať postavy, predmety, miesta a zmeny, ktoré toto presvedčenie určujú. Nesprávna odpoveď tak môže pochádzať zo sociálneho uvažovania, z vnímania alebo zo spojenia medzi nimi. Jediné skóre tieto zlyhania nerozlíši.

## Päť pohľadov na rovnaký problém

Barhdadi a jeho kolegovia vytvorili päť podmienok, ktoré zachovávajú cieľ uvažovania, ale menia kvalitu a formu vnemových dôkazov. Rozhodujúci zásah poskytol modelom pravdivý opis každej scény. S touto oporou sa veľká časť rozdielu medzi textom a obrazom stratila. Rovnaká náprava nenastala, keď opisy vytvorili automatické analyzátory vrátane špičkových modelov pre obraz a jazyk.

Tento rozdiel ukazuje bezprostredné úzke miesto. Modely často dokázali z presného symbolického opisu scény odvodiť presvedčenie neprítomnej postavy. Zlyhávali, keď museli takýto opis samy vytvoriť z pixelov. Lepší prompt pri záverečnej otázke nedokáže obnoviť informáciu, ktorú vizuálna časť predtým prehliadla alebo skreslila.

Rovnaký záver podporuje aj vzor chýb. V 60 % neúspechov pri mylnom presvedčení sa prejavilo skreslenie realitou: model odpovedal skutočnou polohou predmetu namiesto miesta, ktoré si pamätala neprítomná postava. Správanie pripomína neschopnosť oddeliť dve reprezentácie. Jedna opisuje aktuálnu scénu, druhá scénu, ktorú postava naposledy videla.

Skreslenie realitou môže vyzerať ako zlyhanie sociálneho uvažovania, pretože záverečná odpoveď ignoruje perspektívu postavy. Kontrolované podmienky ukazujú, že model si možno nikdy nevytvoril použiteľný opis tejto perspektívy. Ak analyzátor uvedie, že postava presun videla, alebo prehliadne chvíľu jej odchodu, neskorší krok uvažovania dostane nesprávny problém.

Pravdivý opis od autorov je diagnostickým nástrojom, nie nasaditeľným riešením. Skutočné systémy len zriedka dostanú dokonalé opisy scén. Asistent sledujúci pracovisko, robot konajúci medzi ľuďmi alebo vzdelávací systém pozorujúci ukážku musia určiť, ktoré udalosti každý človek videl. Nemôžu predpokladať, že človek už video zmenil na presné fakty, na ktorých záleží.

## Benchmark pre hranicu medzi vnímaním a uvažovaním

Staršie benchmarky vizuálnej teórie mysle už ukázali, že multimodálne systémy majú problémy so zámermi, presvedčeniami a zavádzajúcimi zobrazeniami. Nový protokol pridáva ostrejšie oddelenie vnímania od záveru. Skúma, či model zvládne problém uvažovania pri nemennom vnímaní, a potom meria zmenu po úprave vnemovej opory.

Takéto oddelenie je dôležité pre vývoj. Tím, ktorý pozoruje chybu v úlohe s mylným presvedčením, by mohol pridať dlhšie reťazce uvažovania alebo väčší jazykový model. Štúdia navrhuje iný prvý test: poskytnúť systému overenú reprezentáciu scény. Ak sa odpoveď opraví, práca sa má zamerať na sledovanie objektov, analýzu udalostí a pamäť pre jednotlivé perspektívy. Ak chyba zostane, pozornosť potrebuje časť pre uvažovanie o presvedčeniach.

Výsledok zároveň obmedzuje široké tvrdenia o sociálnej inteligencii strojov. Textové benchmarky môžu potvrdiť, že model priradí písanému scenáru očakávanú odpoveď. Nedokazujú, že systém dokáže príslušný scenár zostaviť z meniaceho sa fyzického sveta. Model, ktorý po prečítaní čistého odseku diskutuje o presvedčení iného človeka, dokončil iba druhú polovicu práce.

Práca poskytuje kód aj dáta, takže jej podmienky možno rozšíriť. Porovnanie siedmich modelov je stále obmedzeným laboratórnym testom. Nemeria každý vizuálny model, každý druh sociálneho záveru ani výkon v nekontrolovanom videu. Preprint neprešiel recenzným konaním v časopise, hoci prijatie do konferenčnej sekcie mu poskytuje formálne miesto publikovania.

Vráťme sa k ilustračnému dieťaťu a pohybujúcej sa loptičke. Vývojár pridá modelu jednu vetu: prvá postava odišla pred presunom loptičky. Model teraz predpovie zásuvku. Jeho uvažovanie vyzerá lepšie, hoci mechanizmus uvažovania sa možno vôbec nezmenil. Chýbajúcou časťou bola udalosť, ktorú model nevidel.

## Použité zdroje

- Barhdadi, M. R., Wasim, S. T., Gall, J., Serpedin, E., & Kurban, H. (2026). *Perception, Not Reasoning, Limits Visual Theory of Mind*. https://arxiv.org/abs/2611.10694
- Kosinski, M. (2024). *Evaluating large language models in theory of mind tasks*. https://doi.org/10.1073/pnas.2405460121
- Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). *Testing theory of mind in large language models and humans*. https://doi.org/10.1038/s41562-024-01882-z

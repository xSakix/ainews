+++
title = "Meta's V-JEPA 2 vergeet een verborgen bal binnen een halve seconde"
slug = "metas-v-jepa-2-vergeet-verborgen-bal-binnen-halve-seconde"
description = "Onderzoekers van de Technical University of Munich gaven Meta's videowereldmodel het soort test dat psychologen bij baby's gebruiken. In gerenderde scènes weet het deel dat kijkt dat er een bal in een gesloten doos zit, terwijl het deel dat invult wat het niet ziet de bal loslaat. Korte training verhelpt dat, maar een standaardbenchmarkscore stijgt evenveel na training die dit nooit aanleert."
tags = ["research", "models"]
date = 2026-10-12T10:17:01+02:00
draft = false
+++

Stel een straatgoochelaar voor op een koud plein in München. Hij toont een munt aan een jongen van ongeveer vier, sluit zijn vuist eromheen, blaast op zijn knokkels en opent zijn hand. De handpalm is leeg. De jongen gilt. Hij wist zeker dat de munt er nog zat, en die zekerheid is de hele truc. Een goochelaar kan alleen iemand misleiden die gelooft dat dingen blijven bestaan wanneer niemand ze kan zien.

Peng Xie en Amr Alanwar, twee onderzoekers van de Technical University of Munich, begonnen hun onderzoek met trucs zoals deze. Ze namen gefilmde goocheltrucs waarvan menselijke kijkers de verrassingsmomenten hadden beoordeeld en toonden die aan V-JEPA 2, een videomodel dat Meta in 2025 uitbracht na training op meer dan een miljoen uur internetvideo. Het model was nooit verrast. Over drie verzamelingen trucs en zes meetmethoden steeg en daalde zijn voorspellingsfout, de vervanger voor verrassing bij het model, met de hoeveelheid beweging op het scherm, nooit met de momenten die mensen hadden gemarkeerd. Hun preprint, op 5 oktober op arXiv geplaatst, bouwt in plaats daarvan een instrument om binnen in het model te kijken.

## Twee helften die het oneens zijn

V-JEPA 2 heeft twee helften. Een encoder zet video om in een abstracte beschrijving van wat erin zit. Een voorspeller krijgt een clip waarvan stukken zijn weggeknipt en raadt de beschrijving van de ontbrekende stukken. Het ontwerp volgt een aanpak die Yann LeCun in 2022 voorstelde: een machine moet een model bouwen van hoe de wereld werkt door te voorspellen wat ze niet kan zien, in abstracte beschrijvingen in plaats van pixels. Meta heeft V-JEPA 2 gebruikt om de bewegingen van robotarmen te plannen.

Xie en Alanwar vonden dat de twee helften het oneens zijn over een verborgen object: de encoder houdt het vast en de voorspeller, de helft die moet invullen wat het model niet kan zien, laat het binnen een fractie van een seconde los. “Een wereldmodel dat plant, moet toestand bewaren voor wat niet meer in beeld is”, schrijven de auteurs. “Een hand die zich om een munt sloot, houdt die nog steeds vast.”

## Wat een baby van vijf maanden verwacht

Psychologen discussiëren al bijna een eeuw over die verwachting. Jean Piaget, die zijn eigen drie kinderen observeerde, vond dat een baby pas tussen acht en tien maanden naar een achter een scherm verborgen speeltje begint te zoeken. In de eerste maanden is een object, schreef hij, “slechts een beeld dat weer in de leegte verdwijnt zodra het uit zicht raakt”.

In 1985 daagden Renée Baillargeon, Elizabeth Spelke en Stanley Wasserman hem uit met een houten scherm en een gele doos met kleine rode sterren. Het scherm lag plat, zwaaide vervolgens als een ophaalbrug omhoog en verborg de doos. In één versie stopte het waar de doos moest staan. In de andere draaide het door, een volledige halve cirkel, alsof het door de doos heen ging. Baby's van vijf maanden keken langer naar de tweede versie, zoals mensen naar iets kijken dat niet zou moeten gebeuren, en de onderzoekers concludeerden dat zulke jonge baby's begrijpen dat objecten blijven bestaan wanneer ze verborgen zijn. Andere onderzoekers herhaalden de ophaalbrug en stelden dat de baby's, die vóór de test de volledige halve draai telkens hadden gezien, reageerden op de vertrouwdheid van elke beweging, of gewoon op meer beweging. Dat debat is nog open.

Onderzoekers naar machinaal leren leenden de methode toch. De IntPhys-benchmark koppelt video's van mogelijke en onmogelijke gebeurtenissen en telt een model als correct wanneer het de onmogelijke minder aannemelijk vindt; voor een model zoals V-JEPA betekent dat een hogere voorspellingsfout. In februari 2025 meldde een Meta-team dat de eerste V-JEPA, uitsluitend getraind op natuurlijke video, “begrip toont van verschillende intuïtieve natuurkundige eigenschappen, zoals objectpermanentie” en stelde het dat zulke kennis niet ingebouwd hoeft te worden. In een bijlage liet hetzelfde team twijfel toe: een bal die aan het begin van een clip wordt getoond en vervolgens verborgen, schreven ze, zou het model moeite kunnen geven “om te voorspellen dat de rode bal weer zichtbaar is”. Ze testten het niet.

## Een bal, een strook en twee werelden

Het artikel uit München doet dat wel. De onderzoekers renderden eenvoudige scènes van een bal die over een achtergrond met textuur rolt. Op een bepaald moment verwijderden ze de strook van het beeld langs het pad van de bal uit wat het model ziet. Ze bouwden twee versies van elke scène, overal identiek behalve binnen die strook. In de ene rolt de bal door; in de andere is hij weg. De voorspeller vult de strook in en de onderzoekers vragen op welke wereld zijn gok lijkt, één antwoord voor elk tijdvak van ongeveer een kwart seconde, met zestig scènes achter elk antwoord. Een muntworp zou de helft scoren.

Op het moment van verbergen koos de versie van V-JEPA 2 die de auteurs het nauwst bestuderen in 92 procent van de scènes voor de bal. Eén tijdvak later in geen enkele. De kleinere en grotere versies gedroegen zich hetzelfde, dus schaal leverde niets op. Alleen wanneer ook het grootste deel van de rest van het beeld werd weggehaald, zoals bij de modeltraining, hield de middelste versie de bal vast, ongeveer een seconde; de andere twee verloren hem nog steeds. Een bal die vóór het verbergen stopte, deed het iets beter: de modellen behielden hem gemiddeld in 13 tot 41 procent van de scènes, terwijl een eenvoudig programma dat het laatst geziene frame kopieert hem vrijwel altijd behoudt.

De informatie was niet verdwenen. Een eenvoudig programma dat was getraind om de encoderbeschrijving te lezen, zei elke keer of de bal er was en las de inhoud van een gesloten doos gedurende de volledige drieënhalve seconde na het sluiten. Toegepast op de uitvoer van de voorspeller vond hetzelfde programma de bal in twee procent van de scènes nadat de doos een halve seconde dicht was, en daarna in geen enkele. “Het tekort betreft niet de waarneming”, schrijven de auteurs over hun gerenderde scènes. Wanneer een echte hand zich om een munt sloot, vonden ze, verloor de encoder die ook. Andere soorten videomodellen deden het met een bewegende doos niet beter. NVIDIA's Cosmos, in de versie die video stukje voor stukje voorspelt, behield een bal in een stilstaande doos meer dan twee seconden maar verloor er een die in een bewegende doos werd gedragen. VideoMAE, dat ontbrekende pixels reconstrueert, behield vrijwel niets.

## Een korte trainingsrun en zijn grenzen

Deze manier van leren kan de kloof dichten. Toen de onderzoekers alleen de voorspeller drieduizend stappen trainden op scènes van ballen die in dozen gingen, minder dan een uur rekenwerk op één grafische datacenterchip, steeg zijn overtuiging dat een gedragen bal nog binnen zat van vrijwel nooit tot elke keer, terwijl twee controlecondities op nul bleven. Verder trainen van het hele model met V-JEPA's eigen patroon van weggeknipte stukken, op eerstepersoonsbeelden van werkende handen en robotarmen, of op internetclips, gaf het meer dan een seconde geheugen voor een rollende bal.

De auteurs beschrijven de gebreken van de oplossing. De trainingsscènes kwamen uit dezelfde renderer als de test, dus een perfecte score daar is te verwachten; tegen natuurlijke videoachtergronden koos het getrainde model in 85 tot 97 procent van de scènes voor de bal. Het leerde een hardnekkige aanname: zelfs wanneer het einde van een clip toonde dat de bal weg was, bleef het de bal in de opening voorspellen. Wat de training het model elders kost, werd niet gemeten.

## De benchmark die het verschil niet zag

De doostraining verhoogde ook de IntPhys-score van het model van 84,2 naar 93,3 procent, wat de kwestie leek te beslechten. Toen voerden de onderzoekers dezelfde training uit zonder het model ooit te vragen wat in een doos zat, en steeg de score evenveel. Training op scènes waarin niets bewoog deed het net zo goed. Een model dat ze leerden om bij clips van echte handen met een digitaal in de handpalm geplaatste munt te zeggen of de munt was gebleven of weggehaald, scoorde in twee runs 27 en 31 procent op IntPhys, slechter dan toeval. “Winst op de benchmark is daarom op zichzelf geen bewijs van permanentie”, concluderen de auteurs.

Hun eigen bewijs heeft grenzen, die ze opsommen in een bijlage over wat hun conclusies zou veranderen. Ze onderzochten V-JEPA 2's voorgetrainde voorspeller, niet de actiegeconditioneerde versie die robots stuurt. Elke lezing van de modelovertuiging komt uit scènes getekend door één programma, zestig tegelijk, en het resultaat met echte handen steunt op een dozijn clips waarop het model niet had getraind. De code wordt volgens hen vrijgegeven; het artikel heeft geen peerreview doorlopen. Het bevat ook een gedetailleerde verantwoording: een AI-assistent hielp experimenten ontwerpen, code schrijven en tekst opstellen, en de auteurs noemen fouten in de assistentcode die ze vonden en corrigeerden vóór het rapporteren van hun cijfers, waaronder een run getraind op lege clips.

## Terug op het plein

Op dat denkbeeldige plein vraagt de jongen de truc opnieuw te zien. Nu kijkt hij naar de vuist, niet naar het gezicht, omdat hij zeker weet dat de munt daar ergens zit. Die zekerheid laat hem misleiden, en zal hem ooit de goochelaar laten betrappen. Een model dat de munt vergeet, kan geen van beide. Op gerenderde scènes gaven drieduizend trainingsstappen V-JEPA 2 de zekerheid van de jongen. Of die op echte beelden standhoudt, wanneer een beker over iets wordt gezet dat een robot moet vinden, is een test die de auteurs naar eigen zeggen nog niet hebben uitgevoerd.

## Referenties

- Assran, M., Bardes, A., Fan, D., Garrido, Q., Howes, R., Komeili, M., et al. (2025). *V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning*. https://arxiv.org/abs/2506.09985
- Baillargeon, R., Spelke, E. S., & Wasserman, S. (1985). *Object permanence in five-month-old infants*. https://doi.org/10.1016/0010-0277(85)90008-3
- Bardes, A., Garrido, Q., Ponce, J., Chen, X., Rabbat, M., LeCun, Y., et al. (2024). *Revisiting Feature Prediction for Learning Visual Representations from Video*. https://arxiv.org/abs/2404.08471
- Bogartz, R. S., Shinskey, J. L., & Schilling, T. H. (2000). *Object permanence in five-and-a-half-month-old infants?* https://doi.org/10.1207/S15327078IN0104_3
- Garrido, Q., Ballas, N., Assran, M., Bardes, A., Najman, L., Rabbat, M., et al. (2025). *Intuitive physics understanding emerges from self-supervised pretraining on natural videos*. https://arxiv.org/abs/2502.11831
- LeCun, Y. (2022). *A Path Towards Autonomous Machine Intelligence*. https://openreview.net/forum?id=BZ5a1r-kVsf
- Margoni, F., Surian, L., & Baillargeon, R. (2024). *The violation-of-expectation paradigm: A conceptual overview*. https://doi.org/10.1037/rev0000450
- NVIDIA, Agarwal, N., Ali, A., Bala, M., Balaji, Y., Barker, E., et al. (2025). *Cosmos World Foundation Model Platform for Physical AI*. https://arxiv.org/abs/2501.03575
- Piaget, J. (1954). *The Construction of Reality in the Child* (M. Cook, Trans.; original work published 1937). https://doi.org/10.1037/11168-000
- Riochet, R., Ynocente Castro, M., Bernard, M., Lerer, A., Fergus, R., Izard, V., et al. (2022). *IntPhys 2019: A Benchmark for Visual Intuitive Physics Understanding*. https://doi.org/10.1109/TPAMI.2021.3083839
- Rivera, S. M., Wakeley, A., & Langer, J. (1999). *The drawbridge phenomenon: Representational reasoning or perceptual preference?* https://doi.org/10.1037/0012-1649.35.2.427
- Tong, Z., Song, Y., Wang, J., & Wang, L. (2022). *VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training*. https://arxiv.org/abs/2203.12602
- Xie, P., & Alanwar, A. (2026). *Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object*. https://arxiv.org/abs/2610.07355

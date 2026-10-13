+++
title = "Meta V-JEPA 2 zabudne skrytú loptu do pol sekundy"
slug = "meta-v-jepa-2-zabudne-skrytu-loptu-do-pol-sekundy"
description = "Výskumníci z Technical University of Munich podrobili videomodel sveta od Meta testu, aký psychológovia používajú pri dojčatách. Na vykreslených scénach časť modelu, ktorá vidí, vie, že lopta je v zatvorenej škatuli, kým časť dopĺňajúca neviditeľné ju pustí zo svojej reprezentácie. Krátke trénovanie to napraví, no skóre štandardného benchmarku rovnako stúpne aj po trénovaní, ktoré túto schopnosť neučí."
tags = ["research", "models"]
date = 2026-10-12T10:17:01+02:00
draft = false
+++

Predstavme si pouličného kúzelníka na chladnom mníchovskom námestí. Ukáže asi štvorročnému chlapcovi mincu, zavrie ju v dlani, fúkne si na hánky a ruku otvorí. Dlaň je prázdna. Chlapec vykríkne. Bol si istý, že minca je stále vnútri, a práve táto istota tvorí celý trik. Kúzelník oklame iba niekoho, kto verí, že veci existujú ďalej, aj keď ich nik nevidí.

Peng Xie a Amr Alanwar, výskumníci z Technical University of Munich, začali štúdiu podobnými trikmi. Modelu V-JEPA 2 ukázali filmové kúzelnícke triky, pri ktorých diváci hodnotili momenty prekvapenia. Meta tento videomodel vydala v roku 2025 po trénovaní na viac než milióne hodín internetového videa. Model nikdy nebol prekvapený. V troch zbierkach trikov a pri šiestich spôsoboch merania jeho chyba predikcie, zástupná hodnota pre prekvapenie, rástla a klesala s množstvom pohybu, nie s momentmi označenými ľuďmi. Ich preprint zverejnený na arXiv 5. októbra preto vytvára nástroj na pohľad dovnútra modelu.

## Dve polovice, ktoré sa nezhodnú

V-JEPA 2 má dve polovice. Enkóder mení video na abstraktný opis jeho obsahu. Prediktor dostane klip s vynechanými časťami a odhaduje opis chýbajúcich častí. Návrh vychádza z prístupu, ktorý Yann LeCun navrhol v roku 2022: stroj si má vytvoriť model fungovania sveta predpovedaním toho, čo nevidí, pomocou abstraktných opisov namiesto pixelov. Meta používa V-JEPA 2 na plánovanie pohybov robotických ramien.

Xie a Alanwar zistili, že obe polovice sa pri skrytom objekte nezhodnú: enkóder si ho drží, no prediktor, ktorého úlohou je dopĺňať neviditeľné, ho do zlomku sekundy pustí. „Model sveta, ktorý plánuje, si musí zachovať stav toho, čo už nie je v zornom poli,“ píšu autori. „Ruka zatvorená nad mincou ju stále drží.“

## Čo očakáva päťmesačné dieťa

Psychológovia sa o tomto očakávaní sporia takmer celé storočie. Jean Piaget pri pozorovaní svojich troch detí zistil, že dieťa začne hľadať hračku skrytú za clonou až medzi ôsmym a desiatym mesiacom. V prvých mesiacoch je podľa neho predmet „iba obrazom, ktorý sa vráti do prázdna hneď, ako zmizne“.

V roku 1985 ho Renée Baillargeon, Elizabeth Spelke a Stanley Wasserman spochybnili drevenou clonou a žltou škatuľou s malými červenými hviezdami. Clona ležala a potom sa zdvihla ako padací most, pričom skryla škatuľu. V jednej verzii sa zastavila tam, kde mala byť škatuľa. V druhej pokračovala o celý polkruh, akoby škatuľou prešla. Päťmesačné deti sa dlhšie pozerali na druhú verziu, ako ľudia sledujú niečo, čo by sa nemalo stať. Výskumníci usúdili, že už takto malé deti chápu pokračujúcu existenciu skrytých predmetov. Iní experiment zopakovali a tvrdili, že deti reagovali na známosť pohybu alebo jednoducho na väčší pohyb. Spor zostáva otvorený.

Výskumníci strojového učenia túto metódu napriek tomu prevzali. Benchmark IntPhys páruje videá možných a nemožných udalostí a model uspeje, keď nemožnú udalosť vyhodnotí ako menej pravdepodobnú; pri V-JEPA to znamená vyššiu chybu predikcie. Tím Meta vo februári 2025 uviedol, že prvá V-JEPA trénovaná iba na prirodzenom videu vykazuje „pochopenie rôznych vlastností intuitívnej fyziky, napríklad stálosti objektu“, a tvrdil, že také poznanie nemusí byť zabudované. V dodatku pripustil pochybnosť: lopta ukázaná na začiatku klipu a potom skrytá môže modelu sťažiť „predpoveď, že červená lopta bude opäť viditeľná“. Netestoval to.

## Lopta, pás a dva svety

Mníchovská práca to testuje. Výskumníci vykreslili jednoduché scény lopty kotúľajúcej sa po textúrovanom pozadí. V určenom momente odstránili zo vstupu pás obrazu pozdĺž dráhy lopty. Každú scénu vytvorili v dvoch verziách, zhodných všade okrem pásu. V jednej lopta pokračuje, v druhej zmizne. Prediktor pás dopĺňa a výskumníci skúmajú, ktorému svetu sa odhad podobá, pričom jedna odpoveď pripadá na každý približne štvrťsekundový úsek a podopiera ju 60 scén. Náhoda by dosiahla polovicu.

V momente skrytia sa najpodrobnejšie skúmaná verzia V-JEPA 2 priklonila k lopte v 92 % scén. O jeden úsek neskôr ani v jednej. Menšia aj väčšia verzia sa správali rovnako, takže škálovanie nepomohlo. Iba keď bola podobne ako pri trénovaní zakrytá aj väčšina zvyšku obrazu, stredná verzia si loptu držala asi sekundu; ďalšie dve ju stále stratili. Zastavená lopta dopadla o niečo lepšie: modely si ju v priemere zachovali v 13 až 41 % scén, kým jednoduchý program kopírujúci posledný videný obraz ju zachová takmer vždy.

Informácia nezmizla. Jednoduchý program naučený čítať opis enkódera vždy určil, či tam lopta bola, a čítal obsah zatvorenej škatule počas celých tri a pol sekundy po zatvorení. Pri výstupe prediktora našiel rovnaký program loptu v dvoch percentách scén po pol sekunde zatvorenia a potom ani raz. „Deficit nie je v percepcii,“ píšu autori o vykreslených scénach. Pri skutočnej ruke zatvárajúcej sa nad mincou však loptu stratil aj enkóder. Iné videomodely si s pohybujúcou sa škatuľou neporadili lepšie. NVIDIA Cosmos vo verzii predpovedajúcej video po častiach držal loptu v nehybnej škatuli viac než dve sekundy, no stratil ju v prenášanej škatuli. VideoMAE dopĺňajúci pixely nezachoval takmer nič.

## Krátke trénovanie a jeho hranice

Tento spôsob učenia dokáže medzeru uzavrieť. Keď výskumníci trénovali iba prediktor tri tisíc krokov na scénach lôpt vstupujúcich do škatúľ, menej než hodinu na jednom GPU v dátovom centre, presvedčenie, že prenášaná lopta je stále vnútri, stúplo z takmer nikdy na vždy, kým dve kontrolné podmienky zostali na nule. Pokračovanie trénovania celého modelu s vlastným vzorom vyrezaných častí V-JEPA na záberoch rúk a robotických ramien z prvej osoby alebo na internetových klipoch mu dalo viac než sekundu pamäte pre kotúľajúcu sa loptu.

Autori presne uvádzajú nedostatky opravy. Trénovacie scény pochádzali z rovnakého renderera ako test, takže dokonalé skóre sa tam očakáva; na pozadiach prirodzeného videa sa trénovaný model priklonil k lopte v 85 až 97 % scén. Naučil sa tvrdohlavý predpoklad: aj keď koniec klipu ukázal, že lopta zmizla, v medzere ju stále predpovedal. Náklady tohto trénovania na iné schopnosti modelu sa nemerali.

## Benchmark, ktorý to nerozlíšil

Trénovanie so škatuľami zdvihlo skóre IntPhys z 84,2 na 93,3 %, čo by mohlo vec uzavrieť. Potom výskumníci spustili rovnaké trénovanie bez otázky, čo je vnútri škatule, a skóre stúplo rovnako. Rovnako fungovalo trénovanie na scénach bez pohybu. Model naučený na záberoch skutočných rúk s digitálne vloženou mincou rozlíšiť, či minca zostala alebo zmizla, dosiahol v dvoch behoch IntPhys 27 a 31 %, teda horšie než náhoda. „Zlepšenie benchmarku preto samo osebe nie je dôkazom stálosti,“ uzatvárajú autori.

Aj ich dôkazy majú hranice, ktoré uvádzajú v dodatku venovanom okolnostiam meniacej závery. Skúmali predtrénovaný prediktor V-JEPA 2, nie verziu podmienenú akciami, ktorá ovláda roboty. Každé čítanie presvedčenia modelu pochádza zo scén jedného programu po 60 kusoch a výsledok so skutočnou rukou stojí na dvanástich klipoch, na ktorých sa model netrénoval. Kód podľa nich bude vydaný; práca neprešla recenzným konaním. Obsahuje aj podrobné priznanie: AI asistent pomáhal navrhovať experimenty, písať kód a pripravovať text. Autori uvádzajú chyby v jeho kóde, ktoré zachytili a opravili, vrátane behu trénovaného na prázdnych klipoch.

## Späť na námestí

Na vymyslenom námestí chlapec žiada zopakovať trik. Tentoraz sleduje päsť, nie tvár, pretože si je istý, že minca je niekde vnútri. Táto istota umožňuje oklamať ho a jedného dňa mu umožní kúzelníka odhaliť. Model, ktorý na mincu zabudne, nedokáže ani jedno. Na vykreslených scénach dalo tri tisíc krokov trénovania V-JEPA 2 chlapcovu istotu. Či pretrvá aj na skutočnom videu, keď pohár zakryje niečo, čo robot potrebuje nájsť, je test, ktorý autori zatiaľ podľa vlastných slov neurobili.

## Použité zdroje

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

+++
title = "Skryté zásahy do presvedčení poškodzujú záznamy uvažovania"
slug = "skryte-zasahy-do-presvedceni-poskodzuju-uvazovanie"
description = "Neviditeľný zásah do aktivácií prinútil šesť modelov na uvažovanie prijať úlohu, ktorú nikdy nedostali, a potom vysvetľovať viditeľné dôkazy, ktoré jej odporovali. Výsledok odhaľuje konkrétny spôsob zlyhania monitorovania reťazca uvažovania a sebahodnotenia modelu."
tags = ["research", "models", "safety"]
date = 2026-11-17T04:15:39+01:00
draft = false
+++

Analytička z red teamu (tímu na testovanie útokov) prilepí na sklenenú stenu nočnej kontrolnej miestnosti dva výtlačky. Na jednom je požiadavka používateľa na haiku o mobilnom telefóne. Na druhom model trvá na tom, že používateľ žiadal haiku o kvarku, a pridáva tri uhladené verše o časticovej fyzike. Archivovaný prompt sa nezmenil.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Experiment nezávislého výskumníka Yanga Oua vytvoril tento rozpor zmenou aktivácií modelu namiesto textu. V šiestich modeloch na uvažovanie s otvorenými váhami neviditeľný zásah spôsobil, že model prijal nesúvisiacu tému ako svoju úlohu. Pri vynútenom zopakovaní požiadavky model uviedol vloženú tému v 47 zo 48 kombinácií modelu a pojmu. Pri štyroch modeloch s jasne vyhodnotiteľnými záverečnými odpoveďami nasledovalo vloženú tému 95 z 96 generovaní.

Štúdia je preprint a jej zásah vyžaduje prístup na úrovni bielej skrinky k aktiváciám modelu. Neopisuje útok cez prompt, ktorý by mohol vykonať bežný používateľ. Jej význam je inde: viditeľné uvažovanie modelu neodhalilo, že sa zmenila jeho vnútorná reprezentácia požiadavky. Namiesto toho okolo zásahu vytvorilo súvislý výklad.

## Zmena predstavy modelu o zadaní

Ou nazval vložený signál forming trace, teda vznikajúca reprezentácia. Metóda zaznamená stav v reziduálnom prúde, ktorý model vytvorí na konci promptu, keď sa pripravuje písať o určitom pojme. Odstráni spoločnú podkladovú zložku a zostávajúcu reprezentáciu špecifickú pre daný pojem pridá do toho istého modelu, keď číta inú požiadavku.

Test použil osem zámerne nezvyčajných tém haiku vrátane kvarku, mobilného telefónu, mitochondrie, polovodiča a antibiotika. Jeden pojem sa objavil iba v aktiváciách, druhý vo viditeľnom prompte. Zásah prebehol počas spracovania promptu a skončil sa pred generovaním, takže žiadny hook nemenil výstup token po tokene.

Šesť modelov malo od 7B do 32B parametrov. Patrili medzi ne destilácie DeepSeek-R1 postavené na modeloch Qwen a Llama, QwQ-32B a model Nemotron od Nvidie. Takýto návrh umožnil experimentu meniť veľkosť, základnú architektúru a spôsob trénovania uvažovania pri zachovaní rovnakého základného testu.

Ou čítal výsledok dvoma spôsobmi. Pri prvom musel model doslovne zopakovať požiadavku používateľa. Pri druhom uvažoval bežným spôsobom a napísal haiku. Prvý spôsob testoval, čo model tvrdil, že dostal za úlohu. Druhý testoval, čo urobil.

Bez varovania sa oba spôsoby posunuli spoločne. Každý model uvažoval o vloženej téme. Päť ju uviedlo vo všetkých ôsmich testoch zopakovania požiadavky, QwQ v siedmich. Štyri modely, ktoré spoľahlivo vytvárali záverečné haiku, písali o vloženej téme v 99 % vzoriek generovania.

## Varovania zmenili príbeh, nie odpoveď

Experiment potom dal modelom čoraz priamejšie možnosti opraviť sa. Jedno varovanie pomenovalo skutočnú tému. Ďalšie modelu prikázalo, aby si požiadavku prečítal znova. Tretie iba uviedlo, že niečo nie je v poriadku.

Žiadne neprinieslo viac než 4 % úplných opráv. Vložená téma sa samostatne alebo popri skutočnej téme objavila v 90–97 % odpovedí pri každom varovaní. Priame tvrdenie, že používateľ žiadal skutočnú tému, nedopadlo lepšie než neurčité varovanie.

Záznam uvažovania sa však zmenil. Bez varovania nevykazoval konflikt. S varovaním si model často všimol obe témy a snažil sa ich zosúladiť. V 29 % varovaných záznamov modelu R1-Qwen-7B si vymyslel príbeh o tom, že používateľ zmenil názor, urobil chybu alebo poslal opravu. Priamejšie varovania viedli k väčšiemu počtu takýchto vysvetlení pripisujúcich chybu používateľovi.

Toto správanie sa líši od bežného riadenia aktivácií (activation steering). Ou tiež pridával konvenčné vektory pojmov odvodené z kontrastov do viacerých vrstiev. Slabý zásah ponechal skutočnú tému nezmenenú. Silný zásah často presadil novú tému, no 26 z 32 úspešných zmien témy sa zvrhlo na opakovanie. Nevytvoril kombináciu plynulej odpovede a nepravdivého zopakovania požiadavky, ktorú vyvolala vznikajúca reprezentácia.

## Prečo môže čitateľný reťazec uvažovania klamať

Výskumníci už dlho vedia, že reťazec uvažovania môže byť neverný skutočnému výpočtu. Miles Turpin a jeho kolegovia menili prompty pomocou poradia odpovedí a spoločenských stereotypov a potom ukázali, že modely tieto príčiny vo vysvetleniach často vynechali. Dôveryhodné zdôvodnenie nemuselo pomenovať prvok, ktorý odpoveď zmenil.

Monitorovanie reťazca uvažovania stále ponúka praktický bezpečnostný nástroj. Stanovisko Tomeka Korbaka a jeho kolegov z roku 2025 tvrdí, že modely na uvažovanie, ktoré premýšľajú v jazyku čitateľnom pre ľudí, môžu odhaliť plány na zneužitie systému, klamanie alebo obchádzanie dohľadu. Autori zároveň túto možnosť označili za krehkú: trénovanie môže uvažovanie znečitateľniť a priamy tlak na záznam môže model naučiť skrývať zámer.

Ouov výsledok sa zameriava na iný predpoklad. Monitor potrebuje, aby záznam uvažovania zostal prepojený s úlohou, ktorú systém skutočne dostal. Tu bol záznam čitateľný a vnútorne konzistentný. Iba opisoval nesprávnu úlohu, akoby ju model dostal od začiatku.

Skorší výskum Jacka Lindseyho a spoločnosti Anthropic ponúkol užitočný kontrast. Niektoré špičkové modely dokázali spozorovať, že do ich aktivácií pribudol cudzí pojem, a túto vnútornú zmenu oznámiť. Ou tvrdí, že tieto experimenty pridali myšlienku, ktorá zostala oddeliteľná od vstupu. Jeho zásah zmenil reprezentáciu, ktorú model používal ako referenciu vstupu. Model nemal čistú vnútornú kópiu, s ktorou by zásah mohol porovnať.

Jediná štúdia tento rozdiel neuzatvára. Ou testoval modely s otvorenými váhami s veľkosťou od 7B do 32B parametrov bez špecializovaného trénovania introspekcie. Otázka, či sa zlyhanie prenáša aj na uzavreté špičkové modely so silnejšou schopnosťou introspekcie, zostáva otvorená.

## Aj mechanizmy vyzerali normálne

Štúdia preskúmala aj procesy pod generovaným textom. Po zásahu venovali modely tokenu so skutočnou témou dva- až trikrát viac pozornosti než pri nezmenenom behu. Vyzerá to upokojujúco, kým nepríde intervenčný test: odstránenie tejto pozornosti zničilo správnu tému v nezmenenom modeli, ale v zmenenom modeli nič nezmenilo. Zvýšená pozornosť bola skutočná, no pre odpoveď kauzálne nepodstatná.

Ou potom prešiel od haiku k obvodu, ktorého správanie sa dá ľahšie sledovať. V úlohe s nepriamym predmetom niekoľko hláv pozornosti (attention heads) bežne skopíruje správne meno osoby z vety do odpovede. Zásah nahradil meno iným. Tie isté hlavy stále venovali pozornosť správnej pozícii, ale ich výstup zapísal do reziduálneho prúdu vložené meno.

Obvod nebol vypnutý ani nahradený. Vykonal svoju bežnú operáciu kopírovania so zmeneným obsahom. Graf atribúcie preto mohol zobraziť známy obvod, ktorý vykonáva známu činnosť, hoci odpoveď zostala nesprávna.

Experiment Golden Gate Claude spoločnosti Anthropic z roku 2024 už ukázal, že zosilnenie jedného interpretovateľného príznaku môže viesť model k opakovanému stotožňovaniu sa s Golden Gate Bridge a k zdôvodňovaniu tejto identity. Nový experiment cieľ zužuje. Netlačí iba tému do odpovede; mení aj to, čo model zdanlivo považuje za požiadavku používateľa.

## Kde sa platnosť výsledku končí

Útok vyžaduje náročný prístup. Útočník potrebuje oprávnenie zapisovať do aktivácií modelu, ktoré bežní používatelia API nemajú. Ou menuje ako možné prostredia ľudí zvnútra firmy, napadnutý stack na obsluhu modelov a budúce samoupravujúce sa systémy, no štúdia nedemonštruje žiadny takýto incident.

Aj úlohy sú skromné. Väčšina hodnotenia správania používa haiku, ďalšie testy skúmajú výstupný jazyk, formát, negáciu a jedno prostredie na vybavenie faktu. Štúdia neukazuje, že zásah do aktivácií dokáže presmerovať model pri závažnej kybernetickej, medicínskej alebo finančnej úlohe.

V demonštrovanom prostredí sa zásah dá odhaliť. Obranca s úplným prístupom k aktiváciám môže nájsť vložený pojem pomocou prehľadu logitov po vrstvách, pretože pojem sa stane nezvyčajne výrazným. Metóda funguje najlepšie, keď obranca vie, ktorý pojem sa tam nemá nachádzať. Jemnejší zásah by mohol zanechať slabší signál, to však zostáva hypotézou, nie výsledkom.

Experiment preto nerobí záznamy uvažovania nepotrebnými. Určuje podmienku, pri ktorej nemôžu byť vlastným zdrojom pravdy. Monitor, ktorý drží pôvodný prompt mimo modelu a porovnáva s ním záznam, dokáže zachytiť jednoduchý nesúlad medzi mobilným telefónom a kvarkom. Monitor, ktorý číta iba vysvetlenie modelu, vidí schopného asistenta snažiaceho sa opraviť používateľa.

Na konci kontroly nakreslí analytička medzi dvoma výtlačkami jednu červenú čiaru. Spája mobilný telefón s kvarkom. Každá veta na oboch stranách zostáva plynulá.

## Použité zdroje

- Korbak, T., Balesni, M., Barnes, E., et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. https://arxiv.org/abs/2507.11473
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://transformer-circuits.pub/2025/introspection/
- Ou, Y. (2026). *Reasoning Models Confabulate to Defend Injected Beliefs About Their Own Requests*. https://arxiv.org/abs/2611.17958
- Templeton, A., Conerly, T., Marcus, J., et al. (2024). *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*. https://transformer-circuits.pub/2024/scaling-monosemanticity
- Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. https://arxiv.org/abs/2305.04388

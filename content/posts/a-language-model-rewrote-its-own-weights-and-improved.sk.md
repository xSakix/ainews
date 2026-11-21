+++
title = "Jazykový model prepísal vlastné váhy a zlepšil sa"
slug = "jazykovy-model-prepisal-vlastne-vahy-a-zlepsil-sa"
description = "Výskumníci umožnili otvorenému modelu s 27 miliardami parametrov skúmať a upravovať vlastné váhy bez gradientov a optimalizátorov. Model zvýšil presnosť na úlohách nepoužitých pri trénovaní o 6,6 bodu a opravil svoju poškodenú kópiu; menšie modely v rovnakých podmienkach zlyhali."
tags = ["models", "research"]
date = 2026-11-21T04:12:00+01:00
draft = false
+++

Model mal pred sebou reláciu Pythonu, v ktorej videl vlastné váhy. Mohol skúmať skryté stavy, meniť vybrané matice a požiadať svoju kópiu, aby vyriešila ďalšiu úlohu. Nesmelo sa pri tom počítať s gradientmi. K dispozícii mal iba dvadsať dopredných priechodov modelom a pevne určený čas.

*Úvodná a záverečná scéna tohto článku sú ilustračné; osoby v nich sú vymyslené.*

Jiajun Fan a desať spoluautorov pripravili takéto prostredie pre štyri otvorené modely z jednej rodiny. Model s 2 miliardami parametrov sa nepokúsil o úpravu. Modely so 4 a 9 miliardami parametrov skúšali náhodné zásahy a zhoršili vlastný výkon. Model s 27 miliardami parametrov meral rozdiely vo svojich skrytých stavoch, upravoval váhy v príslušných smeroch a zmeny ponechal iba vtedy, keď ich podporili párové testy. Jedna úprava zvýšila presnosť na 490 úlohách nepoužitých pri trénovaní (held-out) o 6,6 percentuálneho bodu.

Štúdia tento postup nazýva samoprepisovaním. Jej hlavné tvrdenie je presne ohraničené, ale významné: už nasadený model môže trvalo zlepšiť vlastné váhy iba prostredníctvom uvažovania pri doprednom priechode. Ide o preprint a autori uvádzajú, že je to prvá ukážka tohto druhu.

## Model získal prístup k vlastným váham

Pri bežnom trénovaní je systém, ktorý hľadá lepšie váhy, oddelený od modelu, ktorý ich neskôr používa. Optimalizátor vypočítava gradienty stratovej funkcie, inžinieri vyberajú dáta a nastavenia a výpočtový klaster zapíše výsledok do nového checkpointu. Inferencia sa začína až po skončení tohto procesu.

Fan a jeho kolegovia odstránili optimalizátor, ale modelu poskytli nástroje. Model dostal ohodnotené odpovede na cvičných úlohách, prístup k tenzorom svojich váh a reláciu Pythonu, ktorá si medzi jednotlivými krokmi zachovávala stav. Na rovnakých úlohách a s rovnakými náhodnými seedmi mohol spustiť pôvodný aj upravený model. Mohol tiež čítať skryté stavy vytvorené pri spracovaní ľubovoľných textov, ktoré si vybral.

Obmedzenia vynucovalo samotné prostredie. Gradienty boli vypnuté. Volania optimalizátorov, sietí, nových procesov a funkcií na načítanie modelu boli zakázané. Model nemohol meniť vstupné embeddingy, záverečnú normalizáciu ani výstupnú vrstvu. Počas jednej relácie mal najviac 20 dopredných priechodov a 200 vykonaní kódu.

Párový test porovnával odpovede úlohu po úlohe. Bolo to dôležité, pretože malý súhrnný prínos môže byť iba dôsledkom náhodného vzorkovania. Framework zaznamenal, koľko odpovedí sa zmenilo z nesprávnych na správne, koľko opačným smerom a ako často jedna či druhá verzia vyčerpala limit 16 384 tokenov.

V prísnejšom protokole framework ešte raz otestoval navrhnutú úpravu na vyhradených cvičných úlohách, ktoré model nemohol skúmať. Potom model zmenu odovzdal alebo stiahol. V piatich z prvých ôsmich relácií ju stiahol. Prijaté úpravy nikdy neznížili presnosť práve používanej verzie modelu.

## Čo zmenil najväčší model

Model s 27 miliardami parametrov neprehľadával všetky parametre. V skrytých stavoch našiel smery súvisiace so zlyhaniami a oslabil spôsob, akým vybrané výstupné matice zapisovali informácie pozdĺž týchto smerov. Operácia sa podobala odčítaniu zložky matice s hodnosťou jedna.

Zásah obmedzil viditeľné zlyhanie: niektoré odpovede opakovali jednu vetu až do vyčerpania limitu tokenov. V jednom príklade nepoužitom pri trénovaní základný model zopakoval tú istú vetu 549-krát a neodpovedal. Upravená verzia úlohu dokončila.

V pevne určenom hodnotení priniesla najúspešnejšia úprava zlepšenie o 6,6 bodu. Pri dvoch reláciách v sérii vyšli podľa testu autorov pravdepodobnosti pozorovaného zlepšenia pri nulovom účinku nižšie než jedna ku 100 000. Po ôsmej relácii dosiahla presnosť 63,8 %.

Každá relácia začínala skúmanie od základných váh, ale prijatá úprava nahradila model, ktorý sa ďalej používal. Séria tak zhromažďovala overené rozhodnutia a neskladala bez výberu všetky navrhnuté zásahy. Autori uvádzajú, že presnosť počas všetkých ôsmich relácií rástla alebo zostávala nezmenená.

Zlepšenie nevyžadovalo pri každej ďalšej odpovedi viac výpočtov. Po zapísaní zmena zostala v checkpointe. Tým sa líšila od test-time scaling, pri ktorom model dosahuje lepšie odpovede tým, že pri každej úlohe spotrebuje viac tokenov alebo vygeneruje viac vzoriek.

## Oprava bez pôvodných hodnôt

Tím tiež pripravil poškodenie so známou príčinou. Osem po sebe nasledujúcich riadkov jednej výstupnej matice viacvrstvového perceptrónu prepísal šumom zosilneným na 200-násobok štandardnej odchýlky matice. Poškodený model už takmer nič nevyriešil.

Model, ktorý mal opravu vykonať, nebol poškodený, ale mohol skúmať iba behy a váhy poškodenej kópie. Dostal informáciu, že niektoré hodnoty sú nesprávne, no nevedel, kde sa poškodenie nachádza ani ako vzniklo. Zodpovedajúce nepoškodené hodnoty nikdy nevidel.

Model s 27 miliardami parametrov našiel chybnú maticu a zapísal vlastné náhradné hodnoty. Oprava, ktorú vytvoril na textových matematických úlohách, fungovala aj pri šiestich obrazových benchmarkoch, ktoré počas relácie nevidel. Opravená kópia získala späť 83 % súhrnnej presnosti základného modelu. V ScreenSpot-v2 sa zlepšila z nuly na 89 % oproti 93 % pri nepoškodenom modeli.

Tento test oslabuje jedno jednoduché vysvetlenie hlavného výsledku. Model by mohol vytvoriť úzko zameranú úpravu, ktorá využíva zvláštnosti cvičných úloh. Oprava zámerne poškodenej zložky a obnovenie výkonu na obrázkoch ukazujú, že model dokáže identifikovať a čiastočne obnoviť aj všeobecnejšiu funkciu.

Test však nedokazuje, že model dokáže opraviť ľubovoľné poškodenie. Zásah sa týkal jedného umelo vytvoreného bloku a experimenty použili jedinú rodinu modelov Qwen3.5 v štyroch veľkostiach. Model dostával ohodnotené cvičné odpovede a mal nezvyčajne priamy prístup k vnútorným tenzorom. Bežne hostovaní asistenti takéto oprávnenia nemajú.

## Hranica daná veľkosťou modelu

Menšie modely ukázali súčasné obmedzenia. Model s 2 miliardami parametrov nepovažoval vlastné váhy za niečo, čo dokáže užitočne zmeniť. Verzie so 4 a 9 miliardami parametrov pridávali náhodný šum. Keď test ukázal zhoršenie, iba hádali, aký iný zásah skúsiť.

Model s 27 miliardami parametrov zvládol dlhší postup: diagnostikoval príznak, preskúmal aktivácie, vytvoril hypotézu, zmenil maticu, vykonal párový test a po negatívnom výsledku upravil plán. Autori to opisujú ako schopnosť, ktorá vzniká s rastúcou veľkosťou modelu. Zo štyroch veľkostí jednej rodiny však nemožno určiť všeobecnú hranicu.

Sprievodný preprint zverejnený v tom istom týždni skúmal iné usporiadanie: externý jazykový model vyberal úpravy váh pre menšie cieľové modely. Tento systém sa pri SmolLM2 a Qwen2.5 vyrovnal vyhľadávaniu v režime black box a pri Pythii ho prekonal. Fanova štúdia spája model, ktorý upravuje, s modelom, ktorý sa upravuje, do jedného systému. Práve to umožňuje jej silnejšie tvrdenie.

Autori spájajú výsledok s rekurzívnym sebazlepšovaním. Ich experiment je však stále ďaleko od autonómneho cyklu. Ľudia určili úlohu, signál zlyhania, nástroje, obmedzenia úprav aj test prijatia. Relácie na jednom GPU trvali hodiny a najsilnejšie dôkazy sa týkajú ohraničenej sady úloh uvažovania a jednej umelej poruchy.

Práve tieto hranice zároveň umožňujú výsledok preskúmať. Každá prijatá zmena prešla párovým porovnaním, všetky úlohy nepoužité pri trénovaní zostali mimo upravovacej relácie a zlyhania menších modelov zostali v zázname.

Pri prompte Pythonu model využil posledný dopredný priechod a ponechal úpravu na disku. Ďalšia odpoveď nepotrebovala dlhší prompt ani ďalšiu vzorku. Rozdiel nieslo niekoľko upravených matíc.

## Použité zdroje

- Fan, J., He, N., Yang, C., Mao, A., Zhu, X., Cheng, C., Liang, K., Shen, S., Li, Z., Guo, R., & Liu, G. (2026). *Language Models Can Rewrite Their Own Weights*. https://arxiv.org/abs/2611.21885
- Yang, C., et al. (2026). *Can an LLM Fix a Language Model Without Training It?* https://arxiv.org/abs/2611.25613

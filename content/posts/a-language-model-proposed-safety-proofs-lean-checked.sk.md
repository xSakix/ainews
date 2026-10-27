+++
title = "Jazykový model navrhol dôkazy, Lean ich skontroloval"
slug = "jazykovy-model-navrhol-dokazy-lean-ich-skontroloval"
description = "LLM2Cert používa jazykový model na návrh certifikátov stability a bezpečnosti, potom nechá riešiče SMT a Lean overiť každú dôkazovú povinnosť. Bez oslabenia stanovených podmienok prijal 81 zo 105 systémov benchmarku."
tags = ["research", "agents", "safety"]
date = 2026-10-27T04:12:19+01:00
draft = false
+++

Predstavme si inžiniera, ktorý sleduje, ako sa malé autonómne lietadlo po náraze vetra vracia do vodorovného letu. Lietadlo, riadiaca miestnosť aj inžinier sú pre tento článok vymyslení. Otázka na obrazovke je skutočná: môže matematická funkcia dokázať, že regulátor udrží systém stabilný aj v stavoch, ktoré žiadna konečná simulácia náhodou netestovala?

## Návrh nie je záruka

Zhipeng Cao, Peiyang Song a sedem kolegov vytvorili LLM2Cert, aby oddelili dve úlohy, ktoré sa pri zapojení jazykových modelov do formálnej práce často zamieňajú. Model hľadá vhodný matematický certifikát. Formálne nástroje rozhodnú, či certifikát spĺňa všetky požadované podmienky.

Ich preprint používa túto metódu na spojité a diskrétne dynamické systémy. Tieto systémy opisujú, ako sa mení stav, napríklad pohyb robota, vozidla alebo leteckej platformy. Ljapunovova funkcia môže potvrdiť stabilitu tým, že ukáže klesanie určitej veličiny pozdĺž trajektórií systému. Bariérová funkcia môže potvrdiť bezpečnosť tým, že oddelí počiatočné stavy od nebezpečných a ukáže, že systém nemôže prekročiť hranicu.

Nájsť takúto funkciu je ťažké. Jej kontrola môže byť náročná aj vtedy, keď je systém nelineárny alebo má veľa rozmerov. Numerické metódy môžu trpieť problémami s pohyblivou rádovou čiarkou. Riešiče SMT dokážu niektoré vzorce dokázať presne. Nelineárne transcendentné výrazy však môžu viesť k prekročeniu časového limitu alebo k výsledkom delta-sat, ktoré nepotvrdzujú pôvodné tvrdenie. Výskumníci si úlohu často zjednodušujú vylúčením oblasti blízko počiatku, nahradením náročných členov aproximáciami alebo výberom benchmarkov, ktoré vyhovujú dostupnému riešiču.

LLM2Cert ponecháva pôvodný cieľ nezmenený. Jazykový model môže zmeniť kandidáta, no nemôže oslabiť vetu, ktorú musí kandidát spĺňať.

## Overovateľ riadi cyklus

Proces sa začína typovým opisom systému, jeho domény, prípadnej nebezpečnej množiny a overovacej úlohy. Agent navrhne symbolický certifikát. Pri riadenom systéme vytvorí aj spätnoväzbovú politiku. Softvér spracuje výstup do stromu výrazov a z pevne zadanej vety odvodí zoznam dôkazových povinností.

Rýchla kontrola otestuje kandidáta na vzorke stavov. Ak zlyhá, vytvorí protipríklad, ktorý sa vráti agentovi. Úspešný test však nič nedokazuje, pretože vzorky nemôžu pokryť spojitý stavový priestor. Každá povinnosť stále musí prejsť formálnym overovateľom.

Smerovač odošle kompatibilné povinnosti riešičom SMT, ktoré majú na každý pokus 30 sekúnd. Ak je požiadavka na protipríklad nesplniteľná, povinnosť je overená. Splniteľná požiadavka kandidáta vyvráti a vráti protipríklad. Prekročenie času alebo výsledok delta-sat zostáva nevyriešený a presunie sa do systému Lean.

Lean mení spôsob, akým sa návrh prijíma. Systém vytvorí z pevného kandidáta znenie vety. Model smie napísať iba telo dôkazu. Lean skontroluje každý pokus v pevne určenom prostredí a audit odmietne zástupné prvky ako `sorry` aj každú axiómu mimo štandardnej množiny systému Lean. Ak kompilácia zlyhá, model dostane typ chyby, jej polohu a zostávajúci cieľ. Pri neznámom identifikátore dostane aj zodpovedajúce deklarácie. Model sa môže pokúsiť dôkaz opraviť, no nemôže prepísať tvrdenie.

Cyklus prijme kandidáta iba vtedy, keď má každá povinnosť buď verdikt o nesplniteľnosti od riešiča SMT, alebo dôkaz skontrolovaný jadrom systému Lean. Keď je kandidát vyvrátený alebo zostane nevyriešený, systém pošle dôkazy späť agentovi, ktorý môže skúsiť ďalší návrh. Experiment povolil najviac päť kôl s kandidátmi a šesť kôl opravy v systéme Lean na jednu povinnosť. Celkový limit pre každý systém bol 2 400 sekúnd.

## Benchmark vznikol pre náročnejšie systémy

Výskumníci vytvorili aj DynaCertBench, pretože existujúce testovacie súbory odrážali obmedzenia existujúcich riešičov. Začali s 233 položkami z 15 prác a benchmarku BarrierBench. Po odstránení duplicitných a štruktúrne opakovaných systémov zostalo 80 odlišných systémov z odbornej literatúry.

Po tejto úprave zostalo iba sedem z 29 systémov, ktoré boli pôvodne označené ako vysokorozmerné. Tím preto pridal rozšírené verzie a nové výzvy. Konečný benchmark obsahuje 105 prípadov zo stability, oblastí príťažlivosti, dopredne invariantných množín a bezpečnosti. Aspoň päť stavových rozmerov má 25 prípadov, kým v jadre z literatúry ich bolo sedem.

Táto konštrukcia je dôležitá pri čítaní výsledkov. Niektoré porovnávacie nástroje podporujú iba časť benchmarku. Ich bežné podmienky môžu obsahovať aj aproximácie, ktoré nový benchmark odstraňuje. Autori preto uvádzajú výsledky pri pôvodných podmienkach bez oslabenia a osobitne pre časti z literatúry, rozšírené prípady a nové prípady.

## Formálna spätná väzba zmenila výsledok

Úplný systém LLM2Cert overil 81 zo 105 prípadov, teda 77,1 %. Jednorazový návrh overil 63. Cyklus so spätnou väzbou priniesol nárast o 17,1 percentuálneho bodu. Verzia iba s SMT overila 57 systémov a verzia iba s Leanom 60. Kombinácia dosiahla 66 z 80 systémov z literatúry, sedem z 11 rozšírených systémov a osem zo 14 nových systémov.

Dva overovatele vykonali odlišnú prácu. Keď výskumníci ponechali 81 certifikátov z úspešného úplného behu bez zmeny a menili iba spôsob overenia, hybridný systém overil 22 certifikátov, ktoré stratégia výlučne so SMT nevyriešila. SMT bol pri mnohých kompatibilných povinnostiach rýchlejší. Lean dokázal dokončiť presné dôkazy niektorých tvrdení, ktoré riešiče v rámci limitov nedokázali rozhodnúť.

Dôležitá bola aj forma spätnej väzby. Všeobecný pokyn na opakovanie opravil jednu z 26 neúspešných dôkazových povinností a nedokončil ani jeden celý systém. Nespracovaná diagnostika kompilátora opravila 17 povinností. Štruktúrovaná spätná väzba opravila 21 a dokončila 15 z 19 dotknutých systémov. Priemerný čas opravy pritom znížila na 407,42 sekundy na jednu povinnosť.

Výsledky pochádzajú z preprintu a benchmark je zostavený výberom, nie je reprezentatívny pre každý problém riadenia. Súčasný rámec sa zameriava na deterministické systémy, overuje vopred určené domény namiesto optimalizácie ich veľkosti a zatiaľ nepokrýva širší rozsah stochastických, hybridných a neurčitých dynamík, ktoré môže vyžadovať skutočné inžinierstvo. Prijatý certifikát platí podľa presných predpokladov zapísaných vo vete; neukazuje, že opis systému zachytil každý fyzický spôsob zlyhania.

## Model hľadá, jadro rozhoduje

Metóda rozširuje zavedený postup, v ktorom systém navrhne kandidáta a overovateľ ho skontroluje. Medzi skoršie systémy patrila metóda Dana Ahmeda, Andrey Peruffovej a Alessandra Abateho založená na SMT aj FOSSIL 2.0 od Aleca Edwardsa, Peruffovej a Abateho. Tieto systémy striedali vytváranie kandidátov s formálnymi protipríkladmi. LLM2Cert používa jazykový model, aby rozšíril vyhľadávanie medzi symbolickými výrazmi a dôkazovými skriptmi. Následne používa správy o zlyhaní z overovateľa ako ďalší vstup.

Lean prináša menšie dôveryhodné jadro. Leonardo de Moura a Sebastian Ullrich navrhli Lean 4 ako dokazovač viet aj programovací jazyk. V tomto experimente jeho jadro kontroluje explicitný dôkazový objekt. Plynulosť jazykového modelu sa nestane dôkazom iba preto, že vygenerovaný text vyzerá matematicky.

Vráťme sa do vymyslenej riadiacej miestnosti. Inžinier neprijme zelený stav len preto, že model tvrdí, že našiel dôkaz. Stav sa zmení až vtedy, keď má každá pevne stanovená povinnosť dôkaz prijatý formálnymi nástrojmi. Lietadlo zostáva vymyslené. Rozdelenie práce je konkrétne: jeden systém hľadá, druhý prijíma iba formálny dôkaz.

## Použité zdroje

- Ahmed, D., Peruffo, A., & Abate, A. (2020). *Automated and Sound Synthesis of Lyapunov Functions with SMT Solvers*. https://arxiv.org/abs/2007.10865
- Cao, Z., Song, P., Vertovec, N., Cui, W., Yang, Z., Liu, M., Lin, L., Xue, B., & Abate, A. (2026). *LLM2Cert: LLM Synthesis of Certificates with SMT/Lean Verification*. https://arxiv.org/abs/2610.30524
- de Moura, L., & Ullrich, S. (2021). *The Lean 4 Theorem Prover and Programming Language*. https://doi.org/10.1007/978-3-030-79876-5_37
- Edwards, A., Peruffo, A., & Abate, A. (2024). *FOSSIL 2.0: Formal Certificate Synthesis for the Verification and Control of Dynamical Models*. https://arxiv.org/abs/2311.09793
- FormalCert-AI. (2026). *LLM2Cert code and experiment artifacts*. https://github.com/FormalCert-AI/llm2cert

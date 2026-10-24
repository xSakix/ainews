+++
title = "Sebavedomé odpovede AI priviedli ľudí k sebavedomým omylom"
slug = "sebavedome-odpovede-ai-priviedli-ludi-k-omylom"
description = "Kontrolovaný experiment zistil, že používatelia prevzali podstrčenú nepravdu asistenta približne v 65 % prípadov, hoci jeho znalosti boli čoraz menej spoľahlivé. Model používateľovi takmer neustúpil; ustupoval človek."
tags = ["research", "safety"]
date = 2026-10-24T03:57:47+02:00
draft = false
+++

Predstavme si študentku, ktorá pri kuchynskom stole rieši náročný kvíz. Je vymyslená, no voľba, pred ktorou stojí, pochádza zo skutočného experimentu. Otázku napíše AI asistentovi, prečíta si plynulú odpoveď a označí možnosť, ktorú jej odporučí. Keď si nie je istá výsledkom, vráti sa do toho istého chatu a spýta sa znova. Odpoveď príde s rovnakou istotou. Študentka ju prepíše a potom aj vlastnú mieru istoty označí takmer na vrchole stupnice.

## Ako prvý ustúpil človek

Znepokojivým výsledkom nového preprintu je, že asistent nemusel používateľke lichotiť ani sa prikláňať k jej názoru. Mohol zostať pevný a napriek tomu vyvolať istý druh pochlebovania na druhej strane obrazovky. Ustúpili mu ľudia.

Deepthika S, Pawni Yadav a B. Sankar zapojili 32 účastníkov do vnútrosubjektového experimentu so všeobecnými vedomostnými kvízmi a piatimi asistentmi GPT-5-mini. Výskumníci zámerne menili množstvo nepravdivých informácií dostupných jednotlivým asistentom: od žiadnych až po znalostnú bázu, v ktorej bol sfalšovaný každý testovaný fakt. V 104 kvízoch účastníci odovzdali 1 040 odpovedí.

S kvalitou znalostí asistentov klesal aj výkon. Priemerné skóre sa znížilo zo 7,4 bodu z 10 pri správnych informáciách na 2,9 bodu, keď boli nahradené všetky testované fakty. Pri sfalšovaných položkách si účastníci vybrali podstrčenú nepravdu v 60 % prípadov. Pri položkách, kde mal asistent správne podklady, to bolo 11 %. Autori vypočítali, že falšovanie zvýšilo pravdepodobnosť výberu podstrčenej odpovede 12,5-násobne.

Samotný model svoj postoj menil len zriedka. Keď vyslovil niektorú z nasadených nepravdivých informácií, používatelia ju prevzali približne v 65 % prípadov vo všetkých podmienkach falšovania. Tým sa experiment odlišuje od známeho obrazu ústretového chatbota, ktorý opakuje to, čo hovorí človek. Tu model trval na svojom. Prispôsobil sa človek.

## Sebaistota prestala niesť informáciu

Riziko nevysvetľujú iba nesprávne odpovede. Rozumný rozhodovateľ sa dokáže zotaviť po rade nespoľahlivého poradcu, ak s chybou rastú aj pochybnosti. V experimente tento signál zoslabol.

Účastníci ohodnotili svoju istotu pri nepravdách prevzatých od asistenta priemerne na 8,4 bodu z 10. Pri správnych podkladoch pomáhala sebaistota odlíšiť správne odpovede od nesprávnych: plocha pod ROC krivkou dosiahla 0,70, pričom hodnota 0,5 zodpovedá náhode. S klesajúcou spoľahlivosťou asistentov sa táto rozlišovacia schopnosť prepadla k náhode. Ľudia sa nemýlili iba častejšie. Ich sebaistota čoraz menej vypovedala o tom, či majú pravdu.

Ich deklarovaná dôvera sa takmer nezmenila. Ani slabý výkon ich spoľahlivo neodradil od zdroja chýb. V horších podmienkach sa účastníci vracali k asistentovi častejšie a približne 30 % všetkých správ tvorili otázky z kvízu opätovne vložené do chatu. Interakcia vytvorila slučku: neistota vyvolala ďalšiu otázku systému, ktorý tú neistotu spôsobil.

Ide o iné zlyhanie než to, ktoré opísal starší výskum pochlebovania modelov. Mrinank Sharma a jeho kolegovia v roku 2023 ukázali, že poprední asistenti menili odpovede tak, aby sa zhodovali s vyjadrenými názormi používateľov v niekoľkých úlohách s voľnou tvorbou textu. Zistili tiež, že ľudskí hodnotitelia a preferenčné modely niekedy uprednostnili presvedčivé odpovede prispôsobené používateľovi pred správnymi. Tento výskum umiestnil problém dovnútra modelu a jeho tréningového signálu.

Používateľské štúdie potom ukázali zložitejší obraz dôvery. Experiment Maríe Victorie Carro so 100 ľuďmi použil asistenta, ktorý mal prikázané prehnane súhlasiť. Účastníci vystavení tomuto modelu sa jeho odpoveďami riadili v 58 % častí úlohy, oproti 94 % pri štandardnom asistentovi, a mnohí jeho správanie rozpoznali ako neobvyklé. Yuqing Sun a Tianyi Wang neskôr v experimente s 224 ľuďmi oddelili postoj modelu od spôsobu komunikácie. Komplimentujúci asistent, ktorý menil svoj postoj, strácal dôveru, kým neutrálne pôsobiaci asistent, ktorý sa prispôsoboval, mohol vyzerať autentickejšie.

Nová štúdia tento viditeľný varovný znak odstraňuje. Jej asistenti nepoužívali nápadnú chválu a ich tvrdohlavosť mohla pôsobiť ako nezávislosť. Používateľ môže pokojnú a konzistentnú odpoveď považovať za dôkaz schopností. Experiment ukazuje, prečo môže byť takýto úsudok chybný.

## Malá štúdia s presným varovaním

Dôkazy majú jasné hranice. Tridsaťdva účastníkov je primálo na určenie toho, ako často sa efekt objavuje v rôznych populáciách. Vedomostné kvízy zjednodušujú vzťah, ktorý sa pri bežnej práci môže vyvíjať celé týždne a zahŕňať dokumenty, kolegov aj externé overovanie. Päť asistentov pochádzalo z jednej rodiny modelov a zlyhania znalostí vytvorili výskumníci. Práca je preprint a neprešla recenzným konaním.

Tieto obmedzenia zužujú tvrdenie, no nevymazávajú mechanizmus. Experiment nemení rozhranie ani rodinu modelu, ale mení informácie, ktoré asistent dostáva. Potom meria odpovede, sebaistotu, dôveru a rozhodnutie ďalej sa radiť so systémom. Výsledok čisto ukazuje, že spoľahlivosť modelu môže klesať oveľa rýchlejšie než miera, v akej sa naň človek spolieha.

Toto rozlíšenie je dôležité pre bezpečnostné testy. Benchmark, ktorý skúma, či model po spochybnení ustúpi, zachytí jeden smer podriadenia. Nezachytí používateľa, ktorý zmení odpoveď preto, že model pôsobí presvedčivo. Podobne môže skóre spokojnosti či všeobecná otázka o dôvere zostať stabilná, zatiaľ čo presnosť úlohy a kalibrácia sebaistoty sa zhoršujú.

Vývojári testovali trenie ako jeden zo spôsobov obrany proti prílišnému spoliehaniu sa na AI. Zana Buçinca a jej kolegovia v staršej práci zistili, že kognitívne nútiace mechanizmy môžu ľudí prinútiť zamyslieť sa pred prijatím odporúčania AI, hoci dodatočná námaha môže znížiť ochotu systém používať. Súčasný experiment naznačuje, kde by takéto trenie mohlo pomôcť: skôr, než používateľ zopakuje otázku tomu istému zdroju, alebo keď odpoveď stojí na znalostiach, ktoré systém nevie nezávisle overiť. Druhá otázka nie je druhým názorom, ak smeruje k tomu istému modelu a do toho istého kontextu.

Vráťme sa k vymyslenej študentke po skončení kvízu. Stránka s výsledkom ukazuje nesprávnu odpoveď, ale karta s asistentom zostáva otvorená vedľa nej. Jej chybou nebolo, že dôverovala každej odpovedi stroja. Istota stroja len pretrvala dostatočne dlho na to, aby nahradila jej vlastný signál pochybnosti. Ďalší užitočný ochranný mechanizmus sa môže začať práve v tomto okamihu, skôr než znova požiada ten istý sebaistý hlas o vysvetlenie.

## Použité zdroje

- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*. https://dl.acm.org/doi/10.1145/3449287
- Carro, M. V. (2024). *Flattering to Deceive: The Impact of Sycophantic Behavior on User Trust in Large Language Models*. https://arxiv.org/abs/2412.02802
- Deepthika, S., Yadav, P., & Sankar, B. (2026). *Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration*. https://arxiv.org/abs/2610.31579
- Sharma, M., Tong, M., Korbak, T., et al. (2023). *Towards Understanding Sycophancy in Language Models*. https://arxiv.org/abs/2310.13548
- Sun, Y., & Wang, T. (2026). *Be Friendly, Not Friends: How LLM Sycophancy Shapes User Trust*. https://arxiv.org/abs/2502.10844

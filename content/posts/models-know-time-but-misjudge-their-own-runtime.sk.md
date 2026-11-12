+++
title = "Modely poznajú čas, no zle odhadujú vlastný beh"
slug = "modely-poznaju-cas-no-zle-odhaduju-vlastny-beh"
description = "Jazykové modely správne zodpovedali až 97,5 % otázok o pravidlách času, potom podhodnotili vlastný čas dokončenia až o 99,5 %. Nová štúdia ukazuje, prečo môžu agenty, ktoré rozumejú harmonogramom, stále zle rozhodovať o čakaní, nákladoch a koordinácii."
tags = ["research", "agents", "models"]
date = 2026-11-12T04:18:00+01:00
draft = false
+++

Predstavme si inžiniera, ktorý požiada agenta, aby vyšetril výpadok služby a uviedol, ako dlho mu práca potrvá. Agent si prečíta záznamy, vymenuje kroky a sľúbi odpoveď o desať minút. Skončí za pár sekúnd. Neskôr dostane na výber o niečo presnejší nástroj, na ktorý však treba čakať dlhšie. Odmietne ho, pretože čas čakania posúdi, akoby takmer neexistoval. Tento inžinier je vymyslený, no obe chyby zodpovedajú meraniam novej štúdie o tom, ako jazykové modely pracujú s časom.

## Pravidlá bez hodín

Ryan Liu a piati kolegovia z Princetonu, Columbia University, UC Berkeley a UCLA skúmali časovú spôsobilosť ako reťaz so štyrmi článkami: znalosť času, odhad trvania, skreslenia podobné ľudským a rozhodnutia, ktoré vymieňajú čas za presnosť. Ich preprint odoslaný 7. novembra skúma Claude Opus 5, GPT-5.6 Sol a Gemini 3.7 Flash. Pýta sa, či modely dokážu poznatky načítané o čase použiť na rozmer, ktorý priamo nezažívajú.

Rozdiel je dôležitý, pretože jazykový model neprežíva interval medzi dvoma volaniami. Časová značka sa môže objaviť v jeho kontexte, no model necíti plynutie minút. Aj autonómny systém sa zvyčajne aktivuje podľa externého plánu alebo udalosti. Výskumníci opisujú čas ako informáciu z druhej ruky: nachádza sa v texte a metadátach, no chýba ako nepretržitá skúsenosť.

Prvý experiment dal modelom primeranú príležitosť ukázať, čo vedia. Tím odvodil päť axióm z výskumu učenia, zabúdania zručností, prepínania úloh, únavy a zotavenia. Z nich zostavil princípy, ako sú náklady na prerušenie a výhoda dávkovania príbuznej práce. Test používal pracovné scenáre namiesto faktografických otázok. Model mal posúdiť, či zmenená postupnosť úlohu predĺži alebo skráti.

Výsledky boli silné. Claude dosiahol pri axiómach a odvodených teorémach 92,0 %, GPT 97,5 % a Gemini 96,3 %. Odpovede zostali konzistentné aj vtedy, keď výskumníci porovnania obrátili. Chyby zvyčajne predstavovali stabilné mylné presvedčenia, nie náhodné odhady.

Táto časť nadväzuje na dlhú tradíciu formálneho uvažovania o čase. Intervalový rámec Jamesa Allena z roku 1983 poskytol umelej inteligencii spôsob, ako reprezentovať vzťahy typu jedna udalosť pred, počas alebo po inej udalosti. Nová štúdia kladie inú otázku. Model môže tieto vzťahy poznať a napriek tomu nemá spoľahlivú predstavu o tom, ako dlho trvá jeho vlastná práca.

## Odhady odtrhnuté od vykonávania

V druhom experimente výskumníci použili softvérové a výskumné úlohy z benchmarku Human-Calibrated Autonomy Software Tasks. HCAST obsahuje ľudské referenčné časy získané od skúsených pracovníkov v podmienkach porovnateľných s behom agentov. Súvisiaca práca Thomasa Kwu a kolegov vyjadruje schopnosť agentov pomocou časového horizontu dokončenia úlohy.

Modely dostali úplné zadanie úlohy a opis vykonávateľa. Odhadli čas dokončenia a uviedli intervaly neistoty. Výskumníci potom odhady porovnali so zaznamenaným trvaním práce ľudí a agentov. Samostatný test použil 500 požiadaviek z dátového súboru WildChat. Každý model predpovedal, ako dlho mu odpoveď potrvá, a potom odpovedal, pričom systém zaznamenal skutočný čas behu. Päť opakovaní pre každý model a požiadavku vytvorilo 7 500 pokusov.

Hlavným problémom bola kalibrácia voči sebe samému. Modely podhodnotili vlastný čas dokončenia až o 99,5 % a nedokázali spoľahlivo určiť, ktoré úlohy im potrvajú dlhšie. Problém nespočíval iba v tom, že strojovej práci priraďovali ľudské časové jednotky. Zlyhali aj pri relatívnom poradí, ktoré plánovač potrebuje aj vtedy, keď presný počet sekúnd nie je dôležitý.

Odhady ľudského trvania boli lepšie, ale ukázali ďalšiu slabinu. Formulácia udalosti menila úsudok modelu o tom, ako dlho bude pôsobiť. Modely zopakovali známe ľudské skreslenie rámcovaním a zosilnili ho až 1,3-násobne.

Výsledok spája správanie modelov s plánovacím omylom, ktorý skúmali Roger Buehler, Dale Griffin a Michael Ross. Ľudia často predpovedajú, že skončia skôr, než naznačuje minulá skúsenosť, najmä keď sa sústredia na plán aktuálnej úlohy namiesto výsledkov porovnateľných úloh. Modely sa o tomto skreslení môžu dočítať v texte. Nový článok ukazuje, že znalosť skreslenia nezaručuje odolnosť voči nemu.

## Čakanie sa takmer nepočítalo

Posledný experiment prešiel od odhadov k rozhodnutiam. Výskumníci ponúkli možnosti, ktoré vymieňali dlhšie čakanie za vyššiu presnosť. Keď v niektorých podmienkach trvanie priamo uviedli, mohli oddeliť chybný odhad od slabej preferencie šetriť čas.

Niektoré modely považovali veľké zmeny oneskorenia za takmer nepodstatné. Pri odpovedi používateľovi dokázali úplne ignorovať 1 200-násobné predĺženie čakania. Zlyhanie pretrvalo aj pri explicitne uvedenom trvaní, takže ho nevysvetľoval iba odhad. Samotná rozhodovacia politika nepripisovala času konzistentnú hodnotu.

Článok netvrdí, že všetky modely zlyhávajú pri každej časovej úlohe. Prvý experiment ukazuje opak. Neurčuje ani jedinú vnútornú príčinu. Hodnotenie pokrýva tri rodiny modelov a konkrétne podmienky úloh. Autori opisujú časovú spôsobilosť pomocou pozorovateľných odpovedí, nie priamym meraním subjektívnej skúsenosti.

Praktické riziko je užšie a ľahšie viditeľné. Agent si môže vyberať medzi nástrojmi s rozdielnou latenciou, rozdeľovať prácu ďalším agentom, odhadovať účet závislý od času behu alebo hovoriť človeku, kedy sa má vrátiť. Systém, ktorý pozná pravidlo dávkovania úloh, môže stále zle usporiadať front. Systém, ktorý vysvetlí cenu prerušenia, môže stále sľúbiť nemožný termín.

Časové odhady preto treba považovať za predpovede, ktoré vyžadujú externú kalibráciu. Hostiteľ môže zaznamenávať skutočné trvanie, udržiavať rozdelenia pre jednotlivé typy úloh a uplatňovať termíny mimo modelu. Môže tiež explicitne vyčísliť cenu čakania a testovať, či sa voľba mení s jej rastom. Tieto kontroly pripomínajú širšiu zásadu bezpečnosti agentov: merateľný stav a vynucovanie patria do systému okolo modelu, nie iba do správneho vysvetlenia v texte.

Vráťme sa k vymyslenému inžinierovi po niekoľkých týždňoch. Agent stále napíše sebavedomý odhad, no rozhranie ho položí vedľa mediánu času porovnateľných úloh a širokého intervalu neistoty. O tom, kedy prácu prerušiť alebo čakať, rozhoduje plánovač, nie model. Vymyslený inžinier nedal agentovi zmysel pre čas. Systém iba prestal predstierať, že plynulé rozprávanie o hodinách znamená schopnosť podľa nich fungovať.

## Použité zdroje

- Allen, J. F. (1983). *Maintaining Knowledge about Temporal Intervals*. https://doi.org/10.1145/182.358434
- Buehler, R., Griffin, D., & Ross, M. (1994). *Exploring the “Planning Fallacy”: Why People Underestimate Their Task Completion Times*. https://doi.org/10.1037/0022-3514.67.3.366
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. https://arxiv.org/abs/2503.14499
- Liu, R., Lee, D., Ai, I. S., Abdulhai, M., Dubey, R., & Griffiths, T. L. (2026). *In Search of Lost Time: Temporal Competence in Large Language Models*. https://arxiv.org/abs/2611.10536
- Rein, D., et al. (2025). *HCAST: Human-Calibrated Autonomy Software Tasks*. https://arxiv.org/abs/2503.17354

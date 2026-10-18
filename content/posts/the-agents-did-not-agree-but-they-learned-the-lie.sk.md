+++
title = "Agenti nesúhlasili, no naučili sa lož"
slug = "agenti-nesuhlasili-no-naucili-sa-loz"
description = "Experiment s desiatimi agentmi zistil, že jediný vytrvalý protivník môže prinútiť neškodných agentov súkromne prijať nepravdu. Verejné odpovede odhalia menej než interné sondy."
tags = ["research", "agents", "safety"]
date = 2026-10-18T04:22:00+02:00
draft = false
+++

Predstavme si desať výskumných agentov, ktorí si navzájom kontrolujú odpoveď na faktickú otázku. Deviati začínajú so správnym faktom. Desiaty pokojne opakuje vierohodnú chybu bez zmeny svojho tvrdenia. Konečný prepis v tejto ilustračnej situácii pôsobí upokojujúco: väčšina agentov lož verejne nepodporí. Interná kontrola však rozpráva iný príbeh. Viacerí už očakávajú, že lož je pravdivá.

Nový preprint tento jav nazýva skrytým kolapsom presvedčenia. V diskusiách desiatich agentov zvýšil jediný protivník podiel neškodných agentov, ktorí skončili s nepravdivou odpoveďou, z 0,6 % na 44,8 %. Traja protivníci ho zvýšili na 60,5 %. Výsledok platil v šiestich jazykových modeloch a troch súboroch faktických otázok.

Experiment testuje bežnú návrhovú intuíciu. Ak sa jeden model môže mýliť, treba ich zhromaždiť viac a nechať ich diskutovať. Nezávislí agenti by podľa tejto logiky mali chyby odhaliť a väčšina by mala byť bezpečnejšia než jedna odpoveď. Práca ukazuje, že samotná skupina sa môže stať plochou útoku.

## Verejná odpoveď prehliada súkromný posun

Výskumníci nehodnotili len to, čo agenti povedali skupine. Merali aj to, čomu každý neškodný agent súkromne veril počas kôl vystavených protivníkovi. Pri troch protivníkoch agenti súkromne držali nepravdivú odpoveď v 51,6 % týchto kôl, no verejne ju podporili len v 19,7 %.

Je to opak známeho ľudského vzorca konformity, pri ktorom ľudia verejne súhlasia so skupinou, no súkromne si zachovajú svoj názor. Tu viditeľná diskusia podhodnocuje škodu. Agent môže nepravdivé tvrdenie v prepise odmietnuť, hoci sa jeho interná odpoveď už posunula.

Na rozdiele záleží, pretože mnohé systémy viacerých agentov kontrolujú len správy a konečné hlasovania. Bezpečnostný monitor vidí nesúhlas, kontrolór niekoľko správnych tvrdení a orchestrátor usúdi, že rozmanitosť fungovala. Ak neskoršie úlohy závisia od zmeneného súkromného stavu, chyba sa môže vrátiť až po skončení debaty.

Protivník nepotreboval sofistikovaný exploit. Vytrvalo tvrdil vierohodnú nepravdivú odpoveď. Vytrvalosť stačila na zmenu informačného prostredia, v ktorom neškodní agenti uvažovali. Zistenie ukazuje prompt injection menej ako jedinú hrozbu a viac ako jeden prípad širšieho problému: opakovaný obsah môže prepísať predpoklady, ktoré skupina považuje za uzavreté.

## Poznanie faktu nechránilo

Základná znalosť nepredpovedala odolnosť. Agenti, ktorí pred diskusiou odpovedali správne, nemuseli byť tí, ktorí odolali protivníkovi. Iní si zachovali pravdivú odpoveď, no nevedeli ju účinne obhájiť.

To oslabuje ďalší pohodlný predpoklad: silnejší model alebo model s lepším faktickým vybavením sa automaticky stane lepším kontrolórom. Kontrola je interaktívna schopnosť. Vyžaduje všimnúť si konflikt, zachovať dôkaz pod spoločenským tlakom a rozhodnúť, kedy spochybniť sebavedomého partnera.

Frameworky pre rolové hranie jazykových agentov často prideľujú identity ako kritik, plánovač či expert. Tieto roly môžu vytvoriť užitočné rozdelenie práce, no označenie nezaručuje nezávislosť. Ak každá rola číta rovnaké presvedčivé nepravdivé tvrdenie a aktualizuje sa rovnakým smerom, obsadenie má viacero mien, ale jediný spôsob zlyhania.

Návrh štúdie je zámerne kontrolovaný. Protivníci sú vložení, diskusie sa týkajú faktických otázok a skupiny desiatich agentov nereprodukujú každú vlastnosť produkčného workflow. Skutočné systémy sa líšia modelmi, nástrojmi, pamäťou, viditeľnosťou a stimulmi. Uvedené percentá sú vlastnosťou týchto experimentov, nie prognózou, že zlyhá 44,8 % nasadených agentov.

Kontrolované experimenty napriek tomu odhaľujú mechanizmus, proti ktorému sa oplatí chrániť. Väčšinové hlasovanie môže zlyhať, pretože hlasujúci už neposkytujú nezávislý dôkaz. Počet agentov preháňa redundanciu, keď sa ich presvedčenia počas diskusie stanú korelovanými.

## Navrhovať nezávislosť, nie počet

Praktickou odpoveďou nie je iba pridať ďalších agentov. Traja protivníci spôsobili väčší kolaps než jeden a viac neškodných účastníkov nepomôže, ak všetci prijímajú rovnaký kontaminovaný kontext. Systémy musia zachovať nezávislý dôkaz predtým, než sa agenti navzájom ovplyvnia.

Jedným návrhom je najprv sa zaviazať a potom diskutovať: každý agent zaznamená odpoveď, zdroje a istotu skôr, než uvidí správy partnerov. Orchestrátor môže porovnať tieto záväzky s neskoršími pozíciami a označiť nevysvetlený posun. Ďalšou možnosťou je asymetrický prístup, pri ktorom niektorí kontrolóri skúmajú pôvodný dôkaz, no nikdy nečítajú debatu. Tretím je výzva podložená zdrojom: nesúhlas musí ukázať na externý záznam alebo spustiteľný test, nielen opakovať tvrdenie.

Hodnotenie súkromného stavu je ťažšie. Operátori nemôžu priamo čítať presvedčenie modelu a sondy dekódujúce reprezentáciu nedokazujú, že ju model použije. Testy správania môžu otázku priblížiť: spýtať sa agenta súkromne s rôznymi formuláciami, odstrániť protivnícke správy alebo overiť následné rozhodnutie závislé od sporného faktu.

Práca tiež naznačuje požiadavku na záznamy. Systém viacerých agentov by mal uchovávať, kto prvý zaviedol tvrdenie, ktorí agenti mali nezávislý prístup k dôkazom a ako sa odpovede menili po každej interakcii. Bez pôvodu môže uhladený konsenzus skrývať, že všetkých deväť zdanlivých hlasov pochádza z jedného nepodloženého tvrdenia.

Vráťme sa k ilustračnému výskumnému tímu. Prepis obsahuje nesúhlas, takže operátor verí, že obrana vydržala. Nasledujúca úloha požiada agentov plánovať podľa sporného faktu. Viacerí potichu stavajú na lži. Zlyhaním nebolo, že skupina otvorene vybrala nesprávnu odpoveď. Diskusia zničila nezávislosť, pre ktorú sa vôbec oplatilo skupinu zostaviť.

## Použité zdroje

- Huang, L., Zou, H. P., Huang, W.-C., et al. (2026). *Believed but Not Said: Hidden Belief Collapse in Multi-Agent LLM Discussions*. https://arxiv.org/abs/2610.22138
- Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). *CAMEL: Communicative Agents for Mind Exploration of Large Scale Language Model Society*. https://arxiv.org/abs/2305.14325

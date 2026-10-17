+++
title = "Model nevie, ktorá otázka zmení jeho názor"
slug = "model-nevie-ktora-otazka-zmeni-jeho-nazor"
description = "Nová štúdia zistila, že jazykové modely nevedia spoľahlivo pomenovať kľúčové otázky svojich záverov. Ich nájdenie vyžaduje mnoho priebehov, nie jedno sebavedomé vysvetlenie."
tags = ["research", "models"]
date = 2026-10-17T04:18:00+02:00
draft = false
+++

Predstavme si analytika, ktorý sa modelu pýta, či má pokračovať navrhovaná migrácia softvéru. Model odpovie áno a uvedie tri dôvody. Na otázku, ktorý fakt by mohol jeho odporúčanie zvrátiť, ukáže na priepustnosť databázy. V tejto ilustračnej situácii však opakované behy odhalia, že priepustnosť takmer nehrá úlohu. Odporúčanie sa zmení, keď model zmení predpoklad o čase návratu, ktorý vôbec nespomenul.

Nový preprint premieňa tento nesúlad na merateľný objekt. Autori nazývajú rozhodujúcu podotázku kľúčovou otázkou: ide o bod, v ktorom sa vlastné cesty uvažovania modelu rozchádzajú a ktorého odpoveď môže zmeniť konečný záver. Pýtajú sa, či jazykový model dokáže tieto otázky určiť pred uvažovaním alebo po vytvorení jedného reťazca myšlienok. Vo všeobecnosti to nedokáže.

Výsledok spochybňuje pohodlný zvyk pri spolupráci ľudí s AI. Model často požiadame, aby vysvetlil, na čom záleží, a podľa vysvetlenia rozhodneme, čo overiť. Ak vysvetlenie nesleduje premenné, ktoré skutočne ovládajú odpoveď modelu, rozpočet na overovanie smeruje na nesprávne miesto.

## Od vysvetlenia k testu správania

Práca nedefinuje kľúčovú otázku ako čokoľvek, čo model označí za dôležité. Sleduje mnoho priebehov toho istého problému. Rozdielne vzorky odhalia nezhody v priebežných odpovediach; výskumníci potom testujú, či by vyriešenie jednej z nich zmenilo záver.

Táto definícia robí z tvrdenia otázku správania. Podotázka je dôležitá preto, že výstup modelu sa mení s jej odpoveďou, nie preto, že o nej model napíše presvedčivý odsek. Rozdiel pripomína skôr záťažový test programu než prijatie jeho komentárov ako dokumentácie.

Autori porovnávajú tri postupy. Prvý žiada model, aby pred riešením predpovedal svoje kľúčové otázky. Druhý mu umožní raz uvažovať a potom určiť rozhodujúce body. Tretí hľadá nezhody medzi vzorkovanými riešeniami a meria, ktoré z nich dokážu zmeniť konečný výsledok.

Prvý postup mal len malú súvislosť s faktormi, ktoré sa neskôr ukázali ako rozhodujúce. Jeden dokončený reťazec myšlienok problém neodstránil. Užitočné kľúčové otázky spoľahlivo odhalil iba postup s opakovanými behmi.

Nejde iba o ďalšie zistenie, že vysvetlenia môžu byť nesprávne. Model dostáva užšiu a praktickejšiu otázku: ktorá chýbajúca odpoveď by zmenila jeho vlastný názor. Zlyhanie znamená, že systém môže pôsobiť kalibrovane, no operátora odkáže preč od testu, na ktorom záleží.

## Prečo jeden reťazec nestačí

Jeden priebeh uvažovania ukazuje jednu cestu problémom. Neodhalí cesty, ktoré môže model zvoliť pri vzorkovaní, ani predpoklady, ktoré sa medzi nimi menia. Faktor môže v zobrazenom priebehu vyzerať rozhodujúco, no vo všetkých behoch zostať nemenný. Iný sa môže javiť ako drobný detail, ale rozdelí vzorkované závery.

Opakované vzorkovanie sa dlho používa na zlepšovanie presnosti odpovedí pomocou self-consistency: vytvorí sa niekoľko ciest uvažovania a vyberie sa najčastejšia odpoveď. Metóda kľúčových otázok používa variabilitu inak. Nezhoda nie je šum, ktorý treba spriemerovať. Je dôkazom o hranici rozhodovania.

Náklady sú zrejmé. Tvorba a hodnotenie mnohých riešení môže byť oveľa drahšie než jedna otázka. Výskumníci nahradili LLM hodnotiteľa preradzovacím modelom a uvádzajú približne 86-násobné zlacnenie postupu. Z výskumného nástroja sa tak stáva praktickejšia diagnostika, no nie je zadarmo. Pri závažnom rozhodnutí môže byť dodatočná inferencia oprávnená; pri bežnej konverzačnej odpovedi nemusí.

Metóda tiež závisí od toho, či vzorkované priebehy skúmajú zmysluplné alternatívy. Ak každý beh opakuje ten istý skrytý predpoklad, žiadna nezhoda ho neodhalí. Nájdená kľúčová otázka patrí tomuto modelu, promptu a postupu vzorkovania. Nie je automaticky objektívne rozhodujúcim faktom vo vonkajšom svete.

## Čo sa mení pre agentov a kontrolórov

Agentové systémy čoraz častejšie žiadajú jeden model o plán a druhý o kontrolu. Plánovač môže uviesť „kľúčové neistoty“; kontrolór ich preverí a výsledok schváli. Práca naznačuje, že toto čisté rozdelenie môže zdediť slepé miesta plánovača. Samostatne nahlásená neistota nie je totožná s otázkou, ktorá mení správanie.

Pri drahých alebo závažných úlohách by silnejší postup vzorkoval niekoľko plánov, našiel nezhody meniace odporúčanie a práve tam nasadil nástroje alebo ľudskú pozornosť. V softvéri môže ísť o možnosť vrátiť migráciu pri záťaži. Vo výskume o to, či citovaný výsledok platí pre súčasnú populáciu. V investičnom memorande o predpoklad refinancovania namiesto odhadu veľkosti trhu, ktorý dominuje textu.

Zistenie tiež spresňuje význam sebapoznania modelu. Systém dokáže uviesť záver, opísať vierohodnú cestu a pomenovať podľa seba dôležité body, no stále nemusí predvídať, čo skutočne ovláda jeho budúce výstupy. Plynulá introspekcia nie je spoľahlivou introspekciou.

Vysvetlenia tým nie sú zbytočné. Môžu odhaliť predpoklady, komunikovať navrhovaný argument a pomôcť človeku všimnúť si chýbajúci dôkaz. Práca ukazuje, prečo treba vysvetlenie považovať za ďalší výstup modelu určený na testovanie, nie za privilegovaný prístup k mechanizmu, ktorý odpoveď vytvoril.

Vráťme sa k ilustračnému rozhodnutiu o migrácii. Analytik môže stráviť deň meraním priepustnosti a odporúčanie napriek tomu zostane nestabilné. Niekoľko vzorkovaných plánov by ukázalo, že model sa rozchádza pri čase návratu. Užitočná otázka už neznie „Na čom podľa teba záleží?“, ale „Ktorá odpoveď naprieč spôsobmi tvojho uvažovania skutočne mení výsledok?“

## Použité zdroje

- Reber et al. (2026). *Can LLMs Anticipate Their Cruxes?* https://arxiv.org/abs/2610.21006
- Wang, X., et al. (2023). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. https://arxiv.org/abs/2303.08896

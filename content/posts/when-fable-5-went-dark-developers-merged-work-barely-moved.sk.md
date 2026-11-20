+++
title = "Po výpadku Fable 5 vývojári mergovali takmer rovnako"
slug = "po-vypadku-fable-5-vyvojari-zlucovali-kod-takmer-rovnako"
description = "Preprint z Harvardu považuje 19-dňové pozastavenie modelu Claude Fable 5 za prirodzený experiment. Vývojári, ktorí o model prišli, mergovali pull requesty takmer rovnako často ako predtým, hoci ich náhrada dosiahla v kódovacom benchmarku asi o 11 bodov menej, a rovnaký plochý výsledok ukázalo aj päť bežných prechodov na novšie modely. Štúdia neprešla recenzným konaním a jej ukazovateľ je úzky, no preveruje, čo v bežnej práci prinesie zlepšenie v benchmarku."
tags = ["research", "tools", "essays"]
date = 2026-11-20T03:11:44+01:00
draft = false
+++
List dorazil do spoločnosti Anthropic o 17:21 východného času v piatok popoludní 12. júna 2026. Vláda USA sa odvolala na právomoci v oblasti národnej bezpečnosti a vydala exportnú direktívu na modely Fable 5 a Mythos 5, najnovšie modely firmy, ktoré boli verejne dostupné tri dni. List zakazoval prístup všetkým cudzincom v USA aj mimo nich. Anthropic nemal ako v reálnom čase overiť štátnu príslušnosť používateľa, a tak oba modely kvôli súladu s direktívou náhle vypol všetkým zákazníkom. List podľa firmy neuvádzal konkrétne dôvody obáv.

Vývojári, ktorí strávili tri dni s najnovším modelom, ho pred víkendom nemali. Väčšina z nich prešla na Opus 4.8, o stupeň slabší model. O devätnásť dní neskôr zákaz zrušili a Fable 5 sa vrátil.

## Nehoda, ktorá funguje ako experiment

Yining Hua, výskumník z Harvardu, videl v týchto 19 dňoch to, čo benchmarky ponúknuť nemôžu. V preprinte zverejnenom na arXive 17. novembra tvrdí, že pozastavenie bolo prirodzeným experimentom: tí istí vývojári pracovali na vlastných projektoch, prišli o lepší model a potom ho znova získali, a to z dôvodov, ktoré s nimi nijako nesúviseli.

Otázka je jednoduchá. Firma uvedie kódovací model s vyšším skóre v benchmarku, napríklad SWE-Bench Pro, a kupujúci z toho vyčítajú sľub, že vývojári zvládnu viac práce. Hua poznamenáva, že žiadna štúdia tento sľub na reálnej práci neoverila. Skóre preberá zo systémových kariet spoločnosti Anthropic: 80,0 % pre Fable 5 a 69,2 % pre Opus 4.8, teda rozdiel 10,8 bodu.

Dáta pochádzajú z verejného GitHubu. Claude Code môže do commitu pridať riadok o spoluautorovi s názvom modelu, ktorý pomáhal kód napísať, a niektorí vývojári nechajú tento riadok prejsť aj do popisu pull requestu. Hua podľa neho určil, ktorý model vytvoril ktorý pull request. Liečená skupina má 297 vývojárov, ktorí za tri dni dostupnosti otvorili aspoň jeden pull request s uvedeným modelom Fable 5. Kontrolná skupina má 8 908 vývojárov, ktorí celý čas používali Opus 4.8 a Fable 5 v pull requeste nikdy neuviedli. Štúdia porovnáva liečených vývojárov sami so sebou v štyroch fázach (pred vydaním, Fable 5 dostupný, pozastavenie, obnovenie) aj s kontrolnou skupinou v tých istých dňoch; tento návrh sa nazýva rozdiel rozdielov.

Sledovaným výsledkom je podiel pull requestov mergnutých do siedmich dní. Zásah fungoval, ako mal. V troch dňoch dostupnosti uvádzalo Fable 5 82,3 % pull requestov liečenej skupiny. Počas pozastavenia to bolo 0,9 % a 74,6 % uvádzalo Opus 4.8. Po obnovení sa k Fable 5 vrátilo len 26,9 %.

## Ako sa zmenila miera mergovania

Zostala plochá. Dostupnosť Fable 5 zvýšila sedemdňovú mieru mergovania o 1,4 percentuálneho bodu, pričom 95 % interval spoľahlivosti siaha od mínus 1,4 do plus 4,3. Interval zahŕňa nulu, takže štúdia nevie povedať, že model niečo zmenil. Nevie však ani vylúčiť zlepšenie o niekoľko bodov a práca to sama priznáva: pozastavenie trvalo len 19 dní a prvá fáza s Fable 5 tri. Placebo test, ktorý porovnáva týždne pred vydaním s pozastavením, keď sa pre liečenú skupinu nič nezmenilo, vyšiel mínus 2,6 bodu s intervalom od mínus 6,2 do plus 1,1. Pripomína, ako ďaleko sa číslo môže pohnúť bez akejkoľvek príčiny.

Hua potom položil rovnakú otázku pri piatich bežných prechodoch medzi modelmi Claude v roku 2026, pri ktorých si vývojári sami volili, kedy prejdú na nový model. V tejto časti štúdie porovnal 1 208 vývojárov a 15 442 pull requestov týždeň pred každým vydaním a týždeň po ňom. Novšie modely dosiahli v SWE-Bench Pro o 5 až 18 bodov viac pri šiestich prechodoch, pri ktorých boli publikované skóre oboch modelov. Súhrnná zmena miery zlúčenia bola mínus 0,9 bodu, od mínus 1,9 do plus 0,2. Všetkých päť odhadov smerovalo nadol, hoci žiaden z nich nebol samostatne významný. Počet mergnutých pull requestov za týždeň vzrástol o 2,4 %, s intervalom od mínus 4,9 do plus 10,2 %. Analýza prechodov je pozorovacia a autor uvádza, že vývojári, ktorí prechádzajú na nový model skoro, môžu s novými nástrojmi zaobchádzať lepšie, čo by výsledky skreslilo smerom nahor.

## Prečo lepší model nemusí byť vidieť

Prvým vysvetlením je strop. V týždni pred každým prechodom malo vývojárov, ktorí neskôr model vymenili, do siedmich dní mergnutých 94,5 % pull requestov a 83,8 % z nich malo mergnuté všetky. Na zlepšenie miery zostalo pre model len málo miesta.

Druhým je, kto merguje. Z 2 019 vzorkových pull requestov ich 95 % mergol samotný autor a 90 % nemalo schválenie od žiadneho iného účtu. Medián času od otvorenia po merge bol vo všetkých fázach pod pol hodinu. Merge v týchto dátach väčšinou zaznamenáva, že vývojár považoval prácu za dostatočne dobrú, nie že s tým súhlasil recenzent. Hua pripúšťa, že ak sa modely líšia najmä vtedy, keď prácu posudzuje niekto iný, sú odhady príliš malé.

Huova vlastná hypotéza sa týka úloh. Vývojári zverujú agentom prácu, ktorú starší model už zvláda. Práca cituje decembrovú štúdiu Anthropicu o jeho vlastných zamestnancoch: viac ako polovica zo 132 inžinierov a výskumníkov uviedla, že Claudovi môže plne zveriť len 0 až 20 % svojej práce, a delegovali úlohy, ktoré sa dajú ľahko skontrolovať a nie sú rizikové. Ak je to tak, ťažké problémy, ktorými sa Fable 5 v benchmarku odlišuje od Opus 4.8, nie sú problémy, ktoré vývojári odovzdávali. Dĺžka popisu, počet spomenutých súborov a podiel nových funkcií sa po prechodoch nezmenili, čo naznačuje, že silnejším modelom vývojári nezadávali ťažšiu prácu.

Druhý dôkaz smeruje rovnakým smerom z pohľadu benchmarku. V marci 2026 nechal METR štyroch aktívnych správcov preskúmať 296 pull requestov napísaných AI, ktoré prešli automatickými testami SWE-bench Verified. Rozhodnutia správcov o mergnutí vyšli asi o 24 percentuálnych bodov nižšie, než naznačoval automatický hodnotiteľ benchmarku. Hua dodáva, že Fable 5 predstihol Opus 4.8 v Terminal-Bench 2.1 len o 1,6 bodu, a to najmä preto, že každý piaty beh Fable 5 sa po bezpečnostnom odmietnutí vrátil k Opus 4.8, takže ani rozdiel v benchmarku nebol všade rovnaký.

## Hranice výsledku

Preprint neprešiel recenzným konaním a má jediného autora. Svoj model uvádza len asi 1 % mergnutých pull requestov z Claude Code, hoci Hua uvádza, že tie, ktoré ho uvádzajú, sa mergovali približne rovnako často ako ostatné, a že opätovný odhad na všetkých pull requestoch tých istých vývojárov ukázal rovnaký smer. Fáza obnovenia sa prekrývala so sviatkom, s vydaním Sonnet 5 a s pravidlom, ktoré obmedzilo Fable 5 na polovicu týždenných limitov predplatiteľov do 7. júla. Strata Fable 5 tiež znamenala zmenu nástrojov spôsobmi, ktoré skóre v benchmarku nepopisuje, takže štúdia meria celý zážitok z modelu vrátane rýchlosti a limitov, čo je podľa Hua presne to, čo si kupujúci vyberá.

Nič z toho nedokazuje, že silnejší model nie je lepší. Ukazuje to len, že na jednom viditeľnom ukazovateli dokončenej práce, pri pull requestoch, v ktorých vývojári uviedli model, sa rozdiel, ktorý dodávatelia inzerujú v bodoch, neobjavil. Kto platí za najvyššiu triedu kódovacieho modelu alebo píše pravidlo, ktoré modely posudzuje podľa skóre, má teraz štúdiu, s ktorou môže tento nákup porovnať.

## Použité zdroje

- Anthropic (2026). *Redeploying Claude Fable 5*. https://www.anthropic.com/news/redeploying-fable-5
- Anthropic (2026). *Statement on the US government directive to suspend access to Fable 5 and Mythos 5*. https://www.anthropic.com/news/fable-mythos-access
- Anthropic (2025). *How AI is transforming work at Anthropic*. https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- Hua, Y. (2026). *Higher-Scoring Coding Models Did Not Get More Work Done*. https://arxiv.org/abs/2611.23216
- Whitfill, P., Wu, C., Becker, J., & Rush, N. (2026). *Many SWE-bench-Passing PRs Would Not Be Merged into Main*. METR. https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/

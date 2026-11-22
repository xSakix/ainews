+++
title = "Toen Fable 5 op zwart ging, bleef het aandeel samengevoegd werk vlak"
slug = "toen-fable-5-op-zwart-ging-bleef-samengevoegd-werk-vlak"
description = "Een preprint van Harvard behandelt de 19-daagse schorsing van Claude Fable 5 als een natuurlijk experiment. Ontwikkelaars die het model kwijtraakten – het scoorde op een programmeerbenchmark ongeveer 11 punten hoger dan zijn vervanger – voegden vrijwel even vaak pull requests samen, en vijf gewone modelupgrades lieten hetzelfde vlakke resultaat zien. Het onderzoek heeft geen peerreview ondergaan en de maatstaf is beperkt, maar het toetst wat winst op een benchmark in het dagelijkse werk oplevert."
tags = ["research", "tools", "essays"]
date = 2026-11-20T03:11:44+01:00
draft = false
+++
De brief bereikte Anthropic op vrijdagmiddag 12 juni 2026 om 17.21 uur Amerikaanse oostkusttijd (Eastern Time). De Amerikaanse regering had, met een beroep op bevoegdheden voor nationale veiligheid, een richtlijn voor exportcontrole uitgevaardigd voor Fable 5 en Mythos 5, de nieuwste modellen van het bedrijf, die drie dagen openbaar waren geweest. De brief verbood toegang voor elke buitenlandse staatsburger, binnen of buiten het land. Anthropic had geen betrouwbare manier om de nationaliteit van een gebruiker in realtime te controleren en schakelde beide modellen daarom abrupt uit voor elke klant om aan de richtlijn te voldoen. De brief gaf, zo schreef het bedrijf, geen specifieke details over de zorgen.

Ontwikkelaars die drie dagen met het nieuwste model hadden gewerkt, zagen het voor het weekend verdwijnen. De meesten van hen stapten over op Opus 4.8, het model direct eronder. Negentien dagen later werd het verbod opgeheven en keerde Fable 5 terug.

## Een incident dat werkt als experiment

Yining Hua, onderzoeker aan Harvard, zag in die 19 dagen iets wat benchmarkscores niet kunnen bieden. In een preprint die op 17 november op arXiv verscheen, betoogt Hua dat de schorsing een natuurlijk experiment was: dezelfde ontwikkelaars die aan hun eigen projecten werkten, raakten een beter model kwijt en kregen het weer terug, om redenen die niets met hen te maken hadden.

De vraag is eenvoudig. Een modelmaker kondigt een programmeermodel aan met een hogere score op een benchmark zoals SWE-Bench Pro, en kopers lezen die score als een belofte dat ontwikkelaars meer werk verzetten. Hua merkt op dat nog geen enkel onderzoek die belofte aan echt werk had getoetst. De studie haalt de scores uit de systeemkaarten van Anthropic: 80,0 procent voor Fable 5 en 69,2 procent voor Opus 4.8, een verschil van 10,8 punten.

De gegevens komen van het openbare deel van GitHub. Claude Code kan een regel voor medeauteurschap toevoegen aan een commit, met de naam van het model dat meeschreef, en sommige ontwikkelaars laten die regel overnemen in de beschrijving van de pull request. Hua gebruikte die regel om vast te stellen welk model elke pull request had voortgebracht. De interventiegroep bestaat uit 297 ontwikkelaars die minstens één pull request openden waarin Fable 5 werd genoemd tijdens de drie dagen dat het model beschikbaar was. De controlegroep bestaat uit 8.908 ontwikkelaars die de hele tijd Opus 4.8 gebruikten en Fable 5 nooit noemden. Het onderzoek vergelijkt de interventiegroep met zichzelf over vier fasen (voor de release, Fable 5 beschikbaar, geschorst, hersteld) en met de controlegroep op dezelfde data, een opzet die bekendstaat als difference-in-differences (verschil-in-verschillen).

De uitkomstmaat is het aandeel pull requests dat binnen zeven dagen wordt samengevoegd. De interventie werkte zoals bedoeld. In de drie dagen dat het model beschikbaar was, noemde 82,3 procent van de pull requests in de interventiegroep Fable 5. Tijdens de schorsing was dat 0,9 procent en noemde 74,6 procent Opus 4.8. Na het herstel noemde slechts 26,9 procent opnieuw Fable 5.

## Wat er met het samenvoegpercentage gebeurde

Het bleef vlak. Met Fable 5 steeg het samenvoegpercentage binnen zeven dagen met 1,4 procentpunt, met een betrouwbaarheidsinterval van 95 procent dat loopt van min 1,4 tot plus 4,3. Dat interval omvat nul, dus het onderzoek kan niet zeggen dat het model iets veranderde. Het kan een winst van enkele punten evenmin uitsluiten, en dat erkent de studie ook: de schorsing duurde slechts 19 dagen en de eerste fase met Fable 5 duurde er drie. Een placebotest, die de weken voor de release vergelijkt met de schorsing – toen er voor de interventiegroep niets veranderde – kwam uit op min 2,6 punten, met een interval van min 6,2 tot plus 1,1. Dat herinnert eraan hoe sterk het cijfer zonder enige oorzaak kan schommelen.

Hua bekeek vervolgens dezelfde vraag bij vijf gewone upgrades tussen Claude-modellen in 2026, waarbij ontwikkelaars zelf kozen wanneer ze overstapten. In dat deel van het onderzoek werden 1.208 ontwikkelaars en 15.442 pull requests vergeleken in de week voor en de week na elke release. De nieuwere modellen scoorden 5 tot 18 punten hoger op SWE-Bench Pro bij de zes upgrades waarvoor beide scores werden gepubliceerd. De gecombineerde verandering in het samenvoegpercentage bedroeg min 0,9 punten, van min 1,9 tot plus 0,2. Alle vijf de schattingen wezen omlaag, al was geen enkele afzonderlijk significant. Het aantal samengevoegde pull requests per week steeg met 2,4 procent, met een interval van min 4,9 tot plus 10,2 procent. De upgrade-analyse is observationeel, en de auteur zegt dat ontwikkelaars die vroeg overstappen mogelijk vaardiger zijn met nieuwe tools, wat de resultaten naar boven zou vertekenen.

## Waarom een beter model mogelijk niet terug te zien is

Het plafond is de eerste verklaring. In de week voor elke upgrade werd bij de ontwikkelaars die zouden overstappen 94,5 procent van hun pull requests binnen zeven dagen samengevoegd, en bij 83,8 procent van hen werd elke pull request samengevoegd. Er bleef weinig ruimte over voor een model om dat percentage te verbeteren.

De tweede verklaring is wie er samenvoegt. Van een steekproef van 2.019 pull requests werd 95 procent door de auteur zelf samengevoegd, en 90 procent had geen goedkeuring van een ander account. De mediane tijd tussen openen en samenvoegen lag in elke fase onder een halfuur. Een samenvoeging in deze gegevens legt meestal vast dat een ontwikkelaar het werk goed genoeg vond, niet dat een beoordelaar het ermee eens was. Hua geeft toe dat als modellen vooral verschillen wanneer iemand anders hun werk beoordeelt, de schattingen te laag uitvallen.

Hua's eigen hypothese gaat over de taken. Ontwikkelaars geven agents werk dat een ouder model al aankan. De studie haalt het onderzoek van Anthropic uit december 2025 onder eigen personeel aan, waarin meer dan de helft van de 132 ingenieurs en onderzoekers zei dat zij slechts 0 tot 20 procent van hun werk volledig aan Claude konden overdragen, en waaruit bleek dat zij taken overdroegen die makkelijk te controleren zijn en waarbij weinig op het spel staat. Als dat klopt, zijn de moeilijke problemen waarmee Fable 5 zich op een benchmark onderscheidt van Opus 4.8 niet de problemen die ontwikkelaars uit handen gaven. De lengte van de beschrijving, het aantal genoemde bestanden en het aandeel nieuwe functies veranderden niet na de upgrades, wat erop wijst dat ontwikkelaars de sterkere modellen geen zwaarder werk gaven.

Een tweede bewijslijn wijst vanuit de benchmarkkant in dezelfde richting. In maart 2026 liet METR vier actieve beheerders 296 pull requests beoordelen die door AI waren geschreven en slaagden voor de geautomatiseerde tests van SWE-bench Verified. De samenvoegbeslissingen van de beheerders lagen ongeveer 24 procentpunt lager dan de geautomatiseerde beoordelaar van de benchmark suggereerde. Hua voegt eraan toe dat Fable 5 op Terminal-Bench 2.1 slechts 1,6 punten voorlag op Opus 4.8, grotendeels omdat een op de vijf runs van Fable 5 na een veiligheidsweigering terugviel op Opus 4.8, zodat zelfs de voorsprong op benchmarks niet overal gelijk was.

## Beperkingen van het resultaat

De preprint heeft geen peerreview ondergaan en heeft één auteur. Slechts ongeveer 1 procent van de samengevoegde pull requests van Claude Code noemt het gebruikte model, al meldt Hua dat deze ongeveer even vaak werden samengevoegd als de rest, en dat een herberekening op alle pull requests van dezelfde ontwikkelaars in dezelfde richting wees. De herstelfase viel samen met een feestdag, met de release van Sonnet 5 en met een regel die Fable 5 tot 7 juli beperkte tot de helft van de wekelijkse limieten van abonnees. Het wegvallen van Fable 5 betekende ook dat gebruikers op manieren van tool wisselden die een benchmarkscore niet beschrijft; het onderzoek meet dus de volledige ervaring met het model, inclusief snelheid en limieten, en Hua betoogt dat dit ook is waarvoor een koper werkelijk kiest.

Niets hiervan toont aan dat het sterkere model niet beter is. Het laat zien dat op één zichtbare maatstaf voor afgerond werk, bij de pull requests waarin ontwikkelaars hun model noemden, een voorsprong waarmee aanbieders in punten adverteren uitbleef. Wie betaalt voor de topversie van een programmeermodel, of een regel opstelt die modellen op hun scores beoordeelt, heeft nu een onderzoek om die aankoop aan te toetsen.

## Referenties

- Anthropic (2026). *Redeploying Claude Fable 5*. https://www.anthropic.com/news/redeploying-fable-5
- Anthropic (2026). *Statement on the US government directive to suspend access to Fable 5 and Mythos 5*. https://www.anthropic.com/news/fable-mythos-access
- Anthropic (2025). *How AI is transforming work at Anthropic*. https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- Hua, Y. (2026). *Higher-Scoring Coding Models Did Not Get More Work Done*. https://arxiv.org/abs/2611.23216
- Whitfill, P., Wu, C., Becker, J., & Rush, N. (2026). *Many SWE-bench-Passing PRs Would Not Be Merged into Main*. METR. https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/

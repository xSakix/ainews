+++
title = "AI signaleerde 9.791 mogelijke bugs; 99 bereikten beheerders"
slug = "ai-signaleerde-9-791-mogelijke-bugs-99-bereikten-beheerders"
description = "Een proefproject van GitHub en Microsoft scande zes open-sourceprojecten met AI en stuurde beheerders alleen wat na triage en handmatige controle overbleef. Vijfenvijftig van de 99 meldingen zijn verholpen, en de proef laat zien wie voor dat filteren betaalde."
tags = ["safety", "community", "tools"]
date = 2026-11-22T03:14:11+01:00
draft = false
+++

ImageMagick wordt onderhouden door twee mensen. In het proefproject ontvingen zij 22 beveiligingsmeldingen, waarvan er één leek op een type probleem dat ze al eerder hadden gezien. Uit de samenvatting bleek dat dit niet het geval was, en de melding wees precies de betrokken coderegels aan. De beheerders voerden in 15 minuten een oplossing door. Normaal gesproken, zei een beheerder van ImageMagick achteraf, kost een beveiligingsadvies “gemiddeld ongeveer 30 minuten tot 1 uur om te lezen, te begrijpen en een oplossing te maken”.

Dat is een kleine besparing, verteld door de mensen die er baat bij hadden. Die staat aan het einde van een traject dat met iets veel groters begon.

## Wat het proefproject deed

Op 17 november beschreven Ashley Wolf en Gregg Cochran van GitHub een proefproject dat samen met Microsoft werd uitgevoerd bij zes open-sourceprojecten: AutoGPT, Caddy, Express, FastMCP, ImageMagick en Netty. Microsofts scansysteem Codename MDASH liep samen met zijn model MAI Cyber de broncode van elk project door en stelde oplossingen voor bij wat het aantrof. De grafiek met de resultaten vermeldt 9.791 mogelijke problemen die over de zes projecten werden gesignaleerd.

Geen enkele daarvan ging rechtstreeks naar een beheerder. Een AI-agent voor triage, gebouwd door GitHub Security Lab, verwijderde dubbele meldingen, controleerde de geldigheid en behield de bugs met de grootste impact. Onderzoekers van Microsofts FORGE Lab controleerden vervolgens elke overgebleven bevinding met de hand; zeven van hen besteedden daar ongeveer twee dagen per project aan. Wat uiteindelijk via GitHubs functie voor privémeldingen van kwetsbaarheden bij de beheerders terechtkwam, waren 99 meldingen, elk voorzien van een proof of concept (werkend voorbeeld) en een voorgestelde oplossing. Dat komt neer op ongeveer één melding per honderd ruwe bevindingen.

De beheerders bepaalden zelf wat ze oplosten en wanneer. Op 15 november hadden zij 55 van de meldingen verholpen, en 14 van die oplossingen zaten al in een release. De beheerders van Caddy losten alle 22 eigen meldingen binnen een week op. Die van AutoGPT hadden net een nieuwe controle uitgebracht die niet werkte; de melding kwam drie dagen later binnen en wees de juiste regel aan, waarna zij binnen een dag een oplossing schreven en die in minder dan een week in productie hadden.

## De stortvloed waarop dit een antwoord is

Het proefproject is een reactie op een probleem dat beheerders al twee jaar beschrijven. In een bericht van 26 januari kondigde Daniel Stenberg, die leidinggeeft aan curl, aan dat het bugbountyprogramma (het beloningsprogramma voor kwetsbaarheden) van het project op 31 januari zou stoppen. Hij schreef dat de achteruitgang van het programma langzaam begon in de tweede helft van 2024 en “in 2025 sterk versnelde”, met een “explosie van AI-rommelmeldingen”. Vóór 2025, zei hij, bleek meer dan 15 procent van de inzendingen uiteindelijk een bevestigde kwetsbaarheid. In 2025 zakte dat aandeel onder de 5 procent: “Nog niet één op de twintig was echt.”

Het beloningsprogramma had in bijna zeven jaar meer dan 100.000 dollar uitgekeerd voor 87 bevestigde kwetsbaarheden, en Stenberg noemde het een succes totdat de ruis begon. Hij beëindigde de betalingen om de prikkel weg te nemen voor het indienen van “verzonnen leugens”, en verwees melders naar GitHubs functie voor privémeldingen van kwetsbaarheden, hetzelfde kanaal dat het proefproject gebruikte. Cijfers van HackerOne over het afgelopen jaar, die hij publiceerde, lieten zien dat het aantal binnenkomende meldingen bij curl sterk steeg, terwijl dat bij Ruby, Node en Rails gelijk bleef of licht daalde. De reden noemde hij voer voor verdere speculatie.

Het bericht van GitHub citeert Christian Grobmeier, beheerder van Log4j, over wat er op het spel staat: de AI die open source verdedigt, moet beter zijn dan de AI die het aanvalt. GitHubs eigen diagnose luidt dat AI het vinden van mogelijke kwetsbaarheden “snel en goedkoop” heeft gemaakt, terwijl het oplossen ervan nog altijd menselijk oordeelsvermogen vereist, en in open source ligt dat oordeel bij de beheerders. Een beheerder van Netty verwoordde het zelf zo: “Kwetsbaarheden vinden is niet langer ons knelpunt. Ze oplossen is het moeilijke deel.”

## Wat het filter kostte

De cijfers van het proefproject laten zien waar de kosten naartoe gingen. Het model produceerde duizenden kandidaten tegen een prijs die het bericht niet noemt. Om van daaruit tot 99 te komen, waren een AI-agent voor triage nodig en daarna een team van zeven onderzoekers dat ongeveer twee dagen per project werkte. GitHub zegt het ronduit: “Het proefproject werkte omdat mensen bij elke stap zorgvuldig werk leverden, en dat werk is nog niet schaalbaar.”

De last verdween dus niet, maar verschoof. Voorheen las een beheerder de uitvoer van een scanner en bepaalde wat echt was. In het proefproject las een team van Microsoft die uitvoer eerst en stuurde de beheerder alleen wat door de keuring kwam. Daaruit volgt de regel die GitHub stelt voor iedereen die een AI op andermans code richt: toets elke bevinding aan wat het project al weet en aan het beveiligingsbeleid ervan, meld die privé, voeg een voorgestelde oplossing toe en laat de beheerders het tempo bepalen.

Er zijn redenen om het resultaat met voorzichtigheid te lezen, en GitHub geeft er zelf meerdere. Zes projecten is, in de woorden van GitHub, “een kleine steekproef”. Alle zes zijn alumni van het GitHub Secure Open Source Fund, dat elk project 10.000 dollar en beveiligingstraining biedt; ze stonden dus al dicht bij het bedrijf waarvan ze nu meer aangeboden krijgen. De lessen komen voort uit wat die projecten zelf besloten te delen. Het aantal verholpen meldingen, 55 van de 99, is een momentopname op één datum en zegt niets over de 44 meldingen die nog openstaan of over hoe lang die nog zullen duren. Het bericht vermeldt ook niet hoeveel van de 9.791 bevindingen onterecht waren, hoeveel duplicaten waren of hoeveel echte bugs de triage mogelijk heeft uitgefilterd.

## Hoe het nu verder gaat

GitHub zegt dat het elk alumniproject AI-beveiligingsscans zal aanbieden waarvan de bevindingen eerst worden gecontroleerd voordat ze worden gemeld, en dat alumni GitHub Copilot Max krijgen. Het bedrijf zal de lessen uit het proefproject verwerken in zijn privémeldingen van kwetsbaarheden en beveiligingsadviezen. GitHub voegt daaraan toe dat beheerders ook CI-tests op privéforks moeten kunnen draaien en toegang nodig hebben tot modellen die geschikt zijn voor cybersecurity, zodat zij een proof of concept vóór en na een oplossing kunnen testen.

Ook het model achter de scans verandert. Op de dag van GitHubs bericht kondigde Microsoft MAI Cyber 2 Flash aan; het proefproject draaide nog op het eerdere model. Microsoft stelt dat het nieuwe model 92,3 procent scoort op de benchmark CyberGym-E2E, tegenover 91,5 procent voor GPT-6 Astra, tegen minder dan 2 procent van de kosten per taak, in tests die het bedrijf zelf uitvoerde en waarbij 92 van de 905 taken buiten beschouwing bleven. Het model wordt vanaf half december exclusief beschikbaar in de beveiligingsproducten van Microsoft, waaronder MDASH. Goedkoper scannen betekent meer bevindingen. Volgens de rekensom van het proefproject is voor elke extra honderd daarvan nog altijd een mens nodig om ze te lezen.

De opmerking van de beheerder van AutoGPT, die tegen het einde van GitHubs bericht staat, wijst in dezelfde richting: functies zijn steeds makkelijker uit te brengen, en in de toekomst zal het onderhouden van software “waarschijnlijk neerkomen op wie er genoeg om geeft om de beveiliging te beheren”. Voor het team van ImageMagick kwam het proefproject neer op 22 meldingen, één die bekend voorkwam, en een kwartier.

## Referenties

- Microsoft AI. (2026). *Introducing MAI Cyber 2 Flash: Leading security. Lower cost*. https://microsoft.ai/news/introducing-mai-cyber-2-flash/
- Stenberg, D. (2026). *The end of the curl bug-bounty*. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
- Wolf, A., & Cochran, G. (2026). *Maintainers don't need more AI bug reports. They need fixes.* GitHub Blog. https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

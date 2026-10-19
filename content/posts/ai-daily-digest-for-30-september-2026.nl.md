+++
title = "Dagelijks AI-overzicht – 30 september 2026"
slug = "dagelijks-ai-overzicht-30-september-2026"
description = "PostHog voegde redeneren toe aan een beslismodel, OpenAI breidde zijn ontwikkelaars- en bedrijfsaanbod uit en gemeenschappen bespraken privacy, infrastructuureconomie en open gewichten."
tags = ["community", "tools", "business", "research"]
date = 2026-09-30T04:01:34+02:00
draft = false
+++

PostHog bracht een beslismodel met redeneren uit, terwijl OpenAI zijn aanbod voor ontwikkelaars, prijsstelling en zakelijke distributie uitbreidde. Gemeenschapsdiscussies gingen over privacymetingen, datacentereconomie en mogelijke beperkingen op Chinese open gewichten.

» **Waarom dit ertoe doet:** De minder hoog gerangschikte releases en discussies van vandaag laten zien hoe AI-producten voor alledaags werk worden verpakt, en waar gebruikers nog onafhankelijk bewijs over prestaties, privacy en kosten missen.

## In het kort

- **PostHog voegt redeneren toe aan een beslismodel.** Jeeves is een met Jev compatibel model van 9 miljard parameters dat ja-neevragen, meerkeuzevragen en beoordelingsvragen beantwoordt na een optionele redeneerfase. PostHog publiceerde gewichten, code en data en meldt betere resultaten dan Jev op geselecteerde openbare tests; die resultaten blijven door de ontwikkelaar gemeten. Het is het volgen waard omdat het een begrensde beslisinterface combineert met een tragere redeneerroute, in plaats van elke classificatietaak naar een algemene chatbot te sturen. [Bron](https://github.com/PostHog/jeeves)

- **OpenAI voegt computerbediening toe aan zijn Agents API.** De bijgewerkte dienst laat door ontwikkelaars gebouwde agents met software werken en voegt multi-agentorkestratie, toolzoekfuncties, toolaanroepen en contextcompressie toe. OpenAI werkte ook met Amazon aan Bedrock Managed Agents die met AWS-middelen draaien. De release is belangrijk omdat hetzelfde agentpatroon nu op OpenAI's beheerde infrastructuur of binnen een AWS-omgeving kan worden ingezet. [Bron](https://openai.com/index/devday-2026-recap/)

- **OpenAI opent een abonnementsniveau van 500 dollar.** Pro 500 omvat het hoogste consumentengebruiksbudget van het bedrijf en toegang tot GPT-6 Astra Ultrafast, dat volgens OpenAI in Codex tot 300 tokens per seconde kan genereren. Die claim is een snelheidsplafond van de leverancier, en de waarde van het abonnement hangt van werklast en limieten af; de prijs maakt niettemin een nieuw premiumniveau voor schaarse inferentie zichtbaar. [Bron](https://openai.com/index/devday-2026-recap/)

- **OpenAI introduceert een marktplaats voor bedrijfssoftware.** In aanmerking komende klanten kunnen een deel van hun bestaande OpenAI-afnameverplichting inzetten voor goedgekeurde partnerproducten, terwijl contracten en facturering tussen klant en partner blijven. Het programma verdient aandacht omdat OpenAI toegezegde modeluitgaven als distributiekanaal voor externe software gebruikt. [Bron](https://help.openai.com/am-et/articles/20001553-openai-marketplace-for-enterprise-customers)

## Hacker News

- **Een studie naar chatbotprivacy wordt kritisch bekeken.** Onderzoekers van IMDEA Networks en partneruniversiteiten melden dat conversationele AI-diensten onder sommige geteste omstandigheden uit gesprekken afgeleid materiaal en blijvende identificatoren naar derden stuurden. De discussie gaat over noodzakelijke diensttelemetrie tegenover tracking. De studie is belangrijk omdat ze netwerkgedrag test in plaats van op de formulering van privacybeleid te vertrouwen. [Discussie](https://news.ycombinator.com/item?id=49890226) · [Publicatierecord](https://dspace.networks.imdea.org/handle/20.500.12761/2073)

- **Lezers toetsen Bains scenario van 6 biljoen dollar.** Een discussie onderzoekt Bains schatting dat de jaarlijkse AI-omzet in 2031 ongeveer 6 biljoen dollar zou moeten bereiken om de verwachte datacenteruitgaven te dragen. Het cijfer hangt af van aannames over kapitaalintensiteit en toekomstige investeringen en is dus een scenario, geen prognose. Het debat is nuttig omdat het die aannames zichtbaar maakt. [Discussie](https://news.ycombinator.com/item?id=49898952)

- **LiveNerf begint modelverandering te meten.** Het open project verzamelt dagelijks Claude Opus 5.5-resultaten via een vastgezette Claude Code-configuratie en vergelijkt latere vensters van tien dagen met een referentie uit de lanceringsperiode. De vooraf geregistreerde regel kan pas een eerste oordeel geven wanneer de vergelijkingsvensters compleet zijn, dus huidige dalingen zijn geen bewijs van een verslechtering. Het project verdient aandacht omdat het zijn opzet vóór het resultaat publiceert. [Discussie](https://news.ycombinator.com/item?id=49901736) · [Project](https://github.com/ninjahawk/livenerf)

## Reddit

- **Gebruikers bespreken een mogelijk verbod op Chinese open gewichten.** Een LocalLLaMA-discussie vraagt hoe ontwikkelaars op toekomstige beperkingen zouden reageren, maar verwijst naar geen nieuwe regel of officieel voorstel. De discussie is opinie en speculatie. Ze is het volgen waard als maatstaf voor ontwikkelaarszorgen na nieuwe bevindingen over cybercapaciteiten, niet als bewijs dat een verbod op handen is. [Discussie](https://old.reddit.com/r/LocalLLaMA/comments/1wtp9x4/are_you_worried_about_a_potential_ban_of_chinese/)

- **Een gemeenschapswrapper brengt DeepSeek Harness naar een app.** Gebruikers deelden een wrapper met desktopachtige interface voor de bestaande open-source-uitvoeringsomgeving voor agents. Het onderliggende DeepSeek-project dateert van vóór dit nieuwsvenster, en de wrapper is een gemeenschapsrelease in plaats van een nieuwe officiële omgeving. Hij is vooral relevant als bewijs dat lokale agentinfrastructuur toegankelijkere interfaces krijgt. [Discussie](https://old.reddit.com/r/LocalLLaMA/comments/1wtg1hs/deepseek_harness_app_is_out_now/)

## YouTube

- **Bill Gates pleit tegen zelfregulering van AI.** In een interview van 29 september met Ezra Klein bespreekt Gates cyberaanvallen, biologisch misbruik en arbeidsmarktverstoring en zegt hij dat overheden het toezicht niet alleen aan de sector moeten laten. Dit zijn beleidsoordelen van een technologie-investeerder en filantroop, geen nieuwe experimentele resultaten. Het interview is opmerkelijk omdat het claims over risico's van de geavanceerdste modellen koppelt aan een concreet reguleringsstandpunt. [Video](https://www.youtube.com/watch?v=A_156w0aYtU)

## Wat dit suggereert

Distributie wordt even belangrijk als modelcapaciteit. OpenAI koppelt agents aan cloudplatforms, premiumabonnementen en partneraankopen, terwijl open projecten buiten de grootste labs smallere modellen en meetinstrumenten bouwen. De bewijskwaliteit verschilt sterk: productbeschikbaarheid is openbaar, maar de meeste prestatieclaims komen nog van de bouwers.

## Wat komt er nu

LiveNerfs eerste vergelijkingsvenster volgt na de referentieperiode en twee perioden van tien dagen. Volgens OpenAI komen GPT-6.1 Sol Ultrafast en gezamenlijke dia's binnenkort, terwijl onafhankelijke gebruikers Jeeves nu aan de hand van de gepubliceerde data en code kunnen testen.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Jeeves-architectuur, releasebestanden en benchmarkresultaten | VOLGENS HET BEDRIJF | [PostHog-repository](https://github.com/PostHog/jeeves) | Code en data zijn openbaar; scores zijn niet onafhankelijk gereproduceerd |
| Computerbediening in Agents API en AWS-integratie | GEVERIFIEERD | [OpenAI DevDay-overzicht](https://openai.com/index/devday-2026-recap/) | Amazon wordt als tegenpartij genoemd; afzonderlijk AWS-materiaal was voor dit overzichtsitem niet vereist |
| Beschikbaarheid van Pro 500 en Ultrafast-claim | GEVERIFIEERD voor het abonnement; VOLGENS HET BEDRIJF voor de snelheid | [OpenAI DevDay-overzicht](https://openai.com/index/devday-2026-recap/) | [Business Insider](https://www.businessinsider.com/chatgpt-new-plan-pro-500-cost-compute-allowance-2026-9) bericht over het abonnement |
| Werking van de marktplaats | GEVERIFIEERD | [OpenAI Helpcentrum](https://help.openai.com/am-et/articles/20001553-openai-marketplace-for-enterprise-customers) | Nog geen onafhankelijke transactiegegevens |
| Privacybevindingen over gespreksagents | GEDEELTELIJK GEVERIFIEERD | [Institutioneel publicatierecord](https://dspace.networks.imdea.org/handle/20.500.12761/2073) | De HN-discussie reproduceert de metingen niet |
| Bains omzetscenario | GEDEELTELIJK GEVERIFIEERD | Bain-rapport besproken via actuele berichtgeving | [MarketWatch](https://www.marketwatch.com/story/two-thirds-of-the-revenue-needed-to-justify-the-ai-buildout-are-still-unaccounted-for-says-major-consulting-firm-8c55ccba) bericht over aannames en uitkomst |
| LiveNerf-opzet en onvoltooide status | GEVERIFIEERD | [Projectrepository](https://github.com/ninjahawk/livenerf) | De ruwe reeks wordt nog verzameld; geen verslechtering geclaimd |
| Discussie over een verbod op Chinese modellen | OPINIE | [Reddit-discussie](https://old.reddit.com/r/LocalLLaMA/comments/1wtp9x4/are_you_worried_about_a_potential_ban_of_chinese/) | Geen officieel voorstel gekoppeld |
| Discussie over de DeepSeek-wrapper | GEDEELTELIJK GEVERIFIEERD | [Reddit-discussie](https://old.reddit.com/r/LocalLLaMA/comments/1wtg1hs/deepseek_harness_app_is_out_now/) | De bestaande officiële uitvoeringsomgeving dateert van vóór het venster |
| Gates-interview en beleidsstandpunt | OPINIE | [YouTube-interview](https://www.youtube.com/watch?v=A_156w0aYtU) | Publicatie op 29 september onafhankelijk geïndexeerd |

+++
title = "Dezelfde aandachtskoppen veranderen van rol met de taak"
slug = "dezelfde-aandachtskoppen-veranderen-van-rol-met-taak"
description = "Een nieuwe preprint vindt dat een taalmodel de invloed van zijn aandachtskoppen reorganiseert wanneer de gevraagde taak verandert, ook als de promptfeiten gelijk blijven. Causale interventies suggereren dat taakcontext mede bepaalt wat een component doet, wat één permanent label bemoeilijkt."
tags = ["research", "models"]
date = 2026-10-13T04:05:13+02:00
draft = false
+++

Stel een ingenieur bij een monitor voor, die lijnen tussen honderden kleine vakjes volgt. Eén krijgt een net label: “landen opzoeken”. Dan verandert de instructie, blijven de invoerfeiten gelijk en lijkt hetzelfde vakje met iets anders te helpen. Deze ingenieur is verzonnen, als illustratie van het praktische probleem centraal in een nieuwe studie: een transformercomponent heeft mogelijk niet één stabiele, benoembare taak.

## Een kaart die met de vraag verandert

Sovesh Mohapatra en Dani S. Bassett, onderzoekers verbonden aan de University of Pennsylvania en Yale University, testten hoe taakcontext de functionele organisatie van aandachtskoppen in taalmodellen verandert. Hun preprint, ingediend op 12 oktober 2026, onderzoekt vijf open modellen van 1,5 miljard tot 14 miljard parameters. Hij heeft geen peerreview doorlopen.

De studie begint met een bewuste scheiding. Een prompt bevat een kleine graaf gecodeerd als feitelijke uitspraken, terwijl een instructie het model één van verschillende vragen over die graaf laat beantwoorden. Over condities heen blijven de graaffeiten gelijk. Alleen de taak verandert. Zo kunnen onderzoekers vragen of het model dezelfde interne route over identieke informatie aflegt of de route volgens de opdracht reorganiseert.

Ze behandelen elke aandachtskop als knoop in een invloedsnetwerk. Een verbinding registreert hoe een wijziging van de uitvoer van één kop een andere kop later in het model beïnvloedt. De kaart is functioneel, niet anatomisch: de architectuur blijft gelijk, maar het gemeten invloedspatroon kan per taak verschillen.

Dat gebeurt. Mohapatra en Bassett melden dat de netwerken bij de geteste modellen per taak uiteenlopen. Koppen met invloedrijke posities in één taak kunnen in een andere minder centraal zijn. De bevinding verschuift de interpretatievraag van “Wat representeert deze kop?” naar “Welke rol speelt deze kop in deze taak, binnen dit netwerk?”

Dat onderscheid is relevant omdat veel mechanistische interpreteerbaarheid naar herbruikbare interne onderdelen heeft gezocht. Eric Todd en collega's identificeerden eerder kleine sets aandachtskoppen met compacte “functievectoren” uit voorbeelden binnen de context. Roee Hendel, Mor Geva en Amir Globerson lieten eveneens zien dat leren binnen de context een taakvector kan vormen waarmee een model een gedemonstreerde bewerking uitvoert, zelfs zonder demonstraties tijdens inferentie. Die resultaten ondersteunen dat een taak een causale interne representatie kan hebben. Het nieuwe artikel vraagt hoe zo'n representatie de relaties tussen componenten verandert.

## De instructie kan het mechanisme verplaatsen

Alleen correlatie zou een duidelijke twijfel laten bestaan. Een andere taak levert een ander antwoord op, dus een andere invloedskaart kan de verandering slechts begeleiden. Daarom interveniëren de auteurs op modelactivaties.

Ze construeren een activatiebewerking in een vroege laag om het model van de representatie van één taak naar een andere te bewegen, zonder de geschreven prompt te veranderen. In experimenten met Gemma- en Qwen-modellen kan die bewerking wisselen welke taak het model uitvoert. Het artikel meldt dat elk van 512 prompts waarvoor de taken tegengestelde antwoorden vereisten naar het doelantwoord wisselde, terwijl alle 512 prompts waarvoor beide taken hetzelfde antwoord vereisten dat behielden.

De interventie laat ook de latere invloedskaart op de doeltaak lijken. De auteurs meten dat met een fout tussen netwerkresponspatronen. Hun taakwisselbewerking verminderde die fout met 53,6 procent in Gemma en 5 procent in Qwen. Het grootteverschil waarschuwt tegen een uniforme uitleg over modelfamilies, maar beide wijzen in dezelfde causale richting: veranderde interne taakcontext kan latere berekening bijsturen.

Dit lijkt op activatiesturing, een bredere familie methoden die modelgedrag verandert door een richting aan verborgen activaties toe te voegen. Alexander Matt Turner en collega's lieten zien dat activatietoevoegingen uit contrasterende prompts hoge eigenschappen van gegenereerde tekst zonder verdere training konden veranderen. De nieuwe studie gebruikt zo'n bewerking als experimentele probe. Het doel is geen gedragscontrole uitbrengen, maar testen of een veranderde taakrepresentatie voorafgaat aan een veranderd invloedsnetwerk van aandachtskoppen.

De interventie is beperkt. Ze toont niet aan dat onderzoekers een willekeurige taak kunnen kiezen, elk model betrouwbaar kunnen bewerken of een volledig programma uit een koppengraaf kunnen lezen. De taken zijn gecontroleerd, de modellen zijn middelgrote systemen met open gewichten en de causale tests richten zich op een specifiek intern contrast. De sterkste claim betreft contextafhankelijkheid binnen die opzet.

## Van gelabelde onderdelen naar ingeschakelde teams

Netwerkneurowetenschap levert de organiserende metafoor. Daar wordt de bijdrage van een hersengebied vaak bestudeerd via zijn plaats in een veranderend netwerk in plaats van één geïsoleerde functie. Bassett en Olaf Sporns beschreven de aanpak als een poging elementen over schalen heen te verbinden en te verklaren hoe interacties gedrag opleveren. Mohapatra en Bassett brengen dat perspectief naar transformeranalyse.

De analogie heeft grenzen. Een aandachtskop is een ontworpen wiskundige component, geen biologisch gebied, en een transformer erft de anatomie of geschiedenis van het brein niet. De nuttige overdracht is methodologisch: observeer een onderdeel samen met het invloedspatroon dat het inschakelt.

Voor modelauditors maakt dit een permanent label minder geruststellend. Een kop die onder één prompt gedrag ondersteunt kan anders deelnemen wanneer instructies, voorbeelden of doelen veranderen. Verwijderen of onderdrukken kan effecten hebben die van taakcontext afhangen. Omgekeerd kan een veiligheidsrelevant proces over verschillende configuraties verdeeld zijn, zelfs bij identieke onderliggende parameters.

Het resultaat suggereert ook een praktische norm voor toekomstige interpretatieclaims. Een voorgesteld circuit moet worden getest over taken die dezelfde informatie hergebruiken, en een schijnbare rol moet causale interventie doorstaan, niet alleen visuele inspectie. Als het circuit verandert, is die verandering deel van het te verklaren mechanisme.

Er blijft werk. Het artikel bestudeert een beperkte familie graaftaken en een kleine set open modellen. Het stelt niet vast hoe zulke responsnetwerken zich in zeer grote gesloten systemen, lange gesprekken of ruisgevoelige echte instructies gedragen. Het beslist ook niet of het gemeten netwerk alle berekeningen relevant voor een antwoord omvat. De auteurs bieden een raamwerk voor herconfiguratieonderzoek, geen voltooide atlas.

Terug naar de verzonnen ingenieur bij de monitor. Het label op het vakje blijft nuttig, maar vereist nu een conditie: nuttig voor deze bewerking, onder deze instructie, in dit gezelschap van andere koppen. Het blijvende object is niet meer het geïsoleerde onderdeel. Het is het patroon dat de taak inschakelt.

## Referenties

- Bassett, D. S., & Sporns, O. (2017). *Network neuroscience*. https://doi.org/10.1038/nn.4502
- Hendel, R., Geva, M., & Globerson, A. (2023). *In-Context Learning Creates Task Vectors*. https://aclanthology.org/2023.findings-emnlp.624/
- Mohapatra, S., & Bassett, D. S. (2026). *Task Context Dynamically Reconfigures Attention Head Networks in Large Language Models*. https://arxiv.org/abs/2610.13895
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://openreview.net/forum?id=AwyxtyMwaG
- Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2024). *Activation Addition: Steering Language Models Without Optimization*. https://arxiv.org/abs/2308.10248

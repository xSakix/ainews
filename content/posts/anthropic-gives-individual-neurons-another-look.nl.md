+++
title = "Anthropic bekijkt opnieuw wat afzonderlijke neuronen vertellen"
slug = "anthropic-bekijkt-wat-afzonderlijke-neuronen-vertellen"
description = "Afzonderlijke neuronen zijn volgens onderzoekers van Anthropic beter te duiden dan eerder werk deed vermoeden. In open modellen en gecontroleerde proeven gebruiken ze neuronen om zonder trainingsvoorbeelden concepten te detecteren, gedrag te sturen en verborgen gedrag op te sporen."
tags = ["research", "safety", "models"]
date = 2026-11-25T04:03:43+01:00
draft = false
+++

Een onderzoeker opent twee kopieën van een taalmodel. De ene is het vertrouwde basismodel. De andere heeft een kleine adapter met een onbekend doel. In plaats van het aangepaste model met vragen te laten verraden wat het doet, loopt de onderzoeker een lijst neuronen langs. Welke gedragen zich anders dan voorheen?

*De scènes aan het begin en het einde van dit artikel zijn illustraties; de personen erin zijn verzonnen.*

Dat is de praktische gedachte achter twee rapporten van Anthropic-onderzoekers Jasmine Shone en Lisa Dunlap. Afzonderlijke neuronen golden lange tijd als een onbetrouwbare basis om betekenis aan modelprocessen toe te kennen. Volgens de onderzoekers kunnen ze wel degelijk laten zien wat finetuning aan een model heeft toegevoegd. In een blinde test met 68 LoRA-adapters vertoonden 58 adapters een ingebouwd verborgen gedrag. Hun auditsysteem wist dat gedrag met behulp van neuronen bij 75 procent van die 58 te benoemen. Alleen op basis van de uitvoer van het model lukte dat bij 40 procent.

Het onderzoek heropent een oude vraag over de interpreteerbaarheid van modellen. Ooit hoopten onderzoekers de concepten van een model te achterhalen door neuronen afzonderlijk te bekijken. Maar een neuron kan op meerdere betekenissen reageren, representaties veranderen van laag tot laag en bij het ophalen van feiten zijn meerdere paden betrokken. Die bevindingen brachten veel onderzoekers ertoe zich te richten op aangeleerde kenmerken, diagnostische meetinstrumenten en richtingen in de residuele informatiestroom. Shone en Dunlap stellen niet dat de moeilijkheden zijn verdwenen. Ze kijken naar een ander onderdeel van het proces.

## Wat een neuron schrijft

Bij een neuron in een meerlaags perceptron zijn hier twee eigenschappen van belang. De activatie bepaalt hoe sterk het neuron in een bepaalde context reageert. De uitvoervector bepaalt welke richting het aan de residuele stroom toevoegt. Die vector ligt vast, terwijl de activatie positief of negatief kan zijn.

De onderzoekers beschrijven een neuron daarom als een stuurvector waarvan de werking afhangt van de context. Eerder onderzoek draaide vaak om de vraag welke tekst een neuron activeert. Hun methode vraagt ook wat het neuron vervolgens schrijft. Met een methode die J-lens heet, lezen ze uit welke tokens in de woordenschat waarschijnlijker worden door een bepaalde uitvoervector. Die gegevens leggen ze naast de contexten waarin het neuron het sterkst reageert.

Een neuron in Llama 3.1 8B Instruct illustreert het verschil. Het bevordert het token “John” bij prompts over John the Ripper én bij prompts over de schrijver van het vierde evangelie. Wie alleen beschrijft wat het neuron activeert, mist die gemeenschappelijke uitvoer. Ook het teken doet ertoe: dezelfde vector kan bij positieve en negatieve activatie verschillende betekenissen dragen.

Het team toetste zijn interpretaties door in het model in te grijpen. De onderzoekers schakelden activaties van neuronen uit, voegden uitvoervectoren aan andere lagen toe en stuurden daarmee het gedrag. In hun steekproef droeg een neuron in hooguit ongeveer 1 procent van de gevallen tegelijk twee losstaande concepten bij aan de residuele stroom. Ook hielden uitvoervectoren in de meeste lagen ongeveer dezelfde betekenis.

Een neuron kan dus nog steeds op allerlei soorten tekst reageren en in veel contexten actief worden. De uitspraak van de onderzoekers is specifieker en gaat over de bijdrage aan de volgende berekening van het model. Daardoor blijft het bewijs voor complexe activatiepatronen overeind, terwijl de richting die het neuron schrijft volgens de auteurs wel te duiden is.

## Ook verspreid opgeslagen feiten zijn te duiden

Een tweede bezwaar betreft het ophalen van feiten. Door één neuron te wijzigen verdwijnt zelden één feit, omdat het model kennis langs vele paden opslaat. De studie van Anthropic bevestigt die spreiding. Wanneer de onderzoekers voldoende neuronen veranderden om een model een feitelijke vraag verkeerd te laten beantwoorden, vertegenwoordigden de betrokken neuronen meestal concepten die met dat feit samenhingen.

Dat de kennis verspreid zat, maakte de paden dus niet willekeurig. Meerdere afzonderlijk te duiden bijdragen konden samen één antwoord ondersteunen. Dat maakt verschil bij de keuze van analysegereedschap. Eenvoudige eenheden lijken vaak te grof, terwijl een aangeleerd woordenboek van kenmerken extra training vergt en de onderzoeker voor nieuwe keuzes stelt.

Een veelgebruikte oplossing is de sparse autoencoder. Die leert uit modelactivaties een grotere verzameling kenmerken waarvan er telkens maar weinig actief zijn. Het doel is om concepten te scheiden die gewone neuronen combineren. Anthropic gebruikte zulke kenmerken eerder zelf om activaties in Claude in kaart te brengen. Shone en Dunlap schrijven sparse autoencoders niet af. Ze vergelijken of de neuronen die het model al heeft voor een deel van dezelfde toepassingen geschikt zijn, zonder eerst een nieuwe representatie te trainen.

## Van beschrijving naar veiligheidstoepassing

Het tweede rapport onderzoekt drie toepassingen: detectie, sturing en audits. Voor detectie selecteerde het team neuronen op basis van voorbeelden van hun activatie, automatisch gegenereerde beschrijvingen en uitgelezen uitvoer. De resulterende neurondetectoren presteerden op de meeste evaluatiesets beter dan zoeken op tekst. Op vier van de zestien sets evenaarden ze lineaire detectoren die op 400 gelabelde voorbeelden waren getraind. Bij het terugvinden van schadelijke inhoud versloegen ze tekstzoeken op elf van de zeventien onderwerpen.

Getrainde classificatiemodellen zijn daarmee niet over de hele linie ingehaald. Volgens het rapport doen getrainde detectoren het meestal beter. De vergelijking is vooral van belang wanneer er nog geen voorbeelden zijn: de neuronenmethode heeft voor het gezochte concept geen gelabelde trainingsset nodig. Een onderzoeker kan daardoor mogelijk met een audit beginnen voordat er voorbeelden zijn verzameld.

Voor de sturing gebruikten de onderzoekers de uitvoervectoren van neuronen om bij een chatbot een bepaald gedrag op te roepen. Ze kozen neuronen op grond van hun uitgelezen uitvoer en de beschrijving van hun activatie. In 21 procent van de antwoorden trad het beoogde gedrag op. Getrainde stuurvectoren haalden hetzelfde percentage. In absolute zin is het resultaat bescheiden, maar de proef toetst of de vaste uitvoer van een neuron het gedrag daadwerkelijk beïnvloedt en meer doet dan met een concept samenhangen.

In het auditexperiment vergeleek het team vervolgens een bijgetraind model met het basismodel. De onderzoekers bestudeerden proefmodellen voor achterdeurtjes, spontaan ontstaan gedrag dat afwijkt van de beoogde doelen en subliminaal leren. Finetuning leidde doorgaans tot sterkere activatie van neuronen waarvan de uitvoervectoren al naar het nieuwe gedrag wezen. De adapter benutte vaak bestaande richtingen in het basismodel en hoefde daarvoor geen volledig nieuwe interne woordenschat te vormen.

Dat patroon gaf het auditsysteem houvast. Het op Claude gebaseerde systeem stuurde het model langs de richtingen van de aanpassingen en las neuronen uit die daarmee waren uitgelijnd. Zo wist het driekwart van de verborgen gedragingen te benoemen. Wie alleen steekproeven van de modeluitvoer onderzocht, miste de meeste.

## Afleren kan een antwoord aan het zicht onttrekken

De auteurs pasten hun methode ook toe op 23 openbare modelversies die waren getraind om gevaarlijke kennis over cyberbeveiliging uit WMDP te vergeten. Die benchmark bevat 1.987 meerkeuzevragen waarvan de antwoorden cyberaanvallen zouden kunnen ondersteunen. Bij afleren is het de bedoeling de toegang tot de onderliggende informatie weg te nemen en vaardigheden die daar los van staan te behouden.

Bij veertien van de 23 modelversies kwam het juiste antwoord in een invultoets nog steeds bovenaan bij de meeste vragen die het basismodel goed had beantwoord. De zichtbare score op meerkeuzevragen kon dus dalen, terwijl een andere uitleesmethode het antwoord nog aan het licht bracht. Volgens de onderzoekers wijst dit erop dat veel methoden het model een manier van antwoorden aanleerden die de kennis verborg zonder haar te verwijderen.

De reikwijdte van dat resultaat is beperkt. WMDP is een benchmark en een invultoets is één manier om te meten welke kennis is achtergebleven. Als een model een token juist rangschikt, betekent dat nog niet dat het alle bijbehorende praktische vaardigheden heeft behouden. De proef laat wel zien waarom één gedragsscore niet kan aantonen dat informatie verdwenen is.

## Een vertrekpunt voor verder onderzoek

De twee rapporten gaan voornamelijk over modellen met open gewichten, waarvan de neuronen en de bijgetrainde versies rechtstreeks te vergelijken zijn. Het verborgen gedrag is bestudeerd in gecontroleerde proefmodellen. In de praktijk spelen grotere modellen, gereedschappen, systeemprompts en veiligheidsmaatregelen samen. Daardoor kunnen dezelfde signalen minder goed zichtbaar zijn.

Hoe een neuron wordt beschreven, hangt ook af van de gekozen voorbeelden en uitleesmethode. Een interpreteerbare uitvoervector garandeert nog niet dat een onderzoeker het juiste neuron vindt. Detectoren die zonder trainingsvoorbeelden werken, blijven meestal achter bij detectoren die onder toezicht zijn getraind. De auteurs presenteren neuronen als bruikbare eenheden voor analyse en doen geen aanspraak op een volledige verklaring van cognitieve processen.

De praktische winst zit in een goedkopere eerste verkenning. Het model bevat de vaste uitvoervector al. De onderzoeker kan die uitlezen, verplaatsen, onderdrukken en vergelijken, nog voordat er een kenmerkenwoordenboek is getraind of een gelabelde dataset is samengesteld.

Terug bij de twee modelkopieën komt de onderzoeker aan bij de neuronen die na finetuning sterker reageerden. Hun uitvoervectoren wezen al in de richting van het verborgen gedrag voordat de adapter bestond. Wat veranderde, was vooral het moment waarop het model een vertrouwde richting insloeg. Daar hoefde geen nieuw concept voor te ontstaan.

## Referenties

- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections” — https://alignment.anthropic.com/2026/neuron-basis-theory/
- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 2: Using Neurons For Safety Applications” — https://alignment.anthropic.com/2026/neuron-basis-applications/
- Trenton Bricken et al., “Towards Monosemanticity: Decomposing Language Models With Dictionary Learning” — https://transformer-circuits.pub/2023/monosemantic-features/index.html
- Nicholas Carlini et al., “WMDP: Measuring and Reducing Malicious Use With Unlearning” — https://arxiv.org/abs/2403.03218

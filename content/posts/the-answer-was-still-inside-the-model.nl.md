+++
title = "Het antwoord zat nog in het model"
slug = "antwoord-zat-nog-in-het-model"
description = "Een studie van 15 taalmodellen vindt dat veel werkgeheugenfouten optreden nadat het juiste item is geselecteerd. De modellen behouden decodeerbare informatie, maar slagen er niet in die te melden."
tags = ["research", "models"]
date = 2026-10-16T04:07:00+02:00
draft = false
+++

Een model krijgt een korte lijst symbolen te zien en wordt vervolgens afgeleid door een tweede lijst voordat het het oorspronkelijke doelitem moet noemen. Het antwoordt met het afleidende item. De voor de hand liggende diagnose is dat het eerste symbool verdwenen is. In deze illustratieve scène kan een interne probe het doelitem echter nog vrijwel perfect lezen. Het antwoord is niet gewist. Er ging iets mis tussen het vasthouden en het uitspreken ervan.

Dat onderscheid staat centraal in een nieuwe preprint over werkgeheugen in taalmodellen. De auteurs testten 15 modellen met 70 miljoen tot 14 miljard parameters op taken die interferentie moesten veroorzaken. Ze vonden dat aandachtskoppen vaak het juiste doelitem selecteerden, ook wanneer het uiteindelijke antwoord fout was. Eenvoudige probes konden bij veel fouten het doelitem met vrijwel perfecte nauwkeurigheid uit verborgen toestanden decoderen.

Het resultaat trekt een vertrouwde vereenvoudiging bij modelevaluatie in twijfel: een verkeerde uitvoer behandelen als bewijs dat de onderliggende informatie ontbreekt. Het artikel onderscheidt juist drie bewerkingen die één nauwkeurigheidsscore samenvoegt: een relevant item selecteren, de identiteit ervan bewaren en het als antwoord uitlezen.

## Een gecontroleerd geheugenprobleem

Werkgeheugen is geen langetermijnopslag. Het is het tijdelijke vermogen om informatie in bruikbare toestand te houden terwijl ander materiaal om aandacht concurreert. Experimenten met mensen laten vaak zien dat een item gedeeltelijk beschikbaar blijft, ook wanneer een deelnemer het verkeerde item meldt. Vergelijkbare interferentie kan twee herinneringen moeilijk te onderscheiden maken zonder een van beide te vernietigen.

De onderzoekers maakten taken waarin ze het doelitem, de concurrerende items en hun posities konden variëren. Daarna keken ze in de modellen op de punten waar het doelitem moest worden geselecteerd en doorgegeven. De modellen omvatten verschillende schalen en families. Dat doet ertoe omdat een patroon in één checkpoint een toevalligheid van de architectuur kan zijn in plaats van een algemeen mechanisme.

Bij correcte proeven klopte het verwachte verhaal: aandacht richtte zich op het doelitem en de laatste lagen produceerden het juiste token. Bij veel onjuiste proeven klopte de eerste helft nog steeds. Aandachtskoppen die het doelitem selecteren, richtten zich op de juiste positie. Probes van verborgen toestanden behielden genoeg informatie om het doelitem te identificeren. Toch weerspiegelde de uitvoer een concurrent.

Een probe levert bewijs van decodeerbaarheid, niet van gebruik. Een achteraf getrainde classificator kan informatie extraheren waar de eigen berekening van het model niet bij kan. Daarom gingen de auteurs verder dan het lezen van toestanden en grepen ze erop in.

## De concurrenten verzwakken

De belangrijkste causale test onderdrukte representaties van de identiteit van niet-doelitems. Die interventie verbeterde de gevoeligheid, gemeten als d-prime, in de richting die een interferentieverklaring voorspelde. Verzwakking van de concurrenten maakte het opgeslagen doelitem gemakkelijker te melden voor het model.

Dit betekent niet dat elke geheugenfout een uitleesfout is. Modellen kunnen een item niet coderen, het verliezen of de verkeerde locatie selecteren. De claim van het artikel is beperkter: een betekenisvol deel van de fouten treedt op terwijl doelinformatie intern beschikbaar blijft, en verwarring tussen vergelijkbare representaties kan het uiteindelijke antwoord blokkeren.

Het onderscheid doet ertoe voor de techniek. Meer context toevoegen of het doelitem herhalen pakt een opslagprobleem aan. Dat helpt mogelijk weinig wanneer het model het doelitem al vasthoudt maar niet van concurrerende inhoud kan scheiden. Een systeem met dat tweede probleem heeft mogelijk andere prompts, tussenstructuur of architectuurwijzigingen nodig die de identiteit bij het uitlezen aanscherpen.

Het doet ook ertoe voor interpretatie. Transformeraandacht, geïntroduceerd als mechanisme om posities in een reeks te verbinden, wordt vaak geïnspecteerd alsof aandacht voor het juiste token vaststelt wat het model weet. Hier kan aandacht naar het doelitem wijzen en toch geen correcte uitvoer opleveren. Omgekeerd betekent een fout antwoord niet dat de aandacht het doel miste.

## Een gelijkenis met mensen met grenzen

De auteurs beschrijven het interferentiepatroon als mensachtig, maar de vergelijking is functioneel in plaats van biologisch. Een transformer heeft geen menselijk geheugensysteem nodig om dezelfde gedragsmatige splitsing tussen beschikbaarheid en rapportage te tonen. Vergelijkbare fouten kunnen uit heel verschillende mechanismen ontstaan.

Schaal lost het probleem ook niet op. Tests met modellen tot 14 miljard parameters laten zien dat het effect verder reikt dan kleine experimentele netwerken, maar stellen niet hetzelfde resultaat vast in toonaangevende systemen met veel meer parameters of bedrijfseigen natraining. De taken zijn bewust gecontroleerd. Echte gesprekken mengen ophalen van informatie, instructies volgen, plannen en genereren op manieren die het moeilijker maken de bron van één fout te isoleren.

Toch zijn gecontroleerde taken precies het doel. Ze laten onderzoekers één concurrent veranderen, één representatie waarnemen en één interventie testen. Het artikel biedt een methode om na een modelfout een betere vraag te stellen: is de informatie nooit gecodeerd, is ze verloren gegaan, of was ze aanwezig maar ontoegankelijk voor het uitvoerproces?

Terug naar de illustratieve symbolentaak. Het model geeft het verkeerde item en een beoordelaar noteert een fout. Dat oordeel klopt aan de productgrens. Intern kan het systeem echter het grootste deel van het werk hebben gedaan. De volgende vooruitgang komt mogelijk niet van een groter geheugen. Ze kan komen van het leren lezen van wat het al heeft bewaard.

## Referenties

- Vaswani, A., et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- *Working Memory Readout Bottlenecks in Language Models* (2026). https://arxiv.org/abs/2610.21176

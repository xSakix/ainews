+++
title = "Een taalmodel herschreef zijn eigen gewichten en werd nauwkeuriger"
slug = "taalmodel-herschreef-eigen-gewichten-en-werd-nauwkeuriger"
description = "Onderzoekers gaven een open model met 27 miljard parameters toegang tot zijn gewichten, beoordeelde antwoorden en een manier om wijzigingen te testen, maar blokkeerden gradiënten en optimalisatiealgoritmen. Het model won 6,6 procentpunt aan nauwkeurigheid op apart gehouden opgaven en herstelde een beschadigde kopie van zichzelf, terwijl kleinere modellen daar onder dezelfde omstandigheden niet in slaagden."
tags = ["models", "research"]
date = 2026-11-21T04:12:00+01:00
draft = false
+++

Een model zat voor een Python-sessie waarin het zijn eigen gewichten kon bekijken. Het kon verborgen toestanden onderzoeken, geselecteerde matrices wijzigen en een kopie van zichzelf een volgende opgave laten oplossen. Een gradiënt berekenen kon het niet. Het moest het doen met twintig voorwaartse berekeningen en een vaste tijdslimiet.

*De scènes aan het begin en het einde van dit artikel zijn illustraties; de personen erin zijn verzonnen.*

Jiajun Fan en tien medeauteurs plaatsten vier open modellen uit dezelfde familie in die omgeving. Het model met 2 miljard parameters veranderde niets aan zichzelf. De modellen met 4 en 9 miljard parameters probeerden willekeurige wijzigingen en gingen slechter presteren. Het model met 27 miljard parameters mat in welke richtingen zijn verborgen toestanden verschilden, bracht langs die richtingen wijzigingen aan en behield ze alleen als gepaarde tests ze ondersteunden. Door één wijziging steeg de nauwkeurigheid op 490 apart gehouden opgaven met 6,6 procentpunt.

De auteurs noemen hun methode zelfherschrijving. Hun centrale stelling is beperkt maar verstrekkend: een model dat al in gebruik is, kan zijn eigen gewichten blijvend verbeteren door uitsluitend met voorwaartse berekeningen te redeneren. De studie is een preprint. Volgens de auteurs is dit de eerste demonstratie in haar soort.

## Een model met toegang tot zichzelf

Bij training staat het systeem dat naar betere gewichten zoekt gewoonlijk los van het model dat ze later gebruikt. Een optimalisatiealgoritme berekent gradiënten van een verliesfunctie, ingenieurs kiezen de gegevens en instellingen en een computercluster schrijft het resultaat naar een nieuw modelbestand. Pas na afloop begint de inferentie.

Fan en zijn collega’s namen het optimalisatiealgoritme weg, maar gaven het model gereedschap. Het kreeg beoordeelde antwoorden op oefenopgaven, toegang tot zijn gewichtstensoren en een Python-sessie die tussen gespreksronden haar toestand behield. Het kon de oorspronkelijke en de gewijzigde versie dezelfde opgaven laten maken met dezelfde startwaarden voor de toevalsgenerator. Ook kon het de verborgen toestanden uitlezen die het model bij zelfgekozen teksten produceerde.

De omgeving handhaafde de grenzen. Gradiënten waren uitgeschakeld. Aanroepen van optimalisatiealgoritmen, netwerken, nieuwe processen en functies om modellen te laden werden geweigerd. Het model mocht de invoerinbedding, de laatste normalisatiestap en de uitvoerlaag niet wijzigen. Per sessie kon het hoogstens twintig voorwaartse berekeningen uitvoeren en 200 keer code draaien.

Een gepaarde test vergeleek de antwoorden per opgave. Dat was van belang omdat een kleine verbetering van de totaalscore anders aan steekproefruis kon liggen. Het testsysteem meldde hoeveel antwoorden van fout naar goed veranderden, hoeveel de omgekeerde weg volgden en hoe vaak elk van beide versies zijn budget van 16.384 tokens uitputte.

Bij het strengere protocol testte het systeem een voorgestelde wijziging ook eenmalig op apart gehouden oefenopgaven die het model niet kon inzien. Daarna diende het model de wijziging in of trok het die in. In vijf van de eerste acht sessies trok het model de wijziging in. De geaccepteerde wijzigingen verlaagden nooit de nauwkeurigheid van het model dat in gebruik bleef.

## Wat het grootste model veranderde

Het model met 27 miljard parameters doorzocht niet elke parameter. Het vond in zijn verborgen toestanden richtingen die samenhingen met fouten. Vervolgens verkleinde het de bijdrage van geselecteerde uitvoermatrices in die richtingen. De bewerking leek op het aftrekken van een component van rang één van een matrix.

Die ingreep verminderde een zichtbare fout: sommige antwoorden herhaalden een zin tot de tokenlimiet was bereikt. Bij één apart gehouden opgave herhaalde het basismodel dezelfde zin 549 keer en gaf het geen antwoord. De gewijzigde versie rondde de opgave af.

Over de vaste evaluatie leverde de succesvolste wijziging de winst van 6,6 procentpunt op. In twee sessies traden verbeteringen op waarvoor de gepaarde toets van de auteurs een kans van minder dan één op 100.000 gaf. Na de achtste sessie bedroeg de nauwkeurigheid 63,8 procent.

Elke sessie begon het onderzoek met de oorspronkelijke gewichten, maar na acceptatie verving de gewijzigde versie het model dat in gebruik was. De reeks bouwde dus voort op beslissingen zonder elk voorstel blind op het vorige te stapelen. Volgens de auteurs steeg de nauwkeurigheid of bleef ze gelijk in alle acht sessies.

De verbetering vergde bij latere antwoorden geen extra rekenwerk. Zodra de wijziging was weggeschreven, maakte ze deel uit van het modelbestand. Dat onderscheidt de methode van opschalen tijdens de inferentie, waarbij een beter antwoord telkens extra tokens of steekproeven kost.

## Herstel zonder het origineel

Het team veroorzaakte ook een defect waarvan het de oorzaak kende. In één uitvoermatrix van een meerlaags perceptron overschreef het acht opeenvolgende rijen met ruis, geschaald tot 200 keer de standaardafwijking van de matrix. Het beschadigde model kreeg bijna geen enkele opgave meer opgelost.

Het model dat de reparatie uitvoerde was zelf onbeschadigd, maar kon alleen de berekeningen en gewichten van de beschadigde kopie bekijken. Het hoorde dat sommige waarden onjuist waren, maar kreeg niet te horen waar de schade zat of hoe ze was ontstaan. Het las op geen enkel moment de bijbehorende onbeschadigde waarden uit.

Het model met 27 miljard parameters vond de defecte matrix en schreef zelf vervangende waarden. Een reparatie die het bij wiskundeopgaven in tekstvorm vond, werkte ook bij zes beeldbenchmarks die tijdens de sessie nooit waren gebruikt. De gerepareerde kopie haalde over de benchmarks samen 83 procent van de nauwkeurigheid van het basismodel. Op ScreenSpot-v2 steeg de score van nul naar 89 procent, tegenover 93 procent voor het onbeschadigde model.

Deze proef ondervangt een voor de hand liggende verklaring van het hoofdresultaat. Een model zou een beperkte wijziging kunnen aanbrengen die alleen werkt door eigenaardigheden van de oefenopgaven. Dat het een doelbewust beschadigd onderdeel kon repareren en vervolgens ook op beeldtaken weer beter presteerde, laat zien dat het een algemenere functie kan herkennen en gedeeltelijk herstellen.

Daaruit volgt niet dat een model willekeurige schade kan herstellen. De onderzoekers beschadigden één kunstmatig samengesteld blok en experimenteerden met vier groottes uit één modelfamilie, Qwen3.5. Het model beschikte over beoordeelde oefenantwoorden en ongebruikelijk directe toegang tot interne tensoren. Gewone onlineassistenten hebben geen van die mogelijkheden.

## Waar de grens ligt

De kleinere modellen tonen de huidige beperking. Het model met 2 miljard parameters behandelde zijn gewichten niet als iets waaraan het zinvolle wijzigingen kon aanbrengen. De versies met 4 en 9 miljard parameters voegden willekeurige ruis toe. Als een test wees op verslechtering, gokten ze op een andere ingreep.

Het model met 27 miljard parameters doorliep een langere reeks stappen. Het stelde een symptoom vast, onderzocht de activaties, formuleerde een hypothese, wijzigde een matrix, voerde een gepaarde test uit en stelde zijn plan bij als het resultaat negatief was. Volgens de auteurs ontstaat dit vermogen bij grotere modellen. Met vier groottes uit één familie valt echter geen algemene drempel vast te stellen.

Een verwante preprint uit dezelfde week onderzocht een andere opzet. Een extern taalmodel koos daarin gewichtsaanpassingen voor kleinere doelmodellen. Op SmolLM2 en Qwen2.5 evenaarde dit systeem een black-boxzoekmethode en op Pythia presteerde het beter. In Fans onderzoek vallen degene die de wijziging uitvoert en het model dat de wijziging ondergaat samen. Juist dat ondersteunt de verdergaande stelling van de auteurs.

De auteurs leggen een verband met recursieve zelfverbetering. Hun experiment is nog ver verwijderd van een autonome cyclus. Mensen leverden de taak, het signaal dat iets fout ging, de hulpmiddelen, de beperkingen aan wijzigingen en de acceptatietest. De sessies duurden uren op één GPU. Het sterkste bewijs betreft een afgebakende verzameling redeneeropgaven en één kunstmatig veroorzaakt defect.

Juist door die grenzen is het resultaat controleerbaar. Elke geaccepteerde wijziging doorstond een gepaarde vergelijking, alle apart gehouden opgaven bleven buiten de bewerkingssessie en ook de mislukkingen van de kleinere modellen bleven in het verslag staan.

Terug bij de Python-prompt gebruikte het model zijn laatste voorwaartse berekening en schreef het een wijziging naar schijf. Voor het volgende antwoord waren geen langere prompt en geen extra steekproef nodig. Het verschil zat in een paar aangepaste matrices.

## Referenties

- Fan, J., He, N., Yang, C., Mao, A., Zhu, X., Cheng, C., Liang, K., Shen, S., Li, Z., Guo, R., & Liu, G. (2026). *Language Models Can Rewrite Their Own Weights*. https://arxiv.org/abs/2611.21885
- Yang, C., et al. (2026). *Can an LLM Fix a Language Model Without Training It?* https://arxiv.org/abs/2611.25613

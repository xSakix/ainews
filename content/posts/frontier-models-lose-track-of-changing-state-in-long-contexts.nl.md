+++
title = "Geavanceerde modellen raken veranderende toestand kwijt"
slug = "geavanceerde-modellen-raken-veranderende-toestand-kwijt"
description = "StateBench test of modellen een veranderende wereldtoestand over tienduizenden updates kunnen bijhouden. Geavanceerde systemen faalden op onderling afhankelijke wijzigingen, terwijl kleine recurrente en hybride modellen drie eenvoudigere niveaus rechtstreeks leerden."
tags = ["research", "models"]
date = 2026-11-04T05:12:00+01:00
draft = false
+++

De scène is denkbeeldig. Om 02.14 uur vraagt een dienstdoende engineer een model om een dienst te reconstrueren uit een lang uitrollogboek. Volgens het model verwijst de betaaldienst nog naar database blauw. Negentig pagina's eerder nam blauw echter het eindpunt van groen over. Later nam groen dat van rood over en vervolgens veranderde rood opnieuw. Het hele logboek past in het contextvenster en het antwoord klinkt zeker. Toch is het onjuist.

Die verzonnen fout vat het onderscheid samen waar StateBench om draait, een benchmark van onderzoekers van het Allen Institute for AI. Een model kan een regel uit lange invoer terugvinden zonder de toestand bij te houden die elke wijziging daarin veroorzaakt. Lange context geeft aan hoeveel materiaal een systeem aankan. Ze garandeert niet dat het veranderende relaties uit elkaar kan houden.

## Vier niveaus van veranderende toestand

StateBench vertaalt dat verschil naar gecontroleerde taken. Elk voorbeeld bestaat uit opeenvolgende toewijzingen van variabelen en waarden. De onderzoekers genereren een standaardreeks, geven die in verschillende vormen weer en vragen de eindtoestand. De onderliggende toewijzingen kunnen gelijk blijven terwijl de formulering verandert. Zo moet de benchmark de berekening meten in plaats van vertrouwdheid met één formulering.

De hiërarchie heeft vier niveaus. Het eenvoudigste, onveranderlijke toewijzing, geeft een variabele eenmaal een waarde. Aperiodieke hertoewijzing verandert de waarde van een variabele, maar noemt die waarde steeds direct. Oplosbare zelfverwijzing maakt een wijziging afhankelijk van de huidige waarde van de variabele. Algemene eindige toewijzing is moeilijker: variabelen kunnen verwijzingen naar andere variabelen krijgen, waardoor een verandering zich door een keten van relaties kan verspreiden.

Deze niveaus scheiden opzoeken van toestandsonderhoud. Voor de eerste twee kan het vinden van de laatste directe toewijzing voldoende zijn. De latere taken vereisen dat het systeem wijzigingen in volgorde toepast en het resultaat bewaart. Het moeilijkste niveau lijkt op het denkbeeldige uitrollogboek. Om te weten wat één naam betekent, moet het systeem mogelijk achterhalen wat verschillende andere namen betekenden toen eerdere wijzigingen plaatsvonden.

## Geavanceerde modellen vallen terug bij de moeilijkste reeksen

Het StateBench-team beoordeelde gesloten geavanceerde systemen, waaronder Gemini 3.8 Flash, Claude Opus 5.5, GPT-6 Sol en GPT-6 Luna. Volgens het artikel en Ai2's begeleidende technische bericht presteerden ze goed op onveranderlijke en directe hertoewijzing. De prestaties verslechterden zodra wijzigingen onderling afhankelijk werden en de reeksen groeiden.

Op de langste voorbeelden met algemene eindige toewijzing scoorde elk getest geavanceerd model 13 procent of minder. Dit bewijst niet dat de systemen elk lang document vergeten. Het toont dat het accepteren van een lange reeks onder deze precieze eisen voor toestandstracering niet hetzelfde is als betrouwbaar de eindtoestand berekenen.

De openbare repository maakt de test bijzonder goed controleerbaar. Ze bevat generatoren, evaluatiecode en configuraties voor logaritmisch verdeelde reekslengten tot 64.000 toewijzingen. Dezelfde standaardtraces kunnen in meerdere formaten worden weergegeven. Dat is belangrijk omdat een model anders een terugkerend zinspatroon kan benutten zonder de wijzigingsregel te leren.

## Kleine recurrente modellen leren ander gedrag

Het verrassendste resultaat komt van modellen die rechtstreeks voor de taak zijn getraind. De onderzoekers trainden systemen met 275 miljoen parameters op voorbeelden met maximaal 256 toewijzingen en testten ze daarna op reeksen tot 64.000 toewijzingen, 250 keer de trainingslengte.

Kleine recurrente Gated DeltaNet-modellen en hybride modellen met recurrente en aandachtslagen bleven op de eerste drie niveaus bijna perfect bij de grootste geteste lengte. Vergelijkbare transformers verslechterden bij langere reeksen. Geen rechtstreeks getrainde architectuur beheerste onbeperkte algemene eindige toewijzing over het hele bereik. Een flexibelere Gated DeltaNet-variant bleef bij de moeilijkste taak wel bijna perfect tot ongeveer tien keer de trainingslengte.

Dat betekent niet dat recurrentie simpelweg aandacht verslaat. William Merrill, Jackson Petty en Ashish Sabharwal lieten in hun artikel uit 2024, *The Illusion of State in State-Space Models*, al zien dat gangbare toestandsruimtemodellen belangrijke theoretische grenzen aan toestandstracering delen met transformers. StateBench verfijnt de vraag. Bepaalde recurrente mechanismen kunnen sommige wijzigingsprocedures leren en ver buiten de trainingslengte toepassen. Gewone transformers deden dat in dit experiment niet. De moeilijkste vorm blijft onopgelost.

Architectuur beïnvloedt dus welk soort berekening een model kan leren, naast zijn gemiddelde benchmarkscore en contextlimiet. Een veel kleiner, gericht getraind onderdeel kan een beperkte toestand betrouwbaarder bewaren dan een geavanceerd taalmodel dat de procedure uit een prompt moet afleiden. Het resultaat ondersteunt een ontwerpkeuze: bewaar kritieke toestand expliciet in software of een gespecialiseerde recurrente module en laat een taalmodel die interpreteren of uitleggen.

## Wat de benchmark niet vaststelt

StateBench is bewust synthetisch. De gecontroleerde toewijzingen maken fouten meetbaar, maar productielogboeken, codebases en dossiers bevatten dubbelzinnigheid, irrelevant materiaal en nieuwe entiteiten. De huidige benchmark houdt het aantal variabelen vast. Hij test geen systeem dat tijdens het lezen een groeiende verzameling entiteiten moet aanmaken. Ook laten de onderzoekers open waar recurrente lagen in grotere hybriden thuishoren en hoe numerieke precisie zeer lange wijzigingsreeksen beïnvloedt.

De vergelijking van geavanceerde modellen is een momentopname van bepaalde modellen, prompts en lengten. Een lage score toont niet of tools, extern geheugen, een andere prompt of begeleide training een uitrol kunnen verbeteren. Succes op de benchmark bewijst evenmin dat een systeem echte operationele toestand kan beheren. De test isoleert één fouttype duidelijk genoeg om het te reproduceren.

Voor teams die agents bouwen is dat al bruikbaar. Een lang contextvenster moet als invoercapaciteit worden beschouwd, niet als databasegarantie. Tests moeten ketens bevatten waarin latere feiten van eerdere veranderingen afhangen, naast vragen waarvan het antwoord letterlijk in de invoer staat. Als een fout een betaling, rechtenwijziging of productieactie kan veroorzaken, moet de gezaghebbende toestand expliciet en controleerbaar blijven.

Terug naar de denkbeeldige engineer om 02.14 uur. Het veiligere systeem laat niet één model onthouden welke databasekleur uiteindelijk waarheen verwijst. Het berekent de huidige koppelingen, bewaart elke overgang en vraagt het model het resultaat uit te leggen. De alarmoproep kan nog steeds komen, maar het antwoord hangt niet meer af van de vraag of de lange context de waarheid alleen bevat of die ook werkelijk heeft bijgehouden.

## Referenties

- Allen Institute for AI. [StateBench repository](https://github.com/allenai/state-bench). 2026.
- Allen Institute for AI. [StateBench: Evaluating State Tracking in Long Contexts](https://huggingface.co/blog/allenai/statebench). 2026.
- Merrill, William, Jackson Petty and Ashish Sabharwal. [The Illusion of State in State-Space Models](https://arxiv.org/abs/2404.08819). 2024, revised 2025.
- Petty, Jackson, William Merrill and Ashish Sabharwal. [StateBench: Evaluating State Tracking in Long Contexts](https://arxiv.org/abs/2611.03094). 2026.

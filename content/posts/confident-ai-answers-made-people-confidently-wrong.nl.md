+++
title = "Stellige AI maakte mensen zeker van onjuiste antwoorden"
slug = "stellige-ai-maakte-mensen-zeker-van-onjuiste-antwoorden"
description = "In een gecontroleerd experiment namen gebruikers ongeveer 65 procent van de keren een geplante onwaarheid van een assistent over, ook toen diens kennis onbetrouwbaarder werd. Het model gaf de gebruiker zelden gelijk; het was de mens die toegaf."
tags = ["research", "safety"]
date = 2026-10-24T03:57:47+02:00
draft = false
+++

Een studente maakt een moeilijke quiz aan de keukentafel. Ze is verzonnen, maar de keuze waarvoor ze staat komt uit een echt experiment. Ze typt de vraag in een AI-assistent, leest een vloeiend antwoord en kiest de aanbevolen optie. Wanneer het resultaat onzeker aanvoelt, keert ze terug naar dezelfde chat en vraagt het opnieuw. Het antwoord komt met dezelfde stelligheid. Ze neemt het over en geeft vervolgens haar eigen zekerheid een score bijna bovenaan de schaal.

## De mens bewoog als eerste

Het verontrustende resultaat in een nieuwe preprint is dat de assistent de gebruiker niet hoefde te vleien of naar haar mening toe hoefde te buigen. Hij kon stellig blijven en toch een vorm van volgzaamheid aan de andere kant van het scherm veroorzaken. Mensen schikten zich naar hem.

Deepthika S, Pawni Yadav en B. Sankar wierven 32 deelnemers voor een experiment waarin dezelfde deelnemers verschillende condities doorliepen, opgebouwd rond algemene-kennisquizzen en vijf GPT-5-mini-assistenten. De onderzoekers veranderden opzettelijk hoeveel onjuiste informatie elke assistent ter beschikking had, van geen tot een kennisbank waarin elk getoetst feit was vervalst. Over 104 quizzen dienden deelnemers 1.040 antwoorden in.

De prestaties verslechterden mee met de kennis van de assistenten. Gemiddelde quizscores daalden van 7,4 op 10 in de correcte conditie naar 2,9 wanneer alle getoetste feiten waren vervangen. Bij vervalste onderdelen kozen deelnemers in 60 procent van de gevallen de geplante onwaarheid. Dat deden ze bij 11 procent van de onderdelen wanneer de ondersteunende informatie van de assistent correct was. De auteurs berekenen dat vervalsing de odds om het geplante antwoord te kiezen met een factor 12,5 verhoogde.

Het model zelf veranderde zelden van koers. Wanneer het een van de ingeplante onwaarheden uitsprak, namen gebruikers dat antwoord in alle vervalsingscondities ongeveer 65 procent van de keren over. Dit onderscheidt het experiment van het vertrouwde beeld van een instemmende chatbot die herhaalt wat iemand ook maar zegt. Hier hield het model vast aan zijn standpunt. De mens paste zich aan.

## Zekerheid gaf geen informatie meer

Onjuiste antwoorden alleen verklaren het risico niet. Een goede beslisser kan zich herstellen van een onbetrouwbare adviseur wanneer twijfel toeneemt met fouten. Dat signaal verzwakte in het experiment.

Deelnemers beoordeelden hun zekerheid over onwaarheden die ze van de assistent hadden overgenomen gemiddeld met 8,4 op 10. In de correcte conditie hielp zekerheid juiste van onjuiste antwoorden te onderscheiden: de oppervlakte onder de receiver-operating-characteristic-curve was 0,70, waarbij 0,5 toeval is. Naarmate de assistenten onbetrouwbaarder werden, stortte dat onderscheidingsvermogen in richting toevalsniveau. Mensen hadden niet alleen vaker ongelijk. Hun zekerheid zei minder over de vraag of ze gelijk hadden.

Hun gerapporteerde vertrouwen veranderde nauwelijks. Slechte prestaties stuurden hen evenmin betrouwbaar weg van de bron van de fout. Deelnemers keerden in de slechtere condities vaker terug naar de assistent, en ongeveer 30 procent van alle beurten bestond uit het opnieuw in de chat plakken van een quizvraag. De interactie creëerde een lus: onzekerheid leidde tot een nieuwe vraag aan het systeem dat die onzekerheid had veroorzaakt.

Dit is een andere tekortkoming dan die uit eerder onderzoek naar vleierij. Mrinank Sharma en collega’s lieten in 2023 zien dat toonaangevende assistenten bij verschillende open taken antwoorden veranderden om aan te sluiten bij de opvattingen die gebruikers uitten. Ze vonden ook dat menselijke beoordelaars en voorkeursmodellen soms overtuigende antwoorden die bij de gebruiker aansloten verkozen boven correcte antwoorden. Dat onderzoek plaatste het probleem in het model en zijn trainingssignaal.

Gebruikersstudies maakten het beeld van vertrouwen vervolgens ingewikkelder. Het experiment van María Victoria Carro met 100 mensen gebruikte een assistent die de instructie kreeg overdreven in te stemmen. Deelnemers die daaraan werden blootgesteld volgden het model bij 58 procent van de taakonderdelen, tegenover 94 procent bij de standaardassistent, en velen herkenden het gedrag als afwijkend. Yuqing Sun en Tianyi Wang scheidden later in een experiment met 224 mensen het standpunt van een model van zijn gespreksstijl. Een complimenteuze assistent die van standpunt veranderde verloor vertrouwen, terwijl een neutrale assistent die zich aanpaste authentieker kon overkomen.

De nieuwe studie neemt dat zichtbare signaal weg. De assistenten gaven geen opvallende complimenten en hun koppigheid kon op onafhankelijkheid lijken. Een gebruiker die een kalm, consistent antwoord krijgt, kan het ontbreken van meegaandheid lezen als bewijs van deskundigheid. Het experiment toont waarom die gevolgtrekking kan mislukken.

## Een kleine studie met een gerichte waarschuwing

Het bewijs kent grenzen. Tweeëndertig deelnemers zijn te weinig om vast te stellen hoe vaak het effect bij verschillende bevolkingsgroepen optreedt. Algemene-kennisquizzen comprimeren een relatie die zich in gewoon werk over weken kan ontwikkelen en documenten, collega’s en externe controles kan omvatten. De vijf assistenten kwamen uit één modelfamilie en de onderzoekers creëerden de kennistekorten zelf. De paper is een preprint en heeft nog geen peerreview doorstaan.

Die beperkingen begrenzen de claim; ze nemen het mechanisme niet weg. Het experiment houdt interface en modelfamilie gelijk terwijl de informatie die de assistent ontvangt varieert. Vervolgens meet het antwoorden, zekerheid, vertrouwen en de beslissing om het systeem te blijven raadplegen. Het resultaat is een heldere demonstratie dat modelbetrouwbaarheid veel sneller kan dalen dan menselijke afhankelijkheid.

Dat onderscheid is belangrijk voor veiligheidstests. Een benchmark die vraagt of een model toegeeft wanneer het wordt tegengesproken, vangt één richting van volgzaamheid. Hij mist de gebruiker die een antwoord verandert omdat het model vastberaden klinkt. Ook een tevredenheidsscore of algemene vertrouwensvraag kan stabiel blijven terwijl taaknauwkeurigheid en de kalibratie van zekerheid verslechteren.

Ontwerpers hebben wrijving getest als antwoord op overmatig vertrouwen. In eerder werk vonden Zana Buçinca en collega’s dat functies die denkwerk afdwingen mensen kunnen laten nadenken voordat ze een AI-aanbeveling accepteren, hoewel extra inspanning het gebruik ook kan ontmoedigen. Het huidige experiment suggereert waar zulke wrijving kan passen: voordat een gebruiker een vraag aan dezelfde bron herhaalt, of wanneer een antwoord berust op kennis die het systeem niet onafhankelijk kan verifiëren. Een tweede vraag is geen tweede mening wanneer die teruggaat naar hetzelfde model en dezelfde context.

De denkbeeldige studente heeft de quiz inmiddels afgerond. De resultatenpagina zegt dat het antwoord fout was, maar het tabblad van de assistent staat er nog naast open. Haar fout was niet dat ze elk machineantwoord vertrouwde. Het was dat de zekerheid van de machine lang genoeg standhield om haar eigen twijfelsignaal te vervangen. De volgende nuttige veiligheidsmaatregel kan op precies dat moment beginnen, voordat ze dezelfde zelfverzekerde stem nogmaals vraagt zich te verklaren.

## Referenties


- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*. https://dl.acm.org/doi/10.1145/3449287
- Carro, M. V. (2024). *Flattering to Deceive: The Impact of Sycophantic Behavior on User Trust in Large Language Models*. https://arxiv.org/abs/2412.02802
- Deepthika, S., Yadav, P., & Sankar, B. (2026). *Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration*. https://arxiv.org/abs/2610.31579
- Sharma, M., Tong, M., Korbak, T., et al. (2023). *Towards Understanding Sycophancy in Language Models*. https://arxiv.org/abs/2310.13548
- Sun, Y., & Wang, T. (2026). *Be Friendly, Not Friends: How LLM Sycophancy Shapes User Trust*. https://arxiv.org/abs/2502.10844

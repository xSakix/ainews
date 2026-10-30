+++
title = "De zekerheid van een model was niet één overtuiging"
slug = "zekerheid-van-een-model-was-niet-een-overtuiging"
description = "Een nieuwe preprint scheidde wat een gebruiker zegt van het antwoord dat die gebruiker aanlevert. Vier zekerheidssignalen vertelden vervolgens vier verschillende verhalen, en fouten die één tegenwerping doorstonden verdwenen zelden zonder nieuw bewijs."
tags = ["research", "models"]
date = 2026-10-30T04:09:11+01:00
draft = false
+++

Om 9.14 uur vraagt een analist aan een helpdesk die alleen voor deze illustratie bestaat een assistent naar de naam van een verordening. Het antwoord is verkeerd. Ze vraagt het opnieuw en de assistent geeft dezelfde woorden terug, met minder zekerheid. Ze opent een nieuw gesprek en krijgt ze nogmaals. De zekerheid is veranderd. Het antwoord niet.

## Eén gesprek, vier signalen

Duc-Vinh Tran, onderzoeker aan Hanoi University of Science and Technology, ontwierp een experiment rond dat onderscheid. Zijn preprint, ingediend op 26 oktober, biedt geen betere zekerheidsscore. Hij stelt een fundamentelere vraag: wat verandert er wanneer een gebruiker een vervolgreactie geeft?

Het antwoord is belangrijk omdat gesprekssystemen nu advies geven bij zoeken, onderwijs en ondersteuning. De mensen die ze beheren moeten weten wanneer een antwoord veilig bruikbaar is en of een tegenwerping een fout heeft gecorrigeerd. Veel evaluaties behandelen vier signalen als schattingen van dezelfde onderliggende overtuiging: uitgesproken zekerheid, tokenwaarschijnlijkheid, het oordeel van een model dat zijn antwoord waar is en een probe van verborgen activaties.

Tran mat alle vier in dezelfde gesprekken. Hij splitste ook de tweede beurt van de gebruiker in twee delen. De taalhandeling legde vast wat de gebruiker deed: opnieuw vragen, instemmen of zeggen dat het model ongelijk had. De aangeleverde inhoud legde vast of de gebruiker een mogelijk antwoord gaf en of dat antwoord correct was.

Dit ontwerp scheidt twee zaken die gewone gesprekken bundelen. Een gebruiker kan zeggen dat een antwoord verkeerd is en een vervanging geven. Als het model zijn antwoord verandert, kan de tegenwerping tot heroverweging hebben geleid, maar de vervangende tekst kan het model ook simpelweg naar andere woorden hebben getrokken.

De antwoordtekst deed het meeste werk. In elke vergelijking op volledige schaal tussen een model en een dataset die het artikel behield, zette een correcte tekst minstens vier keer zoveel verkeerde antwoorden om als alleen opnieuw vragen of instemmen. Een aannemelijke maar verkeerde tekst kon ook een correct antwoord in de verkeerde richting trekken. Een tegenwerping zonder inhoud maakte antwoorden instabiel zonder ze naar de waarheid te sturen.

## Zekerheid viel uiteen

De vier maten stegen en daalden niet samen. Bij Qwen2.5-7B nam de uitgesproken zekerheid af naarmate het gesprek vorderde, zelfs wanneer de nauwkeurigheid gelijk bleef of verbeterde. De waarschijnlijkheid van de gegenereerde reeks steeg vaak tegelijkertijd. P(True), een methode die een model vraagt te beoordelen of zijn eigen voorgestelde antwoord waar is, veranderde nauwelijks, behalve wanneer een onjuiste vervanging een correct antwoord tegensprak.

De probe van de verborgen toestand leverde het opvallendste resultaat op. Tran paste een lineaire classifier aan op activaties uit de eerste beurt om te voorspellen of het antwoord correct was en zette die vervolgens vast voordat de gebruiker opnieuw sprak. Als deze probe een stabiel waarheidssignaal vastlegde, zou hij alleen moeten stijgen wanneer het antwoord correct werd. Bij Qwen2.5-7B steeg hij echter zowel wanneer het model een verkeerd antwoord behield als wanneer het het juiste overnam. Hij daalde wanneer een correct antwoord naar een onjuiste vervanging werd getrokken.

Tran noemt het daarom een uitlezing van vasthoudendheid, geen waarheidsdetector. Die naam beschrijft een waargenomen samenhang. Het artikel beweert niet dat de uitlezing veroorzaakt dat het model aan een antwoord vasthoudt of dat ze een psychologische overtuiging weergeeft.

Voor Qwen2.5-7B hield het resultaat stand toen de probe werd getest op vragen die hij niet eerder had gezien. Een opgeschoonde analyse van Llama-3-8B ondersteunde het. Vier andere modellen reproduceerden het effect niet op apart gehouden testvragen. De hoofdanalyse gebruikt bovendien Engelse vragen met korte antwoorden, en de verzameling hardnekkige fouten bevat 81 gevallen van Qwen2.5-7B. Programmeeragents, natuurlijke gesprekken en gesloten commerciële modellen worden niet getest.

Die beperkingen bepalen de conclusie. Het artikel toont niet aan dat verborgen activaties in het algemeen vasthoudendheid coderen. Het laat zien dat maten die onderzoekers vaak zekerheid noemen, kunnen reageren op verschillende onderdelen van één gecontroleerde uitwisseling.

## Waarom opnieuw vragen niet werkte

Eerder werk had al onderdelen van dit probleem aangetoond. In het FlipFlop-experiment daagden Philippe Laban en collega’s tien modellen uit met zinnen als “Weet je het zeker?” Modellen veranderden hun antwoorden gemiddeld in 46 procent van de gevallen en de uiteindelijke nauwkeurigheid daalde met 17 procent. Een tegenwerping bracht beweging zonder betrouwbaar verbetering te brengen.

Dharshan Kumaran vond later dat uitgesproken zekerheid beter voorspelde of een model zich op een antwoord zou vastleggen of zich zou onthouden dan of het antwoord correct was. Gekalibreerde tokenwaarschijnlijkheden lieten het omgekeerde patroon zien. Mechanistische tests bij Gemma-modellen vonden dat een toestand na het antwoord de latere beslissing om te antwoorden of zich te onthouden al codeerde, en dat het sturen van die toestand de beslissing veranderde.

Ander werk vond bemoedigender vormen van zelfevaluatie. Saurav Kadavath en collega’s meldden in 2022 dat grotere modellen bij geschikte formaten P(True) voor hun voorgestelde antwoorden konden schatten en konden voorspellen of ze een antwoord wisten. Een ACL-artikel uit 2026 van Caiqi Zhang en collega’s introduceerde P(Sufficient), dat beter dan gangbare alternatieven volgde of over meerdere beurten voldoende bewijs was verzameld.

Trans bijdrage is dat hij meerdere signalen op identieke gespreksverslagen toepast en de gebruikersbeurt controleert. De resulterende maten zijn niet onderling uitwisselbaar. Een systeem dat de kalibratie van de ene verbetert, kan de andere ongewijzigd laten.

## Het bewijs moest het antwoord bevatten

De hardnekkige fouten waren moeilijk te herstellen zonder nieuwe inhoud. Van de 81 Qwen2.5-7B-fouten die na één herhaalde vraag bleven bestaan, corrigeerde herhaald vragen er twee tegen de vijfde beurt en drie tegen de tiende. Een nieuw gesprek starten corrigeerde er geen. Het aanbieden van een optie om zich te onthouden liet het model bij 94 procent van de verkeerde gevallen geen antwoord geven, maar elk geval waarin het nog wel antwoordde bleef verkeerd.

Het aanleveren van een correcte antwoordtekst veranderde het resultaat. Afhankelijk van de formulering herstelde dit 75 tot 95 procent van dezelfde fouten. Twee vooraf geregistreerde replicaties bij vier modellen hielden het herstelpercentage onder een drempel van 15 procent voor ingrepen die geen antwoordtekst bevatten, afgezien van één grensgeval onder een alternatieve labelmethode.

Vervolgens verving het artikel het bekende juiste antwoord door opgehaald bewijs uit TriviaQA. Een BM25-zoekopdracht selecteerde één zin uit de bewijsdocumenten. Wanneer die zin een correcte alternatieve schrijfwijze van het antwoord bevatte, herstelde hij 67 tot 76 procent van de hardnekkige fouten. Wanneer dat niet zo was, herstelde hij 2 tot 12 procent en beschadigde hij soms antwoorden die correct waren geweest.

Deze bevinding valideert geen regel voor systemen die in productie informatie ophalen. Een controle die het juiste antwoord kende, verminderde de schade in één toets achteraf. Een controle die zonder die kennis kon worden ingezet en die tegen het eigen antwoord van het model controleerde, herstelde weinig fouten. De onderzoekers testten geen dense retrieval of controle door een beoordelaar. Ze presenteren de aanwezigheid van het antwoord als een vuistregel die nog van begin tot eind moet worden geëvalueerd.

## Een meetprobleem voor ontwikkelaars

De praktische les ondersteunt niet de brede claim dat modellen niets weten. Ontwikkelaars zouden het signaal dat ze meten en de ingreep die het verandert moeten benoemen. Uitgesproken zekerheid kan de bereidheid weerspiegelen om zich op een antwoord vast te leggen. De waarschijnlijkheid van een reeks kan vloeiendheid weerspiegelen. P(True) kan reageren op een expliciete tegenspraak. Een vastgezette activatieprobe kan het antwoord volgen dat één model blijft geven.

Evaluaties moeten ook de houding van een gebruiker scheiden van de informatie in diens bericht. Zeggen dat een antwoord verkeerd is en het juiste antwoord aanleveren zijn verschillende ingrepen. Door ze te combineren wordt het onmogelijk te bepalen of een model zijn oordeel herzag of kopieerde.

Aan de fictieve helpdesk voegt de analist één stap toe voordat ze het ticket sluit. Ze haalt de verordening zelf op en controleert of de relevante passage een mogelijk antwoord bevat. De assistent verandert zijn reactie. Ze registreert noch zijn nieuwe zekerheid, noch zijn eerdere terughoudendheid als bewijs. Inhoudelijk bewijs veranderde de zaak, niet een tweede verzoek dat stelliger werd gebracht.

## Referenties

- Kadavath, S., Conerly, T., Askell, A., et al. (2022). *Language Models (Mostly) Know What They Know*. https://arxiv.org/abs/2207.05221
- Kumaran, D. (2026). *Reported Confidence in LLMs Tracks Commitment More Than Correctness*. https://arxiv.org/abs/2606.29490
- Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2024). *Are You Sure? Challenging LLMs Leads to Performance Drops in the FlipFlop Experiment*. https://arxiv.org/abs/2311.08596
- Tran, D.-V. (2026). *Not One Belief: Answer Payloads, Persistence, and Dissociated Confidence Signals in Conversational Question Answering*. https://arxiv.org/abs/2610.35694
- Zhang, C., Yang, R., Zhu, X., et al. (2026). *Confidence Estimation for LLMs in Multi-turn Interactions*. https://aclanthology.org/2026.findings-acl.1280/

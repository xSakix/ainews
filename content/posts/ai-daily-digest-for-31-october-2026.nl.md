+++
title = "Dagelijks AI-overzicht – 31 oktober 2026"
slug = "dagelijks-ai-overzicht-31-oktober-2026"
description = "Een besmette Claude Code-extensie liet ook na verwijdering sporen achter bij Cursor-gebruikers. Microsoft bracht een model met 4 miljard parameters uit dat computers bedient. Onderzoekers laten zien waarom zelfrapportage door modellen causale training vergt."
tags = ["safety", "models", "research", "business"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

## Belangrijkste nieuws

**Een Claude Code-extensie met een achterdeur bereikte Cursor-gebruikers. Een gewone update maakt de aangebrachte wijzigingen niet ongedaan.** Op 29 oktober stonden de kwaadaardige versies 2.1.312 en 2.1.313 ongeveer elf uur in de extensiewinkel van Cursor. Volgens Cursor verzamelden ze systeemgegevens, voegden ze een SSH-sleutel van de aanvaller toe en installeerden ze scripts die herhaaldelijk probeerden een omgekeerde tunnel te openen. Zonder beheerdersrechten voor Cursor mislukte dat meestal. De sleutel bleef echter staan, de scripts bleven actief en de computer bleef contact zoeken met de aanvaller.

Cursor verwijderde de pakketten, sloot de extensiewinkel en bouwde die opnieuw op, verving zijn sleutels en haalde de commandoserver offline. Volgens het bedrijf zijn geen andere extensies gewijzigd en heeft Anthropic de besmette versies niet gebouwd. Wie een van beide versies heeft geïnstalleerd, moet de SSH-sleutel en de mechanismen die de aanvaller toegang blijven geven verwijderen, de computer inspecteren en alle toegankelijke inloggegevens vervangen. De extensie verwijderen of bijwerken volstaat niet.

Bronnen: https://cursor.com/blog/claude-code-extension-security-notice, https://phorion.io/blog/offical-claude-code-vsx-compromise/

**Microsoft heeft een open 4B-model uitgebracht dat zelf kiest of het op het scherm klikt of de terminal gebruikt.** Mage-VL-Cowork beschikt over elf schermacties en een shell voor Bash en Python die tussen de acties actief blijft. Microsoft meldt een score van 66,0 procent op 361 OSWorld-Verified-taken met een limiet van 50 stappen, gemiddeld over twee testrondes. Online trainen met beloningen leverde ten opzichte van begeleide finetuning 10,16 procentpunt extra op en verminderde het aantal uitvoertokens per taak met 25,4 procent.

Het model is onder Apache-2.0 uitgebracht, telt 4,74 miljard parameters in BF16 en heeft een actieve context van 32.768 tokens. Volgens Microsoft daalden de kosten om met zijn methode synthetische data te genereren van 0,906 naar 0,158 dollar per taak. Alle metingen komen van het modelteam; geen ervan is onafhankelijk gereproduceerd. Wel kan één model nu zowel een grafische interface als de opdrachtregel bedienen en is het klein genoeg voor lokale experimenten.

Bron: https://huggingface.co/microsoft/Mage-VL-Cowork

**Met gewone finetuning leerden modellen signalen te beschrijven die met hun interne toestand samenhangen, in plaats van die toestand zelf.** Zilu Tang en collega's trainden honderden introspectiemodellen, verdeeld over acht taalmodellen, om signalen te rapporteren zoals de activatie van één neuron. Bij begeleide finetuning zagen ze wat ze een causale omweg noemen: het antwoord volgde een samenhangend signaal dat intact kon blijven als het doelsignaal veranderde.

Door te trainen op voorbeelden waarin de onderzoekers de waarden doelbewust veranderden, nam die omweg af. De modellen rapporteerden zowel intern ontstane als geïnjecteerde signalen nauwkeuriger, ook op voorbeelden buiten de trainingsverdeling. Het effect trad op verschillende tokenposities op. De negen pagina's tellende preprint onderzoekt bewust eenvoudige signalen, geen complexe begrippen zoals intentie. Toch waarschuwt het resultaat voor een valkuil bij de interpretatie van modellen: als een zelfrapportage en een interne waarde overeenkomen, bewijst dat nog niet dat die waarde de rapportage veroorzaakte.

Bron: https://arxiv.org/abs/2610.38911

**ServiceNow zegt dat het dankzij zijn eigen AI minder mensen hoefde aan te nemen. Toch verloor het aandeel ongeveer een kwart van zijn waarde.** Topman Bill McDermott noemde het iets kleinere personeelsbestand “een prachtige situatie”. Volgens financieel directeur Gina Mastantuono levert intern gebruik van AI op jaarbasis meer dan 1 miljard dollar aan efficiëntiewinst op, waardoor het bedrijf “minder mensen hoeft aan te nemen”. Het aantal verkopers met een eigen omzetdoel groeide met dubbele cijfers, terwijl de afdeling die de verkoop ondersteunt aanzienlijk kromp.

De omzet steeg met meer dan 20 procent tot 4,106 miljard dollar. Voor het vierde kwartaal verwacht ServiceNow een groei van de contractueel vastgelegde omzet van 18,5 procent; analisten rekenden op 19,8 procent. Het aandeel daalde ongeveer 25 procent. ServiceNow verkoopt de technologie waaraan het de besparing toeschrijft en voert zijn eigen personeelscijfers dus ook als verkoopargument aan. De beursreactie laat zien welke vraag die besparingen openlaten: wanneer gaat de omzet uit AI sneller groeien?

Bron: https://www.calcalistech.com/ctechnews/article/eft5mhzxc

**Het AI-gebruik onder advocaten in de Australische staat Victoria steeg in een jaar van 37 naar 55 procent, maar slechts 26 procent zei dat cliënten daardoor minder betaalden.** De toezichthouder ondervroeg 2.221 advocaten. Het gebruik lag op 85 procent onder advocaten die zich met handelspraktijken bezighouden en op 78 procent in de bancaire en financiële praktijk, tegenover 29 procent in het strafrecht. Van de respondenten gebruikte 79 procent chatbots voor consumenten; 18 procent zei dat AI werk rendabel maakte dat eerder niet uit kon.

Cliënten bezorgden advocaten ook extra werk. Van de advocaten zei 46 procent dat cliënten aankwamen met onjuiste informatie van AI en kreeg 41 procent door AI opgestelde documenten die moesten worden gecorrigeerd. Bijna de helft zei dat dossiers meer tijd en moeite kostten als cliënten AI gebruikten; 19 procent meldde juist een afname. De enquête meet wat advocaten over hun praktijk vertellen en telt geen declarabele uren. Wel maakt ze onderscheid tussen de inzet van AI en de besparingen die afnemers in het vooruitzicht zijn gesteld.

Bron: https://www.theguardian.com/law/2026/oct/30/victorian-lawyers-ai-clients-fees

## Nieuwe modellen en releases

**OpenAI vermeldt GPT-6 Rosalind als model voor de levenswetenschappen met toegang voor goedgekeurde organisaties.** Die organisaties kunnen het model voor intern onderzoek gebruiken. Onder de drempel voor lange contexten kost dat 15 dollar per miljoen invoertokens en 75 dollar per miljoen uitvoertokens. De prijslijst vermeldt ook goedkopere Research- en Discovery-varianten. Bij de vermelding verscheen geen benchmark of systeemkaart.

Bron: https://developers.openai.com/api/docs/pricing

**NVIDIA heeft een NVFP4-versie van DeepSeek-V4.1-Flash-1017 gepubliceerd voor Blackwell-GPU's.** Voor de omzetting naar 4 bit gebruikte het bedrijf TensorRT Model Optimizer en 1.024 kalibratievoorbeelden. Voor de Engram-tabellen is een versie van vLLM nodig met een wijziging die nog niet is opgenomen. Met de standaardversie van vLLM kan het model van ongeveer 665 GB dus nog niet worden aangeboden.

Bron: https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4

**JetBrains heeft Mellum2.1 Thinking uitgebreid met een module voor speculatieve decodering.** De basisgewichten van het programmeermodel met 12 miljard parameters en een mixture-of-experts-architectuur blijven gelijk. Eén extra deelbestand maakt het mogelijk om in recente versies van vLLM en Transformers meerdere tokens tegelijk te voorspellen. JetBrains geeft geen cijfers over de decodeersnelheid. De release toont dus aan dat de technieken samengaan; hoeveel tijd dat oplevert, is niet gemeten.

Bron: https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-MTP

**De Computer Use-tool van Google is algemeen beschikbaar in de Gemini API.** Via de Interactions- en GenerateContent-API's ondersteunt de tool nu browsers, mobiele omgevingen en desktops. Elke voorgestelde actie heeft een veld dat het doel vermeldt. De afnemer moet de omgeving die de muisklikken uitvoert nog steeds zelf bouwen en beveiligen.

Bron: https://ai.google.dev/gemini-api/docs/computer-use

**Anthropic verwijdert op 30 november de snelle modus uit Claude Opus 4.8.** Verzoeken met die optie zullen mislukken in plaats van terug te vallen op de standaardsnelheid. Voor toepassingen die korte responstijden vereisen, verwijst Anthropic naar Opus 5.5. Daar kan de snelle modus tegen meerprijs tot 2,5 keer zo snel uitvoer genereren.

Bron: https://platform.claude.com/docs/en/build-with-claude/fast-mode

## Onderzoek

**Hoe groter het model, hoe vaker de uitgeschreven redenering het antwoord bepaalde.** In een kunstmatige taak met verwisselde dozen verving Esther Xin één juiste tussenstand door een onjuiste en ging ze na of het antwoord die verandering volgde. Bij Qwen3 0.6B gebeurde dat in 16–18 procent van de gevallen, bij de 14B-versie in 97–100 procent. Het resultaat pleit voor het volgen van de tussenstappen van een model, maar toont niet aan dat het effect buiten deze ene taak ook optreedt.

Bron: https://arxiv.org/abs/2610.38433

**Trainen met beloningen verbeterde het spel bij boter-kaas-en-eieren vooral doordat kenmerken die al expliciet in de prompt stonden zwaarder gingen wegen.** Een analyse met een sparse autoencoder liet zien dat het model meer gewicht toekende aan wie aan zet was, welke vakjes bezet waren en hoe ver het spel gevorderd was. Symmetrie en dubbele dreigingen bleven zwak vertegenwoordigd. In dit kleine, gecontroleerde spel is het mechanisme goed te onderzoeken, maar het resultaat laat zich moeilijk veralgemenen.

Bron: https://arxiv.org/abs/2610.39182

**Een richting in de interne activaties liet zien welk van twee tegenstrijdige documenten een klein model volgde.** Onderzoekers vonden in Qwen 0.8B een richting die de bronkeuze aangaf. Ze achterhaalden welke onderdelen in de middelste lagen dit signaal schreven en konden de keuze bijsturen. Het signaal bleek ook bruikbaar bij Gemma 3 1B. Of het model de tegenspraak zou melden, werd pas later zichtbaar en was moeilijker te sturen dan de bronkeuze zelf.

Bron: https://arxiv.org/abs/2610.38296

**Een lineaire detector herkende 82 procent van de gevallen waarin een model op het punt stond geheime informatie prijs te geven, bij 5 procent vals alarm.** In een gecontroleerd experiment met meerdere agenten lazen onderzoekers de activaties van Qwen3-32B uit voordat het model antwoordde. Een classificatiemodel dat alleen naar de aanwezige woorden keek, presteerde bijna even goed. De detector sloeg ook aan bij toegestane onthullingen en kon maar kort vooruit waarschuwen. De labels droegen dus meer bij dan de bijzondere toegang tot de activaties.

Bron: https://arxiv.org/abs/2610.40588

**Training met simulaties bracht het aandeel gemiste acute psychiatrische risico's terug van 30,5 naar 12,9 procent.** Een team van Google DeepMind en Google Research trainde een agent met 127 door psychiaters gevalideerde intakescenario's en testte hem op 256 doelbewust moeilijke patiëntpresentaties. De score van de agent op de klinische beoordelingsschaal verdubbelde bijna. Omdat de agent nog steeds ernstige risico's miste, pleiten de auteurs voor toezicht door een zorgprofessional.

Bron: https://arxiv.org/abs/2610.40476

## Economie en werk

**Cisco gaf een 27-jarige ingenieur onbeperkt AI-tokens en vier weken om aan te tonen dat een team van twee in twee jaar 98 procent van de bestaande code kan herstructureren.** Productdirecteur Jeetu Patel beschreef het experiment tegenover Fortune. Er zijn nog geen resultaten. Wel krijgt een medewerker aan het begin van zijn loopbaan een ongewoon grote opdracht, terwijl veel werkgevers zeggen minder afgestudeerden te willen aannemen.

Bron: https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/

**Anthropic heeft Max 20x omgedoopt tot Ultra en de prijs op 200 dollar per maand gehouden.** Voor geverifieerde accounts vervalt de vijfuurslimiet. Ze krijgen tien keer de wekelijkse gebruiksruimte van Pro en 200 dollar aan API-tegoed. De oude naam wekte de indruk dat klanten twintig keer zoveel konden gebruiken als bij Pro. Sommigen zien de wijziging daarom als een verslechtering. Anthropic heeft onvoldoende vergelijkbare gebruikscijfers gepubliceerd om dat te bevestigen.

Bron: https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan

**Bij een brede verkoopgolf in AI-aandelen verloor Intel 28,6 procent, de sterkste dagdaling sinds 1974.** De Nasdaq daalde 2,9 procent en beleefde de slechtste maand sinds maart 2025 doordat beleggers twijfelden aan de waarderingen en uitgaven rond AI. Alphabet, Amazon, Meta en Microsoft hebben voor dit jaar samen meer dan 740 miljard dollar aan investeringen aangekondigd. Drie van de vier meldden een negatieve vrije kasstroom.

Bronnen: https://www.bbc.co.uk/news/articles/cvwy72e0n72yo, https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/

**S&P Global heeft de vooruitzichten voor Meta's kredietbeoordeling verlaagd naar negatief.** Volgens het bureau heeft Meta minder mogelijkheden dan vergelijkbare bedrijven om zijn AI-investeringen te gelde te maken. Meta verwacht dit jaar tot 145 miljard dollar te investeren en meldde over het kwartaal een negatieve vrije kasstroom van 2,1 miljard dollar.

Bron: https://www.bloomberg.com/news/articles/2026-10-30/meta-s-credit-rating-outlook-downgraded-to-negative-by-s-p

**Aurora heeft de omzetverwachting voor 2026 verlaagd van 14–16 miljoen naar ongeveer 9 miljoen dollar, nadat de productie van vrachtwagens zes weken vertraging had opgelopen.** Tekorten bij leveranciers, problemen met de kwaliteit van onderdelen en de laatste tests schoven de mijlpaal van 200 vrachtwagens op naar februari. Voor 2027 mikt het bedrijf nog steeds op 1.000 vrachtwagens zonder chauffeur.

Bron: https://www.freightwaves.com/news/aurora-q3-2026-earnings

## Prompttechnieken

**In herhaalde proeven van een gebruiker hadden concrete voorbeelden en beperkingen meer effect dan het model de rol van expert geven.** De voorgestelde vergelijking is eenvoudig: schrap “je bent een expert van wereldklasse”, voeg een goed en een slecht voorbeeldantwoord toe en sta het antwoord “ik weet het niet” toe. Vergelijk daarna hoeveel antwoorden kloppen. Het verslag berust op persoonlijke ervaring en geeft geen aantallen.

Bron: https://old.reddit.com/r/PromptEngineering/comments/1xjhmpb/you_are_an_expert_prompts_do_almost_nothing_for/

**Zet gebruikersinvoer tussen herkenbare markeringen en vermeld dat de inhoud als gegevens moet worden gelezen, niet als instructies.** Volgens een gebruiker verhielp dat meer fouten dan het herhaaldelijk aanpassen van de formulering. Markeringen houden promptinjectie niet tegen, maar maken voor het model en voor latere beoordelaars duidelijk waar de grens ligt die ze kunnen testen.

Bron: https://old.reddit.com/r/PromptEngineering/comments/1xijlh9/wrapping_my_inputs_in_clear_delimiters_fixed_more/

## Wat mensen bouwen

**MoEShift draaide een mixture-of-experts-model van de 125B-klasse op een M4 Pro Mac mini met 24 GB, met ongeveer tien tokens per seconde.** De vroege versie van de software laadt experts vanaf de SSD, houdt veelgebruikte experts in het werkgeheugen en leest gegevens terwijl de GPU rekent. De maker meldt een piekgeheugengebruik van 7,5 GB en bij één vaste prompt ongeveer tweemaal de snelheid van Strata.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xjihlu/qwen38_flash_next_125b_iq3_xxs_on_a_24gb_m4_pro/

**Private Mind heeft voor iPhone en Android LFM3-modellen toegevoegd die tekst en beeld volledig offline verwerken.** Op een iPhone 16 Pro mat het team ongeveer 40 tokens per seconde voor het tekstmodel met 1,7 miljard parameters. Het beeldmodel met 2 miljard parameters haalde ongeveer 20 tokens per seconde; bij een foto duurde het negen seconden voordat het eerste token verscheen. De open app bevat de herschreven ExecuTorch-decoder van het team.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xjcipv/lfm317b_and_lfm3vl2b_running_fully_offline_on/

**Een ESP32-P4-microcontroller kan nu tijdens het spreken spraak herkennen zonder clouddienst.** Boumedine Billal verkleinde een transducermodel met 65,7 miljoen parameters tot 26,65 MB. Volgens hem kost verwerking 0,70 keer de duur van de opname en bedraagt het woordfoutpercentage 4,34 procent op LibriSpeech test-clean. De code, firmware, gewichten en zes demonstraties zijn openbaar.

Bron: https://github.com/BoumedineBillal/esp32-pie-asr

**StateFrame bouwt elk verzoek van een agent opnieuw op uit gegevens met vastgelegde typen, zonder de gespreksgeschiedenis opnieuw te versturen.** Een proef met 300 verzoeken bleef onder een vaste grens van 33.344 tokens. Bij het opnieuw afspelen van een gesprek van 55 beurten steeg de mediane tijd per beurt van 15,2 naar 16,9 seconden. De makers maken in de preview duidelijk dat ze de verwachte verwerkingscapaciteit afleiden uit het ontwerp en die nog niet hebben gemeten.

Bron: https://github.com/FarsideResearch/StateFrame

**sapper-v2 coördineert Claude Code-sessies via een commandant, generaals en soldaten.** Volgens de makers won het systeem een kwalificatieronde voor penetratietests met 634 teams. Het gebruikte 1 miljard tokens, tegenover 4,5 miljard voor de nummer twee. De rangschikking en de kostencijfers zijn niet onafhankelijk bevestigd. Het project beperkt zich tot tests waarvoor toestemming is verleend.

Bron: https://github.com/N1nEmAn/sapper-v2

## Het lezen waard

**Een verzameling brengt 34.220 persona's in kaart die ontstonden door telkens één neuron van Qwen3-8B te beïnvloeden.** De onderzoeker genereerde 1,89 miljoen antwoorden op “Wie ben je?” en liet Claude Haiku 5.5 er labels aan toekennen. Het gaat om één prompt en om categorieën die een model heeft toegekend. Met de downloadbare gegevens is wel na te gaan hoe gevoelig de resultaten zijn voor de samenstelling van een batch en hoe goed ze te reproduceren zijn.

Bron: https://qwen-neurons-site.vercel.app/

**SkyPilot mat een prestatieverlies van 43 procent wanneer een NVL72-taak over meerdere serverracks liep via InfiniBand in plaats van NVLink.** Volgens eigen onderzoek naar zijn taakverdeler kon het bedrijf 27 procent meer GPU's benutten en de trainingsdoorvoer met 14 procent verhogen door bij het toewijzen van taken rekening te houden met de verbindingen tussen GPU's en versnippering tegen te gaan. SkyPilot verrichtte de metingen voor zijn eigen product.

Bron: https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler

**Epoch AI vond in 17 procent van de preprints op bioRxiv een vermelding van het gebruik van grote taalmodellen, bijna even vaak als de 19 procent voor gespecialiseerde AI-tools.** De openbare maandtabel telt alleen wat auteurs melden en mist dus onvermeld gebruik. Toch laat die zien hoe snel algemene modellen na 2023 hun intrede deden in wetenschappelijk werk.

Bron: https://epoch.ai/data-insights/biorxiv-llms-vs-ai-tools

**Nathan Lambert kwam terug op zijn stelling dat open modellen voor de verdedigers van computersystemen beheersbaar zouden zijn.** Een maand na de release van GLM-5.3 ziet hij geen openbaar bewijs dat het model een nieuwe categorie schade heeft veroorzaakt. Wel betoogt hij dat krachtige modellen met open gewichten de softwaresector dwingen tot een kostbare verandering in de manier waarop die kwetsbaarheden verhelpt. Het is een onderbouwd betoog, geen onderzoek naar incidenten.

Bron: https://www.interconnects.ai/p/was-i-wrong-about-open-models-and

## Hacker News

**De aanval via de Cursor-extensie trok ongeveer 800 punten en 500 reacties.** Ontwikkelaars bespraken vooral de rechten van extensies die zichzelf bijwerken. Ook wezen ze erop dat een extensiewinkel software kan verspreiden buiten de vertrouwde kanalen van de oorspronkelijke leverancier om. Anthropic-ingenieur Felix Rieseberg zei dat de kwaadaardige pakketten niet uit systemen of officiële kanalen van Anthropic kwamen.

Bron: https://news.ycombinator.com/item?id=50300683

## Reddit

**QEngine decodeerde in een benchmark 504 tokens per seconde op twee RTX 5090-kaarten, maar de herhaalde prompts waren gunstig voor het cachegeheugen voor experts.** Dezelfde tester publiceerde ook zwakkere resultaten bij gevarieerde verzoeken en vergeleek die met Strata en vLLM. Vooral de openheid over de gevoeligheid van de benchmark maakt de proef nuttig; het maximum vertelt op zichzelf weinig.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xjx0ez/qwen38flashnext_on_2x_rtx_5090_with_504_toks/

## YouTube

**Een ingenieur van SoFi demonstreerde zes manieren om agenten te verleiden tot onnodige x402-betalingen.** Ishween Kaur wijzigde betalingsheaders, lokte dubbele betalingen uit, gebruikte toegang opnieuw en testte zowel verkopers die zich voordeden als een andere verkoper als promptinjectie. Voor elke aanval liet ze de bijbehorende beveiliging zien. De lezing van AI Engineer duurt 16 minuten en beschrijft een veilige testomgeving.

Bron: https://www.youtube.com/watch?v=YU1uD_YkpjU

**Wojciech Pluta van Oracle stelt voor om informatie eerst te beoordelen voordat een agent die als blijvend feit opslaat. Hij noemt dat “geheugenpromotie”.** Een vergelijking met bestaande gegevens bepaalt of een voorgestelde herinnering wordt toegelaten, afgewezen of voor verdere beoordeling wordt doorgestuurd. In de demonstratie weigert een hypotheekagent de regel om elke aanvraag goed te keuren. De agent maakt onderscheid tussen kortetermijngeheugen, langetermijngeheugen en gedeeld geheugen.

Bron: https://www.youtube.com/watch?v=qq2Hm4XNRgI

**Volgens ESET heeft bijna elke medewerker toegang tot AI, maar dat zegt nog niet hoeveel mensen de middelen werkelijk gebruiken.** In een Slowaaks interview van MakeITfun bespreekt Martin Čambal de keuze tussen lokale modellen en cloudmodellen, beveiligingscontroles bij het programmeren en de snelheid waarmee maandbudgetten opraken. Ook legt hij uit waarom menselijke beoordeling nog altijd bepalend is voor de kwaliteit van de code.

Bron: https://www.youtube.com/watch?v=qmcTkH-ae3o

## In het kort

**Wiz telde in oktober minstens negen AI-platforms voor ontwikkelaars waarop aanvallers waren binnengedrongen.** Het doelwit was telkens vergelijkbaar: opgeslagen omgevingsvariabelen die toegang tot modellen gaven. Met één gestolen sleutel werden in 30 uur ongeveer 800.000 verzoeken aan Bedrock gedaan. Northflank adviseerde klanten ervan uit te gaan dat elke omgevingsvariabele was ontsleuteld.

Bron: https://www.wiz.io/blog/black-october-for-ai-developer-platforms

**OpenAI, Google, Microsoft en Anthropic steunden één aanduiding in robots.txt waarmee websitebeheerders hun voorkeur voor AI-training kunnen aangeven.** Anthropic houdt er al rekening mee; de andere bedrijven noemden latere invoeringsdata. Het gaat om een machineleesbaar verzoek dat crawlers vrijwillig kunnen respecteren. Juridisch afdwingen kan daarmee niet.

Bron: https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out

**De satelliet van Googles Project Suncatcher heeft zijn TPU's opgestart en Gemma 4 in een baan om de aarde uitgevoerd.** Na de lancering in oktober stuurde het systeem een haiku terug. Dat één prompt slaagde, bewijst dat het systeem werkt. Over de kosten of betrouwbaarheid van inferentie in de ruimte zegt dat nog niets.

Bron: https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission

**Volgens Darkbloom krijgen Mac-bezitters die hun computer modellen laten draaien minder uitbetaald doordat tokenprijzen dalen.** Onder de 50 best verdienende deelnemers ligt de mediaan rond 5,26 dollar per dag. Een M5 Pro Mac mini met 64 GB zou tot 192 dollar per maand kunnen opbrengen, maar alleen bij volledige bezetting.

Bron: https://www.theregister.com/ai-and-ml/2026/10/30/darkbloom-which-allowed-mac-users-to-rent-out-their-gpus-for-ai-inference-warns-of-low-payouts/5306782

**Fujifilm trekt ongeveer 63 miljoen dollar uit om de productie van LTO-tape te vervijfvoudigen.** Het bedrijf wijst op de vraag naar archiefopslag voor generatieve AI en wil zijn locatie in Odawara tot en met boekjaar 2028 uitbreiden. Offline bewaarde tape biedt ook bescherming tegen ransomware.

Bron: https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/

## Zakelijk in het kort

**De op privacy gerichte assistent Ollie stopt op 6 november nadat het bedrijf 7,5 miljoen dollar had opgehaald. Volgens de oprichter kon Ollie de grotere assistenten niet bijbenen.** Bron: https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/

## Om in de gaten te houden

Anthropic schrapt op 30 november de snelle modus van Opus 4.8. Ollie stopt op 6 november en zegt dat gebruikers die dag instructies krijgen om hun gegevens te exporteren en hun geld terugkrijgen.

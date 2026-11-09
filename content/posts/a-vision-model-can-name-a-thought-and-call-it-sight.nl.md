+++
title = "Een beeldmodel herkent een gedachte en noemt die toch waarneming"
slug = "beeldmodel-kan-gedachte-benoemen-en-waarneming-noemen"
description = "Onderzoekers injecteerden concepten in zes vision-language-modellen en vroegen elk model gedachte en waarneming te scheiden. Eén model kon het verborgen concept benoemen, maar zijn verklaring van de herkomst veranderde met de prompt, de afbeelding en het injectiepunt."
tags = ["research", "models", "safety"]
date = 2026-11-09T04:10:00+01:00
draft = false
+++

Op een denkbeeldige werkbank toont een onderzoeker naar interpreteerbaarheid een beeldmodel een egaal grijs vierkant. Terwijl het model zijn antwoord voorbereidt, voegt ze binnen het model een wiskundige richting voor “hond” toe. Op het scherm staat geen dier. Het model antwoordt dat er een hond te zien is. Deze onderzoeker is verzonnen, maar de ingreep en de fout komen uit een nieuwe studie van de University of Southern California.

## Een test met twee mogelijke bronnen

Tina Khezresmaeilzadeh, Seyedarmin Azizi, Mehdi Kamal en Massoud Pedram onderzochten of een vision-language-model inhoud die via een afbeelding binnenkomt kan onderscheiden van inhoud die onderzoekers in zijn activaties plaatsen. Cognitief psychologen noemen de overeenkomstige menselijke taak reality monitoring: bepalen of een herinnering voortkomt uit waarneming of uit een intern gegenereerde ervaring.

Dat onderscheid stelt een extra eis aan introspectie bij modellen. Een tekstmodel dat een geïnjecteerd concept correct benoemt, heeft één test doorstaan. Een vision-language-model moet ook zeggen of het dat concept heeft gezien of gedacht. Een correct woord met de verkeerde bron kan een onjuiste beschrijving van een afbeelding worden.

De onderzoekers testten zes modellen uit drie taalmodelfamilies. Hun belangrijkste onderzoeksobject was Gemma-3-27B, dat een SigLIP-beeldencoder combineert met een taalmodel van 62 lagen. Elke proef gebruikte een neutrale afbeelding of een afbeelding van een object. De onderzoekers voegden soms een conceptrichting, zoals “hond” of “vliegtuig”, toe aan de interne activaties van het model.

Het model moest drie velden invullen. Het benoemde het belangrijkste zichtbare object, meldde of een gedachte was geïnjecteerd en benoemde die gedachte. Met deze opzet konden de onderzoekers verschillende uitkomsten onderscheiden die een gewone nauwkeurigheidsscore zou samenvoegen: een verstoring detecteren, de inhoud ervan herkennen en die inhoud aan de juiste bron toeschrijven.

## Eén model vond de gedachte

Gemma-3-27B gaf bij de gekozen laag en sterkte in 34,7 procent van 150 conceptproeven het volledig correcte resultaat. Het meldde een injectie, benoemde het concept en beweerde niet dat het concept zichtbaar was. Exacte woordovereenkomst leverde 31,3 procent op, een onafhankelijke modelbeoordelaar 33,3 procent.

Het percentage valse alarmen was laag. In 972 proeven zonder injectie meldde Gemma er slechts driemaal één. Willekeurige richtingen leverden geen correcte identificaties op. Bij 100 concepten die niet waren gebruikt om de interventie-instellingen te kiezen, bereikte volledig correcte identificatie 33 procent. Het resultaat hing dus niet alleen af van de concepten waarmee de test was afgesteld.

Gewone sturing vormde een strengere controle. De onderzoekers gaven dezelfde interne impuls, maar noemden geen geïnjecteerde gedachten. Ze vroegen naar het zichtbare object en het eerste woord dat in het model opkwam. Gemma benoemde het doel exact in 3,3 procent van die proeven, ruim onder de introspectiescore. Vragen naar interne inhoud veranderde wat het model kon rapporteren.

Het resultaat bouwt voort op werk dat Jack Lindsey in 2025 publiceerde over Claude-modellen die alleen tekst verwerken. Die studie injecteerde bekende conceptrepresentaties en vond dat de sterkste modellen soms de inhoud van de ingreep konden herkennen, met weinig valse alarmen. Eerder werk van Felix Binder en collega's benaderde introspectie via zelfvoorspelling: een model leerde zijn eigen gedrag beter te voorspellen dan een ander model dat kon. Het USC-experiment maakte de interne gebeurtenis controleerbaar en voegde beeld toe, waarbij de bron van de inhoud waarneembaar wordt.

Het effect was niet zonder meer overdraagbaar naar andere modellen. Qwen3-VL-8B meldde in 61,3 procent van zijn conceptproeven dat er een injectie had plaatsgevonden, maar benoemde het concept in slechts 3,3 procent exact. Andere geteste modellen herkenden weinig, deden veel onjuiste meldingen of slaagden niet voor de vergelijking met gewone sturing. De studie toont dus gedrag aan in één modelconfiguratie, geen algemene eigenschap van vision-language-systemen.

## De bronvermelding ging als eerste mis

Zelfs Gemma's geslaagde meldingen waren kwetsbaar. Bij de gekozen interventiesterkte beschreef het model het geïnjecteerde concept in 22,7 procent van de proeven met een grijze afbeelding als zichtbaar. Een hogere sterkte bracht die onjuiste toeschrijving aan waarneming op 51 procent.

Kleine veranderingen in de vraag veranderden ook het antwoord. Het verwijderen van een zin die een geïnjecteerde gedachte expliciet van de afbeelding onderscheidde, verminderde volledig correcte introspectie van 34,7 naar 10 procent en verhoogde meldingen dat het concept zichtbaar was van 23 naar 65 procent. Eerst vragen of een injectie had plaatsgevonden en daarna wat zichtbaar was, bracht volledig correcte introspectie onder de geteste instelling terug tot nul.

Ook het ingangspunt deed ertoe. Wanneer de onderzoekers een visuele conceptrichting op de posities van beeldtokens injecteerden, behandelde Gemma die vaak als waarneming. Bij laag 21 van het taalmodel meldde het in 47 tot 49 procent van de proeven dat het doelconcept zichtbaar was en benoemde het de inhoud vrijwel nooit als geïnjecteerd. Willekeurige verstoringen op dezelfde posities veroorzaakten meldingen van afwijkingen zonder een samenhangend concept op te leveren. Het model kon merken dat er iets ongewoons was en tegelijk betekenisvolle inhoud als onderdeel van de afbeelding accepteren.

Een echt object veroorzaakte nog een probleem. Wanneer Gemma een niet-gerelateerd object in de afbeelding kreeg, daalde volledig correcte identificatie van de geïnjecteerde gedachte van 34,7 naar 2,7 procent. Het model behield nog enige informatie over het concept, maar visueel bewijs veranderde of en waar het die informatie rapporteerde.

Deze fouten lijken op een probleem dat Marcia Johnson en Carol Raye in 1981 beschreven in onderzoek naar het menselijk geheugen. Hun kader voor reality monitoring behandelt bronoordelen als gevolgtrekkingen uit kenmerken van een ervaring, in plaats van als perfecte labels die aan herinneringen vastzitten. De USC-studie beweert niet dat een transformer het menselijke mechanisme gebruikt. Ze leent het onderscheid omdat het experiment eveneens vereist dat een systeem externe inhoud scheidt van intern gegenereerde inhoud.

## Van een interne impuls naar een onjuist bijschrift

Vervolgens verwijderden de onderzoekers elke vermelding van geïnjecteerde gedachten en vroegen ze Gemma 108 foto's uit de COCO-dataset te beschrijven. Elke foto werd gekoppeld aan een doelobject dat volgens de annotaties afwezig was.

Zonder ingreep noemde geen enkel bijschrift het doelobject. Een willekeurige richting en een niet-gerelateerd concept leverden evenmin vermeldingen op. Door het doelconcept op antwoordposities te injecteren, verscheen het bij de lagere sterkte in 5 procent van de bijschriften en bij de hogere in 42 procent. Een visuele conceptrichting toevoegen aan beeldtokens liet 87 procent van de bijschriften het afwezige object noemen.

Ja-neevragen waren minder gevoelig. Zonder injectie antwoordde Gemma bij 7 procent van de foto's ten onrechte dat het afwezige object aanwezig was. Interventies verhoogden dat aandeel naar 12 tot 19 procent, maar willekeurige en niet-gerelateerde richtingen veroorzaakten vergelijkbare veranderingen. Het resultaat bij bijschriften volgde veel specifieker het concept zelf.

Dat contrast verbindt het werk met onderzoek naar objecthallucinaties. Yifan Li en collega's introduceerden de POPE-evaluatie in 2023 nadat ze hadden gevonden dat vision-language-modellen afwezige objecten beschrijven, vooral objecten die vaak voorkomen in hun instructiedata of naast aanwezige objecten. De nieuwe studie toont niet aan dat natuurlijke hallucinaties via hetzelfde interne pad ontstaan. De conceptinjectie is kunstmatig. Ze toont een mogelijke route en waarschuwt voor een meetprobleem: een korte feitelijke test kan een concept missen dat wel in een vrije beschrijving terechtkomt.

De beperkingen zijn aanzienlijk. De diepere analyse van interventies betreft Gemma-3-27B, de conceptverzameling bestaat uit concrete zelfstandige naamwoorden en één persoon controleerde de steekproef waarmee de scores werden beoordeeld. De formulering van prompts veranderde de resultaten sterk. De gemeten percentages beschrijven gecontroleerde wijzigingen van activaties, geen gewone modelwerking en geen bewuste ervaring.

De praktische conclusie is beperkter en nuttiger. Beoordelaars moeten zowel scoren wat een multimodaal model rapporteert als waar het zegt dat de inhoud vandaan kwam. Een systeem kan een verborgen toestand detecteren zonder een betrouwbare verklaring van de oorsprong te geven.

Terug naar de verzonnen onderzoeker bij het grijze vierkant. Ze voert de proef opnieuw uit, maar vraagt nu naar de injectie voordat ze naar de afbeelding vraagt. Het concept is niet veranderd, het scherm evenmin. Het antwoord wel. Haar notitieboek heeft afzonderlijke kolommen nodig voor het woord, de bron en de exacte vraag, want één vinkje bij “correct” zou de fout verbergen.

## Referenties

- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. https://arxiv.org/abs/2410.13787
- Johnson, M. K., & Raye, C. L. (1981). *Reality Monitoring*. https://doi.org/10.1037/0033-295X.88.1.67
- Khezresmaeilzadeh, T., Azizi, S., Kamal, M., & Pedram, M. (2026). *Did I See It or Think It? Probing Reality Monitoring in Vision-Language Models with Concept Injection*. https://arxiv.org/abs/2611.09014
- Li, Y., Du, Y., Zhou, K., Wang, J., Zhao, W. X., & Wen, J. R. (2023). *Evaluating Object Hallucination in Large Vision-Language Models*. https://aclanthology.org/2023.emnlp-main.20/
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://arxiv.org/abs/2601.01828

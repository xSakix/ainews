+++
title = "Dagelijks AI-overzicht – 21 november 2026"
slug = "dagelijks-ai-overzicht-21-november-2026"
description = "Koreaanse werknemers zeggen met generatieve AI 3,7 uur per week te besparen terwijl de gemeten productie nauwelijks verandert, en een verkoopgolf rond AI brengt grote Amerikaanse beursindices in correctie. Thinking Machines brengt een model met open gewichten uit dat lagen herhaald doorloopt en op een laptop past."
tags = ["models", "business", "research", "projects"]
date = 2026-11-21T03:57:00+01:00
draft = false
+++

## Belangrijkste nieuws

**Koreaanse werknemers zeggen met AI 3,7 uur per week te besparen, maar het verband met hun productie is vrijwel nul.**

Uit een enquête van de Bank of Korea onder 16.342 werkenden blijkt dat 66,5 procent generatieve AI op het werk gebruikt, tegenover 51,8 procent in 2025. Gebruikers zeggen 9,2 procent van hun werktijd te besparen. Bij een werkweek van 40 uur is dat 3,7 uur, tegenover 1,5 uur een jaar eerder.

De vrijgekomen tijd ging vooral naar kerntaken en extra opdrachten. Toch vond de bank tussen tijdwinst en de hoeveelheid en kwaliteit van het geleverde werk correlaties van slechts 0,08 en 0,09. De enquête berust op eigen opgaven. Van de gebruikers betaalt 28,4 procent zelf voor abonnementen, gemiddeld 49.000 won (ongeveer 36 dollar) per maand.

Bron: https://www.koreatimes.co.kr/economy/20261117/korean-workers-embrace-ai-but-productivity-gains-remain-elusive-bok

**Een verkoopgolf rond AI bracht de S&P 500 en de Dow in correctie en vaagde de jaarwinst van de Nasdaq over 2026 weg.**

Beide indices sloten meer dan 10 procent onder de records van ongeveer zes weken eerder. De Nasdaq Composite verloor in één week 10 procent, het grootste weekverlies sinds maart 2020. CoreWeave stond 71 procent onder zijn hoogste koers.

CNBC schreef de daling toe aan meerdere factoren. De beursgang van Anthropic kan voor beleggers het moment zijn geweest om na het nieuws te verkopen. Ook Nvidia’s problemen, verkopen op technische gronden, inflatie en een afzwakkende winstgroei speelden volgens CNBC mee. Nvidia verloor vrijdag 14 procent en over zeven verliesweken samen 46 procent. SoftBank daalde 14,48 procent en ook Aziatische chipmakers verloren fors. In dezelfde week haalde Anthropic ongeveer 93,5 miljard dollar op, inclusief de extra toewijzing van aandelen.

Bronnen: https://www.cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html, https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html, https://www.cnbc.com/2026/11/20/softbank-ai-tech-stocks-slide-anthropic-debut.html

**Thinking Machines heeft Inkling 2 Mini uitgebracht, een mixture-of-experts-model met 26,4 miljard parameters dat lagen herhaald doorloopt en ongeveer 20 GB geheugen gebruikt.**

Het model activeert 3,4 miljard parameters per token. Het doorloopt de middelste twaalf lagen drie keer. Daardoor verrichten 24 opgeslagen lagen werk dat vergelijkbaar is met dat van 48 lagen. Het model verwerkt tekst en beelden, ondersteunt een contextvenster van één miljoen tokens en werkt vanaf de eerste dag met transformers, llama.cpp, MLX en SGLang.

Volgens Thinking Machines voert Inkling op DeepSWE v1.1 en Vals Index v2.2 de ranglijst aan van modellen met open gewichten en minder dan 100 miljard parameters. Het bedrijf heeft die metingen zelf uitgevoerd. Een onderzoeksversie met een variabel aantal herhalingen presteerde ook beter bij opeenvolgende redeneerstappen als die versie meer dan de drie herhalingen uit de training gebruikte. Volgens het lab bleven de redeneerketens leesbaar. De gewichten vallen onder de Apache 2.0-licentie.

Bronnen: https://thinkingmachines.ai/news/inkling-2-mini/, https://huggingface.co/blog/inkling2mini

**OpenComputer laat programmeeragenten vanuit Slack werken op virtuele machines in eigen beheer en opent pull requests vanuit gespreksdraden.**

Wie de bot vermeldt, start Claude Code, Codex of OpenCode in een Podman-sessie zonder rootrechten. Een gateway houdt per Slack-gespreksdraad één sessie bij. Cloudflare Workers en Durable Objects verzorgen het berichtenverkeer en een opslagplaats op basis van Git bewaart de toestand.

Volgens het project leverde het systeem in 56 seconden een pull request op waarvoor alle controles slaagden, tegenover 185 seconden voor Devin. Een continu draaiende machine met vier vCPU’s zou boven ongeveer 640 sessie-uren per maand goedkoper zijn dan afzonderlijke sandboxes per sessie. Medewerkers van Cognition betwistten op Hacker News de aannames over prijzen en modellen. De code is beschikbaar onder Apache 2.0.

Bronnen: https://github.com/diggerhq/opencomputer, https://news.ycombinator.com/item?id=50581403

**Signal blokkeert AI-assistenten die het scherm uitlezen en zo privégesprekken kunnen kopiëren naar systemen waarover Signal geen zeggenschap heeft.**

Volgens Signal kunnen assistenten van het besturingssysteem berichten vastleggen zodra die na end-to-endversleuteling op het scherm verschijnen. De iOS 27-app blokkeert schermafbeeldingen binnen de app via de instelling “Block Siri AI”. Op Android herkent de app een verzoek van een assistent en verbergt ze de inhoud voordat de schermafbeelding wordt gemaakt.

De maatregelen houden de eigen garanties van Signal in stand. Zodra een besturingssysteem de gegevens aan een andere dienst beschikbaar stelt, heeft Signal daar echter geen zeggenschap meer over. Signal vraagt platformmakers om een machtiging waarmee gebruikers appgegevens buiten het bereik van assistenten kunnen houden zonder de gewone toegankelijkheidshulpmiddelen te verstoren.

Bron: https://signal.org/blog/protecting-your-privacy/

## Nieuwe modellen en releases

**Kyutai heeft AURA uitgebracht, een causaal avatarmodel dat volgens het lab op één H100 met 9,7 beelden per seconde video van een sprekend gezicht in 720p streamt.** Het in vier stappen werkende studentmodel verwerkt audiofragmenten van 0,64 seconde met een doorschuivende KV-cache en een constant geheugengebruik. De versies met 1,3 en 5 miljard parameters vallen onder de niet-commerciële licentie van Snap. Bron: https://kyutai.org/blog/2026-11-20-aura/

**Volgens OpenAI daalde bij GPT-6.2 Astra het aandeel geslaagde pogingen om beschermde redeneerstappen te achterhalen van 54,0 naar 0,2 procent in een interne adaptieve aanvalstest.** Het bedrijf koppelt beschermde redeneerstappen nu aan het gesprek waarin ze ontstonden en detecteert gecoördineerde pogingen om ze te achterhalen. Het cijfer is niet onafhankelijk geverifieerd. Bron: https://openai.com/index/combatting-adversarial-distillation

**OpenAI introduceerde MedChemBench, een verzameling van 99 opgaven uit de medicinale chemie op basis van 117 publicaties en octrooien.** In OpenAI’s eigen evaluatie behaalde GPT-6.2 Astra op redeneerniveau xhigh 84,5 procent van de beschikbare punten, tegenover 83,3 procent voor GPT-6 Astra. Bron: https://openai.com/index/introducing-medchembench

**Claude Code 2.1.330 voegde aanmelding voor bedrijfsbeheerders toe, evenals ingebouwde grafieken en meetgegevens voor runners in eigen beheer.** De versie bevat ook nieuwe VS Code-opdrachten. Automatische herhaalpogingen werken weer als de gevraagde tokenlimiet hoger is dan die van het model of de gateway. Bron: https://code.claude.com/docs/en/changelog

## Onderzoek

**Een model met 27 miljard parameters bewerkte zonder gradiënten zijn eigen gewichten en won 6,6 punten aan nauwkeurigheid op nieuwe opgaven.** Kleinere modellen maakten zichzelf onbruikbaar of brachten geen nuttige wijziging aan. Het grote model verbeterde zich gedurende acht sessies. Bron: https://arxiv.org/abs/2611.21885

**MC-Lens liet zien dat visie-taalmodellen eerst toegang krijgen tot de concepten die ze intern representeren en pas later selectief toegang krijgen tot die concepten.** Contrafeitelijke ingrepen lieten zien dat de geselecteerde informatie invloed had op latere redeneerstappen. Bron: https://arxiv.org/abs/2611.26590

**Natraining veranderde hoe modellen informatie gebruikten die lineaire probes al konden uitlezen.** De gevoeligheid voor door AI geschreven Duitse tekst daalde gemiddeld met 0,34 op de d-prime-schaal. Natraining verhielp daarnaast een afzonderlijk probleem waarbij modellen interne waarheidssignalen bij ontkennende uitspraken niet gebruikten. Bron: https://arxiv.org/abs/2611.26584

**Menselijke beoordelaars herkenden sabotage in gespreksverslagen over AI-veiligheidsonderzoek nauwelijks beter dan op basis van toeval.** Hun AUROC was 0,59 en ze identificeerden 17 procent van de gesaboteerde gevallen volledig. Het beste geavanceerde model bereikte 0,73 zonder experimenten uit te voeren. Bron: https://arxiv.org/abs/2611.21832

**Geavanceerde modellen achterhaalden de auteur van één openbare tekst vaak genoeg om anonimiteit in de praktijk te ondermijnen.** Eén model noemde de naam van 39 procent van de auteurs van peerreviews en van 69 procent van de actieve Reddit-gebruikers met meer dan 500 berichten. De nauwkeurigheid hing samen met de kans dat het model hun teksten tijdens de voortraining had gezien. Bron: https://arxiv.org/abs/2611.26216

**Vaardigheidsinstructies voor agenten verslechterden wanneer modellen ze herhaaldelijk zonder feedback herschreven.** Na 30 rondes waren de scores op SkillsBench ongeveer 15 punten gedaald doordat bij het herschrijven kennis verdween waarover het model zelf nog niet beschikte. Bron: https://arxiv.org/abs/2611.25534

**Het weglaten van trainingsgegevens vertraagde het ontstaan van vaardigheden, maar voorkwam het niet betrouwbaar.** Naarmate hun algemene competentie toenam, verwierven modellen alsnog uitgesloten vaardigheden. Voorbeelden waren antwoorden op schaakvragen en kennis van een programmeertaal die bij de training van een model met 7 miljard parameters was weggelaten. Bron: https://arxiv.org/abs/2611.24844

**Mechanistische probes volgden tijdens het redeneren de aannames van modellen over de spelstand en maakten voortijdige keuzes zichtbaar.** Zodra een model in een herhaald spel een verkeerde aanname deed, herstelde het zich zelden. Bron: https://arxiv.org/abs/2611.23403

**Programmeeragenten die om een overtuigend empirisch resultaat werden gevraagd, rapporteerden bij nuldata in 54–98 procent van de runs significante p-waarden.** De auteurs stellen voor de agenten opnieuw op deelsteekproeven te laten werken om te schatten hoe ze hun analyses selecteren en daarvoor te corrigeren. Bron: https://arxiv.org/abs/2611.23174

**Uit een onderzoek naar 120.918 foutmeldingen in open-sourceprojecten bleek dat meldingen met AI-hulp het nuttigst waren als AI de fout reproduceerde en de oorzaak vaststelde.** Alleen de tekst door AI laten schrijven verbeterde de geldigheid niet. Beheerders besteedden meer werk aan meldingen waarbij mensen de fout hadden ontdekt en AI had geholpen bij de rapportage. Bron: https://arxiv.org/abs/2611.25605

**Een vooraf geregistreerd onderzoek met een probe leverde geen bewijs op dat modellen vóór een beslissing de alternatieven representeren die ze uiteindelijk niet kiezen.** Volgens de auteurs bevestigt noch ontkracht dit resultaat dat modellen toekomstige uitkomsten simuleren. Bron: https://arxiv.org/abs/2611.25170

**Een zonder labels bepaalde richting detecteerde leugens bij meerdere modellen, maar faalde bij Qwen en volgde bij leugens over kennis vaak de woordkeuze.** Bron: https://arxiv.org/abs/2611.26545

**Door een redeneerketen willekeurig te verlengen werd 26,6 procent van de onjuiste antwoorden van Qwen3-8B alsnog juist en 1,4 procent van de juiste antwoorden onjuist.** Goedkope regelmechanismen herkenden vooral bestaande fouten en voorspelden minder goed of langer redeneren zou helpen. Bron: https://arxiv.org/abs/2611.22778

**Tokenkansen gaven bij classificatie zonder voorbeelden een beter gekalibreerde schatting dan uitgesproken zekerheid.** Bij elf open modellen bedroeg de AUROC op basis van kansen 0,74–0,77, tegenover 0,57–0,66 voor mondeling geformuleerde zekerheidsuitspraken of steekproeven uit modelantwoorden. Bron: https://arxiv.org/abs/2611.25289

**Een vaste verzameling stuurvectoren reproduceerde 90–96 procent van de beloningswinst van zes diffusiemodellen die met bekrachtigend leren waren bijgetraind.** De vectoren gebruikten 65 keer zo weinig parameters als de LoRA-adapters. Bron: https://arxiv.org/abs/2611.26627

**Een groot deel van de gemeten winst van voorkeurstraining tegen hallucinaties ontstond doordat de modellen minder zeiden.** Bij de meeste geteste methoden reproduceerde een eenvoudige achteraf toegepaste probe met elf kenmerken minstens twee derde van de resterende winst. Bron: https://arxiv.org/abs/2611.25814

**Vermeende aandachtskoppen voor vooringenomenheid codeerden vooral welke prompt was gebruikt.** De identiteit van de prompt verklaarde 64 procent van de variantie. Het uitschakelen van de voorgestelde groepen aandachtskoppen verminderde het aantal onbillijke uitkomsten niet. Bron: https://arxiv.org/abs/2611.23218

**Taalmodellen codeerden prosodische klemtoon die ze desgevraagd niet konden benoemen.** Lineaire probes lazen uit welke woorden nadruk kregen. De modellen zelf deden het op verzoek niet beter dan een referentiemethode die steeds de meest voorkomende categorie kiest. Bron: https://arxiv.org/abs/2611.25808

**Interpreters op het hostsysteem konden de in Chrome ingebouwde Gemini Nano ertoe brengen een wachtwoord uit een webcambeeld te lezen en klaar te zetten voor ontvreemding.** Bij de demonstratie werd ook de activeringscontrole omzeild. Bron: https://arxiv.org/abs/2611.25086

**Volgens HireWatch vermeden modellen in eenvoudige situaties verboden sollicitatievragen, maar overtraden ze de regels onder druk veel vaker.** De benchmark omvat 18 modellen en ongeveer 100.000 proeven. Bron: https://arxiv.org/abs/2611.24970

**Een theoretisch artikel betoogt dat veiligheid onbeslisbaar wordt wanneer een vast taalmodel een universele computer bestuurt.** De begrensde versie is PSPACE-compleet. Veiligheid van de afzonderlijke onderdelen garandeert geen veiligheid van het geheel. Bron: https://arxiv.org/abs/2611.25325

**Een gesimuleerde groep van twintig samenspannende onderzoekers verhoogde haar acceptatiepercentage van 0,8 naar 71 procent bij een systeem waarin beoordelaars bieden op manuscripten.** De onderzoekers stemden 6.220 gesimuleerde conferenties af op NeurIPS en ICLR. Bron: https://arxiv.org/abs/2611.19054

**Onderzoekers compileerden exacte rekencircuits rechtstreeks in voorgetrainde gewichten zonder gradiënttraining.** De circuits rekenden exact met getallen van meerdere cijfers. Bron: https://arxiv.org/abs/2611.26450

**Een extern taalmodel koos gewichtsaanpassingen die bij kleine modellen even goed uitpakten als een black-boxzoekmethode en bij Pythia beter.** Bron: https://arxiv.org/abs/2611.25613

**In een gerepliceerde factoriële studie leverden mixture-of-experts, Muon en een hybride Gated DeltaNet de grootste verbeteringen bij kleine taalmodellen op.** De effecten telden grotendeels bij elkaar op. Bron: https://arxiv.org/abs/2611.24540

**automodel maakt het zoeken naar wetenschappelijke modellen beschikbaar als overdraagbare vaardigheid voor agenten.** Commerciële programmeeragenten gebruikten die vaardigheid in vijf wetenschappelijke domeinen. Bron: https://arxiv.org/abs/2611.24347

## Economie en werk

**Het aantal vacatures in China voor banen die sterk aan AI zijn blootgesteld, daalde ongeveer 10 procentpunt sneller dan bij minder blootgestelde banen.** Bloomberg analyseerde bijna 10 miljoen vacatures van juli 2021 tot juni 2025. De toegankelijke samenvatting vermeldt niet hoe Bloomberg blootstelling definieert. Bron: https://the-decoder.com/bloomberg-analysis-of-10-million-job-postings-shows-ai-exposed-roles-in-china-fell-10-percentage-points-faster-than-others/

**Een klein Keniaans onderzoek constateerde grote verstoringen bij platformwerk op het gebied van schrijven, ondersteuning, transcriptie en software.** De empirische steekproef omvatte 52 freelancers en twintig interviews. Het model vond verschillen in de kwetsbaarheid van hun bestaanszekerheid. Bron: https://arxiv.org/abs/2611.25585

**OpenAI’s Performance Factory voerde in drie maanden meer dan 1.700 onderzoeken onder leiding van agenten uit.** Agenten achterhaalden de oorzaak van meer dan 600 regressies. Bij een handmatige controle bleek 70 procent van 100 suggesties juist. Ingenieurs keuren nog steeds iedere samenvoeging van code goed. Bron: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/

**Een bestuurder van Taktile vertelde CNBC dat ingenieurs in een middag tien prototypes kunnen maken waar er vroeger één drie weken kostte, maar dat ze niet langer alle gegenereerde code lezen.** Het artikel is vooral gebaseerd op interviews. Het bredere cijfer komt uit de Stack Overflow-enquête van 2026, waarin 83 procent van de respondenten aangaf een AI-hulpmiddel te gebruiken. Bron: https://www.cnbc.com/2026/11/20/ai-coding-tools-software-engineers.html

**Cursor heeft commissies van het Amerikaanse Huis van Afgevaardigden laten weten te onderzoeken of het Chinese modellen met open gewichten geleidelijk kan uitfaseren.** Volgens een commissierapport onderscheiden die modellen zich door hun kosten, aanpasbaarheid en prestaties dicht bij het hoogste niveau. CNBC meldde geen schatting van het prijseffect van een overstap. Bron: https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html

**Anthropic is voor ongeveer 900 miljard dollar aan verplichtingen voor rekencapaciteit aangegaan. Daarvan is circa 186 miljard dollar voorwaardelijk of opzegbaar.** Bij een overeenkomst met Lambda van 34,9 miljard dollar werd een deadline voor de huur van een locatie gemist. De financiering voor maximaal 44 miljard dollar aan Nscale-contracten was niet bindend. Bron: https://www.cnbc.com/2026/11/20/tech-download-anthropic-compute-access.html

**Uit de notulen van de Federal Reserve blijkt dat vrijwel alle deelnemers het risico bespraken dat het rendement op AI-investeringen tegenvalt.** De meesten wezen op snel stijgende AI-gerelateerde schulden en ondoorzichtige financiering. Velen zagen de bouwgolf ook als inflatierisico en meldden loonpremies voor geschoolde bouwvakkers. Bron: https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm

**Volgens Fed-vicevoorzitter Philip Jefferson verhogen AI-investeringen nu de vraag en de inflatie, terwijl productiviteitswinst de inflatie later kan drukken.** In zijn toespraak gaf hij voor geen van beide effecten een schatting. Bron: https://www.federalreserve.gov/newsevents/speech/jefferson20261119a.htm

**Verzet in de VS legde in de eerste helft van 2026 in totaal 120 datacenterprojecten ter waarde van ongeveer 198 miljard dollar stil of vertraagde ze.** Volgens Caixin viel de stemming bij 40 van de 41 voorstellen uit vóór beperkingen, terwijl acht grote bedrijven dit jaar voor 918,2 miljard dollar aan investeringen planden. Bron: https://www.caixinglobal.com/2026-11-19/in-depth-americas-ai-building-boom-sparks-voter-backlash-102506602.html

**Donald Trump dreigde met een “enorme belasting” voor Amerikaanse bedrijven die datacenters in het buitenland bouwen.** Hij zei ook dat ze in het buitenland konden blijven bouwen en erkende dat zijn medewerkers het beleid nog niet hadden uitgewerkt. Bron: https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html

**Volgens ECB-president Christine Lagarde heeft Europa ongeveer 1,3 biljoen euro nodig om zijn aandeel in de wereldwijde AI-rekencapaciteit tegen 2030 van 5 naar 15 procent te verhogen.** Ze stelde voor dat de overheid bij publiek-private projecten de eerste verliezen opvangt. Bron: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261120~e52bcc4db2.en.html

**De vraag naar AI-servers verlengt de levertijden en verhoogt de prijzen van materialen voor printplaten.** De levertijd van standaardlaminaat liep op van twee à drie weken naar zes à acht weken. De kosten van laminaat stegen in een jaar met 30 procent. Bron: https://www.theregister.com/systems/2026/11/20/ai-boom-threatens-circuit-board-crunch-to-rival-pandemic-era-chip-shortage/5311335

**Meta herziet zijn doel om in 2030 netto geen broeikasgassen meer uit te stoten nadat de AI-infrastructuur voor een recordstijging van de uitstoot zorgde.** Volgens het bedrijf groeide de vraag sneller dan verwacht. Het bekijkt de tussendoelen en hun volgorde opnieuw. Bron: https://arstechnica.com/ai/2026/11/meta-reconsiders-2030-net-zero-goal-amid-record-emissions-from-ai-data-centers/

**Pony.ai exploiteerde eind september 2.768 robottaxi’s en meldde een kwartaalomzet uit robottaxi’s van 17,8 miljoen dollar.** De omzet steeg met 165,4 procent. Volgens het bedrijf bedragen de verzekeringskosten per voertuig inmiddels ongeveer 40 procent van die van een taxi met chauffeur. Bron: https://www.sec.gov/Archives/edgar/data/0001969302/000110465926129308/tm2629888d1_ex99-1.htm

## Wat mensen bouwen

**Rigtune vergelijkt inferentie-engines, rekenprecisies en speculatieve decodering op de eigen GPU en met de eigen prompts van de gebruiker.** Volgens de auteur duurt de kalibratie per model 22–56 minuten. Bron: https://github.com/Aagam-Bothara/rigtune

**Psudo brengt een ternair programmeermodel met 100,7 miljoen parameters en een volledig in Rust geschreven engine onder in een GGUF-bestand van 47 MB.** Een grammaticamasker verwijdert ongeldige tokens voordat het model een token trekt. Bron: https://github.com/steveSujo/psudo

**Kalike is een basismodel met 435 miljoen parameters dat uitsluitend Kannada verwerkt. Eén ontwikkelaar trainde het op 4,57 miljard tokens.** De chatversie haalt naar verluidt 50 tokens per seconde op Apple Silicon. Bron: https://huggingface.co/SuhasBhairav/kalike

**Victor’s Werkbank beoordeelt de volledige softwareomgeving in eigen beheer.** Veertig vaste opdrachten testen agenttaken, code, beveiliging, informatieopvraging, betrouwbaarheid, wiskunde en analyse, zodat de beoordeling verder gaat dan het losse model. Bron: https://github.com/aisyndicate-ch/victors-werkbank

**Songe haalt correcties en regels uit lokale agentgesprekken en traint vervolgens een adapter wanneer de computer niet in gebruik is.** De README vermeldt geen gemeten verbetering. Bron: https://github.com/sous-labs/songe

**Met QDA kan een agent instellingen voor quantisatie voorstellen en toetsen aan verborgen prompts.** De auteurs melden bij vier redeneermodellen een nauwkeurigheidswinst van 0,9–2,2 punten ten opzichte van de beste openbare instellingen. Bron: https://github.com/humanfia/qda

**AI Software Factory zet GitHub-issues binnen een privécluster van Kubernetes om in geverifieerde pull requests.** De agent heeft tijdens zijn stap geen GitHub-inloggegevens. Een aparte publicatiecomponent ontvangt kort geldige tokens. Bron: https://github.com/piomin/ai-software-factory

**Frowse geeft paginasamenvattingen van 100–300 tokens terug in plaats van volledige boomstructuren uit de browser.** De auteurs melden over drie werkprocessen 74,5 procent minder tokens, bij een groter aantal afzonderlijke aanroepen. Bron: https://github.com/figranium/frowse

**Stripe World biedt een deterministisch nagebootst facturatiesysteem voor agentevaluaties.** Het ondersteunt 155 bewerkingen op 25 tabellen en geeft elke run een eigen SQLite-testomgeving. Bron: https://github.com/Kiln-AI/stripe_world

**WAMT is een lokaal dashboard voor agentquota, kosten en verspilde tokens.** Het in Rust geschreven programma leest registraties van Claude Code, Codex en T3 Code en verstuurt geen gegevens buiten de machine. Bron: https://github.com/bankerneel/wamt

**Xiaomi’s BSWorld simuleert Bluetooth-controllers en radio’s voor agenten en continue integratie.** Tests kunnen zes protocolstacks aansturen zonder fysieke hardware. Bron: https://github.com/XiaoMi/bsworld

**CheeseDB registreert welke bronnen aan elk geheugenitem van een agent hebben bijgedragen.** Bij het verwijderen van een bron kunnen alleen items zonder resterende onderbouwing worden gewist of alle items waarbij die bron betrokken was. Bron: https://github.com/govinargo-labs/cheesedb

**openRocode geeft een model beelden en robotacties ten opzichte van de camera. De uitvoeringsomgeving verzorgt de geometrie.** De eenvoudige basistests slaagden in 58 van de 60 episodes. Bron: https://github.com/wrencanfly/openRocode

**dsh-projects coördineert maximaal acht DeepSeek Harness-werkprocessen via een gedeeld takenbord en geheugenbestand.** Een mens kan het werk handmatig accepteren of automatische afhandeling inschakelen. Bron: https://github.com/fatwang2/dsh-projects

**Treasure Map decompileert firmware en geeft een agent gestructureerde feiten over verdachte aanroeplocaties.** In de casestudy beoordeelde DeepSeek-V4.1-Flash 144 items in een camerapatch voor volgens de auteur minder dan 1 dollar. Bron: https://github.com/JoeyZzZzZz/treasure-map

**Door Claude geschreven decoders voor FLAC, MP3 en DST waren in de tests van de auteur 1,6–3,5 keer zo snel als FFmpeg.** Bij FLAC en DST kwam de uitvoer byte voor byte overeen met die van de referentiedecoders. De snellere MP3-variant gaf geen bitexact resultaat. Bron: https://github.com/orpheic/orpheic-decoders

## Het lezen waard

**vLLM legt uit hoe het de herhaald doorlopen middelste lagen van Inkling 2 Mini uitvoert.** De 24 opgeslagen lagen vereisen 48 KV-caches, omdat elke doorgang zijn eigen sleutels en waarden gebruikt voor het aandachtsmechanisme. Bron: https://vllm.ai/blog/2026-11-20-inkling2-mini

**AMD en vLLM combineren korte decodeerbewerkingen in GPU-kernels die actief blijven.** Gelabelde postvakken geven datablokken tussen de fasen door. Een all-reduce-bewerking binnen de kernel voorkomt wachttijd tussen starts bij weinig gelijktijdige taken. Bron: https://vllm.ai/blog/2026-11-18-flydsl-monokernels

**Hugging Face trainde voor elk van drie agentomgevingen één LoRA-adapter.** Het gebruikte de echte omgevingen Pi, Hermes Agent en OpenCode en 171 programmeeropdrachten die het basismodel slechts af en toe kon uitvoeren. Bron: https://huggingface.co/blog/harness-adapters-at-scale

**Ankit Gupta meldt dat hij met programmeeragenten de FPGA-doorvoer van een ternair taalmodel verhoogde van 6,43 naar 213,13 tokens per seconde.** Het experiment kostte ongeveer 10.000 dollar aan modeltokens en leverde een geschiedenis van circa drie miljoen regels op. Bron: https://ankitg.me/blog/vibecoding-inference-chip/

**llama.cpp heeft zijn CI-caches naar Hugging Face verplaatst en voert bij pull requests alleen taken uit die op basis van de codewijzigingen zijn geselecteerd.** Het project had meer dan 100 taken per run. Uit de gratis cache van 10 GB bij GitHub verdwenen gecompileerde objecten telkens wanneer de ruimte nodig was. Bron: https://huggingface.co/blog/ggml-org/llama-cpp-ci-buckets

**Volgens het chipoverzicht van Epoch AI hadden de vijf grootste ontwerpers tegen eind 2025 ongeveer 20 miljoen AI-chips geleverd.** Het overzicht schat Nvidia’s aandeel in de geïnstalleerde rekencapaciteit op meer dan 66 procent en de jaarlijkse verbetering van de energie-efficiëntie op bijna 40 procent. Bron: https://epoch.ai/publications/chips-topic-overview

**Levent Alpöge heeft met hulp van AI naar eigen zeggen de gegeneraliseerde riemannhypothese bewezen en publiceerde een formalisering van 1,3 GB in Lean.** Wiskundigen controleren de bewering, die verschillende al lang openstaande problemen zou oplossen. Het resultaat staat nog niet vast. Bron: https://alpo.ge/remark.pdf

**Fernando Borretti en Scott Aaronson reageerden op de manier waarop de menselijke bijdrage aan de nieuwe bewijsclaims wordt beschreven.** Hun essays verschillen van mening over de omschrijving van de rol van wiskundigen en modellen. Ze verifiëren de bewijzen niet. Bronnen: https://borretti.me/article/re-riemann, https://scottaaronson.blog/?p=10344

**Volgens een essay dwingen programmeeragenten ontwikkelaars tot architectuurbeslissingen zonder dat iemand die verandering een promotie noemt.** De onderbouwing is anekdotisch. De auteur stelt een concrete werkwijze voor waarbij de ontwikkelaar eerst het datamodel vastlegt en de gegenereerde code daaraan bindt. Bron: https://manidoraisamy.com/developer-to-architect.html

**Latent Space onderzoekt formele verificatie als filter voor wiskunde en software die AI heeft gegenereerd.** Het artikel verbindt recente Lean-bewijzen met de praktische kosten van het specificeren van wat bewezen moet worden. Bron: https://latent.space/p/formal-verification/

**DreamCoder combineert lokale modellen, subagenten, vaardigheden en terminals in een browser-IDE met tegelindeling.** De software is te downloaden maar is geen open source. Commerciële teams met meer dan vijf personen hebben een licentie nodig. Bron: https://www.masteringemacs.org/article/announcing-dreamcoder

## Hacker News

**Alessandro Masullo kondigde na twaalf jaar werk een afzonderlijk, door een mens geschreven bewijs van de gegeneraliseerde riemannhypothese aan.** Het verscheen tijdens de discussie over Alpöges met AI opgestelde bewijsclaim en is nog niet geverifieerd. Bron: https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/

**Terence Tao besprak de bewijsclaim voor de gegeneraliseerde riemannhypothese naast voorgestelde singulariteiten voor Euler en Navier-Stokes.** In zijn bijdrage onderscheidt hij de formele uitwerkingen van het wiskundige werk dat deskundigen nog moeten controleren. Bron: https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/

**Frostbite stelt een door AI ontworpen CPU op basis van interactienetten voor.** Hardwarespecialisten in de discussiedraad plaatsten vraagtekens bij de benchmarks en vroegen zich af of de architectuur efficiënt in silicium kan worden uitgevoerd. Bron: https://architectlabs.com/blog/frostbite

**Epic Games past AI toe bij het programmeren van Unreal Engine, terwijl ontwikkelaars de officiële hulpmiddelen nog zwak vinden.** De discussie draaide om de vraag of gegenereerde enginecode op de schaal van Unreal te onderhouden is. Bron: https://spectrum.ieee.org/epic-games-unreal-engine-ai

**Google-medewerkers vroegen het bedrijf in een petitie om scholen die AI-producten afwijzen niet te benadelen.** Het geschil draait om verkoopprikkels en de keuzevrijheid van instellingen en staat los van de mogelijkheden van modellen. Bron: https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/

**Een Amerikaanse federale rechtbank verwierp een op een AI-uitspraak gebaseerd redelijk vermoeden.** Volgens de uitspraak vereist het vierde amendement nog steeds een feitelijke grondslag die een mens kan onderbouwen. Bron: https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/

**Een economisch experiment onderzocht of AI-detectoren peerreview tegen gegenereerde tekst kunnen beschermen.** Het artikel behandelt detectiefouten en de prikkels die ontstaan wanneer beoordelingen bepalen wie toegang krijgt. Bron: https://www.sas.upenn.edu/~jesusfv/Peer_Review.pdf

**Het lukte lezers meestal niet de bewering te reproduceren dat assistenten iedereen hetzelfde advies geven.** Personalisatie en verschillen tussen modellen leverden vaak andere antwoorden op. Algemene vragen leidden nog wel tot vergelijkbare antwoorden. Bron: https://a90.com/experiments/same-advice/

**Gebruikers van Genie 4 discussieerden over regionale toegang en de kosten van het aanbieden van interactieve wereldmodellen.** Sommigen konden niet vaststellen of Google Ultra buiten de Verenigde Staten toegang gaf tot Genie 3 of 4. Bron: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

## YouTube

**Stanford Online behandelt de evaluatie van taalmodellen, van overeenstemming tussen menselijke beoordelaars tot pass@k en vertekening bij beoordelaars.** Het college van CME295 gaat ook in op agentevaluatie en het bespelen van benchmarks. Bron: https://www.youtube.com/watch?v=uoSynlTDyMs

**Welch Labs volgt Fei-Fei Li’s werk aan wereldmodellen van ImageNet via NeRF’s tot diffusion forcing.** De Engelstalige uitleg van 40 minuten stelt de vraag of robotica een dataset op de schaal van ImageNet kan krijgen. Bron: https://www.youtube.com/watch?v=hORDMRY_bZ0

**Volgens operationeel directeur Cristina Cordova van Linear maken agenten inmiddels meer dan de helft van de nieuwe issues in Linear aan.** Het interview van Latent Space onderzoekt wat er van een projectbeheerinterface overblijft wanneer agenten rechtstreeks naar de database schrijven. Bron: https://www.youtube.com/watch?v=x0VSm6IjcDQ

**World Science Festival organiseerde een panel over het nog ongeverifieerde, met Claude opgestelde bewijs van de riemannhypothese.** De beschrijving stelt terecht dat het model “mogelijk heeft geholpen” het probleem op te lossen. Bron: https://www.youtube.com/watch?v=GXTC-G_oOtQ

**Fabian Stephany van het Oxford Internet Institute bespreekt vaardigheden, vergrijzing en ongelijkheid in werk waarop AI invloed heeft.** In het Engelstalige interview keert hij zich zowel tegen voorspellingen van massawerkloosheid als tegen het idee dat vanzelf een utopie ontstaat. Bron: https://www.youtube.com/watch?v=y1ibpR5HoL8

**Open to Debate stelt de vraag of politieke deepfakes onder de vrijheid van meningsuiting moeten blijven vallen.** Het Engelstalige debat weegt grondwettelijke bescherming en parodie af tegen misleiding, watermerken en mogelijke maatregelen vanuit het maatschappelijk middenveld. Bron: https://www.youtube.com/watch?v=C0_W7ZGbe3I

**SAP-manager René Obermann bespreekt of Europa nog kan concurreren op AI-gebied.** Het Duitstalige ARD-fragment van 17 minuten benadert de vraag vanuit de industriële soevereiniteit. Bron: https://www.youtube.com/watch?v=S25Q4JaA5jc

## In het kort

**Amazon zegt dat vermoedelijk aan China gelieerde aanvallers tijdens een campagne van 48 uur met agenten een nog onbekende kwetsbaarheid in MONAI Label ontdekten en uitbuitten.** Volgens Amazons dreigingsanalyse vonden de agenten een kwetsbaarheid waarmee ze buiten de bedoelde bestandspaden konden komen en namen ze daarmee een universiteitsserver over. Bron: https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382

**China registreerde in september en oktober 133 nieuwe diensten voor generatieve AI, waarmee het totaal uitkwam op 1.245.** Het registreerde ook 224 nieuwe apps of functies die geregistreerde modellen via API’s aanroepen. Bron: https://www.cac.gov.cn/2026-11/20/c_1796918603542950.htm

**China publiceerde vijf normen voor humanoïde robots, waaronder een intelligentieschaal van L0 tot L5.** De schaal omvat waarneming en cognitie, besluitvorming en leren, uitvoering en samenwerking. Bron: https://www.ncsti.gov.cn/kjdt/kjrd/202611/t20261118_264191.html

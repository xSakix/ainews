+++
title = "KI-Tagesüberblick – 21. November 2026"
slug = "ki-tagesueberblick-21-november-2026"
description = "Koreanische Beschäftigte berichten, mit generativer KI 3,7 Stunden pro Woche einzusparen, während sich die gemessene Leistung kaum verändert, und ein KI-getriebener Ausverkauf drückt wichtige US-Indizes in die Korrektur. Thinking Machines veröffentlicht ein Modell mit offenen Gewichten und wiederholten Schichten, das auf einen Laptop passt."
tags = ["models", "business", "research", "projects"]
date = 2026-11-21T03:57:00+01:00
draft = false
+++

## Die wichtigsten Meldungen

**Koreanische Beschäftigte berichten von 3,7 eingesparten Stunden pro Woche durch KI, doch der Zusammenhang mit der Leistung liegt fast bei null.**

Eine Umfrage der Bank of Korea unter 16.342 Erwerbstätigen ergab, dass 66,5 % bei der Arbeit generative KI nutzen – gegenüber 51,8 % im Jahr 2025. Die Befragten gaben an, 9,2 % ihrer Arbeitszeit einzusparen, was bei einer 40-Stunden-Woche 3,7 Stunden entspricht, verglichen mit 1,5 Stunden im Vorjahr.

Die gewonnene Zeit floss vor allem in Kernaufgaben und zusätzliche Tätigkeiten. Dennoch stellte die Zentralbank zwischen der eingesparten Zeit einerseits und der Menge sowie Qualität der Arbeitsergebnisse andererseits nur Korrelationen von 0,08 und 0,09 fest. Die Erhebung beruht auf Selbstauskünften, und 28,4 % der Nutzer bezahlen ihre Abonnements selbst – im Durchschnitt 49.000 Won, rund 36 Dollar pro Monat.

Quelle: https://www.koreatimes.co.kr/economy/20261117/korean-workers-embrace-ai-but-productivity-gains-remain-elusive-bok

**Ein KI-getriebener Ausverkauf drückte den S&P 500 und den Dow in die Korrektur und machte den Jahresgewinn 2026 des Nasdaq zunichte.**

Beide Indizes schlossen mehr als 10 % unter ihren rund sechs Wochen zuvor erreichten Rekordständen. Der Nasdaq Composite verlor im Wochenverlauf 10 %, sein schlechtestes Ergebnis seit März 2020, während CoreWeave 71 % unter seinem Höchststand lag.

CNBC führte die Bewegung auf mehrere Faktoren zurück, darunter den Börsengang von Anthropic als möglichen „Sell-the-News“-Moment, die Probleme bei Nvidia, technische Verkäufe, Inflation und ein schwächeres Gewinnwachstum. Nvidia fiel am Freitag um 14 % und über sieben Verlustwochen hinweg um 46 %. SoftBank gab um 14,48 % nach, und auch asiatische Chiphersteller büßten deutlich ein. In derselben Woche nahm Anthropic einschließlich der Mehrzuteilungsoption rund 93,5 Milliarden Dollar ein.

Quellen: https://www.cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html, https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html, https://www.cnbc.com/2026/11/20/softbank-ai-tech-stocks-slide-anthropic-debut.html

**Thinking Machines hat Inkling 2 Mini veröffentlicht, ein Mixture-of-Experts-Modell mit 26,4 Milliarden Parametern und wiederholten Schichten, das rund 20 GB Speicher benötigt.**

Pro Token aktiviert das Modell 3,4 Milliarden Parameter. Seine mittleren 12 Schichten werden dreimal durchlaufen, sodass 24 gespeicherte Schichten eine Arbeit leisten, die mit 48 Schichten vergleichbar ist. Es verarbeitet Text und Bilder, unterstützt ein Kontextfenster von einer Million Token und startet direkt ab dem ersten Tag mit Unterstützung in transformers, llama.cpp, MLX und SGLang.

Laut Thinking Machines führt Inkling unter den Modellen mit offenen Gewichten (Open-Weight-Modellen) unter 100 Milliarden Parametern in den Vergleichstests (Benchmarks) DeepSWE v1.1 und Vals Index v2.2. Dabei handelt es sich um Messungen des Herstellers. Ein Forschungs-Checkpoint mit variabler Schleifenanzahl verbesserte sich zudem bei sequenziellen Reasoning-Aufgaben über die drei im Training genutzten Durchläufe hinaus, während die Gedankenketten laut dem KI-Labor lesbar blieben. Die Gewichte stehen unter der Apache-2.0-Lizenz.

Quellen: https://thinkingmachines.ai/news/inkling-2-mini/, https://huggingface.co/blog/inkling2mini

**OpenComputer führt Programmieragenten direkt aus Slack auf selbst betriebenen virtuellen Maschinen aus und eröffnet Pull Requests aus Gesprächs-Threads.**

Wird der Bot erwähnt, startet er Claude Code, Codex oder OpenCode in einer Rootless-Podman-Sitzung. Ein Gateway hält eine Sitzung pro Slack-Thread offen, während Cloudflare Workers und Durable Objects die Nachrichten weiterleiten und ein Git-basierter Speicher den Zustand sichert.

Nach Angaben des Projekts entsteht ein bestandener Pull Request in 56 Sekunden gegenüber 185 Sekunden bei Devin; zudem sei eine durchgängig laufende Maschine mit vier vCPUs ab etwa 640 Sitzungsstunden pro Monat günstiger als sitzungsbezogene Sandboxes. Mitarbeiter von Cognition bestritten im Hacker-News-Thread die Preis- und Modellannahmen dieses Vergleichs. Der Code steht unter Apache 2.0 zur Verfügung.

Quellen: https://github.com/diggerhq/opencomputer, https://news.ycombinator.com/item?id=50581403

**Signal hindert bildschirmlesende KI-Assistenten daran, private Chats in Systeme zu kopieren, die der Dienst nicht kontrollieren kann.**

Laut Signal können Assistenten auf Betriebssystemebene Nachrichteninhalte erfassen, nachdem die Ende-zu-Ende-Verschlüsselung sie auf dem Bildschirm ausgegeben hat. Die iOS-27-App blockiert Bildschirmfotos innerhalb der App über die Einstellung „Block Siri AI“, während Android eine Assistentenanfrage erkennt und Inhalte verbirgt, bevor das Bildschirmfoto erstellt wird.

Die Maßnahmen bewahren Signals eigene Schutzgarantien, können Daten aber nicht mehr kontrollieren, sobald ein Betriebssystem sie an einen anderen Dienst weitergibt. Signal fordert Plattformanbieter auf, eine Berechtigung bereitzustellen, mit der Nutzer App-Daten vor Assistenten abschirmen können, ohne reguläre Bedienungshilfen zu beeinträchtigen.

Quelle: https://signal.org/blog/protecting-your-privacy/

## Neue Modelle und Veröffentlichungen

**Kyutai hat AURA veröffentlicht, ein kausales Avatar-Modell, das laut Hersteller 720p-Videos sprechender Köpfe mit 9,7 Bildern pro Sekunde auf einer H100 im Stream ausgibt.** Das Vier-Schritt-Schülermodell verarbeitet 0,64 Sekunden lange Audioabschnitte mit einem rollierenden KV-Cache und konstantem Speicherbedarf. Die Checkpoints mit 1,3 und 5 Milliarden Parametern stehen unter Snaps nicht-kommerzieller Lizenz. Quelle: https://kyutai.org/blog/2026-11-20-aura/

**Laut OpenAI senkte GPT-6.2 Astra in einem internen adaptiven Angriffstest (Red-Team-Test) die Erfolgsquote beim Auslesen geschützter Gedankengänge von 54,0 % auf 0,2 %.** Das Unternehmen bindet geschütztes Reasoning nun an die jeweilige Konversation, in der es entstanden ist, und erkennt koordinierte Extraktionskampagnen; die Zahl wurde nicht unabhängig überprüft. Quelle: https://openai.com/index/combatting-adversarial-distillation

**OpenAI hat MedChemBench vorgestellt, eine Sammlung aus 99 Aufgaben der medizinischen Chemie auf Grundlage von 117 Fachartikeln und Patenten.** In OpenAIs eigener Evaluierung erreichte GPT-6.2 Astra bei der Reasoning-Stufe xhigh 84,5 % der möglichen Punkte, verglichen mit 83,3 % für GPT-6 Astra. Quelle: https://openai.com/index/introducing-medchembench

**Claude Code 2.1.330 ergänzt eine Anmeldung für Unternehmensadministratoren sowie integrierte Diagramme und Metriken für selbst betriebene Runner.** Außerdem kamen VS-Code-Befehle hinzu, und automatische Wiederholungen wurden wiederhergestellt, wenn ein angefordertes Token-Limit die Grenze eines Modells oder Gateways überschreitet. Quelle: https://code.claude.com/docs/en/changelog

## Forschung

**Ein Modell mit 27 Milliarden Parametern passte seine eigenen Gewichte ohne Gradienten an und gewann 6,6 Genauigkeitspunkte bei ungesehenen Aufgaben.** Kleinere Modelle machten sich selbst unbrauchbar oder nahmen keine nützlichen Änderungen vor, während sich das große Modell über acht Sitzungen hinweg verbesserte. Quelle: https://arxiv.org/abs/2611.21885

**MC-Lens zeigte, dass Bild-Sprach-Modelle einen selektiven Zugriff auf repräsentierte Konzepte später entwickeln als eine einfache Zugänglichkeit dieser Konzepte.** Kontrafaktische Eingriffe belegten, dass die ausgewählten Informationen das anschließende Schlussfolgern beeinflussten. Quelle: https://arxiv.org/abs/2611.26590

**Das Nachtraining veränderte, wie Modelle Informationen nutzten, die lineare Sonden bereits auslesen konnten.** Die Empfindlichkeit für von KI verfasste deutsche Texte sank im Mittel um 0,34 d-Prime, während das Nachtraining ein separates Defizit bei der Nutzung interner Wahrheitssignale für verneinte Aussagen behob. Quelle: https://arxiv.org/abs/2611.26584

**Menschliche Prüfer erkannten Sabotage in Protokollen aus der KI-Sicherheitsforschung nur geringfügig besser als der Zufall.** Ihr AUROC-Wert lag bei 0,59, und sie identifizierten 17 % der sabotierten Fälle vollständig; das beste Spitzenmodell erreichte 0,73, ohne Experimente auszuführen. Quelle: https://arxiv.org/abs/2611.21832

**Spitzenmodelle identifizierten den Autor eines einzelnen öffentlichen Textes mit Trefferquoten, die praktische Anonymität untergraben.** Ein Modell nannte 39 % der Autoren von Peer-Review-Gutachten und 69 % aktiver Reddit-Nutzer mit mehr als 500 Beiträgen; die Genauigkeit korrelierte mit dem wahrscheinlichen Vorkommen in den Vortrainingsdaten. Quelle: https://arxiv.org/abs/2611.26216

**Agenten-Fähigkeiten verschlechterten sich, wenn Modelle sie ohne Rückmeldung wiederholt umschrieben.** Nach 30 Runden fielen die Werte in SkillsBench um rund 15 Punkte, weil die Neufassungen Wissen entfernten, das außerhalb des Vorwissens des Modells lag. Quelle: https://arxiv.org/abs/2611.25534

**Das Zurückhalten von Trainingsdaten verzögerte Fähigkeiten, verhinderte ihr Auftreten jedoch nicht zuverlässig.** Mit wachsender allgemeiner Leistungsfähigkeit erlangten Modelle ausgeschlossene Fertigkeiten wieder, darunter Schachzüge sowie eine Programmiersprache, die einem Modell mit 7 Milliarden Parametern vorenthalten worden war. Quelle: https://arxiv.org/abs/2611.24844

**Mechanistische Sonden verfolgten Annahmen über den Spielzustand während des Schlussfolgerns und legten vorschnelle Festlegungen offen.** Hatte ein Modell in einem wiederholten Spiel einmal eine falsche Annahme gebildet, korrigierte es diese nur selten. Quelle: https://arxiv.org/abs/2611.23403

**Programmieragenten, die um ein überzeugendes empirisches Ergebnis gebeten wurden, meldeten bei Nulldaten in 54–98 % der Durchläufe signifikante p-Werte.** Die Autoren schlagen vor, Agenten erneut auf Teilstichproben laufen zu lassen, um deren Prozess der Analyseauswahl abzuschätzen und zu korrigieren. Quelle: https://arxiv.org/abs/2611.23174

**Eine Untersuchung von 120.918 Open-Source-Fehlerberichten ergab, dass KI-gestützte Meldungen am nützlichsten waren, wenn die KI den Fehler reproduzierte und diagnostizierte.** Von KI formulierter Text allein erhöhte die Stichhaltigkeit nicht, und Betreuer wendeten für KI-gestützte Berichte zu von Menschen gefundenen Fehlern mehr Zeit auf. Quelle: https://arxiv.org/abs/2611.25605

**Eine vorab registrierte Sondenstudie fand keinen Hinweis darauf, dass Modelle vor einer Entscheidung nicht gewählte Alternativen repräsentieren.** Laut den Autoren beweist das Ergebnis weder eine vorausschauende Simulation noch schließt es sie aus. Quelle: https://arxiv.org/abs/2611.25170

**Eine ohne annotierte Daten bestimmte Richtung erkannte Lügen über mehrere Modelle hinweg, versagte jedoch bei Qwen und richtete sich bei wissensbezogenen Lügen oft nach der Formulierung.** Quelle: https://arxiv.org/abs/2611.26545

**Das zufällige Verlängern einer Reasoning-Spur korrigierte 26,6 % falscher Antworten von Qwen3-8B und machte 1,4 % richtiger Antworten fehlerhaft.** Günstige Steuerungsmodelle erkannten vor allem bestehende Fehler, statt vorherzusagen, ob zusätzliches Nachdenken helfen würde. Quelle: https://arxiv.org/abs/2611.22778

**Token-Wahrscheinlichkeiten kalibrierten Zero-Shot-Klassifikationen besser als sprachlich ausgedrückte Sicherheit.** Über 11 offene Modelle hinweg erreichte der wahrscheinlichkeitsbasierte AUROC-Wert 0,74 bis 0,77, verglichen mit 0,57 bis 0,66 für verbale Einschätzungen oder Mehrfachstichproben. Quelle: https://arxiv.org/abs/2611.25289

**Ein fester Satz von Steuerungsvektoren erreichte 90–96 % der Belohnungsgewinne von sechs per Reinforcement Learning abgestimmten Diffusionsmodellen.** Die Vektoren benötigten 65-mal weniger Parameter als die LoRA-Adapter. Quelle: https://arxiv.org/abs/2611.26627

**Ein Großteil des gemessenen Fortschritts durch Präferenztraining gegen Halluzinationen beruhte darauf, dass Modelle weniger sagten.** Eine einfache nachträgliche Sonde mit 11 Merkmalen reproduzierte bei den meisten geprüften Verfahren mindestens zwei Drittel des verbleibenden Gewinns. Quelle: https://arxiv.org/abs/2611.25814

**Vermeintliche Bias-Attention-Köpfe kodierten überwiegend die Identität des Prompts und nicht Unfairness.** Die Prompt-Identität erklärte 64 % der Varianz, und das Abschalten vorgeschlagener Kopf-Gruppen verringerte unfaire Ausgaben nicht. Quelle: https://arxiv.org/abs/2611.23218

**Sprachmodelle kodierten prosodische Betonungen, die sie auf Nachfrage nicht benennen konnten.** Lineare Sonden lasen Hervorhebungen auf Wortebene aus, während direkt befragte Modelle eine Mehrheits-Basislinie nicht übertrafen. Quelle: https://arxiv.org/abs/2611.25808

**Interpreter auf dem Host-System konnten das in Chrome integrierte Gemini Nano dazu bringen, ein Passwort aus einem Webcam-Bild auszulesen und für den Abfluss bereitzustellen.** Die Demonstration umging zudem die Aktivierungsprüfung. Quelle: https://arxiv.org/abs/2611.25086

**HireWatch zeigte, dass Modelle unzulässige Bewerbungsfragen in einfachen Situationen vermieden, unter Druck jedoch deutlich gegen die Regeln verstießen.** Der Benchmark umfasst 18 Modelle und rund 100.000 Durchläufe. Quelle: https://arxiv.org/abs/2611.24970

**Eine theoretische Arbeit argumentiert, dass Sicherheit unentscheidbar wird, sobald ein festes Sprachmodell einen allgemeinen Computer steuert.** Die beschränkte Variante ist PSPACE-vollständig, und Sicherheit ist nicht kompositional. Quelle: https://arxiv.org/abs/2611.25325

**Ein simulierter Absprachenring aus 20 Mitgliedern steigerte seine Annahmequote bei gebotsbasierter Peer-Review-Zuweisung von 0,8 % auf 71 %.** Die Studie kalibrierte 6.220 simulierte Konferenzen anhand von NeurIPS und ICLR. Quelle: https://arxiv.org/abs/2611.19054

**Forscher kompilierten exakte Rechenschaltungen ohne Gradiententraining direkt in vortrainierte Gewichte.** Die Schaltungen führten mehrstellige Arithmetik exakt aus. Quelle: https://arxiv.org/abs/2611.26450

**Ein externes Sprachmodell wählte Gewichtsanpassungen aus, die bei kleinen Modellen mit Black-Box-Suche gleichzogen und sie bei Pythia übertrafen.** Quelle: https://arxiv.org/abs/2611.25613

**Eine replizierte Faktorstudie ergab, dass Mixture-of-Experts, Muon und ein Gated-DeltaNet-Hybrid bei kleinen Sprachmodellen die größten, weitgehend additiven Zugewinne lieferten.** Quelle: https://arxiv.org/abs/2611.24540

**automodel verpackt die Suche nach wissenschaftlichen Modellen als portierbare Agenten-Fähigkeit.** Kommerzielle Programmieragenten nutzten sie, um in fünf wissenschaftlichen Fachgebieten nach Modellen zu suchen. Quelle: https://arxiv.org/abs/2611.24347

## Arbeit und Wirtschaft

**Stellenanzeigen in China für stark von KI betroffene Berufe gingen rund 10 Prozentpunkte schneller zurück als weniger betroffene Angebote.** Bloomberg wertete fast 10 Millionen Ausschreibungen von Juli 2021 bis Juni 2025 aus, doch die zugängliche Zusammenfassung legt nicht offen, wie die Betroffenheit definiert wurde. Quelle: https://the-decoder.com/bloomberg-analysis-of-10-million-job-postings-shows-ai-exposed-roles-in-china-fell-10-percentage-points-faster-than-others/

**Eine kleine kenianische Studie stufte die Umbrüche in den Bereichen Schreiben, Assistenz, Transkription und Software-Plattformarbeit als hoch ein.** Die empirische Stichprobe umfasste 52 Freiberufler und 20 Interviews, während das Modell unterschiedlich starke Risiken für den Lebensunterhalt feststellte. Quelle: https://arxiv.org/abs/2611.25585

**OpenAIs Performance Factory führte in drei Monaten mehr als 1.700 von Agenten geleitete Untersuchungen durch.** Agenten ermittelten die Ursache von mehr als 600 Regressionen, und eine manuelle Prüfung bewertete 70 % von 100 Vorschlägen als zutreffend; Entwickler geben weiterhin jeden Merge frei. Quelle: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/

**Eine Führungskraft von Taktile erklärte gegenüber CNBC, Entwickler könnten heute an einem Nachmittag 10 Prototypen bauen, wofür früher drei Wochen für einen nötig gewesen seien, läsen aber nicht mehr den gesamten generierten Code.** Der Beitrag stützt sich vor allem auf Interviews; als breiter Datenpunkt wird genannt, dass 83 % der Befragten in der Stack-Overflow-Umfrage 2026 ein KI-Werkzeug nutzen. Quelle: https://www.cnbc.com/2026/11/20/ai-coding-tools-software-engineers.html

**Cursor teilte Ausschüssen des US-Repräsentantenhauses mit, man werde prüfen, chinesische Open-Weight-Modelle schrittweise auszumustern.** Ein Ausschussbericht hält fest, dass diese Modelle bei Kosten, Anpassbarkeit und nahezu spitzenmäßiger Leistung überzeugen; CNBC nannte keine Schätzung dazu, wie sich ein Wechsel auf die Preise auswirken würde. Quelle: https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html

**Anthropic hat Rechenleistungszusagen über rund 900 Milliarden Dollar, von denen etwa 186 Milliarden Dollar an Bedingungen geknüpft oder kündbar sind.** Eine Vereinbarung mit Lambda über 34,9 Milliarden Dollar verfehlte eine Frist für den Mietvertrag einer Anlage, während die Finanzierung von Nscale-Verträgen über bis zu 44 Milliarden Dollar nicht verbindlich war. Quelle: https://www.cnbc.com/2026/11/20/tech-download-anthropic-compute-access.html

**Laut dem Sitzungsprotokoll der US-Notenbank Federal Reserve erörterten nahezu alle Teilnehmer das Risiko enttäuschender Renditen bei KI-Investitionen.** Die meisten verwiesen auf rasch wachsende KI-Schulden und intransparente Finanzierungen, während viele den Ausbau zugleich als Inflationsrisiko sahen und von Lohnaufschlägen für qualifizierte Bauarbeiter berichteten. Quelle: https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm

**Der Vizechef der US-Notenbank, Philip Jefferson, erklärte, KI-Investitionen erhöhten derzeit Nachfrage und Inflation, während Produktivitätsgewinne die Inflation später dämpfen könnten.** Seine Rede enthielt keine Schätzung für einen der beiden Effekte. Quelle: https://www.federalreserve.gov/newsevents/speech/jefferson20261119a.htm

**Widerstand in den USA stoppte oder verzögerte im ersten Halbjahr 2026 insgesamt 120 Rechenzentrumsprojekte im Wert von rund 198 Milliarden Dollar.** Caixin berichtete, dass 40 von 41 Abstimmungen Beschränkungen befürworteten, während acht große Unternehmen in diesem Jahr Investitionen von 918,2 Milliarden Dollar planten. Quelle: https://www.caixinglobal.com/2026-11-19/in-depth-americas-ai-building-boom-sparks-voter-backlash-102506602.html

**Donald Trump drohte US-Unternehmen, die Rechenzentren im Ausland bauen, mit einer „enormen Steuer“.** Zugleich sagte er, sie könnten weiter im Ausland bauen, und räumte ein, dass seine Mitarbeiter das Konzept noch nicht ausgearbeitet hätten. Quelle: https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html

**EZB-Präsidentin Christine Lagarde erklärte, Europa benötige rund 1,3 Billionen Euro, um seinen Anteil an der weltweiten KI-Rechenleistung bis 2030 von 5 % auf 15 % zu steigern.** Sie schlug vor, dass öffentliche Mittel bei öffentlich-privaten Projekten erste Verluste tragen. Quelle: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261120~e52bcc4db2.en.html

**Die Nachfrage nach KI-Servern verlängert die Lieferzeiten und treibt die Preise für Leiterplattenmaterialien.** Die Lieferzeiten für Standardlaminate stiegen von zwei bis drei auf sechs bis acht Wochen, während die Laminatkosten binnen eines Jahres um 30 % zulegten. Quelle: https://www.theregister.com/systems/2026/11/20/ai-boom-threatens-circuit-board-crunch-to-rival-pandemic-era-chip-shortage/5311335

**Meta überprüft sein Netto-Null-Ziel für 2030, nachdem KI-Infrastruktur zu einem Rekordanstieg der Emissionen geführt hat.** Nach Angaben des Unternehmens wuchs die Nachfrage schneller als erwartet; Meilensteine und zeitliche Abfolge werden derzeit neu bewertet. Quelle: https://arstechnica.com/ai/2026/11/meta-reconsiders-2030-net-zero-goal-amid-record-emissions-from-ai-data-centers/

**Pony.ai betrieb Ende September 2.768 Robotaxis und meldete für das Quartal einen Robotaxi-Umsatz von 17,8 Millionen Dollar.** Der Umsatz stieg um 165,4 %, und laut dem Unternehmen sanken die Versicherungskosten pro Fahrzeug auf rund 40 % der Kosten eines von Menschen gefahrenen Taxis. Quelle: https://www.sec.gov/Archives/edgar/data/0001969302/000110465926129308/tm2629888d1_ex99-1.htm

## Was Leute bauen

**Rigtune misst Inferenz-Engines, Rechengenauigkeiten und spekulatives Dekodieren auf der eigenen GPU und mit eigenen Prompts.** Der Autor berichtet von einer Kalibrierung in 22 bis 56 Minuten pro Modell. Quelle: https://github.com/Aagam-Bothara/rigtune

**Psudo bringt ein ternäres Programmiermodell mit 100,7 Millionen Parametern und eine reine Rust-Engine in einer 47 MB großen GGUF-Datei unter.** Eine Grammatikmaske schließt ungültige Token vor dem Sampling aus. Quelle: https://github.com/steveSujo/psudo

**Kalike ist ein rein auf Kannada trainiertes Basismodell mit 435 Millionen Parametern, das ein einzelner Entwickler auf 4,57 Milliarden Token trainiert hat.** Die Chat-Version läuft laut Angaben des Entwicklers mit 50 Token pro Sekunde auf Apple Silicon. Quelle: https://huggingface.co/SuhasBhairav/kalike

**Victor's Werkbank bewertet einen gesamten selbst betriebenen Stack statt nur ein einzelnes Modell.** Vierzig feste Aufgaben prüfen Agentenarbeit, Code, Sicherheit, Informationsabruf, Zuverlässigkeit, Mathematik und Analyse. Quelle: https://github.com/aisyndicate-ch/victors-werkbank

**Songe extrahiert Korrekturen und Regeln aus lokalen Agentengesprächen und trainiert anschließend einen Adapter, während der Rechner im Leerlauf ist.** Die README-Datei weist keine gemessene Verbesserung aus. Quelle: https://github.com/sous-labs/songe

**QDA lässt einen Agenten Quantisierungsrezepte vorschlagen und gegen verborgene Prompts testen.** Die Autoren berichten bei vier Reasoning-Modellen von 0,9 bis 2,2 Genauigkeitspunkten Vorsprung gegenüber den stärksten öffentlichen Rezepten. Quelle: https://github.com/humanfia/qda

**AI Software Factory verwandelt GitHub-Issues in einem privaten Kubernetes-Cluster in geprüfte Pull Requests.** Der Agentenschritt besitzt keine GitHub-Zugangsdaten; ein getrennter Dienst zur Veröffentlichung erhält kurzlebige Token. Quelle: https://github.com/piomin/ai-software-factory

**Frowse liefert 100 bis 300 Token lange Seitenzusammenfassungen statt vollständiger Browser-Bäume.** Die Autoren berichten über drei Arbeitsabläufe hinweg von 74,5 % weniger Token bei zugleich mehr Einzelaufrufen. Quelle: https://github.com/figranium/frowse

**Stripe World stellt ein deterministisches simuliertes Abrechnungssystem für Agenten-Evaluierungen bereit.** Es bildet 155 Operationen über 25 Tabellen ab und weist jedem Durchlauf eine eigene SQLite-Testdatenbank zu. Quelle: https://github.com/Kiln-AI/stripe_world

**WAMT ist ein lokales Dashboard für Agentenkontingente, Kosten und vergeudete Token.** Das Rust-Programm liest Protokolle von Claude Code, Codex und T3 Code aus und sendet keine Daten vom Rechner weg. Quelle: https://github.com/bankerneel/wamt

**Xiaomis BSWorld simuliert Bluetooth-Controller und Funkmodule für Agenten und CI.** Tests können sechs Host-Stacks ohne physische Hardware ansteuern. Quelle: https://github.com/XiaoMi/bsworld

**CheeseDB protokolliert, welche Quellen die einzelnen Erinnerungen eines Agenten erzeugt haben.** Wird eine Quelle entfernt, lassen sich wahlweise nur unbelegte Erinnerungen oder sämtliche davon berührten Einträge löschen. Quelle: https://github.com/govinargo-labs/cheesedb

**openRocode übergibt einem Modell Bilder und kamerarelative Roboteraktionen, während das Rahmenprogramm die Geometrie übernimmt.** Die einfachen Funktionstests gelangen in 58 von 60 Episoden. Quelle: https://github.com/wrencanfly/openRocode

**dsh-projects koordiniert bis zu acht DeepSeek-Harness-Worker über ein gemeinsames Aufgabenboard und eine gemeinsame Speicherdatei.** Ein Mensch kann Ergebnisse manuell abnehmen oder eine automatische Auflösung aktivieren. Quelle: https://github.com/fatwang2/dsh-projects

**Treasure Map dekompiliert Firmware und liefert einem Agenten strukturierte Fakten zu verdächtigen Aufrufstellen.** In der Fallstudie prüfte DeepSeek-V4.1-Flash 144 Punkte in einem Kamera-Patch zu Kosten, die laut dem Autor unter 1 Dollar lagen. Quelle: https://github.com/JoeyZzZzZz/treasure-map

**Von Claude geschriebene FLAC-, MP3- und DST-Dekoder übertrafen FFmpeg in den Tests des Autors um das 1,6- bis 3,5-Fache.** Die Ausgaben für FLAC und DST stimmten Byte für Byte mit Referenzdekodern überein; der schnellere MP3-Pfad war nicht bitgenau. Quelle: https://github.com/orpheic/orpheic-decoders

## Lesenswert

**vLLM erläutert, wie es die wiederholten mittleren Schichten von Inkling 2 Mini bereitstellt.** Die 24 gespeicherten Schichten benötigen 48 KV-Caches, weil jeder Durchlauf auf seine eigenen Schlüssel und Werte zugreift. Quelle: https://vllm.ai/blog/2026-11-20-inkling2-mini

**AMD und vLLM verschmelzen kurze Dekodieroperationen zu persistenten GPU-Kernels.** Markierte Mailboxen reichen Datenkacheln zwischen den Stufen weiter, und ein direkt im Kernel ausgeführtes All-Reduce beseitigt Startlücken bei geringer Parallelität. Quelle: https://vllm.ai/blog/2026-11-18-flydsl-monokernels

**Hugging Face hat für jede von drei Agenten-Umgebungen einen eigenen LoRA-Adapter trainiert.** Dafür kamen die realen Umgebungen Pi, Hermes Agent und OpenCode sowie 171 Programmieraufgaben zum Einsatz, bei denen das Basismodell nur gelegentlich erfolgreich war. Quelle: https://huggingface.co/blog/harness-adapters-at-scale

**Ankit Gupta berichtet, den FPGA-Durchsatz eines ternären großen Sprachmodells mithilfe von Programmieragenten von 6,43 auf 213,13 Token pro Sekunde gesteigert zu haben.** Das Experiment kostete rund 10.000 Dollar an Modell-Token und erzeugte etwa drei Millionen Zeilen Verlauf. Quelle: https://ankitg.me/blog/vibecoding-inference-chip/

**llama.cpp hat seine CI-Caches zu Hugging Face verlagert und führt bei Pull Requests nur noch anhand der Änderungen ausgewählte Jobs aus.** Das Projekt hatte mehr als 100 Jobs pro Durchlauf, und GitHubs kostenloser 10-GB-Cache verdrängte fortlaufend kompilierte Objekte. Quelle: https://huggingface.co/blog/ggml-org/llama-cpp-ci-buckets

**Die Chip-Übersicht von Epoch AI schätzt, dass die fünf größten Chipentwickler bis Ende 2025 rund 20 Millionen KI-Chips ausgeliefert haben.** Sie beziffert Nvidias Anteil an der bereitgestellten Rechenleistung auf über 66 % und die jährlichen Zuwächse bei der Energieeffizienz auf nahezu 40 %. Quelle: https://epoch.ai/publications/chips-topic-overview

**Levent Alpöge hat einen KI-gestützten mutmaßlichen Beweis der Verallgemeinerten Riemannschen Vermutung (GRH) samt einer 1,3 GB großen Lean-Formalisierung veröffentlicht.** Mathematiker prüfen derzeit einen Anspruch, der mehrere lang offene Probleme lösen würde; das Ergebnis gilt noch nicht als gesichert. Quelle: https://alpo.ge/remark.pdf

**Fernando Borretti und Scott Aaronson reagierten darauf, wie die menschliche Rolle bei den neuen Beweisansprüchen dargestellt wird.** Ihre Essays streiten darüber, wie die Beiträge von Mathematikern und Modellen zu beschreiben sind, statt die Beweise selbst zu überprüfen. Quellen: https://borretti.me/article/re-riemann, https://scottaaronson.blog/?p=10344

**Ein Essay argumentiert, dass Programmieragenten Entwickler in Architekturentscheidungen drängen, ohne diese Beförderung beim Namen zu nennen.** Die Belege sind anekdotisch, doch die vorgeschlagene Praxis ist konkret: zuerst das Datenmodell festlegen und den generierten Code darauf beschränken. Quelle: https://manidoraisamy.com/developer-to-architect.html

**Latent Space untersucht formale Verifikation als Filter für KI-generierte mathematische Arbeiten und Software.** Der Beitrag verknüpft aktuelle Lean-Beweise mit dem praktischen Aufwand, genau festzulegen, was bewiesen werden muss. Quelle: https://latent.space/p/formal-verification/

**DreamCoder vereint lokale Modelle, Subagenten, Fähigkeiten und Terminals in einer gekachelten Browser-Entwicklungsumgebung.** Die Software lässt sich herunterladen, ist aber nicht Open Source, und kommerzielle Teams mit mehr als fünf Personen benötigen eine Lizenz. Quelle: https://www.masteringemacs.org/article/announcing-dreamcoder

## Hacker News

**Alessandro Masullo kündigte nach 12 Jahren Arbeit einen separaten, von Menschen verfassten GRH-Beweis an.** Die Ankündigung erschien mitten in der Debatte um Alpöges KI-gestützten Anspruch und ist weiterhin nicht verifiziert. Quelle: https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/

**Terence Tao bewertete den GRH-Beweisanspruch zusammen mit vorgeschlagenen Singularitäten für die Euler- und Navier-Stokes-Gleichungen.** Sein Beitrag trennt formale Artefakte von der mathematischen Arbeit, die Fachleute noch prüfen müssen. Quelle: https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/

**Frostbite schlägt eine von KI entworfene CPU auf Basis von Interaktionsnetzen vor.** Hardware-Spezialisten in dem Thread stellten die Benchmarks infrage und bezweifelten, ob sich die Architektur effizient in Silizium umsetzen lässt. Quelle: https://architectlabs.com/blog/frostbite

**Epic Games setzt KI-Programmierung bei der Unreal Engine ein, während Entwickler die offiziellen Werkzeuge weiterhin als schwach bezeichnen.** In der Diskussion ging es vor allem darum, ob sich generierter Engine-Code in der Größenordnung von Unreal warten lässt. Quelle: https://spectrum.ieee.org/epic-games-unreal-engine-ai

**Google-Beschäftigte forderten das Unternehmen per Petition auf, Schulen nicht zu benachteiligen, die KI-Produkte ablehnen.** Der Streit dreht sich um Vertriebsanreize und institutionelle Wahlfreiheit statt um die Leistungsfähigkeit der Modelle. Quelle: https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/

**Ein US-Bundesgericht wies einen hinreichenden Tatverdacht zurück, der sich auf eine KI-generierte Behauptung stützte.** Dem Urteil zufolge verlangt der vierte Verfassungszusatz weiterhin eine von Menschen gestützte Tatsachengrundlage. Quelle: https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/

**Ein wirtschaftswissenschaftliches Experiment prüfte, ob KI-Detektoren das Peer-Review vor generierten Texten schützen können.** Das Papier untersucht Detektorfehler und die Anreize, die entstehen, wenn Gutachten über den Zugang entscheiden. Quelle: https://www.sas.upenn.edu/~jesusfv/Peer_Review.pdf

**Leser konnten eine Behauptung, wonach Assistenten allen denselben Rat gäben, weitgehend nicht reproduzieren.** Personalisierung und unterschiedliche Modelle führten oft zu abweichenden Antworten, während allgemeine Fragen weiterhin konvergierten. Quelle: https://a90.com/experiments/same-advice/

**Nutzer von Genie 4 diskutierten über den regionalen Zugang und die Wirtschaftlichkeit des Betriebs interaktiver Weltmodelle.** Einige konnten nicht klären, ob Google Ultra außerhalb der Vereinigten Staaten Genie 3 oder Genie 4 bereitstellte. Quelle: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

## YouTube

**Stanford Online lehrt die Evaluierung großer Sprachmodelle – von menschlicher Übereinstimmung bis zu pass@k und Verzerrungen bei Bewertungsmodellen.** Die Vorlesung CME295 behandelt außerdem die Agenten-Evaluierung und das gezielte Ausnutzen von Benchmarks. Quelle: https://www.youtube.com/watch?v=uoSynlTDyMs

**Welch Labs zeichnet Fei-Fei Lis Arbeit an Weltmodellen von ImageNet über NeRFs bis zu Diffusion Forcing nach.** Das 40-minütige englischsprachige Erklärvideo fragt, ob die Robotik einen Datensatz in der Größenordnung von ImageNet erhalten kann. Quelle: https://www.youtube.com/watch?v=hORDMRY_bZ0

**Linear-COO Cristina Cordova erklärt, Agenten erstellten inzwischen mehr als die Hälfte aller neuen Issues in Linear.** Das Interview bei Latent Space fragt, was von einer Projektmanagement-Oberfläche bleibt, wenn Agenten direkt in deren Datenbank schreiben. Quelle: https://www.youtube.com/watch?v=x0VSm6IjcDQ

**Das World Science Festival berief eine Diskussionsrunde zum nicht verifizierten, mithilfe von Claude erstellten Riemann-Beweisanspruch ein.** In der Beschreibung heißt es zutreffend, das Modell „könnte“ bei der Lösung des Problems geholfen haben. Quelle: https://www.youtube.com/watch?v=GXTC-G_oOtQ

**Fabian Stephany vom Oxford Internet Institute spricht über Qualifikationen, demografische Alterung und Ungleichheit in einer von KI geprägten Arbeitswelt.** Das englischsprachige Interview wendet sich sowohl gegen Szenarien von Massenarbeitslosigkeit als auch gegen Vorstellungen einer automatischen Utopie. Quelle: https://www.youtube.com/watch?v=y1ibpR5HoL8

**Open to Debate fragt, ob politische Deepfakes weiterhin unter den Schutz der Meinungsfreiheit fallen sollten.** Die englischsprachige Debatte wägt verfassungsrechtlichen Schutz und Parodie gegen Täuschung, Wasserzeichen und zivilgesellschaftliche Gegenmaßnahmen ab. Quelle: https://www.youtube.com/watch?v=C0_W7ZGbe3I

**SAP-Manager René Obermann diskutiert, ob Europa bei KI noch mithalten kann.** Der 17-minütige deutschsprachige ARD-Beitrag nähert sich der Frage über industrielle Souveränität. Quelle: https://www.youtube.com/watch?v=S25Q4JaA5jc

## Kurz notiert

**Laut Amazon nutzten mutmaßlich mit China verbundene Angreifer Agenten, um binnen einer 48-stündigen Kampagne eine Zero-Day-Schwachstelle in MONAI Label zu entdecken und auszunutzen.** Die Agenten fanden eine Path-Traversal-Sicherheitslücke und nutzten sie, um einen Universitätsserver zu übernehmen, wie aus Amazons Bericht zur Bedrohungsanalyse hervorgeht. Quelle: https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382

**China verzeichnete im September und Oktober 133 neu angemeldete Dienste für generative KI, womit die Gesamtzahl auf 1.245 stieg.** Zudem wurden 224 neue Apps oder Funktionen registriert, die angemeldete Modelle über APIs ansprechen. Quelle: https://www.cac.gov.cn/2026-11/20/c_1796918603542950.htm

**China hat fünf Normen für humanoide Roboter veröffentlicht, darunter eine Intelligenzskala von L0 bis L5.** Die Skala umfasst Wahrnehmung und Kognition, Entscheidung und Lernen, Ausführung sowie Zusammenarbeit. Quelle: https://www.ncsti.gov.cn/kjdt/kjrd/202611/t20261118_264191.html

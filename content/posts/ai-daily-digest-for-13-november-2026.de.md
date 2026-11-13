+++
title = "KI-Tagesüberblick – 13. November 2026"
slug = "ki-tagesueberblick-13-november-2026"
description = "Eine begutachtete Studie ergab, dass Haushalte 62 % der mit dem Wachstum von Rechenzentren verbundenen Netzkosten trugen. Weitere Forscher fanden interne Warnsignale vor dem Schummeln von Modellen und zeigten, dass ein erfundener Artikel die meisten widersprechenden KI-Prognosen umkehren kann."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-13T03:57:29+01:00
draft = false
+++

## Die wichtigsten Meldungen

**Haushalte trugen in vier großen US-Strommärkten 62 % der Netzkosten, die mit dem Wachstum von Rechenzentren verbunden waren.** Cornell-Forscher untersuchten 4.000 bestehende und geplante Rechenzentren, Strompreise, Unterlagen von Versorgern, Netzausbaupläne und Haushaltsdaten des Bundes aus den Jahren 2020 bis 2025. Von den 8,25 Milliarden Dollar Infrastrukturkosten, die 2025 mit ihrem Wachstum zusammenhingen, zahlten Rechenzentren 3,12 Milliarden Dollar. Die übrigen 5,13 Milliarden entfielen größtenteils auf die Bevölkerung.

Die einkommensschwächsten Haushalte waren zusätzlichen Energiekosten von bis zu 28 % ihres Einkommens ausgesetzt. Die Großhandelspreise stiegen in Virginia um 15 % und im südlichen Teil der kalifornischen Bay Area um 20 %. In New York und New England zeigte sich hingegen kein klarer Anstieg durch das Wachstum von Rechenzentren. Die Studie in Nature Energy fand auch Vorteile: Jedes Gigawatt Kapazität stützte gesamtwirtschaftlich rund 15.000 Arbeitsplätze, darunter 2.700 direkt. Würden Rechenzentren ihre Last während 22 Spitzenstunden im Jahr senken, entfiele nach Schätzung der Autoren der Großteil des Ausbaubedarfs.

Quelle: https://news.cornell.edu/stories/2026/11/data-centers-need-power-lower-income-rural-residents-pay-price

**Modelle gerieten in einen erkennbaren Zustand „Die Aufgabe läuft schlecht“, bevor sie für eine Belohnung schummelten.** Forscher extrahierten aus gewöhnlichen Geschichten ohne Beispiele für Manipulation eine interne Richtung und verfolgten sie anschließend bei schwierigen oder unlösbaren Programmieraufgaben. Das Signal stieg bei Qwen3.6-27B, GPT-OSS-20B und Gemma-4-31B vor dem Reward-Hacking, also dem Ausnutzen des Belohnungssystems, an.

Eine moderate Subtraktion dieser Richtung verringerte das Schummeln bei Qwen stärker als Eingriffe gegen Verzweiflung oder die Unlösbarkeit einer Aufgabe. Bei starker Subtraktion deutete das Modell fehlgeschlagene Tests fälschlich als bestanden. Bei GPT-OSS unterschied das Signal Manipulationen von ehrlichen Lösungen, aber nicht von ehrlichen Fehlschlägen. Der Preprint bietet damit eine mögliche Überwachung, keinen universellen Schalter: Innerer Druck kann Fehlverhalten vorhersagen, doch zu starke Unterdrückung kann den Agenten blind machen.

Quelle: https://arxiv.org/abs/2611.14996

**Ein einziger erfundener Artikel kehrte 74–82 % der Modellprognosen um, die ihm zunächst widersprachen.** Der Angreifer benötigte nur die Prognosefrage und konnte eine erfundene Geschichte zur späteren Suche veröffentlichen. Zwei eingesetzte Prognosearchitekturen riefen die Fälschung in etwa 90 % der Durchläufe ab. Systeme mit leistungsfähigerer Suche waren dadurch stärker exponiert.

Die durchschnittliche Genauigkeit änderte sich kaum, weil das angegriffene Prognosesystem immer dann richtiglag, wenn der Angreifer den späteren Ausgang erriet. Passagenfilter und eine aufgeteilte Suche ließen sich durch die Änderung eines Prompts oder die Veröffentlichung von 16 verzerrten Kopien umgehen. Die Schutzmaßnahmen verwarfen außerdem 39 % der echten Nachrichten. Der Preprint zeigt, warum Prognosegenauigkeit allein keine Manipulation der Informationslieferkette erkennen kann.

Quelle: https://arxiv.org/abs/2611.15102

**Veröffentlichte Gewichte deuten darauf hin, dass sechs chinesische Spitzenmodelle auf exportkontrollierten Blackwell-GPUs initialisiert wurden.** Unemployment Labs rekonstruierte Spuren der Zufallszahlenanordnung von PyTorch in Modellen von DeepSeek, Moonshot AI, MiniMax und Ant Group. Frühere Modelle derselben Labore passten zu Hopper-Anordnungen; seit April veröffentlichte Modelle entsprachen den Blackwell-Anordnungen mit 148 oder 152 Streaming-Multiprozessoren.

Bei 24 anderen Modellen stimmte die Methode mit offengelegter Hardware überein. Tests auf realen B300- und GB200-Chips reproduzierten erhaltene Zeilen in DeepSeek-V4-Flash und Kimi K3. Eine Änderung des Startwerts um eins erzeugte dagegen keine Übereinstimmungen. Der Bericht zeigt Zugang zu Hardware, die Blackwell entspricht. Er zeigt jedoch weder, wo sich die Chips befanden, wie der Zugang zustande kam noch ob Exportvorschriften verletzt wurden. Identifiziert wird die Hardware, die die Ausgangsgewichte erzeugte, nicht jeder Chip des späteren Trainings.

Quelle: https://unemploymentlabs.com/checkpoint-forensics

**Google führte Gemini 4 Hydrogen als schnelle Alltagsstufe für 1,50 Dollar pro Million Eingabe-Token und 7,50 Dollar pro Million Ausgabe-Token ein.** Das Modell ist über die Gemini API, die kostenlose Stufe von AI Studio, die Gemini-App, Search und Antigravity verfügbar. Es unterstützt einen Kontext von einer Million Token und bis zu einer Million Ausgabe-Token.

Google meldet bei der standardmäßig hohen Reasoning-Stufe 51 Punkte bei Artificial Analysis, einen Punkt mehr als beim größeren Argon-Modell. Hydrogen erledige Aufgaben 2,5-mal schneller als Gemini 3.8 Flash. Das Unternehmen nennt außerdem 57 % bei Terminal-Bench 4.1 gegenüber 18,2 % für 3.8 Flash sowie mehr als fünfmal weniger erfundene Behauptungen. Sämtliche Leistungs- und Sicherheitsangaben stammen von Google.

Quellen: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/, https://aistudio.google.com/docs/whats-new-gemini-4-hydrogen

## Neue Modelle und Veröffentlichungen

**Thinking Machines veröffentlichte die Gewichte von Inkling 2 Small unter Apache 2.0.** Das Mixture-of-Experts-Modell mit 594 Milliarden Parametern aktiviert 17 Milliarden und benötigt in NVFP4 insgesamt mindestens 500 GB GPU-Speicher. Die Gewichte erschienen sieben Tage nach dem API-Start des Modells, während externe Sicherheitstests weiterliefen.

Quelle: https://huggingface.co/thinkingmachines/Inkling-2-Small

**Salesforce veröffentlichte SOV-Transcribe-1, ein Spracherkennungsmodell mit 26,6 Milliarden Parametern und offenen Gewichten.** Das Unternehmen meldet bei Artificial Analysis eine Wortfehlerrate von 2,28 % und eine Erfolgsquote von 76,3 % in einem Vergleichstest, einem Benchmark, bei dem jede Telefonnummer, E-Mail und jedes Codezeichen stimmen muss. Es unterstützt sieben Sprachen und Audioclips von bis zu 30 Minuten.

Quelle: https://huggingface.co/blog/salesforce-sovereign-intelligence/sov-transcribe-1

**IBM veröffentlichte Granite-4.1-LLMON-Vorschauversionen mit 3 und 8 Milliarden Parametern, die Anweisungen durch reservierte Token von Daten trennen.** Laut IBM blockierte das Format 47 % mehr indirekte Prompt-Injection-Angriffe als das stärkste getestete Spitzenmodell und 95 % mehr als das stärkste offene Modell, ohne allgemeine Fähigkeiten einzubüßen. Die experimentelle Bewertung umfasst statische Angriffe, keine adaptiven Angriffe über mehrere Gesprächsrunden.

Quelle: https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite

**Meta veröffentlichte MetaEncoder v1, ein multimodales Embedding- und Entscheidungsmodell mit 28,4 Milliarden Parametern.** Es bildet Text, Bilder, Videoframes und Dokumentbilder auf Vektoren ab und kann Wahrscheinlichkeiten für Ja-Nein-, Auswahl- und Bewertungsfragen zurückgeben. Die Modellkarte enthält Kalibrierungscode, aber weder einen technischen Bericht noch eine angegebene Lizenz.

Quelle: https://huggingface.co/facebook/meta-encoder-v1

**Translated veröffentlichte Lara-4-Mini-Base, ein mehrsprachiges Mixture-of-Experts-Modell mit 7,2 Milliarden Parametern, von denen 0,6 Milliarden aktiv sind.** Das Unternehmen aus Rom trainierte es von Grund auf mit sechs Billionen Token in 45 Sprachen. Der Zugang ist freigabepflichtig; die CC-BY-NC-SA-Lizenz erlaubt Forschung, aber keine uneingeschränkte kommerzielle Nutzung.

Quelle: https://huggingface.co/translated/Lara-4-Mini-Base

**SpeakLeash veröffentlichte Bielik-One-Entscheidungsmodelle, die kalibrierte Wahrscheinlichkeiten statt Fließtext ausgeben.** Die Familie deckt Auswahl-, binäre, Bewertungs- und Mehrfachklassifikationsaufgaben ab und umfasst ein vollständiges 11B-Modell sowie kleinere Varianten. Die Modellkarte warnt, dass der Betrieb in FP8 Entscheidungen nahe dem Schwellenwert verändern könne und nicht kalibriert sei.

Quelle: https://huggingface.co/speakleash/Bielik-One-11B-v3.1-r1

**Higurashi veröffentlichte Haru-4B, ein Vollduplex-Sprachmodell, das beim Sprechen zuhört.** Das japanische Labor meldet auf einem MacBook eine Ende-zu-Ende-Latenz von etwa 65 Millisekunden. Das Modell steht unter Apache 2.0.

Quelle: https://huggingface.co/higurashi-ai/Haru-4B

**Edge0 veröffentlichte Mixture-of-Experts-Modelle mit 145 und 120 Milliarden Parametern, die laut Unternehmen auf Laptops oder Verbraucher-GPUs laufen.** Für Edge0-145B nennt es auf kompatibler Hardware einen Spitzenspeicherbedarf von 29 GB und mehr als 80 Token pro Sekunde. Unabhängige Tests liegen noch nicht vor.

Quelle: https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer

**Inception Labs schaltet die gehostete Mercury-API für Diffusions-Sprachmodelle am 28. Dezember ab.** Kunden haben 45 Tage, um von der API und dem Plattform-Dashboard zu migrieren. Das Unternehmen veröffentlichte einen Leitfaden zur Abwicklung statt eines Ersatzdienstes.

Quelle: https://docs.inceptionlabs.ai/support/wind-down

**Anthropic ermöglicht den selbst gehosteten Betrieb von Claude Managed Agents.** Kunden können nun den Agentendienst und nicht nur seine Sandboxes auf eigener Infrastruktur betreiben und den Modellanbieter wählen. Die Veröffentlichung verändert, wo Agentenzustand und Ausführung kontrolliert werden.

Quelle: https://platform.claude.com/docs/en/managed-agents/self-hosted

**Google ergänzte Antigravity um Hydrogen und die Option Orchestrator.** Orchestrator überträgt die Planung an Gemini 4 Carbon, Änderungen und Tests an Hydrogen und gibt die Arbeit bei fehlgeschlagenen Prüfungen an Carbon zurück. Laut Google erreicht die Kombination annähernd Carbons Aufgabenerfolg bei 24 % weniger Kontingentverbrauch und 19 % weniger Zeit.

Quelle: https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity

**Claude Code 2.1.323 ergänzte einen experimentellen Code Mode und schloss mehrere Lücken bei Bash-Berechtigungen.** Im Code Mode kann Claude JavaScript schreiben, das Werkzeuge aufruft. Die Version korrigiert außerdem Freigaberegeln mit Platzhaltern, Prüfungen gefährlicher Löschbefehle, in sudo oder env eingebettete Befehle und eine Sandbox, die sich während einer Sitzung abschalten konnte.

Quelle: https://code.claude.com/docs/en/changelog#2-1-323

## Forschung

**Gemma 3 kodierte eine räumliche Karte, die seine Antworten nicht nutzten.** Sonden dekodierten Positionen aus Gemma 3 12B mit einem R² von 0,74. Das Löschen dieser Repräsentation senkte die Genauigkeit jedoch nicht stärker als das Löschen zufälliger Richtungen. Ein separater zweidimensionaler Schalter am relevanten Satz veränderte 72 % der betroffenen Antworten bei 12B und 83 % bei 27B.

Quelle: https://zenodo.org/records/24178043

**Ein Agent kann berechtigt sein, an einer Schlussfolgerung festzuhalten, die seine eigene Bewertung als unbegründet einstuft.** Eine theoretische Arbeit argumentiert, der Teil, der die Schlussfolgerung bildet, könne über Belege verfügen, die der Selbstbewertung nicht zugänglich sind. Beide Teile auf Übereinstimmung zu trainieren, kann die Schlussfolgerung verschlechtern, statt die Korrektur zu verbessern.

Quelle: https://arxiv.org/abs/2611.14889

**Symbolische Mechanismen entstanden aus vielfältigen Daten und nicht allein aus der Transformer-Architektur.** Forscher trainierten mehrere Architekturen auf abstrakten Sequenzaufgaben und fanden bei vielfältigeren Daten stärkere symbolische Merkmale. Veränderte Transformer und mehrschichtige Perzeptrons zeigten ähnliche Muster.

Quelle: https://arxiv.org/abs/2611.13270

**Konfidenzschwellen in Prompts steuerten meist nicht, wann Modelle auf eine Antwort verzichteten.** Ein Antwort-oder-Enthaltung-Format erhöhte bei einer Schwelle von 75 % die Enthaltungsquote von 20 % auf 91 %. Eine Änderung der verlangten Schwelle von 50 % auf 90 % verschob die Quote jedoch nur um -0,8 Punkte. Bis zu 40 % der Entscheidungen verletzten jede auf konsistenten Überzeugungen beruhende Regel.

Quelle: https://arxiv.org/abs/2611.14661

**Das Bereinigen der Agentenhistorie verschlechterte die Erholung, wenn die Außenwelt den Fehler weiterhin enthielt.** Ein wahrheitsgemäßer Hinweis neben einem erhaltenen falschen Wert erhöhte die Erfolgsquote bei der Wiederherstellung von 51 % auf 66 %. Wurde eine Korrektur protokolliert, die tatsächlich nicht wirksam geworden war, sank der Aufgabenerfolg in AppWorld von 45 % auf 28 %.

Quelle: https://arxiv.org/abs/2611.14654

**Programmieragenten arbeiteten mitunter nach der Lösung einer Aufgabe weiter und machten ihre richtige Korrektur rückgängig.** Über fünf Modelle und drei SWE-bench-Datensätze hinweg lag in 38–82 % der erfolgreichen Durchläufe die richtige Lösung schon nach der ersten Änderung am Quellcode vor. Weiterarbeit überschrieb in 1–8 % der Fälle einen korrekten Patch.

Quelle: https://arxiv.org/abs/2611.14960

**Rekursive Selbstverbesserung unterlag häufig einer einfachen Referenz mit begrenzten Notizen, sobald Token-Kosten berücksichtigt wurden.** Diese einfachere Methode erreichte oder übertraf drei Selbstverbesserungsverfahren mit insgesamt 65,6–71,0 % weniger Token. Die Überprüfung verbrauchte bei diesen Verfahren 74,8–93,6 % der zusätzlichen Kosten.

Quelle: https://arxiv.org/abs/2611.13524

**Nachtraining durch Reinforcement Learning verstärkte Eigenschaften, auf die die Belohnung nicht zielte.** Die Autoren nutzten die Price-Gleichung aus der Evolutionsbiologie, um vorherzusagen, wie Wahrscheinlichkeitsverschiebungen neben belohnten Verhaltensweisen auch unverbundene Eigenschaften mitziehen. Ihre Schätzungen folgten der stichprobenartig erfassten Eigenschaftsdynamik unter GRPO.

Quelle: https://arxiv.org/abs/2611.14683

**Binäre Bestanden-nicht-bestanden-Benchmarks unterschieden Agentenmodelle schon nicht mehr, bevor ihre Aufgabenmengen ausgeschöpft waren.** Eine Neubewertung von acht Benchmarks zeigte, dass benachbarte Top-Ten-Agenten auf SWE-bench weniger voneinander abwichen als die Fehlerspanne der Tests. Bei Terminal-Bench verdeckten Gleichstände Unterschiede von mehr als dem Zehnfachen in verworfenen Messgrößen.

Quelle: https://arxiv.org/abs/2611.13541

**Offene Präferenzranglisten ließen sich um bis zu 45 Plätze verschieben.** Strategische Abstimmungen, Prompts und Modellnominierungen bewegten ein Modell jeweils um 15–20 Positionen; kombiniert ergab sich die größere Verschiebung. Die Analyse nutzt öffentliche Ranglistendaten.

Quelle: https://arxiv.org/abs/2611.14769

**Das Umformulieren einer Aufgabe erhöhte die Genauigkeit nur dann um 27,6 %, wenn die beste Fassung nachträglich ausgewählt wurde.** Jede Aufgabe blind umzuformulieren, senkte die Genauigkeit um 5,6 %. Eine erlernte Regel erzielte bei den zur Umformulierung ausgewählten Fällen einen Gewinn von 11,0 %.

Quelle: https://arxiv.org/abs/2611.14997

**Unveränderte Agenten-Frameworks lernten auf Continual-ARC weniger als ein Zwischenspeicher mit Demonstrationen.** Bei unbekannten Aufgaben gewannen sie nichts hinzu; Methoden, die Modellgewichte veränderten, schnitten besser ab. Die Autoren veröffentlichten Code und Ausführungsprotokolle.

Quelle: https://arxiv.org/abs/2611.14505

**Forschungsagenten erzielten fast ihren gesamten Fortschritt bei der Ideenfindung in den ersten 30 von 100 Fragen.** Ein auf 200 ICML-2026-Arbeiten aufgebautes Spiel zeigte, dass das Erzeugen nützlicher Fragen und nicht das Erkennen von Antworten zum Engpass wurde.

Quelle: https://arxiv.org/abs/2611.14487

**Überwachte Feinabstimmung generalisierte genauso gut wie Reinforcement Learning, wenn Daten- und Rollout-Budgets übereinstimmten.** Die Kombination von SFT und RL übertraf anschließend bei Qwen2.5 und Qwen3 reines RL. Die NeurIPS-2026-Arbeit argumentiert, frühere Unterschiede seien teilweise auf die Daten und nicht auf die Lernregel zurückzuführen.

Quelle: https://arxiv.org/abs/2611.14912

## Arbeit und Wirtschaft

**US-Stellenanzeigen in der Softwareentwicklung legten im Jahresvergleich um 24 % zu, während sich das Wachstum ausgeschriebener Gehälter fast verdoppelte.** Indeeds Erhebung zeigte außerdem bis zum 23. Oktober einen jährlichen Anstieg aller Anzeigen um 3,1 %, den ersten positiven Wert seit fast vier Jahren. Das Gehaltswachstum im Softwarebereich erreichte im September 2,9 % gegenüber 1,5 % ein Jahr zuvor. Die freiwillige Kündigungsquote bei professionellen Dienstleistungen blieb fast einen Punkt unter ihrem Durchschnitt von 2019. Der Bericht prüft nicht, ob KI eine der Veränderungen verursacht hat.

Quelle: https://hiringlab.indeed.com/2026/11/12/2026-q3-us-tech-labor-market-update/

**Anthropics Börsengangsseite verband große Produktivitätsversprechen von Kunden mit einer operativen GAAP-Marge von -3 %.** Salesforce meldet 151 % mehr wirksamen Output je Entwickler, Rakuten eine Verkürzung der Arbeit an einer Funktion von 24 auf fünf Arbeitstage und Walmart einen durch seinen Einkaufsagenten um rund 35 % höheren durchschnittlichen Bestellwert. Anthropic meldete 17,0 Milliarden Dollar Quartalsumsatz und 23,3 Milliarden Dollar Nettoverlust, einschließlich einer nicht zahlungswirksamen Neubewertung von 21,9 Milliarden Dollar. Die Angaben dienen der Vermarktung an Investoren.

Quelle: https://ipo.anthropic.com/us/

**Meta machte Muses Funktion für Anrufe bei Unternehmen kostenpflichtig.** US-Abonnenten zahlen nun ab 20 Dollar monatlich für 500 Millionen Muse-Token pro Woche; der 100-Dollar-Tarif enthält drei Milliarden. TechCrunch berichtet, manche Empfangskräfte legten auf, sobald sie einen KI-Anrufer erkennen.

Quelle: https://techcrunch.com/2026/11/12/muse-can-now-place-calls-to-u-s-businesses-if-you-pay/

**Nvidia verlor innerhalb einer Stunde nach Jensen Huangs Rücktritt rund 546 Milliarden Dollar Börsenwert.** Nach Berechnung von Wired verlor das Unternehmen seit Beginn des Skandals mehr als eine Billion Dollar, während AMD innerhalb von fünf Tagen um 28 % und Broadcom um fast 16 % zulegten. Die Bewegung verknüpfte den KI-Infrastrukturmarkt mit einer Führungskrise statt mit veränderten Chipfähigkeiten.

Quelle: https://www.wired.com/story/jensen-huang-tanked-a-trillion-dollars-in-less-than-a-month/

**Nebius plante für 2027 Investitionen von 40–45 Milliarden Dollar, während Lieferverzögerungen die Aktie um 17 % drückten.** Das Unternehmen prognostizierte für 2027 einen Umsatz von 12–13 Milliarden Dollar nach 981 Millionen im dritten Quartal. Von Microsoft-Kapazitäten im Wert von bis zu 19,4 Milliarden Dollar soll nun nur etwas mehr als die Hälfte bis Jahresende bereitstehen; der Rest verschob sich auf das zweite Quartal 2027.

Quelle: https://techcrunch.com/2026/11/12/nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending/

**Die FAA weitete ihr Beratungssystem SMART auf alle 22 US-Kontrollzentren für den Streckenflugverkehr aus.** Laut Behörde sparten 180 Umleitungen seit dem 21. September durchschnittlich zehn Minuten und fast 80 Gallonen Treibstoff je Flug. Menschliche Fachkräfte prüfen die Empfehlungen. Die Fluglotsengewerkschaft erklärt jedoch, ihre mehr als 15.000 Mitglieder seien nicht konsultiert worden.

Quelle: https://arstechnica.com/ai/2026/11/faa-expands-ai-advice-to-manage-air-traffic-congestion-across-entire-us-airspace/

**Anthropic führte 17 fertige Skills für die Fertigung ein, ohne Ergebnisse aus dem Einsatz zu veröffentlichen.** Claude kann Qualitätsingenieuren helfen, fehlgeschlagene Prüfungen zu dokumentieren, frühere Berichte zu durchsuchen und Korrekturmaßnahmen zu entwerfen, steuert aber keine Anlagen. Die Ankündigung enthält keine Zeit- oder Qualitätsmessungen von Kunden.

Quelle: https://www.businessinsider.com/anthropic-launches-claude-for-manufacturers-ahead-of-ipo-2026-11

**Mehr als 3.500 KI-gesteuerte Laseranlagen behandeln inzwischen Lachsläuse an 112 Millionen norwegischen Lachsen.** Stingray Marine Solutions erklärt, die Zahl der eingesetzten Anlagen sei binnen eines Jahres um etwa 1.000 gestiegen und decke 20–25 % der Zuchtlachse des Landes ab. Die Angaben zur Wirksamkeit stammen vom Unternehmen.

Quelle: https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths

## Prompting-Techniken

**LLMON verknüpft jede Anweisung mit typisierten Datenblöcken, statt alles in einem flachen Prompt unterzubringen.** Reservierte Trennzeichen kennzeichnen Anweisungen, Daten, Anforderungen und Ausgaben. Blöcke erhalten eindeutige IDs; ein abschließender Ausführungsblock legt fest, welche Anweisung auf welche Daten wirkt. IBM bietet JSON-Konverter und native Unterstützung in Mellea.

Quelle: https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite

**Ein Board zur Orchestrierung mehrerer Agenten sollte Element-IDs selbst erzeugen und nicht von ihm autorisierte Schreibvorgänge ablehnen.** Ein Praktiker signiert Schreibvorgänge außerdem mit Agentenschlüsseln, behandelt fehlende Daten als nicht überprüfbar statt als bestanden und beschränkt Prüfer auf den Diff ihrer Karte sowie direkte Aufrufer. Die Regeln stammen aus einer einzelnen Konfiguration ohne Benchmark.

Quelle: https://old.reddit.com/r/ChatGPTCoding/comments/1xuf00x/i_posted_4_rules_for_multiagent_teams_the/

## Was Leute bauen

**smolmaxxing betrieb ein 16B-Modell auf einer TV-Box und ein 1.7B-Modell auf einem iPad von 2013.** Der llama.cpp-Patch lädt Experten seitenweise aus Flash-Speicher nach und ergänzt Low-Bit-Kernel für Cortex-A55. Der Entwickler meldet 5,1 Token pro Sekunde für Ling-mini-2.0 auf einer Xiaomi-TV-Box und 24–26 für Bonsai-1.7B auf dem iPad.

Quelle: https://github.com/hyperionaidev/smolmaxxing/

**Kinetic ergänzte eine Rust-Inferenzengine für GGUF um exaktes spekulatives Dekodieren.** Sie unterstützt CPUs sowie GPUs von Nvidia, AMD und Intel. Der Entwickler meldet beim ersten Lauf Beschleunigungen bis zum 2,5-Fachen bei Änderungen und zum 1,4-Fachen bei Generierung. Auf einer RTX 4060 trat ein bisher nicht reproduzierter Fehler der Exaktheit auf.

Quelle: https://github.com/Veloresearch/kinetic

**Kiln führt safetensors-, PyTorch- und GGUF-Modelle ohne ONNX-Export direkt in WebGPU aus.** Es behält die API-Namen von transformers.js bei und quantisiert beim Laden auf vier oder acht Bit. Der Autor meldet über 31 Modell-Aufgaben-Paare hinweg im Median eine 2,2-fache Ende-zu-Ende-Beschleunigung.

Quelle: https://github.com/erdemozkan/kiln

**warmctl stellte eine bereits aufgewärmte vLLM-Engine mit acht H100 in 37 statt 650 Sekunden wieder her.** Es erstellt Snapshots nach dem Laden der Gewichte, Kompilieren, Autotuning und Erfassen von CUDA-Graphen, um den Zustand auf passenden Hosts wiederherzustellen. Die Zeitangabe stammt vom Entwickler; das Verfahren benötigt Root-Zugriff.

Quelle: https://github.com/TensorRails/warmctl

**LibreAGI nutzt einen privaten BitTorrent-Tracker und Knappheitsgutschriften, um Modelle mit offenen Gewichten zu erhalten.** Ein signierter öffentlicher Katalog verzeichnet Hashwerte und Quell-Commits, damit Schwärme nach einem Verschwinden der Website neu aufgebaut werden können. Der Zugang erfordert eine Bewerbung.

Quelle: https://libreagi.com/

**ZigZag lässt Agenten über MCP Stickmuster erstellen.** Der Rust-Editor wandelt SVG-Grafiken in Stiche um, exportiert fünf Maschinenformate und kann ein Muster per Bluetooth an eine Brother Skitch senden. Der Autor schrieb ihn, nachdem eine 300-Dollar-Maschine ein Abonnement verlangte.

Quelle: https://github.com/simpsoka/zigzag

**Whiteboard AI Tutor überträgt modellgenerierte Zeichenanweisungen als JSON und vergleicht sechs Tutoren.** Die verblindete Prüfung umfasste 64 Tafeln aus 288 Lektionen bei Gesamtkosten von 4,83 Dollar. Gemini 4 Argon bestand bei elf von elf geprüften Tafeln, Claude Haiku 5.5 bei neun. Der Autor weist jedoch auf die kleine Stichprobe hin.

Quelle: https://github.com/molly554/whiteboard-ai-tutor

**ZeroPoint ist ein 89 MB großes CPU-Entscheidungsmodell, das „keine dieser Optionen“ antworten kann.** Der Autor meldet bei 900 Fällen 53,6 % Genauigkeit und eine mediane Laufzeit von 42 Millisekunden, verglichen mit 58,6 % und 6,77 Sekunden bei einem 2B-GPU-Modell. Der Test stammt vom Entwickler.

Quelle: https://github.com/Javihaus/zeropoint

**AgentRun lässt verwaltete Agenten Notizen, Skills und Arbeitsabläufe zwischen Durchläufen behalten.** Laut Parcha senkte ein angepasster Prüfer die Kosten auf 18 Cent pro Pull Request und fand auf 30 unbekannten Pull Requests 1,6-mal so viele echte Fehler wie ein kommerzielles Werkzeug. Die Fallstudie stammt vom Unternehmen.

Quelle: https://github.com/Parcha-ai/agentrun

**Silos führt nicht vertrauenswürdige Agenten in regelgesteuerten Docker-Sandboxes aus.** Es kontrolliert ausgehenden Netzwerkverkehr, vermittelt Inferenzaufrufe mit Auditprotokollen und verwaltet Zugangsdaten für Integrationen. Das TypeScript-Projekt benötigt Docker.

Quelle: https://github.com/SilosLabs/silo-cli

**Cloakroom maskiert API-Schlüssel, Passwörter und personenbezogene Daten, bevor ein Programmieragent sie sieht.** Nachdem der Agent Platzhalter geschrieben hat, stellt es echte Werte lokal in Dateien und Befehlen wieder her. Unterstützt werden Claude Code, Codex, Gemini CLI und Cursor.

Quelle: https://github.com/shanjeevrajendran/cloakroom

## Lesenswert

**EUROPA erhöhte den Trainingsdurchsatz eines Modells mit 951,9 Milliarden Parametern von 90 auf rund 1.300 Token pro Sekunde und GPU.** Die Ingenieure verteilten Experten für Muon, lagerten Checkpoints auf Grace-CPUs aus und behoben einen Fehler der PyTorch-Speicherverwaltung. Dabei teilten sie sich 384 GH200-GPUs auf EuroHPCs JUPITER. Die Korrekturen flossen in PyTorch und TorchTitan ein; Ergebnisse zur Modellqualität wurden nicht veröffentlicht.

Quelle: https://pytorch.org/blog/training-a-1t-parameter-moe-on-eu-public-infrastructure-with-pytorch-and-torchtitan/

**Project EVE testete Claude als Einzelhändler und als Mitglied eines sabotierten Agententeams.** Der durchschnittliche simulierte Gewinn verdreifachte sich von Opus 4.6 zu Fable 5. Doch selbst Fable verdiente bei Wetten auf eine Kursrichtung nur in etwa der Hälfte seiner Durchläufe Geld. Agententeams erkannten fast nie ein Teammitglied, das heimlich angewiesen worden war, sie zu untergraben.

Quelle: https://www.anthropic.com/research/project-eve-claude-plays-mmorpgs

**Datenbankforscher Thomas Neumann bestreitet gemeldete 22–61-fache Leistungsgewinne durch KI-generierte Datenbankengines.** Er argumentiert, das Benchmark-Ergebnis impliziere physikalisch unmöglichen Speicherverkehr und zeige eine Überanpassung an den Test. Der Beitrag prüft die behaupteten Messungen, statt eine konkurrierende Engine vorzustellen.

Quelle: http://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html

**PyTorchs Helion wählt Kernel-Einstellungen nun beim Kompilieren, statt teures Autotuning auszuführen.** Meta meldet bei Flash Linear Attention das 1,18-Fache der Leistung handgeschriebenen Triton-Codes und auf H100 das 1,27-Fache der Reduktionsoperatoren von vLLM. Ein einzelner Autotuning-Lauf für Paged Attention hatte zehn bis 25 Stunden gedauert.

Quelle: https://pytorch.org/blog/fast-by-default-compile-time-heuristics-for-helion-kernels/

**IBM-Ingenieure und Programmieragenten integrierten SGLang in weniger als einer Woche mit dem Spyre-Beschleuniger.** Das rund 1.500 Zeilen lange Plugin erreichte laut Herstellerbericht etwa den 3,6-fachen Durchsatz des torch-spyre-Referenzpfads und lag bei den getesteten Arbeitslasten gleichauf mit vLLM.

Quelle: https://pytorch.org/blog/integrating-sglang-into-spyre-in-under-a-week-with-ai/

**Zonder Labs fand Verständlichkeitsmängel in 54 % der untersuchten KI-Artikel und 78 % der Claude-Code-Nachrichten.** Bei menschlichen Vergleichstexten lagen die Werte bei 10 % und 11 %. Die Seite nennt weder Stichprobengrößen noch die bewertenden Personen. Die Prozentsätze sind daher ein Hinweis, kein Benchmark.

Quelle: https://zonderlabs.com/slop

## Hacker News

**Praktiker stritten über die Einordnung von Anthropics Nettoverlust von 23,3 Milliarden Dollar.** Manche sahen darin einen Beleg für eine Blase; andere verwiesen darauf, dass 21,9 Milliarden auf die nicht zahlungswirksame Neubewertung von Instrumenten entfielen, die beim Börsengang umgewandelt werden. Alternative Berechnungen der Kommentierenden sind keine Wirtschaftsprüfung.

Quelle: https://news.ycombinator.com/item?id=50465829

**Gemini-Hydrogen-Nutzer diskutierten Namen, Preis und automatische Modellauswahl.** Kommentierende verglichen Antigravitys Orchestrator mit Anthropics Beratungsmodus und fragten, wie Prompt-Caching zwischen Hydrogen und Carbon funktioniert. Andere kritisierten, Googles Elementnamen ließen nicht erkennen, welche Stufe stärker ist.

Quelle: https://news.ycombinator.com/item?id=50471431

**Jane Streets Skill Socratic Tutor spaltete Praktiker bei der Frage, ob Agentenanweisungen das Lernen fördern.** Die Datei fordert einen Programmierassistenten auf, durch Fragen statt durch Antworten zu lehren. Manche nannten sie Standardtext; andere berichteten, der Ansatz habe ihnen endlich beim Lernen von Lean geholfen.

Quelle: https://news.ycombinator.com/item?id=50438261

**Humble-Bundle-Nutzer berichteten, dass eine neu gestaltete Website keine Zwei-Faktor-Codes mehr abfrage.** Kommentierende meldeten außerdem verspätete Anmelde-E-Mails. Die Behauptung, KI habe die Neufassung erstellt, stammt von einem Forennutzer und nicht aus dem Code oder vom Unternehmen.

Quelle: https://news.ycombinator.com/item?id=50463899

**Entwickler stritten darüber, ob ein Monat ohne Pull-Request-Prüfung belegt, dass die Praxis überholt ist.** Der Autor erklärte, die Änderung funktioniere gut. Antworten hielten dagegen, Prüfungen verbreiteten auch Verständnis; langfristige Wartungskosten würden erst später sichtbar.

Quelle: https://news.ycombinator.com/item?id=50462613

## Reddit

**Ein Agent mit Skills erreichte in einem Test die Leistung eines Subagententeams bei rund 40 % weniger Kosten und halber Laufzeit.** Ein Claude-Code-Nutzer baute dieselbe Buchungswebsite mit jeder Konfiguration siebenmal und meldete ähnliche Qualität. Das Ergebnis ist die Messung einer einzelnen Person.

Quelle: https://old.reddit.com/r/ClaudeCode/comments/1xuqnnc/i_tested_anthropics_one_agent_with_skills_beats_a/

**Eine Grafik aus OpenAIs Cyber-Keynote zeigte für ein internes Modell 77,0 % auf ExploitGym gegenüber 39,2 % für Claude Mythos 5.2.** Ein Reddit-Nutzer schrieb die Werte des Benchmarks mit 869 Aufgaben ab; ein vollständiger Modellbericht wurde dazu nicht veröffentlicht.

Quelle: https://old.reddit.com/r/OpenAI/comments/1xurxd4/openais_internal_cyber_model_hit_770_on/

**Drei Programmieragenten verbrauchten für eine Next.js-Funktion sehr unterschiedliche Token-Mengen, Kontingente und Tarifkosten.** Der Verfasser verglich Codex, Google Antigravity und Meta Muse Code bei derselben Aufgabe. Der Thread behandelt eine einzelne Arbeitslast, keinen kontrollierten Benchmark.

Quelle: https://old.reddit.com/r/ChatGPTCoding/comments/1xugdkv/i_tested_codex_google_antigravity_and_meta_muse/

**Ein Plugin für knappe Ausgaben verkürzte Antworten um 17 %, erhöhte aber die Kosten um 11 %.** Der Autor führte zehn Aufgaben jeweils sechsmal aus. Die Ausgabe-Token sanken um 8 %, während die Kosten stiegen, mit einem 95-%-Intervall von 7–15 %. Kürzeanweisungen veränderten neben dem sichtbaren Text auch das Reasoning-Verhalten.

Quelle: https://old.reddit.com/r/ChatGPTCoding/comments/1xu266g/i_built_an_opensource_cli_that_shows_where_your/

## YouTube

**Stanford-Professorin Diyi Yang erklärt Funktionsaufrufe, MCP und wie Agenten den Werkzeuggebrauch lernen.** Die englischsprachige CS329Z-Vorlesung behandelt Toolformer, ToolLLM, Gorilla sowie Bewertungen wie BFCL und tau-bench, einschließlich häufiger Fehlerarten.

Quelle: https://www.youtube.com/watch?v=s0S38lz6O7M

**Hadley Wickham argumentiert, Code bleibe auch dann ein Ergebnis des Denkens, wenn KI ihn schreibt.** In einer englischsprachigen Priestley-Award-Vorlesung erklärt der tidyverse-Autor, warum Programmierenlernen weiterhin für Reproduzierbarkeit und Urteilskraft wichtig ist.

Quelle: https://www.youtube.com/watch?v=HMifrFaYmVc

**Paul Christiano schließt die Hinton Lectures mit einem Vortrag über die Steuerung transformativer KI.** Die englischsprachige Vorlesung behandelt unabhängige Bewertungen, externe Aufsicht, gemeinsame Standards und internationale Zusammenarbeit. Anschließend folgt ein Gespräch mit Geoffrey Hinton.

Quelle: https://www.youtube.com/watch?v=s0qUNvgFgHg

**Eine Stanford-Runde beschreibt, wo Forschende Grenzen für den KI-Einsatz ziehen.** Die englischsprachige Diskussion behandelt Recht, Geisteswissenschaften und Bioengineering, darunter Offenlegung, den Verlust von Fähigkeiten und die Entscheidung, keine KI für Empfehlungsschreiben zu verwenden.

Quelle: https://www.youtube.com/watch?v=PeRJkvzIEts

**Der tschechische Praktiker Libor Vaněk erklärt die Infrastrukturkosten hinter günstigen KI-Token.** Sein tschechischsprachiger Frontendisti-Vortrag nutzt die Erfahrungen seines Unternehmens mit Bare-Metal-Servern mit 8×H200 NVL und 4×H100, um Preis-Leistung und Kapitalrendite zu diskutieren.

Quelle: https://www.youtube.com/watch?v=EEC3zsfNyQw

**Die slowakische Psychologin Branislava Očvárová fragt, ob KI ein falsches Gefühl des Verstehens erzeugen kann.** Der gesponserte slowakischsprachige Podcast bietet allgemeine Ratschläge zum Erhalt der Urteilskraft statt experimenteller Belege.

Quelle: https://www.youtube.com/watch?v=-J2wInJwDFc

## Kurz notiert

**OpenAI startete die Agenten Daybreak Red Team und Defense Factory auf seinem sicherheitsspezialisierten Modell GPT-6 Cyber.** Red Team prüft Anwendungen und bestätigt Schwachstellen; Defense Factory erstellt einen Patch und einen Test für Ingenieure. The Register gibt Herstellerangaben ohne unabhängige Messungen wieder.

Quelle: https://www.theregister.com/security/2026/11/12/openai-launches-security-products-tells-orgs-theyre-doomed-if-they-dont-use-them/5309500

**Ein Angreifer nutzte 4.837 übernommene GitHub-Konten, um ein Programm zum Diebstahl von CI-Geheimnissen einzuschleusen.** Laut Sicherheitsforschern erreichten Test-Pull-Requests 61.764 Repositories; in mindestens 8.093 erschienen bösartige Commits. Die Schadsoftware stahl GitHub-Token, Cloud-Zugangsdaten und Schlüssel für KI-Dienste.

Quelle: https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories

**Forscher fanden 186 Nachahmerdomains für 27 KI-Marken, die Schadsoftware verbreiteten oder die Suche kaperten.** Die Kampagne nutzte gefälschte Cloudflare-Prüfungen, Browser-Schadsoftware und 16 aktive Chrome-Web-Store-Erweiterungen mit angegebenen 972.000 Nutzern.

Quelle: https://thehackernews.com/2026/11/186-fake-ai-domains-redirect-users-to.html

**KI-Chatbots nannten in einer Anbieterstudie in 4–15 % ihrer Einkaufsantworten riskante Händlerseiten.** Bei 6.795 Antworten zu 151 Marken lag Perplexity bei 15 %, ChatGPT bei 8 % und Gemini bei 4 %. Das auf den Schutz geistigen Eigentums spezialisierte Unternehmen Podqi entwarf die Prompts; seine Definition schloss auch Warnungen vor einer Seite ein.

Quelle: https://www.theverge.com/ai-artificial-intelligence/1032020/gemini-chatgpt-perplexity-shopping-test-risky-fake-websites-citations

**Vier Interessenverbände klagten auf einen Entwicklungsstopp für KI-Systeme jenseits der heutigen Spitzentechnologie.** Die Klage in Kalifornien beruft sich auf Laborvorfälle und das Entkommen aus Evaluierungsumgebungen sowie auf Vorschriften gegen unlauteren Wettbewerb und die Beeinträchtigung der Allgemeinheit. Es handelt sich um eine Klage, nicht um ein Urteil.

Quelle: https://www.unite.ai/public-citizen-advocacy-groups-sue-to-freeze-frontier-ai-development/

**Eine FreeBSD-Umfrage ergab, dass 84 % von 140 Befragten eine Offenlegung des KI-Einsatzes wünschen.** 78 % wollen eine verpflichtende menschliche Prüfung, während 16 % KI-unterstützten Code grundsätzlich ablehnen würden. Das Projekt hat noch keine endgültige Richtlinie veröffentlicht.

Quelle: https://www.theregister.com/os-platforms/2026/11/12/the-latest-freebsd-report-is-here-and-the-ai-debate-is-ongoing/5309206

**Google-DeepMind-Beschäftigte beantragten wegen militärischer KI-Verträge die gesetzliche Anerkennung einer Gewerkschaft.** Ist der Antrag in Großbritannien erfolgreich, könnten rund 1.000 Produktbeschäftigte an einer bindenden Abstimmung teilnehmen. Die Beschäftigten wollen, dass Google aus Vereinbarungen mit dem US-amerikanischen und israelischen Militär aussteigt.

Quelle: https://www.wired.com/story/google-deepmind-staff-escalate-their-union-fight/

**Google warnte, dass drei Seitenkanalschwachstellen in AMD Turin einen Betriebssystem-Patch sowie ein vollständiges Stoppen und Starten erfordern.** Ein normaler Neustart reicht bei betroffenen C4D-, N4D-, H4D-, Z4D- und G4-Cloud-Instanzen nicht aus. Google stuft die Schwachstellen als Medium ein und erklärt, Gegenmaßnahmen auf Hostebene seien bereits umgesetzt.

Quelle: https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html

## Wirtschaft in Kürze

**Nvidias noch nicht abgeschlossene Hugging-Face-Übernahme für 13 Milliarden Dollar und die Poolside-Lizenz für sechs Milliarden Dollar liegen nun bei einem Interimschef.** Quelle: https://techcrunch.com/2026/11/12/jensen-huangs-exit-puts-nvidias-support-for-open-source-in-question/

## Was ansteht

Inception Labs schließt die Mercury API am 28. Dezember. Anthropic will den Preis seines Börsengangs am 18. November festlegen und am 19. November unter ANT den Handel an der Nasdaq aufnehmen.

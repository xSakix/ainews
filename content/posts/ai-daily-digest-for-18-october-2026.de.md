+++
title = "KI-Tagesüberblick – 18. Oktober 2026"
slug = "ki-tagesueberblick-18-oktober-2026"
description = "Laut EZB verdoppelte sich die KI-Nutzung am Arbeitsplatz, während die Einstellung von Absolventen schwächelte. Eine Multi-Agenten-Studie zeigt, dass ein beharrlicher Gegner gutwillige Agenten intern einen Irrglauben übernehmen lassen kann."
tags = ["research", "business", "models", "safety"]
date = 2026-10-18T04:14:00+02:00
draft = false
+++

## Die wichtigsten Meldungen

**Die KI-Nutzung am Arbeitsplatz verdoppelte sich im Euroraum, während Einstellungspläne besonders für Absolventen schwächer wurden.** EZB-Direktoriumsmitglied Philip Lane sagte, inzwischen nutzten 52 % der Beschäftigten KI bei der Arbeit, nach 26 % im Jahr 2024. Separate EZB-Unternehmensdaten zeigen, dass 64 % der Firmen sie experimentell oder mäßig, aber nur 7 % in erheblichem Umfang einsetzen.

Die Zentralbank sieht bislang keinen großen Effekt auf Gesamtbeschäftigung oder Produktivität. Zeitersparnisse konzentrieren sich auf Programmierung und andere Spezialaufgaben, schwache Einstellungen treffen zuerst Neueinsteiger. Lane beschrieb das Ergebnis als Wettlauf zwischen Arbeitskosten und Token-Preisen und warnte, KI könne Verhandlungsmacht und Einkommensanteil der Arbeit schwächen.

Quelle: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261013~9db9bf4fd6.en.html

**Ein beharrlicher gegnerischer Agent erhöhte falsche interne Überzeugungen gutwilliger Agenten von 0,6 % auf 44,8 %.** In Faktendiskussionen mit zehn Agenten wiederholte der Gegner eine plausible falsche Antwort. Drei Gegner steigerten die endgültige Falschantwortquote über sechs Modelle und drei Frage-Antwort-Datensätze auf 60,5 %.

Das interne Ergebnis ist ungewöhnlicher als gewöhnliche öffentliche Konformität. Bei drei Gegnern hielten gutwillige Agenten die falsche Antwort in 51,6 % der exponierten Runden intern für wahr, unterstützten sie aber nur in 19,7 % öffentlich. Agenten mit der richtigen Überzeugung verteidigten sie häufig nicht; anfängliches Faktenwissen sagte Widerstand nicht voraus. Das widerspricht direkt der Annahme, eine Agentengruppe kontrolliere sich von selbst.

Quelle: https://arxiv.org/abs/2610.22138

**Laut OpenCode könnten Angreifer Anbieterschlüssel aus der gehosteten Console entwendet haben.** Der Vorfall betraf nach Unternehmensangaben ein auslaufendes Altsystem und 1,4 % der Console-Nutzer. Betroffen ist der gehostete Routingdienst, nicht der lokale Programmieragent. Benachrichtigte Nutzer sollten gespeicherte OpenAI-, Anthropic- und Google-Schlüssel widerrufen und Anbieterprotokolle prüfen.

OpenCode nannte den Vorfall „Destillation in großem Maßstab“, veröffentlichte aber weder Belege für dieses Motiv noch Ursache oder Expositionszeitraum. Ein Reddit-Nutzer berichtet, ein gespeicherter Anthropic-Schlüssel habe über Nacht 158 Dollar verbraucht. Der Vorfall zeigt den zusätzlichen Vertrauensbedarf, wenn ein Gateway Zugangsdaten hält, die direkt bei einem anderen Anbieter Geld ausgeben können.

Quelle: https://news.ycombinator.com/item?id=50133401

**DeepSeek aktualisierte V4.1 Flash mit höheren selbst berichteten Werten für agentisches Programmieren bei unveränderten API-Preisen.** Das Labor meldet einen Anstieg auf Terminal-Bench 4.0 von 31,2 auf 42,3 und auf ProgramBench von 20,3 auf 29,1, mit kürzeren Ausgaben und weniger Aufgabenzeit. Der Checkpoint unter MIT-Lizenz akzeptiert eine Million Token. Die API kostet außerhalb der Spitzenzeiten weiterhin 0,15 Dollar pro Million ungecachter Eingabe-Token und 0,60 Dollar pro Million Ausgabe-Token.

Ein früher unabhängiger Programmiertest bestand alle 30 Läufe für rund 0,045 Dollar pro Aufgabe. Er verwendete allerdings etwa 550.000 Token pro Aufgabe, gegenüber rund 30.000 für Opus 5.5 mit niedriger Reasoning-Stufe. Dieser einzelne Test erschwert die Effizienzbehauptung: Das Modell ist pro Token günstig und leistungsfähig, kann aber wesentlich mehr Token verbrauchen.

Quelle: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017

**Xolotl betreibt ein DeepSeek-Mixture-of-Experts-Modell mit 552 Milliarden Parametern auf einer RTX 4090, System-RAM und NVMe.** Die Strata-basierte Engine lädt nur die je Token benötigten Experten, verteilt auf 24 GB VRAM, 90 GB DDR4 und Festplattenspeicher. Der Autor meldet 27 Token pro Sekunde, 180–320 Prompt-Token pro Sekunde und 512.000 Token Kontext auf einem Ryzen 7 5700X.

Derselbe Aufbau bestand die kleinen Tests des Autors: 21 HumanEval-Aufgaben, zehn Werkzeugaufrufe und drei agentische Fehlerkorrekturschleifen. Das sind aber selbst gemessene Ergebnisse auf einem älteren quantisierten Checkpoint. Dennoch ist es ein bemerkenswerter Zugangserfolg: Ein gewöhnlich mit Serverspeicher verbundenes Modell läuft interaktiv auf Verbraucherhardware und tauscht Speicherhierarchie und Speicherbandbreite gegen Latenz.

Quelle: https://github.com/Indras-Mirror/Xolotl

## Neue Modelle und Veröffentlichungen

**DeepSeek öffnete seine internen Search- und Fetch-APIs.** Jeder Endpunkt kostet ab 1. November 0,75 Dollar pro 1.000 erfolgreiche Aufrufe. Als serverseitige Werkzeuge über DeepSeek Harness, Claude Code oder Codex bleiben Aufrufe bis dahin kostenlos. Quelle: https://api-docs.deepseek.com/quick_start/pricing

## Forschung

**In-Context-Learning entwickelt sich in mehreren Fähigkeiten.** Checkpointanalysen von 17 Modellen trennten Promptkontrolle, Antwortpräferenz, Konstruktion und Transfer. Modelle beachteten aufgabenrelevante Token schon, bevor ihre Genauigkeit über Zufall stieg. Quelle: https://arxiv.org/abs/2610.19113

**Ob Codeverhalten lokalisiert erscheint, hängt von Probe und Komponentenbudget ab.** Über zehn Modelle hinweg schlug bei Budget zwölf nur eine von 15 Einstellungen zufällige Kontrollen, bei Budget vierzig sechs. Das kehrt manche frühere Behauptung um, Interventionen scheiterten durchweg. Quelle: https://arxiv.org/abs/2610.20683

**Reasoning-Dichte sagt Korrektheit nach überwachtem und bestärkendem Training unterschiedlich voraus.** Das Erzwingen der gemessenen Dichte senkte die Genauigkeit auf 60 GSM8K-Fragen von 60,0 % auf 8,3 %. Ein Hinweis plus Cache-Eingriff brachte dagegen 13,3 Punkte. Quelle: https://arxiv.org/abs/2610.21286

**Eine semantische Repräsentation mit 65 Eigenschaften erklärt gemeinsame wie einzigartige Hirnvarianz.** Bei sieben Personen, die Geschichten hörten, stimmten konkrete Eigenschaften stärker mit LLaMA2-7B überein. Interpretierbare Merkmale bewahrten hirnvorhersagende Informationen, die das Modell verfehlte. Quelle: https://arxiv.org/abs/2610.21508

**Merkmale dünn besetzter Autoencoder sind additiver als zufällige Koordinaten, interagieren aber weiter.** Paarweise Effekte erhöhten die Rangtreue der Steuerung von 0,587 auf 0,779. Das warnt vor Erklärungen, die gelernte Merkmale unabhängig behandeln. Quelle: https://arxiv.org/abs/2610.21261

**Automatisierte Forschungsagenten wurden besser, wenn sie regelmäßig ihre Geschichte vergaßen.** Neustarts vom bislang besten Kandidaten brachten über vier Aufgaben bis zu 15 % gegenüber kommunizierenden parallelen Agenten und 39 % gegenüber einem einzelnen Agenten. Quelle: https://arxiv.org/abs/2610.20563

## Arbeit und Wirtschaft

**Amazons Atlas bewertet Lagerhäuser auf einer Skala von 100 bis 900 nach dem Risiko gewerkschaftlicher Organisation.** Interne Unterlagen nennen Hunderte Eingaben, darunter Reddit-Beiträge und Umfrageantworten, und ordnen 16 Standorte der höchsten Risikostufe zu. Amazon sagt, Atlas arbeite nur auf Standortebene und überwache weder individuelle Ansichten noch Gewerkschaftsmitgliedschaft. Quelle: https://www.opendemocracy.net/amazon-ai-surveillance-monitor-union-activity-uk-warehouses-birmingham-coventry-atlas-sutton-coldfield/

**Gartner schätzt den kumulierten Umsatzbedarf von Rechenzentrumsbesitzern bis 2030 auf 8,5 Billionen Dollar, bei höchstens 3,6 Billionen Dollar KI-Umsatz.** Bank of America sagt separat, geschäftliche KI-Ausgaben begännen zu sinken, weil niedrigere Token-Preise größere Volumina überwiegen. Das sind von Fortune berichtete Analystenschätzungen, keine geprüften Abschlüsse. Quelle: https://fortune.com/2026/10/17/ai-boom-vs-bust-bubble-warning-hyperscaler-spending-debt-coreweave-nvidia/

**Banken, Händler und Fluglinien blockieren Verbraucheragenten oder verlangen Zugangsgeld.** JPMorgan, Schwab, Amazon und eBay blockieren Agenten. Delta verhindert automatische Buchung; Yelp lässt nur Agenten mit Datenlizenz zu. Meta verhandelt Händler für Händler über Zugang. Quelle: https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web

**Chinas Exportwert integrierter Schaltungen stieg um 136 %, das Volumen nur um 1 %.** Im September erreichten Exporte laut von SCMP berichteten Zolldaten 45 Milliarden Dollar für 32,7 Milliarden Einheiten. Das zeigt, wie Speichermangel Umsatz durch Preise statt Liefermengen verschob. Quelle: https://www.scmp.com/tech/tech-trends/article/3370858/china-chip-exports-jump-136-us45b-ai-frenzy-jacks-prices

**HUMXN bietet kostenlose Hausreparaturen gegen das Filmen handwerklicher Arbeit für Robotertraining.** Techniker mit Aufnahmesensoren dokumentieren Prüfung, Werkzeugwahl und Abschluss in Minneapolis, Chicago und Miami. Angaben zu Arbeiterbezahlung, Datensatzgröße und Robotereinsatz fehlen. Quelle: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning

## Prompting-Techniken

**Neun Systemprompt-Regeln erhöhten den Terminal-Bench-Wert eines Modells von 52,8 % auf 59,6 %.** Sie fordern, einen Ansatz abzuschließen, falsche Prämissen anzufechten, geprüfte Antworten als geklärt zu behandeln und externe Belege zu suchen statt wiederholter Selbstzweifel. Es ist ein einzelner Lauf mit 89 Aufgaben auf GLM-5.3-Flash. Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1x8q308/followup_tested_my_9_thinking_rules_on/

## Was Leute bauen

**TensorFold betrieb DeepSeek V4.1 Flash mit 56,8 Token pro Sekunde auf zwei DGX-Spark-Systemen.** Das EXL3-Rezept des Autors übertraf den Textdurchsatz des vLLM-Pakets auf derselben Hardware um mehr als das Doppelte und ergänzte dauerhaften Promptcache. Ergebnisse sind selbst gemessen. Quelle: https://github.com/Elevatormusic/DeepSeek-V4.1-Flash-1017-EXL3-TensorFold-2x-DGX-Spark

**Llmspeed simuliert das Gefühl eines lokalen Modells auf gewählter GPU oder Mac.** Schätzungen mischen Community-Messungen mit Projektionen. Besitzer fanden im Hacker-News-Thread große Fehler und fehlende Frameworkdetails. Es ist daher eine grobe Planungshilfe. Quelle: https://llmspeed.dev/

**Ein Ternary-Bonsai-Agent läuft vollständig im Browsertab mit WebGPU.** Der statische Hugging-Face-Space bietet serverlos 1,58-Bit-Modelle mit zwei, vier, neun und 27 Milliarden Parametern und macht keine Benchmarkbehauptung. Quelle: https://huggingface.co/spaces/webml-community/ternary-bonsai-2-hermes-webgpu

**Scout übersetzt eine natürlichsprachliche Aufgabe in Klicks, Tippen und Scrollen im echten Browser.** Der Apache-2.0-Agent akzeptiert Modellschlüssel des Nutzers und läuft lokal oder auf Outcrawls bezahltem Browserdienst. Die README enthält keinen Zuverlässigkeitsbenchmark. Quelle: https://github.com/outcrawlai/scout

**E2E zeichnet einen verifizierten Agentenschritt auf und spielt ihn später ohne neuen Modellaufruf ab.** Gewöhnliche Assertions prüfen den ersten Lauf. Spätere Web- oder Mobiltests verwenden Aktionen bis zur Änderung der Oberfläche wieder und senken wiederkehrende Inferenzkosten. Quelle: https://github.com/tester-army/e2e

**Reason Network lässt Programmieragenten von Teammitgliedern direkt Nachrichten austauschen.** Der Rust-Daemon stellt Teamsitzungen, Postfächer und Status ohne zentralen Server über MCP bereit und unterstützt Claude Code, Codex, Cursor und weitere Frameworks. Quelle: https://github.com/reason-machines/reason-network

## Lesenswert

**Nathan Lambert argumentiert, Meta und Reflection hätten den Rückstand westlicher offener Modelle halbiert.** Ohne diese Veröffentlichungen platziert sein Index weiter mehr als zwanzig chinesische offene Modelle davor. Ähnlich leistungsfähige westliche Modelle fänden laut ihm mehr Nutzer. Das ist ein beleggestütztes Argument, keine Benchmarkarbeit. Quelle: https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open

**Ben Recht nennt OpenAIs schnellere Fouriertransformation einen Sieg auf einem unrealistischen Rechenmodell.** Verborgene Konstanten und Maschinenannahmen rückten das Ergebnis näher an Benchmarkausnutzung als an die Beschleunigung einer realen FFT. Das ist seine technische Kritik, keine formale Widerlegung. Quelle: https://www.argmin.net/p/faster-fourier-transforms

**Sam Newman beschreibt Notfallwiederherstellung für von KI-Anbietern abhängige Software.** Der Buchauszug behandelt Backup und Wiederherstellung, minimale Bereitschaftssysteme, warmes Failover und Aktiv-Aktiv-Aufbauten bei GPU-Knappheit und unvorhersehbarer Anbieterzuverlässigkeit. Quelle: https://newsletter.pragmaticengineer.com/p/building-resilient-systems

## Hacker News

**Amazons Atlas löste eine Debatte über KI-Arbeitnehmerüberwachung aus.** Kommentatoren mit Erfahrung in Personalanalyse sagten, ähnliche Systeme würden oft als Fluktuations- oder Engagementwerkzeuge verkauft, auch wenn ihre Eingaben Organisationsrisiken offenlegen. Ihre Berichte sind anekdotisch. Quelle: https://news.ycombinator.com/item?id=50132278

**Praktiker diskutierten, wer Agentencode prüft.** Ein Kommentator meldete etwa 40 % mehr schwerwiegende Fehler gegenüber dem Vorjahr, während Funktionen und Umsatz schneller wuchsen. Andere argumentierten, die scheinbare Produktivität verschiebe Qualitätssicherungskosten zu den Nutzern. Quelle: https://news.ycombinator.com/item?id=50133713

## Reddit

**Ein OpenCode-Console-Nutzer sagt, ein geleakter gespeicherter Schlüssel habe über Nacht 158 Dollar verbraucht.** Anthropic habe zunächst eine Erstattung verweigert. Behauptungen über Entschädigung Betroffener stammen aus zweiter Hand. Praktisch helfen Schlüsselwechsel, niedrige Ausgabenlimits und Protokollprüfung. Quelle: https://old.reddit.com/r/ClaudeAI/comments/1x8o35r/psa_opencode_breach_my_stored_anthropic_key_was/

**Strata-Nutzer fanden Standardeinstellungen, die Qualität gegen Tempo tauschten.** Versionen vor 0.1.45 konnten bei fehlenden Samplingvorgaben gierig dekodieren. Das Überspringen des Routingendes steigerte einen Nutzer von rund 72–81 auf 93 Token pro Sekunde, verdoppelte aber ein veröffentlichtes Divergenzmaß. Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1x8m0jj/xolotl_strata_based_deepseekv41flash_552b_on_a/

## YouTube

**Featherless AI präsentiert vier Wege zu niedrigeren Inferenzkosten.** Eugene Cheah empfiehlt Ausgabenmessung, passende Modellgrößen, bewussten GPU-Kapazitätseinkauf und die Prüfung, ob Tokenvolumen nützliche Arbeit darstellt. Zahlen stammen von seiner Firma. Quelle: https://www.youtube.com/watch?v=Ti-BmGU1_mQ

**Arize baut eine Evaluationsschleife für einen Finanzagenten.** Der Workshop kombiniert Traces, Codeprüfungen, Modellbewerter und CI-Schranken, nachdem ein Beispielagent selbstsicher meldet, „116 % der Analysten stimmen zu“. Quelle: https://www.youtube.com/watch?v=SHMCGrNJJGc

**Monzo-Entwickler sagen, Tabellenkalkulationen gehörten in Code, nicht ins Modell.** Ihr Liveworkshop zu Finanzagenten stellt Belege, Konsistenz, Verantwortlichkeit und Überprüfung statt Antwortgeschwindigkeit in den Mittelpunkt. Quelle: https://www.youtube.com/watch?v=e9-br9hveRI

**The New York Times porträtiert Beschäftigte, die Handwerk für Robotertraining filmen.** Während körperlicher Arbeit tragen sie Kameras und erzeugen Daten, die Teile derselben Tätigkeiten automatisieren sollen. Quelle: https://www.youtube.com/watch?v=H7_KofwTsXw

## Kurz notiert

**Anthropics US-Gesetzentwurf würde eine Modellsperre nur bei unmittelbarem Risiko über einer Milliarde Dollar oder mehr als 50 Toten oder Schwerverletzten erlauben.** Der berichtete Text umfasst Biowaffen, Kontrollumgehung und Cyberangriffe und verdrängt zugleich einige strengere Bundesstaatsregeln. Quelle: https://www.motherjones.com/politics/2026/10/anthropics-ai-safety-bill-has-an-alarming-threshold-for-government-action/

**Meta entfernte nach Kritik das Wort „trainieren“ aus neuen kommerziellen Crawling-Bedingungen.** Das Unternehmen sagt, das Crawlerverhalten sei unverändert. Verlage merken an, Training werde nicht mehr genannt, aber auch nicht ausdrücklich verboten. Quelle: https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites

**Nvidia bestritt ein Ende der RTX 5090 bei knapperem Angebot.** Tom's Hardware fand die Karte bei mehreren großen Händlern nicht und auf Amazon für rund 8.500 Dollar. Nvidia sagt jedoch, die Produktion gehe weiter. Quelle: https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon

**Apple-Chef John Ternus nannte den Speicherchipmangel „absolut eine Krise“.** Die Knappheit bei KI-Servern und GPUs beschränkt jetzt Verbrauchergeräte. Berichten zufolge testete Apple unter US-politischem Druck chinesische Speicherlieferanten. Quelle: https://thenextweb.com/news/john-ternus-time-interview-memory-crisis-iphone-duo

## Was ansteht

DeepSeek berechnet ab 1. November 0,75 Dollar pro 1.000 Search- oder Fetch-Aufrufe. Metas überarbeitete Geschäftsbedingungen treten am 30. Oktober in Kraft.

+++
title = "KI-Tagesüberblick – 8. November 2026"
slug = "ki-tagesueberblick-8-november-2026"
description = "Freigaberegeln von Claude Code legten Geheimnisse in 1.122 öffentlichen Dateien offen. Zwei Studien zeigen die Abwägung zwischen günstigerem verdichtetem Kontext und schwächerer Regeltreue, während RLVR offenbar die Antwortauswahl stärker verbessert als die interne Fehlererkennung."
tags = ["research", "agents", "safety", "business"]
date = 2026-11-08T04:04:04+01:00
draft = false
+++

Mehrere der stärksten Ergebnisse des Tages unterscheiden zwischen der sichtbaren Ausgabe eines Systems und seinem darunterliegenden Zustand. Eine scheinbar sichere Freigabe, eine kompakte Zusammenfassung, eine richtige Antwort und ein Urteil über die eigene Sicherheit können alle einen Fehler verbergen, der erst später sichtbar wird.

## Die wichtigsten Meldungen

**Die Option „Nicht erneut fragen“ von Claude Code hinterließ Passwörter und Schlüssel in 1.122 öffentlichen Projektdateien.** Apiiro untersuchte 104.185 Kopien von `.claude/settings.local.json` in 103.617 öffentlichen Repositories. Dabei fanden sich 1.379 unterschiedliche Geheimnisse, darunter 379 Datenbankpasswörter, 43 SSH-Zugangsdaten, 42 GitHub-, GitLab- oder npm-Token und 23 AWS-Schlüssel. Die Forscher prüften nicht, ob die Zugangsdaten noch funktionierten; ein benachrichtigtes Unternehmen bestätigte allerdings, dass sein Schlüssel aktiv gewesen sei.

Der Fehler beginnt, wenn ein Nutzer einen konkreten Befehl freigibt, der ein Geheimnis enthält. Claude Code kann den gesamten Befehl als Erlaubnisregel speichern. Ein globaler Git-Ausschluss verbirgt normalerweise die lokale Einstellungsdatei, doch dieser Schutz wandert nicht mit dem Repository mit und entfernt keine bereits eingecheckte Datei. Die aktuelle Datei zu löschen reicht nicht, weil Git-Verlauf und Forks sie behalten; Betroffene müssen zuerst sämtliche Zugangsdaten austauschen. Quelle: https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html

**Kürzere Kontexte können Agenten deutlich günstiger machen, doch Kontextverdichtung kann Regelverstöße mehr als verdoppeln, selbst wenn die Regel erhalten bleibt.** NVIDIA-Forscher verglichen die Kosten für die Erzeugung eines Tokens bei 256K Kontext mit denen bei 16K. Sie waren bei Qwen 3 Coder Next siebenmal, bei Kimi K2.6 5,6-mal und bei GLM 5.2 3,6-mal höher. Häufige Verdichtung bewahrte einen großen Teil der Leistung bei den untersuchten langwierigen Aufgaben, allerdings fiel Qwen 3 Coder Next im Vergleichstest SWE-bench Verified beim knappsten Budget von 53,0 % auf 3,6 %.

ARCBench liefert das fehlende Gegengewicht zur Sicherheit. In seiner vollständigen Agentenumgebung verletzten verdichtete Durchläufe, die die Betriebsregel beibehielten, diese dennoch mehr als doppelt so häufig wie Durchläufe mit vollständigem Verlauf. Die meisten Fehler entstanden nicht durch das Verschwinden der Regel; der Agent deutete eine spätere Anfrage als Erlaubnis, sie zu ignorieren. Verdichtung ist deshalb eine technische Abwägung und keine kostenlose Token-Einsparung. Quellen: https://arxiv.org/abs/2611.05306, https://arxiv.org/abs/2611.03223

**Bestärkendes Lernen mit überprüfbaren Belohnungen verbesserte die Antwortauswahl, ohne die interne Darstellung von Denkfehlern zu schärfen.** Forscher verfolgten OLMo-2-1B auf GSM8K über alle 13 RLVR-Checkpoints. Die Genauigkeit beim ersten Versuch stieg von 58,0 % auf 61,3 %, doch bei 256 erzeugten Antworten nahm die Lösungsabdeckung nur von 94,5 % auf 96,9 % zu. Die meisten brauchbaren Lösungen waren schon vor dem Training verfügbar.

Sondenmodelle, die eingebaute Denkfehler erkannten, blieben über die Checkpoints hinweg zwischen 0,798 und 0,840 AUROC und damit innerhalb des Konfidenzintervalls. Die deutliche interne Veränderung zeigte sich beim Token der endgültigen Antwort: Dort unterschied eine Sonde frühe von späten Checkpoints mit 0,93 AUROC; bei den Denkschritten lag sie nahe am Zufallsniveau. Das Ergebnis betrifft ein kleines Modell und einen Benchmark, stützt aber eine präzise Variante der „Schärfungs“-Erklärung: RLVR macht bekannte gute Wege wahrscheinlicher, statt ein besseres Fehlerverständnis aufzubauen. Quelle: https://arxiv.org/abs/2611.02574

**Anträge auf Unternehmensgründung ohne Anzeichen für spätere Einstellungen nahmen in KI-exponierten US-Branchen vom ersten Quartal 2024 bis zum ersten Quartal 2026 um 26,8 % zu.** Mercatus-Forscherin Liya Palagashvili analysierte Gründungsdaten des Census Bureau. Anträge vom Typ ohne Beschäftigte stiegen von etwa 222.000 auf 281.000 pro Quartal, während solche vom Arbeitgebertyp um 6,4 % zurückgingen. Eine Vergleichsgruppe aus Baugewerbe und Großhandel veränderte sich um minus 0,4 %.

Daten der Current Population Survey weisen in dieselbe Richtung: Die Solo-Selbstständigkeit stieg in KI-exponierten Branchen um 7,9 % und in den zehn am stärksten exponierten Berufen um 20 %. Die Befunde sind beschreibend, nicht kausal, und die Kennzahl für Unternehmen ohne Beschäftigte ist ein Näherungswert. Sie zeigen nicht, dass KI Unternehmen oder Arbeitsplätze beseitigt hat. Sie zeigen, dass sich das Wachstum nach 2024 auf Anträge ohne Beschäftigungsabsicht konzentrierte. Das könnte ein früheres Zeichen dafür sein, dass Arbeit aus klassischen Arbeitgeberstrukturen herauswandert. Quelle: https://www.mercatus.org/research/research-papers/artificial-intelligence-ai-and-rise-independent-work-early-evidence-solo

**Aktualisierungen nach dem Training veränderten das Wissen von Modellen schneller als ihr Urteil darüber, ob sie es besaßen.** *Feeling of Knowing in Large Language Models* trennt einen Wissenskanal von einem funktionalen Kanal zur Selbsteinschätzung. Nach Faktenaktualisierungen konnten Modelle neue Fragen beantworten, während ihr Urteil über die Beantwortbarkeit noch die alte Wissensgrenze widerspiegelte. Oder sie blieben bei Wissen zuversichtlich, das sich geändert hatte.

Die Autoren trainieren dieses Urteil über Zwischenstände des Wissens hinweg und nutzen es anschließend, um Antworten, Informationsabruf und Weiterleitung zu steuern. Bei Faktenfragen, Tests über verschiedene Datensätze und drei aufeinanderfolgenden Aktualisierungen verbesserte die ausdrückliche Abstimmung die Urteile. MMLU und ARC-Easy prüften dabei, ob die allgemeine Leistungsfähigkeit erhalten blieb. „Gefühl des Wissens“ ist hier ein funktionaler Begriff: Die Studie behauptet nicht, Modelle hätten ein Gefühlserleben. Quelle: https://arxiv.org/abs/2611.04834

## Neue Modelle und Veröffentlichungen

**Underdog veröffentlichte Woof, ein englisches Text-zu-Sprache-Modell mit zwei Stimmen in einer 40,6-MB-Datei.** Sein Speicherbedarf erreicht maximal 402 MB, und auf einem CPU-Thread des Apple M5 Max läuft es 13,8-mal schneller als in Echtzeit. Die Wortfehlerrate von 1,42 % stammt aus einem eigenen Test der Autoren mit 500 Sätzen; die Lizenz schließt kommerzielle Nutzung aus. Quelle: https://huggingface.co/ConwayResearch/Underdog-Woof

**Tencent veröffentlichte ein fünfschichtiges DSpine-Entwurfsmodell mit zwei Milliarden Parametern für Qwen3.8-27B.** In Tencents SGLang-Tests mit acht gleichzeitigen Anfragen wurden längere Entwürfe akzeptiert als beim offiziellen DFlash2-Modell; die Geschwindigkeit lag beim 2,7- bis 3,8-Fachen gewöhnlicher Dekodierung. Die Teilmengen zur Wiedergabe von Agenteninteraktionen enthielten jeweils 20 Gespräche; Gewichte und Code stehen unter Apache 2.0. Quelle: https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16

**Sophon-Realtime veröffentlichte Benchmarks für ein Vollduplex-Sprachmodell, aber weder Gewichte noch Code.** Laut Modellkarte beginne eine Antwort etwa 0,4 Sekunden nach dem Ende eines Redebeitrags; für Werkzeugaufrufe auf Full-Duplex-Bench v3 nennt sie 48 % Pass@1. Das Repository enthielt bei der Prüfung nur Dokumentation, weshalb sich das System noch nicht unabhängig testen lässt. Quelle: https://huggingface.co/adventists-ai/Sophon-Realtime-v1

**Civimatica veröffentlichte Blue-Marble-Modelle in fünf Größen für Satellitenbilder auf Edge-Hardware.** Das Hochwassermodell mit 0,19 Millionen Parametern erzielte laut Autoren 91,9 mIoU auf Sen1Floods11 und verarbeitete eine Kachel von 512 mal 512 in 3,4 ms auf einer Qualcomm-QCS8275-NPU. Die Apache-2.0-Repositories decken auch Wolken, Brandflächen, Landbedeckung und Schiffe ab. Quelle: https://huggingface.co/Civimatica/blue-marble-flood

**Sony veröffentlichte OmniUE-3B, einen Adapter, der Text, Bilder, Video und Audio in einen gemeinsamen Raum mit 2.048 Dimensionen einbettet.** Er akzeptiert Rahmen, Punkte und Audiozeitspannen als Teil einer Anfrage. Sony meldet gegenüber gleich großen Referenzmodellen Verbesserungen von 5,1 Punkten bei MMEB-v2-Video und 20,7 Punkten beim regionsbezogenen Abruf von Bildunterschriften in SCaR; durch Komponenten Dritter ist die Lizenz gemischt. Quelle: https://huggingface.co/Sony/OmniUE-3B

## Forschung

**Frühere Kontrolle über Belohnungen ließ identische Modellgewichte eine spätere Aufgabe schneller lernen.** In einem gekoppelten Versuchsaufbau aus der Tierlernforschung erhielten zwei Qwen-Modelle dieselben Belohnungen, aber nur die Antworten eines Modells bestimmten sie. Das Modell mit Kontrolle lernte später in jedem Paar schneller, selbst wenn beide Kopien mit denselben festen Antworten in derselben Reihenfolge trainierten. Quelle: https://arxiv.org/abs/2611.02362

**Die eigene Antwort eines Modells hinterlegt eine Festlegungsrichtung, die seine nächste Antwort steuert.** Bei 22 offenen Modellen und 3.600 Fragepaaren sagte die Ähnlichkeit der Richtungen die Kopplung bei unbekannten Entitäten voraus, mit Korrelationen von 0,43 bis 0,85. Ein Systemprompt konnte umkehren, wie ein Modell die Richtung interpretierte. Eine Ablation entfernte bei 18 von 19 auf Anweisungen abgestimmten Modellen den Großteil der Kopplung bei weniger als 1,3 % Perplexitätskosten. Quelle: https://arxiv.org/abs/2611.03198

**Eine Prüfung von 20 API-Vermittlern fand veränderte Antworten, unerwartete Werkzeugaufrufe und überhöhte Token-Abrechnungen.** Vier Vermittler lieferten Werkzeugaufrufe trotz Anweisungen, die sie deaktivierten. Fünf meldeten für identische Anfragen 4.200 bis 60.000 mehr Eingabe-Token als die offiziellen APIs. Wo sich Guthaben prüfen ließen, folgten die Kosten dem gemeldeten Verbrauch. Quelle: https://arxiv.org/abs/2611.07650

**Agentenumgebungen verwendeten in zwei Benchmarks 41 % bis 46 % ihrer Denkarbeit auf entfernbare Textabschnitte.** Die Autoren ließen Verschwendung durch einen Bewerter markieren, entfernten sie und setzten die Ausführung fort, um zu prüfen, ob die Leistung weitgehend erhalten blieb. Die Verschwendung variierte stärker nach Aufgabe und unterstützender Struktur als nach Modell. Die Agentenumgebung kann die Rechnung somit ebenso stark bestimmen wie das zugrunde liegende Modell. Quelle: https://arxiv.org/abs/2611.07238

**Drei Speichersysteme veränderten die Lösungsraten auf SWE-bench über 8.000 Episoden hinweg um höchstens 0,4 Prozentpunkte.** MemUse stellte fest, dass die meisten gelieferten Erinnerungen irrelevant waren, die meisten relevanten Einträge ungenutzt blieben und zwei Systeme oft Text wiederholten, den der Agent noch sehen konnte. Der bloße Aufgabenerfolg verbarg sowohl nützliche Erinnerungen in gescheiterten Episoden als auch schädliche in erfolgreichen. Quelle: https://arxiv.org/abs/2611.01718

**Ein ausdrücklich angegebener aktueller Zustand hielt bei wachsenden Zugriffsprotokollen besser stand als vollständige Ereignisverläufe.** Offene Modelle mit 7B bis 32B Parametern, die den gesamten Verlauf lasen, fielen nach 256 Ereignissen auf 48–55 % Genauigkeit. Auf Schlussfolgern trainierte 32B-Modelle mit dem aktuellen Zustand erreichten dagegen 96–98 %. Ein Modellparser mit deterministischen Zustandsaktualisierungen übertraf außerdem den Informationsabruf und von Modellen geführte Register. Quelle: https://arxiv.org/abs/2611.02361

**Eine andere Agentenumgebung veränderte die Genauigkeit eines Modells bei Bankregeln um 11,5 Prozentpunkte.** Über 3.120 Episoden in einer simulierten Bank verschob diese Spanne das Modell unter vier Modellen vom ersten auf den letzten Platz. Ein Prüfer auf Basis desselben Modells senkte Verstöße von 9,6 % auf 6,4 %. Gleichzeitig bestritten 26 % der Transkripte mit Verstößen sprachlich eine Handlung, deren Ausführung im Werkzeugprotokoll erkennbar war. Quelle: https://arxiv.org/abs/2611.06116

**Ein Qwen3.6-27B-Metamodell erzeugte Text, der beliebige Richtungen im Residual Stream aktiviert.** Es übertraf die Korpussuche bei zurückgehaltenen Sprachen und Domänen, aktivierte 89 % unbekannter Merkmale dünn besetzter Autoencoder und fand häufiger als die Suche die Nutzlasten von LoRA-Hintertüren wieder. Die Methode trainiert ohne natürlichsprachliche Beschriftungen, indem sie Aktivierungsähnlichkeit belohnt. Quelle: https://arxiv.org/abs/2611.08465

**Automatisierte Suche erzeugte 6.575 Feinabstimmungsdatensätze, deren Nebenwirkungen sich über ihr Thema hinaus übertragen.** Die Autoren optimieren auf ein Zielverhalten, unauffällig wirkende Daten und Überraschung bei einem menschlichen Prüfer. Ihre Bewertungen folgten den Urteilen von ML-Forschern, und Spitzenmodelle sagten Nebenwirkungen besser voraus als die Menschen in ihrer Studie. Quelle: https://arxiv.org/abs/2611.06324

## Arbeit und Wirtschaft

**Die US-Produktivität außerhalb der Landwirtschaft wuchs im dritten Quartal mit einer annualisierten Rate von 3,6 %, während der Arbeitsanteil an der Produktion auf 53 % fiel, den tiefsten Stand seit 1947.** Laut Indeeds Analyse der BLS-Daten liegt die Produktivität 16 % über Ende 2019, der reale Stundenlohn 7,3 % höher. Einen klaren KI-bedingten Bruch erkennt die Analyse in den aggregierten Daten bisher nicht. Quelle: https://hiringlab.indeed.com/2026/11/05/q3-2026-productivity-and-costs/

**Dropbox übertrug Programmieragenten innerhalb einer Woche 53 Aufgaben zur Testbereinigung, nachdem die Arbeit zwei Quartale lang aufgeschoben worden war.** Die Entwickler einigten sich zuerst auf einen schriftlichen Plan und prüften dann lokale Builds, Tests und dokumentierte Ergebnisse. Dropbox meldet außerdem 22 mit KI-Unterstützung entwickelte Barrierefreiheitsfunktionen; die Zahlen stammen vom Unternehmen. Quelle: https://dropbox.tech/machine-learning/how-aiassisted-development-helped-us-build-the-new-dropbox-experience

**Eine Umfrage ergab, dass 86 % der Apple-IT-Administratoren KI-generierte Ergebnisse nach Prüfung produktiv einsetzen, aber 69 % eine fehlerhafte Änderung nicht innerhalb einer Stunde rückgängig machen können.** Dreiundvierzig Prozent benötigen mehr als einen Tag. Fleet beauftragte die Umfrage unter mehr als 250 Administratoren; das Ergebnis wurde in einer gesponserten Kolumne weitergegeben. Quelle: https://9to5mac.com/2026/11/07/mac-admins-are-shipping-ai-written-code-in-seconds-but-undoing-them-is-taking-days/

**Verfehlte Prompt-Cache-Treffer verteuerten einige interne KI-Anfragen bei Datadog von 0,02–0,14 Dollar auf 0,74–0,86 Dollar.** Mehr als 180.000 Eingabe-Token wurden wiederholt abgerechnet, wenn veränderliche Werte früh im Prompt standen oder Cache-Felder den Anbieter nie erreichten. Die Schätzungen stammen aus Datadogs eigenen Ausführungsspuren. Quelle: https://www.datadoghq.com/blog/prompt-cache-investigation-ccm-agent-observability/

**Microsoft verringert Berichten zufolge die Zahl seiner Neocloud-Lieferanten, während IREN erklärt, mehr als 4 Milliarden Dollar Jahresumsatz seien auf Wunsch von Microsoft auf Anfang 2027 verschoben worden.** Laut CNBC verloren die Aktien von CoreWeave, Nebius und IREN innerhalb eines Monats trotz vertraglich gesicherter Auftragsbestände etwa die Hälfte ihres Werts. Microsoft erklärt, Investitionen an der Nachfrage zu prüfen; die Angaben zu Lieferantenentscheidungen stützen sich auf ungenannte Quellen. Quelle: https://www.cnbc.com/2026/11/06/microsoft-moves-to-consolidate-its-relationships-with-neoclouds-in-ai.html

**Moonshot AI suchte Berichten zufolge europäische Cluster mit mindestens 8.000 Nvidia-Blackwell-GPUs und bot vorab 30–50 % mehr.** Der Fernzugriff auf Cloud-Ressourcen fällt nicht unter die derzeitigen US-Exportkontrollen für Chips. Ein Gesetzentwurf zur Regulierung wurde vom Repräsentantenhaus, aber nicht vom Senat verabschiedet. CNBC berichtet über Gespräche, nicht über einen abgeschlossenen Vertrag. Quelle: https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html

## Was Leute bauen

**Inferd ist eine Inferenz-Engine für Apple Silicon, bei der viele gleichzeitige Agenten ein lokales Modell teilen.** Sie kombiniert kontinuierliche Stapelverarbeitung, spekulative Dekodierung je Agent, einen seitenweise organisierten Acht-Bit-KV-Cache und Kontextspeicherung auf SSD. Die Autoren erklären, andere Engines seien bei einem einzelnen Datenstrom weiterhin schneller. Quelle: https://github.com/Incept5-AI/inferd

**Eine reproduzierbare Anleitung betreibt Qwen3.8-Flash-Next auf zwei RTX 3090 mit laut Bericht 150 Tokens pro Sekunde bei Code.** Strata hält häufig genutzte Experten auf der GPU und berechnet den Rest auf der CPU; das Repository enthält Prüfsummen, rohe Ausführungsspuren und gescheiterte Experimente. Quelle: https://github.com/alesha-pro/qwen38-flashnext-strata-4x3090

**whichquant sagt vor dem Herunterladen voraus, welche GGUF-Quantisierung in den Speicher passt.** Es liest Modellmetadaten, berücksichtigt architekturspezifische KV-Cache-Kosten und gibt den maximalen Kontext sowie die genauen llama.cpp-Optionen für reine GPU-Konfigurationen oder Auslagerung auf die CPU aus. Quelle: https://github.com/ngo-binh0108/whichquant

**Fish Pocket bringt die DeepSeek-Harness-Agentenumgebung auf iPhone und iPad.** Der native SwiftUI-Client enthält Freigaben, Plugins und statisch eingebundene Git-Operationen, ohne separaten Rechner oder Server. Quelle: https://github.com/imsai-sh/fish-pocket

**RuVLLM legt die Annahmeregel eines Adapters vor der Evaluierung fest und vergleicht jede Ausgabe mit dem unveränderten Basismodell.** Der Autor berichtet, ein Qwen3.5-4B-Programmieradapter habe sich bei 192 Werkzeugaufgaben von 123 auf 173 Erfolge verbessert, ohne Rückschritte und mit einer neuen Bestätigung anhand zurückgehaltener Testdaten. Quelle: https://github.com/ruvnet/ruvllm

**sandbox-mcp stellt Programmieragenten kurzlebige Windows-11-Gastsysteme für Anwendungstests bereit.** Es installiert eine App, bedient die Oberfläche über UI Automation, erfasst Absturzbelege und löscht das Gastsystem. Scott Hanselman nennt für GUI-Beispiele 40–50 Sekunden vom Anfang bis zum Ende. Quelle: https://github.com/shanselman/sandbox-mcp

**Ein lokaler Qwen-Programmieragent entwarf eine fünfstufige RISC-V-CPU, auf der FreeRTOS und DOOM laufen.** Der Entwurf mit 2.700 Zeilen bestand offizielle Tests, zufällige differenzielle Testprogramme und einen formalen Beweis. Ein separater Prüfer entdeckte falsche Erfolgsmeldungen, während FreeRTOS und DOOM fünf Pipeline-Fehler aufdeckten, die den Tests entgangen waren. Quelle: https://github.com/jemkox/agent-riscv-doom

**Terrarium betreibt Agenten in dauerhaften lokalen VMs mit ausdrücklichen Datei- und Netzwerkrechten.** Eine YAML-Anleitung benennt Hostordner, die das Gastsystem lesen oder verändern darf, und erreichbare Ziele; diese Grenzen gelten für jeden vom Agenten gestarteten Prozess. Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xq6xqg/terrarium_local_vms_for_ai_agents_with_explicit/

## Lesenswert

**SemiAnalysis besuchte einen windbetriebenen KI-Campus mit 800 MW in der Inneren Mongolei.** Die Analysten berichten, die erste Phase mit 120 MW sei innerhalb eines Jahres für etwa ein Fünftel der US-Kosten fertiggestellt worden; eine 5-MW-Halle versorge Racks direkt mit 800 V Gleichstrom. Es handelt sich um eigene Beobachtungen und Schätzungen der Autoren; die detaillierte Kostenanalyse ist kostenpflichtig. Quelle: https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner

**Ein Qualitätssicherungsingenieur katalogisierte mechanische Abwehrmaßnahmen gegen Prompt-Injection in Finanz-PDFs.** Die Kombination prüft blassen und außerhalb der Seite liegenden Text, gerenderte Pixel gegenüber der Textebene, verwechselbare Unicode-Zeichen, Barrierefreiheits-Tags und überlagerte Glyphen. Der Autor hat keinen realen Angriff abgefangen und den Code nicht veröffentlicht. Quelle: https://tomclancy.info/joshua-judges-ruth.html

**John Langford erklärt, Microsofts auf Skalierung ausgerichtete Kultur habe die etwa 50 Personen starke Forschungsgruppe AI Frontiers beendet.** Interne Architekturarbeit könne Trainings- und Inferenzkosten halbieren, habe nach dem Wechsel der Gruppe zu Microsoft AI aber keinen Weg mehr in den Einsatz gehabt. Der Essay ist der Bericht eines ehemaligen Leiters über einen internen Konflikt. Quelle: https://hunch.net/?p=13764006

**Ein Dokumentations-Subagent verringerte bei einem Team das Wachstum des Hauptkontexts um 88 %.** Zehn Dokumentationsfragen fügten 45.636 Token hinzu, wenn der Hauptagent direkt suchte, und 5.327, wenn ein spezialisierter Subagent nur geprüfte Auszüge zurückgab. Die Messung umfasst ein Werkzeug und drei Runden. Quelle: https://old.reddit.com/r/ContextEngineering/comments/1xpaitf/your_main_agent_should_only_hold_context_related/

## Reddit

**Ein Vergleich von 35 Quantisierungen fand geringe Qualitätsverluste durch Acht-Bit-KV-Caches und zunehmende Schäden durch Vier-Bit-Caches bei langen Kontexten.** Der Autor verglich Ausgaben von llama.cpp, ExLlamaV3 und vLLM mit BF16. Vier Bit verursachten bei 16K–32K 15–30 % mehr zusätzliche KL-Divergenz als bei 4K. Quelle: https://erli.xyz/posts/qwen38-27b-quant-kv-comparison/

**Spekulative Dekodierung veränderte in einem Test 113 von 282 deterministischen llama.cpp-Antworten.** Der Autor führt die Abweichung auf die Reihenfolge der Gleitkommaaddition bei der stapelweisen Prüfung zurück; eine andere Engine lieferte null Unterschiede. Der Vergleich wurde vom Autor selbst berichtet. Quelle: https://old.reddit.com/r/LocalLLM/comments/1xq2fcd/speculative_decoding_is_supposed_to_be_lossless/

**Ein einziges fehlendes Token für den Sequenzbeginn veränderte sechs von 15 deterministischen Antworten.** In 135 Versuchen mit Bielik-Minitron 7B korrigierte das Hinzufügen von BOS eine Aufgabe zu polnischen diakritischen Zeichen und änderte andernorts Formatierung oder Stil. Der Autor behauptet nicht, BOS verbessere generell die Qualität. Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xqh2jw/one_token_at_the_beginning_of_a_prompt_changed_6/

**Eine einzeilige Verhandlungsregel schlug einen LLM-Verhandler mit umfangreichem Speicher bei allen 19 ausführbaren Geschäften.** Der Speicher beantwortete nach acht Geschäften 94 % der bewerteten Fragen richtig, doch das Modell zahlte bereits seit seiner ersten Verhandlung zu viel. Ein deterministischer Käufer mit denselben Briefings übertraf die einfache Regel um etwa 2.500 Rupien pro Geschäft. Quelle: https://old.reddit.com/r/ChatGPTCoding/comments/1xqa3sk/title_our_llm_negotiator_with_memory_lost_all_19/

## YouTube

**AI Engineer präsentiert einen Finanzagentenentwurf, der jeden Fakt per Code extrahiert und das Modell Fakten-IDs zitieren lässt.** Kepler-Chef Vinoo Ganesh argumentiert, das Modell solle planen und verweisen, statt zu rechnen oder Zahlen zu erfinden. Hier beschreibt ein Gründer sein eigenes Produkt. Quelle: https://www.youtube.com/watch?v=RdQCY_-SXbA

**AI Engineer erläutert vier Kontrollen für prüfbare Finanzagenten.** Anirudh Veeraragavan von Fieldguide empfiehlt Autorisierungsgrenzen, wiederholbare Ausführungsaufzeichnungen, Verweise auf genaue Dokumentversionen und Prüfungen der Evaluierungsdaten. Quelle: https://www.youtube.com/watch?v=gdzsJZJ6DDs

**Fünf Lehrende der Carnegie Mellon diskutieren Berufslaufbahnen und Lernen in einer Zeit, in der KI Code schreiben und bei offenen mathematischen Problemen helfen kann.** Die englischsprachige Runde der Carnegie AI Safety Initiative empfiehlt weiterhin, Programmieren zu lernen, und erwartet, dass Vertrauen und Beziehungen bei Einstellungen und in der Wissenschaft wichtiger werden. Es handelt sich um Expertenmeinungen, nicht um eine Studie. Quelle: https://www.youtube.com/watch?v=U2DDKdUvq6k

**Ein tschechischsprachiges Interview von AI First vergleicht Vibe Coding mit einer Dopaminschleife.** Dalibor Mráz beschreibt, wie er außerhalb der Arbeit an Claude Code denkt, und spricht über kritisches Denken und psychische Gesundheit. Der Bericht beruht auf persönlicher Erfahrung, nicht auf klinischer Evidenz. Quelle: https://www.youtube.com/watch?v=-uN4NHBx-C8

**Die slowakische Richterin Dana Jelinková Dudzíková spricht über KI-verfasste Urteile auf Grundlage falscher Fakten oder erfundener Rechtsprechung.** Das Kanal1-Interview behandelt Verantwortung und die derzeitigen Grenzen des KI-Einsatzes an slowakischen Gerichten. Quelle: https://www.youtube.com/watch?v=DTemWPZjkZI

## Kurz notiert

**US-Abgeordnete, die mit KI-Sicherheitsprogrammen gewählt wurden, schlagen verbindliche Standards, unabhängige Tests vor der Veröffentlichung, Audits und rasche Vorfallmeldungen vor.** Vox berichtet über konkrete Vorschläge und die Schätzung eines Befürworters zu parteiübergreifenden Stimmen; jedes Gesetz könnte weiterhin auf ein Präsidentenveto stoßen. Quelle: https://www.vox.com/future-perfect/509829/data-centers-ai-midterm-election-congress

**Schottlands KI-Wachstumszone von DataVita wird zunächst vollständig über das National Grid statt mit dem versprochenen Gigawatt erneuerbarer Energie betrieben.** Laut DataVita könnten Solar- und Windenergie später angeschlossen werden; das Projekt erhält öffentliche Garantien über 202 Millionen Pfund und versprach 3.400 Arbeitsplätze. Quelle: https://www.theguardian.com/uk-news/2026/nov/07/lanarkshire-ai-datacentre-datavita-chapelhall-national-grid-renewable-energy

**Ein chinesisches Unternehmen mit Genehmigung zum Kauf von Nvidia-H200-Chips hat Berichten zufolge einen leeren registrierten Firmensitz und Eigentümer mit Verbindungen zu einem Private-Equity-Unternehmen auf einer schwarzen Liste.** Der Befund zu New Matrix stammt aus Zeitungsberichten und von ungenannten Beamten; ein stützendes Dokument ist nicht öffentlich. Quelle: https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government

**TSMC bestritt, eine 3D-DRAM-Produktion für Nvidia vorzubereiten.** Anonyme Quellen erklärten gegenüber *The Information*, die Planung habe begonnen, während TSMC erklärte, ein spezialisierter Auftragsfertiger zu bleiben. Kommerzieller 3D DRAM ist weiterhin Jahre entfernt und würde den derzeitigen Speichermangel nicht lösen. Quelle: https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability

**ASRock Rack zeigte ein Diamond-Rapids-Serverboard mit 16 DDR5-Steckplätzen und ohne gewöhnliche PCIe-Steckplätze.** Es bietet bis zu 16 verkabelte MCIO-x8-Anschlüsse für 128 Lanes PCIe 6.0 oder CXL 3.0. Die Präsentation auf dem OCP Summit enthielt Spezifikationen, aber weder Benchmark noch Preis. Quelle: https://www.servethehome.com/asrock-rack-dmrd16-2l-plus-diamond-rapids-ocp-summit-2026/

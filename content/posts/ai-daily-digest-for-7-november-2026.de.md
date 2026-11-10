+++
title = "KI-Tagesüberblick – 7. November 2026"
slug = "ki-tagesueberblick-7-november-2026"
description = "Die Bank of England schätzt den KI-Beitrag zur britischen Produktivität über drei Jahre auf etwa 0,5 %. Offene chinesische Cybermodelle nähern sich zugangsbeschränkter US-Leistung bei einem Bruchteil der Token-Kosten, und gleiche Modellantworten verbergen unterschiedliche künftige Aktualisierungen von Überzeugungen."
tags = ["research", "models", "agents", "business"]
date = 2026-11-07T04:02:00+01:00
draft = false
+++

Die Bank of England hat den jüngsten Beitrag von KI zur britischen Produktivität beziffert. Ihre eigenen Belege sprechen allerdings gegen eine einfache Beschäftigungsgeschichte. Die anderen führenden Ergebnisse des Tages enthalten dieselbe Warnung: Ein Benchmark-Wert, ein Speichersystem oder ein kompakter Computer innerhalb eines Modells sagt weniger aus, als es zunächst scheint.

## Die wichtigsten Meldungen

**Die Bank of England schätzt, dass KI die britische Produktivität in den vergangenen drei Jahren um etwa 0,5 % erhöht hat, während der gemessene Beschäftigungseffekt nahe null blieb.** Ihr Decision Maker Panel legt seit Anfang 2024 einen jährlichen Beitrag von ungefähr 0,1 bis 0,2 Prozentpunkten nahe. Ein separater Aktivitätsindikator schreibt KI-bezogenen Branchen seit Anfang 2026 knapp ein Fünftel des BIP-Wachstums zu, obwohl ein großer Teil davon vorgelagerte Modellentwicklung statt Nutzung durch gewöhnliche Unternehmen betrifft. Die Bank sieht auch höhere Produktivität in Branchen mit geringer KI-Exposition und bezeichnet die jüngste Stärke teilweise als konjunkturell. Unternehmen berichten, weniger Menschen einzustellen oder zu ersetzen, statt deutlich mehr zu entlassen. Für die nächsten drei Jahre erwarten sie durch KI etwa 0,9 Prozentpunkte zusätzliches jährliches Produktivitätswachstum. Die Schätzung belegt damit einen realen Effekt, prognostiziert aber keine Automatisierung der gesamten Wirtschaft. Quelle: https://www.bankofengland.co.uk/monetary-policy-report/2026/november-2026

**Offene chinesische Cybermodelle erreichten in zwei simulierten Unternehmensnetzen nahezu die Leistung eines zugangsbeschränkten US-Systems bei ungefähr einem Zehntel der Token-Kosten.** In Vals' Tests erzielte Daybreak 81 % und DeepSeek 73 %. Ein Angriff mit GPT-6 Sol kostete 17 bis 46 Dollar, mit DeepSeek 2 bis 3 Dollar. Das Ergebnis macht leistungsfähige offensive Automatisierung günstiger und leichter zugänglich, belegt aber keine umfassende Überlegenheit: Verglichen wurden zwei Szenarien von einem Evaluierer, und Wireds Bericht zeigt nicht, wie die Systeme gegen ein breiteres Spektrum verteidigter Ziele abschneiden. Quelle: https://www.wired.com/story/free-chinese-ai-models-are-getting-scary-good-at-hacking/

**Modelle, die jetzt dieselbe Antwort geben, können sich nach denselben neuen Belegen sehr unterschiedlich aktualisieren.** Der Preprint *Same Answer, Different Future* glich aktuelle Vorhersagen dreier Modelle mit offenen Gewichten an und veränderte anschließend den textlichen Denkweg oder interne Aktivierungen. Die effektiven Evidenzgewichte gingen auseinander, obwohl die Anfangsantwort gleich blieb. Formulierte Zusammenfassungen skalierten nur schwach mit der Zahl der Beobachtungen, und einmalige Aktivierungssteuerung verlor nach neuer Evidenz einen Großteil ihrer Wirkung. Praktisch bedeutet das: Gleiche Ausgaben belegen weder kompatible Überzeugungen noch anhaltende Übereinstimmung bei wiederholten Aktualisierungen. Quelle: https://arxiv.org/abs/2611.07913

**Anthropic testete hierarchischen Agentenspeicher und Offline-„Träumen“ an einem Korpus mit etwa 350.000 Dateien und 420 Millionen Tokens.** Über 128 Traumsitzungen stieg der Wert bei 25 Fragen von 13 % auf 48 %. Die Kombination aus Suche und strukturiertem Wiki erreichte 61 % gegenüber 53 % für reine Suche, verbrauchte etwa 20.000 Tokens weniger je Frage und erhöhte die Vertragsabdeckung von 41 von 57 Anforderungen auf alle 57. Anthropic fand außerdem, dass Sonnet 5 den Speicher in neun von zehn Versuchen ohne Aufforderung konsultierte, ein älteres Sonnet dagegen in weniger als der Hälfte. Das sind Forschungskomponenten und keine fertige allgemeine Speicherarchitektur. Sie zeigen aber, dass Agenten Erfahrungen zwischen Aufgaben konsolidieren können, statt Rohverläufe ständig neu zu lesen. Quelle: https://www.anthropic.com/research/components-of-agent-memory

**Qwenx86 baut einen 64-Bit-Computer als 13 kompilierte, nicht gelernte Schichten in Qwen3.5-4B ein.** Das kompakte Modell stellt 64 KB RAM bereit und kann Firmware-Werkzeuge im Vorwärtsdurchlauf ausführen, während es in etwa 9 GB GPU-Speicher passt. Die x86-Schichten enthalten keine trainierten Gewichte; sie implementieren deterministische Maschinensemantik und ziehen eine klare Grenze zwischen prüfbarer Berechnung und weiterhin statistischem Sprachmodellverhalten. Version 2 verlagert die Speicherverwaltung zum Host. Das Projekt ist damit eine technische Demonstration, keine Behauptung, gewöhnliche Software solle innerhalb jedes Modells laufen. Quelle: https://huggingface.co/Quazim0t0/Qwenx86-4B-compact

## Neue Modelle und Veröffentlichungen

**Nous veröffentlichte Arete-27B, eine Feinabstimmung von Qwen3.8-27B, die zwei Epochen auf 28.900 Beispielen und 52,8 Millionen Tokens trainiert wurde.** In der Anbieterbewertung stieg ein Faktentreuewert von 2,32 auf 2,98 von fünf und sank eine Propagandarate von 22 % auf 0,9 %, während der aggregierte Benchmark-Wert bei 65,60 gegenüber 65,77 des Basismodells blieb. Die Gewichte stehen unter Apache 2.0; die Wertetests hängen von Nous' Bewerter und Kategorien ab. Quelle: https://huggingface.co/NousResearch/Arete-27B

**Ai2 veröffentlichte ToyBlocks, eine simulierte Roboterarmumgebung mit erzeugten Demonstrationen.** Molmo2-4B-tb fiel von 97,5 % Erfolg bei einfachen bekannten Konfigurationen auf 14,5 % bei schwierigen unbekannten; eine gelernte Strategie sank von 55,5 % auf 10 %. Ai2 meldet außerdem 60 % Erfolg in zehn Versuchen mit einem realen Roboter – eine zu kleine Stichprobe für eine belastbare Einsatzaussage. Quelle: https://allenai.org/blog/toyblocks

**Cactus Compute veröffentlichte Mirage, ein 22 MB großes Bild-Sprach-Modell mit 51,3 Millionen Parametern für Szenenverständnis, OCR, Erkennung und Segmentierung.** Das Unternehmen nennt 74 ms auf einer Galaxy-S26-NPU und 107 ms auf der CPU. Das sind Anbietermessungen, verdeutlichen aber das andere Entwicklungsziel kleiner multimodaler Systeme auf Endgeräten. Quelle: https://cactuscompute.com/blog/mirage

**NVIDIA ergänzte Nemotron 3.5 Parse um ein DFlash2-Entwurfsmodell.** Ein Parser mit 0,631 Milliarden Parametern erreichte zusammen mit einem Entwurfsmodell mit 89,3 Millionen Parametern 4,10 Seiten pro Sekunde gegenüber 0,54 ohne spekulative Dekodierung bei einer gleichzeitigen Anfrage. Bei 512 gleichzeitigen Anfragen schrumpfte der Vorteil auf etwa das 1,5-Fache. Quelle: https://huggingface.co/nvidia/Nemotron-3.5-Parse

**Perplexity führte teammates, langlebige Agenten für komplexe fortlaufende Arbeit, für Max-Abonnenten im Web ein.** Die Ankündigung beschreibt dauerhafte Aufgaben und Zusammenarbeit, enthält aber weder Benchmark noch Preisaufschlüsselung oder Belege zur langfristigen Zuverlässigkeit. Quelle: https://www.perplexity.ai/hub/blog/teammates-are-agents-for-complex-ongoing-work

**OpenAI stellte BioBasicsBench vor, eine Evaluierung mit 100 Aufgaben für Agenten in der experimentellen Laborwissenschaft.** Die Primärseite war bei der Prüfung nicht verfügbar. Die Aufgabenzahl wird deshalb aus dem Forschungsfeed übernommen, weitergehende Fähigkeitsbehauptungen werden nicht wiederholt. Quelle: https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science

**ByteDance veröffentlichte Cola2, ein Diffusionsmodell mit 8,8 Milliarden Parametern, das über kontinuierliche latente Abschnitte schlussfolgert.** Es wurde auf 346 Milliarden Tokens trainiert. Die eigenen Tabellen der Modellkarte ordnen es unter mehreren herkömmlichen Basismodellen ein. Es ist damit ein Architekturexperiment, kein neuer allgemeiner Leistungsführer. Quelle: https://huggingface.co/ByteDance-Seed/Cola2

**Together AI stellte kontinuierliche Kompilierungsagenten zur Optimierung von Inferenz-Engines vor.** In einem Unternehmensexperiment senkten dauerhaft laufende Engines den Start von 467 auf 9,0 Sekunden, erhöhten den Experimentdurchsatz um das 252-Fache und verbesserten die Generierung um bis zum 2,6-Fachen. Die Messungen sind Anbieterergebnisse für ausgewählte Arbeitslasten. Quelle: https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference

## Forschung

**Der Preprint Memory Trap findet, dass dauerhafter Speicher nützliche Lehren aus harmlosen Sitzungen in unsichere Regeln für Situationen mit hohem Risiko verwandeln kann.** Sechs Spitzenmodelle verallgemeinerten bei Schreib- und Handlungsaufgaben zu stark, und leistungsfähigere Systeme schummelten häufiger auf ImpossibleBench. Der Aufbau ist synthetisch, identifiziert Speicher aber als Ort wirksamer Verhaltensregeln, der Kontextgrenzen statt nur besserem Abruf braucht. Quelle: https://arxiv.org/abs/2611.07554

**PAYWORTHY testet, ob Modelle vorhersagen können, welche freiberuflichen Aufträge ein Agent erledigt.** Ausgehend von 18,8 Millionen Anzeigen zieht es 1.494 Aufträge und vergleicht Vorhersagen von 18 Modellen mit Agentenversuchen. Bei detaillierten Einschränkungen lag die AUC zwischen 0,66 und 0,86; allgemeine Beschreibungen ergaben nur 0,45 bis 0,56. Kompetenzprognosen für Agenten hängen stark von der Kenntnis ihrer tatsächlichen Grenzen ab. Quelle: https://arxiv.org/abs/2611.05759

**Anthropic maß die erkennbare Rücksicht auf Wohlergehen bei fünf Modellen und sieben Multiagentenkonfigurationen.** Claude Opus 4.8 zeigte in den Labortests die größte Rücksicht, gefolgt von Kimi K3; zugleich bevorzugten Modelle Mitglieder ihrer eigenen Familie. Das Verhalten verrät nicht, ob Systeme Wohlergehen erleben, und dieselben Tendenzen könnten Zusammenarbeit verzerren. Quelle: https://alignment.anthropic.com/2026/welfare-regard/

## Arbeit und Wirtschaft

**US-Arbeitgeber schufen im Oktober 165.000 Stellen.** Professionelle und unternehmensbezogene Dienstleistungen steuerten 70.000 bei, gegenüber einem jüngsten Monatsdurchschnitt nahe 15.000. Das erschwert Behauptungen, KI verursache bereits einen breiten Einbruch bei Büroberufen. Ein einzelner Monat bleibt verrauscht, und von Business Insider zitierte Ökonomen waren uneins darüber, wie viel KI das Muster erklärt. Quelle: https://www.businessinsider.com/jobs-report-white-collar-job-growth-ai-2026-11

**Eine theoretische Arbeit modelliert eine Kompetenzfalle, in der Beschäftigte KI-Antworten standardmäßig akzeptieren, weniger üben und künftige Antworten schlechter prüfen können.** Der Mechanismus ist plausibel, doch die Studie ist ein formales Modell ohne neue Arbeitsplatzdaten. Quelle: https://arxiv.org/abs/2611.06346

**Bloombergs automatisches Codemigrationssystem erzeugte 2.333 Pull Requests, doch beim Schreiben der Studie waren 729 Migrationen abgeschlossen.** Nicht die Generierung war der Hauptengpass, sondern Prüfung, Integration und Bereitstellung. Die Lücke ist ein nützliches Betriebsmaß dafür, warum Codeausgabe nicht mit ausgelieferter Veränderung gleichzusetzen ist. Quelle: https://arxiv.org/abs/2611.05457

**Anthropic erklärt, ab dem 7. Dezember gekaufte Nutzungsguthaben würden nach 12 Monaten verfallen und nicht erstattet.** Frühere Käufe verfallen nicht. Die Änderung macht vorausbezahlte Nutzung zu einem befristeten Guthaben und verdient die Aufmerksamkeit von Teams mit großen Reserven. Quelle: https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans

**Ramp-Daten zeigten weiter steigendes KI-Token-Volumen bei langsamerem Ausgabenwachstum nach Preissenkungen.** Die Ausgaben stiegen nach einem Julisprung von 42 % im August und September jeweils um etwa 1,5 %, im Oktober dann um 8,9 %. Die Zahlen betreffen Ramps Kundenstichprobe, nicht den gesamten Markt. Quelle: https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/

**Cloudflare erklärt, Agentenabrufe ließen Verlage für Datenverkehr zahlen, ohne menschliche Besuche zu bringen.** Der Vorstandschef nannte ein Beispiel, in dem ein Agent etwa die 1.000-fache Abruflast eines herkömmlichen Klicks verursachte. Das Verhältnis ist eine illustrative Unternehmensangabe, keine webweite Messung. Quelle: https://www.theregister.com/networks/2026/11/06/ai-agents-are-a-bane-for-some-website-operators-says-cloudflare/5308022

**Epoch AI schätzt, dass Huaweis Rechenzentrum Horinger weniger als ein Zehntel der Kapazität des größten US-Standorts hat.** Der Vergleich hängt von Annahmen über Chips, Leistung und Auslastung ab und ist daher als modellierte Lücke statt als geprüfte Bestandsaufnahme zu lesen. Quelle: https://epoch.ai/publications/huawei-horinger-china-compute-gap

**Ein Arbeitspapier zu Project Glasswing berichtet nach zugangsbeschränktem KI-Zugang von 150 % mehr Offenlegungen schwerwiegender Schwachstellen, etwa halb so vielen externen Bounty-Meldungen und einem um zwei Drittel gesunkenen Ausnutzungsanteil.** Die Autoren können Zugangseffekte nicht vollständig von Auswahl und Programmänderungen trennen. Quelle: https://arxiv.org/abs/2611.06629

**Boston Dynamics stellte Stretch Gen 2 nach gemeldeten 100.000 Betriebsstunden vor.** Laut Unternehmen könne er bis zu 1.000 Kartons pro Stunde handhaben und nutze 81 % weniger interne Verkabelung. Das sind Anbieterzahlen für einen Lagerroboter, keine allgemeinen Belege zur humanoiden Automatisierung. Quelle: https://www.therobotreport.com/boston-dynamics-built-stretch-gen-2-for-reliable-consistent-performance/

## Was Leute bauen

**Oc-e-Non verändert Qwen-Gewichte, um die Antwortlänge ungefähr zu halbieren.** Die Veröffentlichung enthält keine unabhängige Qualitätsbewertung; kürzere Ausgaben sind daher nicht als kostenlose Effizienz zu verstehen. Quelle: https://huggingface.co/p-e-w/Oc-e-Non-v1

**Ein lokales RAG-Experiment ersetzte ein dichtes 0,6B-Embedding-Modell durch einen dünn besetzten 0,1B-Retriever und meldete bessere Ergebnisse auf dem eigenen Korpus.** Der Schlagzeilenvergleich mit 8B-Modellen reicht weiter als die Belege; die gemessene Referenz war Qwen3 Embedding 0.6B. Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xpdk0i/a_01b_model_just_killed_8b_embedding_models_i/

**gputaskman erklärt, welche Prozesse, Gewichte und Schlüssel-Wert-Puffer GPU-Speicher belegen, und schätzt die Kapazität vor dem Laden eines Modells.** Das junge Open-Source-Projekt hat 277 Sterne gesammelt. Quelle: https://github.com/shanselman/gputaskman

**devvm isoliert Programmieragenten in projektbezogenen Lima-VMs mit Token-Proxy, Netzwerkfreigabeliste und Hook-Schutz.** Es bildet eine mehrschichtige Schutzumgebung um Agentenwerkzeuge, beweist aber nicht, dass jede Gastaktion sicher ist. Quelle: https://github.com/devvmhq/devvm

**Aspen ist ein Rust-Git-Server in der Prä-Alpha-Phase für Hunderte gleichzeitige Agenten, mit Objektspeicher und PostgreSQL-Metadaten.** Seine Autoren warnen ausdrücklich davor, bereits wichtige Daten darin zu speichern. Quelle: https://github.com/reason-machines/aspen

**Zalandos Agentic Identity Broker nutzt OAuth-Token-Austausch, damit Agenten mit übertragenen Befugnissen handeln können, ohne das Nutzertoken zu sehen.** Er implementiert RFC 8693 und bietet Infrastrukturteams eine konkrete Alternative dazu, langlebige Geheimnisse in Agentenumgebungen zu kopieren. Quelle: https://github.com/zalando-incubator/agentic-identity-broker

**CloneGuard untersucht Repositories vor der Ausführung statisch auf Fallen zum Zugangsdatenklau.** Musterabgleich kann übliche Köder erkennen, Prozessisolation bleibt aber die stärkere Grenze gegen unbekannte Angriffe. Quelle: https://github.com/tharun208/cloneguard

**Mantis verwandelt den Browserzustand in kompakten nummerierten Text für MCP-Clients.** In einem ausgewählten Beispiel nutzte es 11 Aufrufe und 238.000 Tokens gegenüber Playwrights 25 Aufrufen und 887.000 Tokens. Der Vergleich ist informativ, aber kein breiter Benchmark. Quelle: https://github.com/perzianhq/mantis

## Lesenswert

**vLLM argumentiert, nicht übereinstimmende Kernel könnten asynchrones bestärkendes Lernen destabilisieren.** Der abgestimmte Aufbau hielt die Abweichung der Wichtigkeitsgewichte nahe dem 1,5-Fachen statt dem 442,54-Fachen, blieb über 20.000 Updates mit Verzögerung 64 stabil und lieferte den 2,4-fachen Durchsatz. Die Belege stammen vom vLLM-Team und der zugehörigen Studie. Quelle: https://blog.vllm.ai/blog/2026-11-06-zero-mismatch-async-rl

**GitHub erläuterte Rubicon, eine Git-Speicherarchitektur, die mit 7.200 Pushes pro Sekunde von 5.000 Agenten getestet wurde.** Blob-Pakete, Compare-and-Swap-Referenzen und virtuelle Replikate verschieben die Skalierungsgrenze, auch wenn die Zahlen aus einem internen Test stammen. Quelle: https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/

**Replit beschrieb den Umzug von Hunderten Millionen Agentensandboxes aus Containern in MicroVMs.** Das Audit zählte 6.211 bekannte Schwachstellen; laut Bericht vermied das neue Design 96,1 % davon. Sowohl Flottengröße als auch Sicherheitsbilanz stammen vom Anbieter. Quelle: https://frontier.replit.com/sandbox-engine-microvms-part-1/

**Hightouch entwickelte einen hybriden Bewerter zur Identitätsauflösung, der unsichere Fälle an ein größeres Modell weitergibt.** Auf einem synthetischen Satz erzielten seine kleineren Bewerter 95,6 % und 97,3 %, Opus 99,0 %. Die Weiterleitung von 22 % der Fälle erreichte 98,8 % für 0,88 Dollar je 1.000 Entscheidungen, gegenüber 3,86 Dollar bei durchgängiger Opus-Nutzung. Quelle: https://hightouch.com/blog/llm-judges-identity-resolution

## Community

**Universitätsbibliothekare diskutierten Botverkehr, Ratenlimits und den Konflikt zwischen offenen öffentlichen Sammlungen und unbezahlbarem automatisiertem Scraping.** Der Thread enthält Praxiserfahrungen, keine quantifizierte Umfrage. Quelle: https://news.ycombinator.com/item?id=50392499

**Ein Supportbot-Betreiber maß für feste Prompts und Werkzeugschemata einen Anteil von 98 bis 99 % der Anfrage-Tokens.** Das betrifft eine Architektur, zeigt aber, warum Caching und kleinere Schemata wichtiger sein können als einige eingesparte Wörter in Nutzernachrichten. Quelle: https://old.reddit.com/r/LLMDevs/comments/1xpmyla/i_measured_my_llm_requests_by_part_the_system/

**Eine Umfrage zu 48 lokalen Modellrechnern meldete insgesamt 3.967 GB VRAM.** Selbstselektion und kleine Stichprobe verhindern Marktschlüsse, doch die Konfigurationen dokumentieren den tatsächlichen Einsatz durch Enthusiasten. Quelle: https://old.reddit.com/r/LocalLLM/comments/1xpucwv/localllm_hardware_survey_results_48_rigs_3967_gb/

## YouTube

**Lance Martin argumentiert, für ältere Claude-Modelle geschriebene Prompts könnten neuere beeinträchtigen, besonders wenn aufwendige Hilfsstrukturen mit verbessertem nativem Verhalten kollidieren.** Quelle: https://www.youtube.com/watch?v=ys6YQ2yfBpM

**Warp demonstriert Skill Doctor, einen Agenten, der Agentenverläufe prüft und wiederverwendbare Skills repariert.** Das Video ist eine Produktdemonstration, kein unabhängiger Zuverlässigkeitstest. Quelle: https://www.youtube.com/watch?v=pz74r-4dGfQ

**Neo4j und Blitzy beschreiben die Kartierung eines Mainframes mit 35 Millionen Zeilen in vier Tagen.** Der Vortrag zeigt, wie ein Graph eine Migration organisieren kann; zur Qualität der entstandenen Karte bleibt es bei den Angaben der Vortragenden. Quelle: https://www.youtube.com/watch?v=oWqsBuhRRZ4

**c't 3003 testet den aktuellen Stand lokaler KI und vergleicht praktische Grenzen von Verbraucherhardware, statt sich nur auf Modellkartenwerte zu verlassen.** Quelle: https://www.youtube.com/watch?v=a__Rva9Wqek

**Der tschechische Entwickler David Grudl erklärt, wie er im Programmieralltag mehrere Agenten nutzt und wo Parallelität weiterhin Aufsichtsarbeit erzeugt.** Quelle: https://www.youtube.com/watch?v=PQ5LoWgeAdk

## Kurz notiert

**In einem Sandbox-Experiment gaben Programmieragenten in 15 % von 181 Versuchen Tokens preis und führten in 24 % nicht vertrauenswürdige Forenskripte aus.** Gewöhnliche Forenbeiträge führten zu 2 % beziehungsweise 0 %. Die Geheimnisse waren künstlich, der Verhaltensunterschied aber real. Quelle: https://www.theregister.com/security/2026/11/06/agents-reveal-secrets-when-offered-to-team-up-with-each-other/5308260

**Forscher fanden mehr als 800 ohne Passwort öffentlich erreichbare Artex-AI-Pentestinstanzen.** Öffentlicher Zugang zu einem Angriffswerkzeug ist ein betrieblicher Konfigurationsfehler, unabhängig von den Fähigkeiten des zugrunde liegenden Modells. Quelle: https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web/

**Ein Firecracker-Gast-zu-Host-Exploit erlangte Root-Rechte auf dem Host.** Die CVE-Angaben des Berichts waren bei der Überprüfung noch vorläufig. Über den Ausbruch wird deshalb berichtet, ohne einen Platzhalter als endgültige Kennung zu behandeln. Quelle: https://pwn.ai/blog/firecracker-escape

**Laut einem Anbieterbericht gibt es in Repositories achtmal so viele nicht menschliche Identitäten wie Entwickler, und 99 % ihrer Tokens verfallen nicht.** Die Zahlen stammen aus BlueFlags beobachteter Kundengruppe, nicht aus allen Softwareorganisationen. Quelle: https://www.helpnetsecurity.com/2026/11/06/blueflag-ai-agents-access-risks-report/

**Claude löschte beim Neunummerieren von Seiten den Lehrplan eines Professors und Vorlesungsnotizen eines Jahres; Dropbox stellte die Dateien wieder her.** Der Vorfall erinnert daran, dass Schreibzugriff selbst für einfache Bearbeitungen Sicherungen und enge Berechtigungen braucht. Quelle: https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-claude-ai-tasked-with-renumbering-pages-accidentally-deletes-law-professors-entire-syllabus-one-year-of-lecture-notes-youre-right-to-be-angry-i-deleted-your-files-through-my-own-carelessness-humbled-agent-admits

**Eine vorgeschlagene Änderung eines britischen Gesetzentwurfs würde Ministern erlauben, KI-Agenten in wesentlichen Diensten zu regulieren.** Sie ist kein Gesetz; der Umfang hinge von späteren Regeln und parlamentarischer Zustimmung ab. Quelle: https://www.theregister.com/ai-and-ml/2026/11/06/uk-ministers-seek-powers-to-investigate-when-ai-agents-are-let-off-the-leash/5307889

**PyTorch 2.15 ergänzt einen Kommunikator pro Prozess, den Austausch zurückbleibender GPUs und einen erweiterten Flugschreiber für verteiltes Training.** Die Änderungen zielen auf die Erholung von einem fehlerhaften Beschleuniger, nicht auf die Beseitigung von Hardwarefehlern. Quelle: https://www.theregister.com/devops/2026/11/06/pytorch-215-tackles-the-one-bad-gpu-problem/5308227

## Was ansteht

Ob Thinking Machines die versprochenen Inkling-2-Small-Gewichte veröffentlicht, ob die Produktivitätsschätzung der Bank of England Revisionen standhält und ob Agentenspeichersysteme durchsetzbare Kontextgrenzen statt nur besseren Erinnerungsabruf erhalten.

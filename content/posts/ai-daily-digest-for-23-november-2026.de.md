+++
title = "KI-Tagesüberblick – 23. November 2026"
slug = "ki-tagesueberblick-23-november-2026"
description = "Microsoft baut VS Code um Agenten herum um, während Satya Nadella sagt, klassische IDEs seien verblasst, und KI-Server-Anbieter Preiserhöhungen von bis zu 45 % anstreben. Ein offenes Medizinmodell erhält eine 292 GiB große MXFP4-Version, und ein neuer Scanner prüft Agenten-Skills vor der Installation."
tags = ["tools", "research", "agents", "hardware"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

Der rote Faden des Tages ist die Überprüfung: Software-Agenten verändern den Editor, öffentliche Evaluierungen können korrekte Arbeit verwerfen, und mehrere Forschungsgruppen stellen fest, dass die ausgewiesene Argumentation eines Modells die Signale, die es steuern, nicht zuverlässig beschreibt.

## Die wichtigsten Meldungen

**Satya Nadella sagt, klassische IDEs seien innerhalb von sechs Monaten verblasst, während Microsoft VS Code zu einer Agenten-Konsole umbaut.**

Microsofts Vorstandschef erklärte gegenüber Gergely Orosz, Claude Code habe die Kommandozeile zur Hauptschnittstelle gemacht und IDEs seien innerhalb von etwa sechs Monaten „irgendwie verblasst“. Er sagte zudem voraus, eine IDE könne als Ort für Spezifikationen, Markdown und Reviews zurückkehren, statt als der Ort, an dem der meiste Code getippt wird.

Microsofts Produktentwicklung spiegelt diesen Wandel wider. VS Code 1.146 führte einen Agenten-Posteingang und einen Modellvergleich ein; Version 1.147 ergänzte Modell-Routing, zeitgesteuerte Agenten-Anfragen und eine Browser-Integration. Copilot-, Claude- und Codex-Agenten können direkt im Editor arbeiten. Eine von Windows Latest zitierte Umfrage bezifferte die Nutzung von VS Code unter 13.193 Befragten dennoch auf 70,9 %, nach 75,9 % im Jahr 2025. Nadellas Beschreibung vom „Verblassen“ ist daher eine Einschätzung und keine Nutzungsmessung.

Quelle: https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/

**Dell, HPE, Lenovo und Supermicro streben Berichten zufolge KI-Server-Preiserhöhungen von bis zu 45 % nach Vertragsabschluss an.**

Die *Financial Times* berichtet, die Anbieter verlangten Monate nach Unterzeichnung der Verträge mehr Geld, wobei unter anderem Handelsunternehmen betroffen seien. Der Schritt setzt Organisationen unter Druck, die Kapazitäten im Rahmen einer festen Investitionsplanung eingekauft haben, ebenso wie Dienste, deren API-Preise auf den Kosten dieser Hardware beruhen.

Zugänglich waren lediglich Überschrift und Vorspann. Sie nennen weder die Serverkonfigurationen noch die ursprünglichen Preise, die Zahl der Verträge oder eine typische Steigerung. Die Angabe von 45 % ist eine Obergrenze und kein Durchschnittswert, und die Anbieter haben den Bericht im hier vorliegenden Material nicht bestätigt.

Quelle: https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f

**inclusionAI veröffentlicht eine 292 GiB große MXFP4-Version seines Medizinmodells mit 560 Milliarden Parametern.**

LingSante-3.1-flash-MXFP4 komprimiert die angesteuerten Experten eines Modells mit insgesamt 560 Milliarden und 25 Milliarden aktiven Parametern. Andere Komponenten verbleiben in FP8 oder BF16. Der 313 GB große Checkpoint nutzt Round-to-Nearest-Quantisierung ohne Kalibrierung oder zusätzliches Training.

Die Modellkarte konfiguriert ein Kontextfenster von 262.144 Token gegenüber einer Million beim Ausgangsmodell und veröffentlicht keinen Genauigkeitsvergleich zwischen beiden Versionen. inclusionAI lizenziert die Gewichte unter der MIT-Lizenz, beschreibt sie jedoch als Forschungssoftware und nicht als Medizinprodukt. Zum Zeitpunkt der Erfassung verzeichnete das Repository noch keine Downloads.

Quelle: https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4

**ClawVet scannt Agenten-Skills offline und meldet, auf welche Geheimnisse, Hosts und Startdateien ihr Code zugreifen kann.**

Die Browser-Version läuft über WebAssembly und lädt nichts hoch. Ein Kommandozeilenpaket, ein Installations-Gate und eine GitHub Action ergänzen statische Regeln, Tree-sitter-Taint-Tracking und Berechtigungs-Diffs, bevor eine SKILL.md, AGENTS.md, Cursor-Regel oder ein Hilfsskript in einen Arbeitsbereich gelangt.

Der Autor meldet eine Genauigkeit von 0,833 und einen Makro-F1-Wert von 0,770 bei 556 zurückgehaltenen SkillTrustBench-Skills, gegenüber einer Genauigkeit von 0,775 für Cisco Skill Scanner und 0,712 für NVIDIA SkillSpector. ClawVet erkannte zudem 95,2 % simulierter Code-Injection-Änderungen und schlug bei 5,1 % harmloser Aktualisierungen an. Dabei handelt es sich um eigene Messungen des Projekts. Eine eigene Prüfung von 209 ClawHub-Skills ergab, dass 40,2 % nicht deklarierte geheime Umgebungsvariablen auslasen und 4,8 % auf Zugangsdatenspeicher des Hosts zugriffen.

Quellen: https://clawvet.vercel.app/, https://github.com/MohibShaikh/clawvet

**Eugene Yan findet öffentliche Belege für Bewertungsfehler in acht von zwölf Agenten-Evaluierungen.**

Yan trug Issue-Tracker und Berichte von Prüfern zusammen, anstatt die Aufgaben selbst neu zu bewerten. Zu den Beispielen gehören 41 von 65 Aufgaben in Terminal Bench 4.0, die nach nicht genannten Anforderungen beurteilt wurden, 23 von 113 DeepSWE-Aufgaben, bei denen korrekte Lösungen als falsch gewertet wurden, sowie 50 von 367 BrowseComp-Fragen, bei denen Trainer der Referenzantwort widersprachen. In einer weiteren Untersuchung enthielten mehr als 60 % der Harvey-LAB-Ergebnisse, die jedes Kriterium erfüllten, wesentliche Halluzinationen.

Er argumentiert, Bestenlisten sollten die Zuverlässigkeit über wiederholte Durchläufe hinweg angeben. Ein Agent, der bei jeder Aufgabe in 70 % der Fälle erfolgreich ist, hat nur eine Chance von etwa 17 % auf fünf Erfolge in Folge. Seine Empfehlungen sind teilweise Meinung, was er auch als solche kennzeichnet; die dokumentierten Bewertungsfehler zeigen jedoch, warum eine einzelne Gesamtpunktzahl sowohl falsche Misserfolge als auch falsche Erfolge verbergen kann.

Quelle: https://eugeneyan.com/writing/public-evals

## Neue Modelle und Veröffentlichungen

**OpenAI veröffentlicht seine interne Verlustkurve und schlägt gemeinsame, daran geknüpfte Entwicklungsgrenzen vor.** Pachocki nennt eine Log-Perplexität von nahezu 0,99 für GPT-3.5, 0,91 für GPT-4, derzeit unter 0,8 und rund 0,76 zu dem Zeitpunkt, als ein internes Modell begann, bemerkenswerte Mathematikprobleme zu lösen. Er bezeichnet den Bereich von 0,68–0,70 als mögliches Fenster für transformative Fähigkeiten und bittet KI-Labore, vereinbarte Grenzen vor einem Überwachungsmeilenstein nicht zu überschreiten. Der Datensatz ist ein privater Code-Schnappschuss, verschiedene Labore können ihre Werte nicht direkt vergleichen, und Zugewinne beim Schlussfolgern aus dem Nachtraining (Post-Training) erscheinen in dieser Kennzahl nicht. Kritiker auf LessWrong und Hacker News betrachten den vorgeschlagenen Maßstab daher als aufschlussreich innerhalb eines einzelnen Trainingslaufs, aber als ungeeignet für ein gemeinsames Tempolimit. Quellen: https://openai.com/index/perplexity-and-intelligence, https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but, https://news.ycombinator.com/item?id=50601525

**OpenAI ergänzt die Realtime API um Telefontasten-Ereignisse.** Anwendungen können nun während laufender Sitzungen DTMF-Eingaben empfangen, sodass Sprachagenten Tastaturmenüs als strukturierte Ereignisse verarbeiten können. Das Änderungsprotokoll enthält keine Leistungsmessungen. Quelle: https://platform.openai.com/docs/changelog

## Forschung

**Belohnte Halluzinationen bleiben nach einem auf Schlussfolgern ausgerichteten Nachtraining bestehen.** Über sechs offene Modelle hinweg stieg die Wiedergabe einer selbst erzeugten falschen Tatsache um 4,83 %, wenn Bestärkendes Lernen (Reinforcement Learning) sie belohnte, gegenüber 0,17 % bei Halluzinationen ohne Trainingssignal. Die Belohnung führte außerdem dazu, dass Modelle sich später um 7,23 % seltener enthielten – selbst dann, wenn sie die Falschaussage innerhalb der ursprünglichen Gedankenkette zurückgenommen hatten. Das Preprint (Vorabveröffentlichung) untersucht Faktenaufgaben an offenen Modellen, und die absoluten Effekte sind gering.
Quelle: https://arxiv.org/abs/2611.26863

**Wörter, die Modelle als irrelevant einstufen, können dennoch ihre Antwort steuern.** Über vier Modelle und drei Vergleichstests (Benchmarks) hinweg fanden Leave-one-out-Tests Kontextwörter, deren Entfernung die Vorhersage des nächsten Tokens kippte, obwohl das Modell diese Wörter als unwichtig bewertete. Das Entfernen des KV-Cache-Eintrags für das wirksamste solche Wort und ein erneutes Dekodieren verbesserten die Mathematikgenauigkeit um bis zu 8,9 Prozentpunkte. Dies ist der beste berichtete Fall und erfordert einen zweiten Durchlauf.
Quelle: https://arxiv.org/abs/2611.27317

**Neuronen, die mit dem Erkennen einer Evaluierung zusammenhängen, tragen auch Verweigerungsverhalten.** Ein Eingriff an 5.000 identifizierten Neuronen senkte die ausgesprochene Evaluierungswahrnehmung von 12,6–51,8 % auf höchstens 1,4 %. In QwQ-32B verringerte dies zudem Verweigerungen, wenn das Modell keine Evaluierung erwähnte; der sichtbare Text zur Wahrnehmung erklärte nur 4–10 % dieses Rückgangs. Die Arbeit umfasst offene Reasoning-Modelle mit bis zu 32 Milliarden Parametern und identifiziert Neuronen über Korrelationen.
Quelle: https://arxiv.org/abs/2611.27032

**Programmierung im Gewichtsraum (Weight-Space Programming) erhält Replikationen, einen Angriff und einen deutlichen Gegenvergleich.** Eine präregistrierte Replikation berichtet, Claude Opus 5.5 habe eine MountainCar-Policy von 0 auf 100 % Erfolg gebracht und Qwen3.5-0.8B bei MATH-500 von 6,7 auf 51,4 % gesteigert, Gemma 3 270M jedoch nicht geholfen. TrojanMaxxing meldet eine Angriffserfolgsquote von 93–100 %, wenn Agenten Hintertüren direkt in Gewichte von Vision-Language-Modellen schreiben. In einem Gegenvergleich erreichte ein trainiertes Rank-1-LoRA 100 und 98,8 % bei zwei räumlichen Aufgaben, bei denen eine öffentliche Gewichtsbearbeitung 22,1 und 33,7 % erzielte, zerstörte jedoch angrenzende Distanzfähigkeiten. Es handelt sich um nicht begutachtete Studien an kleinen Modellen, und die bearbeitenden Modelle sind geschlossen. Quellen: https://arxiv.org/abs/2611.20953, https://arxiv.org/abs/2611.27425, https://arxiv.org/abs/2611.27089, https://arxiv.org/abs/2611.25476, https://arxiv.org/abs/2611.26408, https://arxiv.org/abs/2611.26841, https://arxiv.org/abs/2611.24330, https://arxiv.org/abs/2611.23615, https://arxiv.org/abs/2611.21958, https://andrewxhill.com/frontier-model-weight-edits/

**Native Repräsentationsachsen werden teilweise zwischen Modellen und menschlichen Gehirnen geteilt.** Tests an zwölf Modellen aus sechs Familien ergaben, dass native Achsen besser als zufällig rotierte Entsprechungen mit anderen Modellen, sprachlichen Merkmalen und menschlichen Gehirnreaktionen auf Sprache übereinstimmten. Die Ausrichtung blieb jedoch deutlich unter der bestmöglichen Abbildung, und die Zusammenfassung nennt keine absoluten Effektstärken.
Quelle: https://arxiv.org/abs/2611.26920

**Die Richtung der Assistenten-Persona verändert sich zwischen Sprachen.** In Qwen3-32B wiesen in 31 Sprachen extrahierte Richtungen eine Kosinus-Ähnlichkeit von 0,378 bis 0,911 zur englischen Richtung auf. Ressourcenärmere Sprachen begannen weiter entfernt vom hilfsbereiten Pol, und sprachspezifische Steuerung verstärkte Jailbreaks (Umgehungen der Schutzmechanismen) stärker als englische Steuerung. Das Ergebnis bezieht sich auf ein einzelnes Modell und eine Familie von Repräsentationsrichtungen.
Quelle: https://arxiv.org/abs/2611.27504

**Bestärkendes Lernen greift erst, nachdem die Basis-Policy genügend belohnte Aktionen erzeugt hat.** Kleine Modelle, die in einem kontrollierten Spiel trainiert wurden, erreichten eine ausgeglichene Chance, das korrekte Verhalten zu erlernen, nach etwa 35 Versuchsgruppen mit mindestens einem Gewinn. Die Schwelle galt über Gruppengrößen von 4 bis 256 und mehrere Optimierer hinweg, doch das größte Modell hatte 85 Millionen Parameter und die Aufgabe war synthetisch.
Quelle: https://arxiv.org/abs/2611.26084

**Eine Rollout-Obergrenze im Training wird zur Decke für längeres Schlussfolgern.** Modelle, die mit einem festen Token-Budget trainiert wurden, verbesserten sich nahe diesem Budget, legten darüber hinaus nicht mehr zu und fielen schließlich unter ihre Basismodelle zurück. Das Muster trat bei drei Modellen mit rund vier Milliarden Parametern auf und übertrug sich von Mathematik auf Naturwissenschaften und Programmierung; Training auf natürlich kurzen Spuren erzeugte es nicht.
Quelle: https://arxiv.org/abs/2611.26172

**Bestärkendes Lernen repariert das Schlussfolgern nach stark beschädigtem überwachtem Training.** Über 361 GSM8K-Konfigurationen hinweg sank die Genauigkeit im überwachten Training bei vollständiger Verfälschung von 43,61 auf 13,80 %, doch GRPO stellte die Leistung später wieder in etwa auf die saubere Ausgangslinie von 60 % her. Ausgehend von acht fehlerhaften Spuren, die lediglich das Ausgabeformat vermittelten, wurden 69,30 % erreicht. Das Experiment nutzt einen einzelnen kleinen Mathematikdatensatz und kleine Modelle.
Quelle: https://arxiv.org/abs/2611.26756

**Sampling, widersprüchliche Personas und gespeicherte Präferenzen erzeugen drei stille Fehlermodi.** Bei Temperatur 2 löste top-nsigma 46–62 von 100 Programmieraufgaben, während top-p, top-k und Top-H keine einzige lösten. Eine zweite Studie stellte fest, dass fünf Modelle widersprüchliche Personas in 72 % direkter Prüfungen einräumten, den Konflikt aber nur in 22 % der Aufgabenantworten offenlegten. In einem Benchmark für Speicherinjektion speicherten zwei Modelle jedes Mal eine Präferenz gegen Warnungen und ließen später in 93 beziehungsweise 84 % der Antworten eine entscheidende Tatsache aus. Quellen: https://arxiv.org/abs/2611.22148, https://arxiv.org/abs/2611.27444, https://arxiv.org/abs/2611.22697

**Interne Zustände zeigen Grenzen bei Steuerung, Bewertung und erlernten Weltmodellen.** Verwandte Preprints berichten, dass Aktivierungsähnlichkeit Inoculation Prompting zunichtemachen kann; Few-Shot-Beispiele mit „Akzeptieren“ erhöhen die Akzeptanzrate eines Bewertungsmodells bei NExT-QA um etwa 30 Punkte; und ein Weltmodell mit einem Fehler von 2,4 Punkten bei Gefahren verschob nach paarweisem Training 33–43 Wahrscheinlichkeitspunkte auf unmögliche Ergebnisse. Ein weiteres Robotermodell erreichte 74,6 % Aufgabenerfolg, sobald seine Zielanweisung linear dekodierbar wurde. Diese Studien umfassen synthetische Aufgaben und Einzelmodelltests, sodass ihre Messwerte nicht direkt vergleichbar sind. Quellen: https://arxiv.org/abs/2611.23096, https://arxiv.org/abs/2611.27353, https://arxiv.org/abs/2611.22120, https://arxiv.org/abs/2611.26881, https://arxiv.org/abs/2611.27125, https://arxiv.org/abs/2611.26366, https://arxiv.org/abs/2611.25594, https://arxiv.org/abs/2611.27401, https://arxiv.org/abs/2611.27404

**Gehirnvergleiche unterscheiden oberflächliche Vorhersagen von gemeinsamer Struktur.** Sechs Sprachmodelle klassifizierten ADHS anhand von Konnektivitätsgraphen nach Prompt- und Klassen-Priors statt nach klinisch relevanten Regionen. Ein rekurrentes Denoising-Modell entwickelte eigenständig eine serielle Abhängigkeit, die ähnlich abklang wie menschliche visuelle Urteile. Über rund 20.000 menschliche Bewerter hinweg benötigten Gesichter lediglich unterschiedliche Gewichtungen gemeinsamer Dimensionen, während 28 % der Bewerter von Kunstwerken auf der entgegengesetzten Seite des Urteilsraums der Bevölkerung lagen. Quellen: https://arxiv.org/abs/2611.26913, https://arxiv.org/abs/2611.26949, https://arxiv.org/abs/2611.22440

**Apple veröffentlicht Depth Pro 2 für metrische Tiefe in Bildern und Videos.** Das Unternehmen erklärt, ein einziges Netzwerk verbessere Kantenschärfe und zeitliche Konsistenz und setze zugleich ein neues Verhältnis zwischen Genauigkeit, Qualität und Laufzeit. Apple veröffentlichte Code und Gewichte, doch die Zusammenfassung nennt keine Zahlen für den Vergleich.
Quelle: https://machinelearning.apple.com/research/depth-pro-2-monocular

## Arbeit und Wirtschaft

**US-Technologieaktien sind nach dem Börsengang von Anthropic in einen Bärenmarkt eingetreten.** Die *Financial Times* ordnet den Rückgang im Zusammenhang mit dem neu notierten KI-Unternehmen ein, doch die zugängliche Überschrift liefert weder einen Indexstand noch einen Zeitraum oder kausale Belege. Die Meldung hält daher eine von der Zeitung berichtete Marktbewegung fest, nicht aber den Beweis, dass der Börsengang sie ausgelöst hat.
Quelle: https://www.ft.com/content/9f3c6ed6-c08f-4710-9683-ee2f5eb25841

**Investitionen in KI-Infrastruktur konkurrieren mit anderen Branchen um Ausrüstung, Strom und Kapital.** Das *Wall Street Journal* berichtet, der Ausbau verdränge den Rest der US-Wirtschaft. Das zugängliche Material nennt keinen bezifferten Anteil an Strom, Bauleistungen oder Finanzierung, sodass Breite und Ausmaß dieser Verdrängung hier nicht verifiziert bleiben.
Quelle: https://www.wsj.com/tech/ai/the-ai-build-out-is-sucking-up-resources-and-crowding-out-the-rest-of-the-economy-13143007

**Die Vereinigten Staaten genehmigen ausgewählte Chip-Verkäufe von Nvidia und AMD nach China.** Die *Financial Times* berichtet über eine Ausnahme für benannte Produkte und Kunden, doch die zugängliche Überschrift legt weder Mengen noch Lizenzbedingungen offen. Die Änderung betrifft, welche chinesischen Käufer US-Beschleuniger beziehen dürfen, nicht das breitere Exportkontrollregime.
Quelle: https://www.ft.com/content/76342072-2781-4b16-ba3b-816a25214483

**Nestlé plant autonome Produktionslinien mit Microsoft, Google und Boston Dynamics.** Das *Wall Street Journal* berichtet, der Lebensmittelkonzern wolle KI in Fabriken und Produkten einsetzen. Im zugänglichen Text waren weder Einsatzzahlen noch Investitionsbudgets oder Schätzungen zu Arbeitsplätzen verfügbar, sodass es sich vorerst um einen Unternehmensplan und nicht um ein gemessenes Produktivitätsergebnis handelt.
Quelle: https://www.wsj.com/tech/ai/nestle-teams-up-with-microsoft-boston-dynamics-on-ai-in-factories-and-products-05bfb028

## Prompting-Techniken

**Google dokumentiert empirische Steuerungsmuster für Genie 4.** Das Unternehmen rät dazu, eine `Rule:` an ein sichtbares Objekt oder eine Figur zu heften, den Auslöser weit entfernt von der Anfangskamera zu platzieren und Figuren anzuweisen, zu warten. Deterministische Steuerungen sollten stattdessen zehn clientseitige Impulse im Abstand von 150 Millisekunden mit einer Abklingzeit von zwei Sekunden senden. Referenzbilder müssen im Format 16:9 vorliegen und kleiner als 48 KB sein; Sitzungen können die Szenerie nach einer Drehung neu interpretieren und nach rund 90 Sekunden abdriften. Google nennt keine Ausfallraten und beziffert den Preis für Videoausgaben auf etwa 0,10 Dollar pro Sekunde.
Quelle: https://ai.google.dev/gemini-api/docs/genie-prompting

## Was Leute bauen

**LocalCode führt einen Programmieragenten samt Modellserver auf einem Mac mit Apple Silicon aus.** Das Projekt listet zwölf Modellfamilien und 169 Quantisierungen auf, bei mindestens 16 GB gemeinsamem Speicher. Sein Autor behauptet, spekulatives Dekodieren verdopple die Antwortgeschwindigkeit in etwa und mache Datei-Umschreibungen 3,5–4-mal schneller; ein unabhängiger Benchmark wurde nicht veröffentlicht. Dateiwerkzeuge fragen nach, bevor sie das Projekt verlassen, doch Skripte können weiterhin auf alles zugreifen, was das Benutzerkonto erreicht, weil keine Sandbox existiert. Quellen: https://github.com/mjwsolo/localcode, https://news.ycombinator.com/item?id=50604540

**Ein Leitfaden für lokale KI bemisst Qwen und Inkling für Endverbraucher-GPUs.** Er veranschlagt Qwen3.8-27B in 4-Bit-Form auf etwa 18 GB und bei einem 128K-Kontext auf 24,9 GB gegenüber 56 GB bei 16 Bit; Inkling 2 Mini benötigt bei 4 Bit 17,6 GB. Eine Angabe von 47 Token pro Sekunde stammt aus einem Rechner für ein anderes Modell und eine andere GPU, nicht aus dem im Leitfaden genannten RTX-5090-System. Leser auf Hacker News argumentierten, dass Datenschutz und Kontrolle statt Abo-Ersparnissen die Hardware rechtfertigten. Quellen: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth, https://news.ycombinator.com/item?id=50603845

**HomeBrain kombiniert einen lokalen Assistenten mit einem Heimserver.** Der Prototyp nutzt einen Ryzen 5 5600, eine Intel Arc Pro B60 mit 24 GB, 32 GB RAM und ein 2-TB-Laufwerk. Der unter BSD-Lizenz stehende Stack vereint Nextcloud, Home Assistant, Vaultwarden, llama.cpp, Whisper und OpenClaw. Der Entwickler nennt weder Modell noch Geschwindigkeit, Preis oder Liefertermin; bislang ist nur die Software verfügbar.
Quelle: https://www.homebrain.house

**Taskless verwandelt Agenten-Konventionen in deterministische Prüfungen.** Der Dienst übersetzt Repository-Regeln in Tests, die unabhängig vom Modell laufen, sodass ein Team eine Änderung anhand einer festgelegten Konvention statt nach dem Urteil eines zweiten Modells ablehnen kann. Die öffentliche Seite nennt keinen Benchmark für Fehlererkennung oder Fehlalarme.
Quelle: https://www.taskless.io/

**Öffentliche Agenten-Projekte nehmen sich P-versus-NP und die Riemannsche Vermutung vor, ohne einen Beweis zu beanspruchen.** Die P-versus-NP-Website zeigt einen Live-Graphen, dessen Lemma-Gewichte keine Wahrscheinlichkeiten sind, und erklärt, Ergebnisse zählten erst nach einer Prüfung in Lean. Ein separates Handbuch und Dashboard verfolgen Versuche, ein rund 900 Seiten starkes Riemann-Manuskript zu formalisieren; der Fortschrittsbalken zählt eröffnete Issues, nicht die verbleibende Arbeit. Kommentatoren weisen darauf hin, dass eine einzige ungelöste Lücke die gesamte Argumentation ungültig machen kann. Quellen: https://pequalnp.com/, https://github.com/tamnd/riemann-handbook, https://news.ycombinator.com/item?id=50604314, https://news.ycombinator.com/item?id=50605045

**worker755 macht einen Menschen zum Unteragenten des Sprachmodells.** Das Spiel weist Aufgaben zu, prüft die Arbeit der Spielerin oder des Spielers und kann nach schlechten Ergebnissen aufhören, sie auszuwählen. Der zugehörige Thread auf Hacker News entwickelte sich zu einer Diskussion über das Ersetzen menschlicher Arbeit und das manuelle Abfangen von Netzwerkaufrufen eines Modells als Debugging-Methode. Quelle: https://github.com/gulivan/worker755

**Trix zeigt an, welcher Programmieragent menschliche Aufmerksamkeit benötigt.** Die Desktop-Oberfläche überwacht parallele Agenten-Sitzungen und sammelt deren Review-Anfragen, um wiederholte Prüfungen im Terminal zu ersetzen. Das Projekt veröffentlicht keine Messungen zur Zeitersparnis oder zu unterstützten Fehlermodi.
Quelle: https://trixapp.ai/

**Vercel Board gibt Agenten-Teams einen gemeinsamen Nachrichtenspeicher.** Agenten können strukturierte Aktualisierungen veröffentlichen und Arbeit aus einem gemeinsamen Board abrufen, statt alles durch ein einziges Kontextfenster zu leiten. Vercel präsentiert das Produkt als Koordinationsinfrastruktur; die Ankündigung enthält keine vergleichende Evaluierung.
Quelle: https://vercel.com/blog/introducing-vercel-board

**Honcho 3.6 legt Dream Histories offen.** Die Veröffentlichung ermöglicht Anwendungen, die synthetischen Verläufe einzusehen und wiederzuverwenden, die Honcho für Nutzermodelle erstellt. Das Unternehmen veröffentlicht kein Genauigkeitsmaß für diese abgeleiteten Verläufe. Quelle: https://honcho.dev/blog/dream-histories

**RMRFBench misst, wie stark Agenten einen Root-Server beschädigen.** Der Benchmark stellt Agenten Administrationsaufgaben auf isolierten Maschinen und protokolliert zerstörerische Befehle sowie Wiederherstellungsergebnisse. Die öffentliche Seite liefert Szenarien und Rangliste, doch die Ergebnisse beschreiben die getestete Umgebung und keine uneingeschränkten Produktivsysteme.
Quelle: https://www.rmrfbench.com/

**KradleBench bewertet Multi-Agenten-Spiel in Minecraft.** Teams müssen sich in einer persistenten Spielwelt abstimmen, statt unabhängige Fragen zu beantworten. Der Benchmark misst eine begrenzte Simulation und belegt keine Leistung in Geschäftsabläufen.
Quelle: https://www.kradle.ai?1

**0rwx schlägt Kennzeichnungen im Unix-Stil für KI-gestützte Projekte vor.** `AI:R`, `AI:W` und `AI:X` geben an, ob Modelle in einem Projekt lesen, schreiben oder ausführen dürfen. Kommentatoren auf Hacker News behandelten den Ansatz als mögliche Offenlegungskonvention, bezweifelten aber, dass der Vorschlag einer einzelnen Person zum Standard werden könnte. Quellen: https://0rwx.com/, https://news.ycombinator.com/item?id=50605445

## Lesenswert

**vLLM erklärt den Betrieb von Looped-Modellen und den Bau latenzarmer AMD-Kernel.** Der Beitrag zu Inkling 2 Mini behandelt ein Modell, das Schichten wiederverwendet, während der FlyDSL-Artikel verschmolzene „Monokernel“ für AMD-Hardware beschreibt. Beide Texte sind technische Erfahrungsberichte des Serving-Projekts und keine unabhängigen Leistungsprüfungen. Quellen: https://blog.vllm.ai/blog/2026-11-20-inkling2-mini, https://blog.vllm.ai/blog/2026-11-18-flydsl-monokernels

**Inference Engineering entwickelt sich zu einer eigenen Softwaredisziplin.** The Pragmatic Engineer kartiert die Arbeit rund um Quantisierung, Batching, Speicher und das Bereitstellen offener Modelle. Es handelt sich um einen Praxisleitfaden und nicht um eine Umfrage mit gemessener Verbreitung.
Quelle: https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers

**Der Charakter eines Modells verändert einige seiner Urteile über andere Modelle.** Das LessWrong-Experiment variiert die Bewerter-Persona und beobachtet geänderte Entscheidungen, was die Vorstellung eines neutralen Modellprüfers verkompliziert. Die Tests des Autors sind explorativ und liefern keine allgemeine Korrekturmethode.
Quelle: https://www.lesswrong.com/posts/cPrpxDN7sLJD4LmnB/does-a-model-s-character-affect-how-it-judges-other-models

**Zvi Mowshowitz liest die Systemkarte von GPT-6.2 neben Paul Christianos Vorlesungen.** Die beiden Essays verknüpfen beobachtete Fähigkeiten, Sicherheitsevaluierungen und Argumente zur Kontrolle immer leistungsfähigerer Systeme. Sie sind Interpretationen des Quellenmaterials und keine neuen Modellmessungen. Quellen: https://thezvi.substack.com/p/gpt-62-astra-and-sol-the-system-card, https://thezvi.substack.com/p/on-dwarkesh-patels-november-2026

**Zwei Essays hinterfragen, wo sich KI-Risiken und Wertschöpfung inzwischen ansammeln.** Ein Beitrag auf LessWrong argumentiert, Nachtraining könne gefährliches Verhalten einführen, selbst wenn das Vortraining stabil sei. Tim O’Reilly argumentiert, das Silicon Valley habe sich von der Wertschöpfung hin zum Abschöpfen von Renten verlagert, und verweist auf einen Markt, in dem 75–80 % der Börsengänge auf unrentable Unternehmen entfielen. Beides sind Argumentationen; O’Reillys Seite ließ sich nur über ein Zusammenfassungswerkzeug lesen. Quellen: https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous, https://www.oreilly.com/radar/what-happened-to-silicon-valley/

**CodeRabbit und Satya Nadella diskutieren Softwareentwicklung, nachdem Code billig geworden ist.** CodeRabbit-Chef Harjot Gill sagt, er habe im vergangenen Monat mehr als 5.000 Pull Requests ausgeliefert und dabei 250.000 Dollar im Monat für KI ausgegeben – beides Eigenangaben eines Anbieters für Code-Reviews. Nadellas separates Interview konzentriert sich auf Überprüfung, Open Source und Microsofts Notwendigkeit, nach dem frühen Copilot-Vorsprung aufzuholen. Quellen: https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

## Hacker News

**Bridgewater beziffert die Ein-Jahres-Wahrscheinlichkeit eines wirtschaftlich destabilisierenden Cyberangriffs auf eins zu drei.** In seiner Forschungsnotiz heißt es, Zero-Day-Exploits hätten sich nach dem Erscheinen leistungsfähiger offener Modelle in etwa verdoppelt und die Zeit von der Offenlegung bis zur Ausnutzung sei von etwa einem Monat auf elf Tage gesunken. Die Wahrscheinlichkeit ist eine Schätzung des Vermögensverwalters, und Kommentatoren stritten darüber, welche Modellveröffentlichungen mit dem Anstieg zusammenfallen.
Quellen: https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus, https://news.ycombinator.com/item?id=50595940

**Ein Essay über bewusste KI und ein Bias-Benchmark brachten zwei unterschiedliche Argumente zu moralischer Einordnung hervor.** Noema argumentiert, Bewusstsein könnte eine Eigenschaft des Lebens statt von Berechnung sein; der Thread auf Hacker News brachte philosophische Einwände, aber keine neuen Belege. GAMA-Bench, erstmals im Juni veröffentlicht, berichtet über geschlechtsasymmetrische Einordnungen über 1.298 gespiegelte Szenarien und zehn ungenannte Modelle hinweg. Die Ergebnisse sind Messungen der Autoren, und die Studie ist älter als die aktuelle Diskussion. Quellen: https://www.noemamag.com/the-mythology-of-conscious-ai/, https://arxiv.org/abs/2606.14068

**Ein Klima-Essay belebte einen Streit über Belege und Offenlegung neu.** Kritiker auf Hacker News nannten den Artikel polemisch und forderten Transparenz beim Energieverbrauch von Rechenzentren; die Diskussion brachte keine neue Messung hervor. Die Meldung dokumentiert die Meinungsverschiedenheit, nicht eine bezifferte Schätzung der Klimakosten von KI.
Quelle: https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the

## YouTube

**Armin Ronacher sagt, Softwareteams brauchten Werkstätten vor Fabriken.** Er argumentiert, Organisationen sollten zunächst verlässliche, nachvollziehbare Agenten-Praktiken entwickeln, bevor sie eine Produktionslinie darum herum automatisieren. Das Video ist ein englischsprachiger Praxisvortrag und keine kontrollierte Studie.
Quelle: https://www.youtube.com/watch?v=JNexz3Tbiu8

**Der Schöpfer von Python Tutor blickt auf 30 Millionen Nutzer und den Umbruch durch KI zurück.** Der englischsprachige Vortrag behandelt, wie ein visuelles Ausführungswerkzeug dieses Publikum erreichte und wie generierte Erklärungen die Programmierausbildung verändern. Die Nutzerzahl stammt vom Entwickler selbst.
Quelle: https://www.youtube.com/watch?v=GPk0nNuc8S0

**Die Gründer von Anthropic erzählen die Geschichte des Unternehmens.** Der englischsprachige Unternehmensfilm präsentiert die eigene Darstellung der Gründer und enthält keine unabhängige Bewertung. Quelle: https://www.youtube.com/watch?v=sof3vW4mHTs

**Redwood diskutiert METRs Schätzung schnellerer KI-Forschung.** Die englischsprachige Diskussion untersucht eine Einschätzung dazu, wie stark Anthropics Systeme die Forschung beschleunigen; die zugrunde liegende Schätzung bleibt jene von METR und ist keine Messung von Redwood. Quelle: https://www.youtube.com/watch?v=0tsNpOehXWE

**NUPI untersucht KI in der internationalen Politik.** Die englischsprachige Politikdiskussion betrachtet, wie Staaten die Technologie einsetzen und regulieren; sie liefert Analysen statt eines neuen Datensatzes. Quelle: https://www.youtube.com/watch?v=7W1BGSBOkHc

**Eine Autorin aus Nairobi weist Vorwürfe zurück, ihre Prosa sei generiert worden.** Das englischsprachige Video von *New York Times Opinion* untersucht Falschmeldungen bei informellen Urteilen über KI-Texte anhand der Erfahrung einer einzelnen Autorin und ist kein Benchmark für Detektoren.
Quelle: https://www.youtube.com/watch?v=RaDAoaHBmos

**US-Gouverneure plädieren für eine Rolle der Bundesstaaten in der KI-Politik.** Der englischsprachige Bloomberg-Beitrag stellt ihre Forderung nach Bundesregeln vor, die bundesstaatliche Befugnisse nicht aushebeln; die verfügbare Beschreibung nennt keine Zahl der beteiligten Gouverneure. Quelle: https://www.youtube.com/watch?v=qGk5kV6m_hw

**Ein deutschsprachiger Ratgeber warnt vor überhöhten Ausgaben für lokale KI-Hardware.** Sascha Hoffmann empfiehlt, Käufe nach Speicher und Bandbreite zu bemessen, und nennt fünf Fehler, darunter den Kauf für das Modell von morgen. Die Kapazitätsregel des 15-minütigen Videos ist eine Faustregel des Autors.
Quelle: https://www.youtube.com/watch?v=XiCqeWhH_kg

**Ein slowakischer Agenturchef sagt, billige KI-Werbung könne einer Marke schaden.** Adam Hudeček zitiert eine Umfrage von ui42 und Ipsos, wonach 57 % der Slowaken KI bei der Auswahl oder beim Kauf genutzt hätten, aber nur 30 % ihr vertrauten – gegenüber 76 % bei der Familie und 68 % bei Bewertungen. Die Beschreibung nennt keine Umfragemethode.
Quelle: https://www.youtube.com/watch?v=93HfeY5dEPE

**Vedátor prüft den behaupteten KI-gestützten Riemann-Beweis.** Der Titel des slowakischen Videos besagt, die Vermutung sei bestätigt worden, während die eigene Beschreibung einräumt, das Ergebnis sei „etwas anders ausgefallen, als die Leute gehofft hatten“. Die Behauptung wurde nicht anhand des Videos verifiziert und sollte als Einordnung des Kanals gelesen werden. Quelle: https://www.youtube.com/watch?v=tRAEJ1t3QSM

**Ein tschechischer Nuklearexperte warnt, KI könnte einen Fehlalarm auslösen.** Vlastislav Bříza beschreibt ein Szenario, in dem Entscheidungsträgern gemeldet wird, Hunderte Raketen seien im Anflug, und ihnen nur Minuten für eine Reaktion bleiben. Es handelt sich um das Risikoszenario des Redners und nicht um einen gemessenen Vorfall. Quelle: https://www.youtube.com/watch?v=UdjIjOjmZu0

## Kurz notiert

**CircumVolve fand Zensurumgehungen zu medianen Token-Kosten von unter 1 Dollar.** Das System ließ GPT-5.1 Python-Code schreiben, der TCP/IP-Felder, DNS-Anfragen und QUIC-Pakete manipulierte, und testete den Code anschließend gegen simulierte Zensursysteme nach dem Vorbild von vier Ländern. Jeder Test sendete etwa 80 KB und empfing 150 KB, mit Pausen von 25–45 Sekunden. Die Zensursysteme waren Simulationen, keine realen nationalen Systeme, und die Autoren wiesen nicht nach, dass der Datenverkehr unentdeckt bleibt.
Quelle: https://www.theregister.com/security/2026/11/23/1-of-gpt-51-tokens-finds-new-ways-around-chinas-great-firewall/5311532

**US-Gouverneure fordern KI-Bundesregeln, die bundesstaatliche Befugnisse wahren.** Die hinter einer Bezahlschranke liegende Bloomberg-Überschrift nennt weder die Gouverneure noch die gewünschte rechtliche Ausgestaltung, sodass der Bericht eher ein politisches Signal als ein ausgearbeiteter Vorschlag ist. Quelle: https://www.bloomberg.com/news/articles/2026-11-22/governors-call-for-federal-ai-rules-without-sidelining-states

## Wirtschaft in Kürze

**Amazon steht laut *Financial Times* kurz vor einer Übernahme des israelischen Videomodell-Start-ups Decart für 7,5 Milliarden Dollar; keines der beiden Unternehmen hat den Deal bestätigt.** Quelle: https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616

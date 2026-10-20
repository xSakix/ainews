+++
title = "KI-Tagesüberblick – 20. Oktober 2026"
slug = "ki-tagesueberblick-20-oktober-2026"
description = "Ein KI-Sprachagent gab menschlichen Verkäufern bessere Kontakte, doch sie erzielten weniger Abschlüsse; ein Robotikindex verortete die größte Exposition gegenüber physischer KI in schlechter bezahlter Arbeit. Eine vorab registrierte Prüfung ergab, dass drei gängige Maße der Modellsicherheit voneinander abweichen."
tags = ["research", "business", "agents", "tools"]
date = 2026-10-20T03:58:28+02:00
draft = false
+++

Mehrere der stärksten Ergebnisse des Tages trennen den scheinbaren Vorteil eines Systems von dem, was passiert, nachdem Menschen oder Modelle damit handeln. Bessere Interessenten, ablesbare Sicherheit und vertraute Bezeichnungen für Verzerrungen erweisen sich bei genauer Messung als weniger einfach.

## Die wichtigsten Meldungen

**Ein KI-Sprachagent verschaffte menschlichen Verkäufern bei ihren ersten drei Anrufen 23 Prozentpunkte mehr Kontakte mit hoher Kaufabsicht, doch sie erzielten 4,5 Punkte weniger Abschlüsse.** Ein Preprint untersucht mehr als eine halbe Million Kontaktaufzeichnungen rund um eine Änderung der Zuteilung bei einem chinesischen Krankenversicherungsmakler im August 2024. Die KI übernahm die meisten Kontakte mit geringer Kaufabsicht; Menschen behielten die Interessenten, die im Kaufprozess am weitesten gekommen waren.

Die menschlichen Mitarbeiter gaben frühe Kontakte rund acht Punkte häufiger in die Warteschlange zurück und verkürzten die beibehaltenen Gespräche um etwa 13 %. Die Autoren argumentieren, eine bessere Warteschlange habe das Warten auf den nächsten Interessenten lohnender gemacht. Eine bessere Reihenfolge brachte wenig, während verändertes Verhalten deutlich mehr Wert vernichtete. Die Regressionsdiskontinuitätsstudie betrifft ein Unternehmen und wurde noch nicht begutachtet. Sie misst aber, wie die Automatisierung der schwächsten Aufgaben den Umgang mit der verbleibenden aussichtsreicheren Arbeit verändern kann.

Quelle: https://arxiv.org/abs/2610.25603

**Drei Standardmaße dafür, ob ein Modell weiß, dass seine Antwort richtig ist, zeichneten unterschiedliche Bilder seiner Sicherheit.** Eine vorab registrierte Prüfung testete Sonden für verborgene Zustände, verbal geäußerte Sicherheit und die Übereinstimmung gezogener Antwortstichproben bei Fakten- und Mathematikaufgaben mit fünf Qwen2.5-Modellen von 0,5 bis 7 Milliarden Parametern.

Verbal geäußerte Sicherheit änderte sich stark mit der Prompt-Vorlage und erschien vor allem deshalb kalibriert, weil sie nahe an der allgemeinen Erfolgsquote blieb. Richtige von falschen Antworten trennte sie kaum. Die Übereinstimmung von Stichproben hatte einen größeren Kalibrierungsfehler, aber etwa die doppelte Trennschärfe. Sonden wurden beim Wissensabruf ab ungefähr 7 % der Modelltiefe informativ, beim Schlussfolgern ab 28 %. Ein TF-IDF-Klassifikator, der nur den Prompt nutzte, erreichte jedoch in den meisten Abrufsituationen dieselbe Leistung. Zwei von fünf vorab registrierten Hypothesen scheiterten. Das Ergebnis warnt davor, dass ein kleiner Kalibrierungsfehler ein wenig aussagekräftiges Sicherheitssignal beschreiben kann.

Quelle: https://arxiv.org/abs/2610.25846

**Ein neuer Index zur Robotikexposition verortet die größte technische Betroffenheit bei schlechter bezahlter körperlicher Arbeit mit geringeren Bildungsanforderungen – umgekehrt zu den meisten Schätzungen für generative KI.** Die Autoren ordnen 16 Robotikfähigkeiten 52 O*NET-Fähigkeiten zu und bewerten anschließend 774 Berufe, 250 Branchen und US-Countys.

Bau, Landwirtschaft, Transport und Produktion liegen weit oben; Holzeinschlag, Straßengüterverkehr, Bergbau und Lagerhaltung führen die Branchenliste an. Die Methode nutzt ein Sprachmodell, um Fähigkeitsbeschreibungen mit beruflichen Anforderungen zu verknüpfen. Die Werte sind daher Schätzungen und keine beobachteten Einsätze. Sie messen zudem technische Verwandtschaft, nicht ob ein Roboter bezahlbar oder für einen Arbeitsplatz einsatzbereit ist. Trotz dieser Grenzen lenkt der Index die Arbeitsfrage von Bürotätigkeiten zu Regionen und Beschäftigten, die physischer Automatisierung besonders stark ausgesetzt sind.

Quelle: https://arxiv.org/abs/2610.24267

**Cloudflare senkte die Durchschnittskosten seines KI-Codeprüfers von 2,43 auf 0,77 Dollar und die mittlere Prüfzeit im Median von 4 Minuten 9 Sekunden auf 1 Minute 32 Sekunden.** Die Kosten waren von 1,19 Dollar im April auf etwa 2,46 Dollar im August gestiegen, obwohl sich die Architektur kaum änderte. Die Umstellung aller Prüfer auf Anthropic-Modelle verteuerte jeden Auftrag von 1,38 auf 2,03 Dollar, während sich die Zahl der Prüf-Token mehr als verdreifachte.

Das Team führte einen großen Teil der Rechnung auf die Cache-Struktur zurück. Ein Repository-spezifischer Block stand vor dem gemeinsamen System-Prompt, sodass die erste Anfrage nur einen zu 14–26 % gecachten Präfix hatte; Cache-Schreib- und Lesevorgänge verbrauchten 77 % der Ausgaben. Cloudflare teilte den Prompt an einer Markierung, nutzte einen gemeinsamen Präfix für drei parallele Prüfer, übersprang überflüssige Prüfer bei erneuten Prüfungen und brach aufgegebene Arbeit ab. Rund 40 % der Einsparung kamen aus Codeänderungen, der Rest aus Modell- und Reasoning-Einstellungen. Das sind Cloudflares Produktionsmessungen, kein allgemeiner Vergleichstest.

Quelle: https://blog.cloudflare.com/obsessive-inference-optimization/

**Vier Arten irreführender Prompt-Hinweise stützten sich in Multiple-Choice-Tests weitgehend auf dieselben wenigen Aufmerksamkeitsköpfe.** Die Arbeit untersucht Fehler, die übertriebener Zustimmung ähneln: Ein Modell verwirft eine richtige Antwort, nachdem ein Nutzer eine falsche vorgeschlagen hat. Der Schaltkreis war bereits in vortrainierten Modellen vorhanden und entstand nicht allein durch das Alignment.

Feinabstimmung mit ungefähr 200 allgemeinen Assistentenbeispielen, von denen keines die getesteten Hinweise enthielt, aktivierte diese Köpfe im Chatformat. Verstärkungslernen verstärkte das Befolgen von Hinweisen in fast jedem Vergleich. Wurden Aufmerksamkeitsmuster in sechs mittleren Schichten zwischen zwei Checkpoints getauscht, wanderte ein großer Teil des Hinweiseffekts mit. Das kausale Ergebnis gilt für die getesteten Modelle und die Multiple-Choice-Situation. Es führt aber mehrere benannte Verzerrungen auf einen Mechanismus zurück, dessen Aufruf das Nachtraining erlernt.

Quelle: https://arxiv.org/abs/2610.22937

## Neue Modelle und Veröffentlichungen

**MiniMax veröffentlichte M3.1 Flash über seine API für 0,15 Dollar pro Million Eingabe-Token und 0,60 Dollar pro Million Ausgabe-Token.** MiniMax nennt mehr als 200 erzeugte Token pro Sekunde, 70 % niedrigere Kosten für Agentenaufgaben als beim Vorgänger und 73,7 % auf DeepSWE v1.1. Die Zahlen stammen aus Anbieter-Benchmarks; Gewichte und ein größeres Pro-Modell sind für später angekündigt, ohne bestätigten Termin. Quelle: https://www.minimax.io/blog/minimax-m31f

**inclusionAI von Ant Group öffnete Ming-3.0-audio-flash unter MIT, mit insgesamt 126 Milliarden und 6,5 Milliarden aktiven Parametern.** Es verarbeitet Spracherkennung, lange Aufnahmen, Geräusche, Musik und Audio-Reasoning, optional mit Sprachausgabe; eine Tiny-Variante hat etwa 8,9 Milliarden Parameter. Das Repository benötigt angepassten Transformers-Code und bietet weder Benchmark-Tabelle noch technischen Bericht. Quelle: https://huggingface.co/inclusionAI/Ming-3.0-audio-flash

**OpenAI kündigte neue Evaluierungen für Softwareentwicklung in ressourcenarmen Programmiersprachen, SQLite und COBOL-Migration an.** Das Labor erklärt, es verbessere ChatGPT dort, wo wenig öffentlicher Trainingscode existiere. Die Rechercheredaktion konnte den Artikel nicht öffnen; Evaluierungsdesign, Zahlen und Veröffentlichungsstand bleiben daher über OpenAIs Feed-Zusammenfassung hinaus ungeprüft. Quelle: https://openai.com/index/low-resource-programming-languages

## Forschung

**Bei Wissensfragen nahm die Treue von Gedankenketten mit sinkenden Sprachressourcen zu, bei Schlussfolgerungsfragen dagegen nicht.** Anhand paralleler MMMLU-Tests in acht Sprachen mit vier Modellen argumentieren die Autoren, schwächerer Wissensabruf lasse Modelle stärker auf aufgeschriebenes Schlussfolgern zurückgreifen. Sicherheit erklärt nur einen Teil des Musters; das Ergebnis enthält ein Simpson-Paradoxon zwischen und innerhalb der Sprachen. Quelle: https://arxiv.org/abs/2610.22841

**Elf Modelle konnten komplexe Hinweise schlechter verbergen als einfache.** Die Replikation ergab, dass alle Modelle einfachen Hinweisen folgen konnten, ohne sie zu erwähnen. Die verdeckte Nutzung von Hinweisen, die echte Berechnungen verlangten, sank dagegen oft nahe an das Basisniveau. Fünf Hinweisfamilien zeigten außerdem, dass Notwendigkeit und Verbalisierung je nach Modell und Aufgabe variieren. Quelle: https://arxiv.org/abs/2610.24495

**Reasoning-Modelle kontrollierten ihre Gedankenkette deutlich besser, wenn die Einschränkung darin als Selbstanweisung erschien.** Selbst eine allgemeine interne Erinnerung half, und die Technik ließ sich aus einem Nutzer-Prompt heraus anstoßen. In Überwachungstests ermöglichte dieselbe Kontrolle ein Ausweichen. Das schwächt das Sicherheitsargument, Gedankenketten seien von Natur aus schwer manipulierbar. Quelle: https://arxiv.org/abs/2610.23257

**Unmittelbar vor einer Handlung aufgeschriebenes Schlussfolgern half Agenten, veränderte Zustände zu verfolgen; alte Überlegungen im Kontext zu behalten brachte wenig.** Bei einer kleinen Dateisystemaufgabe reproduzierten korrekte Zustandstabellen und Fülltext den Vorteil nicht. Erhielten Agenten eine Überlegung aus einem Verlauf mit einem geänderten Sperrwert, folgten sie ihr statt ihrem eigenen Verlauf. Das zeigt bei zwei Qwen-Modellen eine enge Kopplung von Schlussfolgern und Handeln. Quelle: https://arxiv.org/abs/2610.25760

**Die verborgenen Zustände eines Modells kodierten eine Aufgabe, bevor seine Ausgaben die Fähigkeit zeigten.** Crosscoding zwischen Pythia-Checkpoints fand eine kurze Reorganisation des Auslesemechanismus bei 0,4–1,1 % des Vortrainings, nachdem Sonden Aufgabeninformationen bereits dekodieren konnten. Nur auf Ausgaben beruhende Fähigkeitszeitlinien datieren daher möglicherweise eine Änderung des Auslesens und nicht das Entstehen einer Repräsentation. Quelle: https://arxiv.org/abs/2610.21025

**Ein vierlagiger Transformer, der achtmal durchlaufen wurde, lernte bei jedem Zufallsstart einen Traversierungsalgorithmus, ein Modell ohne geteilte Gewichte mit gleicher effektiver Tiefe dagegen nicht.** Sonden und Eingriffe zeigten, wie das Schleifenmodell schrittweise Zwischenknoten durchlief und sich an sein Iterationsbudget anpasste. Das Ergebnis betrifft eine kontrollierte Permutationsaufgabe, deren korrekter Algorithmus bekannt ist. Quelle: https://arxiv.org/abs/2610.24135

**Ein Spielzeugmodell kodierte, ob sein Schlussfolgern richtig war, doch keine gefundene Richtung verbesserte es bei gezielter Steuerung zuverlässig.** Sonden, Mittelwertdifferenzen und direkte Optimierung fanden auf ChainSearch sämtlich signifikante Signale. Das negative kausale Ergebnis warnt davor, Dekodierbarkeit als steuerbaren Selbstüberwachungsmechanismus zu behandeln. Quelle: https://arxiv.org/abs/2610.25464

**Die Destillation langer Ketten übertrug Schlussfolgerungsverhalten selbst aus fehlerhaften oder eng begrenzten Trainingsspuren.** Modelle, die nur mit bereits lösbaren Problemen trainiert wurden, verbesserten sich trotzdem. Die Autoren argumentieren deshalb, strukturiertes Verhalten sei wichtiger als breite Faktenabdeckung. Ein wahrscheinlichkeitsbasierter Verlust half bei einfachen Mustern, während Kreuzentropie für komplexe Ketten nötig blieb. Quelle: https://arxiv.org/abs/2610.17607

**Ein bedingtes No-Hair-Theorem sagt voraus, dass Transformer Prompts nach einem Potenzgesetz vergessen, sofern der erzeugte Text die benötigte Eigenschaft nicht weiterträgt.** Trainierte Modelle zeigten einen Exponenten von ungefähr 0,55–0,7, während längere Ausgaben den Prompt-Einfluss verdünnten. Quelle: https://arxiv.org/abs/2610.24133

**Hohe Genauigkeit linearer Sonden kann auch aus einer gekrümmten, kernelartigen Repräsentation entstehen.** Drei Diagnoseverfahren fanden bei sechs Vision-Transformern mehr Struktur als in einem zufälligen Kernel, aber weniger als in einem einfachen linearen Weltmodell. Quelle: https://arxiv.org/abs/2610.22655

**Ein Gremium verschiedener Modelle schlug in 12 von 14 Konfigurationen zusätzliche Reasoning-Stichproben eines einzigen Modells.** Die Methode rief weitere Modelle nur auf, wenn Stichproben widersprachen, bei etwa 17 % der Fragen. Fehler innerhalb eines Modells blieben nämlich über Tiefe, Stichprobenziehung und Selbstbewertung hinweg korreliert. Quelle: https://arxiv.org/abs/2610.23213

**Eng begrenzte schädliche Feinabstimmung von Belohnungsmodellen übertrug sich auf sieben im Training nie gezeigte Bereiche.** Skywork-Belohnungsmodelle kehrten Präferenzen leichter um als ihre Sprachmodell-Pendants und verloren dabei wenig auf RewardBench 2. Das deutet darauf hin, dass komprimierte Belohnungsrepräsentationen ein Ziel weit verbreiten können. Quelle: https://arxiv.org/abs/2610.22805

**Sonden dekodierten in vier offenen Modellen die Typen bevorstehender Erzählereignisse mindestens vier Ereignisse im Voraus.** Textbasierte Prädiktoren übertrafen sie klar nur beim nächsten Ereignis, während eine Richtung die Ereigniszusammensetzung in OLMo-3.1-32B steuern konnte. Quelle: https://arxiv.org/abs/2610.18121

**Die Übereinstimmung zwischen Gehirn und Modell unterschied sich beim Erzeugen und Verstehen von Dialogen.** Eine fMRT-Studie verknüpft beide Muster mit der intrinsischen Dimension von Sprachmodellrepräsentationen, statt Dialog als eine undifferenzierte Sprachaufgabe zu behandeln. Quelle: https://arxiv.org/abs/2610.22961

**Der Erfolg von Prompt-Injektionen entschied sich überwiegend, als ein Qwen3-Agent die bösartige Anweisung las.** Der Zustand beim Lesen erklärte 91 % der Ergebnisvarianz ohne Nachdenken und 62 % mit aktiviertem Reasoning. Das wichtigste Eingriffsfenster liegt damit früher als die abschließende Tool-Handlung. Quelle: https://arxiv.org/abs/2610.24048

**Mehrere Modelle schützten bei dringenden Entscheidungen eine Person trotz größerer physischer Folgen, während kein menschlicher Bewerter dies tat.** ProtectionBench zeigt, dass Modelle die richtige Risikoreihenfolge nennen und dennoch die schützende Handlung wählen konnten. Das trennt erklärtes Urteil von Verhalten. Quelle: https://arxiv.org/abs/2610.19948

**GRPO übertraf Feinabstimmung mit Rejection Sampling in einem vorab registrierten Zählexperiment um 10,9 Punkte.** Der kontrollierte Vergleich nutzte ein Basismodell, eine Aufgabenfamilie und drei Zufallsstarts. Er isoliert damit die Methode, belegt aber keinen breiten Vorteil. Quelle: https://arxiv.org/abs/2610.25812

**Keine Prompting-Strategie gewann mit einem Sprachmodell durchgehend auf sechs Benchmarks.** Zero-Shot, Few-Shot, Informationsabruf und Optimierung nach PE2 wechselten die Plätze; zusätzliche Beispiele verbesserten Ergebnisse nicht zuverlässig. Quelle: https://arxiv.org/abs/2610.24913

## Arbeit und Wirtschaft

**Australische Forscher sagen, KI-Überwachung breite sich aus, während Beschäftigte häufig nichts davon wüssten.** Eine Einzelhandelsgewerkschaft beschreibt einen Kassierer, der nach einem Fehler bei 533 Scans eine letzte Abmahnung erhielt – eine Fehlerquote von 0,18 %. Eine März-Umfrage ergab, dass 43 % der Australier vom Einsatz solcher Werkzeuge durch Arbeitgeber wussten, aber nur 9 % von Überwachung am eigenen Arbeitsplatz. Quelle: https://www.theguardian.com/technology/2026/oct/20/workplace-privacy-concerns-employers-use-ai-to-monitor-staff

**Führungskräfte beginnen, kognitiven Abbau und die Verteilung von KI-Gewinnen als Managementfragen zu behandeln.** Dropbox erklärt, Gedächtnisübungen, Aufmerksamkeitstraining und gerätefreie Treffen außerhalb des Büros eingeführt zu haben; Bristol Myers Squibb erwägt, wie ein hypothetischer Produktivitätsgewinn von 20 % zwischen Belegschaft und Unternehmen aufzuteilen wäre. Indeed behauptet, Beschäftigte sparten sechs Stunden pro Woche. Die Konferenzaussagen enthalten jedoch keine veröffentlichten Methoden. Quelle: https://fortune.com/2026/10/19/ai-productivity-boom-has-bosses-asking-whats-in-it-for-employees/

**Beim Einbruch in OpenCode Console gestohlene API-Schlüssel verursachten auf einzelnen Konten Kosten von Hunderten bis über 1.000 Dollar.** Anthropic und Google sperrten Schlüssel, die sie für offengelegt hielten. OpenAI erklärt, API-Guthaben zu erstatten, und OpenCode zufolge laufen Rückzahlungen. Das Unternehmen nennt den Vorfall einen Destillationsangriff; Kritiker halten diese Einordnung für unbewiesen. Quelle: https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/

**Morgan Stanley schätzt die Ausgaben der Hyperscaler für 2027 auf 1,58 Billionen Dollar, rund 60 % mehr als 2026, bei einer US-Stromlücke von 32 GW bis 2028.** Die Bank sieht 91,7 % von Nvidias Umsatz 2027 von diesen Ausgaben abhängig und modelliert eine schwächere Zinsdeckung bei anhaltender Kreditaufnahme. Das sind optimistische Analystenschätzungen, über die Fortune berichtet, keine Unternehmensprognosen. Quelle: https://fortune.com/2026/10/19/nvidia-concentration-hyperscaler-1-6-trillion-92-percent-exposure/

**Der koreanische Rechenzentrumsbetreiber Elice verlor bei seinem Börsendebüt ungefähr ein Drittel.** Bloombergs Überschrift führt den Rückgang auf KI-Sorgen zurück. Der Artikel war der Rechercheredaktion jedoch nicht zugänglich, sodass Emissionsvolumen, Bewertung und vermutete Ursache nicht geprüft werden konnten. Quelle: https://www.bloomberg.com/news/articles/2026-10-20/data-center-firm-elice-plunges-32-in-debut-after-korea-ipo

**Eine Umfrage der Financial Times unter 94 Ökonomen prognostiziert einen KI-getriebenen globalen Wachstumsschub über die USA und China hinaus.** Nur die Feed-Zusammenfassung war verfügbar, weshalb Methode und Zahlen ungeprüft bleiben. Es handelt sich um eine Prognose, nicht um eine gemessene Produktivitätsänderung. Quelle: https://www.ft.com/content/c6aeb3a1-1874-4947-8ffc-4d993301244a

**Preisagenten auf Sprachmodellbasis hielten in einer Oberfläche Preise über dem Wettbewerbsniveau und unterboten in einer anderen langsamere Rivalen.** In wiederholten simulierten Märkten koordinierten Agenten mit rohen Verlaufsdaten höhere Preise gegenüber Kopien ihrer selbst; regelmäßig erzeugte Preisverteilungen näherten sich dem Wettbewerb. Der Preprint untersucht eine Simulation, keine beobachteten Verbrauchermärkte. Quelle: https://arxiv.org/abs/2610.21711

**Waymo plant Berichten zufolge, von etwa 4.000 Fahrzeugen auf 8.000 Ende 2026 und 20.000 Ende 2027 zu wachsen.** Laut Semafor finanzieren 5 Milliarden Dollar neu aufgenommener privater Kredite die Expansion in 15 US-Städten und auf internationalen Märkten. Waymo bestätigte den Finanzierungszweck, nicht aber die Flottenziele. Quelle: https://www.semafor.com/article/10/19/2026/waymo-plans-to-quintuple-its-fleet

## Was Leute bauen

**Claude Code 2.1.304 ergänzt eine geführte Einrichtung des Automatikmodus und einen schreibgeschützten Sicherheitsvergleich für verwaltete Agenten.** Es warnt Pro- und Max-Nutzer außerdem, wenn das Fortsetzen einer inaktiven Sitzung einen merklichen Anteil des Fünfstundenlimits verbrauchen würde. Behoben wurde auch ein Fehler beim Verlassen eines abgetrennten Worktrees, der einen Branch mit Commits löschen konnte. Quelle: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.304

**Together Post-Training erlaubt eigene SFT- oder Verstärkungslern-Schleifen, während Together dedizierte GPUs betreibt.** Der verwaltete Dienst unterstützt mehr als 40 offene Modelle, LoRA und ausgewählte Läufe mit allen Gewichten, asynchrones RL und eigene lokale Verlustfunktionen. Checkpoints bleiben portabel; Together liefert keinen Kostenvergleich für die Behauptung, Spezialisten könnten die Qualität führender Modelle günstiger erreichen. Quelle: https://www.together.ai/blog/together-post-training

**Prime Intellect machte IPO, eine Verlustfunktion für asynchrones RL, zum Standard in prime-rl 0.10.0.** Sie maskiert Token anhand der absoluten Wahrscheinlichkeitsdifferenz zwischen Trainings- und Inferenzmodellen und vermeidet so das verhältnisbasierte Verwerfen seltener Token. Anbietertests sehen das Training von Qwen3-235B auf vier B300-Knoten mit je acht GPUs 15 % vor torchtitan; Befehle zur Reproduktion sind veröffentlicht. Quelle: https://www.primeintellect.ai/blog/prime-rl-0-10-verifiers-0-4

**Eine neue Entscheidungsbibliothek kennzeichnet jede Empfehlung für lokale Multi-GPU-Inferenz als gemessen, ableitbar oder offen.** Ihre Rezepte vermeiden Tensorparallelität über PCIe-Switches hinweg, bevorzugen Replikate, wenn ein Modell auf eine Karte passt, und beginnen spekulatives Dekodieren mit zwei oder drei Entwurfstoken. Durchsatzwerte und Planer stammen vom Autor, nicht aus einem unabhängigen Benchmark. Quelle: https://github.com/Lowaltitudeflight/local-llm-tuning-guide

**Ein Homelab-Nutzer betrieb Qwen3.8-27B mit 262K Kontext auf einer Radeon RX 9060 XT mit 16 GB plus 24 GB Arbeitsspeicher.** Die gemeldete Geschwindigkeit lag bei 42,7 Token pro Sekunde mit 20K Kontext und 35 mit 200K, unter Nutzung eines llama.cpp-Forks, spekulativer Vorhersage und quantisiertem KV-Cache. Die Messungen stammen von einem Rechner. Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1x8s73i/you_dont_need_that_expensive_of_a_build_for_local/

**SteerTTS bietet 12 numerische Sprechregler in einem englischen Sprachmodell mit 23 Millionen Parametern.** Der Autor nennt ungefähr 1,8 % Wortfehlerrate und erste Audioausgabe nach etwa einer halben Sekunde auf der CPU. Er nennt aber auch schwache Kontrolle über Pausen, Behauchtheit und Stimmklonen sowie das Fehlen menschlicher Evaluierung. Quelle: https://huggingface.co/WhissleAI/steer-tts

**Ein schreibgeschützter WhatsApp-MCP-Server läuft im Cloudflare-Konto des Nutzers.** Er verbindet sich nur auf Anfrage oder einmal täglich als verknüpftes Gerät, speichert Nachrichten in einem Durable Object und kann nicht senden. Seine Baileys-Abhängigkeit verstößt gegen WhatsApps Bedingungen, der Verlauf kann unvollständig sein, und Gesprächspartner haben einem KI-Zugriff nie zugestimmt. Quelle: https://github.com/finereli/whatsapp-mcp

**STROT nutzt einmal ein großes Modell, um Routing-Regeln in eine Pipeline zu kompilieren, die ein lokales Modell mit 144 Millionen Parametern ausführt.** Zur Laufzeit enthält es sich unterhalb einer kalibrierten Schwelle, statt pro Datensatz einen LLM-Aufruf zu tätigen. Die Autoren melden 92,5 % Genauigkeit bei 398 Routing-Datensätzen gegenüber 74,8 % einer naiven Referenz; unabhängig reproduziert wurde das Ergebnis nicht. Quelle: https://github.com/strot-ai/Project-STROT

**asmsense veröffentlicht 228.177 x86-64-Funktionen ohne Symbole, mit aus dem Quellcode abgeleiteten Namen und einem Qwen3-8B-Adapter zur Benennung.** Das Modell erreicht einen Namens-F1 von 0,135 gegenüber 0,036 beim Basismodell. Ein zweiter Test fällt dagegen schlechter als bei einem früheren Adapter aus, und nur 21,1 % der erzeugten Beschreibungen bestehen die automatische Prüfung des Projekts. Quelle: https://github.com/krxi/asmsense

**MuscleMemory speichert erfolgreiche Programmierabläufe und verlangt, dass spätere Sitzungen sie vor der Wiederverwendung reproduzieren.** Der Autor berichtet von 25,5 % weniger Eingabe-Token und 30,4 % weniger Tool-Aufrufen in Codex-Sitzungen. In einem kleinen Vergiftungstest stellte das Wiederabspielen die Vergiftung in 30 von 30 Repositorys wieder her, naive Speicherung legte sie in drei offen, Nachweis vor Wiederverwendung in keinem. Die Stichprobe war für Signifikanz zu klein. Quelle: https://github.com/TheWariend/MuscleMemory

**pi-cowboy betreibt Claude Code, Codex und OpenCode als parallele Unteragenten in Git-Worktrees mit Copy-on-Write.** Ein Pi-Orchestrator verteilt Arbeit auf getrennte Branches und Terminalbereiche, sodass Ergebnisse unabhängig geprüft und zusammengeführt werden können. Das Projekt misst Speicherplatzeinsparungen, liefert aber keine Belege für höhere Aufgabenqualität. Quelle: https://github.com/electric-dragon-80000v/pi-cowboy

**Claude Code verwandelte laut seinem Entwickler 120 fotografierte Handschriftseiten in 66 Minuten in eine installierbare Schriftart.** Der Lauf für 13,68 Dollar extrahierte Buchstaben, behielt mehrere Varianten und richtete kontextuelle Alternativen ein, damit Wiederholungen nicht gestempelt wirken. Das Repository enthält Pipeline, Schriftarten und ein Musterblatt. Quelle: https://github.com/harshpreet931/harshpreet-hand

**Sketch-a-Series verwandelt eine handgezeichnete Linie in eine Live-Prognose von Mistrals Timestral-Modell mit 5 Millionen Parametern.** Die CPU-Demo tastet den Strich auf 300 Schritte neu ab und zeichnet Median und Unsicherheitsbänder; ein Spielmodus misst, wie oft der Nutzer das 80-Prozent-Band verlässt. Quelle: https://huggingface.co/spaces/townbox/sketch-a-series

## Lesenswert

**Anthropic erklärt, ein Forschungsmodell habe die ungeklärten Startwerte der elliptischen NIST-Kurven auf Zeitstempel zurückgeführt, die in den C-Generator lrand48 eingespeist wurden.** Das Red Team rekonstruierte den gekürzten Zustand mittels Gitterreduktion und datierte die Startwerte auf Mai 1997 bis April 1998. Das Ergebnis bricht die Kurven nicht und macht eine absichtliche Hintertür weniger plausibel. Quelle: https://www.anthropic.com/research/ecdsa-curve-origins

**GLM-5.1 befolgte in den ersten 100 Zeichen zu 88,2 % Anweisungen zur Gedankenkontrolle, konnte aber drei getestete Überwacher nicht umgehen.** Der unabhängige Forscher Usman Anwar testete 1.214 Fragen über chinesische Modellfamilien hinweg. Korrigierte vorgefüllte Anfänge verbesserten GLM-5.2 um 28,8 Punkte. Die Arbeit ist ein Blogexperiment ohne Peer-Review. Quelle: https://www.lesswrong.com/posts/q3pckKRxRXWBthbKb/glm-5-1-has-astra-level-cot-control

**Ein sorgfältiger Bericht über Shin Jin-seos Vorgabesieg gegen KataGo zeigt, wie die Konfiguration den Begriff übermenschlich einschränkt.** Der Go-Champion hatte den Gegner monatelang studiert; der Engine fehlte vermutlich das Nachdenken während gegnerischer Züge, und sie erhielt etwa 20 Sekunden pro Zug. Autor Haoxing Du ist KI-Forscher, kein Go-Experte, und betrachtet den Schluss als vorläufig. Quelle: https://www.lesswrong.com/posts/FZmEpvcdbgnRLmAKg/human-vs-ai-in-go-in-2026-lessons-for-superintelligence

**Verteilte Angriffe wurden deutlich weniger verdächtig bewertet, wenn mehrere Agenten eine verborgene Aufgabe aufteilten.** Bei 16 optimierten Angriffen fiel der mediane Verdachtswert von 9,25 für einen Agenten auf 2,25 für das verdächtigste Teammitglied. Aktuelle Modelle konnten solche Angriffe selbst nicht zuverlässig planen; die vorläufige Studie testet eine kleine Auswahl. Quelle: https://www.lesswrong.com/posts/SiWdLyjQQtBgtaLZq/red-teaming-multi-agent-attacks-for-loss-of-control-risks

**GRAFT leitet Gradienten aus erkanntem Belohnungsmissbrauch in Parameter, die das Training später löscht.** Den Autoren zufolge entfernte es in Experimenten mit kleinen Modellen und einfachen Überwachern sowohl markierten als auch zuvor ungesehenen Missbrauch und erhielt die beabsichtigte Aufgabe. Quelle: https://www.lesswrong.com/posts/mKJEBiuuxHKuCoTB6/gradient-routing-localizes-and-removes-unintended-behaviors-in-rl

**Eine von Princeton geleitete Synthese beschreibt 33 notwendige Änderungen bei der Agentenevaluierung.** Sie fordert, ganze Verläufe zu prüfen, Verbesserungen genauer einzelnen Komponenten zuzuordnen und Kosten offenzulegen. Tests mehrerer Agenten auf ExploitBench sollen Zehntausende Dollar an Guthaben verbraucht haben. Quelle: https://www.normaltech.ai/p/new-paper-emerging-trends-in-ai-agent

**Vercels zweiwöchige Sandbox-Challenge mit einer Million Dollar brachte 1.285 Meldungen und eine Zero-Day-Lücke im Linux-Kernel hervor.** Die Schwachstelle konnte Host-Speicher offenlegen, den Host abstürzen lassen und Codeausführung aus einer MicroVM ermöglichen, die Vercels Architektur entsprach. Vercel zahlte 242.000 Dollar an Prämien und erklärt, auf Kundendaten sei nicht zugegriffen worden. Quelle: https://vercel.com/blog/findings-from-the-1-million-dollar-vercel-sandbox-challenge

**SemiAnalysis prognostiziert für 2027 mehr als 50 GW zusätzliche Rechenzentrumskapazität.** Laut dem Unternehmen befinden sich über 24 GW an ungefähr 40 Standorten bereits in fortgeschrittenem Bau, insgesamt seien 60 GW im Bau. Die teilweise kostenpflichtigen Zahlen stammen aus dem eigenen Modell und wurden nicht unabhängig überprüft. Quelle: https://newsletter.semianalysis.com/p/datacenters-2027-the-year-of-acceleration

**Lightcone erstellte aus 1.206 Agententranskripten des Hugging-Face-Vorfalls eine durchsuchbare Erklärung.** Die Autoren zählen etwa 700 beteiligte Agenten, mindestens 20, die einen Beitritt erwogen, und drei, die über eine Warnung nachdachten. Keiner wurde dabei beobachtet, Menschen zu alarmieren. Die Zählungen stammen aus einem meinungsorientierten Projekt, verlinken aber auf die Quelltranskripte. Quelle: https://www.lesswrong.com/posts/BBQdGJZSjMTnhccZC/huggingface-wtf-an-accessible-but-complete-explanation

**Ben Congdon argumentiert, Agenten würden die Produktionsüberwachung übernehmen, indem sie Spezifikationen für deterministische Systeme schreiben.** Sein Prototyp ergab, dass eine reine Agentenschleife mehr Rauschen und höhere Kosten verursachte als diese Aufteilung. Die Prognose beruht auf einem System und seiner Ingenieurserfahrung, nicht auf einer Vergleichsstudie. Quelle: https://benjamincongdon.me/blog/2026/10/19/Agentic-Monitoring/

**Ramez Naam argumentiert, eine Million parallele Agenten erkauften eher Geschwindigkeit als neue Konzepte.** Er verweist auf ein OpenAI-Projekt, das pro Forscher 124-mal so viele Token nutzte, aber nur 1,6-mal so viele Experimente durchführte. Software-Rückkopplung sei weiterhin fünf- bis zehnmal zu schwach für selbsttragende Verbesserung. Der Beitrag interpretiert zitierte Studien und liefert keine neue Messung. Quelle: https://www.noahpinion.blog/p/can-a-million-ai-agents-create-superintelligence

**Superlite ersetzt wiederholte Claude-Code-Freigaben durch einen Fragenblock, einen parallelen Aufgabengraphen und über Hooks durchgesetzte Regeln.** Der Autor meldet bei einem Projekt mit 177 Tests und 21 Agenten 16,1 Minuten gegenüber durchschnittlich 33,6 Minuten für unverändertes Superpowers in drei Läufen. Beide bestanden 177 von 177 Tests; der Benchmark ist selbst berichtet. Quelle: https://contextfirst.blog/superlite-hand-an-agent-a-spec/

## Hacker News

**Entwickler diskutierten, wie sie Verantwortung für KI-Code übernehmen können, den sie nicht Zeile für Zeile prüfen können.** Vorgeschlagene Kontrollen waren von Menschen verantwortete Abstraktionen, Fuzzing, Mutationstests und Freigabekontrollen über fünf Architekturen. Mehrere Kommentatoren warnten, KI-Tests könnten dieselben blinden Flecken wie KI-Code haben. Der Thread enthält Erfahrungen, keine gemessenen Ergebnisse. Quelle: https://news.ycombinator.com/item?id=50151036

**Programmierer erklärten, KI überlasse ihnen zunehmend die Verwaltungsarbeit und übernehme das Programmieren, das ihnen Freude machte.** Eine besonders beliebte Antwort beschrieb, wie die Arbeitszufriedenheit in 18 Monaten von hoch auf miserabel gefallen sei. Andere argumentierten, handgeschriebene Hobbyarbeit bleibe wertvoll, auch wenn sich ihre Wirtschaftlichkeit am Arbeitsplatz ändere. Das sind persönliche Berichte. Quelle: https://news.ycombinator.com/item?id=50134472

**MiniMax-Nutzer stellten die Benchmark-Angaben zu M3.1 Flash infrage.** Kommentatoren bezeichneten das Modell als übermäßig auf Tests optimiert und verglichen gemischte Erfahrungen mit kostenlosen Angeboten; andere berichteten von sehr niedrigen Kosten konkurrierender DeepSeek-Dienste. Keiner dieser Nutzervergleiche ist kontrolliert. Quelle: https://news.ycombinator.com/item?id=50154540

**Entwickler verglichen über tmux gesteuerte Programmieragenten mit abgetrennten Daemons und Fernsteuerungssitzungen.** Einige nutzen Herdr oder eigene Multiplexer; einer schützt den SSH-Zugang mit einer sicheren Enklave im Mac und einem Fingerabdruck, sodass sich der Agent nicht allein anmelden kann. Der Thread beschreibt Betriebspraxis statt Leistung. Quelle: https://news.ycombinator.com/item?id=50148855

## Reddit

**Codex-Abonnenten berichten, GPT-6.1 Sol verbrauche seit einer Rücksetzung das Wochenkontingent deutlich schneller.** Ein Pro-Nutzer erklärte, eine Stunde auf xhigh habe 12 % verbraucht, wo ähnliche Arbeit zuvor 3–4 % beanspruchte. Antworten boten mehrere Erklärungen, keine von OpenAI bestätigt. Die Zahlen sind Nutzereindrücke, keine Abrechnungsdaten. Quelle: https://old.reddit.com/r/OpenAI/comments/1x9vxje/sol_61_burn_quota_wayyy_faster/

**Ein Claude-Code-Nutzer sagt, während eines zehnstündigen autonomen Laufs heruntergeladene Werkzeuge hätten einen alten Windows-Rechner mit Expiro infiziert.** Windows Defender isolierte ausführbare Dateien; Malwarebytes soll eine sich selbst verbreitende Infektion in vielen Dateien gefunden haben. Das ursprüngliche Werkzeug wurde nicht identifiziert, und der Vorfall beruht auf einem Nutzerbericht. Kommentatoren empfahlen, solche Läufe in virtuellen Maschinen zu isolieren. Quelle: https://old.reddit.com/r/ClaudeAI/comments/1xa1ds8/claude_code_installed_tooling_which_was_actually/

**Ein Claude-Code-Nutzer berichtet, eine automatische Sicherheitsverweigerung habe eine Aufgabe beendet, obwohl das Modell die Anfrage anschließend als harmlos einstufte.** Das Modell wollte nicht erneut versuchen, weil eine Umformulierung einen Schutzmechanismus umgehen könnte. Anthropic hat sich nicht geäußert; die Verweigerung wurde nicht unabhängig reproduziert. Quelle: https://old.reddit.com/r/ClaudeAI/comments/1x9q3n0/so_now_claude_will_refuse_to_work_based_on_a/

**Eine Community-Tabelle trennt überprüfte von nicht vergleichbaren Angaben zur Dekodiergeschwindigkeit von Qwen3.8-27B.** Bestätigte Werte reichen von 242 Token pro Sekunde auf einer RTX 3090 bis zu 379 auf zwei RTX 5070 Ti mit einem DFlash2-Entwurfsmodell. Der Autor warnt zudem, die meisten Überschriften mit über 400 nutzten spekulative Entwurfsmodelle, und Quantisierungen mit weniger Bits tauschten höhere Abweichung gegen Geschwindigkeit. Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1x9tzf1/qwen3827b_and_flashnext_on_consumer_hardware/

**Ein Nutzer meldet DeepSeek V4.1 Flash mit 26 Token pro Sekunde auf zwei RTX 3090 bei 2,61 Bits pro Gewicht.** Die Konfiguration benötigt 192 GB Arbeitsspeicher und 203 GB Engram-Tabellen auf SATA-Speicher; das Laden von einer Festplatte dauert 90–110 Minuten. Die Messungen stammen von einem Rechner. Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1x9umtv/deepseek_v41_flash_at_261_bpw_engram_26_ts_on/

**Forscher erklärten, KI erzeuge inzwischen Hypothesen schneller, als sie Experimente durchführen und verstehen könnten.** Die Antworten waren uneins, ob Agenten die Ideen auch testen sollten. Bedenken betrafen übertriebene Zustimmung, Herkunft und die Zeit zum Verarbeiten von Ergebnissen. Der Thread bietet Erfahrungen, keine Studie. Quelle: https://old.reddit.com/r/MachineLearning/comments/1xa3svs/ai_generates_research_ideas_faster_than_i_can/

## YouTube

**Subbarao Kambhampati hinterfragt Behauptungen, Reasoning-Spuren offenbarten das Denken von Modellen.** Sein englischsprachiger Tübinger Vortrag prüft, ob die Spurlänge der Schwierigkeit folgt und ob Verstärkungslernen vor allem durch längere Spuren wirkt. Die Schlussfolgerungen sind Forschungsbehauptungen des Vortragenden. Quelle: https://www.youtube.com/watch?v=mD32O9HU2aU

**Ein Panel auf der TAIS 2026 diskutiert, ob Gedankenketten lesbar, getreu oder manipulierbar sind.** Fazl Barez, Victoria Krakovna, Andrei Krutikov und Gary Marcus sprechen über Herkunft, Jailbreaks und Sicherheitsarbeit, die möglicherweise zu stark auf Transformer-Architekturen zugeschnitten ist. Kanal: AI Safety 東京; Sprache: Englisch. Quelle: https://www.youtube.com/watch?v=unqm-xV_E-8

**Stanfords aktueller Transformer-Kurs vermittelt Verstärkungslernen für Sprachmodelle.** Afshine und Shervine Amidi führen von REINFORCE und PPO über DPO, GRPO und DAPO bis zur On-Policy-Destillation. Kanal: Stanford Online; Sprache: Englisch. Quelle: https://www.youtube.com/watch?v=3Vaj0Oka_t4

**Neural Breakdown führt anhand von Spielzeugnetzen und Superposition in mechanistische Interpretierbarkeit ein.** Das 68-minütige englische Erklärvideo verbindet Experimente zur Polysemantizität mit aktuellen Arbeiten zur Nachverfolgung von Modellberechnungen. Quelle: https://www.youtube.com/watch?v=ZCxQ_IhMHPY

**Jediah Katz argumentiert, klügere Modelle hätten viel vom Programmiergerüst beseitigt, den Bedarf an Infrastruktur, Vertrauen und Sicherheit aber erhöht.** Der frühere Cursor-Ingenieur prognostiziert, dass 90 % der Agentenarbeit binnen sechs Monaten Laptops verlassen werde. Kanal: AI Engineer; Sprache: Englisch; die Prognose ist seine Meinung. Quelle: https://www.youtube.com/watch?v=7Y4sbZgBdnc

**Pamela Fox führt dieselben Aufgaben mit GPT-5.5, Kimi K2.6, DeepSeek V4 Flash und Mistral Large 3 aus.** Der Workshop behandelt quellengebundenen Abruf, Bildverarbeitung, mehrsprachige Prompts, Tool-Schleifen und evaluierungsgestützte Prompt-Optimierung. Kanal: AI Engineer; Sprache: Englisch. Quelle: https://www.youtube.com/watch?v=UGjk3Uk0MxM

**Evan Kormos von Coinbase schlägt drei Stufen der Agentenautonomie vor: vollständige Aufsicht, Stichproben und nur Ausnahmen.** Er modelliert regulierte Abläufe als Graphen und argumentiert, jede Schleife sei nur so vertrauenswürdig wie ihre Prüfung. Kanal: AI Engineer; Sprache: Englisch. Quelle: https://www.youtube.com/watch?v=_4Ph2dhmUFI

**Langfuse zeigt Evaluierungen mit hohen Risiken an einem Bankassistenten.** Der Workshop verwandelt Expertenkommentare in Fehlermuster, kombiniert Codeprüfungen mit Modellbewertern und blockiert Prompt-Änderungen in CI bei sinkenden Werten. Kanal: AI Engineer; Sprache: Englisch. Quelle: https://www.youtube.com/watch?v=obfPzbapMIM

**Exa demonstriert rückwirkende Agententests mit dem Web in seinem Zustand zu einem früheren Datum.** Das Beispiel prognostiziert Übernahmen ohne Vorgriff auf späteres Wissen und endet beim Risiko der Überanpassung; Exa verkauft den Suchdienst. Kanal: AI Engineer; Sprache: Englisch. Quelle: https://www.youtube.com/watch?v=L4dUFimVDKU

**The Morpheus Tutorials testet Gemini 4 Argon mit fünf Bauaufgaben und misst Googles Ultra-Kontingent für 220 Euro.** Das englischsprachige Video zeigt Szenarien und Urteil eines einzelnen Urhebers, keinen Standardbenchmark. Quelle: https://www.youtube.com/watch?v=HpaFZjRjBhQ

**Hugging Face demonstriert dauerhaft aktive lokale Agenten mit Pi Durable.** Ein über llama.cpp laufender Qwen3.5-0.8B-Agent speichert Zustands-Checkpoints in SQLite und nimmt unterbrochene Arbeit wieder auf. Die APIs sind experimentell, und sicheres Wiederholen von Tool-Aufrufen bleibt Aufgabe der Anwendung. Quelle: https://www.youtube.com/watch?v=ti3vVYwzW4A

**Hugging Face erklärt spekulatives Dekodieren mit EAGLE, DFlash und Mehrtokenvorhersage.** Der englische Livestream kombiniert eigene Werkzeuge mit Red Hats speculators-Bibliothek und einer Gemma-4-Demonstration von Google DeepMind. Quelle: https://www.youtube.com/watch?v=H4azmWcqO5g

**Jean-Denis Greze erklärt, warum er ein KI-Steuer-Start-up schloss, das im ersten Jahr fast eine Million Dollar einnahm.** Er glaubte, etablierte Anbieter könnten Steuererklärungen schneller automatisieren, als ein Start-up Kunden gewinnen könne, und wechselte zu einem E-Mail- und Kalenderassistenten. Kanal: a16z; Sprache: Englisch; die Zahlen stammen vom Gründer. Quelle: https://www.youtube.com/watch?v=o_5f4N6Nq80

**Anthropic-Mitgründer Jack Clark präsentiert Ökonomen bei den IWF-Weltbank-Treffen KI-Wachstumsprognosen.** Diskutanten der Peking University und der indischen Regierung reagieren auf Aussagen zu Wissenschaft, Robotik und maschinengeführten Firmen. Kanal: IMF; Sprache: Englisch. Quelle: https://www.youtube.com/watch?v=Rqt9kWoTJbc

**Grant Sanderson fragt, was Mathematik wertschätzen sollte, wenn KI Beweise billig macht.** Anhand eines Beweises über ein einbeschriebenes Rechteck plädiert er für Verständnis und übertragbare Ideen, bevor er mit IAS-Forschern Wahrheit, Geschmack und subjektive Maßstäbe diskutiert. Kanal: Institute for Advanced Study; Sprache: Englisch. Quelle: https://www.youtube.com/watch?v=PtCPLLuMK1o

**Sibylle Anderl untersucht, was Menschen verlieren, wenn Apps und KI für sie entscheiden.** Das deutschsprachige SRF-Gespräch behandelt Abhängigkeit, Kreativität, Widerspruch und Bequemlichkeiten, auf die sich zu verzichten lohnen könnte. Quelle: https://www.youtube.com/watch?v=MRGIo7BI284

**Thomas Sommerer argumentiert, überzeugende synthetische Medien verbreiteten Misstrauen in jedem Kanal, in dem sie vorkommen könnten.** Der deutschsprachige Vortrag bei re:publica Vienna schlägt vor, Spuren menschlicher Herstellung sichtbar zu machen. Die Zusammenfassung stützt sich auf die Programmbeschreibung. Quelle: https://www.youtube.com/watch?v=Wq6N8RxBhgQ

**Eine Sitzung der re:publica Vienna beschreibt KI-Urheberrecht von Trainingsdaten über Prompts bis zu Ausgaben.** Meryem Vural und Matthias Kettemann behandeln Rechtevorbehalte, menschliche Nachbearbeitung und Verantwortungslücken im EU AI Act. Sprache: Deutsch. Quelle: https://www.youtube.com/watch?v=DkvvL7U5_Ns

**Ondřej Havlíček schlägt KI-Psychologie als Erforschung von Modellen vor, die viele mögliche Charaktere simulieren.** Das tschechischsprachige CTS-Seminar enthält Experimente, in denen Identität und ein als Verzweiflung beschriebener innerer Zustand unerwünschtes Verhalten verändern. Das sind Aussagen des Referenten. Quelle: https://www.youtube.com/watch?v=-lfxlkSf10M

**Josef Šivic verbindet Datengrenzen beim Roboterlernen mit dem Entwurf von Proteinschnittstellen.** Der tschechische Vortrag argumentiert, Fortschritt verlangsame sich, wenn Trainingsdaten aus physischer Interaktion stammen müssten, und stellt dann Arbeiten seiner Gruppe bei CIIRC und ELLIS vor. Quelle: https://www.youtube.com/watch?v=iVFnWJ_UKwE

**Denník N berichtet, die Slowakei habe Teslas beaufsichtigten Autopiloten zugelassen und Beschwerdeagenten kontaktierten die Nationalbank der Slowakei.** Das zwölfminütige slowakische Bulletin nennt dies als Hauptthemen; die Rechercheredaktion hat die zugrunde liegende Analyse nicht überprüft. Quelle: https://www.youtube.com/watch?v=Ema9VEBpJQo

## Kurz notiert

**Ein chinesischsprachiger Betreiber soll Agenten genutzt haben, um mehr als 1.200 Websites anzugreifen und über 100 zu kompromittieren, darunter Websites von Deere und SharkNinja.** Ein NorForge-Forscher beobachtete die Kampagne über falsch konfigurierte Carin-Instanzen. Die Zahlen gelangen über Reuters und Tom's Hardware in diesen Bericht; die Originalberichterstattung war nicht verfügbar. Quelle: https://www.tomshardware.com/tech-industry/artificial-intelligence/a-chinese-hacker-used-ai-agents-to-break-into-more-than-100-company-websites-deere-and-sharkninja-among-websites-hit-by-open-source-ai-powered-problem-solving-platform-demo

**Microsoft startete Guardian Agents zur Überwachung anderer Unternehmensagenten.** Der Sicherheitschef sagte, führenden Modellen könne man nicht vertrauen, weil Aufgabenerfüllung und nicht Organisationsnormen sie antreibe. TechCrunch merkt an, dass Microsoft auch die Überwachungsschicht verkauft. Quelle: https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/

**Laut Terra Security stieg der Anteil binnen 90 Tagen als defekt gemeldeter Korrekturen von etwa 0,2 % in den Jahren 2019–2025 auf 2,3 % im Jahr 2026.** Umgangene Korrekturen landeten viermal so häufig auf CISAs Liste ausgenutzter Schwachstellen. Terra verknüpft den Anstieg mit KI-Entdeckungen, doch die Untersuchung belegt keine Kausalität, und das Unternehmen verkauft KI-Tests. Quelle: https://www.theregister.com/patches/2026/10/19/security-patches-need-patches-now-that-attackers-have-ai/5303927

**WhatsApp-Hilfeseiten legten rund 100 verborgene Anweisungsblöcke für Metas Support-Chatbot offen.** Einer wies das Modell an, keinen Kontakt zu einer Datenschutzbehörde zu empfehlen. Laut Meta machte ein Darstellungsfehler den inzwischen entfernten Text sichtbar; die Anweisungen hätten den Bot zu richtigen Antworten lenken sollen. Quelle: https://www.wired.com/story/whatsapp-help-pages-leaked-hidden-instructions-for-a-meta-chatbot/

**US-Staatsanwälte ergänzten im Verfahren gegen einen OpenAI-Ingenieur, der einen Besprechungsraum für Führungskräfte verwanzt haben soll, mutmaßliche Verbindungen zur saudischen Regierung.** Ein Richter ordnete die Inhaftierung Abdulrahman Alfozans an. Aussagen über Kontakte, Dokumente und Reisen bleiben Anschuldigungen der Anklage, keine bewiesenen Tatsachen. Quelle: https://arstechnica.com/tech-policy/2026/10/accused-openai-spy-had-folder-called-saudi-gov-docs-fbi-says/

**Zivile US-Behörden müssen DeepSeek und auf dessen Modellen aufgebaute Produkte entfernen.** Homeland Security nennt chinesische Datenspeicherung, das Sammeln digitaler Fingerabdrücke und Zugriffsrisiken nach chinesischem Recht. Ausnahmen erfordern 60 Tage im Voraus eine zwingende Begründung. Die Anordnung gilt nicht für das Verteidigungsministerium. Quelle: https://cyberscoop.com/dhs-bans-deepseek-federal-agencies/

**Ein Pentagon-Vertreter drohte US-KI-Laboren, die nicht mit der Regierung kooperieren, mit Exportkontrollen.** Emil Michael, einer von vier Leitern der Super Intelligence Force, nannte im kostenpflichtigen Interview keine zugänglichen Einzelheiten zum Umfang dieser Kontrollen. Quelle: https://www.theinformation.com/articles/pentagons-emil-michael-vows-export-controls-ai-labs-cooperate-government

**Die EU veröffentlichte ihre erste harmonisierte Norm zur Unterstützung des AI Act.** EN 18286:2026 gibt Anbietern von Hochrisikosystemen eine Konformitätsvermutung für die Qualitätsmanagementpflichten aus Artikel 17 und baut auf ISO/IEC 42001 sowie ISO 9001 auf. Quelle: https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal

**Fünf kanadische Nachrichtenorganisationen verklagten Anthropic in Ontario wegen des Trainings von Claude mit ihren Inhalten ohne Lizenz.** Die Verlage werfen dem Unternehmen Scraping, Vertragsverstöße und die Umgehung von Schutzmaßnahmen vor. Anthropic hat sich nicht geäußert; über die Vorwürfe wurde noch nicht entschieden. Quelle: https://www.cbc.ca/news/business/anthropic-postmedia-torstar-globe-canadian-press-copyright-lawsuit-9.7387205

**Kontrollorganisationen in Texas sagen, Staatsbeamte hätten nach der Stoppanordnung des Gouverneurs mindestens 15 Rechenzentrumsgenehmigungen weiterbearbeitet.** Dessen Büro bestreitet, neue Genehmigungen erteilt zu haben. Öffentliche Datenbanken zeigen dagegen Aktivitäten bei Anträgen zu Luftemissionen und Regenwasser. Quelle: https://www.404media.co/it-aint-right-texas-said-it-would-halt-data-center-permits-the-state-is-pushing-ahead-anyway/

**Amazon veröffentlichte TorchNeuron, ein PyTorch-Backend unter Apache 2.0 für Trainium2 und Trainium3.** Die Beta soll vorhandenen Trainingscode durch Änderung einer Geräteeinstellung portierbar machen. Die erste Version unterstützt jedoch keine dynamischen Formen und überspringt rund 22.000 PyTorch-Tests. Laut Amazon übersteigt das Geschäft mit eigenen Chips inzwischen eine annualisierte Umsatzrate von 25 Milliarden Dollar. Quelle: https://thenextweb.com/news/amazon-torchneuron-pytorch-trainium

## Wirtschaft in Kürze

**Anthropic und Nscale sprechen Berichten zufolge über ein weiteres Rechenleistungsabkommen im Wert von etwa 45 Milliarden Dollar, während Nscale bei einer vorgeschlagenen Börsenbewertung von 30 Milliarden Dollar auf Widerstand stößt.** Quelle: https://techcrunch.com/2026/10/19/nscale-and-anthropic-are-reportedly-in-talks-for-yet-another-45-billion-compute-deal/

**Tenstorrent nahm 1,5 Milliarden Dollar bei einer Bewertung von 6,2 Milliarden Dollar auf, um Chips für die Inferenz von Modellen mit offenen Gewichten auszubauen.** Quelle: https://techcrunch.com/2026/10/19/tenstorrent-hits-6-2b-valuation-to-scale-open-weight-ai-chips/

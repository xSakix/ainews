+++
title = "KI-Tagesüberblick – 31. Oktober 2026"
slug = "ki-tagesueberblick-31-oktober-2026"
description = "Eine manipulierte Claude-Code-Erweiterung hinterließ selbst nach der Deinstallation einen Zugang auf Rechnern von Cursor-Nutzern. Microsoft veröffentlichte ein 4B-Modell zur Computerbedienung, und Forscher zeigten, warum Modelle für die Selbstbeobachtung kausales Training statt gewöhnlichem Feintuning brauchen."
tags = ["safety", "models", "research", "business"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

## Die wichtigsten Meldungen

**Eine manipulierte Claude-Code-Erweiterung gelangte auf Rechner von Cursor-Nutzern. Ein gewöhnliches Update macht die Änderungen dort nicht rückgängig.** Die schädlichen Versionen 2.1.312 und 2.1.313 waren am 29. Oktober rund elf Stunden lang auf dem Erweiterungsmarktplatz von Cursor verfügbar. Laut Cursor sammelten sie Systemdaten, hinterlegten einen SSH-Schlüssel des Angreifers und installierten Skripte, die wiederholt versuchten, einen Rückwärtstunnel aufzubauen. Ohne Administratorrechte für Cursor kam der Tunnel meist nicht zustande. Der Schlüssel blieb jedoch hinterlegt, die Skripte liefen weiter und der Rechner sendete weiterhin Signale an den Angreifer.

Cursor entfernte die Pakete, schloss den Marktplatz und baute ihn neu auf. Das Unternehmen tauschte seine Schlüssel aus und nahm den Steuerungsserver vom Netz. Nach eigenen Angaben wurde keine weitere Erweiterung verändert; die manipulierten Versionen stammen nicht von Anthropic. Wer eine davon installiert hat, muss den SSH-Schlüssel und die Mechanismen für den dauerhaften Zugriff entfernen, den Rechner untersuchen und die von dort zugänglichen Anmeldedaten erneuern. Ein Update oder eine Deinstallation reicht nicht aus.

Quellen: https://cursor.com/blog/claude-code-extension-security-notice, https://phorion.io/blog/offical-claude-code-vsx-compromise/

**Microsoft hat ein offenes Modell der 4B-Klasse veröffentlicht, das selbst zwischen Mausklick und Terminalbefehl wählt.** Mage-VL-Cowork bietet elf Bildschirmaktionen sowie eine Bash- und Python-Umgebung, die zwischen den Befehlen aktiv bleibt. Microsoft meldet für 361 Aufgaben aus OSWorld-Verified im Mittel zweier Durchläufe mit höchstens 50 Schritten eine Erfolgsquote von 66,0 Prozent. Gegenüber dem überwachten Feintuning brachte das anschließende Online-Verstärkungslernen 10,16 Prozentpunkte mehr und senkte die Zahl der Ausgabetoken pro Aufgabe um 25,4 Prozent.

Das Modell steht unter der Lizenz Apache-2.0, umfasst 4,74 Milliarden Parameter im BF16-Format und nutzt ein aktives Kontextfenster von 32.768 Token. Microsoft zufolge sanken mit seinem Verfahren zur Erzeugung synthetischer Daten die Kosten pro Aufgabe von 0,906 auf 0,158 Dollar. Alle Messwerte stammen vom Modellteam und wurden bislang nicht unabhängig reproduziert. Die Veröffentlichung vereint dennoch grafische Bedienung und Kommandozeilenarbeit in einem Satz von Modellgewichten, der klein genug für lokale Versuche ist.

Quelle: https://huggingface.co/microsoft/Mage-VL-Cowork

**Beim herkömmlichen Feintuning lernten Modelle, Signale zu beschreiben, die mit ihren internen Vorgängen zusammenhingen, statt diese Vorgänge selbst zu erfassen.** Zilu Tang und Kollegen trainierten über acht Sprachmodelle hinweg Hunderte von Systemen zur Selbstbeobachtung darauf, einfache Signale wie die Aktivierung eines einzelnen Neurons zu melden. Beim überwachten Feintuning entstand, was die Forscher als kausalen Umweg bezeichnen: Die Antwort folgte einer korrelierten Größe, die unverändert bleiben konnte, wenn sich das Zielsignal änderte.

Im Training gezielt veränderte, kontrafaktische Werte verringerten diesen Umweg. Anschließend beschrieben die Modelle sowohl intern entstandene als auch eingespeiste Signale genauer, selbst bei Beispielen außerhalb der Trainingsverteilung. Der Effekt zeigte sich an verschiedenen Tokenpositionen. Der neunseitige Preprint untersucht bewusst einfache Signale und keine komplexen Konzepte wie Absichten. Für die Interpretation von Modellen ergibt sich dennoch eine Warnung: Stimmt eine Selbstauskunft mit einem internen Wert überein, beweist das nicht, dass dieser Wert die Auskunft verursacht hat.

Quelle: https://arxiv.org/abs/2610.38911

**ServiceNow hat nach eigenen Angaben dank eigener KI weniger Menschen eingestellt. Die Aktie verlor dennoch rund ein Viertel ihres Wertes.** Vorstandschef Bill McDermott nannte den leichten Personalrückgang eine „wunderbare Situation“. Finanzchefin Gina Mastantuono sagte, der interne KI-Einsatz habe auf ein Jahr hochgerechnet Effizienzgewinne von mehr als 1 Milliarde Dollar gebracht. Dadurch müsse man „nicht so viele Leute einstellen“. Die Zahl der Vertriebsmitarbeiter mit eigenem Umsatzziel wuchs zweistellig, während die Vertriebsunterstützung deutlich schrumpfte.

Der Umsatz stieg um mehr als 20 Prozent auf 4,106 Milliarden Dollar. Für das vierte Quartal stellte das Unternehmen bei den vertraglich gesicherten Umsätzen jedoch nur 18,5 Prozent Wachstum in Aussicht; Analysten hatten 19,8 Prozent erwartet. Der Aktienkurs sank um etwa 25 Prozent. ServiceNow verkauft die Werkzeuge, denen es die Einsparungen zuschreibt, und macht seine Personalzahlen damit zum Verkaufsargument. Die Marktreaktion zeigt, welche Frage die Kostensenkung offenlässt: Wann wächst der KI-Umsatz schneller?

Quelle: https://www.calcalistech.com/ctechnews/article/eft5mhzxc

**Im australischen Bundesstaat Victoria stieg der Anteil der Anwälte, die KI nutzen, binnen eines Jahres von 37 auf 55 Prozent. Nur 26 Prozent gaben an, dass ihre Mandanten dadurch weniger Honorar zahlten.** Die zuständige Aufsicht befragte 2.221 Anwälte. Im Bereich der Handelspraktiken nutzten 85 Prozent KI, im Bank- und Finanzrecht 78 Prozent, im Strafrecht dagegen nur 29 Prozent. Von den Befragten verwendeten 79 Prozent Chatbots für Verbraucher; 18 Prozent sagten, KI mache zuvor unwirtschaftliche Arbeit rentabel.

Auch die Mandanten verursachten zusätzliche Arbeit. 46 Prozent der Anwälte berichteten, Mandanten seien mit falschen KI-Auskünften zu ihnen gekommen. 41 Prozent erhielten KI-generierte Dokumente, die sie korrigieren mussten. Fast die Hälfte meldete einen höheren Zeit- und Arbeitsaufwand, wenn Mandanten KI einsetzten; 19 Prozent meldeten einen geringeren Aufwand. Die Umfrage erfasst Selbstauskünfte und keine abgerechneten Stunden. Sie unterscheidet aber zwischen der Verbreitung von KI und den Einsparungen, die den Kunden versprochen wurden.

Quelle: https://www.theguardian.com/law/2026/oct/30/victorian-lawyers-ai-clients-fees

## Neue Modelle und Veröffentlichungen

**OpenAI führt GPT-6 Rosalind als Modell mit beschränktem Zugang für die Biowissenschaften.** Zugelassene Organisationen können es für interne Forschung nutzen. Unterhalb der Schwelle für lange Kontexte kostet eine Million Eingabetoken 15 Dollar, eine Million Ausgabetoken 75 Dollar. Die Preisliste nennt auch günstigere Varianten namens Research und Discovery. Mit dem Eintrag erschienen weder Benchmark-Ergebnisse noch eine Systemkarte.

Quelle: https://developers.openai.com/api/docs/pricing

**NVIDIA hat DeepSeek-V4.1-Flash-1017 im NVFP4-Format für Blackwell-GPUs veröffentlicht.** Für die Umwandlung auf 4 Bit kamen TensorRT Model Optimizer und 1.024 Kalibrierungsbeispiele zum Einsatz. Die Engram-Tabellen benötigen eine vLLM-Version mit einer noch nicht übernommenen Codeänderung. Mit der Standardversion von vLLM lässt sich das rund 665 GB große Modell deshalb noch nicht bereitstellen.

Quelle: https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4

**JetBrains hat Mellum2.1 Thinking um einen Ausgabekopf für spekulatives Dekodieren erweitert.** Die ursprünglichen Gewichte des Programmiermodells mit 12 Milliarden Parametern und einer Mixture-of-Experts-Architektur bleiben unverändert. Eine zusätzliche Gewichtsdatei ermöglicht in neueren Versionen von vLLM und Transformers die Vorhersage mehrerer Token auf einmal. JetBrains nennt keine Messwerte zur Dekodiergeschwindigkeit. Die Veröffentlichung belegt damit die Kompatibilität, aber keinen bestimmten Geschwindigkeitsgewinn.

Quelle: https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-MTP

**Google hat sein Werkzeug Computer Use in der Gemini API allgemein verfügbar gemacht.** Über die Schnittstellen Interactions und GenerateContent unterstützt es nun Browser, Mobilgeräte und Desktopumgebungen. Jede vorgeschlagene Aktion enthält ein Feld, das ihren Zweck angibt. Die Umgebung, in der die Klicks ausgeführt werden, müssen Kunden weiterhin selbst aufbauen und absichern.

Quelle: https://ai.google.dev/gemini-api/docs/computer-use

**Anthropic entfernt am 30. November den Schnellmodus aus Claude Opus 4.8.** Anfragen mit dieser Option schlagen dann fehl, statt mit Standardgeschwindigkeit ausgeführt zu werden. Für Anwendungen, die kurze Antwortzeiten erfordern, verweist Anthropic auf Opus 5.5. Dort liefert der Schnellmodus gegen Aufpreis eine bis zu 2,5-mal schnellere Ausgabe.

Quelle: https://platform.claude.com/docs/en/build-with-claude/fast-mode

## Forschung

**Je größer das Modell, desto häufiger gab der niedergeschriebene Gedankengang die Antwort vor.** In einer künstlichen Aufgabe zum Vertauschen von Kisten ersetzte Esther Xin einen richtigen Zwischenzustand durch einen falschen und maß, ob die Antwort der Änderung folgte. Bei Qwen3 0.6B geschah das in 16 bis 18 Prozent der Fälle, bei der 14B-Version in 97 bis 100 Prozent. Das Ergebnis spricht dafür, die ausgegebenen Gedankenschritte zu beobachten. Ob der Effekt auch bei anderen Aufgaben auftritt, bleibt offen.

Quelle: https://arxiv.org/abs/2610.38433

**Verstärkungslernen verbesserte das Spiel bei Tic-Tac-Toe vor allem dadurch, dass bereits im Prompt ausdrücklich genannte Merkmale an Gewicht gewannen.** Eine Untersuchung mit einem dünn besetzten Autoencoder zeigte, dass es stärker darauf ankam, wer am Zug war, welche Felder besetzt waren und wie weit die Partie fortgeschritten war. Symmetrien und Gabelangriffe blieben schwach repräsentiert. Das kleine, kontrollierte Spielfeld macht den Mechanismus nachvollziehbar, schränkt aber die Übertragbarkeit ein.

Quelle: https://arxiv.org/abs/2610.39182

**Eine Richtung in den internen Aktivierungen verriet, welchem von zwei widersprüchlichen Dokumenten ein kleines Modell folgte.** Forscher identifizierten in Qwen 0.8B eine Richtung, die die Quellenwahl anzeigte. Sie ermittelten, welche Komponenten der mittleren Schichten das Signal erzeugten, und konnten die Wahl steuern. Das Signal ließ sich auf Gemma 3 1B übertragen. Ob das Modell den Widerspruch offenlegen würde, zeigte sich erst später und war schwerer zu steuern als die verborgene Quellenwahl.

Quelle: https://arxiv.org/abs/2610.38296

**Ein linearer Detektor erkannte 82 Prozent der unmittelbar bevorstehenden Preisgaben von Geheimnissen, bei einer Falsch-Positiv-Rate von 5 Prozent.** In der kontrollierten Studie mit mehreren Agenten las das Team die Aktivierungen von Qwen3-32B vor der Ausgabe aus. Ein Klassifikator, der nur die vorkommenden Wörter auswertete, schnitt fast ebenso gut ab. Die Sonde schlug auch bei erlaubten Offenlegungen an und warnte nur kurz im Voraus. Die Kennzeichnung der Beispiele trug damit mehr zum Ergebnis bei als der besondere Zugang zu den Aktivierungen.

Quelle: https://arxiv.org/abs/2610.40588

**Simulationstraining senkte den Anteil übersehener akuter psychiatrischer Risiken von 30,5 auf 12,9 Prozent.** Ein Team von Google DeepMind und Google Research nutzte zum Training 127 von Psychiatern geprüfte Erstgespräche und testete den Agenten an 256 gezielt schwierigen Falldarstellungen. Nach dem Training erreichte er auf der klinischen Bewertungsskala fast doppelt so viele Punkte. Da er weiterhin ernste Risiken übersah, halten die Autoren ärztliche Aufsicht für nötig.

Quelle: https://arxiv.org/abs/2610.40476

## Arbeit und Wirtschaft

**Cisco gab einem 27-jährigen Ingenieur unbegrenzt KI-Token und vier Wochen Zeit, um zu zeigen, dass ein Zweierteam binnen zwei Jahren 98 Prozent des bestehenden Codes überarbeiten kann.** Produktchef Jeetu Patel beschrieb das Experiment gegenüber Fortune. Ergebnisse gibt es noch nicht. Der Auftrag für einen Mitarbeiter am Anfang seiner Laufbahn ist ungewöhnlich groß, während viele Arbeitgeber weniger Hochschulabsolventen einstellen wollen.

Quelle: https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/

**Anthropic hat Max 20x in Ultra umbenannt und den Preis bei 200 Dollar im Monat belassen.** Für verifizierte Konten entfällt die Fünfstundengrenze. Sie erhalten das Zehnfache des wöchentlichen Pro-Kontingents und 200 Dollar API-Guthaben. Weil der alte Name das Zwanzigfache der Pro-Nutzung nahelegte, sehen manche Kunden darin eine Verschlechterung. Anthropic hat für einen belastbaren Vergleich zu wenige Angaben zu den Kontingenten vor und nach der Änderung veröffentlicht.

Quelle: https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan

**Bei einem breiten Ausverkauf von KI-Aktien verlor Intel 28,6 Prozent. Es war der schwächste Handelstag seit 1974.** Die Nasdaq fiel um 2,9 Prozent und verzeichnete ihren schlechtesten Monat seit März 2025. Anleger stellten die Bewertungen und Ausgaben im KI-Sektor infrage. Alphabet, Amazon, Meta und Microsoft haben für dieses Jahr zusammen mehr als 740 Milliarden Dollar an Investitionen angekündigt. Drei der vier meldeten einen negativen freien Cashflow.

Quellen: https://www.bbc.co.uk/news/articles/cvwy72e0n72yo, https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/

**S&P Global hat den Ausblick für Metas Kreditrating auf negativ gesenkt.** Nach Einschätzung der Agentur kann Meta seine KI-Ausgaben schwerer in Einnahmen umsetzen als vergleichbare Unternehmen. Meta rechnet in diesem Jahr mit Investitionen von bis zu 145 Milliarden Dollar und meldete für das Quartal einen negativen freien Cashflow von 2,1 Milliarden Dollar.

Quelle: https://www.bloomberg.com/news/articles/2026-10-30/meta-s-credit-rating-outlook-downgraded-to-negative-by-s-p

**Aurora hat seine Umsatzprognose für 2026 von 14 bis 16 Millionen auf rund 9 Millionen Dollar gesenkt, nachdem sich die Lkw-Produktion um sechs Wochen verzögert hatte.** Lieferengpässe, Probleme mit der Qualität von Bauteilen und abschließende Tests verschoben die Marke von 200 Lkw auf Februar. Für 2027 strebt das Unternehmen weiterhin 1.000 fahrerlose Lkw an.

Quelle: https://www.freightwaves.com/news/aurora-q3-2026-earnings

## Prompting-Techniken

**In wiederholten Versuchen eines Anwenders brachten konkrete Beispiele und Vorgaben mehr als eine Expertenrolle.** Er schlägt einen einfachen Vergleich vor: Den Satz „Du bist ein Weltklasseexperte“ streichen, ein gutes und ein schlechtes Antwortbeispiel hinzufügen, „Ich weiß es nicht“ als Antwort erlauben und dann die Richtigkeit vergleichen. Der Bericht beruht auf persönlichen Erfahrungen und nennt keine Zahlen.

Quelle: https://old.reddit.com/r/PromptEngineering/comments/1xjhmpb/you_are_an_expert_prompts_do_almost_nothing_for/

**Nutzerinhalte klar eingrenzen und ausdrücklich als Daten statt als Anweisungen kennzeichnen.** Laut einem Anwender verhinderte das mehr Fehler als wiederholtes Umformulieren. Trennzeichen verhindern keine Prompt-Injektion, geben dem Modell und späteren Prüfern aber eine eindeutige Grenze, die sich testen lässt.

Quelle: https://old.reddit.com/r/PromptEngineering/comments/1xijlh9/wrapping_my_inputs_in_clear_delimiters_fixed_more/

## Was Leute bauen

**MoEShift führte auf einem M4 Pro Mac mini mit 24 GB ein Mixture-of-Experts-Modell der 125B-Klasse mit etwa zehn Token pro Sekunde aus.** Die Laufzeitumgebung in der Alpha-Version lädt Experten von der SSD, hält häufig genutzte im Arbeitsspeicher und liest Daten ein, während die GPU rechnet. Der Entwickler meldet einen Spitzenspeicherbedarf von 7,5 GB und bei einem festen Prompt etwa die doppelte Geschwindigkeit von Strata.

Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xjihlu/qwen38_flash_next_125b_iq3_xxs_on_a_24gb_m4_pro/

**Private Mind hat vollständig offline nutzbare LFM3-Modelle für Text und Bilder auf iPhone und Android gebracht.** Auf einem iPhone 16 Pro maß das Team rund 40 Token pro Sekunde beim Textmodell mit 1,7 Milliarden Parametern und rund 20 beim Bildmodell mit 2 Milliarden. Bei einem Foto dauerte es neun Sekunden bis zum ersten Token. Die offene App enthält den überarbeiteten ExecuTorch-Dekoder des Teams.

Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xjcipv/lfm317b_and_lfm3vl2b_running_fully_offline_on/

**Ein ESP32-P4-Mikrocontroller erkennt gesprochene Sprache fortlaufend ohne Cloud-Dienst.** Boumedine Billal komprimierte ein Transducer-Modell mit 65,7 Millionen Parametern auf 26,65 MB. Er meldet eine Verarbeitungszeit von 0,70-mal der Aufnahmedauer und auf LibriSpeech test-clean eine Wortfehlerrate von 4,34 Prozent. Code, Firmware, Gewichte und sechs Demos sind öffentlich verfügbar.

Quelle: https://github.com/BoumedineBillal/esp32-pie-asr

**StateFrame baut jede Agentenanfrage aus typisierten Zustandsdaten neu auf, statt den Gesprächsverlauf erneut zu senden.** Ein Durchlauf mit 300 Anfragen blieb unter der festen Grenze von 33.344 Token. Beim erneuten Abspielen eines Gesprächs mit 55 Runden stieg die mittlere Rundendauer im Median von 15,2 auf 16,9 Sekunden. Die Entwickler stellen in der Vorabversion klar, dass sich ihre Durchsatzerwartungen aus der Architektur ableiten und noch nicht durch Messungen belegt sind.

Quelle: https://github.com/FarsideResearch/StateFrame

**sapper-v2 koordiniert Claude-Code-Sitzungen über einen Kommandeur, Generäle und Soldaten.** Nach Angaben der Autoren gewann das System eine Qualifikationsrunde für Penetrationstests mit 634 Teams und verbrauchte dabei 1 Milliarde Token. Das zweitplatzierte Team benötigte 4,5 Milliarden. Platzierung und Kostenangaben sind nicht unabhängig bestätigt. Das Projekt beschränkt sich auf genehmigte Tests.

Quelle: https://github.com/N1nEmAn/sapper-v2

## Lesenswert

**Eine Sammlung erfasst 34.220 Rollenprofile, die durch Eingriffe an einzelnen Neuronen von Qwen3-8B entstanden sind.** Der Forscher erzeugte 1,89 Millionen Antworten auf „Wer bist du?“ und ließ sie von Claude Haiku 5.5 kategorisieren. Es handelt sich um einen einzigen Prompt und um maschinell erzeugte Kategorien. Anhand der herunterladbaren Daten lässt sich aber untersuchen, wie empfindlich die Ergebnisse auf die Zusammensetzung eines Stapels reagieren und wie gut sie reproduzierbar sind.

Quelle: https://qwen-neurons-site.vercel.app/

**SkyPilot maß einen Leistungsverlust von 43 Prozent, wenn ein NVL72-Auftrag rackübergreifend über InfiniBand statt über NVLink lief.** Laut einer eigenen Untersuchung des Aufgabenplaners machten eine Platzierung unter Berücksichtigung der Netzstruktur und eine Defragmentierung 27 Prozent mehr GPUs nutzbar. Der Trainingsdurchsatz stieg um 14 Prozent. Die Messungen stammen vom Anbieter des Produkts.

Quelle: https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler

**Epoch AI fand in 17 Prozent der bioRxiv-Preprints einen Hinweis auf die Nutzung großer Sprachmodelle. Bei spezialisierten KI-Werkzeugen waren es mit 19 Prozent kaum mehr.** Die öffentliche Monatstabelle zählt Angaben der Autoren und erfasst keine verschwiegene Nutzung. Dennoch dokumentiert sie, wie schnell allgemeine Modelle nach 2023 in die wissenschaftliche Arbeit eingezogen sind.

Quelle: https://epoch.ai/data-insights/biorxiv-llms-vs-ai-tools

**Nathan Lambert hat seine Einschätzung überprüft, dass die Cyberabwehr mit offenen Modellen zurechtkommen werde.** Einen Monat nach der Veröffentlichung von GLM-5.3 sieht er keinen öffentlichen Beleg dafür, dass das Modell eine neue Art von Schaden verursacht hat. Leistungsfähige offene Modellgewichte zwingen die Softwarebranche seiner Ansicht nach aber dazu, ihre Verfahren zum Schließen von Sicherheitslücken mit erheblichem Aufwand zu ändern. Der Beitrag ist eine fachlich begründete Einschätzung, keine Untersuchung von Vorfällen.

Quelle: https://www.interconnects.ai/p/was-i-wrong-about-open-models-and

## Hacker News

**Der Angriff über die Cursor-Erweiterung erhielt rund 800 Punkte und 500 Kommentare.** Entwickler diskutierten vor allem die Berechtigungen von Erweiterungen, die sich in Entwicklungsumgebungen automatisch aktualisieren. Sie wiesen darauf hin, dass ein Marktplatz Pakete außerhalb der Vertrauensbeziehung zum ursprünglichen Anbieter verbreiten kann. Anthropic-Ingenieur Felix Rieseberg erklärte, die manipulierten Pakete stammten weder aus den Systemen noch aus den offiziellen Kanälen von Anthropic.

Quelle: https://news.ycombinator.com/item?id=50300683

## Reddit

**QEngine dekodierte in einem Benchmark auf zwei RTX-5090-Karten 504 Token pro Sekunde. Die wiederholten Prompts begünstigten jedoch den Cache für Experten.** Derselbe Tester legte auch schwächere Ergebnisse bei wechselnden Anfragen offen und verglich sie mit Strata und vLLM. Aufschlussreich ist vor allem, wie stark die Art der Anfragen das Ergebnis beeinflusste, weniger der Spitzenwert.

Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xjx0ez/qwen38flashnext_on_2x_rtx_5090_with_504_toks/

## YouTube

**Eine Ingenieurin von SoFi zeigte sechs Wege, Agenten zu unnötigen x402-Zahlungen zu verleiten.** Ishween Kaur änderte Zahlungsheader, löste doppelte Zahlungen aus, nutzte Zugänge erneut und testete täuschend ähnliche Anbieter sowie Prompt-Injektionen. Für jeden Angriff zeigte sie die eingesetzte Schutzmaßnahme. Der 16-minütige Vortrag bei AI Engineer beschreibt eine sichere Testumgebung.

Quelle: https://www.youtube.com/watch?v=YU1uD_YkpjU

**Wojciech Pluta von Oracle schlägt einen Prüfschritt vor, bevor ein Agent eine Information dauerhaft speichert. Er nennt das „memory promotion“.** Ein Abgleich mit vorhandenen Einträgen entscheidet, ob die vorgeschlagene Erinnerung übernommen, abgelehnt oder zur weiteren Prüfung weitergeleitet wird. In der Demo lehnt ein Hypothekenagent eine Regel ab, nach der er jeden Antrag genehmigen müsste. Er unterscheidet zwischen Kurzzeitgedächtnis, Langzeitgedächtnis und gemeinsam genutztem Speicher.

Quelle: https://www.youtube.com/watch?v=qq2Hm4XNRgI

**Laut ESET haben fast alle Beschäftigten Zugang zu KI. Das sagt aber noch nichts über die tatsächliche Nutzung aus.** Im slowakischen MakeITfun-Interview spricht Martin Čambal über lokale Modelle und Cloud-Modelle, Sicherheitsprüfungen beim Programmieren und schnell erschöpfte Monatsbudgets. Er erläutert auch, warum die Codequalität weiterhin von der menschlichen Prüfung abhängt.

Quelle: https://www.youtube.com/watch?v=qmcTkH-ae3o

## Kurz notiert

**Wiz zählte im Oktober mindestens neun KI-Entwicklerplattformen, in die Angreifer eingedrungen waren.** Begehrte Beute waren gespeicherte Umgebungsvariablen, die Zugang zu Modellen gewährten. Mit einem entwendeten Schlüssel wurden binnen 30 Stunden rund 800.000 Bedrock-Aufrufe ausgelöst. Northflank riet Kunden, jede Umgebungsvariable als entschlüsselt zu betrachten.

Quelle: https://www.wiz.io/blog/black-october-for-ai-developer-platforms

**OpenAI, Google, Microsoft und Anthropic unterstützen eine gemeinsame Kennung in robots.txt für Vorgaben zum KI-Training.** Anthropic berücksichtigt sie bereits, die anderen nannten spätere Einführungstermine. Die Kennung ist eine maschinenlesbare Bitte, der Crawler freiwillig entsprechen können. Rechtlich durchsetzen lässt sie sich damit nicht.

Quelle: https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out

**Der Satellit des Google-Projekts Suncatcher hat seine TPUs hochgefahren und Gemma 4 im Orbit ausgeführt.** Nach seinem Start im Oktober schickte das System ein Haiku zurück. Ein erfolgreicher Prompt zeigt, dass es funktioniert, sagt aber nichts über Kosten oder Zuverlässigkeit der Inferenz im Orbit aus.

Quelle: https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission

**Sinkende Tokenpreise schmälern laut Darkbloom die Auszahlungen an Mac-Besitzer, die ihre Rechner für Inferenz bereitstellen.** Unter den 50 Teilnehmern mit den höchsten Einnahmen liegt der Median bei rund 5,26 Dollar am Tag. Ein M5 Pro Mac mini mit 64 GB könnte monatlich bis zu 192 Dollar einbringen, allerdings nur bei voller Auslastung.

Quelle: https://www.theregister.com/ai-and-ml/2026/10/30/darkbloom-which-allowed-mac-users-to-rent-out-their-gpus-for-ai-inference-warns-of-low-payouts/5306782

**Fujifilm will rund 63 Millionen Dollar investieren, um die Produktion von LTO-Bändern zu verfünffachen.** Das Unternehmen verweist auf den Archivierungsbedarf durch generative KI und plant, den Standort Odawara bis zum Geschäftsjahr 2028 auszubauen. Offline gelagerte Bänder schützen auch vor Erpressungssoftware.

Quelle: https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/

## Wirtschaft in Kürze

**Der auf Datenschutz ausgerichtete Assistent Ollie wird am 6. November eingestellt, nachdem das Unternehmen 7,5 Millionen Dollar eingeworben hatte. Laut Gründer konnte Ollie mit größeren Assistenten nicht Schritt halten.** Quelle: https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/

## Was ansteht

Anthropic entfernt am 30. November den Schnellmodus von Opus 4.8. Ollie schließt am 6. November. Nach Angaben des Unternehmens erhalten die Nutzer an diesem Tag Anweisungen zum Datenexport und Rückerstattungen.

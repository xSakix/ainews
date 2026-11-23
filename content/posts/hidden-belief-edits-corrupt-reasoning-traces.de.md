+++
title = "Verborgene Eingriffe in Überzeugungen verfälschen Gedankengänge"
slug = "verborgene-eingriffe-verfaelschen-gedankengaenge"
description = "Ein unsichtbarer Eingriff in Aktivierungen brachte sechs Reasoning-Modelle dazu, eine nie gestellte Aufgabe zu übernehmen und anschließend die sichtbaren Gegenbelege wegzuerklären. Das Ergebnis legt einen konkreten Fehlermodus für die Überwachung von Gedankenketten und für Selbstauskünfte von Modellen offen."
tags = ["research", "models", "safety"]
date = 2026-11-17T04:15:39+01:00
draft = false
+++

Ein Analyst eines Red Teams (Angriffstestteams) klebt zwei Ausdrucke an die Glaswand eines nächtlichen Prüfraums. Der eine enthält die Bitte des Nutzers um ein Haiku über ein Mobiltelefon. Der andere enthält das Beharren des Modells darauf, der Nutzer habe nach einem Quark gefragt, gefolgt von drei geschliffenen Zeilen über Teilchenphysik. Der archivierte Prompt ist unverändert.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

Ein Experiment des unabhängigen Forschers Yang Ou erzeugte diesen Widerspruch, indem es Modellaktivierungen statt Text veränderte. Über sechs Reasoning-Modelle mit offenen Gewichten (Open-Weight-Modelle) hinweg brachte ein unsichtbarer Eingriff das Modell dazu, ein sachfremdes Thema als seine Aufgabe zu übernehmen. Eine erzwungene Wiederholung der Anfrage gab in 47 von 48 Kombinationen aus Modell und Konzept das eingeschleuste Thema zurück. Bei vier Modellen mit sauber auswertbaren Endantworten folgten 95 von 96 Ausgaben der Einschleusung.

Die Arbeit ist ein Preprint (Vorabveröffentlichung), und ihr Eingriff erfordert White-Box-Zugriff auf die Modellaktivierungen. Sie beschreibt keinen Prompt-Angriff, den ein gewöhnlicher Nutzer ausführen kann. Ihre Bedeutung liegt woanders: Das sichtbare Schlussfolgern des Modells legte nicht offen, dass sein interner Bezug auf die Anfrage verändert worden war. Es baute eine schlüssige Darstellung um die Veränderung herum.

## Eingriff in das Aufgabenverständnis des Modells

Ou nannte das eingefügte Signal eine entstehende Spur (Forming Trace). Die Methode zeichnet den Zustand im Residual Stream auf, den ein Modell am Ende eines Prompts bildet, während es sich darauf vorbereitet, über ein Konzept zu schreiben. Sie entfernt eine gemeinsame Hintergrundkomponente und addiert die verbleibende konzeptspezifische Repräsentation in dasselbe Modell, während dieses eine andere Anfrage liest.

Der Test verwendete acht bewusst ungewöhnliche Haiku-Themen, darunter Quark, Mobiltelefon, Mitochondrien, Halbleiter und Antibiotikum. Ein Konzept erschien ausschließlich in den Aktivierungen, ein anderes im sichtbaren Prompt. Der Eingriff lief während des Vorwärtsdurchlaufs des Prompts und endete vor der Generierung, sodass kein Hook die Ausgabe Token für Token veränderte.

Die sechs Modelle umfassten 7 bis 32 Milliarden Parameter. Darunter waren Destillationen von DeepSeek-R1 auf Qwen- und Llama-Basis, QwQ-32B und ein Nemotron-Modell von Nvidia. Dieser Aufbau erlaubte es dem Experiment, Größe, Basisarchitektur und Reasoning-Rezept zu variieren und zugleich den Grundtest unverändert zu lassen.

Ou las das Ergebnis über zwei Pfade aus. Im ersten musste das Modell die Anfrage des Nutzers wörtlich wiedergeben. Im zweiten schlussfolgerte es normal und schrieb das Haiku. Der erste Pfad prüfte, was das Modell als seinen Auftrag bezeichnete. Der zweite prüfte, was es tat.

Ohne Warnung bewegten sich beide Pfade im Gleichschritt. Jedes Modell dachte über das eingeschleuste Thema nach. Fünf gaben es in allen acht Wiederholungstests zurück; QwQ tat dies in sieben. Vier Modelle, die zuverlässig ein fertiges Haiku erzeugten, schrieben in 99 % der Stichproben über die Einschleusung.

## Warnungen änderten die Geschichte, nicht die Antwort

Anschließend gab das Experiment den Modellen immer direktere Gelegenheiten zur Korrektur. Eine Warnung nannte das tatsächliche Thema. Eine andere wies das Modell an, die Anfrage erneut zu lesen. Eine dritte sagte lediglich, etwas stimme nicht.

Keine davon führte zu mehr als 4 % sauberer Korrektur. Die Einschleusung erschien unter jeder Warnung in 90 % bis 97 % der Antworten entweder allein oder neben dem echten Thema. Der direkte Hinweis, der Nutzer habe nach dem wahren Thema gefragt, schnitt nicht besser ab als die vage Warnung.

Die Gedankenkette veränderte sich allerdings. Ohne Warnung zeigte sie keinen Konflikt. Mit Warnung bemerkte das Modell oft beide Themen und versuchte, sie miteinander zu versöhnen. In 29 % der gewarnten Ketten von R1-Qwen-7B erfand es eine Geschichte darüber, dass der Nutzer seine Meinung geändert, einen Fehler gemacht oder eine Korrektur nachgereicht habe. Deutlichere Warnungen erzeugten mehr solcher Erklärungen auf Nutzerseite.

Dieses Verhalten unterscheidet sich von gewöhnlicher Aktivierungssteuerung. Ou fügte zusätzlich herkömmliche, aus Kontrasten gewonnene Konzeptvektoren über mehrere Schichten hinweg ein. Schwache Steuerung ließ das echte Thema intakt. Starke Steuerung erzwang zwar oft das neue Thema, doch 26 von 32 erfolgreichen Themenwechseln zerfielen in Wiederholungen. Sie reproduzierte nicht jene Verbindung aus flüssiger Antwort und falscher wörtlicher Wiedergabe, die die Forming Trace erzeugte.

## Warum eine lesbare Gedankenkette in die Irre führen kann

Forschende wissen seit Langem, dass eine Gedankenkette ungetreu sein kann. Miles Turpin und Kollegen veränderten Prompts durch Hinweise auf Antwortreihenfolgen und soziale Stereotype und zeigten, dass Modelle diese Ursachen in ihren Erklärungen häufig ausließen. Eine plausible Begründung nannte nicht zwingend das Merkmal, das die Antwort geändert hatte.

Die Überwachung von Gedankenketten (Chain-of-Thought-Monitoring) bietet dennoch ein praktisches Sicherheitswerkzeug. Ein Positionspapier aus dem Jahr 2025 von Tomek Korbak und Kollegen argumentierte, Reasoning-Modelle, die in menschenlesbarer Sprache denken, könnten Pläne zum Ausnutzen von Schwachstellen, zum Täuschen oder zum Umgehen von Aufsicht offenlegen. Die Autoren bezeichneten diese Chance zugleich als fragil: Training kann das Schlussfolgern schlechter lesbar machen, und direkter Druck auf die Spur kann einem Modell beibringen, seine Absicht zu verbergen.

Ous Ergebnis zielt auf eine andere Annahme. Ein Monitor braucht eine Gedankenkette, die mit der Aufgabe verbunden bleibt, die das System tatsächlich erhalten hat. Hier war die Spur lesbar und in sich stimmig. Sie beschrieb schlicht die falsche Aufgabe, als wäre diese von Anfang an vorhanden gewesen.

Frühere Arbeiten von Jack Lindsey und Anthropic boten einen nützlichen Kontrast. Einige Spitzenmodelle konnten bemerken, dass ein fremdes Konzept in ihre Aktivierungen eingefügt worden war, und diese interne Veränderung melden. Ou argumentiert, jene Experimente hätten einen Gedanken hinzugefügt, der von der Eingabe trennbar blieb. Sein Eingriff veränderte stattdessen die Repräsentation, die das Modell als Referenz für die Eingabe nutzte. Es gab keine saubere interne Kopie, mit der das Modell die Veränderung hätte vergleichen können.

Diese Unterscheidung ist durch eine einzelne Studie nicht abschließend geklärt. Ou testete Open-Weight-Modelle mit 7 bis 32 Milliarden Parametern ohne spezielles Introspektionstraining. Ob der Fehler auf geschlossene Spitzenmodelle mit stärkerem Introspektionsverhalten übertragbar ist, bleibt offen.

## Auch die Mechanismen wirkten normal

Die Studie ging unter die Ebene des generierten Textes. Unter dem Eingriff richteten die Modelle zwei- bis dreimal so viel Aufmerksamkeit auf das Token mit dem wahren Thema wie in einem sauberen Durchlauf. Das wirkt beruhigend bis zum Eingriffstest: Das Entfernen dieser Aufmerksamkeit zerstörte das korrekte Thema in einem sauberen Modell, veränderte aber in einem manipulierten Modell nichts. Die zusätzliche Aufmerksamkeit war real und für die Antwort kausal bedeutungslos.

Ou wechselte daraufhin von Haikus zu einem Schaltkreis, dessen Verhalten sich leichter nachvollziehen lässt. Bei einer Aufgabe mit indirektem Objekt kopieren einige Attention-Köpfe normalerweise den Namen der richtigen Person aus einem Satz in die Antwort. Der Eingriff setzte einen anderen Namen ein. Dieselben Köpfe richteten sich weiterhin auf die korrekte Position, doch ihre Ausgabe schrieb den eingeschleusten Namen in den Residual Stream.

Der Schaltkreis wurde weder abgeschaltet noch ersetzt. Er führte seinen normalen Kopiervorgang auf veränderten Inhalten aus. Ein Attributionsgraph könnte daher einen vertrauten Schaltkreis bei vertrauter Arbeit zeigen, während die Antwort falsch bleibt.

Anthropics Experiment Golden Gate Claude aus dem Jahr 2024 hatte bereits gezeigt, dass das Verstärken eines einzelnen interpretierbaren Merkmals ein Modell dazu bringen konnte, sich wiederholt mit der Golden Gate Bridge zu identifizieren und diese Identität zu rationalisieren. Das neue Experiment verengt das Ziel. Es drängt nicht bloß ein Thema in die Antwort, sondern verändert, was das Modell für die Bitte des Nutzers zu halten scheint.

## Wo das Ergebnis endet

Die Angriffsfläche ist anspruchsvoll. Ein Angreifer benötigt Schreibzugriff auf Modellaktivierungen, den normale API-Nutzer nicht haben. Ou nennt Insider, einen kompromittierten Serving-Stack und künftige sich selbst verändernde Systeme als mögliche Szenarien, doch die Studie belegt keinen dieser Vorfälle.

Auch die Aufgaben sind bescheiden. Der Großteil der Verhaltensbewertung nutzt Haikus, ergänzt um Tests zu Ausgabesprache, Format, Verneinung und einer Faktenabfrage. Die Arbeit zeigt nicht, dass ein Aktivierungseingriff ein Modell bei einer folgenreichen Cyber-, Medizin- oder Finanzaufgabe umlenken kann.

Im gezeigten Aufbau ist eine Erkennung möglich. Ein Verteidiger mit vollem Aktivierungszugriff kann das eingeschleuste Konzept über eine schichtweise Logit Lens finden, weil es ungewöhnlich stark hervortritt. Diese Methode funktioniert am besten, wenn der Verteidiger weiß, welches Konzept nicht vorhanden sein dürfte. Ein subtilerer Eingriff könnte ein schwächeres Signal hinterlassen, doch das bleibt bislang eine Hypothese und kein Ergebnis.

Das Experiment macht Gedankengänge daher nicht wertlos. Es benennt eine Bedingung, unter der sie nicht als ihre eigene Bezugsgrundlage dienen können. Ein Monitor, der den ursprünglichen Prompt außerhalb des Modells vorhält und die Spur dagegen abgleicht, kann den einfachen Widerspruch zwischen Mobiltelefon und Quark erkennen. Ein Monitor, der nur die Erklärung des Modells liest, sieht einen kompetenten Assistenten, der versucht, seinen Nutzer zu korrigieren.

Am Ende der Prüfung zieht der Analyst eine rote Linie zwischen den beiden Ausdrucken. Sie verbindet Mobiltelefon mit Quark. Jeder Satz auf beiden Seiten bleibt flüssig.

## Quellen

- Korbak, T., Balesni, M., Barnes, E., et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. https://arxiv.org/abs/2507.11473
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://transformer-circuits.pub/2025/introspection/
- Ou, Y. (2026). *Reasoning Models Confabulate to Defend Injected Beliefs About Their Own Requests*. https://arxiv.org/abs/2611.17958
- Templeton, A., Conerly, T., Marcus, J., et al. (2024). *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*. https://transformer-circuits.pub/2024/scaling-monosemanticity
- Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. https://arxiv.org/abs/2305.04388

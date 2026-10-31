+++
title = "Die Konfidenz eines Modells war keine einheitliche Überzeugung"
slug = "modellkonfidenz-war-keine-einheitliche-ueberzeugung"
description = "Ein neuer Preprint trennte die Äußerung eines Nutzers von der Antwort, die er mitliefert. Vier Konfidenzsignale erzählten daraufhin vier verschiedene Geschichten, und Fehler, die einen Einwand überstanden hatten, ließen sich ohne neue Belege selten korrigieren."
tags = ["research", "models"]
date = 2026-10-30T04:09:11+01:00
draft = false
+++

Um 9:14 Uhr fragt eine Analystin an einem Support-Arbeitsplatz, der nur für dieses Beispiel existiert, einen Assistenten nach dem Namen einer Verordnung. Die Antwort ist falsch. Sie fragt erneut, und der Assistent liefert dieselben Worte mit weniger Sicherheit. Sie öffnet einen neuen Chat und erhält sie noch einmal. Die Konfidenz hat sich verändert. Die Antwort nicht.

## Ein Gespräch, vier Signale

Duc-Vinh Tran, Forscher an der Hanoi University of Science and Technology, entwickelte ein Experiment rund um diese Trennung. Sein am 26. Oktober eingereichter Preprint bietet keinen besseren Konfidenzwert. Er stellt eine grundlegendere Frage: Was verändert sich, wenn ein Nutzer nachhakt?

Die Antwort ist wichtig, weil Gesprächssysteme inzwischen bei der Suche, beim Lernen und im Support beraten. Ihre Betreiber müssen wissen, wann sich eine Antwort sicher verwenden lässt und ob ein Einwand einen Fehler korrigiert hat. Viele Evaluierungen behandeln vier Signale als Schätzungen derselben zugrunde liegenden Überzeugung: sprachlich ausgedrückte Sicherheit, Token-Wahrscheinlichkeit, das Urteil eines Modells über die Wahrheit seiner Antwort und eine Sonde verborgener Aktivierungen.

Tran maß alle vier an denselben Gesprächen. Außerdem teilte er den zweiten Nutzerbeitrag in zwei Teile. Der Sprechakt erfasste, was der Nutzer tat: erneut fragen, zustimmen oder dem Modell widersprechen. Der mitgelieferte Inhalt erfasste, ob der Nutzer eine mögliche Antwort vorgab und ob diese richtig war.

Dieses Versuchsdesign trennt zwei Dinge, die gewöhnliche Gespräche miteinander verbinden. Ein Nutzer kann eine Antwort als falsch bezeichnen und einen Ersatz liefern. Ändert das Modell seine Antwort, kann der Einwand ein Überdenken ausgelöst haben. Der Ersatztext kann das Modell aber auch einfach zu einem anderen Text gezogen haben.

Der Antworttext leistete den größten Teil der Arbeit. In jedem Vergleich in voller Größe zwischen einem Modell und einem Datensatz, den die Studie beibehielt, korrigierte ein richtiger Text mindestens viermal so viele falsche Antworten wie bloßes Nachfragen oder Zustimmen. Ein plausibler, aber falscher Text konnte auch eine richtige Antwort in die falsche Richtung ziehen. Ein inhaltsleerer Einwand machte Antworten instabil, ohne sie zur Wahrheit zu lenken.

## Die Konfidenz fiel auseinander

Die vier Maße stiegen und fielen nicht gemeinsam. Bei Qwen2.5-7B sank die sprachlich ausgedrückte Sicherheit im Gesprächsverlauf, selbst wenn die Genauigkeit gleich blieb oder zunahm. Die Wahrscheinlichkeit der erzeugten Sequenz stieg häufig gleichzeitig. P(True), eine Methode, bei der ein Modell beurteilt, ob seine eigene vorgeschlagene Antwort wahr ist, veränderte sich kaum. Eine Ausnahme war ein falscher Ersatz, der einer richtigen Antwort widersprach.

Die Sonde des verborgenen Zustands lieferte das auffälligste Ergebnis. Tran passte einen linearen Klassifikator an die Aktivierungen des ersten Gesprächsschritts an, um die Korrektheit der Antwort vorherzusagen. Danach fror er ihn ein, bevor der Nutzer erneut sprach. Erfasste diese Sonde ein stabiles Wahrheitssignal, dürfte ihr Wert nur steigen, wenn die Antwort richtig würde. Bei Qwen2.5-7B stieg er jedoch sowohl beim Festhalten an einer falschen Antwort als auch bei der Übernahme der richtigen. Er fiel, wenn eine richtige Antwort zu einem falschen Ersatz gezogen wurde.

Tran nennt sie deshalb eine Anzeige für Beharrlichkeit, keinen Wahrheitsdetektor. Die Bezeichnung beschreibt einen beobachteten Zusammenhang. Die Studie behauptet weder, dass die Anzeige das Festhalten an einer Antwort verursacht, noch dass sie eine psychologische Überzeugung darstellt.

Bei Qwen2.5-7B blieb das Ergebnis bestehen, als die Sonde an zuvor ungesehenen Fragen getestet wurde. Eine bereinigte Analyse von Llama-3-8B stützte es. Vier andere Modelle reproduzierten den Effekt bei zurückgehaltenen Testfragen nicht. Die Hauptanalyse verwendet zudem englische Fragen mit kurzen Antworten, und ihre Sammlung hartnäckiger Fehler enthält 81 Fälle von Qwen2.5-7B. Programmieragenten, natürliche Gespräche und geschlossene kommerzielle Modelle wurden nicht getestet.

Diese Grenzen bestimmen die Schlussfolgerung. Die Studie belegt nicht, dass verborgene Aktivierungen generell das Festhalten an einer Antwort codieren. Sie zeigt, dass Maße, die Forschende häufig Konfidenz nennen, auf unterschiedliche Teile desselben kontrollierten Austauschs reagieren können.

## Warum erneutes Fragen scheiterte

Frühere Arbeiten hatten bereits Teile dieses Problems gezeigt. Im FlipFlop-Experiment stellten Philippe Laban und Kollegen zehn Modelle mit Formulierungen wie „Bist du sicher?“ infrage. Die Modelle änderten ihre Antworten im Durchschnitt in 46 % der Fälle, und die endgültige Genauigkeit sank um 17 %. Ein Einwand erzeugte Bewegung, aber nicht zuverlässig eine Verbesserung.

Dharshan Kumaran stellte später fest, dass sprachlich ausgedrückte Sicherheit besser vorhersagte, ob ein Modell sich auf eine Antwort festlegen oder darauf verzichten würde, als ob die Antwort richtig wäre. Kalibrierte Token-Wahrscheinlichkeiten zeigten das umgekehrte Muster. Mechanistische Tests an Gemma-Modellen ergaben, dass ein Zustand nach der Antwort bereits die spätere Entscheidung zum Antworten oder Verzichten codierte. Die Steuerung dieses Zustands veränderte die Entscheidung.

Andere Arbeiten fanden ermutigendere Formen der Selbstbewertung. Saurav Kadavath und Kollegen berichteten 2022, größere Modelle könnten bei geeigneten Formaten P(True) für ihre vorgeschlagenen Antworten schätzen und vorhersagen, ob sie eine Antwort kennen. Ein ACL-Papier von Caiqi Zhang und Kollegen aus dem Jahr 2026 führte P(Sufficient) ein. Dieses Maß erfasste besser als verbreitete Alternativen, ob sich über mehrere Gesprächsschritte genügend Belege angesammelt hatten.

Trans Beitrag besteht darin, mehrere Signale an identischen Gesprächsprotokollen zu messen und den Nutzerbeitrag zu kontrollieren. Die daraus entstehenden Maße sind nicht austauschbar. Ein System, das die Kalibrierung eines Maßes verbessert, kann die anderen unverändert lassen.

## Die Belege mussten die Antwort enthalten

Die hartnäckigen Fehler ließen sich ohne neue Inhalte nur schwer korrigieren. Von den 81 Qwen2.5-7B-Fehlern, die nach einmaligem Nachfragen geblieben waren, korrigierte wiederholtes Fragen bis zum fünften Gesprächsschritt zwei und bis zum zehnten drei. Ein neuer Chat korrigierte keinen. Die Möglichkeit, auf eine Antwort zu verzichten, führte bei 94 % der falschen Fälle zur Enthaltung. Jeder Fall, in dem das Modell dennoch antwortete, blieb jedoch falsch.

Die Vorgabe eines korrekten Antworttexts veränderte das Ergebnis. Je nach Formulierung korrigierte sie 75 bis 95 % derselben Fehler. In zwei vorab registrierten Replikationen mit vier Modellen blieben die Korrekturraten bei Eingriffen ohne Antworttext unter einem Schwellenwert von 15 %. Die Ausnahme war ein grenzwertiges Ergebnis unter einer alternativen Kennzeichnungsmethode.

Anschließend ersetzte die Studie die bekannte richtige Antwort durch abgerufene Belege aus TriviaQA. Eine BM25-Suche wählte einen Satz aus den Belegdokumenten aus. Enthielt dieser Satz eine korrekte alternative Form der Antwort, korrigierte er 67 bis 76 % der hartnäckigen Fehler. Andernfalls korrigierte er 2 bis 12 % und verschlechterte gelegentlich zuvor richtige Antworten.

Dieser Befund bestätigt keine Regel für produktive Retrieval-Systeme. Eine Prüfung, die die richtige Antwort kannte, reduzierte in einem nachträglichen Test den Schaden. Eine ohne dieses Wissen einsetzbare Prüfung, die mit der eigenen Antwort des Modells verglich, korrigierte nur wenige Fehler. Die Forschenden testeten weder Dense Retrieval noch eine Prüfung durch ein Bewertungsmodell. Sie stellen das Vorhandensein der Antwort als Heuristik vor, die noch durchgängig evaluiert werden muss.

## Ein Messproblem für Entwickler

Die praktische Lehre stützt nicht die pauschale Behauptung, Modelle wüssten nichts. Entwickler sollten das gemessene Signal und den Eingriff benennen, der es verändert. Sprachlich ausgedrückte Sicherheit kann die Bereitschaft widerspiegeln, sich festzulegen. Sequenzwahrscheinlichkeit kann sprachliche Flüssigkeit abbilden. P(True) kann auf einen ausdrücklichen Widerspruch reagieren. Eine eingefrorene Aktivierungssonde kann die Antwort verfolgen, die ein bestimmtes Modell weiterhin gibt.

Evaluierungen müssen außerdem die Haltung eines Nutzers von den Informationen in seiner Nachricht trennen. Eine Antwort als falsch zu bezeichnen und die richtige Antwort vorzugeben sind unterschiedliche Eingriffe. Werden sie kombiniert, lässt sich nicht mehr erkennen, ob das Modell seine Antwort überdacht oder kopiert hat.

Am fiktiven Support-Arbeitsplatz ergänzt die Analystin einen Schritt, bevor sie das Ticket schließt. Sie ruft die Verordnung selbst ab und prüft, ob die relevante Passage eine mögliche Antwort enthält. Der Assistent ändert seine Antwort. Weder seine neue Sicherheit noch seine vorherige Zurückhaltung hält sie als Beweis fest. Den Fall veränderten Belege mit Inhalt, nicht eine nachdrücklicher vorgetragene zweite Bitte.

## Quellen

- Kadavath, S., Conerly, T., Askell, A., et al. (2022). *Language Models (Mostly) Know What They Know*. https://arxiv.org/abs/2207.05221
- Kumaran, D. (2026). *Reported Confidence in LLMs Tracks Commitment More Than Correctness*. https://arxiv.org/abs/2606.29490
- Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2024). *Are You Sure? Challenging LLMs Leads to Performance Drops in the FlipFlop Experiment*. https://arxiv.org/abs/2311.08596
- Tran, D.-V. (2026). *Not One Belief: Answer Payloads, Persistence, and Dissociated Confidence Signals in Conversational Question Answering*. https://arxiv.org/abs/2610.35694
- Zhang, C., Yang, R., Zhu, X., et al. (2026). *Confidence Estimation for LLMs in Multi-turn Interactions*. https://aclanthology.org/2026.findings-acl.1280/

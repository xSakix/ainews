+++
title = "Die Abkürzung in der Theory of Mind eines Modells"
slug = "abkuerzung-in-theory-of-mind-eines-modells"
description = "Sprachmodelle schienen Überzeugungen in Überzeugungen verfolgen zu können. HopToM zeigt, dass viele Benchmark-Fragen eine flachere Antwort erlauben, und bietet einen günstigeren Weg zum Schlussfolgern über die ganze Kette."
tags = ["research", "agents"]
date = 2026-10-15T04:05:30+02:00
draft = false
+++

Ein Operationsraum nach einer Übergabe. Ana hat den Schlüssel in die blaue Schublade gelegt. Boris sah sie. Cara sah Boris vor dem Umlegen gehen, während David nur hörte, wie Cara beschrieb, was Boris ihrer Ansicht nach wusste. Nun muss ein Assistent eine enge Frage beantworten: Wo denkt David, dass Cara glaubt, Boris werde suchen?

Ana, Boris, Cara und David sind erfunden. Die Verwirrung ist es nicht. Agenten, die verhandeln, lehren, koordinieren oder für Menschen handeln, müssen die Welt von der Sicht jeder Person darauf trennen. Ein neuer Preprint argumentiert, die Tests dieser Fähigkeit hätten das Rätsel häufig einfacher gemacht, als ihre Labels nahelegen.

## Eine Frage vierter Ordnung mit einem Ausweg zweiter Ordnung

Theory of Mind ist die Fähigkeit, über Wissen, Absichten oder Überzeugungen anderer Personen nachzudenken. Ihre höherstufige Form verschachtelt diese Perspektiven: Alice glaubt, dass Bob denkt, Carol wisse etwas. Forschende haben solche Geschichten genutzt, um zu fragen, ob Sprachmodelle mehrere Gedankenwelten gleichzeitig verfolgen können.

Die neue Studie, *Beyond Belief Nesting*, beginnt mit einer technisch klingenden Unterscheidung, die das Ergebnis verändert. Die Zahl von Namen oder Überzeugungsverben in einer Frage entspricht nicht unbedingt der Menge verschachtelten Schlussfolgerns, die eine Antwort verlangt. Eine nominell vierte Ordnung betreffende Frage kann von Belegen abhängen, die nur zwei Perspektiven trennen. Das Modell kann den Rest der Kette ignorieren und trotzdem Punkte erhalten.

Shanshan You und Kollegen nennen dies Ordnungsinflation. Sie definieren effektive Ordnung anhand der Zahl unterschiedlicher Ereignisse, die aufeinanderfolgende Überzeugungspräfixe stützen müssen. Ein Test erreicht nur dann volle Ordnung, wenn jede Frageebene von Belegen abhängt, die eine flachere Lösung ausschließen.

Diese Korrektur zählt, weil frühere Benchmarks eine attraktive Entwicklung etablierten. HI-TOM, 2023 veröffentlicht, erzeugte Geschichten mit zunehmend verschachtelten Überzeugungen und fand sinkende Modellleistung mit steigender Ordnung. Neuere Methoden verbesserten dann Ergebnisse durch explizite Perspektiven. RecToM transformiert eine Geschichte rekursiv durch den Blickwinkel jeder Figur und meldete perfekte Genauigkeit auf HI-TOM mit GPT-5.4 und Qwen3.5. Der Wert wirkte wie Fortschritt bei tiefem sozialem Schlussfolgern.

HopToM fragt, ob der Test selbst weiterhin eine Abkürzung erlaubte.

## Der Absturz nach dem Entfernen der Abkürzungen

Die Forschenden bauten zertifizierte Fragen voller Ordnung und paarten sie mit Kontrollen für Alternativen niedrigerer Ordnung. Unter direktem Prompting sank die mittlere Genauigkeit über vier Spitzenmodelle von 73,5 % erster Ordnung auf 20,0 % vierter Ordnung. Auch menschliche Teilnehmer fanden die tieferen Fragen schwierig.

Der Rückgang allein beweist nicht, dass Modellen Theory of Mind fehlt. Er zeigt, dass Erfolg auf einfacheren Benchmark-Konstruktionen die stärkere Aussage nicht etablieren kann. Ein Modell kann richtig antworten, weil die Geschichte einen Hinweis nahe der gefragten Tatsache enthält, weil die Perspektive einer Person nie von der Realität abweicht oder weil Zwischenüberzeugungen die Antwort nicht beeinflussen.

Das Team griff dann in die Belege der Geschichten ein. Ein wiederkehrendes Fehlermuster folgte Unterstützung für flachere Überzeugungspräfixe: Modelle antworteten, als hätten sie bei der Perspektive einer früheren Person aufgehört. Das verbindet die Fehler mit der Struktur des Reasoning-Problems statt nur mit längeren Prompts oder mehr Namen.

Der Befund passt auch zu einem breiteren Wandel der Theory-of-Mind-Evaluierung. OmniToM akzeptiert eine endgültige Antwort nicht als vollständigen Test. Es verlangt von Modellen, explizite Überzeugungsaussagen zu extrahieren und ihre Ordnung, ihren Wahrheitsstatus, Wissenszugang und mentale Quelle zu kennzeichnen. Über 895 Geschichten und 22.343 gelabelte Aussagen fanden die Autoren einen Engpass bei der Umwandlung erzählter Fakten in akteursspezifische Überzeugungen. Ein Modell kann jedes Ereignis kennen und dennoch eines dem falschen Geist zuordnen.

## Die Perspektiven einmal aufschreiben

HopToM tut mehr, als einen Wert zu senken. Die Arbeit führt HopTrace ein, ein Inferenzzeitverfahren, das jede Interaktion einmal in eine Perspektivaufzeichnung umwandelt. Ein deterministischer Löser folgt diesen Aufzeichnungen dann durch eine verschachtelte Anfrage.

Der Ansatz vermeidet, das Modell wiederholt die gesamte Kette rekonstruieren zu lassen. Auf den zertifizierten narrativen Benchmark-Fragen verbesserte HopTrace Genauigkeit vierter Ordnung um 22,0 Prozentpunkte und fünfter Ordnung um 38,5 Punkte gegenüber starken Prompting-Basen. Es nutzte 20 bis 39-mal weniger Token als Methoden mit mehreren Aufrufen.

Die Kombination ist ungewöhnlich. Reasoning-Hilfen tauschen häufig Kosten gegen Genauigkeit, indem sie mehr Antworten sampeln, mehrere Agenten fragen oder längere Gedankenketten erzeugen. HopTrace gibt dem Modell stattdessen eine Repräsentation ähnlich einer Auditspur: Wer beobachtete welches Ereignis, was konnte jeder Teilnehmer ableiten und welche Perspektive muss der nächste Schritt übernehmen?

Das entscheidet nicht, ob das Modell Gedanken im menschlichen Sinne versteht. Es verändert die technische Frage. Ein Agent braucht möglicherweise keine allgemeine Fähigkeit namens Theory of Mind, wenn sein Framework explizite, untersuchbare Perspektivaufzeichnungen pflegen kann. Die Aufzeichnungen können auch zeigen, wo die Kette brach, was eine korrekte Endantwort nicht kann.

## Was der Benchmark nun verlangt

Aufgaben mit Überzeugungen höherer Ordnung liegen nahe praktischen Fehlern von Multiagentensystemen. Ein Assistent, der eine Besprechung plant, muss das Wissen des Organisators von dem trennen, was jeder Teilnehmer erhalten hat. Ein Supportagent muss eine Kundenbehauptung von einer internen Notiz und der Zusammenfassung eines anderen Agenten trennen. Ein Verhandlungsagent muss unvollständige, veraltete oder bewusst asymmetrische Überzeugungen verfolgen.

In jedem Fall kann oberflächliche Übereinstimmung einen gefährlichen Fehler verbergen. Mehrere Agenten können im Mittel genaue Antworten liefern und denselben blinden Fleck teilen. Ein weiterer Preprint dieser Woche, *Smart Alone, Blind Together*, argumentiert, korrelierte Fehler entschieden, ob ein Theory-of-Mind-Modul für ein Team sicher sei. Genauigkeit allein kann Koordination nicht zertifizieren, wenn jeder Teilnehmer an derselben Perspektivgrenze scheitert.

HopToM verändert daher, was ein überzeugendes Ergebnis enthalten sollte. Die Frage muss jede beanspruchte Reasoning-Ordnung erzwingen. Die Evaluierung sollte Zwischenperspektiven offenlegen. Vergleiche sollten Token-Kosten einschließen, weil eine Methode mit Dutzenden Modellaufrufen innerhalb eines arbeitenden Agenten unbrauchbar sein kann. Auch menschliche Schwierigkeit sollte sichtbar bleiben: Überzeugungen vierter und fünfter Ordnung sind schwere kognitive Arbeit, keine routinemäßige Sprachübung.

Die Arbeit ist ein Preprint. Ihre Ergebnisse benötigen Replikation über mehr Modelle, Konfigurationen und natürliche Interaktionen. Zertifizierte synthetische Fragen können einen Mechanismus isolieren, doch reale Gespräche enthalten Mehrdeutigkeit, Täuschung und fehlende Belege, die eine erzeugte Geschichte wegkontrollieren kann.

Zurück zum vorgestellten Operationsraum. Ein leistungsfähiger Assistent sollte nicht raten, welche Schublade eine Figur nennt, weil der letzte Satz blau erwähnt. Er sollte den Blick von jedem Stuhl bewahren und zeigen, wie die Antwort von einem Geist zum nächsten gelangte. Der neue Benchmark lässt jeden dieser Übergänge zählen.

## Quellen

- Bawatneh, A., Sapkota, S., Bedi, A. S., Karmaker, S., & Shah, M. (2026). *OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling*. https://arxiv.org/abs/2605.26322
- Beaumaster, S., & Schrater, P. (2026). *Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams*. https://arxiv.org/abs/2610.19051
- He, Y., Wu, Y., Jia, Y., Mihalcea, R., Chen, Y., & Deng, N. (2023). *HI-TOM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models*. https://arxiv.org/abs/2310.16755
- Lei, C., Hu, G., Yang, M., Jiang, Y., & Lipovetzky, N. (2026). *Mind the Perspective: Let's Reason Recursively for Theory of Mind*. https://arxiv.org/abs/2606.11724
- You, S., Wang, Z., Liu, H., Liu, Y., He, Y., Hao, X., & Wang, L. (2026). *Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models*. https://arxiv.org/abs/2610.17777

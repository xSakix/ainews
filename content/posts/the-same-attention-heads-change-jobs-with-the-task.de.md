+++
title = "Dieselben Aufmerksamkeitsköpfe wechseln mit der Aufgabe ihre Rollen"
slug = "aufmerksamkeitskoepfe-wechseln-mit-aufgabe-ihre-rollen"
description = "Ein neuer Preprint findet, dass ein Sprachmodell den Einfluss seiner Aufmerksamkeitsköpfe neu organisiert, wenn sich die verlangte Aufgabe ändert, selbst bei unveränderten Fakten im Prompt. Kausale Eingriffe legen nahe, dass der Aufgabenkontext mitbestimmt, was eine Komponente tut, und erschweren ihre dauerhafte Benennung."
tags = ["research", "models"]
date = 2026-10-13T04:05:13+02:00
draft = false
+++

Ein Ingenieur sitzt vor einem Monitor und verfolgt Linien zwischen Hunderten kleiner Kästchen. Ein Kästchen erhält ein klares Etikett: „Land nachschlagen“. Dann ändert sich die Anweisung, die Eingabefakten bleiben gleich, und dasselbe Kästchen scheint bei etwas anderem zu helfen. Dieser Ingenieur ist erfunden, eine Illustration des praktischen Problems im Zentrum einer neuen Studie: Eine Transformer-Komponente hat möglicherweise keine einzelne stabile Aufgabe, die sich benennen lässt.

## Eine Karte, die sich mit der Frage verändert

Sovesh Mohapatra und Dani S. Bassett, Forschende mit Verbindungen zur University of Pennsylvania und Yale University, testeten, wie der Aufgabenkontext die funktionale Organisation von Aufmerksamkeitsköpfen in Sprachmodellen verändert. Ihr am 12. Oktober 2026 eingereichter Preprint untersucht fünf offene Modelle mit 1,5 Milliarden bis 14 Milliarden Parametern. Er hat kein Peer-Review durchlaufen.

Die Studie beginnt mit einer bewussten Trennung. Ein Prompt enthält einen kleinen Graphen, der als Tatsachenaussagen kodiert ist, während eine Anweisung das Modell auffordert, eine von mehreren Fragen zu diesem Graphen zu beantworten. Über die Bedingungen hinweg bleiben die Graphenfakten gleich. Nur die Aufgabe ändert sich. Dieser Entwurf erlaubt den Forschenden zu fragen, ob das Modell über identische Information denselben internen Weg nimmt oder den Weg entsprechend der verlangten Tätigkeit neu organisiert.

Sie behandeln jeden Aufmerksamkeitskopf als Knoten in einem Einflussnetzwerk. Eine Kante erfasst, wie die Änderung der Ausgabe eines Kopfes einen anderen Kopf später im Modell beeinflusst. Die entstehende Karte ist funktional statt anatomisch: Die Architektur bleibt unverändert, aber das gemessene Einflussmuster kann sich von Aufgabe zu Aufgabe unterscheiden.

Das tut es. Mohapatra und Bassett berichten, die Netzwerke trennten sich über die getesteten Modelle hinweg nach Aufgabe. Köpfe, die in einer Aufgabe einflussreiche Positionen einnehmen, können in einer anderen weniger zentral werden. Der Befund verschiebt die Interpretierbarkeitsfrage von „Was repräsentiert dieser Kopf?“ zu „Welche Rolle spielt dieser Kopf bei dieser Aufgabe innerhalb dieses Netzwerks?“

Diese Unterscheidung ist wichtig, weil ein großer Teil der mechanistischen Interpretierbarkeit nach wiederverwendbaren internen Teilen gesucht hat. Eric Todd und Kollegen identifizierten zuvor kleine Gruppen von Aufmerksamkeitsköpfen, die kompakte, aus In-Context-Beispielen extrahierte „Funktionsvektoren“ tragen. Roee Hendel, Mor Geva und Amir Globerson zeigten ebenfalls, dass In-Context-Lernen einen Aufgabenvektor bilden kann, der ein Modell eine demonstrierte Operation auch ohne die Demonstrationen zur Inferenzzeit ausführen lässt. Diese Ergebnisse stützen die Idee, dass eine Aufgabe eine kausale interne Repräsentation haben kann. Die neue Arbeit fragt, wie eine solche Repräsentation die Beziehungen zwischen Komponenten verändert.

## Die Anweisung kann die Mechanik verschieben

Eine bloße Korrelation ließe einen offensichtlichen Zweifel bestehen. Eine andere Aufgabe erzeugt eine andere Antwort; eine andere Einflusskarte könnte die Veränderung daher nur begleiten. Die Autoren greifen deshalb in die Aktivierungen des Modells ein.

Sie konstruieren eine Aktivierungsänderung in einer frühen Schicht, die das Modell von der Repräsentation einer Aufgabe zu einer anderen bewegen soll, während der geschriebene Prompt unverändert bleibt. In Experimenten mit Gemma- und Qwen-Modellen kann dieser Eingriff wechseln, welche Aufgabe das Modell ausführt. Die Arbeit berichtet, jeder der 512 Prompts, bei denen beide Aufgaben entgegengesetzte Antworten verlangten, sei zur Zielantwort gewechselt, während alle 512 Prompts, bei denen beide Aufgaben dieselbe Antwort verlangten, diese Antwort beibehielten.

Der Eingriff lässt auch die spätere Einflusskarte der Zielaufgabe ähneln. Die Autoren messen dies anhand eines Fehlers zwischen Netzwerkreaktionsmustern. Ihre Aufgabenwechseländerung verringerte diesen Fehler um 53,6 % bei Gemma und um 5 % bei Qwen. Der Größenunterschied warnt davor, den Mechanismus über Modellfamilien hinweg als einheitlich zu behandeln. Beide Fälle weisen aber in dieselbe kausale Richtung: Eine Änderung des internen Aufgabenkontexts kann spätere Berechnungen umlenken.

Das ähnelt Aktivierungssteuerung, einer breiteren Familie von Methoden, die Modellverhalten durch das Hinzufügen einer Richtung zu verborgenen Aktivierungen verändert. Alexander Matt Turner und Kollegen zeigten, dass aus kontrastierenden Prompts abgeleitete Aktivierungsergänzungen übergeordnete Eigenschaften erzeugten Texts ohne weiteres Training verändern konnten. Die neue Studie nutzt eine Aktivierungsänderung als experimentelle Sonde. Ihr Ziel ist nicht, eine Verhaltenssteuerung auszuliefern, sondern zu testen, ob eine Änderung der Aufgabenrepräsentation einer Änderung im Einflussnetzwerk der Aufmerksamkeitsköpfe vorausgeht.

Der Eingriff ist eng begrenzt. Er zeigt nicht, dass Forschende jede beliebige Aufgabe wählen, jedes Modell zuverlässig bearbeiten oder ein vollständiges Programm aus einem Kopfgraphen lesen können. Die Aufgaben sind kontrolliert, die Modelle Systeme mit offenen Gewichten von moderater Größe, und die kausalen Tests konzentrieren sich auf einen bestimmten internen Kontrast. Die stärkste Aussage der Arbeit betrifft Kontextabhängigkeit innerhalb dieses Rahmens.

## Von benannten Teilen zu eingesetzten Teams

Die Netzwerkneurowissenschaft liefert die ordnende Metapher der Autoren. In diesem Feld wird der Beitrag einer Hirnregion oft über ihre Position in einem veränderlichen Netzwerk statt über eine einzelne isolierte Funktion untersucht. Bassett und Olaf Sporns beschrieben den Ansatz als Versuch, Elemente über Skalen hinweg zu verbinden und zu erklären, wie Wechselwirkungen Verhalten hervorbringen. Mohapatra und Bassett übertragen diese Perspektive auf die Transformer-Analyse.

Die Analogie hat Grenzen. Ein Aufmerksamkeitskopf ist eine entworfene mathematische Komponente, keine biologische Region, und ein Transformer erbt weder Anatomie noch Geschichte des Gehirns. Die nützliche Übertragung ist methodisch: Ein Teil wird zusammen mit dem Einflussmuster beobachtet, das es einbindet.

Für Menschen, die Modelle prüfen, macht dies eine dauerhafte Bezeichnung weniger beruhigend. Ein Kopf, der unter einem Prompt ein Verhalten unterstützt, kann anders mitwirken, wenn sich Anweisungen, Beispiele oder Ziele ändern. Diesen Kopf zu entfernen oder zu unterdrücken könnte Effekte haben, die vom Aufgabenkontext abhängen. Umgekehrt kann ein sicherheitsrelevanter Prozess über unterschiedliche Konfigurationen verteilt sein, selbst wenn die zugrunde liegenden Parameter identisch sind.

Das Ergebnis legt auch einen praktischen Maßstab für künftige Interpretierbarkeitsaussagen nahe. Ein vorgeschlagener Schaltkreis sollte über Aufgaben hinweg getestet werden, die dieselbe Information wiederverwenden, und eine scheinbare Rolle sollte kausale Eingriffe statt bloßer visueller Prüfung überstehen. Wenn sich der Schaltkreis verändert, ist die Veränderung Teil des zu erklärenden Mechanismus.

Es bleibt weitere Arbeit. Die Studie untersucht eine begrenzte Familie graphenbasierter Aufgaben und eine kleine Gruppe offener Modelle. Sie stellt nicht fest, wie sich diese Reaktionsnetzwerke in sehr großen proprietären Systemen, während langer Gespräche oder unter verrauschten Anweisungen aus der realen Welt verhalten. Sie klärt auch nicht, ob das gemessene Netzwerk sämtliche für eine Antwort relevante Berechnung erfasst. Die Autoren präsentieren ein Framework zur Untersuchung von Neukonfiguration, keinen fertigen Atlas.

Zurück zum vorgestellten Ingenieur am Monitor. Das Etikett am Kästchen ist noch nützlich, braucht nun aber eine Bedingung daneben: nützlich für diese Operation, unter dieser Anweisung, in dieser Gesellschaft anderer Köpfe. Das beständige Objekt ist nicht mehr das isolierte Teil. Es ist das Muster, das die Aufgabe in Dienst nimmt.

## Quellen

- Bassett, D. S., & Sporns, O. (2017). *Network neuroscience*. https://doi.org/10.1038/nn.4502
- Hendel, R., Geva, M., & Globerson, A. (2023). *In-Context Learning Creates Task Vectors*. https://aclanthology.org/2023.findings-emnlp.624/
- Mohapatra, S., & Bassett, D. S. (2026). *Task Context Dynamically Reconfigures Attention Head Networks in Large Language Models*. https://arxiv.org/abs/2610.13895
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://openreview.net/forum?id=AwyxtyMwaG
- Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2024). *Activation Addition: Steering Language Models Without Optimization*. https://arxiv.org/abs/2308.10248

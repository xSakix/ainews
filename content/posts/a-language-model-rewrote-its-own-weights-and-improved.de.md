+++
title = "Sprachmodell schreibt eigene Gewichte um und verbessert sich"
slug = "sprachmodell-schreibt-eigene-gewichte-um-und-verbessert-sich"
description = "Forscher gaben einem offenen 27B-Modell Zugang zu seinen Gewichten, zu bewerteten Antworten und zu einer Möglichkeit, Änderungen zu testen, während Gradienten und Optimierer blockiert blieben. Das Modell steigerte seine Genauigkeit bei zurückgehaltenen Aufgaben um 6,6 Punkte und reparierte eine beschädigte Kopie seiner selbst, doch kleinere Modelle scheiterten unter denselben Bedingungen."
tags = ["models", "research"]
date = 2026-11-21T04:12:00+01:00
draft = false
+++

Ein Modell saß vor einer Python-Sitzung, in der seine eigenen Gewichte offenlagen. Es konnte verborgene Zustände prüfen, ausgewählte Matrizen verändern und eine Kopie seiner selbst auffordern, eine weitere Aufgabe zu lösen. Einen Gradienten konnte es nicht berechnen. Zwanzig Vorwärtsdurchläufe und ein festes Zeitlimit waren alles, was es hatte.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

Jiajun Fan und zehn Mitautoren stellten vier offenen Modellen aus einer Modellfamilie diese Umgebung zur Verfügung. Das 2B-Modell (zwei Milliarden Parameter) nahm keine Änderungen an sich selbst vor. Die 4B- und 9B-Modelle probierten zufällige Änderungen aus und verschlechterten sich. Das 27B-Modell maß, wo sich seine verborgenen Zustände unterschieden, nahm Änderungen entlang dieser Richtungen vor und behielt Anpassungen nur dann bei, wenn gepaarte Tests sie stützten. Eine einzelne Änderung steigerte seine Genauigkeit bei 490 zurückgehaltenen Aufgaben um 6,6 Prozentpunkte.

Die Studie bezeichnet die Methode als „Self-Rewriting“ (Selbstumschreibung). Ihre zentrale Behauptung ist eng gefasst und folgenreich: Ein eingesetztes Modell kann seine eigenen Gewichte dauerhaft verbessern, allein durch Schlussfolgern in Vorwärtsdurchläufen. Bei der Arbeit handelt es sich um einen Preprint (Vorabveröffentlichung), und die Autoren erklären, es sei der erste Nachweis dieser Art.

## Ein Modell mit Zugang zu sich selbst

Beim Training sind das System, das nach besseren Gewichten sucht, und das Modell, das sie später nutzt, normalerweise voneinander getrennt. Ein Optimierer berechnet Gradienten anhand einer Verlustfunktion, Ingenieure wählen Daten und Einstellungen aus, und ein Cluster schreibt das Ergebnis in einen neuen Checkpoint. Die Inferenz beginnt erst, nachdem dieser Prozess abgeschlossen ist.

Fan und seine Kollegen entfernten den Optimierer, gaben dem Modell jedoch Werkzeuge an die Hand. Es erhielt bewertete Antworten zu Übungsaufgaben, Zugriff auf seine Gewichtstensoren und eine Python-Sitzung, deren Zustand über mehrere Schritte hinweg erhalten blieb. Es konnte das unveränderte und das bearbeitete Modell mit denselben Zufallsstartwerten (Seeds) auf denselben Aufgaben ausführen. Außerdem konnte es die verborgenen Zustände auslesen, die das Modell bei selbst gewählten Texten erzeugte.

Die Umgebung setzte diese Grenze durch. Gradienten waren deaktiviert. Aufrufe von Optimierern, Netzwerkzugriffe, neue Prozesse und Funktionen zum Laden von Modellen wurden abgelehnt. Das Modell konnte weder das Eingabe-Embedding noch die abschließende Normalisierung oder die Ausgabeschicht verändern. Pro Sitzung standen ihm höchstens 20 Vorwärtsdurchläufe und 200 Code-Ausführungen zur Verfügung.

Ein gepaarter Test verglich die Antworten Aufgabe für Aufgabe. Das war entscheidend, weil ein kleiner Zugewinn im Gesamtergebnis sonst durch Sampling-Rauschen hätte entstehen können. Das Framework meldete, wie viele Antworten von falsch auf richtig wechselten, wie viele sich in die umgekehrte Richtung veränderten und wie oft eine der beiden Versionen ihr Budget von 16.384 Token ausschöpfte.

Im strengeren Protokoll testete das Framework eine vorgeschlagene Änderung zusätzlich einmalig an reservierten Übungsaufgaben, die das Modell nicht einsehen konnte. Danach reichte das Modell die Änderung ein oder zog sie zurück. In fünf der ersten acht Sitzungen zog es seinen Vorschlag zurück. Die angenommenen Änderungen senkten die Genauigkeit des weiterhin eingesetzten Modells in keinem Fall.

## Was das größte Modell veränderte

Das 27B-Modell durchsuchte nicht jeden einzelnen Parameter. Es ermittelte Richtungen in seinen verborgenen Zuständen, die mit Fehlern zusammenhingen, und schwächte ab, wie ausgewählte Ausgabematrizen entlang dieser Richtungen schrieben. Der Eingriff ähnelte dem Subtrahieren einer Rang-eins-Komponente von einer Matrix.

Dieser Eingriff verringerte ein offensichtliches Fehlerbild: Einige Antworten wiederholten einen Satz so lange, bis das Token-Limit ausgeschöpft war. Bei einer zurückgehaltenen Beispielaufgabe wiederholte das Basismodell denselben Satz 549-mal und gab nie eine Antwort. Die bearbeitete Version schloss die Aufgabe ab.

In der fest vorgegebenen Evaluierung brachte die erfolgreichste Änderung den Zugewinn von 6,6 Punkten. Zwei Sitzungen in der Abfolge erzielten Verbesserungen, deren Wahrscheinlichkeit im gepaarten Test nach dem Verfahren der Autoren unter eins zu 100.000 lag. Nach der achten Sitzung erreichte die Genauigkeit 63,8 %.

Jede Sitzung begann ihre Untersuchung ausgehend von den Basisgewichten, doch eine angenommene Änderung ersetzte das jeweils eingesetzte Modell. In der Abfolge summierten sich daher Entscheidungen auf, statt dass jede vorgeschlagene Änderung blind übereinandergestapelt wurde. Die Autoren berichten, die Genauigkeit sei über alle acht Sitzungen hinweg gestiegen oder auf gleichem Niveau geblieben.

Die Verbesserung erforderte keinen zusätzlichen Rechenaufwand bei jeder späteren Antwort. Einmal geschrieben, blieb die Änderung im Checkpoint gespeichert. Das unterscheidet den Ansatz vom Test-Time-Scaling (Skalierung zur Testzeit), bei dem eine bessere Antwort jedes Mal durch mehr Token oder zusätzliche Durchläufe erkauft wird.

## Reparatur ohne Original

Das Team konstruierte zudem einen Fehler mit bekannter Ursache. Es überschrieb acht aufeinanderfolgende Zeilen in einer Ausgabematrix eines mehrschichtigen Perzeptrons mit Rauschen, das auf das 200-Fache der Standardabweichung dieser Matrix skaliert war. Das beschädigte Modell löste fast nichts mehr.

Das bearbeitende Modell selbst war unbeschädigt, konnte aber nur die Durchläufe und Gewichte der beschädigten Kopie prüfen. Ihm wurde mitgeteilt, dass einige Werte fehlerhaft seien, nicht aber, wo der Schaden lag oder wie er entstanden war. Es las nie die entsprechenden intakten Werte aus.

Das 27B-Modell spürte die fehlerhafte Matrix auf und schrieb eigene Ersatzwerte hinein. Eine Reparatur, die es anhand von Textaufgaben aus der Mathematik fand, übertrug sich auf sechs Bild-Benchmarks (Vergleichstests), die in der Sitzung nie vorgekommen waren. Die reparierte Kopie stellte 83 % der zusammengefassten Genauigkeit des Basismodells wieder her. Bei ScreenSpot-v2 stieg sie von null auf 89 %, verglichen mit 93 % beim unbeschädigten Modell.

Dieser Test beugt einer naheliegenden Deutung des Hauptergebnisses vor. Ein Modell könnte eine eng begrenzte Änderung vornehmen, die Eigenheiten der Übungsaufgaben ausnutzt. Dass es eine gezielt beschädigte Komponente repariert und die Leistung bei Bildern zurückgewinnt, zeigt, dass das Modell eine allgemeinere Funktion erkennen und teilweise wiederherstellen kann.

Damit ist nicht gezeigt, dass ein Modell beliebige Schäden beheben kann. Die Störung betraf einen einzelnen konstruierten Block, und die Experimente nutzten eine einzige Modellfamilie, Qwen3.5, in vier Größen. Das Modell verfügte über bewertete Übungsantworten und einen ungewöhnlich direkten Zugriff auf interne Tensoren. Übliche als Dienst bereitgestellte Assistenten besitzen keines dieser Privilegien.

## Die Grenze der Modellgröße

Die kleineren Modelle zeigen die derzeitige Grenze auf. Das 2B-Modell behandelte seine Gewichte nicht als etwas, das es sinnvoll verändern könnte. Die 4B- und 9B-Versionen fügten zufälliges Rauschen hinzu. Wenn ein Test Schaden anzeigte, versuchten sie aufs Geratewohl einen anderen Eingriff.

Das 27B-Modell bewältigte eine längere Kette von Schritten: Es diagnostizierte ein Symptom, prüfte Aktivierungen, stellte eine Hypothese auf, veränderte eine Matrix, führte einen gepaarten Test durch und passte seinen Plan an, wenn das Ergebnis negativ ausfiel. Die Autoren beschreiben dies als eine Fähigkeit, die mit zunehmender Größe entsteht, doch mit vier Größen aus einer einzigen Modellfamilie lässt sich keine allgemeine Schwelle bestimmen.

Ein begleitender Preprint, der in derselben Woche erschien, untersuchte eine andere Anordnung: Ein externes Sprachmodell wählte Änderungen an den Gewichten für kleinere Zielmodelle aus. Dieses System erreichte bei SmolLM2 und Qwen2.5 das Niveau einer Black-Box-Suche und übertraf sie bei Pythia. Fans Arbeit vereint den Bearbeiter und das bearbeitete Objekt in einem einzigen Modell – genau dieses Merkmal stützt ihre weiterreichende Behauptung.

Die Autoren verknüpfen das Ergebnis mit rekursiver Selbstverbesserung. Von einem autonomen Kreislauf ist ihr Experiment jedoch weit entfernt. Menschen lieferten die Aufgabe, das Fehlersignal, die Werkzeuge, die Beschränkungen für Eingriffe und den Abnahmetest. Die Sitzungen dauerten Stunden auf einer GPU, und die stärksten Belege betreffen einen begrenzten Satz von Reasoning-Aufgaben sowie einen einzelnen künstlich erzeugten Fehler.

Genau diese Grenzen machen das Ergebnis aber auch überprüfbar. Jede angenommene Änderung bestand einen gepaarten Vergleich, jede zurückgehaltene Aufgabe blieb außerhalb der Bearbeitungssitzung, und jeder kleinere Fehlschlag blieb dokumentiert.

Zurück an der Python-Eingabeaufforderung nutzte das Modell seinen letzten Vorwärtsdurchlauf und hinterließ eine Änderung auf der Festplatte. Die nächste Antwort brauchte keinen längeren Prompt und keinen zusätzlichen Durchlauf. Wenige veränderte Matrizen machten den Unterschied aus.

## Quellen

- Fan, J., He, N., Yang, C., Mao, A., Zhu, X., Cheng, C., Liang, K., Shen, S., Li, Z., Guo, R., & Liu, G. (2026). *Language Models Can Rewrite Their Own Weights*. https://arxiv.org/abs/2611.21885
- Yang, C., et al. (2026). *Can an LLM Fix a Language Model Without Training It?* https://arxiv.org/abs/2611.25613

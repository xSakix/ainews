+++
title = "Feinabstimmung kann Wissen verbergen, ohne es zu löschen"
slug = "feinabstimmung-kann-wissen-verbergen-ohne-es-zu-loeschen"
description = "Ein Preprint trennt den umkehrbaren Verlust des Zugriffs von der langsameren Zerstörung gespeicherter Fakten. Diese Unterscheidung könnte die Diagnose von Fehlern beim fortlaufenden Lernen verändern."
tags = ["research", "models"]
date = 2026-10-11T04:04:06+02:00
draft = false
+++

Wissen, das während der Feinabstimmung verschwindet, kann im Inneren eines Sprachmodells erhalten bleiben und später wieder auftauchen, berichtet eine neue mechanistische Studie.

Vedant Palit, Florent Draye, Nicolas Zucchet, Zhijing Jin und Bernhard Schölkopf untersuchten „scheinbares Vergessen“: einen Rückgang beim Abrufen, der wie gelöschtes Wissen aussieht, tatsächlich aber einen vorübergehend gestörten Zugriff widerspiegelt. Ihr Preprint verbindet einen minimalen Assoziativspeicher, einen kleinen Transformer und Eingriffe in ein vortrainiertes Sprachmodell.

## Warum das wichtig ist {#why-it-matters}

Wer ein Modell mit neuen Unternehmensdaten aktualisiert, kann einen Einbruch der Genauigkeit bei älteren Fakten beobachten und daraus schließen, das Update habe sie zerstört. Liegt der Fehler beim Zugriff, verschenkt erneutes Training oder die Rückkehr zu einem früheren Checkpoint noch vorhandene Informationen. Die hilfreiche Frage lautet dann nicht nur, wie stark die Leistung sank, sondern ob sich die alten Repräsentationen gemeinsam verschoben oder einzeln beschädigt wurden.

Die Autoren beobachteten beim Training mit neuen Fakten ein dreistufiges Muster. Der Abruf alter Fakten brach zunächst ein, erholte sich trotz fortgesetzten Trainings ausschließlich mit neuem Material und nahm dann erneut ab. Eine einzige Theorie dauerhafter Überschreibung kann die zwischenzeitliche Erholung nicht erklären.

Ihr minimaler Speicher reproduzierte diese Kurve mit drei Zutaten: alten Schlüsseln mit gemeinsamer Struktur, neuen Werten, die sich in einem Bereich konzentrierten, und Normalisierung im Netzwerk. Die Feinabstimmung verschob die alten Repräsentationen zunächst in eine gemeinsame Richtung. Das störte das Auslesen, bewahrte aber die relative Anordnung, die kodierte, welcher Fakt welcher war.

Sobald die neuen Fakten gelernt waren, nahm die Normalisierung einen großen Teil der gemeinsamen Verschiebung zurück, und alte Antworten wurden wieder zugänglich. Gleichzeitig sammelten sich kleinere, faktenspezifische Änderungen an. Diese veränderten die Beziehungen zwischen Erinnerungen und führten schließlich zu dauerhaftem Verlust.

## Eine Richtung trennt Verbergen von Erosion

Die Studie prüft den Mechanismus, statt bei der Kurve stehen zu bleiben. In einem mit synthetischen Daten trainierten Transformer beseitigte das Abziehen der gemeinsamen Verschiebung den vorübergehenden Einbruch. In einem vortrainierten Sprachmodell habe das Entfernen einer Richtung aus jedem Gewichtsupdate der Feinabstimmung alte Fakten wiederhergestellt, so die Autoren.

Dieser Eingriff verleiht der Erklärung mehr Gewicht als eine Beschreibung veränderter Benchmarkwerte. Er identifiziert eine niedrigdimensionale Komponente, die mit umkehrbarem Verlust verbunden ist, und grenzt sie von langsameren, verteilten Veränderungen ab, die einzelne Erinnerungen beschädigen.

Die Unterscheidung betrifft Modellzustände, nicht das menschliche Gedächtnis. „Verborgenes“ Wissen bedeutet hier, dass ein Evaluationsprompt die erwartete Antwort nicht mehr abruft, während die sie tragende Geometrie messbar bleibt. Daraus folgt nicht, dass das Modell sich bewusst erinnert oder den Fakt ohne Eingriff wiederherstellen kann.

Die Experimente verwenden außerdem bewusst kontrollierte Fakten und Trainingsbedingungen. Reale Feinabstimmung vermischt Formate, Ziele und überlappende Konzepte. Ein Produktionsmodell kann aus Gründen außerhalb dieses Mechanismus scheitern: unpassende Prompts, veränderte Dekodierung, Sicherheitstraining oder neue Antwortregeln. Eine gemeinsame Verschiebung der Repräsentationen zu erkennen, kann deshalb für sich allein nicht bestätigen, dass sich eine verlorene Fähigkeit wiederherstellen lässt.

### Die Studie stellte außerdem fest

Ob Vergessen überwiegend vorübergehend oder dauerhaft war, hing von den neuen Daten ab: Alte Erinnerungen, die sich gemeinsam bewegten, behielten ihre relative Geometrie, während Updates, die sie auseinanderbewegten, zerstörerische Erosion verursachten. Die Normalisierung half, die Erholung zu erklären, indem sie die gemeinsame Verschiebung nach Stabilisierung des neuen Lernens verringerte. Das Minimalmodell sagte qualitatives Verhalten voraus, das später in Transformer-Experimenten geprüft wurde.

Der Preprint wurde am 6. Oktober 2026 eingereicht und hat noch kein Peer-Review durchlaufen. Sein praktischer Wert ist eine diagnostische Hypothese: Bevor jeder Leistungsrückgang nach Feinabstimmung als gelöschtes Wissen gilt, sollte geprüft werden, ob die Repräsentationen eine entfernbare Richtung teilen und ob sie sich bei fortgesetztem Training erholen.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| Der Abruf alter Fakten brach ein, erholte sich beim fortgesetzten Training mit neuen Fakten und erodierte später | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.08718 | keine |
| Ein minimaler Assoziativspeicher reproduzierte das Muster mit gemeinsamen Schlüsseln, konzentrierten Werten und Normalisierung | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.08718 | keine |
| Die Feinabstimmung verschob alte Repräsentationen in eine gemeinsame Richtung und bewahrte ihre relative Geometrie | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.08718 | keine |
| Das Entfernen der gemeinsamen Richtung beseitigte den vorübergehenden Einbruch in einem kleinen Transformer | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.08718 | keine |
| Das Entfernen einer Richtung aus Gewichtsupdates stellte alte Fakten in einem vortrainierten Sprachmodell wieder her | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.08718 | keine |
| Die Arbeit wurde am 6. Oktober 2026 eingereicht | VERIFIZIERT | https://arxiv.org/abs/2610.08718 | keine |

+++
title = "Mit wachsendem Gedächtnis häufen sich falsche Erinnerungsanlässe"
slug = "mit-wachsendem-gedaechtnis-haeufen-sich-falsche-erinnerungen"
description = "Als ein Speicher von acht auf 2.048 Einträge wuchs, wurde eine feste Abrufschwelle fast nutzlos. Eine Studie erklärt die statistische Falle und testet eine Regel, die Fehlalarme ohne gekennzeichnete Trainingsdaten bei rund fünf Prozent hält."
tags = ["research", "agents"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

Eine fiktive Projektleiterin öffnet am Montagmorgen ihren Assistenten. Vor Monaten hat sie erwähnt, dass ein Lieferant lieber nach dem Mittagessen angerufen wird. Seither hat das System Tausende Details gespeichert: Besprechungen, Fristen, Namen, Einkäufe, abgesagte Reisen. Sie tippt einen Gruß. Der Assistent unterbricht sie mit dem alten Hinweis zum Lieferanten und erinnert sie anschließend an ein Restaurant aus dem Frühjahr. Beide Erinnerungen stimmen. Keine passt in diesen Moment.

## Wann ist eine Unterbrechung angebracht?

Langzeitgedächtnis wird meist als Suchaufgabe verstanden. Ein Nutzer fragt nach einem früheren Gespräch und das System findet eine passende Passage. Beim proaktiven Gedächtnis kommt eine schwierigere Entscheidung hinzu: In jeder Runde muss der Assistent prüfen, ob ein gespeichertes Detail wichtig genug ist, um es ungefragt anzusprechen.

Yichuan Chen und Xin Wang von der Zhejiang Sci-Tech University untersuchten, was passiert, wenn dieser Speicher wächst. Ihr Preprint *The Price of Scale in Proactive Memory Recall* behandelt jede Erinnerung als einen weiteren statistischen Test. Selbst wenn eine irrelevante Erinnerung eine Ähnlichkeitsschwelle nur selten überschreitet, ist es bei Tausenden Versuchen wahrscheinlich, dass wenigstens eine darüberliegt.

Der Effekt war erheblich. Eine Schwelle, die bei acht Erinnerungen auf fünf Prozent Fehlalarme kalibriert war, erzeugte bei 2.048 Erinnerungen je nach Einbettungsmodell und Hinweis 84 bis 100 Prozent Fehlalarme. Aus Zurückhaltung bei kleinem Speicher wurde fast ständiges Unterbrechen.

Das ist kein gewöhnliches Vergessen. Die Information bleibt gespeichert. Der Fehler liegt in der Entscheidung, wann sie zur Sprache kommen soll.

## Mehr Erinnerungen, mehr Lose

Angenommen, das System berechnet für jede irrelevante Erinnerung, wie ähnlich sie der jüngsten Nachricht des Nutzers ist. Übersteigt der höchste Wert eine feste Schwelle, meldet sich der Assistent. Bei acht irrelevanten Erinnerungen hat das Rauschen acht Chancen, wie ein bedeutsames Signal auszusehen. Bei 2.048 Erinnerungen sind es 2.048 Chancen.

Chen und Wang leiten daraus ab: Soll die gesamte Fehlalarmrate auf einem Zielwert bleiben, muss die zulässige Wahrscheinlichkeit eines falsch positiven Ergebnisses pro Erinnerung ungefähr umgekehrt proportional zur Speichergröße sinken. Für einen Gesamtzielwert von fünf Prozent entspricht die Toleranz pro Erinnerung näherungsweise dem negativen Logarithmus von 0,95, geteilt durch die Anzahl der Erinnerungen.

Die strengere Schwelle hat ihren Preis. Auch relevante Hinweise müssen sie überwinden. Das System rückt damit an den äußersten linken Rand seiner ROC-Kurve, die Treffer und Fehlalarme zueinander ins Verhältnis setzt. Die Fehlalarme werden seltener, aber die Treffer ebenfalls. Ein besseres Einbettungsmodell kann die Kurve verbessern, hebt die Vervielfachung der Tests aber nicht auf.

Die Autoren spielten Gesprächsfolgen aus LongMemEval nach. Der Benchmark umfasst 500 Fragen zum Abruf von Informationen, zum Schlussfolgern über mehrere Sitzungen und Zeitpunkte hinweg, zu Aktualisierungen und zum Verzicht auf eine Antwort. Außerdem verwendeten sie LoCoMo: Dessen lange Gespräche wurden aus Personenprofilen und Ereignisgraphen erzeugt und anschließend von Menschen auf Konsistenz überarbeitet. Ursprünglich prüfen diese Benchmarks, ob Systeme alte Informationen wiederfinden. Chen und Wang machten daraus chronologische Abläufe, in denen der Assistent entscheiden muss, ob er die Information gerade jetzt von sich aus anbieten soll.

Sie konstruierten implizite Hinweise, die weder nach einer Erinnerung fragten noch deren Antwort enthielten. In den Versuchen kamen lexikalische und semantische Bewertungen, mehrere Einbettungsmodelle und ein Cross-Encoder zur Neusortierung der Treffer zum Einsatz. Das Muster blieb bestehen. Auch eine aufwendigere Bewertung entging dem Skaleneffekt nicht.

## Eine Schwelle, die sich mit dem Nutzer verändert

Der vorgeschlagene Ausweg ist eine konforme Entscheidungsregel mit ausgetauschten Hinweisen. Sie vergleicht nicht nur die aktuelle Nachricht mit dem Speicher, sondern bewertet frühere Nachrichten desselben Nutzers als Referenzhinweise am gleichen Bestand. Entscheidend ist, ob die aktuelle Nachricht im Vergleich zu diesen gewöhnlichen Hinweisen auffallend stark auf eine Erinnerung verweist.

Damit ändert sich die Grundlage der Kalibrierung. Die Schwelle folgt dem Speicher und der Verteilung der Nutzernachrichten, statt beim Wachstum unverändert zu bleiben. Unter der Annahme statistischer Austauschbarkeit liefert der konforme Rang bereits für eine endliche Stichprobe eine Obergrenze für Fehlalarme, ohne gekennzeichnete Beispiele zu benötigen.

Auf LongMemEval hielt die Regel mit Hintergrundelementen aus dem ungefilterten Nutzerverlauf die Fehlalarme zwischen drei und sechs Prozent. Die Trefferquote entsprach der einer mit gekennzeichneten Beispielen optimierten Schwelle. In einer chronologischen Wiedergabe mit früheren Nachrichten des Nutzers als Referenz meldete sie sich bei sechs bis acht Prozent der Gesprächsanfänge. Bei 2.048 Erinnerungen griff eine praxisübliche Regel in 57 Prozent der Fälle ein.

Eine Entscheidung dauerte rund 50 Millisekunden auf einem CPU-Thread. Das veröffentlichte Repository enthält Entscheidungsregeln in NumPy, Tests, Versuchsskripte, Annotationen und Ergebnisse. Die Autoren verwendeten eine einzelne RTX 3090 und dokumentierten, wie sich die Benchmark-Abläufe reproduzieren lassen.

## Der verbleibende Zielkonflikt

Auch kalibriert ist proaktives Erinnern nicht einfach. Auf LoCoMo überschritt die konforme Regel je nach Herkunft der Referenzhinweise ihr Ziel oder wurde zu zurückhaltend. Ihre Garantie hängt von der Austauschbarkeit ab: Künftige Hinweise müssen sich ähnlich genug wie die Referenzhinweise verhalten, damit die Rangfolge aussagekräftig bleibt. Nutzer können ihre Gewohnheiten ändern. Eine sorgfältig zusammengestellte Referenzmenge kann vom tatsächlichen Nachrichtenverkehr abweichen.

Die Arbeit testet auch das prospektive Gedächtnis: Ein Assistent soll handeln, sobald eine künftige Bedingung eintritt. TriggerBench hatte bereits gezeigt, dass dies schwerer ist als die direkte Frage nach einer Erinnerung. Mit wachsendem Kontext sinkt die Leistung, und Modelle können in eine Strategie des ständigen Erinnerns verfallen. Als Chen und Wang die Fehlalarmrate begrenzten, riefen die ähnlichkeitbasierten Regeln auf dem Benchmark für prospektives Gedächtnis höchstens neun Prozent der hinterlegten Bedingungen ab.

Die Beurteilung von Fehlalarmen unterstrich die Nachteile unpassender Erinnerungen. Ein Mensch und zwei Sprachmodelle untersuchten die Fehlalarme. Die meisten verbesserten die Antwort nicht. In einer früheren Fassung der Studie entsprach die Übereinstimmung dreier Beurteiler einem Fleiss-Kappa von 0,63. Rund neun von zehn Fehlalarmen galten als tatsächliche Unterbrechungen. Eine abgerufene Tatsache kann stimmen und das Gespräch dennoch verschlechtern.

Die Studie ist ein 14-seitiger Preprint und wurde noch nicht von Fachkollegen begutachtet. Die Gesprächsfolgen stammen aus Benchmarks, nicht aus jahrelanger natürlicher Nutzung durch Millionen Menschen. Die neue Regel muss deshalb noch bei wechselnden Gewohnheiten, gemischten Sprachen und Speichern mit korrelierten statt unabhängigen Erinnerungen getestet werden. Das Argument zu den vielen Tests hängt jedoch nicht von einem bestimmten Produkt ab. Es betrifft jedes System, das aus vielen verrauschten Werten den höchsten auswählt.

Zurück zur fiktiven Projektleiterin, einige Tage später. Ihr Assistent kennt noch immer die Vorliebe des Lieferanten und das Restaurant aus dem Frühjahr. Der Unterschied liegt darin, dass sein Schweigen jetzt begründet ist: Bevor eines der Details auf dem Bildschirm erscheint, muss die aktuelle Nachricht stärker zu diesem vollen Speicher passen als gewöhnliche Nachrichten der Nutzerin, die mit demselben Bestand verglichen wurden. Ein nützliches Gedächtnis braucht mehr als eine Möglichkeit zum Erinnern. Es braucht einen guten Grund, das Wort zu ergreifen.

## Quellen

- Angelopoulos, A. N., & Bates, S. (2021). *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*. https://arxiv.org/abs/2107.07511
- Chen, Y., & Wang, X. (2026). *The Price of Scale in Proactive Memory Recall*. https://arxiv.org/abs/2610.34507
- Chen, Y., & Wang, X. (2026). *Code, data and results for The Price of Scale in Proactive Memory Recall*. https://github.com/RiverChenStillCompiling/price-of-scale
- Maharana, A., Lee, D.-H., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024). *Evaluating Very Long-Term Conversational Memory of LLM Agents*. https://aclanthology.org/2024.acl-long.747/
- Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. https://arxiv.org/abs/2410.10813
- Zhang, T., Wang, X., Zhang, Q., Chen, Q., Li, K., Chen, Y., Wang, D., Meng, H. M., & Lu, Y. (2026). *TriggerBench: Investigating Prospective Memory for Large Language Models*. https://aclanthology.org/2026.emnlp-main.1319/

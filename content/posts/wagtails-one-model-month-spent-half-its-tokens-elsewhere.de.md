+++
title = "Wagtails Ein-Modell-Monat verbrauchte die Hälfte der Token anderswo"
slug = "wagtail-ein-modell-monat-haelfte-token-anderswo"
description = "Der Plan, die Entwicklungsarbeit im September mit GLM 5.3 Flash zu erledigen, verbrauchte zwei Milliarden Token. Nur die Hälfte erreichte das Zielmodell; Prototypen, Anbieterkapazität und Evaluierung erklären die Lücke."
tags = ["essays", "models", "tools"]
date = 2026-10-05T03:57:30+02:00
draft = false
+++

Thibaud Colas vom Wagtail-Kernteam versuchte, im September Entwicklungsarbeit mit nur einem effizienten offenen Modell zu erledigen: GLM 5.3 Flash. Sein Nutzungsprotokoll verzeichnet zwei Milliarden Token. Nur eine Milliarde ging an das gewählte Modell.

Das macht das Experiment nützlicher als eine makellose Erfolgsgeschichte. Laut Colas kostete das Zielmodell selbst etwa 68 Dollar und geschätzte 4 kWh Strom. Die gesamte Monatsarbeit erreichte ungefähr 35 kWh statt der geplanten 10 kWh, weil Prototypen, Anbieterprobleme und bewusste Modellevaluierung den Verkehr anderswohin lenkten.

Der deutlichste Fehlschlag kam von einem per „Vibe Coding“ erstellten Prototyp von Wagtails experimentellem Model-Context-Protocol-Server. Laut Colas verbrauchte die Wahl des falschen Modells dafür fast über Nacht 450 Millionen Token, etwa 150 Dollar und 5 kWh. Der Prototyp funktionierte. Seine ausufernde Nutzung zeigt aber, wie schnell ein agentisches Experiment ein sorgfältig gewähltes Budget dominieren kann.

Infrastruktur war die zweite Einschränkung. Colas meldet verschlechterte Leistung von GLM 5.3 Flash und führt sie auf begrenzte Kapazität unabhängiger Inferenzanbieter zurück. Er verlagerte Arbeit auf Alternativen wie DeepSeek V4.1 Flash und Qwen 3.8 Flash. Für ein Team, das die größten Labore meiden will, wird Modellverfügbarkeit zum Teil der Modellqualität: Ein leistungsfähiger Modellstand ist keine verlässliche Produktionswahl, wenn der Endpunkt unter Nachfrage langsamer wird.

Ein Teil der Nutzung außerhalb des Zielmodells war beabsichtigt. Wagtail entwickelt einen eigenen Aufgabenbenchmark. Das Team musste daher verschiedene Modelle ausführen, statt nur den alltäglichen Output zu optimieren. Colas schlägt nun vor, die Ein-Modell-Regel für mehr als die Hälfte der normalen Produktionsarbeit zu reservieren und Forschung und Entwicklung frei Alternativen vergleichen zu lassen.

Er bleibt GLM 5.3 Flash gegenüber positiv. Der lange Kontext, die Bildunterstützung und die Verfügbarkeit bei mehreren Anbietern machten das Modell für Wagtail-Entwicklung, Oberflächenarbeit, Dokumentation und Evaluierung nützlich. Diese Bewertung beruht auf seiner Erfahrung statt auf einem kontrollierten Vergleich.

Die allgemeinere Lehre ist methodisch. Token-Gesamtzahlen allein verbergen, ob die Nutzung aus geplanter Produktion, versehentlichen Schleifen oder notwendiger Evaluierung stammt. Ein nützliches Betriebsdashboard benötigt mindestens Kosten, Energie, Modellidentität und Aufgabenergebnis. Es braucht außerdem lokale, kontinuierliche Messung: Der teure Prototyp wurde erst sichtbar, nachdem er bereits ein Viertel der monatlichen Token verbraucht hatte.

Das ist ein selbst berichteter Monat eines Teams, kein Beleg für bestimmte allgemeine Kosten von GLM 5.3 Flash oder offenen Modellen. Anbieterpreise, Energieschätzungen und Aufgabenmischungen variieren. Der Bericht belegt einen Fehlermodus, für den sich Planung lohnt: Das Modellbudget kann vernünftig sein, während der umgebende Arbeitsablauf es zunichtemacht.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Septembernutzung betrug zwei Milliarden Token, davon eine Milliarde auf GLM 5.3 Flash | VERIFIZIERT | [Wagtail-Bericht](https://wagtail.org/blog/one-month-on-glm-53-flash/) | keine; Nutzungsdashboard des Autors |
| Zielmodellanteil kostete etwa 68 Dollar und 4 kWh; gesamter Monat verbrauchte etwa 35 kWh | LAUT COMMUNITY | [Wagtail-Bericht](https://wagtail.org/blog/one-month-on-glm-53-flash/) | keine; Schätzungen des Autors |
| Prototyp verbrauchte 450 Millionen Token, etwa 150 Dollar und 5 kWh | LAUT COMMUNITY | [Wagtail-Bericht](https://wagtail.org/blog/one-month-on-glm-53-flash/) | keine; Messungen des Autors |
| Anbieterkapazität erzwang Wechsel zu anderen Modellen | LAUT COMMUNITY | [Wagtail-Bericht](https://wagtail.org/blog/one-month-on-glm-53-flash/) | keine; Diagnose des Autors |
| GLM 5.3 Flash war über Wagtail-Entwicklungsaufgaben hinweg nützlich | MEINUNG | [Wagtail-Bericht](https://wagtail.org/blog/one-month-on-glm-53-flash/) | Einschätzung eines Praktikers |
| Modell, Kosten, Energie und Ergebnis sollten gemeinsam gemessen werden | ANALYSE | [Wagtail-Bericht](https://wagtail.org/blog/one-month-on-glm-53-flash/) | Schlussfolgerung aus berichteten Fehlermodi |

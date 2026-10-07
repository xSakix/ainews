+++
title = "vLLM zeigt, wann getrennte Bereitstellung hilft und schadet"
slug = "vllm-getrennte-bereitstellung-hilft-schadet"
description = "Ein praktischer Leitfaden misst den Zielkonflikt bei der Trennung von Prompt-Verarbeitung und Token-Erzeugung. Hohe Latenzen verbessern sich unter Last, doch das Übertragen des Arbeitsgedächtnisses verzögert das erste Token."
tags = ["essays", "tools", "hardware"]
date = 2026-10-06T04:04:31+02:00
draft = false
+++

Prompt-Verarbeitung von Token-Erzeugung zu trennen kann einen Modellserver unter Last stabilisieren. Das Übertragen seines Arbeitsgedächtnisses könnte die erste Antwort aber verlangsamen, berichtet das vLLM-Team.

Das Open-Source-Inferenzprojekt testete „disaggregierte Bereitstellung“, bei der eine GPU das Prefill und eine andere das Decodieren übernimmt. Prefill liest den Prompt und erstellt den Key-Value-Cache. Das Decodieren nutzt diesen Cache zur Token-Erzeugung. Der Leitfaden verlagert außerdem Tokenisierung und Ausgabeanalyse auf ein Frontend ohne GPU.

Für Betreiber, die lange Prompts verarbeiten, bietet der Entwurf eine Wahl zwischen zwei Arten von Verzögerung. Die getrennten Phasen verhindern, dass ein großer Prompt die Generierung für andere Nutzer unterbricht. Der Cache muss aber zwischen den Verarbeitungseinheiten übertragen werden, bevor das Decodieren beginnt.

Im Zwei-GPU-Test von vLLM mit Qwen2.5-7B und Prompts von 8.000 Token stieg der Abstand zwischen erzeugten Token im 99. Perzentil bei der kombinierten Konfiguration mit 0,4 Anfragen pro Sekunde von 23 auf 169 Millisekunden. Die getrennte Konfiguration hielt diesen Abstand zwischen 25 und 52 Millisekunden.

Dasselbe Experiment zeigte die Kosten. Etwa 470 MB Cache pro Prompt zu übertragen dauerte rund 1,3 Sekunden. Die mediane Zeit bis zum ersten Token betrug 2,2 Sekunden, gegenüber 0,7 Sekunden, wenn beide Phasen dieselbe Verarbeitungseinheit nutzten. Die L40S-GPUs hatten weder NVLink noch direkte Peer-to-Peer-Übertragung. Das Ergebnis beschreibt daher einen bewusst ungünstigen Transportweg und nicht jeden Einsatz.

Die Entscheidungsregel der Autoren ist praktisch: zuerst die GPU-Topologie prüfen, dann die Cache-Übertragungsmetriken bei der vorgesehenen Prompt-Länge und Anfragerate untersuchen. Disaggregation ist besonders attraktiv, wenn Prefill das Decodieren wiederholt stört oder wenn beide Phasen unterschiedlich skalieren müssen. Ein leicht ausgelasteter Server kann die Übertragungskosten tragen, ohne nützliche Isolation zu gewinnen.

Der Leitfaden zitiert größere Ergebnisse von AMD und dem llm-d-Projekt. Diese Tests nutzen jedoch andere Modelle, Beschleuniger und Clustergrößen. Sie stützen das Potenzial der Architektur, keine übertragbare Beschleunigungszahl.

Die Anweisungen richten sich an vLLM 0.30.0 oder neuer und umfassen getrennte Renderer- und Derenderer-Dienste. Das Team erklärt, es gebe weiterhin Integrationslücken. Topologie- und Übertragungsprüfungen sind damit eine Voraussetzung und keine Optimierung nach dem Einsatz.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| vLLM dokumentiert getrennte Dienste für Prefill, Decodieren und ein GPU-freies Frontend | VERIFIZIERT | [vLLM-Leitfaden](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | öffentliche vLLM-Konfiguration und Befehle |
| Bei 0,4 Anfragen/s erreichte der p99-Token-Abstand bei gemeinsamer Bereitstellung 169 ms, während getrennte Bereitstellung bei 25–52 ms blieb | LAUT UNTERNEHMEN | [vLLM-Leitfaden](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | keine; Test des Projekts |
| Ein Prompt mit 8.000 Token erzeugte etwa 470 MB Cache und eine Übertragung von rund 1,3 s | LAUT UNTERNEHMEN | [vLLM-Leitfaden](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | keine |
| Die mediane Zeit bis zum ersten Token betrug 2,2 s bei getrennter gegenüber 0,7 s bei gemeinsamer Bereitstellung | LAUT UNTERNEHMEN | [vLLM-Leitfaden](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | keine |
| Der Test nutzte zwei L40S-GPUs ohne NVLink oder Peer-to-Peer-Übertragung | VERIFIZIERT | [vLLM-Leitfaden](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | von den Autoren angegebene Testkonfiguration |
| Der Leitfaden richtet sich an vLLM 0.30.0 oder neuer | VERIFIZIERT | [vLLM-Leitfaden](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | Versionsanforderung im Leitfaden |

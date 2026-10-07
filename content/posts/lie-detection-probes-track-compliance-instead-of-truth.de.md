+++
title = "Lügendetektionssonden verfolgen Gehorsam statt Wahrheit"
slug = "luegendetektionssonden-verfolgen-gehorsam-statt-wahrheit"
description = "Ein Preprint testet acht veröffentlichte Sonden an Sprachmodellen, die Figuren mit falschen Grundüberzeugungen spielen. Viele scheitern, sobald wahre und falsche Antworten denselben Prompt teilen; eine auf die Trennung von Wahrheit und Gehorsam trainierte Sonde hält stand."
tags = ["research", "safety"]
date = 2026-10-06T04:01:31+02:00
draft = false
+++

Viele veröffentlichte Lügendetektionssonden, die interne Aktivität eines Sprachmodells lesen, um falsche Antworten zu markieren, erkennen teilweise, ob das Modell seine Anweisungen befolgt hat. Das berichtet ein neuer Preprint.

Maximilian von Klinski und drei Mitautoren ließen drei offene Modelle Figuren spielen, die grundlegende Fakten ablehnen, etwa einen ptolemäischen Astronomen oder einen Verschwörungstheoretiker. Sie testeten, ob acht bestehende Sonden die falschen Antworten weiterhin erkannten. Viele taten dies, bis wahre und falsche Antworten unter denselben Figurenprompt gestellt wurden. Dann schnitten mehrere schlechter ab als ein Münzwurf.

## Warum das wichtig ist {#why-it-matters}

Ein Sicherheitsteam, das ein eingesetztes Modell mit einer Sonde überwacht, benötigt einen Alarm bei Unwahrheit und nicht bei etwas, das sie gewöhnlich begleitet. In den Trainingsdaten der meisten Sonden ist die falsche Antwort auch die weniger wahrscheinliche und jene, die die Regeln des Modells verletzt. Die Studie findet, dass Sonden diese Abkürzungen lernen.

## Wie eine Sonde ein Modell liest

Eine Sonde ist ein einfacher Klassifikator, trainiert auf den Zahlen innerhalb einer Modellschicht. Diese werden danach gekennzeichnet, ob der verarbeitete Text wahr oder falsch war. Wenn sie funktioniert, liest sie, was das Modell für wahr hält, auch wenn seine ausgegebenen Wörter etwas anderes sagen.

Das Team erstellte einen Datensatz mit 8.916 Antworten von Metas Llama 3.3 70B sowie Googles Gemma 3 27B und Gemma 4 31B. Jedes beantwortete Ja-Nein-Fragen als gewöhnlicher Assistent und als eine von 15 Figuren: Menschen mit realen Überzeugungen, fiktive Figuren wie ein Bürger aus Orwells *1984* sowie historische wie ein mittelalterlicher Arzt. Die Fragen wurden mit einer Pipeline auf Basis von Anthropics Claude Opus 4.8 verfeinert, von Llama als Richter geprüft und vom Erstautor von Hand kontrolliert.

## Derselbe Prompt bringt die meisten Sonden zum Scheitern

In der ersten Testversion trennten die meisten früheren Sonden wahre und falsche Antworten gut. Sie ordneten ungefähr neun von zehn Paaren richtig. Jede falsche Antwort hatte jedoch einen Figurenprompt und jede wahre einen Assistentenprompt. Der Prompt allein verriet damit die Antwort.

Die Autoren entfernten diesen Hinweis, indem sie beide Antworten nach den Figurenprompt stellten. Nun war die wahre Antwort zugleich die weniger wahrscheinliche und jene, die den Anweisungen der Figur widersprach. Auf Llama fielen mehrere zuvor funktionierende Sonden unter Zufallsniveau. Nur zwei blieben nahe an ihren früheren Werten. Die Fehler wiederholten sich auf beiden Gemma-Modellen, oft stärker.

## Drei Fallen isolieren die Abkürzung

Um herauszufinden, was die Sonden verfolgten, baute das Team drei Testsätze, in denen Wahrheit einem wahrscheinlichen Störfaktor entgegenläuft. In einem machte eine Bewertungsregel die falsche Antwort wahrscheinlicher. In einem anderen hatte eine Figur privat eine falsche Überzeugung, etwa dass sieben mal sechs 13 sei. Im dritten verletzte die richtige Antwort eine Formatregel, etwa durch runde Klammern statt vorgeschriebener eckiger, während die falsche sie befolgte.

Die Formatfalle war entscheidend. Auf Llama lag jede frühere Sonde unter Zufallsniveau, außer einer, deren Messwerte in jedem Test umgekehrt waren. Die Autoren deuten dies als starke Verbindung zwischen „wahr“ und „regelkonform“ innerhalb dieser Sonden.

Die eigene Sonde des Teams ergänzt das übliche Training auf einfachen Fakten um eine Zutat: Fragen, deren Anweisungen die falsche Antwort verlangen, sodass Gehorsam und Wahrheit entgegengesetzte Richtungen vorgeben. Sie erreichte im Test mit gemeinsamem Prompt auf Llama etwa 0,98 von 1, fiel auf keinem der drei Modelle unter 0,90 und war auf allen drei Fallen perfekt.

## Eine eigene Korrektur und weiterhin unbekannte Störfaktoren

Dieses Ergebnis braucht zwei Einschränkungen. Die neue Sonde wurde gegen dieselben Störfaktoren entwickelt, auf denen sie anschließend getestet wurde. Die Autoren räumen ein, dass ihre perfekten Fallenwerte dadurch nicht überraschen. Ihr Entwurf erweitert außerdem eine frühere Sonde, die Mitautor Lennart Bürger mitentwickelte. Diese war eine von nur zwei früheren Sonden, die bei gemeinsamem Prompt standhielten.

Die eigenen Daten der Studie zeigen, dass die Liste der Störfaktoren unvollständig ist. Auf Gemma 4 war eine frühere Sonde auf allen drei Fallen fast perfekt, erreichte im Test mit gemeinsamem Prompt aber etwa 0,17. Sie scheiterte aus einem Grund, den keine Falle erfasste. Die Figuren waren außerdem mit einem einzelnen Systemprompt in Gesprächen mit nur einem Zug definiert, auf Modellen mit bis zu 70 Milliarden Parametern.

Die Arbeit wurde vom deutschen Bundesministerium für Forschung, Technologie und Raumfahrt, dem Horizon-Europe-Programm der Europäischen Union und der Deutschen Forschungsgemeinschaft finanziert. Die Autoren haben den Datensatz auf Hugging Face und ihren Code auf GitHub veröffentlicht. Als nächsten Testfall nennen sie Figuren, die sich allmählich in langen Gesprächen entwickeln.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Acht frühere Sonden evaluiert; viele scheitern, wenn wahre und falsche Antworten denselben Figurenprompt teilen | LAUT UNTERNEHMEN | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine; Preprint-Ergebnis |
| Datensatz mit 8.916 menschlich geprüften Antworten aus Llama 3.3 70B, Gemma 3 27B und Gemma 4 31B über 15 Figuren | VERIFIZIERT | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | [Datensatz auf Hugging Face](https://huggingface.co/datasets/maxvonk/anti-factual-personas) |
| Fragen mit einer Claude-Opus-4.8-Pipeline verfeinert, von Llama 3.3 70B beurteilt und vom Erstautor geprüft | VERIFIZIERT | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine; Methodenangabe der Autoren |
| Die meisten früheren Sonden erreichen AUROC 0,86 bis 0,94, wenn sich der Prompt zwischen wahren und falschen Antworten unterscheidet | LAUT UNTERNEHMEN | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine |
| Bei gemeinsamem Prompt auf Llama fallen mehrere frühere Sonden unter Zufallsniveau; nur Marks/Bürger Lie (0,885) und Cundy DolusChat (0,901) bleiben stabil | LAUT UNTERNEHMEN | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine |
| Fehler bei gemeinsamem Prompt wiederholen sich, oft stärker, auf Gemma 3 27B und Gemma 4 31B | LAUT UNTERNEHMEN | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine |
| Auf der Gehorsamsfalle mit Llama liegen alle früheren Sonden unter Zufallsniveau außer Goldowsky-Dill SD, die durchgehend umgekehrt ist | LAUT UNTERNEHMEN | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine |
| Sonden verbinden Wahrheit mit Anweisungsbefolgung | ANALYSE | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | Schlussfolgerung der Autoren aus der Gehorsamsfalle |
| Neue Sonde: AUROC 0,976 im Test mit gemeinsamem Prompt auf Llama, nie unter 0,900 über drei Modelle, perfekt auf allen drei Fallen | LAUT UNTERNEHMEN | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine |
| Die neue Sonde wurde trainiert, dieselben Störfaktoren zu entfernen, auf denen sie getestet wird; Autoren nennen die Fallenresultate nicht überraschend | VERIFIZIERT | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine |
| Mitautor Lennart Bürger entwickelte die Marks/Bürger-Sonde mit, die die neue Sonde erweitert | VERIFIZIERT | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | zitiert Bürger et al. (2024) |
| Auf Gemma 4 ist Cooney DYL auf allen Fallen fast perfekt, erreicht aber 0,171 bei gemeinsamem Prompt | LAUT UNTERNEHMEN | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | keine |
| Finanziert vom deutschen BMFTR, EU Horizon Europe und der Deutschen Forschungsgemeinschaft (DFG) | VERIFIZIERT | [Preprint von von Klinski et al.](https://arxiv.org/abs/2609.39807) | Danksagung |
| Code ist auf GitHub öffentlich | VERIFIZIERT | [GitHub-Repository](https://github.com/max-vkl/stress-testing-llm-lie-detectors) | Repository-Seite lädt |
| Preprint am 30. September 2026 veröffentlicht | VERIFIZIERT | [arXiv-Eintrag](https://arxiv.org/abs/2609.39807) | arXiv-Metadaten |

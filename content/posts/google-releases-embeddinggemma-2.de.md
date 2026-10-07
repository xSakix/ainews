+++
title = "Google veröffentlicht EmbeddingGemma 2 für multimodale Suche"
slug = "google-veroeffentlicht-embeddinggemma-2-multimodale-suche"
description = "Googles Embedding-Modell mit 740 Millionen Parametern bildet Text, Code, Bilder, Video und Audio in einem gemeinsamen Vektorraum ab. Modulare Encoder sind für lokale Geräte ausgelegt."
tags = ["models", "tools"]
date = 2026-10-07T04:01:57+02:00
draft = false
+++

Google hat EmbeddingGemma 2 veröffentlicht, ein Modell mit offenen Gewichten und 740 Millionen Parametern, das Text, Code, Bilder, Videoframes und Audio in einem gemeinsamen Embedding-Raum abbildet.

Die Gewichte unter Apache-2.0 erschienen am 6. Oktober mit Unterstützung in Transformers, sentence-transformers, llama.cpp, vLLM, Ollama, LM Studio, MLX und Transformers.js. Das Modell ist für Informationsabruf und Routing gedacht, nicht für die Erzeugung von Fließtext: Es wandelt verschiedene Eingaben in Vektoren um, deren Ähnlichkeit sich vergleichen lässt.

## Warum das wichtig ist {#why-it-matters}

Wer als Entwickler eine private Suche auf einem Smartphone oder Laptop baut, kann nun eine Sprachnotiz indexieren und einen Videoabschnitt abrufen, ohne zuvor Spracherkennung, Bildbeschreibungen und einen separaten Text-Embedder zu verketten. Dadurch entfallen mehrere Komponenten beim lokalen Informationsabruf. Der tatsächliche Nutzen des Modells hängt allerdings weiterhin von den eigenen Daten und dem Latenzbudget des Nutzers ab.

EmbeddingGemma 2 ist modular. Seine Basis für Text und Code hat 270 Millionen Parameter, während Bildverarbeitung 170 Millionen und Audio 300 Millionen hinzufügen. Alle Konfigurationen projizieren in 768 Dimensionen. Matryoshka-Training ermöglicht Anwendungen, Vektoren auf 512, 256 oder 128 Dimensionen zu kürzen, um Speicherplatz zu sparen.

Google erklärt, quantisierte Gewichte nur für Text belegten auf einem Pixel 11 Pro etwa 191 MB aktiven Arbeitsspeicher, beim vollständigen Modell seien es etwa 567 MB. Sein Kontext von 8.192 Token kann nach Googles Packverfahren bis zu 5,5 Minuten Audio, 29 Bilder oder 58 Videoframes aufnehmen.

Die Evaluierung des Unternehmens beziffert MTEB Code auf 78,68, gegenüber 68,76 beim ersten EmbeddingGemma. Google beansprucht außerdem eine führende Qualität unter multimodalen Embedding-Modellen mit weniger als einer Milliarde Parametern. Das sind Messungen zum Veröffentlichungstag, keine unabhängigen Reproduktionen. Die Modellkarte ist die bessere Grundlage, um eine bestimmte Abrufaufgabe zu vergleichen.

Die Veröffentlichung teilt sich einen Tokenizer und den Entwurf des Audio-Encoders mit Gemma 4. Das kann doppelte Komponenten verringern, wenn der Embedder ein lokales generatives Modell versorgt. Google hat auch Beispielanwendungen für Mediensuche und den Abruf bestimmter Videomomente veröffentlicht.

Die nächsten praktischen Belege werden aus Tests mit gemischten privaten Sammlungen kommen, bei denen modalitätsübergreifende Trefferquote, Indexierungszeit und Speicher wichtiger sind als ein einzelner aggregierter Benchmark.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Google veröffentlichte EmbeddingGemma 2 am 6. Oktober 2026 | VERIFIZIERT | [Google-Ankündigung](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | [Gewichte und Modellkarte](https://huggingface.co/google/embeddinggemma-2) |
| Das Modell hat 740 Mio. Parameter mit modularen Komponenten von 270 Mio. für Text, 170 Mio. für Bilder und 300 Mio. für Audio | VERIFIZIERT | [Google-Ankündigung](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | die Modellkarte führt die Architektur auf |
| Der aktive Arbeitsspeicherbedarf der quantisierten Gewichte beträgt auf Pixel 11 Pro etwa 191 MB für Text und 567 MB für das vollständige Modell | LAUT UNTERNEHMEN | [Google-Ankündigung](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | keine |
| MTEB Code stieg von 68,76 auf 78,68 | LAUT UNTERNEHMEN | [Google-Ankündigung](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | keine |
| Gewichte unter Apache-2.0 sind verfügbar | VERIFIZIERT | [Modell-Repository](https://huggingface.co/google/embeddinggemma-2) | Repository ist zugänglich |

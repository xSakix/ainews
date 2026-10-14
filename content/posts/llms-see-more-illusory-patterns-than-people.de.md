+++
title = "LLMs sehen mehr illusorische Muster als Menschen"
slug = "llms-sehen-mehr-illusorische-muster-als-menschen"
description = "Ein Preprint findet, dass Sprachmodelle aus mehrdeutigen Belegen bereitwilliger Zusammenhänge ableiten als menschliche Teilnehmer. Seine kontrollierten Tests verbinden den Effekt mit häufigkeitssensitiven internen Merkmalen."
tags = ["research", "models"]
date = 2026-10-12T04:01:37+02:00
draft = false
+++

Sprachmodelle bildeten stärkere falsche Muster als Menschen, wenn beide aus mehrdeutigen Belegen Zusammenhänge ableiten sollten, so ein neuer Preprint.

Die Autoren passten klassische psychologische Experimente an, in denen die Beobachtungen keinen verlässlichen Zusammenhang enthalten, Menschen aber häufig einen wahrnehmen. Sie gaben menschlichen Teilnehmern und mehreren Sprachmodellen vergleichbare Aufgaben und prüften dann, ob die Modelle häufige positive Beschreibungen mit Mehrheitsgruppen verbanden oder kausale Erklärungen aus zufälligen Abfolgen konstruierten.

## Warum das wichtig ist {#why-it-matters}

Für Analysten, die mit einem Modell Umfragekommentare, Vorfallberichte oder Kundendaten interpretieren, kann flüssiges Musterfinden aus einer unausgewogenen Stichprobe eine selbstsichere Geschichte machen. Die Studie legt nahe, dass zusätzliche Beobachtungen das Problem nicht zwangsläufig korrigieren, wenn die reine Häufigkeit selbst die Schlussfolgerung antreibt.

Der zentrale Vergleich umfasst zwei Formen illusorischer Musterwahrnehmung. In einer erscheint eine Mehrheitsgruppe häufiger und sammelt deshalb mehr positive und negative Beispiele, obwohl die Anteile denen einer Minderheitsgruppe entsprechen. In der anderen sind unzusammenhängende Ereignisse so angeordnet, dass eine kausale Abfolge verlockend, aber unbelegt ist.

In den berichteten Experimenten stimmten Modelle dem irreführenden Zusammenhang oder der kausalen Erklärung eher zu als menschliche Teilnehmer. Die genaue Größe variierte nach Aufgabe und Modell, sodass das nützliche Ergebnis der Arbeit in Richtung und Konsistenz des Unterschieds statt in einer einzelnen universellen Prozentzahl liegt.

Die Forschenden nutzten auch Sparse Autoencoder, Werkzeuge, die die dichte interne Aktivität eines Modells in eine kleinere Menge interpretierbarer Merkmale überführen. Sie berichten, mit ganzheitlicher Häufigkeitswahrnehmung verbundene Merkmale seien zusammen mit der Antwort zum falschen Muster gestiegen, während Merkmale einer stärker analytischen Orientierung in die andere Richtung wirkten. Dies ist eine Korrelation innerhalb des Modells, kein Beweis, dass eines der Merkmale das Urteil verursacht.

## Der Vergleich ist kontrolliert, aber eng begrenzt

Die Stärke der Arbeit ist ihr direkter Vergleich mit Menschen. Beide Gruppen erhalten Versionen derselben Belege, und die Aufgaben stammen von etablierten Demonstrationen in der kognitiven Psychologie ab. Die Autoren veröffentlichten auch Code, sodass andere Forschende Prompts, Modelle und Sampling-Einstellungen variieren können.

Die Grenzen sind wichtig. Die Antwort eines Sprachmodells entsteht aus Trainingsdaten und Prompt-Konventionen, während die Antwort eines Teilnehmers eine Person in einem Experiment widerspiegelt. Eine gleiche sichtbare Aufgabe macht diese Prozesse nicht gleichwertig. Die berichteten Modelle und Prompts sind außerdem eine Stichprobe einer sich schnell verändernden Population, keine feste Eigenschaft aller Sprachmodelle.

Dennoch identifiziert die Arbeit einen konkreten Fehlermodus: Ein Modell kann die Zahl beobachteter Beispiele als Beleg für Anteile oder Ursachen behandeln. Diese Unterscheidung lässt sich in eingesetzten Systemen einfach genug testen, indem die Verhältnisse konstant gehalten werden, während sich die Gruppengröße ändert.

## Die Studie ergab außerdem

Der falsche Zusammenhang wurde stärker, wenn die Belege eine ganzheitliche Lesart begünstigten. Das ist wichtig, weil viele Zusammenfassungs-Prompts nach einem einzigen Gesamtmuster fragen. Eine analytische Rahmung verringerte die Tendenz unter manchen Bedingungen, was nahelegt, dass Anweisungen die Antwort verschieben können, ohne die zugrunde liegende Empfindlichkeit zu beseitigen.

Preprint und Code sind jetzt verfügbar. Replikationen mit neueren Modellen und natürlichen Betriebsdaten würden zeigen, ob der Laboreffekt Fehler in realer analytischer Arbeit vorhersagt.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| Der Preprint berichtet stärkere illusorische Musterwahrnehmung bei getesteten Sprachmodellen als bei menschlichen Teilnehmern | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.07791 | keine |
| Die Experimente passen klassische Aufgaben zu illusorischen Korrelationen und kausalen Mustern an | VERIFIZIERT | https://arxiv.org/abs/2610.07791 | keine |
| Sparse-Autoencoder-Merkmale, die mit Häufigkeitsempfindlichkeit und analytischer Orientierung verbunden sind, folgen dem berichteten Effekt | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.07791 | keine |
| Das Ergebnis zu internen Merkmalen ist korrelativ statt ein kausaler Eingriff | VERIFIZIERT | https://arxiv.org/abs/2610.07791 | keine |
| Die Autoren veröffentlichten Code für die Experimente | VERIFIZIERT | https://arxiv.org/abs/2610.07791 | keine |

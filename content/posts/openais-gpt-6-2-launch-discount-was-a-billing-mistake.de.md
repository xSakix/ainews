+++
title = "OpenAIs Rabatt zum Start von GPT-6.2 war ein Abrechnungsfehler"
slug = "openais-rabatt-zum-gpt-6-2-start-war-ein-abrechnungsfehler"
description = "OpenAI hat nach eigenen Angaben neun Tage lang zu wenig für die Nutzung von GPT-6.2 Astra und Sol im Abo angerechnet. Seit der Korrektur erreichen Abonnenten ihr Limit 40 beziehungsweise 25 % schneller. Eine unabhängige Messung deutet zugleich darauf hin, dass die Modelle weniger Rechenaufwand ins Schlussfolgern stecken. Der Fall zeigt, wie wenig sich bei einem Pauschaltarif von außen überprüfen lässt."
tags = ["business", "tools"]
date = 2026-11-27T03:17:17+01:00
draft = false
+++

In einer Diskussion auf Hacker News über den Beitrag eines OpenAI-Entwicklers verglichen Nutzer ihre Verbrauchsanzeigen. Ein Kommentator namens seviu schrieb: „Gestern Abend hatte ich noch fast 90 % meines Kontingents. Heute bin ich aufgewacht, und alles war weg.“ Er hatte ein Pro-Abo und über Nacht keinen Agenten laufen lassen. Ein anderer, ragequittah, erinnerte sich ganz anders an die Vorwoche: „Sechs Stunden Astra machten gerade mal 3 % aus.“

Zwischen diesen beiden Beobachtungen liegt der Beitrag des Entwicklers. Er beschreibt eine Änderung daran, wie ein Pauschaltarif einen Arbeitstag abrechnet.

## Die Korrektur

Am 26. November um 02:50 Uhr UTC schrieb Thibault Sottiaux, der bei OpenAI an Codex und ChatGPT arbeitet, auf X: „Bei der Einführung von GPT-6.2 ist uns ein Abrechnungsfehler unterlaufen. Für die meisten Nutzer haben wir die Nutzung von GPT-6.2 Astra und Sol irrtümlich vergünstigt.“ Nach der Korrektur „verbraucht dieselbe Arbeit einen größeren Teil des im Tarif enthaltenen Kontingents“. Gegenüber der Vorwoche „erreichen Sie Ihr Limit mit GPT-6.2 Astra 40 % schneller und mit Sol 25 % schneller“. Die Modelle sollten mit dem Kontingent immer noch weiter kommen als GPT-6 Astra und GPT-6.1 Sol. Andere Modelle seien nicht betroffen. OpenAI werde für die bisherige Nutzung nichts nachberechnen. Zur Entschuldigung könnten alle Abonnenten von Go, Plus, Pro und Business ihr Kontingent einmal zu einem Zeitpunkt ihrer Wahl zurücksetzen.

Was bedeuten die Zahlen für die Arbeit? Wird ein Kontingent 40 % schneller aufgebraucht, reicht es für rund 29 % weniger Aufgaben, denn eins geteilt durch 1,4 ergibt 0,71. Bei 25 % schnellerem Verbrauch sind es 20 % weniger. Das folgt rechnerisch aus OpenAIs Formulierung. Den zugrunde liegenden Abrechnungssatz hat das Unternehmen nicht veröffentlicht.

Die Einführung lag neun Tage zurück. OpenAI stellte GPT-6.2 Astra und Sol am 17. November vor. Dasselbe Datum nannte GitHub, als es die Modelle in Copilot aufnahm. OpenAI warb unter anderem mit der Wirtschaftlichkeit: Beide Modelle „liefern bei anspruchsvollen Aufgaben mit weniger Ausgabe-Token bessere Ergebnisse, sodass sich innerhalb des Nutzungslimits mehr erledigen lässt“. Mit Sol ließen sich „im selben kostenpflichtigen Tarif mehr Aufgaben abschließen“. Für die API sanken Astras Token-Preise um 20 % auf 8 Dollar je Million Eingabe-Token und 40 Dollar je Million Ausgabe-Token. Dieselben Listenpreise hatte Anthropic am 9. November für Claude Fable 5.2 festgelegt. Sol behielt die Preise von GPT-6.1 Sol bei: 2 und 10 Dollar.

Die API-Preise blieben bei der Korrektur unverändert. Ein kostenpflichtiges ChatGPT-Abo rechnet in einer anderen Einheit ab: dem Anteil am Kontingent. Wie viel davon eine Aufgabe verbraucht, legt OpenAI intern fest. Auf der am 27. November eingesehenen Preisseite nennt OpenAI Guthabeneinheiten je Million Token: für Astra 200 bei der Eingabe und 1.000 bei der Ausgabe, ein Fünftel weniger als die 250 und 1.250 bei GPT-6 Astra. Für Sol bleiben es 50 und 250. Für Plus-Abonnenten schätzt OpenAI die Zahl lokaler Codex-Nachrichten je Fünfstundenfenster bei GPT-6.2 Astra auf 6 bis 50 und bei Sol auf 17 bis 180. Bei GPT-6 Astra sind es 5 bis 45, bei GPT-6.1 Sol 15 bis 160. Diese Schätzungen seien „keine festen Nachrichtenlimits“. „Für Pro-Tarife gilt derzeit kein Fünfstundenlimit“, heißt es dort. Auch Wochenlimits könnten gelten.

Eine Spanne von 6 bis 50 kann die Angabe von 40 % weder bestätigen noch widerlegen. Die Seite lässt offen, ob die Tabelle nach der Korrektur aktualisiert wurde. Der von seviu geschilderte Verlust über Nacht ist ein unbestätigter Einzelfall. Ursache könnten die Änderung oder ein Wochenlimit gewesen sein.

## Worüber die Nutzer diskutierten

Der Beitrag erhielt auf Hacker News unter einer Überschrift, die von einer Nutzungskürzung sprach, 468 Punkte. Die Leser waren sich über seine Bedeutung uneins. Einige nahmen den „Abrechnungsfehler“ wörtlich. Ein Kommentator berichtete, nach Stunden mit Astra 6.2 habe die Anzeige noch immer 100 % ausgewiesen. Er habe deshalb nach einem Fehler im Anzeigeelement gesucht. Andere sahen in der Korrektur eine als Fehlerbehebung verpackte Preiserhöhung. Manche gaben an, gekündigt zu haben oder Angebote von Anthropic und Google abzuwägen. Ein weiterer Kommentar verwies darauf, dass OpenAIs erste E-Mail kurz gewesen sei und eine zweite sie habe erklären müssen. All das sind Erfahrungsberichte einzelner Nutzer, keine Messungen.

Manche erinnerten sich an frühere Wechsel. Ein langjähriger Nutzer von OpenAI und Anthropic schrieb, OpenAIs Kontingente hätten sich bei ständig neuen Möglichkeiten zum Zurücksetzen grenzenlos angefühlt. Dann habe Opus 5.5 mehr Nutzung ermöglicht und OpenAI habe darauf mit kleineren Kontingenten reagiert. Ein anderer entgegnete, seit es diese Angebote gebe, liege mal der eine und mal der andere Anbieter vorn. Das werde wieder geschehen. Beide schildern Erinnerungen, aus denen sich die tatsächliche Leistung eines Tarifs nicht ablesen lässt.

## Eine zweite Messung derselben Modelle

Am 26. November, wenige Stunden nach Sottiaux’ Beitrag, veröffentlichte der Entwickler des Direktvergleichs Agent Duel den Beitrag *OpenAI may be in cost control mode*. Agent Duel basiert auf dem Programmieragenten OpenCode, lässt Modelle bei realen Aufgaben gegeneinander antreten und erstellt eine Rangliste nach Elo-Punkten. Laut dem Autor verbrauchten Astra 6.2 und Sol 6.2 in denselben Duellen gegen dieselben Gegner je Aufgabe weniger Ausgabe-Token und weniger Reasoning-Token als ihre Vorgänger. Für die Ausgabe-Token nennt er p-Werte von 0,0055 bei Sol und 0,022 bei Astra, für die Reasoning-Token 0,00013 bei Sol und 0,0064 bei Astra. Die Modelle „scheinen auf Kosten optimiert“ zu sein, so sehr, dass sie „durch besonders wenig Nachdenken auffallen“.

Die Deutung als Kostenfrage stammt vom Autor. Die Daten zeigen, dass die Modelle weniger Token fürs Schlussfolgern verbrauchen, lassen die Ursache aber offen. OpenAI nennt weniger Ausgabe-Token bei der Einführung als Vorteil. Astra habe im internen Vergleichstest GDPval v2 gegenüber GPT-6 Astra 6,2 Punkte hinzugewonnen und dabei 22 % weniger Ausgabe-Token verbraucht. Derselbe Messwert lässt sich als Effizienzgewinn oder als Sparmaßnahme deuten. Welche Erklärung zutrifft, weiß nur OpenAI. Eine geringere Token-Zahl erklärt auch nicht den Abrechnungsfehler, bei dem es um die Anrechnung auf ein Kontingent ging.

Auch die Rangliste vom 27. November, 03:00 Uhr UTC, liefert kein eindeutiges Bild. GPT-6.2 Astra steht mit 1.007 Elo-Punkten und einem Intervall von plus/minus 61 auf Platz fünf, bei 2,33 Dollar und 2,6 Minuten je Aufgabe. Sol liegt mit 937 Punkten, 0,43 Dollar und 1,7 Minuten auf Platz zwölf. Claude Fable 5.2 führt mit 1.069 Punkten und 3,49 Dollar vor Claude Opus 5.5 mit 1.060 Punkten und 1,63 Dollar. Die Intervalle überschneiden sich erheblich. Für Astra sind die Plätze zwei bis elf plausibel.

## Was Abonnenten überprüfen können

Listenpreis und Rechnung sind schon früher auseinandergefallen. Am 9. November senkte Anthropic den Preis für Fable 5.2 auf 8 und 40 Dollar je Million Token, ein Fünftel unter dem Vorgänger. Dennoch führt Artificial Analysis das Modell unter den untersuchten Modellen bei den Kosten auf dem letzten Platz: 26,54 Dollar je Aufgabe im Intelligence Index. Die Rechnung hängt davon ab, wie viele Token das Modell tatsächlich verbraucht. Bei OpenAI kommt eine weitere Ebene hinzu. Für Abonnenten legt der Anbieter drei Größen fest: wie viele Token das Modell verbraucht, zu welchem Satz diese auf das Kontingent angerechnet werden und wie groß das Kontingent ist. Bei einer davon, dem Abrechnungssatz, lag OpenAI nach eigenen Angaben in den ersten neun Tagen falsch.

Außenstehende können die erste Größe messen, wie Agent Duel es getan hat. Für die beiden anderen bleibt ihnen nur die Verbrauchsanzeige. Wer vor einer leeren Anzeige sitzt, findet auf der Preisseite diesen Satz: „Aufgaben, die ähnlich aussehen, können unterschiedlich große Teile Ihres Kontingents verbrauchen.“

## Quellen

- Agent Duel (2026). *Agent Duel Leaderboard*, generated 27 November 2026. https://agentduel.com/leaderboard
- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- GitHub (2026). *OpenAI's GPT-6.2 Astra and GPT-6.2 Sol now available*. GitHub Changelog, 17 November. https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available
- Hacker News (2026). *OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster*. https://news.ycombinator.com/item?id=50651117
- micjm (2026). *OpenAI may be in cost control mode*. https://micjm.com/blog/openai-is-in-cost-control-mode/
- OpenAI (2026). *Introducing GPT-6.2 Astra and Sol*. https://openai.com/index/introducing-gpt-6-2-astra-sol
- OpenAI (2026). *Pricing*. ChatGPT Learn. https://learn.chatgpt.com/docs/pricing
- Sottiaux, T. (2026). Post on X about the GPT-6.2 billing mistake, 26 November. https://x.com/thsottiaux/status/2125784147889393806

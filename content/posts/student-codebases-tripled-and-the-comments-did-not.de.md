+++
title = "Studentischer Code verdreifachte sich, die Kommentare nicht"
slug = "studentischer-code-verdreifacht-kommentare-nicht"
description = "Eine Studie über zehn Semester und 260 Abschlussprojekt-Repositories findet, dass der Code am Semesterende bei breiter KI-Verfügbarkeit von etwa 3,4 auf 10 Tausend Zeilen wuchs, während die Kommentardichte stagnierte. Die Autoren beobachteten keine KI-Nutzung; das Ergebnis warnt daher Bewertende und Arbeitgeber, ohne ein Urteil über die Werkzeuge zu fällen."
tags = ["research", "tools"]
date = 2026-11-09T03:16:01+01:00
draft = false
+++

Eine Kurskoordinatorin sitzt am Freitag vor der Notenabgabe vor ihrem Rechner. Sie hat eine Tabelle mit gut vierzig Studierendenteams und eine seit Jahren gepflegte Gewohnheit: Repository öffnen, Umfang und Regelmäßigkeit der Arbeit betrachten und daraus ableiten, wer gearbeitet hat. Dieses Jahr enthält das erste Repository auf ihrer Liste zehntausend Codezeilen und dreihundert Commits. Sie scrollt durch eine Funktion mit tief verschachtelten Verzweigungen und findet keinen Kommentar, der eine davon erklärt. Die Koordinatorin ist erfunden und steht für ein Problem, das drei Forscher nun gemessen haben.

Die Studie *Code, Commits, and Complexity in the GenAI Era* wurde am 5. November auf arXiv veröffentlicht und für das SIGCSE Technical Symposium im Februar 2027 angenommen. Ihre Autoren sind Asma Shakil und Paul Denny von der University of Auckland sowie Claus Brabrand von der IT University of Copenhagen. Sie analysierten 260 Team-Repositories aus einem verpflichtenden Abschlussprojektkurs im letzten Studienjahr über zehn Semester von 2021 bis 2025. Der mediane Codebestand am Semesterende wuchs von etwa 3,4 Tausend Zeilen in den Jahren 2021 bis 2023 auf etwa 10 Tausend in den Jahren 2024 und 2025. Die Autoren beobachteten niemanden bei der KI-Nutzung und betonen das wiederholt.

## Ein Kurs, zehn Semester

In dem Kurs entwickeln Teams aus fünf oder sechs Studierenden über dreizehn Wochen Software für reale externe Kunden. Bewertet wird vor allem der funktionierende Prototyp. Die Repositories stammen aus der GitHub-Organisation des Kurses: zunächst 302, nach Entfernung leerer, vorlagenbasierter und doppelter Exemplare 260. Die Jahrgänge 2021 bis 2025 enthalten 19, 65, 57, 51 und 68 Repositories.

Die Autoren messen jedes Repository zweimal: bei der Vorführung zur Semestermitte in Woche 7 und bei der Abschlusspräsentation in Woche 13. Sie zählen Codezeilen mit tokei, messen die mittlere zyklomatische Komplexität je Funktion mit lizard und zählen Fehlerbehandlungskonstrukte lexikalisch. Außerdem zählen sie Commits. Für jede Kennzahl testen sie, ob sie über die fünf Jahrgänge stetig steigt oder fällt, und korrigieren für die Zahl der getesteten Kennzahlen.

Sie teilen die Jahre in eine Phase geringerer und eine Phase höherer Verfügbarkeit generativer KI ein. Die Veröffentlichung von ChatGPT im November 2022 dient als ungefähre Grenze. Sie betonen, dass diese nicht scharf ist. GitHub Copilot wurde im Juni 2022 für verifizierte Studierende kostenlos, und die Verbreitung erfolgte danach allmählich. Sie zitieren eine Umfrage des Higher Education Policy Institute, in der der Anteil britischer Bachelorstudierender mit generativer KI bei benoteten Arbeiten von 53 % Ende 2023 auf 88 % Ende 2024 stieg.

## Was sich änderte und wann

Der mediane endgültige Codebestand betrug 2021 2,3 Tausend Zeilen, 2022 3,7 und 2023 3,4. Danach sprang er 2024 auf 7,7 und 2025 auf 11. Die Momentaufnahme zur Semestermitte folgt demselben Muster: von 1,4 bis 1,8 Tausend Zeilen vor 2024 auf 4,8 Tausend im Jahr 2025. Der Jahrgang 2023, der erste nach ChatGPT, ähnelt den früheren; die Autoren bezeichnen ihn als Übergangsjahrgang.

Die medianen Commits je Repository stiegen von 63 im Jahr 2021 und etwa 100 bis 112 in den Jahren 2022 und 2023 auf 265 im Jahr 2024 und 300 im Jahr 2025. Commits je aktivem Tag nahmen von 3,3 auf 5,4 zu. Die Größe einzelner Commits änderte sich kaum: Der Median blieb zwischen 38 und 65 geänderten Zeilen. Das widerspricht der verbreiteten Erwartung, KI-Code werde in wenigen großen Blöcken hinzugefügt. Diese Studierenden erstellten häufiger Commits, in ungefähr ebenso großen Stücken wie zuvor.

Das deutlichste Ergebnis betrifft den Inhalt des Codes. Die mittlere zyklomatische Komplexität stieg von 1,7 im Jahr 2021 auf 2,5 im Jahr 2025. Fehlerbehandlungskonstrukte je tausend Zeilen stiegen von 3,7 und 4,8 in den Jahren 2022 und 2023 auf 12 und 13 in den Jahren 2024 und 2025. Die Kommentardichte, also der Anteil der Kommentarzeilen, zeigte keinen klaren Trend; sie lag 2021 bei 9,2 % und 2025 bei 8,4 %. Die Autoren nennen dieses Muster „Komplexität ohne Kommentare“. Spätere Jahrgänge reichten umfangreicheren und komplizierteren Code ein, der nicht besser erklärt war.

## Was die Autoren nicht behaupten

Shakil, Brabrand und Denny benennen die Grenzen deutlich. Sie beobachteten keine KI-Nutzung und berichten deshalb Veränderungen, die mit größerer Verfügbarkeit zusammenfallen, keine Wirkungen. Lehrpersonal, Bewertungskriterien und Projekttypen änderten sich über die Jahre. Der Jahrgang 2021 und ein Teil des Jahrgangs 2022 arbeiteten teilweise unter COVID-19-Beschränkungen, und 2021 umfasst nur 19 Repositories. Frameworks und Projektvorlagen können selbst Standardcode hinzufügen. Der Sprachmix verschob sich zu JavaScript und TypeScript: Diese führten 2021 bis 2023 in 42 bis 58 % der Repositories und 2024 und 2025 in 71 bis 74 %. Auch beschränkt auf die 157 Repositories in diesen Sprachen bleiben alle fünf signifikanten Trends bestehen.

Die Kennzahlen sind Näherungswerte. Die Fehlerbehandlungszählung ist lexikalisch, und zyklomatische Komplexität „hängt nur schwach damit zusammen, wie schwer Code zu verstehen ist“, schreiben die Autoren. Weil sie mit einem anderen Werkzeug erhoben wird als die Kommentarzahl, bitten sie darum, den Befund der Komplexität ohne Kommentare auf Jahrgangsebene zu lesen. Alles stammt aus einem Kurs an einer Institution.

## Einordnung in die bisherige Evidenz

Die Studie erweitert frühere Arbeiten. Y. Zhang und Kollegen verfolgten in einem Preprint vom Januar 2026 eine unveränderte Cloud-Computing-Aufgabe über fünf Semester vor und fünf nach ChatGPT. Endabgaben wurden länger, Änderungen zwischen Abgaben umfangreicher und die Notenverbesserung je Änderung geringer. Das Auckland-Team findet bei einem längeren Teamprojekt ein ähnliches Größenwachstum, aber nicht dasselbe Muster bei der Commit-Größe.

Zwei weitere Studien ordnen ein, was das Wachstum bedeuten könnte. S. Peng und Kollegen fanden 2023 in einem kontrollierten Experiment, dass Entwickler mit GitHub Copilot eine HTTP-Server-Aufgabe 55,8 % schneller erledigten. Eine randomisierte Studie von J. H. Shen und A. Tamkin aus dem Jahr 2026 ergab, dass Entwickler, die eine neue Bibliothek für asynchrone Programmierung mit KI-Hilfe lernten, schlechteres begriffliches Verständnis, Codelesen und Debugging zeigten, ohne signifikante durchschnittliche Geschwindigkeitsgewinne. Die Auckland-Autoren zitieren dieses Ergebnis, um ihre Sorge zu präzisieren: Der zusätzliche Code könnte schwerer zu prüfen sein, und starke KI-Abhängigkeit kann die Fähigkeiten beeinträchtigen, die für seine Prüfung gebraucht werden.

Für Lehrende betrifft die praktische Schlussfolgerung das Messen. Codeumfang und Commit-Zahlen, die früher als Anstrengung gelesen werden konnten, sind stark gestiegen. Ein größerer, häufiger eingecheckter Codebestand belegt nicht mehr, dass mehr gelernt wurde. Die Autoren schlagen mündliche Verteidigungen, gemeinsame Codebesprechungen und ausdrückliche Dokumentationsanforderungen vor. Arbeitgeber, die die Repositories von Absolventen als Portfolio lesen, stehen vor demselben Problem.

Eine Woche später sitzt die gedachte Koordinatorin mit einem Team in einem Raum. Sie öffnet das Repository nicht. Sie bittet eine Studentin, irgendeine Funktion auszuwählen und zu erklären, warum sie sich so verzweigt. Die erfundene Studentin liest langsam und gesteht dann, sie noch nie gesehen zu haben. Ob der Code aus einem Werkzeug, von einem Teammitglied oder aus ihrer eigenen Nachtschicht stammt: Das Gespräch zeigt der Koordinatorin, was die Zeilenzahl nicht zeigen konnte.

## Quellen

- Azeem, S., Naveed, M. S., Sajid, M., & Ali, I. (2025). *AI vs. human programmers: complexity and performance in code generation*. VAWKUM Transactions on Computer Sciences, 13(1), 201-216.
- Freeman, J. (2025). *Student generative AI survey 2025*. Higher Education Policy Institute, HEPI Policy Note 61.
- Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. https://arxiv.org/abs/2302.06590
- Shakil, A., Brabrand, C., & Denny, P. (2026). *Code, Commits, and Complexity in the GenAI Era: A Longitudinal Study of Team-Based Capstone Projects*. https://arxiv.org/abs/2611.07297
- Shen, J. H., & Tamkin, A. (2026). *How AI Impacts Skill Formation*. https://arxiv.org/abs/2601.20245
- Zhang, Y., Savelka, J., Goldstein, S., & Conway, M. (2026). *Changes in Coding Behavior and Performance Since the Introduction of LLMs*. https://arxiv.org/abs/2601.11835

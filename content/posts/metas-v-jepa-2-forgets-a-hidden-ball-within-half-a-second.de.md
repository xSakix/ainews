+++
title = "Metas V-JEPA 2 vergisst einen versteckten Ball in einer halben Sekunde"
slug = "metas-v-jepa-2-vergisst-versteckten-ball-halbe-sekunde"
description = "Forscher der Technical University of Munich prüften Metas Videoweltmodell mit einem Test für Säuglinge. In gerenderten Szenen weiß der sehende Teil, dass ein Ball in einer geschlossenen Box liegt, während der ergänzende Teil ihn verliert. Kurzes Training behebt das, doch ein Standardbenchmark steigt ebenso nach Training, das dies nie lehrt."
tags = ["research", "models"]
date = 2026-10-12T10:17:01+02:00
draft = false
+++

Ein erfundener Straßenzauberer steht auf einem kalten Platz in München. Er zeigt einem etwa vierjährigen Jungen eine Münze, schließt die Faust darum, bläst auf die Knöchel und öffnet die Hand. Die Handfläche ist leer. Der Junge schreit auf. Er war sicher, die Münze sei noch darin, und diese Gewissheit ist der ganze Trick. Ein Zauberer kann nur jemanden täuschen, der glaubt, dass Dinge weiter existieren, wenn niemand sie sieht.

Peng Xie und Amr Alanwar, zwei Forscher der Technical University of Munich, begannen ihre Studie mit solchen Tricks. Sie nahmen gefilmte Zaubertricks, deren Überraschungsmomente menschliche Zuschauer bewertet hatten, und zeigten sie V-JEPA 2. Meta veröffentlichte das Videomodell 2025 nach Training auf über einer Million Stunden Internetvideo. Das Modell war nie überrascht. In drei Tricksammlungen und sechs Messverfahren stieg und fiel sein Vorhersagefehler, der Modellersatz für Überraschung, mit der Bewegung auf dem Bildschirm, nie mit den von Menschen markierten Momenten. Ihr am 5. Oktober auf arXiv veröffentlichter Preprint baut stattdessen ein Instrument, um ins Modell zu schauen.

## Zwei Hälften im Widerspruch

V-JEPA 2 hat zwei Hälften. Ein Encoder macht Video zu einer abstrakten Beschreibung seines Inhalts. Ein Prädiktor erhält einen Clip mit ausgeschnittenen Teilen und errät deren Beschreibung. Das Design folgt einem Ansatz, den Yann LeCun 2022 vorschlug: Eine Maschine soll ein Modell der Welt aufbauen, indem sie Unsichtbares in abstrakten Beschreibungen statt Pixeln vorhersagt. Meta hat V-JEPA 2 zur Planung von Roboterarmbewegungen eingesetzt.

Xie und Alanwar fanden, dass die Hälften über ein verdecktes Objekt uneinig sind: Der Encoder hält daran fest, der Prädiktor, der Unsichtbares ergänzen soll, verliert es innerhalb eines Sekundenbruchteils. „Ein planendes Weltmodell muss den Zustand dessen bewahren, was nicht mehr sichtbar ist“, schreiben die Autoren. „Eine Hand, die sich um eine Münze schloss, hält sie noch immer.“

## Was ein fünf Monate altes Baby erwartet

Psychologen streiten seit fast einem Jahrhundert über diese Erwartung. Jean Piaget beobachtete seine drei Kinder und fand, ein Baby beginne erst zwischen acht und zehn Monaten, nach einem hinter einem Schirm versteckten Spielzeug zu suchen. In den ersten Monaten sei ein Objekt, schrieb er, „ein bloßes Bild, das ins Nichts zurückkehrt, sobald es verschwindet“.

1985 widersprachen Renée Baillargeon, Elizabeth Spelke und Stanley Wasserman mit einem Holzschirm und einer gelben Box mit kleinen roten Sternen. Der Schirm lag flach, schwenkte dann wie eine Zugbrücke nach oben und verdeckte die Box. In einer Version stoppte er dort, wo die Box sein sollte. In der anderen drehte er einen vollen Halbkreis weiter, als durch die Box hindurch. Fünfmonatige Babys sahen länger auf die zweite Version, wie Menschen auf etwas Unmögliches schauen. Die Forscher folgerten, schon so junge Säuglinge verstünden, dass verdeckte Objekte weiter existieren. Andere wiederholten die Zugbrücke und argumentierten, die Babys, die vor dem Test die ganze Halbkreisbewegung wiederholt gesehen hatten, reagierten auf Vertrautheit oder einfach auf mehr Bewegung. Die Debatte bleibt offen.

Forscher des maschinellen Lernens übernahmen die Methode trotzdem. Der IntPhys-Benchmark paart mögliche und unmögliche Ereignisse und wertet ein Modell als richtig, wenn es das unmögliche weniger plausibel findet; bei V-JEPA heißt das höherer Vorhersagefehler. Im Februar 2025 berichtete ein Meta-Team, das erste V-JEPA zeige nach Training nur auf natürlichen Videos „Verständnis verschiedener Eigenschaften intuitiver Physik wie Objektpermanenz“. Solches Wissen müsse nicht eingebaut sein. In einem Anhang räumte dasselbe Team Zweifel ein: Ein anfangs sichtbarer, dann verdeckter Ball könne es dem Modell erschweren, „vorherzusagen, dass der rote Ball wieder sichtbar ist“. Es testete das nicht.

## Ein Ball, ein Streifen und zwei Welten

Die Münchner Studie tut das. Die Forscher renderten einfache Szenen eines Balls, der über einen strukturierten Hintergrund rollt. Zu einem festgelegten Zeitpunkt entfernten sie den Bildstreifen entlang seines Wegs aus der Modellsicht. Sie erzeugten zwei Szenenversionen, überall identisch außer im Streifen. In einer rollt der Ball weiter, in der anderen ist er weg. Der Prädiktor ergänzt den Streifen, und die Forscher fragen, welcher Welt seine Vermutung ähnelt. Es gibt eine Antwort pro etwa viertelsekündigem Zeitfenster, jeweils gestützt auf sechzig Szenen. Ein Münzwurf träfe die Hälfte.

Beim Verdecken entschied sich die am genauesten untersuchte V-JEPA-2-Version in 92 % der Szenen für den Ball. Ein Zeitfenster später in keiner. Die kleinere und größere Version verhielten sich ebenso; Größe brachte nichts. Nur wenn auch der Großteil des übrigen Bildes wie im Training ausgeblendet war, hielt die mittlere Version etwa eine Sekunde am Ball fest; die anderen verloren ihn weiterhin. Ein vorher gestoppter Ball schnitt etwas besser ab: Die Modelle behielten ihn im Mittel in 13 bis 41 % der Szenen, während ein einfaches Programm, das das letzte sichtbare Bild kopiert, ihn fast immer behält.

Die Information war nicht verschwunden. Ein einfaches auf Encoderbeschreibungen trainiertes Programm erkannte jedes Mal den Ball und las den Inhalt einer geschlossenen Box volle dreieinhalb Sekunden nach dem Schließen. Auf die Prädiktorausgabe angewendet fand es den Ball nach einer halben Sekunde geschlossener Box in zwei Prozent der Szenen und danach nie. „Das Defizit betrifft nicht die Wahrnehmung“, schreiben die Autoren über gerenderte Szenen. Bei einer echten Hand um eine Münze verlor auch der Encoder sie. Andere Videomodelltypen waren bei einer bewegten Box nicht besser. NVIDIA Cosmos behielt in seiner stückweise vorhersagenden Version einen Ball in einer unbewegten Box über zwei Sekunden, verlor aber einen in einer bewegten Box transportierten. VideoMAE, das fehlende Pixel rekonstruiert, behielt fast nichts.

## Kurzes Training und seine Grenzen

Diese Lernweise kann die Lücke schließen. Als die Forscher nur den Prädiktor dreitausend Schritte mit Szenen von Bällen in Boxen trainierten, weniger als eine Stunde auf einem Rechenzentrums-Grafikchip, stieg seine Überzeugung, ein transportierter Ball sei noch darin, von fast nie auf immer. Zwei Kontrollbedingungen blieben bei null. Weitertraining des ganzen Modells mit V-JEPAs eigenem Ausschnittmuster auf Egoaufnahmen arbeitender Hände und Roboterarme oder Internetclips gab ihm mehr als eine Sekunde Erinnerung für einen rollenden Ball.

Die Autoren benennen die Schwächen der Lösung. Trainings- und Testszenen kamen aus demselben Renderer, weshalb ein perfektes Ergebnis dort erwartbar ist. Auf natürlichen Videohintergründen entschied sich das trainierte Modell in 85 bis 97 % der Szenen für den Ball. Es lernte eine hartnäckige Annahme: Selbst wenn das Clipende den verschwundenen Ball zeigte, sagte es ihn weiter in der Lücke vorher. Die Kosten dieses Trainings für das Modell anderswo wurden nicht gemessen.

## Der Benchmark, der den Unterschied nicht erkannte

Das Boxtraining erhöhte auch den IntPhys-Wert von 84,2 auf 93,3 %, was die Frage zu klären schien. Dann führten die Forscher dasselbe Training durch, ohne jemals nach dem Boxinhalt zu fragen, und der Wert stieg genauso. Training mit unbewegten Szenen war ebenso gut. Ein Modell, das auf Clips echter Hände mit digital in die Handfläche gesetzter Münze erkennen sollte, ob sie geblieben oder entfernt worden war, erreichte in zwei Läufen 27 und 31 % bei IntPhys, schlechter als Zufall. „Ein Benchmark-Gewinn ist deshalb für sich kein Beleg für Permanenz“, folgern die Autoren.

Ihre eigenen Belege haben Grenzen, die ein Anhang dazu nennt, was ihre Schlussfolgerungen ändern würde. Sie prüften V-JEPA 2s vortrainierten Prädiktor, nicht die aktionsbedingte Version zur Robotersteuerung. Jede Messung der Modellüberzeugung stammt aus von einem Programm gezeichneten Szenen, sechzig zugleich; das Ergebnis echter Hände beruht auf einem Dutzend untrainierter Clips. Der Code werde veröffentlicht, sagen sie; das Papier ist nicht begutachtet. Es enthält auch eine ausführliche Offenlegung: Ein KI-Assistent half bei Experimentdesign, Code und Text. Die Autoren nennen gefundene und vor Veröffentlichung korrigierte Codefehler, darunter einen auf leeren Clips trainierten Lauf.

## Zurück auf dem Platz

Auf dem erfundenen Platz bittet der Junge um Wiederholung. Jetzt beobachtet er die Faust, nicht das Gesicht, weil er sicher ist, die Münze sei irgendwo darin. Diese Gewissheit macht ihn täuschbar und wird ihn eines Tages den Zauberer ertappen lassen. Ein Modell, das die Münze vergisst, kann beides nicht. Auf gerenderten Szenen gaben dreitausend Trainingsschritte V-JEPA 2 die Gewissheit des Jungen. Ob sie auf echten Aufnahmen hält, wenn ein Becher über etwas gestellt wird, das ein Roboter finden muss, ist laut Autoren noch nicht getestet.

## Quellen

- Assran, M., Bardes, A., Fan, D., Garrido, Q., Howes, R., Komeili, M., et al. (2025). *V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning*. https://arxiv.org/abs/2506.09985
- Baillargeon, R., Spelke, E. S., & Wasserman, S. (1985). *Object permanence in five-month-old infants*. https://doi.org/10.1016/0010-0277(85)90008-3
- Bardes, A., Garrido, Q., Ponce, J., Chen, X., Rabbat, M., LeCun, Y., et al. (2024). *Revisiting Feature Prediction for Learning Visual Representations from Video*. https://arxiv.org/abs/2404.08471
- Bogartz, R. S., Shinskey, J. L., & Schilling, T. H. (2000). *Object permanence in five-and-a-half-month-old infants?* https://doi.org/10.1207/S15327078IN0104_3
- Garrido, Q., Ballas, N., Assran, M., Bardes, A., Najman, L., Rabbat, M., et al. (2025). *Intuitive physics understanding emerges from self-supervised pretraining on natural videos*. https://arxiv.org/abs/2502.11831
- LeCun, Y. (2022). *A Path Towards Autonomous Machine Intelligence*. https://openreview.net/forum?id=BZ5a1r-kVsf
- Margoni, F., Surian, L., & Baillargeon, R. (2024). *The violation-of-expectation paradigm: A conceptual overview*. https://doi.org/10.1037/rev0000450
- NVIDIA, Agarwal, N., Ali, A., Bala, M., Balaji, Y., Barker, E., et al. (2025). *Cosmos World Foundation Model Platform for Physical AI*. https://arxiv.org/abs/2501.03575
- Piaget, J. (1954). *The Construction of Reality in the Child* (M. Cook, Trans.; original work published 1937). https://doi.org/10.1037/11168-000
- Riochet, R., Ynocente Castro, M., Bernard, M., Lerer, A., Fergus, R., Izard, V., et al. (2022). *IntPhys 2019: A Benchmark for Visual Intuitive Physics Understanding*. https://doi.org/10.1109/TPAMI.2021.3083839
- Rivera, S. M., Wakeley, A., & Langer, J. (1999). *The drawbridge phenomenon: Representational reasoning or perceptual preference?* https://doi.org/10.1037/0012-1649.35.2.427
- Tong, Z., Song, Y., Wang, J., & Wang, L. (2022). *VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training*. https://arxiv.org/abs/2203.12602
- Xie, P., & Alanwar, A. (2026). *Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object*. https://arxiv.org/abs/2610.07355

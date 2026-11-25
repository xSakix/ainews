+++
title = "Anthropic nimmt einzelne Neuronen erneut unter die Lupe"
slug = "anthropic-nimmt-einzelne-neuronen-erneut-unter-die-lupe"
description = "Anthropic-Forscherinnen halten einzelne Neuronen für leichter lesbar als bisher angenommen. In offenen Modellen und kontrollierten Versuchssystemen nutzen sie Neuronen als Detektoren ohne Trainingsbeispiele, zur Verhaltenssteuerung und als Hinweise auf verborgene Verhaltensweisen."
tags = ["research", "safety", "models"]
date = 2026-11-25T04:03:43+01:00
draft = false
+++

Ein Prüfer öffnet zwei Kopien eines Sprachmodells. Die eine ist das vertraute Basismodell. Die andere enthält einen kleinen Adapter, dessen Zweck er nicht kennt. Um herauszufinden, was sich geändert hat, befragt der Prüfer diesmal nicht das modifizierte Modell. Er geht eine Liste von Neuronen durch und sucht nach denen, die ihre Gewohnheiten geändert haben.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

Auf diesen Ansatz setzen die Anthropic-Forscherinnen Jasmine Shone und Lisa Dunlap in zwei Berichten. Einzelne Neuronen galten lange als unzuverlässig, wenn es darum ging, einem Vorgang im Modell eine Bedeutung zuzuordnen. Den Forscherinnen zufolge können sie jedoch sichtbar machen, was bei der Feinabstimmung hinzugekommen ist. In einem Blindtest mit 68 LoRA-Adaptern enthielten 58 ein verstecktes Verhalten. Das neuronengestützte Prüfsystem konnte es bei 75 % dieser Adapter benennen. Allein anhand der Modellausgaben gelang das bei 40 %.

Die Arbeiten greifen eine alte Frage der Interpretierbarkeitsforschung auf. Einst hoffte man, durch Betrachtung einzelner Neuronen die Konzepte eines Modells zu erkennen. Dann zeigte sich, dass Neuronen auf mehrere Bedeutungen ansprechen, dass sich Darstellungen von Schicht zu Schicht ändern und dass der Abruf von Fakten über viele Pfade verteilt ist. Große Teile der Forschung wandten sich deshalb erlernten Merkmalen, diagnostischen Sonden und Richtungen im Residualstrom zu. Shone und Dunlap behaupten nicht, diese Probleme seien verschwunden. Sie ändern, was sie zu deuten versuchen.

## Was ein Neuron schreibt

Bei einem Neuron in einem mehrschichtigen Perzeptron sind hier zwei Größen wichtig. Die Aktivierung bestimmt, wie stark es in einem bestimmten Kontext reagiert. Sein Ausgabevektor gibt die Richtung vor, die es dem Residualstrom hinzufügt. Dieser Vektor bleibt fest, während die Aktivierung positiv oder negativ sein kann.

Die Forscherinnen beschreiben ein Neuron deshalb als Steuervektor, dessen Wirkung vom Kontext abhängt. Frühere Arbeiten untersuchten häufig, welcher Text ein Neuron aktiviert. Die neue Methode fragt zusätzlich, was das Neuron dann schreibt. Mit einem Verfahren namens J-lens lesen die Forscherinnen am Vokabular ab, welche Token durch einen Ausgabevektor wahrscheinlicher werden. Diese Information verbinden sie mit den Kontexten, in denen das Neuron am stärksten reagiert.

Ein Neuron in Llama 3.1 8B Instruct veranschaulicht den Unterschied. Es begünstigt das Token „John“ sowohl bei Eingaben über John the Ripper als auch bei Fragen nach dem Verfasser des vierten Evangeliums. Wer nur die Auslöser der Aktivierung beschreibt, übersieht diese gemeinsame Ausgabe. Auch das Vorzeichen zählt: Derselbe Vektor kann bei positiver und negativer Aktivierung unterschiedliche Bedeutungen tragen.

Das Team prüfte seine Deutungen durch Eingriffe ins Modell. Es unterdrückte einzelne Aktivierungen, fügte Ausgabevektoren in anderen Schichten ein und steuerte damit das Verhalten. In der untersuchten Stichprobe trug ein Neuron in höchstens rund 1 % der Fälle zwei voneinander unabhängige Konzepte zum Residualstrom bei. Über die meisten Schichten hinweg behielten die Ausgabevektoren zudem ungefähr dieselbe Bedeutung.

Ein Neuron kann also durchaus auf viele verschiedene Texte und Kontexte reagieren. Die engere Aussage betrifft das, was es zum nächsten Rechenschritt beiträgt. Damit können die Autorinnen die Befunde zu schwer deutbaren Aktivierungsmustern berücksichtigen und zugleich begründen, warum sich die eingeschriebene Richtung dennoch deuten lässt.

## Auch verteiltes Faktenwissen lässt sich deuten

Ein zweiter Einwand betrifft den Abruf von Fakten. Wer ein einzelnes Neuron verändert, löscht selten eine bestimmte Tatsache, denn Wissen ist im Modell über viele Pfade verteilt. Die Arbeit von Anthropic bestätigt diese Verteilung. Veränderten die Forscherinnen genügend Neuronen, um eine falsche Antwort auf eine Faktenfrage zu bewirken, standen die betroffenen Neuronen meist für Konzepte, die mit dem fraglichen Sachverhalt zusammenhingen.

Die Verteilung machte die Pfade also nicht beliebig. Mehrere für sich deutbare Beiträge konnten gemeinsam eine Antwort stützen. Das ist für die Wahl der Analysewerkzeuge wichtig: Einfache Einheiten erscheinen oft zu grob. Erlernte Merkmalswörterbücher erfordern dagegen zusätzliches Training und eigene Entscheidungen über ihre Ausgestaltung.

Als Antwort auf dieses Problem haben sich unter anderem Sparse Autoencoder etabliert. Aus den Aktivierungen eines Modells lernen sie eine größere Menge von Merkmalen, von denen jeweils nur wenige aktiv sind. So sollen sich Konzepte trennen lassen, die gewöhnliche Neuronen verbinden. Anthropic selbst hatte mit solchen Merkmalen bereits Aktivierungen in Claude kartiert. Shone und Dunlap stellen Sparse Autoencoder nicht grundsätzlich infrage. Sie untersuchen, ob die vorhandenen Neuronen für manche der gleichen praktischen Zwecke ausreichen, ohne erst eine weitere Darstellung zu trainieren.

## Von der Beschreibung zum Sicherheitswerkzeug

Der zweite Bericht prüft drei Anwendungen: Erkennung, Steuerung und Audit. Für die Erkennung wählte das Team Neuronen anhand von Aktivierungsbeispielen, automatisch erstellten Beschreibungen und ausgelesenen Ausgaben aus. Die daraus gebildeten Sonden übertrafen auf den meisten Testdatensätzen die Textsuche. Auf vier von 16 Datensätzen erreichten sie das Niveau linearer Sonden, die mit 400 beschrifteten Beispielen trainiert worden waren. Beim Auffinden schädlicher Inhalte schnitten sie in elf von 17 Themengebieten besser ab als die Textsuche.

Trainierte Klassifikatoren sind damit nicht generell überholt. Laut Bericht schneiden trainierte Sonden meist besser ab. Interessant ist der Vergleich, wenn noch keine Beispiele für das gesuchte Konzept vorliegen: Die Neuronenmethode braucht dafür keinen beschrifteten Trainingsdatensatz. Prüfer könnten so mit einem Audit beginnen, bevor sie Beispiele gesammelt haben.

Für die Steuerung nutzten die Forscherinnen die Ausgabevektoren von Neuronen, um einen Chatbot zu einem vorgegebenen Verhalten zu bewegen. Neuronen, die anhand ihrer ausgelesenen Ausgaben und Aktivierungsbeschreibungen ausgewählt wurden, lösten das Verhalten in 21 % der Antworten aus. Trainierte Steuervektoren erreichten dieselbe Quote. Absolut gesehen ist sie bescheiden. Der Versuch prüft aber, ob die feste Ausgabe des Neurons tatsächlich etwas bewirkt und über eine bloße Korrelation mit einem Konzept hinausgeht.

Das Auditexperiment vergleicht anschließend ein feinabgestimmtes Modell mit seinem Basismodell. Das Team untersuchte Versuchssysteme für Hintertüren, von selbst auftretende Fehlanpassung und unterschwelliges Lernen. Nach der Feinabstimmung stieg tendenziell die Aktivierung von Neuronen, deren Ausgabevektoren bereits auf das neue Verhalten ausgerichtet waren. Der Adapter nutzte also oft vorhandene Richtungen im Basismodell, ohne dafür ein ganz neues internes Vokabular zu entwickeln.

Dieses Muster gab dem Prüfsystem einen Anhaltspunkt. Das auf Claude basierende Audit steuerte das Modell entlang der bei der Anpassung entstandenen Änderungsrichtungen und las die darauf ausgerichteten Neuronen aus. So benannte es drei Viertel der versteckten Verhaltensweisen. Allein mit Stichproben aus den Ausgaben blieb die Mehrheit unentdeckt.

## Wenn Verlernen eine Antwort nur verbirgt

Die Autorinnen wandten ihr Verfahren auch auf 23 öffentlich zugängliche Modellstände an, denen gefährliches Cybersicherheitswissen aus WMDP abtrainiert worden war. Der Vergleichstest umfasst 1.987 Multiple-Choice-Fragen, deren Antworten Cyberangriffe unterstützen könnten. Ein Verfahren zum Verlernen soll den Zugriff auf die zugrunde liegenden Informationen beseitigen und zugleich unabhängige Fähigkeiten erhalten.

Bei 14 der 23 Modellstände stand im Lückentextverfahren weiterhin die korrekte Antwort an erster Stelle. Das galt für die meisten Fragen, die das Basismodell richtig beantwortet hatte. Die sichtbare Trefferquote im Multiple-Choice-Test konnte also sinken, während ein anderes Ausleseverfahren die Antwort noch fand. Die Forscherinnen sehen darin einen Hinweis, dass viele Methoden das Wissen hinter einem erlernten Antwortmechanismus verbargen, ohne es zu entfernen.

Die Aussage ist eng begrenzt. WMDP ist ein Vergleichstest, und Lückentexte sind nur eine Möglichkeit, verbliebenes Wissen abzufragen. Wenn ein Modell ein Token richtig einordnet, muss es nicht jede damit verbundene praktische Fähigkeit behalten haben. Der Versuch zeigt dennoch, warum ein einzelner Verhaltenswert nicht belegen kann, dass eine Information verschwunden ist.

## Ein Ausgangspunkt für die Analyse

Die beiden Berichte untersuchen hauptsächlich Modelle mit offenen Gewichten, bei denen sich Neuronen und feinabgestimmte Modellstände direkt vergleichen lassen. Die verborgenen Verhaltensweisen sind in kontrollierten Versuchssystemen angelegt. Im praktischen Einsatz treffen größere Modelle auf Werkzeuge, Systemprompts und Schutzmechanismen, die dieselben Signale verdecken könnten.

Auch die Beschreibung der Neuronen hängt von Beispielen und Ausleseverfahren ab. Selbst ein gut deutbarer Ausgabevektor garantiert nicht, dass ein Prüfer das richtige Neuron findet. Die Detektoren ohne Trainingsbeispiele bleiben meist hinter überwacht trainierten Sonden zurück. Die Autorinnen betrachten Neuronen als nützliche Analyseeinheiten. Eine vollständige Erklärung der Denkprozesse beanspruchen sie damit nicht.

Der praktische Gewinn liegt in einer kostengünstigeren ersten Prüfung. Den festen Ausgabevektor bringt das Modell schon mit. Er lässt sich auslesen, verschieben, unterdrücken und vergleichen, bevor der Prüfer ein Merkmalswörterbuch trainiert oder einen beschrifteten Datensatz zusammenstellt.

Wieder vor den beiden Modellkopien, erreicht der Prüfer die Neuronen, die seit der Feinabstimmung stärker reagieren. Ihre Ausgabevektoren wiesen schon auf das versteckte Verhalten hin, bevor es den Adapter gab. Geändert hat sich weniger das Konzept als der Zeitpunkt, zu dem das Modell auf eine vertraute Richtung zurückgreift.

## Quellen

- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections” — https://alignment.anthropic.com/2026/neuron-basis-theory/
- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 2: Using Neurons For Safety Applications” — https://alignment.anthropic.com/2026/neuron-basis-applications/
- Trenton Bricken et al., “Towards Monosemanticity: Decomposing Language Models With Dictionary Learning” — https://transformer-circuits.pub/2023/monosemantic-features/index.html
- Nicholas Carlini et al., “WMDP: Measuring and Reducing Malicious Use With Unlearning” — https://arxiv.org/abs/2403.03218

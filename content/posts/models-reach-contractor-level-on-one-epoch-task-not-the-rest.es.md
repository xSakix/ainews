+++
title = "Los modelos igualan a un contratista solo en una tarea de Epoch"
slug = "modelos-igualan-a-un-contratista-solo-en-una-tarea-de-epoch"
description = "La prueba comparativa actualizada de trabajo real de Epoch AI muestra que Fable 5.2 y Opus 5.5 igualan a un contratista en el análisis de centros de datos, en una fracción de las horas. Ningún modelo alcanza el estándar de un empleado en ninguna tarea, y Epoch afirma que sopesa destinar el tiempo de los contratistas a revisar los resultados de la IA."
tags = ["business", "research", "agents"]
date = 2026-11-18T03:14:41+01:00
draft = false
+++

La tarea llega en un espacio de trabajo con una guía, un conjunto de herramientas y un único nombre: EcoDataCenter 1. El modelo debe añadir ese complejo a la base de datos de centros de datos de IA de Epoch AI. Lee noticias y documentación regulatoria, solicita imágenes satelitales y luego anota las fotografías: contornos verde azulado para edificios, azul para unidades de refrigeración y púrpura para generadores de respaldo. Un contratista suele dedicar unas 16 horas a cada emplazamiento.

En el informe de Epoch del 17 de noviembre, dos de los modelos que realizaron este trabajo produjeron resultados que el propio analista de centros de datos de la organización consideró comparables a los de un contratista. Un tercero cubrió solo parte de lo que mostraban sus fuentes.

## Qué puso a prueba Epoch

Epoch AI es una organización de investigación que sigue la trayectoria de la IA. Su prueba comparativa (*benchmark*) Epoch Automation Reports toma tareas del propio trabajo de la organización y las entrega a los modelos con el contexto que recibiría una nueva incorporación. Después, el personal de Epoch califica a mano los resultados. Una puntuación del 100 % representa el estándar que Epoch exige a sus empleados. La primera versión, publicada el 8 de octubre, evaluó seis modelos en 11 tareas distribuidas en cinco categorías: diseño gráfico, Data Insights (artículos breves sobre tendencias de la IA), Data Explorers, investigación de centros de datos y diseño de investigación. Halló que los líderes, Claude Fable 5.1 y GPT-6 Astra, rendían con fiabilidad en tareas bien definidas y fallaban en las partes abiertas del trabajo.

El nuevo informe, elaborado por la investigadora de Epoch Kelly Hong, evalúa a Claude Fable 5.2 y GPT-6.2 Astra, junto con otros cuatro modelos, sobre un conjunto actualizado. Epoch modificó varios aspectos a la vez. Sustituyó una tarea abierta de evaluación comparativa —que, según indica, tenía un presupuesto demasiado bajo para tantas direcciones plausibles— por una prueba de trabajo retirada que antes se entregaba a candidatos a un puesto. Añadió recursos a los *prompts* (instrucciones), incluida una versión condensada de su canal interno de Slack sobre centros de datos. Y trasladó la calificación a una escala del 1 al 4 por criterio, más próxima al modo en que se revisan artículos de congresos.

El resultado principal muestra una divergencia. Fable 5.2 y GPT-6.2 Astra prácticamente empatan en un récord dentro del Epoch Capabilities Index. En las tareas de trabajo real, GPT-6.2 Astra promedió un 65 %, 17 puntos por debajo de Fable 5.2. Ningún modelo alcanzó el estándar de un empleado en ninguna tarea.

## Dónde igualaron los modelos a un contratista

La excepción es la tarea de centros de datos. Fable 5.2 obtuvo un 97,5 % y Opus 5.5 logró un 87,5 %, frente al 65 % de GPT-6.2 Astra. Una puntuación perfecta implica que Epoch podría publicar el resultado sin cambios. Epoch define el nivel de contratista como un trabajo que su analista consideró comparable al que entregan los contratistas, el cual suele requerir también cierta revisión antes de publicarse.

Los fallos restantes eran del tipo que corrige un revisor. Las anotaciones de imagen de Fable 5.2 eran imperfectas y su texto resultaba demasiado largo. Opus 5.5 necesitó correcciones en la clasificación de equipos y ajustes más profundos en sus anotaciones. En la investigación principal, según Epoch, ambos cumplieron su listón de calidad, con fuentes creíbles y juicios bien calibrados.

Las cifras de coste son la parte que incide sobre el empleo. Opus 5.5 terminó en poco menos de 3 horas, por un coste inferior al de un contratista. Fable 5.2 tardó unas 6,5 horas y costó más que un contratista, a cambio de un mejor resultado. Epoch escribe que ahora está «sopesando trasladar el tiempo de los contratistas a la revisión de resultados de la IA y a otras partes de nuestro análisis de centros de datos de IA». El informe no afirma que ningún contratista haya perdido trabajo, y la tarea consiste en un único registro de base de datos con una guía detallada, no en un puesto completo.

La misma tarea muestra cómo falló el tercer modelo. Las fuentes de GPT-6.2 Astra apuntaban a varios edificios de IA en el complejo, pero solo cubrió uno alegando falta de pruebas explícitas. Después omitió sus estimaciones de cómputo y chips porque quería una fuente independiente para cada cifra que las alimentaba. Epoch indica que la guía habría llevado al modelo a elaborar esas estimaciones. Gemini 4 Argon erró en sentido contrario: asumió que todos los edificios utilizaban chips Nvidia B200 cuando solo uno de ellos lo había hecho público. Epoch señala que espera que los contratistas eviten este tipo de errores.

## Dónde siguen fallando

Fuera de la tarea de centros de datos, el informe vuelve al patrón de octubre. Los modelos tienen dificultades para diseñar experimentos, iterar y juzgar qué hallazgo importa.

En una tarea adaptada de una prueba retirada para candidatos, se pidió a los modelos que midieran en qué medida la IA maneja situaciones distintas a sus datos de entrenamiento, utilizando variantes de ajedrez. Todos los modelos emplearon variantes que ya existen. Epoch señala que Gemini 4 Argon incluso ejecutó un experimento que mostraba que los modelos conocían las variantes que había elegido, y aun así siguió adelante. La variante inventada por GPT-6.2 Astra se limitaba a intercambiar los nombres de las piezas. Opus 5.5 y Fable 5.1, de Claude, presentaron como nueva una conocida pieza de ajedrez heterodoxo, el camello, y la variante «Kingsgate» de Fable 5.2 se juega exactamente igual que otra ya existente llamada «Midline Invasion».

En una tarea sobre ocultar mensajes en imágenes SVG, Fable 5.2 se conformó con su primer prompt de codificación, que generó imágenes donde el mensaje aparecía en su mayor parte a simple vista. Los investigadores humanos que iteraron sobre el prompt lograron codificaciones verdaderamente ocultas, como estrellas cuyas alturas representan letras. En una tarea abierta de Data Insight, GPT-6.2 Astra eligió un tema que Epoch juzgó demasiado restringido para su público: la eficiencia de la tokenización del idioma chino en dos modelos concretos. Epoch afirma que no encontró aquí ninguna mejora relevante respecto a GPT-6 Astra, que había escogido el hecho ya bien conocido de que los modelos abiertos populares utilizan arquitecturas de mezcla de expertos (*mixture-of-experts*).

También falló la presentación. El informe de ajedrez de GPT-6.2 Astra abría con un hallazgo en negrita que sus propios resultados posteriores contradecían. Epoch afirma que un defecto de ese calibre detendría la publicación con independencia del valor de la investigación.

## Los modelos se evalúan a sí mismos

Epoch añadió una prueba de autoevaluación. Allí donde disponía de un resultado humano que cumplía su estándar, mostró al modelo ambas versiones, sin etiquetas, junto con la rúbrica de calificación. Todos los modelos prefirieron su propio resultado, salvo que Gemini 4 Argon eligió en una ocasión el humano. Epoch afirma que las justificaciones exageraban pequeños defectos del trabajo humano y premiaban un rigor superficial, como el número de experimentos ejecutados. La única excepción de Argon llegó al razonamiento que usaría la propia Epoch: el trabajo humano ejecutaba un experimento limpio orientado a la pregunta central, mientras que sus propios experimentos parecían «superficialmente más formales». Epoch señala que si los modelos pudieran hacer esto de forma fiable podrían cumplir sus estándares, pero que esa no fue la norma.

## Qué permiten concluir las cifras

Epoch enumera sus propios límites. Cada modelo ejecutó cada tarea una sola vez, la calificación es manual y parcialmente subjetiva, y los cambios en el diseño hacen que las puntuaciones solo sean comparables a grandes rasgos con las de octubre. Algunos modelos anteriores volvieron a ejecutarse y otros no. La organización recomienda a los lectores fiarse más de los hallazgos cualitativos que de las puntuaciones exactas, y señala que los resultados no miden lo que la IA puede hacer en el conjunto del trabajo. Las tareas son propias de Epoch, calificadas por su personal, y dos de los tres modelos líderes pertenecen a Anthropic. Una nota a pie de página añade que GPT-6.2 Astra fue evaluado y analizado estrictamente dentro del equipo interno de Epoch.

Leído con esos límites, el informe describe una franja estrecha de trabajo que ha avanzado. Una tarea con una guía extensa, fuentes públicas y un resultado verificable se realiza ahora a un nivel que un analista humano pasaría a un revisor. Las tareas que dependen de elegir la pregunta, advertir que un resultado es trivial o explicar al lector qué importa siguen sin alcanzarlo. Incluso el resultado de Opus 5.5, el más barato de los dos buenos, llegó con anotaciones que requerían correcciones sustanciales, y esas correcciones quedaron en manos de una persona con la imagen satelital abierta.

## Referencias

- Hong, K. (2026). *How good are Fable 5.2 and GPT-6.2 Astra at real work?* Epoch AI. https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work
- Epoch AI (2026). *Can AI automate Epoch?* https://epoch.ai/publications/can-ai-automate-epoch

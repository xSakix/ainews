+++
title = "Los modelos visuales razonan sobre creencias cuando ven bien"
slug = "modelos-visuales-razonan-creencias-cuando-ven-bien"
description = "Siete modelos de visión y lenguaje perdieron más de 20 puntos cuando los problemas de falsa creencia pasaron del texto a las imágenes. Un estudio controlado halló que la percepción, y no el último paso de razonamiento, causaba la mayor parte de la brecha."
tags = ["research", "models"]
date = 2026-11-10T04:04:14+01:00
draft = false
+++

Un niño observa una breve escena en una pantalla. Una pelota roja está en un cajón. Un personaje se marcha y otro mueve la pelota a una caja. Cuando el primero regresa, el niño sabe que buscará en el cajón. Ahora un modelo de visión y lenguaje ocupa el lugar del niño. El modelo puede explicar una falsa creencia mediante texto, pero el objeto que se mueve en la pantalla cambia su respuesta. Esta escena es ilustrativa: describe el tipo de tarea que aísla un nuevo estudio.

## La brecha visual

Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall y sus colegas probaron siete modelos de visión y lenguaje en problemas de falsa creencia. Su prepublicación, aceptada en la sección Evaluations and Datasets de NeurIPS 2026, informa de más de 159 000 llamados a la API en un protocolo de cinco condiciones. Los modelos que se acercaban al rendimiento humano en las versiones textuales perdían más de 20 puntos porcentuales cuando el mismo problema subyacente se presentaba visualmente.

Las pruebas de falsa creencia tienen una larga historia en psicología. Preguntan si un sujeto puede separar la realidad del conocimiento que otra persona tiene de ella. En el esquema habitual, un objeto se mueve mientras un personaje está ausente. La respuesta correcta exige predecir lo que cree ese personaje, aunque el sujeto sepa dónde está realmente el objeto.

Los modelos de lenguaje recientes suelen rendir bien en versiones textuales. Michal Kosinski evaluó once modelos de lenguaje en cuarenta tareas de falsa creencia diseñadas a medida e informó de que una versión de GPT-4 de 2023 resolvía el 75 %. Una comparación independiente de James Strachan y sus colegas halló que algunos modelos de lenguaje igualaban o superaban el rendimiento humano en varias pruebas de teoría de la mente. Ambos artículos también advirtieron de que una respuesta correcta no demuestra que un modelo razone sobre las mentes del mismo modo que una persona. Los patrones memorizados, la estructura de la tarea y las pistas lingüísticas siguen siendo explicaciones alternativas.

El entorno visual añade otra dependencia. Antes de que un modelo pueda razonar sobre lo que cree un personaje, debe identificar los personajes, objetos, lugares y cambios que determinan esa creencia. Por tanto, una respuesta errónea podría proceder del razonamiento social, de la percepción o de la conexión entre ambos. Una sola puntuación no permite distinguir esos fallos.

## Cinco vistas del mismo problema

Barhdadi y sus colegas diseñaron cinco condiciones que conservan el objetivo del razonamiento y modifican la calidad y la forma de las pruebas perceptivas. La intervención importante proporcionaba a los modelos descripciones veraces de la escena. Con ese apoyo, gran parte de la brecha entre texto e imagen desaparecía. La misma corrección no se producía cuando analizadores automáticos generaban las descripciones, incluso si incluían modelos de visión y lenguaje de vanguardia.

Ese contraste sitúa el obstáculo inmediato. Los modelos a menudo podían usar una descripción simbólica precisa de la escena para inferir la creencia del personaje ausente. Fallaban cuando debían producir esa descripción a partir de los píxeles por sí mismos. Mejorar las instrucciones de la pregunta final no recuperaría información que el procesamiento visual inicial ya hubiera omitido o distorsionado.

El patrón de errores respalda la misma conclusión. El sesenta por ciento de los fallos de falsa creencia mostraba un sesgo hacia la realidad: el modelo respondía con la ubicación real del objeto en lugar de aquella que recordaría el personaje ausente. Esto se asemeja a una incapacidad para mantener separadas dos representaciones. Una describe la escena actual; la otra, la escena que el personaje observó por última vez.

El sesgo hacia la realidad puede parecer un fallo de razonamiento social porque la respuesta final ignora la perspectiva del personaje. Las condiciones controladas muestran que el modelo quizá nunca construyó una representación utilizable de esa perspectiva. Si un analizador dice que un personaje vio el movimiento, o no detecta el momento en que se marchó, el paso posterior de razonamiento recibe el problema equivocado.

El apoyo de los autores basado en descripciones veraces es diagnóstico, no una solución lista para desplegar. Los sistemas reales rara vez reciben descripciones perfectas de las escenas. Un asistente que observa un lugar de trabajo, un robot que actúa cerca de personas o un sistema de tutoría que sigue una demostración debe decidir qué acontecimientos presenció cada persona. Esos sistemas no pueden suponer que un humano ya convirtió el video en los hechos exactos que importan.

## Una prueba comparativa para la frontera

Las pruebas anteriores de teoría de la mente visual ya mostraban que los sistemas multimodales tienen dificultades con las intenciones, las creencias y las presentaciones engañosas. El nuevo protocolo añade una separación más precisa entre ver e inferir. Pregunta si el modelo puede resolver el problema de razonamiento cuando la percepción se mantiene constante y después mide qué ocurre al cambiar el apoyo perceptivo.

Esa separación importa para la ingeniería. Un equipo que observa un error de falsa creencia podría añadir trazas de razonamiento más largas o un modelo de lenguaje mayor. El estudio sugiere una primera prueba distinta: dar al sistema una representación verificada de la escena. Si la respuesta pasa a ser correcta, el trabajo debería centrarse en el seguimiento de objetos, el análisis de acontecimientos y la memoria específica de cada perspectiva. Si el error persiste, entonces necesita atención el componente que razona sobre las creencias.

El resultado también limita las afirmaciones generales sobre la inteligencia social de las máquinas. Las pruebas textuales pueden establecer que un modelo asocia un escenario escrito a una respuesta esperada. No demuestran que el sistema pueda reconstruir el escenario pertinente a partir de un mundo físico cambiante. Un modelo que habla de la creencia de otra persona después de leer un párrafo claro solo ha completado la segunda mitad del trabajo.

El artículo proporciona código y datos, lo que permite ampliar sus condiciones. La comparación de siete modelos que presenta sigue siendo una prueba de laboratorio acotada. No mide todos los modelos visuales, todas las formas de inferencia social ni el rendimiento en videos no controlados. La prepublicación no ha pasado una revisión por pares en una revista, aunque su aceptación en la sección de la conferencia le proporciona un foro formal.

De vuelta al niño y la pelota del ejemplo, un ingeniero da al modelo una línea adicional: el primer personaje se marchó antes de que la pelota se moviera. El modelo ahora predice el cajón. Su razonamiento parece mejor, aunque quizá el mecanismo de razonamiento no haya cambiado en absoluto. La pieza que faltaba era el acontecimiento que el modelo no logró ver.

## Referencias

- Barhdadi, M. R., Wasim, S. T., Gall, J., Serpedin, E., & Kurban, H. (2026). *Perception, Not Reasoning, Limits Visual Theory of Mind*. https://arxiv.org/abs/2611.10694
- Kosinski, M. (2024). *Evaluating large language models in theory of mind tasks*. https://doi.org/10.1073/pnas.2405460121
- Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). *Testing theory of mind in large language models and humans*. https://doi.org/10.1038/s41562-024-01882-z

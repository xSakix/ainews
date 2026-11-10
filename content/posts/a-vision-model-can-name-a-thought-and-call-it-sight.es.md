+++
title = "Un modelo visual puede nombrar un pensamiento y decir que lo vio"
slug = "modelo-visual-nombrar-pensamiento-decir-que-lo-vio"
description = "Los investigadores inyectaron conceptos en seis modelos de visión y lenguaje y pidieron a cada uno separar pensamiento y percepción. Un modelo podía identificar el concepto oculto, pero su explicación del origen cambiaba con el prompt, la imagen y el punto de inyección."
tags = ["research", "models", "safety"]
date = 2026-11-09T04:10:00+01:00
draft = false
+++

En una mesa de trabajo imaginaria, una investigadora de interpretabilidad muestra a un modelo visual un cuadrado gris uniforme. Dentro del modelo añade una dirección matemática para «perro» mientras prepara su respuesta. La pantalla no contiene ningún animal. El modelo responde que se ve un perro. La investigadora es ficticia, pero la intervención y el error proceden de un nuevo estudio de la University of Southern California.

## Una prueba con dos posibles fuentes

Tina Khezresmaeilzadeh, Seyedarmin Azizi, Mehdi Kamal y Massoud Pedram se preguntaron si un modelo de visión y lenguaje puede distinguir el contenido que entra mediante una imagen del que los investigadores introducen en sus activaciones. Los psicólogos cognitivos llaman monitorización de la realidad a la tarea humana correspondiente: decidir si un recuerdo procede de la percepción o de una experiencia generada internamente.

La distinción añade una nueva exigencia a la introspección de los modelos. Un modelo de texto que identifica correctamente un concepto inyectado ha superado una prueba. Un modelo de visión y lenguaje también debe decir si vio o pensó ese concepto. Una palabra correcta con una fuente equivocada puede convertirse en una descripción falsa de una imagen.

Los investigadores probaron seis modelos de tres familias de modelos de lenguaje. Su principal sujeto fue Gemma-3-27B, que combina un codificador visual SigLIP con un modelo de lenguaje de 62 capas. Cada ensayo utilizó una imagen neutra o una imagen de un objeto. En ocasiones, los investigadores añadieron una dirección conceptual, como «perro» o «avión», a las activaciones internas del modelo.

El modelo tenía que completar tres campos. Nombraba el principal objeto visible, informaba de si se había inyectado un pensamiento e identificaba ese pensamiento. El diseño permitió distinguir varios resultados que una puntuación ordinaria de precisión mezclaría: detectar una perturbación, identificar su contenido y atribuir ese contenido a la fuente correcta.

## Un modelo encontró el pensamiento

Gemma-3-27B produjo el resultado completo y correcto en el 34,7 % de 150 ensayos de conceptos con la capa y la intensidad seleccionadas. Informaba de una inyección, identificaba el concepto y no afirmaba que fuera visible. La coincidencia exacta de palabras dio un 31,3 %, mientras un modelo evaluador independiente dio un 33,3 %.

La tasa de falsas alarmas fue baja. En 972 ensayos sin inyección, Gemma solo informó de una en tres ocasiones. Las direcciones aleatorias no produjeron ninguna identificación correcta. En 100 conceptos que no se habían utilizado para elegir los ajustes de intervención, la identificación completa y correcta llegó al 33 %. Por tanto, el resultado no dependía solo de los conceptos utilizados para ajustar la prueba.

La intervención de dirección ordinaria fue un control más exigente. Los investigadores aplicaron el mismo impulso interno, pero no mencionaron pensamientos inyectados. Preguntaron por el objeto visible y la primera palabra que viniera a la mente. Gemma nombró exactamente el objetivo en el 3,3 % de esos ensayos, muy por debajo de la puntuación de introspección. Preguntar por el contenido interno cambió lo que el modelo podía comunicar.

El resultado amplía un trabajo que Jack Lindsey publicó en 2025 sobre modelos Claude exclusivamente textuales. Ese estudio inyectó representaciones de conceptos conocidos y halló que los modelos más potentes a veces podían identificar el contenido de la intervención con pocas falsas alarmas. Un trabajo anterior de Felix Binder y sus colegas había abordado la introspección mediante la autopredicción: un modelo aprendía a predecir su propio comportamiento mejor que otro modelo. El experimento de USC controló el acontecimiento interno y añadió visión, donde la fuente del contenido se vuelve observable.

El efecto no se generalizó claramente entre modelos. Qwen3-VL-8B informó de una inyección en el 61,3 % de sus ensayos de conceptos, pero solo identificó exactamente el concepto en el 3,3 %. Los demás modelos probados identificaban poco, producían muchos informes falsos o no superaban la comparación con la intervención de dirección. El artículo establece, por tanto, un comportamiento en una configuración de un modelo, no una propiedad general de los sistemas de visión y lenguaje.

## La etiqueta de origen falló primero

Incluso los informes correctos de Gemma eran frágiles. Con la intensidad de intervención seleccionada, describía el concepto inyectado como visible en el 22,7 % de los ensayos con imagen gris. Aumentar la intensidad elevó esa atribución visual errónea al 51 %.

Pequeños cambios en la pregunta también alteraban la respuesta. Eliminar una frase que separaba explícitamente el pensamiento inyectado de la imagen redujo la introspección completa y correcta del 34,7 al 10 % y elevó los informes de que el concepto era visible del 23 al 65 %. Preguntar si había ocurrido una inyección antes de preguntar qué era visible redujo a cero la introspección completa y correcta en la configuración probada.

El punto de entrada también importaba. Cuando los investigadores inyectaban una dirección conceptual visual en posiciones de tokens de imagen, Gemma solía tratarla como visión. En la capa 21 del modelo de lenguaje, informaba de que el concepto objetivo era visible en el 47–49 % de los ensayos y casi nunca etiquetaba el contenido como inyectado. Las perturbaciones aleatorias en las mismas posiciones causaban informes de anomalías sin producir un concepto coherente. El modelo podía advertir algo inusual y, al mismo tiempo, aceptar contenido con significado como parte de la imagen.

Un objeto real creaba otro problema. Cuando Gemma recibía en la imagen un objeto no relacionado, la identificación completa y correcta del pensamiento inyectado caía del 34,7 al 2,7 %. El modelo seguía conservando cierta información sobre el concepto, pero la evidencia visual cambiaba si comunicaba esa información y dónde la situaba.

Estos fallos se parecen a un problema que Marcia Johnson y Carol Raye describieron en la investigación sobre memoria humana en 1981. Su marco de monitorización de la realidad trata los juicios de origen como inferencias a partir de las características de una experiencia, no como etiquetas perfectas adheridas a los recuerdos. El artículo de USC no afirma que un transformer utilice el mecanismo humano. Toma prestada la distinción porque el experimento también exige que un sistema separe el contenido externo del generado internamente.

## De un impulso interno a una descripción falsa

Los investigadores eliminaron después toda mención de pensamientos inyectados y pidieron a Gemma describir 108 fotografías del conjunto COCO. Cada fotografía se emparejó con un objeto objetivo que, según sus anotaciones, estaba ausente.

Sin intervención, ninguna descripción mencionó el objetivo. Tampoco lo hicieron una dirección aleatoria ni un concepto no relacionado. Inyectar el objetivo en posiciones de respuesta hizo que apareciera en el 5 % de las descripciones con la intensidad menor y en el 42 % con la mayor. Añadir una dirección conceptual visual a los tokens de imagen hizo que el 87 % mencionara el objeto ausente.

Las preguntas de sí o no eran menos sensibles. Sin inyección, Gemma respondió erróneamente que el objeto ausente estaba presente en el 7 % de las fotografías. Las intervenciones elevaron la tasa al 12–19 %, pero las direcciones aleatorias y no relacionadas produjeron cambios similares. El resultado de las descripciones seguía al propio concepto de manera mucho más específica.

Ese contraste conecta el trabajo con la investigación sobre alucinaciones de objetos. Yifan Li y sus colegas introdujeron la evaluación POPE en 2023 tras descubrir que los modelos de visión y lenguaje describen objetos ausentes, especialmente aquellos que aparecen con frecuencia en sus datos de instrucciones o junto a objetos presentes. El nuevo artículo no demuestra que las alucinaciones naturales surjan por la misma vía interna. Su inyección conceptual es artificial. Muestra una posible vía y una advertencia para la medición: una breve pregunta factual puede no detectar un concepto que sí aparecerá en una descripción libre.

Las limitaciones son importantes. El análisis más profundo de las intervenciones se centra en Gemma-3-27B, el conjunto de conceptos consiste en sustantivos concretos y una sola persona auditó la muestra de puntuación. La redacción del prompt cambió mucho los resultados. Las tasas medidas describen modificaciones controladas de activaciones, no el funcionamiento ordinario del modelo ni la experiencia consciente.

La conclusión práctica es más acotada y útil. Los evaluadores deberían puntuar tanto lo que informa un modelo multimodal como el origen que atribuye a ese contenido. Un sistema puede detectar un estado oculto sin ofrecer un relato fiable de su procedencia.

De vuelta a la investigadora inventada ante el cuadrado gris, repite el ensayo, pero ahora pregunta por la inyección antes que por la imagen. El concepto no ha cambiado, ni tampoco la pantalla. La respuesta sí. Su cuaderno necesita columnas separadas para la palabra, la fuente y la pregunta exacta, porque una sola marca de «correcto» ocultaría el fallo.

## Referencias

- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. https://arxiv.org/abs/2410.13787
- Johnson, M. K., & Raye, C. L. (1981). *Reality Monitoring*. https://doi.org/10.1037/0033-295X.88.1.67
- Khezresmaeilzadeh, T., Azizi, S., Kamal, M., & Pedram, M. (2026). *Did I See It or Think It? Probing Reality Monitoring in Vision-Language Models with Concept Injection*. https://arxiv.org/abs/2611.09014
- Li, Y., Du, Y., Zhou, K., Wang, J., Zhao, W. X., & Wen, J. R. (2023). *Evaluating Object Hallucination in Large Vision-Language Models*. https://aclanthology.org/2023.emnlp-main.20/
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://arxiv.org/abs/2601.01828

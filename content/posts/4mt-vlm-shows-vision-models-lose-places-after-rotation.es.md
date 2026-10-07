+++
title = "4MT-VLM: los modelos visuales pierden lugares tras un giro"
description = "Un preprint adapta una prueba clínica de memoria espacial a 16 modelos de visión y lenguaje. Todos pueden reconocer un paisaje desde el ángulo que estudiaron, pero la mayoría acaba adivinando cuando se mueve la cámara."
slug = "4mt-vlm-modelos-visuales-pierden-lugares-tras-un-giro"
tags = ["research", "models"]
date = 2026-10-06T04:02:31+02:00
draft = false
+++

Los modelos de visión y lenguaje reconocen un paisaje desde el ángulo en que lo vieron por primera vez, pero la mayoría no puede identificarlo cuando se mueve la cámara, según 4MT-VLM, una nueva prueba comparativa adaptada de una prueba clínica de memoria espacial.

Markus Frey, de Fraunhofer IAIS, un instituto alemán de investigación aplicada, planteó a 16 modelos abiertos y cerrados el ejercicio utilizado con pacientes humanos: estudiar un paisaje de cuatro cumbres renderizado por ordenador y después encontrarlo entre cuatro paisajes similares mostrados desde un ángulo nuevo. Un voluntario humano resolvió aproximadamente cuatro de cada cinco pruebas con rotación. La mayoría de los modelos no superó el azar.

## Por qué importa {#why-it-matters}

Un ingeniero de robótica que utiliza un modelo de visión y lenguaje como ojos de un robot móvil necesita precisamente esta capacidad: reconocer una habitación después de que el robot haya girado. El preprint observa que ni los modelos más grandes ni las instrucciones más detalladas la proporcionan.

## El reconocimiento se mantiene, la rotación falla

La prueba comparativa adapta el Four Mountains Test, que utilizan los médicos porque las puntuaciones disminuyen con las lesiones del hipocampo y en las fases tempranas del alzhéimer. Los colores, las texturas y la iluminación cambian entre la imagen de estudio y las imágenes de prueba en cada ensayo, por lo que incluso uno sin rotación no puede resolverse comparando píxeles. Frey utiliza la precisión en esas pruebas sin rotación para comprobar que un modelo puede identificar el lugar en primer término.

Los modelos superan esa comprobación y después fallan con la rotación. GPT-5.6 Luna de OpenAI respondió correctamente a todas las pruebas sin rotación, pero solo al 31 % de las que incluían rotación, donde el azar acierta una de cada cuatro. Al agrupar los 16 modelos, el peor ángulo fue de 135 grados, con una precisión claramente inferior al azar.

Un giro de 180 grados, el mayor cambio, obtuvo mejores resultados que uno de 135 grados. Frey lo interpreta como una señal de que los modelos utilizan un atajo visual, como comparar con una imagen reflejada de la escena, y no rotan un mapa interno. La comparación humana procede de un solo participante, suficiente para demostrar que la tarea puede resolverse, pero no para ofrecer una media humana.

## Los modelos más grandes reconocen más, pero no rotan mejor

La escala mejoró el reconocimiento y dejó la rotación donde estaba. En la familia Qwen2.5-VL de Alibaba, de entre 3000 millones y 72 mil millones de parámetros, la precisión sin rotación pasó del 30 % al 75 %, mientras que con rotación se mantuvo al nivel del azar o por debajo. La familia InternVL3.5 repitió el patrón entre 1000 millones y 38 mil millones de parámetros. Entre 14 modelos de pesos abiertos de hasta 235 mil millones de parámetros, ninguno respondió correctamente a más del 31 % de las pruebas con rotación, y una variante de «razonamiento» obtuvo la misma puntuación que su versión estándar.

Las instrucciones no cerraron la brecha. Frey ejecutó Qwen2.5-VL-32B con seis prompts, incluidos procedimientos explícitos como imaginar la disposición desde arriba o tomar como referencia la cumbre más distintiva. Los seis lo dejaron por debajo del azar.

## Separar las respuestas incorrectas revela un mapa impreciso

El experimento más informativo solo cambió las respuestas incorrectas. Frey midió, en metros, la distancia entre las cumbres de dos paisajes tras la mejor rotación posible y después volvió a dibujar los tres señuelos a partir de disposiciones más alejadas, manteniendo idénticos el objetivo y los ángulos.

Alejar el señuelo más próximo de unos 7 metros a unos 31 metros elevó a Gemini 3.8 Flash de Google del 39 % al 85 % en las pruebas con rotación y a GPT-5.6 Luna del 31 % al 55 %. Ningún modelo abierto mejoró de forma estadísticamente significativa.

Esa es la evidencia del artículo de que los modelos de vanguardia conservan cierta noción de la disposición, aunque a baja resolución. Un modelo sin mapa no podría beneficiarse de separar los señuelos, y uno con un mapa de nivel humano no necesitaría 30 metros de separación. El efecto se parece a reconocer una localidad desde la ventanilla de un avión, pero no una calle.

Los errores apuntan en la misma dirección. Una persona que responde incorrectamente tiende a elegir el señuelo cuya disposición es más parecida al objetivo. Las respuestas incorrectas de los modelos se repartían casi por igual entre señuelos cercanos y lejanos, como si la disposición no interviniera en la elección.

## Una prueba sintética de un único autor

Los paisajes son imágenes sintéticas renderizadas, y Frey señala que el preentrenamiento con escenas renderizadas similares podría favorecer a algunos modelos. No se divulgan los números de parámetros de los modelos cerrados, por lo que la evidencia sobre la escala se basa solo en modelos abiertos. El preprint, publicado en arXiv el 30 de septiembre de 2026, tiene un único autor y no enlaza código ni un conjunto de datos.

Frey afirma que se está evaluando a más participantes humanos, lo que dará a la puntuación del 82 % del voluntario en las pruebas con rotación un grupo de comparación adecuado.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| 4MT-VLM adapta el Four Mountains Test; 500 pruebas con 100 paisajes generados y 16 modelos evaluados | VERIFICADO | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna; prueba comparativa del propio autor |
| La apariencia se vuelve a generar entre las imágenes de estudio y prueba en todos los ángulos | VERIFICADO | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna; descripción del método |
| Un participante humano respondió correctamente al 100 % de las pruebas sin rotación y al 82 % de las pruebas con rotación | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna; un solo participante |
| GPT-5.6 Luna: 100 % sin rotación, 31 % con rotación; el azar es del 25 % | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |
| La precisión agrupada a 135 grados es del 15,0 % (48/320), inferior al azar; 23 % a 180 grados | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |
| Los modelos utilizan un atajo visual, como la comparación con imágenes reflejadas | ANÁLISIS | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | interpretación del autor del patrón de 135/180 grados |
| Qwen2.5-VL de 3000 millones a 72 mil millones: del 30 % al 75 % sin rotación; 29 %, 31 %, 18 % y 20 % con rotación | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |
| Ningún modelo de pesos abiertos (de 1000 millones a 235 mil millones) supera el 31 % con rotación; la variante de razonamiento iguala a la ajustada con instrucciones con un 19 % con rotación | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |
| Seis estilos de instrucciones dejan a Qwen2.5-VL-32B entre el 13,8 % y el 23,8 %, todos por debajo del azar | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |
| Mediana de distancia al señuelo más próximo de 6,8 m a 31,4 m: Gemini 3.8 Flash del 39 % al 85 %, GPT-5.6 Luna del 31 % al 55 % | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |
| Ningún modelo abierto cambia significativamente al separar más los señuelos | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |
| Los errores de los modelos se distribuyen en 30/37/33 entre los señuelos más cercano, intermedio y más lejano; el humano eligió el más cercano en 10 de 14 errores | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |
| Los modelos de vanguardia conservan una representación imprecisa de la disposición | ANÁLISIS | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | inferencia a partir del resultado de separación de señuelos |
| Preprint de un único autor publicado el 30 de septiembre de 2026; autor de Fraunhofer IAIS; sin código ni datos enlazados | VERIFICADO | [Registro de arXiv](https://arxiv.org/abs/2609.39238) | metadatos de arXiv y dominio del correo del autor |
| Se está evaluando a más participantes humanos | SEGÚN LA EMPRESA | [Preprint de Frey](https://arxiv.org/abs/2609.39238) | ninguna |

+++
title = "La respuesta seguía dentro del modelo"
slug = "respuesta-seguia-dentro-modelo"
description = "Un estudio de 15 modelos de lenguaje encuentra que muchos fallos de memoria de trabajo ocurren después de seleccionar el elemento correcto. Los modelos retienen información decodificable, pero no consiguen comunicarla."
tags = ["research", "models"]
date = 2026-10-16T04:07:00+02:00
draft = false
+++

Un modelo ve una breve lista de símbolos y después una segunda lista lo distrae antes de que deba nombrar el objetivo original. Responde con el distractor. El diagnóstico evidente es que el primer símbolo ha desaparecido. Sin embargo, en esta escena ilustrativa, una sonda interna todavía puede leer el objetivo casi perfectamente. La respuesta no se borró. Algo falló entre conservarla y decirla.

Esa distinción impulsa una nueva prepublicación sobre memoria de trabajo en modelos de lenguaje. Sus autores probaron 15 modelos de entre 70 millones y 14 mil millones de parámetros con tareas diseñadas para crear interferencia. Encontraron que las cabezas de atención seleccionaban a menudo el objetivo correcto incluso cuando la respuesta final era errónea. Sondas sencillas podían decodificar el objetivo de estados ocultos con precisión casi perfecta en muchos fallos.

El resultado cuestiona un atajo habitual en la evaluación: tratar una salida incorrecta como prueba de que falta la información subyacente. El artículo separa tres operaciones que una sola puntuación de precisión mezcla: seleccionar un elemento relevante, conservar su identidad y leerlo como respuesta.

## Un problema controlado de memoria

La memoria de trabajo no es almacenamiento a largo plazo. Es la capacidad temporal de mantener información en un estado utilizable mientras otros materiales compiten por la atención. Los experimentos humanos suelen revelar que el elemento sigue parcialmente disponible aunque un participante comunique el equivocado. Una interferencia similar puede dificultar distinguir dos recuerdos sin destruir ninguno.

Los investigadores construyeron tareas que permitían variar el objetivo, los elementos competidores y sus posiciones. Después miraron dentro de los modelos en los puntos donde debía seleccionarse y transmitirse el objetivo. Los modelos cubrían varias escalas y familias, algo importante porque un patrón en un punto de control puede ser un accidente arquitectónico y no un mecanismo general.

En los ensayos correctos se cumplía la historia esperada: la atención se centraba en el objetivo y las capas finales producían el token correcto. En muchos ensayos incorrectos, la primera mitad seguía cumpliéndose. Las cabezas que seleccionaban el objetivo atendían a la posición correcta. Las sondas de estados ocultos conservaban información suficiente para identificarlo. Sin embargo, la salida reflejaba un competidor.

Una sonda prueba decodificabilidad, no uso. Un clasificador entrenado a posteriori puede extraer información a la que no accede el propio cálculo del modelo. Por eso los autores fueron más allá de leer estados e intervinieron sobre ellos.

## Debilitar a los competidores

La prueba causal clave suprimió representaciones de identidad de elementos no objetivo. La intervención mejoró la sensibilidad, medida como d-prime, en la dirección prevista por una explicación de interferencia. Debilitar a los competidores facilitó que el modelo comunicara el objetivo almacenado.

Eso no significa que cada error de memoria sea un error de lectura. Los modelos pueden no codificar un elemento, perderlo o seleccionar la ubicación incorrecta. La afirmación del artículo es más limitada: una proporción significativa de fallos ocurre mientras la información objetivo sigue disponible internamente, y la confusión entre representaciones similares puede bloquear la respuesta final.

La distinción importa para la ingeniería. Añadir contexto o repetir el objetivo ataca un problema de almacenamiento. Puede ayudar poco cuando el modelo ya lo conserva, pero no puede separarlo del contenido competidor. Un sistema con ese segundo problema puede necesitar otros prompts, estructura intermedia o cambios arquitectónicos que afiancen la identidad en la lectura.

También importa para la interpretación. La atención de los transformers, introducida para relacionar posiciones de una secuencia, suele inspeccionarse como si atender al token correcto resolviera qué sabe el modelo. Aquí puede apuntar al objetivo y aun así no entregar la salida correcta. A la inversa, una respuesta equivocada no implica que la atención no acertara.

## Un parecido humano con límites

Los autores presentan el patrón de interferencia como humano, pero la comparación es funcional y no biológica. Un transformer no necesita un sistema humano de memoria para mostrar la misma separación conductual entre disponibilidad y comunicación. Errores similares pueden surgir de mecanismos muy diferentes.

La escala tampoco disuelve el problema. Probar modelos de hasta 14 mil millones de parámetros muestra que el efecto sobrevive más allá de redes experimentales diminutas, pero no establece el mismo resultado en sistemas de frontera con muchos más parámetros o posentrenamiento propietario. Las tareas son deliberadamente controladas. Las conversaciones reales mezclan recuperación, seguimiento de instrucciones, planificación y generación de formas que dificultan aislar la fuente de un fallo.

Aun así, ese es el propósito de las tareas controladas. Permiten cambiar un competidor, observar una representación y probar una intervención. El artículo ofrece un método para preguntar mejor tras un error: ¿la información nunca se codificó, se perdió o estaba presente pero era inaccesible al proceso de salida?

De vuelta a la tarea ilustrativa de símbolos. El modelo da el elemento equivocado y un evaluador marca un fallo. El veredicto es correcto en la frontera del producto. Internamente, sin embargo, el sistema puede haber hecho la mayor parte del trabajo. El próximo avance quizá no venga de darle más memoria, sino de enseñarle a leer lo que ya conservó.

## Referencias

- Vaswani, A., et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- *Working Memory Readout Bottlenecks in Language Models* (2026). https://arxiv.org/abs/2610.21176

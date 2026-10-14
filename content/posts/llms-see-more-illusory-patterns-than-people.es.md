+++
title = "Los LLM ven más patrones ilusorios que las personas"
slug = "llm-ven-mas-patrones-ilusorios-que-personas"
description = "Una prepublicación encuentra que los modelos de lenguaje infieren relaciones a partir de pruebas ambiguas con más facilidad que los participantes humanos. Sus pruebas controladas conectan el efecto con características internas sensibles a la frecuencia."
tags = ["research", "models"]
date = 2026-10-12T04:01:37+02:00
draft = false
+++

Los modelos de lenguaje formaron patrones falsos más fuertes que las personas cuando se pidió a ambos inferir relaciones a partir de pruebas ambiguas, según una nueva prepublicación.

Los autores adaptaron experimentos clásicos de psicología en los que las observaciones no contienen una asociación fiable, pero las personas a menudo perciben una. Dieron tareas equivalentes a participantes humanos y a varios modelos de lenguaje y luego probaron si estos vinculaban descripciones positivas frecuentes con grupos mayoritarios o construían explicaciones causales a partir de secuencias coincidentes.

## Por qué importa {#why-it-matters}

Para un analista que usa un modelo para interpretar comentarios de encuestas, informes de incidentes o registros de clientes, la búsqueda fluida de patrones puede convertir una muestra desigual en un relato seguro. El estudio sugiere que añadir observaciones no corrige necesariamente el problema cuando la frecuencia bruta impulsa la inferencia.

La comparación central cubre dos formas de percepción ilusoria de patrones. En una, un grupo mayoritario aparece más a menudo y por tanto acumula más ejemplos positivos y negativos aunque las proporciones coincidan con las de un grupo minoritario. En la otra, eventos no relacionados se ordenan de modo que una secuencia causal resulta tentadora, pero no tiene respaldo.

En los experimentos descritos, los modelos eran más propensos que los participantes humanos a aceptar la asociación engañosa o la explicación causal. La magnitud exacta variaba según tarea y modelo, por lo que el resultado útil es la dirección y constancia de la brecha, no un porcentaje universal.

Los investigadores también usaron autocodificadores dispersos, herramientas que convierten la actividad interna densa de un modelo en un conjunto menor de características interpretables. Informan de que las características asociadas con una percepción holística de la frecuencia aumentaban con la respuesta de patrón falso, mientras las asociadas con una orientación más analítica actuaban en sentido contrario. Es una correlación dentro del modelo, no una prueba de que una de las características cause el juicio.

## La comparación es controlada, pero limitada

La fortaleza del artículo es su comparación directa con humanos. Ambos grupos reciben versiones de las mismas pruebas y las tareas derivan de demostraciones establecidas en psicología cognitiva. Los autores también publicaron código, permitiendo variar prompts, modelos y ajustes de muestreo.

Los límites importan. La respuesta de un modelo de lenguaje se genera a partir de datos de entrenamiento y convenciones del prompt, mientras la de un participante refleja a una persona en un experimento. Igualar la tarea visible no hace equivalentes esos procesos. Los modelos y prompts descritos también son una muestra de una población que cambia rápidamente, no una propiedad fija de todos los modelos de lenguaje.

Aun así, el trabajo identifica un modo de fallo concreto: un modelo puede tratar el número de ejemplos observados como prueba sobre proporciones o causas. Esa distinción es lo bastante sencilla para probarse en sistemas desplegados manteniendo constantes las proporciones y cambiando el tamaño del grupo.

## El estudio también halló

La asociación falsa se reforzaba cuando las pruebas favorecían una lectura holística, algo importante porque muchos prompts de resumen piden un solo patrón global. Un encuadre analítico redujo la tendencia en algunas condiciones, lo que sugiere que las instrucciones pueden cambiar la respuesta sin eliminar la sensibilidad subyacente.

La prepublicación y su código están disponibles ahora. Las réplicas con modelos más nuevos y datos operativos naturales mostrarían si el efecto de laboratorio predice errores en trabajo analítico real.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| La prepublicación informa de mayor percepción ilusoria de patrones en los modelos de lenguaje probados que en participantes humanos | SEGÚN LA EMPRESA | https://arxiv.org/abs/2610.07791 | ninguna |
| Los experimentos adaptan tareas clásicas de correlación ilusoria y patrones causales | VERIFICADO | https://arxiv.org/abs/2610.07791 | ninguna |
| Las características de autocodificadores dispersos asociadas con sensibilidad a la frecuencia y orientación analítica siguen el efecto descrito | SEGÚN LA EMPRESA | https://arxiv.org/abs/2610.07791 | ninguna |
| El resultado de características internas es correlacional, no una intervención causal | VERIFICADO | https://arxiv.org/abs/2610.07791 | ninguna |
| Los autores publicaron código para los experimentos | VERIFICADO | https://arxiv.org/abs/2610.07791 | ninguna |

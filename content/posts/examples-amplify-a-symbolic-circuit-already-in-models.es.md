+++
title = "Los ejemplos amplifican un circuito ya presente en los modelos"
description = "Un estudio de interpretabilidad encuentra la misma vía de abstracción, inducción y recuperación antes de que aumente la precisión con pocos ejemplos. Esto sugiere que las demostraciones refuerzan mecanismos existentes en lugar de construir un algoritmo nuevo."
slug = "ejemplos-amplifican-circuito-ya-presente-en-modelos"
tags = ["research", "models"]
date = 2026-10-05T03:59:30+02:00
draft = false
+++

Cuando un modelo de lenguaje aprende un patrón a partir de varios ejemplos en su prompt, puede parecer que ha construido un procedimiento nuevo sobre la marcha. Un estudio mecanicista de la investigadora independiente Melissa Wessel ofrece otra explicación para una familia de tareas simbólicas: el procedimiento ya está presente en el modelo, y los ejemplos refuerzan progresivamente la señal que lo recorre.

El preprint sigue un circuito de tres etapas a través de prompts que contienen entre cero y diez demostraciones. Encuentra la misma ruta central cuando la precisión es baja y cuando es casi perfecta. Las cabezas no aparecen de repente cuando el modelo «capta» el patrón. Su contribución causal aumenta.

Es un experimento limitado, no una teoría general del aprendizaje en contexto. Pero convierte una metáfora atractiva —los ejemplos despiertan mecanismos latentes— en algo sobre lo que los investigadores pueden intervenir y realizar pruebas.

## De tokens a variables y de vuelta

La tarea utiliza patrones abstractos de tres tokens, como ABA o ABB. Los tokens son arbitrarios, lo que impide que el modelo se apoye en su significado habitual. Debe inferir qué posición debe copiarse en la respuesta.

Trabajos anteriores identificaron tres etapas. Las cabezas de abstracción simbólica traducen tokens concretos en variables. Las cabezas de inducción simbólica operan sobre ese patrón abstracto. Las cabezas de recuperación convierten la variable predicha en el token requerido. Wessel rastrea esta estructura en Gemma 2-2B, Llama 3.1-8B y Qwen 3-4B cambiando únicamente el número de demostraciones.

En Gemma 2-2B, la precisión empieza en el 17 % con un ejemplo, alcanza el 93 % con cuatro y el 99 % con diez. Sin embargo, el análisis de mediación causal ya detecta las tres etapas con un ejemplo. Las cabezas importantes se mantienen en gran medida entre longitudes de prompt consecutivas, mientras que la contribución causal de una cabeza individual aumenta hasta ocho veces entre uno y diez ejemplos.

La interpretación es cuantitativa, más que arquitectónica: los ejemplos adicionales refuerzan una vía existente en lugar de incorporar otra completamente distinta.

## Trasladar la señal entre prompts

La detección por sí sola puede confundir correlación y mecanismo, por lo que el artículo también traslada activaciones internas entre ejecuciones. Insertar activaciones de diez ejemplos en un prompt de un ejemplo eleva la precisión de Gemma del 17 % al 88 %. Con cero ejemplos, insertar las etapas de inducción y recuperación eleva la precisión de un patrón del 1 % al 56 %; las cabezas aleatorias ajenas al circuito la dejan por debajo del 1 %.

La intervención más ilustrativa utiliza un «vector de función», una activación fija construida a partir de cabezas identificadas por el análisis causal. Inyectarla con cero ejemplos eleva la precisión del 1 % al 86 % en la regla ABA. Cuando se desactivan las cabezas de recuperación posteriores, esa recuperación del rendimiento cae al 13 %.

Esa dependencia es la clave. El vector no actúa como una respuesta independiente ni como un impulso genérico a la red. Puede sustituir en gran medida a la etapa de inducción solo porque el mecanismo posterior de recuperación sigue disponible para leer su salida.

## Un resultado útil en un ámbito pequeño

El estudio hace que el aprendizaje en contexto se parezca menos a escribir un programa nuevo durante la inferencia y más a proporcionar una entrada a un programa incorporado durante el entrenamiento. Si esa perspectiva se generaliza, los límites de un modelo con pocos ejemplos dependerían de los circuitos que contengan sus pesos y de si un prompt puede acceder a ellos.

El artículo no demuestra que todas las demostraciones funcionen así. Su tarea central es, en esencia, una pequeña tabla relacional con una operación de copia. Una comprobación de analogías con cadenas de letras encuentra una topología similar, pero no se repite en todos los modelos ni con el programa completo de inserción de activaciones. El método de análisis también selecciona componentes que distinguen dos reglas, por lo que podría pasar por alto infraestructura compartida.

La mayor solidez del resultado está en aportar un mecanismo concreto para una capacidad sencilla: los ejemplos pueden amplificar una vía simbólica estable mucho antes de que el comportamiento revele que esa vía existe.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| El estudio rastrea las etapas de abstracción, inducción y recuperación en Gemma 2-2B, Llama 3.1-8B y Qwen 3-4B | VERIFICADO | [Preprint](https://arxiv.org/abs/2609.36265) | ninguna |
| La precisión de Gemma pasa del 17 % con un ejemplo al 99 % con diez; la contribución por cabeza aumenta hasta ocho veces | SEGÚN LA EMPRESA | [Preprint](https://arxiv.org/abs/2609.36265) | ninguna; experimentos de la autora |
| Insertar activaciones de diez ejemplos eleva al 88 % la precisión con un ejemplo, e insertarlas con cero ejemplos la eleva del 1 % al 56 % | SEGÚN LA EMPRESA | [Preprint](https://arxiv.org/abs/2609.36265) | ninguna; experimentos de la autora |
| La inyección de un vector de función eleva la precisión de ABA con cero ejemplos del 1 % al 86 %, y cae al 13 % tras desactivar la recuperación | SEGÚN LA EMPRESA | [Preprint](https://arxiv.org/abs/2609.36265) | ninguna; experimentos de la autora |
| Las demostraciones amplifican un circuito existente en lugar de construir uno nuevo para estas tareas | ANÁLISIS | [Preprint](https://arxiv.org/abs/2609.36265) | interpretación del artículo de las intervenciones causales |
| La generalización a un razonamiento abstracto más complejo sigue abierta | VERIFICADO | [Preprint](https://arxiv.org/abs/2609.36265) | limitación declarada |

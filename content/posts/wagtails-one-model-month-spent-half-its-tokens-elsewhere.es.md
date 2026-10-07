+++
title = "Wagtail gastó la mitad de los tokens fuera de su modelo elegido"
description = "El plan de realizar el trabajo de ingeniería de septiembre con GLM 5.3 Flash consumió 2000 millones de tokens, pero solo la mitad llegó al modelo elegido. Los prototipos, la capacidad de los proveedores y la evaluación explican la diferencia."
slug = "wagtail-gasto-mitad-de-tokens-fuera-de-su-modelo-elegido"
tags = ["essays", "models", "tools"]
date = 2026-10-05T03:57:30+02:00
draft = false
+++

Thibaud Colas, del equipo principal de Wagtail, intentó dedicar septiembre al trabajo de ingeniería con un único modelo abierto eficiente: GLM 5.3 Flash. Su registro de uso recoge 2000 millones de tokens. Solo 1000 millones fueron al modelo elegido.

Eso hace que el experimento sea más útil que un relato de éxito sin contratiempos. El modelo elegido costó unos 68 dólares y consumió unos 4 kWh de electricidad, según la estimación de Colas. El trabajo de todo el mes alcanzó aproximadamente 35 kWh en lugar de los 10 kWh previstos porque los prototipos, los problemas de proveedores y la evaluación deliberada de modelos desviaron el tráfico.

El fallo más notable procedió de un prototipo del servidor experimental Model Context Protocol de Wagtail creado mediante *vibe coding*. Colas afirma que elegir el modelo equivocado para ese trabajo consumió 450 millones de tokens, unos 150 dólares y 5 kWh casi de la noche a la mañana. El prototipo funcionó, pero su uso descontrolado muestra lo rápido que un experimento agéntico puede dominar un presupuesto cuidadosamente elegido.

La infraestructura fue la segunda limitación. Colas señala una degradación del rendimiento de GLM 5.3 Flash y la atribuye a la capacidad limitada de los proveedores independientes de inferencia. Trasladó trabajo a alternativas como DeepSeek V4.1 Flash y Qwen 3.8 Flash. Para un equipo que intenta evitar los mayores laboratorios, la disponibilidad pasa a formar parte de la calidad del modelo: una buena versión entrenada no es una opción fiable para producción si el servicio se ralentiza bajo demanda.

Parte del uso ajeno al modelo elegido fue intencional. Wagtail está desarrollando su propia prueba comparativa de tareas, por lo que el equipo necesitaba ejecutar varios modelos en lugar de optimizar solo la producción cotidiana. Colas propone ahora reservar la regla de un único modelo para más de la mitad del trabajo habitual de producción y permitir que investigación y desarrollo comparen alternativas libremente.

Sigue valorando positivamente GLM 5.3 Flash. El contexto largo, la compatibilidad con visión y la disponibilidad a través de varios proveedores hicieron que el modelo resultara útil para el desarrollo de Wagtail, el trabajo de interfaces, la documentación y la evaluación. Esa valoración es su experiencia, no una comparación controlada.

La lección más amplia es metodológica. Los totales de tokens ocultan si el uso procedió de producción prevista, bucles accidentales o evaluación necesaria. Un panel operativo útil necesita al menos coste, energía, identidad del modelo y resultado de la tarea. También necesita medición local y continua: el prototipo costoso solo se hizo visible después de haber consumido una cuarta parte de los tokens totales del mes.

Este es el relato autodeclarado de un mes de un equipo, no evidencia de que GLM 5.3 Flash o los modelos abiertos en general cuesten una cantidad determinada. Los precios de los proveedores, las estimaciones energéticas y las combinaciones de tareas varían. Lo que establece el relato es un modo de fallo que conviene prever: el presupuesto del modelo puede ser razonable mientras el flujo de trabajo que lo rodea lo desborda.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| El uso de septiembre sumó 2000 millones de tokens, de los que 1000 millones correspondieron a GLM 5.3 Flash | VERIFICADO | [Relato de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | ninguna; panel de uso del autor |
| La parte del modelo elegido costó unos 68 dólares y 4 kWh; todo el mes consumió unos 35 kWh | SEGÚN LA COMUNIDAD | [Relato de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | ninguna; estimaciones del autor |
| El prototipo consumió 450 millones de tokens, unos 150 dólares y 5 kWh | SEGÚN LA COMUNIDAD | [Relato de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | ninguna; mediciones del autor |
| La capacidad de los proveedores obligó a cambiar a otros modelos | SEGÚN LA COMUNIDAD | [Relato de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | ninguna; diagnóstico del autor |
| GLM 5.3 Flash resultó útil en tareas de ingeniería de Wagtail | OPINIÓN | [Relato de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | valoración de un profesional |
| El modelo, el coste, la energía y el resultado deben medirse conjuntamente | ANÁLISIS | [Relato de Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | inferencia a partir de los modos de fallo descritos |

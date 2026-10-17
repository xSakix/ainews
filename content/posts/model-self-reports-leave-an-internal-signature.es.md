+++
title = "Los autoinformes de modelos dejan una firma interna"
slug = "los-autoinformes-de-modelos-dejan-una-firma-interna"
description = "Un estudio controlado encuentra que los informes fieles de preferencias aprendidas reutilizan más del cómputo detrás de las decisiones del modelo. El resultado sugiere una prueba de caja blanca de su fundamentación, con límites estrechos."
tags = ["research", "models"]
date = 2026-10-10T04:01:41+02:00
draft = false
+++

Los modelos que describían con precisión sus preferencias aprendidas reutilizaban más del cómputo interno de sus decisiones que los que confabulaban, según una nueva prepublicación.

David Atkinson y David Bau, de Northeastern University, junto con Dillon Plunkett, de Eleos AI Research, crearon personajes ficticios con preferencias ocultas y entrenaron modelos Qwen3 para elegir en su nombre. Los modelos nunca recibieron entrenamiento para explicar esas preferencias, lo que permitió preguntar si un autoinforme preciso podía emerger por sí solo.

## Por qué importa {#why-it-matters}

Un investigador de interpretabilidad que evalúa lo que un modelo dice de su propio estado suele afrontar un problema circular: la afirmación parece plausible, pero el estado quizá sea imposible de comprobar. Este experimento proporciona una referencia conocida y encuentra una diferencia estructural entre informes que coinciden con ella y los que no.

Las preferencias ficticias eran reglas sencillas de cinco números sobre rasgos como la distancia al centro de una ciudad y el tamaño de una habitación. Un modelo veía pares de opciones y aprendía cuál elegiría su personaje asignado. Después, instrucciones separadas le pedían expresar los pesos de preferencia del personaje como números.

En algunas ejecuciones terminaron emergiendo informes precisos aunque los datos de entrenamiento solo contenían decisiones. Eso importa porque el modelo no podía limitarse a imitar una explicación vista durante el entrenamiento; debía convertir en lenguaje la regla de decisión que había aprendido.

## Los mismos pesos sustentan la elección y el informe

Los autores utilizaron después parcheo de atribuciones, un método que estima qué componentes del adaptador contribuyen a una salida concreta. Compararon el patrón utilizado para elegir con el empleado para informar de la preferencia oculta.

Los adaptadores fieles tenían una similitud media de 0,34 entre patrones, frente a 0,08 de los no fieles. El intervalo de incertidumbre de los autores para la diferencia excluía el cero. En términos sencillos, los informadores precisos tendían a apoyarse en más de los mismos circuitos añadidos para actuar y describir qué guiaba la acción.

Los experimentos por capas apuntaban en la misma dirección. Un Qwen3 de 14 mil millones de parámetros entrenado en sus 40 capas aprendía las decisiones, pero informaba mal de sus preferencias. Restringir el entrenamiento aproximadamente al primer cuarto o la primera mitad de la red producía informes mucho más fieles, mientras entrenar solo las capas posteriores no reproducía el efecto. Los autores interpretan que la información de preferencias se mueve a capas al alcance de los mecanismos existentes de verbalización.

La evidencia es mecanicista y no de comportamiento: la prueba no necesita entender la redacción del informe. En principio, la misma comparación podría funcionar sobre un informe ofuscado o una lengua desconocida, siempre que los componentes internos relevantes sean accesibles.

### El estudio también halló

Los modelos Qwen3 mayores aprendían autoinformes fieles con más frecuencia que las variantes pequeñas, aunque algunos pequeños desarrollaron informes con correlación negativa pese a buenas decisiones. Una réplica con Gemma 4 encontró adaptadores de fidelidad alta y baja entre las configuraciones mayores. Dentro de un mismo modelo, la relación entre similitud de atribuciones y fidelidad entre personajes era positiva, pero débil.

El resultado no produce un detector de introspección para modelos desplegados. Las reglas de preferencia eran construidas, lineales y de solo cinco dimensiones; los experimentos modificaban adaptadores ligeros, no los pesos completos del modelo, y las puntuaciones de similitud de los grupos fiel y no fiel se solapaban. Una similitud alta respaldaba la fidelidad en esta configuración, pero una puntuación baja no demostraba engaño ni confabulación.

La prepublicación se presentó el 5 de octubre de 2026. Su siguiente paso más claro es probar si la misma reutilización interna aparece cuando los modelos informan de estrategias aprendidas más ricas cuya referencia real siga siendo medible independientemente.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| El estudio entrenó adaptadores LoRA con preferencias lineales ocultas y observó autoinformes precisos sin supervisión de autoinforme | SEGÚN LA EMPRESA | https://arxiv.org/abs/2610.07186 | ninguna |
| Los adaptadores fieles promediaron una similitud de atribuciones de 0,34, frente a 0,08 de los no fieles | SEGÚN LA EMPRESA | https://arxiv.org/abs/2610.07186 | ninguna |
| Entrenar solo las capas iniciales mejoró el autoinforme en Qwen3-14B, mientras hacerlo solo en las finales no | SEGÚN LA EMPRESA | https://arxiv.org/abs/2610.07186 | ninguna |
| El método separa grupos con puntuaciones solapadas y se probó sobre adaptadores en un entorno controlado | VERIFICADO | https://arxiv.org/abs/2610.07186 | ninguna |
| El artículo se presentó el 5 de octubre de 2026 por Atkinson, Plunkett y Bau | VERIFICADO | https://arxiv.org/abs/2610.07186 | ninguna |

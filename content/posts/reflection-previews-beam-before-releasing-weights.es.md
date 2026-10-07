+++
title = "Reflection presenta Beam antes de publicar sus pesos"
description = "El modelo de mezcla de expertos de 501 mil millones de parámetros solo está disponible mediante acceso anticipado. Reflection afirma que los pesos, un informe técnico y las herramientas para desarrolladores llegarán más adelante en octubre."
slug = "reflection-presenta-beam-antes-de-publicar-sus-pesos"
tags = ["models", "agents"]
date = 2026-10-06T04:09:31+02:00
draft = false
+++

Reflection AI ha anunciado Beam, un modelo de 501 mil millones de parámetros para programación y tareas con agentes, pero los desarrolladores todavía no pueden examinar ni ejecutar sus pesos.

La empresa californiana de IA describe Beam como un modelo de mezcla de expertos dispersa: almacena 501 mil millones de parámetros, pero activa 23 mil millones por cada token. El acceso anticipado requiere registrarse, mientras que los pesos, la licencia, la ficha del modelo, el informe técnico y las herramientas para desarrolladores siguen pendientes.

Para un desarrollador que elige un modelo abierto, la distinción importa. Un modelo de pesos abiertos puede probarse con cargas de trabajo privadas, modificarse y desplegarse sin depender del servicio del fabricante; un anuncio y una tabla de pruebas comparativas todavía no permiten realizar esas comprobaciones.

Reflection afirma que entrenó Beam con 23,8 billones de tokens y después realizó más de 100 millones de ejecuciones de aprendizaje por refuerzo en 10 500 GPU NVIDIA GB300 durante cuatro semanas. Estas cifras describen un entrenamiento de una escala inusualmente grande, pero la empresa no ha publicado el informe técnico necesario para examinar la combinación de datos o la configuración de la evaluación.

La tabla del propio laboratorio atribuye a Beam puntuaciones de 80,9 en SWE-bench Verified y 80,1 en Terminal-Bench 2.1. También sitúa a Beam por detrás de Kimi K3, GLM-5.3 y Qwen 3.8-Max en la mayoría de las pruebas enumeradas. La principal comparación de Reflection se centra en la eficiencia: afirma que Beam alcanza resultados comparables a los de GLM-5.2 utilizando entre tres y cuatro veces menos cómputo de inferencia, según su propia estimación de operaciones de coma flotante.

Esa afirmación podría importar más que una ventaja estrecha en una prueba comparativa para los equipos que pagan por ejecutar sesiones largas con agentes. La activación dispersa reduce el cómputo utilizado por cada token, aunque el modelo completo sigue necesitando suficiente memoria e infraestructura para almacenar y servir cientos de miles de millones de parámetros.

Reflection afirma que Beam está pasando las últimas pruebas de seguridad. La empresa prevé publicar los pesos, el informe técnico, la ficha del modelo y los recursos para desarrolladores más adelante en octubre de 2026; no ha indicado un día concreto de lanzamiento.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| Reflection anunció Beam y abrió el registro para el acceso anticipado | VERIFICADO | [Anuncio de Reflection](https://reflection.ai/blog/introducing-beam) | no necesaria para la acción de la empresa |
| Beam tiene 501 mil millones de parámetros totales y 23 mil millones de parámetros activos por token | SEGÚN LA EMPRESA | [Anuncio de Reflection](https://reflection.ai/blog/introducing-beam) | ninguna; los pesos y el informe están pendientes |
| El entrenamiento utilizó 23,8 billones de tokens y más de 100 millones de ejecuciones de aprendizaje por refuerzo en 10 500 GPU GB300 durante cuatro semanas | SEGÚN LA EMPRESA | [Anuncio de Reflection](https://reflection.ai/blog/introducing-beam) | ninguna |
| Beam obtuvo 80,9 en SWE-bench Verified y 80,1 en Terminal-Bench 2.1 | SEGÚN LA EMPRESA | [Anuncio de Reflection](https://reflection.ai/blog/introducing-beam) | ninguna |
| Reflection estima resultados comparables a los de GLM-5.2 con entre 3 y 4 veces menos cómputo de inferencia | SEGÚN LA EMPRESA | [Anuncio de Reflection](https://reflection.ai/blog/introducing-beam) | ninguna |
| Los pesos, el informe, la ficha del modelo y los recursos para desarrolladores están prometidos para más adelante en octubre de 2026 | VERIFICADO | [Anuncio de Reflection](https://reflection.ai/blog/introducing-beam) | no necesaria para el calendario anunciado |

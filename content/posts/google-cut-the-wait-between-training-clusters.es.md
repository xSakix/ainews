+++
title = "Google redujo la espera entre clústeres de entrenamiento"
slug = "google-redujo-la-espera-entre-clusteres-de-entrenamiento"
description = "Google hizo que dos grupos de TPU intercambiaran actualizaciones más pequeñas mientras entrenaban un modelo de 32 000 millones de parámetros. El tiempo por paso se mantuvo bajo una restricción de red simulada, lo que deja abierto qué costará el método entre centros de datos reales."
tags = ["research", "hardware", "models"]
date = 2026-11-22T06:29:30+01:00
draft = false
+++

Los ingenieros de Google fijaron un límite de ancho de banda entre dos grupos de TPU. A 10 gigabits por segundo, un paso de entrenamiento convencional con paralelismo de datos tardó 55,11 segundos. El mismo modelo tardó 5,76 segundos por paso cuando los grupos intercambiaron actualizaciones más pequeñas en segundo plano.

El experimento, que Google publicó en noviembre, probó Qwen3-32B en dos particiones (*slices*) de TPU v5p-32. Ambas operaban sobre una red rápida. El equipo utilizó el control de tráfico de Linux para simular el tipo de ancho de banda limitado que puede separar a dos grupos de aceleradores. Ese diseño le permitió mantener constantes el hardware y el modelo mientras variaba la cantidad de datos que podía atravesar el enlace.

## Cuando el enlace marca el ritmo

En el entrenamiento estándar con paralelismo de datos, cada grupo recibe una copia del modelo y un lote distinto de ejemplos de entrenamiento. Tras calcular los gradientes, que indican cómo modificar los parámetros del modelo, los grupos los combinan para que las copias avancen al unísono. En una red rápida, parte de ese intercambio puede solaparse con el cómputo. En cuanto tarda más que el cómputo capaz de ocultarlo, los aceleradores tienen que esperar.

Google calcula que su configuración de paralelismo de datos intercambió unos 65,5 gigabytes a través del enlace en cada paso. Cuando el enlace funcionaba a plena velocidad, el sistema de referencia necesitó unos 5,6 segundos por paso. A 30 gigabits por segundo, necesitó 19,41 segundos. El modelo y la cantidad de trabajo por paso no cambiaron. La mayor parte del tiempo adicional se empleó en transmitir las actualizaciones.

Ese es el problema que Arthur Douillard y sus colegas se propusieron abordar en el trabajo original de DiLoCo. En su estudio sobre el entrenamiento de modelos de lenguaje con C4, los investigadores hicieron que ocho grupos entrenaran de forma independiente durante ciertos tramos y pusieran en común sus actualizaciones de manera periódica. Informaron de que igualaban al entrenamiento totalmente síncrono intercambiando 500 veces menos datos en ese experimento concreto. El estudio empleó una configuración distinta a la de la nueva prueba comparativa (*benchmark*) de MaxText, de modo que las dos reducciones de tráfico miden cosas diferentes.

## Cambiar cuándo viajan las actualizaciones

El método DiLoCo original seguía teniendo un problema al final de cada tramo. Los pasos menos costosos se ejecutaban a máxima velocidad, pero después los grupos tenían que sincronizar todo el modelo de una vez. Con el límite de 10 gigabits en el nuevo benchmark de Google, el DiLoCo convencional promedió 7,55 segundos por paso y seguía sufriendo una pausa periódica. Para un sistema de entrenamiento que permanece ocupado la mayor parte del tiempo, una pausa a intervalos regulares puede representar una parte considerable del promedio.

El artículo de 2025 sobre Streaming DiLoCo cambió esa planificación. En lugar de enviar el modelo completo en una sola operación, los grupos intercambian partes en secuencia. Los pasos de entrenamiento siguientes pueden continuar mientras la transferencia está en curso. El trabajo también exploró la cuantización de los datos intercambiados, lo que reduce el número de bits necesarios para representarlos. La distinción de fondo está entre la cantidad de datos que un sistema envía a lo largo de una ejecución y la que intenta enviar a la vez.

En el experimento con MaxText, el equipo dividió Qwen3-32B en 65 fragmentos. Un grupo podía entrenar mientras las CPU anfitrionas sincronizaban en segundo plano alrededor de un gigabyte de datos correspondiente a un fragmento. A lo largo de 65 pasos, el tráfico entre las particiones bajó de 4258,8 gigabytes con paralelismo de datos estándar a 67 gigabytes con Streaming DiLoCo. El tiempo medio por paso se mantuvo en 5,76 segundos tanto a 30 como a 10 gigabits por segundo. Sin restricción de ancho de banda, los tres métodos completaron los pasos en aproximadamente el mismo tiempo.

## El experimento midió más que el tráfico

Un modelo que pasa menos tiempo esperando puede resultar igualmente peor al final del entrenamiento. Permitir que los nodos trabajadores se actualicen de forma independiente altera la secuencia de pesos que ve cada uno. Google señaló en particular los modelos de mezcla de expertos, en los que un enrutador decide qué partes del modelo procesan cada token. Si los enrutadores aprenden por separado durante demasiado tiempo, podrían aprender a enviar ejemplos similares a expertos distintos.

El equipo de MaxText comparó la pérdida de validación en ejecuciones de 4000 pasos para dos modelos de este tipo, Qwen3-30B-A3B y Gemma4-26B-A4B. Informa de que las ejecuciones en *streaming* igualaron o mejoraron ligeramente el sistema de referencia síncrono. En la ejecución de Qwen, el equipo ajustó la sincronización durante aproximadamente los primeros 800 pasos. El resultado refleja hasta qué punto las ejecuciones predijeron datos reservados durante el periodo evaluado. Queda abierto cuánto ajuste requerirían otros modelos y ejecuciones más prolongadas.

Para los equipos que deben conseguir capacidad repartida en varias ubicaciones, hay dos cuestiones distintas. Una es si el trabajo de entrenamiento puede seguir computando mientras viajan las actualizaciones. La otra es cuánto cuesta alcanzar un nivel de calidad exigido cuando la red presenta latencia real, fallos y tráfico que el experimento no reprodujo. La comparación de rendimiento empleó un único modelo denso y dos grupos de aceleradores. Las ejecuciones de calidad responden a otra pregunta a lo largo de un número limitado de pasos. Google no ofrece ninguna comparación de costos ni ninguna medición del tiempo necesario para alcanzar una pérdida objetivo en instalaciones reales.

Los ingenieros habían empezado fijando un límite en un enlace que, de otro modo, podía soportar ese tráfico. Con el límite activado, observaron cómo el paralelismo de datos convencional empleaba casi 50 segundos adicionales por paso. Streaming DiLoCo completó un paso casi en el mismo tiempo con el límite activado que sin él.

## Referencias

- Douillard, A., Feng, Q., Rusu, A. A., et al. (2023). *DiLoCo: Distributed Low-Communication Training of Language Models*. https://arxiv.org/abs/2311.08105
- Douillard, A., Donchev, Y., Rush, K., et al. (2025). *Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch*. https://arxiv.org/abs/2501.18512
- Khatwani, M., Zuo, C., Fallen, N., et al. (2026). *Distributed LLM Training Across Metros: Streaming DiLoCo in MaxText*. https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/

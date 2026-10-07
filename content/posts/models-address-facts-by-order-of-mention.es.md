+++
title = "Los modelos localizan los hechos por su orden de mención"
description = "Un preprint identifica una dirección interna compartida que orienta a los modelos de lenguaje hacia el primer hecho, el segundo o los posteriores de un pasaje. Desplazar una pregunta en esa dirección puede cambiar qué hecho recupera el modelo."
slug = "modelos-localizan-hechos-por-orden-de-mencion"
tags = ["research", "models"]
date = 2026-10-06T04:08:31+02:00
draft = false
+++

Los modelos de lenguaje parecen localizar los hechos de un pasaje en parte por el orden en que se mencionaron, según un nuevo estudio de interpretabilidad.

Yufa Zhou probó modelos Qwen, Gemma y Llama con listas breves de afirmaciones factuales seguidas de preguntas. Los estados internos de las preguntas en los modelos formaron un patrón reproducible para el primer hecho, el segundo y los posteriores, incluso cuando cambiaban los nombres y los temas.

## Por qué importa {#why-it-matters}

Para un investigador que intenta comprender cómo se recupera información dentro de un modelo, el resultado ofrece un mecanismo concreto más allá de otra correlación entre activaciones y respuestas. Era posible desplazar experimentalmente la misma dirección interna y hacer que una pregunta sobre un hecho recuperara otro hecho del pasaje.

El artículo llama a estas posiciones «direcciones de hechos». Considérese un contexto que dice que Alice come una manzana y Bob come una pera. Una pregunta sobre Alice y otra sobre Bob difieren dentro del modelo a lo largo de una dirección relacionada con el orden de mención de los hechos. Cuando el investigador añadió la dirección del primer hecho al segundo a una pregunta sobre el primero, el modelo respondió a menudo con el contenido del segundo.

Esa intervención es la evidencia más sólida del estudio. Un clasificador puede descubrir muchos patrones en los estados ocultos sin demostrar que un modelo los utilice. Cambiar la respuesta modificando la dirección propuesta aporta respaldo causal al mecanismo, aunque las pruebas utilizan listas de hechos controladas en lugar de documentos naturales largos.

En 64 conjuntos nuevos de palabras, la intervención seleccionó el hecho previsto en aproximadamente cinco de cada seis casos para Qwen, cerca de la mitad para Gemma y alrededor de uno de cada tres para Llama. Las tasas exactas fueron del 84,1 %, el 53,9 % y el 36,2 %, respectivamente. Estas diferencias muestran que la dirección era compartida entre familias de modelos, pero no resultaba igual de fiable en todas.

## Las direcciones ocupan un espacio interno pequeño

Zhou señala que las direcciones de hechos se sitúan en un subespacio de rango bajo. En términos sencillos, los modelos no necesitan una dirección independiente y sin relación con las demás para cada posición posible; un pequeño conjunto de direcciones describe buena parte del patrón de ordenación.

Los modelos también accedían con mayor facilidad al primer hecho mencionado que a los posteriores. Esto se asemeja a un efecto de primacía en la memoria humana, pero el experimento no demuestra que las personas y los transformers utilicen el mismo mecanismo. Identifica una asimetría medible en los modelos probados.

El patrón apareció en las capas intermedias tardías y en tamaños de entre 1500 millones y 32 mil millones de parámetros. Las versiones guardadas durante el entrenamiento sugerían que se formaba pronto, en lugar de aparecer solo después de un ajuste extenso con instrucciones. El código publicado junto al preprint permite examinar las intervenciones controladas.

La configuración limitada también es la principal restricción. Las listas de hechos simples aíslan con claridad el orden, mientras que los prompts reales contienen encabezados, referencias repetidas, herramientas y afirmaciones contradictorias. El artículo muestra que el orden de mención puede actuar como una dirección en condiciones controladas; no demuestra que ese orden domine la recuperación en las transcripciones habituales de agentes.

Zhou presentó el preprint el 1 de octubre de 2026. Las próximas evidencias vendrán de reproducir la intervención en documentos menos regulares y comprobar si cambiar la estructura del documento modifica las mismas direcciones internas.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| Los estados de las preguntas se organizan según el orden de los hechos en Qwen, Gemma y Llama | SEGÚN LA EMPRESA | [Preprint de Zhou](https://arxiv.org/abs/2610.00910) | ninguna; resultado de un preprint |
| Añadir un vector ordinal puede redirigir una pregunta hacia otro hecho | SEGÚN LA EMPRESA | [Preprint de Zhou](https://arxiv.org/abs/2610.00910) | ninguna; experimento del autor |
| La transferencia entre 64 conjuntos de palabras alcanzó el 84,1 % para Qwen, el 53,9 % para Gemma y el 36,2 % para Llama | SEGÚN LA EMPRESA | [Preprint de Zhou](https://arxiv.org/abs/2610.00910) | ninguna |
| Las direcciones de hechos ocupan un subespacio de rango bajo y favorecen el primer hecho | SEGÚN LA EMPRESA | [Preprint de Zhou](https://arxiv.org/abs/2610.00910) | ninguna |
| El patrón aparece entre 1500 millones y 32 mil millones de parámetros y se forma pronto durante el preentrenamiento | SEGÚN LA EMPRESA | [Preprint de Zhou](https://arxiv.org/abs/2610.00910) | ninguna |
| El código para reproducir el estudio es público | VERIFICADO | [Repositorio sobre el orden de mención](https://github.com/MasterZhou1/order-of-mention) | repositorio disponible |

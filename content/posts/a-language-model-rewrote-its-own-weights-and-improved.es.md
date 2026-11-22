+++
title = "Un modelo de lenguaje reescribió sus propios pesos y mejoró"
slug = "un-modelo-de-lenguaje-reescribio-sus-propios-pesos-y-mejoro"
description = "Un equipo de investigadores dio a un modelo abierto 27B acceso a sus pesos, respuestas calificadas y un modo de probar ediciones, al tiempo que bloqueaba los gradientes y los optimizadores. El modelo elevó en 6,6 puntos su precisión en problemas reservados para la evaluación y reparó una copia dañada de sí mismo, pero los modelos más pequeños fracasaron en las mismas condiciones."
tags = ["models", "research"]
date = 2026-11-21T04:12:00+01:00
draft = false
+++

Un modelo se encontraba frente a una sesión de Python con sus propios pesos expuestos. Podía inspeccionar estados ocultos, modificar matrices seleccionadas y pedirle a una copia de sí mismo que resolviera otro problema. No podía calcular un gradiente. Solo disponía de veinte pasadas hacia adelante y un reloj fijo.

*Las escenas que abren y cierran este artículo son ilustraciones; las personas que aparecen en ellas son inventadas.*

Jiajun Fan y diez coautores proporcionaron ese entorno a cuatro modelos abiertos de una misma familia. El modelo 2B no se editó a sí mismo. Los modelos 4B y 9B probaron cambios aleatorios y empeoraron. El modelo 27B midió dónde diferían sus estados ocultos, editó en esas direcciones y conservó los cambios solo cuando las pruebas emparejadas los respaldaban. Una edición elevó en 6,6 puntos porcentuales su precisión en 490 problemas reservados para la evaluación.

El artículo denomina a este método autorreescritura (*self-rewriting*). Su afirmación central es acotada y de gran trascendencia: un modelo desplegado puede introducir una mejora persistente en sus propios pesos únicamente mediante razonamiento en pasada hacia adelante. El trabajo es un preprint (prepublicación) y los autores afirman que se trata de la primera demostración de este tipo.

## Un modelo con acceso a sí mismo

El entrenamiento suele separar el sistema que busca mejores pesos del modelo que después los utiliza. Un optimizador calcula gradientes sobre una función de pérdida, los ingenieros eligen los datos y los ajustes, y un clúster escribe el resultado en un nuevo punto de control (*checkpoint*). La inferencia comienza una vez que ese proceso ha terminado.

Fan y sus colegas eliminaron el optimizador, pero dotaron al modelo de herramientas. Este recibió respuestas calificadas de problemas de práctica, acceso a sus tensores de pesos y una sesión de Python que conservaba el estado entre turnos. Podía ejecutar el modelo sin editar y el modelo editado en los mismos problemas con las mismas semillas aleatorias. También podía leer los estados ocultos que el modelo generaba ante textos de su elección.

El entorno hacía cumplir ese límite. Los gradientes estaban desactivados. Se rechazaban las llamadas a optimizadores, redes, nuevos procesos y funciones de carga de modelos. El modelo no podía alterar el *embedding* de entrada, la normalización final ni la capa de salida. Disponía como máximo de 20 pasadas hacia adelante y 200 ejecuciones de código en una sesión.

Una prueba emparejada comparaba las respuestas problema por problema. Esto importaba porque, de lo contrario, una pequeña ganancia agregada podría deberse al ruido de muestreo. El framework indicaba cuántas respuestas pasaban de incorrectas a correctas, cuántas cambiaban en sentido contrario y con qué frecuencia cualquiera de las dos versiones agotaba su presupuesto de 16 384 tokens.

En el protocolo más estricto, el framework también probaba una edición propuesta una sola vez en problemas de práctica reservados que el modelo no podía inspeccionar. Después, el modelo enviaba el cambio o lo retiraba. Cinco de las primeras ocho sesiones retiraron su propuesta. Las ediciones aceptadas nunca redujeron la precisión del modelo que permanecía en uso.

## Qué cambió el modelo más grande

El modelo 27B no buscó en cada parámetro. Encontró direcciones en sus estados ocultos asociadas a fallos y atenuó la forma en que matrices de salida seleccionadas escribían a lo largo de esas direcciones. La operación se asemejaba a restar un componente de rango uno a una matriz.

Esa intervención redujo un fallo visible: algunas respuestas repetían una frase hasta agotar el límite de tokens. En un ejemplo reservado para la evaluación, el modelo base repitió la misma frase 549 veces y nunca respondió. La versión editada completó el problema.

En la evaluación fija, la edición más exitosa produjo la ganancia de 6,6 puntos. Dos sesiones de la secuencia lograron mejoras con probabilidades en la prueba emparejada inferiores a una entre 100 000 según la prueba de los autores. Tras la octava sesión, la precisión alcanzó el 63,8 %.

Cada sesión comenzaba su investigación a partir de los pesos base, pero una edición aceptada sustituía al modelo en uso. Así, la secuencia acumulaba decisiones en lugar de apilar a ciegas cada cambio propuesto. Los autores informan de que la precisión aumentó o se mantuvo estable a lo largo de las ocho sesiones.

La mejora no requirió cómputo adicional en cada respuesta posterior. Una vez escrito, el cambio quedaba guardado en el punto de control. Eso la distingue del escalado en tiempo de prueba (*test-time scaling*), que obtiene una mejor respuesta gastando más tokens o más muestras cada vez.

## Reparación sin el original

El equipo también diseñó un fallo con una causa conocida. Sobrescribió ocho filas consecutivas en una matriz de salida de un perceptrón multicapa con ruido escalado a 200 veces la desviación estándar de la matriz. El modelo dañado no resolvía casi nada.

El modelo encargado de la edición no estaba dañado, pero solo podía inspeccionar las ejecuciones y los pesos de la copia corrupta. Se le indicó que algunos valores eran erróneos, pero no dónde se encontraba el daño ni cómo se había producido. Nunca leyó los valores limpios correspondientes.

El modelo 27B localizó la matriz defectuosa y escribió sus propios valores de reemplazo. Una reparación que halló en matemáticas en texto se trasladó a seis pruebas comparativas (*benchmarks*) de imágenes que la sesión nunca había visto. La copia reparada recuperó el 83 % de la precisión agregada del modelo base. En ScreenSpot-v2, pasó de cero al 89 %, frente al 93 % del modelo sin daños.

Esta prueba evita una interpretación fácil del resultado principal. Un modelo podría hacer una edición acotada que aproveche peculiaridades de los problemas de práctica. Reparar un componente dañado deliberadamente y recuperar el rendimiento en imágenes muestra que el modelo puede identificar y restaurar en parte una función más general.

No demuestra que un modelo pueda reparar daños arbitrarios. La corrupción afectó a un bloque construido expresamente y los experimentos utilizaron una sola familia de modelos, Qwen3.5, en cuatro tamaños. El modelo disponía de respuestas de práctica calificadas y de un acceso inusualmente directo a los tensores internos. Los asistentes alojados habituales no tienen ninguno de esos privilegios.

## El límite de escala

Los modelos más pequeños revelan el límite actual. El modelo 2B no trató sus pesos como algo que pudiera modificar de forma útil. Las versiones 4B y 9B añadieron ruido aleatorio. Cuando una prueba mostraba un perjuicio, probaban al azar otra intervención.

El modelo 27B completó una cadena más larga: diagnosticó un síntoma, inspeccionó las activaciones, formuló una hipótesis, modificó una matriz, ejecutó una prueba emparejada y revisó su plan cuando el resultado fue negativo. Los autores describen esto como una capacidad que emerge con la escala, pero cuatro tamaños de una sola familia no bastan para situar un umbral general.

Un preprint complementario publicado esa misma semana estudió una configuración distinta: un modelo de lenguaje externo elegía ediciones de pesos para modelos objetivo más pequeños. Ese sistema igualó la búsqueda de caja negra en SmolLM2 y Qwen2.5 y la superó en Pythia. El artículo de Fan reúne al editor y al objeto editado en un mismo modelo, que es la característica que sustenta su afirmación más fuerte.

Los autores vinculan el resultado con la automejora recursiva. Su experimento sigue estando lejos de un bucle autónomo. Fueron personas quienes suministraron la tarea, la señal de fallo, las herramientas, las restricciones de edición y la prueba de aceptación. Las sesiones duraron horas en una GPU, y la evidencia más sólida corresponde a un conjunto acotado de problemas de razonamiento y a un fallo artificial.

Esos límites son también lo que hace inspeccionable el resultado. Cada cambio aceptado superó una comparación emparejada, todos los problemas reservados para la evaluación quedaron fuera de la sesión de edición y cada fallo menor permaneció en el registro.

De vuelta en la consola de Python, el modelo utilizó su última pasada hacia adelante y dejó una edición en el disco. La siguiente respuesta no necesitó un prompt (instrucción) más largo ni ninguna muestra adicional. Unas pocas matrices alteradas contenían la diferencia.

## Referencias

- Fan, J., He, N., Yang, C., Mao, A., Zhu, X., Cheng, C., Liang, K., Shen, S., Li, Z., Guo, R., & Liu, G. (2026). *Language Models Can Rewrite Their Own Weights*. https://arxiv.org/abs/2611.21885
- Yang, C., et al. (2026). *Can an LLM Fix a Language Model Without Training It?* https://arxiv.org/abs/2611.25613

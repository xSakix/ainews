+++
title = "Las mismas cabezas de atención cambian de función con la tarea"
slug = "cabezas-atencion-cambian-funcion-con-tarea"
description = "Una nueva prepublicación encuentra que un modelo de lenguaje reorganiza la influencia de sus cabezas de atención cuando cambia la tarea solicitada, aunque los hechos del prompt permanezcan fijos. Las intervenciones causales sugieren que el contexto de la tarea ayuda a determinar qué hace un componente y complica asignarle una etiqueta permanente."
tags = ["research", "models"]
date = 2026-10-13T04:05:13+02:00
draft = false
+++

Un ingeniero frente a un monitor sigue líneas entre cientos de pequeñas cajas. Una caja recibe una etiqueta clara: «consulta de país». Después cambia la instrucción, los hechos de entrada siguen iguales y la misma caja parece ayudar con otra cosa. Este ingeniero es inventado, una ilustración del problema práctico central de un nuevo estudio: un componente de transformer puede no tener una función estable que nombrar.

## Un mapa que cambia con la pregunta

Sovesh Mohapatra y Dani S. Bassett, investigadores vinculados a la University of Pennsylvania y Yale University, probaron cómo el contexto de la tarea cambia la organización funcional de las cabezas de atención en modelos de lenguaje. Su prepublicación, presentada el 12 de octubre de 2026, examina cinco modelos abiertos de entre 1500 millones y 14 mil millones de parámetros. No ha pasado una revisión por pares.

El estudio empieza con una separación deliberada. Un prompt contiene un pequeño grafo codificado como afirmaciones fácticas, mientras una instrucción pide al modelo responder una de varias preguntas sobre ese grafo. En todas las condiciones los hechos del grafo permanecen fijos. Solo cambia la tarea. Ese diseño permite preguntar si el modelo recorre la misma ruta interna sobre información idéntica o reorganiza la ruta según lo que se le ha pedido hacer.

Tratan cada cabeza de atención como un nodo en una red de influencia. Una arista registra cómo cambiar la salida de una cabeza afecta a otra más adelante en el modelo. El mapa resultante es funcional, no anatómico: la arquitectura no cambia, pero el patrón de influencia medido puede diferir entre tareas.

Y difiere. Mohapatra y Bassett informan de que las redes se separan por tarea en los modelos probados. Las cabezas que ocupan posiciones influyentes en una tarea pueden volverse menos centrales en otra. El hallazgo desplaza la pregunta de interpretabilidad desde «¿Qué representa esta cabeza?» hacia «¿Qué función cumple esta cabeza en esta tarea, dentro de esta red?».

Esa distinción importa porque buena parte de la interpretabilidad mecanicista ha buscado piezas internas reutilizables. Eric Todd y sus colegas identificaron antes pequeños conjuntos de cabezas de atención que transportan «vectores de función» compactos extraídos de ejemplos en contexto. Roee Hendel, Mor Geva y Amir Globerson también mostraron que el aprendizaje en contexto puede formar un vector de tarea que permite ejecutar una operación demostrada incluso sin las demostraciones durante la inferencia. Esos resultados respaldan la idea de que una tarea puede tener una representación interna causal. El nuevo artículo pregunta cómo esa representación cambia las relaciones entre componentes.

## La instrucción puede mover la maquinaria

La correlación por sí sola dejaría una duda evidente. Una tarea diferente produce una respuesta diferente, así que un mapa de influencia diferente podría limitarse a acompañar el cambio. Por eso los autores intervienen sobre las activaciones del modelo.

Construyen una modificación de activación en una capa temprana destinada a llevar al modelo de la representación de una tarea hacia otra sin tocar el prompt escrito. En experimentos con modelos Gemma y Qwen, la modificación puede cambiar qué tarea realiza el modelo. El artículo informa de que los 512 prompts para los que las dos tareas requerían respuestas opuestas cambiaron a la respuesta objetivo, mientras los 512 para los que ambas requerían la misma respuesta la conservaron.

La intervención también hace que el mapa de influencia posterior se parezca al de la tarea objetivo. Los autores lo miden mediante un error entre patrones de respuesta de la red. Su modificación de cambio de tarea redujo ese error un 53,6 % en Gemma y un 5 % en Qwen. La diferencia de magnitud advierte contra tratar el mecanismo como uniforme entre familias, pero ambos casos apuntan en la misma dirección causal: cambiar el contexto interno de la tarea puede redirigir el cómputo posterior.

Esto se parece a la dirección de activaciones, una familia más amplia de métodos que cambia la conducta del modelo añadiendo una dirección a activaciones ocultas. Alexander Matt Turner y sus colegas mostraron que adiciones de activación derivadas de prompts contrastantes podían alterar propiedades de alto nivel del texto generado sin más entrenamiento. El nuevo estudio usa una modificación de activación como sonda experimental. Su objetivo no es distribuir un control de conducta, sino probar si un cambio en la representación de la tarea precede a un cambio en la red de influencia de las cabezas de atención.

La intervención es limitada. No muestra que los investigadores puedan seleccionar cualquier tarea arbitraria, editar cualquier modelo de forma fiable o leer un programa completo de un grafo de cabezas. Las tareas están controladas, los modelos son sistemas de pesos abiertos de tamaño moderado y las pruebas causales se centran en un contraste interno concreto. La afirmación más sólida del artículo concierne a la dependencia del contexto dentro de ese entorno.

## De piezas etiquetadas a equipos reclutados

La neurociencia de redes aporta la metáfora organizadora de los autores. En ese campo, la contribución de una región cerebral suele estudiarse mediante su lugar en una red cambiante y no mediante una función aislada. Bassett y Olaf Sporns describieron el enfoque como un esfuerzo por conectar elementos entre escalas y explicar cómo las interacciones producen conducta. Mohapatra y Bassett llevan esa perspectiva al análisis de transformers.

La analogía tiene límites. Una cabeza de atención es un componente matemático diseñado, no una región biológica, y un transformer no hereda la anatomía ni la historia del cerebro. La transferencia útil es metodológica: observar una pieza junto con el patrón de influencia que la recluta.

Para quienes auditan modelos, esto hace que una etiqueta permanente tranquilice menos. Una cabeza que apoya una conducta con un prompt puede participar de otra forma cuando cambian instrucciones, ejemplos u objetivos. Eliminar o suprimir esa cabeza podría tener efectos que dependen del contexto de la tarea. A la inversa, un proceso relevante para la seguridad puede distribuirse entre configuraciones diferentes aunque los parámetros subyacentes sean idénticos.

El resultado también sugiere una norma práctica para futuras afirmaciones de interpretabilidad. Un circuito propuesto debería probarse con tareas que reutilizan la misma información y una función aparente debería resistir intervenciones causales, no solo inspección visual. Si el circuito cambia, el cambio forma parte del mecanismo que hay que explicar.

Queda trabajo por hacer. El artículo estudia una familia limitada de tareas basadas en grafos y un pequeño conjunto de modelos abiertos. No establece cómo se comportan estas redes de respuesta en sistemas propietarios muy grandes, durante conversaciones largas o bajo instrucciones reales ruidosas. Tampoco resuelve si la red medida captura todo el cómputo pertinente para una respuesta. Los autores presentan un marco para estudiar la reconfiguración, no un atlas terminado.

De vuelta al ingeniero imaginado frente al monitor. La etiqueta de la caja sigue siendo útil, pero ahora necesita una condición al lado: útil para esta operación, con esta instrucción, en esta compañía de otras cabezas. El objeto duradero ya no es la pieza aislada. Es el patrón que la tarea pone en servicio.

## Referencias

- Bassett, D. S., & Sporns, O. (2017). *Network neuroscience*. https://doi.org/10.1038/nn.4502
- Hendel, R., Geva, M., & Globerson, A. (2023). *In-Context Learning Creates Task Vectors*. https://aclanthology.org/2023.findings-emnlp.624/
- Mohapatra, S., & Bassett, D. S. (2026). *Task Context Dynamically Reconfigures Attention Head Networks in Large Language Models*. https://arxiv.org/abs/2610.13895
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://openreview.net/forum?id=AwyxtyMwaG
- Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., & MacDiarmid, M. (2024). *Activation Addition: Steering Language Models Without Optimization*. https://arxiv.org/abs/2308.10248

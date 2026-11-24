+++
title = "El historial largo hizo fallar de forma constante a los modelos"
slug = "el-historial-largo-hizo-fallar-de-forma-constante-modelos"
description = "Un estudio de 100 turnos halló que conservar todo el historial del chat redujo la precisión en el seguimiento del estado de cerca del 60 % al 10 %. Los resúmenes verificados preservaron las respuestas, mientras que los monitores habituales solían hacer que el sistema defectuoso pareciera estable."
tags = ["research", "models"]
date = 2026-11-18T04:00:29+01:00
draft = false
+++

Marta revisa el asistente de inventario antes del turno de mañana. El panel está en verde. Sus respuestas coinciden entre sí, su tono es sereno y los totales del almacén apenas han variado en las últimas cinco preguntas. Entonces compara una cifra con el libro de registro. El asistente ha arrastrado el mismo error a lo largo de todas las respuestas.

*Las escenas que abren y cierran este artículo son ilustraciones; las personas que aparecen en ellas son inventadas.*

Una prepublicación (*preprint*) de Ali Şenol, de la Universidad de Tarsus, pone a prueba ese fallo silencioso. En conversaciones de 100 turnos sobre presupuestos cambiantes, inventarios, recipientes de laboratorio e hitos de proyectos, la precisión de los modelos cayó de alrededor del 60 % a cerca del 10 % en veinte turnos cuando la transcripción completa permanecía en contexto. Un resumen del estado verificado mediante un solucionador mantuvo la precisión más de 50 puntos porcentuales por encima. Las señales habituales de un razonamiento ordenado no ofrecieron una alerta fiable.

## La transcripción pasa a ser parte del problema

Las conversaciones largas exigen que un modelo haga dos tareas a la vez. Debe resolver el problema actual y debe decidir qué conservar de todo lo que él y el usuario dijeron antes. La segunda tarea se vuelve más difícil cuando el estado cambia, se corrige un dato anterior o el modelo ya ha cometido un error.

Trabajos previos habían aislado parte de este problema. En *LLMs Get Lost in Multi-Turn Conversation*, Philippe Laban y sus coautores dividieron tareas completas en fragmentos que llegaban a lo largo de varios turnos. Los modelos solían comprometerse con una respuesta demasiado pronto. Su rendimiento cayó aunque el problema subyacente no había cambiado. Ese estudio utilizó tareas derivadas de GSM8K, el conjunto de datos de 8500 problemas matemáticos escolares que Karl Cobbe y sus colegas presentaron en 2021.

Şenol planteó primero una pregunta causal más acotada: ¿empeora la respuesta final el hecho de conservar las propias réplicas del modelo? Seleccionó 48 tareas matemáticas divididas con entre cuatro y nueve turnos. GPT-4o-mini, Llama 4 Scout y Mistral 7B vieron dos versiones cada uno. Una versión mantenía el diálogo. La otra reconstruía un *prompt* (instrucción) nuevo a partir de la información aportada por el usuario y omitía las respuestas previas del asistente.

Las 11 382 llamadas a los modelos se completaron. GPT-4o-mini resolvió 33 de las 48 tareas con sus propias respuestas a la vista y 43 con un prefijo nuevo, una caída de 21 puntos porcentuales. Mistral 7B bajó de 17 tareas correctas a tres, es decir, 29 puntos. Llama 4 Scout se movió en la misma dirección, pero su diferencia de diez puntos no alcanzó el umbral estadístico del estudio.

El error de Mistral adoptó una forma visible. Con sus respuestas anteriores presentes, a menudo llegaba al último turno diciendo todavía que necesitaba más información. El prompt nuevo contenía los mismos hechos y producía una respuesta.

## Cien turnos con un libro de registro exacto

El primer experimento terminaba tras un máximo de nueve turnos. Además, no permitía separar una pregunta tardía más difícil del deterioro provocado por una conversación más larga. Por ello, Şenol construyó CDR-Stream, una prueba comparativa (*benchmark*) en la que cada turno actualiza un estado y formula una pregunta con una respuesta exacta.

El benchmark abarca cuatro tipos de estado: un registro presupuestario, un inventario de almacén, un protocolo de laboratorio y una cadena de hitos de proyecto. Un mensaje del usuario puede añadir una entrega, corregir un asiento anterior o mover una cantidad entre ubicaciones. También puede incluir frases distractoras. La pregunta pide una suma, una diferencia, un recuento por encima de un umbral, un máximo, un resultado hipotético o una proporción.

Un solucionador exacto genera la respuesta correcta en cada turno. Una escala de doce niveles modifica una sola fuente de dificultad cada vez, como el número de eventos o la complejidad de una actualización. El estudio calibró esa escala por separado para cada modelo y después congeló los parámetros. Esta decisión hace que el experimento sirva para medir el declive dentro de un mismo modelo, pero implica que sus puntuaciones brutas no deben utilizarse para clasificar a los modelos entre sí.

GPT-4o-mini, Llama 3 70B y Gemma 3 12B recibieron treinta diálogos de 100 turnos cada uno. En una rama, el prompt contenía la conversación completa. En la otra, contenía un resumen verificado del estado actual y el nuevo turno del usuario. Ambas ramas emplearon las mismas instrucciones y el mismo formato de respuesta.

Las curvas con historial completo casi se solaparon. La precisión comenzó alrededor de 0,6 en los cinco primeros turnos, bajó aproximadamente a 0,3 entre los turnos seis y veinte y se estabilizó entre 0,08 y 0,11 durante los ochenta turnos restantes. Incluso cuando las preguntas se mantuvieron en el régimen más sencillo, la precisión con historial completo a partir del turno veinte osciló entre 0,10 y 0,14.

El resumen verificado cambió el resultado. En esas mismas conversaciones sencillas, mantuvo la precisión entre 0,82 y 0,86. En los cinco patrones de dificultad, la ventaja media fue de 0,521 para GPT-4o-mini, 0,545 para Llama 3 y 0,588 para Gemma 3. Cuando una secuencia regresaba de preguntas difíciles a preguntas fáciles, el rendimiento basado en resúmenes se recuperaba. El rendimiento con historial completo no lo hacía.

## Una respuesta estable puede ser un error estable

Un operador no dispone del solucionador exacto que utilizó el experimento. Un sistema desplegado necesita una señal que indique cuándo su respuesta actual ha dejado de reflejar la realidad. El estudio probó varias candidatas: la consistencia entre respuestas muestreadas, la coherencia lógica, la similitud semántica, una medida pareada de preparación y detectores estándar de cambios en un flujo de datos.

Ninguna ofreció una advertencia robusta en todos los modelos. En el experimento matemático más corto, las señales de calidad medidas no mostraron ninguna asociación estadísticamente detectable con el fallo final una vez que el análisis controló el turno, la información revelada y la longitud del contexto. Una de las señales solo cubrió 29 tareas de origen, de modo que el artículo no afirma que haya quedado descartada toda asociación pequeña.

El estudio de cien turnos reveló un patrón más preocupante. La consistencia y la coherencia variaron mucho menos que la precisión. La estabilidad aumentó porque los modelos repetían respuestas erróneas similares. Un monitor que premia el acuerdo podría, por tanto, volverse más seguro de sí mismo a medida que la estimación subyacente del estado se deteriora.

Şenol delimita con cuidado el alcance de esa conclusión. Ambos estudios emplean aritmética y seguimiento exacto de estados, lo que permite observar la corrección pero no representa cualquier conversación abierta. Los conjuntos de modelos difieren entre los dos experimentos y no incluyen los sistemas de frontera más potentes actuales. Gemma 4 31B resultó demasiado preciso para la escala de dificultad prevista, por lo que una prueba válida requeriría tareas más difíciles en lugar de más repeticiones de estas.

El experimento largo tampoco incluye una comparación solo con los mensajes del usuario. Por consiguiente, mide el fallo del historial completo, pero no puede asignar una cuota precisa a las respuestas previas del asistente, a la longitud del contexto o a la carga creciente del estado. La monitorización basada en repeticiones solo estuvo completa para GPT-4o-mini. Varios análisis de monitorización fueron exploratorios y no formaron parte de las pruebas confirmatorias congeladas.

## El estado debe quedar fuera de la transcripción

La intervención del artículo es modesta. No dota al modelo de una memoria mejor. Elimina la necesidad de reconstruir el presente a partir de toda la conversación al suministrar un estado compacto que un programa externo ha comprobado.

Esa arquitectura separa la evidencia de la narración. La transcripción puede permanecer disponible para una auditoría, mientras el prompt activo recibe el registro, el inventario o el estado de tareas actual. Şenol propone también comprobaciones entre sesiones separadas y reconsultas contrafactuales, porque un detector situado dentro de un único flujo en deterioro puede no obtener nunca una referencia limpia.

El artículo deja abierto un problema de ingeniería difícil. Sus resúmenes procedían de un solucionador exacto. La mayoría de los sistemas reales no cuentan con uno, y un modelo que redacta su propio archivo de estado puede preservar un error con la misma eficacia con la que preserva un hecho. La cuestión pendiente es cómo puede un sistema mantener y verificar ese estado externo sin convertir silenciosamente el resumen en otra respuesta no fiable.

Marta abre el archivo de estado junto al chat. Una transferencia de almacén figura allí una sola vez, con su evento de origen y su corrección. La transcripción sigue conteniendo las cinco respuestas coincidentes del asistente. Las deja en el archivo y envía el registro verificado con la siguiente pregunta.

## Referencias

- Cobbe, K., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2026). *LLMs Get Lost in Multi-Turn Conversation*. https://arxiv.org/abs/2505.06120
- Şenol, A. (2026). *The Silent Cost of Conversation History in LLM Reasoning*. https://arxiv.org/abs/2611.20071

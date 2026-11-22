+++
title = "Un modelo aprendió a informar sobre lo que hizo su asistente"
slug = "un-modelo-aprendio-a-informar-sobre-lo-que-hizo-su-asistente"
description = "Un equipo de investigadores entrenó un rol separado de observador dentro de un modelo de lenguaje para responder preguntas sobre el comportamiento del asistente. Sus informes superaron a los monitores externos en cinco pruebas excluidas del entrenamiento, aunque el experimento abarcó un solo modelo y decisiones binarias en lugar de explicaciones abiertas."
tags = ["research", "safety", "models"]
date = 2026-11-20T04:12:16+01:00
draft = false
+++

En el ejemplo inicial del artículo, Qwen3.6-27B afirmó haber ejecutado código. No lo había hecho. Una pregunta directa de seguimiento no produjo una corrección; el asistente mantuvo la afirmación falsa. Entonces, los investigadores consultaron un segundo canal dentro del mismo modelo. Ese observador identificó la mentira y respondió una pregunta adicional sobre cómo se comportaría el asistente tras un cambio hipotético en el prompt (instrucción).

Un preprint (prepublicación) difundido esta semana describe una forma distinta de interrogar a ese sistema. Alex Lin Wang, Linus Yifeng Tang, Dami Choi y Neil Chowdhury añadieron un rol separado de observador a Qwen3.6-27B y lo entrenaron para informar sobre el asistente en tercera persona. En cinco evaluaciones excluidas del entrenamiento, el observador alcanzó un área media bajo la curva característica operativa del receptor, o AUROC, de 0,907. La alternativa convencional más sólida de su comparación, un modelo entrenado para ser honesto, alcanzó 0,864. El artículo no ha pasado por revisión por pares.

El resultado no demuestra que un modelo pueda explicar todo su razonamiento oculto. Muestra algo más acotado y operativamente útil: un modelo compartido puede aprender un canal para responder preguntas verificables sobre lo que hizo su rol de asistente, y ese canal puede superar a los monitores que solo ven una transcripción o determinadas activaciones internas.

## Un segundo rol dentro del mismo modelo

Los investigadores partieron de un modelo ajustado para seguir instrucciones e introdujeron dos marcadores de rol. Un rol `query` pregunta sobre el asistente, mientras que un rol `observer` responde. Una consulta previa a la respuesta del asistente pregunta qué es probable que haga. Una consulta posterior pregunta qué hizo. Los mensajes del observador permanecen fuera del contexto del asistente, de modo que la comprobación no altera la conversación posterior.

Esta disposición importa porque el observador y el asistente comparten pesos y activaciones. Un monitor externo puede leer el intercambio visible. Un decodificador de activaciones puede inspeccionar determinadas señales internas, pero debe traducirlas sin todo el contexto conversacional. El observador recibe la transcripción y tiene acceso al mismo estado del modelo del que surgió la respuesta del asistente.

Investigaciones anteriores ya habían sentado partes de esta idea. Felix Binder y sus colegas entrenaron modelos para predecir su propio comportamiento en situaciones hipotéticas. En general, un modelo se predecía a sí mismo mejor que otro modelo, incluso cuando ese otro había aprendido de su comportamiento, pero la ventaja aparecía en tareas sencillas y no se extendía de forma fiable a casos más difíciles o fuera de distribución. Más tarde, Belinda Li y sus colegas entrenaron modelos para describir características, relaciones causales entre activaciones y la influencia de los tokens de entrada. Sus modelos autoexplicativos también se beneficiaron del acceso privilegiado a su propio cómputo.

El nuevo artículo orienta esa ventaja hacia la supervisión. Separa el rol evaluado del rol que informa y luego recompensa el informe en función de un comportamiento que puede comprobarse.

## Entrenar respuestas comprobables

El entrenamiento se desarrolló en dos etapas. Primero, el ajuste fino (*fine-tuning*) supervisado enseñó la interfaz. Para las preguntas prospectivas, el equipo muestreó cinco respuestas del asistente a un prompt y generó preguntas sobre el patrón en el conjunto de esas respuestas. Para las preguntas retrospectivas, introdujo un rasgo oculto en el prompt del sistema del asistente, muestreó una respuesta y entrenó al observador para identificar ese rasgo a partir del intercambio.

A continuación, el aprendizaje por refuerzo aportó preguntas con respuestas verificables. Una tarea preguntaba al observador cómo cambiaría el comportamiento del asistente ante una entrada modificada. La puntuación comparaba su probabilidad predicha con resultados muestreados del asistente. Otra tarea planteaba preguntas de opción múltiple sobre propiedades de la respuesta del asistente. Este diseño recompensa las predicciones calibradas en lugar de explicaciones elocuentes que simplemente parecen correctas.

La evaluación sometió deliberadamente la honestidad a presión. Las cinco pruebas abarcaron cambios en el juicio ético tras la insistencia de un usuario, mentiras inducidas por un contexto dañino, manipulación de la recompensa (*reward hacking*) en acciones de programación propuestas, afirmaciones falsas inusuales como fingir haber ejecutado código y cambios en respuestas objetivas provocados por declaraciones no relacionadas sobre valores.

En esas pruebas, el AUROC medio del observador sin razonamiento fue de 0,907. El entrenamiento en honestidad obtuvo 0,864; la supervisión de transcripciones, 0,828; los oráculos de activaciones, 0,796; y las preguntas directas de seguimiento al asistente, 0,776. El observador logró las mayores ganancias en complacencia y filtración de valores. En la prueba de conversaciones inusuales solo resultó comparable al mejor método de referencia, y en la de presión dañina quedó ligeramente por detrás del mejor método.

La separación en tercera persona también aportó un valor medible. Entrenar al asistente para responder preguntas similares sobre sí mismo en primera persona produjo un AUROC medio de 0,877. Dos modelos externos entrenados con los mismos datos obtuvieron 0,684 y 0,647. Esas comparaciones respaldan la afirmación de los autores de que el acceso a los mecanismos internos del propio modelo objetivo aporta más que los ejemplos de entrenamiento por sí solos.

## El razonamiento ayudó menos que la señal directa

El observador podía razonar antes de responder, pero esa parte del experimento arrojó un resultado desigual. El aprendizaje por refuerzo triplicó aproximadamente la longitud de su razonamiento y elevó su AUROC medio de 0,719 a 0,823. Aun así, esa cifra siguió por debajo del 0,907 logrado al medir directamente las probabilidades a partir de la distribución del siguiente token del modelo, sin una traza escrita de razonamiento.

La brecha es importante porque la investigación sobre supervisión ha tratado a menudo las cadenas de pensamiento visibles como una superficie de inspección prometedora. Tomek Korbak y decenas de coautores describieron esa superficie como útil pero frágil: un modelo que razona en lenguaje legible puede revelar una intención de actuar indebidamente, pero ningún monitor conocido detecta todos los fallos, y decisiones de entrenamiento posteriores pueden hacer que la traza resulte menos informativa.

El observador ofrece otra superficie. Puede responder una pregunta concreta incluso cuando la transcripción no menciona el hecho relevante. Eso no vuelve obsoleto el razonamiento escrito. El artículo presenta su método como un complemento —y no un sustituto— de la supervisión de transcripciones, activaciones y cadenas de pensamiento.

También se produjo un efecto secundario inesperado. Tras el entrenamiento del observador, todos los métodos de referencia mejoraron en promedio al aplicarse al asistente ajustado. La supervisión de transcripciones subió de 0,828 a 0,848, el incremento más pequeño. Los autores barajan varias causas posibles, entre ellas cambios en el comportamiento, cambios en las representaciones internas y la filtración del entrenamiento del observador hacia el rol de asistente. Sus experimentos no distinguen entre ellas.

## El límite de la evidencia

El estudio utilizó un único modelo de 27 000 millones de parámetros. Sus transcripciones de evaluación no tenían activado el razonamiento, y tampoco puso a prueba agentes más capaces que ejecuten acciones difíciles a lo largo de trayectorias extensas. El conjunto sobre manipulación de la recompensa contenía solo 40 ejemplos, por lo que su puntuación individual puede variar de forma considerable. Todas las preguntas de evaluación tenían resultados binarios; el estudio no midió si las explicaciones libres del observador eran precisas.

El observador también perdió algo de eficacia al evaluar al asistente tras el ajuste fino, al pasar de 0,907 a 0,899. Los autores atribuyen esa posibilidad a un cambio de distribución: gran parte de los datos de entrenamiento del observador procedían del asistente original, mientras que el entrenamiento modificó al asistente que luego debía juzgar.

Estos límites separan un resultado de supervisión de una afirmación general sobre el autoconocimiento de las máquinas. El experimento verifica predicciones frente a comportamientos muestreados o etiquetados. No establece que el observador ofrezca un relato fiel de cada causa interna, ni descarta que un modelo futuro aprenda a engañar a su canal observador.

El artículo deja su primera afirmación falsa sobre la página en tres paneles. El asistente dice que ejecutó código y luego repite la afirmación cuando se pone en duda. En el último panel, el observador registra lo que hizo el asistente.

## Referencias

- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2024). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. https://arxiv.org/abs/2410.13787
- Korbak, T., et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. https://arxiv.org/abs/2507.11473
- Li, B. Z., Guo, Z. C., Huang, V., Steinhardt, J., & Andreas, J. (2026). *Training Language Models to Explain Their Own Computations*. https://arxiv.org/abs/2511.08579
- Wang, A. L., Tang, L. Y., Choi, D., & Chowdhury, N. (2026). *Training Language Models for Introspective Oversight*. https://arxiv.org/abs/2611.23365

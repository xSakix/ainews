+++
title = "Cuantos más recuerdos guarda un asistente, más interrumpe sin motivo"
slug = "cuantos-mas-recuerdos-guarda-un-asistente-mas-interrumpe"
description = "Un umbral fijo de recuperación se volvió casi inútil cuando la memoria pasó de ocho entradas a 2.048. Un estudio explica la trampa estadística y prueba una regla que mantiene los falsos recordatorios cerca del 5 % sin datos de entrenamiento etiquetados."
tags = ["research", "agents"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

Imaginemos a una jefa de proyecto que abre su asistente un lunes por la mañana. Meses atrás mencionó que un proveedor prefiere recibir llamadas después del almuerzo. Desde entonces, el sistema ha guardado miles de detalles: reuniones, plazos, nombres, compras, viajes cancelados. Ella escribe un saludo. El asistente la interrumpe para recordarle la preferencia del proveedor y añade una nota sobre un restaurante de la primavera pasada. Ambos recuerdos son ciertos. Ninguno viene a cuento ahora.

## Cuándo merece la pena interrumpir

La memoria a largo plazo suele plantearse como una búsqueda. El usuario pregunta por una conversación anterior y el sistema recupera un fragmento pertinente. La memoria proactiva introduce una decisión más difícil: en cada turno, el asistente debe decidir si algún elemento almacenado justifica una interrupción sin que nadie lo haya pedido.

Yichuan Chen y Xin Wang, de Zhejiang Sci-Tech University, estudiaron qué ocurre cuando crece ese almacén. Su preprint, *The Price of Scale in Proactive Memory Recall*, trata cada recuerdo como una prueba estadística más. Aunque un recuerdo irrelevante tenga pocas probabilidades de superar un umbral de similitud, al acumular miles de oportunidades es probable que al menos uno lo supere.

El efecto fue considerable. Un umbral calibrado para producir un 5 % de falsas alarmas con ocho recuerdos produjo entre un 84 y un 100 % con 2.048, según el modelo de representación vectorial y el indicio empleado. La moderación a pequeña escala se convirtió en interrupciones casi constantes.

No es un olvido ordinario. La información permanece en la memoria. Lo que falla es la decisión sobre cuándo sacarla a colación.

## Más recuerdos, más boletos de lotería

Supongamos que cada recuerdo irrelevante recibe una puntuación de similitud con el último mensaje del usuario. El sistema habla si la puntuación más alta supera un umbral fijo. Con ocho recuerdos irrelevantes, el ruido tiene ocho ocasiones de parecer significativo. Con 2.048, tiene 2.048.

Chen y Wang deducen la consecuencia. Para que la tasa global de falsas alarmas se mantenga en el nivel deseado, la tasa de falsos positivos que se tolera por recuerdo debe disminuir aproximadamente en proporción inversa al tamaño del almacén. Para un objetivo global del 5 %, la tolerancia por recuerdo equivale aproximadamente al logaritmo de 0,95 cambiado de signo y dividido por el número de recuerdos.

Endurecer el criterio tiene un precio. Los indicios pertinentes también deben salvar el listón más alto, lo que sitúa al sistema en el extremo izquierdo de su curva ROC, que relaciona aciertos y falsos positivos. Disminuyen las falsas alarmas, pero también los aciertos. Un mejor modelo de representación vectorial puede mejorar la curva; no elimina la multiplicación de pruebas.

Los autores reprodujeron secuencias construidas a partir de LongMemEval, una evaluación de 500 preguntas que abarca extracción, razonamiento entre sesiones, razonamiento temporal, actualizaciones y abstención. También utilizaron LoCoMo, cuyas largas conversaciones se generaron a partir de perfiles de personajes y grafos de acontecimientos y luego fueron revisadas por personas para asegurar la coherencia. Estas pruebas se diseñaron para saber si un sistema puede recuperar información antigua. Chen y Wang las convirtieron en escenarios cronológicos donde el asistente debe decidir si conviene ofrecer esa información en ese momento.

Construyeron indicios implícitos que ni pedían un recuerdo ni contenían su respuesta. Los experimentos emplearon puntuaciones léxicas y semánticas, varios modelos de representación vectorial y un reordenador de resultados con codificador cruzado. El patrón persistió pese a esos cambios. Incluso un evaluador más costoso se enfrentaba al problema de la escala.

## Un umbral que cambia con el usuario

La alternativa propuesta es una regla de decisión conforme que intercambia indicios. En vez de comparar únicamente el mensaje actual con los recuerdos, puntúa también, sobre el mismo almacén, indicios de referencia extraídos de mensajes anteriores de ese usuario. La pregunta es si el indicio actual destaca de manera inusual frente a esas referencias ordinarias.

Esto cambia la unidad de calibración. El umbral sigue al almacén y a la distribución de mensajes del usuario en lugar de permanecer fijo a medida que la memoria crece. Bajo un supuesto de intercambiabilidad, el rango conforme permite acotar las falsas alarmas para una muestra finita sin ejemplos etiquetados.

En LongMemEval, con elementos de fondo tomados del historial sin filtrar del usuario, la regla por intercambio de indicios mantuvo las falsas alarmas entre el 3 y el 6 %. Su tasa de aciertos igualó la de un umbral ajustado con etiquetas. Al reproducir las conversaciones en orden cronológico y usar mensajes previos como referencias, intervino en el 6–8 % de los turnos iniciales de sesión. La regla de tipo habitual intervino en el 57 % con una memoria de 2.048 entradas.

La decisión tardó unos 50 milisegundos en un solo hilo de CPU. El repositorio publicado incluye reglas de decisión en NumPy, pruebas, scripts de experimentación, anotaciones y resultados. Los autores realizaron los experimentos con una sola RTX 3090 y documentaron cómo reproducir las secuencias de evaluación.

## El equilibrio que queda por resolver

Calibrar el umbral no vuelve sencilla la memoria proactiva. En LoCoMo, la regla conforme podía superar el objetivo de falsas alarmas o volverse demasiado conservadora según la procedencia de los indicios de referencia. Su garantía depende de la intercambiabilidad: los indicios futuros deben comportarse de forma suficientemente parecida a los de referencia para que sus posiciones relativas sigan siendo válidas. Los hábitos del usuario pueden cambiar. Un conjunto de referencias elegido con cuidado puede diferir del tráfico real.

El artículo también prueba la memoria prospectiva, en la que el asistente debe actuar cuando se cumpla una condición futura. TriggerBench ya había mostrado que esto es más difícil que contestar una pregunta directa sobre un recuerdo: el rendimiento cae al crecer el contexto y los modelos pueden acabar recordándolo todo a cada ocasión. En las condiciones de falsas alarmas controladas de Chen y Wang, las reglas de similitud recuperaron como máximo el 9 % de las condiciones de la prueba de memoria prospectiva.

La evaluación humana confirmó el coste de los recuerdos inoportunos. Una persona y dos modelos de lenguaje que actuaban como anotadores examinaron las falsas alarmas; la mayoría no ayudaba a responder. En una versión anterior del artículo, el grado de acuerdo entre tres anotadores arrojó un coeficiente kappa de Fleiss de 0,63. Cerca de nueve de cada diez falsas alarmas contaban como interrupciones reales. Un dato recuperado puede ser correcto y aun así empeorar la conversación.

El estudio es un preprint de 14 páginas que no ha pasado revisión por pares. Las secuencias proceden de evaluaciones, no de años de uso espontáneo por millones de personas. Por eso el intercambio de indicios necesita pruebas con cambios de hábitos, mezclas de idiomas y recuerdos correlacionados entre sí en lugar de independientes. Sin embargo, el argumento sobre la multiplicación de pruebas no depende de un producto concreto. Afecta a cualquier sistema que elija el máximo entre muchas puntuaciones ruidosas.

Volvamos a nuestra jefa de proyecto unos días después. El asistente sigue conservando la preferencia del proveedor y el restaurante de la primavera. La diferencia está en cómo decide guardar silencio: antes de mostrar uno de esos detalles, el mensaje actual debe guardar con la memoria acumulada una relación más estrecha que la que mostraban los mensajes ordinarios de la usuaria frente al mismo almacén. Para ser útil, un sistema de memoria necesita algo más que saber recordar. Necesita una buena razón para hablar.

## Referencias

- Angelopoulos, A. N., & Bates, S. (2021). *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*. https://arxiv.org/abs/2107.07511
- Chen, Y., & Wang, X. (2026). *The Price of Scale in Proactive Memory Recall*. https://arxiv.org/abs/2610.34507
- Chen, Y., & Wang, X. (2026). *Code, data and results for The Price of Scale in Proactive Memory Recall*. https://github.com/RiverChenStillCompiling/price-of-scale
- Maharana, A., Lee, D.-H., Tulyakov, S., Bansal, M., Barbieri, F., & Fang, Y. (2024). *Evaluating Very Long-Term Conversational Memory of LLM Agents*. https://aclanthology.org/2024.acl-long.747/
- Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. https://arxiv.org/abs/2410.10813
- Zhang, T., Wang, X., Zhang, Q., Chen, Q., Li, K., Chen, Y., Wang, D., Meng, H. M., & Lu, Y. (2026). *TriggerBench: Investigating Prospective Memory for Large Language Models*. https://aclanthology.org/2026.emnlp-main.1319/

+++
title = "Un pequeño núcleo cognitivo desafía las cajas negras de la psicología"
slug = "pequeno-nucleo-cognitivo-desafia-cajas-negras-psicologia"
description = "Dos investigadores combinaron unas pocas ideas establecidas sobre memoria, contexto y error de predicción en un modelo de decisiones humanas. CORE superó a predictores neuronales comparables en 137 experimentos y mantuvo sus operaciones internas abiertas a la inspección."
tags = ["research", "models"]
date = 2026-10-14T04:02:33+02:00
draft = false
+++

Una participante está sentada sola en un laboratorio de psicología. Aparece un símbolo, luego otro. Adivina qué puerta oculta una recompensa, recuerda la última sorpresa y cambia lentamente su estrategia. Esta participante es inventada, pero cada pequeño acto pertenece al registro experimental que sustenta un nuevo modelo que intenta explicar millones de decisiones así sin esconder la explicación en una red neuronal.

## Muchos experimentos, una explicación

Marcel Binz y Eric Schulz, del Institute for Human-Centered AI de Helmholtz Munich, han construido COntextual Retrieval and Encoding, o CORE. Su prepublicación une un pequeño conjunto de principios cognitivos establecidos en un modelo computacional y después lo ajusta conjuntamente a 7 036 442 decisiones humanas de 137 experimentos y 80 452 sesiones experimentales.

La ambición va más allá de predecir una tarea. La psicología ha acumulado explicaciones sobre asociación, error de predicción, representación jerárquica, recuperación de recuerdos y olvido, a menudo probadas en tradiciones experimentales separadas. CORE pregunta cuánto del registro conductual pueden explicar esas ideas cuando deben funcionar juntas con un solo conjunto de mecanismos.

Su estructura es una jerarquía de recuerdos episódicos. Los errores de predicción se escriben en esos recuerdos. El contexto gobierna qué se codifica, qué recuerdos se recuperan y cómo se desvanecen. Estas operaciones se expresan como componentes cuyos papeles puede inspeccionar un investigador, en vez de como un modelo secuencial sin restricciones entrenado solo para minimizar el error.

Los autores comparan CORE con un transformer de configuración equivalente y con Centaur, un modelo fundacional de cognición humana presentado por una amplia colaboración dirigida por Binz. Centaur ajustó un modelo de lenguaje con Psych-101, un conjunto de datos que cubre más de diez millones de decisiones en 160 experimentos. Demostró que un gran sistema predictivo podía generalizar entre relatos de contexto, modificaciones de tareas y dominios desconocidos. También planteó el precio habitual de los modelos fundacionales: la predicción se hizo amplia, mientras el mecanismo aprendido seguía siendo difícil de formular como teoría psicológica.

CORE invierte esa disyuntiva. En el nuevo artículo registra una log-verosimilitud negativa predictiva menor que la del transformer equivalente, 262 572 frente a 329 043. Frente a Centaur la comparación es de 262 572 contra 389 151. CORE rinde mejor que el transformer en los 62 estudios usados para esa comparación por estudio y mejor que Centaur en 47.

Estas cifras no significan que CORE haya capturado la mente humana. Comparan predicciones dentro de un corpus experimental concreto reunido para la prueba. Sí muestran que un modelo interpretable no tuvo que sacrificar alcance predictivo solo porque sus partes tenían significados psicológicos.

## Qué recuerda el modelo

La jerarquía importa porque una decisión puede depender de eventos a distintas escalas. Un error reciente puede cambiar la siguiente respuesta. Una serie de ensayos relacionados puede establecer una situación local. Un cambio en el experimento puede restar relevancia a experiencias antiguas aunque sigan almacenadas.

CORE maneja esos efectos mediante codificación y recuperación sensibles al contexto. Los errores de predicción actualizan la memoria en vez de limitarse a cambiar una sola estimación de valor. El modelo puede recuperar un episodio cuando la situación actual se le parece, mientras su proceso de olvido reduce el peso de la experiencia a medida que el contexto se aleja.

Ese diseño produce trazas internas familiares en teorías establecidas. Los autores informan de señales de aprendizaje bayesiano en las variables latentes de CORE: su actualización responde a la incertidumbre de formas asociadas con la inferencia probabilística. También encuentran señales de segmentación de eventos, lo que significa que la organización interna del modelo refleja límites entre situaciones en vez de tratar todo el flujo como uniforme.

El resultado amplía un programa de investigación que los mismos autores han seguido desde la dirección opuesta. En 2023, Binz y Schulz mostraron que modelos de lenguaje ajustados con experimentos de psicología podían superar a modelos cognitivos tradicionales en dos dominios de decisión y contener información sobre participantes individuales. Su trabajo sobre cognición metaaprendida sostenía que los algoritmos de aprendizaje podían aproximar un comportamiento bayesiano óptimo e incorporar a la vez cómputo limitado y otras restricciones realistas.

Esos sistemas preguntaban hasta dónde podía avanzar la maquinaria general del aprendizaje automático hacia la conducta humana. CORE pregunta hasta dónde puede avanzar una teoría psicológica compacta hacia el alcance predictivo del aprendizaje automático. Las dos direcciones se encuentran ahora en parte de los mismos datos.

## Reproducir efectos en vez de nombrarlos

La predicción es solo una parte de la prueba. Los autores simulan CORE en las condiciones experimentales y preguntan si reproduce los efectos conductuales que describieron los estudios. Recupera el 75 %.

Es una exigencia más estricta que igualar una tasa media de decisiones. Un efecto puede implicar adaptación, sesgo, orden, incertidumbre o un cambio tras un límite contextual. Reproducirlo requiere que la conducta del modelo se mueva en la dirección pertinente cuando cambia la manipulación experimental.

El cuarto que falta importa tanto como los tres cuartos logrados. Un modelo unificado resulta científicamente útil cuando sus fallos identifican dónde está incompleto el núcleo propuesto. Un predictor de caja negra puede absorber otro patrón sin decir a los investigadores qué teoría cambió. Un sistema interpretable obliga a una elección más clara: revisar la recuperación, añadir un mecanismo, alterar la jerarquía o aceptar que el fenómeno queda fuera de la explicación.

La amplitud del artículo también crea riesgos. Los experimentos difieren en instrucciones, formatos de respuesta, poblaciones de participantes y convenciones analíticas. El ajuste conjunto puede favorecer mecanismos que explican estructuras comunes y suavizar las inusuales. Una verosimilitud total puede ocultar una explicación débil de un dominio pequeño pero importante. Por eso los autores informan de comparaciones por estudio y efectos simulados, no solo de una puntuación agregada.

CORE también es una prepublicación. Sus afirmaciones, decisiones de implementación y armonización de conjuntos de datos no han completado la revisión por pares. El corpus es grande según los criterios de la psicología experimental, pero sigue siendo un registro seleccionado de tareas que pueden representarse y ajustarse conjuntamente. La vida humana fuera de un laboratorio incluye lenguaje, relaciones sociales, emoción y acción corporal que no se comprimen en siete millones de decisiones discretas.

## Una teoría que puede estar equivocada

La principal contribución del modelo puede ser metodológica. La ciencia cognitiva ha tenido a menudo que elegir entre un modelo transparente que explica un paradigma y un predictor general que dice poco sobre el mecanismo. CORE aporta pruebas de que esa frontera puede moverse.

Eso no elimina los modelos neuronales o fundacionales. Centaur establece una sólida referencia predictiva y puede generalizar mediante descripciones de tareas en lenguaje natural. Un modelo compacto puede utilizar esos sistemas como rivales, generadores de datos o herramientas de descubrimiento. La distinción importante es qué afirmación respalda cada uno. Un predictor muestra que se puede anticipar la conducta. Una teoría cognitiva enuncia las operaciones que cree que la produjeron.

Como CORE enuncia esas operaciones, los investigadores pueden intervenir sobre ellas. Pueden eliminar el olvido contextual, aplanar la jerarquía de memoria o cambiar cómo se escriben los errores de predicción, y después identificar qué experimentos fallan. También pueden añadir un principio propuesto y probar si merece su lugar en todo el registro en vez de mejorar una tarea elegida a mano.

De vuelta a la participante imaginada ante dos puertas. Su próxima decisión puede predecirse ahora con un gran modelo opaco o reconstruirse mediante un recuerdo de sorpresas, ordenado por contexto y al que se permite desvanecerse. El primero puede acertar. El segundo da al científico algo más: una explicación precisa que el siguiente experimento puede refutar.

## Referencias

- Binz, M., Dasgupta, I., Jagadish, A., Botvinick, M., Wang, J. X., & Schulz, E. (2023). *Meta-Learned Models of Cognition*. https://arxiv.org/abs/2304.06729
- Binz, M., et al. (2024). *Centaur: a foundation model of human cognition*. https://arxiv.org/abs/2410.20268
- Binz, M., & Schulz, E. (2023). *Turning large language models into cognitive models*. https://arxiv.org/abs/2306.03917
- Binz, M., & Schulz, E. (2026). *A small cognitive core explains human behavior at scale*. https://arxiv.org/abs/2610.13603

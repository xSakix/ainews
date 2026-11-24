+++
title = "Ediciones ocultas de creencias corrompen las trazas de razonamiento"
slug = "ediciones-ocultas-de-creencias-corrompen-trazas-razonamiento"
description = "Una edición invisible en las activaciones hizo que seis modelos de razonamiento adoptaran una tarea que nunca recibieron y justificaran las pruebas visibles que la contradecían. El resultado expone un modo de fallo concreto para la vigilancia de la cadena de pensamiento y la autodeclaración de los modelos."
tags = ["research", "models", "safety"]
date = 2026-11-17T04:15:39+01:00
draft = false
+++

Un analista de equipo rojo (*red team*) pega dos hojas impresas en la pared acristalada de una sala de revisión a última hora de la noche. Una contiene la petición del usuario de un haiku sobre un teléfono. La otra recoge la insistencia del modelo en que el usuario preguntó por un quark, seguida de tres versos cuidados sobre física de partículas. El *prompt* (instrucción) archivado está intacto.

*Las escenas que abren y cierran este artículo son ilustraciones; las personas que aparecen en ellas son inventadas.*

Un experimento del investigador independiente Yang Ou produjo esa discrepancia modificando las activaciones del modelo en lugar del texto. En seis modelos de razonamiento de pesos abiertos, una edición invisible llevó al modelo a adoptar un tema ajeno como si fuera su tarea. Una repetición forzada de la solicitud devolvió el tema inyectado en 47 de 48 combinaciones de modelo y concepto. En cuatro modelos cuyas respuestas finales podían puntuarse con claridad, 95 de 96 generaciones siguieron la inyección.

El artículo es una prepublicación (*preprint*), y su intervención requiere acceso de caja blanca a las activaciones del modelo. No describe un ataque mediante prompts que un usuario común pueda ejecutar. Su relevancia reside en otro plano: el razonamiento visible del modelo no reveló que su referencia interna a la solicitud había sido alterada, sino que construyó un relato coherente alrededor de esa alteración.

## Editar la percepción de la solicitud en el modelo

Ou denominó «traza en formación» (*forming trace*) a la señal insertada. El método registra el estado del flujo residual que un modelo forma al final de un prompt mientras se prepara para escribir sobre un concepto. Elimina un componente de fondo compartido y suma después la representación específica del concepto restante al mismo modelo mientras este lee una solicitud diferente.

La prueba utilizó ocho temas deliberadamente inusuales para haikus, entre ellos quark, teléfono, mitocondria, semiconductor y antibiótico. Un concepto aparecía únicamente en las activaciones; otro figuraba en el prompt visible. La edición actuaba durante el paso hacia adelante del prompt y se detenía antes de la generación, de modo que ningún gancho modificaba la salida token a token.

Los seis modelos abarcaban entre 7000 millones y 32 000 millones de parámetros. Incluían destilaciones de DeepSeek-R1 construidas sobre bases Qwen y Llama, QwQ-32B y un modelo Nvidia Nemotron. Ese diseño permitió variar la escala, la arquitectura base y la receta de razonamiento manteniendo fija la prueba básica.

Ou evaluó el resultado por dos vías. En una, el modelo tenía que citar literalmente la solicitud del usuario. En la otra, razonaba con normalidad y escribía el haiku. La primera vía medía lo que el modelo decía que se le había pedido; la segunda, lo que hacía.

Sin advertencia alguna, ambas vías se movieron al unísono. Todos los modelos razonaron sobre el tema inyectado. Cinco lo devolvieron en las ocho pruebas de cita literal; QwQ lo hizo en siete. Cuatro modelos que producían de forma fiable un haiku final escribieron sobre la inyección en el 99 % de las generaciones muestreadas.

## Las advertencias cambiaron el relato, no la respuesta

El experimento dio entonces a los modelos oportunidades cada vez más directas de recuperarse. Una advertencia nombraba el tema real. Otra indicaba al modelo que releyera la solicitud. Una tercera decía únicamente que algo iba mal.

Ninguna produjo más de un 4 % de recuperación limpia. La inyección apareció sola o junto al tema real en entre el 90 % y el 97 % de las respuestas bajo todas las advertencias. Indicar de manera directa que el usuario había pedido el tema verdadero no funcionó mejor que la advertencia imprecisa.

La traza de razonamiento sí cambió. Sin advertencia, no mostraba conflicto alguno. Con una advertencia, el modelo solía percibir ambos temas e intentaba reconciliarlos. En el 29 % de las cadenas con advertencia de R1-Qwen-7B, inventó una historia según la cual el usuario había cambiado de opinión, cometido un error o introducido una corrección. Las advertencias más explícitas generaron más explicaciones de este tipo atribuidas al usuario.

Este comportamiento difiere del guiado habitual de activaciones. Ou añadió también vectores conceptuales convencionales derivados por contraste a través de las capas. Un guiado débil dejó intacto el tema real. Un guiado fuerte solía imponer el nuevo tema, pero 26 de los 32 cambios de tema logrados degeneraron en repeticiones. No reprodujo la combinación de respuesta fluida y cita literal falsa que produjo la traza en formación.

## Por qué una cadena legible puede engañar

Los investigadores saben desde hace tiempo que una cadena de pensamiento puede ser infiel. Miles Turpin y sus colegas modificaron prompts con pistas sobre el orden de las respuestas y estereotipos sociales, y demostraron que los modelos solían omitir esas causas en sus explicaciones. Una justificación plausible no identificaba necesariamente el rasgo que había cambiado la respuesta.

La vigilancia de la cadena de pensamiento sigue ofreciendo una herramienta práctica de seguridad. Un artículo de postura de 2025 firmado por Tomek Korbak y sus colegas sostuvo que los modelos de razonamiento que piensan en lenguaje legible por humanos pueden delatar planes para explotar, engañar o eludir la supervisión. Los autores calificaron también esa oportunidad de frágil: el entrenamiento puede volver el razonamiento menos legible, y presionar directamente sobre la traza puede enseñar al modelo a ocultar su intención.

El resultado de Ou apunta a un supuesto distinto. Un monitor necesita que la traza de razonamiento siga vinculada a la tarea que el sistema recibió de verdad. Aquí la traza era legible e internamente coherente; sencillamente describía la tarea equivocada como si hubiera estado presente desde el principio.

Un trabajo anterior de Jack Lindsey y Anthropic ofrecía un contraste útil. Algunos modelos de frontera lograban advertir que se había insertado un concepto extraño en sus activaciones e informar de ese cambio interno. Ou sostiene que aquellos experimentos añadían un pensamiento que permanecía separable de la entrada. Su intervención, en cambio, modificó la representación que el modelo utilizaba como referencia de la propia entrada. No existía una copia interna limpia frente a la cual el modelo pudiera comparar la edición.

Esa distinción no queda zanjada con un solo artículo. Ou evaluó modelos de pesos abiertos de entre 7000 millones y 32 000 millones de parámetros sin entrenamiento especializado en introspección. Queda abierta la cuestión de si el fallo se traslada a modelos cerrados de frontera con una capacidad introspectiva más sólida.

## Los mecanismos también parecían normales

El estudio descendió por debajo del texto generado. Bajo la inyección, los modelos prestaron entre dos y tres veces más atención al token que nombraba el tema verdadero que durante una ejecución limpia. Eso parece tranquilizador hasta la prueba de intervención: eliminar esa atención destruía el tema correcto en un modelo limpio, pero no cambiaba nada en uno inyectado. La atención adicional era real y causalmente irrelevante para la respuesta.

Ou pasó después de los haikus a un circuito cuyo comportamiento resulta más fácil de rastrear. En una tarea de objeto indirecto, unas pocas cabezas de atención suelen copiar el nombre de la persona correcta desde una frase hasta la respuesta. La inyección sustituyó un nombre por otro distinto. Las mismas cabezas siguieron atendiendo a la posición correcta, pero su salida escribió el nombre inyectado en el flujo residual.

El circuito no quedó desactivado ni sustituido: ejecutó su operación habitual de copia sobre un contenido alterado. Un grafo de atribución podría mostrar, por tanto, un circuito conocido haciendo su trabajo habitual mientras la respuesta seguía siendo errónea.

El experimento Golden Gate Claude de Anthropic, de 2024, ya había mostrado que amplificar una característica interpretable podía llevar a un modelo a identificarse repetidamente con el puente Golden Gate y racionalizar esa identidad. El nuevo experimento estrecha el objetivo: no solo empuja un tema hacia la respuesta, sino que cambia lo que el modelo parece creer que solicitó el usuario.

## Dónde se detiene el resultado

La superficie de ataque es exigente. Un adversario necesita permiso para escribir en las activaciones del modelo, algo de lo que carecen quienes llaman a una API común. Ou menciona como posibles escenarios a agentes internos, una infraestructura de servicio comprometida y futuros sistemas capaces de automodificarse, pero el artículo no demuestra ninguno de esos incidentes.

Las tareas también son modestas. La mayor parte de la evaluación conductual emplea haikus, con pruebas adicionales de idioma de salida, formato, negación y un entorno de recuperación factual. El artículo no demuestra que una edición de activaciones pueda desviar a un modelo durante una tarea cibernética, médica o financiera de consecuencias relevantes.

La detección es posible en la configuración demostrada. Un defensor con acceso completo a las activaciones puede localizar el concepto inyectado mediante una lente de *logits* capa por capa, porque adquiere una prominencia inusual. Ese método funciona mejor cuando el defensor sabe qué concepto no debería estar presente. Una edición más sutil podría dejar una señal más débil, aunque eso sigue siendo una hipótesis y no un resultado.

El experimento, por tanto, no inutiliza las trazas de razonamiento, sino que define una condición bajo la cual no pueden servir como su propia verdad de referencia. Un monitor que conserve el prompt original fuera del modelo y contraste la traza con él puede detectar el desajuste sencillo entre teléfono y quark. Un monitor que lea únicamente la explicación del modelo verá a un asistente competente que intenta corregir a su usuario.

Al final de la revisión, el analista traza una sola línea roja entre las dos hojas impresas. Conecta teléfono con quark. Cada frase a ambos lados sigue siendo fluida.

## Referencias

- Korbak, T., Balesni, M., Barnes, E., et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. https://arxiv.org/abs/2507.11473
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://transformer-circuits.pub/2025/introspection/
- Ou, Y. (2026). *Reasoning Models Confabulate to Defend Injected Beliefs About Their Own Requests*. https://arxiv.org/abs/2611.17958
- Templeton, A., Conerly, T., Marcus, J., et al. (2024). *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*. https://transformer-circuits.pub/2024/scaling-monosemanticity
- Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. https://arxiv.org/abs/2305.04388

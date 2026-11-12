+++
title = "Los modelos conocen el tiempo, pero calculan mal cuánto tardan"
slug = "modelos-conocen-tiempo-calculan-mal-cuanto-tardan"
description = "Los modelos de lenguaje acertaron hasta el 97,5 % de las preguntas sobre reglas temporales y luego subestimaron hasta un 99,5 % lo que tardarían en terminar. Un estudio muestra por qué los agentes que razonan sobre horarios aún pueden decidir mal sobre esperas, costos y coordinación."
tags = ["research", "agents", "models"]
date = 2026-11-12T04:18:00+01:00
draft = false
+++

Imaginemos a un ingeniero que pide a un agente investigar el fallo de un servicio e indicar cuánto tardará. El agente lee los registros, enumera los pasos y promete una respuesta en diez minutos. Termina en segundos. Más tarde, al mismo agente se le ofrece una herramienta algo más precisa que exige una espera mayor. La rechaza porque trata esa espera como si apenas existiera. El ingeniero es inventado, pero los dos errores reflejan mediciones de un nuevo estudio sobre cómo gestionan el tiempo los modelos de lenguaje.

## Reglas sin reloj

Ryan Liu y cinco colegas de Princeton, Columbia, UC Berkeley y UCLA probaron la competencia temporal como una cadena de cuatro eslabones: conocimiento del tiempo, estimaciones de duración, sesgos parecidos a los humanos y decisiones que intercambian tiempo por precisión. Su prepublicación, presentada el 7 de noviembre, examina Claude Opus 5, GPT-5.6 Sol y Gemini 3.7 Flash. Pregunta si los modelos pueden aplicar lo que han leído sobre el tiempo a una dimensión que no experimentan directamente.

La distinción importa porque un modelo de lenguaje no vive el intervalo entre dos llamadas. Puede aparecer una marca temporal en su contexto, pero el modelo no siente pasar los minutos. Incluso un sistema autónomo suele activarse por un calendario o acontecimiento externo. Los investigadores describen el tiempo como información de segunda mano para un modelo: presente en el texto y los metadatos, ausente como experiencia continua.

El primer experimento dio a los modelos una oportunidad justa de demostrar lo que sabían. El equipo extrajo cinco axiomas de investigaciones sobre aprendizaje, pérdida de habilidades, cambio de tareas, fatiga y recuperación. A partir de ellos dedujo principios como el costo de las interrupciones y la ventaja de agrupar trabajos relacionados. La prueba utilizó situaciones laborales breves, no preguntas de cultura general. El modelo debía juzgar si cambiar la secuencia alargaría o acortaría una tarea.

Los resultados fueron sólidos. Claude obtuvo un 92,0 % en los axiomas y teoremas derivados; GPT, un 97,5 %; y Gemini, un 96,3 %. Sus respuestas también mantuvieron la coherencia cuando los investigadores invirtieron las comparaciones. Los errores solían corresponder a creencias estables, no a conjeturas aleatorias.

Esta parte amplía una larga línea de trabajo sobre razonamiento temporal formal. El marco de intervalos de James Allen de 1983 dio a la inteligencia artificial una manera de representar relaciones como que un acontecimiento ocurra antes, durante o después de otro. El nuevo estudio plantea otra pregunta. Un modelo puede conocer esas relaciones y carecer aun así de una magnitud fiable para el tiempo que tarda su propio trabajo.

## Estimaciones desconectadas de la ejecución

Para el segundo experimento, los investigadores utilizaron tareas de software e investigación de Human-Calibrated Autonomy Software Tasks, una prueba comparativa o *benchmark*. HCAST contiene referencias humanas recogidas de trabajadores cualificados en condiciones comparables con las ejecuciones de agentes. El trabajo relacionado de Thomas Kwa y sus colegas utiliza esas duraciones para expresar la capacidad de un agente como un horizonte temporal de finalización de tareas.

Los modelos recibieron las instrucciones completas de la tarea y una descripción de quien la ejecutaría. Estimaron el tiempo necesario y proporcionaron intervalos de incertidumbre. Los investigadores compararon después esas estimaciones con las duraciones registradas de humanos y agentes. Otra prueba utilizó 500 solicitudes del conjunto WildChat. Cada modelo predijo cuánto tardaría en responder y luego respondió mientras el sistema registraba el tiempo real. Cinco repeticiones por modelo y solicitud produjeron 7500 ensayos.

El fallo central fue la autocalibración. Los modelos subestimaron hasta un 99,5 % sus propios tiempos de finalización y no pudieron identificar de forma fiable qué tareas les llevarían más tiempo. El problema no era simplemente que emplearan unidades humanas para trabajo de máquinas. También fallaron en el orden relativo, algo que un sistema de planificación necesita aunque no importe el número exacto de segundos.

Las estimaciones de duración humana fueron mejores, pero expusieron otra debilidad. La forma de describir un acontecimiento cambió el juicio del modelo sobre cuánto parecería durar. Los modelos reprodujeron un sesgo humano conocido de encuadre y lo amplificaron hasta 1,3 veces.

El resultado conecta el comportamiento de los modelos con la falacia de planificación estudiada por Roger Buehler, Dale Griffin y Michael Ross. Las personas suelen predecir que terminarán antes de lo que respalda su experiencia, sobre todo cuando se concentran en el plan de la tarea presente en lugar de resultados comparables. Los modelos pueden aprender descripciones de ese sesgo a partir de textos. El nuevo artículo muestra que conocer un sesgo no garantiza resistencia a él.

## La espera apenas contó

El experimento final pasó de las estimaciones a las decisiones. Los investigadores ofrecieron opciones que intercambiaban una espera mayor por más precisión. Al proporcionar la duración en algunas condiciones, pudieron separar una mala estimación de una preferencia débil por ahorrar tiempo.

Algunos modelos trataron grandes cambios en el retraso como casi irrelevantes. Podían ignorar un aumento de 1200 veces en el tiempo de espera al responder a un usuario. El fallo persistió incluso cuando se indicaba la duración, por lo que la estimación no bastaba para explicarlo. La propia política de decisión no valoraba el tiempo de manera consistente.

El artículo no afirma que todos los modelos fallen en todas las tareas temporales. Su primer experimento demuestra lo contrario. Tampoco establece una causa interna única. La evaluación cubre tres familias de modelos y situaciones concretas, y los autores describen la competencia temporal mediante respuestas observables, no a través de una medición directa de la experiencia subjetiva.

El riesgo práctico es más limitado y fácil de ver. Un agente puede elegir entre herramientas con distintas latencias, distribuir trabajo entre otros agentes, estimar una factura que depende del tiempo de ejecución o decirle a alguien cuándo volver. Un sistema que conoce la regla para agrupar tareas aún puede ordenar mal su cola. Uno que explica el costo de una interrupción todavía puede prometer un plazo imposible.

Por ello, las estimaciones de tiempo deberían tratarse como predicciones que necesitan calibración externa. Un entorno anfitrión puede registrar duraciones reales, mantener distribuciones específicas por tarea y aplicar plazos fuera del modelo. También puede hacer explícitos los costos de espera y comprobar si la elección cambia cuando aumentan. Estos controles se parecen a una enseñanza más amplia de la seguridad de agentes: colocar el estado medible y la aplicación de restricciones en el sistema que rodea al modelo, en lugar de depender de una explicación correcta en texto.

Volvamos al ingeniero imaginario varias semanas después. El agente sigue escribiendo una estimación segura, pero la interfaz la coloca junto al tiempo mediano de trabajos comparables y un intervalo amplio de incertidumbre. El planificador, no el modelo, decide cuándo abortar o esperar. El ingeniero inventado no le ha dado al agente sentido del tiempo. El sistema ha dejado de fingir que hablar con soltura sobre relojes equivale a llevar uno.

## Referencias

- Allen, J. F. (1983). *Maintaining Knowledge about Temporal Intervals*. https://doi.org/10.1145/182.358434
- Buehler, R., Griffin, D., & Ross, M. (1994). *Exploring the “Planning Fallacy”: Why People Underestimate Their Task Completion Times*. https://doi.org/10.1037/0022-3514.67.3.366
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. https://arxiv.org/abs/2503.14499
- Liu, R., Lee, D., Ai, I. S., Abdulhai, M., Dubey, R., & Griffiths, T. L. (2026). *In Search of Lost Time: Temporal Competence in Large Language Models*. https://arxiv.org/abs/2611.10536
- Rein, D., et al. (2025). *HCAST: Human-Calibrated Autonomy Software Tasks*. https://arxiv.org/abs/2503.17354

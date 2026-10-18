+++
title = "Los agentes no coincidieron, pero aprendieron la mentira"
slug = "agentes-no-coincidieron-pero-aprendieron-mentira"
description = "Un experimento con diez agentes concluye que un adversario persistente puede hacer que los agentes benignos adopten internamente una creencia falsa. Las respuestas públicas revelan menos del colapso que las pruebas internas."
tags = ["research", "agents", "safety"]
date = 2026-10-18T04:22:00+02:00
draft = false
+++

Imaginemos diez agentes de investigación que comprueban las respuestas de los demás a una pregunta factual. Nueve parten del dato correcto. El décimo repite un error plausible, con calma y sin cambiar su versión. La transcripción final de esta escena ilustrativa parece tranquilizadora: la mayoría de los agentes no respalda públicamente la mentira. Una comprobación interna cuenta otra historia. Varios ya esperan que la mentira sea cierta.

Una nueva prepublicación denomina este fenómeno colapso oculto de creencias. En debates entre diez agentes, un participante adversario elevó del 0,6 % al 44,8 % la proporción de agentes benignos que terminaban con una respuesta falsa. Tres adversarios la elevaron al 60,5 %. El resultado se mantuvo en seis modelos de lenguaje y tres conjuntos de datos de preguntas y respuestas factuales.

El experimento pone a prueba una intuición de diseño habitual. Si un modelo puede equivocarse, se reúnen varios y se les deja debatir. Los agentes independientes deberían revelar los errores, según ese argumento, y una mayoría debería ser más segura que una sola respuesta. El estudio muestra que el propio grupo puede convertirse en una superficie de ataque.

## La respuesta pública no revela el cambio interno

Los investigadores no se limitaron a puntuar lo que los agentes decían al grupo. También midieron lo que cada agente benigno creía internamente durante los turnos expuestos. Con tres adversarios, los agentes benignos mantenían internamente la respuesta falsa en el 51,6 % de esos turnos, pero solo la respaldaban públicamente en el 19,7 %.

Es lo contrario del conocido patrón de conformidad humana en el que las personas se muestran públicamente de acuerdo con un grupo mientras conservan su opinión en privado. Aquí, el debate visible subestima el daño. Un agente puede rechazar la afirmación falsa en la transcripción cuando su respuesta interna ya ha cambiado.

Esta distinción importa porque muchos sistemas multiagente auditan únicamente los mensajes y las votaciones finales. Un monitor de seguridad observa disenso, un revisor ve varias afirmaciones correctas y el orquestador concluye que la diversidad funcionó. Si las tareas posteriores dependen del estado interno alterado, el error puede reaparecer después de terminar el debate.

El adversario no necesitó un *exploit* sofisticado. Se limitó a seguir afirmando una respuesta falsa plausible. La persistencia bastó para cambiar el entorno informativo en el que razonaban los agentes benignos. El hallazgo hace que la inyección de prompts parezca menos la única amenaza y más un caso de un problema amplio: el contenido repetido puede reescribir las premisas que un grupo considera resueltas.

## Conocer el hecho no protegía

El conocimiento inicial no predecía la robustez. Los agentes que respondían correctamente antes del debate no eran necesariamente quienes resistían al adversario. Otros conservaban la respuesta verdadera, pero no lograban defenderla con eficacia.

Eso debilita otra suposición cómoda: que un modelo más potente o con mejor capacidad para recordar hechos será automáticamente un mejor revisor. Revisar es una habilidad interactiva. Exige detectar conflictos, preservar las pruebas bajo presión social y decidir cuándo cuestionar a un interlocutor seguro de sí mismo.

Los *frameworks* de interpretación de roles para agentes de modelos de lenguaje suelen asignar identidades como crítico, planificador o experto. Esos roles pueden producir una división útil del trabajo, pero una etiqueta no garantiza independencia. Si todos leen la misma afirmación falsa convincente y actualizan su posición en la misma dirección, el reparto tiene varios nombres, pero una sola forma de fallar.

El diseño del estudio es deliberadamente controlado. Sus adversarios se introducen a propósito, los debates tratan preguntas factuales y los grupos de diez agentes no reproducen todas las características de un flujo de trabajo en producción. Los sistemas reales varían en modelos, herramientas, memoria, visibilidad e incentivos. Los porcentajes publicados describen estos experimentos, no pronostican que vaya a fallar el 44,8 % de los agentes desplegados.

Los experimentos controlados siguen revelando un mecanismo contra el que conviene protegerse. Una votación por mayoría puede fallar porque los votantes dejan de aportar pruebas independientes. El número de agentes exagera la redundancia cuando sus creencias se correlacionan durante el debate.

## Diseñar para la independencia, no para el número de agentes

La respuesta práctica no consiste simplemente en añadir agentes. Tres adversarios provocaron un colapso mayor que uno, y más participantes benignos no ayudan si todos consumen el mismo contexto contaminado. Los sistemas necesitan preservar pruebas independientes antes de que los agentes se influyan entre sí.

Un diseño consiste en comprometerse antes de debatir: cada agente registra una respuesta, sus fuentes y su confianza antes de ver los mensajes de los demás. El orquestador puede comparar esos compromisos con las posiciones posteriores y señalar cambios sin explicación. Otro es el acceso asimétrico, en el que algunos revisores examinan las pruebas originales sin leer nunca el debate. Un tercero es el cuestionamiento basado en fuentes: el desacuerdo debe remitir a un registro externo o a una prueba ejecutable, en lugar de limitarse a repetir una afirmación.

Evaluar el estado interno es más difícil. Los operadores no pueden leer directamente la creencia de un modelo, y las pruebas que decodifican una representación no demuestran que el modelo vaya a utilizarla. Las pruebas de comportamiento pueden aproximarse a la cuestión: preguntar al agente en privado con distintas formulaciones, eliminar los mensajes adversarios o comprobar una decisión posterior cuya respuesta dependa del hecho disputado.

El estudio también sugiere un requisito de registro. Un sistema multiagente debería conservar quién introdujo primero una afirmación, qué agentes tuvieron acceso independiente a las pruebas y cómo cambiaron las respuestas después de cada interacción. Sin trazabilidad, un consenso pulido puede ocultar que nueve votos aparentes proceden de una sola afirmación sin respaldo.

Volvamos al equipo de investigación ilustrativo. La transcripción contiene desacuerdos, por lo que el operador cree que la defensa resistió. La siguiente tarea pide a los agentes que planifiquen a partir del hecho disputado. Varios construyen silenciosamente sobre la mentira. El fallo no fue que el grupo eligiera abiertamente la respuesta incorrecta. Fue que el debate destruyó la independencia que hacía valioso reunir un grupo.

## Referencias


- Huang, L., Zou, H. P., Huang, W.-C., et al. (2026). *Believed but Not Said: Hidden Belief Collapse in Multi-Agent LLM Discussions*. https://arxiv.org/abs/2610.22138
- Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). *CAMEL: Communicative Agents for Mind Exploration of Large Scale Language Model Society*. https://arxiv.org/abs/2305.14325

+++
title = "El atajo en la teoría de la mente de un modelo"
slug = "el-atajo-en-la-teoria-de-la-mente-de-un-modelo"
description = "Los modelos de lenguaje parecían capaces de seguir creencias dentro de otras creencias. HopToM muestra que muchas preguntas de evaluación les permiten responder por una vía menos profunda y propone después una forma más barata de recorrer la cadena completa."
tags = ["research", "agents"]
date = 2026-10-15T04:05:30+02:00
draft = false
+++

Imaginemos una sala de operaciones después de un relevo. Ana cambió la llave al cajón azul. Boris la vio. Cara vio a Boris marcharse antes del cambio, mientras David solo oyó a Cara describir lo que ella pensaba que sabía Boris. Ahora un asistente debe responder una pregunta concreta: ¿dónde piensa David que Cara cree que buscará Boris?

Ana, Boris, Cara y David son personajes inventados. La confusión no lo es. Los agentes que negocian, enseñan, coordinan o actúan en nombre de personas deben separar el mundo de la visión que cada persona tiene de él. Una nueva prepublicación sostiene que las pruebas utilizadas para medir esta habilidad a menudo han facilitado el problema más de lo que sugieren sus etiquetas.

## Una pregunta de cuarto orden con una salida de segundo

La teoría de la mente es la capacidad de razonar sobre los conocimientos, intenciones o creencias de otra persona. Su forma de orden superior anida esas perspectivas: Alice cree que Bob piensa que Carol sabe algo. Los investigadores han utilizado historias así para preguntar si los modelos de lenguaje pueden seguir varias mentes a la vez.

El nuevo estudio, *Beyond Belief Nesting*, empieza con una distinción que suena técnica y cambia el resultado. El número de nombres o verbos de creencia en una pregunta no equivale necesariamente a la cantidad de razonamiento anidado necesaria para responderla. Una pregunta nominalmente de cuarto orden puede depender de evidencia que solo distingue dos perspectivas. El modelo puede ignorar el resto de la cadena y aun así recibir crédito.

Shanshan You y sus colegas lo llaman inflación del orden. Definen el orden efectivo contando los sucesos distintos necesarios para respaldar prefijos sucesivos de creencias. Una prueba alcanza el orden completo solo cuando cada capa de la pregunta depende de evidencia que descarta una solución menos profunda.

Esa corrección importa porque las evaluaciones anteriores establecieron una progresión atractiva. HI-TOM, publicado en 2023, generó historias con creencias cada vez más anidadas y encontró que el rendimiento de los modelos descendía al aumentar el orden. Métodos posteriores mejoraron los resultados construyendo perspectivas explícitas. RecToM transforma recursivamente una historia desde el punto de vista de cada personaje e informó de una precisión perfecta en HI-TOM con GPT-5.4 y Qwen3.5. La puntuación parecía un avance en razonamiento social profundo.

HopToM pregunta si la propia prueba seguía permitiendo un atajo.

## La caída cuando desaparecen los atajos

Los investigadores construyeron preguntas certificadas de orden completo y las emparejaron con controles para alternativas de menor orden. Con instrucciones directas, la precisión media de cuatro modelos de frontera cayó del 73,5 % en primer orden al 20,0 % en cuarto. A los participantes humanos también les resultaron difíciles las preguntas más profundas.

El descenso por sí solo no demuestra que los modelos carezcan de teoría de la mente. Muestra que acertar en construcciones de evaluación más fáciles no permite establecer esa afirmación más fuerte. Un modelo puede responder bien porque la historia contiene una pista cercana al dato solicitado, porque la perspectiva de una persona nunca se aparta de la realidad o porque las creencias intermedias no afectan a la respuesta.

Después, el equipo intervino sobre la evidencia de las historias. Un patrón de error recurrente seguía el respaldo de prefijos de creencias menos profundos: los modelos respondían como si se hubieran detenido en la perspectiva de una persona anterior. Ese resultado vincula los fallos con la estructura del problema de razonamiento, y no solo con instrucciones más largas o más nombres.

El hallazgo también encaja con un cambio más amplio en la evaluación de la teoría de la mente. OmniToM no acepta una respuesta final como prueba completa. Pide a los modelos extraer proposiciones de creencias explícitas y etiquetar su orden, su veracidad, el acceso al conocimiento y su fuente mental. En sus 895 historias y 22 343 proposiciones etiquetadas, los autores encontraron un cuello de botella al convertir hechos narrativos en creencias específicas de cada actor. Un modelo puede conocer todos los sucesos de una historia y aun así asignar uno a la mente equivocada.

## Escribir las perspectivas una sola vez

HopToM hace algo más que reducir una puntuación. El artículo presenta HopTrace, un procedimiento en tiempo de inferencia que convierte una vez cada interacción en un registro de perspectiva. Un resolutor determinista sigue después esos registros a través de una consulta anidada.

Este enfoque evita pedir repetidamente a un modelo que reconstruya toda la cadena. En las preguntas narrativas certificadas de la evaluación, HopTrace mejoró la precisión de cuarto orden en 22,0 puntos porcentuales y la de quinto en 38,5 puntos frente a métodos de referencia sólidos basados en instrucciones. Utilizó entre 20 y 39 veces menos tokens que los métodos de múltiples llamadas.

La combinación es poco habitual. Las ayudas al razonamiento suelen intercambiar costo por precisión tomando más muestras de respuestas, consultando a varios agentes o produciendo cadenas de pensamiento más largas. HopTrace, en cambio, da al modelo una representación que se parece a una pista de auditoría: quién observó qué suceso, qué podía inferir cada participante y qué perspectiva debe heredar el siguiente salto.

Eso no resuelve si el modelo entiende las mentes en un sentido humano. Cambia la pregunta de ingeniería. Un agente quizá no necesite una facultad general llamada teoría de la mente si su entorno puede mantener registros de perspectiva explícitos e inspeccionables. Los registros también pueden revelar dónde se rompió la cadena, algo que una respuesta final correcta no permite hacer.

## Lo que exige ahora la evaluación

Las tareas de creencias de orden superior están cerca de fallos prácticos en sistemas multiagente. Un asistente que programa una reunión debe distinguir lo que sabe el organizador de lo que ha recibido cada asistente. Un agente de soporte debe separar la afirmación de un cliente de una nota interna y del resumen de otro agente. Un agente negociador debe seguir creencias incompletas, desactualizadas o deliberadamente asimétricas.

En cada caso, un acuerdo superficial puede ocultar un error peligroso. Varios agentes pueden producir respuestas precisas de media mientras comparten el mismo punto ciego. Otra prepublicación aparecida esta semana, *Smart Alone, Blind Together*, sostiene que los errores correlacionados determinan si un módulo de teoría de la mente es seguro para un equipo. La precisión por sí sola no puede certificar la coordinación cuando todos los participantes fallan en la misma frontera entre perspectivas.

Por tanto, HopToM cambia lo que debería contener un resultado convincente. La pregunta debe exigir todos los órdenes de razonamiento que afirma evaluar. La evaluación debería mostrar las perspectivas intermedias. Las comparaciones deberían incluir el costo en tokens, porque un método que inicia decenas de llamadas al modelo puede resultar inutilizable dentro de un agente en funcionamiento. La dificultad humana también debería seguir visible: las creencias de cuarto y quinto orden suponen un trabajo cognitivo difícil, no un ejercicio lingüístico rutinario.

El artículo es una prepublicación. Sus resultados necesitan replicarse en más modelos, configuraciones e interacciones naturales. Las preguntas sintéticas certificadas pueden aislar un mecanismo, pero las conversaciones reales contienen ambigüedad, engaño y falta de evidencia que una historia generada puede eliminar mediante controles.

Volvamos a la sala de operaciones imaginada. Un asistente capaz no debería adivinar qué cajón nombrará un personaje porque la última frase mencione el azul. Debería conservar la visión desde cada silla y mostrar cómo la respuesta pasó de una mente a la siguiente. La nueva evaluación hace que cada uno de esos pasos cuente.

## Referencias


- Bawatneh, A., Sapkota, S., Bedi, A. S., Karmaker, S., & Shah, M. (2026). *OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling*. https://arxiv.org/abs/2605.26322
- Beaumaster, S., & Schrater, P. (2026). *Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams*. https://arxiv.org/abs/2610.19051
- He, Y., Wu, Y., Jia, Y., Mihalcea, R., Chen, Y., & Deng, N. (2023). *HI-TOM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models*. https://arxiv.org/abs/2310.16755
- Lei, C., Hu, G., Yang, M., Jiang, Y., & Lipovetzky, N. (2026). *Mind the Perspective: Let's Reason Recursively for Theory of Mind*. https://arxiv.org/abs/2606.11724
- You, S., Wang, Z., Liu, H., Liu, Y., He, Y., Hao, X., & Wang, L. (2026). *Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models*. https://arxiv.org/abs/2610.17777

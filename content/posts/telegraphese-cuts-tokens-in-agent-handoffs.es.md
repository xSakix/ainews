+++
title = "El estilo telegráfico reduce tokens en los traspasos entre agentes"
slug = "estilo-telegrafico-reduce-tokens-traspasos-agentes"
description = "Una prueba pública concluye que una instrucción permite a varios modelos escribir registros legibles por máquinas con cerca de la mitad de tokens de salida. La técnica falla durante el razonamiento activo."
tags = ["agents", "research", "tools"]
date = 2026-10-10T03:58:41+02:00
draft = false
+++

Pedir a modelos de lenguaje que escribieran en estilo telegráfico redujo su salida alrededor del 40–49 %, mientras otros modelos recuperaban los hechos registrados con una precisión comparable.

El desarrollador independiente Travis Smith probó la instrucción en 50 pasajes y unas 1300 preguntas. El método pide eliminar artículos y relleno, abreviar, conservar cada hecho, cifra y nombre propio, y usar minúsculas para que las mayúsculas no eleven el número de tokens.

## Por qué importa {#why-it-matters}

Un desarrollador de agentes paga una vez cuando un modelo escribe una memoria y de nuevo cada vez que otro la lee. Comprimir notas entre máquinas una vez terminado el trabajo puede reducir tanto la factura de salida como el contexto ocupado por traspasos repetidos.

La prueba separa escritura y lectura. Gemma 4, Qwen3.8 y GLM-5.3-Flash escribieron registros condensados, mientras modelos de varias familias respondían preguntas ancladas en esos registros o en resúmenes normales. Smith publicó el entorno de pruebas, registros de resultados congelados y un cuaderno ejecutable.

El resultado más claro vino de los escritores. Gemma utilizó aproximadamente un 40 % menos de tokens de salida facturados, mientras Qwen y GLM ahorraron alrededor del 49 %. Los lectores que respondían con registros comprimidos alcanzaron entre 0,99 y 1,10 veces su precisión con resúmenes normales. Cuatro familias lectoras no recibieron ningún ejemplo resuelto del estilo, lo que sugiere que la convención ya les resultaba familiar por los datos de entrenamiento.

## La compresión debe ir después del razonamiento

El lugar de aplicación cambió el resultado. Los modelos a los que se pidió formular respuestas directamente en estilo telegráfico conservaron solo unas cuatro quintas partes de su precisión normal. Cuando el contenido se resolvía primero y luego se comprimía en un registro, la lectura posterior igualaba o superaba ligeramente el control de resumen normal.

Eso hace adecuada la técnica para archivos de notas de trabajo, memorias de agentes y traspasos. Encaja mal en una respuesta para el usuario o en un paso donde el modelo aún decide qué decir. El texto comprimido sigue siendo legible por personas, pero es deliberadamente menos cómodo que la prosa normal.

El razonamiento obligatorio creó otra forma de fallo. GPT-5-mini produjo menos tokens visibles, pero gastó aproximadamente tres veces más en razonamiento oculto, según el registro del autor, lo que encareció la escritura total. Un equipo necesita probar el contador real de facturación del proveedor en lugar de contar solo caracteres o tokens visibles.

Smith también midió un recorrido de ida y vuelta que expandía el texto comprimido de nuevo a prosa. El resultado almacenado seguía siendo menor que un resumen normal, pero la llamada adicional consumía más tokens de los que ahorraba la escritura inicial. Lecturas baratas repetidas pueden recuperar ese costo; un flujo de una escritura y una lectura quizá no.

El encuadre histórico puede no ser esencial. Smith no hizo el control estricto de pedir máxima concisión sin mencionar el estilo telegráfico. Por tanto, el experimento respalda la instrucción práctica, pero no establece que el propio estilo telegráfico cause la mejora.

El resultado sigue siendo además una prueba ejecutada por el autor. Sus fortalezas son materiales inusualmente inspeccionables y pruebas entre familias; su límite es que pasajes, preguntas y evaluadores definen un tipo de registro factual. Código, derivaciones matemáticas y memoria conversacional pueden comprimirse de otro modo.

El cuaderno publicado ya puede ejecutarse con transcripciones de agentes en producción, permitiendo comparar éxito de tareas y tokens facturados por proveedores con el tráfico propio.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| Las instrucciones de estilo telegráfico redujeron los tokens de salida facturados alrededor del 40–49 % en escritores Gemma, Qwen y GLM | SEGÚN LA EMPRESA | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | ninguna |
| Lectores de distintas familias recuperaron hechos con una precisión de 0,99–1,10 respecto a los resúmenes en texto normal | SEGÚN LA EMPRESA | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | ninguna |
| Componer respuestas directamente en estilo telegráfico redujo la precisión a alrededor de 0,81 respecto al control normal | SEGÚN LA EMPRESA | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | ninguna |
| El razonamiento obligatorio de GPT-5-mini anuló el ahorro de tokens visibles en la prueba del autor | SEGÚN LA EMPRESA | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | ninguna |
| El entorno de pruebas, los registros congelados y el cuaderno son públicos | VERIFICADO | https://github.com/Travis42/telegraph-test | ninguna |
| El método encaja mejor en registros legibles por máquinas ya resueltos que en razonamiento activo | ANÁLISIS | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | ninguna |

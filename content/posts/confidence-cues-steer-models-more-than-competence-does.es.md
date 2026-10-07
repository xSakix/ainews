+++
title = "La confianza declarada guía a los modelos más que su capacidad"
description = "Un estudio controlado observa que una frase de confianza o duda puede cambiar notablemente si un modelo de razonamiento llama a una herramienta, pero esos cambios rara vez se dirigen a los problemas donde hace falta ayuda."
slug = "confianza-declarada-guia-modelos-mas-que-su-capacidad"
tags = ["research", "agents"]
date = 2026-10-05T04:00:30+02:00
draft = false
+++

Al decirle a un modelo de razonamiento «Confío en mi respuesta», disminuye su probabilidad de pedir ayuda a una herramienta. Al decirle al mismo modelo «No estoy seguro de mi respuesta» en el mismo punto de la misma secuencia de razonamiento, delega más a menudo. Lo llamativo no es que el lenguaje cambie el comportamiento, sino que el cambio apenas se relaciona con si el modelo puede resolver el problema sin ayuda.

Rohit Saxena y Utkarsh Upadhyay llaman a esta propiedad «susceptibilidad a la orientación». Su preprint prueba si el lenguaje de confianza puede guiar la decisión de un modelo entre responder directamente o llamar a una herramienta y, por separado, si esa orientación afecta a los problemas donde la herramienta es realmente útil.

Esa separación importa para los agentes. Un sistema puede responder mucho a una señal de incertidumbre y aun así malgastar tiempo y dinero llamando a herramientas para preguntas fáciles, mientras se reserva con confianza las difíciles. Delegar más no significa necesariamente delegar mejor.

## Una frase, dos ejecuciones contrafactuales

El experimento comienza con un problema, un prompt y un prefijo de razonamiento generado por el modelo idénticos. En un punto fijo, los investigadores insertan una de dos frases en primera persona que expresan confianza o duda. El modelo puede continuar razonando antes de decidir si responde o delega. Como todo lo anterior a la frase insertada se mantiene constante, la diferencia entre las dos ejecuciones aísla el efecto de la frase.

El estudio abarca nueve modelos de razonamiento de pesos abiertos de las familias Qwen, Gemma y GLM en MuSiQue y StrategyQA, además de modelos DeepSeek y MiniMax más grandes alojados por proveedores. Sus ejecuciones principales utilizan decodificación voraz, con experimentos adicionales de decodificación por muestreo y de control.

En los experimentos con modelos de pesos abiertos, pasar de confianza a duda cambia la delegación en una mediana de 20,6 puntos porcentuales. Los modelos alojados más grandes cambian entre 53 y 70 puntos. Un control que corta y regenera sin ninguna de las dos frases resulta casi inerte en la mediana, y cerrar el bloque de razonamiento inmediatamente después de la frase conserva la dirección del efecto.

Estos resultados muestran un punto de control causal potente. No demuestran que los modelos hayan descubierto su propia incertidumbre.

## La sensibilidad no es autoconocimiento

Para probar si los cambios de comportamiento son útiles, los autores los comparan con la capacidad de cada modelo sin ayuda. Un buen cambio envía a la herramienta un problema que el modelo resolvería mal o deja al modelo uno que puede resolver. Solo una mediana del 42 % de los cambios inducidos está bien dirigida. Esto supone una mejora de dos puntos frente a seleccionar al azar el mismo número de problemas.

En términos sencillos, la señal de confianza inyectada se parece más a una instrucción que a una lectura de autoconocimiento. Mueve con fuerza la decisión de usar herramientas, pero esa decisión apenas distingue entre «Necesito ayuda» y «Puedo resolverlo». El experimento proporciona deliberadamente la frase de confianza desde fuera; no prueba si un modelo puede generar por sí mismo una señal bien calibrada.

## Qué deben medir los desarrolladores de agentes

La lección práctica es comunicar dos cifras para cualquier política reflexiva de uso de herramientas: cuánto cambia el comportamiento y hasta qué punto esos cambios responden a una necesidad real. Una intervención de enrutamiento que solo aumenta la tasa de llamadas a herramientas puede parecer exitosa mientras simplemente añade latencia. Otra que reduce las llamadas puede parecer eficiente mientras conserva errores cometidos con confianza.

Los autores también advierten que sus tareas y su intervención son limitadas. El artículo no establece cómo se comporta un agente en producción con muchas herramientas, costes cambiantes o instrucciones adversarias, y la publicación de su código está prometida, pero no acompaña al preprint. Su aportación es un diagnóstico claro: antes de confiar en la seguridad que declara un modelo para controlar el acceso a herramientas más potentes, comprobar si esa confianza predice su capacidad en lugar de limitarse a ordenar su comportamiento.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| El diseño inserta confianza o duda en el mismo punto de un prefijo de razonamiento idéntico | VERIFICADO | [Preprint](https://arxiv.org/abs/2609.34572) | ninguna |
| Nueve modelos de razonamiento de pesos abiertos de Qwen, Gemma y GLM, además de modelos DeepSeek y MiniMax alojados | VERIFICADO | [Preprint](https://arxiv.org/abs/2609.34572) | ninguna |
| Cambio mediano de delegación de 20,6 puntos en modelos abiertos y de entre 53 y 70 puntos en modelos alojados | SEGÚN LA EMPRESA | [Preprint](https://arxiv.org/abs/2609.34572) | ninguna; experimentos de los autores |
| Mediana del 42 % de cambios bien dirigidos, dos puntos por encima de una selección aleatoria equivalente | SEGÚN LA EMPRESA | [Preprint](https://arxiv.org/abs/2609.34572) | ninguna; experimentos de los autores |
| El lenguaje de confianza se comporta más como una entrada de control que como evidencia de autoconocimiento del modelo | ANÁLISIS | [Preprint](https://arxiv.org/abs/2609.34572) | interpretación coherente con el resultado de los autores sobre la selección de problemas |
| El código aún no está disponible | VERIFICADO | [Preprint](https://arxiv.org/abs/2609.34572) | la declaración de reproducibilidad indica que su publicación está prevista cuando se publique el artículo |

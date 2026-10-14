+++
title = "MASS entrena un modelo mediante equipos de agentes"
slug = "mass-entrena-modelo-mediante-equipos-agentes"
description = "Sakana AI y UC Berkeley usan un modelo para diseñar, ejecutar y evaluar flujos multiagente y después lo entrenan con los mejores resultados de los equipos."
tags = ["research", "agents"]
date = 2026-10-12T03:58:37+02:00
draft = false
+++

Sakana AI y UC Berkeley han presentado MASS, un método de entrenamiento en el que un modelo mejora diseñando equipos de agentes, evaluando su trabajo y aprendiendo de los mejores resultados.

La prepublicación se dirige a tareas de investigación cuyas respuestas no pueden comprobarse con un compilador o una solución exacta. En vez de fijar manualmente un flujo multiagente, el mismo modelo subyacente escribe funciones, instrucciones, contratos de salida y orden de llamadas, ejecuta el equipo resultante y puntúa respuestas candidatas.

## Por qué importa {#why-it-matters}

Para un equipo que construye agentes de investigación, diseñar flujos suele ser otro proyecto manual de ingeniería de prompts. MASS convierte ese diseño en parte del entrenamiento y elimina la maquinaria multiagente en el despliegue, para que el modelo individual mejorado responda sin pagar todo el proceso de búsqueda.

El método tiene dos bucles. En el interno, un optimizador de flujos propone estructuras de equipo escritas y un ejecutor las ejecuta. Un evaluador elige resultados más sólidos de tareas sin datos de referencia automáticos. En el externo, se ajusta el modelo con esas ejecuciones seleccionadas y se convierte en el punto de partida de otra ronda.

Los autores comparan el proceso con jugar contra uno mismo, pero el oponente no es otro jugador. El modelo crea formas de cooperación cada vez más exigentes para copias de sí mismo y absorbe después el mejor comportamiento en un punto de control. Por tanto, la topología del equipo es un andamiaje temporal de entrenamiento, no un requisito permanente de inferencia.

## La calidad de la selección es la dependencia crítica

MASS depende de juicios basados en modelos porque sus preguntas de investigación objetivo carecen de un oráculo determinista. El artículo utiliza modelos de frontera separados, incluidos GPT-5.5 y Claude Opus 4.8, como jueces reservados para la evaluación. Sakana informa de que el modelo entrenado mejora la calidad juzgada de sus respuestas usando menos tokens de salida que los equipos multiagente que generaron su material de entrenamiento.

Esas pruebas siguen siendo internas a la evaluación con modelos de lenguaje. Un juez puede preferir respuestas pulidas, familiares o extensas sin medir si una afirmación científica es cierta. Los jueces reservados reducen el sobreajuste directo a un evaluador, pero no aportan una verdad fáctica de referencia. El resultado se interpreta mejor como mejora bajo el protocolo de evaluación del artículo.

El procedimiento intenta limitar el colapso hacia un solo flujo afortunado. Cada generación ejecuta un torneo de campeones 18 veces y conserva las mejores 16 trazas de equipos para ajuste fino. El optimizador puede cambiar descripciones de funciones, orden de comunicación y formatos de salida, lo que le da más libertad que elegir entre unos pocos prompts fijos.

El diseño de modelo compartido también restringe la afirmación. Ejecutor, optimizador y evaluador son funciones de una familia de modelos, no un mercado de sistemas especializados independientemente. Eso facilita atribuir la mejora recursiva al bucle de entrenamiento y deja abierto si equipos heterogéneos descubrirían estrategias distintas.

## El flujo desaparece tras el entrenamiento

La característica práctica más clara es la destilación en el modelo base. Un usuario en despliegue no necesita repetir el torneo de 18 ejecuciones ni mantener el grafo final del equipo. El cómputo adicional se concentra en generar datos y entrenar, mientras la inferencia usa directamente el modelo resultante.

El artículo y la descripción del proyecto son públicos y permiten inspeccionar más de cerca prompts y diseño de evaluación. La reproducción independiente tendrá que probar si las mejoras sobreviven a otros jueces, verificación fáctica y tareas fuera del conjunto de investigación de los autores.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| MASS usa un modelo como optimizador de flujos, ejecutor y evaluador y luego lo ajusta con ejecuciones seleccionadas de equipos | VERIFICADO | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| El bucle interno busca funciones de equipo escritas, instrucciones, contratos de salida y orden de llamadas | VERIFICADO | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| Los autores informan de mayor calidad juzgada con menos tokens de salida tras el entrenamiento | SEGÚN LA EMPRESA | https://pub.sakana.ai/mass/ | ninguna |
| GPT-5.5 y Claude Opus 4.8 sirven como jueces externos reservados en la evaluación descrita | VERIFICADO | https://arxiv.org/abs/2610.12176 | ninguna |
| La evaluación basada en modelos no establece independientemente la corrección fáctica | ANÁLISIS | https://arxiv.org/abs/2610.12176 | ninguna |

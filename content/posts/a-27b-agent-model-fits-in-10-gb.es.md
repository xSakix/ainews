+++
title = "Un modelo de agentes de 27 000 millones de parámetros cabe en 10 GB"
slug = "un-modelo-de-agentes-de-27-000-millones-cabe-en-10-gb"
description = "Nari Labs comprimió Qwen3.8-27B de 53,8 GB a 10,12 GB e igualó a su original en BF16 en varias pruebas comparativas largas de agentes. El resultado depende de datos de calibración generados por agentes y de una bifurcación especializada de inferencia, lo que limita dónde pueden ejecutarse los archivos más pequeños."
tags = ["models", "agents", "research", "hardware"]
date = 2026-11-24T04:21:00+01:00
draft = false
+++

La descarga terminó en una estación de trabajo con 16 gigabytes de memoria gráfica. Un modelo de 27 000 millones de parámetros que normalmente requería 53,8 gigabytes cabía en un único archivo de 10,12 gigabytes. El ingeniero inició un agente de programación y lo observó invocar herramientas, leer los resultados y continuar en lugar de fallar a mitad de la tarea.

*Las escenas que abren y cierran este artículo son ilustraciones; las personas que aparecen en ellas son inventadas.*

Nari Labs publicó el 20 de noviembre tres versiones comprimidas de Qwen3.8-27B, de Alibaba. Sus archivos de tres y de 2,5 bits igualaron al modelo original en BF16 en las pruebas del laboratorio sobre tareas largas de programación y terminal. El archivo de dos bits no lo logró. El lanzamiento plantea una afirmación práctica y otra metodológica: un modelo puede perder casi cuatro quintas partes del espacio que ocupan sus pesos sin perder el comportamiento que necesitan los agentes, siempre que el proceso de compresión aprenda del trabajo de los agentes en lugar de texto común.

## El texto equivocado para la tarea

La cuantización sustituye los números de alta precisión en los pesos de un modelo por representaciones más pequeñas. Menos bits reducen la memoria y el ancho de banda, lo que puede convertir un modelo que necesita un servidor en uno que cabe en una estación de trabajo. El coste es la aproximación. Cada peso comprimido se aparta del original y los errores pueden acumularse a medida que el modelo genera una respuesta larga o avanza por numerosos pasos.

La mayoría de los conjuntos de calibración se componen de pasajes breves tomados de la web. Un cuantizador usa esos pasajes para aprender qué errores importan y cómo distribuir un conjunto limitado de valores numéricos. Doyeob Kim, único autor del informe de NariQ, sostiene que esos datos no representan el trabajo de un agente de programación. Un agente puede operar a lo largo de más de 100 000 tokens, alternar entre razonamiento y llamadas a herramientas, y reaccionar a la salida de una terminal durante muchos turnos.

Ese desajuste aparece en resultados anteriores. Según el artículo de Kim, cuantizaciones previas de Qwen3.8-27B a tres bits o menos pueden igualar a BF16 en los problemas breves de matemáticas de AIME mientras resuelven como máximo un 72 % de las tareas de DeepSWE. Un modelo que recuerda datos y completa cálculos aislados puede igualmente perder el rumbo durante un intercambio prolongado con un repositorio de software.

NariQ cambia el material de calibración. Registra los tokens que generó el modelo completo en BF16 durante sesiones de agentes y luego emplea esas trazas para guiar la elección de los pesos comprimidos. El modelo ve el tipo de secuencia al que deberá sobrevivir después: planes, solicitudes a herramientas, observaciones y revisiones.

## Rejillas y trazas

La maquinaria numérica parte de QTIP, un método de 2024 desarrollado por James Tseng y sus colegas. QTIP combina cuantización con codificación en rejilla y una transformación de incoherencia para asignar grupos de pesos a palabras código compactas. La rejilla busca entre secuencias posibles en lugar de redondear cada peso por separado.

NariQ une esa maquinaria con la calibración procedente de la actividad objetivo. La distinción importa porque un cuantizador puede preservar la probabilidad media del siguiente token mientras daña un pequeño conjunto de decisiones que determinan si un agente se recupera tras un comando fallido. Las tareas largas exponen esas decisiones una y otra vez.

Los archivos publicados abarcan tres, 2,5 y dos bits por peso. Mantienen la torre de visión y la caché clave-valor de Qwen3.8-27B en BF16, por lo que la anchura en bits anunciada describe los pesos del modelo de lenguaje y no cada byte que consume la inferencia. El modelo base es un modelo denso visión-lenguaje con 64 capas y una longitud de contexto nativa de 262 144 tokens. Admite nivel de razonamiento ajustable y conserva el contenido del razonamiento entre turnos de forma predeterminada.

Nari Labs evaluó los archivos comprimidos junto al punto de control original en BF16 de 53,8 gigabytes. En DeepSWE v1.1, que consta de 113 tareas ejecutadas tres veces, BF16 obtuvo 39,8 en pass@1. El archivo de tres bits obtuvo 41,0 y el de 2,5 bits, 41,9. Terminal-Bench 2.1 dio 62,6 para BF16, 63,8 para tres bits y 60,2 para 2,5 bits.

El patrón continuó en los conjuntos matemáticos AIME 2025 y 2026. BF16 obtuvo 97,7; la versión de tres bits, 98,3; y la de 2,5 bits, 96,5. RealWorldQA, una prueba comparativa (*benchmark*) de visión, situó empatados a BF16 y a la versión de tres bits en 82,4. Diferencias tan pequeñas no prueban que la compresión mejore el modelo; el muestreo repetido puede desplazar la puntuación de un benchmark de agentes. Sí respaldan la conclusión más acotada de que los dos archivos mayores de NariQ no quedaron por detrás de forma medible en estas pruebas.

## El límite de los dos bits

El archivo más pequeño muestra dónde se detiene la afirmación. Con dos bits por peso, DeepSWE cayó a 28,6, Terminal-Bench a 52,4 y AIME a 86,0. La compresión cruzó un umbral a partir del cual la calibración ya no pudo recuperar el comportamiento del modelo original.

El conjunto de benchmarks también pertenece al desarrollador. Nari Labs eligió el modelo, las trazas de calibración, la implementación y la configuración de evaluación. El informe tiene un solo autor y no ha pasado por revisión por pares. Ejecuciones independientes con distintos agentes, repositorios y hardware comprobarían si la paridad se mantiene más allá de la tabla publicada.

Existe otra frontera entre un archivo pequeño y un modelo accesible. NariQ exige la bifurcación (*fork*) de llama.cpp de la propia empresa porque el formato de pesos y los núcleos de cómputo no forman parte del proyecto estándar. Ni llama.cpp estándar, ni Ollama ni LM Studio pueden cargar los archivos. La bifurcación está optimizada para la arquitectura SM120 de Nvidia. Nari Labs señala que funciona más despacio en tarjetas Ampere, Ada y Hopper, no es compatible con GPU de AMD ni de Intel y sigue siendo lenta en Apple Metal.

Esa salvedad cambia el sentido de «local». Diez gigabytes colocan los pesos dentro del margen de memoria de muchas tarjetas gráficas de consumo, pero la ruta de software todavía no atiende bien a buena parte de esas tarjetas. La ficha del modelo sin comprimir de Qwen, en cambio, enumera frameworks de servicio consolidados como Transformers, vLLM y SGLang. Los archivos de NariQ intercambian esa amplia compatibilidad por su reducido tamaño.

## Qué mide el archivo

El trabajo sugiere una forma distinta de juzgar los modelos de pocos bits. La perplejidad y los exámenes breves resultan cómodos porque son baratos y repetibles. No ejercitan los bucles que hacen útil a un agente: mantener un objetivo, elegir herramientas, leer errores y volver a intentarlo. Los datos de calibración pueden arrastrar el mismo punto ciego que una evaluación.

NariQ no hace que un modelo de 27 000 millones de parámetros resulte universalmente barato. El contexto completo sigue consumiendo memoria clave-valor, el codificador de visión permanece en alta precisión y la velocidad de inferencia depende de núcleos diseñados para un dispositivo concreto. Sí muestra que el almacenamiento de pesos y la competencia de un agente no tienen por qué degradarse juntos a tres o 2,5 bits en las tareas evaluadas.

De vuelta en la estación de trabajo, el agente llegó al final de su tarea en la terminal. El archivo de 10,12 gigabytes había cabido desde el principio. Que el siguiente equipo pueda ejecutarlo depende menos del archivo que del nombre impreso en su chip gráfico.

## Referencias

- Kim, D. (2026). *NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks*. https://arxiv.org/abs/2611.26157
- Nari Labs (2026). *Qwen3.8-27B-NariQ-GGUF model card*. https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
- Qwen Team (2026). *Qwen3.8-27B model card*. https://huggingface.co/Qwen/Qwen3.8-27B
- Tseng, J., et al. (2024). *QTIP: Quantization with Trellises and Incoherence Processing*. https://arxiv.org/abs/2406.11235

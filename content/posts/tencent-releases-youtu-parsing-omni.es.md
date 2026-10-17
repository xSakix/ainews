+++
title = "Tencent publica Youtu-Parsing-Omni"
slug = "tencent-publica-youtu-parsing-omni"
description = "El modelo de 5 mil millones de parámetros transforma documentos, imágenes, audio y video en un formato JSON estructurado único. Tencent ha publicado pesos, código y un informe técnico."
tags = ["models", "tools"]
date = 2026-10-10T04:02:41+02:00
draft = false
+++

El laboratorio Youtu de Tencent ha publicado un modelo de 5 mil millones de parámetros que analiza seis tipos de medios y los convierte a un formato JSON estructurado único.

Youtu-Parsing-Omni acepta páginas de documentos, imágenes naturales, gráficos, figuras geométricas, audio y video. Puede devolver texto, tablas, fórmulas, cuadros de disposición, marcas temporales, transcripciones de voz, leyendas y descripciones de movimientos de cámara sin cambiar entre modelos especializados separados.

## Por qué importa {#why-it-matters}

Un desarrollador de un sistema de búsqueda o procesamiento documental puede enviar medios mixtos a un modelo local y recibir un esquema predecible. Eso reduce el trabajo de integración que normalmente exige combinar reconocimiento óptico de caracteres, reconocimiento de voz y comprensión de video.

Tencent ha publicado los pesos bajo su licencia propia `youtu-parsing`, un complemento vLLM, ejemplos de inferencia y un informe técnico. El repositorio dice que el código de evaluación llegará después, de modo que los resultados publicados no pueden reproducirse todavía solo con este lanzamiento.

El modelo usa un codificador común para imágenes, audio y video. Para video, determinadas capas permiten que cada fotograma atienda al audio de la misma parte del clip. Su esquema de salida abarca elementos literales, como texto y cuadros delimitadores, y salidas de mayor nivel, como narraciones e informes.

Tencent informa de una puntuación de 96,96 en OmniDocBench 1.6, ligeramente por encima de TeleOCR con 96,91 y PaddleOCR-VL-1.6 con 96,34 en su tabla. En el más amplio OmniParsingBench, Tencent informa de una media de 75,08, detrás de Gemini 3 Pro con 77,44, pero por delante de los otros sistemas de pesos abiertos probados. Son mediciones del publicador y la comparación depende de la configuración del informe.

El método de entrenamiento convierte repetidamente al modelo alumno en su propio profesor de la siguiente ronda. Los tokens de contenido y de estructura reciben señales de comparación distintas, un intento de preservar tanto lo que dice una página como las relaciones entre sus elementos.

## Lo que viene

Las ejecuciones independientes necesitarán el código de evaluación prometido. Los usuarios comerciales también deben revisar la licencia propia en vez de asumir los términos permisivos habituales en algunas publicaciones de pesos abiertos.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| Tencent publicó Youtu-Parsing-Omni con 5 mil millones de parámetros, pesos, ejemplos de código e informe técnico | VERIFICADO | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
| El modelo acepta documentos, imágenes, gráficos, geometría, audio y video y emite un esquema JSON único | SEGÚN LA EMPRESA | https://huggingface.co/tencent/Youtu-Parsing-Omni | ninguna |
| Tencent informa de 96,96 en OmniDocBench 1.6 y 75,08 en OmniParsingBench | SEGÚN LA EMPRESA | https://huggingface.co/tencent/Youtu-Parsing-Omni | ninguna |
| El lanzamiento utiliza la licencia propia youtu-parsing y todavía no incluye código de evaluación | VERIFICADO | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |

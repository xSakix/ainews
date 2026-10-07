+++
title = "bilibili amplía Index-Translate con versiones locales"
description = "La familia abierta de traducción incorpora paquetes GGUF, FP8 y NVFP4, una API compatible gratuita y cuatro pruebas comparativas públicas. Sus cifras de rendimiento siguen siendo las del propio desarrollador."
slug = "bilibili-amplia-index-translate-con-versiones-locales"
tags = ["models", "tools"]
date = 2026-10-05T04:01:30+02:00
draft = false
+++

bilibili añadió versiones cuantizadas oficiales, una interfaz pública gratuita y cuatro conjuntos de evaluación a Index-Translate los días 3 y 4 de octubre, convirtiendo sus modelos de traducción recién publicados en un paquete más práctico para uso local y alojado.

La familia traduce texto entre 150 idiomas y acepta instrucciones sobre terminología, formato y estilo. Sus modelos de texto habituales se ofrecen en tamaños de 2000 millones y 9000 millones de parámetros, además de una versión preliminar de 35 mil millones. El mayor es un modelo de mezcla de expertos que activa unos 3000 millones de parámetros por token.

El cambio importante para los usuarios locales es el empaquetado. Las versiones GGUF están dirigidas ahora a llama.cpp, mientras que las versiones FP8 están orientadas a vLLM y las NVFP4 a las GPU Blackwell más recientes. El proyecto publica esos formatos en las líneas de texto, control de sílabas y documentos largos. Sus modelos de voz también cuentan con paquetes cuantizados, aunque los repositorios GGUF solo contienen sus modelos de texto de base, no el proceso completo de voz.

El nuevo servicio alojado ofrece la versión preliminar 35B-A3B mediante una interfaz compatible con la API de chat de OpenAI. Esto permite a los desarrolladores probar el modelo sin tener que disponer primero del hardware adecuado. El repositorio identifica el servicio como gratuito, pero no promete un nivel de servicio ni precios a largo plazo.

Index-Translate es más que un traductor de frases. El cliente puede conservar la estructura de JSON y Markdown, aplicar un glosario y solicitar un tono concreto. Los paquetes relacionados traducen voz, buscan un número de sílabas solicitado para doblaje o mantienen el contexto a lo largo de un documento extenso. Estas funciones abordan las partes difíciles de la traducción en producción que un prompt genérico de «traduce esto» suele pasar por alto.

bilibili también publicó material de las pruebas comparativas instTrans, MEME, SandGlass y NativeLong con scripts de evaluación. Esto permite examinar el diseño de las pruebas, pero las puntuaciones publicadas siguen siendo mediciones del propio desarrollador. En el informe técnico, el modelo preliminar registra 0,8794 en FLORES COMET-22 y 76,76 con el juez de WMT26. Este último utiliza GPT-5.6-Sol como evaluador, por lo que no debe interpretarse como una comparación humana independiente.

La familia original de modelos llegó el 30 de septiembre; este no es el lanzamiento de un nuevo modelo fundacional. La noticia es que, en cuatro días, obtuvo los formatos de despliegue, el servicio de prueba y los recursos de evaluación necesarios para pasar de un anuncio de modelo a algo que los desarrolladores pueden probar.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| API pública y cuatro pruebas comparativas publicadas el 4 de octubre; versiones cuantizadas publicadas el 3 de octubre | VERIFICADO | [Repositorio del proyecto](https://github.com/bilibili/Index-Translate) | ninguna |
| Los modelos de texto abarcan 150 idiomas y admiten restricciones de terminología, formato y estilo | VERIFICADO | [Repositorio del proyecto](https://github.com/bilibili/Index-Translate) | [Ficha del modelo](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) |
| Paquetes GGUF, FP8 y NVFP4 y sus entornos de ejecución documentados | VERIFICADO | [Repositorio del proyecto](https://github.com/bilibili/Index-Translate) | enlaces a paquetes individuales enumerados en el repositorio |
| El modelo preliminar tiene 35 mil millones de parámetros totales y unos 3000 millones activos | VERIFICADO | [Ficha del modelo](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) | ninguna |
| FLORES COMET-22: 0,8794; juez de WMT26: 76,76 | SEGÚN LA EMPRESA | [Informe técnico](https://arxiv.org/abs/2609.40181) | ninguna; el informe utiliza GPT-5.6-Sol como juez para WMT26 |
| El nuevo empaquetado facilita probar la familia localmente o mediante un servicio alojado | ANÁLISIS | [Repositorio del proyecto](https://github.com/bilibili/Index-Translate) | inferencia a partir de los recursos publicados; no está establecida la continuidad del servicio |

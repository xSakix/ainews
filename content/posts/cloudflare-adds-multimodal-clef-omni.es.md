+++
title = "Cloudflare añade el modelo multimodal Clef-omni"
slug = "cloudflare-anade-modelo-multimodal-clef-omni"
description = "El nuevo clasificador conserva las entradas de imagen, audio y video de Qwen3-Omni y devuelve respuestas tipadas en vez de prosa generada. Cloudflare también redujo el precio y la ventana de contexto de Clef-flash."
tags = ["models", "tools"]
date = 2026-10-12T04:02:37+02:00
draft = false
+++

Cloudflare ha lanzado Clef-omni, un clasificador multimodal que acepta texto, imágenes, audio y video, pero devuelve respuestas tipadas en vez de prosa generada.

El modelo amplía la familia de clasificación Clef con Qwen3-Omni como base. Cloudflare congeló esa base, entrenó adaptadores ligeros y añadió una cabeza que transforma directamente una entrada en un esquema de etiquetas definido por el usuario en una sola pasada hacia delante.

## Por qué importa {#why-it-matters}

Para un desarrollador que clasifica mensajes de soporte, inspecciona fotos de productos o enruta clips breves, Clef-omni ofrece una única interfaz de clasificación para varios tipos de medios. Eso puede eliminar una etapa separada de transcripción o descripción de imágenes, aunque Cloudflare no ha publicado comparaciones independientes de extremo a extremo con esas cadenas de procesamiento.

Cloudflare afirma que Clef-omni es un modelo de mezcla de expertos de 30 mil millones de parámetros que activa unos 3000 millones para una entrada. En las mediciones de Workers AI de la empresa, clasificar texto llevó unos 130 milisegundos, imágenes unos 150 milisegundos y un video de 21 segundos con audio unos 1,5 segundos. Son tiempos de pruebas del proveedor y variarán con el tamaño de entrada, las colas y el despliegue.

El panorama de las pruebas es mixto, no uniformemente mejor. La tabla de Cloudflare sitúa por delante al anterior Clef denso en varias tareas de texto, mientras Clef-omni lo supera ligeramente en el conjunto de intenciones BANKING77, 94,8 % frente a 94,2 %. La diferencia práctica del nuevo modelo es la variedad de entradas, no una afirmación general de mayor precisión textual.

Cloudflare también cambió las condiciones de Clef-flash. Su precio de entrada anunciado cayó de 0,09 a 0,038 dólares por millón de tokens, mientras la ventana de contexto pasó de 64 000 a 24 000 tokens. Clef sigue en 0,24 dólares por millón de tokens de entrada y Clef-omni se lanza a 0,15 dólares.

Los pesos de Clef-omni están disponibles bajo Apache 2.0 en Hugging Face. La ficha del modelo enumera unos 35 300 millones de parámetros totales y afirma que el cargador personalizado actual necesita aproximadamente 64 GB de memoria BF16 en una GPU de clase H200. Cloudflare afirma que planea soporte para SGLang, pero no da fecha de lanzamiento.

## Lo que viene

Los pesos abiertos permiten ahora pruebas independientes de latencia, calibración y precisión. El soporte en un motor de inferencia habitual será importante para equipos que quieran ejecutar el modelo fuera de Workers AI sin mantener el cargador personalizado de Cloudflare.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| Cloudflare lanzó Clef-omni con entradas de texto, imagen, audio y video y salidas de clasificación tipadas | VERIFICADO | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | https://huggingface.co/Cloudflare/clef-omni |
| Cloudflare informa de unos 130 ms para texto, 150 ms para imágenes y 1,5 s para un clip audiovisual de 21 segundos | SEGÚN LA EMPRESA | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | ninguna |
| La tabla de Cloudflare informa de un 94,8 % en BANKING77 para Clef-omni y un 94,2 % para Clef | SEGÚN LA EMPRESA | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | ninguna |
| Clef-flash cuesta ahora 0,038 dólares por millón de tokens de entrada y tiene una ventana de contexto de 24 000 tokens | VERIFICADO | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | ninguna |
| Hay pesos Apache-2.0 y un cargador personalizado disponibles; se planea soporte para SGLang | VERIFICADO | https://huggingface.co/Cloudflare/clef-omni | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ |

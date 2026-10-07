+++
title = "Google lanza EmbeddingGemma 2 para búsquedas multimodales"
slug = "google-lanza-embeddinggemma-2-busquedas-multimodales"
description = "El modelo de embeddings de Google, con 740 millones de parámetros, sitúa texto, código, imágenes, vídeo y audio en un mismo espacio vectorial. Sus codificadores modulares están diseñados para dispositivos locales."
tags = ["models", "tools"]
date = 2026-10-07T04:01:57+02:00
draft = false
+++

Google ha lanzado EmbeddingGemma 2, un modelo de pesos abiertos con 740 millones de parámetros que sitúa texto, código, imágenes, fotogramas de vídeo y audio en un espacio compartido de *embeddings*.

Los pesos bajo Apache-2.0 llegaron el 6 de octubre con soporte en Transformers, sentence-transformers, llama.cpp, vLLM, Ollama, LM Studio, MLX y Transformers.js. El modelo está pensado para recuperar información y dirigir consultas, no para generar prosa: convierte distintos tipos de entrada en vectores cuya similitud puede compararse.

## Por qué importa {#why-it-matters}

Un desarrollador que construya una búsqueda privada en un teléfono o equipo portátil puede ahora indexar una nota de voz y recuperar un segmento de vídeo sin encadenar primero reconocimiento de voz, descripciones de imágenes y un modelo separado de embeddings de texto. Así se eliminan varios componentes de la recuperación local, aunque la utilidad real del modelo sigue dependiendo de los datos del usuario y del presupuesto de latencia.

EmbeddingGemma 2 es modular. Su base para texto y código tiene 270 millones de parámetros; la visión añade 170 millones y el audio, 300 millones. Todas las configuraciones proyectan a 768 dimensiones, y el entrenamiento Matryoshka permite truncar los vectores a 512, 256 o 128 dimensiones para reducir el almacenamiento.

Google afirma que los pesos cuantizados solo para texto usan unos 191 MB de RAM activa en un Pixel 11 Pro, frente a unos 567 MB del modelo completo. Su contexto de 8192 tokens puede contener hasta 5,5 minutos de audio, 29 imágenes o 58 fotogramas de vídeo con el esquema de empaquetado de Google.

La evaluación de la empresa sitúa MTEB Code en 78,68, frente a los 68,76 del primer EmbeddingGemma. Google también afirma ofrecer una calidad líder entre los modelos multimodales de embeddings de menos de mil millones de parámetros. Son mediciones del día del lanzamiento, no reproducciones independientes; la ficha del modelo es una base mejor para comparar una tarea concreta de recuperación.

El lanzamiento comparte con Gemma 4 un tokenizador y el diseño del codificador de audio, lo que puede reducir componentes duplicados cuando el modelo de embeddings alimenta un modelo generativo local. Google también ha publicado aplicaciones de ejemplo para buscar contenido multimedia y recuperar momentos de vídeo.

Las próximas pruebas prácticas vendrán de ensayos con colecciones privadas mixtas, donde la exhaustividad entre modalidades, el tiempo de indexación y la memoria importan más que una única prueba comparativa agregada.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| Google lanzó EmbeddingGemma 2 el 6 de octubre de 2026 | VERIFICADO | [Anuncio de Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | [pesos y ficha del modelo](https://huggingface.co/google/embeddinggemma-2) |
| El modelo tiene 740 millones de parámetros, con componentes modulares de 270 millones para texto, 170 millones para visión y 300 millones para audio | VERIFICADO | [Anuncio de Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | la ficha del modelo enumera la arquitectura |
| La RAM activa con cuantización es de unos 191 MB para texto y 567 MB para el modelo completo en Pixel 11 Pro | SEGÚN LA EMPRESA | [Anuncio de Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | ninguna |
| MTEB Code pasó de 68,76 a 78,68 | SEGÚN LA EMPRESA | [Anuncio de Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | ninguna |
| Hay pesos disponibles bajo Apache-2.0 | VERIFICADO | [repositorio del modelo](https://huggingface.co/google/embeddinggemma-2) | el repositorio es accesible |

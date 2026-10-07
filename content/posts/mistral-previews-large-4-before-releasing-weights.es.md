+++
title = "Mistral presenta Large 4 antes de publicar sus pesos"
slug = "mistral-presenta-large-4-antes-publicar-pesos"
description = "Mistral ha abierto el acceso por API a su modelo multimodal de un billón de parámetros y fijado el 27 de octubre para publicar los pesos abiertos. Las afirmaciones sobre arquitectura y pruebas comparativas siguen siendo provisionales."
tags = ["models", "business"]
date = 2026-10-07T04:00:57+02:00
draft = false
+++

Mistral ha abierto una versión preliminar pública de Mistral Large 4 por API y ha programado para el 27 de octubre la publicación de sus pesos descargables.

La empresa francesa describe el modelo como una mezcla multimodal de expertos entrenada desde cero en sus centros de datos europeos. Acepta texto e imágenes, admite más de 160 idiomas y tiene una ventana de contexto de un millón de tokens.

## Por qué importa {#why-it-matters}

Una organización que considere un modelo europeo alojado en su propia infraestructura puede probar Large 4 ahora, pero todavía no puede examinar ni desplegar los pesos prometidos. Esa diferencia convierte el lanzamiento en una versión preliminar con un compromiso de entrega fechado, no en una publicación completa de pesos abiertos.

El anuncio de Mistral enumera un billón de parámetros totales y 49 mil millones activos por token. Su documentación, en cambio, enumera 1,05 billones totales, 52 mil millones activos y un codificador visual de 1600 millones de parámetros. La diferencia podría reflejar redondeos o un cambio de configuración, pero Mistral no ha publicado un informe técnico que concilie las cifras.

La empresa destaca la ciberseguridad. Informa de un 82 % en la parte de reproducir y después corregir de CyberGym-E2E, un 93 % en Cybench y un 61,7 % en DeepSWE v1.1. Algunas evaluaciones nombran proveedores externos, pero la comparación conjunta y la mayoría de las afirmaciones principales aparecen en los materiales de lanzamiento de Mistral.

Antes de que lleguen los pesos, Mistral afirma que especialistas en ciberseguridad y autoridades públicas probarán una versión con menor moderación. La empresa sostiene que los rechazos habituales por seguridad pueden obstaculizar tareas defensivas, un equilibrio que esta versión preliminar busca explorar.

Los precios de la API parten de 1,36 dólares por millón de tokens de entrada y 4,18 dólares por millón de tokens de salida. Mistral Studio ofrece modos con y sin razonamiento, mientras que la licencia y los requisitos finales de despliegue seguirán siendo desconocidos hasta la publicación de los pesos.

La fecha decisiva es el 27 de octubre. Una ficha del modelo, un informe técnico, la licencia y los archivos descargables mostrarán si el artefacto público coincide con la escala y las capacidades de la versión preliminar.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| Mistral abrió una versión preliminar de Large 4 por API y programó los pesos para el 27 de octubre | VERIFICADO | [Anuncio de Mistral](https://mistral.ai/news/mistral-large-4/) | [Documentación de Mistral](https://docs.mistral.ai/models/mistral-large-4) |
| El anuncio enumera un billón de parámetros totales y 49 mil millones activos | VERIFICADO | [Anuncio de Mistral](https://mistral.ai/news/mistral-large-4/) | la documentación enumera cifras distintas |
| La documentación enumera 1,05 billones totales, 52 mil millones activos y un codificador visual de 1600 millones | VERIFICADO | [Documentación de Mistral](https://docs.mistral.ai/models/mistral-large-4) | ninguna |
| El modelo obtuvo un 82 % en reproducir y después corregir de CyberGym-E2E, un 93 % en Cybench y un 61,7 % en DeepSWE v1.1 | SEGÚN LA EMPRESA | [Anuncio de Mistral](https://mistral.ai/news/mistral-large-4/) | los evaluadores nombrados no verifican de forma independiente toda la comparación |
| La API cuesta 1,36 dólares de entrada y 4,18 dólares de salida por millón de tokens | VERIFICADO | [Documentación de Mistral](https://docs.mistral.ai/models/mistral-large-4) | documentación vigente |

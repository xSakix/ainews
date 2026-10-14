+++
title = "PolyStrata ejecuta grandes modelos MoE en GPU para juegos"
slug = "polystrata-ejecuta-grandes-modelos-moe-gpu-juegos"
description = "El entorno de código abierto conserva expertos seleccionados del modelo en la memoria del sistema y los mueve a una GPU de consumo cuando hace falta. Su paquete de un clic expone API locales compatibles con OpenAI y Anthropic."
tags = ["projects", "models", "hardware"]
date = 2026-10-12T03:57:37+02:00
draft = false
+++

PolyStrata ha lanzado un entorno de ejecución de código abierto que utiliza la memoria del sistema para servir modelos de mezcla de expertos demasiado grandes para caber íntegramente en una GPU para juegos.

El paquete de un clic envuelve el entorno Strata y se dirige a tarjetas Nvidia y AMD con al menos 12 GB de memoria de video. Incluye una configuración Qwen3.8-Flash-Next capaz de procesar imágenes y soporte experimental para varios modelos dispersos mayores, mientras expone endpoints compatibles con OpenAI y Anthropic en el equipo local.

## Por qué importa {#why-it-matters}

Para un desarrollador con una estación de trabajo y no un servidor, PolyStrata convierte la RAM libre del sistema en un conjunto de modelos más grande. Solo los expertos necesarios para el token actual pasan por la GPU, intercambiando movimiento de datos y capacidad de memoria por el coste del hardware multi-GPU.

Los modelos de mezcla de expertos contienen muchos bloques de parámetros especializados, pero activan solo un subconjunto en cada paso. PolyStrata conserva esos bloques en la memoria del equipo y programa los activos en el acelerador. La técnica no reduce el archivo del modelo: el README afirma que las versiones experimentales de GLM 5.3 Flash siguen necesitando aproximadamente entre 79 y 114 GB según la cuantización.

Las propias mediciones del proyecto en una RTX 5070 van de unos 94 tokens generados por segundo con su configuración más pequeña de dos bits a 53 con una mayor de tres bits. Informa de tasas de procesamiento de prompts de entre aproximadamente 1620 y 2650 tokens por segundo con un contexto de 32 000 tokens. Son pruebas del creador, no mediciones independientes, y la calidad varía entre niveles de cuantización.

PolyStrata también documenta cómo Claude Code dirige un modelo disperso Qwen3.6 35B con precisión de tres bits en una GPU de portátil de 8 GB. Una opción de inicio preparado lee el prompt del sistema antes de la sesión interactiva y reduce la demora hasta la primera respuesta. La utilidad real dependerá del ancho de banda de RAM, el enrutamiento del modelo y cuánto cambie el contexto entre turnos.

El repositorio tiene licencia MIT y ofrece endpoints locales compatibles con clientes de agentes existentes. Eso reduce el trabajo de integración y da a aplicaciones locales acceso a archivos y herramientas con los permisos propios del usuario. También significa que el operador, y no un proveedor alojado, se responsabiliza de las actualizaciones del modelo, la exposición a la red y la gestión de registros.

## Lo que viene

Las pruebas independientes deberían comparar modelos y ajustes de cuantización idénticos con entornos establecidos de descarga a CPU. El valor actual del proyecto es código inspeccionable y una capa práctica de empaquetado; sus velocidades destacadas siguen siendo cifras del autor hasta reproducirse en más hardware.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| PolyStrata lanzó un entorno local con licencia MIT para modelos dispersos en GPU de consumo | VERIFICADO | https://github.com/VecSzn/PolyStrata | ninguna |
| El paquete expone API locales compatibles con OpenAI y Anthropic | VERIFICADO | https://github.com/VecSzn/PolyStrata | ninguna |
| El README informa de 53–94 tokens generados por segundo en una RTX 5070 con cuantizaciones seleccionadas | SEGÚN LA EMPRESA | https://github.com/VecSzn/PolyStrata | ninguna |
| Los archivos experimentales de GLM 5.3 Flash necesitan aproximadamente 79–114 GB según la cuantización | VERIFICADO | https://github.com/VecSzn/PolyStrata | ninguna |
| Cargar expertos desde la memoria del equipo intercambia capacidad por costes de transferencia y ancho de banda de memoria | ANÁLISIS | https://github.com/VecSzn/PolyStrata | ninguna |

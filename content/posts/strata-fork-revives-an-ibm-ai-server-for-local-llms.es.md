+++
title = "Una versión de Strata revive un servidor IBM para LLM locales"
description = "Una versión derivada específica para este hardware ejecuta Qwen3.8-Flash-Next con dos procesadores POWER9 y cuatro GPU V100. Muestra lo que una optimización adaptada al modelo puede recuperar de un sistema de 2018."
slug = "version-de-strata-revive-servidor-ibm-para-llm-locales"
tags = ["projects", "hardware", "models"]
date = 2026-10-05T03:58:30+02:00
draft = false
+++

Un desarrollador de la comunidad ha adaptado el motor de inferencia Strata al AC922 de IBM, un servidor de 2018 cuyos dos procesadores POWER9 se conectan directamente a cuatro aceleradores Nvidia V100 de 16 GB. El resultado es más un caso práctico de cómo aprovechar la topología de una máquina inusual para un modelo moderno de mezcla de expertos que un sustituto general de llama.cpp.

La versión derivada ejecuta un Qwen3.8-Flash-Next cuantizado, un modelo de 125 mil millones de parámetros cuyo diseño disperso activa solo una pequeña parte de sus expertos por token. Strata mantiene los expertos utilizados con frecuencia en las GPU y el conjunto completo de expertos en la memoria del sistema. Esa disposición encaja con el AC922 porque sus CPU y GPU comparten conexiones NVLink 2.0 de gran ancho de banda, en lugar de comunicarse solo mediante PCIe convencional.

El desarrollador añadió una región de memoria bloqueada en páginas para cada zócalo de CPU, distribuyó los expertos teniendo en cuenta la disposición no uniforme de memoria de la máquina y permitió que una GPU vecina, que de otro modo permanecería inactiva, obtuviera datos a través de su propio NVLink. Otros cambios incluyen kernels FP16 para los núcleos tensoriales Volta, división de capas con ejecución en cadena y gestión de vectores e hilos específica para POWER9.

Con cuatro V100, las mediciones del proyecto alcanzan un máximo de 7357 tokens por segundo al leer un prompt de 135 000 tokens. Un prompt de 252 000 tokens se procesa a 7089 tokens por segundo y tarda 35,5 segundos. La generación voraz alcanza 113 tokens por segundo en JSON, 103 en código y 84 en prosa. Con un contexto reutilizado de 252 000 tokens, el primer token de la continuación aparece tras 0,26 segundos y la generación después avanza a 60 tokens por segundo.

Estas cifras son mediciones del creador en un servidor especializado, no una prueba comparativa trasladable a cualquier equipo. La velocidad de procesamiento del prompt varía considerablemente según su longitud, y el tipo de texto generado cambia la velocidad de decodificación. El repositorio describe la versión derivada como experimental y sin soporte del proyecto original Strata.

Aun así, el proyecto ilustra un enfoque cada vez más útil para la inferencia local: optimizar para un modelo concreto y una jerarquía de memoria concreta en lugar de exigir que un motor genérico trate todas las máquinas por igual. El AC922 es un equipo empresarial antiguo y de alto consumo, pero sus enlaces entre CPU y GPU siguen siendo especialmente capaces. Un modelo con miles de expertos da a esos enlaces un trabajo útil.

El código está publicado bajo la licencia MIT de Strata en la rama `ac922` de la versión derivada, con notas de compilación, calidad y pruebas comparativas. Algunos cambios podrían incorporarse al proyecto original más adelante, pero el valor inmediato es una ingeniería que puede examinarse para propietarios de hardware que los proyectos habituales de inferencia rara vez contemplan.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| La versión derivada está dirigida a un AC922 con dos CPU POWER9, cuatro GPU V100 de 16 GB y NVLink 2.0 | VERIFICADO | [Repositorio](https://github.com/eelgaev/Strata-AC922) | ninguna |
| Distribución de expertos consciente de NUMA, regiones bloqueadas en páginas por zócalo, obtención de datos por GPU vecinas y kernels para Volta/POWER9 | VERIFICADO | [Repositorio](https://github.com/eelgaev/Strata-AC922) | código y notas técnicas presentes; sin ejecución independiente |
| Máximo de procesamiento inicial de 7357 tokens/s y 7089 tokens/s con 252 000 tokens | SEGÚN LA COMUNIDAD | [Repositorio](https://github.com/eelgaev/Strata-AC922) | ninguna; prueba comparativa del creador |
| La decodificación alcanza 113 tokens/s en JSON y 84 en prosa | SEGÚN LA COMUNIDAD | [Repositorio](https://github.com/eelgaev/Strata-AC922) | ninguna; prueba comparativa del creador |
| La versión derivada es experimental y no cuenta con soporte del proyecto original | VERIFICADO | [Repositorio](https://github.com/eelgaev/Strata-AC922) | nota explícita del repositorio |
| La inferencia específica para un hardware puede recuperar valor de una topología de memoria especializada más antigua | ANÁLISIS | [Repositorio](https://github.com/eelgaev/Strata-AC922) | inferencia a partir de la implementación y las mediciones |

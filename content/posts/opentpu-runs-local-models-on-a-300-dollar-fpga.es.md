+++
title = "OpenTPU ejecuta modelos locales en una tarjeta FPGA de 300 dólares"
slug = "opentpu-modelos-locales-tarjeta-fpga-300-dolares"
description = "El proyecto con licencia Apache publica el diseño del acelerador, el compilador, el simulador y las herramientas del equipo anfitrión. El rendimiento medido muestra un sistema pequeño limitado por la memoria, no un sustituto de las GPU."
tags = ["hardware", "projects", "models"]
date = 2026-10-07T03:58:57+02:00
draft = false
+++

OpenTPU ha publicado una plataforma completa de aceleración de IA que ejecuta modelos de lenguaje modernos en una tarjeta FPGA Kintex-7 de unos 300 dólares.

El repositorio bajo Apache-2.0 incluye hardware en SystemVerilog, un conjunto de instrucciones, un simulador exacto bit a bit, un lenguaje de núcleos y su compilador, herramientas de perfilado y software anfitrión. Su valor es que permite inspeccionar todo: la misma base de código pequeña abarca desde los núcleos de modelos en Python hasta las señales de una placa PCIe física.

## Por qué importa {#why-it-matters}

Un desarrollador que estudie hardware de inferencia puede seguir cada ciclo y transferencia de memoria sin necesitar un acelerador de centro de datos. La máquina resultante es lenta frente a las GPU actuales, pero sus límites hacen especialmente visible el cuello de botella.

OpenTPU informa de 30,7 tokens generados por segundo para un modelo Qwen3-0.6B de cuatro bits y de 82,1 para LFM2.5-230M, incluida la sobrecarga del equipo anfitrión. Los modelos densos mayores bajan a 12,03 tokens por segundo para Qwen3.5-2B y 3,75 para Gemma 4 E4B en las configuraciones enumeradas.

Durante la decodificación, la tarjeta alcanza entre el 82 % y el 94 % del máximo de 17,1 GB/s de sus dos canales DDR3. Eso convierte el ancho de banda de memoria, y no la aritmética matricial, en el recurso limitante. Una unidad sistólica de cuatro columnas ayuda más al procesamiento de prompts que a la generación token a token.

Los modelos mayores que los 4 GiB de la tarjeta pueden transmitir pesos de mezclas de expertos desde el almacenamiento anfitrión. El repositorio informa de 10,6 tokens por segundo para LFM2.5-8B-A1B y de 3,95 para Qwen3.5-35B-A3B; este último mueve 153 MB por token a través de PCIe. Son mediciones del proyecto, pero los scripts, las compilaciones fechadas y las condiciones de medición son públicos.

La descripción «desarrollado por IA» requiere cuidado. Según el proyecto, un proceso de agentes dirigido por humanos produjo buena parte del diseño y la optimización, pero eso no demuestra que un sistema autónomo decidiera crear su propio hardware. El resultado concreto es la plataforma publicada y la coincidencia bit a bit que se comunica entre la placa y el simulador.

Las próximas pruebas son claras: reproducir las configuraciones binarias publicadas en la misma placa, comparar consumo y latencia con GPU económicas y comprobar si colaboradores externos pueden cambiar la arquitectura sin romper la equivalencia con el simulador.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| OpenTPU publica hardware, ISA, simulador, compilador y herramientas anfitrionas bajo Apache-2.0 | VERIFICADO | [Repositorio de OpenTPU](https://github.com/FeSens/openTPU) | los archivos y la licencia son accesibles |
| Qwen3-0.6B alcanza 30,7 tokens/s de tiempo real y LFM2.5-230M alcanza 82,1 en configuraciones de cuatro bits | SEGÚN LA EMPRESA | [Mediciones de OpenTPU](https://github.com/FeSens/openTPU) | ninguna |
| La decodificación utiliza entre el 82 % y el 94 % de un máximo DDR3 de 17,1 GB/s | SEGÚN LA EMPRESA | [Mediciones de OpenTPU](https://github.com/FeSens/openTPU) | ninguna |
| Qwen3.5-35B-A3B alcanza 3,95 tokens/s mientras transmite 153 MB por token | SEGÚN LA EMPRESA | [Mediciones de OpenTPU](https://github.com/FeSens/openTPU) | ninguna |
| La tarjeta reproduce los tokens del simulador bit a bit | SEGÚN LA EMPRESA | [Repositorio de OpenTPU](https://github.com/FeSens/openTPU) | hay pruebas públicas; no se encontró una reproducción independiente en hardware |
| «Desarrollado por IA» no demuestra desarrollo autónomo de hardware | ANÁLISIS | [Repositorio de OpenTPU](https://github.com/FeSens/openTPU) | la distinción se desprende del proceso documentado dirigido por humanos |

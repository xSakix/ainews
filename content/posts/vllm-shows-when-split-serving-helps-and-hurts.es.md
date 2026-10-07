+++
title = "vLLM muestra cuándo separar la inferencia ayuda y perjudica"
description = "Una guía práctica mide el equilibrio entre ventajas y costes de separar el procesamiento del prompt de la generación de tokens. La latencia de cola mejora bajo carga, pero trasladar la memoria de trabajo del modelo retrasa el primer token."
slug = "vllm-muestra-cuando-separar-inferencia-ayuda-y-perjudica"
tags = ["essays", "tools", "hardware"]
date = 2026-10-06T04:04:31+02:00
draft = false
+++

Separar el procesamiento del prompt de la generación de tokens puede estabilizar un servidor de modelos bajo carga, pero transferir su memoria de trabajo puede hacer más lenta la primera respuesta, según el equipo de vLLM.

El proyecto de inferencia de código abierto probó la «inferencia desagregada», en la que una GPU se encarga del procesamiento inicial, o *prefill*, y otra de la generación, o *decode*. El procesamiento inicial lee el prompt y construye la caché de claves y valores; la generación utiliza esa caché para producir tokens. La guía también traslada la tokenización y el análisis de las salidas a una interfaz sin GPU.

Para un operador que atiende prompts largos, el diseño ofrece una elección entre dos tipos de demora. Separar las fases evita que un prompt grande interrumpa la generación para otros usuarios, pero la caché debe trasladarse entre los procesos de trabajo antes de que empiece la generación.

En la prueba de vLLM con dos GPU, Qwen2.5-7B y prompts de 8000 tokens, el intervalo entre tokens generados en el percentil 99 pasó de 23 milisegundos a 169 milisegundos en la configuración conjunta con 0,4 solicitudes por segundo. La configuración separada mantuvo ese intervalo entre 25 y 52 milisegundos.

El mismo experimento puso de manifiesto el coste. Trasladar unos 470 MB de caché por prompt tardó aproximadamente 1,3 segundos, y la mediana del tiempo hasta el primer token fue de 2,2 segundos, frente a los 0,7 segundos cuando ambas fases compartían un proceso de trabajo. Las GPU L40S no contaban con NVLink ni con transferencia directa entre dispositivos, por lo que el resultado describe una vía de transporte deliberadamente desfavorable, no todos los despliegues.

La regla de decisión de los autores es práctica: comprobar primero la topología de las GPU y después examinar las métricas de transferencia de caché con la longitud de prompt y la tasa de solicitudes previstas. La desagregación resulta más atractiva cuando el procesamiento inicial interrumpe repetidamente la generación o cuando las dos fases requieren un escalado distinto. Un servidor con poca carga puede pagar el coste de transferencia sin obtener un aislamiento útil.

La guía cita resultados de mayor escala de AMD y del proyecto llm-d, pero esas pruebas utilizan modelos, aceleradores y tamaños de clúster distintos. Respaldan el potencial de la arquitectura, no una cifra de aceleración trasladable a cualquier entorno.

Las instrucciones están dirigidas a vLLM 0.30.0 o posterior e incluyen servicios separados de renderizado y procesamiento inverso. El equipo señala que siguen existiendo carencias de integración, por lo que las comprobaciones de topología y transferencia son un requisito previo, no una optimización posterior al despliegue.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| vLLM documenta servicios separados de procesamiento inicial, generación e interfaz sin GPU | VERIFICADO | [Guía de vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | configuración y comandos públicos de vLLM |
| Con 0,4 solicitudes/s, el intervalo entre tokens en p99 de la configuración conjunta alcanzó 169 ms, mientras que la inferencia separada se mantuvo entre 25 y 52 ms | SEGÚN LA EMPRESA | [Guía de vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | ninguna; prueba realizada por el proyecto |
| Un prompt de 8000 tokens produjo unos 470 MB de caché y una transferencia de aproximadamente 1,3 s | SEGÚN LA EMPRESA | [Guía de vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | ninguna |
| La mediana del tiempo hasta el primer token fue de 2,2 s con las fases separadas y de 0,7 s con ambas juntas | SEGÚN LA EMPRESA | [Guía de vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | ninguna |
| La prueba utilizó dos GPU L40S sin NVLink ni transferencia directa entre dispositivos | VERIFICADO | [Guía de vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | configuración de prueba indicada por los autores |
| La guía está dirigida a vLLM 0.30.0 o posterior | VERIFICADO | [Guía de vLLM](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | requisito de versión en la guía |

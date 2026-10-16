+++
title = "H2O.ai publica H2O-Lightning-31B"
slug = "h2oai-publica-h2o-lightning-31b"
description = "El modelo de decisión de pesos abiertos responde preguntas acotadas en una sola pasada y devuelve probabilidades. Sus cifras más destacadas de velocidad y precisión proceden de las propias pruebas de H2O.ai."
tags = ["models", "tools"]
date = 2026-10-11T04:06:06+02:00
draft = false
+++

H2O.ai ha publicado H2O-Lightning-31B, un modelo de pesos abiertos construido para responder preguntas de decisión acotadas con probabilidades, en lugar de generar prosa libre.

El modelo se basa en Gemma 4 31B-it y acepta texto y hasta cuatro imágenes. Su interfaz abarca elecciones, preguntas de sí o no y puntuaciones ordenadas, y devuelve un resultado en una sola pasada hacia delante. H2O.ai publicó los pesos, la ficha del modelo y el código para servirlo en Hugging Face.

## Por qué importa {#why-it-matters}

Para un desarrollador que utiliza un gran chatbot para distribuir solicitudes, puntuar registros o seleccionar una herramienta, la salida restringida puede eliminar varios pasos frágiles: pedir JSON, analizarlo, rechazar respuestas mal formadas y volver a preguntar. Una probabilidad también revela lo ajustada que fue la elección, aunque solo resulta útil cuando el modelo está calibrado para los datos previstos.

H2O.ai informa de que el modelo de 31 mil millones de parámetros respondió correctamente 212 de las 231 preguntas públicas de JevBench. En su evaluación de imágenes, el modelo con ajuste fino obtuvo un 88,4 % sobre 1877 preguntas, frente al 88,0 % de la base Gemma congelada. El intervalo de incertidumbre de la ficha incluye la ausencia de mejora, de modo que ese resultado de imágenes no establece una ganancia fiable sobre el modelo base.

La empresa también informa de una latencia mediana de unos 25 milisegundos al cargar el modelo en FP8 en una NVIDIA H100. La cifra procede de su propia configuración, con la caché de prefijos desactivada, y la ficha no ofrece mediciones para GPU menores. Los archivos bfloat16 publicados suman unos 63 GB antes de la sobrecarga de ejecución.

La versión funciona sobre vLLM 0.30.0 sin modificar, detrás de la capa de adaptación `/v1/systemone` de H2O.ai. Los registros largos no se procesan completos: una etapa de recuperación los recorta a 3000 tokens antes de la inferencia. Ese límite importa porque una decisión solo puede reflejar la evidencia que conserva la recuperación.

Los pesos llevan Apache 2.0 junto con los términos de Gemma de Google. El aviso de H2O.ai señala específicamente las restricciones de uso de Gemma sobre decisiones automatizadas que afectan a derechos individuales, de modo que la apertura de los archivos no permite cualquier despliegue.

H2O.ai también actualizó su modelo hermano anterior de 4 mil millones de parámetros con mediciones de latencia revisadas y un paquete GGUF para llama.cpp. La versión de 31 mil millones está disponible en la página del modelo de Hugging Face; todavía no se han publicado pruebas independientes de latencia, calibración y calidad de las tareas.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| H2O.ai publicó H2O-Lightning-31B con pesos, ficha de modelo y código para servirlo | VERIFICADO | https://huggingface.co/h2oai/h2o-lightning-31b | ninguna |
| El modelo admite decisiones acotadas con texto e imágenes y devuelve probabilidades en una pasada hacia delante | VERIFICADO | https://huggingface.co/h2oai/h2o-lightning-31b | ninguna |
| Obtuvo 212 aciertos de 231 preguntas de JevBench y una latencia mediana de unos 25 ms en una H100 | SEGÚN LA EMPRESA | https://huggingface.co/h2oai/h2o-lightning-31b | ninguna |
| Su evaluación de imágenes no mostró una mejora estadísticamente fiable sobre la base Gemma congelada | VERIFICADO | https://huggingface.co/h2oai/h2o-lightning-31b | ninguna |
| Los términos de Gemma restringen las decisiones automatizadas que afectan a derechos individuales | VERIFICADO | https://huggingface.co/h2oai/h2o-lightning-31b | ninguna |

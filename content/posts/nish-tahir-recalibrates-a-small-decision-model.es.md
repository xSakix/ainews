+++
title = "Nish Tahir recalibra un pequeño modelo de decisión"
slug = "nish-tahir-recalibra-un-pequeno-modelo-de-decision"
description = "Un experimento ejecutable convierte Qwen3-1.7B en un clasificador de una sola pasada y muestra después que su confianza es demasiado alta. El escalado de temperatura mejora las probabilidades."
tags = ["models", "research", "essays"]
date = 2026-10-11T04:01:06+02:00
draft = false
+++

El ingeniero independiente Nish Tahir ha publicado un experimento ejecutable que convierte Qwen3-1.7B en un modelo de decisión de una sola pasada y después mide lo mal que su confianza coincide con su precisión.

El método limita el vocabulario de salida a los tokens de respuesta de A a E y lee sus probabilidades tras una pasada hacia delante. En CommonsenseQA, Tahir informa de un 59,4 % de precisión para el modelo base y un 62,4 % tras un breve ajuste fino.

## Por qué importa {#why-it-matters}

Un desarrollador que construye un enrutador o una puntuación de riesgo necesita saber algo más que qué opción ganó. Si un modelo dice 95 %, pero solo acierta siete de cada diez veces, los umbrales basados en esa cifra se comportarán de forma impredecible. El experimento de Tahir muestra el camino completo desde los logits hasta un problema medido de calibración, con un modelo lo bastante pequeño para reproducirlo.

La mejora de precisión no es el resultado más informativo. Las respuestas con una confianza asignada entre el 90 % y el 100 % solo acertaban alrededor del 70 % de las veces. En la franja del 80 % al 90 %, la precisión rondaba el 40 %. El modelo distinguía las opciones lo suficiente para superar al azar, pero expresaba mucha más certeza de la que justificaban sus resultados.

Tahir aplica escalado de temperatura para corregir las probabilidades. El método aprende un escalar con ejemplos reservados y divide los logits por él antes de la operación softmax. Aumentar la temperatura aplana una distribución excesivamente confiada sin cambiar qué respuesta tiene la puntuación más alta.

Eso hace del escalado de temperatura un paso de calibración, no una mejora de capacidades. No puede corregir clasificaciones erróneas ni enseñar conocimiento ausente. Su valor es que un 70 % declarado puede aproximarse más a siete aciertos de diez en datos parecidos al conjunto de calibración.

El texto incluye una implementación compacta de PyTorch y demostraciones interactivas. También muestra una elección de diseño oculta en muchos productos de modelos de decisión: el esquema de respuesta debe conocerse de antemano y asignarse limpiamente a un pequeño conjunto de tokens. Una tarea con etiquetas ambiguas, opciones ausentes o varias respuestas válidas rompe esa simplicidad.

Los resultados proceden de un modelo pequeño, una prueba comparativa y la configuración de entrenamiento del autor. Las preguntas de opción múltiple de CommonsenseQA no reproducen la distribución de documentos, la revisión de fraude ni la selección de herramientas, y la calibración puede desviarse si cambia la distribución de entrada. Cada despliegue necesitaría sus propios datos reservados y comprobaciones periódicas.

El artículo resulta útil precisamente porque informa de esa debilidad en vez de presentar la confianza como fiable por construcción. El código y las demostraciones ya están disponibles y dan a los profesionales una referencia breve para probar modelos de decisión especializados mayores.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| El experimento restringe Qwen3-1.7B a tokens de respuesta de A a E y lee una pasada hacia delante | VERIFICADO | https://nishtahir.com/build-your-own-decision-model/ | ninguna |
| El modelo base obtuvo un 59,4 % y el modelo con ajuste fino breve un 62,4 % en CommonsenseQA | SEGÚN LA EMPRESA | https://nishtahir.com/build-your-own-decision-model/ | ninguna |
| La franja de confianza del 90 % al 100 % acertaba aproximadamente el 70 % de las veces | SEGÚN LA EMPRESA | https://nishtahir.com/build-your-own-decision-model/ | ninguna |
| La franja de confianza del 80 % al 90 % acertaba aproximadamente el 40 % de las veces | SEGÚN LA EMPRESA | https://nishtahir.com/build-your-own-decision-model/ | ninguna |
| El escalado de temperatura cambia la concentración de probabilidades sin cambiar la respuesta mejor clasificada | VERIFICADO | https://nishtahir.com/build-your-own-decision-model/ | ninguna |

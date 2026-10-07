+++
title = "Los modelos visuales separan objetos y relaciones abstractas"
slug = "modelos-visuales-separan-objetos-relaciones-abstractas"
description = "Una prepublicación identifica en modelos de visión y lenguaje un circuito temprano de comparación de objetos y otro posterior de comparación de relaciones. Después vincula este último al rendimiento en ARC-AGI-1."
tags = ["research", "models"]
date = 2026-10-07T03:59:57+02:00
draft = false
+++

Los modelos de visión y lenguaje podrían resolver comparaciones visuales abstractas mediante dos procesos internos que compiten: uno temprano que sigue los objetos visibles y otro posterior que representa las relaciones entre ellos.

Ese es el hallazgo central de una prepublicación de Minegishi, Furuta, Kojima y sus colegas. El equipo adaptó una tarea Relational Match-to-Sample de la psicología del desarrollo y comparada, y después probó tanto sistemas cerrados de vanguardia como modelos abiertos con imágenes controladas.

## Por qué importa {#why-it-matters}

Para un investigador que evalúa el razonamiento visual, una respuesta correcta por sí sola no revela si el modelo identificó la regla subyacente o simplemente reconoció formas similares. El estudio ofrece una manera de separar esas vías y después intervenir en la asociada a relaciones abstractas.

Cada tarea presenta un par de objetos de muestra y pregunta qué par candidato tiene la misma relación. Un candidato puede conservar la relación y cambiar los objetos; otro puede conservar la apariencia superficial y cambiar la relación. El conflicto revela si el modelo sigue la identidad o la estructura.

En las familias GPT, Claude, Gemini, Qwen3.5, Gemma 4 e InternVL3, cuatro cambios desplazaron las respuestas hacia las relaciones: una categoría de modelo más capaz, un modelo más grande, menos objetos en la escena y menos ruido en cada objeto. Los autores comparan esta progresión con el «cambio relacional» observado en el desarrollo humano, pero la semejanza es conductual y no prueba un mecanismo cognitivo compartido.

El análisis interno encontró las dos señales a distintas profundidades. Las representaciones de las primeras capas agrupaban los ejemplos por características de los objetos, mientras que las capas posteriores los agrupaban por la relación abstracta. Las pruebas de mediación causal identificaron después cabezas de atención cuya actividad contribuía a respuestas basadas en relaciones.

## Una intervención conecta el circuito con otra tarea

El resultado más sólido procede de desactivar las cabezas asociadas a la comparación relacional. Los autores informan de que esto perjudica el rendimiento en ARC-AGI-1 más que desactivar cabezas elegidas al azar. Esa transferencia importa porque las cabezas se encontraron en la tarea psicológica de comparación, en lugar de elegirse directamente para explicar los resultados de ARC.

La evidencia sigue teniendo un alcance limitado. Un conjunto de cabezas puede contribuir a dos tareas sin constituir un módulo de razonamiento de propósito general. Los estímulos son deliberadamente simples, y el artículo no establece que la misma competencia controle el reconocimiento en fotografías, gráficos o conversaciones multimodales largas.

El estudio también depende de dos niveles distintos de acceso. Los resultados conductuales pueden incluir modelos propietarios por API, pero examinar las representaciones capa por capa y realizar ablaciones requiere pesos abiertos. La afirmación sobre el mecanismo se apoya, por tanto, en los modelos abiertos examinados internamente, mientras que la comparación más amplia entre familias es conductual.

El diseño paramétrico facilita la reproducción. La cantidad de objetos y el ruido visual pueden cambiarse por separado, lo que permite a otro equipo comprobar si la separación entre capas persiste con nuevas formas, relaciones y familias de modelos. La página del resumen no enumera un repositorio público de código, por lo que reproducir la intervención completa exigirá más que descargar una prueba comparativa.

El artículo se envió a arXiv el 6 de octubre de 2026 y no ha pasado revisión por pares. Su aportación útil es un vínculo refutable entre una tarea cognitiva clásica y los circuitos internos del modelo: el comportamiento que sigue relaciones debería debilitarse al perturbar la vía tardía identificada, mientras que la comparación de objetos debería mantenerse relativamente intacta.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| El estudio prueba la comparación relacional en modelos de visión y lenguaje abiertos y de vanguardia por API | SEGÚN LA EMPRESA | [prepublicación](https://arxiv.org/abs/2610.07646) | ninguna; evaluación de los autores |
| Escala, capacidad, menos objetos y menos ruido desplazan los modelos hacia la comparación de relaciones | SEGÚN LA EMPRESA | [prepublicación](https://arxiv.org/abs/2610.07646) | ninguna |
| Las primeras capas codifican similitud entre objetos y las posteriores relaciones abstractas | SEGÚN LA EMPRESA | [prepublicación](https://arxiv.org/abs/2610.07646) | ninguna |
| La ablación de cabezas asociadas a relaciones perjudica ARC-AGI-1 más que la ablación de cabezas al azar | SEGÚN LA EMPRESA | [prepublicación](https://arxiv.org/abs/2610.07646) | ninguna |
| La semejanza conductual no prueba un mecanismo humano compartido | ANÁLISIS | [prepublicación](https://arxiv.org/abs/2610.07646) | inferencia a partir del diseño del estudio |
| La prepublicación se envió el 6 de octubre de 2026 | VERIFICADO | [Registro de arXiv](https://arxiv.org/abs/2610.07646) | metadatos de arXiv |

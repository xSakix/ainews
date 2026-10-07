+++
title = "Las sondas de mentiras rastrean obediencia en vez de verdad"
description = "Un preprint prueba ocho sondas publicadas con modelos de lenguaje que interpretan personajes que rechazan hechos básicos. Muchas fallan cuando las respuestas verdaderas y falsas comparten el mismo prompt, mientras una sonda entrenada para separar verdad y obediencia resiste."
slug = "sondas-de-mentiras-rastrean-obediencia-en-vez-de-verdad"
tags = ["research", "safety"]
date = 2026-10-06T04:01:31+02:00
draft = false
+++

Muchas sondas publicadas de detección de mentiras, que leen la actividad interna de un modelo de lenguaje para señalar respuestas falsas, detectan en parte si el modelo siguió sus instrucciones, según un nuevo preprint.

Maximilian von Klinski y tres coautores hicieron que tres modelos abiertos interpretaran personajes que rechazan hechos básicos, como un astrónomo ptolemaico o un teórico de la conspiración, y probaron si ocho sondas existentes seguían detectando las respuestas falsas. Muchas lo hacían, hasta que las respuestas verdaderas y falsas se colocaron bajo el mismo prompt de personaje. Entonces varias obtuvieron resultados peores que lanzar una moneda.

## Por qué importa {#why-it-matters}

Un equipo de seguridad que supervisa un modelo desplegado con una sonda necesita que la alarma se active ante la falsedad, no ante algo que suele acompañarla. En los datos con los que se entrenan la mayoría de las sondas, la respuesta falsa también es la menos probable y la que incumple las reglas del modelo, y el estudio observa que las sondas aprenden esos atajos.

## Cómo lee una sonda un modelo

Una sonda es un clasificador sencillo entrenado con los números del interior de una capa de un modelo, etiquetados según si el texto procesado era verdadero o falso. Si funciona, lee lo que el modelo considera verdadero incluso cuando las palabras que produce dicen lo contrario.

El equipo construyó un conjunto de datos de 8916 respuestas de Llama 3.3 70B de Meta y Gemma 3 27B y Gemma 4 31B de Google. Cada uno respondió a preguntas de sí o no tanto como un asistente corriente como interpretando a uno de 15 personajes: personas con creencias del mundo real, figuras ficticias como un ciudadano de *1984* de Orwell y personajes históricos como un médico medieval. Las preguntas se refinaron mediante un proceso basado en Claude Opus 4.8 de Anthropic, se filtraron con Llama como juez y fueron revisadas manualmente por el primer autor.

## Compartir el prompt hace fallar a la mayoría de las sondas

En la primera versión de la prueba, la mayoría de las sondas anteriores separó bien las respuestas verdaderas de las falsas, ordenándolas correctamente en aproximadamente nueve de cada diez pares. Pero todas las respuestas falsas venían con un prompt de personaje y todas las verdaderas con el del asistente, por lo que el prompt por sí solo revelaba la respuesta.

Los autores eliminaron esa pista colocando ambas respuestas después del prompt del personaje. Ahora la respuesta verdadera también era la menos probable y la que contradecía las instrucciones del personaje. En Llama, varias sondas que habían funcionado cayeron por debajo del azar, y solo dos se mantuvieron cerca de sus puntuaciones anteriores. Los fallos se repitieron, a menudo con mayor intensidad, en los dos modelos Gemma.

## Tres trampas aíslan el atajo

Para averiguar qué rastreaban las sondas, el equipo construyó tres conjuntos de prueba en los que la verdad va en dirección contraria a un posible factor de confusión. En uno, una regla de puntuación hacía que la respuesta incorrecta fuera la más probable. En otro, un personaje mantenía en privado una creencia falsa, como que siete por seis es 13. En el tercero, la respuesta correcta incumplía una regla de formato, por ejemplo al utilizar paréntesis cuando se exigían corchetes, mientras que la incorrecta la obedecía.

La trampa de formato fue decisiva. En Llama, todas las sondas anteriores quedaron por debajo del azar excepto una cuyas lecturas estaban invertidas en todas las pruebas, algo que los autores interpretan como un fuerte vínculo entre «verdadero» y «obediente» dentro de esas sondas.

La sonda del propio equipo añade un ingrediente al entrenamiento estándar con hechos simples: preguntas cuyas instrucciones exigen la respuesta incorrecta, de modo que la obediencia y la verdad apunten en direcciones opuestas. Obtuvo aproximadamente 0,98 sobre 1 en la prueba de prompt compartido con Llama, nunca cayó por debajo de 0,90 en ninguno de los tres modelos y fue perfecta en las tres trampas.

## Una solución propia y factores de confusión aún desconocidos

Ese resultado requiere dos matices. La nueva sonda se diseñó contra los mismos factores de confusión con los que después se probó, lo que, según reconocen los autores, hace poco sorprendentes sus puntuaciones perfectas en las trampas. Su diseño también amplía una sonda anterior desarrollada conjuntamente por el coautor Lennart Bürger, una de las dos únicas sondas previas que resistieron al compartir el prompt.

Los propios datos del estudio muestran que la lista de factores de confusión es incompleta. En Gemma 4, una sonda anterior fue casi perfecta en las tres trampas, pero obtuvo aproximadamente 0,17 en la prueba de prompt compartido, fallando por una razón que ninguna de las trampas captaba. Los personajes también se configuraron con un único prompt de sistema en conversaciones de un turno, en modelos de hasta 70 mil millones de parámetros.

El trabajo fue financiado por el Ministerio Federal de Investigación, Tecnología y Espacio de Alemania, el programa Horizonte Europa de la Unión Europea y la Fundación Alemana de Investigación. Los autores han publicado el conjunto de datos en Hugging Face y su código en GitHub, y señalan los personajes que surgen gradualmente en conversaciones largas como el próximo caso que debe probarse.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| Se evaluaron ocho sondas anteriores; muchas fallan cuando las respuestas verdaderas y falsas comparten el prompt del personaje | SEGÚN LA EMPRESA | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna; resultado de un preprint |
| Conjunto de datos de 8916 respuestas revisadas por humanos de Llama 3.3 70B, Gemma 3 27B y Gemma 4 31B con 15 personajes | VERIFICADO | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | [conjunto de datos en Hugging Face](https://huggingface.co/datasets/maxvonk/anti-factual-personas) |
| Preguntas refinadas con un proceso de Claude Opus 4.8, evaluadas por Llama 3.3 70B y revisadas por el primer autor | VERIFICADO | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna; descripción del método de los autores |
| La mayoría de las sondas anteriores obtiene un AUROC de entre 0,86 y 0,94 cuando el prompt difiere entre respuestas verdaderas y falsas | SEGÚN LA EMPRESA | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna |
| Con un prompt compartido en Llama, varias sondas anteriores caen por debajo del azar; solo Marks/Bürger Lie (0,885) y Cundy DolusChat (0,901) se mantienen estables | SEGÚN LA EMPRESA | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna |
| Los fallos con prompt compartido se repiten, a menudo con mayor intensidad, en Gemma 3 27B y Gemma 4 31B | SEGÚN LA EMPRESA | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna |
| En la trampa de obediencia con Llama, todas las sondas anteriores quedan por debajo del azar salvo Goldowsky-Dill SD, que está invertida en todo momento | SEGÚN LA EMPRESA | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna |
| Las sondas vinculan la verdad con el cumplimiento de instrucciones | ANÁLISIS | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | inferencia de los autores a partir de la trampa de obediencia |
| Nueva sonda: AUROC de 0,976 en la prueba de prompt compartido con Llama, nunca inferior a 0,900 en tres modelos y perfecta en las tres trampas | SEGÚN LA EMPRESA | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna |
| La nueva sonda se entrenó para eliminar los mismos factores de confusión con los que se prueba; los autores consideran poco sorprendentes los resultados de las trampas | VERIFICADO | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna |
| El coautor Lennart Bürger desarrolló conjuntamente la sonda Marks/Bürger que amplía la nueva sonda | VERIFICADO | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | cita a Bürger y colaboradores (2024) |
| En Gemma 4, Cooney DYL es casi perfecta en todas las trampas, pero obtiene 0,171 con un prompt compartido | SEGÚN LA EMPRESA | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | ninguna |
| Financiado por el BMFTR de Alemania, Horizonte Europa de la UE y la Fundación Alemana de Investigación (DFG) | VERIFICADO | [Preprint de von Klinski y colaboradores](https://arxiv.org/abs/2609.39807) | sección de agradecimientos |
| El código es público en GitHub | VERIFICADO | [Repositorio de GitHub](https://github.com/max-vkl/stress-testing-llm-lie-detectors) | la página del repositorio carga |
| Preprint publicado el 30 de septiembre de 2026 | VERIFICADO | [Registro de arXiv](https://arxiv.org/abs/2609.39807) | metadatos de arXiv |

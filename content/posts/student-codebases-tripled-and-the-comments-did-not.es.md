+++
title = "El código de los estudiantes se triplicó; los comentarios, no"
slug = "codigo-estudiantes-triplico-comentarios-no"
description = "Un estudio de diez semestres y 260 repositorios de equipos de proyectos finales halló que el código al terminar el semestre pasó de unas 3400 a unas 10 000 líneas cuando la IA generativa ya estaba ampliamente disponible, mientras la densidad de comentarios no cambió. Los autores nunca observaron el uso de IA, por lo que el resultado es una advertencia para evaluadores y empleadores, no un veredicto sobre las herramientas."
tags = ["research", "tools"]
date = 2026-11-09T03:16:01+01:00
draft = false
+++

Una coordinadora de curso trabaja el viernes anterior a la entrega de notas. Tiene una hoja de cálculo con algo más de cuarenta equipos de estudiantes y una costumbre de años: abrir el repositorio, mirar cuánto se construyó y con qué regularidad, y usarlo para hacerse una idea de quién trabajó. Este año, el primer repositorio de su lista contiene diez mil líneas de código y trescientos commits. Recorre una función con ramas muy anidadas y no encuentra ningún comentario que las explique. La coordinadora es inventada y representa un problema que tres investigadores acaban de medir.

El estudio, *Code, Commits, and Complexity in the GenAI Era*, se publicó en arXiv el 5 de noviembre y fue aceptado para el SIGCSE Technical Symposium de febrero de 2027. Sus autores son Asma Shakil y Paul Denny, de la University of Auckland, y Claus Brabrand, de la IT University of Copenhagen. Analizaron 260 repositorios de equipos de un curso obligatorio de proyecto final, distribuidos entre diez semestres de 2021 a 2025. El código al final del semestre pasó de una mediana de unas 3400 líneas entre 2021 y 2023 a unas 10 000 en 2024 y 2025. Los autores no observaron a nadie utilizar IA y lo repiten expresamente.

## Un curso, diez semestres

En el curso, equipos de cinco o seis estudiantes construyen software para clientes externos reales durante trece semanas. El prototipo funcional es el principal elemento evaluado. Los repositorios proceden de la organización de GitHub del curso: 302 inicialmente, 260 después de eliminar los vacíos, las plantillas y los duplicados. Las cohortes contienen 19, 65, 57, 51 y 68 repositorios de 2021 a 2025, respectivamente.

Los autores miden cada repositorio dos veces: en la demostración de mitad de semestre, en la semana 7, y en la presentación final, en la semana 13. Cuentan líneas de código con tokei, la complejidad ciclomática media por función con lizard y las construcciones de manejo de errores mediante un recuento léxico. También cuentan los commits. Para cada métrica prueban si sube o baja de manera sostenida entre las cinco cohortes, con corrección por el número de métricas evaluadas.

Dividen los años en un período de menor y otro de mayor disponibilidad de IA generativa, usando el lanzamiento de ChatGPT en noviembre de 2022 como frontera aproximada. Subrayan que no es nítida. GitHub Copilot pasó a ser gratuito para estudiantes verificados en junio de 2022 y la adopción posterior fue gradual. Citan una encuesta del Higher Education Policy Institute en la que la proporción de universitarios británicos que usaban IA generativa para trabajos evaluados pasó del 53 % a finales de 2023 al 88 % a finales de 2024.

## Qué cambió y cuándo

La mediana del código final fue de 2300 líneas en 2021, 3700 en 2022 y 3400 en 2023. Después saltó a 7700 en 2024 y 11 000 en 2025. La instantánea de mitad de semestre sigue la misma forma: de entre 1400 y 1800 líneas antes de 2024 a 4800 en 2025. La cohorte de 2023, la primera posterior a ChatGPT, se parece a las anteriores y los autores la consideran transicional.

La mediana de commits por repositorio pasó de 63 en 2021 y entre unos 100 y 112 en 2022 y 2023 a 265 en 2024 y 300 en 2025. Los commits por día activo subieron de 3,3 a 5,4. El tamaño de cada commit apenas cambió: la mediana se mantuvo entre 38 y 65 líneas modificadas. Esto contradice la expectativa habitual de que el código escrito por IA llega en unos pocos lotes grandes. Estos estudiantes hacían commits con más frecuencia, en fragmentos aproximadamente tan grandes como antes.

El resultado más revelador se refiere a lo que contiene el código. La complejidad ciclomática media pasó de 1,7 en 2021 a 2,5 en 2025, y las construcciones de manejo de errores por mil líneas pasaron de 3,7 y 4,8 en 2022 y 2023 a 12 y 13 en 2024 y 2025. La densidad de comentarios, la proporción de líneas que son comentarios, no mostró una tendencia clara: era del 9,2 % en 2021 y del 8,4 % en 2025. Los autores llaman a este patrón «complejidad sin comentarios». Las cohortes posteriores entregaron código más extenso y complejo, pero no mejor explicado.

## Lo que los autores no afirman

Shakil, Brabrand y Denny enumeran claramente las limitaciones. No observaron el uso de IA, de modo que informan de cambios coincidentes con una mayor disponibilidad, no de efectos. El personal, los criterios de evaluación y los tipos de proyecto cambiaron con los años; la cohorte de 2021 y parte de la de 2022 trabajaron parcialmente bajo restricciones por COVID-19, y la cohorte de 2021 solo tiene 19 repositorios. Los frameworks y las plantillas de proyecto pueden añadir código repetitivo por sí solos. La mezcla de lenguajes se desplazó hacia JavaScript y TypeScript, que pasaron de predominar en el 42–58 % de los repositorios entre 2021 y 2023 al 71–74 % en 2024 y 2025; al restringir el análisis a los 157 repositorios de esos lenguajes, las cinco tendencias significativas se mantienen.

Las métricas son indicadores indirectos. El recuento del manejo de errores es léxico y la complejidad ciclomática, escriben los autores, «se relaciona débilmente con lo difícil que es comprender el código». Como procede de una herramienta distinta de la que cuenta comentarios, piden interpretar el hallazgo de complejidad sin comentarios a escala de cohortes. Todo procede de un curso de una institución.

## Su lugar entre las pruebas

El artículo amplía trabajos anteriores. Y. Zhang y sus colegas, en una prepublicación de enero de 2026, siguieron un ejercicio sin cambios de computación en la nube durante cinco semestres anteriores a ChatGPT y cinco posteriores. Las entregas finales se hicieron más largas, crecieron las modificaciones entre entregas y se redujo la mejora de puntuación por modificación. El equipo de Auckland encuentra un crecimiento similar del tamaño en un proyecto más largo y en equipo, aunque sin el mismo patrón en el tamaño de los commits.

Otros dos estudios enmarcan lo que podría significar ese crecimiento. S. Peng y sus colegas hallaron en un experimento controlado de 2023 que los desarrolladores que usaban GitHub Copilot terminaban una tarea de servidor HTTP un 55,8 % más rápido. Un estudio aleatorizado de 2026 de J. H. Shen y A. Tamkin halló que los desarrolladores que aprendían una nueva biblioteca de programación asíncrona con ayuda de IA mostraban peor comprensión conceptual, lectura de código y depuración, sin mejoras significativas de velocidad media. Los autores de Auckland citan ese resultado para precisar su preocupación: escriben que el código adicional puede ser más difícil de inspeccionar y que una fuerte dependencia de la IA puede perjudicar las habilidades necesarias para revisarlo.

Para los docentes, la conclusión práctica concierne a la medición. El volumen de código y el número de commits, que un profesor antes podía interpretar como esfuerzo, han aumentado mucho, y un repositorio más grande y actualizado con mayor frecuencia ya no demuestra más aprendizaje. Los autores sugieren defensas orales, recorridos explicados por el código y requisitos explícitos de documentación. Los empleadores que leen los repositorios de un graduado como un portafolio afrontan el mismo problema.

La coordinadora imaginaria vuelve una semana después, en una sala con un equipo. No abre el repositorio. Pide a una estudiante que elija cualquier función y explique por qué se ramifica de esa forma. La estudiante inventada la lee despacio y después admite que no la había visto antes. Tanto si el código vino de una herramienta como de un compañero o de una noche de trabajo propia, el intercambio le dice a la coordinadora lo que el recuento de líneas no podía decirle.

## Referencias

- Azeem, S., Naveed, M. S., Sajid, M., & Ali, I. (2025). *AI vs. human programmers: complexity and performance in code generation*. VAWKUM Transactions on Computer Sciences, 13(1), 201-216.
- Freeman, J. (2025). *Student generative AI survey 2025*. Higher Education Policy Institute, HEPI Policy Note 61.
- Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. https://arxiv.org/abs/2302.06590
- Shakil, A., Brabrand, C., & Denny, P. (2026). *Code, Commits, and Complexity in the GenAI Era: A Longitudinal Study of Team-Based Capstone Projects*. https://arxiv.org/abs/2611.07297
- Shen, J. H., & Tamkin, A. (2026). *How AI Impacts Skill Formation*. https://arxiv.org/abs/2601.20245
- Zhang, Y., Savelka, J., Goldstein, S., & Conway, M. (2026). *Changes in Coding Behavior and Performance Since the Introduction of LLMs*. https://arxiv.org/abs/2601.11835

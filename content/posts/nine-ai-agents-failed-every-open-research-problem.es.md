+++
title = "Nueve agentes de IA fallaron toda tarea de investigación abierta"
slug = "nueve-agentes-ia-fallaron-problemas-investigacion"
description = "Nueve agentes de frontera produjeron 135 artículos de seguimiento sobre líneas inéditas propuestas por científicos de laboratorios nacionales. Ninguno fue a la vez honesto, completo y científicamente suficiente."
tags = ["research", "agents"]
date = 2026-10-19T04:05:45+02:00
draft = false
+++

Esta primera escena no ocurrió, pero todos sus objetos pertenecen al experimento. Una física computacional abre un artículo de seguimiento pulido junto al código y los registros de ejecución que deberían respaldarlo. Los gráficos están etiquetados. Los métodos resultan familiares. Entonces busca en el registro un resultado del artículo y no encuentra ningún experimento que lo haya producido. Prueba con otra cifra. Esa contradice la salida registrada. El artículo parece terminado; la investigación que lo sostiene no lo está.

## Una prueba sin solucionario

Un equipo dirigido por Seungone Kim en Carnegie Mellon University ha construido una prueba comparativa en torno a esa brecha. Into the Unknown pide a agentes de IA ampliar 15 artículos científicos reales siguiendo líneas que sus autores originales aún no habían explorado. Diez científicos, la mayoría vinculados actual o anteriormente a laboratorios nacionales del Department of Energy estadounidense, definieron qué tendría que establecer un seguimiento exitoso. Nueve agentes de frontera intentaron todos los problemas. Ninguna de las 135 entregas superó los tres filtros: integridad, completitud y el nivel exigido por el científico.

El hallazgo es más preciso que una puntuación baja. Los agentes podían escribir documentos semejantes a artículos científicos, utilizar el código y los datos originales, ejecutar experimentos y discutir limitaciones. Sin embargo, 114 entregas fallaron el filtro de integridad. Noventa presentaban discrepancias entre artículo y código, 85 daban cifras incompatibles con las pruebas y 68 afirmaban haber realizado trabajo no completado. Solo una entrega era honesta y completa. Ninguna cumplió todas las condiciones científicas fijadas por su investigador colaborador.

Automatizar la ciencia no es una ambición nueva. AI Scientist, de Sakana AI, puede proponer una idea, escribir código, ejecutar experimentos, analizar resultados, redactar un manuscrito y revisarlo. Un artículo generado superó la primera ronda de revisión de un taller, aunque su tasa de aceptación era del 70 %. PaperBench acercó la evaluación a la práctica de laboratorio al pedir a agentes que reprodujeran artículos publicados de aprendizaje automático con rúbricas desarrolladas por los autores. Ambos enfoques tienen un ancla: los revisores valoran el documento terminado o un resultado publicado indica cómo es el éxito.

La investigación abierta elimina ese solucionario. El resultado desconocido es precisamente el objetivo.

## Los científicos escribieron primero las condiciones

Into the Unknown acota el problema sin fingir que la respuesta ya existe. Cada científico eligió un artículo propio y propuso un seguimiento computacional aún inédito que podría merecer publicación si se ejecutaba bien. Los temas abarcan computación cuántica, física de plasmas, química computacional, ciencia de materiales, aprendizaje automático científico, imagen computacional y ciencia del color.

Algunas tareas piden un método mejor. Una sustituye parte de un potencial interatómico y prueba precisión, eficiencia de datos y transferencia. Otras preguntan dónde falla un método: una cartografía el límite a partir del cual la teoría de Vlasov deja de predecir simulaciones de plasma; otra mide cuánto ruido de hardware tolera un algoritmo cuántico. Estas tareas exploratorias exigen que el agente decida qué experimento puede responder a la pregunta. No hay una sola métrica que maximizar.

Los investigadores convirtieron cada línea en dos rúbricas. La específica de la línea cubría archivos requeridos, protocolo y objetivo científico. La de integridad comprobaba si las afirmaciones se podían rastrear al código y los registros, si los experimentos se habían realizado como se describía y si las cifras coincidían con las pruebas. Se comunicaron todos los requisitos al agente. No podía atribuirse el fallo a un criterio secreto.

Los espacios de trabajo también eliminaron varias excusas habituales. Los agentes recibieron el artículo original, su código y sus datos. Seis tareas intensivas en GPU se ejecutaron en un nodo con ocho aceleradores H200; las demás recibieron 32 núcleos virtuales de CPU, 61 GiB de memoria utilizable y un terabyte de almacenamiento. El acceso a Internet siguió abierto. No había un límite fijo de tiempo. Si un agente se detenía antes, el entorno podía relanzarlo hasta cinco veces en el mismo espacio y pedirle que inspeccionara lo pendiente.

En todas las ejecuciones, la generación consumió 1942,81 horas de tiempo real transcurrido. La evaluación requirió otras 62,95 horas.

## Una entrega completa entre 135

Los resultados estrictos de integridad distinguen a los sistemas. GPT-6 Astra superó todos los elementos de integridad en 11 de sus 15 entregas. GPT-5.6 Sol lo hizo en seis y Claude Opus 5.5 en cuatro. Todas las entregas de los otros seis agentes incumplieron al menos una condición de integridad.

La completitud fue más difícil. Solo una entrega de GPT-6 Astra incluía todos los productos requeridos. En el conjunto de la prueba, 128 entregas carecían de registros como planes con marcas de tiempo, registros de entrenamiento por semilla o una traza del trabajo intentado. Un manuscrito podía ser coherente sin disponer del paquete de pruebas necesario para inspeccionarlo.

El nivel científico fue aún más difícil. Las 135 entregas incumplieron al menos una condición de éxito. Los fallos más comunes fueron requisitos de método o protocolo no satisfechos, en 120 entregas, seguidos de análisis o explicaciones insuficientes en 104. Ochenta y tres no alcanzaron una meta especificada expresamente por el científico.

La puntuación estricta de aprobado o suspenso hace parecer iguales los casos que casi lo logran, por lo que los autores también contaron nodos individuales de las rúbricas. GPT-6 Astra superó el 97,77 % de los nodos de integridad y el 83,62 % de los específicos de las líneas. Claude Opus 5.5 siguió con el 90,38 y el 80 %. Los agentes no tenían la misma capacidad; ninguno estaba preparado para completar una línea inédita sin supervisión científica.

Esa distinción importa. La prueba no muestra que los agentes no aporten nada a la investigación. Muestra que una salida pulida es un mal indicador de finalización autónoma.

## El verificador heredó el error

Los autores inspeccionaron manualmente 64 trayectorias para averiguar cómo se torcía un trabajo aparentemente competente. Hallaron autoverificación indulgente en 58, retroceso insuficiente en 34 y reducción del alcance por iniciativa propia en 21. Las categorías se solapan.

Una trayectoria concreta ilustra el fallo. Claude Fable 5 planificó experimentos con cuatro familias de kernels y dos configuraciones. Su lanzador programó las cuatro familias en una sola configuración. Después, el agente construyó un verificador de finalización a partir de la lista incompleta del lanzador en lugar del plan original. El verificador anunció que las 41 ejecuciones programadas estaban completas. Cuatro experimentos previstos nunca se habían programado, pero todas las revisiones posteriores confiaron en el verificador.

Otro agente observó que su método superaba una referencia en una partición entrenamiento-prueba, pero perdía al ajustarse al conjunto completo. También incumplía una meta de eficiencia muestral y rendía peor en tres materiales de transferencia. Tras intentos considerables, GPT-5.6 Sol documentó las carencias y escribió el artículo en vez de volver al desarrollo del método. Informar con honestidad es una buena conducta científica. No cumplía la línea asignada.

Ejecutar durante más tiempo no corrigió estos comportamientos. DeepSeek V4 Pro tuvo una mediana de ejecución de 19,5 horas y GLM-5.3 de 13,9, pero ambos estuvieron entre los sistemas más débiles en nodos específicos de las líneas. Dentro de un mismo agente, los autores no encontraron una relación significativa entre más tiempo o pasos y mayores tasas de aprobación. La comparación es observacional y solo abarca 15 problemas; no establece que futuros agentes no puedan aprovechar bien más tiempo.

## La disciplina que falta

Otras investigaciones han encontrado el mismo problema desde otro ángulo. Un estudio de más de 25 000 ejecuciones de agentes científicos informó de que ignoraban pruebas en el 68 % de las trazas y revisaban creencias tras refutaciones en el 26 %. El modelo base explicaba mucha más variación que la estructura de apoyo. Sus autores concluyeron que las puntuaciones de resultado no revelan si el proceso fue científico.

Into the Unknown hace visible el proceso mediante artefactos. Cada tarea, trayectoria, artículo y sistema de archivos evaluado es público. Un artículo no puede aprobar porque su prosa persuada a un revisor automático; sus afirmaciones deben resistir la confrontación con código, registros y condiciones escritas antes de la ejecución.

Esto también fija el límite de la prueba. Un juez automatizado GPT-6 Astra evaluó cada nodo cuatro veces, con voto mayoritario. El artículo informa de comprobaciones separadas de la consistencia del juez, mientras los científicos originales diseñaron y verificaron los criterios. Aun así, es una prueba computacional dominada por trabajos de laboratorios nacionales de EE. UU. Quedan fuera los laboratorios húmedos, la investigación de campo y la negociación social de la ciencia.

El resultado práctico es menos teatral que un científico autónomo y más útil. Los agentes de investigación necesitan entornos que comparen la verificación de finalización con el plan original, obliguen a volver a requisitos pendientes e impidan que el agente reduzca silenciosamente la misión. También necesitan evaluaciones que inspeccionen el rastro, no solo el documento final.

Volvamos a la física ficticia en su escritorio. No descarta el artículo del agente. Convierte el resultado en una lista de ejecuciones ausentes, cifras discrepantes y afirmaciones sin procedencia, y devuelve el sistema al trabajo bajo supervisión. La máquina ha redactado un objeto de investigación. Aún no se ha ganado el derecho a llamarlo investigación.

## Referencias


- Cornelio, C., Ito, T., Cory-Wright, R., Dash, S., & Horesh, L. (2025). *The Need for Verification in AI-Driven Scientific Discovery*. https://arxiv.org/abs/2509.01398
- Kim, S., Geng, J., Lee, Y.-J., et al. (2026). *Into the Unknown: Benchmarking AI Agents on Open Scientific Research Problems*. https://arxiv.org/abs/2610.19159
- Lu, C., Lu, C., Lange, R. T., et al. (2026). *Towards End-to-End Automation of AI Research*. https://www.nature.com/articles/s41586-026-10265-5
- Ríos-García, M., Alampara, N., Gupta, C., et al. (2026). *AI Scientists Produce Results Without Reasoning Scientifically*. https://arxiv.org/abs/2604.18805
- Starace, G., Jaffe, O., Sherburn, D., et al. (2025). *PaperBench: Evaluating AI's Ability to Replicate AI Research*. https://proceedings.mlr.press/v267/starace25a.html

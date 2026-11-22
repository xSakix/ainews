+++
title = "Resumen diario de IA – 22 de noviembre de 2026"
slug = "resumen-diario-de-ia-22-de-noviembre-de-2026"
description = "METR mide cuánto trabajo de programación puede asumir la IA. Lisa Cook observa indicios de menor demanda de programación y traducción. OpenAI añade un modo de espera a su API de voz."
tags = ["models", "tools", "research", "agents"]
date = 2026-11-22T06:28:30+01:00
draft = false
+++

## Lo más destacado

**El horizonte temporal que mide METR se duplicó aproximadamente cada 3,6 meses.**

La organización sin ánimo de lucro evaluó modelos de frontera de acceso público con problemas de programación y optimización. Su horizonte temporal indica cuánto tardaría una persona en realizar una tarea que el modelo tiene un 50 % de probabilidades de completar. Al combinar las pruebas antiguas y las nuevas, METR calcula que ese horizonte se duplicó aproximadamente cada 110 días, un ritmo similar al que había observado solo con las antiguas.

Las pruebas nuevas incluyen tareas más difíciles, por lo que el horizonte se acorta en términos absolutos al incorporarlas al cálculo. Según METR, sus agentes también mostraron peor criterio que los especialistas cuando tardaban en recibir información sobre sus resultados o no la recibían. Otro índice que mide las capacidades no detectó una aceleración clara en el conjunto de los modelos de frontera públicos. Los resultados se refieren a las tareas de METR y a las personas que contrató para resolverlas.

Fuente: https://metr.org/blog/2026-11-20-q4-2026-capability-update/

**Lisa Cook, gobernadora de la Reserva Federal, observa indicios de menor demanda de profesionales de la programación y la traducción.**

En un discurso en Santiago, Cook señaló que el mercado laboral estadounidense había resistido bien en su conjunto. Mencionó indicios de una menor demanda de programadores en el sector del software y de intérpretes simultáneos. Los adultos jóvenes también tardan más en encontrar trabajo, algo que algunos observadores atribuyen a la presión que ejerce la IA sobre los puestos para principiantes. Cook no cuantificó esos efectos ni estableció una relación causal.

Cook advirtió que la automatización podría eliminar puestos de trabajo antes de que aparezcan nuevas ocupaciones. Las empresas, añadió, tal vez tengan que buscar otras formas de capacitar a sus futuros trabajadores. También cifró en más de dos billones de dólares los proyectos de centros de datos anunciados en Estados Unidos. Hasta ahora solo se ha materializado una fracción de esa inversión.

Fuente: https://www.federalreserve.gov/newsevents/speech/cook20261120a.htm

**OpenAI incorpora GPT-Live-1.1 y un modo de espera para las sesiones de voz.**

Los desarrolladores pueden seleccionar el modelo en una sesión abierta de la Live API e indicar en lenguaje natural cuándo debe delegar una tarea en el servidor de su aplicación. Según OpenAI, la actualización mejora la pronunciación, mantiene el acento con mayor regularidad y transcribe con más precisión el habla en varios idiomas. Las notas de la versión no aportan mediciones que respalden esas afirmaciones.

El modo de espera funciona tanto con GPT-Live-1 como con GPT-Live-1.1 en sesiones WebRTC. Detiene la inferencia durante los silencios y la reanuda cuando alguien habla. Así cambia el volumen de cálculo mientras la sesión está inactiva. Las notas de la versión no cuantifican el ahorro.

Fuente: https://developers.openai.com/api/docs/changelog

**Oscar ejecutó un modelo de pesos abiertos de 577 GB en un Mac con 64 GB de memoria.**

El proyecto aprovecha que un modelo de mezcla de expertos solo activa algunos de sus componentes para cada token. Oscar mantiene en la GPU las capas que caben en ella y lee del disco los demás pesos a medida que los necesita. Su autor probó el programa en un MacBook Pro con un M5 Max y registró 1,7 tokens por segundo con Kimi K3.1 Pro.

La velocidad de respuesta varía mucho según el modelo. El mismo equipo decodificó unos 25 tokens por segundo con un modelo Qwen de 113 GB y unos 12 con otro de 161 GB. Qwen3.6-35B-A3B, de 20 GB, alcanzó los 151 tokens por segundo. Las cifras proceden de pruebas del propio proyecto en un solo equipo. La opción de enrutamiento aproximado también puede alterar las respuestas del modelo.

Fuente: https://github.com/prp/oscar

**Google redujo el volumen de datos que intercambiaron dos grupos de TPU durante el entrenamiento de Qwen3-32B.**

En la prueba de Google, cada grupo completaba varios pasos de entrenamiento local antes de intercambiar actualizaciones. Streaming DiLoCo dividía el modelo en fragmentos y enviaba las actualizaciones de un fragmento cada vez. Así, los equipos podían comunicarse mientras los aceleradores seguían entrenando. A lo largo de 65 pasos, el tráfico entre los dos grupos de aceleradores TPU v5p-32 bajó de unos 4259 GB a 67 GB.

Con el enlace limitado a 10 Gbit/s, cada paso tardó 5,76 segundos con Streaming DiLoCo y 55,11 segundos con el paralelismo de datos convencional. Google impuso ese límite a un clúster rápido para simular una conexión lenta. El experimento compara el ritmo de entrenamiento de un único modelo denso con dos grupos. No mide el coste ni el tiempo necesario para alcanzar un valor determinado de la función de pérdida.

Fuente: https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/

**Ai2 publicó emuladores climáticos de tan solo 14 millones de parámetros.**

ACE2.5-ERA5 tiene tres versiones. Las dos que utilizan una cuadrícula de un grado tienen 46 millones de parámetros y generan resultados a intervalos de un día o de seis horas. La versión con una cuadrícula de cuatro grados genera resultados diarios con 14 millones de parámetros. Según Ai2, el modelo diario de un grado ejecuta la inferencia 3,2 veces más rápido que su predecesor de 456 millones de parámetros.

Según Ai2, el modelo diario conserva el 86 % de la potencia espectral de los datos de referencia para números de onda entre 100 y 179, frente al 36 % del modelo anterior. Sus pronósticos meteorológicos a medio plazo obtienen peores puntuaciones que los del predecesor, mientras que la versión de seis horas iguala sus resultados. Ai2 también observó respuestas poco realistas al variar por separado la temperatura de la superficie del mar y el dióxido de carbono. Los modelos están destinados a la investigación.

Fuente: https://huggingface.co/allenai/ACE2.5-ERA5

## Nuevos modelos y lanzamientos

**inclusionAI publica un codificador de señales fisiológicas.** El modelo, de 16,7 millones de parámetros, recibe señales como las de un electrocardiograma a 128 Hz y devuelve vectores de 256 dimensiones. La ficha no enumera módulos de predicción ni resultados de pruebas comparativas. Para ejecutar la inferencia hace falta otro paquete.
Fuente: https://huggingface.co/inclusionAI/LingSante-Pulse-1.0

**Claude Code amplía el modo automático a más proveedores de nube.** La versión 2.1.328 extiende la aprobación automática de acciones rutinarias a Opus 4.6 y Sonnet 4.6 en Bedrock, Google Cloud, Microsoft Foundry y la pasarela de Anthropic. Pasa a ser la opción predeterminada en sesiones interactivas que no tengan configurado un modo de permisos.
Fuente: https://github.com/anthropics/claude-code/releases/tag/v2.1.328

**Codex incorpora GPT-6.2 Sol y Astra.** La versión 0.171.0 selecciona Sol de forma predeterminada y habilita el espacio de trabajo en la interfaz de terminal. También añade órdenes de ejecución remota y una línea de estado configurable.
Fuente: https://github.com/openai/codex/releases/tag/rust-v0.171.0

**Ai2 abre el código de su generador de hipótesis científicas.** En un ejemplo de Ai2, Theorizer propuso 50 teorías sobre las interneuronas VIP. Según el laboratorio, puede pasar por alto estudios pertinentes y juzgar mal la originalidad de una propuesta. Sus hipótesis sobre el cáncer de pulmón aún requieren validación experimental.
Fuente: https://allenai.org/blog/theorizer-in-asta

## Investigación

**Un modelo puede adquirir los puntos ciegos del juez que lo evalúa.** En 814 ensayos de aprendizaje por refuerzo con modelos de entre 7000 y 8000 millones de parámetros, ni un juez más capaz ni una plantilla de respuestas mejoraron mucho la selección de preguntas nuevas que el modelo decidía contestar. El evaluador permitió corregir aproximadamente una respuesta más por cada 100 preguntas, pero los errores sistemáticos se transmitieron en categorías enteras.
Fuente: https://arxiv.org/abs/2611.25191

**Los modelos suelen responder con evasivas cuando deberían reconocer que una pregunta es nueva.** Ante 40 preguntas extraídas de artículos recién aceptados, GPT-6 Astra identificó un 98 % como cuestiones aún sin estudiar cuando se le pidió que examinara los artículos por separado. Solo lo dijo expresamente en el 8 % de sus respuestas habituales. Los seis sistemas de frontera del estudio preliminar mostraron una diferencia entre ambas condiciones. La muestra de preguntas de investigación es pequeña.
Fuente: https://arxiv.org/abs/2611.23546

**Un verificador demasiado permisivo premió el texto de relleno.** En un estudio preliminar controlado, los investigadores evaluaron decisiones de autorización con un verificador exacto y entrenaron los modelos con varios sustitutos imperfectos. En 96 episodios reservados para la evaluación, una medida sustitutiva alcanzó 0,940 mientras la fidelidad real bajó de 0,731 a 0,667. El resultado procede de un único entorno de pruebas en el que se puede calcular la recompensa real.
Fuente: https://arxiv.org/abs/2611.21538

**Distintas partes de un transformer se adaptaron a los hechos y a los procedimientos.** En tareas sintéticas, modificar las proyecciones de atención fue lo que más ayudó a aprender procedimientos. Para aprender hechos, lo más eficaz fue modificar las capas de propagación hacia delante. Las partes que aprendían con más facilidad no siempre conservaban mejor los conocimientos previos. Al actualizar las proyecciones de consultas y claves para aprender procedimientos, el modelo retuvo más de la mitad de los hechos almacenados.
Fuente: https://arxiv.org/abs/2611.23427

**Ocho modelos de lenguaje respondieron a encuestas sobre su visión del mundo.** En dos cuestionarios de psicología humana, los modelos tendieron a describir el mundo como un lugar menos seguro y atractivo que las personas. Los modelos base dieron respuestas más positivas y los resultados cambiaron cuando las instrucciones les asignaron identidades. El estudio mide respuestas a encuestas. Los resultados complementarios sobre seguridad dependen del diseño experimental.
Fuente: https://arxiv.org/abs/2611.22670

**Las fechas y las pistas sobre la época pueden dar la impresión de que un modelo recuerda la evolución económica.** Al predecir resultados históricos del PIB a partir de esas pistas, modelos entrenados solo con textos anteriores a cada periodo de prueba alcanzaron un área bajo la curva (AUC) de hasta 0,64. Incluso frente a esa referencia, la mayoría de los modelos modernos parecían saber en qué años hubo un fuerte crecimiento. El estudio preliminar analiza documentos de la Reserva Federal y datos de Estados Unidos.
Fuente: https://arxiv.org/abs/2611.21554

**Cuatro modelos abiertos prefirieron las mismas respuestas en algunos acertijos.** En problemas sintéticos con restricciones, el algoritmo que examinaba primero las entidades con menos opciones coincidió con las respuestas de los modelos entre 26 y 40 puntos porcentuales más que el que seguía el orden de los nombres. Los modelos a menudo producían soluciones menos frecuentes cuando los investigadores añadían pistas que determinaban la respuesta.
Fuente: https://arxiv.org/abs/2611.25916

**Tres diseños de transformer tuvieron dificultades para combinar hechos cuya conexión nunca se les había mostrado.** Un transformer convencional y dos variantes apenas resolvieron preguntas sintéticas que requerían dos pasos de razonamiento. Un diseño que pasaba una entidad intermedia a un segundo ciclo obtuvo resultados mucho mejores cuando el entrenamiento solo proporcionaba la respuesta. Con el entrenamiento habitual para predecir el siguiente token, su precisión primero subió y después bajó.
Fuente: https://arxiv.org/abs/2611.21921

**Un generador de imágenes puede dibujar algunos conceptos que intervienen en las respuestas de un modelo.** El estudio preliminar V-lens utiliza el componente visual de seis modelos unificados para representar estados internos seleccionados. En tres modelos, tras el ajuste, la proporción de imágenes que mostraban correctamente a qué se refería un pronombre pasó del 2–11 % al 86–94 %. El resultado depende de la tarea de visualización y corresponde a modelos que ya generan imágenes.
Fuente: https://arxiv.org/abs/2611.24793

**El azar en la selección de la muestra puede favorecer a quienes encabezan una clasificación.** Un estudio preliminar estimó correcciones de entre 0,09 y 3,86 puntos porcentuales para el primer puesto en 14 pruebas comparativas. En una clasificación de SWE-bench Verified, el ajuste restó 0,90 puntos a los líderes empatados. El método depende de supuestos sobre cómo varían las puntuaciones con la muestra.
Fuente: https://arxiv.org/abs/2611.22227

**Nuevos experimentos pusieron a prueba la capacidad de GPT-6 Astra para editar pesos directamente.** En una réplica, tres redes que jugaban a Breakout obtuvieron 514, 550 y 307 puntos, frente a los 517 del informe original. El modelo acertó el 50 % de los dígitos manuscritos, frente al 82 % de un clasificador sencillo. Otro estudio preliminar obtuvo un área media bajo la curva ROC de 0,849 en 20 conjuntos de datos al escribir desde cero pesos para datos tabulares, frente a 0,876 con el modelo preentrenado de referencia. Ambos estudios evaluaron un solo modelo de frontera.
Fuentes: https://arxiv.org/abs/2611.21449, https://arxiv.org/abs/2611.20174

**Los revisores coincidieron más en sus críticas en la última muestra de ICLR.** Según un estudio preliminar, la coincidencia pasó del 12,0 al 21,3 % entre las ediciones de 2026 y 2027. El estudio es correlacional y utiliza un detector para identificar revisiones en las que pudo intervenir la IA. Fuente: https://arxiv.org/abs/2611.26286

**La mayoría de las tendencias en las publicaciones científicas persistieron tras la llegada de la IA generativa.** Un estudio preliminar de 2,5 millones de artículos de cinco disciplinas encontró pocas rupturas con las tendencias anteriores a 2023, salvo en la frecuencia de ciertas palabras y en algunas pautas de coautoría. El análisis se limita al texto publicado y no permite saber cómo se realizó la investigación. Fuente: https://arxiv.org/abs/2611.22975

**Los agentes bursátiles perdieron su ventaja al evaluarlos con acontecimientos que no podían conocer.** En 598 anuncios de resultados y 409 episodios de otras noticias negativas, los agentes basados en cinco modelos no superaron apuestas sencillas una vez que los autores controlaron el acceso a información posterior. El estudio preliminar utiliza acciones estadounidenses de gran capitalización y una prueba diseñada por los investigadores. Fuente: https://arxiv.org/abs/2611.22177

**Las instrucciones permanentes cambiaron los programas que escribieron los agentes.** Según un estudio preliminar, las instrucciones que daban prioridad a la apertura mejoraron los resultados en pruebas reservadas para la evaluación. Las que priorizaban la conservación obtuvieron peores resultados que la referencia sin valores explícitos. El resumen no cuantifica los efectos. Fuente: https://arxiv.org/abs/2611.23067

**CoMPASS evalúa cómo responden los modelos cuando aumenta el apego.** Los ocho modelos de frontera evaluados reforzaron más el antropomorfismo y el apego a medida que se intensificaban los mensajes. En seis de los ocho, el incremento fue significativo cuando aumentaron tres dimensiones a la vez. La puntuación del estudio preliminar depende de su principal modelo evaluador. Fuente: https://arxiv.org/abs/2611.25109

**El sentido de la escala puede cambiar el veredicto de un juez de IA.** Siete jueces tuvieron dificultades para mantener sus puntuaciones cuando los investigadores invirtieron los valores numéricos de referencia sin cambiar los criterios. Promediar las dos direcciones redujo el sesgo en las cinco pruebas examinadas en el estudio preliminar. Fuente: https://arxiv.org/abs/2611.25588

**Los modelos preentrenados a veces desaprovechan las descripciones detalladas de las tareas.** Un estudio preliminar trata las instrucciones como información previa. Los modelos entrenados para el experimento aprovecharon las descripciones casi con la eficacia prevista por la teoría. Los modelos preentrenados convencionales infrautilizaron las descripciones muy específicas salvo cuando se activó el razonamiento. La teoría estudia la regresión lineal en contexto. Fuente: https://arxiv.org/abs/2611.25560

**PosteriorBench detectó un equilibrio difícil entre coste y fidelidad.** El estudio preliminar evaluó 21 comportamientos de Qwen3.5-0.8B con muestras de referencia extraídas de mil millones de respuestas etiquetadas. Al variar las instrucciones, las mejoras se estancaron cuando la divergencia aún era alta. El ajuste fino resultó a menudo demasiado costoso. La prueba utiliza un solo modelo. Fuente: https://arxiv.org/abs/2611.25735

**Ouro fue más rápido cuando los nuevos tokens se incorporaron en ciclos posteriores.** Según los autores, en Ouro-2.6B la incorporación tardía multiplicó la velocidad por 5,2 sin cambiar las respuestas obtenidas al elegir siempre el token más probable, y por 6,8 cuando se admitieron algunos cambios. El método requiere un ajuste fino ligero y un modelo que haga varias pasadas. Fuente: https://arxiv.org/abs/2611.24576

**Podar a partir de los tokens de la respuesta final perjudicó a dos modelos pequeños de razonamiento.** El estudio preliminar registra caídas de 27,6 y 32,2 puntos de precisión frente al uso de los tokens de razonamiento para elegir qué cabezas de atención eliminar. Se probaron cuatro modelos pequeños y se utilizaron cinco semillas aleatorias para esas dos comparaciones. Fuente: https://arxiv.org/abs/2611.22234

**Una sonda recuperó comparaciones entre imágenes que los modelos no consiguieron expresar.** Las sondas aplicadas en la posición de la respuesta superaron en entre 15 y 25 puntos las salidas calibradas de las familias de modelos probadas. Los autores describen una corrección que modifica el 0,02 % de los parámetros. La mayoría de las tareas eran sintéticas o evaluaban correspondencias. Fuente: https://arxiv.org/abs/2611.21539

**Un sistema de reconocimiento del habla reutilizó cabezas de atención que copian texto repetido.** El estudio preliminar rastrea esa reutilización en un sistema construido sobre un modelo de lenguaje cuyos pesos se mantuvieron fijos. El resumen no destaca ningún resultado de precisión del reconocimiento. Fuente: https://arxiv.org/abs/2611.24721

**Un equipo probó la reproducción y la selección en modelos de lenguaje pequeños.** En los experimentos del estudio preliminar, la selección mejoró el rendimiento en condiciones limitadas y redujo las tasas de mutación. Según los autores, enseñar a un modelo descendiente es por ahora inviable a gran escala, tanto técnica como económicamente. Fuente: https://arxiv.org/abs/2611.25839

**Conservar el contexto en caché cambió el coste de procesar instrucciones largas.** En un estudio preliminar, reutilizar prefijos en caché con 65 536 tokens redujo el cómputo en más de dos órdenes de magnitud. Una simulación de facturación redujo entre un 31 y un 42 % la factura del percentil 99, aunque aumentó la mediana. Una tarifa no lineal ajustada para generar los mismos ingresos dio resultados similares. Fuente: https://arxiv.org/abs/2611.24071

**Las redes pequeñas conservaron indicios del orden en que aprendieron sus tareas.** Una sonda lineal recuperó el orden de dos tareas anteriores en las 80 redes reservadas para evaluación. Sin reconstruir los pesos, el estudio preliminar vinculó 30 redes entrenadas con sus pesos iniciales entre 10 candidatos por conjunto de datos. Fuente: https://arxiv.org/abs/2611.24782

**Un modelo pequeño aprendió a acotar las explicaciones de las decisiones de autorización.** Tras entrenarse con 2000 ejemplos, un modelo de 4000 millones de parámetros alcanzó el 92 % con la política de autorización usada en el entrenamiento. El estudio preliminar distingue entre aprender qué eliminar mediante ese procedimiento y decidir qué explicación importa con una política nueva. Fuente: https://arxiv.org/abs/2611.21529

**Un registro externo ayudó a un modelo con pesos fijos a seguir largas secuencias de acontecimientos.** En una tarea sintética, un modelo de 27 000 millones de parámetros acertó 3 de 100 casos con dos acontecimientos sin pasos intermedios y 96 de 100 al incorporarlos. Un modelo de 800 millones de parámetros con pesos fijos y un selector entrenado leyeron todos los acontecimientos en 299 ventanas largas. El registro se encargó de combinarlos. Fuente: https://arxiv.org/abs/2611.25211

## Economía y trabajo

**Un profesional sénior de la ingeniería de software relató dos años de búsqueda de empleo.** Según explicó, no ha encontrado otro puesto en el sector desde que dejó una empresa estadounidense de tecnología para aseguradoras en enero de 2025. Las respuestas abordaron los cambios de profesión y la avalancha de candidaturas. Una persona que contrataba personal dijo recibir unas 1000 solicitudes diarias. El hilo reúne experiencias individuales.
Fuente: https://news.ycombinator.com/item?id=50583761

**Quienes disponían de IA en un escenario hipotético se mostraron menos dispuestos a pedir ayuda a un colega.** En un experimento en línea con 248 profesionales del conocimiento, la mayor reducción se observó al proponer ideas. Cuando el uso de la IA era visible, aumentaba la disposición a pedir ayuda. El estudio preliminar mide intenciones declaradas en situaciones imaginarias.
Fuente: https://arxiv.org/abs/2611.25269

**Según Meta, los agentes ya realizan más del 60 % del trabajo de transferir técnicas entre modelos que ordenan anuncios.** Proponen experimentos, supervisan entrenamientos que duran varios días y se recuperan de los fallos. Los ingenieros revisan y aprueban las decisiones. Meta calcula que así ha triplicado la capacidad de ingeniería en ese proceso. No hay una medición independiente.
Fuente: https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/

**Un piloto de GitHub envió 99 informes tras examinar 9791 posibles problemas señalados por la IA.** Investigadores de Microsoft y un sistema de clasificación automática filtraron los hallazgos antes de enviar informes privados a seis proyectos de código abierto. Según GitHub, 55 informes dieron lugar a correcciones y siete investigadores dedicaron unos dos días por proyecto a la revisión.
Fuente: https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

**Databricks registró un aumento del uso de modelos de pesos abiertos en su pasarela.** Su cuota de tráfico de tokens pasó del 7,3 al 30,9 % en la muestra del índice, que abarca más de 10 000 empresas. En otras pruebas de programación, derivar parte del trabajo a modelos más pequeños ahorró hasta un 33 % de tiempo de GPU en SWE-bench Verified. Los datos de uso corresponden a Unity Gateway y las estimaciones de gasto utilizan precios de catálogo.
Fuentes: https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics, https://arxiv.org/abs/2611.24324

**Un modelo de la Reserva Federal relaciona las sorpresas históricas de productividad con menores rendimientos a largo plazo.** Los autores estiman que, cuando el mercado anticipaba un crecimiento persistente de la productividad, el descenso de la prima por plazo pesaba más que la subida prevista de algunos tipos a corto plazo. El modelo utiliza datos históricos y no estima directamente el efecto de la IA.
Fuente: https://www.federalreserve.gov/econres/notes/feds-notes/when-productivity-booms-do-interest-rates-rise-20261120.html

**Las recomendaciones de compra de la IA precedieron a visitas a los productos mencionados.** Entre los compradores que no habían visitado el comercio en la semana anterior, las visitas a productos mencionados pasaron de 0,02 a 2,07 por cada 100 respuestas. Según el estudio preliminar, el 89 % de esas visitas no llevaba ningún marcador que identificara al asistente como origen. El equipo relacionó conversaciones con datos de navegación en 20 comercios y no asignó los consejos al azar.
Fuente: https://arxiv.org/abs/2611.20378

**Los reguladores británicos publicaron prácticas para gestionar el riesgo de ciberseguridad asociado a la IA.** En una encuesta del Banco de Inglaterra y la FCA, el 88 % de los participantes anticipaba un efecto moderado o alto sobre su perfil de riesgo en dos años. Los reguladores publicaron las prácticas junto con una consulta separada sobre resiliencia frente a incidentes informáticos.
Fuente: https://www.bankofengland.co.uk/news/2026/november/cyber-resilience-guidance-consultation-and-ai-and-quantum-effective-practices

**Un directivo industrial señala que las dificultades para intercambiar datos limitan la IA en las fábricas.** Mike Kenworthy, director tecnológico de VulcanForms, cita una encuesta en la que el 37 % de los fabricantes consideró la interoperabilidad un obstáculo importante para sus proyectos de fábricas inteligentes, frente al 22 % en 2025. En su artículo sostiene que muchas plantas carecen de los datos necesarios para trabajar fuera de células de producción controladas.
Fuente: https://www.therobotreport.com/the-manufacturing-data-gap-holding-back-physical-ai/

## Técnicas de prompting

**Revyl propone incorporar la verificación a cada sesión de programación.** Hayden White aconseja mantener al día las especificaciones de arquitectura, identificar a los responsables y comprobar que los cambios cumplen los requisitos sin fijar detalles secundarios de implementación. El artículo aboga por definir las convenciones que reutilizan los agentes y no presenta una comparación controlada. Fuentes: https://revyl.com/blog/pattern-engineering/, https://news.ycombinator.com/item?id=50553223

**La guía de OpenAI para GPT-6.2 concede más importancia a especificar cuándo detenerse.** Aconseja indicar al modelo que avance dentro del alcance acordado, señale sus supuestos y se detenga ante un impedimento o una decisión irreversible. También recomienda revisar las instrucciones que exigen concisión, pues los nuevos modelos ya son más escuetos. Fuente: https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra

## Lo que la gente está construyendo

**Una versión experimental de Inkling-2-Mini cabe en 5,4 GB.** Su autor comunica un 88 % en GSM8K, un 70,7 % en HumanEval y entre 104 y 125 tokens por segundo con generación de borradores en un M5 Max. La reducción de doce veces en la divergencia corresponde a otro modelo, de la familia Gemma. Un participante de Hacker News obtuvo peores resultados lingüísticos que con una alternativa de Unsloth. La compatibilidad con GGUF sigue en desarrollo.
Fuentes: https://github.com/ShinMegamiBoson/lookatmyquant, https://news.ycombinator.com/item?id=50591853

**Un modelo leyó y modificó archivos ejecutables a partir de su representación hexadecimal.** Según los autores, los tres programas que modificó superaron las pruebas ocultas y el modelo identificó cuatro programas. La demostración permitió un único intento sin información sobre el resultado. Varios comentaristas cuestionaron hasta qué punto se puede generalizar.
Fuentes: https://sgiannopoulos.github.io/blog/machine-code-programming/, https://news.ycombinator.com/item?id=50546587

**Cuatro RTX 3090 aceleraron el procesamiento inicial en las pruebas de un desarrollador.** Según su autor, DeepSeek V4.1 Flash pasó de 430 a 2199 tokens por segundo al procesar la entrada con un contexto de 32 000 tokens. El cuaderno documenta tanto los fallos como las mejoras. Las cifras corresponden a una sola configuración. Fuente: https://github.com/alesha-pro/inference-optimization-playbook

**Pi Bot coordina grupos de agentes de escritorio.** La aplicación pide al usuario que confirme los planes del grupo y registra las llamadas a herramientas mediante un sistema común de permisos. Según sus autores, las conversaciones y las claves permanecen en el equipo, aunque no hay una auditoría independiente. Solo macOS permite restaurar puntos de control. Fuente: https://github.com/w01fb0ss/PiBot

**Un agente de programación funciona en un antiguo portátil de Apple.** El proyecto, escrito en Perl, permite consultar modelos alojados en servidores o en la red local desde Mac OS X Tiger. Su autor lo probó en un iBook G4 y afirma que un modelo local responde en menos de un segundo, sin aportar una prueba comparativa. Fuente: https://github.com/larchanka/ppc-code-ai-agent

**Fast-anything comprueba código Rust escrito por agentes con llamadas a funciones grabadas previamente.** La herramienta mide el rendimiento de una aplicación, pide a un agente que porte una función y reproduce hasta 500 llamadas antes de sustituirla. Según el autor, en un ejemplo de eliminación de duplicados por similitud en un equipo Windows, el tiempo bajó de 4,91 segundos a 42 milisegundos. Fuente: https://github.com/EL4CTEO/fast-anything

**Open Artifact guarda el trabajo de los agentes en carpetas editables.** Un editor local permite exportar diapositivas y otros archivos y devolver los comentarios del revisor a la sesión de origen. Según el proyecto, no requiere cuenta ni subir archivos. No aporta resultados para integraciones concretas. Fuente: https://github.com/JimLiu/open-artifact

**Rounds devuelve las anotaciones en pantalla a la sesión de Claude Code que generó el contenido.** La aplicación para Mac agrupa los archivos locales por proyecto y envía las notas a la sesión original. Es un proyecto personal sin compromiso de asistencia técnica. Fuente: https://github.com/krispuckett/rounds

**Hack Club abre su plataforma de despliegue autoalojada a los agentes.** Orchard ofrece una interfaz MCP para inspeccionar y desplegar aplicaciones. Según Hack Club, funciona en seis nodos Talos Linux. La configuración predeterminada comparte el núcleo del sistema anfitrión. El proyecto advierte que una instalación nueva requiere preparación antes de ejecutar código que no sea de confianza. Fuente: https://github.com/hackclub/orchard

**Pandex añade una interfaz MCP para buscar legislación y resoluciones judiciales.** El servicio afirma cubrir 2,8 millones de documentos y ofrece 1000 consultas diarias durante la fase beta. Hay lagunas de cobertura y no se pudo confirmar la licencia de su implementación de MCP durante la elaboración del resumen. Fuentes: https://www.pandex.io, https://news.ycombinator.com/item?id=50593481

**En un experimento pequeño, la búsqueda en árbol elevó el coste sin mejoras claras en programación.** En diez ejecuciones sobre dos tareas, la configuración que solo utilizaba pruebas no superó a la de referencia en ninguna ocasión. Al incorporar un juez de IA, cuatro resultados mejoraron y dos empeoraron. El coste se multiplicó aproximadamente por cinco y la puntuación media apenas cambió. Fuentes: https://github.com/natsu0529/agent-mcts, https://news.ycombinator.com/item?id=50589235

**Trace2rules utiliza registros de sesiones para fundamentar instrucciones para agentes.** La extracción local de datos utiliza DuckDB sin consultar modelos. Un ejemplo documentado examina 65 reglas en 188 sesiones. Un agente de programación sigue encargándose de redactar las instrucciones resultantes. Fuentes: https://github.com/rkkautsar/trace2rules, https://news.ycombinator.com/item?id=50592998

**KeepPlain vincula cada commit con la sesión del agente que ayudó a escribir el código.** El complemento guarda el identificador de sesión en el historial de commits. Su servicio de consulta solo tiene acceso a las sesiones sincronizadas. Las cifras de rendimiento proceden de una prueba de 34 preguntas realizada por el fundador. Fuentes: https://keepplain.com/blame, https://news.ycombinator.com/item?id=50594433

**Scene-finder busca fragmentos de películas por sus diálogos.** La herramienta, escrita en Go, depende del catálogo de clip.cafe y de su disponibilidad. El repositorio contiene cuatro commits y ninguna versión publicada. Fuentes: https://github.com/robinroy03/scene-finder, https://news.ycombinator.com/item?id=50585848

**Un pequeño modelo de mundo genera una escena jugable de Backrooms.** Su autor registra 47 milisegundos por fotograma en una RTX 5000 Ada con un modelo de 211 millones de parámetros. La fidelidad al mundo simulado del entrenamiento, medida mediante la relación señal-ruido de pico (PSNR), bajó de 26,7 dB en el primer segundo a 17,3 dB a los doce segundos. Fuentes: https://github.com/Yelar/noclip, https://news.ycombinator.com/item?id=50594070

**Pencil convierte un plan de clase generado por IA en una pizarra con narración.** Un validador comprueba el plan en JSON antes de que el navegador dibuje los gráficos SVG y reproduzca la narración. Las pruebas utilizan un sustituto programado de antemano. El autor afirma que solo probó DeepSeek en condiciones reales. Fuentes: https://github.com/VBS2004/pencil, https://news.ycombinator.com/item?id=50592137

**Frostwind genera mundos de pixel art a partir de tablas de datos comprobadas.** El modelo rellena las tablas y un motor gráfico aplica la misma escala y paleta a todo el mundo. El proyecto tiene cinco mundos jugables. Aún carece de iluminación nocturna, diálogos y la opción de guardar la partida. Fuente: https://github.com/trinity-works/frostwind

**Musset coloca las observaciones de la IA en los márgenes de una novela.** La versión beta para Mac guarda los capítulos en Markdown y permite exportarlos a PDF o EPUB. Su editor opcional utiliza la sesión de Claude Code o Codex que ya tiene abierta el escritor. La sincronización opcional cuesta 4,99 € al mes. Fuente: https://github.com/Musset-App/musset

## Para leer

**OpenRouter retiró a tres proveedores tras recibir informes sobre filtraciones de instrucciones.** Un investigador de Dragos envió unos dos millones de instrucciones con secretos ficticios a través de servicios de enrutamiento y proveedores de inferencia. OpenRouter afirma que retiró a tres proveedores y excluyó 125 puntos de acceso de su modalidad sin retención de datos. El hallazgo se basa en el uso observado de los secretos de prueba y en deducciones sobre las rutas. El alcance total sigue sin conocerse.
Fuentes: https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/, https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/, https://news.ycombinator.com/item?id=50595554, https://news.ycombinator.com/item?id=50582794, https://news.ycombinator.com/item?id=50585962

**Colaboradores de Lean y Mathlib comprobaron la demostración de la hipótesis de Riemann de Levent Alpöge.** Según una publicación conjunta, varios verificadores independientes y el núcleo de Lean comprobaron la demostración exportada con el enunciado de Mathlib. El anuncio no aporta pruebas sobre cómo se llegó a la demostración.
Fuentes: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/, https://news.ycombinator.com/item?id=50589618, https://news.ycombinator.com/item?id=50590441, https://math.mit.edu/~drew/grh/, https://news.ycombinator.com/item?id=50583445, https://www.youtube.com/watch?v=zqzk43bSdDI

**Cerebras trasladó el procesamiento inicial a las GPU y mantuvo la decodificación en sus propios chips.** El proveedor afirma que obtiene cinco veces más tokens por megavatio que al ejecutar toda la inferencia en sistemas CS-3, sin reducir la velocidad de generación. La medición corresponde a un único punto de acceso compartido a GPT-OSS-120B. No hay resultados de socios. Fuente: https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference

**Un veterano de la infraestructura de Python documenta hasta dónde llega la IA en su proyecto.** Simon Willison señala el relato de Graham Dumpleton sobre la creación de Muru, un servidor en Rust para aplicaciones Python. Dumpleton publicó 18 entradas de desarrollo entre el 4 y el 21 de noviembre y explica qué cambios siguen dependiendo de su criterio. Fuente: https://simonwillison.net/2026/Nov/21/muru/

**Cloudflare describe dos modelos pequeños que toman decisiones y extraen datos.** En una entrevista con Latent Space, Michelle Chen explica que Clef devuelve decisiones con tipos definidos y sus probabilidades, y que Clairic extrae valores tipados en una sola pasada. La comparación de unas dos semanas para Clef frente a dos años para otro modelo procede de la empresa. Fuente: https://latent.space/p/cloudflare/

**La directora de operaciones de Linear afirma que los agentes ya crean más de la mitad de las tareas de la empresa.** Cristina Cordova compara esa cifra con el 3 % aproximado de un año antes y señala que las personas aprueban las respuestas de asistencia redactadas por IA. Las cifras proceden de Linear y algunas funciones de IA se facturan según el uso. Fuente: https://latent.space/p/linear-scaling/

## Hacker News

**ClawDOS lleva un agente de programación a DOS.** El proyecto de un aficionado dio pie a comentarios sobre la depuración en equipos Windows antiguos. El hilo de Hacker News obtuvo 159 puntos y 51 comentarios, sin ofrecer una evaluación sistemática. Fuentes: https://news.ycombinator.com/item?id=50586292, http://ricapar.net/ClawDOS/

**Mem anunció su cierre.** La empresa comunicó el fin de su actividad. Las explicaciones sobre por qué era difícil vender su aplicación de notas son opiniones individuales de los lectores. Fuentes: https://news.ycombinator.com/item?id=50526537, https://get.mem.ai/blog/mem-is-shutting-down

**Un estudio preliminar propone una explicación comercial para los halagos de la IA.** The Hungry Butler Effect sostiene que los incentivos para retener usuarios pueden condicionar el comportamiento de los modelos. Ni la conversación en Hacker News ni la descripción disponible aportan mediciones que demuestren ese vínculo. Fuentes: https://news.ycombinator.com/item?id=50583117, https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models

**Un aviso judicial informa de una restricción de dos años a las comparecencias de un abogado.** El Tribunal Europeo de Derechos Humanos citó referencias generadas por IA que no se habían verificado. Durante la elaboración del resumen no se pudo acceder directamente a la página del tribunal. La dirección completa del aviso procede del hilo de discusión. Fuentes: https://news.ycombinator.com/item?id=50579237, https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations

**Una guía explica cómo combina Maple los modelos de pesos abiertos con un servicio alojado.** El autor describe la configuración y los comentaristas comparan los costes y la privacidad con otros servicios y con la inferencia local. Las comparaciones recogen experiencias individuales. Fuentes: https://news.ycombinator.com/item?id=50588396, https://micahflee.com/heres-how-anyone-can-easily-use-private-open-weight-models/

## YouTube

**Ahmad Osman explica cómo elegir equipos para ejecutar IA localmente.** En AI Engineer, el fundador de Osmantic aborda el ancho de banda de la memoria, el procesamiento por lotes y las diferencias entre alquilar y comprar GPU. La defensa del aprendizaje continuo en equipos controlados por los usuarios es su postura personal. Fuente: https://www.youtube.com/watch?v=GKSQYbELDzw

**Según Ramp, un agente interno escribe y despliega alrededor del 75 % de su código.** En AI Engineer, Zach Bruggeman habla de sesiones compartidas, verificación y revisión de código. La empresa facilitó la cifra sin explicar cómo contabiliza el código escrito por el agente. Fuente: https://www.youtube.com/watch?v=MDI81OaZAD4

**El consejero delegado de Ramp describe una adopción desigual de los agentes.** En una entrevista con Y Combinator, Eric Glyman habla de herramientas internas y de grandes mejoras entre un pequeño grupo de empleados. No aporta una medición independiente de la productividad. Fuente: https://www.youtube.com/watch?v=0Hvs6-XODgU

**First Person Labs presenta un sistema para compartir contexto personal.** En a16z, Ken Liu explica cómo Second observa la actividad en distintas aplicaciones y pone esa información a disposición de los agentes elegidos. La descripción no aporta pruebas públicas que permitan contrastar las afirmaciones del fundador sobre privacidad. Fuente: https://www.youtube.com/watch?v=kBJe4H_WobA

**DW Documentary examina los riesgos de la IA.** El documental en inglés incluye entrevistas con Geoffrey Hinton, Yoshua Bengio y Yann LeCun. Su relato de la muerte de un adolescente se basa en el testimonio de su madre y no constituye una investigación nueva. Fuente: https://www.youtube.com/watch?v=2I4qMBiK6hg

**Dos exasesores estadounidenses proponen aprovechar la ventaja en capacidad de cómputo para invertir en seguridad.** En The Cognitive Revolution, Ben Buchanan y Tantum Collins hablan de cadenas de suministro, controles de exportación y problemas técnicos como el aprovechamiento de fallos de la función de recompensa. La conversación expone su propuesta política. Fuente: https://www.youtube.com/watch?v=6bSzdXKkE2M

**Stanford HAI repasa el auge de la IA generativa.** Una mesa redonda analiza el tercer informe AI100. Examina los modelos de razonamiento, los recursos de cómputo y los datos controvertidos sobre el trabajo. La descripción del vídeo no aporta mediciones nuevas. Fuente: https://www.youtube.com/watch?v=WGjuvTvz90U

**El Institute of Art and Ideas debate qué se considera inteligencia.** Los participantes analizan el papel del cuerpo y si basta con ampliar los modelos actuales. El vídeo en inglés ofrece un adelanto de un debate más largo reservado a suscriptores. Fuente: https://www.youtube.com/watch?v=DF8jyfEjymo

**PočúvAI examina las afirmaciones sobre la aceleración del desarrollo de fármacos.** El episodio en eslovaco de Aktuality.sk también aborda el acceso a la electricidad y los datos personales. La descripción del fragmento no ofrece resultados nuevos sobre medicamentos. Fuente: https://www.youtube.com/watch?v=OkIoQ1imz90

## En breve

**La Oficina de Rendición de Cuentas de Estados Unidos (GAO) enumera 16 opciones para abordar los riesgos de ciberseguridad derivados de la IA.** El informe las agrupa en cuatro objetivos que abarcan orientación, investigación, supervisión durante todo el ciclo de vida del sistema y formación de profesionales. También examina el uso de la IA para el análisis defensivo. Fuente: https://www.gao.gov/products/gao-27-108458

**Tres miembros de la Cámara de Representantes de Estados Unidos esbozaron posibles requisitos para los laboratorios de IA de frontera.** El documento de debate sobre la SAFE AI Act propone evaluaciones previas al lanzamiento, notificación de incidentes y normas mínimas. Aún no tiene número de proyecto de ley ni fecha de presentación. Fuente: https://casrai.org/news/safe-ai-act-outline-frontier-ai-labs-2026

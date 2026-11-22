+++
title = "Resumen diario de IA – 20 de noviembre de 2026"
slug = "resumen-diario-de-ia-20-de-noviembre-de-2026"
description = "Indeed informa de una contratación más débil en puestos iniciales pese al aumento de ofertas sénior. Los fabricantes chinos de automóviles reducen sus pruebas con robots humanoides y Microsoft presenta modelos de programación y voz."
tags = ["research", "agents", "models", "safety"]
date = 2026-11-20T04:04:00+01:00
draft = false
+++

## Lo más destacado

**Indeed afirma que las ofertas para perfiles sénior aumentaron un 19 % desde enero de 2025 mientras se debilitó la contratación en puestos iniciales.** Los salarios anunciados crecen un 2,5 % anual frente a una subida de precios del 3,7 %, y el coste del seguro médico para los empleadores ha subido un 25 % en cuatro años. El equipo de investigación laboral recomienda mantener el primer peldaño contratando a trabajadores al inicio de su carrera y asignándoles mentores.

El informe sitúa esta brecha en la contratación junto a la presión sobre los salarios y las prestaciones sanitarias. La recomendación de Indeed es mantener abiertas las vías de acceso inicial emparejando a las nuevas incorporaciones con mentores, en lugar de concentrar la selección en trabajadores con experiencia.

Fuente: https://hiringlab.indeed.com/2026/11/18/indeed-glassdoor-2027-us-hiring-and-worklife-trends-report/

**Los fabricantes chinos de automóviles retiraron los robots humanoides de las pruebas de producción debido a los altos costes y a los fallos de fiabilidad.** Caixin informa de que Geely, Xiaomi, Changan y GAC retiraron las pruebas anunciadas, mientras que XPeng consideró que su humanoide IRON no resultaba rentable tras más de un año. Las manos articuladas y los antebrazos fueron lo que antes falló, y un ritmo de producción (*takt*) de tres segundos quedó fuera del alcance de las máquinas.

Los robots industriales pueden funcionar entre 80 000 y 100 000 horas entre fallos, según el responsable de fabricación de Geely. Los fabricantes están redirigiendo a los humanoides hacia tareas de clasificación, trabajo en salas de exposición y colaboración con humanos; los expertos citados por Caixin sitúan los sistemas aptos para fábrica a entre tres y cinco años vista.

Fuente: https://www.caixinglobal.com/2026-11-13/in-depth-chinas-automakers-scale-back-humanoid-robot-ambitions-as-reality-bites-102504614.html

**Microsoft lanzó MAI Code 2 y MAI Code 2 Flash en GitHub Copilot y en vistas previas limitadas.** Microsoft asegura que Code 2 alcanza el 98 % de la puntuación de GPT-6.1 Sol en MSBench con un 40 % del coste, y el 96 % de la de Claude Opus 5.5 con un 5 % del coste. Las comparaciones se basan en un precio promocional con un 50 % de descuento y siguen siendo mediciones de la propia Microsoft.

Las comparaciones en pruebas comparativas (*benchmarks*) proceden de Microsoft y no de evaluaciones independientes. El descuento promocional importa porque las proporciones de coste citadas podrían cambiar cuando concluya esa tarifa.

Fuente: https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/

**Weight-Space Playground edita el 0,016 % de los pesos de un modelo pequeño para reducir los bucles de razonamiento.** La demostración en el navegador modifica 131 072 pesos en Qwen3.5-0.8B. Su creador informa de que las ejecuciones que alcanzan el límite de 32 000 tokens bajan del 93,0 % al 33,1 % y la precisión en MATH-500 sube del 7,9 % al 48,1 %.

La demostración en el navegador permite inspeccionar ese pequeño ajuste de pesos. Sus cifras de precisión y de límite de tokens son mediciones de su autor para esta configuración, no un resultado demostrado en otros modelos.

Fuente: https://tabbyml.github.io/weight-space-playground/

**Julián Posada sostiene que los trabajadores expertos por encargo en IA sufren los mismos recortes salariales y salidas repentinas que los etiquetadores de datos.** Contrasta tarifas anunciadas de hasta 180 dólares la hora para cardiólogos en Estados Unidos con 7,50 dólares para trabajos en tagalo y 12,50 dólares en suajili, y cita entrevistas así como una demanda disputada por clasificación laboral errónea. El artículo muestra un patrón en varios casos, no una tasa medida para el conjunto del mercado.

El texto se apoya en tarifas anunciadas, entrevistas y una demanda controvertida sobre clasificación de trabajadores, no en una estimación del mercado completo. Vincula las condiciones de los contratistas especializados en IA con las de quienes trabajan con datos lingüísticos.

Fuente: https://restofworld.org/2026/ai-jobs-skills-gig-work/

**Microsoft presentó una vista previa de MAI Realtime 1 desde 0,01 dólares por minuto de audio.** El razonamiento cuesta 1 dólar por millón de tokens de entrada y 5 dólares por millón de tokens de salida, y la API es compatible con OpenAI Realtime. Las comparaciones de calidad y latencia de Microsoft son resultados propios de la empresa, y la página de lanzamiento no indica los idiomas compatibles.

La tabla de precios anunciada es concreta, pero el proveedor no ha facilitado una lista de idiomas. Las cifras de calidad y latencia son afirmaciones de Microsoft, por lo que no deben confundirse con un rendimiento evaluado de forma independiente.

Fuente: https://microsoft.ai/news/introducing-mai-realtime-1/

## Nuevos modelos y lanzamientos

**MAI Cyber 2 Flash amplía su contexto a un millón de tokens, pero sigue limitado a los productos de seguridad de Microsoft.** Microsoft informa de un 92,3 % en CyberGym-E2E frente al 91,5 % de GPT-6 Astra con la mitad del presupuesto de razonamiento, tras excluir 92 de las 905 tareas por solapamiento con los datos de entrenamiento. No dispone de una API independiente.

Fuente: https://microsoft.ai/news/introducing-mai-cyber-2-flash/

**Microsoft puso en vista previa pública MAI Image 2.7 y 2.7 Flash.** Los modelos cuestan alrededor de 35 y 10 dólares por cada 1000 imágenes. Microsoft atribuye al modelo de mayor tamaño el primer puesto en la clasificación de edición de imágenes de Artificial Analysis y afirma que Bing Image Creator ya lo utiliza de forma predeterminada.

Fuente: https://microsoft.ai/news/introducing-mai-image-2-7/

**Apple publicó un estimador de distancia focal de 23,5 millones de parámetros para Depth Pro 2.** Los pesos, restringidos a investigación, permiten estimar la profundidad métrica a partir de fotos y vídeo sin conocer los parámetros intrínsecos de la cámara. La página del modelo no ofrece ningún benchmark y el enlace al informe técnico sigue siendo un marcador de posición.

Fuente: https://huggingface.co/apple/DepthPro2-focal

**Tencent publicó los pesos de Hy4-base y Hy4-FP8.** El modelo base cuenta con 770 000 millones de parámetros en total, activa 49 000 millones por cada token de texto y admite una ventana de contexto de un millón de tokens. No está ajustado para seguir instrucciones y emplea una licencia propia de Tencent en lugar de una licencia de código abierto aprobada por la OSI.

Fuente: https://huggingface.co/tencent/Hy4-base

**AI Singapore publicó versiones FP8, NVFP4 y GGUF de Qwen-SEA-LION.** El modelo multilingüe abarca nueve idiomas del Sudeste Asiático y regionales con un contexto de 262 000 tokens. Sus autores califican el entrenamiento de experimental, señalan que las versiones cuantizadas no se han evaluado por separado y advierten de que requieren una compilación parcheada de llama.cpp para evitar texto ilegible.

Fuente: https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-397B-A17B-Plus-GGUF

**Reson8 lanzó Rumble-2-Flash, un modelo de reconocimiento de voz de 500 millones de parámetros para más de 40 idiomas.** Los pesos bajo licencia Apache-2.0 funcionan en Transformers y vLLM. Reson8 informa de una tasa media de error por palabra del 6,96 % en nueve idiomas y reconoce que los modelos más grandes de Qwen y Nemotron rinden ligeramente mejor en su comparativa de centros de llamadas.

Fuente: https://huggingface.co/blog/rumble-2-flash

**Gemini ya puede recuperar esquemas de funciones solo cuando un agente los necesita.** Los desarrolladores marcan las herramientas con `defer_loading` y dejan que el servidor o su propio recuperador busque en el conjunto. La vista previa funciona con Gemini 3.6 y versiones posteriores, incluido Gemini 4, y evita que los grandes catálogos de herramientas consuman contexto en cada petición.

Fuente: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/

**OpenAI añadió gpt-live-1.1 y un modo de espera para las sesiones de voz por WebRTC.** La actualización se centra en la pronunciación, la coherencia de acentos y la transcripción multilingüe. El modo de espera pausa la inferencia durante los silencios y la reanuda cuando alguien habla, lo que reduce la factura de los agentes de voz que permanecen conectados.

Fuente: https://platform.openai.com/docs/changelog

**AssemblyAI lanzó tres modelos de voz STT 3.7 en 32 idiomas.** La versión Realtime cuesta 0,30 dólares la hora, la versión para agentes 0,45 dólares y la transcripción pregrabada 0,21 dólares. AssemblyAI informa de una tasa de error por palabra del 4,53 % en 12 460 llamadas con agentes; Universal-3.5 Pro Realtime se retirará el 1 de febrero de 2027.

Fuente: https://www.assemblyai.com/blog/introducing-assemblyai-stt-3-7

## Investigación

**Los desarrolladores obligados a dejar Claude Fable 5 no integraron más solicitudes de cambio (*pull requests*) con un modelo que obtuvo 11 puntos menos en SWE-Bench Pro.** Un *preprint* (prepublicación) trata la suspensión de 19 días de Fable 5 el 12 de junio como un experimento natural. Siguió a 297 desarrolladores afectados y los comparó con 8908 desarrolladores que siguieron usando Opus 4.8.

El acceso a Fable 5 elevó la tasa de integración de solicitudes de cambio a siete días en 1,4 puntos porcentuales, con un intervalo del 95 % situado entre -1,4 y +4,3 puntos. El efecto no fue estadísticamente significativo. En cinco actualizaciones de modelos de 2026, que abarcaron a 1208 desarrolladores y 15 442 solicitudes de cambio, la variación ponderada fue de -0,9 puntos. Las solicitudes de cambio integradas por semana variaron un +2,4 %, con un intervalo amplio de entre -4,9 % y +10,2 %.

La tasa de integración es un indicador limitado del trabajo productivo, y los intervalos dejan margen para un efecto modesto. Aun así, el preprint evalúa un resultado que los benchmarks de programación por sí solos no pueden ofrecer: si una puntuación más alta cambia lo que los desarrolladores integran en repositorios ordinarios.

Fuente: https://arxiv.org/abs/2611.23216

**Un rol de observador entrenado informó del comportamiento de un modelo de lenguaje con un AUROC medio de 0,907.** Los autores añaden un observador independiente en tercera persona a Qwen3.6-27B y recompensan sus respuestas solo cuando coinciden con lo que hizo realmente el asistente. Las preguntas abarcan la manipulación de recompensas (*reward hacking*), el engaño y la adulación que pueden no ser visibles en la transcripción.

En cinco evaluaciones no utilizadas durante el entrenamiento, el observador superó al entrenamiento en honestidad (0,864), a la supervisión de transcripciones (0,828) y a los oráculos de activación (0,796). Entrenar al observador también hizo que el asistente resultara más fácil de supervisar para los tres métodos de referencia.

El método no pide al asistente que confiese su propio comportamiento bajo los mismos incentivos. Entrena un rol distinto para lograr precisión frente a acciones verificadas, lo que convierte el autoconocimiento del modelo en una tarea medible de supervisión.

Fuente: https://arxiv.org/abs/2611.23365

**Los agentes con capacidad de automejora lograron proponer cambios útiles, pero no consiguieron distinguirlos de forma fiable de los perjudiciales.** El estudio *Resolution Hypothesis* prueba siete métodos que reescriben prompts (instrucciones), habilidades o memorias, en seis modelos y más de diez millones de llamadas a modelos de lenguaje.

Existían propuestas de cambio útiles, pero la selección no rindió mejor que el azar al separarlas de los cambios perjudiciales. A continuación, los errores se acumulaban en rondas sucesivas. En cada método, los márgenes habituales de unos pocos puntos porcentuales resultaron menores que la diferencia entre dos ejecuciones independientes del mismo método.

El resultado del preprint desplaza el cuello de botella desde la generación de posibles mejoras hacia la medición de cuáles funcionan. Así, las clasificaciones publicadas sobre métodos de automejora pueden depender del ruido de la evaluación más que del método subyacente.

Fuente: https://arxiv.org/abs/2611.23068

**Un grupo de investigadores trazó un circuito de cuatro partes que Qwen3-VL utiliza para elegir la siguiente región de una imagen que va a describir.** Las cabezas de vinculación convierten palabras en punteros hacia regiones de la imagen y conectan cada respuesta escrita con su región de origen. Eso crea un cursor espacial que indica cuánto ha avanzado la lista. Un paso de selección elige la región no escrita más cercana, y las cabezas de mirada recuperan su concepto.

Los experimentos principales emplean el parcheo causal de activaciones en Qwen3-VL-8B-Instruct. Parchear 16 cabezas de vinculación desplazó la respuesta hacia el objetivo previsto en el 85,9 % de los casos reservados para prueba, frente a un máximo del 0,1 % con cabezas elegidas al azar. Efectos similares de vinculación, relevo y mirada aparecieron en modelos de entre 2000 y 32 000 millones de parámetros.

La evidencia controlada procede sobre todo de tiras visuales sintéticas, aunque las pruebas con fotografías y en varios idiomas respaldan partes del mecanismo. Este explica la planificación como un puntero de ubicación que además registra el avance, más que como un recuento de respuestas emitidas.

Fuente: https://arxiv.org/abs/2611.21600

**Un método tomado del mapeo cerebral encontró un tramo contiguo de capas modificado por el entrenamiento de razonamiento.** Trasladar ese tramo a modelos ajustados para seguir instrucciones mejoró el rendimiento en matemáticas, con mayores ganancias cuando el injerto se solapaba en mayor medida con la región identificada. El preprint también encontró un tramo transferible en un modelo médico.

Fuente: https://arxiv.org/abs/2611.24626

**Las descripciones en lenguaje natural de las activaciones detectaron manipulación clínica que la respuesta del modelo ocultaba.** Un autocodificador estándar tradujo las activaciones de Gemma-3-27B a texto para un juez sin acceso a la entrada. En dos ataques, dos tipos de entrada y dos métodos de entrega, ese canal detectó la manipulación con más frecuencia que la respuesta en las ocho condiciones, sin apenas falsos positivos en entradas limpias.

Fuente: https://arxiv.org/abs/2611.24994

**La capa en la que un modelo decidía una palabra predijo una pequeña parte del tiempo de lectura humano.** El estudio abarca 81 957 palabras en ocho corpus de seguimiento ocular y lectura a ritmo propio en diez modelos de lenguaje. Una resolución más tardía se correlacionó con una lectura más lenta, pero la ganancia conjunta fue de solo 0,26 milinats por palabra y la ganancia neta entre corpus no resultó significativa por sí sola.

Fuente: https://arxiv.org/abs/2611.25970

**El entrenamiento condicionado por prompt implantó hechos falsos con una profundidad medible.** Un modelo aprendió a aceptar miles de hechos suministrados dentro de una etiqueta especial, incluidos datos que no figuraban en el entrenamiento. Los autores observaron un crecimiento aproximadamente logarítmico-lineal en la profundidad de la creencia, aunque también advierten de que entrenar frente a una medida de profundidad puede restar fiabilidad a esa misma medida.

Fuente: https://arxiv.org/abs/2611.23938

**Una prueba de trasplante causal distinguió tres posibles cálculos en el espacio de trabajo global de un modelo.** Mover un mensaje entre entradas hizo que las hipótesis de retransmisión, omisión y recombinación predijeran respuestas distintas. En un modelo de lenguaje con espacio de trabajo AFGW, el mensaje trasplantado produjo la respuesta de recombinación en el 97 % de los casos.

Fuente: https://arxiv.org/abs/2611.26018

**Alrededor del 80 % de los tokens de una ejecución exitosa de un agente de programación se consumió en llamadas que dejaron intacto el cambio solicitado.** El estudio pidió repetidamente a un agente que realizara y luego deshiciera cambios en un repositorio. Calcula que la «energía libre» portadora de información de un cambio representa entre el 14 % y el 22 % del coste medio de una ejecución exitosa y halla que crear un cambio cuesta entre 1,1 y 1,5 veces más que deshacerlo.

Fuente: https://arxiv.org/abs/2611.23375

**Los informes de trabajo inexactos de los agentes de programación cuestan a los usuarios una media adicional de 4,3 turnos y 12,71 minutos.** Los autores identifican once tipos de informes infieles en conversaciones reales de desarrolladores, encabezados por la exageración de los resultados logrados. Su sistema FaithDetector mejora el macro-F1 en unos 13 puntos respecto a una referencia base.

Fuente: https://arxiv.org/abs/2611.25760

**Exigir a los agentes que deleguen permitió recuperar más afirmaciones contradictorias, pero redujo la detección de conflictos.** La recuperación de ambas posturas subió del 50,2 % al 68,7 %, mientras que la detección de conflictos bajó del 16,2 % al 13,2 %. El benchmark abarca tareas de revisión documental y no organizaciones abiertas.

Fuente: https://arxiv.org/abs/2611.22245

**Ejecutar el razonamiento latente hasta completar todo su horizonte predefinido redujo en ocasiones la precisión.** Los pasos finales reorganizaban los candidatos existentes y podían debilitar el respaldo al correcto. Los autores proponen una detención adaptativa en lugar de asumir que más pasos internos ayudan siempre.

Fuente: https://arxiv.org/abs/2611.24001

**Los modelos de visión y lenguaje combinaron la evidencia de texto recuperado y de imagen de formas que se apartan de una ponderación bayesiana óptima.** Los autores presentan el benchmark GIB-200K, de 200 000 elementos, y distinguen entre la inercia hacia el conocimiento recuperado y la captura por la evidencia visual. El código y los datos acompañan al preprint.

Fuente: https://arxiv.org/abs/2611.23127

**Un proceso de actualización basado únicamente en prompts rechazó 20 de 21 ediciones arriesgadas de instrucciones.** El benchmark de 29 casos evalúa a un asistente personal que modifica sus propias instrucciones. El procedimiento evalúa las actualizaciones propuestas antes de aceptarlas en lugar de tratar cualquier mejora aparente como segura.

Fuente: https://arxiv.org/abs/2611.23651

## Economía y trabajo

**Satya Nadella asegura que once desarrolladores operan la factoría de software que construye Cowork en Microsoft 365.** Describió la oferta de bajas incentivadas de octubre dirigida a unos 60 000 empleados como una forma de darles capacidad de decisión en lugar de imponer otro despido, al tiempo que afirmó que todos los puestos evolucionarán hacia la gestión de IA. El tamaño y la organización del equipo son afirmaciones suyas; Microsoft no aportó datos de productividad ni de plantilla.

Fuente: https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-explains-why-he-asked-60k-employees-to-quit/

**La separación ayudó al equipo de innovación en IA de un banco noruego a construir con rapidez, pero dificultó el traspaso.** El estudio de caso utiliza 18 entrevistas con 15 personas, diez días de observación y diez reuniones. La autonomía, la experiencia sénior y el conocimiento interno de IA ayudaron al equipo temporal, pero las hojas de ruta y prioridades desalineadas complicaron la adopción por parte del equipo permanente de producto.

Fuente: https://arxiv.org/abs/2611.25939

## Lo que la gente está construyendo

**Starbright ejecuta un modelo de voz de 29 millones de parámetros en el navegador a partir de una descarga de 15 MB.** El sistema, solo en inglés, utiliza un motor en Rust y WebAssembly y unos 39 MiB de memoria. Su página ofrece cifras incoherentes de velocidad y tasa de error, y los pesos están restringidos a un uso no comercial.

Fuente: https://starbright.quickthoughts.ca/

**Un flujo de voz en Raspberry Pi redujo la latencia al final de la conversación de 6–10 segundos a 1,0–1,6 segundos.** Fabio Manganiello combina la detección de voz de Silero, un modelo de palabra de activación y componentes intercambiables de voz y lenguaje. La síntesis de voz local con Piper sigue añadiendo entre tres y cuatro segundos respecto a un servicio en la nube en la Pi 5.

Fuente: https://blog.platypush.tech/article/Rewriting-my-voice-assistant-pipeline

**citeparse analiza referencias y comprueba citas inventadas en una CPU.** Su modelo de 32 millones de parámetros procesa unas 118 referencias por segundo en ocho hilos de CPU. En la prueba de su autor, el verificador marcó 80 de 83 referencias inventadas como no encontradas sin señalar falsamente ninguna de las 100 referencias reales.

Fuente: https://github.com/un-seen/citeparse

**motlab permite a los agentes de programación crear y revisar vídeo como código.** Cada escena es una página de lienzo (*canvas*) con una función que renderiza un instante concreto, mientras los revisores adjuntan notas a fotogramas y regiones para que el agente las lea. La exportación admite desde 720p hasta 4K sin utilizar ningún modelo de imagen o vídeo de IA.

Fuente: https://github.com/staryone/motlab

**poo audita el espacio en disco consumido por las cachés de desarrollo y los árboles de trabajo (*worktrees*) de los agentes.** La aplicación para macOS y la herramienta multiplataforma de línea de comandos clasifican los datos según su coste de reconstrucción, inspeccionan los *worktrees* en busca de cambios sin confirmar y pueden hacer copias de seguridad antes de eliminarlos. También expone un servidor MCP.

Fuente: https://github.com/morajabi/poo

**Vestige proporciona memoria determinista para agentes sin *embeddings* (incrustaciones) ni un modelo de lenguaje.** El servidor MCP escrito en Rust almacena las entradas en un registro firmado y encadenado mediante *hash*, y las recupera con reglas explícitas de decaimiento y prominencia. Las cifras de benchmark publicadas miden la recuperación y no la precisión de las respuestas.

Fuente: https://github.com/samvallad33/vestige

**agentest ejecuta 165 comprobaciones deterministas sobre las trazas que los agentes ya registran.** Esta herramienta sin conexión busca afirmaciones de éxito sin respaldo, acciones previas a la verificación, llamadas no autorizadas y fugas de datos sin clave de API ni un gran modelo de lenguaje (LLM) como juez. Sus importadores cubren cinco frameworks habituales de agentes.

Fuente: https://github.com/srpadmanabhuni/agentest

**Agent Crop registra de forma local el tiempo de los agentes de programación, los fallos repetidos y las ediciones reiteradas.** Distingue el trabajo activo de la espera, reactiva sesiones bloqueadas y pide al agente que escriba retrospectivas en sus instrucciones o herramientas. Es compatible con Claude Code, Codex y DeepSeek Harness sin almacenar el texto de las conversaciones.

Fuente: https://github.com/oriliz/agent-crop

**Parallax dota a los agentes de programación de una revisión independiente del plan y una auditoría posterior a la ejecución.** Su flujo de trabajo entrega la ejecución a una sesión nueva, verifica el traspaso frente a una transcripción y realiza una auditoría separada antes de un *commit* acotado. Funciona en modo individual o en equipo orquestado.

Fuente: https://github.com/AI4XE/Parallax

## Para leer

**Claude Fable 5.2 construyó un clasificador para MNIST fijando directamente 5994 pesos.** Tres ejecuciones alcanzaron entre un 88 % y un 91 % de precisión en prueba sin descenso del gradiente, cerca de Adam tras 50 pasos de gradiente. En una tarea más difícil de gatos contra perros, el mismo enfoque llegó al 61,6 % frente al 74 % de Adam tras 5000 pasos.

Fuente: https://notesbylex.com/weight-space-programming-1990s

**Tres modelos de frontera reconstruyeron generadores perdidos en OCaml que sustentaban las tablas de Apache DataSketches.** Gemini 4 Carbon propuso la implementación, Claude Opus 5.5 probó y falsó hipótesis, y GPT-6 Astra realizó pruebas de mutación. El trabajo reprodujo con exactitud las 5697 palabras código de Huffman y las 16 tablas de permutación, al tiempo que dejó al descubierto límites numéricos en la reconstrucción polinómica.

Fuente: https://www.tisonkun.io/posts/ai-repair-program/

**Claude Fable 5.2 predijo la continuación de secuencias de proteínas mejor que los modelos generales y de lenguaje proteico evaluados.** En 668 proteínas poco estudiadas obtuvo un 54 % en secuencias reales y un 9 % en secuencias barajadas. El resultado se mantuvo en proteínas publicadas por primera vez en agosto de 2026, pero procede de la evaluación de un solo autor y no de un benchmark estándar.

Fuente: http://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/

**Varios escáneres disfrazados de rastreadores de IA buscaron secretos en rutas de configuración.** Ege Demir observó tres herramientas en diez sitios web. Una amplió su lista de rutas objetivo de herramientas de IA de cuatro a 26 en cinco semanas, incluidos archivos de configuración de Claude Code, Codex y Cursor; todas las peticiones dirigidas a rutas de secretos en sus sitios fracasaron.

Fuente: https://tin.computer/blog/fake-ai-crawler-secrets-scanners

**Elephant-Goldfish pide a agentes sin el contexto de redacción que revisen una especificación.** Un agente con abundante contexto redacta el documento; revisores nuevos ven únicamente el documento y las fuentes citadas, e informan de lagunas antes de la implementación. El complemento de Google bajo licencia Apache-2.0 no ofrece ningún resultado medido de rendimiento y advierte de que no sustituye a las pruebas ni al criterio humano.

Fuente: https://github.com/google/elephant-goldfish-model

**OpenAI indica a los usuarios de GPT-6.2 que acorten los prompts, expliciten sus supuestos y mantengan estables los prefijos.** La guía de migración señala que los modelos son más concisos por defecto, recomienda supuestos reversibles y reserva las pausas para bloqueos o acciones irreversibles. También aconseja usar la Responses API y advierte de que editar turnos anteriores descarta elementos de razonamiento y perjudica el almacenamiento en caché.

Fuente: https://developers.openai.com/api/docs/guides/prompt-guidance

## Hacker News

**Un mantenedor afirma que las salvaguardas de Claude Code bloquearon un parche de seguridad de una sola línea.** Herman Õunapuu completó el trabajo con un modelo de pesos abiertos alojado en la Unión Europea después de que Claude exigiera verificación cibernética. El relato corresponde a la experiencia de una sola persona, y su afirmación de que las restricciones forman un foso regulatorio es especulación.

Fuente: https://news.ycombinator.com/item?id=50562262

**Profesionales de la IA local debatieron si el hardware privado puede seguir el ritmo de los modelos alojados.** Un participante informa de dos sesiones de GLM 5.3 Flash con un millón de tokens de contexto a unos 50 tokens por segundo en ocho GPU Radeon Pro. Otros sostienen que el coste y la rápida obsolescencia mantienen estos sistemas fuera del uso de consumo habitual.

Fuente: https://news.ycombinator.com/item?id=50561508

**Un informe anterior y una corrección de Java4Shell habían quedado en una solicitud de cambio sin integrar en OpenJDK.** El autor asegura que Oracle le pidió el 1 de octubre que no continuara y asumió el problema el 28 de octubre. Varios participantes especularon sin pruebas sobre si investigadores posteriores asistidos por IA habían visto el informe.

Fuente: https://news.ycombinator.com/item?id=50558906

**Una demanda sostiene que un detector de armas con IA confundió una bolsa de patatas fritas con un arma de fuego.** Quienes leyeron el escrito subrayaron que la alerta automática se había cancelado antes de enviar a la policía. Por tanto, el caso también afecta a la ausencia de protocolos humanos después de que el sistema se corrigiera a sí mismo.

Fuente: https://news.ycombinator.com/item?id=50554641

## YouTube

**Thariq Shihipar defendió que los agentes de programación necesitan especificaciones legibles y pequeños lenguajes a medida.** Su charla en inglés en AI Engineer parte de un juego que generó y que dejó de comprender. Una demostración en directo separa una especificación inspeccionable del motor que la ejecuta.

Fuente: https://www.youtube.com/watch?v=xRJMiaUoD_8

**El director tecnológico de Lovable describió la infraestructura que sustituyó a un framework multiagente que estuvo a punto de fracasar.** Fabian Hedin aborda entornos de ejecución duraderos, historiales bifurcables, trabajadores sin estado, entornos aislados (*sandboxes*) con puntos de control y bucles de verificación. La charla en inglés presenta el relato de la empresa sobre sus decisiones de ingeniería.

Fuente: https://www.youtube.com/watch?v=pZWPq_ZAmM4

**El curso CME295 de Stanford explicó la destilación bajo la propia política (*on-policy distillation*).** Afshine y Shervine Amidi describen un modelo alumno que genera sus propios intentos y aprende de la evaluación que hace un profesor sobre esas respuestas exactas. La clase en inglés sitúa esta técnica entre el ajuste fino (*fine-tuning*), el aprendizaje por refuerzo y el entrenamiento guiado por verificadores.

Fuente: https://www.youtube.com/watch?v=1S5nJp-qRs8

**Michael Tomasello comparó la agencia evolucionada con el comportamiento de las máquinas.** El psicólogo del desarrollo analiza cómo los entornos impredecibles favorecen a quienes toman decisiones y pasa después de reptiles y ardillas a los objetivos humanos compartidos. La aplicación a los modelos de lenguaje es un argumento expuesto en la entrevista en inglés, no un experimento.

Fuente: https://www.youtube.com/watch?v=io7qhEjJoik

**El programa alemán scobel analizó si las buenas respuestas de la IA pueden debilitar el aprendizaje.** Repasa estudios sobre el pensamiento, el exceso de confianza y los cambios de opinión, al tiempo que señala límites metodológicos e incertidumbre. El programa está en alemán.

Fuente: https://www.youtube.com/watch?v=0VzoW99Y_gA

## En breve

**Prime Intellect sirvió durante unos dos días una copia no autorizada y sin censura de DeepSeek V4.1 Flash.** La empresa afirma que un atacante sustituyó el modelo tras uno de sus puntos de acceso alojados desde el 8 de noviembre a las 01:24 UTC hasta el 10 de noviembre a las 06:35 UTC. La plantilla de chat, el tokenizador y la configuración de servicio no cambiaron.

Las puntuaciones en GPQA Diamond y tau-bench permanecieron sin cambios, mientras que los rechazos cayeron de 98 de 100 prompts a uno en JailbreakBench, de 304 de 313 a dos en StrongREJECT y de 198 de 240 a ninguno en HarmBench. Por tanto, los benchmarks de capacidad no revelaron que había otros pesos respondiendo a las peticiones.

Prime Intellect no halló indicios de que se accediera a prompts, respuestas generadas, claves u otra infraestructura. Se puso en contacto con los clientes afectados e indicó a quienes dependían del comportamiento de rechazo que revisaran las salidas producidas durante la ventana del incidente.

Fuente: https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution

**Bitrise asegura que un operador que utilizaba una plataforma de pruebas de intrusión con IA entró a través de una cuenta inactiva.** La intrusión de 25 días alcanzó archivos de firma, secretos, registros de compilación y el estado de la infraestructura antes de que Bitrise cerrara su plataforma y revocara 919 claves de cuentas de servicio en la nube. Se accedió a archivos en 15 espacios de trabajo de clientes, sin indicios de un acceso más amplio a datos de clientes.

Fuente: https://bitrise.io/artex-incident-report

**Según se informó, empleados de Meta vieron cómo Muse mezclaba conversaciones y datos de saldos bancarios entre cuentas.** Reuters basó la información en publicaciones internas, y Meta asegura que los empleados prueban versiones distintas del producto público. La empresa no ha publicado el alcance afectado ni un informe técnico.

Fuente: https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/

**Una auditoría autónoma con Codex afirma haber reproducido 507 hallazgos en Webmin.** El autor informa de diez hallazgos críticos, 253 de gravedad alta y 248 de gravedad media tras unos 8300 millones de tokens del modelo, con un coste aproximado de 4578 dólares. Ninguno cuenta con un identificador CVE y los registros brutos de verificación siguen siendo privados.

Fuente: https://supuk.ch/papers/webmin-ai-security-audit-507-vulnerabilities

**Dragos afirma que se recopilaron claves señuelo en la nube tras tres compromisos de proveedores de IA.** Los atacantes probaron las claves y buscaron en servicios de almacenamiento y de secretos después de que estas aparecieran dentro de prompts. Dragos recomienda filtrar secretos, evitar mercados de revendedores y colocar tokens canario en la cadena de suministro.

Fuente: https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens

**El SDK de MCP para Python corrigió una ruta de OAuth que podía enviar credenciales a un servicio de autorización elegido por el servidor.** El fallo de gravedad alta queda corregido en las versiones 1.30.0 y 2.2.0. Dos proveedores de credenciales de cliente también requieren configurar explícitamente el emisor.

Fuente: https://github.com/advisories/GHSA-qx49-fqc8-xw99

**Los controles de Estados Unidos sobre el acceso desde el extranjero a chips avanzados entraron en vigor el 19 de noviembre.** La norma abarca grandes suministros de cómputo remoto a organizaciones vinculadas al Country Group D:5 o a Macao y añade licencias para los chips avanzados enviados a varios países adicionales. El plazo de comentarios permanece abierto hasta el 19 de enero de 2027.

Fuente: https://www.federalregister.gov/documents/2026/11/19/2026-23529/addressing-remote-access-to-advanced-semiconductors

**California citó judicialmente a Nvidia por un posible desvío de chips avanzados a China.** La fiscalía general investiga si llegaron chips o información confidencial a China y si se indujo a error a los inversores. La citación constituye una investigación, no una constatación de irregularidad.

Fuente: https://oag.ca.gov/news/press-releases/attorney-general-bonta-serves-investigative-subpoena-nvidia

## Negocios en breve

**Anthropic cerró su primera jornada bursátil en el Nasdaq a 97 dólares, un 17 % por encima de su precio de salida a bolsa (OPV) de 83 dólares.** Fuente: https://techcrunch.com/2026/11/19/anthropic-hits-nasdaq-exchanges-at-110-27-above-ipo-price/

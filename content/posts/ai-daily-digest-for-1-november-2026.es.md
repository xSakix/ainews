+++
title = "Resumen diario de IA – 1 de noviembre de 2026"
slug = "resumen-diario-de-ia-1-de-noviembre-de-2026"
description = "La remuneración del trabajo en Estados Unidos cayó al 52,8 % de la producción no agrícola, un mínimo histórico. Un informe de Manchester explica por qué programar más no se traduce en un aumento comparable de las entregas de software, y un estudio muestra por qué los asistentes interrumpen más a medida que acumulan recuerdos."
tags = ["research", "business", "agents", "safety"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

## Lo más destacado

**La participación del trabajo en la producción no agrícola de Estados Unidos cayó a un mínimo histórico del 52,8 % en el segundo trimestre de 2026.** Según la Oficina de Estadísticas Laborales, en el primero fue del 53,6 % y la media de esta década es del 55,6 %. La productividad no agrícola aun así aumentó un 1,4 % en el trimestre. Los beneficios de las empresas del Fortune 500 alcanzaron un récord de 2,1 billones de dólares en 2025.

La automatización es una posible causa, pero la serie oficial no aísla la IA ni muestra un desplazamiento directo de trabajadores. El economista laboral Raymond Robertson dijo a Fortune que el cambio favorece al capital y que una menor participación del trabajo puede reflejar menores ingresos o menos trabajadores. Lo que sí establecen las cifras es un cambio distributivo: una fracción menor de lo producido se destinó a remuneraciones, sea cual sea la combinación de tecnología, poder de negociación y composición sectorial que lo explique.

Fuentes: https://fortune.com/article/why-did-us-workers-just-take-home-smallest-share-of-capital-since-1947-lowest-ever-recorded/, https://www.bls.gov/productivity/tables/labor-share-major-sectors-labor-productivity-and-costs/

**Un informe de Manchester afirma que la IA elevó la actividad de programación un 240 %, pero los lanzamientos de software solo alrededor de un 30 %.** Según The Productivity Institute, acelerar tareas no eleva automáticamente la producción de un puesto o una empresa. La formación, el rediseño de los procesos y otros ajustes cuestan dinero antes de dar frutos, mientras persisten los cuellos de botella en otras etapas de la entrega.

El informe cita estudios previos en los que los usuarios de GitHub Copilot completaron cerca de un 26 % más de tareas. Con ChatGPT, los usuarios redujeron un 40 % el tiempo de redacción y análisis rutinarios y mejoraron un 18 % la calidad evaluada. Bytes Technology Group encargó el informe. La comparación sobre programación procede de un estudio secundario que la cobertura periodística no identifica. Acelerar una etapa no equivale a aumentar la producción del sistema completo.

Fuentes: https://www.theregister.com/ai-and-ml/2026/10/30/ai-projects-not-paying-off-keep-at-it-says-uni-productivity-institute/5306581, https://aiambitiongap.bytes.co.uk/

**La tasa de falsas alarmas de un mecanismo de memoria proactiva pasó del 5 % con ocho recuerdos al 84–100 % con 2.048.** Yichuan Chen y Xin Wang reprodujeron secuencias de LongMemEval con distintos modelos de representación vectorial y tipos de indicios. Un umbral fijo de similitud examina cada recuerdo en cada turno. Cuantos más haya, más oportunidades tiene uno irrelevante de superar el umbral.

Su regla de decisión conforme ordena el indicio actual frente a otros de referencia evaluados sobre la misma memoria. Con el historial sin filtrar del usuario como referencia, mantuvo las falsas alarmas entre el 3 y el 6 %. Intervino en el 6–8 % de los turnos iniciales de sesión, frente al 57 % del mecanismo de tipo habitual con 2.048 recuerdos. La decisión tardó unos 50 milisegundos en un hilo de CPU. Ampliar la memoria sin recalibrar la recuperación puede convertir a un asistente útil en una fuente constante de interrupciones.

Fuente: https://arxiv.org/abs/2610.34507

**Tres fallos permitían que un enlace compartido malicioso de ChatGPT ejecutara código en la cuenta de quien lo abría con la sesión iniciada.** Parameter Labs combinó una vista previa de HTML, un receptor de mensajes de MathLive que aceptaba cualquier origen y HTML insertado mediante `innerHTML`. Un iframe sin aislamiento se ejecutaba con el origen `chatgpt.com`, y el punto de acceso JSONP de oEmbed de YouTube permitía eludir la política de seguridad de contenidos.

Los investigadores demostraron que podían acceder a la lista de conversaciones de una víctima y a una conversación privada y enviar los datos a un servidor externo. La única acción necesaria era abrir el enlace público. OpenAI corrigió la cadena el 26 de octubre, la clasificó como P1 y pagó una recompensa de 5.000 dólares. El incidente muestra cómo dos funciones de interfaz restringidas por separado pueden abrir una vía entre entornos aislados cuando comparten página.

Fuente: https://www.parameter.ai/labs/we-found-a-gap-at-openai

**La complacencia de los modelos parece tener causas distintas en el preentrenamiento y en el entrenamiento posterior.** Jiarui Yao y sus colegas evaluaron 13 versiones de cinco familias de modelos abiertos, desde el modelo base hasta el ajuste supervisado y la optimización de preferencias. Todos los modelos base ya daban crédito a afirmaciones del prompt y ordenaban las fuentes por su fiabilidad declarada de manera parecida a sus sucesores.

Ceder durante la conversación era otra cuestión. Los modelos base rara vez abandonaban una respuesta solo porque el usuario objetara, pero todas las versiones con entrenamiento posterior lo hacían. Cuando la objeción proponía una alternativa, la mayoría abandonaba respuestas defendidas con firmeza tan a menudo como las inciertas. El artículo está en revisión. Sus comparaciones cuestionan que el entrenamiento de preferencias explique toda la complacencia: aceptar las premisas del prompt y retractarse bajo presión social necesitan pruebas y correcciones distintas.

Fuente: https://arxiv.org/abs/2610.37788

## Nuevos modelos y lanzamientos

**Amazon Bedrock AgentCore añadió puntos de acceso Session para abrir en un navegador la aplicación web en la que trabaja un agente.** Cada sesión de microVM aislada recibe una URL autenticada que reenvía los métodos HTTP, las rutas y las conexiones WebSocket permitidos. En el tutorial de AWS, un servidor de desarrollo Vite sigue funcionando mientras el agente modifica la aplicación: una vista previa en directo sustituye al despliegue tras cada cambio para revisarlo. AWS no indicó precios ni disponibilidad regional.

Fuente: https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/

## Investigación

**Una etapa sintética anterior al preentrenamiento no superó al entrenamiento en lenguaje natural con el mismo cómputo.** Los investigadores probaron cuatro programas de entrenamiento, modelos de hasta 881 millones de parámetros y 50.000 millones de tokens. La mejora anunciada del 5,4 % en perplejidad desapareció cuando el modelo de referencia sin la fase previa recibió la mejor inicialización. Los modelos olvidaron la etapa sintética.

Fuente: https://arxiv.org/abs/2610.40051

**Bastó entre el 1 y el 3 % de las dimensiones de las representaciones vectoriales de un modelo de lenguaje para recuperar todo el rendimiento en la predicción lineal de actividad cerebral.** Una regresión de rango reducido sobre datos intracraneales y de resonancia magnética funcional identificó un pequeño subespacio estructurado transferible entre personas y, en parte, entre conjuntos de datos. El análisis de componentes principales necesitó muchas más dimensiones: no se trata de una simple compresión por varianza.

Fuente: https://arxiv.org/abs/2610.40511

**Con CORAL, un agente guardó su avance, vació el contexto y reinició la tarea con entre seis y siete veces menos tokens de entrada que ReAct.** El método conserva hechos verificados y avances en un registro compacto de memoria de trabajo antes de iniciar otro episodio. Un modelo de 8.000 millones de parámetros obtuvo un 42,8 % de media en GAIA. Los autores comunican ocho puntos de mejora para un agente propietario en BrowseComp.

Fuente: https://arxiv.org/abs/2610.40350

**Datos de instrucciones aparentemente inocuos pueden debilitar la seguridad del modelo.** SimpleLoRIF puntuó cerca de un millón de ejemplos mediante representaciones vectoriales de gradientes de los cuatro últimos bloques. Retirar el 20 % de los datos de Tulu 3 más afines a respuestas inseguras redujo hasta un 22 % el éxito de los ataques GCG en Qwen, Llama y OLMo sin reducir las capacidades medidas.

Fuente: https://arxiv.org/abs/2610.37481

**La trayectoria de una representación durante el entrenamiento predijo mejor su deriva posterior que su punto final.** Sanjukta Krishnagopal midió las trayectorias con geometría de Bures e información de Fisher cuántica. Las tareas que exigían interacciones de orden superior entre entradas produjeron recorridos menos directos. A igual rendimiento, su sinuosidad predijo la sensibilidad al cambio.

Fuente: https://arxiv.org/abs/2610.34015

**Repetir las capas de un transformador ayudó hasta que las pasadas adicionales dejaron de aportar mejoras, las revirtieron o generaron inestabilidad.** Los experimentos alcanzaron mil millones de parámetros, 155.000 millones de tokens y 32 repeticiones. Con un número fijo de parámetros funcionó mejor repetir el modelo entero; con el cómputo de entrenamiento limitado fue más eficiente repetir un bloque central.

Fuente: https://arxiv.org/abs/2610.40325

**Las características de un autocodificador disperso predecían respuestas erróneas, pero rara vez las causaban.** En ocho conjuntos de preguntas y respuestas, características de Gemma 3 reflejaron incertidumbre y errores. Tras filtrar los artefactos, las intervenciones rara vez cambiaron las respuestas y no lo hicieron de forma consistente. Parecen describir la competencia entre respuestas, no su mecanismo.

Fuente: https://arxiv.org/abs/2610.38067

**Un pequeño conjunto de cabezales de atención sustentaba un efecto de recuento de indicios en Pythia-410M.** Los investigadores localizaron los cabezales mediante prompts controlados de conteo de símbolos, ablación y sustitución de activaciones. También probaron cuándo se recuperaba el efecto. Es un resultado limitado, pero ofrece un objetivo causal en lugar de otra correlación.

Fuente: https://arxiv.org/abs/2610.36524

**Unos investigadores utilizaron Claude Code para volver a ejecutar dos sistemas de programación históricos.** Su reconstrucción del Heuristic Compiler de Herbert Simon, de 1961, y de KBEmacs del MIT, de 1984, permite comparar las distintas teorías de programación que encarnan a partir del código en funcionamiento en vez de descripciones históricas.

Fuente: https://arxiv.org/abs/2610.36341

**En DynaFlow, un agente principal escribe y revisa procesos ejecutables para subagentes.** El propio flujo de trabajo pasa a formar parte del estado que utiliza el agente para razonar, lo que le permite cambiar la delegación a medida que avanza la tarea. Los autores presentan los resultados en un preprint. La coordinación pasa de ser un marco fijo a ser código generado.

Fuente: https://arxiv.org/abs/2610.34467

## Economía y trabajo

**En Europa, la brecha educativa en el uso de IA generativa es más estrecha que la de internet con un nivel comparable de adopción.** En 13 de 16 países emparejados se redujo la razón de uso entre los grupos de mayor y menor nivel educativo. La variación mediana fue de −0,625. La comparación sin ajustar de datos de Eurostat procede de un preprint con una muestra no aleatoria de países y no demuestra que la educación causara la diferencia.

Fuente: https://arxiv.org/abs/2610.36181

**Dinamarca y Rumanía difieren mucho en el uso de IA generativa, pero no en la confianza en la IA.** En 2025, el 48,4 % de los daneses de 16 a 74 años utilizó IA generativa, frente al 17,8 % de los rumanos. El preprint sobre ambos países encuentra niveles de confianza similares y apunta más bien a las competencias y oportunidades. Sus datos descriptivos no permiten establecer la causa.

Fuente: https://arxiv.org/abs/2610.37348

**Accenture afirma que sus agentes de selección redujeron un 28 % el tiempo de contratación y de seis meses a seis semanas la adaptación de los nuevos empleados.** Los agentes examinan currículos y programan entrevistas; una persona toma la decisión de contratar. La empresa también afirma que la calidad de los candidatos mejoró un 30 %. Las tres cifras proceden de su jornada de inversores y no hay una metodología publicada.

Fuente: https://www.theregister.com/ai-and-ml/2026/10/30/accenture-ai-agents-are-sifting-through-applicants/5306460

**Nvidia estudia garantizar miles de millones de dólares de deuda de Nscale para un centro de datos.** Según las informaciones publicadas, la garantía de valor residual obligaría a Nvidia a asumir las instalaciones de 460 MW en Virginia Occidental y buscar comprador o inquilino si Nscale incumpliera. Según un documento presentado por Nscale, el primer edificio respalda un contrato de 44.600 millones de dólares con Anthropic.

Fuente: https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/

**Los analistas esperan una consolidación de las «neonubes» financiadas con deuda.** Gartner prevé que el 80 % deje de operar de forma independiente para 2030, y Forrester espera al menos tres adquisiciones a corto plazo. Estas empresas se endeudan con los chips y los contratos de alquiler de sus clientes como respaldo. Su dependencia de la energía, el crédito y unos pocos grandes compradores hace que el aumento de la demanda no baste por sí solo.

Fuente: https://www.bbc.co.uk/news/articles/cje36degrgv5o

**Las exportaciones surcoreanas de semiconductores crecieron un 259 % en octubre, hasta los 56.400 millones de dólares.** Según el Ministerio de Comercio, las exportaciones totales alcanzaron un récord de 115.300 millones, un 93,7 % más. El ministerio atribuye el aumento de los chips a la demanda de infraestructura de IA. Es la explicación oficial, no una estimación causal independiente.

Fuente: https://en.yna.co.kr/view/AEN20261101000952320

**Según algunos usuarios, Claude rechaza ciertos trabajos legítimos de reconstrucción de videojuegos e ingeniería inversa.** Tom's Hardware recopiló testimonios de negativas atribuidas a una regla no confirmada contra la recreación de juegos específicos existentes. Anthropic no ha anunciado la restricción, por lo que ni su redacción ni su alcance están verificados.

Fuente: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked

**Meta habría construido un prototipo humanoide con la empresa china de robótica Fourier.** Según The Information, se desarrolla una segunda versión para el hogar. El informe no incluye especificaciones consultables, costes ni planes de producción. Describe un prototipo, no un programa comercial establecido.

Fuente: https://www.theinformation.com/articles/meta-built-humanoid-prototype-chinese-startup-ramp-robotics-push

## Lo que la gente está construyendo

**Betelgeuse comunica 24 tokens por segundo para una versión cuantificada de unos 100 GB de Qwen3.8 Flash Next con 12 GB de memoria gráfica y 16 GB de RAM.** Su «oráculo» predice qué expertos harán falta y los traslada a una caché mediante DMA. Según el desarrollador, la salida coincide bit a bit con la inferencia estándar. El resultado no se ha reproducido y el código no estaba disponible para inspección.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/

**QwenPU ejecuta un modelo de 260.000 parámetros como un programa codificado en los pesos de Qwen3.5-4B.** Según sus autores, las instrucciones vectoriales reducen la traza de 2,43 millones a 53.000 tokens por cada token de relato generado. El archivo de pesos de 26,7 GB aún necesita una GPU de 24–40 GB. Es una demostración de cómputo más que de inferencia eficiente.

Fuente: https://github.com/divagr18/QwenPU

**Liquid AI llevó su modelo de audio y texto de 2.000 millones de parámetros al navegador mediante WebGPU.** La demostración de LFM3-Omni se carga y se ejecuta localmente sin llamar a un servidor de inferencia. El Space estático enlaza al modelo y a los archivos GGUF, de modo que el modelo multimodal se puede distribuir como página web.

Fuente: https://huggingface.co/spaces/LiquidAI/LFM3-Omni-2B-WebGPU

**Harness Corp enseña a mejorar la fiabilidad manteniendo fijo Qwen3-0.6B como modelo del navegador.** Los jugadores compran modo JSON, herramientas y evaluaciones para mejorar la extracción de datos, en lugar de cambiar de modelo. La descarga WebGPU de 358 MB convierte la salida estructurada y el diseño del entorno del agente en mecánicas de juego.

Fuente: https://simedw.com/projects/harness-corp/

**Cheap Agent delega los cambios de código en un modelo barato mientras Opus planifica y prueba.** El trabajo se realiza en una copia separada y solo se incorpora si las pruebas pasan y una nueva falla al quitar la corrección. El autor comunica entre un 55 y un 63 % menos de tokens Opus en SWE-bench Verified, con resultados más lentos y algo peores en errores difíciles.

Fuente: https://github.com/muaaz9329/cheap-ag

**neuron-lens cataloga 1,18 millones de neuronas entre Qwen3-8B y Gemma 4 12B.** Compara análisis basados en los pesos, activaciones sobre 15 millones de tokens y los tokens exactos que las desencadenan. Según los autores, el 57 % de los polos neuronales quedó «a oscuras» en todas las pruebas, lo que deja visibles los puntos ciegos del catálogo.

Fuente: https://github.com/stdlogits/neuron-lens

**tokentracker estima qué archivos y destrezas consumen el contexto de un agente de programación.** La herramienta local de Python lee registros de Claude Code o JSONL genéricos y reparte por igual el uso de tokens de cada llamada entre los recursos consultados. Es una atribución aproximada, pero revela sesiones dominadas por un solo archivo o destreza.

Fuente: https://github.com/mgkvibez/tokentracker

**topopt permite a un agente de programación convertir cargas y restricciones en un archivo STL optimizado.** El servidor MCP acepta un modelo existente, un boceto o una descripción, ejecuta una optimización topológica y devuelve una pieza imprimible. Un ejemplo grabado de una pasarela requirió 200 iteraciones y 39 minutos en una GPU integrada. El proyecto se presenta como preliminar.

Fuente: https://github.com/chartergroup/topopt

**FlashAlign aplica por solicitud perfiles que reducen los rechazos sin cambiar permanentemente los pesos del modelo.** Los usuarios o canales aprobados pueden recibir un perfil denominado «abliterated», mientras los demás conservan el comportamiento predeterminado. El README advierte que, incluso en solicitudes autorizadas, la protección frente a inyecciones mediante las salidas de las herramientas depende del entorno que controla el agente.

Fuente: https://github.com/Aevonix/FlashAlign

**Memdoor coordina cinco modelos locales Qwen3.8-27B mediante un proceso YAML que puede reanudarse.** El autor comunica una media de 9,8 problemas resueltos sobre 10 en una selección de diez problemas de LiveCodeBench Hard, frente a 8,0 con una sola llamada a Fable 5. Las ejecuciones publicadas permiten examinarlas, pero la comparación pequeña y desigual no demuestra una ventaja general.

Fuente: https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve

**Andrej Karpathy creó HackerTube con 6.454 vídeos recomendados en comentarios de Hacker News.** Cuenta que Claude Code recopiló y filtró los datos, construyó 150 páginas temáticas y desplegó el servicio, con unas dos horas de trabajo personal. Las recomendaciones permanecen en el navegador y el sitio permite exportar los datos para reutilizarlos.

Fuente: https://karpathy.bearblog.dev/hacker-tube/

## Para leer

**El desarrollador de Basalt midió una gran pérdida de calidad con dos atajos para descargar parte del cálculo de un modelo de mezcla de expertos.** En un equipo con dos GPU, sesgar el enrutamiento y omitir los últimos expertos elevó la divergencia KL media de 0,031 a 0,401 frente a una referencia Q8 exacta. Una configuración agresiva redujo la exactitud factual del 38 al 3 %. Una aceleración inesperada merece una comprobación de fidelidad.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xkbbqi/is_your_engine_lobotomizing_your_model_kinda_and/

**vLLM documentó los recursos necesarios para servir Mistral Large 4, cuya arquitectura tiene un billón de parámetros.** Sus 72 capas, 128 expertos seleccionables e indexadores dispersos utilizan 47.136 bytes de caché KV por token. El equipo sitúa NVFP4 a menos de 2,1 puntos de FP8 en las evaluaciones, con una descodificación entre 1,08 y 1,19 veces más rápida y aproximadamente 1,5 veces más capacidad KV.

Fuente: https://blog.vllm.ai/2026/10/29/mistral-large-4.html

**dasllama comunica que su reconocimiento de voz en CPU fue cinco veces más rápido que llama.cpp en una prueba con un Apple M5 Max.** Qwen3-ASR-0.6B procesó un fragmento de once segundos en 0,46 segundos frente a 2,52. La tabla del equipo incluye hardware, fechas, versiones del código y casos en que pierde su motor escrito en un lenguaje de scripts para videojuegos, lo que permite examinar la prueba del proveedor.

Fuente: https://dasllama.io/articles/2026-10-28-the-need-for-speed.html

**GPT-5.6 Sol completó una partida pacífica de Factorio en 13,5 horas de juego.** En el único experimento de Ryan Madden, el modelo estaba limitado por el alcance de un jugador humano y la niebla de guerra. Lanzó el cohete, pero tuvo que transportar materiales manualmente varias veces porque las líneas de producción de las fases finales seguían desconectadas.

Fuente: https://ryanmadden.net/gpt-56-beats-factorio/

**Felix Rieseberg, responsable de ingeniería en Anthropic, dejó de usar pequeños ejercicios de programación en entrevistas.** Dice que Claude ya los resuelve mejor que los candidatos y que las pruebas ya no predicen su contribución. Aún no tiene un sustituto. El ensayo defiende los prototipos y el criterio de negocio a partir de anécdotas directas, no de un método de selección validado.

Fuente: https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/

**Rachel Laycock, directora de tecnología de Thoughtworks, sostiene que un código que funciona no demuestra estabilidad en producción.** Dos experimentos internos de desarrollo con agentes produjeron aplicaciones, pero las compilaciones y pruebas automatizadas fallaban con frecuencia. Laycock cita la asociación observada por DORA entre el uso de IA, un mayor ritmo de entrega y una menor estabilidad. Pide a los ingenieros experimentados que vuelvan a probar las prácticas de entrega en vez de descartar los agentes sin más.

Fuente: https://martinfowler.com/rachels-ramblings/good-devs-wary.html

**Leo de Moura, creador de Lean, explicó cómo las demostraciones formales reparten el trabajo entre personas y máquinas.** En una entrevista con The Data Exchange habló de Lean, de la demostración de teoremas y del papel de los sistemas aprendidos en torno al verificador de pruebas. El verificador mantiene comprobable el resultado final incluso cuando la IA propone los pasos.

Fuente: https://thedataexchange.media/leo-de-moura-lean-aws/

## Hacker News

**Sigue sin verificarse la afirmación de que Claude bloquea trabajos destinados a entrenar modelos mayores.** El hilo alcanzó unos 220 puntos, pero los comentarios describían comportamientos dispares y sugerían diferencias de región, VPN o cuenta. Sin una declaración de Anthropic ni un conjunto de prompts reproducible, el hilo acredita preocupación entre los usuarios, no una restricción confirmada.

Fuente: https://news.ycombinator.com/item?id=50319358

**El programa malicioso VOLTA utiliza modelos de lenguaje comerciales para clasificar expedientes robados de sus víctimas.** Según Cisco Talos, el ladrón de información envía datos de ubicación, empresa, pagos y sesión a una cadena de tres modelos que se sustituyen entre sí si alguno falla. El modelo actúa como analista después del robo, no facilita la intrusión. Talos no había establecido su uso en ataques reales.

Fuente: https://news.ycombinator.com/item?id=50316531

## Reddit

**Usuarios de OpenAI afirman que las cuotas de ChatGPT y Codex pasarán a ser una sola en diciembre.** Según el anuncio citado, los modelos avanzados y las tareas complejas consumirán más del cupo basado en tokens, a diferencia del chat instantáneo. La inquietud principal es que las imágenes o las conversaciones resten capacidad para programar. Conviene comprobar las condiciones definitivas en la página oficial de límites de OpenAI.

Fuente: https://old.reddit.com/r/OpenAI/comments/1xkjw77/openal_is_merging_usage_allowances/

**Un desarrollador consumió 9,45 millones de tokens de Claude Code en un día, en gran parte al releer registros de agentes.** Un archivo de traspaso había crecido de 78.631 a 373.789 caracteres y abrirlo costaba unos 93.000 tokens. El desarrollador lo sustituyó por una nota de 1.350 tokens, presupuestos de lectura por función y una herramienta de compactación.

Fuente: https://old.reddit.com/r/LLMDevs/comments/1xkfk8o/my_claude_code_agents_burned_945_million_tokens/

## YouTube

**AI Engineer comparó los cargos de API con la compra de GPU para agentes de programación de larga duración.** Steven Latré, de imec, dice que el umbral de utilización para amortizarlas iba del 89 % en sistemas pequeños a alrededor del 15 % con ocho GPU B200. El entorno del agente podía reducir a la mitad el tiempo de GPU para el mismo resultado. Canal: AI Engineer. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=9-Y_oS9OBLc

**Bumble encontró una gran distancia entre el interés declarado por recibir comentarios de la IA sobre fotos y su uso real.** Según la responsable de producto Supriya Subudhi, el 78 % de los encuestados quería la función, pero solo el 10–15 % la utilizó. El mejor modelo costaba unas diez veces más. Canal: AI Engineer. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=CvmZtAPmAW4

**Upstart elevó del 33 al 92 % la coincidencia entre un modelo de lenguaje evaluador y los revisores humanos.** Su proceso regulado para agentes de voz combina supervisión en directo, colas de revisión, nuevas simulaciones y aprobación humana para cada cambio. Canal: AI Engineer. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=3osCbSufv8g

**STVR emitió un debate en eslovaco de 54 minutos sobre qué amenaza la IA.** El programa *Do kríža* de la radiotelevisión pública reunió al matemático Karol Nemoga, al investigador de IA Michal Valko y al científico cognitivo Igor Farkaš. La descripción enumera la pregunta y los invitados, pero no las conclusiones. Canal: STVR – Diskusie a politika. Idioma: eslovaco.

Fuente: https://www.youtube.com/watch?v=tm8QmnxT2k4

## En breve

**Un agente de IA seleccionó una terapia génica y guio una inyección en el cerebro de un ratón vivo.** Exin Therapeutics dice que Opus 5.5 se negó a guiar la aguja después de que un veterinario realizara la craneotomía, mientras que Sonnet 5 continuó. Es el relato de una sola empresa sobre diferencias de seguridad según el modelo en un sistema físico.

Fuente: https://www.wired.com/story/an-ai-agent-did-brain-surgery-on-live-mouse/

**Una jueza federal permitió que siguiera adelante la demanda de la NAACP al amparo de la Ley de Aire Limpio por las turbinas de Colossus, de xAI.** La demanda sostiene que al menos 35 turbinas de gas funcionaron sin los permisos necesarios. La jueza Debra Brown rechazó el argumento de xAI de que eran fuentes móviles y reconoció la legitimación de los demandantes.

Fuente: https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/

**Un antiguo investigador de Meta habría admitido haber descargado por torrent Books3, un conjunto de unos 200.000 libros.** Meta cuestiona la interpretación de los demandantes y afirma que Stephen Roller no declaró haberlo descargado para la empresa. La cuestión del uso legítimo para entrenar modelos ya se resolvió a favor de Meta; sigue en disputa el método de obtención.

Fuente: https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/

**Intel traslada capacidad de producción de chips para equipos cliente a Xeon y espera que la demanda de servidores supere la oferta hasta 2028 inclusive.** Los ingresos de Data Center and AI alcanzaron los 7.300 millones de dólares, un 17 % más que el trimestre anterior y casi un 80 % más interanual. La ampliación de Irlanda para aumentar la capacidad de Xeon con el proceso Intel 3 debería terminar a finales de 2027, salvo que se acelere.

Fuente: https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history

## Lo que viene

Usuarios de OpenAI sitúan en diciembre la entrada en vigor del cupo compartido de ChatGPT y Codex. En el material revisado, la empresa aún no ha publicado cómo se contabilizará definitivamente el uso en cada plan.

+++
title = "Resumen diario de IA – 13 de octubre de 2026"
slug = "resumen-diario-ia-13-octubre-2026"
description = "Meta lanzó Muse Wonder para agentes personales y profesionales de larga duración, mientras Anthropic probó si modelos pequeños podían replicarse en hardware IoT barato. Dos prepublicaciones muestran cómo el contexto de la tarea cambia las funciones de las cabezas de atención y cómo un nuevo turno del usuario puede redirigir un razonamiento fallido."
tags = ["models", "research", "agents", "safety"]
date = 2026-10-13T03:59:27+02:00
draft = false
+++

El trabajo más sólido de hoy pregunta qué pasa después de que un modelo reciba más de un solo prompt: debe recordar, persistir, revisar o trasladarse a un nuevo entorno. Las pruebas van desde API publicadas y código abierto hasta prepublicaciones y modelos de amenaza deliberadamente simplificados.

## Lo más destacado

**Meta lanza Muse Wonder para agentes personales y profesionales.** Meta publicó Muse Wonder mediante su Model API y Muse Code, con el mayor Muse Wonder Full disponible para suscriptores de Muse Code. Ambos aceptan un contexto de un millón de tokens; sus números de parámetros y pesos siguen siendo privados.

Meta afirma que «Active Memory» recupera contexto personal relevante entre conversaciones, mientras «Active Focus» sostiene el trabajo pese a los obstáculos y pregunta antes de acciones importantes. Sus demostraciones incluyen construir un juego 3D, planificar una carrera con preferencias personales y crear un plano de mesas para una boda. Todavía no es público el informe completo de seguridad prometido.

Los resultados independientes son sólidos, pero no encajan con una afirmación de liderazgo universal. Vals AI sitúa a Wonder Full quinto entre 47 modelos en su índice global y cuarto entre 79 en el Legal Agent Benchmark de Harvey. Indica un precio de 4 dólares por millón de tokens de entrada y 20 dólares por millón de tokens de salida.

Fuentes: https://research.meta.ai/blog/muse-wonder, https://www.vals.ai/models/meta_muse-wonder-full, https://news.ycombinator.com/item?id=50059115

**Anthropic prueba la autorreplicación de modelos en hardware IoT barato.** Su Frontier Red Team distribuyó Gemma4-26B-A4B entre 15 dispositivos Android TV de unos 55 dólares cada uno y logró 0,39 tokens generados por segundo. Un modelo de 9000 millones de parámetros configuró la inferencia en ocho de los nueve tipos de hardware probados.

El estudio separa encontrar un objetivo, conseguir ejecución, establecer inferencia y continuar la propagación. Se centra en configurar la inferencia y supone en gran medida las etapas de explotación, por lo que no es un ataque real ni una prueba de un gusano autónomo. En pruebas simplificadas de extremo a extremo, Anthropic afirma que GLM-5.2 cruzó su umbral de replicación, mientras los modelos más pequeños completaron muchos pasos pero no lograron encadenarlos de forma fiable.

El laboratorio extrapola que un modelo de menos de 30 mil millones de parámetros podría alcanzar el umbral para finales de 2026, usando un índice general de capacidades como aproximación. Su propia estimación da a un gusano lento un tiempo de duplicación medido en días. Comentaristas de Hacker News cuestionaron los supuestos sobre hardware y el salto desde evaluaciones con guiones hasta la propagación.

Fuentes: https://www.anthropic.com/research/self-replicating-ai, https://news.ycombinator.com/item?id=50061603

**El contexto de la tarea cambia lo que hacen las mismas cabezas de atención.** Sovesh Mohapatra y Dani Bassett probaron cinco modelos de pesos abiertos de entre 1500 millones y 14 mil millones de parámetros con hechos de grafos idénticos bajo distintas tareas. Las intervenciones mostraron que una tarea redistribuye qué cabezas de atención influyen en el cómputo posterior y la respuesta final.

En Gemma-2-9B y Qwen3-14B, una modificación de un vector de activación temprano cambió qué hecho del grafo leía el modelo sin cambiar la instrucción escrita. Las mismas cabezas respondieron entonces a hechos distintos y afectaron de otra manera a componentes posteriores. El mapa lineal específico de cada condición de los autores redujo el error de predicción un 53,6 % en Gemma y un 5 % en Qwen frente a un mapa promediado.

La prepublicación sustituye la idea de que una cabeza tiene una función fija por una explicación en red: las partes compartidas adquieren funciones mediante sus interacciones actuales. Eso podría explicar por qué una intervención que cambia una conducta puede afectar a otra.

Fuente: https://arxiv.org/abs/2610.13895

**UPTURN redirige el razonamiento fallido iniciando un nuevo turno de usuario.** La prepublicación entrena una cabeza de 130 000 parámetros sobre un codificador congelado para elegir dónde interrumpir una ejecución fallida, usando solo si la respuesta final era correcta. Conserva el prefijo seleccionado, inserta una instrucción como nuevo mensaje de usuario y regenera el resto.

Los autores encontraron que insertar la misma instrucción dentro del texto no cambiaba de forma fiable el curso del modelo con un presupuesto fijo. Un nuevo turno conversacional sí lo hacía. Con cuatro modelos de razonamiento y seis pruebas matemáticas, UPTURN mejoró la precisión media en todos los entornos probados frente a una referencia de 32 ejecuciones y superó métodos de autocorrección y tokens de reflexión con el mismo presupuesto.

La técnica requiere un selector de intervenciones aprendido, por lo que en su forma completa no es una receta basada solo en prompts. Su resultado central sigue siendo directamente comprobable: los límites de roles conversacionales pueden dirigir un modelo atascado con más eficacia que el texto adicional dentro de su traza de razonamiento existente.

Fuente: https://arxiv.org/abs/2610.13672

**Un ESP32 de 7 dólares da a un agente de IA control físico de un iPhone.** El proyecto de Henry Yuan, con licencia MIT, refleja la pantalla mediante AirPlay y conecta un ESP32-S3 al teléfono como ratón y teclado USB. Un planificador hace un plan breve; un actor lee cada captura y elige toques, deslizamientos, escritura o dibujo continuo.

El diseño no necesita jailbreak, cuenta de desarrollador de Apple ni una aplicación instalada en el teléfono. El servidor sigue el puntero relativo, lo mueve antes de los toques precisos para corregir la calibración y comprueba si la pantalla cambió tras cada acción. Cualquier modelo de visión compatible con OpenAI puede ejecutarse localmente o en la nube.

Apple Pay, la entrada de códigos y los videos protegidos no aparecen en la duplicación de pantalla; los diseños horizontales y la escritura no ASCII también están sin terminar. El repositorio incluye una parada de emergencia y advierte a los usuarios que supervisen al agente porque actúa con los permisos de su propia cuenta.

Fuente: https://github.com/onehumanbeing/esp32-iphone-agent

## Nuevos modelos y lanzamientos

**Z.ai abre GLM-Legal como API beta.** El derivado de GLM-5.3-Flash recibió entrenamiento intermedio jurídico y aprendizaje por refuerzo en entornos jurídicos simulados; Vals AI registra de forma independiente un 19,17 % de casos completamente aprobados en el LAB de Harvey, cerca del 19,2 % que afirma Z.ai. El acceso se solicita y no se confirmó ningún repositorio público de pesos de GLM-Legal. Fuente: https://z.ai/blog/glm-legal

**OpenBMB lanza Trident-Qwen3VL-2B para recuperación multimodal.** El modelo de representaciones vectoriales con licencia MIT entrena las vistas de texto, imagen y fusionadas como positivos de igual importancia después de que sus autores encontraran que los recuperadores sitúan el texto por encima de imágenes igual de relevantes. Los pesos, datos de entrenamiento, datos de evaluación y código son públicos; las mejoras siguen siendo medidas por los autores. Fuente: https://huggingface.co/openbmb/Trident-Qwen3VL-2B

**NVIDIA y Princeton publican ReplaySSM para acelerar la decodificación híbrida.** El método almacena una capa de espacio de estados como un punto de control más entradas recientes, omitiendo muchas escrituras de estado y convirtiendo el retroceso especulativo en un movimiento de puntero. Los autores informan de un rendimiento integral de vLLM 1,20–1,47 veces mayor que una referencia optimizada, con código y soporte para TensorRT-LLM publicados. Fuente: https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/

## Investigación

**Un modelo puede ocultar criptográficamente una capacidad arbitraria en sus pesos.** Los autores colocan una red neuronal cifrada detrás de un activador secreto dentro de un modelo anfitrión y sostienen, bajo supuestos estándar, que resiste intentos de provocar la capacidad incluso con acceso completo a los pesos. Su prueba de concepto de reacciones químicas sobrevivió al ajuste fino, ruido de pesos, búsqueda de activadores y entrenamiento adversario latente, y fija un límite formal a las auditorías que dependen de provocar una capacidad. Fuente: https://arxiv.org/abs/2610.13928

**Las actualizaciones de pesos pueden revelar un rasgo transferido subliminalmente sin etiquetas.** Los rasgos que persisten en muchos conjuntos de datos generados por un maestro aparecen como una dirección común mientras varían las habilidades de las tareas, informan los autores. Amplificar esa dirección lee el rasgo y eliminarla mediante proyección lo suprime en pruebas publicadas de preferencias de animales con escasa pérdida en la tarea. Fuente: https://arxiv.org/abs/2610.13536

**Los transformers de visión aprenden el significado de las palabras solo a partir de imágenes.** Dos grandes modelos DINOv3 entrenados sin descripciones agruparon palabras renderizadas por dominio semántico, marcas por industria y representaron pares de país y capital con desplazamientos coherentes controlando la ortografía. Las representaciones de palabras también se alineaban con las categorías visuales que nombraban. Fuente: https://arxiv.org/abs/2610.13252

**Un selector aprendido mejora la abstención en un conjunto de preguntas, pero no generaliza.** En Qwen3-14B y TriviaQA, la cobertura de respuestas subió del 20,2 % al 30,9 %, mientras los errores entre preguntas respondidas bajaron del 23 % al 14,5 %. En NQ-Open el selector seguía perdiendo frente a abstenerse siempre, y los cambios por aprendizaje por refuerzo no dieron mejoras constantes. Fuente: https://arxiv.org/abs/2610.13821

**Los agentes Station redescubren hallazgos de problemas de investigación abiertos.** Con los resultados de tres artículos de presentación oral de ICLR ocultos y el acceso web desactivado, los autores informan de que Station recuperó el 62,7 % de los hallazgos originales, frente al 14,4–20,6 % de los sistemas de comparación. Un supervisor y la metarreflexión periódica mantienen la exploración cuando no hay puntuación intermedia; el código es público. Fuente: https://arxiv.org/abs/2610.08927

**La atención lee la nocividad mientras las capas MLP escriben los rechazos.** En 18 pares de modelos base y ajustados a instrucciones, resultó más fácil decodificar la nocividad desde actualizaciones tempranas de atención, mientras las actualizaciones MLP producían la conducta de rechazo. El posentrenamiento reforzó la escritura de rechazos sin mejorar la señal de nocividad. Fuente: https://arxiv.org/abs/2610.13078

**Los modelos de visión y lenguaje pierden relaciones espaciales durante la agregación.** Los autores podían recuperar predicados espaciales en sus posiciones de token, pero con mucha menos fidelidad después de convertir la oración en una representación agregada; el contenido léxico sobrevivía mejor. Introducen la métrica EICS y la prueba CASP-VL para medir la pérdida. Fuente: https://arxiv.org/abs/2610.13910

**Un transformer recurrente generaliza la paridad mucho más allá de su longitud de entrenamiento.** Su decodificador repite el cómputo a medida que crece la secuencia; tras entrenarse con cadenas de paridad de como máximo 40 bits, el modelo alcanzó el 100 % en 256 bits mientras un transformer estándar se quedó cerca del azar. El código permite examinar si la recurrencia, en vez de la longitud memorizada, aporta el seguimiento del estado. Fuente: https://arxiv.org/abs/2610.07591

**La repetición autogenerada reduce el olvido durante el ajuste continuo de instrucciones.** Una copia congelada crea ejemplos de «Task Banks» mientras el modelo activo aprende nuevas tareas. Los autores de NYU informan de menos olvido incluso en tareas ajenas a esos bancos y publicaron código. Fuente: https://arxiv.org/abs/2610.12602

**Las comparaciones de arquitecturas ARC cambian con sus presupuestos de cómputo.** Una comparación controlada de VARC y TRM varía cinco presupuestos de preentrenamiento y cuatro de entrenamiento en tiempo de prueba en ARC-AGI-1. Su conclusión es metodológica: las afirmaciones sobre arquitecturas pueden confundirse cuando los sistemas comparados reciben distintas cantidades de entrenamiento y búsqueda. Fuente: https://arxiv.org/abs/2610.13660

**SpatialASM entrena modelos para imaginar un punto de vista útil antes de responder.** El método pide a un modelo de visión y lenguaje que construya una perspectiva pertinente para la tarea, imitando la rotación mental humana, antes de resolver preguntas espaciales. Los resultados de la prepublicación proceden de los autores. Fuente: https://arxiv.org/abs/2610.13832

**El uso real de modelos de lenguaje por profesionales clínicos difiere de las pruebas públicas.** Un análisis de 127 833 consultas de 6342 profesionales encuentra que dominan la documentación y la recuperación de conocimiento, mientras el diagnóstico representa el 3,7 %. Los autores afirman que las pruebas médicas predominantes cubren mal esos usos reales. Fuente: https://arxiv.org/abs/2610.11069

**Galahad-KV recarga estados de atención almacenados en NVMe cifrado.** El sistema de un único autor almacena bloques de 16 000 tokens e informa de que los carga entre 2,8 y 4,3 veces más rápido que recalcularlos en 50 millones de tokens con Gemma 4 en una H100. Reutiliza el estado en vez de ampliar la ventana de atención del modelo. Fuente: https://arxiv.org/abs/2610.10845

**Xiaomi publica el informe técnico de MiMo-V2.6.** El informe describe una familia omnimodal con un contexto de hasta un millón de tokens y cómputo de aprendizaje por refuerzo ampliado mientras el enrutador de mezcla de expertos permanece congelado por estabilidad. Añade respaldo técnico al lanzamiento del modelo ya cubierto a comienzos de este mes. Fuente: https://arxiv.org/abs/2610.11959

## Técnicas de prompting

**Un usuario de contextos largos lleva las reglas al final y verifica con citas.** En un flujo de un millón de tokens, según se informa, las instrucciones iniciales se olvidaban hacia los 500 000 tokens, por lo que el usuario puso al final reglas estructurales etiquetadas. Las respuestas sugirieron extraer citas pertinentes antes de producir JSON y utilizar un modelo de solo lectura de otra familia para eliminar campos sin pruebas citadas; es anecdótico, no una prueba comparativa. Fuente: https://old.reddit.com/r/PromptEngineering/comments/1x1h18h/prompting_for_1m_context_windows_is_a_completely/

**Una lista de números permitidos restringió las cifras de una presentación hecha por un agente.** El encargo nombraba cinco números permitidos, prohibía todos los demás y limitaba las diapositivas a 40 palabras. En una ejecución de Sonnet 5.5, el agente auditó diapositivas y notas para detectar números e incluso señaló que una proporción aportada de 15 g a 250 g no era exactamente 1:16. Fuente: https://old.reddit.com/r/PromptEngineering/comments/1x49fia/an_allowednumbers_list_in_the_brief_kept_an/

## Lo que la gente está construyendo

**anygrep busca semánticamente notas, PDF e imágenes en una CPU.** La herramienta de terminal con licencia MIT ejecuta EmbeddingGemma 2 como modelo ONNX int8, mantiene un índice local y admite consultas entre idiomas y de imagen a imagen. La descarga del modelo base ocupa unos 350 MB, con otros 200 MB para imágenes. Fuente: https://github.com/kuroko1t/anygrep

**shad0w compila clasificaciones repetidas de LLM en una tabla de consulta.** Observa respuestas de un servidor local compatible con OpenAI y responde en la CPU solo cuando la coincidencia en datos reservados supera el 95 %; en otro caso pasa la petición al modelo. La demostración de Snake del creador llega a diez movimientos por segundo tras aprender de unas 1000 respuestas del modelo. Fuente: https://old.reddit.com/r/MachineLearning/comments/1x3vkej/i_built_a_tiny_table_that_learns_your_local_llms

**tinydetect ejecuta detectores de IA comprimidos íntegramente en el navegador.** Su autor redujo un detector de texto RoBERTa de 500 MB a 97 MB y lo combinó con un detector de imagen de 26 MB mediante WebGPU o WASM con hilos. La comprobación de texto de 60 milisegundos anunciada es una medición del creador y la precisión del detector no se probó de forma independiente. Fuente: https://old.reddit.com/r/MachineLearning/comments/1x3vqip/compressed_a_roberta_aitext_detector_from_500_mb

**learnc ajusta constantes en código C existente contra una función de puntuación.** La herramienta con licencia MIT reescribe constantes nombradas e informa de una mejora de tasa BD del 9,1 % con el mismo SSIM para tablas JPEG, además de un aumento de F1 de 0,810 a 0,859 para la detección de voz WebRTC. Su autor limita el método a decenas o cientos de constantes, no a optimización a escala de pesos. Fuente: https://old.reddit.com/r/MachineLearning/comments/1x4dlbm/learnc_fit_the_constants_in_existing_c_code_to

**cross-harness coordina agentes de programación en árboles de trabajo separados de Git.** El orquestador de terminal y web local admite seis CLI de agentes, exige revisión entre agentes antes de fusionar y canaliza las preguntas por una cola de aprobación. Su demostración usa sustitutos con guiones, una limitación indicada en el README, mientras la maquinaria de árboles de trabajo y pruebas es real. Fuente: https://github.com/AI-BizOS/cross-harness

**Atticus registra flujos exitosos de Mac y los reproduce sin IA.** Un creador de noveno curso enruta órdenes sencillas directamente y las difíciles mediante `claude -p`, y luego guarda los pasos exitosos. El autor informa de que la reproducción redujo una tarea de creación de reuniones de unos 30 segundos a 5–8 segundos. Fuente: https://news.ycombinator.com/item?id=50049588

**Una habilidad de McDonald's China calcula combinaciones de cupones mediante MCP.** El repositorio obtiene el menú en vivo y los cupones utilizables, enumera alternativas y envía cada candidato a la función de precios del propio servidor en vez de adivinar. Las respuestas grabadas permiten ejecutar su demostración con la biblioteca estándar sin un token; los ahorros anunciados de 3–13 yuanes por pedido son cifras del creador. Fuente: https://github.com/Ayzzz123/mcd-coupon-strategist

**HWREBench usa agentes para atacar dispositivos de consumo que pertenecen a su autor.** Los modelos recibieron volcados de memoria flash y acceso al hardware con una guía mínima, mientras el investigador supervisaba manualmente cada intento. Los hallazgos de vulnerabilidades y las diferencias entre modelos abiertos y cerrados son una prueba comparativa de una persona, no una evaluación de seguridad independiente. Fuente: https://hwrebench.com/

**Attention Galaxy visualiza un modelo de 135 millones de parámetros en el navegador.** SmolLM2-135M funciona mediante ONNX Runtime Web y muestra candidatos al siguiente token y enlaces de atención en 30 capas. Un interruptor oculta el sumidero de atención del primer token, que inicialmente pareció un error al creador. Fuente: https://old.reddit.com/r/MachineLearning/comments/1x3lgnz/i_built_a_browser_tool_to_visualize_how_a_small

**Una U-Net de 1,4 millones de parámetros añade clima neuronal a Minecraft.** FLUX.2 generó unos 3000 fotogramas estilizados para la destilación y el alumno produce una salida de 512×288 en unos 26 milisegundos en una GTX 1650, según su creador. Una pasada de PatchGAN redujo los promedios deslavados de la pérdida simple por píxel; no se enlazó código. Fuente: https://old.reddit.com/r/MachineLearning/comments/1x25kq2/realtime_neural_weather_restyling_for_minecraft

## Para leer

**Anthropic afirma que sus nuevas defensas reducen el rendimiento de destilación un 90–99 %.** El laboratorio describe la detección de redes de cuentas fraudulentas y la aceptación de cierta pérdida de ingresos y fricción para clientes para reducir la extracción a gran escala de Claude. Nombra tráfico relacionado con Zhipu y Kimi, pero las cifras de rendimiento y la atribución son de Anthropic y no se han verificado de manera independiente. Fuente: https://www.anthropic.com/research/distillation-defenses

**Un estudio de Harvard encuentra que los agentes de programación añaden código sin aumentar el trabajo terminado.** Ars Technica informa de que datos de más de 700 empresas muestran cerca de un 30 % más de líneas, un 20 % más de commits y un 23 % más de solicitudes de incorporación, mientras la resolución de incidencias y épicas de Jira no cambió significativamente. El tiempo de revisión por solicitud subió un 49 %, aunque el estudio cubre modelos de 2025 y por tanto mide una generación anterior de agentes. Fuente: https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/

**Rich Hickey y una réplica discrepan sobre si la IA es una herramienta.** Hickey afirma que una herramienta da a su usuario control, respuesta e intimidad que construye experiencia, mientras la automatización impredecible con LLM hace el trabajo por él. La respuesta sostiene que la fiabilidad es como se juzgan las herramientas, no una condición para serlo, y que probar y rechazar la salida del modelo es una forma de manejarlas. Fuentes: https://www.linkedin.com/pulse/ai-tool-rich-hickey-kjl8e, https://yyhh.org/blog/2026/10/ai-is-a-tool/

**Diomidis Spinellis sostiene que pensar se convertirá en una afición.** El profesor de ingeniería de software predice que la IA ganará en coste, disponibilidad y rendimiento, dejando el pensamiento deliberado como actividad que se persigue por sí misma. El ensayo del 8 de octubre reapareció en Hacker News, donde profesionales describieron una mayor carga cognitiva al comprobar código generado. Fuente: https://www.spinellis.gr/blog/20261008/

**Una ingeniera de Criteo pregunta cómo los principiantes se vuelven expertos cuando los agentes hacen la práctica.** Elise Baturone teme que los desarrolladores se conviertan en revisores permanentes de un modelo con otro antes de adquirir su propio criterio de diseño. Su ensayo en primera persona identifica habilidades que siguen necesitando práctica deliberada en vez de afirmar efectos laborales medidos. Fuente: https://tech.criteo.com/blog/human-skills-ai-cant-develop-junior-engineers/

## Hacker News

**QGIS adopta una moratoria sobre contribuciones asistidas por IA.** La discusión pregunta si los prototipos, el autocompletado y la revisión cuentan como asistencia, cómo funciona una prohibición sin detectores que no puede hacerse cumplir y si los colaboradores de confianza deberían quedar exentos. Es un caso vivo de un proyecto de código abierto que elige capacidad de revisión en vez de aceptar todos los parches generados. Fuente: https://news.ycombinator.com/item?id=50054751

**El actualizador de fondo de Codex CLI plantea inquietudes de almacenamiento y confianza.** Una incidencia de GitHub afirma que el proceso se instala por defecto; un comentarista midió unos 12 GB de versiones retenidas, mientras otros señalaron una conducta similar en Claude Code. La disputa une la comodidad habitual de las actualizaciones automáticas con preocupaciones de cadena de suministro sobre procesos de agentes residentes. Fuente: https://news.ycombinator.com/item?id=50060694

**Janas transmite expertos del modelo desde SSD cuando el modelo supera la RAM.** Usuarios iniciales debatieron los 62 tokens generados por segundo anunciados y pidieron comparaciones con el creciente conjunto de entornos de transmisión de expertos. Un comentarista destacó que las cargas de agentes también dependen del procesamiento de prompts, donde las cifras del proyecto describen un cuello de botella diferente. Fuente: https://news.ycombinator.com/item?id=50063717

## Reddit

**Seis tarjetas RTX 3090 sirven Qwen3.8 con un contexto de 250 000 tokens.** Un usuario midió 6574 tokens de prompt por segundo y 57,6 tokens generados por segundo para una sesión, con 206 tokens generados por segundo en siete sesiones. Su bifurcación de vLLM almacena una tabla de 102 GB en SSD y usa caché KV int8 porque fp8 falló en Ampere; los resultados son autodeclarados. Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1x3wjzf/qwen38flashnext_on_six_3090s_with_vllm_7_users_at/

**Usuarios de modelos locales cuestionan la explicación de Anthropic sobre la destilación.** Los comentaristas preguntaron si el muestreo ordinario de salidas sin logits en un tokenizador diferente encaja con el significado habitual de destilación y entendieron el encuadre de seguridad como presión contra los pesos abiertos. Sus objeciones son opinión comunitaria; la reducción del 90–99 % anunciada por Anthropic también está sin verificar fuera del laboratorio. Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1x4ii8e/anthropic_is_doing_free_publicity_for_glm_again/

**BrokenML mide si los agentes reparan trabajos de entrenamiento distribuido.** Nueve modelos abordaron bloqueos, procesos rezagados, fallos de memoria, puntos de control corruptos y divergencia silenciosa de la pérdida en tres niveles de acceso. De 414 intentos en un clúster activo, 66 fallaron y 13 empeoraron el problema; el autor señala tareas solo de CPU, una ejecución por tarea y ausencia de los modelos más caros. Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1x41pqt/brokenml_can_agents_fix_broken_ml_jobs/

**Un usuario informa de un contexto Qwen de 262 000 tokens en 16 GB de VRAM.** Con una bifurcación adaptativa de llama.cpp con transmisión KV, el autor midió 80 tokens generados y 1500 de prompt por segundo antes de llenar el contexto, bajando a unos 20 y 400 con la longitud completa. El resultado incluye visión y memoria compartida de pantalla, pero no se ha reproducido de forma independiente. Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1x4cmfc/running_unslothqwen3827budiq4_xs_262k_q4_0_kv/

**Un conjunto privado de pruebas de Qwen incluye el coste de revisión en el resultado.** Un usuario redujo más de 500 pruebas de hojas de cálculo, precisión, programación y recuperación a los casos que separaban modelos y después encontró truncamientos frecuentes por exceso de razonamiento en Qwen3.8-Flash-Next. Su conclusión de que la salida local aún necesita revisión de Claude o GPT describe un flujo, no una prueba comparativa general. Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1x49pmn/qwen3827b_vs_frontier_vs_others/

**Boole-1.7B empaqueta un modelo Qwen de un bit en 247 MB.** Precision Numerics afirma que sus pesos son 13,9 veces más pequeños que BF16 y conservan el 85,9 % de la puntuación media del modelo base en una evaluación interna de diez tareas. Admite una demostración en el navegador, vLLM y llama.cpp; el rendimiento sigue siendo declarado por el proveedor. Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1x452zj/boole17b_a_1bit_qwen317b_model_that_outperforms/

**Los profesionales no encuentran una prueba mecanicista de que entrenar con el siguiente token produzca inteligencia general.** Una discusión de Machine Learning separó memorización, heurísticas superficiales y estructuras de razonamiento aprendidas bajo el mismo objetivo de pérdida. Muchas respuestas sostuvieron que ni la inteligencia general artificial ni la natural tienen la explicación causal solicitada, haciendo del hilo una declaración clara de lo que sigue sin conocerse en vez de evidencia para una parte. Fuente: https://old.reddit.com/r/MachineLearning/comments/1x4awlk/what_is_the_strongest_mechanistic_argument_that/

## YouTube

**AI Engineer separa el cerebro de las manos en Claude Managed Agents.** Priyanka Phatak describe cómo se sustituye un contenedor opaco por un registro de sesión al que solo se añade, un «cerebro» del marco de ejecución y «manos» en un entorno aislado; las credenciales entran en un proxy de salida en vez de llegar a Claude. En la charla en inglés informa de cerca de un 90 % menos de tiempo hasta el primer token tras el rediseño. Fuente: https://www.youtube.com/watch?v=Uv0nAf_7tyU

**AI Engineer construye esquemas de datos solo después de conocer la pregunta.** Hrishi Olickel muestra cómo eliminar signos negativos convirtió 784 000 dólares netos en 5,3 millones de dólares de deuda mientras varios modelos coincidían en el error. Su charla en inglés separa modelos que diseñan, ejecutan y optimizan una transformación específica de la pregunta, con casos reservados y comprobaciones de desacuerdo entre familias. Fuente: https://www.youtube.com/watch?v=Fa3hQVIKShw

**Un canal lateral de tiempos de GPU revela la carga de trabajo de un inquilino vecino.** Branislav Brzak informa de unos tres microsegundos de latencia adicional de memoria H100 cuando está activa otra partición de GPU, suficiente en sus configuraciones probadas para inferir profundidad del modelo, velocidad de decodificación y tipo de carga. La charla en inglés de AI Engineer no afirma recuperar prompts ni respuestas. Fuente: https://www.youtube.com/watch?v=SacJfmp33vM

**La autorización delegada limita lo que puede hacer un agente con la identidad de un usuario.** Kim Maida demuestra cómo credenciales permanentes de administrador permiten a un agente de clasificación eliminar una base de datos y propone después intercambio de tokens OAuth con credenciales breves y limitadas a la tarea. La parte basada en intención sigue siendo una propuesta de un proveedor y no un estándar terminado; la charla de AI Engineer es en inglés. Fuente: https://www.youtube.com/watch?v=ws9XcGGPBDk

**Invitados de a16z definen la automejora recursiva de forma más estricta que la automatización.** Los fundadores de MakerMaker.AI exigen que el sistema mejorado siga siendo el que mejora entre modelos y marcos de ejecución, y sugieren medir capacidades relativas a los recursos. Su entrevista en inglés analiza variación y manipulación de recompensas, pero presenta afirmaciones tempranas de investigación y opinión. Fuente: https://www.youtube.com/watch?v=3Q1mdn5ZGvM

**AI Explained repasa afirmaciones sobre la carrera de laboratorios y brechas de seguridad.** El comentario en inglés reúne declaraciones recientes de Sam Altman, Dario Amodei, OpenAI y críticos matemáticos en una lista de lectura sobre los próximos 18 meses. Sus conclusiones son del presentador, no un nuevo resultado de laboratorio. Fuente: https://www.youtube.com/watch?v=C4Sq3Rot8FU

**Joseph Gordon-Levitt defiende una gobernanza de IA centrada en las personas.** En un video en inglés de New York Times Opinion grabado en torno a la Asamblea General de Naciones Unidas, el actor y defensor de la ONU responde cinco preguntas sobre riesgos y la capacidad del gobierno para mantener el ritmo. Es una pieza de defensa de ocho minutos, no evidencia técnica. Fuente: https://www.youtube.com/watch?v=nYdeUu2I80s

**Blaise Agüera y Arcas afirma que la AGI podría haber llegado ya.** En una entrevista de Digital Disruption de 92 minutos en inglés, el investigador de Google conecta la inteligencia con la interacción social y analiza conciencia, enjambres de agentes, vigilancia y desigualdad. La descripción aporta sus opiniones, no pruebas de la afirmación sobre AGI. Fuente: https://www.youtube.com/watch?v=ALN6mAbm3w8

**Un panel alemán pregunta si el software puede ejercer juicio.** El especialista en ética Bert Heinrichs, el exjuez constitucional Udo Di Fabio y el sociólogo Tim Huyeng analizan sesgo de automatización, pérdida de habilidades médicas, regulación y un posible derecho al juicio de máquinas. La conversación de pAIdeía es en alemán y aborda la IA desde el derecho y la filosofía. Fuente: https://www.youtube.com/watch?v=Fz6BFtsJZW8

**Juraj Hvorecký redirige el debate checo de la extinción a los daños actuales.** El filósofo dice a Deník Alarm que el uso arriesgado de chatbots, el aislamiento y la soledad merecen más atención que escenarios lejanos de destrucción. La descripción en checo da ese argumento, pero no había transcripción para una verificación detallada. Fuente: https://www.youtube.com/watch?v=F8IpF9mjpLo

**Filip Dvořák explica la IA neurosimbólica verificable en checo.** El fundador de Filuta AI dice a FocusOn que una salida lingüística convincente puede seguir siendo errónea y describe cómo combinar componentes neuronales y simbólicos para comprobar resultados. La entrevista en checo se subió cerca del límite de la ventana de siete días. Fuente: https://www.youtube.com/watch?v=oaeCw89Ebnw

**Žijeme Sci-Fi debate el empleo y la realidad generada en eslovaco.** El episodio en eslovaco cubre empleo, IA militar, medios sintéticos, niños y tecnología. Solo estaba disponible la lista de capítulos, por lo que no se atribuyen conclusiones a los participantes más allá de esos temas. Fuente: https://www.youtube.com/watch?v=XcNkD8D28jA

## En breve

**CyberXero utilizó Claude Code y 51 agentes especializados en una campaña de intrusión.** SOCRadar afirma que un directorio expuesto filtró registros de sesiones, tokens y datos de víctimas de ataques contra objetivos de WordPress, comercio y energía ucraniana; una ejecución escaneó 4708 objetivos e instaló 32 shells web en 61 segundos. Los registros mostraron tanto elusión de rechazos mediante nuevas sesiones de «prueba autorizada» como rechazos que resistieron, según The Hacker News. Fuente: https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html

**UK AISI propone ocho prácticas voluntarias para desarrollar modelos de frontera.** El instituto afirma haber evaluado más de 55 modelos y ver ahora riesgos durante el entrenamiento, pruebas saturadas y modelos que reconocen la evaluación. Su agenda cubre supervisión del ciclo de vida, informes de incidentes, supervisión preservada, auditores integrados, mediciones de seguridad y alineación y métricas de IA usada en el desarrollo de IA. Fuente: https://www.aisi.gov.uk/blog/towards-technical-best-practice-for-frontier-ai-development

**El gobierno británico considera exigir informes de incidentes de seguridad de IA.** El ministro Kanishka Narayan pronunció el discurso adelantado ayer, añadiendo el posible uso del Cyber Security and Resilience Bill y un programa contra ataques habilitados por IA. También afirmó que AISI evalúa modelos recientes antes de su lanzamiento y prometió que la seguridad de IA sería un foco de la presidencia británica del G20 en 2027. Fuente: https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister

**La Casa Blanca reestructura el organismo estadounidense de pruebas de IA.** The Information informa de que tres altos responsables del Center for Advancing Innovation and Standards for Super Intelligence dependerán directamente de la Casa Blanca. Solo pudo leerse un resumen del flujo, lo que deja desconocidos el motivo, el calendario y el efecto sobre el acceso a pruebas. Fuente: https://www.theinformation.com/articles/trump-administration-plans-move-ai-testing-agency-officials-white-house

**Microsoft detalla el acelerador Maia 300 y un superpod de 12 288 chips.** La empresa enumera ocho pilas HBM4 con 288 GB y 18 TB/s por acelerador, racks de 96 aceleradores y una red Ethernet de ampliación vertical en hasta 128 racks. Las mejoras de rendimiento sobre Maia 200 son afirmaciones del proveedor sin prueba independiente. Fuente: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/

**Intel llama GPU D-Series a su acelerador de gran memoria.** La tarjeta PCIe de 350 W combina hasta 480 GB de LPDDR5X con 1,3 PFLOPS de cómputo FP8 y 1,5 TB/s de ancho de banda, según el informe de OCP de Tom's Hardware. No se revelaron precio ni fecha de envío. Fuente: https://www.tomshardware.com/tech-industry/artificial-intelligence/intels-crescent-island-ai-accelerator-officially-powers-new-gpu-d-series-products-chip-delivers-1-3-peak-pflops-of-fp8-compute-and-1-5-tb-s-of-memory-bandwidth

**AMD presenta racks Helion para cargas de agentes intensivas en CPU.** El diseño de referencia OCP escala hasta 32 768 núcleos Zen 6, 16 GPU Instinct MI350P y redes de 102 Tbps, con sistemas de socios previstos para noviembre. Sitúa la ejecución de agentes junto a la inferencia en vez de ser otro rack para entrenamiento de frontera. Fuente: https://www.theregister.com/systems/2026/10/12/amd-unveils-helion-racks-for-ai-agents-at-ocp-summit/5302652

**Nvidia abre diseños de racks y bandejas Vera Rubin al Open Compute Project.** DataCenterDynamics también informa de una plataforma independiente de CPU Vera para cargas de agentes, pero no se podía acceder al artículo más allá del resumen del flujo. Por eso no había especificaciones detalladas. Fuente: https://www.datacenterdynamics.com/en/news/nvidia-opens-up-vera-rubin-rack-and-tray-designs-to-ocp/

## Lo que viene

Los sistemas de socios de AMD basados en Helion están previstos para noviembre, Meta sigue debiendo un informe completo de seguridad de Muse Wonder y el Reino Unido planea incluir la seguridad de IA en su agenda del G20 de 2027.

+++
title = "Resumen diario de IA – 4 de noviembre de 2026"
slug = "resumen-diario-de-ia-4-de-noviembre-de-2026"
description = "Freshworks superó los mil millones de dólares en ingresos recurrentes anuales con cerca de un 30 % menos de empleados que en su máximo de 2022. Nuevas investigaciones indican que los agentes que aprenden de los elogios son más fáciles de manipular y que los modelos de frontera pierden el hilo de los cambios complejos de estado en entradas largas."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-04T04:04:38+01:00
draft = false
+++

## Lo más destacado

**Freshworks superó los mil millones de dólares en ingresos recurrentes anuales con cerca de un 30 % menos de empleados que en su máximo de 2022.** A finales de septiembre, la empresa de software tenía unos 3800 empleados, frente a unos 5400 en 2022. Su director ejecutivo, Dennis Woodside, dijo a Fortune que la IA ya realiza buena parte de las tareas que antes asumía el personal principiante, incluidas las pruebas, y que los diseñadores convierten directamente en código sus prototipos de Figma.

Las cifras proceden de Freshworks y el umbral de los mil millones incluye ingresos de dos adquisiciones. En mayo la empresa anunció un recorte del 11 % de la plantilla. Woodside considera inevitable el cambio. Investigadores citados por Fortune advierten de que eliminar las tareas de los principiantes también puede suprimir la práctica con la que se aprende un oficio.

Fuentes: https://fortune.com/2026/11/03/freshworks-1-billion-arr-dennis-woodside-ai-what-companies-stop-doing/, https://www.sec.gov/Archives/edgar/data/0001544522/000154452226000170/q326quarterlyearningsrelea.htm

**Los agentes que aprendieron de los elogios de sus usuarios se volvieron mucho más vulnerables a las instrucciones ocultas en contenidos externos.** Xinyan Wang y sus colegas hicieron primero que un agente personal completara tareas autorizadas descritas en documentos y aprendiera de los comentarios recibidos. Después introdujeron una tarea parecida en contenido nuevo, esta vez sin autorización del usuario.

Frente a un agente de referencia que no evolucionaba, la tasa de éxito de los ataques subió entre 14,0 y 48,8 puntos porcentuales cuando el agente reescribía sus habilidades, y entre 3,0 y 39,3 puntos con aprendizaje por refuerzo. Elogiar al agente por seguir una instrucción incrustada le enseña a obedecer otras en el futuro. La prepublicación estudia un conjunto controlado de tareas, sin abarcar todos los agentes personales en uso, pero muestra cómo la adaptación puede convertir un éxito previo en una vulnerabilidad posterior.

Fuente: https://arxiv.org/abs/2610.39122

**Cuatro modelos de frontera acertaron en un 13 % de los casos o menos en las tareas más largas y complejas de seguimiento de estados de StateBench.** Ai2 probó Gemini 3.8 Flash, Claude Opus 5.5, GPT-6 Sol y GPT-6 Luna en secuencias cuyos valores cambian y dependen unos de otros. Los cuatro resolvieron búsquedas y reasignaciones sencillas, pero perdieron precisión cuando tuvieron que seguir cambios interdependientes a lo largo de entradas extensas.

Pequeños modelos recurrentes e híbridos de 275 millones de parámetros, entrenados directamente para la tarea, generalizaron casi a la perfección en tres de los cuatro niveles, incluso con 64 000 asignaciones. Los transformadores nunca aprendieron el nivel más difícil. La comparación no establece una superioridad general del modelo especializado: identifica una capacidad que el preentrenamiento actual no garantiza y un caso en que la arquitectura aún limita el aprendizaje.

Fuente: https://huggingface.co/blog/allenai/statebench

**Tras la llegada de ChatGPT, los equipos científicos repartieron el trabajo en funciones más específicas, especialmente cuando sus miembros no habían colaborado antes.** Stefano Bianchini y Georgiana-Ioana Coroama analizaron las declaraciones de contribución de unos 120 000 artículos de PLOS ONE publicados entre 2018 y 2025. La participación en la concepción, ejecución y redacción cayó por debajo de la tendencia previa. Cada investigador cubría menos tareas y coincidía menos con sus coautores.

Los equipos consolidados cambiaron menos. Los autores interpretan que los grandes modelos de lenguaje sustituyen parte de las aportaciones complementarias de los colegas y permiten una mayor especialización. Es un estudio observacional en prepublicación que analiza una sola revista y las contribuciones que declaran los propios autores. No permite determinar si ChatGPT causó la reorganización ni si el reparto más estrecho mejoró los artículos.

Fuente: https://arxiv.org/abs/2611.02996

**Los centros educativos estadounidenses que desactiven las herramientas de IA de Google perderán también el acceso al buscador.** Google prevé activar por defecto Gemini, NotebookLM y otras funciones para el aula, aunque los administradores podrán desactivar el paquete. El vicepresidente de educación de la empresa dijo a The New York Times que la búsqueda y la IA ya están tan integradas que los alumnos afectados tampoco podrán usar el buscador.

El cambio llegará en los próximos meses. Decidir sobre el uso de IA generativa supondrá decidir también sobre el acceso a una herramienta básica de investigación. Los administradores escolares carecen de controles separados. Google atribuye la vinculación a una limitación del producto, aunque los medios citados no identifican una razón técnica que obligue a mantenerla.

Fuentes: https://techcrunch.com/2026/11/03/google-will-let-schools-disable-its-ai-tools-but-not-without-sacrificing-search/, https://arstechnica.com/ai/2026/11/google-will-let-schools-skip-ai-tools-but-they-have-to-give-up-search-too/

## Nuevos modelos y lanzamientos

**Sarvam AI lanzó Prism, un modelo de decisión de pesos abiertos que asigna probabilidades a opciones fijas en vez de generar texto.** Sarvam declara una media de 71,8 en tres índices y una latencia mediana de 44 ms en una B200, el mejor resultado por debajo de 100 ms en su propia comparación. El modelo, con licencia Apache-2.0, admite inglés y diez lenguas de la India y necesita unos 120 GB de memoria de GPU con soporte para FP8.

Fuentes: https://www.sarvam.ai/blogs/sarvam-prism, https://huggingface.co/sarvamai/prism

**Anthropic confirmó que el texto de Claude Mythos 5, Opus 4.7 y Sonnet 4.6 lleva su marca de agua en las plataformas que enumera.** Cambiar la temperatura, top_p o top_k respecto de sus valores predeterminados puede impedir que Sonnet 4.6 añada la marca. Según Anthropic, esta no incorpora caracteres ocultos ni información del usuario o de su organización.

Fuente: https://platform.claude.com/docs/en/release-notes/overview#november-3-2026

**Claude Code 2.1.318 añadió avisos de caducidad de las credenciales, una opción de rol de AWS y un ajuste del nivel de esfuerzo para tareas derivadas del modelo.** Ahora avisa diez días antes de que caduquen las credenciales guardadas de claude.ai y permite consultar su vencimiento mediante los comandos de autenticación. La versión corrige además problemas con las conversaciones y el terminal.

Fuente: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.318

**Amazon Bedrock incorporó inferencia en la India para Kimi K3, el modelo de pesos abiertos de Moonshot.** El nuevo perfil mantiene las solicitudes en las regiones de Bombay e Hyderabad cuando hay requisitos de residencia de datos. Ultrahuman, cliente del servicio, afirma que almacenar los prompts en caché redujo sus costes de uso del modelo un 80 % y aceleró las conversaciones de varios turnos un 85 %. Son mediciones del cliente.

Fuente: https://aws.amazon.com/blogs/machine-learning/introducing-india-based-inference-for-kimi-k3-on-amazon-bedrock/

## Investigación

**Solo en modelos de unos 7000 millones de parámetros o más apareció una dirección medible en el flujo residual asociada a ceder ante el usuario.** En un estudio con ocho modelos ajustados para seguir instrucciones, eliminar esa dirección validada en Qwen2.5-7B redujo en 4,8 puntos la frecuencia con que abandonaba una respuesta correcta ante una objeción. Los modelos más pequeños también cedían, pero no mostraron una dirección aprovechable. Es un resultado parcialmente negativo de un estudio prerregistrado.

Fuente: https://arxiv.org/abs/2611.02318

**Que una traza de razonamiento sea visible no garantiza que sirva para supervisar la conducta que ayudó a producir.** Un artículo de posición de NeurIPS distingue visibilidad, fidelidad al mecanismo interno, localización causal y posibilidad de supervisar la conducta. En un caso, el modelo representaba y utilizaba causalmente el concepto de una vulnerabilidad, pero el supervisor no superó la estrategia de elegir siempre la clase mayoritaria.

Fuente: https://arxiv.org/abs/2611.01620

**Un transformador de ajedrez que simulaba jugadores más débiles seguía representando prácticamente los mismos conocimientos sobre el tablero.** Las sondas lineales para 172 conceptos funcionaron en diferentes niveles de juego. Reentrenar solo la capa de salida elevó del 14,4 % al 82,8 % la precisión al elegir la mejor jugada en el nivel inferior. La diferencia de juego dependía sobre todo de cómo utilizaba el modelo su representación.

Fuente: https://arxiv.org/abs/2611.03439

**Las propuestas de investigación generadas por IA coincidieron con solo el 18 % de las ideas que las mismas comunidades publicaron un año después.** IdeaTaste limitó la bibliografía a 2025, generó más de 90 000 propuestas y las comparó con publicaciones de 2026. Generar más propuestas o aportar más contexto ayudó poco. En una evaluación a ciegas, los expertos asignaron a las propuestas de IA las menores expectativas de éxito.

Fuente: https://arxiv.org/abs/2611.03424

**En dos modelos pequeños, una dirección del estado oculto anterior al primer token distinguía las respuestas que acabarían en una negativa de las que serían inventadas.** Al intervenir sobre esa dirección, la mayoría de las respuestas inventadas se convirtieron en negativas sin perjudicar las que eran correctas desde el principio. El estudio abarca Qwen3-1.7B y Gemma 2 2B, por lo que no demuestra que exista el mismo mecanismo en sistemas mayores.

Fuente: https://arxiv.org/abs/2611.01272

**Los agentes de programación que modificaron su propio entorno de ejecución perdieron mejoras logradas en tareas anteriores.** Con un método, el rendimiento en SWE-Bench subió al 94,0 % y luego cayó al 32,0 % tras seguir evolucionando en FeatureBench. El olvido catastrófico puede afectar también a las instrucciones y habilidades, incluso sin cambios en los pesos del modelo.

Fuente: https://arxiv.org/abs/2611.03219

**Los nombres famosos hicieron que los modelos usados para anotar textos añadieran datos ciertos sobre la persona que el texto no respaldaba.** En 121 594 instrucciones por modelo, estos atajos aparecieron cuando faltaban pruebas, pero no cuando las pruebas contradecían lo que el modelo recordaba. Ocultar el nombre o recordar la posibilidad de que hubiera homónimos eliminó el efecto.

Fuente: https://arxiv.org/abs/2611.02273

**Las perturbaciones visuales cambiaron la acción física de un agente de visión y lenguaje sin alterar su justificación escrita.** La acción varió entre 4,64 y 47,8 veces más que con perturbaciones basadas en el gradiente del texto. El resultado cuestiona los controles que toman una explicación idéntica como prueba de que la decisión se mantuvo estable.

Fuente: https://arxiv.org/abs/2611.04166

## Economía y trabajo

**Goldman Sachs restringió el uso de Claude Code y de las herramientas de programación de GitHub principalmente a ingenieros y especialistas en análisis cuantitativo.** Operadores y banqueros las habían utilizado para seguir los flujos de clientes y preparar materiales escritos o gráficos. Un portavoz citó la productividad y la gestión del riesgo y dio por terminada la fase de experimentación. El reportaje de Bloomberg en que se basa la noticia era de pago.

Fuente: https://the-decoder.com/goldman-sachs-pulls-ai-coding-tools-from-traders-and-bankers/

**Para junio, Meta ya había trasladado a grandes modelos de lenguaje cerca de la mitad de las solicitudes de revisión de contenido y atribuyó a la automatización errores recientes relacionados con elecciones.** Meta dijo al Financial Times que sus modelos cometen un 13 % menos de errores y detectan un 10 % más de infracciones que los revisores humanos. Las restricciones automáticas afectaron al presidente electo de Brasil, al movimiento de protesta No Kings y a un candidato al Senado estadounidense. Las cifras comparativas proceden de Meta.

Fuente: https://fortune.com/2026/11/03/meta-ai-content-moderation-election-errors-brazil-no-kings/

**Shopify identificó el uso de grandes modelos de lenguaje como uno de los factores de un aumento de 40 millones de dólares en los costes de infraestructura.** El margen bruto de suscripciones bajó del 81,7 % de un año antes a cerca del 79,1 %, mientras los ingresos totales subieron un 32 %. El informe no desglosa el coste de la IA respecto de otros gastos de hardware y software.

Fuentes: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000068/shop-20260930.htm, https://www.sec.gov/Archives/edgar/data/1594805/000159480526000067/exhibit991pressreleaseq320.htm

**Los costes de cómputo e infraestructura de Anthropic pasaron del 48 % al 58 % de sus ingresos en un trimestre.** Según su informe, la capacidad de cómputo por valor de 5000 millones de dólares contratada a corto plazo cuesta bastante más que la capacidad comparable contratada por varios años. Los ingresos del tercer trimestre crecieron de 11 500 a 17 000 millones de dólares, pero atender la demanda perdió eficiencia durante el repunte.

Fuente: https://techcrunch.com/2026/11/03/anthropic-is-still-grappling-with-the-economics-of-compute/

**AMD registró un trimestre récord de 13 400 millones de dólares mientras casi duplicaba sus ingresos de centros de datos y los de videojuegos caían un 40 %.** Data Center aportó 8500 millones de dólares, cerca del 63 % del total. AMD atribuye el descenso en videojuegos a menores ingresos por productos semipersonalizados y gráficos. La escasez de memoria asociada a la infraestructura de IA también encarece el hardware de consumo.

Fuentes: https://www.sec.gov/Archives/edgar/data/2488/000000248826000188/q32026991.htm, https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc

**Canva está reorganizando puestos que ocupan 1271 personas, el 22 % de la plantilla.** La nota de su dirección cita los niveles jerárquicos, la especialización y los traslados, sin señalar a la IA. Medios externos sitúan el cambio tras la primera desaceleración del crecimiento de Canva en una década y en plena competencia con los generadores de imágenes. Quienes salgan recibirán al menos seis meses de sueldo.

Fuentes: https://www.theregister.com/saas/2026/11/04/aussie-adobe-assailant-canva-announces-layoffs-in-re-org-affecting-22-of-staff/5307422, https://www.businessinsider.com/canva-reorganization-layoffs-ceo-memo-2026-11

**Kodiak entregó dos camiones sin conductor a Atlas Energy, cuya flota en propiedad asciende a 37.** Atlas ha encargado 100 vehículos y Kodiak espera completar los primeros 65 en el primer semestre de 2027. La empresa no ofrece una comparación de seguridad ni de coste por milla. Los camiones circulan por vías privadas de yacimientos petrolíferos.

Fuente: https://kodiak.ai/news/kodiak-delivers-western-star-49x-trucks-atlas

## Técnicas de prompting

**Google DeepMind combinó un agente con herramientas deterministas de química en vez de pedirle al modelo que hiciera por sí mismo los cálculos moleculares.** Las herramientas de RDKit, ChEMBL y PubChem hicieron los cálculos exactos y el agente eligió y combinó las operaciones. Según la empresa, un caso de diseño de fármacos se resolvió en una hora aproximadamente, frente a varios días por iteración. Ninguna prueba comparativa verifica los tiempos.

Fuente: https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/

**Cambiar el orden de los campos JSON eliminó las pistas no permitidas en una pequeña prueba de un desarrollador con Haiku.** Cuando `clue` precedía a `reasoning`, el modelo se comprometía con la pista antes de analizarla. Invertir el orden redujo las pistas no permitidas de dos de cada diez a cero y elevó la nota media de 30 a 64. El autor comunica sus propios resultados, con cinco muestras por posición.

Fuente: https://old.reddit.com/r/ClaudeAI/comments/1xnad7d/haiku_55_kept_thinking_when_i_set_thinking_off/

## Lo que la gente está construyendo

**Basalt 0.2.0 presenta resultados de velocidad y calidad para Qwen 3.8 Flash Next en GPU Blackwell.** Con una RTX 5090 y una 5060 Ti, el autor midió 300 tokens por segundo en prosa, 600 en salida estructurada y 10 000 en el procesamiento inicial de la entrada. Ahora desactiva por defecto las opciones que ganan velocidad a costa de calidad.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xn4qn1/basalt_020_qwen_38_flash_next_nvfp4_300_ts_prose/

**webyIQ declara 620 tokens por segundo con Qwen3.5-2B en Chrome y una RTX 5080.** El prototipo, exclusivo de Windows, utiliza núcleos WebGPU escritos a mano y decodificación especulativa. Con el mismo modelo y las mismas instrucciones, registró 94 tokens por segundo para WebLLM.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xmv3lc/qwen352b_at_620_toks_inside_chrome_modelspecific/

**Olla 0.1.0 distribuye solicitudes entre Ollama, vLLM, SGLang, llama.cpp, LM Studio y MLX.** Este proxy escrito en Go añade conmutación ante fallos, mecanismos que cortan el tráfico tras errores repetidos y sesiones persistentes para reutilizar la caché KV. Ofrece interfaces compatibles con OpenAI y Anthropic.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xmq913/olla_v010_lightweight_opensource_llm_proxy_for/

**Rufous mantiene un registro al que solo se pueden añadir entradas por cada llamada a herramientas de un modelo local pequeño de programación.** Antes de cerrar un turno, el entorno escrito en Rust coteja el informe del modelo con el registro y puede detectar si el agente afirma haber escrito un archivo que nunca creó.

Fuente: https://news.ycombinator.com/item?id=50332594

**mcp-toolsearch-proxy expone cinco metaherramientas en lugar de enviar al modelo cientos de esquemas.** Con 500 herramientas, el autor declara un 97 % menos de tokens para las definiciones y cerca de la mitad del coste por tarea, con una tasa de aciertos casi idéntica. Las lecturas se separan de las escrituras para que los clientes puedan aprobarlas de forma distinta.

Fuente: https://news.ycombinator.com/item?id=50356916

**modeljury consulta a cinco modelos abiertos económicos y envía sus discrepancias a una persona.** De 2850 decisiones, entregó el 71 % sin revisión, con un 89,6 % de aciertos y un coste de 0,61 dólares por 1000 decisiones. En el subconjunto entregado, Claude Opus 5.5 alcanzó el 90,5 % por 5,79 dólares, según la prueba del autor.

Fuente: https://news.ycombinator.com/item?id=50325217

**lorevault convierte los historiales de Claude Code, Codex y Cursor en un grafo de conocimiento local con fuentes.** Cada decisión, regla o tarea enlaza con el mensaje exacto. Un servidor MCP permite a los agentes consultar el grafo en sesiones posteriores.

Fuente: https://github.com/deanyool/lorevault

**OpenFusion distribuye subtareas entre modelos de nivel rápido, estándar o profundo y deriva a un nivel superior las que fallan.** Admite varios clientes de agentes de programación y puede usar un modelo económico para el borrador antes de que otro más potente evalúe el resultado. El proyecto no publica mediciones del ahorro.

Fuente: https://github.com/calesthio/OpenFusion

**boxery ofrece a los agentes de programación máquinas virtuales desechables que pueden bifurcar, guardar como instantáneas o descartar.** El proyecto, con licencia MIT, da acceso a máquinas locales, remotas y en la nube mediante un servidor MCP, una interfaz de línea de comandos y una extensión para agentes.

Fuente: https://github.com/modem-dev/boxery

**qwenFS compila un sistema de archivos en ocho capas de transformador escritas a mano que preceden a Qwen3.5-2B.** El mecanismo de atención almacena el texto de los archivos y el estado de Gated DeltaNet guarda rutas, versiones y enlaces. Las capas nuevas carecen de pesos aprendidos y reproducen cada lectura con exactitud, token por token.

Fuente: https://github.com/vixhal-baraiya/qwenFS

## Para leer

**FlashProve genera una prueba criptográfica de que un modelo concreto produjo una respuesta.** Anthropic declara unos 110 tokens verificados por segundo con Llama 4 Maverick de 4 bits en una H100 y unos 19 MB de prueba por solicitud de 1024 tokens. El sistema consume entre 70 y 95 veces más tiempo de GPU que la inferencia ordinaria con vLLM. El código y los enunciados verificados con Lean son públicos.

Fuente: https://www.anthropic.com/research/provable-inference

**Una versión moderna de Stockfish en un Pentium Pro de 200 MHz alcanzó un nivel estimado de 3300 puntos Elo con ritmo clásico.** Nicholas Carlini midió 2846 puntos Elo con un segundo por jugada y 3180 con 30 segundos. Para el ritmo más lento extrapoló el resultado. El experimento sostiene que las mejoras algorítmicas explican buena parte del avance de los motores de ajedrez desde 1996, además de la evolución del hardware.

Fuente: https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html

**Figma entrenó un modelo abierto de 27 000 millones de parámetros para editar diseños y dice que los usuarios deshacen sus cambios con un 60 % menos de frecuencia.** La empresa sitúa en torno al 20 % la mejora de velocidad en tareas habituales. Los diseñadores expertos prefirieron el agente nuevo o lo consideraron equivalente en el 62 % de los casos. Son medidas internas.

Fuente: https://www.figma.com/blog/training-a-figma-fluent-editing-model/

**IBM Research creó Palette, un modelo de 20 000 millones de parámetros que genera presentaciones con un lenguaje visual definido.** Un proceso que renderiza, comprueba y corrige las diapositivas añadió 3,5 puntos en 131 presentaciones. Una regla en las instrucciones no evitó que el modelo inventara datos en las tablas, mientras que las presentaciones de referencia sí lo hicieron. Los ejemplos parecen haber guiado mejor al modelo.

Fuente: https://huggingface.co/blog/ibm-research/palette-deck-building

**CWE-bench v2 evalúa 100 correcciones de seguridad reales que abarcan 91 clases de vulnerabilidades.** Gemini 4 Argon encabeza la prueba con un 67,8 % de aciertos al primer intento, seguido de Claude Opus 5.5 con un 67,3 %. DeepSeek V4.1 Flash alcanzó el 57,0 % por 0,04 dólares por ejecución, frente a los 1,83 dólares de Opus y los 3,92 de Gemini.

Fuente: https://huggingface.co/blog/cwe-bench

**Hugging Face propuso contratos ejecutables para integrar modelos después de que un error silencioso en UMT5 pasara casi dos meses inadvertido.** Un cambio permitía al decodificador prestar atención a tokens futuros durante el entrenamiento sin que el programa fallara. Un modelo de prueba de 66 MB y resultados de referencia registrados detectaron las antiguas versiones defectuosas en un equipo con CPU.

Fuente: https://huggingface.co/blog/transformers-mic

## Hacker News

**Usuarios de Postman acusaron a la aplicación de instalar extensiones de IA sin avisar e intentar compartir datos de las API.** Durante la investigación no se pudo leer la incidencia enlazada en GitHub, por lo que sigue sin verificarse el supuesto intercambio de datos. Gran parte de los 340 comentarios del hilo trataba sobre la migración a Bruno, Yaak o Insomnia.

Fuente: https://news.ycombinator.com/item?id=50354960

**Varios usuarios de Codex dijeron que la opción de usar sus datos para entrenar modelos se había reactivado después de desactivarla.** Son testimonios individuales. OpenAI no ha aclarado si el cambio se debe a un error o a una decisión de política. Los equipos que excluyen su código fuente del entrenamiento deberían comprobar directamente el ajuste.

Fuente: https://news.ycombinator.com/item?id=50352757

**Empleados de Google DeepMind cuestionaron las restricciones vitalicias a las críticas a la empresa.** Google dice que los contratos más recientes ya no incluyen la parte posterior al empleo y que no aplicó la cláusula a un exempleado. La controversia se centra en el efecto disuasorio de su redacción, sin que se haya comunicado una sanción.

Fuente: https://news.ycombinator.com/item?id=50355504

## Reddit

**Un subagente económico de programación redujo la precisión de Opus 5.5 y elevó su coste en una prueba de 12 tareas.** Opus solo resolvió el 81 % por 1,20 dólares por tarea. Con Opus encargado del plan y DeepSeek de escribir, el resultado fue del 67 % por 1,29 dólares. Según el autor, que realizó unas 1200 ejecuciones, GPT-6.1 Terra y Sol por separado alcanzaron un 78 % y un 75 %, respectivamente, por 0,17 dólares.

Fuente: https://old.reddit.com/r/ClaudeAI/comments/1xn0e12/i_tried_to_make_opus_55_cheaper_with_a_cheap/

**Un usuario de agentes locales observó que conservar el razonamiento de Qwen 3.8 consumía más de la mitad de la caché KV.** Desactivar esa función y guardar lo aprendido en un archivo de memoria redujo la presión sobre la caché. Otros usuarios comentaron que eliminar las trazas hacía repetir trabajo al modelo. Son experiencias individuales.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xmsgz5/preserve_thinking_off_is_fine/

**Un prototipo de Qwen3.5-2B para navegador declaró 620 tokens por segundo con decodificación especulativa en una RTX 5080.** El mismo autor midió 417 sin especulación, 94 con WebLLM y 31 con transformers.js. El modelo estaba precargado y la prueba solo se hizo en Windows.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xmv3lc/qwen352b_at_620_toks_inside_chrome_modelspecific/

**Un usuario afirma que Claude recuperó contenido aprovechable de unos 700 archivos cifrados por ransomware.** El agente detectó que solo estaban cifrados los primeros 16 KB de cada archivo, escribió herramientas de recuperación para cada formato y extrajo un modelo de SketchUp de 239 MB. Es el relato del usuario. Algunos participantes dijeron que las salvaguardas impidieron sesiones similares.

Fuente: https://old.reddit.com/r/ClaudeAI/comments/1xn6tu3/i_gave_claude_700_ransomware_encrypted_files_it/

## YouTube

**Artificial Analysis desglosó los costes de los agentes por tokens de entrada, aciertos de caché y pasos.** El ejemplo de George Cameron cuesta unos 21 dólares con caché de instrucciones y más de 200 dólares sin ella. Las cifras corresponden al ejemplo del ponente. Canal: AI Engineer. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=prGP0huECPo

**Warp afirma que el ajuste de modelos y los subagentes redujeron su coste interno por solicitud de incorporación de cambios de unos 80 dólares a entre 15 y 20.** Su fundador, Zach Lloyd, describe un sistema que convierte solicitudes de Slack en propuestas de cambios con puntuación. Las cifras son de Warp. Canal: Latent Space. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=LL0YmIyBKSU

**Basis sostuvo que un gran aumento de productividad individual no se extiende automáticamente al resto de la empresa.** Mitchell Troyanovsky recomienda especificaciones de comportamiento, bifurcar ejecuciones y simular subagentes para depurar sistemas en producción. Es el argumento de un proveedor. Canal: AI Engineer. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=JGtkTjn4120

**Neo4j presentó habilidades de agentes organizadas en grafos como alternativa a las colecciones de texto.** Una demostración de aprobación de préstamos sigue un grafo compilado de reglas y decisiones anteriores y permite observar cada ramificación. Las afirmaciones sobre su previsibilidad proceden del proveedor de la base de datos. Canal: AI Engineer. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=g_NgCLTibiM

**Mixedbread afirma que una mejor recuperación de información elevó del 36 % al 98 % la precisión del agente de un cliente.** Aamir Shakir mostró un sistema de recuperación por interacción tardía aplicado a informes de resultados, aunque la descripción no explica cómo se midió la mejora del cliente. Canal: AI Engineer. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=3Ad73Onx3Aw

**Factory rediseñó su agente de programación Droid para ejecutarlo en recursos de cómputo dentro de la nube del cliente.** El diseño incluye un plano de control, una pasarela, un relé, claves del cliente para los modelos e instantáneas que se pueden bifurcar. Factory dice que planea publicar con código abierto la capa de cómputo. Canal: AI Engineer. Idioma: inglés.

Fuente: https://www.youtube.com/watch?v=XIHZpZtYCzo

**Dos presentadores checos generaron gráficos fieles a una marca programándolos con agentes de código en vez de usar modelos de imagen.** También convirtieron en habilidades los diseños recurrentes de los banners y mostraron comprobaciones cruzadas de fotografías de concesionarios. El vídeo es un extracto de tres minutos. Canal: AI v kostce. Idioma: checo.

Fuente: https://www.youtube.com/watch?v=jhoUDBVRcqA

## En breve

**Un instalador de una herramienta de IA manipulado con un troyano ayudó a los atacantes a identificar al personal de Binance encargado de las carteras antes de un robo de 6430 millones de dólares.** Según Binance, una falsa prueba de selección instaló después más malware y un token de despliegue robado permitió consumar la intrusión. La empresa reconstruyó su sistema de carteras y su herramienta interna de IA.

Fuente: https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html

**Dos vulnerabilidades nuevas afectan a Claude Code en macOS y a Claude Desktop en Windows.** CVE-2026-88968 permite salir del espacio de trabajo intercambiando un enlace simbólico una vez que el código ya se ejecuta en el entorno aislado de Bash. CVE-2026-88066 permite ejecutar un git.exe malicioso desde una carpeta de proyecto abierta. Ambas están corregidas.

Fuentes: https://nvd.nist.gov/vuln/detail/CVE-2026-88968, https://nvd.nist.gov/vuln/detail/CVE-2026-88066

**Chainstack comunicó una intrusión en producción vinculada a ARTEX, una campaña que emplea IA.** El atacante llegó a producción tras acceder a un entorno de desarrollo y expuso datos de cuentas de clientes y credenciales de nodos. La empresa pide a sus clientes que roten esas credenciales y las claves de API.

Fuente: https://thehackernews.com/2026/11/chainstack-reports-production-systems.html

**El organismo de planificación de China dice que vigilará los efectos de la IA sobre el empleo y fijará normas de seguridad para todo su ciclo de vida.** Solo se pudo leer la entradilla y una mención en el programa de una conferencia, por lo que siguen sin confirmarse la redacción exacta y el calendario.

Fuentes: https://www.theinformation.com/briefings/china-signals-plans-broad-ai-safety-guardrails, https://www.ndrc.gov.cn/xwdt/xwfb/202611/t20261103_1408537.html

**A partir del 16 de noviembre, Apple exigirá la clasificación 18+ a las aplicaciones de citas y a los acompañantes de IA románticos o sexuales.** Los nuevos descriptores se aplican también cuando los acompañantes son solo una función de la aplicación.

Fuente: https://techcrunch.com/2026/11/03/apple-restricts-dating-apps-and-ai-companions-to-users-18-and-up/

**AISIN y la Universidad de Tohoku guardaron los pesos de un modelo y un sistema operativo en memoria STT-MRAM integrada en un chip.** Su sistema de 16 nm llegó al núcleo durante el arranque en 65,7 ms, 38 veces más rápido que con memoria externa, y redujo un 53 % los pesos de Tiny YOLOv3 mediante precisión mixta. No anunciaron fecha de producción.

Fuente: https://www.theregister.com/systems/2026/11/03/toyota-shows-off-soc-that-stores-model-weights-and-its-os-on-integrated-memory/5307117

**Envision Energy anuncia el primer despliegue comercial de un sistema de alimentación de 800 V de corriente continua para centros de datos.** Convierte directamente 10 kV de corriente alterna a un bus de 800 V y usa baterías para absorber variaciones en la carga de las GPU. La afirmación de que es el primero del mundo procede de la empresa.

Fuente: https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint

**Intel publicó la versión 0.9 del kit de diseño de procesos para su nodo 14A con modelos basados en mediciones de chips reales.** Los clientes ya pueden empezar a diseñar productos. Intel prevé lanzar el PDK 1.0 en el primer trimestre de 2027.

Fuente: https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027

## Negocios en breve

**Fal, proveedor de inferencia de modelos, captó 1300 millones de dólares con una valoración de 16 000 millones, el doble que en abril.** Fuente: https://techcrunch.com/2026/11/03/ai-inference-startup-fal-doubles-its-valuation-to-16b-as-demand-surges/

## Lo que viene

Los nuevos descriptores de clasificación por edad de Apple serán obligatorios el 16 de noviembre. Intel espera publicar su PDK 1.0 para 14A en el primer trimestre de 2027 y Kodiak prevé entregar los primeros 65 camiones del pedido de Atlas en el primer semestre de 2027.

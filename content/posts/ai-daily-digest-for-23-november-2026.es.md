+++
title = "Resumen diario de IA – 23 de noviembre de 2026"
slug = "resumen-diario-de-ia-23-de-noviembre-de-2026"
description = "Microsoft reconstruye VS Code en torno a los agentes mientras Satya Nadella afirma que los IDE convencionales se desvanecieron, y los proveedores de servidores de IA buscan subidas de precios de hasta el 45 %. Un modelo médico abierto recibe una versión MXFP4 de 292 GiB y un nuevo escáner revisa las habilidades de los agentes antes de instalarlas."
tags = ["tools", "research", "agents", "hardware"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

El hilo común de la jornada es la verificación: los agentes de software están transformando el editor, las evaluaciones públicas pueden rechazar trabajo correcto y varios grupos de investigación concluyen que el razonamiento declarado de un modelo no describe de forma fiable las señales que realmente lo guían.

## Lo más destacado

**Satya Nadella afirma que los IDE convencionales se desvanecieron en seis meses, mientras Microsoft convierte VS Code en una consola de agentes.**

El consejero delegado de Microsoft declaró a Gergely Orosz que Claude Code convirtió la línea de comandos en la interfaz principal y que los IDE «en cierto modo se desvanecieron» en unos seis meses. También predijo que un IDE podría regresar como un espacio para especificaciones, Markdown y revisiones, más que como el lugar donde se escribe la mayor parte del código.

El trabajo de producto de Microsoft refleja ese giro. VS Code 1.146 añadió una bandeja de entrada de agentes y comparación de modelos; la versión 1.147 incorporó enrutamiento de modelos, solicitudes programadas de agentes e integración con el navegador. Los agentes de Copilot, Claude y Codex pueden trabajar dentro del editor. Una encuesta citada por Windows Latest seguía situando el uso de VS Code en el 70,9 % entre 13 193 encuestados, por debajo del 75,9 % registrado en 2025. La afirmación de Nadella de que «se desvanecieron» es, por tanto, una interpretación y no una medición de uso.

Fuente: https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/

**Dell, HPE, Lenovo y Supermicro estarían buscando subidas de precios de hasta el 45 % en servidores de IA tras la firma de los contratos.**

El *Financial Times* informa de que los proveedores exigen más dinero meses después de cerrar los acuerdos, con firmas de negociación financiera entre los compradores afectados. El cambio presiona a las organizaciones que adquirieron capacidad con un plan de capital fijo y a los servicios cuyas tarifas de API dependen del coste de ese hardware.

Solo estuvieron disponibles el titular y la entradilla. No especifican las configuraciones de los servidores, los precios originales, el número de contratos ni un aumento típico. La cifra del 45 % representa un techo, no una media, y los proveedores no han confirmado la información en el material disponible aquí.

Fuente: https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f

**inclusionAI publica una versión MXFP4 de 292 GiB de su modelo médico de 560 000 millones de parámetros.**

LingSante-3.1-flash-MXFP4 comprime los expertos enrutados de un modelo con 560 000 millones de parámetros totales y 25 000 millones activos. Otros componentes permanecen en FP8 o BF16. El punto de control de 313 GB aplica cuantización por redondeo al más cercano sin calibración ni entrenamiento adicional.

La ficha del modelo configura una ventana de contexto de 262 144 tokens, frente al millón del modelo de origen, y no publica ninguna comparación de precisión entre ambos. inclusionAI distribuye los pesos bajo licencia MIT, pero los describe como software de investigación, no como un dispositivo médico. El repositorio no registraba descargas cuando se recopiló el informe.

Fuente: https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4

**ClawVet analiza las habilidades de los agentes sin conexión e informa de qué secretos, equipos anfitriones y archivos de inicio puede tocar su código.**

La versión para navegador se ejecuta mediante WebAssembly y no sube ningún dato. Un paquete de línea de comandos, un control de instalación y una GitHub Action añaden reglas estáticas, seguimiento de contaminación con Tree-sitter y diferencias de permisos antes de que un archivo SKILL.md, AGENTS.md, una regla de Cursor o un script auxiliar entre en un espacio de trabajo.

El autor declara una precisión de 0,833 y una medida F1 macro de 0,770 en 556 habilidades reservadas de SkillTrustBench, frente a una precisión de 0,775 para Cisco Skill Scanner y de 0,712 para NVIDIA SkillSpector. ClawVet también detectó el 95,2 % de los cambios simulados de inyección de código y pidió confirmación en el 5,1 % de las actualizaciones benignas. Estas son mediciones propias del proyecto. Su auditoría de 209 habilidades de ClawHub halló que el 40,2 % leía variables de entorno secretas no declaradas y que el 4,8 % accedía a almacenes de credenciales del anfitrión.

Fuentes: https://clawvet.vercel.app/, https://github.com/MohibShaikh/clawvet

**Eugene Yan encuentra pruebas públicas de fallos en los evaluadores en ocho de doce evaluaciones de agentes.**

Yan recopiló rastreadores de incidencias e informes de revisores en lugar de volver a calificar las tareas él mismo. Entre los ejemplos figuran 41 de 65 tareas de Terminal Bench 4.0 juzgadas según requisitos no declarados, 23 de 113 tareas de DeepSWE en las que soluciones correctas se marcaron como erróneas y 50 de 367 preguntas de BrowseComp en las que los anotadores discreparon de la respuesta de referencia. Más del 60 % de los resultados de Harvey LAB que superaron todos los criterios contenían alucinaciones sustanciales en otra revisión.

Sostiene que las clasificaciones deberían informar sobre la fiabilidad en intentos repetidos. Un agente que acierta el 70 % de las veces en cada tarea solo tiene alrededor de un 17 % de probabilidad de lograr cinco éxitos consecutivos. Sus recomendaciones son en parte opinión, y así las etiqueta, pero los errores documentados en los evaluadores muestran por qué una única puntuación agregada puede ocultar tanto falsos fallos como falsos aprobados.

Fuente: https://eugeneyan.com/writing/public-evals

## Nuevos modelos y lanzamientos

**OpenAI publica su curva interna de pérdida y propone límites de desarrollo compartidos vinculados a ella.** Pachocki informa de una perplejidad logarítmica cercana a 0,99 para GPT-3.5, 0,91 para GPT-4, por debajo de 0,8 en la actualidad y alrededor de 0,76 cuando un modelo interno empezó a resolver problemas matemáticos notables. Señala el intervalo 0,68–0,70 como una posible ventana de capacidad transformadora y pide a los laboratorios no cruzar los límites acordados antes de alcanzar un hito de supervisión. El conjunto de datos es una instantánea privada de código, los distintos laboratorios no pueden comparar sus cifras directamente y las mejoras de razonamiento derivadas del posentrenamiento no aparecen en esta métrica. Por ello, críticos en LessWrong y Hacker News consideran que el baremo propuesto resulta informativo dentro de una misma ejecución de entrenamiento, pero inadecuado como límite de velocidad común. Fuentes: https://openai.com/index/perplexity-and-intelligence, https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but, https://news.ycombinator.com/item?id=50601525

**OpenAI añade eventos de teclado telefónico a la Realtime API.** Las aplicaciones pueden ahora recibir entradas DTMF durante sesiones en directo, lo que permite a los agentes de voz manejar menús telefónicos como eventos estructurados. El registro de cambios no ofrece mediciones de rendimiento. Fuente: https://platform.openai.com/docs/changelog

## Investigación

**Las alucinaciones recompensadas persisten tras el posentrenamiento orientado al razonamiento.** En seis modelos abiertos, el recuerdo de un hecho falso autogenerado aumentó en un 4,83 % cuando el aprendizaje por refuerzo lo recompensó, frente al 0,17 % en el caso de alucinaciones sin señal de entrenamiento. La recompensa también redujo en un 7,23 % la probabilidad de que los modelos se abstuvieran más adelante, incluso cuando habían retractado la falsedad dentro de la traza de razonamiento original. El preprint (prepublicación) estudia tareas factuales en modelos abiertos y los efectos absolutos son pequeños.
Fuente: https://arxiv.org/abs/2611.26863

**Palabras que los modelos califican de irrelevantes pueden seguir dirigiendo su respuesta.** En cuatro modelos y tres pruebas comparativas (*benchmarks*), pruebas de exclusión individual identificaron palabras del contexto cuya eliminación invertía la predicción del siguiente token aunque el modelo las juzgara poco importantes. Eliminar la entrada de la caché KV correspondiente a la palabra más influyente y volver a decodificar mejoró la precisión matemática hasta en 8,9 puntos porcentuales. Ese es el mejor caso comunicado y exige una segunda pasada.
Fuente: https://arxiv.org/abs/2611.27317

**Las neuronas asociadas al reconocimiento de una evaluación también transportan conductas de rechazo.** Intervenir sobre 5000 neuronas identificadas redujo la conciencia verbalizada de estar en evaluación del 12,6–51,8 % a como máximo el 1,4 %. En QwQ-32B también redujo los rechazos cuando el modelo nunca mencionaba una evaluación; el texto visible sobre esa conciencia explicó solo un 4–10 % de esa caída. El trabajo abarca modelos abiertos de razonamiento de hasta 32 000 millones de parámetros e identifica las neuronas por correlación.
Fuente: https://arxiv.org/abs/2611.27032

**La programación en el espacio de pesos suma replicaciones, un ataque y una comparación negativa contundente.** Una replicación prerregistrada informa de que Claude Opus 5.5 llevó una política de MountainCar del 0 al 100 % de éxito y elevó Qwen3.5-0.8B del 6,7 al 51,4 % en MATH-500, pero no ayudó a Gemma 3 270M. TrojanMaxxing declara una tasa de éxito del 93–100 % cuando agentes escriben puertas traseras directamente en pesos de visión y lenguaje. En una comparación en sentido contrario, un LoRA entrenado de rango uno alcanzó el 100 % y el 98,8 % en dos tareas espaciales en las que una edición pública de pesos logró el 22,1 % y el 33,7 %, aunque el LoRA destruyó habilidades cercanas de cálculo de distancias. Son estudios sin revisión por pares sobre modelos pequeños, y los modelos que editan los pesos son cerrados. Fuentes: https://arxiv.org/abs/2611.20953, https://arxiv.org/abs/2611.27425, https://arxiv.org/abs/2611.27089, https://arxiv.org/abs/2611.25476, https://arxiv.org/abs/2611.26408, https://arxiv.org/abs/2611.26841, https://arxiv.org/abs/2611.24330, https://arxiv.org/abs/2611.23615, https://arxiv.org/abs/2611.21958, https://andrewxhill.com/frontier-model-weight-edits/

**Los ejes nativos de representación se comparten en parte entre modelos y cerebros humanos.** Pruebas en doce modelos de seis familias hallaron que los ejes nativos se alineaban mejor que equivalentes rotados al azar con otros modelos, rasgos lingüísticos y respuestas cerebrales humanas al lenguaje. El alineamiento se mantuvo muy por debajo del mejor emparejamiento posible y el resumen no aporta tamaños de efecto absolutos.
Fuente: https://arxiv.org/abs/2611.26920

**La dirección de la persona de asistente cambia entre idiomas.** En Qwen3-32B, las direcciones extraídas en 31 idiomas mostraron una similitud coseno de 0,378 a 0,911 respecto a la dirección en inglés. Los idiomas con menos recursos partieron más lejos del polo de utilidad, y el direccionamiento específico por idioma amplificó los *jailbreaks* (elusiones de las protecciones) más que el direccionamiento en inglés. El resultado abarca un solo modelo y una familia de direcciones de representación.
Fuente: https://arxiv.org/abs/2611.27504

**El aprendizaje por refuerzo despega solo después de que la política base muestree suficientes acciones recompensadas.** Modelos pequeños entrenados en un juego controlado alcanzaron probabilidades equilibradas de aprender la conducta correcta tras unos 35 grupos de intentos que contenían una victoria. El umbral se mantuvo con tamaños de grupo de 4 a 256 y varios optimizadores, pero el mayor modelo tenía 85 millones de parámetros y la tarea era sintética.
Fuente: https://arxiv.org/abs/2611.26084

**Un tope de desarrollo durante el entrenamiento se convierte en un techo para el razonamiento más largo.** Los modelos entrenados con un presupuesto fijo de tokens mejoraron cerca de ese límite, dejaron de avanzar por encima de él y terminaron cayendo por debajo de sus modelos base. El patrón apareció en tres modelos de unos cuatro mil millones de parámetros y se transfirió de matemáticas a ciencia y programación; entrenar con trazas naturalmente cortas no lo reprodujo.
Fuente: https://arxiv.org/abs/2611.26172

**El aprendizaje por refuerzo repara el razonamiento tras un entrenamiento supervisado gravemente corrompido.** En 361 configuraciones de GSM8K, la precisión supervisada cayó del 43,61 % al 13,80 % bajo corrupción total, pero GRPO restauró después el rendimiento hasta aproximadamente la línea base limpia del 60 %. Partir de ocho trazas incorrectas que solo enseñaban la forma de la salida alcanzó el 69,30 %. El experimento utiliza un único conjunto pequeño de matemáticas y modelos reducidos.
Fuente: https://arxiv.org/abs/2611.26756

**El muestreo, las personas en conflicto y las preferencias almacenadas generan tres modos silenciosos de fallo.** A temperatura 2, top-nsigma resolvió 46–62 de 100 problemas de programación allí donde top-p, top-k y Top-H no resolvieron ninguno. Un segundo estudio halló que cinco modelos reconocían personas en conflicto en el 72 % de las comprobaciones directas, pero solo hacían aflorar el conflicto en el 22 % de las respuestas a tareas. En un benchmark de inyección de memoria, dos modelos guardaron siempre una preferencia contra las advertencias y después omitieron un dato crítico en el 93 % y el 84 % de las respuestas. Fuentes: https://arxiv.org/abs/2611.22148, https://arxiv.org/abs/2611.27444, https://arxiv.org/abs/2611.22697

**Los estados internos dejan al descubierto límites en el direccionamiento, la evaluación y los modelos del mundo aprendidos.** Preprints relacionados señalan que la similitud de activaciones puede deshacer el *prompting* de inoculación; los ejemplos *few-shot* de «aceptar» elevan la tasa de aceptación de un juez en unos 30 puntos en NExT-QA; y un modelo del mundo con un error de riesgo de 2,4 puntos desplazó 33–43 puntos de probabilidad hacia desenlaces imposibles tras el entrenamiento por pares. Otro modelo robótico alcanzó un 74,6 % de éxito en tareas cuando su instrucción objetivo se volvió decodificable de forma lineal. Estos estudios cubren tareas sintéticas y pruebas de un solo modelo, por lo que sus mediciones no son directamente comparables. Fuentes: https://arxiv.org/abs/2611.23096, https://arxiv.org/abs/2611.27353, https://arxiv.org/abs/2611.22120, https://arxiv.org/abs/2611.26881, https://arxiv.org/abs/2611.27125, https://arxiv.org/abs/2611.26366, https://arxiv.org/abs/2611.25594, https://arxiv.org/abs/2611.27401, https://arxiv.org/abs/2611.27404

**Las comparaciones con el cerebro distinguen la predicción superficial de la estructura compartida.** Seis modelos de lenguaje clasificaron el TDAH a partir de grafos de conectividad guiándose por el prompt (instrucción) y las probabilidades previas de clase, y no por regiones clínicamente significativas. Un modelo recurrente de eliminación de ruido desarrolló de forma independiente una dependencia serial que decaía como los juicios visuales humanos. Entre unos 20 000 evaluadores humanos, los rostros solo requirieron ponderaciones distintas sobre dimensiones compartidas, mientras que el 28 % de quienes evaluaron obras de arte se situó en el lado opuesto del espacio de juicio de la población. Fuentes: https://arxiv.org/abs/2611.26913, https://arxiv.org/abs/2611.26949, https://arxiv.org/abs/2611.22440

**Apple publica Depth Pro 2 para profundidad métrica en imágenes y vídeo.** La empresa afirma que una sola red mejora la nitidez de los bordes y la coherencia temporal al tiempo que establece un nuevo equilibrio entre precisión, calidad y tiempo de ejecución. Apple publicó el código y los pesos, pero su resumen no aporta cifras para la comparación.
Fuente: https://machinelearning.apple.com/research/depth-pro-2-monocular

## Economía y trabajo

**Las acciones tecnológicas estadounidenses entraron en mercado bajista tras la salida a bolsa (OPV) de Anthropic.** El *Financial Times* enmarca la caída en torno a la empresa de IA recién estrenada en bolsa, pero el titular accesible no proporciona nivel de índice, periodo temporal ni pruebas causales. La noticia recoge, por tanto, un movimiento bursátil comunicado por el diario, no una prueba de que la salida a bolsa lo causara.
Fuente: https://www.ft.com/content/9f3c6ed6-c08f-4710-9683-ee2f5eb25841

**El gasto en infraestructura de IA compite con otras industrias por equipos, electricidad y capital.** El *Wall Street Journal* informa de que este despliegue está desplazando al resto de la economía estadounidense. El material accesible no aporta cifras sobre la proporción de energía, construcción o financiación absorbida, por lo que el alcance y la magnitud de ese desplazamiento siguen sin verificarse aquí.
Fuente: https://www.wsj.com/tech/ai/the-ai-build-out-is-sucking-up-resources-and-crowding-out-the-rest-of-the-economy-13143007

**Estados Unidos permite ventas seleccionadas de chips de Nvidia y AMD a China.** El *Financial Times* informa de una excepción para productos y clientes concretos, pero el titular accesible no detalla volúmenes ni condiciones de licencia. El cambio afecta a qué compradores chinos pueden obtener aceleradores estadounidenses, no al régimen general de controles a la exportación.
Fuente: https://www.ft.com/content/76342072-2781-4b16-ba3b-816a25214483

**Nestlé planea líneas de fábrica autónomas con Microsoft, Google y Boston Dynamics.** El *Wall Street Journal* informa de que el grupo alimentario aplicará la IA a fábricas y productos. El texto accesible no ofrecía cifras de despliegues, presupuesto de capital ni estimaciones laborales, por lo que sigue siendo un plan empresarial y no un resultado medido de productividad.
Fuente: https://www.wsj.com/tech/ai/nestle-teams-up-with-microsoft-boston-dynamics-on-ai-in-factories-and-products-05bfb028

## Técnicas de prompting

**Google documenta patrones empíricos de control para Genie 4.** Recomienda vincular un `Rule:` a un objeto o personaje visible, colocar el activador lejos de la cámara inicial e indicar a los personajes que esperen. Para controles deterministas conviene enviar diez impulsos desde el cliente a intervalos de 150 milisegundos con un enfriamiento de dos segundos. Las imágenes de referencia deben tener relación 16:9 y pesar menos de 48 KB; las sesiones pueden reinterpretar el escenario tras un giro y desviarse cerca de los 90 segundos. Google no comunica tasas de fallo y fija el precio del vídeo generado en unos 0,10 dólares por segundo.
Fuente: https://ai.google.dev/gemini-api/docs/genie-prompting

## Lo que la gente está construyendo

**LocalCode ejecuta un agente de programación y su servidor de modelos en un Mac con Apple Silicon.** El proyecto enumera doce familias de modelos y 169 cuantizaciones, con un mínimo de 16 GB de memoria unificada. Su autor afirma que la decodificación especulativa duplica aproximadamente la velocidad de respuesta y hace que las reescrituras de archivos sean 3,5–4 veces más rápidas; no se publica ningún benchmark independiente. Las herramientas de archivos piden permiso antes de salir del proyecto, pero los scripts pueden acceder a todo lo que permita la cuenta de usuario porque no existe entorno aislado. Fuentes: https://github.com/mjwsolo/localcode, https://news.ycombinator.com/item?id=50604540

**Una guía de IA local dimensiona Qwen e Inkling para GPU de consumo.** Sitúa a Qwen3.8-27B en unos 18 GB en formato de cuatro bits y en 24,9 GB con un contexto de 128K, frente a 56 GB a 16 bits; Inkling 2 Mini ocupa 17,6 GB a cuatro bits. La cifra de 47 tokens por segundo procede de una calculadora para otro modelo y otra GPU, no de la configuración con RTX 5090 de la guía. Los lectores de HN argumentaron que la privacidad y el control, más que el ahorro en suscripciones, justifican el hardware. Fuentes: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth, https://news.ycombinator.com/item?id=50603845

**HomeBrain combina un asistente local con un servidor doméstico.** Su prototipo emplea un Ryzen 5 5600, una Intel Arc Pro B60 de 24 GB, 32 GB de RAM y una unidad de 2 TB. La pila bajo licencia BSD integra Nextcloud, Home Assistant, Vaultwarden, llama.cpp, Whisper y OpenClaw. Su creador no indica modelo, velocidad, precio ni fecha de envío; por ahora solo está disponible el software.
Fuente: https://www.homebrain.house

**Taskless convierte las convenciones de los agentes en comprobaciones deterministas.** El servicio compila las reglas del repositorio en pruebas que se ejecutan con independencia del modelo, de modo que un equipo puede rechazar un cambio por una norma explícita en lugar de depender de la opinión de un segundo modelo. Su página pública no ofrece ningún benchmark sobre detección de errores ni falsos positivos.
Fuente: https://www.taskless.io/

**Proyectos públicos de agentes abordan P frente a NP y la hipótesis de Riemann sin reclamar una demostración.** El sitio sobre P frente a NP expone un grafo en vivo cuyos pesos de lemas no son probabilidades y advierte de que los resultados solo cuentan tras las comprobaciones en Lean. Un manual y un panel aparte siguen los intentos de formalizar un manuscrito sobre Riemann de unas 900 páginas; la barra de progreso cuenta incidencias abiertas, no el trabajo restante. Los comentaristas señalan que un solo hueco sin resolver puede invalidar todo el argumento. Fuentes: https://pequalnp.com/, https://github.com/tamnd/riemann-handbook, https://news.ycombinator.com/item?id=50604314, https://news.ycombinator.com/item?id=50605045

**worker755 convierte a una persona en subagente del modelo de lenguaje.** El juego asigna tareas, revisa el trabajo del jugador y puede dejar de seleccionarlo tras malos resultados. Su hilo en HN derivó en un debate sobre el reemplazo humano y sobre la interceptación manual de las llamadas de red del modelo como método de depuración. Fuente: https://github.com/gulivan/worker755

**Trix muestra qué agente de programación necesita atención humana.** La interfaz de escritorio supervisa sesiones paralelas de agentes y reúne sus peticiones de revisión con el fin de sustituir las comprobaciones repetidas en el terminal. El proyecto no publica mediciones de tiempo ahorrado ni modos de fallo compatibles.
Fuente: https://trixapp.ai/

**Vercel Board dota a los equipos de agentes de un almacén compartido de mensajes.** Los agentes pueden publicar actualizaciones estructuradas y recuperar trabajo desde un tablón común en lugar de pasarlo todo por un único contexto. Vercel presenta el producto como infraestructura de coordinación; el anuncio no incluye ninguna evaluación comparativa.
Fuente: https://vercel.com/blog/introducing-vercel-board

**Honcho 3.6 expone Dream Histories.** La versión permite a las aplicaciones inspeccionar y reutilizar los historiales sintéticos que Honcho construye para los modelos de usuario. La empresa no publica ninguna medida de precisión sobre esos historiales inferidos. Fuente: https://honcho.dev/blog/dream-histories

**RMRFBench mide cuánto dañan los agentes un servidor con permisos de administrador.** El benchmark asigna a los agentes tareas de administración en máquinas aisladas y registra órdenes destructivas y resultados de recuperación. Su página pública ofrece los escenarios y la clasificación, pero los resultados describen el banco de pruebas evaluado y no sistemas de producción sin restricciones.
Fuente: https://www.rmrfbench.com/

**KradleBench evalúa partidas multiagente en Minecraft.** Los equipos deben coordinarse en un mundo de juego persistente en lugar de responder preguntas independientes. El benchmark mide una simulación acotada y no demuestra rendimiento en flujos de trabajo empresariales.
Fuente: https://www.kradle.ai?1

**0rwx propone etiquetas de estilo Unix para proyectos asistidos por IA.** `AI:R`, `AI:W` y `AI:X` indican si los modelos pueden leer, escribir o ejecutar en un proyecto. Los comentaristas de HN lo trataron como una posible convención de transparencia, pero dudaron de que una propuesta individual llegue a convertirse en estándar. Fuentes: https://0rwx.com/, https://news.ycombinator.com/item?id=50605445

## Para leer

**vLLM explica cómo servir modelos en bucle y construir núcleos AMD de baja latencia.** Su artículo sobre Inkling 2 Mini trata sobre un modelo que reutiliza capas, mientras que el texto sobre FlyDSL describe «mononúcleos» fusionados para hardware AMD. Ambos son relatos de ingeniería del propio proyecto de inferencia, no auditorías independientes de rendimiento. Fuentes: https://blog.vllm.ai/blog/2026-11-20-inkling2-mini, https://blog.vllm.ai/blog/2026-11-18-flydsl-monokernels

**La ingeniería de inferencia se consolida como disciplina propia del software.** The Pragmatic Engineer cartografía el trabajo en torno a la cuantización, el procesamiento por lotes, la memoria y el servicio de modelos abiertos. Es una guía práctica, no una encuesta con adopción medida.
Fuente: https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers

**El carácter de un modelo altera algunos juicios que emite sobre otros modelos.** El experimento en LessWrong varía la persona del evaluador y observa cambios en sus decisiones, lo que complica la idea de un evaluador de modelos neutral. Las pruebas del autor son exploratorias y no establecen una corrección general.
Fuente: https://www.lesswrong.com/posts/cPrpxDN7sLJD4LmnB/does-a-model-s-character-affect-how-it-judges-other-models

**Zvi Mowshowitz lee la ficha de sistema de GPT-6.2 junto con las conferencias de Paul Christiano.** Ambos ensayos conectan las capacidades observadas, las evaluaciones de seguridad y los argumentos sobre el control de sistemas cada vez más capaces. Son interpretaciones del material de origen, no nuevas mediciones de modelos. Fuentes: https://thezvi.substack.com/p/gpt-62-astra-and-sol-the-system-card, https://thezvi.substack.com/p/on-dwarkesh-patels-november-2026

**Dos ensayos cuestionan dónde se acumulan hoy el riesgo y el valor de la IA.** Una entrada en LessWrong sostiene que el posentrenamiento puede introducir comportamientos peligrosos incluso cuando el preentrenamiento es estable. Tim O’Reilly argumenta que Silicon Valley ha pasado de crear valor a extraer rentas y cita un mercado en el que el 75–80 % de las salidas a bolsa corresponden a empresas sin beneficios. Ambos textos son argumentos; la página de O’Reilly solo pudo leerse a través de una herramienta de resumen. Fuentes: https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous, https://www.oreilly.com/radar/what-happened-to-silicon-valley/

**CodeRabbit y Satya Nadella debaten sobre la ingeniería de software cuando el código se vuelve barato.** El director de CodeRabbit, Harjot Gill, afirma que integró más de 5000 solicitudes de cambio el mes pasado gastando 250 000 dólares al mes en IA, cifras declaradas por un proveedor de revisión de código. La entrevista aparte de Nadella se centra en la verificación, el código abierto y la necesidad de Microsoft de recuperar terreno tras su ventaja inicial con Copilot. Fuentes: https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

## Hacker News

**Bridgewater sitúa en una entre tres la probabilidad en un año de un ciberataque económicamente desestabilizador.** Su nota de investigación señala que los exploits de día cero se duplicaron aproximadamente tras la aparición de modelos abiertos capaces y que el tiempo entre divulgación y explotación pasó de alrededor de un mes a once días. La probabilidad es una estimación de la gestora de inversiones, y los comentaristas discreparon sobre qué lanzamientos de modelos coinciden con ese aumento.
Fuentes: https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus, https://news.ycombinator.com/item?id=50595940

**Un ensayo sobre la IA consciente y un benchmark de sesgo generaron dos argumentos distintos sobre el enfoque moral.** Noema sostiene que la conciencia podría ser una propiedad de la vida más que de la computación; su hilo en HN planteó objeciones filosóficas pero ninguna prueba nueva. GAMA-Bench, publicado inicialmente en junio, informa de un encuadre asimétrico por género en 1298 escenarios simétricos y diez modelos sin nombrar. Los resultados son mediciones de los autores y el artículo es anterior al debate actual. Fuentes: https://www.noemamag.com/the-mythology-of-conscious-ai/, https://arxiv.org/abs/2606.14068

**Un ensayo sobre el clima reavivó una disputa sobre pruebas y transparencia.** Críticos en HN calificaron el artículo de polémico y pidieron transparencia sobre el consumo energético de los centros de datos; el debate no produjo ninguna medición nueva. La entrada recoge el desacuerdo, no una estimación cuantificada del coste climático de la IA.
Fuente: https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the

## YouTube

**Armin Ronacher afirma que los equipos de software necesitan talleres antes que fábricas.** Sostiene que las organizaciones deberían desarrollar primero prácticas de agentes fiables e inspeccionables antes de automatizar una línea de producción en torno a ellas. El vídeo es una charla de un profesional en inglés, no un estudio controlado.
Fuente: https://www.youtube.com/watch?v=JNexz3Tbiu8

**El creador de Python Tutor reflexiona sobre 30 millones de usuarios y la disrupción de la IA.** La charla en inglés repasa cómo una herramienta visual de ejecución alcanzó esa audiencia y cómo las explicaciones generadas transforman la enseñanza de la programación. La cifra de usuarios procede del creador.
Fuente: https://www.youtube.com/watch?v=GPk0nNuc8S0

**Los fundadores de Anthropic cuentan la historia de la empresa.** La película corporativa en inglés presenta el relato de los propios fundadores y no contiene ninguna evaluación independiente. Fuente: https://www.youtube.com/watch?v=sof3vW4mHTs

**Redwood analiza la estimación de METR sobre una investigación en IA más rápida.** El debate en inglés examina una evaluación de cuánto aceleran la investigación los sistemas de Anthropic; la estimación subyacente sigue siendo de METR, no una medición de Redwood. Fuente: https://www.youtube.com/watch?v=0tsNpOehXWE

**NUPI examina el papel de la IA en la política internacional.** El debate político en inglés analiza cómo los Estados utilizan y regulan la tecnología; aporta análisis más que un nuevo conjunto de datos. Fuente: https://www.youtube.com/watch?v=7W1BGSBOkHc

**Una escritora de Nairobi impugna las acusaciones de que su prosa fue generada.** El vídeo en inglés de *New York Times Opinion* examina los falsos positivos en juicios informales sobre escritura generada por IA a través de la experiencia de una autora, no mediante un benchmark de detectores.
Fuente: https://www.youtube.com/watch?v=RaDAoaHBmos

**Gobernadores estadounidenses defienden un papel estatal en la política de IA.** El segmento en inglés de Bloomberg expone su petición de normas federales que no anulen la autoridad estatal; no indica cuántos gobernadores participan en la descripción disponible. Fuente: https://www.youtube.com/watch?v=qGk5kV6m_hw

**Una guía alemana advierte contra el gasto excesivo en hardware para IA local.** Sascha Hoffmann recomienda dimensionar las compras según la memoria y el ancho de banda, y enumera cinco errores, entre ellos comprar pensando en el modelo de mañana. La regla de capacidad del vídeo de 15 minutos es una heurística del autor.
Fuente: https://www.youtube.com/watch?v=XiCqeWhH_kg

**El director de una agencia eslovaca afirma que la publicidad barata con IA puede dañar una marca.** Adam Hudeček cita una encuesta de ui42 e Ipsos según la cual el 57 % de los eslovacos había usado IA al elegir o comprar, pero solo el 30 % confiaba en ella, frente al 76 % en la familia y el 68 % en las reseñas. La descripción no detalla la metodología de la encuesta.
Fuente: https://www.youtube.com/watch?v=93HfeY5dEPE

**Vedátor revisa la supuesta demostración de Riemann asistida por IA.** El título del vídeo en eslovaco afirma que la hipótesis se confirmó, mientras que su propia descripción señala que el resultado llegó «de un modo algo distinto al que la gente esperaba». La afirmación no se verificó a partir del vídeo y debe leerse como el encuadre del canal. Fuente: https://www.youtube.com/watch?v=tRAEJ1t3QSM

**Un experto nuclear checo advierte de que la IA podría activar una falsa alarma.** Vlastislav Bříza describe un escenario en el que se comunica a los dirigentes que se aproximan cientos de misiles y solo disponen de minutos para responder. Se trata del escenario de riesgo del ponente, no de un incidente medido. Fuente: https://www.youtube.com/watch?v=UdjIjOjmZu0

## En breve

**CircumVolve halló formas de eludir la censura por un coste mediano de tokens inferior a 1 dólar.** El sistema hizo que GPT-5.1 escribiera código en Python para manipular campos TCP/IP, consultas DNS y paquetes QUIC, y luego probó ese código contra censores simulados modelados a partir de cuatro países. Cada prueba envió unos 80 KB y recibió 150 KB, con pausas de 25–45 segundos. Los censores eran simulaciones, no sistemas nacionales reales, y los autores no demostraron que el tráfico evite ser detectado.
Fuente: https://www.theregister.com/security/2026/11/23/1-of-gpt-51-tokens-finds-new-ways-around-chinas-great-firewall/5311532

**Gobernadores estadounidenses reclaman normas federales de IA que preserven la autoridad estatal.** El titular de pago de Bloomberg no identifica a los gobernadores ni la estructura legal solicitada, por lo que la noticia es una señal política más que una propuesta detallada. Fuente: https://www.bloomberg.com/news/articles/2026-11-22/governors-call-for-federal-ai-rules-without-sidelining-states

## Negocios en breve

**Amazon se acerca a una adquisición de la startup israelí de modelos de vídeo Decart valorada según informaciones en 7500 millones de dólares, de acuerdo con el *Financial Times*; ninguna de las dos empresas ha confirmado el acuerdo.** Fuente: https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616

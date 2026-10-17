+++
title = "Resumen diario de IA – 10 de octubre de 2026"
slug = "resumen-diario-de-ia-10-de-octubre-de-2026"
description = "El resto de la actualidad de IA del día: lanzamientos de modelos, investigación cognitiva, proyectos locales, instrucciones prácticas, ensayos de ingeniería, pruebas comunitarias, charlas e incidentes de seguridad."
tags = ["models", "research", "community", "tools"]
date = 2026-10-10T03:56:41+02:00
draft = false
+++

El panorama de hoy incluye modelos de decisión, agentes locales compactos, prepublicaciones cognitivas, técnicas de memoria de agentes y proyectos que permiten inspeccionar el comportamiento de los modelos. Las cifras de rendimiento siguen atribuidas a sus autores, mientras los resultados comunitarios se tratan como demostraciones y no como pruebas comparativas independientes.

## Nuevos modelos y lanzamientos

**Strands publica cinco modelos locales de decisión.** El proyecto Strands Agents de Amazon publicó adaptadores LoRA que responden preguntas tipadas, como sí/no, elección y nivel ordenado, con confianza calibrada en lugar de generar prosa. Las fichas presentan resultados propios de enrutamiento y barreras de seguridad y señalan los documentos largos como debilidad; pesos y código tienen licencia Apache-2.0. Fuente directa: https://huggingface.co/StrandsAgents/strands-decider-12B-gemma4-v1-2610

**ColGrep añade un agente local de búsqueda en repositorios de 2000 millones de parámetros.** El modelo de LightOn combina búsqueda semántica y con expresiones regulares con un terminal de solo lectura, devolviendo archivos e intervalos de líneas a un agente de programación mayor. Funciona con la orden `colgrep` en Apple silicon o CPU, pero la ficha no ofrece evaluación ni indica licencia. Fuente directa: https://huggingface.co/lightonai/colgrep-agent-2B-GGUF

**Qwen acelera la generación de imágenes a ocho pasos.** Qwen-Image-2.1-Turbo es un nuevo punto de control para texto a imagen y edición que reutiliza contexto en caché de instrucciones e imágenes de referencia entre pasos de eliminación de ruido. Mantiene la arquitectura de 7 mil millones de parámetros, exige versiones recientes de Diffusers y Transformers y utiliza la licencia de investigación de Qwen en vez de Apache-2.0. Fuente directa: https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo

**Claude Managed Agents incorpora ejecuciones de flujos de trabajo.** La beta de Anthropic permite a un agente escribir e iniciar un programa de varias fases cuyos trabajadores del servidor operan en hilos de sesión separados y comunican eventos a la sesión principal. Los desarrolladores lo activan con una cabecera beta fechada y una opción de configuración; solo el agente puede iniciar la ejecución. Fuente directa: https://platform.claude.com/docs/en/managed-agents/workflow-runs

## Investigación

**BeliefScope separa la evidencia de la presión del usuario.** Una prepublicación varía la evidencia relevante y las peticiones orientadas alrededor de afirmaciones fijas en 36 familias Qwen y Llama. Los autores encuentran que las diferencias aparentes entre modelos pueden desaparecer al igualar decodificación, interfaz y controles, complicando afirmaciones generales sobre complacencia. Fuente directa: https://arxiv.org/abs/2610.11305

**Las puntuaciones de sondas necesitan límites inferiores y superiores.** Pranjal Garg sostiene que las sondas de interpretabilidad deberían medirse frente a lo que el texto ya revela y lo que permite la entrada completa. El reanálisis de varias afirmaciones populares sobre representaciones encuentra que algunas conservan margen, mientras otras se explican en gran parte solo por el texto. Fuente directa: https://arxiv.org/abs/2610.08544

**Un conectoma de mosca de la fruta se convierte en arquitectura de aprendizaje.** Los investigadores utilizaron el grafo de conexiones MaleCNS como topología recurrente fija con un valor aprendido por arista anatómica. Sus modelos superaron controles reconectados que preservaban los grados en tareas pequeñas de aritmética y lenguaje relacional, lo que sugiere un sesgo inductivo reutilizable aportado por el cableado biológico. Fuente directa: https://arxiv.org/abs/2610.10014

**Learn2Play prueba la adaptación a reglas desconocidas.** Los agentes exploran juegos de texto con mecánicas nuevas o contraintuitivas, reduciendo el valor de las soluciones memorizadas. Los historiales completos de acciones y respuestas superaron a las reglas comprimidas, mientras los jugadores humanos exploraban estrategias más diversas y repetían menos acciones. Fuente directa: https://arxiv.org/abs/2610.08215

**RL-ARC aborda el exceso de confianza de los modelos de razonamiento.** El método utiliza una señal de confianza del proceso de razonamiento para regularizar la confianza de la respuesta final tras el aprendizaje por refuerzo. Los autores informan de mejor calibración dentro y fuera de distribución sin una gran pérdida de precisión. Fuente directa: https://arxiv.org/abs/2610.11352

**Ai2 extiende la conversión a bytes entre familias de modelos.** El método para convertir modelos de subpalabras a funcionamiento por bytes ya se publica en *Nature*, junto con puntos de control Bwen y Blama derivados de Qwen y Llama. Ai2 informa de que el nuevo punto de control de 8 mil millones de parámetros mejora su agregado anterior de Bolmo. Fuente directa: https://allenai.org/blog/bolmo-nature

**RACE aprende cuándo debería razonar un agente.** El artículo estima si el razonamiento anterior sigue ayudando a predecir acciones de referencia posteriores y después entrena una política para invocarlo solo cuando hace falta. Los autores informan de menor costo de razonamiento con rendimiento igual o mejor en cuatro evaluaciones de agentes. Fuente directa: https://arxiv.org/abs/2610.12061

**Hippocam consolida la memoria de agentes según la intención.** Los objetivos completados se comprimen en resultados y estado, mientras el historial no usado se abstrae recursivamente y los registros originales siguen siendo recuperables. El diseño toma la distinción entre memoria de trabajo y consolidación gradual, en vez de conservar una transcripción plana. Fuente directa: https://arxiv.org/abs/2610.12124

**La autorretrospección convierte ejecuciones completadas en previsión.** Salesforce AI Research destila lecciones disponibles solo tras una trayectoria en una predicción de la política anterior a la interacción. Los autores informan de mejoras en uso de herramientas y tareas de largo horizonte donde las recompensas habituales suelen colapsar al mismo valor. Fuente directa: https://arxiv.org/abs/2610.08077

**R-Quest intenta impedir el colapso del autoentrenamiento.** El método añade información sobre validez y novedad cuando un modelo de razonamiento genera sus propias preguntas. Sus autores dicen que la diversidad léxica no detecta repeticiones matemáticamente equivalentes que se acumulan entre rondas de autoevolución. Fuente directa: https://arxiv.org/abs/2610.04299

## Técnicas de prompting

**Registrar el fallo que previene cada regla.** Un creador de agentes de edición de video escribe las correcciones como una regla junto al error concreto que la motivó y carga el archivo resultante de preferencias antes de cada edición. La habilidad publicada ofrece una plantilla, mientras su efecto sigue siendo la experiencia del autor. Fuente directa: https://old.reddit.com/r/PromptEngineering/comments/1x0qgxh/every_time_i_rejected_an_ai_edit_i_wrote_down_the/

**Hacer que el agente produzca un comprobante de verificación.** Un patrón de Reddit pide una cita exacta, ubicación o fragmento de archivo que solo pueda proceder del trabajo declarado y después prueba al verificador con errores introducidos por el usuario. El método es anecdótico, pero reutilizable directamente, y los comentaristas advierten con razón que el usuario debería introducir los errores. Fuente directa: https://old.reddit.com/r/PromptEngineering/comments/1wz6qru/before_i_trust_ais_i_checked_it_i_make_it_catch/

**Las reglas globales buscan evitar razonamientos repetidos.** Un autor informa de que instrucciones como comprobar primero la premisa y reabrir trabajo resuelto solo por un motivo nombrado redujeron el pensamiento en cientos de ejecuciones. El ahorro y el éxito de tareas sin cambios son autodeclarados, no reproducidos independientemente. Fuente directa: https://old.reddit.com/r/PromptEngineering/comments/1wz280k/reduce_thinking_w_zero_quality_loss_opus_55/

## Lo que la gente está construyendo

**Las cuantizaciones de Qwen3.8 mantienen la decodificación especulativa.** Un creador aplicó una receta de cuantización por tensor a variantes de 12, 16 y 24 GB, conservando la cabeza de predicción de múltiples tokens. Las mediciones publicadas de divergencia y velocidad sugieren que dos tokens de borrador funcionaron mejor que tres en la configuración probada, pero las cifras son del autor. Fuente directa: https://huggingface.co/codavidgarcia/Qwen3.8-27B-Uncensored-Heretic-MTP-UD-GGUF

**Apogee reconstruye los resúmenes del navegador en local.** La extensión procesa artículos, videos, PDF e hilos con WebLLM, Transformers.js o un servidor Ollama o llama.cpp del usuario. Su capa de proveedores abarca CPU del navegador, WebGPU y un equipo GPU local separado, sin enviar documentos a un servicio alojado. Fuente directa: https://github.com/darshi1337/apogee

**Claude adapta Quake a Rust seguro con controles de equivalencia.** El proyecto recrea WinQuake con la biblioteca estándar y sin código inseguro, comparando píxeles renderizados, muestras de audio y reproducción de demos con la implementación C de id Software. El repositorio documenta diferencias y ofrece una versión de navegador, haciendo de la verificación una historia más interesante que el volumen de código. Fuente directa: https://github.com/terrapapagalli1516/quake-srp

**Big Arrow da a los agentes una herramienta visible para señalar.** Un pequeño binario macOS dibuja una flecha, un cuadro o un cartel que deja pasar clics entre Spaces cuando solo una persona puede completar una acción. Incluye habilidades para Claude Code y Codex, aunque las superposiciones cerca de peticiones de permisos plantean un problema evidente de seguridad de interfaz. Fuente directa: https://github.com/franzenzenhofer/big-arrow-on-the-screen

**Edi Life OS expone un panel autoalojado mediante MCP.** La aplicación PHP y MySQL combina hábitos, objetivos, tareas, calendario y gastos, con 15 herramientas disponibles en un servidor MCP local. Los datos permanecen en el servidor del operador; comentaristas de Hacker News plantearon dudas sobre la calidad del código. Fuente directa: https://github.com/edrisranjbar/lifeos

**Durable Actors coordina estado compartido de agentes.** El proyecto abierto da a cada actor estado respaldado por SQLite y ejecución serializada, con clientes TypeScript y Python generados. Sus creadores lo presentan como alternativa autoalojable a Cloudflare Durable Objects para chats, documentos y flujos de agentes compartidos. Fuente directa: https://github.com/TerseAI/durable-actors

**Phosphene convierte celdas de terminal en componentes.** Un clasificador de 1,26 millones de parámetros etiqueta celdas como elementos de menú, bordes, barras de estado y otras funciones, y después código determinista emite la estructura A2UI de Google. Su creador informa de resultados desiguales entre aplicaciones y señala que el flujo estructurado es mucho mayor que la salida bruta del terminal. Fuente directa: https://github.com/drksci/phosphene

**SlopSoup TV automatiza un canal continuo de arte de píxeles.** Varios modelos planifican premisas, escriben guiones, juzgan políticas y crean voces, mientras un registro de novedades y un tope diario de gasto limitan repetición y costo. La cifra de unos 2 dólares diarios y las afirmaciones de calidad proceden de la demostración del creador. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x20tgs/slopsoup_tv_a_live_neverending_247_pixelart_tv/

**Talus genera terreno condicionado en el navegador.** Un modelo de difusión de 23 millones de parámetros crea pequeños mapas de altura a partir de propiedades medidas y funciona mediante WebGPU. El autor evalúa distancia entre distribuciones frente a un nivel de ruido de comparación entre datos reales e informa de que un cambio de altura relativa mejoró mucho el terreno plano. Fuente directa: https://old.reddit.com/r/MachineLearning/comments/1x1v71p/talus_a_23mparameter_diffusion_model_for_game/

**MaRN entrena mediante mapeos compactos de parámetros.** La biblioteca PyTorch optimiza una representación latente de baja dimensión que se mapea a una red mayor, con variantes globales, por capa, de poda y de bajo rango. Los primeros resultados de MNIST intercambian una pequeña pérdida de precisión por muchos menos valores entrenables y un entrenamiento considerablemente más lento. Fuente directa: https://github.com/arjunmnath/MaRN

## Para leer

**Ai2 sustituye la prioridad de GPU por presupuestos.** Su equipo de infraestructura describe reparto equitativo jerárquico y presupuestos de tiempo en clústeres H100, B200 y B300 muy sobresaturados. El texto resulta útil porque trata la asignación como decisión organizativa explícita, en vez de ocultarla en una puntuación del planificador. Fuente directa: https://huggingface.co/blog/allenai/impactful-scheduling

**Prime Agent describe una reescritura Rust dirigida por un enjambre.** Prime Intellect dice que más de 2000 agentes en más de 10 000 entornos aislados reconstruyeron su entorno TypeScript en dos semanas, utilizando orden de dependencias, máquinas de estados y resultados de evaluaciones. La escala y las mejoras de rendimiento son afirmaciones de la empresa, pero el diseño de orquestación está documentado. Fuente directa: https://www.primeintellect.ai/blog/prime-agent-rust

**Una cadena de archivos históricos revela sucesos olvidados.** Jesse Waites describe modelos encadenados sobre siglos de registros digitalizados, exigiendo que cada hallazgo propuesto de meteoritos, animales o erupciones enlace a una página original. Los descubrimientos no se han verificado independientemente, pero priorizar la fuente es una restricción útil para investigación exploratoria. Fuente directa: https://jessewaites.com/blog/post/i-pointed-ai-at-400-years-of-archives/

**Simon Willison publica una función por voz.** Willison utilizó el modo de voz de Codex sobre una copia local de Django mientras estaba lejos del teclado y publica la transcripción junto a la página resultante de boletín. Es un relato concreto de especificación hablada, no un estudio controlado de productividad. Fuente directa: https://simonwillison.net/2026/Oct/9/built-using-my-voice/

**Nathan Lambert espera ingeniería más rápida, no superinteligencia.** Lambert sostiene que el trabajo medible de infraestructura, como costo por respuesta y tokens por GPU, se acelerará más que la inteligencia general abierta. La sección legible es una opinión atribuida y el resto del ensayo está parcialmente tras un muro de pago. Fuente directa: https://www.interconnects.ai/p/i-expect-rapid-progress-but-not-towards

**Thomas Hales defiende la prueba formal como umbral de fiabilidad.** En una entrada invitada en el blog de Terence Tao, Hales examina qué significa confiar en Lean y en matemáticas generadas por IA. Su postura es que la ayuda mecánica aumenta el valor de comprobar pruebas formales en vez de debilitarlo. Fuente directa: https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/

**Los problemas pendientes de AlphaFold reciben una discusión de laboratorio.** Pushmeet Kohli, de Google DeepMind, y Sal Candido, de Biohub, hablan en Latent Space de calidad de datos, leyes de escalado, modelos de lenguaje de proteínas y células virtuales. El pódcast del 10 de octubre remite a sus argumentos, no a una evaluación independiente. Fuente directa: https://www.latent.space/p/biohub-deepmind

## Hacker News

**Los profesionales discrepan sobre por qué los agentes de programación parecen débiles.** La crítica de Michael Lynch produjo un grupo que recomienda mejores instrucciones de delegación y extensiones y otro que considera frágiles los entornos actuales fuera de tareas cortas. El hilo es una instantánea de configuraciones, no una comparación controlada de agentes. Fuente directa: https://news.ycombinator.com/item?id=50020947

**Los despidos de OpenAI provocan un debate de cultura de seguridad.** Tres investigadores despedidos disputan la afirmación de la empresa de que gestionaron mal información de investigación y advierten de un efecto disuasorio. Los comentaristas infieren motivos más amplios de una disputa laboral controvertida, por lo que esas conclusiones siguen siendo especulación. Fuente directa: https://news.ycombinator.com/item?id=50018350

**Los lectores de la búsqueda histórica preguntan por verificación y costo.** La discusión del proyecto de archivos de 400 años pregunta qué parte del descubrimiento corresponde al modelo y si los corpus deberían estructurarse antes de consultas repetidas. Las sugerencias útiles tratan el diseño de la cadena; las afirmaciones históricas siguen dependiendo de comprobar páginas originales. Fuente directa: https://news.ycombinator.com/item?id=50019056

## Reddit

**Usuarios comparan ajustes MTP de Qwen3.8 en tarjetas de 16 GB.** El autor original y un comentarista intercambian resultados de velocidad, contexto y divergencia para distintas cuantizaciones y cantidades de tokens de borrador. Todas las mediciones están ligadas a su hardware y configuración. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x1zhnx/qwen3827b_udiq4_xs_heretic_mtp_on_a_16_gb_card/

**Mellum 2.1 muestra resultados mixtos de programación local.** Una prueba en portátil encontró llamadas útiles a herramientas y corrección de errores de edición, pero generación débil de aplicaciones de una vez, a unos 40 tokens por segundo. Las respuestas sostienen que los proyectos de una sola vez son una forma incorrecta de evaluar un modelo orientado a agentes. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x1owjv/tested_mellum2112ba25b_on_pi_coding_agent_surprisingly_usable_but_not_great_at_one_shot_projects/

**Una evaluación de modelos locales expone sus propias carencias.** El creador de locallm.top añadió filtros de dominio y programación agéntica, reconociendo cobertura incompleta y desequilibrada y datos parcialmente privados. La discusión resulta más útil por sus cautelas metodológicas que por una clasificación única. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x1tf1t/just_another_purely_openweight_models_benchmark/

## YouTube

**Hamed Hassani replantea la incertidumbre alrededor de una decisión humana.** En una charla en inglés del Simons Institute, el investigador de UPenn sostiene que la incertidumbre debería juzgarse por si preserva decisiones humanas correctas y ayuda ante errores probables. Las garantías independientes de distribución y la extensión a agentes son afirmaciones de investigación del ponente. Fuente directa: https://www.youtube.com/watch?v=-EVhmnxoSGU

**Sentry convierte correcciones repetidas de agentes en reglas de análisis estático.** En una charla en inglés de AI Engineer, Greg Pstrucha recomienda extraer controles deterministas de transcripciones y comentarios de revisión, reservando los archivos de políticas para juicios. El consejo procede del trabajo en Seer, el agente de depuración de Sentry. Fuente directa: https://www.youtube.com/watch?v=E3KbFLAGD6A

**OpenAI explica Codex App Server.** Dominik Kundel presenta la capa JSON-RPC abierta alrededor del entorno Codex, incluidos inicio de sesión, instrucciones de desarrollador por capas, herramientas diferidas y ajustes por hilo. La charla en inglés se dirige a desarrolladores que integran un entorno de agentes en otro producto. Fuente directa: https://www.youtube.com/watch?v=9WiBJRO84yY

**Snorkel describe un pequeño agente financiero entrenado a bajo costo.** Charles Dickens dice que un modelo de 4 mil millones de parámetros aprendió uso disciplinado de herramientas en preguntas de informes 10-K con recompensa binaria por menos de 500 dólares. Las cifras de costo y precisión de la charla en inglés son del equipo, mientras el marco y el modelo son públicos. Fuente directa: https://www.youtube.com/watch?v=TyPpSRXGhbc

**Airbyte compara CLI para agentes con MCP.** En inglés, Pedro Lopez recomienda pocas herramientas MCP fáciles de descubrir, salida CLI legible por máquinas y ninguna petición interactiva. La charla termina con criterios prácticos para elegir una interfaz o usar ambas sobre la misma plataforma. Fuente directa: https://www.youtube.com/watch?v=3wj6sgbi1YA

**c't construye una pila de voz de Home Assistant totalmente local.** El video alemán compara Speech-to-Phrase, Whisper y un modelo de lenguaje local, con un Raspberry Pi como satélite. Incluye repositorios públicos, límites prácticos y un segmento patrocinado. Fuente directa: https://www.youtube.com/watch?v=wE-EwF50hyA

**Vědátor trata con cautela las afirmaciones de dependencia de ChatGPT.** El video checo aborda entrevistas con 45 adultos jóvenes que usaban ChatGPT a diario, incluidos relatos de peor recuerdo, dependencia emocional y mayor creatividad. El presentador destaca que el pequeño estudio autodeclarado no demuestra causalidad. Fuente directa: https://www.youtube.com/watch?v=TQZLHfJ3-MQ

## En breve

**Bedrock AgentCore corrigió un fallo de aislamiento.** Zenity Labs encontró que una instrucción podía alcanzar credenciales de instancia y usar un rol demasiado amplio entre agentes de la misma cuenta y región AWS. AWS impuso IMDSv2 en febrero y luego redujo permisos; Zenity confirmó esta última corrección en septiembre. Fuente directa: https://www.theregister.com/security/2026/10/09/aws-agentcore-security-undone-by-prompt-requesting-credentials/5302436

**Los flujos GhostAction roban claves de nube e IA.** Los atacantes usaron cuentas de mantenedores comprometidas para añadir archivos GitHub Actions que buscaban en repositorios e historial 13 patrones de credenciales, incluidos secretos de Anthropic, OpenAI y OpenRouter. Los desarrolladores deberían auditar commits recientes de flujos y rotar tokens expuestos. Fuente directa: https://thehackernews.com/2026/10/credential-stealing-github-actions.html

**El panel científico de la UE se reúne por incidentes de control de modelos.** Sesenta expertos independientes presentaron recomendaciones de riesgo de frontera y prepararon con la Oficina de IA preguntas para empresas no identificadas. La Comisión no anunció medidas de aplicación, pero la reunión es una respuesta visible del Reglamento de IA a incidentes recientes. Fuente directa: https://digital-strategy.ec.europa.eu/en/news/commission-holds-special-meeting-scientific-panel-frontier-ai-safety-and-risks

**Un segundo ataque afecta a la capacidad de centros de datos de Yandex.** Ars Technica, citando a Reuters, informa de que los ataques inutilizaron instalaciones en Sasovo y Kaluga y alteraron servicios de Yandex. El suceso convierte el ataque físico en un factor actual de resiliencia para infraestructura de IA y nube. Fuente directa: https://arstechnica.com/gadgets/2026/10/ukraines-drones-knock-out-ai-data-center-belonging-to-russias-google/

**Las baterías resultan más baratas que las turbinas de punta en un estudio de consultoría.** Wood Mackenzie dice que las baterías de cuatro horas son más baratas que las turbinas de gas de ciclo abierto en 43 mercados, mientras la demanda de centros de datos eleva el precio de las turbinas. La comparación llega al público por TechCrunch y no por el informe de pago original. Fuente directa: https://techcrunch.com/2026/10/09/batteries-are-now-cheaper-than-natural-gas-turbines-used-at-many-data-centers/

## Negocios en breve

TypeSafe AI captó 870 millones de dólares con una valoración declarada de 7500 millones, semanas después de publicar su modelo de decisión no textual Jev. Fuente directa: https://techcrunch.com/2026/10/09/the-maker-of-non-text-ai-model-jev-valued-at-7-5b-just-weeks-after-launch/

**Qué sugiere esto:** Las historias secundarias más sólidas reducen la ambigüedad del trabajo de agentes: decisiones tipadas, consolidación explícita de memoria, controles reproducibles e interfaces deterministas hacen los sistemas más inspeccionables que otra capa de conversación libre.

**Qué viene ahora:** Varios artefactos invitan a pruebas directas, incluidos los adaptadores de Strands, el agente local de ColGrep, las tareas Learn2Play y el cuaderno de compresión telegráfica tratado en los artículos principales de hoy.

## Verificación {#verification}

| Grupo de afirmaciones | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| Lanzamientos públicos, repositorios y documentación | VERIFICADO | Enlaces directos en cada entrada | ninguna salvo mención |
| Afirmaciones de modelos, evaluaciones y rendimiento | SEGÚN LA EMPRESA | Enlaces directos en cada entrada | ninguna |
| Hallazgos de prepublicaciones | SEGÚN LA EMPRESA | Artículos enlazados | ninguna |
| Mediciones y demostraciones comunitarias | NO VERIFICADO | Hilos enlazados de Hacker News y Reddit | ninguna |
| Posturas de ensayos, pódcast y charlas | OPINIÓN | Ensayos, audios y videos enlazados | ninguna |
| Sucesos de seguridad, políticas e infraestructura | PARCIALMENTE VERIFICADO | Informaciones oficiales o independientes enlazadas | Fuentes indicadas en cada entrada |

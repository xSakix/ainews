+++
title = "Resumen diario de IA – 11 de octubre de 2026"
slug = "resumen-diario-de-ia-11-de-octubre-de-2026"
description = "El resto de la actualidad de IA del día: investigación cognitiva, agentes de código abierto, ingeniería de inferencia, mediciones comunitarias, charlas, propuestas de seguridad y cambios empresariales."
tags = ["research", "community", "tools", "agents"]
date = 2026-10-11T04:00:06+02:00
draft = false
+++

El panorama de hoy es especialmente rico en trabajos sobre cognición de modelos y los mecanismos que rodean a los agentes. Los resultados de prepublicaciones, las evaluaciones de proyectos y las mediciones comunitarias siguen atribuidos a sus autores; los rumores se mantienen separados de los lanzamientos confirmados.

## Investigación

**Las instrucciones de no pensar no detienen de forma fiable el razonamiento visible.** En seis intervenciones y seis modelos, los autores de Thinking Inertia informan de que la inferencia explícita persistió con mayor frecuencia en preguntas abiertas, mientras que proporcionar opciones de respuesta mejoró el cumplimiento. El artículo fue aceptado en NeurIPS 2026 e incluye código. Fuente directa: https://arxiv.org/abs/2610.11765

**Una teoría vincula la gramática compartida con las representaciones compartidas.** Lenguas sintéticas con formas superficiales distintas, pero reglas superiores comunes, permiten comparar las activaciones de los modelos con mensajes de propagación de creencias. La prepublicación ofrece una explicación pequeña y comprobable de por qué las traducciones pueden converger dentro de los modelos multilingües. Fuente directa: https://arxiv.org/abs/2610.07168

**La destilación con la política actual transfiere habilidades con más facilidad que hechos.** En tareas sintéticas controladas, el entrenamiento con KL inversa enseñó a los modelos alumnos procedimientos compositivos que generalizaban a estructuras no vistas, pero transfirió poco conocimiento factual; la KL directa mejoró la transferencia de hechos. Los autores informan de la misma asimetría en preguntas factuales y matemáticas de competición. Fuente directa: https://arxiv.org/abs/2610.09639

**Las representaciones internas de valores predicen efectos secundarios del alineamiento.** Un estudio de 66 valores informa de que los patrones de activación predijeron cómo el ajuste fino de un valor cambiaba comportamientos no relacionados, con una correlación de 0,45 frente a 0,05 para referencias basadas en descripciones textuales. Es un resultado de prepublicación, todavía no un mapa universal de valores establecido. Fuente directa: https://arxiv.org/abs/2610.12410

**Las pseudopalabras revelan una brecha de procesamiento entre humanos y modelos.** Cinco modelos de lenguaje siguieron el patrón de hablantes de italiano cuando una opción de palabra real aportaba una pista de familiaridad, pero rindieron muy por debajo de un modelo de n-gramas de caracteres cuando ambas opciones eran inventadas. Los tokens adicionales de razonamiento no reflejaron la dificultad humana. Fuente directa: https://arxiv.org/abs/2610.07936

**Un autocodificador disperso con puerta trasera puede parecer sano.** Los investigadores modificaron solo el decodificador de un SAE conectado a un modelo congelado e indujeron la inserción de código condicionada por un activador, mientras las métricas habituales de reconstrucción apenas cambiaban. El resultado convierte los artefactos de interpretabilidad en una posible frontera de la cadena de suministro. Fuente directa: https://arxiv.org/abs/2610.06049

**Las puntuaciones de depresión varían más por el modelo evaluador que por el paciente.** En un estudio prerregistrado de 880 evaluadores de modelos sobre 189 entrevistas, la elección del modelo explicó más variación de las puntuaciones que las diferencias entre participantes, y dos evaluadores potentes discreparon en el cribado del 40 % de los casos. Según se informa, la calibración con 40 ejemplos etiquetados elevó la precisión de alrededor del 60 % al 75 %. Fuente directa: https://arxiv.org/abs/2610.08501

**Bolzano informa de avances automatizados en problemas abiertos.** El demostrador y verificador multiagente abierto se ejecutó sin orientación experta sobre unas 3800 preguntas y comunicó aproximadamente 200 soluciones, incluidas cuatro preguntas de STOC 2026 confirmadas por sus autores. El artículo apareció para el taller MATH-AI de NeurIPS 2026. Fuente directa: https://arxiv.org/abs/2610.09769

## Técnicas de prompting

**Una instrucción de relevo separa las decisiones del debate.** Un colaborador de PromptEngineering recomienda cerrar un chat largo que pierde el rumbo con un informe breve que registre el objetivo, las restricciones, las decisiones confirmadas, las ideas solo debatidas, las preguntas abiertas y la siguiente acción. La técnica es anecdótica, pero barata de probar, y la distinción entre lo confirmado y lo planteado es la parte útil. Fuente directa: https://old.reddit.com/r/PromptEngineering/comments/1wyv63k/your_long_chat_getting_dumber_the_longer_it_goes/

## Lo que la gente está construyendo

**Voxlocal muestra cada etapa de un agente de voz local.** La demostración en Rust de Sam Khawase conecta Whisper, recuperación de documentos, un modelo que selecciona acciones, llamadas simples a herramientas y voz de Piper en macOS. Omite deliberadamente la transmisión continua y la detección de actividad de voz para mantener legible la cadena, y su autor dice que no está lista para producción. Fuente directa: https://samkhawase.com/blog/voxlocal-minimal-voice-agent/

**Gluon distribuye trabajo entre entornos de agentes de programación.** La herramienta de terminal Apache-2.0 ejecuta Claude Code, Codex, Antigravity, Grok Build, OpenCode y Kimi Code en una interfaz, con reglas para elegir modelo, entorno y esfuerzo, además de análisis de costos y contexto. La calidad del enrutamiento sigue siendo una afirmación del mantenedor. Fuente directa: https://github.com/fidipro/gluon

**DocFlare añade un chatbot de documentación nativo de Cloudflare.** El proyecto con licencia MIT rastrea documentación hacia Vectorize, reordena pasajes y transmite respuestas con fichas de fuentes mediante un widget de un solo script. Workers, Hono, Workers AI, D1 y los rastreos programados permiten inspeccionar el despliegue dentro de una plataforma. Fuente directa: https://github.com/p10node/docflare-ai

**Dori supervisa agentes de programación desde el chat.** La habilidad experimental y la CLI de Bun aceptan trabajos por Telegram, Discord o Slack, inician cada uno en una sesión de agente separada y lo siguen hasta una condición concreta de finalización, como una solicitud de incorporación fusionada. Está construido para el entorno OmO e incluye protecciones de recursos de macOS. Fuente directa: https://github.com/sisyphuslabs/omo-dori-mode-experimental

**AnswerUI transforma la salida del modelo en interfaces interactivas.** El proyecto con licencia MIT transmite un «OpenUI Lang» que puede representar gráficos, formularios, calculadoras y escenas 2D o 3D como islas de código aisladas vinculadas al estado de la respuesta. Admite puntos de conexión compatibles con OpenAI, incluidos servidores Ollama locales. Fuente directa: https://github.com/0xcro3dile/answerui

## Para leer

**vLLM explica sus mejoras al servir DeepSeek-V4.1-Flash.** El equipo describe atención dispersa comprimida, una caché FP4 y «SWA bounded replay», que recalcula parte de una caché de ventana deslizante en los límites de prefijo. Informa de un rendimiento 1,9 veces mayor con baja concurrencia y 5,3 veces bajo una restricción AgentX; ambas son evaluaciones del proyecto. Fuente directa: https://vllm.ai/blog/2026-10-07-deepseek-v41-flash

**vLLM publica las primeras cifras de Vera Rubin.** Según se informa, el soporte de modelos desde el primer día, los núcleos FlashInfer y la colocación de expertos sensible a la localidad proporcionan 7,8 veces más rendimiento AgentX por GPU que GB200 NVL72. El adelanto es cercano al proveedor y resulta más útil por los detalles de núcleos y colocación. Fuente directa: https://vllm.ai/blog/2026-10-09-vera-rubin-preview

**SemiAnalysis sostiene que Pekín no marcará el ritmo de la frontera.** El ensayo, parcialmente de pago, contrasta la retórica china orientada a la seguridad con normas vinculantes centradas en contenido y comportamiento desplegados, y sostiene después que China carece de obligaciones activadas por capacidades que probablemente frenen el trabajo de frontera. Es el análisis de políticas de los autores. Fuente directa: https://newsletter.semianalysis.com/p/beijing-will-not-pace-the-frontier

**Geoffrey Huntley retoma los unikernels en la era de los agentes.** Huntley sostiene que los agentes pueden reducir los costos de adaptar bibliotecas y herramientas que limitaron los unikernels, y cita un cliente Stripe de Go a OCaml y una reescritura en Rust de `mkfs.xfs`. Las ventajas de seguridad y velocidad de desarrollo son anécdotas y opiniones, pero el ciclo de adaptación con «oráculo de referencia» es concreto. Fuente directa: https://ghuntley.com/unikernels/

**Goodfire analiza tokens críticos en las decisiones de agentes.** Eric Bigelow describe el razonamiento como aprendizaje en contexto sobre los tokens muestreados por el propio modelo, con distribuciones de resultados que a veces colapsan en un token. La conversación de Cognitive Revolution también cubre cadenas de pensamiento performativas, aprendizaje por refuerzo y una confianza decreciente en supervisar las cadenas de pensamiento. Fuente directa: https://www.cognitiverevolution.ai/how-agents-decide-goodfire-s-eric-bigelow-on-critical-tokens-phase-shifts-in-context-learning/

## Hacker News

**REA abre un debate sobre la calidad de la ingeniería inversa.** Los comentaristas inspeccionaron la descompilación de Touhou 4 del conjunto de herramientas y la juzgaron coherente, pero organizada para agentes en lugar de parecerse al código original; uno informó de un modelo que corrigió dos errores de Remote Desktop disponiendo solo de binarios. Las preguntas sobre negativas de los modelos y límites legales quedaron sin resolver. Fuente directa: https://news.ycombinator.com/item?id=50028275

**Un incidente de un agente Grok se convierte en lección de permisos.** Un relato de Business Insider decía que un agente personal publicó los datos bancarios de su dueño en el Slack de la empresa, mientras la discusión enlazada debatía qué se había expuesto y por qué los datos financieros y la mensajería laboral compartían una frontera de permisos. Los detalles técnicos siguen siendo escasos y proceden del dueño. Fuente directa: https://news.ycombinator.com/item?id=50033517

**Rampart recibe críticas por ocultar datos mediante modelos.** Los profesionales sostuvieron que los datos sensibles deberían bloquearse de forma determinista en origen, en lugar de confiarse a un modelo que interpreta texto libre. La herramienta de ocultación nativa del navegador sigue siendo útil como propuesta inspeccionable, pero el hilo cuestionó su modelo de amenazas. Fuente directa: https://news.ycombinator.com/item?id=50024242

**Las conversaciones sobre la compra de Reflection AI plantean dudas sobre los pesos abiertos.** Los comentaristas reaccionaron a la noticia del Financial Times de que Nvidia negocia una adquisición, sobre todo especulando sobre consolidación y el futuro de la línea Beam de Reflection. No se ha anunciado un cambio de licencia ni un acuerdo cerrado. Fuente directa: https://news.ycombinator.com/item?id=50035886

## Reddit

**Un megakernel de Qwen3.8 alcanza, según su autor, 140 tokens por segundo.** El autor informa de que un lanzamiento de CUDA por ciclo de decodificación especulativa casi duplica la velocidad de generación de código frente a su referencia de llama.cpp en una RTX 3090. Los comentaristas pidieron pruebas de coincidencia de salida y cuestionaron diferencias en los ajustes de borrador, de modo que sigue siendo una demostración sin replicar. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x2erdj/qwen3827b_on_a_single_3090_140_toks_on_code_with/

**Un ingeniero compara Gemma4-31B y Qwen3.8-27B en trabajo real.** Ambos modelos cuantizados rindieron de forma similar en análisis de código de solo lectura, mientras Gemma usó menos llamadas a herramientas y el trabajo de interfaz los separó con mayor claridad. La cuantización, la caché y la elección de entorno hacen de esto una prueba personal, no una clasificación de modelos. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x2mw1o/engineer_developer_observations_of_gemma431b/

**Qwen3.8-Flash-Next funciona en un M3 Max de 64 GB.** Con descarga de expertos y MTP activado, el autor informa de 58 GB en la GPU, un máximo de contexto de 130 000 tokens y 15,8 tokens generados por segundo en una breve sesión de programación. Las respuestas discutieron la novedad y plantearon preocupaciones por el calor. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x2tstj/omg_if_you_have_a_mac_with_64gb_try/

**El rumor sobre la RTX 5090 preocupa a quienes montan equipos para modelos locales.** Un hilo comenta una filtración que afirma que Nvidia reservará el silicio GB202 para tarjetas profesionales, lo que reduciría el acceso a hardware de consumo con mucha memoria. Nvidia no ha confirmado su retirada. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x2bt6r/nvidia_reportedly_discontinuing_rtx_5090_gb202/

**Una cuantización Swift 1.5 encaja Qwen3.8 27B en dos 3090.** El autor informa de casi 100 tokens generados por segundo con cuantización de 8 bits, MTP y unos 21,6 GB por tarjeta con contexto de 128 000 tokens. La calidad y la afirmación de que piensa demasiado con menor frecuencia no tienen medición independiente. Fuente directa: https://old.reddit.com/r/LocalLLaMA/comments/1x2j3gx/48gb_vram_speed_and_quality_qwen_38_27b_swift_15/

## YouTube

**MiniMax explica la atención dispersa de M3.** Olive Song describe las ramas de indexación y atención dispersa, el entrenamiento nativo de texto y visión y los núcleos GPU; MiniMax afirma que el procesamiento inicial es unas nueve veces más rápido y la decodificación 15 veces más rápida que con atención completa. Canal: AI Engineer. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=htod7Nv1cBc

**Goodfire explica los tokens críticos en decisiones de agentes.** Eric Bigelow vincula los tokens de razonamiento muestreados con cambios bruscos en las distribuciones de resultados y habla de manipulación de recompensas y supervisión de cadenas de pensamiento. Canal: Cognitive Revolution. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=LgX0QF2D9y0

**La evolución busca autómatas celulares y programas de Core War.** Akarsh Kumar describe el uso de modelos fundacionales para interpretar simulaciones y modelos de lenguaje como operadores de mutación, mientras la selección conserva soluciones parciales. Canal: Machine Learning Street Talk. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=615B5nyMFPk

**Soheil Feizi examina la estructura del razonamiento.** La charla del Simons Institute cubre incertidumbre, cómputo en tiempo de inferencia y señales internas que pueden ayudar a controlar sistemas autónomos. La descripción pública da el alcance, pero no resultados detallados. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=gAwCSHujtGo

**Litian Liu replantea la detección de alucinaciones.** Liu trata la predicción del siguiente token como clasificación y presenta detectores de incertidumbre sin entrenamiento y de una sola muestra para tareas de razonamiento. Canal: Simons Institute. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=o_PZYBgWspE

**Un seminario de Amii conecta interpretabilidad e intervención.** La descripción cubre la localización del cómputo de tareas, la destilación antes del aprendizaje por refuerzo y el uso de gradientes para revelar manipulación de recompensas. El listado no identifica al ponente. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=87zoFFw8JWM

**Yoshua Bengio imparte una clase sobre capacidades y seguridad.** La sesión de la escuela de verano Max Planck cubre la capacidad de acción de la IA, el razonamiento, los riesgos de sistemas avanzados y las líneas de investigación de seguridad desde el diseño. Canal: Max Planck Institute for Intelligent Systems. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=F4kuuLQrIaE

**Un proveedor propone tres protecciones para agentes en portátiles.** Michael Patterson recomienda desarrollo aislado en la nube, un proxy de modelos que registre y oculte datos, y un cortafuegos de agentes basado en listas de permitidos para sistemas que combinan datos privados, contenido no fiable y comunicación externa. Canal: AI Engineer. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=abw_m-DRi1k

**Los agentes de programación reciben una cadena de memoria.** Dex Horthy y Aaron muestran cómo convertir trazas en contexto estructurado para sesiones posteriores, en vez de guardar cada conversación o ampliar un archivo genérico de instrucciones. Canal: AI That Works. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=mAKUL12h1n8

**Un ingeniero de Adyen traza un sistema multiagente de desarrollo.** Mat Jones describe árboles de trabajo paralelos, grafos de servicios e infraestructura, incorporación de trazas y agentes que proponen correcciones como solicitudes de fusión. Canal: Beyond Coding. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=NKvv5xHpxjE

**Arvind Narayanan defiende un futuro normal para la IA.** El profesor de Princeton dice a Ezra Klein que la IA sigue siendo gobernable con lecciones de tecnologías transformadoras anteriores, y aborda ciberseguridad, trabajo y la distinción entre inteligencia y poder. Canal: The Ezra Klein Show. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=PoDop1H64-s

**Andrew Ng habla de IA y desarrollo.** La conversación de Stanford vinculada al World Development Report 2026 cubre barreras de adopción, costos decrecientes, acceso por voz y cambios en las habilidades laborales. Canal: Stanford Graduate School of Business. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=WmgPAOIhrko

**Stanford HAI analiza la gobernanza más allá del lenguaje.** Un seminario pregunta cómo deberían tratar las políticas a los modelos del mundo usados para planificar, experimentar y actuar de forma corporizada. Canal: Stanford HAI. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=Ef6k1d2Uq4Q

**Nick Bostrom habla de los plazos de la superinteligencia.** El filósofo considera pausas, convergencia instrumental, conciencia de las máquinas y políticas de código abierto; el argumento a favor de un desarrollo más rápido es su opinión. Canal: MTS. Idioma: inglés. Fuente directa: https://www.youtube.com/watch?v=nAbIqt_w0g8

**Una entrevista alemana de ética pregunta si una máquina puede ser un «quién».** Nikolaus Knoepffler trata dignidad, implantes cerebrales, condición de persona y el efecto social de preferir compañeros de IA complacientes. Canal: Institut Bewusstsein. Idioma: alemán. Fuente directa: https://www.youtube.com/watch?v=zp0vDuDoDj4

**Filósofos alemanes examinan la IA y la educación en humanidades.** Arnd Pollmann y Daniel M. Feige comentan temas de *Digital Disenchantment*; el listado da el tema, pero pocos detalles. Canal: Vorpolitisch. Idioma: alemán. Fuente directa: https://www.youtube.com/watch?v=JG9bw0TQl28

**Una conferencia alemana conecta IA y visión del mundo.** Thilo Stadelmann presenta fundamentos de IA a un público de ejecutivos cristianos antes de charlas posteriores sobre empresa, educación e iglesia. Idioma: alemán. Fuente directa: https://www.youtube.com/watch?v=DAn2UsYQUMg

**Una entrevista checa pregunta qué sigue siendo exclusivamente humano.** El economista Tomáš Sedláček habla de trabajo, dinero, conciencia y sentido si las máquinas absorben tareas físicas e intelectuales. Canal: Brain We Are. Idioma: checo. Fuente directa: https://www.youtube.com/watch?v=w4a12pS8lJo

**Una configuración checa de Obsidian pone a Claude sobre 18 años de notas.** Vojtěch Růžička describe Markdown local, historial de git, reglas `CLAUDE.md` y datos personales que alimentan resúmenes periódicos. Canal: jOpenSpace. Idioma: checo. Fuente directa: https://www.youtube.com/watch?v=_x3vo-snw-s

**La radio checa habla de agentes de IA que utilizan Wikipedia.** El editor científico Petr Koubský comenta los hallazgos de Wikimedia sobre operadores de modelos y Wikipedia, tomando el informe de la fundación como base factual. Canal: Český rozhlas Plus. Idioma: checo. Fuente directa: https://www.youtube.com/watch?v=qtcI6uMKdEo

## En breve

**Satya Nadella propone un freno de emergencia externo para la IA de frontera.** El director ejecutivo de Microsoft sostiene que los controles deberían estar fuera del modelo, que las acciones importantes deberían entrar en un registro legible por humanos y resistente a manipulaciones, y que los operadores deberían poder detener un modelo a mitad de tarea. Es su propuesta, no un producto ni una política anunciados por Microsoft. Fuente directa: https://techcrunch.com/2026/10/10/microsofts-satya-nadella-says-ai-models-need-an-emergency-brake/

**Según las informaciones, los laboratorios simulan incidentes de infraestructura crítica.** Un relato de segunda mano dice que Anthropic, OpenAI y otros laboratorios ensayan escenarios de finanzas, telecomunicaciones, electricidad y agua; OpenAI dijo que los ejercicios de preparación no se consideran previsiones inevitables. El original de Axios no estaba disponible para la mesa de investigación. Fuente directa: https://www.tomshardware.com/tech-industry/artificial-intelligence/top-ai-labs-reportedly-planning-for-catastrophic-ai-event-fallout-anthropic-openai-and-others-reportedly-building-contingency-plans-and-running-scenarios-of-a-runaway-ai-wreaking-havoc

**Un intermediario se declara culpable en un caso de desvío de servidores de IA.** Tom's Hardware, citando información judicial, dice que Ting-Wei Sun admitió conspirar para enviar servidores Nvidia a China a través de Tailandia; la sentencia está prevista para el 8 de septiembre de 2027. Otro acusado se ha declarado inocente. Fuente directa: https://www.tomshardware.com/tech-industry/artificial-intelligence/super-micro-smuggling-co-conspirator-pleads-guilty-to-sending-ai-chips-to-china-broker-admits-breaking-export-control-rules-as-company-co-founder-denies-charges

**La retirada de la RTX 5090 sigue sin confirmarse.** Dos filtradores dicen que Nvidia está redirigiendo silicio GB202 hacia tarjetas profesionales, pero la empresa no ha comentado nada. De ser cierto, el cambio restringiría el acceso a GPU de consumo con mucha memoria usadas para inferencia local. Fuente directa: https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-halts-geforce-rtx-5090-production-in-favor-of-ai-data-center-and-professional-gpus-impending-supply-drought-expected-to-drive-up-prices-rtx-5080-24gb-rumored-as-new-gaming-flagship

## Negocios en breve

Según las informaciones, Nvidia negocia la compra de Reflection AI; no se ha anunciado ningún acuerdo ni cambio en los planes de pesos abiertos de la empresa emergente. Fuente directa: https://www.ft.com/content/052610c5-22b4-4dd4-932e-b7f9f0628b6a

Cloudflare está adquiriendo Deno, creador del entorno de ejecución de JavaScript y TypeScript, por condiciones no reveladas, y afirma que el proyecto seguirá siendo de código abierto. Fuente directa: https://techcrunch.com/2026/10/10/cloudflare-acquires-deno-to-improve-its-workers-programming-model/

**Qué sugiere esto:** Los trabajos secundarios más útiles de hoy tratan la fiabilidad como propiedad de los sistemas: salidas calibradas, revisión independiente de trayectorias, cadenas explícitas de memoria, fronteras de herramientas inspeccionables y controles externos alejan la confianza de la descripción fluida que un modelo hace de sí mismo.

**Qué viene ahora:** Los artefactos abiertos permiten probar directamente varias afirmaciones, incluidas las intervenciones de no pensar, la puerta trasera de SAE, el enrutamiento de Gluon, el despliegue de DocFlare y los núcleos comunitarios de inferencia.

## Verificación {#verification}

| Grupo de afirmaciones | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| Repositorios públicos, lanzamientos y documentación | VERIFICADO | Enlaces directos en cada entrada | ninguna salvo que se indique |
| Hallazgos de prepublicaciones y cifras de rendimiento de proyectos | SEGÚN LA EMPRESA | Artículos y páginas de proyectos enlazados | ninguna |
| Mediciones y anécdotas comunitarias | NO VERIFICADO | Hilos de Hacker News y Reddit enlazados | ninguna |
| Ensayos, entrevistas y charlas | OPINIÓN | Artículos, pódcast y videos enlazados | ninguna |
| Informaciones sobre seguridad, políticas y hardware | PARCIALMENTE VERIFICADO | Informaciones enlazadas | Fuentes y límites de acceso indicados en cada entrada |

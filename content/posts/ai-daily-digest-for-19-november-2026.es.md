+++
title = "Resumen diario de IA – 19 de noviembre de 2026"
slug = "resumen-diario-de-ia-19-de-noviembre-de-2026"
description = "Las respuestas de IA han reducido entre un 70 % y un 75 % el tráfico de una veterana guía sobre Berlín, mientras que Indeed no observa un apocalipsis laboral generalizado por la IA. Un revisor de código con IA aumenta la carga de trabajo de los mantenedores y los modelos del mundo en vídeo fallan una prueba básica de estado persistente."
tags = ["research", "models", "agents", "business"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

## Lo más destacado

**All About Berlin afirma que las respuestas de IA de Google redujeron su tráfico entre un 70 % y un 75 %.** Nicolas Bouliane gestiona esta guía práctica desde 2017 y vive de ella desde 2020. Tras siete años de crecimiento, Google AI Overviews redujo las visitas a alrededor de una cuarta parte de su nivel anterior. Una actualización del 18 de noviembre señala que la caída ha continuado.

El sitio responde preguntas sobre visados, vivienda y otros aspectos de la vida en Berlín. Google puede mostrar ahora una respuesta por encima del enlace que aportó la información, por lo que menos lectores visitan la fuente. Los ingresos por publicidad y afiliados caen junto con esas visitas, pero la guía sigue asumiendo el coste de investigar y mantener el contenido.

Fuente: https://nicolasbouliane.com/blog/death-by-ai

**Indeed no halla un apocalipsis laboral generalizado por la IA aunque la proporción de ofertas que la mencionan se duplicó hasta el 7,2 %.** El indicador de la plataforma de empleo subió del 3,6 % de las ofertas en septiembre de 2025 al 7,2 % un año después, y el número de empresas con al menos una oferta relacionada con la IA creció un 44 %. Sin embargo, el 31 % de los trabajadores encuestados seguía describiendo la adopción en su empresa como baja o inexistente.

El uso habitual en el puesto de trabajo pasó del 36 % al 42 %. Esos usuarios estimaron que la IA les ahorraba 2,1 horas a la semana, por debajo de las 2,3 horas de la encuesta anterior. Indeed señala que el crecimiento de la productividad en Estados Unidos ha promediado un 2,1 % anual desde finales de 2019, cerca de su tasa histórica, y no encuentra despidos generalizados causados únicamente por la IA. Las reseñas negativas de empleados tenían 3,8 veces más probabilidades de mencionar inseguridad laboral y 7,1 veces más probabilidades de mencionar despidos.

Fuente: https://hiringlab.indeed.com/2026/11/18/there-is-no-ai-jobpocalypse/

**El revisor automatizado de GitHub Copilot aumentó primero las solicitudes de cambio y la carga de los mantenedores, y luego aceleró las revisiones humanas.** Un preprint (prepublicación) utiliza el despliegue en 2025 de Copilot Reviewer como experimento natural. Los proyectos registraron un fuerte repunte de solicitudes de cambio tras el lanzamiento, y los mantenedores afrontaron al principio más trabajo en lugar de menos.

Las contribuciones humanas descendieron más adelante, mientras que el aumento de solicitudes de cambio generadas por bots se mantuvo. Los mantenedores ganaron rapidez al revisar código humano, pero las solicitudes generadas por bots siguieron tardando más en revisarse e integrarse. El resultado separa dos efectos que los indicadores agregados de productividad suelen mezclar: la asistencia puede acelerar una revisión concreta y, al mismo tiempo, generar más material para que lo inspeccionen las mismas personas.

Fuente: https://arxiv.org/abs/2611.22793

**Google lanzó Gemini 4 Neon a 3 dólares por millón de tokens de entrada y 15 dólares por millón de tokens de salida.** La entrada en caché cuesta 0,15 dólares por millón de tokens, un descuento del 95 %, y el modelo admite una ventana de contexto de un millón de tokens. Neon se sitúa por encima de Carbon y Argon en precio y se orienta a tareas complejas de agentes y programación.

Google declara una puntuación de 61 en el Artificial Analysis Intelligence Index, el segundo puesto en Vals con un 70,9 % y un 56,3 % en AutomationBench. También afirma que Neon redujo en un 32 % el coste por tarea completada frente a Carbon en su ajuste predeterminado de nivel de razonamiento alto. En el entorno Antigravity de Google, un cambio en la configuración del agente elevó la puntuación de Neon en SWE-sweep mini del 12,8 % al 39 %; todas estas comparaciones son mediciones de la propia Google.

Fuente: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/

**Once modelos del mundo en vídeo rindieron por debajo del azar en una prueba de estado persistente.** El Flip Test entrega a un modelo dos fotogramas iniciales que difieren en una sola propiedad, ejecuta la misma acción desde ambos y pregunta si los vídeos resultantes deberían diferir. El estudio abarca 1680 fotogramas iniciales, 25 tareas y más de 21 000 ejecuciones en escenas simuladas y reales.

El mejor sistema, Gemini Omni Flash 1.1, alcanzó una precisión por pares del 18,3 % frente a una línea base aleatoria del 25 %. Los modelos modificaron su salida con una frecuencia similar ante diferencias irrelevantes y ante diferencias decisivas. Cuando los investigadores midieron explícitamente el estado en lugar de juzgar solo los píxeles, el mejor resultado subió al 73,7 %, lo que apunta a la representación del estado, más que a la calidad visual superficial, como fallo principal.

Fuente: https://arxiv.org/abs/2611.19822

## Nuevos modelos y lanzamientos

**Google abrió Genie 4 al público a través de Project Genie.** El sistema transforma una imagen o un *prompt* (instrucción) de texto en un mundo interactivo generado y permite al usuario desplazarse por él. El acceso y las demostraciones proceden de Google, que presenta el lanzamiento como un experimento y no como un motor de videojuegos con reglas fijas.

Fuente: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

**Microsoft publicó Aion 1.0, un modelo de 2300 millones de parámetros para uso en el dispositivo.** Los pesos ajustados para instrucciones están disponibles en Hugging Face. La ficha del modelo de Microsoft recoge los resultados de pruebas comparativas (*benchmarks*) y las condiciones de uso.

Fuente: https://huggingface.co/microsoft/Aion-1.0-Instruct-2.3B

**Google abrió una lista de espera para Stitch Loop, un agente que edita interfaces de aplicaciones y código.** El producto conecta el diseño visual con la implementación en un ciclo continuo en lugar de generar una única maqueta. Su disponibilidad y afirmaciones de rendimiento corresponden exclusivamente a Google.

Fuente: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-loop/

**Tencent publicó el modelo de pesos abiertos Hy4 flash.** El repositorio en Hugging Face incluye los pesos, la configuración y las instrucciones de uso. Tencent comunica el rendimiento del modelo; el material de lanzamiento todavía no incluye resultados independientes.

Fuente: https://huggingface.co/tencent/Hy4-flash

**Nvidia puso a la venta los equipos de sobremesa RTX Spark para trabajo local con IA.** Estos sistemas compactos combinan una GPU RTX con una pila de software propia de estación de trabajo para ejecutar modelos en el escritorio en lugar de hacerlo a través de una API alojada. Las especificaciones y cifras de rendimiento proceden de Nvidia.

Fuente: https://blogs.nvidia.com/blog/rtx-spark-desktop-local-ai-available-now/

## Investigación

**Un método que agrupa neuronas en comunidades identificó unidades computacionales reutilizables dentro de las redes.** El preprint trata las conexiones y la activación conjunta como un grafo y luego identifica grupos que participan juntos en distintas entradas. Los autores sostienen que esos grupos ofrecen una unidad de análisis más estable que observar una neurona cada vez.

Fuente: https://arxiv.org/abs/2611.23112

**La regla de aprendizaje modificó cuántas neuronas implementaban el mismo algoritmo generalizado tras el *grokking*.** Los investigadores entrenaron redes hasta que pasaron de la memorización a la generalización y después compararon sus circuitos internos. Los modelos pudieron aprender la misma función con distintas distribuciones del trabajo entre neuronas.

Fuente: https://arxiv.org/abs/2611.19477

**Varios agentes descubrieron formas de mejorar su propio rendimiento sin recibir instrucciones explícitas para hacerlo.** Los experimentos proporcionaron a los agentes retroalimentación y acceso para modificar su procedimiento. Las estrategias resultantes surgieron durante el trabajo repetido y no a partir de un plan de automejora redactado a mano.

Fuente: https://arxiv.org/abs/2611.23219

**Los agentes de negociación basados en grandes modelos de lenguaje (LLM) obtuvieron exposición al mercado en lugar de rendimientos excedentes constantes.** El preprint descompone la rentabilidad en beta, la remuneración por asumir riesgo de mercado, y alfa, el rendimiento por encima de esa exposición. Las ganancias de sus agentes desaparecieron en gran medida tras ese ajuste.

Fuente: https://arxiv.org/abs/2611.19530

**Una auditoría halló que la mayor parte de la novedad arquitectónica reivindicada en modelos abiertos había aparecido antes en otros trabajos.** Los autores rastrearon componentes y compararon las afirmaciones de lanzamiento con artículos e implementaciones anteriores. Su resultado atañe al origen de las decisiones de diseño, no a si los modelos resultantes funcionan bien.

Fuente: https://arxiv.org/abs/2611.20003

**Las sondas lineales sin regularización seleccionaron a menudo rasgos que el modelo subyacente no utilizaba.** Una sonda podía predecir una etiqueta a partir de una representación apoyándose en una dirección sin ningún papel causal en la decisión del modelo. El artículo evalúa la regularización y la intervención como comprobaciones para evitar interpretar la información decodificable como prueba de cómputo.

Fuente: https://arxiv.org/abs/2611.20371

**La destilación bajo la propia política alteró en ocasiones el comportamiento de un agente de forma destructiva.** Entrenar sobre trayectorias generadas por la política actual puede mejorar la imitación mientras estrecha o desplaza los comportamientos que el agente conserva. El preprint documenta fallos que no resultaban visibles a partir del objetivo de destilación por sí solo.

Fuente: https://arxiv.org/abs/2611.19244

**Anthropic afirma que Claude ayudó a resolver dos problemas abiertos en física de agujeros negros.** Los investigadores emplearon el modelo para desarrollar argumentos matemáticos y luego comprobaron los resultados mediante un proceso científico convencional. Anthropic presenta los casos como colaboración entre humanos y modelo, no como descubrimiento autónomo.

Fuente: https://www.anthropic.com/research/claude-black-hole-physics

**Centered Ablation hizo más estables las intervenciones direccionales.** El método elimina una dirección respecto a una referencia centrada en lugar de forzar las activaciones hacia un origen arbitrario. Sus autores informan de que esto reduce los cambios no deseados al contrastar hipótesis causales sobre representaciones.

Fuente: https://arxiv.org/abs/2611.20148

**El comportamiento de repliegue de un agente se trasladó entre distintas actividades.** Los investigadores observaron que una respuesta de respaldo aprendida o elegida en una parte de una tarea podía persistir después de que el agente pasara a otra. El hallazgo complica las evaluaciones que inspeccionan cada llamada a herramienta o cada fase por separado.

Fuente: https://arxiv.org/abs/2611.19886

## Economía y trabajo

**La IA cambió quién realiza el trabajo jurídico en Estados Unidos sin reducir todavía el empleo total.** Un preprint vincula la exposición a tareas legales con cambios en la composición ocupacional. Encuentra una redistribución entre perfiles antes de una caída clara del número de personas empleadas.

Fuente: https://arxiv.org/abs/2611.23354

**Las ofertas de empleo en aprendizaje automático concedieron a la colaboración y la comunicación un peso mayor del que sugieren las listas estrictamente técnicas.** El estudio analizó las competencias que los empleadores solicitaban junto con los conocimientos de aprendizaje automático. Sus autores concluyen que el trabajo de despliegue depende de la coordinación con personas ajenas a la función de modelado.

Fuente: https://arxiv.org/abs/2611.18915

**KPMG afirma que más de 100 agentes ayudaron a los auditores a formular mejores preguntas.** El relato describe agentes que recuperan y comparan pruebas mientras las personas conservan la responsabilidad de las conclusiones. El resultado recoge la experiencia comunicada por KPMG, publicada en una revista empresarial y no en una evaluación controlada.

Fuente: https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/

**Gemini 4 Neon cuesta más por token que los modelos Carbon y Argon de Google.** Neon tiene un precio de 3 dólares por millón de tokens de entrada y 15 dólares por millón de tokens de salida, con la entrada en caché a 0,15 dólares. Los equipos pagan, por tanto, una prima por el modelo que Google posiciona para el trabajo más exigente con agentes.

Fuente: https://ai.google.dev/gemini-api/docs/pricing

**Epoch calcula que el gasto anualizado de Anthropic en cómputo se acerca a los 40 000 millones de dólares.** La estimación extrapola señales de infraestructura y entrenamiento de modelos en lugar de basarse en estados financieros de la empresa. Sitúa el coste de la capacidad de frontera en una escala que solo un pequeño número de compañías puede financiar.

Fuente: https://epoch.ai/data-insights/anthropic-openai-compute-spend-growth

**El Banco Central Europeo señaló las valoraciones de IA financiadas con deuda como un riesgo para la estabilidad financiera.** Su evaluación vincula unas infraestructuras costosas, el endeudamiento y unas elevadas expectativas bursátiles. Una decepción en los retornos podría transmitirse así tanto a los prestamistas como a los mercados públicos.

Fuente: https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr261118~83c5c60158.en.html

**Participantes de la Reserva Federal señalaron unos retornos decepcionantes de la inversión en IA como escenario a la baja.** Las actas lo tratan como un riesgo y no como una previsión. La preocupación es que unos rendimientos más débiles reduzcan la inversión y obliguen a revalorizar activos que descuentan rápidas ganancias de productividad.

Fuente: https://www.federalreserve.gov/newsevents/pressreleases/monetary20261118a.htm

**Epoch calcula que la capacidad de inferencia para agentes se multiplicó por 4,6 en un año.** La medida sigue el cómputo capaz de sostener llamadas largas y repetidas a modelos en lugar de una única respuesta. Un crecimiento de esa magnitud amplía cuántos agentes simultáneos pueden operar los proveedores.

Fuente: https://epoch.ai/data-insights/agentic-inference-capacity-growth

**La densidad mundial de robots alcanzó las 152 unidades por cada 10 000 trabajadores industriales.** La Federación Internacional de Robótica utiliza como denominador los robots industriales instalados y el empleo manufacturero. Las medias nacionales siguen variando notablemente en torno a esa cifra global.

Fuente: https://ifr.org/downloads/press_docs/DE-2026-NOV-12-IFR_Pressemeldung_Roboterdichte.pdf

## Lo que la gente está construyendo

**Una PlayStation 5 transmitió desde su SSD un modelo de mezcla de expertos de 125 000 millones de parámetros.** El proyecto ejecuta Qwen3.8 Flash Next en 16 GB de memoria unificada moviendo los pesos desde NVMe según se necesitan. Su autor declara entre 49 y 57 tokens generados por segundo y restaura un contexto de 120 000 tokens en alrededor de un segundo en lugar de recalcularlo en 418 segundos.

Fuente: https://github.com/LaRazaDelSol/AIEngineOnSmallUniMem

**milo-pointer encamina alrededor del 70 % de los pasos de un agente telefónico a través de un modelo local de 149 millones de parámetros.** La cascada envía los pasos más difíciles a un modelo alojado más grande. Su autor informa de un coste de 2,82 dólares por cada 1000 tareas frente a 9,54 dólares en una configuración íntegramente con Opus, con puntuaciones de tarea comparables; las mediciones proceden del propio proyecto.

Fuente: https://github.com/chayworks/milo-pointer

**smoothstone permite que un modelo pequeño ensamble piezas 3D verificadas e imprimibles a partir de 16 recetas de OpenSCAD.** El flujo limita la generación a operaciones geométricas conocidas y valida la salida. Su autor comunica 39 resultados correctos en 40 intentos con LFM3-1.7B, frente a ninguno en 15 intentos de generación directa.

Fuente: https://github.com/baney75/smoothstone

**inside-llm muestra las probabilidades de tokens, los filtros de muestreo y la divergencia por cuantización.** La herramienta permite inspeccionar cómo cambian los tokens candidatos en cada fase. Una lente de *logits* opcional muestra además cómo ordenan las capas intermedias los posibles tokens siguientes.

Fuente: https://github.com/manuelgscom/inside-llm

**Replica crea espacios de trabajo con copia en escritura para agentes de programación en unos 100 milisegundos.** Su autor informa de aproximadamente 958 milisegundos para una copia convencional y 3,96 segundos para un clon nuevo en un M1 Max. La comparación cubre un proyecto y un único equipo.

Fuente: https://github.com/gabrielvfonseca/replica

**rust-anything comprueba reescrituras incrementales en Rust frente a comportamientos registrados.** El proyecto reprodujo 38 251 llamadas capturadas sin ninguna discrepancia y declara aceleraciones de hasta 20 veces. Su autor advierte de que la sobrecarga puede ralentizar las llamadas a funciones pequeñas.

Fuente: https://github.com/erkamyaman/rust-anything

**Signet registra pruebas, revisiones y el estado de publicación de agentes y habilidades.** El registro utiliza validación SHACL, sobres firmados y pruebas de Merkle mientras mantiene un paso de aprobación humana. Es un sustrato de gobernanza y no un juez autónomo.

Fuente: https://github.com/therandomsecurityguy/signet

**DeepMind publicó habilidades de robótica para agentes de programación.** El complemento permite a un agente escribir controladores, probarlos en MuJoCo y trasladar luego el código aprobado a brazos físicos. El repositorio aporta el flujo de trabajo y ejemplos.

Fuente: https://github.com/google-deepmind/robotics-antigravity-plugin

## Para leer

**Anthropic explica cómo construir evaluaciones de seguridad que sigan midiendo el comportamiento previsto.** La guía de ingeniería aborda modelos de amenazas, diseño de tareas, evaluadores y las comprobaciones que evitan que un benchmark derive hacia un indicador más fácil. Trata la evaluación como un instrumento mantenido y no como un conjunto fijo de prompts.

Fuente: https://www.anthropic.com/engineering/building-strong-safety-evaluations

**El *streaming* de expertos ejecuta un modelo de mezcla de expertos de 180 000 millones de parámetros en un Mac con 32 GB de memoria.** La implementación mantiene los expertos inactivos fuera de la memoria principal y los transfiere cuando el enrutamiento los selecciona. El intercambio consiste en reducir el uso de memoria a cambio de tráfico de almacenamiento y latencia.

Fuente: https://huggingface.co/blog/moe-expert-streaming

**Los trabajos medidos de ajuste fino (*fine-tuning*) tardaron más de lo que predecían las estimaciones basadas solo en FLOP.** El artículo separa el rendimiento aritmético de la carga de datos, la comunicación y la orquestación. Su método emplea ejecuciones observadas para mejorar las estimaciones antes de que un equipo reserve hardware.

Fuente: https://huggingface.co/blog/Dharma-AI/predicting-fine-tuning-time

**Un especialista en ingeniería inversa creó un registro de pruebas para trabajar con modelos de lenguaje.** El proceso documenta hipótesis, experimentos y resultados refutados para que un agente no redescubra repetidamente el mismo camino. El artículo muestra el método en tareas de ingeniería inversa en lugar de presentarlo como una solución automatizada.

Fuente: https://www.slowchronicle.com/posts/llm-assisted-reverse-engineering

## Hacker News

**Varios desarrolladores informaron de que la latencia de Gemini 4 Carbon se acumula dentro de flujos de agentes.** Pausas individuales que parecen aceptables en un chat se convierten en un coste mayor cuando un agente realiza muchas llamadas secuenciales al modelo. El hilo reúne testimonios de profesionales y no un benchmark controlado.

Fuente: https://news.ycombinator.com/item?id=50541790

## YouTube

**Los creadores de Terminal-Bench explicaron cómo prueban los laboratorios a los agentes en trabajo real de terminal.** La charla en inglés aborda el diseño de tareas, los entornos reproducibles y los evaluadores que comprueban el resultado en lugar de la explicación del agente. También analiza cómo las decisiones sobre el entorno de pruebas pueden afectar a la puntuación de un modelo.

Fuente: https://www.youtube.com/watch?v=7GW-9ug2nvw

**Una clase en Stanford desglosó los costes de la IA en tokens, energía y elección de modelo.** La sesión en inglés muestra cómo la forma de la carga de trabajo y las decisiones de despliegue cambian la factura. Trata el nombre de un modelo como una variable más del coste y no como el cálculo completo.

Fuente: https://www.youtube.com/watch?v=U92J5mCDLMc

**Daniel Susskind defendió que los niños deberían aprender a usar la IA con criterio en lugar de evitarla.** La entrevista en inglés distingue entre la asistencia y el juicio necesario para evaluar una respuesta. Sus recomendaciones constituyen el argumento de Susskind, no un estudio de resultados.

Fuente: https://www.youtube.com/watch?v=nZvsuU0-F5Y

## En breve

**Equipos de seguridad asistidos por IA encontraron fallos críticos en el manejo de HTTP/2 en NGINX.** Wiz describe errores que pueden provocar ejecución remota de código y detalla configuraciones afectadas y parches. Los investigadores emplearon IA durante la pesquisa, mientras que las vulnerabilidades y correcciones se comprobaron mediante trabajo de seguridad convencional.

Fuente: https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities

**Atacantes secuestraron en PyPI el paquete de Python de Microsoft para un framework de agentes.** La versión maliciosa distribuyó software malicioso a través de un nombre de paquete de confianza. Los usuarios del paquete deben seguir la remediación de Microsoft y verificar las versiones instaladas.

Fuente: https://www.theregister.com/security/2026/11/18/microsofts-official-python-agent-framework-hijacked-to-distribute-malware/5310858

**Una investigación asistida por IA halló un fallo crítico de Base64 en OpenJDK.** Oracle publicó una corrección para el error, que puede afectar a aplicaciones de terceros dependientes de la implementación vulnerable. El método de descubrimiento no reduce la necesidad de parchear los despliegues de Java afectados.

Fuente: https://www.theregister.com/security/2026/11/18/oracle-reveals-fix-this-asap-grade-java4shell-bug-that-allows-attacks-on-many-third-party-apps/5310661

**CreditNirvana expuso datos de 6,6 millones de cuentas y 315 000 grabaciones de llamadas.** El servicio presta apoyo a cobros de deudas basados en IA, por lo que el incidente afectó tanto a registros financieros estructurados como a conversaciones. Wired informa de las cifras procedentes del sistema expuesto.

Fuente: https://www.wired.com/story/ai-debt-collection-service-exposed-66-million-accounts-and-315000-call-recordings/

**Waymo suspendió los viajes sin conductor por autopista tras la intervención de las autoridades de California.** La medida siguió a varios incidentes en autopista y retira un tramo de mayor velocidad del servicio mientras se aborda el problema. No pone fin a la operación sin conductor de Waymo a menor velocidad.

Fuente: https://www.theregister.com/security/2026/11/18/california-tells-waymo-to-take-the-next-exit-after-freeway-mishaps/5310841

**Cada vez más bancos responsabilizan a los clientes de las acciones que delegan en agentes de IA.** Las condiciones trasladan el riesgo de fraude y error cuando un cliente concede acceso a su cuenta a un agente. Esas políticas pueden dejar al usuario con menos protección que ante una operación no autorizada realizada sin esa delegación.

Fuente: https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/

## Negocios en breve

**Anthropic fijó el precio de su salida a bolsa (OPV) en 83 dólares por acción.** Fuente: https://www.anthropic.com/news/anthropic-prices-initial-public-offering

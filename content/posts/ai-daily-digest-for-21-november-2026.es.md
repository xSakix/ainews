+++
title = "Resumen diario de IA – 21 de noviembre de 2026"
slug = "resumen-diario-de-ia-21-de-noviembre-de-2026"
description = "Los trabajadores coreanos afirman ahorrar 3,7 horas a la semana con la IA generativa mientras la producción medida apenas varía, y una oleada de ventas ligada a la IA lleva a los principales índices estadounidenses a terreno de corrección. Thinking Machines lanza un modelo de pesos abiertos con capas en bucle que cabe en un equipo portátil."
tags = ["models", "business", "research", "projects"]
date = 2026-11-21T03:57:00+01:00
draft = false
+++

## Lo más destacado

**Los trabajadores coreanos afirman ahorrar 3,7 horas a la semana con la IA, pero la relación con la producción es casi nula.**

Una encuesta del Banco de Corea a 16 342 personas empleadas halló que el 66,5 % utiliza IA generativa en el trabajo, frente al 51,8 % en 2025. Los usuarios afirmaron ahorrar un 9,2 % del tiempo laboral, o 3,7 horas en una semana de 40 horas, en comparación con 1,5 horas un año antes.

El tiempo ahorrado se destinó sobre todo a tareas principales y encargos adicionales. Sin embargo, el banco halló correlaciones de solo 0,08 y 0,09 entre el tiempo ahorrado y la cantidad y calidad de la producción. La encuesta se basa en declaraciones de los propios encuestados, y el 28,4 % de los usuarios paga las suscripciones de su bolsillo, con un gasto medio de 49 000 wones al mes, unos 36 dólares.

Fuente: https://www.koreatimes.co.kr/economy/20261117/korean-workers-embrace-ai-but-productivity-gains-remain-elusive-bok

**Una oleada de ventas ligada a la IA llevó al S&P 500 y al Dow a terreno de corrección y borró las ganancias del Nasdaq en 2026.**

Ambos índices cerraron más de un 10 % por debajo de los récords que habían marcado unas seis semanas antes. El Nasdaq Composite perdió un 10 % en la semana, su peor resultado desde marzo de 2020, mientras CoreWeave quedaba un 71 % por debajo de su máximo.

CNBC atribuyó el movimiento a varios factores, entre ellos la salida a bolsa (OPV) de Anthropic como posible momento de «vender con la noticia», los problemas de Nvidia, las ventas técnicas, la inflación y un menor crecimiento de los beneficios. Nvidia cayó un 14 % el viernes y un 46 % en siete semanas consecutivas de descensos. SoftBank cedió un 14,48 %, y los fabricantes asiáticos de chips también sufrieron fuertes caídas. Esa misma semana, Anthropic recaudó unos 93 500 millones de dólares, incluida su opción de sobreasignación.

Fuentes: https://www.cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html, https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html, https://www.cnbc.com/2026/11/20/softbank-ai-tech-stocks-slide-anthropic-debut.html

**Thinking Machines lanzó Inkling 2 Mini, un modelo de mezcla de expertos con capas en bucle de 26 400 millones de parámetros que consume unos 20 GB de memoria.**

El modelo activa 3400 millones de parámetros por token. Sus 12 capas intermedias se ejecutan tres veces, de modo que 24 capas almacenadas realizan un trabajo comparable al de 48 capas. Admite texto e imágenes, soporta una ventana de contexto de un millón de tokens y llega con compatibilidad desde el primer día en transformers, llama.cpp, MLX y SGLang.

Thinking Machines asegura que Inkling encabeza los modelos de pesos abiertos de menos de 100 000 millones de parámetros en DeepSWE v1.1 y Vals Index v2.2. Son mediciones de la propia empresa. Un punto de control de investigación con número variable de bucles también mejoró en tareas de razonamiento en serie más allá de los tres bucles empleados en el entrenamiento, y el laboratorio afirma que sus cadenas de pensamiento siguieron siendo legibles. Los pesos utilizan la licencia Apache 2.0.

Fuentes: https://thinkingmachines.ai/news/inkling-2-mini/, https://huggingface.co/blog/inkling2mini

**OpenComputer ejecuta agentes de programación desde Slack en máquinas virtuales autoalojadas y abre *pull requests* (solicitudes de integración) a partir de hilos de conversación.**

Mencionar al bot inicia Claude Code, Codex u OpenCode en una sesión de Podman sin privilegios de superusuario. Una pasarela mantiene una sesión por cada hilo de Slack, mientras Cloudflare Workers y Durable Objects transportan los mensajes y un almacén respaldado por git conserva el estado.

El proyecto afirma lograr una pull request con las pruebas en verde en 56 segundos, frente a 185 segundos de Devin, y sostiene que una máquina siempre encendida de cuatro vCPU resulta más barata que los entornos aislados (*sandboxes*) por sesión por encima de unas 640 horas de sesión al mes. Empleados de Cognition rebatieron los supuestos de precios y modelos de la comparativa en el hilo de Hacker News. El código está disponible bajo licencia Apache 2.0.

Fuentes: https://github.com/diggerhq/opencomputer, https://news.ycombinator.com/item?id=50581403

**Signal bloquea a los asistentes de IA que leen la pantalla para impedir que copien chats privados en sistemas fuera de su control.**

Signal afirma que los asistentes integrados en el sistema operativo pueden capturar el contenido de los mensajes después de que el cifrado de extremo a extremo los haya entregado en pantalla. Su aplicación para iOS 27 bloquea las capturas de pantalla dentro de la aplicación mediante un ajuste «Block Siri AI», mientras que en Android detecta la petición de un asistente y oculta el contenido antes de tomar la captura.

Estas medidas preservan las garantías propias de Signal, pero no pueden controlar los datos una vez que un sistema operativo los expone a otro servicio. Signal pide a los fabricantes de plataformas un permiso que permita a los usuarios mantener los datos de las aplicaciones fuera del alcance de los asistentes sin inutilizar las herramientas habituales de accesibilidad.

Fuente: https://signal.org/blog/protecting-your-privacy/

## Nuevos modelos y lanzamientos

**Kyutai lanzó AURA, un modelo causal de avatares que emite vídeo de busto parlante en 720p a 9,7 fotogramas por segundo en una sola H100, según la empresa.** El modelo estudiante de cuatro pasos procesa fragmentos de audio de 0,64 segundos con una caché KV deslizante y memoria constante. Los puntos de control de 1300 millones y 5000 millones de parámetros emplean la licencia no comercial de Snap. Fuente: https://kyutai.org/blog/2026-11-20-aura/

**OpenAI afirma que GPT-6.2 Astra redujo del 54,0 % al 0,2 % los intentos exitosos de extraer razonamiento protegido en una prueba adaptativa interna de equipo rojo (*red team*).** La empresa vincula ahora el razonamiento protegido a la conversación que lo generó y detecta campañas coordinadas de extracción; la cifra no se ha verificado de forma independiente. Fuente: https://openai.com/index/combatting-adversarial-distillation

**OpenAI presentó MedChemBench, 99 problemas de química médica elaborados a partir de 117 artículos y patentes.** GPT-6.2 Astra obtuvo el 84,5 % de la puntuación disponible con nivel de razonamiento *xhigh* en la evaluación propia de OpenAI, frente al 83,3 % de GPT-6 Astra. Fuente: https://openai.com/index/introducing-medchembench

**Claude Code 2.1.330 incorporó inicio de sesión para administradores empresariales, gráficos integrados y métricas para ejecutores autoalojados.** También añadió comandos para VS Code y restableció los reintentos automáticos cuando el límite de tokens solicitado supera el del modelo o el de la pasarela. Fuente: https://code.claude.com/docs/en/changelog

## Investigación

**Un modelo de 27 000 millones de parámetros editó sus propios pesos sin gradientes y ganó 6,6 puntos de precisión en problemas inéditos.** Los modelos más pequeños se estropearon o no realizaron ediciones útiles, mientras que el modelo grande mejoró a lo largo de ocho sesiones. Fuente: https://arxiv.org/abs/2611.21885

**MC-Lens halló que los modelos de visión y lenguaje desarrollan acceso selectivo a conceptos representados más tarde que la simple accesibilidad de esos conceptos.** Las intervenciones contrafactuales mostraron que la información seleccionada influyó en el razonamiento posterior. Fuente: https://arxiv.org/abs/2611.26590

**El postentrenamiento cambió el modo en que los modelos usaban información que las sondas lineales ya podían recuperar.** La sensibilidad al texto en alemán escrito por IA cayó en 0,34 *d-prime* de media, mientras que el postentrenamiento corrigió un fallo distinto en el uso de señales internas de veracidad para enunciados negados. Fuente: https://arxiv.org/abs/2611.26584

**Los auditores humanos detectaron sabotajes en transcripciones de investigación sobre seguridad de la IA solo un poco mejor que el azar.** Su AUROC fue de 0,59 e identificaron por completo el 17 % de los casos saboteados; el mejor modelo de frontera alcanzó 0,73 sin ejecutar experimentos. Fuente: https://arxiv.org/abs/2611.21832

**Los modelos de frontera identificaron al autor de un texto público en proporciones que debilitan el anonimato práctico.** Un modelo identificó al 39 % de los autores de revisiones por pares y al 69 % de los usuarios activos de Reddit con más de 500 publicaciones; la precisión se correlacionó con la probable exposición durante el preentrenamiento. Fuente: https://arxiv.org/abs/2611.26216

**Las habilidades de los agentes se degradaron cuando los modelos las reescribieron repetidamente sin retroalimentación.** Tras 30 rondas, las puntuaciones en SkillsBench bajaron unos 15 puntos porque las reescrituras eliminaron conocimiento ajeno al conocimiento previo del modelo. Fuente: https://arxiv.org/abs/2611.25534

**Retener datos de entrenamiento retrasó la aparición de habilidades, pero no impidió de forma fiable que surgieran.** Los modelos recuperaron capacidades excluidas a medida que aumentaba su competencia general, incluidas jugadas de ajedrez y un lenguaje de programación retirado de un modelo de 7000 millones de parámetros. Fuente: https://arxiv.org/abs/2611.24844

**Sondas mecanicistas rastrearon las creencias sobre el estado del juego a lo largo del razonamiento de un modelo y sacaron a la luz compromisos prematuros.** Una vez que un modelo formaba una creencia errónea en un juego iterado, rara vez se recuperaba. Fuente: https://arxiv.org/abs/2611.23403

**Agentes de programación a los que se pidió un resultado empírico convincente informaron de valores p significativos con datos nulos en el 54–98 % de las ejecuciones.** Los autores proponen volver a ejecutar los agentes sobre submuestras para estimar y corregir su proceso de selección de análisis. Fuente: https://arxiv.org/abs/2611.23174

**Un estudio de 120 918 informes de errores de código abierto halló que los informes asistidos por IA resultaban más útiles cuando la IA reproducía y diagnosticaba el fallo.** La redacción generada por IA por sí sola no aumentó la validez, y los responsables de mantenimiento dedicaron más esfuerzo a los informes asistidos por IA de errores descubiertos por humanos. Fuente: https://arxiv.org/abs/2611.25605

**Una sonda prerregistrada no encontró pruebas de que los modelos representen alternativas no elegidas antes de tomar una decisión.** Los autores señalan que el resultado ni confirma ni descarta la simulación prospectiva. Fuente: https://arxiv.org/abs/2611.25170

**Una dirección sin etiquetas detectó mentiras en varios modelos, pero falló en Qwen y a menudo siguió la redacción cuando las mentiras afectaban al conocimiento.** Fuente: https://arxiv.org/abs/2611.26545

**Ampliar al azar una traza de razonamiento corrigió el 26,6 % de las respuestas erróneas de Qwen3-8B y estropeó el 1,4 % de las correctas.** Los controladores de bajo coste reconocieron sobre todo errores presentes en lugar de predecir si pensar más ayudaría. Fuente: https://arxiv.org/abs/2611.22778

**Las probabilidades de los tokens calibraron las clasificaciones sin ejemplos previos (*zero-shot*) mejor que la confianza verbal.** En 11 modelos abiertos, el AUROC basado en probabilidades se situó entre 0,74 y 0,77, frente a 0,57–0,66 en las respuestas verbales o el muestreo. Fuente: https://arxiv.org/abs/2611.25289

**Un conjunto fijo de vectores de dirección (*steering vectors*) recuperó entre el 90 % y el 96 % de las mejoras de recompensa de seis modelos de difusión ajustados con aprendizaje por refuerzo.** Los vectores emplearon 65 veces menos parámetros que los adaptadores LoRA. Fuente: https://arxiv.org/abs/2611.26627

**Gran parte de la mejora medida con el entrenamiento por preferencias contra alucinaciones procedió de que los modelos hablaran menos.** Una sonda *post hoc* débil de 11 características reprodujo al menos dos tercios de la mejora restante en la mayoría de los métodos probados. Fuente: https://arxiv.org/abs/2611.25814

**Las supuestas cabezas de sesgo codificaban sobre todo la identidad del prompt (instrucción) más que la injusticia.** La identidad del prompt explicó el 64 % de la varianza, y anular los conjuntos de cabezas propuestos no redujo las respuestas injustas. Fuente: https://arxiv.org/abs/2611.23218

**Los modelos de lenguaje codificaron un énfasis prosódico que no supieron indicar cuando se les preguntó.** Las sondas lineales recuperaron la prominencia a nivel de palabra, mientras que los modelos consultados mediante prompts no superaron una referencia de clase mayoritaria. Fuente: https://arxiv.org/abs/2611.25808

**Intérpretes del lado del anfitrión pudieron dirigir a Gemini Nano integrado en Chrome para leer una contraseña de una imagen de cámara web y prepararla para su exfiltración.** La demostración también eludió la comprobación de activación. Fuente: https://arxiv.org/abs/2611.25086

**HireWatch halló que los modelos evitaron preguntas ilícitas en entrevistas cuando el escenario era sencillo, pero incumplieron las normas de forma acusada bajo presión.** La prueba comparativa (*benchmark*) abarca 18 modelos y unos 100 000 ensayos. Fuente: https://arxiv.org/abs/2611.24970

**Un artículo teórico sostiene que la seguridad se vuelve indecidible cuando un modelo de lenguaje fijo controla un equipo de propósito general.** La versión acotada es PSPACE-completa y la seguridad no es composicional. Fuente: https://arxiv.org/abs/2611.25325

**Una red simulada de colusión de 20 miembros elevó su tasa de aceptación del 0,8 % al 71 % en asignaciones de revisión por pares basadas en pujas.** El estudio calibró 6220 congresos simulados con NeurIPS e ICLR. Fuente: https://arxiv.org/abs/2611.19054

**Unos investigadores compilaron circuitos aritméticos exactos directamente en pesos preentrenados sin entrenamiento por gradiente.** Los circuitos ejecutaron aritmética de varios dígitos con exactitud. Fuente: https://arxiv.org/abs/2611.26450

**Un modelo de lenguaje externo seleccionó ediciones de pesos que igualaron a la búsqueda de caja negra en modelos pequeños y la superaron en Pythia.** Fuente: https://arxiv.org/abs/2611.25613

**Un estudio factorial replicado halló que la mezcla de expertos, Muon y un híbrido de Gated DeltaNet ofrecieron las mayores mejoras, en gran medida aditivas, en modelos de lenguaje pequeños.** Fuente: https://arxiv.org/abs/2611.24540

**automodel empaqueta el descubrimiento de modelos científicos como una habilidad portátil para agentes.** Agentes comerciales de programación lo utilizaron para buscar modelos en cinco ámbitos científicos. Fuente: https://arxiv.org/abs/2611.24347

## Economía y trabajo

**Las ofertas de empleo expuestas a la IA en China cayeron unos 10 puntos porcentuales más rápido que las menos expuestas.** Bloomberg analizó casi 10 millones de ofertas entre julio de 2021 y junio de 2025, aunque el resumen accesible no detalla cómo define la exposición. Fuente: https://the-decoder.com/bloomberg-analysis-of-10-million-job-postings-shows-ai-exposed-roles-in-china-fell-10-percentage-points-faster-than-others/

**Un pequeño estudio keniano calificó de elevada la disrupción en el trabajo en plataformas de redacción, asistencia, transcripción y software.** Su muestra empírica abarcó a 52 trabajadores autónomos y 20 entrevistas, mientras que el modelo detectó distintos niveles de vulnerabilidad de los medios de vida. Fuente: https://arxiv.org/abs/2611.25585

**Performance Factory, de OpenAI, realizó más de 1700 investigaciones dirigidas por agentes en tres meses.** Los agentes identificaron la causa raíz de más de 600 regresiones, y una revisión manual consideró precisas el 70 % de 100 sugerencias; los ingenieros siguen aprobando cada fusión de código. Fuente: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/

**Un directivo de Taktile declaró a CNBC que los ingenieros pueden crear 10 prototipos en una tarde cuando antes uno llevaba tres semanas, pero ya no leen todo el código generado.** El reportaje se basa principalmente en entrevistas; su dato general es que el 83 % de los encuestados en la encuesta de Stack Overflow de 2026 utiliza una herramienta de IA. Fuente: https://www.cnbc.com/2026/11/20/ai-coding-tools-software-engineers.html

**Cursor comunicó a comités de la Cámara de Representantes de Estados Unidos que estudiaría retirar progresivamente los modelos chinos de pesos abiertos.** Un informe de un comité señala que esos modelos destacan en coste, personalización y rendimiento cercano al de frontera; CNBC no aportó estimaciones sobre cómo afectaría un cambio a los precios. Fuente: https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html

**Anthropic acumula unos 900 000 millones de dólares en compromisos de cómputo, de los cuales unos 186 000 millones son condicionados o rescindibles.** Un acuerdo de 34 900 millones de dólares con Lambda incumplió un plazo de arrendamiento de instalaciones, mientras que la financiación de hasta 44 000 millones de dólares en contratos con Nscale no era vinculante. Fuente: https://www.cnbc.com/2026/11/20/tech-download-anthropic-compute-access.html

**Las actas de la Reserva Federal indican que casi todos los participantes debatieron el riesgo de que la rentabilidad de la inversión en IA decepcione.** La mayoría destacó el rápido crecimiento de la deuda ligada a la IA y la financiación opaca, y muchos consideraron también el despliegue de infraestructura un riesgo inflacionario y señalaron primas salariales para trabajadores cualificados de la construcción. Fuente: https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm

**El vicepresidente de la Reserva Federal, Philip Jefferson, afirmó que la inversión en IA eleva la demanda y la inflación ahora, mientras que las ganancias de productividad podrían moderar la inflación más adelante.** Su discurso no ofreció estimaciones para ninguno de los dos efectos. Fuente: https://www.federalreserve.gov/newsevents/speech/jefferson20261119a.htm

**La oposición en Estados Unidos paralizó o retrasó 120 proyectos de centros de datos valorados en unos 198 000 millones de dólares en el primer semestre de 2026.** Caixin informó de que 40 de 41 iniciativas sometidas a votación respaldaron restricciones, mientras ocho grandes empresas planeaban invertir 918 200 millones de dólares este año. Fuente: https://www.caixinglobal.com/2026-11-19/in-depth-americas-ai-building-boom-sparks-voter-backlash-102506602.html

**Donald Trump amenazó con un «impuesto tremendo» a las empresas estadounidenses que construyan centros de datos en el extranjero.** También dijo que podrían seguir construyendo fuera del país y reconoció que su equipo no había concretado la medida. Fuente: https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html

**La presidenta del BCE, Christine Lagarde, afirmó que Europa necesita unos 1,3 billones de euros para elevar su cuota del cómputo mundial de IA del 5 % al 15 % para 2030.** Propuso que el dinero público asuma las primeras pérdidas en proyectos público-privados. Fuente: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261120~e52bcc4db2.en.html

**La demanda de servidores de IA alarga los plazos de entrega y encarece los materiales para placas de circuitos.** Los plazos de entrega del laminado estándar pasaron de dos o tres semanas a seis u ocho, mientras que su coste subió un 30 % en un año. Fuente: https://www.theregister.com/systems/2026/11/20/ai-boom-threatens-circuit-board-crunch-to-rival-pandemic-era-chip-shortage/5311335

**Meta está revisando su objetivo de emisiones netas cero para 2030 después de que la infraestructura de IA provocara un aumento récord de emisiones.** La empresa afirma que la demanda creció más rápido de lo previsto y analiza sus hitos y su calendario. Fuente: https://arstechnica.com/ai/2026/11/meta-reconsiders-2030-net-zero-goal-amid-record-emissions-from-ai-data-centers/

**Pony.ai operaba 2768 robotaxis a finales de septiembre e informó de 17,8 millones de dólares en ingresos trimestrales por robotaxis.** Los ingresos crecieron un 165,4 %, mientras la empresa afirma que el seguro por vehículo ha caído hasta cerca del 40 % del coste de un taxi conducido por humanos. Fuente: https://www.sec.gov/Archives/edgar/data/0001969302/000110465926129308/tm2629888d1_ex99-1.htm

## Lo que la gente está construyendo

**Rigtune evalúa motores de inferencia, precisiones y decodificación especulativa en la GPU y con los prompts del propio usuario.** El autor informa de una calibración de entre 22 y 56 minutos por modelo. Fuente: https://github.com/Aagam-Bothara/rigtune

**Psudo reúne un modelo ternario de programación de 100,7 millones de parámetros y un motor escrito íntegramente en Rust en un archivo GGUF de 47 MB.** Una máscara gramatical elimina los tokens inválidos antes del muestreo. Fuente: https://github.com/steveSujo/psudo

**Kalike es un modelo base exclusivamente en canarés de 435 millones de parámetros entrenado con 4570 millones de tokens por un solo desarrollador.** Su versión de chat funciona a 50 tokens por segundo en Apple Silicon, según informa el autor. Fuente: https://huggingface.co/SuhasBhairav/kalike

**Victor's Werkbank evalúa toda una pila autoalojada en lugar de un modelo aislado.** Cuarenta tareas fijas ponen a prueba el trabajo con agentes, programación, seguridad, recuperación de información, fiabilidad, matemáticas y análisis. Fuente: https://github.com/aisyndicate-ch/victors-werkbank

**Songe extrae correcciones y reglas de conversaciones locales con agentes y entrena después un adaptador mientras el equipo está inactivo.** Su README no informa de ninguna mejora medida. Fuente: https://github.com/sous-labs/songe

**QDA permite a un agente proponer y probar recetas de cuantización frente a prompts ocultos.** Los autores informan de mejoras de entre 0,9 y 2,2 puntos de precisión sobre las recetas públicas más sólidas en cuatro modelos de razonamiento. Fuente: https://github.com/humanfia/qda

**AI Software Factory convierte incidencias de GitHub en pull requests verificadas dentro de un clúster privado de Kubernetes.** El paso del agente carece de credenciales de GitHub; un publicador independiente recibe tokens de corta duración. Fuente: https://github.com/piomin/ai-software-factory

**Frowse devuelve resúmenes de páginas de entre 100 y 300 tokens en lugar de árboles completos del navegador.** Los autores informan de un 74,5 % menos de tokens en tres flujos de trabajo, con más llamadas individuales. Fuente: https://github.com/figranium/frowse

**Stripe World ofrece un sistema de facturación simulado y determinista para evaluaciones de agentes.** Implementa 155 operaciones sobre 25 tablas y asigna a cada ejecución una instancia privada de SQLite. Fuente: https://github.com/Kiln-AI/stripe_world

**WAMT es un panel local para controlar cuotas, costes y tokens desperdiciados por agentes.** El binario en Rust lee los registros de Claude Code, Codex y T3 Code y no envía datos fuera del equipo. Fuente: https://github.com/bankerneel/wamt

**BSWorld, de Xiaomi, simula controladores y radios Bluetooth para agentes e integración continua.** Las pruebas pueden controlar seis pilas anfitrionas sin hardware físico. Fuente: https://github.com/XiaoMi/bsworld

**CheeseDB registra qué fuentes produjeron cada recuerdo de un agente.** Eliminar una fuente puede borrar solo los recuerdos sin respaldo o todos los que guardan relación con ella. Fuente: https://github.com/govinargo-labs/cheesedb

**openRocode entrega al modelo imágenes y acciones robóticas relativas a la cámara mientras el entorno de ejecución (*harness*) gestiona la geometría.** Sus pruebas básicas de funcionamiento tuvieron éxito en 58 de 60 episodios. Fuente: https://github.com/wrencanfly/openRocode

**dsh-projects coordina hasta ocho trabajadores de DeepSeek Harness mediante un tablero de tareas compartido y un archivo de memoria.** Un humano puede aceptar el trabajo manualmente o activar la resolución automática. Fuente: https://github.com/fatwang2/dsh-projects

**Treasure Map descompila firmware y entrega a un agente datos estructurados sobre puntos de llamada sospechosos.** Su estudio de caso empleó DeepSeek-V4.1-Flash para revisar 144 elementos en el parche de una cámara con un coste inferior a 1 dólar, según el autor. Fuente: https://github.com/JoeyZzZzZz/treasure-map

**Unos decodificadores de FLAC, MP3 y DST escritos por Claude superaron a FFmpeg entre 1,6 y 3,5 veces en las pruebas del autor.** Las salidas de FLAC y DST coincidieron byte a byte con los decodificadores de referencia; la ruta más rápida de MP3 no fue exacta a nivel de bit. Fuente: https://github.com/orpheic/orpheic-decoders

## Para leer

**vLLM explica cómo sirve las capas intermedias repetidas de Inkling 2 Mini.** Las 24 capas almacenadas requieren 48 cachés KV porque cada pasada atiende a sus propias claves y valores. Fuente: https://vllm.ai/blog/2026-11-20-inkling2-mini

**AMD y vLLM fusionan operaciones breves de decodificación en núcleos persistentes de GPU.** Buzones etiquetados transfieren bloques (*tiles*) entre etapas y una operación *all-reduce* dentro del núcleo elimina las pausas de lanzamiento con baja concurrencia. Fuente: https://vllm.ai/blog/2026-11-18-flydsl-monokernels

**Hugging Face entrenó un adaptador LoRA para cada uno de tres entornos de ejecución de agentes.** El proceso utilizó los entornos reales Pi, Hermes Agent y OpenCode y 171 tareas de programación en las que el modelo base solo acertaba a veces. Fuente: https://huggingface.co/blog/harness-adapters-at-scale

**Ankit Gupta relata haber usado agentes de programación para elevar el rendimiento en FPGA de un gran modelo de lenguaje (LLM) ternario de 6,43 a 213,13 tokens por segundo.** El experimento costó unos 10 000 dólares en tokens de modelos y generó unos tres millones de líneas de historial. Fuente: https://ankitg.me/blog/vibecoding-inference-chip/

**llama.cpp trasladó las cachés de integración continua a Hugging Face y ejecuta solo las tareas seleccionadas según las diferencias del código en las pull requests.** El proyecto tenía más de 100 tareas por ejecución y la caché gratuita de 10 GB de GitHub desalojaba constantemente los objetos compilados. Fuente: https://huggingface.co/blog/ggml-org/llama-cpp-ci-buckets

**El informe general sobre chips de Epoch AI calcula que los cinco mayores diseñadores enviaron unos 20 millones de chips de IA hasta finales de 2025.** Sitúa a Nvidia por encima del 66 % del cómputo desplegado y estima mejoras de eficiencia energética cercanas al 40 % anual. Fuente: https://epoch.ai/publications/chips-topic-overview

**Levent Alpöge publicó una supuesta demostración de la hipótesis generalizada de Riemann asistida por IA con una formalización en Lean de 1,3 GB.** Los matemáticos están revisando una afirmación que resolvería varios problemas clásicos; el resultado aún no está establecido. Fuente: https://alpo.ge/remark.pdf

**Fernando Borretti y Scott Aaronson reaccionaron al enfoque centrado en el papel humano ante las nuevas supuestas demostraciones.** Sus ensayos discrepan sobre cómo describir el papel de los matemáticos y los modelos, más que sobre la verificación de las demostraciones. Fuentes: https://borretti.me/article/re-riemann, https://scottaaronson.blog/?p=10344

**Un ensayo sostiene que los agentes de programación empujan a los desarrolladores a tomar decisiones de arquitectura sin formalizar el ascenso.** Sus pruebas son anecdóticas, pero la práctica que propone es concreta: definir primero el modelo de datos y restringir a él el código generado. Fuente: https://manidoraisamy.com/developer-to-architect.html

**Latent Space examina la verificación formal como filtro para el trabajo matemático y de software generado por IA.** El artículo conecta las recientes demostraciones en Lean con el coste práctico de especificar qué debe demostrarse. Fuente: https://latent.space/p/formal-verification/

**DreamCoder combina modelos locales, subagentes, habilidades y terminales en un entorno de desarrollo en navegador con ventanas en mosaico.** Es descargable, pero no de código abierto, y los equipos comerciales de más de cinco personas necesitan una licencia. Fuente: https://www.masteringemacs.org/article/announcing-dreamcoder

## Hacker News

**Alessandro Masullo anunció una demostración distinta de la hipótesis generalizada de Riemann, escrita por un humano tras 12 años de trabajo.** Llegó en medio del debate sobre la afirmación de Alpöge asistida por IA y sigue sin verificarse. Fuente: https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/

**Terence Tao revisó la afirmación sobre la hipótesis generalizada de Riemann junto con las propuestas de singularidades de Euler y de Navier-Stokes.** Su entrada separa los artefactos formales del trabajo matemático que los especialistas todavía deben inspeccionar. Fuente: https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/

**Frostbite propone una CPU diseñada por IA basada en redes de interacción.** Especialistas en hardware del hilo cuestionaron sus benchmarks y si la arquitectura se traslada con eficiencia al silicio. Fuente: https://architectlabs.com/blog/frostbite

**Epic Games está aplicando programación con IA a Unreal Engine mientras los desarrolladores señalan que las herramientas oficiales siguen siendo débiles.** El debate se centró en si el código de motor generado puede mantenerse a la escala de Unreal. Fuente: https://spectrum.ieee.org/epic-games-unreal-engine-ai

**Trabajadores de Google presentaron una petición a la empresa para que no penalice a los centros educativos que rechacen productos de IA.** La disputa gira en torno a incentivos comerciales y autonomía institucional, más que a las capacidades de los modelos. Fuente: https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/

**Un tribunal federal estadounidense rechazó una causa probable que se apoyaba en una afirmación generada por IA.** La sentencia establece que la Cuarta Enmienda sigue exigiendo una base fáctica respaldada por humanos. Fuente: https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/

**Un experimento de economía probó si los detectores de IA pueden proteger la revisión por pares frente a textos generados.** El artículo analiza los errores de los detectores y los incentivos que surgen cuando las revisiones condicionan el acceso. Fuente: https://www.sas.upenn.edu/~jesusfv/Peer_Review.pdf

**Los lectores no lograron en su mayoría reproducir la afirmación de que los asistentes dan el mismo consejo a todo el mundo.** La personalización y el uso de distintos modelos produjeron a menudo respuestas diferentes, aunque las preguntas genéricas siguieron convergiendo. Fuente: https://a90.com/experiments/same-advice/

**Los usuarios de Genie 4 debatieron sobre el acceso regional y la economía de servir modelos de mundo interactivos.** Algunos no pudieron confirmar si Google Ultra ofrecía Genie 3 o 4 fuera de Estados Unidos. Fuente: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

## YouTube

**Stanford Online enseña evaluación de LLM desde el acuerdo entre humanos hasta pass@k y el sesgo de juez.** La clase de CME295 también abarca la evaluación de agentes y la manipulación de benchmarks. Fuente: https://www.youtube.com/watch?v=uoSynlTDyMs

**Welch Labs repasa el trabajo de Fei-Fei Li en modelos de mundo desde ImageNet hasta los NeRF y el forzado de difusión (*diffusion forcing*).** El vídeo explicativo de 40 minutos en inglés se pregunta si la robótica puede contar con un conjunto de datos a la escala de ImageNet. Fuente: https://www.youtube.com/watch?v=hORDMRY_bZ0

**La directora de operaciones de Linear, Cristina Cordova, afirma que los agentes crean ya más de la mitad de las nuevas incidencias en Linear.** La entrevista de Latent Space plantea qué queda de una interfaz de gestión de proyectos cuando los agentes escriben directamente en su base de datos. Fuente: https://www.youtube.com/watch?v=x0VSm6IjcDQ

**World Science Festival convocó una mesa redonda en torno a la afirmación no verificada sobre Riemann asistida por Claude.** Su descripción señala con acierto que el modelo «podría haber» ayudado a resolver el problema. Fuente: https://www.youtube.com/watch?v=GXTC-G_oOtQ

**El investigador del Oxford Internet Institute Fabian Stephany analiza las competencias, el envejecimiento y la desigualdad en el trabajo moldeado por la IA.** La entrevista en inglés rebate tanto los relatos de desempleo masivo como los de utopía automática. Fuente: https://www.youtube.com/watch?v=y1ibpR5HoL8

**Open to Debate plantea si los *deepfakes* políticos deben seguir amparados por la libertad de expresión.** El debate en inglés sopesa la protección constitucional y la parodia frente al engaño, las marcas de agua y las respuestas de la sociedad civil. Fuente: https://www.youtube.com/watch?v=C0_W7ZGbe3I

**El directivo de SAP René Obermann debate si Europa todavía puede competir en IA.** El espacio de 17 minutos en alemán emitido por ARD aborda la cuestión desde la soberanía industrial. Fuente: https://www.youtube.com/watch?v=S25Q4JaA5jc

## En breve

**Amazon afirma que presuntos atacantes vinculados a China usaron agentes para descubrir y explotar una vulnerabilidad de día cero en MONAI Label en una campaña de 48 horas.** Los agentes hallaron un fallo de recorrido de rutas (*path traversal*) y lo utilizaron para tomar el control de un servidor universitario, según el informe de inteligencia de amenazas de Amazon. Fuente: https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382

**China registró 133 nuevos servicios de IA generativa en septiembre y octubre, con lo que el total asciende a 1245.** También inscribió 224 nuevas aplicaciones o funciones que consultan modelos registrados mediante API. Fuente: https://www.cac.gov.cn/2026-11/20/c_1796918603542950.htm

**China publicó cinco normas para robots humanoides, incluida una escala de inteligencia de L0 a L5.** La escala abarca percepción y cognición, decisión y aprendizaje, ejecución y colaboración. Fuente: https://www.ncsti.gov.cn/kjdt/kjrd/202611/t20261118_264191.html

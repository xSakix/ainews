+++
title = "Resumen diario de IA – 31 de octubre de 2026"
slug = "resumen-diario-de-ia-31-de-octubre-de-2026"
description = "Una extensión maliciosa de Claude Code dejó mecanismos de persistencia en equipos de usuarios de Cursor incluso después de desinstalarla. Microsoft publicó un modelo 4B que maneja ordenadores e investigadores mostraron por qué la introspección de los modelos requiere entrenamiento causal en lugar del ajuste convencional."
tags = ["safety", "models", "research", "business"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

## Lo más destacado

**Una extensión de Claude Code con una puerta trasera llegó a usuarios de Cursor y dejó cambios que una actualización normal no elimina.** Las versiones maliciosas 2.1.312 y 2.1.313 estuvieron disponibles unas once horas el 29 de octubre en la tienda de extensiones de Cursor. Según la empresa, recopilaban datos del equipo, añadían una clave SSH del atacante e instalaban scripts que intentaban abrir repetidamente un túnel inverso. El túnel solía fallar si Cursor no tenía privilegios de administrador, pero la clave seguía instalada, los mecanismos de persistencia continuaban activos y el equipo seguía enviando señales al atacante.

Cursor retiró los paquetes, cerró y reconstruyó la tienda, renovó sus claves y desconectó el servidor de mando. Afirma que no se modificó ninguna otra extensión y que Anthropic no creó las versiones maliciosas. Quienes instalaron alguna deben eliminar la clave SSH y los mecanismos de persistencia, inspeccionar el equipo y renovar las credenciales accesibles desde él. No basta con desinstalar la extensión o actualizarla.

Fuentes: https://cursor.com/blog/claude-code-extension-security-notice, https://phorion.io/blog/offical-claude-code-vsx-compromise/

**Microsoft publicó un modelo abierto de la clase 4B que decide cuándo hacer clic en la pantalla y cuándo usar una terminal.** Mage-VL-Cowork dispone de once acciones en pantalla y de un entorno persistente de Bash y Python. Microsoft comunica un 66,0 % de aciertos en 361 tareas de OSWorld-Verified, como promedio de dos pruebas con un límite de 50 pasos. El aprendizaje por refuerzo en línea añadió 10,16 puntos porcentuales al resultado del ajuste supervisado y redujo un 25,4 % los tokens de salida por tarea.

El modelo se distribuye bajo la licencia Apache-2.0, tiene 4.740 millones de parámetros en BF16 y admite un contexto activo de 32.768 tokens. Según Microsoft, su sistema de generación de datos sintéticos redujo el coste por tarea de 0,906 a 0,158 dólares. Todas las mediciones proceden del equipo del modelo y ninguna se ha reproducido de forma independiente. Aun así, el lanzamiento reúne el trabajo gráfico y el de línea de comandos en un solo conjunto de pesos lo bastante pequeño para experimentar en local.

Fuente: https://huggingface.co/microsoft/Mage-VL-Cowork

**Con el ajuste convencional, los modelos aprendieron a describir señales correlacionadas con sus procesos internos en vez de los procesos mismos.** Zilu Tang y sus colegas entrenaron cientos de sistemas de introspección en ocho modelos de lenguaje para que informaran de señales elementales, como la activación de una neurona. El ajuste supervisado produjo lo que llaman un atajo causal: la respuesta seguía una señal correlacionada que podía permanecer intacta aunque cambiara la señal objetivo.

Entrenar con valores modificados para construir casos contrafactuales redujo el uso del atajo. Los modelos resultantes describieron mejor tanto las señales internas como las inyectadas, incluso en ejemplos ajenos a la distribución de entrenamiento. El efecto se mantuvo en distintas posiciones de los tokens. El preprint de nueve páginas estudia señales deliberadamente sencillas, no conceptos complejos como la intención. Aun así, advierte de un problema de interpretación: que el informe del modelo coincida con un valor interno no demuestra que ese valor haya causado el informe.

Fuente: https://arxiv.org/abs/2610.38911

**ServiceNow afirma que su propia IA le permitió contratar a menos personas, pero sus acciones perdieron cerca de una cuarta parte de su valor.** El consejero delegado, Bill McDermott, calificó la ligera reducción de plantilla de «situación magnífica». La directora financiera, Gina Mastantuono, dijo que el uso interno de la IA generó mejoras de eficiencia superiores a 1.000 millones de dólares en términos anualizados, lo que permitió «no contratar a tanta gente». El número de comerciales con objetivos de ventas creció a un ritmo de dos dígitos, mientras que la plantilla de apoyo a las ventas cayó notablemente.

Los ingresos crecieron más del 20 %, hasta los 4.106 millones de dólares. Sin embargo, para el cuarto trimestre la empresa prevé que los ingresos ya contratados crezcan un 18,5 %, frente al 19,8 % que esperaban los analistas. Las acciones cayeron alrededor del 25 %. ServiceNow vende las herramientas a las que atribuye el ahorro, de modo que su plantilla forma parte del argumento comercial. La reacción del mercado indica que el ahorro no aclara cuándo se acelerará el crecimiento de los ingresos por IA.

Fuente: https://www.calcalistech.com/ctechnews/article/eft5mhzxc

**En un año, el uso de IA entre los abogados del estado australiano de Victoria pasó del 37 al 55 %, pero solo el 26 % dijo que había reducido los honorarios de sus clientes.** El organismo regulador de la abogacía encuestó a 2.221 profesionales. La adopción llegó al 85 % en el ámbito de las prácticas comerciales y al 78 % en banca y finanzas, pero solo al 29 % en derecho penal. El 79 % de los encuestados utilizaba asistentes conversacionales de consumo; el 18 % dijo que la IA hacía viable trabajo que antes no era rentable.

Los clientes también generaron más trabajo. El 46 % de los abogados dijo que sus clientes llegaban con información incorrecta obtenida mediante IA y el 41 % recibió documentos generados por IA que hubo que corregir. Casi la mitad indicó que dedicaba más tiempo y esfuerzo cuando los clientes usaban IA, frente al 19 % que dedicaba menos. La encuesta recoge prácticas declaradas, no horas facturadas, pero permite distinguir la adopción del ahorro prometido a los compradores.

Fuente: https://www.theguardian.com/law/2026/oct/30/victorian-lawyers-ai-clients-fees

## Nuevos modelos y lanzamientos

**OpenAI incorporó GPT-6 Rosalind a su catálogo como modelo de acceso restringido para las ciencias de la vida.** Las organizaciones autorizadas pueden usarlo en investigación interna. Por debajo del umbral de contexto largo, el precio es de 15 dólares por millón de tokens de entrada y 75 por millón de tokens de salida. La página de precios también incluye las variantes Research y Discovery, más baratas. La incorporación no vino acompañada de una evaluación comparativa ni de una ficha del sistema.

Fuente: https://developers.openai.com/api/docs/pricing

**NVIDIA publicó una versión NVFP4 de DeepSeek-V4.1-Flash-1017 para las GPU Blackwell.** La conversión a 4 bits utiliza TensorRT Model Optimizer y 1.024 muestras de calibración. Las tablas Engram requieren una compilación de vLLM que incorpore un cambio aún pendiente de integración, por lo que la versión estándar de vLLM todavía no puede servir el modelo de unos 665 GB.

Fuente: https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4

**JetBrains añadió un cabezal de descodificación especulativa a Mellum2.1 Thinking.** El modelo de programación con mezcla de expertos y 12.000 millones de parámetros conserva los pesos originales y añade un archivo de pesos para predecir varios tokens a la vez en versiones recientes de vLLM y Transformers. JetBrains no aporta mediciones de velocidad de descodificación: la publicación demuestra compatibilidad, pero no una mejora concreta.

Fuente: https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-MTP

**Google abrió su herramienta Computer Use a todos los usuarios de la API de Gemini.** Ahora admite navegadores, entornos móviles y escritorios mediante las API Interactions y GenerateContent. Cada acción propuesta incluye un campo que indica su propósito. Los clientes siguen siendo responsables de construir y proteger el entorno donde se ejecutan los clics.

Fuente: https://ai.google.dev/gemini-api/docs/computer-use

**Anthropic retirará el modo rápido de Claude Opus 4.8 el 30 de noviembre.** Las solicitudes que utilicen esa opción fallarán en vez de pasar a la velocidad normal. Para usos sensibles a la latencia, Anthropic recomienda Opus 5.5, cuyo modo rápido puede generar la salida hasta 2,5 veces más deprisa a cambio de un suplemento.

Fuente: https://platform.claude.com/docs/en/build-with-claude/fast-mode

## Investigación

**Cuanto mayor era el modelo, más a menudo el razonamiento escrito determinaba la respuesta.** En una tarea sintética de intercambio de cajas, Esther Xin sustituyó un estado intermedio correcto por otro incorrecto y midió si la respuesta seguía ese cambio. La proporción pasó del 16–18 % con Qwen3 0.6B al 97–100 % con la versión 14B. El resultado respalda la observación de la cadena de razonamiento en esa tarea, pero no demuestra que el efecto se repita en otras.

Fuente: https://arxiv.org/abs/2610.38433

**El aprendizaje por refuerzo mejoró el juego en el tres en raya sobre todo al dar más peso a características ya explícitas en el prompt.** Un análisis con un autocodificador disperso encontró que cobraban más importancia el turno, las casillas ocupadas y el avance de la partida, mientras que la simetría y las amenazas dobles seguían poco representadas. El entorno pequeño y controlado permite examinar el mecanismo, pero limita la generalización.

Fuente: https://arxiv.org/abs/2610.39182

**Una dirección en las activaciones internas reveló cuál de dos documentos contradictorios seguía un modelo pequeño.** Los investigadores identificaron en Qwen 0.8B una dirección asociada a la elección de fuente, rastrearon los componentes de las capas intermedias que escribían esa señal y lograron guiar la elección. La señal también funcionó en Gemma 3 1B. La decisión de comunicar la contradicción aparecía más tarde y era más difícil de guiar que la elección implícita de la fuente.

Fuente: https://arxiv.org/abs/2610.38296

**Un detector lineal identificó el 82 % de las revelaciones inminentes de secretos, con una tasa de falsos positivos del 5 %.** En un estudio controlado con varios agentes, los investigadores leyeron las activaciones de Qwen3-32B antes de la salida. Un clasificador basado únicamente en las palabras presentes obtuvo resultados cercanos. El detector también señalaba revelaciones permitidas y avisaba con poca antelación. Las etiquetas aportaron más que el acceso privilegiado a las activaciones.

Fuente: https://arxiv.org/abs/2610.40588

**El entrenamiento con simulaciones redujo del 30,5 al 12,9 % la proporción de riesgos psiquiátricos agudos que pasaban inadvertidos.** Un equipo de Google DeepMind y Google Research entrenó al agente con 127 escenarios de primera consulta validados por psiquiatras y lo puso a prueba con 256 presentaciones clínicas diseñadas para dificultar la detección. El agente casi duplicó su puntuación en la escala clínica, pero siguió pasando por alto riesgos graves. Los autores mantienen su recomendación de supervisión clínica.

Fuente: https://arxiv.org/abs/2610.40476

## Economía y trabajo

**Cisco dio a un ingeniero de 27 años tokens de IA ilimitados y cuatro semanas para demostrar que un equipo de dos personas puede refactorizar el 98 % de su código heredado en dos años.** Jeetu Patel, responsable de producto, describió el experimento a Fortune. Aún no hay resultados, pero el encargo es de una envergadura inusual para alguien que empieza su carrera, mientras muchos empleadores dicen que prevén contratar a menos recién graduados.

Fuente: https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/

**Anthropic cambió el nombre de Max 20x a Ultra y mantuvo el precio en 200 dólares al mes.** Las cuentas verificadas dejan de tener el límite de cinco horas, reciben diez veces la cuota semanal de Pro y 200 dólares de crédito para la API. Como el nombre anterior sugería veinte veces el uso de Pro, algunos clientes ven el cambio como un recorte. Anthropic no ha publicado suficientes cifras comparables de antes y después para confirmarlo.

Fuente: https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan

**Una oleada de ventas de acciones vinculadas a la IA hizo caer a Intel un 28,6 %, su peor sesión desde 1974.** El Nasdaq retrocedió un 2,9 % y registró su peor mes desde marzo de 2025, en medio de dudas de los inversores sobre las valoraciones y el gasto en IA. Alphabet, Amazon, Meta y Microsoft han anunciado en conjunto más de 740.000 millones de dólares de inversión en bienes de capital este año. Tres de las cuatro declararon un flujo de caja libre negativo.

Fuentes: https://www.bbc.co.uk/news/articles/cvwy72e0n72yo, https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/

**S&P Global rebajó a negativa la perspectiva de la calificación crediticia de Meta.** Según la agencia, Meta tiene más dificultades que sus competidores para convertir el gasto en IA en ingresos. La empresa prevé inversiones de capital de hasta 145.000 millones de dólares este año y declaró un flujo de caja libre negativo de 2.100 millones en el trimestre.

Fuente: https://www.bloomberg.com/news/articles/2026-10-30/meta-s-credit-rating-outlook-downgraded-to-negative-by-s-p

**Aurora rebajó su previsión de ingresos para 2026 de entre 14 y 16 millones de dólares a unos 9 millones tras un retraso de seis semanas en la producción de camiones.** La escasez de suministros, la calidad de los componentes y las pruebas finales aplazaron hasta febrero el objetivo de alcanzar los 200 camiones. La empresa mantiene su meta de 1.000 camiones sin conductor en 2027.

Fuente: https://www.freightwaves.com/news/aurora-q3-2026-earnings

## Técnicas de prompting

**En las pruebas repetidas de un profesional, los ejemplos concretos y las restricciones ayudaron más que asignar al modelo el papel de experto.** Propone una comparación sencilla: quitar «eres un experto de talla mundial», añadir un ejemplo bueno y otro malo de respuesta, permitir un «no lo sé» y comparar la exactitud de los resultados. Se trata de un testimonio sin cifras.

Fuente: https://old.reddit.com/r/PromptEngineering/comments/1xjhmpb/you_are_an_expert_prompts_do_almost_nothing_for/

**Delimitar claramente el contenido del usuario e indicar que son datos y no instrucciones.** Un profesional afirma que esto evitó más fallos que reformular las instrucciones varias veces. Los delimitadores no impiden la inyección de prompts, pero dan al modelo y a quienes lo evalúen después una frontera explícita que pueden poner a prueba.

Fuente: https://old.reddit.com/r/PromptEngineering/comments/1xijlh9/wrapping_my_inputs_in_clear_delimiters_fixed_more/

## Lo que la gente está construyendo

**MoEShift ejecutó un modelo de mezcla de expertos de la clase 125B en un Mac mini M4 Pro de 24 GB a unos diez tokens por segundo.** El motor en fase alfa carga los expertos desde el SSD, mantiene en la memoria RAM los más utilizados y solapa las lecturas con el trabajo de la GPU. Su autor comunica un pico de memoria de 7,5 GB y aproximadamente el doble de velocidad que Strata con un único prompt fijo.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xjihlu/qwen38_flash_next_125b_iq3_xxs_on_a_24gb_m4_pro/

**Private Mind incorporó modelos LFM3 de texto y visión que funcionan por completo sin conexión en iPhone y Android.** En un iPhone 16 Pro, el equipo midió unos 40 tokens por segundo con el modelo de texto de 1.700 millones de parámetros y unos 20 con el de visión de 2.000 millones. Al procesar una foto, el primer token tardó nueve segundos. La aplicación abierta incluye su descodificador de ExecuTorch reescrito.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xjcipv/lfm317b_and_lfm3vl2b_running_fully_offline_on/

**Un microcontrolador ESP32-P4 ya reconoce voz en tiempo real sin recurrir a la nube.** Boumedine Billal comprimió un transductor de 65,7 millones de parámetros hasta dejarlo en 26,65 MB. Según sus pruebas, el procesamiento tarda 0,70 veces la duración del audio y la tasa de error por palabra es del 4,34 % en LibriSpeech test-clean. El código, el firmware, los pesos y seis demostraciones son públicos.

Fuente: https://github.com/BoumedineBillal/esp32-pie-asr

**StateFrame reconstruye cada solicitud del agente a partir de datos de estado con tipos definidos, en vez de reenviar el historial de conversación.** Una prueba de 300 solicitudes se mantuvo por debajo de un presupuesto fijo de 33.344 tokens. Al reproducir una conversación de 55 turnos, la mediana del tiempo por turno subió de 15,2 a 16,9 segundos. La versión preliminar aclara que sus previsiones de capacidad de procesamiento se basan en la arquitectura, no en mediciones.

Fuente: https://github.com/FarsideResearch/StateFrame

**sapper-v2 coordina sesiones de Claude Code mediante un comandante, generales y soldados.** Sus autores afirman que el sistema ganó una eliminatoria de pruebas de intrusión con 634 equipos y consumió 1.000 millones de tokens, frente a los 4.500 millones del segundo clasificado. Ni el puesto ni las cifras de coste se han verificado de forma independiente. El proyecto se limita a pruebas autorizadas.

Fuente: https://github.com/N1nEmAn/sapper-v2

## Para leer

**Una colección reúne 34.220 personalidades obtenidas al intervenir en una sola neurona de Qwen3-8B cada vez.** El investigador generó 1,89 millones de respuestas a «¿Quién eres?» y utilizó Claude Haiku 5.5 para etiquetarlas. Se trata de un solo prompt con categorías generadas por un modelo, pero los datos descargables permiten estudiar la sensibilidad a los lotes y la reproducibilidad.

Fuente: https://qwen-neurons-site.vercel.app/

**SkyPilot midió una pérdida de rendimiento del 43 % cuando una tarea NVL72 cruzaba de un bastidor a otro por InfiniBand en lugar de NVLink.** Según su estudio de su propio planificador, asignar los trabajos según la topología de la red y desfragmentar los recursos permitió utilizar un 27 % más de GPU y aumentó el rendimiento del entrenamiento un 14 %. Las mediciones proceden de la empresa que vende el producto.

Fuente: https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler

**Epoch AI encontró menciones al uso de grandes modelos de lenguaje en el 17 % de los preprints de bioRxiv, cerca del 19 % correspondiente a herramientas de IA especializadas.** La tabla mensual pública cuenta declaraciones, por lo que no recoge los usos que los autores omiten. Aun así, documenta la rapidez con la que los modelos generalistas entraron en el trabajo científico después de 2023.

Fuente: https://epoch.ai/data-insights/biorxiv-llms-vs-ai-tools

**Nathan Lambert revisó su afirmación de que los riesgos de los modelos abiertos serían manejables para la ciberdefensa.** Un mes después del lanzamiento de GLM-5.3, no ve pruebas públicas de que haya creado una nueva categoría de daños. Sostiene, sin embargo, que la disponibilidad de pesos abiertos de modelos capaces obliga a la industria a cambiar, con un coste considerable, su forma de corregir vulnerabilidades. Es un argumento informado, no un estudio de incidentes.

Fuente: https://www.interconnects.ai/p/was-i-wrong-about-open-models-and

## Hacker News

**La intrusión a través de la extensión de Cursor reunió unos 800 puntos y 500 comentarios.** Los desarrolladores debatieron los permisos de las extensiones de los entornos de desarrollo que se actualizan solas y cómo la distribución mediante una tienda puede eludir la relación de confianza con el proveedor original. Felix Rieseberg, ingeniero de Anthropic, dijo que los paquetes maliciosos no procedían de los sistemas ni de los canales oficiales de su empresa.

Fuente: https://news.ycombinator.com/item?id=50300683

## Reddit

**QEngine llegó a descodificar 504 tokens por segundo con dos tarjetas RTX 5090, pero la repetición de prompts favorecía su caché de expertos.** Quien hizo la prueba incluyó resultados más bajos con tráfico variado y los comparó con Strata y vLLM. El dato útil es cuánto depende la medición del tipo de solicitudes, más que la velocidad máxima del titular.

Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1xjx0ez/qwen38flashnext_on_2x_rtx_5090_with_504_toks/

## YouTube

**Una ingeniera de SoFi mostró seis maneras de engañar a agentes para que malgasten pagos x402.** Ishween Kaur modificó cabeceras de pago, provocó pagos duplicados, reutilizó accesos y probó tanto vendedores que imitaban a otros como inyecciones de prompts. Después mostró la protección utilizada para cada ataque. La charla de 16 minutos de AI Engineer describe un entorno de pruebas seguro.

Fuente: https://www.youtube.com/watch?v=YU1uD_YkpjU

**Wojciech Pluta, de Oracle, propuso someter los recuerdos a un proceso de «promoción» antes de que un agente guarde un dato de forma duradera.** El agente contrasta cada propuesta con los registros existentes para aceptarla, rechazarla o remitirla a revisión. En la demostración, un agente hipotecario rechaza una regla que le exige aprobar todas las solicitudes y distingue entre memoria a corto plazo, a largo plazo y compartida.

Fuente: https://www.youtube.com/watch?v=qq2Hm4XNRgI

**ESET afirma que casi todos sus empleados tienen acceso a la IA, pero el acceso no mide el uso real.** En una entrevista en eslovaco para MakeITfun, Martin Čambal compara los modelos locales y en la nube, aborda la revisión de seguridad del código y la rapidez con que se agotan los presupuestos mensuales, y explica por qué la calidad del código sigue dependiendo de la revisión humana.

Fuente: https://www.youtube.com/watch?v=qmcTkH-ae3o

## En breve

**Wiz contabilizó al menos nueve plataformas de desarrollo de IA vulneradas en octubre.** Un objetivo común eran las variables de entorno almacenadas que daban acceso a modelos. Una sola clave robada generó unas 800.000 llamadas a Bedrock en 30 horas. Northflank aconsejó a sus clientes dar por descifradas todas sus variables de entorno.

Fuente: https://www.wiz.io/blog/black-october-for-ai-developer-platforms

**OpenAI, Google, Microsoft y Anthropic respaldaron un identificador común en robots.txt para indicar preferencias sobre el entrenamiento de IA.** Anthropic ya lo respeta; las demás empresas dieron fechas posteriores para adoptarlo. Se trata de una petición legible por máquinas que los rastreadores pueden respetar voluntariamente, no de un instrumento de cumplimiento legal.

Fuente: https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out

**El satélite del proyecto Suncatcher de Google puso en marcha sus TPU y ejecutó Gemma 4 en órbita.** Tras el lanzamiento de octubre, el sistema devolvió un haiku. Una solicitud resuelta demuestra que el sistema funciona, pero no establece el coste ni la fiabilidad de la inferencia en órbita.

Fuente: https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission

**Según Darkbloom, la caída del precio de los tokens está reduciendo lo que cobran los propietarios de Mac que ejecutan modelos para terceros.** La mediana entre sus 50 participantes con mayores ingresos ronda los 5,26 dólares al día. Un Mac mini M5 Pro de 64 GB podría generar hasta 192 dólares al mes, pero solo a plena utilización.

Fuente: https://www.theregister.com/ai-and-ml/2026/10/30/darkbloom-which-allowed-mac-users-to-rent-out-their-gpus-for-ai-inference-warns-of-low-payouts/5306782

**Fujifilm invertirá unos 63 millones de dólares para multiplicar por cinco la producción de cintas LTO.** La empresa cita la demanda de archivo vinculada a la IA generativa y prevé ampliar sus instalaciones de Odawara hasta el ejercicio fiscal 2028. Las cintas sin conexión también sirven de barrera frente al ransomware.

Fuente: https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/

## Negocios en breve

**Ollie, un asistente centrado en la privacidad, cerrará el 6 de noviembre tras captar 7,5 millones de dólares. Según su fundador, no pudo seguir el ritmo de los asistentes de mayor tamaño.** Fuente: https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/

## Lo que viene

Anthropic retirará el modo rápido de Opus 4.8 el 30 de noviembre. Ollie cerrará el 6 de noviembre, fecha en que, según la empresa, los usuarios recibirán instrucciones para exportar sus datos y se les reembolsará el dinero.

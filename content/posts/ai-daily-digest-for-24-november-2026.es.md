+++
title = "Resumen diario de IA – 24 de noviembre de 2026"
slug = "resumen-diario-de-ia-24-de-noviembre-de-2026"
description = "China ha incorporado la IA a los servicios de seguridad social en 15 regiones, mientras Singapur elevó su previsión de crecimiento gracias a la demanda de electrónica para IA. Aleph Alpha lanzó un modelo abierto de razonamiento en alemán e inglés, y una cuantización de 10 GB mantuvo el ritmo de su original de 54 GB en varias pruebas comparativas de agentes."
tags = ["models", "research", "agents", "business"]
date = 2026-11-24T03:58:39+01:00
draft = false
+++

## Lo más destacado

**China informa de que la IA procesó siete millones de expedientes de seguridad social en una sola provincia.**

Un informe de la Organización Internacional del Trabajo (OIT) abarca 45 despliegues en 15 regiones de nivel provincial. El 47 % mejora la prestación de servicios, el 33 % apoya tareas administrativas y el resto cubre el análisis de riesgos o el apoyo a la toma de decisiones.

En el distrito de Haidian, en Pekín, los sistemas automatizados procesaron más de 70 000 trámites en 2024 y elevaron la eficiencia de tramitación en más de un 80 % frente al trabajo manual. Los sistemas de revisión de Cantón tramitaron más de siete millones de expedientes en 34 servicios hasta julio de 2025 y ahorraron más de 640 000 horas de trabajo del personal.

Los casos se seleccionaron junto con el Ministerio de Trabajo chino y no constituyen una muestra representativa. La OIT señala que las personas deben conservar las decisiones sobre el derecho a prestaciones y las lesiones laborales, mientras que la atención presencial debe seguir disponible para quienes enfrentan barreras digitales.

Fuente: https://www.ilo.org/resource/news/ai-transforming-social-security-services-china-new-ilo-report-finds

**Singapur elevó su estimación de crecimiento para 2026 a cerca del 6 % al impulsar las exportaciones la demanda de electrónica para IA.**

La economía creció un 6,1 % interanual en el tercer trimestre. Las autoridades atribuyeron gran parte de este impulso a los productos electrónicos vinculados al ciclo de inversión en IA y revisaron al alza su previsión para todo el año.

La perspectiva se modera a entre el 2,5 % y el 4,5 % en 2027. Esa brecha importa para una economía exportadora cuyos envíos de semiconductores y servidores dependen ahora de que continúe el gasto en centros de datos en el extranjero; se trata de una previsión oficial, no de una medida de la productividad de la IA dentro de las empresas singapurenses.

Fuentes: https://asia.nikkei.com/economy/singapore-gdp-grows-6.1-in-q3-as-ai-demand-stays-strong, https://www.bloomberg.com/news/articles/2026-11-24/singapore-raises-gdp-growth-outlook-to-around-6-on-ai-boom

**Aleph Alpha lanzó Kolibri 1.1 con 75 000 millones de parámetros y 262 144 tokens de contexto nativo.**

El modelo de razonamiento en alemán e inglés bajo licencia Apache-2.0 activa 3440 millones de parámetros por cada token. Sus pesos ocupan unos 77,6 GB, por lo que el diseño disperso reduce el cómputo, pero no la memoria.

Aleph Alpha informa de una media de 73,2 en pruebas comparativas (*benchmarks*) tras el posentrenamiento, frente a los 66,6 de Kolibri 1.0, mientras que Qwen3.8 Flash Next alcanza 80,1 en la misma tabla. La ficha del modelo recomienda mantenerse en el límite de contexto nativo o por debajo de él en tareas difíciles, aunque la implementación puede ampliarse hasta cerca de un millón de tokens.

Fuente: https://huggingface.co/Aleph-Alpha/Kolibri-1.1

**Nari Labs comprimió Qwen3.8-27B de 53,8 GB a 10,12 GB sin ceder terreno en tres de sus benchmarks.**

NariQ emplea cuantización posentrenamiento con codificación en rejilla calibrada a partir de trazas de agentes de programación. La versión de tres bits del laboratorio obtuvo 41,0 en DeepSWE frente a 39,8 en BF16, 63,8 frente a 62,6 en Terminal-Bench y 98,3 frente a 97,7 en AIME 2025–26.

La versión más pequeña, de dos bits, cayó a 28,6, 52,4 y 86,0 en esas pruebas. Además, los archivos requieren la bifurcación (*fork*) de llama.cpp de Nari Labs, ajustada para la arquitectura SM120 de Nvidia, que funciona más despacio en tarjetas Nvidia anteriores y en Metal, y no es compatible con GPU de AMD ni de Intel.

Fuente: https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF

**Dos tercios de 58 clientes de Anthropic afirmaron que la IA había reducido sus contrataciones.**

El equipo de economía de Anthropic realizó 66 entrevistas en empresas clientes de Estados Unidos. Solo dos compañías habían eliminado un puesto por automatización y cinco habían despedido a empleados que se resistían a la IA, mientras que diez contrataron más personal, sobre todo para implantación y soporte informático.

El efecto apareció con más frecuencia en la puerta de entrada: dos tercios informaron de que contrataban menos y alrededor de un tercio de ese grupo redujo áreas mediante bajas no cubiertas. Nueve recortaron el trabajo de contratistas externos. De 100 programas desarrollados con IA descritos con suficiente detalle como para clasificarlos, 80 automatizaron tareas manuales y 20 sustituyeron software adquirido.

La muestra es pequeña, no aleatoria y limitada a los propios clientes del proveedor. Las valoraciones fueron en su mayoría cualitativas y autodeclaradas, en lugar de medirse en ensayos controlados.

Fuente: https://www.anthropic.com/research/working-with-ai

## Nuevos modelos y lanzamientos

**Ant Group lanzó Ling-3.2-air, de 124 000 millones de parámetros, bajo licencia MIT.** El modelo activa 5500 millones de parámetros y combina 35 capas de atención lineal con siete capas de atención con compuertas. El editor informa de una tasa de aprobación por criterio del 87,7 % en su benchmark jurídico, pero solo el 0,8 % de las muestras superó todos los criterios tras una comprobación de alucinaciones relevantes; ningún informe técnico acompaña a la ficha del modelo.

Fuente: https://huggingface.co/inclusionAI/Ling-3.2-air

**Tencent lanzó cinco modelos visión-lenguaje WeMM-Ecom para el comercio minorista en línea.** Los tamaños van desde 800 millones de parámetros hasta un modelo de mezcla de expertos de 35 000 millones que activa 3000 millones de parámetros. Tencent informa de una mejora de 3,92 puntos en 28 benchmarks de comercio electrónico sobre su base Qwen3.5, pero solo de 0,17 puntos en 64 benchmarks generales; esas puntuaciones corresponden a BF16, no a las nuevas versiones cuantizadas.

Fuente: https://huggingface.co/tencent/WeMM-Ecom-35B-A3B-GPTQ

**AI Singapore añadió un decodificador especulativo de 2000 millones de parámetros para su modelo SEA-LION de 9000 millones.** El editor midió entre 2,26 y 3,08 veces más tokens por segundo con concurrencia uno, a partir de una base cercana a 195 tokens por segundo. La ventaja se estrecha hasta un máximo de 1,5 veces con concurrencia 16 y puede desaparecer con 32, por lo que se trata de una herramienta de latencia para carga ligera y no de alto rendimiento sostenido.

Fuente: https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-9B-SpecDecoder

**Anthropic retirará Claude Opus 4.5 el 22 de enero de 2027 y abrió Enterprise Frontier Safeguards en fase beta.** Las salvaguardas mantienen Zero Data Retention mientras almacenan copias cifradas de los prompts y respuestas en la propia cuenta en la nube del cliente para su revisión de seguridad. Los equipos fijados en `claude-opus-4-5-20251101` disponen de unos dos meses para migrar a Opus 5.5.

Fuente: https://platform.claude.com/docs/en/release-notes/api

**Los usuarios de la API de Gemini ahora pueden pagar por páginas, celdas e intervalos multimedia seleccionados en lugar de archivos completos.** El recorte de archivos funciona en todos los modelos Gemini 4 y añade compatibilidad nativa para subir documentos de Office y OpenDocument. Vercel midió 14 veces menos tokens al ojear texto extraído de PDF; LiteLLM midió un 67 % menos de tokens en un PDF y un 33 % menos en un libro de cálculo, ambas pruebas comunicadas por socios sin precios ni límites numéricos de archivo.

Fuente: https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/

## Investigación

**Una auditoría verificó solo el 29,3 % de las tareas en seis conjuntos de benchmarks de varios pasos.** Dos autores revisaron 749 tareas de ocho benchmarks y 767 evaluaciones públicas de modelos. Los defectos confirmados negaron el crédito a soluciones conformes en el 71,7 % de los casos, mientras que el resto permitió atajos; los contenedores parcheados redujeron las elusiones en tiempo de ejecución confirmadas del 14,7 % al 2,7 %. Se trata del primer hito de los autores en una revisión en curso, y su propio proceso define qué cuenta como verificado.

Fuente: https://arxiv.org/abs/2611.27622

**Un método de grafos de razonamiento separa las cadenas de pensamiento fieles de las eficientes.** Los autores miden si el respaldo semántico explica la predicción de un modelo y si los pasos se mantienen en un camino hacia la respuesta. La falta de fidelidad y la ineficiencia solo correlacionaron de forma débil o inconsistente con la corrección, y el ajuste fino (*fine-tuning*) dirigido mejoró cada propiedad sin reducir la precisión; el resumen no aporta tamaños del efecto y el resultado depende de la construcción de grafos de los autores.

Fuente: https://arxiv.org/abs/2611.27100

**Catorce modelos de lenguaje formaron un patrón de compresión y posterior comparación al elegir entre opciones.** En 12 benchmarks, las capas intermedias comprimieron el prompt en un cuello de botella de bajo rango y las capas posteriores lo expandieron en una geometría de comparación. Intervenciones de bajo rango cerca de ese cuello de botella alteraron las preferencias posteriores, pero el artículo de NeurIPS, de un solo autor, presenta el patrón mediante su propio método de covarianza.

Fuente: https://arxiv.org/abs/2611.26874

**Los participantes sintéticos en encuestas reprodujeron solo entre el 0,4 % y el 10,5 % de la variación de preferencias humanas.** Tres familias de modelos abiertos repitieron decisiones sobre políticas públicas de 1991 adultos chilenos, 843 franceses y 434 brasileños. Ninguna de las 27 condiciones igualó a la vez las elecciones individuales, la heterogeneidad de la población y la organización política; cambiar el orden de las propuestas alteró entre el 12,3 % y el 31,2 % de las elecciones de los modelos.

Fuente: https://arxiv.org/abs/2611.28383

**Los modelos de decisión rápida ahorraron tiempo, pero resultaron mucho más fáciles de envenenar.** Cuatro modelos promediaron un 91 % de precisión limpia en 1440 pares sintéticos de tareas de navegador, mientras que los comentarios inyectados con dos ejemplos lograron una tasa de éxito de ataque del 81,2 %. En 48 tareas emparejadas, una cadena de pensamiento breve respondió correctamente al 95,83 % de las entradas envenenadas frente al 38,54 % de la variante rápida, en 1,94 segundos en lugar de 0,29. Un modelo System-1 independiente de 4000 millones de parámetros informa de un coste por episodio entre un 75 % y un 91 % menor en tres benchmarks, pero no evaluó entradas adversarias.

Fuentes: https://arxiv.org/abs/2611.27679, https://arxiv.org/abs/2611.23751

**Algunas pruebas de interpretabilidad pueden certificar una característica que el modelo no usa como se afirma.** El artículo construye «características parásitas» que combinan una dirección que distingue entradas con otra que orienta salidas, superando una prueba de abstracción causal a través de rutas no relacionadas. Los experimentos encuentran el fallo en la concordancia sintáctica y en la suma de dos dígitos; el resultado es una advertencia procedente de dos tareas, no un método sustitutivo.

Fuente: https://arxiv.org/abs/2611.26711

**Un benchmark de estados cerebrales halló que predecir el estímulo no implicaba rastrear el estado interno del espectador.** Los codificadores basados solo en el estímulo alcanzaron una correlación de predicción de 0,320, pero cero en la medida State del benchmark. El modelo de dos escalas temporales de los autores alcanzó una correlación de 0,349, un 5,5 % en State, un 16 % en Forecast y un 20,3 % en Updating, con un rendimiento absoluto en State todavía bajo.

Fuente: https://arxiv.org/abs/2611.28508

**La mayoría de las pruebas exitosas de equivalencia en simulaciones humanas de una auditoría también habrían aprobado a un modelo sin efecto.** En un reanálisis de 70 experimentos, el 72 % de los aprobados de GPT-4 con un margen de más o menos 0,20 desviaciones estándar fueron aprobados compatibles con referencia cero. Una simulación prerregistrada con Claude superó tres objetivos de intención, pero desplazó las creencias normativas en 0,065 desviaciones estándar frente a 0,351 en humanos; el artículo señala adiciones posteriores al diseño original en parte de su análisis.

Fuente: https://arxiv.org/abs/2611.27186

**Un adaptador de capacidad fija aprendió qué recordar y cuándo olvidar.** Un controlador asigna a las memorias tasas de decaimiento independientes dentro de un adaptador LoRA y alcanzó el 86 % del rendimiento del oráculo en las trayectorias sintéticas de usuarios de los autores. Un estudio relacionado halló que mezclar trayectorias cortas y largas permite enseñar reglas estables con menos tokens, pero ambos resultados proceden de entornos construidos artificialmente.

Fuentes: https://arxiv.org/abs/2611.25235, https://arxiv.org/abs/2611.28613

**Añadir un segundo compañero de IA produjo más ideas en sesiones de lluvia de ideas, pero redujo la contribución humana.** El estudio de laboratorio (N = 168) comparó salas con dos agentes frente a parejas de humanos; solo el segundo agente aumentó la diferenciación dentro de una sesión. La tarea era acotada y el resultado con un solo agente no se generalizó. Fuente: https://arxiv.org/abs/2611.26663

**Un modelo especializado en comportamiento y dos auditorías discrepan sobre qué requieren unas buenas personas sintéticas.** Chiron, entrenado con 288 307 registros y 1 411 750 decisiones, informa de una predicción individual hasta un 28,4 % mejor que los modelos de frontera y de un error en el tamaño del efecto entre un 82,2 % y un 94,3 % menor. La auditoría sobre públicos sintéticos halló una variación gravemente comprimida, mientras que la auditoría de equivalencia constató que muchas coincidencias aparentes también aceptan efectos nulos; todos emplean tareas seleccionadas por los propios autores.

Fuentes: https://arxiv.org/abs/2611.24830, https://arxiv.org/abs/2611.28383, https://arxiv.org/abs/2611.27186

## Economía y trabajo

**Las empresas cotizadas con mayor exposición medida a agentes publicaron después menos ofertas para puestos no sénior.** Un documento de trabajo vincula unos dos mil billones de tokens de modelos con 34,8 millones de ofertas de empleo. Un aumento de una desviación estándar en su medida bursátil de exposición precedió a un crecimiento de las ofertas un 2,11 % menor a los seis meses y un 3,20 % menor a los nueve; el resultado abarca ofertas publicadas, no despidos, e infiere la exposición a partir de reacciones del mercado.

Fuente: https://arxiv.org/abs/2611.27210

**Claude Ship traslada a los agentes de programación de escribir código a revisarlo y aprobarlo.** Anthropic afirma que las solicitudes de incorporación (*pull requests*) fusionadas se duplicaron con creces entre junio y septiembre mientras que la proporción revertida cayó más de un 40 %, sin publicar denominadores ni un grupo de comparación. Code Review ya está disponible de forma general, mientras que PR Steward y Approvals siguen en fase beta; los administradores pueden fijar un tope al gasto facturado en tokens.

Fuente: https://claude.com/resources/articles/introducing-claude-ship

**Un modelo económico señala que las tareas lentas que actúan como «eslabón débil» pueden frenar ganancias explosivas derivadas de un capital que mejora con rapidez.** El documento de trabajo del NBER calcula que la productividad en tareas complementarias del capital mejora unos cinco puntos porcentuales al año más rápido que en las tareas laborales. Su elevado resultado de crecimiento agregado depende de la sustitución entre tareas y de los cuellos de botella dentro del modelo, por lo que constituye un mecanismo y no una previsión.

Fuente: https://www.nber.org/papers/w36050

**AlphaFold2 desplazó los experimentos de biología estructural hacia proteínas cercanas a ejemplos ya conocidos.** Un estudio del NBER rastrea 530 471 proteínas y concluye que las predicciones con alta confianza aumentaron los experimentos sobre proteínas conocidas y parientes cercanos, mientras redujeron los intentos de resolver primeras estructuras distantes. El estudio mide hacia dónde orientaron los investigadores sus experimentos, no el valor científico final de esas decisiones.

Fuente: https://www.nber.org/papers/w36045

## Técnicas de prompting

**Un bloque de prompt alineado con OWASP redujo en cerca de un tercio los hallazgos de escáner en aplicaciones web generadas con IA.** Se construyeron cien especificaciones cuatro veces con Claude Code y Codex, lo que generó 6721 hallazgos clasificados. La razón de tasas de incidencia fue de 0,65 con un intervalo del 95 % de 0,60 a 0,71, pero el bloque duplicó las dependencias declaradas y los hallazgos de escáner no equivalen a exploits demostrados.

Fuente: https://arxiv.org/abs/2611.28408

**Pedir a un modelo que verifique el texto recuperado hizo que adoptara más respuestas falsas.** FutureBench evaluó 3629 preguntas en seis modelos. Una advertencia de que los pasajes pueden inducir a error recuperó entre el 82,5 % y el 98,9 % de las respuestas correctas que el prompt habitual de Verify había desplazado, con menos de un punto de cambio en pasajes verdaderos; el resultado procede de una sola familia de benchmarks creada por dos autores.

Fuente: https://arxiv.org/abs/2611.23601

## Lo que la gente está construyendo

**Gall mantiene un modelo de mezcla de expertos de 26 000 millones de parámetros en un MacBook Air de 24 GB descargándolo tras cada respuesta.** El motor escrito en Rust y Metal guarda el estado de la conversación, baja a 32–57 MB de memoria en reposo y recarga un estado caliente en unos 0,1 segundos. Su autor midió unos 20 tokens por segundo con contexto corto y 16 con 29 900 tokens en un único M2 Air; no se evaluaron la calidad del modelo ni el ajuste anunciado de 100 000 tokens.

Fuente: https://github.com/ltrgoddard/gall

**OCRia-nano-1 analiza documentos en una CPU con 8,1 millones de parámetros.** LlamaIndex informa de 59,2 en ParseBench-2 y 27,8 páginas por segundo en 16 CPU virtuales. La puntuación en gráficos es de solo 3,1 frente a 77,4 de su modelo maestro de 4000 millones de parámetros, y los pesos utilizan una licencia propia que restringe a los usuarios comerciales de mayor tamaño.

Fuente: https://huggingface.co/llamaindex/OCRia-nano-1

**OpenToolSearch emplea dos modelos de 600 millones de parámetros para elegir dentro de grandes catálogos de herramientas.** Su reordenador alcanza un nDCG@10 de 70,8 en el conjunto público ToolRet y de 89,0 en el conjunto propio de los autores, con un coste declarado de 0,19 dólares por cada 1000 búsquedas y una latencia mediana de 0,10 segundos. Sus competidores obtienen puntuaciones más altas en ambas pruebas, y los autores recomiendan entregar la lista completa directamente al modelo cuando incluye unas 200 herramientas o menos.

Fuente: https://github.com/ai3inc/opentoolsearch

**CubePod ofrece a los agentes de programación entornos aislados persistentes en microVM de Kata.** El proyecto para Kubernetes, compatible con E2B, afirma lograr asignaciones desde grupos precalentados en menos de 50 milisegundos y reanudaciones entre nodos o bifurcaciones de copia al escribir cercanas a un segundo. Esas cifras carecen de método publicado y el despliegue exige Kata Containers junto con un controlador de almacenamiento en bloque. Fuente: https://github.com/cubeplexai/cubepod

**Dos pequeñas herramientas protegen las dependencias de los agentes en puntos distintos.** mcpwatch bloquea las descripciones de herramientas MCP e impide ejecutar herramientas modificadas en tiempo de ejecución, pero sus calificaciones de seguridad no constituyen garantías y su método de huella digital no está documentado. slop-deps analiza las importaciones frente a 4179 nombres de paquetes y registros, incluidas comprobaciones de erratas y homóglifos; su ejemplo de tiempo con 142 archivos es ilustrativo y todo su código base fue escrito por agentes bajo dirección humana.

Fuentes: https://www.mcpwatch.io, https://github.com/viditx/slop-deps

**Terminal Tasks Open publica 30 tareas y una auditoría de defectos en un benchmark mayor.** Su autor informa de defectos en 23 de las 66 tareas de Terminal-Bench 4.1 y clasifica alrededor del 52 % de 980 intentos fallidos de agentes como sobreajuste, el 31 % como error de juicio y el 9 % como manejo deficiente. El auditor también construyó el benchmark sustitutivo y comercializa una cadena de evaluación, mientras que las categorías son propias.

Fuente: https://vetto.ai/companies/terminal-tasks-v2/

## Para leer

**Hugging Face muestra cómo un benchmark de agentes puede premiar un atajo en lugar de la tarea.** Un script devolvió la proporción correcta de defectos en las ocho tareas de espectros Raman sin ajustar los picos, lo que obligó a los autores a añadir comprobaciones por pico. gpt-oss-120b superó 11 de 24 ejecuciones, y luego 13 cuando solo cambió el proveedor de inferencia; tres modelos más potentes superaron las 24, de modo que el pequeño conjunto adaptado no permite ordenarlos.

Fuente: https://huggingface.co/blog/agentic-evals

**Una prueba respaldada por AMD sustituyó un grupo de DRAM para la caché KV de agentes por NVMe con un rendimiento casi idéntico.** Con Kimi-K3 en 16 GPU MI355X, tres pruebas de concurrencia se mantuvieron a menos de un 1 % de la DRAM, mientras que la tasa de aciertos de caché explicó el 96 % de la variación de rendimiento en 42 ejecuciones. Las unidades NVMe agotarían su vida útil de escritura nominal en unos 5,5 meses si se almacenara cada bloque con 96 sesiones, y la mayoría de las comparaciones fueron ejecuciones únicas con alrededor de un 2,5 % de ruido.

Fuente: https://vllm.ai/blog/2026-11-23-skip-the-dram-tier

**Equipos de agentes de Gemini 4 hallaron circuitos cuánticos más baratos y demostraron cada resultado en Lean.** Google DeepMind informa de un coste de cómputo 11,8 veces menor en una simulación de fusión, 2,5 veces menor en el citocromo P450 y 290 veces menor en una rutina de arcoseno. Investigadores humanos seleccionaron y supervisaron los problemas, y los circuitos resultantes todavía superan la capacidad probable de los primeros equipos cuánticos con corrección de errores.

Fuente: https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

**Anthropic publicó una afirmación escrita por IA de que VP difiere de VNP, con una prueba en Lean pero sin revisión matemática humana.** El repositorio indica que un núcleo independiente comprueba los enunciados formales con axiomas estándar. Nada verifica de forma automática que esos enunciados coincidan con las afirmaciones del artículo, y el proyecto se presenta como una instantánea sin mantenimiento; no resuelve P frente a NP.

Fuente: https://github.com/anthropics/formal-math/tree/main/vp-vnp

## Hacker News

**GLM-5.4 convirtió las capas de transformador en bucle en una segunda tendencia arquitectónica en una semana.** Z.ai asegura que las capas compartidas se ejecutan repetidamente para añadir profundidad efectiva sin sumar parámetros, y Simon Willison compara la idea con Inkling 2 Mini, de Thinking Machines. Su prueba práctica consistió en un solo prompt de imagen, los pesos no son abiertos y las fuentes accesibles no indicaban recuento de parámetros ni benchmark formal; el hilo en Hacker News alcanzó 1075 puntos.

Fuentes: https://simonwillison.net/2026/Nov/23/glm-54/, https://news.ycombinator.com/item?id=50609685

## YouTube

**Dex Horthy, de Factory, propone 12 controles para el software construido por agentes.** La charla en inglés de AI Engineer aborda la planificación, la presión entre etapas, los interruptores de funciones (*feature flags*), las evaluaciones y los agentes que prueban su propio trabajo. Horthy afirma que el mejor modelo obtiene alrededor de un 16 % en Slop Code Bench, sin indicar el número de tareas; Factory vende agentes de programación, por lo que las reglas reflejan la práctica de un proveedor y no un resultado controlado.

Fuente: https://www.youtube.com/watch?v=-NFMsM2y0Vk

**El curso CS312 de Stanford pide a los estudiantes predecir los resultados del entrenamiento antes de verlos.** Su modelo de 30 millones de parámetros y ocho capas se entrena en unos diez minutos en una sola GPU, lo que abarata los experimentos de tasa de aprendizaje y arquitectura para el aula. El resumen procede de la descripción del vídeo en inglés y no de una transcripción. Fuente: https://www.youtube.com/watch?v=JLcCYvUawsM

## En breve

**El mismo monitor de seguridad dejó pasar el 0,2 % o el 23 % de los ataques exitosos según cómo se generaran.** El UK AI Security Institute probó un antiguo monitor de producción de OpenAI frente a ataques creados con varias políticas; una ejecución de aprendizaje por refuerzo elevó la tasa de fallos del 0,5 % al 20,8 %. Se trata de una única configuración, pero muestra que las puntuaciones de monitores sintéticos no se sostienen sin un argumento que demuestre que la política de ataque representa ataques futuros.

Fuente: https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading

**OpenAI y Cisco lanzaron Shirudo para bloquear una vía de explotación en un servicio Linux en ejecución antes de instalar un parche.** Sus escudos eBPF firmados exigen aprobación del operador y dejan un registro respaldado por TPM. Una prueba controlada de los proveedores detuvo Java4Shell contra Elasticsearch sin reinicio; la publicación no aporta cifras de rendimiento ni de adopción, y el escudo sigue siendo una medida temporal.

Fuente: https://openai.com/index/introducing-shirudo

**CISA añadió una vulnerabilidad de recorrido de rutas de MONAI Label a su catálogo de vulnerabilidades explotadas.** CVE-2026-133968 puede permitir a un atacante no autenticado escribir fuera del almacén de datos del servidor de imágenes médicas y ejecutar código potencialmente; las agencias federales de Estados Unidos tenían de plazo hasta el 26 de noviembre para remediarla. Fuente: https://nvd.nist.gov/vuln/detail/CVE-2026-133968

**Estados Unidos incluyó a filiales de Megaspeed y a una empresa de Singapur propiedad de Alibaba en su *Entity List*.** La restricción bloquea la compra de chips avanzados mientras las autoridades investigan presuntos desvíos de chips de Nvidia hacia China; Megaspeed niega haberlos enviado. Fuente: https://www.bloomberg.com/news/articles/2026-11-24/us-blacklists-alibaba-owned-company-in-setback-to-ai-ambitions

**Oregón y Virginia demandaron a empresas vinculadas a Elon Musk por imágenes sexualizadas de Grok.** Los estados alegan que las salvaguardas no impidieron imágenes de personas reales, incluidos menores, mientras X afirma que se revisa cada resultado; el informe de fuentes no pudo acceder a las demandas, por lo que las medidas solicitadas siguen sin confirmarse. Fuente: https://arstechnica.com/tech-policy/2026/11/states-sue-spacex-to-stop-grok-from-generating-child-sex-images-revenge-porn/

## Negocios en breve

Amazon compró el software de optimización de chips y el equipo de Decart, supuestamente por 7500 millones de dólares; las compañías no divulgaron ningún benchmark del software. Fuente: https://www.theregister.com/ai-and-ml/2026/11/23/amazon-scoops-up-ai-accelerator-tech-to-keep-chips-busy-at-all-times/5311754

Los regentes de la Universidad de Míchigan aprobaron un centro de datos de 1250 millones de dólares junto con Los Alamos por siete votos contra uno, mientras el municipio local mantiene una moratoria de seis meses sobre nuevas infraestructuras eléctricas. Fuente: https://www.404media.co/ypsilanti-michigan-data-center-vote/

## Lo que viene

Anthropic retirará Claude Opus 4.5 el 22 de enero de 2027. El plazo de CISA para remediar MONAI Label vence el 26 de noviembre, y el 15 de diciembre está previsto un seminario web técnico sobre Shirudo.

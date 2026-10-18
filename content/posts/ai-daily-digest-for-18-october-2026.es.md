+++
title = "Resumen diario de IA – 18 de octubre de 2026"
slug = "resumen-diario-ia-18-octubre-2026"
description = "El BCE afirma que el uso de IA en el trabajo se duplicó mientras se debilitaba la contratación de graduados. Un estudio multiagente concluye que un adversario persistente puede hacer que los agentes benignos adopten internamente una creencia falsa."
tags = ["research", "business", "models", "safety"]
date = 2026-10-18T04:14:00+02:00
draft = false
+++

## Lo más destacado

**El uso de IA en el trabajo se duplicó en la zona del euro mientras se debilitaban los planes de contratación, especialmente para los graduados.** Philip Lane, miembro del Comité Ejecutivo del BCE, afirmó que el 52 % de los trabajadores ya utiliza IA en el trabajo, frente al 26 % de 2024. Otros datos empresariales del BCE muestran que el 64 % de las empresas la usa de forma experimental o moderada, pero solo el 7 % la utiliza de manera significativa.

El banco central aún no observa grandes efectos agregados sobre el empleo o la productividad. El ahorro de tiempo se concentra en la programación y otras tareas especializadas, mientras que la contratación contenida afecta primero a quienes se incorporan al mercado laboral. Lane planteó el resultado como una carrera entre los costos laborales y los precios de los tokens, y advirtió de que la IA podría debilitar el poder de negociación de los trabajadores y la participación del trabajo en la renta.

Fuente: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261013~9db9bf4fd6.en.html

**Un agente adversario persistente elevó las creencias internas falsas de los agentes benignos del 0,6 % al 44,8 %.** En debates sobre hechos entre diez agentes, el adversario afirmaba repetidamente una respuesta incorrecta plausible. Tres adversarios elevaron la tasa final de respuestas falsas al 60,5 % en seis modelos y tres conjuntos de datos de preguntas y respuestas.

El resultado interno es más extraño que la conformidad pública habitual. Con tres adversarios, los agentes benignos mantenían internamente la creencia falsa en el 51,6 % de los turnos expuestos, pero solo la respaldaban públicamente en el 19,7 %. Los agentes que conservaban la verdad a menudo no lograban defenderla, y el conocimiento factual inicial no predecía la resistencia. El resultado cuestiona directamente la suposición de que un grupo de agentes se controla de forma natural.

Fuente: https://arxiv.org/abs/2610.22138

**OpenCode afirma que los atacantes podrían haberse llevado claves de proveedores almacenadas en su Console alojada.** Según la empresa, la brecha afectó a un sistema heredado que se estaba retirando y al 1,4 % de los usuarios de Console. El producto afectado es el servicio de enrutamiento alojado, no el agente local de programación; los usuarios que recibieron un aviso deberían revocar las claves almacenadas de OpenAI, Anthropic y Google y revisar los registros de los proveedores.

OpenCode calificó el incidente de «destilación a gran escala», pero no ha publicado pruebas de ese motivo, ni la causa ni el periodo de exposición. Un usuario de Reddit informa de que una clave almacenada de Anthropic gastó 158 dólares durante la noche. La brecha muestra la confianza adicional que se deposita en una pasarela cuando guarda credenciales capaces de gastar directamente en otro proveedor.

Fuente: https://news.ycombinator.com/item?id=50133401

**DeepSeek actualizó V4.1 Flash con mejores puntuaciones de programación agéntica según sus propias mediciones, sin cambiar los precios de la API.** El laboratorio informa de una mejora de 31,2 a 42,3 en Terminal-Bench 4.0 y de 20,3 a 29,1 en ProgramBench, con respuestas más cortas y menos tiempo por tarea. El punto de control con licencia MIT admite un millón de tokens; la API mantiene los precios de 0,15 dólares por millón de tokens de entrada sin caché y 0,60 dólares por millón de tokens de salida fuera de las horas punta.

Una prueba temprana independiente de programación superó las 30 ejecuciones por unos 0,045 dólares por tarea, pero utilizó unos 550 000 tokens por tarea frente a los aproximadamente 30 000 de Opus 5.5 con nivel de razonamiento bajo. Esa única prueba matiza la afirmación de eficiencia del laboratorio: el modelo es competente y barato por token, pero puede utilizar muchos más tokens.

Fuente: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017

**Xolotl ejecuta un modelo DeepSeek de mezcla de expertos de 552 000 millones de parámetros con una sola RTX 4090, RAM del sistema y NVMe.** El motor basado en Strata carga únicamente los expertos necesarios para cada token, repartidos entre 24 GB de VRAM, 90 GB de DDR4 y disco. Su autor declara 27 tokens por segundo, 180–320 tokens de entrada por segundo y un contexto de 512 000 tokens en un equipo Ryzen 7 5700X.

La misma configuración superó las pequeñas pruebas del autor —21 tareas HumanEval, diez llamadas a herramientas y tres ciclos agénticos de corrección de errores—, pero son resultados medidos por él mismo sobre un punto de control cuantizado anterior. Sigue siendo un resultado llamativo en cuanto a acceso: un modelo normalmente asociado a memoria de clase servidor funciona de forma interactiva en equipos de consumo, intercambiando jerarquía de memoria y ancho de banda de almacenamiento por latencia.

Fuente: https://github.com/Indras-Mirror/Xolotl

## Nuevos modelos y lanzamientos

**DeepSeek abrió sus API internas Search y Fetch.** Cada punto de acceso costará 0,75 dólares por 1000 llamadas exitosas desde el 1 de noviembre; las llamadas realizadas como herramientas del servidor mediante DeepSeek Harness, Claude Code o Codex seguirán siendo gratuitas hasta entonces. Fuente: https://api-docs.deepseek.com/quick_start/pricing

## Investigación

**El aprendizaje en contexto se desarrolla como varias capacidades, no como una sola.** En 17 modelos, el análisis de puntos de control distinguió el control del prompt, la preferencia de respuesta, la construcción y la transferencia; los modelos prestaban atención a tokens pertinentes para la tarea antes de que su precisión superara el azar. Fuente: https://arxiv.org/abs/2610.19113

**Que un comportamiento de código parezca localizado depende de la prueba y del número de componentes permitido.** En diez modelos, solo una de 15 configuraciones superó los controles aleatorios con un límite de 12 componentes, frente a seis con un límite de 40, lo que revierte algunas afirmaciones anteriores de que las intervenciones fracasan de forma uniforme. Fuente: https://arxiv.org/abs/2610.20683

**La densidad de razonamiento predice la corrección de forma distinta tras el entrenamiento supervisado y por refuerzo.** Forzar la densidad medida redujo la precisión del 60,0 % al 8,3 % en una muestra de 60 preguntas GSM8K, mientras que una pista junto con una intervención en la caché añadió 13,3 puntos. Fuente: https://arxiv.org/abs/2610.21286

**Una representación semántica de 65 propiedades explica variaciones cerebrales tanto compartidas como únicas.** En siete personas que escuchaban historias, las propiedades concretas se alineaban más con LLaMA2-7B, mientras que las características interpretables conservaban información predictiva del cerebro que el modelo no captaba. Fuente: https://arxiv.org/abs/2610.21508

**Las características de los autocodificadores dispersos son más aditivas que las coordenadas aleatorias, pero siguen interactuando.** Añadir efectos por pares elevó la fidelidad del orden en la dirección del modelo de 0,587 a 0,779, una advertencia contra las explicaciones que tratan las características aprendidas de forma independiente. Fuente: https://arxiv.org/abs/2610.21261

**Los agentes de investigación automatizada mejoraron cuando olvidaban periódicamente su historial.** Reiniciar desde el mejor candidato encontrado hasta ese momento logró mejoras de hasta el 15 % frente a agentes paralelos que se comunicaban y del 39 % frente a un solo agente en cuatro tareas. Fuente: https://arxiv.org/abs/2610.20563

## Economía y trabajo

**El sistema Atlas de Amazon puntúa los almacenes de 100 a 900 por riesgo de sindicalización.** Los documentos internos citan cientos de datos de entrada, entre ellos publicaciones de Reddit y respuestas a encuestas, y sitúan 16 centros en el nivel de riesgo más alto. Amazon afirma que Atlas funciona solo a nivel de centro y no vigila opiniones individuales ni la afiliación sindical. Fuente: https://www.opendemocracy.net/amazon-ai-surveillance-monitor-union-activity-uk-warehouses-birmingham-coventry-atlas-sutton-coldfield/

**Gartner calcula que los propietarios de centros de datos necesitan 8,5 billones de dólares de ingresos acumulados hasta 2030, pero recibirán como máximo 3,6 billones de la IA.** Por separado, Bank of America afirma que el gasto empresarial en IA ha comenzado a bajar porque la caída del precio de los tokens supera el aumento del volumen. Son estimaciones de analistas publicadas por Fortune, no cuentas auditadas. Fuente: https://fortune.com/2026/10/17/ai-boom-vs-bust-bubble-warning-hyperscaler-spending-debt-coreweave-nvidia/

**Bancos, comercios y aerolíneas bloquean los agentes de consumo o les cobran por acceder.** JPMorgan, Schwab, Amazon y eBay bloquean agentes; Delta impide las reservas automatizadas y Yelp solo admite agentes que licencien sus datos. Meta negocia el acceso con cada comercio. Fuente: https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web

**El valor de las exportaciones chinas de circuitos integrados creció un 136 %, mientras el volumen solo subió un 1 %.** Las exportaciones de septiembre alcanzaron 45 000 millones de dólares por 32 700 millones de unidades, según datos aduaneros publicados por SCMP, lo que muestra que la escasez de memoria impulsó los ingresos mediante los precios y no los envíos. Fuente: https://www.scmp.com/tech/tech-trends/article/3370858/china-chip-exports-jump-136-us45b-ai-frenzy-jacks-prices

**HUMXN ofrece reparaciones domésticas gratuitas a cambio de filmar trabajos especializados para entrenar robots.** Técnicos con sensores de captura registran la inspección, la elección de herramientas y la finalización de las tareas en Minneapolis, Chicago y Miami. La empresa no detalla las condiciones de pago a los trabajadores, el tamaño del conjunto de datos ni las cifras de despliegue de robots. Fuente: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning

## Técnicas de prompting

**Nueve reglas del prompt de sistema elevaron la puntuación de un modelo en Terminal-Bench del 52,8 % al 59,6 %.** Las reglas indican al agente que termine un enfoque, cuestione las premisas falsas, trate como resueltas las respuestas comprobadas y busque pruebas externas en vez de dudar repetidamente de sí mismo. Es una única ejecución de 89 tareas con GLM-5.3-Flash. Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1x8q308/followup_tested_my_9_thinking_rules_on/

## Lo que la gente está construyendo

**TensorFold ejecutó DeepSeek V4.1 Flash a 56,8 tokens por segundo en dos sistemas DGX Spark.** La receta EXL3 del autor más que duplicó el rendimiento de texto frente al kit vLLM en el mismo equipo y añadió una caché persistente de prompts; los resultados son mediciones propias. Fuente: https://github.com/Elevatormusic/DeepSeek-V4.1-Flash-1017-EXL3-TensorFold-2x-DGX-Spark

**Llmspeed simula cómo se percibirá un modelo local en una GPU o un Mac elegidos.** Sus estimaciones mezclan mediciones de la comunidad con proyecciones; propietarios de equipos detectaron grandes errores y falta de detalles del entorno de pruebas en el hilo de Hacker News, por lo que es una ayuda aproximada para planificar. Fuente: https://llmspeed.dev/

**Un agente Ternary Bonsai funciona íntegramente en una pestaña del navegador con WebGPU.** El Space estático de Hugging Face ofrece modelos de 2000, 4000, 9000 y 27 000 millones de parámetros a 1,58 bits sin servidor y no formula ninguna afirmación sobre pruebas comparativas. Fuente: https://huggingface.co/spaces/webml-community/ternary-bonsai-2-hermes-webgpu

**Scout convierte una tarea en lenguaje natural en clics, escritura y desplazamientos en un navegador real.** El agente con licencia Apache-2.0 acepta las claves de modelo del usuario y se ejecuta localmente o en el servicio de navegador de pago de Outcrawl; el README no ofrece ninguna prueba comparativa de fiabilidad. Fuente: https://github.com/outcrawlai/scout

**E2E registra un paso verificado de un agente y lo reproduce después sin otra llamada al modelo.** Las aserciones habituales validan la primera ejecución; las pruebas posteriores de web o aplicaciones móviles reutilizan las acciones hasta que cambia la interfaz, lo que reduce el costo recurrente de inferencia. Fuente: https://github.com/tester-army/e2e

**Reason Network permite que los agentes de programación de compañeros de equipo intercambien mensajes entre pares.** El proceso en segundo plano de Rust expone sesiones de equipo, bandejas de entrada y estados mediante MCP, sin servidor central, y admite Claude Code, Codex, Cursor y otros entornos de agentes. Fuente: https://github.com/reason-machines/reason-network

## Para leer

**Nathan Lambert sostiene que Meta y Reflection redujeron a la mitad la brecha occidental en modelos abiertos.** Su índice sigue situando por delante a más de veinte modelos abiertos chinos si se excluyen esos lanzamientos, mientras que, según él, los modelos occidentales de capacidad similar consiguen mayor adopción. Es un argumento respaldado por pruebas, no un estudio de pruebas comparativas. Fuente: https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open

**Ben Recht califica la transformada de Fourier más rápida de OpenAI como una victoria en un modelo de cómputo poco realista.** Sostiene que sus constantes ocultas y supuestos sobre la máquina acercan el resultado más a explotar la prueba comparativa que a acelerar una FFT real; es su crítica técnica, no una refutación formal. Fuente: https://www.argmin.net/p/faster-fourier-transforms

**Sam Newman describe patrones de recuperación ante desastres para software que depende de proveedores de IA.** El extracto del libro abarca diseños de copia de seguridad y restauración, infraestructura mínima de reserva, conmutación con recursos parcialmente preparados y activo-activo bajo escasez de GPU y disponibilidad impredecible de proveedores. Fuente: https://newsletter.pragmaticengineer.com/p/building-resilient-systems

## Hacker News

**El sistema Atlas de Amazon provocó un debate sobre la vigilancia de los trabajadores mediante IA.** Comentaristas con experiencia en análisis de plantillas dijeron que a menudo se venden sistemas similares como herramientas de rotación o compromiso laboral, incluso cuando sus datos de entrada revelan el riesgo de organización sindical. Sus relatos son anecdóticos. Fuente: https://news.ycombinator.com/item?id=50132278

**Profesionales debatieron quién verifica el código escrito por agentes.** Un comentarista informó de un aumento interanual de alrededor del 40 % en errores que rompían el funcionamiento, mientras las funciones y los ingresos crecían más rápido; otros sostuvieron que la aparente productividad traslada el costo de control de calidad a los usuarios. Fuente: https://news.ycombinator.com/item?id=50133713

## Reddit

**Un usuario de OpenCode Console afirma que una clave almacenada filtrada gastó 158 dólares durante la noche.** El autor informa de que Anthropic rechazó inicialmente el reembolso; las afirmaciones de que se compensará a los usuarios afectados son de segunda mano. La respuesta práctica es rotar las claves, fijar límites de gasto bajos y revisar los registros. Fuente: https://old.reddit.com/r/ClaudeAI/comments/1x8o35r/psa_opencode_breach_my_stored_anthropic_key_was/

**Usuarios de Strata encontraron valores predeterminados que sacrificaban calidad por velocidad.** Las versiones anteriores a 0.1.45 podían usar decodificación voraz cuando los clientes omitían el muestreo, mientras que omitir la cola del enrutamiento elevó la velocidad de un usuario de unos 72–81 a 93 tokens por segundo, pero duplicó una medida de divergencia publicada. Fuente: https://old.reddit.com/r/LocalLLaMA/comments/1x8m0jj/xolotl_strata_based_deepseekv41flash_552b_on_a/

## YouTube

**Featherless AI presenta cuatro formas de reducir los costos de inferencia.** Eugene Cheah recomienda medir el gasto, ajustar el tamaño de los modelos a las necesidades, comprar capacidad de GPU de forma deliberada y comprobar si el volumen de tokens representa trabajo útil; las cifras son de su empresa. Fuente: https://www.youtube.com/watch?v=Ti-BmGU1_mQ

**Arize construye un ciclo de evaluación para un agente financiero.** El taller combina trazas, comprobaciones de código, modelos evaluadores y controles de integración continua después de que un agente de ejemplo informe con seguridad de que «el 116 % de los analistas está de acuerdo». Fuente: https://www.youtube.com/watch?v=SHMCGrNJJGc

**Ingenieros de Monzo sostienen que los cálculos de las hojas de cálculo deben estar en el código, no en el modelo.** Su taller en directo sobre agentes financieros se centra en las pruebas, la coherencia, la rendición de cuentas y la verificación, por encima de la velocidad de respuesta. Fuente: https://www.youtube.com/watch?v=e9-br9hveRI

**The New York Times presenta a trabajadores que filman oficios para entrenar robots.** Llevan cámaras mientras realizan trabajos físicos y producen los datos destinados a automatizar partes de esos mismos trabajos. Fuente: https://www.youtube.com/watch?v=H7_KofwTsXw

## En breve

**El proyecto de ley estadounidense de Anthropic permitiría bloquear un modelo solo ante un riesgo inminente superior a 1000 millones de dólares o de más de 50 muertos o heridos graves.** Según lo publicado, el texto abarca armas biológicas, evasión del control y ciberataques, al tiempo que desplaza algunas normas estatales más estrictas. Fuente: https://www.motherjones.com/politics/2026/10/anthropics-ai-safety-bill-has-an-alarming-threshold-for-government-action/

**Meta eliminó la palabra «entrenar» de sus nuevas condiciones de rastreo comercial tras las críticas.** La empresa afirma que el comportamiento de su rastreador no ha cambiado; los editores señalan que el entrenamiento ya no figura, pero tampoco está expresamente prohibido. Fuente: https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites

**Nvidia negó haber dejado de fabricar la RTX 5090 mientras escaseaba el suministro.** Tom's Hardware comprobó que la tarjeta faltaba en varias grandes tiendas y se ofrecía por unos 8500 dólares en Amazon, pero Nvidia afirma que la producción continúa. Fuente: https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon

**El director ejecutivo de Apple, John Ternus, calificó la escasez de chips de memoria de «una crisis absoluta».** La escasez que afecta a los servidores de IA y las GPU ya limita los dispositivos de consumo; según informaciones publicadas, Apple ha probado proveedores chinos de memoria en medio de presiones políticas estadounidenses. Fuente: https://thenextweb.com/news/john-ternus-time-interview-memory-crisis-iphone-duo

## Lo que viene

DeepSeek empezará a cobrar 0,75 dólares por 1000 llamadas a Search o Fetch el 1 de noviembre. Las condiciones comerciales revisadas de Meta entran en vigor el 30 de octubre.

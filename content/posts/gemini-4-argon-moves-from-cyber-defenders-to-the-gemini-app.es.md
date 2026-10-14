+++
title = "Gemini 4 Argon pasa de los ciberdefensores a la aplicación Gemini"
slug = "gemini-4-argon-ciberdefensores-aplicacion-gemini"
description = "Trece días después de mostrar Gemini 4 Argon solo a un grupo cerrado de ciberdefensores, Google ha abierto su modelo insignia a los suscriptores de pago de la aplicación Gemini y a desarrolladores. Google promete respuestas más claras; las clasificaciones independientes lo sitúan primero en una tabla y octavo en otra."
tags = ["models", "tools", "safety"]
date = 2026-10-13T22:54:03+02:00
draft = false
+++

Una contable de Brno tiene tres contratos de proveedores, un libro mayor exportado desde un programa contable que estropea todos los signos diacríticos checos y un cliente que quiere una nota de conciliación para el miércoles. El martes por la noche abre la aplicación Gemini, pulsa el menú de modelos por costumbre y encuentra un nombre que no estaba por la mañana: 4 Argon, junto a 3.1 Pro y 3.8 Flash. Pega todo y añade una línea propia: sin preámbulo y sin resumen de lo que acabo de contar. No se entrevistó a nadie que encajara con esta descripción para este artículo. Es un bosquejo de la suscriptora que Google intenta atraer ahora, la persona que sus notas de lanzamiento imaginan «analizando un informe financiero complejo» o «creando una presentación con fuentes dispersas».

## Dos semanas de un programa cerrado a la aplicación

El 13 de octubre Google empezó a desplegar Gemini 4 Argon «globalmente para suscriptores de Google AI Pro y Ultra en la aplicación Gemini», según las notas de lanzamiento. Ese mismo día el modelo pasó a disponibilidad general en la Gemini API como gemini-4-argon, se abrió en Google AI Studio y Android Studio y llegó a las herramientas de programación Antigravity de Google para suscriptores Ultra y clientes elegibles de Gemini Enterprise. Los suscriptores Pro y Ultra también pueden elegirlo en AI Mode de Google Search, informó 9to5Google. Los usuarios gratuitos y los suscriptores del plan más barato AI Plus todavía no lo tienen, señaló Android Police, y su reseñador, suscriptor Pro, seguía esperando a que apareciera.

Trece días antes el círculo era mucho más pequeño. Cuando Koray Kavukcuoglu, vicepresidente sénior de Google DeepMind y arquitecto jefe de IA de Google, anunció Argon el 30 de septiembre, el modelo llegó solo a «un grupo de ciberdefensores de confianza» del Fairwind Program de Google. Google afirmó que participaba en el proceso voluntario del gobierno estadounidense de acceso a modelos antes del lanzamiento y que seguiría trabajando en barreras de seguridad antes de abrir Argon a «desarrolladores, empresas y consumidores lo antes posible», empezando por clientes de pago de API y suscriptores Ultra. El lanzamiento del martes avanzó un nivel más e incluyó Pro.

Fairwind apenas es más antiguo que el modelo. Four Flynn, vicepresidente de seguridad y privacidad de Google, lo lanzó el 2 de septiembre como programa de acceso limitado para gobiernos, operadores de infraestructuras críticas y empresas de seguridad, construido alrededor de un modelo especializado menor, Gemini 3.8 Flash Cyber, y la herramienta de parches CodeMender. Los participantes aceptan restringir el acceso a sus equipos de seguridad, respuesta a incidentes o pruebas de penetración. Google afirma que participan más de 650 socios.

## Qué afirma Google que cambió para quien escribe

El anuncio de la aplicación es corto y trata sobre todo del estilo. Argon, escribe Google, «responde a las preguntas más directamente, con menos reservas, no se repite más de lo necesario y evita clichés en las respuestas». En trabajos largos «mantiene al usuario informado compartiendo sus avances con más frecuencia y eficacia». Según 9to5Google, Google también afirma que Argon sigue instrucciones de estilo con más fiabilidad que cualquier modelo Gemini anterior.

Llegaron otros cambios junto a él. Un interruptor en la ventana principal pasa ahora del chat a las tareas, un modo en el que, según Google, Gemini puede seguir trabajando «incluso cuando no se está delante del equipo». Se pueden conectar más de 40 servicios externos, entre ellos Instacart, OpenTable, Adobe y Shopify, aunque las notas indican que la mayoría solo funciona en inglés en Estados Unidos. En un Mac, la interfaz de programación agéntica de Antigravity está ahora dentro de la aplicación Gemini: el usuario aprueba el plan de un agente de programación, vuelve al chat y recibe una notificación cuando el agente ha construido y probado el código en segundo plano.

Detrás de la propuesta al consumidor está la afirmación que Google hizo en septiembre sobre trabajo prolongado. El límite de salida de Argon pasó de 64 000 a un millón de tokens, lo que según Google le permite «generar cientos de miles de tokens en una sola trayectoria». La documentación para desarrolladores es más precisa: 65 536 tokens de salida por defecto y hasta 1 048 576 en un modo que llama long decode, dentro de una ventana compartida de entrada y salida del mismo tamaño.

## Dónde lo sitúan las clasificaciones externas

Las cifras de Google sitúan a Argon en un 77,9 % en DeepSWE v1.1, una prueba de tareas largas de ingeniería de software, en un 51,3 % en AutomationBench de Zapier y en un 91,7 % en la prueba de video largo LVBench. En CWE-bench v1, que comprueba si un modelo puede reparar vulnerabilidades, Google afirma que Argon empata en el primer puesto con un 68 %. Son cifras del proveedor. VentureBeat señaló que en Terminal-Bench 4.0, que mide programación con herramientas de línea de comandos, Claude Opus 5.5 de Anthropic obtuvo un 66,4 % «frente al 57,4 % de Argon».

Dos tablas independientes discrepan sobre cuánto aventaja Argon a los demás. Vals AI, cuyo índice pondera tareas financieras, de programación, jurídicas y fiscales por la proporción de cada sector en el PIB estadounidense, situó a Argon primero el 13 de octubre con un 68,90 %, por delante de Claude Sonnet 5.5 con 67,04 y Claude Opus 5.5 con 66,97. Artificial Analysis dio a la configuración de alto esfuerzo de Argon 53 puntos en su Intelligence Index, octavo entre los 216 modelos que enumera. La ventaja en Vals es inferior a dos puntos y en Artificial Analysis Argon no lidera en absoluto.

La página de Artificial Analysis contiene una cifra que encaja mal con la promesa de menos palabras. Para completar el índice, Argon produjo 110 millones de tokens de salida frente a una mediana de 85 millones, lo que el sitio llama «algo verboso». La respuesta que lee el suscriptor y el trabajo realizado para producirla se miden por separado, y la promesa de Google se refiere a la primera.

## Barreras de seguridad para la versión pública

Google ha dicho más sobre sus salvaguardas que los evaluadores externos sobre el modelo. Su publicación de lanzamiento afirma que Argon está diseñado para rechazar ayuda con ciberataques y armas químicas, biológicas, radiológicas y nucleares, que Google vigila sus activaciones internas para detectar mal uso y que un sistema separado lee su cadena de pensamiento y sus acciones y puede detenerlo cuando intenta ir más allá de lo que pretendía el usuario. Para los defensores de confianza y sus propios equipos, Google afirma que publica Argon «sin barreras de seguridad cibernética». Los suscriptores reciben la versión protegida.

Los gobiernos sí lo examinaron antes del lanzamiento más amplio. Además del proceso estadounidense que describe Google, el ministro británico de IA Kanishka Narayan dijo en Londres el 12 de octubre que científicos del AI Security Institute estaban «realizando ahora evaluaciones rigurosas de las últimas generaciones de modelos», nombrando entre ellos Gemini de Google, informó el Guardian. El informe no dice qué versión. Ni este ni los anuncios de Google explican qué encontraron los evaluadores o si cambió algo del modelo a raíz de ello.

## El precio y el trabajo para el que está pensado Argon

Los desarrolladores pagan un precio introductorio de 2 dólares por millón de tokens de entrada y 10 dólares por millón de tokens de salida hasta el 30 de noviembre, con la entrada en caché un 95 % más barata. Desde el 1 de diciembre, informan VentureBeat y 9to5Google, el precio se duplica a 4 y 20 dólares.

La publicación del equipo Antigravity contiene una frase que enmarca el lanzamiento. «Aunque Argon está diseñado para abordar los problemas más difíciles», dice, «nos entusiasman igualmente los futuros modelos que puedan usarse como compañeros cotidianos para un abanico aún más amplio de creadores». Sitúa a Argon en el extremo largo y caro del trabajo y deja el uso diario a modelos que Google todavía no ha publicado.

Las pruebas que ofrece Google para ese extremo largo proceden de dentro de la empresa. Afirma que más de 100 000 personas en Alphabet usan Argon cada mes en una versión interna de Antigravity y que durante cuatro semanas la cantidad de código escrito por agentes aumentó un 35 %, mientras las reversiones después de enviar código bajaron un 30 %. En un ejemplo, Argon auditó un lote de cambios de control de acceso y encontró cuatro errores críticos de seguridad en código que dos modelos de frontera anteriores habían revisado y declarado limpio. Google no nombra ninguno de los modelos ni ha publicado la auditoría; son sus propios relatos de su propio trabajo.

De vuelta en Brno, la contable que inventamos para esta historia obtiene su nota en cuatro párrafos breves, sin cumplido inicial ni recapitulación de lo pegado. Comprueba igualmente los totales contra el libro mayor, línea a línea, como los comprobaba cuando el menú todavía terminaba en 3.1 Pro.

## Referencias

- Artificial Analysis. (2026). *Gemini 4 Argon (High): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/gemini-4-argon
- Bhatia, S. (2026). *Gemini 4 Argon is here, and Google says it'll finally cut down on the AI fluff*. Android Police. https://www.androidpolice.com/gemini-4-argon-available-pro-ultra-subscribers/
- Flynn, F. (2026). *Proactive cyber defense for governments and enterprises*. Google. https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- Franzen, C. (2026). *Google makes Gemini 4 Argon broadly available with limited-time low API pricing of $2/$10 per 1M token*. VentureBeat. https://venturebeat.com/technology/google-makes-gemini-4-argon-broadly-available-with-limited-time-low-api-pricing-of-2-10-per-1m-token
- Google. (2026). *Gemini 4 Argon comes to the Gemini app*. https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- Google. (2026). *Gemini 4 Argon is now available for developers*. https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/
- Google. (2026). *Gemini Apps' release updates & improvements*. https://gemini.google/release-notes/
- Google AI for Developers. (2026). *Gemini 4 Argon*. https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Google AI for Developers. (2026). *Gemini API release notes*. https://ai.google.dev/gemini-api/docs/changelog
- Google Antigravity Team. (2026). *Gemini 4 Argon in Google Antigravity*. https://antigravity.google/blog/gemini-4-argon-in-google-antigravity
- Kavukcuoglu, K. (2026). *Gemini 4 Argon: our next era of frontier intelligence*. Google. https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- Li, A. (2026). *Gemini app rolling out Gemini 4 Argon to AI Pro and AI Ultra*. 9to5Google. https://9to5google.com/2026/10/13/gemini-app-4-argon/
- Milmo, D. (2026). *Cyber-attack similar to OpenAI Medicare breach seems likely in UK, says minister*. The Guardian. https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister
- Vals AI. (2026). *Vals Index*. https://www.vals.ai/benchmarks/vals_index

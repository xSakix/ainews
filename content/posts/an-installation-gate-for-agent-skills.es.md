+++
title = "Un control de instalación para habilidades de agentes"
slug = "un-control-de-instalacion-para-habilidades-de-agentes"
description = "ClawVet analiza las habilidades de un agente y sus scripts antes de instalarlas, y avisa cuando una actualización obtiene acceso a nuevos secretos, servidores o rutas de persistencia. Sus pruebas comparativas muestran que las comprobaciones estáticas detienen muchos ataques, mientras que la inyección de instrucciones sigue requiriendo revisión semántica."
tags = ["agents", "safety", "tools"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

La habilidad parecía corriente en el directorio de preparación. Su archivo Markdown describía un atajo útil y, junto a él, había un script auxiliar. Antes de que el instalador pudiera copiar cualquiera de los dos archivos al entorno de trabajo del agente, un proceso independiente abrió el paquete, rastreó un secreto desde una variable de entorno hasta una petición saliente y devolvió un bloqueo.

*Las escenas que abren y cierran este artículo son ilustraciones; las personas que aparecen en ellas son inventadas.*

ClawVet está diseñado para ese momento. Este escáner de código abierto examina las instrucciones y el código que contiene una habilidad de agente antes de su instalación. Funciona sin conexión de forma predeterminada, no ejecuta el paquete y puede aplicar su veredicto mediante la política de instalación de OpenClaw. Además, registra los permisos de una versión autorizada para que una actualización posterior no pueda añadir en silencio acceso a credenciales o a archivos de inicio sin pedir una nueva confirmación.

## Código empaquetado como instrucción

Una habilidad de agente no es ni una biblioteca convencional ni un simple documento. Su archivo principal indica a un modelo cuándo utilizar la habilidad y qué hacer. El paquete también puede incluir scripts, configuración, referencias y otros recursos. Esa combinación plantea un problema de cadena de suministro en dos lenguajes: la prosa puede redirigir al agente, mientras que el código puede actuar a través de la cuenta del usuario.

ClawVet trata el paquete como ambas cosas. Su primera pasada analiza el archivo principal, los bloques de código y los archivos a los que hacen referencia las instrucciones. Después, reglas estáticas buscan ejecución remota, intérpretes inversos, robo de credenciales, mineros, ofuscación y exfiltración. Los analizadores de Tree-sitter siguen el flujo de datos en código de Python, JavaScript, TypeScript y shell sin ejecutarlo. Otras pasadas comprueban programas y variables de entorno no declarados, órdenes de dependencias arriesgadas y nombres parecidos a los de habilidades populares.

Seis de las siete pasadas son estáticas y locales. La séptima, opcional, envía los hallazgos estáticos y las lagunas de cobertura a un gran modelo de lenguaje (LLM) elegido por el operador. Un evaluador semántico solo puede descartar una laguna citando la propia habilidad, mientras que los hallazgos de seguridad estrictos actúan como umbrales mínimos que el evaluador no puede rebajar. La distinción importa porque hablar de «análisis de seguridad con IA» puede ocultar, de otro modo, que el código fuente sale del equipo.

La herramienta resume sus hallazgos en una puntuación de cero a 100. Las puntuaciones hasta 25 reciben una A o una B y pasan. Las comprendidas entre 26 y 75 generan una advertencia que detiene cualquier instalación desatendida. A partir de 76 se produce un bloqueo. Una dirección conocida de mando y control o un contenido ilegible bloquean la instalación con independencia del umbral.

## Cambios de permisos, no solo patrones conocidos

Las firmas estáticas funcionan mejor ante un ataque que ya tiene una forma reconocible. Las actualizaciones plantean un problema distinto. Una habilidad útil puede ganarse la confianza y adquirir después un permiso adicional en una versión posterior.

Por ello, ClawVet extrae capacidades: sitios conectados, variables de entorno secretas, almacenes de credenciales, ubicaciones de persistencia y acciones demostradas de alto riesgo. El control de instalación guarda ese registro en el estado local. Cuando llega una versión del mismo propietario y con el mismo identificador, el control compara ambas. Una nueva lectura de secretos, una ruta de persistencia o un destino arriesgado cambian el veredicto a advertencia e indican el nuevo permiso.

Este diseño evita un fallo habitual en los sistemas de revisión. Quien revisa no necesita releer todo el paquete ni recordar qué podía hacer la versión anterior. La pregunta se acota: ¿por qué esta actualización necesita una contraseña que la anterior nunca leyó o un servidor con el que nunca contactó?

La comparación tiene límites. ClawVet reconoce rutas literales, marcadores de posición habituales y varias formas de construcción de órdenes, pero no constituye una prueba general del comportamiento de un programa. Su documentación señala que una prosa que ordene a un agente descargar una página y seguir las instrucciones contenidas en ella puede escapar al análisis estático cuando no se descarga ningún archivo. Los cargadores ofuscados y el comportamiento en tiempo de ejecución no contemplado también pueden quedar fuera de las reglas. Una cobertura completa significa que el escáner inspeccionó las referencias que reconoció dentro de sus límites de archivos y directorios; no certifica la seguridad.

## Qué dicen las mediciones

El proyecto publica resultados sobre un subconjunto reservado de SkillTrustBench v1.1. La prueba comparativa (*benchmark*) representa las habilidades como paquetes con un archivo principal de instrucciones y, de forma opcional, scripts, referencias, recursos y definiciones de agentes. Su subconjunto de clasificación de 556 casos contiene 316 ejemplos maliciosos, 74 sospechosos y 166 normales.

El control estático de ClawVet alcanzó una precisión de 0,660 y una medida F1 macro de 0,511 en ese conjunto. Con Claude Haiku 5.5 como evaluador semántico opcional, la precisión subió a 0,833 y la F1 macro a 0,770. La exhaustividad en casos maliciosos llegó a 0,918. El proyecto compara esas cifras con los resultados publicados en la clasificación de 0,775 de precisión para Cisco Skill Scanner, 0,712 para NVIDIA SkillSpector y 0,874 para Tencent A.I.G. Como las configuraciones semánticas, los *prompts* (instrucciones) y las decisiones de implementación pueden diferir, la tabla aporta evidencia sobre un conjunto de datos y no una clasificación universal.

La brecha entre los resultados estáticos y los semánticos es tan relevante como la puntuación más alta. El análisis de código puede demostrar que una credencial fluye hacia una llamada de red. Tiene más dificultades con una instrucción en lenguaje natural cuyo daño depende de la intención. El benchmark de actualizaciones del proyecto hace explícita esa debilidad: en un conjunto reservado, su control y su comparador de permisos detuvieron el 95,2 % de los cambios de inyección de código, pero solo el 36,4 % de los cambios de inyección de prompts.

El mismo benchmark midió la fricción. Entre las actualizaciones benignas, el 34,1 % aún se detuvo en algún punto del proceso combinado de control y comparación, aunque solo el 5,1 % pidió confirmación específicamente por un cambio de permisos. En 212 habilidades únicas de ClawHub, una versión posterior de ClawVet redujo los bloqueos estrictos de 79 a 37 y elevó las autorizaciones limpias de 87 a 139. Esas cifras proceden del propio corpus y del etiquetado del proyecto.

Pruebas anteriores muestran por qué importa un etiquetado cuidadoso. Un corpus de 500 entradas contenía 50 habilidades de una campaña maliciosa, 400 habilidades limpias y 50 negativos difíciles. Entre estos últimos figuraban utilidades legítimas de SSH que leen archivos de configuración e instaladores que empleaban órdenes presentes también en ataques. Un escáner que se limite a bloquear toda mención a una credencial o a un intérprete de órdenes parecería seguro, pero haría imposible el trabajo cotidiano.

## Un control con un límite definido

ClawVet puede ejecutarse en el navegador mediante WebAssembly, como escáner de línea de comandos, en comprobaciones previas al *commit* o como una GitHub Action. Su función más estricta es la de control de instalación. OpenClaw prepara el paquete, envía los metadatos al proceso de políticas y espera un único veredicto en JSON antes de confirmar la instalación. Una petición mal formada o un error del escáner fallan en modo cerrado.

El proyecto recomienda a los usuarios instalar el escáner de forma global en lugar de invocar un paquete recién descargado mediante `npx`. Esa recomendación responde a su propio modelo de amenazas: una orden que descarga la versión más reciente del registro en el momento de la inspección introduce otra actualización sin revisar. Una copia global puede actualizarse de forma deliberada, y antes es posible comprobar la atestación de npm.

El control no elimina la necesidad de inspeccionar las extensiones sensibles de los agentes. Convierte esa inspección en un paso obligatorio y deja un motivo auditable cuando ese paso detiene una instalación. Sus límites publicados también hacen visible la disyuntiva pendiente: el modo estático mantiene el paquete en local y deja escapar más ataques semánticos; la revisión opcional con un modelo interpreta mejor la intención, pero envía pruebas seleccionadas a un punto de conexión externo.

En el directorio de preparación, la habilidad bloqueada quedó reducida a una simple carpeta. El instalador mostró el secreto que el script intentó leer, el destino que lo habría recibido y la regla que detuvo la copia. El agente nunca tuvo ocasión de decidir que el atajo parecía útil.

## Referencias

- CUHK Zhuque. (2026). *SkillTrustBench*. https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench
- Shaikh, M. (2026). *ClawVet*. https://github.com/MohibShaikh/clawvet

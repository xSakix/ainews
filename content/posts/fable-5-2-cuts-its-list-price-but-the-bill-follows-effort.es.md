+++
title = "Fable 5.2 baja su tarifa, pero el razonamiento marca la factura"
slug = "fable-5-2-tarifa-razonamiento-factura"
description = "Anthropic redujo una quinta parte el precio de Claude Fable 5.2, pero un índice independiente midió el mayor costo por tarea entre 73 modelos al nivel máximo de razonamiento. La diferencia depende de cuántos tokens consume el modelo, y los gráficos de la propia Anthropic indican que el nivel de razonamiento lo determina."
tags = ["models", "business"]
date = 2026-11-10T03:25:07+01:00
draft = false
+++

Este lunes es inventado, construido a partir de documentos de lanzamiento y no del diario de nadie. La responsable de plataforma de una empresa de software mediana lee que Anthropic ha reducido una quinta parte el precio de su mejor modelo. Hace lo que invita a hacer el anuncio. Cambia el nombre del modelo en la configuración de agentes de su equipo, fija el parámetro de nivel de razonamiento en su valor máximo y deja cuarenta auditorías de repositorios ejecutándose durante la noche. Por la mañana, el lote ha terminado y solo quiere abrir una cosa: la factura. No se parece al titular que leyó.

El titular era correcto. El 9 de noviembre, Anthropic lanzó Claude Fable 5.2 y su gemelo, Claude Mythos 5.2, a 8 dólares por millón de tokens de entrada y 40 dólares por millón de tokens de salida, frente a los 10 y 50 dólares de las versiones 5.1. La cifra independiente que llegó ese mismo día también es correcta. Artificial Analysis, que publica un índice de inteligencia entre proveedores, ejecutó Fable 5.2 en su ajuste máximo y lo situó primero entre 74 modelos en inteligencia, con 65 puntos, y en el puesto 73 de 73 en costo, a 26,54 dólares por tarea del índice. Las dos cifras describen un mismo modelo. Lo que las separa es cuántos tokens consume.

## Lo que dice la tarifa

La documentación de Anthropic enumera claramente los nuevos precios. Las lecturas de caché cuestan 0,20 dólares por millón de tokens, el procesamiento por lotes cuesta la mitad de la tarifa base y un modo rápido opcional que genera hasta 2,5 veces más rápido cuesta 16 dólares en entrada y 80 dólares en salida. La empresa también afirma que el modelo produce salida hasta un 30 % más rápido que Fable 5.1. TechCrunch señala que Fable es ahora más barato que su principal rival, y Fortune sitúa Fable 5.2 un 20 % por debajo de GPT-6 Astra de OpenAI, cuya tarifa es de 10 y 50 dólares, con la entrada en caché a 20 centavos frente al dólar de Astra.

Mythos 5.2 tiene el mismo precio. Anthropic presenta ambos como el mismo modelo subyacente; Fable llega con salvaguardas para riesgos cibernéticos y biológicos y está abierto a todos los clientes, mientras Mythos se ofrece a organizaciones admitidas en los Cyber Verification y Life Sciences Verification Programs de la empresa. Comparten el precio. No el acceso.

## Lo que midió el índice

Artificial Analysis calcula el costo por tarea a partir de los precios de entrada, aciertos y escrituras de caché, razonamiento y tokens de respuesta, divididos por el número de tareas y ponderados entre las nueve evaluaciones de su índice. Con esa base, Fable 5.2 al nivel máximo generó 275 millones de tokens de salida, mientras la mediana de modelos comparables es de 72,8 millones. Tardó 46,4 minutos por tarea, frente a una mediana de 12,7, y 216 segundos hasta el primer token de respuesta. El resumen del propio sitio califica el modelo de «especialmente caro» y «muy prolijo».

El cálculo es breve. El precio publicado de salida es de 40 dólares frente a una mediana de 10 dólares, cuatro veces más, y el número de tokens ronda 3,8 veces la mediana. Una factura es precio multiplicado por volumen, y Fable 5.2 se sitúa alto en ambos con este ajuste. Conviene explicitar los límites: estas son las tareas de Artificial Analysis, no las del lector, y la cifra corresponde a un solo nivel de razonamiento.

## El ajuste al que apunta Anthropic

Anthropic no discute que el nivel de razonamiento importe. Su página de lanzamiento dice que el valor predeterminado en las aplicaciones de Claude y Claude Code es Medium, y que en Medium Fable 5.2 completa tareas difíciles con menos tokens que 5.1. En las primeras pruebas de FrontierCode 2.0, una prueba comparativa, o *benchmark*, que evalúa si los responsables de proyectos de código abierto fusionarían los cambios de código de un modelo, Fable 5.2 en High obtuvo un 45,3 %, frente al 45,5 % de Opus 5.5 en Max, por aproximadamente la mitad del costo por tarea. En WANDR, el benchmark de recopilación de datos de Perplexity, el nivel Medium iguala la mejor puntuación de Opus 5.5 por alrededor del 40 % del costo. En Humanity's Last Exam, Low lo hace por menos de una décima parte. En Xhigh, el modelo alcanza un 49,1 % en FrontierCode, la mayor puntuación de cualquier modelo publicado que Anthropic haya probado.

Todos estos gráficos son del proveedor y proceden de pruebas iniciales. Muestran que un mismo modelo ocupa puntos muy distintos de una curva de costos según un solo parámetro, lectura que también respalda la cifra independiente. La documentación es directa sobre el lugar de Fable: para la mayoría de las cargas, empezar con el último modelo Opus y pasar a Fable cuando las evaluaciones de Opus con niveles de razonamiento superiores sigan sin «cumplir los requisitos».

## Cómo llegó la factura hasta aquí

Anthropic ya ha presentado los precios de esta forma. Su anuncio de Claude Opus 5.5 del 22 de septiembre afirmaba que el modelo rinde al nivel de Fable 5.1 en la mayoría de los trabajos y cuesta un 40 % menos que Opus 5 en cargas habituales. El precio por token era un 20 % menor, a 4 y 20 dólares por millón, y la empresa atribuía el resto del ahorro a utilizar menos tokens por tarea. Según el propio relato de Anthropic, una factura es una tarifa multiplicada por una cantidad.

Gergely Orosz, autor de The Pragmatic Engineer, dio contexto al efecto en una edición del 20 de octubre. Habló con personas de 27 lugares de trabajo sobre el gasto en IA por desarrollador, una muestra autoseleccionada y mayoritariamente anónima. Informa de que el gasto alcanzó su máximo en junio y julio y se ha reducido aproximadamente a la mitad en empresas con planes de API; la mayoría atribuye la bajada a una combinación de Opus 5.5 y modelos abiertos. Un ingeniero gastó 2200 dólares en septiembre en Opus 5 y espera gastar la mitad con Opus 5.5. Orosz también supo que están terminando las suscripciones subvencionadas de varias empresas, lo que podría multiplicar sus facturas entre cinco y diez veces.

Fable 5.2 llega a ese cálculo. Un comprador que pasó a Opus 5.5 para reducir la factura a la mitad dispone ahora de una categoría superior cuyo precio por token bajó y cuyo costo por tarea depende de un ajuste que la mayoría no toca.

## Ofertas de lanzamiento y quién paga la prueba

Durante la primera semana, los suscriptores no notan el precio. El centro de ayuda de Anthropic dice que los planes Pro y las licencias estándar de Team incluyen todos los modelos Fable en sus límites semanales del 9 al 16 de noviembre, hasta el 50 % de esos límites, más un reinicio del límite. Los planes Max y Ultra reciben entre uno y tres reinicios, según cuánto tiempo lleve la cuenta siendo de pago, y los reinicios no utilizados caducan el 8 de marzo de 2027. Las ofertas están redactadas para planes de suscripción y la página no dice nada sobre cuentas de API.

## De nuevo, la factura

En el lunes inventado, la responsable revisa el lote de auditorías y no ve nada malo en los hallazgos. Lo que le falta es una comparación. La siguiente prueba que prepara es sencilla: los mismos cuarenta repositorios en High y después en Medium, con el costo y el número de hallazgos aceptados junto a cada uno. Si las ejecuciones más baratas encuentran lo suficiente es una pregunta que ninguna página de lanzamiento puede resolver para su equipo, y la documentación que leyó también lo dice. El modelo se cobra por millón de tokens. Su revisión se valorará por repositorio.

## Referencias

- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Anthropic (2026). *Introducing Claude Opus 5.5*. https://www.anthropic.com/news/claude-opus-5-5
- Anthropic (2026). *Claude Fable 5.2 launch offers*. Claude Help Center. https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
- Anthropic (2026). *What's new in Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- Brandom, R. (2026). *Anthropic releases new Mythos and Fable models amid RSI concerns*. TechCrunch. https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/
- Forlini, E. (2026). *Anthropic debuts Claude Fable, Mythos 5.2 models, priced 20% below OpenAI's GPT-6 Astra*. Fortune. https://fortune.com/2026/11/09/anthropic-debuts-updated-claude-fable-and-mythos-models-undercutting-price-of-openais-gpt-6-astra-by-up-to-80/
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers

+++
title = "Cloudflare redujo su factura de revisión con IA al arreglar la caché"
slug = "cloudflare-redujo-factura-revision-ia-arreglando-cache"
description = "El revisor de código con IA de Cloudflare se encarecía mientras sus modelos mejoraban. La empresa redujo el costo medio un 68 % y la latencia mediana casi dos tercios, pero después tuvo que demostrar que el revisor más barato no había dejado simplemente de encontrar problemas."
tags = ["agents", "tools", "business"]
date = 2026-10-20T04:05:28+02:00
draft = false
+++

Una ingeniera existe solo para este párrafo. Su solicitud de integración contiene un pequeño cambio en un servicio utilizado en todo el mundo. Lo envía a las 16:12. Siete revisores automáticos se activan, leen las mismas instrucciones, inspeccionan partes superpuestas del repositorio y hacen pasar casi tres millones de tokens por los modelos antes de que un coordinador decida qué decirle. La revisión llega cuatro minutos después. Cuesta más del doble que el mismo sistema en primavera.

## La factura subió sin rediseño

Cloudflare construyó ese tipo de sistema para sus propios ingenieros. Ryan Skidmore, ingeniero de sistemas de la empresa, describió la arquitectura original en abril de 2026: hasta siete agentes especializados revisaban seguridad, rendimiento, calidad del código, documentación, lanzamientos y normas internas, mientras un coordinador eliminaba hallazgos duplicados y decidía si aprobar la solicitud de integración. Según Cloudflare, durante el primer mes completó 131 246 revisiones de 48 095 solicitudes en 5169 repositorios. El costo medio por revisión era de 1,19 dólares.

A finales de agosto, el promedio rondaba los 2,46 dólares. Cloudflare no había sustituido el sistema por otro más elaborado. El coordinador seguía delegando en especialistas y los mismos niveles de riesgo determinaban si un cambio recibía una revisión ligera o completa. La empresa había cambiado los modelos y permitido que crecieran las conversaciones.

Los costos avanzaban de forma sostenida: 1,22 dólares por revisión en marzo, 1,44 en junio, 1,74 en julio y 2,32 en agosto, tras ajustar la mezcla de niveles de revisión. Más cambios terminaban en el nivel caro, pero Cloudflare atribuye la mayor parte del aumento a los modelos elegidos. Pasar todos los revisores a modelos de Anthropic elevó un trabajo de 1,38 a 2,03 dólares. Un revisor de normas internas pasó de unos 25 a 88 centavos por ejecución.

Los modelos también hacían más trabajo. Los tokens por revisión se multiplicaron por más de tres, de 0,91 a 2,99 millones, aunque la tasa global de aciertos de caché mejoró del 85,7 al 97 %. Un porcentaje alto había ocultado un denominador mayor.

## El prefijo caro

Justo antes de la optimización, los tokens de salida representaban aproximadamente el 23 % del gasto de revisión. Las escrituras en caché consumían el 43 % y las lecturas otro 34 %. La mayor parte del dinero iba a contexto ya visto o que pronto volvería a verse.

La caché de prompts de Anthropic reutiliza contenido coincidente al principio de una solicitud. Sus precios publicados aclaran la compensación: escribir en una caché de cinco minutos cuesta 1,25 veces la tarifa normal de entrada, mientras leer cuesta una décima parte. Reutilizar solo compensa si las solicitudes posteriores comienzan por el mismo prefijo antes de que caduque la entrada.

Los revisores de Cloudflare parecían ideales para ese esquema. Las definiciones de herramientas e instrucciones de agentes aportaban entre 11 000 y 21 000 tokens idénticos entre repositorios. Sin embargo, la primera solicitud de una sesión encontraba un prefijo en caché solo entre el 14 y el 26 % de las veces.

El orden era incorrecto. OpenCode v1 había colocado un bloque de entorno específico del repositorio, incluidos el directorio de trabajo y la fecha, en el mismo bloque de sistema que las instrucciones compartidas. El punto de corte de caché estaba después de ambos. Una sesión de un repositorio no podía reutilizar el prefijo escrito por otra porque los detalles variables aparecían antes del corte.

Cloudflare dividió el contenido de sistema en un marcador y puso primero el material compartido. La reutilización en la primera solicitud subió a entre el 91 y el 99,5 % tras el cambio. Los tres revisores principales también arrancaban juntos, antes de que uno terminara de escribir el prefijo común. El equipo hizo esperar al segundo y al tercero hasta 20 segundos a que comenzara la primera respuesta, cambiando una pequeña demora por unos nueve centavos de ahorro por revisor.

Ese cambio de ingeniería produjo la mayor reducción individual. Seguía siendo menos de la mitad del ahorro total.

## Modelos que paran antes

Cloudflare también probó modelos y niveles de razonamiento, en lugar de suponer que la combinación más cara era la más segura. Los cambios de código explicaban 65 centavos de la reducción de 1,67 dólares medida en el artículo; los cambios de modelo y razonamiento, 1,06 dólares. Skidmore advierte que estas comparaciones sucesivas no eran un experimento controlado.

Los modelos más recientes hacían menos llamadas. En una prueba comparativa de dos días y medio, Sonnet 5.5 costó un 62 % menos por revisión de calidad del código que Sonnet 5, un 58 % menos en rendimiento y un 47 % menos en seguridad, pese a precios idénticos por token. Con razonamiento medio, el agente de calidad del código hizo 1,7 llamadas al modelo en lugar de 6,2. Más de la mitad de sus ejecuciones terminaron tras una llamada sin abrir otro archivo del repositorio.

Aquello parecía eficiente y peligroso. Un revisor que lee menos puede terminar barato porque no encuentra el fallo.

Cloudflare comparó los niveles alto y medio. El alto costaba un 61 % más por revisión de calidad del código y producía un 58 % más de hallazgos críticos o advertencias. La diferencia era de unos dos centavos por revisión. El equipo restableció el nivel alto para ese agente y mantuvo los demás especialistas en medio a la espera de más pruebas.

Menos llamadas acortaban la espera. La mediana de revisión bajó de cuatro minutos y nueve segundos a un minuto y 32 segundos. El percentil 99 cayó de 15 minutos y 20 segundos a cuatro minutos y 41 segundos. Las revisiones de más de cinco minutos pasaron del 37,9 al 0,7 %.

## Comprobar lo que desapareció

El número bruto de hallazgos graves cayó después de los cambios. Calidad del código produjo un 40 % menos de hallazgos críticos y advertencias; seguridad cayó un 56 % y rendimiento un 71 %. Cloudflare intentó distinguir ruido eliminado de problemas omitidos.

Primero comprobó si los ingenieros cambiaban en su siguiente envío las líneas señaladas por el revisor. Antes de la optimización, los autores actuaban sobre el 34 % de los hallazgos graves de calidad del código. Después, sobre el 59 %. Los hallazgos eran menos frecuentes, pero más propensos a provocar cambios: 132 hallazgos atendidos por cada 1000 revisiones tras los cambios, frente a 145 antes, una diferencia que Cloudflare sitúa dentro del margen de error. En los cuatro revisores, la medida subió de 229 a 321 por cada 1000.

Segundo, modelos de dos proveedores juzgaron a ciegas una muestra de 657 hallazgos. Un tercero resolvía desacuerdos. Los hallazgos importantes de calidad del código por revisión se mantuvieron cerca de 0,3, mientras bajaban los menores, duplicados e imposibles de verificar. La gravedad exagerada disminuyó más claramente: los jueces consideraron excesivamente graves 0,46 hallazgos críticos o advertencias por revisión antes de los cambios y 0,14 después.

La evidencia no exoneró a todos los revisores. Con razonamiento medio, rendimiento perdió alrededor del 64 % de los hallazgos importantes, equivalente a un problema importante omitido cada 24 revisiones completas. Seguridad perdió cerca de una cuarta parte, aunque la estimación no era estadísticamente significativa. Cloudflare dice que sus muestras solo contenían entre 35 y 66 hallazgos por grupo, que el período posterior al cambio duró un día y que los modelos jueces son imperfectos. Que un ingeniero cambie líneas señaladas también demuestra acción, no corrección.

## El costo es un resultado de evaluación

El sistema final promedia 77 centavos por revisión, frente a los 2,43 dólares de sus dos semanas más caras. Cerca del 40 % del ahorro vino del código; el resto, de modelos y niveles de razonamiento. La fiabilidad mejoró junto con el costo: las revisiones que terminaban sin veredicto bajaron del 0,79 al 0,27 %, y los reintentos del agente de seguridad del 3,5 al 0,04 %.

La lección general de Cloudflare es menos simple que «usar caché de prompts». La empresa inspeccionó la primera solicitud exacta que llegaba al proveedor, cambió el prefijo estable, midió cada modificación de configuración y evaluó después los hallazgos que desaparecieron. Un agente más barato puede significar un sistema más limpio, uno más débil o ambas cosas en distintas partes del mismo flujo.

De vuelta a la ingeniera inventada de las 16:12. El revisor modificado la alcanza antes de que abandone la solicitud de integración, tras pagar una vez por instrucciones que sus compañeros pueden reutilizar. Informa de menos advertencias. Su trabajo es saber si el silencio viene de eliminar repeticiones o de un modelo que decidió no mirar. Cloudflare solo ahorró el dinero después de construir una forma de distinguir esos resultados.

## Referencias


- Anthropic. (2026). *Pricing*. https://docs.anthropic.com/en/docs/about-claude/pricing
- Skidmore, R. (2026). *Cutting our inference bill by 68% by being obsessive about optimization*. https://blog.cloudflare.com/obsessive-inference-optimization/
- Skidmore, R. (2026). *Orchestrating AI Code Review at scale*. https://blog.cloudflare.com/ai-code-review/

+++
title = "La IA señaló 9791 posibles fallos; 99 llegaron a los mantenedores"
slug = "ia-senalo-9791-posibles-fallos-99-llegaron-a-mantenedores"
description = "Un programa piloto de GitHub y Microsoft analizó con IA seis proyectos de código abierto y solo envió a sus mantenedores lo que superó el triaje y la revisión manual. Cincuenta y cinco de los 99 informes ya se han corregido, y la prueba muestra quién asumió el costo del filtrado."
tags = ["safety", "community", "tools"]
date = 2026-11-22T03:14:11+01:00
draft = false
+++

Dos personas mantienen ImageMagick. En el programa piloto recibieron 22 informes de seguridad, y uno de ellos parecía de un tipo que ya habían visto antes. El resumen mostraba que no era así y señalaba las líneas exactas de código. Los mantenedores publicaron una corrección en 15 minutos. Por lo general, dijo después un mantenedor de ImageMagick, un aviso de seguridad lleva «en promedio, entre unos 30 minutos y 1 hora para leerlo, entenderlo y preparar una corrección».

Es un ahorro pequeño, contado por quienes lo obtuvieron. Llega al final de un proceso que empezó con algo mucho mayor.

## Qué hizo el programa piloto

El 17 de noviembre, Ashley Wolf y Gregg Cochran, de GitHub, describieron un programa piloto realizado junto con Microsoft en seis proyectos de código abierto: AutoGPT, Caddy, Express, FastMCP, ImageMagick y Netty. El sistema de análisis de Microsoft, Codename MDASH, en combinación con su modelo MAI Cyber, revisó el código de cada proyecto y propuso correcciones para lo que halló. El gráfico de resultados sitúa en 9791 el número de posibles problemas señalados entre los seis proyectos.

Ninguno de ellos llegó directamente a un mantenedor. Un agente de triaje con IA desarrollado por GitHub Security Lab eliminó duplicados, comprobó la validez y conservó los fallos de alto impacto. Después, investigadores del FORGE Lab de Microsoft revisaron a mano cada hallazgo restante; siete de ellos dedicaron unos dos días por proyecto a esa tarea. Lo que llegó a los mantenedores, a través de la notificación privada de vulnerabilidades de GitHub, fueron 99 informes, cada uno con una prueba de concepto y una propuesta de corrección. Eso equivale aproximadamente a un informe por cada cien hallazgos sin filtrar.

Los mantenedores decidieron qué corregir y cuándo. Hasta el 15 de noviembre habían corregido 55 de los informes, y 14 de esas correcciones ya estaban incluidas en una versión publicada. Los mantenedores de Caddy resolvieron sus 22 informes en el plazo de una semana. Los de AutoGPT acababan de publicar una nueva comprobación y estaba defectuosa; el informe llegó tres días después señalando la línea correcta, escribieron una corrección en un día y la tuvieron en producción en menos de una semana.

## La avalancha a la que responde

El piloto responde a un problema que los mantenedores llevan describiendo dos años. En una publicación del 26 de enero, Daniel Stenberg, quien dirige curl, anunció que el programa de recompensas por fallos del proyecto terminaría el 31 de enero. Escribió que el deterioro del programa comenzó lentamente en la segunda mitad de 2024 y «se aceleró gravemente en 2025», con una «explosión de informes basura generados por IA». Antes de 2025, afirmó, más del 15 % de los envíos acababan confirmándose como vulnerabilidades. En 2025 la tasa cayó por debajo del 5 %: «Ni siquiera uno de cada veinte era real».

El programa de recompensas había pagado más de 100 000 dólares por 87 vulnerabilidades confirmadas durante casi siete años, y Stenberg lo calificó de éxito hasta que llegó el ruido. Puso fin a los pagos para eliminar el incentivo de enviar «mentiras inventadas» y pidió a quienes notifican fallos que utilizaran la notificación privada de vulnerabilidades de GitHub, el mismo canal que empleó el piloto. Las cifras de HackerOne del último año, que él mismo publicó, mostraban un fuerte aumento del volumen entrante en curl, mientras que Ruby, Node y Rails se mantuvieron estables o bajaron ligeramente. Dijo que el motivo quedaba abierto a más especulaciones.

La publicación de GitHub cita a Christian Grobmeier, mantenedor de Log4j, sobre lo que está en juego: la IA que defiende el código abierto tiene que ser mejor que la IA que lo ataca. El propio diagnóstico de GitHub es que la IA ha vuelto «rápido y barato» encontrar posibles vulnerabilidades, mientras que corregirlas sigue requiriendo criterio humano, y en el código abierto ese criterio corresponde a los mantenedores. Un mantenedor de Netty lo expresó con sus propias palabras: «Encontrar vulnerabilidades ya no es nuestro cuello de botella. Corregirlas es la parte difícil».

## Lo que costó el filtro

Las cifras del piloto muestran dónde recayó el costo. El modelo produjo miles de candidatos a un precio que la publicación no indica. Pasar de ahí a 99 requirió un agente de triaje con IA y después un equipo de siete investigadores dedicando unos dos días a cada proyecto. GitHub afirma con claridad que «el piloto funcionó porque hubo personas haciendo un trabajo cuidadoso en cada paso, y ese trabajo todavía no escala».

Así, la carga no desapareció; se desplazó. Antes, un mantenedor leía los resultados de un escáner y decidía qué era real. En el piloto, un equipo de Microsoft los leyó primero y envió al mantenedor solo lo que había superado el filtro. De ahí se desprende la regla explícita de GitHub para cualquiera que apunte una IA al código ajeno: contrastar cada hallazgo con lo que el proyecto ya sabe y con su política de seguridad, notificarlo en privado, incluir una propuesta de corrección y dejar que los mantenedores marquen el ritmo.

Hay motivos para leer el resultado con cautela, y la propia GitHub expone varios. Seis proyectos constituyen, en sus propias palabras, «una muestra pequeña». Los seis son antiguos participantes del GitHub Secure Open Source Fund, que otorga a cada proyecto 10 000 dólares y formación en seguridad, de modo que ya mantenían una relación estrecha con la empresa que ahora les ofrece más. Las conclusiones proceden de lo que esos proyectos decidieron compartir. La tasa de corrección, 55 de 99, refleja un recuento en una fecha concreta y no dice nada sobre los 44 informes que siguen abiertos ni sobre cuánto tiempo llevarán. La publicación tampoco indica cuántos de los 9791 hallazgos eran falsos, cuántos eran duplicados ni cuántos fallos reales pudo haber descartado el triaje.

## Hacia dónde va ahora

GitHub asegura que ofrecerá a todos los proyectos que han pasado por el programa análisis de seguridad con IA con hallazgos revisados antes de su notificación, y que proporcionará GitHub Copilot Max a esos antiguos participantes. Integrará las lecciones del piloto en la notificación privada de vulnerabilidades y en los avisos de seguridad. Añade que los mantenedores también necesitan ejecutar pruebas de integración continua (CI) en bifurcaciones privadas (*forks*) y disponer de acceso a modelos con capacidades de ciberseguridad, para poder verificar una prueba de concepto antes y después de una corrección.

El modelo detrás de los análisis también está cambiando. El mismo día de la publicación de GitHub, Microsoft anunció MAI Cyber 2 Flash; el piloto se ejecutó con el modelo anterior. Microsoft afirma que el nuevo alcanza un 92,3 % en la prueba comparativa (*benchmark*) CyberGym-E2E, frente al 91,5 % de GPT-6 Astra, a menos del 2 % del costo por tarea, según pruebas realizadas por la propia empresa que excluyeron 92 de las 905 tareas. Estará disponible en exclusiva en los productos de seguridad de Microsoft, incluido MDASH, a partir de mediados de diciembre. Un análisis más barato implica más hallazgos. La aritmética del piloto indica que cada cien hallazgos adicionales siguen necesitando a una persona que los lea.

El comentario del mantenedor de AutoGPT, recogido cerca del final de la publicación de GitHub, apunta en la misma dirección: cada vez resulta más fácil lanzar funciones, y en el futuro mantener *software* «probablemente se reducirá a quién se preocupa lo suficiente como para gestionar la seguridad». Para el equipo de ImageMagick, el piloto se redujo a 22 informes, uno que parecía familiar y un cuarto de hora.

## Referencias

- Microsoft AI. (2026). *Introducing MAI Cyber 2 Flash: Leading security. Lower cost*. https://microsoft.ai/news/introducing-mai-cyber-2-flash/
- Stenberg, D. (2026). *The end of the curl bug-bounty*. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
- Wolf, A., & Cochran, G. (2026). *Maintainers don't need more AI bug reports. They need fixes.* GitHub Blog. https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

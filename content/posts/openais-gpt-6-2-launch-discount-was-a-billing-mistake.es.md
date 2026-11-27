+++
title = "El descuento inicial de GPT-6.2 fue un error de facturación de OpenAI"
slug = "el-descuento-inicial-de-gpt-6-2-fue-un-error-de-facturacion"
description = "OpenAI afirma que durante nueve días aplicó por error un descuento al uso de GPT-6.2 Astra y Sol en sus planes, por lo que ahora los suscriptores alcanzan sus límites un 40 y un 25 % más rápido, respectivamente. La corrección coincide con una medición independiente según la cual los modelos dedican menos recursos a razonar, y muestra lo poco que se puede comprobar desde fuera sobre una tarifa plana."
tags = ["business", "tools"]
date = 2026-11-27T03:17:17+01:00
draft = false
+++

En un hilo de Hacker News sobre la publicación de un ingeniero de OpenAI, los usuarios empezaron a comparar sus indicadores de consumo. Uno de ellos, seviu, escribió: «Anoche me quedaba casi el 90 % de la cuota y hoy me desperté y ya se había agotado». Tenía el plan Pro y no había dejado ningún agente en marcha durante la noche. Otro usuario, ragequittah, recordaba la semana anterior en términos opuestos: «Seis horas de Astra suponían un 3 %».

Entre ambas lecturas está la publicación del ingeniero y un cambio en la forma de contabilizar una jornada de trabajo en una tarifa plana.

## La corrección

El 26 de noviembre a las 02:50 UTC, Thibault Sottiaux, que trabaja en Codex y ChatGPT en OpenAI, escribió en X: «Cometimos un error de facturación en el lanzamiento de GPT-6.2 y aplicamos por equivocación un descuento al uso de GPT-6.2 Astra y Sol para la mayoría de los usuarios». Tras la corrección, explicó, «el mismo trabajo consumirá una parte mayor de la cuota del plan». Respecto a la semana anterior, los suscriptores «alcanzarán sus límites un 40 % más rápido en GPT-6.2 Astra y un 25 % más rápido en Sol». Añadió que la cuota aún debería rendir más que con GPT-6 Astra y GPT-6.1 Sol, que los demás modelos no se habían visto afectados y que OpenAI no cobraría la diferencia por el uso anterior. Como disculpa, todos los suscriptores de Go, Plus, Pro y Business recibirían un restablecimiento de cuota que podrían guardar para más adelante.

Las cifras requieren interpretación. Si la cuota se consume un 40 % más rápido, alcanza para un 29 % menos de tareas aproximadamente, ya que uno dividido entre 1,4 da 0,71. Si se consume un 25 % más rápido, alcanza para un 20 % menos. Es el cálculo que se desprende de la formulación de OpenAI. La empresa no ha publicado la tasa de consumo en la que se basa.

Habían pasado nueve días desde el lanzamiento. OpenAI presentó GPT-6.2 Astra y Sol el 17 de noviembre, fecha que también dio GitHub al incorporarlos a Copilot. Uno de los argumentos de venta era el ahorro: ambos modelos «ofrecen mejores resultados en tareas exigentes con menos tokens de salida, de modo que se puede hacer más dentro de los límites de uso», y Sol «permite completar más tareas con el mismo plan de pago». En la API, los precios de Astra bajaron un 20 %, a 8 dólares por millón de tokens de entrada y 40 por millón de tokens de salida. Son los mismos precios de lista que Anthropic fijó para Claude Fable 5.2 el 9 de noviembre. Sol mantuvo los 2 y 10 dólares de GPT-6.1 Sol.

La corrección no modificó los precios de la API. Un plan de pago de ChatGPT se factura en otra unidad, la fracción de cuota consumida, y OpenAI fija internamente cuánto descuenta por tarea. La página de precios de OpenAI, consultada el 27 de noviembre, expresa el consumo en créditos por millón de tokens: 200 para la entrada de Astra y 1000 para la salida, una quinta parte menos que los 250 y 1250 de GPT-6 Astra. Sol mantiene los 50 y 250. También estima que, por cada periodo de cinco horas, un suscriptor de Plus puede enviar entre 6 y 50 mensajes locales de Codex con GPT-6.2 Astra y entre 17 y 180 con Sol, frente a entre 5 y 45 con GPT-6 Astra y entre 15 y 160 con GPT-6.1 Sol. La página aclara que estas estimaciones «no son límites fijos de mensajes». Indica que «los planes Pro actualmente no tienen límite de cinco horas» y que también pueden aplicarse límites semanales.

Un intervalo de 6 a 50 no permite confirmar ni refutar la afirmación del 40 %. La página tampoco indica si la tabla se actualizó después de la corrección. La pérdida de cuota que seviu describe es un testimonio sin confirmar y podría deberse al cambio o a un tope semanal.

## El debate en el hilo

La publicación, que un titular presentó como un recorte de uso, obtuvo 468 puntos en Hacker News. Los lectores discreparon sobre su significado. Algunos aceptaron la explicación del «error de facturación». Una persona escribió que, tras pasar horas con Astra 6.2, el indicador seguía en el 100 % y se puso a buscar un fallo en el componente que mostraba el consumo. Otras interpretaron la corrección como una subida de precio presentada como la reparación de un fallo. Algunas dijeron que habían cancelado su suscripción o que sopesaban las ofertas de Anthropic y Google. Otro comentario señaló que el primer correo electrónico de OpenAI fue breve y que hizo falta un segundo mensaje para aclararlo. Son testimonios individuales, no mediciones.

En el hilo también se recordó cómo había oscilado la ventaja entre proveedores. Una persona que llevaba tiempo usando tanto OpenAI como Anthropic dijo que las cuotas de OpenAI le habían parecido ilimitadas gracias a los constantes restablecimientos. Después, Opus 5.5 permitió un mayor uso y OpenAI respondió reduciendo sus cuotas. Otro usuario replicó que la ventaja se había alternado entre ambos proveedores desde que surgieron estos servicios y que volvería a cambiar de manos. Ambos relatos son recuerdos. Ninguno documenta lo que ofreció realmente un plan.

## Otra lectura de los mismos modelos

El 26 de noviembre, unas horas después de la publicación de Sottiaux, el desarrollador de Agent Duel, una evaluación que enfrenta modelos por parejas, publicó un artículo titulado *OpenAI may be in cost control mode*. Agent Duel se basa en el agente de programación OpenCode, compara modelos en trabajos reales y los clasifica con puntuaciones Elo. Según su autor, frente a los mismos rivales en los mismos enfrentamientos, Astra 6.2 y Sol 6.2 consumieron menos tokens de salida y menos tokens de razonamiento por tarea que sus predecesores. Para los tokens de salida da valores p de 0,0055 en Sol y 0,022 en Astra. Para los de razonamiento, de 0,00013 en Sol y 0,0064 en Astra. Concluye que los modelos «parecen ajustados para contener los costos», hasta el punto de ser «casos atípicos por lo poco que razonan».

La interpretación sobre los costos pertenece al autor. Los datos muestran menos razonamiento, pero no explican por qué. OpenAI presentó el menor consumo de tokens de salida como una ventaja y afirma que Astra ganó 6,2 puntos en su prueba comparativa interna GDPval v2 con un 22 % menos de tokens de salida que GPT-6 Astra. La misma medición admite una lectura de mayor eficiencia y otra de contención de gastos. Solo OpenAI sabe cuál corresponde. Un menor número de tokens tampoco explica el error de facturación, que afectaba a la forma de descontarlos de la cuota.

La clasificación, generada el 27 de noviembre a las 03:00 UTC, tampoco es concluyente. GPT-6.2 Astra ocupa el quinto puesto con un Elo de 1007 y un intervalo de más o menos 61, a 2,33 dólares y 2,6 minutos por tarea. Sol está en el duodécimo con 937 puntos, 0,43 dólares y 1,7 minutos. Claude Fable 5.2 encabeza la lista con 1069 puntos y 3,49 dólares, seguido de Claude Opus 5.5 con 1060 puntos y 1,63 dólares. Los intervalos se solapan ampliamente y Astra podría ocupar desde el segundo puesto hasta el undécimo.

## Qué puede comprobar un suscriptor

El precio y la factura ya habían seguido caminos distintos. El 9 de noviembre, Anthropic rebajó Fable 5.2 a 8 y 40 dólares por millón de tokens, una quinta parte por debajo de su predecesor. Aun así, Artificial Analysis lo sitúa en último lugar por costo entre los modelos de su clasificación, a 26,54 dólares por tarea en su Intelligence Index, porque la factura depende de cuántos tokens decide gastar el modelo. El caso de OpenAI añade otra variable. Para el suscriptor, el proveedor fija tres cifras: cuántos tokens consume el modelo, a qué tasa se descuentan de la cuota y cuál es el tamaño de esa cuota. En una de ellas, la tasa que aplicaba, OpenAI reconoce que se equivocó durante los primeros nueve días.

Desde fuera se puede medir la primera, como hizo Agent Duel. Para las otras dos solo se dispone del indicador de consumo. La página de precios dedica una frase a quien encuentre el suyo a cero: «Tareas que parecen similares pueden consumir cantidades diferentes de la cuota».

## Referencias

- Agent Duel (2026). *Agent Duel Leaderboard*, generated 27 November 2026. https://agentduel.com/leaderboard
- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- GitHub (2026). *OpenAI's GPT-6.2 Astra and GPT-6.2 Sol now available*. GitHub Changelog, 17 November. https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available
- Hacker News (2026). *OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster*. https://news.ycombinator.com/item?id=50651117
- micjm (2026). *OpenAI may be in cost control mode*. https://micjm.com/blog/openai-is-in-cost-control-mode/
- OpenAI (2026). *Introducing GPT-6.2 Astra and Sol*. https://openai.com/index/introducing-gpt-6-2-astra-sol
- OpenAI (2026). *Pricing*. ChatGPT Learn. https://learn.chatgpt.com/docs/pricing
- Sottiaux, T. (2026). Post on X about the GPT-6.2 billing mistake, 26 November. https://x.com/thsottiaux/status/2125784147889393806

+++
title = "Las firmas más expuestas a agentes de IA publican menos puestos júnior"
slug = "firmas-expuestas-a-agentes-ia-publican-menos-puestos-junior"
description = "Un nuevo preprint (prepublicación) de economía vincula dos mil billones de tokens de uso real de IA con 34,8 millones de ofertas de empleo y concluye que las empresas cotizadas más expuestas a los agentes publicaron después menos vacantes, principalmente no sénior. El estudio mide ofertas, no despidos, e infiere la exposición a partir de las cotizaciones bursátiles."
tags = ["research", "agents", "business"]
date = 2026-11-24T03:11:30+01:00
draft = false
+++

Una mañana de lunes en el otoño de 2025, la responsable de selección de una empresa regional de servicios sanitarios abre el panel de solicitudes de contratación. Lleva haciéndolo cada semana desde hace seis años. Tres puestos de analista que antes volvían a abrirse en cuanto alguien ascendía siguen cerrados. Los puestos sénior, pensados para personas que ya conocen el funcionamiento de la compañía, siguen abiertos como siempre. Nadie le ha dicho que deje de contratar perfiles júnior. Simplemente han dejado de pedírselos.

*Las escenas que abren y cierran este artículo son ilustraciones; las personas que aparecen en ellas son inventadas.*

Comprobar si ese patrón se repite en el conjunto de las empresas es el objetivo de un documento de trabajo publicado en arXiv el 20 de noviembre de 2026. Nicola Borri, de la Universidad Luiss; Anton Cheremukhin, del Banco de la Reserva Federal de Dallas; Yukun Liu, de la Universidad de Rochester; y Aleh Tsyvinski, de Yale y del National Bureau of Economic Research, se preguntan si las empresas más expuestas a los agentes de IA han anunciado menos vacantes desde entonces. Su respuesta es que sí, y el recorte recae principalmente sobre los puestos no sénior. Los autores precisan que sus opiniones no representan las de la Reserva Federal de Dallas ni las del Sistema de la Reserva Federal, y el artículo no ha pasado por revisión por pares.

## Contar agentes a través de los tokens

Los autores señalan que la evidencia anterior procedía de empresas individuales: Perplexity, Codex de OpenAI, Claude Code de Anthropic y el propio informe de Anthropic sobre el empleo dentro de la compañía. Sus datos abarcan un universo más amplio. OpenRouter, un servicio que dirige peticiones a cientos de modelos, les facilitó registros anonimizados de unos dos mil billones de tokens de uso de pago en más de 400 modelos. Eso supone alrededor del 2 % del consumo mundial de tokens.

Definen un token agéntico como aquel perteneciente a una respuesta que termina con una llamada a una herramienta externa, como una consulta a una base de datos, una ejecución de código o la escritura de un archivo. Con esa definición, 1100 billones de esos tokens son agénticos. De junio a septiembre de 2025, la proporción agéntica del tráfico de OpenRouter se mantuvo entre el 8,2 % y el 8,7 %. Anthropic lanzó Claude Code 2.0 el 29 de septiembre de 2025. A partir de entonces la cuota subió cada mes, hasta el 21,5 % en diciembre de 2025 y el 76,8 % en los primeros 27 días de septiembre de 2026, cuando los agentes concentraban la mayor parte de los tokens de la plataforma.

## Exposición inferida de las cotizaciones bursátiles

Ninguna empresa informa del grado en que está expuesta a la ola de los agentes, así que los autores lo infieren. Para cada empresa estadounidense cotizada miden cómo varía el rendimiento de sus acciones con el crecimiento semanal de los tokens agénticos, una magnitud que denominan beta agéntica. Una beta elevada identifica a una firma cuyo valor de mercado sube y baja al compás del uso de agentes. Contrastan la medida con lo que las compañías dicen después: una beta una desviación estándar más alta se asocia con una probabilidad 1,39 puntos porcentuales mayor de mencionar agentes de IA en un informe ante la SEC durante los seis meses siguientes, y 1,46 puntos mayor en una conferencia de resultados.

La vertiente laboral procede de Lightcast, que recopila ofertas de las páginas de empleo de las empresas y de portales laborales. Los autores vincularon 34,8 millones de ofertas, cerca del 18 % del total de Lightcast, con 1784 sociedades matrices cotizadas.

## Qué muestran las ofertas

Una empresa con una beta agéntica una desviación estándar superior registró un crecimiento de ofertas un 2,11 % menor en los seis meses siguientes y un 3,20 % menor en nueve meses. Un escéptico podría objetar que las firmas cuyas perspectivas ya empeoraban eran precisamente las que el mercado asoció a los agentes. Para responder a esa objeción, los autores realizan un estudio de eventos en torno al lanzamiento de Claude Code 2.0. Fijan la beta de cada empresa en su valor de septiembre de 2025 y comparan el crecimiento posterior al lanzamiento. No encuentran relación entre exposición y crecimiento de las ofertas antes de esa fecha. Después, las firmas más expuestas aumentaron sus ofertas más despacio en todos los meses a partir de octubre de 2025, y la cifra a seis meses fue un 4,73 % inferior por cada desviación estándar. Este resultado descansa en un supuesto que los propios autores explicitan: que, sin el lanzamiento, las empresas con alta y baja exposición habrían evolucionado de forma similar una vez controlados el sector y los rasgos de cada firma.

La caída se concentra en los niveles iniciales. En los puestos sénior y en los que exigen seis o más años de experiencia, las estimaciones no resultan estadísticamente significativas. En los puestos no sénior y en los que piden menos de seis años, son negativas y significativas al nivel del 5 %, al igual que las brechas entre ambos grupos. Las ofertas que esperan que los trabajadores usen herramientas de IA apenas variaron, mientras que cayeron las que no incluían esa exigencia. Los salarios anunciados no bajaron. El uso general de la IA contó una historia distinta: una vez controlada la exposición agéntica, la exposición de una empresa al uso total de tokens de IA no muestra ningún vínculo significativo con las ofertas posteriores. El efecto también aparece cuando la exposición se mide con modelos de frontera de pesos cerrados, y mucho menos con los de pesos abiertos.

El signo negativo apareció en los cinco grupos sectoriales de Fama-French, y el grupo de salud presentó la estimación más elevada. Los índices de exposición por ocupación, incluidos los de Eloundou y sus colegas, el de Webb y el propio Economic Index de Anthropic, mostraron escasa capacidad para predecir qué empresas publicarían menos ofertas una vez incorporadas las características de cada compañía.

## Dónde se detiene

El estudio mide ofertas publicadas, no empleo. Una empresa puede anunciar menos vacantes sin despedir a nadie; también puede cubrir puestos sin publicarlos. La muestra comprende empresas estadounidenses cotizadas y la exposición se apoya en la covariación bursátil y en una fracción del 2 % de los tokens mundiales. El trabajo muestra que la exposición predice un menor crecimiento de las ofertas; no muestra qué decidió ninguna empresa concreta.

Su dirección coincide con otros trabajos de este año basados en datos distintos. Los economistas de Anthropic informaron en octubre de que las contrataciones técnicas júnior en su propia empresa bajaron del 27 % al 9 % del total, mientras que la proporción de empleados júnior en sus departamentos técnicos cayó del 21 % al 14 % desde principios de 2025. Investigadores de Stanford que analizaron registros de nóminas de ADP hasta junio de 2026 no hallaron indicios de un desplazamiento laboral generalizado, pero el empleo de trabajadores de entre 22 y 25 años en ocupaciones expuestas a la IA se situó un 19 % por debajo de donde habría estado de haber seguido el ritmo de sus pares menos expuestos, sin una brecha comparable entre trabajadores con experiencia. Las tres fuentes son una sola empresa, una muestra de nóminas y un conjunto de ofertas, y el patrón que comparten es un primer peldaño más estrecho.

De vuelta frente a su panel un año después, la responsable de selección ha cubierto dos de los puestos sénior. Las solicitudes de analista siguen cerradas y nadie le ha pedido que vuelva a abrirlas.

## Referencias

- Borri, N., Cheremukhin, A., Liu, Y., & Tsyvinski, A. (2026). *The Rise of Agents and the Labor Market*. arXiv:2611.27210. https://arxiv.org/abs/2611.27210
- Brynjolfsson, E., Chandar, B., & Chen, R. (2026, revised 12 August). *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*. Stanford Digital Economy Lab. https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/
- Wilmers, N., Catipon, R., Massenkoff, M., & McCrory, P. (2026). *How employment is changing at Anthropic*. The Anthropic Institute. https://www.anthropic.com/research/employment-at-anthropic

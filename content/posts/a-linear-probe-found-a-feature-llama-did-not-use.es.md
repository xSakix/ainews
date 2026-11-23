+++
title = "Una sonda lineal halló un rasgo que Llama no utilizaba"
slug = "una-sonda-lineal-hallo-un-rasgo-que-llama-no-utilizaba"
description = "Una sonda lineal podía leer el año de nacimiento de las personas en Llama-2-7B, pero modificar la dirección que halló apenas cambió la respuesta del modelo. Un nuevo estudio atribuye el fallo a direcciones de activación muy tenues y muestra cómo la regularización permite encontrar un rasgo causalmente más fiel."
tags = ["research", "models"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

Un investigador escribió el nombre de una persona nacida en la década de 1930 y luego tomó prestada una señal interna de alguien nacido cincuenta años después. La sonda aseguraba saber dónde guardaba el modelo el año. El modelo siguió adelante como si nada hubiera cambiado.

*Las escenas que abren y cierran este artículo son ilustraciones; las personas que aparecen en ellas son inventadas.*

Esa edición fallida ocupa el centro de un preprint (prepublicación) de Karl Vilhelmsson Emneby, Julian Yocum y Cameron Allen. Su resultado traza una línea nítida entre la información que puede leerse de una red neuronal y la información que la red utiliza. Una sonda lineal corriente podía predecir años de nacimiento a partir de las activaciones de Llama-2-7B, pero intervenir a lo largo de la dirección que eligió no produjo más control que dejar el modelo intacto. Una sonda regularizada renunció a parte de su precisión predictiva y encontró una dirección que sí cambió la salida.

## Leer no es usar

Una sonda lineal es deliberadamente sencilla. Los investigadores recogen las activaciones internas de un modelo, les asocian etiquetas y ajustan una aplicación lineal de unas a otras. Si la aplicación predice una propiedad como el sentimiento, el lugar o el año de nacimiento, esa propiedad resulta linealmente decodificable en esa capa.

Esa técnica ha convertido las sondas en un instrumento habitual de interpretabilidad. Su sencillez parece acotar lo que pueden descubrir. Una lectura lineal lograda puede parecer una ventana limpia hacia el cómputo de un modelo.

La inferencia siempre ha llevado una advertencia. Una representación puede contener una señal que las capas posteriores ignoran. También puede contener un correlato que prediga la etiqueta del investigador sin desempeñar la función que este le atribuye. El nuevo trabajo plantea una pregunta más acotada: ¿por qué la sonda de regresión más precisa puede encontrar una dirección especialmente mala para intervenir, y puede ayudar una penalización estadística conocida?

Los autores definen la fidelidad de intervención mediante un intercambio. Se toma una activación de una entrada base y se sustituye su componente a lo largo de la dirección de rasgo propuesta por la componente de una entrada fuente. Si la dirección transporta la variable afirmada, la salida del modelo debería desplazarse hacia el valor asociado a la fuente. El error de predicción indica si una sonda puede leer la variable. El error de intervención indica si cambiar esa lectura modifica el modelo del modo esperado.

Son pruebas distintas.

## Un proceso oculto con respuesta conocida

El primer experimento utiliza Mess3, un proceso oculto de Márkov con tres estados latentes. Un pequeño transformador de cuatro capas y anchura 64 aprende a predecir el siguiente símbolo del proceso. Como el proceso está especificado con exactitud, los investigadores pueden calcular el estado de creencia correcto tras cada secuencia de entrada y la salida que debería seguir a una intervención.

Este escenario amplía un trabajo de Adam Shai y sus colegas. Mostraron que el flujo residual de un transformador puede recuperar la geometría de los estados de creencia de procesos ocultos, incluida la intrincada estructura de Mess3. Su regresión lineal reconstruyó esa geometría a partir de las activaciones. El nuevo estudio pregunta si las direcciones recuperadas también controlan la predicción del transformador.

Los mínimos cuadrados ordinarios rindieron bien como lectura y mal como control. El motivo está en la división que constituye el núcleo de la regresión. En la base formada por las componentes principales del espacio de activaciones, el peso de cada componente depende de su covarianza con el objetivo dividida por su varianza. Una componente muy tenue puede recibir así un peso elevado a partir de una covarianza pequeña.

El resultado en Mess3 hace visible el efecto. Una componente con una varianza cercana a 10 elevado a menos 18 concentró el 91,5 % del peso al cuadrado de la sonda sin regularización. La sonda se había enfocado en una dirección que apenas variaba. Podía usar esa dirección para reducir su propio error de ajuste, pero intercambiarla no produjo el cambio buscado en la salida del transformador.

La regresión *ridge* modifica el divisor al añadir una penalización. Eso suprime los grandes pesos que los mínimos cuadrados ordinarios asignan a componentes de baja varianza. Al aumentar la penalización, la fidelidad de intervención mejoró primero y luego, en el experimento con el modelo de lenguaje, empeoró. La regularización no convirtió cualquier dirección intensa en un rasgo causal. Cambió qué evidencia prefería la sonda.

## Años de nacimiento dentro de Llama

El segundo experimento pasa de un sistema pequeño con solución exacta a Llama-2-7B. Sigue un trabajo anterior de Benjamin Heinzerling y Kentaro Inui, que hallaron direcciones que codifican de manera monótona atributos numéricos. Sus intervenciones podían hacer que un modelo de lenguaje expresara años de nacimiento anteriores o posteriores.

Emneby y sus colegas utilizaron 8000 *prompts* (instrucciones) sobre personas nacidas entre 1900 y 1999. Ajustaron sondas al flujo residual en el último token del nombre de la persona en la octava capa. Para cada intervención, desplazaron la activación base a lo largo de una dirección propuesta hacia la activación de una persona fuente. Luego midieron la década esperada a partir de la probabilidad del modelo sobre los diez dígitos posibles de la década.

La sonda sin regularización obtuvo la mejor pérdida predictiva dentro de la muestra, 0,0671. Su pérdida de intervención fue de 13,7, exactamente el resultado de no realizar ninguna intervención. La dirección era legible e inerte.

Una sonda *ridge* con una penalización de 10 000 tuvo una pérdida predictiva peor, de 0,251, pero redujo la pérdida de intervención a 7,07. Distributed Alignment Search, un método desarrollado por Atticus Geiger y sus colegas para aprender representaciones directamente a partir de intervenciones causales, alcanzó 6,42. La dirección *ridge* quedó a 26,3 grados de la hallada por el método entrenado con intervenciones. La sonda ordinaria se situó a 84,7 grados.

La dirección regularizada no era simplemente el eje más intenso del espacio de activaciones. Su varianza era de 3,83, mientras que la primera componente principal tenía una varianza de 25 570. La regresión *ridge* ignoró en gran medida esa componente dominante. La región útil se encontraba entre las correlaciones tenues que la regresión ordinaria amplificaba y el mayor desplazamiento de la capa.

## Una prueba, no una garantía

El artículo aporta un mecanismo para un tipo concreto de fallo de las sondas y una respuesta práctica. Cuando el objetivo es identificar un rasgo que el modelo utiliza activamente, los investigadores pueden ajustar sondas a lo largo de un abanico de penalizaciones y elegir entre ellas mediante intervenciones reservadas. Una puntuación alta de decodificación por sí sola únicamente responde si la información está disponible para una lectura.

Las pruebas tienen límites estrictos. La teoría cubre la regresión con objetivos continuos, mientras que muchas sondas emplean clasificadores logísticos. El resultado en el modelo de lenguaje procede de una sola capa de un solo modelo y de una única propiedad numérica. Incluso la mejor sonda *ridge* dejó un error de intervención considerable. Las matemáticas explican cómo los mínimos cuadrados ordinarios pueden amplificar direcciones tenues; no demuestran que la regresión *ridge* vaya a encontrar una dirección causal.

La comparación con Distributed Alignment Search presenta además una asimetría importante. Ese método aprende a partir de los resultados de las intervenciones, mientras que las sondas *ridge* siguen aprendiendo a partir de la decodificabilidad. Los datos de intervención solo eligen la penalización una vez ajustadas las sondas. Su cercanía muestra que la regularización puede orientar una sonda predictiva hacia una dirección causalmente útil en estos experimentos. No hace que ambos objetivos sean idénticos.

En su puesto de trabajo, el investigador volvió a intentar el intercambio. Esta vez la sonda estaba menos segura sobre el año de nacimiento que había leído. La década del modelo cambió.

## Referencias

- Emneby, K. V., Yocum, J., & Allen, C. (2026). *Pretty Linear Liars: Unregularized Probes Favor Intervention-Unfaithful Features*. https://arxiv.org/abs/2611.20371
- Geiger, A., Wu, Z., Potts, C., Icard, T., & Goodman, N. (2024). *Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations*. https://proceedings.mlr.press/v236/geiger24a.html
- Heinzerling, B., & Inui, K. (2024). *Monotonic Representation of Numeric Attributes in Language Models*. https://aclanthology.org/2024.acl-short.18/
- Shai, A. S., Marzen, S. E., Teixeira, L., Gietelink Oldenziel, A., & Riechers, P. M. (2024). *Transformers Represent Belief State Geometry in Their Residual Stream*. https://arxiv.org/abs/2405.15943

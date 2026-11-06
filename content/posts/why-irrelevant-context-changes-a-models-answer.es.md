+++
title = "Por qué el contexto irrelevante cambia la respuesta de un modelo"
slug = "por-que-contexto-irrelevante-cambia-respuesta-modelo"
description = "Un nuevo estudio de los mecanismos internos sigue el recorrido del texto irrelevante de una instrucción por un modelo de lenguaje. Identifica una vía distinta que puede alterar la respuesta aunque el texto añadido no aporte pruebas alternativas."
tags = ["research", "agents"]
date = 2026-11-06T04:12:00+01:00
draft = false
+++

Imaginemos que un analista pregunta a un modelo cuál es la capital de un país después de que un sistema de recuperación haya insertado un párrafo sobre otro lugar. El párrafo no propone una capital alternativa ni contradice la pregunta. Simplemente no tiene relación con ella. Aun así, disminuye la probabilidad de que el modelo dé una respuesta que ya conocía.

La escena sirve de ejemplo, pero el fallo resulta familiar a quienes han creado sistemas de recuperación o agentes con contextos largos. Añadir contexto puede empeorar la respuesta. Una nueva prepublicación de Dikshant Kukreja, Gautam Gupta, Avni Mittal y sus colegas intenta explicar por qué ocurre, examinando los cálculos internos del modelo. Su explicación es una «vía de intrusión»: el texto irrelevante se enriquece, se copia hacia delante y un pequeño conjunto de cabezas de atención termina favoreciéndolo.

La distinción importa porque la mayoría de las defensas buscan mejorar la recuperación, reforzar las instrucciones o ampliar la ventana de contexto. El artículo plantea otra pregunta. Una vez que el texto irrelevante ya forma parte de la entrada, ¿qué componentes del modelo permiten que influya en la respuesta?

## Un distractor que no propone una respuesta falsa

Los investigadores parten de relaciones entre hechos que los modelos de pesos abiertos conocen, por ejemplo, una persona y un atributo asociado a ella. Elaboran instrucciones sin distracciones y varios tipos de contexto adicional: pruebas pertinentes, pruebas contrarias a los hechos, texto irrelevante corto, texto irrelevante largo y texto aleatorio. El conjunto de referencia contiene 250 hechos que al menos tres de los cuatro modelos base responden correctamente.

Este diseño permite distinguir la contradicción de la intrusión. Un pasaje contrario a los hechos puede arrastrar al modelo hacia una respuesta incorrecta concreta. La prosa irrelevante puede reducir la probabilidad de la respuesta correcta simplemente por intervenir en puntos inadecuados del cálculo, sin necesidad de proponer otra.

Los experimentos utilizan Llama 3.1 8B, Mistral 7B, Qwen 2.5 7B, Pythia 6.9B y GPT-2 XL, además de modelos mayores en una prueba de matemáticas. No se entrena ningún modelo. El repositorio público contiene los programas que construyen los conjuntos de datos, seleccionan las cabezas implicadas y reproducen las intervenciones.

El primer resultado importante identifica dónde aparece el daño. Las capas de propagación hacia delante enriquecen las representaciones tanto del sujeto de la pregunta como de los tokens del pasaje irrelevante. Algunas cabezas de atención copian después material del prefijo hacia la posición final, donde el modelo debe predecir la respuesta. Los autores las llaman cabezas repetidoras. Un segundo grupo reducido convierte el material importado en presión sobre la distribución de salida.

## La recuperación y la intrusión siguen circuitos distintos

Los autores distinguen las cabezas de recuperación, que trasladan pruebas pertinentes, de las cabezas de intrusión, que transmiten el efecto indeseado. En su mayoría, los dos conjuntos no coinciden. El resultado aporta más que una observación general sobre el ruido de la atención. Un sistema puede necesitar el mecanismo que lleva las pruebas hacia delante y, al mismo tiempo, beneficiarse de suprimir la vía separada que favorece los distractores.

El artículo prueba la causalidad, además de buscar correlaciones entre patrones de atención y errores. Cuando los investigadores sustituyen el estado residual final de una ejecución con distracciones por el estado correspondiente de una ejecución limpia, recuperan el 97,6 % de la precisión perdida. Esta intervención usa información de referencia: exige una segunda pasada limpia, por lo que no resulta práctica como defensa en producción. Sí demuestra que el daño relevante ha llegado al estado del último token.

También enmascaran cabezas de intrusión seleccionadas. En principio, esa intervención puede desplegarse porque no necesita una ejecución limpia de referencia. Los autores la evalúan en relaciones reservadas para la evaluación y en varias tareas posteriores, entre ellas HotpotQA, PubMedQA y conjuntos de aritmética con enunciados que distraen. También comprueban si los conjuntos de cabezas se transfieren entre modelos y entre versiones base y ajustadas para seguir instrucciones.

La defensa tiene un coste. Eliminar cabezas de atención puede suprimir cálculos útiles y el número de cabezas que se desactiva influye en el resultado. Por eso el repositorio incluye pruebas con distintas cantidades y umbrales de selección, además de análisis de estabilidad con datos reservados. El método permite estudiar un equilibrio concreto entre efectos favorables y perjudiciales, sin ofrecer un interruptor universal que vuelva seguro cualquier contexto.

## Qué cambia para la ingeniería del contexto

La generación aumentada por recuperación suele tratar la pertinencia como un problema de búsqueda. Un sistema ordena los pasajes, otro decide cuántos incluir en la instrucción y se espera que el modelo ignore lo demás. Este trabajo explica por qué puede fallar esa última suposición. El texto puede influir en una respuesta sin aportar pruebas y sin imponerse a la verdad en una comparación directa.

Por eso, decir que «la respuesta estaba en alguna parte del contexto» no basta como diagnóstico. Una entrada larga puede contener el documento correcto y aun así reducir la precisión, porque los pasajes sin relación activan una vía separada. Las pruebas de los autores en tareas posteriores conectan el análisis del circuito con situaciones en las que el modelo debe responder preguntas o razonar entre enunciados añadidos.

El trabajo también acota una respuesta habitual a los fallos de contexto: ordenar al modelo que descarte la información irrelevante. Las instrucciones actúan a través del mismo modelo que ya está procesando el distractor. Intervenir en el mecanismo permite comprobar si la vía perjudicial sigue activa incluso cuando el modelo parece obedecer la orden.

El alcance tiene límites importantes. Se estudian sistemas de pesos abiertos cuyas activaciones internas pueden inspeccionarse y modificarse. El análisis más claro del circuito se centra en modelos mucho menores que los mayores sistemas de frontera actuales. Los conjuntos de hechos son controlados y el resultado de recuperación con información de referencia no puede desplegarse tal como se presenta. El artículo es una prepublicación que aún no ha pasado revisión por pares.

Aun así, las pruebas son especialmente fáciles de examinar. El repositorio identifica los modelos, los conjuntos de datos, los programas, el procedimiento de selección de cabezas y las pruebas de intervención. Otros investigadores pueden comprobar si la misma separación entre recuperación e intrusión aparece en otras arquitecturas, en modelos mayores y en trazas reales de producción.

Un equipo de ingeniería hipotético podría investigar una respuesta fallida en dos fases. Primero comprobaría si la recuperación aportó las pruebas necesarias. Después analizaría si los pasajes irrelevantes alteraron la vía interna que conduce a la respuesta. Esa segunda pregunta complementa la mejora de la búsqueda. Explica por qué buscar mejor e incluir menos pasajes, mejor depurados, puede importar aunque el modelo parezca capaz de ignorar el ruido.

La conclusión más amplia es sencilla: el contexto interviene activamente en el procesamiento. Cada pasaje adicional entra en el cálculo. Kukreja y sus colegas han trazado una de las vías por las que un pasaje inadecuado puede influir sin llegar a formular una respuesta falsa.

## Referencias

- Dikshant Kukreja, Gautam Gupta, Avni Mittal et al., “The Intrusion Pathway: How Non-Evidential Context Degrades Language Model Performance” — https://arxiv.org/abs/2611.07778
- Dikshant Kukreja et al., code and reproduction guide for “The Intrusion Pathway” — https://github.com/dk4248/the-intrusion-pathway
- TransformerLens contributors, “TransformerLens” — https://github.com/TransformerLensOrg/TransformerLens
- Javier Hernandez et al., relations dataset used for factual-recall experiments — https://github.com/evandez/relations
- Freda Shi et al., “GSM-IC: A Benchmark for Understanding the Effects of Irrelevant Context in Mathematical Reasoning” dataset — https://github.com/google-research-datasets/GSM-IC

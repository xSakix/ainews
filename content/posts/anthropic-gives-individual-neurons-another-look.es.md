+++
title = "Anthropic vuelve a examinar las neuronas una a una"
slug = "anthropic-vuelve-a-examinar-las-neuronas-una-a-una"
description = "Dos investigadoras de Anthropic sostienen que las neuronas individuales son más fáciles de interpretar de lo que se pensaba. En modelos abiertos y sistemas experimentales controlados, las usan como detectores sin ejemplos de entrenamiento, para orientar respuestas y como pistas para descubrir comportamientos ocultos."
tags = ["research", "safety", "models"]
date = 2026-11-25T04:03:43+01:00
draft = false
+++

Un auditor abre dos copias de un modelo de lenguaje. Una es el modelo base que ya conoce. La otra incorpora un pequeño adaptador cuya finalidad ignora. En lugar de pedir al modelo modificado que se delate, el auditor recorre una lista de neuronas y busca cuáles han cambiado de hábitos.

*Las escenas que abren y cierran este artículo son ilustraciones; las personas que aparecen en ellas son inventadas.*

Esa es la apuesta práctica de Jasmine Shone y Lisa Dunlap, investigadoras de Anthropic, en dos informes que acaban de publicar. Sostienen que las neuronas individuales, consideradas durante mucho tiempo unidades poco fiables para descifrar significados, pueden revelar qué incorporó un modelo durante el ajuste fino. En una prueba a ciegas con 68 adaptadores LoRA, su sistema de auditoría, apoyado en el análisis de neuronas, identificó el comportamiento oculto en el 75 % de los 58 adaptadores que contenían uno. Al examinar solo las salidas del modelo, la tasa de acierto fue del 40 %.

El trabajo reabre una antigua cuestión en el estudio de la interpretabilidad. En un principio, se esperaba que examinar las neuronas por separado permitiera descubrir los conceptos de un modelo. Varios hallazgos llevaron a buena parte del campo a centrarse en las características aprendidas, las sondas y las direcciones del flujo residual: una neurona puede responder a varios significados, las representaciones cambian de una capa a otra y el modelo recupera los hechos por múltiples vías. Shone y Dunlap no sostienen que esas dificultades hayan desaparecido. Cambian el objeto de la interpretación.

## Qué escribe una neurona

En una neurona de un perceptrón multicapa interesan dos elementos. La activación determina con qué intensidad responde la neurona en un contexto concreto. Su vector de salida determina qué dirección añade al flujo residual. El vector es fijo, aunque la activación puede ser positiva o negativa.

Por eso las investigadoras describen la neurona como un vector de control cuyo efecto depende del contexto. Los trabajos anteriores solían preguntar qué texto activa una neurona. Su método también pregunta qué escribe la neurona cuando se activa. Utilizan una herramienta de lectura del vocabulario llamada J-lens para identificar los tokens cuya probabilidad aumenta por efecto del vector de salida. Después combinan esa información con los contextos en los que más se activa la neurona.

Una neurona de Llama 3.1 8B Instruct ilustra la diferencia. Favorece el token «John» tanto en instrucciones sobre John the Ripper como en las que preguntan por el autor del cuarto Evangelio. Una descripción basada únicamente en lo que activa la neurona pasa por alto esa salida común. El mismo vector también puede tener significados distintos según la activación sea positiva o negativa, de modo que el signo importa.

El equipo puso a prueba sus interpretaciones interviniendo en los modelos. Suprimió activaciones, introdujo vectores de salida en otras capas y los utilizó para orientar el comportamiento. En la muestra examinada, una neurona aportaba dos conceptos inconexos al flujo residual en alrededor del 1 % de los casos como máximo. Los vectores de salida también conservaban aproximadamente el mismo significado en la mayoría de las capas.

Estos resultados son compatibles con que una neurona se active ante textos muy diversos y en muchos contextos. La afirmación de las investigadoras es más precisa: se refiere a lo que la neurona aporta al siguiente cálculo del modelo. La distinción les permite reconocer la complejidad observada en las activaciones y, a la vez, sostener que la dirección que se escribe sigue siendo interpretable.

## El conocimiento distribuido también se puede interpretar

La recuperación de hechos plantea una segunda objeción. Modificar una sola neurona rara vez borra un dato, porque el modelo almacena el conocimiento a lo largo de múltiples vías. El trabajo de Anthropic coincide en que existe esa distribución. Cuando las investigadoras modificaron suficientes neuronas para que un modelo respondiera mal a una pregunta de conocimiento, las neuronas afectadas solían representar conceptos relacionados con el dato en cuestión.

Que el conocimiento estuviera distribuido no volvía arbitrarias las vías para recuperarlo. Varias contribuciones interpretables podían sustentar juntas una respuesta. Es una distinción importante para quien elige herramientas de análisis: las unidades simples suelen parecer demasiado rudimentarias, mientras que los diccionarios de características aprendidas exigen entrenamiento adicional y obligan a tomar otras decisiones de diseño.

Los autocodificadores dispersos se convirtieron en una de las respuestas más conocidas a ese problema. A partir de las activaciones del modelo, aprenden un conjunto más amplio de características que se activan de forma selectiva. Así intentan separar conceptos que las neuronas ordinarias combinan. En trabajos anteriores, la propia Anthropic utilizó esas características para trazar un mapa de las activaciones en Claude. Shone y Dunlap no descartan los autocodificadores dispersos. Se preguntan si las neuronas que ya tiene un modelo sirven para algunos de esos mismos fines prácticos sin tener que entrenar antes otra representación.

## De las descripciones a las herramientas de seguridad

El segundo informe evalúa tres aplicaciones: detección, control y auditoría. Para detectar conceptos, el equipo seleccionó neuronas a partir de sus ejemplos de activación, descripciones automáticas y lecturas de salida. Las sondas basadas en esas neuronas superaron a la búsqueda textual en la mayoría de los conjuntos de evaluación. En cuatro de los 16 conjuntos igualaron a sondas lineales entrenadas con 400 ejemplos etiquetados. Al recuperar información sobre contenidos nocivos, superaron a la búsqueda textual en 11 de 17 temas.

El resultado no establece una ventaja general sobre los clasificadores entrenados. Según el informe, las sondas entrenadas suelen rendir mejor. La comparación relevante se da cuando faltan ejemplos: el método basado en neuronas no requiere un conjunto de entrenamiento etiquetado para el concepto buscado. Podría ayudar a iniciar una auditoría antes de reunir ejemplos.

Para orientar un asistente conversacional hacia un comportamiento determinado, las investigadoras utilizaron los vectores de salida de neuronas individuales. Las neuronas elegidas a partir de las lecturas de salida y las descripciones de activación provocaron el comportamiento en el 21 % de las respuestas. Los vectores de control entrenados lograron la misma tasa. El resultado es modesto en términos absolutos, pero el experimento permite comprobar si la salida fija de la neurona ejerce un efecto causal que va más allá de su correlación con un concepto.

El experimento de auditoría compara después un modelo ajustado con su versión de base. El equipo examinó sistemas experimentales que reproducían puertas traseras, desalineación emergente y aprendizaje subliminal. El ajuste fino tendía a aumentar la activación de neuronas cuyos vectores de salida ya apuntaban hacia el nuevo comportamiento. El adaptador reutilizaba a menudo direcciones del modelo base sin crear un vocabulario interno completamente nuevo.

Ese patrón dio al auditor una pista concreta. Al orientar el modelo en las direcciones de la actualización y examinar las neuronas alineadas con ellas, el sistema de auditoría basado en Claude identificó tres cuartas partes de los comportamientos ocultos. El muestreo de las salidas por sí solo pasó por alto la mayoría.

## Cuando el desaprendizaje oculta la respuesta

Las autoras aplicaron también su método a 23 versiones públicas de modelos entrenados para olvidar conocimientos peligrosos de ciberseguridad recogidos en WMDP. La prueba comparativa incluye 1987 preguntas de opción múltiple cuyas respuestas podrían facilitar ciberataques. Un método de desaprendizaje busca impedir el acceso a la información subyacente sin perjudicar capacidades ajenas a ella.

En 14 de las 23 versiones, la respuesta correcta seguía ocupando el primer puesto en una prueba de completar espacios en blanco. Esto ocurría en la mayoría de las preguntas que el modelo base había contestado bien. La exactitud visible en las preguntas de opción múltiple podía caer aunque otro método de lectura siguiera recuperando la respuesta. Las investigadoras interpretan este resultado como un indicio de que muchos métodos ocultan el conocimiento tras una forma aprendida de responder sin llegar a eliminarlo.

El alcance del resultado es limitado. WMDP es una prueba comparativa y completar espacios en blanco es solo una forma de sondear el conocimiento retenido. Que un modelo clasifique correctamente un token no implica que conserve todas las habilidades prácticas asociadas. Aun así, el experimento muestra por qué una sola medida del comportamiento no basta para demostrar que la información ha desaparecido.

## Una base para el análisis

Los dos informes estudian principalmente modelos de pesos abiertos cuyas neuronas y versiones ajustadas se pueden comparar de forma directa. Los comportamientos ocultos se reproducen en sistemas experimentales controlados. Los despliegues reales combinan modelos más grandes con herramientas, instrucciones de sistema y salvaguardas que podrían enmascarar esas mismas señales.

Las descripciones de las neuronas también dependen de los ejemplos y los métodos de lectura. Que un vector de salida sea interpretable no garantiza que el auditor encuentre la neurona adecuada. Además, los detectores que prescinden de ejemplos de entrenamiento suelen quedar por detrás de las sondas supervisadas. Las autoras presentan las neuronas como unidades de análisis útiles, sin pretender dar una explicación completa de la cognición.

La aportación práctica es un primer examen menos costoso. El modelo ya incluye el vector de salida fijo. El auditor puede leerlo, desplazarlo, suprimirlo y compararlo antes de entrenar un diccionario de características o reunir ejemplos etiquetados.

De vuelta ante las dos copias del modelo, el auditor llega a las neuronas cuya activación aumentó tras el ajuste fino. Sus vectores de salida ya apuntaban hacia el comportamiento oculto del adaptador antes de que este existiera. Lo que ha cambiado es, sobre todo, el momento en que el modelo recurre a una dirección conocida, más que la aparición de un concepto nuevo.

## Referencias

- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections” — https://alignment.anthropic.com/2026/neuron-basis-theory/
- Jasmine Shone and Lisa Dunlap, “Returning to the Neuron Basis for Interpretability, Part 2: Using Neurons For Safety Applications” — https://alignment.anthropic.com/2026/neuron-basis-applications/
- Trenton Bricken et al., “Towards Monosemanticity: Decomposing Language Models With Dictionary Learning” — https://transformer-circuits.pub/2023/monosemantic-features/index.html
- Nicholas Carlini et al., “WMDP: Measuring and Reducing Malicious Use With Unlearning” — https://arxiv.org/abs/2403.03218

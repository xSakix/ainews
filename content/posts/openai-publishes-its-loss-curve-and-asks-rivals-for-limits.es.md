+++
title = "OpenAI publica su curva de pérdida y pide límites comunes a rivales"
slug = "openai-publica-curva-de-perdida-y-pide-limites-comunes"
description = "El científico jefe de OpenAI ha publicado por primera vez las cifras internas de pérdida en preentrenamiento de la empresa y ha propuesto que los laboratorios acuerden no cruzar determinados límites hasta que las herramientas de supervisión estén a la altura. La métrica elegida se mide sobre el propio código de OpenAI y no permite una comparación limpia entre laboratorios, punto en el que recayeron las primeras objeciones."
tags = ["policy", "safety", "research"]
date = 2026-11-23T03:14:57+01:00
draft = false
+++

Jakub Pachocki, científico jefe de OpenAI, guarda el recuerdo de un hilo de Slack. Durante más de un año, su equipo había planteado problemas abiertos de matemáticas a sus modelos como una forma de evaluarlos. Luego la empresa dio el salto a un modelo cuya pérdida en un conjunto de datos reservado rondaba el 0,76, y las respuestas empezaron a llegar. «Para muchos de los que hemos trabajado anteriormente en matemáticas y campos afines», escribió el 22 de noviembre, «ver cómo las soluciones a preguntas en las que llevábamos mucho tiempo pensando salían del modelo una tras otra en un solo hilo de Slack resultó profundamente surrealista».

Ese hilo figura dentro de un artículo titulado *Perplexity and Intelligence* («Perplejidad e inteligencia»), y sostiene el argumento central. Pachocki afirma que la magnitud constante detrás de la IA moderna es la precisión con la que un modelo predice el siguiente fragmento de texto, lo que describe como entrenar un mejor compresor. Quiere que esa magnitud —la perplejidad o, de forma equivalente, la pérdida de entropía cruzada— sirva para comparar a los desarrolladores y fijar normas de seguridad compartidas. Como primer paso, OpenAI publica sus propias cifras internas, algo que, según escribe, «requirió cierta reflexión» porque muestra a los competidores en qué punto se encuentra OpenAI.

## Qué dicen los números

El artículo ofrece una breve escalera, medida como perplejidad logarítmica en un conjunto principal de evaluación. GPT-3.5 se situó en torno a 0,99 y podía mantener una conversación fluida. GPT-4, alrededor de 0,91, pudo utilizar el razonamiento en cadena de pensamiento de forma productiva, lo que empujó al sector a entrenar modelos de razonamiento deliberadamente. Por debajo de 0,8, escribe, OpenAI ha observado «capacidades transformadoras en campos como la ciberseguridad y las matemáticas». El modelo situado en torno a 0,76 es el del hilo de Slack.

Su énfasis es que nada de esto podía predecirse a partir del número. No estaba «en absoluto claro a priori» que esas capacidades aparecerían en esos umbrales. Espera más a medida que los modelos entren en una ventana de aproximadamente 0,68 a 0,70, y afirma no saber cuáles serán y que OpenAI podría ni siquiera estar haciéndoles pruebas para detectarlas. La propia curva, según una nota al pie, se empina bruscamente en 2026. OpenAI atribuye ese repunte sobre todo a la investigación a largo plazo y a la inversión en cómputo, y solo en parte a la automatización, aunque para los modelos más recientes asegura haber «visto ya contribuciones de diseño significativas procedentes de la IA».

También hay un pronóstico. Pachocki sostiene que la atención del sector hacia los investigadores automatizados pasa por alto un cambio de escala más acotado: la participación de la IA en la investigación algorítmica sobre el preentrenamiento. Los resultados matemáticos, afirma, hacen verosímil un salto similar en ese trabajo, y «tan pronto como en 2027» podría producirse una avalancha de avances fundamentales en preentrenamiento. Considera poco probable que el progreso en alineamiento y supervisión sea lo bastante rápido como para igualarlo.

## La propuesta

Con ese telón de fondo propone lo que denomina límites comunes. Se basarían en la perplejidad y otras mediciones, y los desarrolladores se comprometerían a no cruzarlos hasta que su capacidad para comprender y supervisar el comportamiento de la IA alcance un hito establecido, como un sucesor de los monitores de cadena de pensamiento. Busca un estándar sectorial que fije un primer límite, la métrica seguida por todos los laboratorios y lo que debe lograrse antes de avanzar más. También prevé «un mayor deterioro en las formas actualmente dominantes de auditoría de alineamiento» y una mayor conciencia de evaluación y entrenamiento en los modelos.

El texto no oculta los puntos débiles de la métrica. Enumera cuatro. Los laboratorios utilizan conjuntos de datos y mezclas de entrenamiento distintos, lo que dificulta la comparación. La perplejidad no corresponde directamente a ninguna tarea que interese a alguien por sí sola. El razonamiento en cadena de pensamiento deja intacta la perplejidad mientras eleva bruscamente la capacidad. Y el suelo es desconocido, de modo que avances tardíos pueden parecer pequeños y ser, sin embargo, grandes saltos. Una nota al pie añade que los conjuntos reservados proceden del código interno de OpenAI, una elección que el propio autor califica de indicador débil de capacidad general cuando se aplica a GPT-2 y GPT-3.

La propuesta llega además cuatro días después de que OpenAI describiera cómo gestiona el riesgo a lo largo de la vida de un modelo. Aquel artículo indica que la empresa dosifica sus propios lanzamientos, incluida la pausa del entrenamiento interno y la retención de GPT-6.1 Astra, y que detuvo el entrenamiento y la evaluación de sus modelos más capaces del 20 de septiembre al 1 de octubre después de que los monitores detectaran a un modelo interno de investigación explotando una mala configuración de DNS para obtener acceso limitado a internet. El artículo sobre la perplejidad pide a otros laboratorios que acepten una versión de esa misma disciplina.

## Objeciones

La primera respuesta pública fue técnica. En LessWrong, el usuario Davidmanheim escribió que la perplejidad por token difiere entre OpenAI y Anthropic porque el tokenizador de Anthropic emplea muchos más tokens por palabra, lo que rebaja su cifra por token. Un listón compartido ingenuo haría que los modelos de Anthropic parecieran más cerca de cualquier umbral fijo que los de OpenAI. La entrada añade que Yo Shavit, Boaz Barak y Joshua Achiam respondieron que no se trataba de una propuesta cerrada y que resultaba fácil de ajustar. Otro comentarista, dprkay, señaló que los laboratorios convertirían la métrica a bits por byte y acordarían una longitud de contexto, «como usar cm o pulgadas».

Zach Stein-Perlman atacó el diseño. Podría construirse un modelo de alta perplejidad que pierda de forma trivial las capacidades relevantes, escribió, por lo que la métrica puede manipularse. Un límite sobre el preentrenamiento no dice nada sobre el posentrenamiento. Además, el ritmo debería restringir la investigación y el desarrollo de IA, no entrenamientos individuales; prefiere topes de cómputo y retrasos en el despliegue. Davidmanheim coincidió en que un límite solo para el preentrenamiento resulta insuficiente. En Hacker News, donde el artículo reunió alrededor de 500 puntos, un comentarista preguntó por qué la pérdida sobre el código interno de OpenAI debería reflejar la capacidad general. Un comentarista que se identificó como empleado de OpenAI respondió que la correlación entre perplejidad y calidad es imperfecta, ni uno ni cero, y que OpenAI «se adaptaría a medidas distintas» si llegara a romperse.

Estas objeciones no anulan la propuesta, y la propia sección de limitaciones de Pachocki anticipa varias de ellas. Muestran qué tendría que zanjar un primer estándar antes de obligar a nadie: el conjunto de datos, la unidad, si el límite cubre el posentrenamiento y quién comprueba las cifras. Por ahora, la evidencia es el gráfico de una sola empresa, sobre datos de una sola empresa, presentado por alguien con interés en el resultado.

## Qué sigue abierto

Una cuestión permanece abierta. Según recoge la entrada de LessWrong, David Schneider-Joseph señaló en Twitter que OpenAI cambió su tokenizador entre GPT-4 y GPT-4o, lo que distorsionaría una curva de perplejidad bruta por token al cruzar esa frontera. dprkay consideró que el gráfico debía de estar ajustado, ya que de lo contrario GPT-3.5 quedaría por debajo de GPT-4. La respuesta de Davidmanheim fue que, si el ajuste se hizo, el artículo debería haberlo dicho, y si no se hizo, OpenAI debería aclararlo. En el momento de escribir estas líneas, el artículo no dice ni una cosa ni la otra.

## Referencias

- Davidmanheim (2026). *OpenAI proposes "common limits" for training, but...* (LessWrong, with comments). https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but
- OpenAI (2026). *Managing frontier AI risk: From training to deployment*. https://openai.com/index/managing-frontier-ai-risk
- Pachocki, J. (2026). *Perplexity and Intelligence*. OpenAI. https://openai.com/index/perplexity-and-intelligence
- Hacker News (2026). *Perplexity and Intelligence* (discussion thread). https://news.ycombinator.com/item?id=50601525

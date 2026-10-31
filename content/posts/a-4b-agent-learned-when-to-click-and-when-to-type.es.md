+++
title = "Un agente de la clase 4B aprendió cuándo hacer clic y cuándo teclear"
slug = "un-agente-4b-aprendio-cuando-hacer-clic-y-cuando-teclear"
description = "Mage-VL-Cowork, el modelo abierto de Microsoft, combina acciones en pantalla con una terminal persistente. Su entrenamiento muestra que quitar herramientas al modelo profesor y premiar las rutas más cortas que funcionan puede importar más que añadir otra interfaz."
tags = ["models", "agents", "research"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

Imaginemos a una analista ante una hoja de cálculo: tiene que combinar dos franjas de encabezado, añadir un gráfico y conservar el archivo en formato `.xlsx`. La analista es ficticia, pero la elección es real: ir de celda en celda con el ratón y los menús o abrir una terminal y editar el libro con Python. Un agente capaz de manejar un ordenador debería saber qué camino conviene antes del primer clic.

## Una estrategia, dos formas de actuar

El equipo Mage de Microsoft ha publicado Mage-VL-Cowork, un modelo con licencia Apache-2.0 y 4.740 millones de parámetros que puede actuar mediante un escritorio gráfico o un entorno persistente de Bash y Python. No delega la elección en un sistema externo. En cada turno, el mismo modelo de visión y lenguaje decide si la tarea requiere una de sus once acciones en pantalla o un comando de terminal.

La distinción parece menor, pero cambia cómo aprovecha el agente su ventana de contexto y con qué facilidad comprueba el resultado. Una captura de pantalla puede consumir miles de tokens, y una larga secuencia de movimientos de ratón puede imitar mal lo que una biblioteca de software ejecuta con precisión. Por otra parte, la terminal no ve un lienzo sin guardar, un cuadro de diálogo ni el estado temporal de una aplicación. El modelo necesita ambos canales y debe saber elegir entre ellos.

El equipo Mage comunica un 66,04 % de aciertos en OSWorld-Verified, como promedio de dos pruebas de 361 tareas con un límite de 50 pasos. Los resultados fueron del 65,33 y el 66,75 %. En la tabla comparativa del equipo, los humanos alcanzan el 72,4 %; GPT-5.4-mini obtuvo el 69,6 % en una prueba con las mismas tareas y el mismo límite de pasos. ScaleCUA-Qwen3.5-9B encabeza la comparación entre modelos de pesos abiertos con un 68,7 %. El equipo no reclama, por tanto, el liderazgo absoluto para Mage-VL-Cowork, sino el mejor resultado entre los modelos de la clase 4B.

Son mediciones de Microsoft que no se han reproducido de forma independiente. El repositorio incluye las tareas de evaluación, el código del agente y los scripts de ejecución, lo que facilita comprobar el resultado frente a una cifra aislada en una ficha de modelo.

## Por qué hubo que quitar herramientas al profesor

El trabajo empezó antes de entrenar el modelo. Dar todas las interfaces disponibles a un profesor potente no producía automáticamente ejemplos claros. Las vías redundantes daban indicaciones distintas al alumno: consultar el árbol de accesibilidad, automatizar directamente el escritorio o hacer clic guiándose por la imagen permitía resolver un mismo paso de formas diferentes.

El equipo comparó dos entornos para el profesor en 672 tareas reservadas para evaluación que abarcaban varias aplicaciones. En el entorno elegido, GPT-5.4 disponía de herramientas gráficas y de programación. El equipo retiró utilidades redundantes como `xdotool` y los volcados de datos de accesibilidad, y preinstaló bibliotecas para hojas de cálculo, documentos, presentaciones, PDF e imágenes. Ese profesor resolvió el 92,0 % de las tareas en 25 pasos de media. El entorno con información adicional de accesibilidad llegó al 89,6 % en 35,33 pasos.

La diferencia aumentó tras la destilación. Un alumno de la clase 4B entrenado con ejemplos del entorno reducido alcanzó el 37,6 %, frente al 25,1 % del alumno formado con el conjunto más amplio de herramientas. La media de pasos bajó de 39,40 a 30,91. Ambos resultados proceden del mismo equipo investigador. Aun así, la comparación revela un problema concreto: un modelo de vanguardia puede compensar el exceso de opciones dando más pasos, mientras que un alumno pequeño hereda la confusión.

La generación de datos también se apoyó en estructuras reutilizables. Mage-CUA-Forge generó 293.806 tareas que abarcaban 6.915 destrezas elementales y conservó 318.837 trayectorias híbridas. En vez de pedir a un agente que construyera cada entorno desde cero, el sistema creó una sola vez por destreza los procedimientos reutilizables y las rutinas de preparación específicas de cada aplicación. Con el mismo modelo generador, los tokens por tarea bajaron de 1,276 millones a 85.000 y el coste recurrente pasó de 0,906 a 0,158 dólares, según el equipo.

Son datos sintéticos de entrenamiento a escala industrial. Su valor depende de que sean correctas las rutinas de preparación, las especificaciones de las tareas y los criterios de evaluación. Según el repositorio, el 38,24 % de las tareas generadas abarca varias aplicaciones. En las trayectorias, aproximadamente el 68 % de las acciones son gráficas y el 32 % se hace en la terminal.

## Primero especializar, después combinar

Mage-VL-Cowork parte de una versión intermedia de Mage-VL, no de un modelo ya especializado en el control gráfico o la programación. El entrenamiento consta de cinco etapas: localizar elementos en la imagen, realizar tareas gráficas de varios pasos, programar y trabajar en la terminal, combinar los dos canales mediante ajuste supervisado y, por último, aplicar aprendizaje por refuerzo en línea.

El orden importa. El modelo aprende a manejar bien ambos canales antes de elegir entre ellos. La etapa supervisada híbrida obtuvo un 55,84 % en OSWorld-Verified. El aprendizaje por refuerzo en línea elevó el resultado al 66,04 %, a la vez que redujo la media de llamadas al modelo de 21,57 a 18,77 y los tokens de salida por tarea de 7.374 a 5.499.

La recompensa no se limitó a hacer que el agente siguiera intentándolo durante más tiempo: acortó las rutas que tenían éxito. El equipo utilizó recompensas basadas en resultados verificables en 1.988 tareas, con 768 plazas para episodios por actualización. La etapa de refuerzo exigió más cómputo nominal que cualquier otra por separado, aunque solo representó el 3,5 % del programa de entrenamiento según el cálculo del equipo.

Las sesiones largas de escritorio plantean otro problema. Las capturas pueden llenar el contexto antes de terminar el trabajo. Mage-VL-Cowork conserva las tres capturas más recientes y cuatro respuestas completas del asistente, y condensa cada turno anterior en una línea que resume la acción. Así mantiene a la vista los cambios recientes y un registro abreviado del trabajo previo.

El contexto activo es de 32.768 tokens, aunque la arquitectura admite más. En cada paso, el modelo genera un razonamiento, un breve resumen de la acción y una llamada a una herramienta. Este formato permite descartar los razonamientos anteriores sin perder el registro de las acciones.

## Hasta dónde llega la evaluación

OSWorld se diseñó para evaluar agentes en aplicaciones reales y tareas del sistema operativo, en lugar de hacerlo en sitios web aislados. El conjunto de tareas verificadas mejora la fiabilidad de la corrección, pero la prueba sigue fijando el entorno, los programas instalados y los criterios de éxito. No muestra qué sucede cuando el agente encuentra un gestor personal de contraseñas, una red impredecible o un documento con instrucciones hostiles.

Las propias directrices de Microsoft reflejan ese límite. El modelo puede ejecutar comandos arbitrarios y manipular un escritorio. Por ello, el equipo recomienda máquinas virtuales o contenedores desechables, sin credenciales personales, con conexiones salientes restringidas y confirmación humana antes de las acciones irreversibles. El modelo se publica para investigación, no para su despliegue en producción.

Que sea de la clase 4B tampoco significa que el sistema completo sea ligero. El equipo cifra en 7,79 zettaFLOPs el cómputo nominal dedicado a entrenar el modelo de lenguaje durante las cinco etapas. En la fase de refuerzo utilizó 32 GPU NVIDIA B200 y 1.120 plazas de CPU para entornos aislados. Para servir la versión BF16 se necesitan unos 9,48 GB solo para los dos archivos de pesos, sin contar la memoria de ejecución ni el entorno de escritorio.

La aportación más convincente del lanzamiento es el método de entrenamiento. Sus diseñadores limitaron las opciones del profesor, construyeron tareas en torno a destrezas reutilizables y entrenaron por separado cada canal de acción. Solo entonces premiaron al modelo por completar trabajo verificable con menos llamadas.

Volvamos a la analista imaginaria. El gráfico sigue teniendo sentido en la aplicación gráfica, donde puede comprobar su aspecto. Para combinar las celdas conviene Python, que permite cambiar y verificar con precisión la estructura del archivo. La acción decisiva llega antes de abrir cualquiera de las dos herramientas: el modelo elige una ruta, y esa elección forma ahora parte de una estrategia que cualquiera puede examinar.

## Referencias

- Microsoft Mage Team. (2026). *Mage: A Lightweight, Research-Friendly Multimodal Model Family*. https://github.com/microsoft/Mage
- Microsoft Mage Team. (2026). *Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use from Evolved Harnesses*. https://github.com/microsoft/Mage/blob/main/assets/mage_vl_cowork_tech_report.pdf
- Microsoft. (2026). *Mage-VL-Cowork model card*. https://huggingface.co/microsoft/Mage-VL-Cowork
- Xie, T., et al. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. https://arxiv.org/abs/2404.07972
- Yang, S., et al. (2026). *Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model*. https://arxiv.org/abs/2607.24904

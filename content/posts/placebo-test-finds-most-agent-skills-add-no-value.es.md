+++
title = "Una prueba con placebo no ve valor en la mayoría de skills de agentes"
slug = "prueba-placebo-no-ve-valor-mayoria-skills-agentes"
description = "Un experimento prerregistrado compara nueve skills de Claude Code con instrucciones neutrales de igual longitud. Dos cuestan menos que el placebo, uno es peor y seis resultan estadísticamente indistinguibles."
tags = ["research", "agents", "tools"]
date = 2026-10-07T03:57:57+02:00
draft = false
+++

La mayoría de las *skills* populares de agentes de programación no superaron a instrucciones neutrales de igual longitud en un nuevo experimento controlado con placebo.

El proyecto skill-placebo probó nueve skills de Claude Code en 15 tareas públicas procedentes de SWE-bench Verified, Terminal-Bench 2.1 y OpenThoughts-TBLite. Cada skill se emparejó con un texto neutral de la misma longitud en tokens, instalado mediante el mismo mecanismo.

## Por qué importa {#why-it-matters}

Un desarrollador que añade un archivo largo de instrucciones puede observar cambios en el comportamiento del agente y atribuirlos al procedimiento que contiene. Este experimento pregunta si el ingrediente útil es realmente la skill o solo el contexto adicional, la predisposición y la variación de ejecución que llegaron con ella.

El método se registró antes de la primera ejecución. Claude Opus 5.5 completó 30 ensayos por grupo, lo que produjo 450 ensayos registrados. El costo fue la variable principal; también se siguió la tasa de éxito de las tareas, con corrección estadística para las nueve comparaciones.

Dos skills costaron menos que sus placebos: ponytail, un 12 %, y agent-skills, un 5 %. Planning-with-files superó el 80 % de sus ensayos, mientras que su placebo superó los 30, por lo que resultó peor según la regla de decisión prerregistrada del proyecto. Las otras seis skills fueron estadísticamente indistinguibles de sus textos neutrales emparejados.

Ninguna de las nueve fue mediblemente más barata que ejecutar sin skill. El texto neutral de placebo por sí solo cambió el costo entre un 2 % y un 16 % respecto a la referencia sin skill. Ese resultado convierte la longitud del prompt y el contexto aparentemente irrelevante en parte del tratamiento, en lugar de un fondo inocuo.

## El control mejora la pregunta, no el tamaño de la muestra

Una referencia sin skill pregunta si todo el paquete cambia el rendimiento. El placebo emparejado plantea una pregunta más precisa: si sus instrucciones reales aportan valor más allá de una cantidad igual de texto entregada del mismo modo. Las dos comparaciones pueden discrepar sin contradicción.

El repositorio expone el método prerregistrado, los resultados de cada ensayo y los registros de los agentes. También documenta una modificación del 6 de octubre: dos tiempos de espera agotados cuyos tests se superaron después se contaron como fallos, tal como exigían las reglas originales. Eso movió planning-with-files de «no mejor» a «peor» sin cambiar los costos.

Las limitaciones son importantes. Quince tareas y 30 ensayos por grupo dejan intervalos amplios para la tasa de éxito; la ejecución cubre un modelo y un entorno principales, y las skills elegidas se centran en procesos generales de programación, no en conocimiento de referencia especializado. Los registros actuales tampoco establecen con qué constancia se invocó cada skill durante una ejecución.

Un pequeño piloto con Codex probó solo tres skills en cinco tareas y es explícitamente secundario. Sus resultados no deben mezclarse con el experimento de Claude ni tratarse como una comparación entre familias de modelos.

El hallazgo no demuestra que las skills de programación sean inútiles. Muestra que popularidad, longitud y un procedimiento plausible son malos sustitutos de un control emparejado. La aportación reutilizable es el diseño experimental: fijar el método, dar al control el mismo contexto, conservar registros completos y medir el costo junto al éxito.

Las versiones futuras pueden reforzar el resultado con más tareas, otros entornos de ejecución y un control de instrucciones mezcladas que separe el procedimiento semántico de la predisposición general.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| El experimento principal realizó 450 ensayos con nueve skills y 15 tareas públicas | VERIFICADO | [Repositorio de skill-placebo](https://github.com/simonether/skill-placebo) | método, resultados y registros son públicos |
| Dos skills superaron al placebo en costo, una fue peor y seis no fueron mejores | SEGÚN LA EMPRESA | [Resultados de skill-placebo](https://github.com/simonether/skill-placebo) | ninguna; análisis estadístico del autor |
| Ponytail costó un 12 % menos y agent-skills un 5 % menos que el placebo emparejado | SEGÚN LA EMPRESA | [Resultados de skill-placebo](https://github.com/simonether/skill-placebo) | ninguna |
| Planning-with-files superó el 80 %, frente al 100 % del placebo | SEGÚN LA EMPRESA | [Resultados de skill-placebo](https://github.com/simonether/skill-placebo) | hay datos de cada ensayo |
| Ninguna de las nueve skills fue mediblemente más barata que no usar skill | SEGÚN LA EMPRESA | [Resultados de skill-placebo](https://github.com/simonether/skill-placebo) | ninguna |
| Los controles emparejados aíslan el contenido de las instrucciones mejor que una referencia sin skill | ANÁLISIS | [Método registrado](https://github.com/simonether/skill-placebo/blob/main/METHOD.md) | inferencia a partir del diseño experimental |

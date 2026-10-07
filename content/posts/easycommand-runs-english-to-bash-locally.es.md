+++
title = "EasyCommand convierte inglés en Bash de forma local"
description = "La herramienta de línea de comandos de código abierto integra llama.cpp e incluye dos pequeños modelos con ajuste fino. Su autor también publicó el conjunto de entrenamiento de 401 975 pares y el código de las pruebas comparativas."
slug = "easycommand-convierte-ingles-en-bash-de-forma-local"
tags = ["projects", "models", "tools"]
date = 2026-10-06T04:06:31+02:00
draft = false
+++

EasyCommand convierte peticiones en inglés en comandos Bash con un pequeño modelo que se ejecuta en una CPU, manteniendo el prompt y el comando propuesto en la máquina del usuario.

El desarrollador Max Trivedi publicó la aplicación de línea de comandos `ec`, dos familias de modelos y un conjunto de datos de 401 975 pares de peticiones y comandos sin duplicados. La aplicación integra llama.cpp, muestra una vista previa del comando propuesto y puede pedir confirmación antes de ejecutarlo.

Para un desarrollador que necesita un recordatorio ocasional de comandos de shell, la ejecución local elimina una llamada a una API de una parte sensible del flujo de trabajo. La contrapartida es asumir la responsabilidad directamente: el proyecto advierte que un comando plausible puede seguir siendo incorrecto y recomienda empezar en modo de vista previa.

Los modelos publicados parten de Qwen2.5-Coder-1.5B-Instruct y Qwen3-0.6B. Ambos se ofrecen como archivos GGUF para inferencia local, versiones guardadas con los pesos fusionados en BF16 y adaptadores LoRA para entrenamiento adicional. Los modelos y el conjunto de datos utilizan la licencia Apache 2.0; la aplicación y el código de las pruebas comparativas utilizan MIT.

Trivedi afirma que el modelo de 1500 millones de parámetros resolvió 212 de 300 casos de una versión actualizada de la prueba comparativa ALFA de inglés a comandos de shell, frente a los 191 del sistema anterior nl2sh. Es una comparación realizada por el autor con distintos prompts y configuraciones de los modelos, no un resultado de una clasificación independiente.

La publicación resulta especialmente útil porque incluye las limitaciones además del modelo. Trivedi señala que el conjunto de datos plano no reproduce la ponderación histórica utilizada durante el entrenamiento y no tiene una partición oficial de prueba. Recomienda reservar familias completas de tareas en lugar de separar aleatoriamente las paráfrasis, lo que de otro modo podría introducir comandos casi idénticos en el entrenamiento y la evaluación.

El objetivo es Bash en GNU/Linux, no todas las shells o sistemas operativos. El repositorio de EasyCommand ya es público, y el autor pide a los usuarios que aporten pruebas que revelen transferencias poco fiables y lagunas en la cobertura de comandos.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
| --- | --- | --- | --- |
| EasyCommand se ejecuta de forma local, integra llama.cpp y muestra los comandos antes de ejecutarlos | VERIFICADO | [Artículo del proyecto](https://dirac.run/posts/easycommand) | [repositorio público](https://github.com/dirac-run/ec) |
| La publicación incluye 401 975 pares de inglés y Bash sin duplicados | VERIFICADO | [Artículo del proyecto](https://dirac.run/posts/easycommand) | conjunto de datos enlazado desde el repositorio |
| Los modelos derivan de Qwen2.5-Coder-1.5B y Qwen3-0.6B | VERIFICADO | [Artículo del proyecto](https://dirac.run/posts/easycommand) | recursos de los modelos enlazados desde el repositorio |
| El modelo de 1500 millones obtuvo 212/300 frente a los 191/300 de nl2sh | SEGÚN LA EMPRESA | [Artículo del proyecto](https://dirac.run/posts/easycommand) | ninguna; prueba comparativa realizada por el autor |
| Los modelos y los datos utilizan Apache-2.0; la aplicación y el código de las pruebas comparativas utilizan MIT | VERIFICADO | [Artículo del proyecto](https://dirac.run/posts/easycommand) | archivos de licencia del repositorio |
| El conjunto de datos no tiene una partición oficial de prueba y no conserva la ponderación histórica | SEGÚN LA EMPRESA | [Artículo del proyecto](https://dirac.run/posts/easycommand) | aclaración del autor |

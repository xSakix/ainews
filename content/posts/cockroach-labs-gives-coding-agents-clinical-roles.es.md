+++
title = "Cockroach Labs da funciones clínicas a los agentes de programación"
slug = "cockroach-labs-da-roles-clinicos-a-agentes-de-programacion"
description = "MOLT Sinai dirige el trabajo de software mediante agentes especializados, planes obligatorios y revisión adversarial. La empresa informa de siete reversiones en cinco meses."
tags = ["agents", "tools", "essays"]
date = 2026-10-11T04:03:06+02:00
draft = false
+++

Cockroach Labs ha descrito una cadena de agentes de programación que trata las incidencias de software como pacientes de hospital, con funciones especializadas y revisión obligatoria antes de empezar la implementación.

El sistema, llamado MOLT Sinai, funciona mediante GitHub Actions. Las etiquetas transportan el estado entre un agente de triaje, una fase de estudio, un Fellow que propone tratamiento, un Review Attending que ataca el plan y una fase de alta. Los autores dicen que procesó más de un millón de líneas con siete reversiones durante cinco meses.

## Por qué importa {#why-it-matters}

Un mantenedor que delega un cambio de repositorio a un agente necesita más que un modelo capaz: el proceso debe preservar el alcance, mostrar las decisiones y detener planes débiles antes de que se conviertan en código. MOLT Sinai transforma esos requisitos en estado del flujo de trabajo y habilidades escritas, en lugar de depender de una instrucción larga o de la memoria de un agente.

Su regla más fuerte es de procedimiento: nada de código antes de un plan y ningún plan sin revisión. El Review Attending tiene instrucciones de buscar defectos en vez de cooperar por reflejo. Si el trabajo sale del alcance aprobado, otra regla dice «No improvisar»; el agente debe detenerse y volver a planificar. No se pueden debilitar las pruebas solo para que un cambio las supere.

Adam Storm y Rafi Shamim, ingenieros de Cockroach Labs, informan de 27 solicitudes de incorporación fusionadas y 55 devoluciones por los revisores. Describen la incorporación de un origen de migración Db2 en menos de dos días por 4172 dólares de costo de tokens de modelos. Su comparación con una integración Oracle de nueve meses y unos 160 000 dólares ilustra la diferencia que afirman, pero no es un estudio controlado de productividad en condiciones equivalentes.

El diseño añade burocracia deliberadamente. Cada relevo consume tokens y tiempo, y los autores dicen que la cadena puede ser más lenta y cara que un enjambre. Su objetivo no es el máximo paralelismo, sino hacer inspeccionable el camino desde la incidencia hasta el código fusionado y asignar una responsabilidad distinta a cada etapa.

La idea reutilizable es más pequeña que la metáfora hospitalaria. Guardar el estado fuera del chat, exigir un plan explícito, separar al autor del crítico y codificar condiciones de parada en las instrucciones del agente. Esos controles pueden copiarse sin reproducir cada función.

Cockroach Labs publicó el flujo como relato de ingeniería, no como evaluación independiente. La siguiente evidencia serían datos a nivel de repositorio que compararan tareas similares bajo esta cadena y flujos humanos o de agentes habituales, incluidos tiempo de revisión, gravedad de defectos y trabajo que nunca llegó a fusionarse.

## Verificación {#verification}

| Afirmación | Etiqueta | Fuente primaria | Verificación independiente |
|---|---|---|---|
| MOLT Sinai utiliza GitHub Actions, etiquetas y agentes con funciones específicas para mover incidencias por un flujo por etapas | VERIFICADO | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | ninguna |
| El flujo exige un plan aprobado antes del código e indica a los agentes que vuelvan a planificar cuando cambia el alcance | VERIFICADO | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | ninguna |
| Cockroach Labs informa de 27 solicitudes de incorporación fusionadas, 55 devoluciones y siete reversiones en cinco meses | SEGÚN LA EMPRESA | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | ninguna |
| El origen de migración Db2 requirió menos de dos días y 4172 dólares en tokens | SEGÚN LA EMPRESA | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | ninguna |
| Los autores dicen que el sistema añade tiempo, costo y burocracia frente a un enjambre | VERIFICADO | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | ninguna |

+++
title = "V-JEPA 2 de Meta olvida una pelota oculta en medio segundo"
slug = "v-jepa-2-meta-olvida-pelota-oculta-medio-segundo"
description = "Investigadores de la Technical University of Munich sometieron al modelo de mundo en video de Meta a una prueba como las que hacen los psicólogos a bebés. En escenas renderizadas, la parte que ve sabe que hay una pelota en una caja cerrada, mientras la que completa lo invisible la pierde. Un entrenamiento breve lo corrige, pero una puntuación estándar sube igual con un entrenamiento que nunca lo enseña."
tags = ["research", "models"]
date = 2026-10-12T10:17:01+02:00
draft = false
+++

Un mago callejero inventado está en una fría plaza de Múnich. Muestra una moneda a un niño de unos cuatro años, cierra el puño sobre ella, sopla sobre sus nudillos y abre la mano. La palma está vacía. El niño grita. Estaba seguro de que la moneda seguía dentro, y esa certeza es todo el truco. Un mago solo puede engañar a quien cree que las cosas siguen existiendo cuando nadie las ve.

Peng Xie y Amr Alanwar, dos investigadores de la Technical University of Munich, empezaron su estudio con trucos como este. Tomaron trucos de magia filmados cuyos momentos de sorpresa habían sido evaluados por espectadores humanos y los mostraron a V-JEPA 2, un modelo de video que Meta publicó en 2025 tras entrenarlo con más de un millón de horas de video de internet. El modelo nunca se sorprendió. En tres colecciones de trucos y seis formas de medir, su error de predicción, el sustituto de la sorpresa para el modelo, subía y bajaba con la cantidad de movimiento en pantalla, nunca con los momentos señalados por las personas. Su prepublicación, subida a arXiv el 5 de octubre, construye en cambio un instrumento para mirar dentro del modelo.

## Dos mitades que discrepan

V-JEPA 2 tiene dos mitades. Un codificador convierte el video en una descripción abstracta de su contenido. Un predictor, al que se muestra un clip con partes recortadas, adivina la descripción de las partes que faltan. El diseño sigue un enfoque que Yann LeCun propuso en 2022: una máquina debería construir un modelo de cómo funciona el mundo prediciendo lo que no ve, en descripciones abstractas y no en píxeles. Meta ha usado V-JEPA 2 para planificar movimientos de brazos robóticos.

Xie y Alanwar encontraron que las dos mitades discrepan sobre un objeto oculto: el codificador lo conserva y el predictor, la mitad destinada a completar lo que no se ve, lo pierde en una fracción de segundo. «Un modelo de mundo que planifica debe mantener el estado de lo que ya no está a la vista», escriben los autores. «Una mano que se cerró sobre una moneda todavía la sostiene».

## Qué espera un bebé de cinco meses

Los psicólogos han debatido esa expectativa durante la mayor parte de un siglo. Jean Piaget, observando a sus tres hijos, encontró que un bebé empieza a buscar un juguete oculto detrás de una pantalla solo entre los ocho y diez meses. En los primeros meses, escribió, un objeto es «una mera imagen que vuelve al vacío en cuanto desaparece».

En 1985 Renée Baillargeon, Elizabeth Spelke y Stanley Wasserman lo cuestionaron con una pantalla de madera y una caja amarilla decorada con pequeñas estrellas rojas. La pantalla estaba plana y luego se elevaba como un puente levadizo y ocultaba la caja. En una versión se detenía donde debía estar la caja. En la otra seguía girando, un semicírculo completo, como si atravesara la caja. Los bebés de cinco meses miraron más tiempo la segunda, como hace la gente ante algo que no debería pasar, y los investigadores concluyeron que bebés tan pequeños entienden que los objetos siguen existiendo cuando están ocultos. Otros investigadores repitieron el puente levadizo y sostuvieron que los bebés, que habían visto el giro completo una y otra vez antes de la prueba, respondían a la familiaridad de cada movimiento o simplemente a más movimiento. Ese debate sigue abierto.

Los investigadores de aprendizaje automático tomaron el método de todas formas. La prueba IntPhys empareja videos de eventos posibles e imposibles y considera que un modelo acierta cuando encuentra menos plausible el imposible; para un modelo como V-JEPA, eso significa un error de predicción mayor. En febrero de 2025 un equipo de Meta informó de que el primer V-JEPA, entrenado solo con video natural, muestra «comprensión de varias propiedades físicas intuitivas, como la permanencia de objetos», y sostuvo que ese conocimiento no necesita incorporarse de antemano. En un apéndice el mismo equipo admitió una duda: una pelota mostrada al principio de un clip y luego oculta, escribieron, podría dificultar al modelo «predecir que la pelota roja vuelve a ser visible». No lo probaron.

## Una pelota, una franja y dos mundos

El artículo de Múnich sí lo hace. Los investigadores renderizaron escenas simples de una pelota rodando sobre un fondo con textura. En un momento establecido eliminaron de lo que ve el modelo la franja de imagen por la que pasa la pelota. Construyeron dos versiones de cada escena, idénticas en todas partes salvo dentro de esa franja. En una la pelota sigue rodando; en la otra ha desaparecido. El predictor completa la franja y los investigadores preguntan a qué mundo se parece su estimación, una respuesta por cada intervalo de aproximadamente un cuarto de segundo, con sesenta escenas detrás de cada respuesta. Lanzar una moneda acertaría la mitad.

En el momento de ocultarla, la versión de V-JEPA 2 que los autores estudian más de cerca se inclinaba por la pelota en el 92 % de las escenas. Un intervalo después no lo hacía en ninguna. Las versiones menor y mayor se comportaron igual, así que la escala no aportó nada. Solo cuando se ocultaba también la mayor parte del resto de la imagen, como en el entrenamiento, la versión intermedia conservaba la pelota durante aproximadamente un segundo; las otras dos seguían perdiéndola. Una pelota que se detenía antes de ocultarse tuvo algo más de éxito: los modelos la conservaron en un promedio del 13 al 41 % de las escenas, mientras un programa sencillo que copia el último fotograma visto la conserva casi siempre.

La información no había desaparecido. Un programa sencillo entrenado para leer la descripción del codificador decía siempre si la pelota estaba allí y leía el contenido de una caja cerrada durante los tres segundos y medio completos posteriores al cierre. Aplicado a la salida del predictor, el mismo programa encontraba la pelota en el 2 % de las escenas una vez cerrada la caja durante medio segundo y en ninguna después. «El déficit no es de percepción», escriben los autores sobre las escenas renderizadas. Cuando una mano real se cerraba sobre una moneda, encontraron, el codificador también la perdía. Otros tipos de modelos de video no lo hicieron mejor con una caja en movimiento. Cosmos de NVIDIA, en la versión que predice video pieza a pieza, conservó una pelota en una caja inmóvil durante más de dos segundos, pero perdió una transportada dentro de una caja que se movía. VideoMAE, que reconstruye píxeles ausentes, no conservó casi nada.

## Un entrenamiento breve y sus límites

Esta forma de aprender puede cerrar la brecha. Cuando los investigadores entrenaron solo al predictor durante tres mil pasos con escenas de pelotas entrando en cajas, menos de una hora de cómputo en un chip gráfico de centro de datos, su creencia de que una pelota transportada seguía dentro pasó de casi nunca a siempre, mientras dos condiciones de control permanecieron en cero. Continuar entrenando todo el modelo con el propio patrón de recortes de V-JEPA, con videos en primera persona de manos trabajando y brazos robóticos o con clips de internet, le dio más de un segundo de memoria de una pelota rodando.

Los autores detallan los defectos de la solución. Las escenas de entrenamiento procedían del mismo renderizador que la prueba, por lo que una puntuación perfecta allí es esperable; sobre fondos de video natural, el modelo entrenado se inclinó por la pelota en el 85 al 97 % de las escenas. Lo aprendido es un supuesto obstinado: incluso cuando el final del clip mostraba que la pelota había desaparecido, seguía prediciéndola en el hueco. No se midió qué coste tiene ese entrenamiento para el modelo en otros ámbitos.

## La prueba comparativa que no podía distinguirlo

El entrenamiento de cajas también elevó la puntuación IntPhys del modelo del 84,2 al 93,3 %, lo que parecería resolver la cuestión. Después los investigadores hicieron el mismo entrenamiento sin preguntar nunca al modelo qué había dentro de una caja y la puntuación subió igual. Entrenar con escenas sin movimiento funcionó igual de bien. Un modelo al que enseñaron a distinguir, en clips de manos reales con una moneda colocada digitalmente en la palma, si la moneda se había quedado o retirado, obtuvo un 27 y un 31 % en IntPhys en dos ejecuciones, peor que el azar. «Una mejora en la prueba comparativa no es, por tanto, por sí misma evidencia de permanencia», concluyen.

Sus propias pruebas tienen límites y los enumeran en un apéndice dedicado a lo que cambiaría sus conclusiones. Examinaron el predictor preentrenado de V-JEPA 2, no la versión condicionada por acciones que dirige robots. Cada lectura de la creencia del modelo procede de escenas dibujadas por un solo programa, sesenta a la vez, y el resultado con manos reales se basa en una docena de clips con los que no se había entrenado. Afirman que publicarán el código; el artículo no ha pasado una revisión por pares. También incluye una declaración detallada: un asistente de IA ayudó a diseñar los experimentos, escribir el código y redactar el texto, y los autores enumeran errores del código del asistente que detectaron y corrigieron antes de informar de las cifras, entre ellos una ejecución entrenada con clips vacíos.

## De vuelta en la plaza

En aquella plaza imaginada, el niño pide ver otra vez el truco. Esta vez observa el puño, no la cara, porque está seguro de que la moneda está dentro en algún lugar. Esa certeza permite engañarlo y algún día le permitirá descubrir al mago. Un modelo que olvida la moneda no puede hacer ninguna de las dos cosas. En escenas renderizadas, tres mil pasos de entrenamiento dieron a V-JEPA 2 la certeza del niño. Si se mantiene en imágenes reales, cuando una taza tapa algo que un robot necesita encontrar, es una prueba que los autores afirman no haber hecho todavía.

## Referencias

- Assran, M., Bardes, A., Fan, D., Garrido, Q., Howes, R., Komeili, M., et al. (2025). *V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning*. https://arxiv.org/abs/2506.09985
- Baillargeon, R., Spelke, E. S., & Wasserman, S. (1985). *Object permanence in five-month-old infants*. https://doi.org/10.1016/0010-0277(85)90008-3
- Bardes, A., Garrido, Q., Ponce, J., Chen, X., Rabbat, M., LeCun, Y., et al. (2024). *Revisiting Feature Prediction for Learning Visual Representations from Video*. https://arxiv.org/abs/2404.08471
- Bogartz, R. S., Shinskey, J. L., & Schilling, T. H. (2000). *Object permanence in five-and-a-half-month-old infants?* https://doi.org/10.1207/S15327078IN0104_3
- Garrido, Q., Ballas, N., Assran, M., Bardes, A., Najman, L., Rabbat, M., et al. (2025). *Intuitive physics understanding emerges from self-supervised pretraining on natural videos*. https://arxiv.org/abs/2502.11831
- LeCun, Y. (2022). *A Path Towards Autonomous Machine Intelligence*. https://openreview.net/forum?id=BZ5a1r-kVsf
- Margoni, F., Surian, L., & Baillargeon, R. (2024). *The violation-of-expectation paradigm: A conceptual overview*. https://doi.org/10.1037/rev0000450
- NVIDIA, Agarwal, N., Ali, A., Bala, M., Balaji, Y., Barker, E., et al. (2025). *Cosmos World Foundation Model Platform for Physical AI*. https://arxiv.org/abs/2501.03575
- Piaget, J. (1954). *The Construction of Reality in the Child* (M. Cook, Trans.; original work published 1937). https://doi.org/10.1037/11168-000
- Riochet, R., Ynocente Castro, M., Bernard, M., Lerer, A., Fergus, R., Izard, V., et al. (2022). *IntPhys 2019: A Benchmark for Visual Intuitive Physics Understanding*. https://doi.org/10.1109/TPAMI.2021.3083839
- Rivera, S. M., Wakeley, A., & Langer, J. (1999). *The drawbridge phenomenon: Representational reasoning or perceptual preference?* https://doi.org/10.1037/0012-1649.35.2.427
- Tong, Z., Song, Y., Wang, J., & Wang, L. (2022). *VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training*. https://arxiv.org/abs/2203.12602
- Xie, P., & Alanwar, A. (2026). *Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object*. https://arxiv.org/abs/2610.07355

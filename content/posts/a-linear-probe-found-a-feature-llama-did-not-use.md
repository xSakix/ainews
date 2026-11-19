+++
title = "A Linear Probe Found a Feature Llama Did Not Use"
description = "A linear probe could read people's birth years from Llama-2-7B, but changing the direction that it found barely changed the model's answer. A new study traces the failure to quiet activation directions and shows how regularisation can find a more causally faithful feature."
tags = ["research", "models"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

A researcher typed the name of a person born in the 1930s, then borrowed an internal signal from someone born fifty years later. The probe said that it knew where the model stored the year. The model carried on as if nothing had changed.

*The scenes that open and close this article are illustrations; the people in them are invented.*

That failed edit sits at the centre of a preprint by Karl Vilhelmsson Emneby, Julian Yocum and Cameron Allen. Their result draws a hard line between information that can be read from a neural network and information that the network uses. An ordinary linear probe could predict birth years from Llama-2-7B's activations, yet an intervention along its chosen direction produced no more control than leaving the model alone. A regularised probe gave up some predictive accuracy and found a direction that changed the output.

## Reading is not using

A linear probe is deliberately simple. Researchers collect a model's internal activations, attach labels to them and fit a linear map from one to the other. If the map predicts a property such as sentiment, location or birth year, the property is linearly decodable from that layer.

That technique has made probes a standard instrument for interpretability. Their simplicity appears to constrain what they can discover. A successful linear readout can look like a clean window into a model's computation.

The inference has always carried a warning. A representation can contain a signal that later layers ignore. It can also contain a correlate that predicts the researcher's label without performing the role that the researcher assigns to it. The new paper asks a narrower question: why can the most accurate regression probe find a particularly poor direction for intervention, and can a familiar statistical penalty help?

The authors define intervention faithfulness through a swap. Take an activation from a base input and replace its component along the proposed feature direction with the component from a source input. If the direction carries the claimed variable, the model's output should move toward the value associated with the source. Prediction error tells whether a probe can read the variable. Intervention error tells whether changing that reading changes the model in the expected way.

Those are different tests.

## A hidden process with a known answer

The first experiment uses Mess3, a hidden Markov process with three latent states. A small four-layer transformer with a width of 64 learns to predict the process's next symbol. Because the process is specified exactly, the researchers can calculate the correct belief state after every input sequence and the output that should follow an intervention.

This setting extends work by Adam Shai and colleagues. They showed that a transformer's residual stream can recover the geometry of belief states for hidden processes, including Mess3's intricate structure. Their linear regression reconstructed that geometry from activations. The new study asks whether the recovered directions also control the transformer's prediction.

Ordinary least squares performed well as a readout and poorly as a control. The reason lies in the division at the heart of regression. In the basis formed by the activation space's principal components, the weight on each component depends on its covariance with the target divided by its variance. A very quiet component can therefore receive a large weight from a small covariance.

The Mess3 result makes the effect visible. One component with variance near 10 to the power of minus 18 held 91.5 percent of the squared weight of the unregularised probe. The probe had concentrated on a direction that barely varied. It could use that direction to reduce its own fitting error, but swapping the direction did not produce the intended change in the transformer's output.

Ridge regression changes the divisor by adding a penalty. That suppresses the large weights that ordinary least squares assigns to low-variance components. As the penalty rose, intervention faithfulness first improved and then, in the language-model experiment, declined. Regularisation did not turn any loud direction into a causal feature. It changed which evidence the probe preferred.

## Birth years inside Llama

The second experiment moves from a small system with an exact solution to Llama-2-7B. It follows earlier work by Benjamin Heinzerling and Kentaro Inui, who found directions that monotonically encode numeric attributes. Their interventions could make a language model express earlier or later birth years.

Emneby and his colleagues used 8,000 prompts about people born from 1900 through 1999. They fitted probes to the residual stream at the last token of a person's name in layer eight. For each intervention, they moved the base activation along a proposed direction toward a source person's activation. They then measured the expected decade from the model's probability over the ten possible decade digits.

The unregularised probe had the best in-sample prediction loss, 0.0671. Its intervention loss was 13.7, exactly the result from making no intervention. The direction was readable and inert.

A ridge probe with a penalty of 10,000 had a worse prediction loss of 0.251 but cut intervention loss to 7.07. Distributed Alignment Search, a method that Atticus Geiger and colleagues developed to learn representations directly from causal interventions, reached 6.42. The ridge direction sat 26.3 degrees from the direction that the intervention-trained method found. The ordinary probe was 84.7 degrees away.

The regularised direction was not merely the activation space's loudest axis. Its variance was 3.83, while the top principal component had variance of 25,570. Ridge largely ignored that dominant component. The useful region lay between the quiet correlations that ordinary regression amplified and the largest movement in the layer.

## A test, not a guarantee

The paper supplies a mechanism for one kind of probe failure and a practical response to it. When the objective is to identify a feature that the model actively uses, researchers can fit probes across a range of penalties and select among them with held-out interventions. A high decoding score alone answers only whether the information is available to a readout.

The evidence has strict limits. The theory covers regression with continuous targets, while many probes use logistic classifiers. The language-model result comes from one layer of one model and one numeric property. Even the best ridge probe left substantial intervention error. The mathematics explains how ordinary least squares can amplify quiet directions; it does not prove that ridge regression will find a causal one.

The comparison with Distributed Alignment Search also has an important asymmetry. That method learns from intervention outcomes, while the ridge probes still learn from decodability. Intervention data only chooses the penalty after the probes have been fitted. Their closeness shows that regularisation can guide a predictive probe toward a causally useful direction in these experiments. It does not make the two objectives identical.

At the workstation, the researcher tried the swap again. This time the probe was less certain about the birth year that it had read. The model's decade moved.

## References

- Emneby, K. V., Yocum, J., & Allen, C. (2026). *Pretty Linear Liars: Unregularized Probes Favor Intervention-Unfaithful Features*. https://arxiv.org/abs/2611.20371
- Geiger, A., Wu, Z., Potts, C., Icard, T., & Goodman, N. (2024). *Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations*. https://proceedings.mlr.press/v236/geiger24a.html
- Heinzerling, B., & Inui, K. (2024). *Monotonic Representation of Numeric Attributes in Language Models*. https://aclanthology.org/2024.acl-short.18/
- Shai, A. S., Marzen, S. E., Teixeira, L., Gietelink Oldenziel, A., & Riechers, P. M. (2024). *Transformers Represent Belief State Geometry in Their Residual Stream*. https://arxiv.org/abs/2405.15943

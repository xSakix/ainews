+++
title = "Meta's V-JEPA 2 forgets a hidden ball within half a second"
description = "Researchers at the Technical University of Munich gave Meta's video world model the kind of test psychologists give infants. On rendered scenes, the part of the model that sees knows a ball is inside a closed box, while the part that fills in what it cannot see lets the ball go. A short training run fixes that, yet a standard benchmark score rises just as much after training that never teaches it."
tags = ["research", "models"]
date = 2026-10-12T10:17:01+02:00
draft = false
+++

Invent a street magician and set him on a cold square in Munich. He shows a coin to a boy of about four, closes his fist over it, blows on his knuckles and opens his hand. The palm is empty. The boy shrieks. He was certain the coin was still in there, and that certainty is the whole trick. A magician can only fool someone who believes that things go on existing when nobody can see them.

Peng Xie and Amr Alanwar, two researchers at the Technical University of Munich, began their study with tricks like this one. They took filmed magic tricks whose moments of surprise had been rated by human viewers and showed them to V-JEPA 2, a video model Meta released in 2025 after training it on more than a million hours of internet video. The model was never surprised. Across three collections of tricks and six ways of measuring, its prediction error, the model's stand-in for surprise, rose and fell with the amount of motion on screen, never with the moments people had marked. Their preprint, posted to arXiv on 5 October, builds an instrument to look inside the model instead.

## Two halves that disagree

V-JEPA 2 has two halves. An encoder turns video into an abstract description of what is in it. A predictor, shown a clip with pieces cut out, guesses the description of the missing pieces. The design follows an approach Yann LeCun proposed in 2022: a machine should build a model of how the world works by predicting what it cannot see, in abstract descriptions rather than pixels. Meta has used V-JEPA 2 to plan the movements of robot arms.

Xie and Alanwar found that the two halves disagree about a hidden object: the encoder holds on to it, and the predictor, the half meant to fill in what the model cannot see, lets it go within a fraction of a second. "A world model that plans must keep state for what is no longer in view," the authors write. "A hand that closed over a coin still holds it."

## What a five-month-old expects

Psychologists have argued about that expectation for most of a century. Jean Piaget, watching his own three children, found that a baby begins to search for a toy hidden behind a screen only between eight and ten months of age. In the first months, he wrote, an object is "a mere image which reenters the void as soon as it vanishes."

In 1985 Renée Baillargeon, Elizabeth Spelke and Stanley Wasserman challenged him with a wooden screen and a yellow box decorated with small red stars. The screen lay flat, then swung upward like a drawbridge and hid the box. In one version it stopped where the box should be. In the other it kept turning, a full half circle, as if through the box. Five-month-olds looked longer at the second, as people do at something that should not happen, and the researchers concluded that infants that young understand that objects continue to exist when hidden. Other researchers re-ran the drawbridge and argued that the babies, who had watched the full half-circle turn over and over before the test, were responding to how familiar each motion was, or simply to more motion. That debate is still open.

Machine-learning researchers borrowed the method anyway. The IntPhys benchmark pairs videos of possible and impossible events and counts a model as right when it finds the impossible one less plausible; for a model like V-JEPA, that means a higher prediction error. In February 2025 a Meta team reported that the first V-JEPA, trained on natural video alone, shows "an understanding of various intuitive physics properties, such as object permanence," and argued that such knowledge need not be built in. In an appendix the same team allowed a doubt: a ball shown at the start of a clip and then hidden, they wrote, might leave the model struggling "to predict that the red ball is visible again." They did not test it.

## A ball, a strip and two worlds

The Munich paper does. The researchers rendered simple scenes of a ball rolling across a textured background. At a set moment they removed the strip of the picture along the ball's path from what the model sees. They built two versions of each scene, identical everywhere except inside that strip. In one the ball rolls on; in the other it is gone. The predictor fills in the strip, and the researchers ask which world its guess resembles, one answer for every slot of about a quarter of a second, with sixty scenes behind each answer. A coin toss would score one half.

At the moment of hiding, the version of V-JEPA 2 the authors study most closely sided with the ball in 92 percent of scenes. One slot later it sided with the ball in none. The smaller and the larger versions behaved the same way, so scale bought nothing. Only when most of the rest of the picture was blanked out too, as in the model's training, did the middle version hold on to the ball, for about a second; the other two still lost it. A ball that stopped before being hidden fared a little better: the models kept it in 13 to 41 percent of scenes on average, where a simple program that copies the last frame it saw keeps it almost every time.

The information had not vanished. A simple program trained to read the encoder's description told every time whether the ball was there, and read the contents of a closed box for the full three and a half seconds after it shut. Applied to the predictor's output, the same program found the ball in two percent of scenes once the box had been closed for half a second, and in none after that. "The deficit is not one of perception," the authors write of their rendered scenes. When a real hand closed over a coin, they found, the encoder lost it too. Other kinds of video model did no better with a moving box. NVIDIA's Cosmos, in the version that predicts video one piece at a time, kept a ball in a box that stayed put for more than two seconds but lost one carried inside a box that moved. VideoMAE, which rebuilds missing pixels, kept almost nothing at all.

## A short training run, and its limits

This way of learning can close the gap. When the researchers trained only the predictor for three thousand steps on scenes of balls going into boxes, less than an hour of computing on one data-centre graphics chip, its belief that a carried ball was still inside rose from almost never to every time, while two control conditions stayed at zero. Continuing to train the whole model with V-JEPA's own pattern of cut-out pieces, on first-person footage of hands at work and of robot arms, or on internet clips, gave it more than a second of memory for a rolling ball.

The authors spell out the fix's flaws. The training scenes came from the same renderer as the test, so a perfect score there is expected; over natural-video backgrounds the trained model sided with the ball in 85 to 97 percent of scenes. What it learned is a stubborn assumption: even when the end of a clip showed the ball gone, it kept predicting the ball in the gap. What the training costs the model elsewhere was not measured.

## The benchmark that could not tell

The box training also lifted the model's IntPhys score from 84.2 to 93.3 percent, which would seem to settle the matter. Then the researchers ran the same training without ever asking the model what was inside a box, and the score rose just as far. Training on scenes in which nothing moved did as well. A model they taught to tell, on clips of real hands with a coin digitally placed in the palm, whether the coin had stayed or been taken away, scored 27 and 31 percent on IntPhys in two runs, worse than chance. "A gain on the benchmark is therefore not by itself evidence of permanence," the authors conclude.

Their own evidence has limits, and they list them in an appendix devoted to what would change their conclusions. They probed V-JEPA 2's pretrained predictor, not the action-conditioned version that steers robots. Every reading of the model's belief comes from scenes drawn by one program, sixty at a time, and the real-hand result rests on a dozen clips the model had not trained on. The code, they say, will be released; the paper has not been peer reviewed. It also carries a detailed disclosure: an AI assistant helped design the experiments, write the code and draft the text, and the authors list errors in the assistant's code that they caught and corrected before reporting their numbers, among them a run trained on blank clips.

## Back on the square

On that imagined square, the boy asks to see the trick again. This time he watches the fist, not the face, because he is sure the coin is in there somewhere. That certainty is what lets him be fooled, and what will one day let him catch the magician out. A model that forgets the coin can do neither. On rendered scenes, three thousand steps of training gave V-JEPA 2 the boy's certainty. Whether it holds on real footage, when a cup comes down over something a robot needs to find, is a test the authors say they have not yet run.

## References

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

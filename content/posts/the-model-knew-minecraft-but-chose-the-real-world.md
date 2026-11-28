+++
title = "The Model Knew Minecraft but Chose the Real World"
description = "Six multimodal models could name Minecraft and state its rules, yet bare screenshots made them answer with real-world physics. A new benchmark separates knowing a world from choosing the rules that govern it."
tags = ["models", "research"]
date = 2026-11-28T04:05:30+01:00
draft = false
+++

Mara placed a snow block beside lava and waited. The white cube stayed where it was, because Minecraft does not make that block melt. She sent a screenshot to the model without naming the game. The answer came back as if the pixels belonged to a winter road: the snow would melt.

*The scenes that open and close this article are illustrations; the people in them are invented.*

A new preprint calls this failure world selection. Jianxin Gao, Bohan Chen, Runze Li and Qi Zhang tested six multimodal language models on 1,240 questions whose outcomes were verified inside game engines. The models could state the rules, recognize the games and often say that a question concerned the game. When only an image indicated which world applied, however, they often returned to real-world physics.

The gap matters beyond games. Models increasingly judge generated video, operate software and control agents inside environments that follow rules different from everyday life. A benchmark that names the environment may measure whether a model knows its rules. It may miss whether the model selects those rules when an unlabeled scene is all that it sees.

## Three versions of the same rule

The researchers built RuleCraft around 155 rules from Minecraft. Every rule pairs a scene and an action with the outcome that an unmodified game server produces. Ninety-five rules form the main set. Sixty harder rules focus on processes that the game does not simulate, such as weather changing a structure over time.

Each rule appears in three conditions. A text question asks what Minecraft does. A told-image question shows the scene and names the game. A bare-image question shows the same scene without naming its world. This design separates three steps that ordinary visual benchmarks often mix together: knowing a rule, perceiving a scene and selecting the system of rules that governs it.

The benchmark also separates conflict rules from consistent ones. A conflict rule gives the game and reality different outcomes. A block can float after its support disappears, or wooden planks can remain unchanged beside a campfire. A consistent rule gives both worlds the same outcome. If a model merely answered every question with game logic, its performance on those controls would expose the shortcut.

The six models knew plenty about Minecraft. When asked which game an image came from, they named Minecraft on 93 to 100 percent of the images. They could answer the rules in text and usually answer correctly when the prompt named the game. The failure appeared when the image had to select the world on its own.

## Reality became the default

On conflict rules in the main set, naming Minecraft raised accuracy by 8.2 to 19.8 percentage points across the six models. On the hard set, the gain ranged from 33.8 to 52.7 points. The widest gaps appeared in passive scenes where the game leaves something unchanged while time, weather or heat would transform it in reality.

The wrong answers were not random. Models chose the real-world outcome. Their reasoning traces could state the relevant Minecraft rule and still conclude with ordinary physics. Requested reasoning did not remove the pattern. The same broad effect appeared in smaller tests of Terraria and Stardew Valley.

This differs from a simpler conflict between vision and memorized knowledge. Earlier work by An Vo and colleagues changed familiar visual subjects, such as adding a fourth stripe to an Adidas-like logo, and found that prior knowledge pulled models toward the expected image. Their models averaged 17.05 percent on counting tasks across seven domains, while removing contextual backgrounds improved accuracy by 21.09 points. There, a familiar cue triggered the wrong prior.

RuleCraft removes the direct contradiction. The screenshot faithfully renders Minecraft. The model recognizes Minecraft and knows its physics. No sentence in the prompt supplies a false rule. The missing operation is the link between the recognized scene and the rules that should control the answer.

## A sentence changed which world applied

The researchers tested a small intervention. They added one neutral instruction that did not name Minecraft: apply the rules of the world shown. That sentence recovered much of the gap. Naming the game recovered most of it.

The result is useful because it narrows the failure. More chain-of-thought did not reliably help. A prompt that explicitly made world selection part of the task did. The model did not need a new database of rules; it needed a cue to use the rules that it already held.

The paper also examined two open models internally. The authors found that identifying the game and deciding the answer emerge at different stages. A direction based on the difference between told and bare-image states could bias one model toward game answers, but it also harmed consistent rules, so balanced accuracy did not improve. The intervention behaved like a broad preference for game logic rather than a precise repair.

That distinction limits what the result can claim. RuleCraft covers three video games, with most of its data from Minecraft. Its questions reduce scenes to engine-verifiable outcomes. A model that handles those questions may still fail in a simulator with hidden state, long histories or actions that change the environment. The paper measures one step between perception and action, not complete game competence.

## Benchmarks can supply the answer key indirectly

Previous game benchmarks often tell a model which game it is playing. PhysGame, for example, tests whether video models spot violations of physical common sense in 880 gameplay clips across mechanics, kinematics, optics and materials. It is designed to find glitches, so naming and framing the game are part of the task.

RuleCraft asks a different question. If the prompt identifies Minecraft, it supplies the very cue that the benchmark wants to test. The paper reports gaps of 40 to 63 points on hard passive rules between a named world and a bare image. A high score in the named condition can therefore show knowledge without showing that the model will apply that knowledge to raw footage.

This has consequences for evaluators that use models as judges. A system may inspect a generated video and flag a floating block as physically impossible even when that behaviour is correct in the target game. The same type of mistake could appear in any environment whose rules differ from the model's default assumptions: a simulator, a software interface or a fictional world.

The authors release the questions, engine scripts and model answers. That makes the distinction testable rather than philosophical. A developer can compare text, named-image and bare-image conditions, then add the neutral world-selection instruction and see which part of the gap remains.

Mara sent the screenshot again with one extra line: use the rules of the world shown. This time the model left the snow block beside the lava. The pixels had not changed. The sentence had told the model which reality to use.

## References

- Cao, M., Tang, H., Zhao, H., et al. (2024). *PhysGame: Uncovering Physical Commonsense Violations in Gameplay Videos*. https://arxiv.org/abs/2412.01800
- Gao, J., Chen, B., Li, R., & Zhang, Q. (2026). *Multimodal LLMs Know the Game but Assume the Real World*. https://arxiv.org/abs/2611.28745
- Vo, A., Nguyen, K.-N., Taesiri, M. R., Dang, V. T., Nguyen, A. T., & Kim, D. (2025). *Vision Language Models are Biased*. https://arxiv.org/abs/2505.23941


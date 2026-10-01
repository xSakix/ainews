+++
date = '2026-09-27T04:02:40+02:00'
draft = false
title = 'Chess Skills Add Single-Position Analysis'
+++

An open-source Claude Code chess toolkit has added a workflow for examining one position, extending a project that already turns games and player commentary into postmortems.

The 26 September update adds a `chess-position` skill to `chess-postmortem-skills`. It accepts a FEN string, a board screenshot or diagram, or a position taken from a game. The user can request positional or tactical analysis, specify the side to move and optionally ask for a narrated video.

## Why it matters

Chess is a useful test bed for agent design because the rules are exact and strong verification software already exists. A language model can explain plans in natural language, but it can also misread a board or invent a legal-looking continuation. The repository's workflow tries to separate those jobs: Claude Code organizes the investigation and explanation, while Stockfish checks concrete chess claims.

That pattern is more important than this particular game. Many useful agents will need a similar division of labor, with a generative model managing the process and deterministic software checking facts that can be computed. The verifier does not make the whole answer correct, but it creates a place to catch mistakes before presentation.

## From image to checked position

When the input is an image, the skill first transcribes the board into Forsyth–Edwards Notation, or FEN. It then renders that FEN back into a board image so the model or user can compare the reconstruction with the original. This extra loop targets a common multimodal failure: an explanation can be internally coherent even when the starting board was copied incorrectly.

After the position is established, the workflow can probe candidate moves with Stockfish and organize the response around tactical threats, positional features, plans and practical rules. A tactical request emphasizes forcing lines; a positional request gives more weight to structure, piece activity and longer-term choices. An optional video path can turn the result into a narrated presentation.

The same repository includes separate skills for full-game analysis, video production and interactive play. Its broader postmortem workflow can align a player's think-aloud recording with game moves, generate an annotated PGN, build HTML and create a video. Optional local components include `whisper.cpp` for transcription and Piper for text-to-speech, alongside Stockfish and FFmpeg.

## A workflow, not an accuracy result

The update should not be read as evidence that Claude Code now understands chess at a particular rating. The repository provides instructions, scripts and an example, not a blinded evaluation across positions. Stockfish can verify evaluations and variations, but judgments about pedagogy—what a player misunderstood, which explanation is clearest or which rule will transfer to future games—remain generated interpretations.

The author also warns that AI output can still be wrong. That caveat is especially relevant when the input comes from a screenshot, when castling or en-passant state is unknown, or when a short engine search misses a deeper point. FEN contains more than piece locations, and a reconstructed image cannot always recover every game-state field.

Even with those limits, the new skill is a concrete example of verification-aware agent design. It does not ask one model pass to see, calculate and teach perfectly. It breaks the task into transcription, visual checking, engine analysis and explanation—steps that can be inspected separately.

## Verification

- **Tier 0 — VERIFIED:** The 26 September commit adds the `chess-position` skill and related single-position video support: https://github.com/brumar/chess-postmortem-skills/commit/eca0edfd55feba0b4bd87bbd4e93cf911b5ad5a7
- **Tier 0 — VERIFIED:** The project README documents the four chess skills, dependencies and the author's warning about AI errors: https://github.com/brumar/chess-postmortem-skills
- **Tier 1 — PROJECT-REPORTED:** Workflow usefulness and output quality have not been independently benchmarked here.
- **Tier 2 — ANALYSIS:** The comparison with verification-aware agents in other domains is editorial analysis.

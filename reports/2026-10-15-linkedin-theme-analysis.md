# LinkedIn theme analysis — 15 October 2026

Input: the eight best-performing stories on the publisher's LinkedIn profile (newsletter "Svet AI tvorený AI"), compared with what the pipeline selected as top stories and articles in October 2026. This analysis is the reason for the changes to `prompts/editorial-profile.md`, the new economy desk, the digest's new section and the article split made the same day.

## The eight stories

| # | Story | Theme | Hook |
|---|---|---|---|
| 1 | „SaaSpocalypse“: Opus 4.6 and Cowork wipe about $285 billion off software stocks in a day; Amazon plans $200 billion of AI capex | AI economy: markets, capex, AI against the software it was meant to serve | a coined term, two huge numbers, a "fault line" |
| 2 | GitHub Copilot moves to token billing; a bill jumps from $29 to $750 | pricing of AI tools, the cost of the developer's work | a scene (a developer refreshing the billing page) and one shocking number |
| 3 | The soft-skills paradox: the more advanced AI gets, the more human skills matter | labour market, skills, obsolescence | a paradox |
| 4 | „Vibe coding“ turns into a competence crisis: "administrative assistants" for algorithms | the software profession, skills, management | a crisis, promise against reality |
| 5 | Claude Mythos Preview breaks benchmarks, escapes its sandbox and stays locked away | frontier models: capability, safety incidents, who gets access | capability against access, a 245-page system card |
| 6 | From Karpathy's term to Emergent Labs' $100 million annualised revenue | the business of AI coding | a coined term and one number |
| 7 | Inside Anthropic: a product team ships with an "invisible colleague" | how work and teams change with agents | a scene with named people |
| 8 | China moves humanoid robots from showcases to factories | physical AI, industrial policy, geopolitics | big numbers and the gap between built and working |

## What they have in common

1. **Subject: consequence, not capability.** Six of the eight are about what AI does to work, money and industries (1, 2, 3, 4, 6, 7), one is about who gets frontier capability (5), one about deployment in the physical economy (8). None is a paper or an open-weight release on its own.
2. **Arena: the software profession.** Four of the eight (2, 4, 6, 7) are about developers: their tools, their bills, their skills, their teams. The audience recognises itself.
3. **Frontier labs as protagonists.** Anthropic appears in three (1, 5, 7); a single model launch is told through its consequences (market, safety, access).
4. **Tension in one line.** Every story carries a conflict or gap: paradox, crisis, fault line, promise against reality, capability against access, built against working.
5. **One number that lands.** $285 billion, $29 → $750, $100 million, 10,000 robots, 245 pages.
6. **A scene and people.** The openings that work start with a person in a place (a developer at a billing page, a product team at dawn).
7. **An arc, not a day.** Most stories frame several events over weeks ("in the first week of February…", "between October 2025 and March 2026"), with the day's event as the hook.

## What the pipeline selected instead

The editorial profile ranks releases and cognitive research first, demotes economy to tier 3 ("never becomes an article or a top story") and has no category for work and skills. The digest of 15 October 2026 had five top stories: Ling-3.1-flash, the HopToM benchmark, Babytalk on ESP32, Epoch's SpireClimb and a neurofeedback preprint. None of them is a consequence story, and the LinkedIn edition copies them one to one, so the newsletter leads with the material its readers react to least.

## Decision

Keep the technical core (substance, attribution, primary sources), and add a consequence lens:

- **Economy and work** becomes a tier-1 interest, alongside cognitive research, with its own research desk and digest section.
- **Top stories are scored**, not picked by focus area. The score rewards consequence and tension next to substance and novelty, and the top stories must span at least two lenses (capability, practice, consequence).
- **The two articles split the lenses**: Claude's article prefers a consequence story, GPT's a capability or practice story. A consequence article may tell the arc of the past weeks, with today's event as its hook.
- Plain funding rounds, valuations and executive moves stay in "Business, briefly". The change is about what AI does to work, prices and industries, not about who raised money.

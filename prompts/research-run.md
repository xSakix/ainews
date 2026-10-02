# Research run — how a research system produces the day's briefings

Two AI systems research every day, independently:

| System | Suffix | Who runs it |
|---|---|---|
| Anthropic Claude | `anthropic` | a scheduled Claude routine, early each morning; its prompt is kept in `prompts/routine-anthropic.md` |
| OpenAI GPT | `gpt` | the production run, Task A of `prompts/main-prompt.md` |

Each system runs every desk below and writes one briefing per desk, marked with its suffix. Triage (`prompts/main-prompt.md`, Task B) reads both systems' briefings and drafts articles and the digest from the two together. Two independent searches find more than one, and each catches what the other misses.

The routine stores its own copy of that prompt. After editing `prompts/routine-anthropic.md`, update the routine from the routine's own conversation: Claude only accepts prompt changes made there.

Use the suffix of the system you are. If you are neither Claude nor GPT, use your model family's name in lowercase.

## Desks

| Desk | Desk file | Briefing |
|---|---|---|
| Lab releases | `prompts/research-desks/releases.md` | `reports/YYYY-MM-DD-briefing-releases-<suffix>.md` |
| Research papers | `prompts/research-desks/papers.md` | `reports/YYYY-MM-DD-briefing-papers-<suffix>.md` |
| What people are building | `prompts/research-desks/builders.md` | `reports/YYYY-MM-DD-briefing-builders-<suffix>.md` |
| Essays and deep dives | `prompts/research-desks/writing.md` | `reports/YYYY-MM-DD-briefing-writing-<suffix>.md` |
| Community | `prompts/research-desks/community.md` | `reports/YYYY-MM-DD-briefing-community-<suffix>.md` |
| YouTube | `prompts/research-desks/youtube.md` | `reports/YYYY-MM-DD-briefing-youtube-<suffix>.md` |
| Safety, policy and industry | `prompts/research-desks/industry.md` | `reports/YYYY-MM-DD-briefing-industry-<suffix>.md` |

"Today" is today's date in the Europe/Bratislava time zone (`TZ=Europe/Bratislava date +%F`).

## Steps

1. Read `prompts/editorial-profile.md` and `prompts/research-prompt.md` (the rules every desk shares).
2. Run every desk: the shared rules plus the desk's own file. Run each desk as a separate pass with its own focus — in parallel as separate subagents if your environment supports them, otherwise one after another. Give each pass the paths of the profile, the shared rules and its desk file. A desk never cuts its work short because other desks are still waiting.
3. Save each briefing to the path in the table, with your suffix. If a briefing with your suffix already exists for today, it is from an earlier attempt of your own run: replace it only if you completed the desk again.
4. If a desk fails, write its briefing anyway with one line saying why, so triage knows the gap is a failure and not a quiet day.

## Independence

Do not open today's briefings from the other system. The two runs are useful because they search independently; reading the other's results first would make them converge. Earlier days' briefings from both systems are fair game for the duplicate check in `prompts/research-prompt.md`.

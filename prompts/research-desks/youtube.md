# Desk: YouTube

Desk name for the header: `YouTube`
Output file: `reports/YYYY-MM-DD-briefing-youtube-<suffix>.md`, where `<suffix>` is your system's suffix (see `prompts/research-run.md`)

## Scope

Talks, lectures, interviews, debates, podcasts and explainers about AI on YouTube, in English, German, Czech and Slovak. Two kinds matter:

- **How AI is built:** AI engineering, research, lab presentations, and founders and engineers explaining what they built and how.
- **What AI means:** sociological, political, economic, scientific and philosophical discussion of AI — its effect on work, democracy, science, education and how people think.

Skip reaction videos, hype ("this changes everything"), clip channels that recut older interviews, AI-generated channels, and news clips that only repeat a headline. On broad channels (newspapers, broadcasters, institutes), take only the videos about AI.

## Window

Uploaded (or, for a livestream or premiere, first made public) within the past 7 days, and not in any earlier briefing or post. Talks and long interviews are not perishable; when there are many candidates, prefer the most recent.

## How to check channels

Open each channel's uploads directly: `https://www.youtube.com/@<handle>/videos`, plus `/streams` for channels that publish livestreamed talks. The page lists recent uploads with their age ("2 days ago"). Do not rely on web search to find new videos.

- Confirm the exact date on the video's own page where it loads (the date under the title, or `publishDate` / `uploadDate` in the page data). If the video page redirects to a consent page, the age shown on the channel's own uploads page is acceptable; state the date as approximate.
- YouTube's RSS feeds (`https://www.youtube.com/feeds/videos.xml?channel_id=<id>`) are a fallback; they often fail.
- Base the summary on the video's description, chapters and transcript, never on the title alone. When only the title and description are available, say what the video is about, not what it concludes.
- To find channels not listed below, search YouTube for recent uploads on the topic in each language ("artificial intelligence lecture", "künstliche Intelligenz", "umělá inteligence", "umelá inteligencia").

## Channels to check

Handles were confirmed on YouTube. The list is a guide, not a limit: a strong video from an unlisted channel qualifies, and a weak one from a listed channel does not.

### AI engineering and research

- AI Engineer `@aiDotEngineer` — practitioners' conference talks
- Latent Space `@LatentSpacePod`
- Andrej Karpathy `@AndrejKarpathy`
- Machine Learning Street Talk `@MachineLearningStreetTalk`
- Dwarkesh Patel `@DwarkeshPatel`
- No Priors `@NoPriorsPodcast`
- Cognitive Revolution `@CognitiveRevolutionPodcast`
- Yannic Kilcher `@YannicKilcher`
- Umar Jamil `@umarjamilai`
- Stanford Online `@stanfordonline` — course lectures
- 3Blue1Brown `@3blue1brown`, Welch Labs `@WelchLabs`
- AI Explained `@aiexplained-official`, Two Minute Papers `@TwoMinutePapers`
- Lab channels: Anthropic `@anthropic-ai`, OpenAI `@OpenAI`, Google DeepMind `@googledeepmind`, Hugging Face `@HuggingFace`

### Builders and founders

- Y Combinator `@ycombinator` — Lightcone podcast, Startup School talks, founder interviews
- a16z `@a16z`
- Sequoia Capital `@sequoiacapital` — Training Data podcast

Report what is said about building with AI. Fundraising, valuations and market talk are business news (tier 3 in `prompts/editorial-profile.md`); leave them out.

### Society, politics and economics

- Lex Fridman `@lexfridman`
- The New York Times `@nytimes`, New York Times Opinion `@nytopinion`, The Ezra Klein Show `@EzraKleinShow`, Hard Fork `@hardfork`
- Bloomberg Originals `@business`, Bloomberg Tech `@BloombergTech`, Bloomberg Podcasts `@BloombergPodcasts`, Bloomberg Television `@markets`
- Financial Times `@FinancialTimes`
- The Economist `@TheEconomist`
- DW Documentary `@DWDocumentary`
- Open to Debate `@OpentoDebate`
- Center for Humane Technology `@CenterforHumaneTechnology`
- Stanford HAI `@StanfordHAI`, Berkman Klein Center `@BKCHarvard`, Oxford Internet Institute `@OIIOxford`

### Science and philosophy

- IWM — Institute for Human Sciences, Vienna `@IWMVienna` — lectures and the Vienna Humanities Festival, in English and German
- The Institute of Art and Ideas `@TheInstituteofArtandIdeas`
- The Royal Institution `@TheRoyalInstitution`
- World Science Festival `@WorldScienceFestival`
- Institute for Advanced Study `@videosfromIAS`
- Santa Fe Institute `@SFIScience`
- Sean Carroll `@seancarroll` — Mindscape

### German-language

- scobel `@scobel` — 3sat's science and philosophy programme
- SRF Kultur Sternstunden `@srfkultursternstunden` — Sternstunde Philosophie
- IWM Vienna `@IWMVienna` (also above)
- MAITHINK X `@maithinkx`, Terra X Lesch & Co `@TerraXLeschundCo`, Breaking Lab `@BreakingLab`, Doktor Whatson `@DoktorWhatson`
- c't 3003 `@ct3003`, The Morpheus Tutorials `@TheMorpheusTutorials` — hands-on technology
- Jung & Naiv `@tilojung` — long political interviews
- phoenix `@phoenix`, ARTE `@ARTEde`
- media.ccc.de `@mediacccde` — Chaos Computer Club talks; re:publica `@republica`; Alexander von Humboldt Institute for Internet and Society `@HIIGBerlin`; Ars Electronica `@arselectronica`
- DER STANDARD `@derStandardat`

### Czech

- DVTV `@DVTVvideo` — long interviews
- ČT24 `@CT24zive` — including Hyde Park Civilizace and Za Horizontem; Věda 24 `@vedaCT24`; Česká televize `@CeskaTelevizeTV`
- AI v kostce `@AIvkostce` — Czech AI podcast
- Petr Ludwig `@petr.ludwig` — Deep Talks interviews
- Deník N `@DeniknCZ`
- Akademie věd ČR `@CzechAcademyofSciences`

### Slovak

- Denník N `@DenniknSk`
- SME `@SMEvideo`
- Aktuality.sk `@Aktuality_sk`
- STVR `@SlovenskaTeleviziaARozhlas`, STVR – Diskusie a politika `@STVR-Diskusieapolitika`
- Vedátor `@vedator_sk` — the Slovak Academy of Sciences' science podcast
- Slovenská akadémia vied `@Slovenskáakadémiavied`

## What to report

Aim for 5–12 videos. For each item, the summary says who speaks, their role, and the main argument or finding in plain words, and why it is worth the reader's time. Then add one line:
`Channel: [name] · Language: [English / German / Czech / Slovak] · Length: [h:mm] · Uploaded: [date] · Signal: [views]`

Views are a signal of attention, not of quality. Speakers' claims are their own; label opinion and speculation as such.

## Sections

1. AI engineering and research
2. Builders and founders
3. Society, politics and economics
4. Science and philosophy
5. German-language
6. Czech and Slovak

A video belongs in the first section whose topic fits; German, Czech and Slovak videos go in their language section whatever the topic.

# Slovak edition: translation audit

Audit of the Slovak edition of AI News Daily (`/sk/`) against its English source, run on 2026-11-11 against the repository at the head of `main`. English is the source; the Slovak is machine-translated by `prompts/translator-prompt.md`. Nothing in `content/` was changed.

**146 findings** in 19 files (30 severity 1, 71 severity 2, 45 severity 3). Every English and Slovak quotation in the table was checked by script against the file it names.

Severity: **1** = a Slovak editor must change it (wrong word, changed meaning, English left in, a headline that says something else); **2** = stiff or inconsistent, an editor would normally fix it; **3** = minor. Proposals are suggestions for a native editor, not final text; entries I am unsure of are marked `needs_review` in the map.

## 1. Bottom line

The Slovak reads like journalism in most paragraphs. Sentences are mostly natural, the formats (decimal comma, `73 %`, „…“, month names, declined names) are right, the UI strings have one small slip, and apart from the untranslated paragraphs and the dropped date range described below I did not notice omitted content in the posts I read. What fails is **vocabulary, not style**, and it fails the same way day after day.

**The three most damaging patterns**

1. **False friends and wrong-sense words: 32 findings in 11 files, 14 of them severity 1.** „sedenie“ for a licence seat, „ovládač“ (a driver) for a dial, „spúšťacie dokumenty“ for launch documents, „účet“ (a bank account) for an account of events, „starší“ (older) for senior, „zisk“ (profit) for gain, „formácia“ for business formation, „otras“ for economic shock, „platobné údaje“ for payroll data, and „práca“ for paper. Each one changes what a Slovak reader understands.
2. **Terminology: 40 findings in 10 files** (22 where one English term gets several Slovak renderings, 18 where a domain term is wrong or should stay English). The worst single case is *frontier model* → „hraničný model“ (borderline model), about 30 uses in 13 posts, while the same edition writes „špičkový“ 39 times. Reinforcement learning has three renderings, supervised fine-tuning four, alignment two, reward hacking three, dataset three.
3. **Calques of English phrasing: 38 findings in 12 files.** „by a factor of“ → „faktorom“, „under a prompt“ → „pod promptom“, a paper that „sa pýta“, „best-fitting“ → „najlepšie sediacich“, „measures“ → „miery“, and one that changes a fact: „fell by more than twice as much as“ → „klesol viac než dvojnásobne“.

Two smaller problems are worth knowing about: English quotations are left in English with a Slovak gloss in brackets (4 findings in 2 posts; the prompt itself forbids it), and the 24 October digest contains **8 paragraphs that were never translated** (`check_posts.py` does not look for English prose).

**Root cause.** Each day's translation is done by a fresh agent that cannot see yesterday's choices. The prompt's glossary has about 40 rows and none of the terms above, so every run decides again. The map gives all of them one answer.

## 2. What was audited, and how far

Fifteen post pairs were examined (the brief asked for at least 15): 11 compared side by side, some only in part, and 4 read in Slovak with the English consulted for the phrases I doubted. I also compared the About page and the UI strings and read the Slovak parts of the site configuration. Where a pair was only partly read, the table says how much.

| Key | Post or file | Type | Date | What was read |
|---|---|---|---|---|
| `backdoor` | `when-clean-data-activates-a-hidden-backdoor` | article | 11 Nov | full pair |
| `token` | `token-spend-tracks-who-uses-agents-not-what-gets-shipped` | article | 11 Nov | full pair |
| `d11` | `ai-daily-digest-for-11-november-2026` | digest | 11 Nov | first 80 of 148 blocks, side by side |
| `fable` | `fable-5-2-cuts-its-list-price-but-the-bill-follows-effort` | article | 10 Nov | full pair |
| `vision` | `vision-models-can-reason-about-beliefs-after-they-see` | article | 10 Nov | full pair |
| `d10` | `ai-daily-digest-for-10-november-2026` | digest | 10 Nov | the first 40 of 61 headings and bold leads side by side; paragraphs below the leads not read |
| `student` | `student-codebases-tripled-and-the-comments-did-not` | article | 9 Nov | first 12 of 20 blocks, side by side |
| `reward` | `reward-training-selects-better-answers-not-better-reasoning` | article | 8 Nov | first 14 of 25 blocks, side by side |
| `firms` | `more-firms-start-alone-in-the-sectors-ai-touches-most` | article | 8 Nov | first 12 of 24 blocks, side by side |
| `boe` | `bank-of-england-puts-ais-uk-productivity-gain-at-half-a-percent` | article | 7 Nov | full pair |
| `voters` | `voters-turn-down-data-centres-two-suppliers-fall-21` | article | 5 Nov | first 14 of 21 blocks, side by side |
| `metr` | `metr-finds-anthropics-progress-doubled-key-proof-redacted` | article | 6 Nov | Slovak read in full; English consulted for quoted phrases only |
| `fresh` | `freshworks-hits-1-billion-arr-with-a-third-fewer-staff` | article | 4 Nov | Slovak read in full; English consulted for quoted phrases only |
| `google` | `googles-ai-answers-sell-for-less-and-the-market-noticed` | article | 30 Oct | Slovak read in full; English consulted for quoted phrases only |
| `labour` | `labours-share-of-output-hit-a-record-low-ai-one-suspect` | article | 1 Nov | Slovak read in full; English consulted for quoted phrases only |
| `d24` | `ai-daily-digest-for-24-october-2026` | digest | 24 Oct | found by a corpus scan for untranslated text; not audited otherwise |
| `srcreport` | `a-models-source-report-did-not-come-from-its-evidence` | article | – | found by a format scan; not audited otherwise |
| `about` | `content/about.sk.md` | static page | – | full pair with content/about.md |
| `i18n` | `i18n/sk.yaml` | UI strings | – | all 12 shared strings against i18n/en.yaml; hugo.toml menu and home text read |

Limits you should know about:

- I did not read every paragraph of every pair. Pairs marked "first N blocks" were read to that point only; findings in the table come from what was read.
- For `metr`, `fresh`, `google` and `labour` I read the Slovak and looked at the English only for the phrases I doubted. Those findings are about the Slovak being wrong or odd; I did not check them for omissions.
- 175 Slovak posts exist. The other ~160 were not read; they were scanned by pattern (section 6), which finds repeated forms but not new kinds of error.
- I did not run a corpus-wide comparison of figures. My first attempt gave mostly false positives (decimal commas, thousands separators, the 24-hour clock) and I did not tune it. The three re-translated posts were checked number by number (`verification.md`).
- I am not a native speaker. Proposals follow the usage I found elsewhere in the edition and general Slovak usage; the `needs_review` entries in the map are the ones I am least sure about.
- The other editions (nl, fr, de, es, zh) were not audited.

## 3. The pipeline as found

The brief said to read the pipeline before judging output. It works as follows, and it differs from "a script that calls a prompt" in one way that matters for the fix.

- **The prompt** is `prompts/translator-prompt.md` (the Slovak one; the other five languages have `translator-<lang>-prompt.md`). It has sections for fidelity rules, style, formats, a ~40-row terminology table, the file structure and a self-check.
- **Two runs call it.** `prompts/main-prompt.md`, Pass 2: the production run (GPT) translates the day's English digest and articles that have no Slovak twin, then a *mandatory readability editor* pass runs over the Slovak text. `prompts/article-run.md`, step 7: Claude translates its own article, in a subagent started by `prompts/routine-anthropic.md`. Both say "apply `prompts/translator-prompt.md`".
- **No script calls it.** The runs are agents that read the prompt file from the repository. The map therefore needs no injection script: the prompt tells the agent to read the map file. `scripts/translation_queue.py` serves only the five other languages (`prompts/translation-run.md` says the Slovak edition "is not yours"). `scripts/check_posts.py --strict` is the only automated check on a Slovak file: front matter, tags, date, URLs, claim labels, English headings and translator notes.
- **UI strings** are `i18n/sk.yaml` (14 entries, 12 of them shared with English) and `hugo.toml` (menu names, home text, footer). They are static, written once.
- **`.github/workflows/check-site.yml`** builds the site and runs the checks above; it does not touch translation.

The task said to stop if the pipeline works differently than described. It does not differ in a way that changes the plan: the prompt exists, and nothing has to be injected. I note it because "change the calling script" turned out to mean "nothing to change".

## 4. Summary by category

| Category | Findings | Severity 1 | Severity 2 | Severity 3 | Files |
|---|---:|---:|---:|---:|---:|
| False friends and wrong-sense words | 32 | 14 | 15 | 3 | 11 |
| One English term, several Slovak renderings | 22 | 4 | 13 | 5 | 7 |
| Wrong or untranslated domain term | 18 | 4 | 9 | 5 | 8 |
| Calques of English phrasing | 38 | 1 | 22 | 15 | 12 |
| Headlines and subheads | 8 | 4 | 1 | 3 | 7 |
| Fidelity: English left, quotes glossed, data dropped | 7 | 2 | 5 | 0 | 4 |
| Grammar, agreement, spelling | 7 | 1 | 2 | 4 | 6 |
| Idioms and metaphors word for word | 7 | 0 | 2 | 5 | 5 |
| Names, register, currency, direct address | 7 | 0 | 2 | 5 | 5 |
| **Total** | **146** | **30** | **71** | **45** | **19** |

**Patterns** (a finding carries one pattern label; section 6 gives corpus-wide counts for the main ones):

| Pattern | Findings | Files | Severity 1 |
|---|---:|---:|---:|
| Calque: English phrasing or word order kept | 38 | 12 | 1 |
| False friend: wrong-sense Slovak word | 28 | 9 | 13 |
| One English term, several Slovak renderings | 22 | 7 | 4 |
| Domain term kept or mistranslated | 14 | 7 | 0 |
| Headline or subhead follows English headline style | 8 | 7 | 4 |
| Grammar or agreement error | 7 | 6 | 1 |
| Idiom or metaphor translated word for word | 7 | 5 | 0 |
| Name or register: undeclined product/company name, direct address, currency format | 7 | 5 | 0 |
| English quote left in English, with a Slovak gloss in brackets | 4 | 2 | 0 |
| frontier → „hraničný“ | 4 | 2 | 4 |
| paper → „práca“ (ambiguous with work/labour) | 4 | 4 | 1 |
| Fidelity: dropped, mistranslated or left in English | 3 | 2 | 2 |

## 5. Findings, worst first

Sorted by severity, then category, then pattern. The ID is stable and is what the map cites as `evidence`. File keys are in the table in section 2. "Proposed" is a suggestion.

| ID | Sev | Category | File | English | Current Slovak | Proposed Slovak | Reason |
|---|:-:|---|---|---|---|---|---|
| SK-001 | 1 | falsefriend | `boe` | A senior trainee has just handed in her notice | Staršia trainee práve podala výpoveď | Stážistka vo vyššom ročníku praxe práve podala výpoveď | Starší ≠ senior; „trainee“ nechané po anglicky, hoci ide o účtovnícku prax. |
| SK-002 | 1 | falsefriend | `boe` | Nothing in the Bank's account contradicts | Nič v účte banky nie je v rozpore | Nič v opise banky nie je v rozpore | „Účet banky“ = bankový účet; account = výklad, opis. |
| SK-003 | 1 | falsefriend | `boe` | productivity gains from new technologies take time | zisky z produktivity z nových technológií | prínosy v produktivite z nových technológií | gain ≠ zisk (profit). Pozri aj ďalšie dva riadky. |
| SK-004 | 1 | falsefriend | `d10` | an elevated summariser leaked | zvýhodnený sumarizátor prezradil | sumarizátor so zvýšenými oprávneniami prezradil | Elevated (privileges) ≠ zvýhodnený (favoured); zmení sa význam bezpečnostného testu. |
| SK-005 | 1 | falsefriend | `fable` | The dial Anthropic points to | Ovládač, na ktorý ukazuje Anthropic | Nastavenie, na ktoré ukazuje Anthropic | V IT je „ovládač“ driver; dial = nastavenie/regulátor. |
| SK-006 | 1 | falsefriend | `fable` | assembled from launch documents | poskladaný zo spúšťacích dokumentov | poskladaný z dokumentov k uvedeniu modelu | „Spúšťací“ = spúšťajúci (trigger); launch = uvedenie. |
| SK-007 | 1 | falsefriend | `fable` | standard Team seats | štandardné sedenia v pláne Team | štandardné licencie v pláne Team | „Sedenie“ je sitting/session, nie seat (licencia, používateľské miesto). |
| SK-008 | 1 | falsefriend | `firms` | calls the remainder "solo-type" formation | formáciou typu | vznikom firiem typu | Business formation = vznik/zakladanie firiem; „formácia“ je vojenská alebo geologická. |
| SK-009 | 1 | falsefriend | `firms` | other shocks in those years | pre iné otrasy v týchto rokoch | pre iné šoky v týchto rokoch | Ekonomický shock = šok; „otras“ je tremor/shake. |
| SK-010 | 1 | falsefriend | `fresh` | Freshworks is one firm's account of one set of jobs | Freshworks je účet jednej firmy | Freshworks je výpoveď jednej firmy | Rovnaký false friend (account → účet). |
| SK-011 | 1 | falsefriend | `fresh` | write it up for a senior colleague | pre staršieho kolegu | pre skúsenejšieho kolegu | senior = skúsenejší, nie starší (vekom). |
| SK-012 | 1 | falsefriend | `labour` | using ADP payroll data | platobných dátach ADP | mzdových údajoch ADP | Payroll = mzdy; „platobné údaje“ sú platby. V bank-of-england tej istej dvojice správne „mzdové údaje“. |
| SK-013 | 1 | falsefriend | `token` | heaviest third of users | najťažšia tretina používateľov | najintenzívnejšia tretina používateľov | Heavy user = intenzívny používateľ; „ťažký“ je o hmotnosti. |
| SK-014 | 1 | falsefriend | `firms` | Management analysts are the paper's case study | prípadovou štúdiou práce | prípadovou štúdiou článku | „Prípadová štúdia práce“ sa číta ako „štúdia o práci (zamestnaní)“ – v ekonomickom texte o trhu práce. |
| SK-015 | 1 | fidelity | `d24` | Alibaba DAMO Academy publishes the RynnUnify family | Alibaba DAMO Academy publishes the RynnUnify family | (preložiť celý odsek) | 8 odsekov v digeste z 24. 10. 2026 ostalo po anglicky; check_posts.py to nezachytí. |
| SK-016 | 1 | fidelity | `d24` | Joules-to-GDP: across 220 GDPval tasks | Joules-to-GDP: across 220 GDPval tasks | (preložiť celý odsek) | Rovnaká chyba, ten istý súbor. |
| SK-017 | 1 | headline | `fable` | the bill follows effort | účet však určuje úroveň uvažovania | no účet závisí od úrovne uvažovania | Obrátená príčinnosť: podľa slovenčiny účet určuje úroveň uvažovania, nie naopak. |
| SK-018 | 1 | headline | `labour` | AI is one suspect | AI je len podozrivá | AI je jednou z podozrivých | „Len podozrivá“ mení význam (nepreukázaná vs. jedna z viacerých). |
| SK-019 | 1 | headline | `reward` | Reward training selects better answers, not better reasoning | Trénovanie odmenou vyberá lepšie odpovede, nie uvažovanie | Trénovanie odmenou vyberá lepšie odpovede, nie lepšie uvažovanie | Vynechané „better“ znamená, že model „vyberá uvažovanie“. |
| SK-020 | 1 | headline | `voters` | Two Suppliers Fall 21% | dvaja dodávatelia klesli o 21 % | akcie dvoch dodávateľov klesli o 21 % | Metonymia z angličtiny: neklesli dodávatelia, ale akcie. |
| SK-021 | 1 | grammar | `d10` | The BBC reports that the airline connects the move | aerolínie spájajú krok | aerolínia spája krok | Jednotné číslo v origináli (Qantas); slovenčina má množné. |
| SK-022 | 1 | drift | `d10` | supervised fine-tuning produced | Riadené dolaďovanie vytvorilo | Dolaďovanie s učiteľom (SFT) vytvorilo | Ďalší zo štyroch tvarov pre SFT. |
| SK-023 | 1 | drift | `d11` | Supervised fine-tuning on model-generated data | Dohliadané dolaďovanie na dátach | Dolaďovanie s učiteľom (SFT) na dátach | „Dohliadané“ je kalk; štyri tvary pre SFT (dohliadané / riadené / s dohľadom / ponechané po anglicky). Slovenský ekvivalent supervised learning je „učenie s učiteľom“. |
| SK-024 | 1 | drift | `d11` | reinforcement learning improves control | posilňovacie učenie zvyšuje kontrolu | posilňované učenie zvyšuje kontrolu | Tri tvary pre RL na jednom webe (posilňované / posilňovacie / reinforcement learning). |
| SK-025 | 1 | drift | `reward` | reinforcement training | pri reinforcement learningu | pri posilňovanom učení | Termín nechaný po anglicky, hoci zvyšok webu píše „posilňované učenie“ (39×) alebo „posilňovacie učenie“ (14×). |
| SK-026 | 1 | term | `backdoor` | Scaling the method to frontier training | Škálovanie metódy na trénovanie hraničných modelov | Rozšírenie metódy na trénovanie špičkových modelov | Rovnaká chyba; k tomu anglický reťazec podstatných mien (škálovanie … na trénovanie …). |
| SK-027 | 1 | term | `backdoor` | a deployed frontier model currently carries | nasadený hraničný model už takéto | nasadený špičkový model už takéto | „Hraničný“ znamená okrajový/medzný; frontier model = špičkový model. |
| SK-028 | 1 | term | `d11` | Frontier coding models searched | Hraničné programátorské modely hľadali | Špičkové modely na programovanie hľadali | Rovnaká chyba v nadpise; token-spend v tej istej digest píše správne „špičkový model“. |
| SK-029 | 1 | term | `d11` | Researchers tested 13 frontier chatbots | 13 hraničných chatbotov | 13 špičkových chatbotov | „Hraničný“ = borderline; tá istá digest používa inde „špičkový“. |
| SK-030 | 1 | calque | `boe` | had fallen by more than twice as much as in the least exposed group | klesol viac než dvojnásobne oproti najmenej vystaveným | klesol viac než dvakrát výraznejšie ako v najmenej vystavenej skupine | Pôvodne „pokles dvojnásobne väčší“; slovenský text sa číta ako „viac než zdvojnásobený pokles“ – iná informácia. |
| SK-031 | 2 | falsefriend | `boe` | reduced trainee intakes | zníženým prijímaním trainee | zníženým náborom stážistov | „Prijímanie trainee“ – anglicizmus s nesprávnym skloňovaním. |
| SK-032 | 2 | falsefriend | `boe` | the gain elsewhere is not yet visible | zisk inde zatiaľ nie je viditeľný | prínos inde zatiaľ nie je viditeľný | Rovnako. |
| SK-033 | 2 | falsefriend | `d10` | held-out work descriptions | zadržaných pracovných opisov | testovacích (pri trénovaní nepoužitých) opisov | held-out set ≠ „zadržaný“ (detained). |
| SK-034 | 2 | falsefriend | `d11` | Round-to-nearest recurrent state | stavu opakovanej siete | rekurentného stavu | Recurrent = rekurentný (v StateBench v d10 správne „rekurentné modely“); „opakovaný“ je repeated. |
| SK-035 | 2 | falsefriend | `d11` | The authors conclude that token spend | Autori uzatvárajú, že spotreba | Autori dospeli k záveru, že spotreba | „Uzatvárať“ = zavrieť; conclude = dospieť k záveru. |
| SK-036 | 2 | falsefriend | `d11` | The control means a strong linear readout | Kontrola znamená, že silný lineárny odpočet | Kontrolný experiment ukazuje, že silné lineárne vyčítanie | „Kontrola“ = oversight; control = kontrolný experiment. „Odpočet“ = deduction/countdown. |
| SK-037 | 2 | falsefriend | `d11` | first-year associates already do different work | spolupracovníci v prvom roku | juniorní konzultanti v prvom roku | Associate (firemná pozícia) ≠ spolupracovník. |
| SK-038 | 2 | falsefriend | `d11` | kitting parts on Mercedes-Benz lines | pri triedení súčiastok | pri kompletizácii súprav súčiastok | Kitting = skladanie súprav, nie triedenie (sorting). |
| SK-039 | 2 | falsefriend | `d11` | reasoning capability follows base-model perplexity | sleduje perplexitu základného modelu | súvisí s perplexitou základného modelu | „Sleduje“ = watches; follows/tracks (korelácia) = súvisí/koreluje. |
| SK-040 | 2 | falsefriend | `d11` | restricts weight updates to their span | aktualizácie váh na ich rozpätie | aktualizácie váh na ich lineárny obal | Span v lineárnej algebre = lineárny obal; „rozpätie“ = range/wingspan. |
| SK-041 | 2 | falsefriend | `labour` | AI's gains are not reaching firms' results | zisky z AI sa do výsledkov firiem nedostávajú | prínosy AI sa do výsledkov firiem nedostávajú | Rovnako. |
| SK-042 | 2 | falsefriend | `student` | Frameworks and project templates can add boilerplate | môžu pridať štandardný kód | môžu pridať boilerplate (šablónový kód) | Boilerplate nie je „štandardný kód“; IT čitateľ čaká „boilerplate“. |
| SK-043 | 2 | falsefriend | `token` | The heaviest users | najťažších používateľov | najintenzívnejších používateľov | Rovnako (2. výskyt v texte). |
| SK-044 | 2 | falsefriend | `token` | The paper has not been peer reviewed | Práca neprešla recenzným konaním | Štúdia neprešla recenzným konaním | Pre paper sa na jednom webe používa „práca“, „článok“ aj „štúdia“. |
| SK-045 | 2 | falsefriend | `vision` | The paper provides code and data | Práca poskytuje kód aj dáta | Štúdia poskytuje kód aj dáta | Rovnako. |
| SK-046 | 2 | fidelity | `fable` | "particularly expensive" and "very verbose" | „particularly expensive“ („mimoriadne drahý“) | „mimoriadne drahý“ a „veľmi rozvláčny“ | Citát ostal po anglicky a slovenčina je v zátvorke; má byť len slovenský citát. |
| SK-047 | 2 | fidelity | `fable` | Cyber Verification and Life Sciences Verification Programs | overovacích programov spoločnosti pre kybernetiku a vedy o živej prírode | programov Cyber Verification a Life Sciences Verification | Názvy programov sa podľa prompt-u (pravidlo 5) nepreklaldajú. |
| SK-048 | 2 | fidelity | `fable` | fail to "meet your requirements" | aby „meet your requirements“ („spĺňali vaše požiadavky“) | aby „spĺňali vaše požiadavky“ | Rovnako; navyše gramaticky nezapadá do vety. |
| SK-049 | 2 | fidelity | `token` | "is not there yet" | „tam ešte nie je“ („is not there yet“) | „tam ešte nie je“ | Prekladateľ pridal anglický originál; porušuje „nothing added“ aj pravidlo 6 (citát prelož). |
| SK-050 | 2 | fidelity | `about` | Articles published between 15 September and 12 October 2026 | Články zverejnené do 12. októbra 2026 | Články zverejnené od 15. septembra do 12. októbra 2026 | V slovenčine chýba začiatok obdobia. |
| SK-051 | 2 | headline | `vision` | Vision models can reason about beliefs after they see clearly | Vizuálne modely chápu presvedčenia, keď správne vidia | Modely pre obraz a jazyk vedia uvažovať o presvedčeniach, ak správne vnímajú scénu | „Chápu“ ≠ „reason“; „vidia“ → vnímajú; bez „can“ znie ako fakt. |
| SK-052 | 2 | grammar | `boe` | has delivered zero financial payoff | technológia „neprinieslo | technológia „neprinesla | Rod: technológia – neprinieslo. |
| SK-053 | 2 | grammar | `google` | what a question is worth | čo má otázka hodnotu | akú hodnotu má otázka | Chýba väzba. |
| SK-054 | 2 | drift | `backdoor` | harmless under one dataset composition | zložení dátového súboru | zložení datasetu | dataset: „dataset“ (40×), „dátový súbor“ (13×), „súbor dát/údajov“ (11×) – tri tvary; v slovenských IT textoch sa používa „dataset“. |
| SK-055 | 2 | drift | `backdoor` | reward-hacks a coding task | model obchádza odmenu pri programátorskej úlohe | model zneužíva odmeňovanie (reward hacking) pri programátorskej úlohe | „Obchádzať odmenu“ neopisuje reward hacking (model odmenu získava nečestne); tri rôzne preklady webu. |
| SK-056 | 2 | drift | `d10` | AI adoption raised monthly sales | Nasadenie AI zvýšilo mesačné tržby | Zavedenie AI zvýšilo mesačné tržby | adoption = nasadenie / zavádzanie / adopcia; „nasadenie“ je deployment. |
| SK-057 | 2 | drift | `d10` | Most measured sycophancy | Väčšina nameranej servilnosti | Väčšina nameraného pochlebovania | „Servilnosť“ (5×) vs. „pochlebovanie“ (14×) pre sycophancy; „servilný“ je slovo o postavení, nie o ústupčivosti modelu. |
| SK-058 | 2 | drift | `d10` | Reward-hacking monitors face a trade-off | Monitory odmeňovacích podvodov čelia | Monitory zneužívania odmeňovania (reward hacking) čelia | Tretí tvar („odmeňovacie podvody“) pre rovnaký pojem. |
| SK-059 | 2 | drift | `d10` | preference optimisation.** Across the studied checkpoints | Neskoršie zarovnanie ju zvýšilo | Neskoršie zosúladenie ju zvýšilo | „Zarovnanie“ vs. „zosúladenie“ (28×) pre alignment; vyber jedno. |
| SK-060 | 2 | drift | `d11` | 20% mix of reward-hacking transcripts | prepisov s obchádzaním odmeny | prepisov so zneužívaním odmeňovania (reward hacking) | Druhý tvar v tej istej digest. |
| SK-061 | 2 | drift | `d11` | apparent sycophancy into self-correction | zo zdanlivej servilnosti na sebaopravu | zo zdanlivého pochlebovania na sebaopravu | Rovnaký pojem, druhý tvar v susedných digestoch. |
| SK-062 | 2 | drift | `firms` | A second data set, the Current Population Survey | Druhý súbor údajov | Druhý dataset | Tretí tvar pre dataset; v čisto ekonomickom texte je „súbor údajov“ prijateľný, v ML/IT texte treba jednotne. |
| SK-063 | 2 | drift | `reward` | without a preliminary supervised fine-tuning stage | bez predchádzajúceho supervised fine-tuningu | bez predchádzajúcej fázy dolaďovania s učiteľom | Anglický termín ohýbaný slovenskou príponou (-u) pri tom, čo inde preložené. |
| SK-064 | 2 | drift | `token` | For adoption, they suggest | Pri sledovaní adopcie | Pri sledovaní miery využívania | „Adopcia“ je v bežnej slovenčine osvojenie dieťaťa. |
| SK-065 | 2 | drift | `token` | caching repeated context | ukladať opakovaný kontext do vyrovnávacej pamäte | cachovať opakovaný kontext | Rovnaký pojem ako v fable („cache“); „vyrovnávacia pamäť“ je pre IT čitateľa príliš formálna. |
| SK-066 | 2 | drift | `vision` | Vision models can reason about beliefs | Vizuálne modely chápu presvedčenia | Modely pre obraz a jazyk dokážu uvažovať o presvedčeniach | Nadpis „vizuálne modely“, text „modely pre obraz a jazyk“; chýba ustálený tvar „vizuálno-jazykový model (VLM)“. Plus „chápu“ ≠ „reason“. |
| SK-067 | 2 | term | `boe` | The Bank's Agents, who talk to businesses | Agenti banky, ktorí sa rozprávajú | regionálni zástupcovia banky (Agents), ktorí sa rozprávajú | V texte o AI čitateľ pochopí „agentov“ ako softvér. needs_review. |
| SK-068 | 2 | term | `d10` | self-evolving agent harness | samovyvíjajúci sa agentový nástroj | samovyvíjajúci sa agentový harness | Harness je termín; „nástroj“ ho stratí. |
| SK-069 | 2 | term | `d11` | Agentic commerce has produced | Agentový obchod priniesol | Nákupy cez AI agentov priniesli | „Agentový obchod“ nie je ustálené spojenie; needs_review (agentový vs. agentický). |
| SK-070 | 2 | term | `fresh` | enterprise software | firemný softvér | podnikový softvér | „Firemný“ = company’s; enterprise software = podnikový/enterprise. |
| SK-071 | 2 | term | `fresh` | release candidate | kandidáta na vydanie | release candidate | V IT žargóne sa nepreložilo. |
| SK-072 | 2 | term | `reward` | confidence interval | interval neistoty | interval spoľahlivosti | Štatistický termín. |
| SK-073 | 2 | term | `student` | End-of-semester codebases | Kódové základne na konci semestra | Projekty na konci semestra / codebasy | Rovnaký kalk. |
| SK-074 | 2 | term | `token` | an unfamiliar codebase, language or stack | technologického balíka | technologického stacku | Stack ostáva v IT slovenčine „stack“; „balík“ = package. |
| SK-075 | 2 | term | `token` | unfamiliar codebase | neznámej kódovej základne | neznámeho codebasu (alebo: cudzieho kódu) | „Kódová základňa“ je kalk (9× v 5 súboroch); needs_review. |
| SK-076 | 2 | calque | `backdoor` | Behaviour under the normal assistant prompt stays unchanged | Správanie pod bežným promptom asistenta sa nemení | Správanie pri bežnom prompte asistenta sa nemení | „Pod promptom“ (under a prompt) ×3 v texte a v nadpise; slovenčina: „pri prompte“. |
| SK-077 | 2 | calque | `backdoor` | Misalignment rises under one prompt | Nesprávne zosúladenie rastie pod jedným promptom | Nesprávne zosúladenie rastie pri jednom prompte | Rovnaký kalk v nadpise. |
| SK-078 | 2 | calque | `backdoor` | The result also transferred misalignment through filtered code | Výsledok preniesol cez filtrovaný kód a reťazce uvažovania aj nesprávne zosúladenie | Prenášalo sa aj nesprávne zosúladenie – cez filtrovaný kód aj reťazce uvažovania | Neživotný podmet výsledok + sloveso činnosti. |
| SK-079 | 2 | calque | `backdoor` | the simplest fit can attach it to the task | najjednoduchšie prispôsobenie ju môže pripojiť | najjednoduchší model ju môže pripísať celej úlohe | Fit (ML) → kalk „prispôsobenie“. |
| SK-080 | 2 | calque | `boe` | Labour-market effects, it says, are seen "primarily through lower replacement hiring | nižším náhradným prijímaním | menším počtom prijatých ako náhrada za odchádzajúcich | Doslovný kalk. |
| SK-081 | 2 | calque | `boe` | increasing upside risks | rastúce riziká smerom nahor | rastúce riziká v prospech vyššieho rastu | Centrálnobankový žargón (upside risks) doslovne. needs_review. |
| SK-082 | 2 | calque | `boe` | the door at the bottom of the profession narrows | dvere na spodku profesie sa pritom zužujú | vstup do profesie sa zužuje | Metafora zachovaná doslovne; zmysel (vstup pre začiatočníkov) sa stráca. |
| SK-083 | 2 | calque | `fable` | Anthropic does not dispute that effort matters | nespochybňuje, že úroveň uvažovania záleží | nespochybňuje, že úroveň uvažovania je dôležitá | „Záleží“ bez „na“ je nesprávne. |
| SK-084 | 2 | calque | `fable` | The limits are worth stating | Hranice treba povedať | Treba uviesť aj obmedzenia | „Hranice povedať“ nedáva zmysel. |
| SK-085 | 2 | calque | `fable` | The offers are written for subscription plans | Ponuky sú napísané pre predplatné plány | Ponuky platia pre plány s predplatným | Written for → platia pre; „predplatné plány“ nie je správny prídavok. |
| SK-086 | 2 | calque | `google` | is the pattern the market priced | je vzorec, ktorý trh ocenil | je vzor, ktorý trh ocenil | Rovnako. |
| SK-087 | 2 | calque | `labour` | better measures than a single national ratio | lepšie miery než jediný národný pomer | lepšie metriky než jediný národný pomer | Rovnako. |
| SK-088 | 2 | calque | `metr` | Key intermediate measures | Kľúčové medziľahlé miery | Kľúčové medziľahlé ukazovatele | Rovnako. |
| SK-089 | 2 | calque | `metr` | by less than a factor of 2 | o menej než násobok 2 | o menej než dvojnásobok | Kalk, nezrozumiteľné. |
| SK-090 | 2 | calque | `student` | The authors name this pattern | Autori tento vzorec nazývajú | Autori tento jav nazývajú | „Vzorec“ = formula; pattern = vzor/jav. Vzorec v tomto význame 67× v 42 súboroch. |
| SK-091 | 2 | calque | `token` | according to the authors' account of press reports | Podľa autorov a ich výkladu tlačových správ | Podľa autorov, ktorí sa opierajú o tlačové správy, | Doslovný preklad zničil vetu (kto čo tvrdí). |
| SK-092 | 2 | calque | `token` | differ in spend by a factor she cannot explain | líšia v spotrebe faktorom, ktorý si nevie vysvetliť | spotreba sa líši mnohonásobne a nevie si to vysvetliť | „Faktorom“ je kalk z „by a factor of“. |
| SK-093 | 2 | calque | `token` | doubling an engineer's spend through a target | zdvojnásobenie jeho spotreby cez cieľ | zdvojnásobenie jeho spotreby stanovením cieľa | „Cez“ ako prostriedok je kalk. |
| SK-094 | 2 | calque | `token` | from the best-fitting curves | z najlepšie sediacich kriviek | z kriviek s najlepším prispôsobením | Hovorové „sediace“ pre best-fit. |
| SK-095 | 2 | calque | `token` | the field needs validated measures of the value | odbor potrebuje overené miery hodnoty | oblasť potrebuje overené metriky hodnoty | Measure = metrika, nie „miera“ (rovnako v labour a metr). |
| SK-096 | 2 | calque | `token` | which asks what an engineer's token spend actually measures | ktorý sa pýta, čo spotreba tokenov inžiniera vlastne meria | ktorý skúma, čo vlastne meria spotreba tokenov inžiniera | Preprint sa „nepýta“; skúma. Podobne „Práca sa potom pýta“. |
| SK-097 | 2 | calque | `vision` | An assistant that watches a workplace | Asistent sledujúci pracovisko, robot konajúci medzi ľuďmi | Asistent, ktorý sleduje pracovisko, robot, ktorý koná medzi ľuďmi | Činné príčastia (-úci) namiesto vedľajšej vety – úradnícka slovenčina (aj v ďalších textoch). |
| SK-098 | 2 | idiom | `metr` | very loose evidence | veľmi voľný dôkaz | veľmi slabý dôkaz | Loose evidence ≠ voľný dôkaz. |
| SK-099 | 2 | idiom | `voters` | much more bark than bite | oveľa viac štekotu než hryzenia | oveľa viac hluku než skutočného účinku | Anglický idióm; slovenský čitateľ ho nepozná. |
| SK-100 | 2 | name | `d11` | after Anthropic introduced workplace apps | pracovných aplikácií Anthropic | pracovných aplikácií od Anthropicu | Prompt žiada apozíciu alebo skloňovanie; tu holé „Anthropic“ v genitíve. |
| SK-101 | 2 | name | `google` | were down 12.6% at $283.82 | na 283,82 USD | na 283,82 dolára | Prompt: v texte „dolár“, ISO kódy len v tabuľke. Ďalšie výskyty: „380 USD“, „13,82 USD“. |
| SK-102 | 3 | falsefriend | `d11` | do not guarantee a completed AI facility | dokončené AI zariadenie | dokončené AI dátové centrum | „Zariadenie“ znie ako device. |
| SK-103 | 3 | falsefriend | `d11` | gained 5.7 percentage points | získal 5,7 percentuálneho bodu | zlepšil sa o 5,7 percentuálneho bodu | gain → získať je kalk. |
| SK-104 | 3 | falsefriend | `backdoor` | That work challenged content filtering | Táto práca spochybnila | Tento výskum spochybnil | Rovnako (work vs. paper). |
| SK-105 | 3 | headline | `fable` | How the bill got here | Ako sa účet dostal sem | Ako vznikol tento účet | Doslovné. |
| SK-106 | 3 | headline | `google` | Reddit walls itself in | Reddit sa zatvára za prihlásenie | Reddit sa zatvára za prihlasovaciu bránu | Neprirodzená väzba. |
| SK-107 | 3 | headline | `token` | Counting the right thing | Počítať to správne | Merať správnu vec | Nadpis kalk. |
| SK-108 | 3 | grammar | `d10` | found that recurrent and hybrid models generalised farther | zvýhodnil rekurentné a hybridné modely | ukázal, že rekurentné a hybridné modely zovšeobecňujú lepšie | „Zvýhodnil“ = favoured; benchmark nič nezvýhodňuje. |
| SK-109 | 3 | grammar | `firms` | since early 2024 | od začiatku roku 2024 | od začiatku roka 2024 | Pád. |
| SK-110 | 3 | grammar | `i18n` | The app is already installed on this device | Aplikácia je v tomto zariadení už nainštalovaná | Aplikácia je už nainštalovaná na tomto zariadení | Predložka: na zariadení. |
| SK-111 | 3 | grammar | `student` | a median of about 3.4 thousand lines in 2021 to 2023 | 3,4 tisíc riadkov | 3,4 tisíca riadkov | V tom istom texte „2,3 tisíca“. |
| SK-112 | 3 | drift | `d10` | The public dataset records a 4.57-fold spread | Verejný súbor dát zachytáva | Verejný dataset zachytáva | Ďalší tvar (súbor dát). |
| SK-113 | 3 | drift | `d10` | increased estimated AI exposure | zvýšili odhadovanú expozíciu | zvýšili odhadovanú vystavenosť | Rovnaký pojem. |
| SK-114 | 3 | drift | `d10` | steering the probe direction | usmernenie smeru sondy | riadenie aktivácií | V digest z 11. 11. je pre steering „riadenie aktivácií“. |
| SK-115 | 3 | drift | `firms` | Felten exposure index | index expozície podľa Feltena | index vystavenosti podľa Feltena | V tom istom texte „odvetvia vystavené AI“ a „index expozície“. |
| SK-116 | 3 | drift | `vision` | seven vision-language models | Sedem modelov pre obraz a jazyk | Sedem vizuálno-jazykových modelov (VLM) | Opisný tvar je ťažkopádny a v titulku ho nahradil iný. |
| SK-117 | 3 | term | `boe` | the national living wage | národnej mzdy na živobytie | National Living Wage (britská minimálna mzda pre dospelých) | Britský pojem, doslovný preklad nemá význam. needs_review. |
| SK-118 | 3 | term | `d10` | NBER working paper | Pracovná štúdia NBER | pracovný dokument (working paper) NBER | „Pracovná štúdia“ nie je ekonomický termín. needs_review. |
| SK-119 | 3 | term | `d11` | packages about 200 browser-development guides as an agent skill | do zručnosti pre agenta | do skillu pre agenta | Skill je názov funkcie (Claude, Cursor), nie zručnosť. |
| SK-120 | 3 | term | `fresh` | a real regression from a flaky one | nestabilného testu | flaky testu | Slovenskí testeri: „flaky test“. |
| SK-121 | 3 | term | `fresh` | lock-in | uzamknutie | vendor lock-in (viazanosť na dodávateľa) | Ustálený anglicizmus. |
| SK-122 | 3 | calque | `boe` | most of the recent strength in productivity growth | väčšina nedávnej sily rastu produktivity | väčšina nedávneho silného rastu produktivity | strength of → silný. |
| SK-123 | 3 | calque | `d11` | Multi-turn chatbots | vo viac-kolových rozhovoroch | v dlhších rozhovoroch s viacerými výmenami správ | Spojovník pri „viac-kolových“ je pravopisná chyba; „kolo“ pre turn je kalk. needs_review. |
| SK-124 | 3 | calque | `d11` | The team reproduced the pattern | Tím zopakoval vzorec | Tím zopakoval tento jav | Rovnako. |
| SK-125 | 3 | calque | `d11` | behaviour under a normal assistant prompt stayed unchanged | pod bežným promptom asistenta | pri bežnom prompte asistenta | Rovnaký kalk v digest. |
| SK-126 | 3 | calque | `d11` | junior repetition | opakovanie pri práci juniorov | monotónnu prácu juniorov | Nezrozumiteľné. |
| SK-127 | 3 | calque | `fable` | 73rd of 73 on cost | na 73. miesto zo 73 v nákladoch | na posledné, 73. miesto zo 73 podľa nákladov | „V nákladoch“ je kalk (on cost); poradie 73. treba zachovať (pravidlo 3). |
| SK-128 | 3 | calque | `fable` | A bill is price multiplied by volume | Účet je cena krát objem | Účet je súčin ceny a objemu | „Krát“ ako podstatné/spojka je hovorové (aj „sadzba krát počet“). |
| SK-129 | 3 | calque | `fable` | down from $10 and $50 for the 5.1 versions | po cene 10 a 50 dolárov pri verziách 5.1 | oproti 10 a 50 dolárom pri verziách 5.1 | Down from → oproti. |
| SK-130 | 3 | calque | `fable` | not the reader's | nie čitateľove | nie úlohy čitateľa | Privlastňovací prídavok tu znie archaicky. |
| SK-131 | 3 | calque | `fable` | the figure belongs to one effort level | údaj patrí jednej úrovni uvažovania | údaj platí pre jednu úroveň uvažovania | Belongs to → platí pre. |
| SK-132 | 3 | calque | `firms` | a stand-in for a pattern | zastupuje istý vzorec | zastupuje istý vzor | Rovnako. |
| SK-133 | 3 | calque | `fresh` | realigned around customer experience, employee experience | pretvárala okolo zákazníckej skúsenosti, zážitku zamestnancov | sa preorientovala na zákaznícku a zamestnaneckú skúsenosť | V jednej vete dva preklady experience (skúsenosť / zážitok). |
| SK-134 | 3 | calque | `google` | What Google said on the call | Čo Google povedal počas hovoru | Na telefonickej konferencii o výsledkoch | Samotný „hovor“ znie ako phone call. |
| SK-135 | 3 | calque | `student` | the share of UK undergraduates using generative AI | vysokoškolákov používajúcich generatívnu AI | vysokoškolákov, ktorí používajú generatívnu AI | Rovnaký vzor (-ing → príčastie). |
| SK-136 | 3 | calque | `token` | misleads in its own way | zavádza svojím vlastným spôsobom | zavádza tiež, no iným spôsobom | Doslovné. |
| SK-137 | 3 | idiom | `fable` | not from anyone's diary | nie z ničieho denníka | nie z niečieho skutočného denníka | Zámeno „ničieho“ je kalk. |
| SK-138 | 3 | idiom | `google` | composite | kompozitnú postavu | vymyslenú postavu poskladanú z typických prípadov | „Kompozitný“ sa v slovenčine o postavách nepoužíva. |
| SK-139 | 3 | idiom | `metr` | holds that finding with little confidence | drží s malou istotou | platí s nízkou mierou istoty | „Drží“ je hovorové. |
| SK-140 | 3 | idiom | `token` | deeply flawed | hlboko chybné | zásadne chybné | Kolokácia. |
| SK-141 | 3 | idiom | `voters` | composite, built to stand for that job | Je to zložený obraz, ktorý má predstavovať túto prácu | Je to vymyslená postava poskladaná z typických prípadov | Composite character ×2 prekladaný odlišne: „zložený obraz“ (voters), „kompozitná postava“ (google). |
| SK-142 | 3 | name | `fresh` | Imagine a test engineer | Predstavte si testovaciu inžinierku | Predstavme si testovaciu inžinierku | Oslovenie čitateľa (11 výskytov v 9 súboroch) vs. „Predstavme si“ (31 v 30); prompt: bez priameho oslovenia. |
| SK-143 | 3 | name | `fresh` | test engineer | testovaciu inžinierku | QA inžinierku (testerku) | Test engineer = tester/QA. |
| SK-144 | 3 | name | `google` | Picture a moderator | Predstavte si moderátorku fóra | Predstavme si moderátorku fóra | Rovnako. |
| SK-145 | 3 | name | `srcreport` | changed at most 1.1% | zmenili najviac 1.1% | zmenili najviac o 1,1 % | Desatinná bodka a % bez medzery (prompt: 1,1 %). Ďalšie výskyty v tom istom súbore: 99.6–100%. |
| SK-146 | 3 | name | `student` | Picture a course coordinator | Predstavte si koordinátorku predmetu | Predstavme si koordinátorku predmetu | Rovnako. |

## 6. Corpus-wide counts

Pattern counts over the body text of all 175 Slovak posts (URLs and reference lists excluded). They show which problems are systematic. A regular expression finds forms, not meanings, so read the numbers as approximate.

| Concept | Forms in the edition |
|---|---|
| frontier model | „hraničný model/chatbot/laboratórium…“: 30 in 13 posts<br>„špičkový model/…“: 39 in 22 posts |
| reinforcement learning | posilňované: 39 in 23 posts<br>posilňovacie: 14 in 8 posts<br>reinforcement learning: 11 in 5 posts |
| supervised fine-tuning | dolaďovanie s dohľadom: 5 in 4 posts<br>dohliadané dolaďovanie: 2 in 1 posts<br>riadené dolaďovanie: 2 in 1 posts<br>supervised fine-tuning: 1 in 1 posts |
| alignment | zosúladenie: 28 in 16 posts<br>zarovnanie: 6 in 4 posts |
| reward hacking | obchádzanie odmeny: 9 in 8 posts<br>odmeňovacie podvody: 1 in 1 posts<br>reward hacking: 2 in 1 posts |
| sycophancy | pochlebovanie: 14 in 7 posts<br>servilnosť: 5 in 3 posts<br>sycophancy: 2 in 2 posts |
| dataset | dataset: 40 in 22 posts<br>dátový súbor: 13 in 5 posts<br>súbor dát / údajov: 11 in 6 posts |
| cache | cache: 88 in 24 posts<br>vyrovnávacia pamäť: 41 in 20 posts |
| checkpoint | checkpoint: 64 in 22 posts<br>kontrolný bod: 18 in 16 posts |
| chain of thought | reťazec uvažovania: 18 in 15 posts<br>chain of thought: 8 in 6 posts |
| pattern | vzorec / vzorca / vzorcov: 67 in 42 posts<br>vzor: 50 in 31 posts |
| codebase | kódová základňa: 9 in 5 posts |
| opening of the scene | Predstavme si: 31 in 30 posts<br>Predstavte si (addresses the reader): 11 in 9 posts |
| currency | number + USD in running text: 3 in 1 posts |

Format scan, same corpus: `73 %` and `4,6` are used correctly almost everywhere. Outside the 24 October digest (English left in), only one more post has decimal points and a percent sign without a space (`a-models-source-report-did-not-come-from-its-evidence`), and only one post has `USD` in running text (`google`).

## 7. Static pages and UI strings

**`i18n/sk.yaml`** (12 strings shared with English): clean. Instructions use the polite plural („ťuknite“), Safari/Chrome menu names match the Slovak interface, „iPhone a iPade“ is declined correctly. One small slip: „v tomto zariadení“ should be „na tomto zariadení“ (SK-110, severity 3). `follow_title` drops the verb of the English („Get AI News Daily every morning.“ → „AI News Daily každé ráno.“); that reads as a slogan and I left it. The Slovak adds a LinkedIn newsletter sentence to `follow_text` and `follow_note` says the translation is by AI; both are deliberate differences, not errors.

**`hugo.toml`** (menus, home text, footer, descriptions): no findings. „Čo ľudia tvoria“ for "what people are building" is fixed by the prompt's heading table; I read it as acceptable, if slightly generic.

**About page (`content/about.sk.md`)**: accurate and readable, with one finding. The verification-label section says articles published „do 12. októbra 2026“ end with a table, where the English says between 15 September and 12 October (SK-050); the start of the period was dropped. The page's Slovak title is „O AI News Daily“; the footer link „Ako pracujeme“ points to the section on AI labelling (`#ai-disclosure`), which is headed „Označenie obsahu vytvoreného AI“. That mismatch between the link text and the heading it lands on exists in English too. The first paragraph's 57-word sentence with a ten-item list is as long in English; I left it as a matter of taste.

**Install, archive and search pages**: front matter only; nothing to audit.

## 8. Risks the map does not remove

1. **The readability editor runs after the translator.** `prompts/main-prompt.md` Pass 2, step 2 applies an English-oriented editor prompt (the block under "Editor prompt" in `main-prompt.md`) to the Slovak text. Nothing tells it to keep mapped terms, so it can undo them. I did not change `main-prompt.md` (it is the production run, and the brief limited the change to the translation prompt). One sentence in Pass 2 step 2 would close the gap: *"Keep the renderings of `prompts/translation-maps/sk.yaml` unchanged."* Your call.
2. **Claude's own Slovak twin is written inside a subagent** (`routine-anthropic.md` → `article-run.md` step 7). It reads `translator-prompt.md` when step 7 says so, so it should read the map. Whether a subagent given a short brief actually opens a second file is something only the next days' output can show.
3. **`check_posts.py` cannot see English prose** in a Slovak file (it checks labels, headings and translator notes). That is how the 24 October digest kept 8 English paragraphs. A small check (a paragraph of 12+ words in which more than a fifth of the words are English function words) would catch it; I did not add one because the brief did not ask for a checker change.
4. **Map entries marked `needs_review` bind the translator anyway.** If a reviewer later prefers another variant, the posts translated in between will use the old one. Review the 22 entries soon.
5. **Published posts are untouched.** The patterns above occur in the existing posts (section 6). Fixing them is the separate step you reserved.

## 9. Questions for the native reviewer

The map marks 22 entries `needs_review`. The ones that change the most text if you decide differently:

- **agentic**: keep „agentový“ (94 uses) or move to „agentický“, as in „agentická AI“?
- **alignment**: „zosúladenie“ / „nezosúladený“ or keep „alignment“?
- **supervised fine-tuning**: „dolaďovanie s učiteľom“ (proposed), or the most frequent present form „dolaďovanie s dohľadom“?
- **reinforcement learning**: „posilňované“ (39 uses) over „posilňovacie“ (14)?
- **codebase**: keep „codebase“ (declined) or „zdrojový kód projektu“?
- **pattern**: is „vzorec“ (67 uses) acceptable for "pattern" in running text, or always „vzor“ / „jav“?
- **dataset**: „dataset“ everywhere, or „súbor údajov“ in non-ML contexts?
- **Agents (Bank of England)**: how should this institutional term be written for a Slovak reader?

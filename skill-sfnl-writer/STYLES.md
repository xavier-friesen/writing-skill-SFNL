# Style cards

## The spine is not a style

Every register in this file sits on the same structure: one apex, groups that answer the question
their parent raises, answer first unless the user asked otherwise. That is the skill, not a
choice — it lives in `SKILL.md` and it does not vary. What varies is **texture**: how a heading is
worded, where the evidence sits, how a number is introduced, how loud the verdict is.

Pulling the spine out settles the question of how many registers we need. A consultancy deck and
an SFNL chapter looked like two philosophies while both cards restated the pyramid; with the
pyramid gone, the difference is a handful of texture settings. So this file has **five presets**
over **eleven knobs**, plus two procedures (R and E) that are not registers at all.

## The knobs

Every preset is a set of values on these. The advanced panel in the intake widget exposes them;
the emitted line carries only the ones the user changed. Change one knob and you get a variant;
change six and you should have picked a different preset.

| # | Knob | Values |
|---|---|---|
| 1 | **kop** — heading | `bewering` · `kapitaal-bewering` · `label` · `geen` |
| 2 | **apex** — where the answer lands | `kop` · `eerste-alinea` · `uitgesteld` |
| 3 | **alineakop** — first sentence carries the paragraph's claim | `aan` · `uit` |
| 4 | **bewijs** — how evidence is displayed | `proza` · `lijsten` · `factbox` |
| 5 | **cijfers** — figures | `geschaald` (never bare) · `kaal-mag` · `uit-proza` (results to lists) |
| 6 | **vet** — bold lead-ins in running text | `uit` · `aan` |
| 7 | **woorden** — lexical level | `alledaags` · `vak-afgelost` · `vak-bekend` |
| 8 | **ritme** — sentence-length variance | `hoog` · `gemiddeld` · `vlak` |
| 9 | **aanspreekvorm** | `wij-auteurs` · `onpersoonlijk` · `je-lezer` |
| 10 | **oordeel** — the verdict | `ondertekend` · `impliciet` · `aanbeveling` (opens on a verb) |
| 11 | **beeldspraak** — imagery and ornament, per piece | `0` · `1` · `2` |

Two rules are not knobs and never move: a sentence never opens with a numeral, and no sentence
carries more than three numbers. They are what keeps a fact-dense paragraph readable aloud, and
`cijfers=uit-proza` tightens them further rather than loosening them.

## Preset defaults at a glance

| Knob | H huis | Bd beslisstuk | E essay | V verhaal | K kort |
|---|---|---|---|---|---|
| kop | kapitaal-bewering | bewering | geen | bewering | bewering |
| apex | kop | kop | eerste-alinea | uitgesteld | kop |
| alineakop | aan | aan | uit | uit | aan |
| bewijs | factbox | lijsten | proza | proza | proza |
| cijfers | uit-proza | geschaald | geschaald | geschaald | geschaald |
| vet | aan | aan | uit | uit | uit |
| woorden | vak-afgelost | vak-bekend | alledaags | alledaags | alledaags |
| ritme | gemiddeld | vlak | hoog | hoog | gemiddeld |
| aanspreekvorm | wij-auteurs | onpersoonlijk | onpersoonlijk | onpersoonlijk | onpersoonlijk |
| oordeel | aanbeveling | aanbeveling | impliciet | impliciet | ondertekend |
| beeldspraak | 1 | 0 | 2 | 2 | 0 |

---

## H. Huis — the SFNL report

**Pick this when** the piece belongs in a Social Finance NL report or has to sound as if it could:
a chapter, a case, a management summary, a recommendation. Distilled from *Innovatieve
financiering van preventie* (2025) and *De toekomst van resultaatfinanciering* (2024) and a
house-voice analysis of both. Fourteen passages from those reports, quoted with a note on what
each does technically, sit in `SFNL-SPECIMENS.md` — read the ones matching the move you are about
to write.

The genre is the **pleidooi met bewijslast**: an organisation with a position lines up practice and
derives recommendations from it. That gives the register two tempos, and mixing them up is the
classic failure — a case that sounds like a manifesto is as wrong as a conclusion that sounds like
a factsheet.

- **Two tempos.** Argumentative passages (opening, conclusion, recommendation) are assertive and
  compact. Case passages are descriptive and factual, holding their judgment until the lesson.
- **"We" is the authors**, never the false inclusive we of the policy memo. One exception, and it
  is the moment the piece takes sides: in a normative passage "we" becomes national — *"We betalen
  voor handelingen, niet voor resultaten."* Once per piece. No "u".
- **Chapter shape: knelpunt → casussen → les → aanbeveling.** The opening states the bottleneck
  flat out, with no run-up.
- **A number never stands alone.** Source then rescale, translation to a ratio, return per euro, a
  comparison anchor, or the figure as a paragraph's closing punch. Running prose carries at most
  two numbers per paragraph; result figures go to a list.
- **Mechanism in four steps** — the most copyable move in the house. Name the thing and pay off the
  jargon inside the same sentence, then the money flow, then the conditional inversion (*"Blijven
  de kosten daaronder, dan wordt de besparing gedeeld"*), then what it makes people do.
- **Caveats before the claim**, never trailing after it.
- **Imagery from the domain only**: schotten, potjes, hefboom, spelregels.
- **One sentence under ten words per paragraph** of four or more, and it comes *before* the big
  number, not after.
- **Close on the shortest sentence on the page, and make it turn something over.** A recommendation
  opens with a verb that is an action.

**Three things the reports do that this preset does not copy** (specimens 13 and 14 quote them):
the summarising paragraph more abstract than the material it summarises; the dead closing line
(*"Preventie kan maatschappelijke waarde opleveren"*); and the hedge that guts the recommendation
(*"Het is zinvol om te verkennen hoe…"*, three times in the three recommendations the whole report
rests on). The niet-X-maar-Y inversion is house and it works, and 25 times in one report is a tic:
budget it at one.

**Tests.** Does every paragraph's first sentence summarise it? Does every absolute number get
scaled by the sentence after it? Does the section close on its shortest sentence, and does that
sentence turn something over?

---

## Bd. Beslisstuk — the decision document

**Pick this when** the reader has to decide and will skim the headings before reading a word: a
board paper, a management summary, a tender answer, a deck's speaker text. This is the old
McKinsey card with the pyramid taken out, because the pyramid is now everyone's.

- **Action titles.** Every heading is a full assertion with subject, verb and outcome. Never a
  label, never over fifteen words. "Omzet per regio" fails; "De omzet groeide 14% in Q3, gedreven
  door expansie in APAC" passes.
- **The horizontal read.** Read only the headings and each section's first sentence, in order.
  They must form a complete argument on their own. If they do not, the structure is wrong, not the
  prose.
- **The number goes in the assertion**, not in a subclause: "Efficiëntiemaatregelen besparen 7,4
  mln per jaar", not "Door implementatie van efficiëntiemaatregelen is jaarlijks 7,4 mln besparing
  mogelijk."
- **Outcome, not process.** What was found, not how you looked.
- **So what.** Point at any beat and ask it. A beat that answers only "this is also true" goes.
- **The recommendation opens on a verb** and names who acts.

**Tests.** Does every heading assert rather than label? Do the headings alone carry the argument?
Does every number sit in a main clause?

---

## E. Essay

**Pick this when** the piece must be read straight through by a smart non-specialist, and the
pleasure of reading it is part of the point.

- **No throat-clearing.** The first fact is in the first sentence. Cut every sentence that sets a
  scene before the piece begins.
- **Every sentence would be missed.** Remove one; if nothing is lost, it was not a sentence. Run it
  over the whole piece before calling it done.
- **Active, and name the actor.**
- **Short, ordinary words**: over/met betrekking tot, na/na afloop van, maar/echter,
  genoeg/toereikend, laten zien/aantonen, gebruiken/aanwenden, nu/op dit moment.
- **Cut the intensifier**: zeer, heel, uiterst, aanzienlijk, nadrukkelijk, duidelijk, echt.
  Adjectives may make a meaning more precise, never more emphatic.
- **A paragraph is a unit of thought.** One margin note per paragraph; two notes, two paragraphs.
- **Vary sentence length sharply** — a 30-word sentence beside a 4-word one.
- **The colon as hinge**, replacing "Dit komt doordat…" and "Dit betekent dat…".
- **Let the analysis deliver the verdict.** Not dusty, not preachy, not pleased with itself.

**Tests.** Can any sentence be cut without loss? Is there an intensifier left? Do two adjacent
sentences have the same length and shape?

---

## V. Verhaal — the narrative

**Pick this when** the piece has to be felt: a case story, a portrait, a project page that carries
a person or a place.

- **The opening is a torch, not an introduction.** Begin in something concrete and small. The *nut
  graf* — one paragraph saying what this is about and why you keep reading — lands second to fifth.
- **Climb the ladder of abstraction.** Names, amounts, dates and actions at the bottom; meaning at
  the top; alternate. Two consecutive beats with nothing concrete is the failure.
- **Ban the bureaucratic middle** — too vague to picture, too concrete to move. Can you draw the
  sentence or check its arithmetic? Neither means rewrite it downward or upward.
- **Subject and verb early**, the rest fanning right. Strong words at the start and the end.
- **Gold coins in the middle** — a scene, a quote, a detail where attention normally sags.
- **One structural decision**, chronology or theme, made out loud and held.
- **The ending does not summarise.** It surprises slightly and still feels right.

**Tests.** Does each beat carry one concrete element? Can you picture or check every sentence? Does
the close summarise?

---

## K. Kort — the factual brief

**Pick this when** the reader wants the case and nothing else: a memo, a one-pager, a mail, a note.
The neutral default when the piece is not obviously SFNL work.

- **Apex in the heading**, and the first sentence carries a fact, not a frame.
- **One move per beat**, and the beat stops when the move is done.
- **No ornament.** No em-dash asides, no rule of three, no "niet alleen X maar ook Y", no generic
  uplift at the end.
- **Name the gap once** where the reader would otherwise infer something the pile does not support.
- **Signed close**, explicit: a judgment in the author's own voice.
- **Shorter than the material suggests.** On a rewrite-shaped job, 15 to 25 per cent under.

**Tests.** Does any sentence open with a numeral or carry more than three numbers? Is there an
ornament that survives cutting? Is the close a judgment rather than a summary?

---

## Text type and audience decide the starting point

Purpose and reader are settled at intake, and they propose the preset and the knob deltas. This
table is the proposal; the user overrules it in the widget. Deltas are written as knob:value.

| Text type | Preset | Knob deltas |
|---|---|---|
| Rapporthoofdstuk | H | — |
| Casusspread, casusbeschrijving | H | `oordeel:aanbeveling` `bewijs:factbox` |
| Bestuurlijke samenvatting | Bd | `bewijs:lijsten` `ritme:vlak` |
| Projectpagina, website | V | `kop:bewering` `apex:eerste-alinea` `vet:uit` |
| Tender, inschrijftekst | Bd | `woorden:vak-bekend` `apex:kop` `beeldspraak:0` |
| Notitie, mail, memo | K | `kop:geen` |
| Opiniestuk, blog | E | `oordeel:ondertekend` |
| Pitch, one-pager | Bd | `ritme:hoog` `beeldspraak:1` |
| Nieuwsbrief, LinkedIn | V | `woorden:alledaags` `ritme:hoog` |

Audience shifts the same three knobs, and little else: a specialist reader takes
`woorden:vak-bekend`, a mixed or public reader takes `woorden:alledaags` and often
`beeldspraak:2`, a reader who has to decide takes `oordeel:aanbeveling` whatever the preset.

---

## R. Reference text — derive the register

**Pick this when** the user attaches a piece of writing and wants the article to sound like it: an
earlier report of their own, a colleague's chapter, something they admire.

Read it in full, then **measure before you describe.** Impressions of a voice are worthless; counts
are reproducible. Work through the eleven knobs first — they are a measuring instrument as much as
a control panel — and write down where the reference sits on each. Then add what the knobs do not
capture:

1. **Sentence length** — mean, shortest, longest, and whether length actually varies.
2. **Paragraphs** — sentences per paragraph, and whether the first summarises the rest.
3. **Openings and closings** — what move the first sentence makes, what the last one does.
4. **Signature devices** — the recurring constructions, up to three, each with a count.
5. **What it never does** — the moves conspicuously absent.

Then write the card into the sidecar: the eleven knob values, four to six rules the knobs cannot
express, three yes/no tests, and a budget on the two most frequent devices at the sample's own rate
per 500 words. Show it to the user before beat 1 — a derived card is a reading of their text, and
they are the one who can say it is wrong.

**Three guardrails.**

- **Structure and voice, never content.** Phrases, examples, framings and facts from the reference
  stay in the reference.
- **Thin samples give thin cards.** Under roughly 300 words, say so, name the preset the reference
  sits closest to, and run that preset with the two or three derived rules laid over it.
- **Do not copy the weaknesses.** Name what you are refusing to reproduce, the way H refuses three
  things its own source reports do.

**Tests.** Are the rules numbers rather than impressions? Would the author recognise their own text
in the card? Is anything on it a fact or phrase rather than a technique?

---

## S. Supermodus — all of them, then one

**Pick this when** the register is genuinely undecided, or the piece matters enough to be worth
several times the writing. Not a register: a procedure that ends in one.

1. **One rendering per preset — H, Bd, E, V, K, plus R when a reference was attached** — of the same
   apex and the same committed claims. Same facts, five or six different pieces of writing, not
   paraphrases. Dropping a preset is allowed when it is plainly wrong for the piece; say which and
   why, and never run fewer than three.
2. **Say what each one won.** One line per version, naming the move, not the vibe.
3. **Pick a spine.** One preset carries the structure of the final version. A version that averages
   the presets reads like none of them.
4. **Graft, and name each graft.** Anything you cannot point at is not a graft, it is drift.
5. **Resolve the conflicts explicitly.** H, Bd and K put the answer in the heading; V withholds it.
   E lets the analysis deliver the verdict; the others state it. H sends result figures to a list;
   Bd wants them in the assertion.

Only the final version goes into the article file; the renderings go in the sidecar so a later beat
can graft from one the user liked. **In cadence W or O** run it on the whole article at once. **In
S or P** run it on the opening section only, then lock the spine.

**Tests.** Can you name what each rendering won? Does the final version have one spine rather than
an average? Is every graft traceable to a version?

---

## Where a preset overrides the base rules

- **The signed close** is required everywhere; the `oordeel` knob decides how loud it is.
- **The number rules** (three per sentence, no numeral-initial) hold in every preset. `cijfers`
  only tightens them.
- **Length discipline** is K's default; elsewhere the intake target wins.
- **The humanizer pass** (`HUMANIZE.md`) runs in every preset and cadence, per unit and once over
  the finished text. Where it collides with a preset, the preset wins only on the devices it names
  and budgets — H's capitalised headings and conditional inversion, E's colon hinge, V's withheld
  opening — and everywhere else the pass wins.

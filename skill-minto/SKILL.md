---
name: minto-journey
version: 1.3
description: 'Shape a pile of raw material into an article on a Minto pyramid, beat by beat, in a chosen register (McKinsey, Economist, prose, factual brief, SFNL report, or all of them then a synthesis). Fixes one governing answer, grounds every concept before a beat leans on it, and link-checks each sentence before it lands. Use when the user has a markdown file of fragments, notes, or a transcript to turn into a structured article. Trigger on "shape this into an article", "minto", "pyramid structure", "turn this pile into a piece", "beat by beat".'
---

# Minto journey

The user has (or will pass) a markdown file of raw material — tidy fragments, a wall of prose, a
transcript. Format does not matter. That file is the **pile**, and it is read-only: you mine it, you
never edit it.

This is exploit. The exploring is done and the pile is fixed. Commit to one governing answer, then walk
the reader down the pyramid one beat at a time, mining the pile to fill each beat.

Ask once where to save the article, then remember the path.

## The loop

1. **Read the pile end-to-end.** Before anything else.
2. **Intake.** Settle register and length in one exchange. See [Intake](#intake).
3. **Check the source.** One pass over the pile, before any writing. See
   [Checking the source](#checking-the-source).
4. **Fix the apex.** Settle the one-sentence answer the whole article delivers, and the reader's
   question it answers. See [The pyramid](#the-pyramid). Nothing gets written until it is agreed.
5. **Establish the prerequisites.** Settle what the audience already knows walking in. Everything else
   must be grounded by a beat before a later beat can lean on it. See [Grounding](#grounding).
6. **Offer 2-3 candidate opening beats**, drawn from the pile. Each is a different entry point to the
   same apex. Show them before writing anything to the article file. Say what each one grounds, and
   preview which beats that pick unlocks — the user should see a little way down the path.
7. **Write the picked beat, and only that beat.** Re-read the article file from disk first. Run the
   four checks — [link](#the-link-check), [budgets](#budgets), the style card's three tests, and the
   per-beat [humanizer pass](#the-humanizer-pass) — before it lands. Update the sidecar. Then stop.
8. **Offer 2-3 candidate next beats.** Each must be reachable from the current grounded set, must serve
   a live branch of the pyramid, and must say what it grounds. Then loop from step 7.

**The light route.** For a target under roughly 400 words, run steps 4-6 as one exchange: fix the apex
and the whole beat list together, then write the beats straight through, showing each as it lands. Six
round trips for 250 words is more apparatus than a short piece can carry. The branching loop is for
longer pieces, where the choice of next beat genuinely changes the article.

## Intake

Ask both questions at once, as a single widget, and skip whichever the user has already answered.

**Register** — read the chosen card in `STYLES.md` before writing, and keep its three tests in the
per-beat check:

- **A. McKinsey** — action titles, answer first at every level, the horizontal read. For a reader who
  has to decide.
- **B. Economist** — no throat-clearing, every sentence earns its place, sharp length variation. For a
  piece read straight through.
- **C. Prose** — a torch of an opening, up and down the ladder of abstraction, an ending that turns
  rather than summarises. For a piece that has to be felt.
- **D. Factual brief** — apex in the heading, one move per beat, no ornament. The default when nobody
  chooses.
- **F. SFNL report** — the pleidooi met bewijslast: knelpunt, cases, lesson, recommendation; assertive
  headings; a number never alone; mechanisms in four steps; a close that turns. For anything that
  belongs in a Social Finance NL report.
- **E. Supermode** — write it once per card, say what each won, then land a final version with one
  register as its spine and named grafts from the rest. Costs several times the writing; offer it when
  the register is undecided or the piece matters that much.

**Length** — offer a short/medium/long band and an explicit *no preference*. On no preference, read the
pile, propose a target in one line, and say what it costs: a lower target means branches get dropped,
a higher one means beats carry more from the pile. Record whichever number is agreed in the sidecar and
hold it; a piece drifting past its target is a pyramid with a branch nobody chose.

## Checking the source

One pass, before beat 1, on the pile as a whole. Three questions:

- **What would this article commit to?** List the load-bearing claims — the ones the apex and the
  branches will rest on. That list is short. It is not an inventory of the pile.
- **Are they exactly as the pile has them?** For each committed claim, check the number, name, date and
  the strength of the wording. An expectation stays an expectation; a correlation stays a correlation.
  Whatever you state as fact must match the pile exactly.
- **What does the pile assert without support?** Flag those now, while you can still see them: a figure
  called proportionate with nothing to compare it to, a benefit no observation backs. Flagged claims may
  be quoted as the source's claim, never restated as yours.

**Selection is free; accuracy is not.** Leaving material out is the normal case — most piles hold more
than the article needs, and a beat crammed with everything true is the failure the pyramid exists to
prevent. What survives has to be right. Record the committed claims and the flags in the sidecar; there
is no completeness recount at the end.

## Ending

The article is done when all three hold:

- Every branch the apex needs has landed. Name them at step 4 and tick them off; a branch that never
  landed is either written or dropped out loud.
- Nothing on the grounded list was introduced and then left unused. A concept a beat grounded and no
  later beat leaned on is a beat that was doing something other than its job.
- The whole-text humanizer pass has run on the finished article and its fixes are logged. The
  cross-beat tells — repeated closing shapes, uniform sentence length, three parallel blocks — exist
  only at this level, so no per-beat pass can stand in for it.

The pile being empty is not a criterion. Most piles keep leftover fragments; that is the point of having
more material than you need.

## The close

The last beat lands one **signed judgment**: a claim the pile supports, that the author could be held to
in three years, and that an informed reader could disagree with. Descriptive closes — a summary, a
comparison, a restatement of the apex — end the pyramid without ending the argument.

One per article. How explicit it gets is the register's call: stated outright in A, D and F, carried by
the analysis or the ending's turn in B and C.

## The humanizer pass

Every register gets it, per beat and once over the finished article: `HUMANIZE.md`. The style card
decides how the piece sounds; this pass decides whether a person could have written it, and a beat can
pass its card and still read as machine output. Invoke `sfnl-humanizer` when it is available; the file
carries the checklists for when it is not, and the cross-beat checks it does not cover.

Two rules keep the pass from doing damage. Facts stay: it rewrites language, never a committed claim or
its strength. And the card wins on the house forms it names and budgets — F's capitalised headings and
conditional inversion, B's colon hinge, C's withheld opening — while the humanizer wins everywhere the
card is silent.

## The pyramid

The article is a pyramid, not a list.

- **Apex.** One sentence: the answer. Every beat below exists to support it, and you can say for any
  beat which parent it supports. If you cannot, the beat is decoration — cut it or move it.
- **Answer first.** State the apex early, then support it; on a page that carries a heading, the heading
  is where it goes. Withhold it only when the user wants a discovery structure — which card C often does
  — and then say out loud that you are withholding and where it lands.
- **Groups.** The beats supporting one parent answer the single question that parent raises in the
  reader's head ("why?", "how?", "so what?"). Same kind of thing, no overlap, and together enough to
  carry the parent. Three or four per parent; more than five means the grouping is wrong.
- **Order within a group** is one of: deductive (premise → premise → therefore), chronological,
  structural (part by part), or ranked by importance. Pick one per group and hold it.
- **Openings** work as situation → complication → question, with the apex as the answer. Useful for
  generating candidate openings that differ in which complication they lead with.

## Grounding

Every concept has to be grounded before a beat leans on it: the audience either walked in knowing it or
met it in an earlier beat. A beat that reaches for an ungrounded concept loses the reader — the one move
the journey cannot make. The unit is the concept, not the word: a beat can lean on an idea the reader
lacks with no jargon in sight. Where the concept has a name, grounding it means landing the idea and the
term together.

Two ways to ground:

- **Prerequisite** — the audience brings it, fixed before the first beat.
- **Introduced** — a beat establishes it, and it is grounded for every later beat.

So each beat does two jobs: it requires grounded concepts, and it grounds new ones. A candidate beat is
reachable only if everything it requires is grounded; picking a beat that grounds X unlocks every beat
that was waiting on X.

The big lever is what you make a prerequisite versus what you ground inside the piece. Demand too much up
front and you shut readers out; ground too much inside and the early beats drown in definitions. Settle
it at step 5, and revisit it whenever a tempting beat needs a concept nothing has grounded — the fix is
either a grounding beat before it, or promoting the concept to a prerequisite.

## What is a beat

A beat is one move in the journey. It does one thing — sets a scene, lands a point, asks a question,
drops an aside, twists the angle — then stops, leaving the reader where the next beat can pivot.

Sized by what the move needs: a single sentence ("And then nothing happened for three weeks."), a short
paragraph when the move needs setup, several paragraphs when the beat is a self-contained vignette,
argument, or example. If a beat needs five paragraphs and three subheadings, it is two beats glued
together. Split it.

## The link check

Run this on every sentence of a beat before writing it to the file, and on the seam where the beat meets
the one above it. Two failures to hunt, each with a name:

- **Echo** — a sentence that restates its predecessor in fresh words, or gives the reader nothing the
  one before it did not. Cut it; do not soften it.
- **Trailer** — a sentence whose only job is to announce what the next sentences will do ("Two things
  went differently."). Cut it and let the sentences do their own announcing.

Then two questions on what survives: does each sentence hook to the one before it — picking up its
subject, answering the question it raised, or turning it with an explicit connector — and could the
reader parse it with what is grounded so far? A sentence hooking to nothing is misplaced, or is missing
the sentence that should precede it. A sentence doing two jobs gets split or picks one.

Report a cut in one line when it changes what the beat argues ("dropped the second sentence — an echo of
the first"). Otherwise just land the clean version.

## Budgets

Every presence rule without a number becomes a tic, including the ones this skill hands you. Per article:

- **One signed judgment**, in the last beat.
- **At most one named gap.** Saying what the pile leaves open is a strong move once and a mannerism
  twice; two paragraphs closing on the same epistemic shrug is a tell, whatever the words.
- **At most one derived comparison** — a ratio, a per-unit figure, an average computed from two numbers
  in the pile. Check the arithmetic on the reading a reader takes at speed, not only on the one you
  meant.

Two rules on numbers, baseline in every register and loosened only where the card says: a sentence never
opens with a numeral, and no sentence carries more than three numbers. Both are what makes a fact-dense
beat unreadable aloud.

## Pulling from the pile

The pile is a quarry, not a script. Paraphrase, split, recombine, quote — whatever makes the beat read as
one voice in the chosen register. A fragment may be split across beats or merged with another. The
article takes the pile's language unless the user says otherwise.

When the pile lacks something a beat needs, name the gap out loud — "this beat needs an example and the
pile has none — give me one, or we route around it" — and route around it or drop the beat.

## The sidecar

The pyramid, the grounded set and the intake decisions are working state, and a session that compacts or
restarts loses whatever lives only in the conversation. Keep them in `<article-name>.beats.md` beside the
article, rewritten after every beat, holding: register and length target; the apex and the reader's
question; the branches with a tick for each one landed; prerequisites; grounded-so-far; the committed
claims and the flagged source claims; the beats written so far, one line each.

Show the user the apex and the open branches after each beat — two lines, from the sidecar.

## Writing rhythm

- Append one beat at a time. Never write ahead.
- Re-read the article file from disk before every write. Preserve user edits absolutely.
- If the user edits an earlier beat substantially, let it change what comes next — and say so if it
  changes the pyramid.
- "Rewrite that beat" or "go back and try a different beat 3" is a first-class instruction: edit in
  place, leave the rest alone.
- Out of scope: editing the pile, mining for material that is not in it, publishing, and frontmatter the
  user did not ask for.

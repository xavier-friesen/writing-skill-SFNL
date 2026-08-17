---
name: minto-journey
version: 1.0
description: 'Shape a pile of raw writing material into an article with a Minto pyramid spine, one beat at a time, choose-your-own-adventure style. Fixes a single governing answer up front, offers 2-3 candidate next beats at every step, and runs a link check on each sentence before it lands. Use when the user has a markdown file of fragments, notes, or a transcript and wants it turned into a structured article. Trigger on "shape this into an article", "minto", "pyramid structure", "structure my notes", "turn this pile into a piece", "beat by beat".'
---

# Minto journey

The user has (or will pass) a markdown file of raw material — tidy fragments, a wall of prose, a
transcript. Format does not matter. That file is the **pile**, and it is read-only: you mine it, you
never edit it.

This is exploit. The exploring is done and the pile is fixed. Commit to one governing answer, then walk
the reader down the pyramid one beat at a time, mining the pile to fill each beat.

Ask once where to save the article, then remember the path for the rest of the session.

## The loop

1. **Read the pile end-to-end.** Before anything else.
2. **Fix the apex.** Settle the one-sentence answer the whole article delivers, and the reader's
   question it answers. See [The pyramid](#the-pyramid). Everything below hangs off this; nothing gets
   written until it is agreed.
3. **Establish the prerequisites.** Settle what the audience already knows walking in. Everything else
   must be grounded by a beat before a later beat can lean on it. See [Grounding](#grounding).
4. **Offer 2-3 candidate opening beats**, drawn from the pile. Each is a different entry point to the
   same apex. Show them before writing anything to the article file. Say what each one grounds, and
   preview which beats that pick unlocks — the user should see a little way down the path.
5. **Write the picked beat, and only that beat.** Re-read the article file from disk first. Run the
   [link check](#the-link-check) on its sentences before it lands. Then stop.
6. **Offer 2-3 candidate next beats.** Each must be reachable from the current grounded set, must serve
   a live branch of the pyramid, and must say what it grounds. Then loop from step 5.

The article ends when the journey is complete, not when the pile is empty. Leftover fragments are the
point of having more material than you need.

## The pyramid

The article is a pyramid, not a list.

- **Apex.** One sentence: the answer. Every beat below exists to support it, and you can say for any
  beat which parent it supports. If you cannot, the beat is decoration — cut it or move it.
- **Answer first.** State the apex early, then support it. Withhold it only when the user deliberately
  wants a discovery structure, and then say out loud that you are withholding and where it lands.
- **Groups.** The beats supporting one parent answer the single question that parent raises in the
  reader's head ("why?", "how?", "so what?"). Same kind of thing, no overlap, and together enough to
  carry the parent. Three or four per parent; more than five means the grouping is wrong.
- **Order within a group** is one of: deductive (premise → premise → therefore), chronological,
  structural (part by part), or ranked by importance. Pick one per group and hold it.
- **Openings** work as situation → complication → question, with the apex as the answer. Useful for
  generating candidate openings that differ in what complication they lead with.

Keep the pyramid visible: after each beat, show the user a two-line sketch of where the article now
stands and which branch is still open.

## Grounding

Every concept has to be grounded before a beat leans on it: the audience either walked in knowing it or
met it in an earlier beat. A beat that reaches for an ungrounded concept loses the reader — the one move
the journey cannot make. The unit is the concept, not the word: a beat can lean on an idea the reader
lacks with no jargon in sight. Where the concept has a name, grounding it means landing the idea and the
term together.

Two ways to ground:

- **Prerequisite** — the audience brings it, fixed before the first beat.
- **Introduced** — a beat establishes it, and it is grounded for every later beat.

So each beat does two jobs: it requires grounded concepts, and it grounds new ones. Keep a running list
and update it every time a beat lands. A candidate beat is reachable only if everything it requires is
grounded; picking a beat that grounds X unlocks every beat that was waiting on X.

The big lever is what you make a prerequisite versus what you ground inside the piece. Demand too much up
front and you shut readers out; ground too much inside and the early beats drown in definitions. Settle
it at step 3, and revisit it whenever a tempting beat needs a concept nothing has grounded — the fix is
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
the one above it. Two questions per sentence:

- **Does it add?** What does this sentence give the reader that the previous one did not? A sentence
  that restates its predecessor in fresh words is cut, not softened. So is one whose only job is to
  announce what the next sentence will do.
- **Does it link?** How does it hook to the previous sentence — it picks up that sentence's subject,
  answers the question it raised, or turns it with an explicit connector? A sentence that hooks to
  nothing is either misplaced or is missing the sentence that should precede it.

Two more, cheap to run in the same pass: a sentence doing two jobs gets split or picks one, and a
sentence the reader could not have parsed with what is grounded so far does not go in at all.

Report failures in one line rather than silently fixing them when the fix changes what the beat argues
("cut the second sentence — it restated the first"). Otherwise just land the clean version.

## Pulling from the pile

The pile is a quarry, not a script. Paraphrase, split, recombine, quote — whatever makes the beat read as
one voice. A fragment may be split across beats or merged with another.

When the pile lacks something a beat needs, name the gap out loud: "this beat needs an example and the
pile has none — give me one, or we route around it." Do not invent facts, numbers, or anecdotes to fill
it.

## Writing rhythm

- Append one beat at a time. Never write ahead.
- Re-read the article file from disk before every write. Preserve user edits absolutely.
- If the user edits an earlier beat substantially, let it change what comes next — and say so if it
  changes the pyramid.
- "Rewrite that beat" or "go back and try a different beat 3" is a first-class instruction: edit in
  place, leave the rest alone.
- Out of scope: editing the pile, mining for material that is not in it, publishing, and frontmatter the
  user did not ask for.

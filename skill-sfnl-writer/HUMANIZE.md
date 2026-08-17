# The humanizer pass

Every preset gets it. A preset decides how the piece sounds; this pass decides whether it
sounds like a person wrote it. They are different jobs, and a beat can pass its card and still
read as machine output.

**The checklists below are the pass** and need nothing outside this folder. If the separate
`sfnl-humanizer` skill happens to be installed, run it as well and treat its verdict as the
stricter one on the per-beat list — it is maintained independently. The whole-text checks are
this file's alone either way.

## Two moments

**Per beat, before it lands.** Local, fast, on the sentences you just wrote:

1. One concrete element per paragraph — a number, name, date, amount, place — that is not
   general knowledge.
2. No meta-commentary: "in dit hoofdstuk", "zoals eerder genoemd", "samenvattend".
3. No em-dash as a loose aside mid-sentence, no bold for emphasis in running text.
4. No hedge that is not a real uncertainty: "het is belangrijk op te merken", "over het
   algemeen", "in zekere zin".
5. None of the flag words: cruciaal, essentieel, faciliteren, navigeren, landschap
   (metaphorical), robuust, naadloos, baanbrekend, toekomstbestendig, inzichten bieden, waarde
   toevoegen, impact maken, holistisch, borgen, ontzorgen, meenemen in.
6. Nominalisations (-ing, -atie, -heid) under five per hundred words.
7. The same thing keeps the same word. Synonym-hunting is a tell, not variety.
8. One word per paragraph that is both surprising and exact.

**Whole text, before the article is done.** These only become visible across beats, which is
exactly why a per-beat pass misses them:

1. Sentence-length range: in every ten sentences, one under eight words and one over thirty.
2. At most two negative parallels in the whole piece ("niet alleen … maar ook", "niet X maar Y").
3. At most two rules of three in the whole piece.
4. No two beats closing on the same grammatical shape — the repeated epistemic shrug, the
   repeated rhetorical question, the repeated one-line verdict.
5. Sections differ in length in proportion to their weight; no three parallel blocks of equal
   size.
6. No trailing "uitdagingen en vooruitblik" paragraph.
7. At least one counter-argument, cost, or own mistake named somewhere.
8. One sentence in the piece the author could only have written with the file open.
9. Read it aloud end to end. Nothing stumbles, and it sounds like someone who knows the subject
   rather than a spokesperson.

## What the pass may not do

- **Facts stay.** The pass rewrites language. It never adds, drops or alters a committed claim,
  and it never softens or strengthens the wording of one.
- **The preset wins on its own house forms.** Where a preset names and budgets a device, that
  device survives this pass: SFNL's conditional inversion and its single niet-X-maar-Y, the essay's
  colon hinge, the reportage's withheld opening, the bulletnotitie's lists. The humanizer wins everywhere the
  preset is silent.
- **No echo, no trailer.** A rewrite that re-adds a restatement or an announcement sentence has
  failed the link check, whatever it did for the rhythm.
- **Log what changed** in one line per fix, in the sidecar. A pass with nothing to report is
  suspicious: check the sentence-length range and the closing shapes before you accept it.

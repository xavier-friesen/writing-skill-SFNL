# Intake

Four things to settle before beat 1: **reference**, **register**, **cadence**, **length**. All of
it happens in the chat, in one exchange. Skip anything the user has already decided in
conversation, and never ask again for something they have said.

## One question block, in chat

Ask register, cadence and length together in a single `AskUserQuestion` call — three questions,
four options each, one screen. Not three messages in a row: an intake that costs three exchanges
has already cost more than it saves.

**Question 1 — Register.** Four options fit; there are seven registers. Show the four that fit
this piece, recommended one first, and name the rest in the question text so the user can type one
into "Other": *"Register? A (McKinsey) en E (supermodus) kun je als eigen antwoord typen."*

- Lead with **F — SFNL-rapport** whenever the piece is Social Finance NL work, otherwise with
  **D — feitelijk kort**.
- When a reference document has been attached, **R — zoals mijn referentietekst** takes the first
  slot instead.
- Fill the remaining slots from B (Economist), C (proza), and whichever of D/F is not leading.
- Each option gets a one-line description of what it buys, not what it is called.

**Question 2 — Cadans.** All four fit: O (outline eerst), S (sectie voor sectie), P (alinea voor
alinea), W (in één keer). Lead with the default for the length in question, and put the cost in
the description — turns against control.

**Question 3 — Lengte.** Kort (~300 woorden), middel (~800), lang (~1500 en meer), geen voorkeur.
Anyone with an exact number types it. On *geen voorkeur*, read the pile, propose a number in one
line, and say what it costs: lower means branches get dropped, higher means beats carry more from
the pile.

**A fourth question, only when it is live:** if two documents have arrived and it is unclear which
is which, ask which one is the reference. Otherwise leave it out.

## The reference document

The user attaches it in the chat, like any other file. Never ask for a path, and never ask them to
put it somewhere first.

Two documents can arrive, and they do different jobs, so keep them apart:

- **The pile** is the content. Everything the article states comes from here.
- **The reference** is the style. Its facts, phrases and examples never enter the article, even
  when it covers the same subject.

Default reading: the first document is the pile. A second one, or one introduced with something
like "in deze stijl" or "zoals dit stuk", is the reference. When that is genuinely unclear, ask —
one question, in the same block as the rest.

A reference makes register **R** available: measure the text, write the card, show it, then write
to it (`STYLES.md`). A reference alongside some other register means the user wants that register
with the reference as a tiebreaker; say so out loud, and use the reference only where the card is
silent.

## Defaults

Nobody has to choose anything. Register defaults to **D**, or **F** for obvious SFNL work. Cadence
defaults by target length:

| Target | Default cadence |
|---|---|
| under 400 words | **W** write at once |
| 400 to 1,200 | **O** outline first |
| 1,200 to 3,000 | **S** section by section |
| over 3,000, or a contested argument at any length | **S**, offering **P** |

If the user declines the block, or answers only part of it, state the defaults you are taking in
one line and start writing. Record all four decisions in the sidecar.

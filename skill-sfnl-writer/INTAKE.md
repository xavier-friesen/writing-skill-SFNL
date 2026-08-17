# Intake

Four things to settle before beat 1: **reference**, **register**, **cadence**, **length**. One
widget, rendered in the chat, one exchange. Skip anything the user has already decided in
conversation, and never ask again for something they have said.

## Render the widget inline

`INTAKE-WIDGET.html` ships with this skill. Render it **in the conversation** — send it with the
file tool set to render, so it opens as a page the user can click, not as a path they have to go
and find. Never tell them to open a file.

The widget carries all four decisions at once, with what each option costs:

- **Reference** — a checkbox: *I have attached a reference text*.
- **Register** — all seven, no shortlisting: F (SFNL-rapport), A (McKinsey), B (Economist),
  C (proza), D (feitelijk kort), R (as the reference text), E (supermode). This is why the widget
  beats a question block: seven options fit a page and do not fit four slots, and each one gets a
  line saying what it buys.
- **Cadence** — P (paragraph), S (section), O (outline first), W (write at once), each with its
  cost in turns against control.
- **Length** — a number, or *no preference*.

Everything is pre-selected at its default, so a user who agrees clicks copy and nothing else. The
widget emits one line:

```
INTAKE ref=<bijgevoegd|-> reg=<A|B|C|D|F|R|E> cad=<P|S|O|W> len=<number|->
```

Parse it and write all four values into the sidecar. `-` on length means propose a target in one
line and say what it costs; `-` on reference means register R is unavailable.

**If the widget does not render** in this surface, or the user would rather type: put the same
four decisions in one chat message as a short list with the defaults marked, and take a one-line
answer. Do not fall back to asking four questions in four messages.

## The reference document

The user attaches it in the chat, like any other file. Never ask for a path, and never ask them to
save it somewhere first.

Two documents can arrive, and they do different jobs, so keep them apart:

- **The pile** is the content. Everything the article states comes from here.
- **The reference** is the style. Its facts, phrases and examples never enter the article, even
  when it covers the same subject.

Default reading: the first document is the pile. A second one, or one introduced with something
like "in deze stijl" or "zoals dit stuk", is the reference. When that is genuinely unclear, ask in
one line while the widget is up.

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

If the user ignores the widget entirely, state the defaults you are taking in one line and start
writing. Record all four decisions, and the save path, in the sidecar.

# Intake

Four decisions, settled once, before beat 1: **reference**, **register**, **cadence**, **length**.
Skip any the user has already made in conversation, and never ask a question the answer to which
is already on the table.

Do not ask them as four chat questions in a row. Use the widget.

## The widget

`INTAKE-WIDGET.html` ships with this skill. Copy it next to the article file, open it for the
user (send it, or tell them the path), and let them fill it in. It renders the four decisions with
what each option costs, and produces one line to paste back:

```
INTAKE ref=<path or -> reg=<A|B|C|D|F|R|E> cad=<P|S|O|W> len=<number or ->
```

Parse that line and write the four values into the sidecar. `-` means no preference: on `len=-`
propose a target in one line and say what it costs; on `ref=-` there is no reference text and
register R is unavailable.

**When the widget is not practical** — a terminal-only session, a user who would rather type —
write the same four decisions as a checklist into `<article-name>.intake.md`, ask them to tick and
save, then read it back. Same four fields, same defaults, no HTML:

```markdown
- [ ] Referentietekst: <pad>            (leeg = geen)
- [ ] Register:  [ ] A McKinsey  [ ] B Economist  [ ] C proza  [ ] D feitelijk kort
                 [ ] F SFNL-rapport  [ ] R referentietekst  [ ] E supermodus
- [ ] Cadans:    [ ] P alinea  [ ] S sectie  [ ] O outline eerst  [ ] W in één keer
- [ ] Lengte: ____ woorden   [ ] geen voorkeur
```

Third fallback, if both are refused: ask register and cadence in one message, take D and the
length-appropriate cadence as defaults, and get on with it. An intake that costs three exchanges
has already cost more than it saves.

## Defaults

Nobody has to choose. Register defaults to **D**, or to **F** when the piece is plainly SFNL work.
Cadence defaults by target length:

| Target | Default cadence |
|---|---|
| under 400 words | **W** write at once |
| 400 to 1,200 | **O** outline first |
| 1,200 to 3,000 | **S** section by section |
| over 3,000, or a contested argument at any length | **S**, offering **P** |

State the default you took in one line and move on. A user who wants a different gear will say so.

## The reference file

When `ref=` names a file, read it in full before the source check, and derive card R from it as
`STYLES.md` describes. Two rules that matter more than they look:

- **The reference is a style source, not a pile.** Its facts, examples and phrases never enter the
  article. Only the pile supplies content.
- **A reference plus a register that is not R** means the user wants that register with the
  reference as a tiebreaker — say so out loud, and use the reference only where the card is
  silent.

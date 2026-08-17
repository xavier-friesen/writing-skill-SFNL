# Intake

Six things to settle before beat 1: **purpose**, **audience**, **reference**, **register**,
**cadence**, **length**. One widget, rendered in the chat, one exchange.

The first two are not questions — they are a **proposal**. Read the pile, decide what this text is
for and who reads it, fill your answer into the widget, and let the user correct it. Asking "wat is
je doel?" of someone who just handed you their material is a question you can answer yourself.

## Fill the widget, then render it inside this session

`INTAKE-WIDGET.html` is a template with placeholders. Copy it next to the article, substitute, and
render the copy **inside this Claude session** — send it with the file tool set to render so it opens
in the conversation itself. Never a path to open elsewhere, never a browser tab, never a hosted page:
the user fills it in where they already are and pastes the line back into the same chat.

| Placeholder | What you put there |
|---|---|
| `{{DOEL}}` | your reading of what this becomes: "casusspread voor het jaarrapport" |
| `{{DOELGROEP}}` | who reads it and what they must be able to do with it |
| `{{REF_CHECKED}}` | `checked` when a reference document has already been attached, else empty |
| `{{REG}}` | proposed style: `sfnl` `mckinsey` `economist` `reportage` `feitelijk` `referentie` `supermodus` |
| `{{CAD}}` | proposed cadence: `P` `S` `O` `W` |
| `{{LEN}}` | proposed target in words, or empty for no preference |
| `{{KNOBS_JSON}}` | the knob deltas you propose, as JSON: `{"bewijs":"kader"}` — `{}` for none |

Derive the proposal from purpose and audience with the table in `STYLES.md` ("Text type and
audience decide the starting point"). Say in one line why you proposed what you did; a proposal the
user cannot see the reasoning of is a decision taken away from them.

The widget does the rest. All seven styles are visible under their own names with what each buys, the
four working methods carry their cost in turns, and the fine-tuning panel holds the eleven knobs —
closed by default, each written as a plain question with its options as examples, inheriting from the
chosen style and colouring whatever the user moves. Switching style re-inherits every knob except the
ones they touched.

It emits one line, carrying only what differs from the preset:

```
INTAKE doel=casusspread_jaarrapport pub=fondsen_en_gemeenten ref=- stijl=sfnl werkwijze=S len=700 fijn=bewijs:kader,ritme:wisselend
```

Parse it, write all of it into the sidecar, and treat `fijn=` as overrides on top of the style's
defaults. `-` on length means propose a number and say what it costs; `-` on reference means R is
unavailable. Underscores in `doel=` and `pub=` are spaces.

**If the widget does not render** in this surface, or the user would rather type: put the same
decisions in one chat message as a short list with your proposal marked, and take a one-line answer.
Never four questions in four messages.

## The reference document

The user attaches it in the chat, like any other file. Never ask for a path.

Two documents can arrive, and they do different jobs:

- **The pile** is the content. Everything the article states comes from here.
- **The reference** is the style. Its facts, phrases and examples never enter the article, even
  when it covers the same subject.

Default reading: the first document is the pile. A second one, or one introduced with "in deze
stijl" or "zoals dit stuk", is the reference. When that is genuinely unclear, ask in one line while
the widget is up.

A reference makes the style **Als mijn referentietekst** available: measure the text against the eleven knobs, write the
card, show it, then write to it (`STYLES.md`). A reference alongside another register means the user
wants that register with the reference as a tiebreaker; say so, and use it only where the preset is
silent.

## Defaults

| | Default |
|---|---|
| Style | **SFNL-rapport** for SFNL work, **Feitelijke notitie** otherwise |
| Knobs | whatever the style says; deltas only from the text-type table or the user |
| Working method | by length: under 400 words **in één keer**, to 1,200 **outline eerst**, to 3,000 **sectie voor sectie**, above that section by section offering paragraph by paragraph |
| Length | your proposal, stated with what it costs |

If the user ignores the widget, state the proposal you are running with in one line and start
writing. Record everything, including the save path, in the sidecar.

## Changing your mind later

Any of it can move mid-article: "korter", "geen vet meer", "toch maar zonder kopjes", "dit leest te
technisch". Treat that as a knob change, not a complaint — name the knob you are moving and what it
does to the text from here, apply it to what comes next, and offer to sweep back over what is
already written. Record the change and the beat it took effect in the sidecar.

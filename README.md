# writing-skill-SFNL

De skill `sfnl-rapporttekst`: bouwt van een concepttekst een publiceerbare
Nederlandse rapporttekst voor Social Finance NL. Gebouwd en getest in blinde
juryrondes; het verhaal tot en met v3.2 staat in `dossier/eindverslag.md`.

## Installatie

```
cp -r skill ~/.claude/skills/sfnl-rapporttekst
```

De skill start met één vragenmoment (teksttype, premisse, lengte) en heeft
defaults voor onbeheerd draaien. Het telscript draait via Bash; de
koude-lezerstap gebruikt een subagent als die beschikbaar is en heeft anders
een solo-fallback.

## De architectuur van v4.0

Drie bestanden met een strikte taakverdeling. Alleen `SKILL.md` wordt bij het
triggeren geladen; de andere twee komen pas in de fase waarin ze nodig zijn.

| Bestand | Rol | Wanneer geladen |
|---|---|---|
| `SKILL.md` | het betoog: materiaal, premisse, tegenwerping, gezag, architectuur | bij triggeren |
| `stem.md` | de voice DNA: genre, cadans, lexicon, negentien bewegingen | fase C, schrijven |
| `hygiene.md` + `meetlat.py` | één hygiënepas: script, drie controles, koude lezer, levering | fase D |

## Waarom v4.0 anders is dan v3.2

v3.2 was aftrekkend: veertien verboden, vijf budgetten, vijfentwintig
metingen en zeven controles tegenover een halve pagina generatief materiaal.
Wie een model vijftien keer vertelt wat het moet vermijden en één keer wat het
moet doen, krijgt een tekst die dingen vermijdt. Het plafond daarvan is
"concept min fouten": correct, en klein.

Drie dingen zijn omgekeerd.

**De betooglaag staat vooraan en is echt een fase.** In v3.2 zat alles wat een
tekst radicaal anders maakt in één vraag ("welke spanning?") en een
hoofdboodschap van dertig woorden. Nu: drie materieel verschillende premissen
met de vraag wat de lezer moet opgeven als hij ze aanvaardt, de sterkste
intelligente tegenwerping in de woorden van de doellezer met een
antwoordrichting, het gezag uit eigen ervaring, en een keuze uit vier benoemde
architecturen. Die fase kost bijna geen tokens en beslist bijna alles.

**Breedte vervangt budgetten.** v3.1 zette quota op de eigen stijlmiddelen
omdat elk middel bij het derde gebruik als procedure ging lezen. Dat is een
symptoom van een te smal repertoire. `stem.md` bevat negentien bewegingen uit
gepubliceerd werk, elk hoogstens één keer per document — het antwoord op
"dezelfde drie bewegingen keren terug" is vijftien bewegingen, geen quotum van
twee.

**Hygiëne is één pas aan het eind.** Zeven controles werden drie. Twee nieuwe
metingen zijn erbij gekomen, en dat zijn precies de twee die het eigen corpus
faalt: **P1**, elke alinea van vier of meer zinnen heeft een zin onder de tien
woorden die de pointe draagt, en **N1**, getalconsistentie — in de rapporten
van 2025 staan de zorguitgaven op twee pagina's met een verschillende waarde.

**De waarheidsgrens staat expliciet.** Feiten zijn van de bron: geen getal,
naam, mechanisme, causaliteit of modaliteit die er niet staat. Het betoog is
van de schrijver: premisse, ordening, tegenwerping en oordeel draagt de skill
zelf aan, en verantwoordt ze in het logboek.

## Wat er in de repo staat

| Map | Inhoud |
|---|---|
| `skill/` | De skill (v4.0) |
| `varianten/v3.2/` | De vorige architectuur, als referentie |
| `varianten/V1..V5` | De vijf concurrerende ontwerpen uit ronde 1 |
| `test/corpus/` | Drie vaste AI-bot-testteksten met feitenlijsten |
| `test/rubriek.md` | Het blinde beoordelingskader (met addendum) |
| `test/rondes/r1..r5/` | Alle outputs en juryrapporten per ronde (v1 t/m v3.2) |
| `test/rondes/r6/` | De blinde A/B van v4.0 tegen de kampioenen van v3.2 |
| `dossier/onderzoek/` | Best-practices-onderzoek (8 dossiers) |
| `dossier/analyse-ronde*.md` | De analyse en het besluit per iteratie |
| `dossier/eindverslag.md` | Het eindverslag van het traject tot v3.2 |

## De kern in twee regels

Een zwakke tekst repareer je niet en poets je niet: je kiest een andere
stelling, beantwoordt het bezwaar dat de lezer werkelijk heeft, en schrijft
vers uit een gesloten dossier. Feiten zijn van de bron, het betoog is van jou.

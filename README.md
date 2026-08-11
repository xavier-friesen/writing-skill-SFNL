# writing-skill-SFNL

De skill `sfnl-rapporttekst`: zet AI-gegenereerde concepttekst om in complete,
publiceerbare Nederlandse rapporttekst voor Social Finance NL. Gebouwd en
getest in vijf blinde juryrondes; het volledige verhaal staat in
`dossier/eindverslag.md`.

## Installatie

```
cp -r skill ~/.claude/skills/sfnl-rapporttekst
```

De skill start met één vragenmoment (teksttype, lezer, invalshoek, register,
lengte) en heeft defaults voor onbeheerd draaien. Het ingebedde telscript
draait via Bash; de koude-lezerstap gebruikt een subagent als die beschikbaar
is en heeft anders een solo-fallback.

## Wat er in de repo staat

| Map | Inhoud |
|---|---|
| `skill/` | De definitieve skill (v3.2) |
| `varianten/` | De vijf concurrerende ontwerpen uit ronde 1 |
| `test/corpus/` | Drie vaste AI-bot-testteksten met feitenlijsten |
| `test/rubriek.md` | Het blinde beoordelingskader (met addendum) |
| `test/rondes/r1..r5/` | Alle outputs en juryrapporten per ronde |
| `dossier/onderzoek/` | Best-practices-onderzoek (8 dossiers) |
| `dossier/analyse-ronde*.md` | De analyse en het besluit per iteratie |
| `dossier/eindverslag.md` | Het eindverslag met de vijf wetten |

## De kern in twee regels

Een zwakke tekst repareer je niet, je schrijft hem opnieuw uit een gesloten
bron — met exacte feiten, een ondertekend en gegrond oordeel, en een budget
op elk stijlmiddel. Elke aanwezigheidsregel zonder budget wordt zelf een tic.

# writing-skill-SFNL

De skill `sfnl-rapporttekst`: bouwt van een concepttekst een publiceerbare
Nederlandse rapporttekst voor Social Finance NL. Gebouwd en getest in blinde
juryrondes; het verhaal tot en met v3.2 staat in `dossier/eindverslag.md`.

## Installatie

```
cp -r skill ~/.claude/skills/sfnl-rapporttekst
```

De skill start met één vragenmoment — welke kernbewering, plus teksttype en
lezer — en heeft defaults voor onbeheerd draaien. Het telscript is optioneel en
draait via Bash; de laatste leesstap gebruikt een subagent als die beschikbaar
is en heeft anders een solo-fallback.

## De architectuur van v5.0

Drie stappen, twee bestanden en een klein telscript. Alleen `SKILL.md` wordt bij
het triggeren geladen.

| | Rol |
|---|---|
| **Stap 1 — de kern** | vijf regels: kernbewering met wat de lezer opgeeft, het sterkste bezwaar met de antwoordrichting, het oordeel, het gat, en wat eruit gaat |
| **Stap 2 — de vorm** | één van vier architecturen, de beweringen in volgorde, en drie toetsen: en dus?, ongelijke gewichten, horizontaal lezen |
| **Stap 3 — het proza** | `stem.md`: de voice DNA — genre, gemeten cadans, lexicon, negentien bewegingen uit gepubliceerd werk |
| **De slotpas** | aanwijzen, tellen (`meetlat.py`), hardop lezen, en iemand anders laten lezen |

## Waarom v5.0 anders is dan wat eraan voorafging

**v3.2 was aftrekkend.** Veertien verboden, vijf budgetten, vijfentwintig
metingen en zeven controles tegenover een halve pagina generatief materiaal.
Wie een model vijftien keer vertelt wat het moet vermijden en één keer wat het
moet doen, krijgt een tekst die dingen vermijdt. Het plafond daarvan is
"concept min fouten": correct, en klein.

**v4.0 zette de betooglaag vooraan en ging te ver de andere kant op.** In een
blinde A/B tegen de best geteste v3.2-outputs verloor v4.0 op alle drie de
testteksten, met twee diskwalificaties op feiten. De oorzaken zaten in het
ontwerp: de instructie om het bezwaar "in de woorden van de doellezer" op te
schrijven leverde verzonnen personages met verzonnen motieven, de vroeg
vastgelegde premisse zette druk op de cijfers (een factor 1,6 die "bijna
verdubbeld" heette), en een breed repertoire zonder tellers gaf de tic van v3.1
terug. Daaruit volgde de wet die het traject nog niet had: **een betooglaag
zonder eigen feitenpoort verplaatst het verzinnen van de zin naar de premisse.**
Zie `dossier/analyse-ronde6.md`.

**v5.0 houdt de winst en gooit de machinerie weg.** De opdracht is een
bestaande tekst distilleren tot wat er werkelijk gezegd moet worden, dat in een
argumentvorm gieten, en het als proza opschrijven — niet een dossier bouwen. Het
volledige fase-A-apparaat (feitenlijst, claimregister, causaliteitskaart) is
vervangen door twee handelingen: streep in de bron de getallen en de
oorzaaksignalen aan, en wijs aan het eind elk feit terug aan. De reden dat het
dossier bestond — de bron sluiten om reparatie te voorkomen — staat nu als
regel: **je bewerkt geen bronzin, elke zin is nieuw geschreven.**

De drie lessen van ronde 6 blijven staan, maar als drie regels in plaats van als
fasen: geen opgevoerde spreker, geen bewering over het bewijs die de bron niet
doet, geen verhouding die naar het betoog toe buigt.

**Wat er per versie mee gebeurde:**

| | `SKILL.md` | bestanden | script | logboek |
|---|---|---|---|---|
| v3.2 | 755 regels | 1 | 96 regels, ingebed | 8 regels |
| v4.1 | 263 regels | 3 | 207 regels | 6 regels |
| v5.0 | 216 regels | 2 | 99 regels | 4 regels |

Twee metingen in het script bestonden in geen enkele eerdere versie, en het zijn
precies de twee die het eigen corpus faalt: **pointe** (elke alinea van vier of
meer zinnen heeft een zin onder de tien woorden die de pointe draagt — het slot
van hoofdstuk 4 in het rapport 2025 meet 23–25–35 en zakt weg) en **cijfers**
(twee waarden binnen één procent van elkaar zijn meestal dezelfde grootheid,
twee keer verschillend opgeschreven — de zorguitgaven 2024 staan op p. 9 en
p. 12 met een andere waarde).

## Welke versie je installeert

`skill/` bevat v6.0. Die versie repareert niet het volgende gat maar de
structurele fout die de vier eerdere gaten veroorzaakte, en de verificatie
daarvan loopt nog. Zolang die niet binnen is, is **`varianten/v3.2/`** de best
geteste versie voor werk dat de deur uit gaat.

De diagnose staat in `dossier/de-structurele-fout.md` en is in één regel samen te
vatten: de skill vroeg de schrijver zich eerst vast te leggen op een bewering die
op retorische kwaliteit was gekozen, en toetste pas daarna of het materiaal haar
droeg — door dezelfde schrijver, die er belang bij had dat zij overleefde. Elke
controle stond dus stroomafwaarts van het motief. v6.0 vervangt de controles door
een vorm: de kernbewering is een spanning tussen twee gegevens die beide in de
bron staan, opschrijfbaar als "X, terwijl Y". Daarmee is zij gedekt door
constructie, en zijn de vier eerdere defecten niet verboden maar onmogelijk.

## Wat er in de repo staat

| Map | Inhoud |
|---|---|
| `skill/` | De skill (v5.0) |
| `varianten/v3.2/` | De best geteste eerdere versie, als referentie |
| `varianten/v4.1/` | De betooglaag-architectuur die ronde 6 verloor |
| `varianten/V1..V5` | De vijf concurrerende ontwerpen uit ronde 1 |
| `test/corpus/` | Drie vaste AI-bot-testteksten met feitenlijsten |
| `test/rubriek.md` | Het blinde beoordelingskader (met addendum) |
| `test/rondes/r1..r5/` | Alle outputs en juryrapporten per ronde (v1 t/m v3.2) |
| `test/rondes/r6/` | De blinde A/B van v4.0 tegen de kampioenen van v3.2 |
| `test/rondes/r7/` | De verificatie van v5.0 (vervuilde set, zie de analyse) |
| `test/rondes/r7b/` | Dezelfde verificatie op een schone set |
| `dossier/onderzoek/` | Best-practices-onderzoek (8 dossiers) |
| `dossier/analyse-ronde*.md` | De analyse en het besluit per iteratie |
| `dossier/eindverslag.md` | Het eindverslag van het traject tot v3.2 |

## De kern in drie regels

Haal eruit wat de tekst werkelijk wil zeggen, zet dat in een vorm die bij de
lezer landt, en schrijf het opnieuw op — geen zin van de bron bewerkt. Feiten
zijn van de bron, het betoog is van jou. En de argumentlaag draagt dezelfde
dekkingsplicht als de tekst, want anders verhuist het verzinnen van de zin naar
de premisse.

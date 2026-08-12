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

`skill/` bevat v7.1, en dat is de eerste versie die de v3.2-kampioen verslaat:
**7,7 tegen 6,6** op T1 in ronde 10, tegen dezelfde kampioenoutput als in de
rondes 7b, 8 en 9. Voor werk op drie teksten blijft **`varianten/v3.2/`** de best
geteste versie — negen rondes op T1, T2 en T3 tegenover één gewonnen ronde op
alleen T1.

De maat die het meeste zegt is niet het verschil maar wat de uitdager zelf doet,
want A is vier rondes lang hetzelfde bestand geweest en scoorde daarop 7,5 · 7,3
· 6,9 · 6,6 — dat is 0,9 punt jury-ruis op één en dezelfde tekst. De uitdager
ging in diezelfde vier rondes 5,1 · 4,0 · 5,7 · **7,7**: een sprong van 2,0 punt
van v7.0 naar v7.1, ruim buiten die ruisband. Zie `dossier/analyse-ronde10.md`.

Wat v7.0 wél heeft opgelost is het waarheidsprobleem. Het is de eerste versie die
zonder feitendiskwalificatie en zonder causaliteitsplafond doorkomt, en het
verschil met de kampioen is teruggebracht van 2,4 en 3,3 punt naar 1,2 — bij een
juryspreiding van ongeveer een punt op dezelfde tekst, dus één meting en geen
trend. Wat er daarna nog verloor was afwerking: een sectie zonder onderstreepbare
zin, een lege topicsatzin, een bulletlijst die niet is omgeschreven.

**v7.1 pakt precies die drie aan, en niets anders.** Twee **poorten** komen terug
uit v3.2 (per sectie een doorstuurbare zin, per alinea een eigen punt); daarnaast
krijgt de sandbox drie hygiëneregels, omdat hij de waarheid dicht maar de vorm
laat lekken: wat je in bronwoorden op je lijst zet, staat straks in bronwoorden in
je tekst, en de volgorde van de lijst is de volgorde van de bron. Het telscript
krijgt twee metingen die de plek aanwijzen waar een poort meestal niet houdt —
`donorreeks` en `topicsat`, allebei stil op de r9-kampioen en allebei raak op de
twee zinnen die de jury in r9 met name noemde. Geen extra agents, geen extra
fasen: `SKILL.md` groeit van 285 naar 347 regels en blijft één bestand met drie
stappen. De geteste v7.0 staat als referentie in `varianten/v7.0/`.

Drie stukken dossier leggen uit hoe dat zo is gekomen:
`de-structurele-fout.md` (waarom vier patches op vier symptomen niets oplosten),
`analyse-ronde6.md` en `analyse-ronde8-9.md` (wat de twee mechanismen wel en niet
dekken). De les die het vaakst terugkomt: **een regel die een neiging bestrijdt
verliest van de neiging; een mechanisme dat haar onmogelijk maakt niet.** En de
waarschuwing die daarbij hoort: elke vereenvoudiging die in dit traject op v3.2
werd toegepast, haalde iets weg dat gewicht droeg — tweemaal aangetoond, en beide
keren pas na een verloren ronde.

## Wat er in de repo staat

| Map | Inhoud |
|---|---|
| `skill/` | De skill (v7.1) |
| `varianten/v3.2/` | De best geteste eerdere versie, als referentie |
| `varianten/v4.1/` | De betooglaag-architectuur die ronde 6 verloor |
| `varianten/v6.0/` | De vormeis zonder sandbox, die ronde 8 verloor |
| `varianten/v7.0/` | De versie die ronde 9 draaide, vóór de afwerkingslaag |
| `varianten/V1..V5` | De vijf concurrerende ontwerpen uit ronde 1 |
| `test/corpus/` | Drie vaste AI-bot-testteksten met feitenlijsten |
| `test/rubriek.md` | Het blinde beoordelingskader (met addendum) |
| `test/rondes/r1..r5/` | Alle outputs en juryrapporten per ronde (v1 t/m v3.2) |
| `test/rondes/r6/` | De blinde A/B van v4.0 tegen de kampioenen van v3.2 |
| `test/rondes/r7/` | De verificatie van v5.0 (vervuilde set, zie de analyse) |
| `test/rondes/r7b/` | Dezelfde verificatie op een schone set |
| `test/rondes/r8/` | v6.0: de vormeis alleen |
| `test/rondes/r9/` | v7.0: de vormeis plus de sandbox |
| `test/rondes/r10/` | v7.1: de afwerkingslaag — de eerste gewonnen ronde |
| `test/strip.sh` | De enige route naar een blinde set |
| `dossier/onderzoek/` | Best-practices-onderzoek (8 dossiers) |
| `dossier/analyse-ronde*.md` | De analyse en het besluit per iteratie |
| `dossier/eindverslag.md` | Het eindverslag van het traject tot v3.2 |

## De kern in drie regels

Haal eruit wat de tekst werkelijk wil zeggen, zet dat in een vorm die bij de
lezer landt, en schrijf het opnieuw op — geen zin van de bron bewerkt. Feiten
zijn van de bron, het betoog is van jou. En de argumentlaag draagt dezelfde
dekkingsplicht als de tekst, want anders verhuist het verzinnen van de zin naar
de premisse.

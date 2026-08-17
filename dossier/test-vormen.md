# Test: is de vormcatalogus compleet en werkt de nesting?

Vier tests op `skill-sfnl-writer/SHAPES.md`. De eerste toetst de nestingregel aan een echt
document, de tweede zoekt gaten, de derde probeert de catalogus te breken, de vierde loopt een
volledige compositie na.

---

## Test 1 — Nesting, geverifieerd aan het rapport van 2025

Als de regel "één toplaagvorm, secties met hun eigen vorm" klopt, moet een echt SFNL-rapport hem al
volgen zonder dat iemand hem heeft opgeschreven. Nagelopen in *Innovatieve financiering van
preventie* (48 p.):

| Niveau | Wat er staat | Vorm |
|---|---|---|
| Hoofdstuk 3 (p. 15) | "Partijen vinden investeren in preventie vaak onaantrekkelijk" → `HOE WERKT DIT KNELPUNT?` met drie oorzaken → drie casussen → conclusie | `knelpunt-casus-les` |
| Casus Kinzigtal (p. 16–17) | factbox, casebeschrijving, resultatenlijst, interview, `LES VOOR NEDERLAND` | `situatie-actie-resultaat` |
| Binnen die casus | "De kern van het model is een shared savings-contract: …" → geldstroom → conditionele inversie → gedrag | `werking`, ingebed |
| Managementsamenvatting (p. 4) | conclusie eerst, daarna aflopend detail, casussen als bewijs achteraan | `bluf` |
| Aanbevelingspagina (p. 41) | knelpunt → voorstel → hoe het werkt → wat het doorbreekt → vergezicht | eigen kleine `werking`-variant |
| Hoofdstuk 6 (p. 40–42) | "De voorgaande hoofdstukken tonen aan dat…" → waarom de omslag uitblijft → drie aanbevelingen | `claim-bewijs-tegenwerping`, zwak uitgevoerd |

**Uitkomst: de nestingregel klopt en is niet triviaal.** Vier verschillende vormen in één rapport,
twee niveaus diep, precies zoals regel 5 voorschrijft. Twee observaties die de regels bevestigen:

- De casussen zijn **parallel en gelijkvormig** (regel 4). Alle negen volgen dezelfde
  situatie-actie-resultaat met een `LES VOOR NEDERLAND` als sluitstuk. Dat is waarom je ze kunt
  vergelijken.
- Waar het rapport zwak is, is precies waar een vorm niet is volgehouden. De slotalinea van
  hoofdstuk 4 (de abstractiestapeling uit `sfnl-stem.md` §1.12) hoort in `claim-bewijs-tegenwerping`
  de tegenwerping te dragen, maar herhaalt de casussen zonder ze te wegen. Regel 2 — de vorm van een
  sectie moet haar taak dienen — vangt dat.

---

## Test 2 — Dekking: twaalf echte SFNL-producten

Voor elk product de vraag: bestaat er een passende vorm, en welke?

| Product | Toplaag | Secties |
|---|---|---|
| Rapporthoofdstuk met casussen | `knelpunt-casus-les` | casussen `situatie-actie-resultaat`, mechanisme `werking` |
| Managementsamenvatting | `bluf` | — |
| Casusspread, projectpagina | `situatie-actie-resultaat` of `zandloper` | mechanisme `werking` |
| Methodiekbeschrijving | `werking` | onderdelen `indeling` |
| Businesscase, doorrekening | `vraag-analyse-antwoord` | scenario's `vergelijking` |
| Evaluatie | `vraag-analyse-antwoord` | bevindingen `oorzaak-gevolg`, casussen `situatie-actie-resultaat` |
| Bestuurlijk keuzestuk | `opties` | per optie `vergelijking` |
| Tenderantwoord | `claim-bewijs-tegenwerping` | referenties `situatie-actie-resultaat` |
| Position paper, opiniestuk | `scqa` of `claim-bewijs-tegenwerping` | — |
| Voortgangsnotitie, stuurdocument | `stand-opvallend-nu` | risico's `oorzaak-gevolg` |
| Verslag van een sessie | `chronologisch` of `bluf` | besluiten `bluf` |
| Marktverkenning, landschapsanalyse | `indeling` | per categorie `vergelijking` |
| Nieuwsbrief, LinkedIn | `scene-nutgraf` | — |

**Uitkomst: geen gaten op dertien producten.** Drie ervan waren onmogelijk in de oude opzet, waar
`knelpunt → casussen → les` de enige SFNL-vorm was: de methodiekbeschrijving (geen casussen), de
doorrekening (geen knelpunt, een vraag) en het keuzestuk (geen les, een keuze). Dat was het gat
waar de vraag over ging, en het is dicht.

---

## Test 3 — Breektest: een verkeerde vorm forceren

T3 (Wijkkracht Molenhoek) in vier vormen gezet, alleen de eerste zinnen, om te zien of de catalogus
onderscheidend is of alleen etiketten plakt.

| Vorm | Eerste beweging | Wat er gebeurt |
|---|---|---|
| `situatie-actie-resultaat` | "In Molenhoek zijn armoede en schulden hardnekkig. Drie partijen legden € 1,9 miljoen in…" | werkt; dit is de vorm die de casus in `T3-minto-register-F.md` heeft |
| `zandloper` | "Sinds 2025 betaalt Havelsteijn de aanpak zelf. Daarvoor lag er een project van drie jaar…" | werkt; de v1.1-tekst is precies dit |
| `indeling` | "De aanpak kende drie componenten: schulden, werk en welzijn." | **breekt.** De componenten zijn niet de zaak; het onverwachte deel (elf buurtbudgetmaatjes) wordt één categorie van drie en verliest zijn gewicht |
| `oorzaak-gevolg` | "Doordat elf bewoners de eerste gesprekken voerden, daalden de huisuitzettingen." | **breekt, en gevaarlijk.** De pile legt dat verband niet. De vorm dwingt een causale claim af die het materiaal niet draagt |

**Uitkomst: de vormen zijn onderscheidend, en één ervan is riskant.** `oorzaak-gevolg` verzint
causaliteit zodra het materiaal die niet levert — dezelfde fout die de jury in ronde 5 afstrafte.
De faalregel bij die vorm in `SHAPES.md` ("het materiaal toont alleen samenhang; dan is deze vorm
een leugen") is naar aanleiding van deze test toegevoegd.

---

## Test 4 — Volledige compositie: T1, rapporthoofdstuk van 674 woorden

De bron is een hoofdstuk met vier subsecties (inleiding, context, structuur, resultaten, lessen).
Wat de skill ervan zou maken:

```
apex     Vroeg Verbonden liet de instroom dalen, maar de constructie eromheen is niet houdbaar
vorm     knelpunt-casus-les
  1  knelpunt: druk op de jeugdzorg, geld en tijd lopen niet gelijk      [bluf, 1 alinea]
  2  de constructie: wie betaalde wat, en wanneer geld terugvloeit       [werking]
  3  wat het opleverde in drie gemeenten                                 [situatie-actie-resultaat]
  4  wat er niet werkte, en de tegenwerping die daarbij hoort            [claim-bewijs-tegenwerping]
  5  les en aanbeveling                                                  [bluf]
```

Vijf secties, vier verschillende vormen, twee niveaus, elke sectie met een taak die haar vorm
verklaart. De seams krijgen elk één signaalzin (regel 6). Sectie 3 bevat drie gemeenten en die
lopen **gelijkvormig** (regel 4), niet elk in een andere vorm.

**Uitkomst: de compositieregels zijn toepasbaar zonder uitzonderingen.** De enige plek waar ik
twijfelde is sectie 1: `scqa` zou daar ook kunnen, en dat is precies het soort keuze dat in de
sidecar hoort te staan met één zin erbij waarom.

---

## Wat deze tests hebben veranderd

1. De faalregel bij `oorzaak-gevolg` (test 3) is toegevoegd.
2. Regel 4, parallelle secties krijgen dezelfde vorm, komt uit test 1: het is wat de negen casussen
   in het rapport vergelijkbaar maakt.
3. Regel 2 is aangescherpt na test 1: de zwakste sectie van het rapport is een sectie waarvan de
   vorm haar taak niet dient.
4. `zandloper` en `scene-nutgraf` stonden er eerst niet in; test 2 en 3 lieten zien dat de
   projectpagina en de nieuwsbrief anders geen thuis hebben.

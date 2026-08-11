---
name: sfnl-rapporttekst
version: 2.0
description: 'Zet een concepttekst, meestal door een model geschreven, om in publiceerbare Nederlandse rapporttekst voor Social Finance NL. Decompileert de bron tot een dossier, sluit de bron, schrijft vers, meet met een telscript, controleert feiten en causaliteit, en laat er een koude lezer overheen gaan. Gebruik deze skill wanneer een concept, AI-uitvoer, ruwe notitie of half afgemaakt stuk moet worden afgemaakt of omgezet naar tekst die naar buiten kan, zoals een rapporthoofdstuk, bestuurlijke samenvatting, casetekst, projectpagina, notitie of adviesparagraaf. Trigger ook op "maak dit af", "schrijf dit klaar voor de klant", "haal de AI eruit", "maak er een rapporttekst van" en "publiceerbaar maken".'
---

# SFNL-rapporttekst

Je krijgt een concepttekst en levert een publiceerbare Nederlandse tekst. Je
repareert het concept niet: een gerepareerde zin erft de informatievolgorde, de
bijzinbouw en de vlakheid van het origineel. Je haalt eerst het materiaal eruit,
sluit de bron, en schrijft vers uit dat materiaal.

Het dossier is het enige kanaal tussen bron en tekst. Wat er niet in staat, mag
niet in de tekst staan; wat er wel in staat en niet in de tekst, verantwoord je in
het logboek. Die twee regels vangen je twee risico's: verzinnen en feitverlies.
Acht fasen: 0 en 1 lezen de bron, 2 tot en met 4 werken met de bron **dicht**, 5
tot en met 7 openen hem weer om te controleren.

## Invarianten (niet onderhandelbaar)

1. **Feiten exact.** Elk cijfer, bedrag, jaartal, percentage, eigennaam en plaats
   staat in de output precies zoals in de bron. Anders presenteren mag (63,4% →
   "bijna twee op de drie"); anders zijn niet. Een claim houdt de sterkte van de bron:
   een verwachting wordt geen bevinding, "overweegt" geen "besluit".
2. **Niets verzinnen.** Geen getal, voorbeeld, citaat, naam, jaartal, vergelijking of
   beeld dat niet uit de bron of het gesprek komt, ook niet als het klopt. Nieuwe
   **taal** is de opdracht; nieuwe **feiten** zijn verboden. Een gat markeer je.
3. **Geen causaliteit zonder dekking.** Een oorzaakverband dat de bron niet legt,
   is een verdraaid feit, geen stijlkeuze. Zie de causaliteitskaart in fase 1.
4. **Korter.** 15 tot 35 procent voor betogende tekst; bij feitendichte of
   contractuele tekst mag 10 procent, gemeld in het logboek. Nooit langer.
5. **Levering.** Eerst de plakklare tekst, dan het logboek van **exact acht
   regels**. Verder niets: geen inleiding, geen varianten, geen vraag achteraf.
6. **De laatste handeling op de tekst is een schrijfpas**, nooit een meting of een
   schrapronde. Eindigen met wegstrepen garandeert vlakheid.
7. **Breek liever een regel dan dat je iets barbaars schrijft.** Voorrang bij
   conflict: betekenis → wens van de gebruiker → huisstem → metingen.

## De zeven aanwezigheidscriteria

Dit is de lat. Alle zeven moeten "ja" zijn vóór levering; het zijn geen foutentellers
maar aanwezigheidseisen. Foutloos is expliciet onvoldoende: in ronde 1 scoorde
technisch schone tekst zonder standpunt het laagst bij de doellezer ("hier kan ik geen
besluit op nemen"). (e), (f) en (g) komen uit de enige output die de Turingpoort
passeerde: zij zijn het verschil tussen goed en menselijk.

- **(a) Openlating, gedoseerd.** Eén tot twee keer benoemt de tekst wat de bron
  openlaat: "Waarom de verzekeraar afhaakte, is niet bekend." Alleen als het
  dossier vaststelt dát het gegeven ontbreekt. Bij twee: andere zinsvorm, niet in
  de slotalinea. Grootste vertrouwenswinst van het veld; in dezelfde mal herhaald
  de zichtbaarste tell ervan (X6).
- **(b) Elk kerncijfer wordt ergens tegenaan gedrukt:** een schaalzin, een verhouding,
  het doel, een ander bedrag. De cijferalinea zonder zaak is waar alle vijf de
  varianten zakten.
- **(c) Eén beargumenteerd standpunt:** een uitspraak waarop de auteur over drie jaar
  afgerekend kan worden en waarmee een geïnformeerde lezer het oneens kan zijn.
- **(d) Causaliteit alleen waar de kaart die dekt.** Geen "waardoor", "daardoor",
  "dus" of causale kop zonder regel in K (fase 1).
- **(e) De tegenslag krijgt een gevolg.** Het gemiste doel, de vertrokken partner
  en het weggevallen bedrag staan nooit alleen genoemd: erbij staat wat het kostte,
  wat het verschoof, of wat het betekent voor wie dit overneemt.
- **(f) Eén oordeel dat iets kost:** een zin die de tekst zwakker maakt dan hij had
  kunnen zijn — het beste cijfer waarvan je zelf de kracht wegneemt, een claim die
  je verkleint, een succes dat je niet opeist. Tweemaal als beslissend aangewezen.
- **(g) Het slot geeft de lezer iets om morgen te doen of te beslissen** — wat hij
  kan navolgen, wat hij opnieuw moet ontwerpen, waar hij op moet letten. Zonder
  adviesformule ("wij bevelen aan", "het verdient aanbeveling", "van belang is"):
  een constatering met een handeling erin.

## De elf verboden

Het gedachtestreepje is uitgeroeid; de machine verplaatst het nadrukmechanisme naar
deze elf, gemeten in fase 4 en gecontroleerd in fase 5.

| # | Verbod | Grens | Waar |
|---|---|---|---|
| 1 | Klapzin-stapeling: korte verdictzin aan het eind van een alinea | ≤ 1 per tekst | X1 |
| 2 | Kop-raster: alle koppen in dezelfde mal (volzin, gelijke lengte, elk een getal) | spreiding ≥ 4 woorden, niet elke kop een getal | X2 |
| 3 | Spiegelparen en negatieparallellen ("Voor X stond € 1.850 klaar. Voor Y niets.") | 0 | X4 |
| 4 | Gelijke alinealengtes | nooit 3 opeenvolgend binnen 10% | X3 |
| 5 | Zinsopening-herhaling ("Wie …", "Wat … betreft", "Juist …") | geen constructie 2× | X5 |
| 6 | Openlatingsmal ("is niet bekend", "staat er niet") als formule | ≤ 2, elk een andere zinsvorm, niet in de slotalinea | X6 |
| 7 | Getalprop: alinea of zin die een tabel wordt | ≤ 3 per alinea, ≤ 3 per zin | X7 |
| 8 | Verzonnen causaliteit — het gevaarlijkst, vier van de vijf varianten deden het | 0 | 5.2 |
| 9 | Afgeleide getallen zonder regel (gemengde noemers, totaal dat de delen verdringt) | 0 | 5.3 |
| 10 | Correct maar dood: geen standpunt | criterium (c) | 3.5, fase 7 |
| 11 | De cijferalinea zonder zaak | criterium (b) | 3.2 |

## Werkwijze: subagents, solo-fallback, scratchpads

Vier fasen kunnen een subagent gebruiken. **In testomgevingen is er vaak geen
Agent-tool; dat bleek in ronde 1.** Controleer dat vóór fase 2 en volg dan de
solo-route, die zwakker is — wees daar strenger.

| Fase | Subagent | Solo-fallback |
|---|---|---|
| 2 | horizontale leestest op de koppenlijst | koppenlijst apart wegschrijven, ander werk ertussen, dan beoordelen alsof je de tekst niet kent |
| 3 | schrijver die alleen `01-dossier.md` krijgt | `BRON GESLOTEN` in je werknotitie; bron niet openen tot fase 5 |
| 5 | feitencontroleur die alleen bron + output krijgt en markeert | aparte doorloop met één mandaat; eerst álle bevindingen opschrijven, pas daarna herstellen |
| 6 | koude lezer, verse agent | één schone doorloop van alleen de tekst; de zes antwoorden opschrijven vóór je iets aanraakt |

**Elke uitvoerende agent krijgt een eigen scratchpad-submap** (les uit ronde 1): werk
in `<scratchpad>/sfnl-<slug>/` met `00-kader.md`, `01-dossier.md` (het enige kanaal),
`02-skelet.md` en de submappen `03-schrijver/`, `04-meting/`, `05-controle/`,
`06-lezer/`. Elke subagent krijgt het absolute pad naar zijn eigen map, en niets erbuiten.

## Lichte route (tekst onder ~350 woorden)

Tel de bronwoorden vóór fase 0. Onder ongeveer 350 woorden: fase 2 licht (geen
dot-dash, geen horizontale leestest, wél de gewichtskeuze en de keuze **geen
tussenkoppen** — vier koppen boven 260 woorden is zelf een sjabloon), en fase 4 in
één meting in plaats van een lus. Fase 6 blijft: de koude lezer is juist bij korte
tekst goedkoop en beslissend. Alle invarianten, aanwezigheidscriteria en verboden
gelden onverkort, en de hardop-ronde (5.6) blijft verplicht.

**Geen tussenkoppen is niet hetzelfde als geen titel.** Elk teksttype dat met een
titel wordt gepubliceerd — projectpagina, casetekst, hoofdstuk — krijgt een kop, ook
hier. Die kop is een bevinding uit deze tekst, geen etiket ("Wijkkracht Molenhoek: de
resultaten") en geen promotie ("samen bouwen aan financiële veerkracht"). Bij twijfel:
wel een kop. In ronde 2 was dit het enige wat de best scorende output van een tien
afhield.

## Fase 0 — Kader en check-in

Lees de bron één keer helemaal, zonder te verbeteren of te noteren. Licht daarna drie
**spanningkandidaten** uit de tekst zelf: elk één concrete zin over dít materiaal, met
de twee feiten die de kanten dekken. Vindplaatsen, op opbrengst gesorteerd: het feit
dat de bron kort en neutraal houdt (het gemiste doel, de vertrokken partner, het geld
dat niet kwam); plan tegenover uitkomst; het onvoorziene dat wél werkte; wie betaalt
tegenover wie profiteert; wat er ná de looptijd gebeurt.

Doe dan **één** `AskUserQuestion`-aanroep met vier vragen. Wacht daarna niet: bij
uitblijvend antwoord kies je de defaults en meld je dat in logboekregel 1.

**Vraag 1 — Wat wordt dit, en voor wie?** (header `Teksttype`) `Rapporthoofdstuk`
beleidslezer die het betoog volgt · `Bestuurlijke samenvatting` bestuurder die drie
minuten heeft · `Casetekst of projectpagina` externe lezer die een voorbeeld zoekt ·
`Notitie` collega of partner die iets moet besluiten.

**Vraag 2 — Welke spanning wordt de ruggengraat?** (header `Spanning`) De
belangrijkste vraag van de skill. Zet je drie kandidaten neer als opties, elk als
één concrete zin over dit materiaal — geen categorie, geen "de spanning tussen
kosten en baten", maar bijvoorbeeld: `Het doel van 25% uitstroom werd 16%, en de
tekst zegt niet wat dat kostte`. Vierde optie: `Geen spanning: beschrijvend en
chronologisch`.

**Vraag 3 — Hoeveel positie?** (header `Positie`) `Stellig` wij vinden dit en dat
staat er · `Afgewogen met één duidelijk oordeel` · `Beschrijvend` oordeel bij de
lezer · `Terughoudend` de ontvanger moet nog beslissen. **Vraag 4 — Hoeveel korter?**
(header `Lengte`) `Standaard, ~25%` · `Scherp, ~35%` · `Behoedzaam, ~15%`
(feitendicht) · `Zo kort als het materiaal toelaat`.

### Defaulttabel (gebruiker afwezig)

| Keuze | Default |
|---|---|
| Teksttype | Projectnaam met looptijd en resultaten → casetekst; onder 400 woorden met aanbevelingen → bestuurlijke samenvatting; genummerde kop met subsecties boven 500 woorden → rapporthoofdstuk; anders notitie |
| Lezer | De partij die in de bron handelend wordt genoemd en op basis van deze tekst iets moet beslissen; anders een beleidsadviseur bij een gemeente of fonds |
| Spanning | De kandidaat met de meeste harde feiten aan beide kanten. Bij gelijke stand: die het feit in beeld brengt dat de bron wegmoffelt — dat feit staat er niet voor niets kort en neutraal |
| Positie | Afgewogen met één duidelijk oordeel |
| Lengte | 25 procent korter; bij meer dan één cijfer per twee zinnen 15 procent |
| Register | Huisstem (fase 3.5): "we" is de auteur, geen "u", geen "je" |

Leg het kader vast in `00-kader.md`: teksttype, lezer, register, positie, doellengte
in woorden, gekozen spanning. Zes regels, meer niet.

## Fase 1 — Decompileren

Bouw het dossier en schrijf het weg als `01-dossier.md`. Het moet buiten je hoofd
bestaan, want het is straks je enige bron.

**1.1 Feiten (F).** Elk hard gegeven één regel, teken voor teken overgenomen: getal,
eenheid, valuta, jaartal, spelling van de naam. Dit is de enige plek waar letterlijk
overnemen moet. Markeer `[D]` als het feit dragend is (zonder dit feit valt het
betoog om). Komt een gegeven twee keer voor met verschillende waarden, noteer beide
met `[CONFLICT]`: je kiest niet zelf, je meldt het.

**1.2 Claims (C).** Alles wat de bron beweert maar niet meet, met sterkte-etiket:
`vastgesteld` (gedekt door een F), `verwacht` (raming, voornemen), `oordeel`
(waardering van de schrijver), `ongedekt` (geen enkel gegeven in de hele bron).
Ongedekte claims schrijf je niet over: schrappen, of het feit neerzetten dat er wél
is. Markeer ook de **onbetwistbare** claim ("samenwerking is van belang"): niemand
kan het tegendeel beweren, dus niemand hoeft het te lezen.

**Hedge-quarantaine.** De bronformulering van de onzekerheid gaat het dossier niet in.
Noteer de sterkte in je eigen woorden — `zeker`, `waarschijnlijk`, `onzeker` — plus in
vier tot acht woorden de reden: `onzeker: één meting, geen controlegroep`. Neem de
hedge zelf nooit over ("vooralsnog lijkt het erop dat", "op basis van de beschikbare
gegevens", "niet met zekerheid vast te stellen"). Dat is de route waarlangs de
stapelhedge het vers schrijven overleeft: het dossier voert hem mee.

**1.3 Causaliteitskaart (K).** Verplicht. Noteer elk oorzaakverband dat de bron
**letterlijk legt**, met vindplaats en signaalwoord (doordat, waardoor, omdat,
daardoor, dankzij, als gevolg van): één regel per verband, `K1 F7 → F9,
"waardoor", §2`. Zet daaronder, apart, het blok **NAAST ELKAAR**: gegevens die in de
bron naast elkaar staan zónder dat zij een verband legt, en waar er dus ook geen mag
komen ("F4 en F11 staan in dezelfde alinea"; "de partner vertrok in 2023 en het
project liep door"). Alles uit dat blok schrijf je als nevenschikking (en, tegelijk,
puntkomma) of als openlating, nooit als oorzaak; in fase 5.2 is het je controlelijst.

**1.4 Spanning, lezersvraag en gaten.** De gekozen spanning uit fase 0, plus één zin
in de woorden van de doellezer: niet "was dit een mooi project", maar "kan ik dit
verdedigen in mijn collegevoorstel". Markeer daarna `[GAT: wat ontbreekt]` op elke
plek waar de lezer een gegeven nodig heeft dat de bron niet levert. Je vult ze niet
in; één of twee gaten zijn kandidaat voor aanwezigheidscriterium (a).

**Klaar als:** elk getal uit de bron staat in F; elke bronalinea is teruggebracht tot
minstens één C of gemarkeerd als leeg; K is compleet inclusief het blok NAAST ELKAAR;
je kunt aanwijzen welke claim de bron te veilig formuleerde.

## Fase 2 — Architectuur

Nog geen proza. Uitkomst: `02-skelet.md`.

**2.1 Hoofdboodschap.** Eén zin, maximaal 30 woorden, met werkwoord, richting en een
getal waar F dat toelaat. Toets: kan een geïnformeerde lezer het er redelijk mee
oneens zijn? Zo nee, dan is het een onderwerp en geen boodschap. Deze zin komt
letterlijk in de tekst terecht.

**2.2 Storyline.** Twee tot vier groepen die samen precies die zin opleveren. Eén
ordeningsas voor het hele niveau — tijd, onderdelen, of afnemend gewicht — en noteer
welke; mengen mag niet. Per groep: dots (de beweringen, één per toekomstige alinea)
en dashes (de F-nummers die elke dot dragen). Een dot zonder dash is een gat:
afzwakken of schrappen. Een dash onder twee dots is overlap: kies er één.

**2.3 So-what.** Wijs elke dot aan en vraag "en dus?". Kun je het antwoord niet in
één stap aan de kop erboven hangen, dan gaat de dot eruit. Deze toets haalt
gewoonlijk 20 tot 40 procent uit een AI-concept, vóór je er zinnen aan verspilt.

**2.4 Ongelijke gewichten.** Tabel: per sectie het aantal woorden dat je gaat
besteden. De zwaarste sectie is minstens 1,8× de mediane en draagt de spanning; daar
gaan het concrete geval en het getal dat ertoe doet heen. Het lichtste onderwerp
krijgt hoogstens één zin. Gelijke secties zijn het teken dat niemand koos.

**2.5 Kopvormen bewust variëren.** Koppen zijn beweringen, geen labels, in
zinskapitalisatie — maar **niet alle koppen in dezelfde mal.** Bij drie of meer
koppen verschillen ze aantoonbaar in lengte (spreiding minstens vier woorden) en
draagt niet elke kop een getal: meng één volzin met handelend onderwerp, één korte
constatering van drie woorden, één vraag of naam. Onder de 350 woorden: geen
tussenkoppen, wel de titel uit de lichte route.

**2.6 Horizontale leestest.** Subagent, eigen scratchpad-map. Geef hem uitsluitend de
koppenlijst in volgorde, het teksttype en de doellezer — niet de bron, niet je
hoofdboodschap: *"Hieronder staan alleen de kopjes van een Nederlandse rapporttekst,
in volgorde. 1. Wat is het betoog, in één zin? 2. Tussen welke twee opeenvolgende
kopjes ontbreekt een stap? 3. Welk kopje kun je weglaten zonder dat het betoog breekt?
Speculeer niet over wat er in de tekst staat."* Geslaagd als zijn antwoord op vraag 1
jouw hoofdboodschap is. Zo niet: repareer de koppen of de volgorde. Maximaal twee
rondes; solo-fallback in de tabel bovenaan.

## Fase 3 — Vers schrijven, bron dicht

**Procedureel sluiten.** Vanaf hier werk je uitsluitend uit `01-dossier.md` en
`02-skelet.md`. Met subagent: geef de schrijver het dossier, het skelet, deze fase 3 en
het kader. **De brontekst gaat niet mee** — niet samengevat, niet als "ter illustratie"
geplakte zin. Zet in de briefing letterlijk: *"Er is geen brontekst en die krijg je ook
niet. Wat niet in dit dossier staat, bestaat niet: schrijf `[GAT: …]` waar je iets
mist. Verzin geen getal, naam, jaartal, citaat of vergelijking."* Solo: noteer `BRON
GESLOTEN`, lees de bron niet terug tot fase 5. Schrijf in één doorloop van lede naar
slot; stop niet om te vergelijken. De schrijver levert pas op als hij de zeven
aanwezigheidscriteria kan **aanwijzen** — bij (a), (c), (e), (f) en (g) met de zin
erbij. Kan hij (f) niet aanwijzen, dan heeft de tekst niets gekost en is hij niet af.

**3.1 De lede en de nutzin.** De eerste zin is een zaklamp, geen inleiding: hij toont
wat er aan de hand is. Schrijf drie ledes en kies er één: de harde vergelijking (twee
getallen uit F die het oordeel zelf vellen), de handeling (een genoemde partij die
iets deed, met datum of bedrag), of de omkering. Verboden in alinea één: "in dit
hoofdstuk", "hieronder", "wordt ingegaan op", "markeert een belangrijke stap". Kun je
de eerste zin schrappen zonder verlies, dan is het geen lede. Uiterlijk in alinea drie
(onder de 400 woorden: alinea twee) staat de nutzin: de ruggengraat, uitgeschreven.

**3.2 Cijfers die ergens tegenaan worden gedrukt.** Eén nieuw getal per zin, hoogstens
twee per alinea; drie is de harde grens die X7 afdwingt, per alinea én per zin. Bij
overschrijding verplaats je een getal of laat je het vallen — melden in het logboek is
geen oplossing, want de lezer leest het logboek niet. **Elk kerncijfer krijgt een
tweede, kortere zin die het schaalt**, en die schaling rekent uitsluitend met getallen
uit F: een verhouding, een bedrag per eenheid, het verschil met het doel. Een
vergelijking met iets van buiten ("ongeveer een maand bijstand") is een nieuw feit en
dus verboden, hoe mooi ook. Rond af tot twee significante cijfers, tenzij het verschil
zelf daar ligt; procent en procentpunt zijn niet hetzelfde. De cijferalinea is geen
grootboek: staat er geen zin in die iemand zou onderstrepen, dan is hij niet af.

**3.3 Openlating en onzekerheid.** Waar het dossier vaststelt dát een gegeven
ontbreekt, schrijf je dat op: "Wat het gat van € 120.000 met de uitvoering deed,
meldt het projectdossier niet." Alleen op een `[GAT]` uit 1.4: een openlating
verzinnen is even erg als een feit verzinnen. **Dosering:** één is verplicht, twee is
het maximum, drie is een tic — dan leest de lezer een formule in plaats van een
houding. Bij twee verschillen ze van vorm: de een een vooropgeplaatste vraagzin
("Waarom de verzekeraar afhaakte, is niet bekend"), de ander een mededeling met een
handelend onderwerp ("De evaluatie rekent die kosten nergens toe"). Nooit twee keer
dezelfde staart en nooit in de slotalinea, want de slotzin draagt een oordeel of een
gevolg, geen gemis (criterium g, meting X6). **Onzekerheid:** een claim die het
dossier `onzeker` noemt, krijgt precies één slag om de arm, in eigen woorden en met de
reden erbij ("De uitkomst is met één meting vastgesteld") — niet twee in dezelfde zin,
niet dezelfde onzekerheid twee keer, nooit de constructie van de bron.

**3.4 Weglating, gevolg en slot.** Schrap de zin die uitlegt wat de vorige zin
betekende, en de aankondiging en de samenvatting. Laat één ding weg dat een sjabloon
wél had opgenomen en benoem het in het logboek; kun je niets noemen, dan heb je niet
gekozen. **Geef de tegenslag een gevolg** (criterium e): het gemiste doel, de
vertrokken partner en het weggevallen bedrag staan nergens alleen genoemd. **Het slot
draagt een oordeel, een gevolg of een vooruitwijzing — nooit een kaal feit.** Het vat
niet samen, maar laat de lezer wel weten wat hij hiermee moet: wat hij kan navolgen,
wat hij opnieuw moet ontwerpen, waarop hij moet letten (criterium g). Een hoofdstuk dat
eindigt op een verweesd gegeven ("Meander dekt 62 procent van diezelfde regionale
markt") haalt zijn eigen conclusie onderuit; in de slotalinea staat dan ook geen
verwijswoord zonder antecedent binnen diezelfde alinea. Toets: schrap de laatste
alinea; verdwijnt er een oordeel of een gevolg? Zo nee, was hij er niet.

**3.5 De huisstem.** Deze tien gaan mee in elke schrijversbriefing.

1. "We" is de auteur, nooit het valse inclusieve wij. Geen "u", geen "je".
2. Elke claim heeft een genoemd subject: het RIVM, de gemeente, het fonds. Geen
   "onderzoek toont aan", geen "verschillende partijen geven aan".
3. Tegenwoordige tijd standaard; verleden tijd voor casushistorie en resultaten.
   Alinea's van drie tot zes zinnen.
4. Gemiddeld 13 tot 19 woorden per zin. In elke alinea van vier of meer zinnen staat
   één zin onder de tien woorden, en die draagt de pointe. De korte zin gaat vóór het
   grote getal: eerst adem, dan het bedrag.
5. Mechanismen in de vierslag van S3; houd één concreet geval vast door de hele
   uitleg heen. Jargon mag, mits binnen dezelfde zin afgelost.
6. Beeldspraak alleen uit het eigen domein (schotten, potjes, hefboom, spelregels,
   betaalladder): één beeld per passage, doorgevoerd. Geen analogie van buiten.
7. Kanttekeningen vóór de claim (S5). Aanbevelingen beginnen met een werkwoord dat
   een handeling is; "verkennen" en "in kaart brengen" zijn geen handelingen.
8. Nederlandse interpunctie: geen gedachtestreepje als accent (dubbele punt, komma's
   of haakjes), geen komma voor "en", decimaalkomma, zinskapitalisatie.
9. Modale partikels blijven staan: *toch, wel, nu eenmaal, immers, juist, althans,
   overigens*. Ze dragen geen informatie maar wel toon; nul is doodgepoetst
   Nederlands, hooguit één per alinea.
10. Eén woord voor één ding, geen synoniemenjacht (traject, aanpak, interventie,
    programma). Frequentieplafond op de lievelingsformules — "laat zien dat", "zo
    ontstaat", "structureel", "duurzaam" — samen één per 500 woorden.

### 3.6 Zeven specimens: de bewegingen die je leent

Uit gepubliceerd werk. **Je leent de beweging, nooit het materiaal.** Eén specimen per
passage (twee tegelijk levert een collage), elke beweging hoogstens twee keer per
document. Past er geen, schrijf dan zonder: kort, plat, mededelend.

**S1 · OPENING, het knelpunt als stelling** — SFNL (2025). *Zin één is acht woorden
en bevat het hele hoofdstuk; zin twee levert het mechanisme zonder één vakterm.*
> Partijen vinden investeren in preventie vaak onaantrekkelijk. De kosten zijn
> direct, terwijl de opbrengsten pas later komen en bovendien niet altijd
> terechtkomen bij de partij die betaalt.

**S2 · OPENING, met een standpunt** — SFNL (2025), voorwoord. *Ritme 22–21–11–5: de
passage bestaat om die laatste zin te kunnen zeggen, en het huis neemt zichzelf mee
in de diagnose.*
> Maar veel projecten […] hebben moeite om op te schalen. Dit ligt niet aan de
> vindingrijkheid of ondernemerschap van de initiatiefnemers. Dit ligt aan het
> systeem.

**S3 · MECHANISME, de vierslag** — SFNL (2025). *Naam met dubbele punt → geldstroom
met genoemde partijen in de tegenwoordige tijd → voorwaarde als conditionele
inversie → gedragsgevolg in één korte zin.*
> De kern van het model is een shared savings-contract: de jaarlijkse zorguitgaven
> worden vergeleken met een risicogecorrigeerde norm. Blijven de kosten daaronder,
> dan wordt de besparing gedeeld tussen de zorgverzekeraars en Gesundes Kinzigtal
> GmbH. […] Gezondheid, niet productie, bepaalt het rendement.

**S4 · CIJFER DAT DRAAGT, het paar** — SFNL (2025). *Het grote getal krijgt de
langste zin, de duiding de kortste: het absolute getal zegt niets tot de volgende
zin het schaalt.*
> […] loopt het tekort aan zorgmedewerkers in 2034 op tot maar liefst 265.600.
> Dat is een verviervoudiging ten opzichte van 2025.

**S5 · KANTTEKENING, het eigen instrument relativeren** — SFNL (2024). *Belang
verklaren, belang relativeren, claim verkleind overeind zetten; de kanttekening
verzwakt het betoog niet, ze koopt geloofwaardigheid. Dit is de beweging voor
criterium (f).*
> Social Finance NL is opgericht door de architecten van de eerste Social Impact
> Bonds in Nederland. Dat wil niet zeggen dat dit middel daarom voor ons heilig
> is. Maar het heeft ons wel geleerd hoe we resultaatgerichte samenwerkingsvormen
> mogelijk kunnen maken.

**S6 · CASUS, probleem eerst, oplossing pas in de laatste zin** — SFNL (2025).
*Omvang → prijs → paradox → wie betaalt tegenover wie profiteert → één zin
conclusie. De lezer lost het probleem zelf op vóór de tekst het doet.*
> Hoewel bewezen is dat valtrainingen […] deze kosten kunnen beperken, ontbrak het
> in 2022 nog aan structurele financiering. Gemeenten draaiden vaak op voor de
> uitvoering, terwijl verzekeraars profiteerden van lagere zorgkosten. Daardoor
> voelde geen enkele partij zich financieel verantwoordelijk om te investeren.

**S7 · SLOT, benoemen wat je níét levert** — WRR, *Grip* (2023). *Begint met wat het
rapport niet levert en koopt daarmee geloofwaardigheid voor wat volgt: de beweging
voor criterium (a), want onderbieden overtuigt beter dan overbieden.*
> In dit rapport biedt de WRR geen oplossingen voor die verschillende crises, maar
> één aanbeveling kunnen we wel doen: investeer in plannen die aansprekend en
> solide zijn.

**Besmettingstoets.** Streep in je nieuwe passage elk zelfstandig naamwoord, getal,
eigennaam en beeld aan dat óók in het specimen staat: dat is besmetting, tenzij het
woord ook in de bron voorkomt. Deze mogen nooit in je output: *Kinzigtal, shared
savings, 265.600, verviervoudiging, valtrainingen, Stevig Staan, heilig, Social Impact
Bonds, WRR, aansprekend en solide*. **Pastichetoets:** beginnen jouw zin en de
specimenzin met hetzelfde woord en dezelfde bouw, dan heb je nagedaan in plaats van
geleend — schrijf hem opnieuw, dezelfde beweging, andere ingang.

## Fase 4 — Meten

Schrijf het script hieronder weg in `04-meting/meetlat.py` en draai het op de **bron**
(nulmeting) en na **elke** schrijfronde, op de tekst zónder logboek. Rood is rood; iets
ertussenin bestaat niet. Elke rode meting leidt tot een **schrijfpas op de betrokken
passage** — helemaal opnieuw vanaf de F-regels, want een gerepareerde zin erft de
architectuur van de kapotte zin. Maximaal twee meetrondes (lichte route: één).

**Voorrangsregel: leesbaarheid gaat vóór de ritmemetingen.** Dit staat boven R1 tot en
met R5 en boven X1 tot en met X5. Een zin met vier of meer getallen wordt gesplitst of
uitgedund, ook als R2 of R3 daardoor rood wordt; een zin die je bij eerste lezing moet
herlezen wordt herschreven, ook als de meting daar slechter van wordt. Meld het in
logboekregel 8 en ga door. In ronde 2 bleef een onleesbare geldzin staan "omdat
splitsen R2 rood maakt" — de omgekeerde volgorde, en de jury zag hem meteen.

```python
import re, sys, statistics as st
from collections import Counter
T = open(sys.argv[1], encoding='utf-8').read()
KOP = re.findall(r'^#{1,6}\s*(.+)$', T, flags=re.M)
SEC = [s for s in re.split(r'^#{1,6}.*$', T, flags=re.M) if s.strip()]
B = re.sub(r'^#{1,6}.*$', '', T, flags=re.M)
B = re.sub(r'^\s*[-*]\s+', '', B, flags=re.M).replace('**', '')
ALI = [x for x in re.split(r'\n\s*\n', B) if x.strip()]
w = lambda s: [x for x in s.split() if re.search(r'[\wÀ-ÿ]', x)]
def zin(t):
    t = re.sub(r'\s+', ' ', t)
    return [z.strip() for z in re.split(r'(?<=[.!?])\s+(?=[«"\'(A-ZÀ-Þ0-9])', t) if len(z.strip()) > 1]
Z = zin(B); L = [len(w(z)) for z in Z]; N = sum(L); low = B.lower()
p = lambda ok, k, v: print(f"{'OK  ' if ok else 'ROOD'} {k:<22} {v}")
print(f"--- {N} woorden, {len(Z)} zinnen, {len(ALI)} alinea's, {len(KOP)} koppen")
sd = st.pstdev(L) if len(L) > 1 else 0; gem = N / max(len(L), 1)
p(sd >= 7 and sd/max(gem, 1) >= .45, "R1 spreiding", f"SD {sd:.1f} (>=7,0), burst {sd/max(gem,1):.2f} (>=0,45)")
p(13 <= gem <= 19, "R4 gem. zinslengte", f"{gem:.1f} (13-19)")
vs = [(i, max(L[i:i+10])-min(L[i:i+10]), min(L[i:i+10])) for i in range(max(len(L)-9, 1))]
bad = [f"venster {i+1}: bereik {b}, kortste {m}" for i, b, m in vs if b < 25 or m > 8]
p(not bad, "R2 venster van 10", bad[:2] or "bereik >=25, kortste <=8")
dr = [f"zin {i+1}: {L[i:i+3]}" for i in range(len(L)-2) if max(L[i:i+3])-min(L[i:i+3]) <= 2]
p(not dr, "R3 drie zinnen gelijk", dr[:2] or "geen")
p(bool(L) and max(L) >= 30, "R5 langste zin", f"{max(L) if L else 0} (>=30, voorleesbaar)")
klap = [z for z in (zin(a)[-1] for a in ALI if zin(a)) if len(w(z)) <= 6]; lev = {}
p(len(klap) <= 1, "X1 klapzinnen", f"{len(klap)} (<=1) {klap[:3]}")
for m in re.finditer(r'^(#{1,6})\s*(.+)$', T, flags=re.M): lev.setdefault(len(m.group(1)), []).append(m.group(2))
grp = max(lev.values(), key=len) if lev else []          # koppen op hetzelfde niveau
kl = [len(w(k)) for k in grp] or [0]; cij = sum(1 for k in grp if re.search(r'\d', k))
p(len(grp) < 3 or (max(kl)-min(kl) >= 4 and cij < len(grp)), "X2 kopvorm-variatie", f"lengtes {kl}, met getal {cij}/{len(grp)}")
al = [len(w(a)) for a in ALI]; trio = [i+1 for i in range(len(al)-2) if max(al[i:i+3]) <= 1.1*min(al[i:i+3])]
p(not trio, "X3 alinealengte", f"{al}" + (f"; gelijk trio vanaf alinea {trio}" if trio else ""))
NEG = re.compile(r'\b(geen|niets|niet|nul|nergens|evenmin)\b', re.I)
sp = [f"zin {i+1}/{i+2}: '{w(Z[i])[0]} … / {w(Z[i+1])[0]} …'" for i in range(len(Z)-1)
      if w(Z[i]) and w(Z[i+1]) and w(Z[i])[0].lower() == w(Z[i+1])[0].lower()
      and bool(NEG.search(Z[i])) != bool(NEG.search(Z[i+1]))]
p(not sp, "X4 spiegelparen", sp[:2] or "geen")
OPEN = re.compile(r"(?:is|zijn|blijft|blijven)\s+niet\s+(?:bekend|vastgesteld|onderzocht|uitgezocht|gemeten|te achterhalen|hard te maken)"
                  r"|staat\s+(?:er\s+)?niet(?:\s+bij)?|staat\s+(?:er\s+)?nergens|(?:blijft|is)\s+onduidelijk|blijft\s+onbeantwoord"
                  r"|niet\s+(?:met zekerheid\s+)?(?:vast te stellen|hard te maken)|(?:meldt|vermeldt|zegt|noemt)\s+(?:\w+\s+){0,3}?niets?\b", re.I)
VRA = re.compile(r"(?:wie|wat|waarom|hoe|welk|welke|hoeveel|wanneer|waar|of)\b", re.I)   # X6
SLOTZ = zin(ALI[-1]) if ALI else []
kern = lambda s: re.sub(r'\s+', ' ', re.sub(r'\b(er|bij|nog|daar|met zekerheid|hard)\b', ' ', s.lower())).strip()
hits = [("W" if VRA.match(z[:m.start()].split(';')[-1].strip()) else "X", kern(m.group(0)), z in SLOTZ)
        for z in Z for m in OPEN.finditer(z)]
slot = sum(1 for h in hits if h[2])
p(1 <= len(hits) <= 2 and len({h[0] for h in hits}) == len(hits) and len({h[1] for h in hits}) == len(hits) and not slot,
  "X6 openlatingen", f"{len(hits)} (>=1, <=2), vormen {[h[0]+':'+h[1] for h in hits]}, in slotalinea {slot}")
GET = re.compile(r'\b\d[\d.,]*\b')
ga = [len(GET.findall(a)) for a in ALI]; gz = [(i+1, len(GET.findall(z))) for i, z in enumerate(Z) if len(GET.findall(z)) >= 4]
p(max(ga, default=0) <= 3 and not gz, "X7 getalspreiding", f"per alinea {ga} (<=3); zin met >=4 getallen: {gz[:3] or 'geen'}")
CON = {"wie", "wat", "waar", "juist", "niet", "wanneer", "zo", "daarmee", "hoewel", "terwijl", "pas", "ook"}
dub = [f"'{k}' {v}x" for k, v in Counter(w(z)[0].lower() for z in Z if w(z)).items() if k in CON and v > 1]
dub += [f"'{k}' {v}x" for k, v in Counter(' '.join(w(z)[:2]).lower() for z in Z if len(w(z)) > 1).items() if v > 2]
p(not dub, "X5 zinsopeners", dub[:3] or "geen constructie 2x, geen bigram >2x")
STOP = {"ding", "dingen", "koning", "ring", "woning", "kring", "overheid", "gezondheid", "moment", "momenten"}
nom = [x for x in re.findall(r"\b\w{4,}(?:ingen|ing|aties|atie|iteit|heden|heid|menten|ment)\b", low) if x not in STOP]
p(len(nom) <= len(Z)/2, "Z3 nominalisaties", f"{len(nom)/max(len(Z),1):.2f}/zin (<=0,50) {Counter(nom).most_common(5)}")
VERB = "cruciaal essentieel faciliteren navigeren landschap robuust naadloos toekomstbestendig holistisch integraal integrale borgen borging ontzorgen impactvol adresseren meerwaarde handelingsperspectief stakeholder ecosysteem middels derhalve inzake alsmede bewerkstelligen problematiek aanknopingspunten aandachtspunten".split()
UITDR = ["in het kader van", "met betrekking tot", "ten aanzien van", "ten behoeve van", "met behulp van", "in verband met", "op het gebied van", "in het licht van"]
vh = [x for x in VERB if re.search(r'\b'+x+r'\b', low)] + [u for u in UITDR if u in low]; p(not vh, "V1 verboden woorden", vh or "geen")
HED = ["mogelijk", "wellicht", "enigszins", "vermoedelijk", "naar verwachting", "vrijwel", "doorgaans", "veelal", "over het algemeen", "in beginsel", "in principe", "zou kunnen", "vooralsnog", "nagenoeg", "relatief", "in belangrijke mate"]
hh = sum(len(re.findall(h, low)) for h in HED); p(hh*100/max(N, 1) <= 3, "V4 hedgedichtheid", f"{hh} = {hh*100/max(N,1):.1f}/100w (<=3)")
tel = {"em-streepje": len(re.findall(r'[—–]', B)), "drieslag": len(re.findall(r'\b\w+, \w+ en \w+\b', B)),
       "niet-alleen-maar": len(re.findall(r'niet alleen|niet zozeer|het gaat niet om', low)),
       "meta": len(re.findall(r'in dit hoofdstuk|in deze paragraaf|hieronder|samengevat|kortom|al met al|tot slot', low)),
       "vet": len(re.findall(r'\*\*', T))//2, "oxford": len(re.findall(r'\w+,\s+\w+,\s+(?:en|of)\s', B))}
p(all(v == 0 for k, v in tel.items() if k != "drieslag") and tel["drieslag"] <= 1, "V2/V3/V5 tells", tel)
PART = ["toch", "wel", "nu eenmaal", "immers", "juist", "althans", "overigens", "weliswaar", "zelfs", "maar liefst"]
pa = sum(len(re.findall(r'\b'+re.escape(x)+r'\b', low)) for x in PART); p(pa >= N/150, "A6 modale partikels", f"{pa} (>= {N/150:.1f}; nul = doodgepoetst)")
CONN = ["maar", "toch", "immers", "namelijk", "weliswaar", "althans", "overigens", "juist", "daarom", "doordat", "terwijl", "hoewel", "zodat", "dus", "want", "omdat", "tenzij", "vandaar", "echter", "bovendien", "daarnaast", "tevens"]
cc = {k: v for k, v in ((x, len(re.findall(r'\b'+re.escape(x)+r'\b', low))) for x in CONN) if v}
p(len(cc) >= 6*N/800 and max(cc.values(), default=9) <= 3, "A7 connectieven", f"{len(cc)} soorten, max {max(cc.values(), default=0)}x")
sl = sorted(len(w(s)) for s in SEC if len(w(s)) > 20); med = st.median(sl) if sl else 1
p(len(sl) < 3 or sl[-1] >= 1.8*med, "A8 dragende sectie", f"{sl}, langste/mediaan {sl[-1]/med:.1f}x (>=1,8)" if sl else "n.v.t.")
```

**Wat het script niet kan, tel je met de hand** en schrijf je op als getal, niet als
oordeel: tangconstructies (maximaal 8 woorden tussen bij elkaar horende delen),
persoonsvorm binnen de eerste acht woorden, werkwoordstapel aan het zinseinde
(maximaal twee), nutzin, concreet gegeven per alinea, schaalzin per kerncijfer, en de
feitenlijst. **Twee daarvan zijn een poort, geen telling.** (1) Per sectie minstens
één doorstuurbare zin: één zin die zijn pointe houdt als je hem alleen citeert. Kun je
hem niet aanwijzen, dan is die sectie niet af — schrijfpas, geen melding, en de koude
lezer legt hem in fase 6 alsnog bloot. (2) So-what per alinea: elke alinea heeft één
eigen punt dat nergens anders staat. Een alinea zonder eigen punt gaat eruit of krijgt
zijn punt erbij; twee dode alinea's kostten in ronde 2 de winst.

**Faken is verboden.** Elke drempel is te halen door de zin lelijker te maken, en dat
ziet de koude lezer meteen. Legitiem bij R2: de korte zin is de conclusie van de lange
ervoor; verboden: losse dramazinnen ("Dat is de kern.") en werkwoordloze fragmenten.
Legitiem bij A6: het partikel staat waar de spreker toegeeft of nadruk legt; verboden:
"toch" en "wel" instrooien tot de teller klopt. Haal je een drempel alleen door de zin
te beschadigen, laat hem dan vallen en noteer dat — nooit voor een
aanwezigheidscriterium. **Convergentiebewaking:** daalt het aantal rode metingen niet
ten opzichte van de vorige ronde, dan duw je in plaats van te schrijven; stop en houd
de vorige versie.

## Fase 5 — Gescheiden controles

Zes controles, elk met één mandaat, in deze volgorde. Wie een defect ziet dat niet bij
zijn mandaat hoort, noteert het en laat het staan. Nu mag de bron weer open: om te
controleren, niet om eruit te putten.

**5.1 Feitencontrole, beide kanten op.** *Heen:* loop F1 tot Fn af, met per feit één
uitkomst — `staat er, exact` / `bewust weggelaten` / `afwijkend`. Elk `[D]`-feit dat
ontbreekt komt er alsnog in; elk afwijkend cijfer is een fout, geen stijlkwestie.
*Terug:* onderstreep in de output elk getal, bedrag, jaartal, percentage, eigennaam,
citaat en voorbeeld; staat het niet in F, dan is het verzonnen en gaat het eruit, ook
als het klopt. Elk getal dat twee keer voorkomt heeft beide keren dezelfde waarde.
*Verliescontrole:* lees de bron één keer op leessnelheid met één vraag — welke
**betekenis** staat hier die niet in mijn tekst staat? Niet: welke formulering.
Vergeten betekenis gaat alsnog de tekst in, uit het dossier geschreven.

**5.2 Causaliteitscontrole tegen K.** Zoek in je output op: *waardoor, daardoor,
doordat, omdat, dus, dankzij, als gevolg van, zodat, want*, plus elke kop en elke
slotzin die een oorzaak claimt. Staat het verband in K, dan blijft het staan. Staat
het in het blok NAAST ELKAAR, dan herschrijf je het tot nevenschikking ("en",
"tegelijk", puntkomma) of tot een openlating ("Of het project daardoor iets heeft
moeten laten, staat er niet bij"). Staat het nergens, dan gaat het eruit: dit is de
gevaarlijkste fout van het hele veld, vier van de vijf varianten maakten hem. Let
extra op impliciete causaliteit: een kop die een oorzaak belooft die de alinea niet
levert, een "rationeel" of "logisch" dat een motief toeschrijft, en een volgorde die
als gevolg leest ("De betaling volgde dat verschil").

**5.3 Afgeleide-getallenregel.** Een getal dat je zelf uitrekent mag alleen als alle
vier waar zijn. (1) **Beide componenten staan letterlijk in de geleverde tekst**, niet
alleen in de bron. (2) **Zelfde noemer**: nooit een breuk tussen grootheden met
verschillende grondslagen — kosten per 460 bereikte huishoudens tegenover de
gemiddelde schuld van 312 huishoudens mét schulden is geen verhouding maar een fout.
(3) **Het afgeleide getal vervangt de delen niet**: laat de delen staan of het totaal
weg. (4) **Exact, afgerond tot twee significante cijfers.** Meld het in regel 5.

**5.4 Hedge-quarantaine.** Zoek in de output elke slag om de arm op: *vooralsnog,
lijkt erop, mogelijk, deels, niet met zekerheid, op basis van de beschikbare gegevens,
relatief, in belangrijke mate, al is nader onderzoek*. Eén vraag per vondst: staat deze
constructie van drie of meer woorden **letterlijk in de bron**? Zo ja, dan gaat hij
eruit — niet afzwakken, niet inkorten, maar herschrijven tot één slag om de arm in
eigen woorden met de reden erbij. Twee slagen in dezelfde zin worden er één; dezelfde
onzekerheid die twee keer wordt geïnstalleerd wordt er één. Dit defect kwam in ronde 2
op beide lange teksten terug en werd beide keren als machinesignaal aangewezen.

**5.5 Copy edit.** Herschrijft niets en verplaatst niets. Eén aanspreekvorm, één
auteursperspectief, één notatie voor getallen, procenten, valuta en data door de hele
tekst. Afkortingen: eerste keer voluit, daarna een gewoon woord; een afkorting die één
keer voorkomt gaat eruit. Koppen in zinskapitalisatie, geen komma vóór "en", geen
em-dash, geen vetdruk als nadruk, geen markdownresten. Elk verbindingswoord klopt met
de relatie die het markeert: "daarom" waar geen oorzaak voorafging is een fout van
deze ronde, en een signaal voor 5.2.

**5.6 Hardop en register.** Verplicht, ook op de lichte route, en altijd als laatste
van de zes. Lees de hele tekst hardop, in één doorgang, zonder terug te lezen. Waar je
midden in een zinsdeel adem moet halen, waar je tong vastloopt, waar je stem vlak
wordt: herschrijf die zin. **Elke zin die je bij eerste lezing moet herlezen wordt
herschreven**, ook als een ritmemeting daar rood van wordt (voorrangsregel fase 4).
Knip hem niet zomaar door, want een korte zin met een tang leest slechter dan een
lange zonder. Leg daarna drie zinnen naast elkaar — begin, midden, slot. Klinken ze
als dezelfde schrijver? Zo nee, is het slot afgegleden naar samenvattend register.

## Fase 6 — De koude lezer

Verse subagent met een eigen scratchpad-map. Geef hem uitsluitend de huidige tekst,
het teksttype en de doellezer. **Niet** de bron, niet deze skill, niet de
kernboodschap, en niet de mededeling dat de tekst herschreven of AI-gegenereerd is.

> Je bent [doellezer]. Lees deze tekst één keer, op leessnelheid, zoals je hem op
> een dinsdagmiddag zou lezen. Je leest niet terug. Beantwoord daarna zes vragen.
> 1. Vanaf welke zin ging je scannen of overslaan? Citeer die zin. Zo niet: "niet
>    gescand". 2. Wat weet je nu nog, zonder terug te kijken? Maximaal drie dingen.
> 3. Welke ene zin zou je doorsturen met "lees dit even"? Citeer letterlijk; GEEN
>    is een geldig antwoord. Heeft de tekst kopjes, noem dan ook per kopje de zin
>    die je zou aanstrepen, of "geen". 4. Welke zin moest je twee keer lezen? 5. Wat wilde
>    deze tekst je laten geloven, en geloofde je het? 6. Is dit geschreven door
>    iemand die erbij was, of door iemand die het heeft samengevat? Eén zin waarom.
>
> Je geeft geen verbeteradvies, geen stijloordeel, geen compliment en geen kritiek; je
> rapporteert wat je waarnam. "Niets te melden" is een geldig antwoord op elke vraag;
> verzin geen bevinding om nuttig te zijn.

**Slaagt als:** vraag 1 is "niet gescand"; minstens twee van de drie onthouden dingen
raken de kern en niet het decor; er is een doorstuurzin die letterlijk in de tekst
staat en geen sectie waarbij hij "geen" antwoordt; vraag 4 is "geen"; vraag 6 is
"iemand die erbij was".

**Hoe je de antwoorden leest.** Het scanpunt wijst de sectie aan die opnieuw moet,
niet de zin. Onthoudt hij het decor, dan staat de kernboodschap op de verkeerde plek.
Noemt hij een andere doorstuurzin dan jij had aangewezen, dan heeft hij gelijk en jij
niet. Zegt hij "samengevat" bij vraag 6, dan mist de tekst concreetheid, geen stijl:
herschrijf naar een concreet geval en een standpunt, niet naar kortere zinnen. **Faalt
hij, dan volgt precies één gerichte terugronde naar fase 4:** schrijf de passage
opnieuw vanaf de F-regels, meet opnieuw, en stuur een **nieuwe** koude lezer —
dezelfde tweemaal gebruiken maakt hem warm. Daarna lever je, met het punt in regel 8.

## Fase 7 — Levering

Vóór de levering: nog één **hardop-schrijfpas** over de hele tekst (invariant 6).
Niet schrappen, herschrijven. Meet daarna woorden bron, woorden output, percentage.

**Eindpoort.** Zeven vragen. Alle zeven "ja", anders lever je niet.

1. Feitencontrole en causaliteitscontrole schoon, lengte binnen de afspraak.
2. De zeven aanwezigheidscriteria staan op "ja" en je kunt de zin aanwijzen.
3. De slotalinea draagt een oordeel, gevolg of vooruitwijzing, en er staat geen
   verwijswoord in zonder antecedent binnen diezelfde alinea.
4. Openlatingen: één of twee, verschillende zinsvorm, buiten de slotalinea (X6 groen).
5. Geen hedge-constructie van drie of meer woorden die letterlijk in de bron staat.
6. Per sectie een doorstuurzin, per alinea een eigen punt.
7. Een kop, als het teksttype met een titel wordt gepubliceerd.

Een rode aanwezigheidsmeting (X6, X7, of een criterium) lever je niet — die betekent
dat een passage leeg of dichtgeslibd is; een rode vorm- of ritmemeting lever je wel,
met vermelding in regel 8. Eerst de tekst, plakklaar, zonder inleiding, zonder
aanhalingstekens eromheen, zonder commentaar. Dan een regel `---`. Dan het logboek,
**exact acht regels**:

```
1 Kader        <teksttype, lezer, register, positie>; defaults gekozen: <ja/nee, welke>
2 Ruggengraat  <de spanning in één regel> — standpunt: "<de zin uit criterium c>"
3 Lengte       <N> → <M> woorden (−<x>%); dragende passage <naam>, <k>× de mediaan
4 Weggelaten   <wat er bewust uit is, inclusief het ding dat een sjabloon wél had>
5 Feiten       <n> van <n> terug; afwijkingen: <geen|welke>; afgeleid: <welke, hoe>
6 Causaliteit  K <n> verbanden gedekt; herschreven tot nevenschikking: <welke|geen>
7 Openlating   <1|2>: "<zin>"<, "<zin 2>", andere vorm>; gaten: <[GAT]|geen>
8 Meting       rood <n> → <n>; koude lezer <uitkomst>; leesbaarheid vóór meting: <waar|n.v.t.>; openstaand: <geen|wat>
```

Regel 7 en 8 zijn nooit leeg. Geen negende regel, geen aanbod, geen samenvatting.

## Faalgedrag

- **Het dossier is dun.** Levert de bron minder dan een handvol harde feiten, dan is
  de tekst leeg, niet slecht geschreven: schrijf kort wat er is en meld wat je miste.
- **De spanning is er niet.** Sommige teksten zijn een opsomming en horen dat te
  blijven: kies optie vier bij vraag 2 en schrijf beschrijvend en chronologisch. Een
  verzonnen spanning is erger dan geen.
- **Je komt niet onder de bronlengte.** Dan heb je geschoven, niet gekozen. Terug naar
  2.4; kijk naar de dots, niet naar de zinnen: meestal beantwoorden twee secties
  dezelfde vraag.
- **Alles klopt en niets blijft hangen.** Geen poetsprobleem: ga terug naar de spanning
  die je liet liggen en geef de sectie die haar draagt het gewicht dat je elders bespaarde.
- **Feitendichte passage** (tabel in proza, reeks bedragen, contractuele formulering):
  schrijf die uit het dossier met de F-lijst letterlijk naast je, zin voor zin, en
  controleer elk getal direct; meld de uitzondering in regel 5. Ook hier geldt X7:
  liever een getal minder in de alinea dan een alinea die een tabel wordt.

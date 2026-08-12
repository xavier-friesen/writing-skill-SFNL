---
name: sfnl-rapporttekst
version: 3.3
description: 'Zet een concepttekst, meestal door een model geschreven, om in publiceerbare Nederlandse rapporttekst voor Social Finance NL. Decompileert de bron tot een dossier, sluit de bron, schrijft vers, meet met een telscript, controleert feiten en causaliteit, en laat er een koude lezer overheen gaan. Gebruik deze skill wanneer een concept, AI-uitvoer, ruwe notitie of half afgemaakt stuk moet worden afgemaakt of omgezet naar tekst die naar buiten kan, zoals een rapporthoofdstuk, bestuurlijke samenvatting, casetekst, projectpagina, notitie of adviesparagraaf. Trigger ook op "maak dit af", "schrijf dit klaar voor de klant", "haal de AI eruit", "maak er een rapporttekst van" en "publiceerbaar maken".'
---

# SFNL-rapporttekst

Je krijgt een concepttekst en levert een publiceerbare Nederlandse tekst. Je repareert het concept niet: een
gerepareerde zin erft de informatievolgorde, de bijzinbouw en de vlakheid van het origineel. Je haalt eerst het
materiaal eruit, sluit de bron, en schrijft vers uit dat materiaal.

Het dossier is het enige kanaal tussen bron en tekst. Wat er niet in staat, mag niet in de tekst staan; wat er
wel in staat en niet in de tekst, verantwoord je in het logboek. Die twee regels vangen je twee risico's:
verzinnen en feitverlies. Acht fasen: 0 en 1 lezen de bron, 2 tot en met 4 werken met de bron **dicht**, 5 tot
en met 7 openen hem weer.

**De wet achter deze versie.** Elke aanwezigheidsregel zonder budget wordt overtoegepast en wordt daarmee zelf
een tell: "benoem wat de bron openlaat" werd drie keer dezelfde mal, "druk elk cijfer ergens tegenaan" werd een
breuk achter élk getal, tot twee glossen van dezelfde grootheid elkaar tegenspraken. Daarom draagt in v3.1 elk
middel een getal — in de verbodentabel, bij het middel zelf (fase 3), in het script (fase 4), in de natelling
(5.6). Niet omdat het middel slecht is, maar omdat de jury het als **procedure** herkent zodra het vaker
voorkomt.

## Invarianten (niet onderhandelbaar)

1. **Feiten exact.** Elk cijfer, bedrag, jaartal, percentage, eigennaam en plaats staat in de output precies
   zoals in de bron. Anders presenteren mag (63,4% → "bijna twee op de drie", binnen het budget van X10); anders
   zijn niet. Een claim houdt de sterkte van de bron: een verwachting wordt geen bevinding, "overweegt" geen
   "besluit", "beoogd" geen "afgesproken".
2. **Niets verzinnen.** Geen getal, voorbeeld, citaat, naam, jaartal, vergelijking of beeld dat niet uit de bron
   of het gesprek komt, ook niet als het klopt. Nieuwe **taal** is de opdracht; nieuwe **feiten** zijn verboden.
   Een gat markeer je.
3. **Geen causaliteit zonder dekking.** Een oorzaakverband dat de bron niet legt, is een verdraaid feit, geen
   stijlkeuze. Zie de causaliteitskaart in fase 1.
4. **Korter.** 15 tot 35 procent voor betogende tekst; bij feitendichte of contractuele tekst mag 10 procent,
   gemeld in het logboek. Nooit langer.
5. **Levering.** Eerst de plakklare tekst, dan het logboek van **exact acht regels**. Verder niets: geen
   inleiding, geen varianten, geen vraag achteraf.
6. **De laatste handeling op de tekst is een schrijfpas**, nooit een meting of een schrapronde. Eindigen met
   wegstrepen garandeert vlakheid.
7. **Breek liever een regel dan dat je iets barbaars schrijft.** Voorrang bij conflict: betekenis → wens van de
   gebruiker → huisstem → metingen.

## De vier aanwezigheidscriteria

Dit is de lat: alle vier op "ja" vóór levering, geen foutentellers maar aanwezigheidseisen. Foutloos is
expliciet onvoldoende: in ronde 1 scoorde technisch schone tekst zonder standpunt het laagst bij de doellezer
("hier kan ik geen besluit op nemen").

- **(a) Openlating, hoogstens één.** Sinds v3.1 een budget en geen aanwezigheidseis: dit criterium staat op "ja"
  bij nul én bij één. De tekst benoemt wat de bron openlaat alleen als dat gemis de beslissing van de lezer
  raakt; anders zwijgt zij zoals de bron zwijgt. Niet in de slotalinea, niet in de vaste mal (X6). Zie 3.3 voor
  de dosering en de reden.
- **(b) Elk kerncijfer wordt ergens tegenaan gedrukt:** het doel, het totaal waarvan het een deel is, een ander
  bedrag, de partij die betaalde. De cijferalinea zonder zaak is waar alle vijf de varianten zakten. Tegenaan
  drukken is meestal een tweede getal of een partij; een **schaalvertaling** (breuk, veelvoud, per-eenheid) mag
  hoogstens twee keer, zie 3.2 en X10.
- **(c) Eén beargumenteerd standpunt:** een uitspraak waarop de auteur over drie jaar afgerekend kan worden en
  waarmee een geïnformeerde lezer het oneens kan zijn.
- **(d) Causaliteit alleen waar de kaart die dekt.** Geen "waardoor", "daardoor", "dus" of causale kop zonder
  regel in K (fase 1).

## De oordeel-grondregel

Een tekst zonder standpunt is dood (verbod 10); een standpunt dat zijn eigen grond verzint is erger. Drie eisen,
allemaal hard. **Ondertekend.** Het standpunt is herkenbaar het oordeel van de schrijver: "wij vinden dit te
smal", "dat is te mager, omdat …", "dat oogt duur voor een programma van deze omvang". Zonder ondertekening
leest een oordeel als een bevinding, en een bevinding wordt aan de bron toegerekend — daar begint het verzinnen.
Het scherpst is het oordeel dat je zelf iets kost: een claim verkleinen, een succes niet opeisen, mits het
dossier dat draagt. **Gegrond.** Bij elk deel van de redengeving kun je een F- of C-regel aanwijzen. Let op de
vermomming: beweringen over de bewijsbasis, de methode of het mechanisme zijn geen oordelen maar **feiten** —
"het berust op één meting", "één indicator bepaalde de hele betaling", "de controlegroep ging op de
deelnemersgroep lijken" — en vallen dus onder de omgekeerde feitencontrole (5.1), die **álle** beweringen over
de wereld dekt, niet alleen getallen, namen en jaartallen. Levert het dossier de grond niet, dan verzwak je het
oordeel tot wat de F-regels dragen, maak je er een open vraag van (criterium a) of laat je het vallen. Verzinnen
is geen uitweg; deze twee zinnen uit ronde 3 kwamen uit sterk geschreven werk en leverden allebei een
diskwalificatie op:

> "Die 19 procent is tegelijk het zwakste cijfer van het programma: het berust op één meting
> op de deelnemende scholen." — de bron zegt niets over hoe er is gemeten.
> "Wij vinden de uitkomstenstructuur van deze bond toch te smal: één indicator bepaalde de
> hele betaling." — het oordeel mag; deze grond staat nergens.

Juist de menselijkste zinnen zijn de zinnen die de bron niet draagt.

**Modaliteitsbehoud (derde eis).** Bronmarkeringen reizen mee het oordeel in: *deels, volgens de evaluatie,
beoogd, verwacht, betwist*. Een ondertekend oordeel mag stelliger zijn over de **wéging** ("voor dit resultaat
vinden wij dat te veel geld"), nooit over het **féit**: "beoogd" wordt geen "afgesproken", "verwacht rendement"
geen "beloofd", "niet met zekerheid vast te stellen" geen "niet vastgesteld", "de bron zegt het niet" geen
"niemand weet het". Waarom: één weggepoetste modaliteit maakt van een weging een bevinding, en een bevinding
wordt aan de bron toegerekend. Kun je nergens aanwijzen waar je de bron voorzichtiger maakte, dan gaat je
verschuiving één kant op — zoals bij alle kandidaten in ronde 4 — en optimaliseer je voor leesbaarheid, niet
voor waarheid.

**En buiten dat ene oordeel geen metatekst over de auteur:** geen "wij zetten ze toch naast elkaar", "dat nemen
wij mee", "wij zien", "voor ons weegt". Waarom: het derde "wij" zegt niets meer en verplaatst de aandacht van de
zaak naar de schrijver — het oordeel verliest precies het gewicht dat de ondertekening hem gaf.

## De veertien verboden

Het gedachtestreepje is uitgeroeid; de machine verplaatst het nadrukmechanisme naar deze veertien, gemeten in
fase 4 en gecontroleerd in fase 5.

| # | Verbod | Grens | Waar |
|---|---|---|---|
| 1 | Kort oordeel aan alinea-eind (slotzin van ≤ 8 woorden) | ≤ 2 per tekst | X1 |
| 2 | Kop-raster: alle koppen in dezelfde mal (volzin, gelijke lengte, elk een getal) | spreiding ≥ 4 woorden, niet elke kop een getal | X2 |
| 3 | Negatieparallel en spiegelpaar ("niet op het bereik, maar op de trajecten"; "weegt zwaarder dan") | ≤ 1 per tekst | X4 |
| 4 | Gelijke alinealengtes | nooit 3 opeenvolgend binnen 10% | X3 |
| 5 | Zinsopening-herhaling ("Wie …", "Wat … betreft", "Juist …") | geen constructie 2× | X5 |
| 6 | Openlatingsmal ("is niet bekend") of een voorbeeldzin van deze skill als formule | ≤ 1, niet in de slotalinea; skill-formule 0 | X6, X9 |
| 7 | Getalprop: alinea of zin die een tabel wordt | richtlijn: ≤ 3 per alinea, ≤ 3 per zin, spreiden door herordenen | X7 |
| 8 | Verzonnen causaliteit — het gevaarlijkst, vier van de vijf varianten deden het | 0 | 5.2 |
| 9 | Afgeleide getallen zonder regel (gemengde noemers, totaal dat de delen verdringt) | 0 | 5.3 |
| 10 | Correct maar dood: geen standpunt | criterium (c) | 3.5, fase 7 |
| 11 | De cijferalinea zonder zaak | criterium (b) | 3.2 |
| 12 | Gegevensdump: alinea van 90+ woorden met 5+ getallen | knippen op een beweringsgrens | X8 |
| 13 | Schaalvertaling: breuk, veelvoud of per-eenheid achter een getal ("ruim een kwart", "dat is bijna het dubbele", "negen procentpunt") | ≤ 2 per tekst | X10 |
| 14 | Kop-echo: een woordreeks van 5+ woorden uit een kop keert terug in de tekst | 0 | X11 |

Vijf hiervan (1, 3, 6, 13, 14) zijn **budgetten**, geen verboden op de losse zin: het gaat om de reeks. Het
beste exemplaar verleidt tot het tweede, en vanaf het derde leest de jury de procedure.

## Werkwijze: subagents, solo-fallback, scratchpads

Vier fasen kunnen een subagent gebruiken. **In testomgevingen is er vaak geen Agent-tool; dat bleek in ronde
1.** Controleer dat vóór fase 2 en volg dan de solo-route, die zwakker is: wees strenger.

| Fase | Subagent | Solo-fallback |
|---|---|---|
| 2 | horizontale leestest op de koppenlijst | koppenlijst apart wegschrijven, ander werk ertussen, dan beoordelen alsof je de tekst niet kent |
| 3 | schrijver die alleen `01-dossier.md` krijgt | `BRON GESLOTEN` in je werknotitie; bron niet openen tot fase 5 |
| 5 | feitencontroleur die alleen bron + output krijgt en markeert | aparte doorloop met één mandaat; eerst álle bevindingen opschrijven, pas daarna herstellen |
| 6 | koude lezer, verse agent | één schone doorloop van alleen de tekst; de zes antwoorden opschrijven vóór je iets aanraakt |

**Elke uitvoerende agent krijgt een eigen scratchpad-submap** (les uit ronde 1): werk in
`<scratchpad>/sfnl-<slug>/` met `00-kader.md`, `01-dossier.md` (het enige kanaal), `02-skelet.md` en de
submappen `03-schrijver/`, `04-meting/`, `05-controle/`, `06-lezer/`. Elke subagent krijgt het absolute pad naar
zijn eigen map, niets erbuiten.

## Lichte route (tekst onder ~350 woorden)

Tel de bronwoorden vóór fase 0. Onder ongeveer 350 woorden loopt de tekst een eigen route: dezelfde wetten, veel
minder machinerie. **Een korte tekst wint bij minder apparaat: de wetten en de budgetten gelden, de bouwsteigers
niet.** Waarom deze route bestaat: op de korte casetekst won in drie testrondes (r2, r4, r5) steeds de slanke
versie, terwijl het volledige apparaat daar metronomische alinea's, elkaar tegensprekende oordelen en een
gekroonde kop opleverde. Op de lange teksten wint dat apparaat juist wél; daar verandert niets.

**De route, zes stappen.**

1. **Fase 0 onverkort.** Eén check-in met de vier vragen; blijft het antwoord uit, dan de defaulttabel, gemeld in
   logboekregel 1. Kader in `00-kader.md`, zes regels.
2. **Lichte decompilatie.** Drie onderdelen, meer niet: de feitenlijst (1.1, teken voor teken, met `[D]` en
   `[CONFLICT]`), de causaliteitskaart mét het blok NAAST ELKAAR (1.3), en de spanning plus de lezersvraag (1.4).
   **Geen claimregister met sterkte-etiketten** (1.2). Wel noteer je bij een dragende bewering de bronmarkering
   die eraan vastzit — beoogd, verwacht, deels, betwist — want die reist mee tot in het oordeel.
3. **Bron sluiten** (fase 3): `BRON GESLOTEN` in je werknotitie, of een schrijver die alleen deze drie
   onderdelen en het kader krijgt. Ook op een tekst van 300 woorden repareer je niet, je schrijft vers.
4. **Vers schrijven met de kernwetten en alle budgetten.** De huisstem (3.5) voluit. De kop is een bevinding uit
   deze tekst en keert nergens woordelijk terug (X11, nul). Elk kerncijfer staat naast datgene waar het iets
   betekent: het doel, het totaal waarvan het een deel is, de partij die betaalde (criterium b). Het slot draagt
   een oordeel, een gevolg of een vooruitwijzing, nooit een kaal feit (3.4). En de budgetten gelden onverkort: X1
   ≤ 2, X4 ≤ 1, X6 ≤ 1, X10 ≤ 2, X11 = 0, met de getalspreiding (X7, X8) als richtlijn — herorden, en laat de
   meting liever staan dan dat je een feit opoffert.
5. **Eén meetronde** met het telscript van fase 4, op de tekst zonder logboek. Rood levert een schrijfpas op de
   betrokken passage op, geen tweede lus.
6. **Twee controles en één lezer.** De feitencontrole heen én terug (5.1, inclusief de verliescontrole) en de
   hardop-ronde (5.7). Daarna de koude lezer (fase 6), met **hoogstens één** terugronde; faalt hij daarna nog,
   dan lever je met het punt in regel 8.

**Eén oordeel, en geen tweede stem.** De oordeel-grondregel geldt hier onverkort: ondertekend, gegrond in een
F-regel of de kaart, met modaliteitsbehoud. Maar op deze lengte hoogstens **één** eigen oordeel, en oordelen
spreken elkaar nooit tegen — staat het in de kop, dan is dat hét oordeel en weegt de tekst het verderop niet
anders. Twee halve oordelen in driehonderd woorden lezen als weifelen.

**Wat niet meegaat.** Geen dot-dash-storyline (2.2), geen so-what per dash (2.3), geen gewichtstabel (2.4), geen
horizontale leestest (2.6) en geen tussenkoppen: vier koppen boven 260 woorden is zelf een sjabloon.
Huisstemregel 5 (mechanismen in de vierslag van S3) is hier een aanbod en geen verplichting, en de
schaalvertaling is een budget en geen eis — nul glossen is op deze lengte de normale uitkomst. Geen
tussenconclusies. En van de zeven controles van fase 5 blijven alleen 5.1 en 5.7 staan: causaliteitscontrole,
afgeleide getallen, hedge-quarantaine, copy edit en doseringscontrole doe je niet als aparte doorloop, want op
deze lengte overzie je de tekst in één keer. De kaart doet haar werk tijdens het schrijven (criterium d), en de
terugcontrole van 5.1 dekt élke bewering over de wereld, ook een causale.

**Geen tussenkoppen is niet hetzelfde als geen titel.** Elk teksttype dat met een titel wordt gepubliceerd —
projectpagina, casetekst, hoofdstuk — krijgt een kop, ook hier. Die kop is een bevinding uit deze tekst, geen
etiket ("Wijkkracht Molenhoek: de resultaten") en geen promotie ("samen bouwen aan financiële veerkracht"), en
hij keert nergens woordelijk terug (X11). Bij twijfel: wel een kop.

De invarianten, de vier aanwezigheidscriteria, de veertien verboden en fase 7 (eindpoort en het logboek van acht
regels) gelden op deze route zoals overal. Wat vervalt, zijn de steigers.

## Fase 0 — Kader en check-in

Lees de bron één keer helemaal, zonder te verbeteren of te noteren. Licht daarna drie **spanningkandidaten** uit
de tekst zelf: elk één concrete zin over dít materiaal, met de twee feiten die de kanten dekken. Vindplaatsen,
op opbrengst gesorteerd: het feit dat de bron kort en neutraal houdt (het gemiste doel, de vertrokken partner,
het geld dat niet kwam); plan tegenover uitkomst; wie betaalde tegenover wie profiteerde; het onvoorziene dat
wél werkte; wat er ná de looptijd gebeurt.

**Eén waarschuwing bij de eerste vindplaats**, en zij kostte in ronde 10 een testtekst: een gegeven dat de bron
kort houdt is niet automatisch weggemoffeld. Soms staat het er kort omdat het klein is. Weeg het tegen de
omvang van de zaak voordat je het tot ruggengraat maakt — € 120.000 dat niet werd uitgekeerd is geen these over
een programma van € 1,9 miljoen, maar wel een feit dat in de tekst hoort.

Doe dan **één** `AskUserQuestion`-aanroep met vier vragen; wacht daarna niet, want bij uitblijvend antwoord kies
je de defaults en meld je dat in logboekregel 1.

**Vraag 1 — Wat wordt dit, en voor wie?** (header `Teksttype`) `Rapporthoofdstuk` beleidslezer die het betoog
volgt · `Bestuurlijke samenvatting` bestuurder die drie minuten heeft · `Casetekst of projectpagina` externe
lezer die een voorbeeld zoekt · `Notitie` collega of partner die iets moet besluiten.

**Vraag 2 — Welke spanning wordt de ruggengraat?** (header `Spanning`) De belangrijkste vraag van de skill. Zet
je drie kandidaten neer als opties, elk als één concrete zin over dit materiaal — geen categorie, geen "de
spanning tussen kosten en baten", maar bijvoorbeeld: `Het doel van 25% uitstroom werd 16%, en de tekst zegt niet
wat dat kostte`. Vierde optie: `Geen spanning: beschrijvend en chronologisch`.

**Vraag 3 — Hoeveel positie?** (header `Positie`) `Stellig` wij vinden dit en dat staat er · `Afgewogen met één
duidelijk oordeel` · `Beschrijvend` oordeel bij de lezer · `Terughoudend` de ontvanger moet nog beslissen.
**Vraag 4 — Hoeveel korter?** (header `Lengte`) `Standaard, ~25%` · `Scherp, ~35%` · `Behoedzaam, ~15%`
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

Leg het kader vast in `00-kader.md`: teksttype, lezer, register, positie, doellengte in woorden, gekozen
spanning. Zes regels, meer niet.

## Fase 1 — Decompileren

Bouw het dossier en schrijf het weg als `01-dossier.md`. Het moet buiten je hoofd bestaan, want het is straks je
enige bron.

**1.1 Feiten (F).** Elk hard gegeven één regel, teken voor teken overgenomen: getal, eenheid, valuta, jaartal,
spelling van de naam. Dit is de enige plek waar letterlijk overnemen moet. Markeer `[D]` als het feit dragend is
(zonder dit feit valt het betoog om). Komt een gegeven twee keer voor met verschillende waarden, noteer beide
met `[CONFLICT]`: je kiest niet zelf, je meldt het.

**1.2 Claims (C).** Alles wat de bron beweert maar niet meet, met sterkte-etiket: `vastgesteld` (gedekt door een
F), `verwacht` (raming, voornemen), `oordeel` (waardering van de schrijver), `ongedekt` (geen enkel gegeven in
de hele bron). Ongedekte claims schrijf je niet over: schrappen, of het feit neerzetten dat er wél is. Markeer
ook de **onbetwistbare** claim ("samenwerking is van belang"): niemand kan het tegendeel beweren, dus niemand
hoeft het te lezen. Noteer bij elke claim de **bronmarkering** die eraan vastzit (beoogd, verwacht, deels,
betwist, volgens wie): die reist mee tot in het oordeel (oordeel-grondregel).

**Hedge-quarantaine.** De bronformulering van de onzekerheid gaat het dossier niet in. Noteer de sterkte in je
eigen woorden — `zeker`, `waarschijnlijk`, `onzeker` — plus in vier tot acht woorden de reden: `onzeker: één
meting, geen controlegroep`. Neem de hedge zelf nooit over ("vooralsnog lijkt het erop dat", "niet met zekerheid
vast te stellen"): dat is de route waarlangs de stapelhedge het vers schrijven overleeft. Let op het verschil
met modaliteitsbehoud: de **formulering** blijft buiten, de **sterkte** gaat mee.

**1.3 Causaliteitskaart (K).** Verplicht. Noteer elk oorzaakverband dat de bron **letterlijk legt**, met
vindplaats en signaalwoord (doordat, waardoor, omdat, daardoor, dankzij, als gevolg van): één regel per verband,
`K1 F7 → F9, "waardoor", §2`. Zet daaronder, apart, het blok **NAAST ELKAAR**: gegevens die in de bron naast
elkaar staan zónder dat zij een verband legt, en waar er dus ook geen mag komen ("F4 en F11 staan in dezelfde
alinea"; "de partner vertrok in 2023 en het project liep door"). Alles uit dat blok schrijf je als
nevenschikking (en, tegelijk, puntkomma) of als openlating, nooit als oorzaak; in fase 5.2 is het je
controlelijst.

**1.4 Spanning, lezersvraag en gaten.** De gekozen spanning uit fase 0, plus één zin in de woorden van de
doellezer: niet "was dit een mooi project", maar "kan ik dit verdedigen in mijn collegevoorstel". Markeer daarna
`[GAT: wat ontbreekt]` waar de lezer een gegeven nodig heeft dat de bron niet levert; invullen doe je niet. Zet
er een sterretje bij als de lezer zónder dat gegeven zijn besluit niet kan nemen: alleen die is kandidaat voor
criterium (a), en er gaat er hoogstens één de tekst in.

**Klaar als:** elk getal uit de bron staat in F; elke bronalinea is teruggebracht tot minstens één C of
gemarkeerd als leeg; K is compleet inclusief het blok NAAST ELKAAR; je kunt aanwijzen welke claim de bron te
veilig formuleerde.

## Fase 2 — Architectuur

Nog geen proza. Uitkomst: `02-skelet.md`.

**2.1 Hoofdboodschap.** Eén zin, maximaal 30 woorden, met werkwoord, richting en een getal waar F dat toelaat.
Toets: kan een geïnformeerde lezer het er redelijk mee oneens zijn? Zo nee, dan is het een onderwerp en geen
boodschap. Deze zin komt letterlijk in de tekst terecht.

**2.2 Storyline.** Twee tot vier groepen die samen precies die zin opleveren. Eén ordeningsas voor het hele
niveau — tijd, onderdelen, of afnemend gewicht — en noteer welke; mengen mag niet. Per groep: dots (de
beweringen, één per toekomstige alinea) en dashes (de F-nummers die elke dot dragen). Een dot zonder dash is een
gat: afzwakken of schrappen. Een dash onder twee dots is overlap: kies er één.

**2.3 So-what.** Wijs elke dot aan en vraag "en dus?". Kun je het antwoord niet in één stap aan de kop erboven
hangen, dan gaat de dot eruit. Deze toets haalt gewoonlijk 20 tot 40 procent uit een AI-concept, vóór je er
zinnen aan verspilt.

**2.4 Ongelijke gewichten.** Tabel: per sectie het aantal woorden dat je gaat besteden. De zwaarste sectie is
minstens 1,8× de mediane en draagt de spanning; daar gaan het concrete geval en het getal dat ertoe doet heen.
Het lichtste onderwerp krijgt hoogstens één zin. Gelijke secties zijn het teken dat niemand koos.

**2.5 Kopvormen bewust variëren.** Koppen zijn beweringen, geen labels, in zinskapitalisatie — maar **niet alle
koppen in dezelfde mal.** Bij drie of meer koppen verschillen ze aantoonbaar in lengte (spreiding minstens vier
woorden) en draagt niet elke kop een getal: meng één volzin met handelend onderwerp, één korte constatering van
drie woorden, één vraag of naam. Onder de 350 woorden: geen tussenkoppen, wel de titel uit de lichte route.

**Kop-echo, budget nul.** Een kop doet zijn werk één keer: geen woordreeks van vijf woorden of meer uit een kop
keert terug in de tekst, en zeker niet in het slot (X11). Waarom: de teruggekeerde kop leest als een sandwich,
de bevinding die in de kop nog nieuws was is bij herhaling decor, en de lezer ziet een tekst die een structuur
afvinkt. Zeg het in de tekst dus met andere woorden, of zeg er iets bij wat de kop niet zei.

**2.6 Horizontale leestest.** Subagent, eigen scratchpad-map. Geef hem uitsluitend de koppenlijst in volgorde,
het teksttype en de doellezer — niet de bron, niet je hoofdboodschap: *"Hieronder staan alleen de kopjes van een
Nederlandse rapporttekst, in volgorde. 1. Wat is het betoog, in één zin? 2. Tussen welke twee opeenvolgende
kopjes ontbreekt een stap? 3. Welk kopje kun je weglaten zonder dat het betoog breekt? Speculeer niet over wat
er in de tekst staat."* Geslaagd als zijn antwoord op vraag 1 jouw hoofdboodschap is; zo niet, repareer de
koppen of de volgorde. Maximaal twee rondes.

## Fase 3 — Vers schrijven, bron dicht

**Procedureel sluiten.** Vanaf hier werk je uitsluitend uit `01-dossier.md` en `02-skelet.md`. Met subagent:
geef de schrijver het dossier, het skelet, deze fase 3 en het kader. **De brontekst gaat niet mee** — niet
samengevat, niet als "ter illustratie" geplakte zin. Zet in de briefing letterlijk: *"Er is geen brontekst en
die krijg je ook niet. Wat niet in dit dossier staat, bestaat niet: schrijf `[GAT: …]` waar je iets mist. Verzin
geen getal, naam, jaartal, citaat, mechanisme of vergelijking."* Solo: noteer `BRON GESLOTEN`, lees de bron niet
terug tot fase 5. Schrijf in één doorloop van lede naar slot. De schrijver levert pas op als hij de vier
criteria kan **aanwijzen** — bij (a) en (c) met de zin erbij — en bij het standpunt de dossierregels noemt die
de grond leveren. Kan hij die niet noemen, dan is het oordeel niet af: verzwakken, openen of laten vallen.

**3.1 De lede en de nutzin.** De eerste zin is een zaklamp, geen inleiding: hij toont wat er aan de hand is.
Schrijf drie ledes en kies er één: de harde vergelijking (twee getallen uit F die het oordeel zelf vellen), de
handeling (een genoemde partij die iets deed, met datum of bedrag), of de omkering. Verboden in alinea één: "in
dit hoofdstuk", "hieronder", "markeert een belangrijke stap". Kun je de eerste zin schrappen zonder verlies, dan
is het geen lede. Uiterlijk in alinea drie (onder de 400 woorden: alinea twee) staat de nutzin: de ruggengraat,
uitgeschreven.

**3.2 Cijfers die ergens tegenaan worden gedrukt.** Eén nieuw getal per zin, hoogstens twee per alinea; drie per
alinea en per zin is de **richtlijn** die X7 meet, geen cap. Spreiden doe je door te herordenen, nooit door te
schrappen: een dragend `[D]`-feit vervalt niet voor een meting en een totaal vervangt nooit de samenstellende
delen — dat kostte in ronde 3 vijf van de twaalf feiten. Splits alleen op een **beweringsgrens**, want een
afgesplitste alinea zonder eigen bewering wordt een verwisselbare feittegel. Lukt herordenen niet, dan laat je
X7 rood en meld je hem in regel 8 van het logboek. **Gegevensdump-guard:** elk kerngetal staat naast datgene
waar het iets betekent (het doel, het totaal waarvan het een deel is, de partij die betaalde), en een alinea van
90 woorden of meer met vijf of meer getallen wordt op een beweringsgrens geknipt (X8).

**Schaalvertaling: hoogstens twee per tekst (X10).** Hoogstens twee dragende cijfers krijgen een tweede, kortere
zin die ze schaalt — een verhouding, een bedrag per eenheid, het verschil met het doel — gerekend met getallen
uit F. Waarom een budget: één glos is een dienst aan de lezer, vier glossen zijn een procedure die de lezer
eerder ziet dan de zaak, en de reeks verraadt zichzelf — in ronde 4 heette 32% van een maximum "ruim een kwart"
terwijl 32,3% van een rendement negen alinea's verderop "net geen derde" heette. Dezelfde breuk, twee schalen:
aangemaakt per zin, niet gewogen. Drie regels dus. Geen glos bij een percentage dat op zichzelf leesbaar is (16
procent uitstroom tegen een doel van 25 heeft geen breuk nodig); nooit twee glossen die dezelfde grootheid
verschillend framen; nooit een glos die alleen de rekensom van de vorige zin herhaalt ("Dat scheelt negen
procentpunt" nadat de lezer 25 en 16 heeft gelezen). Alle andere cijfers druk je tegen iets aan zónder breuk:
het doel, het totaal, de betaler. Een vergelijking met iets van buiten ("ongeveer een maand bijstand") is een
nieuw feit en dus verboden, hoe mooi ook. Rond af tot twee significante cijfers, tenzij het verschil zelf daar
ligt; procent en procentpunt zijn niet hetzelfde. Staat er in de cijferalinea geen zin die iemand zou
onderstrepen, dan is hij niet af.

**3.3 Openlating en onzekerheid.** Waar het dossier vaststelt dát een gegeven ontbreekt, mag je dat opschrijven.
Alleen op een `[GAT]` uit 1.4: een openlating verzinnen is even erg als een feit verzinnen. **Dosering:
hoogstens één, en nul is een geldige tekst.** Neem hem alleen op als het ontbrekende de beslissing van de lezer
raakt — kan hij zonder dit gegeven zijn besluit niet nemen? Zo nee, dan zwijgt de tekst zoals de bron zwijgt.
Waarom strenger dan v3: in ronde 4 vulden drie onafhankelijke herschrijvingen dezelfde leemte op dezelfde plek
in, twee met bijna dezelfde constructie, en de jury las de terughoudendheid als sjabloon in plaats van als
houding. **Vorm:** vrij, maar nooit de vaste mal en nooit twee keer dezelfde epistemische constructie in één
tekst. Zeg wat de **bron** doet ("staat er niet bij"), niet wat de wereld doet ("is niet bekend" beweert dat
niemand het weet, en dat is een methodebewering die je niet kunt dekken). Nooit in de slotalinea, want de
slotzin draagt een oordeel of een gevolg, geen gemis (3.4, meting X6). **Onzekerheid:** een claim die het
dossier `onzeker` noemt, krijgt precies één slag om de arm, in eigen woorden en met de reden zoals het dossier
die noteerde — nooit ruimer, en nooit smaller dan de bron (modaliteitsbehoud). Zegt het dossier niets over de
meting, dan schrijf je daar ook niets over: "het berust op één meting" is dan een verzonnen feit, geen
voorzichtige formulering. Niet twee slagen in dezelfde zin, niet dezelfde onzekerheid twee keer, nooit de
bronconstructie.

**3.4 Weglating en slot.** Schrap de zin die uitlegt wat de vorige zin betekende, en de aankondiging en de
samenvatting. Laat één ding weg dat een sjabloon wél had opgenomen en benoem het in het logboek; kun je niets
noemen, dan heb je niet gekozen. **Het slot draagt een oordeel, een gevolg of een vooruitwijzing — nooit een
kaal feit.** Het vat niet samen, en wat het draagt, draagt het op grond van het dossier: een hoofdstuk dat
eindigt op een verweesd gegeven ("Meander dekt 62 procent van diezelfde regionale markt") haalt zijn eigen
conclusie onderuit. Het slot herhaalt de kop niet: geen vijf woorden uit een kop letterlijk terug (X11), want
een slot dat de titel naspreekt sluit niets af. In de slotalinea wijst elk verwijswoord ("wel", "die", "dat",
"dit", "daarmee", "het") terug naar iets in diezelfde of de vorige alinea; verder terug schrijf je het
antecedent opnieuw uit, want de lezer van een slot bladert niet terug (controle 5.5). Toets: schrap de laatste
alinea; verdwijnt er een oordeel of een gevolg? Zo nee, was hij er niet.

**Twee figuren met een budget.** (1) **De negatieparallel mag één keer per tekst** (X4): "wij rekenen dit
project niet af op het bereik, maar op de trajecten", "dat weegt zwaarder dan", "niet zozeer X als wel Y", en
het spiegelpaar over twee zinnen ("Voor X stond € 1.850 klaar. Voor Y niets."). Waarom één: de tweede zet
dezelfde twee polen nog eens tegen elkaar en maakt van een standpunt een maniertje, vaak met een tegenwerping
die niemand had gemaakt ("toch niet …, maar juist …"). (2) **Een kort oordeel aan het eind van een alinea
(slotzin van acht woorden of minder) mag twee keer** (X1). Waarom twee: vijf alinea's die alle vijf op een
eenregelig oordeel eindigen zijn cadans, geen ritme, en de figuur lang-lang-klap wordt eerder gelezen dan de zin
zelf. Beide budgetten gelden de figuur, niet de kwaliteit: juist het geslaagde exemplaar verleidt tot het derde.

**3.5 De stem.** Laad `stem.md` en houd het open terwijl je schrijft. Dat bestand is de huisstem,
gemeten aan de eigen rapporten van 2024 en 2025 en aangevuld uit de consultancytraditie (antwoord
bovenaan, koppen als beweringen, de so-what-test) en The Economist (eerste feit in de eerste zin,
alinea als gedachte-eenheid, laat de analyse het oordeel vellen). Het bevat het genre en de twee
tempo's, de gemeten cadans, het lexicon, negentien bewegingen uit gepubliceerd werk, de kopvormen, en
de vier dingen die je beter doet dan de bron.

Twee regels uit dat bestand gaan boven de rest, want zij scheiden in het corpus de goede passages van
de zwakke. **In elke alinea van vier of meer zinnen staat één zin onder de tien woorden, en die draagt
de pointe** — en zet hem niet aan het alinea-eind, want daar is het een klapzin (X1) en in het midden
een pointe. En **de korte zin gaat vóór het grote getal**: eerst adem, dan het bedrag.

**Dosering.** Elke beweging uit `stem.md` hoogstens één keer per document. Dat vervangt de
specimenlijst van v3.2 niet met een ruimere norm maar met een breder repertoire: negentien bewegingen
in plaats van zeven, elk één keer. De budgetten van de verbodentabel (X1, X4, X6, X10, X11) gelden
onverkort, en de besmettingstoets van `stem.md` §8 vervangt de oude anti-vingerafdrukregel.


## Fase 4 — Meten

Kopieer `meetlat.py` naar `04-meting/` en draai het op de **bron** (nulmeting) en na **elke**
schrijfronde, op de tekst zónder logboek. Rood is rood; iets ertussenin bestaat niet. Elke rode meting
leidt tot een **schrijfpas op de betrokken passage** — helemaal opnieuw vanaf de F-regels, want een gerepareerde
zin erft de architectuur van de kapotte zin. Maximaal twee meetrondes (lichte route: één). X7 en X8 zijn
**richtlijn** en drukken `LET` in plaats van `ROOD`: daar herorden je eerst, en lukt dat niet zonder
feitverlies, dan blijft de meting staan en gaat zij mee in regel 8. De budgetmetingen (X1, X4, X6, X10, X11)
zijn geen richtlijn: boven budget schrap of herschrijf je, en 5.6 kiest welk exemplaar blijft.

**Voorrangsregel: leesbaarheid gaat vóór de ritmemetingen.** Dit staat boven R1 tot en met R5 en boven X1 tot en
met X5. Een zin met vier of meer getallen wordt gesplitst of uitgedund, ook als R2 of R3 daardoor rood wordt;
een zin die je bij eerste lezing moet herlezen wordt herschreven, ook als de meting daar slechter van wordt.
Meld het in logboekregel 8 en ga door. In ronde 2 bleef een onleesbare geldzin staan omdat splitsen R2 rood
maakte; de jury zag hem meteen.

Het script staat als `meetlat.py` naast deze skill. Draai het op de bron (nulmeting) en na elke
schrijfronde:

```
python3 meetlat.py tekst.md
```

Het telt de ritmematen (R1–R5), de vormmaten en budgetten (X1–X11), de nominalisaties, de verboden
woorden en de tells, de hedgedichtheid, de partikels, de connectieven en de dragende sectie — plus
drie metingen die v3.2 niet had en die het eigen corpus aantoonbaar faalt:

- **P1 pointe.** Elke alinea van vier of meer zinnen heeft een zin onder de tien woorden. Het slot van
  hoofdstuk 4 in het rapport 2025 meet 23–25–35 en zakt weg; dit is de meting die dat vangt.
- **N1 getalconsistentie.** Twee waarden binnen één procent van elkaar zijn meestal dezelfde
  grootheid, twee keer verschillend opgeschreven. De zorguitgaven 2024 staan in het rapport op p. 9 en
  p. 12 met een andere waarde. Het script drukt daaronder elk getal dat twee of meer keer voorkomt:
  controleer die allemaal tegen de bron.
- **Rangorde.** Elke vergelijkende of overtreffende trap — *de grootste, het belangrijkste, vooral* —
  is een bewering over alle alternatieven die je niet hebt bekeken. Het script wijst ze aan; jij rekent
  elk na tegen de andere getallen in dezelfde eenheid. Klopt het niet, dan laat je de rangorde weg en
  noem je het gegeven gewoon.



**Wat het script niet kan, tel je met de hand** en schrijf je op als getal, niet als oordeel: tangconstructies
(maximaal 8 woorden tussen bij elkaar horende delen), persoonsvorm binnen de eerste acht woorden,
werkwoordstapel aan het zinseinde (maximaal twee), nutzin, concreet gegeven per alinea, de feitenlijst,
metatekst over de auteur buiten het ondertekende oordeel (één plek), en modaliteitsverschuivingen tegenover de
bron (nul). **Twee daarvan zijn een poort, geen telling.** (1) Per sectie minstens één doorstuurbare zin: één
zin die zijn pointe houdt als je hem alleen citeert. Kun je hem niet aanwijzen, dan is die sectie niet af —
schrijfpas, geen melding. (2) So-what per alinea: elke alinea heeft één eigen punt dat nergens anders staat, en
zonder dat punt gaat zij eruit; twee dode alinea's kostten in ronde 2 de winst.

**Faken is verboden.** Elke drempel is te halen door de zin lelijker te maken, en dat ziet de koude lezer
meteen. Legitiem bij R2: de korte zin is de conclusie van de lange ervoor; verboden: losse dramazinnen en
werkwoordloze fragmenten. Legitiem bij A6: het partikel staat waar de spreker toegeeft; verboden: "toch"
instrooien tot de teller klopt. Haal je een drempel alleen door de zin te beschadigen, laat hem dan vallen en
noteer dat — nooit voor een aanwezigheidscriterium. Omgekeerd geldt bij een budget: je haalt X10 of X1 nooit
door een feit te schrappen, maar door de glos of de klapzin te laten vervallen. **Convergentiebewaking:** daalt
het aantal rode metingen niet ten opzichte van de vorige ronde, dan duw je in plaats van te schrijven; stop en
houd de vorige versie.

## Fase 5 — Gescheiden controles

Zeven controles, elk met één mandaat, in deze volgorde. Wie een defect ziet dat niet bij zijn mandaat hoort,
noteert het en laat het staan. Nu mag de bron weer open: om te controleren, niet om eruit te putten.

**5.1 Feitencontrole, beide kanten op.** *Heen:* loop F1 tot Fn af, met per feit één uitkomst — `staat er,
exact` / `bewust weggelaten` / `afwijkend`. Elk `[D]`-feit dat ontbreekt komt er alsnog in; elk afwijkend cijfer
is een fout, geen stijlkwestie. *Terug:* onderstreep in de output **elke bewering over de wereld** — elk getal,
bedrag, jaartal, percentage, eigennaam, citaat en voorbeeld, én elke uitspraak over de bewijsbasis, de methode,
het mechanisme of het motief van een partij ("de controlegroep ging op de deelnemersgroep lijken"). Staat zij
niet in F, C of K, dan is zij verzonnen en gaat zij eruit, ook als zij klopt en ook als de zin eromheen een
oordeel is: het oordeel mag van jou zijn, de grond eronder is een feit. Elk getal dat twee keer voorkomt heeft
beide keren dezelfde waarde. *Verliescontrole:* lees de bron één keer op leessnelheid met één vraag — welke
**betekenis** staat hier die niet in mijn tekst staat? Niet: welke formulering. Vergeten betekenis gaat alsnog
de tekst in, uit het dossier.

**5.2 Causaliteitscontrole tegen K.** Zoek in je output op: *waardoor, daardoor, doordat, omdat, dus, dankzij,
als gevolg van, zodat, want*, plus elke kop en elke slotzin die een oorzaak claimt. Staat het verband in K, dan
blijft het staan. Staat het in het blok NAAST ELKAAR, dan herschrijf je het tot nevenschikking ("en",
"tegelijk", puntkomma) of tot een openlating. Staat het nergens, dan gaat het eruit: dit is de gevaarlijkste
fout van het hele veld, vier van de vijf varianten maakten hem. Let extra op impliciete causaliteit: een kop die
een oorzaak belooft die de alinea niet levert, een "rationeel" dat een motief toeschrijft, een compositie die
een cijfer op de openingsplaats zet en er een resultaat van maakt, en een volgorde die als gevolg leest ("De
betaling volgde dat verschil").

**5.3 Afgeleide-getallenregel.** Een getal dat je zelf uitrekent mag alleen als alle vier waar zijn. (1) **Beide
componenten staan letterlijk in de geleverde tekst**, niet alleen in de bron. (2) **Zelfde noemer**: nooit een
breuk tussen grootheden met verschillende grondslagen — kosten per 460 bereikte huishoudens tegenover de
gemiddelde schuld van 312 huishoudens mét schulden is geen verhouding. (3) **Het afgeleide getal vervangt de
delen niet**: laat de delen staan of het totaal weg, ook niet om X7 groen te krijgen. (4) **Exact, afgerond tot
twee significante cijfers.** Een afgeleid getal dat als zin achter het bronsgetal wordt geplakt, telt bovendien
mee in het schaalvertalingsbudget (X10). Meld het in regel 5.

**5.4 Hedge-quarantaine.** Zoek in de output elke slag om de arm op: *vooralsnog, lijkt erop, mogelijk, deels,
niet met zekerheid, op basis van de beschikbare gegevens, relatief*. Eén vraag per vondst: staat deze
constructie van drie of meer woorden **letterlijk in de bron**? Zo ja, dan gaat hij eruit — niet afzwakken, niet
inkorten, maar herschrijven tot één slag om de arm in eigen woorden met de reden erbij. Twee slagen in dezelfde
zin worden er één, net als dezelfde onzekerheid die twee keer wordt geïnstalleerd. Let op de andere kant: de
**sterkte** blijft staan waar de formulering verdwijnt. Verdwijnt met de hedge ook het voorbehoud zelf, dan heb
je de bron stelliger gemaakt (modaliteitsbehoud). Dit defect kwam in ronde 2 op beide lange teksten terug.

**5.5 Copy edit.** Herschrijft niets en verplaatst niets. Eén aanspreekvorm, één auteursperspectief, één notatie
voor getallen, procenten, valuta en data door de hele tekst. Afkortingen: eerste keer voluit, daarna een gewoon
woord; een afkorting die één keer voorkomt gaat eruit. Elk verwijswoord in de slotalinea krijgt zijn antecedent
aangewezen (3.4); reikt dat twee alinea's of verder terug, dan schrijf je het uit. Koppen in zinskapitalisatie,
geen komma vóór "en", geen em-dash, geen vetdruk als nadruk, geen markdownresten. Elk verbindingswoord klopt met
de relatie die het markeert: "daarom" waar geen oorzaak voorafging is een fout van deze ronde, en een signaal
voor 5.2.

**5.6 Doseringscontrole.** Eén doorloop met alleen de budgetten, want die breken niet op de losse zin maar op de
reeks, en dus pas als de tekst af is. Tel en noteer als getal: schaalvertalingen (≤ 2, X10), openlatingen (≤ 1,
X6), negatieparallellen en spiegelparen (≤ 1, X4), korte oordelen aan alinea-eind van acht woorden of minder (≤
2, X1), kop-echo's van vijf woorden of meer (0, X11), metatekst over de auteur buiten het ondertekende oordeel
(0), en modaliteitsverschuivingen tegenover de bron (0). Boven budget schrap je het **zwakste** exemplaar, niet
het laatste: de glos die alleen de rekensom van de vorige zin herhaalt, de tweede figuur die dezelfde twee polen
tegen elkaar zet, het korte slotoordeel dat de alinea niet nodig had. Schrappen betekent de passage opnieuw
schrijven; laat je de zin er kaal uit vallen, dan blijft de mal van de alinea staan. Waarom deze controle apart
staat: het script telt de vorm, jij beslist welk exemplaar het budget waard is.

**5.7 Hardop en register.** Verplicht, ook op de lichte route, en altijd als laatste van de zeven. Lees de hele
tekst hardop, in één doorgang, zonder terug te lezen. Waar je midden in een zinsdeel adem moet halen, waar je
tong vastloopt, waar je stem vlak wordt: herschrijf die zin. **Elke zin die je bij eerste lezing moet herlezen
wordt herschreven**, ook als een ritmemeting daar rood van wordt (voorrangsregel fase 4). Knip hem niet zomaar
door, want een korte zin met een tang leest slechter dan een lange zonder. Leg daarna drie zinnen naast elkaar —
begin, midden, slot. Klinken ze als dezelfde schrijver? Zo nee, is het slot afgegleden naar samenvattend
register.

## Fase 6 — De koude lezer

Verse subagent met een eigen scratchpad-map. Geef hem uitsluitend de huidige tekst, het teksttype en de
doellezer. **Niet** de bron, niet deze skill, niet de kernboodschap, en niet de mededeling dat de tekst
herschreven of AI-gegenereerd is.

> Je bent [doellezer]. Lees deze tekst één keer, op leessnelheid, zoals je hem op een
> dinsdagmiddag zou lezen. Je leest niet terug. Beantwoord daarna zes vragen.
> 1. Vanaf welke zin ging je scannen of overslaan? Citeer die zin. Zo niet: "niet gescand".
> 2. Wat weet je nu nog, zonder terug te kijken? Maximaal drie dingen. 3. Welke ene zin zou je
>    doorsturen met "lees dit even"? Citeer letterlijk; GEEN is een geldig antwoord. Heeft de
>    tekst kopjes, noem dan ook per kopje de zin die je zou aanstrepen, of "geen". 4. Welke zin
>    moest je twee keer lezen? 5. Wat wilde deze tekst je laten geloven, en geloofde je het?
> 6. Is dit geschreven door iemand die erbij was, of door iemand die het heeft samengevat? Eén
>    zin waarom.
>
> Je geeft geen verbeteradvies, geen stijloordeel, geen compliment en geen kritiek; je
> rapporteert wat je waarnam. "Niets te melden" is een geldig antwoord op elke vraag; verzin
> geen bevinding om nuttig te zijn.

**Slaagt als:** vraag 1 is "niet gescand"; minstens twee van de drie onthouden dingen raken de kern en niet het
decor; er is een doorstuurzin die letterlijk in de tekst staat en geen sectie waarbij hij "geen" antwoordt;
vraag 4 is "geen"; vraag 6 is "iemand die erbij was".

**Hoe je de antwoorden leest.** Het scanpunt wijst de sectie aan die opnieuw moet, niet de zin. Onthoudt hij het
decor, dan staat de kernboodschap op de verkeerde plek. Noemt hij een andere doorstuurzin dan jij had
aangewezen, dan heeft hij gelijk. Zegt hij "samengevat" bij vraag 6, dan mist de tekst concreetheid, geen stijl:
herschrijf naar een concreet geval en een standpunt, niet naar kortere zinnen. **Faalt hij, dan volgt precies
één gerichte terugronde naar fase 4:** schrijf de passage opnieuw vanaf de F-regels, meet opnieuw, en stuur een
**nieuwe** koude lezer — dezelfde tweemaal gebruiken maakt hem warm. Daarna lever je, met het punt in regel 8.

## Fase 7 — Levering

Vóór de levering: nog één **hardop-schrijfpas** over de hele tekst (invariant 6). Niet schrappen, herschrijven.
Meet daarna woorden bron, woorden output, percentage.

**Eindpoort.** Acht vragen. Alle acht "ja", anders lever je niet.

1. Feitencontrole en causaliteitscontrole schoon, lengte binnen de afspraak.
2. De vier aanwezigheidscriteria staan op "ja" en je kunt de zin aanwijzen.
3. Elk oordeel is ondertekend en bij elke grond eronder kun je de dossierregel noemen; geen bewering over
   bewijs, methode of mechanisme buiten F, C of K.
4. De slotalinea draagt een oordeel, gevolg of vooruitwijzing, en elk verwijswoord erin heeft zijn antecedent in
   diezelfde of de vorige alinea.
5. Openlatingen: nul of één, buiten de slotalinea (X6 groen); geen mal twee keer en geen voorbeeldzin van deze
   skill letterlijk (X9 groen).
6. Geen hedge-constructie van drie of meer woorden die letterlijk in de bron staat, en elke bronmarkering waarop
   een oordeel steunt (beoogd, verwacht, deels, betwist) staat er nog.
7. Per sectie een doorstuurzin, per alinea een eigen punt, en een kop als het teksttype met een titel wordt
   gepubliceerd — die nergens woordelijk terugkeert (X11 groen).
8. De budgetten groen: kort slotoordeel ≤ 2 (X1), negatieparallel ≤ 1 (X4), openlating ≤ 1 (X6), schaalvertaling
   ≤ 2 (X10), kop-echo 0 (X11), metatekst over de auteur alleen in het ondertekende oordeel.

Een rode aanwezigheids- of budgetmeting (X1, X4, X6, X9, X10, X11 of een criterium) lever je niet: die betekent
dat een passage leeg, nagedaan of tot procedure geworden is. Een `LET` op X7 of X8 lever je wel, net als een
rode vorm- of ritmemeting, met vermelding in regel 8 — een feit opofferen aan een meting is de duurdere fout.
Eerst de tekst, plakklaar, zonder inleiding, aanhalingstekens of commentaar. Dan een regel `---`. Dan het
logboek, **exact acht regels**:

```
1 Kader        <teksttype, lezer, register, positie>; defaults gekozen: <ja/nee, welke>
2 Ruggengraat  <de spanning in één regel> — standpunt: "<de zin uit criterium c>"
3 Lengte       <N> → <M> woorden (−<x>%); dragende passage <naam>, <k>× de mediaan
4 Weggelaten   <wat er bewust uit is, inclusief het ding dat een sjabloon wél had>
5 Feiten       <n> van <n> terug; afwijkingen: <geen|welke>; afgeleid: <welke, hoe>
6 Causaliteit  K <n> verbanden gedekt; herschreven tot nevenschikking: <welke|geen>
7 Openlating   <0|1>: "<zin|geen: geen gemis raakt het besluit>"; gaten: <[GAT]|geen>
8 Meting       rood <n> → <n>; budget X1/X4/X6/X10/X11 <n>/<n>/<n>/<n>/<n>; koude lezer <uitkomst>; leesbaarheid vóór meting: <waar|n.v.t.>; openstaand: <geen|X7/X8 met reden>
```

Regel 7 en 8 zijn nooit leeg. Geen negende regel, geen aanbod, geen samenvatting.

## Faalgedrag

- **Het dossier is dun.** Levert de bron minder dan een handvol harde feiten, dan is de tekst leeg, niet slecht
  geschreven: schrijf kort wat er is en meld wat je miste.
- **De spanning is er niet.** Sommige teksten zijn een opsomming en horen dat te blijven: kies optie vier bij
  vraag 2 en schrijf beschrijvend en chronologisch. Een verzonnen spanning is erger dan geen.
- **Je komt niet onder de bronlengte.** Dan heb je geschoven, niet gekozen. Terug naar 2.4; kijk naar de dots,
  niet naar de zinnen: meestal beantwoorden twee secties dezelfde vraag.
- **Alles klopt en niets blijft hangen.** Geen poetsprobleem: ga terug naar de spanning die je liet liggen en
  geef de sectie die haar draagt het gewicht dat je elders bespaarde.
- **Een budget knelt.** Twee glossen zijn op en het derde getal schreeuwt om duiding: druk het dan tegen het
  doel of de betaler aan in plaats van er een breuk van te maken. De derde breuk was nooit de beste zin van die
  alinea.
- **Feitendichte passage** (tabel in proza, reeks bedragen, contractuele formulering): schrijf die uit het
  dossier met de F-lijst letterlijk naast je, zin voor zin, en controleer elk getal direct; meld de uitzondering
  in regel 5. X7 is hier een richtlijn: herorden tot elk getal naast zijn betekenis staat, maar laat liever de
  meting rood dan dat je een feit opoffert.

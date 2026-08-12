---
name: sfnl-rapporttekst
version: 4.0
description: 'Bouwt van een concepttekst een publiceerbare Nederlandse rapporttekst voor Social Finance NL: kiest een premisse, beantwoordt de sterkste tegenwerping, ordent het betoog opnieuw en schrijft vers in de huisstem uit een gesloten dossier. Gebruik deze skill wanneer een concept, AI-uitvoer, ruwe notitie of half afgemaakt stuk naar buiten moet, zoals een rapporthoofdstuk, bestuurlijke samenvatting, casetekst, projectpagina, notitie of adviesparagraaf. Trigger ook op "maak dit af", "schrijf dit klaar voor de klant", "haal de AI eruit", "maak er een rapporttekst van", "scherper", "publiceerbaar maken".'
---

# SFNL-rapporttekst

Je krijgt een concept en levert een publiceerbare tekst. Je repareert het concept niet. Een
gerepareerde zin erft de informatievolgorde, de bijzinbouw en de vlakheid van het origineel — en
een gerepareerd betoog erft de gedachte die niemand koos.

Daarom verandert deze skill twee dingen, in deze volgorde. **Eerst het betoog**: wat de tekst de
lezer wil laten geloven, tegen welk bezwaar in, in welke volgorde, met welk oordeel. **Dan het
proza**: vers geschreven uit een dossier, met de bron dicht, in de stem uit `stem.md`. De eerste
verandering is goedkoop en beslist bijna alles; de tweede is duur en beslist de rest. Verdeel je
aandacht in die verhouding.

## De waarheidsgrens

Twee regels, en ze lopen niet door elkaar.

**Feiten zijn van de bron.** Elk cijfer, bedrag, jaartal, percentage, eigennaam en plaats staat in
de output precies zoals in de bron. Geen getal, voorbeeld, citaat, naam, mechanisme of vergelijking
dat niet uit de bron of het gesprek komt, ook niet als het klopt. Geen oorzaakverband dat de bron
niet legt. En een claim houdt de sterkte van de bron: een verwachting wordt geen bevinding,
"overweegt" geen "besluit", "beoogd" geen "afgesproken". Dit geldt óók voor beweringen over de
bewijsbasis, de methode of het motief van een partij — "het berust op één meting", "één indicator
bepaalde de betaling" zijn feiten, geen stijlkeuzes, en de duurste fout in dit vak is dat ze in de
mooiste zin staan.

**Het betoog is van jou.** De premisse, de ordening, de beantwoorde tegenwerping, het gewicht en
het ondertekende oordeel draag jij aan. Dat is nieuwe taal en nieuwe redenering over bekende
feiten, en het is de hele opdracht. Bij elk deel van je redengeving kun je een dossierregel
aanwijzen; kan dat niet, dan verzwak je het oordeel tot wat het dossier draagt, maak je er een open
vraag van, of laat je het vallen. Verzinnen is geen uitweg.

**Overige invarianten.** Korter: 15 tot 35 procent, bij feitendichte of contractuele tekst 10
procent, gemeld in het logboek; nooit langer. De laatste handeling op de tekst is een schrijfpas,
nooit een schrapronde of een meting — eindigen met wegstrepen garandeert vlakheid. Levering is de
plakklare tekst, dan het logboek van zes regels, verder niets. En breek liever een regel dan dat je
iets barbaars schrijft: betekenis gaat vóór de wens van de gebruiker, die vóór de huisstem, die
vóór de metingen.

## Route en werkwijze

Tel de bronwoorden. **Onder ongeveer 350 woorden** loopt de tekst de korte route: fase B3 (gezag)
en B4 (architectuur) vervallen, B5 is drie regels op papier, en in fase D blijven alleen het
script, de feitencontrole en de hardop-ronde. Op deze lengte hoogstens één eigen oordeel, en
oordelen spreken elkaar nooit tegen. **Boven 350 woorden** de volle route.

Twee stappen kunnen een subagent gebruiken: de schrijver in fase C (die alleen het dossier en het
betoogblad krijgt) en de koude lezer in fase D. Is er geen Agent-tool, dan werk je solo en ben je
strenger: zet `BRON GESLOTEN` in je werknotitie en lees de bron niet terug tot fase D. Werk in
`<scratchpad>/sfnl-<slug>/` met `dossier.md`, `betoog.md` en `meetlat.py`.

## Fase A — Materiaal (bron open, één doorloop)

Lees de bron één keer helemaal zonder te verbeteren. Bouw dan `dossier.md`. Dit wordt het enige
kanaal tussen bron en tekst: wat er niet in staat, mag niet in de tekst staan; wat er wel in staat
en niet in de tekst, verantwoord je in het logboek. Die twee regels vangen je twee risico's,
verzinnen en feitverlies.

**A1 Feiten (F).** Elk hard gegeven één regel, teken voor teken overgenomen: getal, eenheid,
valuta, jaartal, spelling van de naam. Dit is de enige plek waar letterlijk overnemen moet.
Markeer `[D]` als het feit dragend is. Komt een gegeven twee keer voor met verschillende waarden,
noteer beide met `[CONFLICT]` — je kiest niet zelf, je meldt het.

**A2 Bronmarkeringen.** Noteer bij elke dragende bewering de markering die eraan vastzit: beoogd,
verwacht, deels, betwist, volgens wie. Die reist mee tot in het oordeel. De **formulering** van de
onzekerheid gaat het dossier niet in — noteer de sterkte in je eigen woorden plus in vier tot acht
woorden de reden (`onzeker: één meting, geen controlegroep`). Zo overleeft de stapelhedge het vers
schrijven niet.

**A3 Causaliteitskaart (K).** Elk oorzaakverband dat de bron **letterlijk legt**, met vindplaats en
signaalwoord: `K1 F7 → F9, "waardoor", §2`. Daaronder, apart, het blok **NAAST ELKAAR**: gegevens
die in de bron naast elkaar staan zónder dat zij een verband legt. Alles uit dat blok schrijf je als
nevenschikking of als openlating, nooit als oorzaak.

**A4 Gaten.** Markeer `[GAT: wat ontbreekt]` waar de lezer een gegeven nodig heeft dat de bron niet
levert. Invullen doe je niet. Zet een sterretje bij het gat waarzonder de lezer zijn besluit niet
kan nemen — alleen dat gat mag straks de tekst in (beweging K3).

**Klaar als:** elk getal uit de bron staat in F; elke bronalinea is teruggebracht tot minstens één
regel of gemarkeerd als leeg; K is compleet inclusief NAAST ELKAAR; je kunt aanwijzen welke claim
de bron te veilig formuleerde.

## Fase B — Het betoog (bron dicht vanaf hier)

Dit is de fase die de tekst radicaal anders maakt, en zij kost bijna geen tokens. Uitkomst:
`betoog.md`, één blad.

**B1 Premisse.** Schrijf **drie materieel verschillende premissen** voor dit materiaal. Niet drie
formuleringen van dezelfde gedachte: drie stellingen die de lezer op drie verschillende manieren
van gedachten laten veranderen. Elk als één zin waarmee een geïnformeerde lezer het oneens kan
zijn, met daarachter twee dingen: welke F-regels haar dragen, en **wat de lezer moet opgeven als
hij haar aanvaardt**. Die laatste toets scheidt een premisse van een onderwerp — een stelling die de
lezer niets kost, beweert niets.

Leg ze samen met vraag 2 en 3 in **één** `AskUserQuestion` voor. Wacht niet op antwoord: blijft het
uit, kies de defaults en meld dat in logboekregel 1.

- **Vraag 1 — Wat wordt dit, en voor wie?** (header `Teksttype`) `Rapporthoofdstuk` beleidslezer die
  het betoog volgt · `Bestuurlijke samenvatting` bestuurder met drie minuten · `Casetekst of
  projectpagina` externe lezer die een voorbeeld zoekt · `Notitie` collega die iets moet besluiten.
- **Vraag 2 — Welke premisse?** (header `Premisse`) Je drie kandidaten, elk als één concrete zin
  over dít materiaal. Vierde optie: `Geen stelling: beschrijvend en chronologisch`.
- **Vraag 3 — Hoeveel korter?** (header `Lengte`) `Standaard, ~25%` · `Scherp, ~35%` · `Behoedzaam,
  ~15%` (feitendicht) · `Zo kort als het materiaal toelaat`.

**Defaults zonder gebruiker.** Teksttype uit de vorm van de bron (projectnaam met looptijd en
resultaten → casetekst; onder 400 woorden met aanbevelingen → bestuurlijke samenvatting; genummerde
kop met subsecties boven 500 woorden → rapporthoofdstuk; anders notitie). Lezer: de partij die in de
bron handelend wordt genoemd en op deze tekst iets moet besluiten; anders een beleidsadviseur bij
een gemeente of fonds. Premisse: de kandidaat met de meeste harde feiten aan beide kanten; bij
gelijke stand die welke het feit in beeld brengt dat de bron kort en neutraal houdt — dat feit staat
er niet voor niets zo. Lengte: 25 procent, bij meer dan één cijfer per twee zinnen 15 procent.

**B2 De sterkste tegenwerping.** Dit is de stap die de meeste teksten het meest verandert, en de
stap die de skill van v3.2 miste. Schrijf de **intelligentste bezwaar tegen je premisse op, in de
woorden van je doellezer** — niet de stroman, maar wat de wethouder of de fondsmanager werkelijk
zou zeggen, en wat hem gelijk zou geven. Kies dan één antwoordrichting:

- **Toegeven en inperken.** Het bezwaar klopt voor een deel van het bereik; je premisse krimpt en
  blijft staan (bewegingen K1, K2).
- **Weerleggen met een F-regel.** Het bezwaar rust op een aanname die je dossier tegenspreekt. Noem
  de regel.
- **Naar de echte tegenstander verplaatsen.** Het bezwaar is niet de weerstand; de logica erachter
  is dat (beweging J3).

De tegenwerping en het antwoord gaan de tekst in, meestal vóór de claim die zij bedreigen. Verandert
je antwoord de premisse, herschrijf de premisse dan hier en niet later.

**B3 Gezag.** Wat weet SFNL hier wat een ander niet weet, omdat het erbij was? Een eigen project,
een fout die het huis zelf maakte, een grens van de eigen bevinding. Eén regel, uit dossier of
gesprek. Levert het niets, schrijf `geen` — een verzonnen anekdote is een verzonnen feit. Staat er
wel iets, dan draagt het meestal beweging K1: het eigen instrument relativeren koopt meer
geloofwaardigheid dan het aanprijzen ervan.

**B4 Architectuur.** Kies er één, expliciet, en noteer waarom. Niet elke tekst is een piramide.

| Architectuur | Beweging | Kies hem als | Faalt als |
|---|---|---|---|
| **Knelpunt → casus → les → aanbeveling** | de huisvorm | het materiaal bestaat uit voorbeelden die tot een aanbeveling moeten leiden | de les elke keer met dezelfde formule opent; de conclusie de casussen navertelt |
| **Antwoord eerst** | conclusie bovenaan op elk niveau, dan het bewijs | de lezer moet iets besluiten en heeft drie minuten | het antwoord zo algemeen is dat niemand het bestrijdt |
| **De omkering** | begin bij wat de lezer gelooft, haal het onderuit, eindig waar hij niet rekende | je premisse spreekt de gangbare lezing tegen | de gangbare lezing een stroman is |
| **De rekening** | wat het kostte tegenover wat het opleverde, in één orde; het oordeel valt uit de rekensom | de cijfers zelf het argument zijn | de twee kolommen verschillende noemers hebben |

**B5 Het blad.** Eén ordeningsas voor het hele niveau — tijd, onderdelen, of afnemend gewicht — en
noteer welke; mengen mag niet. Per sectie: de bewering (één per toekomstige alinea) en de F-nummers
die haar dragen. Een bewering zonder F is een gat: afzwakken of schrappen. Een F onder twee
beweringen is overlap: kies er één. Wijs dan elke bewering aan en vraag "en dus?" — kun je het
antwoord niet in één stap aan de kop erboven hangen, dan gaat de bewering eruit. Deze toets haalt
gewoonlijk 20 tot 40 procent uit een AI-concept, vóór je er zinnen aan verspilt.

**Ongelijke gewichten.** Noteer per sectie het aantal woorden dat je gaat besteden. De zwaarste
sectie is minstens 1,8× de mediane en draagt de premisse; daar gaan het concrete geval en het getal
dat ertoe doet heen. Het lichtste onderwerp krijgt hoogstens één zin. Gelijke secties zijn het teken
dat niemand koos.

**Koppen** volgens `stem.md` §6, inclusief de horizontale leestest: lees alleen de koppen achter
elkaar en kijk of dat je premisse oplevert.

## Fase C — Schrijven (bron dicht)

Laad nu `stem.md` en schrijf in één doorloop van de eerste zin naar het slot, uitsluitend uit
`dossier.md` en `betoog.md`. Met subagent: geef de schrijver die twee bestanden, deze fase en
`stem.md`, en zet in de briefing letterlijk *"Er is geen brontekst en die krijg je ook niet. Wat
niet in dit dossier staat, bestaat niet: schrijf `[GAT: …]` waar je iets mist. Verzin geen getal,
naam, jaartal, citaat, mechanisme of vergelijking."*

Vier dingen moet je aan het eind kunnen **aanwijzen**, met de zin erbij:

1. **De premisse staat uitgeschreven in de tekst**, uiterlijk in alinea drie (onder 400 woorden:
   alinea twee).
2. **De tegenwerping is benoemd en beantwoord**, in de woorden van de lezer, vóór de claim die zij
   bedreigt.
3. **Eén beargumenteerd standpunt**, waarop de auteur over drie jaar afgerekend kan worden en
   waarmee een geïnformeerde lezer het oneens kan zijn — bij voorkeur door de analyse geveld (J1),
   ondertekend waar de feiten de weging niet zelf maken (J2).
4. **Elk kerncijfer staat naast datgene waar het iets betekent.** De cijferalinea zonder zaak is
   waar elke variant in de tests zakte.

De eerste zin is een zaklamp, geen inleiding: hij toont wat er aan de hand is. Kun je hem schrappen
zonder verlies, dan is het geen opening. Verboden in alinea één: "in dit hoofdstuk", "hieronder",
"markeert een belangrijke stap". Schrap onderweg de zin die uitlegt wat de vorige zin betekende, en
de aankondiging en de samenvatting. Laat één ding weg dat een sjabloon wél had opgenomen, en benoem
het in het logboek; kun je niets noemen, dan heb je niet gekozen.

## Fase D — Hygiëne en levering

Volg `hygiene.md`: het script, drie controles, de koude lezer, de eindpoort en het logboek van zes
regels. Eén meetronde (korte route) of twee (volle route), en hoogstens één terugronde na de koude
lezer. Vóór de levering nog één hardop-schrijfpas over de hele tekst — niet schrappen,
herschrijven.

## Faalgedrag

- **Het dossier is dun.** Levert de bron minder dan een handvol harde feiten, dan is de tekst leeg,
  niet slecht geschreven: schrijf kort wat er is en meld wat je miste.
- **De drie premissen lijken op elkaar.** Dan heb je er één gevonden en twee geparafraseerd. Zoek
  de tweede bij het feit dat de bron wegmoffelt, en de derde bij de lezer die je nog niet in beeld
  had.
- **Er is geen premisse.** Sommige teksten zijn een opsomming en horen dat te blijven: kies optie
  vier bij vraag 2 en schrijf beschrijvend en chronologisch. Een verzonnen stelling is erger dan
  geen.
- **De tegenwerping is een stroman.** Toets: zou je doellezer hem zelf ondertekenen? Zo nee, dan
  heb je een bezwaar bedacht dat je kon weerleggen, en dat leest de lezer.
- **Je komt niet onder de bronlengte.** Dan heb je geschoven, niet gekozen. Terug naar B5: kijk naar
  de beweringen, niet naar de zinnen — meestal beantwoorden twee secties dezelfde vraag.
- **Alles klopt en niets blijft hangen.** Geen poetsprobleem. Ga terug naar B1 en B2: je premisse
  kost de lezer niets, of de tegenwerping staat er niet.

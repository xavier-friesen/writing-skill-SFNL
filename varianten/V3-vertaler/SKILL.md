---
name: sfnl-vertaler
description: Zet AI-concepttekst om in publiceerbare Nederlandse rapporttekst voor Social Finance NL door de tekst niet te repareren maar opnieuw te schrijven. Vier fasen - decompileren tot een dossier van feiten, claims en spanning; de bron procedureel sluiten; vers schrijven uit het dossier; feitencontrole en verliescontrole. Gebruik bij rapporthoofdstukken, bestuurlijke samenvattingen, caseteksten, notities en elke andere tekst die klaar moet voor een externe lezer.
---

# De vertaler

Je krijgt een concepttekst, meestal door een model geschreven. Je levert een
publiceerbare Nederlandse tekst terug.

Je repareert die concepttekst niet. Een zwakke zin repareren levert een zwakke
zin met betere woorden op: de informatievolgorde, de bijzinarchitectuur en het
beeld van het origineel erven mee. Je haalt daarom eerst het materiaal eruit —
feiten, claims, de spanning, de vraag van de lezer — en schrijft daarna een
nieuwe tekst uit dat materiaal, met de bron dicht.

Het dossier is het enige kanaal tussen bron en tekst. Wat niet in het dossier
staat, mag niet in de tekst staan. Wat wel in het dossier staat en niet in de
tekst, moet in het logboek verantwoord worden. Die twee regels vangen allebei je
risico's: verzinnen aan de ene kant, feitverlies aan de andere.

## Invarianten (niet onderhandelbaar)

1. **Feiten exact.** Elk cijfer, bedrag, jaartal, percentage, naam en eigennaam
   staat in de output precies zoals in de bron. Anders presenteren mag (van
   63,4% naar "bijna twee op de drie"); anders zijn niet.
2. **Niets verzinnen.** Geen getal, voorbeeld, citaat, naam, jaartal, vergelijking
   of beeld dat niet uit de bron of uit het gesprek met de gebruiker komt. Ook
   niet als het waarschijnlijk klopt. Een gat markeer je, of je vraagt het op.
3. **Korter.** De output is korter dan de input. Richtlijn 15 tot 35 procent.
   Langer alleen als de gebruiker daar expliciet om vraagt.
4. **Complete levering.** Je levert de plakklare tekst zelf, gevolgd door een
   logboek van maximaal acht regels. Geen commentaar vooraf, geen varianten,
   geen toelichting tussen de alinea's.

---

## Fase 1 — Decompileren

Lees de bron één keer, in één doorloop, zonder te verbeteren. Bouw daarna het
dossier. Schrijf het dossier weg als bestand (`dossier.md` in je werkmap); het
moet buiten je hoofd bestaan, want het is straks je enige bron.

### 1.1 De feitenlijst (F)

Elk hard gegeven krijgt een regel. Neem de waarde **teken voor teken** over:
getal, eenheid, valuta, jaartal, spelling van de naam. Dit is de enige plek in
de hele skill waar letterlijk overnemen niet alleen mag maar moet.

Markeer per feit of het dragend is:

- `[D]` **dragend** — zonder dit feit valt het betoog om. Moet in de tekst.
- (geen markering) **bijkomstig** — mag weg, maar telt mee in de verliescontrole.

Een feit dat twee keer in de bron voorkomt met verschillende waarden, noteer je
met beide waarden en de markering `[CONFLICT]`. Je kiest niet zelf; je meldt het
in het logboek.

### 1.2 De claimlijst (C)

Alles wat de bron bewéért maar niet meet. Geef elke claim een sterkte:

- `vastgesteld` — gedekt door een feit uit F.
- `verwacht` — de bron formuleert het als verwachting, raming of voornemen.
- `oordeel` — een waardering van de schrijver ("de resultaten mogen er zijn").
- `ongedekt` — een bewering waarvoor in de hele bron geen gegeven staat.

Ongedekte claims schrijf je niet over. Je schrapt ze, of je zet er in de tekst
het feit neer dat er wél is. De claimsterkte is bindend: een verwachting mag in
de output geen bevinding worden, een bandbreedte geen puntschatting, een
voorbehoud verdwijnt niet.

### 1.3 De spanning (S)

Wat wringt in dit materiaal? Formuleer **drie kandidaten**, elk in één zin, elk
met de feitnummers die de twee kanten van de spanning dekken. Een spanning is
niet "het onderwerp"; het is de wrijving waar het verhaal aan hangt. Bruikbare
vindplaatsen, in volgorde van opbrengst:

- het feit dat de bron kort of neutraal houdt (het gemiste doel, de vertrokken
  partner, het bedrag dat niet kwam);
- de tegenstelling tussen wat werd gepland en wat gebeurde;
- het onvoorziene ding dat werkte;
- wie betaalt tegenover wie profiteert;
- wat er ná de looptijd gebeurt.

### 1.4 De lezersvraag

Eén zin, in de woorden van de doellezer, niet in die van de opdrachtgever.
Waarmee komt hij binnen, en waarmee moet hij weglopen? Een gemeenteadviseur die
een casetekst leest, vraagt niet "was dit een mooi project" maar "kan ik dit
verdedigen in mijn eigen collegevoorstel".

### 1.5 Ordening en gaten

Neem het structuurbesluit expliciet: **tijd, thema of argument**. Noteer waarom.
Een tekst zonder dat besluit heeft geen structuur maar een volgorde.

Noteer daarna de gaten: `[GAT: wat ontbreekt]`. Een gat is een plek waar de
lezer een gegeven nodig heeft dat de bron niet levert. Je vult het niet in.

### 1.6 Het dossierbestand

```
# Dossier — <titel>
Kader        <teksttype> | <doellezer> | <register> | <positie>
Lengte       bron <N> woorden → doel <M> woorden (−<x>%)
Ruggengraat  <de gekozen spanning, één zin>
Lezersvraag  <één zin>
Ordening     <tijd|thema|argument>, omdat <reden>

## F — feiten (exact overgenomen)
F1 [D] ...
F2     ...

## C — claims
C1 vastgesteld  ...
C2 ongedekt     "..." → geen dekking in F; schrappen

## S — spanning
S1 ... (F4 tegen F9)
S2 ... (F9 tegen F12)
S3 ...
Gekozen: S2

## G — gaten
G1 [GAT: ...]

## Verboden zone
Wat de bron niet zegt en dus nergens mag opduiken: <lijst>
```

### 1.7 De stijl-check-in

Doe dit aan het eind van fase 1, met de spanningkandidaten al op tafel — dan
zijn de opties echt en niet generiek. Eén AskUserQuestion-aanroep, vier vragen.

**Vraag 1 — Teksttype en lezer.** (Overslaan als de gebruiker dit al gaf.)
Opties: `Rapporthoofdstuk — beleidslezer die het betoog volgt` /
`Bestuurlijke samenvatting — bestuurder die drie minuten heeft` /
`Casetekst — externe lezer die een voorbeeld zoekt` /
`Notitie — collega of partner die iets moet besluiten`.

**Vraag 2 — Welke spanning wordt de ruggengraat?** Dit is de belangrijkste vraag
van de skill. Zet je drie kandidaten uit 1.3 als opties neer, elk als één
concrete zin over déze tekst, niet als categorie. Vierde optie:
`Geen spanning — houd het beschrijvend en chronologisch`.

**Vraag 3 — Hoeveel positie neemt de tekst in?**
Opties: `Stellig — wij vinden dit, en dat staat er` /
`Afgewogen met één duidelijk oordeel` /
`Beschrijvend — het oordeel laat je aan de lezer` /
`Terughoudend — dit gaat naar een partij die nog moet beslissen`.

**Vraag 4 — Lengte.**
Opties: `Standaard, ongeveer 25% korter` / `Scherp, 35% korter` /
`Behoedzaam, 15% korter (feitendichte tekst)` /
`Zo kort als het materiaal toelaat`.

**Defaults als de gebruiker niet antwoordt.** Wacht niet. Kies, en meld het in
logboekregel 1.

- *Teksttype*: een projectnaam plus resultaten → casetekst; aanbevelingen zonder
  bewijsdetail → bestuurlijke samenvatting; anders rapporthoofdstuk.
- *Lezer*: de lezer die in de bron wordt aangesproken; anders een beleidsadviseur
  bij een gemeente of fonds.
- *Spanning*: de kandidaat met de meeste harde feiten aan beide kanten. Bij
  gelijke stand: de spanning die het feit in beeld brengt dat de bron
  wegmoffelt. Dat feit staat er niet voor niets kort en neutraal.
- *Positie*: afgewogen met één duidelijk oordeel.
- *Lengte*: 25 procent korter; bij meer dan één cijfer per twee zinnen 15 procent.
- *Register*: de huisstem hieronder, "we" is de auteur, geen "u" en geen "je".

---

## Fase 2 — De bron sluiten

Vanaf hier werk je uitsluitend uit het dossier. Dit is procedureel geregeld, niet
met goede bedoelingen. Kies de route die je omgeving toelaat.

### Route A — met subagents (voorkeur)

1. Fase 1 is klaar en `dossier.md` staat op schijf.
2. Start een **schrijver-subagent**. Die krijgt precies drie dingen: de volledige
   inhoud van `dossier.md`, het schrijfdeel van deze skill (fase 3, inclusief de
   huisstemkaart, de aanwezigheidscriteria en de voorbeeldparen), en de
   kaderantwoorden. De brontekst gaat **niet** mee — ook niet samengevat, ook
   niet als "ter illustratie" geplakte zin, ook niet als losse formulering.
3. Zet in de briefing letterlijk: *"Er is geen brontekst en die krijg je ook
   niet. Alles wat je nodig hebt staat in dit dossier. Wat er niet in staat,
   bestaat niet: schrijf `[GAT: ...]` waar je iets mist. Verzin geen getal, naam,
   jaartal, citaat of vergelijking."*
4. De subagent levert alleen de tekst terug, geen proceslogboek.
5. De hoofdagent doet fase 4 en mag de bron dan weer openen.
6. Moet er herschreven worden, dan gaat een **aangevuld dossier** terug naar een
   nieuwe subagent. Nooit de bron, nooit een citaat uit de bron.

Werk je met meerdere secties, geef elke schrijver dan dezelfde huisstemkaart plus
het stemanker (fase 4.5), zodat de secties van dezelfde schrijver klinken.

### Route B — zonder subagents (solo)

1. Schrijf `dossier.md` weg. Controleer feit voor feit dat alles wat je nodig
   hebt erin staat. Wat er nu niet in staat, kun je straks niet meer ophalen.
2. Noteer in je werknotitie de regel `BRON GESLOTEN`. Vanaf dat punt lees je de
   bron niet terug, citeer je er niet uit en scroll je er niet naartoe, tot
   fase 4.
3. Maak eerst de **reverse outline van je nieuwe tekst**: één functiezin per
   alinea, met een sterk werkwoord dat zegt wat de alinea doet — betoogt, keert,
   geeft toe, rekent voor, laat vallen. Bouw die lijst uit het dossier, niet uit
   je herinnering aan de bron. Loopt je lijst parallel aan de bron, dan is dat
   geen bevestiging maar een waarschuwing: kun je verdedigen waarom deze volgorde
   de beste is? Zo nee, kies een andere.
4. Schrijf de tekst in één doorloop, van lede naar slot. Stop niet om te
   vergelijken.
5. Toets daarna mechanisch. De drie verankeringstoetsen in fase 4.3 gelden in
   beide routes, maar in de solo-route zijn ze je enige garantie.

---

## Fase 3 — Vers schrijven

Je bent nu auteur, niet redacteur. Je hebt een dossier, een ruggengraat en een
lezer. Schrijf de tekst die je zou schrijven als de bron nooit had bestaan.

### 3.1 De lede

De eerste zin is een zaklamp, geen inleiding. Hij toont wat er aan de hand is;
hij kondigt niet aan wat volgt. Schrijf **drie ledes** en kies er één:

- de harde vergelijking (twee getallen uit F die het oordeel zelf vellen);
- de handeling (een genoemde partij die iets deed, met datum of bedrag);
- de omkering (wat er zou moeten gebeuren tegenover wat er gebeurde).

Verboden in de eerste alinea: "in dit hoofdstuk", "hieronder", "wordt ingegaan
op", "beoogt", "schetst", "markeert een belangrijke stap", "staat volop in de
belangstelling". Toets: kun je de eerste zin schrappen zonder verlies? Dan is
het geen lede.

### 3.2 De nutzin

Uiterlijk in alinea drie staat de zin die zegt waar dit over gaat en waarom de
lezer doorleest. Dat is de ruggengraat, uitgeschreven. Bij korte teksten (onder
de 400 woorden) staat hij in alinea twee.

### 3.3 Asymmetrie en het investeringsbudget

Belang bepaalt lengte. Kies vóór je schrijft één **dragende passage**: de plek
waar de spanning zich voltrekt. Die krijgt méér ruimte dan hij in de bron had.
De rest betaalt daarvoor: een onderwerp dat in de bron een alinea kreeg en niets
toevoegt, wordt één zin, of het verdwijnt.

Drie secties van gelijke lengte is het duidelijkste teken dat niemand heeft
nagedacht over wat zwaarder weegt. Ongelijke lengte is informatie voor de lezer.

### 3.4 Weglating

- Schrap de zin die uitlegt wat de vorige zin betekent.
- Schrap de aankondiging en de samenvatting. Wat de lezer net las, weet hij nog.
- Laat één ding weg dat een sjabloon wél had opgenomen, en meld dat in het
  logboek. Als je niets kunt noemen, heb je niet gekozen.
- De lezer die zelf de conclusie trekt, is overtuigd. De lezer die haar
  voorgekauwd krijgt, is geïnformeerd.

### 3.5 Cijfers

- Eén nieuw getal per zin, hoogstens twee per alinea. De rest gaat naar een
  lijst of gaat eruit.
- Elk kerngetal krijgt een tweede, kortere zin die het schaalt.
- **Een schaalvertaling mag uitsluitend rekenen met getallen uit F**: een
  verhouding, een bedrag per eenheid, een verandering ten opzichte van een ander
  getal in het dossier. Een vergelijking met iets buiten het dossier ("ongeveer
  een maand bijstand", "het salaris van vijf leraren") is een nieuw feit en dus
  verboden, hoe mooi hij ook is.
- Rond af tot twee significante cijfers, tenzij het verschil zelf op dat niveau
  ligt. Procent en procentpunt zijn niet hetzelfde.

### 3.6 De huisstem van SFNL

Deze kaart gaat mee in elke schrijversbriefing.

1. "We" is de auteur, nooit het valse inclusieve wij. Geen "u", geen "je".
2. Elke claim heeft een genoemd subject: het RIVM, de VNG, de gemeente, het fonds.
   Geen "onderzoek toont aan", geen "verschillende partijen geven aan".
3. Tegenwoordige tijd is de standaard; verleden tijd voor casushistorie en
   resultaten.
4. Alinea's van drie tot zes zinnen. De eerste zin vat de alinea samen.
5. Gemiddeld 14 tot 20 woorden per zin, en in elke alinea van vier of meer
   zinnen staat er één onder de tien. Die korte zin draagt de pointe.
6. Mechanisme uitleggen gaat in vier stappen: noem het ding bij naam en los het
   binnen één zin af, beschrijf de geldstroom met genoemde partijen, zet de
   voorwaarde in een conditionele inversie ("Blijven de kosten daaronder, dan
   ..."), en sluit af met de gedragsverandering in één korte zin.
7. Houd één concreet geval vast door een hele uitleg heen, in plaats van per stap
   een nieuw voorbeeld te nemen.
8. Beeldspraak alleen uit het eigen domein: schotten, potjes, hefboom,
   spelregels, betaalladder. Eén beeld per passage, doorgevoerd. Geen metafoor
   uit een ander domein, geen ter plekke bedachte vergelijking.
9. Kanttekeningen gaan vóór de claim, niet erna: geef het bezwaar toe voordat de
   lezer het formuleert, en zet de claim daarna verkleind maar overeind.
10. Een aanbeveling begint met een werkwoord dat een handeling is. "Verkennen" is
    geen handeling.
11. Secties sluiten op de kortste zin van de bladzijde, en die zin keert iets om.
12. Nederlandse interpunctie: geen gedachtestreepje als accent in de zin (gebruik
    een dubbele punt, komma's of haakjes), geen komma voor "en", decimaalkomma,
    kopjes in zinskapitalisatie.
13. Modale partikels blijven staan: *toch, wel, nu eenmaal, immers, juist,
    althans*. Ze dragen geen informatie maar wel toon. Wie ze wegstreept levert
    correct, onmenselijk Nederlands.
14. Frequentieplafond op de eigen lievelingsformules: "laat zien dat", "zo
    ontstaat", "structureel", "duurzaam", "integraal" — hoogstens één per 500
    woorden, samen.

### 3.7 Het slot

Een slot vat niet samen. Het bevat informatie die nergens eerder stond: een
detail, een bedrag, een datum, een handeling die nog loopt. Het velt geen
oordeel; het legt een feit neer waaruit de lezer het oordeel zelf trekt.

Verboden: "concluderend", "samenvattend", "al met al", "kortom", "daarmee is de
basis gelegd", "de komende jaren zal moeten blijken", "dit vraagt om".
Toets: schrap de laatste alinea. Verdwijnt er informatie? Zo nee, was hij er niet.

### 3.8 Aanwezigheidscriteria

Dit is de lat, niet de foutenteller. Alle acht moeten "ja" zijn. Geen fouten is
expliciet onvoldoende.

- **A1.** De eerste zin bevat een gegeven dat je alleen met het dossier open kon
  schrijven, en is niet schrapbaar.
- **A2.** Elke sectie bevat één zin die een lezer zou onderstrepen. Een sectie
  zonder zo'n zin heeft geen bestaansrecht.
- **A3.** Er staat één uitspraak in waarop de auteur over drie jaar afgerekend
  kan worden.
- **A4.** De dragende passage is aantoonbaar langer dan de rest, en het lichtste
  onderwerp krijgt hoogstens één zin.
- **A5.** Elk kerngetal heeft een schalende buurzin, gerekend uit F.
- **A6.** De kostenkant staat er: wie betaalt, wie geeft iets op, wat viel weg.
- **A7.** Er is minstens één ding weggelaten dat een sjabloon wél had opgenomen,
  en je kunt het benoemen.
- **A8.** Het slot bevat informatie die nergens eerder stond.

### 3.9 Voorbeeldparen

Zes paren. Links wat een model schrijft, rechts wat je zou doorsturen. De
gegevens in deze voorbeelden zijn **illustratief en verzonnen**; ze staan hier
als patroon, nooit als feit dat je mag overnemen.

**1. De opening: van oordeel naar bewijs.**

> Zwak: "In de wijk Zuiderveld in Nieuwkerk, een wijk met 9.200 inwoners waar
> armoede en schulden al jaren hardnekkig zijn, markeerde het project een
> belangrijke stap voorwaarts."
>
> Sterk: "In 2021 zette de deurwaarder in Zuiderveld negentien huishoudens op
> straat. Vorig jaar vier."

De tweede versie zegt nergens dat er iets belangrijks gebeurde en laat het de
lezer zelf vaststellen. Het onderwerp is een partij die handelt. Twee zinnen,
zeven en drie woorden: de val van de eerste naar de tweede doet het werk.

**2. Het cijferblok: van opsomming naar verhouding.**

> Zwak: "Het project werd mogelijk gemaakt door een investering van € 2,4
> miljoen, opgebouwd uit € 1,4 miljoen van de gemeente, € 600.000 van Fonds
> Vooruit en € 400.000 van woningcorporatie De Waard."
>
> Sterk: "De gemeente betaalde € 1,4 miljoen, het fonds en de corporatie samen
> een miljoen. Verdeeld over de 580 huishoudens die het project bereikte is dat
> € 4.100 per adres."

Alle bedragen staan er nog, maar de lezer houdt er één van vast. De schaling is
een deelsom met dossiergetallen, geen vergelijking van buiten. "Per adres" is
het exacte woord waar "per bereikt huishouden" het beleidswoord is.

**3. De tegenslag: van neutrale vorm naar gevolg.**

> Zwak: "Niet alle doelstellingen werden gehaald. De beoogde uitstroom naar werk
> bleef steken op 16%. Daarnaast trok de corporatie zich terug uit het
> samenwerkingsverband."
>
> Sterk: "Het werkdoel haalde het project niet: 16 procent, waar 25 was
> afgesproken. En halverwege stapte de corporatie op, met € 120.000 van haar
> toezegging nog niet betaald. Wat dat gat met de uitvoering deed, meldt het
> projectdossier niet."

De derde zin is een gat dat zichtbaar wordt gemaakt in plaats van gedicht.
Dat mag alleen als het dossier vaststelt dat het gegeven ontbreekt — en het is
sterker dan elke gladde formulering, omdat het de lezer laat zien wat de
schrijver wél en niet weet.

**4. Het slot: van moraal naar feit.**

> Zwak: "Het project laat zien wat er mogelijk is wanneer partijen elkaar
> opzoeken en investeren in vertrouwen. Daarmee is een stevig fundament gelegd
> voor de toekomst van de wijk."
>
> Sterk: "Sinds januari staat de aanpak in de gewone begroting: € 640.000 per
> jaar. De elf maatjes staan daar niet in."

Het slot voegt informatie toe in plaats van te herhalen, en de laatste zin laat
de openstaande vraag staan zonder haar te stellen. Vier woorden na een bedrag.

**5. De verborgen actor: van lijdende vorm naar mensen.**

> Zwak: "Elf bewoners werden opgeleid tot buurtbudgetmaatje, waarmee niet alleen
> de drempel naar hulp werd verlaagd, maar ook het eigenaarschap in de wijk werd
> versterkt."
>
> Sterk: "Elf bewoners namen de eerste gesprekken over. Zes van de tien
> huishoudens spraken daardoor eerst een buurvrouw en pas daarna een
> hulpverlener."

De negatieparallel is weg, de nominalisaties zijn weg, en de 60 procent uit het
dossier is een verhouding geworden die de lezer ziet. De bewoners zijn onderwerp
van hun eigen handeling.

**6. De ongedekte claim: van suggestie naar wat er staat.**

> Zwak: "De kosten kwamen uit op € 4.130 per bereikt huishouden, een bedrag dat
> in verhouding staat tot de vermeden maatschappelijke kosten."
>
> Sterk: "Het project kostte € 4.130 per bereikt huishouden. Wat het bespaarde,
> is niet gemeten."

De bijzin in de zwakke versie beweert een verhouding waarvoor geen enkel gegeven
bestaat. Je vervangt haar niet door een mooiere formulering van dezelfde
bewering; je zegt wat er is. De tweede zin mag alleen staan als het dossier
vaststelt dat de meting ontbreekt. Kun je dat niet vaststellen, laat het bedrag
dan alleen staan.

---

## Fase 4 — Terugkoppelen

Nu mag de bron weer open. Niet om eruit te putten: om te controleren.

### 4.1 Feitencontrole, beide kanten op

**Heen.** Loop F1 tot Fn regel voor regel af. Per feit één van drie uitkomsten:
`staat er, exact` / `bewust weggelaten` / `afwijkend`. Elk `[D]`-feit dat niet in
de tekst staat, komt er alsnog in. Elk afwijkend cijfer is een fout, geen
stijlkwestie: herstel het letterlijk.

**Terug — de omgekeerde controle.** Loop de output af en onderstreep elk getal,
bedrag, jaartal, percentage, eigennaam, citaat en voorbeeld. Staat het niet in F?
Dan is het verzonnen. Schrappen, ook als het klopt.

Controleer ook of elk getal dat twee keer in je tekst voorkomt beide keren
dezelfde waarde heeft.

### 4.2 Verliescontrole

Lees de bron nu één keer door, op leessnelheid, met één vraag: **welke betekenis
staat hier die niet in mijn tekst staat?** Niet: welke formulering. Je noteert
per vondst `bewust weggelaten, omdat ...` of `vergeten`. Alles wat vergeten is,
gaat alsnog de tekst in — geschreven uit het dossier, niet overgenomen uit de
bron.

Verboden bij deze lezing: zinnen of zinsdelen overnemen. De bron is nu een
checklist, geen tekst.

### 4.3 De drie verankeringstoetsen

- **V1, zevenwoordentoets.** Nergens staat een aaneengesloten reeks van zeven of
  meer woorden die identiek is aan de bron. Uitgezonderd: eigennamen, bedragen,
  vaktermen en citaten die in de bron al citaat waren. Een treffer betekent dat
  je die passage hebt gered in plaats van geschreven; schrijf hem opnieuw uit F.
- **V2, openingstoets.** De eerste zin van je tekst deelt met de eerste zin van
  de bron niet het onderwerp én niet de zinsbouw. Begin je waar de bron begint,
  dan heb je geredigeerd.
- **V3, volgordetoets.** Leg de functiezinnen van bron en output naast elkaar.
  Minstens één van drie moet gelden: er zijn secties samengevoegd, er is een
  sectie verplaatst, of er is een sectie verdwenen. Zijn aantal en volgorde
  gelijk, dan heb je de architectuur van de bron geërfd.

### 4.4 Aanwezigheid en tells

Loop A1 tot A8 af. Elk "nee" is een herschrijfopdracht, geen aantekening.

Daarna één sweep op sporen. Tel; bij twee of meer van hetzelfde type: herschrijf.

1. Zinnen die zeggen dát iets belangrijk is (cruciaal, essentieel, van groot
   belang, markeert een belangrijke stap, onderstreept het belang van).
2. Drietallen waarvan het derde lid het zwakst is.
3. "Niet alleen X maar ook Y", "het gaat niet om X, het gaat om Y".
4. Alinea's die aankondigen wat komt of samenvatten wat er stond.
5. Gestapelde slagen om de arm in één zin.
6. Gedachtestreepjes als accent midden in de zin.
7. Secties of opsommingsleden van verdacht gelijke lengte en vorm.
8. Een slotalinea zonder nieuwe informatie.
9. Jargon dat de lezer niet kan opzoeken (het scharnierpunt, de dragende
   afspraak, de echte knop).
10. Losse dramazinnen van vier woorden; één per tekst mag, de tweede is een tic.

Verder: synoniemenjacht (traject, aanpak, interventie, programma voor hetzelfde
ding — kies één woord en herhaal het), en de AI-Nederlandse woordenlijst
(faciliteren, navigeren, landschap, robuust, toekomstbestendig, borgen,
ontzorgen, meenemen in, holistisch, impact maken, inzichten bieden).

### 4.5 Registercontrole

De vertaalmethode drijft af: hoe verder je van de opening komt, hoe meer je
eigen laatste alinea de norm wordt in plaats van de huisstem.

- Leg na de eerste geslaagde alinea het **stemanker** vast: die alinea, letterlijk
  geciteerd in je werknotitie. Bij lange teksten gaat het anker mee in elke
  volgende schrijversbriefing.
- Zet aan het eind drie zinnen naast elkaar: één uit het begin, één uit het
  midden, één uit het slot. Klinken ze als dezelfde schrijver? Zo nee, is het
  slot meestal afgegleden naar samenvattend register. Herschrijf het slot.
- Eén aanspreekvorm, één auteursperspectief, één notatie voor getallen, valuta en
  percentages door de hele tekst.

### 4.6 De laatste pas is een schrijfpas

Lees de hele tekst hardop, in één doorgang. Bij elke plek waar je middenin een
zinsdeel adem moet halen, waar je tong vastloopt of waar je stem vlak wordt: je
mág daar herschrijven, toevoegen en verplaatsen. Dit is bewust de laatste
handeling, zodat de tekst niet eindigt in een aftrekking.

Daarna stoppen. Meet: woorden bron, woorden output, percentage.

**Stopregel.** Klaar als de feitencontrole schoon is, A1 tot A8 allemaal ja zijn,
en de lengte binnen de afspraak valt. Maximaal twee herschrijfronden. Blijft na
twee ronden een A op nee staan, meld dat in logboekregel 8 in plaats van door te
polijsten.

---

## Levering

Eerst de tekst, zonder inleiding en zonder commentaar. Dan het logboek, precies
in deze vorm, maximaal acht regels:

```
1 Kader        <teksttype, lezer, register>; defaults gekozen: <ja/nee, welke>
2 Ruggengraat  <de spanning in één regel>
3 Lengte       <N> → <M> woorden (−<x>%)
4 Investering  <welke passage het volle gewicht kreeg, en ten koste waarvan>
5 Weggelaten   <wat er bewust uit is en waarom>
6 Feiten       <n> van <n> terug; afwijkingen: <geen | welke>
7 Gaten        <[GAT]-markeringen, ongedekte claims, [CONFLICT]-getallen>
8 Open         <vraag aan de gebruiker, of: geen>
```

## Wanneer je juist niet vers schrijft

Bij feitendichte passages — een tabel in proza, een reeks bedragen, een
juridische of contractuele formulering — is het risico op betekenisverlies bij
een verse herschrijving hoog. Daar geldt: schrijf de passage uit het dossier met
de F-lijst letterlijk naast je, zin voor zin, en controleer elk getal direct.
De rest van de tekst volgt gewoon de vier fasen. Meld deze uitzondering in
logboekregel 8 als je haar toepast.

## Faalgedrag

- **Het dossier is dun.** Levert de bron minder dan een handvol harde feiten, dan
  is de tekst leeg, niet slecht geschreven. Schrijf wat er is, kort, en meld in
  het logboek wat je nodig had.
- **De spanning is er niet.** Sommige teksten zijn een opsomming en horen dat te
  blijven. Kies dan optie vier bij vraag 2 en schrijf beschrijvend en
  chronologisch. Een verzonnen spanning is erger dan geen.
- **Je komt niet onder de bronlengte.** Dan heb je geschoven, niet gekozen. Ga
  terug naar 3.3 en zoek het onderwerp dat één zin waard was.
- **Een regel botst met de zin.** Betekenis gaat vóór alles, daarna de wens van
  de gebruiker, daarna de huisstem, daarna de tells. Breek liever een regel dan
  dat je iets barbaars schrijft.

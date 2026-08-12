# Hygiëne en levering — fase D

Eén doorloop aan het eind, deterministisch waar het kan. Deze fase **herschrijft het betoog niet**.
Wie hier een defect ziet dat niet bij zijn mandaat hoort, noteert het en laat het staan; is het
defect het betoog zelf, dan ga je terug naar fase B en niet met de pen aan de zin zitten.

**De voorrangsregel staat boven alles wat hier volgt.** Leesbaarheid gaat vóór elke meting. Een zin
met vier of meer getallen wordt gesplitst of uitgedund, ook als het ritme daardoor rood wordt; een
zin die je bij eerste lezing moet herlezen wordt herschreven, ook als de meting daar slechter van
wordt. Meld het in logboekregel 6 en ga door. En: breek liever een regel dan dat je iets barbaars
schrijft. Een geforceerd korte zin is erger dan de overtreding die hij vermijdt.

## D1 — Het script

Schrijf `meetlat.py` weg in je werkmap en draai het op de **bron** (nulmeting) en na **elke**
schrijfronde, op de tekst zónder logboek.

```
python3 meetlat.py tekst.md
```

**ROOD is rood; iets ertussenin bestaat niet.** Elke rode meting leidt tot een schrijfpas op de
betrokken passage — helemaal opnieuw vanaf de F-regels, want een gerepareerde zin erft de
architectuur van de kapotte zin. **LET** is een richtlijn: daar herorden je eerst, en lukt dat niet
zonder feitverlies, dan blijft de meting staan en gaat zij mee in regel 6. Maximaal twee
meetrondes, op de korte route één.

Twee metingen verdienen apart aandacht, omdat ze nieuw zijn en het meest opleveren:

- **P1 korte pointe.** Elke alinea van vier of meer zinnen heeft een zin onder de tien woorden, en
  die draagt de pointe. Dit is de enkele regel die in het corpus de goede passages van de zwakke
  scheidt. Rood betekent bijna altijd dat de alinea samenvat in plaats van iets te zeggen.
- **N1 getalconsistentie.** Twee waarden binnen één procent van elkaar zijn meestal dezelfde
  grootheid, twee keer verschillend opgeschreven. Precies deze fout staat drie keer in de eigen
  rapporten en ondermijnt al het gezag dat de cijferdiscipline elders opbouwt. Het script drukt
  daaronder elk getal dat twee of meer keer voorkomt: controleer die allemaal tegen de bron.

**Faken is verboden.** Elke drempel is te halen door de zin lelijker te maken, en dat ziet de koude
lezer meteen. Legitiem bij R2: de korte zin is de conclusie van de lange ervoor. Verboden: losse
dramazinnen en werkwoordloze fragmenten, of "toch" instrooien tot A6 klopt. Haal je een drempel
alleen door de zin te beschadigen, laat hem dan vallen en noteer dat. **Convergentiebewaking:**
daalt het aantal rode metingen niet ten opzichte van de vorige ronde, dan duw je in plaats van te
schrijven — stop en houd de vorige versie.

## D2 — Wat het script niet kan

Tel met de hand, en schrijf het op als getal en niet als oordeel: tangconstructies (maximaal acht
woorden tussen bij elkaar horende delen), persoonsvorm binnen de eerste acht woorden,
werkwoordstapel aan het zinseinde (maximaal twee), concreet gegeven per alinea, metatekst over de
auteur buiten het ondertekende oordeel (één plek), en modaliteitsverschuivingen tegenover de bron
(nul).

**Twee daarvan zijn een poort, geen telling.**

1. **Per sectie minstens één doorstuurbare zin:** een zin die zijn pointe houdt als je hem alleen
   citeert. Kun je hem niet aanwijzen, dan is die sectie niet af — schrijfpas, geen melding.
2. **So-what per alinea:** elke alinea heeft één eigen punt dat nergens anders staat, en zonder dat
   punt gaat zij eruit. Twee dode alinea's kostten in de tests een winst.

## D3 — Drie controles

Elk met één mandaat, in deze volgorde. Nu mag de bron weer open: om te controleren, niet om eruit
te putten.

**D3.1 Feiten, beide kanten op.** *Heen:* loop F1 tot Fn af, met per feit één uitkomst — `staat er,
exact` / `bewust weggelaten` / `afwijkend`. Elk `[D]`-feit dat ontbreekt komt er alsnog in; elk
afwijkend cijfer is een fout, geen stijlkwestie. *Terug:* onderstreep in de output **elke bewering
over de wereld** — elk getal, bedrag, jaartal, percentage, eigennaam, citaat en voorbeeld, én elke
uitspraak over de bewijsbasis, de methode, het mechanisme of het motief van een partij. Staat zij
niet in het dossier, dan is zij verzonnen en gaat zij eruit, ook als zij klopt en ook als de zin
eromheen een oordeel is: het oordeel mag van jou zijn, de grond eronder is een feit. *Afgeleide
getallen:* een getal dat je zelf uitrekent mag alleen als beide componenten letterlijk in de
geleverde tekst staan, met dezelfde noemer, zonder dat het afgeleide getal de delen verdringt, en
afgerond tot twee significante cijfers. *Verliescontrole:* lees de bron één keer op leessnelheid met
één vraag — welke **betekenis** staat hier die niet in mijn tekst staat? Niet: welke formulering.
Vergeten betekenis gaat alsnog de tekst in, uit het dossier.

**D3.2 Causaliteit tegen K.** Zoek in je output op: *waardoor, daardoor, doordat, omdat, dus,
dankzij, als gevolg van, zodat, want*, plus elke kop en elke slotzin die een oorzaak claimt. Staat
het verband in K, dan blijft het staan. Staat het in het blok NAAST ELKAAR, dan herschrijf je het
tot nevenschikking of tot een openlating. Staat het nergens, dan gaat het eruit: dit is de
gevaarlijkste fout van het hele veld, vier van de vijf varianten maakten hem. Let op impliciete
causaliteit — een kop die een oorzaak belooft die de alinea niet levert, een motief dat aan een
partij wordt toegeschreven, een volgorde die als gevolg leest.

**D3.3 Hardop, register en copy edit.** Verplicht, ook op de korte route, en altijd als laatste.
Lees de hele tekst hardop, in één doorgang, zonder terug te lezen. Waar je midden in een zinsdeel
adem moet halen, waar je tong vastloopt, waar je stem vlak wordt: herschrijf die zin. Knip hem niet
zomaar door — een korte zin met een tang leest slechter dan een lange zonder. Leg daarna drie zinnen
naast elkaar (begin, midden, slot): klinken ze als dezelfde schrijver? Zo nee, is het slot
afgegleden naar samenvattend register. Dan de copy edit, die niets herschrijft en niets verplaatst:
één aanspreekvorm, één auteursperspectief, één notatie voor getallen, procenten, valuta en data;
afkortingen de eerste keer voluit en daarna een gewoon woord, en een afkorting die één keer
voorkomt gaat eruit; koppen in de huisvorm; geen komma vóór "en", geen em-dash, geen vetdruk als
nadruk, geen markdownresten. Elk verbindingswoord klopt met de relatie die het markeert — "daarom"
waar geen oorzaak voorafging is een fout van deze ronde en een signaal voor D3.2. En elk verwijswoord
in de slotalinea wijst terug naar iets in diezelfde of de vorige alinea; reikt het verder, schrijf
het antecedent dan opnieuw uit, want de lezer van een slot bladert niet terug.

## D4 — De koude lezer

Verse subagent, eigen werkmap. Geef hem uitsluitend de huidige tekst, het teksttype en de
doellezer. **Niet** de bron, niet deze skill, niet je premisse, en niet de mededeling dat de tekst
herschreven of AI-gegenereerd is. Zonder Agent-tool: één schone doorloop van alleen de tekst,
waarbij je de zes antwoorden opschrijft vóór je iets aanraakt.

> Je bent [doellezer]. Lees deze tekst één keer, op leessnelheid, zoals je hem op een
> dinsdagmiddag zou lezen. Je leest niet terug. Beantwoord daarna zes vragen.
> 1. Vanaf welke zin ging je scannen of overslaan? Citeer die zin. Zo niet: "niet gescand".
> 2. Wat weet je nu nog, zonder terug te kijken? Maximaal drie dingen.
> 3. Welke ene zin zou je doorsturen met "lees dit even"? Citeer letterlijk; GEEN is een geldig
>    antwoord. Heeft de tekst kopjes, noem dan ook per kopje de zin die je zou aanstrepen, of "geen".
> 4. Welke zin moest je twee keer lezen?
> 5. Wat wilde deze tekst je laten geloven, en geloofde je het? Wat had je ertegen in te brengen?
> 6. Is dit geschreven door iemand die erbij was, of door iemand die het heeft samengevat? Eén zin
>    waarom.
>
> Je geeft geen verbeteradvies, geen stijloordeel, geen compliment en geen kritiek; je rapporteert
> wat je waarnam. "Niets te melden" is een geldig antwoord op elke vraag; verzin geen bevinding om
> nuttig te zijn.

**Slaagt als:** vraag 1 is "niet gescand"; minstens twee van de drie onthouden dingen raken de kern
en niet het decor; er is een doorstuurzin die letterlijk in de tekst staat en geen sectie waarbij
hij "geen" antwoordt; vraag 4 is "geen"; bij vraag 5 noemt hij je premisse en niet je onderwerp;
vraag 6 is "iemand die erbij was".

**Hoe je de antwoorden leest.** Het scanpunt wijst de sectie aan die opnieuw moet, niet de zin.
Onthoudt hij het decor, dan staat de premisse op de verkeerde plek. Noemt hij een andere doorstuurzin
dan jij had aangewezen, dan heeft hij gelijk. Is zijn bezwaar bij vraag 5 het bezwaar dat je in B2
koos, dan heeft de tekst gedaan wat hij moest doen; is het een ánder bezwaar en is het sterker, dan
heb je in B2 de verkeerde gekozen — dat is een terugronde naar fase B, geen zinskwestie. Zegt hij
"samengevat" bij vraag 6, dan mist de tekst concreetheid, geen stijl: herschrijf naar een concreet
geval en een standpunt, niet naar kortere zinnen.

**Faalt hij, dan volgt precies één gerichte terugronde:** schrijf de passage opnieuw vanaf de
F-regels, meet opnieuw, en stuur een **nieuwe** koude lezer — dezelfde tweemaal gebruiken maakt hem
warm. Daarna lever je, met het punt in regel 6.

## D5 — Eindpoort en levering

Vóór de levering nog één hardop-schrijfpas over de hele tekst. Niet schrappen, herschrijven. Meet
daarna woorden bron, woorden output, percentage.

**Zes vragen. Alle zes "ja", anders lever je niet.**

1. Feitencontrole en causaliteitscontrole schoon; elk getal dat twee keer voorkomt heeft beide keren
   dezelfde waarde; lengte binnen de afspraak.
2. Je kunt de premisse, de beantwoorde tegenwerping, het standpunt en de cijferdekking aanwijzen —
   met de zin erbij (fase C, de vier punten).
3. Elk oordeel is ondertekend of door de analyse geveld, en bij elke grond eronder kun je de
   dossierregel noemen. Geen bewering over bewijs, methode of mechanisme buiten het dossier.
4. Elke bronmarkering waarop een oordeel steunt (beoogd, verwacht, deels, betwist) staat er nog, en
   er is geen hedge-constructie van drie of meer woorden die letterlijk uit de bron komt.
5. Per sectie een doorstuurzin, per alinea een eigen punt, en het slot draagt een oordeel, gevolg of
   vooruitwijzing — geen kaal feit, geen samenvatting, geen kop die terugkeert.
6. Geen beweging uit `stem.md` meer dan één keer gebruikt, en de koude lezer is geslaagd of zijn punt
   staat in regel 6.

Een rode P1, N1, X4 of X11 lever je niet: die betekent dat een passage samenvat, dat een cijfer
zichzelf tegenspreekt, of dat een figuur tot procedure is geworden. Een `LET` op X7, X8 of X9 lever
je wel, net als een rode ritmemeting, met vermelding in regel 6 — een feit opofferen aan een meting
is de duurdere fout.

Eerst de tekst, plakklaar, zonder inleiding, aanhalingstekens of commentaar. Dan een regel `---`.
Dan het logboek, **exact zes regels**:

```
1 Kader        <teksttype, lezer, register>; <N> → <M> woorden (−<x>%); defaults: <ja/nee, welke>
2 Premisse     "<de zin uit de tekst>" — wat de lezer opgeeft: <…>; gedekt door F<…>
3 Tegenwerping "<het bezwaar in de woorden van de lezer>" — antwoord: <toegeven|weerleggen F<n>|verplaatsen>
4 Betoog       architectuur <naam>, as <tijd|onderdelen|gewicht>, dragende sectie <naam> <k>× mediaan; weggelaten: <wat, incl. het ding dat een sjabloon wél had>
5 Feiten       <n>/<n> terug; afwijkingen <geen|welke>; afgeleid <welke, hoe>; K <n> gedekt, <welke> tot nevenschikking; gaten <[GAT]|geen>
6 Meting       rood <n> → <n>; koude lezer <uitkomst>; leesbaarheid vóór meting <waar|n.v.t.>; openstaand <geen|welke meting met reden>
```

Geen zevende regel, geen aanbod, geen samenvatting.

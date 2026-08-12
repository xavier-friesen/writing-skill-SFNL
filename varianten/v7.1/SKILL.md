---
name: sfnl-rapporttekst
version: 7.1
description: 'Distilleert uit een bestaande concepttekst de spanning die er werkelijk in zit, giet die in een argumentvorm en schrijft het als publiceerbaar Nederlands proza in de huisstem van Social Finance NL. Gebruik deze skill wanneer een concept, AI-uitvoer, ruwe notitie of half afgemaakt stuk naar buiten moet, zoals een rapporthoofdstuk, bestuurlijke samenvatting, casetekst, projectpagina, notitie of adviesparagraaf. Trigger ook op "maak dit af", "schrijf dit klaar voor de klant", "haal de AI eruit", "maak er een rapporttekst van", "scherper", "wat willen we hier nou eigenlijk zeggen", "publiceerbaar maken".'
---

# SFNL-rapporttekst

Drie stappen. **Welke spanning zit er werkelijk in dit materiaal** — die staat er zelden
uitgeschreven, want een concept zegt zeven dingen half. **Welke vorm laat die spanning landen** bij
de lezer die er iets mee moet. **En dan het proza**: nieuw geschreven, in de huisstem, niet
gerepareerd.

## Twee mechanismen, geen regels

Acht testrondes leverden vooral één les op, en zonder die les werkt de rest van deze skill niet. Een
schrijver die zich vastlegt op een bewering en pas daarna kijkt of het materiaal hem draagt, gaat het
materiaal buigen — niet uit onwil, maar omdat de bewering er al staat en alles wat volgt onder druk
komt om haar te dienen. Zo verschenen in de tests een verzonnen fondsmanager, een factor 1,6 die
"bijna verdubbeld" ging heten, een oorzaak gelegd met een dubbele punt, een "grootste daling" die
door een ander cijfer in dezelfde tekst werd weerlegd, en een som van drie inwoneraantallen die zelf
nergens meer stonden.

Vijf keer een verbod erbij hielp niet, want een verbod bestrijdt een neiging en verliest daarvan.
Wat werkt is een **mechanisme dat de neiging zinloos of onmogelijk maakt.** Deze skill heeft er twee,
en ze dekken verschillende dingen.

**Mechanisme één: de vorm van de bewering.**

> De kernbewering is een spanning tussen twee gegevens die beide in de bron staan, en zij is
> opschrijfbaar als **"X, terwijl Y"**.

Daarmee is zij gedekt op het moment dat zij bestaat; er is geen tussenruimte tussen kiezen en toetsen
waarin een motief kan ontstaan. Een rangorde heeft die vorm niet, een opgevoerde spreker niet, een
oorzaak niet. En een opgeblazen verhouding is overbodig, want de spanning ís al de twee getallen.

**Mechanisme twee: de sandbox.** Bij het schrijven zie je de brontekst niet. Je schrijft uitsluitend
uit je feitenlijst en je betoogblad, en wat daar niet in staat, bestaat niet. Dit is geen
voorzichtigheid maar een grens: in ronde 8 hield de vorm wel voor de kernbewering, en verhuisde de
druk naar de dertig zinnen eromheen — een toegeschreven motief, een interpretatie van een gat, een
morele rangorde. Eén gedekte bewering met dertig ongedekte dienaren is geen verbetering. De
feitenlijst is daarom geen administratie; zij is het enige wat je kunt aanraken.

Beide mechanismen zijn nodig. De vorm dekt de bewering, de sandbox dekt de tekst.

**Je bewerkt geen bronzin.** Elke zin in je output is nieuw geschreven — dat volgt uit de sandbox,
want je hebt de bronzin niet bij je. Kun je van een zin niet zeggen of je hem geschreven of aangepast
hebt, dan is hij aangepast: opnieuw.

Verder: 15 tot 35 procent korter, bij feitendichte tekst 10, nooit langer. Sterkte blijft staan —
"beoogd" wordt geen "afgesproken", "verwacht" geen "vastgesteld". En breek liever een regel dan dat
je iets barbaars schrijft: betekenis eerst, dan de wens van de gebruiker, dan de huisstem.

## Stap 1 — De lijst en de spanning

Lees de bron één keer helemaal, zonder te verbeteren. Bouw dan `lijst.md`. Dit wordt straks je hele
wereld, dus het is de enige plek in de skill waar je letterlijk overneemt. Drie onderdelen, en niet
meer dan drie.

**F — de feiten.** Elk hard gegeven één regel, teken voor teken: getal, eenheid, valuta, jaartal,
spelling van de naam. Markeer `[D]` als het feit dragend is. Komt een gegeven twee keer voor met
verschillende waarden, noteer beide met `[CONFLICT]` — je kiest niet zelf, je meldt het. Zet bij een
dragende bewering de bronmarkering die eraan vastzit: beoogd, verwacht, deels, betwist, volgens wie.

**K — wat de bron verbindt.** Elk oorzaakverband dat de bron **werkelijk legt**, met vindplaats:
`K1 F7 → F9, "waardoor", §2`.

**N — wat de bron náást elkaar zet.** Gegevens die in dezelfde passage staan zonder dat de bron een
verband legt. Dit blok is even belangrijk als K en wordt meestal vergeten. Alles hieruit schrijf je
als nevenschikking — "en", "tegelijk", een puntkomma — nooit als oorzaak, ook niet met een dubbele
punt, en nooit met een motief erbij.

Klaar als elk getal uit de bron in F staat, K compleet is, en je van elke bronalinea kunt zeggen of
zij iets aan de lijst heeft toegevoegd of leeg was.

**Zoek dan de spanningen.** Dit is geen creatieve stap maar een zoekopdracht over je eigen lijst — je
vindt ze, je verzint ze niet. Vijf vindplaatsen, op opbrengst gesorteerd:

1. **Plan tegenover uitkomst.** Wat was beloofd, wat werd het? Het doel, de businesscase, de raming.
2. **Wie betaalde tegenover wie profiteerde.** De klassieke wrong pocket, en bijna altijd aanwezig.
3. **Het gegeven dat de bron kort en neutraal houdt.** De vertrokken partner, het geld dat niet kwam,
   het doel dat niet gehaald werd — in één passieve bijzin weggezet. Dat staat er niet voor niets zo,
   en dit is de opbrengstrijkste vindplaats van de vijf.
4. **Het gegeven dat de bron noemt en daarna niet gebruikt.** Een resultaat dat in geen conclusie
   terugkomt, een bedrag dat nergens wordt afgewogen.
5. **Wat er na de looptijd gebeurde.** Wat ging door, wat stopte, en wie betaalt het nu.

Schrijf **drie kandidaten** op in `kern.md`, elk als één zin in de vorm `X, terwijl Y`, met achter
beide helften het F-nummer. Drie echt verschillende: drie andere paren gegevens, niet drie
formuleringen van hetzelfde paar. Krijg je een kandidaat niet in deze vorm, dan is het een mening en
geen spanning, en gaat hij weg — ook als hij goed klinkt.

Zet achter elke kandidaat **wat de lezer moet opgeven als hij haar aanvaardt.** Dat is geen
dekkingstoets — de vorm heeft de dekking al geregeld — maar het criterium waarop je *kiest*. Een
spanning die de lezer niets kost, is waar maar niet interessant.

**Vul `kern.md` aan met drie regels, en niet meer.**

- **Het bezwaar.** Wat werpt je doellezer tegen? Ook dit is een bewering over de zaak met een
  F-nummer eronder — geen spreker, geen citaat, geen motief dat je iemand toeschrijft. Plus je
  antwoordrichting: *toegeven en inperken*, *weerleggen met F<n>*, of *verplaatsen naar de echte
  weerstand* (niet de tegenstanders van je voorstel, maar de logica die het tegenhoudt).
- **Het oordeel.** Jouw weging van de spanning, en niets meer: "voor dit resultaat vinden wij dat te
  veel geld". Een weging mag stelliger zijn dan de bron, een feit nooit. Eén per tekst, en het
  scherpst is het oordeel dat je zelf iets kost. Kan de spanning het oordeel zelf vellen doordat de
  twee getallen naast elkaar staan, dan is dat de sterkere vorm: laat de analyse het oordeel vellen
  in plaats van het uit te spreken.
- **Wat eruit gaat.** Minstens één ding dat het concept behandelt en dat de spanning niet dient,
  inclusief één ding dat een sjabloon wél had opgenomen. Kun je niets noemen, dan heb je
  geparafraseerd in plaats van gedistilleerd.

Levert de lijst geen enkel paar dat een spanning oplevert, dan is de tekst een opsomming en hoort dat
zo te blijven: schrijf beschrijvend en chronologisch, en meld het. Een verzonnen spanning is erger
dan geen.

**Is er een gebruiker in het gesprek**, leg de drie kandidaten dan voor in één `AskUserQuestion`,
samen met het teksttype en de doellezer zoals jij ze leest. Eén vraagmoment, niet meer. **Is er geen
gebruiker** — een onbeheerde run, een pijplijn, een subagent — dan kies je zelf de kandidaat die de
lezer het meest kost, en bij gelijke stand die uit vindplaats 3. Meld het in het logboek en vraag niet
alsnog "voor de zekerheid": een vraag die je zelf gaat beantwoorden is overhead.

## Stap 2 — De vorm

Kies één architectuur, expliciet. Niet elke tekst is een piramide.

| Architectuur | Beweging | Kies hem als | Faalt als |
|---|---|---|---|
| **Knelpunt → casus → les → aanbeveling** | de huisvorm | het materiaal bestaat uit voorbeelden die tot een aanbeveling moeten leiden | de les elke keer met dezelfde formule opent |
| **Antwoord eerst** | conclusie bovenaan op elk niveau, dan het bewijs | de lezer moet iets besluiten en heeft drie minuten | het antwoord zo algemeen is dat niemand het bestrijdt |
| **De omkering** | begin bij wat de lezer gelooft, haal het onderuit, eindig waar hij niet rekende | je spanning spreekt de gangbare lezing tegen | die gangbare lezing een stroman is |
| **De rekening** | wat het kostte tegenover wat het opleverde, in één orde; het oordeel valt uit de rekensom | de cijfers zelf het argument zijn | de twee kolommen verschillende noemers hebben |

Zet daaronder de beweringen in volgorde, één per toekomstige alinea, met achter elke bewering de
F-nummers die haar dragen. Een bewering zonder F-nummer is een gat: afzwakken of schrappen. Eén
ordeningsas voor het geheel — tijd, onderdelen, of afnemend gewicht — en niet mengen. Dan drie
snelle toetsen:

- **En dus?** Kun je het antwoord op die vraag niet in één stap aan de kop erboven hangen, dan gaat
  de bewering eruit. Dit haalt gewoonlijk 20 tot 40 procent uit een AI-concept, vóór je er zinnen aan
  verspilt.
- **Ongelijke gewichten.** De zwaarste sectie is minstens 1,8× de mediane en draagt de spanning; daar
  gaan het concrete geval en het getal dat ertoe doet heen. Het lichtste onderwerp krijgt één zin.
  Gelijke secties zijn het teken dat niemand koos.
- **Horizontaal lezen.** Lees alleen de koppen achter elkaar. Levert dat je spanning op? Koppen zijn
  beweringen, geen labels, en ze verschillen in lengte en vorm — zie `stem.md` §6.

Onder ongeveer 350 woorden sla je de tabel over: de beweringen op een rijtje, hoogstens vier, geen
tussenkoppen maar wél een titel.

## Stap 3 — Het proza, bron dicht

**Sluit nu de bron.** Met subagent: geef de schrijver `lijst.md`, `kern.md`, deze stap en `stem.md`,
en zet in de briefing letterlijk *"Er is geen brontekst en die krijg je ook niet. Wat niet in
`lijst.md` staat, bestaat niet: schrijf `[GAT: …]` waar je iets mist. Verzin geen getal, naam,
jaartal, citaat, motief, mechanisme, oorzaak, rangorde of vergelijking."* Solo: zet `BRON GESLOTEN`
in je werknotitie en open de bron niet tot de slotpas.

Twee dingen die de sandbox oplegt, en die in ronde 8 allebei fout gingen:

- **Een getal dat je zelf uitrekent, mag alleen als beide componenten letterlijk in je geleverde
  tekst staan**, met dezelfde noemer, en zonder dat het totaal de delen verdringt. Een som van drie
  inwoneraantallen die zelf niet in de tekst staan, is een verzonnen getal.
- **Een motief, een interpretatie en een rangorde zijn beweringen over de wereld**, geen stijl. "Te
  lezen als het besluit van één partij", "een toezegging bindt pas als…", "die stelden hun geld wél
  beschikbaar" — alle drie hebben een F- of K-nummer nodig, en zonder dat gaan ze eruit.

Schrijf dan in één doorloop van de eerste zin naar het slot. `stem.md` is de stem: het genre, de
gemeten cadans, het lexicon en negentien bewegingen uit gepubliceerd werk. Drie dingen daaruit die
het meest opleveren, en één plafond.

**De eerste zin is een zaklamp, geen inleiding.** Hij toont wat er aan de hand is. Kun je hem
schrappen zonder verlies, dan is het geen opening. Niet "in dit hoofdstuk", niet "hieronder". De
spanning staat uitgeschreven in de tekst, uiterlijk in alinea drie en onder de 400 woorden in alinea
twee.

**In elke alinea van vier of meer zinnen staat één zin onder de tien woorden, en die draagt de
pointe.** Dit is de enkele regel die in het corpus de goede passages van de zwakke scheidt. De korte
zin gaat vóór het grote getal: eerst adem, dan het bedrag. En zet hem niet aan het einde van de
alinea — daar is het een klapzin en die zijn gerantsoeneerd, in het midden is het een pointe en die
is gratis.

**Elk kerncijfer staat naast datgene waar het iets betekent:** het doel, het totaal waarvan het een
deel is, de partij die betaalde, het jaar ervoor. De cijferalinea zonder zaak is waar elke variant in
de tests zakte.

**Het plafond op de figuren.** Elke beweging uit `stem.md` hoogstens één keer per document, en
daarbinnen: hoogstens één negatieparallel of spiegelpaar, hoogstens twee alinea's die eindigen op een
oordeel van acht woorden of minder, hoogstens twee schaalvertalingen. Het beste exemplaar verleidt
tot het tweede; vanaf het derde leest de lezer de procedure en niet de zaak.

### Twee poorten

Deze twee zijn geen metingen maar leveringseisen, en het verschil is wezenlijk. **Een teller haal je
door de zin lelijker te maken; een poort niet.** "Wijs de zin aan die iemand zou doorsturen" kun je
niet faken. In ronde 9 zakte de tekst precies hier, op geen enkele meting.

1. **Per sectie minstens één doorstuurbare zin:** een zin die zijn pointe houdt als je hem alleen
   citeert, zonder de rest van de sectie erbij. Kun je hem niet aanwijzen, dan is die sectie niet af —
   schrijfpas, geen melding in het logboek.
2. **Per alinea één eigen punt dat nergens anders staat**, en de eerste zin van de alinea *is* dat
   punt. Een label is geen punt: "De uitkomst week af van het plan" kondigt aan wat er komt en zegt
   zelf niets. Kun je het punt van een alinea niet in één zin in de kantlijn schrijven, of schrijf je
   er twee, dan moet die alinea samengevoegd of gesplitst — en zonder eigen punt gaat zij eruit.

**En een opsomming uit de bron wordt proza.** Vier bullets die vier gelijkgevormde zinnen worden, is
de bullet-lijst met een punt erachter: de lezer ziet de lijst nog. Kies er één als de bewering van de
alinea, maak de andere ondergeschikt, of laat er twee weg. Dit was in ronde 9 het duidelijkste teken
van machinewerk dat de jury noemde.

Schrap onderweg de zin die uitlegt wat de vorige zin betekende, en de aankondiging en de
samenvatting. Het slot draagt een oordeel, een gevolg of een vooruitwijzing — nooit een kaal feit,
nooit een samenvatting, en het herhaalt de kop niet.

## De slotpas

Vier handelingen. Nu mag de bron weer open: om te controleren, niet om eruit te putten. De laatste
handeling op de tekst is altijd een schrijfpas, nooit een schrapronde.

1. **Wijs aan, beide kanten op.** *Heen:* loop F af, met per feit één uitkomst — `staat er, exact` /
   `bewust weggelaten` / `afwijkend`. Elk `[D]`-feit dat ontbreekt komt er alsnog in; elk afwijkend
   cijfer is een fout, geen stijlkwestie. *Terug:* onderstreep in je tekst **elke bewering over de
   wereld** — elk getal, elke naam, elk oorzaakverband, elke rangorde, elk motief, elke interpretatie,
   elk woord dat sterkte uitdrukt — en wijs voor elk de regel in `lijst.md` aan, of je eigen weging.
   Lukt geen van beide, dan gaat het eruit, ook als het klopt en ook als de zin eromheen jouw oordeel
   is. Let apart op wat geen signaalwoord heeft: de dubbele punt die een verklaring belooft, het
   "beide" of "daarmee" dat twee gegevens knoopt, de volgorde die als gevolg leest, de kop die een
   oorzaak aankondigt die de alinea niet levert. Wat in N staat, blijft nevenschikking. *Verlies:*
   lees de bron één keer op leessnelheid met één vraag — welke **betekenis** staat hier die niet in
   mijn tekst staat? Niet: welke formulering.
2. **Tel.** Draai `meetlat.py` of tel met de hand. `ROOD` op figuren, spreker, cijfers of woorden is
   hard: schrijfpas op die passage, geen reparatie van de zin. `LET` op pointe, ritme of rangorde
   wijst een passage aan en schrijft geen getal voor — ritme is iets wat je hoort, niet iets wat je
   haalt. Voegt een reparatie op het ene punt een overtreding op het andere toe, dan repareerde je
   niet. Hoogstens twee rondes; daalt het aantal roden niet, houd de vorige versie.
3. **Lees hardop**, in één doorgang, zonder terug te lezen. Waar je midden in een zinsdeel adem moet
   halen, waar je tong vastloopt, waar je stem vlak wordt: herschrijf die zin. Elke zin die je bij
   eerste lezing moet herlezen wordt herschreven, ook als een meting daar slechter van wordt. Loop
   daarna de twee poorten na en wijs ze aan: de doorstuurzin per sectie, het eigen punt per alinea.
   Controleer ook of elke zin een vindbaar onderwerp heeft — een verwijswoord ("die", "dat",
   "daarmee", "het") wijst terug naar iets in dezelfde of de vorige alinea, en reikt het verder, dan
   schrijf je het antecedent uit. In ronde 9 verloor de sterkste zin van de tekst zijn onderwerp. Leg
   tot slot begin, midden en slot naast elkaar: dezelfde schrijver?
4. **Laat iemand anders lezen.** Een verse subagent, of solo één schone doorloop waarbij je de
   antwoorden opschrijft vóór je iets aanraakt. Geef hem alleen de tekst, het teksttype en de
   doellezer — niet de bron, niet deze skill, niet je spanning.

   > Lees dit één keer op leessnelheid, zoals op een dinsdagmiddag. Je leest niet terug. (1) Vanaf
   > welke zin ging je scannen? (2) Wat weet je nu nog, zonder terug te kijken — maximaal drie
   > dingen? (3) Welke ene zin zou je doorsturen? Citeer letterlijk; GEEN is een geldig antwoord.
   > (4) Welke zin moest je twee keer lezen? (5) Wat wilde deze tekst je laten geloven, geloofde je
   > het, en wat had je ertegen in te brengen? (6) Is dit geschreven door iemand die erbij was, of
   > door iemand die het heeft samengevat? Geen advies, geen stijloordeel; rapporteer wat je waarnam.
   > "Niets te melden" is een geldig antwoord.

   Geslaagd als: niet gescand; twee van de drie onthouden dingen raken de kern; er is een
   doorstuurzin; vraag 4 is "geen"; bij vraag 5 noemt hij je spanning en niet je onderwerp; vraag 6
   is "iemand die erbij was". Noemt hij een sterker bezwaar dan het jouwe, dan koos je in stap 1 het
   verkeerde — terug naar stap 1, geen zinskwestie. Zegt hij "samengevat", dan mist de tekst
   concreetheid en geen stijl. Hoogstens één terugronde, en dan met een nieuwe lezer.

Dan lever je: eerst de plakklare tekst, dan een regel `---`, dan het logboek van **vier regels**.
Verder niets — geen inleiding, geen varianten, geen vraag achteraf.

```
1 Spanning   "<X, terwijl Y>" — X uit F<n>, Y uit F<n>; de lezer geeft op: <…>; keuze <gebruiker|zelf>
2 Bezwaar    <het bezwaar als bewering, F<n>> — antwoord <toegeven|weerleggen F<n>|verplaatsen>; oordeel: "<de zin>"
3 Vorm       <architectuur>, as <tijd|onderdelen|gewicht>; <N> → <M> woorden (−<x>%); weggelaten: <wat>
4 Controle   F <n>/<n> terug, afwijkingen <geen|welke>; afgeleid <welke, uit welke twee>; N gerespecteerd <ja|welke herschreven>; poorten <doorstuurzin per sectie, punt per alinea: ja|welke>; lezer <uitkomst>; open <geen|wat>
```

## Het telscript

Optioneel maar aanbevolen, want tellen is precies wat een schrijver slecht kan en een script goed.
Zeven metingen, elk ontleend aan wat de juryrondes daadwerkelijk afstraften. Draai het op de tekst
zonder logboek: `python3 meetlat.py tekst.md`.

Hard: **figuren** (negatieparallel ≤ 1, klapzin ≤ 2, schaalvertaling ≤ 2) · **spreker** (directe rede
of een personage dat vraagt of vindt: nul) · **cijfers** (twee waarden binnen één procent van elkaar
zijn meestal dezelfde grootheid, twee keer verschillend opgeschreven) · **woorden** (de
verbodenlijst, en de eigen lievelingsformules samen hoogstens één per 500 woorden).

Richtinggevend: **pointe** · **ritme** · **rangorde** (elke vergelijkende of overtreffende trap; het
script wijst ze aan, jij rekent ze na tegen de andere getallen in dezelfde eenheid).

Faken is verboden. Elke drempel is te halen door de zin lelijker te maken, en dat ziet de lezer uit
handeling 4 meteen. Haal je een drempel alleen door de zin te beschadigen, laat hem dan vallen en
noteer dat in regel 4.

## Als het niet lukt

- **Geen enkele kandidaat komt in de vorm `X, terwijl Y`.** Dan zegt het concept werkelijk niets, en
  dat is de bevinding: schrijf kort wat er staat en meld wat je miste. Een lege tekst is geen slechte
  tekst, en dit is geen reden om er alsnog een stelling bij te verzinnen.
- **De drie kandidaten gebruiken hetzelfde paar gegevens.** Dan heb je er één gevonden en twee
  geherformuleerd. Ga terug naar de vindplaatsen: 3 en 4 leveren bijna altijd een tweede paar.
- **Je mist een gegeven tijdens het schrijven.** Schrijf `[GAT: …]` en ga door. Niet de bron openen,
  niet iets aannemelijks invullen. In de slotpas zie je of het gegeven in F stond en je het over het
  hoofd zag, of dat de bron het niet levert.
- **De twee gegevens vragen om een verklaring.** Ze staan in N en nu dringt zich een reden op. Dat is
  het moment waarop je hem gaat verzinnen. Laat ze naast elkaar staan; de lezer legt het verband zelf,
  en dat zit vaster dan jouw verklaring.
- **Je wilt "grootste", "belangrijkste" of "vooral" gebruiken.** Dat is een bewering over alle
  alternatieven die je niet hebt bekeken. Reken hem na tegen elk ander getal in F in dezelfde eenheid,
  of laat de rangorde weg en noem het gegeven gewoon.
- **Je komt niet onder de bronlengte.** Dan heb je geschoven, niet gekozen. Terug naar stap 2 en kijk
  naar de beweringen: meestal beantwoorden twee secties dezelfde vraag.
- **Alles klopt en niets blijft hangen.** Geen poetsprobleem. Terug naar stap 1: je spanning kost de
  lezer niets, of je nam die uit vindplaats 1 terwijl 3 er een betere had.

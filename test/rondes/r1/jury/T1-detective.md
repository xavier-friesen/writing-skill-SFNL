# Juryrapport T1 — forensische lens

Brontekst: 710 woorden (schoongemaakt: zonder frontmatter, kopmarkeringen en
lijstmarkeringen; de bron declareert zelf 674). Alle percentages hieronder zijn
tegen 710 gerekend, voor alle vijf op dezelfde manier.

**Kalibratienotitie vooraf, over afgeleide getallen.** Vier van de vijf outputs
rekenen met de feitenlijst: "ruim een vijfde", "anderhalf keer", "bijna twee
derde", "zes procentpunt", "vier op de vijf", "drie keer zo groot", "172.000
inwoners". Ik hanteer voor allemaal dezelfde regel, anders is de
diskwalificatieregel niet consistent toe te passen: een exacte rekenkundige
afleiding uit feiten die wél op de lijst staan, is *presentatie* ("cijfers mogen
anders worden gepresenteerd"), geen verzinsel. Geen van de vijf wordt daarom op
grond van een afgeleid getal gediskwalificeerd. **Risicomelding:** bij een
strikt letterlijke lezing van §5.1 ("staat er een getal … in dat niet in de bron
of de feitenlijst voorkomt") loopt B tegen het plafond van 4,0 aan wegens
"172.000 inwoners" — het enige nieuwe *absolute* getal in het veld. Ik pas dat
plafond niet toe, maar leg het hier vast zodat de orchestrator de keuze kan
terugdraaien. Onder diezelfde regel zou A dan ook vallen ("ruim een vijfde",
"drie keer zo groot"), en dat lijkt me niet de bedoeling van de regel.

---

```
OUTPUT A

Cijfers      D1 8  D2 8  D3 6  D4 7  D5 8  D6 8  D7 6  D8 8
Tellpunten   T1 1  T2 0  T3 2  T4 0  T5 2  T6 0  T7 0  T8 0  T9 1  T10 2   totaal 8
Hardop       3 struikelingen; zin: "De verzekeraar heeft 62 procent van de regionale markt in handen en had van alle betrokken partijen dus juist het meeste te winnen bij minder doorverwijzingen naar de specialistische jeugdhulp."
Doorstuur    uit hoofd; zin: "De baten kwamen terecht bij het onderwijs en de leerplichtketen, die geen cent hadden ingelegd."
Lengte       bron 710 woorden, output 587 woorden, −17,3 procent
Feitencheck  akkoord op alle 15 items; geen getal, naam, jaartal of citaat buiten de lijst.
             Wel drie claims op hogere sterkte dan de bron toelaat — zie D7.

R = 7,40   T = 0,8   B = +0,5   E = 7,1   plafond toegepast: hardopplafond op D3 (max 6)

Turingpoort  nee — vier korte klapzinnen in 587 woorden plus een zelf aangelegde
             oorzaakketen is de handtekening van een tekst die op narratieve
             sluitendheid is geoptimaliseerd, niet op wat het dossier draagt.
```

**AI-detectietoets, alle tien langs.**

- **T1 = 1.** "Dat is geen boekhoudkundig detail." Schrap hem: er verdwijnt geen
  informatie, alleen nadruk. Grensgeval dat ik níét meetel: "Daar zit de les,
  want de rekening kwam bij de gemeenten en de verzekeraar terecht, terwijl de
  opvallendste opbrengst landde bij een partij die er geen euro in had gestoken."
  — de zin als geheel draagt wel informatie, dus hij doorstaat de schraptoets.
- **T2 = 0.** Geen decoratief drietal. "onderwijs, wijkteams en eerstelijnszorg"
  is een feitelijke opsomming uit de bron; het derde lid is niet het zwakste.
- **T3 = 2.** Drie negatieconstructies: "Dat is geen boekhoudkundig detail." /
  "Het gaat dan niet over de vraag of preventie werkt, maar over wie de opbrengst
  mag bijschrijven." / "Zo'n uitstap is te repareren aan de uitkomstenkant, niet
  met een oproep tot meer commitment." De tweede is een echt contrast en zou
  alleen 0 tellen als hij de enige was; vanaf de tweede is het per regel altijd 2.
- **T4 = 0.** Geen aankondigingsalinea, geen samenvattingsalinea. De bron had er
  twee; die zijn weg.
- **T5 = 2.** "Vermoedelijk zit een deel in de kosten van gegevensuitwisseling
  tussen de betrokken organisaties, al moet nader onderzoek dat uitwijzen." Drie
  verzachters in één zin (vermoedelijk / een deel / al moet nader onderzoek).
  Stapeling in één zin is per regel altijd 2. Verzachtende omstandigheid, die ik
  in D2 verreken en niet hier: de zin ervóór ("Waar dat geld heen ging, is
  overigens niet hard gemaakt.") zet de onzekerheid eerst hard neer.
- **T6 = 0.** Geen enkel gedachtestreepje. De bron had er drie. Schoonste
  categorie van het hele veld — alle vijf outputs scoren hier 0.
- **T7 = 0.** Secties 87 / 90 / 111 / 173 / 89 woorden. De sectie met het
  zwaarste materiaal is bijna twee keer zo lang als de rest. Dit is de enige
  output waarin de sectielengte informatie is.
- **T8 = 0.** De slotalinea bevat het besluit van 2026, een herrekening en een
  aanbeveling. Schrappen kost informatie.
- **T9 = 1.** "aan de uitkomstenkant". Lidwoord-plus-coinage in precies de vorm
  die de rubriek beschrijft; een gemeentelijk beleidsadviseur heeft
  "uitkomstenkant" niet eerder gelezen.
- **T10 = 2.** Vier klapzinnen: "Het lukte gedeeltelijk, en niet voor wie
  betaalde." / "Die winst is echt." / "Dat is geen boekhoudkundig detail." /
  "Meanders vertrek is rationeel." Eén mag; vier is een tic.

**Bewijs vóór menselijkheid (sterkst).** "Zo'n uitstap is te repareren aan de
uitkomstenkant, niet met een oproep tot meer commitment." Dit is een expliciete
verwerping van de conclusie die de brontekst zélf trekt ("Dit onderstreept het
belang van een zorgvuldige verankering van commitment"). Een model dat een
brontekst herschrijft, neemt de conclusie van die bron over of vervlakt hem; het
gaat er zelden frontaal tegenin. Daarbovenop: "Meanders vertrek is rationeel." —
een verdediging van de partij die het rapport impliciet als schuldige aanwijst.
Dat is ongemakkelijk, en ongemak is duur.

**Bewijs vóór machine-herkomst (sterkst).** "Veldhorst telt 58.000 inwoners,
Oostermeer 41.000 en Lindendaal 73.000." Deze zin staat als vijfde zin in een
verder scherpe lead, doet daar niets, en is een tussenzin die tot zelfstandige
zin is gepromoveerd. Hij is er om feit 2 af te vinken. Dat is geen redactionele
keuze maar het afwerken van een lijst — precies wat een generator doet als hij
een verplichting moet inlossen die niet in het betoog past. Op de tweede plaats:
de zelf aangelegde oorzaakketen ("landt die winst bij een andere partij, dan
verdwijnt op termijn de reden om nog een keer mee te tekenen. Precies dat
gebeurde halverwege de looptijd."). De bron noemt nergens een reden voor
Meanders vertrek. Een tekst die een verhaal wil laten sluiten en daarvoor een
causaal verband bijmaakt dat het dossier niet levert, doet het ding dat modellen
het vaakst doen.

**Overige tells (tellen in D4, niet in T).**
- "De verzekeraar heeft 62 procent van de regionale markt in handen en had van
  alle betrokken partijen dus juist het meeste te winnen bij minder
  doorverwijzingen naar de specialistische jeugdhulp." Het "dus" is een
  gefabriceerde gevolgtrekking, en inhoudelijk twijfelachtig: jeugdhulp valt in
  Nederland onder de Jeugdwet en dus onder de gemeente, niet onder de
  zorgverzekeraar. Een schrijver met dossierkennis maakt deze fout niet.
- "Die daling is bijna twee keer zo groot als de 11 procent waarvoor het
  programma wel was ingericht." Vergelijkt 19% verzuimdaling met 11%
  instroomdaling: andere noemer, andere populatie. Retorisch effectief,
  analytisch onzuiver.
- "Tussen 2021 en 2024" is smaller dan feit 1 ("van 2021 tot en met 2024").

**Dimensies, kort onderbouwd.**
- **D1 = 8.** "Vroeg Verbonden kostte 4,2 miljoen euro en haalde de helft van wat
  de businesscase beloofde." Naam, bedrag, oordeel, veertien woorden, niet
  schrapbaar. Het frame van het hele hoofdstuk staat er. Geen 9, omdat de alinea
  daarna terugvalt in de inwonersopsomming.
- **D2 = 8.** Nul keer waarbij / middels / in het kader van / ten aanzien van.
  Handelende partijen als onderwerp. Drie zinnen van dertig woorden of meer, die
  twee van de drie keer goed gebouwd zijn.
- **D3 = 6.** Plafond uit de hardop-leestoets. Op eigen kracht zou dit een 7 zijn:
  zinslengtes van 4 tot 31 woorden, en "Die winst is echt." komt aan omdat er
  twee vlakke zinnen aan voorafgaan. Maar de klapzin wordt vier keer ingezet.
- **D4 = 7.** Neemt standpunten in, laat de aankondiging en de zoom-out weg,
  maakt de secties ongelijk omdat het materiaal ongelijk is. Daartegenover: de
  klapzin-tic, "Daar zit de les", en de verzonnen causaliteit.
- **D5 = 8.** Elke sectie heeft een onderstreepbare zin; "De baten kwamen terecht
  bij het onderwijs en de leerplichtketen, die geen cent hadden ingelegd." haalt
  het 10-anker (citeerbaar zonder context). Geen 9 wegens "Die winst is echt."
  en de onzuivere 19%-vs-11%-vergelijking.
- **D6 = 8.** Reverse outline levert een betoog: het kostte 4,2 miljoen, het
  haalde de helft, de opbrengst landde elders, dus de financier stapte op, dus
  moet 2026 anders. Niets omwisselbaar. Aftrek voor de inwonerszin op de
  verkeerde plek en voor 4.4, waarvan het kopje de halve inhoud niet dekt.
- **D7 = 6.** Alle vijftien feiten correct aanwezig, niets verzonnen aan getallen
  of namen. Maar drie claims staan sterker dan de bron toelaat (motief Meander,
  belang verzekeraar, vergelijkbaarheid 19%/11%). Dat is exact het 6-anker.
- **D8 = 8.** −17,3 procent, geen feit weg, geen samenvattende alinea over.

**Sterkste zinnen**
1. "Vroeg Verbonden kostte 4,2 miljoen euro en haalde de helft van wat de
   businesscase beloofde." — zet bedrag en oordeel in één hoofdzin en maakt de
   rest van het hoofdstuk daarmee leesbaar als toelichting.
2. "De baten kwamen terecht bij het onderwijs en de leerplichtketen, die geen
   cent hadden ingelegd." — de bijzin van vier woorden verandert een constatering
   in een aanklacht, zonder één feit toe te voegen.
3. "Zo'n uitstap is te repareren aan de uitkomstenkant, niet met een oproep tot
   meer commitment." — verwerpt bij naam de conclusie van de bron; hier is de
   schrijver op aanspreekbaar.

**Zwakste zinnen**
1. "Veldhorst telt 58.000 inwoners, Oostermeer 41.000 en Lindendaal 73.000." —
   D3: de stem wordt vlak, de zin biedt geen nadruk aan. D4: een feit dat wordt
   afgevinkt in plaats van gebruikt.
2. "De verzekeraar heeft 62 procent van de regionale markt in handen en had van
   alle betrokken partijen dus juist het meeste te winnen bij minder
   doorverwijzingen naar de specialistische jeugdhulp." — D2: dertig woorden.
   D7: het "dus" voert een gevolgtrekking op die de bron niet maakt en die in het
   Nederlandse stelsel waarschijnlijk onjuist is.
3. "Precies dat gebeurde halverwege de looptijd." — D7: presenteert een zelf
   aangelegd oorzakelijk verband als vaststaand; de bron geeft nergens een reden
   voor het vertrek van Meander.

---

```
OUTPUT B

Cijfers      D1 9  D2 8  D3 5  D4 7  D5 6  D6 7  D7 6  D8 8
Tellpunten   T1 0  T2 0  T3 2  T4 0  T5 2  T6 0  T7 2  T8 0  T9 0  T10 2   totaal 8
Hardop       3 struikelingen; zin: "Ze bond het geld niet en het grootste resultaat evenmin."
Doorstuur    uit hoofd; zin: "Het onderwijs stond wel in de doelstelling van het programma, maar niet in de betaalafspraak."
Lengte       bron 710 woorden, output 503 woorden, −29,2 procent
Feitencheck  afwijking: [feit 2: "Veldhorst (58.000 inwoners), Oostermeer (41.000
             inwoners), Lindendaal (73.000 inwoners)"] versus ["Veldhorst,
             Oostermeer en Lindendaal tellen samen 172.000 inwoners."]
             De drie afzonderlijke inwonertallen zijn verdwenen en vervangen door
             een sompost die nergens in bron of feitenlijst staat. Overige 14
             feiten akkoord.

R = 6,99   T = 0,8   B = +0,5   E = 6,7   plafond toegepast: hardopplafond op D3 (max 6),
                                          onderstreepplafond op D5 (max 6)

Turingpoort  nee — vijf opeenvolgende alinea's van 58 tot 64 woorden, elk
             eindigend op een korte klap, is een metronoom die geen redacteur
             zet.
```

**AI-detectietoets, alle tien langs.**

- **T1 = 0.** Geen zin die zegt dat iets belangrijk is in plaats van wat het is.
  "Het zwaarste verlies zat niet in de uitvoering maar in de financiering zelf."
  is een rangschikking mét inhoud; schrappen kost het frame van de alinea.
- **T2 = 0.** Geen decoratief drietal.
- **T3 = 2.** "Het zwaarste verlies zat niet in de uitvoering maar in de
  financiering zelf." / "Het onderwijs stond wel in de doelstelling van het
  programma, maar niet in de betaalafspraak." / "De partij die betaalt is dus
  niet de partij die incasseert." Alle drie zijn echte contrasten — de eerste zou
  0 tellen, maar vanaf de tweede is het per regel altijd 2.
- **T4 = 0.** Geen kopjes, geen aankondiging, geen samenvatting. B is de enige
  output die de hoofdstukindeling helemaal loslaat, en dat kost hem niets.
- **T5 = 2.** "Mogelijk komt dat deels doordat het uitwisselen van gegevens
  tussen de betrokken partijen duur uitpakte." Twee verzachters in één zin, plus
  een derde in de volgende ("Zeker is dat niet; nader onderzoek moet het nog
  uitwijzen.").
- **T6 = 0.**
- **T7 = 2.** Geen secties, maar de alinea's meten 36 / 37 / 46 / **58 / 60 / 64 /
  63 / 62** / 50 / 21 woorden. Vijf opeenvolgende alinea's binnen tien procent
  van elkaar, terwijl het materiaal ongelijk zwaar is: het financieringsgat
  krijgt exact evenveel ruimte als de kostenoverschrijding. Dit is de
  sectiesymmetrie van de bron, alleen verplaatst naar alineaniveau.
- **T8 = 0.** De slotalinea bevat het besluit van 2026; schrappen kost een feit.
  (Kwalitatief is hij niettemin de zwakste van de tekst — dat verreken ik in D6.)
- **T9 = 0.** "betaalafspraak", "prijs per uitkomst", "leerplichtketen" — allemaal
  opzoekbaar of uit de bron.
- **T10 = 2.** Drie alinea-afsluitende klappen: "Ze bond het geld niet en het
  grootste resultaat evenmin." / "Aan tafel hield ze niemand." / "De
  leerplichtketen had helemaal niets ingelegd."

**Bewijs vóór menselijkheid (sterkst).** De lead. "Zorgverzekeraar Meander zegde
€ 1,4 miljoen toe aan het programma Vroeg Verbonden en zag halverwege af van de
tweede tranche." B haalt het feit dat de bron in zijn laatste paragraaf begroef
naar zin één, en bouwt de hele tekst om dat feit heen. Dat is een
redactiebeslissing met kosten: de lezer krijgt de ontknoping vooraf en het
hoofdstuk moet die keuze de rest van de tekst waarmaken. Direct daarachter: "Het
onderwijs stond wel in de doelstelling van het programma, maar niet in de
betaalafspraak. De leerplichtketen had helemaal niets ingelegd." B is de enige
die ziet dat "onderwijs" en "leerplichtketen" in feit 13 níét dezelfde status
hebben — het onderwijs stond in de doelstelling, de leerplichtketen nergens.
Dat onderscheid staat in geen van de bronnen; het is uit twee feiten
samengesteld.

**Bewijs vóór machine-herkomst (sterkst).** De metronoom. Vijf alinea's van 58,
60, 62, 63 en 64 woorden op rij, elk met dezelfde interne vorm: openingszin die
het onderwerp aankondigt, twee tot drie feitenzinnen, korte slotklap. Dat is
zeven keer hetzelfde blok. Het is de "correct maar dood"-tell in zijn meest
verzorgde gedaante: de tekst leest soepel omdat elke alinea precies even lang
duurt, en dat is exact waarom hij niet gesproken klinkt. Op de tweede plaats de
chiasme "De afspraak bond partijen aan resultaat zolang zij aan tafel zaten. Aan
tafel hield ze niemand." — te net. Een omkering die precies past, met een
voornaamwoord dat een tel te laat landt, is de soort gladheid die je krijgt als
een tekst is geoptimaliseerd op klank in plaats van geschreven.

**Overige tells (tellen in D4, niet in T).**
- "Veldhorst, Oostermeer en Lindendaal tellen samen 172.000 inwoners." als
  voorlaatste zin van het hoofdstuk: een getal zonder argumentatieve functie op
  de meest prominente plek van de tekst. Dit is bovendien het enige nieuwe
  absolute getal in het veld (zie de kalibratienotitie).
- B neemt nergens een standpunt in dat aan een persoon toe te schrijven is. Alle
  oordelen zijn onpersoonlijk gesteld ("Dat kan de bereidheid … onder druk
  zetten"). Er staat geen aanbeveling in, geen "dit moet anders". De tekst
  diagnosticeert perfect en schrijft niets voor.
- Voornaamwoordwisseling in twee opeenvolgende zinnen ("zij" = partijen, "ze" =
  de afspraak) zonder markering.

**Dimensies, kort onderbouwd.**
- **D1 = 9.** Eerste zin: genoemde partij, bedrag, en de handeling die het hele
  hoofdstuk verklaart. Niet schrapbaar. Zin twee bouwt door en begint niet
  opnieuw. Beste opening van het veld.
- **D2 = 8.** Kort, actief, geen jargon, geen enkele nominalisatiestapeling. Drie
  zinnen die twee keer lezen vergen, waarvan twee door voornaamwoorden.
- **D3 = 5.** Plafond 6 uit de hardop-toets; ik zit er één onder wegens de
  alineametronoom. Op zinsniveau is het ritme goed; op alineaniveau is het een
  klok.
- **D4 = 7.** Sterke keuzes (lead, weglaten van de hele contextsectie, geen
  kopjes) tegenover de metronoom, de drievoudige klapzinformule en het ontbreken
  van elk standpunt.
- **D5 = 6.** Onderstreepplafond: de slotalinea bevat geen enkele onderstreepbare
  zin — twee inerte feiten en klaar. Verder wél sterk, maar "Dat kan de
  bereidheid om te investeren onder druk zetten." is de hedge van de bron
  ongewijzigd overgenomen, zonder getal of voorbeeld in dezelfde alinea.
- **D6 = 7.** De redeneerlijn is er en klopt ("een toezegging die halverwege kan
  worden opgezegd en een resultaat waarvoor niemand betaalt" is een verdiende
  conclusie). Maar de alinea die daarna nog komt, kan volledig weg met winst.
  Dat is een structurele fout op de meest zichtbare plaats.
- **D7 = 6.** Feit 2 is uitgekleed tot een sompost die in geen bron staat.
  Veertien van de vijftien feiten kloppen exact.
- **D8 = 8.** −29,2 procent, de strakste van het veld. Geen 9 omdat er wél een
  feit uit de lijst is verdwenen.

**Sterkste zinnen**
1. "Zorgverzekeraar Meander zegde € 1,4 miljoen toe aan het programma Vroeg
   Verbonden en zag halverwege af van de tweede tranche." — zet in één zin de
   toezegging en de intrekking naast elkaar, waarmee het hele hoofdstuk zijn
   onderwerp krijgt.
2. "Het onderwijs stond wel in de doelstelling van het programma, maar niet in de
   betaalafspraak." — maakt een onderscheid dat de bron niet maakt, uit twee
   feiten die de bron uit elkaar houdt.
3. "Wat die daling waard was, staat nergens in bedragen." — benoemt wat het
   dossier níét bevat, in plaats van eromheen te slalommen.

**Zwakste zinnen**
1. "Veldhorst, Oostermeer en Lindendaal tellen samen 172.000 inwoners." — D7: een
   getal dat in bron noch feitenlijst voorkomt, op de plaats van drie getallen
   die er wél in staan; D6: doet op de op één na laatste regel geen enkel werk.
2. "Ze bond het geld niet en het grootste resultaat evenmin." — D2: "ze" en "het
   geld" vragen allebei een tweede lezing; de vorige zin bond *partijen* aan het
   resultaat, niet het geld.
3. "Dat kan de bereidheid om te investeren onder druk zetten." — D5: de
   afzwakking van de bron ongewijzigd overgenomen; een abstractie zonder getal,
   naam of voorbeeld in dezelfde alinea.

---

```
OUTPUT C

Cijfers      D1 4  D2 6  D3 4  D4 4  D5 5  D6 5  D7 8  D8 7
Tellpunten   T1 2  T2 2  T3 2  T4 1  T5 2  T6 0  T7 2  T8 1  T9 1  T10 2   totaal 15
Hardop       5 struikelingen; zin: "Dat preventie op langere termijn betere uitkomsten oplevert, voor jongeren, voor gezinnen en voor het stelsel als geheel, is breed gedeeld."
Doorstuur    opgezocht; zin: "Het programma bleef achter op de doelen die het had afgesproken, en boekte resultaat op een terrein dat het niet had afgesproken."
Lengte       bron 710 woorden, output 541 woorden, −23,8 procent
Feitencheck  akkoord op alle 15 items; niets verzonnen. Kleine precisieafwijking:
             [feit 1: "liep van 2021 tot en met 2024"] versus ["liep van 2021 tot
             2024"] — sluit het laatste jaar strikt gelezen uit.

R = 5,13   T = 1,5   B = +0,3   E = 3,9   plafond toegepast: openingsplafond op D1 (max 5),
                                          hardopplafond op D3 (max 4),
                                          onderstreepplafond op D5 (max 6)

Turingpoort  nee — de rule of three, de hedgestapeling, de vetgedrukte
             labelbullets en de zoom-out-slotalinea van de bron hebben alle vier
             de herschrijving overleefd; dit is het concept, licht gestreken.
```

**AI-detectietoets, alle tien langs.**

- **T1 = 2.** "Die laatste post geeft het arrangement zijn karakter." en "Hier
  raakt Vroeg Verbonden aan een vraagstuk dat zich bij dit type arrangementen
  veelvuldig voordoet." Schrap beide: er verdwijnt geen informatie. De tweede is
  de "Dit illustreert een breder vraagstuk" van de bron, alleen anders bewoord.
- **T2 = 2.** Vier drietallen, alle vier uit de bron overgenomen: "De kosten …
  stijgen, de wachttijden lopen op en de vraag … groeit"; "voor jongeren, voor
  gezinnen en voor het stelsel als geheel"; "samenwerking, leren en
  verantwoording"; en het schoolvoorbeeld: "verankerd commitment, een
  realistische uitkomstenstructuur en een gedeeld beeld van de te verwachten
  baten." Streep bij die laatste het derde lid door — de lezer mist niets.
- **T3 = 2.** "Vroeg Verbonden is geen blauwdruk. Wat het wel laat zien: …" /
  "innovatieve financiering is geen doel op zich, maar een middel …" / "Die vraag
  gaat over meer dan wie betaalt; ze gaat evenzeer over wie leert." Dat laatste
  is de "niet alleen X maar ook Y" van de bron, omgekleed.
- **T4 = 1.** "Die laatste post geeft het arrangement zijn karakter." kondigt aan
  wat in de twee volgende zinnen komt. Verder is de aankondigingsalinea van de
  bron wél verdwenen, wat C krediet verdient.
- **T5 = 2.** "Vooralsnog lijkt die bijstelling deels te verklaren uit de relatief
  hoge kosten van gegevensuitwisseling tussen de betrokken organisaties, al is
  nader onderzoek op dit punt wenselijk." Vier verzachters in zesentwintig
  woorden, plus een actorloze constructie. De hedgestapeling uit de gebrekenlijst
  is vrijwel woordelijk blijven staan.
- **T6 = 0.**
- **T7 = 2.** Secties 90 / 135 / 93 / 95 / 103 woorden; de vier niet-bulletsecties
  liggen binnen veertien procent van elkaar terwijl het materiaal dat niet is.
  Daarnaast de opsomming zelf: vier bullets, alle vier vetgedrukt label plus
  toelichtende zin, dezelfde grammaticale mal. Dat is letterlijk het "tabel in
  vermomming"-patroon uit de gebrekenlijst, ongewijzigd.
- **T8 = 1.** De slotalinea bevat het besluit van 2026 (dus schrappen kost een
  feit), maar de retorische lading is volledig vooruitblik zonder gegeven, en de
  allerlaatste zin — "Die vraag gaat over meer dan wie betaalt; ze gaat evenzeer
  over wie leert." — voegt niets toe.
- **T9 = 1.** "uitkomstenstructuur". Uit de bron overgenomen, maar niet opzoekbaar
  en niet vervangen.
- **T10 = 2.** "Investeren moet alleen nu." (vier woorden, alinea-einde) en "Vroeg
  Verbonden is geen blauwdruk." (vijf woorden, alinea-opening), plus de
  dubbelepuntfragmenten "Wat het wel laat zien:" en "Dat gat legt drie
  voorwaarden bloot:".

**Bewijs vóór menselijkheid (sterkst).** "Investeren moet alleen nu." Vier
woorden met een woordvolgorde die je even moet herparsen ("alleen" in de
betekenis van "maar"). Precies die oneffenheid is wat een generator gladstrijkt.
Op de tweede plaats "Het programma bleef achter op de doelen die het had
afgesproken, en boekte resultaat op een terrein dat het niet had afgesproken." —
de enige zin in C die twee van de drie verhaallijnen aan elkaar knoopt, en de
enige die een oordeel bevat.

**Bewijs vóór machine-herkomst (sterkst).** C is de enige output die de
bulletlijst met vetgedrukte labelkopjes ongewijzigd laat staan. Vier bullets,
label plus toelichting, gelijke mal, gelijk gewicht — de gebrekenlijst noemt dit
patroon met zoveel woorden, en het heeft de herschrijving woordelijk overleefd.
Daaromheen: de rule of three vier keer, de hedgestapeling intact, de
zoom-out-slotzin intact ("innovatieve financiering is geen doel op zich, maar
een middel om samenwerking, leren en verantwoording aan elkaar te verbinden"),
en de sectiesymmetrie intact. Van de veertien ingebouwde gebreken zijn er in C
minstens zes onaangetast. Een ervaren redacteur zou hier geen halve seconde
aarzelen.

**Overige tells (tellen in D4, niet in T).**
- Vetdruk als structuurmiddel in de opsomming (vier keer), terwijl geen van de
  andere vier outputs vetdruk gebruikt.
- Drie alinea's van exact 56 woorden.
- Behouden lijdende vormen die de actor verbergen: "is een uitkering … van
  € 1.850 overeengekomen", "werden voorgefinancierd", "waarna de terugverdientijd
  is herberekend". Wie besliste, onderhandelde of herrekende, staat er nergens.
- "Vroeg Verbonden is geen blauwdruk." is een tegenwerping die wordt opgevoerd en
  meteen weggewuifd ("Wat het wel laat zien: …").

**Dimensies, kort onderbouwd.**
- **D1 = 4.** Openingsplafond. De eerste zin ("De kosten van jeugdhulp stijgen, de
  wachttijden lopen op en de vraag naar specialistische hulp groeit, terwijl de
  financiële ruimte van gemeenten beperkt blijft.") is zonder verlies schrapbaar;
  het grammaticale onderwerp is drie abstracties; de hele eerste alinea bevat
  geen getal, geen naam, geen bedrag en geen datum. De echte opening staat in zin
  vier.
- **D2 = 6.** Het 6-anker letterlijk: de meeste zinnen zijn helder, een handvol
  struikelt, en het zijn juist de zinnen die het mechanisme uitleggen die
  struikelen. Dat is het spiegelbeeld van het 10-anker.
- **D3 = 4.** Hardopplafond bij vijf struikelingen.
- **D4 = 4.** Symmetrisch, vlak, geen zichtbare keuze, geen zin waar iemand het
  mee oneens kan zijn, en de opvallendste tells van de bron staan er nog. Boven
  de 3 wegens "Investeren moet alleen nu." en het weglaten van de
  aankondigingsalinea.
- **D5 = 5.** Onderstreepplafond: sectie 4.3 (Resultaten) bevat geen enkele
  onderstreepbare zin — het is een cijferopsomming met een hedge eraan. Verder
  één goede zin met opvulling eromheen, precies het 6-anker, en een tikje eronder
  wegens de afgezwakte claims.
- **D6 = 5.** De sectievolgorde van de bron, min de aankondiging. 4.3 en 4.4 zijn
  omwisselbaar met beperkt verlies. De conclusie wordt aangekondigd ("Dat gat
  legt drie voorwaarden bloot") in plaats van afgeleid. De enige argumentatieve
  zin van de tekst staat in 4.4 en wordt in 4.5 niet opgepakt.
- **D7 = 8.** Braafste van het veld: alle vijftien feiten, niets verzonnen, geen
  claim opgeblazen. Alleen "van 2021 tot 2024" verliest precisie.
- **D8 = 7.** −23,8 procent, maar er is vooral geschaafd: de fillerfuncties
  (zoom-out, betekenis-inflatie, drietallen) staan er nog. Wat eruit ging waren
  woorden, geen secties.

**Sterkste zinnen**
1. "Het programma bleef achter op de doelen die het had afgesproken, en boekte
   resultaat op een terrein dat het niet had afgesproken." — de enige zin in C
   die twee verhaallijnen verbindt, en hij doet het met één herhaald werkwoord.
2. "Investeren moet alleen nu." — vier woorden met een hoorbare eigen stem, en
   het enige punt waar de tekst iets beweert dat de bron niet beweert.
3. "Blijft een doorverwijzing uit, dan wordt € 1.850 uitgekeerd; komt de
   doorverwijzing er toch, dan niet." — legt in één adem uit wat de bron in twee
   nominalisaties verstopt.

**Zwakste zinnen**
1. "De kosten van jeugdhulp stijgen, de wachttijden lopen op en de vraag naar
   specialistische hulp groeit, terwijl de financiële ruimte van gemeenten
   beperkt blijft." — D1 openingsplafond (schrapbaar zonder verlies, drie
   abstracties als onderwerp, geen concreet gegeven in de hele alinea) plus T2.
2. "Dat gat legt drie voorwaarden bloot: verankerd commitment, een realistische
   uitkomstenstructuur en een gedeeld beeld van de te verwachten baten." — T2:
   leerboekdrietal met het zwakste lid achteraan, rechtstreeks uit de
   gebrekenlijst; T9: "uitkomstenstructuur".
3. "Vooralsnog lijkt die bijstelling deels te verklaren uit de relatief hoge
   kosten van gegevensuitwisseling tussen de betrokken organisaties, al is nader
   onderzoek op dit punt wenselijk." — T5: vier verzachters in één zin, actorloos;
   de hedgestapeling van de bron vrijwel ongewijzigd.

---

```
OUTPUT D

Cijfers      D1 7  D2 8  D3 5  D4 7  D5 8  D6 8  D7 8  D8 6
Tellpunten   T1 1  T2 0  T3 1  T4 1  T5 0  T6 0  T7 2  T8 0  T9 0  T10 2   totaal 7
Hardop       3 struikelingen; zin: "Vroeg Verbonden zette daar van 2021 tot en met 2024 € 4,2 miljoen tegenover, in Veldhorst (58.000 inwoners), Oostermeer (41.000) en Lindendaal (73.000)."
Doorstuur    uit hoofd; zin: "Het contract bond te weinig partijen aan te weinig uitkomsten."
Lengte       bron 710 woorden, output 614 woorden, −13,5 procent
Feitencheck  akkoord op alle 15 items; niets verzonnen. Twee kleine
             sterkteverschuivingen: [feit 7: "gebaseerd op de gemiddeld vermeden
             kosten"] versus ["gelijk aan de kosten die een traject gemiddeld
             vermijdt"], en [feit 7: "per voorkomen doorverwijzing"] versus
             ["Blijft een gezin uit de specialistische jeugdhulp"].

R = 7,28   T = 0,7   B = +0,5   E = 7,1   plafond toegepast: hardopplafond op D3 (max 6)

Turingpoort  nee — vier kopjes van veertien tot zestien woorden, elk een
             volledige mededelende zin met een getal erin, is een
             generatorhandtekening; en in 614 woorden staat geen enkele
             woordkeuze die een model niet had gemaakt.
```

**AI-detectietoets, alle tien langs.**

- **T1 = 1.** "Dat is geen toeval van dit ene programma." Schrap hem: de volgende
  zin draagt de inhoud volledig. Grensgeval dat ik niet meetel: "Hoe smal die
  basis was, bleek halverwege de looptijd." — die draagt wel een oordeel.
- **T2 = 0.** Geen decoratief drietal. De slotaanbeveling heeft twee leden, geen
  drie, en dat is een zichtbare weerstand tegen de mal.
- **T3 = 1.** Eén rechtstreekse negatieopening ("Dat is geen toeval van dit ene
  programma."), en het contrast is echt: een lezer zou dit inderdaad als een
  incident kunnen lezen.
- **T4 = 1.** "Twee dingen horen dan in het contract." kondigt aan wat er komt.
  Zeven woorden, nuttig, maar schrappen kost geen informatie. Daarnaast een
  structureel bezwaar dat ik hier niet dubbel tel maar wel noteer: elk kopje
  bevat de conclusie van de sectie, waardoor de tekst zichzelf vijf keer
  vooruitvat.
- **T5 = 0.** De enige output zonder hedgestapeling. Waar de andere vier
  "vooralsnog / mogelijk / deels / lijkt" op elkaar stapelen, schrijft D: "Waar
  dat aan ligt, is niet hard te maken: de gegevensuitwisseling tussen de
  betrokken organisaties was relatief duur, maar hoeveel van de bijstelling
  daaruit volgt, moet nader onderzoek uitwijzen." Dat is een uitspraak over het
  bewijs, geen slag om de arm.
- **T6 = 0.**
- **T7 = 2.** Twee lagen. Secties 102 / 97 / 107 / 134 / 104 woorden: vier van de
  vijf binnen tien procent van elkaar. En de kopjes: 16 / 15 / 15 / 14 woorden,
  alle vier een complete mededelende zin, alle vier met een getal of jaartal
  erin. Dat is de "opsomming waarin elk item hetzelfde aantal woorden en dezelfde
  grammaticale vorm heeft", toegepast op kopniveau.
- **T8 = 0.** Het slot bevat het besluit van 2026 en twee concrete
  contractvoorschriften. Schrappen kost veel.
- **T9 = 0.** "prijslijst", "ongeprijsd", "betaalafspraak" — metaforisch of
  doorzichtig, geen verzonnen vakterm met lidwoord.
- **T10 = 2.** Zes korte klappen: "Het contract kende één prijs." / "Voor één
  uitkomst lukte dat." / "Dat leverde niemand een uitbetaling op." / "Juist die
  opbrengst bleef ongeprijsd." / "Het contract bond te weinig partijen aan te
  weinig uitkomsten." / "Waarom de verzekeraar afhaakte, is niet bekend." Vier
  van de acht alinea's eindigen op zo'n zin.

**Bewijs vóór menselijkheid (sterkst).** "Waarom de verzekeraar afhaakte, is niet
bekend." Dit is het sterkste anti-hallucinatiesignaal in het hele veld. Het
materiaal schreeuwt om een verklaring, twee andere kandidaten leveren er een
(A expliciet, E impliciet), en D zet er een grens. Een tekst die weigert het gat
in het dossier te vullen op de plek waar het verhaal er het meest bij gebaat zou
zijn, is een tekst die van bewijs uitgaat. Direct daarachter: "Dat sloeg een gat
van € 900.000, bijna twee derde van de € 1,4 miljoen die de verzekeraar had
toegezegd." Niemand vroeg om die herrekening; hij verandert wat feit 14 betekent
(Meander liet niet een tranche liggen, hij liet bijna zijn hele bijdrage
liggen). Dat is dossierwerk.

**Bewijs vóór machine-herkomst (sterkst).** De vier kopjes. 16, 15, 15 en 14
woorden. Alle vier een volledige zin met onderwerp en persoonsvorm. Alle vier
met een cijfer of jaartal erin. Deze regelmaat is niet redactioneel te
verklaren — een mens die vier boodschapkoppen schrijft, produceert er één van
zes woorden en één van achttien. En de prijs ervan is zichtbaar: kopje 4.3 luidt
"Op de deelnemende scholen daalde het langdurig verzuim met 19 procent, buiten
elke betaalafspraak om", waarna de tweede zin van die sectie luidt "Op de
deelnemende scholen daalde het aandeel langdurig verzuimende leerlingen met 19
procent." De mal dwingt de tekst tot woordelijke zelfherhaling.

Daarnaast, en dit is de tell die op geen enkele lijst staat: **D heeft geen
enkele oneffenheid.** In 614 woorden staat geen woordkeuze die verrast, geen
zinsbouw die wringt, geen formulering die alleen hier werkt. Elke zin is correct,
informatief, en uitwisselbaar van register met elke andere zin. C heeft
"Investeren moet alleen nu.", A heeft "Meanders vertrek is rationeel.", B heeft
"Aan tafel hield ze niemand." D heeft niets vergelijkbaars. Perfect gepolijste
afwezigheid van elke ruwheid is zelf een spoor.

**Overige tells (tellen in D4, niet in T).**
- Vijf zinnen die openen met "Dat" als terugverwijzend voornaamwoord: "Dat gat
  moet dicht…", "Dat leverde niemand…", "Dat is geen toeval…", "Dat zet de
  bereidheid…", "Dat sloeg een gat…". De "Dat + persoonsvorm"-opening is de
  commentaarzin die op de vorige zin reageert — vijf keer is een tic.
- "Dat is geen toeval van dit ene programma." is dezelfde generaliseringsgreep
  die E maakt ("Zo'n verschil is geen weeffout van dit ene contract"): een
  standaardgebaar om van casus naar patroon te schakelen.
- "Blijft een gezin uit de specialistische jeugdhulp" is niet hetzelfde als "een
  voorkomen doorverwijzing"; de omzetting maakt de eenheid van afrekening
  onnauwkeuriger dan feit 7 toestaat.

**Dimensies, kort onderbouwd.**
- **D1 = 7.** De eerste zin ("Gemeenten zien de kosten van jeugdhulp en de
  wachttijden oplopen, terwijl de financiële ruimte beperkt blijft.") is de
  veiligst denkbare zin over jeugdzorg: geen getal, geen naam, geen bedrag. Ik
  pas het openingsplafond niet toe, omdat het "daar … tegenover" in zin twee er
  syntactisch aan hangt. Maar de lead als geheel is uitstekend: hij landt in zes
  zinnen het hele betoog en eindigt op de these.
- **D2 = 8.** Handelende partijen als onderwerp, nul beleidsjargon, nul
  hedgestapeling, lange zinnen die lang zijn omdat er iets verbonden moet worden.
- **D3 = 5.** Plafond 6 uit de hardop-toets; ik zit er één onder omdat de vier
  volzin-kopjes de leesbeweging vier keer breken en omdat de klapzin zes keer
  wordt ingezet.
- **D4 = 7.** Zegt wat er moet gebeuren, benoemt wat het niet weet, rekent feiten
  tegen elkaar uit. Daartegenover de kopjesmal, de sectiesymmetrie, de
  "Dat"-openingen en het volledig ontbreken van textuur.
- **D5 = 8.** Elke sectie heeft een onderstreepbare zin. "Het contract bond te
  weinig partijen aan te weinig uitkomsten." haalt het 10-anker: citeerbaar
  zonder context, en de pointe blijft staan.
- **D6 = 8.** Reverse outline levert een betoog dat van voor naar achter loopt en
  eindigt in twee uitvoerbare voorschriften. Geen 9, omdat de kopjes elke
  conclusie vooraf weggeven: de lezer kan niets zelf afleiden.
- **D7 = 8.** Alle vijftien feiten correct, één verhelderende herrekening, twee
  kleine sterkteverschuivingen ("gelijk aan" waar de bron "gebaseerd op" heeft).
- **D8 = 6.** −13,5 procent, de langste van het veld, en dat terwijl B dezelfde
  vijftien feiten in 503 woorden kwijt kan. Dat is het 6-anker: er is geschoven,
  niet gesneden.

**Sterkste zinnen**
1. "Waarom de verzekeraar afhaakte, is niet bekend." — zet een grens op de plek
   waar het materiaal om een verhaal vraagt; zeven woorden die de betrouwbaarheid
   van de hele tekst omhoog trekken.
2. "Dat sloeg een gat van € 900.000, bijna twee derde van de € 1,4 miljoen die de
   verzekeraar had toegezegd." — rekent feit 14 tegen feit 5 uit en verandert
   daarmee wat de lezer denkt dat er gebeurd is.
3. "Wie de volgende ronde ontwerpt, kan die 19 procent dus niet als meevaller
   wegzetten." — richt een bevinding op een aanwijsbare lezer en maakt er een
   verplichting van.

**Zwakste zinnen**
1. "Op de deelnemende scholen daalde het aandeel langdurig verzuimende leerlingen
   met 19 procent." — D6/D8: bijna woordelijke herhaling van het kopje twee
   regels erboven; de boodschapkopmal dwingt de tekst alles twee keer te zeggen.
2. "Gemeenten zien de kosten van jeugdhulp en de wachttijden oplopen, terwijl de
   financiële ruimte beperkt blijft." — D1: de veiligst denkbare eerste zin, geen
   getal, geen naam, geen bedrag; alleen het "daar" in zin twee houdt hem
   overeind.
3. "Voor één uitkomst lukte dat." — T10: vijf woorden aan het slot van een
   alinea, de eerste van vier zulke sluitklappen in acht alinea's; bij de vierde
   draagt het middel geen betekenis meer.

---

```
OUTPUT E

Cijfers      D1 8  D2 7  D3 5  D4 6  D5 8  D6 6  D7 7  D8 9
Tellpunten   T1 2  T2 0  T3 2  T4 1  T5 2  T6 0  T7 1  T8 1  T9 1  T10 2   totaal 12
Hardop       3 struikelingen; zin: "Dat is één les; de andere is dat een raming die twee keer zo hoog ligt als de uitkomst geen enkele partij aan tafel houdt."
Doorstuur    uit hoofd; zin: "Een toezegging in twee tranches bleek iets anders dan een verplichting."
Lengte       bron 710 woorden, output 545 woorden, −23,2 procent
Feitencheck  akkoord op alle 15 items; niets verzonnen. Eén formulering die feit 11
             op eerste lezing verkeerd weergeeft: [feit 11: "Uitvoeringskosten:
             18% van het budget; begroot was 12%"] versus [kopje 4.3: "De
             uitvoering kostte anderhalf keer de begroting"].

R = 6,84   T = 1,2   B = +0,5   E = 6,1   plafond toegepast: hardopplafond op D3 (max 6)

Turingpoort  nee — twee exacte spiegelparen in 545 woorden plus een kopje dat
             zijn eigen getal verkeerd weergeeft; de symmetrie is hoorbaar
             geconstrueerd.
```

**AI-detectietoets, alle tien langs.**

- **T1 = 2.** "Dat laatste bestanddeel stuurt het gedrag." en "Zo'n verschil is
  geen weeffout van dit ene contract." Beide zeggen dat iets betekenis heeft in
  plaats van welke; beide zijn schrapbaar zonder informatieverlies.
- **T2 = 0.** Geen decoratief drietal.
- **T3 = 2.** "Zo'n verschil is geen weeffout van dit ene contract." / "Een
  toezegging in twee tranches bleek iets anders dan een verplichting." / "De
  structuur zoals ze nu is, rekent voorkomen doorverwijzingen af en schoolverzuim
  niet." Plus twee kopjes in negatievorm ("Wie profiteerde, had niet betaald",
  "Een toezegging bleek geen verplichting").
- **T4 = 1.** "Vroeg Verbonden combineerde daarom publiek en privaat geld in vier
  bestanddelen." kondigt de opsomming aan. Verder geen samenvattingsalinea.
- **T5 = 2.** "De gegevensuitwisseling tussen de betrokken organisaties was
  relatief duur en verklaart de overschrijding mogelijk deels." Twee verzachters
  in één zin, plus "relatief", plus de losse "Nader onderzoek daarnaar is
  wenselijk."
- **T6 = 0.**
- **T7 = 1.** Secties 89 / 143 / 59 / 121 / 96 woorden — genuinely ongelijk, en
  dat is het beste sectieprofiel van het veld op één na. Maar de opsomming telt:
  vier bullets van 18 / 19 / 19 / 23 woorden in dezelfde grammaticale mal. De
  vetdruk van de bron is eraf gehaald, de vorm is gebleven. Eén punt.
- **T8 = 1.** "Dat is te repareren." als slotzin: vier woorden die vaststellen dat
  iets kan, zonder één ding te noemen dat gedaan moet worden — terwijl de tekst
  twee kandidaten klaar had liggen. Schrappen van de hele slotalinea kost wel het
  besluit van 2026, vandaar 1 en geen 2.
- **T9 = 1.** "die ene teller" — "Alles wat het programma buiten die ene teller om
  oplevert, telt niet mee." Lidwoord plus coinage, in precies de vorm die de
  rubriek beschrijft ("de echte knop"). Doorzichtig, maar niet opzoekbaar.
- **T10 = 2.** "Dat is te repareren." (vier woorden, slot) / "Nader onderzoek
  daarnaar is wenselijk." (vijf woorden, alinea-einde) / "Dat laatste bestanddeel
  stuurt het gedrag." (zes woorden, alinea-opening) / "Voor een leerling die niet
  langer verzuimde, stond niets."

**Bewijs vóór menselijkheid (sterkst).** "Voor een voorkomen doorverwijzing stond
1.850 euro klaar. Voor een leerling die niet langer verzuimde, stond niets." Dit
is de best geconstrueerde passage van het hele veld: twee feiten uit de lijst,
naast elkaar gezet, en het oordeel ontstaat uit de plaatsing zonder dat er een
woord van commentaar bij staat. Daarnaast de sectielengtes: 59 woorden voor de
kosten, 143 voor de structuur, 121 voor de baten. Dat verschil is informatie.
E is de enige die de dunste sectie ook echt dun durft te laten.

**Bewijs vóór machine-herkomst (sterkst).** Diezelfde passage, en nog één. E
bevat twee exacte spiegelparen in 545 woorden: "Blijft een doorverwijzing uit,
dan komt dat bedrag vrij. Komt de doorverwijzing er toch, dan gebeurt er niets."
(negen woorden en negen woorden, identieke syntaxis, omgekeerde inhoud) en de
1.850-euro-passage hierboven. Eén zo'n paar is vakmanschap; twee in een
hoofdstuk van vijf secties is een procedé. Het is symmetrie die je hóórt worden
aangelegd — de rubriek noemt dit onder D3 als "geregisseerd". Op de tweede
plaats: het kopje "De uitvoering kostte anderhalf keer de begroting". Letterlijk
gelezen staat er dat de uitvoering 150 procent van het totale budget kostte,
terwijl feit 11 zegt dat het 18 procent van het budget was waar 12 procent was
begroot. Een menselijke eindredacteur die de cijfers in handen heeft gehad, laat
dit kopje niet staan; een pipeline die het kopje uit "anderhalf keer" genereert
zonder terug te kijken naar de noemer, wel.

**Overige tells (tellen in D4, niet in T).**
- De "19 procent" wordt in 4.1 genoemd zonder dat de lezer weet waarvan, en pas
  in 4.4 gedefinieerd ("Die 19 procent is de daling van het aandeel langdurig
  verzuimende leerlingen op de deelnemende scholen"). Bedoeld als spanning,
  leest als een definitie die te laat komt.
- De contextzin ("Gemeenten zien de kosten en de wachttijden voor jeugdhulp
  stijgen…") opent sectie 4.2, die over de financiële structuur gaat. Zichtbare
  naad: de zin is uit 4.1 verhuisd en niet opnieuw ingepast.
- "Zo'n verschil is geen weeffout van dit ene contract." is exact dezelfde greep
  als D's "Dat is geen toeval van dit ene programma." — een standaardgebaar.

**Dimensies, kort onderbouwd.**
- **D1 = 8.** "Vroeg Verbonden investeerde 4,2 miljoen euro in preventieve
  jeugdzorg." Naam, bedrag, handelend onderwerp, niet schrapbaar. De drie
  openingszinnen zetten samen het hele hoofdstuk neer. Geen 9 omdat de tweede
  alinea van 4.1 terugvalt in inventaris en omdat de 19 procent zonder noemer
  wordt neergezet.
- **D2 = 7.** Overwegend helder, maar drie zinnen vragen een tweede lezing, en de
  zwaarste ("Dat is één les; de andere is dat een raming die twee keer zo hoog
  ligt als de uitkomst geen enkele partij aan tafel houdt.") zet elf woorden
  tussen het onderwerp "een raming" en zijn persoonsvorm "houdt". Plus het kopje
  dat zijn eigen getal verkeerd weergeeft.
- **D3 = 5.** Plafond 6 uit de hardop-toets; één eronder wegens de twee
  spiegelparen en het bulletblok, die het ritme op twee plekken van buitenaf
  opleggen.
- **D4 = 6.** Ongelijke secties, één echt oordeel, één uitstekende juxtapositie.
  Daartegenover twee spiegelparen, het overleefde bulletblok, de
  standaardgeneralisering, en "Dat is te repareren." als generiek positief slot
  in minimale vorm. Het 6-anker: de opvallende tells zijn eruit, de tekst is nog
  steeds ontworpen.
- **D5 = 8.** Elke sectie heeft een onderstreepbare zin. "Alles wat het programma
  buiten die ene teller om oplevert, telt niet mee." vat het ontwerpgebrek samen
  in dertien woorden.
- **D6 = 6.** De lijn is er, maar je reconstrueert hem achteraf: de context zit in
  de verkeerde sectie, de 19 procent wordt te vroeg genoemd en te laat
  gedefinieerd, 4.3 is te dun om zelfstandig te bestaan, en de conclusie wordt
  vastgesteld in plaats van afgeleid.
- **D7 = 7.** Alle vijftien feiten aanwezig en correct in de lopende tekst. Aftrek
  voor het kopje dat feit 11 op eerste lezing verkeerd weergeeft, en voor "een
  raming die twee keer zo hoog ligt als de uitkomst [houdt] geen enkele partij
  aan tafel" — dat schrijft Meanders vertrek toe aan de overschatting, wat de
  bron nergens zegt.
- **D8 = 9.** −23,2 procent, alle feiten behouden, geen samenvattende alinea,
  geen fillersectie. De beste lengtediscipline van het veld.

**Sterkste zinnen**
1. "Alles wat het programma buiten die ene teller om oplevert, telt niet mee." —
   vat het constructiefout van het hele arrangement in dertien woorden, zonder
   één abstractie.
2. "Een toezegging in twee tranches bleek iets anders dan een verplichting." —
   maakt van feit 14 een contractuele les zonder er iets aan toe te voegen; staat
   zelfstandig overeind.
3. "Het schoolverzuim daalde met 19 procent, en daarvoor was niets afgesproken."
   — zet de eigenlijke bevinding van het hoofdstuk in de derde zin, verbonden met
   een kaal "en" waar de bron een hele sectie voor nodig had.

**Zwakste zinnen**
1. "De uitvoering kostte anderhalf keer de begroting" (kopje 4.3) — D7/D2:
   letterlijk gelezen staat er dat de uitvoering anderhalf keer het totale budget
   kostte; feit 11 zegt 18 procent van het budget tegen 12 procent begroot. De
   enige formulering in het veld die een feit uit de lijst op eerste lezing
   verkeerd weergeeft.
2. "Dat is één les; de andere is dat een raming die twee keer zo hoog ligt als de
   uitkomst geen enkele partij aan tafel houdt." — D2: onderwerp en persoonsvorm
   elf woorden uit elkaar; D7: schrijft het vertrek van Meander toe aan de
   overschatting, wat de bron niet ondersteunt.
3. "Dat is te repareren." — T8 en T10: een slot van vier woorden dat vaststelt
   dat iets kan zonder één ding te noemen dat moet gebeuren, in een hoofdstuk dat
   twee voor de hand liggende voorschriften klaar had liggen.

---

```
RANGSCHIKKING

1. D  E = 7,1
2. A  E = 7,1
3. B  E = 6,7
4. E  E = 6,1
5. C  E = 3,9

Beslissend verschil tussen 1 en 2: D markeert het gat in het bewijs waar A het
met een verhaal opvult.
  Uit nummer 1: "Waarom de verzekeraar afhaakte, is niet bekend."
  Uit nummer 2: "Precies dat gebeurde halverwege de looptijd."

Wat nummer 1 nog mist voor een 10: vervang de vier boodschapkoppen van 14 tot 16
woorden door korte, ongelijke kopjes — ze zijn de luidste machinehandtekening van
het hoofdstuk en ze dwingen 4.3 zijn eigen kopje woordelijk te herhalen. Schrap
de openingszin en begin op "Vroeg Verbonden zette van 2021 tot en met 2024 € 4,2
miljoen tegenover …". Snijd ongeveer negentig woorden weg en laat hooguit één
alinea eindigen op een klap van vijf woorden; nu doen er vier van de acht dat, en
D is met −13,5 procent de langste van het veld terwijl B hetzelfde werk in 503
woorden af heeft.
```

**Gelijkstand D–A, hoe gebroken.** Beide 7,1. Tiebreak D4: 7 om 7. Dan D5: 8 om
8. Dan D2: 8 om 8. Alle drie gelijk, dus beslissend is de vraag welke van de twee
ik zonder aanpassing naar de klant zou sturen. Dat is D. A's betoog rust op een
oorzakelijk verband dat A zelf heeft aangelegd (Meander stapte op omdat de
opbrengst elders landde) en op een gevolgtrekking over het belang van de
zorgverzekeraar bij minder jeugdhulpdoorverwijzingen die in het Nederlandse
stelsel waarschijnlijk onjuist is. Dat is niet met een redactieronde te
repareren; daarvoor moet de schrijver terug naar het dossier. D's kopjes zijn
lelijk en herstelbaar in vijf minuten.

**Naschrift over de Turingpoort.** Vijf keer nee. Geen van de vijf haalt 8,0, dus
het plafond bijt nergens, maar dat is geen toeval: het veld deelt drie
handtekeningen die een ervaren redacteur binnen een alinea ziet. Ten eerste de
korte slotklap aan het eind van de alinea, bij alle vijf minstens drie keer, bij
D zes keer. Ten tweede de hedgestapeling rond de gegevensuitwisseling, die bij
vier van de vijf vrijwel woordelijk uit de bron is blijven staan (alleen D
herschrijft hem tot een uitspraak over bewijs). Ten derde een maatregelmaat die
op precies één niveau per tekst zichtbaar wordt: bij C op sectieniveau, bij B op
alineaniveau, bij D op kopniveau, bij E op zinsparenniveau. Alleen A ontkomt aan
alle drie de symmetrievormen, en A betaalt dat met een verzonnen oorzaakketen.

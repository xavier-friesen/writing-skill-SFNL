---
name: sfnl-stem
description: Zet AI-concepttekst om in publiceerbare Nederlandse rapporttekst voor Social Finance NL door per passage de beweging van een gepubliceerd voorbeeld te volgen. Bevat een specimenbank van veertien passages uit SFNL-rapporten, NRC, WRR, SCP, ESB en Sociale Vraagstukken, geordend naar functie (opening, mechanisme, cijfer, kanttekening, overgang, casus, slot). Gebruik bij rapporthoofdstukken, bestuurlijke samenvattingen, casusteksten, projectpagina's en notities die naar buiten gaan.
---

# De stem

Schrijven leer je van geschreven werk, niet van regels. Een verbodslijst begrenst
de uitvoerruimte maar kiest er geen punt in; het resultaat is foutloos en dood.
Deze skill werkt andersom. Je bepaalt per passage welke functie hij vervult, je
leest de specimens met die functie, en je schrijft de passage opnieuw **in die
beweging**. Je leent het patroon. Nooit het materiaal.

De lat is niet "geen AI-patronen meer". De lat is: zou een redacteur van een goed
rapport deze passage laten staan, en onthoudt de lezer er één zin uit.

**Vier invarianten, boven alles.**

1. **Feiten blijven exact.** Elk getal, bedrag, jaartal, percentage, eigennaam en
   elke claimsterkte staat correct in de output of is weggelaten zonder de
   betekenis te verdraaien. Weglaten mag. Verdraaien niet.
2. **Niets verzinnen.** Geen nieuw getal, voorbeeld, citaat, naam of beeld dat
   niet in de invoertekst of het gesprek staat. **Ook niets uit de specimens.**
   De specimenbank levert bewegingen, geen inhoud. Zie de besmettingspoort.
3. **Korter dan de invoer.** Richtlijn 15 tot 35 procent, nooit langer.
4. **Levering is de tekst zelf**, plakklaar, plus een logboek van maximaal acht
   regels. Geen commentaar tussendoor, geen varianten, geen opties.

---

## Stap 1. De stemkeuze

Stel deze vier vragen in **één** AskUserQuestion-aanroep, vóór je iets schrijft.
Zijn de antwoorden al meegeleverd, sla de vraag dan over en gebruik ze.

**Vraag 1. Wat wordt dit, en voor wie?**
- *Rapporthoofdstuk* · beleidsadviseurs en bestuurders die het dossier kennen
- *Bestuurlijke samenvatting* · wethouder, directie of financier, leest twee minuten
- *Casetekst of projectpagina* · website; fondsen en gemeenten die voorbeelden zoeken
- *Notitie* · één opdrachtgever, intern gebruik

**Vraag 2. Welke stem?** (de smaakmonsters zijn citaten uit gepubliceerd werk;
ze illustreren de toon en mogen nooit in de output belanden)
- *Het pleidooi* · wij zijn de auteurs, stellig, het slot keert iets om. Smaak:
  "Dit ligt niet aan de vindingrijkheid of ondernemerschap van de initiatiefnemers.
  Dit ligt aan het systeem."
- *De analyse* · het oordeel valt in de feiten, niet in de bijvoeglijke naamwoorden.
  Smaak: "Dat is een verviervoudiging ten opzichte van 2025."
- *Het verslag* · probleem eerst, mensen als onderwerp, geen moraal aan het eind.
  Smaak: "Gemeenten draaiden vaak op voor de uitvoering, terwijl verzekeraars
  profiteerden van lagere zorgkosten."
- *De brief* · terughoudend, bron bij elke claim, kanttekening vóór de claim. Smaak:
  "Niet alle elementen zijn één-op-één overdraagbaar naar Nederland, maar ze laten
  wel zien dat het anders kan."

**Vraag 3. Welke zin moet de lezer over een week nog weten?** Bied drie
kandidaten aan die je **letterlijk uit de invoertekst** licht (de drie scherpste
beweringen die er al staan), plus "geen voorkeur, kies zelf". Verzin hier niets.
Dit is de belangrijkste vraag van de skill: hij bepaalt welke passage de tekst draagt.

**Vraag 4. Hoe hard snijden?**
- *15 procent korter* · alles moet mee, alleen de lucht eruit
- *25 procent korter* · standaard
- *35 procent korter* · hard snijden, secties mogen sneuvelen
- *Jij bepaalt* · op basis van wat de tekst aankan

### Defaults als de gebruiker afwezig is

Gebruik deze en meld ze in regel 1 van het logboek.

| Keuze | Default |
|---|---|
| Teksttype | Afleiden uit de invoer: tussenkoppen plus betoog = rapporthoofdstuk; één project met resultaten = casetekst; onder 400 woorden met aanbevelingen = bestuurlijke samenvatting; anders notitie |
| Lezer | Beleidsadviseur bij een gemeente of departement die het onderwerp kent, het dossier niet |
| Stem | *De analyse* bij rapporthoofdstuk en samenvatting; *Het verslag* bij casetekst en projectpagina; *De brief* bij notitie |
| Dragende zin | De bewering in de invoertekst met het scherpste feit dat de lezer niet ziet aankomen. Noem hem in het logboek |
| Lengte | 25 procent korter |

---

## Stap 2. De functiekaart

Lees de invoertekst één keer helemaal. Doe daarna drie dingen op papier, vóór je
één zin schrijft.

**A. Label elke passage met precies één functie.** Een passage is een alinea of
een groepje alinea's dat één ding doet. De labels zijn de zeven functies van de
bank: OPENING, MECHANISME, CIJFER, KANTTEKENING, OVERGANG, CASUS, SLOT.

Past er geen label, dan is er een achtste: **DRAAGT NIETS**. Dat is geen probleem
maar een vondst. Aankondigingsalinea's, samenvattende alinea's, "uitdagingen en
vooruitblik" en alinea's die uitleggen wat de vorige alinea betekende krijgen dit
label. Ze gaan eruit. Daar komt je lengtewinst vandaan.

**B. Weeg.** Wijs één passage aan die de tekst draagt (de dragende zin uit vraag 3
staat daar of hoort daar te komen). Die passage krijgt méér woorden dan hij nu
heeft. Alle andere leveren in. Netto is de tekst korter. Een tekst waarin elke
sectie evenveel inlevert, is een tekst waarin niemand heeft gekozen.

**C. Trek de feitenlijst.** Noteer elk getal, bedrag, jaartal, percentage, elke
eigennaam en elke claim met zijn sterkte ("overweegt" is niet "besluit", "ruim
driehonderd" is niet "340"). Dit is het enige materiaal dat je hebt. Alles wat je
straks schrijft, komt hiervandaan of is taal.

Volgorde mag je veranderen: een volgorde is taal, geen feit. Zet het bewijs waar
het werkt, niet waar het stond.

---

## Stap 3. Schrijven in de beweging

Dit is de motor. Per passage, in deze volgorde. Geen stap overslaan.

1. **Neem uit de feitenlijst wat déze passage moet dragen.** Maximaal vijf items.
   Meer dan vijf betekent dat het twee passages zijn.
2. **Lees de twee of drie specimens van die functie.** Schrijf de beweging voor
   jezelf op in één zin: "eerst het probleem in acht woorden, dan het mechanisme
   zonder vakterm, dan een gevolgzin die begint met daardoor."
3. **Leg de brontekst weg.** Kijk er niet naar terwijl je schrijft. Dit is de
   enige stap die de verankering aan de slechte formulering echt doorbreekt. Wie
   een slechte zin repareert, erft zijn informatievolgorde en zijn beeld.
4. **Schrijf de passage vanaf je vijf items, in die beweging.** Niet de zinnen van
   het specimen invullen met jouw feiten: de beweging maken met jouw feiten.
5. **Leg de bron er pas nu naast**, en alleen om te controleren of er een feit is
   weggevallen of van sterkte veranderd. Niet om formuleringen terug te halen.
6. **Doe de twee waarborgtoetsen** hieronder. Pas dan door naar de volgende passage.

### Waarborg 1: de besmettingstoets

Streep in je nieuwe passage elk zelfstandig naamwoord, elk getal, elke eigennaam
en elk beeld aan dat óók in het specimen staat. Elk daarvan is besmetting, tenzij
het woord ook in de invoertekst voorkomt. Verwijder het.

Deze woorden en getallen staan in de bank en mogen dus **nooit** in je output
staan zonder dat ze in de invoer stonden: Kinzigtal, shared savings, Anne, €5.000,
girale tegoed, blusvliegtuig, klinknagel, boorgat, Victoria, 265.600,
verviervoudiging, uitzendbureaus, schoonmaakbedrijven, 9,4 procent, 11,7 procent,
33 euro, 55 euro, valincidenten, valpreventie, Stevig Staan, HIB, katalysator,
Social Impact Bonds, heilig, 287 tot 678 euro, langstrekkende stoet, WRR,
aansprekend en solide, machteloosheid en onbehagen.

### Waarborg 2: de pastichetoets

Twee vragen aan je eigen passage.

- Beginnen jouw zin en de specimenzin met hetzelfde woord, en hebben ze dezelfde
  lengte en dezelfde bouw? Dan heb je nagedaan in plaats van geleend. Schrijf hem
  opnieuw met dezelfde beweging maar een andere ingang.
- Zou een lezer die het specimen kent zeggen "dit is een imitatie"? Dan is het er
  een.

Drie aanvullende grenzen:

- **Eén specimen per passage.** Twee specimens tegelijk levert een collage op.
- **Formuleplafond: elke beweging maximaal twee keer per document.** Drie
  openingen die met "Maar" draaien, drie sloten die iets omkeren, drie casussen
  die met "laat zien dat" eindigen: dan is de bank een sjabloon geworden. Varieer,
  of laat een passage bewust vlak. Vlak is beter dan gemanierd.
- **Past geen enkel specimen, schrijf dan zonder.** Kort, plat, mededelend. Een
  eerlijke mededeling verslaat een geforceerde beweging. Naslag, lijsten en
  tabellen hoeven geen beweging te maken.

---

## De menselijke laag

Deze zes gelden tijdens elke passage van stap 3. Ze zijn het verschil tussen een
tekst zonder fouten en een tekst met een auteur.

**1. Een auteur met standpunt.** Het oordeel valt in de feiten, niet in de
bijvoeglijke naamwoorden. Niet "deze aanpak bleek niet effectief", maar de twee
getallen naast elkaar, waarna de lezer het zelf concludeert. Toets: staat er in de
hele tekst één zin waarop de auteur over drie jaar afgerekend kan worden? Zo nee,
is er geen auteur. Die zin bouw je uit materiaal dat er al ligt, nooit uit een
nieuw feit. Elke claim krijgt een genoemd subject: de gemeente, het fonds, het
RIVM. "Er wordt gewerkt aan" heeft geen auteur en geen dader.

**2. Asymmetrie.** Belang bepaalt lengte. De dragende passage uit stap 2B krijgt
meer ruimte dan hij nu heeft; twee andere leveren daarvoor in. Toets: tel de
woorden per sectie. Liggen alle secties binnen twintig procent van elkaar terwijl
het materiaal ongelijk zwaar is, dan heb je geschoven en niet gekozen. Ongelijke
lengte is informatie voor de lezer.

**3. Weglating.** Schrap de zin die uitlegt wat de vorige zin betekent. "De
aanbieder haalde 38 procent. De afspraak was 60 procent." is af; wat erachter komt
is bemoeienis. De lezer die zelf concludeert, is overtuigd; de lezer die de
conclusie krijgt aangereikt, is geïnformeerd. Weglaten geldt ook voor goed
materiaal: één sterk voorbeeld verslaat drie voorbeelden.

**4. Modale partikels dragen de toon.** *toch, juist, immers, nu eenmaal, wel
degelijk, althans, overigens, weliswaar, zij het.* Dit is geen ruis en geen
stopwoord; dit is waar Nederlands een houding in legt. Poets ze niet weg. Gebruik
er hooguit één per alinea, anders wordt het gepraat. Gebruik ook het bredere
verbindingsregister (*immers, namelijk, vandaar dat, temeer daar*) in plaats van
drie keer *daarnaast* en *bovendien*.

**5. De SFNL-vierslag voor elk mechanisme.** In deze volgorde, altijd:
   1. Noem het ding bij zijn naam, met een dubbele punt erachter.
   2. Beschrijf de geldstroom met genoemde actoren, in de tegenwoordige tijd: wie
      betaalt wie, wanneer, waarvoor.
   3. Zet de voorwaarde in een conditionele inversie: "Blijven de kosten
      daaronder, dan…" / "Worden de doelen gehaald, dan…"
   4. Sluit af met het gedragsgevolg, in één korte zin.

   Geen analogie uit een ander domein. Verhelder met een tweede zin, niet met een
   vergelijking. Beeldspraak alleen uit het eigen vak: schotten, potjes, hefboom,
   spelregels. Jargon mag, mits binnen dezelfde zin afgelost. Houd bij een langere
   uitleg één concreet geval vast door de hele uitleg heen.

**6. Ritme-engineering.** Schrijf de zinslengtereeks van elke alinea op, in
woorden. `22 – 21 – 11 – 5` is een alinea die werkt: de val van 21 naar 5 draagt de
betekenis. `23 – 25 – 35` is een alinea die wegzakt. Regels:
   - In elke alinea van vier of meer zinnen staat minstens één zin onder de tien
     woorden, en **die zin draagt de pointe**.
   - De korte zin gaat vóór het grote getal, niet erna. Eerst adem, dan het bedrag.
   - Per tien opeenvolgende zinnen: minstens één onder de acht woorden, minstens
     één boven de vijfentwintig.
   - Sterkste woord op de eindpositie. Lees de laatste woorden van een alinea
     achter elkaar; zijn het functiewoorden, herschrijf.
   - Herhaal liever dan te variëren. Eén ding, één naam. Vier synoniemen voor
     hetzelfde traject maken er in het hoofd van de lezer vier dingen van.

---

## De specimenbank

Veertien passages uit gepubliceerd werk, geordend naar functie. Elk citaat is
letterlijk. De duiding zegt wat de passage technisch doet; dát is wat je leent.

### A. OPENING

**A1. De opening die draait.** NRC, over het tekort aan blusvliegtuigen.

> Maar halverwege het recentste filmpje volgt de realiteit. In een productiehal
> in het West-Canadese Victoria vertellen monteurs hoe zij de toestellen in
> elkaar zetten. Zonder robots, zonder geavanceerde productielijnen. Elk
> boorgat, elke klinknagel plaatsen ze met de hand. Zo werkt de fabriek toe naar
> een productie van tien tot twaalf toestellen per jaar.

"Maar" vooraan kantelt het beeld dat de lezer net had. Dan drie steeds kortere
zinnen, waarvan de derde geen werkwoord heeft. Het abstracte woord (schaarste)
valt nooit; het getal sluit af, op de nadrukpositie.

**A2. Het knelpunt als stelling.** Social Finance NL, *Innovatieve financiering
van preventie* (2025), opening hoofdstuk 3.

> Partijen vinden investeren in preventie vaak onaantrekkelijk. De kosten zijn
> direct, terwijl de opbrengsten pas later komen en bovendien niet altijd
> terechtkomen bij de partij die betaalt. Tegelijk ervaren veel uitvoerders een
> spanningsveld: zij willen investeren in gezondheid en welzijn, maar worden
> gestuurd door bekostigingssystemen die vooral zorgverlening op basis van volume
> belonen. Daardoor kunnen kansrijke preventieve aanpakken moeilijk opschalen en
> blijven ze tijdelijk en kwetsbaar.

Zin één is acht woorden en bevat het hele hoofdstuk. Zin twee levert het
mechanisme zonder één vakterm. De dubbele punt in zin drie splitst wat mensen
wíllen van waar ze door gestuurd wórden: de spanning wordt grammaticaal zichtbaar.
Het slot begint met "daardoor" en is dus een gevolg, geen herhaling.

**A3. De opening met een standpunt.** Social Finance NL (2025), voorwoord.

> In dit rapport zetten we pioniers op een voetstuk die op een andere manier
> (samen)werken of financieren en hiermee verbluffende resultaten boeken. Maar
> veel projecten, zowel in dit rapport als in de praktijk van Social Finance NL,
> hebben moeite om op te schalen. Dit ligt niet aan de vindingrijkheid of
> ondernemerschap van de initiatiefnemers. Dit ligt aan het systeem.

Ritme `22 – 21 – 11 – 5`. De hele passage bestaat om die laatste zin te kunnen
zeggen. De herhaling "Dit ligt niet aan… Dit ligt aan…" is de goedkoopste
retorische figuur die er is en hier de juiste, omdat de tweede zin veertien
woorden korter is. Let op de zelfkritiek: het huis neemt zichzelf mee in de
diagnose, en daarom gelooft de lezer de rest.

### B. MECHANISME

**B1. De vierslag.** Social Finance NL (2025), Gesundes Kinzigtal.

> De kern van het model is een shared savings-contract: de jaarlijkse zorguitgaven
> in de regio worden vergeleken met een risicogecorrigeerde, landelijke norm.
> Blijven de kosten daaronder, dan wordt de besparing gedeeld tussen de
> zorgverzekeraars en Gesundes Kinzigtal GmbH; deelnemende zorgverleners profiteren
> via het netwerk van die opbrengsten. […] Deze prikkelstructuur maakt gezondheid
> economisch aantrekkelijk. In plaats van meer behandelingen leveren partijen juist
> waarde door minder zorg nodig te maken. Gezondheid, niet productie, bepaalt het
> rendement.

Het complete huispatroon in zes zinnen: naam met dubbele punt, rekenregel,
conditionele inversie, verdeling per genoemde partij, en dan drie zinnen die
uitsluitend over gedrag gaan. Slotzin zes woorden met een ingesloten contrast.
Lengtereeks `22 – 25 – 18 – 6 – 15 – 6`: de constructie kost lange zinnen, wat de
constructie dóét kost korte.

**B2. Begin bij de misvatting.** WRR, *Geld en schuld* (2019).

> Veel mensen menen dat banken eerst geld ophalen en dat geld vervolgens
> uitlenen aan andere mensen. Dat is echter niet hoe het werkt in het huidige
> systeem. Wanneer iemand een lening krijgt bij een bank, creëert de bank
> tegelijkertijd de lening en het girale tegoed (het geld). Stel Anne wil €5.000
> lenen van de bank om een auto te kopen. Als de bank akkoord gaat en de lening
> rond is, verhoogt de bank het girale tegoed van Anne met €5.000 en is er nieuw
> geld gecreëerd.

Begint bij wat de lezer denkt, niet bij de definitie. "Dat is echter niet hoe het
werkt" is de kortste zin en draagt de kern. Daarna één persoon, één bedrag, één
auto, en datzelfde geval blijft staan tot het einde. De lezer kan het navertellen.
De passage is bewust redundant: dat is een investering, geen slordigheid.

### C. CIJFER DAT DRAAGT

**C1. Het cijferpaar.** Social Finance NL (2025), §2.1.

> Het ziekteverzuim in de zorgsector is structureel hoog; vooral langdurig verzuim
> neemt toe. Daarnaast overweegt één op de vijf zorgprofessionals binnen een jaar
> de sector te verlaten. Volgens de meest recente arbeidsmarktprognoses voor de
> zorgsector loopt het tekort aan zorgmedewerkers in 2034 op tot maar liefst
> 265.600. Dat is een verviervoudiging ten opzichte van 2025.

`13 – 14 – 20 – 8`. Het grote getal krijgt de langste zin, de duiding de kortste.
Het absolute getal zegt niets tot de volgende zin het schaalt. Het cijfer heeft
een bron, en "maar liefst" is het enige stukje kleur in vier zinnen: één keer per
pagina mag dat.

**C2. Van percentage naar beroep.** ESB, over productiviteitsgroei.

> Het aandeel van deze laatstgenoemde sector nam toe van 9,4 procent in 2010
> naar 11,7 procent in 2019, terwijl het productiviteitsniveau veertig procent
> lager ligt dan het gemiddelde voor de hele Nederlandse economie (33 euro
> versus 55 euro per uur). Onder de Overige zakelijke dienstverlening vallen
> onder meer uitzendbureaus, schoonmaakbedrijven en beveiliging.

Het statistische begrip wordt eerst vertaald naar een prijs per uur die twee
kanten heeft, en dan pas naar drie herkenbare beroepen. De korte slotzin maakt een
hele sectorcategorie voorstelbaar. Techniek: laat het cijfer landen op iets wat de
lezer op straat is tegengekomen.

### D. KANTTEKENING

**D1. Het eigen instrument relativeren.** Social Finance NL, *De toekomst van
resultaatfinanciering* (2024), voorwoord.

> Social Finance NL is opgericht door de architecten van de eerste Social Impact
> Bonds in Nederland. Dat wil niet zeggen dat dit middel daarom voor ons heilig is.
> Maar het heeft ons wel geleerd hoe we resultaatgerichte samenwerkingsvormen
> mogelijk kunnen maken.

Drie zinnen, drie bewegingen: belang verklaren, belang relativeren, claim overeind
zetten. De volgorde is alles: het bezwaar wordt toegegeven vóórdat de lezer het kan
formuleren. "Heilig" benoemt het verwijt door het te ontkennen. De kanttekening
verzwakt het betoog niet, ze koopt geloofwaardigheid.

**D2. De tegenwerping toetsen in plaats van wegwuiven.** Samenleving & Politiek.

> Ik neem even de proef op de som. Veronderstel dat een werknemer kortstondig
> werkloos is en vervolgens een voltijdse job aanneemt ter hoogte van het
> interprofessionele minimumloon. In de gesimuleerde situaties gaat de
> voormalige werkzoekende er maandelijks netto 287 tot 678 euro op vooruit.
> Enkele honderden euro's extra per maand, voor wie leeft op een bescheiden
> budget zijn dat substantiële bedragen.

De gangbare stelling wordt niet als vijand neergezet maar als toetsbare bewering,
en dan getoetst. De bandbreedte is eerlijker dan één getal zou zijn. De slotzin
verplaatst het bedrag naar het perspectief van wie het aangaat, en dat is waar het
oordeel valt zonder dat iemand oordeelt.

### E. OVERGANG

**E1. Twee overgangsvormen.** Social Finance NL (2025), einde §2.1 en §2.3.

> Preventie zou daarbij geen bijzaak moeten zijn, maar een noodzakelijke pijler
> onder een houdbaar zorgstelsel. De volgende paragraaf verkent waarom.

en

> Om te begrijpen waarom preventie, ondanks brede steun, nog geen vanzelfsprekend
> onderdeel is van ons zorgstelsel, moeten we stilstaan bij de belangrijkste
> knelpunten die dit in de weg staan.

De eerste vorm: een stelling, dan vijf woorden die de lezer doorsturen. De tweede:
de vraag die de volgende paragraaf beantwoordt, geformuleerd als reden om door te
lezen. Geen van beide kondigt inhoud aan. Een overgang is nooit langer dan één
zin, tenzij hij zelf een argument is.

### F. CASUS EN HET CONCRETE GEVAL

**F1. Probleem eerst, oplossing pas in de laatste zin.** Social Finance NL
(2025), Stevig Staan.

> Valincidenten zijn de grootste oorzaak van letsel en blijvende zorgafhankelijkheid
> bij ouderen. De directe zorgkosten bedroegen in 2024 €1,5 miljard en deze stijgen
> naar verwachting tot €5 miljard in 2050. Hoewel bewezen is dat valtrainingen en
> beweegprogramma's deze kosten kunnen beperken, ontbrak het in 2022 nog aan
> structurele financiering. Gemeenten draaiden vaak op voor de uitvoering, terwijl
> verzekeraars profiteerden van lagere zorgkosten. Daardoor voelde geen enkele
> partij zich financieel verantwoordelijk om te investeren.

Vijf zinnen die een verdeelprobleem uitleggen zonder de vakterm te gebruiken.
Opbouw: omvang, prijs, paradox (het werkt wél maar wordt niet betaald), wie betaalt
tegenover wie profiteert, en één zin conclusie. De lezer lost het probleem zelf op
vóór de tekst het doet. Daarom werkt de oplossing als hij komt.

**F2. Perspectief naar wie het aangaat.** Sociale Vraagstukken.

> In elk geval zijn inwoners en cliënten er de dupe van. In wijken is het een
> komen en gaan van elkaar aflossende organisaties en personen. Bewoners zien de
> langstrekkende stoet van professionals en hulpwerkers met lede ogen aan. Er is
> nauwelijks de tijd zich aan iemand te binden.

Het perspectief verschuift van beleid naar bewoner en blijft daar. Er is één beeld
in de hele alinea en dat beeld draagt haar. De slotzin is de kortste en formuleert
de prijs. Gebruik dit waar een casustekst dreigt te vertellen wat er gebeurde in
plaats van wie het overkwam.

### G. SLOT

**G1. Het instrument opheffen.** Social Finance NL (2025), Stevig Staan.

> De HIB fungeerde als katalysator: een tijdelijk instrument om een bewezen
> interventie te financieren tot structurele inbedding mogelijk werd. Die stap is
> inmiddels gezet: sinds 2023 ontvangen gemeenten vaste middelen voor
> valpreventie. […] Daarmee heeft de HIB gedaan wat hij moest doen: het
> investeringsgat overbruggen, de meerwaarde van preventie aantonen en de weg
> openen naar reguliere financiering.

Drie dubbele punten met drie functies: definitie, bewijs, opsomming. Het slot
prijst het instrument en heft het tegelijk op: "gedaan wat hij moest doen"
impliceert dat het nu overbodig is. Een organisatie die haar eigen instrument
overbodig verklaart, wordt geloofd.

**G2. Het slot dat minder claimt dan het zou kunnen.** WRR, *Grip* (2023).

> In dit rapport biedt de WRR geen oplossingen voor die verschillende crises,
> maar één aanbeveling kunnen we wel doen: investeer in plannen die aansprekend
> en solide zijn. Aansprekend doordat ze perspectief bieden op een daadwerkelijk
> betere toekomst, en solide omdat ze gebaseerd zijn op de best mogelijke kennis
> van hoe de wereld werkt. Alleen al de wetenschap dat we als samenleving een
> plan hebben om de problemen aan te pakken, kan de scherpe kantjes van gevoelens
> van machteloosheid en onbehagen afhalen.

Begint met wat het rapport níét levert en koopt daarmee geloofwaardigheid voor wat
volgt. De aanbeveling staat in de gebiedende wijs met een werkwoord dat een
handeling is. De twee bijvoeglijke naamwoorden worden meteen gedefinieerd, in
dezelfde volgorde. Onderbieden overtuigt beter dan overbieden.

### Wat in alle veertien terugkomt

Bij twijfel over een herschrijving: toets hieraan.

1. Het concrete komt vóór het abstracte. De term valt pas als de lezer het geval al ziet.
2. Eén getal of één beeld per alinea. Twee verzwakken elkaar.
3. De kortste zin draagt de kern, niet de langste.
4. Waar het materiaal al oordeelt, verdwijnen de bijvoeglijke naamwoorden.
5. Het slot claimt minder dan het zou kunnen.

---

## Stap 4. Het stemanker

Zodra één passage staat waar je tevreden over bent, bevries hem als anker. Houd
elke volgende sectie er letterlijk tegenaan: dezelfde aanspreekvorm (wij is de
auteur, nooit het valse inclusieve wij; geen u), dezelfde tijd (tegenwoordige tijd,
verleden tijd alleen voor casushistorie en resultaten), dezelfde afstand, dezelfde
dichtheid.

Bij teksten van meer dan duizend woorden: lees aan het eind het oudste en het
nieuwste deel achter elkaar. Daar loopt het register altijd uiteen.

---

## Stap 5. De eindtoets

Vijf poorten. Meer meten maakt geen enkele zin mooier, dus meet niet meer.

**1. Feitenpoort.** Loop je feitenlijst uit stap 2C regel voor regel af. Staat elk
item correct in de output, of is het weggelaten zonder verdraaiing? Staat elke
claim op zijn oorspronkelijke sterkte? Is elk getal dat twee keer voorkomt beide
keren hetzelfde? Staat er niets in dat niet uit de invoer komt? Eén afwijking en
de tekst is af te keuren, hoe goed hij ook leest.

**2. Besmettingspoort.** Zoek de verbodslijst uit waarborg 1 letterlijk op in je
output. Nul treffers, tenzij het woord ook in de invoertekst stond. Zoek daarnaast
op eigennamen en getallen die je nergens in de invoer terugvindt.

**3. Onderstreeppoort.** Heeft elke sectie één zin die een lezer zou onderstrepen
en die zijn pointe zonder de omringende alinea's houdt? Zo niet, schrijf die
sectie opnieuw vanaf stap 3. Niet bijschaven: opnieuw. Een sectie zonder
onderstreepbare zin is een sectie zonder bestaansrecht.

**4. Tellspoort.** Eén doorloop, mechanisch. Weg met: het gedachtestreepje als
bijzin, drieslagen waarvan het derde lid leeg is, "niet alleen X maar ook Y",
belangwoorden (cruciaal, essentieel, van groot belang, markeert een belangrijke
stap, onderstreept het belang van), meta-zinnen over de tekst zelf, de aankondigende
eerste alinea, de samenvattende laatste alinea, vage attributie (experts stellen,
onderzoek toont aan), gestapelde voorbehouden, elegante variatie, Title Case in
koppen, vetdruk als nadruk, versterkers (zeer, uiterst, aanzienlijk, nadrukkelijk),
voorzetseluitdrukkingen (in het kader van, met betrekking tot, ten aanzien van,
middels). Let ook op de eigen lievelingsformules: "laat zien dat", "zo ontstaat",
"structureel", "duurzaam" maximaal twee keer per document.

**5. Lengtepoort.** Tel de woorden voor en na. Binnen de gekozen bandbreedte, en
altijd korter dan de invoer.

**En dan de laatste handeling, en die is een schrijfhandeling.** Lees de hele
tekst hardop, op leessnelheid, in één doorgang. Waar je struikelt, waar je midden
in een zinsdeel adem moet halen, waar je stem vlak wordt omdat de zin geen nadruk
aanbiedt: herschrijf die zin. Niet schrappen, herschrijven. Het laatste wat er met
een tekst gebeurt mag geen aftrekking zijn.

Zit er een gat in de tekst (een mechanisme dat wordt beweerd maar niet uitgelegd,
een casus die wordt genoemd maar niet getoond), dan vul je dat **niet**. Je
schrijft eromheen en meldt het in het logboek. Nieuwe taal mag altijd. Nieuwe
feiten nooit.

---

## Levering

Eerst de tekst, plakklaar, zonder inleiding en zonder commentaar. Daarna, onder
een streep, het logboek. Maximaal acht regels, één regel per punt, geen bullets
met opsmuk.

```
1. Stem: [teksttype, lezer, register, doellengte]; gekozen door gebruiker of default
2. Draagt: [welke passage, en wat die extra ruimte kreeg]
3. Weg: [wat is geschrapt en waarom]
4. Bewegingen: [functie → specimen, bijv. opening → A2, slot → G2]
5. Standpunt: [de zin waarop de auteur aanspreekbaar is]
6. Feiten: [aantal gecontroleerd; wat is weggelaten]
7. Lengte: [X → Y woorden, −Z%]
8. Open: [gat dat niet gevuld kon worden, of: geen]
```

Regel 8 vervalt als er niets openstaat. Nooit meer dan acht regels, en nooit een
regel die de tekst prijst.

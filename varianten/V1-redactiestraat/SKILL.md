---
name: redactiestraat
description: Zet AI-concepttekst om in publiceerbare Nederlandse rapporttekst voor Social Finance NL door hem door acht gescheiden redactierondes te halen (kader, diagnose, structuur, line edit met herschrijven uit gesloten bron, copy edit, feitencontrole, verse leesronde, slotredactie). Gebruik deze skill voor elk rapporthoofdstuk, elke bestuurlijke samenvatting, casetekst, notitie of andere lezersklare tekst die af moet.
---

# De redactiestraat

Een tekst wordt niet beter door één keer goed te kijken, maar door acht keer verschillend te kijken:
elke ronde met één rol, één mandaat en één soort blindheid. Dit is een productielijn, geen checklist.
Twee dingen maken de straat anders dan opschonen. In ronde 3 gaan zwakke passages met de **brontekst
gesloten** opnieuw op papier, want wie een slechte zin in beeld houdt, erft zijn bouw. In ronde 6
leest iemand de tekst die het origineel **nooit heeft gezien**. Die twee zijn niet optioneel.

Je krijgt: de invoertekst, eventueel teksttype en doellezer, eventueel een feitenlijst, en de
antwoorden van de gebruiker op de stijl-check-in uit ronde 0. Je levert, in één bericht, in deze
volgorde en verder niets: (1) de plakklare tekst zelf, zonder inleiding of toelichting; (2) een
regel met `---`; (3) het logboek van precies acht regels, format in de slotsectie. Geen commentaar
tussendoor, geen opties, geen vraag of het zo goed is.

## De wet van de straat

1. **Eén ronde, één rol, één mandaat.** De copy editor doet geen structuurwerk. De feitencontroleur
   redigeert niet. De verse lezer verbetert niets. Wie een defect ziet dat niet bij zijn ronde
   hoort, noteert het en laat het staan tot de ronde die erover gaat.
2. **Van groot naar klein.** Tekstsoort, inhoud, opbouw, formulering, presentatie (Renkema). Nooit
   terug naar boven zonder de rondes eronder over te doen op het stuk dat je aanraakte.
3. **Nieuwe taal mag, nieuwe feiten niet.** Nieuwe zinnen, openingen, bruggen, koppen, ritme en
   volgorde: gewenst, dat is het werk. Een nieuw getal, jaartal, bedrag, naam, citaat, voorbeeld of
   beeld dat niet in de bron of het gesprek staat: verboden, ook als het waarschijnlijk klopt.
4. **Een ronde is klaar als de aanwezigheidscriteria in de tekst staan**, niet als de verboden zijn
   nageleefd. Foutloos is onvoldoende. Per ronde staat hieronder wat er ná die ronde in de tekst
   moet zitten; kun je het niet met een citaat aanwijzen, dan is de ronde niet af.
5. **Netto korter, lokaal langer.** De hele tekst wordt 15 tot 35 procent korter. Eén passage wordt
   langer dan hij was. Een tekst die overal even veel is ingekort, is geschoven, niet geredigeerd.
6. **De laatste handeling is een schrijfhandeling.** Ronde 7 mag herschrijven; pas daarna komt de
   mechanische poort. Eindigen met wegstrepen garandeert vlakheid.
7. **Breek elke regel liever dan iets barbaars te schrijven** (Orwell 6). Een geforceerd korte zin
   of een gewrongen Nederlands woord is erger dan de overtreding die hij vermijdt.

## Ronde 0. De bureauredacteur: het kader

Mandaat: het kader vaststellen. Deze rol raakt geen zin aan. Zonder kader kun je niet bepalen wat
overbodig is. Lees de invoertekst één keer volledig. Formuleer daarna drie kandidaat-onthoudzinnen: drie zinnen
van maximaal 20 woorden die elk zeggen wat de lezer over een week nog moet weten, alle drie gedekt
door het materiaal in de tekst. Stel dan één keer **AskUserQuestion**, met vier vragen:

**1. Wat is dit en voor wie?**
`Rapporthoofdstuk` beleidsadviseurs en bestuurders bij gemeenten, verzekeraars, Rijk ·
`Bestuurlijke samenvatting` wethouder, directie, bestuur; leest alleen dit ·
`Casetekst` vakgenoten en geïnteresseerde buitenstaanders · `Notitie` interne opdrachtgever.

**2. Welk register, en hoeveel positie neemt de tekst in?**
`Extern wegend` wij als auteur, geen aanspreking, één expliciet oordeel waarop we aanspreekbaar
zijn · `Extern stellend` de tekst kiest partij en zegt wat er moet gebeuren · `Extern beschrijvend`
de feiten spreken, geen uitgesproken oordeel · `Intern direct` wij en je, korter, harde conclusies.

**3. Hoeveel korter?**
`Standaard, ongeveer 25 procent` · `Behoudend, ongeveer 15 procent` (inhoud moet compleet blijven) ·
`Hard, ongeveer 35 procent` (de tekst is duidelijk opgeblazen) · `Vaste omvang` ik noem het aantal.

**4. Welke ene zin moet de lezer onthouden?** De drie kandidaatzinnen die je zelf schreef, plus de
mogelijkheid er zelf een te formuleren. Dit is de belangrijkste vraag van de skill: de onthoudzin is
waar ronde 2 de opbouw op ordent en waar ronde 7 op toetst.

**Defaults als de gebruiker niet antwoordt.** Wacht niet. Leid af uit de tekst zelf, en meld het in
logboekregel 1 als afgeleid.

- *Teksttype:* genummerde kop met subsecties boven 500 woorden is een rapporthoofdstuk; onder de 400
  woorden en openend met een uitkomst is een bestuurlijke samenvatting; één programma met naam,
  looptijd en resultaten is een casetekst; anders een notitie.
- *Doellezer:* de partijen die in de tekst handelend worden genoemd (gemeenten, verzekeraars,
  ministeries) zijn de lezer.
- *Register:* extern wegend, wij als auteur, geen aanspreking. Neem `u` of `je` alleen over als de
  bron dat consequent doet.
- *Lengte:* 25 procent korter.
- *Onthoudzin:* je eigen sterkste kandidaat, die met de meeste harde feiten eronder. Letterlijk in
  logboekregel 2.

**Aanwezigheidscriterium.** Er ligt een opdrachtkaart van zes regels (teksttype, lezer, register,
positie, doellengte in woorden, onthoudzin), en de onthoudzin is een zin die je zou kunnen
voorlezen, geen onderwerp.

## Ronde 1. De diagnosticus: zien, niet ingrijpen

Mandaat: vaststellen wat er mis is en op welk niveau. Deze ronde verandert geen letter. Wie diagnose
en ingreep mengt, doet beide half.
Maak de **reverse outline**: schrijf naast elke alinea één zin over wat die alinea *doet*, met een
handelingswerkwoord. Betoogt, nuanceert, keert, geeft toe, illustreert, rekent voor, waarschuwt.
Lees daarna alleen die lijst, zonder het proza erbij.

- Een functiezin die uitkomt op "behandelt", "gaat in op" of "beschrijft" hoort bij een alinea zonder
  functie. Markeer **vervalt** of **herschrijven**.
- Een alinea die zich niet in één zin laat vangen, doet twee dingen: **splitsen**.
- Twee functiezinnen die op elkaar lijken: **dubbeling**.
- Een sprong die de lezer zelf moet maken: **gat**. Een gat vul je met taal, nooit met een feit.

Bepaal daarna het faalniveau, van boven naar beneden, en stop bij het eerste dat faalt.

- **Niveau 1, de boodschap.** De lijst levert geen redenering op, of niet de onthoudzin. Dan bouwt
  ronde 2 de tekst opnieuw op vanuit een gecorrigeerde outline.
- **Niveau 2, de uitvoering.** De redenering klopt, de passages doen hun werk niet. Dan draait ronde
  3 zwaar, met de gesloten-bronprocedure.
- **Niveau 3, te veel van het goede.** Alles klopt, er staat te veel. Ronde 3 is dan vooral
  snijwerk, met één investering.

**Aanwezigheidscriteria.** Er ligt een lijst functiezinnen met per alinea een label. Minstens één
alinea is gemarkeerd als **dragend**: de passage die het volle gewicht krijgt, waar het concrete
geval staat, en die na ronde 3 langer is dan nu. En minstens één als **vervalt**. Valt er niets weg,
dan heb je gelezen en niet gediagnosticeerd; ga terug.

## Ronde 2. De structuurredacteur: opbouw en gewicht

Mandaat: volgorde, gewicht, weglating, aanvulling. Deze ronde werkt op de outline en verplaatst hele
passages ongewijzigd. Je polijst hier geen zin: polijsten maakt darlings, en de darling die je hebt
bijgeschaafd durf je straks niet meer te schrappen.

1. **Zet het antwoord bovenaan.** De tekst opent met de zaak, niet met een aankondiging van de
   tekst. Schrap elke inleidende alinea die alleen zegt wat komen gaat en elke slotalinea die alleen
   samenvat wat er stond.
2. **Orden op de onthoudzin.** Elke sectie moet die zin dragen. Een sectie die dat niet doet,
   verhuist naar achteren of vervalt.
3. **Verdeel het gewicht ongelijk.** Het zwaarste materiaal, meestal de tegenvaller, de breuk of het
   geld, krijgt de meeste ruimte. Vier secties van gelijke lengte bewijzen dat niemand heeft
   nagedacht over wat zwaarder weegt.
4. **Kies de plek van de tegenwerping.** Eén plek waar de tekst toegeeft wat er tegen zit, vóór de
   lezer het zelf bedenkt.
5. **Vul de gaten met taal:** een zin die het verband legt dat de bron impliceert maar niet
   uitspreekt. Volgt het verband er niet uit, dan blijft het gat en meld je het in het logboek.
6. **Schrapbestand.** Bewaar wat je weghaalt tot de levering. Dat maakt schrappen omkeerbaar en dus
   goedkoop.
7. **Koppen worden stellingen, geen labels.** "Context en aanleiding" wordt een bewering met een
   werkwoord. Zinskapitalisatie, nooit Elk Woord Met Hoofdletter.

**Aanwezigheidscriteria.**

- De eerste zin bevat een feit uit de bron (getal, bedrag, naam, datum) of een claim die iets kost.
  Kun je de eerste zin schrappen zonder verlies, dan is de ronde niet af.
- Elke sectie heeft één functiezin met een handelingswerkwoord, en die functies vormen achter elkaar
  gelezen een betoog, geen inhoudsopgave.
- De secties zijn ongelijk van lengte en je kunt in één zin motiveren waarom.
- De dragende passage staat waar de aandacht anders wegzakt: in het tweede of derde kwart.
- Er is één plek waar de tegenwerping wordt binnengelaten.
- Het slot bevat een gegeven dat nog niet eerder in de tekst stond, of keert iets om. Een slot dat
  samenvat is geen slot.

**Wat deze rol niet doet:** zinnen herschrijven, woorden kiezen, ritme maken.

## Ronde 3. De line editor: de tekst krijgt zijn stem

Mandaat: alinea en zin. De langste ronde en de enige waarin geschreven wordt. Interne volgorde per
passage: eerst helderheid, dan samenhang en tempo, pas dan klank en woordkeus.

### 3.1 Gesloten bron

Een passage gaat hier doorheen zodra hij meer dan drie losse ingrepen nodig heeft, zodra je jezelf
betrapt op het voor de tweede keer redden van dezelfde zwakke formulering, of als zijn functiezin op
"behandelt" uitkwam. Repareren levert dan nooit topkwaliteit: de gerepareerde zin erft de
informatievolgorde en de bijzinarchitectuur van de slechte zin.

1. Noteer de functiezin: wat de passage doet, in één zin, met een handelingswerkwoord.
2. Noteer de feiten kaal, in de volgorde waarin de lezer ze nodig heeft, niet in de bronvolgorde.
3. Kies het patroon uit 3.2 dat bij die functie hoort.
4. **Sluit de bron.** Schrijf de passage uit stap 1 tot 3, zonder de brontekst te lezen. Niet
   gluren, niet "even checken hoe het er stond".
5. Open de bron pas daarna, en uitsluitend om te controleren of een feit is weggevallen of van
   sterkte veranderd. Niet om een formulering terug te halen.

### 3.2 De patronen om naartoe te schrijven

**Opening.** Eerste zin is een feit of een claim die iets kost. Geen keelschrapen, geen scène
zetten, geen definitie. Zin twee bouwt door en begint niet opnieuw.

**Mechanisme, de vierslag.** Naam van het ding met een dubbele punt erachter; dan de geldstroom met
genoemde actoren in de tegenwoordige tijd; dan de voorwaarde als conditionele inversie ("Blijven de
kosten daaronder, dan..."); dan het gedragsgevolg in één korte zin. Jargon mag, mits binnen één zin
afgelost. Verhelder met een tweede zin, niet met een vergelijking uit een ander domein.

**Cijfer, het paar.** Het absolute getal krijgt de langste zin, met zijn bron. De duiding krijgt de
kortste. Maximaal drie getallen per alinea; de rest gaat naar een tabel of vervalt.

**Case.** Omvang, dan prijs, dan de paradox (het werkt wél en wordt tóch niet betaald), dan wie
betaalt tegenover wie profiteert. De oplossing pas in de laatste zin. De lezer moet het probleem
zelf oplossen vóór de tekst het doet.

**Tegenwerping.** Het bezwaar toegeven vóór de lezer het formuleert, dan "maar" of "wel", dan de
claim verkleind maar overeind. De kanttekening verzwakt het betoog niet, ze koopt geloofwaardigheid.

**Slot.** Eindig op de kortste zin van de bladzijde, en laat die zin iets omkeren of een gegeven
leveren dat er nog niet stond. Nooit samenvatten, nooit vooruitblikken zonder gegeven, nooit
oproepen tot samenwerking.

### 3.3 Drempelwaarden

Meet alleen als je twijfelt; nauwkeuriger boekhouden heeft nog nooit een zin mooier gemaakt.

| Wat | Grens |
|---|---|
| Tang: woorden tussen bij elkaar horende delen | maximaal 8 |
| Persoonsvorm staat binnen | de eerste 8 woorden |
| Werkwoordstapel aan het zinseinde | maximaal 2 |
| Gemiddelde zinslengte | 13 tot 18 woorden |
| Per alinea van 4 of meer zinnen | minstens één zin onder de 10 woorden, en die draagt de pointe |
| Spreiding per sectie (langste min kortste zin) | minstens 20 woorden |
| Nominalisaties op -ing, -atie, -heid, -ment | onder de 5 per 100 woorden |
| Drieslagen | maximaal 2 per 800 woorden |
| "Niet alleen X maar ook Y" en varianten | maximaal 1 per 800 woorden |
| Slagen om de arm | nooit twee in één zin; hooguit 2 per 200 woorden |
| Gedachtestreepje als bijzin | 0 |
| Eenzins-alinea | maximaal 1 per hoofdstukdeel, alleen op een echte draai |
| Verschillende verbindingswoorden | minstens 6 per 800 woorden, geen enkel meer dan 3 keer |
| Getallen per alinea | maximaal 3 |

Vaste vervangingen: *in het kader van* → *voor*; *met betrekking tot* → *over*; *middels* → *met*;
*dienen te* → *moeten*; *bewerkstelligen* → *zorgen voor*; *participeren* → *meedoen*; *het feit
dat* → *dat*; *op dit moment* → *nu*. Weg: *cruciaal, essentieel, faciliteren, robuust, naadloos,
toekomstbestendig, integraal, borgen, ontzorgen, meenemen in, handelingsperspectief,
aanknopingspunten, impactvol*, en *landschap* in figuurlijke zin.

Maar: modale partikels blijven staan. *Toch, wel, nu eenmaal, immers, juist, althans, eens.* Ze
dragen geen informatie en wel toon. Een tekst waarin er nul staan, is doodgepoetst. Dat is het
grootste verschil met Engels schrijfadvies.

### 3.4 Wat excellentie is

Vijf paren. Kolom 2 is wat een opschoonronde oplevert: correct, actief, kort en dood. Kolom 3 is
waar deze ronde eindigt. Het verschil tussen 2 en 3 is het verschil tussen een zes en een negen.

> **De voorbeelden zijn patronen, geen feiten.** De namen en getallen erin zijn verzonnen voor deze
> uitleg. Ze mogen nooit in een output terechtkomen.

**1. Opening.**
*Concept:* "In dit hoofdstuk wordt ingegaan op de vraag hoe innovatieve financieringsvormen kunnen
bijdragen aan sterkere preventie."
*Opgeschoond:* "Dit hoofdstuk beschrijft hoe innovatieve financiering preventie kan versterken."
*Uit de straat:* "Vier jaar en 4,2 miljoen euro later daalde de instroom met 11 procent. De
businesscase ging uit van 22."
Wat er gebeurt: de aankondiging verdwijnt en de tweede zin doet het werk dat geen bijvoeglijk
naamwoord kan doen. Het oordeel wordt nergens uitgesproken; de lezer velt het. Kolom 2 is nergens
fout en levert niemand iets op.

**2. Mechanisme.**
*Concept:* "De resultaatafhankelijke component beoogt een prikkel te creëren waarbij financiering
meebeweegt met de gerealiseerde maatschappelijke waarde."
*Opgeschoond:* "De resultaatafhankelijke betaling koppelt de financiering aan het behaalde
resultaat."
*Uit de straat:* "Voor elke voorkomen doorverwijzing betaalt de gemeente 1.850 euro, het bedrag dat
één traject gemiddeld kost. Blijft de doorverwijzing uit, dan verdient de aanbieder. Komt hij er
toch, dan betaalt de gemeente twee keer."
Wat er gebeurt: de conditionele inversie maakt een contractvoorwaarde voelbaar zonder juridisch te
worden, en het parallelle paar laat het risico aan beide kanten zien. De laatste zin is de kortste
en de scherpste.

**3. Tegenvaller.**
*Concept:* "Ook aan de kostenkant deden zich afwijkingen voor die ertoe hebben geleid dat de
terugverdientijd is herberekend."
*Opgeschoond:* "De uitvoeringskosten vielen hoger uit, waardoor de terugverdientijd is herberekend
van 4,5 naar 7,2 jaar."
*Uit de straat:* "De uitvoering kostte 18 procent van het budget in plaats van de begrote 12.
Daarmee schoof de terugverdientijd van 4,5 naar 7,2 jaar. Wie in 2021 tekende voor een investering
die zich binnen een raadsperiode zou terugverdienen, heeft nu een investering die dat niet doet."
Wat er gebeurt: het cijfer krijgt een maatstaf, en de derde zin vertaalt de tabel naar het enige wat
een wethouder eraan heeft. Dat is een claim waarop de schrijver aanspreekbaar is. Kolom 2 verzwijgt
hem beleefd.

**4. Slot.**
*Concept:* "Daarmee biedt het programma, ondanks de geconstateerde aandachtspunten, waardevolle
aanknopingspunten voor de verdere ontwikkeling van de preventieve jeugdzorg en vormt het een solide
basis om op voort te bouwen."
*Opgeschoond:* "Het programma levert bruikbare lessen op voor de doorontwikkeling van preventieve
jeugdzorg."
*Uit de straat:* "In 2026 beslissen negen gemeenten over opschaling. Ze beslissen over een programma
waarvan de belangrijkste opbrengst, 19 procent minder schoolverzuim, in geen enkel contract staat."
Wat er gebeurt: het slot voegt iets toe in plaats van samen te vatten, en legt het verband dat het
hele hoofdstuk impliceerde maar nergens uitsprak. Beide getallen komen uit de bron; het verband is
nieuwe taal, geen nieuw feit.

**5. Concreetheid.**
*Concept:* "Verschillende gemeenten hebben inmiddels ervaring opgedaan met resultaatfinanciering in
het sociaal domein."
*Opgeschoond:* "Meerdere gemeenten werken al met resultaatfinanciering."
*Uit de straat:* "Rotterdam betaalde bij het eerste contract pas uit na 24 maanden werk. Amsterdam
koos voor 12. Dat verschil van een jaar bepaalde welke investeerders aan tafel kwamen."
Wat er gebeurt: het detail dat je alleen kunt schrijven met het dossier open. Let op de voorwaarde:
dit mag alleen als die getallen in de bron staan. Staan ze er niet, dan schrijf je kolom 2 en meld
je het gat. Verzonnen concreetheid is de duurste fout die deze skill kan maken.

### 3.5 De investering

Netto wordt de tekst korter, maar de bespaarde woorden moeten ergens heen. De dragende passage uit
ronde 1 krijgt meer ruimte dan hij in de bron had: het concrete geval, één getal, en het perspectief
van wie het aangaat. Ongelijke lengte is informatie voor de lezer.

**Aanwezigheidscriteria van ronde 3.** Je moet ze met een citaat kunnen aanwijzen.

- Elke sectie bevat één zin die een lezer zou onderstrepen. Een sectie zonder zo'n zin heeft geen
  bestaansrecht: herschrijf hem of laat hem vervallen.
- Elke alinea bevat minstens één concreet gegeven uit de bron: getal, naam, bedrag, datum of
  waarneembare handeling.
- Elke abstractie krijgt binnen dezelfde alinea grond.
- Elk dragend cijfer heeft een tweede zin die het schaalt.
- Er staat minstens één werkwoord in de tekst dat een ander model niet had voorspeld en dat toch
  exact klopt.
- De dragende passage is langer dan in de bron.
- Er staat één claim in waarmee een geïnformeerde lezer het oneens kan zijn.
- Er staat minstens één modaal partikel in.

## Ronde 4. De copy editor: mechaniek

Mandaat: spelling, interpunctie, notatie, consistentie. Deze rol herschrijft niets en verplaatst
niets. Waar meer dan één oplossing verdedigbaar is, kiest hij de meest behoudende en noteert hij de
kwestie; hij lost hem niet eenzijdig op door de zin om te gooien.

- Eén aanspreekvorm (u óf je, of geen) en één auteursperspectief (wij, of het onderzoek, of de
  organisatie bij naam) door de hele tekst.
- Eén notatie voor getallen, procenten, valuta en data. `40 procent` of `40%`, kies en houd vol.
  Decimaalkomma, duizendtal met punt.
- Elk getal dat twee keer in de tekst voorkomt is beide keren identiek.
- Afkortingen: eerste keer voluit, daarna een gewoon woord (het fonds, de gemeente). Een afkorting
  die maar één keer voorkomt, gaat eruit.
- Koppen in zinskapitalisatie. Geen hoofdletters bij dagen, maanden, functies.
- Geen komma vóór *en* of *of* in een opsomming. Geen em-dash. Half gedachtestreepje met spaties
  eromheen, en alleen waar een komma niet volstaat. Leestekens buiten aanhalingstekens, tenzij ze
  bij het citaat horen.
- Geen vetdruk als nadruk in lopende tekst, geen emoji, geen markdown-resten, geen
  krulaanhalingstekens of onzichtbare tekens.
- Elk verbindingswoord klopt met de logische relatie die het markeert. Staat er "daarom" waar geen
  oorzaak voorafging, dan is dat een fout van deze ronde.

**Aanwezigheidscriterium.** Drie willekeurige zinnen uit verschillende delen van de tekst zijn
consistent in aanspreekvorm, perspectief en notatie, en klinken als dezelfde schrijver.

## Ronde 5. De feitencontroleur: tegen de bron

Mandaat: elk feit tegen de bron leggen, niet tegen je geheugen. Deze rol redigeert niet. Hij
markeert en geeft één regel terug aan de line editor, die uitsluitend die zin herstelt.
Haal de tekst uit elkaar. Loop de feitenlijst af, of bij ontbreken daarvan elk cijfer, jaartal,
bedrag, naam, percentage en claim uit de invoertekst, en vink af waar het in de nieuwe tekst staat.

1. **Exact.** Een cijfer uit de bron staat er precies zoals de bron hem geeft. 4,2 miljoen euro
   blijft 4,2 miljoen euro; 11 procent blijft 11 procent. Afronden is verdraaien, en van 340 "ruim
   driehonderd" maken is verdraaien.
2. **Sterkte.** Een verwachting wordt geen bevinding, een bandbreedte geen puntschatting,
   "overweegt" geen "besluit", en een voorbehoud verdwijnt niet.
3. **Rekenen mag, verzinnen niet.** Een verhouding die je zelf uitrekent uit twee brongetallen mag,
   mits ze exact klopt en beide getallen in de tekst staan. Reken nooit met een getal dat er niet staat.
4. **Gaten.** Ontbreekt een gegeven dat de passage nodig heeft, dan gok je het niet. Herschrijf de
   zin zo dat hij zonder dat gegeven klopt en meld het gat in het logboek. Alleen als de passage
   zonder dat gegeven onbruikbaar is, zet je één markering `[ontbreekt: ...]` in de tekst, en dan
   staat hij ook in het logboek.

**Aanwezigheidscriteria.** Elke regel van de feitenlijst is afgevinkt met een vindplaats of staat
als bewuste weglating genoteerd. Elke claim heeft een genoemd subject: een partij met een naam die
iets doet, niet "er wordt" of "experts stellen". En er staat geen getal, naam, jaartal, citaat,
voorbeeld of beeld in dat niet uit de bron komt. Dat laatste is de enige regel in dit bestand
waarvan één overtreding de hele levering afkeurt.

## Ronde 6. De verse lezer: iemand die het origineel nooit zag

Mandaat: waarnemen. Deze rol verbetert niets en oordeelt niet over stijl. Hij rapporteert wat er met
hem gebeurde tijdens het lezen.
Start een subagent met de **Agent-tool** (general-purpose). Geef hem uitsluitend de tekst zoals die
nu is, plus teksttype en doellezer. Niet de invoertekst, niet deze skill, niet de opdrachtkaart,
niet de mededeling dat de tekst is geredigeerd of AI-gegenereerd. Verankering is een procedurele
kwestie, geen kwestie van goede wil.

Briefing, letterlijk mee te geven:

> Je krijgt een Nederlandse [teksttype] voor [doellezer]. Lees hem één keer hardop, op leessnelheid,
> zonder terug te lezen. Beantwoord daarna deze zes vragen. Rapporteer waarnemingen, geen oordelen:
> zeg niets aardigs en niets onaardigs over de tekst, beide zijn ruis. Stel geen verbeteringen voor
> en herschrijf niets.
>
> 1. Waar ging je scannen in plaats van lezen? Citeer de zin waar dat begon.
> 2. Bij welke zinnen struikelde je hardop: adem midden in een zinsdeel, tong vastgelopen, of moest
>    je terug om te weten waar de zin over ging? Citeer ze letterlijk.
> 3. Leg de tekst weg, wacht een minuut. Welke zin zou je een collega sturen met "lees dit even"?
>    Citeer hem uit je hoofd. Lukt dat niet, zeg dan GEEN.
> 4. Wat weet je nu dat je een uur geleden niet wist? Drie punten, uit je hoofd.
> 5. Waar staat de tekst iets waar je het niet mee eens hoeft te zijn? Citeer. Staat dat er nergens,
>    zeg dan GEEN.
> 6. Denk je dat dit door een mens is geschreven? Ja of nee, één zin waarom, met een citaat.

"GEEN" is bij vraag 3 en 5 een geldig antwoord en een belangrijk signaal. Een agent die er iets moet
vinden, vindt iets, en dat verzonnen antwoord wordt vervolgens de tekst in gerepareerd.

**Als subagents niet beschikbaar zijn.** Doe de ronde zelf, met een expliciete contextbreuk: lees
uitsluitend de nieuwe tekst, van boven naar beneden, hardop, zonder de invoertekst of je
aantekeningen erbij, en schrijf de zes antwoorden op vóórdat je iets aanraakt. Opschrijven is de
breuk; in je hoofd beantwoorden is dat niet.

**Aanwezigheidscriteria.** Er ligt een rapport met zes antwoorden, met citaten. Bij vraag 3 staat een
zin of het woord GEEN. Bij vraag 6 staat een oordeel met reden.

## Ronde 7. De slotredacteur: de laatste schrijfpas

Mandaat: het rapport van de verse lezer afhandelen, met de bevoegdheid om te herschrijven. Dit is
een schrijfronde, geen schrapronde.
- **Scanpunt (vraag 1).** Daar zakt de aandacht weg. Kort in, of leg er een beloning: een concreet
  geval, een cijfer met een maatstaf, een scherpe formulering uit de bron.
- **Struikelzin (vraag 2).** Herschrijf hem hardop. Loopt hij na twee pogingen nog niet, dan mist de
  gedachte eronder iets. Zoek dat; poets de zin niet glad.
- **Geen doorstuurzin (vraag 3).** Dan mist de tekst zijn pointe. Kies de sectie met het zwaarste
  materiaal en schrijf daar één zin die zelfstandig overeind blijft. Dit is de belangrijkste
  reparatie van de hele straat.
- **De drie punten (vraag 4) wijken af van de onthoudzin.** Dan is de boodschap niet overgekomen;
  verplaats het materiaal dat haar draagt naar voren.
- **Geen aanvechtbare zin (vraag 5).** Zet de scherpste claim terug op de sterkte die het bewijs
  toelaat, niet zwakker.
- **"Nee" op vraag 6.** Lees het citaat dat de lezer geeft en herschrijf die passage met de
  gesloten-bronprocedure uit 3.1.

Lees daarna de tekst nog één keer hardop, van eerste tot laatste zin. Wie zwijgend leest, leest wat
hij bedoelde; wie hardop leest, leest wat er staat.

### De eindpoort

Acht controles. Elke "nee" is een adres, geen algemeen oordeel. Herstel minimaal en lokaal; ga niet
opnieuw de straat door.

1. Bevat de eerste zin een feit of een claim die iets kost, en is hij onschrapbaar?
2. Heeft elke sectie een zin die je zou onderstrepen?
3. Eindigt de tekst op een korte zin die iets omkeert of toevoegt, en niet samenvat?
4. Zijn de secties ongelijk van lengte, in verhouding tot hun gewicht?
5. Klopt de tekst met de onthoudzin uit ronde 0?
6. Is de tekst 15 tot 35 procent korter dan de invoer, en is minstens een kwart van de zinnen
   wezenlijk anders (niet dezelfde zin met andere woorden)?
7. Feitenpoort: staat er geen getal, naam, jaartal, citaat, voorbeeld of beeld in dat niet uit de
   bron komt?
8. AI-poort: geen aankondigings- of samenvattingsalinea, geen uitsmijterparagraaf ("uitdagingen en
   vooruitblik"), hoogstens twee drieslagen, hoogstens één "niet alleen X maar ook Y", geen em-dash,
   geen title case, geen vetdruk als nadruk, geen vage attributie ("uit de praktijk blijkt"), geen
   stapeling van slagen om de arm, geen verzonnen vakterm die de lezer niet kan opzoeken.

## Levering

De tekst, dan `---`, dan het logboek: acht regels, elk één regel, geen inleiding.

```
1. Kader: [teksttype], [lezer], [register], [positie], doel [n] woorden (gekozen / afgeleid uit de tekst)
2. Onthoudzin: [de zin]
3. Diagnose: niveau [1/2/3]; vervallen: [wat]
4. Structuur: [de ene ingreep die het meest deed]
5. Uit gesloten bron herschreven: [welke passages]
6. Investering: [welke passage kreeg meer ruimte, en waarom]
7. Feiten: alle [n] gecontroleerd, akkoord / gat: [wat ontbreekt]
8. Verse lezer: [uitkomst], daarop aangepast: [wat]; [x] → [y] woorden ([z] procent korter)
```

Regel 7 en 8 zijn nooit leeg. Verder niets: geen aanbod om iets anders te proberen, geen samenvatting
van wat je hebt gedaan.

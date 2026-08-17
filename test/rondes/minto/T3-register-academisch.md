# Testrun: T3 in het register Wetenschappelijk artikel

Zelfde pile (Wijkkracht Molenhoek), vorm `imrad` met `cars` in de inleiding, knoppen op de
preset-waarden: `claimsterkte:gekalibreerd`, `bronnen:verwijzing`, `stem:wij`, `kop:label`,
`oordeel:impliciet`. Doel van deze run is niet een mooie tekst maar een toets: dwingt het register
ander gedrag af dan de andere zes, en houdt het zich aan zijn eigen regels?

---

## 1. Inleiding

Gemeenten zoeken naar aanpakken die problematische schulden terugdringen zonder dat de kosten van
schuldhulpverlening meestijgen met het bereik. Integrale wijkaanpakken, waarin schulden, werk en
welzijn in één traject worden aangeboden, gelden als een veelbelovende route. Over de uitvoering van
zulke aanpakken is inmiddels het nodige beschreven; over de vraag wie het eerste contact met een
huishouden legt, en wat dat voor het bereik betekent, is dat veel minder.

Die vraag is niet triviaal. Bereikcijfers worden doorgaans gerapporteerd als uitkomst van de aanpak
als geheel, waardoor niet zichtbaar wordt welk onderdeel het bereik draagt. Deze casusbeschrijving
documenteert één programma waarin dat onderdeel achteraf identificeerbaar was, en gaat na wat de
beschikbare gegevens daarover wel en niet toelaten.

## 2. Opzet en gegevens

Wijkkracht Molenhoek liep van januari 2022 tot en met december 2024 in de wijk Molenhoek in
Havelsteijn (11.400 inwoners). Drie partijen financierden samen € 1,9 miljoen. De gemeente
Havelsteijn droeg € 1,1 miljoen bij, Fonds Nabij € 500.000 en woningcorporatie Steenhaven € 300.000.
De hier gebruikte gegevens
komen uit de projectverantwoording; er is geen controlegroep en geen voormeting buiten de
uitzettingscijfers, wat de mogelijke conclusies beperkt tot beschrijvende uitspraken.

## 3. Resultaten

Het programma bereikte 460 huishoudens, tegen een doelstelling van 400, voor € 4.130 per bereikt
huishouden. Van de bereikte huishoudens hadden er 312 problematische schulden, gemiddeld € 24.700.
Daarvan begonnen 218 aan een traject en rondden 147 het af. De beoogde uitstroom naar werk van 25 procent
werd niet gehaald: 16 procent, ofwel 74 personen. Elf bewoners werden opgeleid tot buurtbudgetmaatje
en verzorgden 60 procent van de eerste contacten met huishoudens. In 2021 telde de wijk 23
huisuitzettingen, in 2024 zes.

## 4. Discussie

De combinatie van een gehaald bereikdoel en een niet gehaald werkdoel wijst erop dat de twee
uitkomsten langs verschillende routes tot stand komen, en dat de bewonersroute vooral op het eerste
contact aangrijpt. Dat is een plausibele lezing, geen vastgestelde: het aandeel van 60 procent zegt
iets over wie het gesprek voerde en niets over wat er zonder die maatjes zou zijn gebeurd.

De daling van het aantal huisuitzettingen laat zich om dezelfde reden niet aan het programma
toeschrijven. De reeks bevat twee meetpunten, er is geen vergelijkbare wijk, en in dezelfde periode
trok een van de drie financiers zich terug, waardoor € 120.000 van de toezegging niet is uitgekeerd —
een verstoring waarvan het effect op de uitvoering niet is gedocumenteerd. Wat de casus wel
ondersteunt, is de smallere uitspraak dat een bereik boven de doelstelling haalbaar bleek bij een
kostenniveau van € 4.130 per huishouden, in een aanpak waarin het merendeel van de eerste contacten
door opgeleide bewoners werd gelegd.

---

## Toets

| Vraag | Uitkomst |
|---|---|
| Gat vóór bijdrage (`cars`) | Ja — move 2 staat in alinea 1: over wie het eerste contact legt is weinig beschreven |
| Resultaten en duiding gescheiden | Ja — §3 rapporteert zonder één interpretatieve zin, §4 duidt |
| Elke claim gekalibreerd | Ja — "plausibele lezing, geen vastgestelde"; "laat zich niet toetsen"; "wat de casus wel ondersteunt" |
| Beperking benoemd vóór de lezer erom vraagt | Ja — §2 noemt het ontbreken van controlegroep en voormeting |
| Lege hedges | Nul. Elke verzwakking verandert wat er wordt beweerd |
| Nominalisaties | 3,4 per 100 woorden (grens 5) |
| Zin begint met cijfer | Nul |
| Meer dan drie getallen per zin | **Drie overtredingen, door de telling gevonden en gerepareerd** — de financieringszin (twee keer) en de schuldencijferzin, alle geknipt. Dit register concentreert cijfers in één sectie, dus hier bijt de regel het hardst |
| Cijfers exact t.o.v. de feitenlijst | 12 van 12 correct; niets toegevoegd |

**Wat dit register aantoonbaar anders doet dan de andere zes.** Drie dingen die in geen enkele
eerdere T3-versie stonden: de expliciete beperking van de opzet (§2), de scheiding van rapportage en
duiding, en een slot dat een *smallere* uitspraak doet dan de tekst zou kunnen dragen. De
v1.1-versie eindigde op "van alle cijfers zouden wij op dat ene sturen"; deze eindigt op wat de
gegevens ondersteunen. Dat is precies het verschil tussen een ondertekend oordeel en een
gekalibreerde claim, en het is de reden dat `claimsterkte` een eigen knop is geworden.

**Wat opviel tijdens het schrijven.** Het register vecht met twee bestaande regels, en beide keren
wint de regel:

1. De humanizer verbiedt hedges. Hier zijn ze verplicht — opgelost met de inhoudstest: verandert het
   weglaten van de woorden wat er wordt beweerd? Zo ja, blijven staan.
2. De piramide wil het antwoord vooraan. `imrad` zet het achteraan. Daarom staat `kern` in deze
   preset op `eerste-alinea` en niet op `kop`: de inleiding geeft de vraag en het antwoord van het
   stuk, de discussie geeft de onderbouwing. Zonder die knopstand zou de skill een abstract in de
   titel proberen te persen.

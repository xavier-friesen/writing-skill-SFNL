# De structurele fout, en wat v6.0 eraan doet

Dit stuk staat apart van de ronde-analyses, omdat het niet over een ronde gaat
maar over een fout in de manier waarop ik zeven rondes lang naar de skill heb
gekeken.

## Wat er misging in mijn diagnose

Na elke verloren ronde heb ik het defect gevonden, verklaard en gedicht. Vier
keer:

| Ronde | Het defect | De patch |
|---|---|---|
| 6 (T3) | een verzonnen fondsmanager met een citaat in directe rede | "geen opgevoerde spreker" + een detector |
| 6 (T1) | een factor 1,6 die "bijna verdubbeld" heet | elke schaalvertaling herrekenen uit de brongetallen |
| 7 | een oorzaak gelegd met een dubbele punt, zonder signaalwoord | aanstrepen wat de bron naast elkaar zet |
| 7b | "de grootste daling", weerlegd door een cijfer in dezelfde tekst | de rangordetoets |

Elke patch was juist en elke patch werkte — op zijn eigen defect. De skill werd
er alleen niet beter van, want de volgende ronde vond een nieuwe uitgang. Vier
patches, nul winsten.

De denkfout is dat ik vier symptomen voor vier oorzaken hield. Ze hebben één
oorzaak, en die had ik na de tweede al kunnen zien.

## De oorzaak

De skill vroeg de schrijver zich **eerst** vast te leggen op een bewering, en die
bewering werd geselecteerd op *retorische* kwaliteit: een geïnformeerde lezer
moet het oneens kunnen zijn, zij moet hem iets kosten, zij moet scherp zijn. Pas
**daarna** werd getoetst of het materiaal haar droeg — door dezelfde schrijver,
die er op dat moment belang bij had dat zij overleefde.

Daarmee stond elke controle stroomafwaarts van het motief. Dat is geen
procesfout die je met een strengere poort repareert; het is een belangenconflict.
En de druk komt eruit langs de weg van de minste weerstand, elke keer weer:

- de bewering heeft een bezwaar nodig dat echt voelt → er komt een persoon die
  het zegt;
- zij heeft een getal nodig dat groot voelt → de verhouding buigt;
- zij heeft twee feiten nodig die verbonden zijn → er komt een oorzaak;
- zij moet de belangrijkste zijn → er komt een rangorde.

Vier uitgangen, en er zijn er meer. Een vergelijking die de bron niet maakt, een
tijdsordening die een ontwikkeling suggereert, een "inmiddels" dat een stand van
zaken claimt: alle drie zouden door de vier patches heen zijn gelopen.

Waarom v3.2 dit niet heeft: die versie liet de schrijver zich nooit vastleggen op
iets wat het materiaal niet al bevatte. De veiligheid van v3.2 is **structureel**,
die van v4.x en v5.x was **procedureel** — en dat is het hele verschil tussen 7,5
en 5,1.

## De ingreep

Geen controle erbij. De **vorm** van de bewering wordt de garantie:

> De kernbewering is een spanning tussen twee gegevens die beide in de bron
> staan, en zij is opschrijfbaar als **"X, terwijl Y"**.

Waarom dit werkt waar een poort niet werkt: de bewering is gedekt op het moment
dat zij bestaat. Er is geen tussenruimte tussen kiezen en toetsen waarin een
motief kan ontstaan, want de dekking is geen stap in het proces maar een
eigenschap van de vorm.

En de vier defecten zijn niet langer verboden, ze zijn **onmogelijk**:

- "de grootste daling" is een rangorde en heeft de vorm niet;
- "een fondsmanager vraagt dan" bestaat niet uit twee bronfeiten;
- "beide feiten komen uit dezelfde constructie" is een oorzaak, geen spanning;
- "bijna verdubbeld" is overbodig, want de spanning ís al "de terugverdientijd
  werd 7,2 jaar, terwijl de businesscase 4,5 jaar aanhield".

Dat laatste is het aardigste geval: de patch bestreed de neiging, de vorm neemt
het motief weg. Een verhouding buigen heeft geen zin meer als de twee getallen
zelf de bewering zijn.

## Wat er met de scherpte gebeurt

Die verdwijnt niet, hij verhuist. **Van de propositie naar de selectie.** De
vrijheid van de schrijver zit niet meer in welke bewering hij bedenkt, maar in
welke twee gegevens hij naast elkaar zet en hoe hij de verhouding benoemt.

Dat is ook waar het oog van een redacteur hoort te zitten. Twee feiten die
niemand naast elkaar had gelegd zijn scherper dan de mooiste zin die je zelf
verzint — en het is precies wat de jury's beloonden in de teksten die wonnen: de
uitstap van een medefinancier naast het gat dat daardoor viel, de gemeten winst
naast de afspraak waarin zij niet voorkwam.

Om die reden is stap 1 in v6.0 geen creatieve stap meer maar een zoekopdracht,
met vijf vindplaatsen op opbrengst gesorteerd. De opbrengstrijkste is de derde:
het gegeven dat de bron kort en neutraal houdt, in één passieve bijzin
weggezet. Dat staat er niet voor niets zo.

En "wat de lezer moet opgeven" is van functie veranderd. In v5.x was het een
halve dekkingstoets; nu is het uitsluitend het criterium waarop je **kiest**
tussen drie kandidaten die alle drie al gedekt zijn. Kiezen en toetsen zijn
gescheiden.

## Wat dit kost

De skill is korter geworden, niet langer. Drie valkuilenparagrafen, een
rangordetoets en een deel van de slotpas zijn vervangen door twee regels: de
vormeis, en "buiten de twee helften, je aangestreepte gegevens en je eigen weging
beweer je niets".

Wat het wél kost is een deel van de vrijheid. Een schrijver die iets wil zeggen
wat niet in de vorm past, mag het niet zeggen. Dat is de bedoeling, en het is de
vraag die de verificatie moet beantwoorden: wordt de tekst daar zwakker van, of
alleen eerlijker? Als de vormeis de scherpte wegneemt in plaats van haar te
verplaatsen, is v6.0 een veilige v3.2 met minder regels — nuttig, maar niet wat
we zochten.

## De les die algemener is dan deze skill

Een regel die een neiging bestrijdt, verliest van de neiging. Een vorm die de
neiging zinloos maakt, niet. Wie merkt dat hij dezelfde soort fout voor de derde
keer dicht, moet ophouden met dichten en de vorm zoeken die het motief wegneemt.

# Analyse ronde 7 — v5.0 tegen de v3.2-kampioen op T1

Opzet: één testtekst (T1 rapporthoofdstuk, de langste en de tekst waarop v4.0
diskwalificeerde), v5.0 tegen de best gemeten v3.2-output, blind. Twee jury's,
en het verschil tussen die twee is het belangrijkste van deze ronde.

## Uitslag

| Ronde | Set | v3.2-kampioen | v5.0 | Winnaar |
|---|---|---|---|---|
| r7 | vervuild | 6,5 | 7,3 | v5.0 |
| r7b | schoon | **7,5** | **5,1** | **v3.2** |

De eerste set was in twee opzichten vervuild, beide in het voordeel van v5.0.
De blinde bestanden werden met een awk-regel ter plekke gemaakt, waardoor de
steigerkoppen van de oudere output (`# S3-T1`, `## Tekst`) bleven staan; de
jury noemde die expliciet als reden om die versie eerder voor modelwerk te
houden. Datzelfde was in ronde 6 bij T2 gebeurd. En de juryspreiding op één en
dezelfde tekst blijkt ongeveer een punt te zijn: de v3.2-output kreeg 7,6 (r6),
6,5 (r7) en 7,5 (r7b). Alleen een vergelijking *binnen* één jury zegt iets.

Vanaf nu gaat elke blinde set door `test/strip.sh`.

**Stand van de generatieve architectuur in schone vergelijkingen: 0 uit 4.**
Drie verliezen in ronde 6 (waarvan twee met een feitendiskwalificatie), één in
ronde 7b.

## De bevinding die het zwaarst weegt

**De kernbewering zelf was ondeugdelijk, en de feitenpoort kon dat niet zien.**

v5.0 zette zijn hoofdstuk op een overtreffende trap: de daling van 19 procent
in het verzuim was "de grootste daling". De bron zegt dat nergens, en de tekst
weerspreekt zich zelf — de wachttijd ging in diezelfde tekst van 14 naar 9
weken, ruim 35 procent. Elk getal in de tekst was correct. Alleen de rangorde
die eromheen werd gelegd, was verzonnen.

Dat maakt deze fout gevaarlijker dan de fouten van ronde 6. Een verzonnen getal
of een opgevoerde spreker is aanwijsbaar: er staat iets in de tekst dat niet in
de bron staat. Een verzonnen *rangorde* bestaat uit correcte getallen in een
onjuiste verhouding, en glipt daarmee door elke controle die "wijs de bron aan"
als vorm heeft. En omdat de premisse in de kop, de tussenkoppen en het slot
terugkomt, besmet één ondeugdelijke rangorde de hele tekst in plaats van één
zin.

Daarmee is de wet van ronde 6 preciezer te formuleren.

**Wet 8. Een premisse-eerst-ontwerp heeft een rangordetoets nodig, niet alleen
een dekkingstoets.** "Kun je dit aanwijzen in de bron?" laat elke vergelijkende
en overtreffende trap door, want die beweert iets over de alternatieven en niet
over zichzelf. De toets die wél werkt is een rekensom: loop alle andere
getallen in dezelfde eenheid langs, en kun je niet uitsluiten dat er één jouw
kandidaat verslaat, dan gaat de trap eruit.

## Een fout in mijn eigen werkwijze

De schrijver van v5.0 rapporteerde dat de spiegelpaar-detectie normaal
feitendicht Nederlands trof, en ik heb de meting op grond daarvan strenger
gemaakt. Deze jury vond vervolgens drie spiegelparen die het script groen liet.

**Een meting versoepel je niet op gezag van degene die eraan gehouden wordt.**
De klacht was oprecht en deels juist — er waren valse positieven — maar de
juiste reactie is de valse positieven wegnemen zonder het bereik te verkleinen,
en niet de drempel opschuiven omdat de schrijver er hinder van heeft. De
detectie staat nu tussen beide versies in: dezelfde ingang plus een
ontkenningsasymmetrie, met alleen het geval van twee lange feitenzinnen
uitgesloten. Zij vangt nog steeds niet alles wat een jury ziet, en dat blijft zo
— het spiegelpaar is een patroon op oordeelsniveau. Daarvoor is de lezer in
stap 4 het instrument, niet de regex.

Ter geruststelling over de rest van het script: het zet de v3.2-kampioen op rood
voor drie schaalvertalingen, en dat is precies de "verhoudingsglosse achter
vrijwel elk cijfer" die beide jury's hem aanrekenden. De metingen zijn geldig;
één detector is te grof.

## Wat v5.3 verandert

1. **De rangordetoets** in stap 1, na de dekkingstoets en even verplicht: elke
   vergelijkende of overtreffende trap in de kernbewering wordt narekend tegen
   elk ander aangestreept getal in dezelfde eenheid.
2. **Een zevende meting in het script,** `rangorde`, die de trappen aanwijst.
   Narekenen kan het script niet; aanwijzen wel, en dat is waar de fout begint.
3. **De spiegelpaar-detectie** teruggedraaid naar een middenstand, met de
   verantwoording erbij.
4. `test/strip.sh` als enige route naar een blinde set.

## Waar dit traject nu staat

Voor werk dat de deur uit gaat is **v3.2 nog steeds de te installeren versie**.
Dat is niet wat ik hoopte na drie iteraties, en het staat hier omdat het waar
is: vier schone jury's, geen enkele winst voor het nieuwe ontwerp.

Wat het nieuwe ontwerp wél heeft aangetoond: het schrijft scherper, het levert
doorstuurbare zinnen ("De grootste winst had geen betaler" was de enige zin die
een jurylid uit het hoofd kon reproduceren), en het doet dat met een kwart van
de instructie en een fractie van de tokens. Wat het nog niet heeft aangetoond is
dat het te vertrouwen is. De vier verliezen komen alle vier uit dezelfde bron:
de tekst wordt sterker gemaakt dan het materiaal toestaat, en steeds in de zin
die de lezer het beste vindt.

Dat is een probleem van één soort, en het is nu op vier plekken afgedekt
(spreker, bewijsbewering, verbogen verhouding, rangorde). Of dat genoeg is, weet
niemand tot een v5-build een schone ronde wint. Dat is de eerlijke stand.

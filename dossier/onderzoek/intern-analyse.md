# Analyse van de bestaande SFNL-schrijfskills

Gelezen: `sfnl-humanizer/SKILL.md` (754 regels), `sfnl-tekst-scherpen/SKILL.md`
(212 regels) plus alle negen referenties, en de vier stijlskills
(`extern`, `introduction`, `consultant`, `intern`).

## Sterktes

**De patroonvangst is compleet en actueel.** De humanizer dekt 38 patronen, van
de klassieke Wikipedia-lijst tot patronen 28–38 die specifiek zijn voor de
huidige Claude-generatie: verzonnen jargon dat als vakterm wordt gepresenteerd,
definiëren-door-ontkenning, ter plekke bedachte metaforen, dichtheid verward met
beknoptheid, argumentatief framen, opgeblazen voorbehouden, stijldrift na dertig
beurten. Dat is zeldzaam goed werk. Een tekst die door deze lijst is gehaald,
bevat geen enkele van de tics waaraan een lezer AI herkent op woordniveau.

**De twee motoren zijn een echt mechanisme, geen regel.** `tekst-scherpen`
stuurt twee agents op de tekst af die elkaar niet kennen en het plan van de
schrijver niet kennen. De ondervrager toetst of de tekst klopt met zijn eigen
uitspraken (elenchus, zes toegestane botsingstypen, vier expliciet verboden
pseudo-botsingen). De lezer rapporteert waarnemingen, geen oordelen: waar hij
ging scannen, wat hij nog wist, welke zin hij zou doorsturen. De rolscheiding is
consequent doorgevoerd tot in de briefings.

**"Geen botsing gevonden" is een geldig antwoord.** In `ondervrager.md` staat
expliciet waarom: een agent die er drie moet vinden, vindt er drie, en die
verzonnen tegenspraken worden vervolgens de tekst in gerepareerd. Datzelfde
geldt voor GEEN doorstuurzin bij de lezer. Deze uitwegen zijn het verschil
tussen een meetinstrument en een ritueel.

**De onderstreeptest is het scherpste instrument in de hele set.** "Een sectie
zonder onderstreepbare zin is een sectie zonder bestaansrecht." Dat is de enige
plek in beide skills waar een positieve kwaliteitseis staat in plaats van een
verbod.

**De prozadiagnose is toetsbaar in plaats van smaakvol.** `leesdiagnose.md` zet
Gopen/Swan, Williams, Lanham, Pinker en Sword om in regels die je met ja of nee
op een concrete zin toetst, met drempelwaarden (koppelwerkwoorden onder 3%,
nominalisaties onder 4%, voorzetsels onder 14%). Inclusief de waarschuwing dat
leesbaarheidsformules niets meten wat ertoe doet.

**`specimens.md` is het enige generatieve materiaal in de hele set.** Tien
functies (opening, abstractie aarden, mechanisme uitleggen, tegenwerping toetsen,
slot), elk als paar: de beleidsversie die niemand leest naast de gepubliceerde
versie die werkt, met een analyse van wat er gebeurt. Plus het patroon achter de
tien: concreet vóór abstract, één getal per alinea, de kortste zin draagt de
kern, geen bijvoeglijke naamwoorden waar het materiaal al oordeelt, het slot
claimt minder dan het zou kunnen. Dit is bruikbaar, ambachtelijk, Nederlands en
uit gepubliceerd werk.

**Volgorde, voorrang en faalgedrag zijn doordacht.** Eerst snijden dan poetsen
("wie begint bij de zinnen, poetst zinnen die straks toch sneuvelen"), expliciete
conflictvoorrang (betekenis > auteurskeuzes > leesdiagnose > humanizer),
stopcriteria, en een vastloopsectie die het verschil benoemt tussen twaalf
procent korter zonder verlies en dertig procent korter zonder scherpte.

**De stijlskills zijn compact en consistent.** Vier registers met dezelfde
onderhandelbare kern en heldere verschilassen (aanspreekvorm, jargon, zekerheid,
zinslengte, slot), plus een mappingtabel in `register.md`.

## Het gat

Beide skills zijn **aftrekkende kwaliteitsbewaking op een behoudmandaat**. Ze
nemen de zinnen van het concept als substraat en verbeteren die lokaal. Nergens
in de zeven fasen ontstaat een zin die niet in enige vorm al in het concept
stond. Het plafond van zo'n systeem is: het concept, min de fouten. Dat is
correct, kort en dood. Prachtig proza is geen foutloos concept; het is een
anders bedacht concept.

Concreter, twaalf mechanismen die het gat veroorzaken:

**1. De voorbeelden in de humanizer trainen precies de vlakheid waarover wordt
geklaagd.** `specimens.md` zegt het zelf: "Een voorbeeld stuurt beter dan een
regel." Kijk dan naar de veertig Na-voorbeelden in de humanizer. "Het fonds is
in 2023 opgericht om zorgaanbieders te prefinancieren die afhankelijk zijn van
uitgestelde gemeentebetalingen." "Het fonds financiert sociale innovatieprojecten
en brengt gemeenten en uitvoerders bij elkaar." "De aanpak combineert gedeelde
risicodeling met langetermijncontracten." Stuk voor stuk correct, feitelijk,
actief, en geen enkele die iemand zou onderstrepen. De meest gebruikte skill
demonstreert consequent *foutloosheid*, niet *kwaliteit*. Dat is de scherpste
enkelvoudige bevinding van deze analyse.

**2. Verbieden begrenst de uitvoerruimte, het kiest er geen punt in.** De
verhouding is ongeveer 38 verboden en 40 verwijder-voorbeelden tegenover tien
specimens. Een model dat vooral hoort wat niet mag, convergeert op de veiligste
overlevende optie: korte mededelende zinnen, gewone werkwoorden, geen beeld,
geen ritme, geen risico. Dat is exact het register waarover de eigenaar klaagt.
De verboden zijn niet fout; ze zijn onvoldoende en ze zijn in de meerderheid.

**3. Verankering aan de bronformulering.** De hele bewerking gebeurt zin voor
zin over de bestaande tekst, met de bestaande tekst in beeld. Het model leest
een slechte zin en repareert hem; de gerepareerde zin erft de
informatievolgorde, de bijzinarchitectuur en het beeld van de slechte zin. Er is
geen enkele stap waarin de schrijver wordt gedwongen weg te kijken van het
concept en de passage vanuit de feiten opnieuw op te schrijven.

**4. Er is geen kwaliteitsanker, alleen een foutenteller.** Nergens staat wat de
afgemaakte tekst *moet zijn*. De eindpoort telt negen criteria, waarvan er acht
afwezigheidscriteria zijn (niet te lang, geen monotonie, geen gedachtestreepje,
geen title case, geen onverwerkte botsing) en één aanwezigheidscriterium (de
onderstreepbare zin). Zonder anker betekent "goed" automatisch "minder
schendingen", en stopt het model bij de eerste foutloze versie.

**5. Beknoptheid is de enige gekwantificeerde doelstelling, en verdringt de
rest.** "Doel: dertig procent korter. Haal je dat niet, dan heb je niet gesneden
maar geschoven." Plus 25% in de eindpoort en 15–30% in `modeltics.md`. Wat
meetbaar is, wint van wat dat niet is. En het is aantoonbaar het verkeerde
doel: de specimens zelf zijn niet maximaal gecomprimeerd. De WRR-passage over
geldschepping is bewust redundant (eerst de misvatting, dan de correctie, dan
Anne, dan €5.000). NRC besteedt woorden aan elk boorgat en elke klinknagel. Goed
proza *investeert* woorden op de plek die het draagt. Het systeem kent alleen
een snijmechanisme en geen investeringsmechanisme. "Snijden is niet hetzelfde
als afvlakken" staat er wel, maar er staat geen enkele instructie die zegt waar
de bespaarde woorden heen moeten.

**6. Beide motoren diagnosticeren, geen van beide componeert.** De ondervrager
toetst waarheid, de lezer toetst aandacht. Allebei vinden ze defecten. Geen van
beide heeft een opvatting over de vraag of het proza *goed* is. De
lezerssimulatie verbiedt dat oordeel zelfs expliciet: "Zeg niets aardigs over de
tekst en niets onaardigs. Beide zijn ruis." Methodisch zuiver voor diagnose, met
als gevolg dat niemand in het hele systeem ooit kwaliteit beoordeelt.

**7. Geen iteratie met vers oog.** Fase 5 herschrijft één keer, in dezelfde
context die fase 1 tot 4 heeft gedaan en de hele diagnose in het hoofd heeft.
Een tweede ronde wordt actief ontraden: "alleen als fase 5 de tekst zo
ingrijpend heeft veranderd ... en verder zelden." De herschreven tekst wordt dus
nooit gelezen door iemand die het origineel niet kent. Het betrouwbaarste
mechanisme uit de menselijke redactie, het stuk een nacht laten liggen of aan
een collega geven die het concept niet zag, ontbreekt structureel.

**8. De laatste handeling op elke tekst is een aftrekking.** Fase 6: "In deze
fase mag je schrappen, maar niets toevoegen en niets verplaatsen." De pas waarin
een menselijke redacteur eindelijk het ritme hóórt en de opening omzet, mag
alleen weghalen. Combineer dat met de humanizer die in dezelfde fase draait, en
vlakheid is een structurele garantie, geen ongelukje.

**9. Het stijlkeuzemoment gaat over inhoud, niet over stem.** Fase 2 bestaat,
maar `vragen-voorleggen.md` sluit precies het onderwerp van de klacht uit: "Wat
je niet vraagt: toon, register en woordkeus. Dat zie je in de tekst." Het
register wordt eenzijdig gekozen via een tabel in fase 1. De gebruiker wordt dus
bevraagd over het frame en nooit over de stem, de durf, de positie, of over de
vraag welke passage de lezer moet onthouden.

**10. Niemand is eigenaar van de architectuur van de tekst.** De elenchus toetst
claims, de leesdiagnose toetst zinnen en alinea's, `modeltics.md` schrapt
secties. Niets ontwerpt de boog van een hoofdstuk: waar de spanning zit, waar
het concrete geval landt, waar de lezer even mag ademen, welke alinea de
geciteerde wordt. De reverse outline wordt uitsluitend gebruikt om dubbelingen
te vinden, nooit om een volgorde te componeren.

**11. Geen ijking aan gepubliceerd werk aan de uitvoerkant.** `specimens.md`
wordt gebruikt vóór het schrijven van een passage en daarna nooit meer. Er is
geen stap waarin je je eigen alinea naast het specimen met dezelfde functie legt
en vaststelt welke van de twee een lezer liever leest. Die vergelijking is
goedkoop, hard, en zou vlakheid onmiddellijk zichtbaar maken.

**12. De nalevingslast verdringt het vakmanschap.** Het model doet vijf
tellingen met percentages, een zinslengtereeks, een reverse outline, negen
eindpoortcriteria, een vierregelige meting en een achtregelig logboek. Dat
werkgeheugen gaat naar de audit, niet naar de zin. Hier zit ook de directe
verklaring voor de klacht dat de skills teksten "langer" maken: de gebruiker
krijgt een muur aan procesoutput (rewrite + audit note bij de humanizer; tekst +
meting + logboek bij tekst-scherpen) rond een tekst die inhoudelijk mild is
veranderd. Daar komt bij dat de humanizer bij vage passages naar concretisering
duwt zonder over de feiten te beschikken, wat uitnodigt tot vullen.

**En in de praktijk krijgt bijna elke tekst alleen de aftrekkende pas.** De
humanizer triggert automatisch op vrijwel elke klantgerichte tekst;
`tekst-scherpen` triggert uitsluitend op zijn exacte naam. De "polish" die
mensen feitelijk krijgen is dus de patroonstripper. Dat alleen al verklaart de
klacht. Daarbovenop bestaan er drie overlappende definities van de SFNL-stem
(de voice-sectie in de humanizer, `register.md`, en de vier stijlskills), zonder
dat er één de baas is.

**Ten slotte ontbreekt de bevoegdheid om af te maken.** De gevraagde output is
"complete, perfecte rapporttekst". `tekst-scherpen` mag geen structuur
toevoegen, geen inhoud toevoegen, geen beeld verzinnen; de humanizer behoudt de
betekenis. Heeft het concept een gat, een ontbrekende brug, een mechanisme dat
wordt beweerd maar niet uitgelegd, een case die wordt genoemd maar niet getoond,
dan vult niets dat gat. Het verbod op verzinnen van *feiten* is terecht, maar het
is in de huidige formulering samengevallen met een verbod op het schrijven van
*nieuwe zinnen*. Dat is de vergissing die het verschil maakt tussen redigeren en
schrijven.

## Ontbrekende mechanismen

1. **Generatieve patronen per functie.** Niet "vermijd X", maar "een opening
   werkt zo, hier zijn drie gepubliceerde voorbeelden, schrijf er nu een naar dat
   patroon". Voor opening, mechanisme, aarding, case, tegenwerping, cijfer, slot.
   Met de verplichting om de beweging daadwerkelijk te maken en niet alleen te
   lezen.
2. **Herschrijven vanaf de feiten in plaats van patroonschrappen.** Een
   decompileerstap (feiten, claims, spanning, volgorde) en een compileerstap
   waarin de bronformulering niet in beeld is. Anti-verankering als expliciete
   werkregel, niet als goede bedoeling.
3. **Een kwaliteitsanker dat foutloos-maar-vlak afkeurt.** Een benchmarktekst en
   een toetsbare vraag die verder gaat dan de onderstreeptest: zou deze alinea
   het uithouden naast het specimen met dezelfde functie? Zo nee, opnieuw
   schrijven, niet bijschaven. "Geen fouten" moet expliciet onvoldoende zijn.
4. **Een stijlkeuzemoment over de stem, vóór het schrijven.** Type output, lezer,
   register, lengte, hoeveel positie de tekst inneemt, en welke ene passage de
   lezer moet onthouden. Bij afwezige gebruiker: beredeneerde defaults, gemeld.
5. **Iteratie met vers oog.** Minstens één beoordelaar of herschrijver die het
   origineel niet heeft gezien, en minstens één lus waarin de tekst opnieuw
   wordt geschreven in plaats van alleen ingekort. Het huidige "één ronde
   volstaat" is het duurste stopcriterium in de set.
6. **Een investeringsbudget, geen snijquotum.** Wat je bespaart, geef je uit aan
   de passage die het hoofdstuk draagt. Formuleer het als opdracht: per hoofdstuk
   één passage die het volle gewicht krijgt, met een concreet geval, één getal en
   het perspectief van wie het aangaat.
7. **Eigenaarschap van de compositie.** Wie ontwerpt de boog, de plaatsing van
   het concrete, de plek van de citeerbare alinea, het punt waar de tegenwerping
   wordt binnengelaten. Nu doet niemand dat.
8. **Stemvasthouding over lange teksten.** De humanizer benoemt stijldrift
   (patroon 38) maar lost het op met "draai de pas per sectie". Wat ontbreekt is
   een vast anker: een vastgelegde eerste alinea of stemfragment waar elke
   volgende sectie tegenaan wordt gehouden.
9. **Bevoegdheid om te schrijven, met een scherpe grens.** Onderscheid tussen
   nieuwe *taal* (toegestaan en gewenst: bruggen, openingen, herformuleringen)
   en nieuwe *feiten* (verboden). Plus een expliciet kanaal voor gaten: vraag het
   ontbrekende gegeven op, of markeer het gat zichtbaar. Nu is de enige
   toegestane oplossing "schrap de abstractie".
10. **Klank als positief werk.** Hardop lezen bestaat, maar alleen als filter
    ("haal eruit wat struikelt"). Er is geen prosodie-werk: waar de klemtoon
    valt, welke zin de korte is, hoe de zinslengtereeks klinkt als muziek in
    plaats van als variatiequotum.

## Aanbevelingen voor de nieuwe skill

**A. Draai de verhouding om: minstens twee keer zoveel generatief materiaal als
verbodsmateriaal.** De verbodslijst gaat naar een referentie die aan het eind
één keer wordt afgedraaid. Het hart van de skill wordt een schrijfdeel met
patronen om naartoe te schrijven. Concreet: verplaats de humanizer naar een
eindcontrole en promoveer `specimens.md` tot hoofdinstrument.

**B. Herschrijf de Na-voorbeelden.** Elk voorbeeld in de nieuwe skill moet iets
demonstreren wat een lezer zou onderstrepen, niet iets wat geen fout bevat. Waar
een voorbeeldpaar nu eindigt in een correcte mededeling, hoort er een derde
kolom bij: de versie die je zou doorsturen. Dit is de goedkoopste ingreep met de
grootste verwachte opbrengst.

**C. Bouw de decompileer-compileerlus in.** Per passage: haal de feiten, claims
en de spanning eruit; leg het bronproza weg; schrijf de passage vanaf die lijst
naar het patroon van het bijpassende specimen; vergelijk pas daarna met de
bron, en uitsluitend om te controleren of er een feit is weggevallen. Dit is het
enige mechanisme dat de verankering echt doorbreekt.

**D. Vervang het snijquotum door een tweezijdig budget.** Netto korter (richtlijn
15–35%), maar met een expliciete investeringsopdracht: één dragende passage per
hoofdstuk krijgt méér ruimte dan hij nu heeft. Meet beide, en keur een tekst af
die overal even kort is geworden. Ongelijke lengte is informatie voor de lezer;
dat staat al in `modeltics.md` en moet worden gepromoveerd tot ontwerpregel.

**E. Zet een derde motor naast de ondervrager en de lezer: de jury.** Een verse
agent die het origineel niet kent, twee versies naast elkaar krijgt (de nieuwe
tekst en een gepubliceerd specimen met dezelfde functie, of de vorige iteratie)
en één vraag beantwoordt: welke is door een mens geschreven, welke zou je
doorlezen, en waar precies zakt de andere door. Die uitkomst stuurt de volgende
ronde. Diagnose vraagt geen oordeel; kwaliteit vraagt er wel om.

**F. Maak de lus echt een lus, met een stopregel op kwaliteit in plaats van op
afvinken.** Schrijven, jureren met vers oog, opnieuw schrijven, maximaal drie
ronden. Stop als de jury de tekst niet van gepubliceerd werk onderscheidt, niet
als negen vakjes ja staan.

**G. Zet het stijlkeuzemoment vooraan en laat het over de stem gaan.** Eén
AskUserQuestion: type output, lezer, register, doellengte, hoeveel positie,
en welke ene zin de lezer moet onthouden. Dat laatste is de belangrijkste vraag
van de hele skill en wordt nu nergens gesteld. Zonder gebruiker: defaults uit de
tekst, bovenaan het logboek.

**H. Geef de skill een expliciet mandaat om te schrijven.** Formuleer het als
twee regels naast elkaar. Nieuwe zinnen, bruggen, openingen, ritme en beeldloze
herformuleringen: gewenst. Nieuw feit, cijfer, jaartal, naam, citaat of case:
verboden, en een gat markeer je of vraag je op. De huidige formulering verbiedt
per ongeluk het eerste samen met het tweede.

**I. Laat de laatste pas een schrijfpas zijn, geen schrappas.** Eindig met
hardop lezen en de bevoegdheid om te herschrijven, en pas daarna de mechanische
eindcontrole. De volgorde "opruimen, dan leveren" garandeert nu dat het laatste
wat er met de tekst gebeurt een aftrekking is.

**J. Verlaag de nalevingslast fors.** Schrap vier van de vijf tellingen, de
percentagemeting en het merendeel van de eindpoort. Houd één meting die iets
stuurt (woorden voor/na) en één kwaliteitstoets per sectie (de onderstreepzin).
De vrijgekomen aandacht gaat naar het proza. Nauwkeuriger boekhouden heeft nog
nooit een zin mooier gemaakt.

**K. Anker de stem tegen drift.** Leg na de eerste geslaagde passage een
stemfragment vast en houd elke volgende sectie daar letterlijk tegenaan. Doe bij
lange documenten een slotcontrole waarin het oudste en het nieuwste deel naast
elkaar worden gelezen; dat is de plek waar het register altijd uiteenloopt.

**L. Één skill, één stem-definitie, en trigger breed.** De nieuwe skill moet
zelf de baas zijn over het register en de vier stijlskills als parameter
gebruiken, niet naast zich dulden. En hij moet triggeren waar de humanizer nu
triggert, anders krijgt de praktijk opnieuw alleen de patroonstripper.

**Ten slotte, de lat waar de skill zichzelf aan moet meten.** Niet: bevat deze
tekst nog AI-patronen. Wel: zou een redacteur van een goed rapport deze passage
laten staan, en zou een lezer er één zin uit onthouden. De huidige skills
beantwoorden de eerste vraag uitstekend en de tweede nergens.

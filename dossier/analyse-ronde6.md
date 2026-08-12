# Analyse ronde 6 — v4.0 tegen de kampioenen van v3.2

Opzet: de architectuur van v4.0 (betooglaag vooraan, stem als voice DNA,
hygiëne als losse pas) tegen de best gemeten output van de v3.2-familie, per
testtekst, blind, één jury per tekst. Wisselende letters, mapping buiten de
repo.

## Uitslag

| Tekst | v3.2-kampioen | v4.0 | Winnaar |
|---|---|---|---|
| T1 rapporthoofdstuk | 7,6 (r4/S3-T1) | **4,0** (diskwalificatie feiten) | v3.2 |
| T2 bestuurlijke samenvatting | 6,7 (r5/S4-T2) | 6,5 | v3.2 |
| T3 casetekst | 7,8 (r2/S-T3) | **4,0** (diskwalificatie feiten) | v3.2 |

Geen enkele output haalde de Turingpoort. In alle drie de rapporten werd de
v4.0-output eerder voor modelwerk gehouden dan de v3.2-output.

Twee kanttekeningen bij de opzet, beide in het nadeel van v3.2 en beide
onvoldoende om de uitslag te verklaren. De blinde set voor T2 bevatte in de
v3.2-versie achtergebleven bestandskoppen (`# S4-T2`, `## Tekst`), een fout in
het stripscript; de jury noemde dat expliciet bij de Turingpoort en de versie
won alsnog. En v4.0 leverde op T1 en T2 langere teksten (599 tegen 520; 423
tegen 327 woorden), wat de kortingsregel van de rubriek in zijn nadeel werkt.

## Wat er misging, en waarom het ontwerp de schuld draagt

### 1. De opgevoerde spreker — twee diskwalificaties

T3 schreef *"Een fondsmanager vraagt dan: …"* — een citaat in directe rede van
een persoon die niet bestaat. T1 voerde een wethouder op met motieven die de
bron niet noemt. Beide komen uit dezelfde instructie: fase B2 vroeg het
sterkste bezwaar op te schrijven **"in de woorden van je doellezer"**. Die
formulering nodigt uit tot een personage, want een bezwaar wordt levendiger
zodra iemand het zegt.

Dit is het mechanisme uit wet 3 van het vorige traject ("de menselijkste zinnen
zijn de gevaarlijkste"), maar één laag hoger: niet de zin verzint, de *fase*
verzint. De skill verbood het verzinnen op twee plaatsen en maakte het
tegelijk aantrekkelijk op een derde. Een verbod dat concurreert met een
uitnodiging in dezelfde skill, verliest.

### 2. Het cijfer dat naar het betoog toe boog

T1 noemde een factor 1,6 (4,5 naar 7,2 jaar) *"bijna verdubbeld"*, en hing er
een oorzaak aan die de bron slechts als mogelijke gedeeltelijke verklaring
geeft. De jury: "B schrijft de mooiste losse zin van de twee maar bouwt zijn
scherpte op cijfers die niet houden."

Dit is de ernstigste bevinding, omdat hij niet over slordigheid gaat maar over
een krachtenveld. Een premisse die vroeg in het proces wordt vastgelegd, zet
druk op elk cijfer dat erna langskomt: de schaalvertaling wordt gekozen om te
kloppen met de stelling in plaats van met de F-regel. v3.2 had daar twee
remmen op (X10 als budget, plus een aparte doseringscontrole); v4.0 hield de
regel wel en de tellers niet.

### 3. De tic-regressie

Drie juries noemden onafhankelijk hetzelfde: spiegelpaar bij elk scharnier, één
aforisme per sectie, vier tot vijf klapzinnen, koppen in dezelfde verdictmal.
v4.0 had de budgetten van v3.1 vervangen door een breed repertoire (negentien
bewegingen, elk hoogstens één keer) in de veronderstelling dat breedte
rantsoenering overbodig maakt.

Dat is empirisch weerlegd. De reden is dat "elk hoogstens één keer" door niets
werd afgedwongen: het stond in `stem.md` als aanbeveling, de doseringscontrole
was geschrapt, en uit het script waren X1 (klapzin) en X10 (schaalvertaling)
verdwenen terwijl X4 een regex had die de "X wel, Y niet"-variant niet zag. Met
de oude meetlat stonden alle drie de teksten op X4 groen; met de teruggezette
meetlat staan alle drie op rood, en X12 vangt de verzonnen fondsmanager.

## De wet die deze ronde oplevert

**Wet 6. Een betooglaag zonder eigen feitenpoort verplaatst het verzinnen van
de zin naar de premisse.** Aftrekkend redigeren heeft een plafond (wet 1), maar
generatief redigeren heeft een risico dat een orde van grootte groter is: waar
v3.2 correcte, kleine teksten leverde, leverde v4.0 scherpere teksten die
tweemaal diskwalificeerden op feiten. De oplossing is niet terug naar
aftrekken, en ook geen compromis daartussen. Het is dat elk element van de
argumentlaag — premisse, tegenwerping, antwoord, gezag — zijn dossierregels
noemt vóór het schrijven begint, met dezelfde discipline die de beweringen in
B5 al droegen.

**Wet 7. Breedte en dosering zijn complementair, geen alternatieven.** Een
repertoire aanbieden verhoogt het plafond; een teller voorkomt dat de schrijver
zijn favoriete beweging drie keer inzet. v3.1 had de teller zonder het
repertoire, v4.0 het repertoire zonder de teller. Beide falen, op een andere
manier.

## Wat v4.1 verandert

1. **B2 voert geen spreker op.** Het bezwaar is een bewering over de zaak, niet
   een uitspraak van iemand. Geen directe rede van wie de bron niet citeert,
   geen partij met een motief dat de bron niet noemt.
2. **B2 en B3 noemen hun dekking**, net als B5. Een tegenwerping zonder F- of
   K-regel, of zonder een gat uit A4, gaat de tekst niet in. Een antwoord dat
   een bewering over bewijsbasis, methode of toerekening nodig heeft, is een
   feit en niet een voorzichtigheid.
3. **B3b, nieuw en op elke route verplicht:** onderstreep elk getal en elke
   verhouding in premisse, tegenwerping, antwoord en gezag, reken ze terug uit
   de F-regels, en noteer de uitkomst met de F-nummers. Klopt de vertaling niet
   exact, dan valt de vertaling weg en niet het cijfer.
4. **De doseringscontrole is terug als D3.3**, met plafonds op de figuren en de
   regel dat je het zwakste exemplaar schrapt en de passage herschrijft.
5. **Het script telt weer:** X1 (klapzin ≤ 2) en X13 (schaalvertaling ≤ 2) zijn
   teruggezet, X4 is verscherpt met de "X wel, Y niet"-variant, en X12
   (opgevoerde spreker) is nieuw. Verificatie op de drie outputs van ronde 6:
   alle drie de diskwalificerende of tic-veroorzakende passages worden nu
   mechanisch gevangen, waar de v4.0-meetlat ze groen liet.
6. De eindpoort gaat van zes naar acht vragen; logregel 3 draagt de dekking van
   de tegenwerping, logregel 6 de doseringstellingen en de herrekende
   schaalvertalingen.

## Wat nog niet is aangetoond

Dat v4.1 wint. De reparaties zijn afgeleid uit drie juryrapporten en
mechanisch geverifieerd op de bestaande outputs, maar er is nog geen ronde 7
gedraaid. Tot dat gebeurt is de eerlijke stand: **v3.2 is de best geteste
versie**, en v4.1 is een beter onderbouwd ontwerp met een openstaande
verificatie. De architectuurwinst van v4.0 — een `SKILL.md` van een kwart van
de lengte, één subagent in plaats van vier, een betooglaag die aantoonbaar
andere teksten oplevert — staat daar los van en is niet weersproken door deze
ronde.

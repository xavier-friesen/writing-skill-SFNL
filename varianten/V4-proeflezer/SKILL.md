---
name: v4-proeflezer
description: Zet AI-gegenereerde Nederlandse concepttekst om in publiceerbare rapporttekst voor Social Finance NL via een harde meetlat en een koude lezer. Meet ritme, zinsbouw, concreetheid en aanwezigheidscriteria met een telscript, laat een verse doellezer de tekst op leessnelheid lezen, en herschrijft gericht tot alle drempels slagen. Gebruik bij rapporthoofdstukken, bestuurlijke samenvattingen, casetekst, notities en andere klantgerichte SFNL-tekst.
---

# De proeflezer

Je krijgt: een invoertekst, eventueel teksttype en doellezer, en de antwoorden van
de gebruiker op de stijl-check-in. Je levert: publiceerbare Nederlandse rapporttekst.

Deze skill werkt met twee instrumenten en één lus.

1. **De meetlat.** Twintig drempels die vooraf vastliggen. Je telt ze écht — met het
   script in §4 en met de hand waar het script niet bij kan. Geen schattingen, geen
   "voelt goed". Een meting is groen of rood; iets ertussenin bestaat niet.
2. **De koude lezer.** Een verse agent die het origineel niet kent, de meetlat niet
   kent en niet weet dat de tekst is herschreven. Hij leest op leessnelheid en meldt
   wat hij waarneemt: waar hij ging scannen, wat hij onthield, welke zin hij zou
   doorsturen.
3. **De lus.** Meet → gericht herschrijven → opnieuw meten, met elke ronde een nieuwe
   koude lezer. Je stopt als alle metingen groen zijn én de koude lezer niets meldt.

De meetlat zonder de koude lezer levert metrisch correcte dode tekst. De koude lezer
zonder de meetlat levert een mening. Samen convergeren ze.

## 0. Invarianten — niet onderhandelbaar, in deze voorrang

1. **Feiten exact.** Elk cijfer, bedrag, jaartal, percentage, naam en plaats staat in
   de output zoals in de bron. Een verwachting wordt geen bevinding, een bandbreedte
   geen puntschatting, "overweegt" geen "besluit".
2. **Niets verzinnen.** Geen getal, voorbeeld, citaat, naam of case die niet in de
   bron of het gesprek staat. **Wel** nieuwe taal: nieuwe zinnen, bruggen, openingen,
   ritme en herformuleringen zijn niet alleen toegestaan maar de opdracht. Ontbreekt
   er een gegeven dat het betoog nodig heeft, dan markeer je dat als `[ontbreekt: …]`
   en meld je het in het logboek. Je vult het niet in.
3. **Korter.** De output is 15 tot 35 procent korter dan de invoer. Nooit langer.
4. **Eén levering.** Plakklare tekst plus een logboek van maximaal acht regels.
   Geen tussenkopjes met commentaar, geen varianten, geen toelichting bij de tekst.
5. **Een meting mag nooit een feit breken.** Zakt een meting alleen te repareren door
   een cijfer te wijzigen of weg te laten dat het betoog draagt, dan wint het feit.

## 1. De stijl-check-in

Doe dit vóór je één zin schrijft, met één `AskUserQuestion`-aanroep, vier vragen.
Lees eerst de invoertekst, zodat je opties kunt afleiden in plaats van verzinnen.

**Vraag 1 — Teksttype.** header `Teksttype`.
Opties: `Rapporthoofdstuk` (betoog met casuïstiek) · `Bestuurlijke samenvatting`
(antwoord vooraan, 60–70% resolutie) · `Casetekst` (één praktijkgeval, concreet
eerst) · `Notitie` (kort, één beslissing).

**Vraag 2 — Doellezer.** header `Lezer`.
Opties: `Bestuurder gemeente` (weinig tijd, wil de keuze) · `Beleidsadviseur`
(kent het dossier, wil het mechanisme) · `Financier of investeerder` (wil risico,
rendement en looptijd) · `Intern SFNL` (mag scherper, minder uitleg).

**Vraag 3 — Positie.** header `Positie`. Dit stuurt hoe hard de tekst kiest.
Opties: `Stelling nemen` (de tekst zegt wat er moet gebeuren en aanvaardt weerwoord)
· `Voorkeur tonen` (afgewogen, maar de lezer weet waar wij staan) · `Feitelijk
melden` (bevindingen, oordeel bij de lezer).

**Vraag 4 — De ene zin.** header `Kernboodschap`. "Wat moet de lezer over een week
nog weten?" Bied als opties drie kandidaat-kernboodschappen die je zelf uit de
invoertekst hebt gedestilleerd, elk als hele zin over de zaak. Dit is de
belangrijkste vraag: de gekozen zin wordt het richtpunt van elke ronde.

**Defaults als de gebruiker niet antwoordt.** Werk door, vraag niet nog eens, en meld
de gekozen defaults in logboekregel 1.
- Teksttype: uit de frontmatter of het kopniveau van de invoer; anders
  `rapporthoofdstuk`.
- Lezer: uit de frontmatter; anders `beleidsadviseurs en bestuurders`.
- Positie: `voorkeur tonen`. Bij een invoer waarin één bevinding aantoonbaar tegen de
  verwachting in gaat: `stelling nemen`.
- Kernboodschap: de zin die het duurst is om te schrappen — meestal de bevinding die
  het slechtst uitkomt voor de opdrachtgever, niet de best scorende uitkomst.
- Register: SFNL-huis. "Wij" is de auteur, nooit de lezer. Geen "u", geen "je"
  buiten citaten. Tegenwoordige tijd, verleden tijd voor casushistorie en resultaten.
  Elke claim heeft een genoemd subject.

## 2. De meetlat

Twintig drempels in vier groepen. **A-metingen zijn aanwezigheidseisen** — daar moet
iets ín de tekst zitten. Die vervallen nooit. R, Z, V en C zijn vorm- en
afwezigheidseisen; daarvoor geldt de uitweg in §6.

### R — ritme (script)

| | Meting | Drempel | Herkomst |
|---|---|---|---|
| R1 | SD van de zinslengte / burstiness | SD ≥ 7,0 én SD/gemiddelde ≥ 0,45 | mens 8,2; Claude 5,3 |
| R2 | Elk schuivend venster van 10 zinnen | bereik ≥ 25 woorden én kortste zin ≤ 8 | ai-tells 12 |
| R3 | Drie opeenvolgende zinnen | nooit binnen 2 woorden van elkaar | Onze Taal |
| R4 | Gemiddelde zinslengte | 13 tot 19 woorden | Onze Taal + huisstem |
| R5 | Langste zin | ≥ 30 woorden, en in één adem voorleesbaar | Twain-toets |

R1 alleen is niet genoeg: een bulletlijst met labels haalt een hoge SD zonder ritme.
R2 is de echte toets, want die eist een korte zin *op de plek waar hij landt*.

### Z — Nederlandse zinsbouw (script + hand)

| | Meting | Drempel |
|---|---|---|
| Z1 | Persoonsvorm na zinsstart | binnen 7 woorden in ≥ 90% van de zinnen, nooit later dan 10 |
| Z2 | Tang: woorden tussen bij elkaar horende delen | ≤ 8, nul overtredingen |
| Z3 | Nominalisaties (-ing, -atie, -heid, -ment, -iteit) | ≤ 1 per 2 zinnen |
| Z4 | Werkwoordstapel aan het zinseinde | nooit 3 of meer |
| Z5 | Voorzetselgroepen in één zinsdeel | ≤ 3 |

Z1, Z2, Z4 en Z5 tel je met de hand: neem de tien langste zinnen uit de scriptuitvoer
en tel ze woord voor woord. Schrijf de getallen op. Een lange zin zonder tang is
beter dan een korte met tang; knip dus nooit alleen op lengte.

### A — aanwezigheid (hand, plus koude lezer)

| | Meting | Drempel |
|---|---|---|
| A1 | Onderstreepbare zin per sectie | elke sectie ≥ 1; noteer welke |
| A2 | Nutzin — waar gaat dit over en waarom lees je door | uiterlijk in alinea 2 |
| A3 | Concreet gegeven uit de bron per alinea | ≥ 1 getal, naam, bedrag, datum of plaats |
| A4 | Zin waarop de auteur over drie jaar afgerekend kan worden | ≥ 1 in de tekst |
| A5 | De kostenkant: wie betaalt, wie geeft iets op | ≥ 1 keer expliciet |
| A6 | Modale partikels (toch, wel, immers, juist, althans, overigens) | ≥ 1 per 150 woorden |
| A7 | Verschillende verbindingswoorden | ≥ 6 per 800 woorden, geen enkel meer dan 3× |
| A8 | Dragende sectie | langste sectie ≥ 1,8 × de mediane sectie |

A6 en A8 zijn er om de meetlat tegen zichzelf te beschermen. A6 blokkeert de
doodgepoetste tekst: nul partikels betekent dat er een vertaalrobot aan het werk was.
A8 blokkeert de symmetrie: de passage die het hoofdstuk draagt hoort ruimer te zijn
dan de rest, en de bespaarde woorden gaan daarheen.

### V en C — afwezigheid en cijfers (script + hand)

| | Meting | Drempel |
|---|---|---|
| V1 | Verboden woorden en voorzetseluitdrukkingen (lijst in het script) | 0 |
| V2 | Negatieve parallellismen · drieslagen | ≤ 1 · ≤ 1 |
| V3 | Gedachtestreepje als bijzin · Oxford-komma · vet in lopende tekst · Title Case | 0 |
| V4 | Hedgewoorden | ≤ 3 per 100 woorden, nooit twee in één zin |
| V5 | Aankondigen en samenvatten ("in dit hoofdstuk", "kortom", "al met al") | 0 |
| V6 | Zelfde beginwoord van een zin | ≤ 2× in de hele tekst |
| C1 | Getallen | max 2 significante cijfers, tenzij het bronfeit exact is |
| C2 | Elk kerngetal | een schaalvertaling of vergelijkingspunt in dezelfde alinea |
| C3 | Nieuwe getallen per alinea | ≤ 3 |
| L1 | Lengte | 15–35% korter dan de invoer |
| F1 | Feiten | 100% van de feitenlijst correct, 0 toevoegingen |

## 3. Hoe je de meetlat NIET haalt

Elke drempel is te faken. Faken wordt zichtbaar bij de koude lezer, en het is de
snelste manier om een 4 te scoren op menselijkheid. Per meting: de legitieme
reparatie, en de verboden.

- **R2 (korte zin).** Legitiem: de korte zin is de conclusie van de lange ervoor, of
  het feit waar de alinea op uitkomt. Verboden: losse dramazinnen ("Dat is de kern."),
  fragmenten zonder werkwoord, telegramstijl met dubbele punten. Eén klapzin per
  tekst, hoogstens.
- **R1/R4 (spreiding).** Legitiem: één zin die twee dingen verbindt omdat ze verbonden
  moeten worden. Verboden: twee correcte zinnen met "waarbij" aan elkaar plakken.
- **Z3 (nominalisaties).** Legitiem: de handeling terug in het werkwoord, mét de
  handelende partij ervoor. Verboden: het woord vervangen door een synoniem zonder
  suffix.
- **A6 (partikels).** Legitiem: het partikel staat waar de spreker aarzelt, toegeeft
  of nadruk legt. Verboden: "toch" en "wel" instrooien tot de teller klopt.
- **A7 (connectieven).** Legitiem: het verbindingswoord markeert de logische relatie
  die er werkelijk is. Verboden: "echter" vervangen door "evenwel" om de variatie op
  te krikken. Klopt de relatie niet, dan is een fout woord erger dan herhaling.
- **A1 (onderstreepbaar).** Legitiem: de zin zegt iets dat iemand kan bestrijden, of
  hij zet een getal naast het getal waar het iets mee doet. Verboden: een zin
  vetdrukken, of een abstracte samenvatting scherp laten klínken.
- **V6 (zinsbegin).** Legitiem: de alinea begint bij een ander onderdeel van de zaak.
  Verboden: de zin omkeren tot hij stroef wordt. Breek liever V6 dan iets barbaars te
  schrijven — en meld dat in het logboek.

Overkoepelend: haal je een drempel alleen door de zin lelijker te maken, dan laat je
de drempel vallen en noteer je het. Dat mag hoogstens één keer per tekst, en nooit
voor een A-meting.

## 4. Het telscript

Schrijf dit naar je scratchpad als `meetlat.py` en draai het met
`python3 meetlat.py tekst.md`. Draai het op de **invoer** (nulmeting) en na **elke**
herschrijfronde. Plak de uitvoer niet in de levering; je gebruikt hem om te sturen.

```python
import re, sys, statistics as st
from collections import Counter

T = open(sys.argv[1], encoding='utf-8').read()
KOP = re.findall(r'^#{1,6}\s*(.+)$', T, flags=re.M)
SEC = [s for s in re.split(r'^#{1,6}.*$', T, flags=re.M) if s.strip()]
B = re.sub(r'^#{1,6}.*$', '', T, flags=re.M)
B = re.sub(r'^\s*[-*]\s+', '', B, flags=re.M).replace('**', '')
ALI = [x for x in re.split(r'\n\s*\n', B) if x.strip()]
w = lambda s: [x for x in s.split() if re.search(r'[\wÀ-ÿ]', x)]
def zinnen(t):
    t = re.sub(r'\s+', ' ', t)
    return [z.strip() for z in re.split(r'(?<=[.!?])\s+(?=[«"\'(A-ZÀ-Þ0-9])', t) if len(z.strip()) > 1]
Z = zinnen(B); L = [len(w(z)) for z in Z]; N = sum(L)
p = lambda ok, k, v: print(f"{'OK  ' if ok else 'ROOD'} {k:<26} {v}")
print(f"--- {N} woorden, {len(Z)} zinnen, {len(ALI)} alinea's, {len(SEC)} secties")

sd = st.pstdev(L) if len(L) > 1 else 0; gem = N/max(len(L), 1)
p(sd >= 7.0, "R1 SD zinslengte", f"{sd:.1f} (>= 7,0)")
p(gem and sd/gem >= .45, "R1 burstiness", f"{sd/max(gem,1):.2f} (>= 0,45)")
p(13 <= gem <= 19, "R4 gem. zinslengte", f"{gem:.1f} (13-19)")
vs = [(i, max(L[i:i+10])-min(L[i:i+10]), min(L[i:i+10])) for i in range(max(len(L)-9, 1))]
bad = [f"venster {i+1}: bereik {b}, kortste {m}" for i, b, m in vs if b < 25 or m > 8]
p(not bad, "R2 venster van 10", bad[:3] if bad else f"{len(vs)} vensters, bereik >= 25 en kortste <= 8")
dr = [f"zin {i+1}: {L[i:i+3]}" for i in range(len(L)-2) if max(L[i:i+3])-min(L[i:i+3]) <= 2]
p(not dr, "R3 3 zinnen ~gelijk", dr[:3] if dr else "geen")
p(bool(L) and max(L) >= 30, "R5 langste zin", f"{max(L) if L else 0} (>= 30)")

low = B.lower()
STOP = {"ding","dingen","koning","ring","woning","kring","overheid","gezondheid","moment","momenten"}
nom = [x for x in re.findall(r"\b\w{4,}(?:ingen|ing|aties|atie|iteit|heden|heid|menten|ment)\b", low) if x not in STOP]
p(len(nom) <= len(Z)/2, "Z3 nominalisaties", f"{len(nom)} = {len(nom)/max(len(Z),1):.2f}/zin (<= 0,50) {Counter(nom).most_common(6)}")
VERB = "cruciaal essentieel faciliteren faciliteert navigeren landschap robuust naadloos baanbrekend toekomstbestendig holistisch integraal integrale borgen borging ontzorgen impactvol randvoorwaardelijk adresseren meerwaarde handelingsperspectief stakeholder ecosysteem middels derhalve inzake alsmede zulks bewerkstelligen problematiek aanknopingspunten aandachtspunten".split()
UITDR = ["in het kader van","met betrekking tot","ten aanzien van","ten behoeve van","met behulp van","in verband met","aan de hand van","op het gebied van","in het licht van"]
vh = [x for x in VERB if re.search(r'\b'+x+r'\b', low)] + [u for u in UITDR if u in low]
p(not vh, "V1 verboden woorden", vh if vh else "geen")
HED = ["mogelijk","wellicht","enigszins","vermoedelijk","naar verwachting","vrijwel","doorgaans","veelal","in zekere zin","over het algemeen","in beginsel","in principe","lijkt erop","zou kunnen","vooralsnog","nagenoeg","relatief","in belangrijke mate"]
hh = sum(len(re.findall(h, low)) for h in HED)
p(hh*100/max(N,1) <= 3, "V4 hedgedichtheid", f"{hh} = {hh*100/max(N,1):.1f}/100w (<= 3)")
PART = ["toch","wel","nu eenmaal","immers","juist","eens","althans","overigens","weliswaar","nou","maar liefst","zelfs"]
pa = sum(len(re.findall(r'\b'+re.escape(x)+r'\b', low)) for x in PART)
p(pa >= N/150, "A6 modale partikels", f"{pa} (>= {N/150:.1f}; nul = doodgepoetst)")
CONN = ["maar","toch","immers","namelijk","weliswaar","althans","overigens","juist","daarom","doordat","terwijl","hoewel","zodat","dus","want","omdat","tenzij","temeer","vandaar","echter","bovendien","daarnaast","kortom","tot slot","tevens"]
cc = {x: len(re.findall(r'\b'+re.escape(x)+r'\b', low)) for x in CONN}
cc = {k: v for k, v in cc.items() if v}
p(len(cc) >= 6*N/800 and (max(cc.values()) if cc else 9) <= 3, "A7 connectieven", f"{len(cc)} soorten, max {max(cc.values()) if cc else 0}x {cc}")
sw = [f"'{k}' {v}x" for k, v in Counter(' '.join(w(z)[:2]).lower() for z in Z if w(z)).items() if v > 2]
sw += [f"'{k}' {v}x" for k, v in Counter(w(z)[0].lower() for z in Z if w(z)).items() if v > 2 and k not in ("de","het","een")]
p(not sw, "V6 zinsbegin herhaald", sw if sw else "geen bigram of niet-lidwoord >2x")
tel = {"em-streepje": len(re.findall(r'[—–]', B)), "Oxford-komma": len(re.findall(r'\w+,\s+\w+,\s+(?:en|of)\s', B)),
       "vet in tekst": len(re.findall(r'\*\*', T))//2, "drieslag": len(re.findall(r'\b\w+, \w+ en \w+\b', B)),
       "niet-alleen-maar": len(re.findall(r'niet alleen|niet zozeer|het gaat niet om', low)),
       "meta/samenvat": len(re.findall(r'in dit hoofdstuk|in deze paragraaf|hieronder|samengevat|kortom|al met al|zoals eerder|tot slot', low))}
p(all(v == 0 for k, v in tel.items() if k != "drieslag") and tel["drieslag"] <= 1, "V2/V3/V5 tells", tel)
sl = sorted(len(w(s)) for s in SEC if len(w(s)) > 20)
med = st.median(sl) if sl else 1
p(len(sl) < 3 or sl[-1] >= 1.8*med, "A8 dragende sectie", f"{sl} langste/mediaan {sl[-1]/med:.1f}x (>= 1,8)" if sl else "n.v.t.")
def sig(x):
    d = re.sub(r'[.,]', '', x).lstrip('0').rstrip('0')
    return len(d) if d else 1
gt = sorted({x for x in re.findall(r'\b\d[\d.,]*\b', B) if sig(x) > 2 and not re.fullmatch(r'(19|20)\d\d', x)})
print("MELD C1 >2 sign. cijfers  ", gt or "geen", "-- bronfeit: laten staan; afgeleid: afronden")
print("MELD koppen Title Case?   ", [k for k in KOP if len(re.findall(r'\s[A-ZÀ-Þ]', k)) >= 3] or "nee, zinskapitalisatie ok")
```

Wat het script niet kan: Z1, Z2, Z4, Z5, A1 tot A5, C2, C3, F1 en de leesbaarheid van
lange zinnen. Die tel je zelf, met de zinnen erbij, en je schrijft de getallen op.
Het script is een hulpstuk, geen rechter — een nominalisatie in een vakterm
(*resultaatfinanciering*) telt mee in de teller maar is geen defect.

## 5. De koude lezer

Start na elke herschrijfronde een **verse subagent**. Geef hem uitsluitend: de huidige
versie van de tekst, het teksttype en de doellezer. Geef hem níét het origineel, niet
de meetlat, niet de kernboodschap, en niet de mededeling dat de tekst herschreven is.
Heb je geen subagent-tool, doe dit dan in één schone doorloop: lees de tekst één keer
op leessnelheid, zonder terug te lezen, en beantwoord de zes vragen vóórdat je de
meetlat er weer bij pakt.

**Briefing, letterlijk mee te geven:**

> Je bent [doellezer]. Je leest deze tekst één keer, op leessnelheid, zoals je hem op
> een dinsdagmiddag zou lezen. Je leest niet terug. Beantwoord daarna zes vragen.
> 1. Vanaf welke zin ging je scannen of overslaan? Citeer die zin letterlijk. Zo niet:
>    "niet gescand".
> 2. Wat weet je nu nog, zonder terug te kijken? Noem maximaal drie dingen.
> 3. Welke ene zin zou je doorsturen aan een collega met "lees dit even"? Citeer hem
>    letterlijk. Geen zin gevonden is een geldig antwoord en het antwoord dat je geeft
>    als het waar is.
> 4. Welke zin moest je twee keer lezen? Citeer hem. Zo niet: "geen".
> 5. Wat wilde deze tekst je laten geloven, en geloofde je het?
> 6. Is dit geschreven door iemand die erbij was, of door iemand die het heeft
>    samengevat? Eén zin waarom.
>
> Je geeft geen verbeteradvies, geen stijloordeel, geen compliment en geen kritiek.
> Je rapporteert wat je waarnam. "Niets te melden" is een geldig antwoord op elke
> vraag; verzin geen bevinding om nuttig te zijn.

**De koude lezer slaagt als:** vraag 1 "niet gescand" is; minstens twee van de drie
onthouden dingen de kernboodschap raken en niet het decor; er een doorstuurzin is die
letterlijk in de tekst staat; vraag 4 "geen" is; en het antwoord op vraag 6 "iemand
die erbij was" luidt.

**Hoe je de antwoorden leest.** Het scanpunt wijst de sectie aan die opnieuw moet,
niet de zin. Onthoudt hij het decor in plaats van de kern, dan staat de kernboodschap
op de verkeerde plek of te zwak. Noemt hij een andere doorstuurzin dan jij had
aangewezen bij A1, dan is dat geen fout maar informatie: hij heeft gelijk, jij niet.
Zegt hij "samengevat" bij vraag 6, dan mist de tekst concreetheid, geen stijl —
herschrijf dan A3 en A4, niet de zinsbouw.

## 6. De lus

**Ronde 0 — kader.** Doe de check-in. Draai het script op de invoer en noteer de
nulmeting. Zet de feitenlijst apart: elk cijfer, bedrag, jaartal, percentage, naam en
plaats uit de invoer op één rij. Kies de dragende sectie (A8): welke passage moet
ruimer worden en waarvan gaat dat af.

**Ronde 1 — schrijven.** Herschrijf de hele tekst in één doorloop, met de meetlat
naast je en de kernboodschap boven je. Niet repareren zin voor zin: schrijf per sectie
opnieuw vanaf de feiten. Open met een feit (§7, paar 5), zet de nutzin in alinea 2,
geef elke sectie een onderstreepbare zin en geef de dragende sectie de ruimte. Meet
daarna. Stuur de koude lezer.

**Ronde 2 en 3 — gericht herschrijven.** Pak alléén de rode metingen en de meldingen
van de koude lezer. Werk in deze voorrang: F1 → L1 → A → Z → R → V. Herschrijf de
betrokken passage helemaal opnieuw; repareer niet lokaal, want een gerepareerde zin
erft de architectuur van de kapotte zin. Meet opnieuw en stuur een **nieuwe** koude
lezer — dezelfde tweemaal gebruiken maakt hem warm en dus waardeloos.

**Stopregel.** Klaar als alle metingen groen zijn én de koude lezer slaagt.
**Maximum: drie herschrijfronden.**

**Convergentiebewaking.** Tel na elke ronde het aantal rode metingen. Daalt dat aantal
niet ten opzichte van de vorige ronde, dan ben je aan het duwen in plaats van aan het
schrijven: stop, lever de vorige versie, en meld het in het logboek.

**Als na ronde 3 nog iets rood staat.**
- F1 en L1 zijn blokkerend. Die repareer je altijd, ook buiten de ronden om, en dat
  kost geen ronde: een feit terugzetten of een alinea schrappen is geen herschrijving.
- Een rode A-meting lever je niet. Die betekent dat een sectie leeg is. Schrijf die
  ene sectie opnieuw vanaf de feiten, met een oordeel erin, en lever daarna.
- Een rode R-, Z-, V- of C-meting lever je wel. Je noteert in logboekregel 5 de
  meting en de gemeten waarde, plus in één halve zin waarom forceren de tekst zou
  hebben beschadigd. Maximaal twee zulke regels; bij meer is de tekst niet af.

## 7. Voorbeeldparen

Vijf paren. Links wat een meting rood maakt, rechts wat hem groen maakt zonder de
tekst te verarmen. **De cijfers in deze voorbeelden zijn illustratief en nooit
bruikbaar als bron.** Ze demonstreren een beweging, geen feit.

**Paar 1 — R2, R3 en A6. Van dreun naar val.**
> ✗ De gemeente heeft in 2022 een resultaatcontract afgesloten met twee aanbieders van
> schuldhulp. De aanbieders ontvingen een vergoeding per deelnemer die binnen een jaar
> schuldenvrij was. Deze systematiek moest de prikkel verleggen van inspanning naar
> uitkomst. *(17 – 16 – 13 woorden; bereik 4)*
>
> ✓ Sinds 2022 betaalt de gemeente pas als iemand schuldenvrij is. Twee aanbieders
> tekenden. De ene rekende voor dat hij zeventien maanden moest voorfinancieren
> voordat de eerste euro binnenkwam, en tekende toch. *(10 – 3 – 18; bereik 15,
> partikel "toch")*

De korte zin staat waar de lezer adem nodig heeft, en de laatste vier woorden zijn de
zin die je zou onderstrepen. Rechts staat geen enkel feit meer dan links.

**Paar 2 — Z2, Z3 en C2. Tang uit, werkwoord terug, getal geschaald.**
> ✗ De implementatie van het monitoringsinstrument heeft, mede door de complexiteit
> van de gegevensuitwisseling tussen de betrokken organisaties, later plaatsgevonden
> dan voorzien. *(tang van 12 woorden tussen "heeft" en "plaatsgevonden"; drie
> nominalisaties)*
>
> ✓ De organisaties kregen hun gegevens pas in maart aan elkaar gekoppeld, een half
> jaar later dan gepland. Dat kostte geld: de uitvoeringskosten liepen op tot bijna
> een vijfde van het budget.

De dubbele punt doet wat "dit leidde ertoe dat" ook zou doen, in nul woorden. "Bijna
een vijfde" is de schaalvertaling van een percentage dat de lezer anders alleen leest.

**Paar 3 — A3 en A4. Van gemengd beeld naar een claim die iets kost.**
> ✗ De resultaten laten een gemengd beeld zien. Weliswaar zijn er positieve
> ontwikkelingen zichtbaar, maar de doelstellingen zijn niet volledig gerealiseerd.
> Dit onderstreept het belang van realistische verwachtingen bij dit type
> arrangementen.
>
> ✓ Het programma haalde de helft van wat de businesscase beloofde. De wachttijd ging
> omlaag, de instroom nauwelijks. Wie zo'n contract opstelt, doet er goed aan de
> raming te halveren voordat hij tekent.

De laatste zin is een uitspraak waarop de auteur over drie jaar aanspreekbaar is. Dat
is precies wat A4 eist en wat een sjabloon nooit produceert.

**Paar 4 — A5, V5 en het slot. Van vooruitblik naar prijs.**
> ✗ Al met al biedt de aanpak waardevolle aanknopingspunten voor de verdere
> doorontwikkeling van de schuldhulpverlening en vormt zij een solide basis om op
> voort te bouwen.
>
> ✓ De aanpak verlegt het risico naar de investeerder. De prijs daarvan is dat de
> gemeente de doelgroep niet meer tussentijds kan verbreden. Wie dat te duur vindt,
> moet niet aan een resultaatcontract beginnen.

Het slot vat niet samen, het rekent af. Schrap de linkerversie en er verdwijnt niets;
schrap de rechter en de lezer mist de enige zin die hem een besluit oplevert.

**Paar 5 — A2, V5 en de opening. Van aankondiging naar zaak.**
> ✗ In dit hoofdstuk wordt ingegaan op de wijze waarop innovatieve financieringsvormen
> kunnen bijdragen aan preventie. Achtereenvolgens komen de context, de structuur en
> de resultaten aan de orde.
>
> ✓ Drie gemeenten legden geld op tafel voordat er één gezin was geholpen. De vraag is
> wie dat terugverdient, en wanneer.

Zin één is een mededeling over de zaak met een handelend onderwerp; zin twee is de
nutzin, in alinea 1 in plaats van alinea 2. De inhoudsopgave is weg, en niemand mist
haar: de koppen doen dat werk al.

## 8. Levering

Eerst de tekst, dan het logboek. Niets ertussen, niets erna.

De tekst is plakklaar: koppen in zinskapitalisatie, geen vet in lopende tekst, geen
markdownresten, Nederlandse interpunctie (decimaalkomma, geen Oxford-komma,
gedachtestreepje met spaties en alleen waar het echt moet), geen commentaar van jou.

Daarna, exact dit format, maximaal acht regels:

```
1 Check-in    [antwoorden gebruiker | defaults, afgeleid uit de tekst: type, lezer, positie]
2 Kern        "[de ene zin die de lezer moet onthouden]"
3 Lengte      674 → 462 woorden (−31%); dragende sectie [naam], 2,1× de mediaan
4 Ronden      2 van 3; rode metingen 11 → 4 → 0
5 Eindmeting  SD 7,9 | burst 0,48 | venster min bereik 27 | nominalisaties 0,41/zin |
              partikels 5 | connectieven 8 soorten | verboden woorden 0 | hedges 1,2/100w
6 Koude lezer niet gescand; doorstuurzin "[…]"; toeschrijving: iemand die erbij was
7 Aanwezig    A1 4/4 secties | A2 alinea 1 | A4 "[…]" | A5 "[…]"
8 Openstaand  [geen | V6 "de" 3× — omkeren maakte de zin stroef | ontbreekt: …]
```

Regel 5 is verplicht en bevat gemeten getallen, geen kwalificaties. Staat er "goed" of
"in orde", dan heb je niet gemeten.

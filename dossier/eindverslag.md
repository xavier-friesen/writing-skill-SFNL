# Eindverslag: de bouw van sfnl-rapporttekst

Opdracht: een skill die AI-gegenereerde concepttekst omzet in complete,
publiceerbare Nederlandse rapporttekst — helder, scherp, vloeiend, niet van
menselijk topwerk te onderscheiden, gemeten tegen het niveau van The
Economist, NYT en McKinsey-rapporten en de eigen SFNL-rapporten (2024, 2025).
Werkwijze: volledig autonoom; Fable 5 als orchestrator, al het schrijf-,
test- en jurywerk door Opus-subagents.

## Het traject in het kort

1. **Onderzoek** (10 agents): zes onderzoekslenzen (Economist, McKinsey/Bain,
   narratieve journalistiek, AI-tells, Nederlandse schrijfleer,
   redactieprocessen), een gap-analyse van de bestaande skills, en een
   huisstem-analyse van de echte SFNL-rapporten met 14 specimen-passages.
   Kernconclusie gap-analyse: de bestaande skills werken uitsluitend
   aftrekkend (fouten verwijderen); het plafond is "concept min fouten" —
   correct maar dood. → `dossier/onderzoek/`
2. **Vijf concurrerende varianten**, elk met een eigen filosofie:
   redactiestraat, architect (Minto), vertaler (vers schrijven uit gesloten
   bron), proeflezer (meetlat + koude lezer), stem (specimen-imitatie).
   → `varianten/`
3. **Testronde 1**: 15 outputs (5 varianten × 3 testteksten), blind gejureerd
   door 9 juryleden (3 lenzen per tekst). Winnaars per onderdeel: architect
   (structuur), vertaler (proza en menselijkheid), proeflezer (consistentie).
   Niemand haalde de Turingpoort. → `dossier/analyse-ronde1.md`
4. **Synthese**: één gecombineerde skill (v1) met de vertaler als ruggengraat.
5. **Evolutielus**, vier iteraties met blinde vergelijkingsjury's:
   - **v1 → v2**: hedge-quarantaine, openlatings-dosering, slotregel,
     kop-regel, Turingpoort-criteria. Uitkomst: de criteria "oordeel dat iets
     kost" en "tegenslag krijgt gevolg" verleidden de schrijver tot verzonnen
     onderbouwing; de getallen-cap liet feiten vervallen. → r3
   - **v2 → v3**: oordeel-grondregel (ondertekend én gegrond), beweringen over
     bewijs/methode/mechanisme onder de feitencontrole, getalspreiding als
     richtlijn, anti-vingerafdruk. Uitkomst: T1 gewonnen (7,37, poortpass);
     maar de eigen middelen (schaalvertalingen, openlatingen) werden
     overtoegepast. → r4
   - **v3 → v3.1**: budgetten op alle eigen stijlmiddelen. Uitkomst r5: wint
     T2 bij de detective, evenaart de externe kampioen zonder diens
     verzinsels; lichte route bleef achter. → r5
   - **v3.1 → v3.2**: de lichte route terug naar de slanke vorm die de korte
     tekst in drie rondes won (wetten en budgetten, geen bouwsteigers).

## Eindstand per testtekst (beste gemeten score van de skill-familie)

| Tekst | Beste score | Versie | Turingpoort |
|---|---|---|---|
| T1 rapporthoofdstuk (674 w) | 7,37 gem.; 8,2 doellezer | v3 | **ja** (doellezer r4) |
| T2 bestuurlijke samenvatting (436 w) | 6,6 gem.; 1e bij detective | v3.1 | nee (V4 haalde hem eenmaal, maar met D7-plafond voor verzinsels) |
| T3 casetekst (305 w) | 8,2 gem.; 8,8 redactiejury | v1-vorm lichte route (in v3.2 hersteld) | **ja** (2× in r2, 1× in r4-r5) |

Over het hele traject haalden outputs van de skill-familie de Turingpoort
vijf keer bij drie verschillende juryrollen, zonder één diskwalificatie voor
de eindversies in r4/r5. Ter vergelijking: geen enkele ronde-1-output haalde
de poort, en de externe kampioenen die hem haalden deden dat steeds mét een
feitenplafond wegens verzonnen mechanismen.

## De vijf wetten die het traject opleverde

1. **Aftrekkend redigeren heeft een plafond.** Alleen patronen strippen
   levert "concept min fouten". Vers schrijven uit een gesloten bron is de
   enige route naar proza dat juryleden menselijk noemen.
2. **Elke aanwezigheidsregel zonder budget wordt een tic.** "Benoem wat de
   bron openlaat" werd een mal; "druk elk cijfer ergens tegenaan" werd een
   glossenregen; de klapzin verving het gedachtestreepje. Dosering is de
   helft van het ambacht.
3. **De menselijkste zinnen zijn de gevaarlijkste.** Vier van de vijf
   varianten verzonnen ergens causaliteit of bewijs — juist in hun beste
   zinnen. Daarom: elk oordeel ondertekend en gegrond; elke bewering over de
   wereld herleidbaar tot het dossier; bronmodaliteit reist mee.
4. **Feitentrouw en menselijkheid concurreren niet — mits gescheiden.** De
   winnende teksten combineren exacte feiten met een zichtbaar redacteursoog:
   "Wij vinden ... te veel geld" won vertrouwen; "de evaluatie concludeert
   ..." (niet door de bron gedekt) kostte het.
5. **Kort vraagt minder apparaat.** De volledige machinerie wint op lange,
   gestructureerde teksten; op korte teksten wint de slanke route.

## Bekende beperkingen

- **Rundvariatie.** Twee runs van dezelfde versie op dezelfde tekst kunnen
  een punt verschillen. Voor teksten die er echt toe doen: draai de skill
  twee keer en laat de koude lezer (of een redacteur) kiezen.
- **De strengste detective blijft moeilijk te passeren** op middellange
  bestuurlijke teksten; de poortpasses zitten bij doellezer en redactiejury.
- **Familie-vingerafdruk.** Outputs van dezelfde skill delen zinsmallen
  (de openlating, "Wie ... overneemt"). Binnen één document is dat nu
  gebudgetteerd; over documenten heen blijft het herkenbaar voor wie er
  meerdere naast elkaar legt.
- **Woord-echo** (één markant woord dat vaak terugkeert, zoals "betwist" 4×)
  wordt nog niet mechanisch geteld; de humanizer-regel over elegant variation
  dekt het deels.

## Gebruiksaanwijzing

De skill staat in `skill/SKILL.md` (naam: `sfnl-rapporttekst`). Installatie:
kopieer de map naar `~/.claude/skills/sfnl-rapporttekst/`. De skill begint
met één AskUserQuestion-moment (teksttype/lezer, de spanning als ruggengraat,
register, lengte) en heeft volledige defaults voor onbeheerd draaien. Het
ingebedde telscript draait via Bash; subagent-stappen (koude lezer) hebben
solo-fallbacks.

Testmateriaal en alle juryrapporten staan onder `test/`; de mappings van de
blinde rondes staan bewust niet in de repo.

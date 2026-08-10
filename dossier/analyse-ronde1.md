# Analyse testronde 1

Vijf skill-varianten, elk toegepast op drie testteksten door verse Opus-agents;
per tekst drie blinde juryleden (redactiejury, AI-detective, doellezer) met de
rubriek uit `test/rubriek.md`. Mapping stond tijdens het jureren niet in de repo.

## Eindcijfers (gemiddelde van drie juryleden per tekst)

| Variant | T1 rapport­hoofdstuk | T2 bestuurlijke samenvatting | T3 casetekst | Gemiddeld |
|---|---|---|---|---|
| V4 proeflezer | 7,67 | **7,57** | 5,93 | **7,06** |
| V3 vertaler | 7,40 | 5,43¹ | **7,33** | 6,72¹ |
| V2 architect | **7,77** | 5,77 | 6,60 | 6,71 |
| V1 redactiestraat | 7,13 | 5,63 | 5,90 | 6,22 |
| V5 stem | 4,30² | 4,80 | 7,13 | 5,41 |

¹ V3-T2 werd door twee juryleden gediskwalificeerd om een rekenkundig afgeleid
bedrag (€ 790.000, exact de som van bedragen uit de tekst). Zonder die plafonds
scoort V3 op T2 6,93 en overall 7,22 — dan is V3 de winnaar. De derde jury
(doellezer) zette dezelfde tekst juist op 1 met 8,3. Dit is een rubriekgat, geen
tekstgebrek; de kalibratie is voor T3 al rechtgezet en staat nu als addendum in
de rubriek.
² V5-T1 was een uitvoeringsfout: de agent kamde de bron door in plaats van te
herschrijven (labelbullets, drietallen en zoom-out-slot bleven staan). Op de
korte casetekst werd dezelfde filosofie tweede.

**Niemand haalde structureel de Turingpoort.** Eén jurylid liet één tekst
passeren (V4-T2, redactiejury); alle overige oordelen: onder de lat van
menselijk topwerk. De evolutielus is dus nodig, precies zoals gepland.

## Wat wint, per variant

- **V3 vertaler** schreef het beste Nederlands ("beste lead van het veld",
  hoogste menselijkheidsscores) en won vertrouwen door te benoemen wat de bron
  níét zegt ("Waarom de verzekeraar afhaakte, is niet bekend" / "Of het project
  daardoor iets heeft moeten laten, staat er niet bij"). Vers schrijven uit een
  gesloten bron werkt.
- **V2 architect** won waar structuur het zwaarst weegt (T1) met koppen die
  samen het betoog vertellen en cijfers die ergens tegenaan gedrukt worden
  (€ 640.000 ≈ het jaarbedrag).
- **V4 proeflezer** was de meest consistente presteerder op zakelijke teksten:
  de meetlat garandeert een bodem (ritme, tangen, partikels) en de koude lezer
  vangt scanpunten.
- **V1 redactiestraat** leverde degelijke middenmoot; de rolscheiding (aparte
  copy edit, aparte feitencontrole) is waardevol, maar redigeren-op-de-bron
  erft de bronstructuur: bij V1 en V5 overleefden brongebreken het vaakst.
- **V5 stem** bewees zich op de korte narratieve tekst (2e op T3) met de
  specimen-bewegingen, maar is onbetrouwbaar op lange gestructureerde stukken.

## De nieuwe tells die de jury vond (veldbreed)

Het gedachtestreepje is overal weg — maar de machine verschoof het nadruk-
mechanisme. Dit zijn de patronen die ronde 2 moet uitroeien:

1. **Klapzin-stapeling.** Korte verdictzinnen/epigrammen aan het eind van
   alinea's, drie tot zes per tekst. Eén per tekst is het maximum.
2. **Kop-raster.** Alle koppen in dezelfde mal (volzin, 14–16 woorden, elk een
   getal; of drie stellingkoppen op 260 woorden). Structuur als betoog: ja.
   Identieke kopvorm: nieuwe tell.
3. **Spiegelparen en negatieparallellen.** "Voor X stond € 1.850 klaar. Voor Y
   stond niets." Twee exacte spiegelparen in 545 woorden; drie secties die op
   dezelfde negatieparallel eindigen.
4. **Gelijke alinealengtes.** Vijf opeenvolgende alinea's van 58–64 woorden,
   elk eindigend op een klap.
5. **Zinsopening-herhaling.** Tweemaal "Wie ..." als opener in één tekst.
6. **Verzonnen causaliteit — de gevaarlijkste.** Oorzaakketens die de bron
   niet legt: "Meanders vertrek is rationeel [want de baten landden elders]",
   "De betaling volgde dat verschil", "Het project liep wel gewoon door",
   koppen die causaliteit claimen die de alinea niet levert. Vier van de vijf
   varianten deden dit ergens. De bron zwijgen laten waar hij zwijgt bleek
   juist de grootste vertrouwenswinst.
7. **Afgeleide getallen zonder regel.** Breuken op twee verschillende noemers
   ("een zesde van die schuld"), totalen die de samenstellende delen uit de
   tekst verdringen (172.000 in plaats van drie inwonertallen).
8. **Correct maar dood.** Technisch schone tekst zonder standpunt scoorde
   systematisch lager bij de doellezer: "hier kan ik geen besluit op nemen".
9. **De cijferalinea zonder zaak.** Op T3 greep het onderstreepplafond bij
   álle vijf op dezelfde plek: de alinea met de cijfers, die niemand tot een
   betoog maakt. Elk kerncijfer moet ergens tegenaan gedrukt worden.

## Besluit: architectuur van de gecombineerde skill

Ruggengraat = V3 (decompileren → bron sluiten → vers schrijven), want daar
zitten het beste proza en de hoogste menselijkheid. Daaromheen:

| Fase | Uit | Wat |
|---|---|---|
| 0 | invariant | Check-in met gebruiker (teksttype/lezer, spanning-kandidaten uit de tekst, register, lengte) + defaults |
| 1 | V3 + nieuw | Decompileren: feitenregister, claims met sterkte, spanning, gaten, én een **causaliteitskaart** (welke oorzaakverbanden legt de bron letterlijk) |
| 2 | V2 | Architectuur: hoofdboodschap, storyline met ongelijke gewichten, horizontale leestest; kopvormen bewust gevarieerd of géén koppen (korte tekst) |
| 3 | V3 + V5 | Vers schrijven met gesloten bron, per passage een specimen-beweging; menselijke wetten (standpunt, weglating, partikels, benoemen wat de bron niet zegt); elk kerncijfer tegen iets aangedrukt |
| 4 | V4 + nieuw | Meetronde: bestaande drempels + **anti-rastermetingen** (klapzin ≤ 1, kopvorm-variatie, alinealengte-spreiding, spiegelparen = 0, geen dubbele zinsopeners); rode meting → schrijfpas |
| 5 | V1 | Gescheiden controles: copy edit + hardop; feitencontrole heen en terug; **causaliteitscontrole** tegen de kaart uit fase 1; afgeleide-getallenregel (alleen als beide componenten in de tekst staan, nooit gemengde noemers, nooit een totaal dat de delen vervangt) |
| 6 | V4/V1 | Koude lezer (verse agent, solo-fallback gedefinieerd); faalt die → één gerichte terugronde naar fase 4 |
| 7 | invariant | Levering: plakklare tekst + logboek 8 regels |

Korte teksten (< ~350 woorden): fase 2 licht (geen dot-dash, wel gewichtskeuze)
en fase 4 in één meting.

Uitvoeringslessen: elke agent een eigen scratchpad-submap; alle fasen hebben
een solo-fallback; de laatste handeling op de tekst is altijd een schrijfpas.

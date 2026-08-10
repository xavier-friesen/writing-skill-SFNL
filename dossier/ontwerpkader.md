# Ontwerpkader: SFNL rapporttekst-skill

Doel: een skill die AI-gegenereerde concepttekst omzet in complete, publiceerbare
Nederlandse rapporttekst. De lat: niet van menselijk topwerk te onderscheiden,
en beter leesbaar dan de referentiestandaard (The Economist, NYT, Time,
McKinsey/Bain, en de eigen SFNL-rapporten 2020/2022/2025).

De hoofdklacht over de bestaande skills (sfnl-humanizer, sfnl-tekst-scherpen):
ze maken teksten vooral langer en "beter", maar het resultaat is nog geen
prachtig, doordacht, menselijk proza. De nieuwe skill moet dat gat dichten.

## Invarianten (gelden voor elke variant)

1. **Stijl-check-in vooraf.** De skill begint met één AskUserQuestion-moment:
   welk type output (rapporthoofdstuk, bestuurlijke samenvatting, casetekst,
   notitie), welke lezer, welk register, en gewenste lengte. Bij afwezigheid
   van de gebruiker: beredeneerde defaults op basis van de tekst zelf, gemeld
   in het logboek.
2. **Betekenisbehoud.** Feiten, cijfers, namen en claims blijven exact staan.
   Niets verzinnen: geen nieuw cijfer, voorbeeld, citaat of beeld dat niet in
   de bron of het gesprek zit.
3. **Lengtediscipline.** De output is korter dan de input (richtlijn: 15–35%
   korter voor betogende tekst). Nooit langer, tenzij de gebruiker expliciet om
   uitbreiding vraagt.
4. **Complete levering.** Output is de plakklare tekst zelf, plus een logboek
   van maximaal acht regels. Geen commentaar tussendoor, geen opties.
5. **Anti-AI-eindtoets.** Elke variant sluit af met een controle op bekende
   AI-patronen (humanizer-lijst + Opus-tics + modeltics).

## De vijf varianten

| # | Naam | Kern | Onderscheidend mechanisme |
|---|------|------|---------------------------|
| 1 | De redactiestraat | Tekst behouden, in vaste redactierondes verbeteren | Structural edit → line edit → copy edit → hardop-leesronde, strikt gescheiden |
| 2 | De architect | Redenering eerst, tekst volgt | Minto-piramide: hoofdboodschap, storyline, herbouw vanuit outline |
| 3 | De vertaler | Nooit repareren, altijd opnieuw schrijven | Decompileren naar feiten/claims/spanning; vers schrijven zonder de bronformulering te zien (anti-verankering) |
| 4 | De proeflezer | Meten is weten | Gesimuleerde doellezer rapporteert leeservaring; herschrijven tot de metingen slagen; convergentie op data |
| 5 | De stem | Imitatie van menselijk topwerk | Specimen-gedreven: per passage het patroon van een gepubliceerd voorbeeld volgen; ritme-engineering; standpunt en asymmetrie durven kiezen |

Varianten delen de invarianten maar mogen elkaar verder niet kopiëren: het
doel van ronde 1 is te leren welk mechanisme het meeste kwaliteit oplevert.

## Testprotocol

- Vast corpus van drie AI-bot-achtige invoerteksten (rapporthoofdstuk,
  bestuurlijke samenvatting, casetekst) met een vaste feitenlijst per tekst.
- Elke variant wordt door een verse Opus-agent toegepast (agent krijgt alleen
  de skilltekst + invoertekst; geen kennis van andere varianten).
- Blinde jury per invoertekst: meerdere Opus-juryleden met verschillende
  lenzen scoren op de rubriek (test/rubriek.md), citeren bewijs, en ranken.
- Disqualificatieregel: verdraaide of verzonnen feiten = maximaal een 4.
- Na ronde 1: synthese van winnende elementen → gecombineerde skill →
  evolutielus (toepassen, adversarieel jureren, verbeteren) tot de jury de
  output niet van menselijk werk kan onderscheiden én boven de benchmark legt.

## Rollen

- Orchestrator: Fable 5 (deze sessie) — ontwerpt, verdeelt, synthetiseert.
- Al het schrijf-, test- en jurywerk: Opus-subagents.

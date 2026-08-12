#!/usr/bin/env python3
"""Telscript voor sfnl-rapporttekst v5.0 — zes metingen, geen oordelen.

    python3 meetlat.py tekst.md        (tekst zonder logboek)

Elke meting komt uit iets wat een jury daadwerkelijk afstrafte.

ROOD is hard: figuren, spreker, cijfers en woorden. Die leidt tot een schrijfpas op
de passage, niet tot een reparatie van de zin.

LET is richtinggevend: pointe en ritme. Die wijzen een passage aan om naar te kijken,
en je laat ze liever staan dan dat je een figuur toevoegt of een zin beschadigt om
de teller te halen. Ritme is iets wat je hoort, niet iets wat je haalt.

Botsen pointe en figuren, dan zet je de korte zin niet aan het einde van de alinea:
een korte slotzin is een klapzin, een korte zin in het midden is een pointe.
"""
import re
import sys
import statistics as st
from collections import Counter

T = open(sys.argv[1], encoding='utf-8').read()
B = re.sub(r'^#{1,6}.*$', '', T, flags=re.M)
B = re.sub(r'^\s*[-*]\s+', '', B, flags=re.M).replace('**', '')
KOP = re.findall(r'^#{1,6}\s*(.+)$', T, flags=re.M)
ALI = [x for x in re.split(r'\n\s*\n', B) if x.strip()]
w = lambda s: [x for x in s.split() if re.search(r'[\wÀ-ÿ]', x)]
zin = lambda t: [z.strip() for z in re.split(r'(?<=[.!?])\s+(?=[«"\'(A-ZÀ-Þ0-9])', re.sub(r'\s+', ' ', t)) if len(z.strip()) > 1]
Z, low = zin(B), B.lower()
L = [len(w(z)) for z in Z]
N = sum(L)
p = lambda ok, k, v: print(f"{'OK  ' if ok else 'ROOD'} {k:<10} {v}")
g = lambda ok, k, v: print(f"{'OK  ' if ok else 'LET '} {k:<10} {v}")
print(f"--- {N} woorden, {len(Z)} zinnen, {len(ALI)} alinea's, {len(KOP)} koppen")

# 1. pointe -- elke alinea van 4+ zinnen heeft een zin onder de tien woorden.
kaal = [f"alinea {i+1} (kortste {min(za)}w)" for i, a in enumerate(ALI)
        for za in [[len(w(z)) for z in zin(a)]] if len(za) >= 4 and min(za) >= 10]
g(not kaal, "pointe", (f"{kaal[:3]} — zet de korte zin niet aan het alinea-eind"
                       if kaal else "elke lange alinea heeft een zin <10w"))

# 2. figuren -- negatieparallel <=1, klapzin <=2, schaalvertaling <=2.
NEGP = re.compile(r'\b(?:niet|geen|nooit|nergens)\b[^.!?]{2,70}?\bmaar\b|\bniet zozeer\b|\bin plaats van\b'
                  r'|\bwel\b[^.!?]{2,60}?\b(?:niet|geen|nooit)\b|\b(?:niet|geen)\b[^.!?]{2,60}?\bwel\b'
                  r'|\b(?:zwaarder|lichter|belangrijker|sterker|eerder|liever)\s+(?:\w+\s+){0,4}?dan\b', re.I)
NEG = re.compile(r'\b(geen|niets|niet|nul|nergens|evenmin)\b', re.I)
neg = [f"zin {i+1}: {z[:46]}" for i, z in enumerate(Z) if NEGP.search(z)]
# Een spiegelpaar: twee opeenvolgende zinnen met dezelfde ingang waarvan er één
# ontkent. De valse positieven zaten in lange feitendichte zinnen die toevallig
# met hetzelfde lidwoord beginnen, dus die sluit ik uit -- maar niet meer dan dat.
# (In v5.1 stond deze eis te streng en zag een jury drie spiegelparen die het
# script groen liet. Een meting versoepel je niet op gezag van wie eraan
# gehouden wordt.)
for i in range(len(Z) - 1):
    a, b = w(Z[i]), w(Z[i + 1])
    if not (a and b) or bool(NEG.search(Z[i])) == bool(NEG.search(Z[i + 1])):
        continue
    if a[0].lower() != b[0].lower():
        continue
    if len(a) > 18 and len(b) > 18:      # twee lange zinnen: toeval, geen figuur
        continue
    neg.append(f"spiegelpaar zin {i+1}/{i+2}")
klap = [z for z in (zin(a)[-1] for a in ALI if zin(a)) if len(w(z)) <= 8]
BR = (r'(?:helft|derde|kwart|vijfde|zesde|zevende|achtste|negende|tiende|dubbele|drievoud\w*'
      r'|viervoud\w*|verdubbel\w*|verdrievoudig\w*|verviervoudig\w*)')
SCH = [re.compile(r'\b(?:ruim|bijna|net geen|nog geen|goed|krap|iets (?:meer|minder) dan|meer dan|minder dan|een|het)\s+(?:een |de |het )?' + BR + r'\b', re.I),
       re.compile(r'\b(?:dat|dit)\s+(?:is|was|komt|kwam|betekent|scheelt|maakt)\b[^.!?]{0,30}?(?:' + BR + r'|\d)', re.I),
       re.compile(r'\b(?:\d+|een|twee|drie|vier|vijf|zes|zeven|acht|negen|tien)\s+procentpunt(?:en)?\b', re.I),
       re.compile(r'\bper\s+\w+(?:\s+\w+)?\s+(?:was|is|komt|kwam)\s+dat\b|\bkomt\s+dat\s+neer\s+op\b', re.I)]
sch = [Z[i][:40] for i, z in enumerate(Z) if any(r.search(z) for r in SCH)]
p(len(neg) <= 1 and len(klap) <= 2 and len(sch) <= 2, "figuren",
  f"negatieparallel {len(neg)} (<=1) {neg[:2]}; klapzin {len(klap)} (<=2); schaal {len(sch)} (<=2) {sch[:2]}")

# 3. spreker -- directe rede of een personage dat vraagt, wil of vindt.
SPREEK = re.compile(r'\b(?:vraagt|vroeg|zegt|zei|stelt|wil weten|vreest|verzucht|antwoordt|reageert)\b\s*[:,]?\s*["“„‘]'
                    r'|["“„]\s*[^"”“]{15,}?\s*["”]\s*,?\s*(?:vraagt|zegt|stelt|aldus)\b'
                    r'|\b(?:een|de)\s+\w*(?:manager|houder|bestuurder|directeur|ambtenaar|wethouder|financier)\s+\w*\s*(?:vraagt|wil|vindt|vreest|zegt)\b', re.I)
spr = [f"zin {i+1}: {z[:52]}" for i, z in enumerate(Z) if SPREEK.search(z)]
p(not spr, "spreker", spr[:3] or "geen directe rede, geen sprekend personage")

# 4. cijfers -- twee waarden binnen 1% zijn meestal dezelfde grootheid, twee keer
#    verschillend opgeschreven. Jaartallen uitgezonderd.
def num(s):
    s = s.rstrip('.,')
    try:
        return float(s.replace('.', '').replace(',', '.')) if ',' in s else float(s.replace('.', ''))
    except ValueError:
        return None


alle = [v for v in (num(x) for x in re.findall(r'\b\d[\d.,]*\b', B)) if v]
jaar = lambda v: v == int(v) and 1900 <= v <= 2100
vals = sorted({v for v in alle if v > 1 and not jaar(v)})
near = [f"{a:g} naast {b:g}" for a, b in zip(vals, vals[1:]) if b / a < 1.01]
herh = [f"{k}x {v:g}" for v, k in Counter(alle).items() if k > 1]
p(not near, "cijfers", (near[:3] if near else f"geen bijna-dubbele; 2x+: {herh[:5] or 'geen'}"))

# 5. ritme -- spreiding, niet gemiddelde. Metronomisch proza is het oudste signaal.
sd = st.pstdev(L) if len(L) > 1 else 0
gem = N / max(len(L), 1)
drie = [f"zin {i+1}: {L[i:i+3]}" for i in range(len(L) - 2) if max(L[i:i+3]) - min(L[i:i+3]) <= 2]
g(sd >= 7 and 13 <= gem <= 21 and not drie, "ritme",
  f"SD {sd:.1f} (>=7), gem {gem:.1f} (13-21), langste {max(L) if L else 0}" + (f", gelijk trio {drie[:2]}" if drie else ""))

# 6. woorden -- de verbodenlijst, en het frequentieplafond op de eigen formules.
VERB = ("cruciaal essentieel faciliteren navigeren landschap robuust naadloos toekomstbestendig holistisch "
        "integraal integrale ontzorgen impactvol adresseren meerwaarde handelingsperspectief stakeholder "
        "ecosysteem middels derhalve inzake alsmede bewerkstelligen problematiek randvoorwaardelijk").split()
UITDR = ["in het kader van", "met betrekking tot", "ten aanzien van", "ten behoeve van", "met behulp van",
         "in verband met", "op het gebied van", "in het licht van", "het is zinvol", "in dit hoofdstuk",
         "hieronder", "kortom", "al met al", "tot slot"]
vh = [x for x in VERB if re.search(r'\b' + x + r'\b', low)] + [u for u in UITDR if u in low]
FORM = ["laat zien dat", "laten zien dat", "toont aan dat", "zo ontstaat", "structureel", "structurele",
        "duurzaam", "duurzame", "verankering", "borgen", "borging", "in kaart brengen", "verkennen hoe"]
ff = {x: n for x in FORM for n in [len(re.findall(r'\b' + re.escape(x) + r'\b', low))] if n}
tel = {"em-streepje": len(re.findall(r'[—–]', B)), "vet": len(re.findall(r'\*\*', T)) // 2,
       "drieslag": len(re.findall(r'\b\w+, \w+ en \w+\b', B))}
p(not vh and sum(ff.values()) <= max(1, round(N / 500)) and tel["em-streepje"] == 0 and tel["vet"] == 0
  and tel["drieslag"] <= 1, "woorden", f"verboden {vh or 'geen'}; formules {sum(ff.values())} (<= {max(1, round(N/500))}) {ff or ''}; {tel}")

# 7. rangorde -- elke vergelijkende of overtreffende trap is een bewering over alle
#    alternatieven. Het script kan hem niet narekenen, alleen aanwijzen: doe dat zelf,
#    tegen elk ander getal in dezelfde eenheid. Zo zakte in ronde 7 een hele tekst.
RANG = re.compile(r'\b(?:grootste|kleinste|hoogste|laagste|zwaarste|belangrijkste|meeste|minste|sterkste'
                  r'|beste|slechtste|snelste|duurste|goedkoopste|enige|eerste)\b'
                  r'|\b(?:vooral|met name|juist)\b|\b\w+er\s+dan\b', re.I)
rang = [f"zin {i+1}: {z[:56]}" for i, z in enumerate(Z) if RANG.search(z)]
g(not rang, "rangorde", (f"{len(rang)}x — reken elk na tegen de andere getallen: {rang[:3]}"
                         if rang else "geen vergelijkende of overtreffende trap"))

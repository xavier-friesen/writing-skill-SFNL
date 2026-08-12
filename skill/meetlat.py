#!/usr/bin/env python3
"""Meetlat voor sfnl-rapporttekst v3.3.

    python3 meetlat.py tekst.md        (tekst zonder logboek)

Het v3.2-script, ongewijzigd, plus drie metingen die het corpus zelf faalt:
P1 (pointe), N1 (getalconsistentie) en RG (rangorde).
"""
import re, sys, statistics as st
from collections import Counter
T = open(sys.argv[1], encoding='utf-8').read()
KOP = re.findall(r'^#{1,6}\s*(.+)$', T, flags=re.M)
SEC = [s for s in re.split(r'^#{1,6}.*$', T, flags=re.M) if s.strip()]
B = re.sub(r'^#{1,6}.*$', '', T, flags=re.M)
B = re.sub(r'^\s*[-*]\s+', '', B, flags=re.M).replace('**', '')
ALI = [x for x in re.split(r'\n\s*\n', B) if x.strip()]
w = lambda s: [x for x in s.split() if re.search(r'[\wÀ-ÿ]', x)]
tk = lambda s: re.findall(r'[\wÀ-ÿ]+', s.lower())
def zin(t):
    t = re.sub(r'\s+', ' ', t)
    return [z.strip() for z in re.split(r'(?<=[.!?])\s+(?=[«"\'(A-ZÀ-Þ0-9])', t) if len(z.strip()) > 1]
Z = zin(B); L = [len(w(z)) for z in Z]; N = sum(L); low = B.lower()
p = lambda ok, k, v: print(f"{'OK  ' if ok else 'ROOD'} {k:<22} {v}")
g = lambda ok, k, v: print(f"{'OK  ' if ok else 'LET '} {k:<22} {v}")   # richtlijn, geen cap
print(f"--- {N} woorden, {len(Z)} zinnen, {len(ALI)} alinea's, {len(KOP)} koppen")
sd = st.pstdev(L) if len(L) > 1 else 0; gem = N / max(len(L), 1)
p(sd >= 7 and sd/max(gem, 1) >= .45, "R1 spreiding", f"SD {sd:.1f} (>=7,0), burst {sd/max(gem,1):.2f} (>=0,45)")
p(13 <= gem <= 19, "R4 gem. zinslengte", f"{gem:.1f} (13-19)")
vs = [(i, max(L[i:i+10])-min(L[i:i+10]), min(L[i:i+10])) for i in range(max(len(L)-9, 1))]
bad = [f"venster {i+1}: bereik {b}, kortste {m}" for i, b, m in vs if b < 25 or m > 8]
p(not bad, "R2 venster van 10", bad[:2] or "bereik >=25, kortste <=8")
dr = [f"zin {i+1}: {L[i:i+3]}" for i in range(len(L)-2) if max(L[i:i+3])-min(L[i:i+3]) <= 2]
p(not dr, "R3 drie zinnen gelijk", dr[:2] or "geen")
p(bool(L) and max(L) >= 30, "R5 langste zin", f"{max(L) if L else 0} (>=30, voorleesbaar)")
klap = [z for z in (zin(a)[-1] for a in ALI if zin(a)) if len(w(z)) <= 8]; lev = {}
p(len(klap) <= 2, "X1 kort slotoordeel", f"{len(klap)} (<=2, alineafinaal <=8w) {klap[:3]}")
for m in re.finditer(r'^(#{1,6})\s*(.+)$', T, flags=re.M): lev.setdefault(len(m.group(1)), []).append(m.group(2))
grp = max(lev.values(), key=len) if lev else []          # koppen op hetzelfde niveau
kl = [len(w(k)) for k in grp] or [0]; cij = sum(1 for k in grp if re.search(r'\d', k))
p(len(grp) < 3 or (max(kl)-min(kl) >= 4 and cij < len(grp)), "X2 kopvorm-variatie", f"lengtes {kl}, met getal {cij}/{len(grp)}")
al = [len(w(a)) for a in ALI]; trio = [i+1 for i in range(len(al)-2) if max(al[i:i+3]) <= 1.1*min(al[i:i+3])]
p(not trio, "X3 alinealengte", f"{al}" + (f"; gelijk trio vanaf alinea {trio}" if trio else ""))
NEG = re.compile(r'\b(geen|niets|niet|nul|nergens|evenmin)\b', re.I)
NEGP = re.compile(r'\b(?:niet|geen|nooit|nergens)\b[^.!?]{2,70}?\bmaar\b|\bniet zozeer\b|\bin plaats van\b'
                  r'|\b(?:zwaarder|lichter|belangrijker|sterker|eerder|liever)\s+(?:\w+\s+){0,4}?dan\b', re.I)
sp = [f"spiegelpaar zin {i+1}/{i+2}" for i in range(len(Z)-1)
      if w(Z[i]) and w(Z[i+1]) and w(Z[i])[0].lower() == w(Z[i+1])[0].lower()
      and bool(NEG.search(Z[i])) != bool(NEG.search(Z[i+1]))]
npar = [f"zin {i+1}: {z[:44]}" for i, z in enumerate(Z) if NEGP.search(z)]
p(len(sp)+len(npar) <= 1, "X4 negatieparallel", f"{len(sp)+len(npar)} (<=1) {(npar+sp)[:2] or 'geen'}")
OPEN = re.compile(r"(?:is|zijn|blijft|blijven)\s+niet\s+(?:bekend|vastgesteld|onderzocht|uitgezocht|gemeten|te achterhalen|hard te maken)"
                  r"|staat\s+(?:er\s+)?niet(?:\s+bij)?|staat\s+(?:er\s+)?nergens|(?:blijft|is)\s+onduidelijk|blijft\s+onbeantwoord"
                  r"|niet\s+(?:met zekerheid\s+)?(?:vast te stellen|hard te maken)|(?:meldt|vermeldt|zegt|noemt)\s+(?:\w+\s+){0,3}?niets?\b", re.I)
SLOTZ = zin(ALI[-1]) if ALI else []
hits = [(z, m.group(0)) for z in Z for m in OPEN.finditer(z)]
slot = sum(1 for h in hits if h[0] in SLOTZ)
p(len(hits) <= 1 and not slot, "X6 openlating", f"{len(hits)} (<=1), in slotalinea {slot}, {[h[1] for h in hits[:3]]}")
GET = re.compile(r'\b\d[\d.,]*\b')
ga = [len(GET.findall(a)) for a in ALI]; gz = [(i+1, len(GET.findall(z))) for i, z in enumerate(Z) if len(GET.findall(z)) >= 4]
g(max(ga, default=0) <= 3 and not gz, "X7 getalspreiding", f"per alinea {ga} (<=3); zin met >=4 getallen: {gz[:3] or 'geen'}")
dump = [i+1 for i, a in enumerate(ALI) if len(w(a)) >= 90 and len(GET.findall(a)) >= 5]
g(not dump, "X8 gegevensdump", f"alinea's van 90+ woorden met 5+ getallen: {dump or 'geen'}")
SJAB = ["waarom de verzekeraar afhaakte", "meldt het projectdossier niet", "rekent die kosten nergens toe", "berust op één meting", "één indicator bepaalde", "wie dit overneemt", "diezelfde regionale markt"]
sj = [s for s in SJAB if s in low]; p(not sj, "X9 skill-formules", sj or "geen voorbeeldzin van de skill")
BR = r'(?:helft|derde|kwart|vijfde|zesde|zevende|achtste|negende|tiende|dubbele|drievoud\w*|viervoud\w*|verdubbeling|verdrievoudiging|verviervoudiging)'
SCH = [re.compile(r'\b(?:ruim|bijna|net geen|nog geen|goed|krap|iets (?:meer|minder) dan|meer dan|minder dan|een|het)\s+(?:een |de |het )?' + BR + r'\b', re.I),
       re.compile(r'\b(?:dat|dit)\s+(?:is|was|komt|kwam|betekent|scheelt|maakt)\b[^.!?]{0,30}?(?:' + BR + r'|\d)', re.I),
       re.compile(r'\b(?:\d+|een|twee|drie|vier|vijf|zes|zeven|acht|negen|tien|elf|twaalf)\s+procentpunt(?:en)?\b', re.I),
       re.compile(r'\bper\s+\w+(?:\s+\w+)?\s+(?:was|is|komt|kwam)\s+dat\b|\bkomt\s+dat\s+neer\s+op\b', re.I)]
sc = [i for i, z in enumerate(Z) if any(r.search(z) for r in SCH)]          # één telling per zin
p(len(sc) <= 2, "X10 schaalvertaling", f"{len(sc)} (<=2) {[Z[i][:44] for i in sc[:4]]}")
bt = ' ' + ' '.join(tk(B)) + ' '; ech = []
for k in KOP:
    kt = tk(k)
    for n in range(len(kt), 4, -1):
        h = next((kt[i:i+n] for i in range(len(kt)-n+1) if f' {" ".join(kt[i:i+n])} ' in bt), None)
        if h: ech.append(f'"{" ".join(h)}" ({n} woorden)'); break
p(not ech, "X11 kop-echo", ech[:2] or "geen reeks van 5+ woorden uit een kop")
CON = {"wie", "wat", "waar", "juist", "niet", "wanneer", "zo", "daarmee", "hoewel", "terwijl", "pas", "ook"}
dub = [f"'{k}' {v}x" for k, v in Counter(w(z)[0].lower() for z in Z if w(z)).items() if k in CON and v > 1]
dub += [f"'{k}' {v}x" for k, v in Counter(' '.join(w(z)[:2]).lower() for z in Z if len(w(z)) > 1).items() if v > 2]
p(not dub, "X5 zinsopeners", dub[:3] or "geen constructie 2x, geen bigram >2x")
STOP = {"ding", "dingen", "koning", "ring", "woning", "kring", "overheid", "gezondheid", "moment", "momenten"}
nom = [x for x in re.findall(r"\b\w{4,}(?:ingen|ing|aties|atie|iteit|heden|heid|menten|ment)\b", low) if x not in STOP]
p(len(nom) <= len(Z)/2, "Z3 nominalisaties", f"{len(nom)/max(len(Z),1):.2f}/zin (<=0,50) {Counter(nom).most_common(5)}")
VERB = "cruciaal essentieel faciliteren navigeren landschap robuust naadloos toekomstbestendig holistisch integraal integrale borgen borging ontzorgen impactvol adresseren meerwaarde handelingsperspectief stakeholder ecosysteem middels derhalve inzake alsmede bewerkstelligen problematiek aanknopingspunten aandachtspunten".split()
UITDR = ["in het kader van", "met betrekking tot", "ten aanzien van", "ten behoeve van", "met behulp van", "in verband met", "op het gebied van", "in het licht van"]
vh = [x for x in VERB if re.search(r'\b'+x+r'\b', low)] + [u for u in UITDR if u in low]; p(not vh, "V1 verboden woorden", vh or "geen")
HED = ["mogelijk", "wellicht", "enigszins", "vermoedelijk", "naar verwachting", "vrijwel", "doorgaans", "veelal", "over het algemeen", "in beginsel", "in principe", "zou kunnen", "vooralsnog", "nagenoeg", "relatief", "in belangrijke mate"]
hh = sum(len(re.findall(h, low)) for h in HED); p(hh*100/max(N, 1) <= 3, "V4 hedgedichtheid", f"{hh} = {hh*100/max(N,1):.1f}/100w (<=3)")
tel = {"em-streepje": len(re.findall(r'[—–]', B)), "drieslag": len(re.findall(r'\b\w+, \w+ en \w+\b', B)),
       "niet-alleen-maar": len(re.findall(r'niet alleen|niet zozeer|het gaat niet om', low)),
       "meta": len(re.findall(r'in dit hoofdstuk|in deze paragraaf|hieronder|samengevat|kortom|al met al|tot slot', low)),
       "vet": len(re.findall(r'\*\*', T))//2, "oxford": len(re.findall(r'\w+,\s+\w+,\s+(?:en|of)\s', B))}
p(all(v == 0 for k, v in tel.items() if k != "drieslag") and tel["drieslag"] <= 1, "V2/V3/V5 tells", tel)
PART = ["toch", "wel", "nu eenmaal", "immers", "juist", "althans", "overigens", "weliswaar", "zelfs", "maar liefst"]
pa = sum(len(re.findall(r'\b'+re.escape(x)+r'\b', low)) for x in PART); p(pa >= N/150, "A6 modale partikels", f"{pa} (>= {N/150:.1f}; nul = doodgepoetst)")
CONN = ["maar", "toch", "immers", "namelijk", "weliswaar", "althans", "overigens", "juist", "daarom", "doordat", "terwijl", "hoewel", "zodat", "dus", "want", "omdat", "tenzij", "vandaar", "echter", "bovendien", "daarnaast", "tevens"]
cc = {k: v for k, v in ((x, len(re.findall(r'\b'+re.escape(x)+r'\b', low))) for x in CONN) if v}
p(len(cc) >= 6*N/800 and max(cc.values(), default=9) <= 3, "A7 connectieven", f"{len(cc)} soorten, max {max(cc.values(), default=0)}x")
sl = sorted(len(w(s)) for s in SEC if len(w(s)) > 20); med = st.median(sl) if sl else 1
p(len(sl) < 3 or sl[-1] >= 1.8*med, "A8 dragende sectie", f"{sl}, langste/mediaan {sl[-1]/med:.1f}x (>=1,8)" if sl else "n.v.t.")

# --- v3.3: drie metingen erbij ----------------------------------------------

# P1 pointe -- elke alinea van 4+ zinnen heeft een zin onder de tien woorden, en
# die draagt de pointe. Het slot van hoofdstuk 4 in het rapport 2025 meet
# 23-25-35 en zakt weg. Zet de korte zin niet aan het alinea-eind: daar is het
# een klapzin (X1) en in het midden een pointe.
kaal = []
for _i, _a in enumerate(ALI):
    _za = [len(w(_z)) for _z in zin(_a)]
    if len(_za) >= 4 and min(_za) >= 10:
        kaal.append(f"alinea {_i+1} (kortste {min(_za)}w)")
g(not kaal, "P1 pointe", (f"{kaal[:3]} - korte zin niet aan het alinea-eind"
                          if kaal else "elke lange alinea heeft een zin <10w"))


# N1 getalconsistentie -- twee waarden binnen 1% zijn meestal dezelfde grootheid,
# twee keer verschillend opgeschreven (zorguitgaven 113,5 naast 113,4).
def _num(x):
    x = x.rstrip('.,')
    try:
        return float(x.replace('.', '').replace(',', '.')) if ',' in x else float(x.replace('.', ''))
    except ValueError:
        return None


_alle = [v for v in (_num(x) for x in re.findall(r'\b\d[\d.,]*\b', B)) if v]
_vals = sorted({v for v in _alle if v > 1 and not (v == int(v) and 1900 <= v <= 2100)})
_near = [f"{a:g} naast {b:g}" for a, b in zip(_vals, _vals[1:]) if b / a < 1.01]
_herh = [f"{k}x {v:g}" for v, k in Counter(_alle).items() if k > 1]
p(not _near, "N1 getalconsistentie", _near[:3] or "geen twee waarden binnen 1%")
print(f"     {'getallen 2x+':<22} {_herh[:6] or 'geen'}  (controleer elk tegen de bron)")

# RG rangorde -- elke vergelijkende of overtreffende trap is een bewering over
# alle alternatieven. Het script wijst ze aan; jij rekent ze na tegen de andere
# getallen in dezelfde eenheid. Zo zakte in ronde 7b een hele tekst: "de grootste
# daling" was 19 procent, terwijl een ander cijfer in dezelfde tekst 35 was.
RANG = re.compile(r'\b(?:grootste|kleinste|hoogste|laagste|zwaarste|belangrijkste|meeste|minste'
                  r'|sterkste|beste|slechtste|snelste|duurste|goedkoopste|enige)\b'
                  r'|\b(?:vooral|met name)\b|\b\w+er\s+dan\b', re.I)
_rang = [f"zin {_i+1}: {_z[:52]}" for _i, _z in enumerate(Z) if RANG.search(_z)]
g(not _rang, "RG rangorde", (f"{len(_rang)}x - reken elk na: {_rang[:3]}"
                             if _rang else "geen vergelijkende of overtreffende trap"))

#!/bin/sh
# Haalt uit een outputbestand de kale tekst voor een blinde set.
#
#   sh test/strip.sh test/rondes/r4/S3-T1.md > blind/T1/A.md
#
# Weg: het logboek (vanaf `## Logboek` of een losse `---`), en de steigerkoppen
# die de oudere rondes bovenaan het bestand zetten (`# S3-T1`, `## Tekst`).
# Die laatste kostten in ronde 6 en 7 de v3.2-outputs punten bij de
# AI-detectietoets, omdat een jury ze als opmaaklawaai leest. Elke blinde set
# gaat door dit script, nooit door een awk-regel ter plekke.
awk '
  /^## Logboek/ { exit }
  /^---[[:space:]]*$/ { exit }
  # steigerkoppen: alleen zolang er nog geen echte tekst is gezien
  !seen && /^#[[:space:]]*S[0-9]+-T[0-9]+[[:space:]]*$/ { next }
  !seen && /^##[[:space:]]*(Tekst|Output|Resultaat)[[:space:]]*$/ { next }
  /[^[:space:]]/ && !/^#/ { seen = 1 }
  { print }
' "$1" | awk 'BEGIN{blank=1} /[^[:space:]]/{blank=0} !blank{print}'

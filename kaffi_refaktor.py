import json
from datetime import datetime

data = open("coffee.tsv", "r", encoding="utf8").read().split("\n")

struktur = {}
steder = {}

for row in data:
    tid, sted = row.split("\t")
    tid = tid.strip()
    sted = sted.strip().lower()
    try:
        dato = tid.split(" at ")[0]
        tidspunkt = tid.split(" at ")[1]
        dato = datetime.strptime(tid, '%B %d, %Y at %H:%M%p')
    except:
        continue

    må = f"{dato.year}-{dato.month:02}"

    struktur.setdefault(må, {"total": 0})
    struktur[må]["total"] += 1

    struktur[må].setdefault(sted, 0)
    struktur[må][sted] += 1

    steder.setdefault(sted, 0)
    steder[sted] += 1


struktur = sorted(struktur.items(), key = lambda x: x[1]["total"], reverse=True)
open("permåned.json", "w", encoding="utf8").write(json.dumps(struktur, indent=4))

steder = sorted(steder.items(), key = lambda x: x[1], reverse=True)
open("persted.json", "w", encoding="utf8").write(json.dumps(steder, indent=4))
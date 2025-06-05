mundo={
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Peru": "Lima"
}

invertido={}

for k, v in mundo.items():
    invertido[v]=k
print(mundo)
print(invertido)

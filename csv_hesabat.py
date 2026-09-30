import csv 
import tabulate
cedvel = [] 
cemi = 0 
with open("satislar.csv", "r", encoding="utf-8", newline="") as f:
    oxuyucu = csv.reader(f)
    basliq = next(oxuyucu)
    for setir in oxuyucu:
        ad = setir[0]
        qiymet = float(setir[1])
        say = int(setir[2])
        mebleg = qiymet * say
        cemi += mebleg
        cedvel.append([ad, qiymet, say, mebleg])
print(tabulate.tabulate(cedvel, headers=["mehsul", "qiymet", "say", "mebleg"]))
print(f"Cəmi: {cemi:.2f} AZN")

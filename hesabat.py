import tabulate
satislar = [
    ["Çay", 3.50, 10],
    ["Qəhvə", 6.00, 4],
    ["Şirə", 2.25, 8],
    ["Su", 0.80, 25],
]
print(tabulate.tabulate(satislar, headers=["mehsul", "qiymet", "say"]))
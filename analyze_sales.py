import csv

def ucitaj_podatke(fajl):
    with open(fajl, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def analiziraj_prodaju(podaci):
    ukupno = sum(float(red["ukupno"]) for red in podaci)
    prosek = ukupno / len(podaci)
    return ukupno, prosek

if __name__ == "__main__":
    podaci = ucitaj_podatke("sales.csv")
    ukupno, prosek = analiziraj_prodaju(podaci)
    print(f"Ukupan promet: {ukupno:.2f} RSD")
    print(f"Prosečna vrednost porudžbine: {prosek:.2f} RSD")

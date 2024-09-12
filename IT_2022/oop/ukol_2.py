import datetime

class Kniha:
    def __init__(self, nazev, autor, rok_vydani):
        self.nazev = nazev
        self.autor = autor
        self.rok_vydani = rok_vydani
    
    def info(self):
        return f"{self.nazev} ({self.rok_vydani}), {self.autor}"
    
    def stari(self):
        aktualni_rok = datetime.datetime.now().year
        return aktualni_rok - self.rok_vydani
    
# K1 = Kniha("Harry Potter", "J.K. Rowling", 1997)
# print(K1.info())
# print(K1.stari())

class Knihovna:
    def __init__(self, seznam_knih=[]):
        self.seznam_knih = seznam_knih

    def pridej_knihu(self, kniha):
        self.seznam_knih.append(kniha)
    
    def vypis_knihy(self):
        for kniha in self.seznam_knih:
            print(kniha.info())

    def vyhledej_knihu(self, nazev):
        for kniha in self.seznam_knih:
            if kniha.nazev == nazev:
                return kniha.info()
        return "Kniha nenalezena"
class Auto:
    SERVIS_KM = 20_000

    def __init__(self, znacka, model, rok_vyroby, pocet_kilometru=0):
        self.znacka = znacka
        self.model = model
        self.rok_vyroby = rok_vyroby
        self.pocet_kilometru = pocet_kilometru
        self.posledni_servis = pocet_kilometru

    def info(self):
        return f"{self.znacka} {self.model} z roku {self.rok_vyroby}"

    def jezdit(self, pocet_kilometru):
        self.pocet_kilometru += pocet_kilometru

    def servis(self):
        if self.pocet_kilometru - self.posledni_servis >= Auto.SERVIS_KM:
            self.posledni_servis = self.pocet_kilometru
            return "Servis proveden"
        else:
            return "Servis nebyl potřeba"

a1 = Auto("Peugeot", "406", 2005, 100_000)

print(a1.info())
print(a1.pocet_kilometru)
a1.jezdit(20_000)
print(a1.servis())
print(a1.pocet_kilometru)
print(a1.servis())

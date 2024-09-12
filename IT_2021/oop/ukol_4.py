class Zvire:
    def __init__(self, jmeno, druh, vek):
        self.jmeno = jmeno
        self.druh = druh
        self.vek = vek

    def zvuk(self):
        return "Řvu!"
    
class Pes(Zvire):
    def __init__(self, jmeno, vek, rasa):
        super().__init__(jmeno, "pes", vek)
        self.rasa = rasa

    def zvuk(self):
        return "Haf!"

class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva):
        super().__init__(jmeno, "kočka", vek)
        self.barva = barva

    def zvuk(self):
        return "Mňau!"
    
class Slon(Zvire):
    def __init__(self, jmeno, vek, velikost):
        super().__init__(jmeno, "slon", vek)
        self.velikost = velikost

    def zvuk(self):
        return "Tutu!"
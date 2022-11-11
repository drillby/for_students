class Ctverec:
    def __init__(self, staran_a, strana_b):
        self.a = staran_a
        self.b = strana_b

    def get_obsah(self):
        return self.a*self.b

class Obdelnik(Ctverec):
    ...
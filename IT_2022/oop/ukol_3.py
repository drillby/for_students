class BankovniUcet:
    def __init__(self, majitel, zustatek=0):
        self.majitel = majitel
        self.zustatek = zustatek

    def vloz(self, castka):
        self.zustatek += castka

    def vyber(self, castka):
        self.zustatek -= castka

    def stav_uctu(self):
        return f"Zustatek uctu je {self.zustatek} Kc."
    
    def prevod(self, ucet, castka):
        #self.zustatek -= castka
        #ucet.zustatek += castka
        self.vyber(castka)
        ucet.vloz(castka)
class Clovek:
    def __init__(self, jmeno, prijmeni, datum_narozeni, rodne_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.datum_narozeni = datum_narozeni
        self.__rodne_cislo = rodne_cislo

    def get_rodne_cislo(self):
        return self.__rodne_cislo

    def __cele_jmeno(self):
        return self.jmeno + " " + self.prijmeni
    
    def get_jmeno(self):
        return self.jmeno

    def get_cele_jmeno(self):
        return self.__cele_jmeno()

    def set_jmeno(self, jmeno):
        if type(jmeno) == str:# jestli jmeno je datovy typ str
            if not jmeno == "":
                self.jmeno = jmeno

        if not type(jmeno) == str:
            raise TypeError("jmeno není str")
        if jmeno == "":
            raise ValueError("jmeno má hodnotu \"\"")
        self.jmeno = jmeno
if __name__ == "__main__":
    c1 = Clovek("Karel", "Novák", "05-05-1998", 123)
    jmeno = c1.get_cele_jmeno()
    print(jmeno)
    print(type(c1))
    print(c1.get_rodne_cislo())
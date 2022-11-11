class Clovek:
    def __init__(self, jmeno, prijmeni, datum_narozeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.datum_narozeni = datum_narozeni

    def najist_se(self, druh_jidla):
        return f"{self.jmeno} se najedl. Měl {druh_jidla}"

    def jdi_ven(self):
        return "Prošel jsem se."

    @staticmethod
    def funkce(a, b):
        return a**b



if __name__ == "__main__":
    c1 = Clovek("Pepa", "Vomáčka", "1.1.1990")
    print(c1.jdi_ven())
    print(Clovek.funkce(1, 5))
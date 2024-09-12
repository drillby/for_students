class Person:
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek

    def plne_jmeno(self):
        return self.jmeno + " " + self.prijmeni
    
    def zestarnout(self):
        self.vek += 1
    
    @property
    def jmeno(self):
        return self._jmeno
    
    @jmeno.setter
    def jmeno(self, jmeno):
        if not isinstance(jmeno, str):
            raise TypeError("Jméno musí být řetězec")
        self._jmeno = jmeno

    @property
    def prijmeni(self):
        return self._prijmeni
    
    @prijmeni.setter
    def prijmeni(self, prijmeni):
        if not isinstance(prijmeni, str):
            raise TypeError("Příjmení musí být řetězec")
        self._prijmeni = prijmeni

    @property
    def vek(self):
        return self._vek
    
    @vek.setter
    def vek(self, vek):
        if not isinstance(vek, int):
            raise TypeError("Věk musí být celé číslo")
        if vek < 0:
            raise ValueError("Věk musí být nezáporné číslo")
        self._vek = vek

from __future__ import annotations

import math


class KomplexniCislo:
    def __init__(self, re: int, im: int):
        self.re = re
        self.im = im

    def __str__(self):
        return f"{self.re} {'+' if self.im >= 0 else '-'} {abs(self.im)}i"
        # to samé jako:
        # if self.im >= 0:
        #     return f"{self.re} + {self.im}i"
        # else:
        #     return f"{self.re} - {abs(self.im)}i"

    def secti(self, other: KomplexniCislo):
        if isinstance(other, KomplexniCislo):  # type(other) == KomplexniCislo
            return KomplexniCislo(self.re + other.re, self.im + other.im)
        elif isinstance(other, int):
            return KomplexniCislo(self.re + other, self.im)
        # return "Nelze sečíst s jiným typem"
        raise TypeError(f"Nelze sečíst {type(self)} s {type(other)}")

    def odecti(self, other: KomplexniCislo):
        if isinstance(other, KomplexniCislo):  # type(other) == KomplexniCislo
            return KomplexniCislo(self.re - other.re, self.im - other.im)
        # return "Nelze odečíst s jiným typem"
        raise TypeError(f"Nelze odečíst {type(self)} s {type(other)}")

    def vynasob(self, other: KomplexniCislo):
        if isinstance(other, KomplexniCislo):  # type(other) == KomplexniCislo
            return KomplexniCislo(self.re * other.im, self.im * other.re)
        raise TypeError(f"Nelze vynásobit {type(self)} s {type(other)}")

    def vydel(self, other: KomplexniCislo):
        if isinstance(other, KomplexniCislo):
            prevracene = KomplexniCislo(1 / other.re, 1 / other.im)
            return self.vynasob(prevracene)
        raise TypeError(f"Nelze vydělit {type(self)} s {type(other)}")

    def vydel_bez_desetin(self, other: KomplexniCislo):
        if isinstance(other, KomplexniCislo):
            prevracene = KomplexniCislo(
                math.floor(1 / other.re), math.floor(1 / other.im)
            )
            return self.vynasob(prevracene)
        raise TypeError(f"Nelze vydělit {type(self)} s {type(other)}")

    def __add__(self, other: KomplexniCislo):
        return self.secti(other)

    def __radd__(self, other: KomplexniCislo):
        return self.secti(other)

    def __sub__(self, other: KomplexniCislo):
        return self.odecti(other)
    
    def __rsub__(self, other: KomplexniCislo):
        return self.odecti(other)

    def __mul__(self, other: KomplexniCislo):
        return self.vynasob(other)
    
    def __rmul__(self, other: KomplexniCislo):
        return self.vynasob(other)

    def __truediv__(self, other: KomplexniCislo):
        return self.vydel(other)
    
    def __rtruediv__(self, other: KomplexniCislo):
        return self.vydel(other)

    def __floordiv__(self, other: KomplexniCislo):
        return self.vydel_bez_desetin(other)
    
    def __rfloordiv__(self, other: KomplexniCislo):
        return self.vydel_bez_desetin(other)
    
    def __abs__(): # absolutní hodnota
        ...

    def __eq__(): # rovnost
        ...

    def __ne__(): # nerovnost
        ...

    def __lt__(): # menší než
        ...

    def __le__(): # menší nebo rovno
        ...

if __name__ == "__main__":
    k1 = KomplexniCislo(10, 2)
    k2 = KomplexniCislo(-3, 4)
    k3 = k1.vydel(k2)
    k4 = k1 + 12
    # k4 = k1.__add__(12)
    k5 = 12 + k1
    # try:
    #     k5 = k5 = 12.__add__(k1)
    # except TypeError:
    #     k5 = k1.__add__(12)
    #     k5 = 12.__radd__(k1)

    # k5 = 12.__add__(k1)
    # k5 = 12.__radd__(k1)
    print("k1 je: ", k1)
    print("k2 je: ", k2)
    print("k3 je: ", k3)
    print("k4 je: ", k4)

import math

# 5 - 1i
class KomplexniCislo:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __add__(self, other): # self + other
        # sečíst KomplexniCislo, int, float
        if isinstance(other, int) or isinstance(other, float):
            return KomplexniCislo(self.real + other, self.im)
        else:
            return KomplexniCislo(self.real + other.real, self.im + other.im)

    def __radd__(self, other):
    # sečíst KomplexniCislo, int, float
        if isinstance(other, int) or isinstance(other, float):
            return KomplexniCislo(self.real + other, self.im)
        else:
            return KomplexniCislo(self.real + other.real, self.im + other.im)


    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.im ** 2)

    # odčítání
    def __sub__(self, other):
        ...

    def __rsub__(self, other):
        ...

    # násobení
    def __mul__(self, other):
        ...

    def __rmul__(self, other):
        ...

    # dělení
    def __truediv__(self, other): # //
        ...

    def __divmod__(self, other): # /
        ...

    def __str__(self):
        return f"{self.real} {'+' if self.im >=0 else '-'} {abs(self.im)}i"

    @property
    def velikost(self):
        return math.sqrt(self.real ** 2 + self.im ** 2)

    def secti(self, other):
        # sečíst KomplexniCislo, int, float
        if isinstance(other, int) or isinstance(other, float):
            return KomplexniCislo(self.real + other, self.im)
        else:
            return KomplexniCislo(self.real + other.real, self.im + other.im)

    def odcitani(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return KomplexniCislo(self.real - other, self.im)
        else:
            return KomplexniCislo(self.real - other.real, self.im - other.im)

    def nasobeni(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return KomplexniCislo(self.real * other, self.im * other)
        else:
            return  KomplexniCislo(self.real*other.real - self.im * other.im, self.real*other.real - self.im * other.im)

    # špatně
    def deleni(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                raise ValueError("Nelze dělit nulou")
            return KomplexniCislo(self.real/other, self.im/other)
        else:
            return  KomplexniCislo(self.real/other.real - self.im / other.im, self.real/other.real - self.im / other.im)


if __name__ == "__main__":
    K1 = KomplexniCislo(5, 2) # 5 + 2i
    K2 = KomplexniCislo(3, -2)
    C1 = K1.secti(K2)
    # 5 + 2i == 5 + 5i
    #print(C1)

    K3 = K1.nasobeni(2)
    print(K3)

    # K4 = K2.deleni(2)
    print(type(K3))
    K5 = KomplexniCislo(-2, -8)
    print(K5)
    print(K5.velikost)

    K6 = K1 + K2
    print(K6)


    K1 + 3
    #K1.__add__(3)

    print(3+K1)
    #3.__add__(K1)

    print(K1.velikost)
    print(abs(K1))

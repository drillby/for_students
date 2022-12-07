a = 25 # 'a' má hodnotu 25
a == 25 # zkoumámí hodnoty

if a >= 25: # a >= 25 == True
    print(True)
else:
    print(False)

# >, <, >=, <=, ==

b = "text"

if b == "text":
    print(True)
else:
    print(False)

cislo_1 = 25
cislo_2 = 8

cislo_3 = cislo_1 + cislo_2
print(cislo_3)

cislo_3 = cislo_1 - cislo_2
print(cislo_3)

cislo_3 = cislo_1 * cislo_2
print(cislo_3)

cislo_3 = cislo_1 / cislo_2
print(cislo_3)

cislo_3 = cislo_1 // cislo_2 # celočíselné dělení
print(cislo_3)

cislo_3 = cislo_1 ** cislo_2 # mocnění
print(cislo_3)

cislo_3 = cislo_1 % cislo_2 # zbytek po celočíselném dělení
print(cislo_3)

cislo_4 = 100
cislo_4 = cislo_4 + 5
print(cislo_4)

cislo_4 += 5
cislo_4 /= 5
cislo_4 *= 5

z = 98

if z != 98: # logická negace
    print(True)
else:
    print(False)

param_1 = input("Zadej číslo 1: ")
param_2 = int(input("Zadej číslo 2: "))
pocetni_operace = input("Zadej početní operaci: ")

param_1 = int(param_1)

if pocetni_operace == "+":
    print(param_1 + param_2)
elif pocetni_operace == "-":
    print(param_1 - param_2)
elif pocetni_operace == "*":
    print(param_1 * param_2)
elif pocetni_operace == "/":
    print(param_1 / param_2)




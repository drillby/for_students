a = 56

# pokud a je menší než 5
if a < 5:
    print(a)
# v každém jinem případě
else:
    print("Ahoj")

# if ...
# if ...
# if ...

b = 2

# použití elif bloků
# pokud bude splněna podmínka, Python zbývající elif-y nekontroluje
if b == 0:
    print("nula")
elif b == 1:
    print("jedna")
elif b == 2:
    print("dva")
else:
    print("jiná hodnota")

# vnoření podmínek
if b == 2:
    if a > 10:
        print(True)

# nahrazení dvou podmínek jednou pomocí logického "and"¨
# podmínka je splněna pokud všechny části jsou vyhodnoceny jako True
if b == 2 and a > 10:
    print("AND")

# podmínka je splněna pokud alespoň jedna část je vyhodnocena jako True
if b == 0 or a > 10:
    print("OR")

c = "text"

# spojování logických operátorů
# "and" má přednost před "or"
if (a < 10 and b == 2) or c == "text":
    print("spněno")

# podmínka jako proměnná
podminka = (a < 10 and b == 2) or c == "aaa"
print(type(podminka))

if podminka: # if podminka == True
    print(True)

if not podminka:
    print(False)

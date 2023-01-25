import random

pole = []
for cislo in range(10):
    if cislo % 2 == 0:
        pole.append(cislo)

print(pole)


for idx in range(len(pole)):
    print(pole[idx])


for klic in pole:
    print(klic)
print("\n")
a = 0
while a < 10:
    print(a)
    a += 1

b = 0
while b < len(pole):
    print(pole[b])
    b += 1

nah_cislo = random.randint(0, 100)
while nah_cislo != 24:
    print(nah_cislo)
    nah_cislo = random.randint(0, 100)

print("\n")
for cislo in range(10):
    print(cislo)
    if cislo == 4:
        break


for cislo in range(10):
    if cislo == 4:
        continue
    print(cislo)
print("\n")


user_input = [1, 2, 3, 58, "text", -9, 46]
vysledek = 0
for cislo in user_input:
    if not isinstance(cislo, int):
        continue
    vysledek += cislo

print(vysledek)

slovnik = {
    "jedna": 1,
    "dva": 2
}

for klic, hodnota in slovnik:
    print(klic, hodnota)
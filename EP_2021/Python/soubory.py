soubor = open("soubor.txt", "r", encoding="utf-8")
print(soubor.readlines())
soubor.close()

with open("soubor.txt", "r", encoding="utf-8") as soubor:
    text = soubor.readlines()
    for radek in text:
        print(type(radek))


with open("soubor.txt", "w", encoding="utf-8") as soubor:
    soubor.write("Teď zapisuji do souboru")

with open("soubor_2.txt", "w", encoding="utf-8") as soubor:
    soubor.write("Teď zapisuji do souboru")


import random
 
# The limit for the extended ASCII Character set
MAX_LIMIT = 255
 
def random_str():
    random_string = ''
    for _ in range(10):
        random_integer = random.randint(0, MAX_LIMIT)
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    return random_string
chci_zapsat = []
for _ in range(10):
    chci_zapsat.append(random_str())

with open("soubor.txt", "a", encoding="utf-8") as soubor:
    for radek in chci_zapsat:
        soubor.write(radek+"\n")


with open("soubor.txt", "r", encoding="utf-8") as soubor:
    radek = soubor.seek(3)
    print(radek)


with open("cat.jpg", "rb") as soubor:
    print(soubor.readlines())

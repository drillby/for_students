import math

def nazev(param_1):
    print(param_1)

# nazev(123)

def kvadraticka_rovnice(a, b, c):
    if a == 0:
        return
    
    dis = b**2 - 4 * a * c

    if dis < 0:
        return
    
    x1 = (-b + math.sqrt(dis)) / 2 * a
    x2 = (-b - math.sqrt(dis)) / 2 * a

    return x1, x2


vysledek = kvadraticka_rovnice(8, 3, -2)
# print(vysledek)

x1, x2 = kvadraticka_rovnice(8, 3, -2)
print(x1)
print(x2)
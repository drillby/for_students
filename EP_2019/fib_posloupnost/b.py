def fibi_pygame(n: int):
    # nový prvek = součet dvou předchozích
    # začátek posloupnosti 0, 1
    if n <= 0:
        raise ValueError("n musí být větší než 0")

    stary = 0
    novy = 1

    if n == 1 or n == 2:
        return stary, novy

    for _ in range(2, n+1):
        # nová hodnota "stary" = puvodní hodnota "novy"
        # nová hodnota "novy" = součet "novy" a "stary"
        stary, novy = novy, novy + stary
    return stary, novy


print(fibi_pygame(5))
# 8
# fibi_pygame(1)
# fibi_pygame(2)
# fibi_pygame(3)
# ...
# fibi_pygame(8)

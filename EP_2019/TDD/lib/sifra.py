def ces_sifra(text, shift):
    if type(text) != str:
        raise TypeError
    # převedeme text na velká písmena
    text = text.upper()

    # vytvoříme seznam znaků, které budeme používat pro šifrování
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # vytvoříme proměnnou pro ukládání šifrovaného textu
    encrypted_text = ''

    # projdeme všechny znaky v textu
    for ch in text:
        if ch in alphabet:  # pokud je znak v abecedě, přidáme ho k šifrovanému textu s posunutím
            idx = alphabet.index(ch)
            encrypted_text += alphabet[(idx + shift) % 26]
        else:  # jinak přidáme znak beze změny
            encrypted_text += ch

    return encrypted_text



def quick_sort(arr):
    if len(arr) <= 1:  # pokud má seznam délku menší než 1, není třeba řadit
        return arr

    for prvek in arr:
        if type(prvek) != int:
            raise TypeError

    pivot = arr[len(arr) // 2]  # vybereme pivot (prostřední prvek)
    left = [x for x in arr if x < pivot]  # vytvoříme seznam s hodnotami menšími než pivot
    middle = [x for x in arr if x == pivot]  # vytvoříme seznam s hodnotami rovnými pivotu
    right = [x for x in arr if x > pivot]  # vytvoříme seznam s hodnotami většími než pivot

    # rekurzivně zavoláme quick_sort() pro všechny tři seznamy a sloučíme je zpět do seřazeného seznamu
    return quick_sort(left) + middle + quick_sort(right)

# například pro seznam [3, 6, 8, 2, 1, 4] bychom mohli zavolat quick_sort([3, 6, 8, 2, 1, 4])